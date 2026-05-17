---
name: legalcode-due-diligence-report
description: >
  Structure M&A due diligence findings into executive-ready reports with material risks,
  deal-breaker identification, negotiation leverage points, closing conditions, and
  post-closing integration risks. Use when compiling legal due diligence findings into
  board presentations, legal memoranda, or commercial deal reports for mergers,
  acquisitions, carve-outs, joint ventures, or corporate investments. Produces
  audience-differentiated output in three formats — board/executive, legal/counsel,
  and commercial/deal team — with risk heat maps, remediation recommendations, and a
  negotiation playbook. Supports US, UK, and EU transactions. Triggers on "due diligence
  report", "DD report", "findings report", "deal risk summary", "board presentation M&A",
  "legal DD memo", "red flag report", "deal-breaker analysis", "negotiation leverage DD",
  "closing conditions", "post-closing integration risk", or "diligence executive summary".
  Jurisdiction-agnostic with markers for US, UK, and EU variants.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode Due Diligence Report

> **Disclaimer**: This skill provides a framework for AI-assisted structuring of legal due
> diligence findings. It does not constitute legal advice. All outputs should be reviewed by
> qualified legal counsel licensed in the relevant jurisdiction(s) before use in any
> transaction. Laws and regulations change; verify current applicability before relying on
> any provision described here. Statutory and case law references cited from memory carry
> hallucination risk — verify against authoritative sources before relying on them. Due
> diligence findings require professional judgment to assess materiality and deal impact.
> No AI tool replaces experienced M&A counsel.

## Purpose and Scope

This skill transforms raw due diligence findings — gathered via checklists, data room
review, interviews, and workstream reports — into executive-ready, audience-differentiated
reports that drive deal decisions.

**Covers:**
- Aggregation and classification of findings across all 12 legal due diligence workstreams
- Three-tier severity classification: PASS / FLAG / DEAL-BREAKER
- Audience-specific report generation: board/executive, legal/counsel, commercial/deal team
- Risk heat map: probability × business impact matrix for visual deal-health assessment
- Negotiation leverage points: what each finding justifies asking for
- Closing conditions: which issues must be resolved before closing
- Post-closing integration risks: what needs attention after the transaction closes
- Rep & warranty analysis: how findings map to representations and warranties
- Remediation paths: what fixes each flagged issue, who owns it, and by when
- Quality-verified output with Glass Box audit trail

**Does not:**
- Generate the due diligence checklist (see `legalcode-ma-due-diligence-checklist`)
- Review individual contracts clause by clause (see `legalcode-contract-review`)
- Conduct financial or commercial due diligence (financial modeling, market analysis)
- Provide legal advice or replace qualified M&A counsel
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers

**Related skills:**
- `legalcode-ma-due-diligence-checklist` — generates the request list; this skill compiles
  the findings
- `legalcode-contract-review` — deep clause-level analysis for material contracts
- `legalcode-legal-risk-assessment` — enterprise-wide legal risk evaluation
- `legalcode-obligation-tracker` — tracks post-closing obligations and integration tasks

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill designed for cross-border M&A transactions. Findings
and report structure apply across legal systems; jurisdiction-specific content is flagged.

[JURISDICTION-SPECIFIC] Research and apply when localizing:

**United States:**
- Representations and warranties insurance (RWI) underwriting standards and materiality thresholds
- HSR Act pre-merger notification obligations (2026 threshold: USD 133.9M)
- CFIUS review triggers for national security implications
- Delaware corporate law (fiduciary duties, merger mechanics, appraisal rights)
- Material Adverse Effect (MAE) definition scope and carve-outs
- Disclosure schedule standards and bring-down mechanics
- Rep & warranty insurance gap between signing and closing

**United Kingdom:**
- Disclosure letter structure (general vs. specific disclosures; fair disclosure standard)
- Locked box vs. completion accounts mechanism; leakage protection
- Warranty and indemnity (W&I) insurance underwriting standards
- CMA merger control regime
- NSIA 2021 mandatory filing requirements for specified sectors
- TUPE obligations for asset purchases
- Companies Act 2006 financial assistance restrictions

**European Union:**
- EU Merger Regulation (EUMR) notification thresholds and Phase I/II timelines
- FDI screening obligations (25+ member state regimes; approximately 3,100 filings in 2024)
- Works council consultation requirements (EU Directive 2009/38) and timeline impact
- GDPR cross-border transfer and processor compliance
- EU AI Act compliance for high-risk AI systems in the target's products
- Foreign Subsidies Regulation (FSR) — financial contributions from non-EU states

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the direction or depth of the analysis
- Multiple valid approaches exist and user preference matters
- Business context is needed to classify finding severity correctly
- Scope choices significantly affect output length or detail

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

Accept findings in any of these formats:

- **Workstream reports**: One or more due diligence workstream reports from the deal team
- **Findings register**: A raw list or spreadsheet of open issues and red flags
- **Data room notes**: Annotated notes from document review
- **Summary email or memo**: Informal summary of key issues for structuring
- **Existing DD report**: A prior draft or competitor firm's report to supplement or replace

If no findings are provided, prompt the user: "Please share the due diligence findings —
this can be a list of issues, workstream reports, or a draft memo. I will structure them
into an executive-ready report."

If using this skill alongside `legalcode-ma-due-diligence-checklist`, accept the completed
checklist with red flags populated as the primary input.

### Step 2: Gather Context

**⟁ CLARIFY** — Before structuring the report, ask the user:

1. **Audience mix**: Which report formats are needed?
   - Options: Board/executive only, Legal/counsel only, Commercial/deal team only,
     All three formats, Board + Legal (most common)
   - *Why this matters*: Determines depth, terminology, and structure of each output
     section. A board report is 2-3 pages; a legal report may be 20+ pages.

2. **Investigation scope**: What level of coverage is required?
   - Options: Full scope (all findings, all workstreams), Critical-issues-only (DEAL-BREAKER
     and FLAG items; skip PASS), Red-flag-only (DEAL-BREAKER items only)
   - *Why this matters*: Affects report length and whether lower-risk findings are surfaced.

3. **Materiality threshold**: At what level does a finding become material?
   - Options: Conservative (flag anything above 1% of deal value), Standard (flag anything
     above 5% of deal value), Pragmatic (flag only issues affecting deal structure or closing),
     Provide specific threshold
   - *Why this matters*: Determines how many FLAG items to surface vs. background-note.

4. **Risk appetite**: How should borderline classifications be handled?
   - Options: Conservative (escalate borderline items to the higher tier), Balanced (classify
     at face value with explicit caveats), Pragmatic (classify at lower tier with mitigation)
   - *Why this matters*: A conservative buyer in a competitive auction needs different
     treatment than a strategic acquirer with a long diligence timeline.

**Defaults for non-interactive use**: Board + Legal; Critical-issues-only; Standard (5%);
Balanced.

### Step 3: Load Deal Context

Before structuring findings, gather deal-level context to calibrate the report:

1. **Transaction basics**: Target name, transaction structure (stock vs. asset), deal value
   (if available), governing law jurisdiction, expected closing timeline, stage (early
   diligence, confirmatory, pre-signing, pre-closing).

2. **Letter of intent or term sheet**: If available, review key deal terms — purchase price,
   representations and warranties scope, indemnification cap and basket, escrow amount and
   period, closing conditions. Use these as the reference point for "what the current deal
   structure already addresses."

3. **Deal playbook**: Check for an organization-specific deal playbook (e.g., standard
   indemnification expectations, known deal-breaker thresholds, required closing conditions).

   **⟁ CLARIFY** — If no playbook exists, ask:
   - **Option A: Define key thresholds now** — Walk through: minimum indemnification cap,
     maximum escrow exposure, required closing conditions, known deal-breaker categories.
   - **Option B: Proceed with market standards** — Use market-standard thresholds for the
     deal size and structure.

4. **Outstanding diligence gaps**: Identify which workstreams are incomplete or which
   documents have not yet been received. These are reported as **OPEN ITEMS** in the
   report — not as PASS, FLAG, or DEAL-BREAKER — to distinguish "no issues found" from
   "not yet reviewed."

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Identify the target's primary operating jurisdictions and the deal's governing law. Use
**legalcode-mcp** to gather legal authority relevant to the flagged findings.

**Research process:**
1. For each DEAL-BREAKER and major FLAG finding, identify the legal basis for the risk
   assessment (statute, regulation, case law principle).
2. Search legalcode-mcp for jurisdiction-relevant authority, focusing on:
   - Regulatory approval requirements and timelines for the deal
   - Employment law implications (TUPE, WARN, works council consultation)
   - IP ownership and chain-of-title requirements
   - Enforceability of non-competes and non-solicits in the target's jurisdictions
   - Environmental liability standards and successor liability rules
   - Tax indemnity standards and indemnification trigger events
3. Save results to `/tmp/legalcode-dd-authority.md`
4. Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box.

**If legalcode-mcp is not connected:** Mark all statutory citations with [VERIFY].
Note in the Glass Box: `legalcode_mcp: "Not connected — manual verification required"`.

### Step 5: Classify Findings

Apply the **Three-Tier Classification System** to each finding. For each, identify the
tier and — for FLAG items — the remediation sub-type.

**Classification rule:** Read the entire set of findings before classifying any single
item. Findings interact: a manageable FLAG item may become a DEAL-BREAKER when combined
with others in the same workstream, or a seeming DEAL-BREAKER may be downgraded to FLAG
once a specific indemnity is confirmed.

**⟁ CLARIFY** — For borderline classifications, ask rather than assume:

- **FLAG vs. DEAL-BREAKER**: "The target has two pending litigation matters with aggregate
  exposure of approximately USD 12M. Against a USD 200M deal, this is 6% of value — above
  the 5% materiality threshold. Should I classify this as a DEAL-BREAKER requiring pre-
  closing resolution, or a FLAG requiring indemnity escrow?" [Present deal context.]
- **OPEN ITEM vs. FLAG**: "We have not yet received the environmental assessment for the
  Ohio facility. Should I flag this as an OPEN ITEM (incomplete diligence) or treat the
  absence of information as a FLAG given the industrial nature of the site?"

See the **Finding Severity Classification** section below for full definitions and examples.

### Step 6: Build the Findings Register

Create the master findings register — the backbone of all three audience-specific reports.
Each finding should capture:

| Field | Content |
|-------|---------|
| **ID** | Sequential reference (e.g., F-001) |
| **Workstream** | Legal domain (e.g., IP, Litigation, Employment) |
| **Finding** | One-sentence description of the issue |
| **Severity** | PASS / FLAG [sub-type] / DEAL-BREAKER |
| **Evidence** | Source documents or data room references |
| **Business impact** | Quantified or described impact on deal value or operations |
| **Legal basis** | Statute, regulation, or principle — or "General commercial practice" |
| **Confidence** | 0.00-1.00 score with level label |
| **Negotiation lever** | What this finding justifies asking for |
| **Remediation path** | What resolves this issue (pre- or post-close) |
| **Owner** | Who should resolve it (seller, buyer, legal counsel, regulator) |
| **Deadline** | Before signing, before closing, or post-close with timing |
| **Status** | Open / Under Negotiation / Resolved / Accepted as-is |

### Step 7: Generate the Risk Heat Map

Plot findings on a 2D heat map: **Probability of Loss** (x-axis: Low / Medium / High) ×
**Business Impact** (y-axis: Low / Material / Severe). Use this matrix to:

- Identify the highest-priority findings at a glance
- Show the board the deal's overall risk density
- Flag any quadrant clustering (e.g., multiple High-Probability + Severe-Impact findings
  in the Regulatory workstream signal a sector-specific risk concentration)

```
Risk Heat Map Template:

            Low Impact  |  Material Impact  |  Severe Impact
            ─────────────────────────────────────────────────
High Prob.  YELLOW Zone |   ORANGE Zone     |    RED Zone
Med Prob.   GREEN Zone  |   YELLOW Zone     |    ORANGE Zone
Low Prob.   GREEN Zone  |   GREEN Zone      |    YELLOW Zone

Plot each finding: [F-001: Litigation exposure] → (High Prob., Material Impact) → ORANGE
```

For each zone:
- **RED Zone**: DEAL-BREAKER escalation required; present to board immediately
- **ORANGE Zone**: FLAG requiring deal structure adjustment; include in negotiation leverage
- **YELLOW Zone**: FLAG for monitoring or disclosure schedule; note in legal report
- **GREEN Zone**: PASS; document and move on

### Step 8: Identify Negotiation Leverage Points

For each FLAG and DEAL-BREAKER finding, identify what the finding justifies requesting
in the deal structure:

| Finding | Negotiation Lever | Specifics |
|---------|------------------|-----------|
| Pension underfunding | Price reduction | Quantify unfunded liability; reduce price by actuarial shortfall |
| Pending litigation (USD X) | Indemnity escrow | Seller escrow at least 1.5× the claimed exposure |
| Non-transferable software licenses | Closing condition | Seller must obtain third-party consents before closing |
| Environmental contamination | Specific indemnity | Unlimited-duration indemnity for pre-close contamination |
| Key executive no non-compete | Closing condition or earnout | Seller obtains enforceable restrictive covenants at close |
| Customer concentration (1 customer = 40% revenue) | Price adjustment or earnout | Earnout tied to customer retention post-close |
| Outstanding tax audit | Indemnity escrow | Tax escrow until audit resolved; buyer controls audit cooperation |

**Negotiation priority tiering:**

- **Tier 1 — Must-Haves (Walk-Away Conditions)**: Issues where the deal cannot proceed
  without resolution. No equivalent trade can compensate for this risk.
- **Tier 2 — Required Structural Adjustments**: Issues that must be addressed through
  deal mechanics (price, escrow, indemnity, closing condition). Proceed only if addressed.
- **Tier 3 — Preferred Positions (Concession Candidates)**: Issues worth raising but
  negotiable; can be conceded in exchange for Tier 1/2 wins.

**Negotiation sequencing**: Lead with Tier 1 items. Use Tier 3 concessions to secure
Tier 2 wins. Never trade on Tier 1 without executive escalation.

### Step 9: Assess Post-Closing Integration Risks

Beyond findings that affect closing, assess what happens **after** the deal closes.
Integration risks are distinct from legal DD risks — they arise from the friction between
two organizations merging.

**Key integration risk categories:**

| Category | Specific Risk | Early Warning Signs | Day 1 Readiness |
|----------|--------------|---------------------|-----------------|
| Contract continuity | Customer/supplier change-of-control consents not obtained | More than 10% of revenue under contracts with COC clauses | Consent tracker; fallback plans |
| Employment | Key employee flight risk post-announcement | Equity acceleration, no retention agreements, market demand | Retention packages; communication plan |
| Regulatory | License transfers or new applications required | Licenses tied to current ownership structure | Pre-closing regulatory meetings |
| Technology | Systems incompatibility (ERP, CRM, security) | Multiple legacy platforms; no API documentation | Integration timeline; IT workstream |
| IP | Ownership disputes, missing registrations | Informal IP practices; open-source policy gaps | IP audit; clean-up assignments |
| Data | GDPR/privacy notification requirements post-close | Joint controller issues; consent-based processing | Privacy counsel review; Day 1 notice |
| Compliance | Successor liability for pre-close violations | Ongoing investigations, consent decrees | Compliance monitoring plan |

**⟁ CLARIFY** — If the transaction involves significant post-closing integration complexity
(e.g., cross-border merger, carve-out from a larger entity, regulated industry), ask:

- "Should I include a detailed Day 1 readiness checklist as an appendix to the legal report?"
- "Is there a specific integration workstream that concerns the deal team most?"

### Step 10: Quality Verification

Before generating audience-specific reports, run the full quality framework.

1. **Citation Quality Gates** (see Quality Assurance Framework below) — run silently.
   Revise any gate failures before delivery.

2. **Self-Interrogation** (3-pass) — for every DEAL-BREAKER finding, apply the
   Self-Interrogation. Mark each as PASS or REVISED in the audit trail.

3. **Confidence Scoring** — assign a confidence level to every material finding (FLAG or
   DEAL-BREAKER). Do not express certainty on Possible or Unlikely findings without flagging.

4. **Completeness check**: Confirm all 12 DD workstreams are addressed — either with
   findings, PASS status, or an explicit OPEN ITEM note. A workstream absent from the
   report is ambiguous — always state its status.

5. **Internal consistency**: Verify that no finding classified as PASS elsewhere in the
   report creates a contradiction with a FLAG or DEAL-BREAKER. Cross-reference related
   findings (e.g., a PASS on the employment workstream is inconsistent with a DEAL-BREAKER
   involving a key executive's restrictive covenant).

### Step 11: Generate Audience-Specific Reports

Using the findings register, risk heat map, negotiation leverage table, and integration
risk assessment, generate the requested audience-specific reports.

See the **Output Format Templates** section for the complete structure of each report.

For each report:
- Write in the appropriate register (board = strategic narrative; legal = precise and
  citation-dense; commercial = action-oriented and deal-focused)
- Apply the **Writing Standards** section
- Apply confidence qualifiers to every material claim
- Append the Glass Box Audit Trail to the legal report

**⟁ CLARIFY** — If generating the board report, ask before finalizing the recommendation:

- "Is this a competitive process or exclusive negotiation? This affects whether a DEAL-BREAKER
  triggers a walk-away recommendation or a re-bid strategy."
- "Has the board set a maximum risk tolerance for this deal? I can calibrate the
  recommendation to a defined threshold."

### Step 12: Deliver

Deliver the reports in the requested formats. Clearly label each section with its intended
audience. Append a summary of OPEN ITEMS (unresolved diligence questions) and recommended
next steps with owners and deadlines.

---

## Finding Severity Classification

### PASS — No Material Issues

No material issues found in this workstream or on this specific finding. Proceed without
structural adjustment to the deal.

**Examples:**
- IP ownership is clean; all registered IP is in the target's name with no gaps or third-
  party claims
- Employment practices are compliant; no material pending claims
- All material contracts are assignable or transferable without third-party consent

**Action**: Note for awareness. Include in legal report for completeness. Not included in
board report unless the workstream had initial concerns that were resolved.

---

### FLAG — Issues Present; Addressable Through Deal Structure

Issues present but can be addressed through one or more of the following mechanisms.
Use the sub-type label to indicate which mechanism applies.

| Sub-Type | Mechanism | When to Use |
|----------|-----------|-------------|
| **FLAG [PRICE]** | Purchase price reduction | Quantifiable liabilities or value impairment |
| **FLAG [INDEMNITY]** | Specific indemnity provision | Contingent liabilities with uncertain timing |
| **FLAG [ESCROW]** | Retention from purchase price in escrow | Exposures resolvable within 12-24 months |
| **FLAG [CONDITION]** | Closing condition (must be resolved pre-close) | Issues where certainty is required before proceeding |
| **FLAG [POST-CLOSE]** | Post-closing remediation or integration action | Issues addressable after closing without deal risk |
| **FLAG [DISCLOSURE]** | Disclosure schedule exception | Known issue already reflected in reps; seller discloses |

**Examples:**
- Pending tax audit with estimated exposure of USD 2M on a USD 100M deal →
  FLAG [ESCROW] — tax-specific escrow of USD 3M with audit cooperation
- Software licenses not assignable without third-party consent →
  FLAG [CONDITION] — seller obtains consent before closing
- Environmental Phase I recommended; Phase II not yet complete →
  FLAG [POST-CLOSE] — buyer commissions Phase II with seller indemnity for pre-close issues

**Action**: Include in legal report and board report (material FLAGs). Generate specific
negotiation lever for each. Include in remediation tracker with owner and deadline.

---

### DEAL-BREAKER — Cannot Proceed Without Resolution

Issues that cannot be adequately addressed within the current deal structure. These issues
either (a) cannot be resolved by deal mechanics, (b) create regulatory or legal barriers
to closing, or (c) fundamentally undermine the investment thesis.

**Examples:**
- Active government investigation for securities fraud with no resolution timeline
- Core IP that the target does not own and cannot acquire; IP forms the basis of the deal
- HSR or CMA merger control concern that is likely to result in a prohibition or require
  a major divestiture
- Regulatory license that is not transferable and cannot be re-applied for (e.g., banking
  license, FCC license) and is essential to the target's business
- Financial statements found to be materially misstated with no adequate explanation

**Action**: Escalate immediately to deal team and executive leadership. Present in board
report with specific walk-away analysis. Legal team to assess remediation feasibility. Do
not proceed to signing without explicit resolution strategy.

---

## Workstream Reference

Apply this framework across all 12 legal due diligence workstreams. For each workstream,
identify findings, classify them, and apply the Finding Severity Classification.

| # | Workstream | Key Risk Areas | Common FLAG Items | Common DEAL-BREAKER Items |
|---|-----------|---------------|-------------------|--------------------------|
| 1 | Corporate Structure | Ownership chain, authority, encumbrances | Missing board resolutions, undisclosed liens | Fraud, phantom shares, ownership disputes |
| 2 | Material Contracts | Assignment, COC clauses, key relationships | Non-assignable contracts (< 20% revenue) | Non-assignable contracts (> 40% revenue) with no consent mechanism |
| 3 | Intellectual Property | Ownership, registration, open source | Unregistered trademarks, assignment gaps | Core IP not owned; fundamental freedom-to-operate issue |
| 4 | Litigation | Pending claims, regulatory enforcement | Quantifiable pending claims | Active government investigation; class action; uninsured liability |
| 5 | Employment & Labor | Key persons, compensation, compliance | Underfunded pension, misclassified contractors | Works council blocking transaction; mandatory benefit plan wind-up |
| 6 | Regulatory & Compliance | Licenses, permits, investigations | Non-transferable secondary licenses | Non-transferable primary license; material enforcement action |
| 7 | Real Estate | Leases, COC consents, environmental | Lease COC clauses requiring consent | No consents obtainable for key facilities; EPA Superfund PRP status |
| 8 | Environmental | Contamination, compliance, liability | Phase I concerns; prior incidents | Known contamination without remediation; CERCLA PRP status |
| 9 | Tax | Open audits, attributes, structure | State nexus gaps, open audit < 5% | Tax fraud; structure that cannot close without major restructuring |
| 10 | Data Privacy & Cybersecurity | GDPR, CCPA, data breaches | Prior breach (notified); consent gaps | Undisclosed material breach; massive PHI exposure without HIPAA compliance |
| 11 | Antitrust & FDI | Merger control, foreign investment | Uncertain CFIUS timeline | EUMR Phase II; FDI prohibition risk; national security screening |
| 12 | Insurance | Coverage adequacy, claims history | Coverage gaps in D&O, cyber | Uninsured catastrophic loss in litigation; no D&O coverage |

[JURISDICTION-SPECIFIC] Workstream 5 (Employment): Applies TUPE (UK), WARN Act (US),
and works council consultation rights (EU) with different timelines and deal impact.

[JURISDICTION-SPECIFIC] Workstream 11 (Antitrust): HSR notification (US), CMA and
NSIA (UK), EUMR + national FDI regimes (EU) — all have different timelines and
evidentiary standards.

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Identify transaction structure, target jurisdictions, deal context, and risk
appetite. Classify complexity (straightforward domestic, cross-border, regulated industry,
distressed asset). Identify which workstreams are complete and which have open gaps.

**DO**: Execute finding classification, build the findings register, generate the heat map,
identify negotiation leverage, and assess integration risks.

**CHECK**: Run Citation Quality Gates. For DEAL-BREAKER items, run Self-Interrogation.
Verify all workstreams are addressed. Check internal consistency.

**ACT**: Note any patterns in findings (e.g., systemic compliance culture issues, recurring
IP governance gaps) that suggest broader organizational risk beyond individual findings.

---

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise failures before delivery.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every legal risk claim cites a specific statute, regulation, principle, or document | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format** | All citations follow consistent, recognizable format for the jurisdiction | Fix format |
| **Currency** | Every cited provision checked for amendments or repeal | Flag "[CHECK CURRENCY]" |
| **Domain** | Analysis stays within the deal's applicable jurisdictions; no cross-jurisdiction bleed | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated; not hidden beneath confident-sounding language | Add confidence qualifier; downgrade claim level |

---

### Self-Interrogation for DEAL-BREAKER Items

For any finding classified as DEAL-BREAKER, apply this 3-pass self-interrogation:

**Pass 1 — Legal Chain Integrity**:
- Does the risk assessment follow logically from the statute, regulation, or contractual
  provision cited?
- Would a regulator or court in this jurisdiction actually reach this conclusion on these
  facts?
- Is there a reasonable counter-argument that counsel for the other side will make?

**Pass 2 — Completeness**:
- Have all relevant statutes, regulations, and cases been considered?
- Are there deal mechanics (indemnity, specific escrow, price adjustment, condition) that
  could adequately address this issue?
- Are there regulatory pathways (no-action letter, pre-closing consent, waiver) that could
  resolve the issue?

**Pass 3 — Challenge**:
- What is the strongest argument that this finding is a FLAG, not a DEAL-BREAKER?
- Under what circumstances (e.g., different deal structure, pre-closing remediation,
  risk-acceptance by board) might a reasonable acquirer proceed?
- Is the DEAL-BREAKER classification proportionate, or does it reflect excessive caution
  that a pragmatic M&A team would override?

Mark the audit trail: `self_interrogation: PASS` or `self_interrogation: REVISED`.

---

### Confidence Scoring

Assign a confidence level to every material finding (FLAG or DEAL-BREAKER):

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95-1.0 | Clear legal rule, strong evidence, no reasonable counter | State with confidence |
| **High** | 0.80-0.94 | Strong authority, minor factual or legal questions | State with brief caveat |
| **Probable** | 0.60-0.79 | Good arguments; reasonable minds could differ | State with reasoning and contra-indicators |
| **Possible** | 0.40-0.59 | Material uncertainty; competing interpretations | Flag for counsel review with both sides |
| **Unlikely** | 0.0-0.39 | Weak evidentiary or legal basis | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

**Calibration rule for M&A DD**: Given the consequential nature of deal decisions,
err toward flagging uncertainty rather than hiding it. A "Probable" finding presented as
"Definite" can cause a board to decline a viable deal or proceed into a real DEAL-BREAKER.

---

## Glass Box Audit Trail

Every legal due diligence report MUST include a Glass Box audit section. Append to the
legal/counsel report (not the board executive summary, which is for non-technical readers).

```yaml
glass_box:
  skill_name: "legalcode-due-diligence-report"
  transaction: "[Target company name and deal code]"
  transaction_type: "[Stock purchase / Asset purchase / Merger / JV / Carve-out]"
  deal_value: "[If disclosed; 'Undisclosed' if not]"
  governing_law: "[Primary jurisdiction(s)]"
  target_jurisdictions: "[Countries where target operates]"
  diligence_stage: "[Early / Confirmatory / Pre-signing / Pre-closing]"
  workstreams_reviewed: "[number out of 12]"
  workstreams_open: "[number] — [list workstream names]"
  findings_total: "[total]"
  deal_breakers: "[count]"
  flags: "[count by sub-type: PRICE x, INDEMNITY x, ESCROW x, CONDITION x, POST-CLOSE x, DISCLOSURE x]"
  pass_items: "[count]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation:
    deal_breakers_reviewed: "[count]"
    result: "PASS / REVISED — [summary of any revisions]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  playbook_used: "[Playbook name or 'Market standards applied']"
  assumptions:
    - "[Any assumptions made in absence of complete information]"
  limitations:
    - "[Any scope limitations, gaps, or caveats]"
  reviewer: "AI-assisted — requires review by qualified M&A counsel"
```

---

## Multi-Stakeholder Mapping

For every transaction, identify all parties affected by diligence findings beyond the
buyer and seller:

| Stakeholder | Role | Affected Workstreams | Impact | Action Required |
|-------------|------|---------------------|--------|-----------------|
| Target employees | Third party | Employment | Potential redundancy, change of terms | TUPE/WARN notice; retention packages |
| Material customers | Third party | Contracts | COC termination rights | Consent campaign; relationship management |
| Key suppliers | Third party | Contracts | Supply continuity risk | COC consent; supply alternatives |
| Regulators | Regulator | Regulatory, antitrust, environmental | Approval/notification obligations | Filing strategy; regulatory counsel |
| Data subjects | Third party | Data privacy | Privacy rights in acquisition | GDPR transparency; notification |
| Lenders | Financial | Corporate structure | Consent to assignment of finance docs | Lender consent; change of control |
| Works council | Representative body | Employment (EU) | Consultation right before closing | Initiate consultation; timeline planning |

---

## Anti-Patterns

Explicit catalogue of what NOT to do when generating due diligence reports:

1. **Reporting raw findings without deal context** — A finding is not a material finding
   unless its impact on the deal is articulated. "The target has 14 pending employment
   claims" is useless without: aggregate exposure, deal value percentage, insurance
   coverage, and historical pattern analysis.

2. **Treating OPEN ITEMS as PASS** — If a workstream is incomplete (documents not received,
   counsel not engaged, Phase II not completed), it is an OPEN ITEM — not a clean bill of
   health. Distinguishing "no issues found" from "not yet reviewed" is a fundamental
   accuracy obligation.

3. **Classifying findings in isolation** — Findings interact. A FLAG in litigation and a
   FLAG in employment and a FLAG in regulatory all touching the same underlying compliance
   failure may collectively constitute a DEAL-BREAKER, even if each is acceptable alone.
   Always read the full findings register before classifying.

4. **Confidence without evidence** — "The target's IP ownership is clean" asserted without
   a chain-of-title review, inventor assignment checks, and open-source policy analysis is
   false certainty. Every PASS classification should rest on reviewed evidence.

5. **Omitting remediation paths** — A FLAG finding without a remediation path is only half
   useful. Counsel needs to know: what fixes this, who owns the fix, when it must happen,
   and what happens if it is not fixed by closing.

6. **One-format-fits-all output** — A report written for legal counsel is inaccessible to
   a board. A report written for a board is legally imprecise. Audience differentiation is
   not a luxury; it is a prerequisite for the report to serve its purpose.

7. **Ignoring post-closing integration risks** — Legal due diligence traditionally stops
   at closing. But license non-transferability, customer consent failures, and data
   migration obligations create real Day 1 operational risks. Integration risk belongs in
   the report.

8. **Missing negotiation leverage** — Each FLAG finding represents a negotiation lever:
   a price reduction, an indemnity, an escrow, a closing condition. Failing to translate
   findings into leverage leaves value on the table.

9. **Skipping the heat map for complex deals** — In a transaction with 30+ findings across
   12 workstreams, no board or deal team can evaluate risk without a visual prioritization
   tool. The heat map is not optional; it is the executive communication tool.

10. **Treating jurisdiction-specific rules as universal** — TUPE applies in the UK but not
    the US. HSR does not apply below threshold. Works council consultation is required in
    the EU but not in most common law jurisdictions. Importing jurisdiction-specific concepts
    into a general analysis is a material error.

11. **Hiding uncertainty in confident-sounding prose** — "The target's compliance program
    appears adequate" is imprecise if the compliance program was not reviewed. Say what was
    reviewed, what was not, and what the confidence level is. Uncertainty disclosed is a
    quality signal; uncertainty hidden is a liability.

12. **Allowing diligence gaps to extend indefinitely** — Every OPEN ITEM should carry a
    deadline and an escalation path. If the seller cannot produce a document by a defined
    date, that is itself a FLAG — either because the document does not exist or because the
    seller is withholding.

13. **Presenting findings without validating the deal thesis** — The purpose of DD is to
    test the investment thesis. If the deal was premised on the target's IP portfolio, clean
    IP is a PASS and should be called out as validating the thesis — not merely noted. The
    report should connect findings to the deal rationale.

14. **Over-engineering DEAL-BREAKER classifications** — Not every uncomfortable finding is a
    DEAL-BREAKER. If every finding escalates to the highest severity, the board cannot
    distinguish genuine blockers from routine negotiation items. The DEAL-BREAKER tier must
    be reserved for genuine walk-away conditions.

15. **Forgetting the disclosure schedule implication** — In a US or UK deal, every FLAG
    finding has a disclosure schedule dimension: Does the seller need to disclose this? Is
    the rep already qualified? Does the finding fall within a disclosure exception? Missing
    this step creates warranty claim exposure for both parties.

---

## Writing Standards

Apply plain-language discipline to all report sections:

**For board/executive summaries** (read by non-lawyers):
- Maximum 3 sentences per finding. Name the risk, quantify it if possible, state the
  recommended action.
- Active voice: "The target owes USD 4M in unpaid sales tax" — not "Sales tax obligations
  have been identified that may amount to approximately USD 4M."
- No legal jargon. Use "non-compete agreement" not "restrictive covenant"; use "government
  investigation" not "CID."
- Recommendation before detail: lead with the action, then the evidence.

**For legal reports** (read by M&A counsel):
- Technical precision: cite statutes and provisions; use jurisdiction-correct terminology.
- Active voice still applies.
- Confidence qualifiers required: state the legal basis and qualify uncertainty explicitly.
- Cite the source document (data room reference, clause number) for every finding.

**For commercial reports** (read by deal team and business stakeholders):
- Business impact-first: open with what the finding means for the deal, revenue, or
  operations — then explain the legal basis.
- Translate risk into dollars where possible.
- Prioritize by deal impact, not by workstream.

**Quality gates before delivery:**
1. Can a non-lawyer board member understand the executive summary and make a decision?
2. Can M&A counsel use the legal report to draft representations, indemnities, and
   closing conditions?
3. Is every legal claim backed by a specific citation or document reference (or flagged [VERIFY])?
4. Are any phrases vague, hedging, or ambiguous? Fix them.
5. Is every OPEN ITEM distinguished from a PASS?
6. Does every FLAG item have a negotiation lever and a remediation path?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected:**
- In Step 4, search for regulatory requirements, merger control thresholds, employment law,
  and enforcement precedents in the target's operating jurisdictions
- Save results to `/tmp/legalcode-dd-authority.md`
- Use verified authority to support or challenge DEAL-BREAKER classifications
- Check currency of regulatory thresholds (e.g., HSR, EUMR notification values change annually)
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**
- Mark all statutory citations with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Focus the report on commercial risk assessment and deal structure recommendations
  rather than specific legal citations
- Recommend that counsel verify all regulatory requirements and statutory bases before
  the report is finalized

---

## Output Format Templates

### Format A: Board / Executive Summary

Target length: 2-4 pages. Audience: board members, senior leadership, investment committee.

```markdown
# Due Diligence Executive Summary — [Target Name]

**Transaction**: [Deal code or descriptor]
**Structure**: [Stock purchase / Asset purchase / Merger]
**Deal Value**: [Amount or Undisclosed]
**Governing Law**: [Jurisdiction]
**Report Date**: [Date]
**Stage**: [Pre-signing / Pre-closing / Confirmatory]
**Prepared By**: [Deal team / Legal counsel]

---

## Overall Deal Health

**Recommendation**: [PROCEED / PROCEED WITH CONDITIONS / PAUSE / DO NOT PROCEED]
**Confidence**: [Level — rationale in one sentence]

[Two-sentence summary of overall diligence findings.]

---

## Risk Heat Map

[2D grid: Probability × Impact, with findings plotted by ID]

| Zone | Findings Count | Action |
|------|---------------|--------|
| RED (High Prob. × Severe Impact) | [n] | Escalate — DEAL-BREAKERs |
| ORANGE (High/Med × Material) | [n] | Address in deal structure |
| YELLOW (Med × Various) | [n] | Monitor; disclosure schedule |
| GREEN (Low × Low/Material) | [n] | Note; no action needed |

---

## Deal-Breaker Items

[List each DEAL-BREAKER with one-paragraph summary, evidence reference, and board options.]

### [Finding ID] — [One-line title]
**Risk**: [What the issue is, quantified where possible]
**Evidence**: [Document reference or interview source]
**Options for Board**:
  A. [Resolve pre-signing — how, timeline, cost]
  B. [Restructure deal to accommodate — how]
  C. [Walk away — rationale]

---

## Material Findings (FLAG Items)

[Top FLAG items — those material to deal value or structure. Group by workstream.]

| ID | Workstream | Finding | Severity Sub-Type | Negotiation Lever | Status |
|----|-----------|---------|-------------------|-------------------|--------|
| F-001 | [WS] | [Finding] | FLAG [CONDITION] | [What to request] | Open |

---

## Open Items

[List workstreams or specific documents where diligence is incomplete.]

| Workstream | What Is Missing | Deadline | Risk If Not Resolved |
|-----------|----------------|----------|---------------------|
| [WS] | [Document/analysis] | [Date] | [Conservative risk assessment] |

---

## Recommended Closing Conditions

[Conditions the board should require before authorizing closing.]

1. [Condition and rationale]
2. [Condition and rationale]

---

## Next Steps

| Action | Owner | Deadline |
|--------|-------|---------|
| [Action] | [Owner] | [Date] |
```

---

### Format B: Legal / Counsel Report

Target length: 10-30 pages. Audience: M&A counsel, outside counsel, legal team.

```markdown
# Legal Due Diligence Report — [Target Name]

**Transaction**: [Deal code]
**Governing Law**: [Jurisdiction]
**Report Date**: [Date]
**Stage**: [Stage]
**Prepared By**: [Counsel]
**Review Basis**: [Playbook / Market standards]

---

## Scope of Review

[Workstreams reviewed; documents and data room folders accessed; diligence period;
 limitations on scope; outstanding requests]

---

## Summary of Findings

[Table: All findings by ID, workstream, severity, confidence, status]

---

## Findings by Workstream

### Workstream [N]: [Name]

#### [Finding ID] — [Severity] | Confidence: [Level]

**Finding**: [Precise legal description]
**Evidence**: [Data room reference, document name, clause number]
**Legal Basis**: [Statute, regulation, case, principle — or "General commercial practice"]
**Business Impact**: [Quantified or described]
**Negotiation Lever**: [Specific ask — price, indemnity, escrow, condition, disclosure]
**Remediation Path**: [What resolves this; pre- or post-close; owner; deadline]

[Repeat for all FLAG and DEAL-BREAKER items. Note PASS items in a table at the end of
the workstream section.]

---

## Representation & Warranty Analysis

[Map each FLAG and DEAL-BREAKER to the representations in the purchase agreement. Identify:
 (a) which rep covers the risk, (b) whether the rep is qualified adequately, (c) whether
 a disclosure schedule exception is appropriate or required.]

| Finding ID | Relevant Rep | Current Qualification | Gap | Recommended Fix |
|-----------|-------------|----------------------|-----|----------------|
| F-001 | Section [X] (Organization) | None | [Gap] | [Fix — specific language] |

---

## Closing Conditions Recommended

[List specific closing conditions, tied to finding IDs, with precedent language where available.]

---

## Post-Closing Integration Risks

[Legal risks that arise after closing — contract execution, regulatory reporting, compliance
 integration, data migration obligations, employment integration.]

---

## Open Items Register

[All outstanding diligence requests; status; risk if unresolved.]

---

## Glass Box Audit Trail

[YAML block per the Glass Box section above]
```

---

### Format C: Commercial / Deal Team Report

Target length: 3-6 pages. Audience: deal team, business development, investment team.

```markdown
# Commercial Due Diligence — Legal Risk Summary — [Target Name]

**Transaction**: [Deal code]
**Report Date**: [Date]
**Deal Value**: [Amount]

---

## What the Findings Mean for the Deal

[Narrative: How do the overall diligence findings affect the investment thesis? Are the
 core assumptions about the target (IP strength, revenue quality, growth potential)
 validated or challenged?]

---

## Negotiation Leverage Points

[What findings justify requesting — organized by leverage type.]

### Price Reduction Opportunities

| Finding | Estimated Value Impact | Negotiation Approach |
|---------|----------------------|---------------------|
| [Finding] | [USD amount or %] | [Specific ask] |

### Indemnity and Escrow Opportunities

| Finding | Recommended Provision | Escrow Amount / Period |
|---------|----------------------|----------------------|
| [Finding] | [Specific indemnity language] | [Amount / Period] |

### Closing Conditions

| Finding | Condition Required | Seller Action |
|---------|-------------------|--------------|
| [Finding] | [Specific condition] | [What seller must do] |

---

## Integration Risks to Manage Post-Closing

| Risk | Business Impact | Day 1 Action | Owner |
|------|----------------|-------------|-------|
| [Risk] | [Impact] | [Action] | [Owner] |

---

## Contingency Planning

[What to do if key issues remain unresolved at the time of signing:]
- If [DEAL-BREAKER finding] is not resolved: [Recommended response — walk-away threshold,
  alternative structure, price adjustment formula]
- If [FLAG finding] is not addressable in deal documents: [Minimum acceptable outcome]

---

## Recommended Negotiation Playbook

**Must-haves (Tier 1 — Walk-Away Conditions)**:
- [List with rationale]

**Required Structural Adjustments (Tier 2)**:
- [List with specific mechanics]

**Preferred Positions — Concession Candidates (Tier 3)**:
- [List — these can be traded for Tier 1/2 wins]
```

---

## Localization Notes

This skill is jurisdiction-agnostic. To create a jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with jurisdiction-specific legal content
2. Replace [VERIFY] tags with verified statutory references via legalcode-mcp
3. Add jurisdiction-specific workstream items (e.g., TUPE for UK, WARN for US, works
   council consultation for EU)
4. Add jurisdiction-specific regulatory approval timelines and risk thresholds
5. Update the frontmatter name and description to reference the specific jurisdiction

**US-specific additions**: HSR analysis, CFIUS screening, Delaware DGCL mechanics, state
Blue Sky laws, ERISA for pension plans, FCPA anti-corruption compliance.

**UK-specific additions**: NSIA 2021 mandatory filing for 17 sectors, CMA merger control,
disclosure letter structure, locked box vs. completion accounts, TUPE, Companies Act
financial assistance restrictions.

**EU-specific additions**: EUMR thresholds and Phase I/II timelines, FDI screening by
member state, works council consultation (Directive 2009/38), GDPR cross-border issues,
EU AI Act high-risk classification, Foreign Subsidies Regulation.

---

## Provenance

Created by Legalcode (2026-03-01). Original synthesis developed to fill the gap between
the `legalcode-ma-due-diligence-checklist` skill (which generates the request list) and
the need for structured executive-ready findings reports. Incorporates structural patterns
from `legalcode-contract-review` (quality frameworks, Glass Box, negotiation prioritization)
and `legalcode-early-case-assessment` (heat map, audience-differentiated output, integration
risk assessment). Legal substance informed by web research on US/UK/EU M&A practice,
including FDI screening developments (2024-2025), RWI underwriting trends, and disclosure
letter standards. Jurisdiction-agnostic with markers for US, UK, and EU.
