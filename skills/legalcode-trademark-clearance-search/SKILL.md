---
name: legalcode-trademark-clearance-search
description: Conducts comprehensive trademark availability searches including identical mark searches,
  phonetic equivalents, visual similarity analysis, and conceptual similarity assessment across USPTO
  TESS, EUIPO TMView, WIPO Global Brand Database, UKIPO, IP Australia, and IP India databases plus common
  law sources. Use when clearing a new brand name, logo, slogan, or trade dress before filing, launching
  a product, or expanding into new markets.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Conducts comprehensive trademark availability searches including identical mark searches, phonetic equivalents, visual similarity analysis, and conceptual similarity assessment across USPTO TESS, EUIPO TMView, WIPO Global Brand Database, UKIPO, IP Australia, and IP India databases plus common law sources. Applies likelihood of confusion analysis using DuPont factors (sight, sound, meaning, commercial impression, channels of trade, consumer sophistication, mark fame). Evaluates descriptiveness/genericness risks, surname doctrine, geographic marks, and acquired distinctiveness arguments. Covers goods/services classification strategy across Nice Classification 45 classes (NCL 13-2026). Produces clearance opinion with risk rating (CLEAR/CAUTION/BLOCKED) and alternative mark recommendations. Use when clearing a new brand name, logo, slogan, or trade dress before filing, launching a product, or expanding into new markets. Jurisdiction-agnostic methodology with [JURISDICTION-SPECIFIC] markers for US, EU, UK, AU, and IN enforcement variance.


# Legalcode Trademark Clearance Search

> **Disclaimer**: This skill provides a framework for AI-assisted trademark clearance
> research. It does not constitute legal advice and does not substitute for a professional
> trademark search conducted by a licensed trademark attorney or agent. All outputs should
> be reviewed by a qualified intellectual property professional licensed in the relevant
> jurisdiction before relying on them for filing, adoption, or enforcement decisions. Laws
> change; registry data changes daily; verify current status against authoritative sources
> before use. Statutory and case law references cited from AI training data carry hallucination
> risk — verify against authoritative primary sources before relying on them.

## Purpose and Scope

This skill conducts systematic trademark clearance searches and produces a comprehensive
availability assessment across registered trademark databases and common-law sources. It
identifies potentially conflicting marks, evaluates likelihood of confusion, assesses
distinctiveness risks, and delivers a risk-classified clearance opinion with actionable
recommendations.

**Covers:**

- Multi-database registered mark searches (USPTO TESS, EUIPO TMView, WIPO Global Brand
  Database, UKIPO, IP Australia, IP India, and selected national registers)
- Phonetic, visual, and conceptual similarity analysis for each conflicting mark found
- Likelihood of confusion assessment using the DuPont 13-factor framework (US) and
  equivalent multi-factor tests for EU, UK, AU, and IN
- Distinctiveness spectrum assessment (fanciful → arbitrary → suggestive → descriptive →
  generic) with registrability risk scoring
- Special doctrine analysis: surname doctrine, geographic marks, color trademarks,
  sound marks, trade dress, and non-traditional marks
- Nice Classification goods/services strategy and adjacent-class risk analysis
- Common law and unregistered mark research (domain names, business name registrations,
  social media, internet use evidence)
- Priority analysis: first-to-use vs. first-to-file systems by jurisdiction
- Alternative mark recommendations if the proposed mark is blocked
- Clearance opinion with CLEAR / CAUTION / BLOCKED risk rating

**Does not:**

- Replace a professional trademark search conducted by a licensed IP attorney or search
  firm with access to proprietary databases
- Provide legal advice or constitute an attorney-client communication
- Cover design/logo clearance beyond descriptive analysis (device mark searches require
  specialized design code tools such as the USPTO Design Search Code Manual)
- Guarantee registrability or freedom-to-use — only a professional can provide that opinion
- Conduct watch services or ongoing monitoring after initial clearance

**Complementary skills:** Use alongside `legalcode-contract-review` when reviewing
licensing agreements for the cleared mark, and `legalcode-compliance-risk-assessment` when
clearing a mark as part of a broader M&A or regulatory compliance workflow.

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic in methodology. The proposed mark's intended filing
jurisdictions and use territories determine which databases and legal standards apply.

[JURISDICTION-SPECIFIC] **US**: Likelihood of confusion governed by 15 U.S.C. § 1052(d)
(Lanham Act § 2(d)). The TTAB applies the 13-factor DuPont test (_In re E.I. du Pont de
Nemours & Co._, 476 F.2d 1357 (C.C.P.A. 1973)). First-to-use system — prior commercial
use establishes trademark rights independent of registration. Common law rights coexist
with federal registration.

[JURISDICTION-SPECIFIC] **EU**: Relative grounds for refusal under EUTMR Art. 8(1)(b)
require "likelihood of confusion including association" with an earlier mark. The EUIPO
applies a three-part similarity test (visual, phonetic, conceptual) per _SABEL BV v Puma
AG_ (C-251/95) and _Lloyd Schuhfabrik Meyer & Co GmbH v Klijsen Handel BV_ (C-342/97).
Reputation marks may also block under EUTMR Art. 8(5). First-to-file system with coexistence
provisions for prior unregistered marks with repute.

[JURISDICTION-SPECIFIC] **UK**: Post-Brexit, UK Trade Marks Act 1994 governs. Likelihood
of confusion test mirrors EU law but applies independently. Passing off (goodwill +
misrepresentation + damage) protects unregistered marks under common law. UKIPO database
searched separately from EUIPO — EUTMs no longer extend to UK for new filings.

[JURISDICTION-SPECIFIC] **AU**: Trade Marks Act 1995 (Cth). Section 44 deceptive similarity
test. Section 120 infringement standard. Australia is first-to-use — prior use creates
common law rights via passing off (s. 18 ACL misleading and deceptive conduct as parallel
remedy). IP Australia database (Australian Trade Mark Online Search System — ATMOSS) is
the primary registered mark database. [VERIFY current status with IP Australia.]

[JURISDICTION-SPECIFIC] **IN**: Trade Marks Act 1999 (India). First-to-use system —
prior use creates rights under common law; registration under the Act gives additional
statutory remedies. IP India (ipindia.gov.in) provides the official public search database.
Section 11 grounds for opposition include likelihood of confusion with earlier registered
marks and well-known marks. [VERIFY current search system status with IP India.]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's context, the workflow pauses and asks when:

- The answer would change the search scope or database selection
- Multiple valid risk-tolerance postures exist and the user's preference matters
- Ambiguity in the proposed mark's use context creates a fork in the analysis
- The priority filing jurisdiction is unclear

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

### Step 1: Accept the Proposed Mark

Accept the proposed mark in any of these formats:

- **Word mark**: Plain text (e.g., "APEX", "QuickServe", "Bright & Bold")
- **Slogan**: Phrase or tagline (e.g., "Just Do It", "Think Different")
- **Logo/device description**: Written description of the visual element (full device
  mark clearance requires specialized design search tools — flag this limitation)
- **Combined mark**: Word + stylized element (search the word element fully; flag device
  element for specialist clearance)
- **Sound/color/trade dress**: Describe the non-traditional mark in detail

If no mark is provided, prompt the user to supply the proposed mark and its intended use.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the search, ask the user (skip questions already answered):

1. **Intended goods/services**: What products or services will the mark be used with?
   Provide as much detail as possible — this determines Nice class selection.
   - _Why this matters_: Trademark rights are class-specific. A mark clear in Class 9
     (software) may be blocked in Class 42 (software-as-a-service). Wrong class selection
     renders the entire search unreliable.

2. **Priority jurisdictions**: Where will you file and where will you use the mark?
   - Options: US only, EU only, UK only, AU only, IN only, US + EU + UK (specify),
     Global Madrid Protocol filing, Other combination
   - _Why this matters_: Each jurisdiction requires a separate registered-mark search.
     A mark clear in the US may be blocked in the EU and vice versa. Post-Brexit, UK
     must be searched separately from EU.

3. **Risk tolerance**: How much trademark risk is acceptable?
   - Options: Zero tolerance (rebrand at any caution flag), Standard commercial
     (accept low-level caution with monitoring strategy), Aggressive adoption (accept
     caution if coexistence likely)
   - _Why this matters_: Determines whether CAUTION findings trigger a stop or a
     monitoring recommendation. Highly risk-averse users should be informed of all
     potential conflicts; aggressive adopters need the most material risks highlighted.

4. **Timeline**: How urgent is this clearance?
   - Options: Urgent (24–48 hours — abbreviated search, flag limitations), Standard
     (1–2 weeks — full database search plus common law), Comprehensive (3–4 weeks —
     full database plus professional search firm engagement)
   - _Why this matters_: Abbreviated searches carry higher miss-risk for common law
     and international marks. The skill should flag all limitations when timeline
     constrains scope.

5. **Existing use**: Is the mark already in use commercially?
   - Options: Not yet used (pre-launch clearance), Already in use in one market
     (expanding), In use globally (retroactive clearance or M&A due diligence)
   - _Why this matters_: Prior commercial use may create common law priority in
     first-to-use jurisdictions (US, AU, IN) or affect opposition standing. M&A
     contexts require different output formatting.

**Proceed with reasonable defaults if user has not specified:**

- Jurisdiction: US primary, with note that international searches are needed before
  global launch
- Risk tolerance: Standard commercial
- Timeline: Standard (full database search; flag common law limitations)

---

### Step 3: Define Goods/Services Classification Strategy

Before searching, establish the precise Nice Classification scope.

#### 3a. Identify Primary Nice Class(es)

Use the Nice Classification (13th Edition, version 2026 — NCL 13-2026, effective
January 1, 2026) to identify every class covering the proposed goods/services.

**Key class groupings for common technology and service marks:**

| Business Type                 | Primary Class(es)  | Common Adjacent Classes                         |
| ----------------------------- | ------------------ | ----------------------------------------------- |
| Software (downloadable)       | Cl. 9              | Cl. 35 (business services), Cl. 42 (SaaS/cloud) |
| SaaS / Cloud services         | Cl. 42             | Cl. 9, Cl. 35, Cl. 38 (telecom)                 |
| Financial services            | Cl. 36             | Cl. 35, Cl. 42                                  |
| Retail (physical)             | Cl. 35             | Cl. covering specific goods sold                |
| E-commerce / marketplace      | Cl. 35             | Cl. 42, Cl. 36                                  |
| Healthcare / medical devices  | Cl. 10             | Cl. 5 (pharma), Cl. 44 (medical services)       |
| Food and beverage             | Cl. 29, 30, 32, 33 | Cl. 35 (retail), Cl. 43 (restaurant)            |
| Clothing / apparel            | Cl. 25             | Cl. 14 (accessories), Cl. 35 (retail)           |
| Legal / professional services | Cl. 45             | Cl. 35, Cl. 42                                  |
| Education / e-learning        | Cl. 41             | Cl. 9 (software), Cl. 42                        |
| Media / entertainment         | Cl. 41             | Cl. 38 (streaming), Cl. 9 (recordings)          |

[JURISDICTION-SPECIFIC: NCL 13-2026] The 2026 revision reclassified several goods and
services. When searching, confirm that legacy class allocations for pre-2026 registrations
are correctly interpreted and that dual-class searching is applied where reclassification
affects the proposed mark's goods/services. [VERIFY current WIPO NCL-2026 class headings
against wipo.int/classifications/nice before finalizing class strategy.]

#### 3b. Document the Search Classes

Record all primary and adjacent classes for the search. For each class:

- State whether it is a **direct class** (the mark will be filed in this class) or an
  **adjacent class** (conflicting marks here could block due to related goods/services)
- Note any NCL 13-2026 reclassification issues

**⟁ CLARIFY** — Present the proposed class strategy to the user:

- "The proposed mark, used for [goods/services], falls primarily in Class [X]. I will
  also search Class [Y] and [Z] as adjacent classes where conflicts could arise due to
  the relatedness of goods/services. Does this scope look correct, or should any classes
  be added or removed?"

---

### Step 4: Execute Registered Mark Database Search

Search each applicable database for the proposed mark and all variations (see Step 5 for
variation methodology). Document every hit before evaluating.

#### 4a. Database Coverage by Jurisdiction

| Jurisdiction      | Primary Database                                | URL                                   | Search Scope                                   |
| ----------------- | ----------------------------------------------- | ------------------------------------- | ---------------------------------------------- |
| **US**            | USPTO TESS (Trademark Electronic Search System) | tmsearch.uspto.gov                    | All live and pending US federal marks          |
| **US**            | USPTO Design Search                             | tmsearch.uspto.gov                    | Design code search for device marks            |
| **US (state)**    | State trademark registers                       | Via Secretary of State websites       | State-level marks not on TESS                  |
| **EU**            | EUIPO TMView                                    | tmdn.org/tmview                       | All EU member state + EUTM marks (75+ offices) |
| **International** | WIPO Global Brand Database                      | branddb.wipo.int                      | Madrid Protocol international registrations    |
| **UK**            | UKIPO Trade Mark Register                       | trademarks.ipo.gov.uk                 | UK national marks + Brexit-equivalent marks    |
| **AU**            | IP Australia ATMOSS                             | search.ipaustralia.gov.au             | Australian trade mark register                 |
| **IN**            | IP India Public Search                          | ipindiaonline.gov.in/trademarkefiling | Indian trade mark register                     |

[JURISDICTION-SPECIFIC] **EU regional notes**: TMView aggregates data from EUIPO plus
individual EU member state offices (INPI France, DPMA Germany, UKIPO [UK], etc.). An EUTM
covers all 27 EU member states from a single filing; a national EU mark covers only that
country. Both types appear in TMView.

[JURISDICTION-SPECIFIC] **Madrid Protocol**: WIPO Global Brand Database covers
international registrations designating member countries under the Madrid Protocol. If
the proposed mark may be filed via Madrid, search this database in parallel with national
registers. Coverage includes 130+ member territories.

#### 4b. Search Queries to Run (for each database)

For each database, run the following query types:

**Level 1 — Identical mark search**

- Exact proposed mark text
- Proposed mark with punctuation stripped
- Proposed mark with spaces removed (e.g., "QuickServe" → "QUICKSERVE", "QUICK SERVE")
- Plural/singular variants

**Level 2 — Truncated/wildcard search**

- Leading truncation: `*APEX` (marks ending with the term)
- Trailing truncation: `APEX*` (marks beginning with the term)
- Mid-word: `*APEX*` (marks containing the term)

**Level 3 — Phonetic variants** (see Step 5 for full methodology)

- Common misspellings and sound-alikes
- Common letter substitutions (F/PH, C/K/Q, I/Y, S/Z, etc.)

**Level 4 — Status filter**

- Always include: Live/Pending marks
- Consider: Abandoned marks where use evidence may create common law rights
- Expired marks: Check for renewal gaps that may affect rights

Record all hits before filtering. Do not pre-filter during search — evaluate all results
in Step 5.

---

### Step 5: Phonetic, Visual, and Conceptual Similarity Analysis

For every mark found in Step 4, and for every variation of the proposed mark, apply the
three-dimensional similarity analysis used by trademark offices worldwide.

#### 5a. Phonetic Similarity Analysis

Phonetic similarity exists when two marks sound alike when spoken aloud, regardless of
spelling differences.

**Systematic variation methodology:**

| Original Element   | Phonetic Variations to Search             |
| ------------------ | ----------------------------------------- |
| F sound            | F, PH, GH (as in "tough")                 |
| K sound            | C, K, Q, CK, QU                           |
| S sound            | S, Z, C (soft), SS                        |
| I sound            | I, Y, EY                                  |
| AE/EE sound        | AE, E, EE, EA, EI                         |
| OU/OO sound        | O, OU, OO, EW, UE                         |
| Silent letters     | Drop silent letters; add unnecessary ones |
| Prefix/suffix      | UN-, RE-, -ER, -OR, -LY, -ING variations  |
| Double letters     | QUICK/QUIK/QUIKK; strip doubles           |
| Word transposition | "Quick Serve" vs. "Serve Quick"           |

**Phonetic risk indicators:**

- Same or very similar stressed syllable pattern: HIGH risk
- First syllable identical: MEDIUM-HIGH risk (first syllable carries most confusion weight)
- Last syllable identical only: LOW-MEDIUM risk
- Completely different sound pattern: LOW risk

#### 5b. Visual Similarity Analysis

Visual similarity is assessed by overall commercial impression when the marks are seen,
not a letter-by-letter comparison.

**Assessment criteria:**

- Length and structure (short marks have less room for difference)
- Dominant element similarity (what does the eye focus on?)
- Beginning of the mark (consumers remember beginnings)
- Stylization (if any — assess separately for word vs. design elements)
- Color (if claimed as a feature of the mark)
- Overall commercial impression when marks are seen side by side and in isolation

**Visual similarity scale:**

- **Identical/near-identical**: Same word(s), letter arrangement, and style → HIGH risk
- **Dominant element shared**: Key word shared; minor differences → HIGH-MEDIUM risk
- **Similar structure**: Different words but same visual pattern/length/style → MEDIUM risk
- **Minor visual overlap**: Partial word sharing only → LOW-MEDIUM risk
- **Clearly different**: Different length, structure, dominant elements → LOW risk

#### 5c. Conceptual Similarity Analysis

Conceptual similarity exists when two marks convey the same or closely related idea,
even if they look and sound different.

**Assessment method:**

1. What concept/meaning does the proposed mark convey?
2. What concept/meaning does each potentially conflicting mark convey?
3. Are those concepts the same, closely related, or entirely different?
4. Would a consumer associate the two concepts with the same source?

**Examples of conceptual similarity:**

- APPLE and PEAR for computer products → Conceptually similar (fruit category)
- SUNRISE and DAWN for hotel services → Conceptually similar (time of day/light)
- PINNACLE and APEX for business services → Conceptually similar (summit/highest point)
- ROYAL and CROWN for luxury goods → Conceptually similar (monarchy/prestige)
- LIGHTNING and THUNDER for energy drinks → Conceptually similar (storm elements)

**Translations and foreign language equivalents:**

- Check translations of the proposed mark in languages relevant to the target market
- A mark identical in translation to a registered mark may be blocked
- [JURISDICTION-SPECIFIC: EU] EUIPO examines cross-language conceptual similarity
  for EU markets, particularly for widely understood European languages

---

### Step 6: Common Law and Unregistered Mark Search

Registered mark searches miss rights created through use. For first-to-use jurisdictions
(US, AU, IN especially), common law searches are as important as registry searches.

#### 6a. Domain Name Search

Search major domain registrars and WHOIS databases for:

- `proposedmark.com` (most critical for US common law evidence)
- `proposedmark.net`, `.org`, `.co`, `.io`
- Country-code TLDs for target markets (`.co.uk`, `.com.au`, `.in`, `.eu`, `.de`, `.fr`)
- Significant variations and typo domains

**Interpretation:** Active use of the domain in commerce (not mere registration) creates
potential common law rights in the US, UK, and Australia. Domain registration alone is
not trademark use but may indicate intent to use.

#### 6b. Social Media Handle Search

Search major platforms for the proposed mark:

- Instagram, TikTok, YouTube, X (Twitter), Facebook, LinkedIn
- Focus on accounts with actual commercial activity, not just parked handles
- Document: Platform, handle, follower count, activity level, goods/services offered

#### 6c. Business Name / Company Registration Search

Search business registration databases for:

- [JURISDICTION-SPECIFIC: US] State Secretary of State databases (all target states)
- [JURISDICTION-SPECIFIC: UK] Companies House (companyregistrations.co.uk)
- [JURISDICTION-SPECIFIC: AU] ASIC Business Names Register (connectonline.asic.gov.au)
- [JURISDICTION-SPECIFIC: EU] National company registries of target member states
- [JURISDICTION-SPECIFIC: IN] MCA21 Company/LLP database (mca.gov.in)

**Note:** Business name registration ≠ trademark rights, but it evidences commercial use
and intent. A business operating under a name may have common law trademark rights even
without trademark registration.

#### 6d. Internet Use and Trade Press Search

Conduct targeted internet searches for commercial use of the proposed mark:

- `"[proposed mark]" site:[market-specific platform]`
- `"[proposed mark]" + [relevant goods/services term]`
- Search trade publications, press releases, product review sites
- Check Google Shopping for product listings

**Document all findings:** Screenshot (or note URL) of commercial use evidence.

---

### Step 7: Distinctiveness and Registrability Analysis

Independent of conflict, assess whether the proposed mark is inherently registrable.

#### 7a. Distinctiveness Spectrum Assessment

Apply the five-point distinctiveness spectrum to the proposed mark in relation to the
proposed goods/services:

| Category        | Definition                                                            | Clearance Risk                        | Registration Path                                                                                        |
| --------------- | --------------------------------------------------------------------- | ------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Fanciful**    | Invented word with no prior meaning (e.g., KODAK, XEROX)              | LOWEST — strongest protection         | Inherently distinctive; immediate registration                                                           |
| **Arbitrary**   | Real word applied to unrelated goods (e.g., APPLE for computers)      | LOW — broad protection scope          | Inherently distinctive; immediate registration                                                           |
| **Suggestive**  | Suggests but does not directly describe (e.g., NETFLIX for streaming) | LOW-MEDIUM — good protection          | Inherently distinctive; immediate registration                                                           |
| **Descriptive** | Directly describes a feature, quality, or characteristic              | HIGH — weak without secondary meaning | Not inherently distinctive; requires proof of acquired distinctiveness (5+ years use or survey evidence) |
| **Generic**     | The common name for the goods/services                                | ABSOLUTE — cannot be trademarked      | Unregistrable; recommend full rebrand                                                                    |

**⟁ CLARIFY** — If the mark falls in the descriptive or potentially generic range:

- "The proposed mark appears to be [descriptive/possibly generic] in relation to [goods/services].
  This significantly increases refusal risk. Would you like to: (a) proceed with the search
  and note descriptiveness risk; (b) consider alternative marks from the suggestive/arbitrary
  tier; or (c) evaluate acquired distinctiveness arguments (long use + survey evidence)?"

#### 7b. Surname Doctrine Analysis

[JURISDICTION-SPECIFIC: US] A mark that is primarily merely a surname faces rejection
under 15 U.S.C. § 1052(e)(4) unless the applicant proves acquired distinctiveness.
_In re Hutchinson Technology Inc._, 852 F.2d 552 (Fed. Cir. 1988). The TTAB examines:

- Rarity of the surname in the US
- Whether the mark is the surname of anyone associated with the applicant
- Whether the mark has any other recognized meaning
- Whether the proposed mark has the structure/appearance of a surname

[JURISDICTION-SPECIFIC: EU/UK] Similar surname doctrine applies under EUIPO/UKIPO
examination guidelines. [VERIFY current guidelines at euipo.europa.eu.]

**Assessment:** Check the proposed mark against common surname databases. If it is a
common or recognizable surname with no other meaning, flag as CAUTION for surname
doctrine risk.

#### 7c. Geographic Mark Analysis

Marks that are primarily geographically descriptive or misdescriptive face registrability
barriers:

[JURISDICTION-SPECIFIC: US] 15 U.S.C. § 1052(e)(2): Primarily geographically descriptive
marks are refused unless secondary meaning is shown. § 1052(e)(3): Primarily geographically
misdescriptive marks are refused without exception.

[JURISDICTION-SPECIFIC: EU] EUTMR Art. 7(1)(c): Marks consisting exclusively of
indications of geographic origin are absolute grounds for refusal.

**Common geographic risk patterns:**

- Single city/region name used for products from that area (descriptive → registrable
  with secondary meaning in US; likely refused in EU)
- Single city/region name used for products NOT from that area (misdescriptive → higher
  risk in both US and EU)
- Generic country/region + product type (e.g., CALIFORNIA WINES) → HIGH refusal risk

#### 7d. Non-Traditional Mark Special Assessment

For color, sound, shape, or trade dress marks, flag additional clearance complexity:

- **Color marks**: Functionality doctrine bars protection for functional colors. Requires
  proof of acquired distinctiveness. [JURISDICTION-SPECIFIC: US] _Qualitex Co. v. Jacobson
  Products Co._, 514 U.S. 159 (1995). [VERIFY.]
- **Sound marks**: Must be capable of distinguishing source. Examples: NBC chimes (US),
  MGM lion roar (US). Requires proof of distinctiveness.
- **Trade dress**: Product design protectable only with secondary meaning per _Wal-Mart
  Stores, Inc. v. Samara Brothers, Inc._, 529 U.S. 205 (2000) [VERIFY]. Product packaging
  may be inherently distinctive.
- **Shape marks**: Functionality doctrine applies. Non-functional distinctive shapes
  may be protected. [JURISDICTION-SPECIFIC: EU] Shapes that result from the nature of
  the goods or are necessary to obtain a technical result are excluded — EUTMR Art. 7(1)(e).

---

### Step 8: Likelihood of Confusion Assessment

For each potentially conflicting mark identified in Steps 4–6, apply the likelihood of
confusion framework appropriate to the target jurisdiction.

#### 8a. DuPont 13-Factor Analysis (US)

_In re E.I. du Pont de Nemours & Co._, 476 F.2d 1357 (C.C.P.A. 1973). Not all factors
apply in every case; weight each relevant factor proportionately.

**Apply the DuPont factors for each RED/CAUTION finding:**

| Factor                                | Description                                             | Weight              | Assessment                                                             |
| ------------------------------------- | ------------------------------------------------------- | ------------------- | ---------------------------------------------------------------------- |
| **1. Similarity of marks**            | Visual, phonetic, conceptual similarity                 | **HIGHEST**         | [Assess per Step 5 analysis]                                           |
| **2. Relatedness of goods/services**  | How similar or related are the goods/services?          | **HIGHEST**         | [Assess per Step 3 class strategy]                                     |
| **3. Trade channels**                 | Do the goods/services travel through same channels?     | High                | [Retail vs. direct; online vs. brick-and-mortar]                       |
| **4. Consumer sophistication**        | Are buyers careful, sophisticated purchasers?           | High                | [Professionals vs. general public; price point]                        |
| **5. Fame of prior mark**             | Is the senior mark famous/well-known?                   | Very High if famous | [Search for famous mark status — high marketing spend, ubiquitous use] |
| **6. Similar marks in field**         | Are there many similar marks in this field?             | Medium              | [Crowded field = narrower scope of protection for each]                |
| **7. Actual confusion**               | Evidence of actual consumer confusion                   | High when present   | [Rare in clearance — search litigation records]                        |
| **8. Length of concurrent use**       | How long have both marks been used simultaneously?      | Medium              | [Longer coexistence = lower confusion likelihood]                      |
| **9. Variety of goods/services**      | Range of goods/services on which marks are used         | Medium              | [Broader senior mark use = greater risk]                               |
| **10. Market proximity**              | How close are the respective markets?                   | Medium              | [Same city vs. different regions]                                      |
| **11. Right to exclude**              | Does senior mark owner have exclusive right to exclude? | Medium              | [Incontestable status, disclaimers, limitations]                       |
| **12. Extent of potential confusion** | Scale of potential consumer confusion                   | Medium              | [Small vs. large market segment]                                       |
| **13. Any other established fact**    | Other relevant evidence                                 | Low-Medium          | [Industry norms, prior consent agreements]                             |

**Critical interaction:** Factors 1 and 2 (mark similarity × goods/services relatedness)
carry the most weight and operate on a sliding scale. A highly similar mark requires
less goods/services overlap to trigger confusion; highly related goods/services require
less mark similarity. [VERIFY with *In re Chatam Int'l*, 380 F.3d 1340 (Fed. Cir. 2004).]

#### 8b. EUIPO Global Appreciation Test (EU)

_SABEL BV v Puma AG_ (C-251/95); _Lloyd Schuhfabrik Meyer & Co. GmbH v Klijsen Handel BV_
(C-342/97); _Canon Kabushiki Kaisha v MGM Inc._ (C-39/97). [VERIFY current status.]

Key principles:

- **Global appreciation**: The likelihood of confusion must be assessed globally, taking
  into account all relevant factors, not individual features in isolation
- **Interdependence**: A lesser degree of similarity between the marks may be offset by
  a greater degree of similarity between the goods/services, and vice versa
- **Average consumer**: The standard is the notional average consumer who is reasonably
  well-informed and reasonably observant and circumspect
- **First impression**: The imperfect recollection of the consumer is the operative standard
  (marks are not compared side-by-side in the marketplace)
- **Dominant elements**: More weight given to dominant elements than to descriptive or
  weak elements

[JURISDICTION-SPECIFIC: EU] If the senior mark has **enhanced distinctiveness** through use
(reputation), the scope of protection is broader. Document evidence of reputation when
assessing highly distinctive senior marks.

#### 8c. UK Passing Off Test (UK common law)

Even where no registered mark conflict exists, UK common law passing off requires:

1. **Goodwill**: The senior mark has goodwill (commercial reputation) attached to the mark
2. **Misrepresentation**: The proposed mark's use would misrepresent to consumers that
   goods/services originate from or are associated with the senior mark owner
3. **Damage**: The misrepresentation would or is likely to cause damage to the goodwill

_Reckitt & Colman Products v Borden Inc._ [1990] 1 All ER 873 (Jif Lemon case). [VERIFY.]

[JURISDICTION-SPECIFIC: AU] Parallel framework under Australian Consumer Law s. 18
(misleading and deceptive conduct) and common law passing off.

#### 8d. Likelihood of Confusion — Classification Decision

After applying the appropriate test, classify each potentially conflicting mark:

**BLOCKED** (RED): High likelihood of confusion — proceed would create material legal risk

- DuPont factors 1 and 2 both point strongly to confusion, OR
- Factor 5 (famous mark) applies and goods/services are not clearly distinct, OR
- Phonetic/visual/conceptual similarity is very high and goods/services are identical/closely related

**CAUTION** (YELLOW): Moderate likelihood of confusion — proceed with caution

- DuPont factors mixed: some point to confusion, others counsel against it, OR
- Similar marks but in different (though adjacent) Nice classes, OR
- Phonetic or conceptual similarity present but goods/services are in different markets, OR
- Senior mark has limited geographic scope, weak distinctiveness, or limited use

**CLEAR** (GREEN): Low or no likelihood of confusion

- DuPont factors predominantly counsel against confusion, OR
- Marks clearly differ on multiple dimensions (sound, appearance, meaning), OR
- Goods/services clearly in different markets with no reasonable expectation of overlap

---

### Step 9: Generate Clearance Opinion

Synthesize all findings into a structured clearance opinion with the following components.

#### 9a. Overall Risk Rating

Assign one of three overall clearance ratings based on the highest-risk finding:

| Rating         | Label                                     | Definition                                                                            | Recommended Action                                                                     |
| -------------- | ----------------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| ✅ **CLEAR**   | Available — proceed to file               | No material conflicts found; mark appears available for registration and use          | Register promptly to establish filing date priority                                    |
| ⚠️ **CAUTION** | Proceed with monitoring                   | Potential conflicts exist but do not clearly block; risk manageable with strategy     | Document use; consider coexistence agreement; implement watch service; consult counsel |
| 🚫 **BLOCKED** | High risk — do not adopt without strategy | Material conflict(s) found; adoption creates significant infringement/opposition risk | Consult trademark counsel; consider alternatives; do not adopt without legal clearance |

If any single finding is BLOCKED, the overall rating is BLOCKED regardless of other results.
If no BLOCKED findings but one or more CAUTION findings exist, overall rating is CAUTION.
Only if all findings are CLEAR does the overall rating become CLEAR.

#### 9b. Alternative Mark Recommendations

If the proposed mark is BLOCKED or high CAUTION, provide 3–5 alternative mark suggestions:

**Alternative generation framework:**

1. **Fanciful alternatives**: Propose 2 invented words with similar phonetics/feel to
   the proposed mark but no prior registry conflicts
2. **Arbitrary alternatives**: Propose 2 real words applied unexpectedly to the goods/services
3. **Suggestive alternatives**: Propose 1–2 marks that suggest the key benefit without
   describing it directly
4. **Variant of proposed mark**: Propose a modified version of the proposed mark that
   avoids the specific conflict (prefix, suffix, phonetic shift, secondary word added)

For each alternative, note: distinctiveness level, likely search scope needed, and why
it avoids the blocking conflict.

#### 9c. Priority and Coexistence Strategy

If the mark is CAUTION (not outright BLOCKED), document:

**Coexistence strategy options:**

1. **Consent agreement**: Approach the senior mark owner for a consent letter
   acknowledging the applicant's mark in specified goods/services and territory.
   [JURISDICTION-SPECIFIC: US] USPTO gives weight to consent agreements in examination.
   [JURISDICTION-SPECIFIC: EU] EUIPO can accept co-existence agreements under EUTMR Art. 8(4).
2. **Delimitation agreement**: Both parties agree to restrict use to defined territories
   or goods/services classes.
3. **Coexistence by differentiation**: Adopt distinguishing elements (stylization, logo,
   additional word) that reduce confusion risk.
4. **Watch service**: Monitor the senior mark's status and any enforcement actions.
5. **Selective filing**: File in jurisdictions/classes where CLEAR; defer or abandon
   CAUTION jurisdictions/classes pending strategy.

**Priority claims (first-to-use jurisdictions):**
[JURISDICTION-SPECIFIC: US] Document earliest commercial use date. If prior use predates
conflicting registration, the proposed mark owner may have prior rights in the geographic
area of use. Advise collection and preservation of use evidence.

[JURISDICTION-SPECIFIC: IN] Document earliest use in India. India's first-to-use system
means prior use may override a later-filed registration in trademark opposition proceedings
under Trade Marks Act 1999, Section 11.

---

### Step 10: Quality Verification and Delivery

Before delivering the clearance opinion, run the full quality verification protocol.

#### 10a. Self-Interrogation (for all BLOCKED findings)

Apply 3-pass Self-Interrogation to every BLOCKED finding before finalizing:

**Pass 1 — Conflict Chain Integrity**

- Does the conflict finding follow logically from the search results and similarity analysis?
- Would a trademark examiner at the USPTO/EUIPO/UKIPO actually issue an Office Action
  for this exact conflict?
- Is the DuPont/global appreciation analysis correctly weighted (factors 1 and 2 highest)?

**Pass 2 — Search Completeness**

- Have all relevant databases been searched for this mark/class combination?
- Are there any phonetic, visual, or conceptual variations that were missed?
- Has common law use evidence been adequately considered?
- Are there any registration status issues (abandonment, expiry, limited-use disclaimers)
  that affect the conflict?

**Pass 3 — Severity Challenge**

- What is the strongest argument that coexistence with this senior mark is possible?
- Under what circumstances might a trademark examiner allow the proposed mark despite
  the conflict? (e.g., weak senior mark, different channels, high consumer sophistication,
  geographic separation)
- Is BLOCKED the right classification or should this be CAUTION with conditions?

Outcome: Mark as `self_interrogation: PASS` or `self_interrogation: REVISED — [reason and
revision made]`

#### 10b. Citation Quality Gates

Run these 5 gates before delivering the clearance opinion:

| Gate           | Rule                                                                                   | Fail Action                                              |
| -------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every conflict finding cites the specific mark (Reg. #, WIPO #, or URL)                | Add citation or mark `[UNVERIFIED — counsel to confirm]` |
| **Format**     | All citations follow consistent format (USPTO Reg. #XXXXXXX, WIPO Int'l Reg. #XXXXXXX) | Fix citation format                                      |
| **Currency**   | All registry data verified as current (mark is live, not expired/abandoned/cancelled)  | Flag `[CHECK REGISTRY STATUS — may have changed]`        |
| **Domain**     | Analysis stays within trademark law; no copyright/patent/other IP conflation           | Remove or flag any erroneous non-trademark claims        |
| **Confidence** | Uncertainty stated explicitly for each finding                                         | Add confidence qualifier if missing                      |

#### 10c. Completeness Check

Verify before delivery:

- [ ] All proposed Nice classes searched in all jurisdictions
- [ ] Phonetic, visual, and conceptual analysis conducted for all major conflicts
- [ ] Common law search conducted (or limitations documented)
- [ ] Distinctiveness spectrum assessed for the proposed mark
- [ ] Surname/geographic doctrine checked if applicable
- [ ] Overall risk rating assigned correctly (highest finding drives overall)
- [ ] Alternative marks provided if BLOCKED or high CAUTION
- [ ] Glass Box audit trail complete
- [ ] Writing standards applied (plain language, active voice, specific citations)

---

## Distinctiveness Risk Matrix

Use this matrix to quickly calibrate registrability risk by mark type and goods/services:

| Mark Type                     | Generic Risk   | Descriptive Risk                     | Registrability Outlook                                               |
| ----------------------------- | -------------- | ------------------------------------ | -------------------------------------------------------------------- |
| Invented word (no meaning)    | None           | None                                 | Excellent — file immediately                                         |
| Real word (unrelated meaning) | None           | None                                 | Excellent — file immediately                                         |
| Acronym of real words         | Low-Medium     | Medium (if acronym suggests meaning) | Good — check prior registrations for acronym                         |
| Surname only                  | None           | Low                                  | Moderate — surname doctrine risk; check rarity                       |
| Descriptive word/phrase       | None           | HIGH                                 | Poor — needs 5+ years acquired distinctiveness or heavy use evidence |
| Geographic term               | None           | HIGH if region/product linked        | Poor — geographic mark doctrine; strong evidence needed              |
| Common word for the goods     | HIGH — generic | N/A                                  | Unregistrable — rebrand required                                     |
| Slogan / phrase               | Low-Medium     | Depends on meaning                   | Moderate — must assess descriptiveness; avoid "laudatory" phrases    |

---

## Nice Classification Quick Reference

**Goods (Classes 1–34):**

| Class      | Core Goods                                                   | Common Use Cases           |
| ---------- | ------------------------------------------------------------ | -------------------------- |
| 1–5        | Chemicals, paints, cosmetics, pharma                         | Industrial, health, beauty |
| 9          | Scientific instruments, software (downloadable), electronics | Tech, apps, hardware       |
| 10         | Medical devices                                              | MedTech, health devices    |
| 14, 18, 25 | Jewellery, leather goods, clothing                           | Fashion, accessories       |
| 29–33      | Food, beverages, tobacco                                     | F&B brands                 |
| 34         | Tobacco/smoking products                                     | Tobacco, vaping            |

**Services (Classes 35–45):**

| Class | Core Services                                   | Common Use Cases            |
| ----- | ----------------------------------------------- | --------------------------- |
| 35    | Advertising, business management, retail        | Marketplaces, agencies      |
| 36    | Financial services                              | Fintech, insurance, banking |
| 38    | Telecommunications                              | Streaming, VoIP, internet   |
| 41    | Education, entertainment                        | EdTech, media, events       |
| 42    | Scientific, technological services, SaaS, cloud | Software platforms, R&D     |
| 44    | Medical, veterinary, beauty services            | Clinics, wellness           |
| 45    | Legal, security, personal social services       | Legal tech, security        |

[JURISDICTION-SPECIFIC] **NCL 13-2026**: The 2026 edition reclassified several goods and
services categories. Particularly affected: certain financial technology services (Class 36
vs. 42), downloadable vs. non-downloadable software (Class 9 vs. 42), and streaming media
(Class 41 vs. 38). [VERIFY current class assignments at wipo.int/classifications/nice
before finalizing all class recommendations.]

---

## Priority System Comparison by Jurisdiction

| Jurisdiction | Priority System                 | Key Implication for Clearance                                                                 |
| ------------ | ------------------------------- | --------------------------------------------------------------------------------------------- |
| **US**       | First-to-use                    | Prior commercial use = senior rights even without registration; common law search mandatory   |
| **EU**       | First-to-file (with exceptions) | Earlier filing date = senior rights; check pending applications as carefully as registrations |
| **UK**       | First-to-file + passing off     | Filing date governs registered rights; prior use may support passing off claim                |
| **AU**       | First-to-use                    | Prior use creates common law rights; common law search essential before filing                |
| **IN**       | First-to-use                    | Prior use governs; registration reinforces but not required for rights establishment          |
| **Madrid**   | First-to-file (via WIPO)        | International registration date is priority date for all designated countries                 |

**Paris Convention**: Filing in any Paris Convention member country creates a 6-month
priority window. A US application filed January 1 gives 6-month priority for EU/UK/AU/IN
applications. Flag this window whenever the user has already filed in one jurisdiction —
they may still be within the Paris Convention priority period.

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise the
output before delivering.

| Gate           | Rule                                                                                                                                                                                | Fail Action                                                     |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Source**     | Every conflict finding cites a specific mark registration number, WIPO number, URL, or documented use evidence                                                                      | Add citation or mark `[UNVERIFIED — counsel to confirm source]` |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction (USPTO Reg. #, EUIPO EM, WIPO Int'l Reg. #)                                                             | Fix citation format to match jurisdiction standard              |
| **Currency**   | Every cited registry entry verified as currently live/pending (not expired, cancelled, or abandoned) — unless specifically noting an abandoned mark with residual common law rights | Flag `[CHECK REGISTRY STATUS — data may be stale]`              |
| **Domain**     | Analysis stays within trademark law; does not bleed into copyright, patent, trade secret, or other IP domains without explicitly flagging the distinction                           | Remove or separately flag any non-trademark IP claims           |
| **Confidence** | Uncertainty about any finding is explicitly stated in the output, not hidden                                                                                                        | Add confidence qualifier using the confidence scoring framework |

---

## Confidence Scoring

Assign an explicit confidence level to every conflict finding and to the overall clearance
opinion.

| Level                 | Notation                          | Meaning                                                                                                                     | Action                                                                           |
| --------------------- | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **HIGH**              | `[HIGH CONFIDENCE]`               | Direct registry hit; identical or near-identical mark; same or clearly related class; live/pending status confirmed         | Present as material risk; Self-Interrogation required for BLOCKED classification |
| **MEDIUM**            | `[MEDIUM CONFIDENCE]`             | Phonetic or conceptual similarity; adjacent classes; mixed DuPont factors; common law evidence suggestive but not confirmed | Flag as caution; recommend monitoring and professional search confirmation       |
| **LOW**               | `[LOW CONFIDENCE]`                | Weak similarity on one dimension only; different market segment; limited use evidence; geographically remote                | Note for awareness; unlikely to block; coexistence probable                      |
| **INSUFFICIENT DATA** | `[VERIFY — deeper search needed]` | Gaps in search coverage; unclear registration status; insufficient use evidence to classify                                 | Do not classify; recommend professional search service for this specific finding |

---

## Anti-Patterns: What NOT to Do in Trademark Clearance

1. **Single-source search** — Relying on one database (e.g., TESS only) systematically
   misses Madrid Protocol international registrations, national marks in target markets,
   and common law rights. Always search at least registered mark databases + common law
   sources for each target jurisdiction.

2. **Ignoring pending applications** — A mark applied for but not yet registered still
   constitutes a potential conflict in first-to-file systems. In the US, a pending
   application (Intent-to-Use or actual use) can mature into a blocking registration.
   Search live AND pending marks, not just registered marks.

3. **Skipping abandoned mark analysis** — An abandoned registration may still represent
   a mark in active commercial use with common law rights. Check whether the abandonment
   was due to non-renewal (use may continue) or to non-use (rights may be extinguished).

4. **Letter-by-letter comparison only** — Trademark similarity is judged by overall
   commercial impression, not a character-by-character match. "APPEX" and "APEX" are
   more similar than a letter comparison suggests. Always assess phonetic, visual, and
   conceptual dimensions holistically.

5. **Conflating trademark classes** — Class 9 (software) and Class 42 (SaaS) are legally
   separate but functionally adjacent. A mark in Class 42 can still block a Class 9
   application if the goods/services are related. Never dismiss a conflict solely because
   it is in a different class — assess the relatedness of goods/services.

6. **Ignoring first-to-use systems** — In the US, Australia, and India, unregistered marks
   based on prior commercial use can block a later application. A mark with no registry
   presence but active use in commerce is potentially as dangerous as a registered mark.
   Common law search is not optional in these jurisdictions.

7. **Not checking translations and foreign language equivalents** — A proposed mark's
   translation may already be registered by a third party. [JURISDICTION-SPECIFIC: EU]
   EUIPO examines conceptual similarity across languages widely understood in the EU.
   Check translations in all languages relevant to target markets.

8. **Assuming a crowded field means no risk** — A field with many similar marks may have
   narrower individual scopes of protection, but this does not mean any specific similar
   mark can be ignored. Identify the strongest/most proximate marks even in crowded fields.

9. **Treating registration refusal probability as freedom-to-use probability** — A mark
   may be registrable but still infringe a registered mark with common law extension.
   Conversely, a mark may be refused registration on relative grounds but face limited
   practical infringement risk if the senior mark is in a clearly different market. These
   are separate analyses.

10. **Skipping domain and social media search** — Domain registration and active social
    media use are evidence of commercial use and intent. Ignoring these sources leaves
    material common law risks undiscovered, especially in the US and Australia.

11. **Not considering color, shape, and trade dress** — Non-traditional marks are
    protectable. A distinctive color scheme, product shape, or packaging configuration
    that resembles the proposed mark's visual identity may create infringement risk even
    if no word mark conflict exists.

12. **Overweighting distant DuPont factors** — Factors 1 (mark similarity) and 2 (goods/
    services relatedness) are the anchors of the DuPont analysis. Do not let favorable
    outcomes on factors 3–13 override a clear finding of similarity on factors 1 and 2.

13. **Failing to document search methodology** — A trademark clearance opinion is only
    as credible as its methodology. Document every database searched, every query run,
    and every limitation acknowledged. This documentation is critical if the clearance
    is later challenged in litigation.

14. **Assuming coexistence is risk-free** — Marks may have coexisted historically without
    formal consent agreements, but the senior mark owner retains the right to enforce.
    Tolerance of infringement does not extinguish rights (absent laches in specific
    circumstances). Recommend a formal consent or coexistence agreement whenever
    proceeding with a CAUTION mark.

15. **Not checking for concurrent use agreements or consent agreements** — Search USPTO
    TESS for existing consent letters or concurrent use proceedings. A mark registered
    subject to a concurrent use agreement signals that the field is contested and the
    boundaries may be litigated.

16. **Ignoring Madrid Protocol implications** — If the user plans to file internationally,
    a mark clear in the US may be blocked in key international markets via existing Madrid
    Protocol designations. Always check WIPO Global Brand Database for international
    registrations that designate the user's target territories.

17. **Providing clearance without noting professional review requirement** — An AI-assisted
    trademark clearance search supplements but does not replace professional advice. Always
    note that the output requires review by a licensed trademark attorney before adoption
    or filing decisions are made.

---

## Writing Standards

Apply these writing standards before delivering any output:

**Plain language:**

- Write for a business audience: clear, direct, no unexplained jargon
- Define legal terms on first use: "likelihood of confusion (the legal standard for when
  consumers might believe two brands come from the same source)"
- Active voice throughout: "This mark conflicts with APEX (Reg. #123)" not "A conflict
  has been identified between the proposed mark and APEX (Reg. #123)"

**Specificity:**

- Name the specific conflicting mark, its registration number, its owner, and its class
- State the precise basis for concern: "Phonetically similar; same first syllable 'APEX';
  both used on business software services (Class 42)"
- Cite the specific DuPont factors that drive the classification: "Factors 1 (mark
  similarity — HIGH) and 2 (goods/services relatedness — HIGH) both point to confusion"

**Calibrated confidence:**

- Every finding carries an explicit confidence level
- Never assert "No conflict found" — use "No conflicts found in the databases searched"
  and document the databases and methodology
- Use "appears to be available" not "is clear" — the latter implies a guarantee no
  AI-assisted search can provide

**Actionable recommendations:**

- Every BLOCKED finding must include at least one specific recommended action
- Every CAUTION finding must include a monitoring or coexistence strategy
- Alternative marks must be specific (actual mark suggestions, not just categories)

**Quality gate before delivery:**

- [ ] Active voice throughout
- [ ] Every conflict named, cited, classified
- [ ] Confidence levels explicit
- [ ] Limitations documented
- [ ] Professional review reminder included

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

Use **legalcode-mcp** for legal research in Step 8 and when addressing jurisdiction-specific
questions:

1. Search for current TTAB decisions on likelihood of confusion in the relevant industry
2. Search for recent USPTO examination guidelines for the applicable mark type
3. Retrieve current EUIPO examination guidelines for relative grounds of refusal
4. Search for passing off case law in UK/AU for the relevant goods/services
5. Verify current status of any legal principles marked [VERIFY] in this skill

Save research results to a temporary reference file:

```
/tmp/trademark-clearance-research-[YYYY-MM-DD].md
```

Structure the file as:

```markdown
# Trademark Clearance Legal Research — [Mark] — [Date]

## Key Statutes

- [Statute, jurisdiction, relevance]

## Key Case Law

- [Case, citation, key holding, verification status]

## USPTO/EUIPO/UKIPO Guidelines

- [Guideline reference, relevance, verification status]

## Recent Developments

- [Development, date, impact on clearance]
```

Reference this file throughout the clearance analysis and cite it in the Glass Box audit trail.

### Without legalcode-mcp

- Proceed with research from this skill's built-in frameworks and web-backed knowledge
- Mark all statutory and case law references with `[VERIFY against authoritative sources]`
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus quality effort on structural completeness, DuPont analysis depth, and search
  methodology documentation rather than legal citation precision

---

## Output Format Template

Deliver the clearance opinion using this structured template:

---

````markdown
# Trademark Clearance Opinion — [PROPOSED MARK]

**Date:** [YYYY-MM-DD]
**Requested by:** [User/Organization]
**Prepared by:** Legalcode Trademark Clearance Search (AI-assisted — professional review required)

---

## Executive Summary

| Item                         | Details                                                     |
| ---------------------------- | ----------------------------------------------------------- |
| **Proposed mark**            | [Mark text / description]                                   |
| **Goods/services**           | [Description]                                               |
| **Nice class(es)**           | [Classes searched]                                          |
| **Jurisdictions searched**   | [US / EU / UK / AU / IN / Other]                            |
| **Overall clearance rating** | ✅ CLEAR / ⚠️ CAUTION / 🚫 BLOCKED                          |
| **Conflicts found**          | [Number]: [#] BLOCKED / [#] CAUTION / [#] CLEAR             |
| **Distinctive strength**     | [Fanciful / Arbitrary / Suggestive / Descriptive / Generic] |
| **Recommended action**       | [One-sentence recommendation]                               |

### Top Priority Actions

| Priority | Action               | Owner             | Deadline |
| -------- | -------------------- | ----------------- | -------- |
| 1        | [Most urgent action] | Trademark counsel | [Date]   |
| 2        | [Second action]      | [Owner]           | [Date]   |
| 3        | [Third action]       | [Owner]           | [Date]   |

---

## Search Scope and Methodology

**Databases searched:**

- [ ] USPTO TESS (US federal marks — live and pending)
- [ ] EUIPO TMView (EU + member state marks)
- [ ] WIPO Global Brand Database (Madrid Protocol)
- [ ] UKIPO Trade Mark Register
- [ ] IP Australia ATMOSS
- [ ] IP India Public Search
- [ ] Domain names (WHOIS)
- [ ] Social media handles
- [ ] Business name registrations
- [ ] Other: [specify]

**Search queries run:**

- Identical mark: [exact queries]
- Phonetic variants: [queries]
- Conceptual variants: [queries]
- Wildcard/truncated: [queries]

**Limitations:**

- [Any database not searched and reason]
- [Any common law search limitations]
- [Any time/resource constraints affecting scope]

---

## Distinctiveness Assessment

| Dimension                    | Assessment                                                  |
| ---------------------------- | ----------------------------------------------------------- |
| **Proposed mark**            | [Text]                                                      |
| **Distinctiveness category** | [Fanciful / Arbitrary / Suggestive / Descriptive / Generic] |
| **Inherently distinctive?**  | [Yes / No / Borderline]                                     |
| **Surname doctrine risk**    | [None / Low / Medium / High — rationale]                    |
| **Geographic doctrine risk** | [None / Low / Medium / High — rationale]                    |
| **Registrability outlook**   | [Strong / Moderate / Poor — rationale]                      |

---

## Conflict Analysis by Jurisdiction

### [JURISDICTION 1 — e.g., United States]

#### [Mark Name] ([Classification])

| Field                        | Details                                  |
| ---------------------------- | ---------------------------------------- |
| **Conflicting mark**         | [Mark text]                              |
| **Owner**                    | [Owner name]                             |
| **Registration number**      | [USPTO Reg. #XXXXXXX / Pending Serial #] |
| **Nice class(es)**           | [Class(es)]                              |
| **Goods/services**           | [Description from registry]              |
| **Status**                   | [Live / Pending / Abandoned]             |
| **Filing/registration date** | [Date]                                   |
| **Confidence**               | [HIGH / MEDIUM / LOW CONFIDENCE]         |
| **Classification**           | 🚫 BLOCKED / ⚠️ CAUTION / ✅ CLEAR       |

**Similarity Analysis:**

- _Phonetic_: [Detailed phonetic comparison]
- _Visual_: [Detailed visual comparison]
- _Conceptual_: [Detailed conceptual comparison]

**DuPont Analysis:**

| Factor                        | Finding      | Weight           |
| ----------------------------- | ------------ | ---------------- |
| 1. Mark similarity            | [Assessment] | HIGH             |
| 2. Goods/services relatedness | [Assessment] | HIGH             |
| 3. Trade channels             | [Assessment] | Medium           |
| 4. Consumer sophistication    | [Assessment] | Medium           |
| 5. Fame of senior mark        | [Assessment] | [High if famous] |
| [Additional relevant factors] |              |                  |

**Self-Interrogation (BLOCKED findings only):**

- Pass 1 — Chain Integrity: [Assessment]
- Pass 2 — Search Completeness: [Assessment]
- Pass 3 — Severity Challenge: [Assessment]
- Outcome: PASS / REVISED — [reason]

**Recommended action:**

- [Specific, actionable recommendation for this specific conflict]

---

[Repeat for each conflicting mark and each jurisdiction]

---

## Common Law Search Results

| Source                 | Findings   | Risk Level                  |
| ---------------------- | ---------- | --------------------------- |
| Domain names           | [Findings] | [CLEAR / CAUTION / BLOCKED] |
| Social media           | [Findings] | [Level]                     |
| Business registrations | [Findings] | [Level]                     |
| Internet use evidence  | [Findings] | [Level]                     |

---

## Alternative Mark Recommendations

_(Only if BLOCKED or high CAUTION)_

| Alternative Mark | Distinctiveness           | Key Advantage                | Preliminary Risk |
| ---------------- | ------------------------- | ---------------------------- | ---------------- |
| [Alternative 1]  | [Fanciful/Arbitrary/etc.] | [Why it avoids the conflict] | [Low / Medium]   |
| [Alternative 2]  | [Level]                   | [Advantage]                  | [Risk level]     |
| [Alternative 3]  | [Level]                   | [Advantage]                  | [Risk level]     |

---

## Clearance Strategy and Next Steps

1. **Immediate actions** (within 7 days):
   - [Action 1]
   - [Action 2]

2. **Filing strategy**:
   - [Which jurisdictions to file in; which to defer]
   - [Paris Convention priority window, if applicable]
   - [Madrid Protocol filing recommendation, if applicable]

3. **Coexistence or monitoring strategy** (if CAUTION):
   - [Coexistence agreement target, if any]
   - [Watch service recommendation]
   - [Documentation of use evidence]

4. **Professional engagement**:
   - Engage a licensed trademark attorney in [jurisdiction(s)] to review this opinion
     and conduct or commission a professional search before filing or commercial adoption

---

## Glass Box Audit Trail

```yaml
glass_box:
  search_request: "[Proposed mark, goods/services, jurisdictions]"
  search_date: "[YYYY-MM-DD]"
  search_scope:
    jurisdictions: "[List]"
    nice_classes: "[List]"
    databases_searched: "[List]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/trademark-clearance-research-YYYY-MM-DD.md or 'Not created']"
  regulations_cited:
    - "15 U.S.C. § 1052(d) Lanham Act § 2(d) — [VERIFY / VERIFIED]"
    - "In re E.I. du Pont de Nemours & Co., 476 F.2d 1357 (CCPA 1973) — [VERIFY / VERIFIED]"
    - "EUTMR Art. 8(1)(b) — [VERIFY / VERIFIED]"
    - "[Additional citations with verification status]"
  conflicts_identified:
    blocked: "[Count]"
    caution: "[Count]"
    clear: "[Count]"
  self_interrogation:
    applied_to: "[Mark(s) self-interrogation was applied to]"
    pass_1_chain_integrity: "[PASS / REVISED — detail]"
    pass_2_completeness: "[PASS / REVISED — detail]"
    pass_3_challenge: "[PASS / REVISED — detail]"
    outcome: "PASS / REVISED — [reason if revised]"
  citations_verified: "[Number VERIFIED] / [Number UNVERIFIED]"
  overall_confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "Common-law search limited to publicly accessible internet sources"
    - "Registry data current as of search date; verify before filing"
    - "Device/logo elements not fully searched — specialist design search required"
    - "[Any other limitations]"
  reviewer: "AI-assisted — requires review by a qualified trademark attorney before adoption or filing"
```
````

```

---

## Localization Notes

This skill is designed for cross-jurisdictional use. When localizing for a specific jurisdiction:

**US-specific enhancements:**
- Run full TESS search using all three search modes (Basic, Structured, Free Form)
- Check concurrent use registers and opposition records (TTAB records at ttabvue.uspto.gov)
- Verify incontestability status of senior marks (15 U.S.C. § 1065)
- Check for Intent-to-Use (ITU) applications that may mature into blocking registrations

**EU-specific enhancements:**
- Run EUIPO eSearch Plus in addition to TMView for more granular EUIPO data
- Check for national earlier rights in all target EU member states separately
- Assess whether the senior mark has "reputation" status (Art. 8(5) EUTMR)
- Consider EU unitary character — one EUTM registration covers all 27 member states;
  one national objection can block an EUTM [JURISDICTION-SPECIFIC: EU]

**UK-specific enhancements:**
- Search UKIPO database separately — EUIPO search does not cover UK post-Brexit
- Check UK "comparable trade marks" database for Brexit-converted EUTMs
- Assess passing off risk under UK common law even where no registration conflict found

**AU-specific enhancements:**
- Search IP Australia ATMOSS for all live, pending, and lapsed marks
- Conduct a more thorough domain/business name search given AU first-to-use system
- Assess ACL misleading and deceptive conduct risk in parallel with Trade Marks Act 1995

**IN-specific enhancements:**
- Search IP India Public Search by wordmark in all five regional trade mark offices
  (Mumbai, Delhi, Kolkata, Chennai, Ahmedabad) — registration scope differs by office
- Assess prior use evidence carefully — Indian first-to-use system means well-known
  unregistered marks command strong rights under Section 11 and Section 34
- Check for well-known mark status declarations by the Registrar [JURISDICTION-SPECIFIC: IN]

---

## Provenance

Created by Legalcode as an original synthesis (2026-03-02). Methodology draws from:
- *In re E.I. du Pont de Nemours & Co.*, 476 F.2d 1357 (C.C.P.A. 1973) (13-factor test)
- *SABEL BV v Puma AG* (C-251/95) and *Lloyd Schuhfabrik Meyer* (C-342/97) (EU global appreciation)
- USPTO Trademark Manual of Examining Procedure (TMEP) § 1207 (likelihood of confusion guidelines)
- EUIPO Guidelines for Examination of European Union Trade Marks
- UK Trade Marks Act 1994 and UKIPO Examination Guidelines
- Australia Trade Marks Act 1995 (Cth) and IP Australia Examination Practice
- India Trade Marks Act 1999 and IP India examination procedures
- Nice Agreement Concerning the International Classification of Goods and Services (NCL 13-2026)
- Madrid Protocol (Agreement Concerning the International Registration of Marks)
- Paris Convention for the Protection of Industrial Property (priority provisions)
- Legalcode quality framework: Glass Box audit trail, Citation Quality Gates, Self-Interrogation,
  and Confidence Scoring adapted from the legalcode-contract-review reference standard

All legal references should be verified against current authoritative sources before use.
```
