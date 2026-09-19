---
name: legalcode-security-collateral-review
description: Review security interest packages and collateral documentation across US, UK, and EU jurisdictions.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review security interest packages and collateral documentation across US, UK, and EU jurisdictions. Covers UCC Article 9 (attachment, perfection by filing/control/possession, priority rules, PMSI super-priority, fixture filings, continuation statements, 2022 digital asset amendments), deposit account control agreements (DACAs), investment property control, IP security interests (copyright §205 Copyright Office recordation, patent/trademark UCC vs. federal preemption circuit split), UK fixed and floating charges (Companies Act 2006 ss.859A-859Q registration, Re Spectrum Plus [2005] UKHL 41 fixed/floating test, crystallization), UK financial collateral (FCARs 2003), all-asset debentures, real property mortgages and deeds of trust (recording, SNDAs, Garn-St. Germain, cross-collateralization, dragnet clauses), intercreditor arrangements (first/second lien ICAs, unitranche FLFO, AAL standstill provisions), EU Financial Collateral Directive 2002/47/EC, secured party enforcement and remedies (UCC §§9-601–9-628, commercial reasonableness standard, deficiency calculations), bankruptcy interaction (§§362, 363, 544, 547, 548, 552, adequate protection), and secured party duties (UCC §§9-207, 9-210). Produces a collateral-package adequacy assessment with GREEN/YELLOW/RED/ CRITICAL classification per asset class, perfection gap analysis, priority conflict detection, and ranked remediation action plan.


# Legalcode Security Collateral Review

> **Disclaimer**: This skill provides a framework for AI-assisted security interest and collateral
> documentation review. It does not constitute legal advice. All outputs must be reviewed by
> qualified banking and finance counsel licensed in the relevant jurisdiction before use.
> Security interest law is highly technical, jurisdiction-specific, and changes frequently —
> verify all statutory citations and perfection requirements against current authoritative sources
> before relying on any analysis here. Case law and statutory references cited from memory carry
> hallucination risk — verify against authoritative sources before relying on them.
> Perfection failures can result in unsecured status in bankruptcy with significant economic
> consequences — do not rely on this skill alone to confirm collateral adequacy.

## Purpose and Scope

This skill reviews security interest packages, collateral documentation, and perfection mechanics
for secured financing transactions. It analyzes whether collateral is properly created, perfected,
and prioritized, identifies gaps that could result in unsecured status, and generates a ranked
remediation action plan.

**Covers:**

- Security interest creation and attachment (UCC §9-203 value / rights / authenticated agreement)
- Perfection by filing (UCC-1 financing statements, continuation, termination, debtor name rules)
- Perfection by control (deposit accounts via DACAs, investment property, electronic chattel paper)
- Perfection by possession (instruments, certificated securities, tangible chattel paper)
- IP security interests: patent (UCC filing), trademark (UCC filing), copyright (Copyright Act §205
  recordation with the US Copyright Office — federal preemption for registered works)
- PMSI super-priority analysis (§9-324: 20-day windows for goods; inventory notice requirements)
- Fixture filing requirements and real property priority conflict analysis (§9-334)
- After-acquired property clauses and proceeds tracing (§9-204, §9-315)
- UK fixed and floating charge classification (Re Spectrum Plus [2005] UKHL 41; Agnew [2001] UKPC 28)
- UK charge registration at Companies House (Companies Act 2006 ss.859A-859Q, 21-day window)
- UK financial collateral arrangements (Financial Collateral Arrangements (No.2) Regs 2003)
- UK all-asset debentures and Law of Property Act 1925 charges
- Real property mortgages, deeds of trust, and security deeds (recording, SNDAs, dragnet clauses)
- Cross-collateralization and multi-tier security package analysis
- Intercreditor arrangements: first/second lien ICAs, unitranche FLFO, Agreement Among Lenders (AAL)
- EU Financial Collateral Directive 2002/47/EC and UNCITRAL Model Law on Secured Transactions 2016
- UCC Article 9 enforcement procedures (§§9-601–9-628, commercial reasonableness, deficiency)
- Secured party duties (§§9-207, 9-210) and lender liability exposure
- Bankruptcy interaction: automatic stay (§362), cash collateral (§363), adequate protection,
  preference avoidance (§547), fraudulent transfer (§548), strong-arm (§544), post-petition
  security interests (§552)
- 2022 UCC amendments: controllable electronic records (CERs), digital asset security interests

**Does not:**

- Draft new security agreements or financing statements (request a drafting-specific skill)
- Provide legal advice or replace qualified banking and finance counsel
- Perform quantitative LTV calculations, collateral valuations, or appraisal analysis
- Cover project finance, real estate investment trusts, or Islamic finance as primary focus
- Review the underlying loan agreement or credit terms (see `legalcode-loan-agreement-review`)
- Review guaranty provisions in depth (see `legalcode-guaranty-agreement-review`)

**Related skills:**

- `legalcode-loan-agreement-review` — loan agreement clause-by-clause review including security overview
- `legalcode-guaranty-agreement-review` — guaranty analysis including suretyship defenses and anti-deficiency
- `legalcode-contract-review` — general commercial contract review framework

---

## Jurisdiction and Governing Law

This skill is **jurisdiction-agnostic** with focused coverage of US (UCC Article 9 / state law),
UK (English law / Scots law where noted), and EU considerations. The governing law of the security
agreement determines the applicable framework.

[JURISDICTION-SPECIFIC] Before reviewing any security package, identify:

- **Governing law** of the security agreement(s)
- **Jurisdiction of organization** of each debtor (determines UCC filing location for registered
  organizations; § 9-307)
- **Location of collateral** (for goods, real property, and fixtures)
- **Asset class** (determines perfection method — control, filing, possession, or certificate of title)
- **Sector** (financial services, IP-heavy, agricultural, real estate, digital assets — each has
  sector-specific perfection rules)

[JURISDICTION-SPECIFIC] Jurisdiction-specific mandatory rules to research per applicable law:

- **US**: State UCC Article 9 enactment status (particularly Alternative A vs. B for individual
  debtor names; 2022 digital asset amendment adoption status by state); state certificate-of-title
  statutes; state real property recording acts and anti-deficiency statutes (California CCP
  §§580a-580e, one-action rule CCP §726; Arizona A.R.S. §33-814; Texas Property Code Ch. 51)
- **UK**: Companies Act 2006 charge registration requirements; Financial Collateral Arrangements
  (No.2) Regulations 2003 SI 2003/3226; Land Registration Act 2002 for real property charges;
  Bills of Sale Acts 1878/1882 for individual debtors; Insolvency Act 1986 §245 floating charge
  avoidance and prescribed part rules (Enterprise Act 2002)
- **EU/Other**: EU Financial Collateral Directive 2002/47/EC (as implemented in each Member State);
  civil law security structures (German Sicherungsübereignung, French nantissement/hypothèque,
  Dutch pandrecht); Cape Town Convention (aircraft, rail)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming context,
the workflow pauses and asks when:

- The answer would change the perfection method analysis (e.g., control vs. filing)
- Multiple valid perfection paths exist and priority among them is unclear
- Jurisdiction questions affect the severity of a gap (e.g., California anti-deficiency exposure)
- The reviewing party's role changes the risk framing (lender vs. borrower perspective)
- Complexity of the security package warrants scoping the review

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

### Step 1: Accept the Security Package

Accept the collateral documentation in any of these formats:

- **Individual documents**: Security agreements, pledge agreements, control agreements (DACAs/SACAs),
  UCC-1 filings, UK charge certificates, IP security agreements, mortgage/deed of trust instruments
- **Document package or ZIP**: Full security package for a financing transaction
- **URL or CLM reference**: Link to documents in a document management system
- **Pasted text**: Collateral description, lien search results, or perfection checklist

If only a description of the transaction (not documents) is provided, flag that the review is
preliminary and will require document review to confirm any findings.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask the user:

1. **Which side are you on?**
   - Options: Secured Party / Lender, Borrower / Debtor, Purchaser of Collateral, Neutral (due
     diligence), Other
   - _Why this matters_: Risk framing reverses depending on perspective. A lender wants maximum
     perfection; a borrower wants minimum encumbrance. A purchaser wants to take free of existing liens.

2. **Transaction type?**
   - Options: Commercial loan / revolving facility, Real estate secured loan, Leveraged buyout
     (LBO) / acquisition finance, Asset-based lending (ABL), Equipment financing / PMSI,
     Receivables / invoice financing, Intercreditor / refinancing, Insolvency / distressed,
     Other
   - _Why this matters_: The priority issues differ significantly between first-lien senior secured
     loans, ABL facilities, and equipment PMSIs.

3. **Jurisdiction?**
   - Options: United States (UCC Article 9), United Kingdom (English law), European Union,
     Multi-jurisdiction, Other
   - _Why this matters_: Perfection methods and registration requirements differ fundamentally
     between US (filing + control), UK (registration at Companies House), and EU (directive
     implementation plus local law).

4. **Primary asset classes in the collateral package?**
   - Select all that apply: Accounts / receivables, Equipment / inventory, Deposit accounts,
     Investment securities, Real property / fixtures, Intellectual property (patents / trademarks /
     copyright), General intangibles / software, Equity interests in subsidiaries, Digital assets /
     cryptocurrency, All-assets / floating charge
   - _Why this matters_: Each asset class has different perfection requirements; the review depth
     for each depends on what's actually in the package.

5. **Deadline and deal context?**
   - Free text: closing date, transaction size, whether this is a review of an existing facility
     or a new origination, any known perfection issues or prior disputes.
   - _Why this matters_: A closing-day review of a $500M leveraged buyout requires different
     triage than an ongoing monitoring review of a $5M ABL.

### Step 3: Identify Governing Law and Research Jurisdiction-Specific Rules

Read the security agreement(s) and identify:

- Governing law clause
- Jurisdiction of organization for each debtor entity
- Location of primary collateral

Use **legalcode-mcp** to gather jurisdiction-specific legal authority:

1. **For US security interests**: Search for applicable state's UCC Article 9 enactment, any
   non-uniform amendments, state certificate-of-title statutes for vehicles and equipment,
   and applicable state anti-deficiency/one-action rules for real property.

2. **For UK security interests**: Search for current Companies House registration requirements,
   Financial Collateral Arrangements Regulations amendments, and any relevant recent case law
   on fixed/floating charge classification.

3. **For EU security interests**: Search for the applicable EU Member State's implementation
   of the Financial Collateral Directive and any local secured transactions law.

Save results to `/tmp/legalcode-collateral-research.md`.

**If legalcode-mcp is not connected:**

- Proceed with the analysis using general knowledge
- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — manual verification required"`

**⟁ CLARIFY** — If the governing law is unusual, missing, or conflicts between instruments
(e.g., security agreement governed by New York law but collateral located in California), ask
the user before proceeding. Governing law gaps should be flagged as YELLOW deviations.

### Step 4: Build the Collateral Inventory

Create a collateral inventory table:

| #   | Asset Class | Description            | Perfection Method Required            | Perfection Method Used | Status                 |
| --- | ----------- | ---------------------- | ------------------------------------- | ---------------------- | ---------------------- |
| 1   | [category]  | [specific description] | [filing/control/possession/recording] | [what was done]        | [VERIFIED/GAP/UNCLEAR] |

Flag each asset class where:

- No perfection documentation is present
- The perfection method used appears incorrect for the asset class
- The jurisdiction of perfection is ambiguous
- Continuation or renewal filings may be needed

### Step 5: Deep Topic Analysis — Clause-by-Clause Review

Analyze each applicable topic from the 18 collateral topics below. Mark each finding with a
severity classification: **GREEN / YELLOW / RED / CRITICAL**.

For each RED or CRITICAL finding, apply the **Self-Interrogation** 3-pass review before classifying.

**⟁ CLARIFY** — For large or complex security packages (multiple entities, multiple jurisdictions,
or significant real property portfolio), ask the user whether to perform a **full review** of all
18 topics or a **priority review** focused on:

- Critical perfection risk topics (Topics 1-6, 11)
- The user's stated focus areas
- Any RED/CRITICAL items discovered during the collateral inventory (Step 4)

### Step 6: Priority Conflict Analysis

After analyzing individual asset classes, assess the **priority stack**:

- Identify all competing claims on each collateral category
- Apply the first-to-file-or-perfect rule (UCC §9-322 or UK/EU equivalents)
- Flag any PMSI relationships requiring super-priority notice
- Identify any fixture filing conflicts with real property mortgagees
- Review intercreditor agreements (if multi-lender) against collateral package

**⟁ CLARIFY** — When the priority outcome depends on facts not in the documents (e.g., whether
a prior lien search was clean, or when a competing creditor first filed), ask the user for the
missing information rather than assuming.

### Step 7: Bankruptcy and Enforcement Analysis

For each RED or CRITICAL perfection gap, assess the bankruptcy impact:

- Would the gap result in unsecured status in a chapter 7 or chapter 11?
- Is there a preference avoidance risk (§547: perfection within 90 days of bankruptcy, with
  extended 1-year period for insiders)?
- Is there a fraudulent transfer risk (§548: security interest granted while insolvent without
  reasonably equivalent value)?
- Is there a UK §245 Insolvency Act risk (floating charge avoidance within 12 months / 2 years
  for connected parties unless consideration given)?

Flag each gap with a **Bankruptcy Exposure** note.

### Step 8: Identify Missing Perfection Actions

For each gap, identify the specific corrective action:

- File UCC-1 in [specific state filing office]
- Execute and deliver DACA with [bank name]
- Record security interest with US Copyright Office (COVA form)
- Register charge at Companies House within [date] (UK)
- Re-perfect in new state within 4-month window (debtor relocation)
- File UCC-3 continuation statement by [date] (5-year expiry approaching)
- File fixture filing in [county real property records]
- Deliver notice to competing secured party for PMSI inventory priority by [date]

### Step 9: Prioritization and Remediation Plan

Rank all identified gaps using the **Prioritization Framework** (see below). Produce a ranked
remediation action plan with:

- Owner (borrower's counsel / lender's counsel / title company)
- Deadline (especially for time-sensitive windows: 20-day PMSI, 21-day UK registration, 4-month
  debtor relocation)
- Priority tier (Tier 1 / Tier 2 / Tier 3)

**⟁ CLARIFY** — Where the cost of remediation is disproportionate to the collateral value, ask
the user whether to flag it as a monitoring item or escalate for closing condition.

### Step 10: Deliver the Collateral Adequacy Report

Produce the structured output using the **Output Format Template** (see below). Apply the
**Citation Quality Gates** and **Writing Standards** before delivery. Append the **Glass Box
Audit Trail** to every report.

---

## 18-Topic Deep Analysis Framework

### Topic 1: Security Interest Creation and Attachment (UCC §9-203)

**What to assess:** Verify the three attachment conditions are satisfied:

1. **Value given** by the secured party (typically advance of loan proceeds or binding commitment)
2. **Debtor has rights** in the collateral (debtor owns, licenses, or has power to transfer)
3. **Authenticated security agreement** describes the collateral; OR secured party has possession,
   delivery, or control

**Collateral description sufficiency (§9-108):**

- Must "reasonably identify" — specific listing, UCC category, quantity, or formula permitted
- **Supergeneric descriptions** ("all assets," "all personal property") are **insufficient** in a
  security agreement (though valid in financing statements) [VERIFY §9-108(c)]
- **Consumer transactions**: type-only description insufficient for commercial tort claims,
  consumer goods, security entitlements, securities accounts, commodity accounts
- **Commercial tort claims**: must be specifically described at time of attachment — after-acquired
  property clauses do NOT attach to commercial tort claims (§9-204(b)(2))

**After-acquired property (§9-204):**

- Generally permitted — "all inventory now owned or hereafter acquired" is standard
- **Consumer goods exception**: after-acquired consumer goods clause ineffective unless goods
  are accessions offered as additional security or acquired within 10 days after value is given

**Future advances (§9-204(c)):** Valid; priority dates from original filing (§9-323)

**Key review points:**

- Is the security agreement signed/authenticated by the debtor?
- Does the description cover all intended collateral (check for gaps: proceeds, supporting
  obligations, accessions, after-acquired)?
- Are commercial tort claims specifically described (not just "all commercial tort claims")?
- Is there a dragnet / all-obligations clause extending the security to all present and future
  obligations?

**Common RED issues:**

- Security agreement missing signatures / authentication
- Collateral description so vague it fails the §9-108 reasonable identification test
- Commercial tort claims not specifically described
- No proceeds clause — attachment to proceeds requires express or statutory authorization

---

### Topic 2: UCC-1 Financing Statement — Perfection by Filing

**What to assess:** Confirm the UCC-1 financing statement is properly filed and effective.

**Minimum contents (§9-502):**

1. **Debtor name** (correct legal name — the most frequent source of perfection failure)
2. **Secured party name** (or representative)
3. **Indication of collateral** (supergeneric descriptions valid here — "all assets" is sufficient)

**Debtor name rules (§9-503) — the most litigated issue in UCC filing:**

- **Registered organizations** (corps, LLCs, LPs): must use the name on the most recently filed
  public organic record in the jurisdiction of organization — trade names and abbreviations are
  INSUFFICIENT
- **Individuals**: **Alternative A** (majority of states) — must use the name on an unexpired
  driver's license; if no license, use individual name; **Alternative B** — use any of the
  following: individual name, surname + first personal name, or driver's license name [VERIFY
  which alternative applies in the filing state]
- Trusts: specific trust name or settlor name with trust notation (§9-503(a)(3))
- **Error test (§9-506)**: a name error is "seriously misleading" (and the filing ineffective)
  unless the filing would be retrieved under the filing office's standard search logic using
  the correct debtor name — this is a factual, not legal, test

**Filing location (§9-307):**

- **Registered organizations**: state of organization (not state of incorporation of parent)
- **Individuals**: state of principal residence
- **Non-registered organizations** (general partnerships, trusts without public registration):
  state where the chief executive office is located
- **US government entities**: District of Columbia
- **Foreign debtors** with no US establishment: District of Columbia

**Duration and continuation (§9-515):**

- **Standard**: 5 years from filing date — continuation required within 6-month window before lapse
- **Manufactured homes**: 30 years
- **Transmitting utilities**: indefinite until termination filed
- **Continuation (§9-515(d))**: effective for 5 additional years from pre-lapse expiration date
- Missed continuation = lapse = security interest becomes **unperfected** (and treated as never
  perfected against purchasers for value who gave value before the 4-month grace period)

**Name change and relocation (§9-507, §9-316):**

- Name change making filing seriously misleading: original filing remains effective only for
  collateral acquired **before** the change or within **4 months** after — new filing required
- Debtor relocation to another state: original filing remains effective for **4 months** after
  move — re-perfect in new state within 4 months or security interest becomes unperfected
- **Transfer to new debtor in another state**: 1-year window to re-perfect in new state

**Common RED issues:**

- Debtor name on UCC-1 differs from legal name on organic documents
- Filing in wrong state (e.g., filing in state of operations rather than state of organization)
- Continuation missed — 5-year lapse silently occurring
- UCC-1 covers fewer assets than the security agreement describes
- Advance filing before security agreement exists — flag for attachment verification

---

### Topic 3: Perfection by Control — Deposit Accounts and Investment Property

**What to assess:** Confirm control perfection for asset classes where filing alone is insufficient.

**Deposit accounts (§9-104):** Three methods of control:

1. Secured party **is the bank** maintaining the account
2. **Tri-party authenticated agreement (DACA)**: debtor, bank, and secured party agree in
   writing that bank will comply with secured party's instructions **without further debtor consent**
3. Secured party **becomes the bank's customer** with respect to the account

**Critical**: Filing a UCC-1 does NOT perfect a security interest in a deposit account (§9-312(b)(1)).
A security interest in a deposit account can ONLY be perfected by control. A common, serious
error is filing a UCC-1 that lists deposit accounts without executing a DACA.

**Springing control**: A DACA can give the secured party control for perfection purposes while
the debtor retains operational control of the account until a default event triggers the
secured party's exclusive control ("springing" DACAs). This is the market standard for most
revolving credit facilities.

**Investment property (§9-106, §9-314):** Control is perfected by:

- For **certificated securities**: delivery to secured party or broker/intermediary holding for
  secured party (§8-301)
- For **uncertificated securities**: either (a) agreement (§8-106(c)(1)) or (b) becoming
  registered holder
- For **security entitlements** / **securities accounts**: either (a) agreement with securities
  intermediary (SACA — securities account control agreement) or (b) becoming the entitlement holder
- Control beats filing for investment property priority (§9-328)

**Electronic chattel paper (§9-105):** Control requires the secured party to have control of a
single authoritative copy of the electronic record (§9-105(b)). Control continuously required
for perfection to remain effective.

**Letter-of-credit rights (§9-107):** Control requires the consent of the issuer or nominated
person that proceeds be paid to the secured party.

**Common RED issues:**

- Deposit accounts listed in UCC-1 but no DACA executed — deposit accounts unperfected
- Securities account listed without SACA — investment property perfection by filing only
  (control priority lost to other control holders)
- DACA executed but does not cover all deposit accounts at the institution
- "Springing" DACA triggers not clearly defined — ambiguity in activation mechanics

---

### Topic 4: Deposit Account Control Agreements (DACAs) — Deep Analysis

**What to assess:** Verify DACA execution and adequacy in detail.

**Tri-party structure:** DACA is executed by:

- **Debtor/Borrower**: the account owner
- **Depositary bank**: the financial institution holding the account
- **Secured party**: the lender or collateral agent

**Key DACA provisions to review:**

- **Account identification**: Specifically identifies each account by number — blanket "all
  accounts at this bank" language may be insufficient for some banks [VERIFY banking institution
  policy]
- **Acknowledgment of security interest**: Bank acknowledges the security interest
- **Instruction compliance**: Bank agrees to comply with secured party's instructions re: the
  account without debtor's consent (this is what creates "control")
- **Springing vs. blocked accounts**:
  - _Springing DACA_: Debtor retains right to direct funds until a trigger event (typically
    an event of default); on trigger, secured party gives "activation notice" and bank
    thereafter follows only secured party instructions
  - _Blocked DACA_: Secured party has immediate exclusive control; debtor cannot direct funds
    without secured party consent
- **Sweep mechanics**: Some DACAs include automatic sweep provisions (collected funds auto-swept
  to a concentration account or applied to reduce revolving borrowings)
- **Bank's right of offset**: Bank typically retains right to offset fees, service charges,
  and returned items — verify whether this primes the secured party's control
- **Account statements**: Bank agrees to send statements to secured party (information right)
- **Termination**: Requires secured party consent or payoff confirmation before account released
  from DACA

**Common RED issues:**

- DACA does not list all accounts — accounts opened after DACA execution not covered
- Bank retains offset rights that prime secured party's claim — effectively a super-priority lien
- Springing trigger definition too narrow (e.g., requires "payment default" but facility may
  have non-payment covenants as primary risk)
- DACA does not include a blocked account provision for cash collateral facilities
- Multiple DACAs at different banks — no centralized collection/sweep mechanism (ABL risk)
- DACA with foreign bank — control analysis may differ under local law [JURISDICTION-SPECIFIC]

---

### Topic 5: IP Security Interests

**What to assess:** Verify perfection method for each category of intellectual property.

**Copyright security interests:**

- **Registered copyrights**: Security interest must be recorded with the **US Copyright Office**
  under 17 U.S.C. §205. Filing a UCC-1 alone is **insufficient** for perfection against third
  parties for registered copyright works. The leading authority is _In re Peregrine Entertainment,
  Ltd._, 116 B.R. 194 (C.D. Cal. 1990) (federal Copyright Act preempts UCC for registered copyrights)
  [VERIFY — some courts have questioned the breadth of Peregrine's holding]
- **Unregistered copyrights**: UCC Article 9 filing governs — no Copyright Act preemption for
  unregistered works [VERIFY circuit split — some jurisdictions apply Peregrine to unregistered
  works as well]
- Copyright Office recording form: Form COVA (Cover Sheet for Recorded Documents); the underlying
  security agreement must be filed, not just a financing statement

**Patent security interests:**

- The Patent Act (35 U.S.C.) does not address security interests in patents
- **UCC Article 9 governs** — file UCC-1 in debtor's state of organization
- Some practitioners also record the security agreement with the **USPTO** as a precautionary
  measure under 35 U.S.C. §261, but this is NOT required for UCC perfection and does NOT
  substitute for UCC filing [VERIFY — *In re Cybernetic Services*, 9th Cir. 2000, held USPTO
  recordation does not preempt UCC for patents]
- However: failure to record an **assignment** (not security interest) at USPTO can affect
  validity of the patent itself — distinguish assignment vs. security interest

**Trademark security interests:**

- The Lanham Act does not address security interests in trademarks
- **UCC Article 9 governs** — file UCC-1 in debtor's state of organization
- USPTO recordation of trademark security interests is a best practice (recommended but not
  required for UCC perfection) [VERIFY]
- Key risk: **naked licensing** — if a secured party enforces and takes possession of a trademark
  without maintaining quality control over goods sold under the mark, the trademark may become
  unenforceable. Security agreements should include quality control provisions

**Domain names:**

- No federal registration system for security interests
- UCC Article 9 governs as general intangibles — file UCC-1
- Domain name registrar has no notice of security interest from UCC filing alone — consider
  whether registrar notification or escrow is appropriate

**Software:**

- Software embedded in goods: security interest follows the goods (UCC Article 9)
- Stand-alone software: general intangible — UCC-1 filing
- Software subject to open source or other license restrictions: collateral description may be
  limited by license terms — verify assignability of license

**Common RED issues:**

- UCC-1 filed for registered copyrights without Copyright Office COVA recording — perfection
  failure for all registered copyright works (often the most valuable assets in tech/media companies)
- Security agreement description of IP collateral uses only generic terms without identifying
  registered works, patent numbers, or trademark registrations
- No quality control provision for trademark collateral — naked licensing risk on enforcement
- Software licenses not assignable without licensor consent — security interest may not attach
  to the license (or enforcement right to take possession may be restricted)
- IP registered in different name than UCC-1 debtor name — chain of title gap

---

### Topic 6: Priority Rules and Conflict Resolution

**What to assess:** Analyze priority stack among all competing creditors and lien holders.

**First-to-file-or-perfect rule (§9-322(a)):**

1. **Perfected vs. perfected**: priority to the first party to **file OR perfect**, with no
   lapse in perfection between filing and perfection ("the race rule")
2. **Perfected vs. unperfected**: perfected interest prevails regardless of knowledge
3. **Unperfected vs. unperfected**: first to attach (§9-322(a)(3))

**Lien creditor priority (§9-317(a)):**

- Unperfected security interest is subordinate to a lien creditor whose lien arose **before**
  perfection (or filing, if earlier)
- Exception for PMSI: beats lien creditor if UCC-1 filed within **20 days** of debtor receiving
  collateral (§9-317(e))

**Buyer priority (§9-320):**

- A buyer in the ordinary course of business (BIOC) takes free of a security interest **created
  by the seller**, even if perfected and even with knowledge
- Farm products exception: BIOC rule does not apply to farm products — buyer takes subject to
  perfected security interest unless buyer complies with Food Security Act notice requirements

**Future advances (§9-323):**

- Priority of future advances generally dates from original filing
- Against lien creditors: advances made more than **45 days** after lien creditor's interest
  arose are subordinate unless made without knowledge of the lien, or pursuant to a prior
  commitment made without knowledge

**PMSI super-priority (§9-324):**

- **Goods (non-inventory)**: PMSI prevails if perfected when debtor takes possession or **within
  20 days** after — a 20-day grace period
- **Inventory**: PMSI prevails if: (a) perfected when debtor takes possession, AND (b) written
  notice sent to holders of prior conflicting security interests in same types of inventory **before**
  debtor takes possession; notice must describe the type of inventory covered
- **Livestock**: Same as inventory but prior notice effective for **6 months** rather than 5 years
- **Software**: Follows the PMSI status of goods in which software is embedded

**Deposit account priority (§9-327):**

- Control beats non-control; among multiple control holders: first to obtain control
- Bank's own security interest (banker's lien or right of offset) prevails over other secured
  parties unless bank has a DACA and the other party obtained control first

**Investment property priority (§9-328):**

- Control beats filing; among multiple control holders: first to obtain control; securities
  intermediary's own security interest in accounts it maintains takes priority over all

**Common RED issues:**

- Competing UCC-1 with earlier filing date discovered on lien search — senior lien
- PMSI inventory notice not sent before delivery — super-priority forfeited
- Deposit accounts subject to bank's senior offset rights that were not disclosed at closing
- Priority disagreement between co-lenders not addressed by an intercreditor agreement

---

### Topic 7: Fixture Filings

**What to assess:** Identify goods that may be fixtures and verify fixture filing status.

**Fixture definition (§9-102(a)(41)):** Goods become fixtures when they become so related to
real property that an interest in them arises under real property law. The test is state
real property law — varies by jurisdiction.

**Priority (§9-334):** A security interest in fixtures is generally **subordinate** to a
conflicting real property mortgage or deed of trust. Exceptions:

- **PMSI in fixtures**: priority over conflicting real property interest if perfected by
  fixture filing **before goods become fixtures** or **within 20 days** after
- **Readily removable** factory, office, or accounting equipment: perfected security interest
  (non-PMSI) can gain priority if perfected before the real property interest arises
- **Construction mortgage**: takes priority over goods that become fixtures during construction

**Fixture filing requirements (§9-502(b)):**

- Must comply with regular financing statement requirements **plus**:
  - Must describe the real property sufficiently to give constructive notice under real
    property law (sufficient for a real estate recording)
  - Must indicate that it is a fixture filing
  - Should include name of real property owner if debtor does not own the real property
- Filed in **real estate recording office** for the county where the property is located
  (not in the UCC central filing office)
- A fixture filing satisfies both real estate and UCC filing requirements

**Common RED issues:**

- Manufacturing equipment bolted to floor — may be a fixture requiring fixture filing
- HVAC, elevators, built-in IT systems in commercial real estate — typically fixtures
- Fixture filing not made — secured party subordinate to first mortgage holder
- Fixture filing made in UCC central filing office instead of real estate records

---

### Topic 8: After-Acquired Property and Proceeds Tracing

**What to assess:** Verify the security interest properly extends to proceeds and after-acquired property.

**After-acquired property (§9-204(a)):** A security agreement may cover after-acquired collateral
except:

- Consumer goods (unless accessions or acquired within 10 days after value given)
- Commercial tort claims (must be specifically described at time of attachment)

**Proceeds (§9-315):** Security interest automatically continues in identifiable proceeds of
collateral, including: money, accounts, chattel paper, instruments, investment property, and
general intangibles. Perfection of the security interest in proceeds:

- **Automatically perfected** (for 20 days) when proceeds are identifiable cash proceeds
- **Continues perfection** if: (a) proceeds are of a type the security interest was perfected in
  the original collateral, (b) collateral type authorizes filing against the type of proceeds, OR
  (c) proceeds are identifiable cash proceeds
- **Re-perfection required** after 20 days for non-cash, non-automatically-continued proceeds

**Commingled goods (§9-336):** Security interest in goods that become part of a product or
mass in which identity is lost continues in the product/mass as proceeds. When multiple secured
parties have interests in commingled goods, each has a proportionate interest.

**Accessions (§9-335):** Security interest in a whole may include accessions added to the
collateral; security interest in an accession may conflict with security interest in the whole.

**Common YELLOW issues:**

- Proceeds clause limited to proceeds of "sale" only — misses insurance proceeds, condemnation
  awards, and licensing revenues from IP collateral
- After-acquired property clause does not specifically include new IP registrations — gap if
  debtor files new patents or trademark registrations post-closing
- No provision for tracing proceeds through multiple investment layers (e.g., proceeds → deposit
  account → securities account)

---

### Topic 9: UK Fixed and Floating Charges

**What to assess:** Classify charges as fixed or floating under English law and identify risks.

**The test (Re Spectrum Plus [2005] UKHL 41; Agnew v CIR [2001] UKPC 28):**
A charge is **fixed** only if the chargor is **restricted from disposing of the charged assets**
without the chargee's consent. The parties' label is not determinative.

For **book debts / receivables**:

- A charge over uncollected receivables **plus** requirement to pay proceeds into an unrestricted
  current account = **floating charge** (Re Spectrum Plus)
- Charge over receivables **plus** genuinely blocked proceeds account from which chargor cannot
  draw = **fixed charge** (requires genuine restriction)

Classic floating charge characteristics:

1. Charge over a class of assets present and future
2. That class changes in ordinary course of business
3. Chargor may deal with assets in ordinary course until crystallization

**Crystallization:** Conversion of a floating charge to a fixed charge on a specific asset.
Methods:

- **Automatic crystallization**: Triggered by specified events (e.g., appointment of administrator,
  cessation of business, ceasing to carry on business in ordinary course) — automatic crystallization
  clauses are enforceable in English law [VERIFY recent developments]
- **Manual crystallization**: Chargee issues crystallization notice
- Crystallized floating charge has same priority as a fixed charge from the moment of crystallization

**UK insolvency disadvantages of floating charges (Insolvency Act 1986):**

- **§245 avoidance**: A floating charge created within **12 months** (or **2 years** for
  connected parties) before onset of insolvency is void unless consideration (new money,
  goods, services, reduction of debt) was provided at the time of or after the charge creation.
  The consideration must be given at the time of creation, not before.
- **Preferential creditors (§40/§175)**: In a receivership or winding up, preferential creditors
  (employees for unpaid wages up to £800 per employee [VERIFY current cap], holiday pay) rank
  ahead of floating charge holders but after fixed charge holders.
- **Prescribed part (Enterprise Act 2002, s.176A)**: A percentage of floating charge realisations
  must be set aside for unsecured creditors (the "prescribed part"). Currently calculated on a
  sliding scale on the first £10,000 (50%) and remainder (20%) up to a maximum of £800,000
  [VERIFY current cap].
- **Administration expenses (IA 1986 §175(2)(a))**: Expenses of an administration rank ahead
  of floating charge holders.

**Common RED issues:**

- UK security agreement describes charge as "fixed" over receivables but does not restrict
  debtor from collecting and using proceeds — will be recharacterized as floating by an
  administrator (Re Spectrum Plus risk)
- Floating charge created within 12 months of insolvency without new consideration —
  avoidance risk under §245
- Security interest extends over assets subject to third-party consent restrictions —
  floating charge may not attach to such assets at all

---

### Topic 10: UK Charge Registration (Companies Act 2006, ss.859A-859Q)

**What to assess:** Verify timely and complete registration of all charges at Companies House.

**Registration requirement (s.859A):** A UK company must deliver particulars of any charge to
the registrar (Companies House) **within 21 days** of charge creation. The 21-day period runs
from the date of creation, not the date of the instrument.

**Required particulars (s.859D):**

- Company name and registration number
- Date of creation of the charge
- Names and addresses of the chargees (or first four if more than four)
- Whether charge is or includes a floating charge, and if so its scope
- Whether the charge contains a negative pledge clause
- Short particulars of property/undertaking charged
- Whether any land (UK), ships, aircraft, or IP is subject to the charge
- If it is a floating charge that contains a provision restricting it from ranking equally
  with later charges, or whether it will rank as a fixed charge on crystallization

**Certificate of registration (s.859I):** A certificate of registration issued by the registrar
is conclusive evidence of timely registration.

**Consequences of non-registration (s.859H):**

- The charge is **void** as against a liquidator, administrator, or any creditor of the company
  to the extent it purports to create a security interest
- The underlying debt obligation remains valid and enforceable (it becomes an unsecured claim)

**Court extension (s.859F):** Application to court for extension of the 21-day period
possible where failure was accidental, inadvertent, or not prejudicial to creditors.

**Charges over overseas property (s.859Q):** Charges over property outside the UK are
registrable if created by a UK company (i.e., registered in England and Wales, Scotland, or
Northern Ireland).

**Scottish law note [JURISDICTION-SPECIFIC]:** Floating charges over Scottish assets are
governed by the Companies Act provisions but also by the Scots law of moveable property
(Companies (Floating Charges) (Scotland) Act 1961 / Companies Act 2006 provisions).
Charges over land in Scotland are regulated by the Land Registration etc. (Scotland) Act 2012
and Scots law conveyancing requirements.

**Common CRITICAL issues:**

- UK charge created but particulars not delivered to Companies House within 21 days — charge void
  against administrator / liquidator from the outset (no cure other than court order)
- Charge particulars submitted but company number incorrect — registrar may reject or issue
  certificate with error
- Charge extended or amended — amended particulars may require fresh registration depending
  on the nature of the amendment
- Foreign company with UK establishment — charges over UK assets may be registrable [VERIFY
  Overseas Companies Regulations 2009]

---

### Topic 11: UK Financial Collateral Arrangements (FCARs 2003)

**What to assess:** Determine if the security interest qualifies as a "financial collateral
arrangement" and assess available protections.

**Qualification criteria (FCARs 2003 SI 2003/3226, reg.3):**
The arrangement must be:

1. Between parties that are not both individuals
2. Over "financial collateral": cash (money credited to an account), financial instruments
   (shares, bonds, units in collective investment undertakings), credit claims [VERIFY
   applicable EU/UK regime]
3. The collateral must be **provided** — i.e., in possession or under the control of the
   collateral taker, or in the case of a title transfer arrangement, transferred

**Benefits of FCA status:**

- **Exemption from general insolvency law** restrictions: enforcement is not subject to the
  automatic stay or moratorium that would otherwise prevent enforcement
- **Close-out netting** enforceable even in insolvency of the collateral provider
- **No registration requirement** under the Companies Act charge registration regime
  (if the arrangement qualifies as a FCA)
- **Enforcement** without court order and without standard notice periods
- **Appropriation right**: the collateral taker may appropriate the financial collateral
  (take title) in satisfaction of the secured obligation without formal sale process (if the
  arrangement provides for this)

**Limitation:** FCARs apply narrowly — only to financial collateral (cash, financial
instruments). General business collateral (inventory, receivables, equipment) does not qualify.

**Common YELLOW issues:**

- Lender relies on FCARs exemption from registration but arrangement does not qualify as
  FCA because collateral is not "provided" (control or possession not established)
- Appropriation right included but valuation methodology not specified — risk of challenge
  if appropriation price is not commercially reasonable

---

### Topic 12: Real Property Mortgages and Deeds of Trust

**What to assess:** Review real property security documentation and recording status.

**US real property security instruments [JURISDICTION-SPECIFIC by state]:**

- **Mortgage**: Two-party instrument; mortgagor grants lender a lien on real property as
  security; enforcement requires judicial foreclosure in "lien theory" states (NY, FL, etc.)
- **Deed of trust**: Three-party instrument (borrower/trustor, trustee, beneficiary/lender);
  trustee holds legal title; non-judicial foreclosure via trustee's sale permitted in "title
  theory" and many "intermediate theory" states (CA, TX, CO, VA, etc.)
- **Security deed (deed to secure debt)**: Used primarily in Georgia; borrower conveys
  fee title to lender as security, with obligation to reconvey on payment

**Recording requirements:**

- Must be recorded in the real property records (deed records / land records) of the county
  in which the property is located
- Recording provides constructive notice to subsequent purchasers and encumbrancers
- Race-notice and notice recording acts: priority generally to first to record with
  notice analysis varying by state

**Title insurance:** ALTA lender's title insurance policy customarily required; protects
lender against defects in title and encumbrances not shown in public records. ALTA endorsements
for specific risks (survey, zoning, environmental, access, etc.) to be confirmed.

**Assignment of leases and rents (ALR):** Separate instrument (or provision in mortgage/DOT)
assigning rents and leases to lender as additional collateral. Key provision: "absolute
assignment with license back" to borrower allows lender to perfect assignment without
actually collecting rents (constructive possession). Lender's right to collect rents on
default (enforcement of absolute assignment) typically requires notice to tenants.

**Subordination, Non-Disturbance, and Attornment (SNDA):** Agreement among landlord/borrower,
tenant, and lender: (a) tenant's lease subordinated to mortgage (Subordination); (b) lender
agrees not to disturb tenant's possession on foreclosure (Non-Disturbance); (c) tenant agrees
to attorn to (recognize) lender or successor as landlord (Attornment). Required by major
institutional tenants; important to lender for maintaining revenue stream on enforcement.

**Cross-collateralization clauses:** A provision extending the security of one mortgage to
secure multiple loans — "the lien of this deed of trust secures all present and future
obligations of the borrower to the lender." Can create dragnet lien exposure beyond anticipated
secured obligations. Some states restrict enforceability. [JURISDICTION-SPECIFIC]

**Dragnet clauses:** Similar to cross-collateralization — extends collateral to obligations
beyond the original secured debt. Enforceability varies significantly by state. Courts generally
require clear and unambiguous language; some states impose stricter scrutiny for
"unrelated" future obligations.

**Due-on-sale clauses:** Garn-St. Germain Depository Institutions Act (12 U.S.C. §1701j-3)
generally preempts state restrictions on enforcing due-on-sale clauses in real estate mortgages
held by federally chartered institutions. Certain exemptions (e.g., transfers by devise, transfers
to relatives upon death, subordinate lien transfers) limit enforcement.

**Anti-deficiency statutes [JURISDICTION-SPECIFIC by state]:**

- **California** (CCP §§580a-580e, §726): One-action rule (§726) — lender must foreclose
  on real property collateral first before pursuing personal liability; anti-deficiency rules
  (§§580b, 580d) prohibit deficiency judgments after non-judicial foreclosure and in
  purchase-money situations
- **Arizona** (A.R.S. §33-814): Anti-deficiency protection for residential property on
  2.5 acres or less after trustee's sale
- Other states have varying anti-deficiency protections [VERIFY state-specific rules]

**UK real property charges [JURISDICTION-SPECIFIC]:**

- **Legal charge** over land registered at HM Land Registry (Land Registration Act 2002)
- Must be by deed; registered charge has priority from the date of registration
- UK mortgage market distinguishes between registered and unregistered land
- Fixed charge over land — not subject to floating charge crystallization issues

**Common RED issues:**

- Mortgage/DOT not recorded — no constructive notice, priority subordinate to subsequent
  recorded encumbrancers
- ALR executed but no "absolute assignment" language — merely a pledge (weaker)
- Missing SNDA with major tenants — foreclosing lender may face tenant challenges to lease
- Dragnet clause included without borrower awareness — scope may extend beyond expected secured obligations
- California borrower: lender pursuing deficiency without first foreclosing — one-action rule violation

---

### Topic 13: Cross-Collateralization and Multi-Tier Security Structures

**What to assess:** Analyze the cross-collateralization structure and equity pledge mechanics.

**Cross-collateralization:** One pledge of collateral secures multiple obligations. Key issues:

- Which obligations are cross-collateralized? All present and future? Specific facilities only?
- Are all cross-collateralized obligations owed to the same lender entity?
- In a syndicated context: can a lender enforce cross-collateralization against a borrower
  where the cross-collateralized obligation is owed to a different lender in the syndicate?

**Equity pledge (pledge of equity interests in subsidiaries):**

- Standard practice in leveraged finance: parent pledges 100% of stock/LLC interests in
  each operating subsidiary
- **US perfection**: UCC-1 filing (for certificated securities, also physical delivery of
  stock certificate with blank stock power); UCC §9-106 control for investment property
- **US: 65% cap for CFCs**: Pledging more than 65% of voting stock of a controlled foreign
  corporation (CFC) can trigger deemed dividend income — standard market practice is 65%
  of voting stock / 100% of non-voting stock of CFCs
- **UK subsidiary pledges**: Share charges governed by English law; registration at Companies
  House required if shares pledged are shares in a UK company created by a UK company chargor
- **Multi-tier structures**: Each subsidiary entity must separately execute security documents;
  guaranty and security package must cover each entity in the credit group

**Guarantor structural considerations:**

- In multi-entity corporate groups: upstream guarantees (subsidiary guarantees parent's debt)
  may trigger "financial assistance" issues in UK (Companies Act 2006 §§678-681) or fraudulent
  conveyance risk in US (§548) if subsidiary receives insufficient benefit
- **Limitation language (guaranty cap)**: Upstream guarantors typically include limitation
  language restricting guaranty obligations to the maximum amount that would not render the
  guarantor insolvent

**Common RED issues:**

- Equity pledge covers less than 100% of a subsidiary's equity — minority interest holders
  could block enforcement
- CFC equity pledge exceeds 65% voting threshold — adverse tax consequences
- No perfection of equity pledge (UCC-1 not filed; stock certificates not delivered)
- Upstream guaranty or security from subsidiary without insolvency savings language —
  fraudulent conveyance risk in US / financial assistance risk in UK

---

### Topic 14: Intercreditor Arrangements

**What to assess:** Review intercreditor agreements for enforceability and internal consistency
with the collateral package.

**First lien / second lien structure:**

- **Payment subordination**: Second lien lenders' claims to proceeds of collateral are
  subordinated to full payment of first lien obligations in enforcement/insolvency scenarios;
  current cash pay of second lien interest typically permitted unless a payment blockage
  notice has been delivered
- **Lien subordination**: Second lien security interest is subordinated in priority to first
  lien security interest; second lien collateral agent is typically required to execute and
  deliver a "subordination and intercreditor agreement"
- **Standstill period**: Second lien creditors are typically prohibited from enforcing security
  or taking other enforcement actions for **90 to 180 days** after written notice of an event
  of default (standstill period), during which first lien creditors have exclusive enforcement right
- **Purchase option**: First lien creditors typically have the right to purchase second lien
  obligations at par (plus accrued interest) before second lien creditors may enforce
- **Lien release**: Actions by first lien collateral agent to release collateral in connection
  with permitted asset sales bind second lien holders; second lien collateral agent is deemed
  to consent to such releases
- **Bankruptcy provisions**: Second lien creditors agree not to object to DIP financing or
  use of cash collateral by first lien lenders; second lien creditors agree not to challenge
  first lien perfection or priority in bankruptcy

**Unitranche / FLFO (first-out / last-out):**

- Single credit agreement; internal priority governed by Agreement Among Lenders (AAL)
- **First-out lenders** (typically revolving credit / senior portion): priority on interest,
  amortization, and prepayment distributions; lower margin
- **Last-out lenders** (typically term loan / subordinated portion): higher margin; residual
  on enforcement waterfall
- AAL voting provisions: typically require FLFO supermajority or unanimous consent for
  amendment of core economic terms affecting the waterfall

**Pari passu inter-creditor issues:**

- Multiple lenders holding pari passu first liens: pro rata sharing of proceeds required;
  exceptions for ABL / revolving vs. term loan collateral bifurcation
- **Split collateral structures**: ABL revolving lender has first priority on current asset
  collateral (accounts, inventory, deposit accounts); term loan lender has first priority
  on fixed assets (real property, equipment, IP)

**Common RED issues:**

- No intercreditor agreement when capital structure has multiple secured creditors —
  priority dispute defaults to insolvency law waterfall (which may not reflect deal intent)
- Standstill period too long (>180 days) — effectively prevents secured party from protecting
  collateral value; too short (<90 days) — insufficient restructuring time
- First lien / second lien collateral packages differ — assets in one but not the other
  create gaps in priority
- AAL waterfall ambiguous in a multi-dollar-draw scenario — disputed calculations in
  enforcement
- Lien release provision too broad in first/second lien ICA — first lien agent can release
  all collateral without second lien holder consent in scenarios beyond permitted asset sales

---

### Topic 15: UCC Article 9 Enforcement and Remedies

**What to assess:** Review enforcement provisions against UCC §§9-601–9-628 requirements.

**Default and remedies (§9-601):** On default, secured party has rights under:

- UCC Article 9 (§§9-601–9-628)
- The security agreement
- Any other applicable law

**Collection rights (§9-607):** Secured party may notify account debtors to pay directly
to secured party, take control of proceeds to which it is entitled (§9-315), and enforce
or realize on instruments, investment property, and chattel paper.

**Disposition of collateral (§9-610):** Secured party may sell, lease, license, or otherwise
dispose of collateral "after default." Every aspect of the disposition must be **commercially
reasonable** (§9-610(b)).

**Notification requirements (§9-611-9-614):**

- Before disposing of collateral, secured party must send an **authenticated notification**
  to the debtor and any secondary obligors (guarantors)
- For **consumer goods**: form notification requirements in §9-614
- For **non-consumer collateral**: notification must state:
  - Name and address of secured party
  - Description of collateral to be disposed of
  - Method of intended disposition (public or private sale)
  - Statement that debtor is entitled to redemption
  - Time and place of public disposition OR time after which private disposition will be made
- Notification must be sent within a **reasonable time** before disposition; safe harbor:
  **10 days** for non-consumer collateral (§9-612(b))
- Other secured parties: notification required to holders of security interests in the
  collateral that have filed UCC-1s within the last 5 years

**Commercial reasonableness (§9-627):**

- Price received is not determinative of commercial reasonableness
- Commercially unreasonable dispositions expose secured party to: (a) damages (§9-625),
  (b) loss of right to deficiency (§9-626 — consumer transactions: presumed inadequacy rule;
  non-consumer: rebuttable presumption rule in majority of states)
- Commercially reasonable factors: method of sale, time, place, terms, notification, advertising

**Redemption right (§9-623):** Debtor (and secondary obligors) may redeem collateral
before: (a) secured party collects under §9-607; (b) disposition; (c) acceptance in
satisfaction (§9-620). Redemption requires tendering full amount of secured obligation plus
reasonable expenses.

**Deficiency and surplus (§9-626):**

- If disposition proceeds exceed secured obligation: secured party must pay surplus to debtor
- If proceeds are less than secured obligation: secured party may seek deficiency judgment
  (except in consumer transactions — rebuttable presumption rule; and in certain states,
  anti-deficiency statutes may bar deficiency entirely)

**Secured party liability (§9-625):** Secured party that fails to comply with Article 9
(e.g., fails to give proper notification, conducts commercially unreasonable sale) is liable
for actual damages plus penalty of $500 (or credit of the amount, in consumer transactions).

**Common RED issues:**

- Security agreement purports to shorten Article 9 notice periods below the 10-day safe harbor
  (unenforceable against debtor)
- Secured party proposes "quick sale" at distress price without advertising — commercially
  unreasonable, exposes secured party to damages and potential deficiency forfeiture
- Deficiency claim pursued in California without first completing judicial foreclosure
  (one-action rule) — barred

---

### Topic 16: Secured Party Duties and Lender Liability

**What to assess:** Identify secured party obligations and potential lender liability exposure.

**Duty of care for collateral in possession (§9-207):**

- Secured party in possession must use **reasonable care** in the custody and preservation of
  collateral. Expenses of custody and preservation chargeable to debtor.
- Secured party may hold as additional security: insurance proceeds, money received from
  the collateral; reasonable proceeds from identifiable proceeds
- Secured party may create a security interest in the collateral (re-pledging permitted under
  §9-207(b)(3)) but this does not relieve the secured party's duty to return equivalent collateral

**Duty to send account statement (§9-210):**

- Secured party must respond to authenticated request from debtor for statement of account
  (balance of secured obligation) or list of collateral within **14 days**
- Failure to respond = $500 penalty + loss of right to enforce obligation to the extent of
  the incorrect statement

**Lender liability theories:**

- **Environmental**: CERCLA lender liability exemption (42 U.S.C. §9601(20)(E)-(F)) —
  lenders are exempt from CERCLA owner/operator liability if they did not participate in
  the management of the facility prior to foreclosure; foreclosure does not eliminate exemption
  unless lender continued to hold the property and participate in management post-foreclosure
  [VERIFY current EPA guidance]
- **Control person / equitable subordination**: A lender who exercises excessive control
  over a borrower's business may be equitably subordinated in bankruptcy (Taylor v. Standard
  Gas & Electric Co., "Deep Rock" doctrine) [VERIFY]
- **Lender interference with employment**: Lender directions to fire key employees may create
  employment-related claims against the lender
- **Duty of good faith in enforcement**: Courts have found implied duty of good faith in
  exercising discretionary enforcement rights under security agreements [JURISDICTION-SPECIFIC]

**Common RED issues:**

- Lender takes possession of inventory or equipment without proper Article 9 notification —
  breach of duty, potential damages liability
- Lender exercises operational control over borrower's business while holding a security
  interest — CERCLA and equitable subordination risk
- Lender conducts a "sell the collateral to affiliated party" disposition — commercially
  unreasonable and potentially a fraudulent conveyance

---

### Topic 17: Bankruptcy Interaction

**What to assess:** Analyze the security interest package against bankruptcy avoidance risk
and enforcement limitations.

**Automatic stay (§362):** Commencement of a bankruptcy case automatically stays enforcement
of security interests against property of the bankruptcy estate. Exceptions include
**qualified financial contracts** and arrangements covered by the FDIC safe harbor.

**Cash collateral (§363(c)):** Secured party's cash collateral (cash proceeds of collateral)
cannot be used by the debtor in possession without secured party consent or court order
providing adequate protection.

**Adequate protection (§361):** Secured party entitled to adequate protection of its interest
in collateral during bankruptcy. Forms: periodic cash payments, additional or replacement
liens, or an administrative expense claim.

**Strong-arm power (§544):** A trustee (or DIP) has the status of a hypothetical lien creditor
and bona fide purchaser for value as of the petition date — allows trustee to avoid unperfected
security interests (security interests not perfected before bankruptcy filing).

**Preference avoidance (§547):** A transfer of property (including perfection of a security
interest) made:

- To or for the benefit of a creditor
- For or on account of an antecedent debt
- Made while the debtor was insolvent
- Within **90 days** before the filing date (or **1 year** for insiders)
- That enables the creditor to receive more than in a chapter 7 liquidation

Perfection of a security interest within 90 days of bankruptcy can be avoided as a preference
**unless** it was made contemporaneously with the extension of credit (and within 30 days of
attachment — the "purchase money" exception in §547(c)(3)).

**Fraudulent transfer avoidance (§548):** A transfer made with actual intent to hinder/delay/
defraud creditors, or a constructively fraudulent transfer (transfer for less than reasonably
equivalent value while insolvent / undercapitalized), may be avoided. Look-back period: 2 years.
State law fraudulent transfer statutes (Uniform Fraudulent Transfer Act / Uniform Voidable
Transactions Act) typically extend look-back periods further — up to 4-6 years in some states.

**UK §245 Insolvency Act avoidance:**

- Floating charge created within 12 months (or 2 years for connected persons) before onset
  of insolvency is void unless new value (money, goods, services, reduction of existing debt)
  was provided at the time of or after creation of the charge
- A fixed charge is NOT subject to §245 avoidance

**Post-petition security interests (§552):**

- A security interest perfected before bankruptcy attaches to pre-petition collateral and the
  **proceeds** of such collateral post-petition
- A security interest does **NOT** attach to property acquired by the debtor post-petition
  (the "gap problem") under an after-acquired property clause, subject to certain exceptions
  for proceeds and "product or offspring" of pre-petition collateral

**Common CRITICAL issues:**

- Security interest perfected within 90 days of bankruptcy — preference risk; evaluate whether
  contemporaneous exchange exception applies
- Floating charge created within 12 months of UK administration without new value — §245 risk
- After-acquired property clause relied upon for post-petition collateral — §552 cuts off
  attachment post-petition

---

### Topic 18: EU and International Security Interests

**What to assess:** Identify applicable EU and international frameworks for cross-border security.

**EU Financial Collateral Directive (2002/47/EC) [VERIFY transposition status in each Member State]:**

- Applies to financial collateral arrangements (title transfer or pledge/charge) over financial
  collateral (cash, financial instruments, credit claims)
- Key protections: enforceability without court order; close-out netting; exemption from
  insolvency moratoriums; appropriation right
- Implemented differently across EU Member States — verify local transposition [JURISDICTION-SPECIFIC]

**German security structures [JURISDICTION-SPECIFIC]:**

- **Sicherungsübereignung**: Security transfer of ownership (not a charge or pledge) — debtor
  transfers title to secured party as security; debtor retains possession under a "loan for use"
  arrangement; used for moveable property including inventory and equipment
- **Pfandrecht**: Pledge over moveable property; requires transfer of possession (no filing
  system for non-possessory pledges in Germany — hence widespread use of Sicherungsübereignung)
- **Grundschuld**: Land charge (not a mortgage) — more commonly used than Hypothek in German
  real estate finance; can be freely transferred without the underlying debt

**French security structures [JURISDICTION-SPECIFIC]:**

- **Gage**: Pledge over moveable property; requires Act 2021 (gage des stocks) reform for
  inventory pledges without dispossession [VERIFY]
- **Nantissement**: Pledge over intangible assets (receivables, software, IP, securities)
- **Hypothèque**: Mortgage over real property; requires notarized deed and registration
- **Fiducie-sûreté**: Transfer of assets to a fiduciary as security (Civil Code Art. 2372-1);
  French law equivalent of security trust; relatively recent and still developing in practice

**UNCITRAL Model Law on Secured Transactions (2016):**

- Provides a model framework for non-possessory security interests in all types of moveable
  assets; adopted by several jurisdictions including New Zealand (PPSA) and some African states
- Key concepts: registration-based perfection, priority rules, enforcement

**Cape Town Convention:**

- International treaty on security interests in aircraft (Protocol) and rail equipment (Rail Protocol)
- Applies to aircraft engines, airframes, and helicopters; creates an international registry
  (CAPE TOWN REGISTRY) for security interests
- Provides strong international priority and enforcement rights

**Common YELLOW issues:**

- Cross-border security package uses English law concepts without adapting to local civil law —
  "all-asset floating charge" concept does not translate to most civil law systems
- German Sicherungsübereignung not used for equipment security in Germany — pledge requires
  dispossession (impractical for operating equipment)

---

## Severity Classification

Classify each finding using the four-tier system:

| Tier | Classification | Definition                                                                                                                                                              | Required Response                                                                                           |
| ---- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| ✅   | **GREEN**      | Security interest properly created, perfected, and prioritized. Standard or better position.                                                                            | Note for record; no action required                                                                         |
| ⚠️   | **YELLOW**     | Perfection or priority gap addressable without material loss of security; non-standard position that may be acceptable in context; monitoring required                  | Provide specific remediation steps; estimate cost of deferral                                               |
| 🔴   | **RED**        | Material perfection gap or priority defect; could result in unsecured or subordinate status if not remedied; likely enforceable issue in bankruptcy                     | Escalate; require pre-closing remediation or title/escrow holdback; cite legal basis for risk               |
| 🚨   | **CRITICAL**   | Systemic perfection failure; fundamental void or voidable risk under bankruptcy avoidance law; potential lender liability; requires immediate action regardless of cost | Stop; do not advance; require immediate remediation before any further credit advances; document adequately |

### Automatic CRITICAL triggers:

- UK charge not registered at Companies House within 21 days — void against administrator
- UCC-1 continuation missed — security interest lapsed and treated as never perfected against
  purchasers for value
- UK floating charge created within 12 months of insolvency without new value (§245)
- Security agreement not signed/authenticated by debtor — no attachment
- Deposit account listed in UCC-1 but no DACA executed — deposit accounts unperfected
  (filing alone insufficient for deposit accounts)
- Copyright security interest recorded only by UCC-1 without Copyright Office COVA recording —
  perfection failure for all registered copyright works [VERIFY on current circuit split]
- Preference period perfection of security interest within 90 days of bankruptcy petition
  without contemporaneous exchange

---

## Prioritization Framework

Classify all remediation items into three tiers for negotiation and closing management:

**Tier 1 — Must-Remedy Before Closing / Advance:**

- CRITICAL findings
- RED findings with active bankruptcy preference window exposure
- Expired UCC-1 filings
- Missing DACAs for primary operating accounts
- Missing Copyright Office recordings for core IP assets
- Missing UK Companies House registration

**Tier 2 — Remedy Within 30 Days Post-Closing:**

- RED findings that do not trigger immediate unsecured status but must be documented in closing
  conditions
- Fixture filings needed for material real property secured transactions
- Additional PMSI notices required for inventory lenders
- IP security documentation completeness (USPTO recordation best practices)

**Tier 3 — Monitor and Remediate on Annual Collateral Review:**

- YELLOW findings that are low probability or low impact
- UCC-1 continuation timing (monitoring required 6 months before 5-year expiry)
- Debtor name / jurisdiction monitoring for name changes and relocations
- Proceeds tracing and after-acquired property review for evolving asset bases
- Annual lien search refresh to identify new competing creditors

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before delivering.

| Gate           | Rule                                                                                                                                                                | Fail Action                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established principle                                                                                    | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow consistent, recognizable format for the jurisdiction (e.g., UCC §9-203; 17 U.S.C. §205; CA CCP §580d; [2005] UKHL 41)                          | Fix format                                               |
| **Currency**   | Every cited provision verified against current text — check for 2022 UCC amendments, recent Companies Act reforms, current insolvency caps                          | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the security agreement's governing law; no assumptions from other jurisdictions introduced without marking [JURISDICTION-SPECIFIC]            | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty stated explicitly, not hidden — circuit splits (IP preemption), state variations (anti-deficiency), and developing law (2022 digital assets) called out | Add confidence qualifier                                 |

---

## Self-Interrogation for RED and CRITICAL Items

For any finding classified RED or CRITICAL, apply this 3-pass review before finalizing classification:

**Pass 1 — Legal Chain Integrity:**

- Does the perfection gap follow logically from the cited statute?
- Would a bankruptcy court in this jurisdiction actually hold the security interest unperfected
  on these facts?
- Is there a cure mechanism (late filing, court order, etc.) that mitigates the risk?

**Pass 2 — Completeness:**

- Have all relevant perfection requirements been checked for this asset class?
- Are there alternative perfection methods not yet considered?
- Are there regulatory dimensions (FDIC rules, OCC guidance, state-specific requirements)?

**Pass 3 — Challenge:**

- What is the strongest argument that the security interest IS perfected despite this gap?
- Under what circumstances would a court uphold the security interest notwithstanding the defect?
- Is the RED/CRITICAL classification proportionate to actual risk, or is this actually YELLOW
  with appropriate monitoring?

_If any pass reveals a weakness, revise the analysis before delivery. Record outcome as
`self_interrogation: PASS` or `self_interrogation: REVISED` in the Glass Box audit trail._

---

## Confidence Scoring

| Level        | Range     | Meaning                                                  | Action                                                |
| ------------ | --------- | -------------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled UCC or statutory rule; clear case law            | State with full confidence                            |
| **High**     | 0.80–0.94 | Strong authority; minor variation possible               | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments; circuit splits or state variations exist | State with explicit reasoning and contra-indicators   |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing authorities               | Flag for counsel review; present both sides           |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative analysis                         | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Append this YAML block to every collateral review report:

```yaml
glass_box:
  skill_name: "legalcode-security-collateral-review"
  transaction: "[Transaction name and date]"
  reviewing_party: "[Secured party / borrower / neutral]"
  governing_law: "[Jurisdiction(s) identified from security documents]"
  debtor_jurisdiction_of_organization: "[State/country of organization for each debtor]"
  asset_classes_reviewed:
    - "[Asset class 1 — perfection method]"
    - "[Asset class 2 — perfection method]"
  topics_reviewed: "[N of 18 topics reviewed]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "[UCC §9-203 — VERIFIED/UNVERIFIED]"
    - "[17 U.S.C. §205 — VERIFIED/UNVERIFIED]"
    - "[CA 2006 s.859A — VERIFIED/UNVERIFIED]"
  case_law_consulted:
    - "[In re Peregrine Entertainment — VERIFIED/UNVERIFIED]"
    - "[Re Spectrum Plus [2005] UKHL 41 — VERIFIED/UNVERIFIED]"
    - "[Agnew v CIR [2001] UKPC 28 — VERIFIED/UNVERIFIED]"
  findings_summary:
    critical: "[number]"
    red: "[number]"
    yellow: "[number]"
    green: "[number]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED/CRITICAL items)"
  citations_verified: "[N VERIFIED] / [N UNVERIFIED]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "Security interest perfection analysis is highly technical and jurisdiction-specific"
    - "Lien search results not reviewed — conclusions limited to documents provided"
    - "Valuation of collateral not performed"
    - "[Any additional transaction-specific limitations]"
  reviewer: "AI-assisted — requires qualified banking and finance counsel review"
```

---

## Anti-Patterns

What NOT to do when reviewing or advising on security interests and collateral:

1. **Filing UCC-1 for deposit accounts and calling it perfected** — Filing a UCC-1 that lists
   deposit accounts does NOT perfect a security interest in those accounts. UCC §9-312(b)(1)
   is explicit: deposit accounts can only be perfected by control. A UCC-1 filing on deposit
   accounts provides zero perfection benefit and a false sense of security. Execute a DACA.

2. **Relying on UCC-1 alone for registered copyrights** — In re Peregrine Entertainment, Ltd.
   held that the Copyright Act preempts UCC Article 9 for registered copyright works. A secured
   party that files only a UCC-1 for a borrower with significant registered IP (software,
   content, media) may be unperfected in its most valuable collateral. Always file a COVA with
   the US Copyright Office for registered works. [VERIFY circuit applicability]

3. **Using trade names on the UCC-1** — Filing a UCC-1 using the borrower's trade name (DBA)
   rather than its exact registered legal name will be seriously misleading under UCC §9-506 and
   the filing will be ineffective. Always pull the current organic documents (certificate of
   incorporation, articles of organization) and use the exact legal name as filed.

4. **Missing the continuation filing** — UCC-1 financing statements lapse after 5 years (§9-515).
   The continuation must be filed in the **6-month window before** expiration. If missed even
   by one day, the security interest becomes unperfected and is treated as if it was never
   perfected against purchasers for value and lien creditors. A missed continuation in an
   LBO with a 7-year term loan is a systemic risk that must be actively monitored.

5. **Ignoring debtor relocation** — If a registered organization changes its state of
   organization (redomicile) or an individual moves to another state, the original UCC-1 remains
   effective for only 4 months. If the secured party does not re-perfect in the new state within
   that window, the security interest becomes unperfected. This frequently occurs in
   restructurings where entities are merged or redomiciled without updating lien perfection.

6. **Failing to file fixture filings for equipment bolted to the floor** — Manufacturing
   equipment, HVAC, elevators, and built-in IT infrastructure are frequently "fixtures" under
   applicable state law. A secured party who files only in the UCC central filing office (not
   in the real estate records as a fixture filing) may be subordinate to the first mortgage
   holder. In real estate-heavy transactions, always analyze the fixture question.

7. **Writing "all intellectual property" in the security agreement without identifying
   specific registered works** — A description of "all intellectual property" may be insufficient
   to create a security interest under §9-108's reasonable identification requirement for some
   courts. More importantly, Copyright Office recording requires identifying the specific works.
   The security agreement for an IP-rich company should schedule patents by number, trademarks
   by registration number, and registered copyrights by registration number.

8. **Providing 100% equity pledge of a CFC (controlled foreign corporation)** — Pledging 100%
   of the voting equity of a CFC can trigger a deemed dividend under U.S. tax law. The market
   standard is 65% voting / 100% non-voting. This is a frequently missed point in cross-border
   secured transactions with US borrowers having foreign subsidiaries.

9. **Treating a "fixed" charge as fixed just because the documents call it that** — Under
   English law (Re Spectrum Plus [2005] UKHL 41), a charge labeled "fixed" will be recharacterized
   as floating if the chargor is free to collect and use the proceeds. An administrator will
   promptly challenge "fixed" charges over receivables where proceeds flow into an unrestricted
   operating account. If the charge over receivables is to be fixed, ensure the proceeds account
   is genuinely blocked.

10. **Missing the 21-day UK registration window** — UK Companies Act 2006 s.859A requires
    registration of charges at Companies House within 21 days of creation. An unregistered charge
    is void against a liquidator, administrator, and creditors (s.859H) — not just subordinate,
    but void. In UK secured transactions, registration is typically done immediately upon
    execution. Any delay past 21 days requires a court application for extension.

11. **Relying on an intercreditor agreement without checking the collateral package** — The
    best intercreditor agreement is worthless if the underlying security interests are not
    validly created and perfected. Always review the security documents in conjunction with the
    intercreditor agreement. A silent second lien with no DACA over deposit accounts is not
    a second lien — it is no lien at all on those accounts.

12. **Ignoring the §245 UK floating charge avoidance window** — A floating charge granted to a
    new lender within 12 months of insolvency (2 years for connected parties) can be voided
    by an administrator unless new money was advanced. A lender who agrees to refinance an
    existing facility without a cash-out and takes new floating charges in the process is at
    risk if the borrower enters administration within 12 months. Ensure the consideration
    analysis is documented at the time of the transaction.

13. **Missing PMSI notice for inventory — forfeiting super-priority** — A purchase money
    secured party in inventory (ABL, equipment financier) has super-priority over prior blanket
    liens only if: (a) perfected when debtor receives possession, AND (b) written notice sent
    to prior secured parties before the debtor receives possession. Forgetting to send the
    notice (or sending it after delivery) permanently forfeits the super-priority for that
    inventory tranche — the PMSI creditor drops to ordinary UCC priority.

14. **Accepting a "springing DACA" without a clear trigger event definition** — A springing
    DACA that gives the lender control only on a "payment default" may not be adequate if the
    primary risk is a covenant default (e.g., leverage ratio breach). The trigger should be
    defined broadly to include any "event of default" under the credit agreement, not just
    payment defaults.

15. **Not accounting for the bank's senior lien/offset right in a DACA** — Banks typically
    retain the right to offset against deposit accounts for service fees, returned items, and
    bank charges. This right generally primes the secured party's DACA control right for those
    amounts. In a cash collateral analysis, the effective collateral value of a deposit account
    may be reduced by the bank's offset exposure.

16. **Perfecting within 90 days of a bankruptcy petition** — If a secured party perfects (or
    updates perfection) within 90 days of the borrower's bankruptcy filing, the perfection may
    be avoided as a preference under §547 — even if the underlying obligation was incurred much
    earlier. The preferred position of an otherwise unsecured (unperfected) creditor created by
    late perfection is exactly what §547 is designed to reverse.

17. **Failing to address proceeds of collateral in the security agreement** — A security
    agreement that covers "all inventory and equipment" but says nothing about proceeds means
    the secured party may lose the security interest when collateral is sold. Always include
    an explicit proceeds clause, and review whether proceeds tracking through deposit accounts
    and investment accounts is adequately covered by the DACA package.

18. **Using supergeneric descriptions in the security agreement** — "All assets" or "all personal
    property" is invalid as a security agreement collateral description under UCC §9-108(c)
    (supergeneric description insufficient in the security agreement, though valid in the UCC-1
    financing statement). This distinction is frequently confused. The security agreement must
    specifically identify or reasonably describe collateral; the UCC-1 can use supergeneric
    language.

19. **Not monitoring name changes and mergers** — When a debtor changes its legal name or
    merges into another entity, existing UCC-1 filings may become seriously misleading or may
    cover the wrong entity name. The 4-month window under §9-507 (name change) and §9-316
    (relocation) runs from the change event. In complex corporate restructurings, secured
    parties must map every entity name change and domicile change to existing UCC-1 filings
    and re-perfect within the applicable window.

20. **Neglecting to check whether upstream guaranty / security is "financial assistance"
    in UK** — Under Companies Act 2006 §§678-681, a UK private limited company may not give
    financial assistance (including providing security) for the acquisition of its own shares.
    Upstream guaranties and security from UK subsidiaries in leveraged buy-out financings must
    satisfy either the "whitewash" procedure (now repealed for private companies — financial
    assistance by private companies is generally now permitted under the Companies Act 2006 regime
    [VERIFY]) or demonstrate that the assistance is not for the purpose of acquiring shares.
    Failure to comply renders the financial assistance transaction void.

21. **Omitting cross-border perfection in multi-jurisdiction transactions** — In transactions
    with EU/non-US collateral, the secured party may file a UCC-1 in the US but neglect to
    perfect under applicable local law for assets in Germany, France, or the Netherlands. Each
    jurisdiction's law applies to assets located in that jurisdiction. In EU civil law countries,
    there is no UCC equivalent — perfection typically requires local pledge/charge mechanics.

22. **Ignoring CERCLA lender liability in environmental site collateral** — A secured party
    that takes possession and control of collateral that is an "owner or operator" of a facility
    with hazardous substances may incur CERCLA cleanup liability. The secured party exemption
    under CERCLA requires that the lender did not participate in management of the facility.
    Before enforcing against industrial or manufacturing collateral, assess environmental risk
    and the scope of the §9601(20)(E)-(F) exemption.

---

## Writing Standards

**For all collateral analysis output:**

- Use **active voice**: "The secured party has not filed a DACA" not "A DACA has not been filed"
- **Verb-first** where possible: "Execute a DACA with [bank] within [date]" not "It is necessary
  to execute a DACA"
- Be **specific, not vague**: name the account, the filing state, the specific copyright registration
  number, the precise statutory provision — never "the applicable rules" or "relevant law"
- **One issue per finding**: Do not merge multiple gaps into a single finding; each gap needs
  its own classification, citation, and remediation step
- **Short sentences**: each finding should lead with the gap, follow with the legal basis, then
  state the consequence if unaddressed
- Use **tables** for collateral inventory, priority stacks, and remediation plans — structured
  data is more useful than prose paragraphs for complex security packages
- Name every **actor and deadline**: "Borrower's counsel must file COVA with the US Copyright
  Office within 10 business days prior to closing" — not "copyright recording should be done"

**Quality gates before delivery:**

1. Can a banking associate understand every finding without a UCC treatise open?
2. Does each RED/CRITICAL finding include: (a) the specific gap, (b) the statutory basis,
   (c) the consequence if unaddressed, and (d) the specific remediation action?
3. Is every statutory citation formatted correctly (e.g., UCC §9-104(a)(2), not just "Article 9")?
4. Are jurisdiction-specific conclusions properly marked [JURISDICTION-SPECIFIC]?
5. Are all uncertain positions marked [VERIFY] rather than stated with false confidence?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 3, search for jurisdiction-specific UCC Article 9 enactment, state-specific
  amendments (particularly Alternative A vs. B for debtor names), and applicable case law
  on IP preemption and floating charge classification
- Search for current Companies House registration requirements and insolvency cap amounts
- Search for applicable anti-deficiency statutes in the state where real property collateral
  is located
- For intercreditor issues, search for relevant bankruptcy court decisions on standstill
  enforceability and lien release provisions
- Save verified results to `/tmp/legalcode-collateral-research.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with general knowledge and repository analysis
- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected — manual verification required"`
- Flag that perfection analysis requires verification of current state UCC enactment and
  any non-uniform state amendments before relying on conclusions

---

## Output Format Template

```markdown
## Collateral Adequacy Report

**Transaction**: [Name and date]
**Reviewing for**: [Secured party / borrower / neutral]
**Documents reviewed**: [List of security agreements, UCC filings, registrations, DACAs]
**Governing law**: [Jurisdiction(s)]
**Date of review**: [Date]
**Review basis**: [Full review / Priority review — [focus areas]]

---

## Executive Summary

**Overall collateral package assessment**: [ADEQUATE / CONDITIONAL / INADEQUATE]

| Severity    | Count | Key Issues       |
| ----------- | ----- | ---------------- |
| 🚨 CRITICAL | [N]   | [Top 1-2 issues] |
| 🔴 RED      | [N]   | [Top 1-2 issues] |
| ⚠️ YELLOW   | [N]   | [Summary]        |
| ✅ GREEN    | [N]   | —                |

**Recommended action before closing / next advance**: [Yes / No / Conditional]

---

## Collateral Inventory

| #   | Asset Class           | Description             | Required Perfection      | Perfection Used           | Status   |
| --- | --------------------- | ----------------------- | ------------------------ | ------------------------- | -------- |
| 1   | Accounts              | All receivables         | UCC-1 filing             | UCC-1 filed [date, state] | ✅ GREEN |
| 2   | Deposit accounts      | Account #xxxx at [Bank] | Control (DACA)           | DACA executed [date]      | ✅ GREEN |
| 3   | Registered copyrights | [Title/Reg. No.]        | UCC-1 + Copyright Office | UCC-1 only — no COVA      | 🔴 RED   |
| ... |                       |                         |                          |                           |          |

---

## Findings: [CRITICAL / RED / YELLOW] Items

### 🚨 CRITICAL-1: [Issue Name]

**Asset class**: [category]
**Gap**: [Description of the specific gap]
**Legal basis**: [Specific statute or case law]
**Consequence**: [What happens if unaddressed — unsecured, void, preference risk]
**Remediation**: [Specific action, owner, deadline]
**Confidence**: [Level + rationale]

### 🔴 RED-1: [Issue Name]

[Same structure]

### ⚠️ YELLOW-1: [Issue Name]

[Same structure]

---

## Priority Stack Analysis

| Collateral Type       | Secured Party | Filing / Control Date | Priority Position | Competing Interests               |
| --------------------- | ------------- | --------------------- | ----------------- | --------------------------------- |
| All assets (UCC)      | [Lender A]    | [Filing #, date]      | 1st               | None identified                   |
| Deposit accounts      | [Lender A]    | [DACA date]           | 1st (by control)  | Bank offset (§9-327)              |
| Registered copyrights | [Unperfected] | —                     | None              | Bankruptcy trustee super-priority |
| ...                   |               |                       |                   |                                   |

---

## Remediation Action Plan

### Tier 1 — Remedy Before Closing / Advance

| #   | Action                                                            | Owner                    | Deadline               | Legal Basis    |
| --- | ----------------------------------------------------------------- | ------------------------ | ---------------------- | -------------- |
| 1   | Execute COVA and record copyright security at US Copyright Office | Borrower's IP counsel    | 10 days before closing | 17 U.S.C. §205 |
| 2   | Execute DACA with [Bank] for account #xxxx                        | Borrower / Lender / Bank | At or before closing   | UCC §9-104     |
| ... |                                                                   |                          |                        |                |

### Tier 2 — Remedy Within 30 Days Post-Closing

| #   | Action                                                              | Owner            | Deadline             | Legal Basis   |
| --- | ------------------------------------------------------------------- | ---------------- | -------------------- | ------------- |
| 1   | File fixture filing in [County] real estate records for [equipment] | Lender's counsel | 30 days post-closing | UCC §9-502(b) |
| ... |                                                                     |                  |                      |               |

### Tier 3 — Monitor Ongoing

| #   | Action                                   | Frequency    | Trigger                                   | Legal Basis   |
| --- | ---------------------------------------- | ------------ | ----------------------------------------- | ------------- |
| 1   | UCC-1 continuation filing for [filing #] | 5-year cycle | File within 6 months before [expiry date] | UCC §9-515    |
| 2   | Lien search refresh                      | Annual       | Annual review                             | Best practice |
| ... |                                          |              |                                           |               |

---

## Localization Notes

[For each jurisdiction covered, note jurisdiction-specific requirements and markers]

- **[State/Country]**: [Specific requirement or restriction]

---

## Glass Box Audit Trail

[YAML block per template above]
```

---

## Localization Notes

| Topic                | US (UCC Article 9)                                                           | UK (English Law)                                           | EU (Civil Law Examples)                                                                                          |
| -------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Filing system**    | UCC central filing office in debtor's state of organization                  | Companies House registration (21-day window)               | No unified registry; varies by asset type and Member State                                                       |
| **Deposit accounts** | Control via DACA mandatory (§9-312(b))                                       | Financial collateral arrangements (FCARs 2003)             | EU FCD 2002/47/EC — Member State implementation varies                                                           |
| **Real property**    | Mortgage/deed of trust in county records                                     | Legal charge at HM Land Registry                           | Notarized deed + land registry in most civil law systems                                                         |
| **IP security**      | Copyright: Copyright Office + UCC-1; Patent/TM: UCC-1 only                   | IP Charge in debenture; registered at IP rights registry   | No unified EU IP security regime; national law applies                                                           |
| **Priority**         | First-to-file-or-perfect race rule (§9-322)                                  | First to register at Companies House (in general)          | Varies by Member State and asset class                                                                           |
| **Enforcement**      | UCC §9-610 commercially reasonable sale                                      | LPA 1925 mortgagee enforcement rights; FCARs appropriation | National law; EU FCD provides close-out netting protections                                                      |
| **Insolvency**       | §547 preference (90 days), §544 strong-arm                                   | §245 IA 1986 floating charge avoidance (12 months)         | EU Restructuring Directive 2019/1023; Member State variations                                                    |
| **Floating charges** | No direct equivalent; after-acquired property clause achieves similar result | UK floating charge — fixed/floating classification test    | Most civil law systems do not recognize floating charges — use Sicherungsübereignung (DE) or fiducie-sûreté (FR) |

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis from deep legal research pipeline using
web research on UCC Article 9 (2010 and 2022 amendments), UK Companies Act 2006 charge
registration, English fixed/floating charge law (Re Spectrum Plus [2005] UKHL 41; Agnew v CIR
[2001] UKPC 28), UK Financial Collateral Arrangements (No.2) Regulations 2003 SI 2003/3226,
US IP security perfection (In re Peregrine Entertainment, Ltd. 116 B.R. 194 (C.D. Cal. 1990)),
bankruptcy avoidance mechanics (11 U.S.C. §§362, 544, 547, 548, 552), and intercreditor
arrangement practice. Structural patterns adapted from `legalcode-contract-review` (gold standard),
`legalcode-loan-agreement-review` (security collateral overview in Clause 10), and
`legalcode-guaranty-agreement-review` (anti-deficiency and subrogation interactions).
Differentiated from legalcode-loan-agreement-review by focusing on security interest creation,
perfection mechanics, priority analysis, and enforcement as a standalone review topic rather
than as an element of loan agreement review. Banking-finance is a new skill category (first
skill in `skills/general/banking-finance/`).
