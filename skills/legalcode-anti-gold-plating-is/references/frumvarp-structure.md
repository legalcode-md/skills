# Bygging íslensks stjórnarfrumvarps — breytingafrumvarp

Reference for Stage 10 of the `legalcode-anti-gold-plating-is` skill. Defines the canonical structure of an Icelandic government amending bill (_breytingafrumvarp_ / _stjórnarfrumvarp_) and the standard amendment-text formulations used by Alþingi. Sources: lög nr. 55/1991 um þingsköp Alþingis (37. gr.), Reglur forsætisnefndar Alþingis um þinglega meðferð EES-mála (8. gr.), Samþykkt ríkisstjórnarinnar um undirbúning og frágang stjórnarfrumvarpa (13. gr.), and Handbók um undirbúning og frágang lagafrumvarpa (2007, forsætisráðuneytið). Cross-checked against þskj. 559, 153. lögþ. 2022–2023 (frumvarp → lög nr. 16/2023, breyting á lögum um persónuvernd) and þskj. 1029, 148. lögþ. 2017–2018 (frumvarp → lög nr. 90/2018).

---

## 1. Heildaruppbygging — overall structure

The bill is a single document in the following order:

1. **Heiti og flutningsmaður** (title + presenter)
2. **Lagatextinn** (the amending statutory text)
3. **Greinargerð** (explanatory memorandum)
4. **Athugasemdir við einstakar greinar frumvarpsins** (article-by-article notes)
5. **Fylgiskjöl** (annexes — samanburðartafla, mat á áhrifum, álitsgerðir)

No cover sheet, no executive summary at the top — the bill opens with the title and goes straight into the lagatextinn.

---

## 2. Heiti og flutningsmaður

Standard heading block (generic shape with placeholders):

```
Frumvarp til laga
um breytingu á lögum um {heiti laganna},
nr. {NN/YYYY} (samræming við {tilskipun | reglugerð | ákvörðun} (ESB) {YYYY/NN} — afnám gullhúðunar).

Frá {ráðherra heitir} ráðherra.   ← for stjórnarfrumvarp
eða
Flm.: {þingmaður(menn)}.            ← for þingmannafrumvarp
```

Worked example (lög 90/2018 ↔ GDPR):

```
Frumvarp til laga
um breytingu á lögum um persónuvernd og vinnslu persónuupplýsinga,
nr. 90/2018 (samræming við reglugerð (ESB) 2016/679 — afnám gullhúðunar).
```

The parenthetical short-title at the end of the heading describes the substantive purpose. For EEA-compliance bills the convention is `(samræming við [gerð])` or `(innleiðing [gerðar])`.

---

## 3. Lagatextinn — the amending statutory text

The amending text is split into kafla, one kafli per existing act being amended. Within each kafli, every article (`1. gr.`, `2. gr.` ...) makes one or more discrete amendments to the existing law. The very last article of the bill is the gildistökuákvæði.

### 3.1 Kafli structure

```
I. KAFLI
Breyting á lögum um {heiti laganna}, nr. {NN/YYYY}.

1. gr.
{amendment text}

2. gr.
{amendment text}
...
```

If a single bill amends multiple acts (common when removing gold-plating that has crept into related sectoral laws), add `II. KAFLI`, `III. KAFLI`, etc. Each is headed `Breyting á lögum um {...}, nr. {NN/YYYY}.`

### 3.2 Standard amendment-text formulations

Use these phrasings verbatim — Alþingi's standing committee secretariat expects exactly these forms.

| Operation                                             | Standard phrasing                                                                                |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Replace a whole paragraph                             | `1. mgr. X. gr. laganna orðast svo:` (then the new text on next line)                            |
| Replace a whole article                               | `X. gr. laganna orðast svo:`                                                                     |
| Delete a paragraph                                    | `1. mgr. X. gr. laganna fellur brott.`                                                           |
| Delete a whole article                                | `X. gr. laganna fellur brott.`                                                                   |
| Insert a new article after an existing one            | `Á eftir X. gr. laganna kemur ný grein, X. gr. a, svohljóðandi:`                                 |
| Insert a new paragraph after an existing one          | `Á eftir 1. mgr. X. gr. laganna kemur ný málsgrein, svohljóðandi:`                               |
| Insert a new paragraph at the beginning of an article | `Á undan 1. mgr. X. gr. laganna kemur ný málsgrein, svohljóðandi:`                               |
| Add text at end of paragraph                          | `Við 1. mgr. X. gr. laganna bætist nýr málsliður, svohljóðandi:`                                 |
| Replace specific words                                | `Í stað orðanna „{gamla orðalagið}" í 1. mgr. X. gr. laganna kemur: „{nýja orðalagið}"`          |
| Multiple amendments to one article                    | `Eftirfarandi breytingar verða á X. gr. laganna:` followed by lettered subitems `a.`, `b.`, `c.` |

### 3.3 The lettered-subitems pattern (most common for gold-plating remediation)

```
N. gr.
Eftirfarandi breytingar verða á X. gr. laganna:
a. 1. mgr. orðast svo:
   {new paragraph text}
b. Í stað orðanna „skal ávallt" í 2. mgr. kemur: „má, eftir því sem við á,".
c. 3. mgr. fellur brott.
d. Við bætist ný málsgrein, svohljóðandi:
   {new paragraph text}
```

### 3.4 Gildistökuákvæði — the standard closing article

Always the final article. Standard form:

```
N. gr.
Lög þessi öðlast gildi {dagsetning}.
```

Variants:

- Immediate: `Lög þessi öðlast þegar gildi.`
- Conditional on EES incorporation: `Lög þessi öðlast gildi þegar ákvörðun sameiginlegu EES-nefndarinnar nr. {NN/YYYY} hefur verið tekin upp í EES-samninginn og fullnægt er stjórnskipulegum skilyrðum.`
- Phased gildistaka: a numbered list of dates per article.

For a gold-plating-remediation bill the standard form is a fixed date 3–6 months out, giving ábyrgðaraðilar time to adjust.

---

## 4. Greinargerð — the explanatory memorandum

Six mandatory kafla, in this fixed order. **Each kafli is numbered 1.–6. with Arabic numerals, not Roman.** Inside a kafli, subdivisions use `1.1`, `1.2`, etc.

### 4.1 Required kafla

| #     | Heading                                                    | What it must contain                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----- | ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | **Inngangur**                                              | One-paragraph statement of what the bill does. For a gold-plating-remediation bill: identify the act being amended, the EU/EEA instrument the act transposes, and the broad purpose ("draga til baka íþyngjandi ákvæði umfram lágmarkskröfur tilskipunar / reglugerðar"). Cite the gullhúðunarskýrsla that motivates the bill.                                                                                                                                                                                                                            |
| **2** | **Tilefni og nauðsyn lagasetningar**                       | Why now, what problem. For gold-plating remediation: (a) the gullhúðunarskýrsla findings, (b) systemic Foreign Ministry task-force report (31 May 2024) if relevant, (c) any ESA letter / EFTA Court ruling / CJEU jurisprudence that has surfaced since enactment. Cite each.                                                                                                                                                                                                                                                                            |
| **3** | **Meginefni frumvarpsins**                                 | What the bill changes, at a level above the article-by-article. Group the amendments thematically (e.g., "afnám refsiákvæða", "samræming bótaákvæðis við {Art. N gerðarinnar}", "afnám séríslenskra leyfisskyldna").                                                                                                                                                                                                                                                                                                                                      |
| **4** | **Samræmi við stjórnarskrá og alþjóðlegar skuldbindingar** | **The most consequential kafli for a gold-plating-remediation bill.** Must demonstrate: (i) compatibility with stjórnarskrá (65., 71., 72., 75. gr.); (ii) bringing the act into line with the underlying EU/EEA instrument; (iii) compliance with §8(b) Reglur forsætisnefndar (gold-plating disclosure — here the disclosure is that the bill **removes** prior undisclosed gold-plating); (iv) Protocol 35 / Art. 6 EEA homogeneity; (v) any relevant CJEU / EFTA Court holding (e.g., C-300/21 _Österreichische Post_ for Art. 82 questions).         |
| **5** | **Samráð**                                                 | Who was consulted (samráðsgátt mál nr., umsagnir filed, hagsmunaaðilar). If the bill is grounded in a published gullhúðunarskýrsla, name the report and the umsagnir it relied on.                                                                                                                                                                                                                                                                                                                                                                        |
| **6** | **Mat á áhrifum**                                          | Impact assessment. Sub-headings: 6.1 Almennt; 6.2 Áhrif á eftirlitsstofnun (Persónuvernd / Fjármálaeftirlitið / Samkeppniseftirlitið / annars sectoral eftirlitsstjórnvald eftir málaflokki); 6.3 Áhrif á ríkissjóð; 6.4 Áhrif á sveitarfélögin; 6.5 Áhrif á atvinnulífið; 6.6 Áhrif á einstaklinga. For a gold-plating-remediation bill the typical finding is _íþyngjandi byrði fyrir atvinnulíf og einstaklinga er dregin saman_; _neikvæð áhrif á einstaklinga eru engin eða óveruleg_ (because the EU-instrument-level protection remains in place). |

### 4.2 EES-specific obligations inside the greinargerð

When the amending bill brings the act into line with an EEA-incorporated EU instrument:

- §8(b) Reglur forsætisnefndar — the greinargerð must state explicitly which provisions go beyond the underlying EU instrument and which the bill therefore removes. For a remediation bill, the §8(b) statement is the _positive_ form: "Frumvarpið dregur til baka eftirfarandi ákvæði sem ganga lengra en {tilskipun | reglugerð} (ESB) {YYYY/NN} krefst …" followed by a list.
- §37(1) ÞSL — hrein innleiðingarfrumvörp. The bill must not bundle non-EEA changes unless the bundling is justified in kafli 3 with reference to §13(3) Cabinet Resolution.
- Reference to the underlying JCD: standard form is _"{Tilskipun | Reglugerð} (ESB) {YYYY/NN} var tekin upp í EES-samninginn með ákvörðun sameiginlegu EES-nefndarinnar nr. {NN/YYYY} frá {dagsetning}."_ The JCD number is mandatory — look it up in the implementing act's 2. gr. or in EES-viðbætir. Worked example: GDPR was incorporated by JCD nr. 154/2018 frá 6. júlí 2018.

---

## 5. Athugasemdir við einstakar greinar frumvarpsins

After the main greinargerð, one block per article of the bill, in order. Heading form: `Um {N}. gr.`

Each block explains what the amendment does and **why** — for a gold-plating-remediation bill, the _why_ is a specific finding from the gullhúðunarskýrsla. Standard length: one to three paragraphs.

Content per block:

1. State which provision of the existing law is changed and how (recap of the amendment in prose).
2. Cite the gold-plating finding driving the change — finding ID + severity + Davidson category / pattern letter.
3. Cite the controlling EU/EEA authority that the amendment brings the IS provision into line with — specific Article number of the GDPR/directive, recital number if relevant, CJEU/EFTA Court case if applicable.
4. If the amendment narrows rather than removes, explain why narrowing is sufficient and full removal would be excessive.
5. For deletion of an article (e.g. a Pattern G30 heimasmíðuð article), explain what falls away and what catch-all GDPR mechanism remains in force.

The final article (gildistökuákvæði) often has the boilerplate closing: `Ákvæðið þarfnast ekki frekari skýringa.`

---

## 6. Fylgiskjöl — annexes

Mandatory annexes for an EEA-compliance amending bill:

1. **Samanburðartafla** — three columns: `(a) núgildandi ákvæði` (current IS text being repealed/amended) | `(b) tillaga frumvarpsins` (proposed new text or `fellur brott`) | `(c) ákvæði reglugerðar / tilskipunar` (the GDPR/directive article being brought into alignment, in authentic Icelandic from EES-viðbætir). One row per amending article of the bill. For a _heimasmíðuð_-deletion amendment, column (c) is `engin samsvarandi grein í reglugerð`.
2. **Mat á áhrifum á persónuvernd** (if processing-of-persuvernd implications) — usually inline in kafli 6 rather than a separate fylgiskjal for a remediation bill.
3. **Álitsgerð sérfræðings** — for novel constitutional or EEA-conformity questions. Optional.

The samanburðartafla is the single most important annex for gold-plating remediation work because it lets the standing committee see _exactly_ what was over-implementation and what the new text restores.

---

## 7. Style and form rules

- **Tone**: dispassionate, third-person, future-tense for the prospective effect of amendments ("verður ákvæðið …").
- **Citations**: always pinpoint to article + paragraph. "Sbr. 84. gr. reglugerðarinnar" or "sbr. 4. mgr. 47. gr. laganna". For recitals: "sbr. 27. lið formála reglugerðarinnar".
- **Abbreviations**: `sbr.` (samanber), `skv.` (samkvæmt), `þ.e.` (það er), `þ.m.t.` (þar með talið), `o.s.frv.` (og svo framvegis). No `i.e.`, `e.g.`, `etc.`
- **Numerals**: written numbers up to ten unless paired with a unit (`tvær málsgreinar`, but `5 ár`). Always digits for article numbers (`47. gr.`).
- **Quotation marks**: low-9 / high-9 (`„texti"`) for Icelandic, not curly Anglo quotes (`"texti"`). Smart-quote sweep is part of Stage 10e.
- **Hyphens vs en-dashes**: en-dash (–) for date ranges and number ranges (`1.–5. gr.`), hyphen (-) for compounds (`samráðs-`).
- **Capitalisation**: only proper nouns and the first word of a sentence. _Reglugerð_, _tilskipun_, _aðildarríki_ are lower-case in running prose. Persónuvernd (the agency name) is capitalised. GDPR appears as `reglugerð (ESB) 2016/679` on first mention, then `reglugerðin` thereafter.
- **EU institution names**: standard Icelandic forms — _Evrópuþing og ráð_, _framkvæmdastjórn ESB_, _dómstóll Evrópusambandsins_ (CJEU), _EFTA-dómstóllinn_, _Eftirlitsstofnun EFTA_ (ESA), _sameiginlega EES-nefndin_.
- **Foreign acts and case names**: keep in source language, italicised. `Personopplysningsloven`, `Databeskyttelsesloven`, _Österreichische Post_ (C-300/21).
- **Tracked changes**: not used in the introduced bill. The bill states the final form. Tracked-change presentation is for the Alþingi committee phase, not the introduced text.

---

## 8. Output discipline for the skill

When Stage 10 produces a frumvarp draft:

- Filename: `Frumvarp-{lög}-{ISO-dagsetning}.md`, with a sibling `.docx` after Stage 10f.
- All content in professional Icelandic — same language discipline as the gullhúðunarskýrsla (Stage 9e applies).
- Every amending article must trace back to a specific HIGH/CRITICAL finding ID in the Stage 9 report.
- The samanburðartafla (column c) uses authentic Icelandic text from the EES-viðbætir, never re-translated English.
- The bill is **complementary to**, not duplicative of, the Stage 9 gullhúðunarskýrsla. The skýrsla explains the diagnosis; the frumvarp proposes the remedy.

---

**End of frumvarp-structure.md.**
