---
name: legalcode-uk-jct-nec-contract-review
description: 'Reviews UK construction contracts under JCT and NEC4 for England and Wales projects. Use
  when reviewing, negotiating, or advising on JCT Standard Building Contract (SBC/Q 2016 or 2024), JCT
  Design and Build Contract (DB 2016/2024), NEC4 Engineering and Construction Contract (ECC), or any contract
  governed by the Housing Grants, Construction and Regeneration Act 1996. Covers payment provisions, adjudication
  rights, extension of time, loss and expense, practical completion, defects liability, professional indemnity
  insurance, collateral warranties, and retention. Also use for Building Safety Act 2022 liability exposure,
  concurrent delay analysis, and smash-and-grab adjudication risk. Triggers on: JCT, NEC, NEC4, SBC, DB
  contract, construction contract review, HGCRA, Construction Act, adjudication, extension of time, practical
  completion, collateral warranty, retention, PI insurance construction, Building Safety Act construction.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode — UK JCT & NEC4 Construction Contract Review (England & Wales)

> **Disclaimer**: This skill provides a framework for AI-assisted review of UK construction
> contracts. It does not constitute legal advice. All outputs must be reviewed by a qualified
> solicitor or barrister practising in England and Wales before reliance. Statutory and case
> law references cited from memory carry hallucination risk — verify against authoritative
> sources (Westlaw UK, LexisNexis, BAILII) before relying on them. Construction law changes
> frequently through TCC judgments and legislative amendment; verify currency before acting.

---

## Purpose and Scope

This skill reviews construction contracts governed by English law (England & Wales) with
particular focus on JCT and NEC4 standard forms.

**Covers:**

- JCT Standard Building Contract with Quantities (SBC/Q 2016 / SBC/Q 2024)
- JCT Design and Build Contract (DB 2016 / DB 2024)
- NEC4 Engineering and Construction Contract (ECC), Options A–F
- Bespoke construction contracts incorporating HGCRA 1996 statutory requirements
- Clause-by-clause analysis across 12 construction-specific categories
- Risk classification: COMPLIANT / YELLOW / RED / STRUCTURAL-RISK
- Redlines with fallback positions and negotiation strategy
- Statutory compliance check (HGCRA 1996, Building Safety Act 2022, Defective Premises
  Act 1972 as amended)
- Glass Box audit trail

**Does not:**

- Cover Scottish law (separate construction law framework — use a Scotland-specific skill)
- Cover FIDIC, AIA, or AS 4000 forms (use the general legalcode-construction-contract-review skill)
- Provide legal advice or replace qualified construction solicitors
- Substitute for site inspection, quantity surveying, or technical engineering review

---

## Jurisdiction and Governing Law

**Governing law**: England and Wales.

**Primary statutes** (all references to England and Wales unless stated):

- Housing Grants, Construction and Regeneration Act 1996 (HGCRA) — as amended by the
  Local Democracy, Economic Development and Construction Act 2009 (LDEDCA)
- Building Safety Act 2022 (BSA 2022)
- Defective Premises Act 1972 (DPA 1972) — as amended by BSA 2022 s.135
- Limitation Act 1980 (LA 1980)
- Unfair Contract Terms Act 1977 (UCTA 1977)
- Late Payment of Commercial Debts (Interest) Act 1998
- Contracts (Rights of Third Parties) Act 1999 (CRTPA 1999)
- Arbitration Act 1996

**Key secondary legislation:**

- Scheme for Construction Contracts (England and Wales) Regulations 1998 (SI 1998/649)
  as amended by SI 2011/2333 (the "Scheme")

**Standard forms reviewed:**

- JCT SBC/Q 2024 and SBC/Q 2016 (measured works, traditional procurement)
- JCT DB 2024 and DB 2016 (design and build, single point responsibility)
- NEC4 ECC Options A (Priced, activity schedule), B (Priced, BoQ), C (Target cost,
  activity schedule), D (Target cost, BoQ), E (Cost reimbursable), F (Management contract)
- NEC4 with Option W2 (HGCRA adjudication) — mandatory for England and Wales

**Court of jurisdiction**: Technology and Construction Court (TCC), King's Bench Division,
High Court of Justice; appeals to Court of Appeal and UK Supreme Court.

---

## Interactive Clarification

This skill uses **interactive clarification** at decision points that change the direction
of the analysis. Wherever marked **⟁ CLARIFY**, pause and ask the user before proceeding.

Skip a CLARIFY question if the user has already provided the answer.

---

## Workflow

### Step 1: Accept the Contract

Accept input in any format:

- **File**: PDF, DOCX, or scanned document
- **URL**: link to a contract management system, SharePoint, or document portal
- **Pasted text**: contract text pasted directly
- **Form identification only**: "We are using JCT SBC/Q 2024 unamended" — proceed with
  the standard form analysis supplemented by any amendments described

If the contract is a non-standard bespoke form, confirm which standard form (if any) it
is based on — many bespoke construction contracts amend a JCT or NEC4 form substantially.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, gather this information. Present as structured
options where possible:

1. **Which party do you represent?**
   - Options: Employer/Developer, Main Contractor, Subcontractor, Funder/Mortgagee,
     End Purchaser/Tenant, Other
   - _Why this matters_: Payment, adjudication, retention, and EoT risk analysis
     reverses completely depending on which side the user is on.

2. **Standard form or bespoke?**
   - Options: JCT SBC/Q 2024 (unamended), JCT SBC/Q 2024 (with amendments), JCT SBC/Q
     2016, JCT DB 2024, JCT DB 2016, NEC4 ECC Option A, NEC4 ECC Option B, NEC4 ECC
     Option C, NEC4 ECC Option D, NEC4 ECC Option E, NEC4 ECC Option F, Bespoke/hybrid
   - _Why this matters_: Risk analysis differs markedly between JCT (employer-friendly,
     adversarial) and NEC4 (collaborative, compensation event regime).

3. **Project type and scale:**
   - Options: Commercial/retail, Residential (non-HRB), Residential (Higher Risk Building
     — 18m+ / 7 storeys+), Infrastructure, Mixed-use, Refurbishment, Civil engineering
   - Estimated contract value and programme duration
   - _Why this matters_: Building Safety Act 2022 applies specifically to Higher Risk
     Buildings (HRBs). Programme duration affects EoT and L&E exposure. Value determines
     retention amounts and insurance minima.

4. **Design responsibility:**
   - Options: Traditional (Employer designs, Contractor builds), Design and Build
     (Contractor responsible for design), Partially novated design, Professional team
     appointments alongside main contract
   - _Why this matters_: PI insurance requirements, fitness for purpose vs. reasonable
     skill and care obligations, and collateral warranty obligations differ entirely
     between traditional and D&B procurement.

5. **Focus areas (allow multiple):**
   - Payment / adjudication risk, Extension of time, Loss and expense, Practical completion,
     Defects liability, PI insurance, Collateral warranties, Retention, BSA 2022 exposure,
     Full review
   - _Why this matters_: Allows the analysis to lead with what matters most to the user.

6. **Playbook / negotiation position:**
   - Does the user have a standard position on key terms? If so, gather it before analysis.
   - _Why this matters_: Review against organizational positions is more useful than review
     against general market standards.

### Step 3: Identify the Form and Check HGCRA Compliance

Determine the standard form and edition. Then run the HGCRA 1996 statutory compliance
screen before clause-by-clause analysis.

**⟁ CLARIFY** — If the contract is bespoke or heavily amended:

- Ask whether any HGCRA-required provisions (adjudication, payment notices, suspension)
  have been excluded or modified
- A contract that excludes or restricts statutory adjudication rights has those terms
  automatically void (HGCRA s.108(5)) — this is an automatic STRUCTURAL-RISK flag

**HGCRA Statutory Compliance Screen:**

| Statutory Requirement                                                  | HGCRA Reference | JCT SBC/Q 2024                          | NEC4 W2             | Check |
| ---------------------------------------------------------------------- | --------------- | --------------------------------------- | ------------------- | ----- |
| Right to stage payments                                                | s.109           | Cl.4.8 (interim payments)               | Cl.50 (assessments) | □     |
| Payment notice within 5 days of due date                               | s.110A          | Cl.4.10 (payer/specified person notice) | Cl.51.1             | □     |
| Pay less notice: min 7 days before final date for payment              | s.111(3)        | Cl.4.12                                 | Cl.51.3             | □     |
| Adjudication right at any time                                         | s.108(1)        | Cl.9.2 (referral to adjudication)       | W2.1                | □     |
| Adjudicator appointed within 7 days of referral                        | s.108(2)(b)     | Art.8 / Schedule                        | W2.2                | □     |
| 28-day decision period                                                 | s.108(2)(c)     | Schedule                                | W2.4                | □     |
| Right to suspend for non-payment (7 days' written notice)              | s.112           | Cl.4.14                                 | Cl.91.4             | □     |
| "Pay now, argue later" — adjudicator's decision binding unless revised | s.108(3)        | Cl.9.2.3                                | W2.4                | □     |

If the Scheme applies (contract fails to satisfy HGCRA), note this prominently: the
Scheme's implied terms on payment and adjudication override the contract.

### Step 4: Gather Legal Authority

Use **legalcode-mcp** (if connected) to gather verified legal authority for the governing
law before analyzing specific clauses.

**Research priorities for UK construction:**

1. Current HGCRA 1996 text (as amended by LDEDCA 2009) — ss.104-113
2. Scheme for Construction Contracts SI 1998/649 as amended by SI 2011/2333
3. Building Safety Act 2022 ss.130-138 (DPA 1972 amendment, Higher Risk Buildings regime)
4. Defective Premises Act 1972 s.1 (as amended — current limitation periods)
5. Key TCC judgments for issues flagged (see Case Law Reference section)
6. JCT 2024 Practice Notes (if available via legalcode-mcp)

Save results to `/tmp/legalcode-uk-construction-authority.md`.

**Without legalcode-mcp:**

- Mark all statute section references [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Proceed using the Case Law Reference and Statutory Framework sections in this skill,
  treating them as starting points for counsel's independent verification

### Step 5: Clause-by-Clause Analysis

Read the full contract before flagging issues — construction contracts have complex clause
interactions (e.g., a broad payment notice regime may partially mitigate a harsh pay-less
notice provision; EoT Relevant Events interact with loss and expense grounds).

**⟁ CLARIFY** — For contracts over 50 pages, or with multiple schedules, annexes, or
incorporated subcontracts:

- Ask whether to perform a **full review** of all 12 clause categories or a **priority
  review** focused on the user's stated focus areas plus any STRUCTURAL-RISK items
- If the contract incorporates a Schedule of Third Party Rights or Collateral Warranty
  schedule, ask whether those require separate analysis

Cover the 12 construction clause categories below. Flag deviations against market standard
for the identified form.

| #   | Clause Category                            | Depth    | Key Review Points                                                                    |
| --- | ------------------------------------------ | -------- | ------------------------------------------------------------------------------------ |
| 1   | Payment Regime                             | Deep     | HGCRA compliance, due dates, payment notices, pay less notices, smash-and-grab risk  |
| 2   | Adjudication                               | Deep     | Statutory compliance, notice procedure, enforcement, natural justice, insolvency     |
| 3   | Extension of Time                          | Deep     | Relevant events / compensation events, notice conditions precedent, concurrent delay |
| 4   | Loss and Expense / Compensation Events     | Deep     | Grounds, notice, quantification, global claims, NEC4 schedule of cost components     |
| 5   | Practical Completion                       | Deep     | Definition, certificate, effects, sectional completion, snagging                     |
| 6   | Defects Liability                          | Deep     | DLP duration, obligations, latent defects, Defective Premises Act, BSA 2022          |
| 7   | Liquidated Damages                         | Standard | Rate, genuine pre-estimate, Triple Point accrual, prevention principle interaction   |
| 8   | PI Insurance                               | Deep     | Requirement, scope, claims-made/occurrence, single/aggregate basis, net contribution |
| 9   | Collateral Warranties / Third-Party Rights | Deep     | Forms required, step-in rights, assignment, limitation periods                       |
| 10  | Retention                                  | Standard | Rate, release triggers, retention trust, PBA requirement                             |
| 11  | Insurance (Works / CAR / Public Liability) | Standard | Options A/B/C (JCT), joint names, employer's risks, cross-liability                  |
| 12  | Termination                                | Standard | Grounds, notice, payment on termination, re-entry rights, insolvency                 |

### Step 6: Missing Provision Detection

After analyzing present clauses, identify important provisions that are entirely absent.

Critical missing provisions in construction contracts (England and Wales):

- No adjudication right / defective adjudication procedure → STRUCTURAL-RISK (void under HGCRA s.108)
- No payment notice mechanism → STRUCTURAL-RISK (Scheme applies, default payment amount rule)
- No PI insurance requirement in a D&B contract → RED
- No collateral warranties / third-party rights schedule when funder or end-purchaser is involved → RED
- No EoT mechanism → STRUCTURAL-RISK (time goes "at large", LDs unenforceable)
- No fluctuations clause in a long-term contract (inflation risk unallocated) → YELLOW
- No Building Safety Act acknowledgment on an HRB project → RED
- No retention trust provisions where retention is held → YELLOW

### Step 7: Classify and Generate Redlines

Classify each deviation using the four-tier system in the **Severity Classification** section.
For each YELLOW and RED issue, generate a redline using the **Redline Format**.

**⟁ CLARIFY** — For borderline classifications, ask rather than assume:

- Is the user's risk tolerance high or low for this project? (A contractor on a cost-plus
  NEC4 Option E has different exposure than a fixed-price JCT SBC/Q lump-sum contractor)
- For pay-less notice risk: "The employer's pay-less notice procedure looks tight — is
  this a concern worth pushing back on, or is the cash flow manageable?"
- For EoT concurrent delay: "The contract excludes contractor entitlement during concurrent
  delay (similar to _North Midland v Cyden Homes_). Is this acceptable to your client, or
  a must-push-back?"

### Step 8: Business Impact and Negotiation Strategy

Provide a prioritised summary of findings:

- **Overall risk profile**: HIGH / MEDIUM / LOW with brief rationale
- **Top 3 issues**: severity, estimated financial exposure, recommended action
- **Negotiation sequence**: lead with STRUCTURAL-RISK and RED items; use YELLOW items as
  trading currency; identify Tier 3 concessions
- **BSA 2022 exposure note**: flag any extended limitation period exposure relevant to the
  project type

**⟁ CLARIFY** — Before finalizing strategy:

- **Walk-away**: Can the user decline the project if critical amendments are rejected?
- **Precedent risk**: Is this a template the employer will use on all projects? (If so,
  precedent value of amendments is high)
- **Programme constraints**: Is there a tender deadline that limits negotiation time?

### Step 9: Quality Verification

Before delivering output, run the full Quality Assurance Framework:

1. Run the 5 Citation Quality Gates silently
2. For every RED or STRUCTURAL-RISK item, run the 3-pass Self-Interrogation
3. Assign Confidence Scores to all material clause analyses
4. Verify all 12 clause categories addressed or flagged as absent
5. Generate Glass Box Audit Trail

---

## Clause Analysis Reference — UK Construction

### 1. Payment Regime

**Statutory framework**: HGCRA 1996 ss.109–111 (as amended by LDEDCA 2009 ss.142-145);
Scheme for Construction Contracts SI 1998/649 Part II.

**Key elements to review:**

**Due dates and payment cycle:**

- Is the contract a "construction contract" under HGCRA s.104? (Most E&W construction
  contracts — note: residential occupier contracts under s.106 are excluded from payment
  and adjudication provisions)
- Confirm the "due date" for each payment (HGCRA s.110(1)(a)) — must be fixed
- Confirm the "final date for payment" — the last date the sum may be paid without breach
- JCT SBC/Q 2024 cl.4.8: interim valuations monthly; due date = 7 days after valuation date

**Payment notices:**

- **Payer's payment notice** (s.110A): must be given not later than 5 days after the due
  date, stating the sum the payer considers due and the basis of calculation
- **Payee's default payment notice** (s.110B): if payer fails to serve, payee may serve;
  amount in payee's notice becomes the "notified sum" unless a pay less notice is served
- **Pay less notice** (s.111): must be served not less than 7 days before the final date
  for payment; must state the sum the payer considers due and basis; failure = "smash and
  grab" adjudication risk (full notified sum becomes due regardless of merits)
- JCT SBC/Q 2024 cl.4.10: payment notice by employer or specified person within 5 days of
  due date; cl.4.12: pay less notice not less than 7 days before final date for payment

**Common RED flags:**

- Pay less notice period shorter than 7 days → void under s.111 (Scheme Part II para.10
  applies automatically)
- Notice requirements that are conditions precedent beyond the statutory minimum → may be
  unenforceable if they override HGCRA rights
- "No dispute on the face of invoice" payment conditions (pay-when-certified clauses) → RED
  if they effectively remove stage payment entitlement
- Employer retains right to set-off without pay less notice → RED (void under s.111)
- Missing or defective payment notice mechanism → Scheme applies automatically

**"Smash and grab" adjudication risk:**
The critical risk for employers/contract administrators: if a valid pay less notice is not
served by the prescribed deadline, the contractor is entitled to the full notified sum
(from the application/payee default notice) by summary judgment, irrespective of the true
value of works (_ISG Construction Ltd v Seevic College_ [2014] EWHC 4007 (TCC) [VERIFY]).
This risk must be managed procedurally, not legally — ensure the client's payment notice
and pay less notice processes are watertight in practice.

**NEC4 distinction:** NEC4 clause 50 (payment) and 51 (certification) have their own
assessment regime — the Project Manager assesses the amount due at each assessment
interval (typically monthly). Option W2 provides the HGCRA-compliant adjudication route.
Under NEC4, the PM's certificate is the payment notice for HGCRA purposes.

**Confidence**: HIGH (0.85) — HGCRA text is settled; smash-and-grab case law position is
well-established in TCC. [VERIFY specific case citations against BAILII]

---

### 2. Adjudication

**Statutory framework**: HGCRA 1996 s.108; Scheme for Construction Contracts SI 1998/649
Part I; JCT SBC/Q 2024 cl.9.2 and Schedule; NEC4 Option W2.

**Statutory right (s.108):**

- Any party to a "construction contract" (HGCRA s.104) has the right to refer a dispute
  to adjudication at any time
- Contract must provide: notice of intention to refer, adjudicator appointed within 7 days
  of referral, decision within 28 days of referral (extendable by 14 days with referring
  party's consent, or longer with both parties' consent)
- Adjudicator's decision: binding until revised by arbitration, litigation, or agreement
  ("pay now, argue later")
- Any contractual provision that purports to restrict the statutory right is void (s.108(5))

**Key elements to review:**

- Does the adjudication clause track HGCRA s.108 or is it more restrictive? (If more
  restrictive → relevant provisions void, Scheme applies instead)
- Adjudicator nominating body identified? (JCT: RICS, RIBA, CIArb, ICE or agreed; NEC4
  W2: agreed or RICS/CIArb)
- Is the procedure clearly defined (referral + response timelines, document submissions)?
- Is there a stepped pre-adjudication procedure? (Some bespoke contracts require
  "senior representative" negotiation first — permissible if this does not delay the
  right to adjudicate)
- NEC4 W2.4: decision within 28 days of referral (extended to 42 days with consent of
  referring party, or longer if both parties agree)

**Enforcement:**

- Adjudication decisions are enforced by TCC on summary judgment under CPR Part 24 [VERIFY]
- A defendant may resist enforcement only on narrow grounds:
  - The adjudicator had no jurisdiction (wrong dispute, wrong parties)
  - Breach of natural justice (adjudicator decided more than referred; failed to give party
    opportunity to respond to a point; apparent bias) — _Workplace Technologies v E Squared_
    [2017] EWHC 2045 (TCC) [VERIFY]
  - Decision is unintelligible (very rare)
- **"Smash and grab" enforcement**: separate from true value adjudication — employer who
  loses on smash and grab cannot prevent enforcement by launching a true value adjudication
  simultaneously (_ISG v Seevic_ [VERIFY])
- Carillion Construction Ltd v Felix (UK) Ltd [2001] BLR 1: court enforced adjudicator's
  decision even where it was arguably wrong in law — "pay now, argue later" is
  fundamental [VERIFY]
- Macob Civil Engineering v Morrison Construction Ltd [1999] BLR 93: first enforcement
  case, established the "pay now, argue later" principle [VERIFY]
- Bresco Electrical Services Ltd v Michael J Lonsdale (Electrical) Ltd [2021] UKSC 25:
  insolvent party can still exercise statutory right to adjudicate [VERIFY]

**Common RED flags:**

- No adjudication right in a HGCRA-covered contract → void, Scheme applies (automatic
  STRUCTURAL-RISK — note for the record even if benign in outcome)
- "Tolling" or "standstill" agreements that purport to suspend the adjudication right
  during negotiation → void unless genuinely consensual and time-limited
- Adjudicator appointment mechanism that would take more than 7 days → Scheme applies
- Adjudicator's decision made "final and binding" (not just interim binding) without
  provision for litigation/arbitration override → potentially void under s.108(3) [VERIFY]
- Adjudication limited to payment disputes only → restriction of statutory right, void
- Requirement to exhaust other dispute resolution steps before adjudication → void if it
  delays access to adjudication (unless structured as genuinely parallel tracks)

**Confidence**: HIGH (0.82) — statutory framework well-settled; case law citations require
BAILII verification [VERIFY]

---

### 3. Extension of Time

**Standard forms**: JCT SBC/Q 2024 cl.2.26–2.32; NEC4 ECC cl.60.1 (compensation events);
SCL Delay and Disruption Protocol 2nd Edition (2017).

**JCT SBC/Q 2024 — Relevant Events (cl.2.29):**
Grounds for EoT under JCT include (non-exhaustive — verify against contracted edition):

- Force majeure
- Exceptionally adverse weather conditions (contractor risk for ordinary weather)
- Loss or damage to works by employer's risks (cl.6.3 perils)
- Civil commotion, acts of terrorism
- Employer's instructions (opening up, postponement, expenditure of provisional sums)
- Failure by employer to give access by the access date
- Delay by employer's persons / statutory undertakers under employer's control
- Delay in receipt of necessary nominations
- Suspension by contractor under HGCRA s.112
- Act of prevention by employer (underpins the prevention principle)

**Notice requirements (JCT cl.2.27):**

- Contractor must give written notice to architect/contract administrator "as soon as it
  becomes or should reasonably become apparent" that completion is likely to be delayed
- Notice must identify the Relevant Event(s) and the expected delay
- Failure to give notice does not forfeit EoT entitlement under JCT (notice is not
  generally a condition precedent to EoT under JCT — contrast with NEC4) [VERIFY]
- Architect must fix new completion date within 12 weeks of notice or receipt of sufficient
  particulars, or by PC if earlier (cl.2.28.6)

**NEC4 — Compensation Events (cl.60.1):**
NEC4 uses a different regime: "compensation events" give entitlement to both time and
cost (unlike JCT which separates EoT and loss & expense). Key compensation events include:

- PM gives an instruction changing the works information (cl.60.1(1))
- Employer does not provide access (cl.60.1(2))
- PM instructs stop work or does not reply to communication (cl.60.1(4))
- Work conditions materially differ from those stated (cl.60.1(12) — physical conditions)
- Adverse weather beyond reference period (cl.60.1(13))
- Employer's risk events (cl.80.1)

**NEC4 notice discipline (cl.61.3):**

- Contractor must notify a compensation event within 8 weeks of becoming aware of it
  (this IS a condition precedent — failure bars the compensation event claim under NEC4)
- PM must respond within 1 week; contractor then submits quotation within 3 weeks
- Accepted programme is critical: early warning events (cl.15) and delays must be flagged
  through the Early Warning Register
- Failure to maintain or update the Accepted Programme significantly weakens contractor's
  position on EoT and cost claims

**Concurrent delay:**

- Concurrent delay = two or more delaying events, one employer-caused and one contractor-caused,
  operating at the same time and each independently causing delay to completion
- English law approach (JCT): contractor gets full EoT for the employer-caused event
  without reduction for the concurrent contractor-caused delay — _Henry Boot Construction
  (UK) Ltd v Malmaison Hotel (Manchester) Ltd_ [2000] 70 Con LR 32 [VERIFY]
- Express contractual exclusion of EoT during concurrent delay is enforceable in English
  law — _North Midland Building Ltd v Cyden Homes Ltd_ [2018] EWCA Civ 1744 [VERIFY]
  — but contractor loses EoT entitlement for the overlap period only
- Contractor does NOT get prolongation costs during concurrent delay (only the time) even
  where entitled to EoT — _Walter Lilly & Co Ltd v Mackay_ [2012] EWHC 1773 (TCC) [VERIFY]
- Prevention principle: if employer prevents completion and no valid EoT mechanism is
  available to account for that prevention, time goes "at large" — LDs become
  unenforceable; contractor's obligation becomes to complete within a reasonable time —
  _Peak Construction (Liverpool) Ltd v McKinney Foundations Ltd_ [1970] 1 BLR 111 [VERIFY]

**SCL Protocol 2nd Edition (2017):**

- Core Principle 1: Float is owned by the first party that needs to use it
- Core Principle 10: Concurrent delay — EoT for employer-caused event even if
  simultaneous contractor risk (aligns with Henry Boot)
- Core Principle 12: Global claims generally unacceptable without a genuine attempt at
  particularisation — but a global claim may succeed where it is impossible to disentangle
  individual causes (_Walter Lilly_ [VERIFY])

**Common RED flags:**

- Notice of delay as a condition precedent to EoT in a JCT contract → RED (inconsistent
  with JCT scheme; may be unenforceable as penalty or contrary to prevention principle)
- No EoT mechanism at all → STRUCTURAL-RISK (time goes "at large", LDs unenforceable)
- Concurrent delay exclusion clause (contractor loses EoT for entire delay period, not
  just overlap) → RED (overreaching, not aligned with Cyden Homes)
- Employer retains unilateral right to fix or refuse EoT without objective criteria → RED
- 8-week notification condition precedent in NEC4 not reflected in bespoke contract that
  imports NEC4 concepts → YELLOW (ambiguity about condition precedent status)
- No reference to SCL Protocol where parties have agreed to use it → YELLOW

**Confidence**: PROBABLE-HIGH (0.78) — core principles settled; concurrent delay nuances
depend on specific clause wording [VERIFY case citations]

---

### 4. Loss and Expense / Compensation Events

**Standard forms**: JCT SBC/Q 2024 cl.4.20–4.26 (loss and expense); NEC4 ECC cl.63
(assessment of compensation events).

**JCT SBC/Q 2024 — Loss and Expense (cl.4.20–4.26):**

**Grounds (cl.4.21 — Relevant Matters):**

- Variations
- Provisional sum instructions
- Failure by employer/architect to provide information on time
- Delay in receipt of necessary instructions from employer
- Opening up for inspection where work found not defective
- Postponement instructions
- Employer preventing access
- Failure to perform statutory undertaker obligations under employer's control
- Suspension under HGCRA s.112
- Material change in conditions not caused by contractor

**Procedure:**

- Contractor must make written application as soon as it has become (or should have become)
  reasonably apparent that progress has been materially affected (cl.4.20)
- Application must be particularised — vague or global applications may be rejected
- Architect/QS has a duty to ascertain or instruct ascertainment of the amount (cl.4.23)
- Loss and expense is recoverable only for actual direct loss and/or expense — no profit
  element, no consequential loss beyond what directly flows from the Relevant Matter
- Interest: _Walter Lilly_ held that financing charges are recoverable as loss and expense
  under JCT [VERIFY]
- Global or "rolled-up" claims: acceptable where impossible to disentangle, but claimant
  must show: (a) all events relied upon give rise to L&E; (b) causation proven in aggregate;
  (c) loss proven — _Walter Lilly_ [VERIFY]

**NEC4 — Compensation Event Assessment (cl.63):**

- Assessed using Defined Cost (actual or forecast, per Schedule of Cost Components — SCC
  or SSCC for Options A/B) plus Fee (percentage uplift)
- Programme impact assessed against the Accepted Programme
- If contractor fails to submit a quotation on time, PM may assess — contractor loses
  control of the valuation process
- NEC4's "pain/gain share" (Option C/D) means compensation events affect the target cost
  and therefore the gain-share calculation — critical for contractor's financial model

**Common RED flags:**

- Notice as condition precedent to L&E claim in JCT → YELLOW/RED depending on wording
  (time-bar provisions are enforceable if clear, but contested)
- Exclusion of financing charges as recoverable L&E → YELLOW (inconsistent with Walter
  Lilly [VERIFY])
- Cap on L&E recovery that is not correlated to actual exposure → RED
- Global claim bar without exception for impossible-to-particularise situations → RED
- NEC4: PM assessment rights where contractor fails to submit on time — bespoke amendment
  that removes or extends PM assessment right → YELLOW

**Confidence**: PROBABLE (0.72) — core principles established; quantification methodology
is fact-specific and expert-dependent [VERIFY]

---

### 5. Practical Completion

**Standard forms**: JCT SBC/Q 2024 cl.2.27, cl.2.30–2.31; NEC4 ECC cl.30.2 (Completion),
cl.43 (Defects), cl.44 (Accepting Defects).

**JCT — Definition and certificate:**

- JCT SBC/Q 2024 does not define "Practical Completion" in the contract — it remains a
  question of fact and degree
- Leading cases:
  - _Westminster CC v Jarvis & Sons Ltd_ [1970] 1 WLR 637 (HL): "Practical completion means
    the completion of all the construction work that has to be done" but with the ability to
    accept work that is "practically complete" despite minor defects [VERIFY]
  - _Mears Ltd v Costplan Services (South East) Ltd_ [2019] EWCA Civ 502: three propositions
    on PC — (1) there must be completion of the works in a real sense; (2) de minimis rule
    applies; (3) Architect/CA has a limited discretion; (4) defects known at PC date can be
    listed and dealt with during DLP [VERIFY]
  - _Tak v Gupta_ [2020]: confirms that "snagging items" do not necessarily prevent PC if
    they are truly minor [VERIFY] — but employer has no obligation to certify PC until
    works are practically complete
- Architect/CA must certify PC — cannot be unreasonably withheld once the threshold is met
- Employer cannot refuse to certify PC to hold contractor in a commercially disadvantageous
  position (estoppel / Prevention Principle)
- **Snagging lists**: employers sometimes attach snagging lists to PC certificates; JCT
  permits this. Outstanding items on a snagging list do not prevent PC if they are minor.
  But items that are not merely minor → contractor is not entitled to PC certificate.

**Effects of Practical Completion certificate:**

- Liquidated damages cease to accrue (cl.2.32.2) — date of PC is the date LDs stop
- First half of retention released (employer must release within 14 days) (cl.4.18)
- Defects Liability Period starts (typically 12 months from PC date)
- Risk of damage to works passes to employer (cl.6.7)
- Frost damage and insurance risk generally passes to employer
- Contractor's obligation to maintain site insurance ceases

**Sectional completion:**

- JCT SBC/Q 2024 and DB 2024 include sectional completion options in the Contract Particulars
- Each section has its own PC date, LDs regime, retention release, and DLP
- If sectional completion is important, ensure all sections are identified with precise
  definitions and unambiguous boundaries

**NEC4 — Completion vs. Practical Completion:**

- NEC4 uses "Completion" (cl.30.2) — when the contractor has done all the work the
  Works Information requires, and corrected notified Defects — no concept of "Practical"
  completion
- PM certifies Completion within 1 week of it occurring
- Defects after Completion are notified during the Defects Correction Period (Option X12)
- NEC4's regime is more objective — Completion is defined in the Works Information and
  less susceptible to architect discretion arguments

**Common RED flags:**

- Employer's right to refuse PC certificate without objective criteria → RED
- LDs continue to accrue after PC until "making good defects" → RED (overclaiming; LDs
  should stop at PC)
- Retention first moiety not released promptly on PC → YELLOW
- No sectional completion despite multi-phase delivery → YELLOW
- "Substantial completion" language in a JCT-based bespoke contract (a US concept —
  inconsistent with English law PC framework) → YELLOW

**Confidence**: HIGH (0.80) — PC framework well-established; discretion questions are
fact-specific [VERIFY Mears, Tak v Gupta citations]

---

### 6. Defects Liability

**Statutory framework**: Defective Premises Act 1972 s.1 (as amended by BSA 2022 s.135);
Limitation Act 1980 ss.2, 5, 8; Building Safety Act 2022 Part 4.

**Contractual defects liability:**

- JCT SBC/Q 2024 cl.2.38–2.41: Rectification Period (typically 12 months from PC)
- During the Rectification Period, architect/CA may instruct contractor to rectify defects
- Employer's option to have defects made good by others and deduct cost if contractor fails
  to comply within reasonable time (cl.2.40)
- Architect issues Certificate of Making Good when all defects remedied → triggers second
  retention moiety release (cl.4.18.3)
- NEC4: Defects Correction Period — PM notifies defects (cl.42); contractor corrects
  within the defect correction period; Defects Certificate issued (cl.44)

**Latent defects (post-DLP):**

- Defects appearing after the DLP fall under general contract law — limitation period
  under LA 1980:
  - Simple contract (signed under hand): 6 years from the date of breach (LA 1980 s.5)
  - Deed: 12 years from the date of breach (LA 1980 s.8)
  - Commencement of limitation: for latent defects, from the date damage first manifests
    or would be discoverable with reasonable diligence (Latent Damage Act 1986 for
    negligence-based claims: 3 years from knowledge, 15 years long-stop)

**Defective Premises Act 1972 s.1 (as amended by BSA 2022 s.135):**

- Imposes a duty on those involved in the provision of dwellings to do the work in a
  workmanlike manner, with proper materials, so the dwelling is fit for habitation
- **BSA 2022 s.135 extended limitation periods** [VERIFY against current BSA text]:
  - New dwellings completed on or after 28 June 2022: 15 years from completion
  - Existing dwellings (pre-28 June 2022): 30 years from completion (retrospective —
    claims that would have been time-barred under the previous 6-year period are revived)
  - This retrospective extension is significant for all contractors and designers who
    worked on residential buildings in England and Wales
- DPA 1972 applies to: builders, developers, architects, surveyors and others involved in
  the "provision" of a dwelling — cannot be excluded by contract (s.6(3) DPA 1972)

**Building Safety Act 2022 — Higher Risk Buildings (HRBs):**

- HRBs defined: buildings in England that are at least 18 metres or 7 storeys in height
  and contain at least 2 residential units (BSA 2022 s.65) [VERIFY]
- Duty-holder regime: accountable person, principal contractor, principal designer (new
  requirements in addition to CDM 2015)
- Building Control approval regime: approved inspector regime replaced for HRBs by the
  new Building Safety Regulator (Health and Safety Executive)
- Gateway process (BSA 2022 Part 3): Gateway 1 (planning), Gateway 2 (design approval
  before construction), Gateway 3 (completion)
- The BSA 2022 obligations are statutory duties — they cannot be contracted out of

**PI insurance and BSA 2022 interaction:**

- Extended limitation periods (15/30 years DPA) create significant PI tail risk
- PI policies are typically claims-made — any claim brought after the policy expires is
  uninsured unless run-off cover is maintained
- Contractors and design professionals on residential projects should maintain run-off
  cover for 15+ years post-completion (30 years for pre-2022 projects)
- Insurance market has hardened for residential construction PI post-BSA 2022 [VERIFY]

**Common RED flags:**

- DLP shorter than 12 months → YELLOW (below market standard)
- No Certificate of Making Good mechanism → YELLOW (unclear trigger for second retention)
- Contractor's liability for defects excluded after DLP → RED (if it extends to DPA 1972
  obligations, unenforceable under DPA 1972 s.6(3))
- No PI run-off provision for D&B contractor on residential projects → RED
- No BSA 2022 duty-holder provisions on HRB project → RED
- No provision for Building Safety Regulator gateway approvals on HRB project → RED

**Confidence**: PROBABLE-HIGH (0.80) — DPA 1972 / BSA 2022 framework verified; specific
BSA 2022 limitation period figures [VERIFY against current legislation on legislation.gov.uk]

---

### 7. Liquidated Damages

**Standard forms**: JCT SBC/Q 2024 cl.2.29, cl.2.32; NEC4 Option X7.

**Key elements:**

- Rate: expressed as £[amount] per week (or day) of delay beyond the completion date
- Must be a genuine pre-estimate of loss at the time of contracting — not a penalty
  (Cavendish Square Holding BV v Talal El Makdessi [2015] UKSC 67 — LD is valid if it
  protects a legitimate business interest and is not extravagant and unconscionable
  compared to that interest) [VERIFY]
- Rate must appear in the Contract Particulars (JCT) or Accepted Programme (NEC4 X7)
- If LDs are "at large" (rate blank, or mechanism fails), employer's remedy is general
  damages for delay — harder to prove and quantify

**Triple Point Technology v PTT Public Company Ltd [2021] UKSC 29:**

- Supreme Court settled the question of LD accrual when the contract is terminated before
  completion:
  - LDs accrue from the original completion date to the date of termination
  - If the contractor never achieves completion, LDs accrue up to termination only —
    employer's remedy for loss after termination is general damages for the cost of
    getting completion by others [VERIFY]
- Under JCT SBC/Q 2024 cl.2.32.1: LD deduction mechanism is by employer's written notice;
  employer must give notice before the Final Certificate

**Prevention principle interaction:**

- If employer's acts cause delay but no EoT mechanism covers them, LDs clause is
  void — time goes "at large" (_Dodd v Churton_ [1897] 1 QB 562 [VERIFY])
- Ensure all acts of prevention by employer are covered by Relevant Events in the EoT
  clause (JCT SBC/Q 2024 generally achieves this — verify on bespoke contracts)

**Common RED flags:**

- LD rate that is clearly extravagant relative to likely loss (e.g., 10% of contract value
  per week) → RED (penalty; likely void under Cavendish Square test)
- No LD rate stated ("nil" or "TBC") → YELLOW (employer cannot recover LDs without a rate;
  must rely on general damages)
- LD notice requirements not satisfied → RED (employer cannot deduct without proper notice)
- LDs drafted to survive termination and continue to accrue post-termination → RED
  (inconsistent with Triple Point [2021] UKSC 29)
- Sectional LDs where sections are not clearly defined → YELLOW (risk of LDs failing)

**Confidence**: HIGH (0.83) — Triple Point UKSC settled key question; Cavendish Square
is established [VERIFY citations]

---

### 8. Professional Indemnity Insurance

**Relevance**: Arises on design-and-build contracts, partially novated design, or where
contractor assumes design responsibility for any part of the works.

**Key elements to review:**

**Requirement and scope:**

- Is there a PI insurance requirement? If contractor has design responsibility and no PI
  requirement → automatic RED
- Level of liability: "reasonable skill and care" (consistent with PI cover) vs. "fitness
  for purpose" (higher standard, typically uninsured by standard PI policies)
  - JCT DB 2024 cl.2.17.1: design obligation is reasonable skill and care (not FfP) —
    this is market standard and consistent with PI coverage
  - NEC4 Option X15 (if included): limits contractor's design liability to reasonable skill
    and care (absent X15, the NEC4 implied standard may be higher — [VERIFY])
  - A bespoke contract that imposes FfP on a D&B contractor while requiring PI insurance
    creates an uninsurable gap — automatic RED trigger

**Level of cover:**

- Minimum recommended levels [VERIFY against current RIBA/RICS/ICE guidance]:
  - Small projects (<£1M): typically £1M–£2M per claim
  - Medium projects (£1M–£10M): typically £5M–£10M per claim
  - Large projects (£10M+): bespoke — often 100–150% of contract sum
  - HRBs: consider 30-year DPA tail risk in setting minimum cover level

**Claims-made vs. occurrence basis:**

- Nearly all PI policies in UK are **claims-made**: cover applies to claims made during
  the policy period, not when the event causing loss occurred
- A contractor whose PI policy lapses after practical completion has no cover for claims
  made after expiry, even if the defective work occurred during the project
- **Run-off cover**: post-completion PI insurance to cover claims arising from the project
  during the extended limitation period (15 or 30 years under DPA/BSA 2022)
- JCT DB 2024 cl.6.11: contractor must maintain PI insurance "for such period after the
  date of practical completion as specified in the Contract Particulars" — ensure this
  aligns with DPA 1972 limitation periods

**Single vs. aggregate basis:**

- **Single (per occurrence/per claim)**: each claim is covered up to the policy limit —
  more expensive but provides full coverage for multiple claims
- **Aggregate**: all claims in the policy year share a single limit — cheaper but
  potentially inadequate if multiple claims arise

**Net contribution clauses:**

- Many PI policies include net contribution clauses limiting the insurer's contribution
  to the policyholder's proportionate share of liability
- Where a contractor and design consultants are jointly liable, the employer may recover
  less if individual policies have net contribution clauses — check whether joint and
  several liability applies or whether proportionate liability applies

**Common RED flags:**

- FfP obligation + PI insurance requirement (uninsurable gap) → STRUCTURAL-RISK (automatic
  RED — client must be advised immediately)
- No run-off cover requirement on a residential/HRB project → RED
- PI level clearly insufficient for project scale → RED
- Claims-made basis not understood by client → YELLOW (disclosure/education required)
- Contractor's obligation to "use reasonable endeavours" to maintain PI (rather than "shall
  maintain") → YELLOW (insufficient — must be an absolute obligation)
- No obligation to provide evidence of insurance (certificate) before construction starts
  or on renewal → YELLOW

**Confidence**: HIGH (0.82) — PI insurance principles well-established; specific policy
market conditions and current guidance minima [VERIFY against current RIBA/RICS publications]

---

### 9. Collateral Warranties and Third-Party Rights

**Statutory framework**: Contracts (Rights of Third Parties) Act 1999 (CRTPA 1999).

**Why they matter:**

- Funders, purchasers, and tenants often have no contractual relationship with the
  contractor, subcontractors, or professional team
- Without a collateral warranty or third-party rights schedule, they cannot sue directly
  for defective works — they rely on the developer's assignment of rights (limited and
  uncertain)
- Collateral warranties give third parties direct enforceable rights against the warrantor

**JCT standard collateral warranty forms:**

- **CWa/E** (Contractor's Collateral Warranty for a Funder — Employer): warranty from main
  contractor to employer's funder
- **CWa/P&T** (Contractor's Collateral Warranty for a Purchaser and/or Tenant — Employer):
  warranty from main contractor to purchaser or tenant
- **SCWa/E** and **SCWa/P&T**: subcontractor equivalents
- **MCWa/F** and **MCWa/P&T**: management contractor equivalents

**Key terms in collateral warranties:**

- **Standard of care**: warrantor owes same standard of care as under the main contract
  (reasonable skill and care, not FfP — unless main contract imposes FfP)
- **Deleterious materials exclusion**: warrantor has not used and will not use specified
  deleterious materials (NHBC or project-specific schedule) — check list is current
- **PI insurance obligation**: warrantor maintains PI insurance for a specified period —
  ensure this aligns with the limitation period for the warranty
- **Copyright/IP licence**: licence to use design documents for the project purpose
- **Step-in rights** (funder warranties): funder may step in and "take over" the main
  contract on the contractor's insolvency or employer's default — notice procedure,
  conditions, obligation to remedy defaults as a condition of stepping in
- **Assignment**: how many times may the warranty be assigned without consent?
  - Market standard: typically 2 assignments without consent; further assignments require
    warrantor's consent (not unreasonably withheld)
  - Linden Gardens Trust Ltd v Lenesta Sludge Disposals Ltd [1994] 1 AC 85: assignment of
    benefit of building contract requires no consent (CRTPA position) but consent clause
    in the contract must be respected [VERIFY]

**Alternative: Schedule of Third-Party Rights (CRTPA 1999):**

- JCT 2024 forms include a Schedule of Third Party Rights as an alternative to collateral
  warranties — simpler to administer, avoids need for multiple separate documents
- Under CRTPA 1999 s.1, a third party named or sufficiently described in the contract can
  enforce terms expressed to confer a benefit on them
- A Schedule of Third Party Rights in the building contract can grant funders, purchasers,
  and tenants equivalent rights to a collateral warranty — quicker to execute, avoids
  "warranty collection" project management
- However, lenders may still prefer a separate deed of warranty (traditional preference —
  verify with funder's lawyers)

**Limitation periods for collateral warranties:**

- Deed: 12 years from the breach (LA 1980 s.8)
- Simple contract: 6 years (LA 1980 s.5)
- Execute major funders' and purchasers' warranties as deeds — ensures maximum limitation
  period and avoids argument
- BSA 2022 DPA extensions do not generally affect collateral warranty limitation periods
  (which run from breach of the warranty, not from PC) — [VERIFY]

**Common RED flags:**

- No collateral warranty or Schedule of Third Party Rights where funder requires it →
  RED (funder will not permit drawdown without it; deal-stopper)
- Fitness for purpose standard in collateral warranty when contractor has PI cover only
  for reasonable skill and care → RED (creates uninsured gap in warranty)
- No PI insurance obligation in collateral warranty → RED
- Step-in right not triggered until after insolvency (too late for funder to take practical
  action) → YELLOW (consider earlier trigger — e.g., notice of default)
- Collateral warranty caps liability at an amount inconsistent with the PI cover level →
  YELLOW
- Warranty executed as simple contract not deed where funder requires maximum limitation
  period → YELLOW
- Deleterious materials list not updated (still lists materials no longer relevant or misses
  current concerns) → YELLOW

**Confidence**: HIGH (0.81) — framework well-established; CRTPA Schedule alternative is
established JCT 2024 practice [VERIFY Linden Gardens citation]

---

### 10. Retention

**Standard**: 5% reducing to 2.5% on Practical Completion; moieties released at PC
(first half) and Certificate of Making Good (second half) — JCT SBC/Q 2024 cl.4.18.

**Key elements to review:**

- **Rate**: Is it 5%/2.5% or higher? Rates above 5% are above market standard → YELLOW
- **Release triggers**: Are they objective? Employer discretion on retention release is
  unenforceable
- **Retention trust**: Under JCT SBC/Q 2024 cl.4.18.5: the employer holds retention as
  trustee for the contractor — not beneficially. Contractor can demand the trust fund be
  placed in a separate retention trust account — _Rayack Construction Ltd v Lampeter Meat
  Ltd_ [1979] 12 BLR 30 [VERIFY]
- **Insolvency risk**: If employer becomes insolvent before releasing retention, contractor
  is an unsecured creditor for the retention amount unless it is in a separate trust
  account — the JCT retention trust provision helps but is not always enforced in practice
- **Retention bonds**: Some employers accept a retention bond (performance bond from a
  surety) in lieu of cash retention — preferred by contractors for cash flow; check bond
  form carefully (on-demand vs. conditional)

**Retention reform landscape (England and Wales):**

- The Construction (Retention Deposit Schemes) Bill has been introduced to Parliament
  [VERIFY current status — was a private member's bill as of early 2026] to require
  retention monies to be held in a government-approved deposit scheme (ring-fenced trust)
- Government's Piling Industry Alliance introduced a no-retention policy for specialist
  subcontractors in the piling sector — a market-led initiative
- HM Government recommended use of Project Bank Accounts (PBAs) on public sector projects
  (Infrastructure Projects Authority guidance [VERIFY current IPA policy]) — PBAs ring-
  fence payment flows including retention, protecting subcontractors on insolvency
- Many public sector employers (Highways England, Network Rail, NHS) now require PBAs on
  contracts above certain values [VERIFY]

**Common RED flags:**

- Retention rate > 5% → YELLOW
- No trust provisions → RED (contractor entirely unsecured; must request separate account)
- Release of second moiety conditional on subjective employer satisfaction → RED
- No retention bond/PBA alternative offered on large public contracts → YELLOW
- Cash retention held in employer's general bank account (not separate trust) → RED (breach
  of JCT trust obligations; contractor should enforce immediately)
- Scottish style retention of title clauses (employer claims ownership of contractor's plant
  on site as "security") → RED (generally unenforceable in England for construction
  operations — _Aberdeen City Council v Stewart Milne Group_ [2011] CSOH 80 is a Scottish
  case — [VERIFY] applicability to E&W)

**Confidence**: PROBABLE (0.72) — core retention framework clear; reform landscape and
PBA adoption data change rapidly [VERIFY current legislative status]

---

### 11. Insurance (Works / CAR / Public Liability)

**Standard forms**: JCT SBC/Q 2024 cl.6.1–6.16.

**Insurance Options (JCT):**

- **Option A (cl.6.7)**: Contractor takes out and maintains Works insurance in joint names
  — usual for new build projects where contractor controls the site
- **Option B (cl.6.8)**: Employer takes out and maintains Works insurance — used where
  employer has a portfolio policy or carries existing structures (refurbishment)
- **Option C (cl.6.9)**: Employer takes out and maintains insurance of existing structures
  and Works against "Specified Perils" — refurbishment projects where existing structures
  are at risk
- Confirm which option applies — if Option A/B/C is not selected, no Works insurance
  obligation arises → automatic RED

**Joint names requirement:**

- JCT insurance must be placed in the joint names of employer and contractor (and any
  sub-contractors where required) — prevents insurer from exercising subrogation rights
  against the jointly insured parties
- Failure to take out joint-names insurance may mean employer can claim contribution from
  contractor for loss caused by contractor's negligence — defeating the purpose of the
  insurance regime

**Employer's risks (JCT SBC/Q 2024 cl.6.3):**

- List of employer's risks (perils for which employer is responsible irrespective of
  contractor negligence) — typically: ionising radiation, pressure waves, war, terrorism
  (beyond policy cover), employer's negligence
- Loss caused by employer's risks → employer must make good; not covered by contractor's
  Works insurance premium

**Common RED flags:**

- No Works insurance option selected in Contract Particulars → RED
- Insurance not in joint names → RED
- Employer's risks definition expanded to include contractor-risk events → RED
- Level of Works insurance cover significantly below contract sum → YELLOW
- No requirement for contractor to provide evidence of insurance on request → YELLOW
- Insurance excess significantly higher than risk-appropriate level → YELLOW

**Confidence**: HIGH (0.83) — JCT insurance framework well-established [VERIFY]

---

### 12. Termination

**Standard forms**: JCT SBC/Q 2024 cl.8.1–8.12; NEC4 cl.90–94.

**Key elements:**

- **Contractor defaults** (cl.8.4): wholly suspended works without cause; failure to
  proceed regularly and diligently; substantial breach of CDM obligations; insolvency
  — employer may give 14-day written notice specifying default; if not remedied,
  terminate within 10 days
- **Employer defaults** (cl.8.9): non-payment after adjudicator's decision; substantial
  prevention of contractor; insolvency — contractor may terminate on 14-day written notice
- **At will / force majeure termination** (cl.8.11): either party may terminate after
  2-month suspension due to force majeure
- **Consequences of termination**: differs significantly based on who terminated and cause:
  - Employer terminates for contractor default: contractor leaves, employer may engage others,
    employer not obliged to pay further until final account determined; may deduct additional
    cost of completion
  - Contractor terminates for employer default: contractor entitled to be paid for all
    work done, loss of profit on balance of works, loss and expense
  - Neutral termination: contractor paid for work done; not entitled to profit on balance

**NEC4 termination (cl.90–94):**

- Similar structure but with more detailed reasons (R1–R21) and compensation procedures (P1–P4)
- Terminal dates for termination process strictly observed

**Common RED flags:**

- Employer's right to terminate "at will" for convenience without compensation → RED (must
  include fair compensation for work done and loss of profit on balance)
- Shorter notice periods than JCT standard → YELLOW
- No insolvency termination rights → RED (essential if counterparty becomes insolvent
  — without this, insolvency process controls the outcome)
- Contractor's termination rights limited to non-payment only (excluding other employer
  defaults) → RED
- "Step-in" rights for funder on contractor insolvency overlapping with employer's
  termination rights — no clear priority mechanism → YELLOW

**Confidence**: HIGH (0.80) — JCT termination framework settled [VERIFY]

---

## Severity Classification

### STRUCTURAL-RISK — Void or Unenforceable Provision

A provision that is void under statute, unenforceable under English law, or creates an
uninsurable gap that cannot be cured by negotiation alone.

**Examples:**

- Adjudication right excluded or restricted (HGCRA s.108 violation — void)
- PI insurance required but fitness for purpose standard imposed (uninsurable gap)
- LDs that continue to accrue after termination (contrary to Triple Point UKSC)
- Provisions that override DPA 1972 s.6(3) no-exclusion rule
- Contractor's retention trust entitlement excluded

**Action**: Flag immediately. Explain the statutory / legal basis for voidness. Recommend
specialist legal advice before execution. Provide an alternative that achieves the
commercial objective lawfully.

### RED — Escalate to Senior Counsel

Falls outside any acceptable commercial range. Material risk requiring qualified
solicitor review and instruction.

**Examples:**

- Unfitness for purpose imposed without PI cover (uninsured gap)
- No EoT mechanism (time at large risk)
- No collateral warranty where funder requires it (deal-stopper)
- PI insurance period inadequate for BSA 2022 / DPA 1972 extended limitation
- LD rate that is clearly extravagant and likely void as a penalty
- No retention trust provisions

**Action**: Explain the specific risk with legal basis. Provide market-standard alternative
language. Estimate financial exposure. Recommend escalation path.

### YELLOW — Negotiate

Below market standard but within a negotiable range. Requires attention but not
immediate escalation.

**Examples:**

- DLP below 12 months
- Retention rate above 5%
- Concurrent delay exclusion clause (enforceability depends on wording)
- Contractor's obligation to "use reasonable endeavours" to maintain PI
- Pay-less notice periods that are tight but technically HGCRA-compliant
- Sectional LDs where section definitions are imprecise

**Action**: Generate specific redline. Provide fallback position. Estimate business
impact of accepting vs. negotiating.

### COMPLIANT — Acceptable

Clause aligns with or is better than market standard for the contract form. No action
needed — noted for completeness.

---

## Redline Format

For each YELLOW and RED issue:

```
**Clause**: [section reference and clause name]
**Current language**: "[exact quote from the contract]"
**Issue**: [1-sentence description of the problem]
**Market standard**: [what the JCT unamended / NEC4 / market practice says]
**Proposed redline**: "[specific alternative language]"
**Rationale**: [1-2 sentences, suitable for sharing with the other side's lawyers]
**Legal basis**: [Statute / case / principle — mark [VERIFY] if unconfirmed]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative if primary redline is rejected]
```

### Redline Best Practices — UK Construction

1. **Distinguish statutory from commercial**: HGCRA violations are void — frame these as
   points of legal principle, not negotiating preferences. Commercial deviations are
   negotiation matters.
2. **Know your form**: amendments to JCT SBC/Q 2024 are assessed differently from bespoke
   contracts — JCT unamended is generally balanced; departures from it are the issues.
3. **Quantify exposure**: UK construction LDs, loss and expense, and retention amounts
   can be large relative to contract value — estimate exposure before prioritising.
4. **Flag TCC enforcement risk**: if a provision is likely to fail before the TCC (e.g.,
   a void adjudication restriction), flag this as a practical risk, not just a legal one.
5. **Consider project bank accounts**: on public sector contracts, failure to include PBA
   provisions may mean the employer is in breach of government guidance — flag this.

---

## Negotiation Priority Framework

### Tier 1 — Must-Haves (Deal Breakers)

Issues where the party cannot execute the contract without resolution:

- Any STRUCTURAL-RISK items (void provisions)
- FfP + PI insurance mismatch (uninsurable gap)
- No adjudication right / defective adjudication procedure
- No collateral warranty / third-party rights where funder requires it
- No EoT mechanism (time at large risk)
- No PI run-off on HRB / residential D&B project
- PI insurance level clearly insufficient for contract scale

### Tier 2 — Should-Haves (Strong Preferences)

Issues that materially affect risk but have negotiation room:

- Concurrent delay exclusion clause (enforce Cyden Homes-compliant drafting)
- Pay-less notice periods (ensure HGCRA compliance and reasonable timelines)
- Retention trust provisions (separate account obligation)
- LDs rate proportionality (Cavendish Square assessment)
- DLP duration (12-month standard)
- Termination for convenience terms (compensation on employer termination)

### Tier 3 — Nice-to-Haves (Concession Candidates)

Issues that improve the position but can be conceded strategically:

- Retention bond alternative
- Sectional completion refinements (section boundaries)
- Snagging list mechanism in PC certificate
- Retention rate (5% vs 3%)
- Preferred adjudicator nominating body

---

## Quality Assurance Framework

### Citation Quality Gates

Run silently before delivering output. Fail = revise before delivery.

| Gate           | Rule                                                                                        | Fail Action                                         |
| -------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **Source**     | Every legal claim cites a statute (with section), SI (with number), or case (with citation) | Add citation or mark [VERIFY — counsel to confirm]  |
| **Format**     | Citations follow English legal citation format (HGCRA s.108; [2021] UKSC 29)                | Fix format                                          |
| **Currency**   | Construction law changes: check Building Safety Act, HGCRA amendments, current TCC position | Flag [CHECK CURRENCY — legislation.gov.uk / BAILII] |
| **Domain**     | Stay within English law — no Scottish law (separate jurisdiction), no US/AUS concepts       | Remove or flag as [JURISDICTIONAL BLEED]            |
| **Confidence** | State uncertainty explicitly — do not assert equivocal positions as settled law             | Add confidence qualifier                            |

### Self-Interrogation for RED / STRUCTURAL-RISK Items

For any RED or STRUCTURAL-RISK item, apply before delivery:

**Pass 1 — Legal Chain Integrity**: Does the risk follow logically from the cited statute or
case? Would a TCC judge actually apply this principle on these facts? Is there a
counter-argument the other side's lawyers will make?

**Pass 2 — Completeness**: Have relevant HGCRA sections, SI provisions, and TCC authorities
been considered? Is there a BSA 2022 or DPA 1972 dimension not yet addressed?

**Pass 3 — Challenge**: What is the strongest argument that this provision IS acceptable?
Under what commercial circumstances might a reasonable construction solicitor advise
accepting this risk? Is RED classification proportionate, or actually YELLOW with mitigations?

If any pass reveals a weakness, revise before delivery. Mark audit trail:
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                    | Action                                     |
| ------------ | --------- | ------------------------------------------ | ------------------------------------------ |
| **Definite** | 0.95–1.0  | Settled by statute or binding precedent    | State with confidence                      |
| **High**     | 0.80–0.94 | Strong authority, minor questions          | State with brief caveat                    |
| **Probable** | 0.60–0.79 | Good arguments, TCC could differ           | State with reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuinely uncertain, competing authorities | Flag for counsel with both sides           |
| **Unlikely** | 0.0–0.39  | Weak basis or speculative                  | Do not assert; flag [UNCERTAIN]            |

---

## Case Law Reference

The following cases are foundational to UK construction law review under this skill.
Verify all citations against BAILII (bailii.org) or Westlaw UK before relying on them.

| Case                                            | Citation               | Issue                             | Principle                                                                                              |
| ----------------------------------------------- | ---------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Henry Boot Construction v Malmaison Hotel       | [2000] 70 Con LR 32    | Concurrent delay / EoT            | Full EoT for employer-caused event even where concurrent contractor delay [VERIFY]                     |
| North Midland Building v Cyden Homes            | [2018] EWCA Civ 1744   | Concurrent delay exclusion        | Express contractual concurrent delay exclusion enforceable [VERIFY]                                    |
| Walter Lilly & Co v Mackay                      | [2012] EWHC 1773 (TCC) | EoT, L&E, global claims           | Global claims admissible where impossible to particularise; financing charges recoverable L&E [VERIFY] |
| Triple Point Technology v PTT Public Company    | [2021] UKSC 29         | Liquidated damages on termination | LDs accrue to termination only — not beyond [VERIFY]                                                   |
| Cavendish Square v El Makdessi                  | [2015] UKSC 67         | Penalty clause test               | New English law penalty test — legitimate interest + not extravagant/unconscionable [VERIFY]           |
| Mears Ltd v Costplan Services                   | [2019] EWCA Civ 502    | Practical completion              | PC principles — real completion, de minimis rule, architect discretion [VERIFY]                        |
| Westminster CC v Jarvis & Sons                  | [1970] 1 WLR 637 (HL)  | Practical completion              | Historic authority on PC definition [VERIFY]                                                           |
| Macob Civil Engineering v Morrison Construction | [1999] BLR 93          | Adjudication enforcement          | First enforcement case; "pay now, argue later" established [VERIFY]                                    |
| Carillion Construction v Felix (UK)             | [2001] BLR 1           | Adjudication enforcement          | Enforcement even if decision arguably wrong in law [VERIFY]                                            |
| Bresco Electrical Services v Michael J Lonsdale | [2021] UKSC 25         | Adjudication + insolvency         | Insolvent party retains right to adjudicate [VERIFY]                                                   |
| ISG Construction v Seevic College               | [2014] EWHC 4007 (TCC) | Smash and grab                    | Unpaid notified sum immediately enforceable without merits analysis [VERIFY]                           |
| Rayack Construction v Lampeter Meat             | [1979] 12 BLR 30       | Retention trust                   | Contractor's right to demand separate retention trust account [VERIFY]                                 |
| Linden Gardens Trust v Lenesta Sludge           | [1994] 1 AC 85         | Assignment                        | Assignment of benefit of building contract [VERIFY]                                                    |
| Peak Construction v McKinney Foundations        | [1970] 1 BLR 111       | Prevention principle              | Employer prevention → time at large → LDs void [VERIFY]                                                |
| Dodd v Churton                                  | [1897] 1 QB 562        | Prevention principle / LDs        | Foundation of prevention principle in English construction law [VERIFY]                                |

---

## Anti-Patterns

Construction contract review anti-patterns specific to UK JCT/NEC4 law:

1. **Ignoring the HGCRA compliance screen**: Diving into clause analysis without first
   checking HGCRA s.108-112 compliance. A void adjudication clause, a missing payment
   notice regime, or a missing pay-less notice window are structural defects — not minor
   commercial points.

2. **Treating the Scheme as a backstop not a risk**: Saying "the Scheme will apply" as if
   that resolves the problem. The Scheme applies automatically, but its terms may be less
   favourable than the express contractual terms the parties intended. Flag the defect.

3. **Confusing "time at large" with "no delay liability"**: Time at large means the
   contractor must complete in a reasonable time — not that delay becomes unenforceable.
   The employer can still claim general damages. The risk is the difficulty of proof and
   quantification without a clear completion date.

4. **Missing the smash-and-grab risk**: Reviewing payment clauses for fairness without
   assessing the operational risk of failing to serve a valid pay-less notice. The smash-
   and-grab mechanism is a process risk, not just a legal one — the client's contract
   administration procedures must be assessed.

5. **Treating JCT and NEC4 as equivalent**: They are fundamentally different. JCT is
   adversarial and prescriptive; NEC4 is collaborative and relies on early warning and
   prompt notification. NEC4's 8-week notification condition precedent for compensation
   events has no equivalent in JCT. Applying JCT analysis to NEC4 (or vice versa) produces
   wrong conclusions.

6. **Missing the FfP / PI insurance mismatch**: The single most common structural gap in
   D&B contracts. A bespoke contract that imposes fitness for purpose while requiring PI
   insurance creates an uninsured liability. Standard PI covers only reasonable skill and
   care. Any deviation from JCT DB's reasonable skill and care standard must be flagged.

7. **Ignoring BSA 2022 on residential projects**: Treating all construction contracts
   identically regardless of whether the project involves residential buildings or HRBs.
   The BSA 2022 duty-holder regime, gateway process, and extended DPA limitation periods
   (15/30 years) create material additional obligations and long-tail liability.

8. **Accepting "reasonable endeavours" PI maintenance**: The contractor's obligation to
   maintain PI insurance must be absolute, not "best endeavours" or "reasonable
   endeavours". An endeavours obligation does not prevent the contractor from letting the
   policy lapse — leaving collateral warranty beneficiaries unprotected.

9. **Overlooking retention trust enforcement**: Noting that JCT creates a retention trust
   without advising the client to demand a separate trust account immediately. The trust
   obligation is worthless unless the money is ring-fenced — particularly on insolvency.

10. **Reviewing collateral warranties in isolation from PI policies**: A collateral warranty
    that imposes FfP or unlimited liability, while the contractor's PI policy is limited or
    claims-made, creates an enforcement gap. Always cross-check the warranty terms against
    the insurance requirements.

11. **Missing Triple Point on LDs**: Drafting or approving LDs clauses that purport to
    continue accruing after termination. This is now settled by the UKSC: post-termination
    LD accrual is void; employer's remedy is general damages for cost of completion.

12. **Applying Scottish construction law**: Scotland has separate construction legislation
    and case law. Aberdeen City Council v Stewart Milne Group was a Scottish case — not
    directly applicable in England and Wales. Always confirm the governing law.

13. **Relying on global claims without particularisation**: Advising contractors they can
    submit global claims freely. Global claims are risky — they require: (1) all events
    are causative, (2) impossible to disentangle, (3) loss proven in aggregate. They are
    not an alternative to proper record-keeping and contemporaneous notices.

14. **Missing concurrent delay express exclusion clauses**: Many employer-drafted bespoke
    contracts now include North Midland / Cyden Homes-style exclusions that deny EoT
    during concurrent delay. These are valid if clearly worded. They must be flagged and
    the contractor advised of the consequence on programme float strategy.

15. **Overlooking the Certificate of Making Good as retention trigger**: The second moiety
    of retention is released on the Certificate of Making Good (or Defects Certificate in
    NEC4), not automatically at the end of the DLP. If the contract does not define the
    certificate-issuing mechanism or gives the employer discretion over when to issue it,
    the contractor's right to the second moiety becomes uncertain.

16. **Treating NEC4's Accepted Programme as optional**: Contractors who fail to maintain
    and get acceptance of their programme under NEC4 lose significant protection —
    compensation event assessments are based on the Accepted Programme. An unaccepted
    programme = no baseline for time/cost impact assessment.

17. **Ignoring the Early Warning obligation in NEC4**: Failure to give Early Warning of a
    compensation event (cl.15) — while not a condition precedent — weakens the
    contractor's position on the assessment of that event. The PM can reduce the
    compensation event assessment to what it would have been had early warning been given.

---

## Writing Standards

Apply these standards to all output:

**For redline rationales** (shared with other side's lawyers):

- Plain English. No Latin or unexplained jargon.
- Active voice: "This provision excludes the contractor's EoT right during concurrent delay"
  not "The contractor's EoT right is excluded during concurrent delay by this provision."
- One point per sentence.
- Name the risk specifically: "The employer may deduct the full weekly LD rate without
  serving a pay less notice" — not "this may cause payment issues."
- Cite the legal basis in plain terms: "Section 111 of the Housing Grants Act requires a
  pay less notice to be served at least 7 days before the final date for payment."

**For internal analysis**:

- Same plain-language standards
- Include Confidence Score for each material clause
- Identify statutory basis for every RED classification
- Glass Box audit trail appended

**Quality gates before delivery:**

1. Can a non-construction-lawyer project manager understand the executive summary?
2. Can the other side's TCC solicitor understand and respond to each redline?
3. Is every HGCRA violation cited to the specific section?
4. Are any phrases vague, hedging without basis, or ambiguous? If yes, fix.
5. Could any sentence be shorter without losing legal precision? If yes, shorten.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Step 4: search for current HGCRA text (as amended), BSA 2022 text, and key TCC judgments
- Save results to `/tmp/legalcode-uk-construction-authority.md`
- Reference verified authority throughout the clause analysis
- For RED items, search for additional TCC decisions to support or challenge the classification
- Check whether any cited cases have been reversed on appeal (construction law develops rapidly)
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all case citations and statute section references [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Verify HGCRA compliance against the statutory text at legislation.gov.uk before advising
  on void provisions
- Focus on structural analysis, workflow design, and commercial risk assessment where
  legal authority is unverified

---

## Output Format Template

```markdown
## UK Construction Contract Review — JCT / NEC4

**Document**: [contract name, form, edition, reference number]
**Project**: [project name, location, type, value]
**Parties**: [employer name] / [contractor name]
**Representing**: [employer / contractor / funder / subcontractor]
**Governing Law**: England and Wales
**Standard Form**: [JCT SBC/Q 2024 / JCT DB 2024 / NEC4 ECC Option A / bespoke]
**Design Responsibility**: [traditional / design and build / partial]
**Review Date**: [date]

---

## HGCRA Statutory Compliance Screen

| Requirement               | s.   | Contract Provision | Status       |
| ------------------------- | ---- | ------------------ | ------------ |
| Stage payments            | 109  | [clause]           | ✅ / ⚠️ / ❌ |
| Payment notice (5 days)   | 110A | [clause]           | ✅ / ⚠️ / ❌ |
| Pay less notice (7 days)  | 111  | [clause]           | ✅ / ⚠️ / ❌ |
| Adjudication right        | 108  | [clause]           | ✅ / ⚠️ / ❌ |
| Suspension right (7 days) | 112  | [clause]           | ✅ / ⚠️ / ❌ |

**Overall HGCRA Status**: COMPLIANT / PARTIALLY COMPLIANT / NON-COMPLIANT (Scheme applies)

---

## Key Findings

| #   | Issue               | Clause       | Classification     | Priority  |
| --- | ------------------- | ------------ | ------------------ | --------- |
| 1   | [issue description] | [clause ref] | 🔴 RED / 🟡 YELLOW | Must-have |
| 2   | ...                 | ...          | ...                | ...       |

---

## Missing Provisions

[List absent clauses with severity assessment]

---

## Clause-by-Clause Analysis

### [Clause Category] — [COMPLIANT / YELLOW / RED / STRUCTURAL-RISK] | Confidence: [level]

**Contract provision**: [summary of what the contract says]
**JCT / NEC4 standard**: [what the unamended standard form / market standard provides]
**Issue**: [specific deviation or gap]
**Financial exposure**: [estimated range where quantifiable]
**Redline** (if YELLOW or RED):
```

Clause [X.X]: Delete [current language] and replace with: "[proposed language]"
Rationale: [plain English justification for counterparty's lawyers]
Legal basis: [statute or case]
Fallback: [alternative if primary redline rejected]

````

[Repeat for each clause category]

---

## Negotiation Strategy

**Overall Risk Profile**: HIGH / MEDIUM / LOW

**Tier 1 — Must-Haves (Deal Breakers)**:
[Numbered list]

**Tier 2 — Should-Haves (Strong Preferences)**:
[Numbered list]

**Tier 3 — Nice-to-Haves (Concession Candidates)**:
[Numbered list]

**Recommended approach**: [sequencing, tone, strategic trades specific to this project]

---

## BSA 2022 / DPA 1972 Exposure Note

[Applicable only to residential and mixed-use projects — summarise limitation period
exposure and PI tail insurance recommendations]

---

## Next Steps

[Specific actions, with suggested owners: client solicitors, QS, PI broker, funder's lawyers]

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill: "legalcode-uk-jct-nec-contract-review"
  mode: "Jurisdiction-specific UK E&W construction contract review"
  contract: "[contract name and date]"
  standard_form: "[JCT SBC/Q 2024 / NEC4 ECC Option X / bespoke]"
  representing: "[employer / contractor / funder / subcontractor]"
  governing_law: "England and Wales"
  design_responsibility: "[traditional / D&B / partial]"
  project_type: "[residential HRB / residential non-HRB / commercial / infrastructure]"
  clauses_reviewed: 12
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  hgcra_compliance: "COMPLIANT / PARTIALLY COMPLIANT / NON-COMPLIANT"
  structural_risk_items: "[count and brief description]"
  red_items: "[count]"
  yellow_items: "[count]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "HGCRA 1996 ss.108-112 — [VERIFIED / UNVERIFIED]"
    - "BSA 2022 s.135 — [VERIFIED / UNVERIFIED]"
    - "DPA 1972 s.1 — [VERIFIED / UNVERIFIED]"
    - "LA 1980 ss.2/5/8 — [VERIFIED / UNVERIFIED]"
  cases_consulted:
    - "[Case name] [citation] — [VERIFIED / UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  bsa_2022_flag: "[Yes — HRB project / No / Not assessed]"
  limitations:
    - "All case citations require BAILII / Westlaw UK verification before reliance"
    - "BSA 2022 limitation periods require verification against current legislation.gov.uk text"
    - "PI insurance market conditions change — verify with a specialist construction PI broker"
    - "[Any further scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified construction solicitor review before reliance"
````

```

---

## Localization Notes

This skill is specific to England and Wales. For other UK jurisdictions:

- **Scotland**: Separate construction law framework. Construction contracts are governed
  by the Housing Grants, Construction and Regeneration Act 1996 (Scotland) (Construction
  Contracts (Scotland) Regulations 1998), which has similar but not identical provisions.
  Scottish case law applies in TCC Scotland. Use a Scotland-specific skill.
- **Northern Ireland**: The Construction Contracts (Northern Ireland) Order 1997 applies,
  with similar but distinct provisions. Use a Northern Ireland-specific skill.
- **International projects (English law, offshore)**: HGCRA does not apply to contracts
  for operations outside the UK. Adjudication is contractual only (e.g., FIDIC DAAB).

For international projects using English law as governing law but performed outside England:
- HGCRA provisions are non-applicable (s.104(6B))
- Adjudication rights are contractual, not statutory
- This skill's analysis of adjudication clause should be reframed as commercial analysis,
  not statutory compliance

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis from:
- Research pipeline covering JCT SBC/Q 2024, JCT DB 2024, NEC4 ECC Options A–F
- HGCRA 1996 (as amended by LDEDCA 2009), Scheme for Construction Contracts SI 1998/649
- Building Safety Act 2022 (Part 4, s.135), Defective Premises Act 1972 (as amended)
- Limitation Act 1980, Unfair Contract Terms Act 1977, CRTPA 1999
- TCC case law: Henry Boot v Malmaison [2000], North Midland v Cyden Homes [2018] EWCA,
  Walter Lilly v Mackay [2012], Triple Point UKSC [2021], Cavendish Square UKSC [2015],
  Mears v Costplan [2019] EWCA, Macob v Morrison [1999], Carillion v Felix [2001],
  Bresco v Lonsdale [2021] UKSC, ISG v Seevic [2014], Rayack v Lampeter [1979]
- SCL Delay and Disruption Protocol 2nd Edition (2017)
- Infrastructure Projects Authority guidance on Project Bank Accounts
- RIBA and RICS PI insurance guidance frameworks
- JCT 2024 suite structure and practice
- Legalcode quality assurance framework (Citation Quality Gates, Self-Interrogation,
  Confidence Scoring, Glass Box audit trail) — adapted from legalcode-contract-review gold
  standard
Attribution: Legalcode original synthesis. All [VERIFY] markers require independent
verification against BAILII, Westlaw UK, or legislation.gov.uk before reliance.
```
