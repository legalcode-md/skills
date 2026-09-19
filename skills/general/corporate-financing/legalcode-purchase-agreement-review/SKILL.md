---
name: legalcode-purchase-agreement-review
description: Review stock purchase agreements (SPAs) and asset purchase agreements (APAs) clause-by-clause
  against market standards or a transaction playbook.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review stock purchase agreements (SPAs) and asset purchase agreements (APAs) clause-by-clause against market standards or a transaction playbook. Analyzes representations and warranties (fundamental vs. general, materiality and knowledge qualifiers, materiality scrape), purchase price adjustment mechanisms (locked box vs. completion accounts, NWC targets, true-up), indemnification mechanics (tipping baskets, true deductibles, caps, survival periods, fraud carve-outs), MAC/MAE clauses and closing conditions, earnout provisions (metrics definition, anti-manipulation covenants, accounting standards, dispute resolution), escrow and holdback arrangements, representations and warranties insurance (RWI/W&I), non-compete and non-solicitation covenants, pre- and post-closing covenants, employee and benefits provisions, and specific indemnities (tax, environmental, pending litigation). Classifies findings GREEN/YELLOW/RED with confidence scoring, negotiation-tier prioritization, and actionable redlines with fallback positions. Use for buy-side or sell-side M&A transactions, private equity acquisitions, strategic acquisitions, carve-outs, founder exits, distressed sales, and management buyouts. Covers US, UK, and EU deal conventions with jurisdiction markers. Supports transaction-playbook-based or general-market-standard review.


# Legalcode Purchase Agreement Review

> **Disclaimer**: This skill provides a framework for AI-assisted purchase agreement review. It
> does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before use. Laws change; verify current
> applicability before relying on any provision described here. Statutory and case law references
> cited from memory carry hallucination risk — verify against authoritative sources before
> relying on them. Purchase agreement analysis requires professional judgment to assess
> materiality, deal impact, and negotiation risk. No AI tool replaces experienced M&A counsel.

---

## Purpose and Scope

This skill reviews stock purchase agreements (SPAs) and asset purchase agreements (APAs) against
an organization's transaction playbook or general M&A market standards. It identifies clause
deviations, classifies their severity, generates actionable redline suggestions, and produces
a confidence-scored, auditable analysis with negotiation strategy and business impact assessment.

**Covers:**

- Clause-by-clause analysis of SPAs and APAs across 22 analytical categories
- Critical deal mechanics assessment (purchase price, escrow, reps scope, indemnification)
- SPA vs. APA deal-type differentiation with explicit path branching
- MAC/MAE clause analysis against current Delaware and UK judicial standards
- Indemnification basket and cap analysis against current market benchmarks
- Earnout provision analysis with anti-manipulation and dispute-resolution review
- Representations and warranties insurance (RWI/W&I) interaction analysis
- GREEN/YELLOW/RED deviation classification with confidence scoring
- Redline generation with fallback positions
- Missing clause detection and gap analysis
- Negotiation strategy with Tier 1/2/3 prioritization
- Multi-stakeholder impact mapping (buyer, seller, financing sources, regulators)
- Glass Box audit trail for traceability

**Does not:**

- Draft new purchase agreements (see drafting-specific skills)
- Provide legal advice or replace qualified M&A counsel
- Perform financial or accounting analysis of deal economics
- Conduct tax due diligence (see `legalcode-ma-due-diligence-checklist`)
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers

**Complementary skills:**

- `legalcode-ma-due-diligence-checklist` — pre-signing diligence across 12 workstreams
- `legalcode-due-diligence-report` — executive-ready findings report from diligence findings
- `legalcode-contract-review` — general commercial contract review
- `legalcode-redline-generator` — automated redline production

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic. The purchase agreement's own governing law clause determines
which legal framework applies. The review identifies the governing law early and adapts the
analysis accordingly.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- Implied representations under applicable corporate statute (Delaware DGCL, UK Companies Act 2006,
  German GmbH-Gesetz / AktG, EU member-state company law) [VERIFY]
- Warranty claim limitation periods under applicable civil/commercial code vs. contractually agreed
  survival periods (civil law jurisdictions may override shorter contractual periods) [VERIFY]
- Statutory limits on indemnification exclusions (unconscionability in US, UCTA in England,
  mandatory civil code provisions in France/Germany) [VERIFY]
- Non-compete covenant enforceability (state law in the US; FTC bona fide sale exception for 25%+
  owners; UK restrained interest; EU free movement restrictions) [VERIFY]
- Escrow regulation (whether a licensed escrow agent is required; currency controls) [VERIFY]
- Foreign investment screening requirements (HSR filing thresholds, CFIUS, UK NSIA 2021 mandatory
  sectors, EU FDI Regulation, national screening regimes) [VERIFY]
- MAC/MAE judicial standards (Delaware long-term perspective; UK Commercial Court guidance 2024;
  civil law materiality thresholds) [VERIFY]
- Earn-out restrictions (whether deferred consideration is treated as consideration or employment
  income for tax purposes; accounting consolidation implications) [VERIFY]
- Anti-assignment and change-of-control restrictions in target's material contracts under
  applicable contract law [VERIFY]

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

Accept the purchase agreement in any of these formats:

- **File**: PDF, DOCX, or other document format
- **URL**: Link to the document in a VDR, CLM, or cloud storage system
- **Pasted text**: Agreement text pasted directly into the conversation

If no agreement is provided, prompt the user to supply one. Note whether ancillary documents
(disclosure schedules, exhibits, rep insurance policy) are included; their absence limits the
analysis and must be noted in the Glass Box audit trail.

---

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask the user:

1. **Your side in the transaction?**
   - Options: Buyer (Purchaser), Seller (Vendor/Target), Seller's shareholders, Advisor (for which side?), Other
   - _Why this matters_: The entire analysis flips depending on which side you represent. What protects
     a buyer (broad reps, long survival, escrow) harms a seller, and vice versa.

2. **Deal type?**
   - Options: Stock / Share Purchase, Asset Purchase, Forward Merger, Reverse Triangular Merger, Carve-out, Other
   - _Why this matters_: In a stock purchase, the buyer inherits all liabilities of the target.
     In an asset purchase, the buyer selects which assets and liabilities to acquire. The analysis
     of representations, assumed liabilities, anti-assignment clauses, and transfer taxes differs
     fundamentally between these structures.

3. **Approximate deal size / purchase price?**
   - Options: Under $10M (lower middle market), $10M–$100M (middle market), $100M–$1B (large cap),
     Over $1B (major transaction), Not disclosed
   - _Why this matters_: Market-standard basket thresholds, cap percentages, escrow durations,
     and survival periods all scale with deal size. Analysis of a $10M deal differs from a $500M deal.

4. **Representations and indemnification approach?**
   - Options: Full reps and mutual indemnification, Full reps with seller-only indemnification,
     Limited reps only (baseline), Rep insurance (RWI/W&I) in place or expected, Not yet decided
   - _Why this matters_: Full reps with mutual indemnification exposes both sides to post-closing
     claims. Seller-only indemnification is typical in sponsor-to-sponsor PE deals. Rep insurance
     fundamentally changes escrow and survival analysis.

5. **Escrow and holdback structure?**
   - Options: Indemnification escrow in place (state amount/duration if known), Holdback only (no
     formal escrow), No post-closing collateral, Escrow replaced by rep insurance
   - _Why this matters_: Without escrow or rep insurance, buyer has limited practical recourse for
     rep breaches post-closing. The escrow amount and duration must be assessed against the scope
     of representations agreed.

6. **Jurisdiction and governing law?**
   - Options: US (Delaware law / New York law / other state), England & Wales, EU member state
     (specify), Other (specify), Unclear
   - _Why this matters_: MAC/MAE judicial standards, non-compete enforceability, warranty survival
     periods, indemnification doctrine, and dispute resolution options vary materially by jurisdiction.

If the user provides partial context, proceed with reasonable defaults and **state assumptions
explicitly** at the top of the review (e.g., "Assumption: Reviewed from buyer's perspective —
correct if wrong"). Do not silently assume.

---

### Step 3: Load the Transaction Playbook

Check for an organizational transaction playbook in local settings (e.g., `ma.local.md` or
similar configuration files).

The playbook should define:

- **Standard positions**: Preferred terms for each major deal mechanic (cap %, escrow amount,
  survival periods, basket type)
- **Walk-away thresholds**: Terms that justify refusing to sign (e.g., no escrow, no fraud carve-out,
  unlimited seller indemnification)
- **Escalation triggers**: Provisions that require senior M&A counsel or board sign-off

**If no playbook is configured:**

**⟁ CLARIFY** — Inform the user that no playbook was found, and ask which approach to take:

- **Option A: Set up a playbook now** — Walk through defining the organization's standard positions
  for key deal mechanics. Takes time upfront but makes this and all future reviews more precise.
- **Option B: Proceed with general market standards** — Use widely-accepted market benchmarks (ABA
  Deal Studies, Seyfarth Middle Market M&A Survey, KPMG/WTW deal data). Faster but may not
  reflect the organization's specific risk appetite or deal history.
- **Option C: Provide positions as we go** — Start the review and ask about preferred positions
  when they materially affect classification.

If proceeding without a playbook, label the review: "Based on general M&A market standards —
not organizational playbook positions."

---

### Step 4: Identify Deal Type and Structure

Based on context gathered in Step 2, determine the primary analytical path and flag any
deal-structure issues that require immediate attention.

**[SPA-ONLY]** In a stock purchase:

- The buyer acquires all outstanding equity of the target entity
- All liabilities (known and unknown) transfer to the buyer with the entity
- Representations and warranties cover the target company's entire history
- Anti-assignment clauses in target contracts typically do NOT trigger (no transfer of contract)
- Change-of-control provisions in target contracts may trigger — flag for consent analysis

**[APA-ONLY]** In an asset purchase:

- The buyer acquires specified assets and assumes only specified liabilities
- Representations cover assets being transferred, not the entire company history
- Anti-assignment clauses in target contracts typically DO trigger — all contracts need consent
  to transfer (check for broad change-of-control definitions that also trigger in APAs)
- Bulk sales compliance may apply [JURISDICTION-SPECIFIC — VERIFY]
- Transfer taxes typically apply to each transferred asset class (real property, vehicles, etc.)
  [JURISDICTION-SPECIFIC — VERIFY]

**Transaction-structure red flags** (flag immediately if found):

- Agreement executed without disclosure schedules attached or referenced
- No definition of "Material Adverse Effect" despite closing conditions referencing it
- Reps and warranties disclaim materiality but indemnification caps are modest (scope mismatch)
- Earn-out period overlaps with non-compete duration (potential manipulation incentive)
- No anti-assignment analysis despite extensive third-party contract dependencies (common in APAs)

---

### Step 5: Gather Jurisdiction-Relevant Legal Authority

Read the agreement's governing law clause and identify the applicable jurisdiction. Use
**legalcode-mcp** to build a working legal reference file for this review.

**With legalcode-mcp connected (preferred):**

1. Search for applicable corporate/commercial statutes (e.g., Delaware DGCL for US deals, UK
   Companies Act 2006, relevant civil code)
2. Search for leading MAC/MAE case law (Akorn, Inc. v. Fresenius Kabi AG (Del. Ch. 2018 — first
   Delaware finding of MAE); IBP, Inc. v. Tyson Foods (Del. Ch. 2001) [VERIFY each citation])
3. Search for enforceability standards for non-compete covenants (state-specific for US; UK
   reasonableness test; EU competition law)
4. Search for current indemnification market benchmarks (ABA Private Target Deal Study,
   Seyfarth Middle Market M&A Survey)
5. Save results to `/tmp/legalcode-spa-review-authority.md`
6. Reference verified authority throughout the clause analysis
7. Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with general M&A market knowledge and structural analysis
- Focus on deal mechanics and commercial risk assessment rather than legal authority certainty

**⟁ CLARIFY** — If the governing law is unusual (e.g., a civil law jurisdiction not commonly
encountered in the user's practice) or if the deal involves multiple jurisdictions:

- "This transaction involves [jurisdiction/governing law]. Do you want me to flag areas where
  local counsel verification is critical, or do you have access to jurisdiction-specific
  guidance I should incorporate?"

---

### Step 6: Critical Deal Mechanics Assessment

Before the clause-by-clause analysis, assess the overall deal structure and flag any structural
imbalances. This section summarizes the key deal mechanics to provide orientation for the
detailed analysis that follows.

Assess and summarize:

| Mechanic                        | Agreed Term                                    | Market Standard                                                              | Assessment         |
| ------------------------------- | ---------------------------------------------- | ---------------------------------------------------------------------------- | ------------------ |
| **Purchase Price**              | [Fixed / Adjusting — specify]                  | Both are market-standard; adjusting more common in US                        | [GREEN/YELLOW/RED] |
| **Price Mechanism**             | [Locked box / Completion accounts / Fixed]     | Locked box common in UK/EU PE; completion accounts in US                     | [GREEN/YELLOW/RED] |
| **Escrow**                      | [% of purchase price, duration]                | 5–10% for 12–18 months (non-insured deals) [VERIFY]                          | [GREEN/YELLOW/RED] |
| **Rep Scope**                   | [Full / Limited / Baseline]                    | Full reps in most private deals; baseline in sponsor deals                   | [GREEN/YELLOW/RED] |
| **Survival — General Reps**     | [Months after closing]                         | 12–24 months typical [VERIFY]                                                | [GREEN/YELLOW/RED] |
| **Survival — Fundamental Reps** | [Months or indefinite]                         | 3–6 years or indefinite [VERIFY]                                             | [GREEN/YELLOW/RED] |
| **Indemnification Cap**         | [% of purchase price]                          | 10–20% general cap; higher/unlimited for fraud and fundamental reps [VERIFY] | [GREEN/YELLOW/RED] |
| **Basket Type**                 | [Tipping / True Deductible / Mini-Basket]      | True deductible in 60%+ of deals over $10M [VERIFY]                          | [GREEN/YELLOW/RED] |
| **Basket Amount**               | [% of purchase price]                          | 0.5–1.0% of purchase price [VERIFY]                                          | [GREEN/YELLOW/RED] |
| **Fraud Carve-out**             | [Present / Absent]                             | Market standard to include [VERIFY]                                          | [GREEN/YELLOW/RED] |
| **RWI/W&I Policy**              | [Buyer-side / Seller-side / None]              | ~75% of PE deals and 64% of strategic deals [VERIFY]                         | [GREEN/YELLOW/RED] |
| **Earn-out**                    | [Present — state amount and duration / Absent] | ~26% of private deals; 24-month median [VERIFY]                              | [GREEN/YELLOW/RED] |
| **Non-Compete**                 | [Duration, geographic scope]                   | 3–5 years; limited to applicable business [VERIFY]                           | [GREEN/YELLOW/RED] |

Flag any critical structural issues identified in this assessment before proceeding to
clause-by-clause analysis. A structural imbalance (e.g., broad reps + low cap + no escrow)
is more dangerous than any individual clause problem.

---

### Step 7: Clause-by-Clause Analysis

Analyze the agreement across 22 analytical categories organized in six parts. For each category:

1. State what the agreement says
2. State the market standard or playbook position
3. Classify the deviation: **GREEN / YELLOW / RED**
4. Assign a confidence level (Definite / High / Probable / Possible / Unlikely)
5. If YELLOW or RED: provide a specific redline and fallback position
6. Note any applicable [JURISDICTION-SPECIFIC] research points

---

## PART A — PURCHASE PRICE AND CONSIDERATION

### A-1: Purchase Price Definition and Consideration

**What to analyze:**

- [ ] Is the base purchase price clearly defined with no ambiguity in calculation?
- [ ] What forms of consideration are included: cash, stock, notes, assumed liabilities, earn-out?
- [ ] Is consideration allocation (for APA) included? Are allocations consistent with tax treatment?
- [ ] Are there any unusual deductions from purchase price at closing (cure costs, funded debt, etc.)?
- [ ] Are payment mechanics (wire instructions, timing, closing deliverables) clearly specified?

**Classification criteria:**

- **GREEN**: Price clearly defined; payment mechanics unambiguous; no unusual deductions without market-standard protections; [APA] allocation consistent with disclosed tax position
- **YELLOW**: Minor ambiguity in calculation; non-cash consideration without clear valuation mechanism; [APA] allocation absent or inconsistent
- **RED**: Price undefined or subject to unilateral seller adjustment; non-cash consideration with seller-controlled valuation; undisclosed deductions; consideration that could convert to employment income post-close (triggering additional tax and rep obligations)

[JURISDICTION-SPECIFIC] Tax treatment of consideration components (cash vs. notes vs. equity vs. earn-out vs. seller financing) varies by jurisdiction. [VERIFY] — especially for cross-border deals where withholding tax, treaty relief, and acquisition funding rules may apply.

---

### A-2: Purchase Price Adjustment Mechanism

**What to analyze:**

- [ ] Is the mechanism locked box (price fixed at historical balance sheet date) or completion accounts (post-closing true-up)?
- [ ] If locked box: Is the locked box date clearly defined? Is there a leak/permitted leak provision? Does the seller provide a no-leakage warranty?
- [ ] If completion accounts: Is the NWC target defined and agreed? Are accounting policies specified (GAAP/IFRS consistency)? Is the adjustment formula unambiguous?
- [ ] Are working capital, cash, debt, and transaction expenses each defined? Are definitions consistent with the purchase price formula?
- [ ] What is the dispute resolution mechanism for disagreements about the adjustment calculation?
- [ ] Is there a threshold below which no adjustment is made (de minimis)?
- [ ] Is the adjustment one-way (only up or only down) or two-way?
- [ ] [SPA-ONLY] Are intra-group balances, unpaid dividends, or intercompany loans included in or excluded from debt/cash definitions?

**Classification criteria:**

- **GREEN**: Mechanism clearly specified; NWC target agreed and defined; accounting policies explicit; dispute resolution is independent accountant arbitration within defined timeline
- **YELLOW**: NWC target not agreed (left to closing calculation); general GAAP reference without specificity on disputed items; dispute resolution unclear
- **RED**: No adjustment mechanism where one is appropriate; purely subjective adjustment formula; seller controls adjustment calculation without buyer right to challenge; adjustment only in seller's favor

[JURISDICTION-SPECIFIC] Locked box is more common in UK/European PE transactions; completion accounts dominate US deals. Neither is inherently superior — locked box provides price certainty; completion accounts provide economic accuracy. [VERIFY] the tax treatment of price adjustments in the governing jurisdiction.

---

### A-3: Earnout Provisions

**What to analyze (if earnout is present):**

- [ ] Is the earnout metric clearly defined (EBITDA, revenue, gross profit, unit volumes, milestone events)?
- [ ] Does the definition include example calculations illustrating how the metric applies?
- [ ] Is the accounting methodology for the earnout metric specified (consistent with historical practice)?
- [ ] Are adjustments for non-recurring items, extraordinary expenses, and acquisition costs addressed?
- [ ] What is the measurement period (minimum of 12 months; 24 months is market standard [VERIFY])?
- [ ] Is there a maximum earnout amount? Are partial payments available?
- [ ] How is the acquired business operated post-closing during the earnout period? Does buyer commit to run the business in a manner consistent with maximizing the earnout, or is there an express carve-out for buyer's integration decisions?
- [ ] What anti-manipulation protections protect the seller?
- [ ] What is the earnout dispute resolution mechanism?
- [ ] Is the earnout structure consistent with tax treatment? [JURISDICTION-SPECIFIC]
- [ ] If the earn-out is compensation-based (paid to founder who remains an employee), is there a risk of reclassification as deferred compensation rather than sale proceeds?

**Classification criteria:**

- **GREEN**: Metric clearly defined with examples; accounting methodology specified; anti-manipulation covenant present; independent accountant dispute resolution; tax treatment confirmed
- **YELLOW**: Metric defined but without example calculations or with ambiguous accounting treatment; no explicit anti-manipulation covenant; general dispute resolution
- **RED**: Metric undefined or subject to buyer's unilateral determination; no anti-manipulation protections; buyer can direct the business to minimize earn-out; no meaningful dispute resolution; earn-out term too short to demonstrate milestone (< 12 months)

[JURISDICTION-SPECIFIC] Tax treatment of earn-out payments as capital vs. income, and timing of recognition, varies by jurisdiction. [VERIFY] — especially if earn-out coincides with seller's employment with the buyer (reclassification risk).

---

## PART B — REPRESENTATIONS AND WARRANTIES

### B-1: Fundamental Representations

Fundamental representations are the highest-risk, highest-protection reps. They typically survive
indefinitely or for 6+ years and are often excluded from (or subject to a higher) indemnification cap.

**What to analyze:**

- [ ] Are the following reps included as fundamental: organization and good standing, authority and enforceability, capitalization (for SPA), title to shares (for SPA), title to assets (for APA), no broker's fee, absence of conflicts?
- [ ] Is the distinction between fundamental and general reps explicit?
- [ ] Do fundamental reps survive indefinitely or for a period materially longer than general reps?
- [ ] Is the indemnification cap higher or excluded for breaches of fundamental reps (market standard)?
- [ ] Are fundamental reps subject to any materiality qualifier that could dilute them?

**Classification criteria:**

- **GREEN**: All standard fundamental reps present; clearly labeled; unlimited (or high) survival; excluded from or subject to separate higher cap
- **YELLOW**: Some fundamental reps present; survival period not explicitly differentiated; cap not separately addressed
- **RED**: No distinction between fundamental and general reps; fundamental reps subject to same cap and survival as general reps; key fundamental reps missing (e.g., no ownership/title rep)

---

### B-2: General Representations and Warranties

**What to analyze:**

- [ ] Financial statements: Is there a rep that financial statements present fairly in accordance with GAAP/IFRS? Is the period covered (prior 3 fiscal years + most recent interim period market standard)?
- [ ] No undisclosed liabilities: Is there a rep on absence of liabilities not reflected in financial statements? What is the knowledge qualifier and materiality threshold?
- [ ] Material contracts: Are material contracts identified, valid, in full force, and no breach or threatened termination? What threshold defines "material"?
- [ ] Compliance with laws: Is there a rep covering compliance with all applicable laws? How far back does it reach? Is there a knowledge qualifier?
- [ ] Intellectual property: Does the seller rep that the target owns or has rights to all IP necessary to operate the business? Is there a freedom-to-operate rep?
- [ ] Taxes: Are all returns filed, all taxes paid, no pending audits beyond what is disclosed? Any statute of limitations extensions?
- [ ] Litigation: Are there no pending or threatened actions not disclosed? Does the rep cover regulatory proceedings?
- [ ] Environmental: Are there no environmental violations or liabilities not disclosed? [May be standalone — see C-3]
- [ ] Employees and benefits: Are employee matters (no labor disputes, no violations, accurate compensation) accurately represented?
- [ ] Related-party transactions: Are all transactions with affiliates disclosed and at arm's length?
- [ ] Data privacy and cybersecurity: Has the company complied with applicable data protection laws? No unreported breaches?

**Classification criteria:**

- **GREEN**: All material rep categories present; limited materiality qualifiers (preferably materiality-scraper included); knowledge qualifiers defined (including constructive knowledge for key executives)
- **YELLOW**: Some material rep categories missing or narrowed by unqualified "to seller's knowledge" without definition of who has knowledge; no data privacy or cybersecurity reps in a technology business
- **RED**: Major rep categories absent; reps qualified by "actual knowledge of [specific individual only]" without objective reasonableness standard; financial statements rep limited to one year; no compliance rep; no IP rep for an IP-intensive business

---

### B-3: Disclosure Schedules

Disclosure schedules are how sellers take exceptions to their representations. They are as
important as the representations themselves.

**What to analyze:**

- [ ] Are disclosure schedules attached (not merely referenced as TBD)?
- [ ] Are schedule cross-references consistent with the representations they qualify?
- [ ] Are the disclosures sufficiently specific to put the buyer on notice of the actual issue?
- [ ] Is there a general disclosure cross-reference (allowing disclosures in one schedule to qualify all reps), or are disclosures targeted (only qualify the specific rep they're scheduled to)?
- [ ] Are any disclosures qualified so broadly as to negate the underlying representation (e.g., "any matter known to buyer through its own investigation")?
- [ ] Is there a bring-down schedule for the closing date (updating for changes since signing)?

**Classification criteria:**

- **GREEN**: Schedules attached and complete; targeted cross-references; specific disclosures; no general disclosure carve-out negating reps; bring-down mechanism addressed
- **YELLOW**: Some schedules incomplete; general disclosure cross-reference limiting buyer's reliance; minor inconsistencies between reps and schedule references
- **RED**: Schedules not attached (executing without schedules); overly broad general disclosure (e.g., "all matters disclosed in data room" qualifies all reps); catch-all disclosure language negating the value of reps

---

### B-4: Materiality Qualifiers and Materiality Scrape

**What to analyze:**

- [ ] What materiality qualifier is used across the representations ("material," "Material Adverse Effect," "in all material respects," numeric threshold)?
- [ ] Is "Material Adverse Effect" or "Material Adverse Change" defined?
- [ ] Is there a materiality scrape for indemnification purposes — i.e., for purposes of calculating damages and determining basket satisfaction, are materiality qualifiers in the reps disregarded?
- [ ] If there is no materiality scrape, what is the practical effect on the buyer's ability to recover for rep breaches that are real but below the materiality threshold in each individual rep?

**Classification criteria:**

- **GREEN**: Materiality defined; materiality scrape present for indemnification (this is market standard in the US for buyer-favorable deals [VERIFY]); scrape is clearly worded
- **YELLOW**: Materiality used widely in reps without definition; no explicit scrape but damages calculation doesn't double-count materiality thresholds
- **RED**: No materiality definition; overlapping materiality qualifiers (both in reps and in basket/indemnification calculation) creating a double-materiality threshold that practically eliminates recovery; no scrape with broad materiality qualifiers in all reps

[JURISDICTION-SPECIFIC] Materiality scrapes are common in US M&A but less standard in some UK/EU deals. [VERIFY] and confirm with jurisdiction-specific counsel whether a scrape is market-standard in the applicable jurisdiction.

---

## PART C — INDEMNIFICATION FRAMEWORK

### C-1: Indemnification Scope and Structure

**What to analyze:**

- [ ] Who indemnifies whom? Is indemnification mutual, or is it seller-only?
- [ ] What triggers indemnification: rep breach only, or also covenant breach and specific indemnities?
- [ ] Is there an exclusive remedy clause (making indemnification the sole remedy for breach of reps)?
- [ ] Does the exclusive remedy clause contain a fraud carve-out? An intentional misrepresentation carve-out?
- [ ] Are specific indemnities (tax, environmental, pending litigation) separate from general indemnification?
- [ ] Is there a duty to mitigate post-closing losses before claiming indemnification?

**Classification criteria:**

- **GREEN**: Mutual indemnification (or seller-only with clear rationale); fraud carve-out present; exclusive remedy clause; specific indemnities addressed separately; duty to mitigate present
- **YELLOW**: Seller-only indemnification without clear rationale; no explicit exclusive remedy; unclear interaction between rep indemnification and specific indemnities
- **RED**: No fraud carve-out from limitations; exclusive remedy clause cuts off equitable remedies (including specific performance for pre-closing covenants) [VERIFY equitable remedy availability by jurisdiction]; buyer has unlimited indemnification obligations to seller without corresponding seller exposure

---

### C-2: Survival Periods

**What to analyze:**

- [ ] Do the representations survive closing? For how long?
- [ ] Are fundamental reps (title, authority, capitalization, broker's fee) subject to a longer or indefinite survival period?
- [ ] Are tax reps subject to the applicable tax statute of limitations plus a reasonable buffer?
- [ ] What is the survival period for environmental reps (often longer given latent risks)?
- [ ] Are covenants subject to a separate survival analysis?
- [ ] Does the survival period begin on the signing date or the closing date?

**Market standards (subject to [VERIFY]):**

- General reps: 12–24 months post-closing in the US; 12–18 months in many UK PE deals
- Fundamental reps: 3–6 years or indefinite in the US; statutory limitation period + buffer in the UK
- Tax reps: Statute of limitations + 6–12 months in the US; applicable tax limitation period in the UK/EU
- Environmental reps: 3–5 years in many deals; indefinite if known contamination disclosed

**Classification criteria:**

- **GREEN**: Survival periods explicitly defined, differentiated by rep type, and consistent with market standards for the deal size and jurisdiction
- **YELLOW**: Uniform survival period for all reps; short survival for tax or environmental reps; survival measured from signing rather than closing
- **RED**: Reps expire at closing with no post-closing recourse; survival shorter than statute of limitations for key claim types; no differentiation between fundamental and general reps

---

### C-3: Baskets and Deductibles

**What to analyze:**

- [ ] What type of basket is used: tipping basket (all losses recoverable once threshold is met) or true deductible (only losses above threshold are recoverable)?
- [ ] What is the basket amount (as a percentage of purchase price or fixed dollar amount)?
- [ ] Is there a mini-basket (per-claim threshold below which individual claims don't count toward the basket)?
- [ ] Are fundamental rep claims, fraud claims, and specific indemnities excluded from the basket?
- [ ] Is the basket consistent with the deal size (too large a basket can effectively negate recovery)?

**Market standards (subject to [VERIFY]):**

- Tipping basket: More buyer-friendly; historically prevalent in US deals
- True deductible: More seller-friendly; prevalent in >60% of US deals over $10M [VERIFY]; dominant in UK/EU PE
- Basket amount: 0.5–1.0% of purchase price in most US private deals [VERIFY]
- Mini-basket (per-claim): USD 25K–100K in many middle-market deals [VERIFY]

**Classification criteria:**

- **GREEN**: Basket type explicitly stated and agreed; basket amount within market range for deal size; fundamental reps, fraud, and specific indemnities excluded from basket
- **YELLOW**: Basket type not explicitly labeled (ambiguity between tipping vs. deductible); basket amount at high end of market range; mini-basket at restrictive level
- **RED**: Basket amount exceeds 2% of purchase price (for non-insured deals); basket applies to fundamental reps and fraud (limits buyer recovery on most material breaches); ambiguous basket mechanics that seller could interpret to block recovery

---

### C-4: Indemnification Caps

**What to analyze:**

- [ ] Is there a general indemnification cap (maximum total liability for rep breaches)?
- [ ] What is the cap amount (as a percentage of purchase price)?
- [ ] Are fundamental reps, fraud, and specific indemnities excluded from or subject to a higher separate cap?
- [ ] Is there a "sandbagging" provision (allowing or prohibiting recovery for known pre-signing rep breaches)?
- [ ] If rep insurance is in place, does the cap align with the policy retention and coverage limits?

**Market standards (subject to [VERIFY]):**

- General cap: 10–20% of purchase price for middle market private deals [VERIFY]
- Fundamental reps: Often at 100% of purchase price or uncapped [VERIFY]
- Fraud: Uncapped in virtually all deals [VERIFY]
- Sandbagging: Pro-sandbagging is buyer-friendly; anti-sandbagging is seller-friendly; varies by jurisdiction and negotiation [VERIFY]

**Classification criteria:**

- **GREEN**: Cap clearly defined and within market range; fundamental reps and fraud excluded from general cap or subject to separate higher cap; sandbagging approach specified; rep insurance interaction addressed
- **YELLOW**: Cap at upper end of market range; no explicit treatment of fundamental reps vs. general cap; sandbagging not addressed (silence defaults to jurisdiction-specific rule [VERIFY])
- **RED**: General cap applies to fraud (leaves buyer practically unprotected); cap below 10% for a non-insured deal without specific rationale; cap denominated in a way that creates ambiguity (e.g., "10% of adjusted purchase price" without defining adjusted purchase price)

[JURISDICTION-SPECIFIC] Anti-sandbagging provisions may be unenforceable in some US states where waiver doctrine prevents sellers from using buyer's pre-signing knowledge to bar rep claims. [VERIFY] — especially in Delaware, New York, and California. UK courts have generally enforced anti-sandbagging clauses. [VERIFY]

---

### C-5: Escrow and Holdback Mechanics

**What to analyze:**

- [ ] What percentage of the purchase price is held in escrow or withheld?
- [ ] What is the escrow duration?
- [ ] Who is the escrow agent? Is the escrow agreement attached?
- [ ] What events trigger release of escrow (expiry of survival period, resolution of pending claims)?
- [ ] Can the buyer make claims against escrow during the escrow period? What is the claims procedure?
- [ ] If a holdback is used instead of escrow, how is it documented and protected?
- [ ] Is there a separate escrow for purchase price adjustment (separate from indemnification escrow)?
- [ ] Does the escrow amount align with the general indemnification cap?

**Market standards (subject to [VERIFY]):**

- Escrow amount: 5–10% of purchase price in non-insured deals [VERIFY]
- Escrow duration: 12–18 months for non-insured deals; may reduce for rep-insured deals [VERIFY]
- Rep-insured deals: Escrow may be replaced by policy deductible/retention (0.5–0.8% of deal value) [VERIFY]

**Classification criteria:**

- **GREEN**: Escrow amount and duration within market range; escrow agreement attached and reviewed; claims procedure clear; separate escrow accounts for purchase price adjustment vs. indemnification; post-closing release mechanics clearly defined
- **YELLOW**: Escrow amount within market range but duration short; escrow agreement not attached; holdback without formal escrow documentation; claims procedure unclear
- **RED**: No escrow and no rep insurance (buyer has no collateral for post-closing rep breach claims); escrow amount below 5% without rep insurance; no release mechanism or one-sided release favoring seller

---

### C-6: Representations and Warranties Insurance (RWI/W&I)

**What to analyze:**

- [ ] Is a rep insurance policy in place or contemplated?
- [ ] Is it a buy-side or sell-side policy? (Buy-side is more protective for buyers)
- [ ] Does the policy cover all material reps, or only specific reps?
- [ ] What is the policy deductible/retention? Does it align with the basket in the purchase agreement?
- [ ] Does the agreement include a "no-recourse" provision against seller for rep breaches covered by the policy?
- [ ] Does the policy include a fraud exclusion (allowing recovery against seller for seller fraud)?
- [ ] What are the policy limits and coverage period? Do they exceed the general rep survival period?
- [ ] Has underwriting diligence been completed? Are there any pending exclusions?

**Market standards (subject to [VERIFY]):**

- Policy type: Buy-side (most common — buyer claims directly against insurer) [VERIFY]
- Coverage period: 3 years for general reps; 6 years for fundamental reps [VERIFY]
- Premium: 2–2.5% of policy limits (2024) [VERIFY]
- Retention: 0.5–0.8% of deal value, reducing to 0.3–0.5% after 12 months [VERIFY]

**Classification criteria:**

- **GREEN**: Buy-side policy in place; deductible aligns with purchase agreement basket; fraud carve-out preserved against seller; coverage period exceeds rep survival period; no-recourse provision in agreement
- **YELLOW**: Seller-side policy (less buyer-protective); pending exclusions not yet resolved; no explicit interaction analysis between policy and purchase agreement provisions
- **RED**: Policy purports to cover seller fraud but has fraud exclusion (creates gap); policy deductible misaligned with basket creating double-materiality gap; no-recourse provision in agreement that eliminates buyer recovery even for seller fraud that is uninsured

---

## PART D — CLOSING MECHANICS

### D-1: Material Adverse Effect / Material Adverse Change Clause

The MAC/MAE clause allows a buyer to refuse to close (and/or terminate the agreement) if the
target experiences a material adverse effect between signing and closing. Under Delaware law,
this is an extraordinary remedy — courts have found MAE rarely before _Akorn v. Fresenius_
(2018), which upheld termination for the first time in Delaware [VERIFY]. The standard requires a
durationally significant change to long-term earnings power, not a short-term disruption.

**What to analyze:**

- [ ] Is MAE/MAC defined? How broadly or narrowly?
- [ ] What carve-outs exclude effects from the MAE definition?
- [ ] Are the carve-outs weighted back against the target (i.e., do they apply only if the effect
      does not disproportionately affect the target compared to industry peers)?
- [ ] Does the MAC definition include specific items (litigation, regulatory actions, loss of key
      contract) that give buyer a clearer termination right?
- [ ] Is the MAC definition used only in closing conditions, or also in representations?
- [ ] If MAC is also a rep, does that create a double-trigger (seller must both cure and bring-down
      the MAC rep for closing to proceed)?

**Standard MAC carve-outs (each should be reviewed for proportionality):**

1. General economic or financial market conditions
2. Industry-wide conditions affecting the target's industry
3. Changes in applicable law or accounting standards (GAAP/IFRS)
4. Acts of terrorism, hostilities, national disasters, pandemics
5. Changes in the target's stock price (but NOT changes in underlying business)
6. Actions taken at buyer's express written direction
7. Announcement or pendency of the transaction itself

**Classification criteria:**

- **GREEN**: MAE defined with balanced carve-outs; proportionality (disproportionate impact) qualifier preserves buyer's right when the target is worse off than peers; MAC used consistently across closing conditions and reps
- **YELLOW**: MAE carve-outs broad but without proportionality qualifier; MAE definition absent from reps but present in closing conditions; industry-wide carve-out without limitation to general conditions
- **RED**: MAE defined so broadly (or carve-outs so extensive) that it provides no practical closing protection; no MAE definition despite references to it in closing conditions; MAC carve-out explicitly excludes regulatory failures (critical for regulated targets); MAC definition inconsistent with the industry's known risk factors

[JURISDICTION-SPECIFIC] Delaware courts apply a long-term perspective (years, not months) to MAE analysis. The 2018 _Akorn v. Fresenius_ decision (upheld on appeal) found an MAE based on dramatic multi-quarter earnings collapse plus undisclosed regulatory violations. [VERIFY citation and current state of Delaware MAC law — subsequent cases may have refined this standard.] UK Commercial Court provided guidance on MAC clauses in 2024. [VERIFY]

---

### D-2: Closing Conditions

**What to analyze:**

- [ ] What are the mutual conditions to closing (apply to both parties)?
  - No injunction or legal prohibition on closing
  - Regulatory approvals obtained (HSR clearance, CFIUS approval, EU merger control, etc.)
  - Material governmental authorizations
- [ ] What are buyer-only conditions?
  - Seller reps true and correct (at what standard: in all respects, in all material respects, without giving effect to materiality qualifiers)?
  - Seller has performed covenants in all material respects
  - No MAC since signing
  - Bring-down certificate
  - Delivery of closing documents (disclosure schedule updates, officer certificates, etc.)
- [ ] What are seller-only conditions?
  - Buyer reps true and correct
  - Buyer has performed covenants
  - Buyer has paid purchase price / obtained financing
- [ ] What is the "outside date" (the deadline for closing, after which either party may terminate)?
- [ ] What happens if closing conditions cannot be satisfied?

**Classification criteria:**

- **GREEN**: Closing conditions balanced and clearly defined; regulatory approvals identified and timeline tracked; bring-down standard is "accurate in all material respects" (not "accurate in all respects" which creates no materiality threshold); outside date provides adequate time for regulatory clearance; termination rights and fees clearly specified
- **YELLOW**: Closing conditions favor one party; bring-down standard is stricter than "in all material respects" for some reps; outside date is ambiguous; no clear termination procedure upon failure
- **RED**: Buyer conditions make closing practically discretionary (e.g., "satisfactory" bring-down without objective standard); no regulatory approval condition where major filings are anticipated; outside date precedes regulatory clearance timeline; MAE condition absent from buyer's closing conditions

[JURISDICTION-SPECIFIC] HSR filing thresholds (US), CMA/NSIA (UK), EUMR (EU), and national FDI screening regimes all have different timelines and review standards. [VERIFY] current filing thresholds for the jurisdiction.

---

### D-3: Pre-Closing Covenants

**What to analyze:**

- [ ] Is there an obligation for the target to operate in the ordinary course between signing and closing?
- [ ] Are negative covenants (prohibited actions between signing and closing) listed?
  - Common negatives: no material acquisitions, no extraordinary dividends/distributions, no disposal of material assets, no assumption of material debt, no new key employee agreements without buyer consent, no change in accounting practices
- [ ] What are the affirmative covenants (what must the seller/target do before closing)?
  - Common affirmatives: maintain insurance, preserve business relationships, cooperate with regulatory filings, provide access to books and records for further diligence
- [ ] What is the standard for consent to take restricted actions (buyer's consent "not to be unreasonably withheld, conditioned, or delayed" vs. pure consent)?
- [ ] If buyer consent is required, what are the consequences of buyer withholding consent unreasonably?
- [ ] Are there COVID/pandemic-related carve-outs or force majeure exceptions to ordinary course covenants?

**Classification criteria:**

- **GREEN**: Comprehensive ordinary course covenant; clear negative and affirmative covenant lists; consent standard is "not to be unreasonably withheld"; breach of covenant creates closing condition failure right; adequate notice and cooperation requirements
- **YELLOW**: Covenant list incomplete; consent standard is pure buyer discretion for all restricted actions; no mechanism to challenge unreasonable withholding; affirmative covenants absent
- **RED**: No ordinary course covenant; negative covenants allow major actions that could fundamentally change the business before closing; consent required from buyer for routine operations (gives buyer de facto management control which may raise regulatory issues); no access covenant for pre-closing diligence updates

---

## PART E — POST-CLOSING PROVISIONS

### E-1: Post-Closing Non-Compete and Non-Solicitation Covenants

**What to analyze:**

- [ ] Are non-compete covenants present? Who are the restricted parties (seller only, shareholders, key employees)?
- [ ] What is the restricted period? What is the restricted territory? What is the restricted activity (specific business or broader)?
- [ ] Are non-solicitation covenants present (prohibiting solicitation of employees and customers)?
- [ ] Are non-disparagement covenants present?
- [ ] Is there a "bona fide sale" exception for the US FTC context? (Critical: FTC rule struck down as of September 2025 [VERIFY], but state law restrictions remain and the bona fide sale exception remains important) [VERIFY current state of US non-compete law]
- [ ] Are the covenants limited to the business actually sold (not the entire industry)?
- [ ] Is there adequate consideration for the post-closing restrictions?
- [ ] Are remedies for breach of covenants specified (injunctive relief, liquidated damages, specific performance)?

**Market standards (subject to [VERIFY]):**

- US: Non-competes valid in bona fide sale context for substantial sellers (25%+ ownership); duration 3–5 years; geographic scope limited to actual business territory; FTC rule dismissed September 2025 — state law governs [VERIFY current state law restrictions]
- UK: Reasonableness test (duration typically 2–3 years for seller covenants; activity limited to actual business sold) [VERIFY]
- EU: Covenant directly related to transaction, limited in time and territory; competition law interaction [VERIFY]

**Classification criteria:**

- **GREEN**: Non-compete duration and territory reasonably proportionate to business sold; restricted parties clearly identified; non-solicitation appropriately scoped (targeted, not "no hire" for general recruitment); remedies including injunctive relief specified; jurisdiction-specific enforceability confirmed
- **YELLOW**: Duration on high end of range; territory broader than business footprint; restrictions apply to parties beyond actual sellers of the business (e.g., employees who receive no proceeds); no consideration analysis
- **RED**: Duration exceeds 5 years in US context or market norms in applicable jurisdiction; restriction covers business activities not related to what was sold; broad "no hire" prohibition that covers responses to general job postings (unenforceable in many jurisdictions); no jurisdiction-specific analysis; key sellers excluded from covenants

[JURISDICTION-SPECIFIC] Non-compete enforceability is among the most jurisdiction-specific areas of M&A law. [VERIFY] state law (US), Employment Act and Restrictive Practices Act (UK), and national competition law (EU) for the specific governing jurisdiction. German law has specific AGB requirements for non-competes [VERIFY]. Post-2025, US federal law does not ban M&A non-competes for substantial sellers, but some states have independent restrictions [VERIFY].

---

### E-2: Employee and Benefits Provisions

**What to analyze:**

- [ ] Are key employees identified? Are retention arrangements in place?
- [ ] Does the purchase agreement address treatment of change-of-control payments and accelerated vesting triggered by the transaction?
- [ ] Are there WARN Act obligations (US federal/state) or TUPE transfer obligations (UK)?
- [ ] Are employee benefit plans (including pension, health, equity) addressed post-closing?
- [ ] Is there a commitment to maintain compensation at closing levels for a transition period?
- [ ] Are union or collective bargaining agreements identified? Are works council consultation obligations fulfilled?
- [ ] [APA-ONLY] Which employees transfer? Is there a specific hire offer obligation?

**Classification criteria:**

- **GREEN**: Key employees identified; retention arrangements documented; WARN/TUPE obligations addressed; benefit continuation for transition period; works council consultation completed; all change-of-control obligations disclosed and addressed
- **YELLOW**: Key employees not all identified; WARN/TUPE analysis present but incomplete; benefit continuation undefined; no works council consultation analysis
- **RED**: No WARN Act analysis for a transaction that triggers workforce changes [VERIFY threshold for specific jurisdiction]; no TUPE analysis for UK acquisition with employee transfers; undisclosed change-of-control payments that increase purchase price or create hidden liabilities for buyer; no key employee retention in a business where value is people-dependent

[JURISDICTION-SPECIFIC] WARN Act (US — federal and state) thresholds and timing requirements vary [VERIFY]. TUPE (UK) mandates automatic employee transfer and consultation [VERIFY]. EU Works Council Directive (Directive 2009/38/EC) requires consultation for pan-EU businesses [VERIFY]. German co-determination law may require supervisory board consent [VERIFY].

---

### E-3: Specific Indemnities

Specific indemnities cover known or anticipated liabilities identified during diligence that are
excluded from the general rep and indemnification framework.

**What to analyze:**

- [ ] Is there a tax indemnity covering pre-closing tax periods? Is it consistent with tax rep survival?
- [ ] Is there an environmental indemnity for known contamination or environmental non-compliance?
- [ ] Are there indemnities for pending or threatened litigation identified in diligence?
- [ ] Are there indemnities for product liability, recall, or warranty claims arising pre-closing?
- [ ] Are specific indemnities subject to the general cap and basket, or do they stand alone?
- [ ] What is the survival period for specific indemnities (often longer than general reps)?
- [ ] Are specific indemnities from the seller only, or mutual?

**Classification criteria:**

- **GREEN**: All known material diligence risks covered by specific indemnity; specific indemnities carved out from general cap and basket; survival periods appropriate to the specific risk (environmental often indefinite); claims procedure consistent with general indemnification mechanics
- **YELLOW**: Some identified risks covered; specific indemnities subject to general cap limiting recovery; limited survival period for long-tail risks
- **RED**: Known material risks not covered by specific indemnity and not adequately covered by general reps/indemnification; specific indemnities from seller capped below estimated exposure; no environmental indemnity for a business with known environmental issues

---

## PART F — GOVERNING TERMS

### F-1: Governing Law and Dispute Resolution

**What to analyze:**

- [ ] What is the governing law? Is it well-established for M&A transactions (Delaware law, New York law, English law are preferred)?
- [ ] What is the dispute resolution mechanism: litigation in stated courts, or arbitration?
- [ ] If arbitration: what rules (ICC, AAA, LCIA)? What seat? Number of arbitrators? Is the award enforceable?
- [ ] Is specific performance available as a remedy (critical for buyer to compel closing if seller attempts to walk away)?
- [ ] Is injunctive relief available for covenant breaches (non-compete, interim covenants)?
- [ ] Is there a waiver of jury trial? [Effective only in some US jurisdictions — VERIFY]
- [ ] Is there a prevailing party attorney's fees provision?

**Classification criteria:**

- **GREEN**: Well-established governing law; specific performance explicitly available; injunctive relief preserved; arbitration with clear rules and enforceable seat; no unconscionable dispute resolution restriction
- **YELLOW**: Governing law less familiar for M&A but not problematic; specific performance available but subject to unclear conditions; arbitration rules specified but seat or number of arbitrators unclear
- **RED**: Governing law creates material uncertainty (e.g., jurisdiction with no M&A precedent or recent political disruption to rule of law); specific performance waived or not available; exclusive arbitration waives right to injunctive relief for covenant breaches; dispute resolution in forum that is impractical or inaccessible

---

### F-2: [APA-ONLY] Assumed and Excluded Liabilities

**What to analyze:**

- [ ] Is the assumed liabilities list specific and exhaustive?
- [ ] Is the excluded liabilities list specific and exhaustive?
- [ ] Are there any ambiguous liabilities that could fall into neither category?
- [ ] Are pre-closing liabilities (including tort claims, employment claims, environmental claims) expressly excluded?
- [ ] Does the agreement include a bulk sales compliance provision? [JURISDICTION-SPECIFIC]
- [ ] Are successor liability risks addressed? (Buyer inheriting pre-closing liabilities by operation of law in some jurisdictions [VERIFY])
- [ ] If there are unknown liabilities, has buyer negotiated a rep or indemnity covering undisclosed pre-closing liabilities?

**Classification criteria:**

- **GREEN**: Assumed liabilities narrowly and specifically listed; excluded liabilities broadly and specifically listed; catch-all excluded liabilities provision covering any unlisted pre-closing liability; successor liability analysis confirms protection; bulk sales compliance addressed
- **YELLOW**: Assumed liabilities list complete but excluded liabilities list incomplete; no catch-all excluded liabilities provision; bulk sales compliance not addressed (risk in applicable jurisdictions)
- **RED**: Assumed liabilities defined so broadly as to include all existing liabilities without qualification (equivalent to stock purchase without the tax benefits); successor liability risk not analyzed; no protection for unknown pre-closing liabilities

[JURISDICTION-SPECIFIC] Successor liability by operation of law (product liability successor doctrine, environmental successor liability, de facto merger) varies significantly by US state. [VERIFY] applicable law. UK generally does not have broad successor liability doctrine except for environmental contamination. [VERIFY]

---

### F-3: [APA-ONLY] Transferred Assets and Anti-Assignment Analysis

**What to analyze:**

- [ ] Is the transferred assets schedule complete and consistent with the business being acquired?
- [ ] Are all intellectual property assets (registered and unregistered) identified for transfer?
- [ ] Are there any material contracts that cannot be assigned without third-party consent?
- [ ] Has buyer analyzed all material contracts for anti-assignment and change-of-control provisions?
- [ ] For contracts requiring consent, is there a closing condition requiring such consents, or a mechanism for operating without them (sub-contracting, power of attorney)?
- [ ] Are government contracts (which typically require novation rather than assignment) identified?
- [ ] Are software licenses (which typically have anti-assignment clauses) identified?

**Classification criteria:**

- **GREEN**: Assets schedule complete and reviewed; anti-assignment analysis completed for all material contracts; closing condition for critical consents; mechanism for operating without consent where closing condition is not used; government contract novation process initiated
- **YELLOW**: Assets schedule substantially complete but some omissions; anti-assignment analysis partial; consent process not initiated for all material contracts; no closing condition backup for critical consents
- **RED**: Assets schedule incomplete or by reference to "all assets used in the business" without enumeration; no anti-assignment analysis; closing without required consents (breach of target contracts); no mechanism to operate key contracts pending consent; software licenses transferred without licensor consent (EULA breach)

---

## Severity Classification

| Classification | Meaning                                                                                                                     | Action                                                                    |
| -------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **GREEN**      | Clause meets or exceeds market standard; no material negotiation required                                                   | Note for awareness; may approve as-is                                     |
| **YELLOW**     | Clause deviates from market standard in a negotiable way; negotiable redline available                                      | Prepare specific redline with fallback; flag in Tier 2 or Tier 3 priority |
| **RED**        | Clause represents a material deal risk, an unusual departure from accepted norms, or a potential deal-breaker if unresolved | Escalate; prepare redline; consider deal impact; Tier 1 priority          |

**Missing clause severity:**

- **GREEN (not needed)**: Clause type not applicable to this deal structure
- **YELLOW (should be added)**: Market-standard clause absent but addressable with negotiation
- **RED (must be added)**: Material protection clause absent; creates significant unprotected risk

---

## Redline Format

For each YELLOW or RED finding, generate a redline in this format:

```
**Finding ID**: [FR-XXX]
**Clause**: [Agreement section reference]
**Classification**: [YELLOW / RED]
**Confidence**: [Definite / High / Probable / Possible / Unlikely] [0.00–1.00]

**Agreement says**: [Summary or direct quote of current language]
**Market standard**: [What this clause typically provides in a comparable deal]
**Deviation**: [The specific gap or problem]
**Business impact**: [Practical consequence if this language stands]
**Legal basis**: [Applicable statute, case, market data — or [VERIFY] if not confirmed]

**Proposed redline**:
> [Specific proposed language or the key change required]

**Fallback position**:
> [Minimum acceptable position if primary redline is rejected]

**Priority**: [Tier 1 / Tier 2 / Tier 3]
```

---

## Negotiation Priority Framework

Organize all YELLOW and RED findings into three tiers based on deal impact:

### Tier 1 — Must-Haves (Deal Conditions)

Issues where your side cannot sign or close without resolution. Raise these first and hold firm:

- No fraud carve-out from indemnification limitations
- No escrow or rep insurance (no post-closing recourse)
- Reps expire at closing with no post-closing survival
- No MAC/MAE clause or effectively unusable MAC definition
- Fundamental reps subject to same short survival as general reps
- No specific indemnity for a known material pre-closing liability
- Anti-assignment analysis not completed for critical business contracts
- Closing conditions providing buyer with no meaningful protection if reps fail

### Tier 2 — Strong Preferences (Material Negotiation Points)

Issues that materially affect risk profile but are negotiable:

- Basket type and amount (tipping vs. true deductible; basket % above market range)
- Cap amount (below or above market range for deal size)
- Survival period adjustments (too short for tax or environmental)
- Materiality scrape absent from indemnification calculation
- Locked box vs. completion accounts mechanism adjustment
- Earn-out anti-manipulation covenant absent or insufficient
- Non-compete duration or territory overbroad
- Disclosure schedule completeness

### Tier 3 — Preferred Positions (Concession Candidates)

Issues that improve your position but can be conceded strategically:

- Governing law preference (if alternative is acceptable)
- Dispute resolution venue (preferred arbitration vs. acceptable court)
- Notice periods and mechanics
- Choice of escrow agent
- Minor asymmetries in mutual covenant obligations

**Strategy**: Lead with Tier 1 items. Trade Tier 3 concessions to secure Tier 2 wins. Never
concede on Tier 1 without escalation to senior counsel or board sign-off.

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Identify the deal type, parties, deal size, governing law, and user's side. Determine
whether a transaction playbook is available. Assess the scope of representations and any
indemnification approach already agreed in the LOI or term sheet. Identify any known diligence
concerns that require specific indemnities.

**DO**: Execute the Critical Deal Mechanics Assessment (Step 6) and clause-by-clause analysis
(Step 7). Classify GREEN/YELLOW/RED. Generate redlines with fallback positions. Assign
negotiation priorities.

**CHECK**: Run Citation Quality Gates silently. For all RED items, run Self-Interrogation.
Verify that the overall deal structure is coherent (not just individual clauses). Check that
the Glass Box audit trail is complete.

**ACT**: Identify any systemic deal structure issues (not just individual clause problems) that
warrant escalation or deal restructuring. Note patterns: if many reps are heavily qualified
and the escrow is small, the overall deal protection may be inadequate even if each clause
passes individually.

---

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                     | Fail Action                                                   |
| -------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **Source**     | Every legal or market-standard claim cites a specific statute, case, regulation, or market data source   | Add citation or mark "[UNVERIFIED — counsel to confirm]"      |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction                              | Fix format                                                    |
| **Currency**   | Every cited provision checked for amendments, repeal, or superseding case law                            | Flag "[CHECK CURRENCY — may have been amended or superseded]" |
| **Domain**     | Analysis stays within the agreement's governing law — no assumptions from other jurisdictions leaking in | Remove or flag jurisdictional bleed                           |
| **Confidence** | Uncertainty explicitly stated, not hidden. Market standard claims are qualified with [VERIFY]            | Add confidence qualifier                                      |

---

### Self-Interrogation for RED Items

For any clause classified as RED, apply this 3-pass self-interrogation before delivering:

**Pass 1 — Legal Chain Integrity:**

- Does the risk assessment follow logically from the cited statute, case, or market principle?
- Would M&A counsel in this jurisdiction actually reach this conclusion on these deal facts?
- Is there a counter-argument that the other side's counsel will make?
- Would sophisticated M&A counsel in this jurisdiction accept this risk in this deal context?

**Pass 2 — Completeness:**

- Have all relevant statutes, regulations, and market standards been considered?
- Does the provision interact with the escrow, earn-out, purchase price mechanism, or rep
  insurance in ways not yet analyzed?
- Are there deal mechanics (enhanced escrow, specific indemnity, closing condition) that could
  adequately address this issue and convert it from RED to YELLOW?

**Pass 3 — Challenge:**

- What is the strongest argument that this clause IS acceptable?
- Under what deal circumstances (size, structure, industry, relationship) might reasonable M&A
  counsel accept this risk?
- Is the RED classification proportionate, or is this actually YELLOW with redlines?
- Does the RED classification reflect deal-specific risk or over-cautious general advice?

If any pass reveals a weakness, revise the analysis before delivery. Mark the audit trail:
`self_interrogation: PASS` or `self_interrogation: REVISED`.

---

### Confidence Scoring

For the overall assessment and each material finding, assign a confidence level:

| Level        | Range     | Meaning                                                         | Action                                                    |
| ------------ | --------- | --------------------------------------------------------------- | --------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law or clear market standard; no reasonable counter     | State with confidence                                     |
| **High**     | 0.80–0.94 | Strong authority or market data; minor interpretation questions | State with brief caveat                                   |
| **Probable** | 0.60–0.79 | Good arguments; reasonable deal counsel could differ            | State with explicit reasoning and contra-indicators       |
| **Possible** | 0.40–0.59 | Material uncertainty; competing interpretations or evolving law | Flag for qualified counsel review with both sides         |
| **Unlikely** | 0.0–0.39  | Weak evidentiary or legal basis                                 | Do not assert; flag "[UNCERTAIN — M&A counsel to advise]" |

**Calibration note**: Given the deal-consequential nature of purchase agreement analysis, err
toward flagging uncertainty rather than hiding it. A "Probable" finding presented as "Definite"
can cause a board to decline a viable deal or sign into an undisclosed material risk.

---

## Glass Box Audit Trail

Every purchase agreement review output MUST include a Glass Box audit section at the end.

```yaml
glass_box:
  skill_name: "legalcode-purchase-agreement-review"
  agreement: "[SPA/APA title, date, version — e.g., 'Stock Purchase Agreement dated [date] between [Buyer] and [Seller]']"
  agreement_type: "[Asset Purchase / Stock Purchase / Forward Merger / Reverse Triangular Merger / Carve-out]"
  user_side: "[Buyer / Seller / Seller's shareholders / Advisor (buy-side) / Advisor (sell-side)]"
  deal_size: "[USD/GBP/EUR amount or 'Not disclosed']"
  deal_type: "[Strategic acquisition / Financial sponsor (PE/VC) / Carve-out / Founder exit / Distressed / MBO]"
  governing_law: "[Jurisdiction identified from the agreement]"
  dispute_resolution: "[Litigation — [court] / Arbitration — [rules, seat, arbitrators]]"
  playbook_used: "[M&A Playbook name or 'General M&A market standards']"
  review_basis: "[Organizational transaction playbook / General market standards]"

  # DEAL MECHANICS FIELDS
  purchase_price_mechanism: "[Fixed / Locked box / Completion accounts / Not specified]"
  rep_scope: "[Full reps / Limited reps / Baseline only]"
  materiality_scrape: "[Present / Absent / Partial]"
  indemnification_structure: "[Mutual / Seller-only / Buyer-only / Not specified]"
  basket_type: "[Tipping / True deductible / Mini-basket only / Not specified]"
  basket_amount: "[USD/% of purchase price / Not specified]"
  general_cap: "[USD/% of purchase price / Not specified]"
  fundamental_rep_cap: "[USD/% / Uncapped / Not specified]"
  general_rep_survival: "[months / Not specified]"
  fundamental_rep_survival: "[years/indefinite / Not specified]"
  escrow_structure: "[USD/% for X months / Holdback only / None / RWI replaces / Not specified]"
  rw_insurance: "[Buy-side policy / Sell-side policy / None / Pending / Not disclosed]"
  earnout_present: "[Yes — USD X for Y months / No]"
  fraud_carve_out: "[Present / Absent / Unclear]"

  # ANALYSIS FIELDS
  clauses_analyzed: "[count out of 22 categories]"
  green_count: "[count]"
  yellow_count: "[count]"
  red_count: "[count]"
  missing_clauses: "[count] — [list critical missing]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-spa-review-authority.md or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  case_law_consulted:
    - "[Case — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation:
    red_items_reviewed: "[count]"
    result: "PASS / REVISED — [summary of any revisions]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Disclosure schedules not attached — reviewed agreement language only]"
    - "[Rep insurance policy not reviewed — referenced only]"
    - "[Any other scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires review by qualified M&A counsel"
```

---

## Anti-Patterns

What NOT to do when reviewing purchase agreements:

1. **Single-pass analysis without cross-referencing** — Representations, indemnification caps,
   baskets, and survival periods form an interconnected system. A broad rep with a tiny cap
   provides less protection than a narrow rep with an adequate cap. Analyze as a system, not
   as isolated clauses.

2. **Citing M&A case law from memory without verification** — M&A law evolves rapidly. MAC/MAE
   standards, successor liability doctrine, and non-compete enforceability have all shifted
   materially in recent years. Always mark statutory and case law references [VERIFY].

3. **Applying US M&A concepts to non-US transactions** — US materiality scrapes, sandbagging
   provisions, and basket mechanics are not universal. UK deals often use different rep warranty
   periods and indemnification doctrine. German warranty breach analysis under BGB differs from
   common law. [VERIFY] jurisdiction-specific rules before applying US market standards.

4. **Treating all escrow structures as equivalent** — An indemnification escrow of 10% for 18
   months is fundamentally different from a 3% escrow for 9 months. Assess the escrow against
   the cap, the rep scope, and the identified risk profile — not just as a percentage in isolation.

5. **Ignoring the purchase price mechanism interaction with representations** — In a locked box
   deal, price adjustments are determined by the locked box balance sheet and no-leakage warranty.
   In a completion accounts deal, the adjustment determines closing value. Reps covering financial
   statements and the purchase price adjustment mechanism must be reviewed together.

6. **Reviewing reps in isolation from the indemnification cap** — A seller that gives broad
   representations but limits the cap to 5% of purchase price has effectively limited buyer's
   recovery on every rep. The practical question is: "Does the cap cover the realistic
   downside if the most material reps are breached?"

7. **Missing embedded financing contingencies** — Seller financing, promissory notes, or
   earnout clauses can create post-closing obligations that mimic representations. If the seller
   has retained ongoing exposure through contingent consideration, they have an ongoing
   information obligation that must be reviewed.

8. **Redlines without deal-context fallbacks** — "Delete this limitation" is unhelpful if the
   seller will never agree. Redlines must include fallback positions: "If [primary ask] is not
   accepted, the minimum acceptable position is [fallback]." Include alternative deal mechanics
   (enhanced escrow, specific indemnity) as alternatives to pure language redlines.

9. **Assuming change-of-control clauses don't trigger in stock purchases** — Many third-party
   contracts define "change of control" to include changes in beneficial ownership, not just
   assignment. In a stock purchase, a change in the shareholder of the target company can
   trigger change-of-control clauses without any contract assignment.

10. **Treating earn-out provisions as a financial analysis issue, not a legal one** — Earn-out
    disputes are primarily legal disputes about how the metric is calculated and whether the
    buyer impaired the business. Review anti-manipulation covenants, accounting methodology
    definitions, and dispute resolution as carefully as any other deal mechanic.

11. **Confidence without quantification** — Saying "this indemnification cap is too low" is
    insufficient. Estimate as a percentage of purchase price, identify the largest potential
    claim type, and assess whether the cap covers a realistic downside. M&A review without
    quantification of exposure is incomplete.

12. **Importing terminology from the wrong deal type** — Reps and warranties in an asset purchase
    cover assets and assumed liabilities; in a stock purchase, they cover the entire company. "No
    undisclosed liabilities" means entirely different things in APA vs. SPA. Applying one form's
    standards to the other creates misleading analysis.

13. **Ignoring bring-down certificates and reps at closing** — If the purchase agreement requires
    reps to be re-certified at closing via officer certificates, analyze the bring-down standard:
    "accurate in all material respects at closing" is different from "accurate in all respects
    at closing." Bring-down failure may give buyer a right not to close; the standard determines
    how material a rep failure must be to trigger that right.

14. **Skipping the holistic deal structure assessment** — Individual clauses can each be
    YELLOW but the overall deal structure can be RED: broad reps + tiny cap + no escrow + no
    rep insurance + 12-month survival = practically no post-closing protection. The Critical Deal
    Mechanics Assessment (Step 6) exists to catch this pattern before clause-by-clause analysis.

15. **Assuming the disclosed schedules are complete** — Disclosure schedules are the seller's
    primary mechanism for limiting rep exposure. Incomplete schedules are common and deliberate.
    Analyze what is absent as carefully as what is present. An empty litigation schedule for a
    $100M acquisition of a 20-year-old business warrants scrutiny.

16. **Failing to identify the anti-assignment risk for an asset purchase** — In an APA, every
    material contract requires analysis of assignment rights. "There are no anti-assignment
    clauses" is almost never true. The anti-assignment analysis must be completed before signing
    or before the acquisition closes, with consent obtained or a closing condition protecting
    the buyer.

17. **Treating rep insurance as always equivalent to cash escrow** — Rep insurance has exclusions
    (fraud, known breaches, matters disclosed in schedules) that cash escrow does not. A policy
    deductible that is smaller than the cash escrow it replaces may be less valuable if the most
    likely claims are in the policy exclusions. Analyze the policy exclusions against the deal's
    specific risk profile.

---

## Writing Standards

Apply plain-language discipline to all purchase agreement review output:

**For the review report:**

- Plain language. No unnecessary jargon or Latin phrases.
- Active voice: "Section 7.2 limits the indemnification cap to 12% of the purchase price" not
  "An indemnification limitation was identified in Section 7.2."
- Short sentences. One point per sentence.
- Name the section: cite the specific agreement section reference for every finding.
- Specific, not vague: "Negotiate: cap from 12% to 20% of purchase price" not "consider the
  indemnification cap."
- Quantify: "This leaves approximately USD X of potential rep breach exposure uncovered by
  the cap."

**For each finding:**

1. State what the agreement says (with section reference)
2. State what the market standard or playbook position is
3. State the risk of accepting the current language (with exposure quantification where possible)
4. State the proposed redline (specific language or approach)
5. State the fallback position

**Quality gates before delivery:**

1. Is the overall assessment (mix of GREEN/YELLOW/RED) stated at the top?
2. Is every RED item supported by a specific section reference?
3. Does the Critical Deal Mechanics Assessment table reflect the clause analysis?
4. Can a non-lawyer deal team member understand the executive summary?
5. Are legal claims in the rationale backed by authority (or flagged [VERIFY])?
6. Is the Glass Box audit trail complete?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.
legalcode-mcp is the Legalcode law, regulatory, and case law database with powerful search
across jurisdictions.

**With legalcode-mcp connected (preferred):**

- In Step 5, search for jurisdiction-relevant corporate statutes, indemnification doctrine,
  non-compete enforceability law, MAC/MAE case law, and regulatory filing requirements
- Save the most relevant results to `/tmp/legalcode-spa-review-authority.md`
- For each RED item, search for supporting case law or market data to strengthen or challenge
  the classification
- Verify current state of non-compete law in applicable jurisdiction (particularly US — law
  evolving as of 2024–2025) [VERIFY]
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus on structural assessment, deal mechanics analysis, and commercial risk assessment
- Recommend independent verification of legal authority before using any cited provision in
  a transaction

---

## Output Format Template

Structure the final purchase agreement review as:

```markdown
## Purchase Agreement Review

**Agreement**: [SPA/APA title, date, version]
**Parties**: [Buyer] acquiring [Target] from [Seller]
**Your Side**: [Buyer / Seller]
**Deal Size**: [Purchase price and structure]
**Deal Type**: [Asset Purchase / Stock Purchase / Merger]
**Governing Law**: [Jurisdiction]
**Dispute Resolution**: [Litigation — [court] / Arbitration — [rules, seat]]
**Review Basis**: [Transaction Playbook / General M&A market standards]
**Date of Review**: [date]

---

## Overall Assessment

**[GREEN / YELLOW / RED]** — [One-sentence overall assessment]
**Confidence**: [Level and rationale]

**Summary**: [2-3 sentence narrative of overall deal structure quality and key issues]

---

## Critical Deal Mechanics

| Mechanic                 | Agreed        | Market Standard   | Assessment         |
| ------------------------ | ------------- | ----------------- | ------------------ |
| Purchase Price           | [agreed term] | [market standard] | [GREEN/YELLOW/RED] |
| Price Mechanism          | [agreed term] | [standard]        | [GREEN/YELLOW/RED] |
| Escrow                   | [agreed term] | [standard]        | [GREEN/YELLOW/RED] |
| Rep Scope                | [agreed term] | [standard]        | [GREEN/YELLOW/RED] |
| General Rep Survival     | [agreed term] | [standard]        | [GREEN/YELLOW/RED] |
| Fundamental Rep Survival | [agreed term] | [standard]        | [GREEN/YELLOW/RED] |
| General Cap              | [agreed term] | [standard]        | [GREEN/YELLOW/RED] |
| Basket Type/Amount       | [agreed term] | [standard]        | [GREEN/YELLOW/RED] |
| Fraud Carve-out          | [agreed term] | [standard]        | [GREEN/YELLOW/RED] |
| RWI Policy               | [agreed term] | [standard]        | [GREEN/YELLOW/RED] |

---

## Key Findings

[Top 3-5 RED or YELLOW items with severity flags]
[Presented in order of priority: Tier 1 first]

---

## Clause-by-Clause Analysis

### PART A: Purchase Price and Consideration

[Analysis for A-1, A-2, A-3 per the clause analysis framework]

### PART B: Representations and Warranties

[Analysis for B-1 through B-4]

### PART C: Indemnification Framework

[Analysis for C-1 through C-6]

### PART D: Closing Mechanics

[Analysis for D-1 through D-3]

### PART E: Post-Closing Provisions

[Analysis for E-1 through E-3]

### PART F: Governing Terms

[Analysis for F-1 through F-3 as applicable]

---

## Missing Clauses

| Missing Clause | Classification | Rationale                      |
| -------------- | -------------- | ------------------------------ |
| [Clause]       | [YELLOW/RED]   | [Why it's needed in this deal] |

---

## Negotiation Strategy

**Tier 1 (Must-Haves)**: [List with brief rationale]

**Tier 2 (Strong Preferences)**: [List with brief rationale]

**Tier 3 (Concession Candidates)**: [List — can trade for Tier 1/2 wins]

**Recommended approach**: [Sequencing and strategic trades]

---

## Stakeholder Impact Map

| Stakeholder                         | Role                        | Affected Clauses                               | Primary Impact        | Recommended Action        |
| ----------------------------------- | --------------------------- | ---------------------------------------------- | --------------------- | ------------------------- |
| [Buyer]                             | Principal — acquiring party | All                                            | Primary               | Lead negotiation          |
| [Seller / Shareholders]             | Principal — selling party   | All                                            | Primary               | Respond to redlines       |
| [Buyer's lenders/financing sources] | Lender                      | Rep accuracy, MAC, escrow                      | Significant           | May require rep insurance |
| [Regulators]                        | Authority                   | Closing conditions, compliance reps, CFIUS/HSR | Approval timeline     | Track filing requirements |
| [Key employees]                     | Indirect                    | Non-compete, earn-out, benefits                | Employment continuity | Coordinate retention      |
| [Escrow agent]                      | Custodian                   | Escrow mechanics, release                      | Administrative        | Coordinate with counsel   |
| [Target's key customers/suppliers]  | Third parties               | Anti-assignment, change of control             | Contract continuity   | Consent management        |

---

## Red Flags Specific to This Deal

[Highlight deal-specific items that fall outside typical market ranges or create
structural imbalance not captured in the clause analysis above]

---

## Next Steps

1. [Specific action with owner and deadline]
2. [Specific action with owner and deadline]

---

## Glass Box Audit Trail

[YAML block per the Glass Box section above]
```

---

## Localization Notes

This skill is jurisdiction-agnostic by design. To create a jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with verified jurisdiction-specific legal content
2. Replace [VERIFY] tags with confirmed statutory references (via legalcode-mcp where available)
3. Add jurisdiction-specific anti-patterns (e.g., German AGB requirement analysis, French
   garantie des vices cachés interaction with reps, New York common law anti-sandbagging)
4. Update market standard benchmarks with jurisdiction-specific deal data
5. Add local language requirements (if non-English jurisdiction requires bilingual documents)
6. Update the frontmatter name and description to reference the specific jurisdiction

**Planned jurisdiction variants (roadmap):**

- `legalcode-purchase-agreement-review-us` — Delaware DGCL, New York choice of law, HSR/CFIUS,
  WARN Act, FTC non-compete law
- `legalcode-purchase-agreement-review-uk` — UK Companies Act 2006, NSIA 2021, CMA, TUPE,
  locked box standard practice, English warranty doctrine
- `legalcode-purchase-agreement-review-eu` — EUMR, EU FDI Regulation, Works Council Directive,
  GDPR cross-border, country-specific warranty periods

---

## Provenance

Created by Legalcode (2026-03-01). Original synthesis developed to provide comprehensive
clause-by-clause review for M&A purchase agreements, addressing the gap between general
contract review skills (`legalcode-contract-review`) and M&A diligence skills
(`legalcode-ma-due-diligence-checklist`, `legalcode-due-diligence-report`). This skill
covers the purchase agreement itself — the definitive transaction document — as distinct
from due diligence conducted before signing.

Structural patterns and quality frameworks adopted from:

- `legalcode-contract-review` — clause analysis structure, quality frameworks (PDCA, Citation
  Quality Gates, Self-Interrogation, Confidence Scoring, Glass Box), anti-patterns catalogue,
  writing standards, redline generation methodology
- `legalcode-nda-triage` — interactive CLARIFY pattern, Tier 1/2/3 prioritization
- `legalcode-due-diligence-report` — deal mechanics assessment, audience-differentiated output,
  stakeholder mapping, M&A-specific Glass Box fields

Legal substance informed by:

- ABA Private Target M&A Deal Study (market benchmarks for baskets, caps, escrow, survival) [VERIFY]
- Seyfarth Shaw 2023/2024 Middle Market M&A Survey [VERIFY]
- _Akorn, Inc. v. Fresenius Kabi AG_, Del. Ch. 2018 (MAC/MAE clause) [VERIFY]
- _IBP, Inc. v. Tyson Foods, Inc._, Del. Ch. 2001 (MAE long-term perspective) [VERIFY]
- WTW/Willis Towers Watson Transactional Risk Survey 2024 (RWI market data) [VERIFY]
- Kroll Earn-Outs in M&A Report (earnout dispute frequency and best practices) [VERIFY]
- Winston & Strawn: Purchase Price Adjustment Mechanisms (locked box vs. completion accounts) [VERIFY]
- Latham & Watkins: FTC Non-Compete Rule Update 2025 (US non-compete law developments) [VERIFY]

All legal citations are unverified unless marked VERIFIED via legalcode-mcp. Verify all
statutory and case law references against authoritative sources before relying on them in
a transaction.
