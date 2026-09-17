---
name: legalcode-precedent-analyzer
description: Analyzes completed deal corpora — contract archives, CLM exports, closing binders, or raw
  document folders — to extract standard positions, negotiation outcomes, client preferences, clause evolution
  trends, and market deviations. Use when a legal team wants to mine institutional knowledge from historical
  deals, generate or refresh a negotiation playbook backed by real data, understand win/loss rates on
  specific clause positions, identify client preference profiles from recurring counterparties, benchmark
  the firm's standard positions against market norms, or track how clause language has shifted over time.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Analyzes completed deal corpora — contract archives, CLM exports, closing binders, or raw document folders — to extract standard positions, negotiation outcomes, client preferences, clause evolution trends, and market deviations. Use when a legal team wants to mine institutional knowledge from historical deals, generate or refresh a negotiation playbook backed by real data, understand win/loss rates on specific clause positions, identify client preference profiles from recurring counterparties, benchmark the firm's standard positions against market norms, or track how clause language has shifted over time. Triggers on phrases such as "analyze our prior deals," "what do we usually agree on for limitation of liability," "build a playbook from our contracts," "show me our win rate on indemnification caps," "how has our limitation clause evolved," "what do clients typically push back on," "mine our contract history," or "benchmark our positions against market." Produces a statistical term frequency matrix, position classification playbook (BASELINE/FALLBACK/ESCALATE/RED-LINE), negotiation outcome report, clause evolution timeline, client preference profiles, and a market gap analysis. Distinct from legalcode-precedent-search (which retrieves a single precedent for a current matter) — this skill operates on the entire corpus to extract population-level intelligence. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers. Related: legalcode-contract-playbook-builder, legalcode-precedent-search, legalcode-contract-review, legalcode-contract-metadata-extractor.


# Legalcode Precedent Analyzer

> **Disclaimer**: This skill provides a framework for AI-assisted analysis of completed
> deal corpora. It does not constitute legal advice. All analytical outputs, playbook
> recommendations, and statistical summaries should be reviewed by a qualified legal
> professional before use in live negotiations. Statistical patterns extracted from
> historical deals reflect past practice only — they do not guarantee future acceptability
> or legal compliance. Clause language cited from memory carries hallucination risk —
> verify against source documents before relying on any extracted language. Laws and
> market norms change; historical positions may no longer reflect current best practice.

## Purpose and Scope

This skill mines a corpus of completed deals to surface institutional knowledge that is
typically locked in individual attorneys' memories, scattered across document management
systems, or buried in closing binders. It transforms raw deal history into actionable
analytics: which positions the firm routinely wins, which it concedes, where clients
push back, how language has evolved, and where the firm's positions diverge from market.

**Covers:**

- Corpus ingestion and inventory (files, folders, CLM exports, metadata spreadsheets)
- Clause-level extraction: identifying and classifying major clause types across all documents
- Statistical term frequency analysis: prevalence rates, deviation frequencies, position distributions
- Position classification matrix (BASELINE / FALLBACK / ESCALATE / RED-LINE)
- Negotiation outcome analysis: win/concession/compromise rates by clause type and counterparty
- Client preference profiling: clustering preferences by counterparty type, industry, deal size
- Clause evolution tracking: time-series analysis of how positions and language have shifted
- Market gap analysis: where firm positions deviate from published benchmarks
- Playbook generation: standard positions, fallback language, red lines, and rationale

**Does not:**

- Retrieve a single specific precedent for immediate reuse (see `legalcode-precedent-search`)
- Draft new contracts from scratch (see `legalcode-contract-playbook-builder` and type-specific drafting skills)
- Provide legal advice or replace qualified counsel
- Apply to any single jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers

### Relationship to Related Skills

| Skill                                         | What It Does                                                           | When to Use                                          |
| --------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------- |
| **legalcode-precedent-analyzer** (this skill) | Analyzes the entire corpus; extracts statistics, trends, and playbooks | Periodic reviews, playbook refreshes, KM initiatives |
| **legalcode-precedent-search**                | Retrieves the best single precedent for a current matter               | During active deal work                              |
| **legalcode-contract-playbook-builder**       | Builds a playbook interactively, from user input                       | When historical data is unavailable                  |
| **legalcode-contract-metadata-extractor**     | Extracts structured metadata fields from individual contracts          | Pre-processing step for corpus analysis              |
| **legalcode-contract-review**                 | Reviews a single contract against a playbook                           | Reviewing incoming counterparty drafts               |

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The corpus may span multiple governing laws, and
the analysis should preserve that diversity rather than normalizing it away.

[JURISDICTION-SPECIFIC] When building playbooks, apply jurisdiction-specific markers to
positions that differ materially by governing law:

- Limitation of liability caps: UCTA 1977 (UK) vs. UCC §2-719 (US) vs. Civil Code regimes
- IP assignment formality: §204 of the Copyright Act (US) vs. CDPA 1988 s.90(3) (UK)
- Data protection obligations: GDPR/UK GDPR regime vs. US state-law patchwork vs. LGPD
- Non-compete enforceability: jurisdiction-specific mandatory limits
- Penalty clause treatment: Cavendish Square (UK/AU) vs. US liquidated damages doctrine

[JURISDICTION-SPECIFIC] For international deal corpora, segment the analysis by governing
law before aggregating statistics — combining English-law and New York-law deals in the
same frequency count produces misleading "standard positions."

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The corpus scope, quality, or composition would materially change the analytical approach
- Multiple valid segmentation approaches exist (by deal type, counterparty, jurisdiction, etc.)
- The analytical depth required (full statistical model vs. quick summary) is ambiguous
- Output format choices (executive playbook vs. raw data vs. detailed statistical report) need direction

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

### Step 1: Accept the Corpus

Accept the deal corpus in any of these formats:

- **Document folder**: A directory of contracts (PDF, DOCX, TXT) — use Glob to list and Read to ingest
- **CLM export**: A spreadsheet (CSV/XLSX) containing extracted metadata from a contract management system
- **Closing binder**: A structured folder of executed agreements from completed transactions
- **Metadata spreadsheet**: Pre-extracted fields (party names, dates, key clause positions) in tabular form
- **Mixed corpus**: A combination of raw documents and partial metadata

If no corpus is provided, prompt the user to supply the deal documents or metadata.

**⟁ CLARIFY** — If only partial metadata is available without the underlying documents, ask:

- "I have metadata from [N] deals but no underlying documents. Should I proceed with the
  metadata only (faster, but clause-level analysis is limited to extracted fields), or
  would you like to provide the source documents as well?"

### Step 2: Gather Context

**⟁ CLARIFY** — Before analyzing, ask the user these questions (skip any already answered):

1. **Deal type focus**: What contract types should the analysis cover?
   - Options: All types in the corpus, Specific types (NDA / SaaS / MSA / Employment /
     Other — specify), Highest-volume types only (let me identify)
   - _Why this matters_: Mixing contract types in frequency analysis produces misleading
     statistics. Limitation-of-liability positions in NDAs are not comparable to those in
     MSAs.

2. **Primary objective**: What is the main output needed?
   - Options: Generate a negotiation playbook from deal history, Understand win/loss rates
     on specific clauses, Identify what clients push back on most, Track how positions have
     evolved, Benchmark against market standards, All of the above
   - _Why this matters_: Determines which analytical modules to prioritize.

3. **Corpus quality level**: How complete and structured is the data?
   - Options: Raw contracts only (no extraction done yet), Partially extracted metadata
     (some fields captured), Fully structured metadata from CLM system, Mixed
   - _Why this matters_: Raw documents require extraction before analysis; structured
     metadata can be analyzed directly.

4. **Time scope**: What date range should the analysis cover?
   - Options: All available history, Last 1 year, Last 2-3 years, Last 5 years, Custom range
   - _Why this matters_: Older deals may reflect outdated positions or market conditions.
     A 5-year corpus weights old concessions equally with recent ones unless filtered.

5. **Counterparty segmentation**: Should results be segmented by counterparty type?
   - Options: No segmentation (aggregate analysis), By counterparty industry, By
     counterparty size (enterprise/mid-market/SMB), By deal type, By geography, Custom
   - _Why this matters_: What is "standard" with a Fortune 500 enterprise customer differs
     from what is standard with an early-stage startup.

6. **Confidentiality level**: How should privilege and confidentiality be handled?
   - Options: Internal use only (no counterparty identification in outputs), Anonymized
     counterparty references acceptable, Full detail acceptable for internal playbook
   - _Why this matters_: Playbook outputs that reference specific counterparty negotiation
     histories may carry privilege or confidentiality concerns if shared externally.

If the user provides partial context, proceed with reasonable defaults and state
assumptions explicitly.

### Step 3: Build the Corpus Inventory

Before extracting clause data, build a structured inventory of the corpus:

1. **List all documents**: Use Glob to find all contract files in the corpus directory.
   Record: file name, file type, file size, last-modified date.

2. **Identify document types**: For each document, determine the contract type
   (NDA, MSA, SaaS, employment, partnership, etc.) by reading key sections or applying
   pattern matching.

3. **Build the inventory table**:

   | #   | File              | Type | Party 1       | Party 2   | Date    | Governing Law | Status   |
   | --- | ----------------- | ---- | ------------- | --------- | ------- | ------------- | -------- |
   | 1   | acme-msa-2024.pdf | MSA  | [firm/client] | ACME Corp | 2024-03 | NY law        | Executed |
   | ... | ...               | ...  | ...           | ...       | ...     | ...           | ...      |

4. **Report corpus statistics** to the user:
   - Total documents found
   - Document type breakdown (how many of each contract type)
   - Date range of the corpus
   - Jurisdictions represented
   - Documents that could not be parsed or identified (flag for manual review)

**⟁ CLARIFY** — If the corpus is larger than 50 documents and full extraction would be
time-intensive, present the options:

- "I've found [N] documents across [M] contract types. Would you like me to analyze the
  full corpus (comprehensive but slower), or should I focus on the highest-volume types
  ([top 3 types] representing [X]% of the corpus)?"
- "I found [N] documents that appear incomplete, undated, or unexecuted. Should I include
  these in the analysis or exclude them and note the omission?"

### Step 4: Extract Clause-Level Data

For each document in the corpus (or each deal in the metadata spreadsheet), extract
structured data across the major clause categories.

**Extraction approach by data source:**

**If raw documents are available:**

- Read each contract and extract positions for each clause category below
- Record the exact language (abbreviated) plus the position classification
- Note whether the clause is present, absent, one-sided, or bilateral

**If only metadata is available:**

- Proceed with the extracted fields as-is
- Flag any clause categories with missing data as INSUFFICIENT DATA

**Major clause categories for extraction:**

| #   | Clause Category                | Key Data Points to Extract                                                                                      |
| --- | ------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| 1   | Limitation of Liability        | Cap amount / formula, mutual vs. unilateral, carveouts, consequential damages exclusion                         |
| 2   | Indemnification                | Scope (IP / data breach / third-party / specific), mutual vs. unilateral, cap                                   |
| 3   | Intellectual Property          | IP ownership default, assignment of developed IP, license grants, pre-existing IP carveout                      |
| 4   | Data Protection                | DPA included (Y/N), data breach notification timeline, sub-processor approval, transfer mechanism               |
| 5   | Term and Termination           | Initial term, auto-renewal (Y/N), termination for convenience (T4C) notice period, T4C available to which party |
| 6   | Governing Law and Disputes     | Governing law, dispute resolution mechanism (litigation / arbitration / escalation), venue                      |
| 7   | Confidentiality                | Term of obligation, definition scope, post-term survival period, exceptions                                     |
| 8   | Warranties                     | Warranty scope, warranty period, disclaimer present (Y/N), remedy for breach                                    |
| 9   | Payment Terms                  | Net days, late payment interest rate, disputed invoice mechanism                                                |
| 10  | Assignment                     | Assignment restrictions, change-of-control treatment, exceptions                                                |
| 11  | Non-Compete / Non-Solicitation | Present (Y/N), scope, duration, geographic reach                                                                |
| 12  | Force Majeure                  | Present (Y/N), scope of events, notice period, termination trigger                                              |
| 13  | Audit Rights                   | Present (Y/N), scope, frequency, notice period                                                                  |
| 14  | SLA / Performance              | SLA present (Y/N), remedy type (credit / termination / both), cap on credits                                    |

**Save the extracted data in structured form** (either as an in-memory table or a
temporary reference file at `/tmp/legalcode-precedent-analysis-corpus.md`).

**⟁ CLARIFY** — For large corpora where full extraction of all 14 categories is
impractical in one pass, ask:

- "Full extraction across all 14 clause categories for [N] contracts will take significant
  time. Should I prioritize specific clause categories? Or run a quick pass (top 5-6 most
  commonly contested clauses) first, then deep-dive on request?"

### Step 5: Statistical Term Frequency Analysis

For each clause category where sufficient data exists (≥10 deals), compute:

**Clause Prevalence Rates:**

- What % of deals include this clause type at all?
- What % are missing it entirely?

Classify prevalence:

| Tier            | Prevalence                 | Meaning                                      |
| --------------- | -------------------------- | -------------------------------------------- |
| **CORE**        | ≥90% of comparable deals   | Omission is a RED flag — always include      |
| **STANDARD**    | 60–89% of comparable deals | Default include — omission warrants note     |
| **SITUATIONAL** | 20–59% of comparable deals | Include when context warrants                |
| **RARE**        | <20% of comparable deals   | Include only in specific high-risk scenarios |

**Position Distribution Analysis:**
For CORE and STANDARD clauses, group the actual positions into 2-5 variants and compute
frequency of each:

```
Clause: Limitation of Liability Cap
Corpus: 48 executed MSAs (2022-2025)

Position Distribution:
  1x12m fees cap (both parties)    ████████████████  38% (18/48 deals)
  1x contract value cap            ████████████       28% (13/48 deals)
  2x annual fees                   ████████            17% (8/48 deals)
  Negotiated specific $ amount     █████               11% (5/48 deals)
  No cap (mutual)                  ██                   4% (2/48 deals)
  Uncapped (counterparty-favored)  █                    2% (1/48 — FLAG)
```

**Counterparty-Segmented Distributions:**
Repeat the position distribution for each counterparty segment (if segmentation was
requested in Step 2). Note where certain counterparty types consistently achieve
better terms.

**Deal-Size Correlations:**
If deal size data is available, flag any statistically notable correlations:

- Do higher-value deals get more favorable limitation caps?
- Do enterprise counterparties consistently win concessions on indemnification scope?
- Does deal term length correlate with more favorable data protection terms?

**Save frequency tables** in the temporary reference file for use in later steps.

### Step 6: Negotiation Outcome Analysis

For each deal where redline history or multiple contract versions are available,
reconstruct the negotiation trajectory:

**Track the following per contested clause:**

| Outcome Type    | Definition                                                       | Implication                                                                    |
| --------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **WON**         | Our standard position was accepted without change                | Enforce in playbook as firm opening position                                   |
| **CONCEDED**    | We accepted the counterparty's position with minimal negotiation | Elevate to playbook fallback — frequent concession signals weak enforceability |
| **COMPROMISED** | Both parties moved to a middle position                          | Document the compromise range as the playbook negotiation corridor             |
| **ESCALATED**   | Required senior counsel / outside counsel / C-suite sign-off     | Flag as ESCALATE tier in playbook — do not agree without proper authority      |
| **TABLED**      | Removed from final agreement rather than agreed                  | Record as clause that is typically dropped from this deal type                 |

**Compute per-clause win rates:**

```
Clause: T4C Notice Period (Termination for Convenience)
Deals analyzed: 35 MSAs

Win Rate Summary:
  WON (30 days notice)      ██████████████  40% (14/35)
  COMPROMISED (60-90 days)  ████████████    34% (12/35)
  CONCEDED (>90 days)       ████████         23% (8/35)
  ESCALATED (180+ days)     █                 3% (1/35)

Win Rate by Counterparty Size:
  Enterprise (>1B revenue): 25% win rate  ← consistently conceded more notice
  Mid-market ($50-500M):    42% win rate
  SMB (<$50M):              65% win rate
```

**⟁ CLARIFY** — If outcome data (redline history, version tracking) is not available in
the corpus, ask:

- "I have executed final agreements but no redline history showing negotiation trajectory.
  I can analyze final positions but cannot determine what was conceded vs. our opening
  position. Would you like me to: (A) proceed with final position analysis only, noting
  this limitation; or (B) pause while you provide redline history for key deals?"

### Step 7: Client Preference Profiling

For counterparties that appear in multiple deals (recurring clients or suppliers),
build preference profiles capturing their consistent negotiating positions:

**Profile structure:**

```
Counterparty Profile: [Counterparty Type / Name-Anonymized if needed]
Deals analyzed: [N]
Deal types: [MSA / SaaS / NDA / etc.]
Date range: [earliest — latest]

Consistent Positions:
  Limitation cap:        Always pushes for 1x annual fees (accepted in X% of deals)
  T4C notice:           Never accepts <90 days (we conceded in Y% of deals)
  IP ownership:         Demands joint ownership on developed IP (we conceded in Z%)
  Data breach notice:   Always requires 48-hour notification (we accepted in A%)

Key Red Lines (never moved on):
  - [Position they never conceded]
  - [Position they never conceded]

Typical Concession Pattern:
  - Will trade [X] for [Y] — observed in [N] deals
  - Accepts [Z] if we accept [W]
```

**Client clustering:**
Group counterparty profiles into types based on shared preference patterns:

- **Type A**: Enterprise SaaS buyers — prioritize data protection, long T4C notice
- **Type B**: Mid-market services clients — price-sensitive, flexible on liability terms
- **Type C**: Strategic partners — bilateral protections, long relationship horizon
- Etc.

[JURISDICTION-SPECIFIC] Note jurisdiction-driven preference clustering: European
counterparties frequently push harder on GDPR-aligned data processing terms; US
financial services counterparties frequently demand enhanced audit rights.

### Step 8: Clause Evolution Tracking

Track how specific clause positions have changed over the analysis period:

**Time-series analysis:**
For each major clause category, group deals by year (or quarter for large corpora) and
plot how the most common position has shifted:

```
Clause: Data Breach Notification Timeline (standard obligation in data processing addenda)

Year    | Most Common Position        | % Adopting  | Notes
--------|-----------------------------|-----------  |------
2020    | 72 hours (GDPR alignment)   | 45%         | Pre-Schrems II dominance of GDPR-only
2021    | 72 hours                    | 52%         |
2022    | 72 hours or "without undue  | 61%         | UK GDPR post-Brexit divergence begins
        | delay"                      |             |
2023    | 48 hours (US state law push) | 34%         | CA CPRA / state laws driving faster timelines
        | 72 hours                    | 38%         |
2024    | 48 hours                    | 51%         | US state-law patchwork now dominant for US deals
2025    | 48 hours                    | 58%         | Emerging as new market standard for mixed portfolios
```

**Volatility scoring:**
Assign each clause category a volatility score based on how much its prevalence and
positions have shifted:

- **HIGH VOLATILITY**: >20 percentage-point shift in predominant position over analysis period — monitor closely, update playbook annually
- **MEDIUM VOLATILITY**: 10–20 pp shift — review playbook every 2 years
- **STABLE**: <10 pp shift — review playbook every 3-5 years

**Trigger event annotations:**
Note regulatory or market events that correlate with position shifts:

- EU data protection changes (GDPR enforcement, Schrems II, UK GDPR divergence)
- FTC non-compete rule / state-level bans
- Major court decisions affecting enforceability (e.g., Cavendish Square penalty doctrine)
- Industry-specific regulatory events (HIPAA amendments, SEC reporting changes)

### Step 9: Market Gap Analysis

Compare the firm's standard positions (derived from the corpus analysis) against
published market standards:

**Market benchmark sources:**

| Source                                  | Best For                                                                     | Citation                                        |
| --------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------- |
| Bloomberg Law Draft Analyzer            | US commercial contracts — benchmarks against EDGAR-filed agreements [VERIFY] | Bloomberg Law benchmarking tools                |
| World Commerce & Contracting (World CC) | Contract management metrics, cycle times [VERIFY]                            | World CC annual benchmarking reports            |
| Thomson Reuters Practical Law           | Market standard language for US, UK, and EU deals [VERIFY]                   | Practical Law Standard Documents                |
| ABA Model Contracts                     | US-specific contract type benchmarks [VERIFY]                                | ABA Section of Business Law model forms         |
| WSMA / ACC surveys                      | In-house counsel perspective on acceptable terms [VERIFY]                    | ACC/CLOC annual surveys                         |
| Stanford Material Contracts Corpus      | Public company contracts (via SEC EDGAR filings) [VERIFY]                    | mcc.law.stanford.edu (1M+ contracts, 2000-2023) |

**Market gap classification:**

| Gap Level        | Definition                                                   | Action                                                 |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------ |
| **ABOVE MARKET** | Firm's position is more protective than published benchmarks | No change needed; use as leverage signal               |
| **AT MARKET**    | Firm's position aligns with published benchmarks             | Maintain; cite benchmarks in negotiations              |
| **BELOW MARKET** | Firm's position is less protective than published benchmarks | Flag for playbook review; may signal under-negotiation |
| **NO BENCHMARK** | No published market standard for this position               | Rely on corpus-internal norms only; flag explicitly    |

**⟁ CLARIFY** — If legalcode-mcp is available, search for current market benchmarks on
the top 5 most contested clause types identified in Step 5. If not connected, mark all
market benchmark comparisons with [VERIFY — market data not independently confirmed].

### Step 10: Generate the Playbook

Synthesize all prior analysis into a structured negotiation playbook. For each major
clause category, define:

**Four-position structure:**

1. **BASELINE**: The opening position — the firm's preferred position backed by the
   highest win rate and strongest market support. Do not concede below this without
   documented justification.
2. **FALLBACK**: The acceptable alternative — a position the firm has historically
   accepted and can accept again without escalation. Document the specific language
   and conditions under which this fallback applies.
3. **ESCALATE**: The position that requires senior review — below the acceptable risk
   threshold but potentially acceptable in high-value or strategic deals with documented
   approval. Name the required approver (e.g., GC, CFO, C-suite).
4. **RED-LINE**: Non-negotiable position — never concede without approval from the named
   authority level. Document the specific risk that makes this non-negotiable and the
   authority required to override.

**Playbook entry template:**

```
Clause: [Clause Name]
Corpus data: [N] deals analyzed | Win rate at baseline: [X]% | Last updated: [date]
Market alignment: [AT MARKET / ABOVE / BELOW / NO BENCHMARK]

BASELINE (opening position):
  Language: "[Standard clause text — abbreviated]"
  Rationale: [Why this is the opening position]
  Win rate: [X]% across comparable deals

FALLBACK (acceptable alternative):
  Language: "[Fallback clause text]"
  Trigger: [When/why to move to this position]
  Conditions: [Any specific deal conditions that must be met to accept this fallback]
  Historical frequency: Conceded in [Y]% of deals

ESCALATE (requires senior approval):
  Language: "[Escalation-tier clause text]"
  Approver required: [Role / level]
  Risk exposure: [Brief description of the incremental risk accepted at this level]
  Historical frequency: Reached in [Z]% of deals

RED-LINE (never without named authority):
  Definition: [The specific position or absence of clause that triggers red-line status]
  Authority required: [Named role — not "senior management" but "General Counsel and CFO"]
  Rationale: [The specific legal/financial risk that makes this a red line]
```

**⟁ CLARIFY** — Before generating the full playbook, confirm the scope:

- "The analysis covers [N] clause categories. Should I generate full playbook entries for
  all of them, or focus on the top [X] most frequently contested or highest-volatility
  categories first?"
- "Some playbook entries will cite specific language from prior deals. Should counterparty
  names be anonymized in the playbook output, or is full attribution acceptable for
  internal use?"

### Step 11: Quality Verification

Before delivering outputs, apply the quality checks defined in the Quality Assurance
Framework section:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every ESCALATE or RED-LINE classification, run the 3-pass Self-Interrogation.
3. Assign a Confidence Score to each statistical claim based on corpus size.
4. Verify completeness: confirm all requested clause categories have been addressed.
5. Generate the Glass Box Audit Trail and append to the output.
6. Check that all market benchmark comparisons are either verified or marked [VERIFY].
7. Confirm that counterparty confidentiality preferences from Step 2 have been applied.

---

## Corpus Analysis Framework

### Minimum Corpus Requirements

Statistical analysis is only meaningful with sufficient data. Apply these minimums:

| Analysis Type           | Minimum Deals        | Ideal Deals | Reliability Note                                                 |
| ----------------------- | -------------------- | ----------- | ---------------------------------------------------------------- |
| Clause prevalence rate  | 10                   | 30+         | Below 10: directional only, not statistically reliable           |
| Position distribution   | 15                   | 50+         | Below 15: identify top 2-3 positions only, suppress tail         |
| Win/loss rate by clause | 20                   | 50+         | Below 20: report directionally, caveat heavily                   |
| Counterparty profile    | 5 deals/counterparty | 10+         | Below 5: insufficient for profiling, note as anecdotal           |
| Clause evolution trend  | 3 time periods       | 5+ years    | Below 3 periods: insufficient for trend claim                    |
| Market gap analysis     | Any size             | N/A         | Apply regardless — benchmark gaps are independent of corpus size |

When the corpus falls below minimum thresholds, prefix the relevant outputs with
**[LOW CONFIDENCE — N=[X]]** and recommend augmenting the corpus before relying on
these statistics for playbook policy.

### Corpus Segmentation Logic

Before computing statistics, apply this segmentation hierarchy:

1. **Primary segmentation by deal type** (always): Do not mix NDAs, MSAs, SaaS
   agreements, and employment contracts in the same frequency analysis.

2. **Secondary segmentation by jurisdiction** (always for multi-law corpora): Do not
   mix English-law and New York-law deals for substantive clause analysis.

3. **Tertiary segmentation by counterparty type** (if requested or if data shows
   material differences): Enterprise vs. mid-market positions often differ by 20-30+
   percentage points on major clauses.

4. **Quaternary segmentation by time period** (for evolution analysis): Annual or
   quarterly buckets, depending on corpus volume.

Never aggregate across segments without clearly labeling the scope:

```
❌ Wrong:  "Our standard LoL cap is 1x annual fees (38% of deals)"
✅ Right:  "For MSAs with US enterprise SaaS customers (2022-2025), our most common
           LoL cap is 1x annual fees (38% of 48 deals in this segment)"
```

### Corpus Quality Scoring

Rate the corpus quality at intake:

| Dimension                | Score 1 (Low)                         | Score 5 (High)                               |
| ------------------------ | ------------------------------------- | -------------------------------------------- |
| **Completeness**         | Many documents missing, gaps in years | All executed agreements, complete date range |
| **Structuredness**       | Raw PDFs, no extracted metadata       | Full CLM export with structured fields       |
| **Homogeneity**          | Mixed types, multiple jurisdictions   | Single type, single jurisdiction             |
| **Volume**               | <15 deals per segment                 | 50+ deals per segment                        |
| **Redline availability** | Final executed only                   | Multiple drafts + final for most deals       |

Report the total corpus quality score (out of 25) at the start of the analysis and
calibrate confidence levels accordingly:

- **20-25**: High-confidence analysis — statistical claims are reliable
- **12-19**: Moderate-confidence analysis — directional, but caveat key statistics
- **Below 12**: Low-confidence analysis — use for exploration only, not policy-making

---

## Statistical Analysis Methodology

### Term Frequency Calculation

For each clause position within a clause category:

1. Count the number of deals where this exact position (or semantically equivalent
   position) appears.
2. Divide by the total number of deals in the relevant segment.
3. Report as a percentage with the numerator/denominator explicit (e.g., "38% (18/48)").

**Semantic equivalence grouping:**
Positions that differ in phrasing but are legally equivalent should be grouped. For
example, "12 months' fees," "one year's service fees," and "12x monthly contract value"
are semantically equivalent limitation-of-liability caps. Cluster them before counting.

**Variant taxonomy:**
For each clause category, define a flat taxonomy of 3-7 standard positions. Positions
that don't fit any defined variant are classified as CUSTOM and flagged for manual review.
Do not create more variants than the corpus can meaningfully populate (avoid a variant
taxonomy with 10 variants in a 15-deal corpus).

### Confidence Intervals for Small Samples

When reporting percentages from small corpora, note the uncertainty:

| N (deals in segment) | Confidence Note                                                         |
| -------------------- | ----------------------------------------------------------------------- |
| < 10                 | Do not report percentages — report as "X of N deals only"               |
| 10-24                | Report percentage with note: "based on [N] deals — directional only"    |
| 25-49                | Report percentage with note: "based on [N] deals — moderate confidence" |
| 50+                  | Report percentage without special qualifier                             |

### Correlation Analysis

Flag correlations between variables where they appear in the data, but apply the
following cautions:

- Correlation ≠ causation: A correlation between deal size and better LoL terms may
  reflect the bargaining power of larger customers, not that larger deals inherently
  warrant different terms.
- Confounded variables: Counterparty industry and deal size often correlate — report
  both effects separately before attributing causation to either.
- Always report the N for each correlation claim.

---

## Clause Evolution Tracking

### Version Comparison Protocol

When multiple contract versions (redlines) are available for a single deal:

1. Identify the first draft (typically the firm's or counterparty's opening position)
2. Track each redline cycle (Draft 1 → Draft 2 → Draft 3 → Final Executed)
3. For each contested clause, record the trajectory: what changed, who moved, how much

Use this format for per-deal clause trajectories:

```
Deal: [Anonymized ID]  |  Clause: Limitation of Liability Cap
Draft 1 (our opening):  1x annual fees (BASELINE position)
Draft 2 (counterparty): 3x annual fees (counterparty's preferred position)
Draft 3 (our response): 1x annual fees with IP carveout (compromise approach)
Final executed:         1.5x annual fees, IP excluded from cap
Outcome: COMPROMISED — we moved from 1x to 1.5x, counterparty moved from 3x to 1.5x
```

### Temporal Trend Visualization

Represent clause evolution in tabular form with directional indicators:

```
[↑] = Position becoming more protective over time
[↓] = Position becoming less protective / more concessive over time
[→] = Stable position
[?] = Insufficient data for trend
```

### Volatility Scoring

Assign volatility scores to flag clauses requiring more frequent playbook review:

| Score | Label             | Trigger                             | Review Cadence           |
| ----- | ----------------- | ----------------------------------- | ------------------------ |
| 3     | HIGH VOLATILITY   | ≥20pp shift in most common position | Annual                   |
| 2     | MEDIUM VOLATILITY | 10-19pp shift                       | Biennial                 |
| 1     | STABLE            | <10pp shift                         | Every 3-5 years          |
| 0     | INSUFFICIENT DATA | <3 time periods                     | Flag for future tracking |

---

## Negotiation Outcome Analysis

### Win/Loss Methodology

**What counts as a "win":**
A win occurs when the final executed position matches or exceeds the BASELINE playbook
position (the firm's opening preferred position). Not every win is equally valuable —
a win on a non-material clause is not the same as a win on limitation of liability.

**Weighting wins by clause materiality:**
Weight the win/loss score by clause importance:

| Weight | Clause Tier | Examples                                                 |
| ------ | ----------- | -------------------------------------------------------- |
| 3      | Critical    | LoL cap, uncapped indemnity, IP ownership                |
| 2      | Important   | T4C notice, auto-renewal terms, data breach notification |
| 1      | Standard    | Governing law, counterpart execution, notice addresses   |

**Weighted win rate** = Σ(win × weight) / Σ(weight) — use this for overall portfolio score.

### Concession Pattern Analysis

For each CONCEDED outcome, record:

- What was conceded (clause and position)
- When in the negotiation cycle it was conceded (early / late)
- What, if anything, was received in exchange
- Whether the concession was authorized at the right level

**Patterns to flag:**

- Repeated identical concessions on the same clause without any quid pro quo → suggests
  the "conceded" position should be promoted to FALLBACK in the playbook
- Late-stage concessions with no quid pro quo → suggests negotiator time pressure;
  recommend pre-authorizing fallbacks earlier
- Concessions made without documented approvals where ESCALATE-tier was triggered →
  process breakdown, recommend workflow remediation

---

## Client Preference Modeling

### Preference Profile Structure

Build a preference profile for any counterparty (or counterparty type) appearing in
5 or more deals:

```yaml
preference_profile:
  counterparty_type: "[Enterprise SaaS Vendor / Fortune 500 Customer / etc.]"
  deals_analyzed: [N]
  date_range: "[earliest] to [latest]"
  deal_types: "[MSA, SaaS, SOW]"

  known_red_lines:
    - clause: "[Clause type]"
      position: "[Their non-negotiable position]"
      observed_in: "[X of N deals]"

  typical_opening_positions:
    limitation_of_liability: "[Their opening ask]"
    ip_ownership: "[Their opening ask]"
    # etc.

  known_concession_patterns:
    - "Will accept [X] if we accept [Y] — observed in [N] deals"
    - "Always moves on [clause] by [N] days when deal value exceeds [$X]"

  recommended_strategy:
    lead_with: "[Clause most likely to create value]"
    trade_early: "[Clause we can safely concede early to build goodwill]"
    hold_firm: "[Clause to never concede with this counterparty type]"
```

### Anonymization Protocol

When confidentiality is required:

- Replace counterparty names with anonymized codes (Counterparty A, B, C or CP-001, CP-002)
- Group by type/industry rather than identifying individual entities
- Never include deal-specific financial terms in shared outputs
- Note in the Glass Box: `counterparty_anonymization: "Applied — see internal reference file"`

---

## Position Classification System

Every extracted clause position is classified into one of four tiers:

### BASELINE

**Definition**: The firm's preferred opening position, supported by historical win rates
of ≥50% in comparable deals and consistent with market benchmarks (AT MARKET or ABOVE).

**Characteristics**:

- Standard language, used in most new agreements without negotiation
- Can be defended to counterparties with reference to market standard
- Win rate across comparable deals is materially above 50%

**Playbook instruction**: Lead with this position. Do not retreat without documented
counterparty resistance and impact assessment.

### FALLBACK

**Definition**: A position the firm has historically accepted in negotiations without
escalation, representing a reasonable compromise.

**Characteristics**:

- Different from BASELINE but within acceptable risk range
- Accepted in ≥20% of comparable deals without escalation
- Does not materially increase firm risk exposure beyond acceptable levels

**Playbook instruction**: Move to FALLBACK only after counterparty explicitly rejects
BASELINE. Document the concession and any quid pro quo received.

### ESCALATE

**Definition**: A position that increases firm risk meaningfully and requires documented
approval from senior counsel or named stakeholder before agreement.

**Characteristics**:

- Below acceptable risk threshold for standard authority
- May have been accepted previously only under documented special circumstances
- Requires named approver on record before deal proceeds

**Playbook instruction**: Do not agree without written approval from [role]. Bring to
deal team/GC with risk memo before the next negotiation session.

### RED-LINE

**Definition**: A position (or absence of a clause) that the firm will not accept under
any circumstances without specific override from the highest named authority.

**Characteristics**:

- Accepted in <5% of comparable deals or never accepted
- Creates legal, financial, or reputational exposure beyond acceptable limits
- Any prior acceptance was documented as a specific exception, not general policy

**Playbook instruction**: Withdraw offer / escalate to [GC / CFO / Board] immediately.
A red-line concession is not a negotiation decision — it is an exception decision that
requires documented business justification and sign-off at the highest named level.

---

## Playbook Generation Framework

### Playbook Structure

The output playbook follows this structure:

```
Part 1: Portfolio Overview
  1.1 Corpus summary (N deals, date range, deal types, jurisdictions)
  1.2 Overall portfolio health score (weighted win rate)
  1.3 Top 5 most-won positions
  1.4 Top 5 most-conceded positions
  1.5 Market alignment summary

Part 2: Clause-Level Playbook
  [For each clause category, in order of materiality]
  2.1 Statistical summary (prevalence, most common positions, win rates)
  2.2 BASELINE / FALLBACK / ESCALATE / RED-LINE positions
  2.3 Clause evolution note (volatility score, trend direction)
  2.4 Market gap note (AT/ABOVE/BELOW market or NO BENCHMARK)
  2.5 Counterparty-type adjustments (if applicable)

Part 3: Counterparty Profiles
  [For counterparty types with ≥5 deals]
  3.1 Preference profile per type
  3.2 Recommended negotiation strategy per type

Part 4: Flagged Outliers
  4.1 Deals with unusual terms not captured in standard playbook
  4.2 Deals where ESCALATE/RED-LINE positions were accepted without documented approval
  4.3 Clauses with HIGH VOLATILITY scores requiring near-term playbook refresh

Part 5: Maintenance Schedule
  5.1 Recommended playbook refresh schedule by clause (based on volatility scores)
  5.2 Suggested corpus update frequency
  5.3 Metrics to track for ongoing playbook validation
```

### Playbook Maintenance Triggers

Recommend a playbook refresh when any of the following occur:

- A new deal type is added to the firm's practice
- A regulatory or legislative change affects a major clause category [JURISDICTION-SPECIFIC]
- The win rate on a previously strong BASELINE position drops below 40% across 5+ consecutive deals
- A new counterparty type is added representing >10% of deal volume
- More than 24 months have passed without a formal refresh of HIGH VOLATILITY clauses

---

## Prioritization Framework

After generating the playbook, prioritize the findings for immediate action:

### Tier 1 — Immediate Action (Address Before Next Deal Cycle)

- Any clause where current positions are classified as BELOW MARKET and the win rate
  is also declining — combined signal of under-negotiation
- Any clause where ESCALATE or RED-LINE positions were accepted without documented
  approval in the analysis period — process and authority issues
- Any counterparty profile showing a consistent pattern of last-minute concessions
  on high-weight clauses — suggests systemic negotiation pressure issues

### Tier 2 — Next Playbook Refresh (Address in the Next 3–6 Months)

- HIGH VOLATILITY clauses with no recent playbook update
- Clauses where the corpus shows a clear trend diverging from the current playbook
  position (e.g., market is moving to 48-hour data breach notification but playbook
  still says 72 hours)
- Counterparty profiles where negotiation strategy has not been formally documented

### Tier 3 — Background Monitoring (Annual Review)

- STABLE clauses with AT MARKET or ABOVE MARKET positions and strong win rates
- Counterparty profiles with limited deal history (2-4 deals — not yet enough data)
- Clause categories with INSUFFICIENT DATA — schedule corpus augmentation

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise:

| Gate           | Rule                                                                                            | Fail Action                                                                       |
| -------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Source**     | Every statistical claim cites the specific corpus segment (N, date range, deal type)            | Add corpus citation or mark "[UNVERIFIED COUNT]"                                  |
| **Format**     | All clause positions cited use a consistent format (exact language or standardized description) | Fix format; do not mix paraphrase with quoted text without distinguishing clearly |
| **Currency**   | All market benchmarks checked for recency (benchmark data >3 years old flagged)                 | Flag "[CHECK CURRENCY — benchmark from {year}]"                                   |
| **Domain**     | Analysis stays within the stated corpus scope (no claims about deal types not in the corpus)    | Remove or flag out-of-scope inferences                                            |
| **Confidence** | Uncertainty explicitly stated; small-N caveats applied; no false precision on percentages       | Add appropriate confidence qualifier                                              |

### Self-Interrogation for ESCALATE and RED-LINE Classifications

For any ESCALATE or RED-LINE classification, apply this 3-pass review:

**Pass 1 — Basis Integrity**: Is the classification based on sufficient corpus evidence,
or is it derived from a single outlier deal? Would a differently composed corpus (e.g.,
excluding one large unusual deal) reach the same classification?

**Pass 2 — Completeness**: Have all relevant comparable deals been included in the
analysis segment? Were any excluded that might change the classification? Has the market
gap analysis been applied to validate the classification against published benchmarks?

**Pass 3 — Challenge**: What is the strongest argument for accepting the position
classified as ESCALATE or RED-LINE? Under what deal conditions (deal size, strategic
value, counterparty relationship) might a reasonable senior counsel accept it? If those
conditions exist, document them as ESCALATE conditions rather than using a hard RED-LINE.

### Confidence Scoring

| Level            | Range     | Meaning                                           | Action                                                      |
| ---------------- | --------- | ------------------------------------------------- | ----------------------------------------------------------- |
| **Definite**     | 0.95–1.0  | Large, clean corpus; position highly consistent   | Report with confidence                                      |
| **High**         | 0.80–0.94 | Sufficient corpus (30+ deals); some variance      | Report with minor caveat                                    |
| **Probable**     | 0.60–0.79 | Moderate corpus (15–29 deals); pattern visible    | Report with corpus-size caveat                              |
| **Possible**     | 0.40–0.59 | Small corpus (10–14 deals); directional only      | Flag as "[LOW CONFIDENCE — N=[X]]"                          |
| **Insufficient** | 0.0–0.39  | Too few deals (<10); not statistically meaningful | Do not report as a statistic; note as anecdotal observation |

Apply confidence scores to:

- Each clause frequency claim
- Each win/loss rate
- Each market gap determination
- Each counterparty profile recommendation

---

## Glass Box Audit Trail

Append this YAML block to every analysis output:

```yaml
glass_box:
  skill_name: "legalcode-precedent-analyzer"
  mode: "Corpus analysis — playbook generation"
  run_date: "[YYYY-MM-DD]"
  corpus_summary:
    total_documents: "[N]"
    deal_types_analyzed: "[list]"
    date_range: "[earliest] to [latest]"
    jurisdictions: "[list]"
    documents_excluded: "[N] — reason: [reason]"
  segmentation_applied:
    primary: "[By deal type — Y/N]"
    secondary: "[By jurisdiction — Y/N]"
    tertiary: "[By counterparty type — Y/N]"
  corpus_quality_score: "[X]/25"
  minimum_thresholds_met:
    clause_prevalence: "[Y/N — N=[X] for lowest-volume segment]"
    win_loss_analysis: "[Y/N — N=[X] for lowest-volume segment]"
    counterparty_profiles: "[Y/N — profiles built for [N] types]"
  legalcode_mcp: "Connected / Not connected"
  market_benchmarks_verified: "[N VERIFIED] / [N marked [VERIFY]]"
  anonymization_applied: "[Y/N — scope: [counterparty names / none]]"
  confidence_overall: "HIGH / MODERATE / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, data gaps, or corpus quality caveats]"
    - "[Specific clause categories with insufficient data]"
    - "[Jurisdictions where analysis is incomplete]"
  playbook_tiers_generated:
    clauses_with_full_4tier_playbook: "[N]"
    clauses_with_partial_data: "[N]"
    clauses_excluded_insufficient_data: "[N]"
  reviewer: "AI-assisted — requires qualified legal review before operational use"
```

---

## Anti-Patterns

The following errors commonly undermine precedent analysis quality. Avoid them:

1. **Mixing contract types in frequency statistics** — Computing a single "standard LoL
   cap" by combining MSAs, NDAs, and employment agreements produces a meaningless average.
   Always segment by contract type before aggregating.

2. **Confusing final position with negotiation trajectory** — A corpus of executed
   agreements shows only what was ultimately agreed, not what was opened with or conceded.
   Without redline history, "standard position" means "most commonly accepted final
   position" — which may be lower than the firm's actual opening position.

3. **Treating correlation as policy** — If enterprise deals consistently have higher LoL
   caps, that may be because enterprise deals involve higher stakes and justified different
   terms, not because enterprise customers are "entitled" to better terms. Do not
   automatically import observed correlations into the playbook as rules.

4. **Promoting concession rates to baselines** — If the firm conceded 1x annual fees in
   60% of deals, that makes it a FALLBACK candidate — not the new BASELINE. A playbook
   that opens at the most frequently conceded position has already surrendered value
   before the negotiation starts.

5. **Ignoring temporal obsolescence** — A corpus spanning 2018–2025 applies 2018 market
   norms equally with 2025 norms unless segmented by time. Old positions can drag down
   statistical scores for current market standards. Limit active playbook analysis to
   deals within the last 3-5 years unless historical trend analysis is the specific goal.

6. **False precision on small samples** — Reporting "42.3% win rate" based on 12 deals
   implies statistical precision that does not exist. Round percentages to whole numbers
   and cite N prominently when N < 30.

7. **Omitting clause absences** — A clause that is completely absent from 40% of deals
   is analytically important. Omitting it from the frequency analysis because there is
   "nothing to extract" produces an incomplete picture of negotiation behavior.

8. **Building profiles from too few deals** — A counterparty "profile" based on 2 or 3
   deals reflects chance or circumstance, not pattern. Wait for 5+ deals before treating
   observations as preference data.

9. **Skipping privilege and confidentiality review** — Deal-specific information,
   counterparty identities, and negotiation strategies may carry confidentiality
   obligations. Do not generate externally shareable outputs without stripping or
   anonymizing this information.

10. **Producing a static playbook without maintenance guidance** — A playbook without
    a refresh schedule and volatility scores attached to each clause is a playbook that
    silently becomes outdated. Every playbook entry must carry a recommended review date.

11. **Conflating market standard with firm standard** — What the corpus shows the firm
    has historically accepted is the firm's track record, not market standard. Always
    compare against external benchmarks and distinguish clearly between internal corpus
    data and market benchmark data.

12. **Generating playbooks without authority tiers** — A playbook that lists "standard
    positions" without defining who can authorize deviations creates negotiation risk.
    Every ESCALATE and RED-LINE position must name a specific role or approval chain.

13. **Excluding outlier deals from the analysis** — Unusual deals with one-sided or
    atypical terms are analytically valuable. They often reveal what counterparties can
    extract under leverage conditions. Analyze them in a separate "Outliers" section
    rather than discarding them.

14. **Normalizing jurisdiction-specific positions across borders** — A common position
    in English-law MSAs is not automatically applicable to New York-law MSAs or
    German-law service agreements. Jurisdiction-specific analysis is mandatory before
    cross-border positions are recommended. [JURISDICTION-SPECIFIC]

15. **Generating playbooks without negotiation corridor guidance** — A playbook that
    states only opening positions (BASELINE) without fallbacks, corridor ranges, and
    escalation paths is incomplete. Negotiators need to know where they can go, not just
    where they start.

16. **Treating LLM-extracted clause data as ground truth** — Every material clause
    position extracted by this skill should be spot-checked against a sample of source
    documents before the playbook is finalized. LLM extraction is fast and directionally
    accurate but not infallible on nuanced clause language.

17. **Ignoring negotiation context when interpreting outcomes** — A "loss" on indemnification
    scope in a strategic partnership deal may have been an intentional concession in
    exchange for favorable pricing or exclusivity. Win/loss statistics without context
    can misrepresent actual deal quality.

---

## Writing Standards

Apply these standards before delivering any analysis output:

1. **Quantify explicitly**: Never write "frequently" or "commonly" — always write "38%
   (18/48 deals)."

2. **Distinguish sources**: Clearly separate corpus-derived data from market benchmarks
   from general commercial knowledge. Label each.

3. **Caveat small samples**: Any claim based on fewer than 25 data points must carry an
   explicit small-sample caveat in the same sentence, not in a footnote.

4. **Use consistent terminology**: Within a single analysis run, use one consistent name
   for each clause type. Do not alternate between "limitation of liability," "LoL cap,"
   and "liability cap" for the same clause.

5. **Lead with the finding, not the method**: Do not write "After analyzing 48 MSAs
   using frequency analysis, I found that..." — write "LoL cap: 1x annual fees is the
   most common position (38% of 48 MSAs, 2022-2025)."

6. **Mark all unverified market references**: Any reference to an external benchmark
   that was not independently verified in this session must carry [VERIFY].

7. **Separate analysis from recommendation**: Present the data first (what the corpus
   shows), then the recommendation (what the playbook should say). Do not conflate the
   two.

8. **Preserve counterparty confidentiality by default**: When in doubt, anonymize.
   The analytical value of a corpus analysis does not depend on naming specific
   counterparties.

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

In Step 9 (Market Gap Analysis), use legalcode-mcp to search for current market
benchmarks on the most contested clause types:

- Search for recent surveys or benchmarking studies on limitation of liability caps
  for the relevant deal type
- Search for current regulatory requirements that constrain certain positions
  (data breach notification timelines, mandatory employee protections, etc.)
- Verify that the playbook's BASELINE positions remain legally compliant in the
  identified governing law jurisdictions
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

Save the most relevant results to `/tmp/legalcode-precedent-analysis-research.md`:

```markdown
# Market Research — Precedent Analysis

## Date: [date]

## Corpus deal types: [list]

### Benchmarking Findings

- [Clause type, benchmark source, current market standard, jurisdiction]

### Regulatory Requirements

- [Statute/regulation, jurisdiction, effect on clause positions]

### Recent Legal Developments

- [Development, date, impact on playbook positions]
```

### Without legalcode-mcp (Graceful Degradation)

- Proceed with corpus analysis in Steps 1-8 without market verification
- In Step 9, note that market gap analysis is based on general commercial knowledge only
- Mark all market benchmark comparisons with [VERIFY — not independently confirmed]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — market benchmarks unverified"`
- Recommend that market gap analysis be re-run once legalcode-mcp is available before
  the playbook is used in live negotiations

---

## Output Format Templates

### Template 1: Corpus Overview Report

```markdown
# Precedent Analysis — Corpus Overview

**Run date**: [date]
**Deal types analyzed**: [list]
**Total documents**: [N] ([N] executed, [N] drafts, [N] excluded)
**Date range**: [earliest] to [latest]
**Jurisdictions**: [list]
**Corpus quality score**: [X]/25 ([HIGH/MODERATE/LOW] confidence)

## Corpus Composition

| Deal Type | Count | %    | Date Range | Avg. Deal Value   |
| --------- | ----- | ---- | ---------- | ----------------- |
| [Type]    | [N]   | [X%] | [range]    | [$X if available] |

## Portfolio Health Summary

- **Overall weighted win rate**: [X]%
- **Top 3 most-won positions**: [list with win rates]
- **Top 3 most-conceded positions**: [list with concession rates]
- **Clauses with HIGH VOLATILITY**: [list]
- **Clauses with BELOW MARKET positions**: [list]
```

### Template 2: Clause Playbook Entry

```markdown
## [Clause Name]

**Prevalence**: [CORE/STANDARD/SITUATIONAL/RARE] — present in [X]% ([N/total]) of [deal type] deals
**Win rate at BASELINE**: [X]% | **Volatility**: [HIGH/MEDIUM/STABLE]
**Market alignment**: [AT MARKET / ABOVE / BELOW / NO BENCHMARK]
**Confidence**: [level] (N=[total in segment])

### Position Distribution

| Position     | Frequency  | Win Rate | Classification      |
| ------------ | ---------- | -------- | ------------------- |
| [Position A] | [X]% ([N]) | [X]%     | BASELINE            |
| [Position B] | [X]% ([N]) | [X]%     | FALLBACK            |
| [Position C] | [X]% ([N]) | [X]%     | ESCALATE            |
| [Position D] | [X]% ([N]) | [X]%     | RED-LINE if imposed |

### BASELINE

**Language**: "[Standard clause text]"
**Rationale**: [Why this is the opening position — corpus data + market alignment]

### FALLBACK

**Language**: "[Fallback clause text]"
**When to use**: [Trigger conditions]
**Conditions**: [Any required quid pro quo or deal conditions]

### ESCALATE

**Language**: "[Escalation-tier clause text or condition description]"
**Approver required**: [Role]
**Risk memo template**: "[Brief risk description for escalation memo]"

### RED-LINE

**Trigger**: [The specific position or clause absence that triggers red-line status]
**Authority required**: [Named role — e.g., "General Counsel with CFO co-sign"]
**Rationale**: [The specific exposure that makes this non-negotiable]

### Clause Evolution

**Trend**: [↑ More protective / ↓ Less protective / → Stable] over [time period]
**Key inflection point**: [Year/event that drove the most significant change, if identifiable]
**Next scheduled review**: [Date based on volatility score]
```

### Template 3: Negotiation Outcome Summary

```markdown
# Negotiation Outcome Report

**Corpus**: [N] deals with outcome data ([N] with full redline history, [N] final-only)

## Win/Loss Summary by Clause (Weighted)

| Clause          | Weight | WON | COMPROMISED | CONCEDED | ESCALATED | Win Rate |
| --------------- | ------ | --- | ----------- | -------- | --------- | -------- |
| LoL Cap         | 3      | [N] | [N]         | [N]      | [N]       | [X]%     |
| Indemnification | 3      | [N] | [N]         | [N]      | [N]       | [X]%     |
| IP Ownership    | 3      | [N] | [N]         | [N]      | [N]       | [X]%     |
| [etc.]          | ...    | ... | ...         | ...      | ...       | ...%     |

## Weighted Portfolio Win Rate: [X]%

## Key Observations

- [Top insight from win/loss analysis]
- [Notable counterparty-type pattern]
- [Notable deal-size correlation]
- [Process issue flagged — unauthorized concessions, etc.]
```

### Template 4: Counterparty Preference Profile

```markdown
# Counterparty Profile: [Type / Anonymized ID]

**Deals analyzed**: [N] | **Date range**: [range] | **Deal types**: [list]

## Known Red Lines (never moved on)

| Clause   | Their Position                  | Observed in |
| -------- | ------------------------------- | ----------- |
| [Clause] | [Their non-negotiable position] | [N/N deals] |

## Typical Concession Pattern

- Will accept [X] if we accept [Y] — observed in [N/N deals]
- Moves on [clause] by [N days/X%] when deal value exceeds [$X]

## Recommended Strategy

- **Lead with**: [Clause most likely to create value or establish goodwill]
- **Trade early**: [Clause we can safely concede without material loss]
- **Hold firm**: [Clause to defend throughout this counterparty type]
- **Watch for**: [Pattern or tactic this counterparty type typically uses]
```

### Template 5: Executive Dashboard

```markdown
# Legal Precedent Analysis — Executive Summary

**Date**: [date] | **Prepared for**: [audience]

## Portfolio Health at a Glance

- **Deals analyzed**: [N] | **Date range**: [range]
- **Weighted win rate**: [X]% ([Good/Fair/Needs Attention] — benchmark: 55-65% target for commercial legal teams)

## 3 Things the Data Shows We Do Well

1. [Specific clause / position with strong win rate]
2. [Specific clause / position with strong win rate]
3. [Specific clause / position with strong win rate]

## 3 Areas Requiring Immediate Attention

1. [Clause/position: issue + recommended action]
2. [Clause/position: issue + recommended action]
3. [Clause/position: issue + recommended action]

## Playbook Refresh Priorities

| Priority | Clause   | Issue   | Recommended Action | Owner  |
| -------- | -------- | ------- | ------------------ | ------ |
| Tier 1   | [Clause] | [Issue] | [Action]           | [Role] |
| Tier 2   | [Clause] | [Issue] | [Action]           | [Role] |

## Recommended Next Steps

1. [Immediate action — before next deal cycle]
2. [30-day action — playbook update]
3. [90-day action — process improvement]
```

---

## Localization Notes

### Jurisdiction-Agnostic Design

This skill is designed to work across deal corpora governed by different legal systems.
The following adaptations are required when the corpus spans multiple jurisdictions:

1. **Always segment before aggregating**: Run separate frequency analyses for English-law
   deals, New York-law deals, German-law deals, etc. Never merge jurisdictions before
   validating that positions are legally comparable.

2. **Apply [JURISDICTION-SPECIFIC] markers** to any playbook position that varies by
   governing law. Example: "LoL cap at 1x annual fees [AT MARKET — US/UK commercial law;
   [JURISDICTION-SPECIFIC] verify under German BGB §307-309 proportionality requirement
   and French Code Civil Art. 1231-3 limitation enforceability]."

3. **Data protection clause positions** vary substantially by jurisdiction:
   [JURISDICTION-SPECIFIC] GDPR/UK GDPR positions are not directly comparable to US
   state-law positions; analyze separately and flag divergences.

4. **Non-compete clauses** are jurisdiction-specific by nature:
   [JURISDICTION-SPECIFIC] US state-law variance (CA ban, FTC rule litigation, state
   non-compete enforcement range); UK Pye v British Fuels; German Handelsgesetzbuch
   §74-75d commercial agent rules. Never treat US non-compete positions as applicable
   to EU or UK corpora without explicit local review.

5. **Mandatory statutory terms** cannot be contracted out of regardless of prior deal
   history — do not classify positions that violate mandatory law as FALLBACK or
   BASELINE even if historically accepted. [JURISDICTION-SPECIFIC] Always verify
   that BASELINE positions are legally permissible in the governing law jurisdiction.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis informed by:

- Academic research on legal NLP and clause extraction (Stanford CUAD dataset, ContractNLI,
  Stanford Material Contracts Corpus — mcc.law.stanford.edu)
- Industry contract analytics platform methodologies (Spellbook, Ontra, Icertis, TermScout,
  Sirion, ContractKen, Spotdraft — studied for analytical framework design, not content)
- Legal knowledge management best practices (Prism Legal, CenterBase, ABA LTRC guidance)
- Negotiation outcome analysis frameworks (Harvard PON, INSEAD)
- Clause evolution tracking methodology (Ontra transition matrix research, 2024)
- Legalcode quality frameworks from legalcode-contract-review reference standard
- All statutory and case law references in this skill should be verified by qualified
  counsel before operational use — they are provided as orientation, not authoritative guidance
