---
name: legalcode-ca-competition-act-assessment
description: Assess Competition Act (R.S.C., 1985, c. Use when advising on competition law risk, building
  compliance programs, preparing for Bureau investigations, reviewing distribution or franchise agreements,
  conducting cartel self-audits, assessing merger filing obligations, or responding to Competition Bureau
  inquiries.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Assess Competition Act (R.S.C., 1985, c. C-34) compliance for Canadian businesses and counsel. Covers criminal cartel offences (price-fixing, market allocation, bid-rigging, wage-fixing, no-poach), civil reviewable matters (abuse of dominance, price maintenance, exclusive dealing, tied selling, refusal to deal), merger notification and substantive review (post-2024 amendments including repealed efficiency defence and rebuttable presumption), deceptive marketing practices (misleading advertising, drip pricing, greenwashing pre-substantiation obligations), Competition Bureau enforcement and investigation procedures, consent agreements, immunity and leniency programs, private rights of action expanded by Bills C-56 and C-59, and the section 90.1 non-competitor civil collaboration regime in force December 2024. Use when advising on competition law risk, building compliance programs, preparing for Bureau investigations, reviewing distribution or franchise agreements, conducting cartel self-audits, assessing merger filing obligations, or responding to Competition Bureau inquiries. Applies to Canada federal jurisdiction only; provincial competition law overlaps flagged where relevant.


# Legalcode Canada Competition Act Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted Competition Act compliance
> assessment. It does not constitute legal advice. All outputs must be reviewed by a qualified
> competition law practitioner licensed in Canada before any reliance or action. The Competition
> Act was substantially amended in 2022, 2023, and 2024 — verify that all cited provisions
> reflect current law. Statutory provisions and enforcement positions cited from memory carry
> hallucination risk. Mark any uncertain reference [VERIFY] and cross-check against the
> Competition Bureau's published guidelines and the current text of the Act before acting.

---

## Purpose and Scope

This skill assesses an organization's exposure under Canada's Competition Act and supports
counsel in building or reviewing compliance programs, evaluating specific transactions or
practices, and preparing responses to Competition Bureau inquiries.

**Covers:**

- Criminal cartel offences: price-fixing, market allocation, bid-rigging (ss. 45–47), and
  the 2023 per-se criminal wage-fixing and no-poach offences (s. 45(1.1))
- Civil reviewable matters: abuse of dominance (ss. 78–79 post-2024 two-part test), price
  maintenance (s. 76), refusal to deal (s. 75), exclusive dealing, tied selling, and market
  restriction (s. 77)
- Civil competitor collaboration and non-competitor agreements (s. 90.1, as expanded
  December 15, 2024)
- Merger notification obligations and substantive review (ss. 109–124, including repealed
  efficiency defence, rebuttable presumption, and elevated remedy standard)
- Deceptive marketing practices: misleading advertising (s. 74.01), drip pricing (s. 74.01(1.1)),
  and greenwashing pre-substantiation obligations (Bill C-59)
- Competition Bureau investigation and enforcement procedures (s. 11 orders, search and seizure,
  consent agreements, administrative monetary penalties)
- Immunity and leniency programs (including the September 2024 "disclosure first" model)
- Private rights of action (s. 36 civil damages; expanded Tribunal access effective June 20, 2025)
- Investment Canada Act interaction for foreign-investor merger review

**Does not cover:**

- Provincial consumer protection statutes (note: Ontario CPA, Quebec CPA, and similar
  provincial regimes run parallel to the federal Act for consumer-facing conduct)
- Securities law competition concerns (Competition Act/OSC interface)
- CASL (anti-spam) even where it overlaps with deceptive marketing
- Sector-specific regulatory exemptions (banking, insurance, regulated industries)
  without additional research

---

## Jurisdiction and Governing Law

**Statute**: Competition Act, R.S.C., 1985, c. C-34, as amended by:

- Bill C-19 (Budget Implementation Act, 2022, No. 1) — in force June 23, 2023
- Bill C-56 (Affordable Housing and Groceries Act) — Royal Assent December 15, 2023
- Bill C-59 (Fall Economic Statement Implementation Act, 2023) — Royal Assent June 20, 2024

**Enforcement body**: Competition Bureau Canada (an independent law enforcement agency
within Innovation, Science and Economic Development Canada); Commissioner of Competition.

**Adjudicative body**: Competition Tribunal (civil matters); Federal Court of Canada;
Superior Courts (criminal prosecutions via Public Prosecution Service of Canada).

**Private access**: s. 36 civil damages actions in superior courts of competent jurisdiction;
Tribunal access expanded as of June 20, 2025.

**Investment Canada Act** (R.S.C., 1985, c. 28 (1st Supp.)): Parallel review for acquisitions
by non-Canadians above prescribed thresholds; national security review at any value.

**Jurisdictional scope**: Federal legislation applicable throughout Canada. Note that
several provinces maintain their own consumer protection laws that may capture conduct
also reviewable under the federal Act. This skill covers federal Competition Act only.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The assessment area is unclear and would materially change the analytical path
- The organization's role in a market or transaction is ambiguous
- Risk tolerance or business justification is needed to determine severity
- A practice has plausible pro-competitive justification that changes the classification

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

### Step 1: Accept the Engagement

Accept input in any of these formats:

- **Factual summary**: Description of the business practice, transaction, or situation for assessment
- **Document**: Contract, agreement, distribution arrangement, franchise agreement, merger term sheet, or advertising copy for review
- **Question**: Specific Competition Act compliance question
- **Audit request**: Request to assess an organization's overall competition law risk profile

If the engagement scope is unclear, proceed to Step 2 to clarify before analysis.

---

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user these questions (skip those already answered):

1. **Assessment area**: Which area of the Competition Act is the primary focus?
   - Options: Criminal cartels and price-fixing, Wage-fixing / no-poach (labour markets),
     Bid-rigging, Abuse of dominance, Mergers and acquisitions, Distribution / vertical
     agreements, Deceptive marketing and advertising, Competition compliance program review,
     Competition Bureau investigation response, Full Competition Act risk audit
   - _Why this matters_: Determines the analytical depth and the workflow path through Steps 5–9.

2. **Organization type**: What is the client's role?
   - Options: Large corporation (dominant or potentially dominant market position),
     Mid-market business, Trade or industry association, Private equity / acquiror,
     Foreign company operating in Canada, Other
   - _Why this matters_: Exposure under abuse of dominance, merger notification, and s. 90.1
     depends heavily on market position and transaction structure.

3. **Industry sector**: What sector is the business in?
   - Options: Grocery / food retail, Digital platforms / technology, Financial services,
     Healthcare / pharma, Real estate / housing, Energy / resources, Manufacturing / industrial,
     Transportation / logistics, Other
   - _Why this matters_: The Bureau's 2025–2026 Annual Plan identifies grocery, housing, and
     digital markets as enforcement priority sectors. Industry-specific regulatory exemptions
     also vary.

4. **Urgency**: What is the context?
   - Options: Pre-transaction compliance review, Response to Bureau inquiry / investigation,
     Proactive compliance audit, Regulatory advice (no immediate filing or deadline), Urgent
     (Bureau contact or regulatory deadline imminent)
   - _Why this matters_: Determines whether the analysis must prioritize immediate risk
     mitigation steps (e.g., preserving privilege, issuing litigation holds, engaging counsel).

State assumptions explicitly when proceeding without full context.

---

### Step 3: Gather Legal Authority

Use **legalcode-mcp** to gather current legal authority relevant to the assessment.

**Research targets**:

1. Current text of Competition Act provisions applicable to the facts
2. Competition Bureau enforcement guidelines (abuse of dominance, mergers, wage-fixing, compliance programs)
3. Recent Competition Tribunal and Federal Court decisions on the assessed conduct type
4. Recent consent agreements and enforcement outcomes in the relevant industry sector
5. Bureau Annual Plan enforcement priorities for 2025–2026

Save results to `/tmp/legalcode-ca-competition-research.md` structured as:

```markdown
# Competition Act Authority Reference

## Assessment area: [area]

## Date: [date]

### Applicable Statutory Provisions

- [s. XX — current text or summary — amendment status]

### Bureau Guidelines and Policy Documents

- [Title, date, relevance]

### Recent Tribunal / Court Decisions

- [Case name, year, key holding]

### Recent Enforcement Actions (Consent Agreements, AMPs)

- [Party, year, remedy, relevance]

### Current Enforcement Priorities

- [Bureau Annual Plan priorities relevant to this assessment]
```

**If legalcode-mcp is not connected**:

- Mark all statutory references [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with knowledge of the Act through the June 2024 amendments, but flag that
  no verified authority file was created and independent verification is required

---

### Step 4: Identify the Applicable Assessment Modules

Based on the context gathered in Step 2, identify which assessment modules from Step 5
apply. Not every engagement requires all modules.

| Module                                | Trigger                                                                            | Key Provisions             |
| ------------------------------------- | ---------------------------------------------------------------------------------- | -------------------------- |
| **A — Criminal Cartels**              | Price-fixing, market allocation, bid-rigging, information sharing with competitors | ss. 45, 46, 47             |
| **B — Wage-Fixing / No-Poach**        | Labour agreements with competing employers; franchise no-poach                     | s. 45(1.1)                 |
| **C — Abuse of Dominance**            | Dominant firm conduct; exclusionary practices; excessive pricing                   | ss. 78–79                  |
| **D — Vertical Agreements**           | Distribution, franchise, exclusivity, tying, market restriction                    | ss. 75, 76, 77, 90.1       |
| **E — Mergers**                       | Acquisitions, minority investments, joint ventures, serial acquisitions            | ss. 91–124                 |
| **F — Deceptive Marketing**           | Advertising, pricing presentations, environmental claims                           | ss. 74.01–74.19            |
| **G — Trade Association Activity**    | Member meetings, information sharing, standards-setting                            | ss. 45, 90.1               |
| **H — Bureau Investigation Response** | Active Bureau inquiry or dawn raid                                                 | ss. 10, 11                 |
| **I — Compliance Program Review**     | Program adequacy, staff training, risk identification                              | Bureau Compliance Bulletin |
| **J — Private Rights of Action**      | Defending or pursuing s. 36 claims; Tribunal private access                        | ss. 36, 90.1 (June 2025)   |

Apply all triggered modules in Step 5. Flag which modules are in scope in the Glass Box
audit trail.

---

### Step 5: Substantive Assessment

Apply each triggered module. Classify findings using the four-tier system:

| Classification    | Meaning                                                                                | Action                                                                         |
| ----------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **CRITICAL**      | Per-se criminal exposure or material civil enforcement risk requiring immediate action | Immediate legal privilege assertion, document preservation, counsel engagement |
| **NON-COMPLIANT** | Clear or probable statutory violation requiring remediation                            | Cease conduct; remediate; assess voluntary disclosure or leniency              |
| **PARTIAL**       | Practice meets some compliance requirements but contains material gaps                 | Remediate gaps; implement monitoring; document business justification          |
| **COMPLIANT**     | No identified violation under current law; note any watchpoints                        | Document compliance basis; monitor for regulatory developments                 |

---

#### Module A: Criminal Cartels (ss. 45–47)

**Assessment trigger**: Any agreement, arrangement, or understanding with a competitor
(actual or potential) touching on price, output, customers, or territories.

**Critical red flags — per-se criminal liability**:

_Section 45(1) — Price-Fixing and Market Allocation:_

- Agreements with competitors to fix, maintain, increase, or control prices for any product
- Agreements with competitors to allocate sales, territories, customers, or markets
- Agreements with competitors to fix, maintain, control, prevent, lessen, or eliminate production
  or supply of any product
- Any "concerted action" or "common understanding" — formal agreement is not required
- **Penalty**: Indictable offence — imprisonment up to **14 years** and/or fine at court's
  discretion (no statutory maximum; removal of C$25M cap is in force)

_Section 47 — Bid-Rigging:_

- Any agreement to not submit a bid, withdraw a bid, or submit a bid with pre-agreed terms
  without the knowledge of the bid caller
- Covers public procurement, private tendering, and any competitive bidding process
- No market effects need to be shown — conduct is per-se criminal
- **Penalty**: Indictable offence — imprisonment up to 14 years and/or fine at court's discretion

_Section 46 — Foreign-Directed Conspiracies:_

- Corporations in Canada implementing directives from foreign persons giving effect to an
  offshore conspiracy that would violate s. 45 if formed in Canada
- **Penalty**: Fine at court's discretion — no maximum

**Defences available**:

- **Ancillary Restraints Defence** (s. 45(4)): The restraint is ancillary to a broader
  agreement between the same parties, directly related to and reasonably necessary to give
  effect to that broader agreement, and the broader agreement is not itself criminal
- **Regulated Conduct Defence**: Conduct required or authorized by federal or provincial law
- **Environmental Collaboration Exemption** (new, Bill C-59): Bureau may issue a certificate
  exempting a collaboration from ss. 45/90.1 where it achieves a genuine environmental benefit

**Downstream exposure**:

- Debarment from federal government procurement under the Integrity Regime (Public Services
  and Procurement Canada) — automatic for ss. 45, 47 convictions
- Civil class action exposure under s. 36 — Bureau leniency does NOT insulate from
  private litigation
- Quebec and Ontario courts have issued personal prohibition orders against individuals
  in cartel cases

**Assessment checklist — Module A**:

- [ ] Does the company have any agreements, formal or informal, with competitors concerning price?
- [ ] Do employees discuss pricing, bids, or market allocation at trade association events?
- [ ] Does the company use third-party pricing algorithms? Are competitors using the same algorithm?
      [Note: Bureau and international enforcers have signalled algorithmic pricing coordination is
      a cartel enforcement priority — [VERIFY] current Bureau position]
- [ ] Are there any joint ventures, information-sharing arrangements, or cooperation agreements
      with competitors? Have these been assessed for ARD eligibility?
- [ ] Are company employees aware that criminal penalties extend to individuals, not just corporations?

---

#### Module B: Wage-Fixing and No-Poach (s. 45(1.1))

**In force**: June 23, 2023 (Bill C-19 amendment)

**Assessment trigger**: Any agreement or arrangement with an employer whose employees
perform similar functions to your employees (i.e., any employer that is a competitor in
the labour market).

**Per-se criminal offences**:

- Agreement with a competing employer to **fix, maintain, decrease, or control wages, salaries,
  or other terms of employment** — this includes benefit packages, equity compensation, working
  hours, and any terms of employment
- **Mutual** no-poach agreements: agreement with a competing employer not to **solicit or hire**
  each other's employees

**Important scope limitations**:

- Captures only **mutual** arrangements between competing employers — a unilateral no-poach
  imposed by one party on the other (e.g., a franchisor prohibiting franchisees from hiring
  franchisor staff) is not captured (but may be subject to civil review under ss. 77 or 90.1)
- The **Ancillary Restraints Defence** applies: a no-poach embedded in a legitimate broader
  commercial agreement (e.g., an M&A transaction where the seller covenants not to poach
  acquired employees during the transition period) may qualify if the restriction is ancillary
  and reasonably necessary to the transaction
- **Employer association bargaining**: collective bargaining through an employer association
  to set wages with trade unions is NOT captured (exempted by s. 4(1.1))

**Assessment checklist — Module B**:

- [ ] Does the company have any agreements (explicit or implicit) with other employers not to
      poach or hire from each other?
- [ ] Does the company participate in any multi-employer salary surveys or wage benchmarking
      programs where real-time or forward-looking data is shared? [Note: historical, aggregated,
      and sufficiently anonymized data carries lower risk — [VERIFY] Bureau guidance on wage survey safe harbour]
- [ ] For franchise systems: does the franchise agreement contain a clause prohibiting franchisees
      from hiring each other's employees? Is it unilateral or mutual in effect?
- [ ] Have existing no-poach provisions in commercial agreements been reviewed against the
      new criminal standard?
- [ ] Is HR leadership trained on the criminal nature of wage-coordination with competing employers?

**Penalty**: Indictable offence — imprisonment up to 14 years and/or fine at court's discretion.

---

#### Module C: Abuse of Dominance (ss. 78–79)

**Applicable test (post-Bill C-56)**:

The Competition Tribunal may make an order under s. 79 if satisfied of:

1. **Substantial market power** (dominance): one or more persons substantially or completely
   control a class or species of business throughout Canada or any area thereof
2. **Either** (a) OR (b):
   - (a) A **practice of anti-competitive acts** (requires anti-competitive intent or purpose)
   - (b) Conduct that **substantially lessens or prevents competition** in a market in which
     the dominant firm has a plausible competitive interest (no intent required; "superior
     competitive performance" defence available)

**Full remedy package** (including AMPs) requires proof of **all three**: dominance + practice
of anti-competitive acts + substantial lessening/prevention of competition.

**Administrative monetary penalties** (s. 79 — post-2024):

- Greater of: **C$25 million** (first order) / C$35 million (subsequent orders), OR three
  times the economic benefit derived from the conduct, OR 3% of annual worldwide gross revenues

**Section 78 — Anti-competitive acts (non-exhaustive list)**:

- Squeezing the margins of a competitor that also buys from the dominant firm
- Buying up product to prevent its resale by competitors
- Pre-empting scarce facilities or resources to deny competitors access
- Adopting product specifications incompatible with competitors' products
- Requiring customers to deal exclusively with the dominant firm
- Selling articles at a price below acquisition cost to discipline or eliminate a competitor
- Denying competitors access to an essential facility
- **Now expressly includes** (Bill C-59): **directly or indirectly imposing excessive and
  unfair selling prices** — a significant addition targeting monopoly pricing

**Assessment checklist — Module C**:

- [ ] Does the company have market shares exceeding 50% in any product or geographic market?
      (Indicative threshold — dominance is not defined by fixed market share; [VERIFY] Tribunal guidance)
- [ ] Does the company impose loyalty rebates, exclusivity requirements, or MFN/most-favoured
      customer clauses on buyers that have the effect of foreclosing competitors?
- [ ] Does the company's pricing to downstream customers involve any margin squeeze relative
      to input costs?
- [ ] Post-Bill C-59: Are the company's prices in any market significantly above competitive
      levels, and is there a risk the Bureau characterizes this as excessive and unfair pricing?
- [ ] Does the company own or control any bottleneck infrastructure, data, or input that
      competitors require access to?
- [ ] Are any refusals to deal with competitors or suppliers documented with a pro-competitive
      rationale?

---

#### Module D: Vertical Agreements and Distribution (ss. 75–77, 90.1)

**Section 75 — Refusal to Deal**:

- A supplier who refuses to supply a customer where: (i) the customer is substantially affected
  in whole or **part** of its business (amended — previously "entire business"), (ii) the customer
  is willing to meet normal trade terms, (iii) the supplier has ample supply, and (iv) the refusal
  has an adverse effect on competition in a market for any product
- Includes refusal to supply **diagnostic or repair information** or related parts
  (Right to Repair — Bill C-19)

**Section 76 — Price Maintenance**:

- A civil reviewable practice where a supplier attempts to influence upward the resale price
  of a product, or refuses to supply because a reseller is selling below suggested price
- Covers both express price-fixing provisions and more subtle means of influence (e.g.,
  co-op advertising programs contingent on minimum price, withholding supply as "enforcement")

**Section 77 — Exclusive Dealing, Tied Selling, Market Restriction**:

- **Exclusive dealing**: Requiring a customer to deal only or primarily in products of the
  supplier, or refusing to supply unless the customer does so
- **Tied selling**: Requiring a customer to buy one product as a condition of supply of another
- **Market restriction**: Requiring a customer not to sell outside a defined territory or
  customer class
- Reviewable only where the practice is likely to **substantially lessen or prevent competition**

**Section 90.1 — Civil Competitor and Non-Competitor Collaboration** (as amended):

- _Before December 15, 2024_: Applied only to agreements between competitors.
- _Effective December 15, 2024_: Now also captures agreements between **non-competitors**
  where a "significant purpose" is to prevent or lessen competition, and the agreement does
  substantially prevent or lessen competition in a market
- Covers **past agreements** (retrospective application up to three years prior)
- Applies to distribution agreements, franchise arrangements, licensing agreements, joint
  ventures, and other commercial agreements between parties that are not horizontal competitors
  where competition concerns arise
- Potential remedies include prohibition and remedial orders; significant AMPs; disgorgement

**⟁ CLARIFY** — For distribution or franchise agreement review, ask:

- "Is the supplier/franchisor a dominant firm, a mid-market player, or a smaller company?
  The threshold for s. 77 and s. 90.1 concern scales with market power."
- "Does the agreement restrict price (minimum resale price), territory, or customers?
  Each triggers a different assessment track."

**Assessment checklist — Module D**:

- [ ] Do supply or distribution agreements contain exclusive dealing provisions?
- [ ] Do franchise agreements contain no-poach, territory restriction, or minimum price provisions?
- [ ] Are refusals to deal documented with objective criteria unrelated to pricing/competition?
- [ ] Have minimum advertised price (MAP) programs been structured to avoid being characterized
      as price maintenance (e.g., MAP caps only advertised price, not the resale price itself)?
- [ ] Have commercial agreements that are not between direct competitors been reviewed for
      s. 90.1 compliance following the December 2024 amendments?

---

#### Module E: Mergers and Acquisitions (ss. 91–124)

**Pre-merger notification — both thresholds must be met**:

- **Size-of-target** (2024): Book value of assets in Canada, or gross revenues from sales in/from/
  into Canada, exceeds **C$93 million**
- **Size-of-parties**: Combined assets in Canada, or annual gross revenues from sales in/from/into
  Canada, of all parties (including affiliates) exceed **C$400 million**
- **Filing fee** (2024): C$82,719.12
- **Waiting period**: 30 days from certified filing; additional 30 days from SIR compliance
- Criminal penalties for **gun-jumping** (completing a notifiable transaction before expiry of
  the waiting period): fine up to C$10,000/day and potential divestiture order

**Substantive review test**:
The Tribunal may block or remedy a merger that **substantially prevents or lessens competition**
(SPLC) in a market.

**New rebuttable presumption** (Bill C-56, in force):
A merger that **significantly increases concentration** in a market, or **significantly increases
the market share** of the merged entity, is presumed anti-competitive. The burden shifts to the
merging parties to rebut the presumption by demonstrating the merger will not substantially
prevent or lessen competition.

**Expanded merger review factors** (post-2024):

- Impacts on **labour markets**
- Effects from increases in market share (lower threshold than previously)
- Potential for express or **tacit coordination** post-merger
- **Serial acquisition** strategies — the Bureau may assess a pattern of acquisitions to evaluate
  cumulative competitive harm even where no individual acquisition meets the notification threshold

**Efficiency defence — REPEALED** (Bill C-56, December 15, 2023):
Section 96 has been deleted. Parties can no longer justify an anti-competitive merger on the
basis that efficiency gains outweigh competitive harm to competition.

**Elevated remedy standard** (post-2024):
Merger remedies must **restore competition to the level that would have prevailed but for the
merger** — materially more demanding than the former standard.

**Investment Canada Act (ICA) interaction**:

- Net benefit review for acquisitions by non-Canadians above thresholds (WTO-investor
  threshold approximately C$1.287 billion enterprise value as of 2024)
- National security review: no financial threshold — any investment, including minority
  stakes, may be reviewed if it "may be injurious to national security"
- The two regimes run concurrently and must both be satisfied before closing

**⟁ CLARIFY** — For merger assessments, ask:

- "Is this a domestic Canadian-to-Canadian transaction, or does it involve a non-Canadian
  acquiror? (ICA review obligation)"
- "Are there any existing commercial relationships between the parties? (Identifies
  vertical integration concerns alongside horizontal concentration)"
- "Is the acquiror engaged in a pattern of acquisitions in the same sector? (Serial
  acquisition risk post-2024)"

**Assessment checklist — Module E**:

- [ ] Do both notification thresholds (size-of-target and size-of-parties) need to be assessed
      against most recent audited financial data including affiliates?
- [ ] If no formal notification required, has the Bureau's informal guidance process been
      considered for transactions with potential market effects?
- [ ] Has the efficiency defence been removed from the merging parties' justification analysis?
- [ ] Have market concentration effects been modelled using HHI or equivalent methodology,
      with particular attention to the rebuttable presumption threshold?
- [ ] For serial acquisitions: has the cumulative competitive effect of recent acquisitions
      in the same market been assessed?
- [ ] Has ICA review been assessed separately from Competition Act review?

---

#### Module F: Deceptive Marketing Practices (ss. 74.01–74.19)

**Section 74.01 — Misleading Advertising (civil)**:

- Reviewable where a person makes a **materially false or misleading representation** to the
  public, whether express or implied, in any form of advertising, including digital, online,
  and social media
- **Ordinary consumer** test: the representation is assessed from the perspective of the
  ordinary consumer who will be affected by it
- **Penalty**: Greater of C$10 million (first order) / C$15 million (subsequent), OR three
  times the value of the benefit derived, OR 3% of annual worldwide gross revenues

**Section 74.01(1.1) — Drip Pricing (new, Bill C-59)**:

- Now expressly prohibited: advertising a price that cannot reasonably be attained because
  of **mandatory additional charges or fees** that are not disclosed upfront
- The full price (including all mandatory fees) must be disclosed at the outset
- Bureau enforcement examples: SiriusXM Canada (C$3.3M penalty), TicketNetwork (C$825K),
  Canada's Wonderland (active Tribunal proceedings)
- Applies to e-commerce, subscription services, event ticketing, travel, and any sector
  with mandatory ancillary fees

**Greenwashing — Bill C-59 (in force June 2024)**:

- Environmental claims must be based on **adequate and proper tests** conducted **before** the
  claim is published
- **Reversed burden of proof**: The party making the environmental benefit claim bears the burden
  of proving the claim is substantiated — a fundamental departure from prior law where the Bureau
  had to prove falsity
- Applies to claims about environmental or climate benefits of a product or a business activity
- Private access to the Tribunal to bring greenwashing claims (in force June 20, 2025)
- Applies to "net zero," "carbon neutral," "sustainable," "eco-friendly," and similar claims

**Section 74.10–74.11 — Deceptive Telemarketing**:

- Prohibited representations in telemarketing campaigns, including false prize promotions

**Assessment checklist — Module F**:

- [ ] Are all mandatory fees (delivery, platform fees, surcharges) included in the advertised
      price or prominently disclosed alongside the advertised price?
- [ ] Is all comparative pricing advertising (regular price vs. sale price) based on genuine
      prior list prices?
- [ ] Have all environmental / sustainability claims been substantiated by adequate and proper
      tests conducted before publication?
- [ ] For subscription or auto-renewal services: are renewal terms, price changes, and
      cancellation procedures prominently disclosed?
- [ ] Has the company's digital marketing and e-commerce pricing display been reviewed
      against the drip pricing prohibition?

---

#### Module G: Trade Association Activity

**Assessment trigger**: Any participation in trade association meetings, industry working
groups, standards bodies, or information-sharing arrangements.

**High-risk activities at association events**:

- Discussing or disclosing current, forward-looking, or disaggregated pricing, costs,
  margins, output levels, or customers
- Discussions about reducing supply, refusing to deal with specific customers, or coordinating
  responses to labour cost pressures
- Informal side-conversations at events between competitors outside the formal agenda

**Safe harbour framework** (Bureau guidance):

- Information sharing is lower risk where data is: (i) historical (typically 12+ months old),
  (ii) sufficiently aggregated (no individual company data identifiable), (iii) administered
  by an independent third party, and (iv) publicly available
- Sharing **current or forward-looking** price or output data among competitors carries
  CRITICAL exposure regardless of whether there is a formal agreement

**Assessment checklist — Module G**:

- [ ] Does the company have written trade association participation guidelines?
- [ ] Are employees briefed before each association meeting on what cannot be discussed?
- [ ] Is there a protocol for walking out of or objecting to discussions that cross the line,
      and documenting the objection?
- [ ] Are meeting minutes and communications from association participation reviewed by
      competition counsel?

---

#### Module H: Bureau Investigation Response

**Assessment trigger**: Receipt of a Bureau questionnaire, s. 11 order, search warrant,
or any informal Bureau contact.

**Immediate response protocol**:

1. **Preserve privilege immediately**: Identify all communications with legal counsel; instruct
   staff to route all Bureau-related communications through counsel; assert solicitor-client
   privilege over privileged documents before any production
2. **Issue a litigation hold**: Preserve all potentially relevant documents; suspend all
   routine document retention/deletion schedules immediately
3. **Engage outside competition counsel immediately**: Do not respond to any Bureau inquiry
   (including informal requests) without qualified competition counsel present or engaged
4. **Do not destroy or alter documents**: Obstruction of justice charges may apply

**Types of Bureau investigative tools**:

| Tool                              | Trigger                                              | Response Considerations                                                                                   |
| --------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Voluntary information request** | Initial outreach; no legal compulsion                | Discretion to decline without penalty; respond through counsel                                            |
| **Section 11 court order**        | Formal compelled production of documents and records | Mandatory compliance; subject to privilege claims; scope can be challenged                                |
| **Search warrant (s. 15)**        | Court-authorized entry and seizure                   | Compliance required; do not impede; document all seized items; assert privilege over legal communications |
| **Wiretap order**                 | Criminal cartel investigations                       | Rights to counsel; do not discuss the subject matter on any communication channel                         |
| **Formal examination (s. 11)**    | Compelled witness testimony                          | Right to counsel present; answers given under oath; privilege applies to legal advice received            |

**Dawn raid protocol** (if search warrant served):

1. Alert designated in-house counsel or external competition counsel immediately
2. Do not impede officers; greet them professionally
3. Request to review the warrant scope before production begins — do not consent to broader
   production than the warrant specifies
4. Identify and protect privileged materials (separate physically from production scope)
5. Document all items seized; request copy of the seizure inventory
6. Notify management; activate the litigation hold
7. Brief employees on their right to have counsel present during examination

---

#### Module I: Competition Compliance Program Review

**Bureau standard**: The Competition Bureau's Corporate Compliance Programs bulletin and
Core Principles document identify nine elements of a credible and effective program.

**Assessment framework**:

| Element                                | Assessment Questions                                                                                                                                                  | Weight |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **1. Senior management commitment**    | Is there a board-level policy? Does the CEO visibly champion the program? Is compliance tied to executive compensation?                                               | High   |
| **2. Designated compliance officer**   | Is there a named compliance officer with authority and resources? Does the officer report directly to board or CEO?                                                   | High   |
| **3. Risk assessment**                 | Is a formal competition risk assessment conducted at least annually? Does it account for the 2022–2024 amendments (wage-fixing, no-poach, s. 90.1 expansion)?         | High   |
| **4. Written policies and procedures** | Are there written policies for employees in high-risk functions (sales, pricing, HR, procurement, trade association participation)?                                   | High   |
| **5. Training**                        | Is role-specific training provided? Does HR training cover the wage-fixing/no-poach criminal offence? Does sales training cover price-fixing and information sharing? | High   |
| **6. Monitoring and auditing**         | Are periodic unannounced audits conducted? Is pricing data analyzed for anomalies consistent with coordination?                                                       | Medium |
| **7. Reporting mechanisms**            | Is there an anonymous reporting channel? Are reports acted on and tracked?                                                                                            | Medium |
| **8. Enforcement and discipline**      | Is disciplinary policy for violations stated clearly? Has it been applied?                                                                                            | Medium |
| **9. Review and updating**             | Has the program been updated to reflect the 2022–2024 legislative amendments? Is the next review scheduled?                                                           | High   |

**Bureau policy on compliance programs**:
A credible and effective program is recognized as a **mitigating factor** in civil enforcement
proceedings but does **not constitute a defence** to criminal charges. The Bureau expressly
distinguishes between cosmetic (paper) programs and genuine programs with operational impact.
A program in place during violations that were not detected will be scrutinized for genuine effectiveness.

---

#### Module J: Private Rights of Action

**Section 36 — Civil Damages for Criminal Contraventions**:

- Any person who suffers loss or damage from conduct contrary to **criminal provisions** (Part VI:
  ss. 45, 46, 47) may sue in superior court for: (i) proven damages; plus (ii) full costs of
  investigation and legal proceedings
- **Limitation period**: Two years from the date the plaintiff knew or reasonably ought to have
  known of the conduct
- Class actions are the primary private enforcement vehicle — Bureau leniency does not insulate
  from class action exposure

**Expanded Private Tribunal Access (in force June 20, 2025)**:
Private applicants may now bring applications to the Competition Tribunal for:

- Section 74.1 deceptive marketing practices (new — Bill C-59)
- Section 90.1 civil competitor/non-competitor collaboration (new — Bill C-59)

**Revised leave test (in force June 20, 2025)**:

- Applicant must show: (i) directly and substantially affected in **whole or part** of their
  business; OR (ii) it is in the **public interest** that leave be granted
- The public interest ground is a significant expansion that may enable environmental groups
  or NGOs to bring greenwashing claims under s. 74.1

**Disgorgement remedy (new — Bill C-59)**:

- Upon a successful private application, the Tribunal may order disgorgement of an amount not
  exceeding the **value of the benefit derived** from the conduct, distributed to the applicant
  and other affected persons
- This is a fundamental shift — previously, AMPs were payable only to the Crown

**Assessment checklist — Module J**:

- [ ] Has the company assessed its class action exposure for any past cartel participation,
      independent of any Bureau immunity or leniency application?
- [ ] For dominant firms or firms in B2B markets: has the potential for private Tribunal
      applications by competitors, distributors, or suppliers been considered post-June 2025?
- [ ] For businesses making environmental claims: has the greenwashing private enforcement
      risk been assessed given the reversed burden and June 2025 private access?

---

### Step 6: Classify and Prioritize Findings

After completing the applicable modules, consolidate findings and classify using the
four-tier severity system. Apply the prioritization framework:

**Prioritization Tiers**:

| Tier       | Label                | Criteria                                                                                 | Recommended Response Timeline                                                       |
| ---------- | -------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Tier 1** | Critical / Immediate | CRITICAL findings — active or probable criminal exposure; conduct that is per-se illegal | Immediate: engage competition counsel within 24 hours; consider immunity/leniency   |
| **Tier 2** | High / Near-Term     | NON-COMPLIANT findings — clear civil violation risk; consent agreement exposure          | Short-term: remediate within 30 days; assess voluntary Bureau engagement            |
| **Tier 3** | Medium / Planned     | PARTIAL compliance gaps — missing program elements; borderline practices                 | Planned: remediate within 90 days; implement monitoring                             |
| **Tier 4** | Low / Monitored      | COMPLIANT with watchpoints — no current violation; regulatory developments to track      | Monitor: track Bureau policy and enforcement trends; review on next scheduled audit |

**⟁ CLARIFY** — For any finding at Tier 1, ask before finalizing the report:

- "This finding may involve criminal exposure. Has the client considered engaging
  the immunity or leniency program? Do you want me to include an analysis of
  immunity/leniency eligibility and the steps required to obtain a marker?"

---

### Step 7: Leniency and Immunity Analysis (if Tier 1 findings)

Apply this module only where Tier 1 criminal exposure has been identified.

**Immunity Program (only one immunity grant per cartel)**:

- Eligibility: First party to disclose an **unknown** cartel to the Bureau
- Requires: Full factual disclosure; documentary production; recorded witness testimony before
  final immunity is granted
- **Marker**: Obtain immediately to secure position — assembles evidence afterward
- Immunity covers criminal prosecution but **not** civil class actions

**Leniency Program ("Disclosure First" model — in force September 27, 2024)**:

- Eligibility: Parties after immunity has been granted (no limit on number of leniency markers)
- Requires: Full disclosure (documents + recorded testimony) **before** final leniency credit
  is determined (a significant change — previously disclosure could follow the marker)
- **Leniency credit**: Up to 50% reduction from calculated fine; higher credit for early,
  comprehensive disclosure
- Leniency does NOT protect from s. 36 civil damages class actions

**Key steps if Tier 1 exposure identified**:

1. Engage qualified competition counsel with cartel experience immediately
2. Conduct a rapid internal factual investigation under privilege
3. Assess immunity eligibility — is the Bureau already aware of the conduct?
4. If eligible for immunity: contact the Bureau through counsel to request a marker without delay
5. If immunity is not available: assess leniency eligibility and timing
6. Implement a litigation hold for all potentially relevant documents
7. Do not discuss the conduct on any communication channel that is not privilege-protected

---

### Step 8: Generate Remediation Recommendations

For each finding, provide:

**For CRITICAL / Tier 1 findings**:

- Immediate action required: Identify the specific conduct triggering exposure
- Privilege assertion steps: Documents to preserve; communications to route through counsel
- Immunity/leniency program applicability and eligibility assessment
- Employee-facing guidance on right to counsel and privilege

**For NON-COMPLIANT / Tier 2 findings**:

- Specific remediation steps: Amend the agreement or practice; cease the conduct
- Documentation: Written record of business justification for the remediated practice
- Timeline: Recommended remediation deadline
- Voluntary disclosure consideration: Where Bureau engagement is advised

**For PARTIAL / Tier 3 findings**:

- Specific program gaps to fill: Policy update, training module, monitoring mechanism
- Implementation timeline
- Responsible owner for remediation
- Success metrics for verification

**For COMPLIANT / Tier 4 findings**:

- Watchpoints to monitor (regulatory developments, Bureau enforcement actions in the sector)
- Next review trigger (annual audit, specific Bureau announcement, etc.)

---

### Step 9: Quality Verification

Before delivering the assessment, run these quality checks:

1. Run the **5 Citation Quality Gates** (see Quality Assurance Framework below)
2. For every CRITICAL or NON-COMPLIANT finding, run **3-pass Self-Interrogation**
3. Assign a **Confidence Score** to each material finding
4. Verify all [JURISDICTION-SPECIFIC] and [VERIFY] tags are placed correctly
5. Verify no unintended European or US competition law concepts have bled into the analysis
   (e.g., EU TFEU Art. 101/102 analysis does not apply; US Sherman Act s. 1/2 does not apply
   in Canada — use Canadian Act and Canadian Tribunal/court authority only)
6. Generate the **Glass Box Audit Trail** and append to the output

---

### Step 10: Deliver Assessment Output

Produce the output using the **Output Format Template** at the end of this skill.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                              | Fail Action                                         |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **Source**     | Every Competition Act claim cites a specific section of the Act or Bureau guideline                                               | Add citation or mark [UNVERIFIED]                   |
| **Format**     | All citations follow consistent Canadian legal citation format (e.g., "s. 45(1)(a) of the Competition Act, R.S.C. 1985, c. C-34") | Fix format                                          |
| **Currency**   | Every cited provision checked for amendment by Bills C-19, C-56, and C-59                                                         | Flag [CHECK CURRENCY] if amendment status uncertain |
| **Domain**     | Analysis stays within Competition Act scope — no EU/US competition law concepts presented as Canadian law                         | Remove or flag jurisdictional bleed                 |
| **Confidence** | Uncertainty explicitly stated; no uncertain propositions stated as settled law                                                    | Add confidence qualifier                            |

### Self-Interrogation for CRITICAL and NON-COMPLIANT Findings

For any item classified CRITICAL or NON-COMPLIANT, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the finding follow logically from the cited statutory
provision and current Bureau enforcement position? Would the Competition Tribunal or a court
actually reach this conclusion on these facts? Is the per-se nature of any criminal finding
clearly supported — or is there a plausible ancillary restraints or regulated conduct defence?

**Pass 2 — Completeness**: Have all relevant provisions been considered? Are there defences
(Ancillary Restraints Defence, regulated conduct, environmental collaboration exemption, superior
competitive performance) that have not been addressed? Are there Bureau guidelines that qualify
the enforcement position?

**Pass 3 — Challenge**: What is the strongest argument against this classification? Under what
circumstances would a reasonable competition counsel conclude this practice is lawful? Has
market power been properly established for civil offences that require it?

### Confidence Scoring

| Level        | Range     | Meaning                                                                                 | Action                                          |
| ------------ | --------- | --------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law (e.g., per-se criminal s. 45 price-fixing is charged regardless of effects) | State with confidence                           |
| **High**     | 0.80–0.94 | Strong Bureau/Tribunal authority; minor factual questions remain                        | State with brief caveat                         |
| **Probable** | 0.60–0.79 | Good arguments; outcome depends on market definition or factual development             | State with reasoning and contra-indicators      |
| **Possible** | 0.40–0.59 | Genuinely uncertain; reasonable counsel could differ                                    | Flag for qualified legal review with both sides |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                                                                 | Do not assert; flag [UNCERTAIN]                 |

---

## Glass Box Audit Trail Template

```yaml
glass_box:
  skill_name: "legalcode-ca-competition-act-assessment"
  assessment_date: "[date]"
  jurisdiction: "Canada — Federal"
  governing_statute: "Competition Act, R.S.C. 1985, c. C-34 (as amended to Bill C-59, June 2024)"
  modules_assessed:
    - "[List triggered modules: A, B, C, D, E, F, G, H, I, J]"
  organization_type: "[Large corporation / Mid-market / Trade association / PE acquiror / Foreign]"
  industry_sector: "[Sector]"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[/tmp/legalcode-ca-competition-research.md or 'Not created']"
  findings_summary:
    critical: "[n findings]"
    non_compliant: "[n findings]"
    partial: "[n findings]"
    compliant: "[n findings]"
  citations_verified: "[n VERIFIED / n UNVERIFIED — note if legalcode-mcp not connected]"
  amendment_coverage: "Bills C-19 (June 2023), C-56 (December 2023), C-59 (June 2024) incorporated"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "Provincial consumer protection statutes not assessed"
    - "Sector-specific regulatory exemptions require additional research"
    - "Private rights of action exposure for pre-June 2025 conduct may differ"
    - "[Any other scope limitations or assumptions]"
  reviewer: "AI-assisted — requires review by qualified Canadian competition law practitioner"
```

---

## Anti-Patterns

The following are common errors in Competition Act compliance practice. Do not replicate them.

1. **Treating drip pricing as a disclosure issue rather than a prohibition**: After Bill C-59,
   mandatory undisclosed fees are not merely a disclosure gap to cure — they are per-se
   deceptive. The total price, including all mandatory charges, must be displayed at the
   outset of the purchasing funnel.

2. **Assuming the ancillary restraints defence (ARD) covers trade association price discussions**:
   The ARD only applies where the restraint is ancillary to a broader agreement between the
   same parties. It does not provide shelter for horizontal price discussions at association
   events that are not part of any bilateral agreement.

3. **Treating wage-fixing as a civil HR issue**: Since June 23, 2023, wage-fixing between
   competing employers is a **per-se criminal** offence under s. 45(1.1). It is not a civil
   reviewable matter and carries 14-year imprisonment exposure. HR and legal teams must treat
   it with the same urgency as price-fixing.

4. **Relying on the efficiency defence for mergers post-December 2023**: Section 96 was
   repealed by Bill C-56. Economic efficiency arguments are no longer a defence to
   anti-competitive merger findings. Merger analysis must rest on market-effects arguments,
   not efficiency justifications.

5. **Assuming Bureau leniency shields from class action exposure**: Leniency (and even
   full immunity) does not protect from s. 36 civil damages actions or from class actions.
   Leniency recipients frequently face parallel private litigation. Counsel must advise
   clients on both tracks concurrently.

6. **Characterizing no-poach provisions in franchise agreements as unilateral when they
   are functionally mutual**: If a franchise agreement contains a clause prohibiting all
   franchisees from hiring each other's employees, the Bureau may characterize the
   arrangement as a hub-and-spoke conspiracy in which each franchisee has implicitly agreed
   not to hire from other franchisees. Legal advice on whether the ARD applies is essential.

7. **Making environmental claims without pre-publication substantiation**: After Bill C-59,
   the burden of proof for greenwashing is reversed — the company must have adequate and
   proper tests completed **before** publishing the claim. Substantiating claims retroactively
   after a complaint does not cure the violation.

8. **Conflating Competition Act dominance with monopoly**: The abuse of dominance provisions
   (ss. 78–79) require "substantial or complete control" in a market — a lower threshold
   than US monopoly power. Companies with 40–50% market share may face scrutiny even if
   they do not consider themselves dominant.

9. **Underestimating section 90.1 after December 15, 2024**: The extension of s. 90.1 to
   non-competitors is a fundamental change. Distribution agreements, franchise arrangements,
   and licensing deals between parties who are not direct competitors can now be reviewed if
   a "significant purpose" is anti-competitive. Any commercial agreement with territorial,
   customer, or pricing restrictions should be assessed against the new standard.

10. **Failing to update compliance programs for the 2022–2024 amendments**: Many Canadian
    compliance programs were written before the three-round amendment cycle. Programs that
    do not address wage-fixing/no-poach (June 2023), the repealed efficiency defence (December
    2023), the s. 90.1 expansion (December 2024), or the private rights expansion (June 2025)
    are substantively incomplete and will not be treated as credible by the Bureau.

11. **Conflating investment Canada Act "net benefit" with Competition Act merger review**:
    These are two separate, independently administered review regimes. Obtaining approval
    under one does not satisfy the other. Both must be tracked, with potentially different
    timelines and information requirements.

12. **Participating silently in anticompetitive discussions at trade association events**:
    Silent attendance at a competitor discussion about pricing or market allocation may
    constitute tacit participation in a conspiracy. Employees must verbally object, leave
    the meeting, and document the objection in a contemporaneous record.

13. **Treating the post-2024 abuse of dominance test as easier to satisfy than the pre-2024
    test**: The two-part test (Bill C-56) is not a relaxation of the dominance requirement.
    Full remedies (including AMPs) still require proof of all three traditional elements.
    The change primarily enables prohibition-only orders on two elements and removes the
    intent requirement for the effects-based track.

14. **Failing to consider algorithmic pricing coordination**: The Bureau and international
    enforcers are increasingly scrutinizing the use of common third-party pricing algorithms
    by competitors as potential s. 45 violations. If competitors use the same algorithm with
    shared inputs or pricing recommendations, independent legal assessment is required.

15. **Assuming small market share precludes merger notification**:
    The pre-merger notification thresholds are based on the size of the **parties** and the
    **target**, not on competitive effects. Even a merger with no market overlap may be
    notifiable if the parties are large enough to trigger both thresholds.

16. **Treating Competition Bureau consent agreements as final resolution**:
    Consent agreements resolve Bureau civil enforcement proceedings but do not protect
    from: (i) s. 36 civil damages claims by private parties; (ii) potential criminal
    investigation if the facts support a criminal track; or (iii) class action proceedings
    in relation to the same conduct.

---

## Writing Standards

Apply these standards before delivering any output:

- **Quantify exposure**: For every penalty reference, state the applicable maximum (e.g.,
  "imprisonment up to 14 years and/or a fine at the court's discretion") — do not use
  vague terms like "significant penalties."
- **Cite specifically**: Every statutory finding should cite the section number (e.g., "s. 45(1)(a)"
  not just "the cartel provisions").
- **Date all legal changes**: When describing post-amendment law, state when the amendment
  came into force (e.g., "Since June 23, 2023 (Bill C-19)...").
- **Active voice, imperative form**: "Cease the practice" not "the practice should be ceased."
- **Distinguish criminal from civil**: Every finding should clearly identify whether it involves
  criminal exposure (per-se, no effects required, imprisonment available) or civil review
  (effects-based, administrative penalties only).
- **Avoid US and EU analogies as authority**: Competition Act analysis should be grounded
  in Canadian Act provisions, Bureau guidelines, and Tribunal/Federal Court decisions.
  Reference to US or EU law is for context only, not as persuasive authority.
- **Plain language for non-lawyers**: Executive summaries and recommended actions should be
  understandable to general counsel and business executives without competition law backgrounds.
  Reserve technical legal analysis for the detailed findings section.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred)**:

- Search for current text of Competition Act provisions (verify post-2024 amendment status)
- Search for Competition Bureau enforcement guidelines and policy bulletins
- Search for recent Competition Tribunal and Federal Court decisions on abuse of dominance,
  merger review, and cartel offences
- Search for recent consent agreements and AMPs in the assessed industry sector
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp**:

- Mark all statutory section references [VERIFY]
- Mark all penalty amounts and thresholds [VERIFY — subject to annual adjustment]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Focus assessment on structural compliance gaps and workflow guidance rather than
  specific statutory claims requiring current legal authority

---

## Localization Notes

**Federal scope**: This skill covers federal Competition Act only. Several matters require
awareness of provincial overlay:

| Area                                   | Provincial Overlay                                                                                                                                                                                                              |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Consumer protection**                | Ontario CPA, Quebec CPA, Alberta ATA, BC BPCPA run parallel to federal misleading advertising provisions for consumer-facing conduct. Provincial regulators may bring their own proceedings.                                    |
| **Franchise disclosure**               | Ontario Franchise Act, Alberta Franchises Act, BC Franchises Act, Manitoba Franchises Act, New Brunswick Franchises Act, PEI Franchises Act impose disclosure obligations on franchisors independent of Competition Act issues. |
| **Provincial competition authorities** | Quebec Competition Office (Office de la protection du consommateur) and Ontario Ministry of Public and Business Service Delivery have enforcement roles in their respective jurisdictions.                                      |
| **Securities**                         | Competition Act/securities law interface for information barriers and trading by cartel participants should be addressed separately.                                                                                            |

**Language**: All Competition Bureau proceedings and public communications are in English
and French. Regulatory documents, consent agreements, and Tribunal decisions are bilingual.
Legal opinions and compliance materials may be required in French in Quebec.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on:

- Competition Act, R.S.C., 1985, c. C-34 as amended by Bills C-19 (June 2023), C-56
  (December 2023), and C-59 (June 2024)
- Competition Bureau Canada published guidelines: Corporate Compliance Programs, Abuse of
  Dominance Enforcement Guidelines, Enforcement Guidelines on Wage-Fixing and No-Poach
  Agreements, Immunity and Leniency Program documentation
- Competition Bureau 2024–2025 and 2025–2026 Annual Plans
- Leading Canadian competition law commentary: Fasken, McCarthy Tétrault, Osler, Norton
  Rose Fulbright, McMillan, BLG, and Baker McKenzie Canada Insights publications
- Recent enforcement actions: Google online advertising Tribunal application (November 2024),
  SiriusXM drip pricing consent agreement (2024), Broadridge serial acquisition inquiry (2024),
  Sobeys/Loblaw grocery sector investigation (2024)
- ICLG Cartels and Leniency Canada 2024 Report
- Legalcode agent-team research pipeline (structural analysis + prompt engineering analysis
  - deep legal topic research)

---

## Output Format Template

```markdown
# Competition Act Assessment — [Organization / Matter]

**Assessment Date**: [date]
**Prepared Under**: Solicitor-Client Privilege — [if applicable, note engagement context]
**Modules Assessed**: [List modules A–J applied]
**Overall Risk Level**: [CRITICAL / HIGH / MEDIUM / LOW]

---

## Executive Summary

[2–3 paragraph plain-language summary for senior counsel or general counsel. Lead with
the most important findings. State the overall risk level and the basis for it. Identify
the single most important action required.]

---

## Key Findings Summary

| Finding ID | Module | Classification                                   | Provision | Priority   |
| ---------- | ------ | ------------------------------------------------ | --------- | ---------- |
| [F-01]     | [A–J]  | [CRITICAL / NON-COMPLIANT / PARTIAL / COMPLIANT] | [s. XX]   | [Tier 1–4] |
| ...        |        |                                                  |           |            |

---

## Detailed Findings

### Finding F-01: [Short title]

**Classification**: [CRITICAL / NON-COMPLIANT / PARTIAL / COMPLIANT]
**Priority**: [Tier 1–4]
**Statutory basis**: [s. XX of the Competition Act — cite specifically]
**Confidence**: [Definite / High / Probable / Possible / Unlikely — X.XX]

**Finding**:
[Specific description of the conduct, practice, or gap giving rise to the finding]

**Legal basis**:
[Explain why this conduct triggers the provision. Cite relevant statutory text, Bureau
guideline, or Tribunal/court authority. Note whether this is per-se criminal (no effects
required) or requires proof of effects.]

**Exposure**:
[Quantify: criminal penalties (imprisonment term, fine range), civil AMPs (cite maximum),
class action exposure, debarment risk, reputational/regulatory risk.]

**Recommendation**:
[Specific, actionable steps. Use imperative form: "Cease the practice," "Amend the
agreement to remove clause X," "Engage outside competition counsel within 24 hours."]

**Timeline**: [Immediate / 30 days / 90 days / Monitor]

---

[Repeat for each finding]

---

## Compliance Program Gap Summary

[Where Module I was assessed, provide a table of program element scores:]

| Element                          | Score (1–5) | Key Gap           | Recommended Action |
| -------------------------------- | ----------- | ----------------- | ------------------ |
| 1. Senior management commitment  | [1–5]       | [Gap description] | [Action]           |
| 2. Designated compliance officer | [1–5]       |                   |                    |
| 3. Risk assessment               | [1–5]       |                   |                    |
| 4. Written policies              | [1–5]       |                   |                    |
| 5. Training                      | [1–5]       |                   |                    |
| 6. Monitoring and auditing       | [1–5]       |                   |                    |
| 7. Reporting mechanisms          | [1–5]       |                   |                    |
| 8. Enforcement and discipline    | [1–5]       |                   |                    |
| 9. Review and updating           | [1–5]       |                   |                    |
| **Overall**                      | [avg]       |                   |                    |

---

## Remediation Roadmap

| Priority           | Finding | Action       | Owner                      | Deadline           |
| ------------------ | ------- | ------------ | -------------------------- | ------------------ |
| Tier 1 — Immediate | [F-XX]  | [Action]     | [GC / Competition Counsel] | Immediate          |
| Tier 2 — 30 days   | [F-XX]  | [Action]     | [Owner]                    | [date]             |
| Tier 3 — 90 days   | [F-XX]  | [Action]     | [Owner]                    | [date]             |
| Tier 4 — Monitor   | [F-XX]  | [Watchpoint] | [Owner]                    | [Next review date] |

---

## Regulatory Watchpoints

[Identify upcoming regulatory developments that may affect the assessment:]

- **Private rights of action (June 20, 2025)**: Private Tribunal access for ss. 74.1 and
  90.1 now in force — assess exposure to private proceedings
- **Bureau 2025–2026 enforcement priorities**: Grocery sector, housing affordability,
  digital markets, greenwashing, drip pricing
- **[Any pending Bureau market studies or investigations relevant to the sector]**

---

## Glass Box Audit Trail

[Paste completed Glass Box YAML block from Step 9]

---

_This assessment was prepared using the legalcode-ca-competition-act-assessment skill.
It does not constitute legal advice. Review by a qualified Canadian competition law
practitioner is required before any reliance or action._
```
