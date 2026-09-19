---
name: legalcode-nda-triage-pl
description: Screen and triage incoming NDAs under Polish law (prawo polskie) — classify as GREEN (standard
  approval), YELLOW (counsel review), or RED (significant issues) with confidence-scored, auditable analysis.
  Applies Polish Civil Code (Kodeks cywilny, KC), Act on Combating Unfair Competition (Ustawa o zwalczaniu
  nieuczciwej konkurencji, UZNK), Labour Code (Kodeks pracy, KP), and Code of Civil Procedure (Kodeks
  postepowania cywilnego, KPC). Use when a new NDA arrives from sales, business development, or a counterparty,
  when assessing NDA risk level before signature, when deciding whether an NDA needs full counsel review,
  or when routing NDAs through an in-house legal workflow governed by Polish law. Supports playbook-based
  or general-standard screening. Produces a structured triage report with Glass Box audit trail.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode NDA Triage -- Poland (Prawo polskie)

> **Disclaimer / Zastrzezenie**: This skill provides a framework for AI-assisted NDA
> screening under Polish law. It does not constitute legal advice (porada prawna). All
> outputs should be reviewed by a qualified legal professional (radca prawny or adwokat)
> licensed in Poland before use. Laws change; verify current applicability before relying
> on any provision described here. Statutory and case law references cited from memory carry
> hallucination risk -- verify against authoritative sources (e.g., ISAP, LEX, Legalis)
> before relying on them.

## Purpose and Scope

This skill rapidly screens incoming non-disclosure agreements (umowy o zachowaniu poufnosci,
NDA) against standard criteria or an organizational playbook under Polish law, classifies
them by risk level (GREEN / YELLOW / RED), generates actionable findings with suggested
fixes, and produces a confidence-scored, auditable triage report with routing
recommendations.

**Covers:**

- Mutual and unilateral NDAs (standalone agreements)
- Confidentiality sections embedded in larger commercial agreements (with caveats)
- NDAs governed by Polish law (prawo polskie)
- Playbook-based or general-standard screening
- Quality-verified output with Glass Box audit trail

**Does not:**

- Draft new NDAs (see the `nda-mutual` skill for drafting)
- Perform full contract review (see `legalcode-contract-review` for comprehensive review)
- Provide legal advice (porady prawne) or replace qualified counsel (radca prawny / adwokat)
- Cover NDAs governed by foreign law (for jurisdiction-agnostic screening, use
  `legalcode-nda-triage`)

## Jurisdiction and Governing Law

This skill is localized for **Polish law** (prawo polskie). The NDA's governing law clause
should specify Polish law for this skill to apply directly. If the NDA is governed by a
different law, use the jurisdiction-agnostic `legalcode-nda-triage` skill or the
appropriate jurisdiction-specific variant.

### Polish Legal Framework for NDAs

In Polish law, an NDA (umowa o zachowaniu poufnosci) is an unnamed contract (umowa
nienazwana) concluded under the principle of freedom of contract (zasada swobody umow) per
Art. 353^1 of the Civil Code (Kodeks cywilny, KC). Its validity and enforceability rest on
general obligations law. Key statutory provisions:

**Civil Code (Kodeks cywilny, KC):**

- **Art. 353^1 KC** -- Freedom of contract (swoboda umow): parties may shape their legal
  relationship as they see fit, provided its content and purpose do not contradict the
  nature of the relationship, statute, or principles of social coexistence (zasady
  wspolzycia spolecznego). This is the foundational basis for NDA enforceability.
- **Art. 72^1 KC** -- Pre-contractual confidentiality: a party that obtains confidential
  information during negotiations is obliged not to disclose or use it for its own
  purposes, unless the parties agree otherwise. Breach triggers a claim for surrender of
  benefits obtained through unlawful use. This applies even without a signed NDA.
- **Art. 415 KC** -- Tort liability (odpowiedzialnosc deliktowa): whoever by fault causes
  damage to another is obliged to remedy it. Provides a parallel claim path for
  confidentiality breaches.
- **Art. 471 KC** -- Contractual liability (odpowiedzialnosc kontraktowa): the debtor is
  obliged to remedy damage resulting from non-performance or improper performance of an
  obligation, unless non-performance is due to circumstances for which the debtor is not
  responsible. This is the primary claim basis for NDA breach.
- **Art. 483 KC** -- Contractual penalties (kary umowne): parties may stipulate that
  damages for non-performance or improper performance of a non-monetary obligation
  (zobowiazanie niepieniezne) shall be paid as a specified sum. Critically, kary umowne
  may only be stipulated for non-monetary obligations -- a confidentiality obligation
  qualifies.
- **Art. 484 s.1 KC** -- The stipulated penalty is due regardless of the amount of actual
  damage. The obligee may demand supplementary damages (odszkodowanie przenoszace kare)
  only if the contract so provides.
- **Art. 484 s.2 KC** -- Judicial reduction of penalties (miarkowanie kar umownych): if the
  obligation has been performed to a significant extent or if the penalty is grossly
  excessive (razaco wygorowana), the debtor may request reduction by the court.

**Act on Combating Unfair Competition (Ustawa o zwalczaniu nieuczciwej konkurencji, UZNK):**

- **Art. 11 UZNK** -- Trade secret protection (tajemnica przedsiebiorstwa): an act of unfair
  competition is the disclosure, use, or acquisition of another's information constituting
  a trade secret. As amended on 4 September 2018 (implementing EU Trade Secrets Directive
  2016/943), Art. 11 s.2 UZNK defines a trade secret as technical, technological,
  organizational, or other commercially valuable information that is not publicly available
  and for which the entrepreneur has taken necessary steps to maintain its confidentiality.
- **Art. 18 UZNK** -- Remedies for unfair competition: the entrepreneur whose interest is
  threatened or infringed may demand cessation, removal of effects, making a statement,
  damages, surrender of unjust enrichment, and payment to a social purpose.

**Labour Code (Kodeks pracy, KP):**

- **Art. 101^1 KP** -- Non-compete during employment: requires a separate written agreement
  (under penalty of invalidity). Applies to employees with access to information whose
  disclosure could harm the employer.
- **Art. 101^2 KP** -- Post-employment non-compete: requires a separate written agreement
  specifying the period and compensation. Compensation must not be less than 25% of the
  salary received before termination, for the duration of the non-compete period. The
  non-compete obligation ceases if the employer fails to pay compensation.
- **Art. 101^3 KP** -- Written form requirement: non-compete agreements must be in writing
  under penalty of invalidity (forma pisemna pod rygorem niewaznosci).
- **Art. 101^4 KP** -- Provisions on non-compete apply to other contracts where appropriate.

**Code of Civil Procedure (Kodeks postepowania cywilnego, KPC):**

- **Art. 730 KPC** -- Securing of claims (zabezpieczenie roszczen): in every civil case
  subject to examination by a court, the parties may request interim measures. The applicant
  must demonstrate the claim (uprawdopodobnienie roszczenia) and legal interest in securing
  it (interes prawny w udzieleniu zabezpieczenia).
- **Art. 730^1 KPC** -- Legal interest exists when the absence of security would make
  execution of the judgment impossible or seriously hinder it.
- **Art. 755 KPC** -- Interim measures for non-monetary claims: the court may issue
  injunctions to regulate rights and obligations during proceedings, including prohibitions
  on specific actions.

**RODO (Polish GDPR Implementation):**

- Where an NDA involves sharing personal data (dane osobowe), the parties must consider
  whether a separate Data Processing Agreement (umowa powierzenia przetwarzania danych
  osobowych) under Art. 28 RODO/GDPR is required. An NDA alone does not satisfy GDPR
  data processing requirements. If confidential information includes personal data, flag
  the need for a DPA assessment.

**Key distinction from common law**: Polish law does not require consideration (swiadczenie
wzajemne) for an NDA to be valid. A unilateral confidentiality obligation is fully
enforceable. Furthermore, even without a signed NDA, parties to negotiations are bound by
the pre-contractual confidentiality obligation under Art. 72^1 KC, and trade secrets are
protected independently under Art. 11 UZNK.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- Multiple valid approaches exist and the user's preference matters
- Business context is needed to classify severity correctly
- Ambiguity in the NDA creates a fork that only the user can resolve

When you reach a **⟁ CLARIFY** block, ask the user before proceeding — do not silently assume
defaults. Use the harness's structured question tool when one is available:

- **Claude Code / Agent SDK:** invoke the `AskUserQuestion` tool. Limits: 1–4 questions per
  call, 2–4 options each, header ≤ 12 characters. Pass the CLARIFY options as the `options`
  array.
- **OpenAI Codex CLI:** invoke `ask_user_question` (runtime) or, in plan mode,
  `request_user_input`. Pass the CLARIFY options as choices.
- **No structured tool available (other harnesses, CI, headless mode without a `canUseTool`
  callback):** emit the CLARIFY questions as numbered plain text and **stop until the user
  replies**. Do not proceed with assumed answers.

Skip any CLARIFY question the user has already answered in the initial prompt or prior
conversation. When you proceed with partial context, state every assumption explicitly so the
user can correct it.

---

## Workflow

### Step 1: Accept the NDA

Accept the NDA in any of these formats:

- **File**: PDF, DOCX, or other document format
- **URL**: Link to the NDA in a document system
- **Pasted text**: NDA text pasted directly into the conversation

If no NDA is provided, prompt the user to supply one.

### Step 2: Gather Context

**CLARIFY** -- Before beginning the triage, ask the user these questions. Present them as
structured options:

1. **Which side are you on?** (Po ktorej stronie jestes?)
   - Options: Receiving party (strona otrzymujaca), Disclosing party (strona ujawniajaca),
     Both (mutual NDA / NDA wzajemna), Not sure (nie jestem pewien)
   - _Why this matters_: Determines which protections to scrutinize -- a receiving party
     needs strong carveouts and reasonable obligations; a disclosing party needs broad
     protection scope and strong remedies.

2. **Business context**: What is the purpose of this NDA? (Kontekst biznesowy)
   - Options: Exploratory / pre-sales discussions (rozmowy wstepne), Vendor evaluation
     (ocena dostawcy), M&A due diligence (badanie due diligence), Technology evaluation /
     proof of concept, Employment / contractor (zatrudnienie / wspolpraca), Other (inny)
   - _Why this matters_: An M&A NDA may legitimately include standstill provisions; a
     sales-stage NDA should not. Context determines whether unusual clauses are appropriate.

3. **Governing law confirmation**: Is this NDA governed by Polish law? (Prawo wlasciwe)
   - Options: Yes -- Polish law (tak, prawo polskie), No -- different law (nie, inne prawo
     -- specify), Not sure -- let you identify it (nie jestem pewien)
   - _Why this matters_: This skill is optimized for Polish law. If a different law governs,
     recommend the appropriate skill variant.

4. **Risk tolerance**: How should borderline items be classified? (Tolerancja ryzyka)
   - Options: Conservative / zachowawcze (flag more, safer), Pragmatic / pragmatyczne
     (flag only material items), Let me decide case by case (decyduje indywidualnie)
   - _Why this matters_: A kara umowna that is RED for a risk-averse enterprise may be
     YELLOW for a startup that needs the deal.

If the user provides partial context, proceed with reasonable defaults but **state
assumptions explicitly** (e.g., "Zakladam, ze to wzajemna NDA do rozmow wstepnych -- prosze
o potwierdzenie, jesli to nieprawidlowe"). Do not silently assume.

### Step 3: Load the NDA Playbook

Check for the organization's NDA screening criteria in local settings (e.g.,
`legal.local.md` or similar configuration files).

The NDA playbook should define:

- Mutual vs. unilateral requirements
- Acceptable term lengths
- Required carveouts
- Prohibited provisions
- Organization-specific requirements (e.g., standard form NDA for counterproposals)
- Routing rules (who reviews YELLOW, who reviews RED)
- Kary umowne policy (organization's position on contractual penalties in NDAs)

**If no NDA playbook is configured:**

**CLARIFY** -- Inform the user that no playbook was found, and ask:

- **Option A: Set up a playbook now** -- Define the organization's NDA positions for key
  criteria (acceptable terms, required carveouts, prohibited provisions, kary umowne
  position). Takes a few minutes but makes this and all future triages more precise.
- **Option B: Proceed with general market standards** -- Use the default criteria below.
  Faster, but may not reflect the organization's specific risk appetite.
- **Option C: I'll provide positions as we go** -- Start the triage and I'll ask when
  your preferred position matters.

**Default Standards** (when no playbook is configured):

- Mutual obligations required unless the organization is only disclosing
- Term: 1-3 years standard; confidentiality survival: 2-5 years
- All 5 standard carveouts required (public knowledge, prior possession, independent
  development, third-party receipt, legal compulsion)
- No non-solicitation, non-compete, exclusivity, or standstill provisions
- No residuals clause (or narrowly scoped if present)
- No IP assignment or license grants
- Polish law as governing law for agreements between Polish parties; reasonable commercial
  jurisdiction for international agreements
- Return/destruction with retention exception for legal/compliance copies
- No kary umowne, or if present, mutual and in reasonable amounts
- Parties properly identified with full company name (firma), KRS/NIP numbers, and
  authorized representatives

Clearly label when defaults are being used: "Na podstawie ogolnych standardow rynkowych
i prawa polskiego -- nie na podstawie playbooka organizacji."

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Read the NDA's governing law clause and confirm it specifies Polish law (prawo polskie).

**CLARIFY** -- If any of the following are true, ask the user before proceeding:

- **No governing law clause found**: Ask which jurisdiction the user expects to apply,
  and flag the absence as a RED item. Note that under Polish private international law
  (Regulation Rome I), the applicable law for contractual obligations may be determined by
  characteristic performance or party agreement.
- **Governing law is not Polish**: Confirm whether the user wants analysis under Polish
  law anyway, or recommend the appropriate skill variant. If the NDA between two Polish
  entities is governed by a foreign law, flag this as unusual.

**With legalcode-mcp connected (preferred):**

- Search for current text of: Art. 353^1, 72^1, 415, 471, 483-485 KC; Art. 11, 18 UZNK;
  Art. 101^1-101^4 KP; Art. 730, 730^1, 755 KPC
- Search for recent Sad Najwyzszy (Supreme Court) rulings on: miarkowanie kar umownych,
  tajemnica przedsiebiorstwa, zabezpieczenie roszczen in confidentiality cases
- Save results to a local temp file (`/tmp/legalcode-nda-triage-pl-authority.md`)
- Reference verified authority throughout the screening
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark every statutory and case law reference with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with general commercial knowledge of Polish law, but flag that legal authority
  has not been independently verified against current statutory text
- Focus the analysis on structural screening rather than legal certainty

### Step 5: NDA Screening

Read the **entire NDA** before flagging issues -- clauses interact with each other (e.g.,
a broad definition may be partially mitigated by strong carveouts, or a residuals clause
may be offset by a trade secret exception).

Evaluate the NDA against each of the 10 screening criteria systematically:

#### Criterion 1: Agreement Structure

- [ ] **Type identified**: Mutual NDA (NDA wzajemna), Unilateral -- disclosing party
      (jednostronna -- strona ujawniajaca), or Unilateral -- receiving party (jednostronna --
      strona otrzymujaca)
- [ ] **Appropriate for context**: Is the NDA type appropriate for the business
      relationship? (e.g., mutual for exploratory discussions, unilateral for one-way
      disclosures)
- [ ] **Standalone agreement**: Confirm the NDA is a standalone agreement, not a
      confidentiality section embedded in a larger commercial agreement (klauzula poufnosci
      w umowie ramowej)
- [ ] **Party identification**: Are parties correctly identified? Under Polish law, check:
  - Full company name (firma) as registered in KRS
  - KRS number (for entities registered in the National Court Register) or NIP (tax ID)
  - Authorized representatives (osoby uprawnione do reprezentacji) -- verify representation
    per KRS or power of attorney (pelnomocnictwo)
  - For spolka z o.o. (sp. z o.o.) -- check whether the management board acts jointly or
    individually per the articles of association (umowa spolki)

#### Criterion 2: Definition of Confidential Information

- [ ] **Reasonable scope**: Not overbroad (avoid "wszelkie informacje jakiegokolwiek
      rodzaju, niezaleznie od oznaczenia jako poufne" / "all information of any kind whether
      or not marked as confidential")
- [ ] **Alignment with UZNK trade secret definition**: Check whether the NDA's definition
      aligns with Art. 11 s.2 UZNK, which defines a trade secret (tajemnica przedsiebiorstwa)
      as technical, technological, organizational, or other commercially valuable information
      that is (a) not publicly available and (b) for which the entrepreneur has taken necessary
      steps to maintain confidentiality. Where the NDA's definition is broader than UZNK,
      note the divergence. Where narrower, flag that UZNK may provide supplementary
      protection.
- [ ] **Marking requirements**: If marking is required, is it workable? (Written marking
      within 30 days of oral disclosure is standard)
- [ ] **Exclusions present**: Standard exclusions defined (see Criterion 4)
- [ ] **No problematic inclusions**: Does not define publicly available information or
      independently developed materials as confidential
- [ ] **Alignment with purpose**: Definition is tied to the stated purpose (cel umowy),
      not unlimited

#### Criterion 3: Obligations of Receiving Party

- [ ] **Standard of care**: Reasonable care (nalezyta starannosc, Art. 355 KC) or at
      least the same care as for own confidential information. For professional entities,
      note that Art. 355 s.2 KC applies a heightened standard of care (starannosc wymagana
      w stosunkach danego rodzaju z uwzglednieniem zawodowego charakteru dzialalnosci).
- [ ] **Use restriction**: Limited to the stated purpose (cel)
- [ ] **Disclosure restriction**: Limited to those with need to know (osoby z uzasadniona
      potrzeba poznania) who are bound by similar obligations
- [ ] **No onerous obligations**: No impractical requirements (e.g., encrypting all
      communications, maintaining physical logs of every disclosure)
- [ ] **Incident reporting**: Reasonable breach notification obligation (if included)
- [ ] **Consistency with UZNK**: Obligations should not be less protective than the
      statutory protection under Art. 11 UZNK. An NDA that waives or limits UZNK protection
      is problematic (RED).

#### Criterion 4: Standard Carveouts

All of the following carveouts (wylaczenia) should be present:

- [ ] **Public knowledge** (wiedza publiczna): Information that is or becomes publicly
      available through no fault of the receiving party
- [ ] **Prior possession** (wczesniejsze posiadanie): Information already known to the
      receiving party before disclosure
- [ ] **Independent development** (niezalezne opracowanie): Information independently
      developed without use of or reference to confidential information
- [ ] **Third-party receipt** (otrzymanie od osoby trzeciej): Information rightfully
      received from a third party without restriction
- [ ] **Legal compulsion** (przymus prawny): Right to disclose when required by law,
      regulation, court order, or administrative proceedings (with notice to the disclosing
      party where legally permitted). Under Polish law, this includes obligations to disclose
      to the KNF (Financial Supervision Authority), UOKiK (Competition Authority), tax
      authorities, prosecutors, and courts.

#### Criterion 5: Permitted Disclosures

- [ ] **Employees** (pracownicy): Can share with employees who need to know
- [ ] **Contractors/advisors** (wspolpracownicy/doradcy): Can share with contractors,
      advisors, and professional consultants under similar confidentiality obligations
- [ ] **Affiliates** (podmioty powiazane / grupa kapitalowa): Can share with affiliates /
      group companies (if needed for the business purpose)
- [ ] **Legal/regulatory** (organy): Can disclose as required by law, regulation, or
      regulatory authority (KNF, UOKiK, NIK, etc.)
- [ ] **Professional advisors** (doradcy profesjonalni): Can share with legal counsel
      (radca prawny, adwokat), auditors (biegli rewidenci), and accountants under professional
      duties of confidence. Note: Polish radca prawny and adwokat are bound by statutory
      professional secrecy (tajemnica zawodowa) that is independent of contractual NDA
      obligations.

#### Criterion 6: Term and Duration

- [ ] **Agreement term** (okres obowiazywania): Reasonable period for the business
      relationship (1-3 years is standard)
- [ ] **Confidentiality survival** (przezywalnosc obowiazku poufnosci): Obligations survive
      for a reasonable period after termination (2-5 years is standard; trade secrets may be
      longer)
- [ ] **Not perpetual** (nie bezterminowa): Avoid indefinite or perpetual confidentiality
      obligations. Under Art. 353^1 KC, perpetual contractual obligations may be challenged
      as contrary to the nature of the obligation (natura zobowiazania). However, for trade
      secrets, Art. 11 UZNK provides independent statutory protection that persists as long as
      the information qualifies as a trade secret -- so a perpetual NDA clause adds little
      beyond what UZNK already provides.
- [ ] **Termination mechanism**: Under Polish law, contracts for an indefinite term
      (bezterminowe) may generally be terminated with reasonable notice (Art. 365^1 KC). If the
      NDA is intended to be perpetual, confirm this aligns with the parties' intent and that
      termination provisions are included.

#### Criterion 7: Return and Destruction

- [ ] **Obligation triggered**: On termination or upon request (po rozwiazaniu lub na
      zadanie)
- [ ] **Reasonable scope**: Return or destroy confidential information and all copies
- [ ] **Retention exception** (wyjatek retencyjny): Allows retention of copies required
      by law, regulation, or internal compliance/backup policies. Under Polish law, retention
      may be required by tax law (Ordynacja podatkowa -- 5-year retention), accounting law
      (Ustawa o rachunkowosci), RODO/GDPR, and sector-specific regulations.
- [ ] **Certification**: Written certification (pisemne potwierdzenie) of destruction is
      reasonable; a sworn statement (oswiadczenie pod przysiega) or notarial deed (akt
      notarialny) is onerous and non-standard.

#### Criterion 8: Remedies

- [ ] **Interim measures / injunctive relief** (zabezpieczenie roszczen): Acknowledgment
      that breach may justify interim measures under Art. 730 et seq. KPC is standard. Under
      Polish law, the applicant must demonstrate the claim and legal interest in securing it
      (Art. 730^1 KPC). Contractual acknowledgment of irreparable harm does not bind Polish
      courts but may support the application. Note: Polish law does not use the common law
      "irreparable harm" test -- the standard is uprawdopodobnienie roszczenia i interes
      prawny w udzieleniu zabezpieczenia.
- [ ] **Kary umowne (contractual penalties)**: Assess any contractual penalty clause under
      Art. 483-485 KC:
  - Kary umowne may only be stipulated for non-monetary obligations (zobowiazania
    niepieniezne). Confidentiality is a non-monetary obligation, so kary umowne are
    permissible.
  - Check whether the NDA preserves the right to claim supplementary damages
    (odszkodowanie przenoszace kare, Art. 484 s.1 KC in fine). If the NDA caps liability
    at the kara umowna amount without allowing supplementary claims, flag this -- the
    obligee may be limited to the penalty amount even if actual damages exceed it.
  - Assess proportionality: grossly excessive penalties (razaco wygorowane) are subject to
    judicial reduction (miarkowanie) under Art. 484 s.2 KC. Recent Sad Najwyzszy (Supreme
    Court) jurisprudence (including the 19 January 2024 ruling) confirms there is no closed
    catalog of circumstances for miarkowanie -- courts consider the ratio of penalty to
    contract value, nature and duration of violation, debtor's potential benefits from
    breach, and parties' intent regarding punitive character.
  - The Supreme Court ruling of 31 October 2025 (III CZP 22/25) further established that
    clauses limiting liability solely to a low contractual penalty without allowing
    supplementary damages may constitute abusive provisions (klauzule abuzywne) in certain
    contexts.
- [ ] **Not one-sided** (nie jednostronne): Remedies provisions apply equally to both
      parties (in mutual NDAs)
- [ ] **UZNK remedies preserved**: The NDA should not waive or limit claims under Art. 18
      UZNK (cessation, removal of effects, damages, surrender of unjust enrichment). Such
      waiver could be challenged as contrary to Art. 353^1 KC (limits of freedom of contract).

#### Criterion 9: Problematic Provisions to Flag

- [ ] **No non-solicitation** (brak zakazu pozyskiwania pracownikow): NDA should not
      contain employee non-solicitation provisions. In Polish law, such clauses in an NDA
      context may be challenged as exceeding the purpose of the agreement. Under Art. 101^1-
      101^4 KP, non-compete (including non-solicitation) obligations for employees require:
      (a) a separate written agreement, (b) specification of the restriction period, and
      (c) for post-employment restrictions, compensation of at least 25% of prior salary.
      A non-solicitation clause buried in an NDA does not meet these requirements.
- [ ] **No non-compete** (brak zakazu konkurencji): NDA should not contain non-compete
      provisions. Under Polish law, post-employment non-compete requires a separate agreement
      with compensation (Art. 101^2 KP). Embedding such provisions in an NDA without
      compensation is likely unenforceable and creates legal uncertainty. For non-employee
      commercial relationships, a non-compete in an NDA may be challenged under Art. 353^1 KC
      as contrary to the nature of a confidentiality agreement.
- [ ] **No exclusivity** (brak wylacznosci): NDA should not restrict either party from
      entering similar discussions with others
- [ ] **No standstill**: NDA should not contain standstill or similar restrictive
      provisions (unless M&A context -- ask if unclear)
- [ ] **No residuals clause** (brak klauzuli residuals) or narrowly scoped: If present,
      must be limited to information retained in unaided memory of individuals who had
      authorized access; must not apply to trade secrets (tajemnice przedsiebiorstwa) or
      patentable information; must not grant an IP license. A broad residuals clause may
      conflict with Art. 11 UZNK protection.
- [ ] **No IP assignment or license** (brak przeniesienia/licencji IP): NDA should not
      grant any intellectual property rights
- [ ] **No audit rights** (brak prawa audytu): Unusual in standard NDAs; flag if present
- [ ] **Assignment clause** (cesja): Check whether the NDA allows assignment without
      consent. Under Art. 509 KC, claims may be assigned unless prohibited by statute,
      contract, or the nature of the obligation.
- [ ] **RODO/GDPR interaction**: If confidential information may include personal data
      (dane osobowe), flag the need to assess whether a separate Data Processing Agreement
      (umowa powierzenia przetwarzania danych, Art. 28 RODO/GDPR) is required.

#### Criterion 10: Governing Law and Jurisdiction

- [ ] **Polish law preferred**: For agreements between Polish parties, Polish law (prawo
      polskie) should be the standard governing law. For international NDAs, Polish law is
      still acceptable but alternatives may be appropriate.
- [ ] **Consistent**: Governing law and jurisdiction should be aligned -- Polish law with
      Polish court jurisdiction.
- [ ] **Court jurisdiction** (wlasciwosc sadu): Verify jurisdiction clause. Under Polish
      law, the general rule is the court of the defendant's seat (Art. 27 KPC). Prorogation
      agreements (umowa prorogacyjna, Art. 46 KPC) designating a specific court are
      permissible.
- [ ] **Dispute resolution**: For domestic NDAs, litigation before Polish common courts
      (sady powszechne) is generally preferred. Arbitration (sad polubowny) is more appropriate
      for international NDAs (enforcement under the New York Convention). If arbitration is
      specified, check whether the arbitration institution and rules are reasonable (e.g.,
      Sad Arbitrazowy przy KIG, ICC, LCIA).
- [ ] **Exclusive vs. non-exclusive** (wylaczna vs. niewylaczna): Exclusive jurisdiction
      is generally preferred (prevents parallel proceedings).

### Step 6: Classify

Based on the screening results, assign a classification using the rules below:

#### GREEN -- Standard Approval (Standardowe zatwierdzenie)

**All** of the following must be true:

- NDA is mutual (or unilateral in the appropriate direction for the relationship)
- All 5 standard carveouts are present
- Term is within standard range (1-3 years, survival 2-5 years)
- No non-solicitation, non-compete, exclusivity, or standstill provisions
- No residuals clause, or residuals clause is narrowly scoped
- Polish law as governing law (or reasonable jurisdiction for international NDAs)
- Standard remedies (no kary umowne, or kary umowne mutual and reasonable)
- Permitted disclosures include employees, contractors, advisors, and professional advisors
- Return/destruction provisions include retention exception for legal/compliance
- Definition of confidential information is reasonably scoped and tied to purpose
- Definition aligns with or complements Art. 11 s.2 UZNK
- Parties properly identified with KRS/NIP and authorized representatives

**Confidence required**: HIGH (0.80+) -- Confident this meets all standard criteria.

**Routing**: Approve via standard delegation of authority. No counsel review required.
Same-day turnaround.

#### YELLOW -- Counsel Review Needed (Wymagany przeglad prawnika)

**One or more** of the following are present, but the NDA is not fundamentally
problematic:

- Definition of confidential information is broader than preferred but not unreasonable
- Term is longer than standard but within market range (e.g., 5 years agreement term,
  7 years survival)
- Missing one standard carveout that could be added without difficulty
- Residuals clause present but narrowly scoped to unaided memory
- Governing law in an acceptable but non-preferred jurisdiction (e.g., German law,
  English law for international NDA)
- Minor asymmetry in a mutual NDA (e.g., one party has slightly broader permitted
  disclosures)
- Kary umowne present but in reasonable amounts and mutual
- Marking requirements present but workable
- Return/destruction lacks explicit retention exception (likely implied but should be
  added)
- Unusual but non-harmful provisions (e.g., obligation to notify of potential breach)
- Non-exclusive jurisdiction clause when exclusive would be preferred
- Arbitration where litigation would be preferred (or vice versa)
- Minor representation issues (e.g., power of attorney referenced but not attached)

**Confidence required**: PROBABLE (0.60+) -- Issues identified but could be wrong about
materiality. If confidence is below 0.60, flag for counsel review regardless.

**Routing**: Flag specific issues for counsel review (radca prawny). Counsel can likely
resolve with minor redlines in a single review pass. Target: 1-2 business days.

#### RED -- Significant Issues (Istotne problemy)

**One or more** of the following are present:

- **Unilateral when mutual is required** (or wrong direction for the relationship)
- **Missing critical carveouts** (especially independent development or legal compulsion)
- **Non-solicitation or non-compete provisions** embedded in the NDA without meeting KP
  requirements (separate agreement, compensation for post-employment)
- **Exclusivity or standstill provisions** without appropriate business context
- **Unreasonable term** (10+ years, or perpetual without trade secret justification)
- **Overbroad definition** that could capture public information or independently
  developed materials, or that conflicts with UZNK definition
- **Broad residuals clause** that effectively creates a license to use confidential
  information, potentially undermining Art. 11 UZNK protection
- **IP assignment or license grant** hidden in the NDA
- **Grossly excessive kary umowne** (razaco wygorowane) that create disproportionate
  exposure, or one-sided penalty clauses
- **Kary umowne capping liability** without allowing supplementary damages, combined with
  low penalty amounts (per SN III CZP 22/25 reasoning)
- **Audit rights** without reasonable scope or notice requirements
- **Highly unfavorable jurisdiction** or mandatory arbitration in a problematic forum
- **The document is not actually an NDA** (contains substantive commercial terms,
  exclusivity, or other obligations beyond confidentiality)
- **Assignment clause** allowing the counterparty to assign obligations without consent
- **Clauses waiving or limiting UZNK Art. 11 protection** -- such waiver is likely
  contrary to Art. 353^1 KC (limits of freedom of contract)
- **Clauses contrary to mandatory provisions of Polish law** (przepisy bezwzglednie
  obowiazujace), including provisions of KP on non-compete
- **Representation defects**: signatories lack authority per KRS, or entity not properly
  identified

**Confidence required**: HIGH (0.80+) -- Confident the issue is material. If confidence
is below 0.80, classify as YELLOW and flag for counsel review rather than RED. It is
better to send a borderline item for review than to escalate unnecessarily.

**Routing**: Full legal review required (radca prawny / adwokat). Do not sign (nie
podpisywac). Requires negotiation, counterproposal with the organization's standard form
NDA, or rejection. Target: 3-5 business days.

### Step 7: Generate Common Issue Analysis

For each YELLOW or RED finding, provide actionable analysis:

#### Common NDA Issues and Standard Positions (Polish Law)

**Issue: Overbroad Definition of Confidential Information**

- **Standard position**: Confidential information should be limited to non-public
  information disclosed in connection with the stated purpose, with clear exclusions. The
  definition should be consistent with Art. 11 s.2 UZNK (tajemnica przedsiebiorstwa).
- **Polish law context**: Art. 11 s.2 UZNK requires that the entrepreneur has taken
  "necessary steps" (niezbedne kroki) to maintain confidentiality. An NDA with an
  overbroad definition that does not distinguish between protected and unprotected
  information may actually weaken the UZNK protection argument.
- **Redline approach**: Narrow the definition to information that is marked or identified
  as confidential, or that a reasonable person would understand to be confidential given
  the nature of the information and circumstances of disclosure.
- **Priority**: Tier 2 (Should-Have)

**Issue: Missing Independent Development Carveout**

- **Standard position**: Must include a carveout for information independently developed
  without reference to or use of the disclosing party's confidential information.
- **Risk if missing**: Could create claims that internally-developed products or features
  were derived from the counterparty's confidential information. Under Art. 471 KC, the
  receiving party bears the burden of proving the exception.
- **Redline approach**: Add standard independent development carveout.
- **Priority**: Tier 1 (Must-Have) -- Missing this carveout is RED.

**Issue: Non-Solicitation of Employees in NDA**

- **Standard position**: Non-solicitation provisions do not belong in NDAs. Under Polish
  law, non-compete obligations (including non-solicitation) for employees are governed by
  Art. 101^1-101^4 KP and require: (a) a separate written agreement under penalty of
  invalidity, (b) for post-employment restrictions, compensation of at least 25% of prior
  salary. Embedding such provisions in an NDA without these requirements creates legal
  uncertainty and is likely unenforceable.
- **Redline approach**: Delete the provision entirely. If the counterparty insists, the
  provision must be structured as a separate agreement meeting KP requirements (with
  compensation).
- **Priority**: Tier 1 (Must-Have) -- This is always RED in an NDA context under Polish
  law.

**Issue: Broad Residuals Clause**

- **Standard position**: Resist residuals clauses. If required, limit to: (a) general
  ideas, concepts, know-how, or techniques retained in the unaided memory of individuals
  who had authorized access; (b) explicitly exclude trade secrets (tajemnice
  przedsiebiorstwa) in the meaning of Art. 11 UZNK and patentable information; (c) does
  not grant any IP license.
- **Polish law risk**: A broad residuals clause may undermine the "necessary steps"
  requirement under Art. 11 s.2 UZNK, weakening statutory trade secret protection.
- **Redline approach**: Narrow to unaided memory with tajemnica przedsiebiorstwa and IP
  carveouts.
- **Priority**: Tier 1 if broad (RED), Tier 2 if narrowly scoped (YELLOW).

**Issue: Perpetual Confidentiality Obligation**

- **Standard position**: 2-5 years from disclosure or termination, whichever is later.
  Trade secrets may warrant protection for as long as they remain trade secrets.
- **Polish law context**: Art. 11 UZNK provides independent statutory protection for trade
  secrets regardless of NDA duration. Under Art. 353^1 KC, perpetual contractual
  obligations may be challenged as contrary to the nature of the obligation. Art. 365^1 KC
  allows termination of indefinite-term obligations with reasonable notice.
- **Redline approach**: Replace perpetual obligation with a defined term. Add a separate
  clause for trade secrets referencing UZNK protection.
- **Priority**: Tier 2 (Should-Have) unless term is truly unreasonable (10+ years = RED).

**Issue: Kary Umowne (Contractual Penalties) in NDA**

- **Polish law framework**: Kary umowne (Art. 483-485 KC) are permissible for non-monetary
  obligations, including confidentiality. They serve as pre-agreed damages for breach.
- **Key checks**:
  - Proportionality: Are the amounts proportionate to the potential harm? Grossly excessive
    amounts (razaco wygorowane) are subject to judicial reduction (miarkowanie, Art. 484
    s.2 KC).
  - Supplementary damages: Does the NDA preserve the right to claim odszkodowanie
    przenoszace kare (Art. 484 s.1 KC in fine)? If not, the obligee is limited to the
    penalty amount.
  - Mutuality: In mutual NDAs, kary umowne should apply to both parties symmetrically.
  - Multiple penalties: Check for cumulation of multiple penalties for related breaches.
- **SN jurisprudence**: The Supreme Court (ruling of 19 January 2024) confirmed that
  miarkowanie factors include: ratio of penalty to contract/remuneration value, nature and
  duration of violation, benefits gained from breach, and punitive intent. The ruling of
  31 October 2025 (III CZP 22/25) addressed abusive penalty clauses that cap liability at
  disproportionately low amounts.
- **Standard position**: Kary umowne in NDAs are not market standard in Poland but are
  permissible. If present, they should be mutual, reasonable, and preserve the right to
  supplementary damages.
- **Priority**: Tier 1 (RED) if amounts are disproportionate or one-sided; Tier 2 (YELLOW)
  if amounts are reasonable and mutual.

**Issue: Injunctive Relief Language Using Common Law Concepts**

- **Polish law context**: Polish courts do not apply the common law "irreparable harm" /
  "balance of hardships" test for interim relief. Interim measures (zabezpieczenie roszczen)
  are governed by Art. 730 et seq. KPC, requiring: (a) demonstration of the claim
  (uprawdopodobnienie roszczenia), and (b) legal interest in securing it (interes prawny).
  Contractual acknowledgment of "irreparable harm" (nieodwracalna szkoda) does not bind
  Polish courts.
- **Redline approach**: Replace common law language with a reference to the right to seek
  zabezpieczenie roszczen under Art. 730 KPC, acknowledging that breach may satisfy the
  statutory requirements.
- **Priority**: Tier 2 (YELLOW) -- not legally incorrect but reflects jurisdictional bleed.

### Step 8: Negotiation Priority Framework

Organize findings by negotiation priority:

#### Tier 1 -- Must-Haves (Deal Blockers / Warunki konieczne)

Issues where the organization cannot proceed without resolution:

- Missing critical carveouts (independent development, legal compulsion)
- Non-solicitation or non-compete provisions not meeting KP requirements
- Broad residuals clause that creates an effective IP license or undermines UZNK protection
- IP assignment or license hidden in the NDA
- Document is not actually an NDA (embedded commercial terms)
- Grossly excessive or one-sided kary umowne
- Clauses waiving UZNK Art. 11 protection
- Representation defects (unauthorized signatories)

#### Tier 2 -- Should-Haves (Strong Preferences / Silne preferencje)

Issues that materially affect risk but have negotiation room:

- Overbroad confidential information definition
- Term adjustments (longer than standard but negotiable)
- Missing retention exception in return/destruction
- Jurisdiction preference
- Marking requirement modifications
- Certification of destruction scope
- Kary umowne amount adjustments
- Common law language replacement with Polish law equivalents
- Missing supplementary damages clause for kary umowne

#### Tier 3 -- Nice-to-Haves (Concession Candidates / Kandydaci do ustepstw)

Issues that improve the position but can be conceded strategically:

- Preferred governing law (if alternative is acceptable)
- Minor asymmetries in mutual NDA
- Notification obligations (unusual but not harmful)
- Specific dispute resolution mechanism preference
- Minor representation formalities (power of attorney attachment)

**Strategy**: Lead with Tier 1 items. Trade Tier 3 concessions to secure Tier 2 wins.
Never concede on Tier 1 without escalation.

### Step 9: Quality Verification

Before delivering the triage report, run the quality checks:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every RED-classified item, run the 3-pass Self-Interrogation. Revise if any pass
   reveals a weakness.
3. Assign a Confidence Score to the overall classification and to each material finding.
4. Verify completeness: confirm all 10 screening criteria have been addressed.
5. Generate the Glass Box Audit Trail and append it to the output.
6. Run the Writing Standards quality gates.

### Step 10: Routing and Delivery

Based on the classification, recommend the appropriate next step:

| Classification | Recommended Action                                                                      | Typical Timeline  |
| -------------- | --------------------------------------------------------------------------------------- | ----------------- |
| GREEN          | Approve and route for signature per delegation of authority                             | Same day          |
| YELLOW         | Send to radca prawny with specific issues flagged                                       | 1-2 business days |
| RED            | Engage radca prawny / adwokat for full review; prepare counterproposal or standard form | 3-5 business days |

For YELLOW and RED classifications:

- Identify the specific person or role that should review (if the organization has defined
  routing rules in the playbook)
- Include a brief summary of issues suitable for the reviewer to quickly understand the
  key points
- If the organization has a standard form NDA, recommend sending it as a counterproposal
  for RED-classified NDAs (reference the `nda-mutual` skill if drafting is needed)
- For international NDAs, note whether the jurisdiction/arbitration position is appropriate
  for enforcement across borders (New York Convention for arbitral awards, Brussels
  Regulation / Lugano Convention for court judgments within the EU/EFTA)

---

## Severity / Status Classification

| Finding Status     | Meaning                  | Action                                         |
| ------------------ | ------------------------ | ---------------------------------------------- |
| **PASS** (OK)      | Criterion met; no issues | No action needed                               |
| **FLAG** (UWAGA)   | Minor deviation; YELLOW  | Generate redline with fallback position        |
| **FAIL** (PROBLEM) | Material deviation; RED  | Escalate with risk explanation and legal basis |

---

## Prioritization Framework Summary

| Priority   | Category      | Examples                                                                                                                 | Negotiation Posture                   |
| ---------- | ------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------- |
| **Tier 1** | Must-Haves    | Missing carveouts, non-compete without KP compliance, IP assignment, broad residuals, excessive kary umowne, UZNK waiver | Non-negotiable; escalate if rejected  |
| **Tier 2** | Should-Haves  | Overbroad definition, term adjustments, retention exception, kary umowne amount, common law language                     | Push firmly; accept fallback          |
| **Tier 3** | Nice-to-Haves | Governing law preference, minor asymmetries, notification obligations                                                    | Concede strategically for Tier 2 wins |

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Identify the NDA type, counterparty, business context, and confirm Polish
governing law. Determine whether a playbook exists. Assess whether any special
considerations apply (M&A context, regulated sector, international counterparty, high-value
relationship, personal data sharing requiring RODO/GDPR assessment).

**DO**: Execute the 10-criteria screening under Polish law. Classify GREEN/YELLOW/RED.
Generate findings with Polish legal basis and suggested fixes. Assign negotiation
priorities.

**CHECK**: Run the Citation Quality Gates. Verify legal claims cite specific KC, UZNK, KP,
or KPC provisions. For RED classifications, run the Self-Interrogation. Confirm all 10
criteria addressed.

**ACT**: If the NDA reveals a new pattern (e.g., a clause structure becoming common in
the Polish market), note it for playbook update. If the organization's standard form NDA
is missing a protection that this NDA exposed, flag for standard form revision.

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                                                                            | Fail Action                                               |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific KC, UZNK, KP, or KPC provision, or established Polish legal principle                                                                                        | Add citation or mark "[UNVERIFIED -- counsel to confirm]" |
| **Format**     | All citations follow Polish legal citation format (e.g., "Art. 484 s.2 KC", "Art. 11 ust. 2 UZNK")                                                                                              | Fix format                                                |
| **Currency**   | Every cited provision checked for amendments against authoritative sources (ISAP, LEX) where accessible                                                                                         | Flag "[CHECK CURRENCY -- may have been amended]"          |
| **Domain**     | Analysis stays within Polish law. No common law concepts leaking in (e.g., "irreparable harm" test, "consideration", "work for hire") without explicit notation that these are foreign concepts | Remove or flag jurisdictional bleed                       |
| **Confidence** | Uncertainty explicitly stated, not hidden. If uncertain, say so                                                                                                                                 | Add confidence qualifier                                  |

### Self-Interrogation for RED Items

For any item classified as RED, apply this 3-pass review before delivering:

**Pass 1 -- Legal Chain Integrity**: Does the risk assessment follow logically from the
cited Polish statutory provision? Would a Polish court (sad powszechny) or the Supreme
Court (Sad Najwyzszy) actually reach this conclusion on these facts? Is there a
counter-argument the counterparty's radca prawny will make?

**Pass 2 -- Completeness**: Have all relevant KC, UZNK, KP, and KPC provisions been
considered? Are there regulatory dimensions not yet addressed (KNF, UOKiK, RODO)? Could
the clause interact with another clause to mitigate or worsen the risk?

**Pass 3 -- Challenge**: What is the strongest argument that this clause IS acceptable
under Polish law? Under what circumstances might a reasonable radca prawny accept this
risk? Is the RED classification proportionate, or is this actually YELLOW with redlines?
Would a commercial practitioner at a leading Polish firm (kancelaria prawna) send this
back, or mark it up and proceed?

If any pass reveals a weakness, revise the analysis before delivery. Mark the audit trail
with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For the overall classification and each material finding, assign a confidence level:

| Level                        | Range     | Meaning                                                         | Action                                                 |
| ---------------------------- | --------- | --------------------------------------------------------------- | ------------------------------------------------------ |
| **Definite** (pewne)         | 0.95-1.0  | Settled Polish law, clear contractual provision, no ambiguity   | State with confidence                                  |
| **High** (wysokie)           | 0.80-0.94 | Strong basis in KC/UZNK/KP, minor interpretation questions      | State with brief caveat                                |
| **Probable** (prawdopodobne) | 0.60-0.79 | Good arguments but reasonable minds could differ                | State with reasoning and contra-indicators             |
| **Possible** (mozliwe)       | 0.40-0.59 | Genuinely uncertain, competing interpretations under Polish law | Flag for counsel review with both sides                |
| **Unlikely** (watpliwe)      | 0.0-0.39  | Weak basis, speculative                                         | Do not assert; flag "[UNCERTAIN -- counsel to advise]" |

---

## Glass Box Audit Trail

Every NDA triage output MUST include a Glass Box audit section at the end:

```yaml
glass_box:
  nda_counterparty: "[Counterparty name]"
  nda_type: "[Mutual / Unilateral -- direction]"
  governing_law: "Polish law (prawo polskie)"
  classification: "GREEN / YELLOW / RED"
  confidence: "HIGH / MEDIUM / LOW -- [rationale]"
  review_basis: "[Organizational playbook / General market standards + Polish law]"
  criteria_screened: 10
  criteria_summary:
    structure: "PASS / FLAG -- [brief note]"
    definition_scope: "PASS / FLAG -- [UZNK alignment note]"
    obligations: "PASS / FLAG"
    carveouts: "PASS / FLAG -- [missing: independent development]"
    permitted_disclosures: "PASS / FLAG"
    term: "PASS / FLAG -- [3 years / 5 years survival]"
    return_destruction: "PASS / FLAG"
    remedies: "PASS / FLAG -- [kary umowne assessment]"
    problematic_provisions: "PASS / FLAG -- [non-compete found / UZNK waiver]"
    governing_law: "PASS / FLAG"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to temp file or 'Not created']"
  statutes_consulted:
    - "Art. 353^1 KC (swoboda umow) -- VERIFIED / UNVERIFIED"
    - "Art. 72^1 KC (poufnosc przedkontraktowa) -- VERIFIED / UNVERIFIED"
    - "Art. 471 KC (odpowiedzialnosc kontraktowa) -- VERIFIED / UNVERIFIED"
    - "Art. 483-485 KC (kary umowne) -- VERIFIED / UNVERIFIED"
    - "Art. 484 s.2 KC (miarkowanie) -- VERIFIED / UNVERIFIED"
    - "Art. 11 UZNK (tajemnica przedsiebiorstwa) -- VERIFIED / UNVERIFIED"
    - "Art. 18 UZNK (roszczenia) -- VERIFIED / UNVERIFIED"
    - "Art. 101^1-101^4 KP (zakaz konkurencji) -- VERIFIED / UNVERIFIED"
    - "Art. 730 KPC (zabezpieczenie roszczen) -- VERIFIED / UNVERIFIED"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted -- requires review by radca prawny or adwokat"
```

---

## Anti-Patterns

What NOT to do in Polish-law NDA triage:

1. **Classifying everything as YELLOW "to be safe"** -- If everything needs counsel
   review, the triage process adds no value. GREEN means GREEN -- approve and sign. Trust
   the framework. The purpose of triage is to route efficiently, not to defer every
   decision.

2. **Missing the embedded commercial agreement** -- The most dangerous NDA is one that
   is not really an NDA. If the document contains IP assignment, exclusivity, non-compete,
   or standstill provisions, it is a commercial agreement wearing NDA clothing. This is
   always RED. Read every clause, not just the title.

3. **Ignoring the business context** -- An NDA for exploratory due diligence in an M&A
   context may legitimately include standstill provisions. The same clause in a sales-
   stage NDA is a RED flag. Context determines whether unusual clauses are appropriate.

4. **Treating all non-standard terms as problems** -- A well-drafted NDA from a reputable
   Polish counterparty may use different language from your standard form but achieve the
   same legal effect. Read for substance, not just form. A 4-year term is not automatically
   YELLOW just because your standard is 3 years.

5. **NDA triage without reading the whole document** -- Scanning the first page and the
   signature block misses the problematic provisions buried in the middle. The non-
   solicitation clause is in Section 8.2, not the preamble (preambuła).

6. **Citing statutes from memory without verification** -- Statutes are amended, repealed,
   and renumbered. Case citations may not exist. If you cannot verify a citation against
   an authoritative source (ISAP, LEX, Legalis), mark it [VERIFY] or "[UNVERIFIED --
   counsel to confirm]." Never present an unverified citation as settled law.

7. **Applying common law concepts to Polish law NDAs** -- "Irreparable harm" is a US/UK
   injunction standard, not Polish law (zabezpieczenie roszczen under Art. 730 KPC applies
   different criteria). "Consideration" does not exist in Polish law. "Work-for-hire"
   exists in the US but not in Polish copyright law (Polish law uses Art. 12 Ustawy o
   prawie autorskim for employer works). Always verify whether a concept applies under
   Polish law before citing it.

8. **Assuming residuals clauses are always bad** -- A narrowly-scoped residuals clause
   (unaided memory, excluding tajemnice przedsiebiorstwa, no IP license) is increasingly
   market-standard in technology transactions. A broad residuals clause is RED --
   particularly because it may undermine Art. 11 UZNK protection. Distinguish.

9. **Flagging injunctive relief language as a material problem** -- While Polish courts
   use different standards for zabezpieczenie roszczen than common law courts use for
   injunctions, a clause acknowledging the right to seek interim relief is not legally
   wrong. This is at most YELLOW (suggest Polish-law-specific language), not RED.

10. **Single-pass analysis** -- A triage that reads each criterion once, in order, will
    miss interactions between clauses. A broad definition may be partially mitigated by
    strong carveouts. An uncapped remedy may be offset by a well-scoped kary umowne clause
    elsewhere. Read the whole NDA, then screen.

11. **Triage without identifying the governing law first** -- A Polish-law NDA requires
    different analysis from an English-law or German-law NDA. Check governing law in the
    first 30 seconds. If it is not Polish law for an expected Polish-law relationship,
    flag immediately -- the user may need to switch to a different skill variant.

12. **Over-engineering the triage output** -- The purpose of NDA triage is to route, not
    to provide full legal analysis. The report should be concise. If the NDA is RED,
    it goes to counsel (radca prawny) -- they do not need a 10-page analysis from the
    triage tool. Be concise.

13. **Ignoring what is NOT in the NDA** -- Focusing only on clauses that are present and
    ignoring absent clauses. An NDA with no independent development carveout, no legal
    compulsion carveout, or no retention exception has material gaps that must be flagged.

14. **Failing to recommend a counterproposal** -- When an NDA is RED, do not just say
    "reject." Recommend the organization's standard form NDA as a counterproposal, or
    reference the `nda-mutual` skill for drafting one.

15. **Ignoring the interaction between NDA and Art. 11 UZNK** -- An NDA does not replace
    UZNK protection; it supplements it. Clauses that waive, limit, or conflict with
    UZNK protection should be flagged as RED. Conversely, UZNK protection survives NDA
    expiry for as long as the information qualifies as a tajemnica przedsiebiorstwa.
    Always assess NDA clauses in light of UZNK.

16. **Overlooking kary umowne miarkowanie risk** -- Simply noting that a kary umowne
    clause is present without assessing proportionality and miarkowanie risk under
    Art. 484 s.2 KC. Always assess: (a) is the penalty proportionate to the potential
    harm? (b) does the NDA preserve supplementary damages? (c) is the penalty mutual or
    one-sided? Recent SN jurisprudence provides clear guidance on miarkowanie criteria.

17. **Failing to check representation and authority** -- Polish law requires that
    signatories have proper authority per the entity's KRS entry or a valid power of
    attorney (pelnomocnictwo). An NDA signed by an unauthorized person is voidable. Always
    verify the counterparty's representation structure (e.g., for a sp. z o.o., does the
    management board act jointly or individually?).

---

## Writing Standards

Apply plain-language discipline to all triage output:

**For the triage report**:

- Plain language. No jargon or filler.
- Use Polish legal terminology alongside English translations where relevant (e.g.,
  "kary umowne (contractual penalties)", "tajemnica przedsiebiorstwa (trade secret)",
  "zabezpieczenie roszczen (interim measures)")
- Active voice: "This NDA contains a zakaz konkurencji clause (Section 8.2)" not "A
  non-compete clause was identified"
- Short sentences. One point per sentence.
- Name the section: cite the specific NDA section reference for each finding
- Specific, not vague: "Remove Section 7.3 (non-solicitation)" not "consider the
  non-solicitation provision"

**For each finding**:

- State what the NDA says (with section reference)
- State what the standard position is under Polish law
- State the risk of accepting the current language (citing KC, UZNK, KP, or KPC)
- State the suggested fix (specific language or approach)

**Quality gates before delivery**:

1. Is the classification (GREEN/YELLOW/RED) clearly stated at the top?
2. Is every FLAG/FAIL supported by a specific section reference in the NDA?
3. Can the routing recipient (radca prawny) understand the issues without reading the
   full NDA?
4. Are legal claims in the rationale backed by specific Polish statutory provisions (or
   flagged [VERIFY])?
5. Is the report concise enough to be actionable?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.
legalcode-mcp is a law, regulatory, and case law database with powerful search across
jurisdictions, including Polish law.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for current text of KC, UZNK, KP, and KPC provisions
- Search for recent Sad Najwyzszy rulings on kary umowne miarkowanie, tajemnica
  przedsiebiorstwa, and zabezpieczenie roszczen
- Save the most relevant results to `/tmp/legalcode-nda-triage-pl-authority.md`
- Reference verified authority throughout the screening
- For RED items, search for additional case law to support or challenge the classification
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Include a notice that legal citations require independent verification against current
  statutory text (recommended sources: ISAP for statutes, LEX/Legalis for case law)
- Focus the analysis on structural screening and commercial risk assessment

---

## Output Format Template

Structure the triage deliverable as:

```markdown
## NDA Triage Report / Raport triazu NDA

**Classification / Klasyfikacja**: [GREEN / YELLOW / RED]
**Confidence / Pewnosc**: [level with numeric range]
**Parties / Strony**: [party names with KRS/NIP]
**Type / Typ**: [Mutual (wzajemna) / Unilateral (jednostronna -- direction)]
**Term / Okres**: [agreement duration] | **Survival / Przezywalnosc**: [confidentiality survival period]
**Governing Law / Prawo wlasciwe**: Polish law (prawo polskie)
**Review Basis / Podstawa przegladu**: [Organizational Playbook / General Market Standards + Polish Law]
**Date / Data**: [date]

---

## Screening Results / Wyniki przesiewu

| #   | Criterion / Kryterium                                       | Status           | Notes / Uwagi            |
| --- | ----------------------------------------------------------- | ---------------- | ------------------------ |
| 1   | Agreement Structure / Struktura umowy                       | [PASS/FLAG/FAIL] | [details]                |
| 2   | Definition Scope / Zakres definicji                         | [PASS/FLAG/FAIL] | [UZNK alignment]         |
| 3   | Receiving Party Obligations / Obowiazki strony otrzymujacej | [PASS/FLAG/FAIL] | [details]                |
| 4   | Standard Carveouts / Standardowe wylaczenia                 | [PASS/FLAG/FAIL] | [details]                |
| 5   | Permitted Disclosures / Dozwolone ujawnienia                | [PASS/FLAG/FAIL] | [details]                |
| 6   | Term and Duration / Okres i czas trwania                    | [PASS/FLAG/FAIL] | [details]                |
| 7   | Return/Destruction / Zwrot/zniszczenie                      | [PASS/FLAG/FAIL] | [details]                |
| 8   | Remedies / Srodki ochrony prawnej                           | [PASS/FLAG/FAIL] | [kary umowne assessment] |
| 9   | Problematic Provisions / Postanowienia problematyczne       | [PASS/FLAG/FAIL] | [details]                |
| 10  | Governing Law/Jurisdiction / Prawo wlasciwe/jurysdykcja     | [PASS/FLAG/FAIL] | [details]                |

---

## Issues Found / Wykryte problemy

### [Issue 1 -- YELLOW/RED] | Section [X.X] | Priority: Tier [1/2/3]

**NDA says / NDA stanowi**: "[exact quote or summary from the NDA]"
**Standard position / Pozycja standardowa**: [what it should say under Polish law]
**Risk / Ryzyko**: [what could go wrong if accepted]
**Legal basis / Podstawa prawna**: [KC/UZNK/KP/KPC provision -- or "[VERIFY]"]
**Suggested fix / Proponowane rozwiazanie**: [specific language or approach]
**Fallback / Pozycja awaryjna**: [alternative if primary fix is rejected]
**Confidence / Pewnosc**: [level]

[Repeat for each issue]

---

## Recommendation / Rekomendacja

[Specific next step: approve, send for review with specific notes, or reject/counter]

---

## Negotiation Priority / Priorytety negocjacyjne

**Tier 1 (Must-Haves / Warunki konieczne)**: [list]
**Tier 2 (Should-Haves / Silne preferencje)**: [list]
**Tier 3 (Concession Candidates / Kandydaci do ustepstw)**: [list]

---

## Next Steps / Kolejne kroki

1. [Action item 1]
2. [Action item 2]
3. [Action item 3]

---

## Glass Box Audit Trail

[YAML block per Glass Box section above]
```

---

## Localization Notes

This skill is a Poland-specific localization of the jurisdiction-agnostic
`legalcode-nda-triage` skill. It replaces all [JURISDICTION-SPECIFIC] markers with
Polish law content and all [VERIFY] tags with specific KC, UZNK, KP, and KPC references.

### Poland-Specific Screening Additions (vs. Base Template)

1. **Kary umowne analysis** (Art. 483-485 KC): Full assessment of contractual penalty
   clauses including proportionality, miarkowanie risk under Art. 484 s.2 KC,
   supplementary damages preservation, and recent SN jurisprudence.
2. **UZNK Art. 11 alignment**: Every NDA definition is assessed against the statutory
   trade secret definition. Clauses that waive or undermine UZNK protection are flagged.
3. **Freedom of contract limits** (Art. 353^1 KC): Clauses that contradict the nature of
   the obligation, statute, or zasady wspolzycia spolecznego are flagged as potentially
   unenforceable.
4. **Non-compete compensation requirement** (Art. 101^1-101^4 KP): Non-compete and
   non-solicitation provisions in NDAs are assessed against KP requirements for separate
   agreement, written form, and compensation.
5. **Representation verification**: Assessment of party identification against KRS/NIP
   requirements and signatory authority.
6. **RODO/GDPR interaction**: Flag when NDA data sharing may require a separate Data
   Processing Agreement.
7. **Pre-contractual confidentiality** (Art. 72^1 KC): Note that Polish law provides
   baseline confidentiality protection even without an NDA.

### Localization Checklist (Completed)

- [x] Select governing law: Polish law (prawo polskie)
- [x] Validate injunctive relief language: zabezpieczenie roszczen under Art. 730 KPC
- [x] Validate confidentiality duration: Art. 353^1, 365^1 KC; Art. 11 UZNK for trade
      secrets
- [x] Check non-compete/non-solicitation enforceability: Art. 101^1-101^4 KP
- [x] Verify penalty/liquidated damages doctrine: Art. 483-485 KC, miarkowanie under
      Art. 484 s.2 KC
- [x] Confirm evidentiary and signature formalities: KRS representation, pelnomocnictwo
- [x] Add local legal terminology alongside English translations

---

## Provenance

Created by Legalcode (2026-02-27). Poland localization of `legalcode-nda-triage`,
incorporating Polish law content from:

- **legalcode-nda-triage** (base template) -- jurisdiction-agnostic 10-criteria checklist,
  quality frameworks (PDCA, Glass Box, Citation Quality Gates, Self-Interrogation,
  Confidence Scoring), anti-patterns, writing standards, interactive CLARIFY points,
  negotiation priority framework
- **iura-ai/IURA-Plugins** (`iura-pl nda-triage` skill and `triage-nda` command) -- Polish
  law context (KC, UZNK, KP provisions), Polish legal terminology, anti-hallucination
  warnings, kary umowne analysis, UZNK trade secret framework

Polish law research verified against: Kodeks cywilny (consolidated text per Dz.U. 2024
poz. 1061), Ustawa o zwalczaniu nieuczciwej konkurencji (as amended 4 September 2018),
Kodeks pracy (Art. 101^1-101^4), Kodeks postepowania cywilnego (Art. 730 et seq.),
Sad Najwyzszy jurisprudence on miarkowanie kar umownych (2024-2025).
