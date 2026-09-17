---
name: legalcode-eu-competition-law-assessment
description: 'Assess EU competition law compliance across all major enforcement pillars: Article 101 TFEU
  (anti-competitive agreements, cartels, block exemptions including VBER 2022/720 and horizontal BERs),
  Article 102 TFEU (abuse of dominant position, predatory pricing, exclusivity rebates, tying, margin
  squeeze, post-Intel AEC test), EU Merger Regulation 139/2004 (EU dimension thresholds, Phase I/II review,
  gun-jumping, SIEC test, Article 22 post-Illumina/GRAIL), State Aid (Articles 107-109 TFEU, GBER 651/2014,
  De Minimis 2023/2831), dawn raid preparedness (Regulation 1/2003 Article 20, legal privilege, digital
  evidence), and EU leniency programmes (cartel immunity, fine reductions, corporate statements, private
  damages interaction under Directive 2014/104/EU). Use when conducting competition law compliance reviews,
  assessing agreements, evaluating dominance risk, screening M&A transactions, advising on state aid eligibility,
  preparing for or responding to Commission inspections, or advising on leniency filings.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Assess EU competition law compliance across all major enforcement pillars: Article 101 TFEU (anti-competitive agreements, cartels, block exemptions including VBER 2022/720 and horizontal BERs), Article 102 TFEU (abuse of dominant position, predatory pricing, exclusivity rebates, tying, margin squeeze, post-Intel AEC test), EU Merger Regulation 139/2004 (EU dimension thresholds, Phase I/II review, gun-jumping, SIEC test, Article 22 post-Illumina/GRAIL), State Aid (Articles 107-109 TFEU, GBER 651/2014, De Minimis 2023/2831), dawn raid preparedness (Regulation 1/2003 Article 20, legal privilege, digital evidence), and EU leniency programmes (cartel immunity, fine reductions, corporate statements, private damages interaction under Directive 2014/104/EU). Use when conducting competition law compliance reviews, assessing agreements, evaluating dominance risk, screening M&A transactions, advising on state aid eligibility, preparing for or responding to Commission inspections, or advising on leniency filings. Covers Digital Markets Act (DMA) gatekeeper interface. Jurisdiction: European Union — Article 101/102 TFEU, Regulation 139/2004, Regulation 1/2003, ECN+ Directive 2019/1.


# EU Competition Law Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted EU competition law
> analysis. It does not constitute legal advice. All outputs must be reviewed by a
> qualified competition lawyer licensed in the relevant jurisdiction before use. EU
> competition law evolves rapidly through Commission decisions, ECJ/GCEU judgments,
> and revised guidelines — verify currency of all references before relying on them.
> Statutory and case law references cited from memory carry hallucination risk; verify
> against authoritative sources (EUR-Lex, EU competition policy portal, or legalcode-mcp)
> before relying on any citation. This skill covers EU-level competition law; Member State
> national competition law (NCAs) may impose additional or divergent obligations.

---

## Purpose and Scope

This skill conducts systematic EU competition law assessments for undertakings operating
in the EU internal market. It evaluates compliance across all major enforcement pillars
and produces a confidence-scored, actionable report with a Glass Box audit trail.

**Covers:**

- Article 101 TFEU: anti-competitive agreements, cartels, block exemptions (VBER, R&D BER, Specialisation BER), horizontal cooperation, de minimis
- Article 102 TFEU: dominance assessment, abusive practices (predatory pricing, exclusive rebates, tying/bundling, margin squeeze, refusal to supply, discriminatory pricing, data leveraging)
- EU Merger Regulation 139/2004: EU dimension, mandatory filing obligations, gun-jumping, SIEC test, Phase I/II, Article 22 referral (post-Illumina/GRAIL ECJ September 2024)
- State Aid: Articles 107-109 TFEU, GBER Regulation 651/2014 as amended, De Minimis Regulation 2023/2831, notification and standstill, recovery risk
- Dawn Raid Preparedness: Regulation 1/2003 Article 20 inspection powers, legal professional privilege (EU Akzo standard), digital evidence, step-by-step response protocol
- Leniency: Commission Leniency Notice, immunity and fine reduction tiers, corporate statements, ECN coordination, interaction with Damages Directive 2014/104/EU
- DMA interface: Digital Markets Act gatekeeper obligations and intersection with competition law

**Does not:**

- Replace a qualified competition law opinion or outside counsel engagement
- Cover national competition law of individual Member States (beyond noting NCA interactions)
- Cover merger filings under non-EU jurisdictions (US HSR, UK CMA, etc.)
- Provide legal advice or guarantee any regulatory outcome

---

## Jurisdiction and Governing Law

**Jurisdiction**: European Union — primary EU competition law only.

**Core legal framework**:
| Instrument | Citation | Subject |
|-----------|---------|---------|
| Treaty on the Functioning of the EU | Arts. 101-109 TFEU | Core prohibitions (cartels, dominance, state aid) |
| Enforcement Regulation | Regulation 1/2003/EC | Commission and NCA enforcement powers |
| Merger Regulation | Regulation 139/2004/EC | Mandatory pre-merger notification |
| Vertical BER | Regulation 2022/720/EU | Safe harbour for vertical agreements |
| R&D BER | Regulation 1217/2010/EU | Safe harbour for R&D cooperation |
| Specialisation BER | Regulation 1218/2010/EU | Safe harbour for specialisation agreements |
| GBER | Regulation 651/2014/EU (as amended by 2023/1315) | State aid block exemptions |
| De Minimis (State Aid) | Regulation 2023/2831/EU | €300,000 over 3-year threshold |
| Damages Directive | Directive 2014/104/EU | Private antitrust enforcement |
| ECN+ Directive | Directive 2019/1/EU | NCA minimum powers |
| Digital Markets Act | Regulation 2022/2554/EU | Gatekeeper obligations |

**Key Guidelines and Notices** (non-binding but highly influential):

- Vertical Restraints Guidelines 2022 (2022/C 248/01)
- Horizontal Cooperation Guidelines 2023
- De Minimis Notice (10% horizontal / 15% vertical market share safe harbours)
- Market Definition Notice 2024 (SSNIP / SSNDQ / HMT)
- 2024 Draft Article 102 Guidelines (not yet final — cite with caution)
- Commission Leniency Notice 2006/C (as updated)
- Merger Remedies Notice 2008/C 267/01

**NCA Interaction**: EU competition law is enforced in parallel by the Commission
(DG COMP) and national competition authorities (NCAs) under Regulation 1/2003. NCAs may
apply more stringent national rules to unilateral conduct. Always identify relevant
NCA(s) and check for any parallel national proceedings.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming business context, the workflow pauses and asks when:

- The answer would change which enforcement pillar(s) to assess
- Market share data is unavailable and the safe-harbour analysis cannot proceed
- Deal structure or aid amounts are unclear and affect threshold calculations
- The organisation's role (state, undertaking, grantor, recipient) is ambiguous

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

### Step 1: Accept the Assessment Request

Accept inputs in any of these formats:

- **Description of conduct / agreement**: Narrative describing the commercial relationship, transaction, or practice to assess
- **Document(s)**: Distribution agreement, joint venture agreement, merger SPA/term sheet, state aid measure, internal policy, rebate scheme description
- **Specific question**: "Do our exclusive distribution agreements comply with VBER?" or "Does our proposed acquisition require EC notification?"
- **Dawn raid response request**: "Inspectors just arrived — guide us"

**⟁ CLARIFY** — If the request is broad or covers multiple pillars, ask:

1. **Scope of assessment**: Which pillars should this analysis cover?
   - Options: All pillars (full competition audit), Article 101 only (agreements), Article 102 only (dominance), Merger clearance, State aid eligibility, Dawn raid preparedness, Leniency assessment, Specific pillar(s) — specify
   - _Why this matters_: A full competition audit takes substantially longer than a single-pillar review.

2. **Organisation type**: What describes the requesting entity?
   - Options: Private undertaking (corporation/partnership), Public authority / Member State body, Trade / industry association, Individual executive / employee, Outside counsel advising a client
   - _Why this matters_: State aid analysis applies to grantors and recipients differently; NCA privilege rules differ for in-house counsel.

3. **Industry / sector**: What sector does the organisation operate in?
   - Options: Pharmaceutical / life sciences, Digital platforms / technology, Financial services, Energy / utilities, Transport, Healthcare, Consumer goods / FMCG, Industrial / manufacturing, Other (specify)
   - _Why this matters_: Certain sectors have sector-specific competition rules and higher enforcement priority (pharma, digital, energy).

4. **Urgency**: What is the time context?
   - Options: Dawn raid in progress (immediate — skip straight to Step 7), Pre-transaction filing (days/weeks), Compliance review (weeks), Strategic planning (no hard deadline)

### Step 2: Gather Business Context

Collect the following before proceeding with substantive analysis. Ask if not provided:

- **Market shares**: Estimated share of each party in the relevant market(s). If unknown, note and flag that block exemption safe harbours cannot be confirmed.
- **Geographic scope**: In which Member States (and beyond) does the conduct/agreement apply?
- **Duration**: When did/does the arrangement begin and end? Duration matters for block exemption assessment.
- **Counter-party relationships**: Are the parties actual or potential competitors (horizontal), or at different supply chain levels (vertical)?
- **Revenue/turnover**: Worldwide and EU-wide turnover for merger threshold calculation. For state aid: total aid amounts received over 3 years.

**⟁ CLARIFY** — If market share data is unavailable:

- "Without market share estimates, I cannot confirm that block exemption safe harbours apply. Should I: (A) proceed with a qualitative analysis and flag safe harbour status as unconfirmed, or (B) provide a framework for you to confirm safe harbour status once you have share data?"

### Step 3: Research Legal Authority

Use **legalcode-mcp** (if connected) or web research to build a working legal reference
for this assessment.

**Research targets:**

1. Current block exemption thresholds and expiry dates for the relevant BER
2. Any relevant Commission decisions or ECJ/GCEU judgments in the same sector or on the same conduct type
3. Pending guidelines revisions (e.g., 2024 Draft Article 102 Guidelines; TTBER revision effective May 2026)
4. NCA enforcement activity in the relevant Member States
5. DG COMP enforcement priorities for the current year

**Save results** to `/tmp/legalcode-eu-competition-research.md` with:

```markdown
# EU Competition Law Research — [Matter Name]

## Date: [date]

## Pillars: [list of pillars assessed]

### Relevant Block Exemptions

- [BER name, Regulation number, market share thresholds, expiry date]

### Commission Decisions (same sector/conduct)

- [Decision, date, key holding]

### ECJ/GCEU Case Law

- [Case, citation, key holding, confidence: VERIFIED/UNVERIFIED]

### NCA Enforcement Notes

- [NCA, activity, relevance]

### Recent Guidelines/Notices

- [Title, date, relevant provisions]
```

**If legalcode-mcp is not connected:**

- Proceed with general knowledge of EU competition law
- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — all citations require independent verification"`

### Step 4: Article 101 TFEU Assessment

#### 4a. Identify the Nature of the Arrangement

Classify the arrangement:

| Type                             | Characteristics                                                                      | Key Analysis                                                          |
| -------------------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| **Hard-core horizontal cartel**  | Price-fixing, market allocation, output restriction, bid-rigging between competitors | Per se violation — no exemption possible                              |
| **Other horizontal cooperation** | R&D, specialisation, joint venture, information exchange, sustainability agreement   | Must pass through applicable BER or Art. 101(3) individual assessment |
| **Vertical agreement**           | Between parties at different supply chain levels (supplier/distributor)              | VBER 2022/720 analysis; check for hardcore restrictions               |
| **Hub-and-spoke**                | Indirect horizontal coordination via common supplier/platform                        | Treated as horizontal; per se risk                                    |
| **Association of undertakings**  | Trade body decision facilitating coordination                                        | Full Art. 101 analysis applies to association and members             |

#### 4b. Screen for Hard-Core Cartel Conduct

Apply this bright-line test first. If **any** of the following are present, classify as **CRITICAL — CARTEL RISK** and proceed directly to the Leniency Assessment section:

- [ ] Price-fixing: any agreement on prices, pricing components, floor prices, or minimum advertised prices between competitors
- [ ] Market allocation: division of customers, territories, or product lines between competitors
- [ ] Output restriction: agreements to limit production, supply, or sales volumes between competitors
- [ ] Bid-rigging: coordinated tender responses; cover bids; bid rotation; bid suppression
- [ ] Exchange of individualised, non-public forward-looking pricing or capacity data between competitors

> **⟁ CLARIFY** — If the conduct appears to involve competitor coordination but the user is uncertain: "Does this arrangement involve any sharing of individual price lists, future pricing intentions, capacity plans, or customer-specific terms with competitors, even indirectly through an industry association, trade platform, or common supplier?" A yes answer triggers cartel risk analysis regardless of intent.

#### 4c. Block Exemption Assessment (VBER — Vertical Agreements)

Apply for supplier/distributor, franchisor/franchisee, or online platform/seller arrangements.

**Commission Regulation (EU) 2022/720 — Safe Harbour Conditions:**

| Condition                                               | Threshold       | Status                 |
| ------------------------------------------------------- | --------------- | ---------------------- |
| Supplier's market share on supply market                | ≤30%            | ✅ / ❌ / ❓ (unknown) |
| Buyer's market share on purchase market                 | ≤30%            | ✅ / ❌ / ❓ (unknown) |
| Agreement contains no hardcore restriction              | See list below  | ✅ / ❌                |
| Agreement contains no excluded restriction beyond scope | Per Art. 5 VBER | ✅ / ❌                |

**VBER 2022/720 Hardcore Restrictions (automatic exclusion from safe harbour):**

| Restriction                         | Description                                                                                   | Common Manifestations                                                                                                 |
| ----------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **RPM**                             | Fixing or minimum resale prices                                                               | Price floors, minimum advertised price (MAP) enforced with penalties, rebate systems tied to maintaining price levels |
| **Territorial confinement**         | Restricting active or passive sales in exclusive territories (beyond limited permitted scope) | Prohibitions on cross-border sales, customer list restrictions                                                        |
| **Cross-supply prohibition**        | Restricting distributors in selective distribution from selling to each other                 | Blocking inter-distributor trade within the network                                                                   |
| **Online sales ban**                | Prohibiting the effective use of the internet as a sales channel                              | Absolute prohibition; charging higher prices for online vs. offline sales                                             |
| **Component supplier restrictions** | Restricting OEM customers from selling components to non-authorised repairers                 | Aftermarket foreclosure                                                                                               |

**Art. 5 Excluded Restrictions** (severable — do not void whole agreement):

- Non-compete obligations exceeding 5 years (or indefinite)
- Post-term non-compete obligations (generally excluded unless limited to 1 year)
- Selective distribution obligations restricting active/passive sales of competing brands

**New VBER 2022 features to flag:**

- Shared exclusivity (up to 5 exclusive distributors per territory now permitted under conditions)
- Online sales: prohibition on exclusive online channel can be acceptable if matched by offline equivalent
- Retail parity (MFN) clauses: narrow scope permissible; wide scope (cross-platform) generally excluded under revised guidelines

**Classification:**

- Both thresholds met + no hardcore restrictions = **COMPLIANT (safe harbour)**
- Either threshold exceeded but no hardcore restrictions = **PARTIAL** — individual Art. 101(3) assessment required
- Hardcore restriction present = **NON-COMPLIANT** regardless of market share

#### 4d. Block Exemption Assessment (R&D and Specialisation — Horizontal)

**R&D BER (Regulation 1217/2010):**

- Combined market share of parties ≤25% on affected market(s)
- Joint exploitation of results permitted for 7 years from first EU market introduction
- No hardcore restrictions (price-fixing, output limits, market allocation of R&D results)

**Specialisation BER (Regulation 1218/2010):**

- Combined market share ≤20% (applies to both upstream and downstream markets if intermediary products)
- Covers unilateral and reciprocal specialisation; joint production
- No hardcore restrictions

**Horizontal Cooperation Guidelines 2023 — Information Exchange:**
Exchange of competitively sensitive information (prices, volumes, capacities, customer lists) between competitors is presumptively anti-competitive where:

- Information is individualised (company-specific, not aggregated)
- Data is current or forward-looking (not historical — generally >12 months old is safer)
- Information relates to strategic variables (price, volume, capacity)

**⟁ CLARIFY** — If the arrangement involves an industry association collecting member data: "Does the association collect and distribute individualised (per-member) or aggregated data? At what level of aggregation? What is the time lag before distribution?" The answers determine whether the exchange is presumptively anti-competitive.

#### 4e. Article 101(3) Individual Exemption Assessment

Where no block exemption applies, assess whether the arrangement qualifies for individual exemption. All four conditions must be cumulatively satisfied:

| Condition                        | Test                                                                                           | Evidence Required                                       |
| -------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| 1. Efficiency gains              | Agreement produces objective economic benefits (cost savings, innovation, quality improvement) | Quantifiable efficiencies with supporting data          |
| 2. Consumer benefit              | Consumers receive a fair share of efficiency gains                                             | How and when benefits pass through to consumers         |
| 3. Indispensability              | Restrictions are necessary to achieve the efficiencies — no less restrictive alternative       | Why the restriction is essential, not merely convenient |
| 4. No elimination of competition | Agreement does not eliminate competition for a substantial part of products                    | Residual competitive constraint remains                 |

**Sustainability objective (2022/2023 development):** The updated Guidelines acknowledge sustainability agreements may qualify where they generate benefits (e.g., climate, environmental) that accrue to broader society, even if not all benefits directly pass to purchasing consumers. This is an evolving area — mark assessments with [VERIFY currency].

### Step 5: Article 102 TFEU Assessment

#### 5a. Market Definition

Define the relevant market before assessing dominance. Apply the 2024 Market Definition Notice framework:

**Product Market:**

- Demand-side substitutability: what do customers consider interchangeable based on characteristics, price, intended use?
- Supply-side substitutability: can suppliers switch production to the relevant products quickly?
- Apply the SSNIP test (Small but Significant Non-transitory Increase in Price — typically 5-10%): would customers switch to substitutes, making the price increase unprofitable?
- For zero-price markets: apply SSNDQ test (quality decrease) instead of SSNIP
- For innovation markets: quality, pipeline products, and R&D investment may define the market

**Geographic Market:**

- Area where conditions of competition are sufficiently homogeneous
- Consider transport costs, regulatory barriers, consumer preferences, price differentials across regions

**⟁ CLARIFY** — If market definition is contested or uncertain: "The relevant market significantly affects the dominance assessment. Can you provide: (1) which products/services the organisation considers direct competitors, and (2) the geographic area in which the organisation competes for customers? I will flag where market definition uncertainty affects my dominance assessment."

#### 5b. Dominance Assessment

| Market Share | Presumption                                            |
| ------------ | ------------------------------------------------------ |
| ≥50%         | Strong presumption of dominance (Hoffmann-La Roche)    |
| 40-50%       | Possible dominance — requires additional factors       |
| 25-40%       | Unlikely dominant absent additional structural factors |
| <25%         | Very unlikely to be dominant                           |

**Additional factors indicating dominance:**

- Duration of high market share (temporary spikes are less significant)
- Barriers to entry (regulatory, IP, network effects, switching costs, scale economies)
- Buyer power of customers (weak buyers = more likely dominant)
- Access to essential infrastructure or data
- Vertical integration

**Super-dominance (>90% share):** Subject to heightened obligations; even conduct legal for normally dominant firms may be abusive.

#### 5c. Abusive Conduct Assessment

For each identified practice, apply the applicable test:

**Predatory Pricing:**

- Is pricing below Average Variable Cost (AVC)? → Presumptively abusive (Akzo criterion)
- Is pricing above AVC but below Average Total Cost (ATC) with evidence of intent to eliminate? → Potentially abusive
- Apply As-Efficient-Competitor (AEC) test: would a competitor with the same cost structure be able to compete profitably?

**Exclusivity Rebates and Loyalty Discounts (post-Intel ECJ October 2024):**

- Commission MUST conduct AEC test — presumption of illegality for exclusivity rebates no longer applies
- Assess: (1) coverage of the rebate scheme (% of total purchases); (2) incremental pricing (effective price for contestable volume); (3) duration and individualisation; (4) market coverage
- Rebates foreclosing an equally efficient competitor → abusive; rebates not foreclosing such competitor → not automatically abusive
- Document economic evidence proactively if designing rebate schemes

**Tying and Bundling:**

- Dominant position in tying product + leveraged into tied product market
- Customers coerced (contractual tying, technical tying, conditional guarantees)
- No objective justification (quality, safety, technical necessity)
- Tends to foreclose competition in tied market

**Margin Squeeze:**

- Dominant vertically-integrated firm sets wholesale access price so high that downstream competitors cannot profitably replicate retail operations
- Test: retail price minus incumbent's downstream costs vs. wholesale price charged to rivals

**Refusal to Supply:**

- Withdrawal of existing supply relationship: lower threshold for abuse
- Initial refusal to supply essential facility: conditions — (1) facility is essential and cannot be replicated, (2) refusal prevents emergence of new product, (3) refusal economically unjustified
- Data refusal: increasingly relevant — refusal to provide access to data essential for competition in downstream market

**Excessive Pricing (Article 102(a)):**

- Two-stage United Brands test: (1) significant cost-price gap; (2) price unfair in itself or compared to competing products
- Highly fact-specific; Commission generally reluctant to pursue absent sector-specific mandate
- Expanding enforcement in pharma, energy, digital (flag with [VERIFY] — active area of development)

**Discriminatory Pricing:**

- Applying dissimilar conditions to equivalent transactions with different trading partners
- Must distort competition (between trading partners, or vis-à-vis end consumers)

**Data Leveraging (modern abuse):**

- Combining data across platform services without genuine consent
- Refusing interoperability to lock in users
- Self-preferencing own downstream services using data advantage from upstream platform
- _Note_: Digital Markets Act (Regulation 2022/2554) overlaps here for designated gatekeepers

**Classification for Article 102:**

- Conduct present + evidence of foreclosure = **NON-COMPLIANT**
- Conduct present + AEC test passed + objective justification documented = **COMPLIANT**
- Conduct borderline or market share <40% = **PARTIAL** — monitor and document

### Step 6: EU Merger Regulation Assessment

#### 6a. EU Dimension Calculation

Test both alternative thresholds:

**Primary Threshold (Art. 1(2) EUMR):**

- Combined worldwide turnover of all parties > €5 billion, **AND**
- EU-wide turnover of each of at least two parties > €250 million
- **Negative condition**: Not applicable if each party achieves more than 2/3 of EU-wide turnover in a single Member State (2/3 rule → national jurisdiction)

**Secondary Threshold (Art. 1(3) EUMR):**

- Combined worldwide turnover > €2.5 billion
- In each of at least 3 Member States, combined turnover > €100 million
- In the same 3 Member States, each of at least 2 parties has turnover > €25 million
- EU-wide turnover of each of at least 2 parties > €100 million
- **Negative condition**: Same 2/3 rule applies

**Turnover Calculation rules:**

- Include subsidiaries and affiliates (Regulation 139/2004 Art. 5)
- Exclude intra-group sales
- Use most recent audited financial statements
- Exclude VAT and other taxes

**⟁ CLARIFY** — If turnover data is uncertain: "Please provide: (1) most recent audited worldwide turnover for each party (including affiliates), (2) breakdown of turnover in each EU Member State. I cannot confirm EU dimension without these figures."

#### 6b. Gun-Jumping Risk Assessment

Assess whether parties are observing the standstill obligation (Art. 7 EUMR):

- No implementation of merger before EC clearance
- No exchange of competitively sensitive information beyond what is necessary for due diligence (with appropriate clean-team protocols)
- No integration steps (coordinating pricing, sales teams, customers) pre-clearance
- Integration planning is permitted; execution must wait for clearance

**Gun-jumping red flags:**

- Joint customer announcements or sales activities before clearance
- Sharing competitively sensitive information without clean-team protocols
- Acquiring minority shareholding with de facto influence over strategy
- Granting exclusive distribution rights pending clearance

**Precedent fine: Illumina/GRAIL (2023)** — €432 million fine for pre-clearance implementation [VERIFY current status of any appeal].

#### 6c. SIEC Test Assessment

For overlapping product/geographic markets, assess:

- **Unilateral effects**: post-merger, can the combined entity profitably raise prices, reduce quality/output, without being constrained by remaining competitors?
- **Coordinated effects**: does the merger increase the likelihood of tacit collusion among remaining players?
- **Vertical/conglomerate effects**: does the merger foreclose input or customer access for rivals?

#### 6d. Article 22 Referral (Post-Illumina/GRAIL, ECJ September 2024)

**ECJ ruling (Case C-611/22 P, September 3, 2024):** Commission cannot accept Article 22 referrals from NCAs that themselves lack domestic merger control jurisdiction over the transaction.

**Current position:**

- Article 22 referrals remain available where the referring NCA has domestic jurisdiction over the transaction
- Killer acquisitions (no EU dimension, no national dimension) now largely escape EC review
- Parties to below-threshold transactions in innovation sectors (pharma, biotech, digital) should assess whether any NCA has domestic jurisdiction to refer

**Practical implication:** Document proactively why a transaction falls below all thresholds, as the risk of referral is reduced but not eliminated in jurisdictions with domestic merger control.

### Step 7: State Aid Assessment

#### 7a. Four-Element Test (All Must Be Met for State Aid)

| Element                         | Question                                                                                           | Notes                                                                        |
| ------------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **1. Advantage**                | Does the measure confer an economic benefit the recipient could not obtain on normal market terms? | Compare to hypothetical private market operator (private investor test)      |
| **2. State resources**          | Is the measure funded by or attributable to a public authority?                                    | Includes publicly controlled entities, tax exemptions, guarantees            |
| **3. Selectivity**              | Does the measure benefit specific undertaking(s) rather than a general economic policy?            | Sector-wide measures may still be selective if justified by nature of scheme |
| **4. Trade/competition effect** | Does it distort or threaten to distort competition and affect trade between Member States?         | Presumed where beneficiary operates in a market open to inter-EU trade       |

If all four elements are present: **State aid** — notification and standstill obligation applies unless exemption (GBER or De Minimis) applies.

#### 7b. GBER Assessment (Regulation 651/2014 as amended by 2023/1315)

Identify whether the aid measure fits a GBER category:

| GBER Category              | Maximum Intensity (indicative) | Notes                                                  |
| -------------------------- | ------------------------------ | ------------------------------------------------------ |
| R&D (fundamental research) | Up to 100%                     | Lower for industrial research/experimental development |
| SME support                | Various                        | SME status must be verified per Annex I GBER           |
| Environmental/climate      | 35-65%                         | Enhanced rates for green investment (2023 amendment)   |
| Regional development       | 10-50% (region-dependent)      | Based on Assisted Areas map                            |
| Training                   | 50-70%                         | Lower for large enterprises                            |
| Employment                 | Varies                         | Job creation/disadvantaged workers                     |
| Broadband infrastructure   | Up to 100% in white areas      | Must pass open access conditions                       |
| Culture/heritage           | Up to 100%                     | Subject to conditions                                  |

**GBER compliance checklist:**

- [ ] Measure fits within a GBER category
- [ ] Aid intensity does not exceed GBER maximum
- [ ] Incentive effect present (aid applied for before project started)
- [ ] No unlawful aid condition (recipient not in financial difficulty per GBER Art. 1(4)(c))
- [ ] Transparency reporting complete (publish on state aid transparency database if >€100k)
- [ ] Individual aid >€500k requires notification to Commission (GBER Art. 9)

**Classification if GBER compliant:** **COMPLIANT** — no notification required; publish on transparency database.

#### 7c. De Minimis Assessment (Regulation 2023/2831)

| Criterion      | Condition                                                                                                             |
| -------------- | --------------------------------------------------------------------------------------------------------------------- |
| Amount         | ≤€300,000 to single recipient over any 3-year rolling period                                                          |
| Scope          | Any sector except: primary agricultural production, fisheries/aquaculture, export aid, preferential domestic products |
| Cumulation     | Must consider all de minimis aid from all sources to same recipient in same period                                    |
| Record-keeping | Grantor must maintain records for 10 years; recipient for 10 years                                                    |

**Classification if De Minimis compliant:** **COMPLIANT** — no notification or transparency requirement.

#### 7d. Recovery Risk Assessment

If aid has been granted without notification where required:

- Recovery obligation is automatic upon EC finding of unlawful aid
- Recipient must repay principal plus compound interest from date of granting
- 10-year limitation period for Commission recovery action
- National courts may order immediate recovery pending Commission investigation

**Classification:** **NON-COMPLIANT** — immediate notification to Commission strongly recommended; legal counsel required.

### Step 8: Dawn Raid Preparedness Assessment

**⟁ CLARIFY** — If a dawn raid is in progress, skip the assessment and go directly to the **Immediate Dawn Raid Response Protocol** subsection below.

#### 8a. Preparedness Evaluation

Assess the organisation's readiness across these domains:

| Domain                      | Key Questions                                                                                                                                                                       | Status       |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **Response team**           | Is there a pre-identified dawn raid coordinator? External competition counsel on speed dial? Clear authority chain?                                                                 | ✅ / ❌ / ❓ |
| **Privilege management**    | Has the organisation obtained legal opinions from external (not in-house) counsel on sensitive competition issues? Are those opinions clearly marked as privileged?                 | ✅ / ❌ / ❓ |
| **Digital preparedness**    | Can IT quickly identify and isolate relevant email accounts/servers? Are cloud credentials known? Are mobile devices managed?                                                       | ✅ / ❌ / ❓ |
| **Document retention**      | Is there a clear records retention policy? Is there a litigation hold protocol?                                                                                                     | ✅ / ❌ / ❓ |
| **Staff training**          | Do employees know: (1) to immediately notify the dawn raid coordinator on arrival; (2) not to delete or alter documents; (3) their right to silence for self-incriminating answers? | ✅ / ❌ / ❓ |
| **Facilities**              | Are there designated areas that can be used for inspector supervision? Is reception trained to receive officials?                                                                   | ✅ / ❌ / ❓ |
| **Privilege claim process** | Is there a clear process to assert legal professional privilege over documents and seek Commission review?                                                                          | ✅ / ❌ / ❓ |

#### 8b. Legal Professional Privilege (EU Standard — Critical Note)

**External counsel communications: PRIVILEGED (if EEA-qualified advocate)**

- All written communications with external counsel for purposes of rights of defence are privileged (AM&S/Akzo Noble standard)
- Privilege is not limited to litigation — extends to advice on whether conduct may infringe competition law

**In-house counsel communications: NOT PRIVILEGED under EU law**

- ECJ Akzo Nobel (2010): in-house lawyer communications are NOT protected by EU legal professional privilege before the Commission
- **Critical divergence**: Many Member States provide in-house counsel privilege in national proceedings — but EC inspectors apply EU standards, not national standards
- **Practical implication**: All sensitive competition analysis should be commissioned from and addressed by external counsel; in-house analysis of competition risks is discoverable in EC investigations

**Documents covered by national LPP only:**

- During EC investigations, Commission applies EU standard — national privilege provides no protection against Commission inspectors
- Assert claims and request sealed envelope procedure; pursue judicial review if claim denied

#### 8c. Immediate Dawn Raid Response Protocol

Follow this sequence if inspectors arrive:

**Phase 1 — Arrival (first 15 minutes)**

1. Receive officials professionally; do not obstruct entry
2. Ask to see the written inspection decision (authorisation): note the scope, date, signing official, and precise premises covered
3. Call external competition counsel immediately — give them the decision reference number
4. Call the dawn raid coordinator / senior management
5. Do NOT call competitors, other third parties, or discuss the raid publicly

**Phase 2 — During Inspection** 6. Assign a senior employee to accompany each inspector at all times — document everything they touch 7. Record names and badge numbers of all officials 8. Do NOT delete, move, or alter any documents or data — obstruction is a criminal/regulatory offence with severe penalties 9. **Right to silence**: Employees may decline to answer questions that could incriminate themselves personally (not a right for the company to withhold documents) 10. Preserve your right to privilege: if inspectors request communications with external counsel, clearly state the claim and request the document be placed in a sealed envelope pending resolution 11. Do NOT volunteer information beyond the scope of the decision; answer factual questions accurately 12. For digital evidence: require officials to specify exactly what they are seeking before accessing email systems; note what is accessed

**Phase 3 — Sealing** 13. If inspectors seal rooms or devices at end of day, treat seals as inviolable — breaking a seal without prior authorisation carries severe penalties (E.ON: €38 million fine for tampering) 14. Keep a contemporaneous log of all sealed materials and the sealing procedure 15. Inspectors typically return within 2-3 working days; ensure premises are accessible

**Phase 4 — Post-Raid** 16. Conduct an immediate debrief with external counsel — document what was seen, accessed, and copied 17. Activate litigation hold: preserve all potentially relevant documents across all media 18. Do NOT destroy documents — anticipate follow-up information requests (Art. 18 Regulation 1/2003) 19. Prepare for formal requests for information; engage counsel before responding 20. Consider whether any conduct revealed during the raid triggers a leniency application

### Step 9: Leniency Assessment

#### 9a. Leniency Programme Structure

**Immunity (Tier 1 — Full Immunity from Fines):**

- First undertaking to submit evidence enabling the Commission to carry out a targeted inspection OR establish an infringement
- Conditions: terminate participation immediately; cooperate fully and continuously; do not destroy evidence; do not disclose application
- Corporate statements filed orally to prevent Damages Directive Art. 6 disclosure to claimants

**Fine Reduction (Tiers 2-4):**
| Applicant | Maximum Reduction | Condition |
|-----------|-----------------|----------|
| First reduction applicant | 30-50% | Significant added value over Commission's existing evidence |
| Second reduction applicant | 20-30% | Significant added value |
| Subsequent applicants | Up to 20% | Some added value |

**Marker system:**

- Applicant can file oral marker preserving priority while preparing full submission
- Marker valid for limited period (typically 8 weeks for immunity; shorter for reductions)
- Confirm marker in writing immediately after oral filing

#### 9b. Corporate Statements (Critical Protection)

- Corporate statements are oral or written submissions made exclusively for leniency purposes
- Protected from disclosure to private damages claimants under Damages Directive Art. 6(6)
- Do NOT incorporate documentary evidence into the corporate statement — documentary evidence is separately disclosable
- All corporate statements should be prepared by and delivered through external counsel

#### 9c. ECN Coordination

- Leniency applications filed with the Commission do not automatically provide protection in NCAs
- ECN Model Leniency Programme exists but is non-binding — individual NCAs have separate procedures
- For EU-wide cartels, file leniency applications simultaneously with Commission and relevant NCAs on the same day (ECN Leniency Network facilitates this)
- Settlement procedure (10% additional reduction): available for non-immunity applicants; Commission may use; consider if strengthened case for defendant

#### 9d. Interaction with Private Damages Claims (Directive 2014/104/EU)

- Commission decision finding infringement creates rebuttable presumption of harm for private claimants in national courts
- Damages Directive Art. 6 protects: leniency corporate statements; settlement submissions
- Pre-existing documents submitted in leniency are NOT protected — claimants can request disclosure
- Leniency does not eliminate private liability — model consent orders, settlement discussions, and litigation strategy must be planned in parallel
- Immunity from Commission fines does NOT confer immunity from private damages

---

## Severity Classification Framework

Classify each finding across the five enforcement pillars:

| Classification              | Meaning                                                                                                                                                                                                             | Action Required                                                                                             |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **CRITICAL**                | Hard-core cartel conduct (Art. 101(1) object restrictions); gun-jumping; unlawful state aid already disbursed without notification                                                                                  | Cease conduct immediately; engage external counsel; assess leniency; notify Commission                      |
| **NON-COMPLIANT**           | Arrangement or conduct outside applicable block exemption/safe harbour without plausible Art. 101(3) or Art. 102 objective justification; clear abuse of dominance; state aid without notification or GBER coverage | Remediate within defined timeframe; restructure arrangement; seek individual exemption or notify Commission |
| **PARTIAL**                 | Arrangement outside block exemption due to market share excess or excluded restriction; conduct by near-dominant firm requiring monitoring; state aid borderline GBER compliance                                    | Individual assessment required; risk mitigation measures; monitor market share; document justification      |
| **COMPLIANT (conditional)** | Within block exemption safe harbour; conduct passes AEC test with documentation; aid within GBER/De Minimis with proper record-keeping                                                                              | Maintain conditions; re-assess at threshold points; set review triggers                                     |
| **COMPLIANT**               | Conduct clearly outside scope of prohibition; agreement with no competitive concern; dominance absent; aid within De Minimis; dawn raid protocol fully implemented                                                  | Document position; periodic review recommended                                                              |

---

## Prioritisation Framework

### Priority 1 — Immediate Action (Critical)

Issues requiring action before any further commercial steps:

- Hard-core cartel conduct (price-fixing, market allocation, bid-rigging, output restriction)
- Gun-jumping: parties have implemented pre-clearance merger steps
- State aid disbursed without notification where required (recovery risk)
- Dawn raid in progress: immediate protocol activation required
- Document destruction during or after dawn raid (obstruction)

### Priority 2 — High Priority (Non-Compliant / Time-Sensitive)

Issues requiring resolution within 30-90 days:

- Agreements outside block exemption with no plausible Art. 101(3) justification
- Clear abuse of dominance with ongoing harm (exclusionary pricing, refusal to supply)
- State aid notifiable but not yet notified (standstill breach risk if proceeding)
- Missing clean-team protocols in live M&A transaction
- No dawn raid preparedness plan in high-risk enforcement sector

### Priority 3 — Medium Priority (Partial / Monitoring Required)

Issues requiring attention within 3-6 months:

- Agreements outside safe harbour requiring individual assessment documentation
- Market share approaching dominance thresholds (30-40%)
- State aid measures requiring GBER compliance documentation or transparency reporting
- In-house counsel engaged in competition analysis (privilege risk)
- Information exchange with competitors without aggregation/time-lag protocols

### Priority 4 — Low Priority (Compliant / Best Practice)

Issues to address as part of ongoing compliance program:

- Updating distribution agreements for VBER 2022/720 (transitional period expired May 31, 2023)
- Staff competition compliance training refresh
- Periodic market share review to confirm block exemption status
- Annual dawn raid readiness exercise
- Updating leniency contact list (competition counsel, senior management)

---

## Citation Quality Gates

Run these 5 gates silently before delivering any finding. If any gate fails, revise before delivery.

| Gate           | Rule                                                                                                                                                                | Fail Action                                                                                               |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Source**     | Every competition law claim cites a specific TFEU article, Regulation, Commission Notice, or established ECJ/GCEU case                                              | Add citation or mark `[UNVERIFIED — counsel to confirm]`                                                  |
| **Format**     | All citations follow EU legal citation format (e.g., "Regulation (EU) 2022/720"; "Case C-413/14 P Intel v Commission")                                              | Fix format to match EUR-Lex standard                                                                      |
| **Currency**   | Every cited provision checked against current law: BERs have expiry dates; guidelines are revised; case law may be appealed or reversed                             | Flag `[CHECK CURRENCY — provision may have been amended or superseded]`                                   |
| **Domain**     | Analysis stays within EU-level competition law; national competition law divergences flagged as separate and not asserted as EU law                                 | Remove jurisdictional bleed; add note on national law interaction                                         |
| **Confidence** | Uncertainty explicitly stated, not hidden — especially for 2024 Draft Art. 102 Guidelines (not yet final) and evolving enforcement areas (data, AI, sustainability) | Add confidence qualifier; mark evolving areas with `[EVOLVING AREA — verify current Commission position]` |

---

## Self-Interrogation for CRITICAL and NON-COMPLIANT Findings

For any finding classified at CRITICAL or NON-COMPLIANT, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**

- Does the classification follow logically from the cited provision and the facts?
- Would the Commission / ECJ actually reach this conclusion on these specific facts?
- Is there a counter-argument (objective justification, Art. 101(3) exemption, AEC test pass) that needs to be addressed?

**Pass 2 — Completeness**

- Have all relevant block exemptions, safe harbours, and guidelines been considered?
- Have any relevant Commission sector-specific rules or precedents been missed?
- Has NCA enforcement in the relevant Member State been checked?

**Pass 3 — Challenge**

- What is the strongest argument that the conduct IS compliant?
- Under what documented business justification might the Commission accept this practice?
- Is the CRITICAL/NON-COMPLIANT classification proportionate, or should it be PARTIAL with conditions?

Mark the audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

---

## Confidence Scoring

| Level        | Range     | Meaning                                                                                                     | Action                                                                        |
| ------------ | --------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled EU law, clear ECJ jurisprudence, unambiguous regulation text                                        | State with confidence; cite provision                                         |
| **High**     | 0.80-0.94 | Strong authority, minor interpretation questions (e.g., market definition uncertainty within defined range) | State with brief caveat                                                       |
| **Probable** | 0.60-0.79 | Good arguments but reasonable minds differ (e.g., Art. 101(3) assessment, excessive pricing analysis)       | State with reasoning and contra-indicators; recommend external counsel review |
| **Possible** | 0.40-0.59 | Genuinely uncertain — evolving enforcement (data abuses, algorithmic collusion, sustainability agreements)  | Flag for qualified competition counsel; present both sides                    |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative — do not assert                                                                     | Flag as `[UNCERTAIN — competition counsel to advise]`                         |

---

## Anti-Patterns

Explicit catalogue of what NOT to do in EU competition law assessment:

1. **Treating the de minimis safe harbour as applying to hardcore restrictions** — The De Minimis Notice (10%/15% market share thresholds) explicitly does NOT apply to object restrictions (cartels). No market share threshold exempts price-fixing or market allocation. This is the most dangerous misconception in Article 101 analysis.

2. **Assuming VBER covers the arrangement without checking both parties' market shares** — VBER 2022/720 requires BOTH the supplier's AND the buyer's market share to be ≤30%. Checking only the supplier's share is an incomplete analysis that may lead to false comfort.

3. **Using the 2009 Art. 102 Enforcement Priorities Guidance as settled law post-Intel** — The ECJ October 2024 Intel judgment and the 2024 Draft Article 102 Guidelines significantly revise the framework for exclusionary conduct, particularly rebates. Citing the 2009 Guidance for rebate analysis as current law is an error.

4. **Ignoring the Illumina/GRAIL ECJ ruling on Article 22** — As of September 3, 2024, the Commission cannot accept Article 22 referrals from NCAs without domestic merger control jurisdiction. Advising clients that killer acquisitions face EC review via Article 22 regardless of thresholds is no longer correct.

5. **Applying EU legal professional privilege standards to protect in-house counsel advice** — Under the EU Akzo Noble standard, communications with in-house lawyers are NOT privileged before the Commission, even if they are qualified lawyers. Telling clients their in-house legal advice is protected in an EC investigation is incorrect and creates serious risk.

6. **Recommending MAP (Minimum Advertised Price) policies as always legal** — MAP policies are treated as a form of RPM under VBER 2022 if they are enforced with sanctions and effectively set price floors. An unenforceable MAP recommendation carries lower risk; an enforced MAP that functions as a price floor is a hardcore restriction.

7. **Assessing EU dimension without the 2/3 rule** — The merger may meet the primary or secondary threshold but still escape EC jurisdiction if each party achieves more than 2/3 of its EU-wide turnover in a single Member State. Skipping the 2/3 rule check produces incorrect jurisdictional advice.

8. **Assuming GBER compliance without checking the incentive effect requirement** — GBER exemption requires that the aid measure creates an "incentive effect" — the project must not have started before the aid was applied for. Aid granted for projects that have already begun is not GBER-compliant even if the aid amount and intensity are within limits.

9. **Filing leniency corporate statements in writing as regular documents** — Corporate statements should be filed orally (or as clearly designated leniency submissions) to preserve protection from disclosure to private claimants under Damages Directive Art. 6. Written corporate statements drafted as standard business memos may be treated as ordinary documents and be disclosable.

10. **Breaking or touching sealed items during a dawn raid without explicit Commission authorisation** — Tampering with Commission seals triggers automatic sanctions and supports an inference of obstruction. The E.ON precedent (€38 million fine) illustrates the severity. Any business need to access sealed areas must be routed through external counsel to the Commission first.

11. **Advising that leniency immunity eliminates private damages exposure** — Commission immunity from fines is separate from private damages liability under Directive 2014/104/EU. Immunity applicants remain liable to compensate victims (except in certain circumstances for immunity applicants' own direct customers under some Member State implementations). Conflating the two creates client relations and liability risk.

12. **Applying VBER 2022 to agreements predating June 1, 2022 without checking the transitional period** — Agreements that complied with the old VBER 330/2010 had a transitional period until May 31, 2023. All vertical agreements must now comply with VBER 2022/720. Agreements not reviewed and updated since June 2022 may be non-compliant.

13. **Confusing concerted practices with lawful parallel behaviour** — Parallel price increases by competitors do not automatically constitute a concerted practice. Additional "plus factors" — direct contact, information exchange, market behaviour unexplained by oligopolistic interdependence — are required. Do not classify parallel behaviour as a concerted practice without positive evidence of coordination.

14. **Neglecting NCA parallel enforcement** — EU competition law is enforced by both DG COMP and NCAs. A transaction or practice compliant with EU-level rules may still face NCA enforcement under national law (which may be stricter for unilateral conduct). Always identify which NCA(s) have jurisdiction and whether they have active enforcement priorities in this area.

15. **Overlooking the sustainability cooperation exception in horizontal agreements** — The 2023 Horizontal Cooperation Guidelines explicitly acknowledge that sustainability agreements between competitors may qualify for Art. 101(3) exemption where benefits accrue to wider society. Applying a blanket "competitor cooperation = illegal" analysis to sustainability initiatives may be overly conservative and commercially harmful.

16. **Treating information exchange as automatically safe if aggregated** — Aggregated data sharing can still be anti-competitive if: the market is highly concentrated, competitors can reverse-engineer individual data from aggregates, or the frequency and granularity of aggregated data allows inference of individual competitive strategy. Always assess the specific aggregation level and market structure.

---

## Writing Standards

Apply plain-language discipline to all competition law assessment output:

**For findings and recommendations:**

- Lead with the classification: **CRITICAL / NON-COMPLIANT / PARTIAL / COMPLIANT**
- Name the specific provision: "Article 101(1) TFEU" not "the cartel prohibition"
- State the specific risk: "This arrangement fixes minimum resale prices — a hardcore restriction that voids the agreement under Article 101(2) and carries fines of up to 10% of worldwide group turnover"
- Not vague: "This may raise competition concerns" without identifying which ones is insufficient
- Provide a specific remediation step or decision fork, not a generic "seek legal advice"

**Confidence qualifiers:**

- Use consistently: "Definite", "High confidence", "Probable", "Uncertain"
- Do not hedge without explanation: if uncertain, explain why

**Quality gates before delivery:**

1. Does every CRITICAL/NON-COMPLIANT finding cite the specific provision that is violated?
2. Does every block exemption analysis state the market share threshold and whether it is met/not met/unknown?
3. Are evolving enforcement areas (data abuses, AI, sustainability, 2024 Draft Art. 102 Guidelines) flagged as current guidance rather than settled law?
4. Does the prioritisation clearly tell the client what to do first?
5. Is every legal claim backed by a citation, or marked [VERIFY]?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 3, search for current ECJ/GCEU judgments, Commission decisions, and NCA enforcement in the relevant sector
- Verify block exemption expiry dates and current market share thresholds
- Search for sector-specific enforcement priorities (digital, pharma, energy)
- Check whether any 2024/2025 guidelines revisions have been finalised (TTBER, Art. 102)
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — all citations require independent verification"`
- Focus analysis on structural risk assessment and procedural guidance rather than detailed case law
- Recommend that client verify all cited authorities before relying on them

---

## Output Format Template

Structure the final assessment as:

```markdown
## EU Competition Law Assessment

**Matter**: [description of conduct/arrangement/transaction]
**Pillars assessed**: [Article 101 / 102 / Merger / State Aid / Dawn Raid / Leniency]
**Organisation**: [entity type — undertaking / public authority / association]
**Sector**: [industry]
**Date of assessment**: [date]
**Assessment basis**: [legalcode-mcp-verified / general knowledge — [VERIFY] citations]

---

## Executive Summary

[3-5 bullet points — the most important findings with severity flags and one-line descriptions]

**Overall risk level**: CRITICAL / HIGH / MEDIUM / LOW

---

## Priority 1 Findings — Immediate Action Required

[Only present if CRITICAL findings exist]

### [Finding name] — CRITICAL

**Conduct**: [description]
**Provision violated**: [Art. 101(1) TFEU — object restriction: price-fixing]
**Why CRITICAL**: [specific risk and consequence — fines up to 10% worldwide turnover; agreement void; leniency window open]
**Immediate action**: [cease; engage external counsel; assess leniency]
**Self-interrogation**: [PASS / REVISED]
**Confidence**: [Definite — 0.97 — ECJ settled law on object restrictions]

---

## Priority 2 Findings — Non-Compliant

### [Finding name] — NON-COMPLIANT

**Conduct**: [description]
**Provision**: [specific TFEU article / Regulation / BER provision]
**Analysis**: [why it falls outside the safe harbour or constitutes abuse]
**Remediation**: [specific steps — restructure clause, reduce market share, document justification]
**Deadline**: [recommended timeline]
**Confidence**: [level]

---

## Priority 3 Findings — Partial (Monitoring Required)

### [Finding name] — PARTIAL

**Conduct**: [description]
**Issue**: [why it falls outside safe harbour or requires monitoring]
**Risk mitigation**: [specific steps to document or restructure]
**Review trigger**: [market share threshold; expiry date; next filing deadline]

---

## Compliant Findings

| Area                                   | Status    | Notes                                                            |
| -------------------------------------- | --------- | ---------------------------------------------------------------- |
| [Article 101 — distribution agreement] | COMPLIANT | VBER 2022/720 safe harbour confirmed — shares [X]%/[Y]%          |
| [State aid]                            | COMPLIANT | De Minimis — €[X] over 3 years — below €300,000 threshold        |
| [Merger]                               | COMPLIANT | No EU dimension — worldwide turnover €[X]bn below €5bn threshold |

---

## Dawn Raid Preparedness Assessment

[Only if scope included]

| Domain               | Status       | Priority Action |
| -------------------- | ------------ | --------------- |
| Response team        | ✅ / ❌ / ❓ | [action if ❌]  |
| Privilege management | ✅ / ❌ / ❓ | [action if ❌]  |
| Digital preparedness | ✅ / ❌ / ❓ | [action if ❌]  |
| Document retention   | ✅ / ❌ / ❓ | [action if ❌]  |
| Staff training       | ✅ / ❌ / ❓ | [action if ❌]  |

---

## Recommended Next Steps

[Specific actions, in priority order, with recommended owners and timelines]

1. **[Action]** — Owner: [Legal / External Counsel / Business] — By: [timeframe]
2. ...

---

## Glass Box Audit Trail

[See below — always append]
```

---

## Glass Box Audit Trail

Every EU competition law assessment output MUST include this audit section:

```yaml
glass_box:
  skill_name: "legalcode-eu-competition-law-assessment"
  matter: "[Matter name or description]"
  pillars_assessed:
    - "[Article 101 / 102 / Merger / State Aid / Dawn Raid / Leniency]"
  organisation_type: "[Undertaking / Public authority / Association / Individual]"
  sector: "[Industry]"
  market_share_data: "Provided / Not provided — safe harbour analysis conditional"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "[path to /tmp/legalcode-eu-competition-research.md or 'Not created']"
  statutes_consulted:
    - "Article 101 TFEU — VERIFIED / UNVERIFIED"
    - "Article 102 TFEU — VERIFIED / UNVERIFIED"
    - "Regulation 139/2004 (EUMR) — VERIFIED / UNVERIFIED"
    - "Regulation 2022/720 (VBER) — VERIFIED / UNVERIFIED"
    - "[additional provisions]"
  case_law_consulted:
    - "Intel v Commission, Case C-413/14 P (ECJ Oct 2024) — VERIFIED / UNVERIFIED"
    - "Illumina/GRAIL, Case C-611/22 P (ECJ Sep 2024) — VERIFIED / UNVERIFIED"
    - "[additional cases]"
  citations_verified: "[N VERIFIED] / [N UNVERIFIED]"
  critical_findings: "[number]"
  non_compliant_findings: "[number]"
  partial_findings: "[number]"
  compliant_findings: "[number]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL/NON-COMPLIANT findings)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "Market share data not provided — block exemption safe harbour status is conditional"
    - "2024 Draft Article 102 Guidelines not yet final — enforcement approach may shift"
    - "[any other scope limitations or assumptions]"
  reviewer: "AI-assisted — requires qualified competition lawyer review before reliance"
```

---

## Localization Notes

This skill covers EU-level competition law only. Member State national competition law
may impose additional obligations:

| Member State          | Notable Divergences                                                                                                                                         |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Germany**           | BKartA highly active; national merger control separate (turnover thresholds + transaction value >€400m); FCO leading in data/digital enforcement            |
| **France**            | Autorité de la concurrence active in pharma, digital, retail; national merger control (combined FR turnover €150m+ / party FR turnover €50m+)               |
| **Netherlands**       | ACM active; national merger control (combined NL turnover €150m+ / party NL turnover €30m+); separate sector-specific rules for telecoms                    |
| **Italy**             | AGCM active in digital, pharma, energy; national merger control (combined IT turnover €552m+ / party IT turnover €55m+ — 2024 thresholds [VERIFY])          |
| **Spain**             | CNMC active; national merger control (combined ES turnover €240m+ / party ES turnover €60m+)                                                                |
| **UK**                | Post-Brexit: CMA is independent authority; UK Merger Regulation applies (CMA Act 2002/2023); UK competition law generally mirrors EU but divergence growing |
| **All Member States** | In-house counsel LPP: EU law provides no privilege before Commission; national law varies — confirm applicable standard before any proceeding               |

For transactions or practices with significant activity in multiple Member States, identify
relevant NCAs and check for parallel national filing/assessment obligations.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis created via Mode A (Create New
Skill) workflow with 2-agent research pipeline. Legal research conducted via web search
across official EU sources (EUR-Lex, DG COMP competition policy portal), leading law
firm analyses (Ashurst, WilmerHale, White & Case, Cleary Gottlieb, Norton Rose
Fulbright, Covington, Paul Weiss), and academic legal resources. Key authorities verified
via web research: Regulation 2022/720 (VBER); Regulation 1/2003; Regulation 139/2004;
Regulation 2023/2831 (De Minimis); Directive 2014/104/EU (Damages Directive); Directive
2019/1 (ECN+); Intel v Commission ECJ October 2024; Illumina/GRAIL ECJ September 2024;
2024 Draft Article 102 Guidelines; 2024 Market Definition Notice; 2023 Horizontal
Cooperation Guidelines. All citations require independent verification against current
authoritative sources before reliance.
