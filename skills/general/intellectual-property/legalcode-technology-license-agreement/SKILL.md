---
name: legalcode-technology-license-agreement
description: Structure, draft, review, and negotiate technology and IP license agreements covering the
  full commercial deal lifecycle across US, EU, and UK frameworks. Use when drafting a technology license
  from scratch, reviewing a proposed agreement for deal-term acceptability, or advising on the commercial
  structure of a patent license, software license, know-how license, technology transfer, or mixed-IP
  bundle license.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Structure, draft, review, and negotiate technology and IP license agreements covering the full commercial deal lifecycle across US, EU, and UK frameworks. Use when drafting a technology license from scratch, reviewing a proposed agreement for deal-term acceptability, or advising on the commercial structure of a patent license, software license, know-how license, technology transfer, or mixed-IP bundle license. Deep analysis of: grant scope (exclusive, non-exclusive, sole), field-of-use restrictions, territory and sublicensing rights, royalty structures (running royalties, milestones, minimum annual royalties, hybrid structures, MFL clauses), royalty base and SSPPU analysis, improvement and grant-back provisions (antitrust-screened), royalty audit rights, source code escrow (trigger events, verification levels, SaaS alternatives), patent exhaustion (Quanta/Impression Products, EU/UK divergence), IP indemnification (structure, remedy waterfall, caps, carve-outs), and termination effects on licensed rights including licensor insolvency protections under 11 U.S.C. § 365(n). Produces GREEN/YELLOW/RED severity-classified findings, deal-term redlines, royalty negotiation guidance, and a Glass Box audit trail. Complements legalcode-technology-license-review (which focuses on antitrust/TTBER compliance and competition-law screening); this skill focuses on commercial deal structure and IP rights mechanics. Triggers on any request to draft, review, structure, or negotiate a technology license, IP license, patent license, technology transfer agreement, software license (perpetual, subscription, SaaS), or know-how license.


# Legalcode Technology License Agreement

> **Disclaimer**: This skill provides a framework for AI-assisted drafting, review, and
> negotiation of technology and IP license agreements. It does not constitute legal advice.
> All outputs should be reviewed by a qualified legal professional licensed in the relevant
> jurisdiction — preferably with IP, licensing, or technology transactions experience — before
> use. Laws change; verify current applicability before relying on any provision described
> here. Statutory and case law references are derived from research and carry hallucination
> risk — verify against authoritative sources (LII, EUR-Lex, BAILII, national patent offices)
> before relying on them. Competition law compliance (TTBER, Sherman Act, Chapter I of the
> Competition Act 1998) and bankruptcy/insolvency analysis (§ 365(n)) require specialist
> counsel; this skill provides a framework, not a definitive analysis.

---

## Purpose and Scope

This skill assists in the full commercial lifecycle of a technology and IP license agreement —
from initial deal structure through drafting, negotiation, and execution.

**Covers:**

- Drafting and structuring technology license agreements (guided workflow)
- Reviewing proposed agreements against market-standard commercial positions
- Grant scope analysis: exclusive, non-exclusive, sole licenses; field-of-use and territory
- Sublicensing rights: conditions, flow-down, survival on termination
- Royalty structures: running royalties, milestone payments, minimum annual royalties (MARs),
  most-favored licensee (MFL) clauses, hybrid structures, royalty stacking solutions
- Royalty base analysis: SSPPU vs. entire market value rule (EMVR)
- Improvement and grant-back provisions with antitrust screening
- Royalty audit rights: frequency, scope, cost allocation, underpayment thresholds
- Source code escrow: trigger events, verification levels, SaaS alternatives
- Patent exhaustion: Quanta, Impression Products, EU/UK divergence
- IP indemnification: structure, remedy waterfall, caps and carve-outs
- Termination effects on licensed rights and licensor insolvency protections (§ 365(n))
- Background IP vs. foreground IP delineation in technology development contexts

**Does not:**

- Perform competition law / antitrust screening under EU TTBER or US Sherman Act (see
  `legalcode-technology-license-review` for TTBER safe harbor analysis and SEP/FRAND)
- Perform freedom-to-operate or patent validity analysis
- Perform export control screening (ITAR / EAR / UK Strategic Export Controls)
- Replace specialist IP, licensing, bankruptcy, or antitrust counsel
- Address AI/ML-specific model licensing or open source compatibility matrix (see
  `legalcode-technology-license-review`)

**Complementary skills:**

- `legalcode-technology-license-review` — antitrust/competition law compliance, TTBER
  safe harbor assessment, SEP/FRAND, open source compatibility
- `legalcode-ip-assignment-agreement` — outright assignment (rather than licensing) of IP
- `legalcode-nda-triage` — confidentiality/NDA before licensing discussions

---

## Jurisdiction and Governing Law

This skill covers three primary frameworks. Identify the governing law clause early and
apply the correct framework throughout.

**US Framework:**

- Patents: 35 U.S.C. §§ 154, 261–262, 271 (ownership, licensing, infringement)
- Copyright: 17 U.S.C. §§ 101, 106, 204 (exclusive rights, licenses, writing requirement)
- Trademark: 15 U.S.C. §§ 1051–1127 (Lanham Act; naked licensing doctrine)
- Trade Secrets: Defend Trade Secrets Act (DTSA), 18 U.S.C. § 1836; state UTSA variants
- Bankruptcy: 11 U.S.C. § 365(n) (licensee protection on licensor insolvency)
- Bayh-Dole Act: 35 U.S.C. §§ 200–212 (government rights in federally funded IP)
- Patent exhaustion: _Quanta Computer v. LG Electronics_, 553 U.S. 617 (2008);
  _Impression Products v. Lexmark International_, 581 U.S. \_\_\_ (2017)
- Trademark in bankruptcy: _Mission Product Holdings v. Tempnology_, 139 S. Ct. 1652 (2019)

**EU Framework:**

- Technology Transfer Block Exemption Regulation: Reg. 316/2014 (in force until 30 April 2026)
- Draft revised TTBER (European Commission, September 2025; effective 1 May 2026 — extends
  safe harbor grace period; adds data licensing guidance; removes passive sales from
  hardcore list) [VERIFY final adopted text against Official Journal]
- Software Directive: Directive 2009/24/EC
- Unitary Patent Regulation: Reg. 1257/2012 (Unified Patent Court in force 1 June 2023)
- EU Data Act: Reg. 2023/2854 (data licensing implications)
- Patent exhaustion: _Merck v. Primecrown_, Cases C-267/95 & C-268/95 (CJEU 1996);
  _UsedSoft v. Oracle_, C-128/11 (CJEU 2012) (download exhaustion)

**UK Framework (Post-Brexit):**

- Patents Act 1977: ss. 60–68 (infringement, exclusive licensee rights), ss. 48–54
  (compulsory licences)
- CDPA 1988: ss. 90–92 (assignment and licensing; exclusive licence definition)
- Trade Marks Act 1994
- IP Exhaustion: UK+ regime — EEA-to-UK imports treated as exhausted; **not reciprocal**
  (UK-to-EU imports not exhausted in the EU). Now confirmed as the permanent regime
  (IP Update, May 2025) [VERIFY current UKIPO position]
- National Security and Investment Act 2021 (licensing to certain foreign persons/entities
  may require government notification and approval)
- UK TTBER (assimilated EU law) transitions to domestic block exemption order 1 May 2026
  (CMA consultation, March 2025) [VERIFY enacted instrument]

[JURISDICTION-SPECIFIC] For governing law outside US/EU/UK, research: local IP ownership
defaults, technology transfer approval requirements (China SAMR, India DPIIT), compulsory
license regimes, mandatory royalty rate caps (pharmaceutical licensing), government use
rights, and local language requirements for license agreements.

---

## Interactive Clarification

This skill uses interactive clarification at key decision points. Pause and ask when:

- The mode is unclear (drafting from scratch vs. reviewing an existing agreement)
- The type of IP being licensed is ambiguous (patent only, copyright only, mixed bundle)
- The parties' relationship is unclear (competitors vs. non-competitors affects antitrust risk)
- Royalty base, structure, or deal economics are undetermined
- Whether federally funded IP is involved (Bayh-Dole march-in right implications)
- Whether any personal data is included in the licensed technology (GDPR Article 28 overlay)
- The user's side is not stated (licensor vs. licensee analysis is asymmetric)

Use the **⟁ CLARIFY** marker below to indicate where to pause and ask.

---

## Workflow

### Step 1: Determine Mode and Accept Input

This skill operates in two modes:

**Mode A — Draft**: Help structure and draft a technology license agreement.
**Mode B — Review**: Analyze an existing or proposed technology license agreement.

**⟁ CLARIFY** — If the mode is not clear from context, ask:

1. **What would you like to do?**
   - Option A: **Draft** a technology license agreement from scratch (guided deal structure)
   - Option B: **Review** a proposed or existing agreement (clause-by-clause analysis)
   - Option C: **Negotiate** a specific provision (targeted redline generation)

2. **What type of IP is being licensed?**
   - Patent rights (right to make, use, sell)
   - Software / copyright (right to reproduce, distribute, use)
   - Know-how / trade secrets
   - Mixed bundle (patent + copyright + know-how)
   - Technology transfer (including all of the above plus development rights)

3. **What is your role?**
   - Licensor (IP owner granting rights)
   - Licensee (recipient of rights)
   - Advisor to one of the above
     _Why this matters_: The entire analysis is asymmetric — licensor and licensee objectives
     are often directly opposed.

### Step 2: Gather Deal Context

**⟁ CLARIFY** — Before analysis, gather:

1. **Exclusivity**: Exclusive, sole, or non-exclusive? If exclusive, full or field-limited?

2. **Field of use**: What industry, application, or product type is the license limited to?
   Or is it unrestricted?

3. **Territory**: Global, specific countries, or specific regions?

4. **Royalty structure**: Running royalties, milestones, lump-sum, hybrid? Is there a
   minimum annual royalty requirement?

5. **Term**: Perpetual or fixed term? Renewal rights?

6. **Technology type**: What does the licensed technology do? What products will be made
   using it? (Needed for royalty base and scope analysis)

7. **Background/foreground**: Is this a pure license of existing IP, or does the agreement
   involve joint development or customization creating new foreground IP?

8. **Special considerations**:
   - Is the IP federally funded (Bayh-Dole Act implications)?
   - Are any open source components included?
   - Are there standard-essential patents (SEP/FRAND obligations)?
   - Is the licensed technology subject to export controls?

If the user provides partial context, state assumptions explicitly and proceed.

### Step 3: Gather Legal Authority (if legalcode-mcp is connected)

Use **legalcode-mcp** to build a legal reference file for this deal:

1. Research the governing law jurisdiction's IP licensing rules (formalities, assignment
   requirements, mandatory provisions)
2. Search for any recent case law affecting the relevant IP type and jurisdiction
3. If the deal involves patents, check for any applicable FRAND or compulsory license issues
4. Save results to `/tmp/legalcode-techlicense-authority.md`

Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:** Proceed with general commercial knowledge; mark
all statutory and case law references with [VERIFY].

### Step 4A: Guided Drafting Workflow (Mode A)

Follow this sequence to structure the agreement:

1. **Define the parties and recitals**: Identify licensor, licensee, and purpose of the
   license. Recitals should describe the technology and the commercial context.
2. **Draft the Definitions** (Section 1): Start here — ambiguous definitions are the
   single most common source of licensing disputes. See Section 4 (Definitions) below.
3. **Draft the Grant** (Section 2): The commercial heart of the agreement. Follow the
   Grant Clause Analysis (see Topic 1).
4. **Draft the Financial Terms** (Section 3): Royalties, milestones, MARs, audit rights.
   Follow the Royalty Structure Analysis (see Topic 3).
5. **Draft IP Ownership and Improvements** (Section 4): Background/foreground IP,
   grant-back provisions. Follow Topic 5.
6. **Draft Source Code Escrow** (Section 5, if applicable): Trigger events, escrow agent,
   verification level, release license. Follow Topic 6.
7. **Draft Indemnification** (Section 6): IP infringement defense and indemnity. Follow
   Topic 8.
8. **Draft Limitation of Liability** (Section 7): Cap amount, carve-outs.
9. **Draft Term and Termination** (Section 8): Including effects on licensed rights and
   sublicenses. Follow Topics 7 and 9.
10. **Draft Confidentiality** (Section 9): Protection of know-how and deal terms.
11. **Draft Representations and Warranties** (Section 10): Licensor's warranties (IP
    ownership, no encumbrances, no third-party claims).
12. **Draft Boilerplate** (Section 11): Governing law, disputes, notices, assignment,
    entire agreement.

**⟁ CLARIFY** — Before drafting each major section, confirm any deal-specific parameters
(royalty rate, field of use, territory, etc.) not already provided.

### Step 5A: Quality Check for Drafted Agreement (Mode A)

Before delivering a drafted agreement:

1. Verify all cross-references between sections are consistent
2. Confirm all defined terms are used consistently and defined before first use
3. Verify jurisdiction-specific formality requirements are met (e.g., written form for UK
   copyright assignment under CDPA 1988, s.90(3))
4. Run the Citation Quality Gates silently (see Quality Assurance Framework)
5. Confirm the Glass Box Audit Trail is complete

### Step 4B: Review Workflow (Mode B)

Read the entire agreement before flagging issues — clauses interact with each other
(e.g., a broad grant-back may be partially mitigated by a non-exclusive royalty structure,
but could still raise competition concerns if combined with market share).

**⟁ CLARIFY** — For long agreements (30+ pages or with multiple exhibits/schedules):

- Ask whether to perform a **full review** of all 10 core topics, or a **priority review**
  focused on stated concerns (e.g., "I'm worried about the royalty base and the grant-back").
- If the agreement incorporates external terms (e.g., "subject to Licensor's Standard
  License Terms available at [URL]"), ask whether to review those as well.

Analyze all 10 core topics below. For each, classify as GREEN / YELLOW / RED.

### Step 5B: Deviations and Redlines (Mode B)

For each finding:

- **GREEN**: Note for awareness. No action required.
- **YELLOW**: Generate specific redline language, fallback position, and estimated
  business impact.
- **RED**: Explain the specific risk with legal basis, provide market-standard alternative
  language, estimate exposure, and recommend escalation path.

### Step 6: Quality Verification

Before delivering output in either mode:

1. Run the 5 Citation Quality Gates silently
2. For every RED finding, run the 3-pass Self-Interrogation
3. Assign a Confidence Score to each material analysis item
4. Generate the Glass Box Audit Trail and append to output

---

## Core Topic Analysis

### Topic 1: Grant Scope and Field-of-Use Restrictions

**The grant clause is the commercial heart of the license.** A deficient or ambiguous
grant creates downstream disputes about what the licensee is permitted to do.

**Required Elements — Every Grant Must Specify:**

| Element                          | What to Include                                                                                                | Common Omissions                                                                       |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **IP Bundle**                    | Which rights: patents (list or "all patents owned/controlled"), copyright, trade secrets, know-how, trademarks | Omitting copyright when software is included; missing divisional/continuation patents  |
| **Permitted Acts**               | Make, use, sell, offer for sale, import, reproduce, distribute, sublicense, have-made                          | Missing "have made" (contract manufacturing); missing "import" in product contexts     |
| **Territory**                    | Specific countries/regions, or worldwide                                                                       | Omitting territory entirely (creates ambiguity)                                        |
| **Field of Use**                 | Specific industry/application/product category                                                                 | Overly broad (no FOU = full scope license) or overly narrow (restricts legitimate use) |
| **Exclusivity Level**            | Exclusive / sole / non-exclusive                                                                               | No statement defaults to non-exclusive in most jurisdictions                           |
| **Scope of Licensed Technology** | Version(s) included; whether future improvements are included                                                  | Agreement silent on whether future releases are covered                                |

**Exclusivity Analysis:**

| Type              | What It Means                                                                                                                    | Licensor Can…                                                                     | Licensee Standing to Sue                                                                            |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Exclusive**     | Only licensee may exercise granted rights within scope; licensor cannot practice or sublicense within that scope unless reserved | Not practice the IP within the scope; must reserve own rights expressly if needed | US: "all substantial rights" test; UK: s.67 Patents Act — may join proceedings or sue independently |
| **Sole**          | Only licensee is a third-party licensee, but licensor retains right to practice                                                  | Practice the IP within the scope                                                  | Lower — licensee is not "all substantial rights" holder                                             |
| **Non-exclusive** | Licensor retains full freedom to license others                                                                                  | Grant identical rights to as many parties as desired                              | Generally none — personal right only                                                                |

**Field-of-Use (FOU) Restrictions:**

- FOU restrictions are procompetitive under US law (DOJ/FTC 2017 IP Licensing Guidelines):
  they allow IP owners to segment markets and promote broader dissemination [VERIFY]
- EU TTBER permits FOU restrictions within safe harbor thresholds (≤20% for competitors;
  ≤30% for non-competitors) [VERIFY current TTBER; 2026 revision may affect thresholds]
- Draft FOU with specificity: "human therapeutic applications in the field of oncology" not
  "medical applications"
- Include a mechanism to expand or narrow the FOU during the license term (option to expand
  upon milestone achievement; step-down on failure to commercialize)

**Background IP vs. Foreground IP:**
When the license involves development activity, define:

- _Background IP_: Pre-existing IP contributed by each party; each party retains ownership
- _Foreground IP_: IP created during the collaboration
- Specify ownership, license-back rights, and publication restrictions for foreground IP
- Each party should receive at minimum a non-exclusive license to use the other's foreground
  IP for internal research and development

**Severity Classification:**

| Finding                                                                     | Severity | Key Risk                                                                                       |
| --------------------------------------------------------------------------- | -------- | ---------------------------------------------------------------------------------------------- |
| No "have made" right when contract manufacturing is expected                | RED      | Licensee cannot outsource manufacture; third-party manufacturer exposed to infringement claims |
| No territory specified                                                      | YELLOW   | Ambiguity — licensor may later argue restriction to jurisdiction of formation                  |
| FOU so narrow it prevents licensee's stated business plan                   | RED      | Licensee investing in commercialization without full licensed rights                           |
| Exclusive license without licensor reservation of research rights           | YELLOW   | Licensor blocked from own research in the field                                                |
| Future versions not expressly included in definition of Licensed Technology | YELLOW   | Licensee must renegotiate for each new release                                                 |

---

### Topic 2: Sublicensing Rights

**Default Rule**: Absent express authorization, licensees cannot sublicense. The right to
sublicense is personal to the licensee unless expressly granted. This applies under US
law, UK law (CDPA 1988, s.90), and EU member state implementations.

**Sublicensing Framework:**

| Approach                                      | Description                                            | Appropriate When                                                  |
| --------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------- |
| **Prior written consent**                     | Each sublicense requires express licensor approval     | Licensor has significant interest in controlling downstream use   |
| **Blanket approval for affiliates**           | Sublicenses to affiliates permitted without consent    | Large corporate structures; licensee needs affiliate group usage  |
| **Negative consent**                          | Licensor must object within X days; silence = approval | Higher-trust relationships; streamlining high-volume sublicensing |
| **Approval not unreasonably withheld** (ANRW) | Conditional approval with reasonableness obligation    | Balance between licensor control and licensee flexibility         |

**Flow-Down Requirements (Non-Negotiable):**
Every sublicense must flow down and bind sublicensees to:

- All FOU and territorial restrictions
- Audit rights (licensor must be able to audit sublicensees directly)
- Confidentiality obligations covering licensed know-how
- IP ownership provisions (no sublicensee acquires ownership)
- Restrictions on use of licensor's trademarks and brands
- Diligence and minimum royalty obligations (if applicable)
- Prohibition on further sublicensing unless expressly permitted

**Sublicense Survival on Termination (Critical):**
Under US law (_Speedplay, Inc. v. Bebop, Inc._, Federal Circuit), sublicenses do **not**
automatically survive termination of the master license. Without express conversion language,
sublicensees lose their rights when the head license terminates.

**Best-practice options (licensor perspective vs. licensee perspective):**

| Drafting Approach                                     | Effect                                                              | Preferred By           |
| ----------------------------------------------------- | ------------------------------------------------------------------- | ---------------------- |
| Sublicenses terminate with head license               | Sublicensees have no rights post-termination                        | Licensor               |
| Sublicenses convert to direct licenses on termination | Sublicensees keep rights; licensor deals directly with sublicensees | Licensee, sublicensees |
| Sublicenses survive for wind-down period only         | Sublicensees get a defined transition period                        | Compromise             |

**Sublicense Revenue:**
Specify the licensor's share of sublicense income:

- Royalties on sublicensee net sales at the same running royalty rate (most common for
  product licenses)
- A percentage of sublicense income received by the licensee (common in university
  technology transfer: typically 25–50% of non-royalty sublicense income)
- Upfront sublicense fees may be separately allocated

**Severity Classification:**

| Finding                                                                          | Severity                                                              |
| -------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Sublicensing permitted with no flow-down of key licensor protections             | RED                                                                   |
| No conversion clause: sublicenses automatically terminate when head license ends | YELLOW (from licensee perspective); GREEN (from licensor perspective) |
| Sublicense term expressly extends beyond head license term                       | RED                                                                   |
| No audit right over sublicensees                                                 | YELLOW                                                                |
| Sublicense income definition excludes upfront sublicense fees                    | YELLOW                                                                |

---

### Topic 3: Royalty Structures

**Running Royalties:**

- _Per-unit_: Fixed dollar amount per product sold or unit manufactured. Provides certainty
  and is easy to audit. Vulnerable to product bundling and price changes.
- _Percentage of Net Sales / Revenue_: Most common form. The royalty base definition is
  critical — what deductions are permitted?

**Standard Permitted Deductions from Gross Revenue to Arrive at "Net Sales":**

- Actual discounts and rebates
- Freight, insurance, and customs duties (when invoiced separately)
- Taxes (VAT, sales tax, GST — items billed to the buyer)
- Returns and credits for defective/returned products
- _Not permitted_: Internal transfer pricing adjustments, intercompany profits, overhead

**Royalty Base Analysis — SSPPU vs. EMVR:**

| Test                                                 | Description                                                         | When Appropriate                                                                           |
| ---------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **SSPPU** (Smallest Saleable Patent-Practicing Unit) | Royalty applied to the component most closely practicing the patent | When the patent covers a sub-component; prevents windfall from unrelated end-product value |
| **EMVR** (Entire Market Value Rule)                  | Royalty applied to the entire end-product                           | Only when the patented feature drives demand for the entire product                        |

_Key authorities_: _Cornell University v. Hewlett-Packard_ (2009) [VERIFY citation];
_Ericsson v. D-Link_, 773 F.3d 1201 (Fed. Cir. 2014) [VERIFY]: SSPPU is a flexible
evidentiary tool, not a mandatory substantive rule — the essential requirement is that the
royalty reflects the incremental value the patented invention adds.

**Milestone Payments:**

- Lump sums triggered by defined development or commercial events
- Events must be specific, objectively verifiable, and time-bound: "the date on which
  the FDA accepts Licensee's New Drug Application for review" not "regulatory approval"
- Specify: creditable against future running royalties or non-creditable ("fully earned")?
- Include a mechanism to adjust milestones if development timelines shift

**Minimum Annual Royalties (MARs):**

- Floor payment regardless of actual sales; proxy for a diligence obligation
- Structure as a step-up schedule tied to commercialization milestones
- Licensor's remedy if MAR not met: license converts from exclusive to non-exclusive,
  or licensor may terminate (not automatic termination, which may be harsh)
- Shortfall payments: specify whether payment of the shortfall cures the default

**Most-Favored Licensee (MFL) / Most-Favored Nation (MFN) Clauses:**

- Require licensor to offer terms no less favorable than those offered to any other licensee
- **Antitrust risk**: Wide MFNs can softly cap effective royalty rates and are scrutinized
  under EU VBER (2022 Guidelines) and CMA guidance
- Required carve-outs to make MFL workable:
  - Settlement licenses (avoid penalizing the licensor for settling litigation)
  - Government licenses / compulsory licenses (outside the licensor's control)
  - Cross-licenses with non-monetary consideration (not comparable)
  - Licenses with substantially different scope, territory, or FOU (compare like for like)
  - Licenses granted before the MFL clause was effective

**Hybrid Structures (University / Biotech Best Practice):**

1. Upfront license fee at signing (non-refundable; reflects value of exclusive access)
2. Development milestones at defined R&D gates
3. Regulatory/commercial milestones (approval, first sale, net sales threshold)
4. Running royalties on net sales post-commercialization
5. MARs to maintain exclusivity once commercialized

**Royalty Stacking:**
When the licensee must pay royalties to multiple IP holders for the same product,
total payments may make commercialization uneconomical. Mitigation options:

- _Stacking relief clause_: Reduce the licensor's royalty rate by 50% of royalties owed
  to third parties for essential IP, subject to a floor (e.g., not below 1.5%)
- _Bundled cross-license credit_: Credit third-party royalties against the licensor's rate
- _Most-favored licensee trigger_: If licensor grants lower rates to others facing the same
  stacking problem, MFL applies

**Severity Classification:**

| Finding                                                                           | Severity |
| --------------------------------------------------------------------------------- | -------- |
| Net Sales definition includes deductions not permitted under standard practice    | YELLOW   |
| No royalty stacking provision in a multi-patent technology stack                  | YELLOW   |
| EMVR applied to entire end-product where patent covers only a sub-component       | RED      |
| MAR with automatic termination rather than conversion to non-exclusive            | RED      |
| MFL clause with no carve-out for settlement licenses                              | RED      |
| Royalty base ambiguous (references "sales" without defining gross/net)            | RED      |
| Milestone events defined by subjective criteria (e.g., licensor's "satisfaction") | YELLOW   |

---

### Topic 4: Royalty Audit Rights

**Standard Market Mechanics:**

| Element                      | Market Standard                                                                                 | Red Flag Variation                                                   |
| ---------------------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Frequency**                | Once per calendar year                                                                          | Less than once per 2 years (too infrequent)                          |
| **Advance notice**           | 30–60 days written notice                                                                       | No notice requirement (burdensome on licensee)                       |
| **Auditor**                  | Independent CPA/chartered accountant; not a licensee competitor                                 | Licensor retains its own auditors (no independence)                  |
| **Records access**           | Books, records, accounts, ERP system data, contracts (supporting royalty calculation)           | Audit limited to paper records only (inadequate for digital systems) |
| **Look-back period**         | 2–3 calendar years                                                                              | Limited to 1 year (insufficient to catch systematic underreporting)  |
| **Confidentiality**          | Audit report confidential; used only to verify royalties                                        | No confidentiality on audit findings                                 |
| **Underpayment threshold**   | 5% of royalties due for the period, or a fixed dollar floor                                     | Missing threshold (creates uncertainty about cost allocation)        |
| **Cost allocation**          | Licensee bears audit costs if underpayment ≥ 5% threshold; otherwise each party bears own costs | Licensor always bears audit costs (no incentive discipline)          |
| **Interest on underpayment** | Prime rate + 1–3 percentage points from date due                                                | No interest provision (no carrying cost for underpayment)            |

**Affiliates and Sublicensees:**

- The audit right must expressly cover **affiliates** of the licensee and, separately,
  **sublicensees** — the direct licensee's books alone will not show intercompany transfers
  or sublicensee underreporting
- Specify whether the licensor has a direct audit right against sublicensees or only an
  obligation on the licensee to enforce audit rights

**GAAP/IFRS Standards:**

- Under ASC 606 (US GAAP) and IFRS 15, royalty revenue is recognized when the subsequent
  sale or usage occurs (or when a MAR is triggered as a minimum guarantee). Auditors verify
  reports against these accounting standards.
- Specify that royalty reports must be prepared in accordance with GAAP or IFRS (as
  applicable to the licensee)

**Audit Disputes:**

- Include a dispute resolution mechanism for audit disagreements: escalation to senior
  management → independent accountant determination (binding) → arbitration
- Specify that ongoing royalty payments continue during an audit dispute

**Severity Classification:**

| Finding                                                                   | Severity |
| ------------------------------------------------------------------------- | -------- |
| No audit right whatsoever                                                 | RED      |
| Audit right limited to direct licensee; no affiliate/sublicensee coverage | RED      |
| Look-back period shorter than 2 years                                     | YELLOW   |
| No interest provision for underpayments                                   | YELLOW   |
| Underpayment threshold missing or ambiguous                               | YELLOW   |
| Auditor selected by licensee only (no independence)                       | RED      |

---

### Topic 5: Improvement and Grant-Back Provisions

**Types of Grant-Back Obligations:**

| Type                           | Description                                                                                                                     | Antitrust Treatment                                                                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Non-exclusive license-back** | Licensee grants licensor a royalty-free (or royalty-bearing) non-exclusive license to use improvements                          | Generally procompetitive (both parties benefit; licensee retains freedom to license elsewhere); within TTBER safe harbor                     |
| **Exclusive license-back**     | Licensee grants licensor exclusive rights to improvements, restricting licensee's ability to exploit improvements independently | Outside TTBER safe harbor; individual analysis required under Article 101 TFEU; scrutinized under DOJ/FTC rule of reason                     |
| **Assignment-back**            | Licensee assigns ownership of improvements to licensor outright                                                                 | Likely violates Article 101(1) TFEU if licensor has market power; may deter licensee R&D [VERIFY]; discouraged under DOJ/FTC 2017 Guidelines |

**Antitrust Screening Checklist for Grant-Back Provisions:**

1. Is the grant-back **limited to improvements of the licensed technology** specifically?
   Broad grant-backs covering all licensee innovations are the most problematic.
2. Is the grant-back **non-exclusive** (generally permissible) or **exclusive/assignment**
   (requires individual analysis)?
3. Does the licensor have **significant market power** in the technology market? If yes,
   exclusive grant-backs/assignments carry higher antitrust risk.
4. Does the grant-back **reduce the licensee's incentive to invest in R&D**? Consider
   whether the licensee can independently license and commercialize its improvements.
5. Is the grant-back **reciprocal** (licensor also grants access to its improvements)?
   Reciprocal arrangements are less likely to harm competition.

> **⟁ CLARIFY**: If the parties may be competitors (same technology market), flag that the
> grant-back requires competition law review beyond this skill's scope. Refer to
> `legalcode-technology-license-review` for TTBER antitrust screening.

**Definition of "Improvement":**
The definition is critical. Best practice:

> "'Improvement' means any modification, enhancement, or derivative work of the Licensed
> Technology that, to practice without a license, would require a license to the Licensed
> Patent Rights."

Avoid: "any invention or discovery relating to [broad technology field]" — captures
unrelated innovations.

**Royalty-Free vs. Royalty-Bearing Grant-Back:**

- Non-exclusive, royalty-free license-backs are standard in most commercial technology
  licenses (the licensor's benefit is access to improvements; the royalty is not the
  primary return on the grant-back)
- For exclusive or assignment-back, market practice is to include compensation — either
  a cash payment, cross-license, or reduced running royalty rate on the base license

**Severity Classification:**

| Finding                                                                  | Severity                    |
| ------------------------------------------------------------------------ | --------------------------- |
| Assignment-back of all improvements with no compensation                 | RED                         |
| Exclusive grant-back without compensation and with licensor market power | RED                         |
| "Improvement" defined to capture all licensee IP in the technology field | RED                         |
| Non-exclusive grant-back covering only directly related improvements     | GREEN                       |
| No grant-back provision (licensor has no access to improvements)         | YELLOW — from licensor side |
| Grant-back obligation with no time limit                                 | YELLOW                      |

---

### Topic 6: Source Code Escrow

**Purpose and Mechanics:**
A three-party arrangement where the software developer (depositor) places source code and
build materials with a neutral escrow agent. The agent releases them to the licensee
(beneficiary) upon defined trigger events.

**What Must Be Deposited:**

- Complete source code (all languages, modules, libraries, dependencies)
- Build scripts, compiler configurations, and build environment specifications
- Documentation: installation guide, architecture guide, maintenance procedures
- Third-party component list and applicable license information
- Database schemas, data structures, and seed data
- API keys and configuration files (redacted for security-sensitive elements, with a
  separate secure transmission mechanism)
- Escrow deposit must be updated with each major release (define "major release")

**Major Escrow Agents (2026):**

- NCC Group / Escode (largest UK/US provider; acquired Iron Mountain's escrow business 2021)
- Praxis Technology Escrow (US-focused)
- Codekeeper (cloud-native, automated deposit via GitHub/Bitbucket/S3 integration)
- EscrowLondon (UK-focused)

**Verification Levels:**

| Level                               | What Is Tested                                                                             | Assurance | Cost   | Recommended For                                                        |
| ----------------------------------- | ------------------------------------------------------------------------------------------ | --------- | ------ | ---------------------------------------------------------------------- |
| **Level 1** (Inventory/Readability) | Files received, readable, virus-free; matches inventory                                    | Low       | Low    | Simple agreements; where full build is already verified by other means |
| **Level 2** (Build/Compile)         | Source code compiles into working executable using deposited build scripts                 | Medium    | Medium | Most enterprise software licenses                                      |
| **Level 3** (Functionality Testing) | Full deployment in isolated lab; agreed test cases run against production environment spec | High      | High   | Mission-critical software; high-value deals                            |

**Trigger Events / Release Conditions (Standard):**

- Licensor insolvency, bankruptcy, administration, receivership, or liquidation
- Licensor's material breach of maintenance/support obligations (after cure period, typically
  30–60 days)
- Licensor ceasing to trade or winding up operations
- Licensor failing to update the escrow deposit for [X] months (typically 12 months)
- Change of control of licensor where acquirer does not assume maintenance obligations within
  [X] days of closing
- [Optional] Licensor's material breach of the license agreement (broader trigger)

**Release License Scope:**
When the escrow releases, the licensee needs rights to:

- Use, modify, and maintain the source code for its own internal purposes
- Create bug fixes and updates to maintain the software
- Engage a third-party contractor to perform maintenance (must expressly cover)
- Scope: typically limited to internal use; not to commercialize or distribute the code

**SaaS Alternatives to Traditional Escrow:**
Traditional escrow is largely inadequate for SaaS because the licensee cannot replicate
the licensor's infrastructure, third-party APIs, or continuous deployment environment.
Alternatives:

- _Recovery-as-a-Service (RaaS)_: Third party continuously mirrors the SaaS environment;
  activates a standby instance on a trigger event (best available SaaS continuity option)
- _Data escrow_: Guarantees structured data export in an agreed standard format (CSV, JSON,
  XML) within a defined timeframe upon trigger events
- _Cloud provider direct agreement_: Direct contract with the IaaS provider (AWS, Azure,
  GCP) to maintain access post-licensor failure
- _API continuity rights_: Contractual right to direct API access to underlying data sources
  if the application layer fails

**Continuous Escrow / Automated Updates:**
Given agile/DevOps release cycles, require:

- Automated deposit via git integration (GitHub, Bitbucket, GitLab) or S3/SFTP synchronization
- Periodic verification (at minimum Level 1) at each new major release
- Annual independent review of escrow completeness

**Severity Classification:**

| Finding                                                                           | Severity |
| --------------------------------------------------------------------------------- | -------- |
| No escrow provision for business-critical software                                | RED      |
| Trigger events limited to insolvency only (missing support failure and wind-down) | YELLOW   |
| No verification requirement (depositor can file empty archive)                    | RED      |
| Release license too narrow to allow maintenance by third-party contractor         | RED      |
| Escrow never updated after initial deposit (no update obligation)                 | YELLOW   |
| Traditional escrow for SaaS application (no RaaS or data portability alternative) | YELLOW   |
| Escrow license term shorter than 12–24 months needed for migration                | YELLOW   |

---

### Topic 7: Patent Exhaustion

**The Core Doctrine:**
Once a patentee (or authorized licensee) makes an **authorized sale** of a patented article,
the patentee's rights in that specific item are exhausted — the buyer and downstream
purchasers can use and resell the item without infringing the patent.

**US Framework:**

| Case                                                           | Holding                                                                                                                                                                                       | Practical Impact                                                                                        |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| _Quanta Computer v. LG Electronics_, 553 U.S. 617 (2008)       | Exhaustion extends to **method patents** if the sold item "substantially embodies" the patent (essential features embodied; no reasonable use other than to practice the patent) [VERIFY]     | Licensor must use express license conditions (not post-sale restrictions) to control downstream use     |
| _Impression Products v. Lexmark Int'l_, 581 U.S. \_\_\_ (2017) | (1) Authorized post-sale restrictions do not prevent exhaustion through **patent law** (though contract law remedies remain); (2) Exhaustion applies to **foreign authorized sales** [VERIFY] | Patent holders cannot use patent infringement as post-sale enforcement mechanism; must rely on contract |

**Practical Implications for Licensees:**

- If the licensor authorizes sales to the licensee, the patent is exhausted and downstream
  customers of the licensee are protected
- If the licensee **exceeds the scope of its license** (selling outside the FOU, territory,
  or other conditions), that sale is **not authorized** and exhaustion does not apply —
  downstream purchasers remain exposed
- Post-_Impression Products_, licensors seeking to restrict downstream use must use contract
  law, not patent infringement, against direct buyers

**EU Framework:**

- Exhaustion operates throughout the EEA once the goods are placed on the market in any
  EEA state with the IP owner's consent (_Merck v. Primecrown_, CJEU 1996) [VERIFY]
- Does not extend outside the EEA (no international exhaustion under EU law)

**UK Framework (Post-Brexit — UK+ Regime):**

- Exhaustion applies to goods placed on the market in **either the UK or the EEA** — UK
  imports from the EEA are exhausted; **not reciprocal** (EU does not treat UK goods as
  exhausted in the EU)
- Creates asymmetric parallel import exposure: goods sold first in the UK may be re-imported
  into the EU without infringing EU rights but cannot be re-imported from the UK back into
  the EU without consent
- Regime confirmed as permanent in May 2025 [VERIFY current UKIPO position]

**Method Patent Exhaustion:**
Following _Quanta_, method patent claims are exhausted when a product is sold that: (1)
substantially embodies all essential features of the method, and (2) has no other
reasonable use except to practice the method. License agreements covering software or
process patents should explicitly address whether method claims are included.

**Drafting Implications:**

- A "no-exhaustion" clause (stating that authorized sales do not trigger exhaustion) is
  **unenforceable through patent law** post-_Impression Products_ but can be enforced through
  contract law between direct parties
- Licensors seeking downstream price control should consider distribution agreements rather
  than patent licenses
- For cross-border licensing, clearly address exhaustion at EU/UK border to prevent
  unintended parallel imports

**Severity Classification:**

| Finding                                                                                                 | Severity                                                                                              |
| ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| "No exhaustion" clause attempting to restrict downstream purchasers through patent law                  | YELLOW — unenforceable through patent law; may be enforceable through contract with direct buyer only |
| License scope conditions so broad that virtually all sales are "unauthorized" (no exhaustion triggered) | RED — creates downstream licensee exposure for customers                                              |
| No mention of method patent coverage when software/process patents are licensed                         | YELLOW                                                                                                |
| UK+ exhaustion regime not addressed in cross-border US/UK license                                       | YELLOW                                                                                                |

---

### Topic 8: IP Indemnification

**Structure of an IP Indemnification Obligation:**

| Element                | Standard Market Position                                                                                                                                                                              | Common Variation                                                                |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Trigger**            | Third-party claim, suit, or proceeding alleging infringement of patent, copyright, trademark, or trade secret by the Licensed Technology                                                              | Limited to patent only; or "finally adjudicated" claims only (too narrow)       |
| **Defense obligation** | Licensor must defend (pay defense costs) and indemnify (pay damages, settlements, awards)                                                                                                             | Licensor only indemnifies; licensee must arrange its own defense                |
| **Notice**             | Prompt written notice by licensee; failure excuses licensor only if materially prejudiced                                                                                                             | Absolute notice condition with no materiality qualifier                         |
| **Defense control**    | Licensor has sole control of defense; licensee may participate with separate counsel at own expense                                                                                                   | No control right (licensor has no ability to manage its own liability exposure) |
| **Settlement**         | Licensor may not settle on terms that (i) admit licensee's liability, (ii) impose non-monetary obligations on licensee, or (iii) restrict licensee's continued use of the IP without licensee consent | Licensor has unlimited settlement authority                                     |
| **Sole remedy**        | IP indemnity is the licensee's sole and exclusive remedy for infringement claims                                                                                                                      | Sole remedy language inadvertently eliminates breach-of-warranty claims         |

**Remedy Waterfall (When Infringement Occurs):**
When a third-party IP infringement claim is asserted, the licensor typically has the right
to (in order of preference):

1. **Procure a license** from the third-party rights holder permitting continued use
2. **Modify or replace** the allegedly infringing element with a non-infringing functional
   equivalent
3. If neither (1) nor (2) is commercially feasible, **terminate** the affected license and
   refund prepaid fees for the unexpired term on a pro-rata basis

The licensee should resist any formulation that allows the licensor to skip to termination
without attempting procurement or modification first.

**Standard Carve-Outs (Indemnitor-Specified Exclusions):**
No indemnification obligation where infringement arises from:

- Modifications to the licensed IP made by or on behalf of the **licensee** without
  licensor authorization
- Combination of the licensed IP with third-party products not recommended or approved by
  the licensor ("combination claims") — NOTE: combination carve-out should be narrowed to
  combinations the licensor **could not have reasonably anticipated**
- Use of the licensed IP outside the authorized scope, FOU, or territory
- Continued use after the licensor has provided a non-infringing alternative with
  reasonable transition assistance
- Use in compliance with licensee-specified requirements that directly cause the infringement
  (reversed where the licensor is responsible for specifications)

**Caps and Liability Structure:**

| Approach                            | Description                                                                | Market Trend                                                                |
| ----------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Uncapped (traditional standard)** | IP indemnity carved out of overall liability cap; no separate limit        | Still market standard for large enterprise software and technology licenses |
| **Secondary cap (emerging)**        | IP indemnity subject to a cap of 2–5x annual fees or a fixed dollar amount | Increasing among larger SaaS vendors (2022–2024 trend)                      |
| **Super-cap**                       | Higher cap for IP indemnity than general liability, but not uncapped       | Compromise position between full cap and uncapped                           |

**Licensee Customer Pass-Through:**
In B2B deployments where the licensee deploys the licensed technology to its own customers,
ensure the indemnity explicitly covers claims brought against **the licensee's customers**
relating to the licensed technology. Without this, there is a gap: the licensor indemnifies
the direct licensee, but the licensee's customers have no protection from the licensor.

**Severity Classification:**

| Finding                                                                                    | Severity |
| ------------------------------------------------------------------------------------------ | -------- |
| No IP indemnification from licensor at all                                                 | RED      |
| "Sole remedy" language eliminates breach of IP warranty claim from same set of facts       | YELLOW   |
| Combination carve-out so broad it covers combinations the licensor should have anticipated | RED      |
| No remedy waterfall — licensor can terminate immediately on infringement claim             | YELLOW   |
| Settlement control allows licensor to force admission of liability on licensee             | RED      |
| No notice mechanism (indemnitee may lose indemnity if it defends on its own)               | YELLOW   |
| IP indemnity does not extend to licensee's customers                                       | YELLOW   |

---

### Topic 9: Termination Effects on Licensed Rights

**Termination Types and Trigger Events:**

| Termination Type                | Typical Mechanics                                             | Key Drafting Issues                                                                |
| ------------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Expiration**                  | License ends at stated term                                   | Does "expiration" trigger return/destruction obligations immediately?              |
| **Termination for cause**       | Material breach + notice + cure period (typically 30–90 days) | What is "material"? Cure period adequate?                                          |
| **Termination for insolvency**  | Ipso facto clause: automatic termination on insolvency filing | Largely unenforceable against the licensor under § 365(e)(1) (US); check local law |
| **Termination for convenience** | Either party may terminate on notice (typically 90–180 days)  | Is convenience termination available? Should it require grounds?                   |

**Survival Provisions — Must Express:**
Clauses that must expressly survive termination:

- Confidentiality obligations (typically survive for 5 years or indefinitely for trade secrets)
- Audit rights for pre-termination periods (survive for the look-back audit period)
- Indemnification and limitation of liability (survive indefinitely)
- Payment obligations for amounts accrued pre-termination
- Governing law and dispute resolution

**Wind-Down Rights:**
Licensee should obtain a wind-down period (minimum 12 months, ideally 24 months) to:

- Fulfill existing customer orders and commitments
- Migrate to a replacement technology
- Return or destroy licensed materials

**Licensor Insolvency — US (11 U.S.C. § 365(n)) — Critical Protection:**

The most important statutory protection for US licensees:

| Step                             | What Happens                                                                                                                                                                                                |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Licensor files for bankruptcy    | License is an executory contract subject to rejection by the trustee/DIP                                                                                                                                    |
| Trustee/DIP rejects the license  | Licensee may **elect** to retain IP rights under § 365(n)                                                                                                                                                   |
| Licensee makes § 365(n) election | Licensee keeps rights for the remaining term (including contractual renewal rights); retains exclusivity; must continue paying royalties; waives right to offset royalties against licensor's breach claims |
| IP types covered                 | Patents, copyrights (works of authorship), plant varieties, trade secrets — **NOT trademarks**                                                                                                              |

**Critical Drafting Steps for § 365(n) Protection:**

1. Expressly incorporate § 365(n) by reference in the agreement
2. Separate IP license fees from service fees in the payment structure — bundled
   IP + services agreements may lose § 365(n) protection if the court treats the
   entire agreement as a services contract
3. Define licensed rights as "intellectual property" under § 101(35A) of the Bankruptcy Code
4. Provide for source code escrow as a "tangible embodiment" protection: § 365(n) entitles
   the licensee to the right to use any tangible embodiment of the licensed IP

**Trademark Gap Post-Mission Product:**
_Mission Product Holdings v. Tempnology_, 139 S. Ct. 1652 (2019) [VERIFY]: rejection of
a trademark license = **breach** (not rescission), so the licensee retains whatever rights
would survive a breach under applicable non-bankruptcy contract law. Practical consequence:
the agreement must expressly provide that the trademark license **survives breach** —
otherwise the licensee may lose trademark rights post-rejection.

**EU/UK — No Equivalent to § 365(n):**
Under English law, the IP license is an executory contract. On insolvency, the
administrator/liquidator may disclaim onerous contracts. The licensee's rights depend on:
(1) whether the license creates a proprietary right (more protected) vs. a personal right,
(2) the contract's express survival provisions, and (3) any express vesting language.
Practical protections in EU/UK:

- Express survival clause
- Source code escrow (creates tangible embodiment independent of the licensor)
- Transfer IP to a bankruptcy-remote SPE before licensing
- Strong express obligations on administrators/successors to honor the license

**Sublicense Survival:**
As analyzed under Topic 2, sublicenses do not automatically survive termination of the
head license. Best practice: include an express conversion clause.

**Severity Classification:**

| Finding                                                                               | Severity                                                                |
| ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| No wind-down period upon termination                                                  | RED — licensor can immediately cut off licensee and its customers       |
| No § 365(n) election language (US governing law)                                      | RED — licensee loses IP rights on licensor insolvency                   |
| Bundled IP + services fees (no separation)                                            | YELLOW — reduces § 365(n) protection                                    |
| Trademark license not expressly stated to survive licensor breach                     | YELLOW — post-_Mission Product_ gap                                     |
| No survival clause identifying specific surviving provisions                          | RED — creates uncertainty about post-termination obligations            |
| Ipso facto clause purporting to automatically terminate on licensor insolvency filing | YELLOW — likely unenforceable under § 365(e)(1) but creates uncertainty |

---

### Topic 10: Definitions Clause

**Why Definitions Are the Most Important Section:**
Licensing disputes frequently turn on ambiguous defined terms. Definitions are the
foundation on which the entire commercial deal rests.

**Critical Definitions to Include and Review:**

| Term                                      | What to Watch For                                                                                                                                                     |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Licensed Patents / IP**                 | Does it include divisionals, continuations, continuations-in-part, reissues, reexaminations, extensions, and foreign counterparts? Or only issued patents at signing? |
| **Net Sales**                             | Are permitted deductions fully enumerated? Intercompany transfers excluded? Returns and chargebacks capped?                                                           |
| **Improvement**                           | Is scope limited to improvements to the licensed technology, or does it capture all licensee innovations in the field?                                                |
| **Affiliate**                             | Is the definition time-based (current affiliates) or inclusive of future affiliates? Does it track the standard 50% control definition?                               |
| **Sublicensee**                           | Does it include all tiers, or only direct sublicensees?                                                                                                               |
| **Licensed Products / Licensed Services** | Are these defined to correspond with the FOU and royalty scope?                                                                                                       |
| **Field of Use**                          | Precise, objective, industry-standard terminology — avoid vague qualifiers                                                                                            |
| **Confidential Information**              | Does it include know-how incorporated into the licensed technology?                                                                                                   |
| **Governmental Approval**                 | Specific to the relevant regulatory pathway (FDA, EMA, CMA, etc.) for milestone payment triggers                                                                      |
| **Knowledge**                             | For rep/warranty purposes: actual knowledge, or constructive knowledge?                                                                                               |

---

## Severity Classification System

Classify each finding in a review (Mode B), or flag each structural decision in a draft
(Mode A), using this three-tier system:

### GREEN — Acceptable / Standard

The provision aligns with market-standard positions. No negotiation required.
**Action**: Note for awareness. Include in audit trail.

### YELLOW — Negotiate

The provision falls outside standard position but within a negotiable range. Requires
attention but not escalation to senior counsel or decision-maker.
**Action**: Generate specific redline language. Provide fallback position. Estimate
business impact of accepting vs. negotiating.

### RED — Escalate

The provision poses material risk, contradicts statutory protections, creates an
unenforceable term, or falls outside the acceptable range for this deal type.
**Action**: Explain the specific risk with legal basis. Provide market-standard alternative
language. Estimate exposure. Recommend escalation path (senior IP counsel, outside counsel,
or business decision-maker).

### ANTITRUST-RISK — Competition Law Review Required

The provision raises potential competition law concerns requiring specialist antitrust/
competition law counsel before proceeding.
**Action**: Flag the provision, explain the specific concern (TTBER, Article 101 TFEU,
Sherman Act § 1), and refer to `legalcode-technology-license-review` for detailed
competition law analysis.

---

## Actionable Output per Finding

For each YELLOW or RED finding, generate a complete entry using this format:

```
**Section**: [Section and clause reference]
**Finding**: [What the agreement says / what is absent]
**Severity**: YELLOW / RED / ANTITRUST-RISK
**Confidence**: [Definite / High / Probable / Possible / Unlikely]
**Risk**: [Specific business or legal risk this creates]
**Legal Basis**: [Statutory provision, case, or commercial standard — or "General commercial
  practice" — or [VERIFY]]
**Redline**:
  Current: "[exact text, or 'absent']"
  Proposed: "[specific alternative language]"
**Fallback**: [Alternative position if primary redline is rejected]
**Priority**: [Tier 1 Must-Have / Tier 2 Should-Have / Tier 3 Nice-to-Have]
```

---

## Prioritization Framework

### Tier 1 — Must-Have (Deal-Breakers)

Issues the licensor or licensee cannot proceed without resolving:

- IP indemnification entirely absent or structured so as to provide no real protection
- No § 365(n) election language in a US-governed agreement
- No wind-down period: counterparty can immediately terminate and lock out operations
- MAR with automatic termination (not conversion) — triggers accidental deal termination
- Assignment-back of all improvements with no compensation
- Royalty base applying EMVR when only a sub-component practices the patents
- Sublicensing permitted with no flow-down of key licensor restrictions
- Source code escrow absent for business-critical software with no SaaS continuity alternative

### Tier 2 — Should-Have (Strong Preferences)

Material issues with room for negotiation:

- Sublicense conversion clause on head license termination
- MAR shortfall remedy: conversion to non-exclusive rather than termination
- Audit rights covering affiliates and sublicensees
- Interest provision on royalty underpayments
- Combination carve-out narrowed to combinations not reasonably anticipated by licensor
- Escrow verification upgraded to Level 2 or Level 3 for critical applications
- Non-exclusive grant-back obligation rather than exclusive or assignment

### Tier 3 — Nice-to-Have (Concession Candidates)

Preferred improvements that can be strategically conceded:

- MFL carve-out language for government licenses
- Specific audit frequency (once per year vs. once per 18 months)
- Preferred auditor selection mechanism
- Milestone event definition wording refinements
- Escrow update frequency (quarterly vs. semi-annually)

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                              | Fail Action                                                               |
| -------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, case, or established commercial principle                             | Add citation or mark "[UNVERIFIED — counsel to confirm]"                  |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction                                       | Fix format                                                                |
| **Currency**   | Every cited provision checked for amendments or repeal (TTBER expires April 2026; UK+ exhaustion regime evolving) | Flag "[CHECK CURRENCY — may have been amended]"                           |
| **Domain**     | Analysis stays within the contract's governing law. No jurisdiction-specific concepts applied universally         | Remove or flag as "[JURISDICTION-SPECIFIC — verify under applicable law]" |
| **Confidence** | Uncertainty explicitly stated, not hidden                                                                         | Add confidence qualifier                                                  |

### Self-Interrogation for RED Items

For any item classified RED, apply this 3-pass review before delivery:

**Pass 1 — Legal Chain Integrity**

- Does the risk assessment follow logically from the statute/case/principle cited?
- Would a court in this jurisdiction actually reach this conclusion on these facts?
- Is there a counter-argument that the counterparty's counsel will make?

**Pass 2 — Completeness**

- Have all relevant statutes, regulations, and cases been considered?
- Are there antitrust, bankruptcy, or cross-border dimensions not yet addressed?

**Pass 3 — Challenge**

- What is the strongest argument that this clause IS acceptable at market?
- Under what commercial circumstances might a reasonable IP lawyer accept this risk?
- Is the RED classification proportionate, or is this actually YELLOW with mitigations?

Mark audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                          | Action                                                |
| ------------ | --------- | ------------------------------------------------ | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law; clear statute or black-letter rule  | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong authority; minor interpretation questions | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments; reasonable minds could differ    | State with explicit reasoning and contra-indicators   |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing authorities       | Flag for qualified IP counsel with both sides         |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                          | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Anti-Patterns

The following errors are common in technology license agreements. Avoid them in drafting;
flag them in review.

1. **Ambiguous royalty base without SSPPU/EMVR determination** — Drafting "Net Sales of
   products incorporating the Licensed Technology" without specifying whether the royalty
   applies to the component embodying the patent or the entire end product. In patent
   infringement litigation, this ambiguity is routinely exploited to inflate or deflate
   damages. Define the royalty base with precision.

2. **Omitting "have made" from the patent grant** — The right to "make" does not include
   the right to have a third-party manufacturer make on the licensee's behalf. For any
   product license where contract manufacturing is expected, "have made" must be express.
   Absent this, the contract manufacturer infringes.

3. **MFL clause without settlement license carve-out** — If the licensor later settles
   patent litigation by granting a below-rate license, the MFL clause triggers retroactive
   price reductions for all other licensees. The licensor must carve out licenses granted
   in settlement of litigation from MFL.

4. **Exclusive grant-back without competition law review** — Exclusive grant-backs and
   assignment-back provisions are outside the EU TTBER safe harbor and require individual
   Article 101 TFEU analysis. They may also be scrutinized under the US rule of reason.
   Never include an exclusive grant-back without flagging for antitrust review.

5. **Source code escrow for SaaS with no RaaS or data portability alternative** —
   Traditional source code escrow is inadequate for SaaS applications. The licensee cannot
   reconstruct the SaaS environment from source code alone. Require Recovery-as-a-Service,
   data export rights, or a cloud provider direct agreement instead.

6. **Automatic termination on licensor insolvency (ipso facto clause)** — A clause that
   automatically terminates the license upon the licensor's insolvency filing is largely
   unenforceable in the US under § 365(e)(1). In the UK, it creates uncertainty. It may
   also deprive the licensee of its § 365(n) election right.

7. **No § 365(n) election language in US-governed agreements** — Without express
   incorporation of § 365(n), the licensee may not know to make the election when the
   licensor files for bankruptcy, or the right may be waived. Express the election mechanics
   in the license.

8. **Bundled IP + services payment structure reducing § 365(n) protection** — Where the
   license fee includes both IP licensing fees and service fees (maintenance, support), a
   bankruptcy court may treat the entire contract as a services contract and exclude it from
   § 365(n) protection. Separate IP license fees from service fees in the payment schedule.

9. **Improvement defined to capture all licensee innovations in the technology field** —
   An overbroad improvement definition (e.g., "any invention related to [technology area]")
   can capture licensee R&D that has nothing to do with the licensed technology. This both
   chills licensee innovation and raises antitrust risk. Limit "Improvement" to modifications
   that require a license to the Licensed Patents to practice.

10. **Sublicense without automatic conversion clause on head license termination** —
    Under US law (_Speedplay v. Bebop_), sublicenses do not automatically survive termination
    of the head license. Without a conversion clause, sublicensees lose rights when the head
    licensee's license ends. This creates significant downstream exposure for licensees who
    have built sublicensing revenue streams.

11. **IP indemnity combination carve-out too broad** — A carve-out excluding indemnity for
    "combinations with third-party products" that is not limited to "combinations not
    reasonably anticipated or recommended by licensor" can eliminate the practical value of
    the indemnity entirely — modern software products are always used in combination with
    other software.

12. **No wind-down period on termination** — A license that provides no wind-down period
    means the licensor can immediately cut off the licensee and all downstream customers.
    For embedded technology or critical business systems, a minimum 12–24 month wind-down
    period is essential for any responsible deployment.

13. **Trademark license without quality control provisions** — Under the Lanham Act "naked
    licensing" doctrine [VERIFY], a trademark licensor who fails to exercise quality control
    over its licensee's use of the trademark risks abandonment of the trademark. Every
    trademark element of a technology license must include adequate quality control
    provisions.

14. **UK+ exhaustion regime not addressed in cross-border license** — Post-Brexit, the UK+
    exhaustion regime creates asymmetric parallel import exposure (UK-to-EU goods are NOT
    exhausted in the EU; EU-to-UK goods ARE exhausted in the UK). In cross-border US/UK
    or EU/UK licenses, this asymmetry must be expressly addressed if territorial exclusivity
    is material to the deal.

15. **Royalty reports without GAAP/IFRS compliance requirement** — Without requiring
    royalty reports to be prepared on GAAP or IFRS-consistent bases, audits are more
    difficult and disputes about what constitutes a "sale" or "revenue" are harder to
    resolve. Specify the accounting standard applicable to royalty calculations.

16. **No payment obligation separation for sublicense income** — When the licensee
    sublicenses and receives an upfront sublicense fee, the license agreement may not clearly
    address the licensor's share of that upfront fee (as distinct from running royalties
    on sublicensee sales). Define sublicense income separately from royalty income.

17. **Licensor warranty of non-infringement without market clearance** — A licensor that
    warrants the licensed technology does not infringe any third-party rights is making a
    very strong representation, especially in dense patent landscapes (5G, MPEG, software).
    A more defensible alternative is a warranty of "no knowledge of claims" or a warranty
    limited to the licensor's knowledge.

18. **Failure to address Bayh-Dole march-in rights for federally funded IP** — If the
    licensed technology was developed with US federal funding, the government retains
    march-in rights (right to compulsory license the technology to others if the licensee
    fails to commercialize) under the Bayh-Dole Act, 35 U.S.C. §§ 200–212. The licensee
    should understand this risk before acquiring exclusive rights. [VERIFY: NIH/DOE
    march-in guidance as of 2025–2026]

19. **Missing assignment restriction and change-of-control clause** — In technology
    licenses, the identity of the licensee matters (the licensor may have granted exclusivity
    based on the licensee's commercialization capabilities). A change-of-control assignment
    to a competitor of the licensor, or to a financially weaker entity, can fundamentally
    change the commercial deal. Require licensor consent to assignment and change of control.

20. **Escrow verification left at Level 1 for mission-critical software** — A Level 1
    escrow (inventory check only) provides minimal assurance that the deposited code is
    actually buildable and functional. For business-critical applications, require Level 2
    (build verification) or Level 3 (functional testing) verification.

---

## Localization Notes

This skill is jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers. Key areas
requiring local legal verification:

| Topic                     | US                                                                                             | EU                                                                                     | UK                                                                                                                 |
| ------------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| IP formality requirements | Written; signed by assignor (copyright, 17 U.S.C. § 204); verbal patent license valid [VERIFY] | Written for most formal IP transfers; varies by member state                           | Written and signed for copyright exclusive license (CDPA s.90(3)); patent verbal license valid but evidential risk |
| Government IP rights      | Bayh-Dole march-in rights if federally funded                                                  | Member state research funding regimes vary                                             | Innovate UK / UKRI grant terms may impose IP obligations                                                           |
| Bankruptcy IP protection  | § 365(n) election; trademark gap addressed by _Mission Product_                                | No equivalent; rely on contractual protections                                         | No equivalent; English law contract survival provisions                                                            |
| Patent exhaustion         | _Quanta_ / _Impression Products_; domestic + international                                     | EEA-wide on authorized marketing; no international exhaustion                          | UK+ regime: EEA-to-UK exhausted; UK-to-EU not exhausted                                                            |
| Antitrust screening       | DOJ/FTC 2017 Guidelines; rule of reason                                                        | TTBER (Reg. 316/2014 until 1 May 2026; new TTBER from 1 May 2026)                      | UK TTBER (assimilated EU law until 1 May 2026; domestic BEO from 1 May 2026)                                       |
| Compulsory licenses       | Limited; § 203 copyright termination right; FRAND-adjacent                                     | TRIPS-compliant compulsory licensing in health/national emergency; UPC FRAND framework | CDPA compulsory licensing; Patents Act 1977 ss.48–54                                                               |

---

## External Tool Integration

**With legalcode-mcp connected:**

- In Step 3, search for governing law IP licensing statutes, recent case law, and
  jurisdiction-specific formality requirements
- Verify TTBER current status (Reg. 316/2014 expiry April 2026; new regulation text)
- Confirm § 365(n) applicable to the specific IP type in the licensed bundle
- Save verified references to `/tmp/legalcode-techlicense-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with general commercial knowledge
- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`

---

## Writing Standards

### For Redlines and Proposed Language (Shared Externally)

- Plain language. No jargon or filler.
- Active voice: "The Licensor must defend..." not "Defense obligations shall be undertaken
  by the Licensor..."
- Short sentences. One point per sentence.
- Name the actor: "Licensee shall pay..." not "Payment shall be made..."
- Specific, not vague: cite the relevant provision rather than saying "this may create
  issues"

### For Internal Analysis (Not Shared With Counterparty)

- Same plain-language standards apply
- May include more technical legal analysis and confidence qualifiers
- Glass Box audit trail appended at the end

### Quality Gates Before Delivery

1. Can a non-lawyer business stakeholder understand the executive summary and key findings?
2. Can counterparty's IP counsel understand and respond to each redline?
3. Is every legal claim backed by a specific citation (or flagged [VERIFY])?
4. Is every uncertainty acknowledged, not hidden?
5. Does every RED finding have a proposed alternative and priority level?

---

## Output Format Template

````markdown
## Technology License Agreement Analysis

**Document**: [Agreement name / date / parties]
**Type**: [Patent license / Software license / Technology transfer / Mixed bundle]
**Your Side**: [Licensor / Licensee]
**Mode**: [Draft review / Existing agreement review]
**Governing Law**: [Jurisdiction]
**Review Date**: [Date]
**Review Basis**: [Organizational playbook / General commercial standards]

---

## Executive Summary

[2–4 sentences: overall deal balance, top risks, recommended action]

---

## Key Findings (Top Issues)

| #   | Topic   | Severity | One-Line Summary |
| --- | ------- | -------- | ---------------- |
| 1   | [Topic] | RED      | [Summary]        |
| 2   | [Topic] | YELLOW   | [Summary]        |
| ... |         |          |                  |

---

## Core Topic Analysis

### Topic 1: Grant Scope and Field of Use — [GREEN / YELLOW / RED]

**Confidence**: [Level]
[Analysis using the format from Actionable Output per Finding]

### Topic 2: Sublicensing Rights — [GREEN / YELLOW / RED]

...

[Repeat for Topics 3–10]

---

## Missing Provisions

[List any of the 10 core topics entirely absent, with severity and recommended addition]

---

## Negotiation Priority

### Tier 1 — Must-Have

[List with brief rationale for each]

### Tier 2 — Should-Have

[List with brief rationale for each]

### Tier 3 — Concession Candidates

[List]

---

## Redlines

[Complete redline entries for all YELLOW and RED items using the Actionable Output format]

---

## Recommended Next Steps

[Specific actions, owners, and dependencies]

- [ ] [Action 1] — [Owner] — [Deadline or dependency]
- [ ] [Action 2] — ...

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill: "legalcode-technology-license-agreement"
  document: "[Agreement title and date]"
  license_type: "[Patent / Copyright / Know-how / Mixed bundle]"
  user_side: "[Licensor / Licensee]"
  mode: "[Draft / Review]"
  governing_law: "[Jurisdiction]"
  topics_reviewed: 10
  topics_present: "[number]"
  topics_missing: "[number] — [list]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED or UNVERIFIED]"
  case_law_consulted:
    - "[Case — VERIFIED or UNVERIFIED]"
  citations_verified: "[N VERIFIED] / [N UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  antitrust_screening: "Not performed — refer to legalcode-technology-license-review"
  export_control_screening: "Not performed — refer to export control counsel"
  bayh_dole_applicable: "[Yes (verify government rights) / No / Unknown]"
  limitations:
    - "Competition law / TTBER compliance not assessed"
    - "Patent validity / FTO not assessed"
    - "Export control compliance not assessed"
    - "[Any other scope limitations]"
  reviewer: "AI-assisted — requires qualified IP/licensing legal review"
```
````

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis covering the commercial deal structure
and IP rights mechanics of technology and IP license agreements. Addresses grant scope,
sublicensing, royalty structures, improvement rights, audit provisions, source code escrow,
patent exhaustion, IP indemnification, and termination effects on licensed rights. Research
synthesized from: AUTM Technology Transfer Practice Manual, Cambridge IP Licensing and
Transactions (2023 ed.), DOJ/FTC Antitrust Guidelines for the Licensing of IP (2017),
European Commission Draft Revised TTBER (September 2025), UK IP Exhaustion Regulations
(2023), key US/EU/UK case law (_Quanta_, _Impression Products_, _Mission Product Holdings_,
_Ericsson v. D-Link_), law firm client alerts (Fasken, Mayer Brown, Cooley, Venable, DLA
Piper, Finnegan), and NCC Group/Escode escrow verification standards. Complements (and
does not duplicate) `legalcode-technology-license-review` which covers competition law
compliance and SEP/FRAND analysis.

```

```
