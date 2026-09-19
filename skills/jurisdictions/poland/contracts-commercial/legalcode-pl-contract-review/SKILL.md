---
name: legalcode-pl-contract-review
description: Review commercial contracts under Polish law (Kodeks cywilny / Civil Code) — flag deviations,
  generate confidence-scored redlines with Polish-law citations, and produce an auditable analysis with
  business impact assessment. Use when reviewing vendor contracts, customer agreements, SaaS agreements,
  professional services contracts, licences, partnership agreements, procurement contracts, or any commercial
  agreement governed by Polish law requiring clause-by-clause analysis against standard positions or market
  practice. Covers KC mandatory rules (Art. 353¹, 58, 473, 483-485), kara umowna analysis, abusive clause
  register (UOKiK), fields of exploitation (pola eksploatacji), RODO/GDPR data processing addendum requirements,
  UZNK trade-secret protection, limitation periods (przedawnienie), and dispute resolution in Polish courts
  and arbitration (SA KIG, Lewiatan). Consolidates IURA methodology with Legalcode gold-standard quality
  frameworks.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Polish Contract Review (Przegląd Umów / Kodeks Cywilny)

> **Disclaimer**: This skill provides a framework for AI-assisted contract review under Polish
> law. It does not constitute legal advice. All outputs must be reviewed by a qualified legal
> professional (radca prawny / adwokat) licensed in Poland before any reliance. Laws change —
> verify current statutory text against Legalis, LEX, or the official Dziennik Ustaw before
> relying on any provision cited here. Statutory and case-law references cited from memory
> carry hallucination risk — verify against authoritative Polish legal databases before use.

---

## Purpose and Scope

This skill reviews existing contracts against an organisation's negotiation playbook or
general market standards under **Polish law (prawo polskie)**, identifying deviations from
the Civil Code (Kodeks cywilny, KC), mandatory consumer-protection rules, copyright
formalities, and GDPR/RODO requirements. It consolidates the IURA contract-review
methodology with Legalcode quality frameworks (Citation Quality Gates, Self-Interrogation,
Confidence Scoring, Glass Box audit trail).

**Covers:**

- Clause-by-clause analysis of any commercial agreement governed by Polish law
- Polish Civil Code (KC) mandatory provisions that override contractual freedom (ius cogens)
- Abusive clause screening (klauzule abuzywne — Art. 385¹ KC) for B2C and qualifying B2B
- Kara umowna (penalty clause) validity and enforceability analysis (Art. 483-485 KC)
- IP / copyright assignment formalities under Polish copyright law (pola eksploatacji)
- RODO/GDPR data processing addendum (UPP) compliance check
- Trade-secret protection (tajemnica przedsiębiorstwa) under UZNK
- Standard terms incorporation (wzorzec umowny — Art. 384-385 KC)
- Limitation-period (przedawnienie) analysis and contractual interaction
- Deviation classification (ZIELONY / ŻÓŁTY / CZERWONY)
- Redline generation with fallback positions and Polish-law rationale
- Missing clause detection with materiality assessment
- Glass Box audit trail with confidence scoring

**Does not:**

- Draft new contracts from scratch (see drafting-specific skills)
- Provide legal advice or replace qualified Polish counsel
- Cover employment contracts in full (see employment-specific skills)
- Address real estate transactions (notarial-deed requirements are out of scope)

---

## Jurisdiction and Governing Law

This skill is designed specifically for contracts governed by **Polish law** (prawo polskie).
The primary legal framework is:

- **Kodeks cywilny (KC)** — Ustawa z dnia 23 kwietnia 1964 r. [VERIFY currency]
- **Ustawa o prawie autorskim i prawach pokrewnych z dnia 4 lutego 1994 r.** (copyright)
- **Ustawa z dnia 16 kwietnia 1993 r. o zwalczaniu nieuczciwej konkurencji (UZNK)**
- **RODO** — Rozporządzenie (UE) 2016/679 (GDPR), implemented in Poland via:
  - **Ustawa z dnia 10 maja 2018 r. o ochronie danych osobowych**
  - Supervisory authority: **UODO** (Urząd Ochrony Danych Osobowych)
- **Rome I Regulation** (EC/593/2008) — for international contracts with choice-of-law issues

**Important civil-law distinctions** that differ from common-law jurisdictions:

- No work-for-hire doctrine (work-made-for-hire). Use Art. 12 or contractual assignment.
- Kara umowna (Art. 483 KC) applies only to non-monetary obligations — no direct common-law parallel.
- No jury trials or US-style class actions. Judicial reduction (miarkowanie) of penalties is mandatory (Art. 484 § 2 KC) and cannot be contractually excluded.
- Contractual limitation periods are non-modifiable (Art. 119 KC) — statutory periods apply regardless of what the contract says.
- Moral rights (autorskie prawa osobiste) are inalienable — they cannot be transferred, only the exercise can be contractually restricted.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer changes the direction of the analysis
- Multiple valid approaches exist
- Ambiguity in the contract creates a fork only the user can resolve
- Risk tolerance or business context is needed to classify severity correctly

Wherever marked **⟁ CLARIFY** below, present the user with structured options and
descriptions. Skip the question if the information has already been provided.

---

## Workflow

### Step 1: Accept the Contract

Accept the contract in any of these formats:

- **File**: PDF, DOCX, or other document format
- **URL**: Link to a contract in a CLM, cloud storage, or document system
- **Pasted text**: Contract text pasted directly into the conversation

If no contract is provided, prompt the user to supply one.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask these questions (skip those already answered):

1. **Which side are you on?**
   - Options: Vendor/Dostawca, Customer/Zamawiający, Licensor/Licencjodawca,
     Licensee/Licencjobiorca, Partner, Employer/Pracodawca, Employee/Pracownik, Other
   - _Why this matters_: The entire analysis flips depending on representation. A liability
     cap protects different parties depending on who drafted the contract.

2. **Contract type** (if not clear from the document):
   - Options: SaaS / software service, Professional services / usługi, Supply of goods /
     dostawa, Licence / licencja, Distribution / dystrybucja, Joint venture, Other
   - _Why this matters_: Determines which KC provisions (named contracts — umowy nazwane vs.
     unnamed — umowy nienazwane under Art. 353¹ KC) are most likely to apply.

3. **B2B or B2C?**
   - Options: Purely B2B (both parties are entrepreneurs), B2C (one party is a consumer),
     Mixed / unclear
   - _Why this matters_: B2C contracts trigger mandatory abusive-clause protections
     (Art. 385¹-385³ KC) that cannot be waived. Since January 1, 2021, certain B2B
     standard-form contracts also attract abusive-clause scrutiny.

4. **Deadline**:
   - Options: Urgent (hours/days), Standard (1-2 weeks), Flexible
   - _Why this matters_: Affects how many issues to surface vs. focus only on critical ones.

5. **Focus areas** (multi-select):
   - Kara umowna (penalty clauses), IP / copyright formalities, Data protection / RODO,
     Liability limitation, Termination flexibility, Governing law / jurisdiction, Payment terms,
     No specific focus — full review

6. **Deal context** (free text): deal size, strategic importance, existing relationship,
   template or one-off negotiation.

If the user provides partial context, proceed with what you have but **state assumptions
explicitly** (e.g., "I'm assuming B2B — tell me if a consumer party is involved and I'll
re-run the abusive-clause analysis").

### Step 3: Load the Playbook

Check for the organisation's contract review playbook in local configuration files
(e.g., `legal.local.md`, `playbook.md`, or similar).

The playbook should define:

- **Standard positions**: Preferred terms for each major clause type
- **Acceptable ranges**: Terms that can be agreed without escalation
- **Escalation triggers**: Terms requiring senior counsel or decision-maker sign-off

**If no playbook is configured:**

**⟁ CLARIFY** — Inform the user and ask which approach to take:

- **Option A: Set up a playbook now** — Walk through defining standard positions for key
  clauses (liability cap, kara umowna tolerance, IP ownership, data protection minimums,
  termination preferences). Takes time upfront; makes all future reviews more precise.
- **Option B: Proceed with general market standards** — Use Polish market standards and
  KC ius cogens provisions as the baseline. Faster, but may not reflect the organisation's
  specific risk appetite.
- **Option C: I'll provide positions as we go** — Start the review and ask about preferred
  positions when needed for each clause.

If proceeding without a playbook, label the review: "Based on Polish market standards and
KC mandatory provisions — not organisational positions."

### Step 4: Gather Polish-Law Legal Authority

Read the contract's governing law clause. Confirm it selects Polish law (or identify the
effective law under Rome I if there is no express choice). Then use **legalcode-mcp** to
build a working legal reference file.

**Research process:**

1. **Identify the governing law** from the contract.

   **⟁ CLARIFY** — If any of the following are true, ask the user before proceeding:
   - **No governing law clause found**: Flag as RED. Ask which jurisdiction the user expects
     to apply.
   - **Foreign governing law** despite both parties being Polish entities: Confirm the user
     is aware. Analyse under the stated law but flag the commercial and practical risks.
   - **Multiple conflicting governing law clauses**: Ask which governs the main body and
     note the conflict as RED.

2. **Search legalcode-mcp** (if connected) for Polish-law authority across:
   - Art. 473 KC — limits on excluding liability (especially § 2: wina umyślna rule)
   - Art. 483-485 KC — kara umowna requirements, miarkowanie doctrine, key SN decisions
   - Art. 385¹-385³ KC — abusive clause criteria, UOKiK register decisions
   - Copyright Act Art. 41, 12, 74 — pola eksploatacji, employee works, computer programs
   - Art. 361-363 KC — scope of damages (damnum emergens / lucrum cessans)
   - Art. 365¹ KC — termination of indefinite obligations
   - UZNK Art. 11 — tajemnica przedsiębiorstwa (trade-secret definition and protection)
   - Art. 119, 118 KC — non-modifiability of limitation periods; general 6-year and specific periods
   - RODO Art. 28 — data processing agreement (UPP) requirements
   - Sąd Najwyższy (SN) decisions on limitation of liability, kara umowna enforceability

3. **Save the most relevant results** to `/tmp/legalcode-pl-contract-authority.md`:

   ```markdown
   # Polish Law Authority Reference — [Contract Name]

   ## Governing Law: Polish law (prawo polskie)

   ## Date Gathered: [date]

   ### KC Statutes

   - [Article, key text, relevance]

   ### Case Law (Sąd Najwyższy)

   - [Case reference, key holding]

   ### UOKiK/UODO Decisions

   - [Decision, relevance]
   ```

4. Use this reference file throughout the analysis. Mark citations sourced from
   legalcode-mcp as VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**

- Mark all KC citations and SN case references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — citations require verification"`
- If IURA MCP is connected, use tools `Search_DU`, `Search_SN`, `Search_SP` to verify
  statutory texts and case-law signatures. IURA provides the Polish legal database search.

### Step 5: Clause-by-Clause Analysis

Read the **entire contract** before flagging issues — clauses interact (e.g., a wide
kara umowna may be partially mitigated by a limitation-of-liability cap, and together they
may still be enforceable under Art. 484 § 1 KC in fine).

**⟁ CLARIFY** — For long or complex contracts (50+ pages, multiple schedules, or
incorporated standard terms / wzorzec umowny):

- Ask the user whether to perform a **full review** of all 16 clause categories or a
  **priority review** focused on stated focus areas plus any CZERWONY items discovered.
- If the contract incorporates external documents (e.g., "pursuant to Vendor's Standard
  Terms at [URL]"), ask whether the user wants those documents reviewed as well.

Cover all 16 clause categories below. For each, assess against the playbook (or Polish
market standard) and note whether the clause is present, absent, or unusual.

| #   | Clause Category                    | Depth    | Key Polish-Law Issues                                                                        |
| --- | ---------------------------------- | -------- | -------------------------------------------------------------------------------------------- |
| 1   | Limitation of Liability            | Deep     | Art. 473 KC; wina umyślna exclusion ban (Art. 473 § 2); mutual vs. unilateral                |
| 2   | Kara Umowna (Penalty Clauses)      | Deep     | Art. 483 § 1 (non-monetary only); miarkowanie (Art. 484 § 2); cumulation risks               |
| 3   | Intellectual Property / Copyright  | Deep     | Pola eksploatacji (Art. 41); employee works (Art. 12); moral rights; software (Art. 74)      |
| 4   | Data Protection / RODO             | Deep     | UPP / DPA (Art. 28 RODO); UODO; 72-hour breach notification; cross-border transfers          |
| 5   | Term and Termination               | Deep     | Art. 365¹ KC (indefinite obligations); wypowiedzenie vs. odstąpienie; cure periods           |
| 6   | Governing Law and Disputes         | Deep     | Polish courts / SA KIG / Lewiatan arbitration; Rome I; pathological arbitration clauses      |
| 7   | Indemnification                    | Deep     | No native civil-law concept; swoboda umów Art. 353¹; relation to Art. 471/Art. 58 KC         |
| 8   | Confidentiality / Trade Secrets    | Standard | UZNK Art. 11; Art. 72¹ KC; definition of tajemnica przedsiębiorstwa                          |
| 9   | Representations and Warranties     | Standard | Art. 387 (impossible performance); Art. 388 (wyzysk/exploitation); rękojmia vs. gwarancja    |
| 10  | Standard Terms Incorporation       | Standard | Art. 384-385 KC; transparency rule; battle-of-the-forms (Art. 385 § 4 KC)                    |
| 11  | Assignment                         | Standard | Art. 509 KC (przelew wierzytelności — receivables); consent for contractual assignment       |
| 12  | Force Majeure (Siła Wyższa)        | Standard | Art. 471 KC exemption; events; notice; mitigation; termination rights                        |
| 13  | Payment Terms                      | Standard | USNF (late payment interest); VAT; price escalation; disputed invoices                       |
| 14  | Compliance and Regulatory          | Standard | AML/KYC (ustawa o przeciwdziałaniu praniu pieniędzy); anti-bribery (ustawa o CBA); sanctions |
| 15  | Limitation Periods (Przedawnienie) | Standard | Art. 118-119 KC; general 6-year; specific shorter periods; non-modifiability                 |
| 16  | Definitions and Boilerplate        | Standard | Entire agreement; severability; notice; amendment; order of precedence                       |

### Step 6: Missing Clause Detection

After analysing clauses that are present, check for important clauses that are entirely
absent. A missing clause can be as significant as a problematic one.

Common missing clause issues (Polish-law context):

| Missing Clause                                   | Severity | Polish-Law Rationale                                |
| ------------------------------------------------ | -------- | --------------------------------------------------- |
| No limitation of liability                       | CZERWONY | Unlimited exposure; no KC fallback cap exists       |
| No UPP when personal data is processed           | CZERWONY | Art. 28 RODO — mandatory in writing                 |
| No kara umowna cap (łączny limit kar)            | ŻÓŁTY    | Cumulation risk; potential Art. 484 § 2 challenge   |
| No UZNK-aligned confidentiality definition       | ŻÓŁTY    | May not protect trade secrets adequately            |
| No pola eksploatacji specified in IP assignment  | CZERWONY | Transfer void / ineffective under Art. 41           |
| No governing law clause                          | CZERWONY | Rome I default may not produce Polish law           |
| No cure period in termination-for-cause          | ŻÓŁTY    | Abrupt removal creates Art. 471 KC exposure         |
| No UPP in international data-processing contract | CZERWONY | Art. 28 RODO + SCCs/adequacy required               |
| No force majeure with notice obligation          | ŻÓŁTY    | Art. 471 KC exemption still applies but uncertainty |

**⟁ CLARIFY** — When severity depends on business context not yet provided, ask rather
than assume:

- "This contract has no UPP (data processing addendum). Will personal data be processed?
  If yes, this is CZERWONY. If no personal data flows, it is fine."
- "There is no limitation of liability clause. Is there a specific business reason for
  leaving liability uncapped? If not, this is a CZERWONY item."

### Step 7: Flag Deviations

Classify each deviation using the three-tier system defined in the **Deviation Severity
Classification** section below. For each deviation:

- **ZIELONY**: Note for awareness.
- **ŻÓŁTY**: Generate specific redline language, provide a fallback position, and estimate
  business impact of accepting vs. negotiating.
- **CZERWONY**: Explain the specific legal risk (citing the KC or other authority), provide
  market-standard alternative language, estimate exposure, and recommend an escalation path.

**⟁ CLARIFY** — For borderline ŻÓŁTY/CZERWONY classifications:

- "This kara umowna is set at PLN X with no aggregate cap. Given the contract value of
  PLN Y, should I treat this as ŻÓŁTY (negotiate the cap) or CZERWONY (escalate)? It
  depends on your risk appetite."
- "The liability exclusion broadly covers 'indirect damages' but does not explicitly carve
  out willful fault (wina umyślna). Under Art. 473 § 2 KC, a court may void the entire
  exclusion. Should I treat this as ŻÓŁTY or CZERWONY?"

### Step 8: Generate Redlines

**⟁ CLARIFY** — Before generating redlines, ask about negotiation posture if unclear:

- **Relationship dynamic**: New counterparty, existing partner, or must-have vendor?
  Affects tone — redlines for a strategic partner should be collaborative.
- **Volume**: If there are many ŻÓŁTY items, ask: "I've found [N] items worth negotiating.
  Do you want redlines for all, or focus on the top [X] most impactful?"

For each ŻÓŁTY and CZERWONY deviation, generate a redline using the **Redline Format**
below. Follow Redline Best Practices.

### Step 9: Business Impact Summary

Provide a summary covering:

- **Overall risk assessment**: High-level view of the contract's risk profile
- **Top 3-5 issues**: Most important items to address, with severity and priority
- **Negotiation strategy**: Which issues to lead with, what to concede, how to sequence
- **Timeline considerations**: Urgency factors affecting the negotiation approach

**⟁ CLARIFY** — If deal context is unclear and would materially affect strategy:

- "Can you walk away from this deal, or is this vendor/partner essential? This determines
  whether the strategy is assertive or accommodating."
- "Have you negotiated with this counterparty before? Did they move on similar issues?"

### Step 10: Quality Verification

Before delivering the analysis, run all quality checks:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every CZERWONY item, run the 3-pass Self-Interrogation. Revise if any pass reveals
   a weakness.
3. Assign a Confidence Score to each material clause analysis.
4. Verify completeness: confirm all 16 clause categories addressed (present or flagged missing).
5. Generate the Glass Box Audit Trail and append it to the output.

### Step 11: CLM Routing

If a Contract Lifecycle Management system is connected via MCP:

- Recommend the appropriate approval workflow based on contract type and risk level
- Suggest routing path (standard approval, senior counsel, outside counsel / kancelaria zewnętrzna)
- Note any required approvals based on contract value or risk flags

If no CLM is connected, skip this step.

---

## Polish Civil Code — Key Mandatory Rules (Ius Cogens)

These provisions override whatever the contract says. Flag any clause that conflicts with
them as CZERWONY.

| Provision                    | Rule                                                                                                                                                                                                        | Contract Clause Affected                        |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **Art. 473 § 2 KC**          | Cannot exclude/limit liability for damage caused intentionally (wina umyślna). Any such clause is void under Art. 58 KC.                                                                                    | Liability exclusion / limitation                |
| **Art. 483 § 1 KC**          | Kara umowna may only be stipulated for non-performance of a **non-monetary** obligation (zobowiązanie niepieniężne).                                                                                        | Penalty clauses                                 |
| **Art. 484 § 2 KC**          | Court must reduce a grossly excessive kara umowna on application. This right cannot be contractually excluded.                                                                                              | Penalty clauses                                 |
| **Art. 119 KC**              | Limitation periods cannot be shortened or lengthened by contract.                                                                                                                                           | Limitation period clauses                       |
| **Art. 353¹ KC in fine**     | Freedom of contract ends where content/purpose violates the statute, social coexistence principles, or the nature of the legal relationship.                                                                | Any unusual clause                              |
| **Art. 58 § 1 KC**           | A transaction whose content or purpose violates statute or social coexistence principles is absolutely void (nieważność bezwzględna).                                                                       | Clauses referencing waivers of statutory rights |
| **Art. 385¹ KC**             | Provisions in standard terms (wzorzec umowny) not individually negotiated that grossly violate consumer interests are not binding. B2C mandatory; some B2B covered since 2021.                              | Standard terms in B2C and qualifying B2B        |
| **Art. 41 ust. 1-2 Pr.Aut.** | Copyright transfer/licence must specify all fields of exploitation (pola eksploatacji) that are known at the time. Transfer of "all rights" or "all future works" without specifying fields is ineffective. | IP assignment and licence clauses               |
| **Art. 16 Pr.Aut.**          | Author's moral rights (prawa osobiste) are inalienable and non-transferable. They may be subject to contractual restrictions on exercise.                                                                   | IP assignment / moral rights                    |
| **Art. 28(9) RODO**          | A data processing agreement (UPP) must be concluded in written or electronic form with any processor handling personal data.                                                                                | Data processing                                 |

---

## Clause Analysis Reference

### 1. Limitation of Liability (Ograniczenie Odpowiedzialności)

**Legal framework (Art. 471-473 KC):**
Art. 471 KC establishes fault-based contractual liability. Art. 473 § 1 KC permits parties
to contractually extend or restrict liability. However, **Art. 473 § 2 KC absolutely
prohibits excluding or limiting liability for damage caused wilfully (wina umyślna)**. Any
such exclusion is void under Art. 58 KC.

**Key elements to review:**

- Cap amount: fixed sum, multiple of fees paid (wielokrotność wynagrodzenia), or no cap
- Mutual vs. unilateral application
- Carveouts from the cap (e.g., IP indemnity, data breach, personal injury, wilful misconduct)
- Whether consequential damages (szkody pośrednie) and lost profits (lucrum cessans — Art. 361 § 2 KC)
  are excluded and whether the exclusion is mutual
- Whether the cap applies per-claim, annually, or in aggregate (cap łączny)
- Compliance with Art. 473 § 2 KC: does any exclusion purport to cover wilful fault?
- In B2C: consumer's statutory rights under Art. 385¹ KC cannot be excluded

**Common issues:**

- Cap set at fraction of fees (e.g., last 3 months) on a low-value contract — may be
  grossly inadequate; consider whether Art. 388 KC wyzysk might apply
- Broad exclusion of "any damages" without a wina umyślna carveout → void under Art. 473 § 2 KC
- Asymmetric exclusions favouring the drafter
- No distinction between damnum emergens (actual loss) and lucrum cessans (lost profit)
- Exclusion of liability in standard terms without individual negotiation in B2C → abusive (Art. 385¹ KC)

### 2. Kara Umowna (Contractual Penalty Clauses)

**Legal framework (Art. 483-485 KC):**
Kara umowna is a purely Polish civil-law institution. Unlike common-law liquidated damages,
it has no penalty-rule counterpart. Key rules:

- **Art. 483 § 1 KC**: May be stipulated **only** for non-performance / improper performance
  of a **non-monetary obligation (zobowiązanie niepieniężne)**. A kara umowna on failure to
  pay money is void (Art. 58 KC). [Confidence: Definite — 0.95+]
- **Art. 484 § 1 KC in fine**: The creditor may claim compensation exceeding the kara umowna
  if the parties have expressly agreed to this right (roszczenie uzupełniające). Without this
  clause, kara umowna is the maximum recovery.
- **Art. 484 § 2 KC**: The court **must** reduce (miarkować) a kara umowna that is grossly
  excessive (rażąco wygórowana) relative to actual damage, or where the obligation has been
  substantially performed. This right cannot be excluded by contract. [Confidence: Definite]

**Key elements to review:**

- Is the obligation triggering the kara umowna non-monetary? (Mandatory under Art. 483 § 1 KC)
- Quantum relative to contract value and likely damage
- Whether the right to claim supplementary compensation is included (Art. 484 § 1 KC in fine)
- Cumulation risk: can multiple kara umowna provisions accrue simultaneously to disproportionate totals?
- Is there an aggregate cap on total kara umowna (cap łączny)?
- Symmetry: do both parties face kara umowna obligations, or only one?
- For employment-adjacent clauses (non-compete): additional statutory rules apply [VERIFY]

**Common issues:**

- Kara umowna on failure to make payment (void — Art. 483 § 1 KC)
- No aggregate cap — cumulation could produce claims exceeding contract value
- No roszczenie uzupełniające clause — limits ability to claim actual loss above the kara
- Rażąco wygórowana kara — creates miarkowanie risk under Art. 484 § 2 KC
- Asymmetric penalties favouring the drafter

### 3. Intellectual Property / Copyright (Własność Intelektualna / Prawo Autorskie)

**Legal framework (Ustawa z dnia 4 lutego 1994 r. o prawie autorskim i prawach pokrewnych):**

**Art. 41 ust. 2**: Every IP assignment (przeniesienie praw majątkowych) and licence must
**expressly enumerate all fields of exploitation (pola eksploatacji)** that are known at
the time of conclusion. An assignment of "all rights" or "all copyright" without specifying
fields is **ineffective** as to fields not named. [Confidence: Definite — 0.95+]

**Three recognised categories of pola eksploatacji** (Art. 50 Pr.Aut.):

1. Reproduction and recording (utrwalanie i zwielokrotnianie) — specify technique: print, digital, etc.
2. Distribution/placing on market (obrót oryginałem lub egzemplarzami) — rental, sale, lending
3. Public use/communication (rozpowszechnianie) — performance, broadcast, making available online

**Art. 12 (Employee works — Utwory pracownicze)**: Unless the employment contract provides
otherwise, the employer acquires economic copyright rights (majątkowe prawa autorskie) to
works created in the course of performing employment duties, within the limits of the
employment purpose. Acquisition occurs on **acceptance** of the work.

**Art. 74 (Computer programs)**: For computer programs created in the course of employment,
the employer acquires rights **automatically on creation** (no acceptance required). [Confidence: High]

**Art. 16 (Moral rights — Prawa osobiste)**: Author's personal rights are **inalienable and
non-transferable**. They include the right of attribution (prawo do autorstwa), integrity
(prawo do integralności), first publication (prawo do pierwszego udostępnienia), and
supervision over use (prawo nadzoru). Parties may contractually restrict the **exercise**
of moral rights in specified contexts but cannot transfer them.

**Key elements to review:**

- Are all fields of exploitation explicitly named? (Art. 41 ust. 2 — mandatory)
- Does the agreement attempt to assign "future works" or "all works of a particular type"?
  (Invalid — Art. 41 ust. 3 Pr.Aut.)
- Ownership of pre-existing IP: each party should retain their own
- IP developed during engagement: who owns it? Art. 12 or contractual assignment?
- Are moral rights addressed? Is there a contractual restriction on exercise of moral rights
  (dozwolone zobowiązanie do niewykonywania praw osobistych)?
- Open-source considerations: GPL/LGPL contamination of deliverables
- Software specifically: Art. 74 provisions for employee-created computer programs

**Common issues:**

- Assignment of "all intellectual property rights" without listing pola eksploatacji
  (ineffective under Art. 41 ust. 2)
- Work-for-hire language imported from US contracts — not a Polish concept; use Art. 12
  or express assignment with pola eksploatacji
- Assignment purporting to cover future works without limitation (void — Art. 41 ust. 3)
- No restriction on moral rights exercise — vendor may later object to modifications
- Broad feedback licence without consideration

### 4. Data Protection / RODO (Ochrona Danych Osobowych)

**Legal framework (RODO / GDPR Art. 28; Ustawa z dnia 10 maja 2018 r. o ochronie danych osobowych):**

**Art. 28 ust. 9 RODO**: A **data processing agreement (UPP — Umowa Powierzenia Przetwarzania)**
must be concluded in **written or electronic form** whenever a controller (Administrator —
ADO) engages a processor to handle personal data. Absence of a UPP is a regulatory
violation with UODO enforcement exposure. [Confidence: Definite]

**72-hour breach notification (Art. 33 RODO)**: The processor must notify the controller
without undue delay after becoming aware of a personal data breach. The controller then has
72 hours to notify UODO. Contractual breach notification timelines longer than this are not
compliant.

**Key elements to review:**

- Is a UPP required? (Is personal data being processed under this agreement?)
- Does the UPP include all mandatory elements (Art. 28 ust. 3 RODO): subject matter, nature,
  purpose, duration; processor obligation to act only on controller instructions; sub-processor
  authorisation regime; confidentiality obligations; security measures; audit rights; deletion/return
  on termination; assistance with DSARs; assistance with DPIAs
- Breach notification timeline: does it allow the controller to notify UODO within 72 hours?
- Sub-processor regime: general authorisation (with notification right) or prior specific consent?
- International transfers: if data leaves the EU/EEA, what transfer mechanism applies?
  (EU adequacy decision, SCCs — current EU SCC clauses post-June 2021, BCRs)
- UODO supervisory authority: is the correct authority named?
- Data retention and deletion obligations on termination
- Purpose limitation and data minimisation

**Common issues:**

- No UPP where personal data is processed — CZERWONY
- Breach notification timeline of 72 or 96 hours at processor level (too long; must allow
  controller to notify UODO within 72 hours)
- Blanket sub-processor authorisation without notification right for the controller
- No international transfer mechanism when data flows outside the EU/EEA
- Processor claiming controller/co-controller status without justification
- No data deletion clause — data left with processor indefinitely

### 5. Term and Termination (Czas Trwania i Rozwiązanie Umowy)

**Legal framework:**

- **Art. 365¹ KC**: For obligations of a continuous nature (zobowiązania o charakterze
  ciągłym) concluded for an indefinite period, each party retains the right to terminate
  on notice. Statutory notice periods (2 weeks for <6 months, 1 month for ≥6 months, 3
  months for ≥3 years) apply unless the contract provides otherwise. Crucially, a clause
  attempting to exclude termination of an indefinite-period obligation entirely may conflict
  with Art. 353¹ KC (nature of the relationship).
- **Art. 491-496 KC**: Withdrawal from contract (odstąpienie) for non-performance. Art. 492
  KC: contractual right to withdraw (umowne prawo odstąpienia) within a specified period.
- **Art. 395 KC**: Right to withdraw within a specified period must be exercised within that
  period; right lapses automatically.

**Key elements to review:**

- Initial term and renewal mechanisms — autorenewal provisions and notice windows
- Termination for convenience (wypowiedzenie bez przyczyny): available? notice period? early
  termination fees? Is the fee a kara umowna? (If so, must be non-monetary)
- Termination for cause (wypowiedzenie z ważnych przyczyn / odstąpienie): cure period? what
  constitutes cause? Is the list exhaustive or illustrative?
- Effects of termination: data return, UPP obligations, IP reversion, outstanding payments,
  survival clauses (postanowienia przeżywające)
- Transition assistance (pomoc przejściowa) / wind-down period
- Art. 365¹ KC interaction: if the agreement is for an indefinite term, can the non-drafting
  party exercise the statutory right?

**Common issues:**

- Long initial term with no convenience termination and no statutory right under Art. 365¹ KC
- Autorenewal with very short notice window (< 30 days for annual contracts)
- No cure period for termination for cause
- Survival clauses effectively extending the agreement indefinitely
- Early termination fee structured as kara umowna on a monetary obligation (void — Art. 483 § 1 KC)
- Failure to address the Art. 365¹ KC right explicitly (creates ambiguity)

### 6. Governing Law and Dispute Resolution (Prawo Właściwe i Rozwiązywanie Sporów)

**Legal framework:**

- **Rome I Regulation (EC/593/2008)**: For international contracts, choice of law is governed
  by Rome I. Consumer contracts are subject to mandatory protections of the consumer's habitual
  residence regardless of choice of law (Art. 6 Rome I).
- **Polish court system**: Sąd rejonowy (regional court) → Sąd okręgowy (district court) →
  Sąd apelacyjny (court of appeal) → Sąd Najwyższy (Supreme Court). No jury trials.
- **Arbitration institutions**: Sąd Arbitrażowy przy KIG (new rules effective January 1, 2025),
  Sąd Arbitrażowy przy Konfederacji Lewiatan, ICC, LCIA, VIAC. Polish arbitration law based
  on UNCITRAL Model Law.
- **New York Convention**: Poland ratified; foreign arbitral awards enforceable.

**Key elements to review:**

- Choice of law: Polish law expressly selected? Any conflicts with mandatory rules?
- Dispute resolution mechanism: Polish court (sąd powszechny), arbitration, mediation?
- Venue / jurisdiction: appropriate court for the parties?
- Arbitration clause: is the institution named? Are the rules specified? Seat of arbitration?
  Watch for "pathological clauses" (klauzule patologiczne) — ambiguous institution names or
  contradictory procedural rules that may render the clause ineffective
- Escalation: is there a pre-dispute escalation procedure (negotiation → mediation →
  formal proceedings)?
- Attorney's fees: "loser pays" (zasada odpowiedzialności za wynik procesu) is the default
  in Polish courts (Art. 98 KPC). Contractual deviations should be flagged.
- Limitation periods: contractual attempts to modify Polish statutory periods are void
  (Art. 119 KC) — flag any such clauses

**Common issues:**

- Foreign governing law without business justification in a domestic (purely Polish) contract
- Pathological arbitration clause naming a non-existent institution or conflicting rules
- No escalation procedure before formal dispute resolution
- Mandatory arbitration with rules heavily favouring the drafter
- Attempts to shorten or lengthen limitation periods (void — Art. 119 KC)

### 7. Indemnification (Indemnifikacja / Zabezpieczenie)

**Legal framework:**
Indemnification (indemnity) is a common-law concept with no direct KC equivalent. Polish
parties use it via freedom of contract (Art. 353¹ KC). Key considerations:

- An indemnity obligation is distinct from contractual liability (Art. 471 KC) and
  guarantee/suretyship (poręczenie — Art. 876 KC). Polish courts may interpret an indemnity
  clause differently from common-law expectations. [Confidence: Probable — 0.65]
- The mechanism should be precisely defined: trigger events, claim procedure, right to
  control defence, settlement rights, cap (does the liability cap apply?), indemnitor
  control of defence.
- Art. 473 § 2 KC still applies: indemnification for wilful acts cannot be excluded or limited.

**Key elements to review:**

- Mutual or unilateral indemnification?
- Scope of trigger events: IP infringement, data breach, bodily injury, breach of representations?
- Is the indemnity subject to the overall liability cap, or uncapped?
- Defence control: who controls defence of third-party claims? What notice is required?
- Right to settle: can the indemnitor settle without indemnified party's consent?
- Relationship to kara umowna and liability limitation clauses (potential interaction risk)

**Common issues:**

- Unilateral indemnification favouring the drafter when both parties contribute IP
- No right to control defence of third-party claims
- Indemnity effectively uncapping liability beyond the stated limitation clause
- Ambiguous mechanism — courts may require clear evidence of loss (not just trigger event)
- Clause drafted in English indemnity language without Polish-law adaptation

### 8. Confidentiality / Trade Secrets (Poufność / Tajemnica Przedsiębiorstwa)

**Legal framework:**

- **Art. 11 ust. 2 UZNK**: Tajemnica przedsiębiorstwa (trade secret) — information of
  commercial value not publicly available, for which the holder has taken measures to maintain
  secrecy. Protection against disclosure and use by a third party applies.
- **Art. 72¹ KC**: Parties engaged in negotiations have a duty of confidentiality regarding
  information disclosed during negotiations, even without an NDA.
- A standalone NDA is an unnamed contract (umowa nienazwana) under Art. 353¹ KC. Kara
  umowna for NDA breach is permissible (obligation is non-monetary) — subject to miarkowanie.

**Key elements to review:**

- Definition of confidential information: is it consistent with Art. 11 UZNK (tajemnica
  przedsiębiorstwa definition)? Is it overly broad (capturing public information)?
- Standard carveouts: public domain, prior knowledge, independent development, legally required
  disclosure
- Duration: reasonable period (2-5 years post-termination for standard commercial information;
  indefinite for genuine trade secrets aligned with Art. 11 UZNK)
- Return / destruction obligations: with appropriate compliance / backup retention exception
- Remedies: zabezpieczenie roszczenia (interim injunction Art. 730 KPC) — acknowledge this
  right in the agreement

**Common issues:**

- Definition inconsistent with UZNK — may fail to protect trade secrets adequately
- No standard carveouts — overly restrictive and potentially unenforceable
- Indefinite confidentiality without trade-secret justification (ŻÓŁTY)
- Kara umowna for NDA breach without aggregate cap
- Non-solicitation or non-compete hidden in a confidentiality agreement

### 9. Representations and Warranties (Oświadczenia i Zapewnienia)

**Legal framework:**

- No concept of "warranty" identical to English law. Polish law uses:
  - **Rękojmia** (statutory warranty) — applies to contracts of sale (sprzedaż) and
    contracts for specific work (dzieło) under Art. 556-576 KC
  - **Gwarancja** (commercial guarantee) — voluntary contractual guarantee
  - **Oświadczenia zapewnienia** — representations used in international-style contracts
- **Art. 387 KC**: A contract for originally impossible performance (niemożliwość pierwotna)
  is void. This may affect representations about capabilities.
- **Art. 388 KC**: Exploitation (wyzysk) — a party forced into grossly unequal terms due to
  distress, inexperience, or insufficient insight may seek court reduction or rescission
  within 2 years. [VERIFY current statute text after 2021 amendment]

**Key elements to review:**

- Authority and capacity representations (prawidłowe umocowanie)
- Compliance with applicable law representations
- IP ownership / non-infringement representations
- No pending litigation material to performance
- Disclaimer of implied warranties — is the "AS IS" approach commercially reasonable?
- Survival period for representations and remedies for breach

### 10. Standard Terms Incorporation (Wzorzec Umowny)

**Legal framework (Art. 384-385 KC):**

- **Art. 384 § 1 KC**: Standard terms (wzorzec umowny) bind the other party only if the
  drafter provided the terms or gave the other party reasonable opportunity to review them
  before conclusion of the agreement.
- **Art. 385 § 2 KC**: Standard terms must be formulated clearly (jasno) and comprehensibly
  (zrozumiale). Ambiguous provisions are interpreted against the drafter (in dubio contra
  proferentem).
- **Art. 385 § 4 KC**: Where both parties use conflicting standard terms, conflicting
  provisions do not bind either party. The contract is concluded without those conflicting
  provisions, supplemented by statutory defaults.
- **Art. 385¹ § 1 KC** (B2C mandatory; B2B qualifying since 2021): Standard-form provisions
  not individually negotiated that shape the consumer's rights contrary to good customs or
  grossly violate consumer interests are not binding (klauzule niedozwolone / abusive clauses).
  The UOKiK register (rejestr klauzul niedozwolonych) lists prohibited clause types.

**Key elements to review:**

- Were standard terms properly delivered / notified before contract conclusion?
- Do standard terms meet the clarity / comprehensibility requirement of Art. 385 § 2 KC?
- Battle-of-the-forms: did both parties send conflicting standard terms?
- B2C: are any terms on the UOKiK register or consistent with gray-list categories?
- B2B: does the contract constitute qualifying B2B standard terms post-2021?

### 11–16. Standard Clause Checklist

For the following clause categories, review presence, reasonableness, and alignment with
playbook. Flag deviations using the ZIELONY/ŻÓŁTY/CZERWONY system.

**11. Assignment (Przelew / Cesja)**

- [ ] Consent required for assignment (zgoda drugiej strony)
- [ ] Change-of-control provisions addressed
- [ ] Exceptions for affiliates / corporate restructuring
- [ ] Art. 509 KC: receivables (wierzytelności) may be assigned without consent unless
      agreement or the nature of the obligation prohibits it — check interaction
- [ ] Anti-assignment clause is mutual

**12. Force Majeure (Siła Wyższa)**

- [ ] Events enumerated (not just "circumstances beyond control")
- [ ] Notification obligation within defined period
- [ ] Mitigation obligation specified
- [ ] Threshold before termination rights arise
- [ ] Post-pandemic: pandemic/epidemic explicitly addressed or excluded

**13. Payment Terms (Warunki Płatności)**

- [ ] Payment period specified (Art. 7 ustawa o terminach zapłaty — 30 days B2B default; [VERIFY])
- [ ] Late payment interest (odsetki ustawowe za opóźnienie) — Art. 481 KC; currently at
      [CHECK CURRENCY — statutory rate changes]; consider whether contractual rate applies
- [ ] VAT allocation and VAT invoice obligations
- [ ] Price escalation mechanism for multi-year contracts
- [ ] Disputed invoice process
- [ ] Currency and payment method

**14. Compliance and Regulatory (Regulacje)**

- [ ] Anti-bribery / anti-corruption representations (ustawa o Centralnym Biurze Antykorupcyjnym / CBA)
- [ ] Sanctions compliance (Polish and EU sanctions regimes; see Rozporządzenia Rady UE)
- [ ] AML/KYC (ustawa z dnia 1 marca 2018 r. o przeciwdziałaniu praniu pieniędzy — [VERIFY])
- [ ] GDPR/RODO compliance obligations for the processing activities
- [ ] Modern slavery / human trafficking (in cross-border contracts with UK parties: UK Modern Slavery Act)
- [ ] Regulatory approval requirements identified
- [ ] Audit rights for compliance verification

**15. Limitation Periods (Przedawnienie)**

- [ ] General limitation period: **6 years** (Art. 118 KC — reduced from 10 years in 2018);
      [VERIFY current text] lapses on the last day of the calendar year
- [ ] Specific shorter periods: contracts of sale 2 years; contracts for specific work
      (dzieło) 2 years from delivery; tort claims 3 years from knowledge (max 10 years)
- [ ] **Art. 119 KC**: Limitation periods **cannot be modified by contract** — flag any
      such clause as void
- [ ] Is the contract attempting to set a contractual claim deadline shorter than statutory?
      (void if so)
- [ ] Are there any notice-of-claim or notice-of-breach provisions that could amount to a
      de facto shortened limitation period?

**16. Definitions and Boilerplate (Definicje i Postanowienia Ogólne)**

- [ ] Key terms defined consistently and used throughout
- [ ] Entire agreement clause (całość porozumienia) — prevents parol evidence arguments
- [ ] Severability (klauzula salwatoryjna) — separates invalid provisions from the rest
- [ ] No implied waiver clause (brak dorozumianego zwolnienia)
- [ ] Notice provisions (forma i doręczanie) — written, addressed, deemed receipt
- [ ] Amendment provisions — written amendments only
- [ ] Order of precedence (pierwszeństwo postanowień) if multiple documents form the agreement
- [ ] Electronic signatures: QES (qualified electronic signature) satisfies Polish written-
      form requirement; simple e-signatures may not for contracts requiring written form

---

## Deviation Severity Classification

### ZIELONY — Akceptowalne (Acceptable)

The clause aligns with or is better than the organisation's standard position. Minor
variations that are commercially reasonable under Polish law and do not materially increase
risk. No breach of KC mandatory provisions.

**Examples:**

- Liability cap at 18 months of fees when standard is 12 months (better for customer)
- Kara umowna with aggregate cap that is symmetrical and at moderate market level
- RODO-compliant UPP with reasonable sub-processor notification period
- Governing law: Polish (the preference)
- Standard boilerplate that meets Art. 384-385 KC incorporation requirements

**Action**: Note for awareness. No negotiation needed.

### ŻÓŁTY — Do negocjacji (Negotiate)

The clause falls outside the standard position but within a negotiable range. The term is
seen in the Polish market but is not the organisation's preference. Requires attention and
likely negotiation, but not escalation.

**Examples:**

- Liability cap at 6 months of fees when standard is 12 months (below standard but not
  extreme)
- Kara umowna without aggregate cap but individual kara at moderate level (risk of Art. 484
  § 2 KC miarkowanie challenge)
- No roszczenie uzupełniające clause (Art. 484 § 1 KC in fine) — limits actual loss recovery
- Breach notification at processor level within 48 hours (tight but achievable)
- Autorenewal with 30-day notice period when standard is 60 days
- Unilateral indemnification for IP infringement when standard is mutual
- Art. 385 § 2 KC clarity concern in a non-consumer contract
- Foreign governing law (acceptable EU jurisdiction) without specific Polish-law carveout
- No aggregate kara umowna cap with individually reasonable individual kara amounts

**Action**: Generate specific redline language. Provide fallback position. Estimate business
impact of accepting vs. negotiating.

### CZERWONY — Eskalacja (Escalate)

The clause falls outside the acceptable range, triggers an escalation criterion, or poses
material legal risk under Polish law. Requires senior counsel, outside counsel
(kancelaria zewnętrzna), or business decision-maker sign-off.

**Examples (Polish-law specific):**

- Exclusion of liability for wilful fault (wina umyślna) — **void under Art. 473 § 2 KC**
- Kara umowna applied to a monetary obligation — **void under Art. 483 § 1 KC**
- IP assignment without specifying fields of exploitation (pola eksploatacji) —
  **ineffective under Art. 41 ust. 2 Pr.Aut.**
- No UPP where personal data is processed — **RODO Art. 28 violation**
- Clause attempting to modify limitation periods — **void under Art. 119 KC**
- Abusive clauses in consumer contracts — **void under Art. 385¹ KC**
- Breach notification period exceeding 72 hours without mechanism for UODO notification
- No limitation of liability in a high-value contract
- Governing law from a jurisdiction with no reciprocal enforcement (high enforcement risk)
- Broadly drafted non-compete that likely exceeds KC / Art. 353¹ limits
- Contract void in whole under Art. 58 KC (impossible performance, unlawful purpose)
- Standard terms not properly delivered / not satisfying Art. 384 KC incorporation rules

**Action**: Explain the specific risk with KC/Pr.Aut./RODO citation. Provide market-standard
alternative language. Estimate exposure. Recommend escalation path.

---

## Redline Format

For each redline:

```
**Clause**: [Section reference and clause name — Polish and English]
**Current language**: "[exact quote from the contract]"
**Proposed redline**: "[specific alternative language in Polish and/or English]"
**Rationale**: [1-2 sentences explaining why, suitable for sharing with counterparty's
counsel. Include Polish-law basis.]
**Legal basis**: [Art. X KC / Art. Y Pr.Aut. / Art. Z RODO — or "Polish market standard"]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative position if primary redline is rejected]
```

### Redline Best Practices

1. **Be specific**: Provide exact language ready to insert. Not vague guidance.
2. **Be balanced**: Propose language that is firm on critical points but commercially
   reasonable. Overly aggressive redlines slow Polish negotiations.
3. **Explain the rationale**: Include a brief professional rationale suitable for sharing.
   Reference specific KC articles where the redline addresses a legal risk.
4. **Provide fallback positions**: For ŻÓŁTY items, include a fallback if the primary ask
   is rejected.
5. **Prioritise**: Indicate must-haves vs. nice-to-haves.
6. **Consider the relationship**: Adjust tone based on whether this is a new vendor,
   strategic partner, or commodity supplier.
7. **Reference applicable law**: Mark as [VERIFY] if citing from memory without verification.
8. **Use Polish legal terminology**: Use correct Polish terms alongside English translations.
   Polish counsel on the other side will expect this.

---

## Negotiation Priority Framework (Ramy Priorytetów Negocjacyjnych)

### Poziom 1 — Bezwzględne (Must-Haves / Deal Breakers)

Issues where the organisation cannot proceed without resolution:

- Clauses **void under KC mandatory provisions** (Art. 473 § 2, Art. 483 § 1, Art. 119 KC)
- IP assignment **without pola eksploatacji** — ineffective as a matter of law
- Missing UPP **where personal data is processed** — regulatory violation
- Uncapped or materially insufficient liability protection in a high-value contract
- Abusive clauses in a B2C contract (Art. 385¹ KC) — not binding on consumer
- Governing law in a jurisdiction creating material enforcement risk
- Clauses conflicting with the organisation's regulatory obligations

### Poziom 2 — Pożądane (Should-Haves / Strong Preferences)

Issues that materially affect risk but have negotiation room:

- Liability cap adjustments within acceptable range
- Kara umowna amounts, caps, and symmetry
- Indemnification scope and mutuality
- Termination flexibility and cure periods
- Data protection: sub-processor regime, breach notification timeline
- Audit and compliance rights
- UZNK-compliant trade-secret protection

### Poziom 3 — Opcjonalne (Nice-to-Haves / Concession Candidates)

Issues that improve the position but can be conceded strategically:

- Preferred governing law if alternative is acceptable
- Notice period preferences
- Minor definitional improvements
- Insurance certificate requirements
- Boilerplate refinements

**Strategia negocjacyjna**: Lead with Poziom 1. Trade Poziom 3 concessions to secure
Poziom 2 wins. Never concede Poziom 1 without escalation.

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Identify contract type, user's side, playbook position. Classify complexity
(standard / bespoke / high-value). Identify which KC provisions, RODO articles, and
Pr.Aut. provisions are likely to be engaged. Determine B2B vs. B2C.

**DO**: Execute the clause-by-clause analysis. Detect missing clauses. Generate redlines.
Score severity. Apply mandatory KC ius cogens checklist.

**CHECK**: Run Citation Quality Gates. For any CZERWONY item, run the 3-pass Self-
Interrogation. Verify all KC citations where possible. Confirm all 16 clause categories
addressed.

**ACT**: Record any new patterns discovered. Flag heuristics for future reviews. If the
review changes understanding of a standard position, note it for playbook update.

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise.

| Gate           | Rule                                                                                                                                         | Fail Action                                                   |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific KC article, Pr.Aut. provision, RODO article, or established Polish-law principle                          | Add citation or mark "[UNVERIFIED — radca prawny to confirm]" |
| **Format**     | All KC/Pr.Aut. citations follow consistent Polish legal citation format (e.g., "Art. 483 § 1 KC", "Art. 41 ust. 2 Pr.Aut.")                  | Fix format                                                    |
| **Currency**   | Every cited provision checked for amendments — KC and Pr.Aut. are frequently amended. Limitation periods changed from 10 to 6 years in 2018. | Flag "[CHECK CURRENCY — may have been amended]"               |
| **Domain**     | Analysis stays within Polish law. No common-law concepts (work-for-hire, punitive damages, jury waiver) imported without qualification       | Remove or flag jurisdictional bleed                           |
| **Confidence** | Uncertainty explicitly stated. Where Polish SN case law is unclear or there is a split in academic opinion, say so.                          | Add confidence qualifier                                      |

### Self-Interrogation for CZERWONY Items

For any clause classified as CZERWONY, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**:

- Does the risk assessment follow logically from the KC article or Pr.Aut. provision cited?
- Would a Polish court (including SN) actually reach this conclusion on these facts?
- What is the strongest argument the counterparty's radca prawny will make?

**Pass 2 — Completeness**:

- Have all relevant KC provisions been considered? Any relevant SN uchwały (resolutions)?
- Are there UOKiK decisions or UODO guidelines relevant to this clause?
- Are there regulatory dimensions (RODO, UZNK, ustawa AML) not yet considered?

**Pass 3 — Challenge**:

- What is the strongest argument that this clause IS acceptable under Polish law?
- Under what circumstances might a reasonable Polish lawyer accept this risk?
- Is the CZERWONY classification proportionate, or is this actually ŻÓŁTY with conditions?

Mark the audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material clause analysis, assign a confidence level:

| Level        | Range     | Meaning                                                                   | Action                                                   |
| ------------ | --------- | ------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled KC rule, clear Art. X statutory text, consistent SN jurisprudence | State with confidence                                    |
| **High**     | 0.80-0.94 | Strong KC authority, minor interpretation questions, mostly consistent SN | State with brief caveat                                  |
| **Probable** | 0.60-0.79 | Good arguments but SN split or doctrine unsettled                         | State with explicit reasoning and contra-indicators      |
| **Possible** | 0.40-0.59 | Genuinely uncertain, competing SN decisions or academic views             | Flag for Polish counsel review with both sides           |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative, limited or no authority                          | Do not assert; flag as "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every contract review output MUST include a Glass Box audit section at the end:

```yaml
glass_box:
  contract: "[Contract title and date]"
  contract_type: "[SaaS / Professional Services / Licence / Supply / Other]"
  user_side: "[Vendor/Supplier / Customer/Zamawiający / Licensor / Licensee]"
  governing_law: "Polish law (prawo polskie / Kodeks cywilny)"
  contract_structure: "[B2B / B2C / Mixed]"
  playbook_used: "[Playbook name or 'Polish market standards and KC ius cogens']"
  review_basis: "[Organisational playbook / Polish market standards]"
  clauses_reviewed: 16
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  kc_ius_cogens_checked: "[Yes — see mandatory rules checklist]"
  legalcode_mcp: "Connected / Not connected"
  iura_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-pl-contract-authority.md or 'Not created']"
  statutes_consulted:
    - "KC Art. 473 § 2 — [VERIFIED / UNVERIFIED]"
    - "KC Art. 483-485 — [VERIFIED / UNVERIFIED]"
    - "Pr.Aut. Art. 41 ust. 2 — [VERIFIED / UNVERIFIED]"
    - "RODO Art. 28 — [VERIFIED / UNVERIFIED]"
    - "[add all consulted statutes]"
  case_law_consulted:
    - "[SN case reference if available — VERIFIED / UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CZERWONY items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, e.g., 'Kara umowna miarkowanie analysis requires Polish
      court assessment of proportionality — legal counsel recommended']"
    - "[Other caveats]"
  reviewer: "AI-assisted — requires qualified Polish counsel review (radca prawny / adwokat)"
```

---

## Multi-Stakeholder Mapping

For every contract, identify ALL affected stakeholders — not just the two contracting parties:

| Stakeholder                                 | Role                   | Affected Clauses                      | Impact     | Action Required                                                 |
| ------------------------------------------- | ---------------------- | ------------------------------------- | ---------- | --------------------------------------------------------------- |
| [Party A / Strona A]                        | [Customer/Zamawiający] | All                                   | Primary    | Sign / Negotiate                                                |
| [Party B / Strona B]                        | [Vendor/Dostawca]      | All                                   | Primary    | Sign / Negotiate                                                |
| Data subjects (osoby, których dane dotyczą) | Third party            | Data protection / RODO                | Indirect   | UPP required if personal data processed                         |
| Sub-processors (podpowierzający)            | Third party            | Data protection                       | Indirect   | Sub-processor notification/consent regime                       |
| UODO                                        | Regulator              | Data protection                       | Compliance | Breach notification; supervisory authority oversight            |
| UOKiK                                       | Regulator              | Abusive clauses                       | Compliance | B2C standard terms; register compliance                         |
| Employees / Pracownicy                      | Internal               | IP (Art. 12 Pr.Aut.), confidentiality | Indirect   | Employment contract alignment; Art. 12 employee-works provision |
| Sub-contractors / Podwykonawcy              | Third party            | IP, liability, data                   | Indirect   | Flow-down of key obligations                                    |

---

## Localization Notes

### Polish Language Requirements

Polish law does not generally mandate that commercial contracts be in Polish for B2B
relationships. However:

- Labour contracts (umowy o pracę) with employees working in Poland must include Polish or
  bilingual versions of key provisions [VERIFY]
- Consumer-facing terms (regulamin, ogólne warunki umów — OWU) accessible to Polish consumers
  should be in Polish
- Court proceedings in Poland are conducted in Polish — an exhibit contract in a foreign
  language will require a certified translation (tłumaczenie przysięgłe)

### B2B Contract Formalities

- **Written form (forma pisemna)**: Recommended for most commercial contracts. Satisfied by
  handwritten signature or **Qualified Electronic Signature (QES)** under eIDAS and Polish
  implementing regulations.
- **Notarial deed (akt notarialny)**: Required for real property transactions, certain
  corporate documents, and a few special cases. Electronic signatures do NOT satisfy
  notarial-deed requirements.
- **Registered letter / electronically confirmed**: For effective service of important notices
  (wypowiedzenia, odstąpienia) — the contract should specify notice method.

### Drafting in Polish vs. English

When the governing-law is Polish but the contract is in English:

- Polish courts will apply Polish law regardless of language
- Key Polish legal concepts (kara umowna, pola eksploatacji, odstąpienie) should be cross-
  referenced in Polish if the contract is in English, to avoid misinterpretation
- An "as-is" disclaimer is not an effective exclusion of Polish rękojmia (statutory warranty)
  rules in a contract of sale unless drafted specifically to reflect KC Art. 558 [VERIFY]

---

## Anti-Patterns (Katalog Błędów)

What NOT to do when reviewing Polish-law contracts:

1. **Applying common-law concepts without Polish-law adaptation** — "Work-for-hire,"
   "punitive damages," "class action waiver," and "jury waiver" have no direct Polish-law
   equivalent. Importing these terms without Polish-law equivalents creates ambiguity.

2. **Missing Art. 473 § 2 KC in liability exclusions** — Every time a liability exclusion
   clause is reviewed, check whether it could be read to exclude liability for wilful fault
   (wina umyślna). If so, it is void under Art. 58 KC. This is the single most common
   Polish-law trap in imported international contract templates.

3. **Treating kara umowna on a monetary obligation as valid** — Art. 483 § 1 KC is absolute.
   A kara umowna on failure to pay an invoice is void. This arises frequently in translated
   international contracts where a "liquidated damages" clause covers all breaches.

4. **Ignoring miarkowanie risk** — A kara umowna without an aggregate cap (cap łączny)
   carries miarkowanie risk under Art. 484 § 2 KC, but relying on miarkowanie as a
   safeguard is poor practice — it requires court proceedings.

5. **Accepting IP assignment without pola eksploatacji** — An assignment of "all copyright"
   without listing fields of exploitation is ineffective under Art. 41 ust. 2 Pr.Aut. as
   to un-named fields. This is a CZERWONY item that frequently goes unnoticed in contracts
   adapted from US templates.

6. **Overlooking moral rights in creative agreements** — Polish moral rights (Art. 16 Pr.Aut.)
   are inalienable. A clause attempting to transfer moral rights is void. Ensure the contract
   includes a binding restriction on the author's exercise of moral rights (not a transfer).

7. **Forgetting the UPP** — Any agreement where personal data is processed on behalf of the
   controller requires a written UPP (Art. 28 RODO). Even a simple SaaS agreement with
   minimal personal data processing requires one. Absence is a CZERWONY item.

8. **Citing limitation periods without checking Art. 119 KC** — Any clause attempting to
   shorten or extend Polish statutory limitation periods is void. Do not accept contractual
   time-bars shorter than the applicable KC period.

9. **Single-pass analysis** — Reading each clause once without considering inter-clause
   interactions. In Polish contracts, an uncapped kara umowna + an uncapped indemnity clause
   may be read together to create effectively unlimited exposure.

10. **Omitting the kara umowna aggregate cap check** — Multiple separate kara umowna
    provisions (delay, defect, data breach, confidentiality breach) can accumulate to sums
    vastly exceeding contract value. Always sum the potential exposure.

11. **Accepting foreign governing law without assessing mandatory Polish rules** — Rome I
    does not displace all Polish mandatory rules. Consumer contracts retain Polish consumer
    protections regardless of choice of law (Art. 6(2) Rome I). Employment contracts retain
    Polish employment law regardless of choice of law (Art. 8(1) Rome I).

12. **Treating standard terms as equivalent to individually negotiated provisions** — Under
    Art. 385¹ KC, provisions in a standard-form contract (wzorzec umowny) that were not
    individually negotiated and that grossly violate consumer interests are not binding.
    Standard terms require separate analysis.

13. **Ignoring the Art. 385 § 4 KC battle-of-the-forms rule** — Where both parties used
    different standard terms, conflicting provisions are not included. Ensure the contract
    clearly establishes which standard terms govern if both parties used them.

14. **Redlines without Polish-law fallback positions** — A redline that says "delete this
    clause" without offering a Polish-law-compliant alternative is a negotiation dead-end.
    Always provide a fallback in language suitable for a Polish radca prawny.

15. **Assuming the limitation period is 10 years** — The general KC limitation period was
    reduced from 10 to **6 years** in 2018. Many practitioners and online resources still
    cite 10 years. Verify the current text of Art. 118 KC. [CHECK CURRENCY]

16. **Ignoring what is missing** — Focusing only on clauses present and missing absent
    clauses. A Polish-law contract with no UPP, no pola eksploatacji in an IP clause, and
    no limitation of liability has material gaps that constitute legal risk regardless of
    what is present.

17. **Accepting force-majeure clauses without a mitigation obligation** — Under Art. 471 KC,
    force majeure provides a defence to non-performance. But the affected party must still
    mitigate. A force-majeure clause without a mitigation obligation creates asymmetric
    risk.

18. **Assuming without asking** — Silently assuming B2B when a consumer party may be
    involved, or silently assuming Polish law governs when there is no express choice-of-law
    clause. A wrong assumption produces a confidently wrong analysis.

---

## Writing Standards

Apply plain-language discipline to all output:

**For redline rationales** (shared with counterparty's counsel):

- Plain language in English and/or Polish as appropriate to the audience
- Active voice: "This clause excludes liability for negligence" not "Liability for negligence
  is excluded by this clause"
- Short sentences. One point per sentence.
- Name the actor and the legal basis: "Art. 473 § 2 KC prohibits the exclusion of liability
  for wilful fault" not "there may be enforceability issues"
- Reference specific KC articles; do not vaguely say "Polish law may apply here"

**For internal analysis**:

- Same plain-language standards
- May include more technical KC/Pr.Aut./RODO analysis
- Confidence qualifiers where appropriate
- Glass Box audit trail appended

**Quality gates before delivery**:

1. Can a non-lawyer Polish business stakeholder understand the executive summary?
2. Can a Polish radca prawny understand and respond to each redline?
3. Is every legal claim backed by a specific KC article, Pr.Aut. provision, or RODO article
   (or flagged [VERIFY])?
4. Are any Polish legal terms used without explanation? If yes, add a brief translation.
5. Could any sentence be shorter without losing meaning? If yes, shorten.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** and optionally **IURA MCP** as its
primary Polish legal research tools.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for Polish KC provisions, Pr.Aut. articles, RODO guidance, and SN
  case law relevant to the contract's key clauses
- Save results to `/tmp/legalcode-pl-contract-authority.md`
- Reference verified authority throughout the clause analysis
- For CZERWONY items, search for SN decisions (uchwały, wyroki) to support or challenge
  the classification
- Check statutory currency — KC has been amended multiple times
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**With IURA MCP connected (optional — Polish law specialist):**

- Use tools `Search_DU` (Dziennik Ustaw — statutes), `Search_SN` (Sąd Najwyższy — Supreme
  Court), `Search_SP` (Sąd Powszechny — common courts) to verify specific KC articles and
  SN case signatures before relying on them in the analysis
- IURA provides access to Polish legal databases; citations verified via IURA are highly
  reliable for Polish law
- Note IURA connection in the Glass Box audit trail

**Without either tool:**

- Mark all KC and Pr.Aut. citations with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`, `iura_mcp: "Not connected"`
- Focus the analysis on structural risk assessment and commercial issues
- Do not present unverified SN case signatures as settled law — flag "[VERIFY — case
  reference cited from memory; verify in Legalis or LEX before relying on this]"

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Raport z przeglądu umowy / Contract Review Report

**Document / Umowa**: [contract name/identifier]
**Parties / Strony**: [party names and roles]
**Your Side / Wasza strona**: [vendor/customer/etc.]
**Governing Law / Prawo właściwe**: Polish law (Kodeks cywilny)
**Contract Type / Typ umowy**: [SaaS / Professional Services / Licence / etc.]
**B2B / B2C**: [confirmed type]
**Deadline**: [if provided]
**Review Basis / Podstawa przeglądu**: [Playbook name / Polish market standards + KC ius cogens]
**Date of Review / Data przeglądu**: [date]

---

## Kluczowe ustalenia / Key Findings

[Top 3-5 issues with severity flags (CZERWONY/ŻÓŁTY) and one-line summaries]
[Include KC article reference for each CZERWONY item]

---

## Brakujące klauzule / Missing Clauses

[List any of the 16 clause categories that are absent, with severity assessment and KC basis]

---

## KC Mandatory Rules Check

| Provision                                       | Status             | Finding   |
| ----------------------------------------------- | ------------------ | --------- |
| Art. 473 § 2 KC (wina umyślna exclusion ban)    | [OK / ISSUE]       | [finding] |
| Art. 483 § 1 KC (kara umowna scope)             | [OK / ISSUE]       | [finding] |
| Art. 41 ust. 2 Pr.Aut. (pola eksploatacji)      | [OK / ISSUE / N/A] | [finding] |
| Art. 28 RODO (UPP required)                     | [OK / ISSUE / N/A] | [finding] |
| Art. 119 KC (limitation periods non-modifiable) | [OK / ISSUE]       | [finding] |
| Art. 385¹ KC (abusive clauses B2C)              | [OK / ISSUE / N/A] | [finding] |

---

## Analiza klauzula po klauzuli / Clause-by-Clause Analysis

### [Clause Category] — [ZIELONY / ŻÓŁTY / CZERWONY] | Confidence: [level]

**Contract says / Umowa stanowi**: [summary of the provision]
**Standard position / Pozycja standardowa**: [playbook or Polish market standard]
**Deviation / Odstępstwo**: [description of gap]
**Polish-law risk / Ryzyko prawne**: [KC/Pr.Aut./RODO basis]
**Business impact / Wpływ biznesowy**: [what this means practically]
**Redline** (if ŻÓŁTY or CZERWONY):

> [Specific proposed language — Polish and/or English]

[Repeat for each clause category]

---

## Strategia negocjacyjna / Negotiation Strategy

**Poziom 1 (Must-Haves)**: [list]
**Poziom 2 (Should-Haves)**: [list]
**Poziom 3 (Concession Candidates)**: [list]

**Recommended approach / Rekomendowane podejście**: [sequencing, tone, strategic trades]

---

## Stakeholder Impact Map (Mapa Interesariuszy)

[Table per Multi-Stakeholder Mapping section]

---

## Next Steps / Dalsze kroki

[Specific actions, owners, deadlines]

---

[Glass Box audit trail YAML block]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis for Polish-jurisdiction commercial
contract review. Legal research basis: Polish Civil Code (Kodeks cywilny z dnia 23 kwietnia
1964 r.), Polish Copyright Act (Ustawa z dnia 4 lutego 1994 r. o prawie autorskim i prawach
pokrewnych), UZNK (Ustawa z dnia 16 kwietnia 1993 r. o zwalczaniu nieuczciwej konkurencji),
RODO (Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679), Ustawa z dnia 10 maja
2018 r. o ochronie danych osobowych, Rome I Regulation (EC/593/2008). Structural patterns
adapted from the `legalcode-contract-review` Legalcode gold standard. Polish methodology
consolidated from the IURA contract-review imported skill (`iura-ai/IURA-Plugins`,
`iura-pl/skills/contract-review/SKILL.md`, imported 2026-02-27) with deep legal research
supplement and full Legalcode quality framework overlay (Citation Quality Gates, Self-
Interrogation, Confidence Scoring, Glass Box audit trail, Anti-patterns, Writing Standards,
Multi-stakeholder mapping, 18-element completeness). Sources consulted: Dudkowiak & Putyra
Polish contract law guide, CMS Law Poland consequential loss guide, Kieltyka Gladkowski
legal liability limits, WIPO Polish Copyright Law, UODO data processing agreement guidance
(uodo.gov.pl), UOKiK abusive clauses guidance (uokik.gov.pl), SA KIG arbitration rules
2025 (sakig.pl), Lexology Polish limitation periods guide, arslege.pl KC commentaries,
polishprivatelaw.pl introduction to contract law, In Principle (codozasady.pl) contractual
penalties analysis.

All statutory citations are [VERIFY] pending legalcode-mcp or IURA MCP verification in a
live session. Polish law is frequently amended — always verify current statutory text in
Legalis, LEX, or the official Dziennik Ustaw (dziennikustaw.gov.pl / isap.sejm.gov.pl)
before relying on any provision described here.
