---
name: legalcode-us-ftc-advertising-compliance
description: Assess FTC advertising compliance for US advertisers — covering FTC Act Section 5 deceptive
  and unfair practices, advertising substantiation doctrine (prior substantiation, competent and reliable
  scientific evidence), FTC Endorsement and Testimonial Guides (16 CFR Part 255, 2023 amendments), material
  connection disclosures, influencer and social media requirements, clear and conspicuous disclosure standards,
  Made in USA claims (16 CFR Part 323, 2021 rule), FTC Green Guides environmental marketing (16 CFR Part
  260), native advertising and deceptively formatted advertisements, negative option and subscription
  marketing (ROSCA, 2024 Negative Option Marketing Rule, click-to-cancel requirements), consumer reviews
  and testimonials (16 CFR Part 465, 2024 fake reviews rule), children's advertising (CARU, COPPA implications),
  and civil penalty exposure analysis.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Assess FTC advertising compliance for US advertisers — covering FTC Act Section 5 deceptive and unfair practices, advertising substantiation doctrine (prior substantiation, competent and reliable scientific evidence), FTC Endorsement and Testimonial Guides (16 CFR Part 255, 2023 amendments), material connection disclosures, influencer and social media requirements, clear and conspicuous disclosure standards, Made in USA claims (16 CFR Part 323, 2021 rule), FTC Green Guides environmental marketing (16 CFR Part 260), native advertising and deceptively formatted advertisements, negative option and subscription marketing (ROSCA, 2024 Negative Option Marketing Rule, click-to-cancel requirements), consumer reviews and testimonials (16 CFR Part 465, 2024 fake reviews rule), children's advertising (CARU, COPPA implications), and civil penalty exposure analysis. Use when reviewing advertising campaigns, influencer agreements, product marketing claims, green/sustainability messaging, subscription offers, endorsement programs, or when assessing FTC enforcement risk. Covers consent order compliance, prior FTC history, and FTC/state AG coordination risks.


# Legalcode FTC Advertising Compliance Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted FTC advertising compliance
> analysis. It does **not** constitute legal advice. FTC enforcement is highly fact-specific
> and the FTC has broad prosecutorial discretion — no AI-assisted analysis substitutes for
> qualified FTC/advertising law counsel licensed in the relevant jurisdiction. All outputs
> must be reviewed by a qualified attorney before use. Statutory and regulatory references
> cited from memory carry hallucination risk — verify against current FTC.gov guidance,
> the Federal Register, and authoritative legal databases before relying on them. Laws and
> FTC rulemaking change frequently; FTC enforcement positions may shift through policy
> statements, enforcement actions, and rulemakings.

---

## Purpose and Scope

This skill assesses advertising materials, practices, and compliance programs against
FTC advertising law requirements. It identifies violations and risk areas, classifies
their severity, generates actionable remediation steps, and produces a confidence-scored,
auditable compliance analysis.

**Covers:**

- FTC Act Section 5 deceptive and unfair practice analysis
- Advertising substantiation requirements by claim type
- Endorsement and testimonial compliance (2023 Guides)
- Material connection and influencer disclosure requirements
- Made in USA and origin claim compliance (2021 Rule)
- Environmental marketing claims (Green Guides)
- Native advertising and deceptively formatted content
- Negative option, subscription, and free trial compliance
- Consumer review and fake review prohibitions
- Children's advertising standards (CARU/COPPA)
- Civil penalty exposure analysis for consent order holders
- FTC compliance program design assessment

**Does not:**

- Constitute FTC staff opinion, advisory opinion, or legal advice
- Cover FDA drug/device advertising requirements (separate regulatory regime)
- Provide comprehensive state consumer protection law analysis (state UDAP statutes vary)
- Assess NAD/NARB self-regulatory compliance as a substitute for FTC analysis
- Replace review by qualified advertising law or FTC counsel

---

## Jurisdiction and Governing Law

**Primary jurisdiction**: United States federal law. The FTC Act applies to commercial
practices "in or affecting commerce" — it has broad reach over US-based advertisers
and foreign advertisers reaching US consumers.

**Core statutory authorities:**

- **15 U.S.C. § 45** — FTC Act Section 5: unfair or deceptive acts or practices [VERIFY current text for any recent amendments]
- **15 U.S.C. § 45(n)** — Unfairness standard (three-part test) [VERIFY]
- **15 U.S.C. § 45(m)** — Civil penalty authority: up to approximately $51,744 per violation [VERIFY current inflation-adjusted amount via FTC.gov]
- **15 U.S.C. § 45a** — Made in USA labels [VERIFY]
- **15 U.S.C. § 57a** — FTC rulemaking authority; rule violations = civil penalties [VERIFY]
- **15 U.S.C. §§ 8401–8403** — ROSCA (Restore Online Shoppers' Confidence Act) [VERIFY]
- **15 U.S.C. §§ 6501–6508** — COPPA (Children's Online Privacy Protection Act) [VERIFY]
- **15 U.S.C. § 2302** — Magnuson-Moss Warranty Act [VERIFY]

**Core regulatory authorities:**

- **16 CFR Part 255** — Guides for Use of Endorsements and Testimonials (revised 2023) [VERIFY effective date: August 22, 2023]
- **16 CFR Part 260** — Green Guides: environmental marketing claims (current: 2012; FTC review ongoing) [VERIFY current version]
- **16 CFR Part 323** — Made in USA Labeling Rule (effective August 13, 2021) [VERIFY]
- **16 CFR Part 465** — Rule on Use of Consumer Reviews and Testimonials (effective August 22, 2024) [VERIFY]
- **16 CFR Part 425** — Negative Option Marketing Rule (revised 2024; provisions phased in) [VERIFY exact effective dates]
- **16 CFR Part 310** — Telemarketing Sales Rule (negative option in telemarketing context) [VERIFY]
- **16 CFR Part 233** — Guides Against Deceptive Pricing [VERIFY]

**FTC policy statements (non-binding guidance):**

- FTC Policy Statement on Deception (1983) — three-part deceptiveness test
- FTC Policy Statement on Unfairness (1980)
- FTC Policy Statement on Advertising Substantiation (_Pfizer, Inc._, 81 F.T.C. 23 (1972))
- FTC Enforcement Policy Statement on Deceptively Formatted Advertisements (December 2015)
- FTC Native Advertising Guide for Businesses (December 2015)
- FTC Disclosures 101 for Social Media Influencers (2019)

**Note on FTC policy statement currency**: The FTC rescinded several longstanding policy
statements in 2022 (including the 1980 Unfairness Policy Statement and the 1983 Deception
Policy Statement in their role as limiting FTC enforcement authority) and has reaffirmed
its broad Section 5 enforcement posture. [VERIFY: confirm current FTC interpretation of
its policy statement framework; this area is actively evolving.]

**State law intersection**: FTC Act does not preempt state UDAP statutes. California
(B&P Code §§ 17200, 17500, Civil Code § 1750 CLRA), New York (General Business Law
§§ 349, 350), and other states maintain independent enforcement authority. State AGs may
bring parens patriae suits under 15 U.S.C. § 45b; must notify FTC before filing. This
skill focuses on federal FTC analysis; flag significant state law exposure separately.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- The advertiser's specific circumstances create distinct compliance obligations
- Risk classification depends on context not provided
- Enforcement exposure depends on prior FTC history or consent order status

Use the **⟁ CLARIFY** pattern (structured options + `*Why this matters*`) at every marked
point. If the user has already provided the information, skip the question and proceed.
State all assumptions explicitly when proceeding without complete context.

---

## Workflow

### Step 1: Accept Input

Accept advertising materials and context in any of these formats:

- **Campaign materials**: Ad creative, copy, scripts, social media content, email campaigns
- **URL**: Link to a live advertisement, landing page, product page, or influencer post
- **Pasted text**: Ad copy, endorsement scripts, marketing claims pasted directly
- **Document**: Marketing plan, media brief, influencer agreement, substantiation file
- **Compliance program description**: Internal policies, procedures, training materials

If no materials are provided, prompt the user to supply them or describe the advertising
practice to be assessed.

---

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the assessment, ask the user these questions. Present
structured options where possible:

1. **Advertiser type and industry**:
   - Options: Consumer packaged goods (food/beverage), Dietary supplements/nutraceuticals,
     Health devices/services, Technology/software/apps, Financial products/services,
     Retail/e-commerce, Entertainment/media, Other (specify)
   - _Why this matters_: Dietary supplements and health products face the "competent and
     reliable scientific evidence" standard requiring clinical trials; health claims trigger
     FDA overlap analysis; financial products trigger FTC/CFPB jurisdiction overlap.

2. **Media channels and formats**:
   - Options: Television/radio, Digital display/programmatic, Search/paid search,
     Social media (organic), Influencer/creator program, Native advertising/sponsored
     content, Email marketing, Direct mail, Subscription/negative option sales,
     Children-directed media, All of the above
   - Allow multiple selections.
   - _Why this matters_: Different channels carry different disclosure requirements;
     influencer programs require specific material connection analysis; children's media
     triggers heightened standards.

3. **Prior FTC history**:
   - Options: Active consent order (specify scope), Prior consent order (expired),
     Prior FTC investigation/warning letter, No prior FTC history, Unknown
   - _Why this matters_: Active consent order holders face civil penalty exposure
     (up to ~$51,744 per violation/day) for any covered violations, even ones that would
     otherwise only trigger a cease-and-desist. Prior history affects enforcement risk
     assessment and remediation urgency.

4. **Claim scope**:
   - Options: Express performance claims, Health/efficacy claims (drug-like),
     Comparative advertising claims, Environmental/sustainability claims,
     Origin/Made in USA claims, Pricing claims, General brand/image advertising,
     Mixed (describe)
   - Allow multiple selections.
   - _Why this matters_: Express health claims require the highest substantiation
     standard (clinical trials); environmental claims trigger Green Guides analysis;
     origin claims trigger the Made in USA Labeling Rule.

5. **Endorsement/testimonial use**:
   - Options: Celebrity/talent endorsements, Influencer/creator program,
     Consumer testimonials/reviews, Expert endorsements, Employee social media,
     No endorsements/testimonials
   - Allow multiple selections.
   - _Why this matters_: Each category has specific disclosure and substantiation
     requirements under 16 CFR Part 255 (2023 revision).

6. **Subscription/negative option**:
   - Options: Free trial converting to paid, Recurring subscription product/service,
     Membership/club plan, Negative option feature in any offer, Not applicable
   - _Why this matters_: Triggers ROSCA analysis and 2024 Negative Option Marketing Rule
     compliance assessment including click-to-cancel requirements.

_Default for batch/non-interactive run_: Proceed with general consumer product assumptions,
all media channels, no prior FTC history, all claim types, all endorsement categories,
and subscription marketing applicable. Flag assumptions explicitly in the output.

---

### Step 3: Load Legal Authority via legalcode-mcp

Use **legalcode-mcp** to build a working legal reference for this assessment.

**Research targets:**

1. Current text of 16 CFR Part 255 (Endorsement Guides, 2023 revision)
2. Current text of 16 CFR Part 260 (Green Guides) and any pending update notices
3. Current text of 16 CFR Part 323 (Made in USA Labeling Rule)
4. Current text of 16 CFR Part 465 (Consumer Reviews Rule, 2024)
5. Current effective provisions of 16 CFR Part 425 (Negative Option Marketing Rule)
6. FTC civil penalty inflation adjustments — current per-violation maximum
7. Any active FTC rulemakings on commercial surveillance, endorsements, or junk fees
8. Recent FTC consent orders in the advertiser's industry (past 3 years)

**Save results** to `/tmp/legalcode-ftc-adv-authority.md`. Structure as:

```markdown
# FTC Advertising Legal Authority Reference

## Jurisdiction: US Federal (FTC)

## Date Gathered: [date]

### Current Regulations (verified text or citation to current CFR)

- 16 CFR Part 255: [summary of key provisions + effective date]
- 16 CFR Part 260: [summary + pending update status]
- 16 CFR Part 323: [summary]
- 16 CFR Part 465: [summary + effective date]
- 16 CFR Part 425: [summary + phase-in dates]
- Civil penalty maximum: $[current amount per violation]

### Recent Enforcement Actions (past 3 years, advertiser's industry)

- [Entity, violation type, penalty, year]

### Active Rulemakings

- [Rulemaking name, status, expected timeline]
```

Use this reference file throughout the analysis. Mark all legalcode-mcp-sourced citations
as VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**

- Proceed using the regulatory framework described in this skill
- Mark all regulatory citations [VERIFY] in the output
- Note in the Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Flag that FTC rulemaking is active; advise confirming current rule text at FTC.gov before
  acting on any finding

---

### Step 4: Substantiation Assessment

Assess whether all material advertising claims are substantiated **prior** to dissemination,
as required by the FTC's prior substantiation doctrine (_Pfizer, Inc._, 81 F.T.C. 23 (1972)).

**⟁ CLARIFY** — Before assessing substantiation, ask:

- "What is the specific advertising claim being made? (Exact language matters — 'clinically
  proven' triggers a higher standard than 'may help support.')"
- "What substantiation does the advertiser currently possess? (Lab tests, consumer surveys,
  clinical studies, expert reviews?)"
- If no substantiation has been reviewed: "Should I assess the claims for sufficiency against
  FTC standards, and flag the level of evidence that would be required?"

**4a. Claim Type Identification and Substantiation Standard**

| Claim Type                                  | FTC Substantiation Standard                                                                                       | Common Failure Mode                                                                        |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Health/disease treatment claims**         | Competent and reliable scientific evidence; typically 2 well-designed RCTs                                        | Using "clinically tested" when only a pilot study exists                                   |
| **Dietary supplement efficacy**             | Competent and reliable scientific evidence; typically 2 RCTs [VERIFY current standard from recent consent orders] | Single study with methodological flaws                                                     |
| **Non-health product performance**          | Reasonable basis: reliable testing appropriate for the claim                                                      | No testing conducted; relying on subjective user feedback                                  |
| **Environmental attributes**                | Competent and reliable scientific evidence for the specific attribute                                             | Vague "eco-friendly" without substantiation                                                |
| **Safety claims**                           | Reliable testing by qualified persons                                                                             | No adverse event tracking                                                                  |
| **Comparative advertising claims**          | Valid, methodologically sound head-to-head testing                                                                | Cherry-picked metrics; outdated comparison                                                 |
| **Consumer testimonials / typical results** | Substantiation for the typical consumer result implied                                                            | Featuring exceptional outlier results; "results not typical" disclaimer alone insufficient |
| **Pricing claims ("was/now")**              | Bona fide former price actually charged for a reasonably substantial period                                       | Fictitious reference prices; perpetual "sale" pricing                                      |

**4b. Express vs. Implied Claims Analysis**

- Identify all **express claims** (literal statements) and assess substantiation.
- Identify all **implied claims** (claims a significant minority of reasonable consumers
  would take away from the ad's net impression) and assess whether the advertiser
  possesses substantiation for each.
- Advertisers cannot disclaim implied claims they knowingly create. If the overall
  impression of an ad communicates a health benefit, substantiating only the express
  literal language is insufficient.

**Assessment questions for each claim:**

| Element              | Assessment Question                                            | Green Indicator                                                                          | Common Gap                                           |
| -------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Prior substantiation | Was evidence gathered before the claim was made?               | Written substantiation file predates ad launch                                           | Evidence collected post-complaint                    |
| Evidence quality     | Is evidence from qualified experts using accepted methodology? | Peer-reviewed studies; independent lab; qualified expert                                 | Internal tests only; no methodology disclosure       |
| Evidence scope       | Does evidence match the specific claim made?                   | Study tests the specific product at the specific dose in the specific population claimed | Evidence from different product, dose, or population |
| Claim precision      | Is the claim language matched to evidence precision?           | "May help support" vs. "proven to cure"                                                  | Overclaiming relative to evidence                    |
| Typicality           | Is typical consumer result disclosed when using testimonials?  | Specific typical result stated                                                           | "Results not typical" disclaimer used alone          |

---

### Step 5: Disclosure Practices Assessment

Assess whether all required disclosures are **clear and conspicuous** as required by
FTC Guides and rules. The clear-and-conspicuous standard is defined at 16 CFR § 255.0:
a disclosure is clear and conspicuous when it is "difficult to miss (i.e., easily noticeable)
and easily understandable by ordinary consumers."

**5a. Clear and Conspicuous Elements by Format**

| Format                            | Clear and Conspicuous Requirements                                                                   | Common Failures                                                                               |
| --------------------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Digital/display**               | Disclosure visible before scrolling; adequate size; high contrast; not buried in footer              | Fine print; same color as background; disclosed only in terms of service                      |
| **Social media posts**            | Disclosure at start of caption or overlaid on image; not buried in hashtag string                    | "#ad" among 10 other hashtags; disclosure only in link                                        |
| **Video (pre-roll/broadcast)**    | On-screen text disclosure throughout segment; verbal disclosure; adequate size and duration          | Disclosure flashes briefly; disclosure only at end; audio disclosure faster than main content |
| **Podcasts**                      | Clear verbal disclosure near start of sponsored segment                                              | Disclosure only in show notes; disclosure integrated into jokes/banter obscuring nature       |
| **Search/SEM**                    | Platform "Ad" label sufficient where visible; landing page disclosures                               | Platform label obscured; landing page does not match ad representation                        |
| **Email**                         | Sender identification; commercial nature clear if promotional                                        | CAN-SPAM subject line deception [VERIFY CAN-SPAM 15 U.S.C. § 7704 current requirements]       |
| **Native advertising**            | "Advertisement," "Ad," "Sponsored," or "Sponsored Content" label; placement before engagement        | "Promoted by [Brand]" alone; editorial formatting without disclosure                          |
| **Negative option/subscriptions** | All material terms including price, frequency, and cancellation before billing information collected | Disclosure buried in terms; tiny font on order confirmation page                              |

**5b. Material Terms Disclosure (Negative Option Context)**

When a negative option feature is involved, assess all pre-enrollment disclosures against
the 2024 Negative Option Marketing Rule and ROSCA (15 U.S.C. § 8403):

| Required Disclosure                 | Present? | Clear and Conspicuous? | Notes |
| ----------------------------------- | -------- | ---------------------- | ----- |
| Description of subscription/service |          |                        |       |
| Amount(s) to be charged             |          |                        |       |
| Frequency of charges                |          |                        |       |
| Date(s) charges will be applied     |          |                        |       |
| Deadline to cancel to avoid charges |          |                        |       |
| Cancellation mechanism              |          |                        |       |

**⟁ CLARIFY** — If reviewing a subscription offer:

- "Can consumers cancel online with the same ease as enrollment, or is there a
  different/harder cancellation path?"
- "Are annual subscribers receiving renewal reminders before each charge?"
- "Are there any 'saves' or 'win-back' flows that delay the cancellation process?"

---

### Step 6: Endorsement and Testimonial Program Review

Assess the advertiser's endorsement and testimonial practices against 16 CFR Part 255
(2023 revision) and 16 CFR Part 465 (2024 fake reviews rule).

**⟁ CLARIFY** — Before reviewing endorsement program:

- "Does the advertiser have a written influencer/endorsement policy?"
- "What onboarding, training, or contracting is provided to endorsers?"
- "Are employee social media policies in place that cover disclosure obligations?"

**6a. Material Connection Assessment (16 CFR § 255.5)**

Identify all connections between endorsers and the advertiser. A material connection
exists whenever a "significant minority" of the audience would not understand or expect
the connection and it could affect credibility:

| Connection Type                         | Disclosure Required?                             | Sufficient Disclosure Language                                                                        |
| --------------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| Cash payment                            | Always                                           | "Ad," "Advertisement," "Paid," "Sponsored"                                                            |
| Free products (solicited)               | Always                                           | "Ad," "#ad," "Gifted," "[Brand] sent me this" — [VERIFY FTC position on "#gifted" as sole disclosure] |
| Free products (unsolicited, endorsed)   | Yes, if endorsed                                 | Same as above                                                                                         |
| Discount or sweepstakes entry           | Yes                                              | Disclose nature of incentive                                                                          |
| Business relationship (agency, partner) | Always                                           | Disclosure of commercial relationship                                                                 |
| Employment relationship                 | Always when endorsing employer's products        | "I work for [Brand]" or equivalent                                                                    |
| Family/personal relationship            | Yes, if significant minority would not expect it | Disclosure of relationship                                                                            |
| No relationship                         | No disclosure required                           | N/A                                                                                                   |

**6b. Endorsement Program Controls**

| Control                  | Assessment Question                                                           | Green Indicator                                                       | Common Gap                                       |
| ------------------------ | ----------------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------ |
| Written policy           | Does the advertiser have a written endorsement/influencer policy?             | Policy exists; covers all connection types; updated post-2023         | No policy; outdated policy                       |
| Endorser training        | Are endorsers trained on disclosure requirements?                             | Written training; onboarding acknowledgment                           | Verbal instructions only; no training            |
| Contractual requirements | Do influencer agreements require compliance with FTC rules?                   | Explicit FTC disclosure clause; right to terminate for non-compliance | No FTC clause; only "follow platform rules"      |
| Monitoring               | Does the advertiser monitor endorser posts for compliance?                    | Regular audits; documented corrective actions                         | No monitoring; first review on complaint         |
| Employee program         | Are employees covered by social media disclosure policy?                      | Specific employee policy; training on personal account obligations    | General social media policy only                 |
| Atypical results         | Are consumer testimonial result claims substantiated as typical?              | Typical result data on file; typical result disclosed in ad           | Outlier testimonials without disclosure          |
| Review program           | Does the advertiser solicit reviews? Are paid/incentivized reviews disclosed? | Review program policy; disclosure in incentivized review request      | Paying for reviews expressing specific sentiment |

**6c. Virtual Influencers and AI-Generated Content**

If the advertiser uses AI-generated personas or virtual influencers:

- Assess whether their artificial nature is disclosed when they appear to be ordinary
  consumers or independent reviewers [VERIFY 16 CFR § 255.x specific provision reference]
- Assess AI-generated fake reviews against 16 CFR § 465.2 prohibitions

**6d. Expert Endorsement Verification (16 CFR § 255.3)**

| Requirement         | Assessment Question                                                         |
| ------------------- | --------------------------------------------------------------------------- |
| Expertise match     | Do the endorser's qualifications match the expertise claimed in the ad?     |
| Adequate evaluation | Did the expert conduct an evaluation sufficient for their stated expertise? |
| Current opinion     | Does the expert still hold the opinion as advertised?                       |
| Comparative claims  | If comparative, did the expert actually compare competing products?         |

---

### Step 7: Environmental and Origin Claims Assessment

Assess green/environmental marketing claims against FTC Green Guides (16 CFR Part 260)
and origin/Made in USA claims against the Made in USA Labeling Rule (16 CFR Part 323).

**⟁ CLARIFY** — If environmental claims are present:

- "What specific environmental claims does the advertising make? (List each distinct claim.)"
- "Does the advertiser have competent and reliable scientific evidence for each specific
  environmental attribute claimed?"
- "Note: The FTC Green Guides are currently under review for potential update, particularly
  regarding 'sustainable,' 'net zero,' and carbon claims. Should I flag this pending-update
  risk in the analysis?"

**7a. Green Guides Claim Assessment (16 CFR Part 260)**

| Claim Type                                                                 | FTC Standard                                                                                                                                          | Assessment                                                                           | Common Violation                                                                        |
| -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| **General environmental benefit** ("eco-friendly," "green," "sustainable") | Always deceptive if unqualified — implies no negative environmental impacts                                                                           | Flag for qualification to specific, substantiated attributes                         | Using "eco-friendly" without qualification                                              |
| **Recyclable** (§ 260.12)                                                  | Unqualified only when recycling available to substantial majority (≥60%) of consumers where sold                                                      | Assess geographic availability of recycling infrastructure                           | Claiming recyclable when recycling not available to 60%+ of consumers                   |
| **Recycled content** (§ 260.13)                                            | Must state percentage; distinguish pre-consumer vs. post-consumer if claimed                                                                          | Verify percentage and sourcing documentation                                         | Routine manufacturing scrap claimed as recycled                                         |
| **Compostable** (§ 260.7)                                                  | Must break down into usable compost in timely manner; qualify if industrial composting required                                                       | Assess composting infrastructure availability                                        | Claiming compostable for products requiring industrial composting without qualification |
| **Biodegradable/degradable** (§ 260.8)                                     | Must decompose in reasonably short time after customary disposal                                                                                      | Assess disposal pathway — unqualified claim deceptive for landfill-destined products | Claiming biodegradable for landfill products                                            |
| **Carbon offset** (§ 260.5)                                                | Competent and reliable scientific and accounting methods; disclose if reductions are projected 2+ years out; cannot claim legally required reductions | Assess offset quality and timing disclosure                                          | Selling offsets for required emission reductions; not disclosing future-dated offsets   |
| **Renewable energy** (§ 260.15)                                            | Cannot claim if fossil fuels used in significant processes unless matched with RECs; cannot claim if RECs sold to others                              | Verify REC ownership and process energy mix                                          | Selling RECs to others then claiming renewable energy                                   |
| **Certifications/seals** (§ 260.6)                                         | Third-party certification does not eliminate advertiser's substantiation obligation; must disclose basis                                              | Assess underlying certification standards                                            | Using eco-seal when certification standards are inadequate or unknown                   |
| **"Net zero" / "Climate neutral"**                                         | Currently no specific Green Guides provision; FTC review pending; treat as general environmental claim                                                | Flag as high risk; require specific substantiation                                   | Making "net zero" claims without verified, methodologically sound carbon accounting     |

**7b. Made in USA Assessment (16 CFR Part 323)**

**⟁ CLARIFY** — For any Made in USA claim:

- "Where is the final assembly or processing performed?"
- "What percentage (by value or content) of the product's components and ingredients
  are sourced and manufactured in the US?"
- "Is the claim qualified (e.g., 'assembled in USA from imported parts') or unqualified
  (e.g., 'Made in USA')?"

| Requirement Element            | Unqualified MUSA Claim Standard                        | Assessment Question                                         | Violation Pattern                             |
| ------------------------------ | ------------------------------------------------------ | ----------------------------------------------------------- | --------------------------------------------- |
| **Final assembly**             | Must occur in the US                                   | Where is final assembly?                                    | Final assembly outside US                     |
| **Significant processing**     | All significant processing in the US                   | Where are significant manufacturing steps performed?        | Key processing steps offshore                 |
| **Components and ingredients** | All or virtually all sourced and made in the US        | What percentage (by cost/value) of components are imported? | Significant imported components               |
| **Qualified claim accuracy**   | Qualification must be clear, conspicuous, and accurate | Is the specific qualification stated accurate?              | Overstating domestic content in qualification |

**Critical**: For products assembled in the US from mostly imported components, an
unqualified "Made in USA" claim violates 16 CFR § 323.2. Violations treated as violations
under 15 U.S.C. § 57a — civil penalty exposure.

---

### Step 8: Native Advertising and Deceptive Format Analysis

Assess advertising formats for deceptive presentation under FTC's Enforcement Policy
Statement on Deceptively Formatted Advertisements (December 2015) and native advertising
guidance.

**Assessment questions:**

| Format Element                      | Assessment Question                                                                 | Green Indicator                                                             | Common Violation                                              |
| ----------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **Commercial nature**               | Would a reasonable consumer, before engaging, recognize the content as advertising? | Clear placement context; prominent disclosure                               | Editorial-format ad without disclosure                        |
| **Disclosure placement**            | Does disclosure appear before consumer engages with content?                        | Disclosure at top; visible before scroll/click                              | Disclosure at bottom; visible only after engagement           |
| **Disclosure terminology**          | Does the disclosure language clearly communicate commercial nature?                 | "Advertisement," "Ad," "Sponsored," "Sponsored Content," "Paid Advertising" | "Promoted by [Brand]"; "Featured"                             |
| **Format matching**                 | Does the ad format mimic editorial/news content in a misleading way?                | Clear visual distinction from editorial; publisher policy                   | Uses identical font, layout, and byline format as editorial   |
| **Search advertising**              | Are paid search results identified as ads before interaction?                       | Platform "Ad" label clearly visible                                         | Label obscured by design; landing page contradicts ad         |
| **In-feed advertising**             | Are native feed placements identified before interaction?                           | "Sponsored" label prominent and above content                               | Label absent; label appears only on hover                     |
| **Advertorials/sponsored articles** | Published sponsored content — is commercial nature disclosed?                       | "Sponsored Content" or "Advertisement" in consistent, prominent placement   | "Written by [Brand]" without indicating it's paid advertising |

---

### Step 9: Children's Advertising Assessment

Assess any advertising directed to children against CARU guidelines and COPPA.

**⟁ CLARIFY** — "Is any advertising directed to children under 13? Under 16?"

- _Why this matters_: Child-directed advertising is held to a higher standard —
  practices not questioned for adult audiences may be deceptive when directed to children
  (16 CFR § 255.6 note; CARU guidelines). COPPA (15 U.S.C. §§ 6501–6508) restricts
  data collection from children under 13.

**Assessment by claim type (child-directed advertising):**

| Issue Area                             | Standard                                                                                                 | Assessment Question                                                                    |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Clearly distinguishing advertising** | Advertising must be clearly distinct from programming/content                                            | Is ad content visually and clearly separated from non-advertising content?             |
| **Product presentation**               | Products must be clearly represented; size/ability must be accurately depicted                           | Are product capabilities and size accurately shown?                                    |
| **Celebrity/character endorsements**   | Extra scrutiny — children may not distinguish celebrity from character; cannot exploit emotional appeals | Does the endorsement exploit children's developmental vulnerabilities?                 |
| **Disclaimers and disclosures**        | Must be understandable by the age group targeted                                                         | Is disclosure language age-appropriate and in child-understandable terms?              |
| **COPPA data collection**              | Written parental consent required before collecting personal information from children under 13          | Does any advertising involve online data collection from children?                     |
| **Influencer/social media**            | Material connections particularly harmful when directed to children who cannot assess commercial intent  | Are influencer posts directed to children? Are they clearly identified as advertising? |

---

### Step 10: Enforcement Exposure Analysis

Quantify and prioritize enforcement risk based on findings from Steps 4–9.

**10a. Civil Penalty Exposure Assessment**

| Scenario                                                                                      | Penalty Framework                                                                                                                              | Exposure Estimate                                  |
| --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **Active consent order violation**                                                            | Up to ~$51,744 per violation per day [VERIFY current amount]                                                                                   | HIGH: Calculate days × violations × maximum        |
| **Trade regulation rule violation** (16 CFR Part 323, 465, 425, 255 as unfair/deceptive acts) | Up to ~$51,744 per violation [VERIFY]                                                                                                          | MEDIUM-HIGH: Depends on volume of transactions/ads |
| **First-time Section 5 violation (no consent order)**                                         | Cease and desist; no direct civil penalty [VERIFY post-AMG Capital Management v. FTC, 593 U.S. 327 (2021) status of equitable monetary relief] | LOW-MEDIUM: Reputational; future consent order     |
| **Subsequent Section 5 violation (prior consent order)**                                      | Civil penalty exposure triggered                                                                                                               | HIGH: Prior order is constructive notice           |

**Note on monetary remedies**: In _AMG Capital Management v. FTC_ (2021), the Supreme
Court held the FTC could not obtain equitable monetary relief under Section 13(b) [VERIFY
current status of legislative proposals to restore FTC monetary authority absent a consent
order violation — check whether Congress has enacted remedial legislation].

**10b. Key Penalty Factors (FTC Decision Matrix)**

FTC considers these factors in penalty determination:

1. **Prior knowledge** — Did the advertiser know the practice was unlawful?
2. **Severity** — How significant is consumer harm?
3. **Duration** — How long has the practice continued?
4. **Size of respondent** — Revenue and resources of the company
5. **Cooperation** — Cooperation with FTC investigation
6. **Remediation** — Voluntary corrective action taken

**10c. State AG Parallel Exposure**

Flag any claims likely to attract state AG enforcement:

- Health/weight loss claims (multi-state AG task forces)
- Made in USA violations (multi-state coordination common)
- Subscription dark patterns (state AG priority enforcement area)
- Children's data and advertising (California, New York active)

---

### Step 11: Quality Verification

Before delivering the assessment, run all quality checks defined below.

1. Run the **5 Citation Quality Gates** silently. Revise any failures before delivery.
2. For every **CRITICAL DEFICIENCY** finding, run the **3-Pass Self-Interrogation**.
   Revise the classification if any pass undermines it.
3. Assign **Confidence Scores** to each domain finding.
4. Complete the **Glass Box Audit Trail** template.

---

## Severity Classification System

Use this four-tier system for all findings:

| Tier | Classification          | Meaning                                                                                                                                                                                  | Required Action                                                                                                                | Timeframe                   |
| ---- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------- |
| 🔴   | **CRITICAL DEFICIENCY** | Active advertising practice that constitutes a likely FTC Act Section 5 violation or trade regulation rule violation; material deception of consumers; or active consent order violation | Pull or modify advertising immediately; engage FTC/advertising counsel; implement litigation hold if investigation is possible | **IMMEDIATE (24-48 hours)** |
| 🟠   | **NON-COMPLIANT**       | Clear gap in legal requirement or FTC standard; elevated enforcement risk; likely requires advertising modification or program change                                                    | Escalate to CLO/senior counsel; remediate within 30 days; do not expand program until remediated                               | **30 DAYS**                 |
| 🟡   | **PARTIAL**             | Some compliance present; material gaps in documentation, training, or practice; FTC would likely require improvement                                                                     | Implement remediation plan; document corrective actions; complete within 90 days                                               | **90 DAYS**                 |
| 🟢   | **COMPLIANT**           | Meets applicable FTC standard; no material gaps identified                                                                                                                               | Document current compliance; maintain controls; monitor for regulatory updates                                                 | **Ongoing monitoring**      |

**Per-finding output block:**

```
Domain: [Substantiation | Disclosure | Endorsement | Native Advertising | Environmental | Origin | Negative Option | Consumer Reviews | Children's Advertising | Compliance Program]
Classification: 🔴 CRITICAL DEFICIENCY | 🟠 NON-COMPLIANT | 🟡 PARTIAL | 🟢 COMPLIANT
Finding: [One-sentence description of the specific finding]
FTC Authority: [15 U.S.C. § 45 | 16 CFR § 255.x | 16 CFR § 260.x | 16 CFR § 323.x | 16 CFR § 465.x | Other]
Risk: [Specific FTC enforcement theory and civil penalty exposure, if any]
Evidence: [What specific practice, document, or gap supports this finding]
Remediation: [Specific, actionable corrective steps]
Owner: [Marketing | Legal/Compliance | Product | C-Suite]
Deadline: [IMMEDIATE (24-48h) | 30 DAYS | 90 DAYS | 180 DAYS | Ongoing]
Escalation: [Legal/Compliance | CLO | General Counsel | Board | Outside FTC Counsel]
```

---

## Prioritization Framework

**Tier 1 — Immediate (active risk in market):**

- Active advertising without required substantiation for health/efficacy claims
- Active deceptive representations constituting likely Section 5 violations
- Active consent order violations
- Active fake reviews or review suppression programs (16 CFR Part 465)
- Active negative option features without required pre-enrollment disclosures or cancellation mechanisms

**Tier 2 — Near-Term (program gaps creating ongoing risk):**

- Missing or inadequate endorsement/influencer disclosure policies
- Made in USA claims on products not meeting "all or virtually all" standard
- Unqualified environmental claims without substantiation
- Native advertising without required commercial identification
- Missing annual renewal reminders for subscription programs
- Absent or outdated employee social media disclosure training

**Tier 3 — Background (program maturity improvements):**

- Updating influencer contract templates to include 2023 Endorsement Guide requirements
- Refreshing substantiation documentation practices and file organization
- Monitoring program for endorser disclosure compliance
- Green Guides training update in advance of anticipated FTC guide revision
- Internal advertising review checklist development
- Cross-functional alignment (Marketing + Legal) on claim clearance process

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                                        | Fail Action                                                                                            |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Source**     | Every legal claim cites a specific FTC Act provision, CFR section, FTC policy statement, or established FTC enforcement principle                           | Add citation or mark `[UNVERIFIED — counsel to confirm]`                                               |
| **Format**     | All citations follow a consistent US federal format (e.g., 15 U.S.C. § 45, 16 CFR § 255.5, _AMG Capital_, 593 U.S. 327)                                     | Fix format                                                                                             |
| **Currency**   | Every cited provision checked for amendments or supersession; FTC rules and guidance updated frequently                                                     | Flag `[CHECK CURRENCY — FTC rulemaking active in this area]` for any provision where update is pending |
| **Domain**     | Analysis stays within FTC advertising law scope; do not import FDA drug/device requirements or state UDAP law as FTC requirements without clear delineation | Remove jurisdictional bleed or flag separately                                                         |
| **Confidence** | Uncertainty explicitly stated, not hidden; never assert FTC enforcement outcome as definitive                                                               | Add confidence qualifier; note that FTC has prosecutorial discretion                                   |

**FTC-specific currency warning**: FTC policy statements on endorsements and testimonials
were significantly revised in 2023; the Consumer Reviews rule is new as of 2024; the
Negative Option Marketing Rule has phase-in provisions as of 2024-2025. Verify current
CFR text before relying on any pre-2024 authority in these areas.

### Self-Interrogation for CRITICAL DEFICIENCY Items

For any finding classified 🔴 CRITICAL DEFICIENCY, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the deception/unfairness finding follow logically
from the cited FTC authority? Would the FTC's three-part deceptiveness test (_materiality_,
_likely to mislead_, _reasonable consumer_) actually be satisfied for this claim? Is there
a consumer injury pathway?

**Pass 2 — Completeness**: Have all relevant FTC Act provisions, rules, and policy
statements been considered? Is there an FTC safe harbor, advisory opinion, or published
guidance that covers this practice? Are there any regulatory dimensions not yet addressed
(e.g., FDA jurisdiction overlap on health claims)?

**Pass 3 — Challenge**: What is the strongest argument that this practice is NOT a
CRITICAL DEFICIENCY? Is there reasonable substantiation that could cover the claim? Does
the "clear and conspicuous" standard actually apply in this specific context or format?
Could a qualified disclosure cure the deficiency without pulling the advertisement?

If Pass 3 identifies a compelling argument, revise the classification to 🟠 NON-COMPLIANT
and state the basis. Record in the Glass Box: `self_interrogation: "REVISED — [reason]"`.

### Confidence Scoring

| Level        | Range     | Meaning                                                                                           | Action                                                                        |
| ------------ | --------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear FTC Act violation; settled law; unambiguous CFR provision                                   | State with confidence; recommend immediate remediation                        |
| **High**     | 0.80–0.94 | Strong FTC authority; minor interpretation questions; consistent with recent enforcement          | State finding with brief caveat on residual ambiguity                         |
| **Probable** | 0.60–0.79 | Good FTC arguments; reasonable minds could differ; FTC has not specifically addressed this format | State with reasoning and contra-indicators; recommend legal review            |
| **Possible** | 0.40–0.59 | Genuinely uncertain; novel digital format; FTC guidance not yet updated for this practice         | Flag for counsel review with both sides of the analysis                       |
| **Unlikely** | 0.0–0.39  | Speculative; FTC has not pursued similar practices; weak legal basis                              | Do not assert as a finding; flag as an "emerging risk" watch item if relevant |

---

## Anti-Patterns

An explicit catalogue of what NOT to do in FTC advertising compliance work — both
advertiser-side practices that create violations and compliance-program failures that
create blind spots.

**Advertiser-side anti-patterns:**

1. **Burying "#ad" among ten other hashtags** — Placing the required material connection
   disclosure in a crowd of hashtags (#travel #lifestyle #ad #vacation #sunsets) fails
   the clear-and-conspicuous standard. The disclosure must be "difficult to miss."
   16 CFR § 255.0.

2. **Using "#gifted," "#collab," or "#ambassador" as the sole disclosure** — These terms
   are ambiguous and do not clearly communicate a commercial relationship to ordinary
   consumers. Use "Ad," "Advertisement," "#ad," "Paid partnership," or "Sponsored."
   [VERIFY FTC's current enforcement position on "#gifted" as sole disclosure post-2023.]

3. **Claiming "Made in USA" on products assembled from mostly imported components** —
   An unqualified MUSA claim requires that the product's final assembly, significant
   processing, and all or virtually all components and ingredients are US-origin.
   A product assembled in the US from primarily imported parts cannot make the unqualified
   claim. 16 CFR § 323.2. Violations are subject to civil penalties.

4. **Using "Results not typical" as a testimonial disclaimer** — This language was
   specifically identified as inadequate in 16 CFR § 255.2. Must disclose the actual
   typical consumer result (e.g., "average user loses 5 pounds," "typical savings: $35/month").

5. **Failing to disclose employee social media posts about the employer's products** —
   16 CFR § 255.5 explicitly covers employees posting about their employer's products on
   personal accounts, including organic community forum posts. Employers must train
   employees and implement policies.

6. **Claiming "clinically proven" on the basis of a single pilot study** — "Clinically
   proven" communicates scientific consensus to consumers. FTC generally requires at
   least two well-designed, peer-reviewed RCTs for health efficacy claims. A single
   small pilot study is insufficient.

7. **Making unqualified "recyclable" claims when recycling infrastructure serves fewer
   than 60% of consumers** — 16 CFR § 260.12 requires qualification when infrastructure
   availability falls below the "substantial majority" threshold.

8. **Claiming "biodegradable" for products customarily disposed in landfills** — Landfill
   anaerobic conditions prevent biodegradation. An unqualified biodegradable claim for
   a product that will end up in a landfill is deceptive under 16 CFR § 260.8.

9. **Using general "eco-friendly" or "sustainable" claims without qualification** —
   16 CFR § 260.4 explicitly treats unqualified general environmental benefit claims as
   deceptive because they imply the product has no negative environmental impact.

10. **Claiming carbon offset credit for legally mandated emission reductions** —
    16 CFR § 260.5: if the emission reduction is required by law, it would occur regardless
    of offset purchase, making the offset claim deceptive.

11. **Making online enrollment easy but requiring phone calls to cancel** — Post-2024
    Negative Option Marketing Rule, cancellation must be at least as easy to use as
    enrollment. Online enrollment with phone-only cancellation is a direct violation.

12. **Charging customers after a "free trial" without clear upfront disclosure** —
    ROSCA (15 U.S.C. § 8403) and the 2024 Negative Option Rule require clear and
    conspicuous disclosure of all material terms — including free-to-paid conversion —
    before obtaining billing information. Burying the conversion in terms of service
    is inadequate.

13. **Operating a company-controlled review website without disclosing ownership** —
    16 CFR § 465.6 prohibits representing a company-controlled review platform as
    independent. A manufacturer operating an "impartial" comparison site without
    disclosing ownership violates this rule.

14. **Paying for reviews expressing a particular sentiment** — 16 CFR § 465.4 prohibits
    paying for reviews that express a specific (positive or negative) viewpoint. Conditioning
    compensation on positive reviews is a direct violation.

15. **Suppressing negative reviews without uniform, objective criteria** — 16 CFR § 465.7
    prohibits suppression of genuine reviews through threats or intimidation, and prohibits
    falsely representing that displayed reviews represent all submissions. Suppression is
    permitted only on uniformly-applied objective grounds (defamatory, obscene, clearly fake).

16. **Providing free products to influencers without disclosure training or contract
    requirements** — Even unsolicited free products create material connection disclosure
    obligations if endorsed (16 CFR § 255.5). Advertisers have an obligation to ensure
    endorsers make required disclosures; relying on endorsers to self-police is insufficient.

17. **Selling all RECs and then claiming renewable energy in advertising** — 16 CFR § 260.15:
    if you generate renewable energy but sell all renewable energy certificates to others,
    you cannot claim your products are "made with renewable energy."

18. **Treating NAD/NARB clearance as equivalent to FTC compliance** — NAD/NARB
    self-regulatory decisions are not binding on the FTC and do not provide safe harbor.
    NAD clearance is valuable evidence but not a substitute for independent FTC standard
    analysis; the FTC has brought enforcement actions on claims that passed NAD review.

19. **Making health claims first, gathering substantiation second** — The FTC's prior
    substantiation doctrine (_Pfizer_, 81 F.T.C. 23 (1972)) requires that evidence exists
    before the claim is made. Launching a campaign and commissioning studies in response
    to FTC inquiry is the most common pattern in FTC health claim enforcement actions.

20. **Assuming influencer disclosure policies from 2018–2021 are current** — The 2023
    Endorsement Guide revision expanded material connection definitions (to include family/
    personal relationships), clarified the clear-and-conspicuous standard, added agency
    and brand liability provisions, and addressed virtual influencers. Pre-2023 policies
    and contracts should be reviewed and updated.

---

## Writing Standards

### For compliance findings and remediation guidance:

- Write every finding in the format: [subject] [action/omission] [FTC authority violated]
- Write every remediation step in imperative form: "Pull the advertisement," "Add the
  disclosure," "Update the influencer contract template"
- Use plain language for executive summaries; legal citations belong in the detailed findings
- State uncertainty explicitly: "This practice has not been directly addressed by the FTC
  in post-2023 enforcement but is likely to be treated as..." rather than asserting
  uncertain conclusions

### For endorsement/disclosure guidance:

- Provide specific acceptable disclosure language examples, not just abstract principles
- State what is insufficient, not just what is required
- Note platform-specific considerations where material

### Quality gates before delivery:

- [ ] No finding without a specific supporting practice, fact, or omission
- [ ] No legal claim without a cited authority (or explicit [VERIFY] marker)
- [ ] No enforcement outcome asserted as certain (FTC has prosecutorial discretion)
- [ ] All [VERIFY] markers represent genuine regulatory uncertainty, not general hedging
- [ ] Remediation steps are specific enough to act on without further interpretation
- [ ] No assessment of self-regulatory (NAD/NARB) compliance as substitute for FTC analysis
- [ ] Civil penalty exposure estimates flagged as estimates requiring legal confirmation
- [ ] Pending FTC rulemaking flagged where it may affect any current finding

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 3, search for current CFR text for all FTC rules cited in this skill
- Search for recent FTC consent orders and enforcement actions in the advertiser's industry
- Save the most relevant results to `/tmp/legalcode-ftc-adv-authority.md`
- Verify current civil penalty inflation-adjusted maximum
- Check status of pending FTC rulemakings (commercial surveillance, Green Guides update)
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all CFR regulatory citations [VERIFY] in the output
- Note in the Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Advise client to confirm current CFR text at ecfr.gov and current FTC guidance at ftc.gov
- For FTC enforcement action research, refer to ftc.gov/news-events/enforcement
- For current rule text: ecfr.gov (search by CFR title/part)
- For FTC guidance documents: ftc.gov/tips-advice/business-center/guidance
- For active rulemakings: ftc.gov/policy/federal-register-notices/rules

**Related skills:**

- `legalcode-advertising-marketing-compliance` — broader marketing compliance framework
- `legalcode-us-ada-accommodation` — accessibility in advertising and digital properties
- `legalcode-us-fcpa-compliance` — for advertising in international/government-adjacent contexts
- `legalcode-us-ofac-sanctions-screening` — for advertising campaigns involving sanctioned regions

---

## Output Format Template

````markdown
# FTC Advertising Compliance Assessment

**Advertiser**: [Name]
**Assessment Scope**: [Advertising campaign / practice / program]
**Assessment Date**: [date]
**Prepared for**: [Legal/Compliance / Marketing / Executive Team]
**Prior FTC History**: [Active consent order: [scope] / Prior consent order / None / Unknown]
**legalcode-mcp**: [Connected — authority file at /tmp/legalcode-ftc-adv-authority.md / Not connected]

---

## Executive Summary

[2-4 sentences summarizing overall compliance posture, top risks, and priority actions.]

### Compliance Domain Dashboard

| Domain                                 | Classification | Priority   | Key Finding        |
| -------------------------------------- | -------------- | ---------- | ------------------ |
| Advertising Substantiation             | 🔴/🟠/🟡/🟢    | Tier 1/2/3 | [One-line summary] |
| Disclosure Practices                   | 🔴/🟠/🟡/🟢    | Tier 1/2/3 | [One-line summary] |
| Endorsement / Testimonial Program      | 🔴/🟠/🟡/🟢    | Tier 1/2/3 | [One-line summary] |
| Native Advertising / Deceptive Formats | 🔴/🟠/🟡/🟢    | Tier 1/2/3 | [One-line summary] |
| Environmental / Green Claims           | 🔴/🟠/🟡/🟢    | Tier 1/2/3 | [One-line summary] |
| Made in USA / Origin Claims            | 🔴/🟠/🟡/🟢    | Tier 1/2/3 | [One-line summary] |
| Negative Option / Subscription         | 🔴/🟠/🟡/🟢    | Tier 1/2/3 | [One-line summary] |
| Consumer Reviews                       | 🔴/🟠/🟡/🟢    | Tier 1/2/3 | [One-line summary] |
| Children's Advertising                 | 🔴/🟠/🟡/🟢    | Tier 1/2/3 | [One-line summary] |
| FTC Compliance Program                 | 🔴/🟠/🟡/🟢    | Tier 1/2/3 | [One-line summary] |

**Overall Posture**: 🔴 CRITICAL / 🟠 ELEVATED / 🟡 MODERATE / 🟢 COMPLIANT
**Civil Penalty Exposure**: [Yes — active consent order or rule violation / Potential / Low / None identified]
**Outside FTC Counsel Recommended**: Yes / No / Immediate

---

## Detailed Findings

[Repeat per domain where findings exist:]

### [Domain Name]

**Classification**: [🔴/🟠/🟡/🟢 TIER] | **Confidence**: [Level (range)]

#### Findings

| #   | Finding   | Classification | FTC Authority | Priority     |
| --- | --------- | -------------- | ------------- | ------------ |
| 1   | [Summary] | [Tier]         | [Cite]        | [Tier 1/2/3] |

#### Finding Detail

> **Domain**: [Domain]
> **Classification**: [Tier]
> **Finding**: [One sentence]
> **FTC Authority**: [Specific citation]
> **Risk**: [Enforcement theory; civil penalty exposure if applicable]
> **Evidence**: [Specific practice or gap supporting the finding]
> **Remediation**: [Specific corrective actions]
> **Owner**: [Role]
> **Deadline**: [Timeframe]
> **Escalation**: [Internal escalation path]

---

## Enforcement Exposure Analysis

**Civil Penalty Risk**: [Assessment based on consent order history and rule violations]
**Consumer Harm Pathway**: [How consumers are or could be harmed]
**Enforcement Probability**: [Definite/High/Probable/Possible/Unlikely — rationale]
**FTC Penalty Decision Factors**: [Prior knowledge, severity, duration, size, cooperation, remediation]
**State AG Parallel Risk**: [California / New York / Multi-state / None identified]

---

## Priority Remediation Roadmap

### Tier 1 — Immediate (24-48 Hours)

- [ ] [Specific action]

### Tier 2 — Near-Term (30 Days)

- [ ] [Specific action]

### Tier 3 — Background (90 Days)

- [ ] [Specific action]

---

## Limitations and Scope

This assessment did NOT assess:

- [List any domains skipped due to lack of information]
- FDA advertising requirements (separate regulatory regime)
- Comprehensive state UDAP statute compliance

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-us-ftc-advertising-compliance"
  assessment_date: "[date]"
  advertiser: "[name or description]"
  assessment_scope: "[campaign / practice / program assessed]"
  advertiser_industry: "[industry]"
  media_channels_assessed: "[list]"
  prior_ftc_history: "[Active consent order | Prior consent order | None | Unknown]"
  consent_order_applicable: "[Yes | No | Unknown]"
  legalcode_mcp: "[Connected | Not connected — manual verification required]"
  authority_reference_file: "[/tmp/legalcode-ftc-adv-authority.md | Not created]"
  domains_assessed:
    - "[list each domain assessed]"
  statutes_cited:
    - "15 U.S.C. § 45 — [VERIFIED/UNVERIFIED]"
    - "16 CFR Part 255 (2023) — [VERIFIED/UNVERIFIED]"
    - "[additional citations]"
  citations_verified: "[N VERIFIED] / [N total]"
  critical_deficiencies: "[count]"
  non_compliant: "[count]"
  partial: "[count]"
  compliant: "[count]"
  self_interrogation: "[PASS | REVISED — [reason] | NOT APPLICABLE]"
  confidence: "[HIGH | MEDIUM | LOW] — [rationale]"
  ftc_rulemaking_note: "FTC rulemaking on commercial surveillance, endorsement guides, Green Guides, and negative option is active as of 2026 — verify current regulatory status before acting on any rule-based finding"
  limitations:
    - "[scope limitations, missing information, or assumptions made]"
  reviewer: "AI-assisted — requires qualified FTC/advertising law counsel review"
```
````

```

---

## Localization Notes

This skill is jurisdiction-specific to **US federal FTC law**. When advertising crosses
borders, note these overlaps:

- **FTC + FDA**: Health and drug claims are jointly regulated. FTC governs advertising;
  FDA governs labeling. For prescription drugs and medical devices, FDA advertising
  rules are primary; FTC defers. For over-the-counter claims and dietary supplements,
  FTC is primary.
- **FTC + CFPB**: Financial product advertising is jointly regulated. CFPB has primary
  authority for consumer financial products; FTC retains concurrent jurisdiction.
- **FTC + FCC**: CAN-SPAM (email marketing) and TCPA (telephone/text) involve FCC as
  well as FTC enforcement.
- **State UDAP**: California UCL/FAL/CLRA, New York GBL §§ 349/350, Texas DTPA, and
  other state statutes are independent of FTC but often track FTC standards. A finding
  that the FTC would not pursue may still expose the advertiser to state AG or class
  action risk.
- **GDPR/international**: Behavioral advertising and data collection for advertising
  targeting trigger GDPR, UK GDPR, and other international data protection regimes.
  This skill does not cover those regimes.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on primary research into
15 U.S.C. §§ 45, 45a, 45b, 8401-8403, 6501-6508; 16 CFR Parts 255 (2023), 260 (2012),
323 (2021), 425 (2024), 465 (2024), 310; FTC policy statements on deception (1983) and
unfairness (1980); FTC substantiation framework (*Pfizer*, 81 F.T.C. 23 (1972)); and
structural patterns from the Legalcode FCPA and OFAC compliance skill reference standards.
Research conducted via primary legal databases (law.cornell.edu, eCFR) and authoritative
legal commentary. All statutory citations verified against primary sources at research date.
All [VERIFY] markers represent areas where current text or FTC enforcement position should
be independently confirmed against current FTC.gov and ecfr.gov before use.
```
