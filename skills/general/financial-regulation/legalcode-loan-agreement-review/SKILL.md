---
name: legalcode-loan-agreement-review
description: Review loan and credit agreements clause-by-clause from the borrower or lender perspective.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review loan and credit agreements clause-by-clause from the borrower or lender perspective. Covers interest rate provisions (fixed, variable, SOFR/SONIA benchmark transition, default rate, usury compliance), financial covenants (leverage ratio, interest coverage, fixed charge coverage, minimum liquidity, net worth, equity cure), affirmative and negative covenants, representations and warranties, conditions precedent to drawdown, events of default (payment, cross-default, cross-acceleration, MAC/MAE, judgment, insolvency), remedies and acceleration, prepayment provisions (voluntary, mandatory sweeps, make-whole, yield maintenance), security and collateral requirements (UCC Article 9 perfection, IP security interests, springing liens), guaranty provisions, intercreditor arrangements (first/second lien, unitranche FLFO), assignment and participation mechanics, and amendment/waiver provisions (required lender thresholds, yank-a-bank). Also covers EU Credit Servicers Directive 2021/2167, UK Financial Collateral Arrangements Regulations 2003, LMA Green Loan and sustainability-linked loan provisions, and LSTA model credit agreement mechanics. Produces clause-by-clause review with borrower-favorable and lender-favorable redline recommendations and negotiation prioritization.


# Legalcode Loan Agreement Review

> **Disclaimer**: This skill provides a framework for AI-assisted loan and credit agreement
> review. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional — including banking and finance counsel licensed in the
> relevant jurisdiction — before use. Laws change; verify current applicability before
> relying on any provision described here. Statutory and case law references cited from
> memory carry hallucination risk — verify against authoritative sources before relying
> on them. Interest rate and benchmark calculations require verification by a qualified
> financial professional.

## Purpose and Scope

This skill reviews loan agreements, credit agreements, and facility agreements from the
borrower's or lender's perspective. It performs clause-by-clause analysis against market
standards (LMA for English law / LSTA for New York law) and the reviewing party's
preferred positions, identifies deviations, and generates actionable redlines.

**Covers:**

- Bilateral and syndicated loan facilities (term loans, revolving credit facilities,
  delayed-draw term loans, unitranche, first-lien/second-lien structures)
- All core loan agreement sections: interest, covenants, events of default, security,
  prepayment, intercreditor arrangements, and amendment mechanics
- Financial covenant testing: leverage, interest coverage, fixed charge coverage,
  minimum liquidity, net worth, and equity cure mechanics
- Benchmark rate transition (SOFR, SONIA, EURIBOR) and post-LIBOR drafting
- Security perfection analysis: UCC Article 9 (US), FCAR 2003 (UK), and EU considerations
- ESG/sustainability-linked loan provisions (LMA November 2024 Green Loan provisions)
- LMA (English law) and LSTA (New York law) market standard comparisons
- EU Credit Servicers Directive 2021/2167 implications for loan transfers
- Intercreditor analysis: first/second lien, unitranche/FLFO (first-out/last-out),
  Agreement Among Lenders (AAL) structures

**Does not:**

- Provide legal advice or replace qualified banking and finance counsel
- Apply exclusively to any single jurisdiction — uses jurisdiction-agnostic framework
  with [JURISDICTION-SPECIFIC] markers
- Perform quantitative financial modelling (debt capacity, LTV calculations, covenant
  headroom projections — refer to a financial adviser)
- Cover project finance, real estate finance, or Islamic finance as primary focus
  (though the general framework applies with modification)
- Draft new loan agreements from scratch (see legalcode-saas-agreement-drafter or
  legalcode-master-services-agreement for drafting-focused skills)

**Related skills:**

- `legalcode-contract-review` — general commercial contract review
- `legalcode-indemnification-analysis` — deep indemnification clause analysis
- `legalcode-limitation-of-liability-review` — liability cap analysis
- `legalcode-arbitration-clause-review` — dispute resolution clause analysis

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic. The loan agreement's governing law clause determines
which legal framework applies. The two dominant frameworks are:

- **English law (LMA standard)**: Loan Market Association facility agreement conventions.
  Governed by English law, often with English courts or LCIA arbitration. Enforcement of
  security typically requires court order unless FCARs 2003 apply.
- **New York law (LSTA standard)**: Loan Syndications and Trading Association model credit
  agreement provisions (MCAPs). Governed by New York law; UCC Article 9 governs security
  perfection. LSTA MCAPs updated July 2024 govern agency, assignments, and defaulting
  lenders.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- **US**: UCC Article 9 security interest perfection (financing statement filing, control
  agreements for deposit accounts/investment property); Copyright Act § 205 preemption
  for registered copyrights; state usury laws and federal preemption under the National
  Bank Act; valid-when-made doctrine (OCC final rule, 2020); Madden v. Midland Funding
  (786 F.3d 246 (2d Cir. 2015)) risk for non-bank assignees [VERIFY]
- **UK**: Financial Collateral Arrangements (No.2) Regulations 2003 (SI 2003/3226);
  appropriation rights without court order; English insolvency set-off; Companies Act 2006
  charges registration; Law of Property Act 1925 for mortgages [VERIFY]
- **EU**: EU Credit Servicers Directive 2021/2167 (Credit Servicers and Credit Purchasers
  Directive — "CSCD") for non-performing loan transfers; EMIR clearing obligations for
  hedging; ECB regulatory requirements for institutional lenders [VERIFY]
- **All jurisdictions**: Identify mandatory consumer protection rules if any party is a
  consumer; confirm whether the anti-deficiency statutes apply to guarantors (California
  Code of Civil Procedure §§ 580a-580e for real property secured loans) [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points marked with
**⟁ CLARIFY**. The workflow pauses and asks when:

- The answer changes the direction of the analysis
- Multiple valid approaches exist and the reviewer's preference matters
- Risk tolerance or deal context is needed to classify severity correctly
- Ambiguity in defined terms creates material uncertainty

If the user has already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept the Loan Agreement

Accept the document in any format:

- **File**: PDF, DOCX, or other document format (including schedules and exhibits)
- **URL**: Link to the document in a CLM, VDR, or cloud storage system
- **Pasted text**: Agreement text pasted directly into the conversation

If no document is provided, prompt the user to supply one. Note which schedules and
exhibits have been received — schedules often define the economics (interest margins,
commitment amounts, borrowing base) and covenants (financial covenant thresholds,
negative covenant baskets).

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask:

1. **Which party are you reviewing for?**
   - Options: Borrower / Guarantor, Lender / Agent (lead arranger), Lender (participant),
     Intercreditor party (mezzanine / second lien), Other
   - _Why this matters_: The entire analysis flips. What protects a lender (broad MAC,
     tight covenants, uncapped acceleration) harms a borrower and vice versa.

2. **Facility type:**
   - Options: Term loan A (amortizing), Term loan B (bullet / minimal amortization),
     Revolving credit facility (RCF), Unitranche (single tranche with FLFO AAL),
     First lien / second lien (two-tranche structure), Bridge facility, Other
   - _Why this matters_: Covenant-lite vs. maintenance covenant structure, prepayment
     mechanics, and intercreditor analysis differ fundamentally by facility type.

3. **Governing law / market standard:**
   - Options: English law (LMA standard), New York law (LSTA standard), Other
     jurisdiction (specify), Unknown
   - _Why this matters_: Determines the baseline market standard for each clause,
     security perfection requirements, and enforcement mechanics.

4. **Deal context:**
   - Free text. Examples: leveraged buyout (sponsor-backed), investment grade corporate
     facility, real estate secured, asset-based lending (ABL), direct lending /
     private credit, growth equity facility, acquisition facility, refinancing.
   - _Why this matters_: A sponsor-backed leveraged loan uses very different market
     conventions from an investment-grade facility or an ABL deal.

5. **Review focus** (multi-select):
   - Financial covenants, Events of default, Security and collateral, Interest rate
     and benchmark, Prepayment / make-whole, Negative covenants, Intercreditor /
     intercreditor priority, Full review (all 16 categories)
   - _Why this matters_: Long syndicated loan agreements (200+ pages) may warrant
     a priority review focused on the most material issues.

State assumptions explicitly for any questions not answered upfront.

### Step 3: Read the Entire Agreement Before Analyzing

Read the full loan agreement including all schedules before flagging issues. Loan
agreements have deep cross-references — covenants interact with definitions, events
of default reference financial covenant tests, and prepayment mechanics reference
baskets defined in the negative covenants.

Critical sections to locate and read first:

- **Definitions** — EBITDA, Consolidated Net Debt, Leverage Ratio, Material Adverse
  Effect, Permitted Liens, Permitted Debt, Restricted Payment, Change of Control, Market
  Disruption Event, Benchmark Replacement (SOFR/SONIA transition provisions)
- **Financial covenant schedule** — the tested ratios and threshold levels
- **Negative covenant baskets** — the permitted amounts for debt, liens, disposals,
  restricted payments

**⟁ CLARIFY** — For long agreements (100+ pages) or those with multiple schedules:
Ask whether to perform a **full review** of all 16 clause categories or a **priority
review** focused on the stated focus areas plus any items flagged as RED.

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Identify the governing law clause. Then use **legalcode-mcp** to build a working
legal reference file for this review.

**Research process:**

1. Search legalcode-mcp for relevant authority:
   - Security perfection requirements for the applicable jurisdiction
   - Usury and interest rate limits (especially for US facilities)
   - Benchmark rate transition regulations (FCA/FSMA for SONIA, SEC/Fed for SOFR)
   - Insolvency rules affecting close-out netting and set-off
   - MAC/MAE case law in the applicable jurisdiction
   - Credit servicer and loan transfer regulations (EU CSCD if relevant)

2. Save the most relevant results to `/tmp/legalcode-loan-review-authority.md`.

3. Use this reference throughout the analysis. Mark legalcode-mcp-sourced citations
   as VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with analysis but flag that legal authority requires independent verification

**Key 2024 legal developments to check:**

- BM Brazil I FdI MP v. Sibanye BM Brazil [2024] EWHC 2566 (Comm) — MAC clause
  interpretation: material change must be "significant or substantial" [VERIFY]
- LSTA Model Credit Agreement Provisions (MCAPs) updated July 2024 [VERIFY]
- LMA Draft Provisions for Green Loans published November 2024 [VERIFY]
- OCC valid-when-made final rule (2020) — codifies Gaither v. Farmers & Mechanics Bank
  doctrine against Madden v. Midland Funding challenge [VERIFY]

### Step 5: Clause-by-Clause Analysis

Analyze all 16 clause categories systematically. For each clause:

1. Identify what the agreement says
2. Compare to LMA or LSTA market standard (as applicable)
3. Assess from the reviewing party's perspective
4. Classify severity (GREEN / YELLOW / RED)
5. For YELLOW and RED: generate a specific redline with rationale

| #   | Clause Category               | Depth    | Key Review Points                                                     |
| --- | ----------------------------- | -------- | --------------------------------------------------------------------- |
| 1   | Interest Rate & Benchmark     | Deep     | SOFR/SONIA transition, margin, PIK, default rate, usury               |
| 2   | Financial Covenants           | Deep     | Leverage, ICR, FCCR, liquidity, EBITDA definition, equity cure        |
| 3   | Affirmative Covenants         | Standard | Financial reporting, compliance certs, insurance, existence           |
| 4   | Negative Covenants            | Deep     | Debt basket, lien basket, restricted payments, disposals, mergers     |
| 5   | Representations & Warranties  | Deep     | Repeating reps, MAC, solvency, financial statements, IP               |
| 6   | Conditions Precedent          | Standard | Legal opinions, CPs to closing vs. each drawdown                      |
| 7   | Events of Default             | Deep     | Payment, covenant, cross-default, cross-acceleration, MAC, insolvency |
| 8   | Remedies & Acceleration       | Deep     | Automatic vs. discretionary, standstill, cure periods                 |
| 9   | Prepayment Provisions         | Deep     | Voluntary, mandatory sweeps, make-whole, yield maintenance            |
| 10  | Security & Collateral         | Deep     | UCC Article 9, FCARs, IP security, perfection, priority               |
| 11  | Guaranty Provisions           | Standard | Payment vs. collection, continuing, anti-deficiency, waivers          |
| 12  | Intercreditor Arrangements    | Deep     | First/second lien, unitranche FLFO, AAL, standstill, enforcement      |
| 13  | Assignment & Participation    | Standard | Borrower consent, disqualified institutions, LSTA registers           |
| 14  | Amendment & Waiver            | Standard | Required lenders, unanimous consent, yank-a-bank, snooze-you-lose     |
| 15  | Syndicate / Agency Provisions | Standard | Administrative agent, defaulting lender, fronting exposure            |
| 16  | ESG / Sustainability          | Standard | SLL KPIs, margin ratchet, green use-of-proceeds, greenwashing risk    |

### Step 6: Missing Clause Detection

After analyzing present clauses, check for material absent provisions:

Common critical absences in loan agreements:

- No SOFR/SONIA fallback language in a floating-rate loan referencing LIBOR (RED)
- No equity cure mechanics in a sponsor-backed deal with maintenance covenants (RED)
- No cross-default carveout for immaterial debt (RED — could trigger on trivial defaults)
- No make-whole limitation on mandatory prepayment from asset sale proceeds (YELLOW)
- No disqualified institution list or Specified Discount Purchaser provisions (YELLOW
  if the borrower is sponsor-backed)
- No anti-cash-hoarding provision for revolving facilities (YELLOW — lender concern)
- No CSCD compliance provisions for EU-originated loans likely to be transferred (YELLOW)
- No ESG/sustainability provisions when the borrower has made public ESG commitments (YELLOW)
- No intercreditor agreement when the capital structure has multiple debt tranches (RED)

**⟁ CLARIFY** — When the significance of a missing clause depends on business context:

- "This facility has no equity cure mechanics. Are financial maintenance covenants included?
  If yes, equity cure is likely expected by the borrower's sponsor — its absence is RED.
  If this is cov-lite, it may be intentional."
- "There is no SOFR fallback language. Is this a new facility or a legacy LIBOR facility?
  Legacy facilities urgently need fallback documentation."

### Step 7: Classify Deviations

Classify each deviation using the four-tier system in the **Deviation Severity
Classification** section. For each deviation, generate the prescribed output:

- **GREEN**: Note for awareness.
- **YELLOW**: Generate a specific redline with rationale. Provide a fallback position.
- **RED**: Explain the specific risk with legal basis. Provide market-standard alternative
  language. Estimate exposure. Recommend escalation to senior banking counsel.
- **CRITICAL (deal-breaker)**: Flag immediately. This issue must be resolved before
  drawdown. Examples: missing perfected security in a secured facility; no governing law
  clause; covenants so tight that breach is inevitable on day one.

**⟁ CLARIFY** — For borderline classifications:

- Cross-default threshold: "The cross-default threshold is $[X]M. Is this too low given
  the size of the borrower's other indebtedness? What other debt does the borrower have?"
- MAC scope: "The MAC definition includes 'prospects' — courts have held this extremely
  difficult to invoke (BM Brazil I [2024]). Is the MAC here used only as an EOD (standard)
  or also as a CP condition (higher risk of lender manipulation)?"

### Step 8: Generate Redlines

For each YELLOW and RED deviation, generate a redline using the **Redline Format**.
Before generating redlines, confirm negotiation posture if not already clear:

**⟁ CLARIFY** — Ask about negotiation posture if unclear:

- "This facility is [sponsor-backed leveraged / investment grade / bilateral]. Is the
  lender a relationship lender (more flexibility) or a new lender (arm's-length)?"
- "How many other banks are in the syndicate? The size of the required lender threshold
  affects which issues you can realistically push back on."

### Step 9: Business Impact Summary

Provide a summary covering:

- **Overall risk profile**: HIGH / MEDIUM / LOW (from the reviewing party's perspective)
- **Top 3-5 issues**: The most material items to address, with severity
- **Negotiation strategy**: Which issues to lead with; what to concede; sequencing
- **Covenant headroom note**: Flag if any financial covenant appears to have minimal
  headroom based on the stated thresholds and publicly available financial data
- **Execution timeline considerations**: Is this a committed facility with a signing
  deadline that constrains negotiation time?

**⟁ CLARIFY** — If deal context would materially affect strategy:

- "Is the borrower in a competitive process where lenders are competing, or is this
  a sole-lender deal? This affects the borrower's leverage on covenant and pricing terms."
- "Has this been through credit committee already? Post-credit-committee changes may
  require re-approval, which limits the issues worth pushing."

### Step 10: Quality Verification

Before delivering, run the quality checks in the **Quality Assurance Framework**:

1. Run the 5 Citation Quality Gates silently. Revise any failures.
2. For every RED item, run the 3-pass Self-Interrogation. Revise if a pass reveals weakness.
3. Assign a Confidence Score to each material clause analysis.
4. Verify all 16 clause categories addressed (present or flagged as missing).
5. Generate and append the Glass Box Audit Trail.

---

## Clause Analysis Reference

### 1. Interest Rate Provisions

**Key elements:**

- Base rate: fixed vs. floating; benchmark (SOFR / SONIA / EURIBOR / term SOFR /
  daily SOFR / compounded SOFR); margin ratchet mechanism (leverage-linked)
- Credit spread adjustment (CSA) for SOFR/SONIA transition from LIBOR (ARRC/ISDA
  recommended: 26.161 bps for 3-month SOFR vs. 3-month LIBOR) [VERIFY]
- Default interest rate: typically margin + 2-3% per annum over the base rate
- PIK (pay-in-kind) interest toggle provisions
- Market disruption event / market disruption clause fallback
- SOFR/SONIA fallback language — hardwired (preferred) vs. amendment approach

**Common issues:**

- LIBOR references without SOFR/SONIA fallback language (RED for new facilities;
  critical legacy issue for existing facilities)
- Default rate applying from date of default vs. date of demand (lender-favorable:
  from default; borrower-favorable: from demand)
- Absence of a lookback period or observation shift for daily compounded SOFR
  (operational complexity risk)
- PIK option without a corresponding increase in the cash equity cushion (lender risk)
- Market disruption clause with no objective threshold (purely discretionary — RED
  from borrower's perspective)

[JURISDICTION-SPECIFIC] Usury considerations:

- **US**: National Bank Act preempts state usury limits for national banks. However,
  Madden v. Midland Funding LLC (786 F.3d 246 (2d Cir. 2015)) held preemption does
  not extend to non-bank assignees in the Second Circuit. OCC final rule (May 2020)
  codified valid-when-made doctrine but faces ongoing challenge risk [VERIFY]. Non-bank
  lenders and fintechs must verify maximum interest rates in the governing state.
  Delaware and New York have no usury limit for commercial loans above $250K [VERIFY].
- **UK**: No general usury statute for commercial loans. Consumer Credit Act 1974
  applies only to consumer credit [VERIFY].
- **EU**: Varies significantly by member state — many have usury laws for commercial
  lending [VERIFY].

**Redline battlegrounds:**

- SOFR fallback: Borrower should push for hardwired ARRC language; lender may prefer
  amendment approach (more lender control)
- Credit spread adjustment: use ARRC/ISDA recommended spread; reject lender-bespoke CSA
- Default rate: Borrower position — default rate applies only upon acceleration, not
  mere default; Lender position — from first date of default

---

### 2. Financial Covenants

**Key elements:**

- **Leverage ratio**: Total Net Debt / Adjusted EBITDA ≤ [X]x (maintenance covenant
  tested quarterly, or springing covenant tested when revolving facility drawn above
  [Y]% threshold — typically 35-40%)
- **Interest coverage ratio (ICR)**: Adjusted EBITDA / Net Finance Charges ≥ [X]x
- **Fixed charge coverage ratio (FCCR)**: (Adjusted EBITDA - CapEx - Taxes - Dividends)
  / (Interest + Scheduled Debt Service) ≥ [X]x
- **Minimum liquidity**: Cash + undrawn revolving facility commitments ≥ $[X]M
- **Net worth covenant**: Consolidated net worth ≥ $[X]M (often in real estate loans)
- **EBITDA definition**: The critical battleground. Add-backs, adjustments, and
  run-rate projections can materially inflate or deflate the ratio
- **Equity cure mechanics**: Right to inject cash (EBITDA cure or debt cure) to rectify
  covenant breach; typically limited to 2 cures in any 4-quarter period, 5 total

**EBITDA definition key add-backs (typical LMA/LSTA market):**

- Non-recurring / extraordinary items (cap negotiated — typically 15-20% of EBITDA)
- Restructuring charges (time-limited; often limited to 18-24 months post-signing)
- Non-cash charges (stock compensation, impairments)
- Run-rate synergies / cost savings (post-acquisition; time-limited, typically 12-24
  months; often capped at 25-30% of EBITDA in large-cap US / 20% in European mid-market)
- Management fees (capped, often limited to arms-length amounts)
- Pro-forma EBITDA for acquisitions (pre-completion earnings included)

**Common issues (borrower perspective):**

- EBITDA definition caps on add-backs that are too restrictive (RED if add-backs exceed
  cap at signing — technical covenant breach immediately)
- Maintenance covenant with no equity cure right in a sponsor-backed deal (RED)
- Equity cure: no over-cure allowed; limited to exact cure amount (lender-favorable)
- Springing covenant threshold too low (e.g., 20% vs. market 35-40%) (YELLOW)
- Quarterly testing without an annual step-down (lender-favorable; borrower wants
  headroom that steps down as the business grows)

**Common issues (lender perspective):**

- EBITDA definition so broad with add-backs that the leverage ratio has no teeth (RED)
- Equity cure: unlimited cures with no requirement to repay debt (lender risk for
  private credit; note European market often permits uncapped debt cures — VERIFY)
- No cash-flow sweep to repay principal when covenant is being cured repeatedly
- Compliance certificate not required with each quarterly financial statement delivery

[JURISDICTION-SPECIFIC] European market 2024:

- Cov-lite structures (no maintenance covenant) are now common in large-cap European
  syndicated deals and are growing in private credit [VERIFY per ICLG 2024-2025]
- European equity cures: US-style EBITDA cure (no debt paydown required) has become
  standard; over-cures permitted [VERIFY]
- Springing leverage covenant is the primary governance mechanism in cov-lite structures

---

### 3. Affirmative Covenants

**Key elements:**

- Financial reporting: quarterly management accounts (45-60 days), annual audited
  accounts (90-120 days), annual budget / business plan
- Compliance certificate: delivered with each set of accounts, officer-certified, showing
  financial covenant calculations and confirming no Event of Default
- Insurance: maintain adequate insurance; provide evidence of coverage on request;
  lender named as additional insured (for secured loans)
- Maintain corporate existence, approvals, and licences material to the business
- Notify the agent of any Event of Default or Potential Event of Default promptly
- Material contracts: maintain in force; notify lender of material breach

**Common issues (borrower perspective):**

- Reporting deadlines too short for complex group reporting (YELLOW if < 45 days
  for quarterly management accounts)
- Compliance certificate requires officer to certify absence of all defaults (including
  minor covenant breaches) — overly broad, creates personal liability risk (YELLOW)
- Insurance must be maintained with lender-approved insurers — too restrictive (YELLOW)
- Budget delivery with business plan creates confidentiality concerns (YELLOW if sent
  to all syndicate lenders rather than agent only)

**Common issues (lender perspective):**

- No requirement to deliver monthly financials during periods of financial distress
- No field audit / borrowing base examination rights for ABL facilities (RED for ABL)
- No notice of material litigation, environmental issues, or regulatory investigations

---

### 4. Negative Covenants

**Key elements:**

- **Debt covenant / incurrence test**: prohibition on additional Financial Indebtedness
  subject to Permitted Debt baskets; common baskets: (i) existing debt, (ii) capital
  leases, (iii) trade payables, (iv) intercompany debt, (v) acquisition debt (ratio-based
  in large-cap deals: e.g., ≤ [X]x leverage on pro forma basis), (vi) general basket
  ($[X]M or % of EBITDA), (vii) builder basket (retained excess cash flow)
- **Lien covenant**: prohibition on Security Interests subject to Permitted Liens;
  standard carveouts: existing liens, purchase money security interests (PMSI),
  statutory liens, netting and set-off, financial collateral arrangements
- **Restricted payments**: prohibition on dividends, share buybacks, distributions
  to shareholders, management fee payments; carveouts: ordinary course management fees
  (capped), tax distributions, reinvestment from cash flow if pro forma leverage is
  met, builder basket
- **Asset disposals / disposition covenant**: prohibition on sales, transfers, leases
  or other disposals of assets; standard carveouts: ordinary-course sales, obsolete
  assets, intercompany transfers, arm's-length sales ≤ $[X]M, and reinvestment of
  proceeds within 12-18 months
- **Merger / change of control**: prohibition on mergers, consolidations, or similar
  transactions that would result in a Change of Control; carveouts for internal
  restructuring and acquisitions meeting leverage test

**Common issues (borrower perspective):**

- Debt basket too tight — no ratio debt basket, general basket too small (YELLOW/RED
  depending on borrower's investment strategy)
- No builder basket / grower basket (borrower loses ability to grow basket over time)
- Restricted payment basket: no ability to make restricted payments when in compliance
  (no "compliance with leverage" basket) (YELLOW in sponsor-backed deal)
- Disposal proceeds must be applied to mandatory prepayment with no reinvestment window
  (YELLOW — market standard is 12-18 months reinvestment right)
- "Permitted Indebtedness" definition cross-references "Permitted Liens" in a circular
  fashion — definitional drafting error (potential RED)

**Common issues (lender perspective):**

- Ratio debt basket with no floor — could permit unlimited debt at low leverage (RED)
- Restricted payment basket allows dividends even when Event of Default is continuing
- Carveout for "ordinary course" transactions undefined — creates enforcement gap

---

### 5. Representations and Warranties

**Key elements:**

**At signing (once):**

- Organization, authority, and enforceability
- Non-conflict with other agreements / constitutional documents
- No proceedings / material litigation
- Financial statements — most recently delivered accounts are true and fair
- No undisclosed liabilities

**Repeating representations** (deemed repeated at each drawdown and, for revolving
facilities, on each interest payment date):

- **No Material Adverse Effect / MAC representation**: No MAC has occurred since the
  date of the most recent audited accounts — most heavily negotiated rep in any loan
- **Solvency**: Group is solvent (test: assets > liabilities on a going-concern basis;
  no pending / reasonably anticipated insolvency)
- **Compliance with laws** (including AML / KYC, sanctions, anti-bribery — FCPA /
  UK Bribery Act / EU legislation)
- **Environmental compliance**: No material environmental liability; no material
  breach of environmental laws; no pending environmental investigations

**Key battlegrounds:**

| Issue                                   | Borrower Position                                  | Lender Position                                                      |
| --------------------------------------- | -------------------------------------------------- | -------------------------------------------------------------------- |
| MAC definition scope                    | Narrow: specific quantitative threshold            | Broad: subjective "business, assets, financial condition, prospects" |
| "Prospects" carveout                    | Delete "prospects" (courts rarely uphold)          | Retain for maximum lender protection                                 |
| Materiality qualifier on reps           | All repeating reps qualified by materiality or MAC | No materiality qualifier (lender wants absolute accuracy)            |
| Knowledge qualifier on litigation rep   | "So far as the Borrower is aware"                  | Objective (no knowledge qualifier)                                   |
| Solvency rep: historical or prospective | Historical only (at signing)                       | Also prospective / forward-looking                                   |

**Case law on MAC in loan agreements:**

- BM Brazil I FdI MP v. Sibanye BM Brazil [2024] EWHC 2566 (Comm): MAC must be
  "significant or substantial"; not temporary; lender cannot rely on circumstances
  known at signing unless they "worsen in a way that makes them materially different
  in nature"; burden of proof on lender [VERIFY]
- Grupo Hotelero Urvasco SA v. Carey Value Added SL [2013] EWHC 1039 (Comm): MAC
  event of default requires change in the company's financial position, not just in
  the market [VERIFY]

[JURISDICTION-SPECIFIC] Materiality scrape:

- **US (LSTA)**: Materiality scrapes on representations are common in leveraged deals
  (85% of private-target M&A deals include at least one scrape per SRS Acquiom 2024)
  but less common in loan reps [VERIFY]
- **UK (LMA)**: Materiality qualifiers negotiated clause-by-clause; less systematic
  than US practice

---

### 6. Conditions Precedent to Drawdown

**Key elements:**

**Conditions to first drawdown (closing CPs):**

- Loan agreement and security documents duly executed and delivered
- Legal opinions (borrower's counsel, lender's counsel, local counsel) — must confirm
  due authority, enforceability, no conflict, and perfection of security
- Copies of constitutional documents, board resolutions, director certificates
- Insurance certificates (for secured facilities)
- No Event of Default or Potential Event of Default is continuing
- All representations are true and correct (or true in all material respects)
- KYC / AML documentation delivered for all obligors
- Evidence of perfected security interests

**Conditions to each subsequent drawdown (revolving / delayed-draw):**

- No Event of Default or Potential Event of Default
- Repeating representations are true and correct (or true in all material respects)
- For revolving credit / ABL: Borrowing Base Certificate showing sufficient availability

**Common issues (borrower perspective):**

- CPs to each drawdown include MAC representation — lender can refuse funding based
  on MAC if MAC is broadly defined (RED risk; narrow MAC definition critical)
- "All representations true and correct" without materiality qualifier — minor inaccuracy
  could block drawdown (YELLOW — borrower should push for "in all material respects")
- Legal opinion scope overly broad — requires opinions on matters not reliably certifiable
  (YELLOW — work with counsel on feasibility)
- KYC documentation requirements not scoped to a reasonable list — creates delays (YELLOW)

---

### 7. Events of Default

**Key elements:**

| EOD Category                  | Key Issues                                                         | Borrower Watch Points                                                                                |
| ----------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| **Payment default**           | Grace period for principal vs. interest; 3-5 business days typical | Ensure adequate cure period; distinguish payment failure from bank error                             |
| **Financial covenant breach** | Maintenance vs. incurrence; cure period                            | Equity cure mechanics; standstill period before acceleration                                         |
| **Cross-default**             | Threshold ($[X]M); scope of "Indebtedness"                         | Threshold adequate for business size; carveout for bona fide disputes                                |
| **Cross-acceleration**        | Triggers only on acceleration, not default                         | Less aggressive than cross-default; borrower prefers this form                                       |
| **MAC/MAE event**             | Highly subjective; rarely invoked successfully                     | Must be "substantial and significant" and not temporary (BM Brazil I [2024])                         |
| **Change of Control**         | Automatic EOD on CoC triggers acceleration                         | Ensure permitted CoC transactions are carved out                                                     |
| **Repudiation / rescission**  | Borrower repudiates or challenges enforceability of security       | Should be limited to good-faith disputes                                                             |
| **Judgment EOD**              | Unsatisfied judgment > $[X]M                                       | Threshold and grace period; carveout for judgments being appealed in good faith                      |
| **Insolvency EOD**            | Automatic on insolvency filing                                     | Ensure grace period for administrative errors; exclude technical cross-border insolvency proceedings |
| **Cessation of business**     | Borrower ceases to carry on its principal business                 | Define "principal business" narrowly; carveout for internal restructuring                            |

**Cross-default vs. cross-acceleration — critical distinction:**

- **Cross-default**: Any default (even payment failure) on other indebtedness exceeding
  the threshold triggers an EOD here. Most aggressive — borrower unfavorable.
- **Cross-acceleration**: Only triggers if another lender actually accelerates. Less
  aggressive — market standard in LMA/LSTA investment grade; common in leveraged too.
- Borrower should always push for cross-acceleration over cross-default.

**Cure periods:**

- Payment EOD: 3-5 business days (market; no cure for acceleration EOD)
- Financial covenant EOD: typically 30-60 days plus equity cure window
- Representation breach: 10-30 days if remediable
- Cross-default/acceleration: often immediate (no cure) — lender-favorable

[JURISDICTION-SPECIFIC] MAC as EOD:

- UK courts: burden on lender to prove MAC; MAC based on known circumstances at signing
  not available unless circumstances worsen in fundamentally different way (Grupo
  Hotelero; BM Brazil I) [VERIFY]
- US courts: similar high bar; pandemic-era cases confirmed MAC rarely succeeds without
  quantitative evidence of sustained financial deterioration [VERIFY]

---

### 8. Remedies and Acceleration

**Key elements:**

- **Automatic acceleration**: Upon insolvency-related EODs, the facility typically
  accelerates automatically (no lender action required)
- **Discretionary acceleration**: For all other EODs, acceleration requires notice from
  the agent acting on instructions from the Required Lenders (majority lenders — usually
  66⅔% or more of commitments)
- **Standstill periods**: Intercreditor agreements may impose standstill periods during
  which junior lenders cannot enforce (see § 12)
- **Set-off and combination of accounts**: Lender right to set off amounts owed by the
  borrower against deposits held by lender — limited by FCARs in UK [VERIFY]
- **Receiver / administrator appointment**: English law allows appointment of an
  administrative receiver by qualifying floating charge holders [VERIFY]

**Common issues:**

- Automatic acceleration trigger defined too broadly — includes technical / remediable
  defaults (RED from borrower's perspective)
- No notice period before acceleration — acceleration simultaneous with EOD notice (YELLOW)
- Lender acceleration rights preserved even when EOD is being cured / cure is pending
- Set-off right not limited to amounts due and payable (lender can set off contingent
  liabilities — RED from borrower's perspective)

---

### 9. Prepayment Provisions

**Key elements:**

**Voluntary prepayment:**

- Borrower's right to prepay at par + accrued interest with notice (typically 3-5 business
  days for term loans; revolving facilities reborrow freely)
- Break costs (breakfunding): If prepayment is on a day other than an interest payment
  date, borrower must compensate lender for funding break costs (actual cost of unwinding
  hedge — not a make-whole)

**Mandatory prepayment — cash flow sweeps:**

- **Excess cash flow sweep**: % of annual excess cash flow applied to term loan
  amortization (typically 50-75% with step-down to 0-25% if leverage is below threshold).
  ECF defined as Adjusted EBITDA - CapEx - Tax payments - Interest - Scheduled debt service
- **Asset disposal proceeds**: Net proceeds from asset disposals above threshold must
  be applied to prepayment; borrower carveout for reinvestment of proceeds within 12-18
  months in the business
- **Equity issuance proceeds**: % of equity raise applied to prepayment (often 0% in
  sponsor-backed deals post-IPO if leverage is within covenant headroom)
- **Debt issuance proceeds**: 100% of net proceeds from new indebtedness (other than
  Permitted Debt) applied to prepayment
- **Insurance / condemnation proceeds**: Net proceeds above threshold applied if
  not reinvested in like-kind replacement within [X] months

**Make-whole / yield maintenance:**

- **Make-whole**: Prepayment compensates lender for present value of remaining interest
  payments discounted at Treasury rate + spread — most lender-favorable; common in
  US private placements and Term Loan A; less common in leveraged Term Loan B
- **Yield maintenance**: Similar to make-whole but typically calculated over remaining
  life of the facility at a fixed spread
- **Call protection / soft call**: In US leveraged Term Loan B, typical 101% call
  protection for 6 months (borrower pays 1% premium if prepaid in first 6 months);
  no premium after that — less punitive than make-whole

**Common issues (borrower perspective):**

- Make-whole applying to mandatory prepayment (asset sale proceeds) — RED; market
  standard is no make-whole on mandatory prepayments
- ECF sweep percentage too high with no step-down (YELLOW)
- Reinvestment period for asset disposal proceeds too short (YELLOW if < 12 months)
- No right to voluntary prepayment without lender consent (RED)
- Mandatory prepayment on change of control without any step-down or carveout for
  permitted equity transactions (YELLOW)

---

### 10. Security and Collateral

**Key elements:**

**Types of security:**

- All-asset lien (UCC-1 blanket filing / English law fixed and floating charge) —
  most comprehensive; standard for leveraged loans
- Specific asset security: real property mortgage / charge, share pledge, deposit
  account control agreement (DACA), assignment of receivables / intellectual property
- First lien vs. second lien: priority of security interest determines recovery waterfall

**US / UCC Article 9 perfection requirements:**

- **General intangibles / accounts / equipment**: File UCC-1 financing statement in
  the jurisdiction of the debtor's organization (or chief executive office for
  registered organizations)
- **Deposit accounts**: Requires a deposit account control agreement (DACA) — filing
  alone insufficient. Control perfects ahead of filing [VERIFY UCC § 9-327]
- **Investment property (securities accounts / certificated / uncertificated securities)**:
  Requires control (for securities accounts: DACA equivalent — securities account control
  agreement); alternatively, possession for certificated securities [VERIFY UCC § 9-328]
- **Registered copyrights**: Copyright Act § 205 preempts UCC Article 9 for registered
  copyrights — security interest must be recorded with the US Copyright Office. UCC-1
  filing alone is insufficient for perfection against third parties for registered works.
  Unregistered copyrights: UCC-1 filing [VERIFY — circuit split on this point]
- **Patents and trademarks**: UCC-1 filing (neither the Patent Act nor Lanham Act
  addresses security interests — no federal preemption) [VERIFY]
- **Commercial tort claims**: Must specifically describe the claim in the security
  agreement [VERIFY UCC § 9-108(e)]
- **UCC-1 duration**: Financing statements expire after 5 years; UCC-3 continuation
  filing required within 6 months before expiration

**UK — Financial Collateral Arrangements (No.2) Regulations 2003 (FCARs):**

- FCARs apply to "financial collateral" (cash, financial instruments, credit claims)
  between "non-natural persons" (corporate entities)
- Exempt from: (i) requirement for security to be evidenced in writing, (ii) need for
  court order to enforce, (iii) prohibition on appropriation
- Key enforcement right: appropriation — collateral taker can appropriate financial
  collateral (valued in commercially reasonable manner) without court order [VERIFY SI
  2003/3226, reg. 17]
- Title transfer collateral arrangements (repos) exempt from administration moratorium
  under UK Insolvency Act [VERIFY]
- FCARs do not cover real property, general intangibles, or ordinary trade receivables

**EU — Credit Servicers Directive (CSCD / Directive 2021/2167):**

- Requires authorisation of credit servicers managing non-performing loan (NPL) portfolios
- Credit purchasers (non-bank buyers of NPL portfolios) must use an authorised credit
  servicer
- Affects secondary market transfers and loan participations involving EU-originated loans
- EU member states required to implement by 29 December 2023 [VERIFY implementation
  status by jurisdiction]

**Common issues:**

- Missing DACA for deposit accounts in a US secured facility (RED — account not perfected)
- Copyright security recorded only with UCC-1 filing, not Copyright Office (RED for
  registered copyrights — perfection failure risk)
- Springing lien: lien only attaches upon breach of specified condition (e.g., leverage
  exceeds threshold) — operational complexity; ensure perfection on attachment
- Security covers "after-acquired property" without carveout for excluded assets
  (potential IP ownership dispute)
- No negative pledge covenant where security is not taken (YELLOW — lender should
  require negative pledge at minimum)
- FCARs scope not confirmed — if borrower is an individual or the collateral is not
  financial collateral, FCARs enforcement rights unavailable (RED if lender is relying
  on FCARs for enforcement)

---

### 11. Guaranty Provisions

**Key elements:**

- **Payment guaranty** (preferred by lender): guarantor is primarily liable; lender can
  pursue guarantor directly without first exhausting remedies against borrower
- **Collection guaranty** (preferred by guarantor): guarantor's liability arises only
  after lender has first exhausted remedies against borrower
- **Continuing guaranty**: covers all obligations under the facility, including
  amendments, increases, and extensions; not limited to initial advance
- **All-obligations / unlimited guaranty**: no cap on guarantor's liability
- **Limited guaranty**: capped at a fixed dollar amount or percentage of facility
- **Waiver of defenses**: guarantor waives suretyship defenses (right of set-off,
  contribution, exoneration, subrogation until borrower obligations repaid in full)

[JURISDICTION-SPECIFIC] Anti-deficiency and suretyship:

- **California**: CCP §§ 580a-580e — anti-deficiency rules limit lender's ability to
  obtain deficiency judgment following non-judicial foreclosure on real property security;
  may affect guarantor's obligations [VERIFY]
- **Restatement (Third) of Suretyship and Guaranty §§ 37-49**: discharge of guarantor
  upon lender conduct that impairs collateral or alters principal obligation without
  guarantor consent — confirm waiver of these rights in guaranty document [VERIFY]
- **UK**: guarantee must be in writing (Statute of Frauds 1677); guarantor discharged
  by material variation of principal obligation without consent (Holme v. Brunskill (1878))
  — confirm waiver [VERIFY]

**Common issues (guarantor perspective):**

- Payment guaranty with no requirement for lender to exhaust borrower remedies first (YELLOW)
- Continuing guaranty covering future amendments without guarantor consent (RED — changes
  should require guarantor approval or be limited to pre-authorized increases)
- Waiver of set-off rights including amounts genuinely owed to guarantor by lender (YELLOW)
- No cap on guaranty obligation in a group structure where only certain entities benefit
  from the facility (YELLOW — consider financial assistance / corporate benefit analysis)

---

### 12. Intercreditor Arrangements

**Key elements:**

**First lien / second lien structure:**

- **Payment subordination**: second lien lenders paid only after first lien paid in full
  (in enforcement scenarios); current pay of second lien interest typically permitted
  unless EOD is continuing
- **Lien subordination**: second lien security subordinate to first lien security
- **Standstill period**: second lien lenders cannot enforce security for a defined
  standstill period (typically 90-180 days) after an EOD — allows first lien lenders
  to take enforcement action; second lien can enforce after standstill expires
- **Purchase option**: first lien lenders typically have option to purchase second lien
  debt at par before second lien enforces

**Unitranche / FLFO (first-out / last-out) structure:**

- Single credit agreement; internal priority governed by Agreement Among Lenders (AAL)
- **First-out lenders**: receive priority on interest, amortization, and prepayment
  payments; typically hold the revolving facility
- **Last-out lenders**: receive higher margin to compensate for subordination; hold
  term loan (often the majority of the debt)
- 2024 market: unitranche large-cap activity reached $210 billion (>100% increase from 2023) [VERIFY — Chambers Global Practice Guides Private Credit 2025]
- AAL often provides last-out lenders with enhanced rights vs. traditional intercreditor
  (where last-out hold size is large majority of total debt)
- Enforcement waterfall under AAL: first-out lenders paid priority on enforcement;
  last-out lenders receive residual

**Common issues:**

- Standstill period too long (> 180 days) — prevents timely enforcement action (lender
  concern) or too short (< 90 days) — doesn't allow adequate restructuring time
- Purchase option price set at par but second lien lenders have hedging positions that
  make par exit unattractive
- AAL voting provisions: first-out lender veto rights on enforcement decisions not
  aligned with last-out lenders' economic interests
- No intercreditor when capital structure has multiple tranches (RED — priority disputes
  will be resolved by general insolvency law which may not reflect deal intent)
- Releases of security by first lien agent not automatically binding on second lien in
  enforcement scenario (drafting gap — RED)

---

### 13. Assignment and Participation

**Key elements:**

- **Borrower consent to lender assignments**: LMA/LSTA market standard — borrower
  consent required for initial assignments by lenders to third parties (but typically
  not for assignments to other lenders / affiliates / related funds)
- **Consent mechanics**: Consent deemed given if not refused within 10 business days
  (LMA) or 5 business days (LSTA) — "deemed consent" mechanism
- **Disqualified institution (DI) list**: In US leveraged finance, borrower can designate
  a list of entities (competitors, known hostile purchasers) who cannot receive assignment
  or participation — key borrower protection in sponsor-backed deals
- **Specified Discount Purchaser (SDP)**: In LSTA market, borrower or sponsor may
  designate an entity that can purchase loans at a discount — allows open-market
  buyback [VERIFY LSTA MCAPs July 2024]
- **Participations**: Lender can grant a participation to a third party without borrower
  consent; participant has no direct relationship with borrower; only voting rights that
  pass through to participant are typically unanimous consent matters
- **Reg K (US)**: Restrictions on foreign bank branching / lending; affects ability of
  foreign banks to hold certain loan positions in the US [VERIFY]

**Common issues (borrower perspective):**

- No DI list mechanism in a US leveraged deal (RED — competitors may acquire debt)
- Consent deemed given too quickly (5 business days) — not enough time for borrower
  to evaluate proposed assignee
- No restriction on assignment to distressed debt funds / loan-to-own investors (YELLOW)
- EU CSCD requirements for loan transfers involving EU obligors not addressed (YELLOW
  for EU-originated loans)

**Common issues (lender perspective):**

- Borrower consent requirement for assignments within the same credit group unreasonable
- No "yank-a-bank" provision to force non-consenting lenders out on amendment votes
  (see § 14)

---

### 14. Amendment and Waiver Mechanics

**Key elements:**

- **Required Lenders threshold**: Lenders holding > 50% (bilateral) or ≥ 66⅔%
  (syndicated, LMA) or ≥ 51% (LSTA leveraged) of commitments can approve non-unanimous
  amendments and waivers; some agreements use ≥ 50% (simple majority)
- **Unanimous consent matters** ("sacred rights" or "all-lender matters"): typically
  require 100% lender consent: (i) extension of maturity, (ii) reduction of principal,
  (iii) reduction of interest rate or fees, (iv) release of all/substantially all
  security, (v) release of all/substantially all guarantors, (vi) changes to the
  amendment mechanics themselves, (vii) pro rata sharing modifications
- **Yank-a-bank**: Required Lenders can replace a non-consenting lender on an
  amendment vote at par (or at a premium in some structures) — eliminates ability of
  minority lender to hold out and block amendments
- **Snooze-you-lose**: Lenders who fail to respond to an amendment request within the
  voting period are deemed to have voted with the majority / their votes are excluded
  from the denominator — prevents passive blocking
- **Affected lender provisions**: Certain amendments affecting only specific lenders
  require that lender's consent even if they are not a "sacred rights" matter

**Common issues (borrower perspective):**

- Required Lenders threshold too high (75%+ instead of 66⅔%) — harder to get amendments
  approved when lender syndicate is fragmented (YELLOW)
- No yank-a-bank provision — single blocking minority lender can hold up routine
  amendments (YELLOW)
- Unanimous consent matters too broadly drafted — ordinary commercial amendments
  inadvertently classified as requiring 100% consent (YELLOW)
- No snooze-you-lose mechanism — absent lenders block amendments (YELLOW)

**Common issues (lender perspective):**

- Required Lenders threshold too low — majority can approve changes that impair minority
  lender's economic position (YELLOW)
- Sacred rights not comprehensive enough — material changes possible without full consent
- Yank-a-bank price set at par could be used to punish lenders who vote in good faith
  against harmful amendments

---

### 15. Syndicate and Agency Provisions

**Key elements:**

- **Administrative agent**: appointment; duties (ministerial only in most LMA/LSTA
  forms); limitation of liability; right to resign and be replaced; no fiduciary duty
  to lenders absent express provision
- **Collateral agent**: separate from administrative agent in some structures; holds
  security on trust for the benefit of all secured parties
- **Defaulting lender**: lender that fails to fund its commitment; mechanics for
  handling defaulting lender's share (LSTA MCAPs July 2024 govern)
- **Fronting bank exposure**: issuing bank for letters of credit / swingline lender
  exposed if revolving lender defaults on participation obligation; agreement must
  require cash collateralization or repayment of defaulting lender's share
- **Pro rata sharing**: payments received by lenders distributed on a pro rata basis
  by commitment; lenders receiving more than their share must share with the syndicate
  (clawback obligation)

**Common issues:**

- No clear defaulting lender mechanics — failure of a lender to fund creates uncertainty
  for agent and borrower (RED)
- Fronting bank exposure not addressed — issuing bank has uncovered exposure if revolving
  lender defaults (RED for the fronting bank)
- Agent indemnification by lenders covers agent fraud or gross negligence — creates
  moral hazard (YELLOW)
- No successor agent process — current agent can resign leaving syndicate without
  administrative function (YELLOW — ensure reasonable replacement mechanics)

---

### 16. ESG and Sustainability-Linked Provisions

**Key elements:**

**Sustainability-linked loans (SLL) — LMA/LSTA SLL Principles:**

- Margin ratchet tied to performance against agreed Key Performance Indicators (KPIs)
  and Sustainability Performance Targets (SPTs)
- Margin decreases upon achievement of SPTs; increases if no SPTs met
- LMA SLL Provisions: highest margin reduction on satisfaction of 4 SPTs; step-down
  by SPT satisfaction count [VERIFY LMA SLL Provisions]
- Annual sustainability compliance certificate required

**Green loans — LMA November 2024 Green Loan Draft Provisions:**

- Use of proceeds strictly limited to financing or refinancing green projects
- LMA Green Provisions published November 7, 2024 — bolt-on to standard LMA facility
- No margin adjustment recommended (unlike SLLs) — standard LMA interest mechanics apply
- Green project categories defined in the LMA Green Loan Principles [VERIFY]

**Common issues:**

- KPIs not independently verifiable or audited — greenwashing risk (YELLOW)
- SPTs set too low — margin ratchet provides no real incentive (YELLOW — ESG integrity
  risk for borrower / regulatory risk in EU)
- No external review / second-party opinion on SLL framework (YELLOW per LMA guidance)
- SLL provisions not linked to facility covenants — margin penalty for missing SPTs is
  the only consequence (may be insufficient to drive behavior change)
- Green loan provisions not ring-fencing proceeds in a dedicated account — use-of-proceeds
  monitoring risk (YELLOW)
- EU taxonomy compliance not addressed for green loans in EU context [JURISDICTION-SPECIFIC]

---

## Deviation Severity Classification

### GREEN — Acceptable / Market Standard

The clause aligns with or is more favorable than market standard from the reviewing
party's perspective. Minor variations that are commercially reasonable.

**Examples:**

- SOFR hardwired fallback language adopted (borrower-favorable vs. amendment approach)
- Cross-acceleration (not cross-default) — borrower-favorable
- Springing covenant with 35% revolving facility draw threshold
- Equity cure permitted up to 5 times over loan life

**Action**: Note for awareness. No negotiation needed.

### YELLOW — Negotiate

The clause falls outside the preferred position but within a negotiable range. Common
in the market but not optimal for the reviewing party.

**Examples:**

- Cross-default instead of cross-acceleration (LMA standard; LSTA leveraged often
  cross-acceleration)
- ECF sweep at 75% with no step-down (negotiate step-down to 50% / 25%)
- Make-whole on voluntary prepayment with no call protection alternative
- Compliance certificate delivered with quarterly accounts only (lender may want monthly
  during distress)

**Action**: Generate specific redline. Provide fallback position. Estimate impact of
accepting vs. negotiating.

### RED — Escalate

The clause poses material risk to the reviewing party. Requires senior banking counsel
review.

**Examples:**

- MAC representation includes "prospects" — courts rarely uphold MAC; inclusion creates
  false confidence for lender / undue risk for borrower
- Cross-default threshold below $1M for a large borrower — any minor default triggers
- Make-whole on mandatory prepayment from asset disposal proceeds — not market standard
- Missing DACA for deposit accounts in a secured facility — perfection failure
- Copyright security not recorded at US Copyright Office for registered works — perfection
  failure
- Equity cure: no cure right in a maintenance covenant deal for a sponsor-backed borrower

**Action**: Explain specific risk with legal basis. Provide market-standard alternative.
Estimate exposure. Recommend escalation to senior banking counsel.

### CRITICAL — Deal Breaker

The issue must be resolved before drawdown can occur. Proceeding without resolution
exposes the reviewing party to material financial or legal loss.

**Examples:**

- No governing law clause — enforceability uncertainty
- Mandatory perfection actions not completed (UCC-1 not filed; DACA not executed)
- Financial covenant threshold impossible to comply with on day one
- No intercreditor agreement in a two-tranche structure — priority ambiguity
- Applicable interest rate clearly in excess of state usury limit (for non-preempted
  lending) — void ab initio risk

**Action**: Halt drawdown recommendation. Escalate immediately. Resolve before proceeding.

---

## Redline Format

For each YELLOW and RED deviation:

```
**Clause**: [Section reference and clause name]
**Current language**: "[exact quote from the agreement]"
**Issue**: [1-sentence description of the problem]
**Proposed redline**: "[specific alternative language]"
**Rationale**: [1-2 sentences, suitable for external sharing with counterparty's counsel]
**Legal basis**: [Specific statute, regulation, case, or market standard — or "LMA/LSTA
  market standard" with [VERIFY] if uncertain]
**Priority**: [Tier 1 (must-have) / Tier 2 (should-have) / Tier 3 (nice-to-have)]
**Fallback**: [Alternative position if primary redline is rejected]
```

---

## Negotiation Priority Framework

### Tier 1 — Must-Haves (Deal Breakers)

Issues where the reviewing party cannot proceed without resolution:

- Perfection failures in security documents
- Interest rate in excess of applicable usury limit
- Financial covenants impossible to comply with at signing
- Missing intercreditor agreement in a multi-tranche structure
- SOFR/SONIA fallback language absent in a floating-rate facility
- Equity cure mechanics absent in a maintenance covenant deal (sponsor-backed)
- Broad MAC definition in CPs to each drawdown — lender can arbitrarily refuse funding

### Tier 2 — Should-Haves (Strong Preferences)

Issues that materially affect risk but have negotiation room:

- Cross-acceleration vs. cross-default
- Make-whole scope (voluntary vs. mandatory prepayment)
- ECF sweep percentage and step-down
- EBITDA add-back caps
- DI list / Specified Discount Purchaser mechanics (sponsor-backed deals)
- Equity cure: EBITDA cure vs. debt cure; cure cap and frequency
- Required lender threshold for amendments

### Tier 3 — Nice-to-Haves (Concession Candidates)

Issues that improve the position but can be conceded:

- Reporting deadlines (45 vs. 60 days for quarterly accounts)
- Minor definitional adjustments
- Compliance certificate form and timing
- Insurance certificate mechanics
- Snooze-you-lose mechanics (vs. express required lender threshold)

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                             | Fail Action                                                   |
| -------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, market standard, or case | Add citation or mark "[UNVERIFIED — counsel to confirm]"      |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction      | Fix format                                                    |
| **Currency**   | Every cited provision checked for amendments or repeal                           | Flag "[CHECK CURRENCY — may have been amended or superseded]" |
| **Domain**     | Analysis stays within the agreement's governing law; no jurisdictional bleed     | Remove or flag jurisdictional contamination                   |
| **Confidence** | Uncertainty explicitly stated, not hidden                                        | Add confidence qualifier                                      |

### Self-Interrogation for RED and CRITICAL Items

For any RED or CRITICAL classification, apply this 3-pass self-interrogation:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the
cited statute/regulation/case? Would a court in this jurisdiction reach this conclusion?
What will the counterparty's counsel argue in response?

**Pass 2 — Completeness**: Have all relevant statutes, regulations, and cases been
considered? Are there regulatory dimensions (UCC, SOFR transition rules, FCARs,
CSCD) not yet addressed?

**Pass 3 — Challenge**: What is the strongest argument that this clause is acceptable?
Under what commercial circumstances might a reasonable banking lawyer accept this risk?
Is the RED / CRITICAL classification proportionate?

If any pass reveals a weakness, revise before delivery. Mark the audit trail
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                          | Action                                                       |
| ------------ | --------- | ------------------------------------------------ | ------------------------------------------------------------ |
| **Definite** | 0.95-1.0  | Settled market practice; clear statute           | State with confidence                                        |
| **High**     | 0.80-0.94 | Strong authority; minor interpretation questions | State with brief caveat                                      |
| **Probable** | 0.60-0.79 | Good arguments; reasonable minds could differ    | State with explicit reasoning                                |
| **Possible** | 0.40-0.59 | Genuinely uncertain; competing authorities       | Flag for senior counsel review                               |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative                          | Do not assert; flag "[UNCERTAIN — senior counsel to advise]" |

---

## Glass Box Audit Trail

Every review output MUST include a Glass Box audit section:

```yaml
glass_box:
  agreement: "[Facility Agreement title and date]"
  facility_type: "[Term Loan A / TLB / RCF / Unitranche / First Lien / Other]"
  reviewing_party: "[Borrower / Lender / Agent / Intercreditor party]"
  governing_law: "[English law (LMA) / New York law (LSTA) / Other]"
  deal_context: "[Leveraged / Investment Grade / ABL / Private Credit / Other]"
  clauses_reviewed: 16
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  case_law_consulted:
    - "[Case — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  market_standards_applied:
    - "[LMA / LSTA / Other — with relevant edition/date]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  financial_covenant_headroom: "Assessed / Not assessed (requires financial data)"
  perfection_analysis_completed: "Yes (US UCC Article 9) / Yes (UK FCARs) / Not applicable / Partial"
  limitations:
    - "[Any scope limitations, missing schedules, or caveats]"
  reviewer: "AI-assisted — requires qualified banking & finance legal review"
```

---

## Multi-Stakeholder Mapping

For every loan agreement, identify ALL affected stakeholders:

| Stakeholder           | Role                  | Affected Clauses                      | Key Interests                                                 |
| --------------------- | --------------------- | ------------------------------------- | ------------------------------------------------------------- |
| Borrower              | Principal obligor     | All                                   | Minimize constraints; covenant flexibility; prepayment rights |
| Guarantors            | Secondary obligors    | Guaranty; security; EODs              | Limit guaranty scope; obtain guarantor-specific protections   |
| Administrative agent  | Syndicate coordinator | Agency; assignment; defaulting lender | Limitation of liability; resignation rights                   |
| Lead arrangers        | Underwriting risk     | Pricing; market flex                  | Market flex provisions; syndication risk                      |
| Syndicate lenders     | Funded exposure       | All — pro rata share                  | Pro rata treatment; sacred rights protections                 |
| Intercreditor parties | Junior / mezzanine    | Intercreditor; prepayment; EOD        | Standstill; purchase option; enforcement rights               |
| Collateral agent      | Security holder       | Security; collateral                  | Proper perfection; indemnification                            |
| Regulators            | Prudential oversight  | Interest; compliance                  | AML/KYC; Basel III/IV capital treatment                       |
| CSCD / NPL purchasers | Secondary market      | Assignment; CSCD compliance           | Authorisation requirements; proper notification               |

---

## Anti-Patterns

Explicit catalogue of what NOT to do in loan agreement review:

1. **Treating EBITDA as a number, not a definition** — The EBITDA definition is the
   most important number in the agreement. Reviewing covenant compliance without reading
   every word of the EBITDA definition (and its add-back schedule) is a fundamental error.
   Add-backs can inflate EBITDA by 30-50%; whether they do so legally requires careful
   analysis of each item.

2. **Conflating cross-default and cross-acceleration** — These are fundamentally
   different in their breadth and risk profile. Cross-default triggers on any other
   default regardless of lender action; cross-acceleration triggers only on another
   lender's decision to accelerate. This distinction can mean the difference between
   a technical issue and a catastrophic default cascade.

3. **Assuming SOFR and LIBOR are equivalent** — Post-LIBOR benchmark transition is not
   cosmetic. SOFR is a risk-free rate (no credit premium); LIBOR incorporated credit
   risk. The credit spread adjustment (ARRC recommended: 26.161 bps for 3-month SOFR)
   is not universal — verify the applicable CSA in the agreement. Missing or wrong CSA
   affects total interest cost.

4. **Missing the definitions cross-reference trap** — Loan agreement covenants are
   only as strong as their definitions. "Permitted Debt" may reference "Permitted Liens"
   which references "Permitted Investments" in a circular chain. Always trace the
   definitional chain for every covenant basket.

5. **Ignoring UCC continuation requirements** — UCC-1 financing statements expire 5
   years after filing. A security interest that was perfectly perfected at origination
   may become unperfected if the continuation filing is missed. For long-dated facilities,
   verify that continuation filing obligations are in the agreement and monitored.

6. **Applying FCARs without confirming scope** — UK Financial Collateral Arrangements
   Regulations 2003 provide powerful enforcement rights (appropriation without court order).
   But FCARs only apply to "financial collateral" (cash, financial instruments, credit
   claims) and only between "non-natural persons." If the collateral includes real property
   or general trade receivables, FCARs do not apply and full court process is required.

7. **Treating the MAC clause as an effective lender remedy** — English and US case law
   has consistently held that MAC/MAE clauses are very difficult to invoke successfully.
   A lender relying on a MAC EOD without additional EODs is taking significant enforcement
   risk. Analyze what other EODs are available alongside MAC.

8. **Reviewing guaranty without checking governing law suretyship rules** — Guarantor
   discharge rules (Holme v. Brunskill in England; Restatement Third of Suretyship in US)
   can render guaranties unenforceable if the principal obligation is amended without
   guarantor consent. Verify whether the guaranty contains adequate waivers of these
   suretyship defenses.

9. **Ignoring the Copyright Office perfection requirement for registered copyrights** —
   UCC-1 alone does not perfect a security interest in registered copyrights (Copyright
   Act § 205 preemption). A borrower in the media, software, or content industry may
   have its most valuable assets (registered copyrights) inadequately secured if lender's
   counsel recorded only a UCC-1.

10. **Applying usury analysis without confirming preemption** — Federal preemption of
    state usury limits under the National Bank Act does not automatically extend to
    non-bank assignees (Madden v. Midland Funding). For loans originated by national banks
    but purchased by non-banks or fintechs, verify whether the OCC valid-when-made rule
    resolves preemption risk in the relevant jurisdiction.

11. **Missing intercreditor priority analysis in a multi-tranche structure** — The
    intercreditor agreement determines who gets paid first in enforcement. Without
    carefully reading both the loan agreement and the intercreditor agreement together,
    the review of either in isolation may be fundamentally misleading.

12. **Treating all ESG margin ratchets as equivalent** — Sustainability-linked loan
    provisions with poorly defined KPIs or low SPTs may constitute greenwashing (EU
    Green Bond Standard; ESMA greenwashing guidelines). The reviewing party (especially
    a lender) faces regulatory and reputational risk if the SLL framework is cosmetic.

13. **Accepting "ordinary course" carve-outs without definition** — Permitted liens,
    permitted debt, and permitted disposals often carve out "ordinary course" transactions.
    Without a definition, "ordinary course" is contested and creates enforcement ambiguity.

14. **Ignoring equity cure mechanics in a sponsor-backed deal** — For leveraged buyout
    financing, equity cure mechanics are not optional — they are the primary mechanism
    for financial covenant compliance management. A maintenance covenant deal without
    equity cure mechanics is highly unusual and likely a drafting error that needs
    correction pre-signing.

15. **Reviewing loan terms without checking the fee letter** — Arrangement fees,
    commitment fees, structuring fees, and agency fees often appear in a separate fee
    letter that is not included in the main facility agreement. Without the fee letter,
    the total cost of the facility cannot be assessed.

16. **Assuming mandatory prepayment make-whole is standard** — Make-whole premiums
    on voluntary prepayments are common in certain loan types (US private placements,
    Term Loan A). However, make-whole on mandatory prepayments (asset sale proceeds,
    excess cash flow sweeps) is not market standard and represents a significant
    borrower-unfavorable deviation that should be flagged RED.

17. **Failing to flag the DI list / assignment restriction gap in a sponsor deal** —
    In a US sponsor-backed leveraged loan, the Disqualified Institution list protects
    the borrower from hostile debt purchasers (competitors, loan-to-own funds). Absence
    of DI mechanics in a sponsored deal is a significant omission that should be raised
    with the sponsor's legal team.

---

## Writing Standards

Apply plain-language discipline to all output:

**For redline rationales** (shared with counterparty's counsel):

- Active voice: "The current language allows the lender to refuse drawdown on subjective
  MAC grounds" not "Drawdown can be refused on MAC grounds"
- Specific, not vague: "This is inconsistent with LMA market standard" is not enough —
  explain exactly what the market standard is and why this clause deviates
- Cite the authority: LMA recommendation, LSTA MCAPs provision, or specific case

**For internal analysis:**

- Include technical financial and legal analysis
- Confidence qualifiers where appropriate
- Glass Box audit trail appended

**Quality gates before delivery:**

1. Can a non-specialist in-house counsel understand the executive summary?
2. Can the counterparty's banking counsel understand and respond to each redline?
3. Is every legal claim backed by a specific citation (statute, case, market standard,
   or flagged [VERIFY])?
4. Has every financial covenant been reviewed with the actual EBITDA definition in mind
   (not a generic definition)?
5. Have all UCC/FCAR/CSCD perfection requirements been addressed for secured facilities?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- Step 4: Search for jurisdiction-relevant statutes, regulations, and case law
- Save results to `/tmp/legalcode-loan-review-authority.md`
- For RED items: search for additional case law to support or challenge classification
- Check statutory currency (amendments to UCC Article 9, SOFR transition rules,
  CSCD implementation status by member state, California anti-deficiency rules)
- Mark all legalcode-mcp citations as VERIFIED in Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus on structural analysis, market standard comparison, and drafting quality
  rather than legal authority depth

---

## Output Format Template

```markdown
## Loan Agreement Review Summary

**Document**: [Facility Agreement — [Borrower] — dated [date]]
**Facility**: [Revolving Credit Facility / Term Loan A / TLB / Unitranche — $[X]M]
**Parties**: [Borrower: [name] | Agent: [name] | Original Lenders: [list or count]]
**Reviewing For**: [Borrower / Lender / Other]
**Governing Law**: [English law (LMA) / New York law (LSTA) / Other]
**Deal Context**: [Leveraged buyout / Investment grade / ABL / Private credit / Other]
**Review Basis**: [LMA market standard / LSTA market standard / Organizational playbook]
**Date of Review**: [date]

---

## Risk Profile: [HIGH / MEDIUM / LOW] from [reviewing party]'s perspective

---

## CRITICAL Issues (Resolve Before Drawdown)

[List any CRITICAL items — must resolve before execution]

---

## Key Findings — RED (Escalate)

[Top RED issues with one-line summaries and legal basis]

---

## Issues to Negotiate — YELLOW

[Summary of YELLOW items organized by priority tier]

---

## Missing Clauses

[List of the 16 categories not present, with severity assessment]

---

## Clause-by-Clause Analysis

### [Clause Category] — [GREEN / YELLOW / RED / CRITICAL] | Confidence: [level]

**Agreement says**: [summary of the provision with key defined terms]
**Market standard**: [LMA/LSTA standard position]
**Issue**: [specific deviation from market standard or reviewing party's preferred position]
**Recommendation**: [specific redline or accept]
**Legal basis**: [Statute / case / market standard — VERIFIED or [VERIFY]]
**Priority**: [Tier 1 / 2 / 3]
**Fallback**: [Alternative position if primary redline rejected]

---

## Negotiation Strategy

[Sequencing recommendations; what to lead with; what to concede]

## Financial Covenant Note

[Summary of financial covenant headroom if assessable from the document]

## Security Perfection Note

[Summary of perfection analysis — UCC/FCARs/CSCD — with any gaps flagged]

---

[Glass Box Audit Trail — YAML block]
```

---

## Localization Notes

When reviewing a loan governed by a specific jurisdiction, supplement this skill with:

- **English law**: LMA Facility Agreement documentation (primary investment grade,
  leveraged, and real estate editions); Insolvency Act 1986 set-off rules; Companies
  Act 2006 charges registration; FCARs 2003 (SI 2003/3226) scope verification
- **New York law**: LSTA Model Credit Agreement Provisions (MCAPs, updated July 2024);
  UCC Article 9 as enacted in New York; New York Banking Law foreign bank restrictions
- **Delaware law (borrower-side)**: DGCL corporate authority; no special lending law
- **California**: CCP anti-deficiency statutes (§§ 580a-580e) for real property secured
  loans; Labor Code § 2870 for IP assignment carveouts in guaranty analysis
- **EU loans**: CSCD (Directive 2021/2167) — check implementation status by member state
  as of December 2023 deadline; ECB guidance for institutional lenders; EMIR for hedging
- **Dual-currency / multi-jurisdiction**: Note that governing law choice affects security
  enforcement, insolvency treatment, and usury compliance separately

---

## Provenance

Created by Legalcode (2026-03-02). Legalcode original synthesis — created via 2-agent
parallel research pipeline covering LMA and LSTA market standards, UCC Article 9 and
UK FCARs security perfection requirements, EU Credit Servicers Directive 2021/2167,
SOFR/SONIA post-LIBOR benchmark transition, financial covenant mechanics (EBITDA
definition, equity cure), event of default case law (BM Brazil I [2024], Grupo Hotelero
[2013]), Madden v. Midland Funding / valid-when-made doctrine, intercreditor arrangements
(unitranche FLFO, Agreement Among Lenders, 2024 $210B market data), disqualified
institution lists, yank-a-bank and snooze-you-lose mechanics, LMA Green Loan Draft
Provisions (November 2024), LSTA MCAPs (July 2024), and LSTA Complete Credit Agreement
Guide. Covers US/UK/EU jurisdictions with [JURISDICTION-SPECIFIC] markers throughout.
