---
name: legalcode-antitrust-merger-review
description: Analyzes pre-merger notification obligations and merger control strategy for transactions
  subject to antitrust review. Covers US HSR Act notification requirements, EU Merger Regulation (EC 139/2004)
  jurisdictional thresholds and clearance process, UK CMA review under the Enterprise Act 2002, market
  definition methodology (SSNIP/hypothetical monopolist test), competitive effects analysis (unilateral,
  coordinated, vertical, and conglomerate effects), gun-jumping risk management, remedy strategy (structural
  vs. behavioral), multi-jurisdictional coordination, and deal-timeline planning. Use when advising on
  M&A antitrust clearance, conducting pre-signing antitrust risk assessments, preparing HSR filings, negotiating
  merger remedies, managing parallel competition authority reviews, or counseling on standstill obligations
  and clean-team protocols. Jurisdiction-specific coverage of US (FTC/DOJ), EU (European Commission DG
  COMP), and UK (CMA).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Antitrust Merger Review

> **Disclaimer**: This skill provides a framework for AI-assisted antitrust merger analysis.
> It does not constitute legal advice. All outputs must be reviewed by qualified antitrust
> counsel licensed in the relevant jurisdiction(s) before reliance. Merger control law
> evolves rapidly — thresholds, procedures, and enforcement priorities shift annually.
> Statutory citations and numerical thresholds carry hallucination risk; verify all figures
> against current official sources before filing or advising. This skill does not replace
> jurisdiction-specific merger filing counsel.

---

## Purpose and Scope

This skill analyzes the antitrust merger control dimensions of M&A transactions, from
pre-signing risk assessment through regulatory clearance and closing.

**Covers:**

- Filing obligation analysis for US (HSR Act), EU (EC 139/2004), and UK (Enterprise Act 2002)
- Market definition and competitive effects analysis across merger types
- Gun-jumping risk identification and clean-team protocol design
- Merger remedy strategy (structural divestitures, behavioral commitments, fix-it-first)
- Multi-jurisdictional clearance timeline coordination
- Deal documentation strategy (Item 4(c)/4(d) document collection, competitive overlaps)
- Phase classification (COMPLIANT / FLAG / BLOCKING) for each jurisdictional risk dimension
- Confidence-scored analysis with Glass Box audit trail

**Does not:**

- Constitute filing advice or substitute for local antitrust counsel
- Cover merger notifications outside US/EU/UK without jurisdiction extension
- Address non-merger antitrust issues (cartel, abuse of dominance, vertical restraints)
- Guarantee regulatory outcome — competition authority decisions are inherently uncertain

---

## Jurisdiction and Governing Law

This skill covers three primary jurisdictions. Each has distinct thresholds, timelines,
and substantive tests. The analysis always identifies which jurisdictions are triggered
and tailors the output accordingly.

| Jurisdiction       | Primary Law                                | Regulator                               | Substantive Test                                       |
| ------------------ | ------------------------------------------ | --------------------------------------- | ------------------------------------------------------ |
| **United States**  | Clayton Act § 7; HSR Act (15 U.S.C. § 18a) | FTC / DOJ Antitrust Division            | Substantial Lessening of Competition (SLC)             |
| **European Union** | EC Merger Regulation 139/2004              | European Commission DG COMP             | Significant Impediment to Effective Competition (SIEC) |
| **United Kingdom** | Enterprise Act 2002 (as amended)           | Competition and Markets Authority (CMA) | Substantial Lessening of Competition (SLC)             |

[JURISDICTION-SPECIFIC] Additional jurisdictions commonly triggered in cross-border deals
include Canada (Competition Act, Investment Canada Act), China (SAMR), Australia (ACCC),
Germany (Bundeskartellamt), and Brazil (CADE). Each has its own thresholds and timelines.
For deals with significant presence in additional jurisdictions, flag for specialist counsel.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
transaction structure or competitive context, the workflow pauses and asks when:

- The answer would materially change the filing obligation analysis
- Multiple markets may be relevant and the user must define scope
- Competitive sensitivity of information-sharing requires clean-team design guidance
- Remedy strategy depends on business context only the user can supply

Use the **⟁ CLARIFY** pattern (structured options with explanations) wherever marked.
Skip any question where the user has already provided the relevant information.

---

## Workflow

### Step 1: Accept the Transaction

Accept the transaction description in any of these formats:

- **Deal summary**: Parties, transaction structure (acquisition, merger, JV), deal value,
  and description of the businesses
- **Draft agreement**: Term sheet, letter of intent, or merger agreement
- **Regulatory filing draft**: Draft HSR notification or EU notification form
- **Summary memo**: Antitrust risk memo prepared by deal team

If none of these are provided, prompt the user to supply a description of the parties
and the transaction.

### Step 2: Gather Transaction Context

**⟁ CLARIFY** — Before beginning the analysis, ask the user the following. Present as
structured options where possible.

1. **Transaction type:**
   - Options: Acquisition of shares, Acquisition of assets, Statutory merger, Joint
     venture formation, Minority investment with governance rights, Other
   - _Why this matters_: Filing thresholds and the standstill obligation apply differently
     to share acquisitions vs. asset deals; JVs may trigger separate notification rules.

2. **Deal value and party sizes:**
   - Approximate deal value (or "not yet determined")
   - Approximate annual revenues of both acquirer and target in the US, EU, UK, and globally
   - _Why this matters_: Determines which filing thresholds are met. Incorrect size
     estimates can lead to missed filings (gun-jumping exposure) or unnecessary filings.

3. **Business overlap:**
   - Do the parties compete in any markets (horizontal overlap)?
   - Does either party supply inputs to, or purchase outputs from, the other (vertical relationship)?
   - Any conglomerate/portfolio overlap (adjacent products sold to the same customers)?
   - _Why this matters_: The substantive test and depth of competitive effects analysis
     depends entirely on the nature and extent of the overlap.

4. **Jurisdiction coverage:**
   - Options: US only, EU only, UK only, US + EU, US + UK, EU + UK, All three, Other
     (specify additional jurisdictions)
   - _Why this matters_: Determines which filing analyses to run and which timelines
     to coordinate.

5. **Timeline constraints:**
   - Target signing date and anticipated closing date
   - Any external deadline (break fees, financing commitments, board mandates)
   - _Why this matters_: Determines whether parallel filings can be pursued and whether
     the deal timeline allows for second requests or Phase II investigations.

If the user provides partial context, proceed with stated assumptions and flag them
explicitly.

### Step 3: Load Legal Authority

Use **legalcode-mcp** to gather current legal authority for each triggered jurisdiction:

1. Search for current HSR Act jurisdictional thresholds and 16 C.F.R. Part 801 rules
2. Search for current EU Merger Regulation turnover thresholds and Phase I/II timelines
3. Search for current UK Enterprise Act 2002 jurisdictional thresholds (post-2025 reform)
4. Search for 2023 DOJ/FTC Merger Guidelines (confirmed in effect as of February 2025)
5. Search for relevant EU and UK merger decisions in the relevant product/sector markets

Save results to `/tmp/legalcode-merger-authority.md`. Structure as:

```markdown
# Merger Control Authority — [Transaction Name]

## Date: [date]

### US HSR Act

- Current size-of-transaction threshold: [VERIFY]
- Current size-of-person thresholds: [VERIFY]
- Waiting period: [VERIFY]

### EU Merger Regulation

- Primary turnover thresholds: [VERIFY]
- Alternative thresholds: [VERIFY]
- Phase I / Phase II timelines: [VERIFY]

### UK Enterprise Act

- Current turnover threshold: [VERIFY]
- Share of supply threshold: [VERIFY]
- Phase 1 / Phase 2 timelines: [VERIFY]

### Sector-Specific Authority

- [Relevant precedent decisions, if any]
```

**If legalcode-mcp is not connected**, mark all thresholds [VERIFY] and proceed using
the research baseline in the Analysis Reference section below. Note in the Glass Box
audit trail: `legalcode_mcp: "Not connected — all thresholds require independent verification"`.

### Step 4: Filing Obligation Analysis

For each jurisdiction in scope, analyze whether a filing obligation is triggered.

**⟁ CLARIFY** — If exact revenue figures are unavailable, ask whether to:

- **Option A**: Use estimates and flag the analysis as preliminary
- **Option B**: Identify the threshold question and flag it for the deal team to verify
  before signing (safer for compliance purposes)

Apply the **Filing Obligation Checklist** in the Analysis Reference section. For each
jurisdiction:

1. Apply the jurisdictional thresholds
2. Identify any exemptions (e.g., ordinary course of business, foreign-to-foreign,
   passive investment exemptions)
3. Classify: **FILING REQUIRED** / **FILING NOT REQUIRED** / **UNCERTAIN — VERIFY**
4. Note any "catch-all" or discretionary review risk (e.g., UK CMA's share of supply
   test can reach sub-threshold deals)

### Step 5: Competitive Effects Analysis

Assess the competitive effects of the transaction across each identified overlap:

**⟁ CLARIFY** — For the market definition step, ask:

- Are the parties' products/services substitutable from the customer's perspective?
- Do the parties operate in distinct product segments that are NOT substitutable
  (requiring separate market analysis)?
- Are there geographic market issues (local vs. national vs. global)?

Run the analysis prescribed in **Competitive Effects Analysis** in the Analysis Reference
section. Classify each competitive overlap using the three-tier system:

| Classification | Meaning                                                                                          |
| -------------- | ------------------------------------------------------------------------------------------------ |
| **COMPLIANT**  | Transaction unlikely to raise substantive competitive concerns in this jurisdiction              |
| **FLAG**       | Competitive concerns possible; further analysis and/or authority engagement recommended          |
| **BLOCKING**   | Competitive concerns substantial; deal faces material risk of challenge or block unless remedied |

### Step 6: Gun-Jumping Risk Assessment

Assess the risk of gun-jumping violations arising from the deal structure, conduct between
signing and closing, or information-sharing practices.

Apply the **Gun-Jumping Risk Checklist** in the Analysis Reference section. Flag any
HIGH-risk conduct and recommend clean-team protocols where needed.

### Step 7: Remedy Strategy

If any competitive overlap is classified FLAG or BLOCKING:

**⟁ CLARIFY** — Ask the user about remedy tolerance:

- **Option A**: Explore structural remedies (what assets could feasibly be divested?)
- **Option B**: Explore behavioral remedies (what commitments could be offered?)
- **Option C**: Assess deal risk without assuming any remedy (worst-case analysis)
- **Option D**: Develop both options for strategy comparison

Apply the **Remedy Strategy Framework** in the Analysis Reference section.

### Step 8: Multi-Jurisdictional Timeline Coordination

If filings are triggered in multiple jurisdictions, develop a coordinated clearance
timeline:

1. Identify the longest-lead jurisdiction (typically EU Phase II at ~7 months, or
   a US second request at 4-6+ months)
2. Map mandatory waiting periods and their sequencing
3. Flag any jurisdiction where approval is a condition precedent to closing
4. Identify agency coordination mechanisms (confidentiality waivers, model waivers)
5. Note deal document strategy: approach for Item 4(c) business document collection

### Step 9: Quality Verification

Before delivering the analysis, run all checks in the **Quality Assurance Framework**:

1. Run 5 Citation Quality Gates silently. Revise any failures.
2. For every BLOCKING-classified issue, run 3-pass Self-Interrogation. Revise if any
   pass reveals a weakness.
3. Assign Confidence Scores to all threshold calculations and competitive effects
   conclusions.
4. Verify all numerical thresholds are marked [VERIFY] unless confirmed via legalcode-mcp.
5. Generate the Glass Box Audit Trail and append to the output.

### Step 10: Deliver Analysis

Produce the output using the **Output Format Template** in the final section. Present:

- Filing obligation summary table (all jurisdictions)
- Competitive effects assessment with classification
- Gun-jumping risk matrix
- Recommended clearance timeline
- Remedy strategy options (if any FLAG/BLOCKING issues)
- Confidence scores and [VERIFY] flags

---

## Analysis Reference

### Filing Obligation Checklist

#### United States — HSR Act (15 U.S.C. § 18a)

**Threshold Analysis (2026 figures — [VERIFY] annually):**

| Test                                       | 2026 Threshold                            | Notes                                        |
| ------------------------------------------ | ----------------------------------------- | -------------------------------------------- |
| Size of Transaction                        | >$133.9M                                  | Value of acquired assets/securities          |
| Small Transaction Safe Harbor              | ≤$133.9M                                  | No filing required regardless of party size  |
| Large Transaction (no size-of-person test) | >$535.6M                                  | Filing required regardless of party revenues |
| Size of Person — larger party              | ≥$267.8M annual net sales or total assets | Apply when transaction is $133.9M–$535.6M    |
| Size of Person — smaller party             | ≥$26.8M annual net sales or total assets  | Apply when transaction is $133.9M–$535.6M    |

**Key Exemptions and Exceptions:**

- Foreign-to-foreign transactions: Generally exempt unless US nexus (US assets/sales above threshold)
- Ordinary course of business: Acquisitions of goods or real estate in ordinary course
- New entity acquisitions: Specific rules for acquiring newly formed entities
- Intraperson transactions: Acquisitions within the same "person" (controlled affiliates)
- Passive investment: Acquisition of voting securities solely for investment (≤10% of outstanding)
- Certain JV formations: Specific analysis required under 16 C.F.R. § 801.40

**Process:**

- Filing: Premerger Notification Office (PNO), Bureau of Competition, FTC
- Waiting period: 30 days (15 days for cash tender offers and bankruptcy acquisitions)
- Early termination: Available for uncontroversial transactions (FTC + DOJ must both agree)
- Second Request: Extends waiting period; compliance typically takes 4–12 months
- Filing fees (2026): $30,000 (deals $133.9M–$337.6M); $105,000 (deals $337.6M–$843.8M);
  $250,000 (deals $843.8M–$1,687.7M); $500,000 (deals $1,687.7M–$5,063.2M); higher tiers
  apply above — [VERIFY all fee figures]

**Item 4(c)/(d) Document Strategy (Post-January 2025 Rules):**

- Collect all documents from: officers/directors AND "supervisory deal team lead"
- Include: transaction-related documents AND plans/reports analyzing competitive topics
  related to overlapping products/services (regardless of transaction purpose)
- Expanded scope means significantly larger document production burden
- Recommend: early document hold and collection protocol at signing or pre-signing

#### European Union — EC Merger Regulation 139/2004

**Jurisdictional Thresholds ("EU Dimension"):**

Primary Threshold (Article 1(2)):

- Combined worldwide turnover of all undertakings concerned: >€5,000M, AND
- Aggregate Community-wide turnover of each of at least two: >€250M each
- Exception: No EU dimension if each achieves >2/3 of EU-wide turnover in one Member State

Alternative Threshold (Article 1(3)):

- Combined worldwide turnover: >€2,500M, AND
- In each of at least 3 Member States, combined turnover: >€100M, AND
- In each of those same 3 Member States, each of at least two parties: >€25M, AND
- Aggregate Community-wide turnover of each of at least two parties: >€100M each
- Exception: >2/3 rule applies here too

**One-Stop-Shop Principle:** If EU dimension is established, the European Commission has
exclusive jurisdiction. Member State authorities are precluded from applying national
competition law to the concentration (Article 21(3)).

**Referral Mechanisms:**

- Article 4(4): Pre-notification referral to Member State(s) — parties may request
- Article 22: Member State(s) may request Commission review even without EU dimension
  (updated post-_Illumina/Grail_ CJEU decision — [VERIFY current Article 22 scope)
- Article 9: Commission may refer to Member State after notification

**Phase I Timeline:**

- Day 0: Complete notification received
- Day 25: Phase I decision deadline (25 working days)
- Day 35: Extended Phase I if parties offer remedies within 20 working days (35 working days)
- Outcome: Clearance, conditional clearance, or Phase II initiation

**Phase II Timeline:**

- Initiated at end of Phase I if serious doubts
- Day 90: Standard Phase II deadline (90 working days from Phase II initiation)
- Day 105: Extended if parties offer remedies (15 additional working days)
- Day 125: Maximum extension with extraordinary circumstances
- Outcome: Clearance, conditional clearance, or prohibition

**Standstill Obligation (Article 7(1)):**

- Concentration must not be implemented before notification and clearance
- Applies from signing of binding agreement or announcement of public bid
- Derogation available from Commission in exceptional circumstances (Article 7(3))
- Violation: Up to 10% of aggregate worldwide turnover ([VERIFY current maximum])

#### United Kingdom — Enterprise Act 2002

**Jurisdictional Thresholds (post-January 1, 2025 reform — [VERIFY]):**

| Test                        | Threshold                                                                                        |
| --------------------------- | ------------------------------------------------------------------------------------------------ |
| Turnover Test               | UK turnover of target >£100M (raised from £70M)                                                  |
| Media Turnover              | UK turnover of target >£70M (media plurality cases)                                              |
| Share of Supply Test        | Post-merger share ≥25% in UK supply/acquisition of goods/services (no minimum turnover required) |
| Small Business Safe Harbour | Each party UK turnover ≤£10M                                                                     |

**Key Characteristics:**

- **Voluntary system**: No mandatory notification obligation; no suspension of closing
- **However**: CMA retains jurisdiction to investigate any qualifying merger for up to 4 months
  post-public announcement or completion (whichever is earlier) — creates deal certainty risk
- **Pre-notification discussions**: Strongly recommended for problematic deals
- **Interim measures**: CMA may impose on deals that complete before clearance

**Phase 1 Timeline:**

- Statutory period: 40 working days
- CMA may accept undertakings in lieu (UILs) at Phase 1 to avoid Phase 2

**Phase 2 Timeline:**

- Up to 24 weeks from reference decision (6 months)
- CMA statutory duty to decide within this period

**Substantive Test:**

- Substantial Lessening of Competition (SLC) in a substantial part of the UK
- Applies to both Phase 1 (reasonable grounds to believe) and Phase 2 (balance of harms)

---

### Market Definition Methodology

#### SSNIP Test (Hypothetical Monopolist Test)

**Question**: Would a hypothetical monopolist controlling all products in the candidate
market profitably impose a Small but Significant Non-Transitory Increase in Price (5–10%
for at least one year)?

**Procedure:**

1. Define the candidate market (starting with the narrowest plausible definition)
2. Identify all products to which customers would switch if SSNIP were applied
3. If sufficient switching occurs to make the price increase unprofitable, expand the
   market to include the substitute products
4. Repeat until the market is correctly bounded (SSNIP would be profitable)

**Cellophan Fallacy Warning:** Do not start with a broad market — competitive products
may appear substitutable from a starting price that already reflects supracompetitive
pricing. Start narrow and expand.

**Geographic Market:**

- Apply same SSNIP methodology to geographic dimension
- Ask: if price increased in one region, would customers switch to suppliers in another?
- Consider: transport costs, regulatory barriers, local distribution networks, brand preferences

**Relevant Market Types for Merger Analysis:**

- Product market: Demand-side substitutability (customer perspective) + supply-side
  substitutability (can other suppliers redirect production quickly without significant cost?)
- Geographic market: May be local, national, EU-wide, EEA-wide, or global depending on
  competitive dynamics

---

### Competitive Effects Analysis

#### Horizontal Mergers — Unilateral Effects

**Triggers**: Parties compete directly in the same product and geographic market.

**Analysis tools:**

- **Diversion ratios**: What share of sales lost by Party A due to a price increase would
  be recaptured by Party B? Higher diversion = stronger unilateral effects
- **Market shares and HHI**: Calculate Herfindahl-Hirschman Index pre- and post-merger.
  US safe harbors: HHI <1,500 (unconcentrated); change in HHI <100 in moderately
  concentrated market (HHI 1,500–2,500) generally unlikely to be challenged ([VERIFY])
- **Upward Pricing Pressure (UPP) test**: Estimates incentive to raise price post-merger
  by combining margin data with diversion ratios
- **Capacity and competitive constraints**: Is the merged entity the only or closest
  substitute for a significant segment of customers?

**Red flags — automatic FLAG:**

- Post-merger market share >40% in any relevant market
- Merging parties are the two closest competitors in a differentiated market
- High diversion ratios (>30%) between the parties' products
- Target firm is a "maverick" — pricing or innovating aggressively outside industry norms

#### Horizontal Mergers — Coordinated Effects

**Triggers**: Market has few players, homogeneous products, transparent pricing, stable
demand, and high barriers to entry.

**Analysis criteria (post-merger ability to coordinate):**

1. Can firms reach a common understanding on competitive terms?
2. Can coordination be monitored and defection detected quickly?
3. Can defectors be disciplined (punishment mechanism)?
4. Will coordination hold against fringe competitors and new entry?

**Red flags — automatic FLAG:**

- Post-merger market reduces to 3 or fewer significant players
- Industry has history of price-fixing or coordination
- Products are homogeneous with publicly posted prices
- Demand is stable and predictable (easy to monitor deviations)

#### Vertical Mergers

**Triggers**: Acquirer and target operate at different levels of the supply chain.

**Input foreclosure analysis:**

- Could merged entity foreclose rivals' access to a key input controlled by the target?
- Assess: Is the input critical? Does the merged entity have ability and incentive to foreclose?
- Countervailing factors: Can rivals develop alternative inputs? Regulatory access obligations?

**Customer foreclosure analysis:**

- Could merged entity foreclose rival suppliers' access to distribution channels or customers
  controlled by the acquirer?
- Assess: Are the channels essential? Is foreclosure commercially rational?

**Efficiencies:** Vertical mergers commonly generate genuine efficiencies (elimination of
double marginalization, improved coordination) — quantify and document for remedy negotiations.

#### Conglomerate Mergers

**Triggers**: No horizontal or vertical overlap, but parties sell to the same customers
or in adjacent markets.

**Bundling and tying analysis:**

- Could merged entity bundle products in a way that disadvantages rivals?
- EU historically more interventionist on conglomerate effects than US
- GE/Honeywell (2001) remains cautionary example of EU prohibition of a US-cleared deal

---

### Gun-Jumping Risk Checklist

**Definition**: Implementation of a notifiable concentration before obtaining required
regulatory approvals.

#### HIGH RISK — Immediate remediation required

- [ ] Integration activities commencing before clearance (sharing customers, employees,
      pricing strategies, or operations with HSR/EU/UK obligation outstanding)
- [ ] Exchange of competitively sensitive information outside clean-team structure
      (current pricing, customer lists, margin data, forward-looking business plans)
- [ ] Acquirer exercising management influence over target before clearance
- [ ] Parties coordinating on market-facing activities (pricing, bidding, customers)
- [ ] Joint marketing, sales, or HR activities commenced pre-clearance
- [ ] Transition planning meetings that result in actual operational decisions
      (rather than planning-only)

#### MEDIUM RISK — Requires clean-team protocol or counsel review

- [ ] Information shared to conduct due diligence without NDA or clean-team structure
- [ ] M&A agreement contains provisions that immediately transfer operational control
      (veto rights, board seats effective at signing rather than closing)
- [ ] Merger agreement contains restrictive covenants on target's business pre-closing
      that go beyond protecting deal value (e.g., restrictions on hiring, capex, pricing)

#### LOWER RISK — Document and monitor

- [ ] Ordinary course governance rights for acquirer pre-closing (approval of
      extraordinary transactions, major capex, large contracts above deal-size threshold)
- [ ] Due diligence access to aggregated, anonymized, or historical data
- [ ] Clean-team review of competitively sensitive materials with restricted distribution

**Penalty Reference (illustrative — [VERIFY all current figures]):**

- EU: Up to 10% of aggregate worldwide turnover per violation; Altice fined €124.5M total
  (two separate violations: notification breach + implementation breach) [VERIFY]
- US: Civil penalty up to ~$42,000–$50,000 per day of noncompliance [VERIFY current rate]

**Clean-Team Protocol Essentials:**

1. Designate clean-team members (outside antitrust counsel, independent consultants,
   limited internal personnel not involved in competitive decisions)
2. Competitively sensitive materials shared only within clean team under strict protocols
3. Findings communicated to business personnel as aggregated, anonymized summaries only
4. Written protocols signed by all clean-team members
5. Clean-team information not used for competitive decision-making before clearance

---

### Remedy Strategy Framework

#### Structural Remedies (Strongly Preferred by Authorities)

**Divestiture packages:**

- Overlap business: Divest the overlapping business to eliminate the competitive problem
- Product line divestiture: Divest specific competing products or brands
- Asset package: Combine relevant IP, customer contracts, production capacity, and key
  personnel to create a viable standalone business for the buyer

**Divestiture buyer considerations:**

- Must be independent from merged entity post-completion
- Must have financial capacity and operational capability to maintain or develop the business
- **Upfront buyer requirement**: Authorities (especially FTC) may require an approved
  buyer to be identified before granting clearance (common for: complex assets, IP-only
  divestitures, businesses susceptible to deterioration during carve-out)

**Fix-It-First approach:**

- Negotiate and announce the divestiture agreement with the buyer before or during
  regulatory review
- Reduces agency uncertainty about remedy effectiveness
- Can accelerate clearance timeline by eliminating remedy negotiation phase

**Hold-Separate obligations:**

- Maintain divested assets as a standalone operation pending completion of divestiture
- Appoint an independent monitoring trustee if required by authority

#### Behavioral Remedies (Disfavored — Use Selectively)

**When potentially acceptable:**

- Vertical mergers where foreclosure risk can be mitigated by access commitments
- Merger-specific efficiencies are large and offsetting
- Structural remedy would destroy significant deal value
- UK CMA has shown willingness in network/infrastructure sectors (Vodafone/Three, 2024)

**Types of behavioral remedies:**

- Access commitments: Supply competing firms at regulated terms (FRAND-like)
- Interoperability commitments: Ensure rival products can interact with merged entity's platform
- Non-discrimination obligations: Treat internal and external customers equally
- Price/tariff caps: Time-limited caps accepted in highly regulated sectors
- Firewalls: Information barriers preventing merged entity from leveraging competitively
  sensitive information

**Limitations:** DOJ/FTC strongly disfavor behavioral remedies for horizontal mergers;
EU accepts in limited circumstances; UK CMA typically prefers structural for retail markets.

#### Remedy Negotiation Process

**EU (Phase I remedies — preferred):**

- Must be offered within 20 working days of notification
- Market testing by Commission (2–3 weeks)
- Clearance with conditions at end of extended Phase I (Day 35)
- Advantage: Avoids Phase II (months faster)

**EU (Phase II remedies):**

- Must be offered within 65 working days of Phase II initiation (or later with agreement)
- Commission has extended timeline to assess complex remedies

**US (consent decree):**

- Typically negotiated during second request period
- DOJ: Consent decree filed and subject to public comment period
- FTC: Administrative consent order subject to public comment

**UK (Phase 1 UILs):**

- Offered within 5 working days of Phase 1 decision
- CMA has 50 working days to accept UILs
- Must be clear-cut and effective — CMA unlikely to accept UILs of uncertain efficacy

---

## Severity Classification

### COMPLIANT — No Material Concern

Transaction does not raise substantive competitive concerns in the relevant jurisdiction:

- Filing threshold not met, OR
- Market shares remain low post-merger (typically <25% combined), OR
- Parties are not close competitors, OR
- Strong competitive constraints from multiple remaining competitors, OR
- No vertical foreclosure risk (shares at either level insufficient to harm rivals)

**Action**: Document the analysis, confirm no filing requirement or proceed with
straightforward notification, close on schedule.

### FLAG — Concerns Possible; Expert Review Required

Transaction warrants detailed competitive analysis and possible regulatory engagement:

- Post-merger market share in a relevant market is 25–40%, OR
- HHI change >100 in a concentrated market, OR
- Parties are among the top three competitors in a market, OR
- Vertical relationship in a market with significant entry barriers, OR
- Transaction raises novel regulatory questions (digital markets, platform mergers), OR
- CMA share of supply test may be triggered even if turnover threshold is not met

**Action**: Conduct detailed competitive effects analysis; consider pre-notification
meetings with relevant authority; prepare robust efficiency defense; evaluate remedy
options proactively.

### BLOCKING — High Risk; Deal May Require Remedies or Face Challenge

Transaction faces material risk of prohibition or significant remedies:

- Post-merger market share >40% in a relevant market, OR
- Merging parties are the two closest competitors in a concentrated market, OR
- Transaction eliminates a maverick or disruptive competitive force, OR
- Authority has challenged or blocked similar transactions recently, OR
- HHI change >200 in a highly concentrated market (HHI >2,500), OR
- Vertical transaction with evidence of foreclosure incentive and ability, OR
- Clear gun-jumping violation has occurred requiring corrective action

**Action**: Engage antitrust counsel immediately; develop full remedies strategy;
assess deal risk tolerance; prepare for extended regulatory review; consider
whether deal can proceed without remedies.

---

## Actionable Output Per Finding

For each classified finding, provide:

### For COMPLIANT Findings

```
Market: [Market name]
Parties' shares: [X%] + [Y%] = [Z%] post-merger
HHI change: [Δ HHI]
Classification: COMPLIANT
Rationale: [Why no concern — number of remaining competitors, market characteristics]
Action: [No action required / Document analysis / Straightforward notification]
```

### For FLAG Findings

```
Market: [Market name]
Parties' shares: [X%] + [Y%] = [Z%] post-merger
HHI change: [Δ HHI]
Classification: FLAG
Concern: [Unilateral effects / Coordinated effects / Vertical foreclosure / Other]
Evidence: [Market characteristics supporting concern]
Countervailing factors: [Entry conditions, buyer power, efficiencies]
Action: [Pre-notification meeting recommended / Detailed competitive analysis /
         Prepare efficiency defense / Evaluate remedy options]
Confidence: [PROBABLE / POSSIBLE — rationale]
```

### For BLOCKING Findings

```
Market: [Market name]
Parties' shares: [X%] + [Y%] = [Z%] post-merger
HHI change: [Δ HHI]
Classification: BLOCKING
Concern type: [Specific theory of harm]
Supporting authority: [Regulatory precedent or guidelines — [VERIFY]]
Remedy options:
  - Structural: [Specific divestiture package — assets, brands, customer contracts]
  - Behavioral: [Access commitment / Firewall / Price cap — if applicable]
  - Fix-it-first: [If identified buyer exists]
Deal risk: [Probability of challenge / Expected timeline impact]
Escalation: [Outside antitrust counsel / CEO-level decision on remedy tolerance]
Confidence: [HIGH / PROBABLE — rationale]
```

---

## Prioritization Framework

### Tier 1 — Immediate / Deal-Critical (Address Before Signing or Immediately After)

- Filing obligation confirmed: initiate HSR/EU/UK notification preparation
- BLOCKING competitive overlap identified: engage antitrust counsel; assess remedy tolerance
- Gun-jumping HIGH RISK conduct: halt immediately; document corrective action
- Standstill obligation in EU or US: confirm closing is suspended pending clearance
- Item 4(c) document hold: implement immediately upon signing (US transactions)
- Multi-jurisdictional coordination: execute model confidentiality waivers early

### Tier 2 — Material / Strategic (Address Within First Two Weeks Post-Signing)

- FLAG competitive overlaps: retain economic experts; develop competitive analysis
- Pre-notification meeting with authorities (EU, UK): schedule and prepare materials
- Remedy options for FLAG markets: evaluate divestiture candidates and upfront buyers
- Clean-team protocol: implement for all information sharing pending clearance
- Additional filing jurisdictions (Canada, China, Germany, etc.): identify and triage

### Tier 3 — Process / Compliance (Ongoing Through Clearance)

- Monitoring trustee appointment (if required by remedy order)
- Hold-separate compliance for divested assets
- Waiting period tracking across all jurisdictions
- Early termination request (US): file if no substantive concerns
- Phase I extension monitoring (EU): track remedy offer deadline (Day 20)
- UK CMA interim measures: monitor for any ITO or hold-separate direction

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise if any gate fails.

| Gate           | Rule                                                                                                                   | Fail Action                              |
| -------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **Source**     | Every threshold, timeline, or legal standard cites a specific statute, regulation, guideline, or precedent             | Add citation or mark [UNVERIFIED]        |
| **Format**     | All citations follow a consistent recognizable format (US: statute + CFR; EU: Regulation article; UK: statute section) | Fix format                               |
| **Currency**   | Every numerical threshold flagged with [VERIFY] — these change annually                                                | Add [VERIFY] to all numerical thresholds |
| **Domain**     | Analysis stays within the three covered jurisdictions; does not bleed other jurisdictions' standards in as universal   | Remove or flag jurisdictional bleed      |
| **Confidence** | Uncertainty about filing obligation or competitive classification stated explicitly, not hidden                        | Add confidence qualifier                 |

### Self-Interrogation for BLOCKING Findings

For any issue classified as BLOCKING, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the competitive harm theory follow from established
authority? Have I applied the correct substantive test for the jurisdiction (SLC for US/UK;
SIEC for EU)? Is the market definition defensible?

**Pass 2 — Completeness**: Have I considered all countervailing factors — entry conditions,
countervailing buyer power, efficiencies, the parties' combined post-merger share vs.
remaining competitive constraints?

**Pass 3 — Challenge**: What is the strongest argument that this is NOT a BLOCKING concern?
Under what market conditions or remedy package would a reasonable competition authority
clear this transaction?

### Confidence Scoring

| Level        | Range     | Meaning                                                                | Action                                         |
| ------------ | --------- | ---------------------------------------------------------------------- | ---------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, clear threshold met or not met                            | State with confidence                          |
| **High**     | 0.80–0.94 | Strong basis; minor uncertainty (e.g., exact revenue figure)           | State with brief caveat                        |
| **Probable** | 0.60–0.79 | Reasonable basis but key facts uncertain                               | State with reasoning and flag for verification |
| **Possible** | 0.40–0.59 | Genuinely uncertain (e.g., novel market definition, borderline shares) | Flag for competition economist review          |
| **Unlikely** | 0.0–0.39  | Speculative; insufficient basis to classify                            | Do not assert; mark [UNCERTAIN]                |

---

## Anti-Patterns

What NOT to do in antitrust merger analysis:

1. **Relying on stale thresholds** — HSR thresholds adjust annually in February; EU and UK
   thresholds are set by statute but may be amended. Never state a threshold without [VERIFY].

2. **Defining the market too broadly** — Starting with a broad market definition that
   understates market concentration. Apply the hypothetical monopolist test starting from
   the narrowest plausible definition.

3. **Ignoring the Cellophane fallacy** — If parties already have high market shares, their
   current pricing may already be supracompetitive, making apparent substitutes in the broad
   market unreliable. Start narrow.

4. **Assuming voluntary UK notification is optional** — The UK CMA retains jurisdiction to
   investigate for up to 4 months post-announcement even without a filing. "Voluntary" does
   not mean "safe to ignore" for significant deals.

5. **Treating the EU one-stop-shop as absolute** — Article 22 referrals allow the Commission
   to review sub-threshold deals referred by Member States; scope remains contested after the
   _Illumina/Grail_ litigation. Flag Article 22 risk for strategic or digital market deals.

6. **Underestimating gun-jumping in the EU** — The EU standstill obligation is triggered by
   the ability to exercise decisive influence, not just its actual exercise. M&A agreement
   provisions granting pre-closing governance rights may themselves constitute implementation.

7. **Overlooking the HSR "beneficial ownership" concept** — Gun-jumping under HSR does not
   require formal closing; gaining effective control or the ability to control business
   decisions is enough. Review all pre-closing covenants carefully.

8. **Underestimating Item 4(c) document exposure** — Since January 2025, HSR rules require
   collection from the "supervisory deal team lead" in addition to officers/directors, and
   cover plans/reports analyzing competitive topics unrelated to the transaction. Failure to
   identify all required documents is a significant compliance risk.

9. **Proposing behavioral remedies for horizontal overlaps in the US** — DOJ/FTC strongly
   disfavor behavioral remedies for horizontal mergers and are unlikely to accept them. Do
   not lead a remedy strategy with behavioral commitments unless structural divestiture is
   genuinely impossible.

10. **Failing to coordinate multi-jurisdictional timelines** — Failing to identify the
    longest-lead jurisdiction results in a deal condition remaining unsatisfied after
    other jurisdictions have cleared. Map all timelines before signing to avoid surprises.

11. **Relying on a single HHI analysis** — HHI is a starting point, not a conclusion.
    Market concentration is one factor; entry conditions, competitive dynamics, buyer power,
    and innovation competition all affect the substantive analysis. Do not stop at HHI.

12. **Missing a referral obligation to Member States** — Under EU Merger Regulation Article 4(4),
    parties may request pre-notification referral to Member State(s) where a deal has
    primarily national effects. Missing the referral opportunity can lengthen the process
    or leave a deal exposed to parallel national reviews.

13. **Underestimating the UK CMA's aggression** — Post-Brexit, the CMA has developed an
    increasingly independent and interventionist approach. Do not assume UK clearance on
    the basis of EU clearance alone (as Microsoft/Activision demonstrated, CMA blocked
    what the EC conditionally approved).

14. **Neglecting the efficiency defense** — Competition authorities will consider genuine,
    merger-specific, and verifiable efficiencies in the analysis. Failure to document and
    quantify efficiencies early leaves a significant pro-competitive argument on the table.

15. **Forgetting minority stakes and JV creations** — Acquisitions of minority interests
    with governance rights (board seats, veto rights over commercial decisions) may trigger
    filing obligations even below the asset/revenue thresholds. JV formations require
    separate HSR analysis under 16 C.F.R. § 801.40.

16. **Ignoring the fix-it-first opportunity** — In complex deals with identifiable remedies,
    negotiating and announcing a divestiture buyer before the regulatory process concludes
    can dramatically shorten clearance timelines. Missing this opportunity means months of
    avoidable delay.

17. **Assuming early termination is available** — The US early termination program was
    suspended from February 2021 to October 2024. Even now that it is reinstated, it
    requires both FTC and DOJ agreement. Do not build deal timelines around early
    termination without assessing whether the agencies are likely to grant it.

---

## Writing Standards

Before delivering the final analysis, verify:

- [ ] All numerical thresholds are marked [VERIFY] unless confirmed via legalcode-mcp
      with a dated citation
- [ ] Every BLOCKING finding has supporting legal authority or is marked [UNCERTAIN]
- [ ] Classifications (COMPLIANT / FLAG / BLOCKING) are consistent throughout
- [ ] Jurisdiction-specific content is clearly attributed to its jurisdiction
- [ ] No jurisdiction-specific rules are stated as universal
- [ ] All abbreviations are defined at first use (HHI, SSNIP, SLC, SIEC, UIL, UPP, etc.)
- [ ] Actionable recommendations are specific — not "consider remedies" but "evaluate
      divestiture of [specific business] to [type of buyer]"
- [ ] Confidence scores are assigned to all material conclusions
- [ ] Glass Box audit trail is complete and appended

**Plain-language discipline:**

- Use active voice: "The HSR Act requires notification" not "Notification is required under
  the HSR Act"
- Avoid hedge-stacking: "may potentially be possible" → "may be"
- Define technical terms on first use: "SSNIP (Small but Significant Non-Transitory
  Increase in Price)" then use "SSNIP" thereafter
- Present numbers consistently: "$133.9 million" not "$133,900,000" or "133.9 million dollars"

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 3, search for current HSR thresholds and EU/UK merger control authority
- Verify the 2023 DOJ/FTC Merger Guidelines are still in effect (confirmed February 2025)
- Search for recent agency decisions in the relevant product/sector markets
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail
- Save research results to `/tmp/legalcode-merger-authority.md`

**Without legalcode-mcp:**

- Use the thresholds in this skill as a starting baseline, but mark all [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Recommend that the user verify all thresholds against current FTC, EC, and CMA
  guidance before filing or advising

**Third-party tools that may be integrated:**

- **Competition economics tools**: UPP calculators, merger simulation models
- **Filing management systems**: Track filings, waiting periods, and deadlines across
  jurisdictions
- **Document management**: Item 4(c) document collection and review workflow

---

## Glass Box Audit Trail

Append this YAML block to every delivered analysis:

```yaml
glass_box:
  skill_name: "legalcode-antitrust-merger-review"
  mode: "Created from scratch"
  topic: "Antitrust pre-merger notification and merger control"
  jurisdictions:
    [
      "US (HSR Act / Clayton Act)",
      "EU (EC Regulation 139/2004)",
      "UK (Enterprise Act 2002)",
    ]
  enhancement_type: "Create"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[/tmp/legalcode-merger-authority.md / Not created]"
  quality_score: "[X]/40"
  completeness: "18/18 elements"
  citations_verified: "[N VERIFIED] / [M UNVERIFIED — all marked [VERIFY]]"
  thresholds_current_as_of: "[Date verified — VERIFY annually in February for HSR, on legislative change for EU/UK]"
  filing_obligations_identified: "[List jurisdictions where filing required / not required / uncertain]"
  competitive_classifications:
    - "[Market 1: COMPLIANT / FLAG / BLOCKING]"
    - "[Market 2: COMPLIANT / FLAG / BLOCKING]"
  gun_jumping_risk_level: "[HIGH / MEDIUM / LOW / NONE]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "All numerical thresholds must be verified against current official sources before filing"
    - "Competitive market share figures are user-supplied and not independently verified"
    - "Analysis does not cover merger notifications outside US/EU/UK"
    - "Does not constitute a filing or merger clearance opinion"
  reviewer: "AI-assisted — requires qualified antitrust counsel review before reliance"
```

---

## Localization Notes

### United States — Key Localization Points

- **HSR filing fees**: Updated annually alongside thresholds; check FTC website each February
- **Pre-merger notification form**: Significantly expanded as of January 2025; Item 4(c)
  scope broadened; "supervisory deal team lead" concept is new
- **Early termination**: Reinstated October 2024 but remains discretionary; not available
  for problematic transactions
- **2023 Merger Guidelines**: Reaffirmed by FTC and DOJ in February 2025 as the
  applicable enforcement framework; more interventionist than 2010 guidelines
- **State attorneys general**: May bring parallel antitrust challenges under state law
  even where federal review is completed

### European Union — Key Localization Points

- **Article 22 referrals**: Post-_Illumina/Grail_ CJEU decision, the scope of Article 22
  for sub-threshold deals remains contested; flag for digital, pharma, and strategic deals
- **Pre-notification process**: EC strongly encourages pre-notification contacts; typically
  2–8 weeks before formal notification; clock does not start until notification is "complete"
- **Member State filings**: Even with EU dimension, some Member States may retain parallel
  jurisdiction for specific regulated sectors (media, financial services)
- **Remedies timing**: EU Phase I remedy offer window (Day 20) is strict; missing it means
  Phase II referral

### United Kingdom — Key Localization Points

- **Voluntary system risk**: No mandatory filing, but CMA investigates 4 months post-
  completion or announcement. For deals with UK overlaps, proactive engagement is
  strongly recommended
- **Phase 2 powers**: CMA Phase 2 panel acts independently of Phase 1 team; different
  panel may reach a different conclusion on the same facts
- **Behavioral remedies**: The CMA's conditional clearance of Vodafone/Three (December 2024)
  with behavioral commitments (investment, tariff caps, MVNO access) signals potential
  openness in infrastructure sectors, but this remains sector-specific
- **JCRA (Jersey Competition Regulatory Authority) and other Crown Dependencies**: For
  deals with material UK Crown Dependency revenues, separate filings may be required

---

## Multi-Jurisdictional Timeline Matrix

| Event                           | US HSR                                       | EU                                                            | UK                                              |
| ------------------------------- | -------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------- |
| Signing of definitive agreement | Day 0: Filing obligation triggered           | Day 0: Standstill obligation begins                           | Day 0: 4-month clock starts (post-announcement) |
| Filing submission               | Typically 10–30 days after signing           | Typically 2–8 weeks after signing (pre-notification + formal) | Voluntary — no fixed deadline                   |
| Review clock starts             | At submission                                | At "complete" notification                                    | At formal filing acceptance                     |
| Phase I ends                    | Day 30 (Day 15 cash tender)                  | Day 25 (or Day 35 with remedy)                                | ~Day 40                                         |
| Phase II (if triggered)         | Second Request — compliance 4–12 months      | Day 25+90 = ~5.5 months from notification                     | ~6 months from Phase 2 reference                |
| Estimated total timeline        | 1–3 months (clean) / 8–18 months (contested) | 1–2 months (Phase I) / 5–8 months (Phase II)                  | 2–4 months (Phase 1) / 8–14 months (Phase 2)    |

**Practical note**: Sequence filings to begin in all jurisdictions as close to
simultaneously as possible. The deal cannot close until the longest-lead jurisdiction
clears. Staggered filings extend the total timeline unnecessarily.

---

## Output Format Template

Deliver the final analysis using this template:

```markdown
# Antitrust Merger Analysis — [Transaction Name]

**Date**: [Date]
**Prepared by**: Legalcode Antitrust Merger Review (AI-assisted — requires legal review)
**Confidential — Attorney-Client Privilege / Attorney Work Product** [if applicable]

---

## 1. Executive Summary

[2–4 sentence summary of overall antitrust risk profile and recommended actions]

**Overall risk level**: LOW / MEDIUM / HIGH

---

## 2. Filing Obligation Summary

| Jurisdiction         | Filing Required?     | Threshold Basis         | Waiting Period | Estimated Filing Date |
| -------------------- | -------------------- | ----------------------- | -------------- | --------------------- |
| United States (HSR)  | YES / NO / UNCERTAIN | [Threshold met/not met] | 30 days        | [Date]                |
| European Union       | YES / NO / UNCERTAIN | [Threshold met/not met] | Phase I: 25 WD | [Date]                |
| United Kingdom       | YES / VOLUNTARY / NO | [Threshold met/not met] | Phase 1: 40 WD | [Date]                |
| [Other jurisdiction] |                      |                         |                |                       |

**Note**: All thresholds require independent verification. [VERIFY all figures]

---

## 3. Competitive Effects Assessment

### [Market 1 Name]

- **Classification**: COMPLIANT / FLAG / BLOCKING
- **Parties' shares**: [X%] + [Y%] = [Z%] post-merger
- **Theory of harm** (if FLAG/BLOCKING): [Description]
- **Countervailing factors**: [Entry, buyer power, efficiencies]
- **Recommended action**: [Specific next step]
- **Confidence**: [DEFINITE / HIGH / PROBABLE / POSSIBLE]

[Repeat for each market]

---

## 4. Gun-Jumping Risk Assessment

**Overall gun-jumping risk**: HIGH / MEDIUM / LOW / NONE

| Risk Item                       | Jurisdiction   | Risk Level       | Action            |
| ------------------------------- | -------------- | ---------------- | ----------------- |
| [Specific conduct or provision] | [US / EU / UK] | HIGH / MED / LOW | [Specific action] |

**Clean-team recommendation**: [YES — specify protocol / NO — not required]

---

## 5. Clearance Timeline Recommendation

**Critical path jurisdiction**: [Longest-lead authority]
**Estimated overall clearance timeline**: [X months]
**Recommended deal condition**: [Specific language for merger agreement conditions]

| Milestone               | Date   |
| ----------------------- | ------ |
| Signing                 | [Date] |
| HSR filing              | [Date] |
| EU notification         | [Date] |
| UK engagement           | [Date] |
| HSR waiting period ends | [Date] |
| EU Phase I decision     | [Date] |
| UK Phase 1 decision     | [Date] |
| Estimated closing       | [Date] |

---

## 6. Remedy Strategy (if applicable)

**Remedy required**: YES / POSSIBLY / NO

[If yes or possibly:]

- **Affected market(s)**: [Market name(s)]
- **Recommended remedy approach**: [Structural / Behavioral / Fix-it-first]
- **Proposed package**: [Description of divestiture or commitment]
- **Estimated timeline impact**: [Additional time for remedy negotiation and clearance]

---

## 7. Recommended Next Steps

**Immediate (within 1 week):**

- [ ] [Action 1]
- [ ] [Action 2]

**Within 2 weeks:**

- [ ] [Action 1]

**Ongoing:**

- [ ] [Action 1]

---

## 8. Glass Box Audit Trail

[Append the YAML audit trail block here]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on deep research into US HSR
Act and DOJ/FTC enforcement practice, EU Merger Regulation 139/2004 and Commission
procedures, UK Enterprise Act 2002 and CMA guidance (post-January 2025 threshold reform),
market definition methodology (SSNIP/hypothetical monopolist test), competitive effects
frameworks from 2023 DOJ/FTC Merger Guidelines, gun-jumping enforcement precedent
(EU Altice decision, US civil penalty practice), and multi-jurisdictional merger practice
from leading competition law firms.

Reference standard: `skills/general/contracts/legalcode-contract-review/SKILL.md`
Research date: 2026-03-21. Thresholds verified against FTC, EC, and CMA official sources.
All numerical thresholds should be re-verified before use as they adjust periodically.
