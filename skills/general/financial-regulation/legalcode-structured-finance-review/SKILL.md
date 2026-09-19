---
name: legalcode-structured-finance-review
description: Review structured finance and securitization transactions — ABS (asset-backed securities),
  MBS (mortgage-backed securities), CLO (collateralized loan obligations), and other asset-backed structures.
  Use when reviewing securitization transaction documents (indentures, trust agreements, purchase agreements,
  servicing agreements, offering memoranda, CLO indentures), conducting legal due diligence on structured
  finance transactions, advising on regulatory compliance for structured products, or assessing the structural
  integrity of securitization vehicles (SPVs, SSPEs, trusts).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review structured finance and securitization transactions — ABS (asset-backed securities), MBS (mortgage-backed securities), CLO (collateralized loan obligations), and other asset-backed structures. Performs true sale analysis, bankruptcy remoteness assessment, SPV governance review, credit enhancement adequacy, waterfall mechanics verification, and regulatory compliance across Regulation AB II (US), EU Securitisation Regulation STS framework (EUSR 2017/2402), UK Securitisation Regulations 2024, and risk retention rules (Dodd-Frank 17 CFR Part 246 / EUSR Article 6). Covers rating agency legal opinion requirements and common transaction red flags. Use when reviewing securitization transaction documents (indentures, trust agreements, purchase agreements, servicing agreements, offering memoranda, CLO indentures), conducting legal due diligence on structured finance transactions, advising on regulatory compliance for structured products, or assessing the structural integrity of securitization vehicles (SPVs, SSPEs, trusts). Jurisdiction-aware across US, UK, and EU with localization markers.


# Legalcode Structured Finance Review

> **Disclaimer**: This skill provides a framework for AI-assisted review of structured
> finance and securitization transaction documents. It does not constitute legal advice.
> All outputs must be reviewed by a qualified legal professional licensed in the relevant
> jurisdiction before any reliance or action. Structured finance law is highly
> jurisdiction-specific, fact-dependent, and rapidly evolving. Statutory and regulatory
> references cited from memory carry hallucination risk — verify every citation against
> current authoritative sources before relying on them. This skill identifies potential
> issues for expert review; it does not guarantee the completeness or accuracy of any
> analysis.

---

## Purpose and Scope

This skill reviews structured finance transaction documents and structures for legal
sufficiency, regulatory compliance, and common risk factors. It is designed for lawyers,
structured finance counsel, compliance officers, and legal due diligence professionals
working on securitization transactions.

**Covers:**

- Transaction structure identification (ABS, MBS, CLO/CLO arbitrage vs. balance sheet, CMBS, RMBS, CDO)
- True sale and recharacterization risk analysis (US, UK, EU)
- Bankruptcy remoteness assessment (SPV governance, separateness, non-consolidation)
- Credit enhancement adequacy review (OC/IC tests, subordination, reserve funds, swap agreements)
- Waterfall mechanics verification (payment priority, coverage tests, sequential vs. pro-rata)
- Regulation AB II compliance (US — Reg. S-K Items 1100-1123, ABS-EE, CEO/CFO certification)
- EU Securitisation Regulation / STS framework compliance (EUSR Reg. 2017/2402)
- UK Securitisation Regulations 2024 compliance (UK SECN)
- Risk retention analysis (US 17 CFR Part 246; EU EUSR Art. 6; UK SECN)
- Rating agency requirements and required legal opinions
- Red flag identification and deal-structural risk assessment
- Servicer commingling, set-off, and counterparty risk analysis

**Does not:**

- Draft securitization transaction documents (see drafting-specific skills)
- Provide investment advice or securities law opinions
- Substitute for qualified structured finance counsel
- Replace jurisdiction-specific regulatory approval or no-action processes

---

## Jurisdiction and Governing Law

This skill covers three primary securitization regimes. Identify the applicable regimes
early — a single transaction may implicate multiple (e.g., a US-originated CLO with EU
institutional investors implicitly triggers EUSR Article 5 due diligence obligations even
if the CLO itself is a US-law transaction).

**US:** UCC Article 9 (true sale / perfection), Bankruptcy Code 11 U.S.C. §§ 101 et seq.,
Dodd-Frank § 941 / 17 CFR Part 246 (risk retention), Regulation AB II (17 CFR 229/230/240),
Delaware LLC Act and Statutory Trust Act (SPV governance).

**EU:** Regulation (EU) 2017/2402 (EUSR / STS framework), Insolvency Regulation (EU)
2015/848, national civil law for true sale (varies by member state).

**UK:** UK Securitisation Regulations 2024 (SI 2024/[No.] effective 1 November 2024),
FCA Securitisation Sourcebook (SECN), Law of Property Act 1925 s.136 (assignment),
Companies Act 2006 s.859A (charge registration), Insolvency Act 1986.

[JURISDICTION-SPECIFIC] When localizing, adapt analysis for:

- **France**: Cession Dailly (Loi Dailly/Code monétaire et financier) assignment mechanism
- **Germany**: Abtretung (§§ 398-413 BGB) assignment; KWG securitization provisions
- **Netherlands**: Stille cessie (silent assignment post-2012 BW reform)
- **Italy**: Legge 130/1999 securitization law (Legge sulla cartolarizzazione)
- **Japan**: Trust Act; special purpose company (TMK) under Asset Liquidation Act
- **Cayman/Jersey/Ireland**: Offshore SPV structuring and orphan trust mechanics

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points, marked **⟁ CLARIFY**
below. Rather than assuming the user's intent, the workflow pauses when:

- The transaction type, structure, or jurisdiction cannot be determined from the documents
- Multiple review approaches are available (full review vs. issue-focused)
- A critical fact (e.g., whether the originator retains servicing) would change the analysis
- Severity classification requires risk appetite or deal context information
- The regulatory regime applicable to investors is unclear

If the user has already provided the relevant context, skip the question and proceed.

---

## Workflow

### Step 1: Accept the Transaction Documents

Accept transaction documents in any of these formats:

- **Files**: PDF, DOCX, or other formats (indenture, PSA, trust agreement, purchase
  agreement, servicing agreement, offering memorandum/OM/PPM, rating agency pre-sale report)
- **URL**: Link to a transaction document in a document repository or filing system
- **Pasted text**: Document text pasted directly into the conversation
- **Summary / term sheet**: High-level description of the transaction structure

If no documents are provided, prompt the user to supply the relevant document(s) or
describe the transaction structure and the specific review concern.

**Priority documents for a complete review** (request if not supplied):

1. Indenture / Trust Deed / Pooling and Servicing Agreement (PSA) — core structural document
2. Receivables / Loan Sale Agreement — true sale document
3. Servicing Agreement (if separate from PSA)
4. Offering Memorandum / Prospectus
5. Swap Agreement (if applicable)
6. Legal opinions (true sale, non-consolidation, enforceability, perfection)

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user:

1. **Transaction type**: What kind of securitization?
   - Options: ABS (specify sub-type: auto, credit card, student loan, equipment, trade
     receivables, other), RMBS, CMBS, CLO (arbitrage or balance sheet), CDO/CLO²,
     Whole Business Securitization (WBS), ABCP conduit, Mixed/Other
   - _Why this matters_: Each asset class has distinct structural norms, regulatory
     requirements, and risk profiles. CLO mechanics differ substantially from RMBS.

2. **Review scope**: What is the primary focus?
   - Options: Full transaction review (all topics), True sale / bankruptcy remoteness only,
     Regulatory compliance (Reg AB / STS / risk retention), Credit enhancement and
     waterfall mechanics, Rating agency requirements and legal opinions, Deal-specific
     issue or red flag investigation, Other
   - _Why this matters_: Allows efficient allocation of review effort.

3. **Role / perspective**: Who does the user represent?
   - Options: Originator/Seller, Issuer/SPV counsel, Underwriter/Arranger counsel,
     Investor/noteholder, Rating agency, Regulator/supervisor, Independent legal counsel,
     Other
   - _Why this matters_: The analysis emphasis shifts depending on the client. Originator's
     counsel optimizes for achievability; investor's counsel maximizes investor protection.

4. **Applicable jurisdiction(s)**: Which regimes apply?
   - Options: US only, EU only, UK only, US + EU (cross-border investors), US + UK,
     UK + EU, All three, Other (specify)
   - _Why this matters_: Determines which regulatory frameworks to apply (Reg AB II,
     EUSR/STS, UK SECN) and which true sale analysis is primary.

5. **Transaction stage**: Where is the transaction?
   - Options: Pre-issuance / due diligence phase, Closing review, Post-closing compliance
     review, Enforcement / workout, Secondary market acquisition
   - _Why this matters_: Affects which issues can still be remedied vs. must be flagged
     for disclosure.

If the user provides partial context, proceed with stated assumptions and flag them
explicitly at the top of the output.

### Step 3: Identify and Map the Transaction Structure

Before deep analysis, map the transaction:

1. **Identify the asset class** and describe the collateral pool (e.g., "Revolving pool of
   US auto loan receivables with weighted average FICO 720 and 48-month WAL")

2. **Map the parties** and their roles:

   | Party             | Role                                                | Key Risk                                 |
   | ----------------- | --------------------------------------------------- | ---------------------------------------- |
   | Originator/Seller | Sells/assigns assets to SPV                         | True sale challenge; rep/warranty breach |
   | Servicer          | Collects payments, manages collateral               | Commingling; servicer insolvency         |
   | SPV/Issuer        | Issues notes; holds assets                          | Bankruptcy remoteness; governance        |
   | Trustee           | Holds assets for noteholders; administers waterfall | Negligence; direction conflicts          |
   | Collateral Admin  | Calculates OC/IC tests, waterfall                   | Calculation errors; conflicts            |
   | Swap Counterparty | Hedges interest rate / FX risk                      | Downgrade / replacement risk             |
   | Rating Agencies   | Rate the notes                                      | Criteria changes; model reliance         |
   | Backup Servicer   | Standby servicer                                    | Warm vs. cold; activation triggers       |

3. **Identify the note structure**: Number of tranches, rating of each, target sizes,
   scheduled legal final maturity, expected maturity, reinvestment period (if CLO)

4. **Identify the governing law** of each key document (may differ: US law indenture,
   English law swap, Cayman articles)

**⟁ CLARIFY** — If the party structure is complex or unclear (e.g., sub-servicers,
originator is also servicer, multiple sellers), confirm your understanding with the user
before proceeding to the substantive analysis.

### Step 4: Gather Legal Authority

Use **legalcode-mcp** to gather jurisdiction-relevant legal authority. Save results to
a temporary reference file at `/tmp/legalcode-structured-finance-authority.md`.

Research the following per applicable jurisdiction:

**US (priority):**

- UCC Article 9 perfection requirements and recharacterization case law (_In re LTV Steel_,
  _Major's Furniture Mart_, _In re Criimi Mae_)
- Bankruptcy Code §§ 362, 541, 544, 546(e), 548 (true sale / stay / fraudulent transfer)
- Substantive consolidation doctrine (_In re Augie/Restivo_, _In re Owens Corning_)
- Current 17 CFR Part 246 text (risk retention)
- Current Regulation AB II (17 CFR §§ 229.1100–229.1123) — any SEC updates
- EGRRCPA open market CLO exemption (if CLO transaction)
- Relevant FDIC/OCC/FRB guidance on SPV treatment

**EU:**

- Current text of EUSR Regulation (EU) 2017/2402 (Articles 5-7, 18-26)
- ESMA RTS on transparency (Reg. 2020/1224) and STS notification
- Any ESMA Q&A or guidance relevant to the transaction type
- Applicable member state insolvency / assignment law (if EU originator)

**UK:**

- UK Securitisation Regulations 2024 (effective 1 Nov 2024) current text
- FCA SECN (Securitisation Sourcebook) current provisions
- LPA 1925 s.136; Companies Act 2006 s.859A
- UK STS recognition regime and transitional period (EU STS recognition: to June 2026) [VERIFY]

**If legalcode-mcp is not connected:**

- Mark all statutory citations with [VERIFY]
- Flag in Glass Box: `legalcode_mcp: "Not connected — all citations require manual verification"`
- Proceed using general knowledge but note limitations explicitly

### Step 5: True Sale Analysis

Analyze whether the asset transfer from originator to SPV constitutes a legal true sale
in the governing jurisdiction. This is the most legally consequential analysis in any
securitization review.

#### 5a. US True Sale Analysis

Apply the multi-factor recharacterization test. Assess each factor and classify overall
risk as **LOW / MEDIUM / HIGH**:

| Factor                           | Green (Supports True Sale)                                          | Red (Supports Recharacterization)                                                   |
| -------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Recourse**                     | Limited to rep/warranty breach only; no full recourse               | Full recourse to originator for credit losses                                       |
| **Control of Assets**            | SPV has full control; originator has no unilateral repurchase right | Originator can repurchase/substitute at will; retains full control                  |
| **Risk of Loss**                 | SPV (and noteholders) bear credit risk; excess spread limited       | Originator bears all loss through unlimited excess spread obligations               |
| **Economic Upside**              | Originator retains only reasonable excess spread                    | All upside returns to originator; SPV is pass-through only                          |
| **Intent / Documentation**       | Clearly labeled as sale; opinions obtained                          | Labeled as financing; no true sale opinion                                          |
| **Accounting Treatment**         | Off-balance-sheet (ASC 860 / IFRS 9 derecognition)                  | On-balance-sheet; characterized as borrowing by originator                          |
| **Transfer Price**               | At or near fair market value                                        | Far below market (suggesting disguised pledge)                                      |
| **Substitution / Clean-up Call** | Clean-up call ≤ 10% at par; no unilateral substitution              | Clean-up call or substitution rights at book value suggesting expectation of return |

**Rating agency standard**: A "would" or "should" level true sale opinion is required for
investment-grade ratings. A "could" opinion is generally insufficient. [VERIFY]

**UCC Article 9 perfection**: Confirm a UCC-1 financing statement has been filed by the
SPV (as buyer) against the originator in the correct jurisdiction (state of the
originator's organization). [JURISDICTION-SPECIFIC] Filing is required even for true
sales of accounts and chattel paper (UCC § 9-309 automatic perfection does NOT apply
to sales of accounts — filing required).

#### 5b. UK True Sale Analysis

Assess the English law characterization of the asset transfer:

1. **Legal vs. equitable assignment**: Confirm whether the transfer is a legal assignment
   under LPA 1925 s.136 (requires written notice to obligors) or an equitable assignment
   (effective without notice, but risks priority issues). Most UK securitizations begin as
   equitable assignment with provisions for legal assignment on enforcement.

2. **True sale vs. charge**: Under English law, a transaction characterized as a sale
   but retaining originator control may be re-characterized as a charge requiring
   registration under Companies Act 2006 s.859A. An unregistered charge is void against
   a liquidator/administrator (s.859H).

3. **Key factors**: Same substance-over-form analysis applies. _Welsh Development Agency
   v Export Finance Co_ [1992]: assignment can be a true sale even if originator retains
   administrative roles. [VERIFY]

4. **Perfection**: Check Companies House charge registration (if structure creates a
   charge) within 21 days of creation.

#### 5c. EU True Sale Analysis

[JURISDICTION-SPECIFIC] EU member state civil law governs. Key points:

- **EUSR Article 20(1)(a)** (for STS): Requires transfer by true sale or assignment or
  transfer with same legal effect under applicable law; absolute and unconditional.
- **France**: Cession Dailly mechanism (Code monétaire et financier Art. L.313-23)
  provides reliable assignment without debtor notification. Provides "super-priority"
  protection.
- **Germany**: Abtretung (BGB §§ 398-413) effective without notice; no formal requirements.
- **Netherlands**: Silent assignment (cessie Art. 3:94(3) BW) — notification required
  but can be deferred to enforcement event.
- **Set-off risk**: EU civil law jurisdictions generally allow obligors to set off claims
  against the original creditor (assignor) for claims existing before notice of assignment.
  [JURISDICTION-SPECIFIC: Assess under applicable national law.]

**⟁ CLARIFY** — If the true sale analysis reveals factors supporting recharacterization
risk, present the specific factors to the user and ask whether the deal economics can be
restructured (e.g., reducing originator recourse), or whether the issue should be flagged
as a RED risk and disclosed in the OM.

### Step 6: Bankruptcy Remoteness Analysis

Assess whether the SPV is genuinely bankruptcy-remote from the originator. Review each
element:

#### 6a. Structural Elements Checklist

| Element                                                                 | Present? | Adequate? | Issue |
| ----------------------------------------------------------------------- | -------- | --------- | ----- |
| Single-purpose restriction in organizational documents                  |          |           |       |
| Non-petition covenant (minimum 1yr + 1day after final payment) [VERIFY] |          |           |       |
| Independent director / manager provisions                               |          |           |       |
| Separateness covenants in organizational documents                      |          |           |       |
| Separateness covenants in transaction documents                         |          |           |       |
| Prohibition on SPV guaranteeing obligations of affiliates               |          |           |       |
| Prohibition on SPV pledging assets for affiliate benefit                |          |           |       |
| Separate books, records, and bank accounts                              |          |           |       |
| Arm's-length requirement for affiliate transactions                     |          |           |       |
| No commingling covenant                                                 |          |           |       |
| Adequate capitalization provision                                       |          |           |       |

#### 6b. Independent Director / Manager Review

Confirm that independent directors / managers:

- Have no material relationship with originator, sponsor, manager, or their affiliates
- Are obligated to consider the interests of the entity (and creditors) separately
- Must consent to any voluntary bankruptcy filing
- Are from a recognized professional independent director provider, or otherwise
  meet rating agency criteria

Flag as **CRITICAL** if:

- No independent director/manager requirement exists
- Independent director has a material relationship with the originator
- Originator can remove the independent director without cause and at will
- Organizational documents do not explicitly require independent director consent
  for a voluntary bankruptcy filing

#### 6c. Substantive Consolidation Analysis (US)

Assess factors under _In re Augie/Restivo_ (2d Cir. 1988) and _In re Owens Corning_
(3d Cir. 2005) tests:

- Are creditors of the originator and SPV sufficiently distinct?
- Is the SPV held out as a separate entity (distinct branding, contracts, disclosures)?
- Are assets and liabilities clearly segregated (no commingling of assets, no parent
  guarantee of SPV debt)?
- Is the SPV used for other purposes (potentially suggesting a sham entity)?

**Non-consolidation opinion**: Confirm whether a non-consolidation opinion has been
delivered at closing. Note its form ("should" vs. "would" level) and identify any
assumptions it relies on that must remain true throughout the transaction's life (e.g.,
continued separateness practices).

**⟁ CLARIFY** — If a non-consolidation opinion is absent but required by rating agencies
for the transaction's ratings, flag as RED and ask whether the user intends to obtain one
or has a documented reason it is not required.

### Step 7: Credit Enhancement and Waterfall Review

Analyze the adequacy and structure of credit enhancement, then verify waterfall mechanics.

#### 7a. Credit Enhancement Adequacy

For each form of credit enhancement present, assess:

| Enhancement Type                  | Present | Amount / Level | Rating Agency Required? | Issue |
| --------------------------------- | ------- | -------------- | ----------------------- | ----- |
| Overcollateralization (OC)        |         |                |                         |       |
| Subordination (tranche structure) |         |                |                         |       |
| Excess spread / reserve account   |         |                |                         |       |
| Cash reserve fund                 |         |                |                         |       |
| Swap agreement (rate/FX hedge)    |         |                |                         |       |
| Third-party guarantee / wrap      |         |                |                         |       |
| Letter of credit                  |         |                |                         |       |

**OC / IC Test Review:**

- Identify the OC and IC test levels for each rated tranche
- Confirm the calculation methodology (par value basis; CCC haircut provisions)
- Verify what happens on test failure: cash diversion trigger → sequential pay
- Confirm whether the manager (for CLOs) can "cure" a test failure through asset sales
  or new purchases

**Swap Agreement Review:**

- Identify the counterparty and its current rating
- Identify the downgrade triggers:
  - Tier 1 (lower trigger): Obligation to post collateral under ISDA CSA
  - Tier 2 (higher trigger): Obligation to replace counterparty within specified period
- Confirm: Is the replacement timeline adequate (typically 30 days)? [VERIFY]
- Confirm: Are replacement criteria defined in the indenture?
- If the counterparty is an affiliate of the originator/manager: flag as **RED** (creates
  double risk exposure — originator insolvency may impair both the assets and the hedge)

**⟁ CLARIFY** — If OC or IC tests are set at levels significantly below what rating agencies
typically require for the target ratings, ask whether the lower levels have been confirmed
with the rating agencies or whether this is a potential rating concern.

#### 7b. Waterfall Mechanics Verification

Map the priority of payments (interest waterfall and principal waterfall) and verify:

1. **Interest waterfall**: Trace the priority from senior expenses → most senior notes →
   OC/IC tests → junior notes → subordinated fees → equity residual. Confirm no
   "leakage" to equity before senior tests are satisfied.

2. **Principal waterfall**: Distinguish between:
   - **Sequential (hard)**: All principal to most senior tranche until repaid — lower risk
     for senior investors
   - **Pro-rata**: Simultaneous pro-rata repayment — more favorable to equity; triggers
     back to sequential on test failure or event of default

3. **Coverage test failure mechanics**: Confirm that test failure immediately switches
   principal allocation to sequential pay and that the test cure period is appropriate.

4. **Reinvestment period** (CLOs): Identify end date; confirm that eligible investments
   are well-defined; confirm that the manager cannot reinvest in non-eligible collateral
   or breach concentration limits without triggering a test failure.

5. **Events of default**: Identify EOD triggers (payment default, insolvency event,
   covenant breach, coverage test breach at a defined level); confirm the remedy (note
   acceleration) and the process for noteholder consent to direct enforcement.

**Flag as RED** if: Waterfall allows equity distributions before all OC/IC tests are
satisfied; interest payments are not fully cash-flow matched; no EOD provision for
extended coverage test failure.

### Step 8: Regulatory Compliance Review

Apply the applicable regulatory frameworks based on the jurisdictions identified in
Step 2.

#### 8a. Regulation AB II (US — Public ABS Transactions)

_Applies to registered public ABS offerings under the Securities Act of 1933._

| Requirement                                              | Location in Documents  | Compliant? | Issue |
| -------------------------------------------------------- | ---------------------- | ---------- | ----- |
| Shelf registration eligibility (Form SF-3 conditions)    | Registration statement |            |       |
| CEO/CFO certification (17 CFR 240.15d-18)                | Certification exhibit  |            |       |
| Asset-level data disclosure — ABS-EE (Exhibit 102)       | Form ABS-EE            |            |       |
| Correct data fields for asset class (Reg. S-K Item 1111) | ABS-EE                 |            |       |
| Originator/sponsor disclosure (Item 1104)                | Prospectus             |            |       |
| Static pool data (Item 1105)                             | Prospectus             |            |       |
| Servicer disclosure (Item 1108)                          | Prospectus             |            |       |
| Trustee disclosure (Item 1110)                           | Prospectus             |            |       |
| Credit enhancement description (Item 1113-1114)          | Prospectus             |            |       |
| Derivative instruments disclosure (Item 1115)            | Prospectus             |            |       |
| Ongoing Exchange Act reporting (Form 10-D/10-K/8-K)      | Reporting obligations  |            |       |

**Note**: Regulation AB II applies to _registered_ public ABS. Private placements (Rule
144A, Regulation D, Regulation S) have different (lighter) disclosure obligations but
must still satisfy applicable antifraud provisions.

**⟁ CLARIFY** — If the transaction is a Rule 144A offering with registration rights,
confirm whether the exchange offer registration will trigger full Reg AB II disclosure
obligations and whether the transaction documents contemplate this.

#### 8b. EU Securitisation Regulation (EUSR) / STS Framework

_Applies where the transaction involves EU institutional investors (EUSR Article 5
due diligence obligation on EU institutional investors regardless of where issuer is
incorporated)._

**Risk Retention — Article 6:**

| Retention Method                                  | Selected? | Compliant? | Issue |
| ------------------------------------------------- | --------- | ---------- | ----- |
| Vertical slice (5% of each tranche)               |           |            |       |
| Originator's interest in revolving securitisation |           |            |       |
| Random selection (5%, min. 100 exposures)         |           |            |       |
| First loss tranche (≥ 5% of deal)                 |           |            |       |
| First loss per exposure (5% of each)              |           |            |       |

Confirm: (a) The retaining entity qualifies as originator, sponsor, or original lender;
(b) The retained interest is not hedged or sold down; (c) Ongoing retention is monitored
and disclosed; (d) Disclosure of retention method and amount is made to investors.

**Transparency — Article 7:**

- [ ] Underlying exposure-level data available quarterly (monthly for ABCP)
- [ ] Transaction documentation available to investors
- [ ] Investor reports available
- [ ] Information submitted to ESMA-registered securitisation repository (for public transactions)

**STS Compliance (if STS designation is sought or claimed — Articles 20-26):**

_Simplicity criteria:_

- [ ] True sale of exposures (Article 20(1)(a))
- [ ] No re-securitisation of underlying exposures (Article 20(8))
- [ ] Assets originated in ordinary course of business (Article 20(10))
- [ ] Consistent underwriting standards (Article 20(11))
- [ ] No active portfolio management / substitution beyond initial ramp-up (Article 20(12))

_Transparency criteria:_

- [ ] Underlying exposure-level data verified by independent sample (Article 21(1))
- [ ] Full loan-level data provided to prospective investors pre-pricing (Article 21(3))
- [ ] Liability cash flow model available (Article 21(4))
- [ ] Environmental performance data for energy efficiency (Article 21(5)) [if applicable]

_Standardisation criteria:_

- [ ] Interest rate and FX risk mitigated by eligible derivatives (Article 22(1))
- [ ] No tranches referencing synthetic or re-securitised assets (Article 22(4))
- [ ] Eligible servicer provisions (Article 22(5))
- [ ] Governing law provisions meeting EUSR requirements (Article 22(8))

**STS Notification**: Confirm that STS notification has been (or will be) submitted to
ESMA via the securitisation repository. Note that ESMA does **not** certify STS
compliance — the originator/sponsor bears responsibility.

**⟁ CLARIFY** — If the transaction claims STS designation but any STS criterion is
unclear or potentially non-compliant, flag the specific criterion and ask whether the
originator/sponsor has obtained third-party STS verification and addressed the issue.

#### 8c. UK Securitisation Regulations 2024

_Applies from 1 November 2024. Replaces the onshored EU Securitisation Regulation
(retained EU law)._

Key differences from EUSR to verify: [VERIFY current UK SECN provisions]

- UK risk retention requirements (broadly equivalent to EUSR Article 6 at 5%)
- UK transparency template requirements (may diverge from ESMA RTS going forward)
- UK STS regime and recognition of EU STS transactions (transitional recognition to
  June 2026) [VERIFY]
- FCA supervisory role vs. EU competent authorities
- UK due diligence obligations for UK institutional investors

**⟁ CLARIFY** — For transactions with both EU and UK investors post-Brexit, confirm
whether the transaction is structured to comply with both regimes or whether separate
compliance documentation is being prepared for each investor category.

#### 8d. US Risk Retention (17 CFR Part 246)

_Applies to US-registered ABS and, subject to the EGRRCPA CLO exemption, CLOs._

| Requirement                                             | Provision             | Compliant? | Issue |
| ------------------------------------------------------- | --------------------- | ---------- | ----- |
| 5% net economic interest retained by sponsor            | § 246.4               |            |       |
| Retention form: eligible vertical interest              | § 246.4(a)            |            |       |
| Retention form: eligible horizontal residual interest   | § 246.4(b)            |            |       |
| Retention form: combination (V + H totaling ≥ 5%)       | § 246.4(c)            |            |       |
| CMBS third-party purchaser (B-piece) exemption          | § 246.7               |            |       |
| Open market CLO exemption (EGRRCPA § 214)               | 15 U.S.C. § 78o-11(f) |            |       |
| Foreign transaction safe harbor (≤ 10% US persons)      | § 246.20              |            |       |
| Prohibition on hedging / transferring retained interest | § 246.12              |            |       |
| Lock-up period for third-party purchaser (CMBS)         | § 246.7(b)(8) (5 yrs) |            |       |

**Open market CLO exemption requirements** (if claimed):

- [ ] CLO consists of syndicated leveraged loans only (no ABS interests)
- [ ] No loan originated specifically for the CLO
- [ ] CLO manager qualifies as QPAM or equivalent
- [ ] No single loan ≥ 10% of CLO at closing

Flag as **CRITICAL** if risk retention obligations are not met and no exemption applies —
non-compliance results in significant penalties and reputational risk.

### Step 9: Rating Agency Requirements and Legal Opinions Review

Confirm that all materials required by rating agencies are present and adequate.

#### 9a. Required Legal Opinions Checklist

| Opinion                                     | Counsel                        | Level ("Should"/"Would"/"Could") | Received? | Issue |
| ------------------------------------------- | ------------------------------ | -------------------------------- | --------- | ----- |
| True sale (US)                              | [Originator's / SPV's counsel] | "Should" minimum [VERIFY]        |           |       |
| Non-consolidation (US)                      | [SPV's counsel]                | Typically "reasoned should"      |           |       |
| Enforceability / validity                   | [Transaction counsel]          | "Should"                         |           |       |
| Security interest perfection (US)           | [Transaction counsel]          | "Should"                         |           |       |
| Tax opinion (pass-through / no withholding) | [Tax counsel]                  | "Should"                         |           |       |
| True sale (UK) — if English law assets      | [English law counsel]          | "Should"                         |           |       |
| English law enforceability                  | [English law counsel]          | "Should"                         |           |       |
| Cayman/Jersey corporate authority           | [Offshore counsel]             | "Should"                         |           |       |

**True sale opinion review** — for any obtained opinion, confirm:

- Opinion addresses recharacterization factors specifically, not just UCC perfection
- Opinion identifies and analyzes the key risk factors (recourse, control, risk allocation)
- Assumptions are reasonable and within the control of transaction parties
- No material qualifications or carve-outs that undercut the opinion's utility

**Non-consolidation opinion review** — confirm:

- Opinion applies the correct test for the relevant circuit (2d Cir. _Augie/Restivo_
  or 3d Cir. _Owens Corning_) or is written to satisfy both [VERIFY]
- Opinion relies on representations about actual separateness practices
- Opinion identifies breach of separateness covenants as a risk factor that would
  undermine the opinion — confirm ongoing monitoring mechanisms are in place

#### 9b. Rating Agency Communication

- Identify which rating agencies have been engaged
- Confirm pre-sale reports have been reviewed for accuracy of structural description
- Flag any rating agency conditions or open items not yet resolved prior to closing

**⟁ CLARIFY** — If any required legal opinion is absent, or if an opinion is only at
"could" or "may" level, ask whether the missing opinion is being prepared, whether the
rating agency has been notified of the limitation, and whether the transaction should
proceed without it.

### Step 10: Quality Verification and Output

Before delivering the analysis:

1. Run the **5 Citation Quality Gates** silently. Revise failures before delivery.
2. For every **CRITICAL** finding, run the **3-Pass Self-Interrogation**.
3. Assign a **Confidence Score** to each material analytical finding.
4. Verify completeness: confirm all workflow steps were addressed (or noted as not
   applicable with a reason).
5. Generate the **Glass Box Audit Trail** and append to output.
6. Deliver the output in the **Output Format Template** below.

---

## Deep Topic Analysis Reference

### Structuring Norms by Transaction Type

Use these benchmarks when assessing whether a transaction's structure deviates materially
from market norms:

| Metric                        | CLO (Arbitrage)                                    | Auto ABS          | RMBS (Private Label) | CMBS                   |
| ----------------------------- | -------------------------------------------------- | ----------------- | -------------------- | ---------------------- |
| **Senior tranche (AAA) size** | 60-65%                                             | 85-92%            | 80-90%               | 70-80%                 |
| **Equity / first-loss**       | 8-12%                                              | 0-3%              | 2-5%                 | 5-10% (B-piece)        |
| **Reinvestment period**       | 3-5 years                                          | N/A (static)      | N/A (static)         | N/A (static)           |
| **Management fees**           | 0.15-0.50% p.a. (senior) + sub                     | N/A               | N/A                  | N/A                    |
| **OC trigger (AAA level)**    | ~115-125%                                          | N/A               | N/A                  | N/A                    |
| **IC trigger (AAA level)**    | ~110-120%                                          | N/A               | N/A                  | N/A                    |
| **True sale opinion level**   | "Should" [VERIFY]                                  | "Should"          | "Should"             | "Would" preferred      |
| **Non-con opinion level**     | Reasoned "should"                                  | Reasoned "should" | Reasoned "should"    | Reasoned "should"      |
| **Backup servicer**           | Not typical pre-2008; now market practice [VERIFY] | Required (hot)    | Required (warm)      | Required (warm/hot)    |
| **Clean-up call**             | 10% par / non-call period                          | 10% par           | 10% par              | 20-30% (optional call) |
| **Rating agency(ies)**        | S&P, Moody's (both common)                         | All three         | All three            | All three              |

### Key CLO Indenture Provisions

When reviewing a CLO indenture, pay particular attention to:

1. **Eligibility Criteria**: Requirements that each loan must satisfy at purchase.
   Confirm: maximum size limit; minimum rating; industry concentration limits (GICS
   or NAICS); obligor concentration (typically ≤ 2-3%); maximum CCC bucket (typically
   7.5%); no DIP / PIK-only / zero-coupon restrictions; floating rate requirement
   (basis swap risk if fixed-rate loans included); term vs. revolving facility.

2. **Coverage Tests**: Confirm the OC and IC test methodology, calculation date, and
   the consequence of failure. Key: does a CCC haircut apply (i.e., CCC-rated loans
   valued at lower of market or par in OC numerator)? Rating agencies require this.

3. **Manager Discretion vs. Manager Constraints**: Balance between manager flexibility
   (to reinvest, buy/sell loans) and covenant limits (eligibility criteria, concentration
   limits, WAL test, WAS test, WARF test). Overly broad manager discretion with no
   portfolio quality tests is a RED flag.

4. **Reinvestment Period End**: Confirm the exact end date; confirm that post-reinvestment-
   period principal proceeds flow to repay notes sequentially.

5. **Manager Removal**: What triggers removal of the CLO manager? (For-cause removal is
   standard; no-cause removal by equity holders raises conflicts-of-interest concerns.)
   Confirm the successor manager appointment process.

6. **Equityholder Control**: Confirm that equity holders (preference shareholder/income
   note holders) cannot direct the trustee to take actions contrary to senior noteholder
   interests during a coverage test failure or event of default.

### Key Servicer Provisions to Review

| Provision                    | Market Standard                                           | Red Flag                                               |
| ---------------------------- | --------------------------------------------------------- | ------------------------------------------------------ |
| Collection account structure | Dedicated lockbox in SPV/Trustee name                     | Collections in servicer's name; no trust annotation    |
| Transfer timing              | Daily sweep (ideally T+0 or T+1)                          | Weekly or monthly transfer; 5+ business day timing     |
| Backup servicer              | Named warm backup servicer in documents at closing        | No backup named; cold backup only or "best efforts"    |
| Servicer advance obligation  | Limited to amounts recoverable from future collections    | Unlimited advance obligation (unsecured claim risk)    |
| Servicer replacement trigger | Rating downgrade below BB / insolvency                    | No downgrade trigger; voluntary replacement only       |
| Commingling protection       | Structural daily sweep + rating trigger + backup servicer | No protection; originator sole servicer with no backup |

---

## Severity Classification

All findings are classified on a four-tier scale:

| Tier            | Label               | Meaning                                                                                                                           | Action Required                                                             |
| --------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| ✅ **GREEN**    | No issue            | Structure is sound; meets market standard and regulatory requirement                                                              | Note for awareness                                                          |
| 🟡 **YELLOW**   | Flag                | Issue that is manageable or already partially addressed but warrants attention                                                    | Recommend specific remedy; estimate residual risk                           |
| 🔴 **RED**      | Material deficiency | Significant structural or regulatory deficiency; material risk to investors, originator, or ratings                               | Must be addressed before closing (or disclosed prominently if post-closing) |
| 🚨 **CRITICAL** | Deal-stopper        | Issue that, if unaddressed, would prevent the transaction from closing, trigger acceleration, or result in regulatory enforcement | Immediate escalation; no acceptable workaround without structural change    |

**Automatic CRITICAL Triggers** — Classify as CRITICAL regardless of context:

| Trigger                                                                                        | Basis                                      |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------ |
| No true sale opinion obtained and recharacterization risk is material                          | Rating agency requirement; bankruptcy risk |
| No UCC-1 financing statement filed (US)                                                        | Assets not legally perfected in SPV        |
| Non-petition covenant absent or insufficient (<1yr + 1day)                                     | SPV not bankruptcy-remote                  |
| No independent director / manager with bankruptcy consent right                                | SPV not bankruptcy-remote                  |
| Risk retention obligation applies but not satisfied and no exemption applies                   | Dodd-Frank / EUSR violation                |
| Waterfall allows equity distribution before coverage tests are satisfied                       | Senior investor loss; rating deficiency    |
| Swap counterparty below minimum required rating with no replacement obligation                 | Loss of hedge; payment shortfall risk      |
| Material misstatement in registered OM regarding deal structure                                | Securities law violation                   |
| STS designation claimed but material STS criterion is not met                                  | EUSR Art. 27 liability for false STS claim |
| Servicer collections held in servicer's name with no daily sweep and no commingling protection | Servicer insolvency credit exposure        |

---

## Actionable Output Per Finding

For each identified issue, provide:

**For YELLOW / RED issues:**

1. **Precise identification**: The specific document, clause, or absence at issue
2. **Risk statement**: The legal or operational risk created by the issue
3. **Market standard**: What the market standard or regulatory requirement is for this item
4. **Recommended remedy**: A specific, actionable fix (re-draft the clause, obtain missing
   opinion, restructure the mechanism)
5. **If post-closing**: The available mitigation options (disclosure, amendment, waiver)

**For CRITICAL issues:**

1. **Precise identification**: Document, clause, or absence
2. **Risk chain**: Full legal consequence (e.g., recharacterization → assets remain in
   originator estate → investors lose SPV protections → acceleration likely on originator
   insolvency)
3. **Required resolution**: The only acceptable remediation pathway
4. **Timeline**: Whether this can be resolved pre-closing or requires structural change
5. **Escalation**: Who needs to be notified (rating agencies, regulators, senior counsel)

**Redline language**: For documentary deficiencies (missing or inadequate clause), provide
draft replacement language that can be inserted or negotiated. Frame language as:

- _Original_: [quote or describe existing inadequate language]
- _Proposed_: [revised language meeting market standard]
- _Explanation_: [why the change is needed]

---

## Prioritization Framework

Organize findings into three tiers for efficient remediation:

**Tier 1 — Pre-Closing (Must resolve before transaction closes):**

- All CRITICAL findings
- RED findings that rating agencies or regulators require to be resolved pre-closing
- Missing required legal opinions
- Unmet regulatory obligations (risk retention, STS criteria, Reg AB II requirements)

**Tier 2 — Closing Conditions / Immediate Post-Closing (Address within 30-90 days):**

- RED findings addressable by amendment or supplemental agreement
- Missing or inadequate backup servicer arrangements
- Disclosure deficiencies that can be corrected by prospectus supplement
- Ongoing compliance obligations that need to be set up (e.g., ESMA repository registration)

**Tier 3 — Ongoing Monitoring (Address in lifecycle management):**

- YELLOW findings representing market non-standard terms that are not immediately harmful
- OC/IC test monitoring procedures
- Swap counterparty rating monitoring
- Servicer performance triggers
- Annual Reg AB II certification process setup

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                                          | Fail Action                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established principle                                                                              | Add citation or mark "[UNVERIFIED]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction (e.g., 17 CFR 246.4; EUSR Art. 6(3)(b); LPA 1925 s.136)                           | Fix format                          |
| **Currency**   | Every cited provision checked for amendments or repeal (especially post-2022 in structured finance, which saw significant US, UK, and EU regulatory activity) | Flag "[CHECK CURRENCY]"             |
| **Domain**     | Analysis stays within the stated jurisdiction scope; no bleeding of US law concepts into EU analysis or vice versa                                            | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty is explicitly stated, not hidden (e.g., areas where courts have not definitively ruled, where ESMA guidance is pending)                           | Add confidence qualifier            |

---

## Self-Interrogation for Critical Findings

For every **CRITICAL** finding, apply this 3-pass review before delivery:

**Pass 1 — Legal Chain Integrity**: Does the risk chain follow logically from the
statutory or case law basis? Is the claimed consequence (e.g., "assets remain in
originator's estate") actually what would happen under the applicable law, or is that
an oversimplification? Would a bankruptcy court or regulator actually reach this
conclusion on these facts?

**Pass 2 — Completeness**: Have all relevant mitigants been considered? Does the deal
have any structural feature that might partially address the risk even if the primary
mechanism is deficient? Are there regulatory safe harbors or carve-outs that might apply?

**Pass 3 — Challenge**: What is the strongest argument that this is not actually a
CRITICAL issue? Under what circumstances would a reasonable structured finance lawyer
conclude this risk is acceptable? Is the "market standard" being applied actually market
standard, or is it an aggressive interpretation?

---

## Confidence Scoring

Assign a confidence score to each material analytical finding:

| Level        | Range     | Meaning                                                                                             | Action                                                              |
| ------------ | --------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Statutory or regulatory requirement is clear and unambiguous; case law is settled                   | State with confidence                                               |
| **High**     | 0.80–0.94 | Strong authority, well-established market practice; minor interpretive questions                    | State with brief caveat                                             |
| **Probable** | 0.60–0.79 | Good arguments support the conclusion, but outcome is not certain; agency interpretation may differ | State with reasoning and contra-indicators                          |
| **Possible** | 0.40–0.59 | Genuinely contested area; reasonable practitioners disagree                                         | Flag for qualified legal review with both sides stated              |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                                                                             | Do not assert; flag "[UNCERTAIN — qualified legal review required]" |

---

## Glass Box Audit Trail

Append this completed YAML block to every output:

```yaml
glass_box:
  skill_name: "legalcode-structured-finance-review"
  mode: "Transaction review"
  review_date: "[ISO date]"
  transaction_type: "[ABS / MBS / CLO / CMBS / RMBS / Other]"
  asset_class: "[Auto loans / Leveraged loans / Residential mortgages / etc.]"
  applicable_jurisdictions: "[US / EU / UK / combination]"
  review_scope: "[Full / True sale only / Regulatory compliance only / Other]"
  user_perspective: "[Originator / Investor / Underwriter / Other]"
  documents_reviewed:
    - "[Document name and version]"
  documents_requested_not_received:
    - "[Document name — reason not reviewed]"
  legalcode_mcp: "Connected / Not connected"
  citations_verified: "[N VERIFIED] / [N unverified, marked [VERIFY]]"
  critical_findings: "[count]"
  red_findings: "[count]"
  yellow_findings: "[count]"
  green_findings: "[count]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Scope limitations, documents not reviewed, jurisdiction analysis not performed]"
    - "[Regulatory regime may have changed since knowledge cutoff — verify citations]"
  quality_checks_run:
    - "Citation Quality Gates: [PASS / N gates failed and revised]"
    - "Self-Interrogation: [N CRITICAL findings reviewed across 3 passes]"
    - "Confidence scoring: [Applied to N material findings]"
  disclaimer: "AI-assisted analysis — requires review by qualified structured finance counsel"
```

---

## Anti-Patterns

**What NOT to do when reviewing or structuring securitization transactions:**

1. **Conflating UCC-1 filing with true sale**: Filing a UCC-1 financing statement (required
   even for true sales of accounts under Article 9) does not by itself establish true sale
   treatment. Recharacterization analysis is separate from perfection analysis.

2. **Relying solely on transaction document labels**: A document labeled "Purchase and
   Sale Agreement" does not create a true sale. Courts and regulators apply substance-over-
   form analysis regardless of how the parties characterized the transaction.

3. **Assuming EU SSPE = US bankruptcy-remote SPV**: The EUSR defines an "SSPE" (Special
   Purpose Securitisation Entity) in Article 2(2), but SSPE status does not automatically
   provide US-style bankruptcy remoteness. The applicable insolvency analysis is governed
   by national law, not the EUSR.

4. **Treating EU and UK regimes as identical post-Brexit**: Since 1 January 2021, the UK
   has developed its own securitisation regulatory framework. As of 1 November 2024, the
   UK Securitisation Regulations 2024 (SI 2024) apply, replacing the onshored EU
   Securitisation Regulation. Key differences in templates, supervision, and STS
   recognition are evolving. [VERIFY current UK/EU divergences]

5. **Overlooking the EUSR's extraterritorial reach**: EU institutional investors are
   subject to EUSR Article 5 due diligence obligations regardless of whether the issuer
   is incorporated in an EU member state. A Cayman CLO with EU investors must satisfy
   EUSR requirements from the investor-side even if the CLO itself is a US-law transaction.

6. **Ignoring set-off risk in assignment jurisdictions**: Many civil law jurisdictions
   allow obligors to set off claims arising before notice of assignment, even against a
   third-party assignee. This can materially impair receivables pools in European ABS.
   Always assess set-off risk under the obligors' governing law, not only the
   transaction's governing law.

7. **Treating CLO open-market exemption as self-executing**: The EGRRCPA CLO exemption
   from US risk retention is available only if the CLO meets specific conditions (no ABS
   collateral, no origination for the CLO, loans traded in secondary market, manager
   QPAM status). Relying on this exemption without confirming all conditions creates
   regulatory risk.

8. **Underestimating servicer commingling risk**: Servicer failure and commingling is
   the most common cause of investor loss in ABS transactions. A transaction with monthly
   collection transfers, no backup servicer, and collections held in the servicer's name
   is structurally weak regardless of how clean the true sale analysis is.

9. **Assuming the non-consolidation opinion remains valid throughout the transaction**:
   A non-consolidation opinion delivered at closing relies on the SPV actually maintaining
   separateness during the life of the transaction. Commingling, failure to observe
   corporate formalities, or common management between originator and SPV can undermine
   the factual basis of the opinion, even though the opinion was delivered.

10. **Accepting a "could" or "may" level true sale opinion**: Rating agencies generally
    require a "would" or "should" level true sale opinion for investment-grade ratings.
    A "could" opinion signals meaningful recharacterization risk that rating agencies,
    investors, and regulators will treat as a structural weakness.

11. **Failing to review the OC/IC test definitions alongside the coverage tests**: The
    coverage tests in a CLO indenture are only as strong as their definitions. A high OC
    ratio threshold is meaningless if the definition of "Aggregate Par Amount" in the
    numerator excludes CCC haircuts, allows distressed purchases at par, or counts non-
    performing loans without discount.

12. **Missing the "waterfall timing" issue**: Some waterfalls allow subordinated fee
    payments before coverage tests on a given payment date — a potential violation of
    the priority of payments principle that can erode credit enhancement.

13. **Overlooking the swap mark-to-market risk at termination**: On early termination of
    an interest rate or FX swap (e.g., due to counterparty downgrade, transaction
    acceleration, or event of default), the swap termination payment may be owed _by_ the
    SPV to the counterparty. This creates a senior unsecured claim in the waterfall. Confirm
    the ranking of swap termination payments — they should be junior to rated notes.

14. **Failing to assess B-piece buyer exemption conditions for CMBS**: The CMBS B-piece
    exemption under 17 CFR 246.7 requires, among other conditions, a cash purchase with
    no financing from transaction parties and a 5-year lock-up. If these conditions are
    not met, the exemption is unavailable and the sponsor bears full 5% retention.

15. **Treating STS self-certification as a low-risk formality**: Originator/sponsors that
    claim STS status are personally responsible for accuracy (EUSR Article 27). A false or
    misleading STS notification exposes the notifying party to significant regulatory
    sanctions and investor claims. The notification must be legally reviewed, not just
    operationally checked.

16. **Ignoring the reinvestment period end date in CLO analysis**: The end of the CLO
    reinvestment period is a significant structural event. After this date, principal
    proceeds must be applied sequentially to repay notes. Failure to properly document or
    enforce the reinvestment period end can give the CLO manager unauthorized investment
    discretion at the expense of noteholders.

17. **Assuming all required legal opinions were obtained**: It is surprisingly common in
    secondary market due diligence to discover that a closing opinion was never delivered,
    was delivered in an inadequate form, or was based on assumptions that were later
    breached. Always request and review the actual opinions, not just a closing checklist.

---

## Writing Standards

Before delivering any output:

1. **Clarity over jargon**: Define technical terms (OC test, WARF, CCC haircut, Cession
   Dailly, etc.) the first time they appear in the output.

2. **Cite precisely**: Every legal rule, standard, or market practice should be cited
   with a specific reference (statute section, regulation provision, regulatory guidance
   title). Avoid vague references like "applicable law requires..."

3. **Separate finding from severity from recommendation**: Each finding has three distinct
   parts — what the issue is (fact), why it matters (risk), what to do about it (remedy).
   Do not blend these together.

4. **Quantify where possible**: "The OC test for the Class A notes is set at 108%, compared
   to a typical market range of 115-125% for this asset class" is more useful than
   "the OC test appears low."

5. **Flag uncertainty explicitly**: Use "[VERIFY]" for any legal citation that has not
   been confirmed against a current authoritative source. Use "[UNCERTAIN]" for areas
   where the legal outcome is genuinely indeterminate.

6. **No false precision**: Do not assert "this structure complies with EUSR Article 6"
   without having actually verified each element. Use confidence qualifiers that accurately
   reflect the basis for the conclusion.

7. **Plain language for risk escalation**: When a CRITICAL finding requires escalation to
   business decision-makers, state the issue and consequence in plain language before
   the technical detail.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 4, search for current text of 17 CFR Part 246, EUSR Reg. 2017/2402, UK
  Securitisation Regulations 2024, and relevant case law
- Save the most relevant results to `/tmp/legalcode-structured-finance-authority.md`
- Use verified authority to support true sale analysis, bankruptcy remoteness assessment,
  and regulatory compliance checklist
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail
- Run regulatory amendments search for: (a) any SEC updates to Regulation AB II or
  17 CFR Part 246; (b) EUSR amending regulations; (c) UK SECN updates post-November 2024

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — all citations require manual verification"`
- Focus the review on structural quality, document completeness, and identification of
  potential issues, rather than making definitive regulatory compliance conclusions
- Provide the regulatory compliance checklists but note that all items marked with [VERIFY]
  must be confirmed against current regulatory text before any opinion or advice is given

---

## Output Format Template

Deliver the structured finance review in this format:

---

# Structured Finance Review: [Transaction Name / Reference]

> **Disclaimer**: This is an AI-assisted analysis. It does not constitute legal advice.
> All findings must be reviewed by qualified structured finance counsel before any action
> is taken. All citations marked [VERIFY] have not been confirmed against current
> authoritative sources.

## Transaction Summary

**Transaction type**: [ABS / CLO / MBS / CMBS / Other]
**Asset class**: [Auto loans / Leveraged loans / etc.]
**Issuer / SPV**: [Name and jurisdiction of incorporation]
**Originator / Seller**: [Name]
**Key transaction parties**: [Servicer, Trustee, CLO Manager, Swap Counterparty]
**Note tranches**: [Summary table: Class, Rating, Amount, Rate, Legal Final Maturity]
**Applicable regulatory regimes**: [Reg AB II / EUSR / UK SECN / None]
**Documents reviewed**: [List]
**Documents requested but not received**: [List]
**Review scope**: [Full / Scoped]
**User perspective**: [Originator / Investor / Underwriter / Other]
**Assumptions**: [Any assumptions made due to missing context]

---

## Executive Summary

**Overall assessment**: [GREEN / YELLOW / RED / CRITICAL]
**Critical findings**: [Count] — [one-line summary of each]
**Red findings**: [Count] — [brief description]
**Yellow findings**: [Count]

**Top 3 priority items**:

1. [Most critical issue — one-sentence summary, Tier 1]
2. [Second most critical — one-sentence summary, Tier 1 or 2]
3. [Third — one-sentence summary, Tier 2]

**Recommended immediate actions**: [3-5 bullet points]

---

## True Sale Analysis

### Jurisdiction: [US / UK / EU — specify which apply]

**Overall recharacterization risk**: LOW / MEDIUM / HIGH

| Factor                                                  | Finding      | Severity                    |
| ------------------------------------------------------- | ------------ | --------------------------- |
| Recourse                                                | [Assessment] | [GREEN/YELLOW/RED]          |
| Control of assets                                       | [Assessment] | [GREEN/YELLOW/RED]          |
| Risk of loss                                            | [Assessment] | [GREEN/YELLOW/RED]          |
| Economic upside                                         | [Assessment] | [GREEN/YELLOW/RED]          |
| Documentation and opinions                              | [Assessment] | [GREEN/YELLOW/RED]          |
| Accounting treatment                                    | [Assessment] | [GREEN/YELLOW/RED]          |
| UCC perfection (US) / LPA notice / Companies Act filing | [Assessment] | [GREEN/YELLOW/RED/CRITICAL] |

**True sale opinion**: [Present / Absent / Inadequate] — [Opinion level: "Should" / "Could" / Other]
**Key risks**: [Summary of most material recharacterization risks]
**Recommended remedies**: [Specific actions]

---

## Bankruptcy Remoteness Analysis

**Overall assessment**: [SOUND / CONCERNS IDENTIFIED / DEFICIENT]

### SPV Structural Elements

| Element                              | Status  | Severity | Notes |
| ------------------------------------ | ------- | -------- | ----- |
| Single-purpose restriction           | ✅ / ❌ |          |       |
| Non-petition covenant (≥ 1yr + 1day) | ✅ / ❌ |          |       |
| Independent director / manager       | ✅ / ❌ |          |       |
| Separateness covenants               | ✅ / ❌ |          |       |
| No commingling covenant              | ✅ / ❌ |          |       |
| Adequate capitalization              | ✅ / ❌ |          |       |

**Non-consolidation opinion**: [Present / Absent / Inadequate]
**Key risks**: [Summary]
**Recommended remedies**: [Specific actions]

---

## Credit Enhancement and Waterfall Review

### Credit Enhancement Summary

| Form              | Level / Amount         | Assessment       | Issue |
| ----------------- | ---------------------- | ---------------- | ----- |
| OC (Class [X])    | [%]                    | GREEN/YELLOW/RED |       |
| Subordination     | [%]                    | GREEN/YELLOW/RED |       |
| Reserve fund      | [$]                    | GREEN/YELLOW/RED |       |
| Swap counterparty | [Counterparty, rating] | GREEN/YELLOW/RED |       |

### OC / IC Test Analysis

**OC tests**: [Pass / Fail / Not Tested] — [Levels vs. market norms]
**IC tests**: [Pass / Fail / Not Tested]
**CCC haircut provision**: [Present / Absent]
**Sequential pay trigger**: [Adequately defined / Concerns]

### Waterfall Mechanics

**Interest waterfall**: [Sound / Issues identified]
**Principal waterfall**: [Sequential / Pro-rata / Other] — [Sound / Issues identified]
**Equity distribution controls**: [Adequate / Insufficient — detail]
**Key issues**: [List any waterfall deficiencies]

---

## Regulatory Compliance

### US Regulation AB II (if applicable)

**Applicability**: [Registered public ABS / Rule 144A / Not applicable]
**CEO/CFO certification**: [Present / Absent / Inadequate]
**ABS-EE asset-level data**: [Compliant / Non-compliant / Not required]
**Key gaps**: [List]

### EU Securitisation Regulation (EUSR)

**Applicability**: [EU investors / Not applicable]
**Risk retention compliance (Art. 6)**: [COMPLIANT / PARTIAL / NON-COMPLIANT / NOT VERIFIED]

- Method: [Vertical / Horizontal / Other]
- Retaining entity: [Originator / Sponsor / Original lender]
  **Transparency compliance (Art. 7)**: [COMPLIANT / PARTIAL / NON-COMPLIANT / NOT VERIFIED]
  **STS designation**: [Claimed / Not claimed]
- STS criteria: [COMPLIANT / [N] items require verification]

### UK Securitisation Regulations 2024 (if applicable)

**Applicability**: [UK investors / Not applicable]
**Compliance assessment**: [COMPLIANT / PARTIAL / NON-COMPLIANT / NOT VERIFIED] [VERIFY]
**Key divergences from EUSR**: [List any identified]

### US Risk Retention (17 CFR Part 246)

**Applicability**: [Yes — no exemption / Open market CLO exemption claimed / CMBS B-piece exemption claimed / Not applicable]
**Compliance assessment**: [COMPLIANT / NON-COMPLIANT / EXEMPTION NOT VERIFIED]
**Key issues**: [List]

---

## Rating Agency Requirements

### Legal Opinions

| Opinion           | Status           | Level                    | Issue |
| ----------------- | ---------------- | ------------------------ | ----- |
| True sale (US)    | Present / Absent | "Should" / "Could" / N/A |       |
| Non-consolidation | Present / Absent | Reasoned "should" / N/A  |       |
| Enforceability    | Present / Absent | "Should"                 |       |
| Perfection        | Present / Absent | "Should"                 |       |
| Tax               | Present / Absent | "Should"                 |       |

**Missing opinions**: [List any absent opinions that are required]
**Opinion quality concerns**: [Any qualifications or inadequate opinion levels]

---

## Detailed Findings

### Critical Findings

#### CRITICAL-1: [Short Title]

**Issue**: [Precise description of the issue]
**Location**: [Document, clause, or section]
**Risk chain**: [Legal consequence chain]
**Required resolution**: [Specific remediation required]
**Timeline**: [Pre-closing required / Can be addressed post-closing by amendment]
**Confidence**: [Level] ([rationale])

### Red Findings

#### RED-1: [Short Title]

**Issue**: [Description]
**Location**: [Document / clause]
**Risk**: [Specific risk]
**Market standard**: [What market standard / regulatory requirement provides]
**Recommended remedy**: [Specific action]
**Confidence**: [Level]

[Repeat for each RED finding]

### Yellow Findings

[Tabular format for efficiency:]

| #   | Issue | Location | Market Standard | Recommended Remedy | Confidence |
| --- | ----- | -------- | --------------- | ------------------ | ---------- |
| Y-1 |       |          |                 |                    |            |
| Y-2 |       |          |                 |                    |            |

---

## Prioritized Remediation Plan

### Tier 1 — Pre-Closing (Required before transaction closes)

- [ ] [CRITICAL / RED finding — specific action]
- [ ] [...]

### Tier 2 — Post-Closing / Closing Condition (Within 30-90 days)

- [ ] [RED / YELLOW finding — specific action]
- [ ] [...]

### Tier 3 — Ongoing Monitoring

- [ ] [Monitoring obligation — frequency and responsible party]
- [ ] [...]

---

## Localization Notes

_[Include only for jurisdictions identified as applicable in Step 2.]_

---

[Glass Box Audit Trail YAML here]

---

_This review was produced using the legalcode-structured-finance-review skill. Review
date: [date]. All [VERIFY] markers indicate citations that have not been confirmed against
current authoritative sources and require manual verification before reliance._

---

## Localization Notes

### US-Specific

- **Delaware SPV**: Most US securitizations use Delaware LLCs or Delaware statutory trusts.
  Delaware courts generally enforce contractual restrictions on voluntary bankruptcy filings
  and independent director provisions. [VERIFY current Delaware case law]
- **New York trust**: A common law trust established under New York law cannot file for
  bankruptcy under Chapter 11 (Bankruptcy Code defines eligible debtors by reference to
  "persons" — a common law trust is generally not a "person" for this purpose). [VERIFY]
- **Cayman/offshore SPV with US assets**: While the SPV may be offshore, the true sale and
  perfection analysis for US assets follows US law. A Cayman SPV holding US receivables still
  requires UCC-1 filings in the US against the US originator.
- **SOFR transition**: As of June 2023, LIBOR is largely discontinued. CLOs and ABS issued
  before 2023 may still reference the Adjustable Interest Rate (LIBOR) Act (Pub. L. 117-103, 2022) for fallback rate provisions. New transactions should use SOFR; verify benchmark
  language in any legacy transaction being reviewed.

### EU-Specific

- **SSPE requirements**: EUSR Article 2(2) defines an SSPE. Confirm that the transaction
  entity qualifies; non-qualifying SPVs cannot issue STS securitisations.
- **Sovereign CRR treatment**: For EU bank investors, ABS and STS securitizations receive
  different capital treatment under the Capital Requirements Regulation (CRR II, Reg.
  2017/2401). Investors may require STS status as a condition of purchase for capital
  efficiency reasons.
- **DORA interaction**: EU financial entities investing in ABS are subject to DORA (Reg.
  2022/2554) ICT risk management requirements, which may require specific contractual
  provisions in service agreements. [VERIFY DORA applicability to ABS investors]

### UK-Specific

- **Post-Brexit divergence**: Monitor FCA publications for updates to the UK Securitisation
  Sourcebook (SECN). The UK is developing its own STS criteria and transparency templates
  that may diverge from EUSR going forward. [VERIFY current SECN provisions]
- **UK CRR (PRA/FCA rules)**: UK bank investors apply UK CRR capital rules to their ABS
  holdings, not the EU CRR. UK STS status (under the UK regime) may be required for
  UK CRR preferential capital treatment.
- **Financial collateral**: UK Financial Collateral Arrangements (No.2) Regulations 2003
  (SI 2003/3226) provide enhanced enforceability for financial collateral over certain
  securities accounts and cash. Confirm whether FCARs apply to the collateral arrangements
  in the transaction.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis from:

- Deep legal research across US securitization law (UCC Article 9, Bankruptcy Code, 17 CFR
  Part 246, Regulation AB II), EU securitisation law (EUSR Reg. 2017/2402, ESMA RTS), and
  UK securitisation law (UK Securitisation Regulations 2024, FCA SECN)
- Structured finance case law analysis (_In re LTV Steel_, _In re Augie/Restivo_, _In re
  Owens Corning_, _Welsh Development Agency v Export Finance Co_, _Major's Furniture Mart
  v Castle Credit Corp_, _In re General Growth Properties_)
- SIFMA capital markets data and structured finance market practice research (2024-2025)
- Repository patterns from `legalcode-contract-review` (quality frameworks, Glass Box,
  anti-patterns) and `legalcode-security-collateral-review` (UCC Article 9 analysis,
  CRITICAL trigger framework)
- Structured finance and securitization industry standards from S&P Global, Moody's,
  and Fitch rating methodologies

Attribution: Legalcode original synthesis. Not derived from any external skill.
