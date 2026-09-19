---
name: legalcode-construction-contract-review
description: 'Review construction contracts clause-by-clause covering scope of work, payment and retainage,
  change orders and variations, extension of time and delay, liquidated damages, defects liability, insurance,
  indemnification, limitation of liability, dispute resolution, termination, force majeure, design liability,
  subcontracting, health and safety, and bonds. Supports standard forms: JCT (UK), NEC4 (UK/international),
  AIA A201 (US), FIDIC Red Book (international), and AS 4000 (Australia). Applies UK, US, and Australian
  jurisdiction frameworks. Use when reviewing employer-side or contractor-side construction and engineering
  contracts, design-build agreements, EPC contracts, subcontracts, and professional services appointments
  on construction projects. Flags deviations, classifies risk (GREEN/YELLOW/RED), generates redlines,
  and produces a confidence-scored, auditable analysis.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Construction Contract Review

> **Disclaimer**: This skill provides a framework for AI-assisted construction contract
> review. It does not constitute legal advice. All outputs should be reviewed by a qualified
> legal professional licensed in the relevant jurisdiction before use. Construction law is
> jurisdiction-specific and evolves rapidly — statutory and case law references cited from
> memory carry hallucination risk. Verify against authoritative sources before relying on
> any provision described here. Standard form interpretations may differ from the applicable
> contract version in use.

---

## Purpose and Scope

This skill reviews construction and engineering contracts against an organisation's
negotiation playbook or general industry standards. It identifies deviations, classifies
their severity, generates actionable redlines, and produces a confidence-scored, auditable
analysis adapted to the governing standard form.

**Covers:**

- Clause-by-clause analysis of construction contracts using 16 clause categories
- Standard form identification and deviation analysis (JCT, NEC4, AIA A201, FIDIC, AS 4000)
- GREEN / YELLOW / RED classification with automatic RED triggers for construction-specific risks
- Redline generation with fallback positions
- Missing clause detection
- Payment regime compliance (HGCRA 1996 UK; SOPA Australia; Prompt Payment Acts US)
- Dispute resolution pathway analysis (adjudication, DAAB, arbitration, litigation)
- Business impact assessment and negotiation strategy

**Does not:**

- Draft new construction contracts (see drafting-specific skills)
- Provide legal advice or replace qualified construction law counsel
- Apply exclusively to any single jurisdiction — jurisdiction-agnostic with
  [JURISDICTION-SPECIFIC] markers for UK, US, and Australia
- Substitute for specialist review of complex PFI/PPP, offshore, or nuclear construction

---

## Jurisdiction and Governing Law

This skill covers three primary jurisdictions. Identify the governing law from the contract
and apply the corresponding legal framework throughout the analysis.

| Jurisdiction              | Key Statutes                                                                                                                                                                                                     | Standard Forms                                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **UK (England & Wales)**  | HGCRA 1996 (as amended by LDEDCA 2009); Scheme for Construction Contracts SI 1998/649; Limitation Act 1980; Building Safety Act 2022; Late Payment of Commercial Debts (Interest) Act 1998; Arbitration Act 1996 | JCT 2024; NEC4; FIDIC Red Book 2017                                             |
| **US (Federal + States)** | Federal Prompt Payment Act 31 U.S.C. §§ 3901–3907; Miller Act 40 U.S.C. §§ 3131–3134; State retainage statutes; State prompt payment acts; State statutes of repose                                              | AIA A201-2017; AIA A101-2017; ConsensusDocs                                     |
| **Australia**             | BCISPA 1999 (NSW); Building Industry Fairness (Security of Payment) Act 2017 (QLD); BCISPA 2002 (VIC) + state equivalents; WHS Act 2011 (Cth); PPSA 2009 (Cth); Home Building Act 1989 (NSW)                     | AS 4000:2025 (replacing AS 4000-1997); HIA contracts; Master Builders contracts |

[JURISDICTION-SPECIFIC] When localising, also apply:

- **UK**: CDM Regulations 2015; Employer's Liability (Compulsory Insurance) Act 1969; Defective
  Premises Act 1972 (as extended by BSA 2022); RICS professional standards
- **US**: OSHA construction standards (29 C.F.R. Part 1926); applicable state lien laws;
  Davis-Bacon Act for federal projects; Buy America requirements for federally-funded projects
- **Australia**: WHS Regulations (state); Security of payment regime (state-specific acts above);
  PPSA 2009 for contractor's plant and materials; ACCC guidelines for unfair contract terms

---

## Standard Forms Reference

Quick identification guide for the most commonly encountered forms:

| Form                       | Jurisdiction       | Best Suited For                                                    | Key Character                                                        |
| -------------------------- | ------------------ | ------------------------------------------------------------------ | -------------------------------------------------------------------- |
| **JCT SBC 2024**           | UK                 | Traditional build contracts, employer-designed                     | Prescriptive; Architect certifier; hard LD regime                    |
| **JCT D&B 2024**           | UK                 | Design-and-build                                                   | Contractor takes design risk; Employer's Agent replaces Architect    |
| **NEC4 ECC**               | UK / International | Engineering, infrastructure, large civil works                     | Collaborative; early warning; Option A–F pricing                     |
| **AIA A201-2017**          | US                 | Commercial building; alongside AIA A101 Owner-Contractor Agreement | Architect as Initial Decision Maker; retainage-heavy                 |
| **FIDIC Red Book 2017**    | International      | Employer-designed civil and infrastructure                         | DAAB dispute avoidance; strong Engineer role                         |
| **FIDIC Yellow Book 2017** | International      | Design-build, plant                                                | Contractor-designed; Employer's Requirements                         |
| **FIDIC Silver Book 2017** | International      | EPC/turnkey                                                        | Contractor takes most risk; no DAAB by default                       |
| **AS 4000:2025**           | Australia          | Commercial construction (all states)                               | Superintendent certifier; SOPA-compliant; Abrahamson risk allocation |

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the direction or conclusions of the analysis
- Standard form identification affects which clause numbering and regime applies
- Multiple valid approaches exist depending on deal context or risk appetite
- Severity classification of a clause depends on business context not yet provided

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

### Step 1: Accept the Contract

Accept the contract in any of these formats:

- **File**: PDF, DOCX, or other document format
- **URL**: Link to a contract in a CLM or document system
- **Pasted text**: Contract text pasted directly into the conversation

If no contract is provided, prompt the user to supply one.

### Step 2: Identify the Standard Form and Governing Law

Before gathering user context, identify:

1. **Is this a standard form or bespoke?** Check for JCT, NEC4, AIA, FIDIC, AS, or other
   form references on the cover page or in the recitals.
2. **What edition/version?** (e.g., JCT 2024, NEC4, AIA A201-2017, FIDIC 2017, AS 4000:2025)
3. **Are there Z clauses, Special Conditions, or Employer's Amendments** that modify the
   standard form? These are frequently more consequential than the form itself.
4. **What is the governing law?** Find the governing law clause (typically in the dispute
   resolution section or contract data).

**⟁ CLARIFY** — If the standard form is unclear or this appears to be a heavily amended
bespoke contract:

- "I could not identify a recognised standard form. Is this (a) a bespoke contract, (b) a
  modified standard form, or (c) a subcontract? Knowing this affects which baseline I use
  for deviation analysis."
- "The governing law clause is [absent / unclear / unexpected for this deal type]. Which
  jurisdiction's law should I apply? And should I flag the governing law issue as a RED
  deviation?"

### Step 3: Gather Context

**⟁ CLARIFY** — Ask the user these questions before beginning. Present as structured options:

1. **Which side are you on?**
   - Options: Employer/Owner, Contractor/Builder, Subcontractor, Funder/Lender,
     Purchaser (for acquisition due diligence), Other
   - _Why this matters_: The entire analysis inverts depending on side. What is a RED risk
     for a contractor may be standard for an employer.

2. **Contract type and delivery model?**
   - Options: Traditional build (employer-designed), Design-and-build, EPC/Turnkey,
     Management contracting, Construction management, Framework agreement with call-offs,
     Subcontract (flow-down from main contract), Professional services appointment, Other
   - _Why this matters_: Design risk, variation entitlement, and defect liability differ
     fundamentally across delivery models.

3. **Contract value and project type?**
   - Options: Under £/$/A$1M (residential/small), £/$/A$1M–£/$/A$10M (mid-size commercial),
     £/$/A$10M–£/$/A$100M (major commercial), Over £/$/A$100M (major infrastructure/complex)
   - Project type examples: residential, commercial building, industrial, infrastructure,
     fit-out, refurbishment, offshore, nuclear, PFI/PPP
   - _Why this matters_: Proportionality of LD rates, insurance minimums, and bond requirements
     all scale with contract value. High-value/complex projects warrant deeper scrutiny.

4. **Focus areas?** (allow multiple selections)
   - Options: Payment / retainage, Variations and change orders, Time/delay risk,
     Liquidated damages exposure, Defects liability, Dispute resolution,
     Insurance requirements, Termination rights, No specific focus — full review
   - _Why this matters_: Lets the analysis lead with what matters most.

5. **Deadline?**
   - Options: Urgent (today/tomorrow), Standard (this week), Flexible
   - _Why this matters_: Affects whether to perform a full 16-category review or a
     priority-focused review.

If partial context is provided, proceed but state assumptions explicitly.

### Step 4: Load the Playbook

Check for an organisational construction contract playbook in local settings.

The playbook should define:

- Standard positions for each of the 16 clause categories
- Acceptable LD rates (per week, cap, and carve-outs)
- Insurance minimum levels required
- Bond requirements (type, percentage of contract sum)
- Preferred dispute resolution pathway

**If no playbook is configured:**

**⟁ CLARIFY** — Inform the user that no playbook was found, and ask which approach to take:

- **Option A: Set up a playbook now** — Walk through defining standard positions for the
  key construction-specific clauses (LD rate, retainage %, payment notice periods, EOT
  entitlement triggers, defects liability period). Takes time upfront but makes future
  reviews precise.
- **Option B: Proceed with industry standards** — Use JCT/NEC4/AIA/FIDIC/AS 4000 market
  benchmarks as the baseline. Flag deviations from the unamended standard form.
- **Option C: I'll provide positions as we go** — Start the review and I'll ask when
  a specific position is needed for classification.

### Step 5: Gather Jurisdiction-Relevant Legal Authority

Identify the governing law and use **legalcode-mcp** to build a working legal reference.

**Research process:**

1. **Identify the governing law** from the contract.

   **⟁ CLARIFY** — If the governing law clause is:
   - **Absent**: Flag as a RED deviation and ask which jurisdiction to apply for analysis.
   - **Multiple/conflicting**: Ask which governs the main body; note the conflict.
   - **Unexpected** (e.g., a UK project under the laws of a Caribbean jurisdiction): Confirm
     awareness and whether to analyse under stated law or flag as an issue.

2. **Search legalcode-mcp** for applicable authority:
   - Payment regime: HGCRA/SOPA/Prompt Payment Acts
   - LD enforceability: penalty doctrine case law for the jurisdiction
   - EOT and concurrent delay: jurisdiction's treatment
   - Adjudication/dispute resolution: statutory rights and exclusions
   - Insurance and bonding requirements
   - Building safety and latent defect limitation periods

3. **Save results** to `/tmp/legalcode-construction-review.md` structured as:

   ```markdown
   # Legal Authority — [Contract Name]

   ## Governing Law: [Jurisdiction]

   ## Standard Form: [Form and Edition]

   ## Date: [date]

   ### Payment Regime

   - [Applicable statute and key provisions]

   ### Dispute Resolution

   - [Applicable statute; adjudication right; arbitration framework]

   ### LD Enforceability

   - [Penalty doctrine case law; applicable test]

   ### Limitation Periods

   - [Contract / deed; latent defects / building safety extension]
   ```

**If legalcode-mcp is not connected:**

- Mark all statutory and case law references [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed using general construction law knowledge but flag that authority is unverified

### Step 6: Clause-by-Clause Analysis

Read the entire contract before flagging issues — clauses interact heavily
(e.g., a variation clause that excludes concurrent delay from EOT interacts with the LD
clause and the force majeure clause).

**⟁ CLARIFY** — For long or complex contracts (100+ pages, multiple schedules, Z clauses,
or flow-down subcontracts):

- Ask whether to perform a **full review** (all 16 categories) or a **priority review**
  focused on user's stated concerns plus all RED items discovered.
- If the contract incorporates external documents (e.g., employer's requirements, employer's
  information requirements under NEC4, or a BIM protocol), ask whether those should be
  reviewed as well.

Cover all 16 clause categories below (unless priority review agreed). For each, assess
whether the clause is: **present and acceptable** (GREEN), **present but requires
negotiation** (YELLOW), **present but escalation-level risk** (RED), or **absent** (flag
and classify).

| #   | Clause Category             | Depth    | Key Review Points                                                                                 |
| --- | --------------------------- | -------- | ------------------------------------------------------------------------------------------------- |
| 1   | Scope of Work               | Deep     | Definition, drawings/specs, design responsibility, employer's requirements                        |
| 2   | Payment and Retainage       | Deep     | Payment mechanism, notice regime, HGCRA/SOPA compliance, retainage % and release                  |
| 3   | Change Orders / Variations  | Deep     | Instruction mechanism, valuation, constructive changes, no-CO-no-pay risk                         |
| 4   | Extension of Time           | Deep     | EOT triggers, notice conditions precedent, concurrent delay, prevention principle                 |
| 5   | Liquidated Damages          | Deep     | LD rate, enforceability, cap, sectional completion, Triple Point termination issue                |
| 6   | Defects Liability           | Deep     | DLP duration, practical/substantial completion definition, final certificate risk, latent defects |
| 7   | Dispute Resolution          | Deep     | Adjudication right, DAAB/DAB, arbitration/litigation, escalation tiers                            |
| 8   | Insurance                   | Standard | CAR/property all risks, PI, public/third-party liability, EL/WC, adequacy of cover                |
| 9   | Indemnification             | Standard | Scope, mutuality, contractor IP/design indemnity, personal injury, consequential loss             |
| 10  | Limitation of Liability     | Standard | Cap amount, mutual vs. unilateral, consequential loss exclusion, carveouts                        |
| 11  | Termination                 | Standard | For cause, for convenience, repudiation, termination account, insolvency                          |
| 12  | Force Majeure               | Standard | Definition breadth, notice, mitigation, termination rights, pandemic coverage                     |
| 13  | Design Liability            | Standard | Design-build scope, standard of care, fitness for purpose vs. reasonable skill, PI link           |
| 14  | Subcontracting              | Standard | Consent requirements, flow-down obligations, pay-if-paid/pay-when-paid clauses                    |
| 15  | Health, Safety & Compliance | Standard | CDM/OSHA/WHS obligations, principal contractor appointment, regulatory compliance                 |
| 16  | Bonds and Securities        | Standard | Performance bond, advance payment bond, retention bond, parent company guarantee                  |

### Step 7: Missing Clause Detection

After clause-by-clause analysis, check for important absent provisions:

For each of the 16 clause categories:

- Flag if entirely absent
- Classify absence as GREEN (not needed), YELLOW (should be added), or RED (must be added)

**Automatic RED for absent clauses:**

- No payment notice mechanism on a UK project (HGCRA applies regardless — but absence
  creates uncertainty and "smash and grab" risk)
- No EOT clause (prevention principle applies: time goes "at large"; employer loses LD right)
- No LD clause when employer needs certain completion (employer must prove general damages)
- No limitation of liability clause (contractor exposed to uncapped consequential losses)
- No adjudication provision on a qualifying UK contract (Scheme for Construction Contracts
  applies automatically — but may differ from parties' intentions)
- No insurance requirements on a substantial project (uninsured risk exposure)

**⟁ CLARIFY** — When absence severity depends on project-specific context:

- "There is no force majeure clause. Given this is a [multi-year / complex site / materials-
  intensive] project, is this a concern? Under English law, there is no implied force majeure
  — frustration is the only common law relief, which is very narrow."
- "No professional indemnity insurance requirement is specified. Is this a design-build
  contract, or does the contractor have no design liability? If design liability exists, PI
  insurance should be mandated."

### Step 8: Flag Deviations and Classify

Classify each deviation using the **Risk Classification** system below. For each deviation:

- **GREEN**: Note for awareness. No action required.
- **YELLOW**: Generate specific redline language, provide fallback position, estimate
  business impact.
- **RED**: Explain the specific risk (citing legal basis where possible), provide market-
  standard alternative language, estimate exposure, recommend escalation path.

**⟁ CLARIFY** — For borderline classifications, ask:

- YELLOW vs RED borderline: "The LD rate of [X]% per week of contract sum is above the
  market norm of 0.5–1% per week. Should I treat this as YELLOW (negotiate down) or RED
  (penalty risk — may be unenforceable)? This depends on the estimated loss at the time of
  contracting."
- GREEN vs YELLOW: "The retainage rate is 3% (below the JCT standard 5%). Is this
  intentional and acceptable, or should it be noted as a positive deviation?"

### Step 9: Generate Redlines

**⟁ CLARIFY** — Before generating redlines, confirm:

- **Negotiation posture**: New counterparty vs. established relationship? Must-have contractor
  vs. competitive market? This affects tone and firmness of redlines.
- **Volume management**: "I found [N] YELLOW items. Do you want redlines for all of them, or
  should I focus on the top [X] highest-impact items?"

Generate redlines using the **Redline Format** below for all YELLOW and RED deviations.

### Step 10: Business Impact Summary

Provide:

- **Overall risk profile**: High / Medium / Low for this contract
- **Top 3–5 issues**: Most important items with severity and one-line summaries
- **Standard form delta**: Key deviations from the unamended standard form (if applicable)
- **Negotiation strategy**: Which issues to lead with, what to concede, how to sequence
- **Statutory compliance check**: Payment regime compliance, adjudication rights, insurance

**⟁ CLARIFY** — If deal context is unclear:

- "Can you walk away from this contractor/employer, or is this a must-proceed deal? This
  determines whether the strategy should be assertive or accommodating on Tier 2 items."
- "Who has to sign off on final terms — legal only, or also commercial / procurement /
  board?" This frames escalation recommendations.

### Step 11: Quality Verification

Before delivering the analysis:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every RED item, run the 3-pass Self-Interrogation. Revise if any pass reveals a weakness.
3. Assign Confidence Scores to each material clause analysis.
4. Verify completeness: all 16 categories addressed (present or flagged as missing).
5. Generate the Glass Box Audit Trail and append to the output.

---

## Clause Analysis Reference

### 1. Scope of Work (DEEP)

**What to analyse:**

- Whether the scope is defined by employer's drawings, employer's requirements, contractor's
  proposals, specification, or a combination
- Who bears design responsibility — employer, contractor, or split
- Whether "design" includes fitness for purpose (higher standard) or reasonable skill and
  care (professional standard)
- How the scope interfaces with the pricing mechanism (lump sum, bill of quantities, target cost)
- Whether provisional sums or prime cost sums are included and on what basis they are valued
- Whether BIM models or digital data are contractually binding and in what priority order
  they rank against other contract documents

**Common issues:**

- Ambiguous or conflicting scope documents (drawings vs. specification vs. employer's
  requirements) with no order of precedence
- Fitness for purpose obligation imposed on a contractor with no design PI insurance for
  that standard [AUTOMATIC RED on design-build contracts]
- "As per instructions" language that allows scope expansion without compensation
- BIM model included as a contract document with a higher priority than the specification
  (contractor may be bound by employer's unverified model data)

[JURISDICTION-SPECIFIC] UK: Under JCT D&B 2024, the Employer's Requirements take priority
over the Contractor's Proposals unless otherwise specified. Fitness for purpose liability
is excluded from standard PI policies — check alignment. [VERIFY]

[JURISDICTION-SPECIFIC] US: AIA A201 Article 1 sets priority: Agreement > Addenda >
Instructions to Bidders > Supplementary Conditions > General Conditions > Drawings >
Specifications. Any deviation from this order of precedence in the contract is a yellow flag.

[JURISDICTION-SPECIFIC] Australia: AS 4000:2025 Clause 1 — definitions and document
priority. Check whether employer's project requirements are annexed and where they rank.

---

### 2. Payment and Retainage (DEEP)

**What to analyse:**

- Whether the payment mechanism complies with HGCRA 1996 (UK), SOPA (Australia), or
  applicable state prompt payment act (US)
- Payment notice mechanics: who issues the payment notice, timing, and what happens if
  it is not issued
- Pay less notice: deadline, minimum content requirements, and consequences of non-service
- Final date for payment and whether it complies with statutory minimums
- Retainage percentage (industry standard: 3–5%)
- Retainage release mechanism: first half on practical/substantial completion; second half
  on expiry of defects liability period; or alternative trigger
- Whether retainage is held in escrow or trust (required in some jurisdictions / project types)
- Whether any "smash and grab" risk exists (UK) — failure to serve a valid pay less notice
  = contractor can adjudicate for the full applied sum regardless of true value
- Pay-when-paid vs pay-if-paid (for subcontracts and contractor-side review)
- Whether interest on late payment is specified (UK: Late Payment of Commercial Debts
  (Interest) Act 1998 — 8% + Bank of England base rate applies by statute)

**Common issues:**

- **No payment notice mechanism (UK)**: Scheme for Construction Contracts applies, which
  prescribes due dates and timelines — but failure to understand this creates ambiguity
  [RED — statutory compliance risk]
- **Pay-if-paid clause in a subcontract**: Shifts insolvency risk to subcontractor. Void in
  Virginia, California, North Carolina, and other US states. Subject to scrutiny everywhere.
  [RED — depending on jurisdiction and value at risk]
- **High retainage (>5%)**: Exceeds industry norms and many US state caps. Major contractor
  cash flow risk on large projects. [YELLOW — negotiate down or seek retention bond alternative]
- **Retainage release tied to subjective conditions**: "Employer satisfaction" as the release
  trigger is unenforceable and invites disputes. Should be an objective certificate trigger.
  [YELLOW–RED depending on value]
- **No interest for late payment**: Statutory interest applies in UK; should be specified in
  US and Australia contracts for certainty. [YELLOW]

[JURISDICTION-SPECIFIC] UK — HGCRA 1996 (as amended by LDEDCA 2009) mandatory requirements:

- Right to interim/stage payments: Section 109 [VERIFY current threshold]
- Payment notice (payer or specified person): within 5 days of due date, even if sum is nil
- Pay less notice: minimum 7 days before final date for payment (under the Scheme)
- Right to suspend on 7 days' notice for non-payment: Section 112
- "Smash and grab" adjudication: 63% of UK adjudication referrals in 2023–24 were payment
  notice failures — a leading cause of dispute. [VERIFY current statistics]

[JURISDICTION-SPECIFIC] US — Key state retainage caps:

- New York (effective November 2023): 5% cap; contractor may invoice on substantial completion
- California: 5% cap on public works
- Florida: 5% (limited to first 50% of contract value)
- North Carolina: 5% cap; no further retainage after 50% completion if satisfactory
- Tennessee: 5% cap; release within 90 days of completion [VERIFY current state of law]

[JURISDICTION-SPECIFIC] Australia — SOPA regime (state by state):

- Payment claims can be served on reference dates specified in the contract
- Respondent must issue a payment schedule within 10 business days (NSW/similar deadlines)
- Failure to issue schedule = full claimed amount becomes a judgment debt
- Adjudication: fast-track binding decision (10–20 business days)
- Retention trusts: QLD, NSW (projects over A$20M), WA require retention in trust [VERIFY
  current thresholds under 2025 state legislation]

---

### 3. Change Orders / Variations (DEEP)

**What to analyse:**

- How variations are instructed: written instruction required, or can verbal be confirmed later?
- Whether the contractor must proceed with work pending agreement on price and time
- Valuation hierarchy: agreed rates → pro-rated adjustment → fair valuation → daywork
- Whether a daywork schedule is included (essential fallback for unforeseen work)
- Notice requirements for variation claims: are these conditions precedent to recovery?
- Whether there is an agreed mechanism for provisional variation orders pending final valuation
- Constructive change risk: can owner/architect instructions effectively change scope without
  triggering a formal change order? Is there a right to claim as a constructive change?
- Limits on the employer's right to vary: most contracts cap the employer's right to omit
  work and give it to others (omission to deprive the contractor of work is a breach)
- Any limitation on the aggregate value of variations without contractor consent

**Common issues:**

- **"No change order, no pay" clause**: Contractor proceeds at own risk without a written CO.
  Combined with constructive changes, this creates uncompensated risk for contractor-side
  reviews. [RED for contractor side]
- **No written instruction requirement**: Creates valuation disputes. Any oral variations
  should be confirmed in writing immediately. [YELLOW]
- **Broad omission right**: Employer can omit scope and award to another contractor without
  compensation. This is a breach at common law but must be expressly excluded. [RED for
  contractor side if not limited]
- **Time bar on variation claims**: Short notice windows (e.g., 7 days) as conditions
  precedent — contractor loses entitlement on procedural failure. [YELLOW — ensure awareness
  of notice triggers]
- **No daywork schedule**: Leaves valuation of unforeseen/disruptive work without a fallback
  rate structure. [YELLOW]

**NEC4 Compensation Events (Clause 60.1):** 21 listed events entitle the contractor to
changes to prices, completion date, or key dates. Strict timescales: contractor must notify
within 8 weeks of becoming aware (W2 contracts) or lose entitlement. PM must respond within
1 week. Quotations due within 3 weeks. Deviations from these timescales are conditions
precedent — scrutinise Z clauses that modify them.

[JURISDICTION-SPECIFIC] UK (JCT): Only written (or confirmed) instructions are valid
variations. Clause 3.10–3.14 (JCT SBC 2024). Unconfirmed verbal instructions do not adjust
the Contract Sum. Variation valuation: JCT Schedule 7. [VERIFY JCT 2024 clause numbers]

[JURISDICTION-SPECIFIC] US (AIA A201-2017): Three mechanisms: Change Orders (signed by all),
Construction Change Directives (owner-directed, binding pending agreement), Minor Changes
(architect-directed, no adjustment). Article 7. Contractor must continue work pending
resolution of disputes about price/time adjustment. [VERIFY current AIA edition]

[JURISDICTION-SPECIFIC] Australia (AS 4000:2025): Written direction required. No
unauthorised variations. Provisional sum items become variations when instructed.

---

### 4. Extension of Time (DEEP)

**What to analyse:**

- What events entitle the contractor to an EOT (qualifying causes of delay)?
- Are these events exhaustive (list only) or with a residual "any act or omission of the
  employer" catch-all? The catch-all is critical — without it, undiscovered employer-caused
  delays may not qualify.
- Are notice requirements conditions precedent to EOT entitlement? (Strict conditions
  precedent are common and can extinguish claims for procedural failure.)
- Is there a critical path analysis obligation for EOT claims?
- How is concurrent delay treated: is the contractor entitled to EOT during a concurrent
  delay period? (UK default: full EOT, no prolongation costs — _Henry Boot v Malmaison_ [2000])
- Can parties contractually exclude EOT for concurrent delay? (Yes — _North Midland Building
  Ltd v Cyden Homes Ltd_ [2018] EWCA Civ 1744)
- What prolongation costs (if any) accompany an EOT?
- Is there a prevention principle safety net — if the employer causes delay and no valid EOT
  is available, does time go "at large"?

**Common issues:**

- **No EOT clause for employer-caused delay**: Time goes "at large" — employer loses right
  to claim LD entirely. [AUTOMATIC RED for employer-side review]
- **Conditions precedent without practical guidance**: Strict notice conditions (e.g., 7-day
  notice of delay event) with no guidance on when the clock starts — contractor may lose
  entitlement on technical grounds. [RED for contractor side]
- **Concurrent delay expressly excluded from EOT entitlement**: In design-build or NEC-style
  contracts this may be a hidden risk for contractors. [RED for contractor side if included]
- **No provision for employer's representative to grant EOT proactively**: Some contracts
  require contractor to claim; employer cannot give EOT without a claim. If employer causes
  delay without contractor claiming, no mechanism exists to reset the LD exposure. [YELLOW
  for employer side — risk of unenforceable LD]
- **EOT entitlement limited to completion only, not milestones**: Where LD apply to multiple
  milestones/sections, ensure EOT applies to each section separately. [YELLOW]

[JURISDICTION-SPECIFIC] UK: SCL Delay and Disruption Protocol (2nd ed., 2017) provides
recommended methodology for EOT claims. Not legally binding but widely used as an expert
standard. _Henry Boot Construction v Malmaison Hotel_ [2000] 70 Con LR 32 — concurrent delay:
full EOT entitlement but no prolongation cost recovery. [VERIFY currency of SCL Protocol]

[JURISDICTION-SPECIFIC] US: "No damage for delay" clauses are common in US owner-drafted
contracts — contractor limited to EOT only, no financial compensation for employer-caused
delays. Enforceability varies: most states enforce, but exceptions for active interference,
abandonment, fraud, and bad faith. Several states (New York, California) have statutory
limits. [VERIFY current state law]

[JURISDICTION-SPECIFIC] Australia (AS 4000:2025): Superintendent can apportion delay between
qualifying and non-qualifying causes — allowing proportionate EOT (different from UK
all-or-nothing approach). [VERIFY AS 4000:2025 Clause numbering]

---

### 5. Liquidated Damages (DEEP)

**What to analyse:**

- LD rate: expressed as amount per day or per week, as a percentage of contract value, or
  as a fixed sum. Benchmark: 0.5–1% of contract value per week is broadly market-standard
  for most commercial projects; higher rates for revenue-generating assets (hotels, stadiums)
- Whether LD apply to the whole contract, or to defined sections (sectional completion)
  — where multiple sections have different rates, calculate aggregate exposure
- Whether the LD rate constitutes a genuine pre-estimate of the employer's likely loss at
  the time of contracting (test for enforceability)
- Whether there is a cap on aggregate LD (common market position: cap at 10–20% of contract
  value)
- What happens to LD claims upon termination (_Triple Point Technology v PTT Public Company
  Ltd_ [2021] UKSC 29 — LD accrue up to termination, not beyond)
- Whether the employer can claim general damages if LD are inadequate (the so-called "excess
  loss" argument — generally available under English law where LD cap is exceeded)
- "No damage for delay" clauses (US) — contractor limited to time extension only, not money

**Common issues:**

- **Uncapped LD at a high rate**: LD exceeding 20% of contract value aggregate are at
  serious penalty risk in the UK and many jurisdictions. [RED — penalty doctrine risk]
- **No cap on LD aggregate**: Without a cap, contractor exposure is theoretically unlimited
  during extended delays. [YELLOW–RED depending on rate and project profile]
- **LD applied to milestones AND completion without separate caps**: Aggregated exposure
  multiplied across milestones can vastly exceed project value. [RED for contractor side]
- **LD rate based on revenue loss without disclosure at time of contracting**: If the LD
  rate reflects a revenue loss that was not known to the contractor at signing, it may be
  unenforceable as a penalty. [YELLOW — document basis for the rate]
- **No sectional completion provisions where employer needs phased handover**: Employer
  cannot claim LD on individual sections if only a whole-works LD clause exists. [RED for
  employer side if phased delivery is needed]

UK penalty doctrine test: _Cavendish Square Holding BV v Talal El Makdessi_ [2015] UKSC 67
— the "legitimate business interest" test replaced the strict "genuine pre-estimate" test.
A high LD rate may be enforceable if it protects a legitimate interest. Factors: was the
contractor aware of the employer's revenue model at the time of contracting? [VERIFY current
case law developments since 2015]

[JURISDICTION-SPECIFIC] US: LD must be reasonable in light of anticipated/actual harm.
Unenforceable if grossly excessive ("penalty" characterisation). Courts are split on whether
to assess at time of contracting or time of breach. [VERIFY current state of US law]

[JURISDICTION-SPECIFIC] Australia: _Andrews v ANZ Banking Group_ [2012] HCA 30 — penalty
doctrine confirmed to apply to primary payment obligations. LD must be proportionate.
[VERIFY current Australian case law developments since 2012]

---

### 6. Defects Liability (DEEP)

**What to analyse:**

- Duration of the Defects Liability Period (DLP) / Rectification Period / Defects
  Notification Period — industry standard 12 months from practical completion
- How practical completion / substantial completion is defined and who certifies it
- Whether minor defects prevent practical completion or are dealt with by a snagging list
- Employer's rights during the DLP: instruction to remedy; contractor's obligation and
  timeline; right to engage others if contractor fails to return
- Whether the issue of a Final Certificate / Defects Certificate is conclusive evidence
  (JCT risk — 28-day window to challenge; missing the window = rights lost)
- Limitation periods: contract limitation (6 years/12 years for deed under UK Limitation
  Act; state statutes of repose in US; 6 years in Australia) vs. extended periods under
  Building Safety Act 2022 (15 years for new works; 30 years for existing dwellings)
- Whether latent defects are addressed beyond the DLP
- Retention release triggers: half at practical completion; half at expiry of DLP — are
  these clearly defined?

**Common issues:**

- **Final Certificate as conclusive evidence under JCT**: If employer does not issue
  proceedings within 28 days of the Final Certificate, certain rights are lost. [RED for
  employer side — must calendar this deadline]
- **No definition of practical completion**: Leads to disputes about when LD stop running,
  when insurance risk transfers, when the DLP starts. [RED — define clearly]
- **Short DLP (less than 12 months)**: Below industry standard; may not surface latent
  defects. [YELLOW — negotiate to 12 months minimum; note BSA 2022 exposure for UK
  residential]
- **Retention release tied to subjective employer satisfaction**: Creates unacceptable
  uncertainty for the contractor. Should be objective certificate triggers. [YELLOW–RED]
- **No process for snagging list / outstanding works at practical completion**: Without a
  mechanism for recording and clearing snagging items, completion and DLP entitlement
  become disputed. [YELLOW]
- **Latent defect exposure not addressed for high-value or residential projects (UK)**:
  BSA 2022 has extended limitation periods significantly. PI insurance run-off cover and
  contractual latent defect warranties should be considered. [RED for UK residential/
  complex commercial — note BSA 2022 applies]

[JURISDICTION-SPECIFIC] UK — Building Safety Act 2022: Defective Premises Act 1972 limitation
extended to 15 years for works completed after 28 June 2022; 30 years for pre-existing
dwellings (retrospective). This creates latent defect exposure well beyond the DLP and
standard contract limitation. [VERIFY current BSA 2022 provisions and any further amendments]

[JURISDICTION-SPECIFIC] US: Statutes of repose typically 6–10 years from substantial
completion (varies by state — no federal standard). AIA A201 warranty period: 1 year from
substantial completion for contractor's own work, but statutes of repose continue beyond.
[VERIFY applicable state statute of repose]

[JURISDICTION-SPECIFIC] Australia (NSW): Home Building Act 1989 — 6-year major defect
warranty from completion; 2-year minor defect warranty. Commercial construction does not
have a statutory equivalent but limitation periods (6 years, contract) apply.

---

### 7. Dispute Resolution (DEEP)

**What to analyse:**

- Whether the adjudication right (UK qualifying contracts) is properly preserved
- Whether the HGCRA Section 108 requirements are met: right to refer at any time; adjudicator
  appointed and decision in 28 days (+ 14 days with consent)
- For NEC4: which Option W applies (W1 for non-HGCRA; W2 for HGCRA UK contracts) and
  whether senior representative step is included
- For FIDIC: whether the DAAB is constituted, when it must be appointed, and whether it
  has been removed by Z/Special Condition amendments (a red flag)
- For AIA: whether the Initial Decision Maker process is intact; whether mediation precedes
  arbitration or litigation
- Whether the final dispute resolution tier is arbitration or litigation, and if arbitration:
  institution (ICC, LCIA, SIAC), seat, number of arbitrators
- New York Convention: is the seat of arbitration a signatory? Is enforcement likely in the
  relevant jurisdiction?
- Whether dispute resolution is tiered (negotiation → mediation/adjudication → final
  arbitration/litigation) — absence of a quick interim mechanism creates cash flow disputes

**Common issues:**

- **HGCRA adjudication right excluded or undermined (UK)**: Any exclusion of the statutory
  adjudication right in a qualifying UK construction contract is void. The Scheme for
  Construction Contracts applies. [AUTOMATIC RED if attempt to exclude]
- **FIDIC DAAB removed and replaced with direct arbitration**: Removes fast-track project-
  level dispute resolution. DAAB is a condition precedent to FIDIC Golden Principle 5
  arbitration — removal undermines the entire FIDIC dispute framework. [RED for any FIDIC
  contract with DAAB removed]
- **No interim binding mechanism on an international project**: Without adjudication or DAAB,
  payment disputes drag on for years in arbitration. Cash flow risk for contractor is
  significant. [RED for contractor-side international contracts]
- **Arbitration seated in a jurisdiction with poor enforcement of awards**: Non-signatories
  to the New York Convention, or jurisdictions with inconsistent court enforcement, create
  award enforcement risk. [RED for cross-border contracts]
- **Tiered escalation that prevents adjudication**: Any contractual mechanism that purports
  to make adjudication conditional on completing prior steps (other than the statutory right)
  is void under HGCRA. [VERIFY — RED for UK contracts if escalation delays adjudication
  beyond the statutory trigger]
- **No governing law clause or governing law in an unexpected jurisdiction**: See Step 5.
  [YELLOW–RED depending on circumstances]

[JURISDICTION-SPECIFIC] UK — NEC4 Option W2: Senior representatives meet within 4 weeks
of dispute notification; exchange statements (max 10 pages); adjudication then available.
Senior rep step is encouraged but cannot bar the statutory right to adjudicate immediately.
2025 NEC4 Conflict Avoidance Z Clauses provide an optional CAP (Conflict Avoidance Panel)
step. [VERIFY availability in the specific NEC4 version in use]

[JURISDICTION-SPECIFIC] FIDIC 2017 — Four-tier process: Engineer determination (42 days)
→ DAAB reference (84 days for decision) → Notice of Dissatisfaction (28 days) → ICC
Arbitration. The DAAB decision is immediately binding ("pay now, argue later"). Employers
in MENA/sub-Saharan Africa often attempt to remove DAAB — scrutinise amendments. [VERIFY]

[JURISDICTION-SPECIFIC] Australia — SOPA adjudication timelines vary by state (typically
10–20 business days for decision). SOPA adjudication is binding but not final — can be
re-litigated in court or arbitration. AS 4000:2025 default final resolution is litigation
(changed from arbitration in 1997 edition) — parties should specify preferred final tier.

---

### 8. Insurance (STANDARD)

**What to analyse:**

- **Contractors All Risks (CAR) / Property All Risks**: Coverage of works, plant, equipment,
  third-party property damage; sum insured vs. reinstatement cost; joint names policy
  (employer and contractor as named insureds); policy deductibles
- **Professional Indemnity (PI)**: Required where the contractor has design responsibility;
  claims-made basis means continuous annual renewal and run-off cover are critical;
  retroactive date must predate when professional services commenced
- **Public/Third-Party Liability**: Minimum levels specified; additional insured status;
  occurrence basis preferred over claims-made
- **Employer's Liability (UK) / Workers' Compensation (US / Australia)**: Statutory minimum
  requirement; UK minimum £5M per occurrence; US varies by state
- **Delayed Start-Up (DSU)**: For revenue-generating assets (hotels, factories, power plants)
  — covers consequential losses from delayed completion; often overlooked but critical for
  employer revenue protection
- **Adequacy of coverage**: Is the sum insured indexed for inflation? Does the PI limit cover
  BSA 2022 extended liability period?

**Common issues:**

- **PI not required in a design-build contract**: If contractor has design liability (including
  fitness for purpose), PI is mandatory. Absence means uncovered design defect risk.
  [AUTOMATIC RED for design-build if PI not required]
- **PI deductibles not disclosed / excessive**: High deductibles create effectively uninsured
  risk. Employer should know the deductible level. [YELLOW]
- **CAR sum insured based on contract sum not reinstatement cost**: If materials costs rise
  post-contract, the sum insured may be inadequate. [YELLOW — require review at intervals]
- **Contractor's existing CAR policy used without joint names endorsement**: Without joint
  names, employer has no direct right to proceeds. [YELLOW–RED depending on project value]
- **No run-off cover requirement for PI**: Once the contract ends, contractor may not renew
  PI — leaving latent design defect claims uninsured. [RED for design-build contracts where
  BSA 2022 extends exposure to 15 years]

---

### 9. Indemnification (STANDARD)

**What to analyse:**

- Scope: personal injury and death, property damage, third-party claims, IP infringement
  (design claims), data breach (for digitally enabled projects), wilful misconduct
- Whether the indemnity is mutual or unilateral
- Whether indemnification is capped (subject to overall liability cap or uncapped)
- Contractor IP/design indemnity: scope of IP rights indemnified, combination carve-out
  (employer modifications), settlement control rights
- Knock-for-knock provisions (common in offshore/oil and gas): each party bears its own
  losses regardless of fault — review suitability for the project type
- Whether indemnification obligations survive termination and for how long
- Personal injury indemnities: employer's contribution to contractor's liability for employee
  claims; interface with Employer's Liability insurance

**Common issues:**

- **Unilateral broad indemnity for any breach**: Effectively uncaps liability. [RED]
- **No cap on indemnification obligations**: On major projects, uncapped indemnities can
  exceed all insurance and assets. [RED — ensure aligned with liability cap]
- **Contractor IP indemnity without combination carve-out**: Contractor indemnifies employer
  for IP infringement caused by employer's modifications — inequitable and should be carved
  out. [YELLOW]
- **Knock-for-knock imposed on subcontractors without insurance alignment**: Subcontractors
  may not have the insurance capacity to support knock-for-knock. [YELLOW]

---

### 10. Limitation of Liability (STANDARD)

**What to analyse:**

- Cap amount: expressed as contract value, fixed sum, or multiple of fees; industry benchmark
  for construction contracts is typically 100–150% of contract value
- Whether the cap is mutual or asymmetric
- Whether consequential / indirect losses are excluded; what constitutes "consequential"
  under the definition clause (check definitions — contracts often redefine this)
- Carveouts: what liabilities are uncapped (typically: fraud, wilful misconduct, personal
  injury/death, insurance obligations, confidentiality)
- Whether design liability is carved out or separately capped (design claims often attract
  a lower or PI-linked cap)
- Interaction with LD: LD are often expressly stated to be the sole remedy for delay, limiting
  employer's general damages for delayed completion

**Common issues:**

- **No limitation of liability clause**: Contractor exposed to full consequential loss claims
  including loss of revenue, increased construction costs. [AUTOMATIC RED for contractor side]
- **Cap significantly below contract value**: A cap of 50% of fees on a construction contract
  is below industry norm and exposes contractor to disproportionate risk. [YELLOW–RED]
- **Asymmetric carveouts**: Contractor carves out everything meaningful while employer's
  liabilities remain capped. [RED for contractor side]
- **"Consequential loss" defined unusually broadly**: Check definitions — if "consequential"
  includes loss of revenue, the exclusion is commercially significant for the employer.
  [YELLOW — ensure client is aware of scope]

---

### 11. Termination (STANDARD)

**What to analyse:**

- Termination for cause: what constitutes a "default" triggering termination; cure period
  (14–30 days industry norm); whether insolvency is an automatic trigger
- Termination for convenience: available to employer? to contractor? notice period? compensation
  for work done, committed costs, and reasonable profit on incomplete work?
- Effects of termination: obligation to de-mobilise; protection of the works; handover of
  documents and designs; payment account process; LD accrual up to termination (_Triple
  Point_ [2021])
- Insolvency provisions: automatic termination on insolvency events? stepdown / novation
  provisions for funders? interface with TUPE/employment obligations?
- Termination account process: timeline for producing, agreeing, and paying the final
  termination account

**Common issues:**

- **No termination for convenience for employer**: On long-term or complex projects, employer
  needs the ability to exit without having to establish cause. [YELLOW for employer side]
- **Termination for convenience with inadequate compensation**: "Payment for work done only"
  without committed costs and profit on uncompleted work is below market standard.
  [YELLOW for contractor side]
- **Cure period too short**: A 48-hour cure period for complex remediation work is
  unreasonably short and may be challengeable. [YELLOW]
- **No insolvency termination mechanism aligned with funder requirements**: Funders typically
  require a direct agreement allowing step-in rights without triggering termination.
  [YELLOW for funder/employer side on financed projects]

---

### 12. Force Majeure (STANDARD)

**What to analyse:**

- Whether force majeure events are specifically enumerated or broadly defined
- Whether pandemic/epidemic, government actions, supply chain disruption, and price
  escalation are included or excluded (critical post-COVID)
- Notice obligations: typically 7–14 days from onset of event
- Mitigation obligations: party claiming FM must take all reasonable steps to avoid/reduce
  effect
- Duration threshold before termination rights arise (industry norm: 60–180 days)
- Whether relief is time only (EOT) or also financial (cost relief)
- Interaction with EOT clause: many construction contracts treat employer-caused force
  majeure events under the EOT clause rather than force majeure

**Important (UK):** English law has no implied force majeure clause. Without an express
provision, the only common law relief is frustration — a very high bar and rarely available
in construction. [AUTOMATIC RED if no force majeure clause in a UK construction contract]

**Common issues:**

- **No force majeure clause (UK)**: Frustration is the only remedy and rarely available.
  [RED for UK contracts — essential provision]
- **Narrow definition excluding supply chain disruption**: Post-COVID, supply chain issues
  are a material risk. A narrow definition may leave contractors without relief for
  material/equipment unavailability. [YELLOW]
- **No financial relief for FM events**: Time only relief means contractor bears the full
  cost of prolongation caused by FM. [YELLOW for contractor side on cost-reimbursable or
  target cost contracts]
- **Short trigger period for termination**: If a pandemic or major disruption continues, a
  30-day trigger may cause premature termination of a viable project. [YELLOW]

---

### 13. Design Liability (STANDARD)

**What to analyse:**

- Whether the contractor has any design liability (traditional build contracts should not)
- Standard of care: "fitness for purpose" (strict liability — no negligence required) or
  "reasonable skill and care" (professional negligence standard)
- Fitness for purpose obligations in NEC4 Option X15 or JCT D&B — are they limited or
  broad?
- Whether design liability is aligned with PI insurance coverage (standard PI policies
  cover "reasonable skill and care" but NOT "fitness for purpose" — a critical mismatch)
- IP ownership of contractor designs: employer needs a licence to use designs if the
  contractor retains copyright; ensure licence survives termination
- Digital/BIM deliverables: who owns the model? what licence is granted? what happens to
  model data on termination?
- Employer's approval of designs: does approval release contractor from liability?

**Common issues:**

- **Fitness for purpose imposed on contractor without PI cover**: This is arguably the most
  dangerous mismatch in UK construction. Standard PI policies exclude fitness for purpose.
  Contractor faces liability that is uninsured. [AUTOMATIC RED for design-build contracts
  where FfP imposed]
- **Contractor retains IP in designs with no licence to use post-termination**: Employer
  cannot use contractor's designs if the contract is terminated — locks employer into a
  difficult position. [RED for employer side]
- **Design approval deemed to release contractor from liability**: Employer approves designs
  and then cannot claim for design defects. [YELLOW for employer side — should not be a
  full release]

---

### 14. Subcontracting (STANDARD)

**What to analyse:**

- Whether consent is required for subcontracting (and if so, whether unreasonably withheld)
- Whether there is a list of approved/nominated subcontractors
- Flow-down obligations: which main contract obligations are flowed down to subcontractors
  (particularly: LD rates, notice requirements, payment terms, adjudication rights)
- Pay-when-paid provisions: enforceable as a timing clause; contractor must pay within a
  reasonable time regardless of employer payment
- Pay-if-paid provisions: enforceable only if clearly drafted to shift insolvency risk;
  void in several US states; subject to scrutiny everywhere [VERIFY current state law]
- HGCRA right to adjudicate: must flow down to all construction subcontracts
- Domestic vs. nominated subcontractors: employer-nominated subcontractors carry additional
  employer risk (interface risk, design risk, insolvency risk)
- Interface risk between subcontract packages: who is responsible for co-ordination of
  multiple subcontractors?

**Common issues:**

- **Pay-if-paid clause in subcontract**: Shifts insolvency risk to subcontractor. Red-line
  to pay-when-paid with a long-stop payment date (e.g., 60 days after due date regardless
  of employer payment). [RED for subcontractor side in states where enforced; YELLOW–RED
  elsewhere]
- **Flow-down of onerous main contract conditions without disclosure**: Subcontractor exposed
  to LD, no-damage-for-delay, and unusual notice requirements from the main contract it
  has never seen. [YELLOW — subcontractor should request main contract key provisions]
- **Broad consent restrictions on subcontracting without "not unreasonably withheld"**:
  Contractor effectively cannot subcontract — operational risk. [YELLOW for contractor side]

---

### 15. Health, Safety and Compliance (STANDARD)

**What to analyse:**

- CDM Regulations 2015 (UK): Principal Designer and Principal Contractor appointment;
  Health and Safety Plan; Health and Safety File obligations; notifiable project threshold
- OSHA (US): applicable construction safety standards (29 C.F.R. Part 1926); site safety
  plan; designated competent person requirements
- WHS (Australia): WHS Act 2011 (Cth) and state equivalents; principal contractor
  appointment for construction work; safe work method statements (SWMS)
- ESG/Modern Slavery obligations: contractual anti-modern slavery representations and
  supply chain due diligence; UK Modern Slavery Act 2015 Section 54 obligations
- Anti-bribery and anti-corruption: UKBA 2010 (UK); FCPA (US); Criminal Code Act 1995
  (Australia) — particularly relevant for international projects
- Environmental obligations: waste management, protected species, permitted development
  conditions, sustainability certifications (BREEAM, LEED, Green Star)
- Compliance representations: contractor warrants compliance with all applicable laws

**Common issues:**

- **No CDM Principal Contractor designation (UK qualifying projects)**: Missing statutory
  appointment creates regulatory liability. [RED for UK projects meeting notifiable threshold]
- **Health and safety obligations placed entirely on contractor without employer obligations**:
  CDM requires both the employer (Client) and Principal Designer to have duties — cannot be
  entirely contracted out. [YELLOW for UK projects]
- **No modern slavery supply chain clause on large projects**: UK Modern Slavery Act s.54
  statement required for large commercial entities; contractual obligation should flow down
  to supply chain. [YELLOW for large UK commercial projects]

---

### 16. Bonds and Securities (STANDARD)

**What to analyse:**

- **Performance Bond**: Amount (typically 10% of contract sum); on-demand vs. conditional
  (conditional bonds require proof of default; on-demand bonds are callable without proof);
  provider (parent company, bank, surety); duration (through DLP or just to completion)
- **Advance Payment Bond**: Required if any advance payment is made before work commences;
  reduces as advance is recouped through interim payments
- **Retention Bond**: An alternative to cash retainage — contractor provides a bond and
  retainage is not deducted from payments; preferred by contractors for cash flow reasons;
  becoming more common in UK following industry retention reform discussions
- **Parent Company Guarantee**: Required where the contractor is a special purpose vehicle
  or subsidiary without independent financial substance; guarantee should cover all
  obligations under the contract and extend through the DLP

**Common issues:**

- **On-demand performance bond without independent discharge conditions**: Employer can call
  the bond without establishing default — significant risk of abusive calling. [RED for
  contractor side if on-demand without protective conditions]
- **Performance bond expires at practical completion, not end of DLP**: Leaves employer
  unprotected for defects liability period. [YELLOW for employer side]
- **PCG from a parent company with no independent financial substance**: If the parent is a
  shell or itself insolvent, the PCG has no value. [RED if the contractor is a thin-capitalised
  SPV and the PCG parent is not creditworthy]
- **No advance payment bond required when advance payments are made**: Employer's advance
  is at risk on contractor insolvency. [RED if advance payment is material]

---

## Risk Classification

### GREEN — Acceptable

The provision:

- Aligns with the applicable standard form (unamended) or organisational playbook
- Represents a minor variation that is commercially reasonable
- Does not materially increase the reviewing party's risk
- May be noted for awareness but requires no negotiation

**Action**: Note with confidence score. No redline required.

### YELLOW — Negotiate

The provision:

- Falls outside the standard form baseline or organisational playbook
- Is commonly found in the market but not preferred
- Represents moderate risk that is negotiable
- Requires a redline with primary position and fallback

**Action**: Generate full redline. Classify as Tier 2 or Tier 3 in the Prioritization
Framework. Estimate financial impact of accepting vs. negotiating.

### RED — Escalate

The provision:

- Falls materially outside acceptable range or triggers an automatic RED criterion
- Exposes the reviewing party to significant financial, legal, or operational risk
- May be legally unenforceable or contrary to applicable statute
- Requires senior review, business/commercial decision, or external legal counsel input

**Confidence thresholds:**

- RED classification requires confidence ≥ 0.80 that the issue is material
- YELLOW classification requires confidence ≥ 0.60
- Below 0.60: flag as uncertain and recommend professional counsel review

### Automatic RED Triggers (Construction-Specific)

The following automatically classify as RED regardless of playbook:

**Employer-side review:**

- No EOT provision for employer-caused delay (prevention principle: LD unenforceable)
- No sectional completion LD where phased handover is required
- Final Certificate as conclusive evidence without 28-day challenge window clearly understood
- No PI insurance requirement on a design-build contract

**Contractor-side review:**

- Fitness for purpose design obligation with no PI insurance alignment
- Uncapped liability / no limitation of liability clause
- On-demand performance bond callable without any default conditions
- Pay-if-paid clause in a jurisdiction where it is enforceable (shifts insolvency risk entirely)
- Broad IP assignment including pre-existing contractor IP

**All parties:**

- UK qualifying project with HGCRA adjudication right excluded or undermined
- FIDIC contract with DAAB removed and no equivalent fast-track dispute mechanism
- Governing law in a jurisdiction with unreliable contract enforcement

---

## Redline Format

For each redline:

**Clause**: [Section reference and clause name]
**Current language**: "[exact quote from the contract]"
**Proposed redline**: "[specific alternative language — ready to insert]"
**Rationale**: [1-2 sentences suitable for external sharing with counterparty's counsel]
**Legal basis**: [Specific statute, regulation, case, or "General construction market practice"]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative position if primary redline is rejected]

### Redline Best Practices

1. **Be specific**: Provide exact language, not vague guidance. The redline must be ready to insert.
2. **Be balanced**: Firm on critical points but commercially reasonable. Overly aggressive
   redlines on standard construction contracts signal unfamiliarity with the market.
3. **Provide fallback positions**: For YELLOW items, include a fallback if the primary ask
   is rejected.
4. **Reference applicable law**: Where the redline addresses a statutory or case law risk,
   cite the specific authority. If citing from memory, mark [VERIFY].
5. **Consider the delivery model**: A redline appropriate for a lump-sum fixed-price contract
   may be inappropriate for a NEC4 Option E cost-reimbursable contract.
6. **Reference the standard form baseline**: When redlining an amendment to a JCT, NEC4, AIA,
   or FIDIC contract, note that the proposed amendment reinstates the standard form language.
   "Reinstate Clause [X] of JCT SBC 2024 unamended" is a powerful and simple redline.

---

## Prioritization Framework

### Tier 1 — Must-Haves (Deal Breakers)

Issues where the reviewing party cannot proceed without resolution. Concession requires
escalation to leadership or consideration of walking away from the deal.

**Typical Tier 1 items for construction contracts:**

- Prevention principle risk (no EOT for employer-caused delay — employer loses LD right entirely)
- Fitness for purpose / PI insurance mismatch (uninsured design liability)
- Uncapped liability or no limitation of liability clause
- HGCRA adjudication right excluded (UK qualifying contracts)
- FIDIC DAAB removed without equivalent fast-track mechanism
- On-demand performance bond with no protective conditions (contractor side)

**Strategy**: Lead with Tier 1 issues. Do not trade them without escalation.

### Tier 2 — Should-Haves (Strong Preferences)

Issues that materially affect risk or cost but where negotiation room exists. Trade Tier 3
concessions to win Tier 2 items.

**Typical Tier 2 items for construction contracts:**

- LD rate above market benchmark (0.5–1% per week) without a cap
- Retainage above 5% or tied to subjective release conditions
- Strict conditions precedent for EOT/variation claims without practical guidance
- Concurrent delay expressly excluded from EOT entitlement
- Final Certificate as conclusive evidence (JCT) — ensure employer is aware and processes
  are in place to challenge in time
- Pay-if-paid clause in a jurisdiction where enforceable (subcontractor reviews)
- PI insurance with inadequate run-off cover for BSA 2022 exposure (UK)

**Strategy**: Prioritise highest financial-impact items. Offer Tier 3 concessions in exchange.

### Tier 3 — Nice-to-Haves (Concession Candidates)

Issues that improve position but are acceptable to concede strategically.

**Typical Tier 3 items for construction contracts:**

- Reducing retainage from 5% to 3% on a small project
- Adding a daywork schedule where valuation risk is low
- Extending the cure period from 14 to 28 days
- Adding a "not unreasonably withheld" qualification to subcontracting consent

**Strategy**: Concede these readily to secure Tier 1 and 2 wins.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                         | Fail Action                                                           |
| -------------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, case, or established construction law principle      | Add citation or mark "[UNVERIFIED — construction counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognisable format for the jurisdiction                                  | Fix format                                                            |
| **Currency**   | Every cited provision checked for amendments or repeal; standard form references checked for correct edition | Flag "[CHECK CURRENCY — may have been amended]"                       |
| **Domain**     | Analysis stays within the contract's governing law. No assumptions from other jurisdictions                  | Remove or flag jurisdictional bleed                                   |
| **Confidence** | Uncertainty explicitly stated, not hidden                                                                    | Add confidence qualifier                                              |

**Construction-specific gates (run in addition):**

| Gate                            | Rule                                                                                                          | Fail Action                                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Standard Form Version**       | References to standard form clauses are to the correct edition                                                | Flag "[CHECK EDITION — clause numbers differ between JCT 2016 and JCT 2024]"          |
| **Special Conditions Override** | Z clauses, Special Conditions, and Employer's Amendments have been checked against the standard form analysis | Flag "[SPECIAL CONDITIONS OVERRIDE — check employer's amendments]"                    |
| **Statutory Compliance**        | Payment regime analysis (HGCRA/SOPA/Prompt Payment Act) is jurisdiction-correct                               | Flag "[VERIFY PAYMENT REGIME — jurisdiction and applicable act require confirmation]" |

### Self-Interrogation for RED Items

For any clause classified as RED, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the risk assessment follow logically from the cited statute/case/principle?
- Would a court or adjudicator in this jurisdiction actually reach this conclusion on these facts?
- Is there a counter-argument the counterparty's counsel will make?

**Pass 2 — Completeness**:

- Have all relevant statutes and regulations been considered?
- Have the special conditions / Z clauses been checked for modifications to the standard form?
- Are there regulatory dimensions (HGCRA, BSA 2022, SOPA) not yet addressed?

**Pass 3 — Challenge**:

- What is the strongest argument that this clause IS acceptable?
- Under what commercial circumstances might a reasonable construction lawyer accept this risk?
- Is the RED classification proportionate, or is this actually YELLOW with mitigations?

Mark the audit trail: `self_interrogation: "PASS"` or `self_interrogation: "REVISED"`.

### Confidence Scoring

For each material clause analysis, assign a confidence level:

| Level        | Range     | Meaning                                                                                                | Action                                                             |
| ------------ | --------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| **Definite** | 0.95–1.0  | Settled construction law, clear statute, unambiguous standard form provision                           | State with confidence                                              |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions, or minor standard form ambiguity                     | State with brief caveat                                            |
| **Probable** | 0.60–0.79 | Good arguments but reasonable minds could differ; standard form clause is commonly amended in this way | State with explicit reasoning and contra-indicators                |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing authorities; heavily bespoke contract with unclear intent               | Flag for construction counsel review                               |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                                                                                | Do not assert; flag "[UNCERTAIN — construction counsel to advise]" |

---

## Glass Box Audit Trail

Append this YAML block to every analysis output:

```yaml
glass_box:
  contract: "[Contract title and date]"
  contract_type: "[Traditional build / Design-and-build / EPC / Subcontract / etc.]"
  standard_form: "[JCT SBC 2024 / NEC4 ECC / AIA A201-2017 / FIDIC Red Book 2017 / AS 4000:2025 / Bespoke]"
  special_conditions: "[None / Z clauses / Employer's Amendments / Schedule of Amendments — count and nature]"
  user_side: "[Employer / Contractor / Subcontractor / Funder / Other]"
  governing_law: "[Jurisdiction identified from the contract]"
  contract_value: "[£/$/A$ amount or range if disclosed]"
  project_type: "[Residential / Commercial / Infrastructure / Industrial / Other]"
  playbook_used: "[Playbook name or 'Industry standard — [form] unamended baseline']"
  clauses_reviewed: 16
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  automatic_red_triggers_fired: "[list any automatic RED triggers]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-construction-review.md or 'Not created']"
  statutes_consulted:
    - "[Statute 1 — VERIFIED (legalcode-mcp) or [VERIFY]]"
    - "[Statute 2 — ...]"
  case_law_consulted:
    - "[Case 1 — VERIFIED (legalcode-mcp) or [VERIFY]]"
  citations_verified: "[number VERIFIED] / [number [VERIFY]]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "Standard form clause numbering references [edition]; verify against contract in use"
    - "[Any jurisdiction-specific research limitations]"
    - "[Any scope limitations — e.g., incorporated documents not reviewed]"
  reviewer: "AI-assisted — requires qualified construction law review before reliance"
```

---

## Anti-Patterns

What NOT to do when reviewing construction contracts:

1. **Analysing Z clauses last**: Special Conditions, Z clauses, and Employer's Amendments
   are often more consequential than the standard form they modify. Read them first — they
   may effectively rewrite the payment, EOT, LD, or dispute resolution provisions entirely.

2. **Applying standard form defaults without checking amendments**: JCT, NEC4, AIA, and FIDIC
   default positions are the market benchmark — but Employer's Amendments routinely deviate.
   "The standard form says X" is meaningless if a Z clause says Y.

3. **Missing the prevention principle risk**: The most consequential omission in a UK/AU
   construction contract review is failing to check whether there is a valid EOT provision
   for all employer-caused delay events. Without it, LD become unenforceable and the employer
   loses a major contractual protection. A single missing carve-out can trigger this risk.

4. **Treating fitness for purpose and reasonable skill and care as interchangeable**: These
   are fundamentally different design standards. Fitness for purpose is strict liability;
   reasonable skill and care requires proof of negligence. Standard PI policies cover the
   latter, not the former. A design obligation that says "the design shall achieve [result]"
   may be a fitness for purpose obligation even if those words are not used.

5. **Ignoring smash and grab risk (UK)**: Reviewing payment clause adequacy without analysing
   whether the payment notice and pay less notice regime is HGCRA-compliant creates a
   material omission. A valid payment application with no pay less notice = adjudicable
   for the full applied sum, regardless of true value.

6. **Reviewing FIDIC contracts without checking DAAB provisions**: The DAAB is the
   cornerstone of FIDIC 2017 dispute resolution. Employers in certain regions routinely
   remove it. An analysis that misses a deleted DAAB is an incomplete analysis of a FIDIC
   contract's dispute resolution structure.

7. **Calculating LD exposure without checking sectional completion**: Where LD apply to
   multiple milestones and sections, aggregate exposure can dwarf the headline rate. A
   0.5% per week rate applied to three sections simultaneously can equal 1.5% per week
   aggregate exposure.

8. **Ignoring the Final Certificate trap under JCT**: Under JCT Standard Building Contract,
   the Final Certificate can be conclusive evidence on certain matters. The 28-day window
   to challenge is a hard deadline. An employer who does not calendar this date and issue
   proceedings in time may lose the right to pursue defect claims. Always flag this in a
   JCT review.

9. **Not checking NEC4 Option Z clauses for time bar modifications**: NEC4's compensation
   event regime has strict timescales that are conditions precedent. Z clauses frequently
   modify these timescales — making them stricter (shorter notification windows) or relaxing
   them. Missing a Z clause that changes the 8-week compensation event notification period
   is a material review error.

10. **Applying the same LD enforceability analysis across jurisdictions**: The penalty
    doctrine in the UK (_Cavendish Square_ [2015] legitimate interest test), the US
    (reasonable anticipation of harm), and Australia (_Andrews_ [2012] proportionality)
    differ meaningfully. Do not apply the UK test to a US or Australian project.

11. **Treating pay-when-paid and pay-if-paid clauses as equivalent**: Pay-when-paid is a
    timing clause — subcontractor is paid when the main contractor is paid but retains
    the right to be paid within a reasonable time. Pay-if-paid shifts the insolvency risk
    entirely. The distinction is critical for subcontractor-side reviews and jurisdiction-
    dependent for enforceability.

12. **Ignoring Building Safety Act 2022 exposure in UK residential reviews**: The BSA 2022
    has extended limitation periods to 15 years (new works) and 30 years (existing dwellings).
    A DLP of 12 months and a 6-year deed limitation period do not protect against BSA 2022
    claims. This is now a standard consideration for all UK residential and mixed-use projects.

13. **Single-pass reading without tracking clause interactions**: Construction contracts have
    deep interactions between clauses: EOT affects LD; LD interact with force majeure;
    variation valuation interacts with provisional sums; termination interacts with the payment
    account process. Read the whole contract before flagging issues.

14. **Citing construction law from memory without verification**: Construction law evolves
    rapidly — the JCT has released a 2024 suite; NEC4 has 2025 Conflict Avoidance Z clauses;
    AS 4000:2025 replaced the 1997 edition; Triple Point changed LD/termination analysis in
    2021; Building Safety Act 2022 extended limitation periods. Mark all time-sensitive
    references [VERIFY] and advise the user to confirm currency.

15. **Missing knock-for-knock liability allocation in offshore or O&G construction**:
    Knock-for-knock regimes (each party bears its own losses regardless of fault) are
    standard in offshore/oil and gas construction contracts. Applying standard commercial
    construction liability analysis to an offshore contract mischaracterises the risk
    allocation. Identify the project type and apply the appropriate baseline.

16. **Omitting bonds and securities from the review**: Performance bonds, advance payment
    bonds, and PCGs are frequently negotiated and frequently inadequate. An on-demand
    performance bond callable without establishing default, a PCG from a shell company, or
    a performance bond that expires at practical completion rather than end of the DLP are
    common issues that are easy to miss if bonds are not systematically reviewed.

17. **Skipping SOPA compliance check on Australian projects**: Each Australian state/territory
    has its own Security of Payment Act with different reference dates, schedule timelines,
    and adjudication processes. Failing to identify the applicable state act and check
    contract compliance is a fundamental gap in Australian construction contract review.

---

## Writing Standards

Before delivering any output:

1. **Verify internal consistency**: Every clause cross-reference in the analysis should match
   the actual clause numbering in the contract under review (not the standard form default).

2. **Use active voice and imperative form**: "The employer should add a pay less notice
   mechanism" rather than "A pay less notice mechanism would need to be considered."

3. **Match terminology to the contract**: Use the contract's defined terms. If the contract
   says "Completion Date" rather than "Practical Completion," use "Completion Date" throughout
   the analysis.

4. **Calibrate tone to the counterparty**: For a negotiation with a sophisticated contractor
   on a market-standard NEC4 contract, the tone should be collaborative and acknowledge
   standard positions. For a heavily owner-drafted bespoke contract with one-sided amendments,
   the tone should reflect the extent of the deviation.

5. **Distinguish the standard form from the amendments**: "The JCT standard position is X;
   the contract as amended says Y" is more useful than stating Y without context.

6. **Mark all unverified legal authority**: Any statutory or case law reference not verified
   via legalcode-mcp must be marked [VERIFY]. Legal authority cited from memory in a
   construction law context carries specific risk — statutes are amended frequently (e.g.,
   HGCRA amended 2009, BSA 2022, AS 4000:2025).

7. **Quantify wherever possible**: "The LD rate of 1.5% per week applied to all four
   sections represents a maximum aggregate exposure of [£X] if all sections are delayed
   by [Y] weeks" is more useful than "the LD rate may be high."

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 5, search for jurisdiction-specific statutes, regulations, and case law
- Search for the applicable payment regime (HGCRA/SOPA/Prompt Payment Act)
- Search for the applicable penalty/LD doctrine and recent case law
- Search for BSA 2022 or equivalent building safety regime
- Save verified results to `/tmp/legalcode-construction-review.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Proceed using general construction law knowledge and research
- Mark all statutory and case law references [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Advise user to verify statutory and case law currency with construction counsel before
  relying on any legal position taken in the analysis

---

## Localization Notes

### UK (England & Wales)

Key mandatory provisions that cannot be excluded by agreement:

- HGCRA 1996: adjudication right; payment notice requirements — if excluded, the Scheme
  for Construction Contracts applies
- Late Payment of Commercial Debts (Interest) Act 1998: statutory interest applies to
  qualifying debts in commercial contracts unless a contractual rate is agreed
- Building Safety Act 2022: extended limitation periods for defective premises — cannot be
  shortened by contract
- CDM Regulations 2015: statutory duties on Client, Principal Designer, and Principal
  Contractor — cannot be contracted out

### US (Federal and State)

Key jurisdiction-specific points:

- No single federal construction contract law — state law governs most private construction
- Federal projects: Miller Act bonding requirements; Davis-Bacon prevailing wages; prompt
  payment act applies
- State lien laws vary significantly and are not covered by this skill — refer to specialist
  local counsel for lien-related rights
- Pay-if-paid enforceability varies by state: void in Virginia (since January 2023),
  California, North Carolina — check current state law before relying on the clause

### Australia

Key jurisdiction-specific points:

- Security of Payment Acts are state legislation — identify the relevant state act before
  analysing payment provisions
- AS 4000:2025 replaced AS 4000-1997 from 30 June 2025 — confirm which edition applies
  to the contract
- PPSA 2009: relevant to security interests in contractor's plant and materials on site —
  AS 4000:2025 includes PPSA clauses [VERIFY]
- WHS Act 2011 (Cth) and state equivalents: principal contractor obligations for
  construction work — align with HSE equivalent in UK

### Scotland, Northern Ireland, and Wales

HGCRA 1996 applies in Scotland but with separate Scheme for Construction Contracts
(Scotland) Regulations (SI 1998/687). Scottish law generally differs on limitation, penalty
doctrine, and property law — flag for Scottish construction law specialist review.

---

## Output Format Template

````markdown
## Construction Contract Review Summary

**Document**: [contract title and date]
**Parties**: [employer and contractor names and roles]
**Your Side**: [employer / contractor / subcontractor / funder]
**Standard Form**: [JCT SBC 2024 / NEC4 ECC / AIA A201-2017 / FIDIC Red Book 2017 / AS 4000:2025 / Bespoke]
**Special Conditions / Amendments**: [None / Z clauses / Employer's Amendments — brief description]
**Governing Law**: [jurisdiction]
**Contract Value**: [£/$/A$ amount if disclosed]
**Project Type**: [commercial / residential / infrastructure / etc.]
**Review Basis**: [Playbook name / Industry standard — [form] unamended baseline]
**Date of Review**: [date]

---

## AUTOMATIC RED TRIGGERS FIRED

[List any automatic RED triggers identified — or "None"]

---

## Key Findings (Top Issues)

| #   | Clause   | Severity  | Issue              |
| --- | -------- | --------- | ------------------ |
| 1   | [clause] | 🔴 RED    | [one-line summary] |
| 2   | [clause] | 🔴 RED    | [one-line summary] |
| 3   | [clause] | 🟡 YELLOW | [one-line summary] |
| [n] | ...      | ...       | ...                |

---

## Missing Clauses

| Clause Category | Assessment               | Recommended Action |
| --------------- | ------------------------ | ------------------ |
| [clause]        | RED — must be added      | [brief action]     |
| [clause]        | YELLOW — should be added | [brief action]     |

---

## Clause-by-Clause Analysis

### 1. [Clause Category] — [🟢 GREEN / 🟡 YELLOW / 🔴 RED] | Confidence: [level]

**Standard form baseline**: [what the standard form says, if applicable]
**Contract provision**: [summary of what the contract actually says]
**Deviation**: [description of the gap vs. baseline]
**Business impact**: [what this means financially or operationally]
**Legal basis**: [statute / case / principle — or [VERIFY]]

**Redline** (YELLOW and RED only):

**Clause**: [section reference]
**Current language**: "[exact quote]"
**Proposed redline**: "[specific alternative language]"
**Rationale**: [1-2 sentences for external use]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [if primary ask rejected]

[Repeat for each of the 16 clause categories]

---

## Negotiation Strategy

**Tier 1 — Must-Haves (Do not trade):**

- [issue 1]
- [issue 2]

**Tier 2 — Should-Haves (Trade Tier 3 for these):**

- [issue 3]
- [issue 4]

**Tier 3 — Concession Candidates:**

- [issue 5]

**Recommended approach**: [sequencing, tone, key strategic trades]

**Standard form delta summary**: [list of key deviations from unamended standard form]

---

## Statutory Compliance Check

| Requirement                                    | Status                                      | Notes   |
| ---------------------------------------------- | ------------------------------------------- | ------- |
| Payment regime (HGCRA/SOPA/Prompt Payment Act) | ✅ Compliant / ⚠️ Issues / ❌ Non-compliant | [notes] |
| Adjudication right (UK qualifying contracts)   | ✅ / ⚠️ / ❌                                | [notes] |
| CDM/OSHA/WHS                                   | ✅ / ⚠️ / ❌                                | [notes] |
| Insurance requirements                         | ✅ / ⚠️ / ❌                                | [notes] |
| PI/FfP alignment                               | ✅ / ⚠️ / ❌                                | [notes] |

---

## Next Steps

[Specific actions with owners and deadlines]

---

## Glass Box Audit Trail

```yaml
[Insert Glass Box YAML block per template above]
```
````

```

---

## Provenance

Created by Legalcode (2026-03-20). Legalcode original synthesis. Research pipeline:
- 2-agent research pipeline: Structural Analyst (reference skill patterns from
  `legalcode-contract-review` and `legalcode-commercial-lease-review`) + Legal Research
  Agent (web-backed research on JCT 2024, NEC4 ECC, AIA A201-2017, FIDIC Red Book 2017,
  AS 4000:2025, HGCRA 1996, Security of Payment Acts (AU), US prompt payment and retainage
  statutes, SCL Delay and Disruption Protocol, *Triple Point* [2021] UKSC 29, *Cavendish
  Square* [2015] UKSC 67, *Henry Boot v Malmaison* [2000], *North Midland v Cyden Homes*
  [2018] EWCA Civ 1744, Building Safety Act 2022)
- 16-clause construction contract architecture
- 4-jurisdiction coverage (UK, US, Australia, International/FIDIC)
- 5 standard forms (JCT, NEC4, AIA A201, FIDIC Red Book, AS 4000)
- Automatic RED trigger system for construction-specific risk events
- 17 construction-specific anti-patterns
- Glass Box audit trail with construction-specific fields
- HGCRA/SOPA/Prompt Payment Act statutory compliance check in output template

**Key legal research sources consulted** (all [VERIFY] for currency):
- Muckle LLP: JCT 2024 key changes; BCLP: JCT 2024 suite analysis
- Pinsent Masons: Triple Point Technology; BSA 2022 limitation periods
- NEC Contracts: NEC4 ECC compensation events; NEC4 pricing options
- AIA Contract Documents: AIA A201-2017 summary
- Gowling WLG: FIDIC 2017 DAAB dispute resolution; concurrent delay analysis
- Standards Australia / Gilbert + Tobin: AS 4000:2025 update and key changes
- DLA Piper: Security of payment Australia 2025
- King's College London: UK construction adjudication report 2024 (63% smash and grab stat)
- SCL: Delay and Disruption Protocol 2nd Edition
```
