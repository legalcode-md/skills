---
name: legalcode-complaint-drafter-is
description: Drafts stefnur (writs of summons / statements of claim) for civil proceedings in Iceland
  under lög um meðferð einkamála nr. 91/1991 (Code of Civil Procedure). Maps client facts to the legal
  elements of each cause of action under Icelandic law, validates compliance with Article 80 requirements,
  and structures dómkröfur (claims), málavextir (factual narrative), lagarök (legal arguments), and sönnunargögn
  (evidence list). Covers héraðsdómur (district court), Landsréttur (Court of Appeal), and Hæstiréttur
  (Supreme Court) proceedings. Produces court-ready stefnur in the concise Icelandic format (5-6 pages
  typical), with proper kennitala identification, Icelandic-language drafting, and Art. 36 Codex Ethicus
  pre-litigation settlement verification. Companion to legalcode-complaint-drafter (US) and legalcode-complaint-drafter-ew
  (England & Wales). Based on Nordic civil law tradition with EEA/Lugano cross-border framework.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Complaint Drafter — Iceland (Stefnugerð)

> **Fyrirvari / Disclaimer**: This skill provides a framework for AI-assisted
> drafting of stefnur (writs of summons) for Icelandic civil proceedings. It
> does not constitute legal advice (lögfræðiráðgjöf). All outputs must be
> reviewed, verified, and signed by a qualified Icelandic attorney (lögmaður)
> licensed to practise before the relevant court level before filing. Icelandic
> procedural rules, case law (dómafordæmi), and legislation change; verify all
> authoritative sources before reliance. AI-generated pleadings may contain
> errors in element identification, jurisdictional analysis, or factual
> characterisation — all allegations must be verified against actual evidence
> and client instructions. Any cited authority marked `[VERIFY]` has not been
> independently validated and must be confirmed before reliance. A lögmaður
> filing a stefna is bound by the Codex Ethicus of the Icelandic Bar
> Association (Lögmannafélag Íslands), including the obligation not to provide
> false or misleading information to courts (Art. 20) and to present claims
> and offer settlement before litigation (Art. 36).

---

## Purpose and Scope

This skill drafts stefnur (writs of summons / statements of claim) for civil
proceedings in Iceland. It maps client facts to the legal elements of each
cause of action under Icelandic substantive law, validates compliance with
Article 80 of lög um meðferð einkamála nr. 91/1991, and produces court-ready
documents in the concise format expected by Icelandic courts.

The skill operates in two primary modes:

1. **Full Draft Mode** (Stefnugerð): Generates a complete, court-ready stefna
   from client facts — including party identification with kennitala, dómkröfur
   (claims), málavextir (factual narrative), lagarök (legal arguments), and
   sönnunargögn (evidence list).

2. **Validation Mode** (Endurskoðun): Takes an existing draft stefna and
   validates it against Article 80 requirements — checking completeness,
   conciseness, frávísun (dismissal) risk, and strategic coherence.

**Covers:**

- **Article 80 compliance**: All mandatory stefna elements (parties, claims, facts, law, evidence)
- **Concise Icelandic format**: 5-6 page standard, material facts only
- **Icelandic causes of action**: Contract (samningalög), tort (skaðabótaréttur), employment, property, commercial
- **Court jurisdiction**: Héraðsdómur, Landsréttur, Hæstiréttur allocation
- **Frávísun analysis**: Dismissal risk assessment under Act 91/1991
- **Party identification**: Kennitala (national ID), legal entity types (hf., ehf., sf.)
- **Pre-filing obligations**: Art. 36 Codex Ethicus settlement attempt
- **Cross-border**: EEA/Lugano Convention jurisdiction, Hague Service Convention
- **Limitation periods**: Act 150/2007 (fyrningarlög) compliance
- **Remedies**: Compensatory damages (skaðabætur), non-pecuniary (miskabætur), injunctions (lögbann), interest (dráttarvextir)
- **Class actions**: Art. 19a group litigation (opt-in, 3+ claimants)
- **Filing mechanics**: Court fees, service methods (birting), language requirements

**Does not:**

- Replace a lögmaður's professional judgment on claim viability or litigation strategy
- Draft documents in Icelandic (outputs in English with Icelandic terminology — lögmaður must translate and finalize)
- File documents with any court (héraðsdómur)
- Certify compliance with the Codex Ethicus (only the filing lögmaður may certify)
- Conduct independent factual investigation
- Provide oral advocacy preparation (Icelandic proceedings are oral-argument-centric)
- Handle criminal proceedings (sakamál), administrative proceedings, or bankruptcy (gjaldþrot)
- Draft greinargerð (statement of defence) — separate skill

**Related skills:**

- `legalcode-complaint-drafter` — US federal/state complaint drafting
- `legalcode-complaint-drafter-ew` — England & Wales statement of case drafting
- `legalcode-brief-analyzer` — Analysis of legal briefs and submissions
- `legalcode-damages-calculation` — Damages quantification framework
- `legalcode-early-case-assessment` — Pre-filing case evaluation

---

## Jurisdiction and Governing Law

This skill is **jurisdiction-specific to Iceland** (Ísland). All procedural
references are to lög um meðferð einkamála nr. 91/1991 (Code of Civil
Procedure) as amended. Substantive law references are to Icelandic legislation,
general principles of Icelandic law, and Nordic legal tradition.

**Key procedural sources:**

- Lög um meðferð einkamála nr. 91/1991 (Code of Civil Procedure) — English translation available at government.is [VERIFY]
- Lög um dómstóla nr. 50/2016 (Courts Act — establishing Landsréttur)
- Lögmannalög nr. 77/1998 (Act on Lawyers)
- Lög um aukatekjur ríkissjóðs nr. 88/1991 (filing fees)
- Codex Ethicus (Lögmannafélag Íslands, revised 2000, amended 2015, 2023)

**Key substantive sources:**

- Lög um samningsgerð, umboð og ógilda löggerninga nr. 7/1936 (Contracts Act — Nordic uniform)
- Skaðabótalög nr. 50/1993 (Damages Act)
- Lög um fyrning kröfuréttinda nr. 150/2007 (Limitation Act)
- Lög um lögbann og dómsmál til að vernda einkarétt nr. 31/1990 (Injunctions Act)
- Vaxtalög nr. 38/2001 (Interest Act)
- EEA Agreement (Act No. 2/1993)
- Lugano Convention 2007 (in force for Iceland 1 May 2011)

**Court hierarchy (þriggja þrepa dómskerfi — three-tier system since 2018):**

| Level        | Court                                    | Judges                 | Role                                                                                     |
| ------------ | ---------------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------- |
| 1st instance | Héraðsdómur (8 district courts)          | 1 judge (civil)        | Trial, fact-finding, judgment                                                            |
| Appeal       | Landsréttur (Court of Appeal, est. 2018) | 15 judges, panels of 3 | Review of law and fact; most cases reach final resolution here                           |
| Supreme      | Hæstiréttur (Supreme Court)              | 7 judges               | Precedent-setting; leave to appeal required; ~50-60 cases/year from 150-200 applications |

**Specialized courts:**

- Félagsdómur (Labour Court) — collective agreement disputes
- Mannréttindadómstóll Evrópu (ECtHR) — ECHR via Act 62/1994

---

## Interactive Clarification

Before drafting, gather essential context through structured questions. Only ask
when the answer would materially change the stefna's content or strategy.
Default to reasonable assumptions and state them explicitly.

### CLARIFY 1: Analysis Objective

> **What do you need?**
>
> - **Full stefna draft** — Generate complete stefna from client facts (default)
> - **Validation of existing draft** — Review existing stefna for Art. 80 compliance and frávísun risk
> - **Cause of action mapping** — Identify viable causes of action from facts without full drafting
> - **Limitation check** — Verify claims are within fyrning (limitation) periods
>
> _Why this matters_: Full drafting requires comprehensive facts; validation
> focuses on structure and compliance; cause of action mapping is a strategic
> pre-filing exercise.

### CLARIFY 2: Client Side and Posture

> **Which side are you representing?**
>
> - **Stefnandi (Plaintiff)** — Initiating proceedings (default)
> - **Stefndi (Defendant)** considering counterclaim — Preparing gagnstefna
> - **Third party** joining existing proceedings
>
> _Why this matters_: Determines document structure, burden allocation, and
> strategic framing. Gagnstefna (counterclaim) has specific procedural
> requirements.

### CLARIFY 3: Court Level

> **Which court will receive this stefna?**
>
> - **Héraðsdómur** (District Court) — most civil claims start here (default)
> - **Specific héraðsdómur** — if venue matters (Reykjavík, Reykjanes, Vesturland, Vestfirðir, Norðurland vestra, Norðurland eystra, Austurland, Suðurland)
>
> _Why this matters_: Determines filing location, local practices, and
> applicable court fees. Most civil cases are filed in Héraðsdómur Reykjavíkur.

### CLARIFY 4: Cause of Action Type

> **What is the primary legal basis for this claim?**
>
> - **Samningaréttur (Contract)** — breach of contract, formation disputes, Section 36 fairness
> - **Skaðabótaréttur (Tort)** — fault-based (saknæmi), strict liability (hlutlæg ábyrgð)
> - **Vinnuréttur (Employment)** — wrongful termination, discrimination, collective agreement breach
> - **Eignaréttur (Property)** — ownership, boundary, registration (þinglýsing) disputes
> - **Viðskiptaréttur (Commercial)** — company law, competition, insolvency
> - **Neytendaréttur (Consumer)** — consumer protection, EEA-harmonised
> - **Multiple / uncertain** — will assess from facts
>
> _Why this matters_: Each cause of action has different elements, limitation
> periods, burden of proof, and available remedies under Icelandic law.

### CLARIFY 5: Available Materials

> **What materials do you have?**
>
> - Client interview notes / fact summary
> - Key contracts or agreements
> - Correspondence (emails, letters)
> - Financial records / invoices
> - Prior legal opinions or memoranda
> - Expert reports (if any — note: Icelandic courts use court-appointed experts, not party experts)
> - Kennitala for all parties (required for stefna)
>
> _Why this matters_: Article 80 requires specific evidence identification.
> Icelandic courts do not permit discovery — all evidence must be identified
> and available at filing.

### CLARIFY 6: Pre-Litigation Settlement

> **Has a settlement attempt been made?**
>
> - **Yes** — describe outcome (required under Codex Ethicus Art. 36)
> - **No, but planned** — settlement letter will be sent before filing
> - **No — urgency exception** — immediate filing required (explain urgency)
> - **Not applicable** — describe why
>
> _Why this matters_: Article 36 of the Codex Ethicus requires attorneys to
> present claims and offer settlement before initiating litigation, unless
> urgent circumstances require immediate filing. Failure to attempt settlement
> may draw criticism from the court and the Bar.

### CLARIFY 7: Cross-Border Elements

> **Does this matter involve parties or elements outside Iceland?**
>
> - **Purely domestic** — all parties and events in Iceland (default)
> - **EEA/Lugano** — defendant domiciled in another Lugano Convention state
> - **Hague Convention** — service on party outside Lugano states
> - **Foreign law applies** — choice of law issues
> - **Foreign judgment** — seeking recognition/enforcement in Iceland
>
> _Why this matters_: Cross-border elements engage the Lugano Convention
> jurisdiction rules, Hague Service Convention requirements, and potentially
> EFTA Court advisory opinions. Iceland objected to Hague Art. 10(a) postal
> service — service must go through the Central Authority.

### CLARIFY 8: Review Depth

> **How thorough should the analysis be?**
>
> - **Standard** — Full Art. 80 compliance, element mapping, frávísun risk (default)
> - **Express** — Quick compliance check, key issues only
> - **Comprehensive** — Deep analysis including authority research, limitation
>   verification, cross-border assessment, costs estimate, and strategic recommendations
>
> _Why this matters_: Determines depth of research, number of [VERIFY] markers,
> and detail of Glass Box reasoning trail.

---

## Workflow

### Step 1: Accept Input

Accept the client's matter in any format:

- Fact narrative or client interview notes
- Existing draft stefna for review
- Contract, correspondence, or document corpus
- Verbal description of dispute

If receiving a document, read it fully before proceeding.

### Step 2: Gather Context (Interactive Clarification)

Ask CLARIFY questions 1-8 as needed. If the user provides comprehensive
instructions, skip questions where answers are obvious from context. Always
confirm:

- Client side (stefnandi/stefndi)
- Primary cause of action type
- Whether pre-litigation settlement has been attempted (Art. 36)
- Whether kennitala is available for all parties

Default assumptions (state explicitly if used):

- Héraðsdómur Reykjavíkur unless facts indicate another venue
- Standard review depth
- Purely domestic matter
- Stefnandi (plaintiff) posture

### Step 3: Identify Causes of Action

Map client facts to Icelandic causes of action (see Causes of Action Library
below). For each cause of action:

1. Identify the statutory basis and/or general principle
2. List the required legal elements
3. Map specific client facts to each element
4. Assess whether facts satisfy each element
5. Flag elements with weak or missing factual support
6. Check limitation period under Act 150/2007

**Critical Icelandic principle**: The stefna must be "concise and clear"
(Art. 80). Do not over-plead. State material facts only; detailed legal
argument is reserved for oral proceedings (munnlegur málflutningur).

### Step 4: Check Limitation Periods (Fyrning)

Verify each cause of action is within the applicable limitation period
under lög um fyrning kröfuréttinda nr. 150/2007:

| Period                | Applies to                                               | Notes                                                                |
| --------------------- | -------------------------------------------------------- | -------------------------------------------------------------------- |
| **4 years** (general) | Most claims including contract, tort, unjust enrichment  | Default period; runs from when claim could first be brought [VERIFY] |
| **10 years**          | Claims based on written instruments (skuldabréf), bonds  | Longer period for formalized obligations [VERIFY]                    |
| **2 years**           | Certain commercial claims, specific statutory provisions | Check specific statute [VERIFY]                                      |
| **1 year**            | Employment claims (certain types), insurance claims      | Check specific statute [VERIFY]                                      |
| **Suspension**        | Claimant unaware of claim or unable to bring it          | Objective discoverability standard [VERIFY]                          |
| **Interruption**      | Filing of stefna, acknowledgment by debtor               | Resets the period [VERIFY]                                           |

If a limitation period has arguably expired, flag as CRITICAL with specific
analysis and recommendation on whether to proceed (argue tolling/suspension)
or abandon that cause of action.

### Step 5: Assess Frávísun (Dismissal) Risk

Evaluate whether the stefna as drafted would survive a frávísun (dismissal)
application. Under Act 91/1991, a stefna may be dismissed if: [VERIFY]

1. **Jurisdictional defect** — wrong court, no subject matter jurisdiction
2. **Article 80 non-compliance** — missing mandatory elements (names, kennitala, claims, facts, law)
3. **Insufficient factual basis** — facts as stated do not support any legal claim
4. **Lis pendens** — same matter already pending between same parties
5. **Res judicata** — matter already decided (sömu atriði milli sömu aðila)
6. **No legal interest** — plaintiff lacks standing (lögvarðir hagsmunir) [VERIFY]

**Important**: Iceland has no plausibility standard equivalent to US
Twombly/Iqbal or UK reasonable grounds test. The threshold for surviving
dismissal is lower — the stefna must state a cognizable claim with basic
factual support, but need not demonstrate plausibility at the pleading stage.

### Step 6: Draft the Stefna

Structure the stefna according to the Stefna Structure Template (see below).
Apply these cardinal rules:

1. **Conciseness is mandatory** — 5-6 pages is the norm; exceeding this signals poor drafting
2. **Material facts only** — do not include evidence evaluation, detailed legal argument, or witness testimony summaries
3. **Icelandic terminology** — use Icelandic legal terms (with English translations in parentheses for this skill's output)
4. **Numbered paragraphs** — use sequential numbering throughout
5. **All parties fully identified** — name, kennitala, address for each
6. **Claims must be specific** — exact monetary amounts, specific declaratory relief, or precise injunctive terms
7. **Costs claim included** — always include demand for málskostnaður (legal costs)

### Step 7: Validate and Classify

Apply the Classification System (see below) to assess overall stefna quality.
Run Self-Interrogation for any VULNERABLE or DEFICIENT findings.

### Step 8: Deliver Output

Present the complete output package:

1. Executive summary with overall classification
2. Full stefna draft (in English with Icelandic terminology)
3. Cause of action element map
4. Frávísun risk assessment
5. Limitation period verification
6. Filing checklist (court fees, service method, translation needs)
7. Glass Box audit trail

---

## Stefna Structure Template

The standard Icelandic stefna follows this structure per Article 80 of
lög um meðferð einkamála nr. 91/1991:

```
STEFNA
[Héraðsdómur {dómumdæmi}]

─────────────────────────────────────

Stefnandi (Plaintiff):
  [Full legal name]
  Kennitala: [###-####]
  Heimilisfang (Address): [Full address, Iceland]
  [If legal entity: entity type (hf./ehf./sf./ses./ohf.)]
  Lögmaður stefnanda (Plaintiff's attorney): [Name], [Bar number]

Stefndi (Defendant):
  [Full legal name]
  Kennitala: [###-####]
  Heimilisfang (Address): [Full address]
  [If legal entity: entity type]

─────────────────────────────────────

I. DÓMKRÖFUR (Claims / Prayer for Relief)

  1. [Primary monetary claim — exact amount in ISK]
     [OR: Declaratory relief — exact declaration sought]
     [OR: Injunctive relief — specific conduct to be ordered/prohibited]

  2. Dráttarvextir (default interest) pursuant to III. kafli
     vaxtalaga nr. 38/2001 from [date] until payment. [VERIFY rate]

  3. Málskostnaður (legal costs) at the discretion of the court.

─────────────────────────────────────

II. MÁLAVEXTIR (Statement of Facts)

  [Concise, chronological factual narrative — material facts only.
   Each paragraph numbered sequentially. No evidence evaluation,
   no detailed legal argument. Context sufficient for the court
   to understand the dispute.]

  4. [Background / relationship between parties]
  5. [Key events giving rise to the dispute]
  6. [Breach / wrongful act / triggering event]
  7. [Damage / loss suffered]
  8. [Pre-litigation settlement attempt per Codex Ethicus Art. 36]

─────────────────────────────────────

III. LAGARÖK (Legal Arguments)

  [Reference to main legal provisions and principles relied upon.
   Brief — detailed argument is for oral proceedings.]

  9.  [Primary statutory basis, e.g., "Kröfur stefnanda byggja á
       ákvæðum laga nr. 7/1936 um samningsgerð..."]
  10. [Secondary legal basis if applicable]
  11. [General principles invoked (e.g., meðalhófsreglan —
       proportionality; grandvísi — good faith)]

─────────────────────────────────────

IV. SÖNNUNARGÖGN (Evidence)

  [List of documentary evidence and witnesses. No evaluation.]

  Skjöl (Documents):
  12. [Contract / agreement dated ...]
  13. [Correspondence dated ...]
  14. [Financial records / invoices]

  Vitni (Witnesses):
  15. [Name, kennitala, address — for each witness]

  [Note: Icelandic courts appoint their own experts (dómkvaddir
   matsmenn) — do not list party-appointed experts]

─────────────────────────────────────

[Location], [Date]

________________________
[Name of lögmaður]
Lögmaður stefnanda
[Bar association registration number]
```

---

## Causes of Action Library (Kröfugrundvöllur)

### A. Contract Claims (Samningaréttur)

**Statutory basis**: Lög um samningsgerð, umboð og ógilda löggerninga nr. 7/1936
(Contracts Act — Nordic uniform legislation, shared with Denmark, Norway, Sweden, Finland)

#### A1. Breach of Contract (Samningsrof)

| Element                  | Description                                                                                      | Typical evidence                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| Valid contract           | Formation under general principles (offer, acceptance, consideration not required in Nordic law) | Written agreement, correspondence, course of dealing |
| Obligation               | Specific contractual duty owed by defendant                                                      | Contract terms, implied terms                        |
| Breach                   | Failure to perform or defective performance                                                      | Notice of default, evidence of non-performance       |
| Causation (orsakatengsl) | Breach caused the claimed loss                                                                   | Temporal/logical connection                          |
| Damage (tjón)            | Quantifiable loss suffered                                                                       | Financial records, expert assessment                 |

**Key Icelandic features:**

- No consideration doctrine — contracts bind by agreement alone [VERIFY]
- General duty of good faith (grandvísi) in contractual performance [VERIFY]
- Section 36 of Act 7/1936: Court may set aside or modify contract terms that are "unfair" (ósanngjarnt) — extremely broad fairness power unique to Nordic law [VERIFY]
- Anticipatory breach recognized [VERIFY]

#### A2. Contract Invalidity (Ógildanleiki samnings)

| Element            | Description                                                                                                                |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Existing agreement | Contract or purported contract exists                                                                                      |
| Invalidity ground  | Sections 28-36 of Act 7/1936: duress (nauðung), fraud (svik), usury (okurvextir), mistake (villa), unfairness (Section 36) |
| Prejudice          | Party suffered or would suffer from enforcement                                                                            |

**Section 36 (general fairness clause):** The court may "set aside a contract
in whole or in part, or alter its terms, if it would be unfair or contrary to
good business practice to enforce it." Considers circumstances at formation,
subsequent events, and the contract as a whole. [VERIFY]

#### A3. Unjust Enrichment (Auðgunarkrafa / endurheimtukrafa)

| Element                | Description                                               |
| ---------------------- | --------------------------------------------------------- |
| Enrichment             | Defendant received a benefit                              |
| At plaintiff's expense | Benefit came from plaintiff                               |
| Without legal basis    | No contract, statute, or other ground justifies retention |
| Quantification         | Amount of enrichment or loss, whichever is less           |

**Note**: Unjust enrichment is a recognized but judicially developed cause of
action in Icelandic law. Not codified in a single statute. [VERIFY]

### B. Tort Claims (Skaðabótaréttur)

**Statutory basis**: Skaðabótalög nr. 50/1993 (Damages Act) for personal
injury quantification; general tort principles are judge-made law.

#### B1. Fault-Based Liability (Saknæmi)

| Element                    | Description                                                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Duty (skyldubundin hegðun) | Defendant owed a standard of care [VERIFY]                                                                                |
| Fault (saknæmi)            | Defendant acted negligently or intentionally — measured against the "reasonable person" (bonus pater familias equivalent) |
| Causation (orsakatengsl)   | Adequate causation between fault and damage                                                                               |
| Damage (tjón)              | Compensable loss (economic or non-economic)                                                                               |
| No valid defence           | No contributory negligence (meðábyrgð) fully excusing liability                                                           |

**Key features:**

- General fault standard (saknæmi) encompasses both negligence and intentional wrongdoing
- Contributory negligence (meðábyrgð) reduces but does not necessarily eliminate damages [VERIFY]
- Free evaluation of evidence (frjáls sönnunarmat) — no fixed rules on evidence weight
- **No punitive damages** — only compensatory (including miskabætur for non-pecuniary loss)

#### B2. Strict Liability (Hlutlæg ábyrgð)

| Element         | Description                                                                                           |
| --------------- | ----------------------------------------------------------------------------------------------------- |
| Activity/source | Defendant engaged in activity subject to strict liability                                             |
| Statutory basis | Specific statute imposing strict liability (e.g., product liability, environmental, traffic) [VERIFY] |
| Causation       | Activity/product caused the damage                                                                    |
| Damage          | Compensable loss                                                                                      |

**Areas of strict liability in Iceland** (each governed by specific statute): [VERIFY]

- Product liability (afurðaábyrgð) — EEA-harmonised
- Traffic accidents — compulsory insurance
- Environmental damage
- Certain dangerous activities

#### B3. Non-Pecuniary Damages (Miskabætur)

| Element                   | Description                                                          |
| ------------------------- | -------------------------------------------------------------------- |
| Unlawful act              | Defendant's conduct was unlawful (ólögmæt)                           |
| Dignity / personal rights | Act infringed plaintiff's honour, freedom, or personal rights        |
| Severity                  | Infringement was sufficiently serious to warrant compensation        |
| Quantum                   | Court's discretion — no fixed tariff; assess by analogy to precedent |

**Note**: Miskabætur (Art. 26 of Act 50/1993 [VERIFY]) is a distinct head of
damages for non-economic harm to dignity and personal rights. It is separate
from compensatory damages for personal injury and has its own assessment
criteria.

### C. Employment Claims (Vinnuréttur)

#### C1. Wrongful Termination (Ólögmæt uppsögn)

| Element                 | Description                                                     |
| ----------------------- | --------------------------------------------------------------- |
| Employment relationship | Contract of employment existed                                  |
| Termination             | Employer terminated employment                                  |
| Grounds                 | Termination lacked legally sufficient grounds or proper process |
| Notice                  | Required notice period not observed (if applicable)             |
| Damage                  | Lost wages, benefits, non-pecuniary harm                        |

**Key features:**

- Notice periods governed by individual/collective agreements
- Strong protections against discriminatory termination [VERIFY]
- Félagsdómur (Labour Court) has exclusive jurisdiction over collective agreement disputes
- Individual employment disputes go to héraðsdómur

#### C2. Discrimination (Mismunun)

| Element                  | Description                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| Protected characteristic | Gender, age, disability, sexual orientation, religion, nationality, etc. |
| Adverse action           | Termination, demotion, pay disparity, harassment                         |
| Causal link              | Protected characteristic was a factor in the adverse action              |
| Damage                   | Economic loss and/or miskabætur                                          |

**Key legislation**: Lög um jafna stöðu og jafnan rétt kynjanna nr. 150/2020
(Gender Equality Act) [VERIFY]; general non-discrimination principles.

### D. Property Claims (Eignaréttur)

#### D1. Ownership Dispute (Eignardeilur)

| Element        | Description                                  |
| -------------- | -------------------------------------------- |
| Title or claim | Plaintiff claims ownership right             |
| Infringement   | Defendant interferes with ownership          |
| Registration   | Þinglýsing (land registry) status            |
| Remedy sought  | Declaration, recovery of possession, damages |

#### D2. Neighbour Disputes (Grenndarréttur)

| Element                 | Description                                         |
| ----------------------- | --------------------------------------------------- |
| Neighbouring properties | Parties own/occupy adjacent land                    |
| Nuisance/interference   | Defendant's use unreasonably interferes             |
| Harm                    | Demonstrable harm to plaintiff's enjoyment or value |

### E. Commercial Claims (Viðskiptaréttur)

#### E1. Company Law Disputes (Félagaréttur)

| Element                | Description                                                               |
| ---------------------- | ------------------------------------------------------------------------- |
| Corporate relationship | Shareholder, director, creditor of hf. (public) or ehf. (private) company |
| Breach of duty         | Violation of company law or articles of association                       |
| Damage                 | Loss to company, shareholder, or creditor                                 |

**Key legislation**: Lög um hlutafélög nr. 2/1995 (Public Companies Act);
lög um einkahlutafélög nr. 138/1994 (Private Limited Companies Act) [VERIFY]

#### E2. Competition Claims (Samkeppnisréttur)

| Element                  | Description                                                                               |
| ------------------------ | ----------------------------------------------------------------------------------------- |
| Anti-competitive conduct | Abuse of dominance, restrictive agreements                                                |
| Statutory basis          | Samkeppnislög nr. 44/2005 (Competition Act) — mirrors EU competition law via EEA [VERIFY] |
| Causation                | Conduct caused loss to plaintiff                                                          |
| Damage                   | Economic loss                                                                             |

#### E3. Consumer Claims (Neytendaréttur)

| Element              | Description                                             |
| -------------------- | ------------------------------------------------------- |
| Consumer transaction | B2C relationship                                        |
| Statutory protection | Applicable consumer protection statute (EEA-harmonised) |
| Breach               | Violation of consumer rights                            |
| Remedy               | Rescission, repair, replacement, damages                |

---

## Classification System

Classify the overall stefna quality using four tiers mapped to frávísun
(dismissal) risk:

### WELL-PLED (Vel rökstutt)

**Confidence threshold: ≥ 0.80**

All of the following:

- Every Art. 80 element present and complete
- Each cause of action has all elements factually supported
- Claims are specific (exact ISK amounts, precise declaratory relief)
- Limitation periods verified and not expired
- Kennitala and party identification complete
- Pre-litigation settlement documented (Art. 36 Codex Ethicus)
- Concise format (≤ 6 pages)
- No obvious frávísun grounds

### ADEQUATE (Fullnægjandi)

**Confidence threshold: ≥ 0.60**

All of the following:

- All mandatory Art. 80 elements present
- At least one cause of action has elements factually supported
- Claims stated with reasonable specificity
- No expired limitation periods on primary claims
- Minor gaps in party identification that can be cured
- Concise format maintained

Plus none of the following:

- Jurisdictional defect
- Res judicata or lis pendens issue
- Complete absence of factual basis for any pleaded claim

### VULNERABLE (Viðkvæmt)

**Confidence threshold: ≥ 0.80 (to classify as vulnerable, must be ≥ 0.80 confident it IS vulnerable)**

Any of the following:

- One or more Art. 80 elements materially incomplete
- Primary cause of action missing a required legal element
- Limitation period arguable (expired but tolling/suspension argument available)
- Factual basis thin for primary claim
- Kennitala missing for one or more parties (curable but delays filing)
- Settlement attempt not documented
- Stefna exceeds 8 pages (suggesting poor focus)

### DEFICIENT (Ófullnægjandi)

**Confidence threshold: ≥ 0.90**

Any of the following:

- Article 80 mandatory elements missing entirely
- No factual basis for any pleaded cause of action
- All claims clearly time-barred under Act 150/2007
- Jurisdictional defect that cannot be cured
- Res judicata — same matter already decided
- Filing would violate Art. 20 Codex Ethicus (false/misleading information)
- Fundamentally incoherent — claims contradict each other without alternative pleading basis

---

## Court Jurisdiction and Venue

### General Jurisdiction Rule

Under Act 91/1991, the general rule is that a defendant is sued at their
**domicile** (lögheimili). For legal entities, this is the registered office.

### 8 District Courts (Héraðsdómar)

| Court                          | Jurisdiction (approximate)           |
| ------------------------------ | ------------------------------------ |
| Héraðsdómur Reykjavíkur        | Reykjavík                            |
| Héraðsdómur Reykjaness         | Reykjanes peninsula (incl. Keflavík) |
| Héraðsdómur Vesturlands        | Western Iceland                      |
| Héraðsdómur Vestfjarða         | Westfjords                           |
| Héraðsdómur Norðurlands vestra | Northwest Iceland                    |
| Héraðsdómur Norðurlands eystra | Northeast Iceland (incl. Akureyri)   |
| Héraðsdómur Austurlands        | Eastern Iceland                      |
| Héraðsdómur Suðurlands         | Southern Iceland                     |

### Special Venue Rules [VERIFY]

| Claim type                 | Venue                                                    |
| -------------------------- | -------------------------------------------------------- |
| Real property (fasteignir) | Location of the property                                 |
| Maritime claims            | Port of the vessel                                       |
| Tort                       | Where the harmful event occurred OR defendant's domicile |
| Contract                   | Place of performance OR defendant's domicile             |
| Employment                 | Where work was performed OR employer's domicile          |
| Consumer                   | Consumer's domicile (protective jurisdiction)            |

### Cross-Border Jurisdiction (Lugano Convention)

When the defendant is domiciled in another Lugano Convention state (EU + Norway,
Switzerland, Iceland), jurisdiction is determined by the 2007 Lugano Convention:

| Rule                          | Basis                                                   |
| ----------------------------- | ------------------------------------------------------- |
| General                       | Defendant's domicile                                    |
| Contract (Art. 5(1))          | Place of performance                                    |
| Tort (Art. 5(3))              | Place of harmful event                                  |
| Consumer/employment/insurance | Special protective rules                                |
| Exclusive (Art. 22)           | Real property — situs; company validity — incorporation |
| Prorogation (Art. 23)         | Choice of court agreement                               |

**Post-Brexit note**: The UK is NOT a party to the Lugano Convention (application
rejected). For UK-connected disputes, common law principles and the Hague
Convention on Choice of Court Agreements (2005) may apply. [VERIFY]

---

## Filing Mechanics

### Court Fees (Þingfestingargjöld)

Under lög um aukatekjur ríkissjóðs nr. 88/1991, as of January 2023: [VERIFY current rates]

| Claim Amount (ISK)       | Filing Fee (ISK) | Approx. USD |
| ------------------------ | ---------------- | ----------- |
| Up to 3,000,000          | 20,000           | ~$145       |
| 3,000,000 – 30,000,000   | 42,000           | ~$305       |
| 30,000,000 – 90,000,000  | 122,000          | ~$885       |
| 90,000,000 – 150,000,000 | 202,000          | ~$1,465     |
| Over 150,000,000         | 337,000          | ~$2,445     |

**Fee-exempt cases**: Employment/wage disputes, civil rights cases, paternity,
custody/guardianship, child protection, certain adoption proceedings.

**Appeal fees**: Landsréttur filing fee is 70,000 ISK. [VERIFY]

### Service of Process (Birting stefnu)

| Method             | Description                                       | Usage                                   |
| ------------------ | ------------------------------------------------- | --------------------------------------- |
| Persónuleg birting | Personal service by stefnuvörður (process server) | Most common, preferred                  |
| Póstbirting        | Registered mail                                   | Available for known addresses           |
| Rafræn birting     | Electronic service                                | Expanding since 2023 amendments         |
| Opinber birting    | Public notification                               | Last resort — defendant evading service |

**International service**: Iceland ratified the Hague Service Convention
(in force 1 July 2009). Central Authority: Sýslumaður Suðurnesja.
**Iceland objected to Article 10(a)** — no service by direct postal channels.
Nordic Convention (1975) provides simplified service with Denmark, Finland,
Norway, Sweden.

### Language Requirements

- **All court documents must be in Icelandic**
- Foreign-language evidence requires **certified Icelandic translation**
- Translation must be certified by two certified translators (or equivalent)
- English and Nordic-language documents may be accepted by some administrative
  authorities but **courts require Icelandic translation**
- This skill outputs in English with Icelandic terminology — the filing
  lögmaður must prepare the final Icelandic-language stefna

### Foreign Parties

- Only a licensed Icelandic lögmaður may present oral argument before courts
- Foreign parties **must retain Icelandic counsel**
- EEA lawyers may provide temporary services under home title but must work
  **in conjunction with** a locally admitted lögmaður for court appearances
  (EU Lawyers' Services Directive 77/249/EEC via EEA)
- Power of attorney required for Icelandic counsel

### Electronic Filing

- Paper filing remains primary for stefnur at district court level
- Electronic portal: `vefgatt.domstolar.is` for procedural communications
- **July 2024 reform**: Mandatory digital submission for certain case types;
  Casedoc platform supports online document submission [VERIFY scope]
- Landsréttur and Hæstiréttur accept digital submissions through managed portal

---

## Remedies (Úrræði)

### Damages (Skaðabætur)

| Type                             | Description                                   | Basis                           |
| -------------------------------- | --------------------------------------------- | ------------------------------- |
| **Economic loss** (fjártjón)     | Lost profits, diminished value, out-of-pocket | General principles              |
| **Personal injury** (líkamstjón) | Statutory tables for bodily injury            | Skaðabótalög nr. 50/1993        |
| **Non-pecuniary** (miskabætur)   | Dignity, honour, personal rights              | Art. 26 of Act 50/1993 [VERIFY] |
| **Punitive**                     | **NOT AVAILABLE in Iceland**                  | N/A                             |

**Critical**: Iceland does not award punitive or exemplary damages. All
damages are compensatory. Do not include punitive damages in dómkröfur.

### Interest (Vextir)

Under vaxtalög nr. 38/2001 (Interest Act):

| Type                             | Rate                          | Application                           |
| -------------------------------- | ----------------------------- | ------------------------------------- |
| Default interest (dráttarvextir) | Central Bank base rate + 7%   | From date obligation was due [VERIFY] |
| Current approximate rate         | ~14.25% (as of research date) | Verify current Central Bank rate      |

**Always include** a dráttarvextir claim in dómkröfur, citing "III. kafli
vaxtalaga nr. 38/2001."

### Injunctions (Lögbann)

Under lög um lögbann og dómsmál til að vernda einkarétt nr. 31/1990:

- Pre-trial injunctions available through sýslumaður (district commissioner)
- Must demonstrate urgency and likelihood of right being infringed
- Separate application from main stefna [VERIFY procedure]

### Specific Performance

- Available in principle for contract claims
- Court has discretion; more commonly awards damages
- Consider whether specific performance is the appropriate remedy under
  Icelandic law for the specific obligation type [VERIFY]

---

## Costs and Legal Aid

### Costs (Málskostnaður)

Iceland follows a **modified loser-pays** system:

- The losing party is generally ordered to pay the winning party's legal costs
- **However**, courts rarely award full recovery — typical awards cover a
  portion of actual costs [VERIFY typical percentage]
- Court has broad discretion in setting costs amount
- Each party may be ordered to bear their own costs in some circumstances
- **Always include** a málskostnaður demand in dómkröfur

### Legal Aid (Gjafsókn)

Under Chapter 20 of lög nr. 91/1991:

- Available to individuals who cannot afford litigation
- Means-tested and merit-assessed
- Covers court fees, attorney fees, and other litigation costs
- Foreign nationals may be eligible regardless of nationality [VERIFY]
- Application to the Ministry of Justice

### Attorney Fees

- No mandatory fee scale — fees are negotiated
- Contingency fees (hagsmunatengd þóknun) are permitted in Iceland [VERIFY]
- Art. 10 Codex Ethicus: Fees must be "reasonable" based on complexity,
  stakes, and results
- Itemised invoices required

---

## Professional Conduct (Codex Ethicus)

Key ethical obligations when drafting and filing a stefna, drawn from the
Codex Ethicus of Lögmannafélag Íslands:

| Article | Duty                                        | Application to Stefna Drafting                                         |
| ------- | ------------------------------------------- | ---------------------------------------------------------------------- |
| Art. 1  | Uphold justice and conscience               | Ensure claims are well-founded                                         |
| Art. 3  | Independence                                | Draft based on law, not external pressure                              |
| Art. 8  | Competent representation; no discrimination | Deliver objective case assessment                                      |
| Art. 9  | Disclose conflicts of interest              | Check all parties for conflicts                                        |
| Art. 19 | Respect for courts                          | Draft truthful, focused pleadings                                      |
| Art. 20 | **No false information** to courts          | Every factual allegation must be supportable                           |
| Art. 22 | **Swift proceedings**                       | Concise drafting; no unnecessary complexity                            |
| Art. 34 | Respect opposing parties                    | No inflammatory or personal language                                   |
| Art. 36 | **Pre-litigation settlement**               | Must present claims and offer settlement BEFORE filing (unless urgent) |
| Art. 37 | Advise unrepresented opponents              | If opponent is unrepresented, advise them to seek counsel              |

### Tiered Court Licensing

| Court Level                   | License Required                                       |
| ----------------------------- | ------------------------------------------------------ |
| Héraðsdómur (District Court)  | Standard lögmaður license (Bar Exam + Master's degree) |
| Landsréttur (Court of Appeal) | Separate Landsréttur license                           |
| Hæstiréttur (Supreme Court)   | Separate Hæstiréttur license                           |

Verify that the filing lögmaður holds the appropriate license for the court
level where the stefna will be filed.

---

## Citation Quality Gates

Before including any legal authority in the stefna or analysis:

| Gate            | Check                                                                                      | Action if failed                      |
| --------------- | ------------------------------------------------------------------------------------------ | ------------------------------------- |
| **Source**      | Is the statute/case from a reliable Icelandic source (Althingi, Hæstiréttur, Landsréttur)? | Mark [VERIFY]                         |
| **Currency**    | Is the statute still in force? Has it been amended?                                        | Check althingi.is for current version |
| **Translation** | Is the English translation official (government.is) or unofficial?                         | Note translation status               |
| **Relevance**   | Does the authority actually support the proposition?                                       | Remove if inapposite                  |
| **Confidence**  | How confident are you in the citation?                                                     | Apply confidence scoring below        |

### Icelandic Citation Format

| Source          | Format                                                 |
| --------------- | ------------------------------------------------------ |
| Statute         | Lög nr. [number]/[year], [grein (article)]             |
| Supreme Court   | Hrd. [date], mál nr. [number]/[year]                   |
| Court of Appeal | Landsréttur [date], mál nr. [number]/[year]            |
| District Court  | Héraðsdómur [location] [date], mál nr. [number]/[year] |
| EFTA Court      | EFTA Court Case E-[number]/[year]                      |

---

## Self-Interrogation Protocol

For any finding classified as VULNERABLE or DEFICIENT, run three passes:

**Pass 1 — Element Check**: "Have I correctly identified all required elements
for this cause of action under Icelandic law? Am I applying the correct legal
standard (saknæmi for fault-based tort, Section 36 for contract fairness)?"

**Pass 2 — Fact Sufficiency**: "Do the stated facts, taken as true, satisfy
each element? Remember: Iceland has no plausibility standard — the threshold
is lower than US or E&W. Would a héraðsdómur judge find a cognizable claim
stated?"

**Pass 3 — Procedural Compliance**: "Does this stefna comply with Art. 80?
Is it concise? Are all parties identified with kennitala? Are claims specific
enough? Would this survive frávísun?"

If all three passes confirm the classification, retain it. If any pass
suggests reclassification, adjust and document the reasoning.

---

## Confidence Scoring

| Level           | Threshold | Meaning                                                               |
| --------------- | --------- | --------------------------------------------------------------------- |
| **Definite**    | ≥ 0.95    | Based on express statutory text or settled Hæstiréttur precedent      |
| **Very likely** | 0.80–0.94 | Supported by clear authority; minor uncertainty                       |
| **Likely**      | 0.60–0.79 | Reasonable basis but authority is indirect, analogical, or translated |
| **Possible**    | 0.40–0.59 | Plausible argument but limited authority; novel or untested           |
| **Unlikely**    | < 0.40    | Weak basis; contrary authority exists or claim is speculative         |

For each cause of action and each significant finding, assign a confidence
level. Flag anything below "Likely" for specific attorney review.

---

## Sub-Agent Architecture

For complex matters involving multiple causes of action, cross-border
elements, or large document corpora, use the Task tool to spawn parallel
analysis agents:

| Agent                     | Task                                      | Tool Access         |
| ------------------------- | ----------------------------------------- | ------------------- |
| **element-mapper**        | Map facts to cause of action elements     | Read, Grep, Glob    |
| **limitation-checker**    | Verify all limitation periods             | WebSearch, Read     |
| **jurisdiction-analyzer** | Assess venue and Lugano Convention issues | WebSearch, Read     |
| **authority-researcher**  | Find and verify Icelandic legal authority | WebSearch, WebFetch |

Merge agent outputs, resolve conflicts, and produce unified classification.

---

## Anti-Patterns

The following are explicit errors to avoid when drafting an Icelandic stefna:

1. **Do NOT draft a long stefna** — 5-6 pages is the standard. Exceeding 8 pages signals poor advocacy. This is not a US complaint or E&W Particulars of Claim.
2. **Do NOT include detailed legal argument** — the stefna states facts and references law; detailed argumentation is for oral proceedings (munnlegur málflutningur).
3. **Do NOT claim punitive damages** — they do not exist in Icelandic law. Every damages claim must be compensatory.
4. **Do NOT omit kennitala** — it is a mandatory identifier for all parties in Icelandic court documents.
5. **Do NOT reference "discovery" or "disclosure"** — Iceland has no discovery procedure. All evidence must be identified and available at filing.
6. **Do NOT propose party-appointed experts** — Icelandic courts use court-appointed experts (dómkvaddir matsmenn) only.
7. **Do NOT apply Twombly/Iqbal or any plausibility standard** — Iceland has no equivalent. The threshold for stating a claim is functional, not plausibility-based.
8. **Do NOT skip the pre-litigation settlement check** — Art. 36 Codex Ethicus requires settlement attempt before filing (unless urgent).
9. **Do NOT file without checking the filing lögmaður's court license** — separate licenses are required for héraðsdómur, Landsréttur, and Hæstiréttur.
10. **Do NOT use inflammatory or personal language** — Art. 34 Codex Ethicus requires respect for opposing parties.
11. **Do NOT omit the málskostnaður (costs) demand** — always include it in dómkröfur.
12. **Do NOT omit the dráttarvextir (interest) demand** — always claim default interest from the appropriate date under vaxtalög nr. 38/2001.
13. **Do NOT assume the same limitation period for all claims** — check each cause of action against Act 150/2007 specifically.
14. **Do NOT serve by direct post to a party outside Iceland** — Iceland objected to Hague Convention Art. 10(a). International service must go through the Central Authority.
15. **Do NOT draft in English for filing** — the stefna must be filed in Icelandic. This skill outputs in English with Icelandic terminology for the attorney to translate.
16. **Do NOT treat oral proceedings as secondary** — in Iceland, the oral argument is the primary case presentation. The stefna frames the dispute; it does not present the full case.
17. **Do NOT include evidence evaluation in the stefna** — state what evidence exists; do not evaluate its weight or credibility.
18. **Do NOT reference pre-action protocols** — Iceland has no mandatory pre-action protocol system (unlike England & Wales).
19. **Do NOT overlook Section 36** — the Nordic general fairness clause is a powerful and frequently invoked tool that has no direct equivalent in common law jurisdictions.
20. **Do NOT assume foreign judgments are automatically enforceable** — enforcement requires a formal declaration of enforceability (exequatur) under the Lugano Convention or domestic recognition procedures.

---

## Writing Standards

All skill outputs follow these standards:

1. **Active voice** — "The defendant breached the contract" not "The contract was breached by the defendant"
2. **Icelandic legal terms with English** — "saknæmi (fault)" not just "fault"
3. **Statutory citation** — Every legal proposition cites a specific provision: "Section 36 of Act 7/1936" not "Icelandic fairness doctrine"
4. **Section references** — Findings cite the stefna section where the issue appears
5. **Conciseness** — Match the Icelandic norm. If the stefna itself should be 5-6 pages, the analysis should not be disproportionately long
6. **No hedging without substance** — "This element may be weak because [specific reason]" not "This element could potentially perhaps be insufficient"
7. **Bilingual key terms** — First use includes Icelandic term; subsequent uses may use English only if context is clear
8. **[VERIFY] markers** — Every proposition sourced from translation, secondary source, or AI knowledge rather than verified primary Icelandic statute gets a [VERIFY] marker

---

## Output Format Template

### Executive Summary

```
ICELANDIC STEFNA ANALYSIS
═══════════════════════════════════════

Overall Classification: [WELL-PLED / ADEQUATE / VULNERABLE / DEFICIENT]
Confidence: [score]
Primary Cause(s) of Action: [list]
Héraðsdómur: [court name]
Filing Fee: [amount] ISK
Limitation Status: [CLEAR / ARGUABLE / EXPIRED]
Pre-litigation Settlement: [DOCUMENTED / NOT DOCUMENTED / URGENCY EXCEPTION]

Key Strengths:
• [strength 1]
• [strength 2]

Key Vulnerabilities:
• [vulnerability 1 — with section reference]
• [vulnerability 2 — with section reference]

Immediate Actions Required:
1. [action 1]
2. [action 2]
```

### Cause of Action Assessment

For each cause of action:

```
CAUSE OF ACTION: [Icelandic name (English)]
Statutory Basis: [Act/Section]
Classification: [WELL-PLED / ADEQUATE / VULNERABLE / DEFICIENT]
Confidence: [score]
Limitation Period: [period] — Expires: [date] — Status: [CLEAR/ARGUABLE/EXPIRED]

Element Map:
┌─────────────────────┬────────────┬─────────────────────┬────────────┐
│ Element             │ Status     │ Supporting Facts    │ Confidence │
├─────────────────────┼────────────┼─────────────────────┼────────────┤
│ [element 1]         │ ✅ / ⚠️ / ❌│ [fact reference]    │ [score]    │
│ [element 2]         │ ✅ / ⚠️ / ❌│ [fact reference]    │ [score]    │
└─────────────────────┴────────────┴─────────────────────┴────────────┘

Frávísun Risk: [LOW / MEDIUM / HIGH]
Recommendation: [PLEAD / PLEAD WITH CAUTION / DO NOT PLEAD]
```

### Stefna Draft

Full draft in English with Icelandic terminology per the Stefna Structure
Template above.

### Filing Checklist

```
PRE-FILING CHECKLIST
────────────────────
□ Art. 80 compliance verified (all mandatory elements)
□ Kennitala obtained for all parties
□ Court fees calculated: [amount] ISK
□ Correct héraðsdómur identified
□ Limitation periods verified (Act 150/2007)
□ Pre-litigation settlement attempted (Art. 36 Codex Ethicus)
□ Filing lögmaður holds correct court license
□ Service method determined: [method]
□ Foreign-language documents translated to Icelandic
□ Evidence list complete (sönnunargögn)
□ Dráttarvextir calculated from correct date
□ Málskostnaður demand included
□ [If cross-border] Lugano Convention jurisdiction verified
□ [If cross-border] Hague Service Convention requirements met
□ Stefna translated to Icelandic by qualified translator
```

---

## Glass Box Audit Trail

Every analysis produces a Glass Box trail documenting the reasoning chain:

```yaml
glass_box:
  matter: "[matter description]"
  date: "[analysis date]"
  analyst: "legalcode-complaint-drafter-is"
  jurisdiction: "Iceland"
  governing_law: "Lög um meðferð einkamála nr. 91/1991"

  classification:
    overall: "[WELL-PLED / ADEQUATE / VULNERABLE / DEFICIENT]"
    confidence: [0.00-1.00]
    primary_basis: "[explanation of classification]"
    frávísun_risk: "[LOW / MEDIUM / HIGH]"

  causes_of_action:
    - name: "[Icelandic name (English)]"
      statutory_basis: "[Act/Section]"
      classification: "[tier]"
      confidence: [0.00-1.00]
      elements_satisfied: [count]
      elements_total: [count]
      limitation_status: "[CLEAR / ARGUABLE / EXPIRED]"
      limitation_expires: "[date or N/A]"

  procedural_compliance:
    article_80_complete: [true/false]
    kennitala_all_parties: [true/false]
    claims_specific: [true/false]
    settlement_attempted: [true/false]
    correct_court: [true/false]
    within_page_limit: [true/false]
    filing_fee_calculated: "[amount] ISK"

  cross_border:
    applicable: [true/false]
    framework: "[Lugano / Hague / Nordic Convention / N/A]"
    jurisdiction_basis: "[article/rule]"

  verify_markers: [count]
  self_interrogation_runs: [count]

  assumptions:
    - "[assumption 1 — with basis]"
    - "[assumption 2 — with basis]"

  limitations_of_analysis:
    - "[limitation 1]"
    - "[limitation 2]"
```

---

## Alternative Dispute Resolution (ADR)

Consider whether ADR is appropriate before filing a stefna. Iceland offers
several ADR mechanisms:

### Mediation (Sáttameðferð)

| Mechanism                           | Details                                                                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **District Commissioner mediation** | Free mediation service offered by sýslumenn (district commissioners). Available for civil disputes before or during litigation. No charge. [VERIFY current availability] |
| **Court-referred mediation**        | Héraðsdómur may suggest mediation at any stage of proceedings [VERIFY]                                                                                                   |
| **Private mediation**               | Available through private mediators; not regulated by specific mediation statute [VERIFY]                                                                                |

**Art. 36 Codex Ethicus connection**: The pre-litigation settlement obligation
aligns with Iceland's general encouragement of consensual dispute resolution.
A genuine mediation attempt strengthens compliance with Art. 36.

### Arbitration (Gerðardómur)

| Framework                           | Details                                                                                                      |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Lög nr. 53/1989**                 | Act on Contractual Arbitration — governs domestic arbitration [VERIFY]                                       |
| **Lög nr. 25/1999**                 | Based on UNCITRAL Model Law — governs international commercial arbitration [VERIFY]                          |
| **Nordic Arbitration Centre (NAC)** | Operated by Iceland Chamber of Commerce; rules provide 6-month timeframe for award; confidential proceedings |
| **New York Convention**             | Iceland is a signatory — Icelandic arbitral awards enforceable in 159 countries                              |

**When arbitration precludes filing**: If a valid arbitration clause exists
in the underlying contract, the héraðsdómur must decline jurisdiction in
favour of arbitration. Check all relevant contracts for arbitration clauses
before drafting a stefna.

### Consumer Dispute Bodies

| Body                            | Jurisdiction                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------- |
| Neytendastofa (Consumer Agency) | Consumer protection complaints                                                    |
| Úrskurðarnefnd (various boards) | Sector-specific dispute resolution (telecommunications, insurance, etc.) [VERIFY] |

---

## Appeal Procedures

### Appeal to Landsréttur (Áfrýjun til Landsréttar)

| Aspect                      | Detail                                                                                                                      |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Deadline**                | 4 weeks from pronouncement of héraðsdómur judgment                                                                          |
| **Late appeal** (4-8 weeks) | Must apply for leave; court considers public value, important interests, or whether judgment may noticeably change [VERIFY] |
| **Fee**                     | 70,000 ISK [VERIFY current rate]                                                                                            |
| **Panel**                   | 3 judges                                                                                                                    |
| **Scope**                   | Full review of law and fact                                                                                                 |
| **New evidence**            | Generally restricted; court may permit in exceptional circumstances [VERIFY]                                                |

### Appeal to Hæstiréttur (Áfrýjun til Hæstaréttar)

| Aspect                | Detail                                                                                                               |
| --------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Leave required**    | Yes — must apply for leave to appeal                                                                                 |
| **Grounds for leave** | Likely precedent value, important interests, grossly inadequate process, or manifestly incorrect conclusion [VERIFY] |
| **Applications**      | ~150-200 per year; ~50-60 cases decided                                                                              |
| **Panel**             | Varies (typically 5 or 7 judges)                                                                                     |
| **Scope**             | Primarily legal review; fact-finding largely settled at lower levels                                                 |

### Strategic Implications for Stefna Drafting

- A well-drafted stefna creates a clear factual record that survives appeal
- Because oral argument is primary, the stefna's factual narrative must be
  precise enough to anchor the oral presentation
- Errors in the stefna's factual framework are difficult to cure on appeal
  since new evidence is restricted
- Consider the appeal pathway when selecting causes of action — novel
  theories may benefit from Hæstiréttur's precedent-setting role

---

## Default Judgment (Útivistardómur)

If the defendant fails to appear or respond after proper service:

### Requirements for Default Judgment [VERIFY]

1. **Valid service** — stefna was properly served (birting) on the defendant
2. **Defendant's failure** — defendant did not file greinargerð (statement of
   defence) within the prescribed period, or failed to appear at the
   scheduled hearing
3. **Plaintiff's claims sustainable** — the court must be satisfied that the
   claims as stated in the stefna have a sufficient basis

### Procedure

- Plaintiff applies for útivistardómur (default judgment)
- Court reviews the stefna to verify Art. 80 compliance and that claims
  are sustainable on their face
- If satisfied, court enters judgment in favour of plaintiff
- Default judgment is enforceable through sýslumaður (district commissioner)

### Strategic Note

Because the court reviews the stefna independently when entering default
judgment, the quality of the stefna directly determines whether default
judgment will be granted. A stefna that is vague, incomplete, or fails
Art. 80 requirements may be denied even when the defendant has not appeared.

---

## Group Litigation (Hópmálsókn)

Under Article 19a of lög nr. 91/1991 (added by amendment): [VERIFY]

### Requirements

| Element               | Requirement                                                  |
| --------------------- | ------------------------------------------------------------ |
| **Minimum claimants** | 3 or more plaintiffs                                         |
| **Common issues**     | Claims must arise from same or similar circumstances         |
| **Model**             | Opt-in (not opt-out — each claimant must affirmatively join) |
| **Representative**    | One lead plaintiff or attorney may represent the group       |
| **Court approval**    | Héraðsdómur must approve the group litigation format         |

### Comparison with Other Jurisdictions

| Feature        | Iceland (Art. 19a)         | US (Rule 23)                 | E&W (GLO)             |
| -------------- | -------------------------- | ---------------------------- | --------------------- |
| Model          | Opt-in                     | Opt-out (Rule 23(b)(3))      | Opt-in (GLO register) |
| Minimum        | 3 claimants                | Numerosity (typically 40+)   | No fixed minimum      |
| Court approval | Required                   | Required (certification)     | Required              |
| Common issues  | Same/similar circumstances | Common questions predominate | Common/related issues |
| Prevalence     | Rare                       | Common                       | Moderate              |

### Drafting Considerations

- Include a section in the stefna identifying all group members (names,
  kennitala, addresses)
- Clearly articulate the common factual and legal issues
- Explain why group litigation is appropriate and efficient
- Each claimant's individual damages must be separately quantifiable
- Class actions are rare in Iceland — verify that the court will accept the
  group format before filing

---

## Enforcement of Judgments (Fullnusta dóma)

### Domestic Enforcement

| Step                | Detail                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------- |
| **Judgment debtor** | Has 4 weeks from judgment to comply voluntarily [VERIFY]                                          |
| **Application**     | Creditor applies to sýslumaður (district commissioner) for enforcement                            |
| **Methods**         | Bank attachment (fjárnám í bankareikningi), property seizure (fjárnám í eignum), wage garnishment |
| **Fee**             | 20,000 ISK enforcement request fee [VERIFY]                                                       |

### Foreign Judgment Enforcement

| Framework              | Scope                                                                                        |
| ---------------------- | -------------------------------------------------------------------------------------------- |
| **Lugano Convention**  | EU + Iceland, Norway, Switzerland — simplified exequatur procedure                           |
| **Nordic Convention**  | Denmark, Finland, Norway, Sweden — even simpler mutual recognition                           |
| **Bilateral treaties** | Limited; check for specific country                                                          |
| **No treaty**          | Domestic recognition action required; court reviews public policy, due process, jurisdiction |

### Timeline (Approximate)

| Route                            | Duration              |
| -------------------------------- | --------------------- |
| Lugano Convention enforcement    | 2-6 months [VERIFY]   |
| Contested recognition            | 4-8 months [VERIFY]   |
| Domestic recognition (no treaty) | 6-12+ months [VERIFY] |
| Execution (bank attachment)      | Weeks                 |
| Execution (property seizure)     | Months                |

---

## Icelandic Legal System — Key Differences from Common Law

This section summarizes fundamental differences that affect every aspect of
stefna drafting. These are not merely procedural variations — they reflect a
different legal tradition.

| Aspect                 | Common Law (US/E&W)                          | Iceland                                                         | Impact on Stefna                                 |
| ---------------------- | -------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------ |
| Legal tradition        | Common law / equity                          | Nordic civil law (no comprehensive code)                        | Different cause of action structure              |
| Written pleading role  | Primary case presentation                    | **Frames the dispute** — oral argument is primary               | Keep stefna concise; don't over-argue            |
| Plausibility standard  | Twombly/Iqbal (US), reasonable grounds (E&W) | **No plausibility standard**                                    | Lower dismissal threshold                        |
| Discovery/disclosure   | Extensive (US), structured (E&W)             | **None**                                                        | All evidence at filing; no discovery requests    |
| Expert witnesses       | Party-appointed                              | **Court-appointed only** (dómkvaddir matsmenn)                  | Don't propose party experts                      |
| Jury                   | Available (US), limited (E&W)                | **No civil jury**                                               | All matters decided by judge(s)                  |
| Evidence evaluation    | Rules of evidence                            | **Free evaluation** (frjáls sönnunarmat)                        | No fixed evidence rules to comply with           |
| Punitive damages       | Available (US), limited (E&W)                | **Not available**                                               | Never claim punitive damages                     |
| Contract consideration | Required (common law)                        | **Not required** (Nordic contract law)                          | Different formation analysis                     |
| General fairness       | Unconscionability (limited)                  | **Section 36** — broad judicial power to set aside unfair terms | Powerful tool for contract claims                |
| Costs                  | American rule (US), loser-pays (E&W)         | **Modified loser-pays** (partial recovery)                      | Include costs demand; manage client expectations |
| Pre-action protocol    | None (US), mandatory (E&W)                   | **None** (but Art. 36 settlement attempt)                       | No protocol compliance section needed            |
| Document language      | English                                      | **Icelandic only**                                              | Translation required for all filings             |

---

## Common Weaknesses by Claim Type

### Contract Claims (Samningaréttur)

- Failing to consider Section 36 fairness clause as both sword and shield
- Omitting specific contract provisions breached (cite exact clauses)
- Not addressing implied terms under Nordic contract principles
- Ignoring the effect of general principles (meðalhófsreglan, grandvísi)

### Tort Claims (Skaðabótaréttur)

- Claiming punitive damages (not available)
- Applying common law "duty of care" framework instead of Icelandic saknæmi standard
- Confusing miskabætur (non-pecuniary/dignity) with general pain-and-suffering damages
- Failing to identify whether strict liability (hlutlæg ábyrgð) applies under specific statute

### Employment Claims (Vinnuréttur)

- Filing in héraðsdómur when Félagsdómur has exclusive jurisdiction (collective agreement disputes)
- Not verifying collective agreement terms (often govern notice periods and termination grounds)
- Overlooking mandatory equality legislation (Act 150/2020)

### Property Claims (Eignaréttur)

- Not checking þinglýsing (land registry) for encumbrances and title history
- Filing in wrong venue (real property must be in the district where property is located)

### Commercial Claims (Viðskiptaréttur)

- Not considering EEA-harmonised rules (competition, consumer, product liability)
- Applying domestic law when EEA law provides the correct framework
- Overlooking EFTA Court advisory opinions on relevant EEA provisions

---

## Conciseness Quick-Reference (Stefna Drafting Checklist)

### Phase 1: Pre-Drafting

- [ ] All client facts collected and organised chronologically
- [ ] Causes of action identified and elements mapped
- [ ] Kennitala obtained for all parties
- [ ] Limitation periods verified (Act 150/2007)
- [ ] Settlement attempt made or urgency documented (Art. 36)
- [ ] Correct héraðsdómur identified (defendant's domicile)

### Phase 2: Drafting

- [ ] Party identification complete (names, kennitala, addresses)
- [ ] Dómkröfur specific (exact ISK amounts, precise relief)
- [ ] Dráttarvextir claimed with correct date and statutory reference
- [ ] Málskostnaður demanded
- [ ] Málavextir concise — material facts only, no argument
- [ ] Lagarök brief — main statutory/principle references only
- [ ] Sönnunargögn listed — documents and witnesses identified
- [ ] Total length ≤ 6 pages

### Phase 3: Pre-Filing

- [ ] Art. 80 compliance self-check completed
- [ ] Frávísun risk assessed
- [ ] Filing fee calculated and ready
- [ ] Service method determined
- [ ] Filing lögmaður license verified for court level
- [ ] Translation to Icelandic arranged (if drafted in English)
- [ ] Certified translations of foreign-language evidence prepared

### Phase 4: Filing

- [ ] Stefna served on defendant (birting)
- [ ] Proof of service filed with court
- [ ] Filing fee paid
- [ ] Case number received

---

## Localization Notes

This skill is specific to Iceland. The following aspects are
jurisdiction-locked and should NOT be adapted for other jurisdictions:

- Article 80 requirements (unique to lög nr. 91/1991)
- Kennitala identification system
- Codex Ethicus obligations (Lögmannafélag Íslands)
- Court fee schedule (lög nr. 88/1991)
- Nordic contract law principles (Act 7/1936 uniform legislation)
- Section 36 general fairness clause
- Saknæmi fault standard
- Miskabætur non-pecuniary damages regime
- Three-tier court system (post-2018)
- Icelandic-language filing requirement
- Oral-argument-centric procedure

For US proceedings, use `legalcode-complaint-drafter`.
For England & Wales proceedings, use `legalcode-complaint-drafter-ew`.

---

## Provenance

**Skill**: legalcode-complaint-drafter-is
**Created**: 2026-03-01
**Method**: 4-agent deep research pipeline (civil-procedure, substantive-law,
remedies-costs, legal-resources) with Opus-grade agents conducting parallel
web research in English and Icelandic. Research covered: lög um meðferð
einkamála nr. 91/1991, Nordic contract law tradition, Icelandic court structure
(post-2018 three-tier system), Codex Ethicus, EEA/Lugano framework, filing
mechanics, and practical requirements.

**Key research sources:**

- Government of Iceland — English translation of Act 91/1991 (government.is)
- Althingi — Legislative texts (althingi.is)
- Lögmannafélag Íslands — Codex Ethicus, licensing requirements (lmfi.is)
- Héraðsdómur Reykjavíkur — Court fee schedule (heradsdomstolar.is)
- NYU GlobaLex — "Researching Icelandic Law" guide
- EUR-Lex — Lugano Convention summary
- Island.is — Civil suits overview, service of process, court structure
- EFTA Court — Advisory opinion procedures (eftacourt.int)
- Library of Congress — Guide to Law Online: Iceland

**Research artifacts**: Agent team `iceland-civil-procedure-research` outputs
(4 agents, ~280k tokens total research).

**Companion skills**: legalcode-complaint-drafter (US), legalcode-complaint-drafter-ew (E&W)
