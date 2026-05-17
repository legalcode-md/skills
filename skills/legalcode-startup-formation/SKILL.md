---
name: legalcode-startup-formation
description: >
  Generates complete Delaware C-Corporation formation packages for founders and counsel.
  Produces all eight core formation documents: Certificate of Incorporation, Bylaws, Action
  by Incorporator, Initial Board of Directors Consent, Founders Restricted Stock Purchase
  Agreements (with vesting schedule), Confidential Information and Invention Assignment
  Agreements (CIIA), Section 83(b) Election Letters, and Indemnification Agreements.
  Use when incorporating a startup, forming a Delaware C-Corp, preparing founder documents,
  setting up founder equity and vesting, protecting company IP, or preparing for a seed or
  Series A financing. Covers DGCL §§ 102, 108, 109, 141, 145, 151; IRC § 83(b); IRS Form
  15620; California Labor Code § 2870; DTSA immunity notice. Validates the complete
  formation package against VC due diligence standards and common founder mistake patterns.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-6
context: fork
agent: general-purpose
---

# Legalcode Startup Formation

> **Disclaimer**: This skill provides a framework for AI-assisted startup incorporation
> and formation document drafting. It does not constitute legal advice. All outputs must
> be reviewed by a qualified attorney licensed in Delaware and in each founder's state of
> residence before execution. Laws and IRS procedures change — verify current requirements
> before relying on any provision described here, including DGCL amendments, Delaware
> franchise tax rules, and IRS §83(b) filing procedures. Statutory and regulatory
> references cited from research carry residual hallucination risk — verify against
> authoritative sources before use.

---

## Purpose and Scope

This skill generates a complete, VC-ready Delaware C-Corporation formation package. It
walks through the intake, drafts all eight standard formation documents, produces a
filing checklist, and validates the package against common founder mistakes and investor
due diligence expectations.

**Generates:**
- Certificate of Incorporation (DGCL § 102)
- Bylaws (DGCL § 109)
- Action by Incorporator (DGCL § 108)
- Initial Board of Directors Unanimous Written Consent
- Founders Restricted Stock Purchase Agreement(s) — one per founder, with vesting
- Confidential Information and Invention Assignment Agreement(s) — one per founder/initial employee
- Section 83(b) Election Letter(s) — one per founder, pre-filled for IRS filing
- Director and Officer Indemnification Agreement(s)

**Produces additionally:**
- Post-formation filing checklist with critical deadlines (especially the 30-day §83(b) deadline)
- Initial cap table summary
- Delaware franchise tax guidance (APV method election)
- Quality verification report against the 18-point formation checklist

**Does not:**
- Provide legal advice or replace qualified Delaware counsel
- Draft equity incentive plans or stock option agreements (see `legalcode-equity-incentive-plan-review`)
- Draft Series Seed / Series A preferred stock documents (see `legalcode-venture-financing-suite`)
- Handle non-Delaware entities (Delaware is the jurisdiction)
- Generate documents for public benefit corporations, LLCs, or LPs

---

## Jurisdiction and Governing Law

**Jurisdiction:** Delaware (primary — incorporation state). All corporate law analysis
is governed by the Delaware General Corporation Law (DGCL), Title 8 of the Delaware Code.

**Federal overlays:** IRC § 83 (restricted property / vesting), 17 U.S.C. § 101
(work-for-hire), 18 U.S.C. § 1833(b) (DTSA immunity notice).

**State-of-operations overlays:** Founders based in certain states have additional rights
and obligations that affect CIIA enforceability and §83(b) state filings:

| State | Key Statute | Impact on Formation Documents |
|-------|-------------|-------------------------------|
| California | Cal. Lab. Code § 2870–2872 | Mandatory CIIA carve-out notice; CA FTB copy of §83(b) election [VERIFY current FTB requirement] |
| Washington | RCW § 49.44.140 | Similar CIIA carve-out to CA § 2870 |
| Minnesota | Minn. Stat. § 181.78 | Similar CIIA carve-out |
| Illinois | 765 ILCS § 1060/2 | Similar CIIA carve-out |
| North Carolina | N.C. Gen. Stat. § 66-57.1 | Similar CIIA carve-out |
| Delaware | No equivalent | No statutory CIIA carve-out; maximum assignment enforceability |

**Foreign qualification:** A Delaware corporation must qualify as a foreign corporation
in every state where it "does business" (typically: any state where a founder/employee
is located or where the company has a physical office).

**[JURISDICTION-SPECIFIC]** This skill is scoped to Delaware C-Corporations only. If
the founders have a compelling reason to incorporate in another state, a different skill
or qualified counsel is needed.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
founder intent, the workflow pauses and asks when:

- The answer would materially change document content (e.g., vesting schedule, IP scope)
- Legal risk depends on facts only the founder can provide (e.g., pre-formation IP, prior inventions)
- Multiple valid structures exist and the choice has lasting consequences (e.g., share counts, option pool)

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

Accept founder information in any of these formats:
- **Structured intake form** pasted into the conversation (see Output Format Template — Intake Form)
- **Free-form description** ("I'm forming a Delaware C-Corp with two co-founders, 60/40 split, both in California...")
- **Partial information** — proceed with what is provided and ask for the rest

### Step 2: Gather Founder and Company Context

**⟁ CLARIFY** — Ask the user these questions in a single structured intake request.
Present as a numbered list. If any answers have already been provided, skip those questions.

**Company:**
1. **Legal name**: Proposed corporation name (include a backup — Delaware requires the name be distinguishable from existing entities)
2. **Business purpose**: One-sentence description of what the company does (used for the Certificate's purpose clause)
3. **State(s) of operations**: Where founders are located / where the company will initially operate (determines foreign qualification needs and state CIIA overlay)
4. **Fiscal year end**: Calendar year (December 31) or other? (December 31 is almost always correct for US startups)
5. **Registered agent**: Do you have a Delaware registered agent, or should the documents reference a placeholder? (Commercial agents: CT Corporation, Cogency Global, Harvard Business Services, Registered Agents Inc. — typical cost $100–$300/year)

**Founders (one block per founder):**
6. **Full legal name** and **mailing address** (needed for stock certificates and consents)
7. **Equity percentage** (negotiate before incorporation — hardest conversation to have post-incorporation)
8. **Cash consideration**: How much cash will each founder pay for their shares? (Market standard: par value × shares = $0.0001/share × number of shares. Any amount above par value becomes additional paid-in capital.)
9. **IP/services contribution**: Will each founder contribute pre-formation IP or services as partial consideration? If yes, describe what.
10. **Vesting commencement date**: Today, the company formation date, or a prior date (often founders' founding start date)?
11. **Vesting schedule**: Standard 4-year / 1-year cliff / monthly thereafter? Or different?
12. **Prior inventions**: Does each founder have prior inventions, side projects, or other pre-existing IP they wish to **exclude** from the CIIA assignment? If yes, list them.

**Officers (Initial):**
13. **CEO/President**: Name (usually the founding CEO)
14. **Secretary**: Name
15. **CFO/Treasurer**: Name (can be same person as CEO at formation)

**Share Structure:**

**⟁ CLARIFY** — Ask which share structure is appropriate:

- **Option A: Simple Common Only (pre-seed default)** — 10,000,000 shares Common Stock, $0.0001 par value. Simplest structure. Use when: no institutional VC investment is expected soon.
- **Option B: Common + Blank Check Preferred (VC-ready)** — 10,000,000 shares Common + 10,000,000 authorized but undesignated Preferred Stock, $0.0001 par value. Use when: planning a priced financing round within 12–18 months or expecting term sheets.
- **Option C: Custom** — Specify total authorized, classes, and par values.

*Why this matters*: Blank check preferred allows the board to create Series A/B/C preferred by board resolution (Certificate of Designations) without a stockholder vote each time. Without it, a stockholder vote is needed to authorize preferred stock before each financing.

**Option pool:**

**⟁ CLARIFY** — Ask whether to reserve an option pool at formation:

- **Option A: No pool at formation** — Issue all initial shares to founders. Create the option plan when you first need to grant options to employees. Maximizes founder ownership at formation.
- **Option B: Reserve [X]% at formation** — Reserve a block of authorized but unissued shares for future option grants. Creates a "shadow dilution" for founders now but avoids a later stockholder consent to expand authorized shares.

*Standard practice*: No formal option pool at formation (Option A). The option plan is typically adopted when the first non-founder employee joins.

### Step 3: Gather Legal Authority (legalcode-mcp)

If **legalcode-mcp** is connected, search for:
- Current text of DGCL §§ 102, 108, 109, 141, 145, 151 (verify 2025 amendments effective)
- IRS Form 15620 (current version, released November 7, 2024; online filing available July/August 2025)
- Current California Labor Code § 2870 text (for CIIA state overlay)
- Delaware franchise tax current rates and APV method formula

Save results to `/tmp/legalcode-formation-authority.md`.

**If legalcode-mcp is not connected:**
- Mark all statutory text with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed using the statutory references in this skill, all of which should be independently verified before execution

### Step 4: Generate Certificate of Incorporation

Draft the Certificate of Incorporation following DGCL § 102(a) mandatory provisions and
§ 102(b) optional provisions recommended for startups.

**Required provisions (DGCL § 102(a)):**

| Provision | Content to Draft |
|-----------|-----------------|
| Corporate name | Use founder's preferred name + "Inc." or "Corp." (confirm Delaware availability [VERIFY via Delaware Division of Corporations search]) |
| Registered office and agent | Insert agent name and Delaware street address |
| Business purpose | "The purpose of the Corporation is to engage in any lawful act or activity for which corporations may be organized under the General Corporation Law of the State of Delaware." (Broad language is standard and preferred — avoids restricting the business scope) |
| Authorized capital | Per Step 2 intake (Option A, B, or C) |
| Incorporator | Name and mailing address of the incorporator (typically a lawyer or paralegal; founders are rarely the incorporator) |

**Market-standard optional provisions (DGCL § 102(b)) — include all of the following:**

| Provision | Recommended Language Approach | Why Include |
|-----------|-------------------------------|-------------|
| § 102(b)(7) Director exculpation | Eliminate personal monetary liability for breach of fiduciary duty except for: (i) breach of duty of loyalty; (ii) bad faith/intentional misconduct/knowing law violation; (iii) § 174 violations; (iv) improper personal benefit; (v) direct officer conduct in corporate actions (2022 amendment) | Makes it possible to recruit independent directors; required by most VC investors |
| Exclusive forum selection (§ 115) | Delaware Court of Chancery as exclusive forum for all internal corporate claims | Reduces risk of out-of-state securities litigation |
| No preemptive rights | Explicitly exclude preemptive rights | VC investors will require this — it simplifies future financings |
| Blank check preferred (if Option B) | Board may by resolution designate series of Preferred Stock with specified rights under § 151 | Enables future preferred stock financings without a stockholder vote |

**2025 DGCL Amendments — verify compliance:**
- § 102(f): Confirm no fee-shifting provisions against stockholders (prohibited)
- § 144: New safe-harbor procedures for conflict-of-interest transactions (note in governance provisions)
- § 115(c): Optional multi-forum designation now permitted (Delaware court must be available)

**⟁ CLARIFY** — Ask about the forum selection clause:
- **Include standard exclusive forum (Delaware only)** — Court of Chancery is exclusive forum for all internal corporate claims. Widely standard post-*Salzburg* litigation wave.
- **Include expanded forum (Delaware + one federal court)** — For companies anticipating federal securities litigation. More protective but slightly more complex.
- **Omit forum clause** — Not recommended; leaves the company exposed to multi-forum litigation.

### Step 5: Generate Bylaws

Draft internal governance bylaws. **Bylaws are not filed with the state.**

**Key provisions to include:**

| Topic | Market-Standard Approach |
|-------|--------------------------|
| Board size | "Not less than one (1) nor more than [7]" — adjustable by board resolution |
| Board quorum | Majority of directors then in office |
| Board action without meeting | Permitted by unanimous written consent (DGCL § 141(f)) |
| Officer titles | CEO/President, Secretary, CFO/Treasurer (same person may hold multiple offices at formation) |
| Annual stockholder meeting | Required by DGCL § 211; typically held within 13 months of last annual meeting |
| Special meetings | Callable by the Board or by holders of a majority of voting stock |
| Stockholder record date | Board sets record date not more than 60 days before any meeting (DGCL § 213) |
| Indemnification | To the fullest extent permitted by DGCL § 145 (supplements the standalone Indemnification Agreement) |
| Amendment authority | Board may amend bylaws; stockholders may also amend by majority vote |
| Fiscal year | December 31 (unless founder specified otherwise in Step 2) |
| Uncertificated shares | Authorize the Board to issue uncertificated shares (avoids physical certificates — increasingly standard) |
| Electronic records | Permit electronic books, records, and consents |

**Omit from bylaws:**
- Supermajority voting thresholds (reserved for post-investment certificate amendments)
- Pre-negotiated protective provisions for preferred stock (set in Certificate of Designations at funding)

### Step 6: Generate Action by Incorporator

Draft the Action by Incorporator (written consent in lieu of organizational meeting).

**Must execute AFTER the Certificate is filed and accepted by Delaware — never before.**

**Required contents:**
1. Recitals: the Certificate has been filed and accepted; the incorporator has authority to act
2. ADOPT the Bylaws (attach as Exhibit A)
3. APPOINT the initial Board of Directors (full legal name + address of each initial director)
4. TERMINATE the incorporator's authority upon execution
5. Date and incorporator signature line

**⟁ CLARIFY** — Ask who will serve as initial directors:
- In a 2-founder company: both founders typically serve as directors at formation
- Note: at the first VC round, investors will require board seats and may require independent directors

### Step 7: Generate Initial Board of Directors Unanimous Written Consent

Draft the initial organizational consent of all initial directors. This is the primary
governance action that sets up the company for operations.

**Include all of the following resolutions:**

| Resolution | Content |
|------------|---------|
| 1. Ratify organizational documents | Ratify Certificate and Bylaws as adopted |
| 2. Elect officers | CEO, Secretary, CFO/Treasurer (names from Step 2) |
| 3. Authorize stock certificates / uncertificated shares | Approve form of certificate or authorize uncertificated shares under Delaware law |
| 4. Approve stock issuances | Authorize issuance of [X] shares of Common Stock to each founder at $0.0001/share (or other stated consideration) per the Restricted Stock Purchase Agreement |
| 5. Approve FSPA form | Approve the form of Founders Restricted Stock Purchase Agreement |
| 6. Approve CIIA form | Approve the form of CIIA / CIIAA |
| 7. Approve indemnification agreements | Approve form and authorize execution with each director and officer |
| 8. Set fiscal year | Fiscal year ending December 31 |
| 9. Open bank accounts | Authorize specified officers to open bank accounts |
| 10. Apply for EIN | Authorize specified officer to apply for federal EIN (IRS Form SS-4) |
| 11. Registered agent | Confirm appointment of registered agent |
| 12. Authorize S-Corp election waiver | Explicitly waive S-Corp election (a C-Corp cannot make an S-Corp election; confirm the company intends to remain a C-Corp) |
| 13. Foreign qualification | If founders are in a state requiring immediate foreign qualification (e.g., California), authorize the filing |
| 14. Authorize formation counsel | Authorize payment of legal fees for formation work |

**Attach as Exhibits:**
- Exhibit A: Bylaws
- Exhibit B: Form of Restricted Stock Purchase Agreement
- Exhibit C: Form of CIIA
- Exhibit D: Form of Indemnification Agreement

### Step 8: Generate Founders Restricted Stock Purchase Agreements

Draft one FSPA per founder. Each FSPA:

**Covers:**
- Number of shares purchased
- Purchase price per share (typically $0.0001)
- Total consideration (cash + any IP/services contribution)
- Vesting schedule (from Step 2 intake)
- Company repurchase right (unvested shares)
- Early exercise rights (optional)
- Transfer restrictions and right of first refusal (ROFR)
- Co-sale rights (optional)
- Lock-up agreement (optional, typically reserved for IPO)

**Vesting schedule — draft in precise terms:**

```
Total shares: [X,XXX,XXX]
Vesting commencement date: [DATE]
Cliff: [25%] of Total Shares vest on the [12]-month anniversary of the
  Vesting Commencement Date.
Monthly vesting (post-cliff): [1/48th] of Total Shares vest on each monthly
  anniversary of the Vesting Commencement Date following the Cliff Date,
  until the [48]-month anniversary.
Full vest: [48]-month anniversary of the Vesting Commencement Date.
```

**Repurchase right mechanics:**
- Company holds repurchase right over the Unvested Portion only
- Repurchase price: **lower of** (i) original purchase price ($0.0001/share) or (ii) then-current fair market value
- Exercise window: 90 days after the founder's termination of service (voluntary or involuntary)
- Mechanics: company sends written notice; payment within the exercise window; shares automatically revert if timely exercised
- Lapse: if company does not exercise within the window, the repurchase right lapses as to all unvested shares — the founder retains them

**Acceleration provisions:**

**⟁ CLARIFY** — Ask about acceleration:
- **No acceleration** (VC-preferred) — vesting continues unchanged through any acquisition; acquirer retains retention incentive
- **Double-trigger acceleration** (market standard for VC-backed) — acceleration on (i) Change of Control AND (ii) founder terminated without cause or resigns for good reason within 12–18 months post-closing
- **Single-trigger acceleration** (founder-favorable, disfavored by VCs) — full acceleration on Change of Control alone

*Why this matters*: VCs will negotiate this at Series A. Starting with double-trigger is the market standard and avoids a conflict at financing.

**Transfer restrictions and ROFR:**
- Shares are subject to the company's right of first refusal (ROFR) on any proposed transfer
- Permitted transfers: to trusts for estate planning, with board consent
- ROFR procedure: founder gives notice; company has 30 days to exercise at the same price

**Consideration section — specify precisely:**
- Cash portion: $[X] (number of shares × $0.0001 per share)
- IP/services portion: assignment of pre-formation IP and intellectual property contributions, as further described in the CIIA signed concurrently

**Legends on stock certificates / restriction notices for uncertificated shares:**
- Securities Act restrictive legend
- DGCL transfer restriction legend
- Repurchase right notice

### Step 9: Generate CIIA (Confidential Information and Invention Assignment Agreement)

Draft one CIIA per founder and per initial non-founder employee who will have access to
company confidential information or will be developing company IP.

**Assignment clause — use present-tense language:**

```
Employee hereby irrevocably assigns to the Company all right, title, and interest
in and to all Inventions that Employee may solely or jointly conceive, develop,
reduce to practice, or cause to be conceived, developed, or reduced to practice
during the period of Employee's employment by the Company.
```

*Do not use future-tense ("agrees to assign") — present tense effects an automatic
assignment. Future tense requires a court order to compel assignment.*

**Categories of assigned IP:**
- Inventions, discoveries, developments, improvements, innovations
- Software, code, algorithms, and documentation
- Patents and patent applications
- Copyrights and copyrightable works
- Trade secrets and confidential information
- Domain names and trademarks (with separate trademark assignment if needed)
- All IP created during the period of employment (whether or not within working hours, if using company resources or related to company business)

**Confidentiality obligations:**
- Broad definition of Confidential Information (business plans, technical data, financial information, customer lists, trade secrets)
- Obligation survives employment for the life of any trade secret + at least 3 years for other confidential information
- Standard carve-outs: information in the public domain, independently developed without use of confidential information, required disclosures to government (with prior written notice where legally permitted)

**Prior inventions schedule (Exhibit A):**

**⟁ CLARIFY** — For each founder, ask:

*"Do you have any inventions, software, creative works, or other intellectual property
created before your employment with the company that you wish to exclude from the
assignment? If yes, list them in Exhibit A — Prior Inventions. If no prior inventions,
write 'None.'"*

*Why this matters*: An empty schedule creates the strongest inference that all relevant
IP belongs to the company. A founder who omits relevant prior IP from the schedule
risks losing it to the company. A founder who over-discloses creates a gap that could
affect company IP ownership in due diligence.

**State-specific overlays — include for founders in these states:**

*California founders (Cal. Lab. Code § 2870–2872):*
```
NOTICE TO CALIFORNIA EMPLOYEES: The assignment provisions of this Agreement do not
apply to an Invention that Employee developed entirely on Employee's own time without
using the Company's equipment, supplies, facilities, or trade secret information,
except for Inventions that (i) relate at the time of conception or reduction to
practice to the Company's business or actual or demonstrably anticipated research or
development, or (ii) result from any work performed by Employee for the Company.
```

Include for all employees regardless of state: Washington (RCW § 49.44.140), Minnesota
(Minn. Stat. § 181.78), Illinois (765 ILCS § 1060/2), and North Carolina (N.C. Gen. Stat.
§ 66-57.1) have similar protections — if founders are in these states, adapt the notice
language accordingly [VERIFY current statutory text in each state].

**DTSA immunity notice (18 U.S.C. § 1833(b)) — required to access enhanced DTSA remedies:**

```
NOTICE OF IMMUNITY UNDER THE DEFEND TRADE SECRETS ACT: An individual will not be
held criminally or civilly liable under any federal or state trade secret law for
the disclosure of a trade secret that: (A) is made (i) in confidence to a federal,
state, or local government official, either directly or indirectly, or to an attorney;
and (ii) solely for the purpose of reporting or investigating a suspected violation
of law; or (B) is made in a complaint or other document filed in a lawsuit or other
proceeding, if such filing is made under seal. An individual who files a lawsuit for
retaliation by an employer for reporting a suspected violation of law may disclose the
trade secret to the attorney of the individual and use the trade secret information in
the court proceeding, if the individual files any document containing the trade secret
under seal and does not disclose the trade secret, except pursuant to court order.
```

**Moral rights waiver:**
```
To the extent that moral rights under applicable law cannot be assigned, Employee
hereby irrevocably and unconditionally waives all enforcement of such moral rights
to the fullest extent permitted by applicable law.
```

**Non-solicitation provisions** (optional — check enforceability in founders' states):
- Non-solicitation of employees: typically enforceable in most US states (narrower than non-competes)
- Non-solicitation of customers: enforceability varies; California Business & Professions Code § 16600 effectively voids non-solicitation of customers [VERIFY]

**⟁ CLARIFY** — Ask about non-compete provisions:
- **Omit non-compete entirely** (recommended for CA, WA, MN, ND, OK founders — statutorily void)
- **Include narrowly tailored non-compete for non-CA founders** — time-limited (typically 12 months post-termination), geographic scope, and scope of competitive activity must be reasonable
- **Include non-competition in employment agreement instead of CIIA** — separates IP assignment from restrictive covenants

*Why this matters*: California Business & Professions Code § 16600 voids non-competes in employment agreements; SB 699 (effective January 2024) extends this to agreements signed outside California. Including an unenforceable non-compete for a California founder may, in some circumstances, taint the CIIA — consult California counsel [VERIFY].

**Termination provisions:**
- Employment is at-will (if applicable under state law)
- Upon termination: return all company property; certify compliance with confidentiality obligations
- Post-termination disclosure: disclose inventions made within 6 months after termination if they relate to company business or use company information

### Step 10: Generate Section 83(b) Election Letters

Draft one §83(b) election per founder. **The 30-day deadline from the date of stock
issuance is absolute and non-waivable — missing it is a permanent, irreversible mistake.**

**Use IRS Form 15620 (released November 7, 2024) or a qualifying self-drafted statement
per Treas. Reg. § 1.83-2(e). Online filing is available via IRS.gov (launched July/August
2025) and is the IRS's preferred method.**

**Required information for each election:**

| Field | Content |
|-------|---------|
| Taxpayer name | Founder's full legal name |
| Taxpayer SSN/TIN | [To be completed by founder — do not include in draft] |
| Taxpayer address | Founder's home mailing address |
| Date of transfer | Date the FSPA was executed and shares were issued |
| Tax year for which election is made | Calendar year of the transfer date |
| Description of restrictions | Time-based vesting schedule per FSPA; company repurchase right over unvested portion at lower of original price or FMV |
| FMV per share at transfer | $[0.0001 per share] (fair market value at the date of the transfer — in a brand new startup with no assets, FMV ≈ par value) [VERIFY with a 409A valuation if the company has any significant pre-existing assets] |
| Number of shares transferred | [X,XXX,XXX] |
| Total FMV at transfer | $[X] (shares × $0.0001) |
| Amount paid | $[X] (total consideration paid, including cash + FMV of IP assigned) |
| Amount to include in gross income | $[Total FMV] minus $[Amount paid] = $[0 or near-zero for early-stage startups] |
| Service recipient (company) name and EIN | [Company name] — EIN to be completed after EIN application |
| Service recipient address | Company mailing address |
| Declaration | "I hereby elect, pursuant to §83(b) of the Internal Revenue Code of 1986, as amended, to include in gross income for the taxable year in which the property was transferred the excess (if any) of the fair market value of the property at the time of transfer over the amount paid for the property." |

**Filing instructions to include with each letter:**

```
SECTION 83(b) ELECTION FILING INSTRUCTIONS

CRITICAL DEADLINE: This election MUST be filed no later than [DATE — 30 days after
stock issuance date].

STEP 1 — ONLINE FILING (PREFERRED):
  1. Go to IRS.gov and navigate to "File a Section 83(b) Election Online"
     (requires ID.me account with multifactor authentication)
  2. Complete Form 15620 on the IRS website
  3. Submit electronically — you will receive immediate confirmation
  4. Download and retain the confirmation as proof of timely filing
  5. Do NOT also mail a paper copy if you file online

STEP 2 — MAIL FILING (ALTERNATIVE):
  If you cannot access the online portal:
  1. Print Form 15620 (or your completed self-drafted election statement)
  2. Sign under penalty of perjury
  3. Send by CERTIFIED MAIL with RETURN RECEIPT REQUESTED to:
     [Current IRS Service Center address for your state — verify at IRS.gov]
  4. Retain the certified mail receipt as proof of timely mailing

STEP 3 — PROVIDE COPY TO THE COMPANY:
  Provide a signed copy of this election to [Company Name] immediately upon filing.
  Keep for your corporate records.

STEP 4 — STATE FILING (if applicable):
  California: [VERIFY whether CA FTB currently requires a separate state 83(b) filing]
  Other states: consult your state tax advisor

STEP 5 — RETAIN DOCUMENTATION INDEFINITELY:
  Keep proof of filing (online confirmation or certified mail receipt) for the
  life of your holding period plus the applicable tax statute of limitations
  (typically 3–7 years from the sale of the shares).

IMPORTANT: The online filing portal caps submissions at 999,999 securities. Large
grants must use paper filing.
```

### Step 11: Generate Indemnification Agreements

Draft one indemnification agreement per initial director and per officer.

**Statutory authority:** DGCL § 145. This contractual agreement converts permissive
indemnification (where the board has discretion) into mandatory contractual indemnification.

**Core indemnification obligation:**

```
The Company shall indemnify Indemnitee to the fullest extent permitted by the DGCL
and other applicable law in connection with any Proceeding arising by reason of
Indemnitee's Corporate Status [as a director, officer, employee, or agent of the
Company or any affiliate].
```

**Coverage triggers:**
- Any civil, criminal, administrative, investigative, or arbitration proceeding
- Proceedings by reason of the Indemnitee's Corporate Status
- Derivative actions (by or in the right of the Company) — note: indemnification in derivative suits is subject to § 145(b) limits (expenses only; no judgments in favor of the company)
- Service at the Company's request to other entities (subsidiaries, investee companies)

**Mandatory advancement of expenses:**
```
The Company shall advance expenses (including attorneys' fees) incurred by Indemnitee
in defending any Proceeding within thirty (30) days after written request, subject to
Indemnitee's undertaking to repay such amounts if it is ultimately determined that
Indemnitee is not entitled to be indemnified.
```

**Important: advancement rights are independent of indemnification rights — the company
cannot condition advancement on a finding that indemnification will ultimately be available.**

**Exclusions — the following are NOT indemnifiable:**
- Dishonest, fraudulent, or malicious conduct adjudicated by final court judgment
- Actions taken not in good faith and not reasonably believed to be in the Company's best interest
- Improper personal benefit (DGCL § 145 prohibits indemnification for this)
- Section 16(b) Exchange Act short-swing profit disgorgement
- Claims covered by and paid under D&O insurance

**Response requirement:**
- Company must respond to indemnification requests within 60 days
- Failure to respond within 60 days creates a right to seek judicial enforcement

**Contribution right:**
If indemnification is unavailable for any reason, the Company shall contribute to the
Indemnitee's losses in proportion to the relative benefits received and relative fault.

**D&O insurance:**
```
The Company shall use commercially reasonable efforts to obtain and maintain in effect
a policy of directors' and officers' liability insurance. If the Company's D&O insurance
policy lapses or terminates, the Company shall use its best efforts to obtain a
substitute policy providing equivalent coverage.
```

**Tail coverage:**
Include a tail coverage provision requiring the Company to obtain at least a 6-year
discovery period ("tail") upon any Change of Control.

**⟁ CLARIFY** — Ask about who should receive indemnification agreements:
- **Minimum**: Each initial director and officer (CEO, Secretary, CFO/Treasurer)
- **Recommended**: All founders (in their capacity as founders, regardless of officer title)
- **Advisory board members**: Some companies extend indemnification to advisory board members — ask if the company has any advisors at formation

### Step 12: Generate Formation Summary and Filing Checklist

Produce a complete post-formation checklist with every action item, responsible party,
and deadline.

**Phase 1 — Pre-filing (before Certificate is submitted to Delaware):**
- [ ] Agree on founder equity split and vesting terms *(founders — do before anything)*
- [ ] Inventory pre-formation IP per founder *(founders — feeds CIIA Exhibit A)*
- [ ] Confirm company name availability in Delaware *(counsel / incorporator)*
- [ ] Select and engage Delaware registered agent
- [ ] Prepare Certificate of Incorporation

**Phase 2 — Filing:**
- [ ] File Certificate of Incorporation with Delaware Division of Corporations
  - Standard: 1–2 business days; expedited (same day/1-hour) available for additional fee
  - State filing fee: ~$89 (standard) or higher for expedited
- [ ] Obtain certified copy of Certificate *(required for bank accounts and foreign qualification)*

**Phase 3 — Organization (immediately after Delaware accepts the Certificate):**
- [ ] Incorporator executes Action by Incorporator *(after Certificate accepted — not before)*
- [ ] Board executes Initial Board Unanimous Written Consent
- [ ] Each founder signs Restricted Stock Purchase Agreement
- [ ] Founders pay stock consideration (cash + IP assignment)
- [ ] Each founder signs CIIA
- [ ] Directors and officers sign Indemnification Agreements
- [ ] Stockholders execute Initial Stockholder Consent (approving indemnification agreements)
- [ ] Issue stock certificates or record uncertificated shares in stock ledger
- [ ] Set up corporate minute book (physical or electronic)

**Phase 4 — CRITICAL: §83(b) Elections (must happen within 30 days of stock issuance):**
- [ ] **DEADLINE: [DATE — 30 days after stock issuance date]**
- [ ] Each founder files §83(b) election via IRS.gov online portal or certified mail
- [ ] Each founder provides copy of signed §83(b) election to the company
- [ ] Company retains copies in corporate records
- [ ] [If California founders]: Confirm whether CA FTB copy is required [VERIFY]

**Phase 5 — Ongoing Compliance:**
- [ ] Apply for federal EIN (IRS Form SS-4 online — same day; international founders via fax/mail)
- [ ] Open business bank account (requires: certified Certificate, EIN, board resolutions)
- [ ] Foreign qualify in each state where the company "does business"
  - Most common: founders' home state(s)
  - Documents: certified Delaware Certificate, Certificate of Good Standing, state application
- [ ] Register for state tax IDs in applicable operating states
- [ ] Obtain D&O insurance (pre-seed: ~$3,800/year for $1M–$3M limits)
- [ ] Set up cap table management software (Carta, Pulley, or equivalent)
- [ ] Set up corporate accounting (QuickBooks, Bench, or equivalent)
- [ ] File Delaware Annual Report + franchise tax (due March 1 each year)
  - **ELECT APV (Assumed Par Value Capital) method to avoid $75,000+ overpayment**
  - Default "Authorized Shares Method" on 10M authorized shares = ~$85,000–$100,000/year
  - APV method on early-stage startup ≈ $400 minimum

**Initial cap table summary — include in output:**

```
Cap Table — [Company Name], Inc.
Date: [Formation Date]

Name              | Shares | % (as-issued) | Vesting
------------------|--------|---------------|--------
[Founder 1]       |        |               | 4yr/1yr cliff
[Founder 2]       |        |               | 4yr/1yr cliff
Option Pool       |        |               | N/A (reserved)
Treasury / Unissued|       |               | N/A
TOTAL Authorized  | [10,000,000] | 100%   |

Note: This cap table does not include SAFEs, convertible notes, or
future preferred stock. Maintain in cap table software going forward.
```

### Step 13: Quality Verification

Before delivering the formation package, run the quality checks below.

**13a. Formation Document Completeness Check:**

| Document | Generated | Signed/Executed? | Critical Provisions Present |
|----------|-----------|-------------------|-----------------------------|
| Certificate of Incorporation | ☐ | ☐ | §102(b)(7) exculpation, authorized shares, registered agent |
| Bylaws | ☐ | ☐ | Board size, quorum, officer titles, indemnification |
| Action by Incorporator | ☐ | ☐ | Bylaws adopted, directors appointed, incorporator authority terminated |
| Initial Board Consent | ☐ | ☐ | Officers elected, stock issuances approved, CIIA approved |
| FSPAs (one per founder) | ☐ | ☐ | Shares, consideration, vesting schedule, repurchase right |
| CIIAs (one per founder) | ☐ | ☐ | Present-tense assignment, prior inventions exhibit, state overlay, DTSA notice |
| §83(b) Letters (one per founder) | ☐ | ☐ | All required fields per Form 15620, 30-day deadline prominent |
| Indemnification Agreements | ☐ | ☐ | Mandatory advancement, exclusions, D&O insurance obligation |

**13b. VC Due Diligence Readiness Check:**

Run this check to confirm the package is ready for institutional investor review:

- [ ] All shares are subject to vesting (no fully vested shares at formation without documented explanation)
- [ ] All founders have executed CIIAs assigning company IP
- [ ] Pre-formation IP has been assigned via CIIA or separate Technology Assignment Agreement
- [ ] §83(b) elections are filed within 30 days (or founders are aware of the absolute deadline)
- [ ] No outstanding options or warrants without proper board approval
- [ ] No side letters or undisclosed agreements between founders
- [ ] Cap table reconciles: authorized shares ≥ issued + reserved shares
- [ ] Corporate minute book is being maintained
- [ ] Delaware franchise tax is current (or company is in first year with no prior filing due)

**13c. Quality Verification — run before delivery:**

1. Run the 5 Citation Quality Gates (see Quality Assurance Framework below)
2. For any CRITICAL-tier issue identified, run the 3-pass Self-Interrogation
3. Confirm confidence scores are assigned for all material legal positions
4. Generate the Glass Box Audit Trail
5. Confirm that the §83(b) deadline is prominently displayed in the formation summary

---

## Document Status Classification

Classify each document and each provision within a document on a four-tier scale:

### COMPLETE — All required elements present and properly drafted

The document exists, contains all legally required and market-standard provisions,
and is ready for attorney review and execution.

**Example:** Certificate of Incorporation with DGCL § 102(a) mandatory provisions,
§ 102(b)(7) exculpation, blank check preferred (if selected), and forum clause.

**Action:** Deliver for review. Note any optional provisions not included.

### DEFICIENT — Document exists but missing important provisions

The document is present but lacks provisions that should be included. The deficiency
increases legal or business risk.

**Example:** Bylaws that omit indemnification language, or a FSPA that omits ROFR.

**Action:** Flag the specific missing provisions. Provide recommended language.
Indicate whether the gap is Tier 1 (material) or Tier 2 (recommended).

### MISSING — Required document not generated or executed

A document that is part of the standard formation package has not been included.
This creates legal or tax risk that may be difficult to remedy retroactively.

**Example:** CIIA not signed by a founder who contributed code before incorporation.

**Action:** Flag as MISSING. Explain the consequence. Provide the document for
immediate execution. Note any timing issues (e.g., CIIAs executed after a gap period
may require additional consideration under some states' laws [VERIFY]).

### CRITICAL — Absent or fatally defective; immediate remedy required

A condition that, if uncorrected, will result in permanent legal or tax harm or
render the formation package unfit for VC due diligence.

**Examples:**
- §83(b) election not filed within 30 days of stock issuance *(irremediable)*
- CIIA not executed before or concurrent with employment start *(creates IP ownership gap)*
- Certificate not filed before founders begin issuing shares *(shares may be invalid)*
- Pre-formation IP not assigned; VC will require this in due diligence *(may block financing)*

**Action:** Escalate immediately. Explain the specific harm. If still within the remedy
window (e.g., 83(b) deadline has not yet passed), provide emergency instructions.
Mark `CRITICAL` in bold and place the item first in the formation summary.

---

## Provision Priority Framework

When advising founders on what to prioritize, organize provisions into three tiers:

### Tier 1 — Required (Formation is legally defective or materially at risk without these)

- Certificate filed with DGCL-compliant mandatory provisions
- Founders' shares subject to vesting (or documented rationale for departure)
- §83(b) elections filed within 30 days *(absolute deadline — no exceptions)*
- CIIAs executed by all founders assigning all company-relevant IP
- Pre-formation IP assigned via CIIA or Technology Assignment Agreement
- Proper corporate authorization for all stock issuances (board resolutions)
- Delaware registered agent maintained at all times
- Annual Delaware report filed and franchise tax paid (due March 1)
- EIN obtained (required for bank accounts and tax filings)

### Tier 2 — Strongly Recommended (Material investor or governance risk without these)

- §102(b)(7) director exculpation in the Certificate
- Exclusive forum selection clause in the Certificate
- Blank check preferred stock authorization (if VC financing is anticipated)
- Indemnification agreements for all directors and officers
- D&O insurance (VC investors will require this at first priced round)
- DTSA immunity notice in CIIAs
- State-specific CIIA overlay for CA/WA/MN/IL/NC founders
- Double-trigger acceleration in FSPAs
- ROFR on founder share transfers
- Cap table management software from day one (Carta, Pulley, or equivalent)

### Tier 3 — Optional / Defer (Address at first financing round or when relevant)

- Equity Incentive Plan / ISO option plan (adopt when first employee option grants needed)
- Restricted stock units (RSUs) — generally not appropriate for early-stage
- Advisory board agreements
- Trademark applications (file when brand is established — before any public launch)
- Patent applications (consult IP counsel)
- IP audit (comprehensive IP inventory — typically done pre-Series A in due diligence)
- Anti-dilution provisions for founders (rare; VC investors will resist)

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering the formation package. If any gate fails,
revise before delivery.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every statutory reference cites a specific DGCL section, IRC provision, or established legal principle | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format** | All statutory citations follow a consistent format (e.g., "DGCL § 102(b)(7)"; "IRC § 83(b)") | Fix citation format |
| **Currency** | Every provision checked against current law (note: 2025 DGCL amendments to §§ 102, 144, 115, 220 are effective; IRS Form 15620 released November 2024; online §83(b) filing available from July/August 2025) | Flag "[CHECK CURRENCY — verify against current Delaware Code and IRS guidance]" |
| **Domain** | Analysis stays within Delaware corporate law and applicable federal tax law; no unauthorized assumptions from other state laws | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty is explicitly stated (e.g., California FTB §83(b) copy requirement is uncertain — marked [VERIFY]); never hidden | Add confidence qualifier |

### Self-Interrogation for CRITICAL Items

For any item classified as CRITICAL, apply this 3-pass self-interrogation before delivery:

**Pass 1 — Legal Chain Integrity:**
- Does the risk follow logically from the cited statutory provision?
- Would a Delaware court or the IRS actually reach this conclusion on these facts?
- Is there a counter-argument a sophisticated founder's counsel would make?

**Pass 2 — Completeness:**
- Have all relevant statutes, regulations, and IRS guidance been considered?
- Are there state law dimensions not yet addressed?
- Are there timing considerations that could affect the analysis?

**Pass 3 — Challenge:**
- What is the strongest argument that this item is NOT actually CRITICAL?
- Under what circumstances might a reasonable formation attorney accept this risk?
- Is the CRITICAL classification proportionate, or is this actually MISSING (DEFICIENT)?

If any pass reveals a weakness, revise before delivery. Mark the audit trail with
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

Assign a confidence level to each material legal position in the formation package:

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95–1.0 | Settled Delaware law, clear DGCL text, no ambiguity | State with confidence |
| **High** | 0.80–0.94 | Strong authority, minor interpretation questions | State with brief caveat |
| **Probable** | 0.60–0.79 | Good arguments but reasonable practitioners could differ | State with explicit reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuinely uncertain; state law may vary | Flag for attorney review with both sides |
| **Unlikely** | 0.0–0.39 | Weak basis, speculative, or jurisdiction-specific | Do not assert; flag as "[UNCERTAIN — counsel to advise]" |

**Key confidence calls in startup formation:**
- DGCL mandatory provisions (§ 102(a)): **Definite** — clear statutory text
- §83(b) 30-day deadline: **Definite** — absolute, non-waivable
- Present-tense IP assignment vs. agreement-to-assign: **High** — strong case law support but some nuance
- California CIIA § 2870 carve-out applicability: **High** for core provisions; **Probable** for edge cases
- CA FTB §83(b) copy requirement: **Possible** — marked [VERIFY]
- Double-trigger acceleration market standard: **High** — widely confirmed in market practice

---

## Glass Box Audit Trail

Include this audit record with every formation package delivered:

```yaml
glass_box:
  skill_name: "legalcode-startup-formation"
  mode: "Generation — Delaware C-Corp formation package"
  jurisdiction: "Delaware (US); state overlays as applicable"
  documents_generated:
    - "Certificate of Incorporation"
    - "Bylaws"
    - "Action by Incorporator"
    - "Initial Board Unanimous Written Consent"
    - "Founders Restricted Stock Purchase Agreement(s)"
    - "CIIA(s)"
    - "Section 83(b) Election Letter(s)"
    - "Indemnification Agreement(s)"
    - "Formation Checklist and Cap Table Summary"
  statutory_references_used:
    - "DGCL § 102 (Certificate of Incorporation)"
    - "DGCL § 108 (Organizational meeting / Action by Incorporator)"
    - "DGCL § 109 (Bylaws)"
    - "DGCL § 141 (Board of Directors)"
    - "DGCL § 145 (Indemnification)"
    - "DGCL § 151 (Authorized stock)"
    - "IRC § 83(b) (Section 83(b) election)"
    - "Treas. Reg. § 1.83-2 (83(b) election requirements)"
    - "IRS Form 15620 (standardized 83(b) form, released Nov. 7, 2024)"
    - "17 U.S.C. § 101 (work-for-hire)"
    - "18 U.S.C. § 1833(b) (DTSA immunity notice)"
    - "Cal. Lab. Code §§ 2870-2872 (CA CIIA carve-out)"
  legalcode_mcp: "Connected / Not connected [update before delivery]"
  research_reference_file: "/tmp/legalcode-formation-authority.md [if created]"
  key_dates_flagged:
    - "83(b) deadline: 30 days from stock issuance [ABSOLUTE]"
    - "Delaware Annual Report: March 1 each year"
    - "APV franchise tax election: at time of filing annual report"
  citations_verified: "[N VERIFIED] / [N UNVERIFIED — marked [VERIFY]]"
  confidence_summary: "HIGH — formation documents follow well-settled DGCL; tax positions (83(b) FMV, CA FTB filing) are Probable and flagged for verification"
  known_limitations:
    - "IRS Form 15620 is the current standardized form as of research date (March 2026)"
    - "IRS online filing availability verified as of July/August 2025 launch"
    - "CA FTB §83(b) copy requirement is marked [VERIFY] — practice may have changed"
    - "2025 DGCL amendments to §§ 102, 144, 115 effective — verify adoption in draft"
    - "Non-compete enforceability varies significantly by state — not addressed in this package beyond CIIA overlay notices"
    - "This package does not include a formal equity incentive plan or option grant documents"
  reviewer: "AI-assisted — requires review by qualified Delaware corporate attorney and tax advisor before execution"
```

---

## Anti-Patterns

What NOT to do when forming a Delaware startup. These are the most common, most damaging
mistakes founders make — and the ones most likely to surface in Series A due diligence.

1. **Missing the §83(b) election deadline.** The IRS 30-day deadline is absolute and has
   no exceptions. No court, no IRS ruling, no petition can cure a late §83(b) election.
   The founder will owe ordinary income taxes on the FMV of shares at each vesting date
   for the entire vesting period — potentially hundreds of thousands of dollars. There is
   no workaround. Set a calendar alert the day the shares are issued.

2. **Not executing CIIAs concurrently with incorporation.** A CIIA executed weeks or months
   after employment begins may be challenged for lack of consideration under some states'
   laws. IP created before the CIIA was signed may not be covered. VCs will ask: "When
   was the CIIA signed, and is there any gap between employment start and CIIA execution?"

3. **Failing to assign pre-formation IP.** IP created by founders before the company was
   incorporated — the app built in a garage, the algorithm developed as a side project, the
   datasets curated before the company existed — does not automatically belong to the company.
   It must be explicitly assigned via a Technology Assignment Agreement or CIIA covering
   pre-formation work. This is the #1 due diligence failure at Series A.

4. **No founder vesting.** A co-founder who departs after 6 months but holds 33% of the
   company with no vesting is a cap table liability. VCs will require that founders be on
   a vesting schedule, and if one is not already in place, they will impose one at Series A
   — often with less favorable terms and treating existing tenure as day one.

5. **Using an LLC instead of a C-Corp when VC funding is planned.** Institutional VC funds
   cannot invest in LLCs (flow-through tax treatment creates fund-level tax complications).
   Converting an LLC to a C-Corp is expensive, time-consuming, and tax-complicated. Form
   a Delaware C-Corp from day one if VC funding is anticipated.

6. **Using the default Authorized Shares Method for Delaware franchise tax.** A 10M authorized
   share corporation defaults to ~$85,000–$100,000/year in Delaware franchise tax.
   The Assumed Par Value Capital (APV) method typically yields the statutory minimum of $400
   for early-stage startups. Always elect APV when filing the annual report. Founders who
   overlook this discover the error when they receive a tax bill — or, worse, when Delaware
   voids their charter.

7. **Issuing shares without proper board authorization.** Options and stock grants without
   board approval are void. Options issued without a §409A valuation are taxable as ordinary
   income at the time of grant (under IRC § 409A — large penalties and interest). Every
   stock or option grant requires: (a) board approval, (b) appropriate securities law
   exemption, and (c) for ISOs, a current 409A valuation.

8. **Incorporating before agreeing on the equity split.** The hardest conversation between
   co-founders is the one about equity percentages. This conversation is ten times harder
   after incorporation — now there are legal documents to unwind, potentially triggering
   securities and tax issues. Have the equity split discussion before filing the Certificate.

9. **Using future-tense ("agrees to assign") language in CIIAs.** "Employee hereby assigns"
   (present tense) effects an automatic, immediate transfer of IP. "Employee agrees to assign"
   (future tense) creates only a contractual obligation, enforceable only through litigation
   or a court order compelling assignment. In a dispute, a departing founder might exploit
   this distinction. Use present-tense assignment language in all CIIAs.

10. **Failing to foreign qualify in the founders' home state.** A California co-founder
    working from home means the Delaware C-Corp is "doing business" in California and must
    file for California foreign qualification. Failure to do so can result in penalties,
    back taxes, and — in California — loss of the right to sue in California courts until
    the company qualifies retroactively. File the foreign qualification promptly.

11. **Omitting the §102(b)(7) director liability exculpation.** Without this provision, a
    director can be personally liable for damages for breaches of the duty of care. Most
    experienced independent directors will not serve on a board that lacks exculpation. VCs
    will require it. Including it at formation costs nothing; adding it later requires a
    stockholder vote.

12. **Cap table only in a spreadsheet.** A spreadsheet cap table does not enforce vesting
    schedules, track exercise windows, or produce investor-grade summaries. At Series A,
    VCs will require a Carta (or equivalent) cap table and will spend weeks reconciling a
    spreadsheet-based record. Start with cap table software.

13. **Single-trigger acceleration for founders.** While founder-favorable, single-trigger
    acceleration (vesting accelerates on any Change of Control) eliminates the founders'
    retention value in an acquisition. Acquirers will demand it be removed or require an
    escrow hold-back. VCs will push back at Series A. Double-trigger acceleration is the
    market standard — it protects founders against hostile termination while preserving
    the acquirer's retention incentive.

14. **Drafting non-compete provisions for California founders.** California Business &
    Professions Code § 16600 (strengthened by SB 699, effective January 1, 2024) voids
    employment non-compete agreements for California employees, including agreements signed
    before the employee moves to California. Including an unenforceable non-compete may
    complicate the enforceability of the CIIA as a whole in some circumstances [VERIFY with
    California employment counsel].

15. **Ignoring the 2025 DGCL amendments.** Effective 2025, Delaware amended §§ 102(f),
    144, 115, and 220. Specifically: fee-shifting provisions against stockholders are
    prohibited (§ 102(f)); conflict-of-interest transaction safe harbors have been updated
    (§ 144); and nine categories of "core corporate documents" must now be produced on
    books-and-records demand (§ 220 — note for governance practices). Use formation
    documents that reflect these amendments.

16. **Delaying incorporation while building the product.** IP created before incorporation
    must be assigned after the fact. Any IP created after a co-founder signs an employment
    agreement at a prior employer may be subject to that employer's CIIA. The longer founders
    delay incorporation, the larger the pre-formation IP assignment problem. Incorporate
    early, even before the product is complete.

17. **Not obtaining D&O insurance before adding outside directors.** Indemnification agreements
    are only as good as the company's ability to pay. An early-stage startup with no cash
    cannot indemnify a director who is sued. D&O insurance is the safety net. Pre-seed policies
    are available for ~$3,800/year. VCs will require D&O coverage before their partners join
    the board at the first priced round.

18. **Issuing restricted stock to advisors instead of granting options.** Advisors who receive
    restricted stock subject to vesting face the same §83(b) timing obligations as founders,
    but may not be sophisticated enough to file in time. Standard market practice is to grant
    advisors stock options (not restricted stock), typically vesting monthly over 2 years
    with no cliff, after the option plan is adopted.

---

## Writing Standards

When drafting formation documents, apply these quality gates before delivery:

1. **Use defined terms consistently.** Every capitalized term introduced in one document
   must be used with the same definition throughout that document. Cross-document consistency
   (e.g., "Vesting Commencement Date" used identically in the FSPA and the Board Consent)
   is also required.

2. **Date all documents.** Every formation document must be dated. The date matters for
   legal effectiveness (Action by Incorporator cannot predate Certificate acceptance) and
   for §83(b) deadline calculation.

3. **Use recitals to set context.** Each consent and agreement should open with "WHEREAS"
   or "RECITALS" clauses establishing the factual context. This aids interpretation and
   record-keeping.

4. **Be specific on share numbers.** Never use approximate numbers. If a founder receives
   4,000,000 shares, write "Four Million (4,000,000) shares."

5. **Attach exhibits explicitly.** Every exhibit referenced in a document ("as attached
   hereto as Exhibit A") must be prepared and attached. The CIIA's Prior Inventions
   Schedule (even if it says "None") is a required exhibit.

6. **Flag blanks clearly.** All information to be completed by the user (SSNs, EINs, bank
   account numbers) should be flagged with "[TO BE COMPLETED]" placeholders — never leave
   empty brackets.

7. **Plain language for instructions.** The §83(b) election filing instructions should be
   understandable by a non-lawyer founder. Avoid legal jargon in the instructions section.

8. **Separate documents, separate signatures.** Each formation document should be a
   standalone document with its own signature page(s). Do not combine unrelated documents
   into one instrument.

9. **Verify internal cross-references.** Section numbers cited in other sections must
   be accurate. Before delivery, verify that every cross-reference (e.g., "as defined in
   Section 2.3") points to the correct provision.

---

## External Tool Integration

### legalcode-mcp (preferred — if connected)

Use legalcode-mcp to verify:
- Current DGCL text (particularly §§ 102, 108, 109, 141, 145, 151 and 2025 amendments)
- Current IRS guidance on §83(b) elections (Form 15620, online filing procedures)
- California Labor Code § 2870 current text and any recent amendments
- Delaware franchise tax APV method current formula and rates
- Delaware Division of Corporations filing fee schedule (verify current fees)

Save findings to `/tmp/legalcode-formation-authority.md`. Mark legalcode-mcp-sourced
citations as VERIFIED in the Glass Box audit trail.

### Without legalcode-mcp

- Mark all statutory citations with [VERIFY]
- Note: `legalcode_mcp: "Not connected"` in the Glass Box audit trail
- Recommend the founder's attorney verify all statutory references before execution
- The formation package structure remains complete — only verification depth is reduced

---

## Output Format Template

Deliver the formation package in this structure:

```markdown
# [Company Name], Inc. — Delaware C-Corp Formation Package
## Prepared: [Date]

---

### CRITICAL DEADLINE
> §83(b) elections for all founders must be filed no later than:
> **[DATE — 30 days from stock issuance date]**
> This deadline is absolute. Missing it is irremediable.

---

## DOCUMENT SUMMARY

| Document | Recipient | Status | Key Dates |
|----------|-----------|--------|-----------|
| Certificate of Incorporation | File with Delaware | COMPLETE | File date: [DATE] |
| Bylaws | Internal | COMPLETE | Adopted: [DATE] |
| Action by Incorporator | Internal | COMPLETE | After Certificate filed |
| Initial Board Consent | Internal | COMPLETE | Date: [DATE] |
| FSPA — [Founder 1] | [Founder 1] | COMPLETE | Signed: [DATE] |
| FSPA — [Founder 2] | [Founder 2] | COMPLETE | Signed: [DATE] |
| CIIA — [Founder 1] | [Founder 1] | COMPLETE | Signed: [DATE] |
| CIIA — [Founder 2] | [Founder 2] | COMPLETE | Signed: [DATE] |
| §83(b) — [Founder 1] | File with IRS | COMPLETE | Deadline: [DATE] |
| §83(b) — [Founder 2] | File with IRS | COMPLETE | Deadline: [DATE] |
| Indemnification — [Director 1] | [Director 1] | COMPLETE | Signed: [DATE] |
| Indemnification — [Director 2] | [Director 2] | COMPLETE | Signed: [DATE] |

---

## INITIAL CAP TABLE

[Cap table summary — see Step 12]

---

## FORMATION CHECKLIST

[Full checklist — see Step 12, Phases 1–5]

---

## DOCUMENT 1: CERTIFICATE OF INCORPORATION
[Full text of Certificate]

---

## DOCUMENT 2: BYLAWS
[Full text of Bylaws]

---

## DOCUMENT 3: ACTION BY INCORPORATOR
[Full text]

---

## DOCUMENT 4: INITIAL BOARD OF DIRECTORS UNANIMOUS WRITTEN CONSENT
[Full text]

---

## DOCUMENT 5A: FOUNDERS RESTRICTED STOCK PURCHASE AGREEMENT — [FOUNDER 1]
[Full text]

## DOCUMENT 5B: FOUNDERS RESTRICTED STOCK PURCHASE AGREEMENT — [FOUNDER 2]
[Full text]

---

## DOCUMENT 6A: CONFIDENTIAL INFORMATION AND INVENTION ASSIGNMENT AGREEMENT — [FOUNDER 1]
[Full text — including Exhibit A: Prior Inventions Schedule]

## DOCUMENT 6B: CIIA — [FOUNDER 2]
[Full text — including Exhibit A: Prior Inventions Schedule]

---

## DOCUMENT 7A: SECTION 83(b) ELECTION LETTER — [FOUNDER 1]
[Full text — with filing instructions]

## DOCUMENT 7B: SECTION 83(b) ELECTION LETTER — [FOUNDER 2]
[Full text — with filing instructions]

---

## DOCUMENT 8: DIRECTOR AND OFFICER INDEMNIFICATION AGREEMENT
[Full text — one per director/officer, individually named]

---

## QUALITY VERIFICATION REPORT

[Completeness check table — Document Status Classification for each document]

[Glass Box Audit Trail — YAML block]

---

## NEXT STEPS

### IMMEDIATE (within 30 days of stock issuance):
1. [ACTION: File §83(b) elections]

### THIS WEEK:
2. [ACTION: Apply for EIN]
3. [ACTION: Open bank account]

### THIS MONTH:
4. [ACTION: Foreign qualify in [state(s)]]
5. [ACTION: Obtain D&O insurance]

### BEFORE FIRST EMPLOYEE:
6. [ACTION: Adopt equity incentive plan]
7. [ACTION: Set up cap table software]
```

---

## Localization Notes

This skill covers **Delaware C-Corps only**. Key variations if the company or founders
operate in other jurisdictions:

**California-headquartered companies:**
- Foreign qualify in California (California Secretary of State, Form S-1)
- Comply with California Corporations Code securities exemption (Cal. Corp. Code § 25102(f) [VERIFY]) for initial stock issuances to founders
- Note the CA §16600 non-compete prohibition applies to any employee who resides or works in California, regardless of where the company is incorporated
- Consider California's statutory minimum wage and labor law obligations once employees are hired

**New York-headquartered companies:**
- Foreign qualify in New York
- Note New York's relatively strict law regarding securities exemptions for founder stock issuances [VERIFY current NY exemption requirements]

**International founders (non-US citizens / non-US residents):**
- A US EIN application for a foreign-owned corporation must be submitted by fax or mail to the IRS (no online option for entities without a US responsible party with an SSN or ITIN)
- Foreign founders may have additional reporting obligations (FinCEN BOI Report under the Corporate Transparency Act; Form BE-15 for foreign direct investment [VERIFY current CTA enforcement status post-2025 litigation]; potential withholding tax issues on dividends)
- CFIUS review considerations if the company works in regulated industries (defense, critical technology, sensitive personal data) and founders or early investors are from CFIUS-designated countries [VERIFY]

**Corporate Transparency Act / BOI Report:**
As of [VERIFY current status], most new US corporations must file a Beneficial Ownership Information (BOI) report with FinCEN within [VERIFY current deadline]. Include a reminder in the formation checklist, but note that CTA enforcement has been subject to ongoing litigation and its current status must be verified [VERIFY as of the formation date].

---

## Provenance

Created by Legalcode, 2026-03-21. Original synthesis for Delaware C-Corp startup
formation based on:
- Delaware General Corporation Law (DGCL), Title 8, as amended through 2025 amendments
  (84 Del. Laws, including amendments to §§ 102, 115, 144, 220)
- IRC § 83(b) and Treas. Reg. § 1.83-2; IRS Form 15620 (released November 7, 2024)
- IRS online §83(b) election filing (launched July/August 2025)
- California Labor Code §§ 2870–2872 (inventor protection)
- 18 U.S.C. § 1833(b) (DTSA immunity notice)
- Primary research via web sources including: Delaware Division of Corporations, IRS.gov,
  Grant Thornton Tax Advisory (IRS Form 15620 guidance), Mintz (electronic §83(b) filing),
  Goodwin Law (online §83(b) filing), Baker Donelson (IRS §83(b) streamlining), Davis
  Wright Tremaine (§83(b) founder guide), DGCL 2025 amendments via Connolly Gallagher,
  Delaware Ball PLLC (franchise tax), Carta (option pool guidance), Foley Ignite
  (Delaware formation checklist)
- Repository patterns adapted from `legalcode-contract-review` (quality framework),
  `legalcode-entity-formation-advisor` (corporate-transactions category patterns)
