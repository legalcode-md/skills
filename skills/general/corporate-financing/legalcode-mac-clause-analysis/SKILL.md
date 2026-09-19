---
name: legalcode-mac-clause-analysis
description: Analyze and evaluate Material Adverse Change (MAC) / Material Adverse Effect (MAE) clauses
  in M&A transactions — merger agreements, stock purchase agreements, and asset purchase agreements. Use
  when reviewing or drafting MAC/MAE provisions in any M&A, LBO, or private investment agreement.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Analyze and evaluate Material Adverse Change (MAC) / Material Adverse Effect (MAE) clauses in M&A transactions — merger agreements, stock purchase agreements, and asset purchase agreements. Covers definition scope, carve-out taxonomy (general economic conditions, industry-wide conditions, law changes, GAAP changes, acts of war, pandemics/epidemics, deal announcement effects, stock price, failure to meet projections), the disproportionate impact exception, burden of proof allocation under Delaware and English law, bring-down mechanics, ordinary course covenant interaction, financing MAE distinction, and full case law analysis (Akorn v. Fresenius Kabi AG 2018, AB Stable VIII v. MAPS Hotels 2020-21, Hexion v. Huntsman 2008, IBP v. Tyson Foods 2001, Snow Phipps v. KKR 2021). Evaluates from both buyer and seller perspectives, scores each element BUYER-FAVORABLE / BALANCED / SELLER-FAVORABLE, generates redlines with fallback positions, and produces a confidence-scored, auditable analysis. Use when reviewing or drafting MAC/MAE provisions in any M&A, LBO, or private investment agreement.


# Legalcode MAC/MAE Clause Analysis

> **Disclaimer**: This skill provides a framework for AI-assisted analysis of Material
> Adverse Change/Effect clauses in M&A agreements. It does not constitute legal advice.
> All outputs should be reviewed by a qualified M&A attorney licensed in the relevant
> jurisdiction before relying on any analysis. Laws and Delaware court interpretations
> evolve; verify case law currency before relying on any holding cited here. Statutory and
> case law references carry hallucination risk — verify against authoritative sources.

## Purpose and Scope

This skill analyzes MAC/MAE clauses in M&A transactions. It is purpose-built for the
specialized, high-stakes nature of MAC analysis, which differs fundamentally from general
contract review: a MAC clause is often the single most consequential provision in an M&A
agreement, and invoking or resisting a MAC claim involves multi-million-dollar litigation risk.

**Covers:**

- Comprehensive clause-level analysis of all three MAC tiers: general MAE definition,
  carve-outs, and disproportionate impact exception
- Buyer and seller perspective scoring for every element
- Delaware case law framework (IBP, Hexion, Akorn, AB Stable, Snow Phipps)
- English law and Takeover Code MAC standards
- Bring-down condition mechanics and timing risk
- Ordinary course of business covenant interaction
- Financing MAE distinction and reverse termination fee interaction
- Redlines with primary and fallback positions for both buyer and seller
- Glass Box audit trail

**Does not:**

- Analyze the underlying facts needed to invoke or resist an actual MAC claim —
  that requires factual investigation beyond this skill's scope
- Provide legal advice or replace qualified M&A counsel
- Draft the full merger agreement or SPA — see `legalcode-merger-agreement-analysis`
  or `legalcode-purchase-agreement-review` for full-agreement review

**Use alongside:**

- `legalcode-merger-agreement-analysis` — full merger agreement clause analysis
- `legalcode-purchase-agreement-review` — full SPA/APA analysis
- `legalcode-ma-due-diligence-checklist` — DD workstreams that feed MAC risk assessment

---

## Jurisdiction and Governing Law

MAC/MAE analysis is highly jurisdiction-dependent. This skill primarily covers:

### Delaware (Default — Most M&A Transactions)

Delaware courts have developed the most extensive MAC jurisprudence worldwide. The
Delaware Court of Chancery has set the global standard for MAC analysis through a line of
cases from IBP v. Tyson (2001) through Akorn v. Fresenius (2018). Delaware law governs
most major US M&A transactions.

### English Law

The English standard is substantially higher than Delaware in public company takeovers
(governed by the Takeover Code) and somewhat higher in private M&A. English courts
interpret MAC narrowly and with significant deference to specific contractual language.

### Civil Law Jurisdictions [JURISDICTION-SPECIFIC]

Civil law jurisdictions (France, Germany, Netherlands, etc.) may address MAC concepts
through different doctrinal mechanisms — frustration of purpose (Wegfall der
Geschäftsgrundlage in Germany), force majeure, or material breach. MAC clauses in
cross-border deals governed by civil law require jurisdiction-specific legal analysis.

**[JURISDICTION-SPECIFIC]** When localizing, research and apply:

- The applicable courts' MAC jurisprudence
- Whether "materiality" has been judicially defined
- Specific performance availability and willingness
- Remedy for wrongful MAC invocation (damages, specific performance, both)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. The workflow pauses
and asks when:

- The answer changes the direction of the analysis (buyer vs. seller perspective)
- Scope decisions affect which carve-outs to scrutinize most closely
- Factual context (type of deal, industry, deal size) affects MAC risk calibration
- The governing law is ambiguous or unusual for the deal type

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

### Step 1: Accept the MAC Clause

Accept the MAC/MAE provision in any of these formats:

- **Full agreement**: The complete merger agreement, SPA, or APA — extract the MAC
  definition and all references to MAC as conditions, representations, or covenants
- **Clause extract**: The MAE definition section alone (often Section 1.1 or Article I)
- **Pasted text**: The MAC language pasted directly into the conversation
- **No clause**: User describes a deal and asks for drafting guidance

If no clause or agreement text is provided, ask the user to supply one before proceeding.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the analysis, ask the user these questions:

1. **Which side are you advising?**
   - Options: Buyer/Acquirer, Seller/Target, Lender (financing MAC), Neutral (drafting
     guidance only)
   - _Why this matters_: MAC analysis is inherently adversarial. Every element favors one
     party. The entire perspective of the analysis depends on which side you represent.

2. **Deal type?**
   - Options: Merger (forward or reverse triangular), Stock purchase, Asset purchase,
     LBO/leveraged buyout, Investment (minority stake), Other
   - _Why this matters_: MAC standards and carve-out conventions differ by deal type.
     LBO agreements (particularly pre-2008 vintage) often have narrower carve-outs.

3. **Governing law?**
   - Options: Delaware, Other US state (specify), English law, Other (specify)
   - _Why this matters_: Entirely different judicial frameworks apply.

4. **Deal size and industry?**
   - Free text. Examples: "$500M pharma acquisition," "$2B leveraged buyout of retail chain"
   - _Why this matters_: Industry context informs which carve-outs are most relevant
     (e.g., pharma deals need FDA/regulatory carve-outs; pandemic carve-outs became
     standard after COVID-19; financial services deals have regulatory approval issues).

5. **Is there a financing commitment letter?**
   - Options: Yes — Financing MAE analysis needed, No — skip financing MAC section
   - _Why this matters_: Committed financing packages often have a separate "Financing MAE"
     definition that may differ from the deal MAC.

If the user provides partial context, proceed with stated assumptions and flag them
explicitly at the start of the analysis.

### Step 3: Extract and Map the MAC Architecture

Before analyzing substance, map the MAC clause's three-tier architecture:

**Tier 1 — General MAE Definition**
Identify: what circumstances are included in the definition? What is the scope (business /
financial condition / results of operations / prospects)? Is the definition forward-looking
("would reasonably be expected to be materially adverse") or backward-looking only?

**Tier 2 — Carve-Outs**
Identify every carve-out. Check each against the standard taxonomy below. Flag any
non-standard carve-outs. Note whether carve-outs modify the definition with "unless caused
by" or "except to the extent resulting from" language.

**Tier 3 — Disproportionate Impact Exception (Carve-Back)**
Identify whether carve-outs include a disproportionate impact qualifier. Note which
carve-outs do and do not include the qualifier, and what the qualifier says.

**⟁ CLARIFY** — If any carve-out uses unusual or undefined language:

- Flag the specific language
- Ask whether the user wants the ambiguous language interpreted strictly or broadly
- Note that courts will typically construe MAC clauses under the applicable governing law
  (Delaware: narrow, strictly construed in favor of closing; English: construed per
  plain meaning of carefully negotiated text)

### Step 4: Gather Legal Authority

Use **legalcode-mcp** (if connected) to gather current legal authority. If not connected,
proceed using the Case Law Reference Framework below and mark all citations [VERIFY].

Search for:

- Current status of key Delaware MAC cases (Akorn, AB Stable, Hexion, IBP)
- Any post-2021 Delaware MAC decisions
- English law developments (Takeover Code Rule 13 Panel Statements, English court MAC cases)
- Any jurisdiction-specific MAC developments for the governing law identified in Step 2

### Step 5: Analyze the General MAE Definition (Tier 1)

Assess the general MAE definition against market standard and the client's interest.

| Element                      | Market Standard                                           | Analyze For                                                                          |
| ---------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Effect on what?**          | Business, financial condition, results of operations      | Whether "prospects" is included (buyer wants it; seller resists — too speculative)   |
| **Measurement basis**        | Company and subsidiaries, taken as a whole                | Whether subsidiaries can trigger MAC individually (buyer wants this; seller resists) |
| **Forward-looking language** | "Is, or would reasonably be expected to be"               | Whether purely forward-looking risk triggers MAC without actual occurrence           |
| **Duration element**         | Implicit (courts require years-long impact)               | Whether definition requires durationally significant impact or is undefined          |
| **Quantitative threshold**   | None stated (courts define "material")                    | Whether any numerical threshold is specified (rare but more certainty)               |
| **Knowledge qualifier**      | Rare (buyer should not be able to invoke disclosed risks) | Whether definition excludes events known to buyer at signing                         |

**Scoring Key for All Elements:**

- **BUYER-FAVORABLE**: Definition broadly written to give buyer maximum walkaway options
- **BALANCED**: Within the range of market practice; neither side disproportionately burdened
- **SELLER-FAVORABLE**: Definition narrowly written to maximize seller's ability to force closing

**⟁ CLARIFY** — On "prospects":
"The MAE definition [includes / excludes] 'prospects.' Including prospects is buyer-favorable
because it allows invocation based on future expectations — but Delaware courts have been
skeptical of MAC claims based on prospects alone (Hexion v. Huntsman). Do you want me to
flag this as BUYER-FAVORABLE (if included) or SELLER-FAVORABLE (if excluded), or treat
it as market-dependent?"

### Step 6: Analyze the Carve-Out Taxonomy (Tier 2)

Review each carve-out against the standard taxonomy. For each carve-out:

1. Classify it (which standard category does it fit?)
2. Score it (BUYER-FAVORABLE / BALANCED / SELLER-FAVORABLE)
3. Flag gaps (standard carve-outs missing; unusual carve-outs present)
4. Note drafting precision (vague carve-outs create interpretation risk for both sides)

#### Standard Carve-Out Taxonomy

| #    | Carve-Out Category                                                               | Market Standard?   | Buyer Impact                            | Seller Impact                                                   |
| ---- | -------------------------------------------------------------------------------- | ------------------ | --------------------------------------- | --------------------------------------------------------------- |
| C-1  | **General economic / financial market conditions**                               | ✅ Yes             | Neutral — general macro risk shared     | Protected from broad recession                                  |
| C-2  | **Industry-wide / sector conditions**                                            | ✅ Yes             | Neutral — industry risk shared          | Protected from sector downturn                                  |
| C-3  | **Changes in applicable law or regulation**                                      | ✅ Yes             | Neutral — regulatory change risk shared | Protected from regulatory shifts                                |
| C-4  | **Changes in GAAP or accounting standards**                                      | ✅ Yes             | Neutral                                 | Protected from accounting rule changes                          |
| C-5  | **Acts of God / natural disasters / pandemics / epidemics**                      | ✅ Yes (post-2020) | Risk-transferring to seller's detriment | Protected from COVID-type events                                |
| C-6  | **Acts of war / terrorism / national calamity**                                  | ✅ Yes             | Neutral — systemic risk shared          | Protected from geopolitical events                              |
| C-7  | **Actions taken at buyer's request / with buyer's consent**                      | ✅ Yes             | Prevents buyer from inducing MAC        | Protects seller from buyer-directed changes                     |
| C-8  | **Deal announcement effects** (employee attrition, customer/supplier disruption) | ✅ Yes             | Important — forces deal accountability  | Protected from self-fulfilling MAC claims                       |
| C-9  | **Stock price / credit rating changes (in isolation)**                           | ✅ Yes             | Anti-circularity protection             | Prevents cosmetic stock movements from triggering MAC           |
| C-10 | **Failure to meet projections / analyst estimates (in isolation)**               | ✅ Yes             | Anti-circularity protection             | Prevents shortfall from triggering MAC without underlying cause |
| C-11 | **Pandemic / epidemic (explicit)**                                               | ✅ Yes (post-2020) | Limits buyer's COVID-type walkaway      | Strong seller protection; key post-AB Stable lesson             |
| C-12 | **Regulatory approval process delays**                                           | Sometimes          | Deal-specific                           | Protects against merger control delays                          |

**Analyzing for gaps:**

- **Missing C-8** (deal announcement effects): Seller lacks protection from self-fulfilling MAC
  triggered by deal uncertainty. RED issue for sellers.
- **Missing C-11** (pandemic carve-out): Post-COVID, absence is a significant seller vulnerability.
  YELLOW for sellers in most industries; RED in healthcare/hospitality/travel.
- **Narrow C-3** (changes in law): If carve-out is limited to "changes in laws of general
  applicability" but not regulatory interpretations, seller may be exposed to FDA/SEC/other
  agency guidance changes. Industry-dependent issue.
- **Absent anti-circularity** for C-9/C-10: Without anti-circularity language ("excluding
  the underlying causes of such changes"), stock price decline or missed projections can be
  used as evidence of a MAC even though they are excluded.

**[JURISDICTION-SPECIFIC]** For English law deals in regulated industries (financial
services, healthcare, utilities): Regulatory change carve-outs should specifically address
FCA, PRA, CMA, or sector-specific regulator actions. The Takeover Code further restricts
MAC invocation in public company bids (see Localization Notes).

### Step 7: Analyze the Disproportionate Impact Exception (Tier 3)

The disproportionate impact exception (carve-back) is structurally the most contested
element of MAC drafting. It operates as follows:

```
GENERAL RULE:     Carve-out APPLIES → Company protected from general conditions
EXCEPTION:        Unless the Company is disproportionately adversely affected relative
                  to comparable companies in the same industry / sector
EFFECT:           Disproportionate macro/industry impact flows back through to be a MAC
```

**Burden Allocation in Delaware:**

1. **Buyer** bears the initial burden of proving a MAC occurred
2. **Seller** bears the burden of proving a carved-out event caused the adverse effect
3. **Buyer** bears the burden of proving the disproportionate impact exception applies

**Analyze for:**

| Element                     | Buyer Wants                                      | Seller Wants                                                                        |
| --------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------- |
| **Scope of qualifier**      | Exception applies to ALL carve-outs              | Exception applies to few or no carve-outs                                           |
| **Comparator group**        | "Comparable companies" broadly defined           | "Competitors in the same subsector" narrowly defined                                |
| **Degree of disproportion** | Any disproportionate impact sufficient           | "Materially and disproportionately" higher bar                                      |
| **Measurement period**      | Short period (more likely to show disproportion) | Long period (regression to mean reduces apparent disproportion)                     |
| **Express exclusion**       | No                                               | Seller wants some carve-outs (e.g., C-7, C-8) expressly excluded from the exception |

**Key drafting issue:** When the disproportionate impact exception is present in SOME but
not ALL carve-outs, map which carve-outs include it. Asymmetric inclusion creates
unintended risk allocation.

**⟁ CLARIFY** — If the disproportionate impact exception is absent entirely:
"The MAC definition has no disproportionate impact exception. This is seller-favorable —
general economic downturns are fully carved out even if the target is catastrophically
impacted. Should I flag this as [SELLER-FAVORABLE] or as a [BUYER-FAVORABLE gap] to push
for in negotiations?"

### Step 8: Apply the Bring-Down Condition Framework

MAC clauses appear in two separate locations in M&A agreements. Analyze both:

**Use 1 — In Representations and Warranties:**
The seller typically represents that "since the Balance Sheet Date, there has been no MAE."
This representation is then **brought down** at closing — i.e., the buyer must receive a
certificate at closing that the rep is still true.

**Use 2 — As Standalone Closing Condition:**
Many agreements include a standalone closing condition that "no MAE shall have occurred
and be continuing" since signing (or since balance sheet date). This is separate from
the bring-down of representations.

**Analyze:**

- Does the agreement contain both uses, or only one? Missing the standalone closing
  condition leaves the buyer dependent on the rep bring-down path.
- What is the bring-down standard for the MAC rep? Is it:
  - **"True and correct in all material respects"** — standard language
  - **"No material adverse effect has occurred"** — tautological, may cause interpretation problems
  - **"True and correct except to the extent that any failure to be true would not have
    a Material Adverse Effect"** — double materiality scrape risk
- What is the closing condition standard? "Since the date of this Agreement" or "since
  the Applicable Date"?

**Timing risk analysis:**

- Between signing and closing (the "interim period"), macro events can evolve
- The longer the expected closing timeline, the more valuable MAC carve-outs become
- For deals requiring regulatory approvals (antitrust, CFIUS, sector regulators), the
  interim period may be 12-18 months — pandemic-type carve-outs become critical

### Step 9: Analyze Ordinary Course Covenant Interaction

**The AB Stable lesson**: Even when MAC carve-outs protect the seller from a MAC finding,
the seller can still lose the deal if it breached the ordinary course of business ("OCB")
covenant during the interim period.

In AB Stable VIII v. MAPS Hotels (Del. Ch. 2020, Del. 2021), the seller:

- Was protected by the pandemic carve-out (COVID-19 was a carved-out event)
- BUT: To respond to COVID, seller shut down hotels, furloughed employees, suspended
  operations — all deviations from ordinary course
- Delaware Court of Chancery: seller breached the OCB covenant; buyer entitled to refuse
  to close
- Delaware Supreme Court affirmed (2021)

**Analyze the OCB covenant against the MAC clause:**

| Question                                                                                       | Why It Matters                                                                          |
| ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Does the OCB covenant include a "consistent with past practice" qualifier?                     | Tighter standard — deviation during crisis may trigger breach                           |
| Does the OCB covenant have explicit carve-outs for pandemic/force majeure responses?           | Post-AB Stable, sellers should insist on this                                           |
| Does the OCB covenant allow seller to take reasonable actions in response to MAC events?       | Protects seller's crisis management flexibility                                         |
| Is buyer consent required for extraordinary actions (furloughs, shutdowns, facility closures)? | Seller may need to act fast in a crisis — consent requirement creates practical problem |
| What is the standard for buyer consent? "Not to be unreasonably withheld"?                     | Critical for seller's practical ability to manage through the interim period            |

**Flag if absent:** If the OCB covenant does not expressly permit reasonable responses to
pandemic, force majeure, or emergency events, flag as SELLER RISK — OCB BREACH RISK.

### Step 10: Quality Verification and Deliver Output

Before delivering the analysis:

1. Run the 5 Citation Quality Gates silently. Revise failures before delivery.
2. For every RED-classified finding, run the 3-pass Self-Interrogation.
3. Assign a Confidence Score to each material finding.
4. Verify that all three MAC tiers have been analyzed.
5. Verify that the OCB covenant interaction has been addressed.
6. Generate the Glass Box Audit Trail and append to the output.

---

## Case Law Reference Framework

Use this framework when analyzing MAC provisions. Cite these cases where relevant; mark
all citations as [VERIFY] if legalcode-mcp is not available to confirm currency.

### Delaware Cases

#### IBP, Inc. v. Tyson Foods, Inc. (Del. Ch. 2001) [VERIFY]

**Key holdings:**

- Established the foundational Delaware MAC standard
- "A short-term hiccup in earnings should not suffice; rather the MAE should be material
  when viewed from the longer-term perspective of a reasonable acquirer"
- Buyer bears the burden of proving MAC
- Court refused to find MAC based on one-quarter earnings decline
- Vice Chancellor Strine: MAC requires "substantial threat to the overall earnings
  potential of the target in a durationally significant manner"
- Specific performance ordered; Tyson required to close

**Use in analysis:** The baseline case establishing buyer's burden and the durational
requirement. Cite when MAC definition lacks express durational element, or when buyer
is asserting MAC based on short-term performance decline.

#### Hexion Specialty Chemicals v. Huntsman Corp. (Del. Ch. 2008) [VERIFY]

**Key holdings:**

- Buyer failed to establish a MAC based on Huntsman's deteriorating earnings
- Reinforced the high bar: adverse change must be "durationally significant" and
  "consequential to the company's long-term earnings power over a commercially reasonable
  period, which one would expect to be measured in years rather than months"
- A seller whose performance has declined but is recovering is unlikely to have suffered a MAC
- Buyer's own financing failure (not Huntsman's performance) contributed to the impasse

**Use in analysis:** Cite when buyer is asserting MAC based on earnings deterioration
without longitudinal evidence of structural decline. Reinforces that short-term downturns
are insufficient.

#### Akorn, Inc. v. Fresenius Kabi AG (Del. Ch. 2018) [VERIFY]

**Key holdings:**

- First Delaware case finding that a MAC had occurred
- Target's FDA compliance failures were systemic, pervasive, and not short-term
- Akorn's financial results had declined ~86% year-over-year on key metrics (EBITDA margin,
  revenues) with no recovery in sight
- The compliance failures were undisclosed at signing and constituted fraudulent
  misrepresentation in the representations
- Court applied the durational test: these were not one-quarter blips but fundamental
  deteriorations affecting long-term earnings power
- Fresenius validly terminated; no specific performance for seller

**Use in analysis:** Cite when MAC claim involves regulatory compliance failures, pervasive
undisclosed problems, or catastrophic decline across multiple business dimensions. Also
cite for the intersection of MAC with representation accuracy (seller's fraud/inaccuracy
removes the ordinary durational protection).

**Critical limitation:** Akorn was exceptional — the standard remains very high. Do not
cite Akorn as support for ordinary-course MAC claims.

#### AB Stable VIII LLC v. MAPS Hotels and Resorts One LLC (Del. Ch. 2020; Del. 2021) [VERIFY]

**Key holdings:**

- COVID-19 pandemic did NOT constitute a MAC: pandemic was expressly carved out
- BUT: Seller's operational responses to COVID (hotel closures, furloughs) breached the
  OCB covenant
- Delaware Supreme Court affirmed: carve-outs protect from MAC findings but do not
  authorize deviation from the OCB covenant
- Buyer entitled to refuse to close based on OCB covenant breach, not MAC

**Use in analysis:** Cite in every MAC analysis that includes a pandemic carve-out. The
lesson is that carve-outs are necessary but not sufficient — the OCB covenant is an
independent obligation. Also cite when seller is defending against MAC claim but faces
OCB covenant exposure.

#### Snow Phipps Group LLC v. KKR & Co. (Del. Ch. 2021) [VERIFY]

**Key holdings:**

- Fitness equipment company (Pty Ltd/specialty retail context)
- Court refused to find a MAC despite COVID-19 severely impacting the business
- Pandemic carved out; buyer could not establish disproportionate impact exception
- Reaffirmed: MAC standard is exceptionally high; courts resist finding a MAC absent
  extraordinary, longitudinal deterioration

**Use in analysis:** Cite alongside AB Stable to establish that COVID-19 alone, even in
severely impacted industries, will not constitute a MAC where standard carve-outs are
present.

#### Channel Medsystems, Inc. v. Boston Scientific Corp. (Del. Ch. 2019) [VERIFY]

**Key holdings:**

- Employee criminal fraud discovered post-signing (undisclosed)
- Court found that undisclosed employee fraud constituted a MAC
- Fraud/criminal conduct that is undisclosed and systemic can satisfy the MAC threshold
- Overlaps with representation accuracy analysis (similar to Akorn)

**Use in analysis:** Cite when MAC analysis involves undisclosed fraud, criminal conduct,
or serious compliance failures discovered after signing.

---

### English Law MAC Standards

#### Takeover Code — Rule 13 (Public Company Takeovers) [VERIFY]

The UK Takeover Code sets an exceptionally high bar for invoking a MAC as a condition in
public company offers:

- MAC must be "of material significance to the offeror in the context of the offer"
- The Takeover Panel interprets MAC conditions narrowly; buyers must satisfy the Panel
  that invoking MAC is appropriate before lapsing an offer
- In practice, the Panel requires conditions to be "entirely exceptional in nature and
  would not have been in the reasonable contemplation of the offeror when the offer was made"
- The Code prohibits subjective MAC conditions (must be objectively determinable)
- Public takeover MAC conditions are rarely invoked successfully

**Use in analysis:** Essential for UK public company takeovers. Significantly different
from Delaware private M&A MAC standards.

#### English Law Private M&A MAC Standard

English courts interpret MAC clauses per their plain meaning as carefully negotiated
commercial provisions. The general standard:

- English courts require "a very considerable significance striking at the heart of the
  purpose of the transaction"
- English courts give more weight to the specific contractual language than Delaware
  courts, which apply a broader common-law gloss
- No equivalent of the IBP/Hexion durational framework — the analysis is more textual
- Specific performance is available but courts have discretion; not as buyer-friendly
  as Delaware in forcing a close

**[JURISDICTION-SPECIFIC]** For English law deals, the specific contractual language
carries more weight than in Delaware. Drafting precision matters even more.

---

## Buyer vs. Seller Perspective Matrix

Use this matrix to score each MAC element and to structure redlines. Every element of
the MAC clause is either BUYER-FAVORABLE, BALANCED, or SELLER-FAVORABLE.

### General MAE Definition

| Element                                                         | BUYER-FAVORABLE | BALANCED     | SELLER-FAVORABLE |
| --------------------------------------------------------------- | --------------- | ------------ | ---------------- |
| Includes "prospects"                                            | ✅              |              |                  |
| Includes subsidiaries individually (not just consolidated)      | ✅              |              |                  |
| Forward-looking ("would reasonably be expected")                |                 | ✅           |                  |
| Backward-looking only                                           |                 |              | ✅               |
| Excludes "prospects"                                            |                 |              | ✅               |
| Consolidated measurement only                                   |                 |              | ✅               |
| Quantitative threshold (e.g., >10% revenue decline)             |                 | Depends on % |                  |
| Knowledge qualifier (excludes events known to buyer at signing) |                 |              | ✅               |

### Carve-Out Analysis

| Element                                                    | BUYER-FAVORABLE       | BALANCED | SELLER-FAVORABLE |
| ---------------------------------------------------------- | --------------------- | -------- | ---------------- |
| Narrow carve-out language (limited scope)                  | ✅                    |          |                  |
| Broad carve-out language (expansive scope)                 |                       |          | ✅               |
| No pandemic/epidemic carve-out                             | ✅                    |          |                  |
| Pandemic/epidemic carve-out present                        |                       |          | ✅               |
| Disproportionate impact exception on all carve-outs        | ✅                    |          |                  |
| No disproportionate impact exception                       |                       |          | ✅               |
| Anti-circularity on projections/stock price                |                       | ✅       |                  |
| No anti-circularity (projections excluded as symptom only) | ✅                    |          |                  |
| Deal announcement carve-out absent                         | ✅ (seller locked in) |          |                  |
| Deal announcement carve-out present                        |                       | ✅       |                  |

### Disproportionate Impact Exception

| Element                                                       | BUYER-FAVORABLE | BALANCED | SELLER-FAVORABLE |
| ------------------------------------------------------------- | --------------- | -------- | ---------------- |
| Exception applies to all carve-outs                           | ✅              |          |                  |
| Exception applies to economic/industry carve-outs only        |                 | ✅       |                  |
| Exception applies to selected carve-outs                      |                 | Depends  |                  |
| No exception (carve-outs fully protect seller)                |                 |          | ✅               |
| Low threshold ("disproportionately affected")                 | ✅              |          |                  |
| High threshold ("materially and disproportionately affected") |                 |          | ✅               |

---

## Financing MAE Distinction

Where the deal involves committed third-party financing (bank debt, bridge loans), the
commitment letter will typically contain a separate "Financing MAE" or "Lender MAE"
definition that may differ from the deal MAC.

**Analyze the following:**

1. **Relationship between deal MAC and Financing MAC**: If the Financing MAC is narrower
   than the deal MAC, lenders may refuse to fund even where the deal MAC has not been
   triggered. This creates a gap that exposes buyers to specific performance claims.

2. **Reverse Termination Fee (RTF) link**: Many agreements tie the RTF to the buyer's
   inability to obtain financing. If the Financing MAC is triggered but the deal MAC is
   not, the buyer's RTF may be its sole remedy — seller cannot compel closing.

3. **Sycamore v. L Brands / similar disputes**: Post-COVID litigation showed that RTF
   provisions linked to "failure to obtain financing" vs. "financing MAC" create litigation
   over which trigger applies. Verify the exact language of the RTF and its conditions.

4. **Buyer's obligation to use reasonable best efforts to obtain financing**: Even if
   a Financing MAC is triggered, buyer may still be obligated to seek alternative
   financing before invoking the RTF path.

---

## Severity Classification

### RED — Significant MAC Risk / Material Drafting Issue

A MAC provision element that materially disadvantages the representing party, creates
substantial litigation risk, or departs significantly from market practice in a way that
could affect deal certainty.

**RED examples (Seller-side):**

- No pandemic/epidemic carve-out (post-2020, market standard; absence is RED)
- No deal announcement carve-out (exposes seller to self-fulfilling MAC)
- No anti-circularity language (missed projections can be used as MAC evidence)
- OCB covenant has no force majeure / crisis management carve-out (AB Stable risk)
- MAC definition includes "prospects" with no qualification (too speculative, creates
  litigation risk for both parties)
- Disproportionate impact exception absent entirely (seller bears all macro risk)

**RED examples (Buyer-side):**

- No disproportionate impact exception in any carve-out (buyer bears all macro risk even
  if company uniquely devastated)
- MAC definition excludes subsidiaries unless parent is affected (buyer loses walkaway
  right for subsidiary-level collapse)
- Bring-down standard uses double materiality scrape (all rep accuracy measured through
  "material adverse effect" standard — buyer's closing rights severely eroded)
- No standalone MAC closing condition; buyer's only protection is rep bring-down
- Financing MAC broader than deal MAC (financing becomes unavailable before deal MAC
  is triggered — leaves buyer exposed to specific performance)

### YELLOW — Negotiate

Below market standard but within negotiable range. Requires attention; may be
acceptable depending on deal context and risk appetite.

**YELLOW examples:**

- Disproportionate impact exception absent from pandemic/acts of war carve-outs but
  present in economic/industry carve-outs
- OCB covenant has consent requirement without "not to be unreasonably withheld" qualifier
- MAC definition scope is unusually narrow (only "business" — not financial condition,
  results of operations)
- Projections carve-out absent — underlying cause still excluded, but anti-circularity
  language is weaker than market standard
- Forward-looking MAE language ("would reasonably be expected") absent — buyer limited
  to backward-looking triggering events

### BALANCED — Market Standard

Elements within the range of standard market practice; neither side disproportionately
burdened.

**BALANCED examples:**

- Standard economic/industry/law/GAAP carve-outs present
- Deal announcement carve-out present (standard)
- Anti-circularity on stock price and projections present (standard)
- OCB covenant with "consistent with past practice" qualifier
- Forward-looking ("would reasonably be expected to be") language in definition

---

## Prioritization Framework

### Tier 1 — Must-Address Before Signing

MAC elements that create deal certainty risk or expose a party to material loss if not
corrected:

- Missing pandemic/epidemic carve-out (post-2020)
- OCB covenant with no crisis management carve-out (AB Stable risk)
- Double materiality scrape in bring-down creating unclear closing standard
- No disproportionate impact exception where deal is in a volatile industry
- Financing MAC materially broader than deal MAC without RTF protections

### Tier 2 — Strong Negotiating Positions

Elements that materially affect risk but have room to negotiate:

- Scope of disproportionate impact exception (which carve-outs it covers)
- Precision of anti-circularity language
- Comparator group definition for disproportionate impact analysis
- Buyer consent standard in OCB covenant
- Whether "prospects" is included in the MAC definition

### Tier 3 — Concession Candidates

Positions that improve one party's position but can be conceded strategically:

- Exact threshold language ("materially" vs. "significantly") in disproportionate
  impact exception
- Whether subsidiaries measured individually vs. consolidated
- Governing law for disputes over MAC interpretation (if primary governing law already
  accepted)

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                      | Fail Action                                                  |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Source**     | Every MAC case law citation identifies the court, year, and key holding                                                                   | Add citation or mark "[UNVERIFIED — M&A counsel to confirm]" |
| **Format**     | All citations follow a consistent format: Case Name (Court Year) [VERIFY if unconfirmed]                                                  | Fix format                                                   |
| **Currency**   | Each case cited is still good law — has it been affirmed, reversed, or distinguished?                                                     | Flag "[CHECK CURRENCY — may have been subsequently decided]" |
| **Domain**     | MAC analysis stays within the contract's governing law; no Delaware cases cited as authority in English law matters without qualification | Remove or flag jurisdictional bleed                          |
| **Confidence** | Uncertainty explicitly stated, not hidden. If MAC outcome is uncertain, say so rather than asserting false certainty                      | Add confidence qualifier                                     |

### Self-Interrogation for RED-Classified Items

For any item classified RED, apply this 3-pass review before delivery:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the
clause language and the cited authority? Would a Delaware court (or English court) actually
reach this conclusion on these facts? What would the other side's counsel say?

**Pass 2 — Completeness**: Have all relevant carve-outs and interactions been considered?
Are there other provisions in the agreement that mitigate the identified RED risk? (e.g.,
an OCB covenant risk may be mitigated by a broad consent carve-out elsewhere)

**Pass 3 — Challenge**: What is the strongest argument that this element is acceptable?
Under what deal context might a sophisticated buyer/seller accept this risk? Is the RED
classification proportionate, or is YELLOW with mitigation more accurate?

_Track result as_: `self_interrogation: PASS` (RED classification stands) or
`self_interrogation: REVISED` (reclassify or note mitigation).

### Confidence Scoring

| Level        | Range     | Meaning                                                       | Action                                                    |
| ------------ | --------- | ------------------------------------------------------------- | --------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled Delaware law, clear case holding directly on point    | State with confidence                                     |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions              | State with brief caveat                                   |
| **Probable** | 0.60–0.79 | Good arguments but reasonable M&A lawyers could differ        | State with explicit reasoning and contra-indicators       |
| **Possible** | 0.40–0.59 | Genuinely uncertain, competing authorities or novel situation | Flag for M&A counsel review with both sides               |
| **Unlikely** | 0.0–0.39  | Speculative, weak basis                                       | Do not assert; flag "[UNCERTAIN — M&A counsel to advise]" |

---

## Glass Box Audit Trail

Append this YAML to every output. It provides traceability and auditability.

```yaml
glass_box:
  skill: "legalcode-mac-clause-analysis"
  agreement: "[Agreement title and date]"
  deal_type: "[Merger / SPA / APA / LBO / Investment]"
  user_side: "[Buyer / Seller / Lender / Neutral]"
  governing_law: "[Delaware / English law / Other]"
  analysis_basis: "[Organizational playbook / General market standard]"
  mac_tiers_analyzed:
    tier_1_general_definition: "[Analyzed / Not present]"
    tier_2_carveouts_count: "[N carve-outs identified]"
    tier_3_disproportionate_impact: "[Present / Absent / Partial — N of M carve-outs]"
  bring_down_analyzed: "[Yes / No]"
  ocb_covenant_analyzed: "[Yes / No]"
  financing_mac_analyzed: "[Yes / Not applicable]"
  legalcode_mcp: "Connected / Not connected"
  cases_cited:
    - "IBP v. Tyson Foods (Del. Ch. 2001) — [VERIFIED / UNVERIFIED]"
    - "Hexion v. Huntsman (Del. Ch. 2008) — [VERIFIED / UNVERIFIED]"
    - "Akorn v. Fresenius Kabi AG (Del. Ch. 2018) — [VERIFIED / UNVERIFIED]"
    - "AB Stable VIII v. MAPS Hotels (Del. Ch. 2020; Del. 2021) — [VERIFIED / UNVERIFIED]"
    - "Snow Phipps v. KKR (Del. Ch. 2021) — [VERIFIED / UNVERIFIED]"
  red_items_count: "[N]"
  yellow_items_count: "[N]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence_overall: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "Analysis based on clause text only — underlying facts needed to assess actual MAC risk"
    - "Case law citations require verification against current authoritative sources"
    - "[Any scope limitations or assumptions]"
  reviewer: "AI-assisted — requires qualified M&A counsel review"
```

---

## Anti-Patterns

What NOT to do when analyzing or drafting MAC/MAE clauses:

1. **Treating MAC invocation as routine**: MAC is an extraordinary remedy. Delaware courts
   have found a MAC in only a handful of cases since IBP. Do not advise clients to invoke
   MAC without detailed factual analysis and a clear durational-impact theory.

2. **Conflating MAC with ordinary breach**: A seller that misses quarterly earnings has
   not necessarily suffered a MAC. Do not treat any negative development as potential MAC
   justification — this leads to overconfident positions and litigation exposure.

3. **Ignoring the OCB covenant**: Post-AB Stable, analyzing the MAC clause in isolation
   from the OCB covenant is malpractice-level error. The two provisions interact
   systematically; always analyze them together.

4. **Asserting MAC without durational analysis**: Delaware requires that the adverse
   change be "consequential to the company's long-term earnings power over a commercially
   reasonable period, measured in years, not months." Any MAC opinion that does not
   address duration is incomplete.

5. **Citing Akorn as the standard**: Akorn is the exception, not the rule. It involved
   pervasive, systemic, undisclosed regulatory fraud that destroyed 86% of EBITDA. Citing
   Akorn to support ordinary business deterioration is misleading.

6. **Assuming pandemic carve-outs are complete protection**: As AB Stable showed, a
   pandemic carve-out protects from a MAC finding but does NOT authorize OCB covenant
   deviations. Always analyze the OCB covenant for crisis response flexibility.

7. **Ignoring anti-circularity**: MAC definitions that exclude stock price changes and
   missed projections but do not include anti-circularity language ("excluding the
   underlying causes") can still allow those metrics to be used as evidence of MAC.
   These are different protections.

8. **Drafting disproportionate impact exception for only some carve-outs** without
   conscious intent: Asymmetric inclusion of the exception across carve-outs creates
   unintended risk allocation. Each carve-out's inclusion/exclusion from the exception
   must be deliberate.

9. **Conflating "prospects" exclusion from MAC with forward-looking analysis**:
   Excluding "prospects" from the MAC definition limits it to current and past conditions.
   Forward-looking language ("would reasonably be expected") is a separate structural
   element — a definition can include forward-looking triggering language but still
   exclude "prospects" as a measurement metric.

10. **Ignoring the bring-down standard**: The specific standard for bringing down the
    MAC representation at closing (e.g., "true in all material respects" vs. "true
    except where failure would not constitute a MAE") can significantly affect buyer's
    closing rights. Double materiality scrapes are a known risk.

11. **Drafting standalone MAC condition identically to the rep bring-down**: Some
    agreements use the same MAE definition for both uses. But the standalone closing
    condition and the rep bring-down serve different functions and may require different
    cure periods, notice requirements, and measurement dates.

12. **Failing to analyze the financing commitment letter alongside the deal MAC**:
    In LBO/leveraged transactions, the Financing MAC and the deal MAC may have different
    thresholds. A narrower Financing MAC leaves buyer exposed to specific performance
    claims when lenders pull out but the deal MAC has not been triggered.

13. **Relying on English Takeover Code Rule 13 analysis for private M&A**:
    The Takeover Code's exceptionally high MAC bar (public company takeovers) does not
    apply to private M&A. English law private M&A MAC standards are different and more
    contractual. Do not use Takeover Code precedents to analyze private deal MAC clauses.

14. **Missing post-2020 market standard shift**: The COVID-19 pandemic fundamentally
    changed MAC drafting norms. Pandemic/epidemic carve-outs, OCB covenant flexibility
    provisions, and consent processes for operational responses are now market standard.
    Applying pre-2020 market standards to current deals is an error.

15. **Assuming specific performance is always available**: Delaware courts strongly favor
    specific performance in merger agreements (IBP v. Tyson). But specific performance
    requires a valid and enforceable agreement — if the buyer validly invoked MAC, specific
    performance is unavailable. The analysis must determine whether MAC was properly
    invoked before assessing remedies.

16. **Ignoring the knowledge qualifier question**: Whether buyer can invoke MAC based on
    risks it knew about at signing is a significant open issue. Akorn suggests that known
    risks, at some point, may be priced into the deal and not available for later MAC
    invocation. Some agreements address this explicitly; many do not.

---

## Writing Standards

Apply these standards before delivering any MAC analysis:

1. **Lead with the conclusion**: State the overall MAC risk assessment (buyer-favorable /
   balanced / seller-favorable) before detailing element-by-element findings.

2. **Separate findings by tier**: Present Tier 1 (General Definition), Tier 2 (Carve-Outs),
   and Tier 3 (Disproportionate Impact) findings in structured sections.

3. **Flag jurisdiction clearly**: Every case law citation must identify the jurisdiction
   and year. Never cite Delaware cases as applicable to English law matters without
   explicit qualification.

4. **Use the classification consistently**: RED / YELLOW / BALANCED labels must be applied
   consistently throughout. Do not use "significant" or "important" as informal substitutes.

5. **Redlines must be ready to use**: Do not provide guidance like "consider adding language
   about proportionality." Provide exact alternative language that can be sent to
   counterparty counsel.

6. **Mark all unverified citations**: Every statutory and case law citation should be
   marked [VERIFY] unless confirmed via legalcode-mcp.

7. **Qualify speculative analysis**: MAC outcomes depend heavily on facts that are often
   unknown at drafting. Flag analytical conclusions that depend on factual assumptions
   with explicit qualification (e.g., "assuming no significant deterioration prior to
   closing, this carve-out should protect the seller...").

8. **Avoid false precision**: Do not state that a specific % of EBITDA decline "will"
   or "will not" constitute a MAC. Delaware courts have declined to set bright-line
   numerical thresholds. Frame quantitative analysis as factors weighing toward/against
   MAC, not as definitive triggers.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for current status of Akorn, AB Stable, Hexion, IBP, Snow Phipps, and Channel
  Medsystems (verify whether affirmed, distinguished, or followed)
- Search for any Delaware Court of Chancery MAC decisions post-2021
- Search for English Takeover Panel Statements on MAC conditions (public takeovers)
- Search for current ABA M&A Deal Points Study data on MAC carve-out market practice
- Save results to `/tmp/legalcode-mac-research.md`
- Mark all legalcode-mcp-confirmed citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Use the Case Law Reference Framework above
- Mark all citations [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — all citations require independent verification"`
- Focus analysis on structural and drafting elements (Tiers 1-3), burden allocation,
  OCB interaction, and redlines; defer specific case law application to M&A counsel

---

## Localization Notes

### US — States Other than Delaware [JURISDICTION-SPECIFIC]

Most major M&A transactions are governed by Delaware law. For non-Delaware US transactions:

- New York law applies to many financial services and real estate transactions
- New York courts have applied similar MAC standards to Delaware but with some differences
- California and other states have less developed MAC jurisprudence
- Verify applicable case law for the specific governing state [VERIFY]

### English Law — Public Company Takeovers [JURISDICTION-SPECIFIC]

- Takeover Code Rule 13 governs MAC conditions in public company offers
- The Takeover Panel has near-absolute control over MAC condition invocation
- MAC conditions in public offers require Panel approval before lapsing
- The standard is "entirely exceptional" — almost never met in practice
- The Code prohibits subjective MAC conditions (must be objectively verifiable)

### English Law — Private M&A [JURISDICTION-SPECIFIC]

- No equivalent of the Delaware IBP/Hexion jurisprudence
- Clause language governs more heavily than in Delaware
- English courts interpret MAC clauses as carefully negotiated commercial provisions
- Specific performance discretionary (courts weigh hardship and circumstances)
- Consider whether "Material Adverse Change" vs. "Material Adverse Effect" terminology
  carries any English-law-specific connotation in the particular industry [VERIFY]

### European Civil Law Jurisdictions [JURISDICTION-SPECIFIC]

- MAC clauses in deals governed by French, German, Dutch, or other civil law systems
  require jurisdiction-specific legal analysis
- German law equivalent: wesentliche Verschlechterung (substantial deterioration); courts
  consider the doctrine of Wegfall der Geschäftsgrundlage (frustration of contract basis)
- French law: consider interaction with force majeure and imprévision (Civil Code Art. 1195)
- Civil law courts may be less familiar with MAC clauses from common law M&A practice
- Always engage local counsel for civil law MAC analysis [VERIFY]

---

## Output Format Template

Structure every analysis output using this template:

```markdown
# MAC/MAE Clause Analysis

**Agreement**: [Title and date]
**Deal type**: [Merger / SPA / APA / LBO / Investment]
**Governing law**: [Delaware / English / Other]
**Client side**: [Buyer / Seller / Lender / Neutral]
**Analysis date**: [YYYY-MM-DD]

---

## Executive Summary

**Overall MAC risk assessment**: [BUYER-FAVORABLE / BALANCED / SELLER-FAVORABLE]
**Key risks identified**: [Top 3 issues in 1-2 lines each]
**Recommended next steps**: [Top 3 action items]

---

## Tier 1 — General MAE Definition Analysis

| Element     | Present | Classification      | Finding            |
| ----------- | ------- | ------------------- | ------------------ |
| [Element 1] | Yes/No  | RED/YELLOW/BALANCED | [1-2 line finding] |
| [Element 2] | ...     | ...                 | ...                |

**Confidence**: [Score and rationale]

**Redline (if applicable)**:

> **Current language**: "[exact quote]"
> **Proposed**: "[exact alternative]"
> **Rationale**: [1-2 sentences]
> **Priority**: [Tier 1 / Tier 2 / Tier 3]
> **Fallback**: [Alternative if primary rejected]

---

## Tier 2 — Carve-Out Analysis

### Carve-Outs Present

| #   | Carve-Out     | Standard?    | Classification                                | Notes       |
| --- | ------------- | ------------ | --------------------------------------------- | ----------- |
| 1   | [Description] | ✅ / ⚠️ / ❌ | BUYER-FAVORABLE / BALANCED / SELLER-FAVORABLE | [Key issue] |
| ... |               |              |                                               |             |

### Missing Standard Carve-Outs

| Carve-Out           | Severity   | Recommended Language |
| ------------------- | ---------- | -------------------- |
| [Missing carve-out] | RED/YELLOW | [Proposed language]  |

---

## Tier 3 — Disproportionate Impact Exception Analysis

**Present?**: [Yes / No / Partial — N of M carve-outs]
**Classification**: [BUYER-FAVORABLE / BALANCED / SELLER-FAVORABLE]

[Finding: which carve-outs include the exception, which do not, and what the threshold language says]

**Confidence**: [Score and rationale]

---

## Bring-Down Mechanics

| Element                        | Finding   | Classification   |
| ------------------------------ | --------- | ---------------- |
| [Bring-down standard]          | [Finding] | [Classification] |
| [Standalone closing condition] | [Finding] | [Classification] |

---

## Ordinary Course Covenant Interaction (AB Stable Risk Assessment)

**OCB Covenant**: [Present / Absent]
**Crisis management carve-out in OCB**: [Present / Absent]
**AB Stable risk level**: [HIGH / MEDIUM / LOW]

[1-2 paragraph analysis of OCB interaction with MAC carve-outs]

---

## Financing MAE Analysis [if applicable]

[Analysis of Financing MAC vs. deal MAC, RTF interaction]

---

## Negotiation Priorities

### Tier 1 — Must-Address Before Signing

[List of RED items requiring resolution]

### Tier 2 — Strong Negotiating Positions

[List of YELLOW items worth negotiating]

### Tier 3 — Concession Candidates

[Items that can be conceded strategically]

---

## Case Law Application

[Key cases applicable to this MAC clause and their relevance to the specific language analyzed]

---

[Glass Box YAML]
```

---

## Provenance

Created by Legalcode (2026-03-22). Original synthesis covering the full MAC/MAE clause
analysis framework for US and UK M&A transactions. Research basis: Delaware Court of
Chancery case law (IBP v. Tyson 2001, Hexion v. Huntsman 2008, Akorn v. Fresenius 2018,
AB Stable VIII v. MAPS Hotels 2020-2021, Snow Phipps v. KKR 2021), ABA M&A Deal Points
Study market practice data, UK Takeover Code Rule 13 and Panel guidance, and synthesis
of Legalcode repository MAC/MAE coverage in `legalcode-merger-agreement-analysis` and
`legalcode-purchase-agreement-review`. All case law citations require independent
verification before reliance.
