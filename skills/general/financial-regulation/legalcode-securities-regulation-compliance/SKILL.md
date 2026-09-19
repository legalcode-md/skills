---
name: legalcode-securities-regulation-compliance
description: Analyze securities offering compliance covering US exemptions (Reg D Rule 506(b) / 506(c),
  Regulation A+ Tier 1/Tier 2, Regulation CF crowdfunding, Regulation S offshore transactions, Rule 144/144A
  resale, Rule 504), EU Prospectus Regulation (Reg 2017/1129, €8M/€12M thresholds, passporting, SME Growth
  Market), and UK FCA prospectus regime including January 2026 FSMA 2023 / PS24/2 Public Offer Platform
  reform. Use when structuring a private placement, selecting a securities exemption, conducting a compliance
  audit of an existing offering, preparing offering documents, advising on resale restrictions for restricted
  or control securities, or assessing cross-border offering compliance across US, EU, and UK.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Analyze securities offering compliance covering US exemptions (Reg D Rule 506(b) / 506(c), Regulation A+ Tier 1/Tier 2, Regulation CF crowdfunding, Regulation S offshore transactions, Rule 144/144A resale, Rule 504), EU Prospectus Regulation (Reg 2017/1129, €8M/€12M thresholds, passporting, SME Growth Market), and UK FCA prospectus regime including January 2026 FSMA 2023 / PS24/2 Public Offer Platform reform. Covers exemption selection logic, accredited investor qualification and verification, bad actor disqualification (Rule 506(d)/(e)), Form D / Form 1-A / Form C filing requirements, integration doctrine and 30-day safe harbor, Blue Sky laws and NSMIA preemption, EDGAR filing mechanics, directed selling efforts prohibitions, distribution compliance periods, and anti-fraud compliance (Section 10(b) / Rule 10b-5 / Section 17(a)). Use when structuring a private placement, selecting a securities exemption, conducting a compliance audit of an existing offering, preparing offering documents, advising on resale restrictions for restricted or control securities, or assessing cross-border offering compliance across US, EU, and UK. Produces COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY classifications per requirement, remediation action plans with deadline-anchored timelines, and exemption selection matrices. Jurisdiction- anchored to US (federal and Blue Sky), EU, and UK with [JURISDICTION-SPECIFIC] markers.


# Legalcode Securities Regulation Compliance

> **Disclaimer**: This skill provides a framework for AI-assisted securities regulation
> compliance analysis. It does not constitute legal advice, does not create an
> attorney-client relationship, and is not a substitute for qualified securities counsel
> licensed in the relevant jurisdictions. Securities regulation is highly technical,
> jurisdiction-specific, and subject to rapid change; all outputs must be reviewed by
> a licensed securities attorney before any reliance in connection with an actual offering
> or transaction. Statutory and regulatory citations are drawn from training-data knowledge
> and carry hallucination risk — verify every citation against authoritative sources
> (SEC.gov, EUR-Lex, FCA Handbook, state securities administrator websites) before
> relying on them. Nothing in this skill constitutes an offer or solicitation of any
> security.

---

## Purpose and Scope

This skill analyses securities offering compliance across the United States, European
Union, and United Kingdom. It maps a proposed or existing offering against the applicable
exemption framework, identifies compliance gaps, and produces a prioritized remediation
plan with actionable filing, documentation, and investor qualification requirements.

**Covers:**

- US private offering exemptions: Reg D Rules 504, 506(b), 506(c); Regulation A+ (Tier 1
  and Tier 2); Regulation CF; Regulation S; Rule 144/144A resale exemptions
- Integration doctrine: Safe harbor analysis under the revised 17 C.F.R. § 230.152 (2020)
- Investor qualification: Accredited investor definition (Rule 501), verification
  requirements, sophistication standards
- Bad actor disqualification: Rule 506(d) look-back, Rule 506(e) disclosure obligations
- Form D, Form 1-A, and Form C filing obligations (EDGAR)
- Blue Sky law compliance: NSMIA preemption, "covered securities," notice filing states
- EU Prospectus Regulation (Reg 2017/1129): €8M / €12M thresholds, qualified investor
  exemption, passporting, SME Growth Market regime
- UK prospectus regime: Current retained EU law + FSMA 2023 / FCA PS24/2 January 2026
  reforms, Public Offer Platform (POP) regime
- Cross-border offering structuring: Reg S / Reg D concurrent offerings
- Anti-fraud provisions: Section 10(b), Rule 10b-5, Section 17(a) of the Securities Act
- Ongoing reporting and legend requirements for restricted and control securities

**Operates in three modes:**

- **Structure**: Select the optimal exemption(s) for a proposed offering and map
  requirements before launch
- **Audit**: Assess an existing offering for compliance gaps and remediation needs
- **Resale**: Analyse resale restrictions on restricted or control securities and
  advise on Rule 144 / Rule 144A availability

**Does not:**

- Constitute legal advice or replace qualified securities counsel
- Cover registered public offerings (Form S-1, S-3, F-1, etc.) — this skill focuses
  exclusively on exempt and resale transactions
- Apply to investment company regulation under the Investment Company Act of 1940
  (beyond noting 3(c)(1) / 3(c)(7) interaction with Reg D)
- Cover exchange-traded derivatives, commodities futures, or CFTC-regulated instruments

---

## Jurisdiction and Governing Law

This skill covers three primary regulatory frameworks:

**United States (Federal):** Securities Act of 1933 (15 U.S.C. § 77a et seq.); Securities
Exchange Act of 1934 (15 U.S.C. § 78a et seq.); Dodd-Frank Wall Street Reform Act 2010;
JOBS Act of 2012; Regulation D (17 C.F.R. §§ 230.500–230.508); Regulation A
(17 C.F.R. §§ 230.251–230.263); Regulation CF (17 C.F.R. §§ 227.100–227.503);
Regulation S (17 C.F.R. §§ 230.901–230.905); Rule 144 (17 C.F.R. § 230.144);
Rule 144A (17 C.F.R. § 230.144A); Integration doctrine (17 C.F.R. § 230.152, amended 2020).

**United States (State — Blue Sky):** Each state has its own securities statute.
[JURISDICTION-SPECIFIC: Identify the states where offering proceeds will be raised and
check whether the securities are "covered securities" under NSMIA (15 U.S.C. § 77r)
or require state notice filings, registration, or exemption filings.]

**European Union:** EU Prospectus Regulation (Reg 2017/1129, as amended); Market Abuse
Regulation (Reg 596/2014); MiFID II (Dir 2014/65/EU); EU Crowdfunding Regulation
(Reg 2020/1503); ESMA guidelines on prospectus disclosure.

**United Kingdom (Post-Brexit):** FSMA 2000, Part VI (official listing) and s.85
(prohibition on offering without prospectus); Financial Services Act 2012; UK Prospectus
Regulation (retained EU law, currently applying); FSMA 2023 (prospectus reform, POP
regime); FCA Policy Statement PS24/2 (January 2026 prospectus reform implementation);
FCA Prospectus Regulation Rules (PRR) Sourcebook.

[JURISDICTION-SPECIFIC: For non-US/EU/UK jurisdictions, this skill identifies common
principles (registration/exemption requirement, anti-fraud rules, resale restrictions)
but does not analyse local law. Engage local counsel for any jurisdiction outside the
three covered frameworks.]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
offering structure, the workflow pauses and asks when:

- The answer would change the applicable exemption framework
- Multiple valid exemptions exist with materially different compliance requirements
- Investor eligibility is ambiguous or borderline
- Cross-border elements create overlapping regulatory obligations

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

### Step 1: Accept the Offering Description

Accept the offering description in any of these formats:

- **Offering memo or term sheet**: PPM, term sheet, or investment summary document
- **Offering description**: Free-text description of the issuer, amount, security type,
  and investor profile
- **Compliance audit request**: Existing offering materials for gap analysis

If no description is provided, prompt the user to supply one before proceeding.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning analysis, ask these structured questions. Skip any
already answered by the user's input:

1. **Mode**: What is the primary objective?
   - Options: (A) Structure a new offering — select the best exemption and map requirements,
     (B) Audit an existing offering — identify compliance gaps and remediation actions,
     (C) Resale analysis — advise on Rule 144 / Rule 144A / other resale exemptions
   - _Why this matters_: Determines whether the workflow focuses on exemption selection,
     gap identification, or resale restriction analysis.

2. **Jurisdictions**: Where will securities be offered / sold?
   - Options: US only (federal), US + Blue Sky (specify states), EU only (specify member
     states), UK only, US + EU, US + UK, US + EU + UK, Other (specify)
   - _Why this matters_: Determines which exemption frameworks apply and whether
     concurrent offering structuring is needed.

3. **Issuer type**: What is the issuer?
   - Options: US domestic issuer (reporting company), US domestic issuer (non-reporting),
     Foreign private issuer, Special purpose vehicle, Investment fund
   - _Why this matters_: Affects Reg S availability (Category 1/2/3), Reg A+ eligibility,
     and EU/UK prospectus threshold applicability.

4. **Security type**: What type of security is being offered?
   - Options: Equity (common/preferred stock, LLC interests), Debt (notes, bonds,
     debentures), Convertible instruments (SAFEs, convertible notes), Warrants/options,
     Tokens/digital assets, Other
   - _Why this matters_: Some exemptions are restricted to equity or debt; digital assets
     require separate analysis under the Howey test.

5. **Offering amount**: What is the total amount to be raised (per 12-month period)?
   - Options: Under $10M, $10M–$20M, $20M–$75M, Over $75M
   - _Why this matters_: Determines Reg A+ Tier eligibility and Reg CF annual limits;
     larger offerings may require full Reg D or registered offering.

6. **Investor base**: Who are the expected investors?
   - Options: All accredited investors only, Mix of accredited and up to 35 non-accredited
     sophisticated investors, Retail investors (non-accredited), Institutional / QIBs only,
     Non-US persons only
   - _Why this matters_: The single most important factor in exemption selection —
     non-accredited investors dramatically limit available exemptions.

7. **General solicitation**: Does the issuer intend to publicly advertise the offering?
   - Options: Yes — general solicitation intended (public website, social media, cold
     outreach), No — private pre-existing relationships only, Unsure
   - _Why this matters_: General solicitation is prohibited under 506(b) and 504 but
     permitted under 506(c) (with enhanced verification) and Reg A+/CF.

If partial context is provided, proceed with stated assumptions and label them explicitly.

### Step 3: Load Legal Authority

Use **legalcode-mcp** (if connected) to search for:

- Current text of applicable SEC rules (Reg D, Reg A+, Reg CF, Reg S, Rule 144)
- Recent SEC no-action letters and releases relevant to the offering type
- State securities law notice filing requirements for identified states
- Current EU Prospectus Regulation requirements and ESMA guidelines
- FCA PS24/2 implementation status and effective date for UK reform

Save results to `/tmp/legalcode-securities-research.md`.

**If legalcode-mcp is not connected:**

- Proceed using this skill's embedded legal framework
- Mark every statutory and regulatory reference with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`

### Step 4: Exemption Selection (Structure Mode) or Gap Assessment (Audit Mode)

**Structure Mode → Step 4A:** Apply the Exemption Selection Matrix (below) to identify
available exemptions and recommend the optimal path.

**Audit Mode → Step 4B:** Map the existing offering against the identified exemption's
requirements using the Compliance Requirement Checklist (below).

**Resale Mode → Step 4C:** Apply the Rule 144 / Rule 144A eligibility framework (below).

### Step 5: Deep Compliance Analysis

For each applicable exemption, conduct the deep analysis set out in the **Exemption
Framework Analysis** section below. Classify each requirement using the four-tier system:

| Status                  | Description                                                                                        |
| ----------------------- | -------------------------------------------------------------------------------------------------- |
| **COMPLIANT**           | Requirement fully satisfied; documentation adequate                                                |
| **PARTIAL**             | Requirement partially met; identified gaps require remediation                                     |
| **NON-COMPLIANT**       | Requirement not met; immediate remediation required                                                |
| **CRITICAL DEFICIENCY** | Fundamental exemption condition not met; offering may be an unlawful distribution; rescission risk |

### Step 6: Investor Qualification Review

**⟁ CLARIFY** — Before assessing investor qualification, ask:

- Has the issuer collected investor qualification questionnaires?
- For 506(c) offerings: Has the issuer taken "reasonable steps" to verify accredited
  investor status (documents-based or third-party letter approach)?
- Are there any investors who are non-US persons? (Triggers Reg S analysis)
- Are there any investors who are broker-dealers, investment companies, or employee
  benefit plans? (May affect integration or 3(c)(1)/3(c)(7) analysis)

### Step 7: Bad Actor Disqualification Check

Run the Rule 506(d) bad actor disqualification screen for all covered persons:
the issuer, each officer/director/general partner, 20%+ beneficial owners, promoters,
finder/placement agents, and any person compensated for solicitation. Apply the look-back
period and identify any events requiring disclosure under Rule 506(e).

**⟁ CLARIFY** — If any covered person has a potential disqualifying event:

- Ask the user to describe the event (date, court/regulator, type of order/conviction)
- Determine whether the event predates the look-back period
- Determine whether a waiver has been sought from the SEC
- Assess whether disclosure under Rule 506(e) is required

### Step 8: Filing Obligations Analysis

Map all required regulatory filings with deadlines:

- **Form D** (Reg D): Must be filed within 15 calendar days after first sale
  (17 C.F.R. § 230.503)
- **Form 1-A** (Reg A+): Filed on EDGAR before qualification; ongoing Form 1-K (annual)
  and Form 1-SA (semi-annual) post-qualification
- **Form C** (Reg CF): Filed on EDGAR before offering launch; Form C-U (updates),
  Form C-AR (annual), Form C-TR (termination)
- **Blue Sky**: Identify notice filing deadlines per state (typically 15 days after
  first sale in state)
- **EU**: Prospectus approved by competent authority before offer; passporting
  notification to host member state NCAs
- **UK**: FCA approval of prospectus (current regime) or POP operator registration
  (post-January 2026 reform); UKLA notification

### Step 9: Ongoing Compliance and Resale Restrictions

Identify ongoing compliance obligations post-offering:

- Restricted legend requirements on certificates / book-entry
- Transfer restriction enforcement procedures
- Reg D: Prohibition on general solicitation (506(b)) — ongoing for duration of offering
- Rule 144 holding period calendar for restricted securities
- Form D amendment requirements (material changes; annual updates if offering continues)
- Reg A+ Tier 2: Ongoing reporting obligations (Form 1-K / 1-SA / 1-U)
- EU: Ongoing disclosure obligations under MAR for listed securities

### Step 10: Generate Compliance Report

Produce the output using the **Output Format Template** at the end of this skill.
Run all Quality Gates before delivery. Present findings using the four-tier classification,
with remediation actions and filing deadlines anchored to specific dates where the
offering timeline is known.

---

## Exemption Framework Analysis

### Module 1: Regulation D — Rules 506(b) and 506(c)

**Statutory basis:** Securities Act § 4(a)(2); 17 C.F.R. § 230.506

#### Rule 506(b) — Private Placement Without General Solicitation

| Requirement                                                                                | Compliance Standard                                                                                          | Common Gaps                                                                                                       |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| No general solicitation or advertising                                                     | Zero tolerance — any mass communication to unvetted recipients destroys the exemption                        | Email blasts to purchased lists; LinkedIn posts about the offering; press releases mentioning specific deal terms |
| Unlimited accredited investors; max 35 non-accredited sophisticated investors per offering | Count carefully — investors across concurrent integrated offerings count together                            | Failure to count friends/family who lack sophistication; aggregating across related entities                      |
| Non-accredited investors meet sophistication standard                                      | Must have sufficient knowledge/experience to evaluate merits and risks, OR have purchaser representative     | Relying on investor self-certification of sophistication without factual basis                                    |
| Disclosure to non-accredited investors                                                     | If any non-accredited investor participates, disclosure documents equivalent to registered offering required | Providing offering materials to accredited investors only; assuming all investors are accredited                  |
| "Reasonable belief" as to accredited status                                                | Lower standard than 506(c) — issuer must form belief based on information available                          | No questionnaire; accepting oral representations without documentation                                            |
| Form D filing within 15 calendar days of first sale                                        | 17 C.F.R. § 230.503 — first sale date triggers clock                                                         | Late filing; incorrect first-sale date; failing to amend for material changes                                     |
| Bad actor disqualification screen                                                          | Rule 506(d) — all covered persons must be screened                                                           | Failure to screen placement agents, finders, 20%+ owners                                                          |
| No state registration required (covered security)                                          | 15 U.S.C. § 77r — NSMIA preempts state registration for Rule 506 offerings                                   | Forgetting state notice filing requirements (≠ registration, but still required in most states)                   |

**Integration with prior offerings:** Under the revised integration doctrine
(17 C.F.R. § 230.152, effective 2020), a completed offering more than 30 days before
does not integrate with a current Reg D offering. Concurrent offerings using different
exemptions may integrate — analyze each concurrent offering separately.

**⟁ CLARIFY** — If the issuer has conducted or is conducting any other securities
offering within the past 30 days, describe it to assess integration risk.

#### Rule 506(c) — Private Placement With General Solicitation Permitted

| Requirement                                    | Compliance Standard                                                                                                                          | Common Gaps                                                                             |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| All investors must be accredited investors     | No exceptions — even one non-accredited investor voids the exemption                                                                         | Failing to complete verification before accepting subscription                          |
| "Reasonable steps" to verify accredited status | Rule 506(c)(2)(ii) — documentation-based approach (income tax returns + bank statements + third-party letters) OR principles-based approach  | Relying solely on investor questionnaire/self-certification (insufficient under 506(c)) |
| General solicitation permitted                 | Must still comply with anti-fraud rules; no misleading statements in solicitation materials                                                  | Materially misleading offering summaries; failure to update stale projections           |
| Form D: Check "Rule 506(c)" box on Form D      | Correct box must be checked; cannot retroactively convert 506(b) to 506(c)                                                                   | Filing under 506(b) for a 506(c) offering                                               |
| Verification methods — income test             | Two most recent years' IRS Form W-2 or 1040 + written representation re current year                                                         | Accepting pay stubs as substitute for tax returns                                       |
| Verification methods — net worth test          | Bank/brokerage statements (within prior 3 months) + credit report + written representation re liabilities                                    | Failing to net out liabilities; failing to exclude primary residence                    |
| Third-party letter                             | Letter from registered broker-dealer, SEC-registered investment adviser, licensed attorney, or CPA                                           | Accepting letters from unregistered advisers; outdated letters (>90 days)               |
| Minimum investment amount safe harbor          | $200,000+ investment from investors other than natural persons raises a rebuttable presumption of accreditation [VERIFY — SEC 2023 guidance] | Treating the safe harbor as conclusive                                                  |

**2023 SEC Accredited Investor Amendments [VERIFY — confirm current effective date]:**
The SEC has extended the accredited investor definition to include: (i) individuals
holding Series 7, 65, or 82 licenses in good standing; (ii) "knowledgeable employees"
of a private fund; and (iii) certain spousal equivalents.

#### Rule 504 — Small Offering Exemption ($10M Cap)

| Requirement                                                  | Compliance Standard                                                                                                                                            |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Maximum $10M raised in any 12-month period                   | Aggregate of all Rule 504 offerings in 12 months                                                                                                               |
| No Exchange Act reporting company                            | Reporting companies, blank check companies, and investment companies ineligible                                                                                |
| State registration or exemption required                     | Unless securities are offered exclusively in one or more states that require public filing and delivery of disclosure document (see 17 C.F.R. § 230.504(b)(1)) |
| General solicitation permitted only in limited circumstances | Only if offering is registered in state permitting general solicitation, or meets Rule 504(b)(1)(iii) condition                                                |

---

### Module 2: Regulation A+ — Exempt Public Offering

**Statutory basis:** Securities Act § 3(b)(2); 17 C.F.R. §§ 230.251–230.263
(as amended by SEC Release No. 33-10786, effective March 15, 2021 — raising Tier 2 cap
from $50M to $75M)

#### Tier 1 vs. Tier 2 Comparison

| Feature               | Tier 1                                           | Tier 2                                                                                                     |
| --------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| Annual offering cap   | $20M (issuer + affiliates)                       | $75M (issuer + affiliates)                                                                                 |
| Re-sale cap           | $6M by affiliates                                | $22.5M by affiliates                                                                                       |
| Blue Sky preemption   | None — state registration/qualification required | Full — covered security under NSMIA                                                                        |
| EDGAR filing required | Form 1-A qualification required                  | Form 1-A qualification required                                                                            |
| Ongoing reporting     | None required post-qualification                 | Annual (Form 1-K), Semi-annual (Form 1-SA), Current report (Form 1-U)                                      |
| Audited financials    | Required for qualification                       | Required; must be in US GAAP                                                                               |
| Investor limits       | None — retail investors permitted                | Non-accredited natural persons limited to 10% of greater of annual income or net worth per 12-month period |
| Exchange listing      | Permitted                                        | Permitted                                                                                                  |

**Eligible issuers:** US and Canadian issuers not subject to Exchange Act reporting (with
exceptions); investment companies and blank check companies are ineligible.

**Testing the waters:** Issuers may "test the waters" — gauge investor interest before
filing Form 1-A — using oral or written communications, provided the communications
include specified legends and any written communications are filed with the SEC.

**Form 1-A components:**

- Part I: Notification (eligibility, type of offering, issuer information)
- Part II: Offering circular (business description, risk factors, MD&A, financial statements)
- Part III: Exhibits (articles, bylaws, material contracts, consent of auditors)

**Key compliance issues:**

- Bad actor disqualification applies (Rules 262/263)
- Annual offering cap measured over rolling 12-month period (not calendar year)
- Tier 2 investor limit applies only to non-accredited natural persons — no limit for
  entities or accredited investors
- Regulation A offerings may integrate with concurrent Reg D offerings — apply the 30-day
  safe harbor or factor-based analysis

---

### Module 3: Regulation CF — Equity Crowdfunding

**Statutory basis:** Securities Act § 4(a)(6); 17 C.F.R. §§ 227.100–227.503
(as amended by SEC Release No. 33-10884, effective March 15, 2021 — raising annual limit
from $1.07M to $5M)

| Requirement                                                                           | Compliance Standard                                                                                                                                                                                                             | Common Gaps                                                                                   |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Maximum $5M raised in any 12-month period                                             | All Reg CF offerings in 12 months aggregate; fractional compliance required                                                                                                                                                     | Failure to count simultaneous or overlapping Reg CF campaigns; counting wrong 12-month window |
| Must conduct offering through a registered funding portal or registered broker-dealer | 17 C.F.R. § 227.300 — direct issuer solicitation prohibited outside a portal                                                                                                                                                    | Hosting "crowdfunding" on issuer's own website without using a registered portal              |
| Investor limits (non-accredited natural persons)                                      | Per 12 months, greater of: (i) $2,500; (ii) if annual income or net worth <$107,000 [VERIFY current inflation-adjusted figure] — 5% of lesser; (iii) if both ≥$107,000 — 10% of lesser, max $107,000 (total across all issuers) | Failing to remind investors of the cross-issuer aggregate limit                               |
| Accredited investors                                                                  | No investment limit                                                                                                                                                                                                             | N/A                                                                                           |
| Form C filing on EDGAR                                                                | Must be filed before offering commences; includes business description, financial statements, use of proceeds, dilution                                                                                                         | Late filing; inadequate financial statements                                                  |
| Financial statement requirements                                                      | <$124,000 raised: reviewed or audited; $124,000–$618,000: reviewed by independent CPA; >$618,000: audited [VERIFY current inflation-adjusted thresholds]                                                                        | Using management-prepared financials above the reviewed threshold                             |
| 12-month lock-up on resale                                                            | Securities may not be transferred for 12 months, subject to limited exceptions (transfer to issuer, accredited investor, family member, trust, registered offering)                                                             | Permitting transfers without legal review of transfer restriction exceptions                  |
| Integration                                                                           | 30-day safe harbor with other exemptions; also consider prior Reg CF offerings in 12-month count                                                                                                                                | Failing to aggregate prior Reg CF campaigns                                                   |

**Regulation CF integration with Reg D:** The SEC confirmed that a Reg CF offering may
run concurrently with a Reg D offering to the same investors without integration, provided
they are structured as distinct, separate offerings. Use distinct subscription agreements,
separate offering materials, and separate closing mechanics.

---

### Module 4: Regulation S — Offshore Transactions

**Statutory basis:** Securities Act §§ 4(a)(2), 3(a)(9)-(11); 17 C.F.R. §§ 230.901–230.905

Regulation S provides that US registration requirements do not apply to offers and sales
of securities occurring outside the United States.

#### Two Safe Harbor Conditions (Rules 903 and 904)

1. **Offshore transaction**: Offer must not be made to a person in the United States;
   buyer must be outside the US at the time of offer and purchase (or the transaction
   must be executed on a foreign securities exchange).

2. **No directed selling efforts in the United States**: No directed selling efforts
   (general advertising, targeted marketing, etc.) directed at the US market.

#### Issuer Category Framework (Rule 903)

| Category       | Issuer Type                                                                                                         | Additional Conditions                                                                                                                                                  |
| -------------- | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Category 1** | Foreign issuers with no substantial US market interest (SUSMI)                                                      | No additional conditions beyond the two safe harbors                                                                                                                   |
| **Category 2** | Reporting foreign issuers; US issuers for debt securities and investment-grade asset-backed securities              | Distribution compliance period: 40 days for debt; distributors must agree to comply with offshore selling restrictions                                                 |
| **Category 3** | US domestic issuers for equity; reporting companies for equity; non-reporting foreign issuers for equity with SUSMI | Distribution compliance period: 1 year for equity of US domestic issuers; 6 months for reporting companies; legend + certification requirements; flowback restrictions |

**[JURISDICTION-SPECIFIC: Reg S is a US federal rule. The offshore jurisdiction's own
securities laws apply independently — verify local prospectus/registration requirements
in each country where securities are offered.]**

**Reg S + Reg D concurrent offering:** US issuers commonly conduct simultaneous Reg D
(US) and Reg S (offshore) offerings. The offshore tranche must strictly comply with
Category 3 conditions. The two tranches must not integrate — use separate subscription
agreements, separate pricing, and clear geographic separation of investor solicitation.

**Key red flags:**

- Any communication directed at US persons that mentions or implies the offshore offering
- Flowback into the US market during the distribution compliance period
- Failure to affix required restrictive legends on Category 3 equity securities

---

### Module 5: Rule 144 and Rule 144A — Resale Exemptions

**Statutory basis:** 17 C.F.R. § 230.144 (Rule 144); 17 C.F.R. § 230.144A (Rule 144A)

#### Rule 144 — Safe Harbor for Resale of Restricted and Control Securities

| Condition                      | Affiliates                                                                                                    | Non-Affiliates                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Holding period**             | 6 months if issuer is Exchange Act reporting; 1 year if non-reporting                                         | 6 months if reporting; 1 year if non-reporting; after 1 year, no further conditions |
| **Current public information** | Exchange Act reports must be current                                                                          | Required only during the 6-month to 1-year window                                   |
| **Volume limitations**         | Greater of: 1% of outstanding shares per class; or average weekly reported trading volume (preceding 4 weeks) | None after holding period satisfied                                                 |
| **Manner of sale**             | Brokers' transactions; directly with market makers; certain riskless principal transactions                   | None after holding period satisfied                                                 |
| **Form 144 filing**            | Required if volume sold in 3-month period exceeds 5,000 shares or $50,000                                     | Not required                                                                        |

**Control securities:** Securities held by affiliates (10%+ shareholders, directors,
officers) are "control securities" even if originally acquired in a registered offering.
Rule 144 conditions apply to affiliate resales regardless of acquisition method.

**Aggregation rule for affiliates:** All sales by affiliates who are deemed to be acting
in concert must be aggregated against the volume limitation. Controlled entities of an
affiliate also aggregate.

#### Rule 144A — Resale to Qualified Institutional Buyers (QIBs)

Rule 144A provides a safe harbor for resale of restricted securities to QIBs — entities
that own and invest on a discretionary basis at least $100M in securities of issuers
not affiliated with the entity (17 C.F.R. § 230.144A(a)(1)).

| Feature                   | Rule 144A                                                                                                       |
| ------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Eligible sellers          | Any person (not just original purchasers)                                                                       |
| Eligible buyers           | QIBs only — must verify QIB status                                                                              |
| Holding period            | None required                                                                                                   |
| Securities not listed     | Cannot use Rule 144A for securities of the same class as securities listed on a US national securities exchange |
| Concurrent Reg S offering | Permissible for offshore tranche — Rule 144A for US QIBs, Reg S for offshore                                    |
| PORTAL / DTC eligibility  | Rule 144A securities are typically traded through PORTAL Market or DTC                                          |

**[JURISDICTION-SPECIFIC: Rule 144A is a US-only safe harbor. Offshore jurisdictions
impose their own resale restrictions — verify in each relevant jurisdiction.]**

---

### Module 6: Integration Doctrine

**Statutory basis:** 17 C.F.R. § 230.152 (revised effective November 2020)

Under the revised integration doctrine, two concurrent or consecutive offerings integrate
(and must be analyzed as a single offering) if they are deemed part of a single plan of
financing. Integrated offerings that collectively fail an exemption may constitute an
unlawful distribution.

#### 30-Day Safe Harbor

An offering that is completed more than 30 calendar days before the commencement of a
subsequent offering is NOT integrated with the subsequent offering — regardless of any
other factors. This is the most important safe harbor.

#### Exemption-Specific Safe Harbors (Rule 152(b))

| Prior Offering        | Subsequent Offering        | Safe Harbor Condition                                                            |
| --------------------- | -------------------------- | -------------------------------------------------------------------------------- |
| Reg S (offshore)      | Reg D (domestic)           | Reg S offering complies with all applicable Category conditions                  |
| Registered offering   | Exempt offering            | Exempt offering commences after effective date of registration statement         |
| Reg D                 | Crowdfunding (Reg CF)      | Separate and distinct offering documents, mechanics, and investor communications |
| Employee benefit plan | Concurrent exempt offering | EBP complies with Rule 701 or Securities Act § 3(a)(11)                          |

#### Factors-Based Analysis (Where No Safe Harbor Applies)

When no safe harbor applies, the SEC considers five integration factors:

1. Are the offerings part of a single plan of financing?
2. Do the offerings involve issuance of the same class of security?
3. Are the offerings made at or about the same time?
4. Is the same type of consideration received in both offerings?
5. Are the offerings made for the same general purpose?

No single factor is determinative. A "same plan of financing" finding is the most
dangerous — it suggests the exemptions were used as a subterfuge to make a single
offering appear exempt.

**⟁ CLARIFY** — If the issuer has conducted or plans to conduct multiple concurrent or
consecutive offerings, describe each offering (type, size, timing, investor base) so the
integration analysis can be applied.

---

### Module 7: Blue Sky Laws (State Securities Regulation)

**Statutory basis:** Each state has its own securities act; National Securities Markets
Improvement Act of 1996 (NSMIA), 15 U.S.C. § 77r, preempts state registration for
"covered securities."

#### Covered Securities — Federal Preemption

| Security Type                   | Covered?                                                        | State Role                                                                                                       |
| ------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Rule 506(b) / 506(c) securities | YES — covered securities under § 18(b)(4)(D)                    | Notice filing and fee only (not registration); most states require filing within 15 days of first sale in state  |
| Rule 504 securities             | NO                                                              | Full state registration or state exemption required                                                              |
| Regulation A+ Tier 2            | YES — covered securities under § 18(b)(3)                       | Notice filing and fee; state may review quality of the offering (limited basis) [VERIFY current state positions] |
| Regulation A+ Tier 1            | NO                                                              | Full state registration or qualification required in each state                                                  |
| Regulation CF                   | NO — not a covered security                                     | Each state may impose its own requirements; many states exempt Reg CF offerings [VERIFY per state]               |
| Regulation S                    | Offshore only — no US state law applies to offshore transaction | N/A if properly structured; flowback into US triggers state requirements                                         |

**[JURISDICTION-SPECIFIC: State notice filing requirements vary significantly. Some states
(e.g., New York — Martin Act) have expansive anti-fraud jurisdiction even for covered
securities. Verify current requirements for each state where securities are sold.]**

**Common state compliance gaps:**

- Filing Form D with state securities administrator late or not at all
- Failure to pay state filing fees
- Selling to state residents before the notice filing deadline (some states require
  pre-sale filing)
- New York: Martin Act filing and anti-fraud compliance even for federal exemptions

---

### Module 8: EU Prospectus Regulation (Reg 2017/1129)

**Applicable law:** EU Prospectus Regulation (Regulation (EU) 2017/1129, as amended by
Regulation (EU) 2021/337 "Quick Fix" and Regulation (EU) 2022/2115 "Listing Act").

#### Registration Threshold and Exemptions

| Scenario                                                                              | Threshold / Condition                                                                   | EU Treatment                                                                                          |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Offer to the public                                                                   | Total consideration ≥ €8M in EU (12 months)                                             | Full prospectus required (or applicable exemption)                                                    |
| Offers in member states with higher threshold                                         | Members may raise threshold to €12M [VERIFY which states have adopted higher threshold] | Higher threshold applies in that state                                                                |
| Qualified investors only                                                              | No retail investors                                                                     | Prospectus not required (Art. 1(4)(a))                                                                |
| Fewer than 150 natural/legal persons per member state (excluding qualified investors) | Per-state count                                                                         | Prospectus not required (Art. 1(4)(b))                                                                |
| Minimum denomination ≥ €100,000                                                       | Per unit denomination                                                                   | Prospectus not required (Art. 1(4)(c))                                                                |
| Total consideration < €8M (or applicable higher threshold) in EU over 12 months       | Aggregate across EU                                                                     | Exempt from EU Prospectus Regulation; national laws may impose lighter regime [JURISDICTION-SPECIFIC] |
| M&A consideration securities                                                          | Shares offered as consideration in a takeover                                           | Prospectus not required; equivalent document (Art. 1(5)(d))                                           |
| Employee share plans                                                                  | Shares/options for employees or directors                                               | Prospectus not required; simpler document required (Art. 1(5)(f))                                     |

#### SME Growth Market Simplified Regime

Issuers with securities admitted to trading on an SME Growth Market may use the simplified
prospectus (Art. 15 of Reg 2017/1129). Key features:

- Simplified disclosure requirements (reduced minimum information items)
- Shorter review period by competent authority (10 working days vs. 20)
- Three-year universal registration document (URD) alternative

#### Passporting

Once a prospectus is approved by the competent authority (NCA) of the home member state,
it may be "passported" to any other EU member state by notification. The issuer notifies
the home NCA, which transmits a certificate of approval and the prospectus to the host
NCA. No re-approval required in host state. Timeline: 3 working days after notification.

**[JURISDICTION-SPECIFIC: Post-Brexit, UK no longer participates in EU passporting.
UK issuers must seek separate EU approval; EU issuers must seek separate FCA approval
for UK offers.]**

#### Prospectus Content Requirements

A full EU prospectus must contain (per Annexes to the Delegated Regulation (EU) 2019/980):

- **Registration document**: Issuer information, business overview, risk factors, financial
  statements (3 years, IFRS), management, shareholders, related-party transactions
- **Securities note**: Terms of the securities, use of proceeds, dilution, risk factors
  specific to the securities
- **Summary**: Maximum 7 pages, standardized ESMA format, 4-section structure

**Key anti-fraud provision:** Art. 11 of Reg 2017/1129 — civil liability for misleading
or omitted information in a prospectus. Offeror, issuer, guarantor, and underwriters
may be liable. [JURISDICTION-SPECIFIC: National law determines specific civil liability
remedies and the defendant class.]

---

### Module 9: UK Prospectus Regime — Pre- and Post-January 2026

**Current (Pre-January 2026) Regime:**

- FSMA 2000, s.85: Prohibition on offering transferable securities to the public in the
  UK without an approved prospectus (with exceptions)
- UK Prospectus Regulation (retained EU law post-Brexit): Broadly mirrors Reg 2017/1129;
  €8M threshold translated to £8M equivalent [VERIFY current FCA guidance]
- FCA Prospectus Regulation Rules (PRR) Sourcebook: Governs form and content of UK prospectuses
- FCA is the competent authority (UK Listing Authority / UKLA function)

**Post-January 2026 Reform — FSMA 2023 / FCA PS24/2:**

The FSMA 2023 substantially reformed UK prospectus law, with the new regime taking effect
in January 2026 (FCA Policy Statement PS24/2, published 2024):

| Feature                          | Pre-Reform (retained EU law)                               | Post-Reform (FSMA 2023 / PS24/2)                                                                                               |
| -------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Public offer prohibition         | s.85 FSMA 2000 — applies unless prospectus approved        | Revised s.85 — applies unless within an exemption or uses a Public Offer Platform                                              |
| Public Offer Platform (POP)      | Not available                                              | New regime: Offers via FCA-authorised POP operator without full prospectus; POP prepares and is responsible for offer document |
| Admission to UK-regulated market | Full UK Prospectus required                                | UK Prospectus required; streamlined for secondary issuances                                                                    |
| Secondary issuances              | Full prospectus (with URD shortcut)                        | Simplified forward-looking regime for secondary issuances by companies with existing disclosure record                         |
| Threshold for full prospectus    | £8M equivalent                                             | Revised — FCA has power to set by rules; new secondary issuance regime has higher threshold [VERIFY — PS24/2 final thresholds] |
| Private placement exemption      | Qualified investor / <150 persons / >£100,000 denomination | Preserved; FCA may adjust thresholds under rulemaking powers                                                                   |
| Retail offer without prospectus  | Not possible below POP                                     | Possible through FCA-authorised POP operator                                                                                   |

**[JURISDICTION-SPECIFIC: The January 2026 FCA PS24/2 reform timeline should be verified
against current FCA communications — delayed implementation is possible. Confirm
effective date before advising on the post-reform regime.]**

---

### Module 10: Bad Actor Disqualification — Rule 506(d) and 506(e)

**Applicable to:** All Reg D Rule 506 offerings (both 506(b) and 506(c)).

#### Covered Persons (17 C.F.R. § 230.506(d)(1))

1. The issuer (including predecessors and affiliated issuers)
2. Any director, executive officer, other officer participating in the offering, general
   partner, or managing member of the issuer
3. Any beneficial owner of 20% or more of the issuer's outstanding voting equity securities
   (calculated on the basis of voting power)
4. Any promoter connected with the issuer in any capacity at the time of the offering
5. Any investment manager of an issuer that is a pooled investment fund, and the general
   partners, managing members, and directors of any such investment manager
6. Any person that has been or will be paid (directly or indirectly) remuneration for
   solicitation of purchasers in connection with the offering (finder / placement agent)
   and the general partners, managing members, and directors of any such person

#### Disqualifying Events (17 C.F.R. § 230.506(d)(1))

- Criminal convictions for securities fraud, financial crimes, or breach of fiduciary duty
  (within 10 years for the issuer and its predecessors and affiliated issuers; 5 years for
  all other covered persons)
- Court injunctions and restraining orders in connection with securities, banking, or
  insurance matters (entered within 5 years)
- Final orders of state securities regulators, banking regulators, insurance regulators,
  federal banking agencies, CFTC (entered within 10 years if related to fraud or within
  5 years otherwise)
- SEC orders (cease and desist orders related to violations of any section of the Securities
  Act, Exchange Act, Investment Advisers Act, Investment Company Act, or commodity laws;
  bars and suspensions)
- FINRA bars or suspensions
- US Postal Service false representation orders (entered within 5 years)

#### Rule 506(e) — Disclosure of Prior Events Outside Look-Back Period

If a disqualifying event occurred before the look-back period, the offering may still
proceed, but the issuer must disclose the event in writing to each purchaser before sale.
Failure to make the required disclosure is itself a violation — even if the underlying
event no longer disqualifies.

**⟁ CLARIFY** — Request the following for each covered person:

- Full name and role in the offering
- Any SEC, FINRA, state securities regulator, banking regulator, or court orders,
  injunctions, convictions, or sanctions in the past 10 years
- Any prior securities-related enforcement history (regardless of date)

---

## Severity Classification and Remediation Framework

### Four-Tier Classification

| Tier | Label                   | Definition                                                                                                                                  | Action Required                                                                          |
| ---- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| 1    | **COMPLIANT**           | Requirement fully satisfied; documentation adequate                                                                                         | Document and maintain; no immediate action needed                                        |
| 2    | **PARTIAL**             | Requirement partially met; identified documentation gaps or procedural weaknesses                                                           | Remediate within 30 days; document corrective action                                     |
| 3    | **NON-COMPLIANT**       | Requirement not met; offering condition not satisfied                                                                                       | Immediate remediation before closing or further solicitation; legal counsel review       |
| 4    | **CRITICAL DEFICIENCY** | Fundamental exemption condition not met; offering may constitute unlawful distribution; rescission risk; potential SEC enforcement exposure | STOP — do not close; engage securities counsel immediately; assess rescission obligation |

### Automatic CRITICAL DEFICIENCY Triggers

The following conditions automatically trigger CRITICAL DEFICIENCY regardless of
surrounding facts:

- General solicitation occurred in a Rule 506(b) offering (even one mass communication)
- Non-accredited investor participated in a Rule 506(c) offering
- Undisclosed bad actor event for a covered person
- Form D not filed and offering has closed (late filing — assess cure options)
- EU/UK offer to the public above threshold with no approved prospectus and no exemption
- Regulation S Category 3 offering with flowback into the US during the 1-year compliance
  period
- Annual cap exceeded (Reg A+, Reg CF) — amount above cap constitutes unregistered offering
- Offering conducted by an ineligible issuer (blank check company, disqualified issuer)

---

## Prioritization Framework

### Priority Tiers for Remediation

| Priority                | Label                       | Timeframe   | Criteria                                                                                                                 |
| ----------------------- | --------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------ |
| **P1 — Critical**       | STOP the offering           | Immediately | Any CRITICAL DEFICIENCY; any undisclosed bad actor event; any offer to non-accredited investor in 506(c) offering        |
| **P2 — High**           | Remediate before next close | 72 hours    | Late Form D (file immediately); missing investor verification documents for 506(c); annual cap at risk of being exceeded |
| **P3 — Material**       | Remediate within 30 days    | 30 days     | PARTIAL compliance items; state notice filing delinquencies; legend deficiencies on previously issued certificates       |
| **P4 — Administrative** | Address in next cycle       | 60–90 days  | Non-material procedural improvements; documentation enhancements; training                                               |

---

## Compliance Requirement Checklist

### Pre-Offering Checklist (All Exemptions)

- [ ] Exemption selected and documented in legal opinion or counsel memorandum
- [ ] Offering amount confirmed within exemption caps (12-month trailing calculation)
- [ ] Issuer eligibility verified (not an ineligible issuer for selected exemption)
- [ ] Bad actor screen completed for all covered persons; results documented
- [ ] Integration analysis completed for all concurrent and recent offerings
- [ ] Offering materials reviewed for anti-fraud compliance (no material misstatements
      or omissions)
- [ ] Investor qualification documentation procedures established
- [ ] State Blue Sky compliance map prepared

### Reg D — Specific Pre-Offering Checklist

- [ ] General solicitation prohibition acknowledged (506(b)) OR verification procedures
      established (506(c))
- [ ] Investor count: accredited (unlimited); non-accredited (max 35 for 506(b))
- [ ] Non-accredited investor disclosure document prepared (if any non-accredited investors)
- [ ] Form D filing calendar prepared (15-day post-first-sale deadline)
- [ ] State notice filing calendar prepared per identified states
- [ ] Subscription agreement includes required representations and investor questionnaire

### Reg A+ — Specific Pre-Offering Checklist

- [ ] Form 1-A drafted and reviewed; financial statements audited (US GAAP)
- [ ] Testing-the-waters materials include required legends if used pre-qualification
- [ ] Offering circular reviewed for compliance with Part 253 of Reg A
- [ ] Bad actor screen completed (Rules 262/263)
- [ ] Post-qualification ongoing reporting obligations documented (Form 1-K, 1-SA, 1-U)
- [ ] Tier 2 investor cap calculation process established for non-accredited natural persons
- [ ] Blue Sky compliance confirmed (Tier 2 preempted; Tier 1 full state compliance required)

### Reg CF — Specific Pre-Offering Checklist

- [ ] Registered funding portal or broker-dealer engaged
- [ ] Annual $5M cap verified against prior 12-month Reg CF offerings
- [ ] Financial statements prepared at correct level (reviewed vs. audited per amount)
- [ ] Form C filed on EDGAR before offering launch
- [ ] Investor limit calculation mechanism established
- [ ] 12-month transfer restriction documented in subscription agreement

### Regulation S — Specific Pre-Offering Checklist

- [ ] All investors confirmed as non-US persons (definitions in Rule 902(k) apply)
- [ ] Category of issuer determined (Category 1, 2, or 3)
- [ ] Directed selling efforts prohibition confirmed; no US-directed marketing materials
- [ ] Distribution compliance period identified and calendar prepared
- [ ] Required legends affixed (Category 3 equity securities)
- [ ] Offshore legal counsel confirmation of compliance with local laws obtained
- [ ] Certification and undertaking from distributors obtained (Category 2/3)

---

## Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                                                                                     | Fail Action                                          |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| **Source**     | Every regulatory citation references a specific CFR section, release number, or statutory provision                                                                      | Add citation or mark "[UNVERIFIED]"                  |
| **Format**     | All US citations follow standard format (e.g., "17 C.F.R. § 230.506(b)"); EU citations reference the Regulation and Article                                              | Fix format                                           |
| **Currency**   | Every cited provision checked for amendments; 2020 integration doctrine revision, 2021 Reg A+/CF cap increases, 2023 accredited investor amendments noted where relevant | Flag "[CHECK CURRENCY — rule may have been amended]" |
| **Domain**     | Analysis stays within federal securities law and identified state/EU/UK frameworks; does not bleed into unrelated regulatory domains                                     | Remove or flag cross-domain analysis                 |
| **Confidence** | Uncertainty explicitly stated; state Blue Sky requirements marked [JURISDICTION-SPECIFIC]; UK post-reform timeline marked [VERIFY]                                       | Add confidence qualifier                             |

---

## Self-Interrogation for CRITICAL DEFICIENCY Findings

For any finding classified as CRITICAL DEFICIENCY, apply this three-pass review before
reporting it:

**Pass 1 — Legal Chain Integrity**: Is the deficiency based on a correct reading of the
applicable rule? Is the specific condition cited correctly? Would the SEC Division of
Corporation Finance or a court actually reach this conclusion on these facts?

**Pass 2 — Completeness**: Have all potentially applicable exemptions, safe harbors, and
curative steps been considered? Is there a waiver, no-action letter, or interpretive
release that addresses this specific fact pattern?

**Pass 3 — Challenge**: What is the strongest counter-argument? What would competent
issuer's counsel argue in response? Under what circumstances might a reasonable securities
attorney accept the risk of proceeding?

---

## Confidence Scoring

| Level        | Range     | Meaning                                                   | Action                                                                     |
| ------------ | --------- | --------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled SEC rule, clear statutory text                    | State with confidence; cite specific CFR section                           |
| **High**     | 0.80–0.94 | Strong regulatory authority; minor interpretive questions | State with brief caveat; note the interpretive question                    |
| **Probable** | 0.60–0.79 | Good arguments but SEC guidance is incomplete or dated    | State with reasoning and contra-indicators; recommend counsel confirmation |
| **Possible** | 0.40–0.59 | Genuine uncertainty; no clear no-action letter or rule    | Flag for securities counsel review with both sides of the argument         |
| **Unlikely** | 0.00–0.39 | Weak legal basis; speculative interpretation              | Do not assert; flag "[UNCERTAIN — requires securities counsel opinion]"    |

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-securities-regulation-compliance"
  mode: "[Structure / Audit / Resale]"
  offering_type: "[Reg D 506(b) / 506(c) / Reg A+ Tier 1 / Tier 2 / Reg CF / Reg S / Rule 144 / Rule 144A / Concurrent]"
  jurisdictions_analyzed: "[US federal / Blue Sky states / EU / UK / Other]"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "/tmp/legalcode-securities-research.md OR Not created"
  critical_deficiencies_found: "[number]"
  non_compliant_items: "[number]"
  partial_items: "[number]"
  compliant_items: "[number]"
  bad_actor_screen_completed: "Yes / No / Pending information"
  integration_analysis_completed: "Yes / No / Not required"
  quality_score: "[X]/40"
  completeness: "18/18 elements"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "State Blue Sky requirements are jurisdiction-specific — verify per identified states"
    - "UK January 2026 reform implementation timeline should be confirmed against current FCA communications"
    - "Accredited investor definition amendments — verify current effective provisions"
    - "Digital assets / tokens: Howey test analysis required; not covered by this skill module"
    - "Investment company status (3(c)(1) / 3(c)(7)) — verify eligibility separately"
  reviewer: "AI-assisted — requires review by licensed securities attorney before reliance"
```

---

## Anti-Patterns

What NOT to do when conducting securities regulation compliance analysis:

1. **Relying on investor self-certification for 506(c) offerings.** The single most common
   and dangerous error. Under Rule 506(c), a questionnaire or checkbox is not "reasonable
   steps." Income tax returns, bank statements, or a third-party accreditation letter are
   required. Self-certification suffices only under 506(b).

2. **Conflating the 30-day integration safe harbor with a blanket rule.** The 30-day safe
   harbor protects a completed offering from integrating with a subsequent offering — it
   does NOT apply to concurrent offerings. Two simultaneous offerings always require
   factor-based integration analysis.

3. **Forgetting to run the bad actor screen on finders and placement agents.** Most issuers
   screen officers and directors but overlook compensated solicitors, placement agents,
   and finders. A single disqualifying event for a finder voids the entire Rule 506 offering.

4. **Using Reg S as a disguised US offering.** Directing US persons to offshore entities
   that then immediately re-sell to US persons (the "flowback" problem) defeats Reg S.
   The SEC scrutinizes short distribution compliance periods and immediate resale patterns.

5. **Forgetting that Reg A+ Tier 1 does NOT preempt Blue Sky.** Many practitioners
   assume all Reg A+ offerings preempt state registration. Only Tier 2 is a covered
   security under NSMIA. Tier 1 requires individual state qualification — often a
   significant undertaking.

6. **Missing the 15-day Form D filing deadline.** The 15-day clock runs from the date of
   first sale, not the closing date. In soft-circled deals where subscription agreements
   are signed before funds arrive, confirm which event constitutes "first sale" under
   Rule 902(a)(1) of Reg D.

7. **Aggregating Reg CF offerings incorrectly.** The $5M annual cap aggregates all Reg CF
   offerings by the same issuer over a 12-month look-back period — not a calendar year.
   Late-year Reg CF campaigns frequently exceed the cap because prior campaigns are not
   counted.

8. **Treating Reg S as a permanent solution for US issuer equity.** For US domestic
   issuers offering equity, the Category 3 distribution compliance period is 1 year.
   During that year, any transfer of securities to a US person defeats Reg S. Robust
   transfer restriction mechanics (stop-transfer instructions, legends, certification
   requirements for transfers) are essential.

9. **Assuming EU passporting applies in the UK.** Since Brexit, UK is no longer part of
   the EU passporting system. A prospectus approved in France does not authorize a UK
   public offer. Separate FCA approval (or reliance on a UK exemption) is required.

10. **Ignoring the Martin Act (New York).** New York's Martin Act (General Business Law
    Article 23-A) has broad anti-fraud jurisdiction and is not preempted by federal
    securities law for fraud claims. Even a properly structured Reg D offering must comply
    with New York anti-fraud requirements. The New York AG can and does bring enforcement
    actions against nationally distributed offerings.

11. **Missing the Reg CF 12-month resale lock-up.** Securities issued in a Reg CF offering
    cannot be transferred for 12 months without exception (other than back to the issuer,
    to accredited investors, family members, or in connection with a registered offering).
    Issuers often fail to implement transfer restrictions in their cap table system,
    creating inadvertent violations.

12. **Under-specifying "offshore transaction" in Reg S.** The Rule 902(h) definition of
    "offshore transaction" requires the offer not to be made to a person in the United
    States AND the buyer to be outside the United States at the time of the buy order. A
    foreign person who places a buy order while temporarily visiting the United States
    does not satisfy Reg S without additional structuring.

13. **Failing to update Form D on material changes.** Form D must be amended within
    15 days of any change in the information required to be included in the form. Common
    missed triggers: change in the total offering amount, addition of a new placement
    agent, or change in the minimum investment amount.

14. **Structuring around integration by creating technical separations.** Splitting one
    offering into two using artificial distinctions (different closing dates on the same
    deal, different names for the same issuer vehicle) does not defeat integration.
    The SEC focuses on substance over form — two offerings serving the same general
    financing purpose are integrated.

15. **Overlooking Rule 144(d)(3) tacking for converted securities.** When restricted
    securities are converted into another class (e.g., preferred stock converts to common),
    the holding period from the original acquisition "tacks" onto the converted securities.
    However, tacking is not available if additional consideration is paid on conversion.

16. **Assuming digital tokens are not securities.** The Howey test (SEC v. W.J. Howey Co.,
    328 U.S. 293 (1946)) applies to all investment contracts regardless of form. Most
    utility tokens and virtually all profit-sharing tokens are securities. Structuring a
    token offering as a "utility" without substantive legal analysis is high-risk. The SEC
    has brought enforcement actions against token issuers that relied on this assumption.

17. **Forgetting ongoing Reg A+ Tier 2 reporting.** Qualification under Reg A+ Tier 2
    creates ongoing Exchange Act-like reporting obligations. Annual Form 1-K must be filed
    within 120 days of fiscal year-end; semi-annual Form 1-SA within 90 days of mid-year.
    Many Reg A+ issuers are unaware of these obligations or fail to comply, creating
    suspension of the offering privilege.

---

## Writing Standards and Plain-Language Discipline

Before delivering any output under this skill:

1. **Replace jargon with precision.** Do not use "securities laws" or "regulations" when
   the specific statute or rule is identifiable. Write "17 C.F.R. § 230.506(b)" not
   "Regulation D."

2. **Anchor every deadline to a trigger event and a specific date.** "Form D is due 15
   calendar days after first sale" → "Form D is due by [specific date] based on a first
   sale date of [date]."

3. **State the consequence of non-compliance.** Not just "the requirement is not met" but
   "failure to satisfy this requirement means the 506(c) exemption is unavailable and the
   offering constitutes an unregistered distribution under Securities Act § 5, subject to
   rescission rights under § 12(a)(1)."

4. **Do not overstate confidence on Blue Sky requirements.** State Blue Sky compliance
   is highly fact-specific and changes frequently. Always mark with [JURISDICTION-SPECIFIC]
   and recommend verification with a state securities practitioner.

5. **Label all assumptions.** If the analysis proceeds on assumed facts (e.g., "assuming
   all investors are US persons"), state the assumption explicitly and note the consequence
   if the assumption is wrong.

6. **Verify numeric thresholds before each use.** Reg A+, Reg CF, and accredited investor
   thresholds are subject to SEC amendment. Always include a [VERIFY — confirm current
   SEC-published threshold] annotation for any monetary or percentage threshold derived
   from a delegated rulemaking provision.

---

## External Tool Integration

**With legalcode-mcp connected:**

- Search for the most recent text of 17 C.F.R. §§ 230.500–230.508 (Reg D), 230.251–230.263
  (Reg A+), 227.100–227.503 (Reg CF), and 230.901–230.905 (Reg S)
- Retrieve the current version of Form D, Form 1-A, and Form C instructions
- Search for recent SEC no-action letters and interpretive releases on offering integration,
  bad actor disqualification, and accredited investor verification
- Search for FCA PS24/2 and FSMA 2023 prospectus reform implementation guidance
- Save verified citations to `/tmp/legalcode-securities-research.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Use this skill's embedded regulatory framework
- Mark all statutory and regulatory citations with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Recommend that the user independently verify all thresholds, deadlines, and filing
  requirements against SEC.gov, EDGAR.gov, and FCA.org.uk before relying on any output

---

## Output Format Template

````markdown
# Securities Regulation Compliance Report

**Date:** [date]
**Issuer:** [issuer name]
**Offering:** [description of offering]
**Mode:** [Structure / Audit / Resale]
**Exemption(s) Analyzed:** [list]
**Jurisdictions:** [US federal, states, EU, UK]
**Prepared by:** Legalcode Securities Regulation Compliance Skill (AI-assisted — not legal advice)

---

## Executive Summary

[2–4 sentences: what was analyzed, overall compliance status, number of critical/high
issues, and highest-priority recommended action.]

**Overall Compliance Status:** [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]

| Category                  | Count |
| ------------------------- | ----- |
| CRITICAL DEFICIENCY items | [N]   |
| NON-COMPLIANT items       | [N]   |
| PARTIAL items             | [N]   |
| COMPLIANT items           | [N]   |

---

## Exemption Eligibility Matrix

| Exemption         | Available?                         | Key Condition(s) | Status   |
| ----------------- | ---------------------------------- | ---------------- | -------- |
| Reg D 506(b)      | [Yes/No/Conditional]               | [Key condition]  | [Status] |
| Reg D 506(c)      | [Yes/No/Conditional]               | [Key condition]  | [Status] |
| Reg A+ Tier 1     | [Yes/No/Conditional]               | [Key condition]  | [Status] |
| Reg A+ Tier 2     | [Yes/No/Conditional]               | [Key condition]  | [Status] |
| Reg CF            | [Yes/No/Conditional]               | [Key condition]  | [Status] |
| Reg S             | [Yes/No/Conditional]               | [Key condition]  | [Status] |
| EU Prospectus Reg | [Applicable/Not Applicable/Exempt] | [Key condition]  | [Status] |
| UK Prospectus Reg | [Applicable/Not Applicable/Exempt] | [Key condition]  | [Status] |

**Recommended Exemption:** [Primary recommendation with brief rationale]

---

## Critical Deficiencies (P1 — STOP)

[If none: "No critical deficiencies identified."]

### CD-1: [Short Title]

**Classification:** CRITICAL DEFICIENCY
**Requirement:** [Specific regulatory requirement, cited with CFR/statutory reference]
**Finding:** [Specific fact(s) giving rise to the deficiency]
**Consequence:** [Specific legal consequence — rescission rights, enforcement exposure, etc.]
**Required Action:** [Precise remediation step]
**Deadline:** IMMEDIATE — do not close further subscriptions until resolved
**Confidence:** [Score and rationale]

---

## Non-Compliant Items (P2/P3)

[Format same as Critical Deficiencies section; label each NC-1, NC-2, etc.]

---

## Partial Compliance Items (P3/P4)

[Format same above; label each PC-1, PC-2, etc.]

---

## Compliant Items

| Item   | Requirement   | Status    | Notes       |
| ------ | ------------- | --------- | ----------- |
| [Item] | [Requirement] | COMPLIANT | [Any notes] |

---

## Bad Actor Disqualification Screen

| Covered Person | Role   | Events Identified | Status                |
| -------------- | ------ | ----------------- | --------------------- |
| [Name]         | [Role] | [None / See note] | COMPLIANT / DEFICIENT |

[If any events identified: describe event, look-back period analysis, disclosure requirement]

---

## Integration Analysis

**Prior / concurrent offerings:** [List]
**30-day safe harbor applies:** [Yes / No / N/A]
**Factor-based analysis (if no safe harbor):** [Summary]
**Integration risk:** [NONE / LOW / MEDIUM / HIGH]

---

## Filing Obligations and Deadlines

| Filing               | Form     | Platform         | Deadline                         | Status                          |
| -------------------- | -------- | ---------------- | -------------------------------- | ------------------------------- |
| Reg D notice         | Form D   | EDGAR            | [Date — 15 days post first sale] | [Filed / Not yet due / OVERDUE] |
| [State] notice       | [Form]   | [State platform] | [Date]                           | [Status]                        |
| Reg A+ qualification | Form 1-A | EDGAR            | [Date — before first sale]       | [Status]                        |
| [Other]              |          |                  |                                  |                                 |

---

## Blue Sky Compliance Map

| State   | Investors? | Coverage                         | Requirement                                  | Status   | Deadline |
| ------- | ---------- | -------------------------------- | -------------------------------------------- | -------- | -------- |
| [State] | [Yes/No]   | [Covered security / Not covered] | [Notice filing / Full registration / Exempt] | [Status] | [Date]   |

---

## Ongoing Compliance Calendar

| Obligation                          | Frequency    | Next Due Date       | Responsible Party        |
| ----------------------------------- | ------------ | ------------------- | ------------------------ |
| Form D amendment (material changes) | As triggered | [Date if triggered] | Issuer / Counsel         |
| [Reg A+ Form 1-K annual]            | Annual       | [Date]              | Issuer                   |
| [Reg CF Form C-AR]                  | Annual       | [Date]              | Issuer / Portal          |
| [Restricted legend review]          | Per transfer | As triggered        | Transfer Agent / Counsel |

---

## Recommended Actions — Priority Order

| Priority | Action                  | Owner   | Deadline                 |
| -------- | ----------------------- | ------- | ------------------------ |
| P1       | [Critical action]       | [Owner] | IMMEDIATE                |
| P2       | [High action]           | [Owner] | [Date — within 72 hours] |
| P3       | [Material action]       | [Owner] | [Date — within 30 days]  |
| P4       | [Administrative action] | [Owner] | [Date — within 90 days]  |

---

## Glass Box Audit Trail

```yaml
[See Glass Box Audit Trail Template above — populate with actual values]
```
````

---

## Limitations and Important Notices

- This report is AI-assisted and does not constitute legal advice.
- All threshold amounts and regulatory citations should be independently verified against
  current SEC and FCA publications before reliance.
- State Blue Sky requirements are jurisdiction-specific — verify with state securities
  administrator websites or local counsel.
- UK January 2026 reform implementation timeline should be confirmed against current FCA
  publications.
- Digital asset / token offerings require separate Howey test analysis beyond the scope
  of this report.
- This report does not address Investment Company Act eligibility (3(c)(1) / 3(c)(7)).

```

---

## Localization Notes

This skill analyzes three regulatory frameworks. Applying it outside the US / EU / UK
perimeter requires the following adjustments:

**For Canada:** Canadian securities regulation is primarily provincial. National Instrument
45-106 governs private placement exemptions across provinces; equivalent of Reg D is
typically the "accredited investor exemption" or "offering memorandum exemption." Federal
registration exemptions under the Securities Act (Ontario) or BCSA differ materially from
US Reg D. [JURISDICTION-SPECIFIC — engage Canadian securities counsel.]

**For Australia:** Chapters 6D and 7 of the Corporations Act 2001 govern securities
offers. Key exemptions: offers to sophisticated investors (s.708(8)), small-scale offers
(s.708(1) — 20 investors / $2M cap), offers to accredited investors. ASIC administers
the regime. [JURISDICTION-SPECIFIC — engage Australian securities counsel.]

**For Asia-Pacific jurisdictions:** Singapore, Hong Kong, Japan, and other APAC
jurisdictions each have their own securities regimes with institutional/sophisticated
investor exemptions broadly analogous to Reg D but with material differences in threshold
amounts, filing requirements, and investor count limits. [JURISDICTION-SPECIFIC — engage
local securities counsel in each relevant jurisdiction.]

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis drawing on:
- 17 C.F.R. §§ 230.500–230.508 (Regulation D), 230.251–230.263 (Regulation A+),
  227.100–227.503 (Regulation CF), 230.901–230.905 (Regulation S), 230.144, 230.144A
- Securities Act of 1933, 15 U.S.C. § 77a et seq.
- JOBS Act of 2012 (Titles II, III, IV)
- SEC Release No. 33-10786 (Reg A+ / Reg CF cap increases, 2021)
- SEC Release No. 33-10824 (Integration doctrine amendment, 2020)
- SEC Release No. 33-10884 (Regulation CF amendments, 2021)
- EU Prospectus Regulation (Regulation (EU) 2017/1129)
- FSMA 2000, FSMA 2023; FCA Policy Statement PS24/2 (January 2026 prospectus reform)
- FCA Prospectus Regulation Rules (PRR) Sourcebook
- ESMA Guidelines on prospectus disclosure (ESMA32-382-1138)
- 15 U.S.C. § 77r (NSMIA — covered securities / Blue Sky preemption)
- FINRA Rule 5110 (underwriting compensation in exempt offerings) [VERIFY applicability]
- Legalcode AML/KYC Compliance skill patterns and framework structure
- Legalcode Contract Review quality framework (Glass Box, Self-Interrogation,
  Citation Quality Gates, Confidence Scoring)
All legal references should be independently verified by a licensed securities attorney
before use in connection with an actual offering or transaction.
```
