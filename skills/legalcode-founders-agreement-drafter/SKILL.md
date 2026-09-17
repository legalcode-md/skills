---
name: legalcode-founders-agreement-drafter
description: Draft comprehensive founders agreements covering equity allocation and split methodology,
  vesting schedules (cliff, acceleration on single/double-trigger change of control), intellectual property
  assignment with pre-existing IP carve-outs, role definitions and decision-making authority, capital
  contribution requirements, expense policies, non-compete and non-solicitation obligations, departure
  mechanics (voluntary, involuntary, for-cause), buyback provisions with valuation methodology, deadlock
  resolution, and dissolution/wind-down procedures. Use when founding a new company, restructuring founder
  relationships, preparing for Series A investment, or documenting founding team equity arrangements.
  Supports multi-jurisdiction formation decisions (Delaware C-Corp, UK Ltd, Singapore Pte Ltd, India Private
  Limited). Includes explanatory notes for non-lawyer founders. Jurisdiction-aware with [JURISDICTION-SPECIFIC]
  markers. Produces playbook-integrated, investor-ready draft sections with Glass Box audit trail.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Founders Agreement Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted founders agreement
> drafting. It does not constitute legal advice. All outputs must be reviewed by a
> qualified corporate attorney licensed in the relevant jurisdiction before execution.
> Laws change; verify current applicability before relying on any provision described
> here. Statutory and case law references cited carry hallucination risk — verify
> against authoritative sources before relying on them. Securities law (SEC registration,
> SEBI filings, MAS licensing) and tax advice (IRC § 83(b) filing deadlines, EMI
> valuations, ESOP trust compliance) are beyond the scope of this skill and require
> specialist counsel.

---

## Purpose and Scope

This skill drafts comprehensive founders agreements from scratch or accelerates
existing drafts. It defines equity allocation, control mechanics, founder duties,
vesting schedules, IP assignment, departure mechanics, dispute resolution, and
exit provisions. All drafts are market-standard, playbook-integrated, and
jurisdiction-aware, with explanatory notes written for non-lawyer founders.

**Covers:**

- Cap table initialization and share authorization structure
- Founder equity split (equal, role-weighted, or contribution-weighted)
- Vesting schedule mechanics: 4-year / 1-year cliff baseline with alternatives
- Single-trigger and double-trigger acceleration on change of control and termination
- Intellectual property assignment to company with pre-existing IP carve-outs
- Moral rights and work-made-for-hire treatment by jurisdiction
- Role definitions, decision-making authority, and reserved matters
- Capital contribution requirements (cash, IP, services) and valuation methodology
- Non-compete, non-solicitation, and confidentiality obligations by jurisdiction
- Good Leaver / Bad Leaver definitions and departure mechanics
- Redemption and buyback rights with valuation methodology
- Deadlock resolution mechanisms (escalation, mediation, shotgun clauses)
- Dissolution and wind-down procedures and survival provisions
- Multi-jurisdiction formation guidance: Delaware C-Corp, UK Ltd, Singapore Pte Ltd, India Private Limited
- Investor-readiness checklist for Series A due diligence
- Quality-verified output with Glass Box audit trail and confidence scoring

**Does not:**

- Provide legal advice or replace qualified corporate counsel
- Draft stock option plans or employee equity incentive plans (see legalcode-equity-incentive-plan-drafter)
- Draft investor side documents (term sheets, SAFEs, investor rights agreements, shareholder agreements)
- Advise on securities law compliance (SEC registration, SEBI/MAS filings, Regulation D exemptions)
- Draft employment agreements or independent contractor agreements
- Advise on tax structuring (IRC § 83(b) elections, EMI valuations, ESOP trustee obligations)
- Apply to one jurisdiction exclusively — jurisdiction-aware with [JURISDICTION-SPECIFIC] markers

**Related skills:**

- `legalcode-shareholders-agreement-review` — Review an existing shareholders agreement
- `legalcode-term-sheet-analysis` — Analyze term sheet economics and control provisions
- `legalcode-master-services-agreement` — Draft or review MSA for service engagements
- `legalcode-nda-triage` — Screen non-disclosure agreements for founder relationships

---

## Jurisdiction and Governing Law

This skill is jurisdiction-aware. Every founders agreement section that differs
materially across jurisdictions is marked **[JURISDICTION-SPECIFIC]** with a summary
of how the analysis changes. The skill supports four primary formation jurisdictions:

| Jurisdiction          | Key Framework                          | IP Assignment                                                              | Vesting Mechanics                                              | Non-Compete                                                       |
| --------------------- | -------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Delaware C-Corp**   | DGCL (Title 8)                         | Assignment agreement; § 2870 carve-out (CA employees)                      | Reverse vesting + repurchase right                             | Enforceable if reasonable; CA ban applies to CA employees         |
| **UK Ltd**            | Companies Act 2006; CDPA 1988          | Must be in writing, signed (CDPA § 90(3)); moral rights waiveable only     | Restricted stock + buyback right; or growth shares             | Enforceable if reasonable in scope, geography, duration           |
| **Singapore Pte Ltd** | Companies Act (Cap. 50)                | Employer owns inventions made in normal duties (Patents Act § 49)          | Restricted share scheme; ESOP via trust or direct grants       | Blue Pencil doctrine — courts sever unreasonable terms            |
| **India Pvt Ltd**     | Companies Act 2013; Copyright Act 1957 | Copyright Act § 17: employer first owner for works in course of employment | Vesting via contractual stock option plan; ESOP SEBI Reg. 2021 | Void post-termination (Contract Act § 27); only during employment |

[JURISDICTION-SPECIFIC] When working in a jurisdiction outside the four above, research:

- Mandatory employee IP rights (many jurisdictions have statutory employee inventor rights)
- Enforceability of buyback and redemption clauses (some jurisdictions restrict company self-purchase)
- Non-compete enforceability standards (varies from total ban to reasonableness test to blue pencil)
- Share transfer restriction formalities (many require conspicuous notice; see DGCL § 202)
- Founder equity and option taxation events and rates

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming intent, the workflow pauses and asks when:

- The answer changes the direction of the draft
- Multiple valid approaches exist and the founders' preferences matter
- Jurisdiction-specific choices require founder input
- Equity split or governance choices have strategic implications for investor relations

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

- **Founding team description**: Names, roles, proposed equity percentages, jurisdiction
- **Existing draft**: A partial or complete founders agreement in any format (PDF, DOCX, pasted text)
- **Data room documents**: Articles of incorporation, cap table, prior term sheets, IP assignment agreements
- **Minimal brief**: "Three founders, Delaware C-Corp, equal split, pre-seed stage"

If minimal input is provided, proceed to Step 2 immediately to gather context.

### Step 2: Interactive Clarification

**⟁ CLARIFY** — Before drafting, gather these inputs. Present as structured options
where possible. Skip any question already answered by the user's input.

**1. Founding team composition and equity philosophy?**

- Options: **Equal split** (e.g., 33/33/33 for three founders — simple but may lack conviction for investors), **Role-weighted** (CEO 40%, CTO 35%, COO 25% — accounts for leadership premium), **Contribution-weighted** (accounts for pre-existing IP, capital, early customers), **Negotiated** (founders have already agreed to specific percentages)
- _Why this matters_: Equity philosophy drives share authorization, investor narrative, and future dilution dynamics. Investors often view equal splits as a signal of indecision about leadership.

**2. Company stage and nearest financing event?**

- Options: **Pre-seed / bootstrapped** (no external investors planned in 6 months), **Seed round planned** (≤ 12 months), **Series A expected** (≤ 24 months), **Already seed-funded** (existing investors in the cap table)
- _Why this matters_: Market-standard vesting terms and option pool sizes are stage-dependent. Seed-stage investors typically expect 4-year / 1-year cliff vesting with 10–15% pre-money option pool.

**3. Governing law and incorporation jurisdiction?**

- Options: **Delaware C-Corp** (default for US VC-funded startups), **UK Ltd** (England & Wales), **Singapore Pte Ltd** (Southeast Asia hub), **India Private Limited** (domestic-first or FEMA compliance needed), **Other** (specify)
- _Why this matters_: Statutory defaults for IP ownership, buyback mechanics, preference share enforceability, and non-compete validity differ materially across jurisdictions.

**4. Founder roles and contribution types?**

- Options: **Clearly defined** (distinct roles with no overlap), **Partial overlap** (technical co-founders share code ownership), **Undefined** (roles to be established post-incorporation), **Role includes pre-existing IP** (founder bringing prior-developed technology or customer relationships)
- _Why this matters_: Pre-existing IP carve-outs, role scope for IP assignment, and non-compete geographic scope all depend on role definition.

**5. Any existing investor commitments, term sheets, or SAFE agreements?**

- Free text: Investor name, investment amount, SAFE cap/discount, pro-forma ownership, any specific rights demanded (board seats, anti-dilution, information rights, pro-rata)
- _Why this matters_: The founders agreement must be compatible with any existing investor rights. Governance provisions, drag-along thresholds, and option pool reservations must align with SAFE/term sheet terms.

**6. Any sensitive factors?**

- Options: **Founder has prior employer IP concerns** (may have conflict with former employer's IP), **International co-founder** (one or more founders are non-residents), **Existing entity to be reorganized** (this is not a greenfield founding), **Academic/university spinout** (IP assignment from university required)
- _Why this matters_: These factors require additional IP assignment diligence, foreign investment compliance (FEMA, CFIUS), or university technology transfer office involvement.

If the user provides partial context, state assumptions explicitly:

> _"Assuming three founders with an equal equity split, Delaware C-Corp, pre-seed stage, and no existing investor commitments. Let me know if any of these differ."_

---

### Step 3: Load Playbook

Check for an organizational equity/governance playbook in local settings (e.g.,
`equity-playbook.local.md`, `founder-terms.local.md`, `investor-positions.local.md`).

The playbook should define standard positions for:

| Parameter                     | Playbook Value | Market Standard Fallback                                     |
| ----------------------------- | -------------- | ------------------------------------------------------------ |
| Vesting schedule              | [custom]       | 4-year / 1-year cliff                                        |
| Cliff percentage              | [custom]       | 25% at cliff                                                 |
| Acceleration (single-trigger) | [custom]       | 25–50% on change of control                                  |
| Acceleration (double-trigger) | [custom]       | 100% on CoC + involuntary termination within 18 months       |
| Anti-dilution type            | [custom]       | Broad-based weighted average                                 |
| Drag-along threshold          | [custom]       | 66–75% of voting stock                                       |
| Option pool size (pre-money)  | [custom]       | 10–15% (seed), 15–20% (Series A)                             |
| Good Leaver repurchase price  | [custom]       | Fair market value for vested; cost for unvested              |
| Bad Leaver repurchase price   | [custom]       | Lower of cost or fair market value                           |
| Non-compete duration          | [custom]       | 12 months post-departure (UK); 1–2 years (US if enforceable) |

**If no playbook exists**: Use the market-standard benchmarks above and state this
explicitly in the Glass Box audit trail: `playbook_used: "Market standards (NVCA/BVCA/AIF)"`.

---

### Step 4: Gather Jurisdiction Authority

Research and compile relevant legal authority for the identified governing jurisdiction.

**With legalcode-mcp connected:**
Search for: `[jurisdiction] founders agreement [specific clause type]` — e.g., `"Delaware DGCL Section 151 preferred stock mechanics"`, `"UK Companies Act 2006 Section 994 unfair prejudice"`.

Save the most relevant results to `/tmp/legalcode-founders-agreement-research.md`.

**Without legalcode-mcp:**
Rely on jurisdiction-specific markers below (marked [VERIFY]) and note in the Glass Box:
`legalcode_mcp: "Not connected — citations require independent verification"`.

**[JURISDICTION-SPECIFIC] Key authority by jurisdiction:**

**Delaware C-Corp:**

- DGCL § 141 — Board authority and director duties [VERIFY]
- DGCL § 151 — Authorized stock and preferred share mechanics [VERIFY]
- DGCL § 202 — Transfer restrictions (must be conspicuously noted on share certificates) [VERIFY]
- DGCL § 122(18) (eff. August 1, 2024) — Stockholder governance agreements expressly authorized [VERIFY]
- DGCL § 262 — Appraisal rights (triggered by certain mergers) [VERIFY]
- IRC § 83 / Treas. Reg. § 1.83-7 — Taxation of property received for services [VERIFY]
- Cal. Lab. Code § 2870 — California employee IP carve-out (if any founder is California-based) [VERIFY]
- Cal. Bus. & Prof. Code § 16600 (as amended by AB 1076, eff. January 2024) — Non-compete ban in California [VERIFY]

**UK Ltd:**

- Companies Act 2006 §§ 168–170 — Director duties (loyalty, care, conflicts) [VERIFY]
- Companies Act 2006 § 994 — Unfair prejudice remedy (_O'Neill v Phillips_ [1999] UKHL 24) [VERIFY]
- Companies Act 2006 §§ 561–577 — Pre-emption rights on allotment [VERIFY]
- CDPA 1988 § 90(3) — IP assignment must be in writing and signed [VERIFY]
- CDPA 1988 §§ 77–89 — Moral rights (cannot be assigned; only waived) [VERIFY]
- Employment Rights Act 1996 — Employee protections applicable to founder-employees [VERIFY]
- HMRC EMI — Enterprise Management Incentive options for UK Qualifying Companies [VERIFY]

**Singapore Pte Ltd:**

- Companies Act (Cap. 50) § 76B — Share buyback; § 76F — Solvency requirements [VERIFY]
- Companies Act (Cap. 50) § 161 — Director's duty of loyalty and care [VERIFY]
- Patents Act (Cap. 221) § 49 — Employer owns employee inventions made in normal duties [VERIFY]
- Employment Act (Cap. 91A) — Minimum employment protections for founders who are employees [VERIFY]
- ACRA — Singapore companies must file annual returns with the Accounting and Corporate Regulatory Authority [VERIFY]

**India Private Limited:**

- Companies Act 2013 §§ 43–47 — Share capital, voting rights, and preference share mechanics [VERIFY]
- Companies Act 2013 § 56 — Transfer of shares requires execution of Form SH-4 [VERIFY]
- Copyright Act 1957 § 17 — Employer is first owner of copyright for works made in course of employment [VERIFY]
- Patents Act 1970 § 6 — Who may apply for patent (inventor or assignee) [VERIFY]
- Contract Act 1872 § 27 — Non-compete post-termination is void [VERIFY]
- FEMA Non-Debt Instruments Rules 2019 — Foreign investment restrictions and pricing guidelines [VERIFY]
- SEBI (Share Based Employee Benefits and Sweat Equity) Regulations 2021 — ESOP compliance for listed companies [VERIFY]

---

### Step 5: Define Cap Table and Equity Structure

Draft the equity structure before writing any clauses. An unambiguous cap table
is the foundation of every founders agreement.

**⟁ CLARIFY** — Confirm these cap table parameters:

1. **Total authorized shares?**
   - Delaware default: 10,000,000 shares authorized (avoids higher franchise tax)
   - UK: Unlimited authorized share capital (no authorized limit required)
   - Singapore / India: Specify in Memorandum of Association
   - Market standard: 10,000,000 or 20,000,000 (Delaware); 1,000 or 10,000 (UK/SG/IN)

2. **Share classes?**
   - **Pre-seed**: Common stock only (or Ordinary shares) — no preferred yet
   - **Seed with SAFE/convertible notes**: Common + anticipated preferred on conversion
   - **Series A contemplated**: Common + Preferred (with anti-dilution, liquidation preference mechanics)

3. **Option pool size and timing?**
   - Pre-money pool: Dilutes founders before investor conversion
   - Post-money pool: Dilutes investors equally

**Standard Pre-Seed Cap Table Template:**

```
| Holder | Share Class | Shares | Ownership (Pre-Option Pool) | Ownership (Post-Option Pool) |
|--------|-------------|--------|----------------------------|------------------------------|
| Founder A (CEO) | Common | [X] | [%] | [%] |
| Founder B (CTO) | Common | [X] | [%] | [%] |
| Founder C (COO) | Common | [X] | [%] | [%] |
| Employee Option Pool | Common (reserved) | [X] | — | [%] |
| **TOTAL** | | **[X]** | **100%** | **100%** |
```

**Scenario Modeling — Founder Economics Under Exit Scenarios:**

Before finalizing the equity split, model founder economics under three exit scenarios.
This prevents surprise dilution and aligns founder expectations before investor entry.

| Scenario                | Exit Amount | Investor Preference (est.) | Founder A Net | Founder B Net | Founder C Net |
| ----------------------- | ----------- | -------------------------- | ------------- | ------------- | ------------- |
| Down (50% of seed val.) | $[X]        | $[pref]                    | $[net]        | $[net]        | $[net]        |
| Flat (at seed val.)     | $[X]        | $[pref]                    | $[net]        | $[net]        | $[net]        |
| Up (3× seed val.)       | $[X]        | $[pref]                    | $[net]        | $[net]        | $[net]        |

> _Insert actual numbers once cap table and anticipated investor terms are confirmed._

---

### Step 6: Draft Core Sections

Draft each section using the **section-by-section analysis format** below. For every
section, assess it as GREEN (market-standard), YELLOW (negotiate/review), or RED
(investor concern or legal risk). Include explanatory founder notes (EN) for each
clause.

---

#### Section 1: Equity Allocation and Vesting Schedule

**Section Purpose**: Document the founding team's equity split and the vesting
schedule that governs when each founder earns their shares.

**⟁ CLARIFY** — Choose vesting structure:

- **Reverse vesting** (Delaware standard): Founder receives all shares at founding but
  company holds repurchase right that lapses over the vesting schedule. Shares are
  "issued" immediately — important for IRC § 83(b) elections.
- **Forward vesting** (UK/SG/IN common): Shares or options granted in tranches over time.
  No shares issued until each tranche vests.

**Standard 4-Year / 1-Year Cliff Language:**

```
Vesting Schedule. Each Founder's shares shall vest as follows:
(a) No shares shall vest during the first twelve (12) months following the Commencement
    Date (the "Cliff Period").
(b) Upon completion of the Cliff Period, twenty-five percent (25%) of the total shares
    allocated to such Founder shall vest.
(c) Following the Cliff Period, the remaining seventy-five percent (75%) of such
    Founder's shares shall vest in equal monthly installments over the subsequent
    thirty-six (36) months, such that all shares shall be fully vested upon the
    fourth anniversary of the Commencement Date.
```

**Classification:**

- 4-year / 1-year cliff = **GREEN** (market standard; NVCA, BVCA, AIF norm)
- 3-year / 6-month cliff = **YELLOW** (below market; some seed investors accept for experienced founders)
- No vesting or > 5-year vesting = **RED** (investor red flag; signals misalignment or inexperience)

**Founder Explanatory Note (EN)**: _Vesting means you earn your shares gradually over time rather than all at once. The 1-year cliff means you must stay for a full year before you own any shares — this protects your co-founders if one of you leaves early. After the cliff, you earn roughly 1/48th of your shares each month. If the company is sold while you are still vesting, acceleration provisions (below) determine how many unvested shares you receive._

**[JURISDICTION-SPECIFIC] IRC § 83(b) Election (US Only)**: If shares are subject to
a repurchase right (reverse vesting), each US-resident founder must file an IRC § 83(b)
election with the IRS **within 30 days** of receiving the restricted shares. Failure to
elect means each vesting tranche triggers ordinary income tax at the then-current fair
market value. [VERIFY] _This is tax advice — refer to specialist counsel._

---

#### Section 2: Acceleration of Vesting

**Section Purpose**: Specify when unvested shares accelerate (vest immediately)
upon trigger events such as company sale or involuntary founder termination.

**Single-Trigger Acceleration (CoC Only):**

```
Single-Trigger Acceleration. In the event of a Change of Control, [X]% of each
Founder's then-unvested shares shall immediately vest upon the consummation of
such Change of Control transaction, without regard to continued service.
```

**Double-Trigger Acceleration (CoC + Termination):**

```
Double-Trigger Acceleration. If, within [12/18] months following a Change of
Control, a Founder's service is terminated by the Company (or its successor)
without Cause, or such Founder resigns for Good Reason, then 100% of such
Founder's then-unvested shares shall immediately vest.
```

**Classification:**

- Double-trigger (100% on CoC + involuntary termination within 18 months) = **GREEN** (market standard; NVCA preferred; protects founders and does not impede deals)
- Single-trigger (25–50% on CoC alone) = **YELLOW** (acceptable for seed-stage; some acquirers object; may reduce deal attractiveness)
- Single-trigger (100% on CoC) = **RED** (investor red flag; reduces deal attractiveness; acquirer will demand escrow or clawback)
- No acceleration = **YELLOW** (acceptable at pre-seed; problematic for seed+ stage)

**EN**: _Single-trigger acceleration means your remaining unvested shares automatically vest when the company is sold — even if you stay on after the sale. Double-trigger requires two things to happen: the sale AND that you are then fired or forced out without a fair reason. Investors generally prefer double-trigger because it keeps founders incentivized after the acquisition._

**⟁ CLARIFY** — Acceleration type and percentage:

- Double-trigger (100%) — market standard recommendation
- Single-trigger (25% on CoC) — discuss trade-offs with founders
- Founder-specific acceleration (different terms per founder based on role risk)

---

#### Section 3: Intellectual Property Assignment

**Section Purpose**: Ensure the company owns all IP necessary for its business,
while protecting founders from inadvertently assigning unrelated personal IP.

**Standard Assignment Clause:**

```
IP Assignment. Each Founder hereby irrevocably assigns, transfers, and conveys to
the Company, its successors and assigns, all right, title, and interest in and to
any and all Intellectual Property Rights that are or were:
(a) developed by the Founder in the course of their duties to the Company;
(b) developed using the Company's materials, equipment, facilities, or Confidential
    Information; or
(c) related to the Company's current or reasonably anticipated business activities,
    whether or not developed during normal business hours.

"Intellectual Property Rights" means all patents, copyrights, trade secrets,
trademarks, moral rights, and other proprietary rights worldwide.
```

**Pre-Existing IP Carve-Out:**

```
Pre-Existing IP. The assignment in Section [X] does not apply to any Intellectual
Property Rights that: (a) were created solely by the Founder before their
affiliation with the Company; (b) do not incorporate or use any of the Company's
Confidential Information or resources; and (c) are listed in Exhibit [A] to this
Agreement (the "Pre-Existing IP Disclosure").

Each Founder shall complete and attach Exhibit [A] at the time of execution of
this Agreement, disclosing all material Pre-Existing IP. Failure to disclose
material Pre-Existing IP shall not affect the Company's ownership of IP assigned
above.
```

**Classification:**

- Clear assignment + pre-existing IP disclosure exhibit = **GREEN**
- Assignment without scope limitation on personal projects = **YELLOW** (overly broad; founder may resist; investor due diligence will flag)
- No IP assignment clause = **RED** (company may not own its technology; investor deal-breaker at Series A)
- Assignment of IP developed before founding without written disclosure exhibit = **RED** (creates disputed IP claims at exit)

**EN**: _This clause means the company owns the code, inventions, and designs you create while working on it. The carve-out protects your personal side projects that have nothing to do with the business — but you need to list them in Exhibit A. If you don't list them, the company could claim them._

**[JURISDICTION-SPECIFIC] Moral Rights (UK):**
UK copyright law gives authors "moral rights" (right of attribution and integrity) that
cannot be transferred — they can only be waived. Add the following for UK founders:

```
Moral Rights Waiver (UK). Each Founder, to the fullest extent permitted by the
Copyright, Designs and Patents Act 1988, irrevocably and unconditionally waives all
moral rights in and to any works assigned to the Company under this Agreement.
```

Per CDPA 1988 §§ 77–89, moral rights cannot be assigned — only waived. [VERIFY]

**[JURISDICTION-SPECIFIC] California Employee Carve-Out (US):**
If any founder is California-based, the following notice is mandatory per California
Labor Code § 2870. Failure to include this notice renders the IP assignment unenforceable
against California employees: [VERIFY]

```
California Notice. The IP assignment above shall not apply to any invention that
qualifies fully under California Labor Code Section 2870, as follows: an invention
that the Founder developed entirely on the Founder's own time without using the
Company's equipment, supplies, facilities, or trade secret information, and that
does not relate at the time of conception or reduction to practice to the Company's
business or to the Company's actual or demonstrably anticipated research or
development; and does not result from any work performed by the Founder for the
Company.
```

---

#### Section 4: Role Definitions and Decision-Making Authority

**Section Purpose**: Define each founder's title, responsibilities, and authority
level to prevent governance disputes as the company scales.

**Role Definition Framework:**

```
Founder Roles and Authority.
(a) [Founder A] shall serve as Chief Executive Officer and shall have responsibility
    for [strategic direction, investor relations, fundraising, business development].
(b) [Founder B] shall serve as Chief Technology Officer and shall have responsibility
    for [product architecture, engineering team, technical roadmap].
(c) [Founder C] shall serve as Chief Operating Officer and shall have responsibility
    for [operations, finance, human resources, legal and compliance].

Each Founder shall devote [full-time / substantially all of their working time] to
the Company. Any paid outside activities (consulting, advisory roles) require prior
written approval from the other Founders.
```

**Decision-Making Framework:**

```
Decisions Requiring Unanimous Founder Approval:
(i) Issuance of new equity or debt instruments;
(ii) Sale, merger, or liquidation of the Company;
(iii) Appointment or removal of executive officers;
(iv) Amendment of this Agreement or the Company's constitutional documents;
(v) Capital expenditures exceeding $[threshold] per transaction;
(vi) Entry into contracts exceeding $[threshold] per annum;
(vii) Commencement of material litigation or settlement of claims;
(viii) Material change in the Company's business scope.

All other operational decisions may be made by majority vote or delegated to
the relevant Founder within their area of responsibility.
```

**Classification:**

- Clear role definitions + reserved matters list = **GREEN**
- Vague role descriptions ("Founder A will do strategy") = **YELLOW** (leads to disputes; specify scope)
- No decision-making framework = **RED** (operational disputes will paralyze the business)

**EN**: _This section defines who does what and who gets a say in major decisions. The "Reserved Matters" list protects every founder — no one can sell the company, issue new shares, or spend large amounts without everyone agreeing. For day-to-day decisions, each of you acts within your area._

---

#### Section 5: Capital Contributions and Expense Policy

**Section Purpose**: Document each founder's initial contribution (cash, IP, services)
and establish an expense reimbursement policy.

**Standard Contribution Table:**

```
| Founder | Cash Contribution | IP Contribution | Services Commitment | Total Deemed Value |
|---------|------------------|-----------------|---------------------|-------------------|
| [A] | $[X] | [Pre-existing IP listed in Exhibit A] | Full-time | $[X] |
| [B] | $[X] | [Technical architecture] | Full-time | $[X] |
| [C] | $[X] | [None] | Full-time | $[X] |
```

**Expense Reimbursement:**

```
Expense Policy. The Company shall reimburse reasonable and necessary business
expenses incurred by Founders, subject to:
(a) expenses below $[threshold] per month are approved by any Founder;
(b) expenses between $[threshold] and $[higher threshold] require approval of
    [two / all] Founders;
(c) expenses above $[higher threshold] require Board approval;
(d) all expenses must be submitted with receipts within [30] days of incurrence.
```

**Classification:**

- Documented contributions with IP valuation methodology = **GREEN**
- Cash contributions only (no IP or services documented) = **YELLOW** (incomplete; investor diligence will ask)
- Undocumented IP contributed by a founder = **RED** (company IP ownership uncertain; Series A blocker)

---

#### Section 6: Non-Compete, Non-Solicitation, and Confidentiality

**Section Purpose**: Protect the company's competitive position and confidential
information from departing founders.

**Confidentiality (Perpetual for Trade Secrets):**

```
Confidentiality. Each Founder shall maintain in strict confidence all Confidential
Information of the Company, both during their affiliation with the Company and
thereafter. "Confidential Information" means all non-public information relating
to the Company's business, technology, customers, finances, and strategic plans.

Confidentiality obligations with respect to trade secrets shall survive indefinitely.
Confidentiality obligations with respect to other Confidential Information shall
survive for [five (5) / seven (7)] years following departure.
```

**Non-Solicitation (Employees and Customers):**

```
Non-Solicitation. During the Restricted Period, each Founder shall not, directly
or indirectly:
(a) solicit, recruit, or induce any employee or consultant of the Company to
    terminate their relationship with the Company; or
(b) solicit or accept business from any customer or prospective customer of the
    Company that such Founder had material contact with during their last twelve
    (12) months of service.

"Restricted Period" means the period during service and for [twelve (12) / twenty-
four (24)] months following the effective date of departure.
```

**Non-Compete (Jurisdiction-Dependent):**

```
Non-Competition. During the Restricted Period, each Founder shall not, without
prior written consent of the Board, directly or indirectly engage in, own, manage,
operate, control, be employed by, or provide services to any Competing Business
within the Restricted Territory.

"Competing Business" means any business that competes directly with the Company's
[primary product / service category].
"Restricted Territory" means [geographic scope: country / region / worldwide].
"Restricted Period" for non-compete purposes means [twelve (12) / eighteen (18)]
months following departure.
```

**Classification:**

- Non-solicitation (12 months) + reasonable non-compete = **GREEN** (market standard)
- Non-compete > 24 months or worldwide geographic scope = **YELLOW** (may be unenforceable; review by jurisdiction)
- Non-compete applicable to California-resident founders = **RED** (void under Cal. Bus. & Prof. Code § 16600 as amended by AB 1076, eff. January 2024) [VERIFY]
- Non-compete post-termination in India = **RED** (void under Contract Act § 27) [VERIFY]

**EN**: _The confidentiality clause means you cannot share the company's secrets even after you leave. The non-solicitation means you cannot poach the team or customers for a period after leaving. The non-compete restricts you from starting or joining a direct competitor — but in some places like California or India, this type of restriction is unenforceable._

**[JURISDICTION-SPECIFIC] Non-Compete Enforceability Matrix:**

| Jurisdiction                      | Non-Compete During Service | Non-Compete Post-Termination                                              | Key Standard                           |
| --------------------------------- | -------------------------- | ------------------------------------------------------------------------- | -------------------------------------- |
| US (non-CA)                       | Generally enforceable      | Enforceable if reasonable scope, geography, duration                      | State-by-state; check applicable state |
| California                        | Generally enforceable      | **Void** (Cal. Bus. & Prof. Code § 16600; AB 1076 eff. Jan 2024) [VERIFY] | Total ban on post-termination          |
| Minnesota, Oklahoma, North Dakota | Generally enforceable      | **Void** or severely restricted [VERIFY]                                  | Effective ban                          |
| UK                                | Generally enforceable      | Enforceable if reasonable (garden leave common)                           | Restraint of trade test                |
| Singapore                         | Generally enforceable      | Blue Pencil doctrine — courts sever unreasonable terms                    | _Man Financial v Wong_ [2008] [VERIFY] |
| India                             | Generally enforceable      | **Void** (Contract Act § 27) [VERIFY]                                     | Post-termination ban                   |
| Germany                           | Generally enforceable      | Enforceable with compensation (GewO § 74) [VERIFY]                        | Must pay compensation                  |

---

#### Section 7: Departure Mechanics — Good Leaver and Bad Leaver

**Section Purpose**: Define what happens to a founder's shares when they leave
the company, depending on the reason for departure.

**Good Leaver Definition:**

```
Good Leaver. A Founder shall be a "Good Leaver" if their service terminates
by reason of:
(a) death;
(b) Permanent Disability (inability to perform material duties for six consecutive
    months or nine months in any twelve-month period);
(c) termination by the Company without Cause;
(d) resignation for Good Reason (material reduction in role, compensation, or
    authority; relocation without consent; material breach by the Company); or
(e) retirement at age [65] or above with [12] months' notice.
```

**Bad Leaver Definition:**

```
Bad Leaver. A Founder shall be a "Bad Leaver" if their service terminates
by reason of:
(a) voluntary resignation without Good Reason;
(b) termination by the Company for Cause;
(c) material breach of this Agreement (including IP assignment, confidentiality,
    or non-solicitation obligations); or
(d) engaging in Competing Business activity in violation of Section [X].

"Cause" means: (i) conviction of a felony or crime of moral turpitude; (ii) fraud,
embezzlement, or theft from the Company; (iii) gross negligence or willful misconduct;
(iv) material breach of fiduciary duty; (v) material breach of this Agreement that
is not cured within fifteen (15) days after written notice; or (vi) material violation
of the Company's code of conduct.
```

**Repurchase Rights:**

```
Good Leaver Repurchase. Upon a Founder becoming a Good Leaver, the Company shall
have the right (not obligation) to repurchase:
(a) vested shares: at Fair Market Value, determined by an independent valuation
    within [90] days of departure; and
(b) unvested shares: at the lower of cost of acquisition or Fair Market Value.

Bad Leaver Repurchase. Upon a Founder becoming a Bad Leaver, the Company shall
have the right to repurchase all shares (vested and unvested) at the lower of:
(a) the original acquisition cost; or
(b) Fair Market Value at the time of the repurchase election.
```

**Classification:**

- Good Leaver at FMV (vested) / cost (unvested) + Bad Leaver at cost = **GREEN** (market standard)
- Good Leaver at cost for all shares = **YELLOW** (below market; may disincentivize founders)
- No Good Leaver / Bad Leaver distinction (all departures treated equally) = **YELLOW** (unfair to long-serving founders; investor scrutiny)
- Company right to purchase vested shares at cost (Good Leaver) = **RED** (punitive; drives founder conflicts)

**EN**: _Good Leaver means you left for a fair reason (fired unjustly, became ill, died). In that case, the company pays a fair price for your shares. Bad Leaver means you quit without good reason or were fired for serious misconduct. In that case, the company can buy back your shares at cost — which may be much less than they are worth. This protects your co-founders if someone abandons the company._

---

#### Section 8: Buyback Provisions and Valuation Methodology

**Section Purpose**: Establish the mechanics for the company or other founders to
purchase a departing founder's shares at a defined price.

**Buyback Mechanics:**

```
Right of First Refusal. Before any Founder (a "Transferring Founder") may transfer
any shares (other than to a Permitted Transferee), the Transferring Founder must
first offer such shares to:
(a) the Company, at the price and on the terms of the proposed third-party transfer
    (the "ROFR Price"); and
(b) if the Company declines within [10] business days, the remaining Founders on
    a pro-rata basis, at the ROFR Price.

If neither the Company nor the remaining Founders exercise their right within [20]
business days of notice, the Transferring Founder may complete the proposed transfer
to the third party at no less than the ROFR Price.
```

**Valuation Methodology (Dispute Context):**

```
Valuation Methodology. Where Fair Market Value is required under this Agreement
(including upon repurchase of a Good Leaver's shares), it shall be determined as:
(a) by mutual agreement of the Founders within [30] days of the triggering event; or
(b) failing agreement, by an independent valuation firm mutually selected by the
    parties within [15] days; or
(c) failing selection, by the independent auditor of the Company applying a
    [revenue multiple / EBITDA multiple / DCF / last funding round price] methodology.

The cost of any independent valuation shall be shared equally between the Company
and the departing Founder.
```

**Classification:**

- ROFR at third-party offer price = **GREEN** (market standard; NVCA, BVCA)
- ROFR at formula price below FMV = **YELLOW** (may be challenged in court; founder may resist)
- Company redemption right with no ROFR procedure = **RED** (forced buyout risk; may not comply with corporate law)

**[JURISDICTION-SPECIFIC] Share Buyback Restrictions:**

- **Delaware**: Company may repurchase its own shares unless prohibited by the Certificate of Incorporation. No solvency test required, but board must act in good faith. [VERIFY]
- **UK**: Share buyback from a shareholder requires shareholder approval (Companies Act 2006 § 694) and may require a solvency statement. [VERIFY]
- **Singapore**: Companies Act § 76B — buyback requires shareholder approval by ordinary resolution; cannot exceed 10% of total issued shares in one year (treasury shares); solvency requirement applies (§ 76F). [VERIFY]
- **India**: Companies Act 2013 § 68 — buyback permitted up to 25% of paid-up capital; requires board/shareholder resolution and compliance with SEBI Buyback Regulations 2018. [VERIFY]

---

#### Section 9: Deadlock Resolution

**Section Purpose**: Establish a structured escalation process when founders
cannot reach agreement on a required decision.

**Escalation Framework:**

```
Deadlock Resolution. If the Founders are unable to reach agreement on a Reserved
Matter after good-faith negotiation, the following process applies:

Level 1 — Internal Escalation: Any Founder may declare a deadlock in writing.
The Founders shall convene a meeting within [5] business days and attempt resolution
through good-faith discussion.

Level 2 — Mediation: If Level 1 fails within [15] days, the parties shall engage a
mutually agreed mediator (or, failing agreement on a mediator within [5] days,
a mediator appointed by [JAMS / Centre for Effective Dispute Resolution (CEDR) /
Singapore Mediation Centre]) for a [1]-day mediation session.

Level 3 — Buy-Sell (Shotgun) Clause: If mediation fails, any Founder may invoke
the Buy-Sell clause. The invoking Founder shall name a price per share (the "Trigger
Price"). The other Founders, within [30] days, shall elect to either:
(a) purchase the invoking Founder's shares at the Trigger Price; or
(b) sell their own shares to the invoking Founder at the Trigger Price.

Level 4 — Dissolution: If no Founder elects within [30] days of the Trigger Price
notice, the Founders shall take all steps necessary to wind up and dissolve the
Company.
```

**Classification:**

- 4-level escalation with shotgun clause fallback = **GREEN** (provides certainty without litigation)
- Mediation only (no final resolution mechanism) = **YELLOW** (may not resolve fundamental disagreements)
- No deadlock provision = **RED** (business paralysis risk; forces expensive litigation)

**EN**: _The deadlock clause is a last resort for when you cannot agree on something important. The 'shotgun' mechanism (Level 3) is powerful — whoever names the price must be willing to buy OR sell at that price. This creates an incentive to name a fair price. If no one wants to buy or sell, the company dissolves._

---

#### Section 10: Dissolution and Wind-Down

**Section Purpose**: Establish an orderly process for dissolving the company and
distributing its remaining assets.

**Dissolution Trigger Events:**

```
Events Triggering Dissolution. The Company shall be dissolved upon:
(a) unanimous written consent of all Founders;
(b) failure to resolve a deadlock pursuant to Section [Deadlock Resolution] above;
(c) [insolvency / inability to pay debts as they fall due]; or
(d) material breach by a Founder that cannot be remedied and that the remaining
    Founders unanimously elect to treat as a dissolution trigger.
```

**Distribution Waterfall:**

```
Dissolution Distribution. Upon dissolution, the Company's assets shall be applied
in the following order:
(a) payment of all outstanding debts, liabilities, and obligations;
(b) establishment of reserves for contingent liabilities;
(c) distribution of remaining assets to shareholders pro rata to their equity
    ownership, subject to any liquidation preference applicable to preferred shares.
```

**Survival Provisions:**

```
Survival. The following obligations survive dissolution of the Company:
(a) IP assignment obligations (perpetual);
(b) confidentiality obligations with respect to trade secrets (perpetual);
(c) confidentiality obligations with respect to other Confidential Information
    ([5] years from dissolution);
(d) non-solicitation obligations ([12] months from dissolution).
```

**Classification:**

- Defined dissolution triggers + distribution waterfall + survival provisions = **GREEN**
- No survival provisions for IP assignment = **RED** (company may lose IP ownership upon dissolution; acquired assets tainted)
- No distribution mechanism (founders just walk away) = **RED** (exposes founders to personal liability for undistributed obligations)

---

#### Section 11: Multi-Jurisdiction Formation Guidance

**Section Purpose**: Advise founders on the key trade-offs between formation
jurisdictions before the founders agreement is signed.

**Formation Decision Matrix:**

| Factor                         | Delaware C-Corp               | UK Ltd                             | Singapore Pte Ltd                        | India Pvt Ltd                |
| ------------------------------ | ----------------------------- | ---------------------------------- | ---------------------------------------- | ---------------------------- |
| **US VC Funding**              | ✅ Standard                   | ⚠️ Requires flip to Delaware       | ⚠️ May require flip                      | ❌ Difficult                 |
| **EU/UK Investor Base**        | ⚠️ May need UK HoldCo         | ✅ Native                          | ⚠️ Remote                                | ❌ Difficult                 |
| **APAC/SEA Investor Base**     | ⚠️ Remote                     | ⚠️ Remote                          | ✅ Standard                              | ⚠️ India-only                |
| **Option Plan Simplicity**     | ✅ Stock options (IRC § 422)  | ✅ EMI options (HMRC approved)     | ✅ ESOP via trust                        | ⚠️ Complex (SEBI regs)       |
| **Franchise / Annual Tax**     | ⚠️ Delaware franchise tax     | ✅ Corporation tax only            | ✅ Low annual costs                      | ✅ Moderate compliance       |
| **IP Ownership Clarity**       | ✅ Assignment standard        | ✅ CDPA § 90 + employer default    | ✅ Patents Act § 49                      | ✅ Copyright Act § 17        |
| **Non-Compete Enforceability** | ⚠️ State-by-state (CA banned) | ✅ Reasonable terms enforceable    | ✅ Blue Pencil doctrine                  | ❌ Post-termination void     |
| **Dissolution Flexibility**    | ✅ Board can authorize        | ⚠️ Requires shareholder resolution | ⚠️ Requires court or members' resolution | ⚠️ Regulatory steps required |

**[JURISDICTION-SPECIFIC] Delaware C-Corp Structural Note:**

- Post-_Moelis_ legislative fix: DGCL § 122(18) (effective August 1, 2024) expressly
  authorizes stockholder governance agreements covering board size, director nominations,
  and transaction approval requirements. Founders agreements that pre-date this amendment
  should be reviewed against the new statutory framework. [VERIFY]

**[JURISDICTION-SPECIFIC] UK "Flip" to Delaware:**
UK-incorporated companies planning US VC funding often execute a "flip" — reincorporating
to a Delaware C-Corp while preserving UK subsidiary operations. A founders agreement
signed for the UK entity may need to be replaced or novated upon flip. Plan the flip
timeline before signing long-term founders agreements with UK entities.

---

### Step 7: Interaction Analysis

Before delivering the draft, analyze how the key provisions interact. Inconsistent
provisions are among the most common founders agreement defects.

**Mandatory Interaction Checks:**

| Check                       | Analysis Required                                                                                                                                   |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Vesting + Acceleration      | Does cliff vesting interact correctly with single/double-trigger? Model full vesting + acceleration + exit for each founder                         |
| IP Assignment + Role Scope  | Does the IP assignment scope match the role definition scope? Overly broad IP assignment may capture personal projects                              |
| Non-Compete + Jurisdiction  | Does the governing law support the non-compete duration and geographic scope? Flag any California-resident founders                                 |
| Buyback + Corporate Law     | Does the buyback mechanics comply with share repurchase rules in the governing jurisdiction (solvency, shareholder approval, 10% treasury limit)?   |
| Good Leaver FMV + Valuation | Does the Good Leaver valuation methodology produce a practically determinable result, or could it lead to perpetual dispute?                        |
| Option Pool + Anti-Dilution | If seed investors are already in the cap table, does the option pool reservation interact with any anti-dilution protection?                        |
| Dissolution + IP Survival   | Does the IP assignment survive dissolution? Are there surviving obligations that bind founders after the company ceases to exist?                   |
| Reserved Matters + Deadlock | Are reserved matters clearly linked to the deadlock resolution procedure? Can a non-reserved matter deadlock the company without a resolution path? |

---

### Step 8: Multi-Founder Impact Map

Document how each major provision affects each founder and other stakeholders.
This prevents one founder from benefiting at another's expense without awareness.

| Stakeholder                 | Role                                | Sections Affected                                   | Impact                                                                     | Action Required                                                    |
| --------------------------- | ----------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Founder A (CEO)             | Lead + primary equity holder        | All                                                 | Primary — most governance authority; acceleration risk                     | Review and sign                                                    |
| Founder B (CTO)             | Technical lead + IP contributor     | IP Assignment, Vesting, Non-Compete                 | IP carve-out critical; non-compete scope must account for domain expertise | Review Exhibit A carefully; obtain legal advice on IP scope        |
| Founder C (COO)             | Operations + minority equity holder | Capital Contributions, Decision-Making, Good Leaver | Minority protection important; ensure reserved matters protect minority    | Confirm reserved matters sufficient                                |
| Employee Option Pool        | Future hire pool                    | Cap Table, Option Pool                              | Dilution risk; pool size affects future hires                              | Confirm pool size adequate for 18-month hiring plan                |
| Series A Lead (future)      | Investor                            | All (ROFR, Drag-Along, Anti-dilution, Option Pool)  | Must be contractually clean before due diligence                           | Investor-readiness checklist below                                 |
| Key Customers / IP Licensor | Third party                         | IP Assignment, Confidentiality                      | IP assignment must not breach third-party IP rights                        | Confirm no assignment restrictions in customer/licensor agreements |

---

### Step 9: Quality Verification

Before delivering the draft, run all quality checks silently. If any check fails,
revise before delivering.

#### Citation Quality Gates

Run these 5 gates before delivering any output:

| Gate           | Rule                                                                                             | Fail Action                                                       |
| -------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established market practice           | Add citation or mark `[UNVERIFIED — counsel to confirm]`          |
| **Format**     | All statute/regulation citations follow consistent, recognizable format for the jurisdiction     | Fix format: e.g., "DGCL § 151" not "Delaware preferred stock law" |
| **Currency**   | Every cited provision checked for recent amendments                                              | Flag `[CHECK CURRENCY — may have been amended]`                   |
| **Domain**     | Analysis applies only the identified governing jurisdiction's law; no cross-jurisdictional bleed | Remove or clearly flag: "Delaware rule only — UK law differs"     |
| **Confidence** | Uncertainty explicitly stated; no hidden hedging                                                 | Add confidence qualifier per Confidence Scoring framework below   |

#### Self-Interrogation for RED Items

For any provision classified as RED, apply this 3-pass review before delivering:

**Pass 1 — Enforceability Chain:**

- Does the risk follow logically from the cited statute or established principle?
- Would a court in this jurisdiction actually reach this conclusion on these facts?
- What counter-argument will the challenging party's counsel make?

**Pass 2 — Completeness and Interaction:**

- Are all relevant statutes, regulations, and market standards considered?
- Does this provision interact with other clauses in a way that changes the risk?
- Are there regulatory dimensions not yet addressed (tax, securities, employment)?

**Pass 3 — Investor Alignment:**

- Is this provision founder-friendly, investor-friendly, or neutral?
- Under what circumstances might a reasonable investor accept this risk?
- Is the RED classification proportionate to market norms, or is this a YELLOW with mitigations?

Mark the Glass Box audit trail: `self_interrogation: PASS` or `self_interrogation: REVISED`.

#### Confidence Scoring

For each material provision, assign a confidence level:

| Level        | Range     | Meaning                                          | Action                                                |
| ------------ | --------- | ------------------------------------------------ | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, clear statute, no ambiguity         | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments, reasonable minds could differ    | State with reasoning and contra-indicators            |
| **Possible** | 0.40–0.59 | Genuinely uncertain, competing authorities       | Flag for counsel review with both sides               |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                          | Do not assert; flag `[UNCERTAIN — counsel to advise]` |

**Examples for founders agreement context:**

- 4-year / 1-year cliff vesting = **Definite (0.97)** — NVCA/BVCA universal standard; fully statutory
- Double-trigger acceleration (100%) = **High (0.88)** — market standard; specific % varies by negotiation
- Non-compete enforceability in California = **Unlikely (0.05)** — AB 1076 and § 16600 effectively prohibit [VERIFY]
- Non-compete post-termination enforceability in India = **Unlikely (0.10)** — Contract Act § 27 renders void [VERIFY]
- IP assignment carve-out adequacy in cross-employer context = **Possible (0.55)** — fact-specific; requires lawyer review

---

### Step 10: Glass Box Audit Trail

Complete the following audit trail template for every engagement. This provides
full traceability and is shared with the human reviewer.

```yaml
glass_box:
  document: "Founders Agreement — [Company Name] — [Date]"
  document_type: "Founders Agreement"
  founding_team_size: "[number] founders"
  governing_law: "[Delaware / UK / Singapore / India / Other]"
  company_stage: "[Pre-seed / Seed / Series A]"
  playbook_used: "[Playbook name or 'Market standards (NVCA/BVCA/AIF)']"
  draft_basis: "[Organizational playbook / Market standards]"
  sections_drafted:
    - "Section 1: Equity Allocation and Vesting"
    - "Section 2: Acceleration of Vesting"
    - "Section 3: Intellectual Property Assignment"
    - "Section 4: Role Definitions and Decision-Making Authority"
    - "Section 5: Capital Contributions and Expense Policy"
    - "Section 6: Non-Compete, Non-Solicitation, and Confidentiality"
    - "Section 7: Departure Mechanics — Good Leaver and Bad Leaver"
    - "Section 8: Buyback Provisions and Valuation Methodology"
    - "Section 9: Deadlock Resolution"
    - "Section 10: Dissolution and Wind-Down"
  market_benchmarks_applied:
    - "NVCA model vesting terms (US)"
    - "BVCA model documents for early stage investments (UK)"
    - "AIF/SEBI ESOP compliance framework (India)"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-founders-agreement-research.md or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED (legalcode-mcp) or UNVERIFIED]"
    - "[Statute — VERIFIED or UNVERIFIED]"
  case_law_consulted:
    - "[Case — VERIFIED or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  assumptions:
    - "[e.g., Equal founder roles assumed unless specified otherwise]"
    - "[e.g., No existing investors in cap table]"
    - "[e.g., Delaware C-Corp — IRC § 83(b) election advisable within 30 days of share issuance]"
  limitations:
    - "Requires review by qualified corporate counsel before execution"
    - "Securities law compliance (Regulation D, SEC reporting) not addressed"
    - "Tax advice (IRC § 83(b) election deadline, EMI valuations) not addressed"
    - "State-specific non-compete rules for multi-state teams not independently verified"
  reviewer: "AI-assisted — requires qualified corporate counsel review before execution"
```

---

### Step 11: Deliver Output

Assemble the final deliverable in the following format.

---

## Output Format Template

### Founders Agreement Drafting Summary

**Company**: [Company name and incorporation date / date of founding]
**Founders**: [Names, roles, proposed equity percentages]
**Governing Law**: [Jurisdiction]
**Stage**: [Pre-seed / Seed / Series A planned]
**Basis**: [Organizational playbook name / General market standards (NVCA/BVCA/AIF)]
**Date Drafted**: [Date]

---

### Key Provisions Overview

[3–5 sentence summary of cap table, vesting structure, governance framework, and key
protective provisions. Written in plain language for founders.]

---

### Cap Table Summary

| Holder             | Share Class       | Shares  | Pre-Option Pool % | Post-Option Pool % |
| ------------------ | ----------------- | ------- | ----------------- | ------------------ |
| Founder A ([Role]) | Common            | [X]     | [%]               | [%]                |
| Founder B ([Role]) | Common            | [X]     | [%]               | [%]                |
| Founder C ([Role]) | Common            | [X]     | [%]               | [%]                |
| Option Pool        | Common (reserved) | [X]     | —                 | [%]                |
| **TOTAL**          |                   | **[X]** | **100%**          | **100%**           |

**Authorized Stock**: [X] shares | **Option Pool**: [X]% pre-money | **Par Value**: $[0.0001]

---

### Section-by-Section Drafting Notes

[For each section drafted, provide:]

#### [Section Title] — [GREEN / YELLOW / RED] | Confidence: [Level]

**Proposed Language**: [Draft language — quoted]
**Market Standard**: [NVCA / BVCA / AIF benchmark]
**Rationale**: [Why this term was chosen]
**Founder Impact**: [Practical consequence for each founder]
**Alternatives** (if YELLOW or RED):

> Option A: [More founder-friendly language]
> Option B: [Investor-friendly language]
> Fallback: [Compromise position]

---

### Governance Framework

**Board Composition**: [Current structure and anticipated post-seed structure]
**Reserved Matters (Shareholder Level)**: [List of matters requiring unanimous approval]
**Reserved Matters (Board Level)**: [Board-only vetoes, if any]
**Founder Duties**: [Key fiduciary and operational obligations]

---

### Vesting Schedule Summary

| Founder   | Start Date | Cliff Date | Monthly Vesting | Full Vest Date | Acceleration (Single) | Acceleration (Double) |
| --------- | ---------- | ---------- | --------------- | -------------- | --------------------- | --------------------- |
| Founder A | [Date]     | [+12 mo]   | [1/48/month]    | [+48 mo]       | [25–50%]              | [100%]                |
| Founder B | [Date]     | [+12 mo]   | [1/48/month]    | [+48 mo]       | [25–50%]              | [100%]                |
| Founder C | [Date]     | [+12 mo]   | [1/48/month]    | [+48 mo]       | [25–50%]              | [100%]                |

---

### Investor Readiness Checklist

- [ ] Cap table is clean — no prior undocumented founder disputes, side agreements, or oral equity promises
- [ ] Vesting is 4-year / 1-year cliff (market standard); deviations documented with rationale
- [ ] IP assignment to company is in writing, signed, and scope-limited to company business
- [ ] Pre-existing IP is disclosed in Exhibit A — no undisclosed third-party IP claims
- [ ] California-resident founders have § 2870 carve-out included; California § 16600 non-compete exclusion noted
- [ ] UK founders: CDPA § 90(3) compliant written assignment; moral rights waiver included
- [ ] Singapore founders: Companies Act § 76B-compliant buyback mechanics; solvency requirement noted
- [ ] India founders: FEMA Non-Debt Instruments Rules 2019 reviewed for any foreign co-founder
- [ ] Anti-dilution type is broad-based weighted average (NVCA standard) — noted for investor due diligence
- [ ] Drag-along threshold is 66–75% of voting stock
- [ ] Tag-along rights are reciprocal (all shareholders)
- [ ] Option pool reserved at [10–15]% pre-money (seed) or [15–20]% (Series A)
- [ ] Redemption / buyback mechanics are defined with clear valuation methodology
- [ ] Good Leaver / Bad Leaver definitions are clear and specific
- [ ] Deadlock resolution has a final resolution mechanism (shotgun or dissolution)
- [ ] Governing law is clearly stated and matches incorporation jurisdiction
- [ ] Related documents are aligned: employment agreements, option plans, IP assignment agreements
- [ ] IRC § 83(b) elections filed within 30 days of restricted stock grant (US founders only)

---

### Next Steps

- [ ] Founders review all sections and confirm agreement on equity split, vesting, and governance
- [ ] Corporate counsel reviews draft against applicable jurisdiction-specific law
- [ ] IP assignment Exhibit A completed by each founder (pre-existing IP disclosure)
- [ ] Board approval (if board exists or is being constituted)
- [ ] Cap table updated in equity management system (Carta, Capdesk, Ledgy, or similar)
- [ ] IRC § 83(b) elections filed if reverse vesting structure adopted (US founders — **30-day deadline**)
- [ ] Founders agreement signed by all founders and company
- [ ] Copies delivered to company records and each founder
- [ ] Series A readiness review scheduled for [date] before investor outreach

---

### Glass Box Audit Trail

```yaml
[Insert completed glass_box YAML block per Step 10]
```

---

## Quality Assurance Frameworks Reference

### Deviation Severity Classification

Apply to every provision drafted:

| Severity   | Meaning                                     | Examples                                                                                             | Action                                                                        |
| ---------- | ------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **GREEN**  | Market-standard; investor-ready             | 4-year / 1-year cliff; broad-based anti-dilution; ROFR at FMV; double-trigger 100% acceleration      | Draft as proposed; note as standard                                           |
| **YELLOW** | Negotiable variant; within acceptable range | 3-year vesting; single-trigger 25%; non-compete > 12 months in UK                                    | Present alternatives; explain trade-offs                                      |
| **RED**    | Investor concern or legal risk              | No IP assignment; no vesting; California non-compete; § 16600 violation; undisclosed pre-existing IP | Escalate; require corporate counsel review; cannot proceed without resolution |

---

## Anti-Patterns Catalogue

What NOT to do when drafting founders agreements. These are the most common
errors that create founder disputes, investor concerns, and legal risk.

1. **No vesting schedule** — Founder who leaves after 3 months keeps full equity. Investors will demand vesting retroactively at Series A, creating conflict. _Standard: 4-year / 1-year cliff is non-negotiable for investor-backed startups._

2. **IP assignment without scope limitation** — "All IP developed by Founder" captures personal side projects unrelated to the business. Creates founder liability for pre-existing personal projects and may be challenged. _Standard: limit scope to "IP developed in furtherance of the Company's business or using Company resources."_

3. **Missing pre-existing IP disclosure (Exhibit A)** — Founder with prior employer IP conflict or personal IP asset does not disclose it. Company's IP ownership becomes disputed at due diligence. _Standard: mandatory Exhibit A completed at signing._

4. **California non-compete for California-resident founders** — Post-termination non-compete is void under California Business & Professions Code § 16600 (reinforced by AB 1076, effective January 2024). Including it gives false comfort and wastes legal fees. _Standard: omit; rely on non-solicitation and confidentiality instead._

5. **India post-termination non-compete** — Non-compete post-termination is void under Contract Act § 27. Same defect as California — creates false confidence. _Standard: omit; use garden leave or trade secret protection instead._

6. **Equal equity split with no leadership differentiation** — Investors often read equal splits as "founders can't decide who's in charge." No inherent problem, but requires founders to explain the split confidently. _Standard: document the rationale in a founding memo._

7. **Single-trigger 100% acceleration** — Accelerates all unvested shares upon company sale alone. Acquirers typically respond by escrowing or reducing purchase price. Creates adverse deal economics. _Standard: double-trigger acceleration; single-trigger limited to 25–50%._

8. **Good Leaver repurchase at cost (not FMV) for vested shares** — Penalizes a founder who was fired without cause. Creates legal risk (constructive dismissal claims) and reputational harm. _Standard: Good Leaver vested shares repurchased at Fair Market Value._

9. **No deadlock resolution mechanism** — Founders cannot agree on a Reserved Matter; business is paralyzed; expensive litigation follows. _Standard: 4-level escalation with shotgun clause or dissolution trigger._

10. **No IP assignment survival post-dissolution** — Company dissolves; IP assignment clause ends with it; founders claim back IP. Acquirors in distressed M&A find the asset stripped. _Standard: IP assignment survives dissolution indefinitely._

11. **Vesting without IRC § 83(b) election notice** — US founders on reverse vesting are subject to ordinary income tax on each vesting tranche at the then-current FMV unless they file § 83(b) within **30 days**. Missing this window is irrecoverable. _Standard: include § 83(b) deadline warning in plain language; refer to tax counsel._

12. **Buyback mechanics non-compliant with corporate law** — Company buyback right that does not comply with Singapore Companies Act § 76B (solvency, 10% treasury cap) or UK Companies Act 2006 § 694 (shareholder approval) is unenforceable. _Standard: verify buyback mechanics against applicable statutory framework._

13. **Confidentiality term shorter than trade secret life** — 3-year confidentiality on a 20-year technology trade secret. After 3 years, the founder may freely disclose. _Standard: trade secret confidentiality should be perpetual._

14. **Undocumented capital contributions** — Founder A contributes $50,000 cash; not documented; Founder B later disputes it. No remedy without documentation. _Standard: every capital contribution — cash, IP, or services — must be documented and valued in writing at the time of contribution._

15. **Option pool creation timing not negotiated** — Seed investor demands pre-money option pool creation; founders agree without modeling dilution. Founders receive less than expected post-conversion. _Standard: model pre-money vs. post-money pool creation before signing any SAFE or term sheet._

16. **Reserved matters list too broad** — Every routine decision requires unanimous approval. Operational paralysis results before formal governance is established. _Standard: reserved matters cover only fundamental transactions; operational matters delegated to role-responsible founder._

17. **No founder duty provisions** — Founders can pursue competing side projects, engage in self-dealing, or fail to disclose conflicts. _Standard: explicit duty of loyalty, confidentiality, and conflict of interest disclosure._

18. **Governing law does not match formation jurisdiction** — Delaware company governed by New York law; UK company governed by Delaware law. Creates uncertainty about which statutory framework applies. _Standard: governing law must match (or explicitly override) the incorporation jurisdiction._

19. **Founder explanatory notes omitted** — Non-lawyer founders sign a 30-page agreement without understanding what they agreed to. Disputes arise later over "what this clause means." _Standard: provide plain-language Founder Explanatory Notes (EN) for every material clause._

20. **Assuming the agreement is complete without lawyer review** — Founders agreement generated by AI is treated as final. Jurisdiction-specific defects (missing § 90(3) writing requirement, missing § 76B solvency language) are not caught. _Standard: mandatory qualified corporate counsel review before execution._

---

## Writing Standards

Apply these plain-language standards to all output:

**For draft clauses** (shared with founders and counsel):

- Active voice: "The Company shall repurchase" not "Founder shares may be repurchased by the Company"
- Short sentences: one legal concept per sentence
- Name the actor: "Founder A must notify the Board" not "The Board shall be notified"
- Specific, not vague: "within 30 calendar days of the Commencement Date" not "promptly"
- Cite the authority: "per NVCA market standard" not "typically" or "industry practice"

**For Founder Explanatory Notes (EN)**:

- Written for a non-lawyer founder with business (not legal) background
- Explain the "why" not just the "what"
- Use analogy where helpful: "the cliff is like a probationary period for your equity"
- Flag the most important practical consequences
- Keep to 2–4 sentences per note

**Quality gates before delivery:**

1. Can a non-lawyer founder understand the Founder Explanatory Notes without a law degree?
2. Can opposing counsel understand and respond to every provision without ambiguity?
3. Is every legal claim backed by a specific citation (or flagged [VERIFY] / [UNVERIFIED])?
4. Are any phrases vague, hedging, or ambiguous? If yes, fix.
5. Are all jurisdiction-specific provisions marked with [JURISDICTION-SPECIFIC]?
6. Is the Glass Box audit trail complete and consistent with the provisions drafted?

---

## External Tool Integration

### With legalcode-mcp connected (preferred):

In Step 4, search for jurisdiction-specific statutes and authority related to each
major provision. Recommended search terms:

- `"Delaware DGCL Section 151 authorized shares preferred stock"`
- `"UK Companies Act 2006 Section 994 unfair prejudice founders agreement"`
- `"California Labor Code Section 2870 employee IP carve-out"`
- `"Singapore Companies Act Section 76B share buyback solvency"`
- `"India Contract Act Section 27 non-compete void"`

Save results to `/tmp/legalcode-founders-agreement-research.md`. Mark all
legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail.

### Without legalcode-mcp:

- Rely on [JURISDICTION-SPECIFIC] markers and [VERIFY] tags throughout
- Mark all statutory references as UNVERIFIED in the Glass Box
- Note: `legalcode_mcp: "Not connected — citations require independent verification"`
- Focus quality effort on structural completeness, workflow design, and plain-language clarity

---

## Localization Notes

When drafting for a jurisdiction not covered by the four primary formation tracks:

1. Identify the governing statute for: authorized share capital, IP ownership defaults,
   share transfer restrictions, share buyback rules, and employment law
2. Determine non-compete enforceability standard (total ban / reasonableness / blue pencil / compensation required)
3. Verify whether equity vesting has specific tax treatment (EMI equivalent, ESOP trust)
4. Apply [JURISDICTION-SPECIFIC] markers to every provision that differs from the default Delaware treatment
5. Recommend local corporate counsel review for any statutory compliance items

---

## Provenance

Created by Legalcode (2026-03-01). Legalcode original synthesis combining:

- 2-agent research pipeline: structural analysis of legalcode-contract-review (gold
  standard), legalcode-shareholders-agreement-review, and legalcode-term-sheet-analysis;
  parallel legal research across Delaware DGCL, UK Companies Act 2006 / CDPA 1988,
  Singapore Companies Act (Cap. 50) / Patents Act (Cap. 221), India Companies Act 2013 /
  Copyright Act 1957 / FEMA Non-Debt Instruments Rules 2019
- Market benchmarks: NVCA model vesting and anti-dilution terms; BVCA model documents
  for early stage investments; AIF/SEBI ESOP compliance framework; Y Combinator
  standard founder terms
- Key statutory authority: DGCL § 122(18) (eff. August 1, 2024, post-_Moelis_);
  Cal. Bus. & Prof. Code § 16600 (as amended by AB 1076, eff. January 2024);
  Cal. Lab. Code § 2870; CDPA 1988 §§ 90(3), 77–89; IRC §§ 83, 409A, 422, 280G;
  Singapore Companies Act § 76B/76F; India Contract Act § 27; FEMA NDI Rules 2019
- Structural frameworks: 20 anti-patterns, Glass Box audit trail, 5-gate Citation
  Quality Gates, 3-pass Self-Interrogation, 5-level Confidence Scoring, 4-level
  deadlock escalation, investor-readiness checklist
- Target: 500–1,000+ lines, all 18 Legalcode quality elements present
