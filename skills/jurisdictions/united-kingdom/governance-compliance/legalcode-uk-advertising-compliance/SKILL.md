---
name: legalcode-uk-advertising-compliance
description: Review UK advertising and marketing communications for compliance with the CAP Code (non-broadcast),
  BCAP Code (broadcast), ASA enforcement practice, CMA consumer-protection expectations, pricing and discount
  claim rules, influencer and affiliate disclosure obligations, green and environmental claims, comparative
  advertising rules, distance selling disclosures, sector-specific restrictions (financial promotions,
  alcohol, gambling, food/nutrition/health, children's advertising, vaping/tobacco, crypto-assets), PECR
  and UK GDPR direct marketing obligations, and the Digital Markets, Competition and Consumers Act 2024
  (DMCCA) consumer protection regime including fake reviews, drip pricing, and subscription contract obligations.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review UK advertising and marketing communications for compliance with the CAP Code (non-broadcast), BCAP Code (broadcast), ASA enforcement practice, CMA consumer-protection expectations, pricing and discount claim rules, influencer and affiliate disclosure obligations, green and environmental claims, comparative advertising rules, distance selling disclosures, sector-specific restrictions (financial promotions, alcohol, gambling, food/nutrition/health, children's advertising, vaping/tobacco, crypto-assets), PECR and UK GDPR direct marketing obligations, and the Digital Markets, Competition and Consumers Act 2024 (DMCCA) consumer protection regime including fake reviews, drip pricing, and subscription contract obligations. Produces COMPLIANT / ADVISORY / NON-COMPLIANT / CRITICAL EXPOSURE findings with prioritised remediation and a Glass Box audit trail. Use when pre-clearing advertising copy or campaign materials before publication, assessing existing advertising against CAP/BCAP Code requirements, responding to ASA complaints or investigations, preparing for CMA consumer protection scrutiny, auditing influencer campaign compliance, reviewing green claims against CMA and ASA standards, assessing pricing promotions and discount claim compliance, or evaluating sector-specific advertising restrictions. Jurisdiction: England and Wales (primary); CAP Code applies UK-wide; BCAP Code governed by Ofcom; certain sector-specific rules (gambling, financial promotions) apply across UK with separate devolved enforcement.


# UK Advertising and Promotions Compliance Review

> **Disclaimer**: This skill provides an AI-assisted framework for assessing advertising
> and marketing communications compliance under the CAP Code, BCAP Code, and applicable
> UK consumer protection law. It does not constitute legal advice or a compliance
> certification. CAP and BCAP Code rules, ASA enforcement practice, CMA guidance, and
> supporting legislation change frequently; all references carry hallucination risk —
> verify against current CAP Code text at asa.org.uk, ASA AdviceOnline, CMA guidance at
> gov.uk/cma, and primary legislation at legislation.gov.uk before relying on them. This
> skill does not replace advice from a qualified solicitor or regulatory specialist. ASA
> adjudications are fact-specific; no framework guarantees immunity from complaint or
> enforcement. Verify all statutory references before use.

---

## Purpose and Scope

This skill assesses advertising and marketing communications for compliance with UK
self-regulatory codes and consumer protection law, identifies compliance gaps, classifies
their severity, and produces a prioritised remediation roadmap with clear next steps.

**Covers:**

- CAP Code (UK Code of Non-broadcast Advertising and Direct & Promotional Marketing) —
  all sections including recognition, misleading advertising, harm and offence, pricing,
  testimonials, environmental claims, comparative advertising, and distance selling
- BCAP Code (UK Code of Broadcast Advertising) — broadcast-specific rules for TV and radio,
  including scheduling, children's advertising, and alcohol
- ASA enforcement practice — complaints procedure, investigation responses, proactive
  monitoring, and escalation pathways
- CMA consumer-protection expectations — DMCCA 2024 unfair commercial practices, drip
  pricing, fake reviews, subscription contract rules
- Pricing and discount claims — "was/now" reference prices, "free" claims, mandatory fees,
  sale advertising, dynamic pricing disclosure
- Influencer and affiliate marketing disclosures — CAP Code Section 2 recognition rules,
  "#ad" requirements, paid partnership labels, affiliate link disclosure
- Green and environmental claims — CMA Green Claims Code, ASA October 2025 guidance,
  net zero and carbon neutral substantiation requirements
- Comparative advertising — Business Protection from Misleading Marketing Regulations 2008
  (BPRs), conditions for permissible comparisons
- Distance selling and online advertising — Consumer Contracts (Information, Cancellation
  and Additional Charges) Regulations 2013, CAP Code Section 9
- Sector-specific restrictions — financial promotions (FSMA 2000 s.21 / FCA rules),
  alcohol, gambling (UKGC), food and nutrition health claims, HFSS advertising to
  children, tobacco and vaping, crypto-assets (FCA financial promotion rules)
- PECR and UK GDPR — email and SMS marketing consent, cookie-based ad targeting, ICO
  direct marketing requirements
- DMCCA 2024 — fake reviews (Schedule 20 per se prohibited practices), drip pricing,
  subscription contract obligations
- COMPLIANT / ADVISORY / NON-COMPLIANT / CRITICAL EXPOSURE classification
- Prioritised remediation (IMMEDIATE / NEAR-TERM / BACKGROUND)
- Glass Box audit trail for counsel and compliance team use

**Does not:**

- Certify regulatory compliance — that determination rests with the ASA, CMA, or relevant
  regulator
- Provide legal opinions on specific enforcement risk or litigation exposure
- Constitute legal advice or replace qualified advertising law counsel
- Assess detailed FCA financial promotions compliance in depth for regulated firms —
  use `legalcode-uk-fca-regulatory-compliance` for full FCA Handbook analysis
- Cover data protection compliance beyond its advertising context — use
  `legalcode-eu-dpia-assessment` or ICO guidance for full UK GDPR assessments
- Apply to product liability, intellectual property infringement, or defamation claims
  arising from advertising content (though it flags advertising-context IP risks)

**Related skills:**

- `legalcode-uk-fca-regulatory-compliance` — full FCA Handbook compliance for regulated
  firms; use alongside this skill for financial promotions by authorised firms
- `legalcode-uk-bribery-act-compliance` — anti-bribery considerations in sponsorship and
  promotional arrangements
- `legalcode-eu-gdpr-breach-notification-operations` — UK GDPR breach notification if a
  data incident affects advertising datasets

---

## Jurisdiction and Governing Law

**Primary jurisdiction**: England and Wales, though the CAP Code applies across the United
Kingdom. Key instruments:

- **CAP Code** (15th edition, current) — self-regulatory code administered by the
  Committee of Advertising Practice (CAP) and enforced by the Advertising Standards
  Authority (ASA). Not primary legislation but has quasi-regulatory effect through industry
  commitment, media owner sanctions, and ASA referral powers to Trading Standards and Ofcom.
- **BCAP Code** (current edition) — broadcast advertising equivalent, enforced by ASA
  under delegation from Ofcom under the Communications Act 2003.
- **Consumer Protection from Unfair Trading Regulations 2008 (CPUTRs)** — implements
  the EU Unfair Commercial Practices Directive in UK law; Schedule 1 lists 31 per se
  unfair practices; enforced by CMA and Trading Standards. [VERIFY: DMCCA 2024 has
  substantially replaced CPUTRs for most purposes from April 6 2025.]
- **Digital Markets, Competition and Consumers Act 2024 (DMCCA)** — consumer protection
  provisions in force from April 6 2025; Schedule 20 lists 32 per se unfair commercial
  practices including fake reviews and aggressive subscription traps.
- **Business Protection from Misleading Marketing Regulations 2008 (BPRs)** — governs
  comparative advertising between businesses; implements the EU Comparative Advertising
  Directive [VERIFY: retained post-Brexit].
- **Consumer Contracts (Information, Cancellation and Additional Charges) Regulations
  2013 (SI 2013/3134)** — prescribes pre-contract information requirements for distance
  and off-premises contracts.
- **Privacy and Electronic Communications Regulations 2003 (PECR)** — consent
  requirements for electronic direct marketing and cookie-based ad targeting.
- **Sector-specific regimes**: FSMA 2000 s.21 and FCA Handbook COBS 4 (financial
  promotions); Gambling Act 2005 and UKGC codes; Regulation (EC) 1924/2006 retained as
  UK domestic law (nutrition and health claims); Tobacco and Related Products Regulations
  2016; Vaping Products (Restrictions) Regulations 2024 [VERIFY current SI number].

**Scotland and Northern Ireland**: The CAP Code applies across the UK. Enforcement
referrals may go to Trading Standards Scotland or CCNI (Consumer Council for Northern
Ireland) for persistent non-compliance. Broadcasting rules are UK-wide under Ofcom.

**Non-UK advertisers targeting UK consumers**: The CAP Code applies to ads targeting
UK consumers regardless of the advertiser's location. ASA jurisdiction over non-UK
websites is limited but can be exercised where UK consumers are targeted; enforcement
may be through platform pressure, Trading Standards referral, or EASA cross-border
mechanisms [VERIFY current EASA cross-border reach post-Brexit].

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses and asks when:

- The answer would change which CAP/BCAP rules or sector-specific regime applies
- The type of medium or audience affects which code provisions are triggered
- Severity classification requires knowing the commercial context or audience profile
- A recent regulatory development may affect the analysis

Use the **⟁ CLARIFY** pattern (structured options with descriptions) wherever marked below.
If the user has already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept Input

Accept advertising materials in any of these formats:

- **Document**: PDF, DOCX, image file, or video/audio file with transcript
- **Pasted text**: Ad copy, script, or marketing communication pasted directly
- **Campaign brief**: Description of a planned campaign including claims and channels
- **URL**: Link to a live advertisement, social media post, or landing page
- **Multiple assets**: A campaign comprising several related materials (review holistically)

If no material is provided, prompt the user to supply the advertising content to be reviewed.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the following. Skip questions already answered
by the input.

1. **Review purpose** — What is the primary objective?
   - **Pre-clearance**: Review before publication/broadcast to identify issues proactively
   - **Post-complaint**: Respond to an ASA complaint or investigation
   - **CMA/Trading Standards inquiry**: Respond to regulatory scrutiny
   - **Internal audit**: Assess existing campaign materials for compliance risk
   - **Campaign brief review**: Assess planned claims before creative development
   - _Why this matters_: Post-complaint review requires evidence gathering strategy;
     pre-clearance focuses on proactive remediation before the ad goes live.

2. **Medium and channel** — Where will / does the ad appear?
   - Non-broadcast online (website, social media, email, display, search, affiliate)
   - Broadcast TV (BCAP Code; Clearcast pre-clearance may be required)
   - Broadcast radio (BCAP Code; Radiocentre pre-clearance may be required)
   - Print (newspapers, magazines, direct mail)
   - Outdoor / out-of-home (posters, digital OOH)
   - Cinema
   - Multiple channels (list all)
   - _Why this matters_: CAP Code covers non-broadcast; BCAP Code covers broadcast.
     Some rules differ materially (e.g., alcohol scheduling rules, children's HFSS
     restrictions). TV ads require Clearcast pre-clearance before broadcast.

3. **Product / service sector** — What is being advertised?
   - General consumer goods or services (default CAP/BCAP rules)
   - Alcohol
   - Gambling or betting
   - Food, nutrition supplements, or health products
   - Financial products or services (including credit, investments, insurance, crypto)
   - Medicines or medical devices (MHRA jurisdiction)
   - Tobacco, vaping, or e-cigarettes
   - Cosmetics or beauty products
   - Vehicles (environmental claims common)
   - Other (describe)
   - _Why this matters_: Sector-specific rules apply additional or stricter requirements
     beyond the general CAP/BCAP framework. Financial promotions require FCA authorisation.

4. **Target audience** — Who is the primary audience?
   - General adult consumers (18+)
   - Consumers including under-18s or general population (not age-restricted)
   - Children (under 12) or young people (12-17) primarily
   - Vulnerable consumers (gambling, financial products, health claims)
   - Business-to-business (B2B in specialist trade media)
   - _Why this matters_: Stricter rules apply to ads targeting children (HFSS food,
     gambling, alcohol scheduling). Vulnerable consumer protections apply in regulated
     sectors.

5. **Influencer or affiliate involvement** — Does the campaign use influencers, endorsers,
   or affiliates?
   - No influencer or affiliate involvement
   - Paid influencer posts (cash payment)
   - Gifted products / services (free items provided)
   - Affiliate links or commission arrangements
   - Brand ambassador or long-term commercial relationship
   - _Why this matters_: All commercial relationships require "#ad" or equivalent
     disclosure under CAP Code Section 2. The brand bears responsibility for ensuring
     influencer compliance.

6. **Environmental claims** — Does the ad make any green, sustainability, or environmental
   claims?
   - Yes — specify the claims (e.g., "carbon neutral", "eco-friendly", "sustainable")
   - No
   - _Why this matters_: Environmental claims trigger the CMA Green Claims Code and ASA
     October 2025 guidance; absolute claims require full lifecycle substantiation.

7. **Pricing or promotional claims** — Are there pricing promotions, comparisons, or
   "was/now" pricing?
   - Yes — describe the pricing claims
   - No
   - _Why this matters_: Reference prices must be genuine; mandatory fees must be included
     in headline prices; DMCCA 2024 and ASA rules apply.

If the user provides partial context, proceed with reasonable assumptions and state them
explicitly at the start of the assessment.

### Step 3: Map the Applicable Regulatory Framework

Based on the context gathered in Step 2, identify which codes and statutory instruments
apply to the specific material under review.

**Core codes applicable to all advertising:**

| Code / Instrument            | Applies To                            | Key Contact / Enforcer  |
| ---------------------------- | ------------------------------------- | ----------------------- |
| CAP Code (all sections)      | All non-broadcast advertising         | ASA                     |
| BCAP Code                    | TV and radio advertising              | ASA / Ofcom             |
| CPUTRs 2008 / DMCCA 2024     | Consumer-facing advertising           | CMA / Trading Standards |
| BPRs 2008                    | Comparative advertising (B2B and B2C) | CMA / Trading Standards |
| Consumer Contracts Regs 2013 | Distance-selling advertising          | Trading Standards       |
| PECR 2003                    | Email, SMS, cookie-based targeting    | ICO                     |

**Sector-specific instruments — apply if the product/audience triggers them:**

| Sector                        | Applicable Rules                                                   | Regulator                |
| ----------------------------- | ------------------------------------------------------------------ | ------------------------ |
| Financial products / services | FSMA 2000 s.21; FCA COBS 4; FG24/1 social media; PS23/6 crypto     | FCA                      |
| Alcohol                       | CAP Code Ch. 18; BCAP Code Ch. 19 (scheduling restrictions)        | ASA                      |
| Gambling                      | CAP Code Ch. 16; BCAP Code Ch. 17; UKGC Social Responsibility Code | ASA / UKGC               |
| Food and nutrition claims     | EC 1924/2006 (retained UK); MHRA (medicines); HFSS scheduling      | ASA / MHRA               |
| Tobacco                       | Tobacco Advertising and Promotion Act 2002; Health Act 2009        | Trading Standards        |
| Vaping / e-cigarettes         | TRPR 2016; Vaping Products (Restrictions) 2024                     | MHRA / Trading Standards |
| Medicines / medical devices   | Medicines Act 1968; Human Medicines Regulations 2012; MHRA         | MHRA / ASA               |
| Crypto-assets                 | FCA financial promotion rules PS23/6 (from October 2023)           | FCA                      |
| Children's food (HFSS)        | Ofcom HFSS rules (non-broadcast online from October 2025)          | Ofcom / ASA              |

**⟁ CLARIFY** — If the sector is unclear or straddles multiple categories (e.g., a health
supplement that also makes weight-loss claims), ask the user to confirm which sector rules
to prioritise before proceeding.

### Step 4: Gather Legal Authority

Use **legalcode-mcp** (if connected) to retrieve current CAP Code and BCAP Code provisions,
recent ASA adjudications relevant to the ad type, and applicable statutory instruments.

**Research process:**

1. Search for recent ASA rulings on the specific claim type or sector involved
2. Search for relevant CAP AdviceOnline guidance articles on the topics identified
3. Search for CMA enforcement notices or guidance applicable to the product/claims
4. Save the most relevant results to `/tmp/legalcode-uk-ad-compliance.md`

**If legalcode-mcp is not connected:**

- Mark all ASA ruling citations with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Proceed using the research frameworks in this skill

### Step 5: Systematic Compliance Assessment

Assess the advertising material systematically across all applicable compliance areas.
Read the full material before flagging issues — claims interact (e.g., a "best" superlative
combined with a footnote restriction can still create an overall misleading impression).

**⟁ CLARIFY** — For large campaign sets (5+ assets, or complex multi-channel campaigns),
ask the user whether to perform a full assessment of all compliance areas or a priority
assessment focused on the highest-risk elements identified in Step 2 (e.g., green claims,
influencer disclosures, pricing claims).

Cover all applicable compliance areas from the **Topic Analysis** section below. For each,
assess whether the material:

- Complies with applicable rules
- Raises an advisory concern requiring attention
- Is non-compliant and requires amendment before publication
- Creates critical statutory exposure requiring immediate withdrawal

### Step 6: Missing Disclosure Detection

After assessing the claims made, check for required disclosures or information that is
absent from the material:

- **Ad recognition label** missing from influencer post or sponsored content
- **Representative APR** absent from financial advertising triggering the requirement
- **Risk warning** absent from gambling or investment advertising
- **Cancellation rights** absent from distance-selling advertising
- **Material information** about charges, conditions, or limitations omitted
- **Alcohol unit / "drink responsibly" statement** missing from alcohol ads
- **Age restriction label** missing from age-restricted products

For each missing disclosure, assess severity using the classification framework below.

**⟁ CLARIFY** — Where the severity depends on the audience profile or channel (e.g.,
whether the ad targets children determines HFSS rule applicability), ask rather than assume.

### Step 7: Classify Each Finding

Classify every finding using the four-tier severity system:

**COMPLIANT** — The material satisfies the applicable CAP/BCAP Code rule and supporting
law. No action required.

**ADVISORY** — A minor or technical issue that is unlikely to result in an upheld ASA
ruling but creates a risk of complaint or could be improved. Should be rectified before
or at the next creative refresh.

**NON-COMPLIANT** — A breach of the CAP or BCAP Code that is likely to result in an
upheld ASA ruling if complained about. The material should be amended before publication
(pre-clearance review) or immediately withdrawn and amended (post-publication review).

**CRITICAL EXPOSURE** — A breach of primary legislation (CPUTRs / DMCCA 2024, FSMA 2000
s.21, Tobacco Advertising and Promotion Act, MHRA rules, PECR) or a per se unfair
commercial practice under DMCCA 2024 Schedule 20. Carries risk of Trading Standards
referral, CMA enforcement, FCA action (including financial penalties), or criminal
liability. Requires immediate withdrawal and legal counsel involvement.

**⟁ CLARIFY** — For borderline classifications where the severity depends on business
context (e.g., whether a claim is puffery or an objective claim requiring substantiation),
present the ambiguity and ask: "This claim [X] could be read as obvious puffery (which
does not require substantiation) or as an objective performance claim (which does). How
does your organisation characterise it, and do you have supporting evidence?"

### Step 8: Generate Remediation Steps

For each NON-COMPLIANT or CRITICAL EXPOSURE finding, generate specific remediation steps:

- **Immediate action**: Withdraw the ad / pause the campaign / suspend influencer posting
- **Amendment required**: Specify the exact change needed (add "#ad", add qualification
  to the claim, add pricing disclosure, remove unsubstantiated claim)
- **Evidence to gather**: Specify what evidence is needed to substantiate the claim if
  retained (e.g., trial data, expert opinion, genuine pricing history records)
- **Regulator notification**: Whether to proactively engage ASA CAP Copy Advice,
  Clearcast, or Trading Standards
- **Fallback position**: An alternative claim or approach that can be used immediately
  while the full remediation is prepared

For ADVISORY findings, recommend the improvement and indicate whether it should be
implemented at the next opportunity or at the next creative refresh.

### Step 9: Prioritise Remediation

Apply the three-tier prioritisation framework:

**IMMEDIATE** (act before the ad continues running or immediately upon discovery):

- All CRITICAL EXPOSURE findings
- NON-COMPLIANT findings where the ad is currently live and generating consumer harm

**NEAR-TERM** (amend before next publication / within 30 days):

- NON-COMPLIANT findings for pre-clearance reviews (must fix before publication)
- NON-COMPLIANT findings for scheduled re-runs or planned campaign extensions

**BACKGROUND** (monitor; address at next creative refresh):

- All ADVISORY findings
- Technical compliance improvements that do not affect the ad's legality

### Step 10: Quality Verification

Before delivering the assessment, run the quality checks from the **Quality Assurance
Framework** section:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every CRITICAL EXPOSURE finding, run the 3-pass Self-Interrogation.
3. Assign a Confidence Score to each finding.
4. Complete the Glass Box audit trail template.

---

## Topic Analysis

### Area 1: Ad Recognition and Identification (CAP Code Section 2)

**Key rules:**

- Rule 2.1: Marketing communications must be obviously identifiable as such
- Rule 2.4: Advertisers must not disguise the commercial nature of marketing communications
- CPUTRs 2008 Schedule 1, item 11 / DMCCA 2024 Schedule 20: Using editorial content to
  promote a product without making clear it is paid-for promotion is a **per se prohibited
  practice** — automatically CRITICAL EXPOSURE regardless of whether consumers are harmed

**Influencer and sponsored content disclosure:**

The following situations require prominent disclosure as a marketing communication:

- Brand has paid money (cash or money's worth) AND has editorial control or approval rights
  → must be labelled "#AD", "Ad", "Sponsored", or "Paid Partnership" prominently
- Affiliate arrangements (commission on sales) → "AD" disclosure required
- Free gifts with expectation of promotion → disclosure strongly recommended [VERIFY:
  DMCCA 2024 may expand mandatory disclosure — check updated CAP/CMA influencer guidance]
- Brand ambassador with ongoing commercial relationship → disclosure required even for
  apparently organic content

**What "prominent" means:**

- Visible without requiring the viewer to expand text, scroll, or pause a video
- Not buried among other hashtags — must appear before any "…more" fold on social posts
- On Stories and short-form video: must appear at a time and in a position where a typical
  viewer would see it
- Instagram "Paid Partnership" label satisfies the requirement when correctly applied;
  X/Twitter and TikTok equivalent labels must be verified to confirm ASA acceptance

**Common failures to check:**

- "#ad" or "#spon" placed at the end of a long hashtag list
- Disclosure only in bio, not in the specific post
- Disclosure visible on desktop but hidden on mobile
- Branded content amplified via paid boost without disclosure
- Advertorial or native ad in editorial format without clear "Advertisement" / "Sponsored"
  label immediately identifiable

**Severity guide:** Any non-disclosure of a commercial relationship is NON-COMPLIANT at
minimum; where the ad is designed to deceive consumers about its commercial origin, this
is CRITICAL EXPOSURE under DMCCA 2024 Schedule 20 item 11.

---

### Area 2: Misleading Advertising and Substantiation (CAP Code Section 3)

**Key principle**: Ads must not materially mislead consumers by act or omission, including
through overall impression, ambiguity, or exploitation of consumer expectations.

**Substantiation requirements (Rule 3.7)**:

- Substantiating evidence must be held **before** the ad is published or submitted for
  publication — post-hoc evidence is not a valid defence
- Objective claims (any claim a reasonable consumer would interpret as a factual assertion
  capable of being true or false) require documentary evidence
- Obvious puffery (clear exaggeration no reasonable person would believe literally) is
  exempt under Rule 3.2 — but the advertiser, not the ASA, does not determine this

**Evidence types and standards:**

- Clinical trials and studies: peer review preferred; sample size, methodology, and
  relevance to the specific claim are assessed; industry-funded studies are accepted
  but scrutinised closely
- Consumer surveys: must use representative samples with sound methodology
- Expert opinion: generally insufficient alone for efficacy claims
- Regulatory approvals: do not automatically authorise all advertising claims about the product
- Comparative tests: must use fair methodology applicable to both products

**Overall impression test**: Assess the ad as a whole — technically accurate statements
combined with misleading visuals, omissions, or framing can still breach Section 3. Check:

- Does the headline contradict or overstate what the body copy qualifies?
- Do images imply claims not made in text (e.g., product performance depicted)?
- Is material information hidden in footnotes or fine print that contradicts the main message?
- Are conditions or exclusions presented so prominently they negate the main claim?

**Testimonials and reviews (Rules 3.45-3.52)**:

- Must reflect genuine consumer experience (not paid endorsements presented as organic)
- Must be accurate at time of use — historical testimonials should be dated
- Atypical results must be disclosed ("Results may vary" or equivalent)
- Testimonials cannot make claims the advertiser could not make directly

**Superlatives and "number one" claims**: Objective superlatives ("the UK's best",
"most effective", "number one seller") require substantiation. Common failures:

- No evidence held to support the superlative scope (UK-wide, category, time period)
- Basis of "number one" claim not disclosed (sales volume, customer satisfaction, specific
  period, specific category)
- Outdated research used to support a current superlative

**"Clinically proven" and similar claims**: High-risk claim type requiring robust,
relevant evidence (ideally RCT-level for health/efficacy claims). Scrutinise:

- Are the studies genuinely relevant to the specific product and claim?
- Were studies conducted on the same formulation?
- Is "clinically proven" specific about what was proven, or a generic quality claim?

**Severity guide:** Misleading claims are NON-COMPLIANT; misleading claims about material
characteristics that could cause consumers to make different purchasing decisions are a
high priority NON-COMPLIANT. Claims that are knowingly false are CRITICAL EXPOSURE under
DMCCA 2024.

---

### Area 3: Harm, Offence, and Social Responsibility (CAP Code Section 4)

**Key principle**: Ads must not cause serious or widespread offence or condone or encourage
harmful behaviour.

**Gender stereotyping (Rule 4.9, in force since June 2019)**: Ads must not include gender
stereotypes likely to cause harm or serious or widespread offence. Prohibited examples:

- Showing a woman unable to complete a practical task or a man unable to do household tasks
- Suggesting a person's appearance is their primary value
- Ads implying that achieving an unrealistic body ideal is necessary for success

**Financial irresponsibility**: Ads for credit or financial products that portray debt as
an aspirational or casual lifestyle choice without appropriate context.

**Unsafe practices**: Ads that encourage dangerous behaviour (e.g., speeding, extreme
dieting, excessive alcohol consumption).

**Offensive content**: Assessed against the standards of a reasonable adult. Context
matters — an ad acceptable in an adult men's magazine may be NON-COMPLIANT on a general
billboard visible to children.

**Social responsibility (Rule 1.3)**: Ads must be prepared with a sense of responsibility
to consumers and society. This is a broad principle applied across all advertising.

**Severity guide:** Ads causing potential widespread offence or condoning harm are
NON-COMPLIANT; ads depicting or encouraging behaviour that could cause physical harm
are CRITICAL EXPOSURE.

---

### Area 4: Pricing and Promotional Claims (CAP Code Section 3; DMCCA 2024)

**Reference prices ("was/now" pricing)**:

- The "was" price must be a genuine price at which the product was offered for a meaningful
  period — an artificially inflated reference price is misleading
- Key question: Was this price genuinely offered to consumers for a sufficient period
  before the promotion began? "Sufficient period" is not defined but ASA practice and
  CMA guidance suggest the reference price period should not be shorter than the sale period
- Evidence required: pricing records demonstrating the reference price was live
- Common failure: inflating the reference price to make the discount appear larger
  (Simba Sleep March 2024 and Origin Mattress July 2025 upheld by ASA) [VERIFY]

**"Free" claims (Rule 3.22)**:

- Items described as free must be genuinely free
- If another item must be purchased at a higher price to obtain the "free" item, the claim
  is misleading
- Compulsory ancillary charges (delivery, processing, membership) must not be described as free

**Drip pricing and mandatory fees**:

- Under DMCCA 2024 and CAP Code Rule 3.17: All mandatory charges must be included in the
  headline price — they may not be revealed progressively during the purchase journey
- Booking fees, delivery charges, mandatory service charges: must be in the headline price
  if unavoidable; optional add-ons may be disclosed later
- CMA Ticketmaster undertakings (September 2025): dynamic pricing tiers require 24-hour
  advance consumer notice [VERIFY]

**Sale advertising**: "Sale" labels must represent a genuine reduction. Ads depicting
sale prices alongside inflated original prices breach Section 3 if the original price is
not genuine.

**False urgency and limited availability (DMCCA 2024 Schedule 20 / CPUTRs Schedule 1)**:

- "Limited time only" and "while stocks last" claims must be genuine — manufactured urgency
  is a per se unfair commercial practice
- Countdown timers that reset or are permanently present are specifically prohibited

**Price match guarantees**: Comparisons must be like-for-like, the methodology must be
disclosed, and all mandatory charges must be included in both prices being compared.

**Severity guide:** Reference price manipulation is NON-COMPLIANT at minimum; manufactured
urgency and drip pricing are CRITICAL EXPOSURE under DMCCA 2024 as per se prohibited
practices.

---

### Area 5: Comparative Advertising (BPRs 2008; CAP Code Section 3.33+)

**Permitted comparative advertising conditions**: Under the BPRs 2008 (Regulation 4), a
comparative ad is permissible only if it [VERIFY current BPRs provisions post-DMCCA]:

1. Is not misleading under the BPRs
2. Compares goods or services meeting the same needs or intended for the same purpose
3. Objectively compares one or more material, relevant, verifiable, and representative
   features (which may include price)
4. Does not create confusion between the advertiser and a competitor or their trade marks
5. Does not discredit or denigrate a competitor's trade marks, trade names, goods, or services
6. Relates to goods with the same designation of origin for products with such designations
7. Does not take unfair advantage of a competitor's trade mark, trade name, or other
   distinguishing marks
8. Does not present goods or services as imitations or replicas of those with a protected
   trade mark or trade name

**Practical checks:**

- Is the competitor identified by name, trade mark, or clearly identifiable description?
- Is the comparison verifiable — can an independent party confirm the basis of comparison?
- Are the products or services genuinely comparable (like-for-like)?
- Does the ad misrepresent the competitor's product or make denigrating statements beyond
  objective comparison?
- Does the ad risk trade mark infringement (use of competitor's mark in advertising)?

**Malicious falsehood risk**: Comparative claims that are false and made with malice could
give rise to a malicious falsehood claim by the competitor — an independent legal risk
outside the CAP Code framework.

**Severity guide:** Non-compliant comparative advertising is NON-COMPLIANT; false
comparative claims that denigrate a competitor using their trade mark without authorisation
are NON-COMPLIANT and carry additional IP litigation risk.

---

### Area 6: Environmental and Green Claims (CMA Green Claims Code; ASA Guidance Oct 2025)

**High-risk claim types requiring fullest substantiation:**

| Claim Type                                       | Issue                           | Required Substantiation                      |
| ------------------------------------------------ | ------------------------------- | -------------------------------------------- |
| "Eco-friendly"                                   | Absolute, unqualified claim     | Full product lifecycle evidence              |
| "Sustainable"                                    | Absolute, unqualified claim     | Full product lifecycle evidence              |
| "Carbon neutral"                                 | May rely on offsets             | Emissions + methodology disclosure           |
| "Net zero"                                       | Corporate vs. product confusion | Scope and timeline must be specified         |
| "Green" / "Clean"                                | Vague, unqualified              | Specific attribute evidence required         |
| "Better for the planet" / "kinder to the planet" | Unqualified comparative         | Evidence of what "better" means and vs. what |

**CMA Green Claims Code six principles** [VERIFY full text in CMA guidance]:

1. Claims must be truthful and accurate
2. Claims must be clear and unambiguous (not require expert knowledge to understand)
3. Claims must not omit or hide important relevant information
4. Comparisons must be fair and meaningful
5. Claims must consider the full life cycle of the product or service
6. Claims must be substantiated

**Cherry-picking**: Highlighting one environmental benefit while ignoring significant
environmental harms elsewhere in the product or supply chain is misleading by omission —
a breach of both the CAP Code and the CMA Green Claims Code.

**Carbon offsetting claims**: Claims of carbon neutrality that rely on offsets must:

- Disclose that the claim is offset-based
- Specify the offset methodology, project type, and verification standard
- Not imply that products are emissions-free when they are merely offset

**Sector-specific heightened scrutiny**:

- Airlines and fossil fuel companies face elevated ASA monitoring (Air France-KLM December
  2023; Lufthansa March 2023 upheld) [VERIFY]
- Vehicle manufacturers: lifecycle claims for hybrid or electric vehicles must not
  overstate environmental benefit vs. conventional alternatives (Mazda September 2024) [VERIFY]
- Fashion and retail: greenwashing claims about fabric sustainability, recycled content,
  and circular economy practices are under active CMA scrutiny

**DMCCA 2024 and greenwashing**: False environmental claims are per se unfair commercial
practices under DMCCA 2024 Schedule 20 [VERIFY specific Schedule 20 provision]. CMA has
direct enforcement powers from April 6 2025.

**Severity guide:** Absolute unqualified environmental claims are NON-COMPLIANT; claims
designed to mislead about the environmental impact of a product are CRITICAL EXPOSURE
under DMCCA 2024 and CMA Green Claims Code enforcement powers.

---

### Area 7: Sector-Specific Restrictions

#### 7a. Financial Promotions

**FSMA 2000 s.21**: Communicating a financial promotion to a person in the UK without FCA
authorisation or FCA-approved approval is a criminal offence. This applies to:

- Invitations or inducements to engage in regulated investment activity
- Promotions for credit products, insurance, mortgages, collective investment schemes
- Cryptoasset promotions (from October 2023 under PS23/6)

**Key compliance checks for financial promotions:**

- Is the ad approved by an FCA-authorised person (or the firm is itself FCA-authorised)?
  [If not → CRITICAL EXPOSURE immediately]
- Is the ad fair, clear, and not misleading (COBS 4.2.1R)?
- Are required risk warnings present (e.g., "Capital at risk" for investments)?
- Is representative APR stated where required, and does it apply to the majority of
  customers obtaining that product?
- Are "typical cost of credit" or "total amount payable" disclosures present for credit ads?

**Cryptoasset promotions (PS23/6, October 2023)**: All qualifying cryptoasset promotions
must be approved by an FCA-authorised person; must include mandatory risk warning
("Don't invest unless you're prepared to lose all the money you invest"); must include
24-hour cooling-off period for retail customers. [VERIFY current FCA crypto promotion rules]

**⟁ CLARIFY** — If the material includes financial services content, immediately ask:
"Has this financial promotion been approved by an FCA-authorised person? If yes, which
firm and when? If no, this is a CRITICAL EXPOSURE issue requiring immediate attention."

#### 7b. Alcohol Advertising

**CAP Code Section 18 / BCAP Code Section 19 key requirements:**

- Must not be directed at or appeal particularly to people under 18 — content, medium,
  and placement all assessed
- Must not depict persons who appear to be under 25 drinking alcohol
- Must not link alcohol to sexual success, daring, or social acceptance
- Must not suggest alcohol has medicinal properties
- Must not condone excessive consumption or irresponsible behaviour
- Must not portray drunkenness positively

**BCAP scheduling**: Alcohol ads on broadcast may not be shown when a significant
proportion of the audience is under 18.

#### 7c. Gambling Advertising

**CAP Code Section 16 / BCAP Code Section 17 / UKGC Social Responsibility Code:**

- Must not appeal to children or young people
- Must not exploit people under 18 or vulnerable people
- Must include required "responsible gambling" messaging and signposting to support services
- Must not trivialise gambling or suggest it is a solution to financial problems
- Must not portray gambling as risk-free or guarantee winnings
- Bonus and free bet promotions must have T&Cs clearly disclosed

**UKGC requirements**: Gambling operators must comply with UKGC Social Responsibility Code
requirements alongside ASA rules; non-compliance can affect the operating licence.

#### 7d. Food, Nutrition, and Health Claims

**Retained EC 1924/2006 (GB Nutrition and Health Claims Register)**:

- Only health claims on the GB register may be used in advertising food products
- Disease prevention/treatment claims are categorically prohibited for food products
- Medicinal claims for foods or supplements require MHRA licensing

**HFSS advertising restrictions (High in Fat, Sugar, or Salt)**:

- Ofcom rules: HFSS products may not be advertised in paid-for online media targeting
  children or in media where children comprise a significant proportion of the audience
  [VERIFY: Ofcom HFSS online rules effective from October 2025]
- CAP/BCAP HFSS rules: apply scheduling restrictions for TV and radio

**Common failures**: Claims like "healthy", "natural", "pure", "wholesome" may imply
health benefits not permitted; "probiotic" requires substantiation for specific strains
and claimed functions.

#### 7e. Tobacco and Vaping

**Tobacco Advertising and Promotion Act 2002**: Advertising tobacco products in any
media accessible to the public is a criminal offence — CRITICAL EXPOSURE if present.

**Vaping / e-cigarettes**:

- Advertising vaping products through channels accessible to under-18s is prohibited
- Only licensed vaping products may be advertised
- Health/cessation claims require MHRA licensing as medicinal products
- Brand advertising of vaping companies (without product claims) may be permissible
  in some channels — verify specific channel rules [VERIFY current Advertising Codes provisions]

---

### Area 8: Distance Selling and Online Advertising

**Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013**
require traders to provide Schedule 2 information clearly and comprehensibly before a
distance contract is concluded. In advertising contexts, the most material obligations are:

- **Total price**: Must be stated inclusive of all taxes; if exact price cannot be determined,
  state the basis of calculation
- **Mandatory additional charges**: Delivery, subscription fees, or handling charges must
  be disclosed
- **Cancellation rights**: Existence of the 14-day right to cancel must be communicated
  in pre-contract information (not necessarily in every ad, but must be accessible before
  contract formation)
- **Trader identity**: Name and geographical address required (PO Box not sufficient for
  complaints address under CAP Code Section 9)

**CAP Code Section 9** mirrors and reinforces the Regulations for non-broadcast advertising:

- Clearly states trader name and address requirements
- Requires full price including all charges to be disclosed
- Requires cancellation and returns information in distance-selling ads

**DMCCA 2024 subscription contracts**: For subscription-based products or services:

- Consumers must expressly acknowledge the payment obligation at the final purchase step
- Reminder notices required before auto-renewal
- Easy cancellation mechanism required (cannot require lengthy phone calls for online subscriptions)

---

### Area 9: Direct Marketing and Digital Advertising (PECR / UK GDPR)

**Email and SMS marketing:**

- Consent is required for sending marketing emails or texts to individuals under PECR
  Regulation 22
- Consent must be: specific, informed, freely given, and evidenced; pre-ticked boxes invalid
- **Soft opt-in exception**: Applies where (a) contact details collected in context of an
  actual or negotiated sale, (b) marketing is for similar products or services, (c)
  recipient was given a clear opt-out opportunity at collection and in every message
- Every marketing message must include an easy opt-out mechanism
- B2B marketing to corporate entities: PECR consent rules do not apply in the same way;
  UK GDPR legitimate interests basis may be available [VERIFY current ICO position]

**Cookie-based ad targeting:**

- Cookies placed for advertising purposes require prior, informed, freely-given consent
  under PECR Regulation 6
- Consent must be obtained before cookies are set
- Cookie walls (conditioning site access on consent) are challenged by ICO [VERIFY
  current ICO enforcement position]

**Check for:**

- Consent records for email / SMS marketing lists — when obtained, for what purpose
- Whether unsubscribe mechanism is prominent in each marketing email
- Whether cookie consent banners and preference centres meet ICO standards
- Whether third-party consent (from data brokers) is sufficiently specific

**Severity guide:** Email marketing without valid consent is NON-COMPLIANT under PECR;
where the ICO has previously warned the organisation, it becomes CRITICAL EXPOSURE. Absence
of cookie consent for advertising cookies is NON-COMPLIANT; systematic evasion of consent
requirements is CRITICAL EXPOSURE.

---

### Area 10: DMCCA 2024 — Consumer-Facing Digital Practices

**DMCCA 2024 Schedule 20 per se unfair commercial practices (in force April 6 2025)**
relevant to advertising and digital marketing:

| Practice                                                                | Schedule 20 Reference         | Severity          |
| ----------------------------------------------------------------------- | ----------------------------- | ----------------- |
| False consumer reviews or commissioning fake reviews                    | Item 23-24 [VERIFY numbering] | CRITICAL EXPOSURE |
| Selectively publishing reviews to mislead                               | Item 25 [VERIFY]              | CRITICAL EXPOSURE |
| Advertorials without disclosure of commercial nature                    | Item 11                       | CRITICAL EXPOSURE |
| False "limited time" or limited quantity claims                         | Item 7                        | CRITICAL EXPOSURE |
| Hidden charges revealed only at checkout                                | Drip pricing provisions       | CRITICAL EXPOSURE |
| Bait advertising (price/product not available in sufficient quantities) | Retained from CPUTRs          | CRITICAL EXPOSURE |

**Online reviews compliance checks:**

- Does the organisation collect customer reviews?
- Are all published reviews genuine (not incentivised or fabricated)?
- Are negative reviews suppressed while positive reviews are displayed?
- Does any invitation to leave a review suggest or require a positive rating?

**⟁ CLARIFY** — If the organisation manages consumer reviews, ask: "Does your review
collection process involve any incentives (discounts, free products) for leaving a review?
And are all received reviews displayed or are some filtered out? Both practices may be
caught by DMCCA 2024 Schedule 20."

---

## Severity Classification Framework

| Classification        | Definition                                                                                                                                                      | Typical Response                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **COMPLIANT**         | Satisfies applicable CAP/BCAP Code rules and supporting law. No action required.                                                                                | Document for audit trail                                                                       |
| **ADVISORY**          | Minor or technical issue; unlikely to result in upheld ASA ruling but creates complaint risk or could be improved.                                              | Address at next creative refresh                                                               |
| **NON-COMPLIANT**     | Breach of CAP or BCAP Code likely to result in upheld ASA ruling if complained about. Must be amended before publication or immediately withdrawn and amended.  | Amend before publication; escalate to legal/compliance                                         |
| **CRITICAL EXPOSURE** | Breach of primary legislation or DMCCA 2024 per se prohibited practice. Risk of Trading Standards referral, CMA enforcement, FCA action, or criminal liability. | Immediate withdrawal; involve external legal counsel; consider proactive regulatory engagement |

---

## Prioritisation Framework

**Tier 1 — IMMEDIATE** (act before the ad continues running or upon discovery):

- All CRITICAL EXPOSURE findings
- NON-COMPLIANT findings for live ads where consumer harm is ongoing
- Missing financial promotion approval (FSMA s.21 breach)
- Tobacco advertising prohibition breach
- Any per se prohibited practice under DMCCA 2024 Schedule 20

**Tier 2 — NEAR-TERM** (amend before next publication or within 30 days):

- NON-COMPLIANT findings for pre-clearance reviews (must fix before publication)
- NON-COMPLIANT findings for scheduled re-runs or campaign extensions
- Green claims without adequate substantiation (proactive amendment before ASA complaint)
- Influencer disclosure failures for ongoing campaigns (instruct influencers immediately)

**Tier 3 — BACKGROUND** (address at next creative refresh):

- ADVISORY findings
- Technical improvements to disclosure placement or emphasis
- Substantiation record-keeping improvements
- PECR consent record clean-up for existing marketing lists

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any finding. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                  | Fail Action                          |
| -------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **Source**     | Every legal claim cites a specific CAP/BCAP Code rule, statute, or ASA ruling                                         | Add citation or mark "[UNVERIFIED]"  |
| **Format**     | All CAP/BCAP Code citations use consistent rule numbering (e.g., "CAP Code Rule 3.7")                                 | Fix format                           |
| **Currency**   | Every cited provision confirmed against current CAP Code edition; ASA rulings post-date 2022                          | Flag "[CHECK CURRENCY]"              |
| **Domain**     | Analysis stays within advertising law scope — no general contract, IP, or employment law drift without flagging scope | Remove or flag out-of-scope analysis |
| **Confidence** | Uncertainty explicitly stated; jurisdiction-specific nuances flagged                                                  | Add confidence qualifier or [VERIFY] |

### Self-Interrogation for CRITICAL EXPOSURE Findings

For any finding classified as CRITICAL EXPOSURE, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**: Does the CRITICAL EXPOSURE classification follow
logically from the cited authority? Is the statutory provision actually applicable to this
advertiser, product, and medium? Would a regulator actually reach this conclusion on these
specific facts?

**Pass 2 — Completeness**: Have all relevant CAP/BCAP Code provisions, statutory instruments,
and regulatory guidance been considered? Are there sector-specific exemptions or carve-outs
that apply?

**Pass 3 — Challenge**: What is the strongest argument against this CRITICAL EXPOSURE
classification? Under what circumstances might a reasonable compliance professional
accept this risk or classify it differently? Does the advertiser have evidence that would
change the outcome?

### Confidence Scoring

| Level        | Range     | Meaning                                                         | Action                                                          |
| ------------ | --------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Clear breach of specific CAP/BCAP Code rule with ASA precedent  | State with confidence                                           |
| **High**     | 0.80-0.94 | Strong basis for finding; minor interpretive uncertainty        | State with brief caveat                                         |
| **Probable** | 0.60-0.79 | Good arguments for finding; ASA may decide differently on facts | State with reasoning and contra-indicators                      |
| **Possible** | 0.40-0.59 | Genuinely uncertain; depends heavily on context                 | Flag for specialist review with both sides of argument          |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative                                         | Do not assert as a finding; flag for background monitoring only |

---

## Anti-Patterns

Do NOT commit these errors when reviewing advertising compliance:

1. **Treating brand organic social as editorial**: All brand posts on owned social media
   accounts that promote products are marketing communications subject to the CAP Code.
   There is no editorial exemption for brand-owned content.

2. **Failing to audit evidence before publication**: CAP Code Rule 3.7 requires evidence
   to be held before publication. Advising a client to "gather evidence after launch" is
   incorrect and useless as a defence in ASA proceedings.

3. **Assuming ASA investigation ends when the ad is withdrawn**: Withdrawing an ad stops
   further consumer harm but does not terminate the ASA investigation. A ruling will still
   be published, creating public precedent. Withdrawal should be considered alongside the
   investigation response, not as a substitute for it.

4. **Confusing CAP and BCAP codes**: The CAP Code (non-broadcast) and BCAP Code (broadcast)
   apply different rules in some areas — particularly children's advertising, alcohol
   scheduling, and health claims. A TV ad cleared by Clearcast under BCAP is not
   automatically compliant with CAP Code for the same ad used online.

5. **Treating CAP Copy Advice as a safe harbour**: CAP's copy advice service is non-binding.
   The ASA can still uphold a complaint against an ad that received a favourable copy
   advice opinion. The advice reduces risk but does not eliminate it.

6. **Applying the "overall impression" test last**: The overall impression of an ad is the
   primary assessment tool. Accurate individual claims can combine to create a misleading
   overall message. Apply the overall impression test first, then verify individual claims.

7. **Ignoring the CMA alongside the ASA**: The CMA has broader statutory enforcement
   powers under DMCCA 2024 and can impose significant financial penalties. The same conduct
   may attract both ASA adjudication (reputational) and CMA enforcement (financial). Do
   not assess ASA risk in isolation for consumer-facing pricing, green claims, or digital
   practices.

8. **Characterising all environmental claims as "mere puffery"**: The ASA and CMA have
   consistently held that environmental claims like "eco-friendly" and "sustainable" are
   objective and require substantiation. Only claims like "we love the planet" without
   any specific factual assertion qualify as non-actionable puffery.

9. **Failing to check the influencer's post after it goes live**: Brands are responsible
   for ensuring their influencers comply with CAP Code disclosure requirements. Issuing
   contractual obligations to influencers without monitoring compliance does not transfer
   regulatory responsibility to the influencer — the brand remains liable.

10. **Missing the Section 2 issue in affiliate marketing**: Affiliate links are a
    commercial relationship. Any content linked to via an affiliate arrangement must be
    labelled as advertising, even if the content creator did not receive direct payment
    for the post itself.

11. **Applying substantiation requirements only to clinical claims**: Substantiation is
    required for any objective claim — performance claims, pricing claims, superlatives,
    comparisons, and environmental claims all require pre-publication evidence.

12. **Overlooking DMCCA 2024 for existing campaigns**: The DMCCA 2024 consumer protection
    provisions came into force on April 6 2025. Campaigns designed and launched before this
    date may now contain per se prohibited practices. Existing campaigns must be audited
    for DMCCA compliance, not just new ones.

13. **Conflating the financial promotion restriction with CAP Code financial advertising
    rules**: FSMA 2000 s.21 is a criminal prohibition on unapproved financial promotions —
    it operates independently of and in addition to the CAP Code's rules on financial
    advertising. An ad can comply with CAP Code but still be an unlawfully approved
    financial promotion under FSMA.

14. **Treating user-generated content (UGC) as outside scope**: UGC promoted (boosted,
    whitelisted, or amplified) by a brand becomes a marketing communication for which the
    brand is responsible. UGC that makes claims the brand could not make directly (e.g.,
    unsubstantiated health claims in consumer testimonials) cannot be promoted.

15. **Ignoring the "before the fold" placement requirement**: Disclosures buried below
    the visible content area on a social media post (requiring the viewer to expand or
    scroll) are not compliant with CAP Code Section 2 disclosure requirements. Disclosures
    must be immediately visible without any additional user action.

16. **Skipping the distance selling check for online advertising**: Many digital ads are
    the first point of consumer contact in a distance-selling transaction. The Consumer
    Contracts Regulations 2013 require material pre-contract information to be accessible
    before contract formation. Ads that fail to link to or include this information create
    regulatory exposure.

17. **Assuming B2B advertising is wholly unregulated**: Some restrictions apply to B2B
    advertising (BPRs for comparative advertising, general fraud and misrepresentation
    law). The more relaxed consumer protection rules do not make B2B advertising a
    regulatory-free zone.

18. **Underestimating proactive ASA monitoring**: The 2023 ASA Annual Report showed that
    92% of ad removals resulted from ASA's own proactive monitoring (AI-assisted), not
    from public complaints. Compliance cannot rely on the low probability of a consumer
    complaint — the ASA is actively searching for non-compliant content.

---

## Writing Standards

Apply these standards before delivering any output:

1. **Lead with the classification**: State COMPLIANT / ADVISORY / NON-COMPLIANT /
   CRITICAL EXPOSURE at the start of each finding — do not bury the headline in analysis.

2. **Cite the specific rule**: Every finding must reference the applicable CAP/BCAP Code
   rule number, statute, or ASA ruling. "Section 3" is not specific enough; "CAP Code
   Rule 3.7 (substantiation)" is.

3. **State the required action precisely**: "Add disclosure" is not actionable; "Add '#AD'
   label in the first line of the post, before any hashtags or additional text, visible
   without expanding the post" is.

4. **One finding, one issue**: Do not bundle multiple compliance failures into a single
   finding. Each issue should be separately identified and classified.

5. **Active voice**: "The ad does not disclose the commercial relationship" rather than
   "The commercial relationship has not been disclosed."

6. **Plain language for remediation steps**: Legal remediation steps should be expressible
   in plain language that a marketing team can implement. Where technical legal language
   is necessary, provide a plain-language explanation alongside.

7. **No false certainty**: Where a finding is at Confidence level "Probable" or below,
   say so explicitly — "This is likely to be NON-COMPLIANT based on ASA precedent, but
   the outcome may vary depending on [specific factor]."

8. **Verify before delivering**: Run the 5 Citation Quality Gates before sending any
   analysis. Do not deliver a finding that fails a Quality Gate — revise first.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for recent ASA rulings on the specific claim type, sector, or advertiser involved
- Retrieve current CAP Code and BCAP Code provisions for the identified rules
- Search for CMA enforcement actions relevant to the product sector or claim type
- Search for ICO enforcement decisions relevant to PECR or UK GDPR issues
- Search for relevant FCA guidance if financial promotions are involved
- Save search results to `/tmp/legalcode-uk-ad-compliance.md` for use throughout the review
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all ASA ruling citations and statutory references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Recommend that the user verify key citations against asa.org.uk, legislation.gov.uk,
  and gov.uk/cma before acting on findings
- Focus the assessment on structural compliance issues (disclosure, overall impression,
  substantiation framework) rather than specific ASA ruling precedent

**Clearcast pre-clearance** (TV advertising):

- If the ad is for broadcast TV, recommend Clearcast pre-clearance before production
- Certain categories require specific Clearcast pre-vetting: financial services, gambling,
  alcohol, food and nutrition, medicines

**CAP Copy Advice Service** (non-broadcast):

- For high-risk claims (health, environmental, comparative, financial), recommend obtaining
  CAP Copy Advice before publication
- Note: standard free advice moving to 3-5 working day turnaround from late April/May 2026;
  express paid service available for faster response
- Advice is non-binding but is a meaningful risk-reduction step

---

## Localization Notes

**England and Wales vs. UK**: The CAP Code applies across all four nations of the UK.
Enforcement referrals may vary: Trading Standards England and Wales enforce CPUTRs and
consumer protection law; Trading Standards Scotland operates separately; Consumer Council
for Northern Ireland handles NI consumer issues.

**Scotland**: Scottish law applies to contracts and some civil remedies; the CAP and BCAP
Codes apply UK-wide. ASA adjudications apply UK-wide.

**Northern Ireland**: Protocol/post-Brexit arrangements may affect some product-specific
rules where EU alignment continues to apply [VERIFY: specific sectors including food
standards]. Consumer protection enforcement via CCNI.

**Non-UK advertisers targeting UK consumers**: The CAP Code applies regardless of the
advertiser's location. Enforcement against non-UK advertisers may be through platform
pressure, EASA cross-border mechanisms, or Trading Standards referral for criminal law
breaches.

---

## Output Format Template

Use this template to structure the final compliance assessment:

```markdown
# UK Advertising Compliance Assessment

**Date**: [YYYY-MM-DD]
**Ad/Campaign**: [Name or description]
**Medium**: [CAP Code / BCAP Code / Both]
**Product/Service Sector**: [Sector]
**Target Audience**: [Description]
**Prepared by**: AI-assisted review — requires qualified legal professional review

---

## Executive Summary

**Overall Compliance Status**: [COMPLIANT / ADVISORY / NON-COMPLIANT / CRITICAL EXPOSURE]
**Number of Findings**: [X] Critical Exposure / [X] Non-Compliant / [X] Advisory / [X] Compliant
**Immediate Action Required**: [Yes / No — brief description if yes]

### Top Priority Issues

1. [Most critical finding — one sentence]
2. [Second most critical finding]
3. [Third most critical finding]

---

## Compliance Findings

### Finding 1: [Short descriptive title]

**Area**: [Ad Recognition / Misleading Advertising / Pricing / Green Claims / etc.]
**Classification**: [COMPLIANT / ADVISORY / NON-COMPLIANT / CRITICAL EXPOSURE]
**Priority**: [IMMEDIATE / NEAR-TERM / BACKGROUND]
**Confidence**: [Definite / High / Probable / Possible / Unlikely] ([0.00-1.00])

**Issue**: [One-paragraph description of the compliance issue, referencing the specific
ad content and the applicable rule]

**Applicable Rule**: [CAP Code Rule X.XX; and/or BCAP Code Rule X.XX; and/or Statute/
Regulation; and/or DMCCA 2024 Schedule 20 item XX]

**Evidence / ASA Precedent**: [Relevant ASA rulings or CMA guidance — mark [VERIFY] if
not confirmed via legalcode-mcp]

**Required Action**: [Specific steps to remedy the issue]

**Fallback Position**: [Alternative claim or approach that can be used immediately while
full remediation is prepared]

---

### Finding 2: [Continue for each finding]

---

## Remediation Roadmap

### IMMEDIATE Actions (act now)

| #   | Finding             | Action            | Owner                    |
| --- | ------------------- | ----------------- | ------------------------ |
| 1   | [Finding reference] | [Specific action] | [Legal/Marketing/Agency] |

### NEAR-TERM Actions (within 30 days / before next publication)

| #   | Finding             | Action            | Deadline          |
| --- | ------------------- | ----------------- | ----------------- |
| 1   | [Finding reference] | [Specific action] | [Date or trigger] |

### BACKGROUND Actions (next creative refresh)

| #   | Finding             | Action            | Notes     |
| --- | ------------------- | ----------------- | --------- |
| 1   | [Finding reference] | [Specific action] | [Context] |

---

## Clearance Recommendations

| Service             | Recommended?     | Reason   |
| ------------------- | ---------------- | -------- |
| CAP Copy Advice     | [Yes / No]       | [Reason] |
| Clearcast (TV)      | [Yes / No / N/A] | [Reason] |
| Radiocentre (Radio) | [Yes / No / N/A] | [Reason] |

---

## Glass Box Audit Trail

[See YAML template below]
```

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-uk-advertising-compliance"
  mode: "Advertising Compliance Review"
  jurisdiction: "England and Wales (CAP Code UK-wide)"
  ad_material: "[Description of material reviewed]"
  medium: "[CAP / BCAP / Both]"
  sector: "[Product/service sector]"
  target_audience: "[Audience description]"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "/tmp/legalcode-uk-ad-compliance.md / Not created"
  primary_codes_applied:
    - "CAP Code [edition/date]"
    - "BCAP Code [edition/date]"
    - "DMCCA 2024 (in force April 6 2025)"
    - "[Other applicable instruments]"
  sector_specific_instruments: "[List if applicable]"
  total_findings: "[N]"
  findings_by_severity:
    critical_exposure: "[N]"
    non_compliant: "[N]"
    advisory: "[N]"
    compliant: "[N]"
  citations_verified: "[N] VERIFIED / [N] UNVERIFIED [VERIFY]"
  quality_score: "[X]/40"
  completeness: "18/18 elements"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "ASA adjudications are fact-specific; this analysis does not guarantee the outcome
      of any specific complaint or investigation"
    - "CAP Code and BCAP Code rules are periodically updated; verify currency before use"
    - "Sector-specific regulations (FCA, MHRA, UKGC) require specialist regulatory review
      in addition to CAP/BCAP Code analysis"
    - "[Any other scope limitations or assumptions]"
  reviewer:
    "AI-assisted — requires review by a qualified advertising law specialist
    before reliance"
```

---

## Provenance

Legalcode original synthesis (2026-03-22). Created from deep legal research across:
ASA/CAP Code current edition and AdviceOnline guidance; BCAP Code; CMA Green Claims Code
and DMCCA 2024 consumer protection provisions (in force April 6 2025); Consumer
Contracts (Information, Cancellation and Additional Charges) Regulations 2013; BPRs 2008;
PECR 2003; FSMA 2000 s.21 and FCA financial promotion rules; ASA 2023 Annual Report
enforcement data; ASA adjudication precedents (2022-2026 including Simba Sleep, Origin
Mattress, TUI, Air France-KLM, Lufthansa, Mazda, Innocent Health, Huel, Jake Quickenden,
Chloe Ferry, Charlotte Tilbury); CMA enforcement actions (ASOS/Boohoo/Asda greenwashing
2024; Ticketmaster dynamic pricing 2025); Clearcast and Radiocentre pre-clearance
procedures; CAP October 2025 environmental claims guidance; DMCCA 2024 Schedule 20
per se unfair practices. No pre-existing skill imported or adapted. Quality bar calibrated
against `legalcode-uk-fca-regulatory-compliance` and `legalcode-contract-review` reference
standards.
