---
name: legalcode-venture-financing-sg
description: 'Singapore venture financing advisor covering the full early-stage investment lifecycle under
  Singapore law: CARE agreements and VIMA 2.0 (February 2025) document suite, Series A term sheet analysis
  against SVCA/SAL market standards, convertible note review, VCFM fund manager licensing (post-RFMC repeal
  August 2024), Section 13O/13OA/13U/13H fund tax incentive qualification (January 2025 revamp), Variable
  Capital Company (VCC) fund structuring, Singapore Pte Ltd formation for startups, and ASEAN cross-border
  DTA and regulatory considerations. Use when reviewing or drafting CARE notes, convertible notes, VIMA
  term sheets, shareholders'' agreements, or subscription agreements under Singapore law; when advising
  on VCFM licence applications or compliance; when assessing fund tax incentive eligibility; when structuring
  a Singapore VC fund (VCC vs LP vs Pte Ltd); or when advising founders on Singapore company formation
  and ASEAN expansion structuring.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Singapore venture financing advisor covering the full early-stage investment lifecycle under Singapore law: CARE agreements and VIMA 2.0 (February 2025) document suite, Series A term sheet analysis against SVCA/SAL market standards, convertible note review, VCFM fund manager licensing (post-RFMC repeal August 2024), Section 13O/13OA/13U/13H fund tax incentive qualification (January 2025 revamp), Variable Capital Company (VCC) fund structuring, Singapore Pte Ltd formation for startups, and ASEAN cross-border DTA and regulatory considerations. Use when reviewing or drafting CARE notes, convertible notes, VIMA term sheets, shareholders' agreements, or subscription agreements under Singapore law; when advising on VCFM licence applications or compliance; when assessing fund tax incentive eligibility; when structuring a Singapore VC fund (VCC vs LP vs Pte Ltd); or when advising founders on Singapore company formation and ASEAN expansion structuring. Also use when the user mentions: VIMA, SAL, SVCA, MAS VCFM, Section 13H, Section 13O, Section 13OA, Section 13U, VCC Act, CARE note, Singapore SAFE, SFA fund manager, Singapore startup equity round, ASEAN VC deal structure, or pre-Series A Singapore.


# Legalcode — Singapore Venture Financing

> **Disclaimer**: This skill provides a framework for AI-assisted legal analysis of Singapore
> venture financing transactions. It does not constitute legal advice. All outputs should be
> reviewed by a qualified Singapore-admitted advocate and solicitor before use. Singapore law
> changes frequently — verify all statutory references, regulatory thresholds, and tax
> conditions against current MAS, IRAS, ACRA, and EDB guidance before relying on them.
> Statutory and regulatory references cited from memory carry hallucination risk — verify
> against authoritative sources before use.

---

## Purpose and Scope

This skill advises on the full spectrum of early-stage venture financing activity in Singapore,
from pre-seed company formation through Series A documentation and fund structuring.

**Covers:**

- CARE (Convertible Agreement Regarding Equity) agreement review and drafting guidance (VIMA 2.0, Feb 2025)
- Convertible note review and CARE vs. convertible note selection analysis
- Series A term sheet analysis against VIMA 2.0 / SVCA market standards
- Shareholders' agreement and subscription agreement key provisions review
- VCFM (Venture Capital Fund Manager) simplified licensing regime (post-RFMC repeal)
- Fund tax incentive qualification: Sections 13O, 13OA, 13U, and 13H of the Income Tax Act
- Variable Capital Company (VCC) fund structure analysis and formation requirements
- Singapore Pte Ltd formation requirements and foreign founder structuring
- ASEAN cross-border DTA strategy and portfolio company jurisdiction considerations
- ESG provisions under VIMA 2.0 ESG Letter Agreement

**Does not:**

- Provide legal advice or replace Singapore-admitted counsel
- Cover public market fundraising (IPOs, listed company rights issues)
- Cover venture debt or bank lending facilities
- Apply outside Singapore (except for ASEAN cross-border analysis under Track E)
- Draft final legal documents — provides analysis, issue identification, and recommended positions

---

## Jurisdiction and Governing Law

**Primary jurisdiction**: Republic of Singapore

**Legal system**: Common law (inherited from English law via Reception of English Law Act),
supplemented by extensive Singapore-specific legislation and MAS regulatory framework.

**Key governing statutes:**

| Statute                                    | Abbreviation | Relevance                                                 |
| ------------------------------------------ | ------------ | --------------------------------------------------------- |
| Securities and Futures Act 2001 (Cap. 289) | SFA          | Fund manager licensing, VCFM regime                       |
| Companies Act 1967 (Cap. 50)               | CA           | Pte Ltd formation, share rights, shareholders' agreements |
| Variable Capital Companies Act 2018        | VCC Act      | VCC fund structure and governance                         |
| Income Tax Act 1947 (Cap. 134)             | ITA          | ss. 13H, 13O, 13OA, 13U fund tax incentives               |
| Limited Partnerships Act 2008 (Cap. 163B)  | LPA          | Singapore LP fund structures (s.13OA vehicle)             |
| Personal Data Protection Act 2012          | PDPA         | Data protection in investment documents                   |

**Key regulatory instruments:**

- MAS Guidelines on Licensing and Conduct of Business for Fund Management Companies (SFA 04-G05) [VERIFY for latest version — updated March 2025]
- MAS Circular IID 04/2025 on Governance and Management of Variable Capital Companies (June 2025)
- VIMA 2.0 Model Documents (SAL & SVCA, February 2025)

**Singapore vs. Cayman for ASEAN VC:**
Singapore is the dominant domicile for ASEAN-focused VC funds due to its network of ~100 DTAs
(covering all ASEAN member states), VCC and LP structures eligible for tax incentives, proximity
to portfolio companies, and MAS regulatory credibility with LPs. Cayman structures remain
common for funds targeting US institutional LPs requiring FATCA/ERISA-optimised vehicles.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming the
user's objective, the workflow pauses and asks when:

- The user's role (founder, investor, fund manager) materially changes the analysis
- The deal stage or instrument type is ambiguous
- A regulatory threshold determination requires fact-specific information
- Tax incentive eligibility requires entity-specific facts
- The correct ASEAN holding structure requires country-specific input

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

### Step 1: Accept Input

Accept input in any of these formats:

- **Document**: PDF or DOCX of a CARE agreement, term sheet, convertible note, shareholders'
  agreement, or subscription agreement for review
- **Description**: Free-text description of the transaction (stage, parties, proposed terms)
- **Question**: Specific question about Singapore VC law, licensing, or tax incentives
- **Scenario**: Structuring query (e.g., "should we use a VCC or LP for our new fund?")

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user these questions (skip any already answered):

1. **What is your role?**
   - Options: **Founder** (receiving investment), **Investor/VC** (deploying capital),
     **Fund Manager** (establishing/managing a fund), **Legal Counsel** (advising a party),
     **Other**
   - _Why this matters_: Analysis of term sheet provisions, tax incentives, and structure
     recommendations flips depending on which side you represent.

2. **What stage/instrument are you working with?**
   - Options: **Pre-seed/seed CARE note** (VIMA 2.0 CARE Agreement), **Convertible note**
     (bridge/pre-Series A), **Series A equity round** (VIMA 2.0 full suite), **Fund structuring**
     (VCC, LP, Pte Ltd fund vehicle), **VCFM licensing**, **Tax incentive qualification**,
     **ASEAN cross-border structure**, **General question**
   - _Why this matters_: Determines which of the five analysis tracks to activate.

3. **Singapore-incorporated entity?**
   - Confirm: Is the startup or fund vehicle a Singapore-incorporated company (Pte Ltd or VCC)?
   - _Why this matters_: Many VIMA documents, tax incentives, and regulatory regimes require
     Singapore incorporation.

4. **Relevant facts for regulatory/tax tracks** (ask only if Track B, C, or D selected):
   - For VCFM licensing: estimated AUM, investor types (accredited/institutional only?),
     investment strategy (only unlisted companies ≤10 years old for VCFM?)
   - For tax incentives: fund AUM, local business spending capacity, fund vehicle type,
     open-end or closed-end fund?
   - For VCC structuring: number of strategies/sub-funds, investor base, re-domiciliation needed?

### Step 3: Select Analysis Track

Based on user context, activate one or more of the following tracks:

| Track       | Topic                                       | When to Use                                                     |
| ----------- | ------------------------------------------- | --------------------------------------------------------------- |
| **Track A** | CARE / Convertible Note / Term Sheet Review | Document-level analysis of investment instruments               |
| **Track B** | VCFM Licensing & Regulatory Compliance      | Fund manager establishing or reviewing MAS licence requirements |
| **Track C** | VCC / LP / Pte Ltd Fund Structuring         | Choosing and structuring a Singapore fund vehicle               |
| **Track D** | Fund Tax Incentive Qualification            | Assessing eligibility for s.13O, s.13OA, s.13U, s.13H           |
| **Track E** | ASEAN Cross-Border Structuring              | Holding company structure for ASEAN portfolio investments       |

Multiple tracks may be active simultaneously (e.g., a fund manager establishing a new VCC
may activate Tracks B, C, and D concurrently).

### Step 4: Execute Track Analysis

See the **Deep Topic Analysis** section for each track's detailed analysis framework.

### Step 5: Quality Verification

Before delivering any output:

1. Run the 5 Citation Quality Gates silently. Revise any failures.
2. For any CRITICAL-classified finding, run the 3-pass Self-Interrogation.
3. Assign Confidence Scores to all material legal conclusions.
4. Verify all regulatory thresholds and conditions are current (note the date of any threshold
   cited — MAS and IRAS update them periodically).
5. Generate the Glass Box Audit Trail.

### Step 6: Deliver Output

Use the Output Format Template appropriate to the active track(s).

---

## Deep Topic Analysis

### Track A: Investment Document Review

#### A.1 — CARE Agreement (VIMA 2.0, February 2025)

The CARE (Convertible Agreement Regarding Equity) is Singapore's standardised equivalent of
a US SAFE. It was introduced in VIMA 2.0 (February 2025) by SAL and SVCA. Unlike a US SAFE,
the CARE has a Maturity Date but carries **no repayment obligation at maturity** — the investor
may elect to convert at the Maturity Cap or leave the amount outstanding (repayable only on
dissolution).

**Analyse these key economic terms:**

| Term                               | What to Assess                                                                        | Founder Position                                                          | Investor Position                                                           | RED Flag                                                                                      |
| ---------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Valuation Cap**                  | Financing Cap and Maturity Cap (may differ)                                           | Cap as high as possible; consider effect on future round dilution         | Cap reflects current valuation ceiling for risk taken                       | Cap below current reasonable valuation is abusive; dual-cap structure needs careful modelling |
| **Conversion Discount**            | 10–25% off next-round price per share                                                 | Prefer 10–15%; model dilution at exit price                               | 20–25% is standard for high-risk seed                                       | Discount >30% — unlikely to be seen in VIMA-standard transactions                             |
| **Maturity Date**                  | Typically 18–24 months from signing                                                   | Longer maturity reduces pressure to close priced round                    | Shorter maturity creates conversion event sooner                            | <12 months creates excessive founder pressure; >36 months unusual                             |
| **Qualifying Financing Threshold** | Minimum raise size that triggers mandatory conversion                                 | Lower threshold prevents investor holding CARE indefinitely               | Higher threshold protects investor from converting at a micro-round price   | Threshold set so high it can never realistically be met — de facto permanent instrument       |
| **Pro-Rata Rights**                | Investor right to participate in next priced round                                    | Negotiate informational threshold (e.g., invest >S$250K)                  | Standard at most seed rounds                                                | Uncapped pro-rata + highest valuation cap = excessive dilution at Series A                    |
| **Change of Control treatment**    | Cash-out or conversion option at investor election                                    | Prefer conversion at cap if acquirer is credible; cash-out at 1x is floor | Cash-out at 1x or conversion at lower of cap/price                          | No change-of-control provision — investor may have no liquidity event right                   |
| **MFN Clause**                     | Most Favoured Nation — investor gets benefit of more favourable subsequent CARE terms | Prefer to exclude or cap MFN to same-instrument CARE terms                | Standard MFN protects against later investors getting better economic terms | MFN that extends to priced-round terms effectively re-prices the CARE                         |

**CLARIFY** — If reviewing a CARE agreement provided by the user: confirm (a) whether the
VIMA 2.0 CARE template was used as the base, or a bespoke instrument, and (b) whether the
user wants a full clause-by-clause analysis or focus on the economic terms only.

**Jurisdiction note**: CARE agreements in Singapore are governed by Singapore law and the
Companies Act. Dissolution triggers should reference Singapore winding-up provisions under
the CA. [VERIFY applicability of CA insolvency provisions to CARE dissolution events]

#### A.2 — Convertible Note vs. CARE Selection Analysis

When the user needs to select an instrument for a pre-Series A round:

| Factor                        | CARE (VIMA 2.0)                                                                               | Convertible Note                                                                |
| ----------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Interest                      | None                                                                                          | Yes (typically 4–8% p.a., accrues)                                              |
| Maturity repayment obligation | No — investor may convert or leave outstanding                                                | Yes — principal + accrued interest due at maturity                              |
| Accounting treatment          | Equity-like (no debt on balance sheet)                                                        | Debt instrument (appears on balance sheet)                                      |
| Preferred by                  | Founders who want clean balance sheet; seed investors comfortable with equity-like instrument | Bridge investors requiring downside (repayment) protection; later-stage bridges |
| MAS implications              | Not a debenture for SFA purposes (no lending); simpler investor qualification                 | May trigger debenture/lending considerations depending on structure [VERIFY]    |
| VIMA template available       | Yes (CARE Agreement, VIMA 2.0, Feb 2025)                                                      | Yes (Model Convertible Note Purchase Agreement, VIMA 2.0, Feb 2025)             |

**Recommendation framework**:

- **Pre-seed / seed / first external capital** → CARE preferred (no balance sheet debt, aligned with SVCA/SAL market standard, VIMA template available)
- **Bridge between known equity rounds** (existing investors, defined timeline) → Convertible Note appropriate (known parties comfortable with debt instrument, repayment as backstop)
- **Unknown investors / first-time founders** → CARE — simpler structure, less negotiation surface

#### A.3 — Series A Term Sheet Analysis (VIMA 2.0)

Analyse a Series A term sheet against VIMA 2.0 market standards (SAL/SVCA, February 2025):

**Economic terms — classification:**

| Term                         | Market Standard (Singapore, 2025)                                           | FLAG if:                                                       | CRITICAL if:                                                                                          |
| ---------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Liquidation preference**   | 1x, pari passu, non-participating                                           | 1x participating or 1.5x non-participating                     | 2x+ or full participation — effectively eliminates common equity value at modest exits                |
| **Anti-dilution protection** | Broad-based weighted average (BBWA)                                         | Narrow-based weighted average                                  | Full ratchet anti-dilution — almost never seen at Singapore Series A; severely punitive on down round |
| **ESOP pool**                | 10–15% reserved pre-money                                                   | >20% pre-money pool that disproportionately dilutes founders   | Pool created from founder shares rather than company authorised but unissued shares                   |
| **Pre-emptive rights**       | Yes, standard for new share issuances                                       | Excluded for strategic issuances without limit                 | No pre-emptive rights at all                                                                          |
| **Founder vesting**          | 4-year monthly vest, 1-year cliff (acceleration on change-of-control)       | 5-year vest or no acceleration on acquisition                  | Immediate full vesting (investor concern) or 100% single-trigger acceleration                         |
| **Valuation**                | Market-determined; no VIMA standard                                         | Post-money valuation not clearly defined relative to ESOP pool | Pre-money / post-money ambiguity that changes effective price per share significantly                 |
| **Board composition**        | Common directors ≥ Preferred directors; typically 3: 2 founder + 1 investor | Investor board majority at Series A                            | Investor veto on all business decisions regardless of board vote                                      |

**Control terms — classification:**

| Term                      | Market Standard                                                                                    | FLAG if:                                                                   | CRITICAL if:                                                                                     |
| ------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Protective provisions** | Class vote on defined matters (new shares, change to rights, M&A, winding up, constitution change) | Protective provisions extend to routine operations (hiring, budget, capex) | Investor effectively controls all material business decisions                                    |
| **Drag-along**            | Majority of Series A + majority of ordinary shares required to drag                                | Drag can be exercised by investor alone at Series A                        | Drag price below the investor's liquidation preference (investor can drag and take all proceeds) |
| **Information rights**    | Quarterly management accounts; annual audited; annual budget                                       | No audit requirement for 3+ years post-investment                          | No financial reporting at all                                                                    |
| **No-shop / exclusivity** | 30–45 days is standard; mutual no-shop                                                             | >60 days no-shop on founders                                               | Indefinite exclusivity without carve-out for superior proposals                                  |
| **Governing law**         | Singapore law                                                                                      | Cayman law for Singapore-operated company                                  | Unknown jurisdiction; no dispute resolution mechanism                                            |

**⟁ CLARIFY** — For borderline term classifications where market practice is evolving (e.g.,
participating preferred liquidation preferences post-2024 market recovery), ask: "This term
falls between market standard and aggressive. Based on your deal context (round size, competing
term sheets, investor quality), should I treat this as FLAG (negotiate) or CRITICAL (reject
absent material concession)?"

#### A.4 — VIMA 2.0 Document Suite Completeness Check

For a Series A transaction using VIMA 2.0 documents, verify all required documents are present:

- [ ] **Term Sheet** (short-form ~7 pages or long-form ~24 pages) — signed and binding only on
      stated binding provisions (exclusivity, confidentiality, costs)
- [ ] **Subscription Agreement** — primary investment contract; representations and warranties;
      conditions precedent to closing
- [ ] **Shareholders' Agreement** — investor rights; governance; transfer restrictions; exits
- [ ] **Model Constitution** (new in VIMA 2.0) — ACRA-filed constitutional document aligned
      with VIMA shareholder rights; replaces Articles of Association for VIMA-compliant companies
- [ ] **Due Diligence Request List** — completed and key issues resolved or disclosed
- [ ] **ESG Letter Agreement** (optional but increasingly standard; VIMA 2.0 short-form or
      long-form) — ESG reporting commitments, best-efforts ESG policy adoption

**Missing document RED flags:**

- No Shareholders' Agreement in a multi-investor round — governance gaps, no drag/tag
- Term Sheet binding on all commercial terms (not just exclusivity/costs) — creates premature
  contract with potential specific performance risk [VERIFY under Singapore contract law]
- Constitution not updated to align with VIMA investor rights — mismatch between CA-required
  constitutional protections and Shareholders' Agreement terms

---

### Track B: VCFM Licensing & Regulatory Compliance

#### B.1 — VCFM Simplified Regime (Post-RFMC, August 2024)

The Registered Fund Management Company (RFMC) regime was **repealed on 1 August 2024**.
Former RFMCs were required to apply between April–June 2024 for either an A/I LFMC licence
or the VCFM simplified regime.

**Current licensing categories for Singapore fund managers:**

| Category                                | Key Conditions                                                                                                                                  | Suitable For                                                        |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **VCFM** (Venture Capital Fund Manager) | 80% rule; unlisted companies ≤10 years; AIs and IIs only; no minimum base capital; 2 Singapore-resident IPs + CEO; no minimum years' experience | Pure VC/seed funds investing only in early-stage unlisted companies |
| **A/I LFMC**                            | CMS licence; restricted to AIs and IIs; initial S$250M AUM cap (lifted over time); min. base capital S$250K; 5 years' experience for PM         | Growth/buyout funds; former RFMCs with broader mandates             |
| **LFMC (Full)**                         | CMS licence; unrestricted investor base; min. base capital S$250K–S$1M; complex ongoing compliance                                              | Retail-accessible funds; large managers                             |

**VCFM eligibility requirements checklist** [VERIFY against current SFA 04-G05]:

- [ ] **80% qualifying investment test**: At least 80% of committed capital (net of fees/
      expenses) must be invested in securities/instruments **directly issued by unlisted businesses
      incorporated ≤10 years** at initial investment
- [ ] **Investor base restricted**: All investors must be accredited investors (AIs) or
      institutional investors (IIs) as defined in the SFA — no retail investors
- [ ] **Singapore incorporation**: VCFM entity must be incorporated in Singapore
- [ ] **Physical Singapore office**: Permanent physical office (not virtual) in Singapore
- [ ] **CEO requirement**: Full-time CEO who is Singapore-resident responsible for daily operations
- [ ] **Two investment professionals**: At least two full-time IPs resident in Singapore
      (may overlap with directors)
- [ ] **Two directors**: At least two directors; at least one must be full-time and Singapore-resident
- [ ] **Fit and proper**: All key persons must satisfy MAS fit-and-proper requirements
- [ ] **AML/CFT programme**: Compliant anti-money laundering/counter-financing of terrorism
      programme in place before licence grant
- [ ] **No minimum base capital**: VCFM does not require minimum base capital (unlike other LFMCs)

**VCFM limitation — the 80% rule in practice:**
A VCFM that makes a follow-on investment into a portfolio company that has been incorporated
**more than 10 years** at the time of the follow-on cannot count that investment toward the
80% threshold. VCFM managers should track portfolio company ages for each investment tranche.

FLAG triggers in VCFM compliance:

- Any investment in a **listed** company — disqualifies that investment from the 80% count
- Any **retail investor** LP — immediately invalidates the VCFM regime; requires full LFMC
  licence
- Portfolio company older than 10 years at initial investment — must track proportion carefully
- No Singapore-resident CEO or IPs — regulatory non-compliance

**⟁ CLARIFY** — For VCFM licensing questions, confirm: (a) intended AUM and investor types,
(b) whether 100% of the fund strategy will meet the 80% unlisted/≤10-year test, and
(c) whether any existing investors are retail (which would preclude the VCFM simplified regime).

---

### Track C: VCC / LP / Pte Ltd Fund Structuring

#### C.1 — Vehicle Comparison Matrix

| Factor                     | VCC (Umbrella)                                  | Singapore LP                                                      | Pte Ltd Fund                                                            |
| -------------------------- | ----------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Legal basis**            | VCC Act 2018                                    | Limited Partnerships Act 2008                                     | Companies Act 1967                                                      |
| **Multi-strategy**         | Yes — segregated sub-funds                      | No — one strategy per LP                                          | No — requires separate Pte Ltd per strategy                             |
| **Capital variability**    | Fully variable — easy subscriptions/redemptions | Variable via LP agreement                                         | Capital reduction requires CA process                                   |
| **Dividend source**        | Capital and profits                             | Pass-through                                                      | Profits only                                                            |
| **Investor privacy**       | Members register not publicly disclosed         | Limited partner names not in public register                      | Shareholders in public ACRA register                                    |
| **Tax incentive eligible** | s.13O, s.13U                                    | s.13OA (Jan 2025), s.13U                                          | s.13O, s.13U                                                            |
| **Fund manager required**  | Yes — Permissible Fund Manager (MAS-regulated)  | No MAS requirement on LP per se (manager still needs CMS licence) | Manager needs CMS licence                                               |
| **Re-domiciliation**       | Yes — offshore funds can re-domicile to VCC     | No                                                                | No                                                                      |
| **Market adoption**        | 1,200+ VCCs as of March 2025                    | Growing post-13OA (Jan 2025)                                      | Common for single-fund Pte Ltd VC structures; declining relative to VCC |
| **Governance**             | Shared board for umbrella; sub-fund directors   | GP/LP structure; GP manages                                       | Board of directors                                                      |

**VCC advantages for new VC funds:**

- Sub-fund segregation: run multiple vintage funds or strategies under one umbrella without separate legal entities
- Tax incentive access: eligible for s.13O and s.13U (and re-domiciled funds retain eligibility)
- Variable capital: clean NAV management without CA capital reduction procedure
- Investor privacy: institutional LPs value non-disclosure of membership

**VCC formation requirements:**

- At least one Singapore-resident director (citizen, PR, or valid work pass holder)
- At least one director must be a qualified representative or director of the Permissible Fund Manager
- Must be managed by a Permissible Fund Manager — a CMS licence holder
- Registered office in Singapore; resident company secretary; Singapore-registered auditor
- Cannot be self-managed — a separate MAS-regulated fund manager entity is mandatory

**June 2025 MAS VCC Governance Circular (IID 04/2025) — key expectations** [VERIFY for
implementation requirements]:

- Fund managers must conduct **substantive investment management** in Singapore — not merely
  act as a conduit for investment decisions made offshore
- Assets must be subject to **independent custody**, except for PE/VC investments offered
  only to AIs/IIs
- VCC directors conducting regulated activities (deal sourcing, portfolio management,
  trade execution) must be **licensed representatives** of the fund manager
- Dormant VCCs with no assets or investors must be wound down
- AML/CFT controls required via engagement of an eligible financial institution (EFI)

#### C.2 — Singapore LP + Section 13OA (new January 2025)

Section 13OA (effective 1 January 2025) extended the fund tax exemption to Singapore LPs,
filling the gap that previously required most LP-structured funds to incorporate a holding
company to access s.13O benefits.

LP structure advantages post-13OA:

- Pass-through taxation at LP level (no entity-level Singapore tax)
- Limited partners receive proportional tax exemption on Specified Income from Designated
  Investments
- GP retains full management control; limited partners have limited liability
- Familiar structure for US institutional LPs (Delaware LP analogue)
- Closed-end fund irrevocable election available from 1 January 2025: waive minimum AUM
  and LBS requirements after a specified period consistent with the closed-end lifecycle

**Recommendation**: For PE/VC funds with institutional US LP investors, the Singapore LP +
s.13OA combination may be optimal. For ASEAN-focused funds with Asian family office LPs who
value privacy and flexibility, the VCC remains preferred.

---

### Track D: Fund Tax Incentive Qualification

#### D.1 — Overview of Fund Tax Incentives (Post-January 2025 Revamp)

| Incentive  | Vehicle Eligible                                           | Minimum AUM                                                               | Local Business Spending (LBS)      | Min. IPs                       | Extension               |
| ---------- | ---------------------------------------------------------- | ------------------------------------------------------------------------- | ---------------------------------- | ------------------------------ | ----------------------- |
| **s.13O**  | Singapore-incorporated company (Pte Ltd, VCC)              | S$5M in Designated Investments [VERIFY — changed from NAV basis Jan 2025] | S$200K–S$500K/year (tiered by AUM) | 2 IPs employed by fund manager | To 31 Dec 2029          |
| **s.13OA** | Singapore LP (new Jan 2025)                                | S$5M in Designated Investments                                            | S$200K–S$500K/year (tiered by AUM) | 2 IPs                          | To 31 Dec 2029          |
| **s.13U**  | Company, trust, LP (resident and non-resident)             | S$50M in Designated Investments                                           | S$200K–S$500K/year (tiered by AUM) | 2 IPs                          | To 31 Dec 2029          |
| **s.13H**  | PE/VC funds investing in Singapore SMEs/unlisted companies | No fixed minimum                                                          | Separate EDB approval criteria     | EDB/MAS joint assessment       | Up to 10-year exemption |

**Designated Investments** include: listed/unlisted equities, debt instruments, REITs, PE/VC
instruments, private credit, infrastructure. [VERIFY full list against IRAS — Sixth Schedule ITA]

**Specified Income** includes: gains from Designated Investments; interest income; dividends
from Designated Investments. Does not include: income from Singapore immovable property;
income from Singapore-situated business other than fund activities. [VERIFY]

**AUM measurement change (January 2025)**: AUM is now measured by the **value of Designated
Investments** held at year-end (DI-value basis), replacing the former NAV basis. Funds
invested primarily in illiquid PE/VC instruments may face different AUM characterisation than
under the old methodology. [VERIFY with fund's auditors]

#### D.2 — Section 13O/13OA Tiered LBS Requirements

| AUM in Designated Investments | Required Annual LBS                                      |
| ----------------------------- | -------------------------------------------------------- |
| S$5M – S$20M                  | S$200,000                                                |
| S$20M – S$50M                 | S$350,000 [VERIFY exact thresholds — announced Oct 2024] |
| >S$50M                        | S$500,000                                                |

LBS includes: Singapore-based investment professionals' salaries and CPF; Singapore legal,
accounting, and admin fees; Singapore office costs; advisory fees to Singapore service
providers. [VERIFY full definition against IRAS guidance]

**Closed-end fund election (new January 2025)**:
A closed-end fund (PE/VC fund with fixed capital commitments and defined lifespan) may make
an **irrevocable one-time election** at the time of application to waive the minimum AUM and
tiered LBS requirements after a period consistent with the fund's closed-end lifecycle
(e.g., after the investment period when capital is deployed but not yet realised). This
election is permanent — model the full fund lifecycle before electing.

#### D.3 — Section 13H (VC/SME Equity Incentive)

Section 13H provides tax exemption specifically for **equity remuneration incentive schemes
for SMEs** and is administered jointly by EDB and MAS. It applies to approved PE/VC funds
investing in:

- Singapore SMEs and unlisted companies
- Investments receiving qualifying equity instruments

Key distinction from s.13O: Section 13H involves a joint EDB/MAS application process and
is specifically targeted at funds with a Singapore SME/startup investment mandate.
Up to **10-year exemption period**. [VERIFY current eligibility criteria with EDB]

**⟁ CLARIFY** — For tax incentive queries, confirm: (a) fund vehicle type (Pte Ltd, VCC, LP),
(b) estimated AUM at application and projected peak, (c) whether the fund is open-end or
closed-end, (d) number of Singapore-based investment professionals employed by the manager,
and (e) expected LBS capacity. Without these facts, only a framework analysis is possible.

---

### Track E: ASEAN Cross-Border Structuring

#### E.1 — Singapore as Regional Hub

Singapore is the dominant holding structure and fund domicile for ASEAN-focused investments.
The standard structure: **Singapore Pte Ltd or VCC** as the holdco/fund vehicle, with
operating subsidiaries or portfolio companies incorporated in the target ASEAN jurisdiction.

**Singapore DTA network advantages for ASEAN VC:**

| Portfolio Country | Singapore DTA Benefit                                                                          | Key Consideration                                                                                                      |
| ----------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Indonesia**     | Dividends 10% withholding (vs. 20% standard); reduced interest/royalty rates                   | OJK foreign investment rules; restricted sectors (media, telecoms, agriculture)                                        |
| **Malaysia**      | No dividend withholding (Malaysia zero-rates dividends domestically); reduced interest/royalty | Bursa-listed investments require SC Malaysia licence for fund managers; Bumiputera equity requirements in some sectors |
| **Thailand**      | Reduced withholding rates via DTA                                                              | Thai BOI incentives stackable with Singapore holdco; sector-specific FDI restrictions                                  |
| **Vietnam**       | Dividends 5–15% via DTA                                                                        | DICA/MPI foreign investment registration required; Vietnam Enterprise Law                                              |
| **Philippines**   | DTA in force; reduced rates                                                                    | Negative investment list; 40% foreign ownership cap in many sectors                                                    |

**Standard Singapore holdco structure for ASEAN VC:**

1. **Singapore Pte Ltd (or VCC sub-fund)** as direct investor
2. Holds equity stake in operating company in ASEAN jurisdiction
3. Routes distributions up through Singapore to fund (collecting DTA benefits)
4. Singapore IRAS territorial basis: capital gains from disposal of foreign shares generally
   not taxable in Singapore (no capital gains tax) [VERIFY — position based on established
   practice; tax treatment depends on trading vs. investment characterisation]
5. Dividends received from foreign subsidiaries: exempt under one-tier system in most cases

**India "reverse flip" note**: Indian-origin startups that previously held Singapore Pte Ltd
holdcos have been "reverse-flipping" back to India (since 2022–2023) to access BSE/NSE
listings and Indian government incentives. Founders considering a Singapore holdco for an
India-focused startup should model both scenarios and timing of any future reverse flip.

#### E.2 — Entity Type Selection for ASEAN Portfolio Companies

When a Singapore VC is investing into an ASEAN portfolio company:

| Country     | Standard Entity Type      | Foreign Ownership                                                 | Key Restriction                                       |
| ----------- | ------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------- |
| Indonesia   | PT (Perseroan Terbatas)   | Generally 100% in eligible sectors via BKPM OSS                   | Negative Investment List; specific sectors restricted |
| Malaysia    | Sdn. Bhd.                 | 100% in most sectors                                              | Equity conditions for Bumiputera in specific sectors  |
| Thailand    | Co., Ltd                  | 49% (majority Thai) in most sectors; 100% via BOI or AMLO licence | Foreign Business Act; land ownership restrictions     |
| Vietnam     | LLC (Công ty TNHH) or JSC | Up to 100% in most non-conditional sectors                        | Sector-specific conditional investment list           |
| Philippines | Corporation               | Max 40% foreign in most sectors; 100% in export zones             | Constitution art. XII; Negative List                  |

[All country-specific restrictions should be verified with local counsel — this table reflects
general positions as of early 2026 and may not reflect recent policy changes]

---

## Severity Classification

### MARKET-STANDARD — Acceptable

Term or condition aligns with VIMA 2.0 / SVCA market standards or applicable regulatory
requirements. No negotiation required.

**Examples**: 1x non-participating liquidation preference; BBWA anti-dilution; 4-year monthly
vest with 1-year cliff; standard VCFM 80% qualifying investment test.

**Action**: Note for awareness. Proceed.

### FLAG — Negotiate / Monitor

Term or condition deviates from market standard but falls within a negotiable range.
Commercially common but not the preferred position for the user's side.

**Examples**: 1.5x non-participating liquidation preference; narrow-based weighted average
anti-dilution; 5-year founder vesting; VCFM compliance gap that can be remediated without
licence loss.

**Action**: Identify specific issue, provide recommended negotiating position, estimate impact
of conceding vs. negotiating.

### CRITICAL — Reject / Escalate

Term or condition falls outside acceptable range, creates material legal or regulatory risk,
or is inconsistent with Singapore law or VIMA market standards. Requires senior counsel review
or regulatory escalation.

**Examples**: Full ratchet anti-dilution; 2x+ participating preferred; no Shareholders'
Agreement in a multi-investor round; VCFM servicing a retail investor; fund applying for
s.13O/13OA below minimum AUM threshold; VCC managed without MAS-regulated fund manager.

**Action**: Explain the specific risk (with legal basis). Provide market-standard alternative.
Estimate exposure. Recommend escalation path. Flag Singapore counsel engagement.

---

## Actionable Output per Finding

For each FLAG or CRITICAL finding, provide:

```
**Issue**: [Concise description of the deviation or compliance gap]
**Severity**: FLAG / CRITICAL
**Current position**: "[Exact term, clause, or regulatory status]"
**Risk**: [Specific consequence — dilution impact, regulatory sanction, tax exemption loss, etc.]
**Recommended position**: "[Specific VIMA market-standard alternative or compliant position]"
**Legal basis**: [Statute, regulation, VIMA standard, or MAS guideline — or "[VERIFY]"]
**Priority**: [Tier 1 Must-Resolve / Tier 2 Should-Resolve / Tier 3 Monitor]
**Negotiating note**: [For term sheet items: fallback position; for regulatory items: remediation timeline]
```

---

## Prioritization Framework

### Tier 1 — Must-Resolve (Pre-Signing / Pre-Licence)

Issues that must be addressed before signing documents or submitting regulatory applications:

- Structural terms that cannot be unwound post-investment (full ratchet anti-dilution, 2x+ liquidation preference)
- Missing Shareholders' Agreement or constitution in multi-investor round
- VCFM licensing non-compliance (retail investor in fund; insufficient Singapore-resident IPs)
- Fund tax incentive structuring error that disqualifies the vehicle before application
- VCC without Permissible Fund Manager — regulatory void

### Tier 2 — Should-Resolve (Before Closing / Within 3 Months)

Issues that materially affect risk but have remediation paths:

- Term sheet ambiguity on valuation basis (pre-money vs. post-money including ESOP pool)
- CARE MFN clause scope that should be narrowed before investors sign
- VCFM 80% compliance monitoring process not yet established
- LBS planning for s.13O/13OA that has not been budgeted
- VCC governance documentation not aligned with MAS IID 04/2025 circular expectations

### Tier 3 — Monitor (Periodic Review)

Issues that should be tracked but do not require immediate action:

- ESG letter agreement provisions that are best-efforts only
- ASEAN portfolio company foreign ownership thresholds as sector rules evolve
- DTA benefit confirmation (withholding tax certificates required annually)
- s.13O/13OA AUM test monitoring (measured at year-end; DI-value basis)

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                                          | Fail Action                                                          |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific Singapore statute, MAS regulation/guideline, or established principle                                                      | Add citation or mark "[UNVERIFIED — Singapore counsel to confirm]"   |
| **Format**     | All citations follow consistent Singapore legal citation format (e.g., "SFA s.99"; "ITA s.13O"; "CA s.161")                                                   | Fix format                                                           |
| **Currency**   | Every cited provision checked for amendments or repeal — MAS and IRAS update thresholds and guidelines frequently (note: October 2024 / January 2025 changes) | Flag "[CHECK CURRENCY — verify against MAS/IRAS as of current date]" |
| **Domain**     | Analysis stays within Singapore law unless explicitly addressing ASEAN cross-border matters                                                                   | Remove or flag jurisdictional bleed                                  |
| **Confidence** | Uncertainty explicitly stated, not hidden — Singapore regulatory positions change with MAS policy cycles                                                      | Add confidence qualifier and date of source                          |

---

## Self-Interrogation for CRITICAL Items

For any item classified as CRITICAL, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the risk assessment follow logically from the cited Singapore statute or MAS guideline?
- Would MAS / IRAS / ACRA enforcement staff actually reach this conclusion on these facts?
- Is there a counter-argument (e.g., an exemption under the SFA, an IRAS advance ruling
  position) that the other party's counsel would make?

**Pass 2 — Completeness**:

- Have all relevant Singapore statutes and MAS/IRAS guidelines been considered?
- Have recent amendments (e.g., January 2025 tax changes, August 2024 RFMC repeal) been
  accounted for?
- Are there regulatory dimensions (e.g., PDPA, foreign investment restrictions, FATF/AML)
  not yet addressed?

**Pass 3 — Challenge**:

- What is the strongest argument that this term or position IS acceptable under Singapore law?
- Under what commercial circumstances would a Singapore corporate lawyer accept this risk?
- Is the CRITICAL classification proportionate, or is this actually FLAG with appropriate
  safeguards?

Mark the audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

---

## Confidence Scoring

For each material legal conclusion, assign a confidence level:

| Level        | Range     | Meaning                                                                                   | Action                                                          |
| ------------ | --------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled Singapore law, clear statutory text, established MAS position                     | State with confidence                                           |
| **High**     | 0.80–0.94 | Strong authority (statute + MAS guideline), minor interpretation questions                | State with brief caveat                                         |
| **Probable** | 0.60–0.79 | Good arguments based on statute/VIMA standard, but MAS has not issued definitive guidance | State with reasoning and contra-indicators                      |
| **Possible** | 0.40–0.59 | Genuinely uncertain; MAS policy in flux or novel instrument type                          | Flag for Singapore counsel review with both sides               |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative or based solely on analogical reasoning                           | Do not assert; flag "[UNCERTAIN — Singapore counsel to advise]" |

---

## Glass Box Audit Trail

Every output MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-venture-financing-sg"
  transaction_or_query: "[description of the matter reviewed]"
  active_tracks: "[A / B / C / D / E — one or more]"
  user_role: "[Founder / Investor / Fund Manager / Counsel / Other]"
  instrument_type: "[CARE / Convertible Note / Series A Term Sheet / VCC / VCFM / Tax Incentive / etc.]"
  singapore_law_basis:
    - "SFA (Cap. 289)"
    - "CA (Cap. 50)"
    - "ITA ss.13O/13OA/13U/13H"
    - "VCC Act 2018"
    - "[other statutes as applicable]"
  vima_version: "VIMA 2.0 (February 2025)"
  legalcode_mcp: "Connected / Not connected"
  key_regulatory_thresholds_verified:
    - "[threshold 1 and source]"
    - "[threshold 2 and source]"
  citations_verified: "[number VERIFIED via legalcode-mcp or current source] / [number UNVERIFIED — marked [VERIFY]]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  findings_summary:
    critical: "[number]"
    flag: "[number]"
    market_standard: "[number]"
  limitations:
    - "[Scope limitations, assumptions, or caveats — especially for rapidly changing MAS/IRAS thresholds]"
    - "[Country-specific matters noted as requiring local counsel]"
  date_of_analysis: "[date]"
  reviewer: "AI-assisted — requires qualified Singapore-admitted advocate and solicitor review"
```

---

## Anti-Patterns

Singapore VC-specific catalogue of what NOT to do:

1. **Using a US SAFE without Singapore adaptation** — A US Y Combinator SAFE is not designed
   for Singapore law. CARE (VIMA 2.0) is the Singapore-specific equivalent. Using a SAFE with
   Singapore law creates conversion mechanism ambiguity and potential mismatch with CA share
   issuance rules. Use CARE for Singapore companies.

2. **Assuming the RFMC regime still exists** — The RFMC regime was repealed on 1 August 2024.
   Advising a fund manager to register as an RFMC is incorrect. All new managers must apply
   under the CMS licence framework (VCFM, A/I LFMC, or LFMC).

3. **Applying s.13O/13OA/13U thresholds from pre-2025 guidance** — The October 2024 revamp
   changed minimum AUM thresholds (using DI-value basis), LBS tiers, and introduced the
   closed-end election. Pre-2025 advisory materials will have incorrect thresholds. Always
   verify against the January 2025 MAS Circular and current IRAS guidance.

4. **VCC without a Permissible Fund Manager** — A VCC cannot be self-managed; it must be
   managed by an MAS-regulated fund manager (CMS licence holder). Forming a VCC without
   arranging a regulated fund manager in advance creates a regulatory void from day one.

5. **VCFM fund accepting a retail investor** — A single retail investor LP immediately
   invalidates the VCFM simplified regime, requiring full LFMC licensure. Due diligence
   on all LP investor qualifications (AI/II status) is mandatory before accepting capital.

6. **Ignoring the VCFM 80% rule for portfolio company age** — The 10-year limit runs from
   incorporation at the **time of initial investment**. A portfolio company that was young
   at initial investment but ages past 10 years before follow-on may reduce the 80% test
   compliance. Track each portfolio company's incorporation date for each investment tranche.

7. **Full ratchet anti-dilution on Singapore equity** — Full ratchet is almost never seen
   at Singapore Series A and effectively eliminates common shareholder value in a down round.
   It should be classified CRITICAL and countered with BBWA as the VIMA market standard.

8. **Binding term sheet on commercial terms** — Under Singapore contract law, a term sheet
   intended to be non-binding (except on exclusivity, costs, and confidentiality) must
   clearly state which provisions are binding. A term sheet that appears to bind all
   commercial terms may be enforceable — potentially allowing specific performance claims
   for the investment even if parties subsequently disagree on documentation. Use standard
   VIMA term sheet language clearly limiting binding provisions.

9. **Constitution not updated post-investment** — A Singapore company's constitution (filed
   with ACRA) takes precedence over a Shareholders' Agreement in some respects under the
   CA. If investor protective provisions (e.g., class voting rights, preference share terms)
   are in the Shareholders' Agreement but not in the constitution, a third-party acquirer or
   subsequent investor may not be bound. The VIMA 2.0 Model Constitution addresses this;
   use it or ensure your constitution is updated at closing. [VERIFY under CA]

10. **Singapore holdco for India-heavy portfolio without reverse-flip planning** — For
    founders with primarily Indian operations, the India "reverse flip" trend (redomiciling
    back to India for BSE/NSE listing) should be considered early in structuring. A Singapore
    holdco may complicate an Indian listing exit. Model the full exit scenario before adopting
    the holdco structure.

11. **Ignoring CPF implications for VCFM IP employees** — Investment professionals employed
    by a Singapore VCFM entity who are Singapore citizens or PRs require CPF contributions,
    which count toward the LBS requirement for tax incentives. Foreign IP hires on Employment
    Passes do not require CPF. The two-IP minimum is a headcount rule; CPF implications
    affect the cost structure and LBS modelling.

12. **Mixing ASEAN investment mandates in a VCFM** — A VCFM must invest ≥80% in qualifying
    investments (unlisted, ≤10 years). Portfolio companies in Indonesia, Malaysia, Vietnam etc.
    that are unlisted and ≤10 years old can qualify — the test is not restricted to Singapore
    companies. However, a blended strategy with some listed ASEAN investments or secondary
    market positions may fall below 80% compliance. Model the strategy before applying for VCFM.

13. **Assuming no Singapore tax on carry (carried interest)** — Singapore currently has no
    capital gains tax, and management company income (fees) is taxed as income. Carry
    (performance allocation from a fund) may be characterised as a capital gain or revenue
    depending on structure and trading frequency. Complex carry structures should be reviewed
    with Singapore tax counsel before implementation. [VERIFY current IRAS position on carry]

14. **Overlooking PDPA obligations in due diligence** — Singapore's Personal Data Protection
    Act 2012 applies to due diligence data rooms. Founders sharing employee data, customer
    lists, and other personal data with investors in a data room must ensure PDPA-compliant
    data handling obligations are imposed on recipients (via NDA/confidentiality provisions
    that include PDPA terms). VIMA 2.0 NDA provisions should be checked for PDPA adequacy.

15. **Pro-rata rights without an anti-dilution model** — CARE investors with pro-rata rights
    AND an anti-dilution adjustment at Series A can compound their ownership in unexpected
    ways. A founder who grants both CARE valuation caps and pro-rata rights to multiple seed
    investors without modelling the Series A dilution impact may find themselves with
    significantly lower ownership post-Series A than expected. Always model both before
    agreeing to combined terms.

16. **Ignoring MAS IID 04/2025 substantive management requirement for VCCs** — Following
    the June 2025 circular, VCCs where the "Singapore fund manager" is only nominally
    present (offshore investment decisions; Singapore entity only for tax/structure) face
    regulatory risk. Substantive investment activity must occur in Singapore.

17. **Drafting CARE maturity date too short for fundraising cycle** — An 18-month CARE
    maturity is tight given Singapore/ASEAN fundraising cycles. If the company has not closed
    a Qualified Financing by month 16 and approaches the maturity date, founders face pressure
    to accept any priced round. Consider 24-month maturity with option to extend by mutual
    agreement.

---

## Writing Standards

Apply plain-language discipline to all output:

**For term sheet analysis and redline recommendations**:

- Active voice: "This clause gives the investor full ratchet protection" not "Full ratchet
  protection is provided to the investor by this clause"
- Short sentences. One concept per sentence.
- Name the party: "The investor may drag the founders" not "A drag-along may be exercised"
- Cite the VIMA standard: "VIMA 2.0 market standard is broad-based weighted average" not
  "the market generally uses BBWA"

**For regulatory and tax analysis**:

- State thresholds precisely (S$5M AUM for s.13O, not "a minimum AUM threshold")
- Cite the exact provision (ITA s.13O, not "the tax incentive")
- Flag uncertainty explicitly: "as of January 2025 per MAS Circular; verify current position"

**Quality gates before delivery**:

1. Can a non-lawyer founder understand the executive summary?
2. Can Singapore corporate counsel immediately act on each FLAG/CRITICAL finding?
3. Is every legal claim backed by a specific Singapore statute, MAS guideline, or VIMA
   standard — or explicitly flagged [VERIFY]?
4. Are all regulatory thresholds date-stamped (as of when they were last verified)?
5. Could any sentence be shorter without losing precision? If yes, shorten.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 4 analysis, search for current SFA provisions, MAS guidelines (SFA 04-G05), and
  ITA sections (13O, 13OA, 13U, 13H)
- Save relevant results to `/tmp/legalcode-sg-vc-authority.md`
- Verify current VCFM eligibility thresholds and tax incentive conditions
- Check for any MAS circulars issued since October 2024 on the VCFM regime or fund incentives
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory thresholds and regulatory requirements with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed with analysis using the thresholds in this skill, noting that MAS/IRAS update them
  periodically and all figures require verification against current official sources
- Recommend that the user engage Singapore-admitted counsel to verify all regulatory
  positions before acting

---

## Localization Notes

**Singapore-specific legal terminology:**

| Singapore Term                    | Equivalent Concept                             | Notes                                                            |
| --------------------------------- | ---------------------------------------------- | ---------------------------------------------------------------- |
| Pte Ltd (Private Limited Company) | Closely held corporation (US) / Ltd (UK)       | Governed by CA Cap. 50; default vehicle for startups             |
| Accredited Investor (AI)          | Sophisticated investor (US)                    | SFA definition: net personal assets >S$2M OR income >S$300K p.a. |
| Institutional Investor (II)       | Institutional investor                         | Banks, insurers, licensed fund managers, pension funds           |
| Advocate and Solicitor            | Attorney / Solicitor                           | Singapore Bar admission required                                 |
| ACRA                              | Companies House (UK) / Secretary of State (US) | Accounting and Corporate Regulatory Authority                    |
| BizFile+                          | Companies registry online portal               | ACRA's incorporation and filing system                           |
| CPF                               | Social security / superannuation               | Central Provident Fund; mandatory for citizens/PRs               |
| EntrePass                         | Founder work pass                              | For foreign founders who will operate their Singapore business   |
| IRAS                              | Tax authority                                  | Inland Revenue Authority of Singapore                            |

**ASEAN note**: Southeast Asian markets use distinct legal terminology and entity types.
When advising on ASEAN cross-border structures, always engage local counsel in each
target jurisdiction. This skill's ASEAN analysis covers strategic structuring only;
country-specific legal requirements require jurisdiction-specific expertise.

---

## Output Format Template

Structure deliverables as follows (adapt sections based on active tracks):

```markdown
## Singapore Venture Financing Analysis

**Matter**: [description of the transaction or query]
**User Role**: [Founder / Investor / Fund Manager / Counsel]
**Active Tracks**: [A / B / C / D / E]
**Instrument / Vehicle**: [CARE / Term Sheet / VCFM / VCC / Tax Incentive / Cross-border]
**Singapore law basis**: [primary statutes and VIMA version]
**Date of analysis**: [date]

---

## Executive Summary

[2–4 sentence summary for a non-lawyer founder/investor/manager.
Lead with the most important finding. State the recommended action.]

---

## Key Findings

### CRITICAL Issues — Act Now

[For each CRITICAL finding, use the Actionable Output format above]

### FLAG Issues — Negotiate / Monitor

[For each FLAG finding, use the Actionable Output format above]

### MARKET-STANDARD Provisions

[Summary table of provisions reviewed and confirmed as market-standard]

---

## [Track-specific section — repeat for each active track]

### Track A: Document Analysis — [Instrument Name]

[Clause-by-clause or term-by-term analysis using classification framework]

### Track B: VCFM Licensing Compliance

[Eligibility checklist with COMPLIANT / NEEDS REMEDIATION / NON-COMPLIANT per requirement]

### Track C: Fund Vehicle Analysis

[Vehicle comparison and recommendation with rationale]

### Track D: Tax Incentive Qualification

[Incentive eligibility assessment with threshold analysis]

### Track E: ASEAN Cross-Border Structure

[DTA benefits analysis; portfolio country entity selection; key restrictions]

---

## Prioritized Action Plan

### Tier 1 — Must-Resolve Before [Signing / Licence Application / Closing]

1. [Action item]

### Tier 2 — Should-Resolve Within [30 / 60 / 90] Days

1. [Action item]

### Tier 3 — Monitor Ongoing

1. [Action item]

---

## Recommended Singapore Counsel Engagement

[Note any areas where Singapore-admitted counsel must be engaged:

- Term sheet negotiation and VIMA documentation
- VCFM CMS licence application (MAS)
- VCC formation and MAS registration
- s.13O/13OA tax incentive application (IRAS / MAS)
- ASEAN country-specific legal requirements]

---

[Glass Box Audit Trail YAML]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on comprehensive research of:

- VIMA 2.0 documentation suite (SAL & SVCA, February 2025)
- MAS Guidelines SFA 04-G05 on Licensing and Conduct of Business for Fund Management Companies
  (March 2025 update)
- MAS Circular IID 04/2025 on Governance and Management of Variable Capital Companies
  (June 2025)
- MAS Circular on RFMC Repeal (effective 1 August 2024)
- October 2024 MAS announcement on fund tax incentive revamp (effective 1 January 2025)
  including Section 13OA introduction and Section 13O/13U AUM/LBS threshold revisions
- Section 13H EDB/MAS joint incentive framework
- VCC Act 2018 and ACRA VCC regulatory framework
- Singapore Companies Act 1967 (Cap. 50) and ACRA Pte Ltd formation requirements
- Singapore DTA network and ASEAN cross-border structuring practice
- SVCA market practice data and Chambers & Partners Singapore VC Trends 2025

All citations should be verified against current MAS, IRAS, ACRA, and SAL/SVCA publications
before use. This skill does not constitute legal advice.
