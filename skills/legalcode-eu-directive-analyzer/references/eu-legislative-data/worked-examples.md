# Worked Examples — NIS2, AI Act, CSRD, CSDDD, GDPR, DSA, DMA

This file is the concrete-instrument reference used by every skill in the
seven-skill EU Legislative Compliance suite. The examples below provide short
title, formal title, CELEX, ELI URI, OJ reference, transposition deadline (if a
directive), notable language-version issues, sample obligations, transposition
status across priority Member States, gold-plating examples, and CJEU/EFTA Court
case law. Every citation is real and verifiable; verification flags are placed
at points where the suite's analyst should re-confirm against primary sources
before regulatory submission. Where exact NIM citations are unsettled or
fast-moving, the example references a published transposition tracker (Linklaters,
Herbert Smith Freehills, Ropes & Gray) as the verifiable secondary source.

---

## 1. NIS2 Directive — Directive (EU) 2022/2555

### 1.1 Identification

| Field | Value |
|---|---|
| Short title | NIS2 Directive |
| Formal title | Directive (EU) 2022/2555 of the European Parliament and of the Council of 14 December 2022 on measures for a high common level of cybersecurity across the Union, amending Regulation (EU) No 910/2014 and Directive (EU) 2018/1972, and repealing Directive (EU) 2016/1148 |
| CELEX | `32022L2555` |
| ELI (English) | `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng` |
| OJ reference | OJ L 333, 27.12.2022, p. 80 |
| Adopted | 14 December 2022 |
| Entry into force | 16 January 2023 (twentieth day after publication, Art. 45) |
| Transposition deadline | **17 October 2024** (Art. 41(1)) |
| EEA-relevance flag | Marked "Text with EEA relevance"; JCD process pending as of late 2025 |
| OEIL dossier | 2020/0359(COD) |

### 1.2 Sample obligation extraction (5 obligations)

| ID | Article | Deontic | Addressee | Text (English) |
|---|---|---|---|---|
| OBL-NIS2-001 | Art. 21(1) | Obligation | Essential entities; important entities | "Member States shall ensure that essential and important entities take appropriate and proportionate technical, operational and organisational measures to manage the risks posed to the security of network and information systems which those entities use for their operations or for the provision of their services, and to prevent or minimise the impact of incidents on recipients of their services and on other services." |
| OBL-NIS2-002 | Art. 23(1) | Obligation | Essential entities; important entities | "Each Member State shall ensure that essential and important entities notify, without undue delay, its CSIRT or, where applicable, its competent authority [...] of any incident that has a significant impact on the provision of their services as referred to in paragraph 3 (significant incident)." |
| OBL-NIS2-003 | Art. 23(4) | Obligation | Essential entities; important entities | "Member States shall ensure that, for the purpose of notification under paragraph 1, the entities concerned submit to the CSIRT or, where applicable, the competent authority: (a) without undue delay and in any event within 24 hours of becoming aware of the significant incident, an early warning [...]; (b) without undue delay and in any event within 72 hours of becoming aware of the significant incident, an incident notification [...]; (c) upon the request of a CSIRT or, where applicable, the competent authority, an intermediate report [...]; (d) a final report not later than one month after the submission of the incident notification under point (b) [...]." |
| OBL-NIS2-004 | Art. 32(2) | Obligation | Member States (supervisory regime) | "When exercising their supervisory tasks in relation to essential entities, the competent authorities shall have the power to subject those entities at least to the following [ex-ante powers listed]." |
| OBL-NIS2-005 | Art. 34(1) | Obligation | Member States (sanctions regime) | "Member States shall ensure that the administrative fines imposed on essential and important entities pursuant to this Article in respect of infringements of this Directive are effective, proportionate and dissuasive [...]." |

### 1.3 Transposition status (priority Member States; verify against Linklaters NIS2 transposition tracker at `https://www.linklaters.com/en/insights/blogs/digilinks/nis2-tracker` before reliance)

| MS | Status (as at late 2025/early 2026) | NIM citation (verify against published tracker) |
|---|---|---|
| Germany (DE) | Draft NIS2-Umsetzungs- und Cybersicherheitsstärkungsgesetz (NIS2UmsuCG); deadline missed; legislative process delayed across the 2024–2025 parliamentary calendar | Verify against Linklaters NIS2 tracker — final BGBl. citation pending adoption |
| France (FR) | Loi n° 2025-... transposing NIS2; verify against Linklaters NIS2 tracker for current JORF citation; partial transposition in advance via the SREN Loi (Loi n° 2024-449 du 21 mai 2024 visant à sécuriser et à réguler l'espace numérique) | Verify against Linklaters NIS2 tracker — JORF citation |
| Sweden (SE) | Cybersäkerhetslagen (cybersecurity act) transposing NIS2; SFS reference to be confirmed against Linklaters NIS2 tracker | Verify against Linklaters NIS2 tracker — SFS citation |
| Poland (PL) | Ustawa o krajowym systemie cyberbezpieczeństwa amendment transposing NIS2; Dz.U. citation to be confirmed | Verify against Linklaters NIS2 tracker — Dz.U. citation |
| Iceland (IS) | NIS2 not yet incorporated into the EEA Agreement (JCD pending); national transposition cannot precede incorporation; Stjórnartíðindi citation N/A until JCD adopted | Track via EEA-Lex pending JCD; see §6 of `source-playbook.md` |

### 1.4 Gold-plating examples (verify against Linklaters NIS2 tracker)

The Linklaters NIS2 tracker (URL above) flags the following gold-plating
patterns across MS as of late 2025:

- **Broader-scope** — several MS (verify per-MS) have extended the entity scope
  beyond the Annex I/II minimum to additional sectors not enumerated in the
  Directive, invoking the Art. 2(2) NIS2 Member State competence for sub-threshold
  entities.
- **Stricter-substantive** — at least one MS has imposed shorter incident
  notification windows than the Art. 23(4) 24-hour early warning + 72-hour
  detailed notification floor.
- **Earlier-deadline** — several MS adopted partial-transposition NIMs before
  the 17 October 2024 deadline; this is not gold-plating per the Commission HLG
  taxonomy (it is timing, not over-implementation), but the gold-plating-detector
  skill must distinguish.
- **Additional-sanction** — verify against the Commission's published
  conformity-assessment template practice; some MS impose criminal sanctions in
  addition to the Art. 34 administrative fines.

The published-tracker reference is the operationally verifiable source. The
gold-plating-detector skill cites the tracker; the conformity-assessment skill
verifies against the underlying NIM text by ELI/sector-7-CELEX dereference.

### 1.5 NIS1 precursor case law (interpretive context)

NIS2 repeals and replaces Directive (EU) 2016/1148 (NIS1; CELEX `32016L1148`).
Although NIS1 generated only limited CJEU jurisprudence, the Commission's
infringement record under NIS1 is the operative interpretive baseline. As of
late 2025 the Commission opened multiple Art. 258 TFEU procedures against MS
for incomplete NIS1 transposition (verify per-MS against the Commission
infringement decisions register at
`https://ec.europa.eu/atwork/applying-eu-law/infringements-proceedings/`); these
procedures inform the standard the Commission is likely to apply under NIS2.

---

## 2. AI Act — Regulation (EU) 2024/1689

### 2.1 Identification

| Field | Value |
|---|---|
| Short title | AI Act |
| Formal title | Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence and amending Regulations (EC) No 300/2008, (EU) No 167/2013, (EU) No 168/2013, (EU) 2018/858, (EU) 2018/1139 and (EU) 2019/2144 and Directives 2014/90/EU, (EU) 2016/797 and (EU) 2020/1828 (Artificial Intelligence Act) |
| CELEX | `32024R1689` |
| ELI (English) | `https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng` |
| OJ reference | OJ L, 2024/1689, 12.7.2024 |
| Adopted | 13 June 2024 |
| Entry into force | 1 August 2024 (twentieth day after publication, Art. 113) |
| EEA-relevance flag | Marked "Text with EEA relevance"; JCD process pending as of late 2025/early 2026 |
| OEIL dossier | 2021/0106(COD) |

### 2.2 Regulation (no transposition) but national-implementing-measure obligations

The AI Act is a **Regulation** under Art. 288 TFEU — directly applicable in all
Member States. There is no transposition deadline. However, the Act requires
several categories of National Implementing Measures:

- **Designated competent authorities** (Art. 70 AI Act) — each MS shall designate
  one notifying authority and one or more market surveillance authorities. The
  designation is itself a national act published in the national OJ.
- **Penalty regimes** (Art. 99 AI Act) — MS shall lay down rules on penalties
  applicable to infringements; while the Regulation sets the maximum fines
  (Art. 99(3): up to EUR 35 million or 7% of total worldwide annual turnover for
  the most serious infringements), the MS chooses the procedural and
  enforcement architecture.
- **Sandbox arrangements** (Art. 57 AI Act) — MS shall establish at least one
  AI regulatory sandbox at national level, operational by 2 August 2026.

The transposition-tracker skill applies to the AI Act in the **NIM-collection
mode**: it tracks designation acts and penalty acts per MS, even though there
is no Art. 260(3) TFEU notification obligation (which applies only to legislative
directives).

### 2.3 Phased application

The AI Act applies in phases:
- 2 February 2025 — prohibitions on Art. 5 unacceptable-risk practices.
- 2 August 2025 — General-Purpose AI (GPAI) provider obligations.
- 2 August 2026 — high-risk system obligations (Annex III).
- 2 August 2027 — high-risk obligations for systems falling under existing
  Union harmonisation legislation listed in Annex I, Section A.

The conformity-assessment skill, when applied to AI Act NIMs, must reference
the relevant phase: a designation act adopted before 2 August 2025 is timely;
one adopted in 2026 is late as to GPAI but timely as to Annex III high-risk.

### 2.4 EEA relevance assessment status

The AI Act is marked "Text with EEA relevance"; the EEA Joint Committee has
not formally incorporated it as of late 2025/early 2026. The EFTA Standing
Committee has issued EEA EFTA Comments (verify current version at
`https://www.efta.int/eea-lex`). Until incorporation by JCD, the AI Act is
not part of the EEA acquis and is not directly applicable in IS/NO/LI; the
EEA-incorporation-tracker skill follows this dossier closely.

---

## 3. CSRD — Directive (EU) 2022/2464

### 3.1 Identification

| Field | Value |
|---|---|
| Short title | CSRD |
| Formal title | Directive (EU) 2022/2464 of the European Parliament and of the Council of 14 December 2022 amending Regulation (EU) No 537/2014, Directive 2004/109/EC, Directive 2006/43/EC and Directive 2013/34/EU, as regards corporate sustainability reporting |
| CELEX | `32022L2464` |
| ELI (English) | `https://eur-lex.europa.eu/eli/dir/2022/2464/oj/eng` |
| OJ reference | OJ L 322, 16.12.2022, p. 15 |
| Adopted | 14 December 2022 |
| Entry into force | 5 January 2023 |
| Transposition deadline | **6 July 2024** (Art. 5(1)) |
| EEA-relevance flag | Marked "Text with EEA relevance" |
| OEIL dossier | 2021/0104(COD) |

### 3.2 Transposition gold-plating examples

The Linklaters CSRD transposition tracker (verify at
`https://sustainablefutures.linklaters.com/`) and the Ropes & Gray tracker
(verify at `https://www.ropesgray.com/en/insights/alerts`) document the
following gold-plating patterns:

- **Germany** — Verify against Linklaters CSRD tracker for the current
  CSRD-Umsetzungsgesetz status; Germany missed the 6 July 2024 deadline and
  the Commission opened an Art. 258 TFEU letter of formal notice on 26
  September 2024 (verify against `https://ec.europa.eu/commission/presscorner/`).
  Several Bundesländer published draft NIM language with stricter assurance
  requirements than the CSRD floor; verify per-Land against the tracker.

- **France** — Ordonnance n° 2023-1142 du 6 décembre 2023 (JORF n° 0283 du
  7 décembre 2023, texte n° 9; NOR : ECOT2326842R) transposing CSRD ahead of
  deadline; verify against the Linklaters tracker for any gold-plating flagged.

- **Italy** — Decreto Legislativo n. 125 del 6 settembre 2024 (G.U. Serie
  Generale n. 212 del 10.9.2024); verify against Ropes & Gray CSRD tracker —
  the Italian transposition has been flagged for extending the assurance
  requirements to a wider perimeter than the CSRD floor.

The gold-plating-detector skill applies the published-tracker citation as the
authoritative secondary source for each per-MS finding, then verifies against
the underlying NIM text via ELI/Cellar dereference.

---

## 4. CSDDD — Directive (EU) 2024/1760

### 4.1 Identification

| Field | Value |
|---|---|
| Short title | CSDDD (Corporate Sustainability Due Diligence Directive) |
| Formal title | Directive (EU) 2024/1760 of the European Parliament and of the Council of 13 June 2024 on corporate sustainability due diligence and amending Directive (EU) 2019/1937 and Regulation (EU) 2023/2859 |
| CELEX | `32024L1760` |
| ELI (English) | `https://eur-lex.europa.eu/eli/dir/2024/1760/oj/eng` |
| OJ reference | OJ L, 2024/1760, 5.7.2024 |
| Adopted | 13 June 2024 |
| Entry into force | 25 July 2024 |
| Transposition deadline | **26 July 2026** (Art. 37(1)) |
| EEA-relevance flag | Marked "Text with EEA relevance" |
| OEIL dossier | 2022/0051(COD) |

### 4.2 Live transposition exercise

CSDDD is the "live" transposition exercise for the suite as of late 2025/early
2026: the deadline lies in the future (26 July 2026), several MS have published
draft NIM language, and the cross-MS comparison is dynamic. Verify the current
state against the Herbert Smith Freehills CSDDD tracker (verify at
`https://www.herbertsmithfreehills.com/insights/`) and the Linklaters CSDDD
tracker.

The transposition-tracker and gold-plating-detector skills, when applied to
CSDDD, must:
- Treat any NIM in force before 26 July 2026 as **early transposition**, not
  gold-plating per se.
- Flag the pre-existing **German LkSG** (Lieferkettensorgfaltspflichtengesetz,
  in force since 1 January 2023 for 3,000+-employee companies) as a parallel
  national regime that overlaps with CSDDD; the German transposition will
  involve amending the LkSG to align with the CSDDD floor.
- Flag the pre-existing **French Loi n° 2017-399 du 27 mars 2017 relative au
  devoir de vigilance** as the analogous parallel French regime.

### 4.3 Phased application

CSDDD applies in phases linked to company size:
- 26 July 2027 — companies with > 5,000 employees and > EUR 1.5 billion
  worldwide net turnover.
- 26 July 2028 — companies with > 3,000 employees and > EUR 900 million
  worldwide net turnover.
- 26 July 2029 — full scope (companies with > 1,000 employees and > EUR 450
  million worldwide net turnover).

(Note: the CSDDD phasing was modified by the **Omnibus** package in 2025; the
analyst should verify the current phasing against the latest consolidated
version of the Directive via the Cellar query in `source-playbook.md` § 1.1(a)
before reliance.)

---

## 5. GDPR — Regulation (EU) 2016/679

### 5.1 Identification

| Field | Value |
|---|---|
| Short title | GDPR |
| Formal title | Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation) |
| CELEX | `32016R0679` |
| ELI (English) | `https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng` |
| OJ reference | OJ L 119, 4.5.2016, p. 1 |
| Adopted | 27 April 2016 |
| Entry into force | 24 May 2016 |
| Application date | **25 May 2018** (Art. 99(2)) |
| EEA-relevance flag | Marked "Text with EEA relevance"; incorporated by JCD No 154/2018 of 6 July 2018, in force in IS/NO/LI from 20 July 2018 |
| OEIL dossier | 2012/0011(COD) |

### 5.2 Regulation example for contrast

GDPR is a Regulation under Art. 288 TFEU — directly applicable in all MS without
national transposition. Member States nonetheless adopt **national implementing
measures** for the **opening clauses** in the GDPR text — specific provisions
that the Regulation expressly leaves for MS specification:

- **Art. 6(2)–(3)** — MS may maintain or introduce more specific provisions for
  Art. 6(1)(c) (legal obligation) and (e) (public interest) processing.
- **Art. 8(1)** — MS may lower the digital age of consent below 16 (down to 13).
- **Art. 9(2)(b),(g),(h),(i),(j)** — MS conditions for special-category data
  processing.
- **Arts. 36(5), 37(4), 38(5), 80(2)** — multiple supervisory and procedural
  opening clauses.

Each MS has therefore enacted a **national GDPR implementation act**:
- Germany — Bundesdatenschutzgesetz (BDSG) of 30 June 2017 (BGBl. I S. 2097),
  re-issued 20 November 2019 (BGBl. I S. 1626).
- France — Loi n° 78-17 du 6 janvier 1978 relative à l'informatique, aux
  fichiers et aux libertés, modified by Loi n° 2018-493 du 20 juin 2018
  (JORF n° 0141 du 21 juin 2018, texte n° 1).
- Sweden — Lag (2018:218) med kompletterande bestämmelser till EU:s
  dataskyddsförordning (SFS 2018:218).
- Poland — Ustawa z dnia 10 maja 2018 r. o ochronie danych osobowych
  (Dz.U. 2018 poz. 1000).
- Iceland — Lög nr. 90/2018 um persónuvernd og vinnslu persónuupplýsinga.

The transposition-tracker skill, applied to GDPR, tracks the opening-clause NIMs
rather than a "transposition deadline" (there is none). The conformity-assessment
skill verifies that the opening-clause NIMs are within the bounds permitted by
the corresponding GDPR provision — exceeding the bounds would be an Art. 16
TFEU pre-emption issue, not gold-plating in the usual sense.

### 5.3 Notable CJEU jurisprudence (interpretive context)

- *Schrems II* (Case C-311/18, ECLI:EU:C:2020:559) — Privacy Shield invalidation;
  Standard Contractual Clauses survival with supplementary measures.
- *Bundesverband der Verbraucherzentralen* (Case C-319/20, ECLI:EU:C:2022:322) —
  collective redress under Art. 80(2) GDPR.
- *Österreichische Post* (Case C-300/21, ECLI:EU:C:2023:370) — non-material
  damage under Art. 82 GDPR.

---

## 6. DSA — Regulation (EU) 2022/2065

### 6.1 Identification

| Field | Value |
|---|---|
| Short title | DSA (Digital Services Act) |
| Formal title | Regulation (EU) 2022/2065 of the European Parliament and of the Council of 19 October 2022 on a Single Market For Digital Services and amending Directive 2000/31/EC (Digital Services Act) |
| CELEX | `32022R2065` |
| ELI (English) | `https://eur-lex.europa.eu/eli/reg/2022/2065/oj/eng` |
| OJ reference | OJ L 277, 27.10.2022, p. 1 |
| Adopted | 19 October 2022 |
| Entry into force | 16 November 2022 |
| Application date | 17 February 2024 (general); 25 August 2023 (designated VLOPs/VLOSEs) |
| EEA-relevance flag | Marked "Text with EEA relevance"; JCD pending |
| OEIL dossier | 2020/0361(COD) |

### 6.2 Regulation contrast

Like GDPR and the AI Act, DSA is a Regulation — no transposition. National
implementing measures are limited to:
- Designating Digital Services Coordinators (Art. 49 DSA).
- Establishing penalty regimes (Art. 52 DSA).
- Procedural rules for trusted-flagger certification (Art. 22 DSA).

The DSA is the operative example for the suite when illustrating the
narrow scope of NIM tracking on a Regulation.

---

## 7. DMA — Regulation (EU) 2022/1925

### 7.1 Identification

| Field | Value |
|---|---|
| Short title | DMA (Digital Markets Act) |
| Formal title | Regulation (EU) 2022/1925 of the European Parliament and of the Council of 14 September 2022 on contestable and fair markets in the digital sector and amending Directives (EU) 2019/1937 and (EU) 2020/1828 (Digital Markets Act) |
| CELEX | `32022R1925` |
| ELI (English) | `https://eur-lex.europa.eu/eli/reg/2022/1925/oj/eng` |
| OJ reference | OJ L 265, 12.10.2022, p. 1 |
| Adopted | 14 September 2022 |
| Entry into force | 1 November 2022 |
| Application date | 2 May 2023 |
| EEA-relevance flag | Marked "Text with EEA relevance"; JCD pending |
| OEIL dossier | 2020/0374(COD) |

### 7.2 Regulation contrast — heavy direct enforcement

DMA is administered centrally by the Commission (DG COMP) under a Regulation-only
enforcement model. Unlike DSA, the DMA does not delegate enforcement to national
DSCs; the Commission's gatekeeper-designation decisions and non-compliance
decisions are themselves the enforcement instruments. National implementing
measures are minimal — primarily ensuring national procedural compliance with
Commission information requests under Art. 21 DMA.

This is the "pure central enforcement" contrast to NIS2's "minimum-harmonisation
directive" model: the same domain (cybersecurity / digital services / digital
markets) yields three different EU instrument types with three different
transposition-or-enforcement architectures.

---

## 8. Cross-instrument summary table

| Instrument | CELEX | Type | Deadline / Application | EEA-relevant | Transposition tracker authority |
|---|---|---|---|---|---|
| GDPR | `32016R0679` | Regulation | Applied 25.5.2018 | Yes (JCD 154/2018) | EDPB; national DPAs |
| NIS2 | `32022L2555` | Directive | Transposition 17.10.2024 | Yes (JCD pending) | Linklaters NIS2 tracker |
| DSA | `32022R2065` | Regulation | Applied 17.2.2024 | Yes (JCD pending) | Commission DSA register |
| DMA | `32022R1925` | Regulation | Applied 2.5.2023 | Yes (JCD pending) | Commission DG COMP |
| CSRD | `32022L2464` | Directive | Transposition 6.7.2024 | Yes | Linklaters / Ropes & Gray CSRD trackers |
| AI Act | `32024R1689` | Regulation | Phased 2.2.2025–2.8.2027 | Yes (JCD pending) | EU AI Office; published trackers |
| CSDDD | `32024L1760` | Directive | Transposition 26.7.2026 | Yes | HSF / Linklaters CSDDD trackers |
| DORA | `32022R2554` | Regulation | Applied 17.1.2025 | Yes | EBA / ESMA / EIOPA |

---

## 9. Verification flags

Where a citation in this file carries "verify against [tracker URL]" language,
the analyst must perform the verification **before** the suite emits any
artefact citing the fact. The following claims are flagged for verification at
the time of suite execution because they are fast-moving:

- All NIS2 NIM citations across DE/FR/SE/PL — verify against Linklaters NIS2
  transposition tracker at `https://www.linklaters.com/en/insights/blogs/digilinks/nis2-tracker`.
- All CSRD NIM citations across DE/FR/IT — verify against the Linklaters CSRD
  tracker (`https://sustainablefutures.linklaters.com/`) and Ropes & Gray
  CSRD tracker.
- All CSDDD NIM citations and phasing — verify against the HSF and Linklaters
  CSDDD trackers; the Omnibus package in 2025 modified the original phasing
  schedule, and any analytical use must use the consolidated text.
- AI Act EEA incorporation status — verify against EEA-Lex
  (`https://www.efta.int/eealaw`) for the current JCD status.
- All Commission Art. 258/260 TFEU procedure references — verify against
  `https://ec.europa.eu/atwork/applying-eu-law/infringements-proceedings/`.

The verification flag is not a defect — it is the operational consequence of
working in EU law, where transposition status, infringement procedures, and
consolidated text versions change continuously. Every skill in the suite
honours the flag by passing the cited fact through a re-verification step
before emission. This is what equal authenticity, the doctrine of *CILFIT*, and
the rigour bar of the suite require in operational practice.
