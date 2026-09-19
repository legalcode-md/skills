---
name: legalcode-us-reg-s-offering-review
description: Reviews offshore securities offerings and resale controls under SEC Regulation S (17 CFR
  §§ 230.901–230.905). Use when conducting Reg S compliance reviews, structuring offshore offering transactions,
  reviewing offering documents for Reg S compliance, assessing resale restriction mechanics, analyzing
  concurrent domestic/offshore offering integration, performing capital markets due diligence, or advising
  on post-distribution-period resale procedures.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Reviews offshore securities offerings and resale controls under SEC Regulation S (17 CFR §§ 230.901–230.905). Covers Category 1/2/3 issuer safe harbor analysis, directed selling effort restrictions and safe harbors, distribution compliance period mechanics (40-day, 6-month, and 1-year), SUSMI (substantial US market interest) determination for equity and debt, Rule 903 issuer/distributor conditions, Rule 904 reseller safe harbor, Rule 905 restricted securities and Rule 144 tacking, debt vs. equity distinctions (TEFRA C/D, Eurobond mechanics, global notes), concurrent Reg D/Rule 144A integration analysis (Rule 152 / Release 33-10736), transfer restriction legends and removal procedures, foreign private issuer qualification and reporting obligations, hedging restrictions, ADR deposit controls, subscription agreement representations, and common enforcement red flags. Use when conducting Reg S compliance reviews, structuring offshore offering transactions, reviewing offering documents for Reg S compliance, assessing resale restriction mechanics, analyzing concurrent domestic/offshore offering integration, performing capital markets due diligence, or advising on post-distribution-period resale procedures. Jurisdiction: United States federal securities law (SEC enforcement, Securities Act of 1933, 17 CFR §§ 230.901–230.905).


# Legalcode US Regulation S Offering Review

> **Disclaimer**: This skill provides a framework for AI-assisted Regulation S compliance
> review. It does not constitute legal advice. All outputs must be reviewed by qualified
> securities counsel admitted to practice in the United States before use. Regulation S
> and its application evolve through SEC rule amendments, no-action letters, staff
> guidance, and enforcement actions. Statutory and case law references cited from memory
> carry hallucination risk — verify against authoritative SEC sources before relying on
> them. The Regulation S safe harbor is highly fact-specific; minor variations in offering
> structure, jurisdiction, issuer type, or security type can change the category and
> conditions that apply.

---

## Purpose and Scope

This skill performs a structured Regulation S compliance review covering all major
analytical domains relevant to offshore securities offerings under SEC rules.

**Covers:**

- Category determination (Category 1, 2, or 3) based on issuer type, security type, and SUSMI
- Directed selling efforts compliance — what is prohibited, permitted, and borderline
- Distribution compliance period mechanics — period length, conditions, and running of the clock
- Issuer and distributor obligations under Rule 903 (issuer/distributor safe harbor)
- Reseller obligations and rights under Rule 904 (reseller safe harbor)
- Rule 905 restricted securities status and Rule 144 interaction
- Debt securities mechanics: TEFRA conventions, global note structures, Eurobond market practice
- Equity securities mechanics: Category 3 hedging restrictions, ADR deposit prohibition, legend requirements
- Integration of concurrent Reg S and domestic offering (Reg D, Rule 144A, Rule 152 / Release 33-10736)
- Foreign private issuer (FPI) qualification, SUSMI analysis, and Exchange Act reporting
- Transfer restriction legends: form, placement, and removal procedure
- Subscription agreement and purchaser certification requirements
- Enforcement patterns and common red flags from SEC enforcement history

**Does not:**

- Cover Regulation A or Regulation CF (crowdfunding) offshore offering implications
- Provide advice on non-US securities regulations (EU Prospectus Regulation, UK FSMA, etc.)
- Constitute legal advice or substitute for qualified US securities counsel
- Address Exchange Act Section 12(g) foreign private issuer registration obligations in depth
- Apply to municipal securities, government securities, or exempted securities

---

## Jurisdiction and Governing Law

**Primary Statute**: Securities Act of 1933, § 5 (15 U.S.C. § 77e) — registration requirement
that Regulation S operates as a safe harbor from.

**Regulation**: Regulation S, 17 CFR §§ 230.901–230.905.

**Key Definitions Rule**: 17 CFR § 230.902 (US person, offshore transaction, directed selling
efforts, SUSMI, distribution compliance period, distributor).

**Issuer/Distributor Safe Harbor**: 17 CFR § 230.903.

**Reseller Safe Harbor**: 17 CFR § 230.904.

**Restricted Securities**: 17 CFR § 230.905.

**Integration**: 17 CFR § 230.152 (as amended by SEC Release No. 33-10736, Nov. 2, 2020).

**Key SEC Releases**:

- SEC Release No. 33-7190 (June 27, 1995) — Problematic Practices Interpretive Release [VERIFY]
- SEC Release No. 33-7505 (Feb. 25, 1998) — 1998 Amendments strengthening Category 3 [VERIFY]
- SEC Release No. 33-10736 (Nov. 2, 2020) — Integration Framework Modernization [VERIFY]

**Enforcement authorities**: SEC Division of Enforcement (civil); DOJ (criminal Section 5
violations where willful conduct established under 15 U.S.C. § 77x).

**Subject matter jurisdiction**: All analysis in this skill is US-law-only. Where a transaction
also implicates non-US securities regulation (EU Prospectus Regulation, UK FSMA Prospectus
Rules, MiFID II marketing restrictions), this skill flags the intersection but defers to
jurisdiction-specific skills for those regimes.

---

## Interactive Clarification

This skill uses **interactive clarification** (⟁ CLARIFY) at decision points where:

- The answer changes category classification or condition requirements
- Multiple analytical paths exist for the same offering structure
- Fact-specific determinations require issuer/counsel input
- Integration analysis requires knowledge of concurrent domestic offering terms

When marked ⟁ CLARIFY, present structured options. If the user has already provided the
information, skip the question and proceed. For batch/non-interactive runs, use the default
stated at each CLARIFY point.

---

## Workflow

### Step 1: Accept Input

Accept the review request in any format:

- **Offering documents**: Preliminary or final offering memorandum, term sheet, prospectus supplement, subscription agreement, purchase agreement, underwriting agreement
- **Transaction description**: Narrative of the proposed or completed offering structure, issuer identity, security type, and target investor base
- **Resale context**: Description of a proposed secondary market resale, with identity of seller (original distributor, investor, affiliate) and proposed buyer
- **Due diligence checklist request**: Request to assess Reg S compliance for a portfolio company or target

If no input is provided beyond a general request for Reg S review, proceed to Step 2 to gather the facts needed for category determination.

---

### Step 2: Gather Offering Context

**⟁ CLARIFY** — Before scoping the review, gather this context (skip what is already known):

1. **Issuer type and reporting status**:
   - Options: **Foreign Private Issuer (FPI) — SEC reporting** (files Form 20-F, 6-K),
     **Foreign Private Issuer — non-reporting** (no Exchange Act periodic reports),
     **Domestic issuer — SEC reporting** (files Form 10-K, 10-Q, 8-K),
     **Domestic issuer — non-reporting** (no Exchange Act periodic reports),
     Unknown/to be determined
   - _Why this matters_: Issuer type is the single most important variable in category
     determination. FPI reporting status governs whether equity falls in Category 1, 2,
     or 3; domestic issuer equity always falls in Category 3.

2. **Security type**:
   - Options: **Equity securities** (common stock, preferred stock, ADRs, equity-linked),
     **Debt securities** (bonds, notes, debentures), **Convertible securities** (convertible
     notes, mandatory convertibles), **Warrants / rights**, **Combination** (units),
     **Asset-backed or structured finance securities**, Other/hybrid
   - _Why this matters_: Equity and debt have different category rules, different compliance
     periods, and different additional conditions (hedging restriction applies to equity only).

3. **SUSMI status (for equity offerings)**:
   - Options: **No SUSMI** (US trading < 20% of total AND US markets not the single largest),
     **SUSMI exists** (US markets single largest OR ≥20% US trading + <55% in any single
     foreign market), **Not yet determined** (provide trading data for analysis),
     **Debt offering** (SUSMI test differs; see debt-specific analysis)
   - _Why this matters_: SUSMI determines whether a FPI can use Category 1 (no SUSMI) or
     must use Category 2 or 3.

4. **Offering structure and concurrent domestic offering**:
   - Options: **Pure offshore Reg S only**, **Concurrent Rule 144A placement** (institutional
     resale exemption), **Concurrent Reg D offering** (private placement), **Follow-on to
     registered offering**, **Concurrent registered offering** (simultaneous S-1/F-1/S-3),
     Other
   - _Why this matters_: Concurrent domestic offerings require integration analysis under
     Rule 152 / Release 33-10736 to ensure the offshore and domestic tranches are properly
     segregated.

5. **Review type**:
   - Options: **Full compliance review** (all conditions, all domains), **Category
     determination only**, **Resale / secondary market analysis**, **Distribution compliance
     period tracking**, **Integration analysis only**, **Documentation review** (legends,
     subscription agreements)
   - _Default for batch run_: Full compliance review.

State all assumptions explicitly before proceeding.

---

### Step 3: Load Legal Authority

Use **legalcode-mcp** to gather current Regulation S authority relevant to the review.

**Research targets:**

1. Current text of 17 CFR §§ 230.901–230.905 (most recent codification)
2. SEC Release No. 33-10736 (Nov. 2020) integration framework modernization — key changes
3. Any recent SEC no-action letters or staff interpretations on directed selling efforts,
   US person definition, or SUSMI calculations in the past 24 months
4. Recent SEC enforcement actions involving Reg S violations in the past 36 months
5. TEFRA C/D guidance if debt offering is involved
6. DTC / DTCC procedural requirements for restricted/unrestricted designation if relevant

**Save results to** `/tmp/reg-s-authority.md` with structure:

```markdown
# Regulation S Legal Authority Reference

## Date: [date]

## Offering: [issuer / security type / structure]

### Current Rule Text Summary

- Rule 901: [territorial principle]
- Rule 902: [key definitions — capture US person, offshore transaction, directed selling efforts, SUSMI, distribution compliance period]
- Rule 903: [issuer safe harbor — Category 1/2/3 conditions]
- Rule 904: [reseller safe harbor conditions]
- Rule 905: [restricted securities / Rule 144 tacking]

### Integration Framework (Rule 152 / Release 33-10736)

- Key changes from 2020: [principles-based approach]
- Application to concurrent 144A / Reg D offerings

### Recent No-Action Letters / Staff Guidance

- [Letter, date, issuer/requestor, key guidance]

### Recent Enforcement Actions

- [Action, date, violation type, outcome]

### TEFRA / Eurobond Guidance (if debt)

- TEFRA D restricted period alignment with Category 2 40-day period
```

**If legalcode-mcp is not connected:**

- Mark every statutory and case law reference with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — manual verification required"`
- Proceed using the rule text and guidance embedded in this skill

---

### Step 4: Determine Issuer Category

Apply the category determination framework to classify the offering into Category 1, 2, or 3.

**⟁ CLARIFY** — For borderline category determinations (particularly SUSMI analysis), ask:

- If SUSMI data is unavailable: "SUSMI status cannot be determined without trading data. Do
  you want to (a) proceed assuming SUSMI exists (conservative — triggers Category 2 or 3),
  (b) provide trading data for SUSMI calculation, or (c) assume no SUSMI (higher risk if
  assumption is wrong)?"
- If issuer recently lost or may lose FPI status: "Has the issuer conducted its annual FPI
  qualification determination? Loss of FPI status moves equity from Category 1/2 to
  Category 3."

Use the **Category Determination Matrix** in the Analysis Framework section below.

---

### Step 5: Apply Category-Specific Conditions

For each applicable category, verify compliance with all required conditions:

1. **Universal conditions** (apply to all categories): offshore transaction + no directed
   selling efforts. Verify both independently.

2. **Category-specific additional conditions**: Apply the conditions from the applicable
   Category in the Analysis Framework. For Category 2, check offering restriction legend
   and 40-day distribution compliance period. For Category 3, check purchaser certification,
   hedging restriction, ADR prohibition, transfer legend, and issuer refusal-to-register
   obligation.

3. **Directed selling efforts audit**: For every US-facing activity identified, apply the
   directed selling efforts analysis from the Analysis Framework.

**⟁ CLARIFY** — For borderline directed selling efforts questions (e.g., road shows with
possible US investor participation, research published by affiliates, internet-accessible
offering materials), ask:

- "Road show materials reference [US investors / a US city]. Were any road show presentations
  made to investors in the United States or to US persons? If so, a directed selling effort
  likely exists unless a safe harbor applies."
- "Offering materials are accessible via a public URL without geoblocking. Has any effort
  been made to restrict US-person access? Unrestricted internet access to offering materials
  creates directed selling effort risk."

---

### Step 6: Analyze Distribution Compliance Period

Determine the applicable distribution compliance period and verify all in-period conditions:

1. **Period length**: Apply the period length from the Category Determination Matrix.
2. **Clock start**: Identify the start date — the **later** of: (a) closing date of the
   offering; (b) date on which the securities were first offered to persons other than
   distributors (commencement of offering).
3. **In-period restrictions**: For Category 2 and 3 offerings, verify that all resales
   during the period comply with Reg S, registration, or another exemption.
4. **Distributor pass-through notice**: For Category 2 and 3, verify that distributor-to-
   distributor transfers during the period were accompanied by the required pass-through notice.
5. **Period expiration**: Calculate the expiration date and note any events that could
   restart or extend the clock (e.g., unsold allotment return from dealers to the issuer).

**⟁ CLARIFY** — If the offering commenced in tranches or had delayed closing, ask:

- "This offering appears to have closed in multiple tranches / had delayed delivery.
  Please confirm: (a) the date of first offering to non-distributor investors, and
  (b) the final closing date. The distribution compliance period starts from the later of
  these dates."

---

### Step 7: Analyze Resale and Secondary Market

For resale transactions, apply the Rule 904 reseller safe harbor analysis:

1. **Seller identity**: Is the seller an issuer, distributor, or affiliate of either? If yes,
   Rule 904 is unavailable — Rule 903 or registration must apply.
2. **Directed selling efforts**: No directed selling efforts by the reseller or persons acting
   on its behalf.
3. **In-period resale restrictions**: If within the distribution compliance period, verify
   that the buyer is certified as a non-US person or the transaction qualifies as an offshore
   transaction.
4. **Rule 144 interaction**: For Category 3 equity (restricted securities under Rule 905),
   verify the applicable Rule 144 holding period has been met (6 months for reporting issuers,
   1 year for non-reporting issuers) before resale under Rule 144 into the US market.

**⟁ CLARIFY** — For Rule 144 tacking questions, ask:

- "Is the seller seeking to resell into the US market under Rule 144? If so, the Reg S
  distribution compliance period does **not** tack onto the Rule 144 holding period — the
  Rule 144 holding period runs separately and begins only when the securities are paid for.
  [VERIFY]"

---

### Step 8: Analyze Integration with Concurrent Domestic Offering

If a concurrent domestic offering is identified, apply the integration analysis:

1. **Applicable framework**: Apply the principles-based framework from Rule 152 / SEC Release
   No. 33-10736 (Nov. 2020). The old mechanical "30-day bright line" test has been replaced
   by a multi-factor analysis.
2. **Segregation conditions**: For a concurrent Reg S + Reg D offering to avoid integration,
   verify: (a) each offering is made to separate, identified investor groups; (b) the offshore
   component satisfies the two Reg S universal conditions; (c) the domestic component
   independently satisfies its own exemption.
3. **Concurrent 144A + Reg S**: The standard global offering structure (144A for QIBs in
   the US, Reg S for non-US investors) is a well-established, SEC-sanctioned structure.
   Confirm that US tranche buyers qualify as QIBs, that no general solicitation has been
   made to non-QIBs in the US, and that the Reg S tranche buyers are non-US persons with
   appropriate certifications.
4. **Flag integration risk factors**: Any of the following increases integration risk:
   - Same securities offered to US and non-US investors simultaneously without clear
     structural separation
   - US investors purchasing into the "offshore" tranche through nominees or foreign accounts
   - Cross-tranche purchasing by US persons

---

### Step 9: Review Documentation

Assess the offering documentation for Reg S compliance:

1. **Offering memorandum / prospectus**: Check for required restriction legends; verify that
   US person and offering restrictions are clearly stated; verify compliance period disclosure.
2. **Subscription agreement**: Verify presence of all required representations (see
   Documentation Requirements section).
3. **Purchase / underwriting agreement**: Verify distributor representations and undertakings;
   distributor pass-through notification obligation; no-directed-selling-efforts covenant.
4. **Global note / certificate legends**: Verify correct form of transfer restriction legend
   for the applicable category.
5. **Issuer organizational documents**: For Category 3 equity, verify that bylaws, articles,
   or charter (or a separate transfer restriction agreement) require refusal to register
   non-compliant transfers.

**⟁ CLARIFY** — If documentation is incomplete, ask:

- "The subscription agreement does not appear to include the hedging restriction representation
  required for Category 3 equity. Is this a finalized document or a draft? If finalized,
  this is a compliance gap requiring remediation."

---

### Step 10: Quality Verification

Before delivering the analysis, run the Quality Assurance Framework:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every NON-COMPLIANT or CRITICAL finding, run the 3-pass Self-Interrogation.
3. Assign a Confidence Score to each material finding.
4. Verify completeness: confirm all applicable review domains have been addressed.
5. Generate the Glass Box Audit Trail and append it to the output.

---

## Analysis Framework

### Category Determination Matrix

| Issuer Type                            | Security Type                 | SUSMI?       | Category            | Distribution Compliance Period |
| -------------------------------------- | ----------------------------- | ------------ | ------------------- | ------------------------------ |
| Foreign Private Issuer                 | Equity                        | No SUSMI     | **Category 1**      | None                           |
| Foreign Private Issuer                 | Equity                        | SUSMI exists | **Category 2**      | 40 days                        |
| Foreign Private Issuer (reporting)     | Equity                        | SUSMI exists | **Category 2**      | 40 days                        |
| Foreign Private Issuer (non-reporting) | Equity                        | SUSMI exists | **Category 3**      | 1 year                         |
| Foreign Private Issuer                 | Debt                          | Any          | **Category 1 or 2** | None (Cat.1) / 40 days (Cat.2) |
| Domestic Issuer (reporting)            | Equity                        | N/A          | **Category 3**      | 6 months                       |
| Domestic Issuer (non-reporting)        | Equity                        | N/A          | **Category 3**      | 1 year                         |
| Domestic Issuer (reporting)            | Debt                          | N/A          | **Category 2**      | 40 days                        |
| Domestic Issuer (non-reporting)        | Debt                          | N/A          | **Category 3**      | 40 days                        |
| Any Issuer                             | Foreign government securities | N/A          | **Category 1**      | None                           |

**Notes**:

1. "Reporting" means subject to Exchange Act §§ 13 or 15(d) periodic reporting. [VERIFY]
2. FPI debt with no SUSMI qualifies for Category 1; FPI debt of a reporting FPI qualifies
   for Category 2 (40-day period). [VERIFY]
3. Non-reporting FPI with SUSMI falls to Category 3 (1-year period). [VERIFY]
4. Category determination should be made at the **outset** of the offering and re-evaluated
   if material changes occur (e.g., issuer loses FPI status during the offering).

---

### SUSMI Determination Framework

#### SUSMI for Equity Securities (Rule 902(j)(1)) [VERIFY]

SUSMI **exists** if, for the class of equity being offered, over the **shorter of** (a) the
issuer's prior fiscal year or (b) the period since incorporation:

| Condition              | SUSMI Exists If…                                                                                                                       |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| US market ranking      | US exchanges and inter-dealer quotation systems constitute the **single largest market** for the securities (regardless of percentage) |
| Combined US percentage | **20% or more** of all trading occurred in the US **AND** less than 55% occurred in any **single foreign country's** markets           |

SUSMI **does not** exist if neither condition is met — i.e., US trading is below 20%, or
below the single-largest-market threshold, and at least one foreign country has 55%+ trading.

**Practical Calculation**: The issuer or its counsel typically obtains trading data from
Bloomberg, data vendors, or the relevant stock exchange to perform this calculation.

#### SUSMI for Debt Securities (Rule 902(j)(2)) [VERIFY]

SUSMI **exists** for debt if **any one** of the following is true:

- **300 or more U.S. persons** hold the securities of record; OR
- **$1 billion or more** in aggregate principal amount is held by U.S. persons; OR
- **20% or more** of the aggregate principal amount outstanding is held of record by U.S. persons.

---

### Directed Selling Efforts Analysis

#### What Constitutes Directed Selling Efforts (Rule 902(c)) [VERIFY]

"Directed selling efforts" means any activity undertaken **for the purpose of, or that could
reasonably be expected to have the effect of, conditioning the US market** for securities
offered under Regulation S.

| Activity                                                                   | DSE Status           | Notes                                                           |
| -------------------------------------------------------------------------- | -------------------- | --------------------------------------------------------------- |
| Advertisements in US-circulation publications                              | **DSE — PROHIBITED** | Unless publication has <20% US circulation                      |
| Mailing materials to US addresses                                          | **DSE — PROHIBITED** |                                                                 |
| Road shows / presentations in the United States                            | **DSE — PROHIBITED** | Including video conferences primarily directed to US investors  |
| Research reports timed to coincide with offering distributed to US persons | **DSE — PROHIBITED** | Particularly where research departs from prior frequency/timing |
| Tombstone ads in publications with ≥20% US circulation                     | **DSE — PROHIBITED** |                                                                 |
| Bloomberg messages / electronic communications targeting US investors      | **DSE — PROHIBITED** | Where reasonably likely to condition US market                  |
| Unrestricted internet-accessible offering materials                        | **DSE — HIGH RISK**  | Without adequate geoblocking / US person access controls        |
| Social media posts referencing offshore offering                           | **DSE — HIGH RISK**  | If accessible to US persons without restriction                 |

#### Activities That Are NOT Directed Selling Efforts (Safe Harbors) (Rule 902(c)(3)) [VERIFY]

| Safe Harbor                                         | Conditions                                                                                                                                                                                            |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Legally required advertisements**                 | Required by US or foreign law/regulatory body; contain only required information plus Securities Act non-registration disclaimer                                                                      |
| **Contacts with excluded persons**                  | Contact with persons excluded from US person definition (foreign branches of US banks, certain foreign insurers) acting in their capacity as such                                                     |
| **Tombstone in low-US-circulation publication**     | Publication has **<20% US circulation**; ad contains only: issuer name, security amount and title, type of business, price/yield, managing underwriters, purpose of offering                          |
| **Offshore bona fide research reports**             | Published by broker-dealer not participating in distribution; publication is consistent with the firm's prior research practices; not timed to coincide with offering; contains no offering materials |
| **Contacts limited to non-US persons offshore**     | All investor contacts occur outside the US with confirmed non-US persons                                                                                                                              |
| **Internet postings with adequate access controls** | Offshore website not accessible by US persons (genuine geoblocking with US IP exclusion and click-through US person certification); [VERIFY — staff interpretations vary]                             |

---

### Category-Specific Conditions Summary

#### Category 1 — Conditions (Rule 903(b)(1)) [VERIFY]

| Condition                      | Requirement            |
| ------------------------------ | ---------------------- |
| Offshore transaction           | Required (Rule 902(h)) |
| No directed selling efforts    | Required (Rule 902(c)) |
| Distribution compliance period | **None**               |
| Legends required               | No                     |
| Purchaser certification        | No                     |
| Hedging restriction            | No                     |
| ADR deposit restriction        | No                     |

#### Category 2 — Conditions (Rule 903(b)(2)) [VERIFY]

| Condition                            | Requirement                                                                                                                                                                            |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Offshore transaction                 | Required                                                                                                                                                                               |
| No directed selling efforts          | Required                                                                                                                                                                               |
| Distribution compliance period       | **40 days**                                                                                                                                                                            |
| Offering restriction statement       | Required in offering materials — securities not registered under Securities Act; may not be offered/sold to US persons (other than distributors) during distribution compliance period |
| Temporary global note legend         | Required — same restriction statement as above                                                                                                                                         |
| Distributor pass-through notice      | Required — distributor selling to distributor/dealer must send confirmation that purchaser is subject to the same restrictions                                                         |
| Permanent global note / certificates | Legend required only during distribution compliance period; removable after period expires                                                                                             |

#### Category 3 — Conditions (Rule 903(b)(3)) [VERIFY]

| Condition                             | Requirement                                                                                                                                               |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Offshore transaction                  | Required                                                                                                                                                  |
| No directed selling efforts           | Required                                                                                                                                                  |
| Distribution compliance period        | **6 months** (reporting domestic issuer equity) / **1 year** (non-reporting domestic issuer equity) / **40 days** (debt of non-reporting domestic issuer) |
| Purchaser certification               | Required — non-US person certification (or Section 4(a)(2) acquisition certification)                                                                     |
| Resale restriction agreement          | Required — purchaser agrees to resell only under Reg S, registration, or available exemption                                                              |
| **Hedging restriction**               | **Required** — purchaser agrees not to engage in any hedging transaction with respect to the securities unless in compliance with the Securities Act      |
| Transfer restriction legend           | Required on certificates / book-entry notations — prohibits transfer except under Reg S, registration, or available exemption                             |
| Issuer refusal-to-register obligation | Required — issuer must refuse to register any non-compliant transfer (by contract or organizational documents)                                            |
| **ADR deposit prohibition**           | **Required** — no deposit into US depositary receipt programs prior to expiration of distribution compliance period                                       |

---

### Rule 904 Reseller Safe Harbor Analysis

**Availability**: Rule 904 is available to **any person other than the issuer, distributor,
or their affiliates**. Dealers and other intermediaries may also use Rule 904, but with
additional conditions during the distribution compliance period. [VERIFY]

**Conditions for Rule 904** [VERIFY]:

1. **Seller is not the issuer, distributor, or affiliate**: Confirm seller identity. If seller
   is a distributor or affiliate, Rule 904 is unavailable — use Rule 903 or another exemption.

2. **No directed selling efforts in the US**: Same as Rule 903 requirement.

3. **If within the distribution compliance period** (for Category 2 and 3 securities):
   - **Non-distributor / non-dealer resale**: Buyer must certify that it is not a US person
     and is not acquiring for the account of a US person; OR seller must reasonably believe
     buyer is not a US person.
   - **Dealer resale** (if seller is a dealer but not the original distributor): The buyer
     must certify non-US person status, OR the transaction must be in compliance with the
     applicable Category 2 or 3 additional conditions.

4. **Outside the distribution compliance period**: No additional conditions beyond the two
   universal conditions (offshore transaction + no directed selling efforts).

---

### Rule 905 — Restricted Securities and Rule 144 Interaction

**What Rule 905 does** [VERIFY]: Equity securities sold by an issuer or distributor pursuant
to Rule 903 (Category 2 or 3) are deemed **restricted securities** as defined in Rule 144(a)(3).
Equity securities resold pursuant to Rule 904 in reliance on the reseller safe harbor during
the applicable distribution compliance period are **also** restricted securities.

**Effect on Rule 144 resales into the US market**:

- The restricted securities designation means that US-market resales under Rule 144 require
  the Rule 144 holding period (6 months for reporting issuers; 1 year for non-reporting
  issuers, measured from when the securities were paid for).
- **Critical**: The Reg S distribution compliance period does **not** tack onto the Rule 144
  holding period. The Rule 144 holding period runs independently from the date the
  securities are paid for. [VERIFY]
- Resale in the US market before the Rule 144 holding period expires requires registration
  or another exemption (e.g., Section 4(a)(1) non-underwriter resale, Section 4(a)(7) resale
  to QIBs).

**Category 1 equity**: Category 1 equity securities are NOT deemed restricted securities
under Rule 905 — they are freely resalable under Reg S (offshore) and under Rule 144 (US
market) without restriction from the Reg S perspective. [VERIFY]

---

### Debt Securities — Eurobond Mechanics

#### TEFRA Conventions [VERIFY]

**TEFRA C**: Applies to certificated bearer bonds. US persons are prohibited from holding
bearer bonds without an interest certification. HIRE Act 2010 effectively eliminated new US-
issued bearer bonds for tax purposes (FATCA withholding consequences). For post-HIRE Act
offshore bearer bond issuances in Category 2 (rare in current market), TEFRA C certification
requires purchasers to certify non-US person status.

**TEFRA D**: The dominant market convention for Eurobond offerings. Securities are initially
represented by a **temporary global note** (TGN) deposited with Euroclear or Clearstream.
During the **40-day restricted period** (which aligns with the Regulation S Category 2
distribution compliance period), the TGN is exchangeable for a **permanent global note**
(PGN) or definitive certificates only upon certification that the holder is not a US person.
Key mechanics:

- At issuance: temporary global note issued to common depositary (Euroclear/Clearstream)
- Days 1–40: only coupon payments on the TGN (no exchange into PGN / definitive notes)
- Day 40 (or later): upon certification of non-US person status, TGN exchangeable for PGN
- The 40-day TEFRA D restricted period and the 40-day Reg S distribution compliance period
  **run concurrently** for Category 2 debt offerings — one compliance structure serves both.

#### Book-Entry Settlement Systems

For Eurobond offerings, securities settle through **Euroclear** (Brussels) or **Clearstream
Banking** (Luxembourg). The common depositary model means the issuer delivers to a single
custodian; investors hold interests in the global note through their accounts at Euroclear
or Clearstream. This structure supports enforcement of Reg S transfer restrictions:

- During the distribution compliance period, the clearing system enforces the restricted
  period by preventing exchange of TGN into PGN without the certification
- Post-period, the PGN is freely tradeable through the clearing system without restriction

**DTC linkage**: The US market (DTC/DTCC) and the Euroclear/Clearstream systems are linked.
After the distribution compliance period expires, securities can be transferred from the
Euroclear/Clearstream system into DTC for US-market trading — this is a significant flowback
pathway that the distribution compliance period and legend requirements are designed to manage.

---

### FPI Qualification Analysis

#### FPI Definition (Rule 405 / Exchange Act Rule 3b-4) [VERIFY]

An issuer qualifies as a **foreign private issuer** if it meets **both** of the following:

1. It is incorporated or organized under the laws of a foreign country (non-US); **AND**
2. A majority of its outstanding voting securities is not held by US residents, **OR**
   (even if US residents hold a majority) all three of the following are true:
   - A majority of its directors/managers are non-US citizens or residents; AND
   - More than 50% of its assets are located outside the US; AND
   - Its business is principally administered outside the US.

**Annual determination**: FPI status is determined annually, as of the last business day of
the second fiscal quarter. Loss of FPI status takes effect at the beginning of the following
fiscal year.

**Why FPI status matters for Reg S**:

- FPI equity with no SUSMI → Category 1 (no distribution compliance period, fewest conditions)
- FPI equity with SUSMI (reporting FPI) → Category 2 (40-day period)
- FPI equity with SUSMI (non-reporting FPI) → Category 3 (1-year period)
- Domestic issuer equity → always Category 3 (6-month or 1-year period)

**Exchange Act reporting consequences of FPI status**:

- FPIs file Form 20-F (annual report) instead of Form 10-K
- FPIs file Form 6-K (current reports) instead of Form 8-K (on a voluntary/required basis)
- FPIs are exempt from US proxy rules (§ 14(a)) and Regulation FD
- FPIs are exempt from Section 16 reporting until they list on a US exchange

---

### Concurrent Offering Integration Analysis

#### Principles-Based Framework (Rule 152 / Release 33-10736) [VERIFY]

The 2020 integration reform replaced the prior mechanical "30-day rule" (which deemed
offerings made within 30 days of each other to be integrated) with a **principles-based**
multi-factor analysis focused on whether the offerings were made to the **same class of
investors** at the **same time** using the **same medium of communication**.

**Key principles**:

1. A Regulation S offering that satisfies the two universal conditions (offshore transaction +
   no directed selling efforts) **will not be integrated** with a concurrent domestic offering
   that independently satisfies its own exemption. [VERIFY — this is the core principle of
   Release 33-10736 as applied to Reg S]
2. The test focuses on functional segregation: are the offshore and domestic investor bases
   genuinely separate?
3. Sequential offerings (domestic first, then offshore, or offshore first, then domestic)
   with a genuine intervening period carry lower integration risk than simultaneous offerings.

#### Concurrent 144A / Reg S Structure (Standard Global Offering) [VERIFY]

The most common structure for large international offerings:

| Tranche          | Exemption    | Eligible Purchasers                                               | Transfer Restrictions                        |
| ---------------- | ------------ | ----------------------------------------------------------------- | -------------------------------------------- |
| US tranche       | Rule 144A    | QIBs (qualified institutional buyers; ≥$100M in securities owned) | Resale only to QIBs or offshore; 144A legend |
| Offshore tranche | Regulation S | Non-US persons in offshore transactions                           | Distribution compliance period; Reg S legend |

**Documentation**: Dual-legend global notes or certificates — the 144A leg and Reg S leg are
typically represented by separate global notes (or separate accounts within a single global
note), with DTC receiving the 144A global note and Euroclear/Clearstream receiving the
Reg S global note.

**Investor eligibility**: US QIBs purchase into the 144A tranche; offshore (non-US) institutional
investors purchase into the Reg S tranche. Crossover purchases (a non-US QIB purchasing
144A notes) are permissible.

**Post-period fungibility**: After the Reg S distribution compliance period expires, Reg S
notes may be exchanged into 144A notes (if the issuer is Exchange Act-reporting) or traded
freely offshore. This is documented in the indenture or trust deed.

---

### Documentation Requirements

#### Subscription Agreement — Required Representations for Reg S Offerings

| Representation                                | Category 1  | Category 2   | Category 3                 |
| --------------------------------------------- | ----------- | ------------ | -------------------------- |
| Not a US person (Rule 902(k))                 | Recommended | **Required** | **Required**               |
| Offshore transaction (Rule 902(h))            | Recommended | **Required** | **Required**               |
| Not acquiring for benefit of US person        | Recommended | Recommended  | **Required**               |
| Distribution compliance period acknowledgment | N/A         | **Required** | **Required**               |
| Resale restrictions acknowledged              | N/A         | Recommended  | **Required**               |
| **Hedging restriction representation**        | N/A         | N/A          | **Required** (equity only) |
| No ADR deposit during period                  | N/A         | N/A          | **Required** (equity only) |
| Legend acknowledgment                         | N/A         | Recommended  | **Required**               |

#### Form of Category 3 Equity Transfer Restriction Legend (Standard Form) [VERIFY]

The following (or substantially similar) legend is required on Category 3 equity
certificates or book-entry notations:

> THE SECURITIES REPRESENTED HEREBY HAVE NOT BEEN REGISTERED UNDER THE UNITED STATES
> SECURITIES ACT OF 1933, AS AMENDED (THE "SECURITIES ACT"), OR THE SECURITIES LAWS OF
> ANY STATE OR OTHER JURISDICTION. THE SECURITIES MAY NOT BE OFFERED, SOLD, PLEDGED,
> OR OTHERWISE TRANSFERRED EXCEPT (1) IN ACCORDANCE WITH RULE 904 OF REGULATION S UNDER
> THE SECURITIES ACT, (2) PURSUANT TO AN EFFECTIVE REGISTRATION STATEMENT UNDER THE
> SECURITIES ACT, OR (3) PURSUANT TO AN AVAILABLE EXEMPTION FROM THE REGISTRATION
> REQUIREMENTS OF THE SECURITIES ACT, IN EACH CASE IN ACCORDANCE WITH ANY APPLICABLE
> STATE SECURITIES LAWS. HEDGING TRANSACTIONS INVOLVING THESE SECURITIES MAY NOT BE
> CONDUCTED UNLESS IN COMPLIANCE WITH THE SECURITIES ACT.

#### Legend Removal Procedure (Category 3 Equity)

After expiration of the distribution compliance period:

1. Holder submits a written request to issuer's transfer agent (or registrar)
2. Request accompanied by: (a) completed representation letter certifying compliance with
   Reg S; (b) opinion of counsel (if required by issuer) confirming exemption availability
3. Transfer agent re-registers or re-issues securities without the restricted legend
4. In book-entry systems (DTC, Euroclear/Clearstream): the restricted vs. unrestricted
   coding is updated; securities become freely tradeable

---

## Severity Classification

All findings are classified into one of four tiers:

| Classification          | Definition                                                                                                                                                               | Action Required                                                               |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| **CRITICAL DEFICIENCY** | Condition fundamental to Reg S safe harbor compliance is absent or violated; registration requirement may be triggered; SEC enforcement and/or rescission rights at risk | Immediate remediation; cease further distribution; consult securities counsel |
| **NON-COMPLIANT**       | Specific required condition not satisfied; may be remediable but currently deficient                                                                                     | Remediation required before closing or before next resale                     |
| **AT-RISK**             | Condition is technically met but borderline; heightened enforcement scrutiny if reviewed; ambiguous facts                                                                | Counsel review; additional documentation; strengthen fact pattern             |
| **COMPLIANT**           | Condition fully satisfied on available facts                                                                                                                             | No action required; note basis for determination                              |

---

## Prioritization Framework

### Tier 1 — Offering-Stopping Issues (Must Remediate Before Close)

- Missing offshore transaction condition (no evidence of offshore execution)
- Active directed selling efforts in the US without safe harbor (US road shows, US mailings)
- Wrong category applied (e.g., domestic issuer equity treated as Category 1)
- Missing Category 3 equity purchaser certification or hedging restriction
- Missing Category 3 equity issuer refusal-to-register obligation
- Premature US-market resales within distribution compliance period without exemption

### Tier 2 — Material Gaps (Remediate Before First Resale or Closing)

- Incomplete or defective transfer restriction legend
- Missing offering restriction statement in offering materials (Category 2)
- Distributor pass-through notices not sent during distribution compliance period
- Incorrect distribution compliance period start date calculated (clock running issue)
- Missing ADR deposit restriction documentation (Category 3 equity)
- SUSMI determination not documented or outdated

### Tier 3 — Documentation and Process Improvements (Address in Ordinary Course)

- Subscription agreement representations technically present but ambiguous in scope
- Legend removal procedure not documented in transfer restriction agreement
- SUSMI calculation methodology not formally documented
- FPI qualification determination not recorded in annual board minutes / legal opinion
- Integration analysis memo not prepared for concurrent domestic/offshore offering

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                         | Fail Action                         |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every regulatory claim cites a specific rule section (17 CFR §), SEC Release number, or established SEC staff interpretation | Add citation or mark "[UNVERIFIED]" |
| **Format**     | All citations follow a consistent, recognizable format: "17 CFR § 230.XXX" or "Rule XXX(y)(z)"                               | Fix format                          |
| **Currency**   | Every cited rule or release checked for subsequent amendments                                                                | Flag "[CHECK CURRENCY]"             |
| **Domain**     | Analysis stays within US federal securities law; non-US securities laws flagged as out-of-scope                              | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated; "reasonably believes" standards flagged as fact-specific                                      | Add confidence qualifier            |

### Self-Interrogation for CRITICAL DEFICIENCY Items

For any item classified as CRITICAL DEFICIENCY, apply this 3-pass review before delivery:

**Pass 1 — Regulatory Chain Integrity**: Does the finding follow directly from the cited rule
or release? Would the SEC enforcement staff actually characterize this as a Section 5
violation? Has the safe harbor condition been correctly identified as required vs. optional?

**Pass 2 — Completeness**: Have all relevant rules been considered? Is there a safe harbor
or no-action position that might cure the deficiency? Have alternative structures (e.g.,
Section 4(a)(2), Rule 144A) been evaluated as potential fall-backs?

**Pass 3 — Challenge**: What is the strongest argument that this finding is overstated? Under
what circumstances might the offering still qualify for Reg S despite the apparent deficiency?
Would a reasonable offering counsel reach the same conclusion?

### Confidence Scoring

| Level        | Range     | Meaning                                                        | Action                                             |
| ------------ | --------- | -------------------------------------------------------------- | -------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled regulatory requirement; clear rule text                | State with confidence                              |
| **High**     | 0.80–0.94 | Strong authority; minor interpretive questions                 | State with brief caveat                            |
| **Probable** | 0.60–0.79 | Good arguments; SEC staff interpretation available but limited | State with reasoning and contra-indicators         |
| **Possible** | 0.40–0.59 | Genuinely uncertain; fact-specific; no clear staff position    | Flag for securities counsel review with both sides |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative; unsupported by rule text              | Do not assert; flag "[UNCERTAIN]"                  |

---

## Anti-Patterns

The following are the most common errors in Regulation S practice — each has caused SEC
enforcement actions or rescission risk in documented transactions:

1. **Treating Reg S as a catch-all offshore exemption**: Reg S is a safe harbor, not an
   unlimited exemption. Failure to satisfy both universal conditions (offshore transaction +
   no directed selling efforts) means the safe harbor is unavailable, and Section 5
   registration may be required regardless of where the sale nominally occurred.

2. **Relying on purchaser representations alone without diligence**: Buyers' representations
   that they are non-US persons are not sufficient without a factual basis for the seller's
   reasonable belief. Sellers must conduct due diligence proportionate to the risk — reviewing
   addresses, passport details, or account locations for high-risk situations.

3. **Applying wrong category to domestic issuer equity**: US company equity always falls in
   Category 3, regardless of how "offshore" the offering feels. Applying Category 1 or 2
   analysis to a domestic issuer's equity offering is a fundamental error.

4. **Misidentifying FPI status without current-year determination**: FPI status must be
   determined annually (as of the last business day of the second fiscal quarter). Using
   stale FPI determination from a prior year creates category classification risk.

5. **Failing to impose the hedging restriction in Category 3 equity**: The 1998 Reg S
   amendments added the hedging restriction requirement specifically because offshore
   purchasers were using short sales into the US market to effectively transfer risk to
   US persons without registration. Omitting this requirement is a well-known enforcement
   trigger.

6. **Premature exchange of temporary global note before TEFRA D/Reg S period expires**:
   Exchanging a TGN into a PGN or definitive notes before the 40-day period, without proper
   non-US person certification, violates both TEFRA D conventions and Category 2 Reg S
   conditions simultaneously.

7. **Failing to send distributor pass-through notices**: During the Category 2 or 3
   distribution compliance period, distributors selling to other distributors or dealers
   must send the required notice. Omitting this step disrupts the chain of restriction
   enforcement and creates compliance gaps for downstream resellers.

8. **US road show participation that conditions the US market**: Including US-based
   institutional investors in road show presentations — or conducting video conferences
   primarily directed to US investors — is a directed selling effort. Even a single US
   stop on an otherwise offshore road show can taint the entire Reg S safe harbor.

9. **Unrestricted website or electronic distribution of offering materials**: Posting
   offering materials on a publicly accessible website without US-person access controls
   (geoblocking, click-through certifications) creates directed selling effort risk. The
   SEC has historically taken a skeptical view of offshore-only internet offerings without
   demonstrated access restrictions.

10. **Tacking the Reg S distribution compliance period onto Rule 144**: The two periods run
    separately. An investor who completes the Reg S distribution compliance period cannot
    immediately resell into the US market under Rule 144 — the Rule 144 holding period must
    be independently satisfied (starting from when the securities were paid for).

11. **Overlooking ADR deposit prohibition for Category 3 equity**: Depositing Category 3
    equity into a US ADR program before the distribution compliance period expires is
    explicitly prohibited. Transfer agents and DTC custodians may not catch this without
    specific contractual instructions; the prohibition must be explicitly documented in the
    deposit agreement and purchase agreement.

12. **Integration failure with concurrent domestic offering**: Treating the Reg S and
    domestic tranches as independent when the same investors are targeted in both (or when
    the domestic offering uses general solicitation that reaches offshore investors) risks
    destroying the domestic exemption.

13. **Ignoring the "reasonably believes" evidentiary standard**: The offshore transaction
    condition is satisfied if the seller "reasonably believes" the buyer is outside the US.
    Courts and the SEC look at what steps the seller took to form and document that belief.
    A bare contractual representation from the buyer, without more, may be insufficient in
    high-risk fact patterns (e.g., buyer with US addresses, undisclosed US principals).

14. **Using Reg S for transactions where the buyer is economically a US person**: Nominee
    or conduit structures (offshore entity acting as front for US-person beneficial owner)
    do not qualify for Reg S protection. The Rule 902(k) US person definition is broad and
    includes trusts controlled by US persons, estates of US persons, and accounts for
    US-person beneficial owners.

15. **Failing to document the SUSMI determination before pricing**: The SUSMI analysis is
    required to be made before the offering. Post-hoc rationalization of SUSMI status after
    a compliance question arises is weak. Best practice is a formal SUSMI memorandum prepared
    by counsel before pricing with supporting trading data.

16. **Conflating Rule 904 availability with Rule 903 conditions**: A reseller seeking to use
    Rule 904 must independently satisfy the reseller safe harbor conditions — it cannot rely
    on the issuer's Rule 903 compliance. An affiliate of the issuer or a distributor cannot
    use Rule 904; it must use Rule 903.

17. **Treating the Reg S offering as closing the distribution compliance clock for all
    purposes**: The distribution compliance period starts from the **later** of closing or
    commencement of offering. For offerings with delayed closings or multiple-tranche
    structures, calculating the wrong start date shortens the period and risks premature
    resales.

18. **Not updating transfer restriction documentation after issuer loses FPI status**: If
    an issuer loses FPI status after an offshore offering, future offshore offerings shift to
    Category 3. Failing to update template documentation (subscription agreements, legends,
    purchase agreements) to reflect the new category creates systematic compliance errors
    across future issuances.

---

## Writing Standards

Apply these standards before delivering any Reg S analysis:

1. **Precision over brevity**: Regulation S is highly technical. Do not simplify conditions
   at the cost of accuracy. Each condition should be stated with the specificity it requires
   in practice.

2. **Distinguish confirmed from inferred facts**: Separate what the offering documents
   establish from what has been assumed or inferred. Label assumptions explicitly.

3. **Flag the Rule reference, not just the conclusion**: Never state "this violates
   Regulation S" without citing the specific condition under which the violation occurs
   (Rule 902(c), Rule 903(b)(3)(iii), etc.).

4. **Use [VERIFY] consistently**: Any statutory or regulatory citation drawn from memory
   (not verified via legalcode-mcp) must be marked [VERIFY]. This is non-negotiable in a
   domain where amendments and no-action letters change practice regularly.

5. **State what is NOT covered**: The analysis should explicitly note any aspect of the
   offering that has not been reviewed (e.g., non-US securities laws, Exchange Act
   reporting obligations, state Blue Sky laws) so counsel can address those gaps.

6. **Avoid false confidence on fact-specific determinations**: The "reasonably believes"
   standard, SUSMI calculations, and directed selling efforts analysis are intensely
   fact-specific. Qualify conclusions with the facts on which they rest.

---

## External Tool Integration

**With legalcode-mcp connected (preferred)**:

- Search for current text of 17 CFR §§ 230.901–230.905 and verify rule citations
- Search for relevant SEC no-action letters and staff interpretations on directed selling
  efforts, US person definition, and SUSMI methodology
- Search for recent SEC enforcement actions involving Reg S violations
- Verify current version of Rule 152 and Release 33-10736 (Nov. 2020) integration framework
- Save verified authority to `/tmp/reg-s-authority.md` and mark citations as VERIFIED in
  the Glass Box audit trail

**Without legalcode-mcp**:

- Mark all rule text citations with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected — manual verification required"`
- Proceed using the rule summaries embedded in this skill, with explicit uncertainty flags
- Recommend that counsel independently verify all cited conditions against current CFR text

---

## Glass Box Audit Trail

Append the following YAML block to every output:

```yaml
glass_box:
  skill_name: "legalcode-us-reg-s-offering-review"
  mode: "Created from scratch — Legalcode original"
  topic: "Regulation S offshore offering and resale compliance (17 CFR §§ 230.901–230.905)"
  jurisdiction: "United States federal securities law"
  issuer_type: "[FPI reporting / FPI non-reporting / Domestic reporting / Domestic non-reporting]"
  security_type: "[Equity / Debt / Convertible / Other]"
  category_determined: "[Category 1 / Category 2 / Category 3 / Not determined]"
  distribution_compliance_period: "[None / 40 days / 6 months / 1 year] — expires [date or TBD]"
  concurrent_offering: "[None / Rule 144A / Reg D / Registered / Other]"
  legalcode_mcp: "[Connected / Not connected]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  review_scope: "[Full review / Category determination only / Resale analysis / Documentation review]"
  findings_summary:
    critical_deficiency: [number]
    non_compliant: [number]
    at_risk: [number]
    compliant: [number]
  quality_score: "[X]/40"
  completeness: "18/18 elements"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "Non-US securities law implications not analyzed"
    - "State Blue Sky laws not covered"
    - "Exchange Act Section 12(g) registration analysis not included"
    - "Tax consequences (FATCA, TEFRA, withholding) not analyzed"
    - "[Any additional limitations based on scope of review]"
  reviewer: "AI-assisted — requires review by qualified US securities counsel"
```

---

## Output Format Template

```markdown
# Regulation S Compliance Review

## [Issuer Name] — [Security Type and Description]

## Date: [date]

## Prepared by: legalcode-us-reg-s-offering-review

---

## Executive Summary

**Overall Assessment**: [COMPLIANT / AT-RISK / NON-COMPLIANT / CRITICAL DEFICIENCY]
**Category Determination**: [Category 1 / 2 / 3]
**Distribution Compliance Period**: [None / 40 days / 6 months / 1 year] — [Start Date] to [End Date]
**Concurrent Offering**: [None / Rule 144A / Reg D / Other]
**Critical Issues**: [Number]
**Material Issues**: [Number]

---

## Offering Profile

| Element                        | Detail                                                          |
| ------------------------------ | --------------------------------------------------------------- |
| Issuer                         | [Name, type (FPI / domestic), reporting status]                 |
| Security                       | [Type, aggregate principal / share amount, CUSIP/ISIN if known] |
| Category                       | [1 / 2 / 3] with basis                                          |
| SUSMI Status                   | [No SUSMI / SUSMI exists / Not determined]                      |
| Distribution Compliance Period | [Period and dates]                                              |
| Concurrent Offering            | [Description or None]                                           |
| Offering Documents Reviewed    | [List]                                                          |

---

## Condition-by-Condition Analysis

### Condition 1: Offshore Transaction (Rule 902(h))

**Classification**: [COMPLIANT / AT-RISK / NON-COMPLIANT / CRITICAL DEFICIENCY]
**Confidence**: [Level (range)]
**Analysis**: [Finding]
**Basis**: [Rule citation and facts]
**Action**: [Required action or "No action required"]

### Condition 2: No Directed Selling Efforts (Rule 902(c))

**Classification**: [...]
**Confidence**: [...]
**Analysis**: [...]
**Basis**: [...]
**Action**: [...]

### [Category-Specific Conditions]

[For each applicable Category 2 or Category 3 condition — format as above]

---

## Distribution Compliance Period Status

**Period**: [Length]
**Start Date**: [Date and basis — closing date vs. commencement date]
**Expiration Date**: [Date]
**Status**: [In period / Expired / Not yet commenced]
**In-Period Compliance**: [Confirmed / Issues identified — see below]

[List any in-period resale issues]

---

## Concurrent Offering Integration Analysis

[If applicable — address Rule 152 / Release 33-10736 analysis]
[If not applicable — state "No concurrent domestic offering identified"]

---

## Documentation Assessment

| Document                          | Status                    | Issues           |
| --------------------------------- | ------------------------- | ---------------- |
| Offering memorandum               | [Reviewed / Not provided] | [Issues or None] |
| Subscription agreement            | [Reviewed / Not provided] | [Issues or None] |
| Purchase / underwriting agreement | [Reviewed / Not provided] | [Issues or None] |
| Global note / certificate legends | [Reviewed / Not provided] | [Issues or None] |
| Issuer organizational documents   | [Reviewed / Not provided] | [Issues or None] |

---

## Findings Register

| #   | Finding       | Classification                                   | Tier    | Rule Reference | Recommended Action |
| --- | ------------- | ------------------------------------------------ | ------- | -------------- | ------------------ |
| 1   | [Description] | [CRITICAL / NON-COMPLIANT / AT-RISK / COMPLIANT] | [1/2/3] | [17 CFR §...]  | [Action]           |
| ... |               |                                                  |         |                |                    |

---

## Prioritized Action Plan

### Tier 1 — Offering-Stopping (Remediate Before Close)

- [ ] [Action item with responsible party and deadline]

### Tier 2 — Material (Remediate Before First Resale)

- [ ] [Action item]

### Tier 3 — Process Improvements

- [ ] [Action item]

---

## Counsel Notes and Assumptions

[Material assumptions made in the absence of documentation]
[Areas flagged for further review by securities counsel]
[Non-US law matters outside scope of this review]

---

[Glass Box YAML block]
```

---

## Localization Notes

While this skill covers US federal securities law exclusively, Reg S offerings almost always
implicate non-US securities regulation. Flag these for separate analysis:

| Non-US Regime                                     | Triggered When                                        | Reference                                                      |
| ------------------------------------------------- | ----------------------------------------------------- | -------------------------------------------------------------- |
| **EU Prospectus Regulation** (Reg (EU) 2017/1129) | Securities offered or admitted to trading in EU/EEA   | Separate EU prospectus counsel required                        |
| **UK FSMA / UK Prospectus Regulation**            | Securities offered in UK post-Brexit                  | UK FSMA §§ 85, 86 and UK Prospectus Regulation                 |
| **MiFID II / MiFIR**                              | Distributor or dealer acting as investment firm in EU | Marketing restrictions, product governance, target market      |
| **Japan FIEA**                                    | Securities offered to Japanese investors              | Foreign securities registration / private placement rules      |
| **Hong Kong SFO**                                 | Securities offered to Hong Kong investors             | Chapter 571 SFO prospectus / professional investor exemptions  |
| **Singapore SFA**                                 | Securities offered to Singapore investors             | Section 275 / 305 private placement exemptions                 |
| **TEFRA / FATCA**                                 | Bearer bonds or US withholding tax implications       | IRS / Treasury regulations; FATCA intergovernmental agreements |

---

## Provenance

Created by Legalcode (2026-03-22). Legalcode original synthesis. Research conducted via
2-agent parallel research pipeline (structural/legal research + advanced topic research)
using authoritative sources including 17 CFR §§ 230.901–230.905 (current text), SEC
Release Nos. 33-7190 (1995), 33-7505 (1998), and 33-10736 (2020), and practitioner-oriented
analysis of Category 1/2/3 conditions, directed selling efforts framework, TEFRA D/
Eurobond mechanics, and Rule 144 interaction. Intended as a native Legalcode replacement
for any imported Reg S offering skill, providing full 18-element quality standard
compliance.

No prior Legalcode Reg S skill existed; this is a Mode A (Create New Skill) creation.
