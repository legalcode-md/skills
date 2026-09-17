---
name: legalcode-merger-agreement-analysis
description: Analyze merger agreements clause-by-clause against market standards or a transaction playbook.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Analyze merger agreements clause-by-clause against market standards or a transaction playbook. Covers deal structure (forward merger, reverse triangular merger, statutory merger), representations and warranties (bring-down conditions, materiality scrape, fundamental vs. general reps, survival periods), MAC/MAE clause drafting and judicial standards (Akorn, Snow Phipps), interim operating covenants (ordinary course, consent thresholds, efforts standards), conditions to closing (regulatory approvals, HSR, CMA, EU merger regulation, CFIUS), deal protection mechanisms (no-shop, fiduciary out, matching rights, go-shop), termination rights and fees (breakup fees, reverse termination fees), consideration structures (cash, stock-for-stock, mixed, earnouts), and dissenter/appraisal rights (DGCL Section 262, UK scheme squeeze-out). Classifies findings GREEN/YELLOW/RED with confidence scoring, Tier 1/2/3 negotiation prioritization, and actionable redlines with fallback positions. Use for buy-side or sell-side public or private mergers, triangular mergers, schemes of arrangement, PE take-privates, strategic acquisitions, and cross-border deals. Covers US (Delaware-centric) and UK (Takeover Code and Companies Act) deal conventions with jurisdiction markers. Supports transaction-playbook-based or general-market-standard review.


# Legalcode Merger Agreement Analysis

> **Disclaimer**: This skill provides a framework for AI-assisted merger agreement analysis. It
> does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before use. Laws change; verify current
> applicability before relying on any provision described here. Statutory and case law
> references cited from memory carry hallucination risk — verify against authoritative
> sources before relying on them. Merger agreement analysis requires professional judgment to
> assess materiality, deal impact, board fiduciary duties, and regulatory risk. No AI tool
> replaces experienced M&A counsel.

---

## Purpose and Scope

This skill analyzes merger agreements against an organization's transaction playbook or general
M&A market standards. It identifies clause deviations, classifies their severity, generates
actionable redline suggestions, and produces a confidence-scored, auditable analysis with
negotiation strategy and business impact assessment.

**Covers:**

- Deal structure analysis (merger type, tax structuring considerations, liability implications)
- MAC/MAE clause drafting and judicial standard analysis (Delaware and UK)
- Representations and warranties analysis (scope, qualifiers, bring-down conditions, materiality
  scrape, fundamental vs. general, survival periods)
- Interim operating covenant review (ordinary course standard, consent thresholds, efforts
  standards hierarchy)
- Conditions to closing analysis (regulatory approvals, HSR/CMA/EU merger control, CFIUS)
- Deal protection mechanism review (no-shop, fiduciary out, matching rights, go-shop, last look)
- Termination rights and fee analysis (breakup fees, reverse termination fees, risk-based pricing)
- Consideration structure and payment mechanics (cash, stock, mixed, earnouts, exchange ratios)
- Appraisal and dissenter rights (DGCL Section 262, UK scheme/contractual offer squeeze-out)
- D&O indemnification and tail insurance review
- Employee matters and retention provisions
- Post-closing covenants and integration governance
- GREEN/YELLOW/RED deviation classification with confidence scoring
- Redline generation with fallback positions
- Missing provision detection and gap analysis
- Negotiation strategy with Tier 1/2/3 prioritization
- Multi-stakeholder impact mapping (buyer, target, shareholders, financing sources, regulators)
- Glass Box audit trail for traceability

**Does not:**

- Draft new merger agreements (see drafting-specific skills)
- Provide legal advice or replace qualified M&A counsel
- Perform financial modeling, synergy analysis, or deal valuation
- Conduct pre-signing due diligence (see `legalcode-ma-due-diligence-checklist`)
- Apply to stock purchase agreements or asset purchase agreements (see `legalcode-purchase-agreement-review`)
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers

**Complementary skills:**

- `legalcode-ma-due-diligence-checklist` — pre-signing diligence across 12 workstreams
- `legalcode-due-diligence-report` — executive-ready findings from diligence
- `legalcode-purchase-agreement-review` — SPA/APA clause-by-clause analysis
- `legalcode-term-sheet-analysis` — LOI/term sheet review before definitive agreement

---

## Jurisdiction and Governing Law

This skill is US/UK-focused with jurisdiction-agnostic framework elements. The merger
agreement's own governing law determines which legal framework applies.

[JURISDICTION-SPECIFIC] **United States (Delaware-centric)**:

- Delaware General Corporation Law (DGCL) governs most US public company mergers [VERIFY]
- Delaware Court of Chancery standards for MAC/MAE (Akorn v. Fresenius Kabi 2018; Snow Phipps
  v. KKR 2021) set high bar for invocation [VERIFY]
- HSR Act filing thresholds (indexed annually; $111M for FY 2024) [VERIFY current threshold]
- CFIUS mandatory filing triggers (TID US businesses; critical infrastructure; sensitive
  personal data) [VERIFY]
- DGCL Section 262 appraisal rights: available to dissenting stockholders in statutory mergers
  unless certain exceptions apply (market-out exception, listing exception) [VERIFY]
- Fiduciary duty of target board under Revlon (for sale of control) and Unocal (deal
  protection mechanisms) standards [VERIFY]

[JURISDICTION-SPECIFIC] **United Kingdom**:

- UK Takeover Code (City Code) governs public company acquisitions; Panel enforces strict
  timetables, no-frustration rules, and mandatory cash offer triggers [VERIFY]
- Rule 2.7 firm intention announcement commits bidder to proceed [VERIFY]
- Scheme of arrangement (Companies Act 2006, Part 26A): 75% in value, majority in number
  threshold; binding on all shareholders [VERIFY]
- Contractual offer: 90% threshold required for compulsory acquisition squeeze-out [VERIFY]
- MAC standard in UK context: "entirely exceptional in nature" and "very considerable
  significance striking at heart of transaction purpose" — significantly higher bar than
  Delaware [VERIFY]
- Rule 9 mandatory cash offer triggered at ≥30% voting rights acquisition [VERIFY]
- Financing conditions disfavored; committed facilities required before announcement [VERIFY]

[JURISDICTION-SPECIFIC] **Cross-border considerations**:

- US bidder for UK target: navigates both Takeover Code AND US securities law if stock
  consideration used (Securities Act 1933 registration may be required) [VERIFY]
- EU Merger Regulation: Phase I 25 working days; Phase II up to 90 working days [VERIFY]
- National security screening: UK NSIA 2021 (mandatory sectors); US CFIUS; other
  jurisdictions as applicable [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- Multiple valid approaches exist and the user's preference matters
- Deal structure ambiguity creates a fork that only the user can resolve
- Risk tolerance or business context is needed to classify severity correctly

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

### Step 1: Accept the Agreement

Accept the merger agreement in any of these formats:

- **File**: PDF, DOCX, or other document format
- **URL**: Link to the document in a VDR, CLM, Edgar, or cloud storage system
- **Pasted text**: Agreement text pasted directly into the conversation

Note whether ancillary documents (disclosure schedules, exhibits, voting agreements,
support agreements, financing commitments, RWI policy) are included; their absence limits
the analysis and must be noted in the Glass Box audit trail.

---

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask the user:

1. **Your side in the transaction?**
   - Options: Buyer (Acquirer), Target (Company), Target shareholders, Advisor (specify side),
     Board committee (special committee, audit committee), Other
   - _Why this matters_: The entire analysis pivots depending on which side you represent. What
     protects a buyer (broad MAC, strong no-shop, low RTF) harms a target, and vice versa.

2. **Deal type / merger structure?**
   - Options: Forward triangular merger (target merges into buyer sub; sub survives), Reverse
     triangular merger (buyer sub merges into target; target survives as subsidiary),
     Direct/statutory merger (parties merge directly), Scheme of arrangement (UK), Other
   - _Why this matters_: Reverse triangular mergers preserve non-transferable contracts and
     licenses; forward triangular mergers provide asset acquisition tax treatment but risk
     contract loss. Structure affects analysis of anti-assignment clauses and closing conditions.

3. **Target type (public or private)?**
   - Options: US public company (SEC-registered), UK public company (Takeover Code), Private
     company (US), Private company (UK/other), Other
   - _Why this matters_: Public company mergers require fiduciary out provisions, proxy/circular
     disclosure, appraisal rights, and (for UK) Takeover Code compliance. Private company
     mergers can include more tailored deal protection.

4. **Approximate transaction value?**
   - Options: Under $100M, $100M–$500M, $500M–$2B, $2B–$10B, Over $10B, Not disclosed
   - _Why this matters_: Deal size affects regulatory filing thresholds (HSR, CMA, EU),
     market-standard termination fee percentages, and appropriate escrow/indemnification levels.

5. **Governing law?**
   - Options: Delaware (US), Another US state (specify), English law (UK), Other
   - _Why this matters_: Determines applicable MAC/MAE judicial standards, appraisal rights
     procedures, fiduciary duty framework, and mandatory regulatory filings.

6. **Regulatory risk profile?**
   - Options: Low (simple horizontal deal, no market overlap), Moderate (some overlap, HSR
     or one foreign filing expected), High (significant overlap, HSR second request risk, EU or
     UK Phase II likely), Unknown/not yet assessed
   - _Why this matters_: Determines whether reverse termination fee levels, outside dates, and
     regulatory efforts covenants are market-appropriate.

If the user provides partial context, proceed with what is provided and **state assumptions
explicitly** (e.g., "Assuming target-side representation and Delaware law — correct me if wrong
and I'll revise the analysis").

---

### Step 3: Load the Transaction Playbook

Check for the organization's M&A playbook in local settings (e.g., `legal.local.md` or
transaction-specific configuration files).

The playbook should define:

- **Standard positions**: Preferred terms for key provisions (MAC carve-outs, efforts standard,
  termination fee caps, no-shop scope, fiduciary out trigger, matching rights period)
- **Acceptable ranges**: Terms that can be agreed without escalation
- **Escalation triggers**: Terms that require outside counsel, board, or special committee review

**If no playbook is configured:**

**⟁ CLARIFY** — Inform the user that no playbook was found, and ask which approach:

- **Option A: Proceed against general market standards** — Use current market data (ABA M&A
  Deal Points Study, Haynes & Boone Transaction Fee Study, NABMRG) as the baseline. Label:
  "Based on general market standards — not organizational playbook."
- **Option B: Define key positions now** — Walk through defining positions on the 5 most
  material provisions (MAC carve-outs, efforts standard, termination fee cap, no-shop/fiduciary
  out balance, outside date mechanism). Takes time upfront but produces a more precise analysis.
- **Option C: Provide positions as we go** — Start the review and ask about preferred positions
  when they matter for each clause.

---

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Read the agreement's governing law clause and identify the applicable jurisdiction. Then
use **legalcode-mcp** to build a working legal reference file for this review.

**Research process:**

1. **Identify the governing law** from the agreement.

   **⟁ CLARIFY** — If any of the following apply, ask before proceeding:
   - **No governing law clause**: Flag as RED and ask which jurisdiction to apply.
   - **Conflicting governing law across schedules**: Ask which governs the main body.
   - **Governing law inconsistent with target incorporation**: Note the inconsistency.

2. **Search legalcode-mcp** for jurisdiction-relevant authority:
   - MAC/MAE judicial standards and leading cases for the governing jurisdiction
   - Merger statutes (DGCL for Delaware; Companies Act 2006 for UK) [VERIFY]
   - Fiduciary duty standards applicable to target board in sale-of-control context [VERIFY]
   - Applicable regulatory approval regimes and current filing thresholds [VERIFY]
   - Appraisal rights procedures and leading case law on fair value determination [VERIFY]
   - Efforts standard case law for the governing jurisdiction [VERIFY]
   - Any recent legislative or regulatory developments affecting the merger structure [VERIFY]

3. **Save the most relevant results** to `/tmp/legalcode-merger-authority.md`.

4. **Use this reference throughout the analysis.** Mark legalcode-mcp-sourced citations as
   VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**

- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed using general M&A knowledge; flag that authority has not been independently verified

---

### Step 5: Map Deal Structure and Identify Path

Before clause-by-clause review, map the deal structure to identify which analytical path to follow:

1. **Confirm merger structure** from the recitals and merger mechanics provisions:
   - Is it a forward or reverse triangular merger? Or direct statutory merger?
   - For UK: scheme of arrangement or contractual offer?
   - Note the merger sub's role, surviving entity, and the consideration to be paid.

2. **Identify the deal protection devices** present in the agreement (no-shop, go-shop, fiduciary
   out, matching rights, last look). Summarize in a one-line deal protection profile.

3. **Identify regulatory approval requirements** from the closing conditions:
   - Which regulatory filings are required (HSR, EU, UK CMA, CFIUS, sector-specific)?
   - What are the outside date(s) and extension mechanisms?

4. **Flag any structural anomalies** worth highlighting before the full analysis:
   - Direct merger where triangular structure is market standard for liability protection
   - Absence of a reverse termination fee in a deal with material regulatory risk
   - No MAC definition despite reliance on it in closing conditions
   - Financing condition in a UK Takeover Code context (disfavored by Panel)

**⟁ CLARIFY** — If the merger structure is ambiguous or uses an unusual form (e.g., LLC
merger, UP-C structure, SPAC merger), confirm the structure with the user before proceeding.

---

### Step 6: Critical Deal Mechanics Assessment

Before the full clause-by-clause analysis, present a summary assessment of the 12 most
material merger mechanics. This gives the user an immediate view of the deal's risk profile.

| #   | Mechanic                        | Value in Agreement | Market Standard                                                       | Status             |
| --- | ------------------------------- | ------------------ | --------------------------------------------------------------------- | ------------------ |
| 1   | MAC/MAE definition              | [Extract]          | Carve-outs for macro/industry events with disproportionate carve-back | [GREEN/YELLOW/RED] |
| 2   | Bring-down standard             | [Extract]          | "All material respects" or MAE-qualified                              | [GREEN/YELLOW/RED] |
| 3   | Materiality scrape              | [Extract]          | Double scrape in ~64% of deals (ABA 2023) [VERIFY]                    | [GREEN/YELLOW/RED] |
| 4   | Efforts standard                | [Extract]          | "Reasonable best efforts" or "commercially reasonable"                | [GREEN/YELLOW/RED] |
| 5   | No-shop / fiduciary out balance | [Extract]          | Fiduciary out required for public company board                       | [GREEN/YELLOW/RED] |
| 6   | Matching rights period          | [Extract]          | 3–5 business days typical [VERIFY]                                    | [GREEN/YELLOW/RED] |
| 7   | Termination fee (target)        | [Extract]          | 2–3% of deal value [VERIFY]                                           | [GREEN/YELLOW/RED] |
| 8   | Reverse termination fee         | [Extract]          | 2–4% (low risk) to 4–6.5% (high reg. risk) [VERIFY]                   | [GREEN/YELLOW/RED] |
| 9   | Outside date and extension      | [Extract]          | Initial + automatic extension for regulatory approval                 | [GREEN/YELLOW/RED] |
| 10  | Appraisal / dissenter rights    | [Extract]          | DGCL §262 / UK scheme mechanics as applicable                         | [GREEN/YELLOW/RED] |
| 11  | Regulatory approval condition   | [Extract]          | Clearly specified filings; standard termination rights                | [GREEN/YELLOW/RED] |
| 12  | D&O tail / indemnification      | [Extract]          | 6-year D&O tail at existing or comparable coverage                    | [GREEN/YELLOW/RED] |

---

### Step 7: Clause-by-Clause Analysis

Analyze the merger agreement systematically across all 18 analytical categories below. Read
the entire agreement before flagging issues — provisions interact (e.g., a weak MAC carve-out
may be partially offset by a buyer-favorable materiality scrape; a broad no-shop may be
partially mitigated by a well-drafted fiduciary out).

**⟁ CLARIFY** — For very long agreements (60+ pages, multiple schedules and exhibits):

- Ask whether to perform a **full review** (all 18 categories) or **priority review** focused
  on the user's highest-risk areas.
- If ancillary documents (support agreements, equity commitment letters, debt commitment letters)
  are included, ask whether to include them in scope.

For each category, assess against the playbook (or general market standards), classify the
finding, and generate actionable output per the **Deviation Severity Classification** below.

---

#### PART A — Deal Structure and Transaction Mechanics

**A-1: Merger Structure and Surviving Entity**

_What to analyze:_

- Merger type (forward triangular, reverse triangular, direct statutory merger)
- Identity of the surviving entity and its organizational documents post-merger
- Treatment of merger sub equity and outstanding target equity
- Whether the structure appropriately preserves non-transferable licenses and contracts
- Change-of-control implications for material contracts of the target under applicable law
- Potential loss of permits, licenses, or governmental approvals in the merger

_Market standard:_ Reverse triangular merger is the market-dominant structure for US acquisitions
where the target has material non-transferable assets or licenses. Forward triangular used when
asset acquisition tax treatment is preferred. Direct merger less common for large deals.

_Jurisdiction-specific:_
[JURISDICTION-SPECIFIC] For UK, determine whether structure is a scheme of arrangement (preferred
for recommended transactions; 75%+50 threshold) or contractual offer (90% threshold for compulsory
acquisition). Schemes are more efficient but require court supervision and are binding on all
shareholders. [VERIFY]

_Common issues:_

- Forward merger used where target holds non-transferable IP licenses or government contracts,
  triggering inadvertent assignment
- Merger sub with inadequate capitalization or authority for the merger mechanics
- Surviving entity's charter/bylaws not specified or inconsistent with the deal structure
- Change-of-control clauses in material contracts not mapped against merger structure selected

---

**A-2: Consideration Mechanics**

_What to analyze:_

- Form of consideration (all-cash, stock-for-stock, mixed cash/stock)
- For stock consideration: exchange ratio (fixed, floating, or collar), determination date, and
  proration mechanisms
- For earnout components: metric definition (EBITDA, revenue), measurement period, tiered
  payment structure, buyer's operational control obligations during earnout period, seller
  audit rights
- Consideration adjustment mechanisms (net debt adjustment, working capital peg, cash
  sweep, transaction expense escrow)
- Treatment of in-the-money options, RSUs, restricted stock, warrants, convertible notes

_Market standard:_ Cash consideration is most common for private targets. Stock consideration
requires market price risk allocation (collar, walk-away rights). Mixed consideration (~60-70%
cash + stock) is common for large strategic acquisitions. Earnouts used in ~30% of private
deals (ABA 2023) [VERIFY] to bridge valuation gaps; EBITDA is the most common metric (~50%).

_Common issues:_

- Exchange ratio with no collar mechanism exposing target shareholders to buyer stock price risk
  during a long regulatory approval period
- EBITDA earnout without precise definition of add-backs, accounting methodology, and adjustments
- Earnout with no seller audit rights or independent accountant dispute resolution mechanism
- Option treatment at variance with target equity plan terms (requires plan amendment analysis)
- In-the-money convertible note conversion mechanics not addressed

---

**A-3: Financing Mechanics and Certainty of Funds**

_What to analyze:_

- For all-cash deals: confirmed financing (equity commitment letter, debt commitment letter/credit
  agreement); financing condition (present or absent)
- Specificity of financing condition: can buyer walk if banks withdraw committed financing?
- Relationship between financing failure, buyer MAC, and reverse termination fee
- Rollover equity mechanics if any target equity rolls into the acquiring entity

_Market standard:_ In US public company mergers, financing conditions are uncommon in large-cap
strategic deals but standard in PE take-privates. If present, reverse termination fee (RTF) is
the target's primary remedy for financing failure; buyer's obligation to close is often limited
to payment of the RTF. In UK, financing conditions are strongly disfavored by the Takeover Panel;
committed facilities required before announcement. [VERIFY]

_Common issues:_ Financing condition with no RTF leaving target without adequate remedy if deal
fails. RTF structured as sole remedy even for willful buyer breach.

---

#### PART B — Representations and Warranties

**B-1: Target Representations**

_What to analyze:_

- Scope of target reps (organizational, capital structure, financial statements, absence of
  changes, material contracts, litigation, regulatory compliance, intellectual property, taxes,
  employee matters, environmental, data privacy, anti-bribery, no undisclosed liabilities)
- Knowledge qualifier: whose knowledge, actual vs. constructive, list of knowledge persons
- Materiality qualifiers: "Material Adverse Effect," "in all material respects," specific dollar
  thresholds — check for consistency across rep sections
- Disclosure schedule: whether schedules are complete and whether items not listed in schedules
  are accurate without qualification
- Bring-down condition: which reps must survive to closing and to what standard

_Market standard:_ Target reps are comprehensive for public company mergers; buyers typically
require broad scope with few qualifiers at signing, accepting qualifier risk is borne at bring-down.
Material adverse effect as a qualifier (vs. a binary bring-down standard) is market for general
reps; fundamental reps typically must be true in "all material respects" or "all respects."

_Common issues:_

- Inconsistent materiality qualifiers across rep sections (some reps materiality-qualified, others
  not) creating double-counting risk with materiality scrape
- Overly narrow knowledge qualifier (CEO only, vs. senior management team)
- Blank or incomplete disclosure schedules at signing
- Financial statement rep with no specific GAAP compliance or audit standards reference

---

**B-2: Buyer Representations**

_What to analyze:_

- Scope of buyer reps (organization, authority, financing, share issuance if stock consideration,
  absence of competing acquisition agreements, no knowledge of target MAC)
- "No knowledge of target breach" rep: heavily buyer-favorable; limits target's right to sue
  for pre-closing breaches buyer knew of

_Market standard:_ Buyer reps are intentionally narrower than target reps. Key buyer reps are
authorization, financing sources, and (for stock deals) issued share authority and listing.

_Common issues:_

- Anti-sandbagging: buyer rep that it is unaware of any target rep breaches can be used to
  waive claims. 76% of 2023 deals are silent on sandbagging [VERIFY]; express anti-sandbagging
  provisions appear in ~24% of deals [VERIFY].

---

**B-3: Bring-Down Conditions and Materiality Scrape**

_What to analyze:_

- Bring-down condition standard: how accurate must reps be at closing? ("all material respects,"
  "all respects" for fundamental reps, or "Material Adverse Effect" qualification for general reps)
- Materiality scrape applicability: does the bring-down condition strip out materiality qualifiers
  embedded in the reps themselves when testing accuracy at closing?
  - **Single scrape**: Disregards materiality qualifiers when determining whether a breach
    occurred, but not when calculating damages
  - **Double scrape**: Disregards materiality qualifiers for BOTH breach determination AND
    damage calculation — heavily buyer-favorable
- Cure rights: if reps are inaccurate at closing, does the breaching party have a right to cure
  before the other party can terminate?

_Market standard:_ Double materiality scrape present in ~64% of deals for breach determination
(ABA 2023) [VERIFY]; prevalence has risen sharply since 2005 (~15%). Buyer-side request;
seller typically resists double scrape on damages calculation. Single scrape on breach
determination + no scrape on damages is a compromise position.

_Common issues:_

- Bring-down condition drafted to require "accurate in all respects" (not "material respects")
  for general reps — too buyer-favorable in most market contexts
- Materiality scrape applies inconsistently across different rep categories
- No distinction between fundamental reps (typically higher bring-down standard) and general reps
- Cure period after breach too short (1-2 days) given complexity of merger closing mechanics

---

**B-4: Survival Periods**

_What to analyze:_

- Do any reps survive closing (unusual in public company mergers; common in private mergers)?
- Survival periods by rep category: fundamental reps (typically indefinite or statute of
  limitations period), general reps (typically 12-24 months post-closing), specific
  indemnities (tax: statute of limitations + 90 days; environmental: open-ended)

_Market standard:_ In public company mergers, reps generally do not survive closing and parties
rely on closing conditions as the remedy mechanism. In private mergers, survival periods are
heavily negotiated; 2023 median for general reps is 15 months [VERIFY].

---

#### PART C — MAC/MAE Analysis

**C-1: Material Adverse Effect Definition**

_What to analyze:_

- Core definition: what events, changes, or effects constitute a Material Adverse Effect on
  the target?
- Carve-outs from the MAC definition (events excluded from what counts as a MAC):
  - General economic or financial market conditions
  - Changes affecting the industry in which the target operates (industry-wide conditions)
  - Acts of war, terrorism, natural disasters, epidemics/pandemics
  - Changes in applicable law or GAAP/accounting standards
  - Effects arising from announcement of the transaction itself (including employee attrition,
    customer reaction, supplier disruption)
  - Effects from actions taken with buyer's written consent
  - Changes in the target's stock price or credit ratings (in isolation)
  - Failure to meet internal projections or analyst estimates (in isolation)
- Disproportionate effect carve-back: carve-outs should not apply to the extent the target is
  disproportionately affected relative to comparable companies in its industry
- Buyer MAC: does the agreement also include a buyer MAC (uncommon but used in stock-for-stock
  deals where target shareholders bear buyer execution risk)?

_Market standard (US):_ MAC carve-outs are market standard in all US merger agreements. The
"disproportionate effect" carve-back is critical — without it, seller bears all industry risk
even if target is unusually exposed. Post-Akorn (2018), buyers bear a heavy burden to invoke
MAC; courts require durational impact (measured in years, not months). Post-COVID (Snow Phipps
2021), pandemic carve-out is now standard market practice. [VERIFY]

_Market standard (UK):_ MAC threshold substantially higher. Takeover Panel requires "entirely
exceptional" circumstances with "very considerable significance striking at heart of transaction
purpose." Rarely successfully invoked. [VERIFY]

_Common issues:_

- MAC definition missing "disproportionate effect" carve-back (seller bears all macro risk)
- No pandemic/epidemic carve-out (creates ambiguity for future public health events)
- MAC carve-outs narrowly drafted (e.g., covering only "natural disasters" but not "pandemics")
- MAC definition does not address party's knowledge of disclosed risks at signing
  (Akorn teaches this matters: disclosed risks generally cannot form basis of MAC claim)
- MAC measured over too short a period (Delaware requires durational quality — years, not months)

---

**C-2: MAC as Closing Condition**

_What to analyze:_

- How is MAC used as a closing condition? (Buyer may refuse to close if target suffers MAC)
- Is MAC a binary condition or qualified by materiality standards?
- Does the agreement address interaction between MAC as bring-down condition and as standalone
  termination right?
- Is there a "regulatory MAC" (material adverse effect from regulatory changes affecting deal
  economics) and how is it allocated?

_Common issues:_

- MAC condition allows buyer to walk but does not specify the standard for invoking it (leaves
  disputes to litigation)
- Buyer MAC also present, creating risk of parallel claims if deal collapses

---

#### PART D — Covenants

**D-1: Interim Operating Covenants**

_What to analyze:_

- Is the operating covenant a flat/absolute obligation or qualified by efforts standards?
- "Ordinary course of business consistent with past practice": courts measure this against the
  target's OWN historical practices, not industry norms [VERIFY Delaware case law]
- Consent required actions: what specific actions require buyer prior written consent?
  - Must-list items (require consent regardless of materiality threshold)
  - Threshold-based items (require consent if above specified dollar threshold)
- Consent standard: "not to be unreasonably withheld, conditioned, or delayed" (WCDOD)?
  Or unconditional consent right?
- Reasonable response timeline for consent requests (missing or too long = operational friction)
- Carve-outs: what is expressly permitted without consent?

_Market standard:_ Modern practice uses qualified covenants (efforts-based or materiality-
qualified) rather than flat unconditional obligations. Seller-favorable positions: WCDOD
consent standard + long response period + broad carve-outs for disclosed/budgeted items.
Buyer-favorable: absolute negative covenants + broad must-list + short consent response period.

_Common issues:_

- Flat unconditional ordinary course covenant (seller cannot respond to business needs)
- Absence of WCDOD standard on consent right (buyer can block normal business operations)
- No consent response deadline (buyer can delay indefinitely, creating closing obstruction risk)
- Negative covenant list so broad it covers routine business decisions (dividend policy, capex
  decisions, ordinary-course hiring)
- "Ordinary course" defined by reference to industry practice rather than target's own history

---

**D-2: Pre-Closing Affirmative and Negative Covenants**

_What to analyze:_

- Affirmative covenants (operate business, maintain insurance, comply with laws, pay taxes,
  preserve material contracts, obtain required consents)
- Negative covenants (no dividends, no disposals, no new debt above threshold, no new
  agreements outside ordinary course, no capital structure changes)
- Disclosure obligations (requirement to notify buyer of material events between signing and
  closing — "bring-down notice" mechanism)

_Common issues:_

- Negative covenants that prohibit actions required for regulatory compliance between signing
  and closing (e.g., mandatory law changes requiring new processes)
- No bring-down notice obligation (buyer not informed of intervening events)
- Disclosure update right with no buyer ability to re-open MAC claim for newly disclosed items

---

**D-3: Efforts Standards for Regulatory Approvals**

_What to analyze:_

- What standard of effort does each party owe with respect to obtaining regulatory approvals?
  - "Reasonable best efforts": requires all reasonable steps including good faith cooperation
  - "Commercially reasonable efforts": Delaware courts treat as substantially equivalent to
    "reasonable best efforts" [VERIFY]
  - "Best efforts": highest standard; requires all reasonable steps to solve problems [VERIFY]
- Remedy cap: is buyer's regulatory efforts obligation capped? (e.g., no obligation to divest
  more than X% of revenue; no obligation to accept behavioral remedies)
- Whether efforts covenant includes a specific obligation to litigate to challenge regulatory
  block (litigation covenant)
- Outside date mechanism: can parties extend if regulatory approval not yet obtained?

_Market standard:_ "Reasonable best efforts" is the most common formulation in US public
company mergers. Buyer-favorable position: cap on divestitures or structural remedies required.
Seller-favorable: uncapped efforts obligation + litigation covenant + automatic extension if
second request issued.

_Common issues:_

- Buyer efforts cap set too low (only needs to propose behavioral remedies, not structural ones)
- No litigation covenant even in deals with significant antitrust risk
- Outside date too short for realistic regulatory review (HSR Phase II + DOJ negotiations
  routinely take 9-12 months)
- Efforts obligation for target's consents (from third parties) less rigorous than regulatory

---

**D-4: Post-Closing Covenants**

_What to analyze:_

- Transition services agreement (TSA) framework: scope, duration, pricing, exit rights
- Non-compete and non-solicitation obligations (scope, duration, geographic scope,
  enforceability under applicable law)
- Confidentiality obligations for seller/target post-closing
- Further assurances covenant: cooperation on post-closing filings and regulatory matters
- Key employee retention arrangements: rollover equity, retention bonuses, non-solicitation

_Common issues:_

- Non-compete duration exceeding enforceability limits under applicable law (e.g., FTC
  non-compete rule, state restrictions) [VERIFY current FTC non-compete rule status]
- TSA not included for carve-outs or businesses with shared services dependencies
- No post-closing cooperation for tax audits, litigation, or regulatory matters

---

#### PART E — Conditions to Closing

**E-1: Target-Side Conditions**

_What to analyze:_

- Accuracy of buyer representations (to what standard?)
- Buyer covenant compliance
- Payment of consideration
- Receipt of financing (if financing condition present)
- Absence of buyer MAC (if present)
- Required regulatory approvals obtained by buyer

---

**E-2: Buyer-Side Conditions**

_What to analyze:_

- Accuracy of target representations (bring-down standard — link to B-3 analysis above)
- No MAC condition (link to C-2 analysis above)
- Target covenant compliance
- Required stockholder approval obtained
- Required regulatory approvals: list all required filings; confirm adequacy
  - HSR filing threshold and waiting period [VERIFY current threshold]
  - EU Merger Regulation (Phase I/II) if applicable [VERIFY]
  - UK CMA if applicable [VERIFY]
  - CFIUS (if foreign buyer or TID US business) [VERIFY]
  - Industry-specific approvals (FCC, FERC, banking regulators, FINRA) [VERIFY as applicable]
- Officers' certificates confirming accuracy of reps
- Required third-party consents
- No injunction or legal prohibition on closing

_Common issues:_

- Required regulatory approvals listed incompletely (omits CFIUS, foreign competition filings,
  or sector-specific approvals)
- Third-party consent condition too broad (includes consents that are purely precautionary
  and unlikely to be required)
- Officers' certificate required for reps where a materiality scrape applies — potential
  conflict between the scrape and the certificate obligation

---

**E-3: Regulatory Approval Conditions and Outside Date**

_What to analyze:_

- Which regulatory approvals are conditions vs. merely covenants (important distinction:
  a covenant to obtain approval does not allow termination if approval is denied)
- Outside date (End Date): initial date; extension mechanism; which party can extend and how
  many times; consequences of extension
- "Back-stop" outside date: maximum period regardless of regulatory proceedings
- Who can terminate if outside date passes: both parties, or only the non-breaching party?

_Market standard:_ Initial outside date of 9-12 months for US deals with moderate regulatory
risk; 12-18 months for deals with high antitrust risk. Automatic 3-6 month extension if
regulatory proceedings ongoing. Buyer should not be able to extend outside date if buyer is
in breach of regulatory efforts covenant.

_Common issues:_

- Initial outside date insufficient for realistic regulatory timeline (6-month initial date
  for a deal requiring HSR Phase II review)
- No extension mechanism (deal dies automatically if regulatory approval delayed)
- Either party can terminate on outside date even if that party is in breach
- Back-stop outside date missing (regulatory proceedings can theoretically extend indefinitely)

---

#### PART F — Deal Protection Mechanisms

**F-1: No-Shop Covenant**

_What to analyze:_

- Scope: What activities are prohibited? (Soliciting, initiating, encouraging, facilitating
  acquisition proposals)
- Exceptions for board fiduciary duties: can the board respond to unsolicited proposals?
- Definition of "Acquisition Proposal": scope of competing transactions captured
- Definition of "Superior Proposal": trigger for fiduciary out (see F-2 below)

_Market standard:_ No-shop is universal in US public company mergers. Board must retain ability
to respond to unsolicited Superior Proposals under Delaware fiduciary duty law [VERIFY].
No-shop cannot prohibit board from exercising fiduciary duties under Revlon/Unocal principles.

_Common issues:_

- No-shop so broad it prohibits board from receiving or evaluating an unsolicited proposal
  (Delaware courts would not enforce this against board's fiduciary duties)
- "Acquisition Proposal" defined to include minority investments (too broad, triggering
  no-shop for ordinary business transactions)
- No carve-out for passive receipt of unsolicited inquiries

---

**F-2: Fiduciary Out and Board Recommendation Change**

_What to analyze:_

- Superior Proposal definition: Is it defined objectively? Does it require:
  - Written, bona fide proposal from a third party
  - Financial capability and no material financing contingency
  - Terms that are more favorable to target stockholders than the merger (considering all
    material terms, not just price)
  - Board determination after consultation with financial and legal advisors
- Board recommendation change procedure: Can board change its recommendation?
  - Only after providing buyer with notice (typically 4-5 business days before change)
  - Only after matching rights period expires
  - Whether a board recommendation change triggers target obligation to pay termination fee
- Intervening events: Can board change recommendation for an event unrelated to a competing
  proposal (e.g., material deterioration in buyer's business in a stock deal)?

_Market standard:_ Fiduciary out is required in any US public company merger. Board cannot
contractually waive fiduciary duties under Delaware law [VERIFY]. "Intervening event" carve-out
is common in stock deals where buyer's performance during the approval period matters to target
shareholders.

_Common issues:_

- Superior Proposal definition so narrowly drafted that no realistic offer would qualify
- No "intervening event" carve-out in a stock-for-stock deal
- Board recommendation change automatically triggers full termination fee without notice to buyer
- Matching rights period so short (1 business day) that buyer has no realistic ability to match

---

**F-3: Matching Rights**

_What to analyze:_

- Matching rights period: how many business days does buyer have to match or improve on a
  Superior Proposal?
- Last look: does buyer get a "last look" to improve its offer after the matching period?
- Target obligation: must target negotiate in good faith with buyer during matching period?
- Multiple rounds: is there a cap on the number of matching rounds, or can buyer make
  unlimited adjustments?

_Market standard:_ 3-5 business days is standard for matching rights in US deals [VERIFY].
Multiple matching rounds create competitive bid dynamics unfavorable to buyer; cap on rounds
is seller-friendly. Target must negotiate in good faith during matching period.

_Common issues:_

- No matching rights at all (buyer has no ability to retain the deal if Superior Proposal received)
- Unlimited matching rounds (target and third-party bidder effectively get to run an auction
  against buyer after signing)
- Matching right triggered only for price, not for other material terms

---

**F-4: Go-Shop Provision**

_What to analyze:_

- Is a go-shop period present? (30-60 days post-signing to actively solicit competing bids)
- Lower termination fee for bids submitted during go-shop period (typically 1-1.5% vs. 3%)
- Exclusivity: does go-shop exclude certain pre-identified potential bidders?
- Effect of go-shop on post-period no-shop (does prior go-shop contact grandfathered?)

_Market standard:_ Go-shop provisions appear in approximately 15-20% of deals [VERIFY]; more
common in PE take-privates and when board faces Revlon scrutiny with limited pre-signing market
check. Less common in strategic acquisitions where board has already conducted an auction.

---

#### PART G — Termination Rights and Fees

**G-1: Termination Rights**

_What to analyze:_

- Mutual termination rights: by agreement; on outside date; if condition permanently fails
- Buyer termination rights: target rep inaccuracy (not curable within notice period); target
  material covenant breach; target MAC
- Target termination rights: buyer rep inaccuracy; buyer material covenant breach; buyer MAC
  (if applicable); to accept Superior Proposal (with fee obligation)
- Cure rights: specify notice period and cure period for each termination trigger

_Common issues:_

- No cure period for covenant breach termination (party can terminate immediately upon
  non-material breach)
- Termination triggers asymmetric (buyer has broader termination rights than target)
- Outside date termination available to breaching party (should only be available to non-breaching
  party or both parties equally)

---

**G-2: Target Termination Fee (Breakup Fee)**

_What to analyze:_

- Fee amount: expressed as dollar amount or percentage of deal value
- Trigger events: board recommendation change; acceptance of Superior Proposal; failure to
  obtain stockholder approval in certain circumstances; termination fee on outside date
- Whether fee is sole remedy for specific trigger events
- Fee as percentage of deal value: is it within market range?

_Market standard:_ Target breakup fee typically 2-3% of deal value for US public company
mergers [VERIFY]. Lower end (1.5-2%) for large deals; higher end (3-4%) for competitive
situations. Fee must not be so high as to deter competing bids (Delaware courts scrutinize
under Unocal) [VERIFY].

_Common issues:_

- Fee above 3.5% potentially deterring superior offers (Unocal challenge risk)
- Fee triggered by board recommendation change even before matching rights process completes
  (should only be payable after matching period and final board determination)
- Fee payable even if buyer ultimately breaches (creating perverse incentive)

---

**G-3: Reverse Termination Fee (RTF)**

_What to analyze:_

- Fee amount: percentage of deal value; is it risk-calibrated to regulatory complexity?
- Trigger events: buyer failure to obtain financing; regulatory approval failure; buyer
  material breach of representations or covenants; buyer election to terminate
- Whether RTF is sole and exclusive remedy against buyer for failure to close
- "Specific performance" override: can target elect specific performance (to force closing)
  instead of accepting the RTF?
- Delaware enforceability: sophisticated parties; genuinely negotiated; not a disguised penalty

_Market standard:_ RTF range: 1.5-2% for low regulatory risk; 2-3.5% for moderate risk;
4-6.5% for high regulatory risk / expected second request (Haynes & Boone 2024) [VERIFY].
In many deals, RTF is sole remedy against buyer; however, specific performance right
is often preserved alongside RTF for cases of buyer willful breach.

_Common issues:_

- RTF too low relative to regulatory risk (seller under-compensated if deal blocked by regulators)
- RTF as sole remedy even for willful buyer breach (no deterrence against deliberate non-close)
- No specific performance right preserved (target has no mechanism to compel buyer to close)
- RTF trigger limited to financing failure but not buyer regulatory efforts failure
- RTF payment mechanics unclear (escrow, letter of credit, or unsecured obligation of buyer)

---

#### PART H — Governance and Ancillary Provisions

**H-1: Appraisal and Dissenter Rights**

_What to analyze:_

- For US mergers: DGCL Section 262 applies; market-out exception (no appraisal if consideration
  is publicly traded stock) [VERIFY]
- Disclosure of appraisal rights in proxy/circular
- Appraisal risk allocation: are appraisal claims covered by RWI or indemnification?

_Common issues:_

- Proxy does not adequately disclose appraisal procedures (Section 262 requires specific notice)
- Market-out exception assumed without confirming stock consideration is exchange-listed [VERIFY]

---

**H-2: D&O Indemnification and Tail Insurance**

_What to analyze:_

- Obligation to maintain target directors' and officers' indemnification rights (requires
  surviving entity to honor existing D&O indemnification obligations)
- D&O tail insurance: period (typically 6 years); coverage level (existing coverage or
  comparable); cost cap (typically 300% of current annual premium); obligation on buyer vs.
  target (pre-closing purchase)
- Buyer guarantee or assumption of indemnification obligations if surviving entity wound down

_Market standard:_ 6-year D&O tail is market standard for US public company mergers [VERIFY].
Cost cap of 200-300% of current annual premium is typical. Buyer should not be able to wind
down the surviving entity without assuming the indemnification obligations.

_Common issues:_

- D&O tail for only 3 years (insufficient; statute of limitations runs longer for many claims)
- Cost cap so low that adequate tail coverage cannot be obtained
- No buyer guarantee of surviving entity's indemnification obligations

---

**H-3: Employee Matters**

_What to analyze:_

- Compensation continuation period: how long must buyer maintain comparable compensation?
- Benefit plan continuation: does buyer agree to maintain existing benefit plans or provide
  comparable benefits for a specified period?
- Service credit: do target employees receive credit for prior service for vesting, eligibility,
  and benefit accrual purposes under buyer's plans?
- Change-of-control payments: are they consistent with underlying plan documents and will
  they be paid?
- Retention arrangements: are key employees retained through closing?
- WARN Act obligations (if US): mass layoff notifications; which party bears the obligation?

_Common issues:_

- Compensation/benefit continuation period too short (6 months below market; 12 months is
  more common) [VERIFY]
- No service credit for prior service (employees start from zero under buyer's plans)
- WARN Act obligations not clearly allocated between parties

---

**H-4: Governing Law, Dispute Resolution, and Jurisdiction**

_What to analyze:_

- Governing law clause: which jurisdiction's law governs the agreement?
- Dispute resolution: litigation vs. arbitration
- Jurisdiction and venue: exclusive jurisdiction clauses; jury trial waiver
- Specific performance and injunctive relief: is specific performance available as a remedy?
  (Critical for target to force closing or for parties to enforce deal protection provisions)
- Fee-shifting: which party pays attorneys' fees in a breach dispute?

_Common issues:_

- No specific performance right (prevents parties from compelling performance)
- Fee-shifting that could deter legitimate breach claims
- Jury waiver not mutual (asymmetric procedure)

---

### Step 8: Missing Provision Detection

After analyzing the provisions present, check for material provisions absent from the agreement:

| Missing Provision                                      | Classification | Recommended Action                                |
| ------------------------------------------------------ | -------------- | ------------------------------------------------- |
| No MAC definition (but MAC used as closing condition)  | RED            | Add MAC definition with standard carve-outs       |
| No fiduciary out (US public company merger)            | RED            | Required by Delaware law; add immediately         |
| No reverse termination fee (deal with regulatory risk) | RED            | Negotiate RTF or buyer specific performance right |
| No D&O tail obligation                                 | YELLOW         | Add 6-year tail at comparable coverage            |
| No WARN Act allocation                                 | YELLOW         | Clarify which party bears obligation              |
| No cure period for termination triggers                | YELLOW         | Add 20-30 day cure period for curable breaches    |
| No post-closing cooperation covenant                   | YELLOW         | Add further assurances / cooperation obligation   |
| No regulatory approval timeline (just a condition)     | YELLOW         | Add specific outside date and extension mechanism |
| No employee transition / retention covenant            | YELLOW         | Add compensation continuation commitment          |
| No specific performance right                          | YELLOW         | Add mutual specific performance right             |

**⟁ CLARIFY** — When classification depends on deal context not yet provided:

- "There is no reverse termination fee. Given the regulatory risk profile you described as
  [X], should I classify this as RED (must-add) or YELLOW (strongly recommended)?"
- "No employee benefit continuation covenant found. Are there key employee retention concerns
  for this deal? This affects whether the gap is material."

---

### Step 9: Business Impact Summary and Negotiation Strategy

Provide a business impact summary:

- **Overall risk assessment**: High-level view of the merger agreement's risk profile
- **Top 3-5 findings**: Most critical items with severity, business impact, and priority
- **Negotiation strategy**: Which issues to lead with, what to concede, how to sequence asks
- **Regulatory timeline assessment**: Is the outside date realistic? What are the risks?
- **Shareholder consideration**: Key provisions affecting stockholder vote and appraisal risk

**⟁ CLARIFY** — If deal context would materially affect negotiation strategy:

- "Can your client walk away from this deal, or is this transaction essential to the business
  strategy?" (Determines how assertive to be on must-have issues)
- "Has there been a prior round of negotiation? What did the counterparty agree to move on?"
  (Predicts which redlines will land)
- "What is the anticipated shareholder vote profile? Is there activist investor risk?"
  (Affects how tightly to draft fiduciary out and deal protection provisions)

---

### Step 10: Quality Verification

Before delivering the analysis, run the quality checks defined in the **Quality Assurance
Framework** section:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every RED-classified item, run the 3-pass Self-Interrogation. Revise if any pass
   reveals a weakness.
3. Assign a Confidence Score to each material clause analysis.
4. Verify completeness: confirm all 18 analytical categories have been addressed (present or
   flagged as missing).
5. Verify MAC carve-out and disproportionate effect analysis is consistent with applicable
   judicial standard.
6. Verify no jurisdiction-specific concepts bleed into jurisdiction-agnostic analysis sections.
7. Generate the Glass Box Audit Trail and append it to the output.

---

## Deviation Severity Classification

Classify each deviation from market standards using this three-tier system:

| Classification | Definition                                                                                                         | Required Action                                                                                                                 |
| -------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| **GREEN**      | Meets or exceeds market standard; no significant risk identified                                                   | Note for awareness only; no redline required                                                                                    |
| **YELLOW**     | Deviates from market standard; creates negotiation risk or exposure but not a deal-level risk                      | Generate specific redline with fallback position; estimate business impact of accepting vs. negotiating                         |
| **RED**        | Material deviation; creates significant legal or business risk, potential deal-breaker, or likely to be challenged | Explain the risk (cite legal basis); provide market-standard alternative language; estimate exposure; recommend escalation path |

**Borderline classification guidance:**

**⟁ CLARIFY** — For borderline RED/YELLOW items where risk tolerance is needed:

- "The MAC carve-outs omit a disproportionate effect qualifier. Under Delaware case law this
  exposes seller to industry-wide risks. Should I classify this as RED (must fix) or YELLOW
  (negotiate) based on your risk tolerance?"
- "The RTF is 1.5% for a deal with moderate antitrust risk. Market is 2-3.5% for this risk
  profile. Is this a RED (inadequate protection) or YELLOW (negotiate upward)?"

---

## Redline Format

For each YELLOW and RED deviation, generate a redline using this format:

```
### [Section Reference] — [Provision Name]

**Current Text:**
> [Exact text from the agreement, or "[Missing — provision absent]"]

**Issue:**
[One to three sentences explaining the specific risk created by the current text or absence,
citing legal authority or market standard where applicable.]

**Proposed Redline:**
> [Revised text — use strikethrough for deleted language and **bold** for added language,
or full replacement text if the provision is entirely absent]

**Fallback Position:**
[If the counterparty rejects the proposed redline, what is the minimum acceptable alternative?
What concession can be offered in exchange for the counterparty accepting this change?]

**Business Impact (Accept vs. Negotiate):**
- *If accepted as drafted*: [Quantified or qualified impact on the accepting party]
- *If negotiated to proposed position*: [What is gained]
- *Confidence*: [Definite / High / Probable / Possible / Unlikely — X.XX]
```

---

## Negotiation Priority Framework

Use these tiers to prioritize findings for negotiation:

**Tier 1 — Must-Have (Non-Negotiable Positions):**

- RED deviations where accepting the current text would create unacceptable legal or business
  risk
- Provisions where deficiency would render the transaction commercially unreasonable
- Examples: Missing fiduciary out (US public company), no reverse termination fee with high
  regulatory risk, MAC carve-outs missing disproportionate effect qualifier, sole remedy
  RTF for buyer willful breach

**Tier 2 — Strong Preferences (Fight for These):**

- YELLOW deviations where current text deviates from market standard in a material way
- Provisions where the deviation creates meaningful economic exposure
- Examples: Materiality scrape (single vs. double), matching rights period (too short),
  efforts standard cap on regulatory remedies, outside date mechanism, D&O tail period,
  employee benefit continuation period

**Tier 3 — Nice-to-Have (Concession Candidates):**

- Minor deviations from market norms that do not create material risk
- Items where accepting the counterparty's position is reasonable given the overall deal
- Examples: Governing law (non-material state vs. Delaware), notice mechanics, consent
  response timelines for minor decisions, boilerplate formatting

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise before delivery if any gate fails.

| Gate           | Rule                                                                                                                            | Fail Action                                            |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **Source**     | Every legal/market-standard claim cites a specific statute, case, study, or established principle                               | Add citation or mark "[UNVERIFIED]"                    |
| **Format**     | All citations follow consistent, recognizable format for the jurisdiction (e.g., "Del. Ch. 2018," "ABA 2023 Deal Points Study") | Fix format                                             |
| **Currency**   | Every cited provision checked for amendments, superseding case law, or updated market data                                      | Flag "[CHECK CURRENCY — confirm current as of [date]]" |
| **Domain**     | Analysis stays within the agreement's governing law scope; no jurisdiction-specific concepts stated as universal                | Remove or flag jurisdictional bleed                    |
| **Confidence** | Uncertainty explicitly stated; no finding presented with more certainty than authority supports                                 | Add confidence qualifier                               |

### Self-Interrogation for RED Items

For any item classified RED, apply this 3-pass review before delivery:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the cited
authority? Would a court or experienced counsel actually reach this conclusion? Is the legal
authority current and applicable to this jurisdiction?

**Pass 2 — Completeness**: Have all relevant statutes, case law, and deal mechanics been
considered? Are there regulatory or structural dimensions not yet addressed? Does the
analysis consider the full interaction between this provision and other provisions?

**Pass 3 — Challenge**: What is the strongest argument for accepting the current provision?
Under what circumstances might experienced counsel recommend accepting it? Does the
overall deal context or risk allocation elsewhere in the agreement change the severity?

### Confidence Scoring

| Level        | Range     | Meaning                                                               | Output Format                                       |
| ------------ | --------- | --------------------------------------------------------------------- | --------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law; clear statute or unambiguous case holding                | State without qualification                         |
| **High**     | 0.80–0.94 | Strong authority; minor interpretive questions                        | Brief caveat (e.g., "[VERIFY jurisdiction]")        |
| **Probable** | 0.60–0.79 | Good arguments; reasonable counsel could reach a different conclusion | State with reasoning and contra-indicators          |
| **Possible** | 0.40–0.59 | Material uncertainty; competing interpretations exist                 | Flag for outside counsel review; present both sides |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                                               | Do not assert; flag "[UNCERTAIN]"                   |

---

## Glass Box Audit Trail

Include this YAML block at the end of every analysis output:

```yaml
glass_box:
  skill_name: "legalcode-merger-agreement-analysis"
  analysis_date: "[date]"
  agreement_name: "[Agreement name / parties]"
  deal_type: "[Forward triangular / Reverse triangular / Direct merger / Scheme / Other]"
  governing_law: "[Jurisdiction]"
  deal_value_range: "[Under $100M / $100M-$500M / etc. / Not disclosed]"
  target_type: "[US public / UK public / Private US / Private UK / Other]"
  regulatory_risk: "[Low / Moderate / High / Not assessed]"
  user_side: "[Buyer / Target / Target shareholders / Advisor (side) / Other]"
  playbook_used: "[Playbook name] / [General market standards] / [None]"
  ancillary_documents_reviewed: "[List or 'None provided']"
  legalcode_mcp: "Connected / Not connected"
  legal_authority_file: "[/tmp/legalcode-merger-authority.md] / [Not created]"
  analytical_categories:
    total: 18
    reviewed: "[number]"
    not_applicable: "[number]"
  finding_summary:
    red: "[count]"
    yellow: "[count]"
    green: "[count]"
    missing_provisions: "[count]"
  tier_breakdown:
    tier_1_must_have: "[count]"
    tier_2_strong_preference: "[count]"
    tier_3_concession_candidate: "[count]"
  key_red_findings:
    - "[Top RED finding 1]"
    - "[Top RED finding 2]"
    - "[Top RED finding 3]"
  citations:
    verified: "[count VERIFIED via legalcode-mcp]"
    unverified: "[count marked [VERIFY]]"
  quality_gates: "PASSED / [Gate name(s) flagged]"
  self_interrogation_applied: "[count RED items reviewed through 3-pass interrogation]"
  confidence_rationale: "HIGH / MEDIUM / LOW — [brief rationale]"
  mac_invocability_risk: "HIGH / MEDIUM / LOW — [brief assessment]"
  scope_limitations:
    - "[Any excluded ancillary documents]"
    - "[Aspects requiring outside counsel judgment]"
    - "[Any provisions not analyzed due to document extraction issues]"
  reviewer: "AI-assisted — requires review by qualified M&A counsel"
```

---

## Anti-Patterns

What NOT to do when analyzing merger agreements:

1. **Conflating merger agreement analysis with purchase agreement analysis**: Merger agreements
   have unique mechanics (MAC as closing condition, fiduciary out, deal protection, appraisal
   rights) that differ fundamentally from SPAs/APAs. Do not import SPA/APA analysis patterns
   without adaptation.

2. **Citing MAC case law without jurisdiction specificity**: Delaware and UK MAC standards are
   fundamentally different. Akorn (2018) and Snow Phipps (2021) are Delaware; the Moss Bros
   (2020) Takeover Panel ruling reflects the UK's much higher standard. Do not cite across
   jurisdictions without flagging the difference.

3. **Ignoring the durational requirement for MAC**: Under Delaware law (post-Akorn), a MAC must
   show durational impact — measured in years, not months. A temporary earnings decline is
   insufficient. Do not classify short-term adverse events as MAC risks without noting this.

4. **Analyzing no-shop without considering fiduciary out**: A no-shop clause is incomplete
   without examining the fiduciary out. The no-shop scope and the fiduciary out trigger must
   be analyzed together — a narrow no-shop with a broad fiduciary out may be acceptable; a
   broad no-shop with no fiduciary out is unenforceable for US public companies.

5. **Treating RTF as always sole remedy**: Some merger agreements preserve specific performance
   alongside the RTF. The critical question is whether the target can elect specific performance
   OR accept the RTF. Analyzing only the RTF amount without examining the specific performance
   right gives an incomplete picture.

6. **Misjudging efforts standard equivalence**: Delaware courts have held "commercially
   reasonable" and "reasonable best efforts" are substantially equivalent, but "best efforts"
   imposes a higher burden. Do not conflate these without checking governing jurisdiction's case
   law.

7. **Ignoring the disproportionate effect carve-back in MAC carve-outs**: The presence of
   industry-wide carve-outs without a "disproportionate effect" carve-back exposes the seller
   to all macro risk, including events that affect the target far more severely than its peers.
   This is one of the most material MAC drafting gaps and should always be checked.

8. **Assuming ordinary course means industry norms**: Delaware courts measure "ordinary course
   of business consistent with past practice" against the target's own historical practices, NOT
   industry norms. Drafting or analyzing this provision using industry benchmarks is incorrect.

9. **Under-weighting outside date risk for regulatory deals**: Regulatory approval timelines
   routinely exceed initial deal projections. An outside date that seems adequate for a clean
   deal may be wholly inadequate if a DOJ second request is issued (extending review by 6-12
   months). Always check the outside date against a realistic worst-case regulatory timeline.

10. **Analyzing termination fees in isolation**: Termination fee analysis is meaningless without
    considering the full termination rights framework. A seller-favorable termination fee is worth
    less if the buyer has broad termination rights. A buyer-favorable RTF is more impactful if
    paired with a weak regulatory efforts obligation.

11. **Ignoring change-of-control triggers in material contracts**: Merger structure selection
    (forward vs. reverse triangular) has direct implications for which material contracts trigger
    change-of-control or anti-assignment provisions. Failing to map the merger structure against
    the target's key contracts is a material analytical gap.

12. **Treating UK and US deal protection as equivalent**: UK Takeover Code prohibits "frustrating
    action" by target boards and imposes Rule 21 restrictions on deal protection devices that are
    standard in US deals (e.g., matching rights, go-shop periods are regulated differently under
    the Code).

13. **Reviewing reps in isolation from bring-down conditions**: The practical effect of target
    reps depends entirely on the bring-down standard and whether a materiality scrape applies.
    A broad rep with a weak bring-down standard is less protective than a narrow rep with a
    strict bring-down. Always analyze the two together.

14. **Missing sandbagging implications**: Anti-sandbagging and pro-sandbagging positions affect
    whether a buyer can bring a rep warranty claim after closing for a breach it knew about
    before closing. 76% of 2023 deals are silent; silence is generally pro-seller. Note this
    allocation explicitly.

15. **Skipping D&O tail analysis**: Target directors' and officers' indemnification and D&O
    tail insurance provisions are often overlooked in favor of economic provisions. They are
    material for securing board approval and ensuring directors are not personally exposed to
    post-closing litigation arising from the transaction.

16. **One-pass analysis of complex deal protection mechanisms**: Deal protection provisions
    interact across no-shop, fiduciary out, matching rights, board recommendation change
    procedure, and termination fee triggers. Single-pass reading misses these interactions.
    Re-read the deal protection provisions as a system, not as individual clauses.

17. **Ignoring appraisal rights risk**: For US deals, appraisal rights under DGCL Section 262
    are automatic for certain stockholders and can create post-closing litigation risk and
    valuation uncertainty. Check whether the market-out exception applies and whether the
    proxy adequately discloses appraisal procedures.

18. **Insufficient attention to financing condition and RTF interplay**: In PE take-private
    mergers, the relationship between the financing condition, RTF payment obligation, and
    specific performance right is often the most negotiated provision. Analyze all three as an
    integrated system.

---

## Writing Standards

Apply these standards before delivering any output:

1. **Precision first**: Every finding must be traceable to a specific provision in the
   agreement. Cite the section number or page reference where applicable.

2. **Active voice**: "Section 7.2 does not contain a disproportionate effect qualifier" is
   better than "A disproportionate effect qualifier is not present in Section 7.2."

3. **Quantify where possible**: "The RTF of $50M represents 1.8% of the $2.75B deal value,
   below the 2-3.5% market range for moderate regulatory risk transactions" is better than
   "The RTF appears low."

4. **Hedging proportionate to uncertainty**: Do not say "this provision will be unenforceable"
   when you mean "this provision raises enforceability concerns." Use confidence scores to
   calibrate hedging language.

5. **Avoid generic M&A boilerplate**: Do not produce summaries that could apply to any merger
   agreement. Every finding must be specific to the agreement being analyzed.

6. **No jurisdiction drift**: If analyzing under Delaware law, do not import UK concepts. If
   analyzing under English law, do not assume DGCL fiduciary duty standards apply.

7. **Redlines must be lawyer-ready**: Proposed redline language should be drafting-quality —
   precise enough for a lawyer to include in a comment letter without further revision.

8. **Complete over partial**: A complete analysis of 14 out of 18 categories that clearly
   identifies the 4 not reviewed is better than a superficial pass across all 18.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for: applicable MAC/MAE case law; merger statute provisions; regulatory
  approval procedures and current filing thresholds; fiduciary duty standards; appraisal
  case law
- Save results to `/tmp/legalcode-merger-authority.md`
- Mark legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail
- Re-query for any provision where the agreement departs significantly from what was expected
  based on the governing law

**Without legalcode-mcp:**

- Proceed with web research, repository analysis, and general M&A knowledge
- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Flag any provision where unverified legal authority is load-bearing for the analysis

---

## Output Format Template

````markdown
# Merger Agreement Analysis

## Executive Summary

| Item          | Detail                                                     |
| ------------- | ---------------------------------------------------------- |
| Agreement     | [Name / Parties]                                           |
| Deal Type     | [Forward triangular / Reverse triangular / Scheme / Other] |
| Deal Value    | [Amount or range]                                          |
| Governing Law | [Jurisdiction]                                             |
| Representing  | [User's side]                                              |
| Analysis Date | [Date]                                                     |
| Overall Risk  | 🔴 HIGH / 🟡 MODERATE / 🟢 LOW                             |

**Top 3 Critical Findings:**

1. 🔴 [Most critical RED finding — one sentence]
2. 🔴 [Second most critical RED finding — one sentence]
3. 🟡 [Most significant YELLOW finding — one sentence]

---

## Critical Deal Mechanics Assessment

| #   | Mechanic                | Agreement Value | Market Standard | Status   |
| --- | ----------------------- | --------------- | --------------- | -------- |
| 1   | MAC/MAE definition      |                 |                 | 🟢/🟡/🔴 |
| 2   | Bring-down standard     |                 |                 | 🟢/🟡/🔴 |
| 3   | Materiality scrape      |                 |                 | 🟢/🟡/🔴 |
| 4   | Efforts standard        |                 |                 | 🟢/🟡/🔴 |
| 5   | No-shop / fiduciary out |                 |                 | 🟢/🟡/🔴 |
| 6   | Matching rights         |                 |                 | 🟢/🟡/🔴 |
| 7   | Target termination fee  |                 |                 | 🟢/🟡/🔴 |
| 8   | Reverse termination fee |                 |                 | 🟢/🟡/🔴 |
| 9   | Outside date            |                 |                 | 🟢/🟡/🔴 |
| 10  | Appraisal rights        |                 |                 | 🟢/🟡/🔴 |
| 11  | Regulatory approvals    |                 |                 | 🟢/🟡/🔴 |
| 12  | D&O tail                |                 |                 | 🟢/🟡/🔴 |

---

## Clause-by-Clause Analysis

### PART A — Deal Structure and Mechanics

#### A-1: Merger Structure and Surviving Entity

**Status:** [🟢 GREEN / 🟡 YELLOW / 🔴 RED] — Confidence: [Level X.XX]
[Analysis]
[Redline if YELLOW/RED]

#### A-2: Consideration Mechanics

...

### PART B — Representations and Warranties

...

### PART C — MAC/MAE Analysis

...

### PART D — Covenants

...

### PART E — Conditions to Closing

...

### PART F — Deal Protection Mechanisms

...

### PART G — Termination Rights and Fees

...

### PART H — Governance and Ancillary Provisions

...

---

## Missing Provisions

| Provision      | Classification     | Recommendation                |
| -------------- | ------------------ | ----------------------------- |
| [Missing item] | 🔴 RED / 🟡 YELLOW | [Specific recommended action] |

---

## Negotiation Strategy

### Tier 1 — Must-Have (Non-Negotiable)

1. [Item with specific ask and rationale]
2. ...

### Tier 2 — Strong Preferences

1. [Item with specific ask and fallback]
2. ...

### Tier 3 — Concession Candidates

1. [Item with trade-off rationale]
2. ...

### Recommended Sequencing

[How to present these asks: what to lead with, what to hold back, what to concede first]

---

## Stakeholder Impact Map

| Stakeholder         | Key Concerns                | Most Critical Provisions                          |
| ------------------- | --------------------------- | ------------------------------------------------- |
| Buyer               | [Buyer's perspective]       | [Key buyer-protective provisions]                 |
| Target / Board      | [Target's perspective]      | [Key target-protective provisions]                |
| Target stockholders | [Stockholder perspective]   | [Consideration, appraisal, recommendation change] |
| Financing sources   | [Lender/equity perspective] | [Conditions, covenants, financing mechanics]      |
| Regulators          | [Regulatory perspective]    | [Approval conditions, efforts covenants]          |

---

## Regulatory Timeline Assessment

[Assessment of whether outside date is realistic given the regulatory risk profile.
Specific risks: second request, Phase II, CFIUS, foreign approvals.]

---

## Glass Box Audit Trail

```yaml
[Insert populated Glass Box YAML from the Glass Box Audit Trail section]
```
````

```

---

## Localization Notes

When applying this skill to jurisdictions beyond US/UK:

**EU (German/French governing law):**
- MAC (Material Adverse Change) is not a native concept in many civil law systems; courts
  may interpret contractual MAC clauses restrictively under the principle of *clausula rebus
  sic stantibus* or force majeure [VERIFY]
- Non-compete covenants subject to EU freedom of movement restrictions; German non-compete
  requires compensation payment to be enforceable [VERIFY]
- Mandatory works council consultation may affect signing-to-closing timeline [VERIFY]

**Canada:**
- Competition Act pre-merger notification thresholds and Investment Canada Act review [VERIFY]
- Ontario and British Columbia Securities Commissions rules for public company bids [VERIFY]

**Australia:**
- FIRB (Foreign Investment Review Board) approvals for material foreign acquisitions [VERIFY]
- ASX Listing Rules for schemes of arrangement [VERIFY]

**Cross-border deals generally:**
- Always identify which jurisdiction's merger statute governs the mechanics (even in cross-
  border transactions, the target's incorporating jurisdiction typically governs the merger
  procedure)
- Always separately identify which law governs the merger agreement's contractual obligations
  (which may differ from the merger mechanics governing law)

---

## Provenance

Created by Legalcode (2026-03-21). Legal substance informed by:
- *Akorn, Inc. v. Fresenius Kabi AG*, C.A. No. 2018-0300-JTL (Del. Ch. Oct. 1, 2018) [VERIFY]
- *Snow Phipps Group, LLC v. KCAKE Acquisition, Inc.*, C.A. No. 2020-0282-KSJM (Del. Ch. Apr. 30, 2021) [VERIFY]
- Delaware General Corporation Law §§ 251-267 (merger statutes), § 262 (appraisal rights) [VERIFY]
- ABA 2023 Private Target M&A Deal Points Study [VERIFY]
- Haynes & Boone 2024 Transaction Termination Fee Study [VERIFY]
- UK City Code on Takeovers and Mergers (The Takeover Panel) [VERIFY]
- UK Companies Act 2006, Part 26A (schemes of arrangement) [VERIFY]
- HSR Act filing thresholds (current as of March 2026) [VERIFY current threshold]
- ABA Model Merger Agreement and Commentary [VERIFY]
- Takeover Panel Guidance on invoking offer conditions [VERIFY]
- Harvard Law School Forum on Corporate Governance: MAC drafting and judicial standards

Structural patterns adapted from: `legalcode-contract-review` (quality frameworks, workflow
design, Glass Box audit trail), `legalcode-purchase-agreement-review` (M&A-specific clause
analysis depth and multi-stakeholder mapping), `legalcode-proxy-statement-analysis` (public
company disclosure framework).
```
