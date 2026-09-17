---
name: legalcode-partnership-agreement-review
description: Review partnership agreements — general partnerships (GP), limited partnerships (LP), and
  limited liability partnerships (LLP) — covering capital contributions, profit/loss allocation and distribution
  waterfalls, management authority and reserved matters, partner fiduciary duties, non-compete and non-solicitation
  obligations, admission and withdrawal of partners, dissolution triggers and winding-up procedures, and
  tax allocation mechanics. Use when reviewing or negotiating any partnership agreement, joint venture
  structured as a partnership, fund limited partnership agreement (LPA), LLP members' agreement, family
  limited partnership (FLP), or professional partnership deed.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review partnership agreements — general partnerships (GP), limited partnerships (LP), and limited liability partnerships (LLP) — covering capital contributions, profit/loss allocation and distribution waterfalls, management authority and reserved matters, partner fiduciary duties, non-compete and non-solicitation obligations, admission and withdrawal of partners, dissolution triggers and winding-up procedures, and tax allocation mechanics. Applies RUPA 1997/2013, ULPA 2001, and Delaware DRULPA for US analysis; Partnership Act 1890, Limited Partnership Act 1907, and LLP Act 2000 for UK analysis; and state-based Partnership Acts plus ITAA 1936 Division 5/5A for Australian analysis. Use when reviewing or negotiating any partnership agreement, joint venture structured as a partnership, fund limited partnership agreement (LPA), LLP members' agreement, family limited partnership (FLP), or professional partnership deed. Covers UK/US/AU with jurisdiction-agnostic markers for other common-law and civil-law systems. Identifies GREEN (acceptable), YELLOW (negotiate), RED (escalate), and STRUCTURAL (requires restructuring advice) findings. Produces confidence-scored analysis with redlines, negotiation priorities, and a Glass Box audit trail.


# Legalcode Partnership Agreement Review

> **Disclaimer**: This skill provides a framework for AI-assisted partnership agreement
> review. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional licensed in the relevant jurisdiction before use. Laws
> change frequently — verify current applicability before relying on any provision
> described here. Statutory and case law references cited from research carry hallucination
> risk — verify against authoritative sources before relying on them. Tax analysis is
> indicative only and must be verified by a qualified tax adviser.

## Purpose and Scope

This skill reviews partnership agreements — general partnerships (GP), limited partnerships
(LP), and limited liability partnerships (LLP) — against market-standard positions and
applicable statutory frameworks. It identifies deviations, classifies their severity,
generates actionable redlines, and produces a confidence-scored, auditable analysis.

**Covers:**

- Clause-by-clause analysis of any partnership agreement, LPA, members' agreement, or
  partnership deed
- All partnership structures: GP, LP, LLP, PFLP (UK), DRULPA (Delaware), corporate LP
  (Australia)
- Deviation classification (GREEN / YELLOW / RED / STRUCTURAL)
- Redline generation with fallback positions
- Missing clause detection
- Tax allocation mechanics review (US §704(b), targeted allocations, §754)
- Jurisdiction-specific statutory compliance checks
- Quality-verified output with Glass Box audit trail

**Does not:**

- Draft new partnership agreements from scratch (see drafting-specific skills)
- Provide legal or tax advice, or replace qualified counsel or tax advisers
- Cover partnership structures in civil-law systems in depth (markers provided where relevant)
- Apply exclusively to one jurisdiction — jurisdiction-agnostic with [JURISDICTION-SPECIFIC]
  markers for UK/US/AU variations and guidance on other systems

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The agreement's own governing law clause determines
which statutory framework applies. The review identifies the governing law early and adapts
the analysis accordingly.

**Primary Jurisdictions Supported:**

| Jurisdiction             | Key Statutes                                                                        | Partnership Types              |
| ------------------------ | ----------------------------------------------------------------------------------- | ------------------------------ |
| **US (Federal/RUPA)**    | RUPA 1997 (2013 amendments), ULPA 2001 [VERIFY adoption by state]                   | GP, LP, LLP, FLP               |
| **US (Delaware)**        | Delaware DRULPA (6 Del. C. §§ 17-101 et seq.), DRUPA                                | Delaware LP (most US fund LPs) |
| **UK (England & Wales)** | Partnership Act 1890, LPA 1907, LLP Act 2000/Regs 2001, PFLP Order 2017             | GP, LP, PFLP, LLP              |
| **Australia**            | Partnership Acts (state-based, e.g., Partnership Act 1958 Vic); ITAA 1936 Div. 5/5A | GP, LP (ordinary/corporate)    |

[JURISDICTION-SPECIFIC] When localizing for other jurisdictions, research and apply:

- The jurisdiction's default partnership statute and default rules for profit sharing,
  dissolution, and mutual agency
- Whether the "entity theory" (separate legal personality) applies
- Corporate limited partnership vs. pass-through tax treatment
- Mandatory expulsion and dissolution provisions
- Fiduciary duty codification vs. equitable obligations
- Anti-money laundering and beneficial ownership registration requirements

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- Partnership structure type is ambiguous (GP vs. LP vs. LLP)
- Multiple valid approaches exist and the user's preference matters
- Ambiguity in the agreement creates a fork that only the user can resolve
- Tax treatment choices affect the review direction (US §754, AU Division 5A)
- Risk tolerance or commercial context is needed to classify severity correctly

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

Accept the partnership agreement in any of these formats:

- **File**: PDF, DOCX, or other document format
- **URL**: Link to an agreement in a document system
- **Pasted text**: Agreement text pasted directly into the conversation

If no agreement is provided, prompt the user to supply one.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask the user:

1. **Partnership type**: What structure does this agreement govern?
   - Options: General Partnership (GP), Limited Partnership (LP/LPA), Limited Liability
     Partnership (LLP/Members' Agreement), Private Fund Limited Partnership (PFLP),
     Family Limited Partnership (FLP), Professional Partnership (solicitors/accountants/
     medics), Other/Unknown
   - _Why this matters_: The applicable statute, default rules, and key risk areas differ
     fundamentally across structure types. An LP analysis focuses on GP authority and LP
     limited liability protection; an LLP analysis focuses on the salaried members rules;
     a professional partnership analysis focuses on fiduciary duties and restraint of trade.

2. **Which side are you on?**
   - Options: General Partner/Managing Partner, Limited Partner/Minority Partner,
     Incoming/Prospective Partner, Advisor to the partnership entity, Lender/secured
     creditor assessing the agreement
   - _Why this matters_: What protects a GP (broad management authority, limited partner
     consent requirements) harms a limited partner and vice versa.

3. **Jurisdiction**: What law governs this agreement?
   - Options: US — Delaware, US — [specify state], UK — England & Wales, UK — Scotland,
     Australia — [specify state], Other [specify]
   - _Why this matters_: Determines which default statutory rules apply, which mandatory
     provisions cannot be contracted out of, and which tax analysis framework to apply.

4. **Purpose/context**: What type of transaction or entity is this?
   - Options: Private equity/venture fund LP, Real estate fund LP, Professional services
     partnership, Operating joint venture, Family wealth vehicle (FLP), Investment LLP,
     Management buyout vehicle, General commercial partnership, Other
   - _Why this matters_: Fund LPs have market-standard waterfall mechanics (e.g., European
     vs. American waterfall), professional partnerships have regulatory constraints
     (SRA Handbook for UK solicitors), and family limited partnerships have estate-planning
     specific concerns.

5. **Focus areas**: Any specific concerns?
   - Options: Capital contributions / funding obligations, Profit/loss allocation and
     distribution waterfall, Management authority and voting rights, Fiduciary duties,
     Non-compete and restrictive covenants, Partner exit / withdrawal / buyout, Tax
     allocation mechanics, ECCTA / HMRC compliance (UK), Dissolution and deadlock provisions,
     No specific focus — full review
   - Allow multiple selections.

If the user provides partial context, proceed with reasonable assumptions and state them
explicitly. Do not silently assume.

### Step 3: Load the Playbook (if configured)

Check for any organisation-specific contract review playbook (e.g., `legal.local.md` or
similar configuration file).

**If no playbook is configured:**

**⟁ CLARIFY** — Inform the user that no playbook was found, and ask:

- **Option A: Proceed with general market standards** — Use market-standard positions for
  the identified partnership type and jurisdiction. Faster, but may not reflect the
  organisation's specific risk appetite or investment policy.
- **Option B: Provide key positions now** — The user specifies their standard positions on
  key terms (management consent thresholds, preferred return, non-compete duration,
  expulsion triggers, buyout valuation methodology) and the review will assess against
  those positions.
- **Option C: I'll answer as we go** — Start the review and ask about preferred positions
  when they matter for each clause.

Label clearly when proceeding on general market standards rather than organisational positions.

### Step 4: Identify Structure and Statutory Baseline

Read the agreement's governing law clause, partnership type recitals, and parties section.
Identify:

1. **Partnership structure** (GP / LP / LLP / PFLP / other)
2. **Applicable statute** — the specific Act or equivalent that supplies default rules
3. **Parties and roles** — general partner(s), limited partner(s), members, designated
   members, managing partner, etc.
4. **Effective date** and any prior agreements being superseded

Use **legalcode-mcp** (if connected) to verify current statute versions and any recent
amendments relevant to the governing law.

**⟁ CLARIFY** — Ask the user before proceeding if any of the following are true:

- **No governing law clause found**: Flag as a RED gap; ask which jurisdiction the user
  expects to apply.
- **Governing law is a state/jurisdiction without RUPA adoption** (e.g., Louisiana for US
  partnerships): Flag the specific statute that applies.
- **Agreement appears to govern an LLP but lacks LLP-specific provisions**: Confirm
  whether the user intends to analyze as an LLP (LLP Act 2000 / LLC equivalent) or GP.
- **Australian agreement**: Confirm the relevant state to identify the correct Act and
  assess whether the LP structure will be treated as a corporate LP under Division 5A.

**If legalcode-mcp is not connected:**

- Mark all statutory citations with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with general knowledge of applicable statutes but flag for independent verification

### Step 5: Clause-by-Clause Analysis

Analyze the agreement systematically. Read the entire agreement before flagging issues —
clauses interact with each other (e.g., a broad management authority clause may be
partially constrained by a reserved matters schedule; a buyout provision may be undermined
by a valuation methodology defined elsewhere).

**⟁ CLARIFY** — For long or complex agreements (40+ pages, or with multiple schedules,
side letters, or incorporated documents):

- Ask whether to perform a **full review** (all 16 clause categories) or a **priority
  review** (focused on user's stated focus areas plus all RED items found).
- If the agreement incorporates external documents by reference (management agreement,
  subscription agreement, separate deed of adherence), ask whether to review those too.

Cover all 16 clause categories below. For each, assess against the playbook (or general
market standards) and note whether the clause is present, absent, or unusual.

| #   | Clause Category                               | Depth    | Key Review Points                                                                                 |
| --- | --------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------- |
| 1   | Capital Contributions                         | Deep     | Initial vs. additional calls, mandatory vs. optional, default consequences, in-kind contributions |
| 2   | Profit/Loss Allocation & Distributions        | Deep     | Waterfall structure, preferred return, catch-up, carried interest, clawback                       |
| 3   | Management Authority & Reserved Matters       | Deep     | GP/managing partner powers, voting thresholds, LPAC role, removal rights                          |
| 4   | Partner Fiduciary Duties                      | Deep     | Duty of loyalty, duty of care, good faith, conflict of interest, corporate opportunity            |
| 5   | Non-Compete & Restrictive Covenants           | Deep     | Scope, duration, geographic reach, enforceability, garden leave                                   |
| 6   | Partner Admission                             | Standard | Consent threshold, deed of adherence, anti-dilution, conditions precedent                         |
| 7   | Withdrawal, Retirement & Expulsion            | Deep     | Withdrawal mechanics, expulsion triggers, notice, valuation on exit                               |
| 8   | Transfer Restrictions                         | Standard | Restrictions on transfer, ROFO/ROFR, tag-along, drag-along, charging order                        |
| 9   | Dissolution & Winding Up                      | Deep     | Triggering events, deadlock mechanism, winding-up agent, asset distribution                       |
| 10  | Tax Allocation (US) / Tax Treatment (UK/AU)   | Deep     | §704(b) allocations, targeted allocations, §754 election, UK salaried members, AU Division 5A     |
| 11  | Confidentiality                               | Standard | Scope, term, carveouts, portfolio company information walls                                       |
| 12  | Indemnification & Insurance                   | Standard | Partner indemnity, scope of coverage, D&O insurance for GP                                        |
| 13  | Information Rights & Books/Records            | Standard | Partner information rights, audit rights, capital account statements                              |
| 14  | Governing Law & Dispute Resolution            | Standard | Jurisdiction, arbitration, deadlock escalation, expert determination                              |
| 15  | Anti-Money Laundering & Regulatory Compliance | Standard | ECCTA 2023 (UK), PSC/ROE, FinCEN/CTA (US), FATF compliance                                        |
| 16  | Definitions & Boilerplate                     | Standard | Entire agreement, amendment, notices, force majeure, liability caps                               |

### Step 6: Missing Clause Detection

After analyzing clauses that are present, check for important clauses that are entirely
absent. A missing clause is often as significant as a problematic one.

For each of the 16 clause categories:

- Assess whether the absence is acceptable or a material gap
- Classify the absence as GREEN (not needed), YELLOW (should be added), or RED (must be added)

Common missing clause issues in partnership agreements:

- No capital account maintenance provisions (RED — undermines US tax allocations)
- No clawback provision in a fund LP with American waterfall (RED)
- No deadlock resolution mechanism in an equally-held partnership (RED)
- No expulsion clause — default law prohibits expulsion without one (RED)
- No reserved matters schedule in a multi-partner GP (RED)
- No drag-along right in a fund LP or JV partnership (YELLOW)
- No LPAC provisions in a UK PFLP or US fund LP (YELLOW)
- No ECCTA 2023 compliance provisions in a UK LP (YELLOW — effective spring 2026)
- No information rights for limited partners (YELLOW)
- No anti-dilution protection for existing partners on admission of new partners (YELLOW)

**⟁ CLARIFY** — When the severity of a missing clause depends on business context:

- "This agreement has no clawback provision. Is this a deal-by-deal (American) waterfall?
  If yes, the absence of clawback is a RED gap for limited partners."
- "There is no reserved matters schedule. How many partners are involved and what is the
  voting structure? If management decisions require only GP approval, this may be fine;
  in a GP structure with multiple partners, it is a RED gap."
- "No ECCTA 2023 compliance clause found. Is this a UK LP registered or to be registered
  after spring 2026? If yes, this is a YELLOW-to-RED compliance gap."

### Step 7: Flag Deviations

Classify each deviation from market standards using the four-tier system defined in
the **Deviation Severity Classification** section below. For each deviation:

- **GREEN**: Note for awareness.
- **YELLOW**: Generate specific redline language, provide a fallback position, and estimate
  business impact of accepting vs. negotiating.
- **RED**: Explain the specific risk (citing legal basis where possible), provide
  market-standard alternative language, estimate exposure, and recommend an escalation path.
- **STRUCTURAL**: Flag where the clause or structure requires advice from a specialist
  (tax counsel for US §704(c)/§754 issues, regulatory counsel for PFLP control rule
  concerns, restructuring counsel for AU Division 5A issues).

**⟁ CLARIFY** — For borderline classifications:

- **YELLOW vs. RED borderline**: "This carried interest catch-up is structured as a 100%
  catch-up, meaning the GP receives 100% of distributions until fully caught up before
  the LP receives further distributions. Is this acceptable given the partnership's
  strategy, or should I treat this as RED (escalate to senior counsel)?"
- **Risk tolerance check**: "This agreement has several provisions consistently favouring
  the general partner. Should I apply a conservative classification (flag more items) or
  pragmatic classification (flag only items with material economic impact)?"

### Step 8: Generate Redlines

**⟁ CLARIFY** — Before generating redlines, ask:

- **Negotiation posture**: Is this an incoming LP reviewing a GP-drafted standard LPA
  (i.e., less leverage), or is this a joint venture negotiation between equally positioned
  parties (more leverage)?
- **Volume of redlines**: If there are many YELLOW items, ask: "I've found [N] items worth
  negotiating. Do you want redlines for all of them, or the top [X] most impactful?"

For each YELLOW and RED deviation, generate a redline using the **Redline Format** below.

### Step 9: Business Impact Summary

Provide a summary section covering:

- **Overall risk assessment**: High-level view of the agreement's risk profile
- **Top 3-5 issues**: Most important items with severity and one-line summaries
- **Negotiation strategy**: Which issues to lead with, what to concede, how to sequence
- **Structural notes**: Any STRUCTURAL items requiring specialist engagement

**⟁ CLARIFY** — If deal context would materially affect the negotiation strategy:

- "Can you walk away from this partnership, or is the GP/counterparty essential to your
  strategy? This determines whether the approach is assertive or accommodating."
- "Who has authority to approve deviations from standard terms? This determines whether
  RED items need escalation to the investment committee, board, or external counsel."

### Step 10: Quality Verification

Before delivering the analysis:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every RED-classified item, run the 3-pass Self-Interrogation. Revise if any pass
   reveals a weakness.
3. Assign a Confidence Score to each material clause analysis.
4. Verify completeness: confirm all 16 clause categories addressed (present or flagged
   as missing).
5. Generate the Glass Box Audit Trail and append it to the output.

### Step 11: CLM / Fund Admin Routing

If a Contract Lifecycle Management or fund administration system is connected via MCP:

- Recommend the appropriate approval workflow based on partnership type and risk level
- Suggest routing path (standard LP review, IC approval, external counsel, tax review)
- Note any required approvals based on commitment size or risk flags

If no system is connected, skip this step.

---

## Clause Analysis Reference

### 1. Capital Contributions

**Key elements to review:**

- Distinction between **initial** capital contributions (committed at closing) and
  **additional** capital calls (drawn over the investment period)
- Whether additional capital calls are **mandatory** (breach → default consequences) or
  **optional** (voluntary top-ups only)
- **Default consequences**: interest accrual, dilution/forfeiture of interest, forced
  buyout at discounted price, conversion to loan, suspension of distributions,
  exclusion from future investments
- **In-kind contributions**: valuation mechanism (agreed value? independent appraisal?
  mutual consent?), tax treatment (US: §721 non-recognition; AU: potential CGT event)
- **Capital account maintenance**: required for US §704(b) compliance; must track book
  value adjustments separately from tax basis
- **Unfunded commitment obligations**: survival of funding obligations on transfer,
  obligations post-dissolution

**Common issues:**

- Default provisions that are disproportionately punitive (e.g., forfeiture of entire
  committed capital without fair value compensation) — potential penalty doctrine challenge
- No cure period before default consequences trigger
- No mechanism for adjusting capital accounts on admission of new partners ("book-up")
  — critical for US tax compliance
- In-kind contributions accepted without independent appraisal — dispute risk
- Capital calls with no limit on frequency or maximum amount beyond committed capital
- No provisions for failure to make a capital call: partnership left without agreed
  funding, no recourse mechanism

[JURISDICTION-SPECIFIC] Key variations:

- **US**: Capital account maintenance is mandatory for §704(b) allocations to have
  "substantial economic effect." Default provisions must be commercially reasonable
  to avoid challenge as unenforceable penalties [VERIFY]
- **UK**: No equivalent to §704(b). Capital accounts track economic entitlements. Default
  provisions subject to penalty doctrine (Cavendish Square Holding BV v El Makdessi
  [2015] UKSC 67) — must be a "genuine pre-estimate of loss or legitimate deterrent" [VERIFY]
- **Australia**: In-kind contributions may trigger CGT events. Corporate LP treatment under
  Division 5A means capital contributions are treated as share subscriptions for tax
  purposes [VERIFY]

### 2. Profit/Loss Allocation and Distribution Waterfalls

**Key elements to review:**

- **Allocation vs. distribution**: US partnerships must distinguish tax allocations (which
  determine tax liability) from distributions (actual cash flows). These may differ.
- **Waterfall structure type**:
  - _European waterfall_: Full return of all LP committed capital + preferred return
    before any GP carried interest. Protects LPs against early carry without full recovery.
  - _American (deal-by-deal) waterfall_: Carry calculated and paid on each deal as it
    realises. Benefits GP but creates substantial clawback risk.
- **Preferred return (hurdle rate)**: Typically 8% p.a. Specify: simple vs. compound
  interest; compounding frequency; basis (committed vs. invested capital); whether
  preferred return applies to management fees and organisational costs.
- **Catch-up provision**: After preferred return, GP receives 100% (or partial %) until
  total carry = agreed %. Market standard is full catch-up to 20% carry split. Ensure
  the catch-up formula is mathematically precise.
- **Carried interest split**: Market standard is 20%/80% (GP/LP), with variations 25%/75%
  or 30%/70% for top-tier managers. Clarify: does carry apply only to unrealised gains
  at fund end, or on a realisation-by-realisation basis?
- **Clawback**: On final liquidation, if the GP has received excess carried interest (due
  to early outperformance followed by later underperformance), it must return the excess
  to LPs. Specify: net or gross of tax? Escrow mechanism? Personal guarantee from GP
  principals? Time limit on clawback recovery?
- **Interim clawback**: Approximately 64% of funds now include interim clawback
  mechanisms triggered by falling below the preferred return threshold. Check whether
  the agreement has this or only an end-of-fund clawback.
- **GP escrow**: Market standard is ~25% of carry distributions held in escrow to secure
  clawback obligations. Check whether escrow is required and what triggers release.
- **Loss allocation**: Check that losses are allocated consistently with the capital
  account maintenance requirements.
- **Tax allocations**: US: §704(b) "substantial economic effect" or "partner's interest
  in the partnership" test must be satisfied. Targeted/target capital account allocations
  are now market standard (allocate income/loss to bring each partner's capital account
  to their hypothetical liquidation proceeds). Review for internal consistency.

**Common issues:**

- American waterfall without clawback — RED for LPs
- Clawback calculated gross of tax, leaving GP exposed to tax on distributions already
  returned — identify which party bears the tax cost
- Preferred return not compounded — reduces LP economics in long-term funds
- Catch-up formula ambiguous — "GP receives 20% of all profits" vs. "GP receives
  profits until GP has received 20% of all profits distributed" are mathematically
  different with large practical consequence
- Targeted allocations that do not properly specify the "liquidation proceeds" reference
  point — creates audit risk under US §704(b) regulations
- No mechanism for adjusting IRR calculation date if the fund extends its term

[JURISDICTION-SPECIFIC] Key variations:

- **US §1061 (TCJA 2017)**: Carried interest held less than 3 years is subject to
  short-term capital gains rates rather than long-term rates. Verify that the agreement
  and fund timeline are calibrated accordingly [VERIFY]
- **UK**: Carried interest is typically taxed as capital gain at 28% (residential property)
  or 18-20% (other assets), subject to meeting the "carried interest" conditions under
  TCJA Finance Act 2015 Sch. 5. HMRC has become more aggressive on fund manager
  remuneration structures [VERIFY]
- **Australia (corporate LP)**: Under Division 5A, distributions from a corporate LP
  are treated as dividends and taxed at the corporate rate. This fundamentally changes
  the economics of carried interest. VCLPs registered under the Venture Capital Act 2002
  retain pass-through treatment [VERIFY]

### 3. Management Authority and Reserved Matters

**Key elements to review:**

- Scope of **general/managing partner authority**: What decisions can the GP/managing
  partner make unilaterally?
- **Reserved matters**: Decisions requiring LP/partner consent (specify the threshold:
  simple majority by number/capital interest, supermajority 66%/75%, or unanimous).
  Typical reserved matters: new lines of business, borrowing above threshold, major
  asset disposals, admission of new partners, appointment/removal of key persons,
  amendments to the agreement.
- **LPAC (Limited Partner Advisory Committee)**: Composition, quorum, scope of advisory
  role vs. binding consent, conflict of interest approval, GP replacement input. Verify
  that LPAC functions are advisory-only (especially in Australian LPs to avoid triggering
  control rule and loss of limited liability).
- **GP removal**: Distinguish for-cause removal (fraud, wilful default, key person event)
  from no-fault removal (requires supermajority LP vote, typically 75%+ by capital
  interest). Check: does removal trigger a right to continue the partnership, or does
  it trigger dissolution?
- **Key person provisions**: Named key persons; what events trigger a "key person event"
  (death, incapacity, departure, reduced commitment); consequences (suspension of new
  investment period, right to remove GP without penalty, acceleration of no-fault
  removal rights)
- **RUPA §303 Statement of Authority** (US): If a Statement of Authority is filed,
  check whether it limits or expands apparent authority of individual partners.

**Common issues:**

- No reserved matters schedule, or reserved matters list is too narrow — leaves minority
  partners without veto on fundamental changes
- LPAC given formal approval rights rather than advisory role — may inadvertently trigger
  control rule in Australia and RULPA 1985 jurisdictions
- GP removal requires unanimous LP consent — effectively gives each LP a veto, creating
  deadlock risk
- Key person provisions identify individuals by role rather than name — creates ambiguity
  on succession
- No mechanism to replace a GP that has been removed — dissolution is the only outcome

[JURISDICTION-SPECIFIC] Key variations:

- **US (RUPA § 301)**: Unless the partnership agreement limits a partner's authority,
  every partner is an agent of the partnership for business purposes. A Statement of
  Authority (§ 303) can restrict this for recorded transactions [VERIFY]
- **UK (PA 1890 § 8)**: Every partner is an agent of the firm for the purpose of the
  business. Third parties dealing with a partner in good faith are protected even if that
  partner exceeded internal authority. Management restrictions in the agreement bind
  partners inter se but not innocent third parties [VERIFY]
- **Australia**: Control rule in most state LP Acts: a limited partner who participates in
  management loses their limited liability shield. LPAC approval functions should be
  structured as advisory recommendations. The whitelist approach under PFLP Order 2017
  (UK) is not available in Australia — specific LPAC scope drafting is essential [VERIFY]

### 4. Partner Fiduciary Duties

**Key elements to review:**

- **Duty of loyalty**: Partners must account for profits derived from partnership business
  or from use of partnership property. Competing with the partnership is prohibited before
  dissolution. Verify whether the agreement modifies these defaults.
- **Duty of care**: Under RUPA § 404(c), the standard is gross negligence / reckless
  conduct / intentional misconduct. Many agreements seek to lower this standard; confirm
  whether the modification is permissible under the governing law.
- **Good faith and fair dealing**: RUPA § 404(d) imposes a non-waivable duty of good
  faith and fair dealing in the exercise of rights under the agreement. UK and Australia
  impose equitable good faith obligations between partners.
- **Exculpation clauses**: Partners typically agree to exculpate each other for acts not
  constituting gross negligence, fraud, or wilful misconduct. Check for scope creep:
  does the exculpation apply to the GP's management of partnership assets?
- **Conflict of interest waivers**: LPs typically consent in advance to identified
  categories of conflicts (related-party transactions, co-investments with other funds,
  GP investing alongside). Check that the consent mechanism is specific enough to be
  meaningful and properly noticed.
- **Corporate opportunity carve-outs**: GP and its affiliates may identify investment
  opportunities outside the partnership's investment mandate. Check whether the agreement
  includes a carve-out releasing the GP from the duty to present these to the partnership.

**Common issues:**

- Exculpation clause so broad it effectively eliminates the GP's duty of care
- No mechanism for LP approval of related-party transactions beyond LPAC advisory opinion
- Conflict of interest consent so generic it may not effectively waive specific future
  conflicts — courts in both US and UK have been critical of blanket advance waivers
- No side letter cross-referencing regime to manage conflicts between LP-specific rights
  and the partnership's obligations to the fund generally
- UK: Duty of good faith under Floydd v Cheney [1970] Ch 602 cannot be fully excluded by
  agreement — check that the agreement does not purport to do so [VERIFY]

[JURISDICTION-SPECIFIC] Key variations:

- **US RUPA § 404**: The duty of loyalty and duty of care are mandatory — they cannot
  be eliminated but may be "reasonably restricted" by the partnership agreement. The 2013
  amendments removed the word "only" from the mandatory duty formulation [VERIFY]
- **UK (PA 1890)**: The Act does not codify fiduciary duties but they arise from the
  equitable obligation of good faith between partners (Floydd v Cheney [1970]). These
  duties are more flexible and context-dependent than RUPA's codified duties [VERIFY]
- **Delaware**: Delaware courts have enforced broad contractual modifications to fiduciary
  duties in LP agreements under DRULPA § 17-1101(d), provided the modification is
  explicit. This is more permissive than RUPA [VERIFY]
- **Australia**: The High Court has confirmed that partners owe each other fiduciary
  obligations of loyalty. Exact scope is court-determined rather than statutorily defined;
  standard of review is objective reasonableness [VERIFY]

### 5. Non-Compete and Restrictive Covenants

**Key elements to review:**

- **Scope of activity restricted**: Define the "restricted business" with precision.
  Overly broad definitions increase unenforceability risk.
- **Geographic scope**: The wider the geography, the less likely to be enforceable.
  Global restrictions are extremely difficult to enforce outside specialist fund management
  contexts. Assess whether the scope is proportionate to the legitimate interest.
- **Duration**: The longer the restriction, the higher the enforceability risk. Typical
  enforceable ranges: 12–24 months post-exit for most industries; up to 3–5 years for
  senior partners in some professional service contexts.
- **Non-solicitation of clients**: Typically more enforceable than full non-competes.
  Assess whether the restriction applies to clients the partner actually dealt with (more
  defensible) or the entire client list.
- **Non-solicitation of staff**: Broad team-raiding restrictions (preventing solicitation
  of all employees) are viewed more sceptically than targeted restrictions on key persons.
- **Garden leave**: UK and AU preference over bare post-exit restrictions. A partner on
  garden leave is paid through notice and restricted from practice — courts treat
  garden leave as reducing the time for which post-exit covenants are justified.
- **Distribution-conditioned covenants** (US): Delaware Supreme Court January 2024 ruling
  confirmed that non-compete covenants tied to the receipt of partnership distributions
  (i.e., the partner must refrain from competing to receive distributions) are enforceable.
  This is a powerful structuring tool in Delaware but may not transfer to other states [VERIFY]

**Common issues:**

- Global non-compete in an agreement governed by California law — void under Bus. & Prof.
  Code § 16600, even if the partner is not a California resident (SB 699/AB 1076 2024
  extraterritorial application) [VERIFY]
- Post-exit restriction that is longer than necessary for legitimate interest protection
  and therefore unenforceable
- No garden leave provision in a UK agreement — bare post-exit non-compete in a
  professional partnership context is vulnerable to challenge
- Non-solicitation applies to prospective clients as well as existing clients — courts
  regularly sever or invalidate the prospective client element
- No carve-out for passive investments — broad non-compete that technically prohibits
  holding listed company shares

[JURISDICTION-SPECIFIC] Key variations:

- **US (General)**: Enforceability is entirely state-specific. The FTC's proposed non-compete
  rule was struck down by federal courts in 2024 (Ryan LLC v. FTC). Eleven states now ban
  or severely restrict post-employment/post-partnership non-competes [VERIFY]
- **UK**: Restraint of trade doctrine applies. Courts assess whether the covenant: (i)
  protects a legitimate proprietary interest (trade secrets, client relationships); (ii)
  goes no further than reasonably necessary; and (iii) is not contrary to public policy.
  Garden leave period reduces acceptable post-exit restriction duration [VERIFY]
- **Australia**: Similar reasonableness test. Blue-penciling is available in some states
  to sever unreasonable provisions rather than voiding the entire covenant [VERIFY]

### 6. Partner Admission

**Key elements to review:**

- Consent threshold for admission: unanimous consent is the statutory default in all three
  jurisdictions. Agreements frequently modify this to GP discretion or simple majority.
  Assess whether the modification appropriately protects existing partners.
- **Anti-dilution protection**: Existing partners should have pre-emptive rights to
  subscribe for new interests proportionally before new partners are admitted at
  advantageous terms.
- **Deed of adherence**: Incoming partners must execute a deed adhering to the agreement
  (and any existing side letters). Verify the mechanism is legally effective in the
  governing jurisdiction.
- **Representations from incoming partners**: Regulatory status, accredited investor/
  professional investor status, AML/KYC compliance, sanctions screening.
- **US §708 technical termination** (pre-TCJA 2017): Abolished for tax years beginning
  after December 31, 2017. However, admission of a new partner still has §704(c)
  consequences (book-tax disparities on contributed property) that require careful attention.

### 7. Withdrawal, Retirement, and Expulsion

**Key elements to review:**

- **Voluntary withdrawal** (at-will partnerships): Any partner may withdraw on notice.
  Specify notice period; consequences of withdrawal (continuation or dissolution?);
  whether a withdrawing partner remains liable for pre-withdrawal obligations.
- **Wrongful dissociation** (US RUPA): A partner who withdraws in breach of a fixed-term
  agreement is liable for damages caused. Verify whether the agreement specifies what
  constitutes wrongful dissociation.
- **Retirement by agreement**: Negotiated exit, typically with valuation based on agreed
  methodology. Check whether the retiring partner must accept the offered valuation or
  can trigger an independent appraisal.
- **Expulsion**:
  - Express authority is required (RUPA § 601(4); UK PA 1890 § 25 — majority cannot
    expel a partner without express agreement provision)
  - Expulsion triggers should be specific and objective (fraud, wilful default,
    insolvency, regulatory disqualification) rather than vague ("conduct prejudicial to
    the business") to reduce challenge risk
  - Procedural fairness: notice, opportunity to cure (where applicable), appeal mechanism
  - Valuation on expulsion: fair value vs. discounted "bad leaver" price — discounted
    expulsion prices are enforceable if they represent a proportionate deterrent
    (Cavendish Square test in UK; see also Delaware's enforcement of "bad leaver"
    provisions)
- **Buyout valuation on exit**:
  - RUPA § 701 default: greater of liquidation value or going-concern value
  - Agreement should specify the valuation methodology (EBITDA multiple, independent
    appraisal, agreed formula) and the timing (last accounts, current, hypothetical
    realisation)
  - Deadlines for completing the buyout and interest on delayed payment

**Common issues:**

- Expulsion clause with vague triggers giving GP/majority subjective discretion — RED,
  expulsion exercised in bad faith is challengeable in all three jurisdictions
- No cure period for remediable breaches before expulsion triggers
- Buyout valuation based solely on book value — significantly undervalues going-concern
  businesses and is frequently challenged
- No mechanism to challenge the offered valuation — partner is stuck with GP's
  self-determined price
- Survival of non-compete obligations not expressly linked to the buyout being paid —
  creates an argument that non-compete is unenforceable if consideration is not received

[JURISDICTION-SPECIFIC] Key variations:

- **US RUPA § 701**: "Greater of liquidation value or going-concern value" is a mandatory
  default that cannot be contracted away to the detriment of the departing partner [VERIFY]
- **UK**: No equivalent statutory floor. Courts apply the general law on penalty clauses
  (Cavendish Square test). Discriminatory buyout valuations between partners of the same
  class may be challengeable as breach of good faith [VERIFY]

### 8. Transfer Restrictions

**Key elements to review:**

- **Restrictions on voluntary transfer**: Transfer of a partner's interest typically
  requires unanimous consent (statutory default). Agreements commonly relax this for
  permitted transferees (affiliates, related funds, estate planning transfers).
- **ROFO/ROFR**: Right of first offer (ROFO) or right of first refusal (ROFR) in favour
  of existing partners. ROFO (partner offers interest to partners first before going to
  market) is generally preferred by the selling partner; ROFR (existing partners can
  match any third-party offer) is generally preferred by buying partners.
- **Tag-along rights**: Minority partners' right to sell alongside a majority on the same
  terms. Specify: threshold of majority sale that triggers the right; time limit for
  exercise; apportionment mechanism if the buyer will not purchase all interests.
- **Drag-along rights**: Majority's right to compel minority to sell on same terms.
  Specify: triggering threshold (typically 75%+); same-price-and-terms requirement;
  exclusion of non-cash consideration; interaction with pre-emption rights (must be
  expressly addressed or pre-emption takes priority). Note: Foley Hoag 2025 alert on
  French drag-along clause invalidation for failing to specify price determination.
- **Charging order**: In all three jurisdictions, a partner's personal creditor's
  remedy is limited to a charging order against the partner's distributional interest —
  the creditor cannot obtain management rights or force dissolution. Check whether the
  agreement provides any additional protection or addresses charging order consequences.
- **GP/managing partner interests**: Separate transfer restrictions often apply — GP
  interest is usually non-transferable without LP consent (key person concern).

### 9. Dissolution and Winding Up

**Key elements to review:**

- **Dissolution triggers**: List specific triggering events and ensure they are exclusive
  (i.e., dissolution cannot be triggered unilaterally by a dissatisfied partner outside
  this list). Typical triggers: expiry of fixed term; unanimous consent; court order;
  insolvency of the partnership; GP insolvency/removal without replacement; persistent
  deadlock; regulatory prohibition.
- **Deadlock mechanism**: This is the most dangerous gap in equally-held partnerships.
  Escalation procedure options: (i) senior management referral; (ii) mediation;
  (iii) shotgun/Russian Roulette buy-sell (one party sets a price, the other chooses
  whether to buy or sell at that price); (iv) Texas Shoot-Out (each party submits a
  sealed bid, highest bidder buys out the other); (v) appointment of independent
  tiebreaker; (vi) dissolution as backstop. A provision that provides only for "good
  faith negotiation" without a backstop is NOT an effective deadlock mechanism.
- **Winding-up agent**: Who conducts the winding up? Appointment mechanism if the GP is
  dissolved or removed? Does the court have jurisdiction to appoint a liquidator?
- **Asset distribution on winding up**: Creditors first; then partner loans; then return
  of capital contributions; then residual profits/losses per allocation provisions. Verify
  the agreement expressly addresses the distribution waterfall on dissolution and aligns
  with applicable statute.
- **Survival of obligations**: Non-compete, confidentiality, and indemnity obligations
  should expressly survive dissolution.

**Common issues:**

- No effective deadlock mechanism (only "good faith negotiation") — RED in equally-held
  or supermajority-required partnerships
- Dissolution triggered by death/withdrawal of any partner, with no continuation
  mechanism — creates unnecessary dissolution risk (this is the PA 1890 § 33 default;
  nearly all professional agreements address this)
- No mechanism to replace a removed GP, meaning removal automatically triggers dissolution
- Winding-up waterfall does not expressly override the profit allocation waterfall —
  creates ambiguity on final distributions

[JURISDICTION-SPECIFIC] Key variations:

- **US RUPA §§ 801–807**: Dissolution is restricted to specific events; the 2013
  amendments further limited dissolution triggers. Winding up: §807 distribution order —
  creditors → partner loans → capital → residual surplus [VERIFY]
- **UK PA 1890 §§ 32–44**: More liberal dissolution defaults (e.g., §33 — dissolution
  on partner death unless agreement provides otherwise). Section 44 governs asset
  distribution on dissolution [VERIFY]
- **Australia**: State-based Acts broadly follow PA 1890. No unified national approach
  to dissolution procedures for limited partnerships [VERIFY]

### 10. Tax Allocation Mechanics (US) and Tax Treatment (UK/AU)

**US — §704(b) Substantial Economic Effect:**

- US partnership tax allocations must either have "substantial economic effect" (the
  two-part safe harbour) or be in accordance with the "partners' interest in the
  partnership." The safe harbour requires: (i) economic effect (the partner bears the
  economic burden/benefit matching the allocation); and (ii) substantiality (the
  allocation meaningfully affects partners' net economic positions independent of tax).
- **Targeted allocations** (market standard): The agreement allocates income and loss to
  bring each partner's capital account to their hypothetical liquidation proceeds. Review
  the "hypothetical liquidation" language carefully — it must be precise and consistently
  applied across the entire agreement.
- **§704(c) contributed property**: When a partner contributes property with a book-tax
  basis disparity, allocations must use an approved method (traditional, traditional with
  curative, or remedial) to prevent shifting pre-contribution gain/loss to other partners.
- **§754 election**: An election to adjust the basis of partnership property upon
  transfer of a partner interest (§743(b)) or certain distributions (§734(b)). On a
  partner's death, the estate takes a stepped-up outside basis (§1014), but without a
  §754 election this does not carry through to partnership assets. Should the agreement
  specify whether the partnership will maintain a §754 election? Check for the IRS 2025
  final regulations targeting related-party basis adjustment transactions. [VERIFY]
- **Guaranteed payments (§707(c))**: Distinguish partner compensation styled as
  guaranteed payments from distributive shares. Guaranteed payments are deductible by
  the partnership and taxable as ordinary income to the recipient, regardless of
  partnership profitability. Misclassification creates tax issues.
- **BBA centralized audit rules**: Post-TEFRA, the Bipartisan Budget Act 2015 centralized
  audit rules apply to most large partnerships. Check whether the agreement designates
  a "partnership representative" and provides for the "push-out election" mechanism.

**UK — Salaried Members Rules (LLP context):**

- Finance Act 2014 introduced the Salaried Members rules to prevent LLP members from
  claiming self-employed tax treatment when their economic position resembles employment.
  A member is treated as a salaried employee if they satisfy **all three conditions**:
  - **Condition A**: ≥80% of remuneration is "disguised salary" (fixed, not variable by
    reference to LLP overall profits)
  - **Condition B**: Member does not have "significant influence" over LLP affairs
  - **Condition C**: Member's capital contribution is less than 25% of their disguised salary
    A member who fails at least one condition retains self-employed status.
- **2024 HMRC guidance reversal**: HMRC issued and then reversed guidance narrowing
  "significant influence" under Condition B. Current position is uncertain — LLPs should
  maintain contemporaneous evidence of each member's influence.
- **BlueCrest case (2025)**: Ongoing judicial scrutiny of significant influence; fund
  management LLPs face heightened HMRC scrutiny.
- Review: Does the members' agreement create structures that satisfy at least one condition
  for all members? Are profit share provisions documented to demonstrate variability?

**Australia — Division 5A Corporate Limited Partnerships:**

- Limited partnerships formed on or after 19 August 1992 are generally taxed as
  **corporate limited partnerships** under Division 5A, ITAA 1936, at corporate tax rates.
  Distributions are treated as dividends; partner interests as shares.
- **Exceptions**: (i) Venture Capital Limited Partnerships (VCLPs) registered under the
  Venture Capital Act 2002 retain pass-through treatment; (ii) foreign hybrid LPs may
  qualify under §830-10 exclusions.
- **ATO TR 2024/2**: Clarifies when a corporate LP "credits" an amount to a partner —
  relevant to determining when distributions arise for tax purposes.
- Review: Is the LP intended to be a VCLP? If yes, verify registration requirements.
  If not, have the parties understood and accepted the corporate tax treatment?

### 11–16. Standard Clause Checklist

For the following clause categories, review presence, reasonableness, and alignment with
market standards. Flag deviations using the GREEN/YELLOW/RED/STRUCTURAL system.

**11. Confidentiality**

- [ ] Scope of confidential information defined and reasonable
- [ ] Partners owe confidentiality obligations to each other and to the partnership
- [ ] Provisions for portfolio company information (in fund context) — information
      barriers between LPs who may be competitors
- [ ] Term of confidentiality obligations appropriate (typically 3–5 years post-dissolution,
      or indefinite for trade secrets)
- [ ] Standard carveouts present (public domain, legally required disclosure, independent
      development)
- [ ] Return or destruction of confidential materials on dissolution or partner exit

**12. Indemnification and Insurance**

- [ ] Partnership indemnifies partners for acts within authority
- [ ] GP/managing partner indemnity scope defined (not broader than authority granted)
- [ ] Exculpation and indemnity consistent — no gaps where partner has no indemnity
      but faces personal liability
- [ ] D&O insurance for GP/managing partner expressly required
- [ ] Insurance obligations survive for a "tail period" after dissolution
- [ ] No indemnity for fraud, wilful default, or gross negligence (standard carveout)

**13. Information Rights and Books/Records**

- [ ] Partners have access to the partnership's books and records
- [ ] Regular financial reporting obligations (quarterly/annual accounts, capital account
      statements)
- [ ] Audit rights for partners
- [ ] US: right of access to books is a mandatory default under RUPA § 403 — confirm
      any limitations on this default right are not unduly restrictive
- [ ] UK: PA 1890 § 24(9) gives every partner access to books — check whether agreement
      restricts this for limited partners
- [ ] K-1/equivalent tax reporting obligations specified (US)
- [ ] Prohibition on trading on MNPI received through partnership information access
      (fund context)

**14. Governing Law and Dispute Resolution**

- [ ] Governing law specified and appropriate for the partnership type
- [ ] Dispute resolution mechanism (arbitration vs. litigation) appropriate for the
      partnership and its investors
- [ ] Escalation provisions: negotiation → mediation → formal proceedings
- [ ] Deadlock escalation is a **separate mechanism** from general dispute resolution
      (deadlock is a management failure; general disputes are about rights under the agreement)
- [ ] Costs allocation provision
- [ ] Jurisdiction/venue appropriate (for fund LPs: typically Courts of England and Wales
      or Delaware courts for US funds)

**15. Anti-Money Laundering and Regulatory Compliance**

- [ ] **UK ECCTA 2023 compliance** (effective spring 2026): All partners in UK LPs must
      be disclosed to Companies House; GP must appoint a registered officer; UK connection
      requirement for new LP registrations. Check whether the agreement includes provisions
      facilitating ECCTA compliance.
- [ ] **UK ROE (Economic Crime Act 2022)**: If the partnership owns UK land, overseas
      entities must register with Companies House. Check whether any partners are overseas
      entities holding UK land interests.
- [ ] **US FinCEN / CTA (Corporate Transparency Act 2024)**: March 2025 interim final rule
      exempted domestic companies from beneficial ownership reporting requirements; foreign
      entities with US registered partnerships still face obligations [VERIFY]
- [ ] **PSC Register** (UK partnerships): LLPs must maintain a register of persons with
      significant control
- [ ] AML/KYC representations from incoming partners on admission
- [ ] FATF compliance representations for cross-border fund structures

**16. Definitions and Boilerplate**

- [ ] All key defined terms used consistently throughout
- [ ] Entire agreement / integration clause present
- [ ] Amendment provisions (written amendments only; specify consent threshold)
- [ ] Severability clause
- [ ] Notice provisions (method, addresses, deemed receipt)
- [ ] Force majeure clause (for operational partnerships)
- [ ] Counterparts/electronic execution
- [ ] Order of precedence between agreement and any schedules/side letters

---

## Deviation Severity Classification

### GREEN — Acceptable

The clause aligns with or is better than market-standard position. Minor variations that
are commercially reasonable and do not materially increase risk.

**Examples:**

- European waterfall with 8% preferred return and 20% carry — fully market standard
- Non-compete of 12 months post-exit in a mid-market professional partnership
- Expulsion triggers limited to objective events with clear cure periods

**Action**: Note for awareness. No negotiation needed.

### YELLOW — Negotiate

The clause falls outside the market standard position but within a negotiable range. The
term is common but not preferred. Requires attention and likely negotiation, but not
escalation.

**Examples:**

- American waterfall without interim clawback (end-of-fund clawback only)
- Non-compete of 24 months in a UK agreement with no garden leave provision
- Reserved matters requiring 75% consent (slightly low for minority partner protection)
- No GP escrow for carried interest distributions

**Action**: Generate specific redline language. Provide fallback position. Estimate
business impact of accepting vs. negotiating.

### RED — Escalate

The clause falls outside the acceptable range, poses material risk, triggers an applicable
statutory prohibition, or requires senior counsel review or business decision-maker sign-off.

**Examples:**

- American waterfall with no clawback provision whatsoever
- Expulsion clause with subjective, vague triggers and no fair process
- Buyout price fixed at book value with no appraisal right — potentially unenforceable
  under RUPA § 701 (greater-of standard)
- Non-compete void under governing law (e.g., California-governed agreement)
- No deadlock mechanism in an equally-held partnership with unanimous consent requirements
- LPAC with binding consent rights in an Australian LP — control rule risk
- No capital account maintenance provisions in a US partnership — §704(b) compliance risk

**Action**: Explain the specific risk with legal basis. Provide market-standard alternative
language. Estimate exposure. Recommend escalation path.

### STRUCTURAL — Requires Specialist Review

The issue is not merely a drafting deviation but a structural matter requiring specialist
advice outside the scope of this review.

**Examples:**

- Australian LP structured as a corporate LP under Division 5A — whether parties
  intended pass-through treatment requires tax restructuring advice
- UK LLP members' agreement where all members likely satisfy all three salaried members
  conditions — HMRC salaried members exposure requires tax counsel
- US partnership §704(b) targeted allocation provisions that appear internally
  inconsistent — tax counsel needed to assess compliance and risk of IRS challenge
- ECCTA 2023 compliance structural issue requiring Companies House legal advice

**Action**: Flag the issue and explain why specialist advice is required. Do not attempt
to resolve the issue within this review. Provide enough detail for the specialist to scope
their engagement.

---

## Redline Format

For each redline:

```
**Clause**: [Section reference and clause name]
**Current language**: "[exact quote from the agreement]"
**Proposed redline**: "[specific alternative language]"
**Rationale**: [1-2 sentences explaining why, suitable for external sharing]
**Legal basis**: [Relevant statute, regulation, or principle — or "General market practice"]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative position if primary redline is rejected]
```

### Redline Best Practices

1. **Be specific**: Provide exact language, not vague guidance. The redline should be
   ready to insert.
2. **Be balanced**: Propose language that is firm on critical points but commercially
   reasonable.
3. **Explain the rationale**: Include a professional rationale suitable for sharing with
   the counterparty's counsel.
4. **Provide fallback positions**: For YELLOW items, include a fallback if the primary
   ask is rejected.
5. **Prioritize**: Indicate which redlines are must-haves and which are nice-to-haves.
6. **Reference applicable law**: Cite the relevant statute or principle. If citing from
   memory, mark with [VERIFY].
7. **Consider the relationship**: GP-drafted standard LPA vs. negotiated JV agreement —
   adjust tone accordingly.

---

## Negotiation Priority Framework

When presenting redlines, organise by negotiation priority:

### Tier 1 — Must-Haves (Deal Breakers)

Issues where the party cannot proceed without resolution:

- Clawback provisions in a fund LP with American waterfall
- Expulsion clause with no express authority (PA 1890 § 25 / RUPA § 601(4))
- Non-compete provisions that are void under the governing law
- No deadlock mechanism in an equally-held partnership
- Buyout valuation methodology so unfavourable as to be commercially unacceptable
- No capital account maintenance in a US partnership (§704(b) risk)
- LPAC with binding rights in an Australian LP (control rule)

### Tier 2 — Should-Haves (Strong Preferences)

Issues that materially affect risk and economics but with negotiation room:

- Preferred return rate and compounding methodology
- Catch-up formula mechanics
- GP escrow for carried interest distributions
- Reserved matters thresholds
- Key person provision trigger events
- Duration and scope of non-solicitation restrictions
- Information rights and audit frequency

### Tier 3 — Nice-to-Haves (Concession Candidates)

Issues that improve the position but can be conceded strategically:

- Preferred governing law/venue if an acceptable alternative exists
- Anti-dilution pre-emption mechanics (form of exercise, timing)
- Minor definitional improvements
- Additional reporting obligations beyond statutory minimum
- Notice period length (if statutory minimum is adequate)

**Negotiation strategy**: Lead with Tier 1 items. Trade Tier 3 concessions to secure
Tier 2 wins. Never concede on Tier 1 without escalation.

---

## Multi-Stakeholder Mapping

For every partnership agreement, identify ALL affected stakeholders:

| Stakeholder                        | Role                  | Affected Clauses                                        | Impact                                 | Action Required                                |
| ---------------------------------- | --------------------- | ------------------------------------------------------- | -------------------------------------- | ---------------------------------------------- |
| General/Managing Partner           | Primary fiduciary     | Management authority, indemnity, fiduciary duties       | Direct — exposed to personal liability | Confirm authority and indemnity scope          |
| Limited Partners                   | Economic stakeholders | Waterfall, clawback, information rights, exit           | Direct — economic returns at risk      | Negotiate waterfall and exit provisions        |
| Incoming/Prospective Partners      | Future stakeholders   | Admission, anti-dilution, deed of adherence             | Direct                                 | Review conditions precedent and anti-dilution  |
| LPAC members                       | Advisory role         | LPAC scope, conflict consents                           | Indirect — advisory liability          | Confirm advisory-only status                   |
| Portfolio companies (fund context) | Indirect              | Confidentiality, information barriers                   | Indirect                               | Ensure confidentiality provisions are adequate |
| Regulatory bodies                  | Compliance            | AML/KYC, ECCTA, PSC register                            | Compliance                             | ECCTA readiness check for UK LPs               |
| HMRC / IRS / ATO                   | Tax authority         | Tax allocation, salaried members (UK), Division 5A (AU) | Compliance                             | STRUCTURAL items for tax counsel review        |
| Estate/successors of partners      | Future stakeholders   | Dissolution, buyout, §754 election                      | Indirect — continuity risk             | Confirm succession and continuation provisions |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                        | Fail Action                                              |
| -------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, case, or established principle                  | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognisable format for the jurisdiction                 | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments, repeal, or superseding legislation            | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the contract's governing law; no assumptions from other jurisdictions | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden                                                   | Add confidence qualifier                                 |

### Self-Interrogation for RED and STRUCTURAL Items

For any clause classified as RED or STRUCTURAL, apply this 3-pass self-interrogation:

**Pass 1 — Legal Chain Integrity**:

- Does the risk assessment follow logically from the statute/principle cited?
- Would a court in this jurisdiction actually reach this conclusion on these facts?
- Is there a counter-argument the counterparty's counsel will make?

**Pass 2 — Completeness**:

- Have all relevant statutes, regulations, and cases been considered?
- Are there regulatory dimensions (tax, HMRC, ATO, IRS) not yet addressed?
- Have any recently enacted or amended rules been missed (ECCTA 2023, IRS 2025 regs)?

**Pass 3 — Challenge**:

- What is the strongest argument that this clause IS acceptable?
- Under what commercial circumstances might a reasonable professional accept this risk?
- Is the RED classification proportionate, or is this actually YELLOW with mitigations?

Mark the audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material clause analysis, assign a confidence level:

| Level        | Range     | Meaning                                          | Action                                                |
| ------------ | --------- | ------------------------------------------------ | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, clear statute, no ambiguity         | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments but reasonable minds could differ | State with explicit reasoning and contra-indicators   |
| **Possible** | 0.40–0.59 | Genuinely uncertain, competing authorities       | Flag for counsel review with both sides               |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                          | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every partnership agreement review output MUST include a Glass Box audit section:

```yaml
glass_box:
  agreement: "[Agreement title and date]"
  partnership_type: "[GP / LP / LLP / PFLP / FLP / Other]"
  user_side: "[GP/Managing Partner / Limited Partner / Incoming Partner / Advisor / Lender]"
  governing_law: "[Jurisdiction identified from the agreement]"
  applicable_statute: "[e.g., RUPA 1997 / Partnership Act 1890 / Partnership Act 1958 Vic]"
  review_basis: "[Organisational playbook / General market standards]"
  clauses_reviewed: 16
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  structural_items: "[number] — [brief description of each]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to temp file or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  case_law_consulted:
    - "[Case — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  tax_items_flagged: "[number] — [brief description; note: refer to tax counsel]"
  eccta_2023_reviewed: "Yes / Not applicable — [governing jurisdiction]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified legal review and tax adviser review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do when reviewing partnership agreements:

1. **Applying the wrong statutory default rules** — Analysing a UK LP under RUPA default
   rules (or vice versa), or applying RUPA uniformly without checking the specific state's
   adopted version. RUPA has been amended by states in material ways; Delaware's DRULPA
   is entirely distinct. Always verify the applicable statute before applying defaults.

2. **Treating all waterfalls as equivalent** — A European waterfall and an American
   waterfall have fundamentally different risk profiles for LPs. Never summarise a
   waterfall without specifying which type it is and what the consequences are for the
   relevant party.

3. **Ignoring the allocation/distribution distinction** — In a US partnership, tax
   allocations (who bears the tax liability) and distributions (who receives cash) are
   separate and may differ. Treating them as synonymous creates materially incorrect
   analysis.

4. **Assuming good faith obligations cannot be modified** — In the US (RUPA § 404(d)),
   good faith and fair dealing is mandatory but can be given specific meaning by the
   agreement. In Delaware, courts have upheld broad contractual modifications to
   fiduciary duties under DRULPA § 17-1101(d). The analysis must reflect the specific
   jurisdiction's approach.

5. **Overlooking the control rule in Australian LPs** — LP limited liability in Australian
   state-based LP Acts is lost if a limited partner participates in management. Unlike the
   UK PFLP regime, Australia has no whitelist of permitted LPAC activities. Reviewing
   LPAC provisions without flagging control rule risk is a material omission.

6. **Applying post-TCJA §704(b) analysis without checking the agreement date** — Many
   older US partnership agreements use traditional layered allocation methods that may
   not satisfy current §704(b) regulations. If the agreement predates 2017 TCJA changes,
   verify the current compliance position before issuing a confident analysis.

7. **Missing Division 5A's company-tax treatment for Australian LPs** — Assuming an
   Australian LP is taxed on a pass-through basis without checking whether it is a
   corporate limited partnership under Division 5A. This is a structural error that
   fundamentally affects the economics of the investment.

8. **Redlines without fallback positions** — A redline that says "add clawback provision"
   without offering draft language is not actionable. Always provide specific language,
   even if drawn from market-standard precedents, with a clear fallback.

9. **Reviewing expulsion provisions without checking mandatory law** — PA 1890 § 25 (UK)
   and RUPA § 601(4) (US) require express authority for expulsion. A reviewof an
   expulsion clause that misses the need for it to be expressly included (rather than
   implied) is dangerously incomplete.

10. **Ignoring the non-compete jurisdictional matrix** — FTC rule vacatur (2024), California
    SB 699/AB 1076 extraterritorial ban, and eleven-state restriction/ban framework make
    US non-compete analysis highly state-specific. Never apply a uniform "reasonableness
    test" without first checking whether the governing state bans non-competes outright.

11. **Accepting the clawback provision at face value** — Review not only whether a
    clawback exists but whether it is enforceable: Is the obligation personal to GP
    principals or only to the GP entity? Is there a GP escrow? Is it gross or net of tax?
    What is the recovery mechanism and time limit? A poorly structured clawback may be
    commercially useless to LPs in practice.

12. **Treating LPAC advisory opinions as binding consents** — In fund structures,
    mischaracterising LPAC functions creates both governance confusion and liability risk.
    Confirm the LPAC's role is advisory only (unless the agreement expressly grants binding
    rights and the jurisdiction permits this without triggering the control rule).

13. **Skipping the tax items** — Partnership tax allocation mechanics are among the most
    commercially significant provisions in the agreement. A review that ignores §704(b)/
    targeted allocations (US), salaried members rules (UK LLPs), or Division 5A treatment
    (AU LPs) is incomplete and potentially misleading. Flag STRUCTURAL items; do not
    attempt to provide tax advice.

14. **Ignoring ECCTA 2023 for UK LPs** — The Economic Crime and Corporate Transparency
    Act 2023 introduces mandatory full partner disclosure, registered officer requirements,
    and UK connection requirements for UK limited partnerships (effective spring 2026).
    Reviewing a UK LP agreement without considering ECCTA readiness is incomplete for any
    agreement that will remain in force after spring 2026.

15. **Assuming a "good faith negotiation" deadlock provision is effective** — A clause
    that provides only for parties to negotiate in good faith in the event of a deadlock
    provides no practical resolution mechanism. Flag the absence of a binding backstop
    (shotgun, Texas shoot-out, expert determination, or dissolution trigger) as RED.

16. **Redlining for the wrong party** — The analysis must be conducted from the user's
    stated perspective. A managing partner analysis and a limited partner analysis of the
    same agreement will reach opposite conclusions on many clauses. Confirm the side
    before beginning and do not switch perspectives mid-review.

17. **Single-pass analysis** — Partnership agreements contain significant clause
    interactions: the waterfall references capital account definitions; the exit provisions
    reference the valuation methodology in a different schedule; the non-compete duration
    interacts with the garden leave period. Read the full agreement before flagging issues.

18. **Ignoring side letters** — In fund structures, individual LP side letters may
    override provisions in the main LPA. A review of the LPA alone may miss material
    concessions already granted to specific LPs that affect the overall fairness analysis.

---

## Writing Standards

Apply plain-language discipline to all output:

**For redline rationales** (shared with counterparty's counsel):

- Plain language. No jargon or filler.
- Active voice: "This clause does not provide a clawback mechanism" not "A clawback
  mechanism is absent from this clause"
- Short sentences. One point per sentence.
- Name the actor: "The general partner must..." not "It is required that..."
- Specific, not vague: cite the relevant provision rather than saying "this may have
  enforceability issues"

**For internal analysis:**

- Same plain-language standards
- May include more technical legal and tax analysis
- Confidence qualifiers where appropriate
- Glass Box audit trail appended
- STRUCTURAL items clearly separated from RED items

**Quality gates before delivery:**

1. Can a non-lawyer business stakeholder understand the executive summary?
2. Can the counterparty's counsel understand and respond to each redline?
3. Is every legal claim backed by a specific citation (or flagged [VERIFY])?
4. Are any phrases vague, hedging, or ambiguous? If yes, fix.
5. Could any sentence be shorter without losing meaning? If yes, shorten.
6. Are all STRUCTURAL items clearly labelled and distinguished from items the reviewer
   can address?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.
legalcode-mcp is a law, regulatory, and case law database with powerful search across
jurisdictions.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for jurisdiction-relevant statutes, cases, and regulatory guidance
- Save the most relevant results to `/tmp/legalcode-partnership-review-authority.md`
- Reference verified authority from the temp file throughout clause analysis
- For RED items, search for additional case law to support or challenge the classification
- Verify: RUPA adoption status in the US state, current ECCTA 2023 implementation dates,
  current IRS regulations on partnership basis adjustments, HMRC salaried members
  guidance, ATO TR 2024/2 status
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Include a prominent notice that legal citations require independent verification
- Focus the analysis on commercial risk assessment and structural issues rather than
  legal certainty
- Do not create the local authority reference file

---

## Localization Notes

### United States — Additional Considerations

- **Delaware LP / DRULPA**: Most US fund limited partnerships are Delaware entities. DRULPA
  is more permissive than RUPA/ULPA and explicitly allows broad modifications to fiduciary
  duties and the distribution waterfall. Delaware courts enforce well-drafted GP-favourable
  LPA terms even against LP challenge — but inadequately drafted provisions receive less
  protection.
- **California B&P § 16600**: Applies extraterritorially since SB 699/AB 1076 (2024) to
  void non-compete provisions in agreements with California-based partners, regardless of
  governing law. A Delaware-governed LPA with California resident LPs should include a
  California carve-out or the non-compete is at risk of being void as applied.
- **BBA audit rules**: Partnerships with more than 100 partners, or complex structures,
  should designate a partnership representative and include push-out election mechanics.

### United Kingdom — Additional Considerations

- **ECCTA 2023 transition**: From spring 2026, all UK limited partnerships must disclose
  all partners to Companies House; GP entities must appoint a registered officer with a
  verified identity. Agreements should include covenants from partners to provide
  required information and cooperate with registration. Failure to comply is an offence
  by the GP and the registered officer.
- **Scottish limited partnerships (SLPs)**: SLPs have separate legal personality (unlike
  English LPs). They have been historically misused for financial crime; ECCTA 2023 and
  prior reforms (LP Act 2017) were partly directed at SLP abuse. Agreements should
  address the substantive UK connection requirement.
- **LLP — non-member employees**: Agreements should clearly distinguish members
  (partners) from employees of the LLP, as different tax, employment law, and insolvency
  rules apply.
- **Professional partnerships (SRA/FCA regulated)**: Additional provisions required for
  SRA compliance (solicitors' practices), FCA authorisation (investment managers), and
  other regulatory registrations. These are beyond the scope of this skill.

### Australia — Additional Considerations

- **State variation**: Partnership law is state-based. The Northern Territory's Partnership
  Act 1997 is the most modern; other states broadly follow the 1890 model. Confirm the
  relevant state before applying defaults.
- **VCLP registration**: VCLPs (Venture Capital Act 2002) registered with Innovation and
  Science Australia retain pass-through tax treatment. Review registration requirements
  and ensure the VCLP structure is reflected in the agreement.
- **Trust overlay**: Many Australian private equity and property funds use a unit trust
  over a limited partnership structure. If a trust overlay is used, trust deed provisions
  interact with and may override partnership agreement provisions — both documents must
  be reviewed together.

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Partnership Agreement Review Summary

**Document**: [Agreement title and date]
**Parties**: [party names and roles — GP, LPs, managing partner, members]
**Your Side**: [GP/managing partner / LP / incoming partner / other]
**Partnership Type**: [GP / LP / LLP / PFLP / FLP / JV partnership]
**Governing Law**: [jurisdiction and applicable statute]
**Review Basis**: [Organisational playbook / General market standards]
**Date of Review**: [date]

---

## Key Findings

[Top 3–5 issues with severity flags (RED/YELLOW/STRUCTURAL) and one-line summaries]

---

## Missing Clauses

[List any of the 16 clause categories that are absent, with severity assessment]

---

## Structural Items Requiring Specialist Review

[List any STRUCTURAL items with brief explanation of why specialist advice is needed]

---

## Clause-by-Clause Analysis

### [Clause Category] — [GREEN / YELLOW / RED / STRUCTURAL] | Confidence: [level]

**Agreement says**: [summary of the provision]
**Market standard**: [what market-standard agreements typically provide]
**Deviation**: [description of gap or issue]
**Business impact**: [what this means practically for the user's side]
**Redline** (if YELLOW or RED):

> [Specific proposed language]

[Repeat for each clause category]

---

## Negotiation Strategy

**Tier 1 (Must-Haves)**: [list]
**Tier 2 (Should-Haves)**: [list]
**Tier 3 (Concession Candidates)**: [list]

**Recommended approach**: [sequencing, tone, strategic trades]

---

## Stakeholder Impact Map

[Table per Multi-Stakeholder Mapping section]

---

## Next Steps

[Specific actions to take, with owners and deadlines if applicable]
[Note STRUCTURAL items and specialist referrals clearly]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis based on deep research into RUPA
1997/2013, ULPA 2001, Delaware DRULPA, Partnership Act 1890, LPA 1907, LLP Act 2000,
PFLP Order 2017, ECCTA 2023 LP reforms, ITAA 1936 Division 5/5A, ATO TR 2024/2, and
IRS 2025 final regulations on related-party basis adjustments. Covers US/UK/AU
partnership law with jurisdiction-agnostic markers. Follows Legalcode gold standard
methodology including 16-clause architecture, 4-tier severity classification (GREEN/
YELLOW/RED/STRUCTURAL), Citation Quality Gates, Self-Interrogation, Confidence Scoring,
Glass Box audit trail, and 18 topic-specific anti-patterns.
