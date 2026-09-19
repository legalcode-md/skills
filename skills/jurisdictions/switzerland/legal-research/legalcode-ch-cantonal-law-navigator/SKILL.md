---
name: legalcode-ch-cantonal-law-navigator
description: 'Navigate Switzerland''s 26-canton legal patchwork: map federal vs. cantonal authority, compare
  commercial register procedures and fees, model effective corporate and inheritance tax rates by canton,
  identify the correct labor court (Arbeitsgericht / Tribunal des prud''hommes) and civil court of first
  instance, understand real estate transfer taxes (Handänderungssteuer / droits de mutation) and land
  registry (Grundbuch / Registre foncier) requirements, clarify notarization obligations under the Staatliches
  vs. Freies Notariat distinction, and flag cantonal variations that affect entity formation, property
  transactions, succession planning, or litigation strategy. Use when a client''s matter touches Switzerland
  and you need to know which canton''s rules apply and how they differ from other cantons.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Navigate Switzerland's 26-canton legal patchwork: map federal vs. cantonal authority, compare commercial register procedures and fees, model effective corporate and inheritance tax rates by canton, identify the correct labor court (Arbeitsgericht / Tribunal des prud'hommes) and civil court of first instance, understand real estate transfer taxes (Handänderungssteuer / droits de mutation) and land registry (Grundbuch / Registre foncier) requirements, clarify notarization obligations under the Staatliches vs. Freies Notariat distinction, and flag cantonal variations that affect entity formation, property transactions, succession planning, or litigation strategy. Use when a client's matter touches Switzerland and you need to know which canton's rules apply and how they differ from other cantons. Covers ZH Zurich, ZG Zug, GE Geneva, VD Vaud, BE Bern, BS Basel-Stadt, LU Lucerne, SG St. Gallen, AG Aargau, TI Ticino, VS Valais, SZ Schwyz, NW Nidwalden, OW Obwalden, and all remaining cantons. Jurisdiction: Switzerland.


# Legalcode CH Cantonal Law Navigator

> **Disclaimer**: This skill provides a framework for AI-assisted navigation of Swiss
> cantonal law variations. It does not constitute legal advice. All outputs must be
> reviewed by a qualified Swiss legal professional (Rechtsanwalt / avocat / avvocato)
> licensed in the relevant canton before use. Swiss law is subject to frequent cantonal
> amendment; verify currency of all cantonal references before relying on them. Statutory
> and case law references carry hallucination risk — verify against authoritative sources
> (fedlex.admin.ch, cantonal official gazettes) before acting. This skill covers Swiss
> domestic law only; cross-border EU matters require separate EU law analysis.

---

## Purpose and Scope

This skill navigates the interplay between federal Swiss law and the 26 cantonal legal
systems. It answers the question: _for this specific legal domain and this specific canton,
what rule applies — and how does it differ from the federal baseline and from other cantons?_

**Covers:**

- Federal vs. cantonal authority mapping across core legal domains
- Commercial register (Handelsregister / Registre du commerce / Registro di commercio)
  procedures, fees, and cantonal office variations
- Corporate, capital, wealth, and inheritance tax effective rates by canton
- Labor court (Arbeitsgericht / Tribunal des prud'hommes) structure per canton
- Civil courts of first instance and the cantonal court organization hierarchy
- Land registry (Grundbuch / Registre foncier / Registro fondiario) requirements and
  real estate transfer taxes (Handänderungssteuer / droits de mutation)
- Notarial systems (Staatliches Notariat vs. Freies Notariat) and acts requiring
  public deeds (öffentliche Urkunde / acte authentique)
- Cantonal inheritance and gift tax regimes
- Building permits and administrative procedures
- Professional licensing and bar admission

**Does not:**

- Provide legal advice or replace cantonal counsel
- Cover EU law or bilateral treaties in depth
- Substitute for a cantonal tax advisor for binding tax rulings
- Address federal-level FINMA, SECO, or competition law (separate skills required)
- Apply to Liechtenstein, which has its own separate legal system

---

## Jurisdiction and Governing Law

Switzerland is a civil-law confederation governed at three levels:

1. **Federal (Bundesrecht / Droit fédéral / Diritto federale)**: Applies uniformly to
   all 26 cantons. The Federal Constitution (BV/Cst.) [SR 101], Swiss Civil Code
   (ZGB/CC/CC) [SR 210], Code of Obligations (OR/CO/CO) [SR 220], Swiss Code of Civil
   Procedure (ZPO/CPC/CPC) [SR 272], and Criminal Code [SR 311.0] are all federal.
   Federal law prevails over cantonal law (Art. 49 BV [VERIFY currency]).

2. **Cantonal (Kantonsrecht / Droit cantonal / Diritto cantonale)**: Each of the 26
   cantons (including 6 half-cantons) exercises autonomous authority in areas not
   delegated to the Federation (Art. 3 BV). Key cantonal domains: taxes (cantonal and
   municipal), court organization, notariat, inheritance tax, building law.

3. **Municipal (Gemeinderecht / Droit communal)**: Over 2,100 municipalities add a
   further layer for zoning, local taxes, and building permits.

**Official Languages by Canton:**

| Language | German                                                                        | French                                          | Italian | Trilingual                                        |
| -------- | ----------------------------------------------------------------------------- | ----------------------------------------------- | ------- | ------------------------------------------------- |
| Cantons  | ZH, BE (part), LU, UR, SZ, OW, NW, GL, ZG, SO, BS, BL, SH, AR, AI, SG, AG, TG | GE, JU, NE, VD, BE (part), FR (part), VS (part) | TI      | GR (DE/IT/RM), VS (DE/FR), FR (DE/FR), BE (DE/FR) |

**Primacy rule**: Where cantonal law conflicts with federal law, federal law governs (Art.
49 BV). Cantons may legislate more strictly than the federal minimum but not more leniently
in areas of federal exclusive jurisdiction.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. The workflow pauses
and asks when:

- The answer would change the analysis materially (e.g., different canton = different tax rate)
- Multiple domains are involved and prioritization is needed
- The client's status (resident/non-resident, entity type) affects which cantonal rules apply
- Cantonal information is ambiguous or the user has not specified the canton

Use the ⟁ CLARIFY pattern wherever marked. If the user has already provided the information,
skip the question and proceed.

---

## Workflow

### Step 1: Accept the Query

Accept the query in any of these forms:

- **Specific question**: "What is the commercial register fee in Zug for a GmbH?"
- **Transaction scenario**: "Swiss AG acquiring property in Geneva — what transfer tax applies?"
- **Comparative question**: "Which canton has the lowest corporate tax rate?"
- **Compliance check**: "Does our client need a notarized deed for this Vaud real estate?"
- **Litigation question**: "Is there a commercial court in Ticino?"

If the query is incomplete (no canton specified, no entity type), proceed to Step 2.

### Step 2: Gather Context

**⟁ CLARIFY** — Before analyzing, ask:

1. **Which canton(s) are involved?**
   - Single canton: specify which one (e.g., Zurich, Zug, Geneva)
   - Multi-canton: list all cantons involved (e.g., entity in Zug, property in Valais)
   - Comparison: which cantons to compare (or "all major cantons")?
   - _Why this matters_: Rules vary significantly — the analysis is canton-specific.

2. **What legal domain(s) are relevant?**
   - Options: Commercial register | Corporate/capital tax | Inheritance/gift tax | Labor
     courts | Civil courts (litigation) | Land registry & transfer tax | Notariat | Building
     permits | Professional licensing | All applicable domains
   - Allow multiple selections.
   - _Why this matters_: Narrows the analysis to what the user actually needs.

3. **What is the client profile?**
   - Entity type: individual / AG (SA) / GmbH (Sàrl) / Kollektivgesellschaft / branch /
     foreign entity with Swiss operations
   - Residency status: Swiss resident / non-resident / EU/EFTA national / non-EU/EFTA
   - _Why this matters_: Lex Koller restrictions apply to non-residents; tax rates differ
     for legal entities vs. individuals; notarization requirements vary by act.

4. **What is the primary objective?**
   - Options: Entity formation | Property transaction | Tax planning / relocation |
     Succession planning | Litigation / dispute resolution | Compliance check | Pure comparison
   - _Why this matters_: Determines which cantonal domains to analyze and in what depth.

State all assumptions explicitly if the user provides partial context.

### Step 3: Map Federal vs. Cantonal Authority

Before diving into the specific domain, classify the legal question on the
**Federal/Cantonal/Municipal authority spectrum**. Use the Authority Map in the
**Domain Analysis** section below.

For each domain raised in the query:

- Identify whether the rule is FEDERAL (uniform), MIXED (federal framework + cantonal
  implementation), or CANTONAL (purely cantonal, varies canton to canton)
- Flag any MUNICIPAL layer (communal variation below cantonal)

**⟁ CLARIFY** — If the query mixes federal and cantonal questions (e.g., asking about
both labor law substance and labor court procedure), confirm whether to cover both or
focus on one:

- "Your question touches both substantive employment law (federal — OR Art. 319ff) and
  labor court procedure (cantonal organization). Should I cover both, or focus on the
  cantonal court structure?"

### Step 4: Navigate the Specific Domain(s)

Execute the deep domain analysis for each selected domain using the **Domain Analysis**
sections below. For each domain:

1. State the federal baseline (if any)
2. Identify the cantonal variation(s) specific to the queried canton(s)
3. Flag any RED issues (compliance risk, legal invalidity, material gap)
4. Provide the actionable output (verified rule, recommended action, reference source)

**⟁ CLARIFY** — For multi-canton queries, ask whether to produce:

- **Side-by-side comparison table**: Best for planning/selection decisions
- **Canton-by-canton narrative**: Best for compliance mapping across multiple locations
- **Priority-ranked summary**: Best when one canton matters most but context for others is needed

### Step 5: Build the Cantonal Variation Output

Compile the findings from Step 4 into the output format defined in **Output Format
Template** below. For each domain:

- Classify each rule as FEDERAL / MIXED / CANTONAL / MUNICIPAL
- Rate each cantonal variation as MATERIAL (affects strategy), ADVISORY (planning note),
  or CRITICAL (compliance risk / legal invalidity risk)
- Provide specific cantonal data (rate, article reference, office, processing time)

### Step 6: Flag Red Issues and Recommendations

After the domain analysis, surface any CRITICAL issues:

- Non-compliance risk (e.g., no notarized deed for a required transaction)
- Legal invalidity risk (e.g., document in wrong language for the canton)
- Material planning errors (e.g., incorporating in the wrong canton for tax purposes)
- Missed deadlines (e.g., intercantonal double tax relief filing window)
- Lex Koller restriction violations for foreign clients

**⟁ CLARIFY** — For CRITICAL issues where the risk level depends on deal context not yet
provided, ask before classifying:

- "The Geneva droits de mutation apply here, but the rate depends on whether the buyer
  is a natural person or legal entity. Can you confirm the buyer's status?"

### Step 7: Quality Verification

Before delivering the output:

1. Run the 5 Citation Quality Gates silently. Revise failures before delivery.
2. For any CRITICAL classification, run the 3-pass Self-Interrogation.
3. Confirm the governing language of the target canton — all document references should
   use the correct official-language name.
4. Verify all [VERIFY] tags are placed on any legal reference not confirmed from an
   authoritative source in this conversation.
5. Generate the Glass Box Audit Trail and append to the output.

---

## Domain Analysis Reference

### A. Federal vs. Cantonal Authority Map

Use this table to classify any Swiss legal question before analyzing it:

| Legal Domain                                    | Authority Level    | Federal Source                                            | Cantonal Variation                                                         |
| ----------------------------------------------- | ------------------ | --------------------------------------------------------- | -------------------------------------------------------------------------- |
| Contract law (formation, validity, performance) | FEDERAL            | OR (SR 220)                                               | None — uniform                                                             |
| Company law (AG, GmbH, foundation)              | FEDERAL            | OR Art. 620ff / 772ff                                     | None for substance; cantonal for notarization fees and register processing |
| Commercial register                             | MIXED              | OR Art. 927-943; HRegV (SR 221.411)                       | Cantonal offices, fees, processing times                                   |
| Corporate income tax (federal)                  | FEDERAL            | DBG (SR 642.11) — 8.5% of taxable profit                  | None for federal rate                                                      |
| Corporate income tax (cantonal + municipal)     | CANTONAL           | StHG (SR 642.14) harmonizes structure                     | Rates vary dramatically canton to canton                                   |
| Capital tax on equity                           | CANTONAL           | StHG Art. 29 (framework only)                             | Cantonal rates 0.001% – 0.5%                                               |
| Inheritance & gift tax                          | CANTONAL           | No federal inheritance tax                                | 26 different cantonal regimes                                              |
| Stamp duty (issuance tax)                       | FEDERAL            | StG (SR 641.10) — 1% on equity contributions above CHF 1M | None                                                                       |
| Individual income tax (federal)                 | FEDERAL            | DBG                                                       | None for federal                                                           |
| Individual income tax (cantonal + municipal)    | CANTONAL           | StHG framework                                            | Rates vary; effective rates differ substantially                           |
| Real estate gains tax                           | CANTONAL/MIXED     | No single federal rule                                    | Some cantons use income tax; others use special real estate gains tax      |
| Real estate transfer tax (Handänderungssteuer)  | CANTONAL           | None (no federal transfer tax)                            | Some cantons have none; rates 0.1% – 3%+                                   |
| Land registry (Grundbuch)                       | MIXED              | ZGB Art. 942-977 (federal framework)                      | Cantonal offices; notarization requirements; fees                          |
| Foreign land ownership (Lex Koller)             | FEDERAL            | ANRA (SR 211.412.41)                                      | Cantonal implementation; cantonal quotas for holiday homes                 |
| Agricultural land                               | FEDERAL            | BGBB (SR 211.412.11)                                      | Limited cantonal variation                                                 |
| Succession law (substantive)                    | FEDERAL            | ZGB Art. 457-640                                          | None for substance; cantonal for process                                   |
| Notarization (when required)                    | MIXED              | ZGB Art. 657, 184; OR Art. 629, 777 define when required  | Cantonal notariat organization, systems, fees                              |
| Civil procedure                                 | MIXED              | ZPO (SR 272) — federal procedure                          | Cantonal court organization (Art. 3 ZPO)                                   |
| Courts of first instance                        | CANTONAL           | BGG Art. 75 (two-instance requirement)                    | Cantonal court structure entirely cantonal                                 |
| Commercial courts                               | CANTONAL           | ZPO Art. 6 (optional)                                     | Only ZH, BE, SG, AG have Handelsgerichte                                   |
| Labor courts                                    | CANTONAL           | ZPO Art. 1 + OR Art. 343-347                              | Most cantons have specialized labor courts; some use ordinary civil courts |
| Building permits                                | CANTONAL/MUNICIPAL | RPG (SR 700) (federal framework)                          | Cantonal PBG/LAT; municipal BZO                                            |
| Bar admission / lawyer licensing                | CANTONAL           | BGFA (SR 935.61) (intercantonal freedom of movement)      | 26 cantonal bar examinations and registers                                 |
| Professional licensing (non-lawyers)            | CANTONAL           | Varies by profession                                      | Cantonal licensing requirements                                            |

---

### B. Commercial Registers (Handelsregister / Registre du Commerce / Registro di Commercio)

**Federal framework**: The commercial register is governed by OR Art. 927-943 [VERIFY
currency] and the Handelsregisterverordnung (HRegV) [SR 221.411]. The central aggregation
portal is **ZEFIX** (zefix.ch), which indexes all 28 cantonal registers. Entries in any
cantonal register are legally valid across Switzerland.

**Why cantonal offices matter**: Despite the federal framework, each canton operates its
own register office with distinct:

- Processing times (same-day in Zug; 1-2 weeks in some cantons)
- Fee structures (cantonal fee schedules)
- Document language requirements (German in ZH; French in GE; Italian in TI)
- Digital filing capabilities

**Key cantonal characteristics:**

| Canton           | Office Name                                | Language | Approx. Processing | Notable Feature                                                     |
| ---------------- | ------------------------------------------ | -------- | ------------------ | ------------------------------------------------------------------- |
| ZH (Zurich)      | Handelsregisteramt des Kantons Zürich      | DE       | 3-7 business days  | Largest volume; robust digital portal                               |
| ZG (Zug)         | Handelsregisteramt des Kantons Zug         | DE       | 24-48 hours        | [VERIFY] Fastest in Switzerland; low fees attract holding companies |
| GE (Geneva)      | Office du Registre du commerce             | FR       | 5-10 business days | Bipartite court-supervised process; French only                     |
| VD (Vaud)        | Registre du commerce du canton de Vaud     | FR       | 5-10 business days | Lausanne-based; life sciences sector concentration                  |
| BE (Bern)        | Handelsregisteramt des Kantons Bern        | DE/FR    | 5-10 business days | Bilingual canton; documents accepted in DE and FR                   |
| BS (Basel-Stadt) | Handelsregisteramt des Kantons Basel-Stadt | DE       | 3-7 business days  | Pharma/life sciences hub                                            |
| TI (Ticino)      | Registro di commercio del Cantone Ticino   | IT       | 5-10 business days | Italian-language only; proximity to Italian market                  |
| SZ (Schwyz)      | Handelsregisteramt des Kantons Schwyz      | DE       | 3-7 business days  | Tax-advantaged; no cantonal inheritance tax                         |
| SG (St. Gallen)  | Handelsregisteramt des Kantons St. Gallen  | DE       | 3-7 business days  | Has commercial court (Handelsgericht)                               |
| AG (Aargau)      | Handelsregisteramt des Kantons Aargau      | DE       | 3-7 business days  | Has commercial court (Handelsgericht)                               |

**Registration requirements by entity type** (same across cantons — federal law):

| Entity                              | Threshold / Requirement                       | Notarized Deed Required? |
| ----------------------------------- | --------------------------------------------- | ------------------------ |
| AG (SA/SA)                          | Must register; min. capital CHF 100,000       | Yes — OR Art. 629        |
| GmbH (Sàrl/Sagl)                    | Must register; min. capital CHF 20,000        | Yes — OR Art. 777        |
| Kollektivgesellschaft               | Must register if commercial enterprise        | No                       |
| Einzelunternehmen (Sole proprietor) | Must register if annual revenue ≥ CHF 100,000 | No                       |
| Branch of foreign entity            | Must register                                 | No                       |

**CRITICAL**: All register entries are published in the Swiss Official Gazette of Commerce
(Schweizerisches Handelsamtsblatt / SHAB) and become effective on publication. Searching
ZEFIX alone is sufficient for existence check; individual cantonal register for certified
extract (Handelsregisterauszug).

---

### C. Cantonal Corporate and Capital Tax

**Tax layering**: A Swiss company pays three layers of tax:

1. **Federal corporate income tax**: 8.5% of taxable profit (flat, uniform) — DBG [SR 642.11]
2. **Cantonal corporate income tax**: Varies by canton (see table below)
3. **Municipal corporate income tax**: A multiplier on the cantonal tax (typically 50–150%
   of cantonal tax), varying by municipality within each canton

**Tax harmonization (StHG [SR 642.14])**: Harmonizes the _structure_ (tax base, procedure,
assessment method) but NOT the _rates_. Cantons can set their own rates freely within the
StHG framework.

**Effective combined corporate tax rates (federal + cantonal + municipal, approximate):**

| Canton           | Low Est. | High Est. | Notes                                                                |
| ---------------- | -------- | --------- | -------------------------------------------------------------------- |
| ZG (Zug)         | 11.5%    | 12.5%     | [VERIFY] One of the lowest; attractive for holding companies         |
| NW (Nidwalden)   | 11.5%    | 12.5%     | [VERIFY] Consistently low; competes with Zug                         |
| OW (Obwalden)    | 12.5%    | 13.5%     | [VERIFY] Low rate; no inheritance tax                                |
| SZ (Schwyz)      | 12.0%    | 13.0%     | [VERIFY] Low rate; no inheritance tax; Küssnacht exemption zones     |
| LU (Lucerne)     | 12.0%    | 13.0%     | [VERIFY] Reformed; competitive for central Switzerland               |
| BS (Basel-Stadt) | 13.0%    | 14.0%     | [VERIFY] Post-reform improvement; still higher than ZG               |
| GE (Geneva)      | 13.5%    | 14.5%     | [VERIFY] Post-BEPS reform; reduced from historic highs               |
| VD (Vaud)        | 13.5%    | 14.5%     | [VERIFY] BEPS-driven reform; life sciences incentives                |
| TI (Ticino)      | 14.0%    | 16.0%     | [VERIFY] Italian-facing; border company structures                   |
| ZH (Zurich)      | 19.0%    | 21.0%     | [VERIFY] Higher than low-tax cantons; quality infrastructure         |
| BE (Bern)        | 20.5%    | 22.0%     | [VERIFY] Federal capital; higher rates; municipal multipliers matter |

**[VERIFY all tax rates against current ESTV publications before advising — rates change
with cantonal tax reforms and municipal multiplier adjustments.]**

**Capital tax on equity (Kapitalsteuer)**:

- CANTONAL only — no federal capital tax
- Assessed on net equity (paid-in capital + reserves)
- Range: ~0.001% (Zug, Obwalden) to ~0.5% (some cantons) [VERIFY]
- Most cantons allow a credit against the capital tax equal to the income tax paid
- Material for holding companies with large balance sheets and modest operating income

**Inter-cantonal double taxation**:

- Switzerland prohibits intercantonal double taxation (principle established in federal case law)
- Relief mechanism: profit and capital allocated between cantons based on activity/payroll
- Filing requirement: taxpayer must proactively claim relief; no automatic federal offset
- CRITICAL: Missing the cantonal filing deadline forfeits relief — verify deadline with each canton

---

### D. Labor Courts (Arbeitsgericht / Tribunal des Prud'hommes / Tribunale di Conciliazione)

**Federal substantive law**: Individual employment contracts are governed by OR Art. 319-362
(Code of Obligations) — uniform across all cantons. The Swiss Code of Civil Procedure (ZPO)
[SR 272] governs procedure — uniform.

**Cantonal variation**: Court _organization_ is entirely cantonal (Art. 3 ZPO). Cantons
may establish specialized labor courts or route labor disputes through ordinary civil courts.

**ZPO key rules for labor disputes** (uniform):

- Disputes up to CHF 30,000: simplified procedure; no lawyers required; no court fee
- All labor disputes: mandatory conciliation attempt before court filing (Art. 197ff ZPO)
  (except where court acts as conciliation authority itself)
- Appeals: to cantonal appellate court, then to Federal Supreme Court (Bundesgericht)
  in Lausanne for disputes > CHF 15,000

**Cantonal court structures for labor disputes:**

| Canton           | Labor Court Type                                        | Notes                                                             |
| ---------------- | ------------------------------------------------------- | ----------------------------------------------------------------- |
| ZH (Zurich)      | Arbeitsgericht Zürich (standalone)                      | Paritätisch (employer + employee representatives); sits in Zurich |
| GE (Geneva)      | Tribunal des prud'hommes                                | French-style paritätisch court; specialized chambers by industry  |
| VD (Vaud)        | Tribunal des prud'hommes                                | Industry-based chambers; conciliation before the court            |
| BE (Bern)        | Regionalgericht (ordinary court)                        | No specialized labor court; labor disputes in civil division      |
| BS (Basel-Stadt) | Arbeitsgericht Basel                                    | Specialized; paritätisch composition                              |
| LU (Lucerne)     | Bezirksgericht (ordinary court)                         | No specialized labor court                                        |
| ZG (Zug)         | Kantonsgericht (ordinary court)                         | Small canton; no specialized labor court                          |
| SG (St. Gallen)  | Kreisgericht (ordinary court)                           | No specialized labor court                                        |
| AG (Aargau)      | Bezirksgericht (ordinary court)                         | No specialized labor court                                        |
| TI (Ticino)      | Tribunale di appello, Sezione civile (via lower courts) | Italian-language; specialized labor division at appellate level   |
| SZ (Schwyz)      | Bezirksgericht (ordinary court)                         | Small canton; no specialized court                                |

**ADVISORY**: In cantons without specialized labor courts, employment disputes are handled
by general civil judges who may have less employment law expertise. Consider this in
litigation strategy — expert witnesses and detailed submissions become more important.

**Conciliation**: Before filing in ANY canton, a conciliation attempt is mandatory (ZPO
Art. 197). The authority conducting conciliation varies by canton. Exemptions exist for
clear-value disputes and collective matters.

---

### E. Courts of First Instance (Erstinstanzliche Gerichte / Tribunaux de Première Instance)

**Federal framework**: The ZPO [SR 272] governs civil procedure uniformly. The Federal
Court Act (BGG [SR 173.110]) Art. 75 requires at least two cantonal instances before
Federal Supreme Court access.

**Court organization is entirely cantonal**: Each canton has its own court names, structure,
and competence thresholds.

**Standard structure** (varies by canton):

| Canton | First Instance                                                | Second Instance                | Notes                                                      |
| ------ | ------------------------------------------------------------- | ------------------------------ | ---------------------------------------------------------- |
| ZH     | Bezirksgericht                                                | Obergericht des Kantons Zürich | Also has Handelsgericht for commercial disputes            |
| GE     | Tribunal de première instance                                 | Cour de justice                | French-language; Geneva-specific procedural culture        |
| VD     | Tribunal d'arrondissement                                     | Cour d'appel civile            | Lausanne seat                                              |
| BE     | Regionalgericht                                               | Obergericht des Kantons Bern   | Also has Handelsgericht                                    |
| BS     | Zivilgericht                                                  | Appellationsgericht            | City-canton; compact structure                             |
| LU     | Bezirksgericht                                                | Kantonsgericht                 | Cantonal court serves as second instance                   |
| ZG     | Kantonsgericht (sole instance for most matters above CHF 30K) | Obergericht                    | Small canton; Kantonsgericht often acts as direct instance |
| SG     | Kreisgericht                                                  | Kantonsgericht                 | Also has Handelsgericht                                    |
| AG     | Bezirksgericht                                                | Obergericht                    | Also has Handelsgericht                                    |
| TI     | Pretura / Tribunale d'appello                                 | Tribunale cantonale            | Italian-language proceedings                               |
| SZ     | Bezirksgericht                                                | Kantonsgericht                 |                                                            |
| GR     | Regionalgericht                                               | Kantonsgericht                 | Trilingual proceedings (DE/IT/RM)                          |

**Commercial Courts (Handelsgericht)** — available ONLY in:

- **Zurich (ZH)**: Handelsgericht Zürich — ZPO Art. 6; for commercial disputes where
  both parties are registered in the commercial register and dispute value > CHF 30,000
- **Bern (BE)**: Handelsgericht des Kantons Bern
- **St. Gallen (SG)**: Handelsgericht des Kantons St. Gallen
- **Aargau (AG)**: Handelsgericht des Kantons Aargau

**CRITICAL**: In all other cantons, commercial disputes go to ordinary civil courts.
A Handelsgericht is a single-instance court (Art. 6 ZPO) — direct appeal to Federal
Supreme Court. This significantly shortens the litigation path but removes one appellate level.

**Federal Supreme Court (Bundesgericht)**: Seat in Lausanne. Not a cantonal court. Reviews
cantonal decisions on questions of law; facts are final as decided by cantons. Threshold:
CHF 30,000 for monetary disputes (BGG Art. 74).

---

### F. Land Registry and Real Estate Transfer Tax

**Federal framework**: The land registry (Grundbuch) is governed by ZGB Art. 942-977
[SR 210]. Registration creates legal title (Art. 656 ZGB) — no registration = no ownership.
Every canton maintains its own cantonal land registry office (Grundbuchamt / Office du
Registre foncier / Ufficio del Registro fondiario).

**Notarization for real estate transfers**: Art. 657 ZGB requires an authentic document
(öffentliche Urkunde) for any agreement to transfer real estate. The notary must be
authorized in the canton of the property location.

**Real estate transfer tax (Handänderungssteuer / Droits de mutation)**:

- **CANTONAL only** — no federal transfer tax
- Many cantons have NO cantonal transfer tax (but municipalities may charge separately)
- Where they exist, rates vary significantly

| Canton      | Transfer Tax              | Rate (approx.)                 | Payer        | Notes                                               |
| ----------- | ------------------------- | ------------------------------ | ------------ | --------------------------------------------------- |
| ZH          | None at cantonal level    | 0%                             | N/A          | Some municipalities charge; Zurich city: 0%         |
| ZG          | Yes                       | ~0.15–0.2% [VERIFY]            | Buyer        | Low rate; competitive canton                        |
| GE          | Yes — Droits de mutation  | ~3% (natural persons) [VERIFY] | Buyer        | One of the highest; additional notary fees separate |
| VD          | Yes — Droits de mutation  | ~2.2% [VERIFY]                 | Buyer        | Life sciences canton; high property values          |
| BE          | Yes — Handänderungssteuer | ~1.8% [VERIFY]                 | Buyer/Seller | Cantonal rate + municipal surcharge possible        |
| BS          | Yes                       | ~0.2% [VERIFY]                 | Buyer        | Lower than GE/VD                                    |
| BL          | Yes                       | ~0.2% [VERIFY]                 | Buyer        |                                                     |
| LU          | Yes                       | ~1.5–2% [VERIFY]               | Buyer        |                                                     |
| SZ          | None                      | 0%                             | N/A          | Tax-advantaged canton                               |
| NW          | Yes                       | ~0.2% [VERIFY]                 | Buyer        | Low rate                                            |
| OW          | Yes                       | ~0.15% [VERIFY]                | Buyer        | Low rate                                            |
| TI          | Yes — Tassa di mutazione  | ~2% [VERIFY]                   | Buyer        | Italian-language process                            |
| VS (Valais) | Yes — Droits de mutation  | ~1% [VERIFY]                   | Buyer        | Holiday home restrictions apply                     |
| GR          | Yes                       | ~0.2% [VERIFY]                 | Buyer        | Romansh areas have specific procedures              |

**[VERIFY all rates with current cantonal tax authority before any transaction closing —
rates are subject to frequent municipal adjustment.]**

**Land registry fees**: Separate from transfer tax. Typically 0.1–0.5% of transaction
value for the registration act. Cantonal fee schedules apply.

**Lex Koller (ANRA [SR 211.412.41])**: Federal law restricting real estate acquisition by
non-residents (foreign nationals without Swiss residence permit, non-resident EU/EFTA
nationals). Key rules:

- Commercial property: generally exempt from restrictions
- Primary residence (Hauptwohnung): permitted for buyers intending to live in Switzerland
- Holiday homes: restricted to ~1,500 units/year nationally, allocated by canton; size
  limits apply (~200 m²); resale restrictions; prior authorization required [VERIFY]
- Cantons with active holiday home quotas: VS (Valais), GR (Graubünden), TI (Ticino)
- Cantons with limited demand for permits: ZG, ZH (few holiday home transactions)

**Agricultural land**: Additional federal restrictions under BGBB [SR 211.412.11] —
structural integrity rules apply regardless of canton.

---

### G. Notarial Systems (Notariat / Notariat / Notariato)

**Two main systems exist across cantons**:

**Staatliches Notariat / Notariat d'État (Official/State Notariat)**:

- Notaries are cantonal civil servants (Beamte)
- Employed by cantonal government
- Fee schedules set by canton (typically lower and uniform)
- **Cantons**: ZH (Amtsnotariat), SH, GL, and others [VERIFY current list]

**Freies / Freiberufliches Notariat (Liberal / Self-Employed Notariat)**:

- Notaries are self-employed licensed professionals
- Subject to cantonal supervision but set fees within tariffs
- Fee schedules can vary between individual notaries
- **Cantons**: GE, VD, VS, FR, NE, JU, BE (for French-speaking parts), TI, BS, BL,
  LU, SZ, ZG, SG, AG, AR, AI, GR, and others [VERIFY current list]

**When notarization (public deed / öffentliche Urkunde) is legally required:**

| Act                                          | Federal Basis      | Requirement                                        |
| -------------------------------------------- | ------------------ | -------------------------------------------------- |
| Real estate purchase agreement (Kaufvertrag) | ZGB Art. 657       | Public deed — ALWAYS; notary in canton of property |
| AG (SA) formation                            | OR Art. 629        | Public deed for founding act (Gründungsakt)        |
| GmbH (Sàrl) formation                        | OR Art. 777        | Public deed for founding act                       |
| Marriage contract (Ehevertrag)               | ZGB Art. 184       | Public deed — must be authenticated by notary      |
| Donation of real property                    | ZGB Art. 657 + 243 | Public deed                                        |
| Capital increase (AG)                        | OR Art. 650        | Public deed                                        |
| Real estate mortgage (Grundpfandrecht)       | ZGB Art. 799       | Public deed                                        |
| Permanent and building rights (Baurecht)     | ZGB Art. 779       | Public deed                                        |

**Intercantonal validity**: A public deed executed by an authorized notary in one canton
is valid throughout Switzerland. However, the act must be lodged with the register office
of the canton where the property or company is located.

**ADVISORY**: Notary fees vary substantially between cantonal systems and between
individual notaries in liberal cantons. For high-value transactions, obtain fee estimates
from multiple notaries before engagement.

---

### H. Cantonal Inheritance and Gift Tax

**No federal inheritance or gift tax**: Unlike most EU countries, Switzerland levies NO
federal inheritance or gift tax. All inheritance and gift taxation is CANTONAL — and
varies dramatically.

**The two tax-free cantons:**

| Canton        | Inheritance Tax | Gift Tax | Notes                                                |
| ------------- | --------------- | -------- | ---------------------------------------------------- |
| SZ (Schwyz)   | None            | None     | Only canton with no cantonal inheritance OR gift tax |
| OW (Obwalden) | None            | None     | One of the lowest-tax cantons overall                |

**Exemptions for spouses and descendants (most cantons)**:
Most cantons exempt spouses and lineal descendants (children, grandchildren) from
inheritance tax. **Exceptions — cantons that tax direct descendants:**

- Appenzell Innerrhoden (AI): taxes certain transfers [VERIFY]
- Neuchâtel (NE): taxes transfers to descendants above exemption threshold [VERIFY]
- Vaud (VD): taxes lineal descendants above exemption amounts [VERIFY]

**Indicative rates for non-family heirs (highly variable — [VERIFY all]):**

| Canton           | Rate Range (non-relatives) | Rate (siblings) | Notes                                 |
| ---------------- | -------------------------- | --------------- | ------------------------------------- |
| ZH (Zurich)      | 15–20%                     | 4–10%           | Progressive by amount and kinship     |
| BE (Bern)        | ~25–50%                    | ~20–25%         | Significant for non-relatives         |
| GE (Geneva)      | Progressive, up to 26%     | ~6%             | French-style progression              |
| VD (Vaud)        | Up to 50%                  | Moderate        | Highest rates in CH for non-relatives |
| ZG (Zug)         | Moderate                   | Low             | Competitive with low corporate rates  |
| BS (Basel-Stadt) | ~12–25%                    | ~12%            |                                       |
| SZ (Schwyz)      | 0%                         | 0%              | Tax-free jurisdiction                 |
| OW (Obwalden)    | 0%                         | 0%              | Tax-free jurisdiction                 |
| TI (Ticino)      | Moderate                   | Low             | Italian-style structure               |

**[VERIFY all rates with the cantonal tax authority or current ESTV publication before
estate planning advice.]**

**Intercantonal inheritance tax allocation**:

- Movable assets (bank accounts, securities, personal property): taxed in the canton of
  the deceased's last domicile
- Immovable assets (real estate): taxed in the canton where the property is located,
  regardless of domicile

**Federal succession law reform (effective 2023)**: Compulsory portions (Pflichtteile)
reduced — children's share: ½ of statutory entitlement (down from ¾); parents no longer
have compulsory portion. Increased testamentary freedom, but forced heirship cannot be
circumvented by choice-of-law (PILA amendment 2025).

**EU Succession Regulation (EU 650/2012)**: Does NOT apply to Switzerland. For clients
with assets in both Switzerland and EU member states, separate succession plans are
required under each applicable legal system.

---

### I. Building Permits and Administrative Procedures

**Three-level structure**:

1. **Federal**: Land use planning (Raumplanungsgesetz, RPG [SR 700]) sets the framework;
   limits urban sprawl; defines zones
2. **Cantonal**: Planning and Building Law (Planungs- und Baugesetz, PBG — each canton
   has its own version) sets cantonal rules
3. **Municipal**: Building and Zoning Ordinance (Bau- und Zonenordnung, BZO) sets
   local rules for each municipality

**Key cantonal variation**:

- Processing times: 2 weeks (minor works in small cantons) to 12–24 months (large
  projects in urban cantons with neighbor objection processes)
- Neighbor objection rights: some cantons allow any affected neighbor; others restrict
  to directly adjacent properties
- Heritage/design review: urban cantons (ZH, GE, BS) have architectural review boards;
  rural cantons typically do not
- Environmental impact assessment thresholds: vary by canton

**CRITICAL**: For multi-canton development projects, obtain separate building permits in
EACH municipality. No cross-cantonal permit recognition exists.

---

## Cantonal Quick Reference Matrix

Reference matrix for the 10 most commercially significant cantons across all six domains:

| Domain               | ZH Zurich               | ZG Zug               | GE Geneva                | VD Vaud                  | BE Bern              | BS Basel       | LU Lucerne           | SZ Schwyz            | SG St.Gallen         | TI Ticino            |
| -------------------- | ----------------------- | -------------------- | ------------------------ | ------------------------ | -------------------- | -------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| **Corp. Tax (est.)** | ~19-21%                 | ~11-12%              | ~13-14%                  | ~13-14%                  | ~21%                 | ~13-14%        | ~12-13%              | ~12-13%              | ~16%                 | ~14-16%              |
| **Transfer Tax**     | None (cantonal)         | ~0.2%                | ~3%                      | ~2.2%                    | ~1.8%                | ~0.2%          | ~1.5%                | None                 | Yes                  | ~2%                  |
| **Inheritance Tax**  | Yes                     | Yes                  | Yes                      | Yes (incl. descendants)  | Yes                  | Yes            | Yes                  | **None**             | Yes                  | Yes                  |
| **Handelsgericht**   | **Yes**                 | No                   | No                       | No                       | **Yes**              | No             | No                   | No                   | **Yes**              | No                   |
| **Labor Court**      | Separate Arbeitsgericht | Ordinary civil court | Tribunal des prud'hommes | Tribunal des prud'hommes | Ordinary civil court | Arbeitsgericht | Ordinary civil court | Ordinary civil court | Ordinary civil court | Specialized division |
| **Register Lang.**   | German                  | German               | French                   | French                   | DE/FR                | German         | German               | German               | German               | Italian              |
| **Notariat Type**    | Staatlich (Amt)         | Liberal              | Liberal                  | Liberal                  | Liberal              | Liberal        | Liberal              | Liberal              | Liberal              | Liberal              |
| **Capital Tax**      | Yes                     | Low                  | Yes                      | Yes                      | Yes                  | Yes            | Yes                  | Low                  | Yes                  | Yes                  |

_[VERIFY all rates and classifications — cantonal law changes frequently.]_

---

## Severity and Priority Classification

### Rule Classification

| Classification | Meaning                                              | Example                                                                                          |
| -------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **FEDERAL**    | Uniform across all 26 cantons; no cantonal variation | OR contract law; DBG federal income tax rate                                                     |
| **MIXED**      | Federal framework; cantonal implementation varies    | Commercial register (HRegV framework; cantonal office); ZPO (uniform procedure; cantonal courts) |
| **CANTONAL**   | No federal rule; varies canton to canton             | Cantonal income tax rates; inheritance tax; transfer tax; Handelsgericht existence               |
| **MUNICIPAL**  | Further variation at municipality level below canton | Local building codes; municipal tax multipliers; local transfer tax surcharges                   |

### Issue Severity

| Severity     | Meaning                                                                            | Action                                                                  |
| ------------ | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **CRITICAL** | Compliance risk, potential legal invalidity, or material loss if not addressed     | Halt and correct before proceeding; engage cantonal counsel immediately |
| **MATERIAL** | Significant variance affecting planning, tax, or strategy; not immediately invalid | Factor into advice; verify with cantonal specialist before finalizing   |
| **ADVISORY** | Planning consideration; no immediate compliance risk                               | Note for client; include in planning memo                               |

### Planning Priority Tiers

**Tier 1 — Pre-transaction Verification** (must verify before any transaction):

- Notarization requirement and correct cantonal notary
- Lex Koller authorization (if foreign buyer)
- Transfer tax rate in the specific canton
- Commercial register language and filing requirements

**Tier 2 — Strategic Planning** (verify before entity/domicile decision):

- Effective corporate tax rate (cantonal + federal + municipal)
- Inheritance tax exposure for succession planning
- Handelsgericht availability for dispute resolution strategy
- Capital tax impact for holding companies

**Tier 3 — Operational Awareness** (verify before ongoing operations):

- Labor court structure for the canton where employees are based
- Building permit timelines for real estate development
- Bar admission requirements for external counsel engagement
- Intercantonal double taxation relief filing deadlines

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                        | Fail Action                                                        |
| -------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Source**     | Every cantonal rule cites a specific statute, ordinance, or cantonal tariff                 | Add citation or mark [UNVERIFIED — verify with cantonal authority] |
| **Format**     | Citations use the SR number (federal) or canton abbreviation + law name (cantonal)          | Fix format to standard Swiss citation style                        |
| **Currency**   | Every tax rate, fee schedule, and procedural rule flagged as subject to change              | Add [VERIFY currency — rates change with cantonal reforms]         |
| **Domain**     | Analysis stays within the correct jurisdiction — no EU law assumptions applied to Swiss law | Remove or flag with [JURISDICTION NOTE]                            |
| **Confidence** | Uncertainty about cantonal variation explicitly stated                                      | Add confidence qualifier; add [VERIFY] tag                         |

---

## Self-Interrogation for CRITICAL Items

For any issue classified CRITICAL, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the CRITICAL classification follow logically from the cantonal rule cited?
- Is the cited rule actually cantonal (not federal) — am I correctly attributing the variation?
- Could a counterargument reduce the risk to MATERIAL?

**Pass 2 — Completeness**:

- Have all relevant levels been checked — federal, cantonal, AND municipal?
- Have I verified the official language of the canton for document requirements?
- Have I confirmed whether the specific canton is a Handelsgericht canton or not?

**Pass 3 — Challenge**:

- What is the strongest argument that the CRITICAL issue is manageable?
- Under what circumstances might a competent cantonal practitioner resolve this risk?
- Is this truly CRITICAL or is it a MATERIAL issue that can be mitigated with proper structuring?

Mark the audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

---

## Confidence Scoring

| Level        | Range     | Meaning                                                    | Action                                                         |
| ------------ | --------- | ---------------------------------------------------------- | -------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Federal rule clearly stated in statute                     | State with confidence; cite SR number                          |
| **High**     | 0.80–0.94 | Cantonal rule verified from authoritative cantonal source  | State with brief caveat; cite cantonal source                  |
| **Probable** | 0.60–0.79 | General cantonal pattern consistent with majority practice | State with reasoning; add [VERIFY with cantonal authority]     |
| **Possible** | 0.40–0.59 | Cantonal variation uncertain or in flux                    | Flag for cantonal counsel review; present both possibilities   |
| **Unlikely** | 0.0–0.39  | Weak basis; cantonal rule not confirmed                    | Do not assert; flag as [UNCERTAIN — cantonal counsel required] |

Assign confidence scores to each cantonal-specific statement in the output.

---

## Glass Box Audit Trail

Append this YAML block to every output:

```yaml
glass_box:
  skill_name: "legalcode-ch-cantonal-law-navigator"
  mode: "Created from scratch — Mode A"
  topic: "Swiss cantonal law navigation"
  jurisdiction: "Switzerland — 26 cantons"
  query_canton(s): "[List of cantons queried]"
  domain(s): "[List of domains analyzed]"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[Path or 'Not created']"
  federal_rules_cited: "[Number]"
  cantonal_rules_cited: "[Number]"
  critical_issues: "[Number]"
  material_issues: "[Number]"
  advisory_issues: "[Number]"
  citations_verified: "[Number VERIFIED] / [Number UNVERIFIED — marked [VERIFY]]"
  confidence_overall: "HIGH / MEDIUM / LOW — [rationale]"
  self_interrogation: "PASS / REVISED / N/A — [description of revision if applicable]"
  language_of_target_canton: "[German / French / Italian / Romansh / Bilingual]"
  limitations:
    - "Tax rates reflect publicly available estimates; verify with current ESTV publications"
    - "Cantonal law changes frequently; currency of all cantonal references must be verified"
    - "This output does not substitute for cantonal counsel advice"
    - "Municipal-level variations (building codes, local tax multipliers) not fully analyzed"
  reviewer: "AI-assisted — requires qualified Swiss legal professional review"
```

---

## Anti-patterns Catalogue

The following errors are the most common sources of failure when navigating Swiss cantonal law:

1. **Applying Zurich rules to all cantons** — Assuming ZH practice is Swiss practice.
   ZH is the largest canton but represents one of 26 systems. Zug, Geneva, and Bern all
   differ materially on commercial courts, transfer tax, and notarial systems. Always
   verify canton-specifically.

2. **Ignoring the language of the target canton** — Submitting German-language documents
   to a French-speaking canton (GE, VD) or Italian-speaking canton (TI) without proper
   translation may render the document inadmissible or require costly re-execution.
   Match the document language to the canton's official language.

3. **Assuming all cantons have a Handelsgericht** — Only ZH, BE, SG, and AG have
   commercial courts. In all other cantons, commercial disputes go to ordinary civil
   courts. This affects litigation strategy, procedural timelines, and the availability
   of commercially specialized judges.

4. **Confusing the transfer tax rate with the land registry fee** — Two separate charges
   apply to real estate transactions: the cantonal transfer tax (Handänderungssteuer)
   AND the land registry registration fee. Some cantons have zero transfer tax (ZH, SZ)
   but all have land registry fees. Quote both separately.

5. **Forgetting the municipal tax multiplier** — Effective corporate and individual tax
   rates include a municipal multiplier (Gemeindesteuerfuss / centimes additionnels) on
   top of cantonal tax. The same canton can have materially different effective rates
   between municipalities. Always check the municipal multiplier for the specific commune.

6. **Not checking Lex Koller before property advice to non-residents** — Foreign buyers
   without Swiss residence permits need prior authorization for residential real estate.
   Assuming the purchase is unrestricted without checking is a CRITICAL error. Engage the
   cantonal land registry early for Lex Koller pre-clearance.

7. **Missing the notary-in-canton-of-property requirement** — For real estate transfers,
   the notary must be authorized in the canton where the property is located (not the
   buyer's or seller's canton). A Zurich notary cannot authenticate a Geneva property sale.

8. **Planning inheritance without checking the domicile canton's tax regime** — Most
   Swiss high-net-worth individuals can reduce inheritance tax significantly by relocating
   domicile to Schwyz or Obwalden (both have no cantonal inheritance tax). Failure to
   surface this option in estate planning is a material advisory gap.

9. **Missing the intercantonal double tax relief filing deadline** — When a business
   operates in multiple cantons, profit and capital are allocated between them. If double
   taxation occurs, relief must be claimed proactively within the cantonal deadline.
   Missing the deadline forfeits relief — there is no automatic federal offset mechanism.

10. **Treating Konkordats (intercantonal agreements) as universally binding** — Konkordats
    bind only the signatory cantons. A tax coordination Konkordat may not apply if one
    canton involved is a non-signatory. Verify signatory status before relying on Konkordat.

11. **Assuming Swiss civil procedure is uniform down to the court level** — While the ZPO
    is federal (uniform procedure), court organization — names, competence thresholds,
    chamber structure, judge composition — is entirely cantonal. A "Bezirksgericht" in
    one canton is not the same as a "Regionalgericht" in another in terms of jurisdiction.

12. **Confusing cantonal bar licensing with federal practice rights** — The Federal Act
    on Freedom of Movement for Lawyers (BGFA [SR 935.61]) allows lawyers registered in
    one canton to appear in courts of other cantons. BUT: disciplinary rules of BOTH the
    registration canton and the forum canton apply. Do not assume a Zurich bar card is
    sufficient for a long-term Geneva practice.

13. **Applying EU Succession Regulation (EU 650/2012) to Swiss estates** — Switzerland
    is not an EU member and does not apply the Brussels IV Succession Regulation. Swiss
    forced heirship rules (Pflichtteile) apply to Swiss estates and cannot be circumvented
    by EU choice-of-law provisions. Cross-border EU-Switzerland succession requires
    separate legal analysis for each jurisdiction.

14. **Ignoring agricultural land restrictions (BGBB)** — Federal law (BGBB [SR 211.412.11])
    restricts agricultural land acquisitions (fragmentation prohibition, price controls,
    acquisition authorization). These restrictions apply regardless of canton and override
    cantonal building or zoning law.

15. **Confusing the Zefix central index with an official register extract** — Zefix
    (zefix.ch) is a federal aggregation portal — useful for existence searches but does
    NOT replace a certified cantonal register extract (Handelsregisterauszug). Courts,
    notaries, and public authorities require the official cantonal extract for legal proceedings.

16. **Overlooking municipal building ordinance variations within the same canton** — Even
    within a single canton, each municipality has its own Bau- und Zonenordnung (BZO).
    A project permitted under cantonal PBG may still require a separate municipal permit.
    Multi-site developments require site-specific permit analysis for each municipality.

17. **Assuming the same notarial fee structure across cantons** — In Staatliches Notariat
    cantons, fees are fixed by cantonal tariff. In Freies Notariat cantons, individual
    notaries may charge within tariff ranges. For high-value transactions, compare cantonal
    notary tariffs before selecting the canton for a transaction.

18. **Failing to verify the conciliation authority before filing in labor courts** — All
    Swiss labor disputes require a mandatory conciliation attempt (ZPO Art. 197). The
    conciliation authority varies by canton (sometimes the Arbeitsgericht itself, sometimes
    a separate Schlichtungsbehörde). Filing directly in court without first going through
    conciliation results in the action being dismissed.

19. **Underestimating building permit timelines for Swiss real estate development** —
    Permit timelines vary from weeks (minor works, rural canton) to 2+ years (major
    development, urban canton, neighbor objections, environmental review). Factor realistic
    cantonal timelines into project schedules before committing to financing or lease
    obligations contingent on permit receipt.

20. **Treating Vaud, Bern, and Fribourg as French-speaking cantons only** — These are
    bilingual cantons. Bern and Fribourg have both German-speaking and French-speaking
    regions; legal proceedings and documents must be in the language of the specific
    municipality or district within the canton, not just the canton's dominant language.

---

## Writing Standards

Before delivering any output:

- [ ] **Accuracy over completeness**: Flag [VERIFY] on any cantonal claim not confirmed
      from an authoritative source rather than stating it with false confidence
- [ ] **Canton precision**: Never use "Swiss law requires X" when the rule is cantonal.
      Always identify the specific canton or use "most cantons" / "some cantons" with examples
- [ ] **Language precision**: Use the official-language name for the institution (e.g.,
      "Tribunal des prud'hommes" in GE, not "labor court" or "Arbeitsgericht")
- [ ] **Three-name awareness**: For trilingual terms (Handelsregister / Registre du
      commerce / Registro di commercio), use the language-appropriate term for the canton
- [ ] **Rate currency**: Explicitly flag all tax rates as approximate and subject to
      change with [VERIFY with ESTV/cantonal tax authority]
- [ ] **Plain-language summary**: After any technical cantonal analysis, include a 2-3
      sentence plain-language summary of the practical implication for the client
- [ ] **No EU law bleed**: Swiss law operates separately from EU law. Do not describe
      Swiss rules using EU legal concepts unless explicitly comparing the two systems

---

## External Tool Integration

**With legalcode-mcp connected (preferred)**:

- Search for the specific cantonal statute (e.g., "Zurich Handelsregisterverordnung",
  "Genf Handänderungssteuergesetz")
- Search for current tax rates from cantonal tax administrations
- Search for recent Federal Supreme Court decisions on intercantonal questions
- Save results to `/tmp/legalcode-ch-cantonal-research.md`
- Mark all legalcode-mcp sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp**:

- Mark all cantonal law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Direct user to official sources:
  - **fedlex.admin.ch**: Federal statutes (SR numbers)
  - **zefix.ch**: Commercial register central index
  - **estv.admin.ch**: Federal tax administration and inter-cantonal tax data
  - **admin.ch**: Federal government portal
  - **Cantonal official gazettes** (Amtsblatt / Feuille officielle / Foglio ufficiale)
    for cantonal law amendments
  - **Cantonal tax authority websites**: tax.zh.ch, steuern.be.ch, estv.ge.ch, etc.

---

## Output Format Template

```markdown
# Swiss Cantonal Law Navigator — Analysis Report

**Date**: [date]
**Query**: [user's question summarized]
**Canton(s) analyzed**: [list]
**Domain(s) covered**: [list]

---

## Federal vs. Cantonal Authority Classification

| Domain   | Classification                           | Federal Source       | Cantonal Variation              |
| -------- | ---------------------------------------- | -------------------- | ------------------------------- |
| [Domain] | [FEDERAL / MIXED / CANTONAL / MUNICIPAL] | [SR citation or N/A] | [Summary of cantonal variation] |

---

## Cantonal Analysis

### [Domain Name] — [Canton Name]

**Classification**: [FEDERAL / MIXED / CANTONAL / MUNICIPAL]
**Severity of variation**: [CRITICAL / MATERIAL / ADVISORY]
**Confidence**: [Definite / High / Probable / Possible / Unlikely] ([range])

**Rule**: [Specific cantonal rule, with citation if available]

**Citation**: [Cantonal statute / SR number / cantonal tariff — or "[VERIFY with cantonal authority]"]

**Practical implication**: [2-3 sentence plain-language summary]

**Action required**: [What the client/counsel must do]

---

## Cantonal Comparison Table (if multi-canton query)

| Feature     | [Canton A]  | [Canton B]  | [Canton C]  |
| ----------- | ----------- | ----------- | ----------- |
| [Feature 1] | [Rule]      | [Rule]      | [Rule]      |
| [Feature 2] | [Rate/rule] | [Rate/rule] | [Rate/rule] |

---

## CRITICAL Issues Summary

| #   | Issue   | Canton   | Classification | Recommended Action |
| --- | ------- | -------- | -------------- | ------------------ |
| 1   | [Issue] | [Canton] | CRITICAL       | [Action]           |

---

## Key Reference Sources

- **Federal law**: fedlex.admin.ch (search by SR number)
- **Commercial registers**: zefix.ch (central index) + [cantonal office URL]
- **Tax rates**: estv.admin.ch + [cantonal tax authority URL]
- **Lex Koller**: bj.admin.ch
- **[Other specific sources for the queried domain]**

---

[Glass Box Audit Trail — YAML block]
```

---

## Localization Notes

This skill is jurisdiction-specific to Switzerland. The following localizations apply:

**Within Switzerland**:

- Always use the official-language name for each institution (see Domain B for registry
  names; Domain D for labor court names)
- Bern (BE), Fribourg (FR), Valais (VS), and Graubünden (GR) are multilingual cantons —
  identify the relevant district's language before naming institutions
- Legal documents must be in the official language of the canton where they are filed or executed

**Cross-border matters**:

- EU persons and entities are subject to Swiss law when transacting in Switzerland —
  EU law does not apply domestically
- The bilateral agreements between Switzerland and the EU (particularly the Freedom of
  Movement Agreement) affect certain employment, residency, and market access questions —
  flag for separate analysis
- Tax treaties: Switzerland has an extensive DTA network (over 100 treaties); cross-border
  tax questions should be analyzed under the relevant DTA in addition to cantonal law
- FATCA, CRS, and automatic exchange of information are federal matters (not cantonal)

---

## Provenance

Created by Legalcode (2026-03-21). Mode A (created from scratch). 2-agent research pipeline
covering: Swiss federal/cantonal authority mapping (Art. 3 and 49 BV; OR, ZGB, ZPO, DBG,
StHG, ANRA, BGBB, RPG, HRegV); commercial register cantonal variation (28 cantonal offices,
ZEFIX portal, OR Art. 927-943, HRegV SR 221.411); corporate and capital tax by canton
(StHG SR 642.14, DBG SR 642.11, ESTV data); labor court organization (ZPO Art. 3, 197ff;
OR Art. 319-362; cantonal court structures for ZH, GE, VD, BE, BS, LU, ZG, SG, AG, TI);
courts of first instance and commercial courts (ZPO Art. 6; BGG Art. 74-75; cantonal
court hierarchies); land registry and transfer taxes (ZGB Art. 657, 942-977; ANRA Lex
Koller SR 211.412.41; BGBB SR 211.412.11; cantonal transfer tax schedules); notarial
systems (Staatliches vs. Freies Notariat; ZGB Art. 184, 657; OR Art. 629, 777); cantonal
inheritance tax regimes (no federal inheritance tax; 26 cantonal regimes; ZGB Art. 457-640);
building permits (RPG SR 700; cantonal PBG; municipal BZO); professional licensing (BGFA
SR 935.61). Research covered 26 cantons with detailed analysis of 10 major cantons (ZH,
ZG, GE, VD, BE, BS, LU, SZ, SG, TI). 20 anti-patterns catalogued. Sources: fedlex.admin.ch,
admin.ch, estv.admin.ch, zefix.ch, bj.admin.ch, nyulawglobal.org/globalex/switzerland,
charlesrussellspeechlys.com, lindemannlaw.ch, taxsummaries.pwc.com, concordanz.com,
ch.ch/inheritance-tax, sav-fsa.ch.
