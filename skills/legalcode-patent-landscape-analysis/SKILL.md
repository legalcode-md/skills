---
name: legalcode-patent-landscape-analysis
description: Conduct patent landscape analyses and freedom-to-operate (FTO) assessments covering patent
  family mapping, claim scope analysis, prior art assessment, white space identification, competitive
  intelligence, prosecution history review, and infringement risk scoring. Use when a company is entering
  a new technology area, evaluating M&A or licensing targets, planning R&D investment, clearing a product
  for commercialization, assessing competitor patent portfolios, or building IP filing strategy. Covers
  USPTO, EPO/UPC, WIPO/PCT, and JPO databases with IPC/CPC classification-based search methodology. Jurisdiction-agnostic
  framework with US, EU/UPC, UK, Japan, and WIPO-specific markers. Supports strategic landscape mode (broad
  competitive intelligence, white space identification, filing trend analysis) and FTO mode (product-specific
  element-by-element claim analysis and infringement risk scoring). Also supports validity / prior art
  searches and M&A patent due diligence.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Patent Landscape Analysis

> **Disclaimer**: This skill provides a framework for AI-assisted patent landscape and
> freedom-to-operate analysis. It does not constitute legal advice or a formal FTO opinion.
> All outputs must be reviewed by a qualified patent attorney licensed in the relevant
> jurisdiction before any commercialization or product launch decision. Patent law changes;
> verify current applicability of all statutory and regulatory references before relying on
> them. Statutory and case law references cited from memory carry hallucination risk —
> verify against authoritative sources (USPTO, EPO, WIPO, national patent offices) before
> use in any legal proceeding or business decision. A formal FTO opinion establishing
> attorney-client privilege must be issued by a registered patent attorney, not an AI tool.

## Purpose and Scope

This skill conducts patent landscape analyses and freedom-to-operate assessments, providing
strategic IP intelligence and product-specific infringement risk analysis across the US, EU,
WIPO/PCT, and JPO patent systems.

**Covers:**

- Patent landscape analysis: filing trends, assignee portfolio mapping, technology cluster
  analysis, white space identification, citation network analysis
- Freedom-to-operate (FTO) analysis: element-by-element claim charting of relevant patents
  against a defined product or process specification
- Patent family mapping: DOCDB simple and INPADOC extended family deduplication and
  geographic coverage mapping
- Claim scope analysis: independent vs. dependent claim hierarchy, claim construction
  (intrinsic evidence hierarchy per Phillips v. AWH Corp.)
- Prior art assessment: novelty (35 U.S.C. § 102 / EPC Art. 54) and obviousness
  (35 U.S.C. § 103 / EPC Art. 56) evaluation
- Prosecution history review: file wrapper estoppel analysis (Festo, 2002), doctrine of
  equivalents scope assessment
- Competitive intelligence: assignee analysis, inventor tracking, citation networks,
  M&A signal detection from portfolio patterns
- Infringement risk scoring: GREEN / YELLOW / RED tiered risk classification per patent
- UPC exposure analysis (post-June 2023) for European markets
- Patent due diligence for M&A and licensing transactions
- Validity / invalidity search to support IPR/PGR petitions or opposition proceedings

**Does not:**

- Draft or prosecute patent applications (see patent drafting skills)
- Replace a formal FTO opinion by a registered patent attorney with attorney-client privilege
- Guarantee freedom to operate — patent searching cannot achieve 100% certainty; pending
  applications, undisclosed continuation claims, and post-filing claim amendments create
  inherent ongoing risk
- Provide legal advice or substitute for qualified patent counsel

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The target jurisdiction(s) are determined by where
the product will be made, imported, sold, or used. A patent only creates risk in jurisdictions
where it is filed, granted, and maintained.

[JURISDICTION-SPECIFIC: US] When analyzing under US law, apply:

- 35 U.S.C. as amended by the America Invents Act (AIA, 2011): first-inventor-to-file
  system; § 101 patent eligibility, § 102 novelty, § 103 obviousness, § 112 written
  description and enablement, § 154 patent term, § 271 infringement, § 284 damages
- Alice/Mayo two-step framework for patent eligibility of software, business methods,
  and life-science claims: Alice Corp. v. CLS Bank Int'l, 573 U.S. 208 (2014); Mayo
  Collaborative Services v. Prometheus Laboratories, 566 U.S. 66 (2012)
- USPTO 2024 Guidance Update on Patent Subject Matter Eligibility (Fed. Reg. July 17,
  2024, 2024-15377) — AI-specific Examples 47–49 [VERIFY currency]
- USPTO AI Inventorship Guidance (November 2025): AI is a tool, not a co-inventor;
  human conception remains required [VERIFY]
- Claim construction hierarchy: Phillips v. AWH Corp., 415 F.3d 1303 (Fed. Cir. 2005
  en banc) — intrinsic evidence (claims, specification, prosecution history) first;
  extrinsic evidence (experts, dictionaries) secondary
- Markman hearings: claim construction is a question of law for the judge (Markman v.
  Westview Instruments, 517 U.S. 370, 1996)
- Prosecution history estoppel: Festo Corp. v. Shoketsu Kinzoku Kogyo Kabushiki Co.,
  535 U.S. 722 (2002) — presumptive bar on doctrine of equivalents following narrowing
  amendments made for patentability reasons
- PTAB post-grant proceedings: IPR (§ 311–319, prior art only, within 1 year of complaint
  service); PGR (§ 321–329, any invalidity ground, within 9 months of grant)
- Proposed PREVAIL Act reforms to IPR standard (pending as of early 2026) [VERIFY]
- Patent term: 20 years from earliest effective filing date (§ 154); Patent Term
  Adjustment (PTA) for USPTO prosecution delays

[JURISDICTION-SPECIFIC: EU/UPC] When analyzing under European law, apply:

- European Patent Convention (EPC): Art. 54 (novelty), Art. 56 (inventive step), Art. 53
  (exceptions to patentability), Art. 69 + Protocol (scope of protection)
- Unified Patent Court (UPC) — operative since June 1, 2023: covers 18 EU member states;
  a single infringement or revocation action has pan-European effect
- Unitary Patent: provides uniform protection across all UPC member states after grant;
  no national validation required; significantly raises the stakes of European FTO
- UPC opt-out: during the transitional period, holders of classic European patents may opt
  out of UPC jurisdiction — check opt-out status at register.epo.org per patent [VERIFY]
- UPC preliminary injunction standard: "more likely than not" that claimant is entitled to
  bring proceedings, patent is infringed, and patent is valid
- EPO opposition: any third party may oppose a granted EP within 9 months of grant —
  cost-effective invalidity challenge alternative to litigation
- UK: not a UPC member post-Brexit; UK Patents Act 1977 / UKIPO; IPEC and Patents Court
  (Chancery Division); separate analysis required for UK market

[JURISDICTION-SPECIFIC: WIPO/PCT] When analyzing PCT filings:

- Patent Cooperation Treaty: 157+ contracting states; international filing with
  national/regional phase entry deadline at month 30–31
- International Search Report (ISR) + Written Opinion: non-binding prior art search and
  patentability assessment by an International Searching Authority (ISA)
- PCT applications publish at 18 months from priority date — prior art effective from
  publication; leading indicator of global IP filing strategy
- WIPO PatentScope is the authoritative source for PCT application data

[JURISDICTION-SPECIFIC: Japan] When analyzing Japanese patents:

- Japan Patent Act (特許法): JPO J-PlatPat is the authoritative database; FI/F-term
  classification is JPO-proprietary and supplements IPC
- Also consider utility model registrations (実用新案) for consumer product FTO
- Machine-translated claims carry additional uncertainty — flag with [MACHINE TRANSLATION]
  and recommend qualified translation for high-risk Japanese patents [VERIFY]

[JURISDICTION-SPECIFIC: China] When China is a target market:

- CNIPA (China National Intellectual Property Administration): patent volume is highest
  globally; must include for any comprehensive global FTO or landscape
- Search at cpquery.cnipa.gov.cn; invalidity proceedings at CNIPA Patent Reexamination
  and Invalidation Division; inventiveness standard may differ from US/EU

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The analysis type (landscape vs. FTO vs. both) determines the entire methodology
- The target jurisdictions determine which databases, legal frameworks, and risk standards apply
- The product specification required for FTO analysis is incomplete or ambiguous
- Risk tolerance determines whether borderline YELLOW/RED classifications should escalate
- Scope choices materially affect the result set size and feasibility

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

Accept input in any of these formats:

**For landscape analysis:**

- Technology description (field, sub-domain, product category, industry keywords)
- IPC/CPC classification codes (if known)
- Competitor names (for focused competitive landscape)
- Patent numbers of known relevant patents (as anchor documents)
- Time period of interest

**For FTO analysis:**

- Technology Document or product specification describing all features, variants, and
  manufacturing steps of the subject product or process
- Target commercialization jurisdictions (where the product will be made, sold, or used)
- Known patents of concern (if any) — these become anchor documents for the search
- Product launch timeline (urgency factor for triage)

**For both:**

- Multiple of the above, combined

If the input is ambiguous or incomplete, proceed to Step 2 before any analysis.

---

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user (skip questions already answered by the input):

1. **Analysis mode**: What type of analysis is needed?
   - Options: **Landscape only** (strategic intelligence, competitive mapping, white space
     identification), **FTO only** (product-specific infringement risk clearance), **Full
     analysis** (landscape + FTO), **Validity / prior art search** (support an IPR/PGR
     petition or opposition), **M&A patent due diligence** (portfolio quality + FTO of
     target's products)
   - _Why this matters_: Determines the entire methodology. Landscape uses broad search
     and statistical analysis. FTO requires a precise Technology Document and
     element-by-element claim charting. Validity search requires comprehensive NPL coverage.

2. **Target jurisdictions**: Where will the product be made, sold, imported, or used?
   - Options: US only, EU/UPC (specify member states), US + EU, US + EU + UK, US + EU +
     JP, All major markets (US/EU/UK/JP/CN), Custom selection
   - _Why this matters_: A patent only creates infringement risk in jurisdictions where it
     is filed, granted, and maintained. A US patent does not block activities in Germany.

3. **Technology scope**: How broad is the technology domain?
   - Options: Narrow (specific product/process), Moderate (technology sub-domain), Broad
     (full technology field), Let me see sample results first, then refine
   - _Why this matters_: A landscape that is too broad returns thousands of irrelevant
     results; too narrow risks missing blocking IP. Most FTO analyses are narrow-scope
     while landscape analyses use moderate to broad scope.

4. **Deadline / urgency**: When is the output needed?
   - Options: Critical path (days — FTO triage only, flag highest risks), Standard
     (1–2 weeks — full analysis with prosecution history review), Strategic planning
     (flexible — comprehensive coverage including NPL)
   - _Why this matters_: Affects analysis depth — critical-path mode produces a rapid
     triage of highest-risk patents only, not a comprehensive FTO opinion.

5. **Prior knowledge** (if FTO mode): Are there known patents or competitors of concern?
   - Free text. Named patents become anchor documents for forward/backward citation search.
   - _Why this matters_: Anchor documents dramatically improve search recall by seeding
     the citation network search.

If the user provides partial context, proceed with stated assumptions (e.g., "I am assuming
US + EU are the target jurisdictions — confirm if that is wrong and I will revise").

---

### Step 3: Gather Legal Authority

Read the target jurisdiction(s) and use **legalcode-mcp** to build a working legal reference
file for this analysis.

**Research focus by jurisdiction:**

| Jurisdiction | Key Research Topics                                                                                                                                                                                                         |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US           | Current § 101 eligibility guidance (Alice/Mayo); IPR/PGR procedures; relevant PTAB precedent; § 284 damages precedent for the technology field; key Federal Circuit decisions on claim construction in this technology area |
| EU/UPC       | UPC preliminary injunction standards; EPO opposition board precedent; EPC Art. 69 scope of protection cases; UPC Court of Appeal decisions (2023–present)                                                                   |
| UK           | UK Patents Act 1977 provisions; UK Supreme Court / Court of Appeal patent decisions; IPEC small claims track (for SME context)                                                                                              |
| WIPO/PCT     | PCT timeline and national phase entry deadlines; ISA standards for the relevant technology classification                                                                                                                   |

**Save research results** to `/tmp/legalcode-patent-research.md`:

```markdown
# Legal Authority Reference — [Technology Area]

## Jurisdictions: [list]

## Date Gathered: [date]

### US Statutes & Regulations

- [Statute, section, current text or summary]

### US Case Law

- [Case, citation, key holding relevant to this FTO or landscape]

### EU/UPC Legal Framework

- [EPC Article / UPC Rule / Court of Appeal decision]

### Regulatory Guidance

- [Office, guidance document, relevance]

### Recent Developments

- [Development, date, impact on the analysis]
```

**If legalcode-mcp is not connected:**

- Proceed using general patent law knowledge
- Mark every statutory and case law reference with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`

---

### Step 4: Construct Search Strategy

Design the search strategy before executing database queries. A well-constructed strategy
reduces the risk of missed blocking patents (the primary error mode in FTO analysis).

**Step 4a: Identify IPC/CPC Classification Codes**

IPC (International Patent Classification) and CPC (Cooperative Patent Classification) are
hierarchical, language-independent classification systems used by all major patent offices.
Using classification codes alongside keywords dramatically improves recall for non-English
documents.

Method:

1. Identify the primary IPC/CPC class for the technology domain (examples: A61K for
   pharmaceuticals; G06F for computing; H04L for network communications; B60L for
   electric vehicles)
2. Drill down to relevant subclass, group, and subgroup levels
3. Use the CPC concordance browser in Espacenet or USPTO to find all sub-codes applicable
   to the technology
4. Document all classification codes used and their definitions

**⟁ CLARIFY** — If the technology spans multiple IPC/CPC classes (e.g., a medical device
with embedded software spans A61B + G16H):

- "This technology spans [X] and [Y] classification areas. Should I search both domains
  fully (comprehensive, more results) or focus on the primary domain (faster, fewer
  results)?"
- _Why this matters_: Cross-domain coverage gaps are a leading source of missed blocking
  IP in multi-technology products.

**Step 4b: Construct Boolean Keyword Query**

Develop a multi-layer Boolean query combining:

- Primary technical terms (core feature names and function descriptions)
- Synonyms and variant spellings (including international terminology variations)
- Broader/narrower terms (hierarchical expansion for recall; narrowing for precision)
- Inventor or assignee names (for competitive-focused landscape)

WIPO rule of thumb: target **≥ 90% recall / ≥ 70% precision** for landscape analysis;
**≥ 95% recall** for FTO analysis (missing a blocking patent is the dominant risk).

**Step 4c: Define Scope Parameters**

| Parameter     | Landscape Default                                           | FTO Default                                                              |
| ------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------ |
| Date range    | Last 20 years (or full patent lifetime for foundational IP) | All unexpired patents: 20-year term from earliest effective filing date  |
| Legal status  | All (including expired, for prior art and trend analysis)   | Active only: granted + pending published applications                    |
| Jurisdictions | Target markets + PCT/WIPO for global filings                | Target markets where commercialization will occur                        |
| Family unit   | DOCDB simple families (for deduplication and counting)      | Individual national members (for jurisdiction-specific enforcement risk) |
| NPL inclusion | Optional (recommended for biotech/pharma/materials)         | Recommended — NPL is prior art under § 102 / EPC Art. 54                 |

---

### Step 5: Execute Database Search

Run the search across at least two databases. Document all queries, execution dates, and
result counts in the Glass Box audit trail.

**Recommended database combinations by purpose:**

| Purpose                      | Primary                                      | Secondary                  | Supplementary                |
| ---------------------------- | -------------------------------------------- | -------------------------- | ---------------------------- |
| Landscape (all domains)      | EPO Espacenet                                | WIPO PatentScope           | Google Patents (scope check) |
| Landscape (chemistry/pharma) | Derwent Innovation                           | CAS STNext / SciFinder     | Espacenet                    |
| FTO (US market)              | USPTO Patent Public Search                   | Espacenet (family members) | PatSnap or Orbit             |
| FTO (European/UPC)           | EPO Espacenet + Patent Register              | Orbit Intelligence         | EPO Global Patent Index      |
| FTO (Japan)                  | JPO J-PlatPat                                | Espacenet (family members) | PatSnap                      |
| Prosecution history (US)     | USPTO Patent Center (patentcenter.uspto.gov) | —                          | —                            |
| Prosecution history (EU)     | EPO Patent Register (register.epo.org)       | —                          | —                            |

**Search execution checklist:**

- [ ] Run search with IPC/CPC codes + keywords combined (AND) — primary query
- [ ] Run search with IPC/CPC codes alone — captures non-English and misabstracted patents
- [ ] Run search with keywords alone in title/abstract/claims — captures misclassified patents
- [ ] Cross-validate: check overlap between databases (identifies missed documents)
- [ ] Run forward citation search from anchor documents (patents citing the same prior art)
- [ ] Run backward citation search from anchor documents (foundational prior art)
- [ ] Search for published pending applications (potential future threats)
- [ ] Document total result counts before and after deduplication

**⟁ CLARIFY** — If the initial search returns >5,000 results (landscape) or >500 results
(FTO), present the counts to the user:

- "The initial search returned [N] documents. I recommend [specific refinement: limit to
  last 10 years / narrow to sub-class [X] / exclude expired]. Would you like me to apply
  this refinement, or proceed with the full result set?"
- _Why this matters_: Result set size determines feasibility of qualitative analysis;
  unmanaged scope produces shallow coverage of a large set rather than deep analysis of
  the highest-risk subset.

---

### Step 6: Patent Family Mapping and Deduplication

Consolidate results at the patent family level to avoid inflating statistics and to map the
geographic filing strategy of each patent holder.

**Family type selection:**

| Family Type                       | Definition                                                                                          | Use Case                                                          |
| --------------------------------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **DOCDB Simple Family** (EPO)     | Patents sharing exactly the same priority document(s); strictest definition, smallest families      | Counting distinct inventions for landscape statistics             |
| **INPADOC Extended Family** (EPO) | All patents directly or indirectly sharing at least one priority; broader grouping, larger families | FTO: identifying all national counterparts of a patent of concern |

**Deduplication process:**

1. Group retrieved documents by DOCDB simple family (for counting and trend analysis)
2. For each high-relevance family, retrieve all INPADOC extended family members to map
   geographic coverage (which countries the patent holder has pursued protection in)
3. Check legal status per family member: granted / pending / expired / abandoned /
   lapsed for non-payment
4. Identify US continuation and continuation-in-part (CIP) applications — pending
   continuations may issue with claims specifically drafted to cover a product seen
   in the market after the parent's filing date
5. For European patents post-2023: check UPC opt-out status at register.epo.org

**Output**: Patent family map showing — for each relevant family — the family ID, title,
priority date, all national members with jurisdiction and legal status, assignee, and
(for FTO relevance) a preliminary relevance flag.

---

### Step 7: Landscape Analysis

_(Skip to Step 8 if analysis mode is FTO-only.)_

Apply quantitative and qualitative analysis to the consolidated patent family dataset.

**7a: Filing Trend Analysis**

Plot filing volume over time using priority date for cross-database consistency:

- Overall trend line (growing, stable, declining, cyclical)
- Breakdown by top 10 assignees (3-year rolling average to smooth noise)
- Breakdown by key technology sub-domain (IPC/CPC sub-class)

Interpret trends:

- Rapid recent growth → high competitive activity; space may be crowding quickly
- Declining filings → technology maturation, obsolescence, or patent cliff approach
- Spike followed by plateau → typical product launch cycle; patents precede commercial
  launch by 18–36 months; a spike indicates product launch 1–3 years later
- Competitor acceleration → signals strategic R&D investment; warrants FTO follow-up

**7b: Assignee and Competitive Intelligence Analysis**

Identify and assess:

- Top assignees by family count (overall and by jurisdiction)
- Recent entrants (first filings within last 3–5 years) — new competitive threats
- Assignees increasing vs. decreasing filing rate (3-year rolling average comparison)
- University and research institution filers — typically licensing targets; lower
  likelihood of aggressive litigation vs. operating companies
- Non-practicing entities (NPEs) / patent assertion entities (PAEs) in the landscape —
  higher litigation risk; often willing to license at a price

**Landscape Density Classification** — assign to each technology sub-domain:

| Classification       | Criteria                                                                  | Strategic Implication                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **HIGH DENSITY**     | >50 active families per sub-domain; top 3 assignees hold >60% of families | Crowded — freedom to operate requires detailed FTO; consider whether design-around or licensing is more efficient than novel development |
| **MODERATE DENSITY** | 10–50 active families; distributed assignee concentration                 | Competitive but navigable — selective FTO on highest-relevance patents; licensing is likely available from multiple sources              |
| **WHITE SPACE**      | <10 active families; no dominant assignee                                 | Open opportunity zone — lower IP barrier to entry; validate before relying on (see 7c white space validation checklist)                  |

**7c: Technology Cluster and White Space Analysis**

Map the technology taxonomy across two analytical dimensions:

1. **Technology axis**: functional sub-domains derived from IPC/CPC codes
   (e.g., Sensing → Signal Processing → Output/Interface → Materials → System Integration)
2. **Time axis**: filing date bands (pioneer period / growth period / mature period /
   recent filings — last 3 years)

Generate a technology-time matrix:

- Each cell: sub-domain × time period combination
- Cell intensity: number of active patent families
- WHITE SPACE cells: sub-domains with low or no patent coverage

**White space validation checklist** — before declaring a white space:

- [ ] Do any broad independent claims in adjacent HIGH DENSITY cells potentially cover
      the white space via doctrine of equivalents or broad functional language?
- [ ] Is the white space vacant because the technical approach has not been shown to work,
      or because it is a genuine opportunity overlooked by the field?
- [ ] Are pending applications (published PCT or national) moving into the white space?
- [ ] Does NPL prior art exist in the white space that would prevent patenting but not
      block commercial activity?
- [ ] Is the white space protected by trade secrets rather than patents in this industry?

**7d: Citation Network Analysis**

- Identify foundational patents: high forward-citation count = likely seminal technology;
  critical FTO and licensing target
- Map citation clusters: groups of patents citing each other reveal technology lineage
  and competitive benchmarking patterns
- Identify citation bridges: patents connecting otherwise separate clusters signal
  cross-domain technology transfer or standards-essential positions
- Flag rapidly accumulating forward citations: emerging standards or blocking positions

**⟁ CLARIFY** — After completing the landscape analysis, present findings and ask before
proceeding to FTO:

- "The landscape analysis is complete. The highest-density zones are [X, Y, Z]. I
  identified [N] white space opportunities. Should I now conduct a full FTO analysis
  against [specific high-risk sub-domains], or focus FTO on a specific product feature
  set you can describe?"
- _Why this matters_: FTO analysis is labor-intensive. Directing it at landscape hotspots
  maximizes efficiency and ensures the most material risks are addressed first.

---

### Step 8: Claim Scope Analysis and FTO Assessment

_(Skip if analysis mode is landscape-only.)_

For FTO analysis, apply element-by-element claim charting of each relevant patent against
the Technology Document.

**8a: Technology Document Review**

Verify the Technology Document is complete before beginning claim analysis:

- [ ] All product/process features described, including optional and variant configurations
- [ ] Manufacturing steps documented (relevant for process patent claims)
- [ ] Materials and components specified (relevant for composition and material claims)
- [ ] Software / algorithm steps described (relevant for method and system claims)
- [ ] Geographic scope of activities defined: where manufactured, imported, sold, and used

**⟁ CLARIFY** — If the Technology Document is incomplete or ambiguous:

- "The product specification does not describe [specific feature]. Claims in [Patent X]
  appear to cover [feature]. Can you provide more detail on [feature] before I finalize
  the claim mapping?"
- _Why this matters_: An incomplete Technology Document produces false GREEN classifications.
  Missing a claim element that is actually present in the product is the primary error
  mode in FTO analysis.

**8b: Independent Claim Identification**

For each patent in the FTO scope:

1. Read all independent claims (claims not referencing another claim in their preamble)
2. Identify the claim with the broadest scope (fewest limitations) — this is the primary
   infringement risk vector
3. Parse each independent claim element-by-element for claim charting
4. Note: if a product does not infringe an independent claim, it cannot infringe any
   dependent claim of that independent claim — but assess dependent claims of high-risk
   independent claims for scope nuance and narrowing alternatives

**8c: Element-by-Element Claim Charting**

Construct a claim chart for each patent in the FTO scope:

```
Patent: [Patent Number / Title / Assignee]
Independent Claim [N]: "[Full verbatim claim text]"

| Claim Element | Product Feature | Mapped? | Notes |
|---|---|---|---|
| [Element 1] | [Product feature] | ✅ YES / ⚠️ POSSIBLY / ❌ NO | [Explanation] |
| [Element 2] | [Product feature] | ✅ YES / ⚠️ POSSIBLY / ❌ NO | [Explanation] |
| [Element 3] | [Product feature] | ✅ YES / ⚠️ POSSIBLY / ❌ NO | [Explanation] |

Overall: [Literal infringement / Possible DOE / No infringement]
```

**All-elements rule**: For **literal infringement**, every element of a claim must map
onto the product. A single element absent from the product = no literal infringement of
that claim.

**Doctrine of Equivalents (DOE)**: Even where a product does not literally include a claim
element, it may infringe if that element's function, way, and result are substantially
the same in the product. Check for prosecution history estoppel before relying on or
asserting DOE (see Step 9). DOE is the secondary risk vector after literal infringement.

---

### Step 9: Prosecution History Review

Review the prosecution history (file wrapper) for every patent classified YELLOW or RED.
Prosecution history estoppel narrows claim scope beyond the issued claim text.

**9a: Accessing the File Wrapper**

| Jurisdiction | Source                                       | Access                                                                    |
| ------------ | -------------------------------------------- | ------------------------------------------------------------------------- |
| US           | USPTO Patent Center (patentcenter.uspto.gov) | Search by patent or application number; download full prosecution history |
| EU           | EPO Patent Register (register.epo.org)       | All prosecution documents public; search by EP number                     |
| PCT          | WIPO PatentScope                             | PCT application documents including ISR and Written Opinion               |
| UK           | UK IPO file wrapper (uk.ipo.gov.uk)          | Search by UK patent number                                                |

**9b: Key Documents to Review**

- [ ] Original claims as filed — compare to issued claims to identify all amendments
- [ ] All Office Actions: note rejections (§ 101 / § 102 / § 103 / § 112) and prior art cited
- [ ] Applicant responses: identify every narrowing amendment and the stated reason
- [ ] Examiner interviews: may contain informal scope admissions not in the written record
- [ ] Notice of Allowance: allowance reasons may implicitly narrow claim scope
- [ ] Continuation / CIP applications: pending claims may be drafted to cover the product

**9c: Estoppel Analysis**

For each narrowing amendment in a RED or YELLOW patent:

1. Identify the pre-amendment vs. post-amendment claim scope (what was surrendered)
2. Identify the stated reason for the amendment (to overcome § 102/§ 103 rejection vs.
   other reasons)
3. Apply the Festo presumptive bar: a narrowing amendment for patentability reasons creates
   a presumption that the patentee surrendered the territory between original and amended
   scope (Festo Corp. v. Shoketsu Kinzoku Kogyo Kabushiki Co., 535 U.S. 722, 2002)
4. Assess rebuttal: can the patentee overcome the presumption by showing (a) the amendment
   was for a reason unrelated to patentability, (b) the equivalent was unforeseeable, or
   (c) the amendment was only tangentially related to the equivalent?
5. Document: "DOE [barred / partially barred / not barred] in [scope range] — [reason]"

**⟁ CLARIFY** — If the prosecution history is voluminous (>200 pages) and the deadline
is tight:

- "The prosecution history for [Patent X] is approximately [N] pages. Should I conduct a
  full review of all office actions and responses, or a targeted review of the most recent
  pre-allowance amendments (highest estoppel risk)?"
- _Why this matters_: Later amendments (immediately pre-allowance) carry the highest
  estoppel risk and are the most time-efficient focus for triage analysis.

---

### Step 10: Risk Classification and Scoring

Classify each patent analyzed in the FTO assessment using the FTO Risk Classification
system in the section below.

**⟁ CLARIFY** — Before finalizing risk classifications, if any borderline YELLOW/RED
decisions depend on business context not yet provided, ask:

- "Patent [X] has independent claims where [elements Y and Z] map onto the product but
  [element W] is ambiguous. The patent owner has filed [N] infringement suits in this
  field. My assessment is [YELLOW / RED] — does your organization's risk tolerance
  require me to treat borderline cases more conservatively?"
- _Why this matters_: Risk tolerance varies significantly. A pre-revenue startup often
  treats YELLOW as RED; a large firm with litigation resources may accept more YELLOW.

---

### Step 11: Quality Verification and Delivery

Before delivering any output, run the Quality Assurance Framework:

1. Run the 5 Citation Quality Gates silently. Revise all failures before delivery.
2. For every RED-classified patent, run the 3-pass Self-Interrogation. Revise if any
   pass reveals a weakness.
3. Apply Confidence Scoring to each patent risk classification.
4. Complete the Glass Box Audit Trail YAML.
5. Produce the output using the Output Format Template.

---

## FTO Risk Classification

### GREEN — No Infringement Risk

The patent does not pose a current infringement risk. The product is clear to operate with
respect to this patent under the current analysis.

**Criteria (any one of the following is sufficient):**

- At least one element of every independent claim is absent from the product and not
  infringed under DOE
- Patent is expired (20-year term lapsed; annuity not paid; or abandoned)
- Patent has been invalidated by PTAB IPR/PGR, EPO opposition, or court judgment
- Prosecution history estoppel completely bars any doctrine of equivalents theory for
  the relevant claim elements
- Patent is pending but published claims do not read on the product and continuations
  have not issued

**Examples:**

- Patent expired — final maintenance fee (7.5-year) not paid; lapsed 14 years ago
- Independent Claim 1 requires [specific element X]; product does not use [element X]
  and no DOE theory is available due to prosecution history bar
- PTAB IPR cancelled all independent claims (August 2024 — final written decision)

**Action**: Note for reference in the monitoring register. Re-evaluate if product features
change or if the patent family has pending continuation applications.

---

### YELLOW — Monitor / Caution

The patent poses a potential infringement risk warranting monitoring, design-around
evaluation, or formal legal review. Do not ignore; do not proceed without further analysis.

**Criteria (any of the following):**

- Claims read on the product under a plausible claim construction but prosecution history
  may limit DOE scope or narrow literal claim coverage
- Product may not include all claim elements under a strict literal construction but
  plausible DOE theory exists (subject to prosecution history estoppel analysis)
- Published pending application with claims not yet final — may narrow or broaden before
  issuance; represents future issuance risk
- Patent nearing expiry (≤2 years remaining) — diminishing but non-zero risk
- Patent owner is inactive (no litigation history, no current products) but patent is live
- Claims are broad but potentially vulnerable to invalidity (Alice/Mayo issues, prior art
  identified, § 112 concerns)
- Continuation family active — pending applications that may issue with specifically
  targeted claim language

**Action**: Commission formal FTO opinion from patent counsel; assess design-around
feasibility; monitor continuation filings via prosecution monitoring alert; evaluate
IPR/PGR challenge viability if invalidity arguments are strong.

---

### RED — High Infringement Risk

The patent poses a high risk of infringement requiring immediate action. Do not proceed to
commercialization without formal legal advice and a remediation plan.

**Criteria (multiple factors compound the risk):**

- All elements of at least one independent claim map literally onto the product
- Patent is valid, enforceable, and in force in the target jurisdiction
- Prosecution history does not provide meaningful scope narrowing for the relevant elements
- Patent owner has a documented history of asserting patents in this technology area
  (operating company protecting market position or active NPE/PAE)
- High forward-citation count — patent is considered foundational in the field
- Continuation family active with pending claims that may broaden or specifically
  target coverage

**Action**: Engage patent counsel immediately; commission formal FTO opinion establishing
attorney-client privilege; conduct detailed invalidity analysis; identify design-around
options; assess licensing feasibility; evaluate IPR/PGR or EPO opposition viability.

---

## Infringement Risk Scoring Framework

For each RED or YELLOW patent, produce a structured risk scorecard:

```
Patent Risk Scorecard

Patent:           [Number, e.g. US10,123,456B2] — [Title]
Assignee:         [Name] | Owner type: [Operating company / NPE / University / Government]
Jurisdiction(s):  [List of countries where patent is in force]
Expiry date:      [Date] | Remaining term: [N years]
Claim coverage:   [All elements map literally / Partial literal / DOE only / No mapping]
Prosecution:      [Not yet reviewed / Reviewed — [estoppel scope summary]]
Validity risk:    [Low / Medium / High] — [basis: prior art found / Alice/Mayo /
                  §112 issues / EPO opposition pending]
Owner assertion:  [Active (N suits filed in last 5 years) / Moderate / Inactive]
Continuation:     [No pending continuations / N pending — risk of broadening]
Overall risk:     [RED / YELLOW / GREEN]
Confidence:       [Definite / High / Probable / Possible / Unlikely] — [rationale]

Recommended actions:
1. [Specific action with owner or timeline]
2. [Design-around option, if assessed]
3. [IPR/PGR or opposition viability, if assessed]
```

---

## Prioritization Framework

### Tier 1 — Immediate Action (Deal-Breaking Risk)

Patents that must be resolved before commercialization:

- RED-classified patents with literal claim coverage, valid and in force, active-litigant
  owner
- Continuation families with pending claims in the target jurisdiction with literal
  coverage of the product
- Patents recently enforced against competitors in the same technology field
- Unitary Patents or non-opted-out European patents with literal claim coverage —
  a single UPC infringement action can block 18 EU member states simultaneously
- Standard-essential patent (SEP) declarations in relevant standards bodies
  (ETSI, IEEE, etc.) for standards-compliant products

**Action**: Engage patent counsel immediately. Do not launch without formal FTO opinion,
invalidity analysis, and a documented remediation decision (design-around, license,
challenge, accept risk with counsel sign-off).

### Tier 2 — Near-Term Action (Material Risk Requiring Resolution)

Patents requiring resolution within 90 days of planned launch:

- YELLOW-classified patents with plausible DOE coverage and prosecution history not
  yet reviewed
- Pending applications with published claims that read on the product
- RED-classified patents where strong invalidity arguments exist (IPR/PGR/opposition viable)
- Patents expiring within 18 months — assess whether waiting is more efficient than
  designing around
- Foreign (non-US) counterparts of RED-classified US patents in target jurisdictions

**Action**: Commission formal FTO opinion and invalidity analysis; assess design-around
options; initiate licensing discussions if appropriate; file IPR/PGR or opposition
petition if invalidity arguments are strong and timing allows.

### Tier 3 — Monitor (Background Risk)

Patents to track but not act on immediately:

- GREEN-classified patents (re-evaluate at product revision milestones)
- YELLOW-classified patents with very narrow claims or strong invalidity arguments
- Expired patents (no enforcement risk; valuable as prior art in validity challenges)
- Published PCT applications not yet in national phase in the target jurisdictions
- Patents held by entities with no history of assertion in this field

**Action**: Set prosecution monitoring alerts for continuation filings; re-run FTO
triage at major product revision milestones and at 12-month intervals for products
in active commercialization.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                                                              | Fail Action                                              |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every claim mapping cites a specific patent number, jurisdiction, and claim number; every legal standard cites a specific statute or case                                         | Add citation or mark [UNVERIFIED]                        |
| **Format**     | All patent citations follow standard format (US10,123,456B2; EP3456789A1; WO2023/012345A1)                                                                                        | Fix citation format to standard                          |
| **Currency**   | Every cited patent's legal status confirmed current (active / expired / abandoned); every statute confirmed not superseded                                                        | Flag [CHECK CURRENCY — status as of search date: {date}] |
| **Domain**     | Analysis stays within the target jurisdictions; do not apply US Phillips claim construction doctrine to EU Art. 69 EPC analysis, or vice versa                                    | Remove or flag [JURISDICTIONAL NOTE]                     |
| **Confidence** | Uncertainty explicitly stated: machine-translated claims flagged; large prosecution history not fully reviewed disclosed; pending applications distinguished from granted patents | Add confidence qualifier                                 |

### Self-Interrogation for RED-Risk Patents

For every patent classified RED, apply this 3-pass adversarial review before delivery.

**Pass 1 — Legal Chain Integrity**:

- Does the claim mapping follow logically from the verbatim claim language and the
  Technology Document as written?
- Would a court applying the correct claim construction standard (Phillips hierarchy for
  US; Art. 69 EPC + Protocol for EU) reach the same infringement conclusion?
- What is the strongest non-infringement argument the patent owner's litigation counsel
  would make in response to this analysis?

**Pass 2 — Completeness**:

- Have all independent claims been analyzed — not just the first or most prominent?
- Have continuation and CIP applications in the same family been checked for pending
  broader or targeted claims?
- Has the prosecution history been reviewed, or is it explicitly flagged as NOT YET
  REVIEWED in the risk scorecard?

**Pass 3 — Challenge**:

- What is the strongest invalidity argument against this patent? (Prior art identified?
  Alice/Mayo patent eligibility vulnerability? § 112 enablement or written description
  issue? § 103 obviousness over a combination?)
- Under what circumstances would reasonable patent counsel recommend accepting this risk
  rather than designing around or challenging?
- Is the owner's actual likelihood of assertion high (consider: operating company vs.
  NPE; active litigation portfolio; product competition overlap with the client's product)?

**Outcome**: Mark the audit trail with `self_interrogation: "PASS"` or
`self_interrogation: "REVISED — [what changed]"` per RED patent.

### Confidence Scoring

| Level        | Range     | Meaning                                                                                                                                             | Action                                                                        |
| ------------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | All claim elements mapped from issued verbatim claim text; legal status confirmed; prosecution history reviewed                                     | State with confidence                                                         |
| **High**     | 0.80–0.94 | Strong claim mapping; prosecution history reviewed; minor claim construction ambiguities only                                                       | State with brief caveat                                                       |
| **Probable** | 0.60–0.79 | Claim mapping relies on claim construction judgment; prosecution history not fully reviewed; DOE assessment uncertain                               | State with explicit reasoning and contra-indicators                           |
| **Possible** | 0.40–0.59 | Machine-translated claims; ambiguous product-to-claim mapping; claim construction genuinely disputed; pending application with final claims unknown | Flag for patent counsel review; present both interpretations                  |
| **Unlikely** | 0.0–0.39  | Inadequate source material; claim text unavailable or untranslated; technical domain outside confident analysis                                     | Do not assert risk classification; flag [UNCERTAIN — patent counsel required] |

---

## Glass Box Audit Trail

Every patent landscape and FTO output MUST include a Glass Box audit section at the end.
This makes the analysis traceable, auditable, and reproducible.

```yaml
glass_box:
  skill_name: "legalcode-patent-landscape-analysis"
  analysis_type: "[Landscape / FTO / Full / Validity / M&A Due Diligence]"
  technology_domain: "[Description]"
  target_jurisdictions: "[US / EU / UK / JP / CN / WIPO / Custom list]"
  analysis_date: "[Date]"

  search_parameters:
    ipc_cpc_codes_used: ["[Code 1 — description]", "[Code 2 — description]"]
    keyword_query_summary: "[Brief description of Boolean query logic]"
    date_range: "[From — To]"
    legal_status_filter: "[All / Active only / Other]"
    npl_searched: "Yes / No — [databases if yes]"
    databases_searched:
      - name: "[Database 1]"
        date: "[Date]"
        results_raw: "[N documents]"
        results_after_dedup: "[N families]"
      - name: "[Database 2]"
        date: "[Date]"
        results_raw: "[N documents]"
        results_after_dedup: "[N families]"
    anchor_documents: ["[Patent 1 if any]", "[Patent 2 if any]"]

  results:
    total_families_after_dedup: "[N]"
    patents_analyzed_for_fto: "[N]"
    red_classified: "[N]"
    yellow_classified: "[N]"
    green_classified: "[N]"
    white_spaces_identified: "[N]"
    prosecution_history_reviewed:
      - patent: "[Patent Number]"
        pages_reviewed: "[N]"
        estoppel_findings: "[Summary or 'Not reviewed — flagged for counsel']"

  legal_authority:
    legalcode_mcp: "Connected / Not connected"
    authority_reference_file: "[/tmp/legalcode-patent-research.md or 'Not created']"
    statutes_consulted:
      - "[Statute — VERIFIED (legalcode-mcp) or UNVERIFIED]"
    case_law_consulted:
      - "[Case, citation — VERIFIED (legalcode-mcp) or UNVERIFIED]"
    citations_verified: "[N VERIFIED] / [N UNVERIFIED]"

  quality:
    self_interrogation:
      - patent: "[Patent Number]"
        outcome: "PASS / REVISED — [what changed]"
    confidence_overall: "HIGH / MEDIUM / LOW — [rationale]"

  limitations:
    - "Search conducted on [date]; patent landscape changes continuously — re-run before launch"
    - "This analysis does not constitute a formal FTO opinion; does not create attorney-client privilege"
    - "[Any scope limitations, machine translation reliance, prosecution history gaps]"

  reviewer: "AI-assisted — formal FTO opinion by qualified patent attorney required before commercialization"
```

---

## Anti-Patterns

Common failures in patent landscape and FTO analysis — do not repeat these:

1. **Keyword-only searching** — Using keywords without IPC/CPC classification codes
   produces systematically incomplete results. Foreign-language patents (Japanese, Chinese,
   German) may use entirely different terminology; classification codes are language-
   independent and must be included in every professional-grade search.

2. **Single database reliance** — No single patent database has complete global coverage.
   Using only Google Patents or only Espacenet misses documents. Cross-validate across at
   least two databases and document the cross-validation in the audit trail.

3. **Counting documents instead of families** — A US patent and its 30 national equivalents
   represent one invention. Counting individual documents inflates filing statistics by
   10–30x and distorts competitive landscape analysis. Always deduplicate to DOCDB simple
   families for counting; use INPADOC extended families for geographic coverage mapping.

4. **Ignoring pending applications** — A pending application is not yet an infringement
   threat — but it will become one on issuance. Continuation claims in particular may be
   drafted after the product is public to specifically cover visible features. Always
   search published pending applications and set monitoring alerts.

5. **Skipping prosecution history for RED patents** — The issued claim text alone does not
   determine infringement scope. Prosecution history estoppel (Festo, 2002) and argument-
   based estoppel can dramatically narrow even broadly-written issued claims. A RED
   classification without prosecution history review is incomplete and must be so labeled.

6. **Treating FTO as a one-time event** — Patent landscapes change continuously: patents
   expire, new patents issue, continuation claims file, patents transfer to PAEs, IPR
   proceedings succeed or fail. FTO analyses must be refreshed at major product revision
   milestones and at 12-month intervals for products in active commercialization.

7. **No non-patent literature (NPL) search** — In R&D-intensive fields (biotech, pharma,
   materials science, AI/software), published research articles and conference papers
   constitute prior art under § 102 / EPC Art. 54. Limiting the search to patents
   produces an incomplete validity analysis and may miss invalidating prior art.

8. **Geographic tunnel vision** — Analyzing only the home market. A patent filed in
   Germany may block manufacturing for export to any jurisdiction. A US patent does not
   block activities in France. FTO must address the jurisdictions of manufacture,
   importation, sale, and use separately for each identified RED patent.

9. **Conflating landscape with FTO** — A landscape report shows "who holds patents in
   this space" but does not answer "does my specific product infringe specific claims."
   A landscape showing few patents does not establish FTO clearance — a single foundational
   patent with broad independent claims can cover an entire sub-domain.

10. **Ignoring assignee normalization** — "General Electric," "GE," "GE Healthcare," and
    dozens of subsidiary names are one corporate family. Failure to normalize assignee
    names produces material underestimation of dominant portfolio holders' true coverage
    and understates competitive concentration.

11. **Over-reliance on abstract/title screening for FTO** — Claims govern infringement,
    not abstracts. A patent with a misleading title or abstract may have claims of critical
    relevance. In FTO analysis, the full claims of every potentially relevant patent must
    be read, not screened by abstract alone.

12. **Declaring white space without validation** — Identifying low patent density in a
    sub-domain and concluding it is "open" without validating: are any broad independent
    claims in adjacent zones potentially covering this space via DOE? Are pending
    applications moving in? Is the space vacant because the technology does not work?

13. **Failing to assess UPC opt-out status (post-June 2023)** — For European FTO, not
    checking whether a relevant European patent has opted in or out of UPC jurisdiction
    is an error of omission. A non-opted-out EP patent now anchors a potential pan-
    18-member-state infringement action — a qualitatively different risk profile than
    a bundle of national patents.

14. **Omitting design-around analysis** — Identifying a RED patent without assessing
    design-around feasibility is an incomplete analysis. Even a brief technical note
    ("removing [element X] from the product would require [description of redesign
    impact]") materially improves the action-value of the FTO output.

15. **Treating the FTO as a guarantee of clearance** — No FTO search can guarantee true
    freedom to operate. Inherent uncertainty sources: unpublished applications (publish
    at 18 months), continuation claims filed after the search date, and post-filing claim
    amendments. The Glass Box audit trail must document these limitations explicitly.

16. **Failing to distinguish NPE from operating company risk** — A RED patent held by a
    PAE requires different mitigation than one held by a direct competitor. PAEs assert
    readily but typically prefer licensing settlements. Operating companies may seek
    injunctive relief to block market entry. Risk mitigation strategy must account for
    owner type.

17. **Analyzing only the first independent claim** — Analyzing Claim 1 and ignoring other
    independent claims of the same patent. A patent may have multiple independent claims
    with different scope. Claim 10 may cover a design-around of Claim 1.

18. **Conflating patentability search with FTO search** — A prior art search for
    patentability asks "is my invention novel and non-obvious?" and does not answer "will
    my product infringe someone else's claims?" These require different search scopes,
    different analysis frameworks, and produce different outputs. A patentability search
    can complement FTO but does not replace it.

---

## Writing Standards

### For FTO Risk Summaries (shared with business stakeholders)

- Write in plain language accessible to a non-patent-attorney reader
- Active voice, short sentences: "Patent X covers [feature]. Our product includes [feature].
  Risk is RED." — not "It has been observed that a potential risk may be present."
- Name the actor: "Assignee [Company] holds Patent X" — not "Patent X is held by"
- Quantify where possible: "7 RED patents require immediate action; 12 YELLOW patents
  require monitoring before launch"
- Never soften a RED classification with hedging language to make it easier to deliver —
  do not dilute "HIGH INFRINGEMENT RISK" into "some potential IP considerations"

### For Patent Claim Analysis (shared with patent counsel)

- Quote the relevant claim elements verbatim — do not paraphrase claim language
- Reference the claim number and element number precisely
- Document the Technology Document basis for each product-to-claim mapping
- Flag with [CLAIM CONSTRUCTION JUDGMENT] any mapping that depends on interpretation
  rather than literal reading
- Note confidence level per claim chart entry using the 5-level scale

### Quality Gates Before Delivery

1. Can a business decision-maker understand the top-line risk summary without reading
   the claim charts?
2. Can patent counsel reconstruct the claim mapping from the analysis without access
   to additional materials?
3. Is every RED classification backed by a specific patent number, a specific claim number,
   and a specific element-by-element mapping?
4. Are all legal status checks current? (Confirm search date in Glass Box audit trail.)
5. Have all passive constructions, redundant qualifiers, and unnecessary hedging been
   removed from the risk summary?

---

## Analysis Reference

### Database Coverage Matrix

| Database                       | Coverage                                          | Access                         | Strengths                                                                       | Limitations                                  |
| ------------------------------ | ------------------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------- | -------------------------------------------- |
| **USPTO Patent Public Search** | All US patents (1976+) and published apps (2001+) | Free — ppubs.uspto.gov         | Boolean + CPC field search; CPC classification browser                          | US-only without family data                  |
| **USPTO Patent Center**        | US prosecution history (all applications)         | Free — patentcenter.uspto.gov  | Complete file wrapper; real-time status                                         | US only                                      |
| **EPO Espacenet**              | 150M+ documents; 100+ countries                   | Free — worldwide.espacenet.com | Best features for searching; INPADOC family data; CPC; machine translation      | Some national collections incomplete         |
| **EPO Patent Register**        | EP prosecution history                            | Free — register.epo.org        | EP file wrapper; UPC opt-out status                                             | EP only                                      |
| **WIPO PatentScope**           | PCT applications + 70+ national offices           | Free — patentscope.wipo.int    | Best for analysis tools; CLIR multilingual; ISR documents                       | PCT-focused; national coverage varies        |
| **JPO J-PlatPat**              | Japanese patents + FI/F-term                      | Free — j-platpat.inpit.go.jp   | FI/F-term unique classification; English machine translation                    | Machine translation quality variable         |
| **Google Patents**             | 120M+ documents; multilingual                     | Free — patents.google.com      | Accessible; semantic search; no subscription                                    | Not suitable as sole database for formal FTO |
| **Derwent Innovation**         | DWPI curated; 100M+                               | Commercial — Clarivate         | Expert-rewritten abstracts; Derwent Manual Codes; superior for chemistry/pharma | Cost; subscription required                  |
| **PatSnap**                    | 130M+ documents                                   | Commercial                     | AI semantic search; strong visualization; R&D integration                       | Cost                                         |
| **Orbit Intelligence**         | 100M+ patents; 150M scientific docs               | Commercial — Questel           | 97%+ machine translation; SEP analysis; strong multi-jurisdiction FTO           | Cost                                         |
| **CAS STNext / SciFinder**     | INPADOCDB + INPAFAMDB + NPL                       | Commercial                     | Best for pharma/bio patent + NPL combined search                                | Cost; specialty focus                        |

### IPC Classification — Key Technology Areas

| Technology Domain             | Primary IPC Class                              | Notes                                                  |
| ----------------------------- | ---------------------------------------------- | ------------------------------------------------------ |
| Pharmaceuticals / biologics   | A61K                                           | Cross-reference A61P (therapeutic use)                 |
| Medical devices               | A61B, A61F, A61N                               | Cross-reference G16H for digital health                |
| Software / computing          | G06F, G06N                                     | G06N for AI/ML; cross-reference H04 for communications |
| Semiconductors / electronics  | H01L, H04B                                     | H01L for devices; H04B for transmission                |
| Electric vehicles / batteries | B60L, H01M                                     | H01M for energy storage                                |
| Telecommunications            | H04L, H04W                                     | H04W for wireless                                      |
| Biotechnology                 | C12N, C12Q                                     | C12N for microorganisms; C12Q for diagnostic methods   |
| Chemistry / materials         | C07, C08, C09                                  | Broad — use CPC for finer granularity                  |
| Mechanical engineering        | F16, B23, F01                                  | Context-dependent                                      |
| Clean energy                  | F03D (wind), F24S (solar), C25B (electrolysis) | Cross-reference H02 for electrical systems             |

### PCT Timeline Reference

| Event                                               | Timing      | Significance                                                 |
| --------------------------------------------------- | ----------- | ------------------------------------------------------------ |
| PCT application filed                               | Month 0     | Priority date established                                    |
| International Search Report (ISR) + Written Opinion | Month 16    | Non-binding prior art assessment; X/Y/A citations            |
| PCT publication by WIPO                             | Month 18    | Application becomes prior art; publicly searchable           |
| Optional: IPEA Demand (Chapter II examination)      | Month 22    | Refined written opinion before national phase                |
| National/regional phase entry deadline              | Month 30–31 | Varies by country; extensions possible in some jurisdictions |

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 3, search for jurisdiction-relevant patent statutes, claim construction case law,
  and recent Federal Circuit / UPC decisions relevant to the technology domain
- Save verified legal references to `/tmp/legalcode-patent-research.md`
- Use verified case law citations in risk assessments — do not rely on memory for case
  holdings, claim construction holdings, or damages precedent
- For technology-specific § 101 eligibility decisions, search legalcode-mcp by case name
  and jurisdiction to confirm current Alice/Mayo application
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with general patent law knowledge from training data
- Mark every statutory and case law reference with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus analysis on claim mapping and patent text; flag all legal authority as unverified

**Patent database access:**

- If the user has access to a commercial platform (Derwent Innovation, PatSnap, Orbit,
  PatBase), note this in the Glass Box audit trail and leverage its family consolidation
  and assignee normalization features
- If only free public databases are available, document this as a scope limitation and
  recommend professional-grade database review for RED-classified patents
- If no patent database is accessible: stop and inform the user — FTO and landscape
  analysis cannot be conducted responsibly without access to patent documents

**Graceful degradation if only Google Patents is available:**

- Document in Glass Box: "Search limited to Google Patents — completeness not guaranteed;
  professional database review required before reliance on any GREEN classification"
- Downgrade maximum confidence to Probable (0.60–0.79) — no analysis can reach Definite
  or High without multi-database cross-validation

---

## Output Format Template

````markdown
# Patent Landscape and FTO Analysis Report

**Technology Domain**: [Description]
**Analysis Type**: [Landscape / FTO / Full / Validity / M&A Diligence]
**Target Jurisdictions**: [List]
**Analysis Date**: [Date]
**Conducted by**: AI-assisted (legalcode-patent-landscape-analysis) — requires patent
attorney review before reliance

---

## Executive Summary

**Overall IP Risk Level**: [LOW / MODERATE / HIGH / CRITICAL]

**Key Findings**:

- [Finding 1 — most material risk or opportunity]
- [Finding 2]
- [Finding 3]

**Immediate Actions Required**: [List or "None — see Tier 2/3 monitoring items"]

---

## Landscape Analysis Results

_(Omit if FTO-only mode)_

### Filing Trend Analysis

[Data table or narrative: volume by year; top 10 assignees over time; sub-domain trends]

### Technology Density Map

| Sub-Domain     | IPC/CPC Range | Family Count | Density                       | White Space? |
| -------------- | ------------- | ------------ | ----------------------------- | ------------ |
| [Sub-domain 1] | [Codes]       | [N]          | HIGH / MODERATE / WHITE SPACE | Yes / No     |

### Top Assignees

| Rank | Assignee | Families | Filing Trend | Owner Type | Assertion History |
| ---- | -------- | -------- | ------------ | ---------- | ----------------- |

### White Space Opportunities

| Opportunity | IPC/CPC Range | Validation Status | Strategic Recommendation |
| ----------- | ------------- | ----------------- | ------------------------ |

### Citation Network Observations

[Foundational patents; citation clusters; emerging positions; bridging patents]

---

## FTO Analysis Results

_(Omit if landscape-only mode)_

### Risk Summary

| Risk Level          | Count | Patent Numbers |
| ------------------- | ----- | -------------- |
| 🔴 RED — High Risk  | [N]   | [Numbers]      |
| 🟡 YELLOW — Monitor | [N]   | [Numbers]      |
| 🟢 GREEN — Clear    | [N]   | [Numbers]      |

### Tier 1 — Immediate Action Required

#### [Patent Number] — [Title] | 🔴 RED | Confidence: [Level]

**Assignee**: [Name] | **Expiry**: [Date] | **Owner Type**: [Operating / NPE / University]
**Risk Basis**: [One paragraph: why this is RED; cite claim; cite product feature]
**Key Claim**:

> "[Verbatim text of relevant independent claim]"
> **Claim Chart Summary**:
> | Element | Product Feature | Mapped? |
> |---|---|---|
> | [Element 1] | [Feature] | ✅ YES |
> | [Element 2] | [Feature] | ✅ YES |
> **Prosecution History**: [Reviewed — [estoppel findings] / Not yet reviewed]
> **Invalidity Assessment**: [Prior art identified / Alice-Mayo risk / § 112 issues / None identified]
> **Design-Around Feasibility**: [Assessment]
> **Recommended Action**: [Specific steps]

[Repeat for each Tier 1 patent]

### Tier 2 — Near-Term Action Required

#### [Patent Number] — [Title] | 🟡 YELLOW | Confidence: [Level]

[Same format, abbreviated as appropriate]

### Tier 3 — Monitor

| Patent | Assignee | Expiry | Risk Basis | Monitor Trigger |
| ------ | -------- | ------ | ---------- | --------------- |

---

## Competitive Intelligence Summary

**Key players and strategic posture:**
[One paragraph per major assignee: filing rate, technology focus, litigation profile]

**Emerging entrants (last 3 years)**:
[List with filing volume and technology focus]

---

## Recommended IP Strategy

### Patenting Recommendations

[White space opportunities worth patenting; design-around innovations that may be
patentable in the white spaces identified]

### Licensing Recommendations

[Tier 1 patents worth licensing-in to resolve RED risk; any licensing program opportunities
if the client holds patents in adjacent zones]

### Challenge Recommendations

[Patents vulnerable to IPR/PGR petition; EPO opposition candidates; invalidity arguments]

### Monitoring Plan

[Prosecution monitoring alerts to set; re-run FTO trigger events]

---

## Glass Box Audit Trail

```yaml
[Insert completed Glass Box YAML]
```
````

---

_This report was produced using the legalcode-patent-landscape-analysis AI skill. It does
not constitute a formal Freedom-to-Operate opinion and does not create attorney-client
privilege. RED-classified findings require formal legal review by a registered patent
attorney before any commercialization decision._

```

---

## Localization Notes

**US Market** (primary litigation risk jurisdiction):
- Apply Phillips claim construction hierarchy — intrinsic evidence (claims, specification,
  prosecution history) governs claim meaning; extrinsic evidence secondary
- Assess Alice/Mayo patent eligibility as an invalidity dimension for software, business
  method, life science diagnostic, and AI-related patents
- Review continuation and CIP family status via USPTO Patent Center
- Consider IPR/PGR challenge at PTAB for RED patents with strong invalidity arguments;
  note proposed PREVAIL Act reforms to IPR standard [VERIFY current legislative status]
- Consider ITC Section 337 investigation risk for import-blocking in addition to district
  court infringement for products manufactured abroad
- Willful infringement exposure (§ 284 enhanced damages up to 3x) if the RED patent was
  known to the client before launch without remediation

**EU / UPC** (significantly elevated stakes post-June 2023):
- Check opt-out status of all European patents at register.epo.org per patent — this
  determines UPC vs. national court jurisdiction
- Unitary Patents: no national validation required; treat as the highest-priority FTO
  target for pan-European commercialization
- UPC preliminary injunction: "more likely than not" standard — lower bar than some
  national courts; risk of launch-blocking injunction is real for RED patents
- EPO opposition (within 9 months of grant): cost-effective invalidity challenge;
  consider for RED EP patents with strong novelty/inventive step arguments
- UK requires separate FTO analysis post-Brexit; UK courts operate independently of UPC

**Japan**:
- J-PlatPat is authoritative; FI/F-term classification supplements IPC — use both
- Machine-translated claims carry additional uncertainty: flag with [MACHINE TRANSLATION]
  and recommend qualified human translation for any RED or YELLOW Japanese patent
- Consider utility model (実用新案) registrations for consumer product FTO — shorter
  examination, no substantive examination required; can be asserted quickly

**China (CNIPA)**:
- Largest patent volume globally; must include for any global FTO analysis
- Separate invalidity proceedings via CNIPA Patent Reexamination and Invalidation Division
- Chinese courts have significantly increased patent damage awards since 2019; no longer
  a jurisdiction to treat as low-risk
- Inventiveness standard may differ from US § 103 / EPC Art. 56 — some claims valid in
  China may face stronger obviousness attacks in other jurisdictions, and vice versa

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis combining:
- WIPO Guidelines for Preparing Patent Landscape Reports (WIPO Publication No. 946E,
  A. Trippe, 2015) — methodology for landscape reports
- USPTO, EPO, and WIPO database documentation and comparative search studies
- Phillips v. AWH Corp., 415 F.3d 1303 (Fed. Cir. 2005) — claim construction doctrine
- Festo Corp. v. Shoketsu Kinzoku Kogyo Kabushiki Co., 535 U.S. 722 (2002) — prosecution
  history estoppel framework
- Alice Corp. v. CLS Bank International, 573 U.S. 208 (2014) — patent eligibility
- USPTO 2024 Guidance Update on Patent Subject Matter Eligibility (July 2024)
- UPC statistics and Court of Appeal case law (2023–2025)
- Unified Patent Court operational analysis (Clarivate, 2024; Baker McKenzie, 2026)
- PREVAIL Act and USPTO PTAB proposed rule changes (2025)
- Legalcode reference standard: skills/general/contracts/legalcode-contract-review/SKILL.md
- 2-agent research pipeline: structural analysis agent (reference skill pattern extraction)
  + legal research agent (US/EU/WIPO/JP patent law frameworks, databases, anti-patterns)
```
