---
name: legalcode-letter-of-intent-review
description: Review letters of intent (LOIs), memoranda of understanding (MOUs), term sheets, heads of
  terms, and agreements in principle for corporate transactions.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review letters of intent (LOIs), memoranda of understanding (MOUs), term sheets, heads of terms, and agreements in principle for corporate transactions. Identifies binding vs. non-binding provisions, assesses enforceability risks from purportedly non-binding language, and flags provisions creating unintended binding obligations. Analyzes exclusivity and no-shop clauses (scope, duration, fiduciary-out carveouts, penalty for breach), break-up fees and reverse break-up fees (trigger events, market benchmarks, Takeover Panel inducement fee rules), confidentiality obligations (standalone vs. integrated, duration, residuals clauses), conditions precedent to closing (satisfactory due diligence risk, financing conditions, regulatory clearances), expense allocation (reliance damages exposure, culpa in contrahendo under civil law), and governing law provisions. Evaluates alignment between LOI terms and market-standard definitive agreement provisions. Produces gap analysis with recommended additions before signing. Classifies findings GREEN/YELLOW/RED with confidence scoring, Tier 1/2/3 negotiation priorities, and actionable redlines with fallback positions. Use for M&A transactions (strategic and financial sponsor), private equity acquisitions, joint ventures, real estate transactions, licensing platform deals, and any corporate transaction using a preliminary agreement before a definitive document. Covers US (Delaware and New York law), UK (English law, Takeover Panel rules), and EU/European transactions with jurisdiction markers. Supports buyer-side, seller-side, and advisor review.


# Legalcode Letter of Intent Review

> **Disclaimer**: This skill provides a framework for AI-assisted letter of intent and
> term sheet review. It does not constitute legal advice. All outputs should be reviewed
> by a qualified legal professional licensed in the relevant jurisdiction before use.
> Laws change; verify current applicability before relying on any provision described
> here. Statutory and case law references cited from memory carry hallucination risk —
> verify against authoritative sources before relying on them. Enforceability of LOI
> provisions is highly fact-specific and jurisdiction-dependent; this skill produces
> analytical frameworks, not legal opinions.

---

## Purpose and Scope

This skill reviews letters of intent, memoranda of understanding, term sheets, heads of
terms, and agreements in principle for corporate transactions. It identifies provisions
that are binding versus non-binding, flags enforceability risks where nominally
non-binding language may create legal obligations, and evaluates alignment between LOI
terms and market-standard definitive agreement provisions.

**Covers:**

- Binding vs. non-binding provision identification with enforceability risk scoring
- Unintentional binding obligation detection (estoppel, part performance, conduct)
- Exclusivity / no-shop / no-talk covenant analysis (scope, duration, carveouts)
- Break-up fee and reverse break-up fee review (market benchmarks, trigger events)
- Confidentiality obligation analysis (scope, duration, residuals, standalone vs. integrated)
- Conditions precedent assessment (satisfactory due diligence, financing, regulatory)
- Expense allocation review (reliance damages risk, pre-signing cost allocation)
- Governing law and dispute resolution analysis
- Gap analysis: key provisions missing before the LOI is signed
- GREEN / YELLOW / RED classification with confidence scoring
- Actionable redlines with fallback positions
- Negotiation strategy with Tier 1/2/3 prioritization
- Glass Box audit trail for traceability

**Does not:**

- Draft new LOIs, term sheets, or heads of terms (see drafting-specific skills)
- Provide legal advice or replace qualified M&A or transaction counsel
- Perform financial, tax, or accounting analysis of deal economics
- Conduct due diligence on the target business (see `legalcode-ma-due-diligence-checklist`)
- Review definitive purchase agreements (see `legalcode-purchase-agreement-review`)
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers

**Complementary skills in the M&A workflow:**

- `legalcode-ma-due-diligence-checklist` — pre-signing diligence across 12 workstreams
- `legalcode-purchase-agreement-review` — full SPA/APA review once the LOI leads to a definitive agreement
- `legalcode-due-diligence-report` — executive DD findings report
- `legalcode-nda-triage` — standalone NDA review (where LOI confidentiality is insufficient)
- `legalcode-contract-review` — general commercial contract review for non-M&A contexts

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic. The LOI's governing law clause (or, if absent, the
applicable law of the negotiating parties' domicile or transaction location) determines
which legal framework applies. The review identifies governing law early and adapts the
enforceability analysis accordingly.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

**United States:**

- Delaware corporate law on fiduciary duties and Revlon obligations during a sale process
  (whether seller is obligated to conduct a market check) [VERIFY]
- New York contract law on agreements to agree and enforceability of preliminary documents
  (_Teachers Insurance & Annuity Ass'n v. Tribune Co._, 2d Cir. 1987: Type I fully
  binding agreement vs. Type II binding only as to agreement to negotiate) [VERIFY]
- Texas law on agreement-in-principle enforceability (_Texaco, Inc. v. Pennzoil Co._,
  729 S.W.2d 768 (Tex. App. 1987), affirmed; $11.1 billion verdict on binding agreement
  in principle) [VERIFY]
- _SIGA Technologies, Inc. v. PharmAthene, Inc._ (Del. 2015) — expectation damages
  available when party breaches obligation to negotiate in good faith on LOI terms [VERIFY]
- Promissory estoppel doctrine for LOI reliance damages (restatement § 90) [VERIFY]
- HSR Act filing requirements and timing once deal is sufficiently definitive [VERIFY]

**United Kingdom:**

- English law position: no general duty to negotiate in good faith (_Walford v. Miles_
  [1992] 2 AC 128 — House of Lords) [VERIFY]
- Whether heads of terms / heads of agreement create binding obligations on specific
  provisions depends on language (_Cheverny Consulting Ltd v. Whitehead Mann Ltd_
  [2006]) [VERIFY]
- UK Takeover Panel Rule 21.2 on inducement fees / offer-related costs: limit 1% of
  deal value; requires Panel consent for amounts above de minimis [VERIFY]
- Offeror-side break-up fees must comply with City Code on Takeovers and Mergers for
  listed company targets [VERIFY]
- Companies Act 2006 board duties in sale processes; directors' duties to act in
  best interests of shareholders [VERIFY]

**European Union / Civil Law:**

- Culpa in contrahendo doctrine: obligation of good faith in pre-contractual negotiations
  under German BGB § 311(2), French Code Civil Article 1112-1, Dutch Civil Code [VERIFY]
- Pre-contractual liability for breaking off negotiations (applies even where LOI says
  "non-binding" in many EU jurisdictions) [VERIFY]
- MIFIR/MIFID II implications for financial institution transactions [VERIFY]
- EU FDI Regulation (Regulation 2019/452) and national FDI screening requirements
  where acquirer is from outside EU [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming the user's intent, the workflow pauses when:

- The answer would change the direction of the analysis
- Multiple valid approaches exist and the user's preference matters
- Transaction context is needed to correctly classify severity
- Jurisdiction-specific enforceability analysis requires user confirmation

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

## LOI Document Taxonomy

Before beginning the review, identify the type of preliminary document in hand. Different
document types carry different enforceability assumptions and market conventions.

| Document Type                         | Common Usage                                      | Typical Binding Status                                           | Jurisdiction                 |
| ------------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------- |
| **Letter of Intent (LOI)**            | M&A (private company); real estate; licensing     | Non-binding on economics; binding on process protections         | US primarily                 |
| **Heads of Terms (HoT)**              | M&A (UK private company); real estate; commercial | Same as LOI; UK convention                                       | UK primarily                 |
| **Term Sheet**                        | Venture financing; PE deals; licensing; JVs       | Often more specific than LOI; binding on key terms often debated | US, international            |
| **Memorandum of Understanding (MOU)** | Government, JV, cross-border; strategic alliances | Often explicitly non-binding; but conduct can override           | International                |
| **Indicative Offer Letter**           | M&A auction processes (first-round bids)          | Non-binding by convention; subject to DD and SPA                 | UK, US                       |
| **Agreement in Principle**            | M&A; financial transactions                       | Often treated as binding on essential terms                      | Risk: see Texaco v. Pennzoil |
| **Heads of Agreement**                | Commercial; M&A in Commonwealth jurisdictions     | Binding on process; non-binding on economics typical             | UK, Australia, NZ            |
| **Offer to Purchase (OTP)**           | Real estate; business acquisition                 | Often more binding than LOI; can become the purchase agreement   | US, international            |

**Identify the document type before applying the review.** LOI conventions differ from
MOU conventions, and the risk profile of an "agreement in principle" is categorically
different from an "indicative offer letter."

---

## Workflow

### Step 1: Accept the Document

Accept the LOI or term sheet in any format:

- **File**: PDF, DOCX, or other document
- **URL**: Link to document in cloud storage or data room
- **Pasted text**: Content pasted directly into the conversation

If no document is provided, prompt the user to supply one.

### Step 2: Gather Transaction Context

**⟁ CLARIFY** — Before beginning the review, ask these questions. Present as structured
options. Skip any already answered by the user.

1. **Which side are you on?**
   - Options: Buyer (acquirer), Seller (target company), Seller's shareholders,
     Financial advisor (buy-side), Financial advisor (sell-side), Target board (independent
     committee), Other
   - _Why this matters_: The entire analysis flips depending on which side you represent.
     Exclusivity protects the buyer; break-up fees protect the seller. What is a
     protection for one party is a burden for the other.

2. **What type of transaction is this?**
   - Options: M&A (private company acquisition), M&A (public company acquisition / tender
     offer), Private equity acquisition (financial sponsor), Joint venture formation,
     Strategic partnership / licensing deal, Real estate acquisition, Other
   - _Why this matters_: Public company M&A triggers Takeover Code rules in the UK and
     SEC disclosure requirements in the US. JV term sheets have different enforceability
     conventions. Real estate LOIs sometimes become purchase agreements by conduct.

3. **What is the approximate deal size?**
   - Options: < $10M, $10M–$100M, $100M–$1B, > $1B, Not disclosed
   - _Why this matters_: Market standards for break-up fees (as % of deal value) and
     exclusivity periods scale with deal size. A 3% break-up fee is market for a $50M
     deal; it is very high for a $2B deal.

4. **What is the governing law of the LOI?**
   - Options: Delaware (US), New York (US), Other US state, English law (UK), EU/civil
     law jurisdiction (specify), No governing law clause, Not yet determined
   - _Why this matters_: Enforceability of "non-binding" provisions and exposure to
     reliance damages / culpa in contrahendo liability vary dramatically by jurisdiction.
     An MOU that is entirely aspirational under New York law may create pre-contractual
     liability under German BGB § 311(2).

5. **What stage of the transaction is this?**
   - Options: Pre-due diligence (LOI signed first, DD to follow), Post-preliminary
     discussion (LOI formalizes agreed framework), Parallel (LOI and DD running
     simultaneously), Advanced (LOI executed; definitive agreement in negotiation)
   - _Why this matters_: An LOI signed pre-DD has different risk than one signed post-DD.
     Conditions precedent to closing may be redundant or under-specified at the pre-DD
     stage.

6. **Has there been a prior NDA covering this transaction?**
   - Options: Yes — standalone NDA in place, Yes — but the LOI contains all confidentiality
     provisions, No — the LOI is the first document, Unknown
   - _Why this matters_: If a standalone NDA exists, the confidentiality provisions in
     the LOI need to be aligned. Conflicting confidentiality regimes create gaps.

**⟁ CLARIFY** — After answering, ask:

7. **Do you have a transaction playbook or deal positions document?**
   - Options: Yes — provide it now, No — proceed with general market standards,
     No — I will give you our key positions as we go
   - _Why this matters_: A transaction playbook defines acceptable and unacceptable
     positions for this party. Without one, the review defaults to current market
     standards as reported in ABA studies, SRS Acquiom data, and practitioner guidance.

### Step 3: Load the Transaction Playbook

If a playbook is provided, load it and extract the party's stated positions on:

- Acceptable exclusivity period duration and any go-shop rights
- Break-up fee / reverse break-up fee positions (% of deal value; triggers)
- Confidentiality duration, residuals clause position, and permitted disclosures
- Acceptable conditions precedent (definitive agreement / regulatory / financing)
- Expense allocation positions (who pays for failed deal; any deposit requirement)
- Governing law preference

If no playbook is provided, apply these general market standards as defaults (mark all
with `[General market standards — not party-specific]`):

| Provision                           | Buyer Default       | Seller Default                      | Market Range                                        |
| ----------------------------------- | ------------------- | ----------------------------------- | --------------------------------------------------- |
| Exclusivity period                  | 60–90 days          | 30–45 days                          | 30–120 days depending on deal complexity            |
| Break-up fee (buyer walks)          | Not preferred       | 1–3% of deal value                  | 0.5–5% (public: Rule 21.2 cap UK)                   |
| Reverse break-up fee (seller walks) | 3–5% of deal value  | Avoided                             | 3–8% (financing failure up to 6%)                   |
| Confidentiality term (post-signing) | 2–3 years           | 3–5 years                           | 2–5 years standard                                  |
| Due diligence scope                 | Full scope          | Limited scope; management time cost | Agreed access protocol                              |
| Expense allocation                  | Each party pays own | Each party pays own                 | Market: own-expenses; deviations need justification |
| Deposit / earnest money             | None preferred      | 2–5% of deal value                  | Deal-specific                                       |

### Step 4: Classify the Document's Binding Posture

Before clause-by-clause review, assess the LOI's overall binding posture. This is the
single most important analytical step — it sets the frame for all subsequent analysis.

#### Binding Strength Classification

Assess the document's overall characterization and intended legal effect:

| Classification              | Definition                                                                                                           | Key Indicator Language                                                                                       | Risk                                                                                    |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| **FULLY BINDING**           | Document is intended to be a binding contract on all substantive terms                                               | "This agreement is legally binding"; explicit consideration; no "subject to definitive agreement" carveout   | HIGH — parties are committed to the deal structure; walk-away rights limited            |
| **PARTIALLY BINDING**       | Core economic terms non-binding; specific provisions (exclusivity, confidentiality, break-up fee) explicitly binding | "The provisions of Sections X, Y, Z are legally binding on the parties" with explicit carveout for economics | MEDIUM — binding scope clearly delineated; enforceability risk on ambiguous terms       |
| **NOMINALLY NON-BINDING**   | Document states it is non-binding but contains specific binding provisions                                           | "This letter is non-binding in its entirety except for [list]"                                               | LOWER — but still check conduct and reliance for estoppel risk                          |
| **AMBIGUOUSLY NON-BINDING** | Document uses non-binding language inconsistently or fails to specify which provisions bind                          | "This letter of intent is not intended to be binding" without clear scope                                    | HIGH — risk of court finding binding obligations; see Texaco v. Pennzoil analysis below |
| **UNINTENTIONALLY BINDING** | Document does not claim to bind parties but conduct and reliance has created enforceable obligations                 | Post-LOI conduct consistent with commitment; significant reliance expenditures; part performance             | CRITICAL — obligations may exist regardless of document language                        |

#### Enforceability Risk: The Texaco v. Pennzoil Framework

Under US law (particularly in New York and Delaware), courts use a four-factor test to
determine whether a preliminary agreement is binding [VERIFY — jurisdiction-specific]:

1. **Whether the contract is of a type that is usually committed to writing** — M&A
   deals above a threshold are typically committed to writing; oral or letter agreements
   on essential terms can still bind.

2. **Whether there has been partial performance of the contract** — If either party has
   begun performing (sharing confidential information for DD, dedicating management time,
   making exclusivity commitments), this weighs toward binding effect.

3. **Whether all of the terms of the alleged contract have been agreed upon** — Agreement
   on all essential terms (price, structure, key conditions) weighs toward binding; if
   material terms remain open, weighs against binding.

4. **Whether the agreement is complex, requiring many contracts to be negotiated** — For
   very complex deals, courts may find that parties expected a more formal document; for
   simpler deals, a letter agreement may suffice.

Mark each LOI section with its enforceability risk level:

- **BINDING**: Language and context clearly create an enforceable obligation
- **AMBIGUOUS**: Language is unclear; court could find either way; [VERIFY] risk
- **NON-BINDING**: Language and context clearly establish non-binding intent

### Step 5: Gather Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** (if connected) to search for:

- Current case law on LOI enforceability in the identified governing law jurisdiction
- Recent regulatory developments affecting the transaction type (UK Takeover Code updates,
  US SEC guidance, HSR thresholds, EU merger control thresholds)
- Any jurisdiction-specific mandatory provisions that override LOI language

If legalcode-mcp is not connected, proceed with research-based analysis only. Mark all
case citations and statutory references with [VERIFY] until confirmed via authoritative
sources.

Save results to `/tmp/loi-review-research.md` if created.

### Step 6: LOI Mechanics Assessment

Before clause-by-clause analysis, assess the key LOI mechanics at a high level:

| Mechanic              | LOI Provision                           | Market Standard                                    | Assessment             |
| --------------------- | --------------------------------------- | -------------------------------------------------- | ---------------------- |
| Binding intent        | [explicit / implicit / absent]          | Explicit and clear                                 | [GREEN / YELLOW / RED] |
| Exclusivity period    | [duration]                              | 60–90 days (private M&A)                           | [GREEN / YELLOW / RED] |
| Break-up fee          | [% of deal value / absent]              | 1–3% (seller protection)                           | [GREEN / YELLOW / RED] |
| Reverse break-up fee  | [% of deal value / absent]              | 3–5% (buyer commits to financing)                  | [GREEN / YELLOW / RED] |
| Confidentiality scope | [integrated / standalone NDA reference] | Standalone NDA or clear LOI provision              | [GREEN / YELLOW / RED] |
| Conditions to closing | [specified / vague / absent]            | Key conditions identified                          | [GREEN / YELLOW / RED] |
| DD scope              | [defined / open-ended / absent]         | Scope and timing defined                           | [GREEN / YELLOW / RED] |
| Expense allocation    | [each party / other]                    | Each party pays own expenses                       | [GREEN / YELLOW / RED] |
| Governing law         | [specified / absent]                    | Specified; consistent with negotiated expectations | [GREEN / YELLOW / RED] |

Flag any critical structural issues before proceeding to clause-by-clause analysis.
A missing governing law clause in an LOI creates higher enforceability risk than
almost any other single gap.

### Step 7: Clause-by-Clause Analysis

Analyze the LOI across 12 analytical categories organized in 4 parts. For each category:

1. Identify the binding or non-binding status of the provision
2. Assess the enforceability risk
3. Compare to market standards
4. Generate redlines where the provision is RED or where binding intent is ambiguous

---

## Part A — Document Foundation

### A-1: Document Characterization and Binding Intent

**Purpose**: Assess whether the LOI clearly states which provisions are binding and which
are not. This is the most critical section of the LOI.

**GREEN (Adequate):**

- Clear statement that the LOI is non-binding in its entirety except for specifically
  named provisions (e.g., "except for Sections 4 [Exclusivity], 5 [Confidentiality],
  and 6 [Expenses], this letter of intent is not binding on either party")
- The binding sections are individually identifiable by section number or heading
- The non-binding characterization is unambiguous ("not legally binding," "not a
  commitment to consummate the Transaction")
- The LOI states explicitly that obligation to consummate is "subject to execution of
  a definitive written agreement"

**YELLOW (Marginal):**

- Non-binding language present but not explicitly applied to individual provisions
- Binding vs. non-binding distinction present but imprecise in scope
- LOI states it is "subject to further negotiation" without specifying which terms remain open
- Binding provisions listed but the list may be incomplete

**RED (Inadequate):**

- No statement of binding intent anywhere in the document
- Document uses language of present obligation ("the parties agree to") without non-binding
  disclaimer
- "This letter is non-binding" but immediately followed by obligation language that
  contradicts the disclaimer (e.g., "Buyer agrees to pay Seller $X")
- "Agreement in principle" language without explicit non-binding carveout

**Unintentional Binding Risk Checklist:**

- [ ] Does any section use language of present obligation without non-binding qualifier?
- [ ] Have the parties taken significant actions in reliance on the LOI?
- [ ] Does the LOI contain all essential terms of the transaction (price, structure,
      timing, parties)?
- [ ] Is there partial performance by either party (payment, disclosure, dedicated resources)?
- [ ] Would a court find that the parties intended to be bound based on their conduct?

---

### A-2: Binding Scope Mapping

**Purpose**: Map every provision in the LOI to its intended binding status and identify
gaps or inconsistencies.

Create a binding scope map:

| LOI Section | Provision       | Intended Status | Actual Language    | Risk                            |
| ----------- | --------------- | --------------- | ------------------ | ------------------------------- |
| [Section]   | Purchase Price  | Non-binding     | [language summary] | [BINDING/AMBIGUOUS/NON-BINDING] |
| [Section]   | Exclusivity     | Binding         | [language summary] | [BINDING/AMBIGUOUS/NON-BINDING] |
| [Section]   | Confidentiality | Binding         | [language summary] | [BINDING/AMBIGUOUS/NON-BINDING] |
| [Section]   | Break-up Fee    | Binding         | [language summary] | [BINDING/AMBIGUOUS/NON-BINDING] |
| [Section]   | Conditions      | Non-binding     | [language summary] | [BINDING/AMBIGUOUS/NON-BINDING] |
| [Section]   | Governing Law   | Binding         | [language summary] | [BINDING/AMBIGUOUS/NON-BINDING] |

Flag any mismatch between intended status and actual language risk.

---

### A-3: Unintentional Binding Risk Assessment

**Purpose**: Assess whether the LOI creates binding obligations through conduct, reliance,
or estoppel even where the document states non-binding intent.

**Key risk factors (score each 0–2; total 0–10):**

| Risk Factor                      | Score 0               | Score 1                             | Score 2                                       |
| -------------------------------- | --------------------- | ----------------------------------- | --------------------------------------------- |
| **Essential terms completeness** | Material terms open   | Most terms agreed                   | All essential terms agreed                    |
| **Reliance by either party**     | None                  | Modest (< $50K)                     | Significant (> $500K or strategic commitment) |
| **Partial performance**          | None                  | One party beginning performance     | Both parties performing                       |
| **Post-LOI conduct**             | No performance        | Some consistency with completion    | Strong indicia of commitment                  |
| **Prior course of dealing**      | No prior relationship | Established commercial relationship | Prior binding LOIs treated as binding         |

**Risk Assessment:**

- **0–3**: LOW unintentional binding risk — non-binding disclaimer likely effective
- **4–6**: MEDIUM unintentional binding risk — review carefully; seek legal advice on
  pre-contractual liability exposure
- **7–10**: HIGH unintentional binding risk — parties may be bound regardless of LOI
  language; immediate legal review recommended

[JURISDICTION-SPECIFIC] Under civil law systems (Germany, France, Netherlands), even a
score of 3 may trigger culpa in contrahendo liability if negotiations are broken off
without legitimate reason. The applicable legal standard differs from common law [VERIFY].

---

## Part B — Economic Framework

### B-1: Purchase Price and Consideration

**Purpose**: Assess whether the purchase price (or valuation framework) is adequately
specified given its non-binding status, and identify any provisions that could inadvertently
lock in pricing before due diligence is complete.

**Typical LOI price provisions:**

- **Fixed price**: Specific dollar amount (e.g., "$50 million")
- **Valuation basis**: EV/EBITDA multiple or other formula (e.g., "6x trailing 12-month EBITDA")
- **Price range**: Upper/lower bound depending on DD findings
- **Price subject to working capital adjustment**: Placeholder mechanism

**GREEN (Adequate):**

- Price is clearly characterized as non-binding and subject to adjustment post-DD
- Valuation basis and adjustment mechanism (if any) are clearly described
- Price is consistent with preliminary discussions and reasonable for the deal stage
- Any earn-out or contingent consideration is noted as subject to definitive agreement
- Working capital normalization approach identified (locked box vs. completion accounts)

**YELLOW (Marginal):**

- Price stated without clear non-binding qualifier (creates inadvertent anchor)
- Adjustment mechanism referenced but not defined ("working capital adjustment as agreed")
- Price range provided but no mechanism for resolving within-range disputes
- Earn-out included in LOI without clear framework or non-binding qualifier

**RED (Inadequate):**

- Price uses binding language ("Buyer agrees to pay") without non-binding disclaimer
- Price stated as fixed without acknowledgment that DD may affect valuation
- No price at all — risk that courts infer market value as binding consideration
- Price stated as "TBD" or "to be negotiated" — creates risk that the LOI is an
  unenforceable agreement to agree under New York law [VERIFY]

**Buyer-side issues:**

- Beware of price stated as a multiple — if EBITDA definition is not included, seller
  can inflate the denominator
- Confirm whether price is equity value or enterprise value; confirm treatment of debt,
  cash, and working capital
- Working capital peg: if unspecified, buyer carries risk that closing WC differs from
  LOI assumption

**Seller-side issues:**

- Avoid agreeing to a price adjustment mechanism in the LOI that locks in a seller-
  adverse formula before the mechanism is fully negotiated in the definitive agreement
- Price ranges favor buyers — narrow the range before signing exclusivity

---

### B-2: Deal Structure and Transaction Form

**Purpose**: Assess whether the deal structure is adequately characterized and whether
the structure choice creates unintended obligations or omits key considerations.

**Structure options and LOI implications:**

| Structure                     | Key LOI Issues                                                                             | Buyer Risk                                                           | Seller Risk                                                |
| ----------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Stock / Share Purchase**    | Anti-assignment clauses do NOT typically trigger; change-of-control provisions MAY trigger | Inherits all target liabilities                                      | Cannot cherry-pick assets                                  |
| **Asset Purchase**            | Anti-assignment clauses DO typically trigger; bulk sales compliance may apply              | Must identify each asset; assumed liabilities subject to negotiation | Tax treatment typically worse (double taxation risk in US) |
| **Forward Merger**            | Requires shareholder vote; Revlon duties triggered for public targets                      | Slower process                                                       | Board process requirements                                 |
| **Reverse Triangular Merger** | Typical for US acquisitions; target becomes wholly-owned subsidiary                        | Preserves target's contracts                                         | Tax treatment depends on elections                         |
| **Earnout-heavy**             | Contingent consideration; definition of metrics is critical                                | Business integration restrictions                                    | Revenue recognition risk                                   |

**GREEN:** Structure clearly identified; key implications acknowledged in LOI.
**YELLOW:** Structure identified but key structural implications not addressed (e.g.,
asset purchase without mentioning anti-assignment issues; share purchase without noting
change-of-control provisions).
**RED:** Structure not specified; or structure specified without awareness of critical
legal implications for the deal.

[JURISDICTION-SPECIFIC] In cross-border transactions, structure affects withholding tax,
branch profits tax, and local law mandatory offer rules. A US acquirer purchasing a UK
subsidiary should consider UK stamp duty (0.5% on share purchases) and potential SDLT
on real property assets [VERIFY].

---

### B-3: Break-Up Fees and Reverse Break-Up Fees

**Purpose**: Assess the fee structure for deal termination, evaluate market-standard
compliance, and identify gaps in fee trigger language.

#### Termination Fee Types

| Fee Type                             | Who Pays | Triggered When                                                             | Market Standard (US Private M&A)                                   |
| ------------------------------------ | -------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Break-up fee (target fee)**        | Seller   | Seller terminates LOI or definitive agreement to accept superior proposal  | 1–3% of deal value                                                 |
| **Reverse break-up fee (buyer fee)** | Buyer    | Buyer fails to close for specified reasons (financing failure, regulatory) | 3–5% of deal value; up to 8% for financing failure                 |
| **Termination fee (mutual)**         | Either   | Walk-away for any reason                                                   | Less common; smaller amount                                        |
| **Earnest money deposit**            | Buyer    | Forfeited to seller if buyer breaches                                      | 2–5% of deal value (real estate convention; sometimes used in M&A) |

[JURISDICTION-SPECIFIC] **UK public company M&A (Takeover Panel rules):**

- Rule 21.2 of the City Code on Takeovers and Mergers restricts "inducement fees" to
  a maximum of 1% of the offer value, subject to Panel consent [VERIFY]
- Reverse break-up fees (payable by bidder) are not subject to the same restriction,
  but the Panel must be consulted for non-standard structures [VERIFY]
- Inducement fees must be publicly disclosed [VERIFY]

**GREEN (Adequate — buyer-side):**

- Reverse break-up fee is clearly defined with specific trigger events
- Financing failure is expressly addressed as a trigger (or expressly excluded with
  financing representation instead)
- Reverse break-up fee is buyer's sole remedy for seller's claim upon buyer default
  (limits seller exposure to specific performance)

**GREEN (Adequate — seller-side):**

- Break-up fee amount is within market range (1–3% for deals above $50M)
- Trigger events are clearly defined and limited to genuinely adverse seller conduct
- Break-up fee is not the seller's exclusive remedy against buyer (seller retains
  specific performance right)

**YELLOW:**

- Fee triggers include "any termination" rather than specific breach or superior proposal
  acceptance — overbroad
- Fee amount is at the edge of market range (< 0.5% or > 5%) without justification
- Reverse break-up fee is the buyer's sole remedy even for intentional fraud (should
  not be sole remedy for fraud)
- No anti-assignment of fee obligation — fee should survive corporate reorganization

**RED:**

- Break-up fee absent: seller has no protection if buyer walks after exclusivity
- Reverse break-up fee absent: buyer has no committed deal certainty mechanism;
  seller can walk at will without consequence
- Trigger events are vague ("material breach of obligations") without reference to the
  specific obligations being breached
- Fee is so high (> 10%) it may constitute a penalty clause and be void as unliquidated
  damages in some jurisdictions [VERIFY — jurisdiction-specific]

**Post-COVID deal certainty note (2021–2025):** Post-pandemic, reverse break-up fees
have increased in prevalence. In 2023, approximately 60% of deals over $500M included
a reverse break-up fee, up from 36% in 2019. This trend reflects increased deal
uncertainty (financing market volatility, regulatory scrutiny). LOIs without a reverse
break-up fee in this environment leave sellers exposed [VERIFY market data].

---

## Part C — Process Protections

### C-1: Exclusivity / No-Shop / No-Talk Covenants

**Purpose**: Assess whether exclusivity and no-shop provisions are market-standard,
whether they adequately protect the buyer's diligence investment, and whether the seller
retains appropriate fiduciary flexibility.

#### Key Distinctions

| Type                 | Definition                                                        | Seller's Ability to Respond to Unsolicited Interest   |
| -------------------- | ----------------------------------------------------------------- | ----------------------------------------------------- |
| **No-shop**          | Seller shall not solicit alternative transactions                 | Cannot solicit; can respond to unsolicited            |
| **No-solicitation**  | Seller shall not solicit or facilitate alternative transactions   | Cannot solicit; limited ability to respond            |
| **No-talk**          | Seller shall not solicit or discuss alternative transactions      | Cannot solicit or discuss even unsolicited approaches |
| **Full exclusivity** | No-talk plus no disclosure of deal pending                        | Most restrictive; problematic for public targets      |
| **Go-shop**          | Post-signing right to solicit alternative bids for defined period | Affirmatively permitted during go-shop period         |

**Duration: Market Standards**

| Deal Size   | Typical Exclusivity Period | Justification                               |
| ----------- | -------------------------- | ------------------------------------------- |
| < $25M      | 30–60 days                 | Simpler diligence; faster SPA negotiation   |
| $25M–$100M  | 45–90 days                 | Standard diligence; moderate complexity     |
| $100M–$500M | 60–120 days                | Complex diligence; regulatory consideration |
| > $500M     | 90–180 days                | Full diligence; regulatory; cross-border    |

**GREEN (Adequate):**

- Duration is within market range for deal size
- No-shop provisions preserve seller's ability to respond to unsolicited approaches
  (fiduciary out)
- Exclusivity has a clear drop-dead date after which exclusivity terminates automatically
- Extension mechanism requires mutual written consent (seller retains control)
- For public company targets: fiduciary out explicitly preserved for board to exercise
  judgment on superior proposals

**YELLOW:**

- Duration is longer than market range (seller should seek to shorten)
- No-talk provision without fiduciary out — creates tension with board fiduciary duties
  for public targets and may violate Revlon obligations [VERIFY — Delaware law]
- Exclusivity extends automatically unless one party objects (creates rolling exclusivity
  without seller agreement)
- Breach of exclusivity gives buyer claim for specific performance (rarely appropriate
  for process breach)

**RED:**

- Indefinite exclusivity ("until the parties execute a definitive agreement or agree to
  terminate negotiations") — seller loses all negotiating leverage and time pressure
- No-talk without fiduciary exception for a public target board — may breach directors'
  duties and expose board members to liability [VERIFY]
- Exclusivity prohibits seller from conducting auction even before LOI; applicable to
  past as well as future solicitation efforts (cannot restrict pre-LOI contacts)
- No mechanism for buyer to lose exclusivity if milestones are not met (e.g., if buyer
  fails to submit SPA markup within X days, exclusivity terminates)
- Seller represents there are no ongoing discussions with other parties — creates
  representation with indemnification exposure

**Buyer-side negotiation priorities:**

- Maximize duration while market testing has been limited
- No-talk provisions are stronger than no-shop
- Include milestone schedule (DD completion dates, SPA delivery dates) to ensure deal
  progresses during exclusivity
- Include seller obligation to promptly notify buyer of any unsolicited approach received
  during exclusivity

**Seller-side negotiation priorities:**

- Limit to no-shop (not no-talk) — preserve ability to respond to superior proposals
- Require fiduciary out explicitly: "notwithstanding the foregoing, seller's board may
  respond to unsolicited bona fide proposals from third parties where failure to do so
  would reasonably be expected to constitute a breach of directors' fiduciary duties"
- Set a drop-dead date; do not allow open-ended extensions without affirmative seller
  consent
- Include milestone obligations on buyer (e.g., "Buyer shall deliver its initial SPA
  draft within 30 days of LOI execution")

[JURISDICTION-SPECIFIC] **Delaware:** Revlon duties are triggered when a company is
put "in play" for sale. Even where an LOI restricts the board, Delaware courts may
require the board to respond to a clearly superior proposal. A no-talk without fiduciary
out should be reviewed carefully by Delaware counsel [VERIFY]. **UK:** English courts
have held that an agreement to negotiate exclusively is enforceable where sufficiently
certain (_Walford v. Miles_ notwithstanding specific exclusivity clauses) [VERIFY].

---

### C-2: Confidentiality Obligations

**Purpose**: Assess whether confidentiality provisions in the LOI are adequate, consistent
with any standalone NDA, and whether they protect both parties appropriately.

#### LOI Confidentiality vs. Standalone NDA

Most transactions involve a standalone NDA before the LOI is signed. The LOI may:

1. **Incorporate the standalone NDA by reference** (preferred — no duplication)
2. **Contain standalone confidentiality provisions** (common in simpler transactions)
3. **Contain confidentiality provisions that conflict with the NDA** (dangerous — gap risk)
4. **Contain no confidentiality provisions** (dangerous — NDA must cover the LOI itself)

**GREEN (Adequate):**

- LOI explicitly references and incorporates the standalone NDA (e.g., "The existing
  NDA dated [date] between the parties is incorporated herein and governs disclosure
  of Confidential Information")
- If standalone: confidentiality provisions are adequate, include definition of
  Confidential Information, standard carveouts (public domain, independent development,
  compelled disclosure), duration (post-signing), and remedies (equitable relief)
- LOI terms themselves are marked confidential and subject to the NDA
- Permitted disclosures defined (advisors, financiers, regulatory authorities)

**YELLOW:**

- LOI references a standalone NDA but confidentiality provisions in the LOI are
  inconsistent with the NDA (e.g., different duration, different carveouts)
- Confidentiality provisions in the LOI are narrower than the NDA (creates gap for
  information shared pursuant to the LOI)
- Duration of confidentiality is short (< 2 years after termination)
- Residuals clause: "Notwithstanding the foregoing, each party may use Residuals for
  any purpose" — residuals clauses can swallow the confidentiality obligation if not
  carefully circumscribed

**RED:**

- No confidentiality provisions in LOI and no standalone NDA — target's confidential
  information (financials, customer lists, trade secrets) shared during DD without protection
- Confidentiality obligations are unilateral (only seller is bound; buyer retains
  complete freedom to use information)
- No injunctive remedy provision — damages may be inadequate remedy for breach
- Permitted disclosures include "affiliates" without restricting affiliate use to the
  transaction — creates data leak risk through buyer's group companies

**Duration standards:**

- 2–3 years post-termination: standard market for general commercial transactions
- 3–5 years post-termination: technology and trade secret heavy deals
- Indefinitely for trade secrets under DTSA [VERIFY]: separate provision for trade
  secrets often prudent

---

### C-3: Due Diligence Scope and Access

**Purpose**: Assess whether the LOI adequately defines the scope of due diligence,
access rights, and any limitations that protect the seller during the process.

**GREEN (Adequate):**

- DD scope is described at a high level (financial, legal, tax, operational)
- Access to management is defined (e.g., one management presentation; subsequent access
  by reasonable request)
- Data room access process described (virtual data room; information request list within
  X days)
- Seller's right to limit access to sensitive competitive information acknowledged
  (firewall provisions for sensitive customer/supplier data)
- Timeline for DD completion identified

**YELLOW:**

- DD scope not described (open-ended access obligation creates management disruption risk)
- No management access limitations — seller management could be exhausted by buyer's
  unlimited requests
- No timeline for DD completion — exclusivity period can expire without completion

**RED:**

- Full and unrestricted access to all business records and personnel — seller has no
  protection for trade secrets or competitive information being shared with a potential
  competitor buyer
- No data room process — seller has no record of what was disclosed (critical for
  warranty and indemnification analysis in the SPA)
- No limitation on buyer's right to contact customers, suppliers, employees without
  seller's consent — creates significant relationship and business disruption risk

---

## Part D — Closing Framework

### D-1: Conditions Precedent to Closing

**Purpose**: Assess whether conditions precedent to closing are adequately specified in
the LOI, whether they are objectively determinable, and whether any condition creates a
right to walk away that one party controls.

**Common conditions precedent in LOIs:**

| Condition                                             | Who Controls | Risk                                                              |
| ----------------------------------------------------- | ------------ | ----------------------------------------------------------------- |
| Satisfactory completion of due diligence              | Buyer        | Buyer can invoke to walk away if DD finds any adverse information |
| Execution of mutually acceptable definitive agreement | Both         | Agreement to agree — high risk if not qualified                   |
| No material adverse change                            | Buyer        | Trigger definition is critical                                    |
| Regulatory approval (antitrust, FDI screening)        | Regulator    | Neither party controls; timing risk                               |
| Financing (debt or equity commitment)                 | Buyer        | If deal is "fully financed," this should not appear               |
| Board / shareholder approval                          | Both         | Standard; timeline matters                                        |
| Key employee retention                                | Buyer        | Creates pressure on seller management                             |
| Third-party consents (material contracts)             | Neither      | Can be deal-killer if major consents required                     |

**GREEN (Adequate):**

- Conditions are specific and objectively determinable (e.g., "regulatory approval from
  [specific regulators]" not "all required regulatory approvals")
- Satisfactory DD condition is defined: "Buyer, in its sole but reasonable discretion,
  not discovering any material adverse finding during DD" — "reasonable" qualifier limits
  walk-away right
- MAC/MAE definition includes exceptions (market-wide conditions, COVID-type pandemic
  risks) that prevent opportunistic invocation
- Definitive agreement condition specifies timeline for negotiation and mechanism if
  parties cannot agree

**YELLOW:**

- "Satisfactory completion of due diligence in buyer's sole discretion" without
  reasonable qualifier — gives buyer an unfettered option to walk away at no cost
- MAC/MAE condition without definition or exceptions — buyer can invoke on any adverse
  change, no matter how minor or market-wide
- Financing condition present without financing representation — signals buyer has not
  secured financing; creates execution risk for seller

**RED:**

- Conditions are open-ended ("all conditions precedent to closing as agreed in the
  definitive agreement") — creates circular reference; conditions unspecified
- All conditions are buyer-beneficial with no seller-protective conditions (e.g., no
  buyer obligation to maintain reps and warranties or operate in ordinary course)
- "Execution of a definitive agreement satisfactory to Buyer in its sole discretion" —
  this is effectively no agreement at all; buyer retains complete optionality

**MAE/MAC in LOIs — Post-COVID Considerations:**
Post-pandemic deal drafting has narrowed MAC definitions to exclude pandemics and
market-wide conditions as triggers. LOIs written before 2020 or with broad MAE
definitions should flag this as a gap. Key exclusions that should appear:

- General economic conditions affecting the market as a whole
- Industry-wide changes affecting companies in the same sector
- Changes in applicable laws or regulations
- Actions taken at Buyer's request or direction
- Natural disasters, pandemics, or force majeure events

[JURISDICTION-SPECIFIC] Delaware courts have held that proving a MAC is an
extremely high bar — the Delaware Court of Chancery declined to find a MAC in
_Akorn, Inc. v. Fresenius Kabi AG_ (Del. Ch. 2018) even after substantial target-
specific deterioration [VERIFY]. UK courts have applied a similarly high threshold
in recent decisions [VERIFY].

---

### D-2: Expense Allocation

**Purpose**: Assess how the LOI allocates costs if the transaction does not close, and
identify exposure to reliance damages or pre-contractual liability.

**Standard market positions:**

| Scenario                             | Market Standard                         | High-Risk Alternative              |
| ------------------------------------ | --------------------------------------- | ---------------------------------- |
| Deal closes                          | Each party bears its own costs          | —                                  |
| Buyer walks (no breach)              | Each party bears own costs              | Buyer pays seller's break-up costs |
| Seller walks (no breach)             | Each party bears own costs              | Seller pays break-up fee           |
| Buyer walks (breach of exclusivity)  | Buyer pays seller's documented DD costs | Specific performance               |
| Seller walks (breach of exclusivity) | Seller pays break-up fee                | Liquidated damages                 |
| Regulatory termination               | Each party bears own costs              | Deal-specific                      |

**GREEN (Adequate):**

- Each party bears its own costs and expenses (lawyers, advisors, DD costs) in all scenarios
- Break-up fee is the exclusive remedy for each party's breach (no additional damages)
- Reimbursement of documented expenses limited to breach scenarios with a specific cap
- Expense allocation is symmetric (both buyer and seller bear own costs)

**YELLOW:**

- Seller bears buyer's DD costs if seller terminates for any reason (not just breach)
  — overbroad expense allocation against seller
- Expense caps are insufficient relative to likely DD cost (e.g., $50K cap on a $200M
  deal where buyer's legal fees alone may exceed $500K)
- No specification of expense calculation method — potential for dispute over what
  constitutes a reimbursable expense

**RED:**

- Seller bears all of buyer's costs (including financing costs, advisory fees) if deal
  does not close — potentially uncapped and crushing liability for seller
- No expense provisions at all: creates reliance damages exposure under applicable law
  without agreed limitation
- Expense allocation triggers on seller's unilateral judgment that buyer has breached —
  creates dispute risk

[JURISDICTION-SPECIFIC] **Civil law jurisdictions:** Even where the LOI says each party
pays own costs, courts in Germany, France, and the Netherlands may award reliance damages
(culpa in contrahendo) where one party breaks off negotiations after inducing substantial
expenditure by the other. This is particularly acute where:

- The withdrawing party had no legitimate reason to abandon negotiations
- The other party made significant expenditures in reasonable reliance
- The withdrawing party had information at the time of the LOI that should have prevented
  them from entering into negotiations [VERIFY].

---

### D-3: Governing Law and Dispute Resolution

**Purpose**: Assess whether the LOI's governing law and dispute resolution provisions
are adequate, and whether they are consistent with what will govern the definitive agreement.

**Why governing law is critical for LOIs specifically:**

- Governing law determines whether "non-binding" language is effective
- It determines whether promissory estoppel or culpa in contrahendo applies
- It determines the enforceability of exclusivity and break-up fee provisions
- It governs whether specific performance is available as a remedy

**GREEN (Adequate):**

- Governing law explicitly stated and consistent with transaction parties' expectation
  (e.g., Delaware for US corporate transactions; English law for UK-domiciled deals)
- Dispute resolution mechanism specified (courts or arbitration; exclusive jurisdiction
  clause)
- Forum clause consistent with governing law (Delaware courts for Delaware law; LCIA
  or ICC arbitration for English law cross-border)
- Choice of law consistent with anticipated governing law of the definitive agreement
  (avoiding split-law issues)

**YELLOW:**

- Governing law stated but forum for dispute resolution absent — creates multi-forum
  litigation risk
- Different governing law for LOI vs. anticipated governing law for definitive agreement
  — creates interpretive disconnect (LOI enforceable as breach of contract; SPA analysis
  under different law)
- Arbitration specified but no arbitral rules, seat, or number of arbitrators stated —
  unenforceable arbitration clause in some jurisdictions [VERIFY]

**RED:**

- No governing law clause — creates risk that different courts apply different law;
  particularly dangerous for cross-border transactions
- Forum selection clause that does not align with chosen governing law (e.g., Delaware
  law but French courts — creates enforceability uncertainty)
- Governing law of a jurisdiction with strong culpa in contrahendo doctrine (Germany,
  France) but parties not aware that "non-binding" language may be ineffective

**Jurisdiction preferences (market convention):**

- US domestic deals: Delaware or New York (predictable, sophisticated courts)
- UK deals: English law; Commercial Court or LCIA arbitration
- Cross-border EU: English law or arbitration (ICC, LCIA) in international
  financial center
- Asian deals: Singapore law / SIAC or Hong Kong / HKIAC arbitration as alternatives
  to English or New York law

---

## Gap Analysis: Provisions Missing Before Signing

After completing the clause-by-clause analysis, check for provisions that should appear
in the LOI but are absent. A gap at the LOI stage creates negotiation complexity when
it surfaces in the definitive agreement — better to address it now.

### Critical Gaps (Must Add Before Signing)

- [ ] **Binding vs. non-binding delineation**: If absent, the entire LOI is ambiguous
- [ ] **Governing law**: If absent, enforceability of the LOI itself is uncertain
- [ ] **Exclusivity duration and drop-dead date**: Open-ended exclusivity favors buyer
- [ ] **Confidentiality**: If no standalone NDA and LOI lacks provisions, DD is unprotected
- [ ] **Break-up fee / reverse break-up fee**: If absent, walk-away has no consequence
- [ ] **Conditions to closing**: If absent, buyer has unlimited optionality with no commitment

### Important Gaps (Should Add Before Signing)

- [ ] **DD scope and timeline**: Protects seller; ensures buyer cannot extend indefinitely
- [ ] **Expense allocation on breach**: Without this, reliance damages are uncapped
- [ ] **Dispute resolution mechanism**: Prevents forum shopping post-LOI
- [ ] **Milestone obligations**: Without these, exclusivity period can lapse without progress
- [ ] **Treatment of LOI on execution of definitive agreement**: Does the LOI survive?

### Nice-to-Have Additions

- [ ] **Public announcement provisions**: Who can say what; when
- [ ] **Employee provisions**: Non-solicitation of key employees during DD
- [ ] **Representations on deal authority**: Buyer's board has authorized the transaction
- [ ] **Specific performance right for exclusivity**: Buyers should have ability to
      enforce exclusivity breach by specific performance, not just damages

---

## Negotiation Priority Framework

### Tier 1 — Must-Haves (Deal Conditions)

These issues require resolution before the LOI should be signed:

1. Clear binding vs. non-binding delineation with specific provision identification
2. Governing law clause — if absent, add before signature
3. Exclusivity period with drop-dead date and extension mechanism requiring mutual consent
4. Break-up fee / reverse break-up fee — at least one or both; amount and triggers clear
5. Confidentiality adequate for information to be shared during DD
6. Conditions to closing are specific (not "all conditions as agreed in the definitive
   agreement")

### Tier 2 — Strong Preferences (Material Negotiation Points)

These issues materially affect risk but have room for negotiation:

1. DD scope and timeline definition
2. Fiduciary out language for seller's board (if no-talk provision present)
3. MAC/MAE definition with post-COVID exceptions
4. Expense allocation on breach with cap
5. Milestone obligations on buyer during exclusivity
6. Dispute resolution mechanism aligned with governing law

### Tier 3 — Nice-to-Haves (Concession Candidates)

These issues improve position but can be conceded strategically:

1. Preferred governing law (if alternative is acceptable)
2. Specific arbitration institution vs. court litigation
3. Employee non-solicitation during DD
4. Public announcement timing
5. Management access protocols
6. Data room access mechanics

---

## Quality Assurance Frameworks

### Citation Quality Gates

Run these 5 gates before delivering output. If any gate fails, revise before delivering.

| Gate           | Rule                                                                                                                               | Fail Action                                              |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, case, or established market principle                                                  | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction                                                        | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments or repeal; market data for the relevant deal-size cohort and year                     | Flag "[CHECK CURRENCY — may be outdated]"                |
| **Domain**     | Analysis stays within LOI's governing law. No jurisdiction bleed (e.g., do not apply Revlon doctrine to English law transactions). | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden. If uncertain, say so.                                                                   | Add confidence qualifier                                 |

### Self-Interrogation for RED Items

For any item classified RED, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the
applicable law or market principle cited? Would a court in the governing jurisdiction
actually find a binding obligation, reliance damages exposure, or enforceability failure?
Is there a credible counter-argument the other party's counsel would make?

**Pass 2 — Completeness**: Have all relevant legal principles been considered? For
binding vs. non-binding analysis: have estoppel, part performance, and culpa in
contrahendo (where applicable) all been assessed? Are there deal mechanics (specific
performance, enhanced break-up fee, milestone obligations) that could convert this
risk from RED to YELLOW?

**Pass 3 — Challenge**: What is the strongest argument that this provision IS adequate?
Under what deal context would a sophisticated party accept this risk? Is the RED
classification proportionate, or is this YELLOW with appropriate mitigations?

Result: Mark as `self_interrogation: PASS` or `self_interrogation: REVISED`

### Confidence Scoring

| Level        | Range     | Meaning                                                      | Action                                                |
| ------------ | --------- | ------------------------------------------------------------ | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law; clear statute; well-established market standard | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong authority; minor interpretation questions             | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments but reasonable minds could differ             | State with explicit reasoning and contra-indicators   |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing authorities                   | Flag for counsel review with both sides stated        |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                                      | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

Given the deal-consequential nature of LOI analysis, err toward flagging uncertainty
rather than hiding it. An AMBIGUOUS binding classification presented as NON-BINDING
can cause a party to rely on the LOI as a framework without recognizing the binding
risk — the precise scenario that produced the $11.1 billion Texaco v. Pennzoil verdict.

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-letter-of-intent-review"
  document: "[LOI / Term Sheet / MOU / Heads of Terms title and date]"
  document_type: "[LOI / MOU / Term Sheet / Heads of Terms / Agreement in Principle]"
  user_side: "[Buyer / Seller / Seller's shareholders / Financial advisor / Board]"
  transaction_type: "[M&A-private / M&A-public / PE acquisition / JV / Real estate / Other]"
  deal_size: "[USD/GBP/EUR amount or 'Not disclosed']"
  governing_law: "[Jurisdiction identified from document or 'Not specified']"
  dispute_resolution: "[Courts (jurisdiction) / Arbitration (rules, seat) / Not specified]"
  playbook_used: "[Transaction playbook name or 'General market standards']"

  # BINDING POSTURE
  binding_classification: "[FULLY BINDING / PARTIALLY BINDING / NOMINALLY NON-BINDING / AMBIGUOUSLY NON-BINDING / UNINTENTIONALLY BINDING]"
  unintentional_binding_risk_score: "[0-10 — see A-3 scoring matrix]"

  # LOI MECHANICS
  exclusivity_period: "[duration / 'absent']"
  break_up_fee: "[amount or % / 'absent']"
  reverse_break_up_fee: "[amount or % / 'absent']"
  confidentiality_coverage: "[Standalone NDA / LOI integrated / Both / Neither]"
  conditions_specified: "[Specific / General / Not specified]"
  governing_law_present: "[Yes / No]"

  # RESEARCH
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to temp file or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED (legalcode-mcp) or UNVERIFIED [VERIFY]]"
  case_law_consulted:
    - "[Case — VERIFIED (legalcode-mcp) or UNVERIFIED [VERIFY]]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"

  # QUALITY
  clauses_reviewed: "[number]"
  red_findings: "[number]"
  yellow_findings: "[number]"
  green_findings: "[number]"
  critical_gaps: "[number of must-add missing provisions]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats — e.g., governing law not specified; assumed Delaware]"
  reviewer: "AI-assisted — requires qualified legal review before reliance"
```

---

## Anti-Patterns

What NOT to do when reviewing letters of intent and term sheets:

1. **Treating the non-binding label as the end of the analysis** — The most common
   LOI mistake is assuming "this letter is non-binding" insulates the parties from
   obligation. Conduct, reliance, and pre-contractual liability doctrine can bind parties
   to a nominally non-binding document. Always assess the Texaco v. Pennzoil four-factor
   test and the unintentional binding risk score.

2. **Reviewing only the explicit provisions** — LOIs create implicit obligations by
   what they do not say. A no-shop clause without a fiduciary out implicitly restricts
   a board's judgment. A condition precedent that says "satisfactory DD" implicitly
   creates a buyer walk-right with no seller protection. The gaps are as important as
   the text.

3. **Applying purchase agreement market standards to LOI provisions** — LOI provisions
   are intentionally less precise than purchase agreement provisions. Do not red-flag
   an LOI for lacking a materiality scrape or a representation qualifier — those are
   SPA concepts. Calibrate expectations to the document stage.

4. **Missing the binding scope mismatch** — The most dangerous LOI drafting error is
   a document that says "non-binding in its entirety" in the preamble but then uses
   binding obligation language in substantive provisions ("Seller agrees to...").
   Courts read the specific provision, not the general disclaimer.

5. **Ignoring governing law when assessing non-binding language** — A "non-binding" LOI
   under English law (where there is no general duty to negotiate in good faith) is very
   different from a "non-binding" LOI under German law (where culpa in contrahendo may
   impose pre-contractual liability regardless of the disclaimer). Always identify
   governing law before assessing enforceability.

6. **Overlooking the exclusivity trap** — Sellers lose most of their negotiating power
   when they sign exclusivity. An LOI with a 90-day no-talk and no fiduciary out, no
   milestone obligations on the buyer, and no drop-dead date can leave a seller locked
   out of the market for months while the buyer conducts unlimited diligence.

7. **Approving vague conditions precedent** — "Subject to completion of satisfactory
   due diligence" in the buyer's sole discretion is not a condition — it is a free
   walk-away option. Insist on a qualifier ("reasonable and good-faith determination"
   or "material adverse finding") that limits the buyer's ability to invoke the condition
   opportunistically.

8. **Failing to check the MAC definition against post-COVID standards** — An LOI from
   before 2020 or one drafted using pre-COVID market standards may lack critical
   exceptions (pandemics, market-wide disruptions, government actions) that are now
   expected. A broad MAC clause without these exceptions gives the buyer excessive
   walk-away rights.

9. **Treating break-up fees as only a seller protection** — A well-structured reverse
   break-up fee (payable by buyer) actually benefits the deal by giving the seller
   confidence that the buyer is committed. A buyer who accepts a reverse break-up fee
   is signaling deal seriousness. The absence of a reverse break-up fee in large deals
   should be flagged as a seller-protection gap.

10. **Reviewing LOI confidentiality in isolation from the standalone NDA** — The LOI
    may incorporate a standalone NDA by reference. If it does, check for inconsistencies
    between the LOI confidentiality provisions and the NDA. If the LOI confidentiality is
    narrower, information shared pursuant to the LOI may fall through the gap.

11. **Accepting open-ended expense reimbursement obligations** — An LOI that requires
    the seller to reimburse buyer's "all costs and expenses" if the seller terminates
    creates potentially uncapped liability. Buyer M&A costs (legal fees, financial
    advisory, financing costs) can exceed $10M on a $200M deal. Always seek a cap or
    limit reimbursement to documented direct costs.

12. **Skipping the post-LOI conduct analysis** — The LOI review must consider how the
    parties have acted since signing the LOI. If both parties have behaved as if the
    transaction is committed (seller has told customers, buyer has announced the deal
    publicly, DD is substantially complete), the binding risk has escalated beyond what
    the document language alone suggests.

13. **Ignoring Takeover Panel rules for UK public company targets** — The City Code on
    Takeovers and Mergers imposes strict limits on inducement fees (1% maximum) and
    requires Panel consent for certain fee structures. Applying US private M&A break-up
    fee conventions to a UK public target without checking Takeover Panel rules is a
    serious error.

14. **Assuming the LOI will be superseded by the SPA without issue** — Where the LOI
    and SPA are inconsistent (e.g., LOI says "full reps and warranties" but SPA limits
    reps to a knowledge standard), the LOI terms can create argument that the SPA
    departs from the agreed framework. Ensure the LOI is either superseded expressly
    ("this letter of intent is superseded in its entirety by the definitive agreement")
    or that its terms are non-binding in a way that cannot be enforced against the
    definitive agreement.

15. **Not identifying the document as the appropriate type** — An "agreement in principle"
    carries higher enforceability risk than an "indicative offer letter" or a "letter of
    interest." Before completing the review, confirm the document's characterization and
    apply the appropriate standard.

16. **Leaving fiduciary flexibility ambiguous for a corporate seller** — Directors of a
    company being sold have fiduciary duties to maximize shareholder value. An LOI that
    completely locks the board out of responding to superior proposals — without legal
    review of whether this is permissible under applicable corporate law — creates
    potential board liability risk.

17. **Missing the milestone obligations gap** — Exclusivity without buyer milestones
    is a one-sided covenant. The buyer gets 90 days of exclusive access but faces no
    obligation to move the deal forward. Include milestone obligations: SPA draft by
    Day 30; financing commitment by Day 45; regulatory filings by Day 60.

18. **Single-pass analysis** — Read the entire LOI before analyzing. The binding intent
    stated in the preamble may be contradicted by obligation language in later sections.
    An inconsistency between preamble and operative provisions is more dangerous than
    either alone.

19. **Overlooking the interaction between the LOI and the definitive agreement** — The
    LOI creates a framework expectation. If the SPA materially departs from the LOI
    framework (e.g., LOI contemplates a stock purchase but SPA is structured as an asset
    purchase), one party may argue this is a breach of the obligation to negotiate in
    good faith toward the LOI framework.

20. **Presenting certainty on inherently uncertain enforceability questions** — LOI
    enforceability is one of the most fact-specific areas of commercial law. "This LOI
    is non-binding" is a legal conclusion, not a statement of fact. Present findings
    with appropriate confidence levels; never state definitively that the LOI is
    non-binding without appropriate qualification and recommendation to seek legal advice.

---

## Writing Standards

### For redline rationales (suitable for counterparty's counsel):

- Plain language. No jargon or filler.
- Active voice: "This clause removes seller's fiduciary flexibility" (not "Fiduciary
  flexibility is removed by this clause")
- Short sentences. One point per sentence.
- Name the actor: "Buyer may walk away without consequence" (not "There is an ability
  to terminate without consequence")
- Specific, not vague: cite the specific provision being redlined

### For internal analysis:

- Same plain-language standards
- May include technical legal analysis with confidence qualifiers
- Jurisdiction-specific analysis marked [JURISDICTION-SPECIFIC]
- Unverified citations marked [VERIFY]
- Glass Box audit trail appended to output

### Quality gates before delivery:

1. Can a non-lawyer business executive understand the executive summary?
2. Can counterparty's counsel understand and respond to each redline?
3. Is every legal claim backed by a citation (or flagged [VERIFY])?
4. Are any phrases vague or hedging without reason? If yes, fix or qualify.
5. Is the binding vs. non-binding analysis of each provision explicit and defensible?
6. Are all jurisdiction-specific conclusions clearly scoped to the identified governing law?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 5, search for current case law on LOI enforceability in the governing law jurisdiction
- Verify Takeover Panel rules, HSR filing thresholds, and EU merger control thresholds
- Search for recent Delaware Court of Chancery decisions on LOI enforceability, fiduciary
  duties in sale processes, and MAC/MAE definitions
- Search for current ABA or SRS Acquiom deal data on break-up fee benchmarks
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with research-based analysis only
- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Focus on structural and process analysis (binding scope mapping, gap analysis,
  provision classification) rather than jurisdiction-specific legal opinion

---

## Localization Notes

When localizing for a specific jurisdiction, adapt the following sections:

### US Jurisdictions:

- Replace general enforceability analysis with the Teachers Insurance two-type framework
  (Type I fully binding; Type II binding to negotiate)
- Apply Revlon doctrine for public company seller fiduciary out analysis
- Confirm HSR Act applicability and filing thresholds for the deal size [VERIFY]
- Apply DTSA protection period for trade secrets in confidentiality analysis [VERIFY]
- State-specific non-compete enforceability for any non-solicitation provision [VERIFY]

### UK / English Law:

- Replace general enforceability discussion with Walford v. Miles analysis (no general
  duty to negotiate in good faith)
- Apply Takeover Panel rules (Rule 21.2) to break-up fee / inducement fee analysis
  for listed target companies
- Check Companies Act 2006 board duties and recommended offer procedure
- Consider stamp duty (0.5%) and SDLT on real property in deal structure analysis

### EU / Civil Law Jurisdictions:

- Apply culpa in contrahendo doctrine: assess whether breaking off negotiations creates
  pre-contractual liability even where LOI says "non-binding"
- Review local merger control thresholds and FDI screening requirements
- For German law: BGB § 311(2) pre-contractual obligations apply from the moment
  parties enter into negotiations [VERIFY]
- For French law: Code Civil Article 1112-1 requires good faith in negotiations [VERIFY]

---

## Output Format Template

```markdown
## Letter of Intent Review Summary

**Document**: [LOI / Term Sheet / MOU title and date]
**Document Type**: [LOI / Term Sheet / Heads of Terms / etc.]
**Parties**: [Buyer name and Seller name]
**Your Side**: [Buyer / Seller / Advisor]
**Governing Law**: [Jurisdiction]
**Transaction Type**: [M&A-private / PE / JV / etc.]
**Deal Size**: [Amount or 'Not disclosed']
**Review Basis**: [Transaction playbook or General market standards]
**Date of Review**: [date]

---

## Binding Posture Assessment

**Overall Classification**: [FULLY BINDING / PARTIALLY BINDING / NOMINALLY NON-BINDING /
AMBIGUOUSLY NON-BINDING / UNINTENTIONALLY BINDING]

**Unintentional Binding Risk Score**: [X/10] — [LOW / MEDIUM / HIGH]

**Summary**: [2-3 sentence summary of the binding posture finding]

**Binding Scope Map**:

| LOI Section | Provision   | Intended Status | Risk Classification                 |
| ----------- | ----------- | --------------- | ----------------------------------- |
| [Section]   | [Provision] | [Non-binding]   | [BINDING / AMBIGUOUS / NON-BINDING] |

---

## Critical Findings

[Top 3-5 issues with RED classification — most important for immediate attention]

---

## LOI Mechanics Assessment

| Mechanic | LOI Provision | Market Standard | Assessment |
| -------- | ------------- | --------------- | ---------- |

[Table from Step 6]

---

## Gap Analysis

### Must Add Before Signing:

- [List of critical missing provisions]

### Should Add Before Signing:

- [List of important missing provisions]

### Optional Additions:

- [List of nice-to-have additions]

---

## Clause-by-Clause Analysis

### [A-1] Document Characterization — [GREEN / YELLOW / RED] | Confidence: [X.XX]

**Document says**: [Summary of binding intent language]
**Market standard**: [Clear, specific delineation of binding vs. non-binding provisions]
**Assessment**: [Analysis]
**Redline** (if YELLOW or RED):

> [Specific proposed language]
> **Fallback**: [Minimum acceptable alternative]
> **Priority**: [Tier 1 / 2 / 3]

[Continue for all 12 categories]

---

## Negotiation Strategy

**Tier 1 (Must-Haves — resolve before signing)**: [list]
**Tier 2 (Strong Preferences — material negotiation points)**: [list]
**Tier 3 (Nice-to-Haves — concession candidates)**: [list]
**Recommended approach**: [2-3 sentences on sequencing and strategic framing]

---

## Recommended Next Steps

1. [Specific action with owner and timing]
2. [Follow-up items — e.g., "Obtain counsel opinion on culpa in contrahendo exposure"]

---

## Glass Box Audit Trail

[YAML block from Glass Box section above]
```

---

## Provenance

Created by Legalcode (2026-03-01). Legalcode original synthesis from 2-agent research
pipeline. Legal research draws on US case law (Texaco v. Pennzoil [1987], Teachers
Insurance & Annuity Ass'n v. Tribune Co. [2d Cir. 1987], SIGA Technologies v. PharmAthene
[Del. 2015], Akorn v. Fresenius Kabi [Del. Ch. 2018]), UK case law (Walford v. Miles
[1992]), civil law pre-contractual liability frameworks (BGB § 311(2), Code Civil
Article 1112-1), UK Takeover Code Rule 21.2, ABA and SRS Acquiom M&A market data
(2021–2024), and post-COVID MAC/MAE clause evolution research. Structural patterns,
quality frameworks (Citation Quality Gates, Self-Interrogation, Confidence Scoring,
Glass Box audit trail), and anti-patterns adapted from the `legalcode-purchase-agreement-review`
and `legalcode-contract-review` gold standard skills. Jurisdiction-agnostic with
[JURISDICTION-SPECIFIC] markers for US (Delaware / New York), UK (English law,
Takeover Panel), and EU (civil law pre-contractual liability).
