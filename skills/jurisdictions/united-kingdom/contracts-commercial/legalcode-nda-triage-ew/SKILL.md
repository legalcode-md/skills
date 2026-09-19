---
name: legalcode-nda-triage-ew
description: Screen and triage incoming NDAs under the laws of England and Wales — classify as GREEN (standard
  approval), YELLOW (solicitor review), or RED (significant issues) with confidence-scored, auditable
  analysis. Applies English law tests for enforceability, including the American Cyanamid injunction test,
  Cavendish Square penalty doctrine, restraint of trade doctrine (Nordenfelt / Egon Zehnder v Tillman),
  Trade Secrets Regulations 2018, and the common law doctrine of breach of confidence (Coco v AN Clark).
  Use when a new NDA arrives governed by English law, when assessing NDA risk for a UK-based organisation,
  when deciding whether an NDA needs solicitor review, or when routing NDAs through an in-house legal
  workflow. Produces a structured triage report with Glass Box audit trail.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode NDA Triage -- England & Wales

> **Disclaimer**: This skill provides a framework for AI-assisted NDA screening under the
> laws of England and Wales. It does not constitute legal advice. All outputs should be
> reviewed by a qualified solicitor admitted in England and Wales before use. Laws change;
> verify current applicability before relying on any provision described here. Statutory and
> case law references cited from memory carry hallucination risk -- verify against
> authoritative sources before relying on them.

## Purpose and Scope

This skill rapidly screens incoming non-disclosure agreements governed by, or expected to be
governed by, the laws of England and Wales. It classifies NDAs by risk level (GREEN / YELLOW
/ RED), generates actionable findings with suggested fixes grounded in English law authority,
and produces a confidence-scored, auditable triage report with routing recommendations.

**Covers:**

- Mutual and unilateral NDAs (standalone agreements)
- Confidentiality sections embedded in larger commercial agreements (with caveats)
- NDAs governed by the laws of England and Wales
- NDAs where English law is expected but the governing law clause is missing or different
- Playbook-based or general-standard screening
- Quality-verified output with Glass Box audit trail

**Does not:**

- Draft new NDAs (see the `nda-mutual` skill for drafting)
- Perform full contract review (see `legalcode-contract-review` for comprehensive review)
- Provide legal advice or replace qualified solicitors
- Apply to NDAs governed by Scots law, Northern Ireland law, or any non-English jurisdiction
  (use the jurisdiction-agnostic `legalcode-nda-triage` for other governing laws)

## Governing Law: England and Wales

This skill applies the laws of England and Wales exclusively. The legal framework includes:

**Statutory framework:**

- Trade Secrets (Enforcement, etc.) Regulations 2018 (SI 2018/597) -- implementing EU
  Directive 2016/943, providing statutory remedies for trade secret misappropriation
  including injunctions, damages, and seizure of infringing goods. Limitation period: 6
  years from the date of the unlawful acquisition, use, or disclosure.
- Victims and Prisoners Act 2024, s.17 -- from 1 October 2025, NDAs are unenforceable to
  the extent they prevent victims of crime from disclosing information about relevant
  conduct to police, solicitors, regulated healthcare professionals, or victim support
  services. Commercial NDAs must include carve-outs to comply.
- Higher Education (Freedom of Speech) Act 2023 -- from 1 August 2025, higher education
  providers cannot use NDAs in handling complaints of sexual harassment, abuse, or bullying.

**Common law framework:**

- Breach of confidence doctrine: _Coco v AN Clark (Engineers) Ltd_ [1969] RPC 41 --
  three-part test: (1) the information must have the necessary quality of confidence,
  (2) it must have been imparted in circumstances importing an obligation of confidence,
  (3) there must be unauthorised use to the detriment of the confiding party.
- Confidential information definition: _Saltman Engineering Co v Campbell Engineering Co
  Ltd_ (1948) 65 RPC 203 -- information has the "necessary quality of confidence" if it is
  not public property or public knowledge; the result of work by the maker on materials
  available to all can still be confidential.
- Trade secret classification: _Faccenda Chicken Ltd v Fowler_ [1987] Ch 117 --
  distinguishes three categories: (1) trivial information, (2) confidential information
  protectable during employment, (3) trade secrets protectable after employment ends.

**Injunctive relief:**

- _American Cyanamid Co v Ethicon Ltd_ [1975] AC 396 (HL) -- the test for interim
  injunctions: (1) is there a serious question to be tried? (2) would damages be an
  adequate remedy? (3) where does the balance of convenience lie? (4) if the balance is
  even, preserve the status quo.
- _NWL Ltd v Woods_ [1979] 1 WLR 1294 -- the court may consider the merits more closely
  where the injunction would effectively determine the dispute.

**Penalty doctrine:**

- _Cavendish Square Holding BV v Makdessi / ParkingEye Ltd v Beavis_ [2015] UKSC 67 --
  a clause is an unenforceable penalty if it imposes a detriment on the contract-breaker
  out of all proportion to any legitimate interest of the innocent party in enforcement of
  the primary obligation. This replaced the older _Dunlop Pneumatic Tyre Co Ltd v New
  Garage and Motor Co Ltd_ [1915] AC 79 "genuine pre-estimate of loss" test.

**Restraint of trade:**

- _Nordenfelt v Maxim Nordenfelt Guns and Ammunition Co Ltd_ [1894] AC 535 -- a restraint
  of trade must (a) protect a legitimate business interest, (b) be no wider than reasonably
  necessary, and (c) not be contrary to the public interest.
- _Egon Zehnder Ltd v Tillman_ [2019] UKSC 32 -- confirmed the restraint of trade doctrine
  applies to all post-termination restrictions; established the modern severance test: (1)
  the unenforceable provision is capable of being removed without adding to or modifying
  what remains (blue pencil test), (2) remaining terms are supported by adequate
  consideration, (3) removal does not change the character of the contract.

**Pending reform (monitor):**

- The UK Government published a working paper on 26 November 2025 consulting on reform of
  non-compete clauses in employment contracts, including options for statutory duration
  limits (3-6 months), outright bans, or salary-threshold restrictions. Consultation closed
  18 February 2026. No legislation enacted yet. This may affect non-compete provisions
  found in NDAs in the employment context.

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

1. **Which side are you on?**
   - Options: Receiving party, Disclosing party, Both (mutual NDA), Not sure
   - _Why this matters_: Determines which protections to scrutinise -- a receiving party
     needs strong carveouts and reasonable obligations; a disclosing party needs broad
     protection scope and strong remedies.

2. **Business context**: What is the purpose of this NDA?
   - Options: Exploratory / pre-sales discussions, Vendor evaluation, M&A due diligence,
     Technology evaluation / proof of concept, Employment / contractor, Other
   - _Why this matters_: An M&A NDA may legitimately include standstill provisions; a
     sales-stage NDA should not. Context determines whether unusual clauses are appropriate.

3. **Governing law confirmation**: Is this NDA governed by the laws of England and Wales?
   - Options: Yes / confirmed English law, Not sure -- I'll let you identify it, The NDA
     states a different governing law (specify)
   - _Why this matters_: This skill applies English law exclusively. If the NDA is governed
     by another jurisdiction, recommend using the jurisdiction-agnostic
     `legalcode-nda-triage` or the relevant jurisdiction-specific variant.

4. **Risk tolerance**: How should borderline items be classified?
   - Options: Conservative (flag more, safer), Pragmatic (flag only material items),
     Let me decide case by case
   - _Why this matters_: A liability cap that is RED for a risk-averse enterprise may be
     YELLOW for a startup that needs the deal.

5. **Victims and Prisoners Act 2024 applicability**: Was or will this NDA be signed on or
   after 1 October 2025?
   - Options: Yes (post-1 October 2025), No (signed before), Not sure
   - _Why this matters_: NDAs signed on or after 1 October 2025 must comply with s.17 of
     the Victims and Prisoners Act 2024. Clauses that prevent victims of crime from
     disclosing relevant conduct to specified persons are unenforceable.

If the user provides partial context, proceed with reasonable defaults but **state
assumptions explicitly** (e.g., "I'm assuming this is a mutual exploratory NDA governed by
English law -- let me know if that's wrong"). Do not silently assume.

### Step 3: Load the NDA Playbook

Check for the organisation's NDA screening criteria in local settings (e.g.,
`legal.local.md` or similar configuration files).

The NDA playbook should define:

- Mutual vs. unilateral requirements
- Acceptable term lengths
- Required carveouts
- Prohibited provisions
- Organisation-specific requirements (e.g., standard form NDA for counterproposals)
- Routing rules (who reviews YELLOW, who reviews RED)

**If no NDA playbook is configured:**

**CLARIFY** -- Inform the user that no playbook was found, and ask:

- **Option A: Set up a playbook now** -- Define the organisation's NDA positions for key
  criteria (acceptable terms, required carveouts, prohibited provisions). Takes a few
  minutes but makes this and all future triages more precise.
- **Option B: Proceed with general market standards** -- Use the default criteria below.
  Faster, but may not reflect the organisation's specific risk appetite.
- **Option C: I'll provide positions as we go** -- Start the triage and I'll ask when
  your preferred position matters.

**Default Standards** (when no playbook is configured):

- Mutual obligations required unless the organisation is only disclosing
- Term: 1-3 years standard; confidentiality survival: 2-5 years
- All 5 standard carveouts required (public knowledge, prior possession, independent
  development, third-party receipt, legal compulsion)
- No non-solicitation, non-compete, exclusivity, or standstill provisions
- No residuals clause (or narrowly scoped if present)
- No IP assignment or licence grants
- Governing law: laws of England and Wales with exclusive jurisdiction of the English courts
- Return/destruction with retention exception for legal/compliance copies
- Compliant with Victims and Prisoners Act 2024, s.17 (if signed on or after 1 October 2025)

Clearly label when defaults are being used: "Based on general market standards -- not
organisational playbook positions."

### Step 4: Gather English Law Authority

Read the NDA's governing law clause and confirm it specifies the laws of England and Wales.

**CLARIFY** -- If any of the following are true, ask the user before proceeding:

- **No governing law clause found**: Ask which jurisdiction the user expects to apply,
  and flag the absence as a RED item.
- **Governing law is not English law**: Confirm whether the user wants analysis under the
  stated law (recommend `legalcode-nda-triage`) or under English law (with caveats about
  applicability).
- **Governing law is Scots law or Northern Ireland law**: Note that this skill covers
  England and Wales only. Scots law has a different prescriptive period (5 years under the
  Trade Secrets Regulations) and different procedural rules.

**With legalcode-mcp connected (preferred):**

- Search for current English law statutes and cases governing: trade secret protection
  (Trade Secrets Regulations 2018, breach of confidence), penalty/liquidated damages
  enforceability (Cavendish Square v Makdessi), injunctive relief standards (American
  Cyanamid), non-compete/non-solicitation enforceability (restraint of trade doctrine,
  Egon Zehnder v Tillman), and Victims and Prisoners Act 2024 NDA provisions
- Save results to a local temp file (`/tmp/legalcode-nda-triage-ew-authority.md`)
- Reference verified authority throughout the screening
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark every statutory and case law reference with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with the English law authority summarised in this skill's "Governing Law" section
- Focus the analysis on structural screening and English law principles

### Step 5: NDA Screening

Read the **entire NDA** before flagging issues -- clauses interact with each other (e.g.,
a broad definition may be partially mitigated by strong carveouts, or a residuals clause
may be offset by a trade secret exception).

Evaluate the NDA against each of the 10 screening criteria systematically:

#### Criterion 1: Agreement Structure

- [ ] **Type identified**: Mutual NDA, Unilateral (disclosing party), or Unilateral
      (receiving party)
- [ ] **Appropriate for context**: Is the NDA type appropriate for the business
      relationship? (e.g., mutual for exploratory discussions, unilateral for one-way
      disclosures)
- [ ] **Standalone agreement**: Confirm the NDA is a standalone agreement, not a
      confidentiality section embedded in a larger commercial agreement
- [ ] **Party identification**: Are parties correctly identified (full legal names,
      registered company numbers where applicable, authorised signatories)?
- [ ] **English law formalities**: The NDA should be executed as a simple contract (signed
      by authorised representatives). If executed as a deed, note implications for limitation
      period (12 years rather than 6 under the Limitation Act 1980).

#### Criterion 2: Definition of Confidential Information

- [ ] **Reasonable scope**: Not overbroad (avoid "all information of any kind whether or
      not marked as confidential")
- [ ] **Marking requirements**: If marking is required, is it workable? (Written marking
      within 30 days of oral disclosure is standard)
- [ ] **Exclusions present**: Standard exclusions defined (see Criterion 4)
- [ ] **No problematic inclusions**: Does not define publicly available information or
      independently developed materials as confidential
- [ ] **Alignment with purpose**: Definition is tied to the stated purpose, not unlimited

**English law check -- alignment with trade secret protection regime:**
The definition should be assessed against the _Saltman Engineering_ quality-of-confidence
test: does the NDA's definition capture information that genuinely has the "necessary
quality of confidence"? If the definition is so broad it includes public knowledge or
trivial information, it may be difficult to enforce under the common law of breach of
confidence (_Coco v AN Clark_) and the Trade Secrets Regulations 2018. Under the
Regulations, a "trade secret" must: (a) be secret, (b) have commercial value because it is
secret, and (c) have been subject to reasonable steps to keep it secret. Where the NDA's
definition is broader than the statutory trade secret definition, note whether the NDA
provides different levels of protection for trade secrets vs. other confidential
information.

#### Criterion 3: Obligations of Receiving Party

- [ ] **Standard of care**: Reasonable care or at least the same care as for own
      confidential information
- [ ] **Use restriction**: Limited to the stated purpose
- [ ] **Disclosure restriction**: Limited to those with a need to know who are bound by
      similar obligations
- [ ] **No onerous obligations**: No impractical requirements (e.g., encrypting all
      communications, maintaining physical logs of every disclosure)
- [ ] **Incident reporting**: Reasonable breach notification obligation (if included)

#### Criterion 4: Standard Carveouts

All of the following carveouts should be present:

- [ ] **Public knowledge**: Information that is or becomes publicly available through no
      fault of the receiving party
- [ ] **Prior possession**: Information already known to the receiving party before
      disclosure
- [ ] **Independent development**: Information independently developed without use of or
      reference to confidential information
- [ ] **Third-party receipt**: Information rightfully received from a third party without
      restriction
- [ ] **Legal compulsion**: Right to disclose when required by law, regulation, court
      order, or legal process (with notice to the disclosing party where legally permitted and
      practicable)

**English law check -- Victims and Prisoners Act 2024 carveout:**
For NDAs signed on or after 1 October 2025, verify that the legal compulsion carveout (or
a separate provision) expressly permits disclosures required by s.17 of the Victims and
Prisoners Act 2024. A blanket prohibition on "any disclosure to any third party" without
this carveout may be unenforceable to the extent it conflicts with s.17.

#### Criterion 5: Permitted Disclosures

- [ ] **Employees**: Can share with employees who need to know
- [ ] **Contractors/advisers**: Can share with contractors, advisers, and professional
      consultants under similar confidentiality obligations
- [ ] **Affiliates**: Can share with group companies (if needed for the business purpose)
- [ ] **Legal/regulatory**: Can disclose as required by law, regulation, or regulatory
      authority (including the FCA, PRA, CMA, ICO, and other UK regulators)
- [ ] **Professional advisers**: Can share with solicitors, barristers, and accountants
      under professional duties of confidence (note: English solicitors and barristers are
      already bound by professional duties of confidentiality under the SRA Standards and
      Regulations and the BSB Handbook respectively)

#### Criterion 6: Term and Duration

- [ ] **Agreement term**: Reasonable period for the business relationship (1-3 years is
      standard)
- [ ] **Confidentiality survival**: Obligations survive for a reasonable period after
      termination (2-5 years is standard; trade secrets may be longer)
- [ ] **Not perpetual**: Avoid indefinite or perpetual confidentiality obligations
      (exception: trade secrets, which may warrant protection for as long as they remain
      trade secrets)

**English law check -- trade secret duration:**
Under the Trade Secrets Regulations 2018, a trade secret is protected for as long as it
meets the three statutory criteria (secret, commercially valuable because secret, subject
to reasonable steps). The NDA's survival clause should complement, not undermine, this
statutory protection. An NDA that imposes a fixed 2-year survival period on all
confidential information (including trade secrets) may inadvertently signal that the
disclosing party considers the information to cease being confidential after 2 years. Best
practice: define a fixed survival period for general confidential information and a
separate, longer or indefinite period for information qualifying as a trade secret under
the Regulations.

Limitation period note: contractual claims under a simple contract are subject to a 6-year
limitation period (Limitation Act 1980, s.5). If the NDA is executed as a deed, the
limitation period is 12 years (s.8). The Trade Secrets Regulations impose their own 6-year
limitation period from the date of unlawful acquisition, use, or disclosure (reg. 14).

#### Criterion 7: Return and Destruction

- [ ] **Obligation triggered**: On termination or upon request
- [ ] **Reasonable scope**: Return or destroy confidential information and all copies
- [ ] **Retention exception**: Allows retention of copies required by law, regulation,
      or internal compliance/backup policies (including regulatory record-keeping obligations
      under FCA, PRA, HMRC, or other UK regulatory requirements)
- [ ] **Certification**: Certification of destruction is reasonable; sworn affidavit or
      statutory declaration is onerous and unusual under English practice

#### Criterion 8: Remedies

- [ ] **Injunctive relief**: Acknowledgment that breach may cause loss that cannot be
      adequately compensated by damages alone and that equitable relief (including injunctions)
      may be appropriate

**English law check -- injunction standard (American Cyanamid):**
The test for interim injunctions under English law is _American Cyanamid Co v Ethicon Ltd_
[1975] AC 396:

1. Is there a serious question to be tried?
2. Would damages be an adequate remedy? (If so, no injunction.)
3. Where does the balance of convenience lie?
4. If the balance is even, preserve the status quo.

This is **not** the US "irreparable harm" standard. NDA language referencing "irreparable
harm" is not legally wrong under English law but does not reflect the test English courts
actually apply. Where an NDA uses US-style injunctive relief language, consider suggesting:
"The parties acknowledge that a breach of this Agreement may cause loss that cannot be
adequately compensated by an award of damages alone and that the non-breaching party may be
entitled to seek equitable relief, including injunctive relief, without prejudice to any
other rights and remedies available to it."

The court may also consider the merits more closely where the injunction would effectively
determine the dispute (_NWL Ltd v Woods_ [1979] 1 WLR 1294).

- [ ] **No pre-determined damages**: Avoid liquidated damages clauses in NDAs

**English law check -- penalty doctrine (Cavendish Square v Makdessi):**
Under _Cavendish Square Holding BV v Makdessi / ParkingEye Ltd v Beavis_ [2015] UKSC 67,
a clause is an unenforceable penalty if it imposes a detriment on the contract-breaker out
of all proportion to any legitimate interest of the innocent party in enforcement of the
primary obligation. This replaced the older _Dunlop Pneumatic Tyre v New Garage_ [1915]
"genuine pre-estimate of loss" test.

A liquidated damages clause in an NDA is unusual and should be flagged. The difficulty of
pre-estimating loss from a confidentiality breach makes such clauses harder to justify as
proportionate to a legitimate interest. If a liquidated damages clause is present:

- Assess whether the amount is proportionate to any legitimate interest the innocent party
  has in the performance of the confidentiality obligation
- Flag disproportionate amounts as RED (likely unenforceable penalty)
- Flag proportionate and mutual amounts as YELLOW (unusual but potentially defensible)

- [ ] **Not one-sided**: Remedies provisions apply equally to both parties (in mutual
      NDAs)

#### Criterion 9: Problematic Provisions to Flag

- [ ] **No non-solicitation**: NDA should not contain employee non-solicitation provisions
- [ ] **No non-compete**: NDA should not contain non-compete provisions
- [ ] **No exclusivity**: NDA should not restrict either party from entering similar
      discussions with others
- [ ] **No standstill**: NDA should not contain standstill or similar restrictive
      provisions (unless M&A context -- ask if unclear)
- [ ] **No residuals clause** (or narrowly scoped): If present, must be limited to
      information retained in unaided memory of individuals who had authorised access; must
      not apply to trade secrets (as defined in the Trade Secrets Regulations 2018) or
      patentable information; must not grant an IP licence
- [ ] **No IP assignment or licence**: NDA should not grant any intellectual property
      rights
- [ ] **No audit rights**: Unusual in standard NDAs; flag if present

**English law check -- restraint of trade doctrine:**
Non-solicitation and non-compete provisions embedded in NDAs are **restrictive covenants**
under English law. The restraint of trade doctrine (_Nordenfelt v Maxim Nordenfelt_ [1894]
AC 535) requires that any restriction must:
(a) protect a legitimate business interest,
(b) be no wider than reasonably necessary to protect that interest, and
(c) not be contrary to the public interest.

In the context of an NDA (as opposed to an employment agreement or sale-of-business
agreement), a non-solicitation or non-compete clause is more vulnerable to challenge
because the NDA context provides weaker justification for restraint. The court will assess
whether the restriction is reasonably necessary to protect the confidential information
being disclosed -- if the confidentiality obligations themselves provide adequate
protection, an additional non-compete or non-solicitation clause may be struck down as
going beyond what is reasonably necessary.

_Egon Zehnder Ltd v Tillman_ [2019] UKSC 32 confirmed that if a restrictive covenant is
partially unreasonable, the court may sever the unreasonable part using the blue pencil
test, provided: (1) the offending words can be removed without adding to or modifying what
remains, (2) the remaining terms are supported by adequate consideration, and (3) removal
does not change the character of the contract. However, severance is not guaranteed -- it
is discretionary and the court will not rewrite the covenant.

**Pending reform note:** The UK Government is consulting on statutory limits on non-compete
clauses in employment contracts (working paper published 26 November 2025). Options under
consideration include duration caps (3-6 months), outright bans, and salary-threshold
restrictions. No legislation has been enacted, but monitor for developments that may affect
non-compete provisions in NDAs entered in an employment context.

#### Criterion 10: Governing Law and Jurisdiction

- [ ] **English law**: Laws of England and Wales are the preferred governing law for UK
      organisations
- [ ] **Consistent**: Governing law and jurisdiction should be aligned (English law +
      English courts, or English law + London-seated arbitration)
- [ ] **Exclusive jurisdiction**: An exclusive jurisdiction clause is generally preferred
      for NDAs (prevents parallel proceedings)
- [ ] **English courts preferred**: The High Court of England and Wales is the preferred
      forum. For confidentiality disputes, the Chancery Division is typically appropriate.
- [ ] **No mandatory arbitration** (in standard NDAs): Litigation is generally preferred
      for NDA disputes -- arbitration offers limited appeal rights and can be
      disproportionately expensive for smaller disputes. However, London-seated arbitration
      (LCIA or ICC rules) may be appropriate for international NDAs where enforcement across
      borders is a concern (New York Convention).

### Step 6: Classify

Based on the screening results, assign a classification using the rules below:

#### GREEN -- Standard Approval

**All** of the following must be true:

- NDA is mutual (or unilateral in the appropriate direction for the relationship)
- Governed by the laws of England and Wales with exclusive English court jurisdiction (or
  acceptable common law equivalent)
- All 5 standard carveouts are present
- Term is within standard range (1-3 years, survival 2-5 years)
- No non-solicitation, non-compete, exclusivity, or standstill provisions
- No residuals clause, or residuals clause is narrowly scoped
- Standard remedies (no liquidated damages)
- Permitted disclosures include employees, contractors, advisers, and professional advisers
- Return/destruction provisions include retention exception for legal/compliance
- Definition of confidential information is reasonably scoped and tied to purpose
- Compliant with Victims and Prisoners Act 2024, s.17 (if applicable)

**Confidence required**: HIGH (0.80+) -- Confident this meets all standard criteria.

**Routing**: Approve via standard delegation of authority. No solicitor review required.
Same-day turnaround.

#### YELLOW -- Solicitor Review Needed

**One or more** of the following are present, but the NDA is not fundamentally
problematic:

- Definition of confidential information is broader than preferred but not unreasonable
- Term is longer than standard but within market range (e.g., 5 years agreement term,
  7 years survival)
- Missing one standard carveout that could be added without difficulty
- Residuals clause present but narrowly scoped to unaided memory
- Governed by Scots law or another acceptable common law jurisdiction (not English law,
  but not problematic)
- Non-exclusive jurisdiction clause when exclusive would be preferred
- Minor asymmetry in a mutual NDA (e.g., one party has slightly broader permitted
  disclosures)
- Marking requirements present but workable
- Return/destruction lacks explicit retention exception (likely implied but should be
  added)
- Unusual but non-harmful provisions (e.g., obligation to notify of potential breach)
- London-seated arbitration (LCIA or ICC) where litigation would be preferred
- US-style "irreparable harm" injunction language (suggest English-law-appropriate
  replacement)
- No explicit Victims and Prisoners Act 2024 carveout, but the general legal compulsion
  carveout likely covers it

**Confidence required**: PROBABLE (0.60+) -- Issues identified but could be wrong about
materiality. If confidence is below 0.60, flag for solicitor review regardless.

**Routing**: Flag specific issues for solicitor review. Solicitor can likely resolve with
minor redlines in a single review pass. Target: 1-2 business days.

#### RED -- Significant Issues

**One or more** of the following are present:

- **Unilateral when mutual is required** (or wrong direction for the relationship)
- **Missing critical carveouts** (especially independent development or legal compulsion)
- **Non-solicitation or non-compete provisions** embedded in the NDA (likely challengeable
  under restraint of trade doctrine in this context, but still risky to sign)
- **Exclusivity or standstill provisions** without appropriate business context
- **Unreasonable term** (10+ years, or perpetual without trade secret justification)
- **Overbroad definition** that could capture public information or independently
  developed materials
- **Broad residuals clause** that effectively creates a licence to use confidential
  information
- **IP assignment or licence grant** hidden in the NDA
- **Liquidated damages or penalty provisions** (likely unenforceable under _Cavendish
  Square v Makdessi_ [2015] UKSC 67, but signals aggressive counterparty)
- **Audit rights** without reasonable scope or notice requirements
- **Foreign governing law** in a problematic jurisdiction with mandatory arbitration
- **The document is not actually an NDA** (contains substantive commercial terms,
  exclusivity, or other obligations beyond confidentiality)
- **Assignment clause** allowing the counterparty to assign obligations without consent
- **Clauses conflicting with Victims and Prisoners Act 2024, s.17** -- blanket non-
  disclosure provisions that would prevent crime victims from making protected disclosures
  (for NDAs signed on or after 1 October 2025)
- **Clauses potentially void under English law** -- provisions that conflict with
  mandatory statutory requirements or settled common law principles

**Confidence required**: HIGH (0.80+) -- Confident the issue is material. If confidence
is below 0.80, classify as YELLOW and flag for solicitor review rather than RED. It is
better to send a borderline item for review than to escalate unnecessarily.

**Routing**: Full solicitor review required. Do not sign. Requires negotiation,
counterproposal with the organisation's standard form NDA, or rejection. Target: 3-5
business days.

### Step 7: Generate Common Issue Analysis

For each YELLOW or RED finding, provide actionable analysis:

#### Common NDA Issues and Standard Positions (England & Wales)

**Issue: Overbroad Definition of Confidential Information**

- **Standard position**: Confidential information should be limited to non-public
  information disclosed in connection with the stated purpose, with clear exclusions.
- **English law basis**: _Saltman Engineering v Campbell Engineering_ (1948) -- information
  must have the "necessary quality of confidence." _Coco v AN Clark_ [1969] RPC 41 --
  three-part test for breach of confidence. Overbroad definitions may be difficult to
  enforce because they capture information lacking the necessary quality of confidence.
- **Redline approach**: Narrow the definition to information that is marked or identified
  as confidential, or that a reasonable person would understand to be confidential given
  the nature of the information and circumstances of disclosure.
- **Priority**: Tier 2 (Should-Have)

**Issue: Missing Independent Development Carveout**

- **Standard position**: Must include a carveout for information independently developed
  without reference to or use of the disclosing party's confidential information.
- **Risk if missing**: Could create claims that internally-developed products or features
  were derived from the counterparty's confidential information.
- **Redline approach**: Add standard independent development carveout.
- **Priority**: Tier 1 (Must-Have) -- Missing this carveout is RED.

**Issue: Non-Solicitation of Employees**

- **Standard position**: Non-solicitation provisions do not belong in NDAs. They are
  appropriate in employment agreements, M&A agreements, or specific commercial agreements
  where they protect a legitimate business interest.
- **English law position**: In the context of an NDA (not employment or sale of business),
  a non-solicitation clause is vulnerable to challenge under the restraint of trade
  doctrine (_Nordenfelt_ [1894]; _Egon Zehnder v Tillman_ [2019] UKSC 32). It must
  protect a legitimate interest and be no wider than reasonably necessary. The
  confidentiality obligations in the NDA themselves may provide sufficient protection,
  making an additional non-solicitation clause unnecessary and therefore unreasonable.
- **Redline approach**: Delete the provision entirely. If the counterparty insists, limit
  to direct targeted solicitation (not general recruitment or responses to advertisements)
  with a short term (6-12 months).
- **Priority**: Tier 1 (Must-Have) -- This is always RED in an NDA context.

**Issue: Broad Residuals Clause**

- **Standard position**: Resist residuals clauses. If required, limit to: (a) general
  ideas, concepts, know-how, or techniques retained in the unaided memory of individuals
  who had authorised access; (b) explicitly exclude trade secrets (as defined in the Trade
  Secrets Regulations 2018); (c) does not grant any IP licence.
- **Risk if too broad**: Effectively grants a licence to use the disclosing party's
  confidential information for any purpose. May undermine the "reasonable steps" limb
  of the trade secret definition under the Regulations.
- **Redline approach**: Narrow to unaided memory with trade secret and IP carveouts.
- **Priority**: Tier 1 if broad (RED), Tier 2 if narrowly scoped (YELLOW).

**Issue: Perpetual Confidentiality Obligation**

- **Standard position**: 2-5 years from disclosure or termination, whichever is later.
  Trade secrets may warrant protection for as long as they remain trade secrets.
- **English law basis**: The Trade Secrets Regulations 2018 protect trade secrets for as
  long as they meet the three statutory criteria. A perpetual obligation for all
  information (not just trade secrets) may be challenged as unreasonable, though English
  law generally permits parties freedom to agree terms. Best practice is a defined term
  for general confidential information with a separate, longer period for trade secrets.
- **Redline approach**: Replace perpetual obligation with a defined term. Offer a trade
  secret carveout for longer protection of qualifying information.
- **Priority**: Tier 2 (Should-Have) unless term is truly unreasonable (10+ years = RED).

**Issue: Liquidated Damages / Penalty Clauses**

- **Standard position**: Liquidated damages clauses are unusual in NDAs and should be
  flagged. The difficulty of pre-estimating loss from a confidentiality breach makes
  such clauses harder to justify.
- **English law basis**: Under _Cavendish Square v Makdessi / ParkingEye v Beavis_ [2015]
  UKSC 67, a clause is an unenforceable penalty if it imposes a detriment out of all
  proportion to any legitimate interest of the innocent party. The older "genuine
  pre-estimate of loss" test (_Dunlop v New Garage_ [1915]) has been replaced by the
  proportionality-to-legitimate-interest test.
- **Priority**: Tier 1 (RED) if amounts are disproportionate; Tier 2 (YELLOW) if amounts
  are reasonable and mutual.

**Issue: US-Style "Irreparable Harm" Injunction Language**

- **Standard position**: While the phrase is not legally incorrect under English law, it
  does not reflect the test English courts apply for interim injunctions.
- **English law basis**: The test is _American Cyanamid v Ethicon_ [1975] AC 396 (serious
  question to be tried + adequacy of damages + balance of convenience), not "irreparable
  harm."
- **Suggested replacement**: "The parties acknowledge that a breach of this Agreement may
  cause loss that cannot be adequately compensated by an award of damages alone and that
  the non-breaching party may be entitled to seek equitable relief, including injunctive
  relief, without prejudice to any other rights and remedies available to it."
- **Priority**: Tier 3 (Nice-to-Have) -- cosmetic improvement, not a material issue.

**Issue: Non-Compliance with Victims and Prisoners Act 2024**

- **Standard position**: NDAs signed on or after 1 October 2025 must not prevent victims
  of crime from disclosing information about relevant conduct to police, solicitors,
  regulated healthcare professionals, or victim support services.
- **English law basis**: Victims and Prisoners Act 2024, s.17.
- **Redline approach**: Add an express carveout permitting disclosures in accordance with
  s.17, or ensure the general legal compulsion carveout is broad enough to cover it.
- **Priority**: Tier 1 (Must-Have) if the NDA contains blanket non-disclosure provisions
  without any carveout; Tier 2 (Should-Have) if the general legal compulsion carveout
  is present but does not expressly reference s.17.

### Step 8: Negotiation Priority Framework

Organise findings by negotiation priority:

#### Tier 1 -- Must-Haves (Deal Blockers)

Issues where the organisation cannot proceed without resolution:

- Missing critical carveouts (independent development, legal compulsion)
- Non-solicitation or non-compete provisions in an NDA
- Broad residuals clause that creates an effective IP licence
- IP assignment or licence hidden in the NDA
- Document is not actually an NDA (embedded commercial terms)
- Blanket non-disclosure conflicting with Victims and Prisoners Act 2024, s.17
- Disproportionate liquidated damages (likely unenforceable penalty under _Makdessi_)

#### Tier 2 -- Should-Haves (Strong Preferences)

Issues that materially affect risk but have negotiation room:

- Overbroad confidential information definition
- Term adjustments (longer than standard but negotiable)
- Missing retention exception in return/destruction
- Express Victims and Prisoners Act 2024 carveout (where general carveout exists)
- Certification of destruction scope
- Marking requirement modifications

#### Tier 3 -- Nice-to-Haves (Concession Candidates)

Issues that improve the position but can be conceded strategically:

- Preferred governing law wording (if English law is confirmed)
- Minor asymmetries in mutual NDA
- Notification obligations (unusual but not harmful)
- US-style injunction language replacement
- Specific dispute resolution mechanism preference (e.g., High Court vs. LCIA)

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

| Classification | Recommended Action                                                         | Typical Timeline  |
| -------------- | -------------------------------------------------------------------------- | ----------------- |
| GREEN          | Approve and route for signature per delegation of authority                | Same day          |
| YELLOW         | Send to designated solicitor/reviewer with specific issues flagged         | 1-2 business days |
| RED            | Engage solicitor for full review; prepare counterproposal or standard form | 3-5 business days |

For YELLOW and RED classifications:

- Identify the specific person or role that should review (if the organisation has defined
  routing rules in the playbook)
- Include a brief summary of issues suitable for the reviewer to quickly understand the
  key points
- If the organisation has a standard form NDA, recommend sending it as a counterproposal
  for RED-classified NDAs (reference the `nda-mutual` skill if drafting is needed)
- For international counterparties, consider whether the English court jurisdiction or
  London-seated arbitration position is appropriate for enforcement purposes (New York
  Convention for arbitration awards; Hague Convention on Choice of Court Agreements for
  judgments)
- For confidentiality disputes, note that the Chancery Division of the High Court is the
  appropriate forum

---

## Severity / Status Classification

| Finding Status | Meaning                  | Action                                               |
| -------------- | ------------------------ | ---------------------------------------------------- |
| **PASS**       | Criterion met; no issues | No action needed                                     |
| **FLAG**       | Minor deviation; YELLOW  | Generate redline with fallback position              |
| **FAIL**       | Material deviation; RED  | Escalate with risk explanation and English law basis |

---

## Prioritisation Framework Summary

| Priority   | Category      | Examples                                                                                | Negotiation Posture                   |
| ---------- | ------------- | --------------------------------------------------------------------------------------- | ------------------------------------- |
| **Tier 1** | Must-Haves    | Missing carveouts, non-compete, IP assignment, broad residuals, VPA 2024 non-compliance | Non-negotiable; escalate if rejected  |
| **Tier 2** | Should-Haves  | Overbroad definition, term adjustments, retention exception                             | Push firmly; accept fallback          |
| **Tier 3** | Nice-to-Haves | Injunction language, governing law wording, minor asymmetries                           | Concede strategically for Tier 2 wins |

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Identify the NDA type, counterparty, business context, and confirm English law
governs. Determine whether a playbook exists. Assess whether any special considerations
apply (M&A context, regulated sector, international counterparty, high-value relationship,
Victims and Prisoners Act 2024 applicability).

**DO**: Execute the 10-criteria screening. Classify GREEN/YELLOW/RED. Generate findings
with English law basis and suggested fixes. Assign negotiation priorities.

**CHECK**: Run the Citation Quality Gates. Verify legal claims in the triage rationale
against English law authority. For RED classifications, run the Self-Interrogation. Confirm
all 10 criteria addressed.

**ACT**: If the NDA reveals a new pattern (e.g., a clause structure becoming common in
the market), note it for playbook update. If the organisation's standard form NDA is
missing a protection that this NDA exposed, flag for standard form revision. Monitor
developments in non-compete reform and Victims and Prisoners Act 2024 implementation.

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                                                                                                                                                                                                      | Fail Action                                                 |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific English statute, regulation, case, or established common law principle                                                                                                                                                                                                                 | Add citation or mark "[UNVERIFIED -- solicitor to confirm]" |
| **Format**     | All citations follow English law conventions: statutes by short title and section; cases by name, neutral citation, and law report reference                                                                                                                                                                              | Fix format                                                  |
| **Currency**   | Every cited provision checked for amendments or repeal -- Trade Secrets Regulations 2018 in force; Cavendish Square (2015) is current law; American Cyanamid (1975) remains good law; Egon Zehnder v Tillman (2019) is the leading severance authority; Victims and Prisoners Act 2024, s.17 in force from 1 October 2025 | Flag "[CHECK CURRENCY -- may have been amended]"            |
| **Domain**     | Analysis stays within English law. No US assumptions (no "irreparable harm" as injunction test, no state-specific non-compete rules, no class action waiver). No civil law concepts (no kary umowne, no miarkowanie).                                                                                                     | Remove or flag jurisdictional bleed                         |
| **Confidence** | Uncertainty explicitly stated, not hidden. If uncertain, say so                                                                                                                                                                                                                                                           | Add confidence qualifier                                    |

### Self-Interrogation for RED Items

For any item classified as RED, apply this 3-pass review before delivering:

**Pass 1 -- Legal Chain Integrity**: Does the risk assessment follow logically from the
cited English law authority? Would a court in England and Wales actually reach this
conclusion on these facts? Is there a counter-argument the counterparty's solicitors will
make? Consider: would the Chancery Division or the Commercial Court reach the same view?

**Pass 2 -- Completeness**: Have all relevant statutes, regulations, and common law
principles been considered? Are there regulatory dimensions not yet addressed (FCA, CMA,
ICO)? Could the clause interact with another clause to mitigate or worsen the risk? Has the
Victims and Prisoners Act 2024 been considered where applicable?

**Pass 3 -- Challenge**: What is the strongest argument that this clause IS acceptable?
Under what circumstances might a reasonable solicitor at a City firm or Magic Circle firm
accept this risk? Is the RED classification proportionate, or is this actually YELLOW with
redlines? Would a commercial practitioner at a leading firm send this back, or mark it up
and proceed?

If any pass reveals a weakness, revise the analysis before delivery. Mark the audit trail
with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For the overall classification and each material finding, assign a confidence level:

| Level        | Range     | Meaning                                                             | Action                                                   |
| ------------ | --------- | ------------------------------------------------------------------- | -------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled English law, clear contractual provision, no ambiguity      | State with confidence                                    |
| **High**     | 0.80-0.94 | Strong basis in statute or case law, minor interpretation questions | State with brief caveat                                  |
| **Probable** | 0.60-0.79 | Good arguments but reasonable minds could differ                    | State with reasoning and contra-indicators               |
| **Possible** | 0.40-0.59 | Genuinely uncertain, competing interpretations                      | Flag for solicitor review with both sides                |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative                                             | Do not assert; flag "[UNCERTAIN -- solicitor to advise]" |

---

## Glass Box Audit Trail

Every NDA triage output MUST include a Glass Box audit section at the end:

```yaml
glass_box:
  nda_counterparty: "[Counterparty name]"
  nda_type: "[Mutual / Unilateral -- direction]"
  governing_law: "Laws of England and Wales"
  classification: "GREEN / YELLOW / RED"
  confidence: "HIGH / MEDIUM / LOW -- [rationale]"
  review_basis: "[Organisational playbook / General market standards]"
  criteria_screened: 10
  criteria_summary:
    structure: "PASS / FLAG -- [brief note]"
    definition_scope: "PASS / FLAG -- [brief note]"
    obligations: "PASS / FLAG"
    carveouts: "PASS / FLAG -- [missing: independent development]"
    permitted_disclosures: "PASS / FLAG"
    term: "PASS / FLAG -- [3 years / 5 years survival]"
    return_destruction: "PASS / FLAG"
    remedies: "PASS / FLAG"
    problematic_provisions: "PASS / FLAG -- [non-compete found]"
    governing_law: "PASS / FLAG"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to temp file or 'Not created']"
  statutes_consulted:
    - "Trade Secrets (Enforcement, etc.) Regulations 2018 (SI 2018/597) -- [VERIFIED/UNVERIFIED]"
    - "Victims and Prisoners Act 2024, s.17 -- [VERIFIED/UNVERIFIED]"
    - "Limitation Act 1980, ss.5, 8 -- [VERIFIED/UNVERIFIED]"
  cases_consulted:
    - "American Cyanamid Co v Ethicon Ltd [1975] AC 396 -- [VERIFIED/UNVERIFIED]"
    - "Coco v AN Clark (Engineers) Ltd [1969] RPC 41 -- [VERIFIED/UNVERIFIED]"
    - "Saltman Engineering v Campbell Engineering (1948) 65 RPC 203 -- [VERIFIED/UNVERIFIED]"
    - "Faccenda Chicken Ltd v Fowler [1987] Ch 117 -- [VERIFIED/UNVERIFIED]"
    - "Cavendish Square v Makdessi / ParkingEye v Beavis [2015] UKSC 67 -- [VERIFIED/UNVERIFIED]"
    - "Nordenfelt v Maxim Nordenfelt [1894] AC 535 -- [VERIFIED/UNVERIFIED]"
    - "Egon Zehnder v Tillman [2019] UKSC 32 -- [VERIFIED/UNVERIFIED]"
    - "NWL Ltd v Woods [1979] 1 WLR 1294 -- [VERIFIED/UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  vpa_2024_applicable: "Yes / No / Not determined"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted -- requires qualified solicitor review"
```

---

## Anti-Patterns

What NOT to do in NDA triage under English law:

1. **Classifying everything as YELLOW "to be safe"** -- If everything needs solicitor
   review, the triage process adds no value. GREEN means GREEN -- approve and sign. Trust
   the framework. The purpose of triage is to route efficiently, not to defer every
   decision.

2. **Missing the embedded commercial agreement** -- The most dangerous NDA is one that
   isn't really an NDA. If the document contains IP assignment, exclusivity, non-compete,
   or standstill provisions, it's a commercial agreement wearing NDA clothing. This is
   always RED. Read every clause, not just the title.

3. **Ignoring the business context** -- An NDA for exploratory due diligence in an M&A
   context may legitimately include standstill provisions. The same clause in a sales-
   stage NDA is a RED flag. Context determines whether unusual clauses are appropriate.

4. **Treating all non-standard terms as problems** -- A well-drafted NDA from a reputable
   counterparty may use different language from your standard form but achieve the same
   legal effect. Read for substance, not just form. A 4-year term is not automatically
   YELLOW just because your standard is 3 years.

5. **NDA triage without reading the whole document** -- Scanning the first page and the
   signature block misses the problematic provisions buried in the middle. The non-
   solicitation clause is in Section 8.2, not the recitals.

6. **Citing statutes from memory without verification** -- Statutes are amended, repealed,
   and renumbered. Case citations may not exist. If you cannot verify a citation against
   an authoritative source, mark it [VERIFY] or "[UNVERIFIED -- solicitor to confirm]."
   Never present an unverified citation as settled law.

7. **Applying US injunction concepts under English law** -- "Irreparable harm" is a US
   injunction standard, not English law. The test under English law is _American Cyanamid_
   (serious question to be tried + adequacy of damages + balance of convenience). Do not
   assess the NDA's injunctive relief clause against the wrong legal test. This is the
   single most common jurisdictional error in NDA triage.

8. **Assuming residuals clauses are always bad** -- A narrowly-scoped residuals clause
   (unaided memory, excluding trade secrets per the Trade Secrets Regulations 2018, no IP
   licence) is increasingly market-standard in technology transactions. A broad residuals
   clause is RED. Distinguish.

9. **Flagging "irreparable harm" language as a material problem** -- While the English
   test for injunctions is _American Cyanamid_ not "irreparable harm," the phrase is not
   legally wrong in an NDA -- it simply does not reflect how English courts decide
   injunctions. This is at most YELLOW (suggest replacement language), not RED.

10. **Single-pass analysis** -- A triage that reads each criterion once, in order, will
    miss interactions between clauses. A broad definition may be partially mitigated by
    strong carveouts. An uncapped remedy may be offset by a well-scoped limitation
    elsewhere. Read the whole NDA, then screen.

11. **Triage without confirming English law governs** -- Check governing law in the first
    30 seconds. If the NDA is governed by New York law, Scots law, or any other
    jurisdiction, this skill does not apply. Flag immediately and recommend the
    jurisdiction-agnostic `legalcode-nda-triage` or the relevant jurisdiction-specific
    variant.

12. **Over-engineering the triage output** -- The purpose of NDA triage is to route, not
    to provide full legal analysis. The report should fit on one page. If the NDA is RED,
    it goes to a solicitor -- they do not need a 10-page analysis from the triage tool.
    Be concise.

13. **Ignoring what is NOT in the NDA** -- Focusing only on clauses that are present and
    ignoring absent clauses. An NDA with no independent development carveout, no legal
    compulsion carveout, or no retention exception has material gaps that must be flagged.

14. **Failing to recommend a counterproposal** -- When an NDA is RED, do not just say
    "reject." Recommend the organisation's standard form NDA as a counterproposal, or
    reference the `nda-mutual` skill for drafting one.

15. **Ignoring the Victims and Prisoners Act 2024** -- For NDAs signed on or after 1
    October 2025, blanket non-disclosure provisions that do not carve out protected
    disclosures under s.17 are unenforceable to that extent. Failure to check for
    compliance is a material omission. This is a new requirement that many template NDAs
    will not yet reflect.

16. **Conflating English law penalty doctrine with US unconscionability** -- The English
    penalty test (_Cavendish Square v Makdessi_ [2015] UKSC 67) asks whether the clause
    imposes a detriment out of all proportion to any legitimate interest. This is not the
    US unconscionability standard. Do not import US analysis. The test is whether there is
    a legitimate interest and whether the detriment is proportionate to it.

17. **Overlooking the significance of deed execution** -- If the NDA is executed as a deed
    rather than a simple contract, the limitation period extends from 6 to 12 years
    (Limitation Act 1980, ss.5 and 8). This is not a problem per se but changes the risk
    profile and should be noted.

---

## Writing Standards

Apply plain-language discipline to all triage output:

**For the triage report**:

- Plain language. No jargon or filler.
- Active voice: "This NDA contains a non-compete clause (Section 8.2)" not "A non-
  compete clause was identified"
- Short sentences. One point per sentence.
- Name the section: cite the specific NDA section reference for each finding
- Specific, not vague: "Remove Section 7.3 (non-solicitation)" not "consider the
  non-solicitation provision"
- Use British English spelling conventions (organisation, licence, favour, defence)

**For each finding**:

- State what the NDA says (with section reference)
- State what the standard position is under English law
- State the risk of accepting the current language
- State the English law basis (statute, case, or common law principle)
- State the suggested fix (specific language or approach)

**Quality gates before delivery**:

1. Is the classification (GREEN/YELLOW/RED) clearly stated at the top?
2. Is every FLAG/FAIL supported by a specific section reference in the NDA?
3. Can the routing recipient understand the issues without reading the full NDA?
4. Are legal claims in the rationale backed by English law authority (or flagged [VERIFY])?
5. Is the report concise enough to fit on one page?
6. Are all citations in correct English law format?
7. Has British English spelling been used throughout?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.
legalcode-mcp is a law, regulatory, and case law database with powerful search across
jurisdictions.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for current English law statutes and cases governing trade secrets,
  breach of confidence, penalties, injunctions, and restrictive covenants
- Search for Victims and Prisoners Act 2024 provisions and any statutory instruments
- Save the most relevant results to `/tmp/legalcode-nda-triage-ew-authority.md`
- Reference verified authority throughout the screening
- For RED items, search for additional case law to support or challenge the classification
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Rely on the English law authority summarised in this skill's "Governing Law" section
- Include a notice that legal citations require independent verification
- Focus the analysis on structural screening and English law principles

---

## Output Format Template

Structure the triage deliverable as:

```markdown
## NDA Triage Report (England & Wales)

**Classification**: [GREEN / YELLOW / RED]
**Confidence**: [level with numeric range]
**Parties**: [party names]
**Type**: [Mutual / Unilateral (disclosing) / Unilateral (receiving)]
**Term**: [agreement duration] | **Survival**: [confidentiality survival period]
**Governing Law**: Laws of England and Wales
**Jurisdiction**: [Exclusive / Non-exclusive -- English courts / London arbitration]
**Review Basis**: [Organisational Playbook / General Market Standards]
**VPA 2024 Applicable**: [Yes / No / Not determined]
**Date**: [date]

---

## Screening Results

| #   | Criterion                   | Status           | Notes     |
| --- | --------------------------- | ---------------- | --------- |
| 1   | Agreement Structure         | [PASS/FLAG/FAIL] | [details] |
| 2   | Definition Scope            | [PASS/FLAG/FAIL] | [details] |
| 3   | Receiving Party Obligations | [PASS/FLAG/FAIL] | [details] |
| 4   | Standard Carveouts          | [PASS/FLAG/FAIL] | [details] |
| 5   | Permitted Disclosures       | [PASS/FLAG/FAIL] | [details] |
| 6   | Term and Duration           | [PASS/FLAG/FAIL] | [details] |
| 7   | Return/Destruction          | [PASS/FLAG/FAIL] | [details] |
| 8   | Remedies                    | [PASS/FLAG/FAIL] | [details] |
| 9   | Problematic Provisions      | [PASS/FLAG/FAIL] | [details] |
| 10  | Governing Law/Jurisdiction  | [PASS/FLAG/FAIL] | [details] |

---

## Issues Found

### [Issue 1 -- YELLOW/RED] | Section [X.X] | Priority: Tier [1/2/3]

**NDA says**: "[exact quote or summary from the NDA]"
**Standard position**: [what it should say under English law]
**Risk**: [what could go wrong if accepted]
**English law basis**: [statute/case/principle -- or "[VERIFY]"]
**Suggested fix**: [specific language or approach]
**Fallback**: [alternative if primary fix is rejected]
**Confidence**: [level]

[Repeat for each issue]

---

## Recommendation

[Specific next step: approve, send for solicitor review with specific notes, or
reject/counter]

---

## Negotiation Priority

**Tier 1 (Must-Haves)**: [list]
**Tier 2 (Should-Haves)**: [list]
**Tier 3 (Concession Candidates)**: [list]

---

## Next Steps

1. [Action item 1]
2. [Action item 2]
3. [Action item 3]

---

## Glass Box Audit Trail

[YAML block per Glass Box section above]
```

---

## Localization Notes

This skill is a jurisdiction-specific variant of the base `legalcode-nda-triage` skill,
localised for England and Wales. It was created by:

1. Replacing all [JURISDICTION-SPECIFIC] markers with English law content citing specific
   statutes and cases
2. Replacing all [VERIFY] tags with verified references to English law authority
3. Adding England & Wales-specific screening criteria: penalty doctrine analysis
   (_Cavendish Square v Makdessi_), American Cyanamid injunction test, restraint of trade
   doctrine for non-competes in NDAs (_Nordenfelt_, _Egon Zehnder v Tillman_), Trade
   Secrets Regulations 2018 alignment, Victims and Prisoners Act 2024 compliance, and
   deed execution implications
4. Adding 3 England & Wales-specific anti-patterns (items 15-17) on top of the base 14
5. Updating frontmatter to reference England & Wales
6. Adding relevant case law citations throughout

---

## Provenance

Created by Legalcode (2026-02-27). England & Wales localisation of the jurisdiction-
agnostic `legalcode-nda-triage` skill. Incorporates English law authority from:

- **Base template**: `legalcode-nda-triage` -- 10-criteria checklist, PDCA quality
  framework, Glass Box audit trail, confidence scoring, interactive CLARIFY points,
  negotiation priority framework
- **Deprecated UK skill**: `imported-uk-legal-plugins--skills-uk-legal-nda-triage` --
  American Cyanamid test, Cavendish Square penalty doctrine, Trade Secrets Regulations
  2018, restraint of trade analysis, RLM Challenge framework, English law writing
  standards
- **English law research**: Trade Secrets (Enforcement, etc.) Regulations 2018 (SI
  2018/597); Victims and Prisoners Act 2024, s.17; _American Cyanamid v Ethicon_ [1975]
  AC 396; _Coco v AN Clark_ [1969] RPC 41; _Saltman Engineering v Campbell Engineering_
  (1948) 65 RPC 203; _Faccenda Chicken v Fowler_ [1987] Ch 117; _Cavendish Square v
  Makdessi_ [2015] UKSC 67; _Nordenfelt v Maxim Nordenfelt_ [1894] AC 535; _Egon Zehnder
  v Tillman_ [2019] UKSC 32; _NWL v Woods_ [1979] 1 WLR 1294
