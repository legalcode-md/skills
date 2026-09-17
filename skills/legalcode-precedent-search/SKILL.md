---
name: legalcode-precedent-search
description: Search firm knowledge bases, document repositories, and legal precedent libraries for relevant
  prior agreements, templates, clauses, memoranda, court filings, transaction documents, and legal positions.
  Use when drafting new contracts and need proven language, advising clients on recurring legal issues
  and need prior advice letters, evaluating counterparty positions against prior deals, building or refreshing
  a clause library, or identifying subject matter experts within the organization.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Search firm knowledge bases, document repositories, and legal precedent libraries for relevant prior agreements, templates, clauses, memoranda, court filings, transaction documents, and legal positions. Use when drafting new contracts and need proven language, advising clients on recurring legal issues and need prior advice letters, evaluating counterparty positions against prior deals, building or refreshing a clause library, or identifying subject matter experts within the organization. Covers semantic search by legal concept (not just keyword), multi-dimensional filtering (jurisdiction, counterparty, matter type, practice area, date range, document type), precedent applicability assessment, currency and staleness evaluation, conflicting-positions detection, subject matter expert identification, and privilege and confidentiality handling. Produces a ranked precedent digest with four-dimensional confidence scoring (Relevance, Currency, Reusability, Consensus), key excerpts, applicability assessment, reuse recommendations with adaptation guidance, conflict flags, and a Glass Box audit trail. Jurisdiction-agnostic with localization markers. Related: legalcode-contract-review, legalcode-clause-library-manager, legalcode-contract-comparison, legalcode-matter-triage-workflow.


# Legalcode Precedent Search

> **Disclaimer**: This skill provides a framework for AI-assisted legal precedent search and
> knowledge retrieval. It does not constitute legal advice. All precedent search outputs should
> be reviewed by a qualified legal professional before any retrieved language is reused,
> adapted, or relied upon in live matters. Laws and market practices change; verify the current
> applicability of any retrieved precedent before use. Legal citations and case references
> produced from memory carry hallucination risk — verify against authoritative sources before
> relying on them. Retrieved precedents may reflect outdated law, superseded firm positions, or
> context-specific negotiation dynamics not applicable to the current matter.

## Purpose and Scope

This skill searches firm knowledge bases, document repositories, and legal precedent libraries
to surface relevant prior work product and institutional expertise. It supports both targeted
searches (find the best precedent for this specific clause) and broad landscape searches (what
positions has the firm taken on limitation of liability in SaaS agreements over the past three
years?).

The skill evaluates every retrieved precedent on four independent dimensions — relevance to the
current matter, currency of the underlying law and market practice, reusability of the language,
and degree to which it represents settled firm consensus. It surfaces contradictory positions
across matters without assuming which is correct. It applies privilege and confidentiality
protocols before returning results. It identifies subject matter experts who have worked on
similar matters. Where no internal precedent exists, it flags the gap and suggests external
sources or alternative research paths.

**Covers:**

- Semantic search by legal concept (finds conceptually similar precedents even when terminology differs)
- Multi-dimensional filtering: document type, matter type, jurisdiction, counterparty, practice area, date range, deal size
- Four-dimensional confidence scoring (Relevance, Currency, Reusability, Consensus) per precedent
- Currency and staleness evaluation (legal staleness vs. market-practice staleness vs. firm-position staleness)
- Conflicting positions detection and surface-without-resolution protocol
- Privilege and confidentiality tier enforcement (attorney-client, work product, matter-confidential)
- Subject matter expert identification (who has worked on analogous matters?)
- Reuse classification: DIRECT REUSE / ADAPT / REFERENCE / ARCHIVE
- Adaptation guidance (specific edits needed, not generic "review and customize")
- Gap detection (no internal precedent exists; recommended external sources)
- Glass Box audit trail for search transparency and reproducibility
- Integration with DMS platforms (iManage, NetDocuments, SharePoint, HighQ) and legalcode-mcp

**Does not:**

- Draft new contracts (see `legalcode-contract-review`, `legalcode-saas-agreement-drafter`)
- Provide legal advice or replace qualified counsel
- Conduct conflict-of-interest checks (see `legalcode-conflict-check`)
- Research public case law or statutes as primary legal research (use legalcode-mcp directly)
- Guarantee that retrieved precedents are currently enforceable or market-standard

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic. Retrieved precedents carry their own governing law. The
skill surfaces the governing law of each precedent and flags whether it is portable to the
current matter's jurisdiction.

[JURISDICTION-SPECIFIC] When evaluating precedent portability across jurisdictions, research:

- Mandatory terms that differ by jurisdiction (data protection, employment minimums, penalty clause
  enforceability, IP assignment formalities)
- Work-for-hire doctrine (exists in the US; does not exist in the UK or most civil law systems)
- Punitive / exemplary damages (available in the US; generally unavailable in England & Wales / EU)
- Jury trial rights (US only in most contexts)
- Directness of application of consumer protection rules (B2B vs. B2C differs significantly)
- Statute of limitations and notice periods (vary materially across jurisdictions)
- Anti-assignment restrictions enforceability under local law

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
search intent, the workflow pauses and asks when:

- The answer would significantly change search strategy, ranking criteria, or output scope
- Multiple valid approaches exist (exact reuse vs. methodological reference)
- The matter context is needed to assess precedent applicability
- Confidentiality or privilege concerns require a scope decision

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

### Step 1: Accept the Search Request

Accept input in any of these formats:

- **Natural language query**: "Find precedents for limitation of liability clauses in SaaS vendor agreements where we are the vendor"
- **Current draft clause**: Paste a clause you are working on — the skill searches for analogous language and prior positions
- **Matter context**: Describe the deal (type, parties, jurisdiction, key issue) and ask for relevant precedents
- **Concept only**: Name a legal concept or clause type (limitation of liability, IP assignment, data processing, indemnification)
- **Document type filter**: "Show me all data processing agreements signed with European counterparties in the last two years"

If no query is provided, ask the user to describe what they are looking for.

---

### Step 2: Gather Search Intent

**⟁ CLARIFY** — Before searching, ask these questions. Present as structured options. Skip any
question the user has already answered.

**1. Search Mode — What do you need from this search?**

- **Options**:
  - **Exact reuse**: I need language I can copy with minimal edits
  - **Comparable positioning**: I want to see how we have positioned similar terms before
  - **Market practice survey**: I want to understand what range of positions the firm has taken
  - **Structure / approach**: I want to see how to draft this clause type, not copy specific language
  - **Risk mitigation examples**: I want to see how we have managed this risk in prior deals
- _Why this matters_: Exact reuse weights recency and match quality heavily. Market practice survey
  values breadth over depth. Structure / approach may return older or more diverse results. Your
  goal determines the ranking algorithm.

**2. Current Matter Context**

- Deal type (SaaS / Professional Services / Supply / Licensing / Partnership / M&A / Employment /
  Litigation / Regulatory / Other)
- Our side (Vendor / Customer / Licensor / Licensee / Employer / Employee / Claimant / Respondent /
  Other)
- Counterparty profile (Startup / Mid-market / Enterprise / Government / Individual / Consortium)
- Deal size range (Under $100K / $100K–$1M / $1M–$10M / $10M+ / Unknown)
- _Why this matters_: A precedent from a $5M enterprise deal may be over-engineered for a $150K
  SME contract. A precedent where we were the supplier has inverted risk from when we are the
  buyer. Matter context determines whether a precedent is actually applicable or just superficially
  similar.

**3. Jurisdiction and Governing Law**

- Current matter's governing law (jurisdiction of current deal)
- Portability requirement (Must be same jurisdiction / Willing to localize / Open to any jurisdiction)
- _Why this matters_: Liability cap language from an English-law contract may not translate to a
  California-law contract without material changes (UCTA 1977 vs. UCC unconscionability; different
  IP assignment formalities). Jurisdiction portability flags determine which precedents need a
  localization caveat.

**4. Confidentiality and Privilege Scope**

- **Options**:
  - Include all available precedents (including matter-confidential, with anonymization)
  - Exclude all matter-confidential precedents (return public or internally cleared precedents only)
  - Flag attorney work product separately (return but highlight privilege level)
- _Why this matters_: Attorney-client communications and work product have different reuse
  implications than standard transactional precedents. Settlement-related precedents may reflect
  context-specific concessions, not firm policy. Access controls exist for a reason — user choice
  determines scope.

**5. Date Range and Currency Preference**

- **Options**:
  - Last 1 year (maximum currency)
  - Last 3 years (standard market-practice window)
  - Last 5 years (broader landscape including older precedents)
  - All available dates (historical survey, including superseded precedents)
- _Why this matters_: Recent RAG (retrieval-augmented generation) research on legal LLMs
  reports hallucination rates of 58-80% on stale legal content. Even without AI, a 2019 data
  processing agreement predates GDPR full enforcement, Schrems II, and the EU-US Data Privacy
  Framework. Staleness is a material risk, not just an aesthetic preference.

---

### Step 3: Configure Knowledge Sources

Load available knowledge sources in priority order:

**Internal Sources (Primary)**

1. DMS / Document Management System (iManage, NetDocuments, SharePoint, HighQ, or file server)
2. CLM platform precedent library (Ironclad, Juro, DocuSign CLM, Icertis, Agiloft)
3. Firm knowledge portal or KM database
4. Matter management system (for metadata: deal type, size, counterparty, outcome)
5. Template library (approved standard forms with version history)

**External Sources (Secondary)** 6. legalcode-mcp — for public legal research, statutes, regulations, and case law [if connected] 7. Published legal databases (Westlaw, LexisNexis, vLex) [if accessible] 8. Counterparty-published standard form agreements (if publicly available)

**⟁ CLARIFY** — If no DMS or internal repository is connected:

- Manual search guidance: Specify directories, folders, or file paths to search
- Paste relevant precedents directly: User provides documents for comparison
- Graceful degradation mode: Skill analyzes user-provided materials and flags absence of broader
  search capability. Note in Glass Box audit trail: `knowledge_base: "Manual input only — broader
repository not searched"`

---

### Step 4: Define Search Dimensions

Establish the multi-dimensional filter set before executing the search. This prevents returning
100 superficially similar results; the filter combination determines precision.

**Primary Dimensions (Apply Always)**

| Dimension         | Options                                                                                                           | Default             |
| ----------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------- |
| **Legal concept** | Specific clause type or legal issue (e.g., "limitation of liability", "IP ownership", "data breach notification") | Derived from query  |
| **Document type** | Agreement, MOU, NDA, clause extract, memorandum, opinion letter, court filing, template                           | All types           |
| **Matter type**   | Commercial contract, employment, litigation, M&A, regulatory, IP, real estate, finance                            | All types           |
| **Practice area** | Corporate, litigation, employment, IP, data privacy, tax, real estate, finance                                    | Inferred from query |

**Secondary Dimensions (Apply When Provided)**

| Dimension                        | Options                                                     | Default           |
| -------------------------------- | ----------------------------------------------------------- | ----------------- |
| **Jurisdiction / governing law** | Specific jurisdiction(s) or all                             | All jurisdictions |
| **Our side**                     | Vendor, customer, licensor, etc.                            | Both sides        |
| **Counterparty type**            | Startup, enterprise, government, etc.                       | All types         |
| **Deal size range**              | Dollar thresholds                                           | All sizes         |
| **Date range**                   | Custom range or preset (1/3/5 years / all)                  | 3 years           |
| **Author / attorney**            | Specific name for SME search                                | All authors       |
| **Outcome**                      | For litigation: won / settled / lost / pending              | All outcomes      |
| **Playbook status**              | Approved standard / negotiated variant / exception approved | All statuses      |

**Concept Extraction (for Semantic Search)**

Before executing keyword search, extract the underlying legal concept from the query:

- "Find our standard limitation of liability clause" → Concept: `limitation_of_liability` →
  Also search for: `liability cap`, `aggregate liability`, `maximum liability`, `exclusion of liability`
- "Show me how we handle data breach notification" → Concept: `data_breach_notification` →
  Also search for: `security incident notice`, `breach disclosure`, `GDPR Article 33`, `notification period`
- "What have we done on non-solicitation" → Concept: `non_solicitation` →
  Also search for: `no-poach`, `talent restriction`, `employee restriction`, `post-termination covenant`

This concept expansion prevents missing relevant precedents that use different terminology.

---

### Step 5: Execute the Search

Execute the search using the configured dimensions and search strategy.

**Search Strategy (apply in sequence)**

1. **Exact keyword match** — Search for the query terms verbatim in document text and metadata
2. **Concept-expanded keyword match** — Search for expanded concept terms identified in Step 4
3. **Semantic / conceptual match** — If DMS supports semantic search (iManage Insight+, NetDocuments
   ndMAX): identify conceptually similar content using natural language understanding, not just term
   frequency. This surfaces precedents that address the same legal issue with different terminology
4. **Matter-type cross-match** — Within results, identify precedents from analogous (not identical)
   matter types that address the same legal concept in a comparable context

**Handling Search Results**

- **Retrieve full document + metadata** for each result: matter type, deal size, counterparty type,
  governing law, date, author, matter status, playbook approval status
- **Flag restricted documents** before surfacing: apply privilege tier protocol (see Step 6)
- **Deduplicate**: If the same clause appears in multiple versions of the same template, return
  the most recent approved version and note how many prior versions exist
- **Surface amendments**: If a retrieved agreement has been amended, retrieve both the base
  agreement and all amendments; apply the amended version

---

### Step 6: Score and Rank Results

Apply the four-dimensional confidence scoring model to each retrieved precedent.

#### Four-Dimensional Confidence Model

Score each dimension independently. Do not aggregate into a single score — display all four so
the user can see exactly why a precedent ranks the way it does.

**Dimension 1: RELEVANCE** — How well does this precedent match the current deal?

| Score     | Meaning              | Criteria                                                                                                     |
| --------- | -------------------- | ------------------------------------------------------------------------------------------------------------ |
| 0.90–1.0  | Identical context    | Same deal type, our side, counterparty profile, jurisdiction, and deal size range                            |
| 0.75–0.89 | Close context        | Same deal type and side; minor differences in counterparty profile or deal size                              |
| 0.55–0.74 | Analogous context    | Same deal type but opposite side (risk inversion required) OR closely analogous deal type in same legal area |
| 0.35–0.54 | Structural reference | Different deal type but same legal concept; useful for methodology, not direct copy                          |
| 0.0–0.34  | Low relevance        | Different deal type, different legal concept, or insufficient metadata to assess                             |

**Dimension 2: CURRENCY** — Is the underlying law and market practice still current?

| Score     | Meaning          | Criteria                                                                              |
| --------- | ---------------- | ------------------------------------------------------------------------------------- |
| 0.90–1.0  | Fully current    | Drafted or reviewed within 12 months; no known law changes affecting this area        |
| 0.75–0.89 | Probably current | 1–2 years old; market practice stable in this area; no known material law changes     |
| 0.55–0.74 | Possibly stale   | 2–3 years old OR market practice has evolved in this area since drafting              |
| 0.35–0.54 | Likely stale     | 3–5 years old OR known law change (new regulation, court ruling) since drafting       |
| 0.0–0.34  | Outdated         | 5+ years old OR directly superseded by known law, regulation, or firm playbook update |

**Dimension 3: REUSABILITY** — How much effort does reuse require?

| Score     | Meaning             | Criteria                                                                 |
| --------- | ------------------- | ------------------------------------------------------------------------ |
| 0.90–1.0  | Direct copy         | Update parties, dates, and defined terms; no substantive changes needed  |
| 0.75–0.89 | Minor edits         | Update 2–5 specific provisions; no structural change; 30–60 minutes      |
| 0.55–0.74 | Moderate adaptation | Multiple provisions need revision; possible structural change; 2–4 hours |
| 0.35–0.54 | Significant rework  | Framework useful but most language needs rewriting; 4–8 hours            |
| 0.0–0.34  | Template only       | Structural / methodological reference; do not copy language directly     |

**Dimension 4: CONSENSUS** — Does this represent settled firm practice or a one-off?

| Score     | Meaning              | Criteria                                                                         |
| --------- | -------------------- | -------------------------------------------------------------------------------- |
| 0.90–1.0  | Settled standard     | Used in 5+ matters; appears in approved firm template; GC / playbook approved    |
| 0.75–0.89 | Established approach | Used in 3–4 matters consistently; no material variation across uses              |
| 0.55–0.74 | Common approach      | Used in 2–3 matters; minor variation; no known contradicting position            |
| 0.35–0.54 | Single use           | Used once; not repeated in subsequent similar matters; may be outlier            |
| 0.0–0.34  | Contradicted         | Contradicted by more recent precedent OR expressly superseded by playbook update |

**Display Format**:

```
Precedent: [Matter / Template Name] — [Clause Name]
Relevance: [X.XX] | Currency: [X.XX] | Reusability: [X.XX] | Consensus: [X.XX]
Overall Tier: [TIER A / B / C / D]
```

#### Relevance Tier Classification

| Tier       | Label                            | Criteria                                                                          | Recommended Action                                                |
| ---------- | -------------------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **TIER A** | **HIGHLY APPLICABLE**            | Relevance ≥ 0.75 AND Currency ≥ 0.70 AND Reusability ≥ 0.70                       | Recommend for use; provide specific adaptation guidance           |
| **TIER B** | **CONTEXTUALLY RELEVANT**        | Relevance ≥ 0.55 AND at least one other dimension ≥ 0.65                          | Flag for attorney review; provide conditional adaptation guidance |
| **TIER C** | **LOW APPLICABILITY / CONFLICT** | Relevance < 0.55 OR Consensus < 0.35 (contradicted) OR Currency < 0.35 (outdated) | Do not recommend for direct use; route to SME for judgment        |
| **TIER D** | **INSUFFICIENT DATA**            | Metadata insufficient to score any dimension reliably                             | Request additional context; flag knowledge base gap               |

---

### Step 7: Apply Privilege and Confidentiality Protocol

Before surfacing any precedent, classify it against the four privilege tiers. Apply tier
controls before returning results.

**Privilege Tier Definitions**

| Tier   | Label                 | Definition                                                                                          | Return Policy                                                                                         |
| ------ | --------------------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **P1** | Public-Safe           | Precedents from publicly disclosed transactions; approved firm templates; non-sensitive matters     | Return with full metadata                                                                             |
| **P2** | Matter-Confidential   | Precedents from client-confidential matters where client identity is sensitive                      | Return with anonymization (client name → [SECTOR] client; matter ID → anonymized reference)           |
| **P3** | Attorney Work Product | Advice memoranda, strategy documents, litigation work product; captures attorney mental impressions | Flag as restricted; provide access path only. Do not return content                                   |
| **P4** | Settlement-Related    | Precedents from settlement negotiations; positions may be context-specific, not firm policy         | Flag prominently: "Settlement position — may not represent firm policy"; return with mandatory caveat |

[JURISDICTION-SPECIFIC] Attorney-client privilege and work product doctrine protections vary by
jurisdiction and context. In the US, the work product doctrine [VERIFY: Hickman v. Taylor, 329 U.S.
495 (1947); FRCP 26(b)(3)] protects materials prepared in anticipation of litigation from discovery.
In England & Wales, legal professional privilege (advice and litigation privilege) applies. Privilege
rules for in-house counsel vary materially across jurisdictions. Verify applicable privilege framework
before configuring access controls.

---

### Step 8: Flag Conflicts and Gaps

Before assembling the precedent digest, run two critical checks:

#### 8a. Conflicting Positions Detection

A firm may have taken different positions on the same legal issue across different matters. This is
normal — positions evolve, clients have different risk appetites, leverage dynamics differ. The skill
must surface contradictions without assuming which is correct.

**Conflict Detection Process:**

1. Identify pairs of precedents that address the same legal concept and clause type
2. Compare the substantive position taken (e.g., liability cap = 12 months fees vs. 6 months fees;
   IP ownership = full assignment vs. limited license)
3. Flag where the firm took materially different positions: "Note: Firm has used both [Position A] and
   [Position B] for [Clause Type]. Recommend confirming current firm position with [Practice Group Lead]
   or checking the approved playbook before choosing."
4. Distinguish legitimate variation from genuine conflict:
   - **Legitimate variation**: Different deal sizes, counterparty sophistication, or leverage dynamics
     produced different outcomes (expected)
   - **Genuine conflict**: Same deal context, similar counterparty, but materially opposite positions
     (flag for senior review)

[JURISDICTION-SPECIFIC] Positional conflicts may have ethical implications. In US jurisdictions
governed by the ABA Model Rules, Rule 1.7 addresses conflicts of interest including situations where a
firm argues directly conflicting positions in litigation for different clients on the same legal issue.
In-house counsel should assess whether any detected conflict triggers Rule 1.7 analysis. [VERIFY with
qualified counsel; rule applicability varies by state and bar association guidance]

#### 8b. Knowledge Base Gap Detection

If no relevant precedent is found for a dimension combination, surface this explicitly rather than
returning silence.

**Gap Types and Responses:**

| Gap Type                            | Response                                                                                                                                                                                                                                                                                        |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **No internal precedent**           | Flag: "No internal precedent found for [Concept + Jurisdiction + Matter Type]. Consider: (1) legalcode-mcp research for market standards; (2) published form agreements (Common Paper, Bonterms); (3) KM team inquiry for unpublished precedents; (4) outside counsel familiar with this area." |
| **Precedent exists but restricted** | Flag: "[N] precedents found but restricted (P3/P4 privilege). Contact [matter team] for access, or proceed with general market standards."                                                                                                                                                      |
| **Precedent outdated only**         | Flag: "Available precedent is [N] years old. Market practice may have evolved. Recommend legalcode-mcp research for current standards before relying on retrieved language."                                                                                                                    |
| **Jurisdiction-specific gap**       | Flag: "No precedent for [Jurisdiction] governance. Available precedents from [Other Jurisdiction] require localization. See Jurisdiction and Governing Law section for localization checklist."                                                                                                 |

#### 8c. Subject Matter Expert Identification

From the search metadata, identify attorneys or professionals who have worked on analogous matters:

- **Primary author**: Who drafted the most relevant precedents?
- **Supervising attorney**: Who approved or negotiated the most relevant deals?
- **Practice group lead**: Who owns this clause area in the firm's playbook?
- **Frequency indicator**: Who appears most often in matters matching the search dimensions?

Return as a structured expert reference:

```
Subject Matter Experts for [Clause Type / Legal Concept]:
- [Name, Title] — [N] analogous matters; most recent: [Matter ID, Date]
- [Name, Title] — [N] analogous matters; primary focus: [Jurisdiction / Deal Type]
- Practice Group: [Name] — [Contact info or matter management system link]
```

---

### Step 9: Assemble Precedent Digest and Verify Quality

Assemble the final precedent digest using the output template (see Output Format Template section).
Then run the quality verification sequence before delivery.

#### Quality Assurance: PDCA Cycle

**PLAN**: Confirm search dimensions are aligned with user intent. Verify knowledge source coverage.
Confirm privilege scope with user if ambiguous.

**DO**: Execute search, apply scoring, detect conflicts and gaps, identify experts, assemble digest.

**CHECK**: Run Precedent Quality Gates (below). For TIER A recommendations, run Self-Interrogation
(below). Verify all TIER C / conflict flags are explicitly presented, not buried.

**ACT**: If a new conflict is detected (firm took contradictory positions in two matters), note it
for playbook review. If a gap exists (no internal precedent for a common clause type), note it as
a KM recommendation. If a precedent has been reused 10+ times across matters, recommend formalizing
it as an approved template.

---

## Precedent Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate                   | Rule                                                                                                                                | Fail Action                                                                                                                 |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Applicability**      | Every precedent's applicability stated explicitly: identical, analogous, structural reference. No unlabeled comparisons.            | Add applicability tier label. Mark uncertain cases "[APPLICABILITY UNCLEAR — attorney review required]"                     |
| **Currency**           | Every precedent's temporal status captured and flagged if ≥ 3 years old or if known law change affects this area.                   | Flag: "[POSSIBLY OUTDATED — check if law / market practice has evolved since [date]]"                                       |
| **Conflict Awareness** | All precedents checked against contradictory positions in other matters. Surface contradictions before user selects language.       | Flag: "Note: Firm also used [Alternative Language] in [Matter X]. Confirm current position before choosing."                |
| **Matter Fit**         | Precedent's deal context documented: deal type, size, side, counterparty, leverage dynamic. No orphaned precedents without context. | Add context block: "This language appears in [# deals], range $[X]–$[Y], all [side] positions with [counterparty profile]." |
| **Confidence**         | Uncertainty stated explicitly. Single-use precedents not presented as settled firm practice.                                        | Add qualifier: "Used once in [Matter]. Not confirmed as firm standard — verify with [attorney / practice group]."           |

---

## Self-Interrogation for TIER A Recommendations

For any precedent ranked TIER A (Highly Applicable) and being recommended for direct reuse, apply
this three-pass self-interrogation before delivering.

**Pass 1 — Relevance Chain Integrity**

Ask:

- Is this precedent actually analogous, or am I pattern-matching on superficial similarity?
- Would the user be harmed by reusing this language without attorney review?
- Am I over-weighting recency at the expense of established market standard?
- Is there a material difference in the current deal — size, leverage, counterparty sophistication —
  that makes this precedent counterproductive?

_If any answer reveals a weakness_: Downgrade to TIER B. Add specific caveat before recommending.
E.g., "TIER B (downgraded): High relevance score but deal size 10× smaller than prior precedent.
Recommend checking whether enterprise-level language is appropriate for your SME counterparty."

**Pass 2 — Conflict and Contradiction Completeness**

Ask:

- Have I identified all contradicting precedents, not just the most obvious one?
- Is the recommended precedent the firm's _current_ position, or has the playbook evolved?
- Could this precedent create a problem by contradicting an adjacent agreement in the same transaction?
- Am I presenting a single-use precedent as representing firm consensus?

_If contradictions surface_: Return both positions. Flag explicitly. Do not choose between them.
That is for the attorney.

**Pass 3 — Context Fitness Challenge**

Ask:

- What is the strongest argument that this precedent is **not** appropriate for the current matter?
- Under what circumstances would reusing this language produce a worse outcome?
- Are there deal-specific constraints (relationship preservation, regulatory overlay, unusual leverage)
  that override general precedent guidance?

_If a material caution emerges_: State it before recommending. E.g., "Caution: This language was
used where we had strong leverage as sole-source vendor. Current counterparty has multiple options
and may push back. Consider the more balanced approach in Precedent B."

Mark the audit trail: `self_interrogation: PASS` or `self_interrogation: REVISED — [reason]`.

---

## Confidence Scoring

| Level        | Range     | Meaning                                                                    | Action                                                        |
| ------------ | --------- | -------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled firm position, recently used, approved template, same deal context | Recommend with full confidence                                |
| **High**     | 0.80–0.94 | Strong match, minor context differences, recently used, no contradictions  | Recommend with minor caveats                                  |
| **Probable** | 0.60–0.79 | Good match but relevant differences (age, side, counterparty)              | Recommend conditionally; state specific adaptation needed     |
| **Possible** | 0.40–0.59 | Partial match; opposite side, different size, or older                     | Flag for attorney review with both the upside and the concern |
| **Unlikely** | 0.0–0.39  | Weak match, contradicted, outdated, or privilege-restricted                | Do not recommend for use; flag as reference only              |

---

## Glass Box Audit Trail

Every precedent search output MUST include a Glass Box audit section:

```yaml
glass_box:
  search_query: "[User's original query or derived search terms]"
  search_mode: "[Exact Reuse / Comparable Positioning / Market Practice / Structure / Risk Mitigation]"
  sources_queried:
    - "[Source 1: DMS / Knowledge Portal / Manual Input / legalcode-mcp / etc.]"
    - "[Source 2: ...]"
  knowledge_base_configured: "YES / NO — [if no, note scope limitation]"
  search_dimensions_applied:
    legal_concept: "[e.g., limitation of liability]"
    document_type: "[e.g., SaaS Agreement, All]"
    matter_type: "[e.g., Commercial contract]"
    our_side: "[e.g., Vendor, Both]"
    jurisdiction: "[e.g., US, California, All]"
    counterparty_type: "[e.g., Enterprise, All]"
    deal_size_range: "[e.g., $1M–$10M, All]"
    date_range: "[e.g., 2022–2026, All]"
    practice_area: "[e.g., Technology Transactions]"
  results_returned: "[Total count from search]"
  results_after_privilege_filter: "[Count after applying P1/P2/P3/P4 tiers]"
  results_restricted: "[Count restricted; P3/P4 tier]"
  precedents_recommended:
    tier_a: "[Count of TIER A — Highly Applicable]"
    tier_b: "[Count of TIER B — Contextually Relevant]"
    tier_c: "[Count of TIER C — Low Applicability / Conflict]"
    tier_d: "[Count of TIER D — Insufficient Data]"
  conflicts_identified: "[Yes / No — list conflict pairs if Yes]"
  gaps_identified: "[Yes / No — list gap types if Yes]"
  subject_matter_experts_identified: "[Yes / No — list names/roles if Yes]"
  legalcode_mcp: "Connected / Not connected"
  self_interrogation: "PASS / REVISED — [reason] / NOT APPLICABLE (no TIER A results)"
  quality_gates_passed: "All 5 / [List any gate with issue]"
  confidence: "[HIGH / PROBABLE / POSSIBLE] — [1–2 sentence rationale]"
  limitations:
    - "[Knowledge base scope: manual input only / DMS not connected]"
    - "[Date range restriction: only last N years available]"
    - "[Privilege restriction: P3/P4 documents excluded]"
    - "[Jurisdiction limitation: no precedents for [Jurisdiction]]"
  reviewer: "AI-assisted — requires qualified legal review before precedent use"
```

---

## Anti-Patterns

What NOT to do in legal precedent search and knowledge management:

1. **Searching without clarifying intent** — "Find NDA precedents" returns 200 results, all
   useless. The user wanted the mutual NDA clause on residual knowledge for technology licensing,
   governing California law, where we were the disclosing party. Clarify first. Precision over
   volume.

2. **Over-trusting old precedent** — Reusing a 2019 template "because it worked before" without
   checking that GDPR, NIS2, US state privacy laws, or a relevant court ruling changed the analysis.
   That precedent may now be a liability, not a timesaver.

3. **Precedent without provenance** — Finding a clause in a shared folder with no metadata (date,
   counterparty, jurisdiction, negotiation history, outcome). You cannot assess applicability without
   context. A clause without provenance is not a precedent; it is an orphaned fragment.

4. **Treating "signed before" as approval** — "We signed this language once" does not mean it
   represents firm policy. It means both sides agreed to it once, under specific leverage conditions,
   at a specific deal size. Check if it was an exception approved under time pressure.

5. **Missing embedded amendments** — Extracting Section 5 from a base agreement that was amended
   three times. The amendment controls, not the base. Always retrieve the full amendment chain before
   extracting any clause.

6. **Single-source search** — Only searching the internal DMS and missing that a major counterparty
   published a new standard form (publicly available) that the market is beginning to adopt. External
   precedent data matters for market-practice positioning.

7. **Reusing language without understanding why** — Clause X was included because of a specific
   2021 dispute with a now-departed counterparty. You reuse it in a completely different context,
   creating unnecessary complexity and negotiation friction. Understand before copying.

8. **Precedent conflict without detection** — The firm has used two conflicting positions on
   limitation of liability caps (12 months in some deals, 6 months in others). You return only one.
   The user anchors on it. When the other position surfaces in the next deal, credibility suffers.
   Surface both, always.

9. **Assuming currency without checking** — "It's from 2023 so it's recent." But the EU-US Data
   Privacy Framework launched in 2023 and NIS2 came into force in October 2024. Age alone does not
   equal legal currency. The relevant question is whether the _law this precedent relies on_ has
   changed.

10. **Context extraction without deal-size calibration** — Limitation of liability language from a
    $50M enterprise SaaS contract (uncapped for IP indemnification, $10M aggregate cap otherwise) is
    not appropriate for a $50K SME services contract. The risk allocation logic is entirely different.
    Size matters.

11. **Privilege leakage via precedent search** — Returning attorney work product (litigation strategy,
    settlement positions, advice memoranda) as general precedents. These documents are protected and
    must not be exposed through the back door of a knowledge search.

12. **SME identification without access path** — Identifying that Partner A has the most experience
    on cross-border IP assignments but providing no way to contact them or access their prior matters.
    Expert identification is useless without a routing mechanism.

13. **Opposite-side reuse without inversion analysis** — Copying limitation of liability language from
    a contract where we were the customer (capped exposure = good for us) into a contract where we are
    the vendor (capped exposure = also good for us, but _not for this counterparty_). Same language,
    opposite practical effect. Always flag side mismatch.

14. **Knowledge hoarding without retrieval** — 1,000 contracts in a shared drive with no consistent
    naming convention, no metadata tags, no version control, no search capability. That knowledge
    exists in principle but not in practice. Precedent search can only work on what is findable.

15. **Precision without recall** — Running a highly specific search ("California-law SaaS agreements
    with liability caps over $5M") and returning 0 results, when 12 relevant precedents exist under
    different classification labels. Always run the concept-expanded secondary search before reporting
    "no results found."

16. **Recommending without ranking** — Returning 15 precedents in random order with no triage
    guidance. The user is busy. They need the top 2–3 recommendations with explicit reasoning, not a
    pile of options. Sort by combined confidence score; explain why the top results rank first.

17. **Updating precedents without versioning** — Improving a template clause without preserving the
    prior version. Six months later, a matter executed against the old version and you cannot explain
    why the language differs. Version history is not optional.

18. **Feedback loop failure** — Completing the search, delivering the precedent, and never tracking
    whether the counterparty accepted the language, pushed back, or required negotiation. The search
    engine gets better only if outcomes feed back into the knowledge base. Closing this loop is the
    KM professional's core contribution.

---

## Writing Standards

Apply plain-language discipline to all precedent digest output:

**For applicability assessments**:

- Active voice: "This precedent matches your deal type exactly" not "An identical match was found"
- Specific, not vague: "Deal size mismatch: original deal was $5M; your deal is $150K" not "Context
  differs"
- Cite the precedent explicitly: reference the matter ID or template version, not just the clause name

**For confidence scores**:

- Explain each score with a 1–2 sentence rationale (do not display a number without context)
- State uncertainty directly: "Used once in a non-representative matter — treat as reference, not
  standard"
- Use positive and negative qualifiers together: "High relevance (identical deal type) but low
  currency (3 years old, market has evolved on this point)"

**For reuse guidance**:

- List specific edits needed: "Update liability cap from 12 months to [your agreed cap]; replace
  insurance threshold $5M with [your threshold]; localize Section 8 for California law (current
  version is New York)"
- Distinguish must-change from should-consider: must-change = structurally incorrect if not changed;
  should-consider = market practice recommends updating
- Active voice: "Change Section 5.1(b) to exclude gross negligence" not "Section 5.1(b) may warrant
  review"

**Quality gates before delivery**:

1. Can the user identify the top 2–3 precedents to start with in under 30 seconds?
2. Is every confidence score accompanied by a rationale?
3. Are all conflicts surfaced before the user selects language?
4. Is every reuse recommendation specific enough to execute without additional attorney guidance?
5. Is the privilege tier of every returned precedent explicitly labeled?

---

## DMS and Repository Integration

This skill is designed to integrate with leading document management and knowledge systems.

**With DMS connected (preferred):**

| Platform                                    | Integration Approach                                                                                                                                                                         |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **iManage Insight+**                        | Hybrid search combining keyword, semantic, and vector-based search via Azure OpenAI; matter metadata (client, deal type, date) retrieved automatically; RAVN AI concept extraction available |
| **NetDocuments ndMAX**                      | Semantic search understanding query context and intent; metadata filters for deal type, date, jurisdiction; AI clause suggestions during drafting                                            |
| **SharePoint / OneDrive**                   | Full-text and metadata search; Microsoft 365 Copilot for semantic search in E3/E5 tenancies; manual metadata tagging required for precision                                                  |
| **HighQ**                                   | iManage-integrated knowledge portal; structured matter pages; searchable clause libraries and playbooks                                                                                      |
| **CLM platforms (Ironclad, Juro, Icertis)** | Clause-level search with approval status, playbook alignment flags, and counterparty acceptance history                                                                                      |

**With legalcode-mcp connected:**

- Use for external legal research to contextualize internal precedents (verify currency, identify
  market-standard language, check statutory authority underlying a precedent)
- Save relevant research to `/tmp/legalcode-precedent-research.md` for reference during analysis
- Mark legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without DMS or legalcode-mcp (graceful degradation):**

- Accept user-provided documents via paste or file path as the precedent set
- Note in Glass Box audit trail: `knowledge_base: "Manual input only — broader repository not
available"`
- Focus on comparative analysis of user-provided materials rather than broad repository search
- Include note in output: "Search scope limited to [N] user-provided documents. Broader repository
  search not performed. Recommend KM team query for additional precedents."

---

## Output Format Template

Structure the final deliverable as:

```markdown
# Precedent Search Results

**Search Query**: [User's original query]
**Search Mode**: [Exact Reuse / Comparable Positioning / Market Practice / Structure / Risk Mitigation]
**Knowledge Sources**: [DMS / CLM / Manual input / legalcode-mcp]
**Date Searched**: [date]
**Total Results**: [N found; M returned after privilege filter; K recommended]

---

## Executive Summary

[2–3 sentences on the precedent landscape: how many precedents exist, overall quality/currency of
available materials, top recommendation(s), and any critical gaps or conflicts to flag immediately.]

---

## Recommended Precedents

### [TIER A] Precedent 1: [Matter Identifier / Template Name] — [Clause Name]

**Relevance**: [X.XX] | **Currency**: [X.XX] | **Reusability**: [X.XX] | **Consensus**: [X.XX]
**Overall Tier**: TIER A — Highly Applicable

#### Key Metadata

| Field                 | Value                                 |
| --------------------- | ------------------------------------- |
| Matter / Template     | [ID or name]                          |
| Deal Type             | [Type]                                |
| Our Side              | [Side]                                |
| Deal Size             | $[Amount]                             |
| Counterparty          | [Profile]                             |
| Governing Law         | [Jurisdiction]                        |
| Date                  | [Date]                                |
| Uses in Other Matters | [N times / Template — N uses]         |
| Playbook Status       | [Approved / Exception / Not assessed] |

#### Clause Language

> [COMPLETE CLAUSE TEXT — not just a summary or excerpt]

#### Confidence Rationale

- **Relevance ([score])**: [1–2 sentences explaining why this precedent matches or deviates from
  the current matter]
- **Currency ([score])**: [1–2 sentences on legal and market-practice currency]
- **Reusability ([score])**: [1–2 sentences on ease of adaptation]
- **Consensus ([score])**: [1–2 sentences on whether this represents settled firm practice]

#### Reuse Guidance

**Tier: DIRECT REUSE / ADAPT / REFERENCE / ARCHIVE**

[If DIRECT REUSE]:

- Required edits only: Update [party names, dates, defined terms, deal-specific values]
- No substantive changes needed

[If ADAPT]:

- **Must change**: [Specific provision and reason — e.g., "Section 5.1: liability cap amount needs
  updating from $2M (prior deal size) to $[your amount]"]
- **Should consider**: [Specific provision and reason — e.g., "Section 5.3: add data breach
  exclusion from cap if your deal involves data processing"]
- **Jurisdiction localization**: [If governing law differs — specify what needs localization]
- **Side inversion**: [If our side differs — specify which risk allocations need flipping]

[If REFERENCE]:

- Use for framework/structure only — do not copy language
- Methodology applicable to current matter: [describe]
- Language requires significant rewriting due to: [reason]

#### Flagged Issues

- [ ] **Privilege / Confidentiality**: [Tier and implication]
- [ ] **Conflict with other precedents**: [Describe conflict; reference Precedent Y]
- [ ] **Possibly outdated**: [Flag if Currency < 0.55]
- [ ] **Single-use outlier**: [Flag if Consensus < 0.45]
- [ ] **Side inversion required**: [Flag if our side differs]
- [ ] **Jurisdiction localization required**: [Flag if governing law differs]

---

### [TIER B] Precedent 2: [Matter Identifier] — [Clause Name]

[Repeat structure for each TIER B result; fewer mandatory fields]

---

### [TIER C] Precedents: Flagged for Review

[List TIER C results briefly — matter ID, why it ranks low, whether referral to SME is needed]

---

## Conflicting Positions Identified

[List any conflicts detected in Step 8a. Format:]

**Conflict: [Clause Type]**

- Precedent A ([Matter ID, Date]): [Summary of Position A]
- Precedent B ([Matter ID, Date]): [Summary of Position B]
- Recommendation: Confirm current firm position with [Practice Group Lead / Playbook] before
  selecting.

---

## Knowledge Base Gaps

[List any gap types detected in Step 8b:]

- **No precedent found for**: [Clause type + jurisdiction + matter type]
  - Recommended next steps: [Options from gap detection table above]

---

## Subject Matter Experts

| Name / Role           | Relevant Matters                   | Focus Area                               |
| --------------------- | ---------------------------------- | ---------------------------------------- |
| [Name, Title]         | [N matters; most recent: ID, date] | [Jurisdiction / Deal Type / Clause Area] |
| [Practice Group Lead] | [Contact route]                    | [Practice Group]                         |

---

## Glass Box Audit Trail

[YAML block per Glass Box Audit Trail section above]
```

---

## Localization Notes

This skill is jurisdiction-agnostic by design. To use it effectively for jurisdiction-specific
precedent search:

1. Configure the jurisdiction filter in Step 4 before executing the search
2. Enable jurisdiction portability assessment in Step 6 (each precedent receives a portability flag)
3. For precedents from other jurisdictions, the reuse guidance in the output will specify which
   provisions require localization and what law applies [JURISDICTION-SPECIFIC]
4. For cross-border matters, search both the primary and secondary jurisdiction independently;
   compare positions; flag where they diverge

**Common localization trigger points** (search results will flag these):

- IP assignment formalities (US work-for-hire vs. UK/EU explicit assignment requirement)
- Penalty and liquidated damages clauses (enforceability varies widely)
- Limitation of liability clauses (UCTA 1977 in England & Wales; unconscionability doctrine in US;
  BGB §307-309 in Germany) [VERIFY]
- Data protection provisions (GDPR, UK GDPR, CCPA, LGPD, PDPA each impose different obligations)
- Employee IP ownership (CA Labor Code §2870 carve-outs; UK Patents Act 1977; German UrhG §12–14)
  [VERIFY]
- Anti-assignment rules (vary by jurisdiction and contract type)

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis based on: (1) 2-agent research pipeline
analyzing structural patterns from `legalcode-contract-review`, `legalcode-matter-triage-workflow`,
and `legalcode-nda-triage` reference skills; (2) web-backed research on legal knowledge management
best practices, iManage RAVN / NetDocuments ndMAX semantic search capabilities, RAG-based legal
precedent retrieval (LegalBench-RAG benchmark; JusBuild architecture; LRAGE evaluation tool);
(3) analysis of privilege tier frameworks (attorney-client privilege, work product doctrine under
Hickman v. Taylor [VERIFY]; FRCP 26(b)(3) [VERIFY]; Legal professional privilege in England &
Wales [VERIFY]); (4) ABA Model Rule 1.7 positional conflict analysis [VERIFY with counsel]. All
statutory references require independent verification before reliance.
