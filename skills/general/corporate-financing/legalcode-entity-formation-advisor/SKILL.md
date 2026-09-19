---
name: legalcode-entity-formation-advisor
description: Advise on entity type selection and formation for startups, SMEs, joint ventures, holding
  companies, and professional practices. Use when a founder, startup, investor, or corporate legal team
  needs to decide what type of entity to form, where to form it, how to form it, and what ongoing obligations
  follow.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Advise on entity type selection and formation for startups, SMEs, joint ventures, holding companies, and professional practices. Covers C-Corp vs. LLC vs. LP vs. LLP vs. S-Corp entity selection; Delaware, UK Ltd, GmbH/UG, Irish Ltd, and Singapore Pte Ltd jurisdiction selection; tax implications (pass-through, double taxation, QSBS, Irish KDB, Singapore StartSG); liability protection and veil-piercing risks; governance flexibility; formation documents (Certificate of Incorporation, Bylaws, Gesellschaftsvertrag, Articles of Association); post-formation compliance; foreign qualification; and investor readiness. Use when a founder, startup, investor, or corporate legal team needs to decide what type of entity to form, where to form it, how to form it, and what ongoing obligations follow. Jurisdiction-agnostic framework with deep coverage of US (Delaware), UK, Germany, Ireland, and Singapore. Also triggers on: "what entity should I form," "C-Corp or LLC," "Delaware incorporation," "GmbH formation," "holding company structure," "Ireland vs Singapore," "post-formation checklist," "foreign qualification," "83(b) election," "franchise tax."


# Legalcode Entity Formation Advisor

> **Disclaimer**: This skill provides a framework for AI-assisted entity formation advisory.
> It does not constitute legal advice, tax advice, or accounting advice. All outputs should
> be reviewed by a qualified legal professional and tax advisor licensed in the relevant
> jurisdiction(s) before any formation decision is made or documents are filed. Laws,
> regulations, and tax rules change; verify current applicability before relying on any
> provision described here. Statutory references cited from memory carry hallucination risk —
> verify against authoritative sources before relying on them.

## Purpose and Scope

This skill guides founders, corporate counsel, and legal advisors through the full entity
formation decision: selecting the right entity type, choosing the right jurisdiction,
understanding the tax and governance consequences, preparing formation documents, and
meeting post-formation compliance obligations.

**Covers:**

- Entity type selection across US, UK, Germany, Ireland, and Singapore
- Jurisdiction selection analysis with RECOMMENDED / SUITABLE / NOT RECOMMENDED classification
- Tax implication analysis (double taxation, pass-through, QSBS, KDB, territorial systems)
- Liability protection and veil-piercing risk assessment
- Governance flexibility and investor readiness analysis
- Formation document checklist and drafting guidance
- Post-formation compliance calendar
- Foreign qualification and multi-state / multi-jurisdiction operating requirements
- Investor readiness checklist (VC, angel, institutional)
- Common anti-patterns and formation mistakes

**Does not:**

- Provide legal advice or replace qualified counsel
- File incorporation documents on behalf of users
- Provide accounting, tax return preparation, or financial planning services
- Cover public companies or IPO-readiness in depth (see legalcode-term-sheet-analysis for
  pre-IPO matters)
- Cover all jurisdictions — focuses on US (Delaware emphasis), UK, Germany, Ireland, Singapore

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic advisory framework covering five primary jurisdictions. Where
legal requirements differ materially, they are identified with jurisdiction markers:

- `[US-DE]` — United States, Delaware (default US reference)
- `[US-FED]` — United States federal law (tax, securities)
- `[UK]` — United Kingdom (primarily England and Wales)
- `[DE]` — Germany
- `[IE]` — Ireland
- `[SG]` — Singapore

[JURISDICTION-SPECIFIC] When advising on jurisdictions not covered here, research and apply:

- Minimum capital requirements
- Notarization or formal execution requirements
- Mandatory governance structures (supervisory boards, two-tier boards)
- Foreign ownership restrictions
- Substance requirements for tax treaty benefits
- Beneficial ownership registration obligations

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The entity type or jurisdiction depends on undisclosed business facts
- Multiple valid structures exist and the user's priorities determine the choice
- Tax strategy decisions require specialized professional input
- Investor requirements constrain the available options

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

### Step 1: Accept the Formation Request

Accept inputs in any of these forms:

- **Brief description**: "I'm starting a SaaS business with two co-founders and plan to
  raise venture capital"
- **Structured spec**: Entity type preferences, jurisdiction, number of founders, investor
  plans, tax jurisdiction of founders/investors
- **Document**: Existing formation documents to review or improve
- **Comparison request**: "Compare Delaware C-Corp vs UK Ltd for our circumstances"

If insufficient context is provided, proceed to Step 2.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the analysis, ask for the following. Present as structured
options where possible:

1. **Business type and stage**:
   - Options: Pre-revenue startup, Revenue-stage SME, Holding company / investment vehicle,
     Professional services practice, Joint venture between existing companies, Real estate
     holding, Other (describe)
   - _Why this matters_: Startup ≠ holding company ≠ professional practice. Each has
     different governance, tax, and investor requirements.

2. **Fundraising plans**:
   - Options: Venture capital / institutional investors, Angel investors / friends-and-family,
     Private equity, No external investors (self-funded / bootstrapped), Unsure
   - _Why this matters_: VC investors almost exclusively require Delaware C-Corps. Selecting
     the wrong entity forces a costly conversion later.

3. **Founders / principals**:
   - Number of co-founders? Equity split? Vesting schedule planned?
   - Where are founders located? (Country / US state)
   - _Why this matters_: Affects governing law, tax residency, veil-piercing risk if sole
     founder, and equity incentive structuring.

4. **Primary operating jurisdiction**:
   - Where will the business primarily operate? (Country, US state if applicable)
   - _Why this matters_: Determines foreign qualification needs; operating in a state / country
     different from formation jurisdiction creates compliance obligations.

5. **Tax priorities**:
   - Options: Minimize pass-through income taxation, Optimize for capital gains / QSBS on
     exit, International tax efficiency (IP holding, royalties), Avoid double taxation now,
     No specific tax priority — use best-practice defaults
   - _Why this matters_: C-Corp double taxation may be worth it for QSBS ($15M exclusion);
     LLC pass-through may be preferable for an SME that will never sell at scale.

6. **Timeline**:
   - How quickly does the entity need to be formed?
   - Options: Immediate (days), Standard (2–4 weeks), Flexible (planning phase)
   - _Why this matters_: German GmbH takes 2–4 weeks due to notarization; Delaware C-Corp
     can be filed same-day.

If the user provides partial context, proceed with reasonable defaults and state assumptions
explicitly. For batch runs, use these defaults: Delaware C-Corp for VC-backed startup, LLC
for bootstrapped SME, jurisdiction-agnostic for holding company advisory.

### Step 3: Load Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** to search for current legal authority relevant to the jurisdictions
in scope. Save results to `/tmp/legalcode-formation-authority.md`.

**Research priorities by jurisdiction:**

| Jurisdiction | Key Authority Areas                                                                   |
| ------------ | ------------------------------------------------------------------------------------- |
| [US-DE]      | DGCL §§102/141/152/157/170/228/242; IRS §§83/422/1202/1244/409A; SEC Rule 701         |
| [UK]         | Companies Act 2006 §§7-16/154-259; LLP Act 2000; Income Tax Act 2007 Pt. 5 (EIS/SEIS) |
| [DE]         | GmbHG (GmbH Act) §§5/7/19; AktG (Stock Act); HGB §§1-104                              |
| [IE]         | Companies Act 2014; Corporation Tax Act 2010 s.21; KDB (Finance Act 2015 s.31)        |
| [SG]         | Companies Act (Cap. 50) ss.19/45/66/85; Income Tax Act 1947; MOM Employment Act       |

**If legalcode-mcp is not connected:**

- Mark all statutory citations with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed using general legal knowledge with appropriate uncertainty flagging

### Step 4: Entity Type Analysis

Analyze each entity type against the user's stated requirements. Apply the three-tier
classification:

| Rating              | Meaning                                                                   |
| ------------------- | ------------------------------------------------------------------------- |
| **RECOMMENDED**     | Best fit for the stated requirements; materially better than alternatives |
| **SUITABLE**        | Workable for the stated requirements; some trade-offs                     |
| **NOT RECOMMENDED** | Material disadvantages or incompatibilities with stated requirements      |

Cover all applicable entity types from the **Entity Type Reference** section below.

**⟁ CLARIFY** — If the business type or investor requirements create a clear constraint
(e.g., VC-backed → must be C-Corp), state the constraint explicitly and confirm with the
user before narrowing the analysis:

- "VC fundraising almost always requires a Delaware C-Corp. Given this, I'll focus the
  analysis on Delaware C-Corp and address alternatives only as a contingency. Is this right,
  or do you have a specific reason to consider other structures?"

### Step 5: Jurisdiction Selection Analysis

For each RECOMMENDED or SUITABLE entity type, analyze the optimal formation jurisdiction.
Use the **Jurisdiction Reference** section below.

Apply the same three-tier classification (RECOMMENDED / SUITABLE / NOT RECOMMENDED) to each
jurisdiction considered.

**Key jurisdiction trade-offs to surface:**

- Delaware C-Corp: Superior legal framework and investor familiarity, but franchise tax and
  potential double foreign qualification if the business operates primarily elsewhere
- UK Ltd: EIS/SEIS investor tax incentives, lower formation cost, but different governance
  model unfamiliar to US VCs
- German GmbH: Required notarization, 2–4 week timeline, €25,000 minimum capital, but
  preferred for German market operations
- Irish Ltd: 12.5% corporate tax rate, but OECD Pillar Two 15% minimum narrows advantage
  for large groups; substance requirements are strict
- Singapore Pte Ltd: No capital gains tax, territorial system, but 17% rate (vs. Ireland's
  12.5%) and Asia-Pacific focus

**⟁ CLARIFY** — If the jurisdiction analysis reveals a structural decision (e.g., Ireland
as IP holdco + operating subsidiary in US), present the structure clearly and confirm the
user understands the complexity and ongoing substance requirements before proceeding.

### Step 6: Formation Document Checklist

For the RECOMMENDED entity/jurisdiction combination, provide a complete formation document
checklist. Use the **Formation Documents Reference** section below.

Classify each document as:

- **REQUIRED** — Must be filed or executed before the entity exists or can operate
- **RECOMMENDED** — Should be completed at formation (omission creates risk)
- **TIME-CRITICAL** — Has a filing deadline (e.g., 83(b) election: 30 days from grant)

**⟁ CLARIFY** — For equity grants to founders, always ask:

- "Have equity grants to founders already been made or approved by the board?"
- If yes: "The Section 83(b) election must be filed with the IRS within 30 days of the
  grant date. Has this deadline passed? If not, filing must happen immediately."
- _Why this matters_: Missing the 83(b) deadline has permanent adverse tax consequences
  that cannot be remedied retroactively.

### Step 7: Post-Formation Compliance Calendar

Provide a compliance calendar for the first 12 months and ongoing annual obligations.
Use the **Post-Formation Compliance Reference** section below.

Flag any immediate post-formation obligations (EIN, bank account, registered agent,
beneficial ownership registration) that must be completed within days or weeks.

### Step 8: Investor Readiness Assessment

If external investment is planned, assess the entity's investor readiness against the
checklist in the **Investor Readiness Reference** section. Classify each item:

- **COMPLETE** — Done and documented
- **REQUIRED** — Must be completed before investor diligence
- **RECOMMENDED** — Should be completed before investor diligence
- **NOT APPLICABLE** — Does not apply to this structure

### Step 9: Quality Verification

Before delivering the analysis:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For any CRITICAL advisory recommendation, run the 3-pass Self-Interrogation.
3. Assign Confidence Scores to each material recommendation.
4. Generate the Glass Box Audit Trail and append it to the output.

### Step 10: Deliver Analysis

Structure the output using the **Output Format Template** section below.

---

## Entity Type Reference

### United States Entity Types

#### C-Corporation (Delaware)

**Overview**: A separate legal entity owned by shareholders. The dominant structure for
venture-backed startups and public companies globally.

**Key characteristics:**

| Factor                    | Assessment                                                                                               |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| Liability protection      | ✅ Full personal liability separation (subject to veil-piercing)                                         |
| Tax treatment             | ⚠️ Double taxation: 21% federal corporate tax + dividend tax on distributions                            |
| QSBS eligibility          | ✅ Section 1202: up to $15M gain exclusion (post-OBBBA 2025) after 5-year hold [VERIFY]                  |
| Investor compatibility    | ✅ Required by virtually all institutional VCs; preferred stock, options, multi-class stock all possible |
| Governance                | Formal: board of directors, officers, shareholders; annual meetings required                             |
| Formation speed [US-DE]   | Same-day to 24 hours (online filing)                                                                     |
| Formation cost [US-DE]    | $89–$239 filing fee; total setup cost $500–$3,000 with counsel                                           |
| Annual compliance [US-DE] | Annual Report + franchise tax due March 1 (min. $175; Authorized Shares method)                          |

**Delaware advantages**: Court of Chancery expertise; extensive and predictable case law;
privacy protections for shareholders/directors; no state income tax on non-Delaware
operations; preferred by institutional investors globally. [US-DE]

**QSBS Section 1202 mechanics [US-FED]**: Excludes up to $15M of gain (post-OBBBA 2025,
increased from $10M) on sale of QSBS held 5+ years. Partial exclusions available: 50%
at 3 years, 75% at 4 years (OBBBA 2025). Aggregate gross assets must be ≤$75M at time of
issuance (increased from $50M). [VERIFY current OBBBA 2025 enactment status]

**When RECOMMENDED**: VC-backed startups; companies planning for institutional investment
or IPO; multi-founder technology companies; any company where Section 1202 QSBS exit
planning matters.

**When NOT RECOMMENDED**: Sole proprietors needing simple structure; real estate investment
(LLC preferred for pass-through + flexibility); professional services where state law
prohibits corporate form.

---

#### Limited Liability Company (LLC)

**Overview**: A hybrid entity combining partnership-level flexibility and taxation with
corporate-level liability protection.

**Key characteristics:**

| Factor                 | Assessment                                                                                     |
| ---------------------- | ---------------------------------------------------------------------------------------------- |
| Liability protection   | ✅ Full personal liability separation (subject to veil-piercing)                               |
| Tax treatment          | ✅ Default pass-through (no double taxation); can elect C-Corp or S-Corp treatment             |
| QSBS eligibility       | ⚠️ Not eligible by default; requires C-Corp tax election — but then loses pass-through benefit |
| Investor compatibility | ⚠️ Institutional VCs generally cannot invest; forces conversion to C-Corp pre-investment       |
| Governance             | Flexible: member-managed or manager-managed; operating agreement governs                       |
| Formation speed        | Same-day in most states                                                                        |
| Annual compliance      | Varies by state; Delaware: $300 franchise tax                                                  |

**Series LLC [US-DE]**: Delaware introduced Series LLC in 1996. Each series segregates
assets and liabilities; debts of one series are not enforceable against another series or
the master entity. Single $300 annual franchise tax regardless of series count. Best for:
multiple ventures, real estate portfolios, investment holdings. [VERIFY current Delaware
series LLC statute status and cross-state recognition]

**When RECOMMENDED**: Bootstrapped SMEs; real estate investment; professional services
(where state permits); joint ventures between existing companies; multi-asset holding
structures (Series LLC).

**When NOT RECOMMENDED**: VC-backed startups (forces costly conversion); businesses
expecting institutional investment; companies where QSBS planning is material.

---

#### S-Corporation

**Overview**: A C-Corp that has made the S election under IRC §1362. Provides pass-through
taxation while retaining corporate structure.

**Key characteristics:**

| Factor                      | Assessment                                                                                                        |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Liability protection        | ✅ Full corporate liability protection                                                                            |
| Tax treatment               | ✅ Pass-through: income taxed only at shareholder level                                                           |
| Restrictions                | ⚠️ Max 100 shareholders; one class of stock only; all shareholders must be US citizens/residents                  |
| Investor compatibility      | ❌ VC firms (not "natural persons") cannot invest; election automatically lost if ineligible shareholder acquired |
| QSBS eligibility            | ❌ S-Corps are not eligible for Section 1202 QSBS                                                                 |
| Self-employment tax savings | ✅ Owners can split income into salary + distribution, reducing SE tax                                            |

**When RECOMMENDED**: Profitable small businesses (owner-operated) where self-employment
tax savings outweigh S-Corp restrictions; service businesses not seeking institutional
investment; C-Corps that qualify and want to convert for operational profitability phase.

**When NOT RECOMMENDED**: Any business seeking VC or institutional investment; multi-founder
startups planning equity grants with options; businesses with non-US investors.

---

#### Limited Partnership (LP) / Limited Liability Partnership (LLP)

**Overview**: LP has general partners (unlimited liability) and limited partners (liability
limited to investment). LLP provides liability protection for all partners.

**Key characteristics:**

| Factor                   | Assessment                                                                       |
| ------------------------ | -------------------------------------------------------------------------------- |
| LP liability protection  | ⚠️ General partner: unlimited liability; limited partners: limited to investment |
| LLP liability protection | ✅ All partners protected from personal liability for entity obligations         |
| Tax treatment            | ✅ Pass-through taxation by default                                              |
| Governance               | Flexible partnership agreement                                                   |
| Best use                 | Investment funds, real estate, professional services (LLP)                       |

[US-DE] Delaware LP offers charging order protection and creditor limitation on LP interests.

**When RECOMMENDED**: Real estate syndications and investment partnerships; private equity
and venture fund structures; professional service partnerships (law, accounting, consulting)
where LLP is permitted.

**When NOT RECOMMENDED**: Operating businesses seeking broad-based employee equity; VC-backed
startups; structures where unlimited GP liability is unacceptable without an LLC as GP.

---

### United Kingdom Entity Types

#### Private Limited Company (Ltd) [UK]

**Overview**: The standard incorporated form for UK businesses. Governed by Companies Act 2006.

**Key characteristics:**

| Factor                 | Assessment                                                                               |
| ---------------------- | ---------------------------------------------------------------------------------------- |
| Liability protection   | ✅ Shareholders liable only to extent of investment                                      |
| Tax treatment          | 25% corporate tax rate (2024+; 19% for profits ≤£50,000)                                 |
| EIS/SEIS eligibility   | ✅ Powerful investor tax incentives (see below)                                          |
| Governance             | Minimum 1 director; shareholders vote on major decisions                                 |
| Formation cost         | £100 (digital, standard) / £156 (same-day) via Companies House                           |
| Confirmation statement | £50 online annually                                                                      |
| Investor compatibility | ⚠️ US VCs generally prefer Delaware C-Corp; UK angels/institutional investors prefer Ltd |

**EIS (Enterprise Investment Scheme) [UK]**: 30% income tax relief for investors on
investments up to £1M per year (£2M for knowledge-intensive companies). Companies can raise
up to £5M/year. Requires advance assurance from HMRC. [VERIFY current limits]

**SEIS (Seed Enterprise Investment Scheme) [UK]**: 50% income tax relief for investors on
investments up to £200,000 (investor limit). Companies can raise up to £250,000. Target:
early-stage companies <3 years old. Requires advance assurance from HMRC. [VERIFY current
limits post-2023 reforms]

**When RECOMMENDED**: UK-based startups targeting UK angel investors; companies seeking EIS/
SEIS eligibility; businesses primarily operating in UK; professional services, consulting.

**When NOT RECOMMENDED**: UK startups planning US VC fundraising (investor friction);
businesses requiring complex preferred stock structures standard in Delaware C-Corps.

---

#### Limited Liability Partnership (LLP) [UK]

**Overview**: Hybrid between limited company and partnership. Governed by LLP Act 2000.

**Key characteristics:**

| Factor               | Assessment                                                             |
| -------------------- | ---------------------------------------------------------------------- |
| Liability protection | ✅ Members protected from personal liability                           |
| Tax treatment        | Pass-through: members taxed on their share of profits                  |
| Governance           | Private LLP Agreement governs; minimum 2 members (persons or entities) |
| Designated members   | Minimum 2; have enhanced statutory responsibilities                    |
| Formation cost       | £100 (standard) / £156 (same-day) via Companies House                  |

**When RECOMMENDED**: Professional service partnerships (law firms, accounting practices,
consulting); structures requiring pass-through taxation with liability protection.

---

### Germany Entity Types

#### GmbH (Gesellschaft mit beschränkter Haftung) [DE]

**Overview**: Germany's most popular business form. Equivalent to a limited liability
company.

**Key characteristics:**

| Factor                | Assessment                                                                                                                                |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Liability protection  | ✅ Shareholders protected; company bears liability                                                                                        |
| Tax treatment         | ~30% effective rate: 15% corporate income tax + 5.5% solidarity surcharge + ~15% trade tax (Gewerbesteuer) [VERIFY local trade tax rates] |
| Minimum capital       | €25,000 (at least €12,500 must be paid before registration)                                                                               |
| Formation requirement | ✅ Notarization mandatory for Gesellschaftsvertrag                                                                                        |
| Formation timeline    | 2–4 weeks (Handelsregister registration)                                                                                                  |
| Formation costs       | €600–€1,000 (notary + Handelsregister)                                                                                                    |
| Legal existence       | Only upon Handelsregister registration (pre-registration = personal liability)                                                            |

**Handelsregister critical note [DE]**: The GmbH does not legally exist until registered in
the commercial register (Handelsregister). Contracts entered before registration bind the
founders personally. Never commence trading as a "GmbH" before registration is confirmed.

**When RECOMMENDED**: German market entry; EU-based operations; businesses requiring a
well-understood, credible legal form in the German-speaking market.

---

#### UG (Unternehmergesellschaft haftungsbeschränkt) [DE]

**Overview**: A variant of the GmbH with a minimum share capital of €1. Sometimes called
"Mini-GmbH."

**Key characteristics:**

| Factor                     | Assessment                                                                                        |
| -------------------------- | ------------------------------------------------------------------------------------------------- |
| Liability protection       | ✅ Same as GmbH                                                                                   |
| Minimum capital            | €1 (vs. GmbH's €25,000)                                                                           |
| Profit reserve requirement | ⚠️ Must reinvest 25% of annual net profits until €25,000 is accumulated; can then convert to GmbH |
| Perception                 | ⚠️ Less prestigious than GmbH; some counterparties view UG skeptically                            |
| Formation cost             | Slightly lower than GmbH (same notarization requirement)                                          |

**When RECOMMENDED**: Bootstrap startups in Germany without sufficient capital for GmbH;
stepping stone to GmbH once capital accumulated.

**When NOT RECOMMENDED**: Businesses requiring immediate credibility; companies seeking
institutional investment; cases where €25,000 capital is available.

---

### Ireland Entity Types

#### Private Limited Company (Ltd) [IE]

**Overview**: The standard Irish corporate form for trading and holding companies.

**Key characteristics:**

| Factor                          | Assessment                                                                             |
| ------------------------------- | -------------------------------------------------------------------------------------- |
| Liability protection            | ✅ Shareholders protected                                                              |
| Corporate tax rate              | **12.5% on trading income** / 25% on non-trading income [VERIFY]                       |
| Pillar Two note                 | ⚠️ OECD global minimum 15% applies to groups with €750M+ revenue (effective Jan 2024)  |
| Knowledge Development Box (KDB) | ✅ 6.25% effective rate on qualifying IP profits (declining to 10% from 2026) [VERIFY] |
| R&D tax credit                  | ✅ 30% on qualifying R&D expenditure (stacks with 12.5% deduction) [VERIFY]            |
| Substance requirements          | ⚠️ Central management and control must be in Ireland for treaty/rate benefits          |
| Formation timeline              | 5–10 business days via CRO                                                             |
| Tax treaty network              | 70+ bilateral tax treaties; qualified dividend/royalty withholding elimination         |

**Substance requirements [IE]**: To qualify for Ireland's tax treaty benefits and 12.5%
rate, the company must have genuine substance: board meetings in Ireland, key management
decisions made domestically, local staff and management. Shell companies without substance
face transfer pricing challenges and may be re-characterized as tax resident elsewhere.

**When RECOMMENDED**: IP-holding structures for tech/pharma companies; European holding
companies taking advantage of treaty network; businesses with genuine Irish operations;
companies below €750M revenue where 12.5% rate is meaningful.

**When NOT RECOMMENDED**: Groups with €750M+ revenue (Pillar Two equalizes advantage);
structures where substance requirements cannot genuinely be met; operations where proximity
to clients/market makes Ireland impractical.

---

#### Designated Activity Company (DAC) [IE]

**Overview**: An Irish company with a limited objects clause, used for regulated and
structured finance purposes.

**Key characteristics:**

| Factor              | Assessment                                                                       |
| ------------------- | -------------------------------------------------------------------------------- |
| Objects restriction | ⚠️ Limited to activities stated in Constitution; inflexible for general business |
| Minimum directors   | 2 (vs. 1 for Ltd)                                                                |
| AGM                 | Generally required (less dispensable than Ltd)                                   |
| Best use            | Structured finance, aircraft leasing, insurance, regulated entities, JVs, SPVs   |

**When RECOMMENDED**: Structured finance vehicles; aircraft/asset leasing; regulated
financial entities; SPVs where defined purpose is a feature, not a bug.

---

### Singapore Entity Types

#### Private Limited Company (Pte Ltd) [SG]

**Overview**: Singapore's dominant business form. Regulated by ACRA under the Companies
Act.

**Key characteristics:**

| Factor                        | Assessment                                                                               |
| ----------------------------- | ---------------------------------------------------------------------------------------- |
| Liability protection          | ✅ Full liability protection                                                             |
| Corporate tax rate            | 17% (with 75% partial exemption on first S$10,000 profits; startup exemptions available) |
| Capital gains tax             | ✅ None                                                                                  |
| Withholding tax on dividends  | ✅ None                                                                                  |
| CFC rules                     | ✅ None (territorial system)                                                             |
| Foreign ownership             | ✅ 100% foreign ownership permitted                                                      |
| Resident director requirement | ⚠️ At least 1 Singapore-resident director required                                       |
| Formation timeline            | 1–3 business days (ACRA Bizfile)                                                         |
| Formation fees                | S$315 total (S$15 name reservation + S$300 incorporation)                                |
| Annual compliance             | AGM annually; annual return within 7 months of year-end                                  |
| Employment Pass               | S$5,600/month minimum salary for foreign directors requiring EP (2025) [VERIFY]          |

**Startup tax exemption [SG]**: For the first 3 years, qualifying startups pay 0% on first
S$100,000 of chargeable income and 8.5% on next S$100,000 (subject to qualifying conditions).
[VERIFY current thresholds]

**When RECOMMENDED**: Asia-Pacific operations; holding companies for Asian investments; IP
holding for Asia; businesses where no capital gains tax is a material advantage; fintech and
technology companies benefiting from MAS programs.

**When NOT RECOMMENDED**: European-focused operations (Ireland more suitable); groups above
€750M revenue comparing Ireland vs. Singapore (different Pillar Two interactions).

---

## Jurisdiction Selection Framework

### Selection Matrix by Use Case

| Use Case                              | RECOMMENDED                    | SUITABLE                   | NOT RECOMMENDED                       |
| ------------------------------------- | ------------------------------ | -------------------------- | ------------------------------------- |
| VC-backed startup (global ambitions)  | Delaware C-Corp                | UK Ltd (if UK VC only)     | LLC, GmbH, UG                         |
| Bootstrapped SME (US-based)           | Delaware LLC or home-state LLC | S-Corp election            | C-Corp (overkill overhead)            |
| IP holding company (EU focus)         | Ireland Ltd (trading IP)       | UK Ltd, Netherlands BV     | Delaware (US tax complexity)          |
| IP holding company (Asia focus)       | Singapore Pte Ltd              | Ireland Ltd (if EU too)    | GmbH (tax rate)                       |
| German market entry                   | GmbH                           | UG (budget)                | None (GmbH/UG required for substance) |
| Professional services (UK)            | UK LLP                         | UK Ltd                     | US LLC (no recognition)               |
| Real estate investment fund           | Delaware LP / Series LLC       | UK Ltd SPV                 | C-Corp (double taxation)              |
| Joint venture (multi-party)           | Delaware LLC or C-Corp         | UK Ltd, GmbH               | LP (GP liability risk)                |
| UK early-stage startup (EIS eligible) | UK Ltd                         | Delaware C-Corp (if US VC) | LLP (EIS incompatible)                |

### Delaware vs. Other US States

[US-DE] Delaware is the default US incorporation jurisdiction for the following reasons:

- **Court of Chancery**: Specialized business court with bench-only trials and predictable
  case law on corporate governance, fiduciary duties, and M&A disputes
- **Flexible statute**: DGCL permits broad customization of governance rights, preferred
  stock terms, and board authority
- **Investor familiarity**: Every major VC firm and institutional investor knows Delaware
  corporate law; standardized documentation (NVCA model docs) assumes Delaware
- **Privacy**: No public disclosure of directors or officers in formation documents
- **No income tax** on non-Delaware operations and no tax on stock owned by non-residents

**When to incorporate in home state instead**: Sole-owner businesses with no outside
investment planned; businesses that would incur two sets of state filings and fees
(Delaware formation + home-state foreign qualification) for no benefit.

**Nevada and Wyoming [VERIFY]**: Sometimes marketed as alternatives to Delaware for
privacy and tax reasons. Generally not suitable for VC-backed startups; Delaware's legal
infrastructure far outweighs cost savings for any company expecting institutional investment.

### Ireland vs. Singapore Holding Company Comparison

| Factor                | Ireland                           | Singapore                       |
| --------------------- | --------------------------------- | ------------------------------- |
| Corporate tax rate    | 12.5% (trading)                   | 17%                             |
| Capital gains tax     | 33% (after allowances)            | None                            |
| Dividend withholding  | None (EU/treaty)                  | None                            |
| Tax treaty network    | 70+ treaties                      | 80+ treaties                    |
| Pillar Two impact     | Major (large groups)              | Similar                         |
| Geographic focus      | Europe, transatlantic             | Asia-Pacific                    |
| IP incentive          | KDB 6.25% (to 2026)               | IP Development Incentive        |
| Substance requirement | High — board and management in IE | High — local director mandatory |
| Formation speed       | 5–10 days                         | 1–3 days                        |

**Rule of thumb**: Ireland for European IP holding and EU gateway; Singapore for Asia-Pacific
IP holding and investment management.

---

## Formation Documents Reference

### Delaware C-Corporation [US-DE]

| Document                                                           | Status            | Notes                                                                                                        |
| ------------------------------------------------------------------ | ----------------- | ------------------------------------------------------------------------------------------------------------ |
| Certificate of Incorporation                                       | **REQUIRED**      | Public filing; establishes entity; defines authorized shares and classes                                     |
| Bylaws                                                             | **REQUIRED**      | Governs internal procedures; must be formally adopted                                                        |
| Action of Incorporator                                             | **REQUIRED**      | Transfers authority to board; adopts bylaws                                                                  |
| Initial Board Resolutions                                          | **REQUIRED**      | Approves option plan, IP assignments, bank accounts, officers                                                |
| Restricted Stock Purchase Agreement (RSPA)                         | **RECOMMENDED**   | Founder share grants at nominal price with vesting schedule                                                  |
| **Section 83(b) Election**                                         | **TIME-CRITICAL** | File with IRS within **30 days** of stock grant date. Missing deadline = permanent adverse tax consequences. |
| Confidential Information and Invention Assignment Agreement (CIIA) | **RECOMMENDED**   | Assigns all founder IP to the company; required for investor diligence                                       |
| Employer Identification Number (EIN)                               | **REQUIRED**      | Obtain from IRS (Form SS-4) after incorporation; free; required for bank accounts, payroll, and tax filings  |
| Stock ledger / cap table                                           | **REQUIRED**      | Maintain from day one; must be accurate for investor diligence                                               |
| Delaware registered agent                                          | **REQUIRED**      | Required at all times; typical cost $100–$300/year                                                           |

**Authorized shares guidance**: A typical Delaware startup authorizes 10,000,000 shares of
common stock at $0.0001 par value. Authorizing more shares increases the Delaware franchise
tax under the Authorized Shares method. Use the Assumed Par Value Capital method for franchise
tax calculation if authorized shares are high relative to issued shares (can dramatically
reduce the tax). [VERIFY current Delaware franchise tax calculation guidance]

### Delaware LLC [US-DE]

| Document                 | Status       | Notes                                                                |
| ------------------------ | ------------ | -------------------------------------------------------------------- |
| Certificate of Formation | **REQUIRED** | Public filing; $90 filing fee                                        |
| Operating Agreement      | **REQUIRED** | Not filed publicly; governs all member rights, economics, management |
| EIN                      | **REQUIRED** | Required for multi-member LLC and any LLC with employees             |
| Registered agent         | **REQUIRED** | Required at all times                                                |

### UK Limited Company [UK]

| Document                        | Status                            | Notes                                                                                        |
| ------------------------------- | --------------------------------- | -------------------------------------------------------------------------------------------- |
| Memorandum of Association       | **REQUIRED**                      | Filed with Companies House; static after formation                                           |
| Articles of Association         | **REQUIRED**                      | Filed with Companies House; can use Model Articles or bespoke                                |
| Director consent to act (IN01)  | **REQUIRED**                      | Part of Companies House registration                                                         |
| Share certificates              | **RECOMMENDED**                   | Evidence of share ownership                                                                  |
| Shareholders agreement          | **RECOMMENDED**                   | Governs shareholder relations; not filed publicly                                            |
| HMRC SEIS/EIS Advance Assurance | **TIME-CRITICAL** (if applicable) | Obtain before investor commitment; not formal approval but essential for investor confidence |
| PAYE registration               | **REQUIRED** (if employees)       | Register with HMRC before first payroll                                                      |

### German GmbH [DE]

| Document                                       | Status       | Notes                                                                                          |
| ---------------------------------------------- | ------------ | ---------------------------------------------------------------------------------------------- |
| Gesellschaftsvertrag (Articles of Association) | **REQUIRED** | Must be notarized by German notary; cannot be executed remotely without specific authorization |
| Gründungsprotokoll (Formation Protocol)        | **REQUIRED** | Notarized; confirms share purchases and Articles adoption                                      |
| Handelsregister filing                         | **REQUIRED** | Entity does not legally exist until registration confirmed                                     |
| Gewerberegister registration                   | **REQUIRED** | Trade office registration required separately from Handelsregister                             |
| Bank account + capital deposit                 | **REQUIRED** | At least €12,500 of the €25,000 minimum capital must be deposited before registration          |
| Tax registration                               | **REQUIRED** | File with local Finanzamt (tax office) after registration                                      |

### Irish Limited Company [IE]

| Document                                        | Status       | Notes                                                                                  |
| ----------------------------------------------- | ------------ | -------------------------------------------------------------------------------------- |
| Constitution (Memorandum + Articles equivalent) | **REQUIRED** | Filed with CRO                                                                         |
| Form A1 (registration form)                     | **REQUIRED** | Directors, secretary, registered office                                                |
| Registered office                               | **REQUIRED** | Physical Irish address required                                                        |
| Revenue registration                            | **REQUIRED** | Register for corporation tax (and VAT if applicable) with Irish Revenue                |
| HMRC advance assurance                          | N/A          | SEIS/EIS is a UK scheme; Ireland has its own Employment and Investment Incentive (EII) |

### Singapore Pte Ltd [SG]

| Document                           | Status                            | Notes                                                                              |
| ---------------------------------- | --------------------------------- | ---------------------------------------------------------------------------------- |
| ACRA Bizfile application           | **REQUIRED**                      | Name reservation + incorporation; online via Singpass                              |
| Constitution (Articles equivalent) | **REQUIRED**                      | Filed with ACRA at incorporation                                                   |
| Consent to act as director         | **REQUIRED**                      | Required for each director                                                         |
| Company secretary appointment      | **REQUIRED**                      | Must appoint qualified Singapore-resident company secretary within 6 months        |
| ACRA registered office             | **REQUIRED**                      | Singapore address; accessible 3+ hours on business days                            |
| IRAS registration                  | **REQUIRED**                      | Register for corporate income tax; GST if turnover >S$1M                           |
| Employment Pass application        | **TIME-CRITICAL** (if applicable) | Foreign directors/managers requiring EP: apply before commencing work in Singapore |

---

## Post-Formation Compliance Reference

### United States (Delaware C-Corp) [US-DE] [US-FED]

| Obligation                                              | Deadline                                    | Consequence of Non-Compliance                                                                             |
| ------------------------------------------------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Delaware Annual Report + Franchise Tax                  | March 1 each year                           | $200 penalty + 1.5%/month interest; corporate status suspended                                            |
| IRS Form SS-4 (EIN)                                     | Immediately post-formation                  | Cannot open bank account, hire employees, or file taxes without EIN                                       |
| Section 83(b) election                                  | **30 days from stock grant date**           | Permanent adverse tax treatment; cannot be remedied                                                       |
| FinCEN Beneficial Ownership (BOI)                       | 90 days from formation (new entities 2024+) | $500/day civil penalty; criminal penalties for willful violations [VERIFY current BOI enforcement status] |
| Home-state foreign qualification                        | Before doing business in state              | Fines, inability to enforce contracts, loss of good standing                                              |
| Federal income tax return (Form 1120)                   | March 15 (calendar year C-Corp)             | Penalties and interest on underpayment                                                                    |
| State income tax filings                                | Varies by state                             | State-specific penalties                                                                                  |
| Delaware registered agent                               | Ongoing                                     | Entity falls out of good standing                                                                         |
| ISO/NSO option grants — board approval + 409A valuation | Before each grant                           | 409A violations: immediate income recognition + 20% penalty tax [VERIFY]                                  |

### United Kingdom [UK]

| Obligation                                      | Deadline                                               | Consequence of Non-Compliance            |
| ----------------------------------------------- | ------------------------------------------------------ | ---------------------------------------- |
| Confirmation statement                          | Within 14 days of confirmation date; at least annually | Companies House strike-off risk          |
| Annual accounts                                 | Within 9 months of financial year-end                  | Escalating penalties; strike-off risk    |
| Corporation tax return                          | Within 12 months of accounting period end              | Penalties and interest                   |
| VAT registration                                | When taxable turnover exceeds £90,000 (2024) [VERIFY]  | Penalties for late registration          |
| PAYE setup                                      | Before first payment to employees                      | HMRC penalties                           |
| PSC register (persons with significant control) | Ongoing                                                | Criminal offense for failure to maintain |

### Germany [DE]

| Obligation                                    | Deadline                                          | Consequence of Non-Compliance                             |
| --------------------------------------------- | ------------------------------------------------- | --------------------------------------------------------- |
| Trade office registration (Gewerberegister)   | Before commencing trade                           | Administrative penalties                                  |
| Tax registration with Finanzamt               | Immediately after Handelsregister registration    | Delays in receiving tax number; cannot issue VAT invoices |
| Annual financial statements to Bundesanzeiger | Within 12 months of year-end                      | Fines; Handelsregister scrutiny                           |
| Corporate income tax return                   | 31 July of following year (extended with advisor) | Penalties and interest                                    |
| VAT filings                                   | Monthly or quarterly                              | Penalties                                                 |
| UG profit reserve (25% rule)                  | Annual                                            | Regulatory violation; inability to convert to GmbH        |

### Ireland [IE]

| Obligation                        | Deadline                                                    | Consequence of Non-Compliance                                 |
| --------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------- |
| CRO Annual Return (Form B1)       | Within 56 days of Annual Return Date                        | Late filing penalty; loss of audit exemption; strike-off risk |
| Corporation tax return (Form CT1) | Within 9 months of accounting period end                    | Penalties and interest; surcharge on late filing              |
| Revenue registration              | Within 30 days of commencing trade                          | Penalty for late registration                                 |
| VAT registration                  | If turnover >€37,500 (services) or €75,000 (goods) [VERIFY] | Penalties                                                     |
| Substance maintenance             | Ongoing                                                     | Treaty benefits and 12.5% rate at risk                        |

### Singapore [SG]

| Obligation                        | Deadline                              | Consequence of Non-Compliance                            |
| --------------------------------- | ------------------------------------- | -------------------------------------------------------- |
| Annual General Meeting            | Within 6 months of financial year-end | S$5,000 fine per officer                                 |
| Annual Return (ACRA)              | Within 7 months of financial year-end | S$300 if 3 months late; S$600 if more than 3 months late |
| Income tax return (Form C-S or C) | 30 November each year                 | Penalties and estimated assessments                      |
| GST registration                  | When turnover >S$1M [VERIFY]          | Penalties for late registration                          |
| Employment Pass renewal           | Per EP expiry date                    | Illegal employment of foreign worker                     |
| Record retention                  | 5 years minimum                       | ACRA compliance action                                   |

---

## Investor Readiness Reference

### VC / Institutional Investor Readiness (Delaware C-Corp)

| Item                                            | Priority                          | Notes                                                              |
| ----------------------------------------------- | --------------------------------- | ------------------------------------------------------------------ |
| Delaware C-Corp (not LLC)                       | **REQUIRED**                      | VCs cannot invest in LLCs; conversion is costly and time-consuming |
| Certificate of Incorporation filed              | **REQUIRED**                      | Must exist and be in good standing                                 |
| Bylaws adopted                                  | **REQUIRED**                      | Required for investor diligence                                    |
| Founder stock grants documented                 | **REQUIRED**                      | RSPA for each founder with vesting schedule                        |
| Section 83(b) elections filed                   | **REQUIRED**                      | VCs will ask; missing elections create investor concern            |
| All IP assigned to company                      | **REQUIRED**                      | CIIA signed by all founders and employees; no IP held personally   |
| No founder equity disputes                      | **REQUIRED**                      | Any ambiguity in equity ownership is a deal-breaker                |
| Clean cap table                                 | **REQUIRED**                      | Accurate stock ledger; no undocumented commitments                 |
| Board resolutions for all equity grants         | **REQUIRED**                      | Evidence that all grants were properly authorized                  |
| 409A valuation current                          | **REQUIRED** (if options granted) | Stale 409A = options potentially mispriced = §409A liability       |
| Delaware registered agent active                | **REQUIRED**                      | Good standing certificate required at close                        |
| Home-state foreign qualification                | **REQUIRED** (if applicable)      | Good standing in operating state required                          |
| CIIA signed by all founders and key employees   | **REQUIRED**                      | IP chain-of-title must be clear                                    |
| Employment / consulting agreements for founders | **RECOMMENDED**                   | Clarifies role, compensation, non-compete (where permitted)        |
| Operating in right entity (C-Corp not S-Corp)   | **REQUIRED**                      | S election automatically lost with VC investment; convert first    |

### UK Angel / EIS Readiness

| Item                                                       | Priority     | Notes                                     |
| ---------------------------------------------------------- | ------------ | ----------------------------------------- |
| HMRC Advance Assurance letter                              | **REQUIRED** | Obtain before investor commitment         |
| UK Ltd incorporated and in good standing                   | **REQUIRED** |                                           |
| New ordinary shares to be issued (not transfers)           | **REQUIRED** | EIS/SEIS requires issue of new shares     |
| Company not listed on recognized stock exchange            | **REQUIRED** |                                           |
| Company <10 years old (EIS) / <3 years old (SEIS)          | **REQUIRED** | Age limits apply at time of share issue   |
| Qualifying trade (no financial activities, property, etc.) | **REQUIRED** | Certain activities excluded from EIS/SEIS |
| Gross assets test: <£15M (EIS) / <£350K (SEIS)             | **REQUIRED** | [VERIFY current thresholds]               |

---

## Severity Classification System

Applied to findings in the formation analysis:

### CRITICAL — Formation Blocker

Issues that prevent valid formation or create immediate and severe legal risk.

**Examples:**

- Operating as a GmbH before Handelsregister registration (personal liability)
- Missing 83(b) election window (permanent tax harm)
- GmbH capital not deposited before registration
- No resident director for Singapore Pte Ltd

**Action**: Must be resolved before proceeding. Stop and flag immediately.

### HIGH — Material Risk

Issues that create significant ongoing legal, tax, or investor risk.

**Examples:**

- Forming an LLC when VC investment is planned (requires conversion)
- IP not assigned to entity (investor diligence blocker)
- No operating agreement / bylaws (governance vacuum)
- Franchise tax delinquency (entity suspended)

**Action**: Resolve before first external investment or material contract.

### MEDIUM — Operational Risk

Issues that create operational inefficiency or moderate risk.

**Examples:**

- Authorized shares not optimized for franchise tax minimization
- No foreign qualification in operating state
- Substance requirements not monitored for Irish/Singapore structures

**Action**: Resolve within 30–90 days; flag for legal advisor review.

### LOW — Best Practice

Items that represent best practice but are not legally required.

**Examples:**

- Shareholders agreement not executed (recommended but not mandatory)
- Cap table maintained in spreadsheet rather than dedicated software
- Initial board resolutions not fully documented

**Action**: Address when resources permit; document the gap.

---

## Prioritization Framework

### Tier 1 — Formation Essentials (Do Immediately)

Must be completed for the entity to legally exist and operate:

- File Certificate of Incorporation / Articles of Formation / Gesellschaftsvertrag
- Obtain EIN / tax registration number
- Appoint registered agent / registered office
- Execute operating agreement / bylaws / LLP agreement
- Open business bank account (separate from personal funds)
- File 83(b) elections within 30 days of founder equity grants

### Tier 2 — Investor and Compliance Prerequisites (Do Within 30 Days)

Required before external investment and for compliance:

- Execute CIIA with all founders and key hires
- Obtain and document board resolutions for all equity grants
- File FinCEN BOI (US entities) [VERIFY current enforcement status]
- Foreign qualify in operating state / country (if different from formation)
- Set up compliance calendar for annual filings

### Tier 3 — Optimization and Governance (Do Within 90 Days)

Best practice and investor readiness:

- Commission 409A valuation if options are to be granted
- Execute shareholders agreement / investor rights pre-agreement
- Implement cap table management software (Carta, Pulley, Ledgy)
- Obtain HMRC Advance Assurance if EIS/SEIS relevant
- Review IP assignment scope and completeness

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                     | Fail Action                                              |
| -------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal or tax claim cites a specific statute, regulation, or established principle  | Add citation or mark "[UNVERIFIED — advisor to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction              | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments, repeal, or rate changes                    | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within each jurisdiction's legal framework; no cross-jurisdiction leakage | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated; no false confidence on unsettled questions                | Add confidence qualifier                                 |

### Self-Interrogation for CRITICAL Items

For any CRITICAL-classified issue, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the
cited statute or principle? Would a licensed attorney in this jurisdiction reach the same
conclusion?

**Pass 2 — Completeness**: Have all relevant statutes, regulations, and tax rules been
considered? Are there current legislative changes (e.g., OBBBA 2025, Pillar Two) that
affect the analysis?

**Pass 3 — Challenge**: What is the strongest argument that this issue is not as severe as
classified? Under what circumstances might a formation advisor accept the risk? Is the
CRITICAL classification proportionate?

### Confidence Scoring

| Level        | Range     | Meaning                                          | Action                                                 |
| ------------ | --------- | ------------------------------------------------ | ------------------------------------------------------ |
| **Definite** | 0.95–1.0  | Settled law, clear statute, no ambiguity         | State with confidence                                  |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions | State with brief caveat                                |
| **Probable** | 0.60–0.79 | Good arguments but reasonable minds could differ | State with reasoning and contra-indicators             |
| **Possible** | 0.40–0.59 | Genuinely uncertain, competing authorities       | Flag for professional review with both sides           |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                          | Do not assert; flag "[UNCERTAIN — advisor to confirm]" |

---

## Glass Box Audit Trail

Every formation advisory output MUST include a Glass Box section:

```yaml
glass_box:
  skill_name: "legalcode-entity-formation-advisor"
  request_summary: "[Brief description of user's formation request]"
  entity_types_analyzed: "[List of entity types reviewed]"
  jurisdictions_analyzed: "[List of jurisdictions reviewed]"
  recommended_entity: "[RECOMMENDED entity type]"
  recommended_jurisdiction: "[RECOMMENDED jurisdiction]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to temp file or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  assumptions:
    - "[Any assumption made where user context was not provided]"
  limitations:
    - "[Scope limits: jurisdictions not covered, tax topics requiring CPA review, etc.]"
  reviewer: "AI-assisted — requires review by qualified legal and tax professionals"
```

---

## Anti-Patterns

What NOT to do in entity formation advisory:

1. **Recommending Delaware for everything** — Delaware is optimal for VC-backed startups
   and multi-state US operations. For a sole-proprietor SME in Texas with no outside investors,
   a Texas LLC avoids the dual filing burden (Delaware + Texas foreign qualification) for no
   benefit. Match the recommendation to the actual circumstances.

2. **Ignoring the conversion problem** — Advising a startup to form as an LLC without
   disclosing that VC investment will force a conversion to C-Corp. Conversions cost $5,000–
   $20,000 in legal fees, disrupt cap tables, and delay fundraising. Disclose the risk
   upfront if any VC investment is possible.

3. **Missing the 83(b) election** — Founders who receive restricted stock with a vesting
   schedule MUST file Form 83(b) within 30 days of the grant date. This is non-negotiable
   and non-remediable. The skill must flag this as TIME-CRITICAL on every founder equity
   grant recommendation.

4. **Ignoring the franchise tax** — Delaware franchise tax using the Authorized Shares
   method can reach tens of thousands annually for a startup with 10M+ authorized shares.
   The Assumed Par Value Capital method dramatically reduces the bill. Always explain the
   calculation method options.

5. **Treating Ireland or Singapore as simple tax havens** — Both jurisdictions have strict
   substance requirements. A hollow shell without genuine management, board activity, and
   local staff will be re-characterized as tax-resident in the founder's home country,
   defeating the entire structure. Never recommend without substance analysis.

6. **Recommending GmbH without disclosing pre-registration liability** — A German GmbH
   does not legally exist until Handelsregister registration. Contracts signed beforehand
   bind the founders personally. Never describe the GmbH as "formed" until registration
   is confirmed.

7. **Omitting foreign qualification** — A Delaware C-Corp operating in California must
   also qualify in California as a foreign corporation. Failing to do so means fines,
   back taxes, inability to enforce contracts in California, and potential veil-piercing.
   Always check where the business actually operates.

8. **Ignoring veil-piercing risks** — Liability protection exists only if corporate
   formalities are maintained: separate bank accounts, documented resolutions, no personal/
   business fund commingling, adequate capitalization. Advising on formation without
   covering ongoing formality obligations is incomplete.

9. **Assuming S-Corp is always better for tax savings** — S-Corp election has strict
   eligibility requirements (100 shareholders max, US citizens only, one class of stock).
   Any VC investment automatically terminates S status. Recommend only when all restrictions
   are acceptable and no institutional investment is anticipated.

10. **Failing to identify the Section 1202 QSBS opportunity** — For C-Corp founders, the
    QSBS gain exclusion (up to $15M under post-OBBBA 2025 rules) is potentially one of
    the most valuable tax provisions available. Formation advisors should always flag this
    and recommend verification with a tax advisor. [VERIFY OBBBA 2025 enactment status]

11. **Recommending EIS/SEIS without advance assurance** — UK investors will not commit
    capital without confidence that the investment qualifies. HMRC advance assurance is
    not a guarantee, but it is an essential precondition to any EIS/SEIS fundraise. Never
    advise a UK startup to skip this step.

12. **Ignoring the OECD Pillar Two effect** — The 15% global minimum tax (effective
    January 2024 for qualifying groups) materially reduces the tax advantage of Ireland and
    Singapore for large multinationals. For groups with €750M+ revenue, the traditional
    holding company arbitrage is largely gone.

13. **Not addressing the resident director requirement in Singapore** — Every Singapore
    Pte Ltd must have at least one resident director (Singapore citizen, PR, or EP holder)
    at all times. Non-compliance exposes all directors to personal liability. Professional
    nominee director services are common but require careful structuring.

14. **Treating the cap table as an afterthought** — Investor due diligence always
    scrutinizes the cap table. Undocumented equity commitments, missing board resolutions
    for grants, or missing 83(b) elections are deal-breakers. Cap table hygiene from day
    one is as important as the formation documents themselves.

15. **Recommending complex cross-border structures without disclosing transfer pricing** —
    IP holding in Ireland or Singapore with operating subsidiaries elsewhere triggers
    transfer pricing obligations. Intra-group royalties and service fees must be arm's-
    length. Non-compliance exposes both the holding company and the subsidiary to tax
    adjustments, penalties, and reputational risk.

16. **Skipping the IP assignment step at formation** — Founders who develop IP before
    formation own it personally. Without a formal IP assignment to the entity at (or before)
    formation, the company does not own its own core assets. Investors will not fund an
    entity without clear IP title.

17. **Treating the LLC operating agreement as optional** — Without a written operating
    agreement, the LLC is governed by default state rules that may not reflect the members'
    intent on voting, distributions, management, or buy-out. "Optional" in the legal sense
    does not mean advisable to omit.

---

## Writing Standards

Apply plain-language discipline to all output:

**For formation recommendations:**

- Lead with the recommendation, then explain
- Active voice: "Form a Delaware C-Corp" not "A Delaware C-Corp should be formed"
- Short sentences; one point per sentence
- Quantify where possible: "$175 minimum franchise tax" not "a low annual fee"
- Name the risk: "VCs cannot invest in LLCs" not "this may create investor compatibility issues"

**For compliance calendars:**

- Exact deadlines where known ("March 1 each year" not "early in the year")
- Flag TIME-CRITICAL items prominently
- Include consequences of non-compliance

**Quality gates before delivery:**

1. Can a first-time founder understand the entity recommendation and why it was made?
2. Are all CRITICAL and HIGH items prominently placed — not buried in detail?
3. Is every statutory citation either verified or flagged [VERIFY]?
4. Are the compliance deadlines accurate for the current year?
5. Does the output make a clear recommendation, not just list options?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 3, search for jurisdiction-relevant statutes and current regulatory requirements
- Verify current tax rates, formation fees, and filing deadlines
- Check for recent legislative changes (e.g., OBBBA 2025, Pillar Two, BOI requirements)
- Save results to `/tmp/legalcode-formation-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Mark all statutory and regulatory citations with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Recommend that the user verify current tax rates and filing fees independently before
  acting on any recommendation

---

## Localization Notes

### Extending to Other Jurisdictions

This skill covers US, UK, Germany, Ireland, and Singapore. When advising on other
jurisdictions, research and apply:

- **Netherlands (BV)**: Often compared to Irish Ltd for EU holding; 25% CIT rate but
  participation exemption and innovation box (9% on qualifying IP) [VERIFY]
- **Cayman Islands**: Used for offshore hedge funds and PE vehicles; no corporate income
  tax but no substance for operating companies; CIMA regulated for financial activities
- **Canada**: CBCA federal corporation or provincial equivalents; QSBS analog in Canadian
  LCGE (Lifetime Capital Gains Exemption) for CCPC shares [VERIFY]
- **India**: Private Limited Company (Companies Act 2013); mandatory MCA21 filings; FEMA
  restrictions on foreign investment and outbound transactions [VERIFY]
- **France**: SARL (société à responsabilité limitée) for SMEs; SAS (société par actions
  simplifiée) for startups — SAS is preferred by French VCs [VERIFY]

For any jurisdiction-specific analysis, replace [JURISDICTION-SPECIFIC] markers with
researched local content and verify against authoritative sources.

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Entity Formation Advisory

**Request**: [Summary of user's formation objective]
**Date**: [date]
**Jurisdictions Analyzed**: [list]
**Entity Types Analyzed**: [list]

---

## Recommendation

**Entity Type**: [RECOMMENDED entity]
**Formation Jurisdiction**: [RECOMMENDED jurisdiction]
**Confidence**: [HIGH / MEDIUM / LOW]

### Why This Structure

[2–4 sentences explaining why this is the best fit for the stated requirements.
Lead with the most important reason.]

### Key Trade-offs Accepted

[Any material disadvantages of the recommended structure that the user should be aware of.]

---

## Entity Type Analysis

### [Entity Type 1] — [RECOMMENDED / SUITABLE / NOT RECOMMENDED]

[Key factors, 3–5 bullet points]

### [Entity Type 2] — [SUITABLE / NOT RECOMMENDED]

[Key factors, 3–5 bullet points]

---

## Formation Document Checklist

| Document   | Status                                 | Deadline                | Notes      |
| ---------- | -------------------------------------- | ----------------------- | ---------- |
| [Document] | REQUIRED / RECOMMENDED / TIME-CRITICAL | [date or "Immediately"] | [key note] |

---

## Post-Formation Compliance Calendar (Year 1)

| Obligation   | Jurisdiction   | Deadline   | Consequence if Missed |
| ------------ | -------------- | ---------- | --------------------- |
| [Obligation] | [jurisdiction] | [deadline] | [consequence]         |

---

## Investor Readiness Assessment

| Item   | Status                                  | Priority       |
| ------ | --------------------------------------- | -------------- |
| [Item] | COMPLETE / REQUIRED / RECOMMENDED / N/A | TIER 1 / 2 / 3 |

---

## Issues Identified

### CRITICAL Issues

[List any CRITICAL issues found]

### HIGH Issues

[List any HIGH issues found]

### MEDIUM Issues

[List any MEDIUM issues found]

---

## Next Steps (Prioritized)

1. [Tier 1 action]
2. [Tier 1 action]
3. [Tier 2 action]
   ...

---

## Disclaimers and Limitations

[Specific caveats for this analysis: jurisdictions not covered, tax matters requiring
CPA review, legal matters requiring attorney review, currency of statutory citations.]

---

[Glass Box Audit Trail YAML]
```

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis based on deep web research across
US (Delaware), UK, Germany, Ireland, and Singapore formation law, tax rules, and compliance
requirements. Research sources include Delaware Division of Corporations, Companies House,
German Handelsregister guidance, Irish CRO, ACRA Singapore, IRS publications, HMRC
guidance, and practitioner resources from Cooley, Westaway, Harvard Business Services,
1st Formations, and related sources. Incorporates the Legalcode 18-element quality
standard including Citation Quality Gates, Self-Interrogation, Confidence Scoring, Glass
Box audit trail, and 17 anti-patterns.

Research basis: Comprehensive web research (2024–2026 sources) via parallel agent team.
All statutory citations should be verified against authoritative sources before reliance.
