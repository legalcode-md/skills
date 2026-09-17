# Tracing Gold-Plating in Icelandic EEA-Implementing Legislation: A Source-Level Reference

> Companion reference for the `legalcode-anti-gold-plating-is` skill. This is the operational guide for walking an Icelandic statutory provision back through the legislative record to its EU/EEA origin and determining whether (and where) gold-plating was introduced.

---

## 1. Alþingi Document Taxonomy

The Icelandic parliament (Alþingi) treats each legislative initiative as a **mál** (matter / case). A mál carries one **mál number** (mnr) per legislative session (**löggjafarþing**, abbreviated ltg or lögþ.). Inside a mál live one or more **þingskjöl** (parliamentary documents, abbreviated þskj.), each with its own running number that resets each session. The first document of any mál is the foundational instrument (the bill itself, or the resolution proposal). All subsequent documents — committee reports, amendments, the final enacted text — accumulate under the same mnr.

### 1.1 Pre-Introduction Phase (executive)

| Icelandic                  | English                                | Where it lives                                   | Gold-plating signal                                                                                                                                                                                                                                |
| -------------------------- | -------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Áform um lagasetningu**  | Legislative plan / pre-bill notice     | samradsgatt.island.is                            | First public artefact. Mentions whether the topic implements an EES gerð. An EES bill that does not appear here at all is a procedural red flag.                                                                                                   |
| **Frummat á áhrifum**      | Preliminary impact assessment          | samradsgatt.island.is                            | Should quantify burdens. If absent or pro-forma when implementing a directive, gold-plating is harder to detect and more likely to slip through.                                                                                                   |
| **Drög að frumvarpi**      | Draft bill                             | samradsgatt.island.is                            | The **only** version of the text that often shows the _original_ ministry intent before stakeholder pressure trims or expands it. Compare drög ↔ introduced frumvarp to detect last-minute additions.                                              |
| **Samanburðartafla**       | Transposition / comparison table       | samradsgatt.island.is or as appendix to frumvarp | **The single most important gold-plating artefact.** Should map each Icelandic article to the corresponding directive article. Required by the post-2024 task-force reforms. Gaps, blanks, or "ekki á við" rows often mark gold-plated provisions. |
| **Umsagnir í samráðsgátt** | Pre-introduction stakeholder responses | samradsgatt.island.is                            | Industry bodies (SA, SFF, SVÞ, Viðskiptaráð) routinely flag gold-plating here. These responses are public, dated, often signed PDFs.                                                                                                               |

### 1.2 Alþingi Phase

| Icelandic                              | English                              | Document type                                           | Gold-plating signal                                                                                                                                                                                                                                                               |
| -------------------------------------- | ------------------------------------ | ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Frumvarp til laga**                  | Bill                                 | First þskj. in the mál                                  | The operative text. Compare wording to authentic Icelandic directive in EES-viðbætir.                                                                                                                                                                                             |
| **Greinargerð**                        | Explanatory memorandum               | Appended to frumvarp, same þskj.                        | Since 2017, the unified term. Holds the conformity declaration.                                                                                                                                                                                                                   |
| **Athugasemdir við einstakar greinar** | Article-by-article notes             | Within greinargerð (final section)                      | **CRITICAL.** This is where the drafter explains _each_ article. The phrase to look for is "Greinin felur í sér innleiðingu á X. gr. tilskipunar nr. X/X/ESB." Absence of such a citation against an article in an otherwise EEA-implementing bill is a strong gold-plating tell. |
| **Mat á áhrifum / kostnaðarmat**       | Impact / cost assessment             | Section of greinargerð, sometimes a separate fylgiskjal | When stricter-than-directive choices have measurable cost, this section should justify them. Bare boilerplate = suspect.                                                                                                                                                          |
| **Umsagnir (Alþingi phase)**           | Stakeholder submissions to committee | Filed as erindi (erindisskjöl) on the mál's ferill page | Distinct from samráðsgátt umsagnir. Same actors often re-file, sometimes with sharper criticism after seeing the introduced bill.                                                                                                                                                 |
| **Nefndarálit**                        | Committee report                     | New þskj. inside same mál                               | Issued by the standing committee. Majority and minority versions ("nefndarálit meiri hluta" / "minni hluta") often diverge on whether a gold-plated provision should be trimmed.                                                                                                  |
| **Framhaldsnefndarálit**               | Supplementary committee report       | New þskj.                                               | Issued when a committee reopens deliberation between 2nd and 3rd reading. Often the venue where a late amendment to a gold-plated clause appears.                                                                                                                                 |
| **Breytingartillögur**                 | Amendments                           | New þskj.                                               | Often accompany nefndarálit. Track these to see whether stakeholder warnings led to actual trimming.                                                                                                                                                                              |
| **Framsöguræða**                       | Introductory speech                  | Transcript in B-deild umræður                           | First-reading speech by the minister. Sometimes explicitly states "við gengum aðeins lengra en lágmark tilskipunarinnar" — direct admission of gold-plating.                                                                                                                      |
| **1./2./3. umræða**                    | First / second / third readings      | B-deild umræður                                         | A bill needs three readings. Articles are debated individually only at 2nd reading, when amendments are also voted.                                                                                                                                                               |
| **Atkvæðagreiðsla**                    | Vote record                          | Listed on ferill page                                   | Per-article and per-amendment votes recorded. Useful when a gold-plated provision survives despite a close vote.                                                                                                                                                                  |
| **Lög nr. X/ÁÁÁÁ**                     | Enacted act                          | Final þskj. ("lög í heild") + A-deild Stjórnartíðinda   | The authoritative text.                                                                                                                                                                                                                                                           |
| **Reglugerð**                          | Subsequent regulation                | B-deild Stjórnartíðinda → Reglugerðasafn                | Ministers issue these under enabling clauses of the lög. Gold-plating frequently lives here, beyond parliamentary scrutiny.                                                                                                                                                       |

### 1.3 Þingskjöl Numbering — the URL Algebra

- **þskj.** runs sequentially within a löggjafarþing from 1.
- **mnr** (mál numbering) runs sequentially within a löggjafarþing from 1.
- Each mál has one mnr but many þskj.

URL grammar on althingi.is:

- HTML of a document: `https://www.althingi.is/altext/{ltg}/s/{NNNN}.html` (þskj. zero-padded to 4 digits)
- PDF: `https://www.althingi.is/altext/pdf/{ltg}/s/{NNNN}.pdf`
- DOCX: `https://www.althingi.is/altext/doc/{ltg}/s/{NNNN}.docx`
- Mál ferill: `https://www.althingi.is/dba-bin/ferill.pl?ltg={ltg}&mnr={mnr}` or the modern form `https://www.althingi.is/thingstorf/thingmalalistar-eftir-thingum/ferill/{ltg}/{mnr}/`
- Mál summary: `https://www.althingi.is/thingstorf/listar-yfir-mal-a-yfirstandandi-thingi/samantektir-um-thingmal/?ltg={ltg}&mnr={mnr}`
- Erindi: `https://www.althingi.is/altext/erindi/{ltg}/{ltg}-{N}.pdf`

---

## 2. Access — Where to Fetch Each Document

### 2.1 Primary: Legalcode MCP `search_pre_laws` (jurisdiction: IS)

The Legalcode MCP exposes a purpose-built tool `search_pre_laws` for Icelandic pre-law materials. Key parameters:

| Parameter                    | Purpose                                | Example value                                                             |
| ---------------------------- | -------------------------------------- | ------------------------------------------------------------------------- |
| `jurisdiction`               | Required. ISO code.                    | `IS`                                                                      |
| `session`                    | Alþingi legislative session            | `148` (for 2017–2018)                                                     |
| `matterNumber`               | Alþingi mál number                     | `622`                                                                     |
| `documentNumber`             | Þingskjal number                       | `1029`                                                                    |
| `flowKey`                    | Exact pre-law flow ID                  | (from previous result metadata)                                           |
| `lawKey`                     | Linked enacted law key                 | (from law-result metadata)                                                |
| `relatedNumberYear`          | Filter flows related to a specific law | `90/2018`                                                                 |
| `role`                       | Document role filter                   | `ORIGINAL_BILL`, `PARLIAMENTARY_DOCUMENT`, `SUBMITTED_OPINION`, `SUMMARY` |
| `status`                     | Pre-law flow status                    | `INTRODUCED`, `IN_COMMITTEE`, `ENACTED`                                   |
| `stage`                      | Procedural stage (staða/umræða)        | `2. umræða`                                                               |
| `enacted`                    | Boolean — bill became law              | `true`                                                                    |
| `hasOriginalBill`            | Filter to flows with frumvarp          | `true`                                                                    |
| `hasParliamentaryDocuments`  | Filter to flows with þingskjöl         | `true`                                                                    |
| `hasSubmittedOpinions`       | Filter to flows with umsagnir          | `true`                                                                    |
| `hasSummary`                 | Filter to flows with summary           | `true`                                                                    |
| `proposer`                   | Bill originator                        | minister/committee/MP name                                                |
| `presenter`                  | Þingskjal presenter                    | flutningsmaður name                                                       |
| `submitter`                  | Umsögn sender                          | "SA" / "Viðskiptaráð" / "SFF"                                             |
| `recipient`                  | Umsögn recipient                       | committee name                                                            |
| `query`                      | Full-text across all doc types         | `"gengur lengra"`                                                         |
| `originalBillQuery`          | Full-text inside frumvarp only         | `"umfram lágmark"`                                                        |
| `parliamentaryDocumentQuery` | Full-text inside þingskjöl only        | `"gullhúðun"`                                                             |
| `submittedOpinionQuery`      | Full-text inside umsagnir only         | `"umfram tilskipun"`                                                      |
| `summaryQuery`               | Full-text inside Alþingi summary       | `"innleiðing"`                                                            |
| `dateFrom` / `dateTo`        | Activity date range                    | `2018-01-01` / `2018-12-31`                                               |
| `enactedFrom` / `enactedTo`  | Enactment date range                   | as above                                                                  |
| `sort`                       | `relevance` / `date` / `title`         |                                                                           |
| `limit`                      | 1–50                                   | `50` for full pre-law sweep                                               |

**Companion**: `analyze_pre_laws` returns counts, top buckets, date histograms. Useful for "show me every umsögn submitter that flagged gold-plating in 2020–2024".

### 2.2 althingi.is (HTML fallback)

- Mál pages list every þskj., every speech, every vote, every erindi.
- Site exposes HTML, PDF, and DOCX renderings.
- **No official public REST/JSON API** for parliamentary documents. Closest open-data assets: [althingi-net/lagasafn-xml](https://github.com/althingi-net/lagasafn-xml) (consolidated lawbook) and the [CLARIN Althingi Parliamentary Speech corpus](https://clarin.is/en/resources/althingisgognin/) (transcripts 2005–2016).
- Programmatic access via deterministic URL templates (§1.3) plus HTML parsing.

### 2.3 samradsgatt.island.is

- All ministry pre-bills and drafts. Mál numbered as **S-N/YYYY**.
- Pretty URL: `https://island.is/samradsgatt/mal/{caseId}` (caseId is internal numeric)
- Older slug: `https://samradsgatt.island.is/oll-mal/$Cases/Details/?id={caseId}`
- **Undocumented document API**: `https://samradapi.island.is/api/Documents/{GUID}` (observed in production). Harvest GUIDs from the rendered mál page.
- Comments published immediately by default; commenter may request anonymity or delayed publication. Minimum consultation window 2–4 weeks; results summarised within ~3 months.

### 2.4 island.is / Stjórnartíðindi / Reglugerðasafn

- **Stjórnartíðindi**: [island.is/stjornartidindi](https://island.is/stjornartidindi). Three divisions:
  - **A-deild**: laws (lög nr. X/ÁÁÁÁ)
  - **B-deild**: regulations (reglugerðir) and fee schedules (gjaldskrár)
  - **C-deild**: notices, including announcements of EU/EEA acts being implemented
- **Reglugerðasafn**: `https://island.is/reglugerdir/nr/{NNNN-YYYY}` for canonical permalink (e.g. `/reglugerdir/nr/0601-2018`).

### 2.5 EES-viðbætir við Stjórnartíðindi Evrópusambandsins

- The **authentic Icelandic translation** of every EU act incorporated into the EEA Agreement.
- PDFs on efta.int — paths like `https://www.efta.int/sites/default/files/documents/legal-texts/eea/other-legal-documents/adopted-joint-committee-decisions/{YEAR}%20-%20Icelandic/{NNN}-{YY}i.pdf`
- Individual translated acts: `https://www.efta.int/sites/default/files/media/documents/legal-texts/eea/other-legal-documents/translated-acts/icelandic/i{CELEX}.pdf`
- These are the **only authentic Icelandic versions** of EU acts. The Icelandic enacted statute must be compared to them — _not_ to the English EUR-Lex version — to detect divergence.

### 2.6 EFTA / ESA / EFTA Court

- **EEA Joint Committee Decisions (JCDs)**: [efta.int/legal-text/eea-agreement-1327](https://www.efta.int/legal-text/eea-agreement-1327)
- **ESA Internal Market Scoreboard**: [eftasurv.int](https://www.eftasurv.int/)
- **ESA infringement letters and reasoned opinions**: ESA newsroom
- **EFTA Court**: [eftacourt.int](https://eftacourt.int/)

### 2.7 EEA-related flagging at Alþingi

- Government bills implementing EEA acts pass through **utanríkismálanefnd** (Foreign Affairs Committee) for EEA-conformity scrutiny, in addition to the sectoral standing committee.
- Iceland's parliament approved the EEA Agreement itself by **lög nr. 2/1993** — the constitutional anchor for all subsequent transposition.

### 2.8 Transposition Tables — where they appear

- Pre-2024: rarely published, sometimes appended to the bill as a fylgiskjal.
- Post-Jan 2024 task force reforms: **required** as a separate document accompanying the bill from samráðsgátt phase onward, and updated through committee stages.

---

## 3. The Tracing Workflow: Article → Pre-Law → Directive (10-Step Protocol)

Use this as the canonical protocol when starting from any single section of an Icelandic implementing act.

### Step 1 — Find the enacting bill

- Look up the law by number on [island.is/stjornartidindi](https://island.is/stjornartidindi). Published lög will name the originating frumvarp.
- Cross-reference on althingi.is by searching by law number; mál ferill page gives ltg + mnr + every þskj.
- **MCP**: `search_pre_laws` with `relatedNumberYear: "90/2018"` and `role: "ORIGINAL_BILL"`.

### Step 2 — Read the article-specific note

- Open the originating þskj. (the introduced frumvarp), scroll to "**Athugasemdir við einstakar greinar**" (sometimes "**Um einstakar greinar frumvarpsins**").
- Locate the heading "**Um 3. gr.**" — that paragraph is your tracing anchor.
- **MCP**: `search_pre_laws` with `originalBillQuery: "Um 3. gr."` and `relatedNumberYear: "90/2018"`.

### Step 3 — Extract the directive citation

- Well-formed pattern: "_Greinin felur í sér innleiðingu á X. gr. tilskipunar Evrópuþingsins og ráðsins (ESB) nr. YYYY/NN/ESB frá DD. mánuður ÁÁÁÁ um …_"
- Capture: directive number + article + cited recitals (if any).
- **No directive citation against an article in an otherwise EES-implementing bill** = prima facie **silent gold-plating** — flag it and continue.

### Step 4 — Consult the samanburðartafla

- If the bill has one (always for post-Jan 2024 bills, sometimes earlier), find the row for the article.
- Right-hand column should map to a directive article. Look for explicit "_Gullhúðun_", "_Gengur lengra en tilskipunin krefst_", "_Nýtir heimild aðildarríkja_", or "_Án samsvörunar í tilskipuninni_" notations.

### Step 5 — Sweep umsagnir for stakeholder flags

- Visit samráðsgátt page for áform/drög, then Alþingi mál ferill for committee-phase erindi.
- Frequent gold-plating callers: **Samtök atvinnulífsins (SA)**, **Viðskiptaráð**, **Samtök fjármálafyrirtækja (SFF)**, **Samtök verslunar og þjónustu (SVÞ)**, **Samtök iðnaðarins (SI)**, **Félag atvinnurekenda (FA)**.
- **MCP**: `search_pre_laws` with `role: "SUBMITTED_OPINION"`, `submitter: "Viðskiptaráð"`, `relatedNumberYear: "90/2018"`, `submittedOpinionQuery: "umfram lágmark"`.

### Step 6 — Check nefndarálit and breytingartillögur

- Mál ferill page lists the committee report(s) (often two: meiri hluti / minni hluti).
- Did the committee notice the gold-plating? Did breytingartillögur trim it? If amendments adopted, the **lög í heild** þskj. will reflect final wording.
- **MCP**: `search_pre_laws` with `relatedNumberYear: "90/2018"`, `role: "PARLIAMENTARY_DOCUMENT"`, `parliamentaryDocumentQuery: "nefndarálit"`.

### Step 7 — Cross-check 2./3. umræða for substantive changes

- B-deild speeches under the mál. At 2. umræða, individual articles are debated and votes recorded on each.
- Search transcripts for the article number, for the minister's name (framsöguræða), and for phrases like "gengur lengra" or "tilskipunin krefst þess ekki".

### Step 8 — Compare to the authentic Icelandic directive

- Locate the directive in **EES-viðbætir** (§2.5). This is the binding Icelandic-language version.
- Diff the cited article against the Icelandic statute. Differences that _expand_ scope, _lower thresholds_, _add categories_, _increase penalties_, or _remove exemptions_ indicate gold-plating.

### Step 9 — Check the EEA Joint Committee Decision

- Each EU act enters EEA through a JCD published in the EES-section/Supplement of the OJ.
- JCD may contain **adaptations** specific to EFTA EEA states. Verify whether what looks like Icelandic gold-plating is actually mandated by JCD adaptation.
- If parliamentary approval required, look for the constitutional-reservation note — the parallel þingsályktunartillaga may itself add conditions.

### Step 10 (residual) — Check the reglugerð

- If the lög delegates detail to a minister, fetch the implementing reglugerð from Reglugerðasafn. Gold-plating frequently lives at this sub-statutory tier, beyond the Alþingi record.

---

## 4. Diagnostic Phrases in Greinargerð

Treat the explanatory memorandum as the primary corpus. Search for these phrases verbatim; their presence (or pointed absence) signals gold-plating.

### 4.1 Pure-transposition language (signals NO gold-plating, if accurate)

- "_Frumvarpið felur í sér innleiðingu á tilskipun nr. YYYY/NN/ESB._"
- "_Í samræmi við lágmarksákvæði tilskipunarinnar._"
- "_Innleiðing er með umritunaraðferð._" / "_… með tilvísunaraðferð._"
- "_Hér er um hreina innleiðingu að ræða._" — "Pure transposition" (the 2018 procedural-reform target).

### 4.2 Discretion-use language (legitimate gold-plating)

- "_Nýtir heimild aðildarríkja til að…_" — Uses Member State discretion to…
- "_Tilskipunin heimilar að gengið sé lengra og hér er sú heimild nýtt._"
- "_Gengur lengra en tilskipunin krefst._" — Explicit admission. **Post-Jan 2024 handbook requires this admission to be paired with justification.**

### 4.3 Soft-signal / euphemistic language (often hides gold-plating)

- "_Byggir á gildandi rétti._" — Often masks retention of a stricter pre-EEA regime that should have been relaxed.
- "_Skv. íslenskri lagahefð._" — Per Icelandic legal tradition.
- "_Að höfðu samráði við hagsmunaaðila þótti rétt að…_" — Typical preamble to a non-directive addition.
- "_Viðurlög skv. íslenskri löggjöf._" — Sanctions per Icelandic law.
- "_Til samræmis við markmið laganna._"
- "_Til að tryggja skilvirka framkvæmd._"

### 4.4 Procedural / EEA-process phrases

- "_Frumvarpið er samið í samráði við utanríkisráðuneytið._" — Drafted with MFA (EEA-conformity-reviewed).
- "_Ákvörðun sameiginlegu EES-nefndarinnar nr. NN/ÁÁÁÁ._" — JCD reference.
- "_Stjórnskipulegum fyrirvara hefur verið aflétt._" — Constitutional reservation lifted.

### 4.5 Silent gold-plating

**No directive citation against an article inside an otherwise EEA-implementing bill** is the strongest signal. The 2024 review found ~50% of bills inadequately flagged gold-plating; in those cases the only diagnostic is the absence of a tilskipun cite against a substantive article.

---

## 5. The EEA Twist

Iceland is **not in the EU**. It is bound by EU acquis only via the EEA Agreement, with structural consequences for gold-plating analysis.

### 5.1 Two-pillar architecture

- EEA runs on a **two-pillar structure**: EU pillar (Commission, ECJ) + EFTA pillar (ESA, EFTA Court). Iceland sits in the EFTA pillar.
- An EU directive does not automatically apply to Iceland. It must be screened for **EEA relevance**, then incorporated by a **Joint Committee Decision (JCD)**, then transposed into Icelandic law.

### 5.2 The Joint Committee Decision and the six-month rule

- **EEA Joint Committee** decides by consensus between EU and EFTA EEA states acting as one. 6–8 meetings/year.
- Where a JCD requires parliamentary approval in any of the three EFTA EEA states, that state may invoke a **constitutional reservation**. It then has **six months** to obtain Alþingi approval.
- Iceland's approval typically takes the form of a þingsályktunartillaga authorising lifting of the constitutional reservation, on the recommendation of utanríkismálanefnd.

### 5.3 Protocol 35: no direct effect, no supremacy

- Under **Protocol 35**, EFTA EEA states are _not_ obliged to confer direct effect or supremacy on EEA rules, but must introduce a statutory rule giving EEA rules precedence in cases of conflict.
- The EFTA Court has held that JCDs are _not_ directly effective at the national level qua EEA law.
- **Implication for gold-plating**: because individuals cannot directly invoke an EEA directive against an inconsistent stricter Icelandic statute, the political cost of gold-plating is lower. Alþingi can over-implement without ECJ pushback; only ESA infringement proceedings provide pressure.

### 5.4 EFTA Surveillance Authority (ESA) — detection source

- ESA monitors transposition via the **Internal Market Scoreboard** and infringement proceedings: letter of formal notice → reasoned opinion → referral to EFTA Court.
- ESA letters are public on eftasurv.int and corroborate when gold-plating later becomes a complaint subject — but ESA chiefly polices **under-** rather than **over-** transposition.

### 5.5 EFTA Court case law

- Cases at [eftacourt.int](https://eftacourt.int/). Landmark: **E-16/11 Icesave** (Deposit Guarantee Directive). Recent: **E-10/25** and **E-16/25** ESA v Iceland.
- EFTA Court generally follows ECJ on min-vs-max harmonisation. In max-harm areas (parts of consumer-credit and securities law), any stricter Icelandic rule is **unlawful gold-plating** ("ólögmæt gullhúðun").

### 5.6 Utanríkisráðuneytið's role

- Coordinates EEA notifications, EFTA Working Group representation, and conformity review of draft Icelandic bills implementing JCDs.
- Following the **January 2024 task force**, MFA in concert with PM's Office, Justice Ministry, and Finance Ministry, updates the bill-preparation handbook, EEA guidelines, and standard government forms to require **explicit gold-plating disclosure**.

### 5.7 The Handbók and the conformity declaration

- 2007 _Handbók um undirbúning og frágang lagafrumvarpa_ instructs drafters to trace international obligations and assess conformity.
- _Handbók um EES-skuldbindingar_ hosted at MFA.
- Government regulation **24 February 2023** requires: announcement of legislative plans, identification of relevant international commitments, cross-ministry consultation, documentation of conformity.

---

## 6. Citation Format

The conventional citation system in Icelandic legal writing follows an **OSCOLA-adapted** local standard.

### 6.1 Laws and regulations

- Full: `Heiti laga nr. XX/YYYY` — e.g. _Almenn hegningarlög nr. 19/1940_
- With pinpoint: `Lög um almannatryggingar nr. 100/2007, 5. gr., mgr. 2`

### 6.2 Parliamentary documents (web version, post-2009)

- Full: `Alþt. {YYYY-YY}, A-deild, þskj. {NNN} – {mnr}. mál`
- With pinpoint: `Alþt. 2010-2011, A-deild, þskj. 82 – 78. mál, athugasemdir við 5. gr., mgr. 7`
- Example: `Athugasemdir við 3. gr. frumvarps til laga nr. 90/2018, Alþt. 2017-2018, A-deild, þskj. 1029 – 622. mál, 148. lögþ.`

### 6.3 Speeches and debates (B-deild)

- Web: `Alþt. 2010-2011, B-deild, 78. mál, 43. fundur (Mörður Árnason) skoðað 21. október 2011`

### 6.4 Umsögn

- Alþingi-phase: `Umsögn {Author} um frumvarp til laga um {topic}, mál nr. {mnr}/{ltg}, dags. {DD. mánuður YYYY}`
- Samráðsgátt: `Umsögn {Author} í samráðsgátt stjórnvalda, mál nr. S-{N}/{YYYY}, dags. {date}`

### 6.5 EU/EEA acts

- `Tilskipun Evrópuþingsins og ráðsins (ESB) nr. YYYY/NN/ESB frá DD. mánuður ÁÁÁÁ um {subject}, OJ L NNN, dd.mm.yyyy, bls. NN.`
- For Icelandic authentic text: append `EES-viðbætir við Stjórnartíðindi ESB nr. NN/yy, dd.mm.yyyy, bls. NN.`

### 6.6 Joint Committee Decisions

- `Ákvörðun sameiginlegu EES-nefndarinnar nr. NN/YYYY frá DD. mánuður ÁÁÁÁ um breytingu á {Annex} við EES-samninginn.`

### 6.7 EFTA Court / ESA

- EFTA Court: `Mál E-{NN}/{YY} {Parties}, dómur frá DD. mánuður ÁÁÁÁ.`
- ESA: `Rökstutt álit ESA, mál nr. NNNNN, dags. DD. mánuður ÁÁÁÁ.`

---

## 7. Tooling Notes for the Skill

### 7.1 Suggested call pattern when the Legalcode MCP is available

| Tracing step                             | Primary tool                                                                                        | Fallback URL pattern                                 |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Find enacting lög by number              | `search_laws` (jurisdiction: IS)                                                                    | `https://island.is/stjornartidindi` + search         |
| Find pre-law flow                        | `search_pre_laws` with `relatedNumberYear`                                                          | mál ferill `/dba-bin/ferill.pl?ltg={ltg}&mnr={mnr}`  |
| Fetch frumvarp text                      | `search_pre_laws` with `role: ORIGINAL_BILL` + `fetch_source`                                       | `https://www.althingi.is/altext/{ltg}/s/{NNNN}.html` |
| Pull greinargerð / athugasemdir          | `search_pre_laws` with `originalBillQuery: "Um {N}. gr."`                                           | Same                                                 |
| Locate cited tilskipun                   | `search_laws` (jurisdiction: EU) + `fetch_source`                                                   | EUR-Lex                                              |
| Pull samanburðartafla                    | `search_pre_laws` with `originalBillQuery: "samanburðartafla"`                                      | Fylgiskjal links on mál ferill                       |
| Sweep umsagnir                           | `search_pre_laws` with `role: SUBMITTED_OPINION` + `submitter` / `submittedOpinionQuery`            | Mál ferill "Erindi" list + samradsgatt mál page      |
| Pull nefndarálit, breytingartillögur     | `search_pre_laws` with `role: PARLIAMENTARY_DOCUMENT` + `parliamentaryDocumentQuery: "nefndarálit"` | `/altext/{ltg}/s/{NNNN}.html`                        |
| Pull 1./2./3. umræða transcripts         | (likely no MCP coverage)                                                                            | Mál ferill umræður links                             |
| Compare to authentic Icelandic directive | (likely no MCP coverage)                                                                            | EES-viðbætir PDFs on efta.int                        |
| Check JCD                                | (likely no MCP coverage)                                                                            | efta.int/legal-text/eea-agreement                    |
| Check ESA / EFTA Court                   | `search_guidance` (jurisdiction: EU, agency: ESA); WebFetch                                         | eftasurv.int; eftacourt.int                          |

### 7.2 Where MCP coverage is thin → use WebFetch fallback

- **Umsagnir PDFs** (when not surfaced by MCP) — fetch from mál ferill or samradsgatt; for samráðsgátt documents the undocumented `https://samradapi.island.is/api/Documents/{GUID}` is fastest.
- **Samráðsgátt drafts** (pre-bill) — only on samradsgatt.island.is.
- **Speech transcripts / umræður** — fetch via althingi.is HTML.
- **EFTA / ESA / EFTA Court materials** — fetch from efta.int, eftasurv.int, eftacourt.int directly.
- **EES-viðbætir authentic Icelandic translations** — only on efta.int.

### 7.3 Skill heuristics

1. **Always start from the enacted lög number**, then walk up through mál → þskj. → directive → JCD.
2. **Always read the athugasemdir við einstakar greinar for the specific article first**. If no directive citation appears, treat the article as a gold-plating candidate.
3. **Always diff against the EES-viðbætir Icelandic text, never against EUR-Lex English** — translation choices can themselves shift scope.
4. **Always check the samanburðartafla last, not first** — useful but not always present; absence is itself an indicator on pre-2024 bills.
5. **Treat ESA letters as corroborating, not primary** — ESA mainly chases under-implementation.
6. **Cite to þskj. + pinpoint** ("athugasemdir við 3. gr., mgr. 2") — load-bearing citation form.

---

## 8. Bibliography

### Alþingi (primary)

- Alþingi front page — https://www.althingi.is/
- Standing Orders (English) — https://www.althingi.is/english/about-the-parliament/standing-orders-of-the-althingi-/
- Standing Committees — https://www.althingi.is/english/members-of-parliament/standing-committees-/
- Starfsreglur fyrir fastanefndir — https://www.althingi.is/um-althingi/upplysingar-um-althingi/reglur-settar-af-forsaetisnefnd-/fastanefndir/starfsreglur-fyrir-fastanefndir-althingis/
- Alþingistíðindi (structure) — https://www.althingi.is/thingstorf/leidbeiningar-og-yfirlit/althingistidindi/
- Tilvísanir í Alþingistíðindi — https://www.althingi.is/thingstorf/ymsar-leidbeiningar/tilvisanir-i-althingistidindi/
- Leiðbeiningar um umsagnir — https://www.althingi.is/thingnefndir/viltu-senda-umsogn/leidbeiningar-um-umsagnir-um-thingmal/

### Gold-plating — Icelandic sources

- Vísindavefurinn svar nr. 88538 — https://www.visindavefur.is/svar.php?id=88538
- Skýrsla 925/154 (Einarsdóttir review) — https://www.althingi.is/altext/154/s/0925.html
- Skýrsla starfshóps URN PDF (Jan 2024) — https://www.stjornarradid.is/library/02-Rit--skyrslur-og-skrar/URN/URN_Skyrsla_um_gullhudun_012024.pdf
- Þingmálasvar 757/156 — https://www.althingi.is/altext/156/s/0757.html
- Þingmálasvar 889/154 — https://www.althingi.is/altext/154/s/0889.html
- "Starfshópur um aðgerðir gegn gullhúðun" — https://www.stjornarradid.is/efst-a-baugi/frettir/stok-frett/2024/01/25/Starfshopur-um-adgerdir-gegn-gullhudun/
- Viðskiptaráð — https://vi.is/frettir/adgerdir-gegn-gullhudun
- Seðlabanki Íslands — https://sedlabanki.is/frettir-og-utgefid-efni/grein/gullhudun-loggjafar-a-fjarmalamarkadi
- SVÞ — https://svth.is/island-gengur-lengra-en-evropa-i-regluverki-um-peningathvaetti-svth-varar-vid-ohoflegu-eftirliti/
- SFF — https://www.sff.is/umsagnir/umsogn-sff-um-frumvarp-til-laga-um-varfaerniskrofur-til-verdbrefafyrirtaekja

### EEA / EFTA framework

- How EU Law becomes EEA Law — https://www.efta.int/eealaw
- EEA Decision Making — https://www.efta.int/eea-relations-eu/eea-decision-making
- EEA Joint Committee — https://www.efta.int/eea-relations-eu/eea-institutions-two-pillar-structure/eea-joint-committee
- Q&A about the EEA Agreement — https://www.efta.int/eea-relations-eu/qa-about-eea-agreement
- EFTA Surveillance Authority — https://www.eftasurv.int/
- EFTA Court — https://eftacourt.int/

### Stjórnarráðið

- Handbók um undirbúning og frágang lagafrumvarpa — https://www.stjornarradid.is/media/forsaetisraduneyti-media/media/utgefidefni/handbok_lagafrumvorp.pdf
- Handbók um EES-skuldbindingar — https://www.stjornarradid.is/media/utanrikisraduneyti-media/media/utgafa/handbokees_v.pdf
- Skrifstofa löggjafarmála — https://www.stjornarradid.is/raduneyti/domsmalaraduneytid/um-raduneytid-/skrifstofa-loggjafarmala/
- EES.is upplýsingaveitan — https://www.stjornarradid.is/verkefni/utanrikismal/evropusamvinna/ees-upplysingaveitan/

### Stjórnartíðindi / Reglugerðasafn

- Stjórnartíðindi — https://island.is/stjornartidindi
- Reglugerðasafn — https://island.is/reglugerdir?rn=hr

### Samráðsgátt

- Um Samráðsgátt — https://island.is/samradsgatt/um
- Öll mál — https://island.is/samradsgatt
- Document API (undocumented) — https://samradapi.island.is/api/Documents/{GUID}

### Citation guides

- RU OSCOLA-Íslenska — https://bokasafn.ru.is/oscola/islenska
- RU OSCOLA — Íslenskar frumheimildir — https://bokasafn.ru.is/c.php?g=988256&p=7272432
- RU Lögfræði — Alþingi guide — https://bokasafn.ru.is/logfraedi/althingi
- LoC Guide to Law Online — Iceland — https://guides.loc.gov/law-iceland

### Open data / tooling

- althingi-net/lagasafn-xml — https://github.com/althingi-net/lagasafn-xml
- CLARIN Althingi Parliamentary Speeches — https://clarin.is/en/resources/althingisgognin/
- apis.is — https://docs.apis.is/
