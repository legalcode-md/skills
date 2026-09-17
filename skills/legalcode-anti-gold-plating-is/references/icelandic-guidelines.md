# Icelandic Guidelines and Deliverable Standards

## Output Language — Read This First

**The report is written entirely in professional, legal Icelandic.** The skill instructions in this file (SKILL.md) are in English; the deliverable is not.

Rules for the deliverable:

1. **No word-for-word translation from English.** Generate Icelandic legal text natively. If a sentence reads like a literal translation ("með beinum sótt af", "ber þungun gegn", "stefnumótunarlegur rökstuðningur"), rewrite it as a native Icelandic speaker would phrase it.
2. **Only foreign primary sources stay in their original language** — verbatim quotations from GDPR articles, EU directive recitals, CJEU/ECJ judgments, and the names of foreign acts (Personopplysningsloven, Databeskyttelsesloven, Tietosuojalaki, Dataskyddslag). Everything else — section headings, classifications, analysis, recommendations, limitations — is in Icelandic.
3. **Use Icelandic legal vocabulary, not calques.** Examples: _svigrúm aðildarríkja_ (not "valdrúm"), _ófjárhagslegt tjón_ (not "ósnertanlegt tjón"), _tilgreint í greinargerð_ (not "tilkynnt"), _vegur þyngra_ (not "ber þungun"), _27. liður formála_ (not "inngangsorð 27"), _sóttar beint af vef Alþingis_ (not "með beinum sótt af althingi.is").
4. **The Icelandic grammar / language pass (Stage 9e) is the last markdown-editing step.** Substantive content is frozen by the verifier pass at 9d. After 9e, the only remaining step is rendering to `.docx` — no further content changes. See Stage 9 below.

## Stage 9e — Report Language and Grammar Pass

**9e — Icelandic language / grammar pass (mandatory; last markdown-editing step).** Read the draft section by section, top to bottom, and rewrite any of the following in native Icelandic legal prose. This is the polish step: substantive content is now frozen; only prose, vocabulary, and grammar change.

- Word-for-word translations from English (calques such as "með beinum sótt", "ber þungun gegn", "stefnumótunarlegur rökstuðningur", "ósnertanlegt tjón", "tilkynnt í greinargerð" where the proper term is "tilgreint", "engin sérstök andmæli fundust" where "engar sérstakar athugasemdir" is natural, "Stutt samantekt í þremur setningum" where "Niðurstaða í þremur setningum" reads cleanly).
- Stilted Anglo-style sentence order; rewrite for Icelandic verb position and natural flow.
- Technical Anglicisms when an established Icelandic legal term exists (e.g., _svigrúm aðildarríkja_ not "valdrúm"; _27. liður formála_ not "inngangsorð 27"; _vegur þyngra_ not "ber þungun gegn"; _ófjárhagslegt tjón_ not "ósnertanlegt tjón"; _sóttar beint af vef Alþingis_ not "með beinum sótt af althingi.is").
- Capitalised English-style classification labels in headings (translate `Severity: HIGH` to `Alvarleikastig: Há`; `Confidence: Probable` to `Öryggi: Líklegt`; `Pre-law forensics` to `Lagaferill málsins`; `Counter-argument stress test` to `Mótrökspróf`).
- Icelandic morphological correctness — beygingar (declensions and conjugations) of names and technical terms; check that _sbr._ / _skv._ abbreviations are used consistently; check _þ.e._ / _þ.m.t._ spacing.
- **Internal tooling and process references — strip every one.** The deliverable is a standalone legal document for lawyers, Alþingi committees, and regulated parties. It must not mention MCP tool names (`legalcode_search`, `legalcode_trace`, `legalcode_fetch`, `legalcode_analyze`, `cases_for_law`, `pre_law_for_law`, `resultLevel`, `flowKey`, `sourceRef`, `downloadUrl`), skill names (`legalcode-anti-gold-plating-is`, `anti-gold-plating-is`, `Legalcode`, `Anthropic`), internal stage references (`Stage 1`, `Stage 8`, `§8 of the skill`, `Iron Law 7`, `verkferli`, `samkvæmt verkferli`), agent terms (`agent`, `orchestrator`, `subagent`, `tool call`), or working-directory file names (`sources/`, `articles/`, `forensics/`, `stress/`, `revisions/`, `article-index.json`, `frumvarp-mapping.md`). The reader needs the legal substance — not how it was produced. Refer to evidence by its **public citation** (þingskjal number, ákvörðun, dómsmál, umsögn submitter + date) and to method-level requirements (e.g. counter-argument analysis) **without naming the internal procedure or its file**.

#### 9e.1 — Common Icelandic grammar and word-choice errors (general reference)

These patterns appear in any Icelandic prose written by an English-native author and are not law-specific. They were observed empirically in pre-9e drafts of this skill's deliverables and form the core checklist for the 9e pass. Sweep for each category.

**(a) Calques from English — direct word-for-word translations.** These look superficially Icelandic but read as foreign-mind constructions:

| Calque                                            | Standard Icelandic                                 | Why the calque fails                                                                    |
| ------------------------------------------------- | -------------------------------------------------- | --------------------------------------------------------------------------------------- |
| _„innihalda"_ (contain)                           | _„geyma"_, _„að finna sé í"_, _„hafa að geyma"_    | `Innihalda` is for physical/chemical containment; documents _„geyma ákvæði"_.           |
| _„beitt eins og skrifað"_ (applied as written)    | _„beitt eftir orðanna hljóðan"_, _„beitt orðrétt"_ | The verb `beinast` does not mean `apply`.                                               |
| _„bera þungan af [áhrifum]"_ (bear the brunt of)  | _„hafa mest áhrif á"_, _„bera þyngd af"_           | English idiom does not map directly.                                                    |
| _„teoretísk"_ (theoretical)                       | _„fræðileg"_                                       | Direct adoption of the English word.                                                    |
| _„forensik-"_ (forensic)                          | _„rannsóknar-"_                                    | Not a word in Icelandic.                                                                |
| _„verbatim"_ (Latinism via English)               | _„orðréttur"_                                      |                                                                                         |
| _„sectoral"_ (English in IS text)                 | _„sérgreindur"_, _„sérgreint"_                     |                                                                                         |
| _„rauntækur"_ (effective / real-world)            | _„raunverulegur"_                                  | The Anglicism reads stilted.                                                            |
| _„vernda gegn"_ (protect against [something])     | _„vernda [andlag]"_ (sögnin tekur þolfall)         | The IS verb is transitive: _„verndar persónuupplýsingar"_, not _„verndar gegn brotum"_. |
| _„draga til baka [ákvæði]"_ (roll back)           | _„fella úr gildi"_, _„nema úr gildi"_              | `Draga til baka` is for withdrawing a statement/offer, not legislation.                 |
| _„starfa undir"_ (operate under)                  | _„starfa eftir"_, _„lúta"_                         | IS preposition for compliance is `eftir`.                                               |
| _„bjóða upp á"_ (provide / offer)                 | _„veita"_                                          | Colloquial; in formal prose use `veita`.                                                |
| _„léttara skilyrði"_ (lighter condition)          | _„vægara skilyrði"_                                | `Léttur` is physical weight; for thresholds use `vægur`.                                |
| _„sterkasta breyting"_ (strongest change)         | _„veigamesta breyting"_                            | `Sterkur` is physical strength; for significance use `veigamikill`.                     |
| _„hélt [X] óbreyttri"_ (kept it unchanged)        | _„lét [X] standa óbreytt"_                         | English `keep` construction is unidiomatic.                                             |
| _„byggði [úrskurð] á"_ (based on)                 | _„reisti [úrskurð] á"_                             | `Reisa á` is the legal idiom; `byggja á` is acceptable but less formal.                 |
| _„hægir á"_ used for "reduces"                    | _„dregur úr"_                                      | `Hægja á` literally means slow down.                                                    |
| _„draga saman [byrði]"_ (intended as reduce)      | _„draga úr [byrði]"_                               | `Draga saman` means summarise/contract; `draga úr` means reduce.                        |
| _„tilkynntar niðurstöður"_ (reported findings)    | _„niðurstöður"_                                    | Participle is redundant — judgments are not "announced findings".                       |
| _„hámarksviðmið samræmingar"_ (max harmonisation) | _„hámarkssamræming"_; in tables _„ófrávíkjanlegt"_ | Established legal term.                                                                 |
| _„flækja"_ (complicate)                           | _„torvelda"_                                       | `Flækja` is talmál; `torvelda` is formal.                                               |
| _„skapa hegðun"_ (create behaviour)               | _„leiða af sér hegðun"_, _„valda hegðun"_          | One does not "create" behaviour in IS.                                                  |
| _„opna heimild víðar"_ (open more widely)         | _„rýmka heimildina"_                               | Standard verb is `rýmka`.                                                               |
| _„yrði til hindrunar"_ (would be a hindrance)     | _„stendur í vegi"_, _„verður hindrun"_             | The IS idiom for an obstacle is `standa í vegi`.                                        |
| _„mótbárur"_ (objections, formal)                 | _„athugasemdir"_                                   | `Mótbárur` is talmál; formal IS is `athugasemdir`.                                      |
| _„textaleg afmörkun"_ (textual limitation)        | _„þrenging"_                                       | The IS legal noun for narrowing is `þrenging`.                                          |
| _„engin sérstök andmæli fundust"_                 | _„engar sérstakar athugasemdir komu fram"_         | Calque of "no specific objections were found".                                          |
| _„textaleg afmörkun frá ófrávíkjanlegri grein"_   | _„þrenging á ófrávíkjanlegu ákvæði"_               | The IS legal idiom takes `á` + dative.                                                  |

**(b) Verb-government and preposition errors (sögn- og forsetningarstýring).** Icelandic verbs and adjectives govern specific cases and prepositions; English-native writers often default to wrong constructions:

- _„vara við að [setning]"_ → _„vara við því að [setning]"_ — the verb takes a dative pronoun anchor before the `að`-clause.
- _„háð að [grein]"_ → _„lýtur skilyrðum [greinar]"_ — the adjective `háður` takes dative directly (`háð því`), never `að`. For "subject to [a rule]" the standard verb is `lúta` + dative.
- _„rökstuðningur frávika"_ (ef.) → _„rökstuðningur fyrir frávikum"_ (þgf.) — IS `rökstuðningur` takes `fyrir` + dative; English `justification of` is a calque.
- _„létta [þf.]"_ → _„létta [þgf.]"_ — the verb `létta` takes dative: _„léttir formkröfum"_, _„léttir lögfræðilegri óvissu"_.
- _„kæruferli til lögreglu"_ → _„kæruferli gagnvart lögreglu"_ — the IS preposition for the relational party is `gagnvart`.
- _„fyrir hverja tegund"_ (after `rýmkar`) → _„til hverrar tegundar"_ — the verb `rýmka til` governs genitive.

**(c) Gender and case agreement (kynjasamræmi og fallaskipting).** The most frequent grammatical errors are agreement mismatches between noun and modifier:

- _„Engar sakamál"_ → _„Engin sakamál"_ — `sakamál` is hk. ft.; quantifier must be `engin`, not `engar` (kvk. ft.).
- _„fjölmargar úrskurðir"_ → _„fjölmargir úrskurðir"_ — `úrskurður` is kk.; ft. modifier is `fjölmargir`, not `fjölmargar` (kvk. ft.).
- _„fjárhagslega tjón"_ (in nominative) → _„fjárhagslegt tjón"_ — `tjón` is hk. nf.; nf. and þf. of the adjective are identical (`fjárhagslegt`); the form `fjárhagslega` is the lh.-mynd / atviksm., which is wrong in nominal contexts.
- _„verulegan áhrif"_ → _„veruleg áhrif"_ — `áhrif` is hk. ft.; modifier is `veruleg`, not the kk. þf. et. `verulegan`.
- _„almenn stjórnsýsluúrræði"_ (when modifying noun adverbially) → _„almennt stjórnsýsluúrræði"_ — when "in general / as a rule", use the atviksm. `almennt`, not the lo. `almenn`.
- _„ófrávíkjandi"_ → _„ófrávíkjanleg"_ — the lh.-nt. form `ófrávíkjandi` (present participle of `víkja`) is not the same as the adjective `ófrávíkjanleg` (-leg-suffixed). Use the latter for the legislative-technique concept.
- _„lögfræðileg óvissu"_ → _„lögfræðilegri óvissu"_ — `óvissa` is kvk.; dative is `óvissu` with adjective `lögfræðilegri` (kvk. þgf.).

**(d) Verb conjugation, mood, and tense (sagnbeyging, háttur og tíð).**

- After _„í ljósi þess að"_ (in light of the fact that), IS legal prose prefers viðtengingarháttur: _„í ljósi þess að engin önnur ríki haldi …"_, not _„halda"_.
- Wrong viðtengingarháttur where nútíð fits: _„þegar greinin yrði til hindrunar"_ (viðth. of `yrði`) where the meaning is recurring/general — should be nútíð _„þegar greinin stendur í vegi"_.
- Plural subject demands plural verb: _„verndarráðstafanir helst óbreyttar"_ → _„verndarráðstafanir haldast óbreyttar"_ (the form `helst` is 3sg of `haldast`).
- _„afnumur"_ is not an Icelandic word; the present indicative of `afnema` is `afnemur`.
- Singular noun with plural-implying verb: _„Þvingunarsekt er almenn stjórnsýsluúrræði"_ — number must agree. Use ft.: _„Þvingunarsektir eru almennt stjórnsýsluúrræði"_.

**(e) Compound-word formation (samsett orð).** Icelandic compounds use linking morphemes (bandstafir) that English natives often get wrong:

- _„breytingafrumvarp"_ → _„breytingarfrumvarp"_ — `breyting` requires `-ar-` in compounds; sbr. `breytingartillaga`, `breytingarlög`.
- _„stjórnsýslusektarakerfi"_ → _„stjórnsýslusektakerfi"_ — use ft. ef. `-sekta-` once, not `-sektar-a-`.
- _„bótabyrð"_ → _„bótabyrði"_ — the noun is kvk. i-stem `bótabyrði`.
- _„viðurlagaramur"_ → _„viðurlagarammi"_ — the masculine word for `frame/scope` is `rammi` (weak), not `*ramur`.
- _„Útgáfutímabilstexti"_ — not a word; for a release-date metadata field use _„Útgáfudagur"_.
- _„byrgjum"_ (intended as `pillars`) — `byrgi` does not carry this metaphor in Icelandic; use _„þættir"_ or _„ákvæði"_.

**(f) Double definiteness (tvöföld ákveðni).** Icelandic does not double-mark definiteness: a demonstrative pronoun already conveys it.

- _„sú heimildin"_ → _„sú heimild"_ — drop the suffixed article when `sú/sá/það` precedes.
- _„þessi maðurinn"_ → _„þessi maður"_.

**(g) Concessive conjunctions (`þrátt fyrir að` vs `þótt`).** Two near-synonyms with different register:

- _„þrátt fyrir að"_ is heavy/concessive and often a calque from English `despite the fact that`. Best reserved for emphasis on contradiction.
- _„þótt"_ is the lighter, more natural Icelandic concessive: _„þótt 15. gr. sé ekki tekin fyrir"_. In legal prose `þótt` reads cleanly; `þrátt fyrir að` is verbose.

**(h) Numerals (talnaritun).** Lágar tölur (≤ 12) eru ritaðar í bókstöfum í lögfræðiprósu: _„á sjö árum"_, ekki _„í 7 árum"_. _„Í 7 árum"_ er auk þess enskumengun („in 7 years"); rétta forsetningin er _„á sjö árum"_ eða _„á þeim sjö árum sem"_ (þolfall án `í`).

**(i) `Tilteknir` vs `ákveðnir` (specific).** _„ákveðnum samningum"_ er calque af enska _„certain agreements"_. Á íslensku merkir _„ákveðinn"_ (1) ákvarðaður og (2) ákveðinn í afstöðu — ekki _„some unspecified"_. Rétta orðið er _„tiltekinn"_: _„tilteknum samningum"_.

**(j) Ellipsis-pattern from English (`X does, Y does not`).** _„Svíþjóð hefur sambærilegt kerfi, Noregur og Danmörk ekki"_ — enskt mynstur `do not`-ellipsis. Á íslensku þarf að klára sögnina: _„Noregur og Danmörk hafa það ekki"_. Auk þess hentar semikomma frekar en komma þegar tvær aðskildar staðhæfingar liggja saman.

**(k) Eignarfall samsvörun í eldri-vísi tilvitnunum.** Þegar tilvísun fer fram með _„(eldri lög nr. X/Y)"_ eftir nafnorði í eignarfalli skal `lög` einnig vera í eignarfalli — _„áhrif eldri löggjafar (laga nr. 77/2000)"_ en ekki _„(lög nr. 77/2000)"_.

**(l) `vara við [þgf.]` + `því að`** og önnur föst orðasambönd: _„vara við að"_ + setning → _„vara við því að"_ + setning. Sambærilegt: _„benda á það að"_, _„vekja athygli á því að"_.

**Pre-9f sweep grep — append to existing line 817 sweep:**

```bash
grep -nE "innihalda|teoretís|forensik|verbatim|sectoral|rauntæk|vernda gegn|draga til baka|starfa undir|bjóða upp á|léttara skilyrði|sterkasta breyting|hélt .* óbreyttri|byggði .* á|hægir á|draga saman .* byrð|tilkynntar niðurstöður|hámarksviðmið|\\bflækir\\b|skapa hegðun|opna heimild víðar|yrði til hindrunar|mótbárur|textaleg afmörkun|engin sérstök andmæli|sú [a-zíáéðýúóöþæ]+inn\\b|í [0-9]+ árum|vara við að|háð að|rökstuðningur [a-zíáéðýúóöþæ]+a frá|fyrir hverja tegund|kæruferli til|Engar sakamál|fjölmargar úrskurðir|verulegan áhrif|almenn stjórnsýsluúrræði|\\bófrávíkjandi\\b|lögfræðileg óvissu|breytingafrumvarp|stjórnsýslusektaraker|bótabyrð\\b|viðurlagaramur|byrgjum|ákveðnum samningum|þrátt fyrir að" Gullhudunarskyrsla-*.md Frumvarp-*.md
```

Each hit is a candidate for the table above. Not every hit is wrong (the context matters — `þrátt fyrir að` is sometimes the right concessive), but every hit deserves a moment of review. After resolving hits, the grep returns empty or only the deliberately-kept variants.

**What stays in the source language**, untouched:

- Verbatim quotations from GDPR articles, EU directive recitals, and CJEU/ECJ judgments (English).
- Names of foreign acts (Personopplysningsloven, Databeskyttelsesloven, Tietosuojalaki, Dataskyddslag, Brottsdatalag).
- Names of foreign institutions in their canonical form (Folketinget, Storting, Bundestag, grundlagsutskottet).
- Case identifiers (C-300/21 _Österreichische Post_, E-16/11 _Icesave_).

Sweep with `grep -nE "með beinum|ber þungun|stefnumótunarlegur|ósnertanlegt|frásagnarform|upprunaaktor|tilkynnt í greinargerð|stakeholder|forsöguslóð|valdrúm"` to catch the most common residue from earlier drafts.

**Internal-tooling sweep (mandatory before docx).** Any of these tokens appearing in the deliverable is a hard fail — strip them all:

```bash
grep -nE "legalcode_(search|trace|fetch|analyze|discover)|legalcode-(anti-gold-plating-is|search-agent|agent-pack|counsel|full-bench|adversarial|review|verification|roundtable|tabulate)|anthropic-skills|cases_for_law|pre_law_for_law|laws_for_case|resultLevel|flowKey|sourceRef|downloadUrl|nextAction|Stage [0-9]|§[0-9] (of|í) (the )?skill|verkferli|Iron Law|orchestrator|subagent|tool call|MCP|article-index\.json|frumvarp-mapping\.md|articles/|forensics/|stress/|revisions/|sources/" Gullhudunarskyrsla-*.md
```

Returns must be empty. Replace each hit with the public citation or substantive description it stands in for. Examples:

- `samkvæmt verkferli legalcode-anti-gold-plating-is §8` → delete entirely; the reader needs the _finding_, not the procedure that produced it.
- `úrtak úr legalcode_trace cases_for_law` → `úrtak úr dómaframkvæmd Persónuverndar, Landsréttar og Hæstaréttar` (or list the case numbers directly).
- `Iron Law 7 mótrökspróf` → `mótrökspróf gegn niðurstöðunni` (the method is named, the internal label is not).
- `sbr. sourceRef pre_law_document/IS/...` → cite by þskj. + dagsetning + sender instead.

**After 9e the markdown file is final.** Do not edit the markdown after this step except to fix a typo a Stage 9f docx-rendering check uncovers.

## Stage 10e — Frumvarp Language and Grammar Pass

**10e — Icelandic language / grammar pass (mandatory; last markdown step).** Same discipline as Stage 9e, with three frumvarp-specific additions:

- **Standard amendment-text formulations** — exact phrasings from `references/frumvarp-structure.md` §3.2. Replace any paraphrase with the canonical form (`X. gr. laganna fellur brott.` not "X. gr. is repealed").
- **Quotation marks** — Icelandic low-9 / high-9 (`„texti"`), not Anglo curly (`"texti"`). Sweep: `grep -nE '"[^"]*"' Frumvarp-*.md` and replace each pair with `„`…`"`.
- **Icelandic abbreviations** — `sbr.`, `skv.`, `þ.e.`, `þ.m.t.`, `o.s.frv.` only. No `i.e.`, `e.g.`, `etc.`, `cf.`. Sweep: `grep -nE "\\b(i\\.e\\.|e\\.g\\.|etc\\.|cf\\.)\\b" Frumvarp-*.md` returns nothing.
- **Internal-tooling sweep (mandatory).** Same discipline as Stage 9e. Run the full Stage-9e sweep regex against `Frumvarp-*.md` — must return zero hits. A frumvarp introduced to Alþingi that mentions tool names, skill names, MCP, sourceRefs, or working-directory paths is unfit for filing.
