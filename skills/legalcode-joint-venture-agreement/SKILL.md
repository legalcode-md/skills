---
name: legalcode-joint-venture-agreement
description: Drafts and reviews joint venture agreements covering governance structure, board composition
  and voting thresholds, capital contributions, profit and loss allocation, management rights, deadlock
  resolution mechanisms (Russian roulette, Texas shoot-out, expert determination), non-compete obligations,
  exit strategies (put/call options, ROFO/ROFR, shotgun clauses, tag-along/drag-along), intellectual property
  ownership and licensing (background IP/foreground IP), and dissolution procedures. Use when drafting
  a new JV agreement, reviewing a counterparty's JV draft, structuring a corporate joint venture, evaluating
  deadlock provisions, or assessing exit mechanism enforceability.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Drafts and reviews joint venture agreements covering governance structure, board composition and voting thresholds, capital contributions, profit and loss allocation, management rights, deadlock resolution mechanisms (Russian roulette, Texas shoot-out, expert determination), non-compete obligations, exit strategies (put/call options, ROFO/ROFR, shotgun clauses, tag-along/drag-along), intellectual property ownership and licensing (background IP/foreground IP), and dissolution procedures. Addresses tax structuring implications across entity types. Primary coverage: US (Delaware LLC and C-Corp structures), UK (England and Wales companies/LLPs), EU (cross-border JVs and merger control), and India (Companies Act 2013 / FEMA compliance). Use when drafting a new JV agreement, reviewing a counterparty's JV draft, structuring a corporate joint venture, evaluating deadlock provisions, or assessing exit mechanism enforceability. Also triggers on "shareholder agreement for JV", "joint venture partnership agreement", "50/50 joint venture", "co-venture agreement", "JV governance", "consortium agreement with equity", or any arrangement where two or more parties co-own an entity or project and need governance rules.


# Legalcode Joint Venture Agreement

> **Disclaimer**: This skill provides a framework for AI-assisted joint venture agreement
> drafting and review. It does not constitute legal advice. All outputs should be reviewed
> by a qualified legal professional licensed in the relevant jurisdiction before use.
> Laws change; verify current applicability before relying on any provision described here.
> Statutory and case law references cited from memory carry hallucination risk — verify
> against authoritative sources before relying on them.

## Purpose and Scope

This skill drafts and reviews joint venture agreements for multi-party equity ventures
across the full deal lifecycle — from initial term sheet to execution-ready agreement.

**Covers:**

- Governance architecture (board/committee composition, voting, reserved matters, quorum)
- Capital contributions (initial, additional calls, default consequences, valuation)
- Profit and loss allocation and distribution waterfall
- Management rights and day-to-day operational authority
- Deadlock resolution mechanisms (escalation, Russian roulette, shoot-out, expert determination, winding up)
- Non-compete and non-solicitation obligations during and after the JV term
- Exit strategies (put/call options, ROFO/ROFR, tag-along, drag-along, IPO, shotgun clauses)
- Intellectual property (background IP retention, foreground IP ownership, licensing, reversion on dissolution)
- Dissolution procedures and asset distribution waterfall
- Tax structuring implications by entity type and jurisdiction
- Regulatory/merger control considerations (EU, US HSR, India CCI)
- Jurisdiction-specific mandatory requirements (US/UK/EU/IN)

**Does not:**

- Provide legal advice or replace qualified counsel
- Handle pure contractual joint ventures with no equity component (see legalcode-master-services-agreement)
- Cover publicly listed joint ventures with securities law considerations
- Draft the underlying shareholders agreement where the JV has third-party investors

**Two modes:**

- **Draft mode**: Build a new JV agreement from a term sheet or party instructions
- **Review mode**: Analyze a counterparty's draft, flag deviations, generate redlines

## Jurisdiction and Governing Law

This skill covers four primary JV jurisdictions. Mark jurisdiction-dependent content with
**[JURISDICTION-SPECIFIC]** throughout. Each jurisdiction brings mandatory provisions that
cannot be contracted out.

| Jurisdiction          | Primary Law                                           | Key Mandatory Provisions                                                                                                                                                                             |
| --------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **US (Delaware)**     | Delaware LLC Act (6 Del. C. §§ 18-101 et seq.) / DGCL | Fiduciary duties (waivable in LLC); minority oppression remedies limited; HSR notification thresholds                                                                                                |
| **UK (E&W)**          | Companies Act 2006; IA 1986                           | Unfair prejudice petition (s.994 CA 2006); just and equitable winding up (s.122(1)(g) IA 1986); stamp duty on share transfers; statutory pre-emption rights (s.561 CA 2006, disapplicable)           |
| **EU (cross-border)** | EU Merger Regulation 139/2004; TFEU Art. 101          | Full-function JV notification (EU MR Art. 3(4)); Art. 101 scrutiny for cooperative JVs; potential ancillary restraint clearance                                                                      |
| **India**             | Companies Act 2013; FEMA 1999; Competition Act 2002   | FDI approval/automatic route sector compliance; CCI combination notification (threshold-based); FEMA pricing guidelines (equity allotment at fair market value); transfer pricing (Chapter X IT Act) |

[JURISDICTION-SPECIFIC] For each JV, confirm:

1. Which law governs the JV entity (entity law of the jurisdiction of incorporation)
2. Which law governs the JV agreement (governing law clause)
3. Whether regulatory approval is required before completion (antitrust, sector-specific)
4. Whether the JV constitutes a "full-function joint venture" for merger control purposes

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer changes the direction of the drafting or analysis
- Multiple structuring approaches exist and the parties' preference matters
- Ambiguity in the deal terms creates a fork only the user can resolve
- Jurisdiction-specific mandatory provisions require local adaptation

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

- **Term sheet or heads of terms**: PDF, DOCX, or text summary of agreed deal points
- **Draft JV agreement**: Counterparty's draft for review and redline
- **Party instructions**: Free-text description of the JV structure, parties, and objectives
- **Existing agreement**: Prior JV agreement for renewal, amendment, or dispute analysis

If insufficient information is provided to determine the skill's mode, prompt the user
to supply the input.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user:

1. **Mode**: What is the primary task?
   - Options: **Draft new JV agreement** (Mode A), **Review counterparty's draft and generate redlines** (Mode B), **Analyze specific provisions** (Mode C — governance, exit mechanisms, IP, tax, etc.), Other
   - _Why this matters_: Draft mode requires gathering all deal parameters; review mode requires understanding which party the user represents.

2. **Which party are you representing?**
   - Options: Party A (specify name/role), Party B (specify name/role), Neutral drafter, Other
   - _Why this matters_: The entire analysis and drafting tilts based on which party's interests to protect.

3. **JV structure**: What is the intended legal vehicle?
   - Options: Delaware LLC (US), C-Corporation (US), English limited company (UK), LLP (UK/India), Indian private limited company, EU cross-border structure (specify), Other
   - _Why this matters_: Fiduciary duties, exit mechanics, and tax treatment vary fundamentally by entity type.

4. **Ownership split**: What is the equity ownership percentage between the parties?
   - Free text: e.g., 50/50, 60/40, 70/30, multiple parties
   - _Why this matters_: 50/50 JVs require more robust deadlock resolution; minority protection rights are more critical in unequal splits.

5. **Key issues / focus areas**: Any specific concerns?
   - Options: Deadlock resolution, Exit mechanisms, IP ownership, Non-compete enforceability, Tax structuring, Governance and control, No specific focus — full review/draft
   - Allow multiple selections.
   - _Why this matters_: Lets the analysis lead with what the user cares about most.

6. **Governing law and jurisdiction**:
   - Options: US (Delaware preferred), UK (England and Wales), India, EU cross-border, Other
   - _Why this matters_: Determines mandatory provisions, enforceability of mechanisms, and regulatory requirements.

If the user provides partial context, proceed with reasonable assumptions stated
explicitly. Do not silently assume.

### Step 3: Gather Jurisdiction-Relevant Legal Authority

Identify the governing law from the JV agreement or user's instructions. Then use
**legalcode-mcp** to gather jurisdiction-specific legal authority.

**Research process:**

1. **Identify the governing law** from the JV agreement or user instructions.

   **⟁ CLARIFY** — If any of the following apply, ask before proceeding:
   - No governing law clause identified: Ask which jurisdiction governs the JV entity and the JV agreement separately.
   - Cross-border JV where entity law differs from JV agreement governing law (common): Confirm the user is aware and explain the implications.
   - India JV involving foreign party: Confirm FEMA compliance approach and FDI route (automatic vs. approval).

2. **Search legalcode-mcp** for jurisdiction-relevant authority covering:
   - Fiduciary duty rules for the entity type (waivability in Delaware LLCs; directors' duties under CA 2006)
   - Minority shareholder/member protection remedies
   - Deadlock resolution mechanism enforceability
   - Non-compete enforceability by jurisdiction
   - Exit mechanism (put/call, shotgun) enforceability and valuation disputes
   - IP ownership rules for jointly developed works
   - Merger control notification thresholds
   - Tax treatment of the JV structure

3. **Save the most relevant results** to `/tmp/legalcode-jva-authority.md`.

**If legalcode-mcp is not connected:**

- Mark every statutory and case law reference with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed using general legal knowledge for the relevant jurisdiction

### Step 4: Regulatory Pre-Screen

Before clause-by-clause analysis or drafting, run a regulatory pre-screen. This is
mandatory — merger control and sectoral approvals are conditions precedent for many JVs.

**⟁ CLARIFY** — Ask the user to confirm the parties' revenues/turnover and the nature
of the JV business if not already provided. This determines merger control notification
requirements.

**Full-Function JV Test (EU Merger Regulation 139/2004, Art. 3(4))**:

- Performs, on a lasting basis, all the functions of an autonomous economic entity
- Has management dedicated to day-to-day operations
- Access to resources needed to operate independently
- _If full-function_: EU MR thresholds apply → potential ECON notification requirement [VERIFY current thresholds]

**US HSR Act (15 U.S.C. § 18a)**:

- Transaction value test: check current HSR thresholds [VERIFY — adjusted annually]
- Size-of-person test: apply to both parties
- Waiting period: 30 days (15 for cash-only transactions) [VERIFY]

**India Competition Act 2002**:

- Combination thresholds: check current CCI thresholds (Schedule I de minimis exemptions) [VERIFY]
- Target exemption: "small target" exemption if target's value below threshold [VERIFY]

**Sector-specific approvals**: Flag if the JV operates in a regulated sector (financial services, telecoms, media, defence, infrastructure, healthcare) as additional approvals may be needed.

| Pre-Screen Item                 | Outcome                           | Action                                    |
| ------------------------------- | --------------------------------- | ----------------------------------------- |
| EU full-function JV test        | Full-function / Cooperative       | Notification required / Art. 101 analysis |
| US HSR notification             | Above threshold / Below threshold | File / Proceed                            |
| India CCI combination           | Above threshold / Below threshold | File / Proceed                            |
| Sector regulatory approval      | Required / Not required           | Engage regulator / Proceed                |
| FEMA compliance (India inbound) | FDI route confirmed               | Automatic / Approval route                |

### Step 5: Clause-by-Clause Analysis (Review Mode) or Drafting Framework (Draft Mode)

**⟁ CLARIFY** — For complex JV agreements (50+ pages, multiple annexes, existing commercial relationship):

- Ask whether to perform a **full review** of all 18 clause categories, or a **priority review** focused on the user's stated concerns from Step 2.
- If the JV agreement incorporates external documents by reference (shareholders register, business plan, IP licence), ask whether those incorporated documents should be reviewed.

Cover all 18 clause categories below. For each, assess against the parties' agreed term
sheet (or general market standards) and classify each provision's status.

| #   | Clause Category                            | Depth    | Key Drafting / Review Points                                                                                 |
| --- | ------------------------------------------ | -------- | ------------------------------------------------------------------------------------------------------------ |
| 1   | Purpose and Term                           | Deep     | JV scope, exclusivity, fixed vs. perpetual term, extension                                                   |
| 2   | Entity Structure and Capitalization        | Deep     | Entity type, registered capital, shareholding/membership interests, issue price, classes of equity           |
| 3   | Governance: Board and Management Committee | Deep     | Board size, appointment/removal rights, quorum, voting thresholds, reserved matters                          |
| 4   | Deadlock Resolution                        | Deep     | Escalation, mediation, expert determination, Russian roulette/shotgun, Texas shoot-out, winding up           |
| 5   | Capital Contributions                      | Deep     | Initial contributions (cash, IP, assets), valuation methodology, contribution schedule, default consequences |
| 6   | Additional Funding / Capital Calls         | Deep     | Call mechanism, funding obligation, dilution on non-funding, drag-along for capital calls                    |
| 7   | Profit and Loss Allocation                 | Deep     | Allocation formula, preferred returns, waterfall, retained earnings policy                                   |
| 8   | Distribution Policy                        | Deep     | Timing, frequency, minimum distribution, restrictions on distressed JVs, tax withholding on distributions    |
| 9   | Exit Mechanisms                            | Deep     | Put/call options, ROFO/ROFR, tag-along/drag-along, shotgun clause, IPO right, forced sale                    |
| 10  | Non-Compete and Non-Solicitation           | Deep     | Duration, geographic scope, exceptions for retained businesses, enforceability by jurisdiction               |
| 11  | Intellectual Property                      | Deep     | Background IP ownership/licensing, foreground IP ownership, improvements, reversion on dissolution           |
| 12  | Confidentiality                            | Standard | Scope, permitted disclosures to lenders/advisors, duration, return/destruction obligations                   |
| 13  | Representations and Warranties             | Standard | Authority, ownership, no conflict, financial condition, regulatory compliance                                |
| 14  | Termination and Dissolution                | Standard | Trigger events, dissolution procedure, asset distribution waterfall, IP reversion                            |
| 15  | Tax and Structuring                        | Standard | Entity-level tax, withholding tax on distributions, transfer pricing, exit tax                               |
| 16  | Regulatory Compliance                      | Standard | Merger control, sector approvals, anti-bribery (FCPA/UK Bribery Act/PMLA), sanctions                         |
| 17  | Governing Law and Dispute Resolution       | Standard | Choice of law, arbitration vs. litigation, seat and institution, multi-tier escalation                       |
| 18  | Boilerplate                                | Standard | Entire agreement, amendment, assignment/change of control, notices, force majeure, third-party rights        |

---

## Clause Analysis Reference

### 1. Purpose and Term

**Key drafting and review points:**

- Define the JV's business purpose with precision — ambiguity creates disputes over whether a new activity falls within the JV scope
- Exclusivity clause: does each party agree not to pursue competing opportunities outside the JV? For how long and in what geography?
- Fixed term vs. perpetual term: fixed terms with agreed renewal or extension provisions are generally cleaner; perpetual JVs create valuation and dissolution complications
- Early termination triggers: regulatory non-approval, material breach, insolvency

**Classification triggers:**

- **RED**: JV purpose undefined or excessively broad (creates scope disputes); no termination event for regulatory non-approval
- **YELLOW**: Exclusivity obligations broader than the JV's actual business scope
- **GREEN**: Well-defined purpose with clear exclusivity carve-outs for each party's retained business

[JURISDICTION-SPECIFIC]

- **India**: Objects clause in the Memorandum of Association must align with the JV's business purpose; ultra vires doctrine applies despite Companies Act 2013 reforms [VERIFY]
- **UK**: No ultra vires issue for English companies (CA 2006 s.39), but articles of association must be consistent with JV agreement
- **EU**: Cross-border JVs should specify which national law governs the entity in addition to the JV agreement governing law

### 2. Entity Structure and Capitalization

**Key drafting and review points:**

- Choice of entity profoundly affects governance flexibility, fiduciary duties, tax treatment, and exit mechanics
- Delaware LLC: maximum flexibility; fiduciary duties freely waivable (6 Del. C. § 18-1101(c)) [VERIFY]; operating agreement is the primary governance document; single-member LLC disregarded for US tax; multi-member LLC treated as partnership by default
- Delaware C-Corp: no duty waiver; less flexible but preferred for IPO exit; double taxation (corporate + dividend) unless S-Corp elected (not available if foreign shareholders)
- English limited company: directors' duties under CA 2006 ss.171-177 cannot be contracted out; statutory pre-emption rights on new share issuance apply unless disapplied by shareholders' resolution
- Indian private limited company: Share transfer restrictions (Companies Act 2013 s.2(68)); FDI pricing guidelines (shares must be allotted/transferred at FEMA-prescribed fair market value) [VERIFY]; maximum 200 members
- Authorized vs. issued capital: ensure authorized capital is sufficient for all anticipated additional issuances

**Classification triggers:**

- **RED**: Entity type chosen is tax-inefficient or unsuitable for exit strategy (e.g., C-Corp when exit is revenue-share buyout, not IPO); no issued capital tracking mechanism
- **YELLOW**: Authorized capital insufficient for anticipated capital calls
- **GREEN**: Entity type matches the JV's purpose, tax profile, and exit strategy

[JURISDICTION-SPECIFIC]

- **India**: Authorized capital is subject to Registrar of Companies fees; amending it requires board and shareholder resolution, and ROC filing [VERIFY]
- **UK**: No par value shares abolished; statement of capital and initial shareholdings required on incorporation (CA 2006 s.10)

### 3. Governance: Board and Management Committee

**Key drafting and review points:**

- **Board composition**: Each party's appointment rights should be proportional to (or at least aligned with) their equity stake; typical structures: 3-member (1+1+1 with independent), 4-member (2+2), 2-member (1+1 with CEO casting vote)
- **Quorum**: Specify minimum attendance for valid meetings; ensure quorum requires representation of both parties to prevent one party railroading decisions
- **Simple majority matters**: Day-to-day operational decisions below a financial threshold; hiring below C-suite level; routine contracts below a value threshold
- **Reserved matters / supermajority**: Require unanimous or supermajority approval; the reserved matters list is often the most heavily negotiated part of a JV agreement

**Reserved Matters Checklist (adapt thresholds to deal size):**

| Reserved Matter                                    | Threshold               | Typical Vote Required                           |
| -------------------------------------------------- | ----------------------- | ----------------------------------------------- |
| Amendment to JV agreement or articles              | Any amount              | Unanimous                                       |
| New issuance of equity / dilution                  | Any amount              | Unanimous                                       |
| Incurrence of debt above [threshold]               | e.g., $[X]              | Supermajority (75%+)                            |
| Capital expenditure above [threshold]              | e.g., $[X] per annum    | Supermajority                                   |
| Acquisition or disposal of material assets         | e.g., >5% of net assets | Supermajority                                   |
| Entry into related party transactions              | Any amount              | Unanimous                                       |
| Change in nature of JV business                    | Any                     | Unanimous                                       |
| Appointment/removal of CEO and senior management   | —                       | Board appointment right of majority / unanimous |
| Approval of annual budget and business plan        | —                       | Supermajority                                   |
| Initiation of litigation above [threshold]         | —                       | Supermajority                                   |
| Distribution of profits / declaration of dividends | —                       | Supermajority                                   |
| Winding up / dissolution of JV                     | —                       | Unanimous                                       |
| IPO or other liquidity event                       | —                       | Unanimous                                       |
| Merger, amalgamation, demerger                     | —                       | Unanimous                                       |

**Classification triggers:**

- **RED**: No reserved matters clause; one party can unilaterally approve material business changes, new equity issuances, or debt; quorum does not require both parties' attendance
- **YELLOW**: Reserved matters list too narrow (omits key decisions); supermajority threshold too low (allows majority partner to steamroll); no deadlock backstop for reserved matter disagreements
- **GREEN**: Balanced board composition; reserved matters calibrated to deal size; quorum requires both parties' representation

[JURISDICTION-SPECIFIC]

- **UK**: CA 2006 s.168 allows shareholders to remove directors by ordinary resolution notwithstanding anything in the articles — JV agreement should address this risk
- **India**: Board meetings require minimum notice (CA 2013 s.173); video conferencing for board meetings permitted; company secretary requirement for public companies [VERIFY]
- **US (Delaware LLC)**: LLC agreement can vest governance in non-members (managers) — distinguish member-managed vs. manager-managed LLCs
- **EU**: Some EU member states require minimum number of board members for public companies; cross-border JVs may need supervisory board (Germany GmbH with >500 employees: co-determination rights) [VERIFY]

### 4. Deadlock Resolution

**This is the most critical — and most frequently litigated — provision in 50/50 JVs.**

**Multi-tier escalation framework (market standard):**

**Tier 1 — Senior Management Escalation (Days 1-30)**:
Upon deadlock on a board matter, refer the matter to designated senior executives of
each party (typically CEO or CFO level). Give them [30] days to resolve.

**Tier 2 — Mediation (Days 31-60)**:
If senior management cannot resolve, submit to non-binding mediation before a mutually
agreed mediator or institutional mediation service (CEDR, AAA, SIAC mediation rules).
Duration: [30] days or as agreed.

**Tier 3 — Expert Determination (for specific technical/financial matters)**:
For valuation disputes or technical deadlocks (e.g., whether a business plan is
commercially reasonable), appointment of an independent expert whose determination is
binding. Used as an alternative to — not a precursor to — Tier 4 mechanisms for
certain defined matter types.

**Tier 4 — Mandatory Offer Mechanisms (Last Resort)**:

**Option A — Russian Roulette / Shotgun Clause**:

- Party A offers to buy Party B's interest at a stated price per share
- Party B must elect within [30] days: (i) accept the offer and sell to Party A, or (ii) reverse the offer and buy Party A's interest at the same price per share
- Effect: creates incentive to set a fair price — the initiating party doesn't know which role it will play
- _Enforceability_: Generally enforceable in US (Delaware) [VERIFY], England and Wales [VERIFY], and most common law jurisdictions; Indian enforceability under SEBI/Companies Act in listed/unlisted contexts is less settled — obtain local counsel opinion

**Option B — Texas Shoot-Out / Sealed Bid**:

- Both parties simultaneously submit sealed bids for the other's interest
- Highest bidder acquires the other's interest at its stated bid price
- _Advantage over Russian roulette_: Eliminates first-mover disadvantage when parties have asymmetric financing ability
- _Disadvantage_: Value is the highest bid price, which may be above fair value

**Option C — Put/Call Option Trigger on Deadlock**:

- Upon deadlock and expiry of cooling-off period, either party may exercise a put (sell own shares to other party) or call (buy other party's shares)
- Valuation: Fair market value determined by agreed formula (EBITDA multiple) or independent expert (two valuers, average, or baseball arbitration)
- _Advantage_: Valuation is market-based rather than strategically set
- _Disadvantage_: Valuation disputes are common; expert appointment can itself deadlock

**Option D — Winding Up as Default Backstop**:

- If all Tier 4 mechanisms fail or neither party exercises within the exercise period, the JV is wound up
- Asset distribution: apply dissolution waterfall (see Clause 14)

**⟁ CLARIFY** — Deadlock mechanism selection:

- If the parties have very different financial resources, Russian roulette may systematically favour the better-capitalized party. Consider the Texas shoot-out or expert valuation instead.
- If the JV involves highly illiquid assets (real estate, infrastructure), a forced sale timeline may be commercially unworkable. Extend cooling-off periods and consider expert determination as the default.

**Classification triggers:**

- **RED**: No deadlock mechanism in a 50/50 JV or a JV with unanimity requirement on key matters; no senior management escalation before formal mechanisms; winding up not addressed as backstop
- **YELLOW**: Deadlock mechanism present but valuation methodology vague (e.g., "fair market value" without specifying who determines it); no time limits on each tier
- **GREEN**: Multi-tier escalation with clear timescales; Tier 4 mechanism appropriate to the parties' relative resources; expert determination with ICEDR or similar rules for valuation

[JURISDICTION-SPECIFIC]

- **India**: Shot-gun and Russian roulette clauses in Indian private limited company JVs should be reviewed for compliance with FEMA pricing guidelines — the acquirer cannot pay more than fair market value for shares from a foreign seller without RBI approval in certain circumstances [VERIFY]
- **UK**: Just and equitable winding up (IA 1986 s.122(1)(g)) and unfair prejudice petition (CA 2006 s.994) are powerful statutory remedies available to any member if the JV relationship breaks down — the JV agreement should not try to exclude these (they are not excludable) but should address the procedure
- **Delaware LLC**: Judicial dissolution on "deadlock or are so divided" (6 Del. C. § 18-802) is available but courts are reluctant to grant it — private contractual mechanisms are strongly preferred and enforced [VERIFY]

### 5. Capital Contributions

**Key drafting and review points:**

- **Initial contributions**: specify cash amount, IP to be licensed or assigned, assets to be contributed, services to be provided, and the agreed valuation for non-cash contributions
- **Contribution schedule**: milestone-based vs. upfront; consequences if milestones are not met (cure period, dilution, termination right)
- **Valuation methodology for non-cash contributions**: independent valuation, agreed formula, or GAAP book value — must be specific
- **Contribution default**: if a party fails to contribute, options include: (i) cure period + right to contribute for the other party; (ii) automatic dilution (non-contributing party's stake reduces proportionally); (iii) interest on unfunded amounts; (iv) deemed deadlock/trigger for exit mechanisms
- **In-kind contributions**: IP licences contributed "in lieu" of cash — distinguish a licence from an assignment; confirm whether the licence is perpetual or co-terminous with the JV

**Classification triggers:**

- **RED**: No valuation methodology for non-cash contributions; no consequences for contribution default; contribution obligation is "best efforts" rather than specific and binding
- **YELLOW**: Cure period for default too long (>30 days for cash contributions); dilution mechanism present but dilution formula not specified
- **GREEN**: Specific contribution schedule; independent valuation for non-cash; graduated default consequences (notice, cure, dilution, exit trigger)

[JURISDICTION-SPECIFIC]

- **India**: Cash contributions by foreign parties must comply with FEMA pricing guidelines; contribution in kind (IP, assets) may require separate RBI approval and FEMA valuation [VERIFY]
- **UK**: Non-cash consideration for shares in English companies requires independent valuation (CA 2006 ss.593-597) for public companies; private companies have more flexibility [VERIFY]
- **US (Delaware LLC)**: The operating agreement can freely set contribution terms; no independent valuation requirement under Delaware law; but consider tax implications (§ 704(c) built-in gain)

### 6. Additional Funding and Capital Calls

**Key drafting and review points:**

- **Capital call mechanism**: board or majority resolution required to call additional capital; notice period to contributing parties (typically 10-30 business days)
- **Pro-rata obligation**: each party contributes pro-rata to its current ownership interest (or agreed call ratio)
- **Consequences of non-funding**: graduated approach:
  1. **Grace period**: [10] business days with interest at agreed rate
  2. **Dilution**: non-funding party's interest is reduced (anti-dilution formula — typically "funded / (funded + unfunded) × pre-call interest")
  3. **Right of other party to fund shortfall**: contributing party may elect to fund the shortfall and further dilute the non-contributor
  4. **Exit trigger**: material non-funding may trigger a put/call or deemed deadlock
- **Maximum capital obligation**: consider a cap on total additional capital obligation per party and per year
- **Third-party financing**: can the JV take on external debt? What approval is required? Who provides guarantees?

**Classification triggers:**

- **RED**: Unlimited capital call obligation with no cap and no exit if unable to fund; dilution formula not specified; no limit on frequency of capital calls
- **YELLOW**: Capital call mechanism present but board approval threshold too low (e.g., majority = one party can unilaterally call capital); no grace period for non-funding
- **GREEN**: Capital call subject to reserved matters approval; clear dilution formula; cap on annual capital obligation; graceful exit from JV if genuinely unable to fund

### 7. Profit and Loss Allocation

**Key drafting and review points:**

- **Allocation formula**: pro-rata to ownership interest is simplest; parties may negotiate preferred returns for the larger contributor
- **Preferred returns**: investor/financial party may negotiate a preferred return (e.g., 8% per annum on outstanding contributed capital) before pro-rata allocation
- **Tax allocations vs. economic allocations (US LLC)**:

  [JURISDICTION-SPECIFIC — US only]:
  Under IRC § 704(b), allocations of profit and loss must have "substantial economic effect" to be respected for federal income tax purposes. The three-part test (economic effect, substantiality) is complex. Key requirements: capital account maintenance, liquidating distributions must follow positive capital accounts (deficit restoration obligation or qualified income offset). Failure to comply results in allocations being recast to ownership percentages. [VERIFY with US tax counsel]

- **Loss carryforward**: can losses be carried forward and offset against future profits before distributions? Specify carryforward periods.
- **Retained earnings reserve**: minimum amount of profit to be retained in the JV before distribution

**Classification triggers:**

- **RED**: No allocation formula specified; US LLC allocation does not satisfy IRC § 704(b) requirements (risk of IRS recast)
- **YELLOW**: Preferred return structure present but not modelled for downside scenarios; loss allocation creates unintended dilution
- **GREEN**: Clear allocation formula; US LLC complies with § 704(b); preferred return mechanism is fair and modelled

[JURISDICTION-SPECIFIC]

- **India**: Profit allocation for Indian company JV is straightforward (proportional to shareholding); dividend is subject to TDS at applicable rate for foreign shareholders (typically 10-20% depending on DTAA) [VERIFY]
- **UK**: Company law distributable profit rules apply (CA 2006 s.829); distributions out of capital are a reduction of capital requiring court approval or solvency statement procedure

### 8. Distribution Policy

**Key drafting and review points:**

- **Timing**: quarterly, semi-annual, or annual distributions; specify trigger (e.g., board approval post-audit or post-management accounts)
- **Minimum distribution**: some JVs specify a minimum distribution percentage of net profit (e.g., 60% of distributable profit) to prevent one party artificially accumulating cash
- **Restrictions on distribution**: no distribution if JV is in financial difficulty, has unpaid capital calls, or is in breach of debt covenants
- **Currency and withholding tax**: identify the distribution currency; address withholding tax obligations (JV entity must withhold tax at source for some jurisdictions)
- **In-kind distributions**: permitted or prohibited? If permitted, how are assets valued for distribution purposes?

**Classification triggers:**

- **RED**: No distribution policy; one party can unilaterally block distributions indefinitely; no mechanism to force distribution if JV has surplus cash
- **YELLOW**: Distribution policy present but no minimum distribution; no protection against distribution blocking by majority party
- **GREEN**: Clear distribution policy with timing, minimum percentage, and conditions; withholding tax addressed; forced distribution mechanism (e.g., minority right to demand distribution above retained earnings reserve)

### 9. Exit Mechanisms

**This section is the most financially significant. Get it right.**

**Exit trigger events**: specify circumstances that activate exit rights (deadlock, change of control, insolvency, material breach, regulatory trigger, expiry of term, voluntary exit).

**Exit mechanism menu:**

**Put Option** (seller's right to compel purchase):

- Who holds it: typically each party on certain trigger events; minority may hold a put against majority on oppression events
- Price: agreed formula (EBITDA × multiple), fair market value (independent valuer), or floor (invested capital + preferred return)
- Exercise period: [30-90] days after trigger event
- Completion timeline: [30-60] days after exercise notice
- _Drafting trap_: Ensure the put can be financed — a put at a potentially high valuation may be unexercisable in practice

**Call Option** (buyer's right to compel sale):

- Who holds it: typically each party symmetrically, or majority party on certain trigger events
- Price: same formula as put (must be symmetric) or different (e.g., lower price for cause-based call)
- _Drafting trap_: A call at a low price for subjectively defined "cause" can be weaponized — define "cause" precisely

**Right of First Offer (ROFO)**:

- Selling party must offer to sell to the other party first, at a price it names
- Other party has [30-45] days to accept or decline
- If declined, selling party may sell to a third party at no less than the ROFO price
- _Advantage over ROFR_: Selling party sets the price — less disruption to third-party negotiations
- _Disadvantage_: Buyer gets second look at third-party terms — potential chilling effect

**Right of First Refusal (ROFR)**:

- Selling party must first offer to sell to the other party on the same terms as a bona fide third-party offer
- Other party has [30-45] days to match or waive
- _Advantage over ROFO_: Buyer knows they can match the best market price
- _Disadvantage_: Chills third-party bids (bidders know they may be used as price-discovery tool only)

**Tag-Along Right**:

- Minority party's right to participate in any sale of the majority's interest on the same terms
- Purpose: protects the minority from being "left behind" in a change of control
- _Drafting detail_: Specify pro-rata tag percentage; whether tag-along applies to partial sales; whether the third-party buyer must agree to acquire all tagged shares

**Drag-Along Right**:

- Majority party's right to compel the minority to sell its interest alongside a majority sale
- Purpose: enables majority to deliver 100% of the JV to a buyer
- _Drafting detail_: Price and terms must be the same as those offered to the majority; include protections for the minority (minimum price floor, cash-only drag, indemnity protection)

**IPO Right**:

- Either party may initiate an IPO process after a specified lock-up period
- Other party may not unreasonably withhold consent
- Lockup post-IPO: specify how long each party's shares are locked up post-listing
- Underwriter discretion: underwriter may require modification to governance on IPO

**Forced Sale / Auction**:

- If no exit mechanism resolves within a specified long-stop date, the JV is sold by auction to a third party
- Independent investment bank appointed to run the process
- Proceeds distributed according to the dissolution waterfall

**Exit Valuation — Methodology Comparison**:

| Method                                 | Pros                                     | Cons                                                                   | Best for                     |
| -------------------------------------- | ---------------------------------------- | ---------------------------------------------------------------------- | ---------------------------- |
| EBITDA multiple (fixed)                | Certainty; fast                          | Can be very wrong if business has changed                              | JVs in stable industries     |
| Fair market value (independent valuer) | Market-reflective                        | Time-consuming; valuation disputes                                     | General use                  |
| Baseball arbitration                   | Resolves valuer disagreement efficiently | Each party submits, judge picks closest — incentivizes reasonable bids | Valuation disputes           |
| Book value                             | Simple; no dispute                       | May significantly undervalue or overvalue                              | Asset-heavy JVs              |
| NAV (for funds/real estate)            | Standard in sector                       | Requires reliable mark-to-market                                       | Real estate / investment JVs |

**⟁ CLARIFY** — Valuation methodology:

- If the JV is a technology company with no profits, an EBITDA multiple is meaningless. Consider revenue multiples, DCF, or comparable transaction analysis instead.
- If the JV is in a regulated sector (banking, insurance), ask the user whether regulatory capital adequacy affects the fair market value calculation.

**Classification triggers:**

- **RED**: No exit mechanism; put/call price is uncapped or subject to litigation (not a formula or expert); drag-along has no minimum price protection; ROFR with no time limit (transaction never closes)
- **YELLOW**: Exit mechanism present but valuation methodology vague; no completion timeline after exercise; no deadlock tie-breaker on valuation (two valuers but no baseball provision)
- **GREEN**: Full menu of exit rights with trigger events; symmetric pricing for put and call; clear valuation methodology with baseball provision if valuers disagree; drag-along with minimum price floor and cash requirement

[JURISDICTION-SPECIFIC]

- **India**: Put/call options in Indian private limited companies involving foreign parties must comply with FEMA pricing guidelines — the price of the put/call cannot contractually exceed fair market value (for seller to foreign party) or fall below fair market value (for buyer from foreign party) [VERIFY with FEMA counsel]. Options with a guaranteed price floor (which is common commercially) may not be permitted without RBI approval.
- **UK**: UK Stamp Duty applies to share transfers — 0.5% of consideration; SDRT applies to paperless transfers; consider duty in valuation and mechanics
- **US (Delaware)**: Put/call options in Delaware LLCs are freely enforceable via contract; no SEC registration required for transfers among existing members (subject to securities law analysis for resale) [VERIFY]
- **EU**: VBER and national competition law may restrict exit restrictions that amount to market-partitioning arrangements

### 10. Non-Compete and Non-Solicitation

**Key drafting and review points:**

- **Scope**: during the JV term, each party agrees not to compete with the JV's business; after termination, an agreed post-term restriction period
- **Geographic scope**: must match the JV's actual operational territory — broader restrictions are less likely to be enforced
- **Activity scope**: define the competitive activities precisely; overly broad definitions will be blue-pencilled or voided
- **Duration**:
  - During-term restriction: no duration limit; coterminous with the JV
  - Post-term restriction: typically 1-2 years; longer periods are at heightened enforceability risk
- **Carve-outs** (critical to negotiate): existing businesses of each party, passive investments below [5%], employment of group companies
- **Non-solicitation**: separate from non-compete; typically applies to JV employees, customers, and suppliers; usually 12-18 months post-termination

**Enforceability by jurisdiction:**

| Jurisdiction          | Non-Compete Enforceability                                                                                                                                                                                                                 | Post-Term Restriction                                       | Key Authority                                                         |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- | --------------------------------------------------------------------- |
| **US — Delaware, NY** | Enforceable if reasonable in scope, geography, duration; blue-pencilling available                                                                                                                                                         | Typically 1-2 years max                                     | Confidentiality Agreement Enforceability — state case law [VERIFY]    |
| **US — California**   | Non-competes void for employees; **may** be enforceable as between business sellers/owners (Cal. Bus. & Prof. Code §16601-16602.5); JV exit context is closer to §16601 than employment [VERIFY]                                           | Very limited                                                | Cal. Bus. & Prof. Code §16600                                         |
| **UK (E&W)**          | Reasonable restrictions enforceable under restraint of trade doctrine; post-Cavendish Square [2015] UKSC 67, the penalty doctrine does not govern forfeiture clauses                                                                       | 12-18 months generally reasonable for corporate JV contexts | Cavendish Square Holding BV v. Makdessi [2015] UKSC 67 [VERIFY]       |
| **EU**                | Ancillary to concentrations: non-competes up to 3 years (if knowhow + goodwill transferred), 2 years otherwise, permitted as ancillary restraints under EU MR; stand-alone non-competes scrutinized under Art. 101 TFEU                    | As above                                                    | EU Commission Notice on Ancillary Restraints 2005/C 56/03 [VERIFY]    |
| **India**             | Section 27 Indian Contract Act 1872 renders agreements in restraint of trade void subject to limited exceptions (sale of goodwill); JV non-competes are difficult to enforce post-exit; focus on confidentiality and IP protection instead | Very limited enforceability post-term                       | Niranjan Shankar Golikari v. Century Spinning [1967] SCR 361 [VERIFY] |

**⟁ CLARIFY** — Non-compete scope:

- If Party A's retained business overlaps significantly with the JV's business, a blanket non-compete would require Party A to fundamentally restructure. Carve-outs for existing business lines are essential and must be specifically defined.

**Classification triggers:**

- **RED**: Non-compete with no carve-outs for existing businesses of either party; post-term restriction exceeding 2 years (unenforceable risk); California non-compete for California-based operations without § 16601 analysis
- **YELLOW**: Post-term restriction present but geographic scope broader than JV operations; no blue-pencil provision; non-solicitation does not cover JV customers
- **GREEN**: Tailored non-compete with specific carve-outs; post-term restriction proportionate (1-2 years); enforceability provisos for California and India; arbitration as enforcement mechanism

### 11. Intellectual Property

**Key drafting and review points:**

**Background IP (Pre-Existing IP):**

- Each party retains ownership of its pre-existing IP
- License to the JV: what scope is granted? (field of use, territory, sublicensing rights)
- Is the license exclusive or non-exclusive within the JV's business scope?
- What happens to the license on JV termination? — **The reversion mechanism is critical**
- License fee or royalty: some JVs have party A license IP free of charge; others charge a commercial royalty; royalty terms must be at arm's length if the JV is subject to transfer pricing rules

**Foreground IP (IP Developed During the JV):**

- Jointly developed IP: most frequently litigated IP issue in JV disputes
- Options for ownership:
  1. **JV entity owns all foreground IP**: cleanest structure; issue is what happens on dissolution
  2. **Joint ownership by both parties**: creates joint ownership complications (in US: each co-owner can license independently without consent; in UK: each joint owner must obtain consent of the other to licence — very different outcomes [VERIFY])
  3. **Ownership follows contribution**: IP attributable to one party's contribution is owned by that party; jointly developed IP jointly owned
- **Cross-licenses on exit**: each party should receive a licence to foreground IP on exit from the JV (or on dissolution)
- **Employee inventions**: ensure JV employees' invention assignment agreements are in place; align with applicable national law (US: 35 U.S.C. § 116 [VERIFY]; UK: Patents Act 1977 ss.39-42; India: Patents Act 1970 s.6)
- **IP upon dissolution**: reversion of background IP licences; assignment or licence of foreground IP to each party; IP escrow for software

**Key jurisdictional IP traps:**

| Jurisdiction                     | Key IP Trap                                                                                                                                                                                          | Authority                       |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **US**                           | Joint ownership of patents allows each co-owner to license independently without other's consent — "joint ownership is usually a bad idea"                                                           | 35 U.S.C. § 262 [VERIFY]        |
| **UK/EU**                        | Joint ownership of patents requires consent of all co-owners to grant licences (Patents Act 1977 s.36; German Patentgesetz s.741 BGB analogy); more restrictive than US [VERIFY]                     | PA 1977 s.36 [VERIFY]           |
| **India**                        | Indian Patents Act 1970 s.50: each co-owner of a patent can exploit it independently without other's consent but cannot assign or grant exclusive licences without consent of all co-owners [VERIFY] | Patents Act 1970 s.50 [VERIFY]  |
| **Software (all jurisdictions)** | Copyright assignment in software jointly developed by employees of each party: confirm copyright vests in the JV entity (requires written assignment) [VERIFY]                                       | Various copyright statutes      |
| **Moral rights**                 | France, Germany: moral rights inalienable; waiver not possible for individual authors' moral rights — practical issue for creative/media JVs                                                         | French CPI Art. L121-1 [VERIFY] |

**Classification triggers:**

- **RED**: No background IP licence grant to the JV (JV cannot operate); joint ownership of foreground IP without addressing the jurisdictional consequences of joint ownership; no IP reversion mechanism on JV termination; no employee invention assignment
- **YELLOW**: Background IP licence scope broader than JV's business need (risk of inadvertent IP grant beyond JV scope); foreground IP ownership vague ("jointly owned"); no cross-licence on exit
- **GREEN**: Clear background IP licence with defined scope and reversion; foreground IP owned by JV entity with cross-licence grant to each party on exit/dissolution; employee invention assignment in place; moral rights waiver obtained where applicable

[JURISDICTION-SPECIFIC]

- **India**: IP contributed to an Indian JV by a foreign party may require RBI/FEMA approval if the contribution is treated as foreign investment (IP-for-equity structures) [VERIFY]

### 12. Confidentiality

**Key drafting and review points:**

- **Scope**: all information exchanged in connection with the JV, including proprietary information of each party
- **Duration**: typically for the JV term + [3-5] years post-termination; trade secrets often protected indefinitely
- **Permitted disclosures**: to employees/contractors on need-to-know basis; to lenders and advisors (with back-to-back confidentiality); required by law (court order, regulatory request)
- **Return/destruction**: on termination, all confidential information returned or destroyed; certification required
- **Information barriers**: if each party has a competing business, consider information barriers (Chinese walls) between JV employees and the parties' retained businesses

**Classification triggers:**

- **RED**: No confidentiality obligation; confidentiality obligations do not extend to JV term (pre-term disclosures not covered)
- **YELLOW**: Confidentiality term too short (< 3 years post-termination); no return/destruction obligation; no information barrier provision where parties have competing businesses
- **GREEN**: Comprehensive confidentiality with appropriate carve-outs; extended protection for trade secrets; information barrier framework for sensitive commercial information

### 13. Representations and Warranties

**Key drafting and review points:**

- **Authority and capacity**: each party has corporate authority to enter the JV agreement; no conflict with existing agreements or applicable law
- **IP representations**: each party has the right to contribute/license its background IP; no third-party IP claims
- **Financial condition**: each party has sufficient financial resources to meet its capital contribution obligations
- **No prior agreements**: no existing agreements that would prevent participation in the JV
- **Regulatory compliance**: each party is compliant with applicable law; no pending regulatory proceedings that could materially affect the JV
- **Survival period**: representations should survive closing for a defined period (typically 18-24 months for corporate warranties; IP warranties often longer)

**Classification triggers:**

- **RED**: No IP representation (if IP is a key contribution); no regulatory compliance warranty; representations do not survive closing
- **YELLOW**: Representations too heavily qualified (material adverse effect qualifications on every representation); no remedy for warranty breach specified
- **GREEN**: Full representation set matched to the nature of contributions; clear survival period; remedy for breach specified (indemnification with cap or buy-out trigger)

### 14. Termination and Dissolution

**Key drafting and review points:**

- **Termination events**:
  - Expiry of fixed term
  - Material and unremedied breach (with cure period)
  - Insolvency or receiver/administrator appointment
  - Change of control of either party (if change of control is a termination trigger)
  - Regulatory trigger (loss of licence, regulatory prohibition)
  - Unanimous agreement to dissolve
  - Deadlock (after Tier 4 mechanisms exhausted)
- **Dissolution waterfall** (adapt to entity type):
  1. Payment of JV's creditors and liabilities
  2. Return of outstanding capital contributions (in priority order if different contribution dates)
  3. Payment of preferred returns (if applicable)
  4. Distribution of remaining assets pro-rata to ownership interests
- **IP reversion on dissolution**: background IP licences terminate; foreground IP: either (i) distributed in-kind (impractical for jointly developed IP), (ii) cross-licensed to both parties, or (iii) sold to the highest bidder with proceeds in the waterfall
- **Ongoing contracts**: who assumes existing JV contracts on dissolution? What happens to JV employees?
- **Liquidation preference**: if any party has a liquidation preference (typically financial investors), specify the amount and priority

**Classification triggers:**

- **RED**: No termination events defined; no dissolution waterfall; IP reversion not addressed; no plan for JV employees on dissolution
- **YELLOW**: Termination events too narrow (omits regulatory trigger or insolvency); dissolution waterfall present but liquidation preference not modelled; no IP cross-licence on dissolution
- **GREEN**: Comprehensive termination events; fully modelled dissolution waterfall; IP reversion and cross-licence mechanism; employee transition plan (TUPE in UK context [VERIFY])

[JURISDICTION-SPECIFIC]

- **UK**: TUPE (Transfer of Undertakings (Protection of Employment) Regulations 2006) may apply to JV employees on dissolution or transfer of business — affects employment costs on dissolution [VERIFY]
- **India**: Labour law implications of JV dissolution: Industrial Disputes Act 1947 retrenchment compensation; gratuity obligations under Payment of Gratuity Act 1972 [VERIFY]
- **US**: WARN Act (29 U.S.C. § 2101) may require 60-day notice to employees before mass layoff or plant closing on dissolution [VERIFY]

### 15. Tax and Structuring

**Key drafting and review points:**

[JURISDICTION-SPECIFIC — US]:

- **LLC vs. C-Corp**: LLC treated as partnership (multi-member) or disregarded entity (single-member) by default under check-the-box regulations (Treas. Reg. § 301.7701-3); parties must make affirmative election if corporate treatment desired
- **Section 704(b) allocations**: must have substantial economic effect; capital accounts must be maintained; liquidating distributions must follow capital accounts
- **Section 704(c) built-in gain**: if IP or appreciated assets are contributed, § 704(c) allocations must address built-in gain at the time of contribution to prevent taxable event deferral from being disproportionately shifted
- **Section 1031 like-kind exchange**: if JV involves real property exchange, confirm § 1031 eligibility
- **FIRPTA**: if a foreign party holds US real property through the JV, FIRPTA withholding applies on disposition [VERIFY]

[JURISDICTION-SPECIFIC — UK]:

- **Company vs. partnership**: UK JV structured as limited company: subject to corporation tax (25% main rate as of 2023); distributing profits as dividends: subject to withholding tax for non-UK shareholders (0% for UK companies; treaty rate for foreign shareholders) [VERIFY]
- **Stamp duty on JV shares**: 0.5% SDLT on share transfers; stamp duty reserve tax for paperless transfers
- **EIS/SEIS**: UK JV formed as company may be eligible for EIS relief for individual investors [VERIFY — structure-dependent]
- **Transfer pricing**: related-party transactions (IP licences, management fees, intercompany loans) between parties and the JV must be at arm's length (TIOPA 2010 s.147) [VERIFY]

[JURISDICTION-SPECIFIC — EU]:

- **Withholding tax**: EU Parent-Subsidiary Directive (2011/96/EU) exempts withholding tax on dividends distributed by EU subsidiaries to EU parent companies with ≥10% shareholding [VERIFY]; benefits depend on double-tax treaties for third-country parties
- **VAT grouping**: JV entity may be eligible to join the parent's VAT group under applicable national law; implications for inter-company transactions [VERIFY]
- **EU State Aid**: tax arrangements with the JV entity must not constitute illegal State Aid (EU Treaty Art. 107-109) — relevant for government-sponsored JVs

[JURISDICTION-SPECIFIC — India]:

- **Entity type**: Indian private limited company or LLP; LLP has greater flexibility in profit allocation and no mandatory dividend distribution tax (post-DDT abolition 2020) but transfer pricing still applies
- **TDS on dividends**: dividend from Indian company subject to TDS at 10-20% for foreign shareholders; rate depends on applicable DTAA [VERIFY]
- **Transfer pricing**: transactions between JV and foreign parent/other party are subject to Chapter X of the Income Tax Act 1961; maintain TP documentation [VERIFY]
- **FEMA on dividends and distributions**: no FEMA restriction on repatriating dividends from Indian companies; capital repatriation (on exit) subject to FEMA pricing guidelines [VERIFY]

**Classification triggers:**

- **RED**: LLC allocation mechanism does not comply with § 704(b); FIRPTA withholding not addressed for US real property JVs; no transfer pricing analysis for IP licensing within the JV
- **YELLOW**: Tax structuring present but no exit tax modeling; withholding tax not addressed; no TP documentation obligation in JV agreement
- **GREEN**: Full tax analysis completed; § 704(b) compliance confirmed; withholding tax addressed in distribution clause; TP documentation obligation included; exit tax modelled

### 16. Regulatory Compliance

**Key drafting and review points:**

- **Anti-bribery and corruption**: FCPA (15 U.S.C. §§ 78dd-1 et seq.) compliance obligations; UK Bribery Act 2010 (ss.1, 2, 6, 7); India PMLA and Prevention of Corruption Act
- **Sanctions**: OFAC, EU sanctions (Council Regulation 833/2014 and related); HM Treasury OFSI (UK); include unilateral termination right if sanctions trigger
- **Export control**: EAR/ITAR (US); Dual-Use Regulation 2021/821 (EU); SCOMET (India) — relevant if JV involves dual-use technology
- **Data protection**: applicable data protection law for the JV entity's processing activities (GDPR, UK GDPR, PDPB India)
- **Environmental compliance**: ESG obligations, EIA requirements for industrial JVs
- **Modern slavery**: UK Modern Slavery Act 2015 (for JVs with UK operations or turnover ≥ £36M) [VERIFY]
- **Audit rights**: each party should have audit rights over the JV's compliance with the foregoing

**Classification triggers:**

- **RED**: No FCPA/Bribery Act compliance representation or obligation in a cross-border JV; no termination right on sanctions designation; no audit rights
- **YELLOW**: Anti-bribery representation present but no ongoing compliance obligation; no sanctions termination right; GDPR DPA not addressed for EU-processing JVs
- **GREEN**: Comprehensive compliance framework; sanctions termination right; export control obligations; audit rights; data protection DPA in place

### 17. Governing Law and Dispute Resolution

**Key drafting and review points:**

- **Multi-tier dispute resolution**: negotiation → senior management escalation → mediation → arbitration (or litigation)
- **Arbitration strongly preferred** for international JVs: enforce arbitral award under New York Convention (157 signatories) vs. enforcing a foreign court judgment (no equivalent treaty)
- **Arbitration institution**: ICC, LCIA, SIAC, AAA, HKIAC — choice affects procedure, cost, and enforcement optics in counterparty's jurisdiction
- **Seat of arbitration**: determines supervisory court; curial law; available interim relief mechanisms; popular seats: London, Singapore, New York, Paris, Geneva
- **Carve-outs from arbitration**: urgent interim relief; IP injunctions; expert determination on valuation
- **Expert determination**: binding on valuation and technical disputes; non-arbitral; specify institution (RICS, CEDR, ICEDR) and procedure

**⟁ CLARIFY** — Dispute resolution mechanism:

- If India is a JV party, note that enforceability of foreign arbitral awards against Indian assets requires separate consideration; domestic arbitration under the Arbitration and Conciliation Act 1996 may be more practical for some disputes. [VERIFY with Indian counsel]

**Classification triggers:**

- **RED**: No governing law clause; no dispute resolution mechanism; no multi-tier escalation before arbitration/litigation; pathological arbitration clause (e.g., "disputes to be settled amicably or by arbitration in accordance with ICC rules by a sole arbitrator in [two different cities]")
- **YELLOW**: Governing law clause present but dispute resolution is litigation-only for an international JV (enforcement risk); no senior management escalation; no expert determination for valuation disputes
- **GREEN**: Governing law clearly specified; multi-tier dispute resolution; arbitration with named institution and seat; expert determination for valuation; carve-outs for urgent relief and IP injunctions

[JURISDICTION-SPECIFIC]

- **India**: The Arbitration and Conciliation (Amendment) Act 2019 introduced provisions to promote institutional arbitration; arbitral award from international commercial arbitration centre is enforceable in India [VERIFY]
- **UK**: Arbitration Act 2025 (expected to come into force, replacing Arbitration Act 1996) — confirm current law [VERIFY]
- **US**: Federal Arbitration Act (9 U.S.C. §§ 1 et seq.) governs enforceability of arbitration agreements in commerce

### 18. Boilerplate

**Key drafting and review points:**

- **Entire agreement**: no reliance on pre-contractual representations not incorporated in the JV agreement; carve-out for fraud
- **Amendment**: written amendments only; signed by authorized representatives of all parties
- **Assignment and change of control**: JV agreement rights are generally personal and not assignable without consent; change of control of either party is a significant event — decide whether it triggers exit rights or requires consent
- **Notices**: method (email/physical delivery), addresses, deemed receipt timing
- **Force majeure**: specify events; notification obligation; mitigation; long-stop termination right
- **Third-party rights**: English law: Contracts (Rights of Third Parties) Act 1999 applies unless excluded; ensure JV employees, lenders, and other third parties have (or do not have) rights under the JV agreement as intended
- **Counterparts and electronic execution**: permit electronic signatures (eIDAS in EU; Electronic Signatures in Global and National Commerce Act (ESIGN) in US; The Information Technology Act 2000 in India)

---

## Deviation Severity Classification

### GREEN — Acceptable / Standard

The clause aligns with market standard for this type of JV or is favourable to the
reviewing party. Minor variations that are commercially reasonable and do not materially
increase risk.

**Examples:**

- Reserved matters list slightly shorter than party's preference but covers all critical items
- ROFO duration of 30 days instead of preferred 45 days
- Governing law in a reputable commercial jurisdiction

**Action**: Note for awareness. No negotiation needed.

### YELLOW — Negotiate

The clause falls outside the standard position but within a negotiable range. Requires
attention and likely negotiation but not immediate escalation.

**Examples:**

- Deadlock mechanism present but valuation methodology vague
- Put/call option price formula references only one valuation method with no tiebreaker
- Non-compete scope broader than JV's operational territory by one country
- Distribution policy has no minimum distribution percentage

**Action**: Generate specific redline language. Provide fallback position. Estimate
business impact of accepting vs. negotiating.

### RED — Escalate / Restructure

The clause falls outside the acceptable range, poses material risk, or is potentially
unenforceable. Requires senior counsel review or business decision-maker sign-off.

**Examples:**

- No deadlock mechanism in a 50/50 JV
- Put/call price manipulable (e.g., "agreed fair value" without a process for agreement)
- Non-compete void under governing law (California, India) with no replacement protection
- IP foreground ownership vested in one party with no cross-licence on exit
- Exit mechanism has no completion timeline (closing never required)
- FEMA-incompatible exit price guarantee for Indian JV with foreign party

**Action**: Explain the specific risk with legal basis. Provide market-standard alternative
language. Estimate exposure. Recommend escalation path.

---

## Actionable Output Per Finding

For each YELLOW and RED item, generate a redline using this format:

```
**Clause**: [Section reference and clause name]
**Finding Type**: [Missing / Deviation / Unenforceable risk / Market below standard]
**Current language**: "[exact quote from the agreement, or 'Clause absent']"
**Proposed redline**: "[specific alternative language, ready to insert]"
**Rationale**: [1-2 sentences explaining why — suitable for sharing with counterparty's counsel]
**Legal basis**: [Relevant statute, regulation, or principle — or "General JV market practice"; if from memory, mark [VERIFY]]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback position**: [Alternative position if primary redline is rejected]
```

---

## Prioritization Framework

### Tier 1 — Must-Haves (Deal-Breakers)

Issues where the party cannot proceed to signing without resolution:

- No deadlock mechanism in a 50/50 JV (creates unworkable impasse)
- IP provisions that jeopardize core background IP or fail to provide reversion
- Exit mechanism with no enforceable completion obligation
- Non-compete obligations void under governing law with no replacement protection
- Regulatory non-compliance (FEMA pricing violation; merger control notification missed)
- Capital call obligations unlimited with no exit right if unable to fund

### Tier 2 — Should-Haves (Strong Preferences)

Issues that materially affect risk but have negotiation room:

- Valuation methodology vague (add independent expert + baseball provision)
- Reserved matters list too narrow (add 2-3 critical items)
- Distribution policy missing minimum percentage
- Transfer pricing documentation obligation missing
- Tag-along and drag-along not fully symmetrical

### Tier 3 — Nice-to-Haves (Concession Candidates)

Issues that improve the position but can be conceded strategically:

- Preferred governing law (if alternative is reputable)
- ROFO duration extended from 30 to 45 days
- Dispute resolution institution preference (LCIA vs. ICC — both reputable)
- Minor definitional improvements
- Information barrier formality requirements

**Negotiation strategy**: Lead with Tier 1 items as conditions to signing. Trade Tier 3
concessions to secure Tier 2 wins. Never concede on Tier 1 without full escalation.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                       | Fail Action                                              |
| -------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established principle                           | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction                                | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments or repeal                                                     | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the JV agreement's governing law; no assumptions from other jurisdictions leaking in | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden                                                                  | Add confidence qualifier                                 |

### Self-Interrogation for RED Items

For any clause classified as RED, apply this 3-pass self-interrogation before delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the risk assessment follow logically from the statute/principle cited?
- Would a court or arbitral tribunal in this jurisdiction actually reach this conclusion?
- Is there a counter-argument the counterparty's counsel will make?

**Pass 2 — Completeness**:

- Have all relevant statutes, regulations, and principles been considered?
- Have any relevant cases or principles been missed?
- Are there regulatory dimensions (merger control, FEMA, FCPA) not yet addressed?

**Pass 3 — Challenge**:

- What is the strongest argument that this clause IS acceptable?
- Under what commercial circumstances might a reasonable JV counsel accept this risk?
- Is the RED classification proportionate, or is this actually YELLOW with specific mitigations?

If any pass reveals a weakness, revise the analysis before delivery. Mark the audit trail
with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material clause analysis or drafting recommendation, assign a confidence level:

| Level        | Range     | Meaning                                                 | Action                                                   |
| ------------ | --------- | ------------------------------------------------------- | -------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled law, clear statute, established market practice | State with confidence                                    |
| **High**     | 0.80-0.94 | Strong authority, minor interpretation questions        | State with brief caveat                                  |
| **Probable** | 0.60-0.79 | Good arguments but reasonable minds could differ        | State with explicit reasoning and contra-indicators      |
| **Possible** | 0.40-0.59 | Genuinely uncertain, competing authorities              | Flag for counsel review with both sides of the argument  |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative                                 | Do not assert; flag as "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every JV agreement output MUST include a Glass Box audit section at the end. This makes
the reasoning traceable and auditable:

```yaml
glass_box:
  document: "[JV Agreement title and date]"
  document_type: "Joint Venture Agreement"
  mode: "[Draft / Review / Specific clause analysis]"
  user_side: "[Party A / Party B / Neutral drafter]"
  jv_structure: "[Delaware LLC / English company / Indian Pvt Ltd / LLP / Other]"
  ownership_split: "[e.g., 50/50 / 60/40 / other]"
  governing_law: "[Jurisdiction identified from the agreement or user instructions]"
  jurisdictions_covered: "[US / UK / EU / IN — as applicable]"
  clauses_reviewed: "[number out of 18]"
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  regulatory_prescreen:
    eu_full_function: "[Full-function / Cooperative / N/A]"
    us_hsr: "[Above threshold / Below threshold / Not assessed]"
    india_cci: "[Above threshold / Below threshold / Not assessed]"
    sector_approvals: "[Required / Not required / Not assessed]"
  deadlock_mechanism: "[Russian roulette / Texas shoot-out / Expert determination / Put/call / None]"
  exit_mechanisms: "[Put / Call / ROFO / ROFR / Tag-along / Drag-along / IPO / None]"
  ip_structure: "[JV entity owns foreground / Joint ownership / Party-owns / Not addressed]"
  noncompete_jurisdictions: "[List jurisdictions; flag enforceability concerns]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to temp file or 'Not created']"
  statutes_consulted:
    - "[Statute 1 — VERIFIED (legalcode-mcp) or UNVERIFIED]"
    - "[Statute 2 — VERIFIED or UNVERIFIED]"
  case_law_consulted:
    - "[Case 1 — VERIFIED or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified legal review"
```

---

## Multi-Stakeholder Mapping

JV agreements affect a wider set of stakeholders than typical bilateral contracts.
Map all affected parties before analysis or drafting:

| Stakeholder                    | Role                    | Affected Provisions                                      | Interest                                     | Action Required                             |
| ------------------------------ | ----------------------- | -------------------------------------------------------- | -------------------------------------------- | ------------------------------------------- |
| Party A                        | JV parent / co-venturer | All                                                      | Governance control; exit value               | Sign / Negotiate                            |
| Party B                        | JV parent / co-venturer | All                                                      | Governance control; exit value               | Sign / Negotiate                            |
| JV Entity                      | Subsidiary / vehicle    | All — entity law compliance                              | Arm's length dealings; regulatory compliance | Corporate governance setup                  |
| JV Employees                   | Operations              | IP assignment; non-solicitation; dissolution (TUPE/WARN) | Employment continuity                        | Invention assignment; employment agreements |
| JV Lenders                     | Financing               | Capital call; distributions; security                    | Debt service coverage                        | Lender consent rights; pledge agreements    |
| Regulators (antitrust)         | Oversight               | Merger control; non-competes                             | Competition law compliance                   | Notification; filing                        |
| Tax Authorities                | Revenue                 | Tax structuring; transfer pricing                        | Tax collection                               | TP documentation; withholding compliance    |
| Third-Party IP Owners          | Licensors               | Background IP licences                                   | Royalty; scope compliance                    | Sub-licence consent (if required)           |
| Minority Shareholders (if any) | Co-venturer             | Exit; governance; distribution                           | Protection from majority oppression          | Tag-along; reserved matters                 |

---

## Anti-Patterns

Explicit catalogue of what NOT to do when drafting or reviewing joint venture agreements:

1. **Deadlock without a resolution mechanism in a 50/50 JV** — The most catastrophic error. Without a contractual mechanism, deadlock leads to unfair prejudice/just and equitable winding-up petitions, litigation, and destruction of JV value. Every 50/50 JV must have a multi-tier deadlock resolution mechanism.

2. **Russian roulette without assessing financial asymmetry** — Russian roulette incentivizes rational pricing only when both parties can afford to be the buyer. When one party is significantly better capitalized, the weaker party will be forced to sell at a low price (or be outbid). Assess relative financial capacity before selecting the mechanism.

3. **Vague IP foreground ownership ("jointly owned")** — "Jointly owned" means fundamentally different things in different jurisdictions. In the US, each joint owner can licence independently; in the UK, consent of all is required. State the specific ownership and licensing arrangement, don't rely on local law defaults.

4. **Non-compete without jurisdiction-specific enforceability analysis** — A non-compete valid in Delaware is void in California and very difficult to enforce in India under Section 27 of the Contract Act. Drafting a single non-compete clause for a multi-jurisdiction JV without jurisdiction-specific analysis creates a false sense of security.

5. **Exit mechanism with no valuation tiebreaker** — Two independent valuers will frequently disagree. A shotgun clause without a valuation determination process is not a mechanism — it is an invitation to a valuation dispute. Always specify a tiebreaker (baseball arbitration, average, ICEDR expert).

6. **FEMA-incompatible exit pricing for Indian JVs** — Guaranteeing a minimum purchase price (floor) to a foreign seller of shares in an Indian company may violate FEMA pricing guidelines, which prohibit the foreign seller from receiving more than the fair market value of the shares. This is one of the most common errors in India-inbound JV agreements.

7. **Reserved matters with unanimity but no deadlock mechanism** — A JV with a unanimous reserved matters requirement and no deadlock resolution mechanism is an engineered impasse. If either party has a veto over material decisions, the JV agreement must address what happens when the veto is exercised permanently.

8. **Capital call with no cap and no exit right** — An open-ended capital call obligation with no maximum and no right to exit if unable to fund creates unlimited financial exposure and an unconscionable obligation. Always cap the aggregate capital obligation and provide an exit mechanism for a party that is genuinely unable to fund.

9. **Background IP licence without reversion on JV termination** — If the JV agreement does not specify that background IP licences terminate on dissolution, the JV entity (controlled by whoever is the liquidator) may have an argument that the licences survive. Specify the reversion mechanism explicitly.

10. **Ignoring transfer pricing for IP licences into the JV** — If one party licences IP to the JV for less than arm's length consideration, this creates a transfer pricing risk (US: § 482; UK: TIOPA 2010 s.147; India: Chapter X IT Act). Quantify and document the arm's-length royalty rate.

11. **Change of control not addressed** — If Party A is acquired by Party A's competitor, Party B's JV rights become valueless or worse (the competitor now has access to the JV's business and IP). Change of control events must be defined and should trigger exit rights or require consent.

12. **Drag-along without minimum price protection** — A drag-along clause that compels the minority to sell at any price the majority receives — including a distressed sale — is commercially coercive. Include a minimum price floor (typically: greater of (i) fair market value and (ii) return of contributed capital plus preferred return).

13. **Merger control filing missed** — Cross-border JVs forming a full-function JV frequently trigger EU Merger Regulation notification and/or US HSR filing requirements. Missing a mandatory filing results in gun-jumping fines (EU: up to 10% of worldwide turnover; US: daily civil penalties). Always perform a merger control pre-screen.

14. **Arbitration clause naming two different seats** — A pathological arbitration clause that names two different seats or institutions renders arbitration unworkable and may result in no effective dispute resolution mechanism. Specify one institution, one set of rules, one seat.

15. **Treating the JV agreement as a static document** — JVs evolve; the initial business plan may become obsolete. A JV agreement with no amendment mechanism (or a unanimity requirement for all amendments, making evolution practically impossible) becomes unfit for purpose. Include a structured amendment process with clear approval thresholds.

16. **Profit allocation without § 704(b) analysis for US LLCs** — In a US LLC JV, profit and loss allocations that do not satisfy the substantial economic effect requirements of IRC § 704(b) will be recast by the IRS to ownership percentages. The operating agreement must be drafted by a US tax attorney familiar with § 704(b) regulations.

17. **Ignoring TUPE on JV dissolution (UK)** — If the JV's business is transferred on dissolution (including to one of the JV parents), TUPE (Transfer of Undertakings (Protection of Employment) Regulations 2006) may apply, triggering automatic transfer of JV employees and significant cost implications. Assess and plan for TUPE.

18. **Confidentiality without information barriers** — Where both JV parties also operate competing businesses, a confidentiality obligation alone does not prevent the inadvertent flow of the JV's competitively sensitive information to a party's competing business division. Consider structural information barriers (Chinese walls) or recusal obligations for board members with conflicts of interest.

---

## Writing Standards

Apply plain-language discipline to all JV agreement drafting and review output:

**For redline rationales** (shared with counterparty's counsel):

- Plain language; no jargon or filler
- Active voice: "This clause compels the minority to sell at any price" not "A situation may arise in which the minority's shares are required to be sold"
- Short sentences; one point per sentence
- Name the actor: "Party A must notify Party B within 5 business days"
- Specific, not vague: cite the provision and the risk, not "this may be problematic"

**For internal analysis** (delivered to the user):

- Same plain-language standards
- May include more technical legal analysis and jurisdiction-specific depth
- Confidence qualifiers where appropriate
- Glass Box audit trail appended

**Quality gates before delivery**:

1. Can a non-lawyer business stakeholder understand the executive summary?
2. Can the counterparty's JV counsel understand and respond to each redline?
3. Is every legal claim backed by a specific citation (or flagged [VERIFY])?
4. Are any phrases vague, hedging, or ambiguous? If yes, fix.
5. Could any sentence be shorter without losing meaning? If yes, shorten.
6. Have all jurisdiction-specific concepts been properly marked [JURISDICTION-SPECIFIC]?
7. Have all unverified legal references been marked [VERIFY]?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 3, search for jurisdiction-relevant statutes, regulations, and case law for:
  - Fiduciary duties and minority protection rules in the JV jurisdiction
  - Deadlock mechanism enforceability (Russian roulette, shot-gun clauses)
  - Non-compete enforceability in each JV party's jurisdiction
  - IP ownership and joint ownership rules by jurisdiction
  - Merger control thresholds (current year — thresholds are adjusted annually)
  - FEMA pricing guidelines and RBI circulars (for India JVs)
  - Tax provisions (§ 704(b), TIOPA 2010, Chapter X IT Act)
- Save the most relevant results to `/tmp/legalcode-jva-authority.md`
- Reference verified authority throughout clause analysis and drafting
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail
- Check statutory currency for all cited provisions

**Without legalcode-mcp:**

- Mark every statutory and case law reference with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Include a prominent notice in the output that legal citations require independent verification
- Focus analysis on commercial risk assessment and structural issues rather than legal certainty
- Recommend user obtain local counsel opinion for jurisdiction-specific provisions (especially FEMA India, § 704(b) US, CA 2006 UK)

---

## Localization Notes

This skill is jurisdiction-agnostic for the US, UK, EU, and India. All jurisdiction-specific
content is marked [JURISDICTION-SPECIFIC]. When working with a specific jurisdiction:

**US (Delaware preferred)**:

- Confirm entity type: Delaware LLC (maximum governance flexibility) vs. C-Corp (preferred for IPO exit)
- Delaware LLC: operating agreement is the governing document; articles of organization are minimal
- Fiduciary duties are waivable in Delaware LLCs (6 Del. C. § 18-1101(c)) — specify in operating agreement [VERIFY]
- Tax: confirm partnership tax treatment; § 704(b) compliance; FIRPTA for foreign members

**UK (England and Wales)**:

- Confirm entity type: limited company (most common) vs. LLP (more flexible but different tax treatment)
- CA 2006 mandatory provisions apply: directors' duties (ss.171-177); pre-emption rights (s.561, disapplicable); unfair prejudice petition (s.994)
- IA 1986 s.122(1)(g): just and equitable winding up is available regardless of contractual provisions
- Stamp duty and SDRT on share transfers

**EU (cross-border)**:

- Run full-function JV test under EU Merger Regulation Art. 3(4)
- If full-function and thresholds met: mandatory ECON notification before closing
- Art. 101 TFEU: ancillary restraints (non-competes up to 3 years if knowhow transferred) are permitted; scrutinize further restrictions
- Governance may be subject to national company law in the JV entity's jurisdiction (Germany: co-determination; France: works council rights)

**India**:

- Companies Act 2013: private limited company is the standard JV vehicle; maximum 200 members
- FEMA compliance: FDI route (automatic vs. approval); pricing guidelines for equity allotment and transfer; RBI approval for structures with guaranteed returns
- CCI: filing requirement for combinations above threshold; sector-specific approvals (banking: RBI; insurance: IRDAI; telecom: DoT/TRAI)
- Non-competes: Section 27 Indian Contract Act — post-exit restrictions are generally void; focus on IP protection and confidentiality as substitutes
- Tax: TDS on dividends; transfer pricing documentation; treaty benefits depend on DTAA between India and the foreign party's country

---

## Output Format Template

Structure the final deliverable as follows:

### For Review Mode:

```markdown
## JV Agreement Review Summary

**Document**: [JV Agreement title and date]
**Parties**: [Party A / Party B / JV Entity]
**Your Side**: [Party A / Party B / Neutral]
**JV Structure**: [Entity type and jurisdiction]
**Ownership Split**: [e.g., 50/50]
**Governing Law**: [Jurisdiction]
**Reviewer**: AI-assisted — requires qualified legal review
**Date of Review**: [date]

---

## Regulatory Pre-Screen Results

| Item                | Outcome  | Action   |
| ------------------- | -------- | -------- |
| EU full-function JV | [Result] | [Action] |
| US HSR              | [Result] | [Action] |
| India CCI           | [Result] | [Action] |
| Sector approvals    | [Result] | [Action] |

---

## Executive Summary

**Overall Risk Assessment**: [High / Medium / Low]
**Top 3 Issues**:

1. [Issue] — [Severity] — [Recommended action]
2. [Issue] — [Severity] — [Recommended action]
3. [Issue] — [Severity] — [Recommended action]

**Deadlock Mechanism**: [Present / Absent / Inadequate]
**Exit Mechanisms**: [Present / Absent / Partially addressed]
**IP Structure**: [Adequate / Inadequate — specific gaps]
**Non-Compete Enforceability**: [Jurisdiction-by-jurisdiction assessment]

**Negotiation Strategy**: [Summary of recommended approach]

---

## Clause-by-Clause Analysis

### [Clause 1: Name] — [GREEN / YELLOW / RED]

[Analysis — current language, issue, legal basis, confidence score]

### [Clause 2: Name] — [GREEN / YELLOW / RED]

[...]

---

## Redlines and Recommendations

### Must-Have Redlines (Tier 1)

**Clause**: [ref] | **Priority**: Must-have
**Current**: "[...]"
**Proposed**: "[...]"
**Rationale**: [...]
**Legal basis**: [...]
**Fallback**: [...]

### Should-Have Redlines (Tier 2)

[...]

### Nice-to-Have Redlines (Tier 3)

[...]

---

## Multi-Stakeholder Mapping

[Table from Multi-Stakeholder Mapping section, populated]

---

[Glass Box Audit Trail — YAML block]
```

### For Draft Mode:

```markdown
## JV Agreement — Draft Framework

**Parties**: [Party A / Party B]
**JV Entity**: [Name and jurisdiction of incorporation]
**JV Purpose**: [Business purpose]
**Ownership Split**: [e.g., 50/50]
**Governing Law**: [Jurisdiction]
**Date Prepared**: [date]

---

## Regulatory Pre-Screen

[Pre-screen results and required actions before drafting proceeds]

---

## Agreement Structure

[Clause-by-clause draft framework, covering all 18 clause categories, with:

- Recommended approach for this specific JV
- Draft language (or instruction for legal counsel to finalize)
- Key issues flagged for the parties to resolve before signing
- Jurisdiction-specific provisions with [JURISDICTION-SPECIFIC] markers
- [VERIFY] markers on all legal references requiring independent verification]

---

[Glass Box Audit Trail — YAML block]
```

---

## Provenance

Created by Legalcode (2026-03-19). Legalcode original synthesis via Mode A skill creation
workflow with 2-agent parallel research pipeline (Structural Agent analyzing reference
standard `legalcode-contract-review` and adjacent corporate-transactions skills; Legal
Research Agent conducting multi-query JV law research covering US/UK/EU/India). Research
coverage: Delaware LLC Act § 18-1101 fiduciary duty waivability; CA 2006 ss.168, 171-177,
561, 829, 994; IA 1986 s.122(1)(g); EU Merger Regulation 139/2004 Art. 3(4) full-function
JV test; TFEU Art. 101 and Commission Notice on Ancillary Restraints 2005/C 56/03; US HSR
Act 15 U.S.C. § 18a; India Competition Act 2002 and CCI combination thresholds; FEMA 1999
and pricing guidelines (equity allotment and transfer); Companies Act 2013 and Indian
Patents Act 1970 s.50; IRC § 704(b) substantial economic effect; § 704(c) built-in gain;
35 U.S.C. § 262 joint patent ownership; Patents Act 1977 s.36; UK Bribery Act 2010;
FCPA 15 U.S.C. §§ 78dd-1 et seq.; Cavendish Square Holding BV v. Makdessi [2015] UKSC 67
restraint of trade; Cal. Bus. & Prof. Code §§ 16600-16602.5; Section 27 Indian Contract
Act 1872 and Niranjan Shankar Golikari v. Century Spinning [1967]; EU Parent-Subsidiary
Directive 2011/96/EU; TIOPA 2010 s.147 transfer pricing; Chapter X IT Act 1961; TUPE
2006 (UK); WARN Act 29 U.S.C. § 2101 (US); FAA 9 U.S.C. §§ 1 et seq.; India Arbitration
and Conciliation (Amendment) Act 2019. Novel structural contributions: 18-clause JV
architecture (8 deep/10 standard); multi-tier deadlock resolution framework (4 tiers:
senior management → mediation → expert determination → mandatory offer mechanism);
Russian roulette / Texas shoot-out / put/call / winding up mechanism comparison with
jurisdiction-specific enforceability notes; FEMA-incompatible exit pricing as a RED
anti-pattern (India); reserved matters checklist with threshold guidance; exit valuation
methodology comparison table (5 methods); IP foreground/background ownership analysis
with joint ownership jurisdiction matrix (US § 262 / UK PA 1977 s.36 / India Patents Act
s.50); non-compete enforceability matrix (4 jurisdictions); tax structuring by entity type
and jurisdiction (US § 704(b)/(c); UK corporation tax and SDLT; EU Parent-Subsidiary
Directive; India TDS/FEMA/transfer pricing); regulatory pre-screen (EU MR full-function
test / US HSR / India CCI / sector approvals); 18 anti-patterns specific to JV agreement
failures; multi-stakeholder mapping (9 stakeholders); Glass Box YAML with JV-specific
fields (deadlock_mechanism, exit_mechanisms, ip_structure, regulatory_prescreen);
18/18 quality elements present. All legal citations marked [VERIFY] — verify against
authoritative sources before reliance.
