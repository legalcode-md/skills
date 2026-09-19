---
name: legalcode-distribution-agreement-review
description: Review distribution and reseller agreements covering territory exclusivity, minimum purchase
  commitments (MPC/MAP), pricing and discount structures (including RPM and MFN clauses), marketing obligations
  and brand standards, IP licenses for trademarks and trade dress (naked licensing risk), termination
  and post-termination obligations, competition law compliance (EU VBER 2022 / Regulation 2022/720, US
  Sherman Act Section 1 / Leegin / Sylvania / Colgate doctrine / Robinson-Patman), and channel conflict
  management (dual distribution, online/offline separation, marketplace bans). Use when reviewing exclusive
  distribution agreements, non-exclusive distribution agreements, reseller agreements, authorised distributor
  agreements, OEM distribution agreements, or any channel-partner contract where a supplier appoints an
  intermediary to resell its products or services into a defined territory or customer segment.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review distribution and reseller agreements covering territory exclusivity, minimum purchase commitments (MPC/MAP), pricing and discount structures (including RPM and MFN clauses), marketing obligations and brand standards, IP licenses for trademarks and trade dress (naked licensing risk), termination and post-termination obligations, competition law compliance (EU VBER 2022 / Regulation 2022/720, US Sherman Act Section 1 / Leegin / Sylvania / Colgate doctrine / Robinson-Patman), and channel conflict management (dual distribution, online/offline separation, marketplace bans). Produces clause-by-clause review with EU/US market-standard benchmarks, severity-classified findings, and competition-law compliance screening. Use when reviewing exclusive distribution agreements, non-exclusive distribution agreements, reseller agreements, authorised distributor agreements, OEM distribution agreements, or any channel-partner contract where a supplier appoints an intermediary to resell its products or services into a defined territory or customer segment.


# Legalcode Distribution Agreement Review

> **Disclaimer**: This skill provides a framework for AI-assisted review of distribution
> and reseller agreements. It does not constitute legal advice. All outputs should be
> reviewed by a qualified legal professional licensed in the relevant jurisdiction before
> use. Laws change; verify current applicability before relying on any provision described
> here. Statutory and case law references cited from memory carry hallucination risk —
> verify against authoritative sources before relying on them. Competition law analysis
> in particular requires jurisdiction-specific counsel as fines can reach 10% of worldwide
> group turnover (EU) or treble damages (US).

---

## Purpose and Scope

This skill reviews distribution and reseller agreements against market standards and
competition law requirements. It identifies deviations, classifies severity, generates
actionable redline suggestions, and flags competition law compliance risks across EU and
US frameworks.

**Covers:**

- Clause-by-clause analysis of distribution and reseller agreements
- Competition law compliance screening (EU VBER 2022, US Sherman Act)
- Territory exclusivity and minimum purchase commitment review
- Trademark/IP licensing quality control (naked licensing risk)
- Termination and post-termination obligation analysis (EU mandatory country law)
- Channel conflict and dual distribution assessment
- Deviation classification (GREEN / YELLOW / RED / COMPETITION-RISK)
- Redline generation with fallback positions
- Multi-stakeholder impact mapping
- Glass Box audit trail

**Does not:**

- Draft new distribution agreements (use a drafting-specific skill)
- Provide legal advice or replace qualified competition or distribution law counsel
- Replace a full antitrust analysis for market-share-sensitive transactions
- Apply exclusively to one jurisdiction — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill with specific coverage of EU and US frameworks.
The contract's own governing law clause determines which legal framework applies. The
review identifies the governing law early and adapts the analysis accordingly.

**Primary frameworks covered:**

- **EU**: VBER 2022 (Regulation 2022/720), TFEU Article 101, Vertical Guidelines
  (Commission Notice 2022/C 248/01), Geo-Blocking Regulation 2018/302
- **US**: Sherman Act 15 U.S.C. § 1, Leegin Creative Leather Products v. PSKS 551 U.S.
  877 (2007), Continental T.V. v. GTE Sylvania 433 U.S. 36 (1977), Colgate doctrine,
  Robinson-Patman Act 15 U.S.C. § 13, state law (California Cartwright Act, Maryland
  RPM statute)
- **IP**: Lanham Act 15 U.S.C. § 1127 (naked licensing / trademark abandonment)
- **Country-specific mandatory distribution law** (Belgium, France, Germany, Netherlands,
  Spain — see Termination section)

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- Mandatory distributor protection statutes (Belgium Law of 27 July 1961, French Commercial
  Code Art. L.442-1, German HGB §§ 89-89b by analogy)
- Local competition authority guidance and recent enforcement actions
- Antitrust notification or approval requirements for exclusivity arrangements
- Product liability and recall obligations for resellers under local law
- Consumer protection rules applicable to end-customer sales in the territory
- Local language requirements for agreements or labeling

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- Multiple valid approaches exist and the user's preference matters
- The competition law risk profile depends on market-share information only the user can provide
- Country-specific mandatory law triggers depend on identifying the distributor's territory

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

Accept the distribution or reseller agreement in any of these formats:

- **File**: PDF, DOCX, or other document format
- **URL**: Link to agreement in a CLM, cloud storage, or document system
- **Pasted text**: Agreement text pasted directly into the conversation

If no agreement is provided, prompt the user to supply one.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask the user these questions:

1. **Which side are you on?**
   - Options: Supplier/Manufacturer (appointing the distributor), Distributor/Reseller
     (being appointed), Other (e.g., reviewing for a third-party transaction)
   - _Why this matters_: The entire analysis flips. An MPC that harms a distributor
     benefits the supplier. Post-termination obligations that protect the supplier burden
     the distributor.

2. **Agreement type?**
   - Options: Exclusive distribution (sole rights in territory), Non-exclusive distribution
     (multiple distributors in territory), Selective distribution (qualitative network),
     Reseller/VAR agreement (for technology/software), OEM distribution, Other
   - _Why this matters_: Competition law treatment differs. Exclusive distribution
     qualifies for VBER 2022 active-sales protection; selective distribution has different
     hardcore restriction rules.

3. **Primary territory?**
   - Options: EU only, US only, EU + US (cross-border), Other (specify)
   - _Why this matters_: Determines which competition law framework governs hardcore
     restriction analysis.

4. **Market share information** (if available):
   - Does either the supplier or the distributor exceed 30% market share in the relevant
     product and geographic market?
   - Options: Both below 30% (VBER safe harbor likely applies), One or both above 30%
     (individual assessment needed), Unknown
   - _Why this matters_: Above 30%, the VBER 2022 safe harbor does not apply and every
     vertical restraint requires individual Article 101(3) TFEU assessment.

5. **Specific focus areas?**
   - Options: Territory and exclusivity, Minimum purchase commitments, Pricing / RPM risk,
     Termination and post-termination, Trademark/IP licensing, Competition law compliance,
     No specific focus — full review
   - Allow multiple selections.

6. **Deal context**: Deal value, strategic importance, territory population (new market vs.
   established), existing relationship, whether agreement is a draft or counterparty-issued
   form?
   - _Why this matters_: A distributor appointing its first small regional partner requires
     different treatment than a €50M exclusive distributor covering the entire EU.

### Step 3: Load the Playbook

Check for the organization's distribution agreement playbook in local settings (e.g.,
`legal.local.md` or similar configuration files).

The playbook should define standard positions for: MPC targets, exclusivity thresholds,
termination notice periods, trademark quality control standards, and competition law
compliance policies.

**If no playbook is configured:**

**⟁ CLARIFY** — Inform the user that no playbook was found, and ask:

- **Option A: Set up a playbook now** — Define standard positions for key distribution
  clauses (MPC levels, exclusivity performance thresholds, trademark quality standards,
  preferred termination notice periods, competition law compliance requirements). Slower
  upfront but makes future reviews precise.
- **Option B: Proceed with EU/US market standards** — Use market-standard EU/US
  distribution agreement positions as the baseline. Faster.
- **Option C: I'll provide positions as we go** — Start the review and ask about
  preferred positions when they matter for each clause.

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Read the governing law clause and identify the applicable jurisdiction. Then use
**legalcode-mcp** to build a working legal reference file.

**Research process:**

1. **Identify the governing law** from the agreement. For multi-territory distribution
   agreements, note that local mandatory law in each distribution territory may apply
   regardless of governing law choice.

   **⟁ CLARIFY** — If any of the following are true, ask before proceeding:
   - **No governing law clause**: Flag as RED deviation; ask which law the user expects.
   - **Governing law conflicts with distributor's territory**: For example, agreement
     governed by New York law but distributor covers Belgium — Belgian mandatory
     distribution law may apply regardless. Flag and confirm user is aware.
   - **EU distribution territory with US governing law**: Competition law compliance
     for EU territory requires EU/VBER analysis regardless of chosen governing law.

2. **Search legalcode-mcp** for:
   - VBER 2022 (Regulation 2022/720) and Vertical Guidelines provisions relevant to
     the restraints identified in the agreement
   - Sherman Act case law on vertical restraints (Sylvania, Leegin, Colgate, Robinson-Patman)
   - Country-specific mandatory distributor protection statutes for each territory covered
   - Lanham Act naked licensing case law if trademark license provisions are present
   - State law variations for US agreements (California Cartwright Act, Maryland RPM)

3. **Save results** to `/tmp/legalcode-distribution-review-authority.md`.

**If legalcode-mcp is not connected:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — manual verification required"`
- Proceed with analysis using the legal framework below, but flag that authority has
  not been independently verified

[JURISDICTION-SPECIFIC] For EU distribution agreements, confirm:

- Whether the agreement covers selective or exclusive distribution (different VBER rules)
- Market share of both supplier and distributor in the relevant market
- Whether online sales restrictions are included (VBER Art. 4(e) analysis mandatory)

### Step 5: Competition Law Screening

Before clause-by-clause review, run a competition law pre-screen. This is the most
material risk area in distribution agreements.

**EU VBER 2022 Hardcore Restriction Check (VBER Art. 4):**

Run through each restriction in the agreement. If any of the following are present,
immediately flag as **COMPETITION-RISK** (severity above RED — requires competition
counsel review):

| Restriction                                                               | VBER Article  | Impact if Present                      |
| ------------------------------------------------------------------------- | ------------- | -------------------------------------- |
| Fixed or minimum resale price (RPM)                                       | Art. 4(a)     | Entire agreement loses block exemption |
| Restriction on passive sales into exclusive territory                     | Art. 4(b)(i)  | Entire agreement loses block exemption |
| Restriction on passive sales to exclusive customer group                  | Art. 4(b)(ii) | Entire agreement loses block exemption |
| Restriction on active/passive sales to end users (selective distribution) | Art. 4(c)     | Entire agreement loses block exemption |
| Restricting cross-supply between network distributors                     | Art. 4(d)     | Entire agreement loses block exemption |
| Preventing effective use of the internet (absolute online ban)            | Art. 4(e)     | Entire agreement loses block exemption |

**⟁ CLARIFY** — If any COMPETITION-RISK items are found, pause and inform the user:

> "This agreement contains a potential hardcore restriction under EU VBER 2022 [Article X].
> If confirmed, the entire block exemption may be lost, requiring individual assessment
> under Article 101(1) and 101(3) TFEU and potentially exposing parties to fines of up to
> 10% of worldwide group turnover. I recommend pausing this review to obtain competition
> counsel advice on this specific clause before proceeding. Do you want me to (A) pause
> and flag this issue for competition counsel, (B) continue the review noting this as a
> critical issue, or (C) re-read the clause — I may have misinterpreted it?"

**US Sherman Act Section 1 Screening:**

Identify any per se illegal provisions:

- Minimum or fixed RPM in states where per se illegal (Maryland, potentially California)
  — flag as COMPETITION-RISK
- Horizontal territorial market division between competing distributors — flag as
  COMPETITION-RISK
- Any provision that could be characterized as a hub-and-spoke horizontal conspiracy
  (e.g., all distributors promised the same pricing floor by the supplier as a coordination
  mechanism) — flag as COMPETITION-RISK

For rule-of-reason restraints (territorial exclusivity, post-term non-competes, exclusive
dealing), classify as YELLOW or RED based on breadth and market-share context.

**Robinson-Patman Act screening (US):**

- Do tiered discount or pricing schedules discriminate between competing purchasers?
- Note: FTC Robinson-Patman enforcement resumed in December 2024 (wine/spirits) and
  January 2025 (PepsiCo/Walmart). Flag pricing structures that could raise Robinson-Patman
  risk as YELLOW with a [VERIFY] note. [VERIFY]

### Step 6: Clause-by-Clause Analysis

Analyze the agreement systematically. Read the entire agreement before flagging issues —
clauses interact (e.g., an MPC shortfall remedy may be affected by force majeure provisions).

**⟁ CLARIFY** — For long agreements (30+ pages, multiple schedules):

- Ask whether to perform a **full review** of all 18 clause categories, or a **priority
  review** focused on the user's stated focus areas plus any COMPETITION-RISK / RED items.
- If schedules incorporate territory-specific terms, ask whether to review all schedules.

Cover all 18 clause categories below:

| #   | Clause Category                       | Depth    | Key Review Points                                                     |
| --- | ------------------------------------- | -------- | --------------------------------------------------------------------- |
| 1   | Grant of Distribution Rights          | Deep     | Exclusivity type, territory definition, customer segments, carve-outs |
| 2   | Minimum Purchase Commitments          | Deep     | MPC level, measurement, shortfall remedy, take-or-pay, escalation     |
| 3   | Pricing, Discounts, and MFN           | Deep     | RPM risk, MFN scope (wide vs. narrow), max price, dual pricing        |
| 4   | Term and Renewal                      | Deep     | Initial term, renewal, auto-renewal notice, performance thresholds    |
| 5   | Termination and Post-Termination      | Deep     | Notice periods, mandatory law, good cause, inventory repurchase       |
| 6   | IP License (Trademarks / Trade Dress) | Deep     | Quality control, naked licensing risk, goodwill, sublicensing         |
| 7   | Marketing Obligations                 | Standard | Minimum spend, co-op funds, brand standards, approval process         |
| 8   | Competition Law Compliance            | Deep     | VBER compliance, non-compete duration, active/passive sales           |
| 9   | Channel Conflict / Dual Distribution  | Deep     | Supplier direct sales, information barriers, online/offline           |
| 10  | Limitation of Liability               | Standard | Cap amount, carveouts, consequential damages exclusion                |
| 11  | Indemnification                       | Standard | Scope, IP infringement, product liability, procedure                  |
| 12  | Representations and Warranties        | Standard | Product conformity, IP ownership, regulatory compliance               |
| 13  | Confidentiality                       | Standard | Scope, term, carveouts, return/destruction                            |
| 14  | Compliance and Regulatory             | Standard | Anti-bribery, sanctions, export control, modern slavery               |
| 15  | Reporting and Audit Rights            | Standard | Sales reporting, market data, audit frequency, cost allocation        |
| 16  | Governing Law and Dispute Resolution  | Standard | Jurisdiction, arbitration, mandatory territory law                    |
| 17  | Data Protection                       | Standard | Customer data collection, GDPR/CCPA, DPA requirement                  |
| 18  | Definitions and Boilerplate           | Standard | Key terms, order of precedence, entire agreement, amendments          |

---

## Clause Analysis Reference

### 1. Grant of Distribution Rights

**Key elements to review:**

- **Exclusivity type**: Exclusive (sole distributor in territory), semi-exclusive (supplier
  retains right to appoint limited others), non-exclusive (unlimited parallel distributors)
- **Territory definition**: Geographic precision (country, region, postal codes); whether
  online territory is defined; whether EU Geo-Blocking Regulation 2018/302 compliance is
  addressed [VERIFY]
- **Customer segment exclusivity**: B2B vs. B2C, key accounts, government/institutional
  carve-outs, named account reservation schedule
- **Distributor's exclusive-to-resell right**: Does the distributor get the products
  exclusively, or only distribution rights?
- **Supplier reservation rights**: Direct sales to end customers, key account carve-outs,
  e-commerce direct channel
- **Active vs. passive sales** (EU): Does the agreement correctly distinguish between
  active sales (restrictable) and passive sales (never restrictable under VBER Art. 4(b))?

**Common issues:**

- Territory defined so broadly it prevents genuine exclusivity or so narrowly it is
  commercially meaningless
- No mechanism to expand or contract territory based on performance
- Supplier reserve rights over e-commerce that effectively eliminate the territory value
- No schedule of named key accounts carved out, creating post-hoc disputes
- Passive sales restriction disguised as "territorial integrity" clause (hardcore restriction risk)

[JURISDICTION-SPECIFIC] **EU**: Under VBER 2022 Art. 4(b), exclusive territory may be
granted to up to five distributors. Active sales outside territory are restrictable; passive
sales are never restrictable. Online sales = passive sales unless geo-targeted. [VERIFY]

[JURISDICTION-SPECIFIC] **US**: Vertical territorial restrictions analyzed under rule of
reason since _Continental T.V. v. GTE Sylvania_, 433 U.S. 36 (1977). Horizontal territorial
divisions between competing distributors remain per se illegal. [VERIFY]

**Classification triggers:**

- Passive sales restriction → COMPETITION-RISK
- No territory definition → RED
- Vague territory with no map or schedule → YELLOW
- Supplier's direct e-commerce competing with distributor's exclusive territory → YELLOW

---

### 2. Minimum Purchase Commitments

**Key elements to review:**

- **MPC structure**: Fixed annual minimum, rolling 12-month forecast, tiered discount with
  volume incentives, take-or-pay
- **Measurement period**: Annual, quarterly, cumulative; how partial years are prorated
- **Performance threshold**: Typically 80% of MPC constitutes compliance; below triggers
  remedies
- **Shortfall remedy**: Loss of exclusivity (conversion to non-exclusive), cure period,
  take-or-pay payment, termination
- **Ramp-up structure**: Year 1 lower minimums growing to steady-state Year 3+
- **Force majeure relief**: Does prolonged supply disruption suspend MPC obligations?
- **Supplier's ability to set MPC**: Unilateral right to adjust MPC vs. bilateral amendment
- **Liquidated damages for shortfall**: If present, assess against penalty doctrine

**Common issues:**

- MPC set at supplier's aspirational sales target rather than realistic commercial baseline
- No ramp-up period for new markets where distributor must build brand from zero
- Shortfall remedy is automatic termination rather than loss of exclusivity (disproportionate)
- Take-or-pay clause in goods contracts where liquidated amount is full contract price
  rather than lost margin — risk of unenforceability as a penalty
- No force majeure carve-out from MPC, exposing distributor to shortfall liability for
  supply chain disruptions the supplier caused

**Penalty doctrine assessment:**

[JURISDICTION-SPECIFIC] **US (UCC § 2-718)**: Liquidated damages enforceable only if
"reasonable in the light of the anticipated or actual harm." Shortfall damages = full
contract value (not just lost margin) risk being struck as an unenforceable penalty. [VERIFY]

[JURISDICTION-SPECIFIC] **EU civil law**: French courts may reduce excessive penalty clauses
under Civil Code Art. 1231-5; German courts apply §§ 339-345 BGB requiring reasonable
relationship between penalty and protected interest. [VERIFY]

**Best practice**: Tie liquidated shortfall amount to lost gross margin on the undelivered
volume, not to the full purchase price.

**Classification triggers:**

- MPC with take-or-pay at full contract price → RED (penalty risk)
- No MPC (exclusive distribution without any performance obligation) → YELLOW
- MPC with automatic termination as sole shortfall remedy → YELLOW
- MPC without force majeure carve-out → YELLOW

---

### 3. Pricing, Discounts, and MFN

**Key elements to review:**

- **Resale price maintenance (RPM)**: Any clause fixing or setting a minimum resale price
  is the highest-risk provision in any distribution agreement
- **Maximum/recommended prices**: Maximum resale prices are permitted (EU VBER Art. 4(a);
  US rule of reason). Non-binding recommended prices are permitted. [VERIFY]
- **Wholesale pricing**: Supplier's right to change wholesale prices; notice period for
  price changes; distributor's right to purchase at pre-change prices for existing commitments
- **Most Favored Nation (MFN)**: Wide MFN (no better prices anywhere) vs. narrow MFN
  (no better prices in supplier's own direct channel)
- **Dual pricing**: Different wholesale prices for online vs. offline channeled goods —
  permitted under VBER 2022 only if reflecting genuine investment-level differences
- **Tiered discounts**: Volume-based discount structures; Robinson-Patman compliance
  for US multi-distributor arrangements

**Competition law matrix:**

| Clause Type                             | EU Status                                                                  | US Status                                                                                     |
| --------------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Fixed/minimum RPM                       | HARDCORE (Art. 4(a)) — agreement loses exemption                           | Rule of reason federally; per se in Maryland; California uncertain [VERIFY]                   |
| Maximum RPM                             | Permitted                                                                  | Rule of reason; rarely found anticompetitive                                                  |
| Recommended prices                      | Permitted                                                                  | Permitted (Colgate doctrine if unilateral)                                                    |
| Wide MFN (all channels)                 | Excluded restriction (Art. 5(1)(d) for OIS) — individual assessment needed | Rule of reason; per se if part of hub-and-spoke horizontal conspiracy (_Apple_, 2d Cir. 2015) |
| Narrow MFN (own channel only)           | Block-exempted below 30%                                                   | Rule of reason                                                                                |
| Dual pricing (genuine investment basis) | Permitted under VBER 2022                                                  | Generally permitted                                                                           |

**Common issues:**

- Supplier imposes "suggested" resale prices with contractual consequences for deviation
  (functionally = minimum RPM)
- Supplier monitors resale prices via algorithms and threatens termination to non-compliant
  distributors (RPM by indirect means — loses _Colgate_ protection in US)
- Wide MFN clause preventing distributor from offering lower prices on competing platforms
  (EU excluded restriction; US potential per se risk in platform contexts)
- Price change notice period too short for distributor to manage existing customer commitments
- Tiered discounts that discriminate between similarly-situated distributors (Robinson-Patman)

**Classification triggers:**

- Any fixed/minimum RPM clause → COMPETITION-RISK
- Wide MFN imposed by supplier on distributor → RED (EU) / YELLOW (US) with [VERIFY]
- No price change notice period → YELLOW
- No most-favored pricing protection for distributor → YELLOW
- Algorithmically monitored pricing compliance → YELLOW / COMPETITION-RISK depending on facts

---

### 4. Term and Renewal

**Key elements to review:**

- **Initial term**: Adequacy relative to distributor's required investment payback period
- **Auto-renewal**: Notice period for non-renewal; who triggers renewal; evergreen risk
- **Performance-linked renewal**: Right to renew conditional on meeting MPC
- **Renewal MPC**: Whether MPC is renegotiated or rolls over automatically
- **Right of first refusal on renewal**: Does existing distributor have right to match
  any competing offer?

**Common issues:**

- Short initial term (1-2 years) for a territory requiring significant upfront distributor
  investment (3-5 years minimum is market standard for new markets)
- Auto-renewal with short notice window (30 days) making non-renewal practically difficult
- Evergreen renewal with MPC escalation that compounds without bilateral review
- No performance-based renewal right for distributor who has exceeded MPC targets

**Classification triggers:**

- Initial term < 2 years with substantial required investment → RED
- Auto-renewal notice < 60 days → YELLOW
- No termination for convenience after initial term → YELLOW
- Supplier right to change MPC unilaterally at renewal → YELLOW

---

### 5. Termination and Post-Termination

This is typically the most legally complex section for EU distribution agreements due to
mandatory country-specific protections that cannot be contracted away.

**Key elements to review:**

- **Notice period**: Contractual notice for convenience termination; for-cause termination
  rights; cure periods
- **EU mandatory country law** (applies regardless of governing law choice in many cases):
- **Inventory repurchase**: Supplier obligation to repurchase unsold inventory post-termination;
  repurchase price formula; condition standards; return logistics
- **Transition assistance**: Post-termination sell-down period; continued access to supply
  during transition; customer notification obligations
- **Post-termination non-compete**: Duration, territory, scope, know-how nexus
- **Customer data**: Transfer of customer database to supplier on termination
- **IP reversion**: Cessation of trademark use; run-out period for existing inventory

**EU Mandatory Country Law Matrix (applies regardless of governing law):**

| Country         | Statute                                       | Protection                                                  | Notice Required                                                  | Compensation                                                                  |
| --------------- | --------------------------------------------- | ----------------------------------------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Belgium**     | Law of 27 July 1961 on Exclusive Distribution | Exclusive and quasi-exclusive distributors                  | Up to **36 months**                                              | Client indemnity up to 18 months' gross profit + staff / investment costs     |
| **France**      | Commercial Code Art. L.442-1, II              | All commercial relationships                                | Proportional to relationship length; 18 months deemed reasonable | None (no goodwill indemnity for distributors)                                 |
| **Germany**     | HGB §§ 89-89b (by analogy)                    | Integrated distributors obligated to transfer customer data | 1 month per year of agreement, max **6 months**                  | Goodwill indemnity up to 1 year's avg. annual margin (new customers) [VERIFY] |
| **Netherlands** | Franchise Law (Wet franchise, 2021)           | Franchise-like distribution relationships                   | Varies                                                           | Goodwill compensation; law still developing [VERIFY]                          |
| **Spain**       | Real Decreto 1438/1985 (by analogy)           | Integrated distributors                                     | Varies                                                           | Goodwill compensation analogous to commercial agent [VERIFY]                  |

**⟁ CLARIFY** — When the distributor's territory includes Belgium, France, or Germany,
ask the user: "The territory covered by this agreement includes [country], which has
mandatory distributor protection law that applies regardless of the agreement's governing
law. The contractual notice period of [X] may be insufficient. Do you want me to assess
whether the contractual provisions comply with the applicable mandatory law?"

**Inventory repurchase review:**

[JURISDICTION-SPECIFIC] **US**: No general common-law obligation to repurchase distributor
inventory. Some states have specific dealer protection statutes (Georgia § 13-8-22 for
terminated distributors, Florida Chapter 686 for certain industries). Check state law for
each US territory. [VERIFY]

[JURISDICTION-SPECIFIC] **EU**: No uniform EU obligation; country-specific law and
individual contract terms govern. Best practice: express repurchase provision specifying
buyback price (cost price or cost price minus handling fee), condition standards, and
timeframe for return.

**Post-termination non-compete assessment:**

[JURISDICTION-SPECIFIC] **EU (VBER 2022 Art. 5(1)(b))**: Post-termination non-competes
permitted only where: (i) ≤ 1 year duration after termination; (ii) purpose = protection
of know-how transferred by supplier; (iii) geographic scope limited to operated territory;
(iv) subject matter limited to competing goods/services. [VERIFY]

[JURISDICTION-SPECIFIC] **US**: State law analysis required. Courts apply reasonableness
test (duration, geographic scope, legitimate interest, adequate consideration). FTC's 2024
broad non-compete ban was enjoined (N.D. Tex., August 2024); state-law analysis controls. [VERIFY]

**Classification triggers:**

- Belgian territory with notice period < 36 months → RED
- French territory with notice period < proportional to relationship duration → YELLOW
- German territory, integrated distributor, no goodwill indemnity addressed → YELLOW
- No inventory repurchase obligation → YELLOW
- Post-termination non-compete > 1 year in EU territory → COMPETITION-RISK (automatically
  severs from VBER exemption)
- No IP reversion / run-out period defined → YELLOW
- No customer data transfer mechanism on termination → YELLOW

---

### 6. IP License (Trademarks / Trade Dress)

**Key elements to review:**

- **Scope of license**: Products, territory, term, permitted uses
- **Quality control provisions**: Contractual quality standards; inspection and audit rights;
  approval process for marketing materials and product presentation
- **Naked licensing risk**: Adequate quality control is mandatory for trademark validity
- **Goodwill**: Express statement that goodwill from distributor's use accrues to licensor
- **Sublicensing**: Restrictions on sublicensing to sub-distributors
- **Trade dress**: If applicable, quality standards for trade dress presentation
- **License termination**: Automatic termination of license on agreement termination; no
  survival of license
- **Modifications**: Prohibition on unauthorized product modification, repackaging, or
  co-branding

**Naked Licensing Risk Analysis (Lanham Act 15 U.S.C. § 1127):**

A trademark owner who licenses without maintaining adequate quality control risks
**trademark abandonment** — the mark becomes unenforceable and all trademark rights
are forfeited.

**Three-factor quality control test:**

1. Did the trademark owner **retain contractual rights** over quality?
2. Did the trademark owner **actually exercise** quality control (in practice, not just
   on paper)?
3. Could the trademark owner **reasonably rely** on the licensee's internal standards
   (e.g., pre-existing relationship, regulatory framework requiring compliance)?

**Mandatory quality control provisions checklist:**

- [ ] Express quality standards (minimum grade/quality of goods or services)
- [ ] Right to inspect premises and goods (at licensor's cost or shared cost)
- [ ] Approval process for use of marks in non-standard contexts
- [ ] Annual certification of compliance with brand guidelines
- [ ] Prohibition on sublicensing without prior written consent
- [ ] Obligation to report product defects or complaints affecting mark reputation
- [ ] Right of licensor to withdraw approval and require cessation if quality fails

**Leading naked licensing cases (US):**

- _Barcamerica International USA Trust v. Tyfield Importers_: wine brand abandoned due
  to failure to maintain quality control [VERIFY]
- _FreecycleSunnyvale v. The Freecycle Network_ (9th Cir. 2010): insufficient contractual
  quality control provisions led to naked licensing finding [VERIFY]

**Common issues:**

- Trademark license clause stating only "distributor shall use marks in accordance with
  brand guidelines" with no audit rights or quality standards — legally insufficient for
  quality control under US naked licensing doctrine
- No explicit goodwill statement (all goodwill inures to licensor's benefit)
- License scope not limited to agreement term — risk of arguing license survives termination
- No approval process for co-branded marketing (joint events, third-party promotions)
- Blanket sublicensing permitted to sub-distributors without quality control flow-down

**Classification triggers:**

- No quality control provisions in trademark license → RED (naked licensing risk)
- No audit rights over quality → RED
- No goodwill statement → YELLOW
- Blanket sublicensing permitted → YELLOW
- License scope extends beyond agreement term → YELLOW
- No approval process for marketing materials → YELLOW

---

### 7. Marketing Obligations and Brand Standards

**Key elements to review:**

- **Minimum marketing spend**: Amount or percentage of projected net sales (market standard
  2–5%); annual schedule; eligible activities; reporting obligations
- **Market Development Funds (MDF) / Co-op**: Supplier contribution amount; trigger
  (performance-based vs. automatic); claim process; proof of performance; recapture of
  unused funds
- **Brand standards compliance**: Reference to brand guidelines; approval process for
  non-standard use; digital/social media usage rules
- **Marketing approval**: Pre-approval requirement for significant campaigns; supplier
  turnaround time; consequence of silence
- **Reporting**: Frequency of marketing activity reports; market intelligence sharing

**Common issues:**

- Minimum marketing spend obligation but no corresponding supplier obligation to provide
  MDF or marketing support
- No turnaround time for supplier approval of marketing materials — effectively a veto
  right that can be used to obstruct distributor's marketing
- MDF recapture clause that takes back unused funds with no carryover, creating a
  "use-it-or-lose-it" dynamic that prevents strategic marketing timing
- Distributor required to maintain social media accounts but no guidance on tone, content,
  or how to handle crisis communications

**Classification triggers:**

- Marketing spend obligation with no supplier MDF contribution → YELLOW
- No brand guidelines referenced in the agreement → YELLOW
- Unlimited approval right with no deemed-approval after silence → YELLOW

---

### 8. Competition Law Compliance Covenants

**Key elements to review:**

- **Non-compete during agreement (single-branding / exclusive purchasing)**:
  - EU VBER: permitted for up to 5 years; covers 80%+ sourcing requirement [VERIFY]
  - US: rule of reason; permissibility depends on market share and duration
- **Post-termination non-compete**: See Termination section (§5)
- **Online sales restrictions**: Marketplace bans; quality standards for e-commerce;
  geo-blocking obligations (EU: check against Geo-Blocking Regulation 2018/302)
- **Active vs. passive sales obligations**: What the distributor is required to do actively
  vs. what it cannot do actively outside its territory
- **Price communication restrictions**: Prohibition on sharing pricing information with
  other distributors in the network (horizontal information exchange risk)
- **Compliance policy references**: Does the agreement require VBER/Sherman Act compliance?
  Is there a competition law compliance policy appendix?

**Online sales restriction matrix (EU, VBER 2022):**

| Restriction                                                         | Status                                                         |
| ------------------------------------------------------------------- | -------------------------------------------------------------- |
| Prohibit all internet sales                                         | HARDCORE — Article 4(e)                                        |
| Require specific online marketplace absence (e.g., no Amazon sales) | Permitted                                                      |
| Require minimum online service standards                            | Permitted                                                      |
| Require offline-minimum as condition for online permission          | HARDCORE — Article 4(e)                                        |
| Dual pricing with genuine investment basis                          | Permitted                                                      |
| Geo-blocking requirements (forcing local domains)                   | Potentially violates Geo-Blocking Regulation 2018/302 [VERIFY] |
| Maximum online price ceiling                                        | Permitted                                                      |

**Common issues:**

- Agreement requires distributor to sell on supplier's own marketplace platform exclusively
  (limits competition on that platform — OIS exclusion from VBER may apply)
- Distributor prohibited from responding to unsolicited online orders from outside territory
  (passive sales restriction — hardcore)
- Non-compete obligation has no end date and tacitly renews past 5-year VBER limit
- No competition law compliance covenant requiring distributor to comply with applicable
  antitrust law

**Classification triggers:**

- Prohibition on all internet sales → COMPETITION-RISK
- Online-only minimum sales requirements as condition of internet permission → COMPETITION-RISK
- In-territory non-compete > 5 years → COMPETITION-RISK (VBER excluded restriction)
- No competition law compliance covenant → YELLOW

---

### 9. Channel Conflict and Dual Distribution

**Key elements to review:**

- **Supplier direct sales**: Does the supplier sell direct to end customers in the
  distributor's territory? Is this permitted? How are direct sales accounted for?
- **Key account reservation**: Supplier-reserved key accounts that the distributor cannot
  serve; schedule of named accounts required
- **E-commerce direct channel**: Supplier's own e-commerce competing with distributor's
  exclusive territory (most common channel conflict point)
- **Information barriers**: Dual distribution firewall — prohibition on competitively
  sensitive information (distributor's customer lists, pricing, sales pipeline) flowing
  to supplier's B2C/direct sales team
- **Dispute resolution for channel conflict**: Process when supplier and distributor compete
  for the same customer

**EU dual distribution treatment (VBER 2022):**

- Dual distribution (supplier also competing at retail level) remains block-exempted below
  30% threshold with an important restriction: information exchanged must be (i) directly
  related to implementing the vertical agreement and (ii) necessary to improve production
  or distribution. Competitively sensitive intelligence (customer lists, pricing data,
  sales pipeline) shared with the supplier's competing retail team is NOT exempted. [VERIFY]

**US dual distribution treatment:**

- Not per se problematic but creates channel conflict. Supplier acting as a competing
  distributor occupies a horizontal level; information shared creates risk of a horizontal
  conspiracy characterization. Contractual information barriers are advisable.

**Common issues:**

- No key account schedule — disputes guaranteed when supplier sells direct to a customer
  the distributor has been cultivating
- No information barrier between supplier's sales analytics (from distributor's monthly
  reports) and supplier's direct sales team in a dual distribution context
- Supplier's e-commerce platform ships to distributor's exclusive territory without
  territorial compensation (margin support, carve-out payment)
- No dispute resolution mechanism for channel conflict — escalation to termination by default

**Classification triggers:**

- Dual distribution with no information barrier → YELLOW (EU) / COMPETITION-RISK (if
  clearly competitively sensitive data flows to competing retail team)
- No key account schedule in a claimed exclusive arrangement → RED
- Supplier e-commerce competing with exclusive distributor, no compensation mechanism → YELLOW

---

### 10. Limitation of Liability

**Key elements to review:**

- Cap amount (fixed fee multiple, contract value, insurance coverage amount)
- Whether mutual or applies asymmetrically
- Carveouts from cap (death/bodily injury, fraud, IP indemnity, confidentiality breach)
- Consequential, indirect, special, punitive damages exclusion
- Whether the exclusion is mutual

**Distribution-specific issues:**

- Product liability claims that exceed any reasonable liability cap — caps on indemnification
  for product defects vs. regulatory product recall liability exposure
- MPC shortfall claims that could aggregate to full contract value if distributor converts
  unsold inventory multiple periods

[JURISDICTION-SPECIFIC] Check whether statutory reasonableness tests apply to exclusion
clauses: UCTA 1977 (England), Reasonableness (US unconscionability), BGB § 309 (Germany),
Code Civil Art. 1170 (France). [VERIFY]

**Classification triggers:**

- No limitation of liability clause → RED
- Asymmetric cap strongly favoring supplier → YELLOW
- No consequential damages exclusion → YELLOW
- Product liability excluded from cap entirely (supplier-side) → RED (for distributor)

---

### 11. Indemnification

**Key elements to review:**

- **Product liability indemnification**: Who bears liability for defective products sold
  into the territory? Is the supplier required to indemnify the distributor for product
  defect claims from end customers?
- **IP infringement indemnification**: Supplier indemnity for use of supplier's trademarks
  and products not infringing third-party IP
- **Regulatory non-compliance indemnification**: Indemnity for supplier's failure to meet
  applicable regulatory standards (CE marking, product safety, labeling)
- **Distributor indemnification obligations**: Distributor indemnifies for own conduct,
  marketing claims, distribution methods

**Common issues:**

- No product liability indemnification from supplier to distributor — distributor exposed
  to end-customer product defect claims for supplier's own defective products
- IP indemnification carve-out that removes protection when distributor has modified
  packaging or combined products — carve-out may be broader than the actual risk
- No clear procedure (notice, control of defense, cooperation requirements)

**Classification triggers:**

- No product liability indemnification from supplier → RED (for distributor)
- No IP infringement indemnification from supplier for use of licensed marks → YELLOW
- Unilateral indemnification with no cap → YELLOW

---

### 12–18. Standard Clause Checklist

For these categories, review presence, reasonableness, and market alignment. Flag using
GREEN/YELLOW/RED.

**12. Representations and Warranties**

- [ ] Supplier warrants products conform to specifications and applicable regulations
- [ ] Supplier warrants it owns / has right to sublicense the IP being licensed
- [ ] Distributor warrants it is legally authorized to distribute in the territory
- [ ] Mutual warranties of authority and legal capacity to enter the agreement
- [ ] Product safety compliance warranties (EU product safety regulations, US CPSC)
- [ ] No regulatory approvals needed / all regulatory approvals already obtained
- [ ] Survival period defined (typically 2-3 years post-termination for warranty claims)

**13. Confidentiality**

- [ ] Scope covers commercial terms, customer data, pricing, and business information
- [ ] Standard carveouts present (public domain, independent development, required by law)
- [ ] Term: at least 3 years; indefinite for trade secrets
- [ ] Return or destruction on termination
- [ ] Permitted disclosures to affiliates, advisors, and financing parties (under NDA)
- [ ] Special treatment for customer database shared with supplier under reporting obligations

**14. Compliance and Regulatory**

- [ ] Anti-bribery / anti-corruption representations and compliance obligations
- [ ] Sanctions and export control compliance (OFAC, BIS, EU sanctions)
- [ ] Modern slavery / human trafficking statement (required in UK and Australia, recommended globally)
- [ ] Product safety and labeling compliance in each distribution territory
- [ ] Regulatory approvals and import/customs compliance obligations
- [ ] Consequences of compliance breach (termination trigger, indemnification)

**15. Reporting and Audit Rights**

- [ ] Sales reporting frequency (monthly is standard for active relationships)
- [ ] Content of reports: units sold, revenue, customer name/segment, territory breakdown
- [ ] Market intelligence sharing: competitive activity, pricing trends, customer feedback
- [ ] Audit rights: who can audit, at whose cost, frequency, notice period, dispute process
- [ ] Customer database maintenance obligations and format standards
- [ ] Consequences of reporting failures (material breach trigger?)

**16. Governing Law and Dispute Resolution**

- [ ] Governing law clause present and unambiguous
- [ ] Dispute resolution: litigation vs. arbitration; if arbitration, institutional rules
- [ ] Mandatory territory law carve-out (acknowledges local mandatory law applies)
- [ ] Escalation provisions before formal dispute (negotiation, mediation)
- [ ] Emergency relief provisions (injunctive relief availability)

**17. Data Protection**

- [ ] Whether distributor collects personal data of end customers
- [ ] If yes: Is distributor the data controller? Does supplier need to be notified?
- [ ] GDPR compliance obligations for EU territory (data controller vs. processor analysis)
- [ ] CCPA compliance obligations for California end customers
- [ ] Cross-border data transfer mechanisms if customer data leaves the territory
- [ ] Data breach notification obligations (to supplier and to regulators)
- [ ] Data deletion or return obligations on termination

**18. Definitions and Boilerplate**

- [ ] "Products" definition: exhaustive list or category-based? Supplier's right to
      modify product range?
- [ ] "Territory" definition: precise, unambiguous geographic scope
- [ ] "Competing Products" definition: clear enough to evaluate non-compete scope
- [ ] Entire agreement clause present
- [ ] Severability clause (especially important for competition law — a severable
      excluded restriction should not void the entire agreement)
- [ ] Order of precedence: if multiple documents, which governs on conflict
- [ ] Amendments: written only; oral modifications excluded

---

## Missing Clause Detection

After analyzing present clauses, check for entirely absent provisions:

**Material gaps in distribution agreements:**

| Missing Clause                            | Severity | Assessment                                                                    |
| ----------------------------------------- | -------- | ----------------------------------------------------------------------------- |
| No territory definition                   | RED      | Agreement is commercially unworkable and legally uncertain                    |
| No exclusivity type specified             | RED      | Creates fundamental uncertainty about the business relationship               |
| No MPC (in exclusive distribution)        | YELLOW   | Exclusivity without performance obligation is a one-sided burden on supplier  |
| No trademark license quality control      | RED      | Naked licensing risk — trademark abandonment                                  |
| No inventory repurchase obligation        | YELLOW   | Distributor exposed to stranded inventory risk on termination                 |
| No competition law compliance covenant    | YELLOW   | Both parties exposed to regulatory risk without express compliance obligation |
| No mandatory territory law acknowledgment | YELLOW   | Creates false sense of security about governing law choice                    |
| No channel conflict resolution mechanism  | YELLOW   | Disputes likely in dual distribution without defined escalation path          |
| No product liability indemnification      | RED      | Distributor bears supplier's product defect risk                              |
| No reporting obligations                  | YELLOW   | Supplier cannot manage or support the distribution network                    |

---

## Deviation Severity Classification

### GREEN — Acceptable

Clause aligns with or is better than the organization's standard position. Minor variations
that are commercially reasonable and do not materially increase risk.

**Distribution-specific examples:**

- MPC set at 90% of distributor's own sales forecast (self-imposed target is easier to achieve)
- Notice period for termination for convenience is 4 months when standard is 3 months
- Governing law in an adjacent commercial jurisdiction with equivalent protections

**Action**: Note for awareness. No negotiation needed.

### YELLOW — Negotiate

Clause falls outside the standard position but within a negotiable range. Requires
attention and likely negotiation, but not escalation.

**Distribution-specific examples:**

- Shortfall remedy is automatic termination rather than loss of exclusivity
- Wide MFN clause with no carve-out for the distributor's own promotional activities
- Post-termination trademark use during sell-down limited to 60 days (standard is 90-120 days)
- Marketing spend obligation with no corresponding MDF from supplier

**Action**: Generate specific redline language. Provide fallback position.

### RED — Escalate

Clause falls outside the acceptable range, triggers a defined escalation criterion, or
poses material risk. Requires senior counsel or business decision-maker sign-off.

**Distribution-specific examples:**

- No trademark license quality control (naked licensing risk, trademark abandonment)
- No product liability indemnification from supplier to distributor
- Belgian or French territory with contractual notice period materially below mandatory minimum
- No limitation of liability clause

**Action**: Explain specific risk (citing legal basis). Provide market-standard alternative.
Recommend escalation path.

### COMPETITION-RISK — Stop / Seek Competition Counsel

The clause is a potential hardcore restriction or per se illegal provision. The agreement
may be void or unenforceable. Fines and damages exposure can be severe.

**Examples:**

- Fixed or minimum resale price (EU VBER Art. 4(a) / US per se in some states)
- Restriction on passive sales into exclusive territory (EU VBER Art. 4(b)(i))
- Absolute prohibition on internet sales (EU VBER Art. 4(e))
- Post-termination non-compete > 1 year in EU territory (VBER Art. 5 excluded restriction)

**Action**: Pause review. Escalate to competition counsel immediately. Flag the specific
clause and applicable legal provision. Do not proceed with other redlines until this is
resolved — a void agreement invalidates all other negotiated positions.

---

## Redline Format

For each redline:

```
**Clause**: [Section reference and clause name]
**Current language**: "[exact quote from the agreement]"
**Proposed redline**: "[specific alternative language]"
**Rationale**: [1-2 sentences explaining why, suitable for external sharing]
**Legal basis**: [Relevant statute, regulation, or principle — or "General commercial
practice" — or mark [VERIFY] if not independently confirmed]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative position if primary redline is rejected]
```

### Redline Best Practices

1. **Be specific**: Exact language ready to insert, not vague guidance.
2. **Address competition law first**: Never let negotiation of secondary issues distract
   from COMPETITION-RISK items.
3. **Provide fallback positions**: Especially for YELLOW items. A redline with no fallback
   is a dead end.
4. **Cite authority**: For COMPETITION-RISK items, cite the specific VBER article or
   Sherman Act case. Mark unverified citations [VERIFY].
5. **Acknowledge mandatory law**: When redlining termination provisions for EU territories,
   cite the specific mandatory country statute, not just general market practice.
6. **Adjust tone to relationship**: New distributor (neutral/firm); strategic long-term
   partner (collaborative); must-have channel (accommodating on nice-to-haves).

---

## Negotiation Priority Framework

### Tier 1 — Must-Haves (Deal Breakers)

Issues where the organization cannot proceed without resolution:

- COMPETITION-RISK provisions (hardcore restrictions, per se illegal clauses)
- No trademark license quality control (naked licensing / trademark abandonment)
- No product liability indemnification from supplier (for distributor side)
- Territory definition absent or fatally ambiguous
- EU/Belgian mandatory notice period violations
- No limitation of liability clause
- MPC shortfall remedy = automatic termination with full-price liquidated damages

### Tier 2 — Should-Haves (Strong Preferences)

Issues that materially affect risk but have negotiation room:

- MPC levels and ramp-up structure
- Inventory repurchase obligation and price formula
- Post-termination transition period (trademark use, inventory sell-down)
- Competition law compliance covenant
- Key account schedule for dual distribution
- Product liability indemnification cap and procedure
- Reporting obligations scope and frequency

### Tier 3 — Concession Candidates

Issues that improve the position but can be conceded strategically:

- Marketing MDF amount
- Audit frequency
- Preferred governing law (if alternative is acceptable)
- Notice period preferences within mandatory minimum
- Boilerplate refinements

**Strategy**: Lead with Tier 1 (COMPETITION-RISK + trademark quality control first).
Use Tier 3 concessions to secure Tier 2 wins. Never concede Tier 1 without senior
counsel and business decision-maker sign-off.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                      | Fail Action                                                          |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Source**     | Every competition law claim cites a specific regulation, statute, or case                                                                 | Add citation or mark "[UNVERIFIED — competition counsel to confirm]" |
| **Format**     | All EU citations reference Regulation and Article; all US citations include case name and reporter                                        | Fix format                                                           |
| **Currency**   | VBER 2022 is the current regulation (in force June 1, 2022). State law varies — confirm current status for each state. [VERIFY]           | Flag "[CHECK CURRENCY — may have been amended]"                      |
| **Domain**     | Analysis stays within the agreement's governing law. Do not apply EU competition law to purely US arrangements or vice versa              | Remove or flag jurisdictional bleed                                  |
| **Confidence** | Uncertainty explicitly stated. Competition law is particularly fact-specific; many positions depend on market share and market definition | Add confidence qualifier                                             |

### Self-Interrogation for RED and COMPETITION-RISK Items

For any clause classified RED or COMPETITION-RISK, apply this 3-pass review before
delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the risk assessment follow logically from the statute/regulation/case cited?
- For VBER analysis: is the 30% market share threshold actually exceeded? If unknown,
  have I stated that the analysis assumes it is met?
- For naked licensing: have I confirmed the agreement actually fails to provide adequate
  quality control, or just that quality control provisions are sparse?

**Pass 2 — Completeness**:

- Have all applicable competition frameworks been considered (EU VBER, US Sherman Act,
  Robinson-Patman, state antitrust law)?
- Have I considered all country-specific mandatory distribution laws for each distribution
  territory?
- Are there regulatory dimensions (product safety, import licensing, data protection) not
  yet addressed?

**Pass 3 — Challenge**:

- What is the strongest argument that this clause IS acceptable?
- Under VBER 2022: is there an individual exemption argument under Art. 101(3) TFEU?
- Under US law: is this a unilateral supplier policy under _Colgate_ rather than an
  agreement?
- Is the RED classification proportionate, or is this actually YELLOW with documented
  mitigations?

If any pass reveals a weakness, revise before delivery. Mark the audit trail with
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material clause analysis, assign a confidence level:

| Level        | Range     | Meaning                                                                                                                 | Action                                                            |
| ------------ | --------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled law, clear statute, no ambiguity (e.g., VBER Art. 4(a) RPM is a hardcore restriction)                           | State with confidence                                             |
| **High**     | 0.80-0.94 | Strong authority, minor interpretation questions (e.g., Belgian 36-month notice is mandatory)                           | State with brief caveat                                           |
| **Probable** | 0.60-0.79 | Good arguments but reasonable minds could differ (e.g., wide MFN's effect under US rule of reason in this fact pattern) | State with explicit reasoning and contra-indicators               |
| **Possible** | 0.40-0.59 | Genuinely uncertain (e.g., whether German goodwill indemnity applies to this particular distributor structure)          | Flag for competition counsel review with both sides               |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative                                                                                                 | Do not assert; flag "[UNCERTAIN — competition counsel to advise]" |

---

## Glass Box Audit Trail

Every distribution agreement review output MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-distribution-agreement-review"
  agreement: "[Agreement title and date]"
  agreement_type: "[Exclusive / Non-exclusive / Selective / Reseller / OEM]"
  user_side: "[Supplier / Distributor / Reviewing for third party]"
  governing_law: "[Jurisdiction identified from the agreement]"
  territory: "[Distribution territory covered]"
  playbook_used: "[Playbook name or 'EU/US market standards']"
  clauses_reviewed: 18
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  competition_risk_items: "[number] — [list VBER articles / statutes triggered]"
  mandatory_country_law_triggered: "[Belgium / France / Germany / None / [Other]]"
  trademark_license_present: "[Yes / No]"
  naked_licensing_risk: "[HIGH / MEDIUM / LOW / N/A — rationale]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to temp file or 'Not created']"
  statutes_consulted:
    - "VBER 2022 (Regulation 2022/720) — [VERIFIED / UNVERIFIED]"
    - "Sherman Act 15 U.S.C. § 1 — [VERIFIED / UNVERIFIED]"
    - "[Additional statutes]"
  case_law_consulted:
    - "[Case name, citation — VERIFIED / UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED/COMPETITION-RISK items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
    - "Market share data not provided — VBER safe harbor analysis is conditional"
  reviewer: "AI-assisted — requires qualified distribution and competition law counsel"
```

---

## Multi-Stakeholder Mapping

For every distribution agreement, identify all affected stakeholders:

| Stakeholder                   | Role                       | Affected Clauses                       | Impact             | Action Required                         |
| ----------------------------- | -------------------------- | -------------------------------------- | ------------------ | --------------------------------------- |
| Supplier / Manufacturer       | Primary party              | All clauses                            | Primary            | Sign / Negotiate                        |
| Distributor / Reseller        | Primary party              | All clauses                            | Primary            | Sign / Negotiate                        |
| End customers (territory)     | Third party                | Product warranty, liability, data      | Indirect           | Consumer protection compliance          |
| Sub-distributors              | Third party (if permitted) | IP license, competition law            | Indirect           | Non-compete / quality control flow-down |
| Competition authority (EU/US) | Regulator                  | Competition law clauses                | Enforcement        | VBER compliance verification            |
| Product safety regulator      | Regulator                  | Product compliance, recall             | Enforcement        | Regulatory approvals required           |
| Data subjects                 | Third party                | Data protection (if customer data)     | Indirect           | GDPR / CCPA compliance                  |
| Supplier's direct sales team  | Internal                   | Channel conflict, dual distribution    | Internal conflict  | Information barriers required           |
| Finance (distributor)         | Internal                   | MPC, take-or-pay, inventory repurchase | Capital commitment | FP&A modeling of MPC exposure           |

---

## Anti-Patterns

Explicit catalogue of what NOT to do in distribution agreement review:

1. **Skipping competition law screening** — Reviewing a distribution agreement clause by
   clause without first running the VBER Art. 4 hardcore restriction screen is the most
   dangerous omission. A single RPM clause or passive sales restriction can void the entire
   agreement's block exemption and expose both parties to fines.

2. **Assuming governing law controls mandatory territory law** — Parties routinely believe
   a New York governing law clause protects them from Belgian distributor protection law.
   It does not. Belgian mandatory distribution law applies where the territory is Belgium,
   regardless of governing law choice. Always check mandatory country law for each
   distribution territory independently.

3. **Missing naked licensing risk** — Reviewing a trademark license clause that says
   "distributor shall use marks in accordance with brand guidelines" and classifying it as
   adequate. Without audit rights, quality standards, and actual quality control exercise,
   this creates naked licensing risk and potential trademark abandonment.

4. **Treating passive sales restrictions as territorial protection** — Suppliers sometimes
   draft "territorial integrity" clauses that effectively restrict passive sales (e.g.,
   prohibiting the distributor from accepting orders from customers in other territories).
   Any restriction on passive sales is a hardcore restriction under VBER Art. 4(b)(i)
   regardless of how it is labeled.

5. **Recommending RPM without state-by-state US analysis** — Post-_Leegin_, minimum RPM
   is analyzed under the rule of reason federally, but Maryland has legislatively reversed
   _Leegin_ and California's Cartwright Act may treat it as per se illegal. Recommending
   RPM provisions as legally safe without jurisdiction-specific US state-law analysis is
   an error.

6. **Treating MFN clauses as equivalent** — Wide MFNs (no better prices anywhere) and
   narrow MFNs (no better prices in own direct channel) have materially different
   competition law risk profiles. Wide MFNs imposed by online intermediation service
   providers are excluded restrictions under VBER 2022 Art. 5(1)(d). Analyzing them
   identically is an error.

7. **Ignoring the penalty doctrine for MPC take-or-pay** — Classifying a take-or-pay
   shortfall provision at full contract price as commercially standard without assessing
   the penalty doctrine under the governing law. Under UCC § 2-718 and EU civil law
   equivalents, liquidated damages must bear a reasonable relationship to actual harm.

8. **Not checking each distribution territory for mandatory country law** — Running only
   one country's mandatory distribution law analysis when the agreement covers multiple EU
   territories. Belgium, France, Germany, the Netherlands, and Spain each have distinct
   mandatory protections that require individual assessment.

9. **Classifying dual distribution as competition-risk without checking VBER conditions**
   — Dual distribution (supplier competing at retail) is broadly block-exempted under VBER
   2022 below the 30% threshold. The key restriction is on information exchange, not on
   the dual distribution itself. Over-classification undermines deal viability.

10. **Ignoring Robinson-Patman for US multi-distributor pricing** — Distribution agreements
    with tiered discount structures for multiple distributors are subject to Robinson-Patman
    Act scrutiny if price discrimination affects competition between competing purchasers.
    Post-2024 FTC enforcement revival, this deserves explicit flagging rather than omission.

11. **Single-pass analysis** — Reading the agreement linearly without noting how clauses
    interact. An MPC take-or-pay clause may be partially mitigated by a force majeure
    provision; an exclusivity grant may be effectively undermined by a broad supplier
    reservation of rights. Read the entire agreement before classifying individual clauses.

12. **Redlines without fallback positions** — Particularly problematic in distribution
    negotiations where competition counsel may restrict certain positions as legally impermissible.
    A redline that says "delete this clause" with no alternative is a negotiation dead end.

13. **Assuming non-compete scope is clear** — "Competing products" definitions are
    frequently drafted too broadly (covering products the distributor has been selling for
    years) or too narrowly (covering only identical products and missing functional
    equivalents). Always check the definition against the distributor's actual product range.

14. **Omitting post-termination trademark review** — When reviewing termination provisions,
    not reviewing whether the distributor gets a sell-down period to use the marks for
    existing inventory. A hard stop of trademark use on termination creates a stranded
    inventory problem for the distributor and a wasted investment problem for both parties.

15. **Treating boilerplate as irrelevant** — Severability is particularly critical in
    distribution agreements because competition law may sever an excluded restriction while
    preserving the rest of the agreement. A severability clause that does not expressly
    preserve the remainder of the agreement in the event of competition law severance
    creates unnecessary risk.

16. **Failing to ask about market share** — Running a VBER analysis and concluding the
    safe harbor applies without confirming that neither party exceeds 30% market share.
    Market share is a threshold condition for the entire safe harbor. Failure to ask
    when market share is unknown produces a confident but potentially wrong analysis.

17. **Not flagging the Robinson-Patman revival** — The FTC brought its first Robinson-
    Patman enforcement action in nearly 20 years in December 2024, followed by a second
    in January 2025 against PepsiCo. Differential pricing structures in US distribution
    agreements now carry meaningfully higher regulatory scrutiny than they did in prior years.
    [VERIFY — current enforcement status]

---

## Writing Standards

Apply plain-language discipline to all output:

**For redline rationales** (shared with counterparty's counsel):

- Plain language. No jargon or filler.
- Active voice: "This clause restricts passive sales" not "Passive sales are restricted by this clause."
- Short sentences. One point per sentence.
- Cite the authority: "VBER Art. 4(b)(i)" not "EU competition law."
- Specific, not vague: cite the provision, state the consequence, propose the remedy.

**For competition law analysis**:

- State the framework (VBER / Sherman Act) before the conclusion.
- Distinguish between hardcore restrictions (agreement loses exemption), excluded
  restrictions (clause severs), and rule-of-reason positions (fact-specific).
- Always state whether the VBER safe harbor is confirmed or assumed.

**Quality gates before delivery**:

1. Can a non-lawyer business stakeholder understand the executive summary?
2. Has every COMPETITION-RISK item been escalated with a specific authority citation?
3. Is every legal claim backed by a specific citation (or flagged [VERIFY])?
4. Has mandatory country law been assessed for each distribution territory?
5. Has the trademark quality control analysis confirmed or denied naked licensing risk?
6. Could any sentence be shorter without losing meaning? If yes, shorten.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.
legalcode-mcp is a law, regulatory, and case law database with powerful search across
jurisdictions.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for VBER 2022 provisions, Sherman Act case law, and country-specific
  mandatory distribution statutes relevant to each territory covered
- Search for recent competition authority enforcement decisions (Mondelez 2022,
  Pierre Cardin/Ahlers 2022, FTC Robinson-Patman 2024-2025)
- Verify current status of VBER 2022 (effective June 1, 2022; due for review in 2034)
- Search for Lanham Act naked licensing cases in the applicable US circuit
- Save verified results to `/tmp/legalcode-distribution-review-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — manual verification required"`
- Focus analysis on structural and competition law framework issues
- Do not assert that any specific statute is current without [VERIFY] qualifier

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Distribution Agreement Review Summary

**Document**: [agreement name/identifier]
**Parties**: [supplier and distributor names and roles]
**Your Side**: [Supplier / Distributor]
**Agreement Type**: [Exclusive / Non-exclusive / Selective / Reseller / OEM]
**Territory**: [Distribution territory]
**Governing Law**: [jurisdiction identified from the agreement]
**Review Basis**: [Playbook name / EU/US market standards]
**Date of Review**: [date]

---

## Competition Law Pre-Screen

**EU VBER 2022 Status**: [Safe harbor confirmed / Safe harbor assumed (market share
unconfirmed) / Safe harbor lost — [Article] triggered / Not applicable]
**US Sherman Act Issues**: [None identified / [Specific issue]]
**COMPETITION-RISK items requiring immediate escalation**: [None / [list with clauses]]

---

## Key Findings

[Top 3-5 issues with severity flags (RED/YELLOW/COMPETITION-RISK) and one-line summaries]

---

## Missing Clauses

[List any of the 18 clause categories that are absent, with severity assessment]

---

## Clause-by-Clause Analysis

### [Clause Category] — [GREEN / YELLOW / RED / COMPETITION-RISK] | Confidence: [level]

**Agreement says**: [summary of the provision]
**Standard position**: [EU/US market standard or playbook position]
**Deviation**: [description of gap]
**Business impact**: [what this means practically]
**Legal basis** (if applicable): [statute, regulation, or case — mark [VERIFY] if unconfirmed]
**Redline** (if YELLOW or RED):

> [Specific proposed language]
> **Fallback**: [alternative position if primary redline is rejected]

[Repeat for each clause category]

---

## Negotiation Strategy

**Tier 1 (Must-Haves)**: [list — competition law issues first, then naked licensing, then liability]
**Tier 2 (Should-Haves)**: [list]
**Tier 3 (Concession Candidates)**: [list]

**Recommended approach**: [sequencing, tone, strategic trades]
**Competition counsel engagement**: [required immediately / not required at this stage]

---

## Stakeholder Impact Map

[Table per Multi-Stakeholder Mapping section]

---

## Next Steps

[Specific actions to take, with owners and deadlines if applicable. Always list competition
counsel engagement if any COMPETITION-RISK items found. List country-specific counsel
engagement for each mandatory-law territory.]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

This skill is jurisdiction-agnostic with EU/US primary coverage. To create a
jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with jurisdiction-specific legal content
2. Replace [VERIFY] tags with verified statutory references
3. Add jurisdiction-specific mandatory distribution law requirements for the specific
   territory (beyond the Belgium/France/Germany/Netherlands/Spain matrix already included)
4. Add jurisdiction-specific competition law framework (e.g., CMA for UK, Bundeskartellamt
   for Germany, Autorité de la concurrence for France)
5. Add local product safety and regulatory compliance requirements
6. Update the frontmatter name and description to reference the specific jurisdiction
7. Add jurisdiction-specific anti-patterns

**Potential jurisdiction-specific variants:**

- **UK**: Post-Brexit VARE (Vertical Agreements Block Exemption) + CMA guidance + UK
  Commercial Agents Regulations 1993 by analogy for distribution termination
- **Australia**: ACCC guidance on vertical restraints + ACL (unfair contract terms for
  small business distributors) + Franchising Code by analogy
- **Canada**: Competition Act Part VI (criminal) / Part VIII (civil) vertical restraints
  - provincial distribution law
- **China**: Anti-Monopoly Law 2022 vertical guidelines + Ministry of Commerce approval
  for certain exclusive arrangements

---

## Provenance

Created by Legalcode (2026-03-19). Original synthesis built from deep research on EU VBER
2022 (Regulation 2022/720), EU Vertical Guidelines (2022/C 248/01), US Sherman Act Section
1 vertical restraint case law (_Leegin_, _Sylvania_, _Colgate_, _Palmer v. BRG_,
_United States v. Apple_), Robinson-Patman Act enforcement revival (2024–2025), Belgian
Law of 27 July 1961 on Exclusive Distribution, French Commercial Code Art. L.442-1 II,
German HGB §§ 89-89b by analogy, Lanham Act naked licensing doctrine (_Barcamerica_,
_FreecycleSunnyvale_), and UCC §§ 2-718 and 2-609 take-or-pay and liquidated damages
analysis. Structural frameworks adapted from the legalcode-contract-review gold standard
skill (2026-02-27). 2-agent research pipeline (structural + prompt engineering analysis)

- Perplexity-backed legal research + repository best practices synthesis.
