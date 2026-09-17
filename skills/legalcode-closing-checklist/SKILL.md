---
name: legalcode-closing-checklist
description: Generate comprehensive transaction closing checklists covering pre-closing deliverables,
  conditions precedent tracking, signature page logistics, funds flow and escrow mechanics, post-closing
  obligations, regulatory filings calendars, and closing binder indexes. Use when managing or preparing
  for M&A closings (stock purchases, asset purchases, mergers), secured financing closings (credit facilities,
  bonds, mezzanine), or commercial real estate closings. Triggers on "closing checklist", "pre-closing
  conditions", "conditions precedent tracking", "closing deliverables", "post-closing obligations", "regulatory
  filings after closing", "closing binder", "funds flow memo", "bring-down certificate", "officer certificate",
  "good standing certificate", "UCC filing", "transaction closing", "sign and close", or "deferred closing".
  Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers for US, UK, EU, and international variants.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Closing Checklist

> **Disclaimer**: This skill provides a framework for AI-assisted transaction closing management.
> It does not constitute legal advice. All outputs should be reviewed by qualified legal counsel
> licensed in the relevant jurisdiction(s) before use. Laws change; verify current applicability
> before relying on any provision described here. Statutory and case law references cited from
> memory carry hallucination risk — verify against authoritative sources before relying on them.
> Closing checklist management requires professional judgment to assess materiality, timing, and
> deal impact. No AI tool replaces experienced transactional counsel at the closing table.

---

## Purpose and Scope

This skill generates and manages comprehensive closing checklists for corporate and real estate
transactions. It tracks pre-closing conditions, organizes deliverables, models funds flow,
schedules post-closing obligations, and produces a closing binder index — all in a single,
auditable workflow.

**Covers:**

- Transaction-type-specific master closing checklists (M&A stock, M&A asset, M&A merger, secured
  financing, commercial real estate)
- Pre-closing conditions precedent tracking across all categories (representations bring-down,
  regulatory approvals, third-party consents, officer certificates, good standing)
- Signature page logistics and execution mechanics (wet, electronic, escrow release)
- Funds flow memoranda and wire instruction frameworks
- Escrow arrangement structuring and release condition analysis
- Post-closing obligation tracking with deadline calendars
- Regulatory filing calendars (state corporate filings, SEC filings, UCC/PPSA, real estate
  recording, antitrust)
- Closing binder index generation with document categorization
- OPEN/IN PROGRESS/SATISFIED/WAIVED/FAILED condition status tracking
- Responsibility matrix (party, counsel, deadline, evidence of satisfaction)
- Quality-verified output with Glass Box audit trail

**Does not:**

- Draft the underlying transaction documents (see `legalcode-purchase-agreement-review`,
  `legalcode-ma-due-diligence-checklist`, `legalcode-venture-financing-suite`)
- Conduct legal due diligence on the target or transaction
- Provide legal advice or replace qualified transactional counsel
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers

**Related skills:**

- `legalcode-purchase-agreement-review` — clause-level SPA/APA review
- `legalcode-ma-due-diligence-checklist` — pre-signing legal due diligence
- `legalcode-due-diligence-report` — executive-ready findings report
- `legalcode-letter-of-intent-review` — LOI binding/non-binding analysis
- `legalcode-board-resolution-drafter` — board consents and authorizations

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The transaction's governing law determines which filing
requirements, regulatory approvals, and post-closing obligations apply.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

**United States:**

- Hart-Scott-Rodino (HSR) Act filing thresholds and waiting periods [VERIFY current thresholds]
- CFIUS mandatory / voluntary filing for covered transactions (FIRRMA) [VERIFY]
- UCC Article 9 financing statement filing: debtor name precision requirement; filing in debtor's
  state of organization; 5-year effectiveness; UCC-3 continuation within 6-month window [VERIFY]
- Delaware General Corporation Law §251 (merger) / §271 (asset sale) / §228 (UWC in lieu of meeting)
  certificates of merger filing with Delaware SOS [VERIFY]
- SEC Form 8-K: 4 business days post-closing for material acquisitions; Item 2.01; 71-day window
  for audited financials via 8-K/A [VERIFY]
- Form 4 / Schedule 13D / 13G: post-closing securities ownership reporting [VERIFY]
- State bulk sales laws (some states retain; check jurisdiction) [VERIFY]
- ERISA Form 5500 amendments for benefit plan changes [VERIFY]
- Real property deed recording: county recorder; transfer taxes; title insurance final policy [VERIFY]

**United Kingdom:**

- UK National Security and Investment Act 2021 (NSIA): mandatory notification sectors; 30
  working-day initial review + 45 working-day assessment [VERIFY]
- Companies Act 2006 s.597: Companies House filing of merger documentation [VERIFY]
- TUPE 2006: employee liability information obligations pre-closing [VERIFY]
- Land Registry AP1 form for real property transfer; SDLT return within 14 days [VERIFY]
- UK NSI Act clearance letter required before closing for mandatory filing sectors [VERIFY]

**European Union:**

- EU Merger Regulation 139/2004: standstill obligation; Commission clearance before closing [VERIFY]
- Member-state foreign investment screening (varies by jurisdiction) [VERIFY]
- Works council information and consultation obligations before closing [VERIFY]
- GDPR data controller/processor notification for data-processing assets acquired [VERIFY]

**Canada:**

- Competition Act (ISED/Competition Bureau) pre-merger notification [VERIFY]
- Investment Canada Act: national security review; net benefit review for large transactions [VERIFY]
- PPSA provincial filings for secured transactions (varies by province) [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
transaction details, the workflow pauses and asks when:

- The transaction type is ambiguous (stock vs. asset purchase vs. merger)
- Multiple parties' counsel are involved and responsibility is unclear
- Regulatory filing requirements are jurisdiction-specific and not yet confirmed
- The sign-and-close vs. deferred closing structure has not been established
- Post-closing obligations have hard deadlines that differ by jurisdiction

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

### Step 1: Accept Transaction Input

Accept transaction details in any of these formats:

- **Transaction description**: Free-text description of the deal (parties, type, structure)
- **Draft purchase agreement**: Extract transaction type, conditions precedent, and closing
  mechanics from the agreement text
- **Existing checklist draft**: Supplement or restructure an existing closing checklist
- **Verbal briefing**: Gather details through structured clarification (Step 2 below)

If no transaction details are provided, proceed immediately to Step 2.

---

### Step 2: Gather Transaction Context

**⟁ CLARIFY** — Before generating the checklist, ask for the following if not already provided.
Present as structured options:

1. **Transaction type** — What kind of transaction is this?
   - Options: M&A — Stock Purchase, M&A — Asset Purchase, M&A — Statutory Merger,
     M&A — Combination (multiple structures), Secured Financing (credit facility/bond),
     Real Estate — Commercial, Real Estate — Residential, Other
   - _Why this matters_: Each transaction type requires fundamentally different closing
     deliverables, regulatory filings, and post-closing obligations.

2. **Closing structure** — How is this transaction structured in time?
   - Options: Simultaneous sign-and-close (signing and closing occur at the same time),
     Deferred closing (signed, now tracking to a future closing date), Pre-signed, preparing
     to close now
   - _Why this matters_: A deferred closing needs ongoing condition precedent tracking and
     a countdown timeline; a simultaneous sign-and-close needs everything ready on day one.

3. **Party perspective** — Whose side is this checklist for?
   - Options: Buyer / Acquirer / Lender, Seller / Target / Borrower, All parties (neutral
     master checklist), Outside counsel coordinator
   - _Why this matters_: Responsibility assignments in the checklist depend on which party's
     obligations need tracking.

4. **Target closing date** — When is closing scheduled?
   - Free text. If not yet set, note that deadline-sensitive post-closing obligations cannot
     be populated until a closing date is confirmed.
   - _Why this matters_: All regulatory filing deadlines (SEC Form 8-K 4-day requirement,
     UCC filings, deed recording, state merger filings) are measured from the closing date.

5. **Jurisdiction(s)** — What jurisdiction(s) govern the transaction?
   - Options: United States (specify state(s)), United Kingdom, European Union / EU member
     state (specify), Canada, Cross-border (specify), Other
   - _Why this matters_: Determines which regulatory filings, consent requirements, and
     post-closing obligations are triggered.

6. **Regulatory complexity** — Are any of the following applicable?
   - Allow multiple selections: Antitrust / competition clearance required, Foreign investment
     screening (CFIUS / NSIA / EU FDI), Industry-specific regulator approval (banking,
     insurance, telecommunications, healthcare), SEC reporting company (public target or
     acquirer), None / standard transaction
   - _Why this matters_: Regulatory closings can require months of lead time and have standstill
     obligations that constrain the checklist timeline.

7. **Real property involved?** — Does the transaction include real property transfers?
   - Options: Yes — commercial, Yes — residential, Yes — as collateral only, No
   - _Why this matters_: Real property triggers deed recording, title insurance, transfer
     taxes, and survey requirements that do not apply to share-only transactions.

8. **Secured financing component?** — Is there a financing closing concurrent with the
   transaction closing?
   - Options: Yes — new credit facility, Yes — assumption of existing debt, Yes — bond
     issuance, No financing component
   - _Why this matters_: Financing closings require separate security agreement execution,
     UCC/PPSA filings, lender condition satisfaction, and funds flow coordination.

If the user provides partial context, proceed with stated assumptions and note them explicitly.

---

### Step 3: Gather Jurisdiction-Relevant Filing Requirements

Use **legalcode-mcp** (if connected) to identify the current filing requirements for the
applicable jurisdiction(s).

**Research these categories for the relevant jurisdiction(s):**

1. **Antitrust / Competition**: Current filing thresholds, waiting periods, and standstill
   obligations (HSR, EU Merger Regulation, UK CMA, Canadian Competition Act)
2. **Foreign Investment Screening**: Mandatory vs. voluntary filing obligations, sector scope,
   and typical review timeline (CFIUS/FIRRMA, UK NSIA 2021, EU FDI Regulation)
3. **Corporate Filings**: Post-closing state filings for the transaction structure (articles of
   merger, certificate of amendment, change of registered agent)
4. **Securities Filings**: Applicable SEC reporting obligations and deadlines for public entities
5. **UCC / PPSA**: Filing location, debtor name accuracy requirements, effectiveness period,
   and continuation filing timing
6. **Real Property**: Recording requirements, transfer taxes, title insurance final policy,
   survey update requirements
7. **Employment**: TUPE, WARN Act, works council consultation obligations triggered by the
   transaction

Save research results to `/tmp/legalcode-closing-research.md`.

**If legalcode-mcp is not connected:**

- Mark all filing deadline references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed using the jurisdiction-specific guidance in this skill, but flag that all deadlines
  require verification against current law before use

---

### Step 4: Generate the Master Closing Checklist

Generate a master closing checklist using the **Transaction-Type Framework** below as the
structural foundation. Adapt the checklist based on the answers gathered in Steps 2–3.

**⟁ CLARIFY** — If the transaction involves multiple structures simultaneously (e.g., an
M&A closing funded by a concurrent financing with real property as collateral):

- Confirm whether a single integrated checklist is preferred, or separate checklists per
  closing track (M&A track / financing track) with a coordination section
- For simultaneous closings with multiple parties' counsel, confirm whether one party is
  designated as closing coordinator, or whether coordination responsibilities are shared

Populate the checklist with:

- All applicable condition categories from the Transaction-Type Framework
- Responsibility assignments (Buyer's Counsel / Seller's Counsel / Lender's Counsel /
  Third Party / Regulatory Authority / Company / Outside Counsel — specify)
- Target completion date per item (working backward from the closing date)
- Evidence of satisfaction (what document or confirmation constitutes satisfaction)
- Initial status: OPEN

---

### Step 5: Track Pre-Closing Conditions Precedent

For each condition precedent in the checklist, apply the **Condition Precedent Analysis
Framework** below to assess:

1. **Satisfaction standard**: What precise standard must be met? (Unqualified / Material /
   MAE-qualified bring-down; unconditional regulatory approval; written third-party consent)
2. **Responsibility**: Which party has the obligation to satisfy or cause satisfaction?
3. **Lead time**: How far in advance of closing must this condition be initiated?
4. **Escalation trigger**: At what point (e.g., 7 days before closing) does an unsatisfied
   condition escalate to senior counsel?
5. **Waivability**: Can this condition be waived by the benefiting party? Is waiver mutual
   or unilateral?

**⟁ CLARIFY** — For any condition with a binary outcome that would block closing (a BLOCKING
condition assessed as FAILED or unlikely to be satisfied by the target closing date):

- Alert the user immediately with: "Condition [X] is classified BLOCKING and currently FAILED
  or AT RISK. This will prevent closing if not remedied. Shall I escalate this, identify
  workarounds, or adjust the closing timeline?"

---

### Step 6: Signature Page and Execution Management

Generate a signature page tracker covering:

1. **Document inventory**: List every agreement to be executed at closing, the required
   signatories, and the execution format required
2. **Execution mechanics**: Confirm applicable format (wet ink, electronic / DocuSign,
   notarized, witnessed, under seal)
3. **Counterpart execution**: Note whether counterpart execution is permitted; confirm all
   counterparts will be collected before funds are released
4. **Authorization verification**: Confirm that each signatory has proper authorization (board
   resolution, officer certificate, power of attorney)
5. **Escrow protocol**: If signature pages are to be held in escrow pending closing, confirm
   the escrow agent, release instructions, and trigger conditions

**⟁ CLARIFY** — If any signatory is a foreign entity or individual requiring notarization,
apostille, or authentication:

- Ask which jurisdiction governs the formality requirements
- Flag that apostille or legalization requirements may require additional lead time of 1–4 weeks

[JURISDICTION-SPECIFIC] Key execution formality requirements:

- **United States**: Electronic signatures generally valid under ESIGN Act / UETA; wet ink
  required for deeds in some states; notarization required for real property transfers and
  some UCC fixture filings [VERIFY]
- **United Kingdom**: Deeds require two witnesses or a notary; electronic execution of deeds
  requires compliance with Land Registry requirements; Companies Act 2006 s.44 execution
  by companies [VERIFY]
- **EU civil law jurisdictions**: Notarization required for share transfers in many EU jurisdictions
  (GmbH share transfers in Germany require notarial deed; France requires actes authentiques for
  real property) [VERIFY]

---

### Step 7: Funds Flow and Escrow Analysis

Generate a funds flow framework covering:

1. **Closing statement**: Purchase price calculation, prorations, adjustments (working capital,
   net debt, transaction expenses)
2. **Wire instructions**: List each wire transfer required at closing with receiving party,
   bank details, amount, and timing (wire before vs. at closing)
3. **Escrow arrangements**:
   - Amount held in escrow and purpose (indemnification, purchase price adjustment, regulatory
     holdback)
   - Escrow agent identity and escrow agreement terms
   - Release triggers and dispute resolution mechanics
   - KYC / AML documentation requirements for escrow setup
4. **Tax withholding**: Identify any required withholding at closing (FIRPTA, UK SDLT, French
   précompte, state withholding) [JURISDICTION-SPECIFIC]
5. **Payoff mechanics**: Debt payoff letters from existing lenders; confirmation of lien release
   upon payoff
6. **Funds release sequence**: The precise order in which funds are released and documents
   are exchanged at closing (typically: buyer funds escrow → escrow confirms receipt → parties
   execute → documents released → funds wired to seller)

**⟁ CLARIFY** — For complex funds flows involving multiple currencies, cross-border wires,
or currency hedging:

- Confirm whether currency conversion risk is addressed in the purchase agreement
- Flag that international wires may require SWIFT confirmation and 1–2 day settlement

---

### Step 8: Post-Closing Obligations and Regulatory Filing Calendar

Generate a post-closing obligation tracker with deadlines calculated from the closing date.

**⟁ CLARIFY** — If the closing date is not yet confirmed:

- Note that all deadline fields are calculated as "D + [N] days" from closing and will be
  updated once the closing date is confirmed
- Ask whether the user wants the calendar populated with target dates or with offset formulas

Populate the post-closing calendar using the **Post-Closing Obligation Framework** below.
For each obligation:

- Deadline (absolute date or D + N formula)
- Responsible party and counsel
- Required action and filing location
- Evidence of completion
- Status: PENDING / FILED / COMPLETED

---

### Step 9: Generate Closing Binder Index

Generate a closing binder index organizing all transaction documents into a structured,
hyperlinked table of contents. Use the **Closing Binder Structure** below.

**Index format principles:**

- Number documents sequentially within each tab/section
- Include document name, date, parties, and page count
- Indicate execution status (Executed / Initialed / Draft)
- Group related documents together (main agreement + schedules + exhibits in one section)
- Note confidential documents that should be excluded from certain parties' copies

---

### Step 10: Quality Verification

Before delivering the checklist, run the quality checks in the **Quality Assurance Framework**:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every BLOCKING condition classified as FAILED or AT RISK, run the 3-pass
   Self-Interrogation. Revise if any pass reveals a weakness.
3. Assign a Confidence Score to each regulatory filing deadline.
4. Verify completeness: confirm all applicable condition categories have been addressed.
5. Generate the Glass Box Audit Trail and append it to the output.

---

## Transaction-Type Closing Frameworks

### Framework A: M&A — Stock Purchase (Share Purchase)

**Pre-Closing Deliverables Checklist**

| #   | Category                   | Item                                                                                                             | Responsible                 | Evidence of Satisfaction                                        |
| --- | -------------------------- | ---------------------------------------------------------------------------------------------------------------- | --------------------------- | --------------------------------------------------------------- |
| 1   | Corporate Authority        | Board resolutions / UWC of seller authorizing transaction                                                        | Seller's Counsel            | Executed resolution                                             |
| 2   | Corporate Authority        | Board resolutions / UWC of buyer authorizing transaction                                                         | Buyer's Counsel             | Executed resolution                                             |
| 3   | Corporate Authority        | Stockholder / shareholder approval (if required by applicable law or charter)                                    | Seller's Counsel            | Written consent or meeting minutes                              |
| 4   | Corporate Authority        | Good standing certificates for seller, buyer, and target (in state of formation and each state of qualification) | Each party's counsel        | SOS certificates dated within 30 days of closing                |
| 5   | Corporate Authority        | Incumbency certificates for authorized signatories                                                               | Each party's counsel        | Officer certificate                                             |
| 6   | Corporate Authority        | Foreign qualification certificates (each jurisdiction where target operates)                                     | Seller's Counsel            | SOS certificates                                                |
| 7   | Representations Bring-Down | Seller bring-down certificate                                                                                    | Seller                      | Executed bring-down certificate                                 |
| 8   | Representations Bring-Down | Buyer bring-down certificate                                                                                     | Buyer                       | Executed bring-down certificate                                 |
| 9   | Regulatory Approvals       | HSR clearance (if applicable — confirm threshold) [VERIFY]                                                       | Both counsel                | Termination of waiting period letter or expiration confirmation |
| 10  | Regulatory Approvals       | CFIUS clearance / approval (if applicable) [VERIFY]                                                              | Buyer's Counsel             | CFIUS written approval or safe harbor letter                    |
| 11  | Regulatory Approvals       | Other regulatory approvals (banking, insurance, telecom, healthcare — list)                                      | Lead regulatory counsel     | Written approval from each regulator                            |
| 12  | Third-Party Consents       | Material contract consents to change-of-control                                                                  | Seller's Counsel            | Written consent from each counterparty                          |
| 13  | Third-Party Consents       | Lender consents (change-of-control under existing debt)                                                          | Seller's Counsel            | Written consent or payoff letter                                |
| 14  | Third-Party Consents       | Lease consents (landlord approvals for change-of-control)                                                        | Seller's Counsel            | Written landlord consent                                        |
| 15  | Third-Party Consents       | License / IP consents (change-of-control restrictions in key licenses)                                           | Seller's Counsel            | Written licensor consent                                        |
| 16  | Legal Opinions             | Seller's counsel legal opinion                                                                                   | Seller's Counsel            | Executed opinion letter                                         |
| 17  | Legal Opinions             | Buyer's counsel legal opinion                                                                                    | Buyer's Counsel             | Executed opinion letter                                         |
| 18  | No MAE                     | No material adverse effect (MAE/MAC) bring-down                                                                  | Seller                      | Bring-down certificate or officer certificate confirming no MAE |
| 19  | Employment                 | Key employee retention agreements (if required)                                                                  | Buyer / Seller's Counsel    | Executed agreements                                             |
| 20  | Employment                 | Employee non-compete / non-solicit agreements                                                                    | Buyer's Counsel             | Executed agreements                                             |
| 21  | IP                         | IP assignment agreements (if required)                                                                           | Seller's Counsel            | Executed assignments                                            |
| 22  | Financing                  | Financing commitment letters (if financing condition applies)                                                    | Buyer's Counsel             | Confirmed committed financing                                   |
| 23  | Insurance                  | Representations and warranties insurance (RWI/W&I) binder                                                        | Buyer's Counsel             | Insurance binder effective at closing                           |
| 24  | Transaction Documents      | Stock purchase agreement — final execution version                                                               | Both counsel                | Fully executed SPA                                              |
| 25  | Transaction Documents      | Disclosure schedules — final, signed                                                                             | Seller                      | Signed disclosure schedules                                     |
| 26  | Transaction Documents      | Escrow agreement                                                                                                 | Both counsel / Escrow Agent | Fully executed escrow agreement                                 |
| 27  | Transaction Documents      | Transition services agreement (if applicable)                                                                    | Both counsel                | Fully executed TSA                                              |
| 28  | Transaction Documents      | Stockholder / shareholder documentation (stock certificates, transfer ledger, capitalization table)              | Seller                      | Delivered to buyer or buyer's counsel                           |

**Conditions Precedent Standards**

The bring-down certificate standard must match the purchase agreement language exactly:

| Standard                                             | When to Use                                                              | Failure Threshold                              |
| ---------------------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------- |
| **True and correct in all respects (unqualified)**   | Fundamental representations (authority, title to shares, capitalization) | Any inaccuracy triggers failure                |
| **True and correct in all material respects**        | General representations                                                  | Inaccuracy must be material to trigger failure |
| **True and correct except as would not cause a MAE** | Standard representations with MAE qualifier                              | Only a MAE-level inaccuracy triggers failure   |

**⟁ CLARIFY** — If the purchase agreement uses different bring-down standards for different
representations (as is common), confirm the specific standards for:

- Fundamental representations (capitalization, authority, title to shares)
- General representations
- Whether the MAE qualifier applies to the bring-down of covenants separately from representations

---

### Framework B: M&A — Asset Purchase

Includes all items from Framework A plus:

| #   | Category            | Item                                                                     | Responsible      | Evidence of Satisfaction                                  |
| --- | ------------------- | ------------------------------------------------------------------------ | ---------------- | --------------------------------------------------------- |
| A1  | Asset Transfers     | Bill of sale for tangible personal property                              | Seller's Counsel | Executed bill of sale                                     |
| A2  | Asset Transfers     | Assignment and assumption agreements for each assumed contract           | Both counsel     | Fully executed A&A per contract                           |
| A3  | Asset Transfers     | IP assignment agreement (patents, trademarks, copyrights, trade secrets) | Seller's Counsel | Executed IP assignments (recorded with USPTO / IP office) |
| A4  | Asset Transfers     | Domain name and digital asset transfer                                   | Seller's Counsel | Transfer confirmation from registrar                      |
| A5  | Asset Transfers     | Real property deed (for each parcel)                                     | Seller's Counsel | Executed and notarized deed                               |
| A6  | Consents            | Third-party consents to assignment for each assigned contract            | Seller's Counsel | Written consent from each counterparty                    |
| A7  | Consents            | Government and regulatory license transfer approvals                     | Seller's Counsel | Written approval from each licensing authority            |
| A8  | Consents            | Lease assignment consents (landlord approvals per lease)                 | Seller's Counsel | Written landlord consent per lease                        |
| A9  | Assumed Liabilities | Assumption agreement for assumed liabilities                             | Both counsel     | Executed assumption agreement                             |
| A10 | Excluded Assets     | Excluded asset / excluded liability schedule confirmed as final          | Both counsel     | Executed/confirmed final schedules                        |

**Critical Asset Purchase Distinction**: Unlike a stock purchase, an asset purchase requires
separate assignment and consent for each contract, lease, license, and permit. The closings
are often more complex due to the volume of individual transfer documents. Identify early:

- How many material contracts require assignment consent?
- Which permits and licenses can be transferred vs. require new application?
- Are there contracts that cannot be assigned (non-assignable by statute or terms) that must
  be handled via subcontracting, power of attorney, or post-closing new agreement?

---

### Framework C: M&A — Statutory Merger

Includes applicable items from Frameworks A and B plus:

| #   | Category             | Item                                                                       | Responsible                | Evidence of Satisfaction                                   |
| --- | -------------------- | -------------------------------------------------------------------------- | -------------------------- | ---------------------------------------------------------- |
| M1  | Stockholder Approval | Stockholder / shareholder vote (record date, proxy, vote threshold)        | Seller's Counsel           | Certified vote results; meeting minutes                    |
| M2  | Merger Documents     | Certificate / Articles of Merger — signed, ready to file                   | Both counsel               | Execution versions of merger certificate                   |
| M3  | Merger Documents     | Merger agreement — final, executed version                                 | Both counsel               | Fully executed merger agreement                            |
| M4  | Post-Closing Filing  | File Certificate of Merger with Secretary of State [JURISDICTION-SPECIFIC] | Surviving entity's counsel | Filed certificate; SOS acknowledgment                      |
| M5  | Post-Closing         | Cancel / transfer stock certificates of surviving entity                   | Transfer agent             | Cancelation confirmations; new certificates or DRS entries |
| M6  | Post-Closing         | Update bank accounts, authorized signatories                               | CFO / Treasury             | Bank confirmation letters                                  |
| M7  | Post-Closing         | Update employer identification numbers / VAT registrations                 | Tax counsel                | IRS / HMRC notification                                    |

[JURISDICTION-SPECIFIC] Delaware merger: DGCL §251 (certificate of merger filed with Delaware
SOS); effective time of merger specified in certificate; dissenter's rights under DGCL §262
(if applicable) [VERIFY]

---

### Framework D: Secured Financing Closing

| #   | Category         | Item                                                                              | Responsible                   | Evidence of Satisfaction                                              |
| --- | ---------------- | --------------------------------------------------------------------------------- | ----------------------------- | --------------------------------------------------------------------- |
| F1  | Credit Documents | Credit agreement / note purchase agreement — final execution version              | Lender's / Borrower's Counsel | Fully executed credit agreement                                       |
| F2  | Credit Documents | Security agreement (pledge of collateral assets)                                  | Borrower's Counsel            | Fully executed security agreement                                     |
| F3  | Credit Documents | Promissory note(s)                                                                | Borrower                      | Fully executed note(s)                                                |
| F4  | Credit Documents | Guaranty agreements (each guarantor)                                              | Guarantors' Counsel           | Fully executed guaranties                                             |
| F5  | Credit Documents | Intercreditor agreement (if multiple lenders or debt tranches)                    | Lead counsel                  | Fully executed intercreditor                                          |
| F6  | Collateral       | UCC-1 financing statements — filed at closing [JURISDICTION-SPECIFIC]             | Lender's Counsel              | Filed UCC-1 with filing receipt; confirm proper debtor name           |
| F7  | Collateral       | Lien searches confirming no prior perfected liens on collateral                   | Lender's Counsel              | Clean lien search results (UCC, judgment, tax lien, real property)    |
| F8  | Collateral       | Control agreements (deposit accounts, securities accounts) [VERIFY]               | Lender's Counsel              | Executed control agreements acknowledged by bank                      |
| F9  | Collateral       | Mortgages / deeds of trust (for real property collateral) [JURISDICTION-SPECIFIC] | Lender's Counsel              | Executed, notarized mortgage; title insurance policy                  |
| F10 | Collateral       | Stock pledge / share charge (equity of subsidiaries pledged)                      | Lender's Counsel              | Executed stock pledge; delivered share certificates with stock powers |
| F11 | Conditions       | Borrower bring-down certificate (no default; representations accurate)            | Borrower                      | Executed certificate                                                  |
| F12 | Conditions       | Financial statements (most recent audited / unaudited + compliance certificate)   | Borrower                      | Delivered statements + compliance certificate                         |
| F13 | Conditions       | Officer's certificate confirming authority, incumbency, and good standing         | Borrower                      | Executed officer's certificate                                        |
| F14 | Conditions       | Legal opinions (enforceability, authority, perfection)                            | Borrower's Counsel            | Executed opinion letters                                              |
| F15 | Conditions       | Insurance certificates naming lender as additional insured and loss payee         | Borrower                      | Insurance certificates                                                |
| F16 | Funding          | Funding request / borrowing notice                                                | Borrower                      | Delivered in accordance with credit agreement notice requirements     |
| F17 | Funding          | Funds flow memo — wire instructions for all proceeds                              | Both counsel                  | Agreed and executed funds flow memo                                   |
| F18 | KYC / AML        | Beneficial ownership certification (FinCEN/equivalent) [JURISDICTION-SPECIFIC]    | Borrower                      | Completed certification form                                          |

**UCC Filing Precision Protocol** [JURISDICTION-SPECIFIC — US only]:

1. File UCC-1 in the state of the debtor's formation / organization (not state of operations)
2. Confirm debtor's exact legal name against state-issued formation documents
3. Even minor name discrepancies (abbreviations, commas, Inc. vs. Inc) may render the filing
   seriously misleading and unenforceable [VERIFY — UCC § 9-503]
4. If the debtor is an individual, use legal name as shown on unexpired driver's license or
   passport
5. Post-filing: confirm proper indexing within 48 hours via search-to-reflect check
6. UCC-1 expires in 5 years; UCC-3 continuation must be filed within the 6-month window
   before expiration [VERIFY — UCC § 9-515]

---

### Framework E: Commercial Real Estate Closing

| #   | Category           | Item                                                                              | Responsible                      | Evidence of Satisfaction                                             |
| --- | ------------------ | --------------------------------------------------------------------------------- | -------------------------------- | -------------------------------------------------------------------- |
| R1  | Title              | Title commitment (CLTA / ALTA preliminary report) — current                       | Title Company                    | Title commitment dated within 30 days of closing                     |
| R2  | Title              | Title insurance commitment — final, with all exceptions resolved                  | Title Company                    | Marked-up title commitment / pro forma policy                        |
| R3  | Title              | Existing liens / encumbrances — payoff and release confirmed                      | Seller's Counsel                 | Payoff letters; lien release commitments                             |
| R4  | Survey             | ALTA/NSPS survey (for commercial property)                                        | Seller / Buyer                   | Current survey certified to buyer, buyer's lender, and title company |
| R5  | Environmental      | Phase I ESA (and Phase II if Phase I findings warrant)                            | Buyer's Counsel                  | Phase I/II report; reliance letter from consultant                   |
| R6  | Zoning             | Zoning compliance letter / certificate of occupancy                               | Seller's Counsel                 | Zoning confirmation from municipality                                |
| R7  | Leases             | Estoppel certificates from all tenants (for investment property)                  | Seller's Counsel                 | Executed estoppel certificates from each tenant                      |
| R8  | Leases             | SNDAs (subordination, non-disturbance, and attornment agreements)                 | Lender / Seller's Counsel        | Executed SNDAs from each tenant                                      |
| R9  | Leases             | Rent roll — current, as of closing                                                | Seller                           | Certified rent roll                                                  |
| R10 | Transfer Documents | Deed (statutory warranty / grant deed / quitclaim) — appropriate for jurisdiction | Seller's Counsel                 | Executed and notarized deed                                          |
| R11 | Transfer Documents | Bill of sale for personal property and fixtures                                   | Seller's Counsel                 | Executed bill of sale                                                |
| R12 | Transfer Documents | Assignment of leases and service contracts                                        | Seller's Counsel                 | Executed assignments                                                 |
| R13 | Transfer Documents | FIRPTA certificate or withholding certificate from IRS [JURISDICTION-SPECIFIC]    | Seller / Tax Counsel             | Executed FIRPTA affidavit; IRS withholding certificate [VERIFY]      |
| R14 | Transfer Documents | Transfer tax declarations and affidavits [JURISDICTION-SPECIFIC]                  | Both counsel                     | Executed declarations                                                |
| R15 | Inspection         | Property inspection report (physical condition)                                   | Buyer's Counsel                  | Report; itemized objection resolution                                |
| R16 | Financing          | Mortgage / deed of trust (lender's financing)                                     | Lender's Counsel                 | Executed mortgage; filed simultaneously with deed                    |
| R17 | Settlement         | ALTA settlement statement / HUD-1                                                 | Settlement Agent                 | Agreed ALTA statement                                                |
| R18 | Post-Closing       | Deed recording at county recorder [JURISDICTION-SPECIFIC]                         | Settlement Agent / Title Company | Recorded deed; recording number                                      |
| R19 | Post-Closing       | Transfer tax payment [JURISDICTION-SPECIFIC]                                      | Settlement Agent                 | Payment confirmation                                                 |
| R20 | Post-Closing       | Final title insurance policy                                                      | Title Company                    | Policy issued within 30–60 days of recording                         |

---

## Condition Precedent Analysis Framework

### Condition Status Classification

Track every condition using the following five-status taxonomy:

| Status          | Symbol | Meaning                                           | Required Action                                               |
| --------------- | ------ | ------------------------------------------------- | ------------------------------------------------------------- |
| **OPEN**        | ⬜     | Not yet initiated                                 | Assign responsible party; set deadline                        |
| **IN PROGRESS** | 🔄     | Initiated; awaiting completion or confirmation    | Monitor; escalate if within 7 days of closing and unsatisfied |
| **SATISFIED**   | ✅     | Fully satisfied; evidence received                | Archive evidence; note date satisfied                         |
| **WAIVED**      | 🟡     | Waived by the benefiting party; waiver documented | Confirm waiver is valid; note in checklist                    |
| **FAILED**      | 🔴     | Cannot be satisfied by the closing date           | Escalate immediately; assess deal consequences                |

### Criticality Classification

In addition to status, classify each condition by its impact if unsatisfied:

| Classification     | Definition                                                                     | Consequence of Failure                                        |
| ------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| **BLOCKING**       | Closing cannot proceed if this condition is unsatisfied or unwaived            | Deal stalls or falls; immediate escalation required           |
| **MATERIAL**       | Condition affects post-closing obligations or creates liability if unsatisfied | Post-closing cure obligation; potential indemnification claim |
| **ADMINISTRATIVE** | Housekeeping item; failure does not affect transaction validity                | Cure in ordinary course post-closing                          |

---

## Post-Closing Obligation Framework

### Regulatory Filing Calendar

Populate with actual deadlines once the closing date is confirmed. All deadlines are measured
in calendar days from closing unless otherwise noted.

| Obligation                                                   | Applicable Transactions                                      | Deadline                                                                                                          | Responsible Party                | Filing Location                                     | Status |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------- | ------ |
| **Certificate / Articles of Merger**                         | Statutory mergers                                            | Within 30 days (varies by state) [VERIFY]                                                                         | Surviving entity's counsel       | Secretary of State                                  |        |
| **SEC Form 8-K** (Item 2.01)                                 | Public company acquirer or target                            | **4 business days** from closing [VERIFY]                                                                         | SEC counsel / IR                 | EDGAR                                               |        |
| **SEC Form 8-K/A** (audited financials)                      | Material acquisitions requiring financial statements         | Within **71 calendar days** of initial 8-K [VERIFY]                                                               | SEC counsel                      | EDGAR                                               |        |
| **Form 4** (Section 16 officers/directors)                   | Public company transactions affecting 10%+ holders           | **2 business days** from transaction [VERIFY]                                                                     | Compliance counsel               | SEC EDGAR                                           |        |
| **Schedule 13D**                                             | Acquirer crosses 5% beneficial ownership with control intent | Within **10 calendar days** of crossing threshold [VERIFY]                                                        | Buyer's Counsel                  | SEC EDGAR                                           |        |
| **Schedule 13G**                                             | Passive investor crossing 5% beneficial ownership            | Within **20 calendar days** of calendar year-end, or 45 days from end of year in which threshold crossed [VERIFY] | Buyer's Counsel                  | SEC EDGAR                                           |        |
| **UCC-1 Financing Statement**                                | Secured financing                                            | At or immediately after closing                                                                                   | Lender's Counsel                 | Secretary of State (debtor's state of organization) |        |
| **UCC-3 Amendment** (name change, collateral change)         | Post-closing mergers, name changes                           | Immediately upon triggering event                                                                                 | Lender's Counsel                 | Secretary of State                                  |        |
| **Deed Recording**                                           | Real estate transactions                                     | At closing or within 24–48 hours                                                                                  | Title Company / Settlement Agent | County Recorder / Register of Deeds                 |        |
| **Mortgage / Deed of Trust Recording**                       | Real estate financing                                        | Simultaneously with deed                                                                                          | Lender's Counsel / Title Company | County Recorder                                     |        |
| **State Corporate Filings** (name changes, registered agent) | Mergers, restructurings                                      | Within 30–60 days [VERIFY per state]                                                                              | Corporate counsel                | Secretary of State                                  |        |
| **Business license updates**                                 | Changes to operating entity                                  | Within 30–90 days [VERIFY per jurisdiction]                                                                       | Corporate counsel                | State / local licensing authority                   |        |
| **ERISA Form 5500 amendment**                                | Benefit plan changes affecting employee benefits             | By filing deadline for plan year [VERIFY]                                                                         | ERISA counsel                    | DOL / IRS                                           |        |
| **TUPE employee liability information**                      | UK business transfers                                        | Before transfer (pre-closing) [VERIFY]                                                                            | UK counsel                       | Delivered to transferee                             |        |
| **SDLT return**                                              | UK real property                                             | Within **14 days** of effective completion date [VERIFY]                                                          | UK conveyancing solicitors       | HMRC                                                |        |
| **Companies House filing**                                   | UK mergers and restructurings                                | Within specified period [VERIFY]                                                                                  | UK company secretary             | Companies House                                     |        |
| **Antitrust / merger control filing**                        | If condition not pre-satisfied                               | Pre-closing (standstill obligation applies)                                                                       | Antitrust counsel                | Relevant competition authority                      |        |
| **FIRPTA withholding**                                       | US real property transferred by foreign person               | At closing (buyer withholds 15%) [VERIFY]                                                                         | Settlement Agent                 | IRS Form 8288                                       |        |
| **Transfer tax returns**                                     | Real estate                                                  | At or before recording [VERIFY per state]                                                                         | Conveyancing counsel             | State / county authority                            |        |

---

## Closing Binder Structure

Organize the closing binder into the following standard tabs/sections:

| Tab        | Section Title                                | Contents                                                                                          |
| ---------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Tab 1**  | Transaction Overview                         | Closing checklist (final); transaction summary; parties list; counsel list                        |
| **Tab 2**  | Principal Transaction Documents              | Purchase agreement / merger agreement / credit agreement (executed); amendments and modifications |
| **Tab 3**  | Disclosure Schedules                         | Seller's disclosure schedules (executed/initialed)                                                |
| **Tab 4**  | Corporate Authorization — Seller / Target    | Board resolutions / UWC; stockholder approvals; officer certificates; incumbency certificates     |
| **Tab 5**  | Corporate Authorization — Buyer / Acquirer   | Board resolutions / UWC; officer certificates; incumbency certificates                            |
| **Tab 6**  | Good Standing and Qualification Certificates | Good standing certificates for all entities (all jurisdictions)                                   |
| **Tab 7**  | Legal Opinions                               | Seller's counsel opinion; buyer's counsel opinion; special opinions                               |
| **Tab 8**  | Representations Bring-Down Certificates      | Seller bring-down; buyer bring-down; officer certificates confirming covenants                    |
| **Tab 9**  | Regulatory Approvals                         | HSR clearance; CFIUS approval; industry regulator approvals; antitrust certificates               |
| **Tab 10** | Third-Party Consents                         | Material contract consents; lender consents; landlord consents; license consents                  |
| **Tab 11** | Transfer Documents                           | Bills of sale; IP assignments; lease assignments; deed(s); assignment and assumption agreements   |
| **Tab 12** | Financing Documents                          | Credit agreement; security agreement; notes; guaranties; intercreditor agreement                  |
| **Tab 13** | Escrow and Funds Flow                        | Escrow agreement; funds flow memo; closing statement; wire confirmation                           |
| **Tab 14** | Employment and Benefits                      | Key employee agreements; non-compete agreements; ERISA documents                                  |
| **Tab 15** | Real Property                                | Deed; title insurance commitment / policy; survey; environmental report; estoppel certificates    |
| **Tab 16** | Post-Closing Obligations                     | Post-closing obligation tracker; regulatory filing calendar; deadline dates                       |
| **Tab 17** | Miscellaneous                                | Any additional closing documents not categorized above                                            |

**Closing Binder Delivery Protocol:**

- Assemble initial draft binder 3 business days before closing
- Update with executed documents on closing day
- Deliver final closing binder within 2–3 business days of closing
- Prepare customized versions for different parties as needed (exclude confidential documents)
- Retain archive copy for minimum 7 years (or longer per applicable statute of limitations)

---

## Severity and Priority Classification

### Condition Classification Summary

When assessing each closing condition, apply the dual classification:

**Status × Criticality Matrix:**

|                    | BLOCKING                                      | MATERIAL                        | ADMINISTRATIVE    |
| ------------------ | --------------------------------------------- | ------------------------------- | ----------------- |
| **SATISFIED** ✅   | Closing may proceed on this item              | Post-closing obligation met     | Complete          |
| **IN PROGRESS** 🔄 | Monitor daily; alert if 7 days before closing | Weekly status check             | Routine follow-up |
| **WAIVED** 🟡      | Confirm waiver authority and documentation    | Confirm waiver scope            | Note in binder    |
| **FAILED** 🔴      | **IMMEDIATE ESCALATION — Closing blocked**    | Assess indemnification exposure | Cure post-closing |
| **OPEN** ⬜        | **URGENT — Initiate immediately**             | Initiate per timeline           | Schedule          |

---

## Prioritization Framework

Organize all checklist items into three tiers for management focus:

### Tier 1 — BLOCKING Conditions (Must Satisfy Before Closing)

Items where closing cannot proceed without satisfaction or valid waiver:

- All conditions precedent that are contractually non-waivable
- Regulatory clearances subject to standstill obligations (HSR, EU Merger Regulation, CFIUS)
- Government approvals required by applicable law
- Fundamental representations bring-down certificates
- Execution of principal transaction documents
- Funding / wiring of purchase price

**Management protocol**: Track daily; escalate to senior counsel 7 days before closing if
OPEN or IN PROGRESS; document every communication.

### Tier 2 — MATERIAL Conditions (Required but May Have Post-Closing Cure Path)

Items with defined post-closing cure periods or that, if unsatisfied, create indemnification
exposure rather than blocking closing:

- Third-party consents that are contractually required but for which there is a limited waiver
  or deemed-consent mechanism
- Post-closing regulatory filings with defined deadlines (SEC filings, state filings)
- UCC / PPSA / deed recording (typically completed within hours or days of closing)
- Post-closing key employee agreements

**Management protocol**: Track weekly; pre-populate responsibility matrix with deadlines;
set calendar reminders for each deadline.

### Tier 3 — ADMINISTRATIVE Obligations (Post-Closing Housekeeping)

Items that, if incomplete, do not affect transaction validity but must be completed for
good order:

- Closing binder assembly and delivery
- Government records and corporate book updates
- License, permit, and professional registration transfers not immediately material
- Bank account and authorized signatory updates
- Insurance certificate updates and additional-insured endorsements

**Management protocol**: Track monthly for first 6 months post-closing; delegate to
corporate secretary or junior counsel with oversight.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any checklist output. If any gate fails,
revise before delivering.

| Gate           | Rule                                                                                                                   | Fail Action                                                                         |
| -------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Source**     | Every filing deadline cites a specific statute, rule, or regulation                                                    | Add citation or mark "[UNVERIFIED — counsel to confirm current threshold/deadline]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction                                            | Fix format                                                                          |
| **Currency**   | Every threshold and deadline confirmed as current (HSR thresholds and UCC details change)                              | Flag "[CHECK CURRENCY — threshold/deadline may have been updated]"                  |
| **Domain**     | Analysis stays within the transaction's identified jurisdiction(s). No assumptions from other jurisdictions leaking in | Remove or flag jurisdictional bleed                                                 |
| **Confidence** | Uncertainty explicitly stated, not hidden. If a filing requirement is uncertain, say so                                | Add confidence qualifier                                                            |

### Self-Interrogation for BLOCKING / FAILED Conditions

For any condition classified as BLOCKING and FAILED (or BLOCKING and at risk of failing):
apply this 3-pass review before reporting:

**Pass 1 — Legal Chain Integrity**:

- Is the condition actually contractually BLOCKING, or is there a waiver right that has not
  been assessed?
- Has the applicable legal authority (statute, agreement provision) been correctly identified?
- Would counsel in this jurisdiction reach the same conclusion about the condition's satisfaction
  standard?

**Pass 2 — Completeness**:

- Have all possible paths to satisfying this condition been considered?
- Are there alternative mechanisms (waiver, escrow holdback, indemnification arrangement) that
  could allow closing to proceed while the condition is resolved post-closing?
- Have all regulatory dimensions been considered (not just the obvious approvals)?

**Pass 3 — Challenge**:

- What is the strongest argument that this condition IS or CAN BE satisfied on the current
  timeline?
- Under what circumstances might a reasonable transactional attorney advise closing anyway
  (e.g., the waiver right is clearly available and the risk is manageable)?
- Is the BLOCKED classification proportionate, or should this be reclassified as MATERIAL
  with a post-closing cure obligation?

Mark the audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each regulatory filing deadline and condition satisfaction standard, assign a confidence
level. Declining confidence requires more explicit flagging:

| Level        | Range     | Meaning                                                    | Required Action in Output                             |
| ------------ | --------- | ---------------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled obligation; specific statutory deadline confirmed  | State deadline with confidence                        |
| **High**     | 0.80–0.94 | Strong authority; minor interpretation questions           | State deadline with brief caveat                      |
| **Probable** | 0.60–0.79 | Good arguments; threshold or timing may have been adjusted | State with explicit [VERIFY] and rationale            |
| **Possible** | 0.40–0.59 | Genuinely uncertain; multiple conflicting sources          | Flag for counsel verification with both sides         |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                                    | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Multi-Party Coordination Framework

Transactions involve multiple parties and their counsel. Map responsibilities explicitly:

| Workstream           | Primary Party                | Primary Counsel             | Second Review          | Deadline Lead Time             |
| -------------------- | ---------------------------- | --------------------------- | ---------------------- | ------------------------------ |
| Buyer conditions     | Buyer                        | Buyer's Counsel             | —                      | 3–5 days pre-closing           |
| Seller conditions    | Seller                       | Seller's Counsel            | —                      | 3–5 days pre-closing           |
| Regulatory approvals | Both                         | Lead regulatory counsel     | Both counsel           | 30–180 days pre-closing        |
| Third-party consents | Seller                       | Seller's Counsel            | Buyer's Counsel review | 4–8 weeks pre-closing          |
| Financing conditions | Buyer                        | Lender's Counsel            | Buyer's Counsel        | 5 business days pre-closing    |
| Signature logistics  | All parties                  | Closing coordinator         | Both counsel           | 2–3 days pre-closing           |
| Funds flow           | Buyer + Seller               | Both counsel + Escrow Agent | CFO both parties       | 3–5 days pre-closing           |
| Post-closing filings | Surviving / acquiring entity | Designated filing counsel   | Compliance team        | Calculated from closing date   |
| Closing binder       | Both counsel                 | Both counsel                | —                      | 2–3 business days post-closing |

**Coordination cadence:**

- Weekly status calls for first 4 weeks after signing
- Bi-weekly or weekly calls during final 30 days pre-closing
- Daily checklist review calls in final 5 business days before closing
- Closing day protocol meeting confirming execution order, wire sequence, and condition satisfaction

---

## Anti-Patterns

Explicit catalogue of what NOT to do when managing a transaction closing:

1. **Starting the closing checklist after signing** — The closing checklist should be initiated
   at or before signing, not in the final week before the target closing date. Regulatory approvals,
   third-party consents, and KYC documentation can take months. A late-start checklist creates
   artificial urgency and increases the risk of closing delays.

2. **Imprecise UCC debtor name** — Even a minor variation from the debtor's exact legal name
   (as shown on state formation documents) can render a UCC-1 filing seriously misleading and
   unenforceable against a lien creditor. Always confirm the debtor's exact legal name against
   the state's entity records before filing. [VERIFY — UCC § 9-503]

3. **Bring-down certificate standard mismatch** — The bring-down certificate must precisely
   mirror the bring-down standard in the purchase agreement. A certificate that says "true and
   correct in all material respects" when the agreement requires "true and correct" (unqualified)
   for fundamental representations creates a closing condition gap that can delay or block closing.

4. **Treating all third-party consents as equivalent** — Lender consents (change-of-control under
   debt instruments) have legal consequences if not obtained: they may accelerate debt or trigger
   events of default. Government permit consents may be legally non-assignable. Categorize consents
   by legal consequence before treating any as waivable.

5. **Ignoring the standstill obligation for regulated approvals** — Closing before obtaining
   required regulatory clearances (HSR, EU Merger Regulation, CFIUS for mandatory filings, NSIA
   in the UK) is a legal violation. Gun-jumping carries significant penalties. Never close before
   required clearances are confirmed in writing.

6. **Escrow KYC left to the last minute** — Escrow account setup requires KYC/AML verification
   that can take 1–4 weeks. Beneficial ownership certifications, W-9/W-8 forms, and FATCA
   documentation must be collected well in advance. A closing delayed because the escrow account
   is not open is avoidable.

7. **Funds flow memo treated as a formality** — The funds flow memo is a binding document that
   coordinates simultaneous wire transfers from multiple parties. Errors in wire instructions,
   incorrect amounts, or ambiguous release triggers can cause closing day disasters (funds released
   before document execution; payments to wrong accounts). Require both parties' counsel to review
   and sign off on the final funds flow memo before closing day.

8. **Missing change-of-control triggers in material contracts** — Not all change-of-control
   provisions are labeled as such. They may appear in "assignment" clauses, "key person" clauses,
   "ownership change" definitions, or "most favored nations" provisions. A comprehensive consent
   audit must review all material contracts, not just those with obvious "change of control" language.

9. **Post-closing filings treated as optional** — SEC Form 8-K (4 business days), state merger
   certificates, deed recording, and UCC-1 filings are not optional. Missing these deadlines creates
   regulatory exposure, priority disputes (UCC), and SEC enforcement risk. Assign responsible counsel
   immediately upon closing and calendar all deadlines.

10. **Closing binder assembled from drafts** — The closing binder must contain executed, final versions
    of every document. A closing binder with draft or superseded documents is actively harmful — it
    creates evidentiary confusion and can undermine the parties' rights in a post-closing dispute. Allow
    2–3 business days after closing to assemble the binder with confirmed executed versions.

11. **Single party managing the checklist** — For complex transactions, no single party's counsel
    should unilaterally maintain the master closing checklist. The checklist should be a shared
    document updated by all parties' counsel in real time, with a designated closing coordinator
    responsible for the master version.

12. **Waiving conditions without documentation** — Any waiver of a closing condition should be in
    writing, signed by the party with the right to waive, and clearly specify which condition is
    being waived and to what extent. An oral waiver may be contested post-closing when disputes arise
    about whether a condition was actually satisfied.

13. **Ignoring FIRPTA and foreign seller withholding** — In US real property transactions involving
    a foreign seller, the buyer is responsible for withholding 15% of the amount realized under FIRPTA.
    If the buyer fails to withhold, the buyer may become liable for the tax. Check seller's status
    before closing; collect the FIRPTA certificate or initiate withholding. [VERIFY — 26 U.S.C. § 1445]

14. **Confusing sign-and-close with deferred closing logistics** — A simultaneous sign-and-close
    requires all conditions to be satisfied at signing; a deferred closing requires ongoing tracking
    through a condition-satisfaction period. Using a deferred-closing checklist for a sign-and-close
    transaction (or vice versa) will create gaps: for sign-and-close, all deliverables must be ready
    on day one; there is no time to cure deficiencies.

15. **Omitting transition mechanics from the checklist** — Post-closing transition — transfer of
    IT systems, customer relationships, employee onboarding, facility access — is a common checklist
    gap. A transition services agreement (TSA) is often required to bridge the operational gap. If
    the parties have agreed to a TSA, the TSA execution is itself a closing deliverable that belongs
    on the checklist.

16. **Filing UCC-1 too early** — A UCC-1 filed more than 20 days before the security agreement is
    signed may not be effective to perfect the lien under certain circumstances [VERIFY — state law
    variations]. Coordinate with the security agreement execution to ensure proper sequencing.

17. **Ignoring post-closing covenants with short deadlines** — Some covenants in the purchase agreement
    have short post-closing windows (e.g., 10 business days to deliver a final closing statement; 30
    days to notify counterparties of the transaction). Populate these deadlines from the agreement and
    assign them immediately upon closing. Do not wait for post-closing disputes to read the covenants.

18. **No contingency for delayed regulatory approval** — Transactions with regulatory closing conditions
    should include a "drop-dead date" after which either party may terminate if closing has not occurred.
    The closing checklist should prominently flag the drop-dead date and any extension rights so the
    parties can plan accordingly.

---

## Writing Standards

Apply plain-language discipline to all closing checklist output:

**For condition summaries and status updates** (shared with all parties):

- State the condition clearly: "Condition X requires delivery of [item] by [party] by [date]."
- Status first, then action: "BLOCKED — [party] has not received [item]. Escalated to senior counsel."
- Short sentences. Active voice. Name the responsible party explicitly.
- Avoid legal jargon when plain language is equally precise.

**For regulatory filing descriptions**:

- Name the specific statute and form: "File Form 8-K (Item 2.01) within 4 business days of closing under
  Item 5.01 of the SEC Rules — [VERIFY current requirements]."
- Include the filing location: "Filed with SEC EDGAR / Secretary of State of Delaware / County Recorder."
- State the consequence of failure: "Late 8-K filing triggers SEC enforcement exposure and public
  disclosure obligations."

**Quality gates before delivery**:

1. Can a non-lawyer business stakeholder read the executive summary and understand the current closing status?
2. Is every filing deadline cited with its source (or marked [VERIFY])?
3. Are any instructions vague or ambiguous? If yes, fix.
4. Are all BLOCKING conditions explicitly called out at the top of the output?
5. Could any sentence be shorter without losing meaning? If yes, shorten.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 3, verify current HSR filing thresholds, EU Merger Regulation turnover thresholds, and
  CFIUS / NSIA mandatory filing sector scope
- Confirm current UCC Article 9 debtor-name requirements and search office procedures
- Verify current SEC Form 8-K, Form 4, and Schedule 13D/G deadlines
- Verify FIRPTA withholding rate and exemption thresholds
- Check current state merger certificate filing requirements for the applicable jurisdiction(s)
- Mark all legalcode-mcp-verified deadlines and thresholds as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all filing deadlines, thresholds, and requirements with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus the checklist on structural completeness, responsibility assignment, and workflow coordination
  rather than legal certainty about specific deadlines
- Include a prominent notice that all filing deadlines require verification before use

---

## Glass Box Audit Trail

Every closing checklist output MUST include a Glass Box audit section:

```yaml
glass_box:
  transaction: "[Transaction name / Deal codename]"
  transaction_type: "[Stock Purchase / Asset Purchase / Merger / Secured Financing / Real Estate]"
  framework_used: "[Framework A / B / C / D / E or combination]"
  party_perspective: "[Buyer / Seller / Lender / Borrower / Neutral]"
  target_closing_date: "[Date or 'Not yet confirmed']"
  jurisdiction: "[Governing jurisdiction(s)]"
  regulatory_complexity: "[Antitrust / Foreign Investment / Sector-Specific / Public Company / Standard]"
  conditions_total: "[number of conditions identified]"
  conditions_blocking: "[number BLOCKING]"
  conditions_material: "[number MATERIAL]"
  conditions_administrative: "[number ADMINISTRATIVE]"
  conditions_satisfied: "[number SATISFIED at time of checklist]"
  conditions_at_risk: "[number IN PROGRESS and within 7 days of target close]"
  conditions_failed: "[number FAILED]"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "[/tmp/legalcode-closing-research.md or 'Not created']"
  filing_deadlines_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no BLOCKING-FAILED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations — e.g., 'Post-closing filings not yet populated: closing date not confirmed']"
    - "[Jurisdiction limitations — e.g., 'HSR thresholds marked VERIFY — not yet confirmed against current year']"
  reviewer: "AI-assisted — requires qualified transactional counsel review"
```

---

## Output Format Template

Structure the final closing checklist deliverable as follows:

```markdown
## Transaction Closing Checklist

**Transaction**: [name]
**Transaction Type**: [Stock Purchase / Asset Purchase / Merger / etc.]
**Party Perspective**: [Buyer's / Seller's / Neutral]
**Jurisdiction(s)**: [governing law]
**Target Closing Date**: [date or TBD]
**Checklist Date**: [date of checklist generation]
**Coordinator**: [firm / counsel]

---

### CLOSING STATUS SUMMARY

| Category             | Total | SATISFIED | IN PROGRESS | OPEN | WAIVED | FAILED |
| -------------------- | ----- | --------- | ----------- | ---- | ------ | ------ |
| BLOCKING Conditions  |       |           |             |      |        |        |
| MATERIAL Conditions  |       |           |             |      |        |        |
| ADMINISTRATIVE Items |       |           |             |      |        |        |
| **TOTAL**            |       |           |             |      |        |        |

> ⚠️ **ALERTS**: [List any BLOCKING conditions that are FAILED or at risk; any regulatory
>
> > deadlines within 7 days; any unresolved third-party consents for BLOCKING conditions]

---

### SECTION 1: PRE-CLOSING CONDITIONS PRECEDENT

#### 1.1 Corporate Authority & Authorization

| #     | Item                       | Responsible      | Target Date | Status  | Evidence            | Notes |
| ----- | -------------------------- | ---------------- | ----------- | ------- | ------------------- | ----- |
| 1.1.1 | Board resolutions — Seller | Seller's Counsel | [date]      | ⬜ OPEN | Executed resolution |       |
| ...   |                            |                  |             |         |                     |       |

#### 1.2 Representations Bring-Down

| #     | Item                          | Standard                                 | Responsible | Target Date | Status  | Evidence             |
| ----- | ----------------------------- | ---------------------------------------- | ----------- | ----------- | ------- | -------------------- |
| 1.2.1 | Seller bring-down certificate | [Unqualified / Material / MAE-qualified] | Seller      | [date]      | ⬜ OPEN | Executed certificate |
| ...   |                               |                                          |             |             |         |                      |

#### 1.3 Regulatory Approvals

| #     | Approval      | Authority | Threshold / Basis    | Target Clearance Date | Status  | Notes |
| ----- | ------------- | --------- | -------------------- | --------------------- | ------- | ----- |
| 1.3.1 | HSR clearance | DOJ / FTC | [threshold] [VERIFY] | [date]                | ⬜ OPEN |       |
| ...   |               |           |                      |                       |         |       |

#### 1.4 Third-Party Consents

| #     | Contract / Counterparty        | Consent Type      | Request Date | Status  | Evidence        |
| ----- | ------------------------------ | ----------------- | ------------ | ------- | --------------- | --- |
| 1.4.1 | [Contract name — counterparty] | Change-of-control | [date]       | ⬜ OPEN | Written consent |
| ...   |                                |                   |              |         |                 |     |

#### 1.5 Transaction Documents — Execution Status

| #     | Document           | Parties        | Signatory(ies) | Execution Format | Status  |
| ----- | ------------------ | -------------- | -------------- | ---------------- | ------- |
| 1.5.1 | Purchase Agreement | Buyer / Seller | [names]        | Electronic / Wet | ⬜ OPEN |
| ...   |                    |                |                |                  |         |

---

### SECTION 2: SIGNATURE PAGE TRACKER

| #   | Document   | Signatory      | Party          | Authorization          | Format         | Status  |
| --- | ---------- | -------------- | -------------- | ---------------------- | -------------- | ------- |
| 2.1 | [Document] | [Name / Title] | [Buyer/Seller] | [Board resolution/POA] | [Wet/DocuSign] | ⬜ OPEN |

---

### SECTION 3: FUNDS FLOW MEMO

**Purchase Price Components:**

- Base purchase price: $[amount]
- Working capital adjustment (estimated): $[amount]
- Net debt adjustment (estimated): $[amount]
- Transaction expense allocation: $[amount]
- **Estimated aggregate consideration**: $[amount]

**Wire Instructions:**
| # | From | To | Amount | Timing | Status |
|---|------|----|--------|--------|--------|
| 3.1 | Buyer | Escrow Account | $[amount] | By [date/time] | ⬜ OPEN |
| 3.2 | Escrow Agent | Seller | $[amount] | Upon condition satisfaction | ⬜ OPEN |
| ... | | | | | |

**Escrow Details:**

- Escrow Agent: [name]
- Escrow Amount: $[amount] / [purpose]
- Release Conditions: [summary of release triggers]
- Dispute Resolution: [per escrow agreement Section X]

---

### SECTION 4: POST-CLOSING OBLIGATION TRACKER

| #   | Obligation                     | Deadline            | Responsible       | Filing Location | Status     |
| --- | ------------------------------ | ------------------- | ----------------- | --------------- | ---------- |
| 4.1 | SEC Form 8-K [VERIFY]          | D + 4 business days | SEC Counsel       | EDGAR           | ⬜ PENDING |
| 4.2 | Certificate of Merger [VERIFY] | D + 30 days         | Corporate Counsel | SOS Delaware    | ⬜ PENDING |
| 4.3 | UCC-1 Filing [VERIFY]          | D + 0 (at closing)  | Lender's Counsel  | SOS [state]     | ⬜ PENDING |
| ... |                                |                     |                   |                 |            |

---

### SECTION 5: CLOSING BINDER INDEX

**Transaction**: [name] | **Closing Date**: [date]

| Tab | Section              | Document                 | Date   | Parties        | Execution Status | Pages |
| --- | -------------------- | ------------------------ | ------ | -------------- | ---------------- | ----- |
| 1   | Transaction Overview | Closing Checklist        | [date] | All            | Final            |       |
| 2   | Principal Documents  | Stock Purchase Agreement | [date] | Buyer / Seller | Executed         |       |
| ... |                      |                          |        |                |                  |       |

---

### SECTION 6: GLASS BOX AUDIT TRAIL

[Insert Glass Box YAML from template above]

---

_Checklist generated: [date] — AI-assisted — requires qualified transactional counsel review._
_All filing deadlines marked [VERIFY] require confirmation against current statute/regulation._
```

---

## Localization Notes

When adapting this skill for specific jurisdictions, update the following elements:

| Element                            | US                                  | UK                                              | EU (Germany example)                  | Canada                          |
| ---------------------------------- | ----------------------------------- | ----------------------------------------------- | ------------------------------------- | ------------------------------- |
| **Competition clearance**          | HSR — FTC/DOJ                       | CMA Phase 1 / Phase 2                           | BKartA / EU Merger Reg.               | Competition Bureau              |
| **Foreign investment**             | CFIUS / FIRRMA                      | NSIA 2021 (mandatory sectors)                   | BMWi FDI screening                    | Investment Canada Act           |
| **Share transfer formality**       | Stock certificate + transfer ledger | Instrument of transfer (stock transfer form)    | GmbH: notarial deed required          | Varies by province              |
| **Real estate recording**          | County Recorder                     | Land Registry (AP1)                             | Grundbuchamt (land registry)          | Land titles office (provincial) |
| **Transfer taxes**                 | State transfer taxes (vary)         | SDLT (14-day return)                            | GrESt (real estate transfer tax)      | Land transfer tax (provincial)  |
| **Corporate filing**               | SOS (state)                         | Companies House                                 | Handelsregister                       | Provincial registry             |
| **UCC equivalent**                 | UCC-1 (SOS)                         | Form MR04 / charges register at Companies House | No direct equivalent (EU PPSR varies) | PPSA (provincial)               |
| **Secured transaction perfection** | UCC Article 9                       | CA 2006 charges registration                    | HGB / pledge formalities              | PPSA provincial registration    |
| **Employment — transfer**          | WARN Act (60-day notice)            | TUPE 2006 (information 28 days pre)             | BetrVG (works council)                | ESA / WARN (provincial)         |

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis developed from:

- Deep web research on M&A closing checklist best practices, conditions precedent standards,
  UCC filing requirements, SEC post-closing filing timelines (Form 8-K, Form 4, Schedule 13D/G),
  FIRPTA mechanics, real estate recording requirements, and escrow setup best practices
- Repository pattern analysis of `legalcode-purchase-agreement-review`,
  `legalcode-ma-due-diligence-checklist`, `legalcode-board-resolution-drafter`, and
  `legalcode-contract-review` (reference standard for quality frameworks)
- Quality frameworks (Citation Quality Gates, Self-Interrogation, Confidence Scoring, Glass Box
  audit trail) adapted from the `legalcode-contract-review` gold standard
- Transaction-type framework adapted from the M&A structure taxonomy in
  `legalcode-ma-due-diligence-checklist`
