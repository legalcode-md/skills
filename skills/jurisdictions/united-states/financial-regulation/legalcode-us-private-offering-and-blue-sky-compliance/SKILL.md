---
name: legalcode-us-private-offering-and-blue-sky-compliance
description: Reviews US private securities offerings and resale transactions for Securities Act compliance
  — validates exemption selection (Reg D Rules 504/506(b)/506(c), Reg A/A+, Reg CF, Section 4(a)(2), Section
  4(a)(7), Rule 144/144A), audits accredited investor verification procedures, performs bad actor disqualification
  checks under Rule 506(d), analyzes general solicitation controls, reviews offering materials and investor
  disclosures, maps Blue Sky notice filing obligations across all states, applies the integration doctrine,
  identifies broker-dealer and finder touchpoints, and builds a post-closing compliance calendar. Use
  when structuring a new Reg D offering, advising on resale path for restricted securities, preparing
  Blue Sky filings, reviewing placement agent agreements, conducting a private placement compliance audit,
  evaluating bad actor status of offering participants, or assessing securities law exposure before an
  M&A transaction involving privately placed securities.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Reviews US private securities offerings and resale transactions for Securities Act compliance — validates exemption selection (Reg D Rules 504/506(b)/506(c), Reg A/A+, Reg CF, Section 4(a)(2), Section 4(a)(7), Rule 144/144A), audits accredited investor verification procedures, performs bad actor disqualification checks under Rule 506(d), analyzes general solicitation controls, reviews offering materials and investor disclosures, maps Blue Sky notice filing obligations across all states, applies the integration doctrine, identifies broker-dealer and finder touchpoints, and builds a post-closing compliance calendar. Use when structuring a new Reg D offering, advising on resale path for restricted securities, preparing Blue Sky filings, reviewing placement agent agreements, conducting a private placement compliance audit, evaluating bad actor status of offering participants, or assessing securities law exposure before an M&A transaction involving privately placed securities. US federal Securities Act of 1933 plus state Blue Sky laws. Companion to legalcode-us-sec-reporting-compliance for public companies.


# Legalcode US Private Offering & Blue Sky Compliance

> **Disclaimer**: This skill provides a framework for AI-assisted securities law compliance
> review. It does not constitute legal advice. All outputs must be reviewed by a qualified
> securities attorney before relying on them for structuring, filing, or compliance
> purposes. Securities laws change frequently and carry criminal penalties; verify all
> provisions against current SEC releases, EDGAR, and authoritative state securities
> division sources before acting. Statutory and regulatory references cited from memory
> carry hallucination risk — verify against SEC.gov, EDGAR, and state securities division
> websites before relying on them.

---

## Purpose and Scope

This skill audits US private securities offerings — from initial structuring through
post-closing compliance — against the Securities Act of 1933, Regulation D, and
applicable state Blue Sky laws.

**Covers:**

- Exemption selection and validation (Reg D 504/506(b)/506(c), Reg A/A+, Reg CF,
  Section 4(a)(2), Section 4(a)(7), Rule 144, Rule 144A)
- Accredited investor and QIB qualification and verification
- Bad actor disqualification checks (Rule 506(d)/506(e))
- General solicitation and advertising controls (Rule 502(c) vs. Rule 506(c))
- Offering materials: PPM sufficiency, Rule 502(b) disclosure requirements,
  subscription agreement review, investor questionnaire adequacy
- Blue Sky preemption analysis (NSMIA covered securities vs. merit review states)
- State notice filing map — all 50 states + DC + territories
- Integration doctrine analysis (amended Rule 152, safe harbors)
- Broker-dealer and finder compliance (Reg BI, FINRA Rule 5123,
  Section 15(a) registration analysis, M&A broker exemption)
- Post-closing compliance: Form D filing/amendment, legend compliance,
  resale restriction analysis, Form D annual updates

**Does not:**

- Provide legal advice or substitute for qualified securities counsel
- Cover Exchange Act registration or ongoing reporting for public companies
  (see legalcode-us-sec-reporting-compliance)
- Cover Regulation S offshore offerings (separate analysis required)
- Address Investment Advisers Act registration for fund managers
- Cover SEC enforcement defense strategy

---

## Jurisdiction and Governing Law

**United States federal securities law** (Securities Act of 1933, as amended;
17 C.F.R. Parts 230–239) **plus all state Blue Sky laws** for notice filing purposes.

Key federal authorities:

- **Securities Act of 1933** — 15 U.S.C. § 77a et seq. (the "Securities Act")
- **Regulation D** — 17 C.F.R. §§ 230.500–230.508 (Rules 501–508)
- **Regulation A** — 17 C.F.R. §§ 230.251–230.263 (Regulation A/A+)
- **Regulation Crowdfunding** — 17 C.F.R. §§ 227.100–227.503
- **Rule 144** — 17 C.F.R. § 230.144 (resale safe harbor)
- **Rule 144A** — 17 C.F.R. § 230.144A (QIB resale)
- **NSMIA** — National Securities Markets Improvement Act of 1996,
  15 U.S.C. § 77r (federal preemption of "covered securities")
- **SEC Release No. 33-10734** (2020) — Accredited investor definition amendments
- **SEC Release No. 33-10884** (2020) — Integration safe harbor reforms; amended Rule 152
- **Securities Act § 4(a)(2)** — Private placement exemption (statutory)
- **Securities Act § 4(a)(7)** — FAST Act 2015 resale exemption
- **Securities Act § 4(a)(6)** — Regulation Crowdfunding exemption

State law: Each state's Blue Sky statute governs notice filing obligations.
Key state authorities cited in this skill include the New York Martin Act
(NY General Business Law § 352 et seq.), California Corporate Securities Law
(Cal. Corp. Code § 25000 et seq.), Massachusetts Uniform Securities Act
(Mass. Gen. Laws ch. 110A), and the Uniform Securities Act (2002) (adopted
by most states). [VERIFY current state adoption status before relying on
state-specific provisions.]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming facts that would change the analysis, the workflow pauses and asks when:

- The exemption structure is ambiguous or multiple exemptions could apply
- The offering's investor mix (accredited vs. non-accredited) affects the analysis
- A covered person's triggering event history is unknown
- State Blue Sky obligations depend on where purchasers are located
- Integration with a prior or concurrent offering is possible
- A finder or placement agent's role triggers broker-dealer registration questions

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

Accept engagement materials in any of these formats:

- **File(s)**: Private Placement Memorandum (PPM), subscription agreement, investor
  questionnaire, Form D draft/filing, placement agent agreement, term sheet,
  offering circular, or other transaction documents
- **Pasted text**: Document text pasted directly into the conversation
- **Description**: Verbal description of the offering structure and key facts

If no materials are provided, prompt the user to supply them or proceed in
advisory/planning mode (the skill will ask questions to map the structure).

### Step 2: Gather Engagement Context

**⟁ CLARIFY** — Before beginning, gather key facts. Present as structured options:

1. **Engagement type**: What is the primary objective?
   - Options: **Structure a new offering** (select exemption, design compliance
     framework), **Audit an existing offering** (identify gaps in current structure),
     **Resale path analysis** (determine available resale exemptions for restricted
     securities), **Blue Sky filing map only** (generate state notice filing checklist),
     **Pre-M&A securities law diligence** (assess private placement exposure in
     target company), **Full offering compliance review** (all of the above)
   - _Why this matters_: Determines which workflow modules to activate.

2. **Issuer type**: What type of entity is the issuer?
   - Options: Operating company (startup/growth stage), Special purpose vehicle,
     Investment fund (venture / private equity / hedge), Real estate issuer,
     Development stage company with no revenue
   - _Why this matters_: Affects exemption eligibility, disclosure requirements,
     and Blue Sky filing obligations.

3. **Claimed exemption**: Which Securities Act exemption is the issuer relying on?
   - Options: Rule 506(b) (private placement, no general solicitation),
     Rule 506(c) (general solicitation, verified accredited only),
     Rule 504 (up to $10M), Regulation A+ Tier 1 (up to $20M),
     Regulation A+ Tier 2 (up to $75M), Regulation CF (up to $5M),
     Section 4(a)(2) (statutory private placement), Rule 144A (QIB resale),
     Section 4(a)(7) (FAST Act resale), Multiple / Not yet determined
   - _Why this matters_: Every downstream analysis depends on the exemption.

4. **Investor composition**: Who are the investors?
   - Options: All accredited investors only, Mix of accredited and
     non-accredited (up to 35 sophisticated non-accredited for 506(b)),
     QIBs only (144A), Retail investors included (Reg A/CF), Unknown
   - _Why this matters_: Determines verification obligations, disclosure
     requirements, and whether the exemption is facially available.

5. **General solicitation**: Has any general solicitation or advertising occurred?
   - Options: No — offering limited to pre-existing relationships,
     Yes — public advertising or social media used (requires 506(c) or Reg A/CF),
     Demo day / conference pitches occurred (need to assess),
     Website or online platform used, Uncertain
   - _Why this matters_: General solicitation disqualifies Rule 506(b) and
     Section 4(a)(2); it is permissible only under Rule 506(c), Reg A, and Reg CF.

6. **State geography**: In which states are purchasers located?
   - Options: Provide state list, All states (nationwide offering),
     Single state only, Unknown (I will provide full 50-state map)
   - _Why this matters_: Determines which states require Blue Sky notice filings.

7. **Placement agent involvement**: Is a broker-dealer or finder being used?
   - Options: No placement agent or finder, Registered broker-dealer,
     Unregistered finder (need to assess), Internal salesperson only
   - _Why this matters_: Triggers FINRA compliance requirements or broker-dealer
     registration analysis under Exchange Act § 15(a).

If the user provides partial context, proceed with reasonable assumptions and state
them explicitly. Do not silently assume.

### Step 3: Load Applicable Authorities

Use **legalcode-mcp** to build a working legal reference file for this review.

Search for current versions of:

- 17 C.F.R. §§ 230.500–230.508 (Regulation D rules and definitions)
- 17 C.F.R. § 230.144 and 230.144A (Rule 144 and 144A resale safe harbors)
- 17 C.F.R. §§ 230.251–230.263 (Regulation A)
- 17 C.F.R. §§ 227.100–227.503 (Regulation Crowdfunding)
- Form D instructions (17 C.F.R. § 239.500)
- SEC guidance on accredited investor verification under Rule 506(c)
- Any recent SEC releases amending Regulation D
- State Blue Sky filing requirements for purchaser states identified in Step 2

Save relevant results to `/tmp/legalcode-private-offering-authority.md`.

**If legalcode-mcp is not connected:**

- Mark all statutory and regulatory references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed using the Offering Analysis Reference sections below

### Step 4: Exemption Selection and Validation

Validate the claimed exemption against the offering facts gathered in Step 2.
Use the **Exemption Analysis Reference** below.

**⟁ CLARIFY** — If the claimed exemption appears facially unavailable or suboptimal,
present the issue and ask:

- "The facts suggest [general solicitation has occurred / non-accredited investors
  are included / offering amount exceeds the cap]. This may disqualify [Rule 506(b)
  / Rule 504]. Should I (a) proceed with the stated exemption and identify the gaps,
  or (b) identify the best available alternative exemption?"
- If multiple exemptions could work, present the trade-offs table from the
  Exemption Analysis Reference and ask which to proceed with.

For each requirement of the claimed exemption, assess: SATISFIED / AT RISK /
UNSATISFIED / UNKNOWN (requires additional facts).

### Step 5: Accredited Investor Verification Review

Evaluate whether the issuer has adequately verified (or reasonably believed) that
investors qualify as accredited under Rule 501(a) of Regulation D.

Distinguish the verification standard based on the exemption:

- **Rule 506(b)**: "Reasonable belief" standard — self-certification sufficient;
  no affirmative verification required
- **Rule 506(c)**: "Reasonable steps to verify" — affirmative verification required
  using methods in the rule or reasonable alternative methods

Use the **Accredited Investor Verification Reference** section below.

**⟁ CLARIFY** — If the exemption is Rule 506(c) and verification documents have
not been provided or procedures are undocumented, ask:

- "Rule 506(c) requires documented verification. Has the issuer (or a third party)
  verified each investor's accredited status using one of the permitted methods?
  If so, please provide the verification documentation or describe the procedure."

### Step 6: Bad Actor Disqualification Check

Screen all "covered persons" under Rule 506(d) for disqualifying events.
Use the **Bad Actor Disqualification Reference** section below.

**⟁ CLARIFY** — Present a checklist of covered persons to the user and ask:
"To complete the bad actor check, please confirm the identity of all the following
covered persons and whether any triggering events apply:
(a) The issuer and any predecessor or affiliated issuer
(b) Directors, executive officers, general partners, and managing members of the issuer
(c) 20%-or-more beneficial owners of the issuer's voting equity
(d) Any promoter connected to the issuer
(e) Investment managers and principals of the fund (if applicable)
(f) Persons paid remuneration in connection with this offering
(g) Any placement agent, broker, dealer, or finder involved
(h) Solicitors of purchasers"

Flag any confirmed or potential bad actor disqualification as CRITICAL DEFICIENCY.
Flag disclosure-only situations under Rule 506(e) as AT RISK.

### Step 7: General Solicitation Controls Review

Assess whether the offering's marketing and investor-outreach activities comply
with the applicable general solicitation rules.

For **Rule 506(b)** offerings:

- Identify any activity that could constitute general solicitation under Rule 502(c)
- Apply the pre-existing substantive relationship analysis
- Flag demo day, conference, website, or social media activity for assessment

For **Rule 506(c)** offerings:

- Confirm all investors are verified accredited
- Confirm Form D was amended to elect Rule 506(c) (or check initial Form D)
- Review advertising for material misstatements or anti-fraud issues

For **Reg A/CF** offerings:

- Confirm testing-the-waters compliance (where applicable)
- Confirm integration with concurrent 506(b) offering is assessed

Use the **General Solicitation Controls Reference** section below.

### Step 8: Offering Materials and Disclosure Review

Review the PPM, offering circular, subscription agreement, and investor
questionnaire for adequacy and accuracy.

**⟁ CLARIFY** — If no PPM or offering circular has been provided, ask:

- "Rule 506(b) requires disclosure of specified information to non-accredited
  investors (Rule 502(b)). Have any non-accredited investors received disclosure
  documents? If yes, please provide them. If the offering is to accredited
  investors only under Rule 506(b) or Rule 506(c), no specific disclosure format
  is mandated — but anti-fraud rules apply. Please confirm whether a PPM or
  other offering document has been prepared."

For Rule 502(b) compliance (non-accredited investors in 506(b)):

- Check disclosure of financial statements (audited if required by offering size)
- Verify risk factors, use of proceeds, dilution, management backgrounds
- Confirm "reasonable opportunity to ask questions" provided

For anti-fraud compliance (Rule 10b-5 / Securities Act § 17(a)):

- Review for material misstatements or omissions
- Flag overly optimistic projections without adequate risk disclosure
- Flag undisclosed conflicts of interest, compensation arrangements, or litigation

### Step 9: Blue Sky Notice Filing Compliance

Map Blue Sky obligations for each state where purchasers are located.

For **Rule 506 offerings** (covered securities under NSMIA, 15 U.S.C. § 77r(b)(4)(F)):

- State registration and qualification are federally preempted
- Most states still require notice filings (Form D + fee) within specified deadlines
- Identify any states with additional requirements beyond notice + fee

For **Rule 504 and Reg CF offerings** (not NSMIA-covered):

- Full state registration or exemption required in each purchaser state
- Merit review states may impose substantive requirements

Use the **Blue Sky State Filing Reference** section below.

**⟁ CLARIFY** — If purchaser state list is not confirmed, ask:
"To generate the complete Blue Sky filing calendar, please confirm the states where
securities were (or will be) sold. If this is a nationwide offering, I will provide
the full 50-state + DC map."

### Step 10: Integration Doctrine Analysis

Assess whether this offering integrates with any prior or concurrent securities
offerings under the amended Rule 152 integration framework.

**⟁ CLARIFY** — Ask:

- "Has the issuer conducted any other securities offerings in the past six months,
  or does the issuer plan to conduct a concurrent or subsequent offering under a
  different exemption? If yes, please describe the prior/concurrent offering
  (exemption relied on, timing, amount, investor type)."

Apply the Rule 152 integration analysis framework from the **Integration Doctrine
Reference** section below.

### Step 11: Broker-Dealer Touchpoints Review

Assess all persons receiving compensation in connection with the offering for
Exchange Act § 15(a) broker-dealer registration requirements.

**⟁ CLARIFY** — Ask:
"Is any person other than the issuer's officers and directors receiving compensation
(cash, securities, or other consideration) in connection with soliciting investors
or facilitating this offering? If yes, please describe their role and compensation."

Apply the broker-dealer and finder analysis from the **Broker-Dealer Touchpoints
Reference** section below.

### Step 12: Post-Closing Compliance Audit

After closing (or as part of pre-closing planning), generate the post-closing
compliance checklist:

1. **Form D filing** — 15-day deadline from first sale; 17 C.F.R. § 239.500
2. **State Form D notice filings** — per Blue Sky map from Step 9
3. **Securities legends** — verify restricted securities legend on all certificates
   and book entries
4. **Resale restrictions** — document holding period start dates for Rule 144
5. **No general solicitation certifications** — signed confirmations from investors
   (for 506(b) offerings)
6. **Ongoing reporting** — investor update obligations (if any)
7. **Form D amendments** — required within 15 days of material change
8. **Annual Form D updates** — required if offering continues past 12 months

Use the **Post-Closing Compliance Reference** section below.

### Step 13: Quality Verification

Before delivering output, run the Quality Assurance Framework:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every CRITICAL DEFICIENCY item, run the 3-pass Self-Interrogation.
3. Assign a Confidence Score to each material finding.
4. Verify all covered persons have been screened (Steps 6 and 11).
5. Verify all purchaser states have been mapped to Blue Sky obligations (Step 9).
6. Generate the Glass Box Audit Trail and append to the output.

### Step 14: Deliver Output

Structure the deliverable using the **Output Format Template** at the end of
this skill.

---

## Exemption Analysis Reference

### Regulation D Overview

| Exemption        | Max Offering       | Investor Limit                           | Accreditation          | General Solicitation      | NSMIA-Covered     | Form D Required |
| ---------------- | ------------------ | ---------------------------------------- | ---------------------- | ------------------------- | ----------------- | --------------- |
| **Rule 504**     | $10M / 12 months   | Unlimited                                | None required          | Prohibited (exceptions)   | No                | Yes             |
| **Rule 506(b)**  | Unlimited          | 35 non-accredited + unlimited accredited | Reasonable belief      | Prohibited                | Yes               | Yes             |
| **Rule 506(c)**  | Unlimited          | Unlimited                                | Must verify accredited | Permitted                 | Yes               | Yes             |
| **Reg A Tier 1** | $20M / 12 months   | Unlimited                                | None                   | Permitted                 | No (state review) | No (Form 1-A)   |
| **Reg A Tier 2** | $75M / 12 months   | Unlimited; limits for non-accredited     | None generally         | Permitted                 | Yes               | No (Form 1-A)   |
| **Reg CF**       | $5M / 12 months    | Individual limits                        | None                   | Permitted (via portal)    | No                | Form C          |
| **§ 4(a)(2)**    | No statutory limit | Sophisticated investors                  | Sophisticated standard | Prohibited                | No                | Voluntary       |
| **§ 4(a)(7)**    | No limit (resale)  | Qualified purchasers                     | Qualified purchaser    | Prohibited                | Yes (resale)      | No              |
| **Rule 144A**    | No limit (resale)  | QIBs only                                | QIB verification       | Permitted to QIBs         | Yes (resale)      | No              |
| **Rule 144**     | No limit (resale)  | Unlimited                                | None                   | Subject to manner-of-sale | Yes               | No              |

### Rule 504 — Key Requirements (17 C.F.R. § 230.504)

- Maximum aggregate offering price: $10,000,000 in any 12-month period (Rule 504(b)(2))
- Bad actor disqualification applies (Rule 506(d) incorporated by reference)
- General solicitation: prohibited unless proceeds used in registered offering or
  sold exclusively in states with registered/qualified offering procedures
- **Not NSMIA-covered** — state registration or exemption required in each state;
  no preemption for state registration requirements
- Common use cases: seed rounds in states with exemptions; intrastate offerings
- Integration with Rule 506 offerings possible — analyze carefully

### Rule 506(b) — Key Requirements (17 C.F.R. § 230.506(b))

**Conditions:**

1. No general solicitation or advertising (Rule 502(c)) — applies to any
   "communication that offers or sells securities to the general public"
2. Up to 35 "sophisticated" non-accredited investors; unlimited accredited investors
3. Non-accredited investor disclosure (Rule 502(b)): financial statements + specified
   information; if non-accredited investors participate, disclosure required
4. Reasonable belief as to accredited investor status (Rule 501(a)) — self-certification
   questionnaire sufficient; no affirmative verification required
5. Offering integration analysis under Rule 152 required
6. Bad actor disqualification (Rule 506(d)) applies

**Sophistication standard for non-accredited investors:**
Investors must have "such knowledge and experience in financial and business matters
that [they are] capable of evaluating the merits and risks of the prospective
investment" (Rule 506(b)(2)(ii)). This is a facts-and-circumstances analysis.

**Disclosure requirements for non-accredited investors (Rule 502(b)):**
| Offering Size | Financial Statement Requirement |
|--------------|--------------------------------|
| ≤ $2M | Balance sheet (120 days old; audited if available) |
| > $2M to $7.5M | Financial statements independently reviewed |
| > $7.5M | Financial statements audited by independent CPA |

### Rule 506(c) — Key Requirements (17 C.F.R. § 230.506(c))

**Conditions:**

1. All purchasers must be accredited investors (no non-accredited investors)
2. Issuer must take "reasonable steps to verify" accredited investor status
3. General solicitation and advertising permitted
4. Bad actor disqualification (Rule 506(d)) applies
5. Form D must be filed with Rule 506(c) box checked
6. Rule 502(b) disclosure not required, but anti-fraud rules apply

**Verification methods (Rule 506(c)(2)(ii)) — non-exclusive safe harbors:**

_Income-based verification:_

- Review IRS Form W-2, 1099, Schedule K-1, or 1040 for two most recent years
  plus written representation of expectation to reach same threshold in current year

_Net worth-based verification:_

- Review bank/brokerage/retirement account statements (< 3 months old) plus
  consumer credit report (< 3 months old) plus written liability certification

_Third-party verification letter:_

- Written confirmation from registered broker-dealer, SEC-registered IA,
  licensed attorney, or CPA that they have taken reasonable steps to verify
  and reasonably believe investor is accredited

_Existing investor verification:_

- Prior verification completed within 5 years plus investor certification of
  no material change in financial status (Rule 506(c)(2)(ii)(D))

**Reasonableness factors** (SEC guidance, Release No. 33-9415):

- Nature of purchaser and type of accredited investor category claimed
- Amount and type of information available
- Nature of offering (size, manner of conduct, relationship with purchaser)
- Higher offering amount / lack of relationship with investor → more rigorous verification

### Regulation A / A+ — Key Requirements

**Tier 1 (17 C.F.R. § 230.251 et seq.):**

- Maximum: $20M per 12-month period (up to $6M by selling securityholders)
- No individual investor investment limits
- Requires filing and qualification of Form 1-A with SEC
- **Not NSMIA-covered** — state qualification or exemption required
- Annual reporting not required after offering
- Testing the waters permitted (Rule 255)

**Tier 2:**

- Maximum: $75M per 12-month period (up to $22.5M by selling securityholders)
  (raised from $50M by SEC in March 2021)
- Non-accredited investors limited to greater of 10% of annual income or 10% of
  net worth per offering (Rule 251(d)(2)(i)(C)); no limits for accredited investors
  and exchange-listed securities
- Ongoing reporting required: annual (Form 1-K), semiannual (Form 1-SA),
  current reports (Form 1-U)
- **NSMIA-covered** — state registration preempted for Tier 2 offerings of
  equity, debt, and asset-backed securities listed on national exchange or
  sold to "qualified purchasers" [VERIFY state treatment]
- [VERIFY] States may still require notice filings for Tier 2 offerings

### Section 4(a)(2) — Statutory Private Placement Exemption

**Requirements (judicially developed; no specific rule):**

- Sales to persons who can "fend for themselves" — sophisticated investors
- No general solicitation or advertising
- Limited number of offerees (not a "public offering")
- Investment intent (restricted securities issued)
- Available information (investors can access same information as registered offering)
- Small number of offerees

**Practical guidance:**

- Section 4(a)(2) is the statutory basis; Rule 506(b) is the SEC safe harbor
- Issuers preferring the statutory route (no Form D filing required) must rely on
  facts-and-circumstances analysis — higher risk without the safe harbor
- Recommend Rule 506(b) reliance in almost all cases unless specific reason exists
  to avoid EDGAR Form D filing

### Section 4(a)(7) — FAST Act Resale Exemption

**Requirements (Securities Act § 4(a)(7), added 2015):**

1. Seller is not the issuer or an underwriter
2. Issuer has been in reporting status for 90+ days or Section 12 registered
3. Issuer is not a blank check, shell, or development stage company
4. No general solicitation
5. Each purchaser is an "accredited investor"
6. Seller and soliciting broker reasonably believe purchaser is accredited
7. Issuer either provides or makes available specified information
8. Seller provides the purchaser with notice of intent to rely on § 4(a)(7)

**Key advantage**: Preserves restricted security status; no integration with primary
offering. Permits resale of restricted securities to accredited investors without
Rule 144 holding periods.

### Rule 144 — Resale Safe Harbor (17 C.F.R. § 230.144)

**Conditions for non-affiliates:**
| Factor | Reporting Company | Non-Reporting Company |
|--------|------------------|-----------------------|
| Holding period | 6 months | 12 months |
| Current public information | Required during holding period | N/A after 12 months |
| Volume limits | None after 12-month mark | None after 12 months |
| Manner of sale | None | None |
| Broker confirmation | None | None |

**Conditions for affiliates (17 C.F.R. § 230.144(b)(1)):**

- 6-month holding period (reporting company) / 12 months (non-reporting)
- Current public information (Rule 144(c))
- Volume limits: greater of 1% of outstanding class OR average weekly trading
  volume during 4 weeks preceding sale
- Manner of sale: broker transactions or direct transactions with market makers
  or Form 144 for sales > 5,000 shares or > $50,000

**Shell company restriction**: Rule 144 is NOT available for resales of
securities issued by shell companies (including blank check companies) regardless
of holding period, except upon exit from shell status per Rule 144(i) [VERIFY].

### Rule 144A — QIB Resale (17 C.F.R. § 230.144A)

**Requirements:**

1. Securities offered only to "Qualified Institutional Buyers" (QIBs)
2. QIB definition (Rule 144A(a)(1)): institutional investors that in aggregate
   own and invest on a discretionary basis at least $100M in securities
   of issuers not affiliated with the QIB; for registered broker-dealers: $10M
3. Securities of same class not listed on US exchange
4. Seller and soliciting broker-dealer must reasonably believe purchaser is QIB
5. Purchaser acknowledges seller is relying on Rule 144A
6. Information right: non-reporting issuers must provide brief statement of
   business, financial statements for most recent 2 fiscal years (Rule 144A(d)(4))

---

## Accredited Investor Verification Reference

### Rule 501(a) Accredited Investor Categories (as amended 2020)

**Individual — financial thresholds:**
| Category | Threshold | Verification Approach |
|----------|-----------|----------------------|
| Income | > $200K individual or $300K joint, each of past 2 years + expectation for current year | W-2, 1099, Schedule K-1, tax returns (506(c)) or self-certification (506(b)) |
| Net worth | > $1M (individual or joint), excluding primary residence equity | Account statements + credit report (506(c)) or self-certification (506(b)) |

**Individual — professional credentials (2020 amendments, Rule 501(a)(10)):**
| Credential | Requirement |
|-----------|-------------|
| Series 7 (General Securities Representative) | FINRA licensed and in good standing |
| Series 65 (Investment Adviser Representative) | FINRA licensed and in good standing |
| Series 82 (Private Securities Offerings Representative) | FINRA licensed and in good standing |
| "Knowledgeable Employee" of exempt fund | As defined under Investment Company Act Rule 3c-5(a)(4) |

**Entity categories (selected):**

| Entity Type                          | Rule 501(a) Category  | Key Requirement                                                                          |
| ------------------------------------ | --------------------- | ---------------------------------------------------------------------------------------- |
| Bank, savings institution            | (1)                   | Registered under Exchange Act § 12 or subject to § 15(d)                                 |
| Registered broker-dealer             | (1)                   | FINRA-registered                                                                         |
| Registered investment company        | (1)                   | Investment Company Act registered                                                        |
| SEC-registered IA                    | (1)                   | Registered under IA Act                                                                  |
| Rural Business Investment Company    | (1)                   | Approved under Small Business Investment Act                                             |
| Business development company         | (2)                   | IA Act § 2(a)(48)                                                                        |
| Small Business Investment Company    | (2)                   | Licensed under SBIC Act § 301(c) or (d)                                                  |
| Private Business Development Company | (2)                   | IA Act § 202(a)(22)                                                                      |
| Certain tax-exempt orgs / nonprofits | (3)                   | Total assets > $5M; not formed for specific investment                                   |
| Any trust                            | (7)                   | Total assets > $5M; not formed for specific investment; directed by sophisticated person |
| Entity all accredited owners         | (8)                   | All equity owners individually accredited                                                |
| LLC or other entity                  | (3) with > $5M assets | Not formed to make specific investment (2020 amendment)                                  |
| "Family offices"                     | (12)                  | ≥ $5M AUM, not formed to make specific investment, directed by sophisticated person      |
| "Spousal equivalent"                 | (11)                  | Same income/net worth computation rights as spouse (2020 amendment)                      |

**⟁ CLARIFY** — For entities, confirm whether the entity meets its applicable
category, including asset thresholds and formation-purpose restriction.

### 506(c) Verification Procedures — Best Practices

For issuers using Rule 506(c):

1. **Document the verification method used for each investor** — maintain a
   verification file with the method, documents collected, and date verified
2. **Obtain verification before accepting the subscription** — verification
   should precede receipt of funds
3. **Use third-party verification services** where available (VerifyInvestor,
   Prime Trust, etc.) — third-party verification shifts risk
4. **Refresh verifications** — verification is "stale" after 5 years unless
   refreshed under Rule 506(c)(2)(ii)(D)
5. **Income method**: collect 2 years of tax documents + current-year
   representation; if using joint income, collect joint returns
6. **Net worth method**: bank/brokerage statements < 3 months old +
   credit report < 3 months old + written liability certification;
   exclude primary residence equity (Reg D Rule 501(a)(5) note)
7. **Attorney/CPA letter**: must be from licensed professional; confirm
   professional has actually reviewed underlying documents

---

## Bad Actor Disqualification Reference

### Covered Persons Under Rule 506(d)(1)

| Category                                  | Who Is Covered                                                                                                                                                                 |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| (i) Issuer                                | The issuer itself; any predecessor or affiliated issuer                                                                                                                        |
| (ii) Directors and officers               | Any director, executive officer, other officer participating in the offering, general partner, managing member                                                                 |
| (iii) 20% beneficial owners               | Any person who is a beneficial owner of 20% or more of the issuer's outstanding voting equity, calculated on the basis of voting power                                         |
| (iv) Promoters                            | Any promoter connected with the issuer in any capacity at the time of sale                                                                                                     |
| (v) Investment managers (funds)           | Investment managers of an investment fund issuer and their directors, executive officers, other officers participating in the offering, general partners, and managing members |
| (vi) Persons compensated for solicitation | Any person that has been or will be paid (directly or indirectly) remuneration for solicitation of purchasers in connection with the offering                                  |
| (vii) Solicitors' GPs/MMs                 | Any general partner, managing member, director, executive officer, or other officer participating in the offering of any such solicitor                                        |

**Key note on (iii)**: Beneficial ownership calculation uses voting power, not economic interest. If a person holds non-voting shares but has voting rights through contract, proxy, or convertible instruments, they may be a covered person. [VERIFY calculation method for each class of securities.]

### Triggering Disqualifying Events (Rule 506(d)(1)(i)–(viii))

A Regulation D offering is disqualified if any covered person has been subject to:

| Triggering Event                                                                                             | Look-Back Period                                   | Notes                                                   |
| ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- | ------------------------------------------------------- |
| Criminal convictions for securities fraud, false statements to SEC, mail/wire fraud, postal violations       | 10 years (5 years for others)                      | Measured from conviction date                           |
| Court injunctions or restraining orders in connection with purchase/sale of securities                       | 5 years                                            | Includes court orders; does not include pending actions |
| Final orders of state securities regulators, bank regulators, insurance regulators, federal banking agencies | 10 years (willful conduct) / 10 years (securities) | Bar or suspension triggers disqualification             |
| SEC disciplinary orders (§§ 15(b), 15B, 15C, 17A suspension/bar, censure)                                    | Final orders under these sections                  | Disciplinary orders by SEC                              |
| SEC cease-and-desist orders for Securities Act § 5 violations or scienter-based AML                          | Final C&D orders                                   |                                                         |
| Suspension or expulsion from FINRA or national securities exchange                                           | Current or within 5 years                          |                                                         |
| US Postal Service false representation orders                                                                | Current or within 5 years                          |                                                         |
| SEC stop orders and orders refusing qualification                                                            | Current orders; 5 years for others                 |                                                         |

### Rule 506(e) — Disclosure Exception (Not Disqualification)

If a triggering event occurred **before** September 23, 2013 (the rule's effective
date), the issuer is NOT disqualified but must **disclose** the event to each
purchaser "a reasonable time prior to sale" under Rule 506(e).

**Practice point**: Build Rule 506(e) disclosure into the subscription process when
pre-2013 events exist. Failure to disclose voids the exemption.

### Bad Actor Waiver Process

The SEC may waive a disqualification upon a showing of good cause (Rule 506(d)(2)(iii)).
Waivers are available but rarely granted quickly; apply well in advance of the offering.
[VERIFY current SEC waiver processing timeline.]

### Screen Expansion — Looking Behind Entities

Screen not just the entities but also their directors, executive officers, and
other participating officers. A disqualified individual within an entity can trigger
disqualification of the entity as a covered person.

---

## General Solicitation Controls Reference

### What Constitutes General Solicitation (Rule 502(c))

General solicitation includes (non-exhaustive list from SEC releases):

| Activity                                        | Generally Constitutes GS?   | Notes                                                                                                           |
| ----------------------------------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Advertisement in newspaper, magazine, or online | Yes                         | Rule 502(c) prohibition                                                                                         |
| Broadcast or social media advertisement         | Yes                         | Twitter/X, Facebook, LinkedIn ads                                                                               |
| Mass email to prospect list                     | Yes                         | Unless pre-existing relationship with each recipient                                                            |
| Website with open public access                 | Yes — if describes offering | Password-protected portals with pre-existing relationships may be acceptable                                    |
| Demo day pitch to general audience              | Generally yes               | SEC no-action letters have provided limited relief for accredited-investor-only demo days; analyze case by case |
| Conference pitch (SXSW, etc.)                   | Generally yes               | Public conferences with unknown attendees                                                                       |
| Pitch to known, pre-qualified investors         | Generally no                | If pre-existing substantive relationship                                                                        |
| Seminar for invited attendees                   | Depends                     | Invitation to general public = GS; invitation to pre-screened accredited investors = may not be GS              |
| Discussion in online forum                      | Depends                     | Public forum = GS; private accredited investor forum with pre-existing relationships = may not be               |
| Cold call to investor                           | Generally yes               | No pre-existing relationship                                                                                    |

### Pre-Existing Substantive Relationship Doctrine

The SEC has long held that a "pre-existing, substantive relationship" between the
issuer/placement agent and an investor can negate a finding of general solicitation
under Rule 506(b). However:

1. The relationship must be **pre-existing** — established before the offering commences
2. The relationship must be **substantive** — the issuer must have knowledge of
   the investor's financial circumstances or sophistication
3. The relationship **cannot be created** by registering with an investment platform
   immediately before offering shares

**Common risk**: Online platforms and broker-dealers sometimes argue that their
investor database constitutes pre-existing relationships. The SEC has cautioned
that a perfunctory questionnaire completed immediately before access to an
offering does not establish a substantive relationship. [VERIFY current SEC guidance.]

### Safe Harbor for Concurrent 506(c) Offerings

Under the amended Rule 152 integration framework (2020), an issuer may conduct
a concurrent Rule 506(c) offering (with general solicitation) alongside a
Rule 506(b) offering, provided the Rule 506(b) offering is made only to investors
with whom the issuer had a pre-existing substantive relationship before the
commencement of the Rule 506(c) general solicitation.

---

## Blue Sky State Filing Reference

### NSMIA Preemption Framework (15 U.S.C. § 77r)

**"Covered securities" under NSMIA** (preempted from state registration):

- Securities offered under Rule 506 (both 506(b) and 506(c)) — 15 U.S.C. § 77r(b)(4)(F)
- Securities offered under Rule 144A — 15 U.S.C. § 77r(b)(4)(A)
- Securities listed on NYSE, Nasdaq, AMEX — 15 U.S.C. § 77r(b)(1)
- Securities of registered investment companies — 15 U.S.C. § 77r(b)(1)(B)
- Regulation A Tier 2 offerings (limited preemption) [VERIFY state-specific treatment]

**NSMIA preemption does NOT prevent:**

- State notice filing requirements (most states require Form D + fee)
- State anti-fraud jurisdiction
- State enforcement of federal securities law violations
- State regulation of investment advisers (if threshold not met)

**Rule 504 and Regulation CF**: NOT NSMIA-covered securities; full state
registration or exemption analysis required.

### Form D Notice Filing — General Requirements

For Rule 506 offerings:

- File Form D electronically via EDGAR within **15 days of the first sale**
  of securities in the offering (17 C.F.R. § 239.500)
- File amendments to Form D within 15 days of any material change in the
  information provided, except year-end address changes
- File a "closing amendment" when an offering is completed or abandoned
- Annual amendment required if offering is ongoing after 12 months

**State notice filings**: Almost all states require a copy of the federal Form D
(or a state-specific form) plus a filing fee within a specified deadline from
the first sale in that state. Deadlines vary by state (most are 15 days from
first sale; some are longer).

### Selected State Blue Sky Requirements for Rule 506 Offerings

| State             | Form Required                    | Deadline                        | Fee                                                               | Additional Requirements                                                                          |
| ----------------- | -------------------------------- | ------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **California**    | Form D (EDGAR) + Blue Sky notice | 15 days from first CA sale      | $300 minimum + 1/20th of 1% of securities sold in CA (max $1,500) | —                                                                                                |
| **New York**      | Form 99 (Reg D Notice Filing)    | Within 15 days of first NY sale | $1,200 per offering                                               | Martin Act filing; NY attorney signed                                                            |
| **Texas**         | Form D (EDGAR copy) + TX Form D  | 15 days from first TX sale      | $500                                                              | —                                                                                                |
| **Florida**       | Form D (EDGAR copy)              | 15 days from first FL sale      | Varies by offering size                                           | —                                                                                                |
| **Massachusetts** | Form D (EDGAR)                   | 15 days from first MA sale      | $0                                                                | MA has engaged in merit-style review of Reg D offerings; aggressive enforcement posture [VERIFY] |
| **Illinois**      | Form D (EDGAR copy)              | 15 days from first IL sale      | $500                                                              | —                                                                                                |
| **Colorado**      | Form D + CO notice               | Within 15 days of first CO sale | $50                                                               | —                                                                                                |

> ⚠️ **[VERIFY ALL STATE FEES AND DEADLINES]** State Blue Sky requirements change
> frequently. Verify current fees, forms, and deadlines against each state's
> securities division website before filing. This table reflects general patterns
> as of the skill creation date; state law is dynamic.

**States with merit review authority** (not preempted by NSMIA for 506 notice
filings, but may scrutinize disclosures):

- Massachusetts (950 CMR 14.00) — known for aggressive oversight
- [VERIFY] States that retain anti-fraud review rights for notice filings

**States with additional requirements or registration requirements for non-NSMIA
offerings** (Rule 504, Reg CF):

- All states have their own registration or exemption requirements
- Conduct a state-by-state analysis for any offering not covered by NSMIA

### Generating the Blue Sky Filing Calendar

For each state where purchasers are (or will be) located:

```
State: _______________
First sale date in state: _______________
Notice filing deadline: _______________  (typically 15 days from first sale)
Form required: _______________
Filing fee: _______________
Additional requirements: _______________
Filing completed: ☐ / Date: _______________
```

---

## Integration Doctrine Reference

### Amended Rule 152 (effective 2020, SEC Release No. 33-10884)

The amended Rule 152 establishes integration safe harbors to replace the
pre-2020 five-factor test. Under the current framework:

**Statutory safe harbor** (Rule 152(a)): Offers and sales made more than
**30 calendar days** before the start of a Regulation D offering, or more than
30 calendar days after the termination or completion of a Regulation D offering,
will not be integrated with that Regulation D offering.

**Concurrent offering safe harbors** (Rule 152(b)): Certain concurrent offerings
are never integrated with Regulation D offerings, including:

- Registered offerings
- Regulation A offerings
- Regulation CF offerings (provided no general solicitation for the Reg D offering
  is made to Reg CF investors)
- Rule 701 offerings (employee benefit plans)
- Offshore offerings under Regulation S

**Practical application — the 30-day look-back:**

1. Identify all securities offerings completed in the 30 days before this offering
2. Identify all offerings planned to commence within 30 days after this offering
3. Assess whether any such offering used or will use a different exemption that
   could be integrated
4. Note: offerings more than 30 days apart are presumptively not integrated

**Legacy five-factor test** (still relevant for pre-2020 offerings and where
safe harbors don't apply):

1. Whether the offerings are part of a single plan of financing
2. Whether the offerings involve issuance of the same class of securities
3. Whether the offerings are made at approximately the same time
4. Whether the same type of consideration is received
5. Whether the offerings are made for the same general purpose

**Critical integration scenarios:**

- Concurrent Rule 506(b) and Rule 506(c) offerings → See General Solicitation
  Controls Reference above
- Reg D offering followed immediately by Reg A offering → 30-day rule applies
- Back-to-back Reg D rounds with different exemptions → Analyze under Rule 152

---

## Broker-Dealer Touchpoints Reference

### Exchange Act § 15(a) — Registration Requirement

Any person "engaged in the business of effecting transactions in securities for
the account of others" (Exchange Act § 3(a)(4)) must register as a broker-dealer
under Exchange Act § 15(a) unless an exemption applies.

**Compensation-based analysis** — the SEC generally applies a multi-factor test:

- Receiving transaction-based compensation (commission, finder's fee,
  percentage of proceeds) is the strongest indicator of broker-dealer activity
- Regularly participating in securities transactions (not just one or two)
- Soliciting investors (actively seeking purchasers)
- Handling customer funds or securities

**Risk factor**: An unregistered finder who receives transaction-based compensation
and actively solicits investors in a private placement likely requires broker-dealer
registration — regardless of how their role is characterized. SEC and FINRA have
pursued enforcement actions against unregistered finders.

### M&A Broker Exemption (Exchange Act § 3(h), effective 2023)

The Consolidated Appropriations Act of 2023 codified a statutory M&A broker
exemption permitting unregistered persons to facilitate securities transactions
in connection with the transfer of ownership of "privately held companies" meeting
specified criteria:

- Does not apply to: offerings to general public, transactions where issuer is
  a blank check company, transactions involving publicly traded securities
- M&A brokers may not handle funds or securities, extend credit, or bind parties
- [VERIFY current SEC guidance on scope of § 3(h) exemption]

**Practice point**: The M&A broker exemption covers business acquisition/sale
transactions, not straight capital-raising by issuers. For capital-raising, no
general unregistered finder exemption exists at the federal level.

### Regulation Best Interest (Reg BI) — 17 C.F.R. § 240.15l-1

When a registered broker-dealer is involved:

- Reg BI requires the broker-dealer to act in the "best interest" of retail customers
  when making a recommendation
- Applies to retail customers (natural persons); does not apply to institutional investors
- Requires: disclosure (Form CRS), care obligation, conflict of interest obligation,
  and compliance obligation
- [VERIFY] Placement agents in Reg D offerings to accredited natural persons must
  consider whether Reg BI applies

### FINRA Rule 5123 — Private Placement of Securities

FINRA-member broker-dealers participating in private placements must:

- File a copy of any PPM or other offering document (or notice if no document) with
  FINRA within 15 calendar days of the first sale in the offering
- FINRA Rule 5123(b)(1) exemption: certain offerings (to institutional investors,
  QIBs, bank affiliates, investment companies, etc.) are exempt from filing requirement

### Placement Agent Agreement Review

When a placement agent agreement is provided, check for:

- [ ] FINRA registration confirmation
- [ ] Clear scope of engagement (solicitation vs. advisory only)
- [ ] Compensation structure (tail provisions, expenses)
- [ ] Representations and warranties regarding FINRA compliance and Reg BI
- [ ] Bad actor representations from placement agent and its covered persons
- [ ] Rule 10b-5 anti-fraud representations
- [ ] Indemnification for securities law violations
- [ ] Governing law and dispute resolution

---

## Post-Closing Compliance Reference

### Form D Filing Calendar

| Action                                | Timing                                                                | Authority                     |
| ------------------------------------- | --------------------------------------------------------------------- | ----------------------------- |
| Initial Form D (federal EDGAR)        | Within 15 days of first sale                                          | 17 C.F.R. § 239.500; Rule 503 |
| State notice filings                  | Per state deadlines (typically 15 days from first sale in that state) | State Blue Sky laws           |
| Amendment for material change         | Within 15 days of change                                              | Rule 503(a)(3)                |
| Amendment for new offering amount     | Within 15 days of change                                              | Rule 503(a)(3)                |
| Annual amendment (ongoing offering)   | Annually while offering continues                                     | Rule 503(a)(4)                |
| Closing amendment (offering complete) | Within 30 days of completion                                          | Best practice                 |

### Restricted Securities Legends

All restricted securities must bear a legend substantially as follows:

> THE SECURITIES REPRESENTED BY THIS [CERTIFICATE/NOTICE OF ISSUANCE]
> HAVE NOT BEEN REGISTERED UNDER THE SECURITIES ACT OF 1933, AS AMENDED
> (THE "SECURITIES ACT"), OR APPLICABLE STATE SECURITIES LAWS. THE
> SECURITIES HAVE BEEN ACQUIRED FOR INVESTMENT PURPOSES ONLY AND MAY NOT
> BE SOLD, TRANSFERRED, OR OTHERWISE DISPOSED OF WITHOUT REGISTRATION
> UNDER THE SECURITIES ACT AND APPLICABLE STATE SECURITIES LAWS, OR AN
> EXEMPTION THEREFROM.

Verify legends appear on:

- Stock certificates (if certificated) or in the issuer's transfer records (if book-entry)
- Subscription agreements
- Operating/shareholder agreements

### Rule 144 Holding Period Tracker

| Investor Type                         | Holding Period                   | Start Date           | Earliest Rule 144 Sale Date |
| ------------------------------------- | -------------------------------- | -------------------- | --------------------------- |
| Non-affiliate (reporting company)     | 6 months                         | Date of full payment | [calculate]                 |
| Non-affiliate (non-reporting company) | 12 months                        | Date of full payment | [calculate]                 |
| Affiliate (reporting company)         | 6 months + volume/manner limits  | Date of full payment | [calculate]                 |
| Affiliate (non-reporting company)     | 12 months + volume/manner limits | Date of full payment | [calculate]                 |

**Tacking note**: Rule 144(d)(3) permits tacking of holding periods in certain
circumstances (conversions, exchanges, reclassifications). [VERIFY tacking
eligibility for convertible instruments.]

---

## Severity Classification

Classify each finding using this four-tier system:

### CRITICAL DEFICIENCY — Offering May Be Void; Immediate Action Required

The offering lacks a valid exemption or is structurally defective in a way that
exposes the issuer to rescission liability, criminal referral, or SEC enforcement.

**Automatic CRITICAL DEFICIENCY triggers:**

- Bad actor disqualification of a covered person (Rule 506(d)) with no waiver
- General solicitation in a Rule 506(b) offering (securities sold to investors
  contacted through general solicitation)
- Sale to non-accredited investors in a Rule 506(c) offering
- Offering amount exceeds Rule 504 cap ($10M) with no alternate exemption
- Form D not filed and statute of limitations has not run (no safe harbor for
  late filing; state law violations possible)
- Material misstatement or omission in PPM (Securities Act § 17(a) / Rule 10b-5 exposure)
- Unregistered broker-dealer receiving transaction-based compensation

**Action**: Immediately escalate to securities counsel. Do not complete additional
closings until resolved. Assess rescission obligation to existing investors.
Assess SEC voluntary self-reporting.

### NON-COMPLIANT — Material Deficiency Requiring Remediation

The offering has a documented compliance failure that does not necessarily void
the exemption but creates significant legal risk.

**Examples:**

- 506(c) verification procedures inadequate or undocumented
- Rule 502(b) disclosure not provided to non-accredited investors in 506(b) offering
- Form D filed late (after 15-day deadline) — exemption not automatically lost but
  SEC and state enforcement risk elevated
- Blue Sky notice filings not made in all purchaser states
- Securities issued without restricted legend

**Action**: Remediate before next closing. Document corrective steps taken.
Assess whether voluntary disclosure to SEC or states is appropriate.

### AT RISK — Gap That Creates Enforcement Exposure Without Full Remediation

The offering has a procedural gap or ambiguity that, while not yet a confirmed
violation, creates material risk if challenged.

**Examples:**

- Rule 506(e) pre-2013 events identified but not yet disclosed to investors
- Pre-existing substantive relationship documentation inadequate for 506(b) defense
- Integration analysis not completed; potential for integration with prior offering
- Placement agent agreement missing Reg BI compliance representations
- Accredited investor questionnaires outdated (> 5 years old for 506(c) verification)
- FINRA Rule 5123 filing not completed by placement agent

**Action**: Remediate within 30 days. Document analysis and remediation steps.

### COMPLIANT — No Material Issues Identified

The offering satisfies the applicable exemption requirements and compliance
procedures are in place.

**Action**: Note for completeness. Maintain documentation. Schedule post-closing
compliance calendar items.

---

## Actionable Output per Finding

For each finding, provide:

```
Finding: [Short title]
Severity: [CRITICAL DEFICIENCY / NON-COMPLIANT / AT RISK / COMPLIANT]
Confidence: [Definite / High / Probable / Possible / Unlikely] — [X.XX]
Rule / Authority: [Specific citation]
Description: [What the issue is and why it matters]
Impact: [Practical consequence if unaddressed: rescission, enforcement, loss of exemption]
Remediation: [Specific steps to fix, with sequence and timing]
Timeline: [Immediate / Within 15 days / Within 30 days / Before next closing / Ongoing]
Escalation: [Who needs to be involved: securities counsel, board, placement agent, etc.]
```

---

## Prioritization Framework

### Tier 1 — Must-Resolve Before Next Closing (Deal-Blockers)

Issues that, if unresolved, render the offering unlawful or expose the issuer
to rescission liability and criminal enforcement:

- Any bad actor disqualification without waiver
- Any confirmed general solicitation in a Rule 506(b) offering
- Any non-accredited investor in a Rule 506(c) offering
- Offering amount exceeding applicable cap with no alternative exemption
- Material misstatement or omission in offering materials
- Unregistered broker-dealer receiving transaction-based compensation

**Rule**: Do not close additional investors until Tier 1 issues are resolved.
Seek securities counsel involvement before proceeding.

### Tier 2 — Must-Remediate Within 30 Days (Material Gaps)

Issues that create significant legal risk but do not necessarily void the
offering if promptly remediated:

- Inadequate 506(c) verification procedures (remediate before next closing)
- Late Form D filing — federal and state (file immediately)
- Missing Rule 502(b) disclosure to non-accredited investors in 506(b)
- Rule 506(e) disclosure not provided to investors re: pre-2013 triggering events
- Blue Sky notice filings not made (file immediately)
- Securities issued without restricted legend

**Rule**: Prioritize above other legal matters. Document remediation steps.

### Tier 3 — Address in Ordinary Course (Best Practice Gaps)

Issues that reflect best practice deficiencies but carry lower immediate risk:

- Investor questionnaires approaching 5-year staleness for 506(c) purposes
- Missing FINRA Rule 5123 filing by placement agent
- Placement agent agreement lacking Reg BI compliance representations
- Form D closing amendment not filed after offering completion
- Incomplete Rule 144 holding period tracker documentation
- Missing annual Form D update for ongoing offering

**Rule**: Address through standard diligence and document requests.
Include in post-closing compliance calendar.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise any failures
before delivery.

| Gate           | Rule                                                                                                                                                          | Fail Action                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every securities law claim cites a specific rule, statute section, or SEC release                                                                             | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow consistent format: Rule 506(c) = "17 C.F.R. § 230.506(c)"; statutes = "Securities Act § 4(a)(2)"                                         | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments — SEC regularly amends Regulation D, Rule 144, Regulation A                                                      | Flag "[CHECK CURRENCY — rule may have been amended]"     |
| **Domain**     | Analysis stays within federal securities law scope; state law findings properly attributed to state sources                                                   | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated; "general solicitation" determinations are facts-and-circumstances; do not state definitively what the SEC has only guidance on | Add confidence qualifier                                 |

### Self-Interrogation for CRITICAL DEFICIENCY Items

For any finding classified as CRITICAL DEFICIENCY, apply this 3-pass review
before delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the bad actor disqualification / GS determination / exemption failure
  follow logically from the applicable rule text?
- Has the correct version of the rule been applied (pre- vs. post-2020 amendments)?
- Would the SEC or a court actually reach this conclusion on these specific facts?
- Is there a contrary SEC no-action letter or guidance that should be considered?

**Pass 2 — Completeness**:

- Has every element of the claimed exemption been checked?
- Have all covered persons been screened (not just the issuer)?
- Have all purchaser states been identified for Blue Sky purposes?
- Has the integration doctrine been fully applied to all prior and concurrent offerings?

**Pass 3 — Challenge**:

- What is the strongest argument that the offering IS exempt despite this finding?
- Under what circumstances might qualified securities counsel take a different view?
- Is the CRITICAL DEFICIENCY classification proportionate, or is this actually
  NON-COMPLIANT with a clear remediation path?

If any pass reveals a weakness, revise before delivery. Mark audit trail with
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

Assign a confidence level to each material finding:

| Level        | Range     | Meaning                                                   | Action                                                           |
| ------------ | --------- | --------------------------------------------------------- | ---------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled rule text; no interpretive ambiguity              | State with confidence                                            |
| **High**     | 0.80–0.94 | Strong authority; minor facts-and-circumstances questions | State with brief caveat                                          |
| **Probable** | 0.60–0.79 | Good arguments; reasonable minds could differ             | State reasoning and contra-indicators explicitly                 |
| **Possible** | 0.40–0.59 | Genuinely uncertain; depends on facts not yet available   | Flag for counsel review; present both sides                      |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative under available facts             | Do not assert; flag "[UNCERTAIN — securities counsel to advise]" |

**Securities-specific note**: "General solicitation" and "substantive relationship"
determinations are inherently facts-and-circumstances; confidence rarely exceeds
Probable (0.60–0.79) without complete marketing history. Mark accordingly.

---

## Glass Box Audit Trail

Every output MUST include this audit section:

```yaml
glass_box:
  skill_name: "legalcode-us-private-offering-and-blue-sky-compliance"
  engagement_type: "[Structure new offering / Audit existing offering / Resale path analysis / Blue Sky map / Pre-M&A diligence / Full review]"
  claimed_exemption: "[Rule 506(b) / Rule 506(c) / Rule 504 / Reg A Tier 1/2 / Reg CF / Section 4(a)(2) / Section 4(a)(7) / Rule 144 / Rule 144A]"
  issuer_type: "[Operating company / Fund / SPV / Real estate / Other]"
  investor_composition: "[All accredited / Mix accredited+non-accredited / QIBs only / Retail / Unknown]"
  general_solicitation_used: "[Yes / No / Uncertain — [detail]]"
  purchaser_states: "[List of states or 'All states (nationwide)' or 'Unknown']"
  bad_actor_screening: "[Completed / Partial / Not completed — [reason]]"
  covered_persons_screened: "[Number screened]"
  blue_sky_states_mapped: "[Number mapped]"
  integration_doctrine_applied: "[Yes / No — [reason]]"
  broker_dealer_analysis: "[Completed / Not applicable — no placement agent]"
  form_d_status: "[Filed [date] / Not yet filed / Late / Not required]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "[Rule 506(b) — 17 C.F.R. § 230.506(b) — VERIFIED / UNVERIFIED]"
    - "[Rule 501(a) — 17 C.F.R. § 230.501(a) — VERIFIED / UNVERIFIED]"
  findings_summary:
    critical_deficiency: "[number]"
    non_compliant: "[number]"
    at_risk: "[number]"
    compliant: "[number]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL DEFICIENCY items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations — e.g., bad actor screening limited to persons identified; additional persons may exist]"
    - "[Blue Sky analysis limited to states confirmed by user; unconfirmed states not mapped]"
    - "[State fees and deadlines require independent verification against current state law]"
  reviewer: "AI-assisted — requires qualified securities attorney review before relying on for any offering decision"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in private offering compliance review:

1. **Treating Rule 506(b) verification as equivalent to Rule 506(c) verification** —
   Rule 506(b) requires only "reasonable belief" (self-certification); Rule 506(c)
   requires affirmative "reasonable steps to verify." Applying the 506(b) standard
   to a 506(c) offering is a compliance failure. Never conflate the two.

2. **Checking the issuer only for bad actor disqualification** — Rule 506(d) covers
   seven categories of persons, most of whom are not the issuer itself. Officers,
   20%-owners, promoters, and persons paid for solicitation must all be screened.
   A disqualified placement agent or promoter voids the exemption even if the
   issuer itself is clean.

3. **Assuming NSMIA preemption eliminates all state obligations** — NSMIA preempts
   state registration for covered securities, not state notice filing requirements.
   Every Rule 506 offering in every purchaser state still requires a Form D notice
   filing (plus fee) in most states. "We're doing a 506 offering" does not mean
   Blue Sky is complete.

4. **Filing Form D "when convenient"** — The 15-day filing deadline is firm. Late
   filing does not automatically void the exemption but creates SEC and state
   enforcement exposure, and several states (including New York and Massachusetts)
   treat late filing seriously. Build a Form D filing calendar before the first sale.

5. **Treating general solicitation as a binary yes/no** — General solicitation is
   a facts-and-circumstances determination. Demo day pitches, conference presentations,
   and online postings that reach the general public may constitute general solicitation
   even if the issuer "only talked to accredited investors." Assess the audience and
   medium, not just the stated intent.

6. **Ignoring pre-2013 triggering events under Rule 506(e)** — Issuers sometimes
   conduct bad actor screens for disqualifying events but fail to identify pre-2013
   events requiring disclosure under Rule 506(e). The two analyses are distinct:
   post-2013 events disqualify; pre-2013 events require disclosure. Missing the
   disclosure obligation voids the exemption.

7. **Allowing integration to happen by default** — Issuers often conduct a 506(b)
   offering and then immediately begin a 506(c) offering without an integration
   analysis. Under the amended Rule 152, the 30-day safe harbor provides protection
   only if offerings are actually separated by 30 days. Back-to-back offerings without
   a gap require a careful integration analysis.

8. **Using "finder" as a magic word to avoid broker-dealer registration** — No
   general unregistered finder exemption exists at the federal level. An unregistered
   person who receives transaction-based compensation for soliciting investors in a
   securities offering is almost certainly acting as an unregistered broker-dealer.
   The title "finder" does not change the analysis.

9. **Skipping Rule 502(b) disclosure for non-accredited investors in 506(b)** —
   If even one non-accredited investor participates in a Rule 506(b) offering, the
   issuer must provide the Rule 502(b) prescribed disclosure, including financial
   statements at the specified audit/review level. Issuers frequently omit this
   because they "didn't expect any non-accredited investors."

10. **Forgetting to update Form D for material changes** — Form D is not a one-time
    filing. Material changes in offering amount, use of proceeds, or total offering
    amount require an amendment within 15 days. Many issuers file the initial Form D
    and never amend even as the offering grows substantially.

11. **Treating 506(c) as a simple "general solicitation permitted" switch** — Converting
    to Rule 506(c) from Rule 506(b) mid-offering without properly structuring the
    transition is a common error. The issuer must file an amended Form D electing
    506(c), ensure all prior investors were accredited and verified under 506(c) standards,
    and assess whether the pre-solicitation period constitutes an integrated 506(b) offering.

12. **Issuing securities without a restricted legend** — Securities issued in exempt
    offerings are "restricted securities" and must bear the appropriate legend. Failure
    to legend is not just a paperwork issue — it can affect the validity of transfer
    restrictions and complicate resale analysis under Rule 144.

13. **Confusing 144A resale with Rule 144 resale** — Rule 144A is a resale safe harbor
    for resales to QIBs only; it does not create freely tradeable securities. Rule 144
    provides a public resale safe harbor subject to holding periods and other conditions.
    The resale path analysis must identify which safe harbor applies to each class of
    security and each investor type.

14. **Omitting accredited investor representations from subscription agreements** —
    The subscription agreement must include investor representations (accredited status,
    investment purpose, access to information, ability to bear risk). Missing these
    representations weakens the issuer's reasonable belief defense for 506(b)
    purposes and its documentation defense for 506(c) purposes.

15. **Assuming Regulation A preempts state registration in all circumstances** —
    Regulation A Tier 1 offerings are NOT NSMIA-covered; state registration or
    qualification is required in each offering state. Tier 2 offers limited federal
    preemption for certain securities, but state notice filing requirements remain.
    Do not treat Regulation A as a fully federal offering equivalent.

16. **Skipping the annual Form D update for ongoing offerings** — If an offering
    remains open after 12 months (common in real estate or fund offerings), an annual
    amendment to Form D is required. Failure to file the annual amendment is a
    violation of Rule 503 and can affect the issuer's ability to use the exemption
    for the ongoing offering period.

17. **Structuring "testing the waters" incorrectly for Reg A** — Regulation A
    permits testing the waters (solicitation of interest before filing) under specific
    conditions. Issuers who engage in testing-the-waters activity before properly
    complying with Rule 255 (filing of solicitation materials, required legends) risk
    disqualifying the Reg A exemption.

18. **Overlooking state-specific aggressive postures** — Massachusetts and New York
    are known for assertive Blue Sky enforcement. Massachusetts 950 CMR 14.00 provides
    the Massachusetts Securities Division with substantive review authority over Reg D
    offerings, and the Division has taken enforcement action against issuers who
    failed to comply with notice requirements. Texas, California, and New Jersey also
    have active enforcement programs. Do not treat state Blue Sky as a rubber stamp.

---

## Writing Standards

Apply plain-language discipline to all output:

**For compliance findings** (shared with business team and counsel):

- State the finding directly: "The Form D was not filed within the 15-day deadline."
  Not: "There may be a possible issue with timing of certain filings."
- Name the actor: "The issuer must file..." not "A filing should be made..."
- Cite the specific rule: "Rule 503(a)(1) requires..." not "the rules require..."
- Quantify the impact: "Late filing creates enforcement risk; New York treats late
  filing as a separate violation of the Martin Act" — not "this could be problematic"
- Specify the remediation concretely: "File Form D via EDGAR at sec.gov/cgi-bin/browse-edgar
  immediately; file state Form D notices in all purchaser states within 48 hours"

**For uncertainty**:

- Use confidence qualifiers explicitly: "The general solicitation determination
  is fact-specific (Probable confidence, 0.65). The SEC has not provided bright-line
  guidance on conference pitches; the analysis turns on audience composition and
  whether investors had pre-existing relationships."
- Never state as settled law what is only guidance or inference

**Quality gates before delivery**:

1. Can the issuer's business team understand each finding without securities law training?
2. Can securities counsel immediately identify what remediation steps are required?
3. Is every finding backed by a specific rule citation (or flagged [VERIFY])?
4. Have all required actor screens (bad actors, broker-dealers) been completed?
5. Has the Blue Sky map been generated for all confirmed purchaser states?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 3, search for current text of all Regulation D rules, Rule 144, Rule 144A,
  and Regulation A
- Save results to `/tmp/legalcode-private-offering-authority.md`
- Search for any recent SEC releases amending the applicable rules (post-2020)
- Search for applicable state Blue Sky statutes for each purchaser state
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and regulatory citations with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Include prominent notice that rule citations require independent verification
  against the current Code of Federal Regulations (ecfr.gov) and SEC.gov
- Focus analysis on structural and procedural compliance gaps rather than legal
  authority depth; flag substantive legal questions for securities counsel

---

## Output Format Template

```markdown
## Private Offering & Blue Sky Compliance Analysis

**Issuer**: [Issuer name]
**Offering**: [Description of offering — security type, amount, purpose]
**Claimed Exemption**: [Rule 506(b) / 506(c) / Rule 504 / Reg A / Reg CF / other]
**Engagement Type**: [Audit / Structuring advice / Resale path / Blue Sky map / M&A diligence]
**Purchaser States**: [List or "Nationwide"]
**Date of Analysis**: [YYYY-MM-DD]

---

## Executive Summary

[2–4 sentences: overall compliance status, number of critical deficiencies,
most urgent actions required, recommended next steps]

---

## Summary Dashboard

| Category                         | Status                                                      | Finding Count |
| -------------------------------- | ----------------------------------------------------------- | ------------- |
| Exemption Validity               | [COMPLIANT / AT RISK / NON-COMPLIANT / CRITICAL DEFICIENCY] | [n]           |
| Accredited Investor Verification | [status]                                                    | [n]           |
| Bad Actor Disqualification       | [status]                                                    | [n]           |
| General Solicitation Controls    | [status]                                                    | [n]           |
| Offering Materials & Disclosure  | [status]                                                    | [n]           |
| Blue Sky Notice Filings          | [status]                                                    | [n]           |
| Integration Doctrine             | [status]                                                    | [n]           |
| Broker-Dealer Compliance         | [status]                                                    | [n]           |
| Post-Closing Compliance          | [status]                                                    | [n]           |

---

## Critical Deficiencies (Immediate Action Required)

[If none: "No CRITICAL DEFICIENCY findings identified."]

### [CD-1] [Short title]

**Severity**: CRITICAL DEFICIENCY
**Rule**: [Citation]
**Confidence**: [Level — score]
**Description**: [What the issue is]
**Impact**: [Consequence if unresolved]
**Remediation**: [Specific steps]
**Timeline**: Immediate

[Repeat for each CRITICAL DEFICIENCY]

---

## Non-Compliant Findings (Remediate Within 30 Days)

### [NC-1] [Short title]

**Severity**: NON-COMPLIANT
**Rule**: [Citation]
**Confidence**: [Level — score]
**Description**: [What the issue is]
**Impact**: [Consequence if unresolved]
**Remediation**: [Specific steps]
**Timeline**: [Within 15 days / Within 30 days / Before next closing]

[Repeat for each NON-COMPLIANT finding]

---

## At-Risk Findings (Address in 30 Days)

[Abbreviated format: Finding | Rule | Description | Remediation]

---

## Blue Sky Filing Calendar

| State   | First Sale Date | Filing Deadline | Form                  | Fee   | Status    |
| ------- | --------------- | --------------- | --------------------- | ----- | --------- |
| [State] | [date]          | [deadline]      | Form D + state notice | [fee] | ☐ Pending |
| ...     |                 |                 |                       |       |           |

---

## Post-Closing Compliance Calendar

| Action                                                             | Deadline                         | Authority          | Status |
| ------------------------------------------------------------------ | -------------------------------- | ------------------ | ------ |
| File Form D (EDGAR)                                                | [date — 15 days from first sale] | Rule 503           | ☐      |
| File state notice filings                                          | [per state]                      | State Blue Sky     | ☐      |
| Restricted legends on all securities                               | Before issuance                  | Rule 144           | ☐      |
| Annual Form D update (if ongoing)                                  | [12 months from first sale]      | Rule 503(a)(4)     | ☐      |
| Rule 144 holding period expiry (non-affiliates, reporting co.)     | [date — 6 months from payment]   | Rule 144(d)(1)(i)  | ☐      |
| Rule 144 holding period expiry (non-affiliates, non-reporting co.) | [date — 12 months from payment]  | Rule 144(d)(1)(ii) | ☐      |

---

## Tier Prioritization Summary

**Tier 1 (Must-Resolve Before Next Closing)**:
[List of CRITICAL DEFICIENCY items]

**Tier 2 (Must-Remediate Within 30 Days)**:
[List of NON-COMPLIANT items]

**Tier 3 (Address in Ordinary Course)**:
[List of AT RISK items]

---

## Recommended Next Steps

1. [Specific action — owner — deadline]
2. [...]

---

[Glass Box Audit Trail — YAML as per template above]
```

---

## Localization Notes

This skill covers **US federal law (Securities Act of 1933 + Regulation D)** and
**all US state Blue Sky laws**. It does not cover:

- **Offshore offerings**: Regulation S (17 C.F.R. §§ 230.901–230.905) governs
  offshore transactions; this skill does not address Regulation S compliance
- **Investment Company Act**: Fund managers must separately analyze Investment
  Company Act § 3(c)(1) and § 3(c)(7) exclusions; this skill covers the issuer
  securities law analysis only
- **Investment Advisers Act**: Registration analysis for fund managers investing
  in private offerings is not covered
- **ERISA**: Benefit plan investor considerations (25% limitation on "plan assets")
  are outside this skill's scope

For non-US offerings or dual-listed securities, consult jurisdiction-specific
counsel and consider legalcode-eu-prospectus-regulation, legalcode-eu-securities
compliance, or applicable jurisdiction-specific skills.

---

## Provenance

Created by Legalcode (2026-03-22). Legalcode original synthesis. Research
sources: US Securities Act of 1933; 17 C.F.R. Parts 230–239 (Regulation D,
Rules 144, 144A, Regulation A, Regulation Crowdfunding); SEC Release No. 33-10734
(2020 accredited investor amendments); SEC Release No. 33-10884 (2020 integration
safe harbor reforms / Rule 152); NSMIA 15 U.S.C. § 77r; Exchange Act § 3(h)
M&A broker exemption (2023); FINRA Rules 5123, Reg BI (17 C.F.R. § 240.15l-1);
state Blue Sky statutes and securities division guidance. Designed as the
US-specific operational complement to legalcode-us-sec-reporting-compliance.
Structural quality frameworks adapted from legalcode-contract-review (reference
standard) and legalcode-us-section-409a-valuation-review (US federal compliance
pattern). All legal citations marked [VERIFY] require independent verification
against current authoritative sources.
