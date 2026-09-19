---
name: legalcode-pl-legal-memorandum
description: Draft and review Polish law legal memoranda (opinia prawna) covering statutory interpretation
  (wykładnia prawa), Civil Code (Kodeks cywilny, KC) analysis, commercial company law (Kodeks spółek handlowych,
  KSH), administrative law (Kodeks postępowania administracyjnego, KPA), court structure, and precedent
  treatment. Use when answering a specific legal question (pytanie prawne) under Polish law, preparing
  formal legal opinions for corporate clients or regulatory submissions, assessing transaction permissibility,
  corporate authority, administrative compliance, or contractual validity under Polish law, or reviewing
  an existing opinia prawna for completeness and analytical quality.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Draft and review Polish law legal memoranda (opinia prawna) covering statutory interpretation (wykładnia prawa), Civil Code (Kodeks cywilny, KC) analysis, commercial company law (Kodeks spółek handlowych, KSH), administrative law (Kodeks postępowania administracyjnego, KPA), court structure, and precedent treatment. Applies the canonical Polish opinia prawna structure (Przedmiot / Podstawa prawna / Podstawa faktyczna / Analiza prawna / Wnioski / Zastrzeżenia). Consolidates IURA-methodology subsumption analysis with Legalcode quality frameworks. Use when answering a specific legal question (pytanie prawne) under Polish law, preparing formal legal opinions for corporate clients or regulatory submissions, assessing transaction permissibility, corporate authority, administrative compliance, or contractual validity under Polish law, or reviewing an existing opinia prawna for completeness and analytical quality. Governed exclusively by Polish law (prawo polskie); for jurisdiction-agnostic memo work use legalcode-contract-review.


# Legalcode Polish Legal Memorandum

# Opinia Prawna — Legalcode (Prawo Polskie)

> **Disclaimer / Zastrzeżenie prawne**: This skill provides a framework for AI-assisted
> drafting and review of Polish legal memoranda (opinie prawne). It does not constitute
> legal advice (porada prawna) and is not a substitute for qualified professional counsel.
> All outputs must be reviewed by a qualified **radca prawny** or **adwokat** licensed in
> Poland before reliance or submission. Polish law changes frequently; verify the current
> state of every statute and court decision against authoritative sources (ISAP, LEX,
> Legalis, sn.pl, nsa.gov.pl) before use. Statutory and case law references generated from
> AI memory carry **hallucination risk** — treat every citation as unverified unless
> confirmed against an authoritative database.

---

## Purpose and Scope

This skill drafts and reviews formal Polish legal memoranda (**opinia prawna**) and their
lighter-weight variant (**memorandum prawne**) in response to specific legal questions
(**pytania prawne**) under Polish law.

**Covers:**

- Drafting a complete opinia prawna conforming to canonical Polish structure
- Reviewing an existing opinia prawna for analytical quality, completeness, and accuracy
- Statutory interpretation using the recognised Polish methods (językowa → systemowa →
  celowościowa / teleologiczna)
- Civil Code (KC) analysis — obligations, contracts, representation, limitation, invalidity
- Commercial company law (KSH) analysis — corporate authority, consents, governance
- Administrative law (KPA) analysis — administrative decisions, procedural compliance,
  regulatory approvals
- Polish court structure and treatment of precedent
- Applying the PERMISSIBLE / UNCERTAIN / IMPERMISSIBLE conclusion classification with
  5-level confidence scoring
- Glass Box audit trail for every opinion

**Does not:**

- Provide legal advice (porada prawna) or replace qualified legal counsel
- Draft court pleadings (pisma procesowe) — see litigation-specific skills
- Provide tax analysis unless explicitly noted — tax opinions require a doradca podatkowy
- Cover NDAs or contract review — see `legalcode-nda-triage-pl` or `legalcode-contract-review`
- Apply to non-Polish governing law — for other jurisdictions use the appropriate
  jurisdiction-specific skill

---

## Jurisdiction and Governing Law

This skill is localized exclusively for **Polish law (prawo polskie)**.

### Legal System Classification

Poland is a **civil law** (prawo kontynentualne) jurisdiction. Key consequences for the opinia:

- Statutes (ustawy) and codes (kodeksy) are the primary source of law — they must be cited
  in the **Podstawa prawna** of every opinion
- Court decisions are **not formally binding precedent** (stare decisis does not apply),
  but consistent Supreme Court (Sąd Najwyższy, SN) jurisprudence carries very strong
  persuasive authority
- Legal doctrine (doktryna prawnicza) — academic commentaries and monographs — is
  routinely cited and carries persuasive weight where case law is absent or divided
- EU law takes primacy over Polish statute (subject to the TK/EU law tension noted below)

### Polish Legislative Citation Format

| Document Type | Citation Format (first reference)                                                       | Short form                |
| ------------- | --------------------------------------------------------------------------------------- | ------------------------- |
| Statute       | ustawa z dnia [date] r. [full name], t.j. Dz.U. [year] poz. [number]                    | [name abbreviation]       |
| Code (kodeks) | Kodeks [name] z dnia [date] r., t.j. Dz.U. [year] poz. [number]                         | KC / KSH / KPA / KPC / KP |
| Regulation    | rozporządzenie [authority] z dnia [date] r. w sprawie [...], Dz.U. [year] poz. [number] | rozp.                     |
| EU Regulation | Rozporządzenie PE i Rady (UE) [number/year] z dnia [...]                                | [name]                    |
| SN decision   | wyrok/uchwała SN z dnia [date] r., sygn. [chamber] [number/year]                        | SN [date], sygn.          |
| TK decision   | wyrok/postanowienie TK z dnia [date] r., sygn. K/P/SK/U [number/year]                   | TK [date], sygn.          |
| NSA decision  | wyrok NSA z dnia [date] r., sygn. [chamber] [number/year]                               | NSA [date], sygn.         |
| Doctrine      | [Author], [Title], [ed.], [publisher] [year], s. [page] or art. [X], nb. [number]       | [Author] (year)           |

All statutory citations should include the consolidated text reference (tekst jednolity, t.j.)
where available. Verify via ISAP (isap.sejm.gov.pl).

---

## Interactive Clarification

This skill uses **interactive clarification** (⟁ CLARIFY) at key decision points. The
workflow pauses and asks when:

- The scope or audience of the opinion changes the analytical approach
- Multiple valid legal conclusions exist and the user's risk tolerance matters
- Factual assumptions are incomplete or ambiguous, and the analysis could materially differ
- The format (traditional or executive-summary-first) is not specified

When the user provides partial context, proceed with **stated assumptions** — never
silently assume. For example: "Zakładam, że pytanie dotyczy sp. z o.o. z prawem polskim
jako prawem właściwym — proszę o potwierdzenie, jeśli to nieprawidłowe."

---

## Workflow

### Step 1: Accept the Request (Przyjęcie zlecenia)

Accept input in any of these forms:

- **Legal question (pytanie prawne)**: A specific question requiring a legal answer
- **Transaction / situation description**: Facts of a business scenario requiring a legal
  assessment of permissibility, validity, or risk
- **Existing opinia**: A draft or existing opinion to be reviewed for quality and accuracy
- **Mandate document**: A formal statement of the client's questions (zlecenie)

If input is ambiguous, proceed to Step 2 before attempting analysis.

### Step 2: Gather Context (Zebranie kontekstu)

**⟁ CLARIFY** — Before beginning, ask the following. Skip any already provided:

1. **Requesting party and role**:
   - Options: External client (klient zewnętrzny), Internal legal department (dział prawny
     wewnętrzny), Regulatory submission (organ administracji), Board / supervisory board
     (zarząd / rada nadzorcza), Other
   - _Why this matters_: Formal external opinions require the full canonical structure and
     signature block; internal memoranda may use an abbreviated format.

2. **Opinion type**:
   - Options: Full opinia prawna (formal, externally releasable), Memorandum prawne
     (internal, rapid), Review of existing opinion (ocena istniejącej opinii)
   - _Why this matters_: Determines which sections are mandatory and the level of formality.

3. **Urgency / deadline**:
   - Options: Urgent — same day/next day (pilne), Standard — within 3–5 days, Flexible
   - _Why this matters_: Affects depth of analysis — urgent matters may require a memorandum
     prawne flagging open points for follow-up.

4. **Audience**:
   - Options: Board of directors / management (zarząd), Shareholders / supervisory board,
     Regulatory authority (organ administracyjny), Counter-party / external business partner,
     Court submission, Internal use only
   - _Why this matters_: External-reliance opinions require the zastrzeżenia clause and
     formal bar-roll signature block; submissions to regulators may require specific formatting.

5. **Legal area(s) involved**:
   - Options (multi-select): Contract law / civil obligations (KC), Corporate law (KSH),
     Administrative / regulatory law (KPA), Employment law (KP), Competition law (UOKiK),
     Data protection (RODO), IP law, Other (specify)
   - _Why this matters_: Determines which code-specific analysis layers to activate.

6. **Factual documentation available**:
   - Free text: list documents provided (contracts, board resolutions, correspondence,
     register excerpts, etc.)
   - _Why this matters_: The opinion's **Podstawa faktyczna** can only address facts
     supported by documentation; undocumented facts must be flagged as assumptions.

If partial context is given, state assumptions explicitly in the **Przedmiot opinii** section.

### Step 3: Decompose the Legal Questions (Analiza pytań prawnych)

This step is unique to opinion-drafting work and critical to quality.

Before beginning analysis, identify and list every discrete legal question (zagadnienie
prawne) contained in the mandate. Complex mandates often contain nested sub-questions.

**⟁ CLARIFY** — If the mandate is ambiguous, confirm the question decomposition with the
client before proceeding:

- Present a numbered list of the questions as you understand them
- Flag any scope gaps: "The mandate does not appear to ask about [X]. Should that be
  included or is it deliberately excluded?"
- Flag scope overlaps: "Questions 2 and 3 both touch on Art. 17 KSH authority. I will
  address them jointly unless you prefer separate analysis."

The number of questions identified here determines the structure of **Analiza prawna** and
**Wnioski** — every question receives an analysed sub-section and a direct wniosek.

> **The single most common failure in Polish legal memoranda is answering a different
> question than was asked.** The question decomposition step prevents this. Do not skip it.

### Step 4: Gather Legal Authority (Zebranie podstaw prawnych)

Identify all applicable statutes, regulations, and major case law for each question.

**Use legalcode-mcp** to search for:

- Applicable KC, KSH, KPA, or other code provisions (with current consolidated text
  references from ISAP)
- SN and TK decisions on the relevant legal issues
- NSA/WSA rulings for administrative law questions
- EU law provisions and CJEU/TSUE decisions where EU law is relevant
- Recent legislative amendments affecting the applicable provisions

Save results to `/tmp/pl-legal-memo-authority.md`. Structure as:

```markdown
# Podstawy prawne — [Przedmiot opinii]

## Data zebrania: [date]

## Stan prawny na dzień: [date]

### Akty prawne (Statutes and Codes)

- [ustawa / kodeks — Art. X — treść lub streszczenie — VERIFIED / UNVERIFIED]

### Orzecznictwo (Case Law)

- [wyrok/uchwała SN/TK/NSA — sygn. — teza — VERIFIED / UNVERIFIED]

### Doktryna (Doctrine)

- [Author, Title, ed., year, art. X, nb. N]

### Prawo UE (EU Law — if applicable)

- [Regulation/Directive — article — relevance]
```

**If legalcode-mcp is not connected:**

- Proceed using the legal framework sections of this skill
- Mark every statutory and case law citation [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — manual verification required"`

**⟁ CLARIFY** — If any of the following arise, resolve before analysis:

- **Governing law conflict**: The documents reference multiple legal systems (e.g., English
  law for a contract but Polish law for corporate authority) — confirm which law governs
  each question
- **Recent legislative change**: A provision you identify may have been recently amended
  (e.g., the 2022 KSH reform, 2018 KC limitation period reform) — flag and confirm
  whether the new or old version applies based on intertemporality rules (przepisy
  intertemporalne)
- **TK/EU law tension**: The question involves an area where TK has issued rulings that
  conflict with CJEU jurisprudence — confirm whether the opinion should note this tension
  or resolve it in favour of EU law primacy (standard position for commercial opinions)

### Step 5: Statutory Interpretation Analysis (Wykładnia przepisów)

For each legal question, apply the statutory interpretation methodology in sequence:

**Stage 1 — Wykładnia językowa (Linguistic Interpretation)**
Establish the literal meaning of the applicable provision. Use the provision's own
defined terms (definicje legalne) first; then ordinary language; then specialist terminology.

If the linguistic result is unambiguous and produces a reasonable outcome consistent with
the overall statutory framework, it controls. If it produces an absurd or unjust result,
proceed to Stage 2.

**Stage 2 — Wykładnia systemowa (Systematic Interpretation)**
Examine the provision in its legislative context:

- Its position in the code structure (chapter, title, division)
- Relationship to adjacent and general provisions in the same code
- Relationship to other codes or statutes (lex specialis / lex generalis analysis — see
  KC vs. KSH hierarchy below)
- Conformity with constitutional principles (Art. 2 RP — państwo prawne; Art. 22 RP —
  freedom of economic activity; Art. 64 RP — property protection)
- Conformity with EU law (prounijna wykładnia) if EU law is applicable

**Stage 3 — Wykładnia celowościowa / teleologiczna (Purposive Interpretation)**
Determine the provision's purpose (ratio legis):

- Examine the legislative history (uzasadnienie projektu ustawy) where available
- Identify the social, economic, or regulatory purpose the provision serves
- Test whether the linguistic result serves or undermines that purpose

> For each question, document which stages were applied and why, and state any
> divergence between linguistic and purposive results. Where the methods diverge, explain
> which prevails and why.

**KC vs. KSH Lex Specialis Analysis (for commercial questions)**

| Situation                         | Governing Regime                          | Basis                                     |
| --------------------------------- | ----------------------------------------- | ----------------------------------------- |
| General civil obligations (umowy) | KC exclusively                            | General civil law                         |
| Acts of a commercial company      | KSH as lex specialis, KC as lex generalis | Art. 2 KSH                                |
| KSH silent on an issue            | KC fills the gap                          | Art. 2 KSH (subsidiary application of KC) |
| KSH conflicts with KC             | KSH prevails                              | Lex specialis derogat legi generali       |
| Consumer protection               | Ustawa o prawach konsumenta + KC          | Special regime                            |

Explicitly identify which regime governs each question before beginning analysis.

### Step 6: Case Law and Precedent Analysis (Analiza orzecznictwa)

Assess the weight of the precedent identified in Step 4 using the Polish Precedent
Spectrum:

| Source                                             | Formal Status                                 | Practical Authority                                           |
| -------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------- |
| **Wyrok TK** — unconstitutionality ruling          | Erga omnes binding (Art. 190 Konst.)          | Highest — provision loses force                               |
| **Wyrok TK interpretacyjny** — interpretive ruling | Constitutionally binding interpretation       | Very high — specified reading is mandatory                    |
| **Uchwała SN — zasada prawna** (7+ judges)         | Binding on all SN panels                      | Very high — effectively settles the question for SN           |
| **Uchwała SN** (3 judges)                          | Not formally binding                          | High — courts routinely follow                                |
| **Orzeczenie SN** (ordinary judgment)              | Not binding stare decisis                     | High persuasive — consistent SN line = utrwalone orzecznictwo |
| **Orzeczenie SA / SO**                             | Not binding                                   | Moderate — same-circuit courts show deference                 |
| **Uchwała NSA**                                    | Binding in administrative proceedings         | High for administrative law questions                         |
| **Wyrok TSUE/CJEU** (preliminary ruling)           | Binding on referring court; highly persuasive | High — Polish courts apply EU law primacy                     |
| **Komentarze prawnicze / doktryna**                | Not binding                                   | Material — courts actively cite leading commentaries          |

**Formulation rules for citing precedent:**

| Weight level             | Correct formulation                                                                                                                     |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| Binding (TK erga omnes)  | "Zgodnie z wyrokiem TK z dnia [...], przepis art. X [ustawy] jest niezgodny z Konstytucją RP i utracił moc obowiązującą."               |
| SN uchwała zasada prawna | "Sąd Najwyższy w uchwale składu siedmiu sędziów z dnia [...] (sygn. [...]) przyjął jako zasadę prawną, że..."                           |
| Consistent SN line       | "W utrwalonym orzecznictwie Sądu Najwyższego przyjmuje się, że... (zob. wyroki SN: [...], [...])."                                      |
| Isolated SN judgment     | "W wyroku z dnia [...] Sąd Najwyższy wyraził pogląd, że... Pogląd ten nie uzyskał jednak dotychczas charakteru utrwalonego stanowiska." |
| Doctrinal consensus      | "Dominujący pogląd doktryny, wyrażony przez [Author] ([citation]) oraz [Author] ([citation]), wskazuje, że..."                          |
| Divided doctrine         | "Zagadnienie to jest sporne w doktrynie. Zdaniem [Author] ([citation])... Odmiennie: [Author] ([citation])..."                          |

> **Critical rule**: Never state that an SN ordinary judgment is "binding" (wiążący).
> The correct term is "persuasive" (przekonujący) or "authoritative" (autorytatywny).
> Reserve "wiążący" for TK erga omnes rulings and zasady prawne.

**TK / EU Law Tension (2025 context)**

Where the question involves EU law, note:

- If TK has issued rulings that the SN or CJEU has found inconsistent with EU law primacy,
  the opinion should explicitly state that ordinary Polish courts (including SN) apply EU
  law primacy under Art. 91 Konstytucji RP and CJEU C-448/23 (December 2025)
- The TK's post-2015 independence concerns are publicly known — for opinions destined for
  EU-law-intersecting proceedings, it is safer to rely on SN and CJEU rulings than on TK
  rulings in disputed constitutional matters

### Step 7: Draft the Memorandum (Sporządzenie opinii)

Draft the opinia prawna in the canonical eight-section Polish structure. Apply the format
defined in the **Output Format Template** section below.

Key drafting rules:

**Wnioski placement**: For commercial/transactional opinions, place the **Wnioski** section
immediately after the **Podstawa faktyczna** and before the **Analiza prawna**. This
"executive summary first" model follows current big-law practice and ensures the reader
can access the conclusions without reading the full analysis. Mark clearly: "Pełna analiza
prawna uzasadniająca powyższe wnioski zawarta jest w Sekcji V." Include both models for
formal judicial/regulatory submissions: in those contexts, the traditional order
(analysis before conclusions) may be required.

**Per-question IRAC/subsumption loop**: In the **Analiza prawna**, address each question
in a numbered sub-section (§1, §2, etc.) following the subsumption structure:

```
§[N]. [Short title of the question]

[a] Teza prawna (applicable norm):
    Pursuant to Art. X §Y KC/KSH/KPA: "[literal text of provision]"

[b] Stan faktyczny relevanty dla tej normy (relevant facts):
    [Application of norm to client's specific facts]

[c] Subsumcja (application):
    [Reasoning — how the facts satisfy or fail the norm's conditions;
     interpretation methodology applied; precedent cited]

[d] Wniosek cząstkowy (intermediate conclusion):
    [PERMISSIBLE / PERMISSIBLE WITH CONDITIONS / UNCERTAIN / IMPERMISSIBLE /
     REQUIRES REGULATORY CLEARANCE] — Confidence: [level]
    [Direct, unambiguous answer to sub-question N]
```

**Form requirements check**: For every transaction or legal act analysed, complete the
form requirements analysis layer:

| Form Requirement                                                      | Applicable? | Provision       | Consequence of Failure               |
| --------------------------------------------------------------------- | ----------- | --------------- | ------------------------------------ |
| Forma pisemna zwykła (ordinary written form)                          | Yes/No      | Art. [X] KC/KSH | Ograniczenia dowodowe or nieważność  |
| Forma pisemna pod rygorem nieważności (written — invalidity sanction) | Yes/No      | Art. [X]        | Nieważność bezwzględna               |
| Forma aktu notarialnego (notarial deed)                               | Yes/No      | Art. [X]        | Nieważność bezwzględna               |
| Forma z podpisem notarialnie poświadczonym                            | Yes/No      | Art. [X]        | Nieważność bezwzględna               |
| Rejestracja / wpis do KRS (KRS registration)                          | Yes/No      | Art. [X] KSH    | Constitutive / declaratory (specify) |
| Zgoda / uchwała korporacyjna (corporate consent)                      | Yes/No      | Art. [X] KSH    | Per Art. 17 KSH analysis             |

**KC Invalidity taxonomy**: Whenever invalidity (nieważność) is identified, specify the type:

| Type                                  | Polish Term                        | Legal Basis                              | Effect                                                         | Cure                               |
| ------------------------------------- | ---------------------------------- | ---------------------------------------- | -------------------------------------------------------------- | ---------------------------------- |
| Absolute invalidity                   | Nieważność bezwzględna             | Art. 58 KC                               | Void ab initio, ex lege                                        | Cannot be cured                    |
| Relative invalidity / voidability     | Nieważność względna / wzruszalność | Art. 84–88 KC; Art. 388 KC               | Valid until avoided by protected party                         | Can be ratified / not invoked      |
| Ineffectiveness against third parties | Bezskuteczność                     | Art. 59 KC; Art. 527 KC (actio pauliana) | Valid inter partes; ineffective against certain third parties  | No cure needed between parties     |
| Suspended effectiveness               | Bezskuteczność zawieszona          | Art. 17 §2 KSH; Art. 63 KC               | Act valid but effectiveness suspended pending required consent | Ratification within 2 months (KSH) |
| Relative ineffectiveness              | Bezskuteczność względna            | Various                                  | Ineffective only against the protected party                   | No cure needed                     |

Do not collapse these into binary "void/voidable." The distinction determines available
remedies, enforcement options, and third-party rights.

### Step 8: Quality Verification (Weryfikacja jakości)

Before delivering the opinion, run the Quality Assurance Framework silently:

1. Run the **5 Citation Quality Gates** — revise any failures before delivery
2. For every IMPERMISSIBLE or UNCERTAIN conclusion, run the **3-Pass Self-Interrogation**
3. Apply the **5 Writing Standards Quality Gates**
4. Verify the **Zastrzeżenia section** contains all mandatory clauses
5. Confirm every question from Step 3 is answered in the **Wnioski section**

If the opinion scores below 35/40 on the prompt-engineering scorecard (internal check),
identify and revise the weak dimensions before delivery.

### Step 9: Deliver the Opinion with Glass Box Audit Trail

Deliver the complete opinia prawna per the Output Format Template.

Append the Glass Box Audit Trail YAML at the end of the opinion. The Glass Box is for
internal AI process transparency — it may be removed from the client-facing deliverable
at the user's discretion, but it must be produced.

---

## Legal Framework Reference

### Primary Codes and Their Abbreviations

| Code / Statute                   | Polish Name                           | Abbreviation | Current Consolidated Text                          |
| -------------------------------- | ------------------------------------- | ------------ | -------------------------------------------------- |
| Civil Code                       | Kodeks cywilny                        | KC           | t.j. Dz.U. 2024 poz. 1061 [VERIFY]                 |
| Commercial Companies Code        | Kodeks spółek handlowych              | KSH          | t.j. Dz.U. 2024 poz. 18 (as amended 2022) [VERIFY] |
| Code of Administrative Procedure | Kodeks postępowania administracyjnego | KPA          | t.j. Dz.U. 2024 poz. 572 [VERIFY]                  |
| Code of Civil Procedure          | Kodeks postępowania cywilnego         | KPC          | t.j. Dz.U. 2024 poz. 1568 [VERIFY]                 |
| Labour Code                      | Kodeks pracy                          | KP           | t.j. Dz.U. 2023 poz. 1465 [VERIFY]                 |
| Criminal Code                    | Kodeks karny                          | KK           | t.j. Dz.U. 2024 poz. 17 [VERIFY]                   |
| Constitution of Poland           | Konstytucja RP                        | Konst. RP    | Dz.U. 1997 nr 78 poz. 483 (as amended) [VERIFY]    |

Always verify consolidated text references against ISAP before use. [VERIFY] markers
indicate references that require authoritative confirmation.

### KC Core Provisions for Commercial Opinions

| Article                       | Subject                             | Key Content                                                                                                                                                                                                                                                                          |
| ----------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Art. 5 KC                     | Abuse of rights                     | Rights exercised contrary to socio-economic purpose or zasady współżycia społecznego receive no legal protection. Defence, not positive claim.                                                                                                                                       |
| Art. 56 KC                    | Effects of legal acts               | Legal acts produce effects expressed therein and those resulting from statute, principles of social coexistence, and established custom.                                                                                                                                             |
| Art. 58 KC                    | Invalidity                          | Act contrary to statute or intended to circumvent statute is void (nieważny) unless special provision says otherwise; act contrary to zasady współżycia społecznego is void.                                                                                                         |
| Art. 60 KC                    | Declaration of will                 | Will may be expressed by any conduct sufficiently revealing it, including electronic form.                                                                                                                                                                                           |
| Art. 65 KC                    | Contract interpretation             | §1: Declarations interpreted considering circumstances of making, zasady współżycia społecznego, and established custom. §2: In contracts, parties' common intent and contract purpose govern over literal wording.                                                                  |
| Art. 66–81 KC                 | Contract formation                  | Offer (oferta), acceptance, counter-offer (Art. 68¹ — modified acceptance between merchants), silence (Art. 70), pre-contractual duties (Art. 72, 72¹).                                                                                                                              |
| Art. 73–77 KC                 | Form requirements                   | Art. 73 §1: Form required by statute — absence = invalidity (nieważność) or evidentiary restriction (ograniczenia dowodowe). Art. 73 §2: Notarial form — absence always = nieważność.                                                                                                |
| Art. 95–109 KC                | Representation and agency           | Three types of pełnomocnictwo (ogólne/rodzajowe/szczególne). Art. 99 §2: General power of attorney must be in writing. Art. 104: Unilateral act beyond authority — invalid. Art. 108: No self-contracting without permission.                                                        |
| Art. 118 KC (as amended 2018) | Limitation periods                  | General: 6 years (reduced from 10 in 2018). Business/periodic: 3 years. End-of-year calculation rule for periods of 2+ years.                                                                                                                                                        |
| Art. 353¹ KC                  | Freedom of contract                 | Parties may structure their relationship as they see fit unless content/purpose contradicts: (1) nature of the relationship, (2) statute, (3) zasady współżycia społecznego.                                                                                                         |
| Art. 354 KC                   | Good faith performance              | Debtor shall perform obligation consistent with its content; in the manner required by its socio-economic purpose and zasady współżycia społecznego.                                                                                                                                 |
| Art. 358¹–358² KC             | Currency and hardship               | §1: Monetary obligations expressed in PLN unless otherwise agreed. §2: clausula rebus sic stantibus — court may modify or terminate contract if extraordinary change in circumstances.                                                                                               |
| Art. 405–414 KC               | Unjust enrichment                   | Bezpodstawne wzbogacenie: obligation to return enrichment in kind or in value. Art. 410: Condictio (return of undue payment). Art. 411: Exceptions (moral duty, equally culpable unlawful act).                                                                                      |
| Art. 415 KC                   | Tort liability                      | Whoever by fault causes damage is obligated to repair it. Claimant bears burden of proof (fault, damage, causal link).                                                                                                                                                               |
| Art. 471 KC                   | Contractual liability               | Debtor liable for damage from non-performance/improper performance. Reversed burden — debtor must prove absence of fault.                                                                                                                                                            |
| Art. 483–485 KC               | Contractual penalties (kara umowna) | Art. 483: Parties may specify a fixed sum payable for non-performance. Art. 484 §2: Court may reduce (miarkować) the penalty if obligation substantially performed or penalty is grossly excessive. Art. 485: Parties may preserve right to supplementary damages above the penalty. |
| Art. 527–534 KC               | Actio pauliana                      | Bezskuteczność: creditor may challenge legal acts by debtor that harm creditors. Conditions: act causing insolvency, debtor's knowledge, third-party awareness or benefit without remuneration.                                                                                      |

### KSH Core Provisions for Corporate Opinions

| Article             | Subject                              | Key Content                                                                                                                                                                                                                                                                                                                                                        |
| ------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Art. 2 KSH          | Subsidiary application of KC         | KC applies to commercial companies insofar as KSH does not provide otherwise. KSH is lex specialis.                                                                                                                                                                                                                                                                |
| Art. 17 KSH         | Corporate consent requirements       | §1: Legal act requiring a shareholders' or supervisory board resolution, performed without it, is **invalid (nieważna)**. §2: Required resolution may be granted retroactively within **2 months** (bezskuteczność zawieszona converts to valid act retroactively).                                                                                                |
| Art. 18 KSH         | Eligibility for board positions      | §2 (as amended 2018 + 2022): Conviction of specified economic, document, or corruption crimes prohibits holding board/supervisory/liquidator positions for prescribed periods.                                                                                                                                                                                     |
| Art. 201–211 KSH    | Sp. z o.o. management board          | Art. 201 §1: Board conducts affairs and represents company. Art. 204 §2: Internal restrictions on authority have **no effect against third parties**. Art. 205 §1: Multi-member board default — two members jointly, or one member + prokurent. Art. 210: Company vs. board member transactions require supervisory board or shareholders' meeting representation. |
| Art. 228–230 KSH    | Sp. z o.o. shareholder resolutions   | Art. 228: Mandatory shareholder resolutions for specified acts (real property, own shares, extraordinary distribution, subsidiary establishment). Art. 229: Acquisition of assets from shareholders within 2 years of incorporation — shareholder approval. Art. 230: Acts exceeding twice the share capital require shareholder approval if articles specify.     |
| Art. 368–379 KSH    | SA management board                  | Art. 368 §1: Board conducts affairs and represents. Art. 373 §1: Default joint representation (two members or member + prokurent). Art. 374: Internal restrictions — no effect against third parties. Art. 379: Conflict of interest — supervisory board or PEŁNOMOCNIK authorized by shareholders' meeting represents company against board member.               |
| Art. 393 KSH        | SA supervisory board resolutions     | Mandatory resolutions for: enterprise disposal/lease, acquisition of real property > PLN 100K (or lesser amount in articles), related-party transactions (post-2022: threshold at 10% of total assets).                                                                                                                                                            |
| Art. 3001–30098 KSH | PSA (Simple Joint Stock Company)     | Introduced 2021. Minimum capital: 1 PLN. Contribution of work/services permitted. Unitary governance model (rada dyrektorów) or dual model.                                                                                                                                                                                                                        |
| Art. 2111–2116 KSH  | Group company law (prawo holdingowe) | Added 2022. Holding company may issue binding instructions to subsidiaries within limits. Subsidiary board compliance with binding instruction not treated as breach of duty. Minority shareholder and creditor protections.                                                                                                                                       |

**2022 KSH Reform highlights** (effective 13 October 2022, Dz.U. 2022 poz. 807):

- Expanded supervisory board information rights and advisor-appointment powers
- Business Judgment Rule codified (ochrona biznesowej oceny sytuacji)
- Mandatory board minutes for sp. z o.o.
- Related-party transaction approval — SA: supervisory board approval for transactions
  with related parties exceeding 10% of total assets
- Criminal penalties for withholding information from supervisory board (PLN 20,000–50,000)
- Loyalty duty codified for board members

### KPA Core Provisions for Administrative Law Opinions

| Principle/Article | Polish Name                                  | Content                                                                                                                                                                                                           |
| ----------------- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Art. 6 KPA        | Praworządność (rule of law)                  | Authorities act only on legal basis; subjects must be informed of their rights                                                                                                                                    |
| Art. 7 KPA        | Prawda obiektywna                            | Authority must establish the truth and balance public and individual interests                                                                                                                                    |
| Art. 7a KPA       | In dubio pro citizen                         | Where legal doubt remains after all interpretation methods, authorities must resolve it in favour of the party                                                                                                    |
| Art. 8 KPA        | Trust, impartiality, proportionality         | Authorities must build citizen trust; act impartially; apply proportionate measures                                                                                                                               |
| Art. 104–105 KPA  | Decision and order                           | Final disposition in administrative case: decyzja (decision on merits) or postanowienie (procedural order)                                                                                                        |
| Art. 107 KPA      | Mandatory elements of decyzja                | Authority designation, date, parties, operative part (rozstrzygnięcie), legal basis, statement of reasons (uzasadnienie), appeal instruction (pouczenie), signature                                               |
| Art. 156 KPA      | Void (nieważna) administrative decision      | Grounds: issued without jurisdiction, in rażące naruszenie prawa (gross violation of law), re settled matter, to wrong party, inherently unenforceable, would constitute criminal offence, or incurably defective |
| Art. 127–144 KPA  | Odwołanie (appeal)                           | Appeal to superior authority within 14 days of receipt of decision; odwołanie does not require reasoning (bezformalne); authority may affirm, modify, or annul                                                    |
| Art. 35 KPA       | Processing deadlines                         | Simple matters: 1 month; complex matters: 2 months; appeal decisions: 1 month                                                                                                                                     |
| Art. 40 KPA       | Milczące załatwienie sprawy (tacit approval) | Authority deemed to have granted request if it fails to notify refusal/conditions within deadline; requires specific statutory basis                                                                              |

---

## Conclusion Classification System

Polish legal memoranda use a **two-dimensional classification**. Apply both dimensions to
every conclusion:

### Dimension 1 — Legal Conclusion Classification

| Classification                    | Polish Term                          | Meaning                                                                                                                                                   | When to Use                                                                                                            |
| --------------------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **PERMISSIBLE**                   | Dopuszczalne                         | The action is clearly permitted under applicable Polish law; no conditions or reservations                                                                | Unambiguous statutory authorisation; consistent SN jurisprudence; no conflicting provisions                            |
| **PERMISSIBLE WITH CONDITIONS**   | Dopuszczalne z zastrzeżeniami        | Permitted, but specific legal requirements, formalities, consents, or procedural steps must be satisfied                                                  | Form requirements; corporate consent under Art. 17 KSH; regulatory approval; mandatory notice period                   |
| **UNCERTAIN**                     | Niepewne / Wymaga analizy ad casum   | The law is ambiguous, interpretation methods produce different results, or the question depends on unresolved facts                                       | Divided doctrine; absence of SN ruling; genuine statutory ambiguity; facts not yet established                         |
| **IMPERMISSIBLE**                 | Niedopuszczalne                      | The action is prohibited, would result in invalidity (nieważność) under Art. 58 KC, or exposes the client to material legal risk that cannot be mitigated | Express prohibition; ius cogens violation; mandatory form not satisfiable; would constitute nieważność bezwzględna     |
| **REQUIRES REGULATORY CLEARANCE** | Wymaga zgody regulatora / zgłoszenia | The action requires prior administrative decision, regulatory notification, or registration                                                               | Merger notification (UOKiK thresholds); KNF approvals; KRS registration with constitutive effect; construction permits |

### Dimension 2 — Analytical Confidence

| Level                             | Range     | Meaning                                                                     | Action in the Opinion                                                          |
| --------------------------------- | --------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Definite** (pewne)              | 0.95–1.0  | Settled law, clear statute, consistent SN zasada prawna                     | State conclusion without qualifier                                             |
| **High** (wysokie)                | 0.80–0.94 | Strong authority (consistent SN line or TK), minor academic controversy     | State conclusion with brief caveat noting the minority view                    |
| **Probable** (prawdopodobne)      | 0.60–0.79 | Good arguments, no settled SN position, or divided doctrine                 | State conclusion with full reasoning and identification of contrary arguments  |
| **Possible** (możliwe)            | 0.40–0.59 | Genuinely uncertain; competing interpretations; facts not fully established | Present both sides; characterise as UNCERTAIN; flag for professional review    |
| **Unlikely** (mało prawdopodobne) | 0.0–0.39  | Weak basis, speculative, contrary to dominant doctrine or SN line           | Do not assert as a conclusion; mark [NIEPEWNE]; recommend alternative approach |

**Combined classification example**:

> "W ocenie niniejszej opinii, planowana transakcja jest **DOPUSZCZALNA Z ZASTRZEŻENIAMI**
> (Confidence: Wysokie — 0.85), przy czym konieczne jest uprzednie podjęcie uchwały
> przez zgromadzenie wspólników w trybie art. 228 KSH."

---

## Quality Assurance Framework

### Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate                      | Rule                                                                                                                                                                                                                                    | Fail Action                                                                                |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Source (Źródło)**       | Every legal claim cites a specific article, statute, or recognised principle; doctrine cited to a specific author, work, and page/margin number                                                                                         | Add citation or mark [NIEZWERYFIKOWANE]                                                    |
| **Format (Format)**       | All citations follow Polish citation format (Art. X §Y [code]; t.j. Dz.U. [year] poz. [number]; sygn. [chamber] [number])                                                                                                               | Fix format; verify Dz.U. reference against ISAP                                            |
| **Currency (Aktualność)** | Every cited provision verified for amendments, repeal, or Constitutional Tribunal annulment; every SN/TK decision verified as still current and not overruled                                                                           | Flag [SPRAWDŹ AKTUALNOŚĆ]; note any known 2022–2026 amendments                             |
| **Domain (Zakres)**       | Analysis stays within Polish law; no import of common law doctrines without Polish-law equivalent translation (e.g., do not use "frustration" — use Art. 475 KC; do not use "void for uncertainty" — use Art. 58 KC ambiguity analysis) | Remove or translate the imported doctrine; add [WERYFIKACJA JURYSDYKCJI]                   |
| **Confidence (Pewność)**  | Uncertainty explicitly stated, not hidden in hedging language; where confidence is below 0.60 (Probable), the opinion must disclose this in the Wnioski                                                                                 | Add confidence qualifier; remove hedge phrases (wydaje się, być może, nie jest wykluczone) |

### Self-Interrogation for IMPERMISSIBLE and UNCERTAIN Conclusions

For every conclusion classified as IMPERMISSIBLE or UNCERTAIN at Confidence ≥ 0.60, run
this 3-pass review before finalising:

**Pass 1 — Prawny łańcuch przyczynowy (Legal Chain Integrity)**

Does the IMPERMISSIBLE conclusion follow logically from the cited authority? Would a
Polish court or regulatory authority (organ administracyjny) actually reach this conclusion
on these facts? Is there a statutory construction that leads to a different result without
straining the text?

**Pass 2 — Kompletność analizy (Completeness)**

Have all relevant provisions been considered? Check:

- Are there applicable provisions in KSH that modify the KC analysis (or vice versa)?
- Has the form requirements layer been completed?
- Has the Art. 17 KSH corporate consent analysis been applied where a company act is involved?
- Have EU law dimensions been considered where potentially applicable?
- Has the invalidity type been correctly identified (nieważność bezwzględna vs. wzruszalność
  vs. bezskuteczność)?

**Pass 3 — Adversarial challenge (Kontrargumenty)**

What is the strongest counter-argument to this conclusion? Could a reputable Polish
kancelaria prawna (law firm) issue an opinion reaching the opposite conclusion on a
supportable legal basis? If yes — either (a) lower confidence to Possible (0.40–0.59) and
disclose the uncertainty, or (b) strengthen the analysis to clearly distinguish the
counter-position. Do not maintain IMPERMISSIBLE at High confidence where the counter-
argument is not clearly refuted.

Mark the Glass Box with `self_interrogation: "PASS"` or `self_interrogation: "REVISED"`.

### Confidence Scoring Application

When setting confidence for each conclusion:

- Base the numeric estimate on the strength of the authority (TK erga omnes → Definite;
  settled SN line → High; divided doctrine → Probable or Possible)
- Adjust downward by one level if the applicable statute has been amended within the last
  3 years and the transitional provisions are not fully clear
- Adjust downward by one level if the facts provided contain assumptions that have not
  been verified
- Never state a conclusion at Definite (0.95–1.0) based on doctrine alone — Definite
  requires at least a zasada prawna SN or TK erga omnes ruling

---

## Anti-Patterns

The following are the most common failures in Polish legal memoranda. Do not reproduce them.

1. **Answering a different question** — spending 10 pages on a general legal framework
   without directly answering the specific pytanie prawne posed. Every numbered question in
   the Przedmiot opinii must receive a direct numbered answer in the Wnioski.

2. **Missing "stan prawny na dzień" declaration** — failure to state the legal status date
   creates ambiguity about whether subsequent amendments affect the analysis. Every opinia
   must declare: "Stan prawny na dzień [date] r."

3. **Treating SN ordinary judgments as binding** — the correct formulation is "w
   orzecznictwie SN przyjmuje się" (in SN jurisprudence it is held), not "jest ugruntowane,
   że" (it is established that) unless there is an SN zasada prawna. Stare decisis does not
   apply in Polish law.

4. **Conflating KC invalidity types** — using "nieważność" without specifying whether this
   is nieważność bezwzględna (Art. 58 KC — void ab initio, cannot be cured), wzruszalność
   (voidable — can be ratified or not invoked), or bezskuteczność (effective inter partes
   but ineffective against third parties). Each has different consequences, remedies, and
   procedural requirements.

5. **Omitting form analysis** — analysing the substantive permissibility of a transaction
   without checking form requirements is an incomplete analysis under Polish law. Forma
   pisemna pod rygorem nieważności and forma aktu notarialnego are jurisdictionally unique
   features of Polish civil law that have no direct common law equivalent. Omission is a
   material analytical error.

6. **Ignoring Art. 17 KSH corporate consent** — for any legal act by a company that may
   require a shareholders' meeting or supervisory board resolution, failing to check whether
   such a resolution was required under KSH or the articles. If required and absent, the
   consequence is invalidity (or bezskuteczność zawieszona for a 2-month ratification window
   under Art. 17 §2 KSH).

7. **Importing common law doctrines without translation** — using "frustration of purpose"
   instead of Art. 475 KC (supervening impossibility) or Art. 357¹ KC (clausula rebus sic
   stantibus); "void for uncertainty" instead of Art. 58 KC analysis; "promissory estoppel"
   instead of the culpa in contrahendo doctrine under Art. 72 KC; "apparent authority"
   instead of the pełnomocnictwo rzekomego (Art. 39, 104 KC) framework. These are different
   doctrines with different elements and consequences.

8. **Ignoring zasady współżycia społecznego** — Polish courts can and do strike down
   commercially standard provisions on the basis that their exercise violates these
   principles (Art. 5, Art. 353¹, Art. 58 §2 KC). Failing to assess this limit — particularly
   for contractual penalty clauses, exclusion clauses, and unilateral termination rights — is
   an incomplete analysis.

9. **Failing to distinguish KC and KSH regimes** — where both could apply (e.g., validity of
   a legal act by a sp. z o.o. board), identify which regime governs (KC general rules; KSH
   lex specialis where KSH addresses the issue). Art. 2 KSH governs the relationship.

10. **Hedging instead of concluding** — phrases such as "wydaje się, że" (it seems that),
    "być może" (perhaps), "nie jest wykluczone, że" (it cannot be excluded that), "kwestia
    ta jest kontrowersyjna" without resolution — these are professional failures, not caution.
    Where genuine uncertainty exists, disclose it in the confidence score and present both
    sides; where it does not, state the conclusion directly.

11. **Outdated case law** — citing SN or TK decisions without verifying they remain current,
    especially in areas affected by: the 2018 KC limitation period reform; the 2022 KSH
    reform; the ongoing TK independence crisis; EU law primacy issues post-2021. Mark all
    decisions [VERIFY] if not confirmed against sn.pl or nsa.gov.pl.

12. **Client-directed conclusion** — issuing an opinion that reaches the conclusion the
    client desires rather than what the law supports. This violates the independence
    requirement under KERP and ZZEA (ethics codes). Where the client's desired conclusion
    is unsupported, the opinion must say so, and may suggest how the situation could be
    legally restructured to achieve a permissible outcome.

13. **No Zastrzeżenia section** — failure to include the scope limitation clause, reliance
    restriction ("wyłącznie na użytek zleceniodawcy"), and the caveat that new facts may
    change conclusions exposes the issuing professional to liability and renders the opinion
    procedurally incomplete.

14. **Mixing factual assumptions with legal conclusions** — legal analysis must rest on
    clearly stated, documented facts. Undocumented assumptions must be flagged as "przyjmując
    za podstawę niniejszej opinii, że..." (taking as a premise for this opinion that...).
    Unstated assumptions that later prove false will invalidate the conclusions.

15. **Stopping at wykładnia językowa** — taking the literal text as dispositive without
    testing it against systemowa and celowościowa methods. Polish courts routinely correct
    linguistically clear provisions where the literal result is absurd or contrary to
    legislative purpose. Opinia that does not acknowledge this step may be analytically
    incomplete.

16. **Ignoring TK/EU law tension** — for any question touching EU law, failing to note
    where TK rulings may conflict with CJEU jurisprudence and that ordinary Polish courts
    apply EU law primacy. An opinion that relies on a TK ruling subsequently found contrary
    to EU law (post-C-448/23) without caveat is materially flawed.

17. **Signature block without bar roll number** — a formal opinia prawna signed without the
    issuing radca prawny's or adwokat's bar roll number (numer wpisu na listę) and chamber
    affiliation (OIRP/ORA) is procedurally incomplete. The AI skill produces a placeholder;
    the qualified professional must complete it.

---

## Writing Standards

Apply these standards before delivering any opinia:

**1. Specificity over generality**: Every legal claim must be anchored to a specific
article, paragraph, and point. "The Civil Code provides..." is inadequate. "Pursuant to
Art. 353¹ KC..." is correct. If you cannot identify the specific provision, mark the
claim [NIEZWERYFIKOWANE] rather than stating it without citation.

**2. Active voice with a named legal actor**: "Zgodnie z art. 201 §1 KSH, zarząd prowadzi
sprawy spółki i ją reprezentuje" (the board conducts company affairs and represents it),
not "it is the case that the company is represented by the management board."

**3. Anti-hedging discipline**: Remove hedge phrases — wydaje się (it seems), być może
(perhaps), nie jest wykluczone (it cannot be excluded), kwestia ta jest sporna bez
dalszego komentarza (the issue is disputed without further comment). Replace with: (a) a
direct conclusion at the appropriate confidence level, or (b) an explicit uncertainty
disclosure ("Zagadnienie to nie zostało rozstrzygnięte w jednolitym orzecznictwie SN...
Autor opinii stoi na stanowisku, że...").

**4. Bilingual glossing**: On first use of each Polish legal term in a section, provide the
English equivalent in parentheses. Subsequent references may use Polish alone. Example:
"zasady współżycia społecznego (principles of social coexistence)". This is particularly
important in cross-border transaction opinions destined for international counterparties.

**5. Logical traceability**: Every wniosek (conclusion) in the Wnioski section must be
traceable to a specific numbered paragraph in the Analiza prawna. Number the wnioski to
correspond with the zagadnienia prawne from the Przedmiot opinii.

**Quality gates before delivery**:

- [ ] Does each wniosek directly answer the corresponding pytanie prawne from the Przedmiot?
- [ ] Is every legal claim backed by a specific article citation or marked [NIEZWERYFIKOWANE]?
- [ ] Has hedge language been removed and replaced with direct conclusions or explicit
      uncertainty disclosure?
- [ ] Does the Zastrzeżenia section contain all mandatory clauses (scope, stan prawny date,
      reliance restriction, new facts caveat)?
- [ ] Are all Polish legal terms glossed in English on first use in each section?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 4, search for: (1) KC, KSH, KPA provisions with current consolidated text
  references from ISAP; (2) SN uchwały on the relevant legal issues (especially zasady
  prawne); (3) TK decisions on any relevant constitutional questions; (4) NSA/WSA rulings
  for administrative law questions; (5) CJEU preliminary rulings where EU law applies
- Save all results to `/tmp/pl-legal-memo-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Proceed with built-in legal framework sections and general knowledge
- Mark all statutory and case law citations [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Recommend verification against ISAP (isap.sejm.gov.pl), sn.pl, nsa.gov.pl, trybunal.gov.pl
- Focus the opinion on structural quality, logical reasoning, and explicit confidence
  disclosures rather than authoritative citation depth

**Authoritative Polish legal databases for manual verification**:

| Database               | URL               | Content                                          |
| ---------------------- | ----------------- | ------------------------------------------------ |
| ISAP                   | isap.sejm.gov.pl  | Consolidated statutory texts — definitive source |
| Sąd Najwyższy          | sn.pl             | Supreme Court decisions and resolutions          |
| NSA / WSA              | nsa.gov.pl        | Administrative court decisions                   |
| Trybunał Konstytucyjny | trybunal.gov.pl   | Constitutional Tribunal decisions                |
| LEX / Legalis          | Commercial        | Case law, commentary, consolidated texts         |
| EUR-Lex                | eur-lex.europa.eu | EU legislation and CJEU decisions                |

---

## Output Format Template

The following template defines the canonical structure of a Polish opinia prawna produced
by this skill. Every formal opinion must include all eight sections. The memorandum prawne
(informal) may omit the Podstawa prawna enumeration and abbreviate the Zastrzeżenia.

````markdown
# OPINIA PRAWNA

# [Title describing the subject matter]

**Data:** [Warszawa / city], dnia [date] r.
**Numer referencyjny:** [reference number or "---"]
**Zleceniodawca:** [Client name and registered address]
**Wystawca:** [AI-assisted draft — do not release without review by qualified radca prawny
or adwokat; name, numer wpisu, OIRP/ORA affiliation to be completed by issuing professional]

---

## I. Przedmiot opinii (Subject Matter)

Niniejsza opinia prawna (the Opinion) została sporządzona w odpowiedzi na zlecenie
[Zleceniodawca] z dnia [date] i dotyczy wyłącznie następujących zagadnień prawnych:

1. [Question 1 — precise statement of the legal question]
2. [Question 2 — if applicable]
3. [Question N — if applicable]

**Stan prawny na dzień:** [date]

Opinia opiera się wyłącznie na faktach i dokumentach przedstawionych przez Zleceniodawcę,
opisanych w Sekcji III poniżej. Zmiana stanu faktycznego może mieć wpływ na wnioski
niniejszej opinii.

---

## II. Wnioski (Conclusions)

_[Executive Summary — for commercial opinions, place before Analiza prawna]_

| Nr  | Zagadnienie  | Wniosek                                                                                             | Pewność analizy                        |
| --- | ------------ | --------------------------------------------------------------------------------------------------- | -------------------------------------- |
| 1   | [Question 1] | DOPUSZCZALNE / DOPUSZCZALNE Z ZASTRZEŻENIAMI / NIEPEWNE / NIEDOPUSZCZALNE / WYMAGA ZGODY REGULATORA | Definite/High/Probable/Possible (0.XX) |
| 2   | [Question 2] | ...                                                                                                 | ...                                    |

Szczegółowe uzasadnienie każdego wniosku zawarte jest w Sekcji V (Analiza prawna).

---

## III. Podstawa faktyczna (Factual Foundation)

Niniejsza opinia opiera się na następujących faktach i dokumentach:

**Dokumenty dostarczone przez Zleceniodawcę:**

- [Document 1: name, date, and summary of relevance]
- [Document 2: name, date, and summary of relevance]

**Fakty przyjęte za podstawę opinii:**

1. [Fact 1 — stated as established from documents]
2. [Fact 2 — if factual assumption: "Przyjmując za podstawę niniejszej opinii, że..."]

**Uwaga**: Wnioski niniejszej opinii opierają się wyłącznie na faktach opisanych powyżej.
Ujawnienie nowych okoliczności może zmienić ocenę prawną.

---

## IV. Podstawa prawna (Legal Basis)

Niniejsza opinia opiera się na następujących aktach prawnych, orzeczeniach i doktrynie:

**Akty normatywne (Normative Acts):**

- Kodeks cywilny z dnia 23 kwietnia 1964 r., t.j. Dz.U. [year] poz. [number]
- [Other statutes applicable to the questions]

**Orzecznictwo sądowe (Case Law):**

- [SN/TK/NSA decisions cited — sygn., key holding]

**Doktryna prawnicza (Legal Doctrine):**

- [Author, Title, edition, publisher, year, art. and margin number]

---

## V. Analiza prawna (Legal Analysis)

### §1. [Short title of Question 1]

**[a] Teza prawna (Applicable norm):**
Zgodnie z art. [X] [§Y] [KC/KSH/KPA]:
"[Exact text of provision — marked [VERIFY] if not confirmed against ISAP]"

**[b] Stan faktyczny i subsumcja (Facts and application):**
[Apply the provision to the client's specific facts. State which elements of the norm are
satisfied and which are not, with reference to the documents in Section III.]

**[c] Analiza wykładni (Interpretation analysis):**
_Wykładnia językowa:_ [Result of linguistic interpretation]
_Wykładnia systemowa:_ [Systematic context — if material to the result]
_Wykładnia celowościowa:_ [Purpose of the provision — if linguistic result is ambiguous]

_Orzecznictwo:_ [Cite applicable SN/TK/NSA decisions with correct authority characterisation]
_Doktryna:_ [Cite applicable commentary if relevant and no SN ruling exists]

**[d] Forma prawna (Form requirements — complete for every transaction analysis):**
| Form Requirement | Required? | Provision | Consequence of failure |
|-----------------|-----------|-----------|----------------------|
| [Form type] | Yes/No | Art. [X] KC | [Nieważność bezwzględna / ograniczenia dowodowe / inne] |

**[e] Typ nieważności (Invalidity type — if applicable):**
[NIEWAŻNOŚĆ BEZWZGLĘDNA / WZRUSZALNOŚĆ / BEZSKUTECZNOŚĆ / BEZSKUTECZNOŚĆ ZAWIESZONA]
Podstawa: Art. [X] [KC/KSH]. Konsekwencje: [...]

**[f] Wniosek cząstkowy (Intermediate conclusion for Question 1):**
**[DOPUSZCZALNE / DOPUSZCZALNE Z ZASTRZEŻENIAMI / NIEPEWNE / NIEDOPUSZCZALNE /
WYMAGA ZGODY REGULATORA]** — Confidence: [level] ([numeric range])

[Direct answer to Question 1 in one to three sentences. No hedging.]

[Conditions if "Dopuszczalne z zastrzeżeniami":

- Warunek 1: [...]
- Warunek 2: [...]]

---

### §2. [Short title of Question 2 — repeat structure above]

---

---

## VI. Zastrzeżenia (Reservations and Limitations)

1. **Zakres zlecenia (Scope)**: Niniejsza opinia dotyczy wyłącznie zagadnień prawnych
   opisanych w Sekcji I. Kwestie nieobjęte niniejszą opinią nie zostały zbadane i nie
   powinny być wywodzone z niniejszego dokumentu.

2. **Stan prawny (Currency)**: Niniejsza opinia odzwierciedla stan prawny na dzień wskazany
   w Sekcji I. Późniejsze zmiany ustawodawstwa, orzecznictwa lub aktów wykonawczych mogą
   zmienić wnioski niniejszej opinii.

3. **Ograniczenie reliance (Reliance restriction)**: Niniejsza opinia sporządzona jest
   wyłącznie na użytek [Zleceniodawca] w związku z [described purpose]. Nie może być
   przywoływana przez osoby trzecie ani stosowana w innych celach bez uprzedniej pisemnej
   zgody wystawcy.

4. **Nowe fakty (New facts)**: Wnioski niniejszej opinii opierają się na faktach
   opisanych w Sekcji III. Ujawnienie nowych okoliczności może zmienić ocenę prawną
   i wymagać uzupełnienia lub zmiany niniejszej opinii.

5. **Analiza podatkowa (Tax scope)**: [Niniejsza opinia nie obejmuje aspektów podatkowych
   transakcji / Analiza podatkowa jest / nie jest przedmiotem niniejszej opinii — specify]

6. **AI-assisted draft**: Niniejsza opinia sporządzona została przy wsparciu systemu AI
   (Legalcode). Wymaga przeglądu i akceptacji przez uprawnionego radcę prawnego lub
   adwokata przed udostępnieniem zleceniodawcy.

---

## VII. Podpis (Signature Block)

[Do not release before completion by a qualified professional]

---

[Name]
Radca prawny / Adwokat
Nr wpisu: [bar roll number]
[OIRP / ORA chamber name]
[city], dnia [date] r.

---

## Glass Box Audit Trail

```yaml
glass_box:
  opinion_subject: "[Brief description of the legal question(s)]"
  mode: "Created"
  requesting_party: "[Zleceniodawca name or type]"
  opinion_type: "Opinia prawna (formal) / Memorandum prawne (informal)"
  governing_law: "Polish law (prawo polskie)"
  stan_prawny_date: "[date]"
  legal_basis:
    primary_codes: ["KC", "KSH", "KPA"] # adjust as needed
    specialized_statutes: ["[list or empty]"]
    eu_law: ["[list or empty]"]
  questions_analyzed: N
  conclusions:
    - question: "Question 1"
      conclusion: "PERMISSIBLE / PERMISSIBLE WITH CONDITIONS / UNCERTAIN / IMPERMISSIBLE / REQUIRES REGULATORY CLEARANCE"
      confidence: "[level] (0.XX)"
    - question: "Question 2"
      conclusion: "..."
      confidence: "..."
  form_requirements_checked: "Yes / No"
  form_requirements_identified: "[list or 'None identified']"
  invalidity_types_addressed: "[nieważność bezwzględna / wzruszalność / bezskuteczność / N/A]"
  ksh_corporate_consents_checked: "Yes / No / N/A — [list of consent requirements identified]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "[Art. X Code — VERIFIED / UNVERIFIED]"
  case_law_consulted:
    - "[SN/TK/NSA — sygn. — VERIFIED / UNVERIFIED]"
  citations_verified: "[N VERIFIED] / [N UNVERIFIED]"
  tku_eu_tension_applicable: "Yes / No — [brief note if Yes]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  limitations:
    - "[factual assumptions relied on]"
    - "[scope exclusions]"
    - "[statutory currency limitations]"
  reviewer: "AI-assisted — requires review by qualified radca prawny or adwokat before use"
```
````

```

---

## Localization Notes

This skill is Poland-specific. All outputs are governed by Polish law.

**Language**: The opinia prawna is produced primarily in Polish, consistent with standard
Polish legal practice. Bilingual glossing (Polish term with English translation in
parentheses on first use in each section) is applied for cross-border transaction opinions.

**Authoritative legal database**: All statutory citations should be verified against
ISAP (isap.sejm.gov.pl). LEX and Legalis are the leading commercial legal databases
for case law and commentary.

**Professional requirements**: The final opinion must be reviewed, accepted, and signed by
a radca prawny or adwokat licensed in Poland. AI-assisted drafts must not be delivered to
clients as final opinions without such review.

**EU law integration**: Since Poland's EU accession in 2004, EU law takes primacy.
For opinions on EU-intersecting matters (competition law, data protection, financial
services regulation, environmental law), always assess EU law alongside Polish domestic
provisions. For CJEU preliminary rulings on questions of EU law interpretation, those
rulings bind the Polish court that made the reference and carry very strong authority
for all other Polish courts.

**KRS identification**: Party identification in Polish corporate opinions should always
include the KRS number (national court register) and NIP (tax identification number),
plus verification of signatory authority from the entity's current KRS extract
(odpis pełny lub aktualny z KRS). Management board representation rules (joint vs.
individual) must be verified from the current KRS entry, not assumed from the articles.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on:
- Repository reference standard: `skills/general/contracts/legalcode-contract-review`
  (structural quality frameworks, workflow design, citation gates, self-interrogation,
  confidence scoring, Glass Box pattern)
- Repository Poland baseline: `skills/jurisdictions/poland/contracts/legalcode-nda-triage-pl`
  (Polish legal terminology convention, bilingual output pattern, kary umowne analysis,
  KC framework, RODO integration, Polish authoritative sources)
- IURA methodology reference: `general/contracts/imported-iura-plugins--iura-pl-skills-contract-review`
  (IURA Poland analytical methodology)
- Deep legal research via web research on Polish opinia prawna conventions, KC/KSH/KPA
  provisions, Polish court structure and precedent treatment, statutory interpretation
  methodology, and professional ethics standards
- Agent team structural analysis (2-agent research pipeline: Structural Analyst + Legal
  Research Agent)

Legal substance references (all [VERIFY] against authoritative sources):
- Kodeks cywilny t.j. Dz.U. 2024 poz. 1061
- Kodeks spółek handlowych t.j. Dz.U. 2024 poz. 18 (as amended by reform 2022, Dz.U. 2022 poz. 807)
- Kodeks postępowania administracyjnego t.j. Dz.U. 2024 poz. 572
- ISAP consolidated text references (isap.sejm.gov.pl)
- Professional ethics: Kodeks Etyki Radcy Prawnego (KERP); Zbiór Zasad Etyki Adwokackiej (ZZEA)
- Statutory interpretation: Maciej Zieliński, Wykładnia prawa — zasady, reguły, wskazówki
- CJEU: C-448/23 (December 2025) on TK independence and EU law primacy [VERIFY]
```
