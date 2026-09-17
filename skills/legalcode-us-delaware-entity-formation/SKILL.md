---
name: legalcode-us-delaware-entity-formation
description: Guide Delaware C-corporation formation end-to-end — Certificate of Incorporation drafting
  (8 Del. Use when a founder, startup, legal team, or corporate counsel needs to incorporate a Delaware
  C-corp, prepare a formation document package, structure authorized capital, understand franchise tax
  obligations, qualify to do business in another state, or verify a formation checklist is complete.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Guide Delaware C-corporation formation end-to-end — Certificate of Incorporation drafting (8 Del. C. § 102), Section 102(b)(7) director and officer exculpation (including 2022 amendment), authorized shares structuring for franchise tax minimization (Authorized Shares vs. Assumed Par Value Capital Method under 8 Del. C. § 503), blank check preferred stock for VC readiness, bylaws adoption under DGCL § 109, initial organizational actions (board and stockholder written consents under §§ 141(f) and 228), registered agent requirements (§ 132), Section 83(b) election timing, 409A valuation sequencing, IP assignment at formation, and multi-state foreign qualification. Use when a founder, startup, legal team, or corporate counsel needs to incorporate a Delaware C-corp, prepare a formation document package, structure authorized capital, understand franchise tax obligations, qualify to do business in another state, or verify a formation checklist is complete. Also triggers on: "Delaware incorporation," "Certificate of Incorporation Delaware," "Delaware franchise tax," "authorized shares method," "assumed par value method," "102(b)(7) exculpation," "Delaware bylaws," "organizational consent," "83(b) election," "Delaware registered agent," "foreign qualification Delaware," "blank check preferred," "startup C-corp formation," "Delaware annual report," "SB 21 2025 Delaware."


# Legalcode — Delaware C-Corporation Entity Formation

> **Disclaimer**: This skill provides a framework for AI-assisted Delaware corporate
> formation guidance. It does not constitute legal advice. All outputs must be reviewed
> by a qualified attorney licensed in Delaware (and any other relevant jurisdiction)
> before use. Delaware corporate law changes; statutory and case law references cited
> carry hallucination risk — verify against authoritative sources before relying on
> them. Nothing here creates an attorney-client relationship.

---

## Purpose and Scope

This skill guides end-to-end Delaware C-corporation formation. It covers every step from
initial formation decisions through post-formation compliance obligations, with particular
depth on the areas where practitioners most frequently make costly errors.

**Covers:**

- Certificate of Incorporation drafting and optional provisions (8 Del. C. §§ 101–115)
- Section 102(b)(7) exculpation for directors and officers (including August 2022 extension
  to qualifying officers)
- Authorized shares structuring and franchise tax method selection (§ 503)
- Blank check preferred stock for VC fundraising readiness
- Bylaws: required provisions, Section 109 adoption rights, board vs. stockholder authority
- Initial organizational actions: board written consent (§ 141(f)) and stockholder written
  consent (§ 228)
- Registered agent requirements and commercial agent standards (§ 132)
- Section 83(b) election: the 30-day window and consequences of missing it
- 409A valuation: timing, purpose, and safe harbor requirements
- IP assignment at formation: mechanics and common failures
- Multi-state foreign qualification: nexus triggers and California-specific obligations
- Annual compliance calendar (franchise tax, annual report, registered agent updates)
- 2025 Delaware legislative developments (Senate Bill 21 — § 220 books and records reform)

**Does not:**

- Cover LLC, LP, or LLP formation (see `legalcode-entity-formation-advisor` for entity
  selection)
- Draft complete formation documents (produces annotated guidance and templates, not
  attorney-reviewed final documents)
- Provide legal advice or replace qualified Delaware counsel
- Cover federal tax elections (S-Corp, check-the-box) beyond brief formation sequencing notes
- Cover securities law compliance for stock issuances (Rule 701, Reg D, state blue sky)

---

## Jurisdiction and Governing Law

**Primary jurisdiction**: Delaware — the Delaware General Corporation Law (DGCL),
Title 8 of the Delaware Code, governs all provisions in this skill.

**Secondary jurisdiction**: Federal law applies to tax elections (§ 83(b), 409A) and
securities law (Rule 701, Reg D). State law of the operating state applies to foreign
qualification obligations.

**Key statutory authority**:

| Topic                                 | Primary Authority                 |
| ------------------------------------- | --------------------------------- |
| Formation and Certificate             | 8 Del. C. §§ 101–115              |
| Certificate of Incorporation contents | 8 Del. C. § 102                   |
| Director/officer exculpation          | 8 Del. C. § 102(b)(7)             |
| Registered agent and office           | 8 Del. C. § 132                   |
| Classes of stock                      | 8 Del. C. § 151                   |
| Stock issuance consideration          | 8 Del. C. §§ 152–153              |
| Transfer restrictions                 | 8 Del. C. § 202                   |
| Board governance                      | 8 Del. C. § 141                   |
| Board written consent                 | 8 Del. C. § 141(f)                |
| Stockholder meeting quorum/voting     | 8 Del. C. § 216                   |
| Stockholder written consent           | 8 Del. C. § 228                   |
| Bylaw adoption authority              | 8 Del. C. § 109                   |
| Franchise tax                         | 8 Del. C. § 503                   |
| Foreign qualification                 | 8 Del. C. § 371                   |
| Books and records (post-SB 21)        | 8 Del. C. § 220 (as amended 2025) |

[VERIFY] All statutory citations should be confirmed against the current Delaware Code at
https://delcode.delaware.gov — Delaware law is actively evolving (SB 21 passed March 2025).

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming intent, the workflow pauses and asks when:

- The answer would change the formation structure or document content
- Multiple valid approaches exist (e.g., franchise tax method, authorized shares structure)
- Business context is needed to classify risk correctly
- Missing information would produce a materially incomplete output

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

Accept input in any of these forms:

- **Natural language description**: "I'm forming a Delaware C-corp for my SaaS startup,
  3 founders, planning to raise a seed round"
- **Draft Certificate of Incorporation**: Provide the draft for review and gap analysis
- **Formation checklist**: Provide an existing checklist to verify completeness
- **Specific question**: "How do I calculate Delaware franchise tax?" or "What goes in
  the board organizational consent?"

If no context is provided beyond "help me form a Delaware C-corp," proceed to Step 2 to
gather context before advising.

---

### Step 2: Gather Formation Context

**⟁ CLARIFY** — Before beginning, ask the user these questions. Present as structured
options where applicable:

1. **What is the intended use of the entity?**
   - Options: VC-backed startup (seed/Series A path), Bootstrapped operating company,
     Holding company / SPV, Professional services firm, Joint venture, Other
   - _Why this matters_: Determines authorized shares structure, preferred stock needs,
     franchise tax optimization priority, and investor-readiness requirements.

2. **How many founders / initial stockholders?**
   - Free text (e.g., "2 founders, 50/50 split" or "1 founder, solo").
   - _Why this matters_: Affects stock authorization, vesting structure, and whether
     stockholder written consent mechanics matter from day one.

3. **Do you expect venture capital or angel investment?**
   - Options: Yes — actively seeking VC/angel, Possibly — uncertain, No — self-funded
   - _Why this matters_: VCs require Delaware C-corp with blank check preferred stock.
     This drives the entire authorized capital structure. Getting it wrong at formation
     requires an expensive amendment later.

4. **Do you have employees or contractors today (or within 90 days)?**
   - Options: Yes — employees starting immediately, Contractors only (no W-2), Not yet
   - _Why this matters_: Triggers 409A valuation timing, option pool sizing in certificate,
     and whether a stock plan must be adopted at the organizational consent stage.

5. **Where is the company actually operating?**
   - Free text: state(s) where physical offices, employees, or significant activities exist.
   - _Why this matters_: Determines foreign qualification obligations. California has
     especially onerous requirements for Delaware corps operating there.

6. **What specific output do you need?**
   - Options: Full formation guidance (end-to-end), Certificate of Incorporation review
     / drafting, Franchise tax calculation, Organizational consent checklist, Foreign
     qualification guidance, Specific question on one topic
   - Allow multiple selections.
   - _Why this matters_: Scopes the output to what is immediately useful.

If partial context is provided, proceed with stated assumptions and flag them explicitly.
Example: "I'm assuming VC-backed startup structure — correct me if the company is
bootstrapped and I'll adjust the authorized shares recommendation."

---

### Step 3: Gather Delaware Legal Authority

Use **legalcode-mcp** to gather verified authority for this formation analysis.

**Search for:**

1. Current text of 8 Del. C. § 102 (Certificate of Incorporation requirements)
2. Current text of 8 Del. C. § 102(b)(7) (officer exculpation — verify 2022 amendment
   is reflected)
3. Current text of 8 Del. C. § 503 (franchise tax — Authorized Shares and Assumed Par
   Value methods)
4. Current text of 8 Del. C. § 132 (registered agent — verify August 2025 amendments
   re: physical presence requirement)
5. Current text of 8 Del. C. § 220 (books and records — verify SB 21 / March 2025
   amendment)
6. Recent Delaware Chancery Court and Supreme Court decisions affecting formation
   (Tesla/Musk 2024, Mindbody 2024 reversal, TripAdvisor 2025 reversal)

**Save results** to `/tmp/legalcode-delaware-formation-authority.md`.

**If legalcode-mcp is not connected:**

- Mark all statutory references below with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- All DGCL citations in this skill carry hallucination risk — verify against
  https://delcode.delaware.gov before relying on them

---

### Step 4: Certificate of Incorporation Analysis

Analyze the Certificate of Incorporation (COI) — the foundational formation document
filed with the Delaware Secretary of State's office.

#### 4a. Required Contents (§ 102(a))

The COI must contain all of the following to be valid:

| Element                | Requirement                                                                                                                                                                                          | Common Errors                                                                                     |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Corporate name**     | Must include "Corporation," "Incorporated," "Company," "Limited," or abbreviation; must be distinguishable from existing Delaware entities                                                           | Name not reserved before filing; name conflict discovered post-filing                             |
| **Registered office**  | Physical street address in Delaware (no P.O. boxes); city, county, zip code                                                                                                                          | Using a P.O. box; using a non-Delaware address                                                    |
| **Registered agent**   | Name of agent at the registered address                                                                                                                                                              | Naming an agent who has not consented; naming an individual without confirming Delaware residency |
| **Nature of business** | May be stated as "any lawful act or activity" under § 101 — specific description not required                                                                                                        | Over-specifying purpose, which can inadvertently limit corporate powers                           |
| **Authorized stock**   | Number of shares of each class the corporation is authorized to issue; par value per share (or statement that shares have no par value); relative rights, preferences, and limitations of each class | See § 4b for detailed structuring guidance                                                        |
| **Incorporator**       | Name and mailing address of each incorporator                                                                                                                                                        | Using a law firm address without identifying the individual                                       |

#### 4b. Authorized Stock Structure — Critical Formation Decision

The authorized stock structure is permanent until amended by a stockholder vote. Get this
right at formation. Amendments later require board approval + stockholder approval at a
duly noticed meeting — expensive for an early-stage company.

**Standard VC-Ready Structure:**

```
Total Authorized: 20,000,000 shares
  — Common Stock:   10,000,000 shares, $0.000001 par value per share
  — Preferred Stock: 10,000,000 shares, $0.000001 par value per share
                     (blank check — see § 4c)
```

**Rationale:**

- 10M common is sufficient for founders + employee option pool at initial stage
- 10M preferred gives room for multiple VC rounds without amending the certificate
- $0.000001 par value minimizes the "paid-in capital" floor for stock issuance
  (consideration must equal at least par value under § 153; low par = flexibility)
- Blank check preferred means the board can designate series terms later without
  a stockholder vote (see § 4c)

**Franchise Tax Implication of Large Authorized Share Pools:**
More authorized shares = higher Authorized Shares Method tax. A 20M share authorization
triggers a significant tax bill under the Authorized Shares Method. Solution: always
calculate using the Assumed Par Value Capital Method (see Step 6). Most startups with
modest assets pay the minimum ($400) regardless of authorized shares under that method.

**⟁ CLARIFY** — For non-VC companies or unusual structures, ask:

- "Is this company expecting to raise institutional VC? If not, a simpler single-class
  common structure (e.g., 10M shares common, no preferred) reduces complexity and
  franchise tax."
- "Does the company need a dual-class structure (e.g., high-vote founder shares)? This
  requires explicit authorization in the certificate and should be planned from day one."

#### 4c. Blank Check Preferred Stock (§ 151(g))

For VC-backed companies, include blank check preferred authorization. This provision:

1. Authorizes the board (without stockholder approval) to issue preferred shares in
   one or more series
2. Delegates to the board the power to fix the number of shares, voting powers,
   preferences, and special/relative rights of each series by resolution
3. Allows the board to file a Certificate of Designation with the Delaware Secretary of
   State establishing series terms when needed (e.g., at a Series A closing)

**Required language in the COI:**

```
"The Board of Directors is expressly authorized, subject to limitations prescribed by
law, to provide for the issuance of the shares of Preferred Stock in one or more series,
and by filing a certificate pursuant to the applicable law of the State of Delaware
(hereinafter referred to as a 'Preferred Stock Designation'), to establish from time
to time the number of shares to be included in each such series, and to fix the
designation, powers, preferences and rights of the shares of each such series and any
qualifications, limitations or restrictions thereof."
```

**Without this language**: Any preferred stock issuance requires a full stockholder vote
to amend the certificate. This is a deal-killer for VC fundraising timelines.

#### 4d. Section 102(b)(7) Exculpation Clause

**What it does**: Eliminates monetary liability of directors (and now qualifying officers)
for breaches of the duty of care. Does NOT eliminate liability for:

- Breaches of the duty of loyalty
- Acts or omissions not in good faith
- Intentional misconduct or knowing violation of law
- Unlawful stock repurchases or dividends (§ 174)
- Transactions from which the director derived an improper personal benefit

**2022 Amendment — Officer Exculpation:**
Effective August 1, 2022, § 102(b)(7) was amended to permit exculpation of "qualifying
officers" — a defined subset including: (i) the president, (ii) CEO, COO, CFO, chief
legal officer, controller, treasurer, and chief accounting officer; (iii) officers
identified in SEC filings as executive officers; and (iv) officers who have consented
to service of process in Delaware.

**Critical limitation for officers**: Qualifying officers CANNOT be exculpated for:

- Derivative claims (unlike directors, who can be exculpated for derivative suits too)
- Duty of loyalty breaches
- Bad faith acts

**Industry adoption**: In the 2023 proxy season, ~80% of public Delaware companies that
put officer exculpation to a vote received stockholder approval. For new incorporations,
include it in the initial COI — no stockholder vote needed at formation.

**Recommended COI language** (include both director and officer exculpation):

```
"To the fullest extent permitted by the DGCL as it now exists and may hereafter be
amended, a director or qualifying officer of the corporation shall not be personally
liable to the corporation or its stockholders for monetary damages for breach of
fiduciary duty as a director or qualifying officer, except to the extent such exemption
from liability or limitation thereof is not permitted under the DGCL as the same exists
or may hereafter be amended."
```

[VERIFY] Confirm exact statutory language requirements with current DGCL text before
including in a filed document.

#### 4e. Additional Optional Provisions (§ 102(b))

Consider including at formation to avoid later amendments:

| Provision                                         | Benefit                                      | When to Include                                                  |
| ------------------------------------------------- | -------------------------------------------- | ---------------------------------------------------------------- |
| **Supermajority voting requirements**             | Entrenches protective provisions             | Rarely advisable without investor counsel                        |
| **Forum selection** (Delaware as exclusive forum) | Forces litigation to Delaware Chancery Court | Advisable for most startups; reduces multi-forum litigation risk |
| **Anti-takeover provisions**                      | Board control over hostile M&A               | Only if relevant to business context                             |
| **Director indemnification standard**             | Can expand beyond statutory minimum          | Consider expanded indemnification up to the maximum DGCL permits |
| **Advance notice bylaw authorization**            | Enables advance notice bylaws                | Typically included in bylaws, not certificate                    |

**Post-SB 21 note (March 2025)**: SB 21 amended § 102 to prohibit charter provisions
that impose liability on stockholders for attorneys' fees in internal corporate claims.
Do not include any such provision.

---

### Step 5: Bylaws Analysis

Bylaws are the internal governance rules of the corporation. Unlike the COI, bylaws are
generally not filed publicly with the State of Delaware.

#### 5a. Adoption Authority (§ 109)

**Who adopts the initial bylaws?**

| Scenario                                          | Authority                                   |
| ------------------------------------------------- | ------------------------------------------- |
| Incorporator-adopted bylaws (before stock issued) | Incorporator (most common at formation)     |
| Board-adopted bylaws                              | Board, if authorized in the certificate     |
| Stockholder-adopted bylaws                        | Stockholders always retain concurrent power |

**Default rule**: After payment for stock is received, both stockholders AND the board
(if certificate confers board bylaw power) have concurrent authority to adopt, amend,
or repeal bylaws.

**Best practice at formation**: Incorporator adopts initial bylaws before any stock is
issued; board ratifies at organizational consent.

#### 5b. Required and Recommended Bylaw Provisions

| Provision                        | Required?            | Notes                                                  |
| -------------------------------- | -------------------- | ------------------------------------------------------ |
| **Registered office and agent**  | Recommended          | Can track the COI                                      |
| **Stockholder meetings**         | Recommended          | Annual and special meeting procedures                  |
| **Notice requirements**          | Recommended          | Timing, method, and waiver of notice                   |
| **Quorum**                       | Recommended          | Default: majority of shares entitled to vote (§ 216)   |
| **Board composition**            | Recommended          | Number of directors (range or fixed); staggered boards |
| **Board meetings and action**    | Required in practice | In-person, telephonic, written consent                 |
| **Board quorum**                 | Recommended          | Default: majority of total directors (§ 141(b))        |
| **Officer titles and authority** | Recommended          | President, Secretary, Treasurer minimum                |
| **Indemnification**              | Highly recommended   | Reference § 145 and any broader COI indemnification    |
| **Fiscal year**                  | Recommended          | Typically calendar year for simplicity                 |
| **Amendments**                   | Recommended          | How bylaws can be changed post-adoption                |

#### 5c. Board Quorum — Critical Governance Point

Under § 141(b), the default quorum for a board meeting is a majority of the total number
of directors (not just directors present or voting). Bylaws may reduce this to no less
than one-third of total directors.

**Vacancy issue**: A sole director on a three-seat board does NOT constitute a quorum.
This means:

- Written consents under § 141(f) require all directors who are present at the meeting —
  but a quorum must exist first
- A company with 3 authorized board seats but only 1 director cannot validly take board
  action by written consent absent a bylaw reducing quorum

**⟁ CLARIFY** — Ask the user: "How many board seats will the certificate authorize, and
how many directors will be elected at formation?" Mismatch between authorized seats and
actual director count is a common governance defect.

#### 5d. Officer Structure

Delaware law does not mandate specific officer titles. However, standard practice for
formation is to elect at minimum:

- **President** (or CEO) — chief executive authority
- **Secretary** — maintains corporate records, certifies resolutions
- **Treasurer** (or CFO) — financial officer

One person may hold multiple officer positions in a startup context. The Secretary is
the officer most critical to legal compliance — stock certificates, stockholder lists,
and corporate records are the Secretary's statutory responsibility.

---

### Step 6: Delaware Franchise Tax

The Delaware franchise tax is a significant annual obligation that surprises many startups.
The method of calculation — not just the tax rate — is a critical decision.

#### 6a. Two Methods — Always Choose the Lower

Delaware offers two calculation methods. **Use the method that produces the lower tax.**
There is no filing requirement to elect a method; simply calculate both and pay the lower.

#### Method 1: Authorized Shares Method (Default)

```
Rate:
  — 5,000 shares or fewer:              $175 flat
  — 5,001 to 10,000 shares:             $250 flat
  — Each additional 10,000 shares (or fraction thereof): add $85

Formula example for 20,000,000 authorized shares:
  First 10,000 shares:           $250
  Remaining 19,990,000 shares ÷ 10,000 = 1,999 additional brackets × $85 = $169,915
  Total:                                $170,165

  (Capped at $200,000 maximum)
```

**When to use**: Companies with very few authorized shares and substantial assets.
For startups with millions of authorized shares, this method is nearly always worse.

#### Method 2: Assumed Par Value Capital Method (Preferred for Startups)

```
Step 1: Divide total gross assets by total issued shares to get assumed par value.
        Assumed Par Value = Total Gross Assets ÷ Total Issued Shares

Step 2: Multiply assumed par value by total authorized shares.
        Assumed Par Value Capital = Assumed Par Value × Total Authorized Shares

Step 3: Apply the tax rate: $400 per $1,000,000 of Assumed Par Value Capital
        (or fraction thereof).
        Minimum tax under this method: $400.

Example for early-stage startup:
  Total Gross Assets:   $500,000
  Total Issued Shares:  2,000,000
  Assumed Par Value:    $500,000 ÷ 2,000,000 = $0.25/share
  Authorized Shares:    20,000,000
  Assumed Par Value Capital: $0.25 × 20,000,000 = $5,000,000
  Tax: $5,000,000 ÷ $1,000,000 × $400 = $2,000

  Versus Authorized Shares Method: ~$170,165
  Savings: ~$168,165
```

**When to use**: Almost always for venture-backed startups. The assumed par value method
treats authorized shares as if they have an implied value proportional to actual assets —
which is low for early-stage companies.

**Source for gross assets**: Use total assets from the federal corporate tax return
(Form 1120, Schedule L) for the fiscal year ending in the calendar year of the report.
For pre-revenue companies, use the balance sheet as of December 31 of the reporting year.

#### 6b. Annual Report and Payment Deadline

| Item                                       | Details                                         |
| ------------------------------------------ | ----------------------------------------------- |
| **Annual Report due date**                 | March 1 (covering prior calendar year)          |
| **Franchise tax due date**                 | March 1 (same as annual report)                 |
| **Annual Report filing fee**               | $50                                             |
| **Minimum tax (Authorized Shares Method)** | $175                                            |
| **Minimum tax (Assumed Par Value Method)** | $400                                            |
| **Maximum tax (both methods)**             | $200,000                                        |
| **Late penalty**                           | $200 flat + 1.5% monthly interest on unpaid tax |
| **Filing portal**                          | Delaware Division of Corporations online portal |

**⟁ CLARIFY** — If the user wants a franchise tax estimate, ask:

1. "What are the company's total gross assets as of December 31 of the reporting year?
   (Use the balance sheet or Form 1120 Schedule L total assets line.)"
2. "How many shares are currently issued and outstanding?"
3. "How many total shares are authorized in the certificate?"

Then calculate both methods and present the lower figure.

---

### Step 7: Initial Organizational Actions

After the COI is filed, the corporation must hold its organizational meeting or execute
written consents to constitute itself as a functioning entity. These actions are typically
taken by unanimous written consent to avoid the formality of a physical meeting.

#### 7a. Board Action by Unanimous Written Consent (§ 141(f))

The board's initial organizational consent typically accomplishes:

| Action                                           | Legal Basis             | Notes                                       |
| ------------------------------------------------ | ----------------------- | ------------------------------------------- |
| Adopt Bylaws                                     | § 109                   | If not adopted by incorporator              |
| Elect officers                                   | § 142                   | President/CEO, Secretary, Treasurer minimum |
| Authorize bank accounts                          | Board power under § 141 | Designate authorized signatories            |
| Authorize stock issuance to founders             | § 152–153               | Fix price; verify consideration             |
| Designate fiscal year                            | Board power             | Calendar year typically                     |
| Adopt equity incentive plan                      | Board discretion        | If employees are imminent                   |
| Authorize S-election (if applicable)             | IRS Form 2553           | Time-sensitive; file within 2.5 months      |
| Ratify incorporation and organizational expenses | Best practice           | Creates documentary record                  |

**Critical requirement**: The consent must be signed by ALL directors (§ 141(f) requires
unanimity). A single director who refuses to sign prevents written consent action.

**Quorum pre-condition**: Although written consent bypasses a physical meeting, the
quorum requirement of § 141(b) is not eliminated by § 141(f). If only one director is
serving on a board with 3 authorized seats, the company lacks a quorum and CANNOT take
valid board action by written consent. Either fill the vacant seats first or reduce the
authorized board size in the bylaws.

#### 7b. Stockholder Action by Written Consent (§ 228)

**When stockholder consent is needed at formation:**

- To approve the adoption of bylaws (concurrent power with board)
- To elect initial directors (if not named in the COI)
- To approve any certificate amendment at formation (e.g., changing authorized shares
  before stock issuances)

**§ 228 requirements:**

- Consent must be executed by holders of not less than the minimum number of votes
  that would be necessary to authorize the action at a duly held meeting
- All consents must be dated and delivered within 60 days of the first dated consent
- Prompt written notice to non-consenting stockholders required
- If the action requires a certificate filing, the certificate states consent was given

**⟁ CLARIFY** — Before organizational documents are prepared, ask: "Who are the initial
directors? Will they be named in the COI or elected by stockholder consent post-filing?"
This determines whether a separate stockholder organizational consent is needed.

#### 7c. Founder Stock Issuance at the Organizational Consent

The organizational consent should authorize the issuance of founder common stock.
Key issues:

| Issue                     | Details                                                                                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Consideration**         | Must equal at least par value (§ 153). For $0.000001 par, this is trivially satisfied by cash, services, or property. Board determines fair consideration. |
| **Vesting**               | Restricted stock with a vesting schedule protects the company if a founder departs early. Standard: 4-year vesting with 1-year cliff.                      |
| **§ 83(b) election**      | If stock is subject to vesting (a "substantial risk of forfeiture"), founders MUST file a § 83(b) election within 30 days of stock grant. See Step 8.      |
| **IP assignment**         | Contemporaneous with stock issuance, require founders to sign a Proprietary Information and Inventions Assignment (PIIA) agreement. See Step 9.            |
| **Transfer restrictions** | Bylaws or a stockholders' agreement can impose right of first refusal on transfers (§ 202 — must be conspicuously noted on stock certificates).            |

---

### Step 8: Section 83(b) Election — Critical Tax Step

**What is a § 83(b) election?**
Under IRC § 83, property transferred in connection with services (including founder
restricted stock subject to vesting) is taxed as ordinary income at the time it vests —
not when it is granted. A § 83(b) election reverses this: the founder is taxed at grant
(when the stock is worth very little) rather than at vesting (when it may be worth a lot).

**Why it matters for founders:**
Without a § 83(b) election, each vesting event is a taxable income event at the then-fair
market value of the vested shares. For a startup that succeeds, this can mean ordinary
income tax bills of millions of dollars at each vesting cliff and monthly thereafter.

With a § 83(b) election, all future appreciation is capital gain (long-term if held
more than 12 months).

**The 30-day window:**

- Must be filed with the IRS within **30 calendar days** of the date of the stock grant
- No extensions — the IRS does not grant them
- Late filing = permanent loss of § 83(b) protection
- The 30-day clock starts on the grant date, not the date the stock certificate arrives

**Filing requirements:**

1. Complete the § 83(b) election notice (no official IRS form; standard notice format)
2. File with the IRS service center where the founder files income taxes
3. Send by certified mail (to create a postmark record proving timely filing)
4. Attach a copy to the founder's income tax return for the year of grant
5. Keep a copy in the corporate records

**⟁ CLARIFY** — Before organizational consent is executed, ask: "Have all founders been
advised that § 83(b) elections must be filed within 30 days of the stock grant date?
Who is tracking the deadline?" This should be calendared immediately upon signing.

---

### Step 9: IP Assignment at Formation

IP assignment is a formation step, not a post-formation housekeeping item.

**Why it is critical:**
If founders begin working on the company's technology, product, or brand before the
corporation is formed — or if they did so as part of another entity, employer, or
university — that IP may not belong to the corporation without an explicit assignment.
This is a diligence blocker in every VC fundraising process.

**What the assignment agreement must cover:**

1. **Prior work**: All inventions, code, designs, and IP created before incorporation
   that relate to the company's business
2. **Future work**: All IP created during the founder's service to the company
3. **Scope**: Patents, copyrights, trademarks, trade secrets, and moral rights (to the
   extent assignable under applicable law)
4. **Consideration**: The receipt of founder equity is adequate consideration

**Common failures:**

- Founders do not sign IP assignment until demanded by investors — by which time a
  founder may have departed and leverage is gone
- Assignment covers only "developed during employment" rather than prior IP
- Assignment does not cover IP developed on personal equipment or outside business hours
  (some states have statutes limiting assignment of IP created on personal time without
  company resources — check the relevant state law [JURISDICTION-SPECIFIC])
- University affiliation issues: founders who were students or faculty may have IP
  obligations to their university that conflict with company assignment
- Prior employer obligations: founders with non-compete or IP assignment agreements
  from prior employers may not be free to assign certain IP

**Timing**: Execute the PIIA (or equivalent IP assignment agreement) simultaneously with
the founder stock grant. Make it a condition of receiving stock — not a separate request.

[VERIFY] Some states (California, Delaware, Washington, Minnesota, North Carolina,
Illinois) have statutes limiting the scope of IP assignments. Confirm the governing state
law and whether any assignment must be narrowed to comply.

---

### Step 10: Registered Agent and Office

#### 10a. Statutory Requirements (§ 132)

Every Delaware corporation must continuously maintain:

1. A registered office in Delaware with a physical street address (no P.O. boxes)
2. A registered agent at that address who is:
   - An individual Delaware resident with a business or residence in Delaware, OR
   - A business entity authorized to provide registered agent services in Delaware

#### 10b. Commercial Registered Agent Standards (Effective August 2025)

As of August 1, 2025, commercial registered agents (those serving 50+ entities) must:

- Maintain a physical office in Delaware open during regular business hours
- Accept service of process and perform registered agent functions at that office
- Maintain up-to-date contact information for each entity they serve

[VERIFY] Confirm the August 2025 amendments are in effect and review current DGCL § 132
text for any subsequent changes.

#### 10c. Maintaining Current Agent Contact Information

The corporation must provide its registered agent with:

- Name, business address, and business telephone of at least one officer, director,
  or authorized employee to receive communications
- Updated contact information whenever the designated contact changes

**Consequences of losing registered agent:**

- Service of process may be ineffective — missed lawsuits, default judgments
- Delaware Secretary of State may void the corporation's good standing
- Legal notices may not reach the company

**Practical guidance:** Use a commercial registered agent service. Costs range from
$50–$300/year. Major providers include CT Corporation, The Corporation Trust Company,
Cogency Global, Harvard Business Services, and Northwest Registered Agent.

---

### Step 11: Multi-State Foreign Qualification

A Delaware corporation doing business in other states must register as a "foreign
corporation" in each operating state. Failure to qualify exposes the company to:

- Inability to enforce contracts in that state
- State penalties and back taxes
- Personal liability exposure in some states

#### 11a. Nexus Triggers — When to Qualify

"Doing business" is defined differently by each state, but the following activities
commonly trigger qualification obligations:

| Activity                                      | Typically Triggers Qualification? |
| --------------------------------------------- | --------------------------------- |
| Physical office or storefront                 | Yes — always                      |
| Employees in the state                        | Yes — almost always               |
| Officers working from their home in the state | Generally yes                     |
| Opening a bank account in the state           | Varies by state                   |
| Owning real estate in the state               | Yes                               |
| Frequent in-person client meetings            | Often yes                         |
| Shipping products to customers                | No — isolated transactions        |
| Providing remote services to customers        | No — if no physical nexus         |
| Holding a one-time conference                 | Generally no                      |

**⟁ CLARIFY** — Ask the user: "In which states does the company have any physical
presence, employees, or regular in-person activity?" Map each to a qualification
obligation.

#### 11b. Foreign Qualification Process

**Required documents (varies by state):**

1. **Certificate of Good Standing** from Delaware Secretary of State (order online;
   typically 24-hour processing; ~$50 for standard, more for expedited)
2. **Application for Certificate of Authority** (or equivalent) filed with target state
   Secretary of State
3. **Registered agent** appointment in the target state
4. **Filing fees** (vary by state; $100–$500 typical range)

**Typical processing time**: 1–5 business days (expedited available in most states).

#### 11c. California — High-Priority Warning [US-CA]

California deserves special attention because it is the most onerous state for Delaware
corporations:

| Obligation                                              | Details                                                                                                                         |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **California minimum franchise tax**                    | $800/year, beginning after the first year                                                                                       |
| **California corporate income tax rate**                | 8.84% on California-sourced income                                                                                              |
| **Application for Certificate of Authority filing fee** | $100                                                                                                                            |
| **Annual Statement of Information**                     | $25/year, due within 90 days of qualification and annually thereafter                                                           |
| **Late filing penalty**                                 | $250 flat + suspension risk                                                                                                     |
| **Consequences of non-qualification**                   | Cannot maintain any California action; contract enforcement risk; back taxes and penalties from the date "doing business" began |

**Bay Area startup note**: A Delaware corp incorporated in Delaware but with all employees
and founders working in the San Francisco Bay Area is "doing business" in California on
day one. Qualify immediately to avoid retroactive penalty exposure.

#### 11d. Annual Compliance in Qualified States

Each qualified state typically requires:

- Annual report (timing and fee varies by state)
- Annual registered agent fee in that state
- State income/franchise tax filings (if applicable)
- Maintaining current registered agent and contact information

---

### Step 12: Post-Formation Compliance Calendar

After formation, the corporation has recurring compliance obligations. Missing any of
these deadlines risks loss of good standing, financial penalties, or corporate voidance.

| Obligation                                     | Jurisdiction              | Deadline                                        | Consequence if Missed                                          |
| ---------------------------------------------- | ------------------------- | ----------------------------------------------- | -------------------------------------------------------------- |
| **Delaware Annual Report + Franchise Tax**     | Delaware                  | March 1 (annual)                                | $200 penalty + 1.5%/month interest; entity becomes delinquent  |
| **Registered agent contact info update**       | Delaware                  | Whenever contact changes                        | Service of process failures; standing risk                     |
| **California Annual Statement of Information** | California (if qualified) | Within 90 days of qualification, then annual    | $250 penalty; potential suspension                             |
| **California franchise tax payment**           | California (if qualified) | April 15 (estimated); March 15 (annual return)  | Penalties; entity suspension                                   |
| **Other state annual reports**                 | Each qualified state      | Varies by state                                 | Per-state penalties; loss of good standing                     |
| **§ 83(b) election**                           | Federal (IRS)             | 30 days from stock grant date                   | Permanent loss of § 83(b) benefit                              |
| **409A valuation update**                      | Federal (IRS)             | Before any option grants; after material events | Options may fail IRC § 409A; 20% penalty tax on option holders |
| **Delaware Certificate of Good Standing**      | Delaware                  | Before fundraising, contracts, or M&A           | Deal delays; qualification failures                            |

**⟁ CLARIFY** — Ask whether the user wants a customized compliance calendar with exact
dates based on the formation date and operating states provided in Step 2. If yes,
generate specific deadlines.

---

### Step 13: 409A Valuation — Sequencing

A 409A valuation establishes the fair market value (FMV) of the corporation's common
stock. Options granted at or above FMV are not subject to the punitive income inclusion
rules of IRC § 409A.

**Why it matters:**
If options are granted below FMV and § 409A applies, option holders face:

- Ordinary income inclusion at vesting
- 20% additional federal tax penalty
- Possible state penalty taxes
- Back taxes plus interest from the grant date

**When to get the first 409A:**

- Before issuing ANY stock options to employees or consultants
- After any significant funding round (each round resets FMV)
- After any material change in business value (new major customer, FDA approval, etc.)

**Safe harbor protection:**

- Independent third-party 409A appraisal provides a "rebuttable presumption" of FMV
- IRS bears the burden of proof to challenge a properly obtained appraisal
- No safe harbor = company bears the burden of proof in an IRS audit

**Typical cost**: $2,000–$5,000 for an initial startup 409A; more for complex situations.

**Sequencing error to avoid**: Do not issue options and then get a 409A retroactively.
The 409A must precede the grants it is used to support.

---

## Formation Checklist Classification

### CRITICAL — Must Complete Before Operating

Issues that create immediate legal risk, personal liability, or irreversible harm:

| Item                                                             | Risk if Not Done                                           |
| ---------------------------------------------------------------- | ---------------------------------------------------------- |
| File Certificate of Incorporation with Delaware SOS              | Corporation does not legally exist                         |
| Appoint registered agent before filing                           | Filing rejected                                            |
| Execute § 83(b) elections within 30 days of stock grants         | Permanent, uncorrectable tax harm to founders              |
| Assign IP from founders to corporation at formation              | Diligence blocker; may be uncorrectable if founders depart |
| Qualify in operating states immediately if employees are present | Back-tax exposure; contract enforcement risk               |

### HIGH — Complete Within 30 Days of Formation

| Item                                                                | Risk if Deferred                                                |
| ------------------------------------------------------------------- | --------------------------------------------------------------- |
| Execute board organizational consent                                | Corporation cannot validly issue stock or appoint officers      |
| Issue founder stock via organizational consent                      | Founders may not have a valid equity grant                      |
| Execute PIIA / IP assignment agreement                              | IP ownership uncertain                                          |
| Adopt bylaws                                                        | Governance vacuum; director action may be questionable          |
| Establish corporate bank account                                    | Commingling of personal and corporate funds; veil-piercing risk |
| File initial Statement of Information in California (if applicable) | $250 penalty; 90-day deadline                                   |

### MEDIUM — Complete Within 90 Days of Formation

| Item                                                               | Risk if Deferred                                                           |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| Obtain first 409A valuation (if option grants planned)             | Cannot issue compliant options                                             |
| Adopt equity incentive plan (if employees are imminent)            | Cannot grant equity to employees                                           |
| Establish capitalization table management system                   | Cap table errors accumulate                                                |
| Confirm registered agent contact information is current            | Service of process failures                                                |
| Consult tax advisor regarding S-election eligibility (if relevant) | S-election must be filed within 2.5 months of formation or new fiscal year |
| Calendar Delaware franchise tax deadline (March 1)                 | Late filing penalty                                                        |

### LOW — Best Practice, Address When Resources Permit

| Item                                               | Notes                                                                |
| -------------------------------------------------- | -------------------------------------------------------------------- |
| Execute stockholder agreement / voting agreement   | Recommended but not legally required at formation                    |
| Establish directors' and officers' (D&O) insurance | Critical before any VC investment                                    |
| Implement insider trading policy                   | Required for public companies; good practice earlier                 |
| Maintain corporate minute book                     | Required by § 220 (as amended by SB 21) for books and records access |
| Adopt board committee structure                    | Not needed at early stage but important pre-IPO                      |

---

## Delaware Franchise Tax — Step-by-Step Calculator

Use this calculator when the user provides gross assets, issued shares, and authorized shares:

```
INPUT:
  Total Gross Assets (A):         $[user-provided]
  Total Issued Shares (I):        [user-provided]
  Total Authorized Shares (Auth): [user-provided]

AUTHORIZED SHARES METHOD:
  If Auth ≤ 5,000:     $175
  If Auth ≤ 10,000:    $250
  If Auth > 10,000:    $250 + ceiling((Auth − 10,000) / 10,000) × $85
  Cap at $200,000

ASSUMED PAR VALUE CAPITAL METHOD:
  Assumed Par Value = A / I
  Assumed Par Value Capital = Assumed Par Value × Auth
  Tax = ceiling(Assumed Par Value Capital / 1,000,000) × $400
  Minimum: $400
  Cap at $200,000

RESULT:
  Use the LOWER of the two methods.
  Add $50 annual report filing fee.
  Total due March 1.
```

---

## 2025 Delaware Legislative Developments

### Senate Bill 21 — Books and Records Reform (March 2025)

SB 21 significantly amended § 220 (stockholder inspection rights). Key changes:

**Narrowed definition of "books and records":**
SB 21 creates an enumerated list of documents subject to stockholder inspection:

1. Certificate of Incorporation and amendments
2. Bylaws and amendments
3. Minutes of stockholder meetings and written stockholder consents
4. Formal communications to stockholders
5. Minutes of board and committee meetings/resolutions
6. Board-approved materials
7. Annual financial statements
8. § 122(18) agreements (charter-authorized stockholder agreements, post-Moelis)
9. Director independence questionnaires

**Expressly excluded**: Director, officer, or manager emails, text messages, and informal
communications are NOT "books and records" subject to inspection. This reverses a trend
of broad discovery in stockholder litigation.

**Heightened stockholder burden**: Stockholders must now state with "reasonable
particularity" both the purpose for inspection and the specific records sought.

**"Compelling need" standard**: Courts will evaluate whether the demand meets this
standard; fishing expeditions are now explicitly disfavored.

**Effective date and retroactivity**: SB 21 applies retroactively to demands not yet
pending as of February 17, 2025 (the introduction date). Actions and demands pending
before that date are not affected.

**Formation implication**: Do NOT include charter provisions that impose stockholder
liability for attorneys' fees in internal corporate claims (SB 21 added this explicit
prohibition to § 102).

[VERIFY] SB 21 was signed by the Governor on March 25, 2025. Confirm no subsequent
amendments have been enacted.

---

## Citation Quality Gates

Run these 5 gates silently before delivering any formation output. If any gate fails,
revise before delivering.

| Gate           | Rule                                                                                       | Fail Action                                              |
| -------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| **Source**     | Every statutory claim cites a specific DGCL section or established principle               | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow consistent format (e.g., "8 Del. C. § 102(b)(7)")                     | Fix format                                               |
| **Currency**   | Every cited DGCL provision checked for 2022–2025 amendments (officer exculpation, SB 21)   | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within Delaware corporate law; no other state's formation rules bleeding in | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden                                                  | Add confidence qualifier                                 |

---

## Self-Interrogation for CRITICAL Items

For any item classified as CRITICAL, apply this 3-pass review before delivery:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the
cited DGCL section? Would a Delaware attorney actually reach this conclusion? Is there
a counter-argument a Delaware court would accept?

**Pass 2 — Completeness**: Have all relevant DGCL sections been considered? Have any
2022–2025 amendments been checked? Are there federal tax dimensions (§ 83(b), § 409A)
not yet addressed?

**Pass 3 — Challenge**: What is the strongest argument that this item is not as severe
as classified? Under what circumstances might a reasonable startup counsel accept this
risk? Is the CRITICAL classification proportionate to the actual consequence?

**Action**: If any pass reveals a weakness, revise before delivery. Mark in the audit
trail: `self_interrogation: PASS` or `self_interrogation: REVISED`.

---

## Confidence Scoring

| Level        | Range     | Meaning                                             | Action                                                            |
| ------------ | --------- | --------------------------------------------------- | ----------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled Delaware law, clear DGCL text, no ambiguity | State with confidence                                             |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions    | State with brief caveat                                           |
| **Probable** | 0.60–0.79 | Good arguments but reasonable minds could differ    | State with explicit reasoning and contra-indicators               |
| **Possible** | 0.40–0.59 | Genuinely uncertain, competing interpretations      | Flag for qualified Delaware counsel with both sides               |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                             | Do not assert; flag as "[UNCERTAIN — Delaware counsel to advise]" |

---

## Anti-Patterns

What NOT to do when guiding Delaware entity formation:

1. **Recommending Delaware without confirming the company's operating state**: Delaware
   incorporation is standard for VC-backed companies, but a Delaware corp operating
   exclusively in, say, Wyoming or Montana with no VC ambitions may be better off
   incorporating locally to avoid Delaware franchise tax and foreign qualification costs.

2. **Setting authorized shares without considering franchise tax**: Authorizing 100M+
   shares "for flexibility" without explaining the Authorized Shares Method tax bill is
   negligent advice. Always calculate the franchise tax impact of the proposed authorization
   and present the Assumed Par Value method as the solution.

3. **Omitting the § 83(b) election from the formation workflow**: The 30-day window is
   absolute. Missing it cannot be corrected retroactively. This must be calendared and
   confirmed before the organizational consent is signed.

4. **Issuing options before a 409A valuation**: A company that issues options to employees
   before obtaining a 409A valuation has created potential § 409A violations for every
   option holder. There is no safe retroactive fix — the options were granted without a
   valid FMV determination.

5. **Treating IP assignment as a post-formation housekeeping item**: Every day that passes
   after formation without IP assignment agreements is a day of risk. If a founder departs
   or has a dispute before signing, the company's core IP may not be properly owned.

6. **Forgetting California foreign qualification**: A San Francisco startup incorporated
   in Delaware is doing business in California on day one. The $800/year minimum franchise
   tax is inescapable. Pretending it can be deferred exposes the company to retroactive
   penalties from the date operations commenced.

7. **Using the Authorized Shares Method for franchise tax**: For any startup with millions
   of authorized shares (standard VC structure), the Authorized Shares Method can produce
   a tax bill of $100,000+. The Assumed Par Value method almost always produces a lower
   bill. Never present only one method without checking both.

8. **Confusing § 141(f) (board written consent) with a meeting waiver**: Written consent
   under § 141(f) still requires a quorum to exist. A board with vacant seats may lack
   a quorum. Always verify quorum before relying on written consent for organizational
   actions.

9. **Omitting officer exculpation from the COI**: The August 2022 amendment allows
   officer exculpation under § 102(b)(7). New incorporations that omit it must later
   obtain stockholder approval to amend — an unnecessary friction that a single sentence
   at formation avoids.

10. **Naming the incorporator as a permanent officer or director**: The incorporator's
    role terminates upon filing the COI (unless the COI states otherwise). Officers and
    directors must be properly elected by the board and/or stockholders at the
    organizational consent stage — not assumed from the incorporator's role.

11. **Drafting bylaws with a fixed board size instead of a range**: Early-stage companies
    grow their boards. A bylaw specifying "the Board shall consist of three directors"
    requires a formal amendment every time the board expands. Use a range (e.g., "not
    fewer than one and not more than seven") with current board size set by resolution.

12. **Overlooking the quorum-and-vacancy trap**: If the certificate authorizes 5 board
    seats but only 3 directors are elected at formation, no quorum exists unless bylaws
    specify otherwise (minimum = majority of authorized seats). This can prevent the
    company from taking valid board action. Fill all authorized seats or reduce the
    authorized seat count in the bylaws immediately.

13. **Ignoring the 60-day window for stockholder written consents (§ 228)**: When
    obtaining stockholder written consent, all consents must be delivered within 60 days
    of the first dated consent. A consent obtained on day 61 is ineffective. In a
    multi-founder company, track each founder's signing date carefully.

14. **Authorizing blank check preferred without the requisite board language**: A certificate
    that says "the corporation may issue preferred stock" without the explicit delegation
    language under § 151(g) does not create true blank check preferred. The board must
    be expressly authorized to set series terms by resolution. Verify the COI language
    against the statutory standard.

15. **Treating SB 21 as only relevant to litigation**: The SB 21 prohibition on charter
    provisions imposing attorney fee liability on stockholders in internal corporate claims
    affects COI drafting. Review any form COI against this provision before filing —
    especially older form COIs that may predate SB 21.

16. **Forgetting to update the registered agent contact information**: Many startups
    appoint a registered agent and never update the contact person after the founding
    team changes. Service of process sent to a departed founder's contact creates missed
    lawsuit risk. The August 2025 amendments to § 132 impose explicit contact maintenance
    obligations.

17. **Not calendaring the Delaware franchise tax deadline**: The March 1 deadline is fixed.
    A $200 flat penalty plus monthly interest begins accruing immediately. For a startup
    managing cash carefully, this is an avoidable expense.

18. **Confusing Delaware "good standing" with multi-state good standing**: A Delaware
    Certificate of Good Standing confirms only Delaware compliance. It says nothing about
    whether the company is in good standing in California, New York, or other qualified
    states. Each state's good standing must be confirmed separately.

---

## Writing Standards

**For formation guidance delivered to founders:**

- Lead with what they must do, then explain why
- Active voice: "File the Certificate of Incorporation" not "The Certificate of
  Incorporation should be filed"
- Quantify: "$800/year minimum California franchise tax" not "significant annual tax
  obligation"
- Name the risk: "Missing the 30-day § 83(b) window is permanent and cannot be corrected
  retroactively" not "late filing may have tax implications"
- Short sentences; one point per sentence

**For formation guidance delivered to legal counsel:**

- Include DGCL section citations for every material point
- Flag [VERIFY] on any citation that has not been confirmed via legalcode-mcp
- Include confidence scoring on any item that is not definitively settled law
- Reference recent case law and legislative developments (SB 21, officer exculpation 2022)

**Quality gates before delivery:**

1. Can a first-time founder understand the CRITICAL items and why they are urgent?
2. Are all deadlines stated with exact dates or clear formulas, not vague timeframes?
3. Is every statutory citation either confirmed or flagged [VERIFY]?
4. Does the output make specific recommendations, not just list options?
5. Are the franchise tax calculations mathematically correct?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 3, search for current DGCL text for all cited sections
- Verify the August 2022 officer exculpation amendment is reflected in § 102(b)(7)
- Verify SB 21 March 2025 amendments to §§ 102 and 220 are current
- Verify August 2025 § 132 registered agent amendments
- Search for recent Delaware Chancery and Supreme Court decisions on formation,
  corporate governance, and § 102(b)(7)
- Mark verified citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with general knowledge of Delaware corporate law
- Mark all DGCL section references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Flag that statutory currency (especially 2022–2025 amendments) has not been independently
  confirmed — recommend counsel verify before relying on any provision

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-us-delaware-entity-formation"
  request_summary: "[Brief description of user's formation request]"
  formation_type: "Delaware C-Corporation"
  intended_use: "[VC-backed startup / Operating company / Holding company / Other]"
  operating_states: "[List of states where the company operates]"
  authorized_shares_structure: "[e.g., '10M common + 10M blank check preferred at $0.000001 par']"
  franchise_tax_method: "[Authorized Shares / Assumed Par Value Capital / Not calculated]"
  franchise_tax_estimate: "[$ amount or 'Not calculated']"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-delaware-formation-authority.md or 'Not created']"
  statutes_consulted:
    - "8 Del. C. § 102 — [VERIFIED or UNVERIFIED]"
    - "8 Del. C. § 102(b)(7) — [VERIFIED or UNVERIFIED]"
    - "8 Del. C. § 109 — [VERIFIED or UNVERIFIED]"
    - "8 Del. C. § 132 — [VERIFIED or UNVERIFIED]"
    - "8 Del. C. § 141(f) — [VERIFIED or UNVERIFIED]"
    - "8 Del. C. § 151 — [VERIFIED or UNVERIFIED]"
    - "8 Del. C. § 228 — [VERIFIED or UNVERIFIED]"
    - "8 Del. C. § 503 — [VERIFIED or UNVERIFIED]"
    - "IRC § 83(b) — [VERIFIED or UNVERIFIED]"
    - "IRC § 409A — [VERIFIED or UNVERIFIED]"
  sb21_reviewed: "[Yes / No — SB 21 March 2025 amendments to §§ 102 and 220]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  critical_items_flagged: "[List any CRITICAL issues identified]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  assumptions:
    - "[Any assumption made where user context was not provided]"
  limitations:
    - "This skill covers Delaware C-corporation formation only. LLC, LP, and other entity
      types require separate guidance."
    - "Federal securities law compliance (Rule 701, Reg D, state blue sky) is not covered."
    - "Tax advice (S-election, QSBS, partnership tax) requires a qualified CPA or tax
      attorney."
    - "This skill does not substitute for a Delaware-licensed attorney reviewing formation
      documents before filing."
  reviewer:
    "AI-assisted — requires review by Delaware-licensed attorney before relying on
    any provision for actual formation decisions"
```

---

## Output Format Template

```markdown
## Delaware C-Corporation Formation Advisory

**Request**: [Summary of user's formation request]
**Date**: [date]
**Intended Use**: [VC-backed startup / Operating company / Other]
**Operating States**: [list]

---

## Formation Recommendation Summary

**Entity**: Delaware C-Corporation
**Authorized Structure**: [e.g., 10M common + 10M blank check preferred at $0.000001 par]
**Franchise Tax Method**: [Assumed Par Value Capital — estimated $X/year]
**Immediate Action Items**: [Count of CRITICAL items]
**Confidence**: [HIGH / MEDIUM / LOW]

---

## CRITICAL Items — Act Immediately

[For each CRITICAL item:]

### [Item Name]

**Risk**: [Specific consequence if not done immediately]
**Action**: [Exact step to take]
**Deadline**: [Date or event-based trigger]
**Statute**: [DGCL citation or "[VERIFY]"]

---

## Certificate of Incorporation Analysis

### Required Elements

| Element           | Status                             | Notes   |
| ----------------- | ---------------------------------- | ------- |
| Corporate name    | ✅ Present / ⚠️ Issue / ❌ Missing | [Notes] |
| Registered office | ✅ Present / ⚠️ Issue / ❌ Missing | [Notes] |
| Registered agent  | ✅ Present / ⚠️ Issue / ❌ Missing | [Notes] |
| Authorized shares | ✅ Present / ⚠️ Issue / ❌ Missing | [Notes] |
| Incorporator      | ✅ Present / ⚠️ Issue / ❌ Missing | [Notes] |

### Optional Provisions

| Provision                        | Present? | Recommendation                       |
| -------------------------------- | -------- | ------------------------------------ |
| § 102(b)(7) director exculpation | [Yes/No] | [Add if absent]                      |
| § 102(b)(7) officer exculpation  | [Yes/No] | [Add if absent]                      |
| Blank check preferred (§ 151(g)) | [Yes/No] | [Add if VC-backed]                   |
| Forum selection clause           | [Yes/No] | [Recommend Delaware exclusive forum] |

---

## Franchise Tax Calculation

**Authorized Shares Method**:
Authorized shares: [X]
Tax: $[calculated]

**Assumed Par Value Capital Method**:
Total gross assets: $[X]
Total issued shares: [X]
Total authorized shares: [X]
Assumed par value: $[X/share]
Assumed par value capital: $[X]
Tax: $[calculated]

**Recommended method**: [Lower of the two] — saves $[X] vs. [higher method]
**Annual Report fee**: $50
**Total due March 1**: $[tax + $50]

---

## Organizational Consent Checklist

### Board Organizational Consent (§ 141(f))

| Action                           | Status    |
| -------------------------------- | --------- |
| Adopt Bylaws                     | ☐ Pending |
| Elect Officers                   | ☐ Pending |
| Authorize bank account           | ☐ Pending |
| Authorize founder stock issuance | ☐ Pending |
| [Additional items as applicable] | ☐ Pending |

### Stockholder Organizational Consent (§ 228)

| Action                                  | Status    |
| --------------------------------------- | --------- |
| Approve Bylaws                          | ☐ Pending |
| Elect initial directors (if not in COI) | ☐ Pending |

---

## Post-Formation Compliance Calendar

| Obligation                             | Jurisdiction | Deadline                     | Consequence        |
| -------------------------------------- | ------------ | ---------------------------- | ------------------ |
| § 83(b) election (per founder)         | Federal      | [30 days from grant = DATE]  | Permanent tax harm |
| Delaware Annual Report + Franchise Tax | Delaware     | March 1                      | $200 + 1.5%/month  |
| [California Statement of Information]  | California   | [90 days from qualification] | $250 penalty       |
| 409A valuation (if options planned)    | Federal      | Before first option grant    | § 409A exposure    |

---

## Issues Identified

### CRITICAL

[List each with action and deadline]

### HIGH (Complete Within 30 Days)

[List each with action]

### MEDIUM (Complete Within 90 Days)

[List each with action]

### LOW (Best Practice)

[List each]

---

## Disclaimers and Limitations

[Skill-generated from the Glass Box limitations section — statutory citations require
independent verification; tax advice requires CPA; Delaware attorney review required
before filing any formation documents.]

---

[Glass Box Audit Trail YAML]
```

---

## Localization Notes

This skill covers Delaware corporate law exclusively. When the analysis touches
multi-state issues:

- **[US-CA]** California-specific rules apply when the company operates in California.
  The $800/year minimum franchise tax, 8.84% corporate income tax, and 90-day Statement
  of Information deadline are California-specific. See Step 11c.
- **[US-FED]** Federal tax rules (§ 83(b), § 409A, QSBS under § 1202, S-election
  under § 1362) apply regardless of Delaware formation. These require a qualified CPA
  or tax attorney for advice beyond the framework in this skill.
- **[JURISDICTION-SPECIFIC]** IP assignment scope limitations vary by state (California
  Labor Code § 2870, Washington RCW 49.44.140, Minnesota, Illinois, North Carolina, Delaware).
  Confirm the applicable state's statute before finalizing IP assignment agreements.
- **[JURISDICTION-SPECIFIC]** "Doing business" definitions for foreign qualification
  purposes vary by state. Each state's standard must be applied to determine whether
  qualification is required.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis from deep research on the Delaware
General Corporation Law (Title 8, Delaware Code), Delaware Division of Corporations
guidance, and recent DGCL amendments (2022 officer exculpation amendment, SB 21 March
2025). Research sources include Delaware Division of Corporations official guidance,
Morgan Lewis / Mayer Brown / Cooley / Skadden publications on SB 21 and Delaware corporate
developments, and IRS guidance on §§ 83(b) and 409A. Modeled on the Legalcode quality
standard established by `legalcode-contract-review` and the multi-jurisdiction formation
framework in `legalcode-entity-formation-advisor`. All statutory citations carry
hallucination risk and should be verified against current Delaware Code before reliance.
