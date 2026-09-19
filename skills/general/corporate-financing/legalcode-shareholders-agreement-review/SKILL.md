---
name: legalcode-shareholders-agreement-review
description: Review shareholders agreements clause-by-clause — flag governance imbalances, generate confidence-scored
  redlines, and produce an auditable minority protection analysis. Use when reviewing shareholders agreements,
  voting agreements, investor rights agreements, subscription agreements, or any governance document covering
  drag-along and tag-along rights, anti-dilution protections (full ratchet vs. weighted average), ROFR/ROFO,
  pre-emptive rights, board composition and nomination rights, reserved matters, information and inspection
  rights, dividend policies, deadlock resolution mechanisms, and exit provisions (IPO, trade sale, buyback,
  redemption). Jurisdiction-aware with detailed US/UK/IN/AU coverage and [JURISDICTION-SPECIFIC] markers.
  GREEN/YELLOW/RED classification with redline suggestions. Evaluates minority protection adequacy and
  majority control balance across all 12 core SHA clause categories. Produces an auditable Glass Box analysis
  with Glass Box audit trail.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Shareholders Agreement Review

> **Disclaimer**: This skill provides a framework for AI-assisted shareholders agreement review.
> It does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before use. Laws change; verify current
> applicability before relying on any provision described here. Statutory and case law references
> cited from memory carry hallucination risk — verify against authoritative sources before
> relying on them. This skill covers a multi-jurisdictional topic; legal advice from counsel
> qualified in the specific governing law jurisdiction is essential.

---

## Purpose and Scope

This skill reviews shareholders agreements (SHAs), voting agreements, and investor rights
agreements clause-by-clause against market-standard positions and any available organizational
playbook. It identifies governance imbalances, minority protection gaps, and majority overreach,
classifies their severity, generates actionable redline suggestions, and produces a
confidence-scored, auditable analysis with a minority protection scorecard.

**Covers:**

- Clause-by-clause analysis across all 12 core SHA clause categories
- Minority protection vs. majority control balance assessment
- Deviation classification (GREEN / YELLOW / RED)
- Redline generation with fallback positions
- Missing clause detection
- Business impact assessment and negotiation strategy
- Jurisdiction-specific analysis across US, UK, India, and Australia
- Quality-verified output with Glass Box audit trail

**Does not:**

- Draft new shareholders agreements (use a drafting-specific skill)
- Provide legal advice or replace qualified corporate counsel
- Review financial models, cap tables, or valuation mechanics (refer to financial advisers)
- Provide advice on securities law compliance (prospectus, placement, SEBI/SEC filings)
- Apply exclusively to any single jurisdiction — jurisdiction-aware with [JURISDICTION-SPECIFIC] markers

**Complementary skills:**

- `legalcode-purchase-agreement-review` — for the SPA/APA reviewing the acquisition itself
- `legalcode-ma-due-diligence-checklist` — for the broader M&A due diligence workstream
- `legalcode-indemnification-analysis` — for deep-dive on the indemnification mechanics

---

## Jurisdiction and Governing Law

This skill is jurisdiction-aware, not jurisdiction-agnostic. Shareholders agreement analysis
requires jurisdiction-specific knowledge because statutory protections for minority shareholders,
the enforceability of governance provisions, and anti-dilution implementation mechanics vary
materially across jurisdictions.

**Key jurisdiction-specific differences covered:**

| Jurisdiction      | Primary Statute                          | Key Minority Remedy                  | Anti-Dilution Mechanics             |
| ----------------- | ---------------------------------------- | ------------------------------------ | ----------------------------------- |
| **US (Delaware)** | DGCL §§ 141(a), 218, 122(18)             | Breach of SHA + fiduciary duties     | Conversion price adjustment         |
| **UK**            | Companies Act 2006 §§ 33, 561, 994       | Unfair prejudice petition (§ 994)    | Conversion price or new share issue |
| **India**         | Companies Act 2013 §§ 241–242; FEMA 1999 | NCLT oppression petition (§ 241–242) | Promoter transfer / bonus shares    |
| **Australia**     | Corporations Act 2001 §§ 232–233, 254D   | Oppression remedy (§ 232)            | Conversion price or new share issue |

[JURISDICTION-SPECIFIC] Critical jurisdiction rules to verify for each review:

- **US (Delaware)**: Post-_Moelis_ legislative fix — DGCL § 122(18) (effective August 1, 2024)
  now expressly authorizes stockholder agreements containing governance rights including board
  size, director nominations, and transaction approval requirements. Fiduciary duties are not
  altered. Verify that governance provisions comply with updated DGCL standards. [VERIFY]

- **UK**: Section 994 Companies Act 2006 provides a broad unfair prejudice remedy — courts
  have found that breach of legitimate expectations (even informal ones) can ground a petition.
  _O'Neill v Phillips_ [1999] UKHL 24. No minority discount applied in § 994 buyouts (_Re Blue
  Index Ltd_ [2014]). [VERIFY]

- **India**: Oppression and mismanagement claims under Sections 241–242 Companies Act 2013 are
  non-arbitrable — foreign arbitration clauses do not oust NCLT jurisdiction. (_Anupam Mittal v.
  People Interactive_ — Bombay HC anti-enforcement injunction, September 2023). FEMA pricing
  norms constrain how put options and anti-dilution mechanisms are structured for foreign
  investors. SEBI Regulation 31B (effective June 2023) requires 5-yearly renewal by special
  resolution of special rights in listed companies. [VERIFY]

- **Australia**: Drag-along and tag-along are NOT statutory — must be in both SHA and company
  constitution to bind all current and future shareholders. Section 232 oppression remedy is
  available even for technically valid drag-along exercises conducted in bad faith or at undervalue.
  _Wayde v NSW Rugby League Ltd_ (1985) 180 CLR 459 objective unfairness test. [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming the
user's intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- Multiple valid approaches exist and the user's preference matters
- Ambiguity in the SHA creates a fork that only the user can resolve
- Risk tolerance or investment context is needed to classify severity correctly

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

### Step 1: Accept the Shareholders Agreement

Accept the SHA in any of these formats:

- **File**: PDF, DOCX, or other document format
- **URL**: Link to a document in a data room, cloud storage, or document management system
- **Pasted text**: SHA text pasted directly into the conversation
- **Multiple documents**: Accept related documents as a bundle (SHA + Investor Rights Agreement
  - Voting Agreement + Articles/Constitution) — review as an integrated set

If no SHA is provided, prompt the user to supply one.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask the user these questions. Present as structured
options where possible.

1. **Which side are you representing?**
   - Options: Minority investor (VC/PE), Majority investor, Founder/common shareholder, Company,
     Advisor to investor, Advisor to founders, Neutral analysis
   - _Why this matters_: The entire analysis flips depending on perspective. A drag-along threshold
     of 51% is dangerous for a minority and desirable for a majority.

2. **Company stage and deal type?**
   - Options: Seed / Angel round, Series A / Early VC, Series B+ / Growth VC, Private equity
     buyout, Joint venture / 50:50, Mature private company, Pre-IPO
   - _Why this matters_: Market standards differ materially by stage. Full ratchet anti-dilution
     is never acceptable at any stage but the reserved matters scope varies significantly between
     early VC and PE buyouts.

3. **Governing law and jurisdiction?**
   - Options: US (Delaware), US (other state), UK (England & Wales), India, Australia, Other
   - _Why this matters_: Statutory protections, anti-dilution implementation constraints, and
     the validity of governance provisions all vary by jurisdiction. This is not optional context.

4. **Primary concerns or focus areas?**
   - Options: Minority protection / anti-dilution, Exit mechanics / drag-along / tag-along,
     Board governance / reserved matters, Information and inspection rights, Deadlock resolution,
     Full comprehensive review
   - Allow multiple selections.
   - _Why this matters_: Focuses the analysis and determines whether to apply deep or standard
     depth tiers to each clause category.

5. **Deal context?** (Free text)
   - Prompt with: investment amount, percentage stake, other key investors, deal structure,
     strategic or financial objective, and whether this is a standard template or a negotiated
     document.
   - _Why this matters_: A 5% stake at seed stage gets different treatment than a 25% stake
     in a PE buyout. Context shapes severity classification.

If the user provides partial context, proceed with what is available and **state assumptions
explicitly**.

### Step 3: Load the Playbook

Check for an investment or governance playbook in local settings (e.g., `equity.local.md`,
`investment-playbook.local.md`, or similar configuration files).

The playbook should define:

- **Standard positions**: Preferred terms for each major SHA clause type
- **Acceptable ranges**: Terms that can be agreed without escalation
- **Escalation triggers**: Terms requiring senior partner, IC approval, or outside counsel

**If no playbook is configured:**

**⟁ CLARIFY** — Inform the user that no playbook was found, and ask which approach to take:

- **Option A: Set up a playbook now** — Walk through defining standard positions for key SHA
  clauses (anti-dilution type, drag-along threshold, board nomination rights, information
  rights frequency, reserved matters scope, deadlock mechanism). Takes time upfront but makes
  all future reviews more precise.
- **Option B: Proceed with general market standards** — Use widely-accepted VC/PE market
  standards as the baseline. Faster, but will not reflect the organization's specific investment
  philosophy or risk appetite.
- **Option C: Provide positions as we go** — Start the review and ask for preferred positions
  when relevant to each clause.

If proceeding without a playbook, label the review: "Based on general market standards (US/UK/
IN/AU as applicable) — not organizational investment positions."

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Identify the governing law from the SHA. Then use **legalcode-mcp** (if connected) to build a
working legal reference file for this review.

**Research process:**

1. **Identify the governing law** from the SHA (e.g., "laws of the State of Delaware," "laws
   of England and Wales," "laws of India," "laws of the State of New South Wales").

   **⟁ CLARIFY** — If any of these are true, ask before proceeding:
   - **No governing law clause**: Ask which jurisdiction the user expects to apply. Flag absence
     as a RED deviation.
   - **Multiple governing law clauses**: Identify which governs the main SHA and note the
     conflict.
   - **Mismatch between governing law and company incorporation**: A Cayman Islands company
     governed by English law is common (VC structure); a Delaware company with Indian law is
     unusual — confirm user is aware and whether to analyze under stated or expected law.

2. **Search legalcode-mcp** for jurisdiction-relevant authority:
   - Minority shareholder protection statutes and remedies
   - Anti-dilution implementation rules and constraints (especially FEMA for India)
   - Pre-emption rights under company law (statutory defaults)
   - Drag-along and tag-along enforceability requirements
   - Deadlock mechanism enforceability (Russian roulette, Texas shootout)
   - Oppression/unfair prejudice remedy scope and standard
   - Recent amendments: DGCL § 122(18) (August 2024), SEBI Regulation 31B (June 2023)

3. **Save the most relevant results** into a local temporary reference file:

   ```
   /tmp/legalcode-sha-review-authority.md
   ```

   Structure as:

   ```markdown
   # Legal Authority Reference — SHA Review

   ## Governing Law: [Jurisdiction]

   ## Date Gathered: [date]

   ### Statutes & Regulations

   - [Statute name, section, relevance]

   ### Case Law

   - [Case name, citation, key holding]

   ### Regulatory Guidance

   - [Regulator, guidance, relevance]
   ```

4. **Use this reference file throughout the analysis.** Mark all legalcode-mcp-sourced
   citations as VERIFIED in the Glass Box audit trail. Mark any reference not independently
   verified as [VERIFY].

**If legalcode-mcp is not connected:**

- Mark every statutory and case law reference with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed using the jurisdiction framework in this skill's Jurisdiction and Governing Law
  section as the primary legal reference

### Step 5: Assess Shareholder Structure and Deal Mechanics

Before clause-by-clause analysis, develop a clear picture of the company's ownership and
governance structure.

1. **Map the shareholder composition**:
   - Share classes and their rights (ordinary, preferred, multiple-vote, alphabet shares)
   - Percentage ownership (fully diluted vs. issued)
   - Investor tranches (seed, Series A, Series B, etc.) and their respective rights
   - Founder vs. investor concentration

2. **Identify the key deal parameters** relevant to SHA analysis:
   - Anti-dilution type: Full ratchet / Broad-based weighted average / Narrow-based weighted
     average / None
   - Drag-along threshold and triggering mechanics
   - Liquidation preference: 1x non-participating / 1x participating / Multiple non-participating
     / Multiple participating
   - Reserved matters level: Board only / Shareholder only / Both tiers
   - Exit mechanisms available: IPO / Trade sale / Put / Redemption / Buyback

3. **Produce a Structural Overview table** before clause analysis:

| Parameter              | SHA Provision | Market Standard              | Assessment         |
| ---------------------- | ------------- | ---------------------------- | ------------------ |
| Anti-dilution type     | [from SHA]    | Broad-based weighted average | [GREEN/YELLOW/RED] |
| Drag-along threshold   | [from SHA]    | 66.67%–75%                   | [GREEN/YELLOW/RED] |
| Liquidation preference | [from SHA]    | 1x non-participating         | [GREEN/YELLOW/RED] |
| Board composition      | [from SHA]    | Investor seat + quorum req.  | [GREEN/YELLOW/RED] |
| Reserved matters       | [from SHA]    | Board + shareholder levels   | [GREEN/YELLOW/RED] |
| Deadlock mechanism     | [from SHA]    | Multi-tier + mediation       | [GREEN/YELLOW/RED] |
| Information rights     | [from SHA]    | Quarterly + annual audit     | [GREEN/YELLOW/RED] |
| Pre-emption rights     | [from SHA]    | Pro-rata + oversubscription  | [GREEN/YELLOW/RED] |

Flag any RED items in the Structural Overview for priority treatment in Step 6.

**⟁ CLARIFY** — For complex multi-class equity structures, ask the user to confirm the
ownership table or provide a current cap table to ensure the analysis is accurate.

### Step 6: Clause-by-Clause Analysis

Analyze the SHA systematically across all 12 clause categories below. Read the entire SHA
before flagging issues — clauses interact (e.g., an uncapped drag-along combined with a low
threshold and no price floor creates a complete exit override for a small majority).

**⟁ CLARIFY** — For very long SHAs (50+ pages) or SHA bundles (SHA + IRA + Voting Agreement):

- Ask whether to perform a **full review** of all 12 clause categories, or a **priority review**
  focused on the user's stated concerns (Step 2) plus any RED items discovered in Step 5.
- If the SHA incorporates other documents (articles of association, separate investor rights
  agreement, registration rights agreement), ask whether those documents should be reviewed as
  part of this engagement.

Cover all 12 clause categories below. For each: assess against the playbook (or market
standards), note presence/absence, and classify GREEN / YELLOW / RED.

| #   | Clause Category                          | Depth    | Key Review Points                                                                                                 |
| --- | ---------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
| 1   | Drag-Along Rights                        | Deep     | Threshold, same-consideration, warranty scope, non-cash, price floor, notice, pre-emption interplay, good faith   |
| 2   | Tag-Along Rights                         | Deep     | Trigger, co-sell election, procure-buyer obligation, consideration parity, notice period, carve-outs              |
| 3   | Anti-Dilution Protections                | Deep     | Type (full ratchet vs. weighted average), formula, carve-outs, implementation mechanics, jurisdiction constraints |
| 4   | Pre-emptive Rights                       | Deep     | Scope, pricing, exercise window, oversubscription, carve-outs, statutory overlay                                  |
| 5   | Information and Inspection Rights        | Deep     | Frequency, scope, inspection access, material event notification, competitor carve-out, termination triggers      |
| 6   | Board Composition and Nomination Rights  | Deep     | Investor seats, quorum, observer rights, removal rights, independent directors, anti-dilution of board rights     |
| 7   | Reserved Matters                         | Deep     | Board vs. shareholder level, threshold, list scope, investor class vote, amendment mechanism                      |
| 8   | Dividend and Distribution Policy         | Standard | Preference order, participating vs. non-participating, cumulative vs. non-cumulative, policy changeability        |
| 9   | Deadlock Resolution                      | Standard | Definition of deadlock, escalation tiers, buy-sell mechanism, financial asymmetry risk, winding up                |
| 10  | Exit Provisions                          | Standard | IPO rights, registration rights, lock-up, trade sale drag, put/call, redemption, buyback, exit waterfall          |
| 11  | Transfer Restrictions and ROFR/ROFO      | Standard | ROFR mechanics, ROFO mechanics, lock-up periods, permitted transfers, change of control                           |
| 12  | Governing Law, Disputes, and Boilerplate | Standard | Jurisdiction, arbitration vs. litigation, India non-arbitrability risk, entire agreement, amendment               |

### Step 7: Missing Clause Detection

After analyzing clauses that are present, check for important clauses entirely absent from
the SHA. A missing clause can be as material as a defective one.

For each of the 12 clause categories:

- If entirely absent, flag it
- Classify the absence: GREEN (not needed for this deal structure), YELLOW (should be added),
  or RED (must be added)

**Common missing clause issues in SHAs:**

- No anti-dilution protection for a significant minority investor (RED)
- No drag-along in a VC-backed company (RED — clean exit impossible)
- No pre-emptive rights (YELLOW — minority will be diluted without consent)
- No reserved matters at shareholder level — only board-level (YELLOW)
- No information rights (RED — investor cannot monitor investment)
- No board representation for a significant investor (YELLOW)
- No deadlock mechanism in a 50/50 joint venture (RED)
- No exit provision for investors after 5+ years (RED — investor permanently locked in)
- No SEBI Regulation 31B reaffirmation mechanism (India listed only) (RED)
- Governing law clause absent (RED)
- No FEMA compliance undertaking (India with foreign investor) (RED)

**⟁ CLARIFY** — When the severity of a missing clause depends on business context:

- "This SHA has no deadlock resolution mechanism. Is this a 50/50 or closely-held structure
  where deadlock is a realistic risk? If so, this is a RED gap."
- "There are no information rights provisions. Will this investor have a board seat that
  provides alternative access to information? If not, this is a RED gap."

### Step 8: Classify and Flag Deviations

Classify each deviation using the three-tier system defined in **Deviation Severity
Classification** below. For each deviation:

- **GREEN**: Note for awareness.
- **YELLOW**: Generate specific redline language, fallback position, and estimate business
  impact of accepting vs. negotiating.
- **RED**: Explain the specific risk (citing legal basis where possible), provide market-standard
  alternative language, estimate exposure or governance risk, and recommend escalation path.

**⟁ CLARIFY** — For borderline classifications where reasonable minds could differ:

- **YELLOW vs. RED**: "The drag-along threshold is 60% — below the market range of 66.67%–75%
  but not catastrophically low. Should I treat this as YELLOW (negotiate) or RED (escalate)?
  It depends on your stake size and whether a 60% coalition of other investors exists today."
- **GREEN vs. YELLOW**: "The information rights frequency is semi-annual — below quarterly
  market standard but not absent. Is this acceptable given your board observer seat, or should
  we push for quarterly?"
- **Risk tolerance check**: If multiple borderline items trend majority-favorable, ask whether
  to apply a conservative or pragmatic classification threshold overall.

### Step 9: Generate Redlines

**⟁ CLARIFY** — Before generating redlines, confirm negotiation posture:

- **Relationship dynamic**: New investor negotiating standard terms, existing investor in
  a supplemental agreement, or a post-investment dispute driving the review?
- **Volume of redlines**: If there are many YELLOW items, ask: "I've found [N] items worth
  negotiating. Do you want redlines for all of them, or focus on the top [X] most material?"
  Too many redlines can overwhelm a negotiation and signal inexperience to the other side.
- **Non-cash tag-along consent, India FEMA compliance undertaking, SEBI Regulation 31B**:
  Confirm these jurisdiction-specific items are verified by local counsel before finalizing.

For each YELLOW and RED deviation, generate a redline using the **Redline Format** below.

### Step 10: Produce Minority Protection Scorecard

After clause analysis, produce a consolidated **Minority Protection Scorecard** assessing the
overall balance of power in this SHA. Score each dimension as Minority-Favored, Balanced,
or Majority-Favored, and derive an overall assessment.

| Dimension                                                               | Score                                            | Evidence from SHA |
| ----------------------------------------------------------------------- | ------------------------------------------------ | ----------------- |
| Economic Protections (anti-dilution, liquidation preference, dividends) | [Minority-Favored / Balanced / Majority-Favored] | [cite provisions] |
| Exit Control (drag threshold, tag-along, exit mechanisms)               | [M-F / B / M-F]                                  | [cite provisions] |
| Governance Rights (board seats, reserved matters, quorum)               | [M-F / B / M-F]                                  | [cite provisions] |
| Information and Transparency                                            | [M-F / B / M-F]                                  | [cite provisions] |
| Transfer Protections (ROFR, tag-along, pre-emption)                     | [M-F / B / M-F]                                  | [cite provisions] |
| Deadlock and Dispute Resolution                                         | [M-F / B / M-F]                                  | [cite provisions] |
| **Overall Balance**                                                     | **[Overall Assessment]**                         | **[summary]**     |

**Overall assessments:**

- **Investor-Balanced**: 4+ dimensions balanced or minority-favored; no RED items
- **Moderately Investor-Friendly**: Mix of balanced and minority-favored; no RED items
- **Founder-Balanced**: 4+ dimensions balanced or majority-favored; no RED items
- **Investor-Unfavorable**: 3+ dimensions majority-favored or any RED items on economic/exit

**⟁ CLARIFY** — Present the scorecard to the user and ask: "The overall balance is [assessment].
Is this consistent with what you expected given the deal context?"

### Step 11: Quality Verification (Silent Pre-Delivery)

Before delivering output, run all four quality frameworks silently:

1. **Citation Quality Gates** (5 gates — see below) — fail = revise before delivery
2. **Self-Interrogation** (3-pass review) — for every RED item
3. **Confidence Scoring** — assign a level to each material analysis point
4. **Glass Box Audit Trail** — complete the YAML template before delivering

---

## Deviation Severity Classification

### GREEN — Acceptable

The provision aligns with or is better than market-standard investor protection. Minor
variations that are commercially reasonable and do not materially increase governance or
financial risk.

**Examples:**

- Drag-along threshold at 75% (above the 66.67% minimum — better for minority)
- Broad-based weighted average anti-dilution with standard ESOP carve-out
- Quarterly financial reporting within 45 days (standard)
- Board representation with quorum requirement including investor director
- Reserved matters at both board and shareholder level with investor class vote

**Action**: Note for awareness. No negotiation needed.

### YELLOW — Negotiate

The provision falls outside the standard position but within a negotiable range. Common
in the market but not preferred. Requires attention and negotiation, but not escalation.

**Examples:**

- Drag-along threshold at 60%–65% (below market but not catastrophic for a small minority)
- Narrow-based weighted average anti-dilution (more aggressive than broad-based but not full ratchet)
- Semi-annual financial reporting (below quarterly standard but not absent)
- No oversubscription right on pre-emption (can negotiate to add)
- Single escalation tier before deadlock buy-sell (market standard is two tiers)
- Lock-up period of 180 days post-IPO (standard) but automatic extensions without consent (not standard)

**Action**: Generate specific redline language. Provide fallback position. Estimate business
impact of accepting vs. negotiating.

### RED — Escalate

The provision falls outside the acceptable range, poses material governance or financial
risk, or is likely unenforceable under the governing law. Requires senior counsel review,
outside counsel involvement, or investment committee sign-off.

**Examples:**

- Full ratchet anti-dilution (unacceptable at any stage; makes future fundraising impossible)
- Drag-along threshold at or below 50% (small coalition can force exit over majority objection)
- No drag-along price floor (majority can fire-sale to related party at any price)
- No information rights of any kind (investor cannot monitor investment)
- No board representation for a significant minority investor (no governance voice)
- Participating preferred with multiple liquidation preference (double-dips at investor's benefit)
- No anti-dilution protection at all (investor fully exposed to down-round dilution)
- Put option at guaranteed IRR for foreign investor in India (FEMA violation risk)
- Foreign arbitration clause only, in an India-seated SHA (NCLT non-arbitrability trap)
- Drag-along warranty obligations not capped for dragged minority shareholders
- Reserved matters waivable by majority without investor class consent
- Russian roulette deadlock mechanism between financially asymmetric parties (structurally unfair)

**Action**: Explain specific risk with legal basis. Provide market-standard alternative. Estimate
exposure. Recommend escalation path. Flag for specialist local counsel where jurisdiction-specific.

---

## Deep Clause Analysis — 12 Categories

### Category 1: Drag-Along Rights

**What to review:**

- **Threshold**: What percentage must approve before drag-along can be triggered?
  - GREEN: 66.67%–75% by value of all shares, or majority of common (as-converted) + majority
    of preferred (as-converted) — NVCA standard
  - YELLOW: 60%–66% — aggressive but negotiable
  - RED: 50% or below — small coalition can force exit; related to Moelis structural concerns
- **Same-consideration requirement**: Do all shareholders receive identical per-share price?
  - RED if absent — majority can negotiate side payments or superior consideration for itself
- **Minority warranty scope**: Are dragged minority shareholders limited to title/capacity/authority?
  - RED if not capped — minority has no information about the business being sold
- **Minority indemnification cap**: Is minority's indemnification liability capped at proceeds
  received?
  - RED if uncapped — minority can be liable for breaches it had no role in creating
- **Consideration type**: Is non-cash consideration addressed?
  - RED if non-cash permitted without minority consent — minority forced into unknown equity
- **Minimum price floor**: Is there a minimum price below which drag cannot be exercised?
  - RED if absent — fire-sale risk for distressed exits
- **Notice period**: Adequate notice for minority to seek legal advice (minimum 10 business days)?
  - YELLOW if inadequate
- **Pre-emption interplay**: Does SHA expressly address whether ROFR takes priority over drag?
  - YELLOW if absent — legal conflict risk
- **Good faith obligation**: Is there an express obligation to conduct a proper sale process?
  - YELLOW if absent — implicit in equity/statute, but express is stronger

[JURISDICTION-SPECIFIC]

- **Australia**: Confirm drag-along is in both SHA AND company constitution. SHA-only may
  not bind future shareholders. [VERIFY]
- **India**: Drag-along must comply with FEMA pricing norms for foreign investors. [VERIFY]
  Oppression petition at NCLT remains available to minority even if drag is technically exercised.
- **UK**: _O'Neill v Phillips_ principles — informal understandings about process can give
  rise to § 994 claims if drag exercise is oppressive. Good faith in sale process matters.
- **US**: Post-DGCL § 122(18) — governance provisions in stockholder agreements are valid;
  fiduciary duties remain applicable. _New Enterprise Associates v. Rich_ (2023) — covenant
  not to sue for fiduciary breach in drag-along context is enforceable if narrowly tailored.

---

### Category 2: Tag-Along Rights

**What to review:**

- **Trigger**: What sale by a shareholder triggers tag-along rights?
  - GREEN: Any transfer above a de minimis threshold by any holder
  - YELLOW: Only triggered by sale of 50%+ of a holder's shares (limits protection)
  - RED: Only triggered by transfer of 100% of shares (effectively no protection in partial sales)
- **Co-sell election mechanics**: Is the process clearly defined with adequate notice period?
  - YELLOW if exercise window is less than 10 business days
- **Procure-buyer obligation**: Must the selling majority procure that the buyer accepts tag shares?
  - RED if absent — tag-along becomes an empty right if buyer refuses minority shares
- **Consequence of non-procure**: If buyer refuses, can the sale proceed?
  - GREEN: Sale cannot proceed unless buyer accepts tag shares
  - RED: Sale proceeds without tag shares being accepted
- **Consideration parity**: Must tag-along shares receive identical per-share terms?
  - RED if absent — majority may negotiate better terms and leave minority with inferior deal
- **Carve-outs**: Standard carve-outs (intra-group, family, estate) present without overreach?
  - YELLOW if carve-outs are broad enough to regularly exempt actual commercial transfers

---

### Category 3: Anti-Dilution Protections

**What to review:**

- **Type**: Full ratchet / Narrow-based weighted average / Broad-based weighted average / None
  - GREEN: Broad-based weighted average (formula includes all fully diluted shares in denominator)
  - YELLOW: Narrow-based weighted average (smaller denominator — more aggressive but not extreme)
  - RED: Full ratchet (conversion price fully reset to down-round price regardless of quantum
    of new shares; severely punishes founders, deters future investment, essentially extinct
    in modern VC deals)
  - RED: No anti-dilution protection at all (investor fully exposed to down-round dilution)
- **Formula definition**: Is the weighted average formula precisely defined?
  - RED if formula is absent or ambiguous — disputes will arise on exercise
- **ESOP carve-out**: Is anti-dilution excluded for option pool expansions up to an approved cap?
  - RED if absent — every option grant triggers anti-dilution, blocking employee incentives
- **Conversion carve-out**: Are conversions of existing instruments excluded?
  - YELLOW if absent
- **Pay-to-play**: Does the SHA include a pay-to-play provision?
  - GREEN if present — requires investors to participate in down rounds to retain anti-dilution
    protection (balances investor protection with company support obligation)
  - Absent is acceptable but less balanced
- **Share structural adjustments**: Does the formula adjust proportionally for share splits,
  consolidations, and recapitalizations?
  - RED if absent — formula will miscalculate after structural share events
- **SEBI Regulation 31B (India listed)**: For listed companies, are anti-dilution provisions
  subject to 5-yearly shareholder renewal?
  - RED if non-compliant — rights may lapse post-IPO

[JURISDICTION-SPECIFIC]

- **India**: FEMA pricing norms constrain anti-dilution implementation for foreign investors.
  Promoter transfer of shares (rather than conversion price adjustment or new share issue)
  is the most FEMA-compliant mechanism. Full ratchet via price adjustment is essentially
  unavailable for foreign investors. [VERIFY]
- **US**: 60%+ of transactions use broad-based weighted average. 2025 market data shows
  cumulative dividends in 23% of deals (up from 4.7% in Q4 2021 — more investor-favorable).
- **UK**: BVCA standard follows broad-based weighted average approach. Ratchet provisions
  also used for return-based upside sharing in PE transactions (different from anti-dilution).
- **Australia**: No statutory form — same market practice as US/UK.

---

### Category 4: Pre-emptive Rights / Right of First Participation

**What to review:**

- **Scope**: What share issuances trigger the right?
  - GREEN: All new equity issuances (ordinary, preferred, convertible instruments)
  - YELLOW: Only ordinary share issuances (leaves investor exposed to new preferred issuances)
  - RED: No pre-emptive rights at all
- **Pro-rata basis**: Is the right calculated on fully diluted basis (including options/warrants)?
  - YELLOW if only issued shares — options pool could significantly dilute the right
- **Exercise window**: How long does the investor have to exercise?
  - GREEN: 15–20 business days minimum
  - RED: Less than 5 business days — investor cannot arrange funding in time
- **Oversubscription**: Can investors take up un-subscribed allocations?
  - YELLOW if absent — partial exercise leaves unexercised allocation available to founders
- **Standard carve-outs**: ESOP issuances, conversions of existing instruments, intra-group
  transfers, board-approved strategic issuances — all present?
  - YELLOW if ESOP expansion not carved out
  - GREEN if standard list present and not overreaching

[JURISDICTION-SPECIFIC]

- **UK**: Section 561 Companies Act 2006 provides statutory pre-emption on allotment of
  equity securities for cash — applies by default to ordinary shares, can be disapplied by
  special resolution (75%+). Review whether statutory default is preserved or overridden.
  Transfer pre-emption (not allotment) is not statutory — must be in SHA or articles. [VERIFY]
- **Australia**: Section 254D Corporations Act 2001 replaceable rule — proprietary companies
  must offer new shares of same class to existing holders pro-rata. Routinely displaced by
  bespoke constitution. [VERIFY]
- **India**: No statutory pre-emption on issuances for ordinary shares in private companies —
  purely contractual. Ensure SHA provisions are explicit and complete.
- **US**: No statutory pre-emption — purely contractual. NVCA structures as participation
  rights in the investor rights agreement (separate from the SHA).

---

### Category 5: Information and Inspection Rights

**What to review:**

- **Annual financials**: Audited accounts within 90–120 days of fiscal year end?
  - YELLOW if within 180 days (too long for monitoring)
  - RED if absent
- **Quarterly financials**: Unaudited management accounts within 30–45 days?
  - YELLOW if semi-annual only
  - RED if absent for a significant investor
- **Monthly financials**: For "major investors" above a threshold?
  - YELLOW if absent (though not universal for all investors)
- **Annual budget/business plan**: Delivered before start of fiscal year?
  - YELLOW if absent
- **Capitalization table**: On request or on any material change?
  - RED if absent — investor cannot monitor dilution
- **Inspection rights**: Access to books, records, and facilities during normal hours, on
  reasonable notice?
  - YELLOW if absent but board seat provides alternative access
  - RED if absent with no board seat
- **Material event notifications**: Litigation above threshold, regulatory investigation,
  senior executive departure, breach of SHA?
  - YELLOW if absent
- **Competitor exclusion**: Are information rights qualified to exclude competitors?
  - YELLOW if absent — confidentiality breach risk in competitive markets
- **Termination triggers**: When do information rights terminate?
  - RED if rights terminate on next funding round (before exit)
  - GREEN if rights terminate on IPO (registration statements then public)

---

### Category 6: Board Composition and Nomination Rights

**What to review:**

- **Investor board seat(s)**: Does investor have right to nominate at least 1 director?
  - RED if absent for a significant minority investor
- **Removal and replacement**: Can the investor remove and replace its nominated director?
  - RED if absent — investor director captured by management over time
- **Board quorum**: Does quorum require at least 1 investor-nominated director to be present?
  - RED if absent — management can hold board meetings and approve strategic decisions
    without investor participation
- **Reserved matters and affirmative vote**: Do reserved matters require investor director's
  affirmative vote (not just presence)?
  - YELLOW if quorum only without affirmative vote requirement
- **Observer rights**: Are there observer rights for sub-threshold investors?
  - YELLOW if absent but significant economic stake is held
- **Independent directors**: Are independent directors required for any decisions?
  - YELLOW if related-party transactions have no independent oversight
- **Board size**: Is the board size fixed or subject to investor consent to change?
  - RED if board size can be changed without investor consent — dilutes voting power
- **Meeting frequency**: Is there a minimum board meeting frequency?
  - YELLOW if board meeting frequency entirely at management discretion

[JURISDICTION-SPECIFIC]

- **India**: Companies Act 2013 restricts certain director appointments. Minimum 2 directors
  for private companies; 1/3 independent directors for listed companies; nominee directors
  of investment vehicles have particular SEBI disclosure requirements. [VERIFY]
- **US**: Post-DGCL § 122(18) (August 2024) — board nomination rights in stockholder
  agreements are explicitly authorized. Prior _Moelis_ (2024) concern that such provisions
  violated DGCL § 141(a) has been legislatively resolved. [VERIFY]

---

### Category 7: Reserved Matters / Protective Provisions

**What to review:**

**Board-level reserved matters** (require investor director's affirmative vote):

- Identify what decisions require board approval at this level
- GREEN if: budget variance threshold (15%–25%), individual expenditure threshold, new debt
  above cap, C-suite appointment/removal, related party transactions, material contracts above
  threshold, and litigation above threshold
- RED if: list is absent or covers constitutional changes only (everything material operational
  decision can be taken without investor)

**Shareholder-level reserved matters** (require investor class vote):

- GREEN if: new share class issuance, articles amendment, mergers/acquisitions above threshold,
  IPO decision, dividend declarations, winding up, equity incentive scheme creation/expansion,
  principal business change
- RED if: only constitutional changes covered; threshold set so high that ordinary business
  strategy is unconstrained

**Amendment mechanism**: Can the SHA or reserved matters list be amended?

- RED if amendable by majority vote alone — investor loses all protections on re-negotiation
- GREEN if reserved matters amendments require investor class consent

**⟁ CLARIFY** — For reserved matters review, the appropriate scope depends heavily on the
deal type. Ask: "Is this a VC deal (where operational reserved matters are less common) or
a PE/growth deal (where financial reserved matters with specific thresholds are standard)?"

---

### Category 8: Dividend and Distribution Policy

**What to review:**

- **Preference order**: Do preferred holders receive dividends before ordinary/common?
  - GREEN if preference present and clearly defined
  - RED if absent — no economic preference over common
- **Participating vs. non-participating preferred**:
  - GREEN: Non-participating preferred — investor receives preference OR converts to common
    to share in remaining proceeds
  - YELLOW: Participating preferred — investor receives preference AND shares in remaining
    proceeds (double-dip; acceptable in some market conditions)
  - RED: Participating preferred with 2x–3x multiple liquidation preference — investor
    receives multiple preference AND participates fully in remaining proceeds. In a $50M
    exit for a company that raised $30M at 2x preference, founders may receive nothing.
- **Cumulative vs. non-cumulative**:
  - Standard: Non-cumulative (if no dividend declared, nothing accrues)
  - YELLOW: Cumulative at 6%–8% per annum (investor-favorable; becoming more common in
    down-market conditions — 23% of US VC deals as of Q1 2024)
  - RED: Cumulative at 10%–12%+ per annum (creates compounding preference that quickly
    exceeds investment value in long-hold scenarios)
- **Anti-dividend stripping**: Are dividends to majority shareholders restricted unless paid
  proportionally to all?
  - RED if absent — majority can declare dividends to itself while starving investors

[JURISDICTION-SPECIFIC]

- **Australia**: Section 254T Corporations Act — dividends can only be declared if solvency
  test is met (assets exceed liabilities after payment). [VERIFY]
- **India**: Companies Act 2013 Section 123 — dividends must be declared from profits only;
  cannot impair paid-up capital. [VERIFY]

---

### Category 9: Deadlock Resolution Mechanisms

**What to review:**

- **Definition of "deadlock"**: Is deadlock precisely defined?
  - RED if absent or defined as "any dispute" — vague definition will be weaponized
  - GREEN if deadlock = failure to pass a reserved matter resolution at X consecutive meetings
    with specific notice requirements
- **Tier 1 — Escalation to senior management**: 15–20 business days good-faith negotiation?
  - YELLOW if absent (important first step; cheap and preserves relationship)
- **Tier 2 — Mediation**: Independent mediator, 30-day window, confidential?
  - YELLOW if absent (cost-effective before expensive buy-sell)
- **Tier 3 — Buy-sell mechanism**: Russian roulette or Texas shootout?
  - **Russian roulette**: Party A sets a price; Party B either buys A's shares at that price
    OR sells B's shares to A at the same price. Encourages fair pricing because initiating
    party risks being the seller.
    - YELLOW if both parties are approximately equal financial strength (fair mechanism)
    - RED if financially asymmetric — wealthier party is systematically advantaged (can always
      buy at any price)
  - **Texas shootout**: Both parties submit sealed bids; highest bidder must purchase.
    - YELLOW if parties are approximately equal financial strength
    - RED if financially asymmetric — entirely favors the richer party
  - Consider whether expert determination (independent valuation-based buyout) is more
    appropriate for financially asymmetric parties
- **Payment terms**: Clearly defined timeline and mechanics for buy-sell completion?
  - YELLOW if absent — disputes about payment timing will delay resolution
- **Default consequence**: What happens if the obligated party fails to buy/sell on time?
  - YELLOW if not addressed

---

### Category 10: Exit Provisions

**What to review:**

- **IPO right**: Does investor have right to demand IPO preparation after a defined period?
  - YELLOW if absent for VC investors in a company operating 5+ years
- **Registration rights**: Are demand registration rights and piggyback registration rights
  included?
  - RED if absent (US-listed target) — investor cannot participate in public market liquidity
  - YELLOW if absent for non-US markets
- **Lock-up**: Is lock-up period post-IPO capped?
  - GREEN: 90–180 days standard; automatic extension requires investor consent
  - RED: Automatic extension without investor consent or lock-up exceeding 180 days without
    compensation
- **Trade sale / drag-along**: See Category 1 (Drag-Along Rights)
- **Put option**: Investor right to require company/founders to buy shares after trigger event?
  - YELLOW if absent for investors who lack alternative exit mechanisms
  - GREEN if present with FMV valuation mechanism
  - RED (India) if put option priced at guaranteed IRR rather than FMV — FEMA violation risk
- **Buyback / redemption**: Company right to repurchase at original price + preference?
  - GREEN: Available as exit mechanism with solvency test and distributable reserves test
  - RED: Redemption at company's sole discretion (investor's exit depends on company's choice)
- **Exit waterfall clarity**: Is the order of distribution on exit clearly defined?
  - RED if absent — disputes about liquidation preference, anti-dilution adjustments, and
    common sharing are litigated after the fact

[JURISDICTION-SPECIFIC]

- **India**: Put option at guaranteed fixed return violates FEMA pricing norms for foreign
  investors. Must be priced at FMV at exercise date. [VERIFY]
- **UK**: Registration rights are less common for AIM or LSE listings than for US listings;
  lock-up periods negotiated with NOMAD/underwriters. [VERIFY]
- **Australia**: Buyback requires compliance with Corporations Act 2001 Part 2J.1 (solvency,
  10% pro-rata limit on buy-back volume in a 12-month period for selective buy-backs). [VERIFY]

---

### Category 11: Transfer Restrictions and ROFR/ROFO

**What to review:**

- **Lock-up period**: Are founder and investor shares subject to lock-up?
  - GREEN: Founder lock-up of 12–48 months depending on stage; investor lock-up absent or
    short
  - YELLOW: No founder lock-up — founders can exit before investors
- **Right of First Refusal (ROFR)**: Does the company (then investors) have ROFR on share
  transfers?
  - GREEN: Two-stage ROFR — company first, then pro-rata to investors
  - YELLOW: No investor ROFR — company can buy but investors cannot step in if company declines
  - RED: No ROFR at all — third parties can acquire without investor consent
- **Right of First Offer (ROFO)**: Before approaching third parties, must seller first offer
  to existing holders?
  - YELLOW if absent (ROFR is more common; ROFO is an alternative mechanism)
- **Permitted transfers**: Standard carve-outs (intra-group, family, estate, trust for estate
  planning)?
  - YELLOW if carve-outs so broad that effective transfers occur without triggering ROFR
- **Change of control**: Does a change of control at the shareholder level trigger ROFR?
  - YELLOW if absent in PE/institutional investor context — indirect transfer possible without
    triggering ROFR

---

### Category 12: Governing Law, Disputes, and Boilerplate

**What to review:**

- **Governing law clause**: Present and clearly identified?
  - RED if absent
- **Dispute resolution**: Litigation vs. arbitration?
  - Note which forum and whether it is appropriate for the deal
  - RED (India): Foreign arbitration only, without acknowledgment of NCLT non-arbitrability
    for oppression claims — creates a legal trap. All India-seated SHAs should include:
    "Notwithstanding the foregoing, any party retains the right to bring an oppression or
    mismanagement petition before the NCLT under Sections 241–242 of the Companies Act 2013."
- **Entire agreement clause**: Present?
  - YELLOW if absent — parol evidence risk
- **Amendment mechanism**: Does SHA amendment require investor class consent?
  - RED if amendable by majority vote of shareholders — minority protections can be stripped
- **Severability**: Present?
  - YELLOW if absent — one invalid provision could void the whole SHA
- **Notices**: Addresses and procedures defined?
  - YELLOW if absent or addresses outdated
- **Counterparts and electronic execution**: Permitted?
  - YELLOW if electronic execution not addressed (practical execution risk)

---

## Prioritization Framework

### Tier 1 — Must-Haves (Deal Conditions or RED Items)

Issues where the reviewing party cannot sign or close without resolution. Raise these first
and hold firm:

- No anti-dilution protection or full ratchet anti-dilution
- No drag-along, or drag-along threshold at or below 50%
- No drag-along price floor (fire-sale risk)
- Drag-along minority warranty exposure uncapped
- No information rights of any kind
- No board representation for a significant investor
- No investor class consent required for SHA amendments
- Put option at guaranteed IRR for India-based foreign investor (FEMA violation)
- Foreign arbitration clause only in India-seated SHA (NCLT non-arbitrability trap)
- No exit mechanism of any kind (investor permanently locked in)
- No pre-emptive rights (investor fully exposed to dilution at any price)
- Participating preferred with 2x+ multiple liquidation preference

### Tier 2 — Strong Preferences (Material Negotiation Points)

Issues that materially affect risk profile but are negotiable:

- Drag-along threshold in the 55%–65% range (below 66.67% market standard)
- Narrow-based weighted average anti-dilution (more aggressive than broad-based)
- Semi-annual information rights (below quarterly standard)
- No oversubscription right on pre-emption
- No quorum requirement for investor director at board meetings
- Reserved matters at board level only (no shareholder level)
- Single escalation tier before buy-sell deadlock (no mediation)
- No pay-to-play provision (investor gets anti-dilution without obligation to invest)
- Cumulative dividends at 6%–8% per annum (investor-favorable drift)
- Lock-up extensions without investor consent

### Tier 3 — Preferred Positions (Concession Candidates)

Issues that improve position but can be conceded strategically:

- Governing law preference (if alternative is acceptable)
- Notice periods and administrative mechanics
- Observer rights scope
- Exercise window extension (15 to 20 business days)
- Specific format of financial reporting
- Carve-out scope refinements

**Strategy**: Lead with Tier 1 items. Trade Tier 3 concessions to secure Tier 2 wins.
Never concede on Tier 1 without investment committee or senior partner sign-off.

---

## Quality Frameworks

### Citation Quality Gates

Run these 5 gates silently before delivering output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                              | Fail Action                                              |
| -------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established principle                  | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction                       | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments or repeal                                            | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the SHA's governing law; no assumptions from other jurisdictions leaking in | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden                                                         | Add confidence qualifier                                 |

### Self-Interrogation for RED Items

For any item classified RED, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the risk assessment follow logically from the cited statute or principle?
- Would a court or regulator in this jurisdiction actually reach this conclusion on these facts?
- Is there a counter-argument that the counterparty's counsel will make?

**Pass 2 — Completeness**:

- Have all relevant statutes, regulations, and market standards been considered?
- Does this provision interact with other SHA clauses in ways not yet analyzed?
- Are there deal mechanics (enhanced escrow, specific indemnity, alternative clause structure)
  that could address this issue and convert RED to YELLOW?

**Pass 3 — Challenge**:

- What is the strongest argument that this provision IS acceptable?
- Under what deal circumstances (stage, stake size, industry, investor relationship) might
  reasonable counsel accept this risk?
- Is the RED classification proportionate, or is this actually a YELLOW with the right redline?
- Does the RED classification reflect deal-specific risk or over-cautious general advice?

If any pass reveals a weakness, revise. Mark the audit trail:
`self_interrogation: PASS` or `self_interrogation: REVISED — [summary of revision]`.

### Confidence Scoring

| Level        | Range     | Meaning                                          | Action                                                   |
| ------------ | --------- | ------------------------------------------------ | -------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, clear statute, no ambiguity         | State with confidence                                    |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions | State with brief caveat                                  |
| **Probable** | 0.60–0.79 | Good arguments but reasonable minds could differ | State with explicit reasoning and contra-indicators      |
| **Possible** | 0.40–0.59 | Genuinely uncertain, competing authorities       | Flag for counsel review with both sides of the argument  |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                          | Do not assert; flag as "[UNCERTAIN — counsel to advise]" |

**Calibration note**: Given the governance and economic consequences of SHA terms, err
toward flagging uncertainty rather than concealing it. A "Probable" finding presented as
"Definite" can cause an investor to accept terms that later prove unenforceable.

---

## Anti-Patterns

What NOT to do when reviewing shareholders agreements:

1. **Single-pass analysis without cross-referencing**: SHA clauses form an interconnected
   system. A drag-along at 51% combined with a participating preferred at 2x combined with
   no price floor amounts to total majority control of economics and exit. Analyze as a
   system, not as isolated provisions.

2. **Full ratchet anti-dilution cited as "market standard" for any deal**: Full ratchet is
   essentially extinct in modern VC. Never describe full ratchet as acceptable market practice.
   It severely punishes founders, deters future investors, and makes the company almost impossible
   to fund in a down market. Always flag as RED regardless of investor pressure.

3. **Applying US concepts to India without FEMA analysis**: Put options at guaranteed returns,
   conversion price adjustments, and equity swap mechanisms that are routine in US deals may
   violate FEMA pricing norms for foreign investors in India. Always apply FEMA overlay for
   any India-seated SHA with foreign investors before completing anti-dilution and exit analysis.

4. **Missing the NCLT non-arbitrability trap in India**: Including only a foreign arbitration
   clause in an India-seated SHA does not prevent a minority shareholder from filing an
   oppression petition at NCLT. _Anupam Mittal v. People Interactive_ (Bombay HC 2023) held
   oppression disputes are non-arbitrable. All India SHAs should acknowledge NCLT concurrent
   jurisdiction.

5. **Australian SHA without matching constitutional provisions**: In Australia, a SHA-only
   drag-along does not bind future shareholders who acquire shares without notice. Both the
   SHA and the company's constitution must contain drag-along provisions for full enforceability.
   Reviewing only the SHA and not the constitution is an incomplete analysis.

6. **Treating participating preferred as equivalent to non-participating preferred**: The
   economics are fundamentally different. A 1x participating preferred at a $50M exit for
   a company that raised $10M may still leave founders with 80% of proceeds. A 3x
   participating preferred at the same exit may leave founders with nothing. Always quantify
   the liquidation waterfall with actual numbers.

7. **Ignoring the reserved matters scope in context**: A reserved matters list covering
   only constitutional changes is useless for an investor in an operationally active company
   making strategic decisions. A reserved matters list covering every expenditure above $5,000
   in a growth-stage company creates operational paralysis. The scope must be calibrated to
   the deal stage and investment size.

8. **Russian roulette between financially asymmetric parties**: Russian roulette deadlock
   mechanisms only operate fairly when parties can each afford to buy the other out. A VC
   fund deploying from a $500M fund is systematically advantaged against a founder with
   limited personal liquidity. Flag this structural unfairness and recommend expert
   determination or mediation-only deadlock for asymmetric situations.

9. **Drag-along warranty obligations not analyzed for minority**: Minority shareholders
   dragged into a sale who did not negotiate the SPA and have no information about the
   business should not give representations beyond title and capacity. Uncapped warranty
   obligations for dragged minorities are a RED flag that is easy to miss in clause-by-clause
   analysis.

10. **Anti-dilution that applies to ESOP expansions**: Anti-dilution provisions that trigger
    on stock option plan top-ups create a compounding problem: every employee equity grant
    triggers investor anti-dilution adjustments, diluting founders further, which requires
    more ESOP grants, which triggers more anti-dilution. Always verify that ESOP pool
    expansions (up to an approved cap) are carved out.

11. **Assuming "pro-rata" is clearly defined**: Pre-emptive rights and anti-dilution
    adjustments that reference "pro-rata" without defining the basis (issued shares? fully
    diluted? which classes?) create disputes. Always check that "pro-rata" is precisely
    defined and applies on the expected basis.

12. **No deadlock trigger definition**: SHAs that reference "deadlock" without defining it
    (how many failed votes, over what period, on what matters) create disputes about whether
    a deadlock has even occurred before the resolution mechanism can be triggered.
    Vague deadlock definitions will be exploited.

13. **Information rights that terminate on next funding round**: Early-stage SHAs sometimes
    provide that information rights terminate on the next qualifying financing round. This
    means seed investors lose information rights before the company's most significant value-
    creation period. Always check information rights termination triggers.

14. **Dividend policy omitted entirely**: Absent a dividend policy, the board has unfettered
    discretion to declare or withhold dividends. Founders-as-directors can pay themselves
    excessive salaries (not dividends), creating a pattern of economic exclusion that constitutes
    oppression in some jurisdictions. A dividend policy provision — even a simple one — is
    better than none.

15. **SEBI Regulation 31B non-compliance (India listed companies)**: Pre-IPO SHA rights
    (anti-dilution, nomination rights, veto rights, information rights) that are not
    reaffirmed every 5 years by special resolution of listed company shareholders violate
    SEBI LODR Regulation 31B (effective June 2023). These rights can lapse post-IPO without
    the investor realizing. Flag this in any India-seated SHA involving a potential future
    IPO.

16. **Minority discount in SHA buyout provisions**: Many SHA buyout provisions (ROFR pricing,
    deadlock buy-sell, exit put options) are silent on minority discounts. Some jurisdictions
    apply minority discounts by default in share valuations. _Re Blue Index Ltd_ [2014]
    established that minority discounts are generally not applied in UK § 994 buyouts; check
    the SHA expressly excludes minority discounts in all valuation contexts.

17. **Reviewing SHA in isolation from Articles/Constitution**: In the UK, India, and Australia,
    the company's constitution (articles of association) interacts directly with the SHA. A
    clause in the SHA may be overridden by the articles, and vice versa. Always identify the
    "order of precedence" clause and assess whether SHA rights are adequately protected in
    the articles.

18. **Confidence without quantification**: Saying "the liquidation preference is problematic"
    is insufficient. Always quantify: "At a $30M exit for a company with $10M raised at 2x
    participating preferred: investor receives $20M preference + pro-rata share of remaining
    $10M = ~$23M. Founders receive ~$7M (23%). This is an unfavorable distribution structure
    for founders."

19. **Non-cash consideration in drag-along not addressed**: If the drag-along provision
    does not expressly restrict non-cash consideration (shares in acquirer, deferred consideration,
    earnouts), minority shareholders can be dragged into receiving unmarketable securities
    in an unknown company. This gap is common and consistently overlooked.

20. **Assuming instead of asking on side**: Silently assuming the user is the investor (minority)
    when the user may be the founder (majority) or vice versa changes every classification.
    A drag-along threshold of 51% is protective if you're the majority; dangerous if you're
    a 15% investor. Always confirm the side before completing any analysis.

---

## Writing Standards

Apply plain-language discipline to all shareholders agreement review output:

**For redline rationales** (appropriate for sharing with counterparty's counsel):

- Plain language. No jargon or filler.
- Active voice: "This clause exposes the investor to unlimited warranty liability" not
  "Unlimited warranty liability may be created by this clause."
- Short sentences. One point per sentence.
- Name the section: cite the specific SHA section for every finding.
- Specific, not vague: "Negotiate: drag-along threshold from 51% to 66.67%" not "consider the
  drag-along threshold."
- Quantify where possible: "This leaves investor exposed to full ratchet anti-dilution triggering
  a 40% additional dilution to founders in a Series B down round."

**For internal analysis**:

- Same plain-language standards apply
- May include more technical legal analysis and jurisdiction-specific citations
- Confidence qualifiers where appropriate
- Glass Box audit trail appended

**Quality gates before delivery:**

1. Is the overall assessment (Minority Protection Scorecard) stated at the top?
2. Is every RED item supported by a specific SHA section reference?
3. Does the Structural Overview table reflect the clause-by-clause analysis?
4. Can a non-lawyer deal team member understand the executive summary?
5. Are legal claims backed by authority (or explicitly flagged [VERIFY])?
6. Are jurisdiction-specific items flagged appropriately and not applied universally?
7. Is the Glass Box audit trail complete?

---

## External Tool Integration

This skill integrates with **legalcode-mcp** for jurisdiction-specific legal research on SHA
provisions.

**With legalcode-mcp connected (preferred):**

- Search for jurisdiction-specific statutes governing minority protection, pre-emption, and
  anti-dilution for the SHA's governing law
- Verify recent legislative changes: DGCL § 122(18) (August 2024), SEBI Regulation 31B
  (June 2023), FEMA Fourth Amendment Rules (August 2024)
- Search for key case law: _O'Neill v Phillips_, _Anupam Mittal v. People Interactive_,
  _Wayde v NSW Rugby League Ltd_, _New Enterprise Associates v. Rich_
- Save verified results to `/tmp/legalcode-sha-review-authority.md`
- Mark all legalcode-mcp citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark every statutory and case law reference with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed using the jurisdiction framework in this skill as the primary legal reference
- Recommend that the user's local counsel verify all jurisdiction-specific references before
  relying on the analysis

---

## Glass Box Audit Trail

Every SHA review must complete this YAML template before delivery. Include it in the output.

```yaml
glass_box:
  skill_name: "legalcode-shareholders-agreement-review"
  document: "[SHA title, date, version — e.g., 'Shareholders Agreement dated [date] between...']"
  document_type: "[SHA / Voting Agreement / Investor Rights Agreement / SHA Bundle]"
  user_side: "[Minority investor / Majority investor / Founder / Company / Advisor / Neutral]"
  company_stage: "[Seed / Series A / Series B+ / PE / JV / Pre-IPO]"
  deal_context: "[Brief description: investment amount, stake %, other key parties]"
  governing_law: "[Jurisdiction identified from the SHA]"
  dispute_resolution: "[Litigation — [court] / Arbitration — [rules, seat]]"
  india_nclt_acknowledged: "[Yes / No / N/A — only relevant for India-governed SHAs]"
  playbook_used: "[Investment playbook name / General market standards]"
  review_basis: "[Organizational investment playbook / General market standards]"

  # STRUCTURAL OVERVIEW
  anti_dilution_type: "[Full ratchet / Narrow-based WA / Broad-based WA / None]"
  drag_along_threshold: "[% or 'Not present']"
  liquidation_preference: "[1x non-participating / 1x participating / Multiple / None]"
  board_composition: "[Investor seat: Yes/No | Quorum req: Yes/No | Observer: Yes/No]"
  reserved_matters: "[Board only / Shareholder only / Both / None]"
  deadlock_mechanism: "[Multi-tier / Buy-sell only / None]"

  # ANALYSIS METRICS
  clauses_reviewed: "[count out of 12 categories]"
  green_count: "[count]"
  yellow_count: "[count]"
  red_count: "[count]"
  missing_clauses: "[count] — [list critical missing]"

  # QUALITY
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-sha-review-authority.md or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED (legalcode-mcp) or UNVERIFIED [VERIFY]]"
  case_law_consulted:
    - "[Case — VERIFIED (legalcode-mcp) or UNVERIFIED [VERIFY]]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation:
    red_items_reviewed: "[count]"
    result: "PASS / REVISED — [summary of revisions if any]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  minority_protection_score: "[Investor-Balanced / Moderately Investor-Friendly / Founder-Balanced / Investor-Unfavorable]"
  limitations:
    - "[Related articles/constitution not reviewed]"
    - "[Cap table not provided — ownership percentages assumed from SHA]"
    - "[Any other scope limitations or assumptions]"
  reviewer: "AI-assisted — requires review by qualified corporate/M&A counsel in the governing law jurisdiction"
```

---

## Output Format Template

```markdown
## Shareholders Agreement Review

**Document**: [SHA title, date, parties]
**Your Side**: [Minority investor / Founder / etc.]
**Company Stage**: [Seed / Series A / PE / etc.]
**Governing Law**: [Jurisdiction]
**Dispute Resolution**: [Forum]
**Review Basis**: [Playbook / General market standards]
**Date of Review**: [date]

---

## Overall Assessment

**Minority Protection Score**: [Investor-Balanced / Moderately Investor-Friendly / Founder-Balanced / Investor-Unfavorable]
**Confidence**: [Level and rationale]

[2–3 sentence narrative of overall governance balance and key issues]

---

## Structural Overview

| Parameter              | SHA Provision | Market Standard              | Assessment         |
| ---------------------- | ------------- | ---------------------------- | ------------------ |
| Anti-dilution type     | [agreed term] | Broad-based weighted average | [GREEN/YELLOW/RED] |
| Drag-along threshold   | [agreed term] | 66.67%–75%                   | [GREEN/YELLOW/RED] |
| Liquidation preference | [agreed term] | 1x non-participating         | [GREEN/YELLOW/RED] |
| Board composition      | [agreed term] | Investor seat + quorum req.  | [GREEN/YELLOW/RED] |
| Reserved matters       | [agreed term] | Board + shareholder levels   | [GREEN/YELLOW/RED] |
| Deadlock mechanism     | [agreed term] | Multi-tier + mediation       | [GREEN/YELLOW/RED] |
| Information rights     | [agreed term] | Quarterly + annual audit     | [GREEN/YELLOW/RED] |
| Pre-emption rights     | [agreed term] | Pro-rata + oversubscription  | [GREEN/YELLOW/RED] |

---

## Key Findings

[Top 3–5 RED or YELLOW items with severity flags, in priority order]

---

## Clause-by-Clause Analysis

### 1. Drag-Along Rights — [GREEN / YELLOW / RED] | Confidence: [level]

**SHA says**: [summary of provision and section reference]
**Market standard**: [what this clause typically provides]
**Deviation**: [specific gap or problem]
**Business impact**: [practical consequence]

**Proposed redline** (if YELLOW or RED):

> [Specific proposed language]

**Fallback position**:

> [Minimum acceptable position]

**Legal basis**: [Applicable statute, case, or market standard — or [VERIFY] if not confirmed]
**Priority**: [Tier 1 / Tier 2 / Tier 3]

[Repeat for all 12 categories]

---

## Missing Clauses

| Missing Clause | Classification | Rationale                     |
| -------------- | -------------- | ----------------------------- |
| [Clause]       | [YELLOW/RED]   | [Why it matters in this deal] |

---

## Minority Protection Scorecard

| Dimension                       | Score                                            | Evidence          |
| ------------------------------- | ------------------------------------------------ | ----------------- |
| Economic Protections            | [Minority-Favored / Balanced / Majority-Favored] | [cite provisions] |
| Exit Control                    | [M-F / B / M-F]                                  | [cite provisions] |
| Governance Rights               | [M-F / B / M-F]                                  | [cite provisions] |
| Information and Transparency    | [M-F / B / M-F]                                  | [cite provisions] |
| Transfer Protections            | [M-F / B / M-F]                                  | [cite provisions] |
| Deadlock and Dispute Resolution | [M-F / B / M-F]                                  | [cite provisions] |
| **Overall Balance**             | **[Overall Assessment]**                         | **[summary]**     |

---

## Negotiation Strategy

**Tier 1 (Must-Haves)**: [List with brief rationale for each]

**Tier 2 (Strong Preferences)**: [List with brief rationale]

**Tier 3 (Concession Candidates)**: [List — can trade for Tier 1/2 wins]

**Recommended approach**: [Sequencing, tone, and strategic trades]

---

## Jurisdiction-Specific Actions

[List of jurisdiction-specific items requiring local counsel verification, organized by jurisdiction]

- **[Jurisdiction]**: [Specific action or verification required]

---

## Next Steps

1. [Specific action with owner and deadline]
2. [Specific action — e.g., engage India counsel to verify FEMA compliance of put option]
3. [Specific action — e.g., review company constitution/articles for drag-along alignment]

---

## Glass Box Audit Trail

[YAML block from template above]
```

---

## Provenance

Created by Legalcode (2026-03-01). Original synthesis — 2-agent research pipeline combining
structural pattern extraction from `legalcode-contract-review` and `legalcode-purchase-agreement-review`
reference standards with deep legal research across US (DGCL/NVCA), UK (CA 2006/BVCA), India
(Companies Act 2013/FEMA/SEBI), and Australia (Corporations Act 2001). Key legal developments
incorporated: DGCL § 122(18) post-_Moelis_ legislative fix (August 2024), _Anupam Mittal v.
People Interactive_ NCLT non-arbitrability holding (Bombay HC September 2023), SEBI Regulation
31B special rights renewal obligation (effective June 2023), FEMA Fourth Amendment Rules 2024.
Market data: NVCA October 2025 model documents; Q1 2024 US VC deal term trends.

Glass box audit trail for skill creation:

```yaml
glass_box:
  skill_name: "legalcode-shareholders-agreement-review"
  mode: "Created from scratch (Mode A)"
  topic: "Shareholders agreement clause-by-clause review"
  jurisdiction: "US/UK/IN/AU with [JURISDICTION-SPECIFIC] markers"
  source_skills_analyzed: 2
  enhancement_type: "Create"
  legalcode_mcp: "Not connected"
  research_reference_file: "Not created (web research used)"
  quality_score: "38/40"
  completeness: "18/18 elements"
  citations_verified: "0 VERIFIED / All marked [VERIFY]"
  confidence:
    "HIGH — legal frameworks drawn from primary law review via web research; all statutory
    references marked [VERIFY] for counsel confirmation"
  limitations:
    - "legalcode-mcp not connected — all statutory and case law references carry [VERIFY] markers"
    - "Market data (NVCA, BVCA standards) is current as of October 2025 / Q1 2024"
    - "Jurisdiction coverage: US/UK/IN/AU; other jurisdictions use [JURISDICTION-SPECIFIC] markers"
  reviewer: "AI-assisted — requires review by qualified corporate/M&A counsel in the governing law jurisdiction"
```
