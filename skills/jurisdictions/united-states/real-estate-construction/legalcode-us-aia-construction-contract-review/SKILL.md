---
name: legalcode-us-aia-construction-contract-review
description: Review US construction contracts with emphasis on AIA standard forms (A101, A102, A133, A201
  General Conditions, A401 Subcontract) and US owner-contractor risk allocation. Covers scope of work
  and contract sum mechanics, change orders and constructive changes, schedule and delay risk, retainage
  and payment applications, liquidated damages, insurance and performance/payment bonds, indemnification
  and anti-indemnity statutes, mechanic's lien exposure, substantial and final completion, and dispute
  forum strategy under AIA Article 15. Use when reviewing AIA prime contracts, subcontracts, ConsensusDocs,
  or owner-modified AIA forms on US commercial, institutional, healthcare, or public construction projects.
  Flags deviations from AIA standard, classifies risk (GREEN/YELLOW/RED), generates redlines with AIA
  fallback language, and produces a confidence-scored, auditable analysis. Also applies to CM-at-Risk
  (A133) and Design-Build delivery variants. Supports both owner-side and contractor-side review.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode US AIA Construction Contract Review

> **Disclaimer**: This skill provides a framework for AI-assisted review of US construction
> contracts. It does not constitute legal advice. All outputs must be reviewed by a qualified
> construction attorney licensed in the relevant US state before use. AIA document versions
> differ materially (A201-2017 vs. A201-2007 vs. earlier editions); verify which version
> governs. State lien laws, anti-indemnity statutes, and prompt-payment acts vary by
> jurisdiction — no provision stated here should be relied on without state-specific
> verification. Statutory and case law references cited from memory carry hallucination
> risk; verify against authoritative sources.

---

## Purpose and Scope

This skill reviews US construction contracts against AIA standard form baselines and
owner/contractor negotiation playbooks. It identifies deviations from AIA standard
language, classifies their severity, generates actionable redlines with AIA alternative
language, and produces a confidence-scored, auditable analysis.

**Covers:**

- Clause-by-clause analysis against AIA A201-2017 General Conditions baseline
- AIA contract family identification (A101, A102, A133, A401, B101) and version verification
- Delivery method risk mapping (Design-Bid-Build, CM@Risk, Design-Build)
- Change order and constructive change risk (AIA Article 7)
- Schedule, float, delay, and acceleration risk
- Payment, retainage, and prompt payment act compliance
- Liquidated damages enforceability (US penalty doctrine)
- Insurance program review (CGL, builder's risk, performance/payment bonds)
- Indemnification analysis with anti-indemnity statute overlay by state
- Mechanic's lien exposure and lien waiver strategy
- Dispute resolution pathway (AIA Article 15: IDM → Mediation → Arbitration/Litigation)
- Owner-side vs. contractor-side risk classification
- GREEN / YELLOW / RED deviation classification with automatic RED triggers

**Does not:**

- Draft new AIA contracts or prepare supplementary conditions from scratch
- Provide legal advice or replace qualified construction law counsel
- Substitute for specialist review of public contracting (FAR/DFAR compliance), federal
  Davis-Bacon Act wage issues, environmental remediation contracts, or nuclear construction
- Apply outside the United States — for international projects see `legalcode-construction-contract-review`

---

## Jurisdiction and Governing Law

**Primary jurisdiction**: United States (federal principles + state-specific overlays).

All US construction contracts are governed by the law of a specific state. The skill
applies a federal/common-law baseline and layers in state-specific statutes.

### Federal Statutes (Apply on Federal Projects) [VERIFY currency]

| Statute                                            | Relevance                                                            |
| -------------------------------------------------- | -------------------------------------------------------------------- |
| Miller Act, 40 U.S.C. §§ 3131–3134                 | Performance + payment bonds required on federal contracts > $150,000 |
| Federal Prompt Payment Act, 31 U.S.C. §§ 3901–3907 | Governs payment timing on federal construction                       |
| Davis-Bacon Act, 40 U.S.C. §§ 3141–3148            | Prevailing wage requirements on federally funded projects            |
| Buy America Act / Buy American Act                 | Domestic materials requirements on federally funded projects         |
| OSHA Act (29 C.F.R. Part 1926)                     | Federal construction safety standards                                |
| Contract Disputes Act, 41 U.S.C. §§ 7101–7109      | Dispute resolution on federal contracts                              |

### State-Level Statutes (Apply on Private and State Public Projects)

Identify the project's state at Step 2 and apply:

| Area                           | Key State-Law Variation Points                                                                        |
| ------------------------------ | ----------------------------------------------------------------------------------------------------- |
| **Mechanic's Liens**           | Preliminary notice deadlines, lien filing deadlines, enforcement timelines all vary by state          |
| **Retainage Limits**           | Many states cap retainage (e.g., California 5%, Texas 10% → 5% at 50%, New York 5%) [VERIFY by state] |
| **Prompt Payment**             | Every state has a prompt payment act; interest rates and cure periods vary                            |
| **Anti-Indemnity Statutes**    | 44+ states restrict broad-form indemnity in construction; see Anti-Indemnity Matrix below             |
| **Statutes of Repose**         | Construction defect repose periods vary: 4 years (Florida) to 10 years (Massachusetts, Ohio) [VERIFY] |
| **Arbitration Enforceability** | Most states follow Federal Arbitration Act; a few limit mandatory arbitration in construction         |
| **Little Miller Acts**         | State equivalents of the Miller Act for state public projects vary in thresholds and scope            |

---

## AIA Contract Family Reference

### Form Identification Guide

Identify which AIA form governs before beginning any analysis. The choice of form
determines the pricing structure, risk allocation, and applicable supplements.

| AIA Form      | Full Name                                     | Delivery Method                 | Pricing Structure                                    |
| ------------- | --------------------------------------------- | ------------------------------- | ---------------------------------------------------- |
| **A101-2017** | Owner-Contractor Agreement (Stipulated Sum)   | Design-Bid-Build                | Fixed lump sum; owner bears design risk              |
| **A102-2017** | Owner-Contractor Agreement (Cost Plus + GMP)  | CM@Risk / Design-Build          | Cost of Work + Fee + GMP ceiling                     |
| **A133-2019** | Owner-CM as Constructor Agreement             | CM@Risk                         | Cost of Work + Fee + GMP (CM advisory → constructor) |
| **A201-2017** | General Conditions of the Contract            | All (incorporated by reference) | N/A — governs procedures, not price                  |
| **A401-2017** | Contractor-Subcontractor Agreement            | All                             | Mirrors prime contract delivery method               |
| **B101-2017** | Owner-Architect Agreement                     | All                             | Architect services + construction administration     |
| **A104-2017** | Abbreviated Owner-Contractor (Stipulated Sum) | Small projects                  | Fixed lump sum; simplified A201                      |

**Version Alert**: AIA updates forms periodically. Common legacy versions in use:

- A201-2007 (widely used; differs significantly from A201-2017 on claims process)
- A101-2007, A102-2007, A133-2009

**⟁ CLARIFY** — Always confirm the AIA version year. If the contract incorporates A201
by reference without specifying a year, ask the user to confirm which edition applies.

### Document Hierarchy

```
Owner ←→ Architect (B101-2017)
           ↓ Architect administers contract, acts as Initial Decision Maker
Owner ←→ General Contractor (A101/A102/A133 + A201 General Conditions)
           ↓ A201 obligations flow down via A401
Contractor ←→ Subcontractors (A401 + incorporated A201)
```

**Flow-Down Rule**: A401 incorporates A201 General Conditions by reference. Prime contract
supplementary conditions that modify A201 flow down to subcontractors only if expressly
incorporated. Review A401 § 5.3 and supplementary conditions for flow-down scope.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- Multiple valid approaches exist and user preference matters
- Risk classification depends on business context only the user can provide
- State-specific law requires identifying which state governs

Use the **⟁ CLARIFY** pattern (structured options with descriptions) wherever marked.
If the user has already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept the Contract

Accept the construction contract in any format:

- **File**: PDF, DOCX, or other document
- **URL**: Link to a contract document or CLM system
- **Pasted text**: Contract text pasted directly

If no contract is provided, prompt the user to supply one. If the contract references
and incorporates other documents (AIA A201 general conditions, supplementary conditions,
specifications, drawings), ask whether those documents are available for review.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask:

1. **Which side are you on?**
   - Options: **Owner** | **General Contractor** | **Subcontractor** | **Surety / Bonding Company** | **Lender** | **Other**
   - _Why this matters_: The risk analysis is mirror-image — provisions favorable to the owner are adverse to the contractor and vice versa.

2. **Project state and type?**
   - State: [e.g., California, Texas, New York — determines mechanic's lien law, anti-indemnity, retainage cap, prompt payment act]
   - Project type: **Federal public** | **State/local public** | **Private commercial** | **Residential** | **Healthcare** | **Other regulated industry**
   - _Why this matters_: Miller Act bonds, Davis-Bacon wages, Little Miller Acts, and state prompt payment acts apply differently.

3. **AIA form and version?**
   - Form: A101 / A102 / A133 / Non-AIA / AIA-based with significant modifications
   - Version year: 2017 / 2007 / Earlier
   - _Why this matters_: AIA-2017 vs. AIA-2007 differ materially on claims timing and procedures.

4. **Contract value and project type?**
   - Options: Under $500K (small) / $500K–$5M (medium) / $5M–$50M (large) / Over $50M (major)
   - _Why this matters_: Bond thresholds, retainage practices, and negotiation dynamics shift with contract size.

5. **Focus areas?**
   - Options: Change order risk | Schedule and delay | Payment and retainage | Insurance and bonds | Indemnity and lien exposure | Dispute resolution | Full review
   - Allow multiple selections.

6. **Negotiation posture?**
   - Options: Highly negotiable (both sides willing to move) | Moderately negotiable (owner's form with limited changes) | Owner's "take it or leave it" form | Contractor-initiated modifications
   - _Why this matters_: Determines how many redlines to generate and the fallback strategy.

### Step 3: Identify the AIA Form and Version

Read the contract front matter. Identify:

- The AIA form number and edition year
- Whether A201 General Conditions are incorporated by reference or set out in full
- Whether supplementary conditions modify A201 (look for "Supplementary Conditions" document)
- Whether the contract uses ConsensusDocs instead of AIA — if so, note the form number and alert the user that the analysis below applies to AIA forms and material differences exist in ConsensusDocs

**Supplementary Conditions Alert**: Many owners modify AIA forms via supplementary conditions (SC). Identify every SC provision and flag modifications from AIA standard for separate analysis. SC modifications are the primary source of owner-favorable deviations from AIA balanced terms.

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** (if connected) to research:

- State mechanic's lien law (preliminary notice requirements, deadlines)
- State anti-indemnity statute (form and limitations)
- State retainage statute (cap and release requirements)
- State prompt payment act (timing and interest rate)
- State statute of repose for construction defects
- State little Miller Act thresholds (for public projects)
- Leading state case law on: constructive change doctrine, delay damages, liquidated damages enforceability, and AIA arbitration clause enforceability

Save results to `/tmp/legalcode-aia-review-authority.md`.

**If legalcode-mcp is not connected:**

- Proceed with analysis
- Mark all state-specific statutory references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — state law provisions require manual verification"`

### Step 5: Clause-by-Clause Analysis

Analyze the contract systematically against the 16 construction clause categories below.
Read the entire contract before flagging issues — construction clauses interact heavily
(e.g., a broad change order clause interacts with the claims notice provision and the
dispute resolution clause).

**⟁ CLARIFY** — For large contracts (over 50 pages, with multiple exhibits/specifications):

- Ask whether to perform a **full review** (all 16 categories) or a **priority review**
  focused on user's stated focus areas plus any automatic RED triggers.

#### Construction Clause Analysis Matrix

| #   | Category                               | Review Tier | Key AIA Reference              |
| --- | -------------------------------------- | ----------- | ------------------------------ |
| 1   | Scope of Work and Contract Documents   | Deep        | A201 § 1.1, A101 § 2           |
| 2   | Contract Sum and Pricing Mechanics     | Deep        | A101 § 4, A102 § 5, A201 § 9.1 |
| 3   | Change Orders and Constructive Changes | Deep        | A201 Article 7                 |
| 4   | Schedule and Time for Completion       | Deep        | A201 Article 8                 |
| 5   | Delay, Disruption, and Acceleration    | Deep        | A201 § 8.3, § 3.7.4, § 15.1    |
| 6   | Applications for Payment and Retainage | Deep        | A201 § 9.3–9.9, AIA G702/G703  |
| 7   | Substantial and Final Completion       | Deep        | A201 § 9.8–9.10, AIA G704      |
| 8   | Liquidated Damages                     | Deep        | A101 § 4.5                     |
| 9   | Insurance                              | Deep        | A201 Article 11                |
| 10  | Performance and Payment Bonds          | Deep        | A201 § 11.6, Miller Act        |
| 11  | Indemnification                        | Deep        | A201 § 3.18                    |
| 12  | Mechanic's Liens                       | Deep        | State law; A201 § 9.10.2       |
| 13  | Dispute Resolution                     | Deep        | A201 Article 15                |
| 14  | Termination                            | Standard    | A201 Article 14                |
| 15  | Design Liability and Shop Drawings     | Standard    | A201 § 3.12, § 3.2             |
| 16  | Subcontracting and Flow-Down           | Standard    | A201 Article 5, A401           |

---

## Clause Analysis Reference

### 1. Scope of Work and Contract Documents

**AIA Baseline**: A201 § 1.1 defines the Contract Documents as the Agreement, General
Conditions, Supplementary Conditions, Drawings, and Specifications. The Contract
Documents are complementary; anything required by one is binding as if required by all
(A201 § 1.2.1).

**Key elements to review:**

- Is the scope defined by reference to Drawings and Specifications, or by description only?
  Description-only scope creates constructive change risk.
- Does the contract clearly identify _all_ Contract Documents and their precedence order?
  Missing precedence clause creates interpretation disputes.
- Is there a design responsibility allocation? Who prepared the design? Is design liability
  on the architect (traditional DBB) or contractor (Design-Build)?
- Does the contract incorporate documents by reference that are not attached? (e.g.,
  "owner's project requirements," "BIM execution plan," "project manual") — obtain and review.
- Check for integration/entire agreement clause and whether it supersedes pre-bid representations.

**Common deviations from AIA standard:**

- Owner adds a document hierarchy favoring their documents over A201 (e.g., "Owner's
  Supplementary Conditions supersede A201 in all cases of conflict") — RED
- Scope defined as "all work reasonably inferable" without drawings/specs — YELLOW/RED
- BIM model added as a Contract Document with no clear status (informational vs. binding) — YELLOW
- Owner reserves right to issue additional drawings without change order — RED

**GREEN**: Contract Documents clearly identified, scope well-defined by drawings and
specifications, precedence clause balanced.

**YELLOW**: Scope partially description-based; some documents referenced but not attached;
precedence clause ambiguous.

**RED**: No drawings or specifications incorporated; scope is description-only; or owner
reserves unilateral right to expand scope without change order.

---

### 2. Contract Sum and Pricing Mechanics

**AIA Baseline (Stipulated Sum — A101)**: Contract Sum is a fixed lump sum. Increases
only via Change Order (CO) or Construction Change Directive (CCD). A201 § 9.1.

**AIA Baseline (Cost Plus + GMP — A102/A133)**: Contractor is paid Cost of Work plus
a negotiated Fee. GMP is the absolute ceiling. Savings below GMP may be shared. A102 §§ 5.1–5.3.

**Key elements to review:**

_Stipulated Sum (A101):_

- Are allowances itemized and defined? (A201 § 3.8 — allowance amounts are included in
  contract sum; actual cost substituted when selections finalized)
- Are unit prices established for potential scope additions? (A101 § 4.3)
- Is there a material escalation clause for extended projects? (AIA standard forms have none)
- Does the contract define what is included in general conditions costs?

_Cost Plus / GMP (A102/A133):_

- Is the GMP set as a hard ceiling? Are GMP adjustment triggers clear?
- Are reimbursable costs defined and limited? (A102 § 7 lists reimbursable costs)
- Is the contractor's Fee percentage defined, or is it a fixed amount? Does Fee change if
  scope changes?
- Is contingency within the GMP defined and who controls it?
- Do shared savings provisions accurately reflect negotiated splits?
- Are owner audit rights adequate (typically 3 years after final payment)?

**Common deviations from AIA standard:**

- Owner modifies A102 to make all savings owner's property, no contractor share — YELLOW
- GMP contingency controlled entirely by owner with no contractor access — YELLOW
- Cost reimbursement definitions narrowed to exclude common job-site expenses — RED
- No right to adjust GMP for Owner-caused delays or owner-directed changes — RED
- Material escalation risk placed entirely on contractor for multi-year projects — YELLOW/RED

---

### 3. Change Orders and Constructive Changes

**AIA Baseline**: A201 Article 7 establishes a three-tier mechanism:

- **Change Order (CO)**: Agreed change in Work, Contract Sum, or Contract Time — signed
  by Owner, Architect, and Contractor (A201 § 7.2)
- **Construction Change Directive (CCD)**: Owner-directed change when agreement cannot
  be reached — immediately binding pending resolution; price determined afterward (A201 § 7.3)
- **Minor Change in Work**: Architect-directed change without effect on Contract Sum or
  Time (A201 § 7.4)

**Key elements to review:**

_Notice Requirements:_

- A201-2017 § 15.1.2: Contractor must provide written notice of claims within **21 days**
  of the event giving rise to the claim, or within 21 days of first recognizing the
  condition. Failure to provide timely notice may bar the claim.
- Note: A201-2007 used 21 days for notice but had a different claims process overall.
- **⟁ CLARIFY** — If supplementary conditions modify the notice period (many owners shorten
  to 7 or 10 days), flag prominently and confirm with user.

_CCD Pricing:_

- A201 § 7.3.4: Compensation under a CCD is the contractor's actual costs plus overhead
  and profit (A201 § 7.3.4 lists allowable percentages: 15% overhead + profit on contractor's
  work, 10% on subcontractor's work)
- Does the contract modify these markup percentages? Many owners cap at lower amounts.

_Constructive Change Doctrine:_

- Not codified in AIA but recognized in US construction law: acts by the owner that
  effectively change the scope without a formal CO (e.g., rejection of conforming work,
  over-inspections, defective specs) give rise to an equitable adjustment claim. [VERIFY]
- Does the contract contain a waiver of constructive changes? — RED trigger

_Common deviations:_

- Notice period shortened to less than 14 days in supplementary conditions — YELLOW/RED
  (depending on complexity of project)
- Owner reserves right to unilaterally direct changes without CCD procedure — RED
- All change order requests subject to owner approval with no default resolution mechanism — RED
- Markup percentages reduced below AIA standard (especially below 10% combined) — YELLOW
- "No Damage for Delay" clause eliminating compensation for owner-caused delays — RED (see § 5)
- Change order dispute resolution waived in favor of forced continuation — RED

**Automatic RED Triggers — Change Orders:**

1. Waiver of constructive change claims
2. Change order notice period less than 7 days
3. No CCD mechanism — contractor must agree to all changes before proceeding
4. Overhead and profit markup eliminated or below 5%

---

### 4. Schedule and Time for Completion

**AIA Baseline**: A201 § 3.10 requires the Contractor to prepare and maintain a
construction schedule. The Contract Time is established in A101 § 3.1. Substantial
completion is the target date.

**Key elements to review:**

- Is Contract Time measured in calendar days from Notice to Proceed (NTP), or is it a
  fixed calendar date? Fixed calendar dates are riskier for contractor if NTP is delayed.
- Does the contract define "float" and who owns it? AIA standard is silent on float
  ownership — most US jurisdictions treat float as a project resource, but contract language
  can allocate it to either party. [VERIFY]
- Does the contract allow the owner to require a contractor to accelerate without additional
  compensation? — RED trigger if so
- Is there a baseline schedule approval process? If owner can reject schedules indefinitely,
  NTP may be de facto delayed.
- Are weather day provisions adequate for the project location and type? What is the
  definition of an "adverse weather day" that entitles an extension?

**Schedule-Related RED Triggers:**

1. Fixed completion date with no adjustment mechanism for owner-caused delays
2. Owner retains all float ("Project float belongs to Owner")
3. Constructive acceleration (forced to accelerate without formal change order)
4. NTP delayed beyond a reasonable period with no adjustment to completion date or contract sum

---

### 5. Delay, Disruption, and Acceleration

**AIA Baseline**:

- A201 § 8.3: Delays caused by the owner or architect entitle contractor to an extension
  of Contract Time and, if appropriate, an equitable adjustment in Contract Sum.
- A201 § 3.7.4: Delays due to conditions not reasonably anticipated entitle contractor to
  claim adjustment.

**No-Damage-for-Delay Clauses**:

Many owner-drafted supplementary conditions add a "no-damage-for-delay" (NDD) clause
that limits contractor's remedy for owner-caused delays to a time extension only — no
money. This is the most consequential single modification to AIA standard language.

[VERIFY] NDD clause enforceability varies by state:

- **Broadly enforceable**: Texas, Alabama, Mississippi (with some exceptions)
- **Restricted by statute**: California (Gov't Code § 4215 for public contracts), New York
  (GBL § 756-a prohibits NDD clauses in public contracts > $100K), Oregon, Washington, Ohio,
  Wisconsin, Colorado [VERIFY each state's current rule]
- **Limited by judicial exceptions**: Most states recognize exceptions for: active
  interference by owner, fraud or bad faith, abandonment of project, changes in scope

**Key elements to review:**

- Is there an NDD clause? If yes, identify the state and apply the matrix above.
- Does the delay clause distinguish between excusable delay (time extension only) vs.
  compensable delay (time + money)?
- Is there a concurrent delay clause? If Owner's delay and Contractor's delay overlap,
  who bears the cost?
- Are force majeure events listed? Does the list cover supply-chain disruptions, labor
  shortages, and pandemic events?
- Is there a notice-of-delay requirement? What happens if notice is late?

**Delay Claim Checklist:**

- [ ] Identify cause of delay (owner-caused, contractor-caused, third party, force majeure)
- [ ] Confirm notice was provided within contract-required period
- [ ] Assess whether NDD clause applies and whether state-law exceptions are available
- [ ] Classify as excusable-only or compensable
- [ ] Check concurrent delay allocation
- [ ] Calculate critical path impact

**Automatic RED Triggers — Delay:**

1. NDD clause in a state with no statutory protection
2. No compensable delay provision for owner-directed acceleration
3. Notice deadline less than 7 days for delay claims in complex projects
4. Force majeure excludes supply-chain and labor availability events

---

### 6. Applications for Payment and Retainage

**AIA Baseline**:

- A201 § 9.3: Monthly payment applications on AIA G702/G703 forms (Schedule of Values)
- A201 § 9.4: Architect certifies payment within 7 days; Owner pays within 7 days of
  certification (aggregate: payment within 14 days of contractor's application)
- **Retainage**: AIA standard (A201 § 9.3.1) does not specify a retainage rate — it is
  established in A101 § 5.1.7. Market practice is 10%, reducing to 5% at 50% completion.
- A201 § 9.8.5: Upon substantial completion, owner must pay the retainage balance less
  amounts related to incomplete or defective work.
- Stored materials: A201 § 9.3.2 allows payment for materials stored off-site if title
  transfers, materials are insured, and appropriate documentation provided.

**State Retainage Statutes** [VERIFY for project state]:
| State | Cap / Rule |
|-------|-----------|
| California | 5% cap on private projects; Pub. Cont. Code § 7201 for public |
| Texas | 10%, reducing to 5% at 50% completion; prompt payment rules in Prop. Code § 28 |
| New York | 5% cap; GBL § 756-b for retainage release |
| Florida | 10% reducing to 5% for public projects; § 255.078 Fla. Stat. |
| Illinois | 10% cap; 820 ILCS 580 |
[VERIFY all state retainage statutes for current provisions]

**Key elements to review:**

- Retainage rate and reduction trigger — does contract comply with state statutory cap?
- Does retainage reduction require owner approval, or is it automatic at 50% completion?
- Retainage on stored materials — can contractor include stored materials in G702?
- Lien waiver conditioning — does owner require unconditional lien waivers before
  processing payment? (This extinguishes lien rights before payment is actually received — RED)
- Payment period — does it comply with state prompt payment act?
- Interest on late payments — is the contractual rate less than the statutory rate?
- Suspension for non-payment — A201 § 14.1.1 allows contractor to suspend if owner fails
  to pay certified amounts; ensure this right is not waived by supplementary conditions.

**Automatic RED Triggers — Payment/Retainage:**

1. Retainage rate exceeds state statutory cap
2. Unconditional lien waivers required before payment is received
3. Payment period exceeds state prompt payment act requirements
4. Contractor's right to suspend for non-payment is waived or modified
5. Owner has unilateral right to withhold payment for disputed items exceeding certified amount

---

### 7. Substantial and Final Completion

**AIA Baseline**:

- **Substantial Completion** (A201 § 9.8): The stage when the Work is sufficiently complete
  that the Owner can occupy or utilize it for its intended purpose. Marked by issuance of
  Certificate of Substantial Completion (AIA G704).
- Effect: (a) retainage substantially released; (b) contractor's obligation to insure the
  Work transfers to Owner; (c) LDs typically stop running; (d) 1-year correction period
  begins (A201 § 12.2.2); (e) statute of repose clock starts in many states.
- **Final Completion** (A201 § 9.10): All Work complete, all punch list items resolved,
  all close-out documents submitted. Prerequisite for final payment.

**Key elements to review:**

- Who has authority to issue the Certificate of Substantial Completion? AIA assigns this
  to the Architect. Does the contract change this? (Removing architect certification
  authority may leave contractor without a mechanism to trigger retainage release.)
- Is there a defined punch list process and deadline? AIA standard is silent on punch list
  completion deadline — owner may stall final completion indefinitely.
- Does the contract carve out unresolved change order claims from final payment?
  (A201 § 9.10.4: acceptance of final payment waives claims except those identified in writing)
- Is the correction period (AIA uses 1 year from substantial completion) consistent with
  any applicable warranty periods? Can the owner extend the correction period?
- Does LDs stop running at substantial completion or at final completion? The latter is
  contractor-adverse; AIA standard ties LDs to substantial completion.

**Common deviations:**

- Punch list completion deadline not defined — creates indefinite hold on final payment — YELLOW
- Owner reserves right to reject substantial completion if any item on punch list remains — RED
- Correction period extended beyond 1 year in supplementary conditions — YELLOW
- LDs run until final completion, not substantial completion — RED

---

### 8. Liquidated Damages

**AIA Baseline**: A101 § 4.5 provides space to insert LDs. AIA A201 is otherwise silent
on LDs — they are established in the Owner-Contractor Agreement.

**US Enforceability Standard** [VERIFY]:
LDs are enforceable under US common law if, at the time of contracting:

1. Actual damages were difficult or impossible to estimate, AND
2. The LD amount was a reasonable forecast of just compensation (not a penalty)

Courts apply either the "reasonableness at time of contracting" test or (in some states)
the "reasonableness at time of breach" test. [VERIFY applicable state standard]

**Key elements to review:**

- Is the LD rate stated as a fixed dollar amount per day of delay? Percentage-based or
  indeterminate LDs may be unenforceable.
- Is the LD rate a reasonable pre-estimate of owner's actual damages? Review against
  actual financing costs, lost revenue, and tenant/occupant damages.
- Are there milestone LDs (intermediate dates) in addition to final completion LDs?
  Milestone LDs increase contractor risk; ensure milestones are realistic and controlled.
- Does the contract address concurrent delay? If owner and contractor both caused delay,
  most courts will not award LDs to owner — but check whether the contract modifies this.
- Does "substantial completion" stop LDs? AIA standard does; confirm no modification.
- Is there a cap on LDs? Without a cap, LDs could dwarf the contract sum on long delays.
- Are LDs stated to be the owner's "exclusive remedy" for delay, or can owner also seek
  actual damages? Exclusive remedy language protects contractor.

**State-Specific LD Issues** [VERIFY]:

- California: LDs must be reasonable at time of contracting; "exclusive remedy" language
  broadly enforced (Civ. Code § 1671)
- New York: Strictly enforced if reasonable at inception; courts disfavor clauses that
  allow owner to collect LDs AND terminate for cause (cumulative remedy issue)
- Texas: Enforced if reasonable; courts look at reasonableness as of breach date

**Automatic RED Triggers — LDs:**

1. LD rate that is facially unreasonable (e.g., exceeds 10-15% of contract sum on short project)
2. LDs run until final completion (not substantial completion) without compensating carve-out
3. No concurrent delay defense
4. LDs plus actual damages (not exclusive remedy) — double exposure

---

### 9. Insurance

**AIA Baseline**: A201-2017 Article 11 restructures insurance requirements from A201-2007,
adding an Insurance Exhibit (AIA Exhibit A to A201-2017) with detailed coverage schedules.

**Required Insurance — Contractor (A201 § 11.1)**:

- Commercial General Liability (CGL): Occurrence-based; minimum limits typically
  $1M/$2M. A201 requires coverage for bodily injury, property damage, personal injury,
  advertising injury, and completed operations.
- Automobile Liability: Covering owned, hired, and non-owned autos
- Workers' Compensation: Statutory limits by state + Employer's Liability
- Umbrella/Excess: AIA does not specify — owner typically establishes minimum in Exhibit A

**Required Insurance — Owner (A201 § 11.2)**:

- Property/Builder's Risk: AIA § 11.2.1 — Owner is responsible for builder's risk unless
  contract assigns this to contractor. Builder's risk must cover Work at jobsite and
  stored materials, and all materials in transit.
- Builder's risk gap: AIA does not require Owner to include subcontractors as additional
  insureds on builder's risk — check whether policy covers sub-tiers.

**OCIP/CCIP (Wrap Programs)**:

- Owner Controlled Insurance Program (OCIP) or Contractor Controlled Insurance Program
  (CCIP): single consolidated insurance program covering all project participants.
- If OCIP/CCIP exists: verify which coverages are included vs. excluded, enrollment
  requirements, how claims affect contractor's experience modification rate (EMR), and
  whether wrap program coverage is primary.

**Additional Insured Requirements** (A201 § 11.1.4):

- Contractor must name Owner and Architect as additional insureds on CGL
- Additional insured status should be primary and non-contributory
- A201-2017 adds requirement that additional insured status continue for completed
  operations for 3 years after final payment

**Key elements to review:**

- Do coverage limits meet project-specific requirements? Standard A201 limits may be
  inadequate for large projects.
- Is builder's risk assigned to Owner or Contractor? Who insures materials in transit
  and off-site storage?
- Are all required carriers admitted in the project state?
- Are certificates of insurance required, and does the contract require notification of
  cancellation? (ISO cancellation endorsements have changed — verify notice mechanism)
- Does the contract require Waiver of Subrogation? (A201 § 11.3.7 — mutual waiver of
  subrogation for builder's risk losses is standard; ensure it is mutual)

**Automatic RED Triggers — Insurance:**

1. No builder's risk coverage allocated — neither owner nor contractor is required to maintain
2. CGL limits inadequate for project size and risk profile
3. No additional insured status for owner on contractor's CGL
4. No workers' compensation or employer's liability requirement
5. Waiver of subrogation missing from builder's risk provisions

---

### 10. Performance and Payment Bonds

**AIA Baseline**: A201 § 11.6 allows owner to require bonds. Bond forms: AIA A312-2010
(Performance Bond and Payment Bond).

**Miller Act (Federal Projects)**:
Performance + payment bonds required on federal construction contracts over $150,000
(40 U.S.C. § 3131). [VERIFY current threshold]

- Performance Bond: Protects owner if contractor defaults
- Payment Bond: Protects subcontractors and suppliers (direct right of action against surety)
- Payment bond claim deadline: 90 days after last work/materials furnished to file notice;
  1 year to file suit [VERIFY]

**Little Miller Acts (State Public Projects)**:
Most states require performance + payment bonds on public projects above threshold
(thresholds vary: e.g., California $25K, Texas $100K, New York no fixed threshold for
performance bond on public works) [VERIFY by state]

**Private Projects**:
No statutory bond requirement for private projects. Bonds are contractually required.
Lenders frequently require performance and payment bonds as loan conditions.

**Key elements to review:**

- Are performance and payment bonds required? What is the bond amount (100% of contract
  sum is standard)?
- Is the bond form AIA A312-2010? Non-AIA bond forms may have contractor-favorable
  provisions that limit surety's obligations.
- Does the performance bond require the owner to give the surety written notice of default
  before the surety's obligations trigger? (AIA A312 requires notice and investigation)
- Are subcontractors required to provide bonds flowing up to the prime? Flow-down of
  bond obligations protects the GC from sub-default.
- Does lien waiver for payment bond claimants coincide with payment application cycle?

**Automatic RED Triggers — Bonds:**

1. No payment bond on public project above Little Miller Act threshold
2. Non-standard bond form that limits surety's obligations
3. Bond amount less than 100% of contract sum without compelling justification

---

### 11. Indemnification

**AIA Baseline**: A201 § 3.18 — **Intermediate Form Indemnity**:
Contractor indemnifies Owner, Architect, and their agents against claims arising out of
or resulting from performance of the Work, **to the extent caused by the negligent acts
or omissions of the Contractor**, its subcontractors, or their agents. This is intermediate
form — Contractor does not indemnify Owner for Owner's own negligence.

**US Indemnity Forms:**
| Form | Description | AIA Standard? |
|------|-------------|---------------|
| **Broad Form** | Indemnitor covers indemnitee's own negligence | No — A201 uses intermediate |
| **Intermediate Form** | Indemnitor covers claims caused by indemnitor's negligence | Yes — A201 § 3.18 |
| **Limited Form** | Indemnitor covers only indemnitor's own negligence (no shared negligence coverage) | No — narrower than AIA |

**Anti-Indemnity Statute Matrix** [VERIFY — statutes change]:
Most US states restrict or prohibit broad-form indemnity in construction contracts.

| State      | Restriction Level                                                                            | Statute                                                              |
| ---------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| California | Prohibits indemnity for indemnitee's own negligence                                          | Civ. Code § 2782                                                     |
| Texas      | Prohibits broad-form; intermediate allowed with express negligence test                      | Tex. Ins. Code § 151.102; Indus. Found. v. Texas Indus. Accident Bd. |
| New York   | Allows broad-form for personal injury/death only with General Obligation Law § 5-322.1       |
| Florida    | Prohibits indemnity for indemnitee's sole negligence § 725.06 Fla. Stat.                     |
| Illinois   | Prohibits indemnity for indemnitee's negligence — 740 ILCS 35/1                              |
| Washington | Prohibits indemnity for indemnitee's negligence — RCW 4.24.115                               |
| Colorado   | Prohibits indemnity for indemnitee's sole or concurrent negligence — C.R.S. § 13-21-111.5    |
| Ohio       | Prohibits indemnity agreements that purport to cover indemnitee's negligence — ORC § 4113.62 |

[VERIFY all — anti-indemnity statutes are amended; confirm current version for project state]

**Key elements to review:**

- Is the indemnity mutual or one-way? AIA § 3.18 is one-way (contractor indemnifies owner).
  Does the owner's A201 modification add mutual indemnity? If owner-side indemnity is absent,
  this is YELLOW.
- Has the owner modified indemnity to broad-form (covering owner's own negligence)?
  Check against state anti-indemnity statute — modification may be void as a matter of law.
- Is there a separate IP indemnity? AIA A201 does not have one — if contractor creates
  designs, this may be needed.
- Does the indemnity include defense obligations? "Defend, indemnify, and hold harmless"
  triggers immediate defense obligation, not just reimbursement of judgment.
- Is the indemnity subject to the contractor's limitation of liability? Many supplementary
  conditions make indemnity obligations uncapped — RED.

**Automatic RED Triggers — Indemnity:**

1. Broad-form indemnity in a state with anti-indemnity statute that prohibits it
2. Uncapped indemnity obligation for Contractor not tied to limitation of liability
3. Indemnity scope extended to intellectual property infringement without carve-outs
4. Defense obligation without right to control defense or consent to settlement

---

### 12. Mechanic's Liens

**AIA Baseline**: A201 § 9.10.2 — Owner may require lien waivers as a condition of
final payment. A201 does not otherwise address mechanic's lien law — this is entirely
state-specific.

**Lien Law Fundamentals** [VERIFY by state]:

_Preliminary Notice_: Many states require subcontractors and suppliers to serve a
preliminary notice (also called "20-day notice," "Notice to Owner," or "Notice of
Furnishing") within a short window after first furnishing labor or materials —
failure to serve voids lien rights. Critical deadlines vary:

| State      | Preliminary Notice Rule                                                 |
| ---------- | ----------------------------------------------------------------------- |
| California | 20 days from first furnishing for subs/suppliers (Civ. Code § 8204)     |
| Texas      | Monthly notices; §§ 53.056–53.057 Tex. Prop. Code                       |
| Florida    | 45 days from first furnishing — §§ 713.13–713.06 Fla. Stat.             |
| New York   | No preliminary notice required; lien filed within 8 months of last work |
| Illinois   | No preliminary notice; 4 months to file lien                            |

[VERIFY all — lien statutes are frequently amended]

_Lien Filing Deadline_: After project completion (or last furnishing), lienors have a
limited window to file the mechanic's lien. Deadlines range from 60 days (some states
for sub-subcontractors) to 8–12 months. Missing this deadline extinguishes lien rights.

_Lien Waivers — AIA G706/G707_:

- AIA publishes four standard lien waiver forms: Conditional Waiver on Progress Payment,
  Unconditional Waiver on Progress Payment, Conditional Waiver on Final Payment,
  Unconditional Waiver on Final Payment
- California mandates specific lien waiver language (Civ. Code §§ 8132–8138) — use only
  statutory forms in California
- **Conditional waiver**: effective only upon actual receipt of payment — protects claimant
- **Unconditional waiver**: immediately effective regardless of whether payment is received —
  extinguishes lien rights even if check later bounces — DO NOT SIGN before payment clears

_Lien Priority vs. Construction Lender_:

- A mechanic's lien typically relates back to the date construction commenced ("first
  visible commencement") which may predate the lender's mortgage recording.
- Lenders often require a "date-down" title endorsement and recorded construction loan
  before visible commencement to establish priority.

**Key elements to review:**

- Does the owner require unconditional lien waivers before payment? — RED (see § 6)
- Are lien waiver forms project-state compliant? In California, only statutory forms are valid.
- Does the contract require contractor to deliver lien waivers from all subcontractors and
  suppliers before owner releases final payment? This is reasonable and standard.
- Does the contract include a lien release bond provision? If a lien is improperly filed,
  the bond allows the project to close.
- Is the joint check provision (owner pays subcontractors directly) addressed?

**Automatic RED Triggers — Liens:**

1. Unconditional lien waivers required before payment cleared
2. Lien waiver forms that do not comply with state-mandated language (e.g., California)
3. No mechanism for contractor to bond around disputed liens

---

### 13. Dispute Resolution

**AIA Baseline — A201 Article 15 (2017)**:
AIA-2017 establishes a mandatory multi-step process:

**Step 1 — Initial Decision Maker (IDM)**: Claims must first be submitted to the IDM
(default: the Architect, unless parties designate a neutral). IDM has 10 days to
acknowledge; 30 days to render a decision or request additional information (A201 § 15.2).
IDM decision is final and binding unless timely contested (60 days).

**Step 2 — Mediation**: Mandatory before arbitration or litigation. If a party rejects
IDM decision, they demand mediation under AAA Construction Industry Mediation Procedures
(A201 § 15.3). Mediation is a precondition to arbitration/litigation.

**Step 3 — Arbitration or Litigation**: Default under A201-2017 is **litigation**, not
arbitration. The 2017 edition changed this from 2007 edition (which defaulted to
arbitration). Parties must check box in A101/A102 if they want to arbitrate.

**Common Modifications:**

- Many owners elect arbitration in A101 (check box at § 6.2)
- AAA Construction Industry Rules govern if arbitration selected
- Some owners designate a Dispute Review Board (DRB) or Standing Neutral instead of IDM

**Arbitration vs. Litigation Considerations:**

| Factor              | Arbitration                                                | Litigation                  |
| ------------------- | ---------------------------------------------------------- | --------------------------- |
| Discovery           | Limited                                                    | Full (FRCP/state rules)     |
| Decision-maker      | Arbitrator(s) — often industry experts                     | Judge ± jury                |
| Appeal              | Very limited (9 U.S.C. § 10 grounds)                       | Full appellate rights       |
| Speed               | Faster (typically)                                         | Slower                      |
| Cost                | Lower (initially) — higher arbitrator fees on large claims | Lower per-claim cost        |
| Confidentiality     | Private                                                    | Public record               |
| Multi-party joinder | Difficult across tiers                                     | Possible with consolidation |

**Multi-Tier Dispute Issues**:

- Owner-GC dispute (A101 arbitration) + GC-Sub dispute (A401 arbitration) may result in
  parallel proceedings. Does A401 include a "consolidation" provision tying sub-arbitration
  to prime arbitration?
- If Owner and GC litigate but GC and Sub have arbitration clause, GC may face inconsistent
  outcomes.

**Key elements to review:**

- Has arbitration been selected? If so, is AAA Construction Rules specified? No. of arbitrators?
- Is the IDM mechanism intact? Owner-modified contracts often remove IDM, leaving disputes
  without a first-step decision mechanism — weakens contractor's ability to get quick relief.
- Is mediation as a pre-condition to arbitration/litigation retained? Some owners remove it.
- Does the dispute clause include all types of claims, or carve out certain claims (e.g.,
  lien enforcement, injunctive relief for IP)?
- Is there a statute of limitations or claim filing deadline that is shorter than the state's
  applicable limitations period?
- Does the contract include a jury trial waiver? Does it require mutual class action waiver?
- For subcontract (A401): Is there a "flow-up" dispute clause aligning sub-disputes with
  prime dispute schedule?

**Automatic RED Triggers — Disputes:**

1. IDM removed with no replacement mechanism
2. Mandatory mediation waived — direct to arbitration/litigation
3. Arbitration required in a distant jurisdiction with no connection to the project
4. Claims notice period that is less than the AIA 21-day standard for complex disputes

---

### 14. Termination

**AIA Baseline**: A201 Article 14 provides four termination rights:

- **§ 14.1 — Contractor Termination for Cause**: If Owner repeatedly fails to pay sums
  properly due, becomes insolvent, or persistently violates contract; Contractor may
  terminate on 7-day written notice.
- **§ 14.2 — Owner Termination for Cause**: If Contractor repeatedly fails to supply
  workers/materials, fails to make payments to subs, disregards laws, or otherwise
  substantially violates the contract; Owner may issue 7-day cure notice, then terminate.
- **§ 14.3 — Owner Suspension for Convenience**: Owner may suspend Work for up to 90
  days with equitable adjustment to Contract Sum and Time upon resumption.
- **§ 14.4 — Owner Termination for Convenience**: Owner may terminate for convenience
  at any time. Contractor is paid for Work done, costs incurred, reasonable overhead and
  profit for unperformed work, and reasonable termination costs.

**Key elements to review:**

- Does the contract eliminate Contractor's termination for cause rights? — RED
- Has the owner modified the cure period (AIA uses 7 days)? Less than 7 days with no right
  to cure is contractor-adverse — YELLOW/RED
- Does the termination-for-convenience payment formula adequately compensate for anticipated
  profit on unperformed work? Some owners cap termination payment at cost-without-profit.
- Does the contract permit owner to convert a termination-for-convenience to a
  termination-for-cause after the fact? This is the "bad faith termination" risk.
- Does the subcontract flow-down termination rights properly from prime to sub?

---

### 15. Design Liability and Shop Drawings

**AIA Baseline**:

- **Design-Bid-Build**: Owner's architect prepares design. Contractor is not responsible
  for design errors (Spearin doctrine: A201 § 3.2.2 — Owner implicitly warrants accuracy
  of Contract Documents) [VERIFY]
- **Design-Build (A141)**: Contractor takes design risk; no Spearin protection.
- A201 § 3.12: Contractor submits shop drawings, product data, and samples. Architect
  reviews for conformance with design intent, not for means and methods.
- A201 § 3.12.8: Contractor is not relieved of responsibility for deviations from Contract
  Documents by architect's approval of shop drawings unless contractor has specifically
  informed architect of the deviation and architect has approved it.

**Key elements to review:**

- Is design-build delivery being used with an AIA form not designed for it? (Using A101 for
  design-build creates significant coverage gaps — AIA A141 is the correct form.)
- Does the contract impose design-build obligations on a contractor using an A101 form?
  If so, Spearin protection is effectively waived without consideration — RED.
- Are shop drawing review periods defined? Unlimited review time creates schedule exposure.
- Does the owner reserve right to reject shop drawings without cause? — YELLOW

---

### 16. Subcontracting and Flow-Down

**AIA Baseline**:

- A201 § 5.2: Contractor must submit list of proposed subcontractors to Architect/Owner.
  Owner may object within 14 days; Owner's objection triggers equitable adjustment if
  substitute sub is more expensive.
- A201 § 5.3: Subcontract terms must bind subs to GC as GC is bound to Owner; make all
  work available for correction as required by A201 § 12.1.
- A401 § 3.1: Sub agrees to be bound to GC by the terms of the prime contract.

**Key elements to review:**

- Does the subcontract properly incorporate A201 by reference, not just by title? Improper
  incorporation fails to create flow-down obligations.
- Are pay-when-paid vs. pay-if-paid clauses used? **Pay-if-paid** (sub only gets paid if
  GC gets paid from owner) — enforceability varies: California prohibits pay-if-paid in
  most contexts; New York enforces; Texas enforces if express [VERIFY by state].
- Does the subcontract flow down the correct dispute resolution pathway (aligning with
  prime contract dispute clause)?
- Is the retainage rate on the sub consistent with the prime contract rate?
- Are lien waiver obligations correctly flowed down?

---

## Deviation Severity Classification

### GREEN — Acceptable / AIA Standard

The clause matches or is better than AIA standard language. Minor variations that are
commercially reasonable for the owner/contractor relationship.

**Action**: Note for awareness. No negotiation needed.

**Examples:**

- Retainage rate of 5% (better than market 10% standard for contractor)
- Mutual indemnity added alongside AIA § 3.18 one-way indemnity
- LD rate is reasonable relative to project size and owner's documented daily damages

### YELLOW — Negotiate / Deviation from AIA Standard

The clause deviates from AIA standard but within a negotiable range. Common
owner-favorable modifications that merit negotiation but are not deal-breakers.

**Action**: Generate specific redline restoring AIA language or a balanced alternative.
Provide fallback position. Estimate business impact of accepting vs. negotiating.

**Examples:**

- Change order notice period shortened from 21 days to 14 days
- Retainage reduction from 10% requires owner approval (not automatic at 50% completion)
- Overhead and profit markup reduced from AIA standard to 10% combined

### RED — Escalate / Material Deviation

The clause falls outside acceptable range, exposes the party to material unquantified
risk, or is potentially void under applicable state law. Requires escalation and/or
outside counsel review.

**Action**: Explain specific risk with legal basis. Provide AIA standard language as
replacement. Estimate maximum exposure. Recommend escalation path.

**Automatic RED Triggers (Contractor-Side Review):**

1. No-damage-for-delay clause in a state without statutory protection
2. Unconditional lien waivers required before payment received
3. Retainage above state statutory cap
4. Broad-form indemnity in anti-indemnity-statute state
5. Contractor's right to terminate or suspend for non-payment eliminated
6. Waiver of Spearin protection on a design-bid-build project
7. LD rate facially unreasonable (exceeds 1.5% of contract sum per day)
8. No Payment Bond on a project that requires it under Little Miller Act
9. Unilateral right to expand scope without change order
10. Claims/disputes notice period less than 7 days

**Automatic RED Triggers (Owner-Side Review):**

1. No performance bond on a project above bond threshold with financially weak contractor
2. Float owned entirely by contractor (all float allocated to contractor's schedule)
3. Uncapped consequential damages flowing to owner with no shared limitation of liability
4. No mechanic's lien waiver requirements in states with broad lien rights
5. No right to audit on GMP (cost-plus) contracts
6. Pay-if-paid clause in a state where it is unenforceable — owner cannot rely on it to protect GC
7. Force majeure clause so broad that it excuses virtually any performance delay

---

## Prioritization Framework

### Tier 1 — Deal-Breaker (Must Negotiate Before Signing)

Issues that expose the reviewing party to uncapped or catastrophically large risk, that
may be void under applicable law, or that fundamentally misallocate the construction risk.

- Automatic RED triggers (above)
- State law violations (anti-indemnity, retainage cap, lien waiver)
- Uncapped indemnity with defense obligation
- No-damage-for-delay in contractor-adverse states

**Strategy**: Do not sign without resolution. Present as non-negotiable at the outset.
Offer AIA standard language as a ready replacement.

### Tier 2 — Material (Should Negotiate — Significant Value at Stake)

Issues that create meaningful financial or schedule exposure but are negotiable and
commonly moved by sophisticated owners/GCs.

- Change order markup percentages
- Retainage reduction mechanics
- LD rate reasonableness
- Insurance limits adequacy
- Dispute resolution forum

**Strategy**: Prioritize these in the first negotiation round. Accept reasonable
compromises; document the basis for any accepted position.

### Tier 3 — Minor (Nice-to-Have — Low Financial Impact)

Issues that represent modest deviations from AIA standard with limited financial impact.
Acceptable to leave on the table to close the deal.

- Notice address updates
- Minor punch list wording
- Certificate of insurance delivery timing
- Boilerplate administrative provisions

**Strategy**: Trade against Tier 1 and 2 issues. Concede freely if needed to preserve
capital on material items.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                         | Fail Action                                                       |
| -------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific AIA section, statute, or established US principle                         | Add citation or mark "[UNVERIFIED]"                               |
| **Format**     | AIA citations use form number + section (e.g., "A201-2017 § 3.18"); statutes use standard US citation format | Fix format                                                        |
| **Currency**   | Every cited AIA document verified against edition year in the contract; every statute checked for amendment  | Flag "[CHECK CURRENCY — verify edition year and statute version]" |
| **Domain**     | Analysis stays within US construction law; no UK, Australian, or FIDIC concepts imported without labeling    | Remove or flag cross-jurisdictional bleed                         |
| **Confidence** | Uncertainty about state-specific rules explicitly stated, not hidden                                         | Add confidence qualifier and [VERIFY by state] tag                |

### Self-Interrogation for RED Items

For any item classified RED, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the
cited AIA provision or US statute? Is the anti-indemnity statute actually operative in
the project state? Would a construction court actually reach this conclusion?

**Pass 2 — Completeness**: Have all relevant AIA sections been considered? Does the
contract's supplementary conditions modify the provision being analyzed in a way that
changes the analysis?

**Pass 3 — Challenge**: What is the strongest argument for the other side? Under what
circumstances might a construction attorney advise accepting this provision (e.g., deal
dynamics, state where anti-indemnity statute has exceptions)?

### Confidence Scoring

| Level        | Range     | Meaning                                     | Action                                     |
| ------------ | --------- | ------------------------------------------- | ------------------------------------------ |
| **Definite** | 0.95–1.0  | Settled AIA standard; clear statute         | State with confidence                      |
| **High**     | 0.80–0.94 | Strong AIA/state authority; minor questions | State with brief caveat                    |
| **Probable** | 0.60–0.79 | General US practice; state may vary         | State with [VERIFY by state]               |
| **Possible** | 0.40–0.59 | Genuinely uncertain; state-specific         | Flag for construction attorney review      |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                     | Do not assert; flag "[UNCERTAIN — verify]" |

---

## Anti-Patterns

What NOT to do when reviewing US AIA construction contracts:

1. **Applying AIA-2007 analysis to AIA-2017 contracts** — The 2017 edition changed the
   default dispute resolution forum from arbitration to litigation, revised the claims
   notice process, and added the Insurance Exhibit. Never assume edition without verifying.

2. **Treating AIA standard language as owner-neutral** — AIA documents are negotiated
   between owner and contractor industry groups and represent a balanced starting point,
   not an owner-favorable baseline. When supplementary conditions modify AIA, the
   modifications are presumptively owner-favorable deviations that favor the drafting party.

3. **Ignoring the state anti-indemnity statute** — The most commonly missed state-law
   overlay. A broad-form indemnity that is void in California may be enforced in Texas.
   Never classify indemnity risk without identifying and verifying the project state's statute.

4. **Analyzing a GMP contract as if it were a stipulated sum** — GMP contracts have
   fundamentally different audit, cost control, and contingency provisions. Applying
   stipulated-sum review logic to A102/A133 misses the most important risk areas.

5. **Accepting unconditional lien waivers as standard practice** — Some owner representatives
   request unconditional waivers at every payment application as a matter of course. This
   is not standard practice and extinguishes lien rights even if the check subsequently
   bounces. Always flag this as RED regardless of how the owner characterizes it.

6. **Missing the no-damage-for-delay clause** — NDD clauses are often buried in
   supplementary conditions, not in the "Delay" section of the main body. Read all
   supplementary conditions carefully; this single provision is worth more than any other
   in a delayed project.

7. **Failing to check whether arbitration was elected** — A201-2017 defaults to litigation,
   but the boxes in A101/A102 must be checked to confirm the dispute forum. Many parties
   execute A201 without completing the A101 election — leaving the dispute mechanism
   ambiguous.

8. **Analyzing indemnity in isolation from insurance** — An uncapped indemnity is less
   dangerous if the contractor is required to carry adequate insurance. An indemnity that
   requires defense even for owner's own negligence may be partially mitigated by
   additional insured status on the contractor's CGL. Always analyze indemnity and
   insurance together.

9. **Ignoring flow-down provisions in subcontract review** — The A401 subcontract
   incorporates A201 by reference. Supplementary conditions from the prime contract may
   not automatically flow down unless A401 § 3.1 expressly states they do. Missing
   flow-down of the no-damage-for-delay clause or arbitration election is a frequent
   dispute source.

10. **Treating all lien waivers as equivalent** — Conditional vs. unconditional, and
    progress vs. final, are four materially different instruments. In states with statutory
    lien waiver forms (California), non-compliant forms are void. Never advise a party to
    sign without identifying the waiver type and state compliance.

11. **Missing constructive change exposure** — Owners sometimes increase scope through
    architect directions, specification interpretations, over-inspection, or rejection of
    conforming work — all without issuing a formal CO. If the contract has a tight claims
    notice period, constructive change rights may be forfeited without timely written notice.

12. **Overlooking the IDM's identity** — AIA defaults the IDM to the Architect. When the
    architect is owner's design professional, the IDM is not neutral. Check whether
    parties have designated an independent IDM or a Dispute Review Board. On large projects,
    architect-as-IDM is a structural bias point for contractors.

13. **Assuming Spearin protection without checking delivery method** — The Spearin doctrine
    (owner impliedly warrants contractor-provided design) applies in Design-Bid-Build.
    It does not apply in Design-Build. A contractor agreeing to a "performance specification"
    may inadvertently accept design liability. Identify delivery method before applying
    Spearin analysis.

14. **Not checking state-specific retainage cap before flagging rate** — A 10% retainage
    rate is standard in many states but above the cap in others (California allows max 5%).
    Flagging a 10% rate as standard in California is an error; flagging it as compliant is
    a different error. Always verify against the project state's statute.

15. **Delivering analysis without the Glass Box audit trail** — Construction disputes are
    extensively litigated; the reviewing attorney needs to know which AIA provisions were
    checked, what state law was applied, and what was uncertain. The Glass Box is not
    administrative overhead — it is a professional responsibility safeguard.

---

## Writing Standards

Before delivering any output:

1. **Use construction-specific terms precisely**: "Change Order" (CO), "Construction
   Change Directive" (CCD), "Retainage" (not "holdback" unless contract uses that term),
   "Substantial Completion" (capital S and C — it is a defined AIA term), "Contract Sum"
   (not "contract price" unless the contract uses that term).

2. **Cite AIA provisions in full**: Always use form number + edition year + section
   (e.g., "AIA A201-2017 § 3.18.1"). Do not abbreviate to "§ 3.18" without the form
   reference — AIA forms share section numbers.

3. **State the edition year for every AIA citation** unless the contract version has
   already been confirmed and noted in the Glass Box.

4. **Flag state-specific assertions explicitly**: Every claim about state mechanic's lien
   law, anti-indemnity statute, retainage cap, or prompt payment act must be tagged with
   the state and [VERIFY] unless verified via legalcode-mcp.

5. **Separate "AIA standard says X" from "this contract says Y"**: The analysis must
   always be clear about whether it is describing the AIA baseline or the actual contract
   under review.

6. **Active voice, imperative form for recommendations**: "Revise § 5.1.7 to reduce the
   retainage rate to 5%" not "the retainage provision could potentially be revised."

7. **Run Citation Quality Gates silently before delivering**.

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

In Step 4, use legalcode-mcp to verify:

- State mechanic's lien law for the project state
- State anti-indemnity statute text and any recent amendments
- State retainage statute and cap
- State prompt payment act (private construction, not just public)
- State statute of repose for construction defects
- State little Miller Act thresholds

Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box.

### Without legalcode-mcp

- Mark all state statutory references with [VERIFY by state]
- Note in Glass Box: `legalcode_mcp: "Not connected — state law provisions require manual verification"`
- Focus analysis on AIA structural deviations, which are document-based and do not require
  external legal research
- Advise user to retain a construction attorney in the project state for state-law issues

---

## Glass Box Audit Trail

Append this to every review output:

```yaml
glass_box:
  skill: legalcode-us-aia-construction-contract-review
  date: "[date of review]"
  contract_name: "[contract name or description]"
  reviewing_party: "[Owner / GC / Subcontractor / Lender / Surety]"
  aia_form: "[A101-2017 / A102-2017 / A133-2019 / Non-AIA / AIA-modified]"
  aia_edition_confirmed: "[Yes / No — assumed from context]"
  project_state: "[state]"
  project_type: "[Federal / State Public / Private Commercial / Other]"
  contract_value: "[approximate range]"
  legalcode_mcp: "[Connected — N citations verified / Not connected]"
  state_law_verified:
    anti_indemnity: "[Verified / [VERIFY] / Not applicable]"
    retainage_cap: "[Verified / [VERIFY] / Not applicable]"
    lien_law: "[Verified / [VERIFY] / Not applicable]"
    prompt_payment: "[Verified / [VERIFY] / Not applicable]"
  deviations_found:
    red: "[count]"
    yellow: "[count]"
    green: "[count]"
  automatic_red_triggers_fired: "[list triggered items or 'None']"
  quality_score: "[X]/40"
  confidence: "[HIGH / MEDIUM / LOW — rationale]"
  limitations:
    - "State law provisions not verified without legalcode-mcp — flag for construction attorney"
    - "AIA edition year [confirmed / assumed] — verify before relying on section citations"
    - "[Any other caveats specific to this review]"
  reviewer: "AI-assisted — requires qualified construction attorney review before use"
```

---

## Output Format Template

```markdown
# Construction Contract Review: [Contract Name]

**Review Date**: [date]
**Reviewing Party**: [Owner / GC / Sub]
**AIA Form**: [form + edition year]
**Project State**: [state]
**Contract Value**: [range]

---

## Executive Summary

**Overall Risk Profile**: [HIGH / MEDIUM / LOW]

| Finding       | Severity  | Category   |
| ------------- | --------- | ---------- |
| [Top issue 1] | 🔴 RED    | [Category] |
| [Top issue 2] | 🔴 RED    | [Category] |
| [Top issue 3] | 🟡 YELLOW | [Category] |

**Bottom Line**: [2-3 sentence summary of the contract's overall risk posture,
top issues, and recommended negotiation strategy.]

---

## Clause Analysis

### 1. Scope of Work and Contract Documents

**Status**: [🟢 GREEN / 🟡 YELLOW / 🔴 RED]
**AIA Baseline**: [What AIA standard says]
**Contract Language**: [What this contract says — quote key deviating language]
**Issue**: [Description of deviation and why it matters]
**Confidence**: [Definite / High / Probable / Possible]
**Recommended Redline**:

> **Delete**: "[current language]"
> **Replace with**: "[AIA standard language or balanced alternative]"
> **Fallback Position**: [If counterparty resists full redline, minimum acceptable language]
> **Business Impact**: [Quantified or qualified risk of accepting current language]

[Repeat for each clause category with findings]

---

## Missing Clauses

| Clause           | Classification     | Recommendation                          |
| ---------------- | ------------------ | --------------------------------------- |
| [Missing clause] | 🔴 RED / 🟡 YELLOW | Add [suggested language or AIA section] |

---

## State Law Overlay: [Project State]

| Issue          | State Rule              | Contract Compliance                     | Action   |
| -------------- | ----------------------- | --------------------------------------- | -------- |
| Anti-indemnity | [Statute + restriction] | [Compliant / Non-compliant / [VERIFY]]  | [Action] |
| Retainage cap  | [Statute + cap]         | [Compliant / Non-compliant / [VERIFY]]  | [Action] |
| Prompt payment | [Statute + timing]      | [Compliant / Non-compliant / [VERIFY]]  | [Action] |
| Lien law       | [Key rules]             | [Contract addresses / Does not address] | [Action] |

---

## Negotiation Strategy

### Tier 1 — Deal-Breaker (Must Resolve Before Signing)

1. [Issue]: [Brief description + AIA alternative]
2. [Issue]: [Brief description + AIA alternative]

### Tier 2 — Material (Negotiate in First Round)

1. [Issue]: [Brief description + fallback position]
2. [Issue]: [Brief description + fallback position]

### Tier 3 — Minor (Concede if Needed)

1. [Issue]: [Brief description]

---

## Automatic RED Triggers Check

| Trigger                                          | Present?              | Notes |
| ------------------------------------------------ | --------------------- | ----- |
| No-damage-for-delay in adverse state             | [Yes / No / N/A]      |       |
| Unconditional lien waivers before payment        | [Yes / No]            |       |
| Retainage above state cap                        | [Yes / No / [VERIFY]] |       |
| Broad-form indemnity with anti-indemnity statute | [Yes / No / [VERIFY]] |       |
| Right to suspend for non-payment waived          | [Yes / No]            |       |
| AIA form + edition year unverified               | [Yes / No]            |       |

---

[Glass Box Audit Trail — YAML block as specified above]
```

---

## Localization Notes

This skill is US-specific. For construction contracts in other jurisdictions:

- **UK**: Use `legalcode-construction-contract-review` (covers JCT, NEC4)
- **International (FIDIC)**: Use `legalcode-construction-contract-review` (covers FIDIC Red/Yellow/Silver)
- **Australia**: Use `legalcode-construction-contract-review` (covers AS 4000)

For US **public contracting** (federal FAR/DFAR contracts), this skill covers foundational
risk areas but does not substitute for FAR-specific review covering:

- Termination for Convenience (FAR 52.249-2)
- Changes clause (FAR 52.243-1)
- Disputes clause (FAR 52.233-1)
- Differing Site Conditions (FAR 52.236-2)
- Suspension of Work (FAR 52.242-14)

---

## Provenance

Created by Legalcode (2026-03-22). Original synthesis based on:

- AIA A201-2017 General Conditions (AIA, 2017 edition)
- AIA A101-2017, A102-2017, A133-2019, A401-2017, B101-2017 form analysis
- `legalcode-construction-contract-review` (general multi-jurisdiction skill) — structural patterns and quality frameworks adapted for US AIA context
- `legalcode-contract-review` (reference standard) — quality framework templates (Citation Quality Gates, Self-Interrogation, Confidence Scoring, Glass Box)
- Deep research on US state anti-indemnity statutes, mechanic's lien laws, retainage statutes, and prompt payment acts
- General US construction law principles: Spearin doctrine, concurrent delay, no-damage-for-delay, constructive change doctrine
- AIA contract family relationships and delivery method risk allocation

All statutory references marked [VERIFY] require state-specific verification before reliance.
