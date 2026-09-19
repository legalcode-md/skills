---
name: legalcode-corporate-restructuring
description: Comprehensive corporate restructuring analysis covering US Chapter 11 reorganization (automatic
  stay §362, DIP financing §364, Section 363 asset sales, cramdown §1129(b), executory contracts §365,
  avoidance actions §547-548, absolute priority rule, SBRA/Subchapter V small business track), UK administration
  and CVA (Insolvency Act 1986, Part 26A restructuring plans, cross-class cramdown, pre-pack administration
  SIP 16, schemes of arrangement), German Insolvenzverfahren and StaRUG (InsO, Eigenverwaltung, Schutzschirmverfahren,
  ESUG 2012, StaRUG 2021 preventive framework), out-of-court workouts (forbearance, standstill, intercreditor
  agreements, LSTA/LMA distressed trading), debt-for-equity swaps (COD income, IRC §382 NOL limitations,
  UK/DE tax rules), Section 363 sales (stalking horse, free and clear, bidding procedures), DIP financing
  (priming liens, roll-ups, milestones, loan-to-own), Assignment for Benefit of Creditors (ABC), receivership,
  and liability management exercises (uptier, exchange offers, co-ops).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Comprehensive corporate restructuring analysis covering US Chapter 11 reorganization (automatic stay §362, DIP financing §364, Section 363 asset sales, cramdown §1129(b), executory contracts §365, avoidance actions §547-548, absolute priority rule, SBRA/Subchapter V small business track), UK administration and CVA (Insolvency Act 1986, Part 26A restructuring plans, cross-class cramdown, pre-pack administration SIP 16, schemes of arrangement), German Insolvenzverfahren and StaRUG (InsO, Eigenverwaltung, Schutzschirmverfahren, ESUG 2012, StaRUG 2021 preventive framework), out-of-court workouts (forbearance, standstill, intercreditor agreements, LSTA/LMA distressed trading), debt-for-equity swaps (COD income, IRC §382 NOL limitations, UK/DE tax rules), Section 363 sales (stalking horse, free and clear, bidding procedures), DIP financing (priming liens, roll-ups, milestones, loan-to-own), Assignment for Benefit of Creditors (ABC), receivership, and liability management exercises (uptier, exchange offers, co-ops). Use when counsel, restructuring advisor, creditor, debtor, or investor needs to: analyze reorganization options across jurisdictions; evaluate DIP financing terms; assess cramdown viability; review intercreditor waterfall; map avoidance action exposure; compare pre-packaged vs. free-fall Chapter 11; navigate StaRUG vs. Insolvenzverfahren choice; evaluate UK restructuring plan fairness post-Petrofac/Saipem; assess out-of-court workout feasibility; or identify restructuring anti-patterns and tax traps. Also triggers on: preference window, fraudulent transfer lookback, absolute priority rule exception, new value exception, exclusivity period, plan of reorganization confirmation, adequate protection, cash collateral, credit bid, executory contract assumption/ rejection, preference settlement, § 502(b) claim objection, distressed M&A, liability management, equitization, Insolvenzplan, Eigenverwaltung, StaRUG plan, CVA moratorium, administration exit, scheme of arrangement jurisdictional competition.


# Legalcode Corporate Restructuring

> **Disclaimer**: This skill provides a framework for AI-assisted restructuring analysis. It does
> not constitute legal, financial, tax, or investment advice. Restructuring law is highly fact-
> specific, jurisdiction-sensitive, and subject to rapid change through case law, legislative
> reform, and market practice. All outputs must be reviewed by qualified restructuring counsel,
> financial advisors, and tax specialists licensed in the relevant jurisdiction before any reliance
> or action. Statutory citations are to provisions current as of early 2026 — verify current
> status. Nothing here constitutes an offer to buy or sell securities or a solicitation of any
> investment decision. AI analysis of restructuring scenarios requires independent expert
> verification, particularly on valuation, solvency, and plan feasibility.

---

## Purpose and Scope

This skill analyses corporate restructuring decisions end-to-end — from the initial choice of
forum and mechanism through plan confirmation, exit, or liquidation — across the three major
restructuring jurisdictions (US, UK, Germany) and key out-of-court tools.

**Covers:**

- US Chapter 11: voluntary petition, automatic stay, DIP financing, 363 sales, plan of
  reorganization, cramdown, avoidance actions, executory contracts, Subchapter V SBRA
- UK administration, CVA, Part 26A restructuring plans, schemes of arrangement, pre-pack
  administration, liquidation
- German Insolvenzverfahren, Eigenverwaltung, Schutzschirmverfahren, ESUG reforms, StaRUG
  preventive restructuring framework
- Out-of-court workouts: forbearance, standstill, intercreditor agreements, distressed debt
  exchanges, covenant waivers
- Debt-for-equity swaps: mechanics, valuation, COD tax treatment, holdout resolution
- Liability management exercises: uptier transactions, exchange offers, lender co-ops
- Receivership and Assignment for Benefit of Creditors (ABC)
- Cross-jurisdiction comparison and forum selection
- At least 20 named anti-patterns and common practitioner pitfalls

**Does not:**

- Provide legal, tax, or investment advice or replace qualified counsel
- Draft plans of reorganization, DIP credit agreements, or intercreditor agreements — those
  are drafting skills
- Perform independent valuation or solvency analysis
- Substitute for engagement of a financial advisor (investment banker, financial restructuring
  advisor) in live matters
- Constitute securities or insolvency practitioner advice regulated in any jurisdiction

**Relationship to other skills:**

| Task                            | Use This Skill  | Route To                               |
| ------------------------------- | --------------- | -------------------------------------- |
| Restructuring analysis          | ✅ This skill   | —                                      |
| Loan agreement review           | Cross-reference | `legalcode-loan-agreement-review`      |
| M&A due diligence (distressed)  | Cross-reference | `legalcode-ma-due-diligence-checklist` |
| Guaranty analysis               | Cross-reference | `legalcode-guaranty-agreement-review`  |
| Entity formation post-emergence | Cross-reference | `legalcode-entity-formation-advisor`   |

---

## Jurisdiction and Framework Coverage

| Track            | Primary Statute                                       | Key Tools                                                      | Court/Forum                                               |
| ---------------- | ----------------------------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------- |
| **US**           | 11 U.S.C. (Bankruptcy Code)                           | Chapter 11, §363 sale, DIP, Subchapter V                       | US Bankruptcy Courts (SDNY, D.Del. dominant)              |
| **UK**           | Insolvency Act 1986; Companies Act 2006 Part 26A      | Administration, CVA, Restructuring Plan, Scheme                | England & Wales High Court (ChD, Companies Court)         |
| **Germany**      | InsO (Insolvency Code); StaRUG 2021                   | Insolvenzverfahren, Eigenverwaltung, Schutzschirm, StaRUG plan | Local Insolvency Courts (Amtsgerichte); specialist courts |
| **Cross-border** | UNCITRAL Model Law; EU Insolvency Regulation 2015/848 | Chapter 15 recognition; COMI analysis; Galapagos race to court | Forum shopping; center of main interests                  |

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming intent,
the workflow pauses when:

- The answer would materially change the forum or mechanism recommendation
- Solvency status is ambiguous (affects StaRUG eligibility, ABC viability, cramdown standards)
- Creditor composition is unknown (secured vs. unsecured ratio changes options materially)
- Tax implications depend on facts not yet provided

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

- **Company profile**: Jurisdiction, capital structure, creditor composition, current liquidity,
  solvency status, strategic objective (reorganize vs. sell vs. wind down)
- **Document review**: DIP credit agreement, plan of reorganization, intercreditor agreement,
  forbearance agreement, CVA proposal, StaRUG plan — provided as file/URL/pasted text
- **Specific question**: "Should we file Chapter 11 or pursue an out-of-court workout?",
  "Can we cram down our senior lenders?", "Is our DIP roll-up defensible?", "How does
  StaRUG compare to Insolvenzverfahren?", "What are the tax traps in our debt-for-equity swap?"
- **Scenario analysis**: Compare mechanism options with risk/benefit analysis

### Step 2: Gather Context

**CLARIFY** — Before routing the analysis, ask (skip any already answered):

1. **Primary jurisdiction** — Where is the company incorporated and where are key operations/assets?
   - Options: United States, United Kingdom, Germany, Multi-jurisdictional (specify), Other
   - _Why this matters_: Determines applicable insolvency framework, court jurisdiction, and
     whether cross-border recognition (Chapter 15 / EU Insolvency Regulation) is needed.

2. **Solvency status** — What is the company's current financial condition?
   - Options: Cash flow insolvent (cannot pay debts as due), Balance sheet insolvent (liabilities
     exceed assets), Imminent illiquidity (will be insolvent within weeks/months), Over-indebted
     (negative equity), Solvent but distressed (liquidity stress only), Unknown
   - _Why this matters_: Determines which mechanisms are available. StaRUG requires only "imminent
     illiquidity" (drohende Zahlungsunfähigkeit). Chapter 11 is available regardless of solvency.
     Wrongful/insolvent trading obligations trigger on insolvency.

3. **Capital structure** — How is the debt structured?
   - Options: Single secured lender, Syndicated first lien, First lien / second lien stack,
     Senior notes / subordinated notes, Unitranche, Mixed secured + unsecured, Trade creditors only
   - _Why this matters_: Determines cramdown feasibility, DIP priming complexity, and intercreditor
     dynamics. First/second lien structures create waterfall and standstill considerations.

4. **Strategic objective** — What is the goal of the restructuring?
   - Options: Preserve the business as going concern (reorganize), Sell business/assets to new
     owner (§363 sale or equivalent), Wind down (liquidation), Reduce debt load only (balance
     sheet restructuring), Pre-insolvency de-leverage (StaRUG / out-of-court), Unknown
   - _Why this matters_: Going-concern goal → Chapter 11 plan / administration exit / StaRUG.
     Asset sale → §363 / pre-pack administration / distressed M&A. Wind down → Chapter 7 / CVL.

5. **Creditor consensus** — What is the level of creditor support?
   - Options: Strong majority support (prepackaged), Some support, negotiating (pre-negotiated),
     No support, adversarial (free-fall), Out-of-court feasible (workout), Unknown
   - _Why this matters_: Determines prepack feasibility, DIP lender identity, cramdown risk, and
     timeline. Adversarial creditor base → expect contested DIP, plan fights, avoidance actions.

6. **Perspective** — Whose interests does this analysis serve?
   - Options: Debtor/Company (management/board), Secured creditor, Unsecured creditor/committee,
     DIP lender, Equity sponsor, Potential buyer (distressed M&A), Neutral/Advisory
   - _Why this matters_: Trade-offs differ fundamentally. DIP lender wants tight milestones and
     priming; unsecured creditors want avoidance actions and plan value. Neutral analysis presents
     all sides.

### Step 3: Route to Modules

| Task Type                                    | Primary Module               | Supporting Modules                            |
| -------------------------------------------- | ---------------------------- | --------------------------------------------- |
| US Chapter 11 analysis                       | A (Chapter 11)               | B (363 Sale), C (DIP), F (Avoidance), G (Tax) |
| Section 363 sale                             | B (363 Sale)                 | A (Chapter 11), C (DIP)                       |
| DIP financing                                | C (DIP Financing)            | A (Chapter 11)                                |
| UK administration / CVA / restructuring plan | D (UK Frameworks)            | H (Out-of-Court)                              |
| German Insolvenzverfahren / StaRUG           | E (German Frameworks)        | H (Out-of-Court)                              |
| Avoidance actions                            | F (Avoidance)                | A (Chapter 11)                                |
| Tax issues                                   | G (Tax & Debt Restructuring) | All modules                                   |
| Out-of-court workout                         | H (Workout & OOC)            | A, D, E, G                                    |
| Debt-for-equity swap                         | I (Debt-for-Equity)          | G (Tax), H (Workout)                          |
| Intercreditor analysis                       | J (Intercreditor)            | A, C, H                                       |
| ABC / receivership                           | K (ABC & Receivership)       | H (Out-of-Court)                              |
| LME / uptier                                 | L (Liability Management)     | J (Intercreditor), H                          |
| Cross-jurisdiction / forum selection         | M (Cross-Border)             | All modules                                   |
| Anti-patterns review                         | N (Anti-Patterns)            | All modules                                   |

### Step 4: Gather Legal Authority (legalcode-mcp)

If **legalcode-mcp** is connected, search for:

- Applicable insolvency statutes and recent amendments (by jurisdiction track from Step 2)
- Recent plan confirmation decisions and cramdown rulings in the relevant court
- Avoidance action trends (preference settlement ranges, fraudulent transfer lookback issues)
- Tax authority on COD income, §382 NOL, and OID in the applicable jurisdiction
- Cross-border recognition decisions (Chapter 15 orders, COMI rulings, EU Regulation cases)

Save results to `/tmp/legalcode-restructuring-authority.md`. Mark sourced citations as `VERIFIED`.

If legalcode-mcp is **not connected**: proceed using the statutory citations and case law tables in this
skill, mark all as `[VERIFY]`, and note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`.

### Step 5: Execute Module Analysis

Activate the modules identified in Step 3. For each module:

1. Apply the module's analytical framework to the facts provided
2. Identify issues and classify each as **GREEN / YELLOW / RED**
3. For every RED item, apply Self-Interrogation (3-pass, below)
4. Note applicable anti-patterns from Module N
5. Apply Confidence Scoring to each finding

### Step 6: Classify Findings and Apply Prioritization

Use the Severity Notation:

- **GREEN** — Low risk; standard practice; well-settled law
- **YELLOW** — Moderate risk; requires attention; unsettled or jurisdiction-dependent
- **RED** — High risk; significant exposure; escalate to qualified counsel immediately
- **STRUCTURAL** — Fundamental issue with chosen mechanism; requires mechanism reassessment

Apply the **Prioritization Framework** (adapted for restructuring):

| Tier       | Label         | Description                                                                 | Action                                              |
| ---------- | ------------- | --------------------------------------------------------------------------- | --------------------------------------------------- |
| **Tier 1** | Deal-Critical | Mechanism-disqualifying, tax-destroying, or creditor-right-violating issues | Resolve before proceeding; senior counsel required  |
| **Tier 2** | Material      | Significant risk or value impact; strongly negotiable                       | Address in next planning cycle; document trade-offs |
| **Tier 3** | Monitoring    | Minor risk; standard in market; low probability of harm                     | Track; raise if related issues arise                |

**CLARIFY** — If the analysis reveals a Tier 1 issue that is disputed or where the facts are
ambiguous, present the alternatives:

- "This issue is classified Tier 1 [reason]. Do you want me to (a) proceed on conservative
  assumptions, (b) model the scenario where the risk does not materialize, or (c) flag and
  continue with [VERIFY] markers?"

### Step 7: Apply Quality Assurance

Run all three quality checks before delivering output:

1. **Citation Quality Gates** (5 gates — see Quality Frameworks section below)
2. **Self-Interrogation** for all RED items (3-pass — see Quality Frameworks section below)
3. **Confidence Scoring** for each material finding (5-level — see Quality Frameworks section below)

### Step 8: Deliver Analysis and Glass Box

Deliver the output using the Standard Restructuring Analysis Report format (see Output Format section).
Include the completed Glass Box Audit Trail YAML at the end of every output.

---

## Quality Frameworks

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before delivering.

| Gate           | Rule                                                                                                                                        | Fail Action                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established principle                                                            | Add citation or mark `[UNVERIFIED]` |
| **Format**     | All citations follow consistent format for the jurisdiction (e.g., 11 U.S.C. §362, IA 1986 Schedule B1, InsO §17)                           | Fix format                          |
| **Currency**   | Every cited provision checked for amendments or repeal (particularly StaRUG 2021, CIGA 2020 Part 26A, SBRA 2019 Subchapter V)               | Flag `[CHECK CURRENCY]`             |
| **Domain**     | Analysis stays within the jurisdiction track identified in Step 2; no bleed between US/UK/DE rules                                          | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated — do not present contested positions (e.g., LME Sacred Rights, new value exception circuit splits) as settled | Add confidence qualifier            |

### Self-Interrogation for RED Items

For any item classified RED or STRUCTURAL, apply this 3-pass review before including in output:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the cited
statute or case? Would a court in the relevant jurisdiction actually reach this conclusion?
Mark: `PASS` or `REVISED`.

**Pass 2 — Completeness**: Have all applicable statutes, regulations, cross-border rules, and
recent case law been considered? Are there tax dimensions (COD, §382, OID, Sanierungsgewinn) not
yet addressed? Mark: `PASS` or `REVISED`.

**Pass 3 — Challenge**: What is the strongest argument that this risk does NOT materialize?
Under what circumstances might experienced restructuring counsel accept this position? Are there
safe harbors, judicial exceptions, or market precedents that mitigate the risk?
Mark: `PASS` or `REVISED`.

Include Pass 3 output in the analysis (as the "Strongest counter-argument" field) — transparency
on uncertainty is required.

### Confidence Scoring

Assign a confidence level to each material finding in the analysis:

| Level        | Range     | Meaning                                                                       | Presentation Rule                                              |
| ------------ | --------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, clear statute, Supreme Court or House of Lords authority         | State with confidence; cite authority                          |
| **High**     | 0.80–0.94 | Strong authority, minor circuit or jurisdiction questions                     | State with brief caveat; cite authority                        |
| **Probable** | 0.60–0.79 | Good arguments, unsettled in some circuits; recent legislation not yet tested | State with reasoning and contra-indicators                     |
| **Possible** | 0.40–0.59 | Genuinely uncertain; active litigation; competing line of cases               | Flag for specialist review; present both sides                 |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative; not yet established                                  | Do not assert; flag `[UNCERTAIN]`; recommend specialist advice |

**Restructuring-specific calibration:**

- LME sacred rights violations post-_Serta Simmons_: High (0.85) in 5th Circuit; Probable (0.65) elsewhere
- StaRUG cross-class cramdown eligibility: Probable (0.70) — limited case law
- Part 26A cramdown post-_Petrofac_: High (0.80) — Court of Appeal authority
- New value exception market testing requirement: High (0.85) in 3d/7th Circuits; Probable (0.65) in 2d/9th

### Glass Box Audit Trail

Include this YAML block at the end of every output, completed for the specific analysis:

```yaml
glass_box:
  skill_name: "legalcode-corporate-restructuring"
  analysis_date: "[date]"
  jurisdiction_track: "[US / UK / DE / Multi-jurisdictional]"
  perspective: "[Debtor / Secured Creditor / Unsecured Committee / Buyer / Neutral]"
  modules_activated: "[list, e.g., A, C, G, N]"
  solvency_status: "[as provided or 'Unknown — assumed insolvent']"
  strategic_objective: "[reorganize / sell / wind down / de-leverage]"
  legalcode_mcp: "[Connected / Not connected]"
  authority_reference_file: "[/tmp/legalcode-restructuring-authority.md or 'Not created']"
  statutes_relied_upon:
    - "[11 U.S.C. §362 — VERIFIED / UNVERIFIED]"
    - "[IA 1986 Schedule B1 — VERIFIED / UNVERIFIED]"
    - "[StaRUG §26 — VERIFIED / UNVERIFIED]"
  case_law_relied_upon:
    - "[Serta Simmons (5th Cir. 2024) — VERIFIED / UNVERIFIED]"
  red_items_count: "[number]"
  self_interrogation: "[PASS / REVISED on [item] / NOT APPLICABLE — no RED items]"
  anti_patterns_checked: "[AP-01 through AP-21 — list those identified]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  assumptions_made:
    - "[list explicit assumptions where facts were not provided]"
  items_requiring_specialist_verification:
    - "[list items marked VERIFY or flagged for counsel]"
  limitations:
    - "[scope limitations, e.g., 'No solvency data provided — analysis assumes imminent illiquidity']"
    - "[e.g., 'Cross-border issues flagged but not analyzed in depth — Module M only']"
  reviewer: "AI-assisted — requires review by qualified restructuring counsel, financial advisor, and tax specialist"
```

---

## Writing Standards

Apply these standards before delivering any analysis output:

1. **Use jurisdiction-precise terminology**: "automatic stay" (US §362), not "stay"; "moratorium"
   (UK administration), not "freeze"; "Insolvenzeröffnung" alongside "opening of proceedings" (DE).

2. **Never state contested positions as settled law**: LME sacred rights, new value exception scope,
   and Part 26A fairness standard are actively litigated — present with confidence qualifiers.

3. **Distinguish between mechanism description and analysis**: Explain what the mechanism does,
   then separately assess whether it works for the specific facts.

4. **Flag jurisdictional bleed explicitly**: If a US concept (e.g., automatic stay) is being
   applied in a UK or German context, note that the equivalent is different (moratorium vs. stay).

5. **Pre-delivery quality gates** — before output is delivered, verify:
   - [ ] All RED items have completed 3-pass Self-Interrogation
   - [ ] Confidence levels are assigned to each material finding
   - [ ] All statutory citations are in the correct format for the jurisdiction
   - [ ] The Glass Box YAML is completed, not a template stub
   - [ ] Any legalcode-mcp results are recorded as VERIFIED; others as [VERIFY]

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

In Step 4, search for:

```
"Chapter 11 cramdown" jurisdiction:US recent-cases
"Part 26A restructuring plan" jurisdiction:UK
"StaRUG Stabilisierungsrahmen" jurisdiction:DE
"DIP financing priming lien" adequate-protection
"§382 NOL ownership change" debt-for-equity
```

Save results to `/tmp/legalcode-restructuring-authority.md`:

```markdown
# Restructuring Legal Authority

## Date: [date]

### US Statutes and Cases

- [citation, relevance, VERIFIED]

### UK Statutes and Cases

- [citation, relevance, VERIFIED]

### German Statutes and Cases

- [citation, relevance, VERIFIED]

### Tax Authority

- [citation, relevance, VERIFIED]
```

Mark all legalcode-mcp sourced citations as `VERIFIED` in the Glass Box.

### Without legalcode-mcp

Proceed using this skill's Key Statutory Citations and Key Case Law sections.
Mark all citations `[VERIFY]` in the Glass Box. Note: `legalcode_mcp: "Not connected"`.
Focus the analysis on structural and strategic guidance rather than cite-specific legal assertions.

---

## Module A: US Chapter 11 Reorganization

### Legal Framework

**Primary statute**: Title 11 U.S.C. (Bankruptcy Code), specifically:

- §101 — Definitions (including "insolvent," "insider," "claim," "equity security")
- §362 — Automatic stay
- §363 — Use, sale, or lease of property
- §364 — Obtaining credit (DIP financing)
- §365 — Executory contracts and unexpired leases
- §502 — Allowance of claims
- §510 — Subordination
- §547 — Preferences
- §548 — Fraudulent transfers
- §1101-1174 — Chapter 11 plan provisions
- §1123 — Contents of plan
- §1125 — Disclosure statement
- §1126 — Voting on plan
- §1129 — Confirmation of plan (including cramdown at §1129(b))

**Administering courts**: US Bankruptcy Courts. Major restructuring dockets concentrate in:

- Southern District of New York (SDNY) — traditionally preferred by large debtors
- District of Delaware (D.Del.) — most active venue for corporate Chapter 11
- Venue selection: debtor may file where incorporated, principal place of business, or where
  an affiliate has a pending case (28 U.S.C. §1408)

### Automatic Stay (§362)

Upon filing, an automatic stay immediately stops all collection actions, foreclosures,
enforcement of judgments, and creation of liens against the debtor or its property.

**Key features:**

- Immediate and automatic — no court order required
- Applies to all creditors worldwide (extraterritorial reach against foreign creditors asserted)
- Continues until case dismissal, plan confirmation, or court order lifting it

**Relief from stay (§362(d))**: Secured creditors may seek relief "for cause" (e.g., lack of
adequate protection, debtor has no equity in property and property not needed for reorganization).

**Notable**: Stay does not apply to criminal proceedings, tax audits, exercise of regulatory
police and regulatory powers, or setoff of certain financial contracts (safe harbors for repos,
swaps, forward contracts).

### Automatic Stay — Adequate Protection

When a secured creditor's collateral is used or is subject to a stay, the debtor must provide
"adequate protection" of the creditor's interest (§361):

- Periodic cash payments
- Replacement liens on other assets
- "Indubitable equivalent" (flexible, court-determined)

Failure to provide adequate protection can result in the secured creditor obtaining relief from
stay, converting the case to Chapter 7, or obtaining super-priority status.

### Plan of Reorganization (§1123)

A plan must:

1. Designate classes of claims and interests
2. Specify treatment of each class
3. Provide same treatment within each class (unless class members consent to lesser treatment)
4. Provide adequate means for implementation (e.g., issuance of new securities, merger, sale)
5. Prohibit issuance of non-voting equity securities

**Classification**: Claims are classified by legal nature and priority. Secured claims are
typically classified separately. Each secured claim secured by distinct collateral is its own
class. Unsecured claims may be classified in one or multiple classes based on legal character.

**Impairment**: A class is "impaired" unless the plan (a) leaves its legal, equitable, and
contractual rights unaltered, or (b) cures all defaults and reinstates original maturity
(reinstatement / de-acceleration, often for real estate loans).

### Plan Confirmation — Standard Requirements (§1129(a))

A plan may be confirmed if (among other requirements):

- At least one impaired class accepts (excluding insiders)
- All impaired classes accept OR cramdown applies (§1129(b))
- Plan is feasible (no likelihood of need for further liquidation or reorganization)
- Plan is proposed in good faith
- Administrative expenses are paid in full (unless holder agrees otherwise)
- Priority tax claims paid over 5 years with interest

**Voting thresholds**: A class accepts if holders of at least two-thirds in amount AND more than
one-half in number of allowed claims that vote, vote in favor (§1126(c)). Equity interests:
two-thirds in amount (§1126(d)).

### Cramdown (§1129(b))

If a class rejects (or is deemed to reject), the plan proponent may request cramdown confirmation.
The court must find the plan is:

1. **Does not discriminate unfairly** — similarly situated creditors receive reasonably equivalent
   treatment
2. **Fair and equitable** — the "absolute priority rule" cascade:
   - Secured claims: creditor retains lien AND receives deferred cash payments equal to value of
     collateral (or property equal to allowed amount, or sale of collateral with right to credit
     bid)
   - Unsecured claims: creditor receives value equal to allowed claim OR no junior class receives
     anything "on account of" its claim/interest
   - Equity: receives nothing unless unsecured creditors paid in full

**Absolute priority rule (APR)**: Under §1129(b), equity cannot retain value unless creditors above
it are paid in full. This is the fundamental fulcrum of Chapter 11 plan economics.

**APR exceptions and modifications:**

- **New value exception**: Existing equity may retain interest if they contribute "money or money's
  worth" that is "new, substantial, necessary to the plan, and reasonably equivalent to value
  received" — requires market testing (In re 203 N. LaSalle; In re Philadelphia Newspapers)
- **Gifting**: Higher-priority creditors may voluntarily share value with junior classes (gift
  from senior to junior) — permitted where senior creditor gives its own value and does not
  skip an intermediate class (but Second Circuit restricted gifting in DBSD / Tribune)
- **Subchapter V exception**: In SBRA small business cases, APR does not apply; owner-operator
  can retain equity if plan is fair and equitable (§1191(c)(2))

### Pre-Packaged, Pre-Negotiated, and Free-Fall Chapter 11

| Type               | Description                                                                                                            | Timeline                 | Cost    | Best For                                                                                         |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------- | ------------------------------------------------------------------------------------------------ |
| **Prepackaged**    | Plan and disclosure statement fully negotiated; votes solicited BEFORE filing; case filed with confirmed votes in hand | 30-90 days in bankruptcy | Lowest  | Capital-light balance sheet restructure; concentrated creditor base; strong pre-filing consensus |
| **Pre-negotiated** | Plan terms agreed; support agreement (RSA) signed; votes solicited AFTER filing                                        | 2-6 months               | Medium  | Broad creditor base requiring bankruptcy solicitation; some holdouts expected                    |
| **Free-fall**      | Filed without pre-arranged plan; negotiate in bankruptcy under court supervision                                       | 6-18+ months             | Highest | Emergency filing; no creditor consensus; complex operational issues; DIP needed immediately      |

**Restructuring Support Agreement (RSA)**: Contract binding signatories (often majority of a class)
to vote for a specific plan. Challenged if seen as locking the process, but widely used.

### Executory Contracts and Unexpired Leases (§365)

The debtor-in-possession may assume or reject executory contracts and unexpired leases (subject to
court approval). Key mechanics:

- **Assumption**: Debtor must cure all defaults and provide adequate assurance of future performance
- **Rejection**: Treated as a pre-petition breach — counterparty gets an unsecured damages claim
- **Assignment**: Debtor may assign assumed contracts despite anti-assignment clauses (§365(f)),
  though certain contracts (personal service, IP licenses with specific restrictions) have limits
- **365(n) — IP licenses**: Licensee of a right to intellectual property may elect to retain rights
  even if debtor rejects the license (critical for software/IP licensees facing debtor rejection)

**Real estate leases**: Debtor has 210 days to decide whether to assume or reject commercial real
property leases (§365(d)(4)).

### Subchapter V — Small Business Reorganization Act (SBRA 2019)

**Eligibility**: Debtors with aggregate non-contingent liquidated debts (secured and unsecured,
excluding debts to insiders and affiliates) under $7.5 million (temporary COVID increase; as of
2024, the threshold reverted to $2.725 million — verify current threshold).

**Key advantages over standard Chapter 11:**

- No creditors' committee unless ordered for cause (reduces professional fees)
- No disclosure statement required (plan contains required disclosures)
- Only debtor may file plan; 90-day deadline from petition date
- No impaired consenting class required for confirmation
- Absolute priority rule DOES NOT APPLY — owner may retain equity while paying disposable
  income for 3-5 years
- Subchapter V trustee appointed in every case to facilitate plan negotiation

**Cramdown under Subchapter V (§1191(c))**: If plan rejected by impaired class, court may
confirm if plan does not discriminate unfairly, is fair and equitable, and the debtor will
commit all projected disposable income for 3-5 years.

---

## Module B: Section 363 Asset Sales

### Legal Framework

**Statute**: 11 U.S.C. §363 — Use, sale, or lease of property (outside the ordinary course of
business requires notice, hearing, and court approval; see also §363(b)).

**"Free and clear" principle (§363(f))**: Assets may be sold free and clear of all liens,
claims, and encumbrances if one of five conditions is met:

1. Applicable non-bankruptcy law permits sale free and clear
2. Lienholder consents
3. The interest is a lien and the sale price exceeds all liens on the property
4. The interest is in bona fide dispute
5. Lienholder could be compelled in a legal or equitable proceeding to accept a money
   satisfaction of its interest

Liens attach to proceeds (with same priority as original collateral).

### The Sale Process

**Typical timeline:**

1. **Pre-bankruptcy marketing**: Investment banker engages potential bidders; data room opened;
   indicative bids received (often 4-12 weeks pre-filing)
2. **Stalking horse selection**: Debtor selects lead bidder; negotiates asset purchase agreement (APA)
3. **Bidding procedures motion**: Filed with court (Day 1 or shortly after petition); includes
   bidding procedures, qualification requirements, auction mechanics, break-up fee, expense
   reimbursement; court hearing typically 15-21 days after filing
4. **Marketing and diligence period**: Other bidders conduct due diligence (typically 30-45 days)
5. **Bid deadline and qualification**: Competing bids submitted; debtor, committee, and advisors
   review; qualified bidders identified
6. **Auction**: Open competitive bidding process; debtor (with creditor oversight) selects highest
   or otherwise best bid
7. **Sale hearing**: Court approval of winning bid (typically 1-3 days post-auction); objections
   heard and resolved
8. **Closing**: 10-30 days post-order (subject to regulatory approvals, financing, etc.)

### Stalking Horse Bid Protections

The stalking horse bidder receives protections for its role in setting the floor price:

- **Break-up fee**: Paid if debtor chooses competing bid. Delaware courts cap at 3% of purchase
  price in many cases; SDNY more flexible. US Trustee scrutinizes fees exceeding 3%.
- **Expense reimbursement**: Reimbursement of due diligence costs (separate from or combined with
  break-up fee)
- **Minimum overbid increment**: Establishes step-up for competing bids (typically 5-10% above
  stalking horse price)
- **Bid deposit**: Competing bidders must submit cash deposit (typically 10%) to qualify

**Bid protection scrutiny**: Courts apply business judgment test. US Trustee may object if
protections do not benefit the estate. Fifth Circuit in 2025 affirmed value of bid protections
where they produced competitive process.

### Credit Bidding (§363(k))

A secured creditor may "credit bid" its secured claim — i.e., bid the amount of its allowed
secured claim without paying cash. This is the secured creditor's primary defense against an
undervalued sale of its collateral.

**Limits on credit bidding**: Courts may limit or prohibit credit bidding "for cause" (RadLAX
Gateway Hotel LLC v. Amalgamated Bank, 566 U.S. 639 (2012) — plan cannot deprive secured
creditor of credit bid right unless provides indubitable equivalent; but §363 court has §363(k)
"for cause" discretion).

### Section 363 vs. Plan Sale

A §363 sale can occur at any time during a Chapter 11 case; does not require confirmation of
a plan. Post-RadLAX and other cases, courts have confirmed that §363 does not apply to plan-
based asset sales governed exclusively by §1129. Debtors use §363 sales when:

- Speed is critical (going-concern value deteriorating)
- Plan confirmation process too uncertain or time-consuming
- Buyer requires certainty before holiday/fiscal year
- DIP milestones require consummation within compressed timeline

---

## Module C: DIP Financing

### Legal Framework

**Statute**: 11 U.S.C. §364 — Obtaining credit post-petition:

- §364(a): Ordinary course unsecured credit (no court order needed)
- §364(b): Non-ordinary course unsecured credit (court order required)
- §364(c): Super-priority administrative expense claim; liens on unencumbered assets; junior
  liens on encumbered assets (court order required)
- §364(d): **Priming liens** — liens senior to or equal to existing liens on same collateral
  (court order required; court must find existing lienholders are adequately protected)

### DIP Financing Structures

**New money DIP**: Lender provides entirely new cash. Common where prepetition lender unwilling
or unable to fund post-petition.

**Roll-up DIP**: Prepetition lender's existing debt is "rolled up" — converted from a prepetition
claim (subject to plan treatment and avoidance) into the post-petition super-priority DIP facility.
Roll-up provides the lender with enhanced priority protection on its existing exposure.

- Historical norm: 2:1 roll-up ratio (2 dollars of rolled-up debt per 1 dollar of new money)
- Aggressive examples: First Brands (3:1 roll-up; $3.3B rolled); True Religion (4:1 roll-up,
  non-pro-rata among prepetition lenders)
- Courts scrutinize roll-ups for compliance with sacred rights provisions in syndicated credits

**Priming DIP**: Post-petition lien granted senior to prepetition liens. Requires court finding
of adequate protection for primed creditors. In practice, rare against well-perfected senior
liens on substantially all assets (20% equity cushion benchmark). Prospect Medical (Dallas, 2024)
illustrates the high threshold.

### DIP Covenants and Milestones

DIP credit agreements contain tighter covenants than prepetition facilities, including:

- **Reporting**: Weekly cash flow reports, 13-week cash flow budget, variance reporting
- **Milestones**: Hard deadlines for key case events — triggers for default if missed:
  - Disclosure statement filing deadline
  - Plan filing deadline
  - Plan confirmation order deadline
  - 363 sale bidding procedures approval
  - 363 sale closing deadline
  - Committee formation (information milestones)
- **Budget compliance**: Actual spending vs. approved budget variance limits (typically 10-15%
  cumulative, 20% weekly)
- **Consent rights**: DIP lender consent required for material asset dispositions, assumption/
  rejection of key contracts, settlement of claims above threshold

**Milestones as leverage**: DIP milestones give the DIP lender (often the prepetition senior
lender) significant influence over case pace and outcome. A default on a milestone can trigger
demand for repayment, conversion to Chapter 7, or restructured terms favoring the DIP lender.
Courts have pushed back on milestones designed to force a sale outcome rather than allow
genuine plan exploration.

### Loan-to-Own Strategy

Private equity and distressed debt funds use DIP financing as a pathway to equity ownership:

1. Acquire prepetition debt at a discount in secondary market
2. Provide DIP financing (often with equity conversion option or exit financing commitment)
3. Credit bid DIP facility at §363 sale or support plan that converts DIP to equity
4. Emerge as equity owner of reorganized company

This strategy is legitimate but courts scrutinize plans where DIP lender becomes sole equity
owner without meaningful marketing or competition.

---

## Module D: UK Administration, CVA, and Restructuring Plans

### Insolvency Act 1986 — Administration

**Purpose** (IA 1986 Schedule B1, para. 3): The administrator must perform their functions with
the objective of:

1. Rescuing the company as a going concern (primary objective, if reasonably practicable)
2. Achieving a better result for creditors as a whole than would be likely on winding up
3. Realizing property to make distribution to secured or preferential creditors (last resort)

**Appointment routes:**

- Court order (on application of company, directors, or qualifying floating charge holder)
- Out-of-court appointment by holder of qualifying floating charge (QFCH) — most common route
- Out-of-court appointment by company or directors

**Moratorium**: Administration triggers an automatic moratorium (IA 1986 Schedule B1, para. 43)
— no legal process may be instituted or continued against the company or its property without
court leave. Applies to enforcement of security (except by QFCH), repossession of goods on HP/
conditional sale, forfeiture of leases.

**Administrator's duties**: Administrator is an officer of the court; owes duties to all creditors
as a body; must act with reasonable skill and care; has wide powers to manage and dispose of
assets (Schedule B1, para. 59-70).

**Exit routes from administration:**

- Approval of CVA by creditors (then administration discharged)
- Return of company to directors (if objective achieved)
- Move to creditors' voluntary liquidation (CVL)
- Dissolution (if no assets)
- Sale of business/assets and distribution to creditors (pre-pack or post-appointment sale)

### Company Voluntary Arrangement (CVA) — IA 1986 Part I

**Process:**

1. Directors or administrator propose CVA
2. Insolvency practitioner acts as nominee, assesses viability
3. Nominee reports to court
4. Creditor vote: approval requires 75% in value of unsecured creditors who vote
5. Shareholder vote: approval requires 50%+ of shareholders
6. CVA binds all unsecured creditors — including those who voted against or abstained
7. Supervisor oversees implementation (often same IP as nominee)

**Key limitation**: CVA cannot bind secured creditors without their consent. Secured creditors
retain enforcement rights unless they agree to compromise.

**Challenge grounds (IA 1986 §6)**:

- Unfair prejudice to a creditor or member
- Material irregularity in relation to any of the meetings

**Challenge window**: 28 days from the date of the nominee's report to court.

**Landlord challenges**: Major source of CVA litigation. Key cases:

- _New Look_ (2021): High Court dismissed landlord challenge to CVA creating multiple classes
  of landlords treated differently — not inherently unfair
- _Regis_ (2021): Court revoked CVA where 75% discount applied to landlord claims for voting
  purposes was arbitrary — discount must be a reasonable estimate of minimum value
- _Debenhams_: CVA upheld despite differential treatment of landlords

### Pre-Pack Administration — SIP 16

**Definition**: A pre-pack is a sale arranged before the appointment of the administrator, which
is completed immediately upon (or shortly after) appointment.

**SIP 16 (Statement of Insolvency Practice 16)**: Regulatory standard governing pre-pack
administrations. Requires:

- Comprehensive disclosure statement to creditors explaining the transaction
- Evidence of marketing efforts (or explanation of why pre-marketing was not undertaken)
- Independent valuation of assets
- Explanation of why pre-pack was in the best interests of creditors

**Connected party pre-packs (Phoenix transactions)**: Sale to a connected party (e.g., existing
directors, shareholders) requires enhanced scrutiny. Since April 2021 (The Administration
(Restrictions on Disposal etc. to Connected Persons) Regulations 2021):

- Connected party pre-packs require either creditor approval OR opinion from an independent
  evaluator (from the Pre-Pack Pool) that the deal is reasonable
- Growth: connected party pre-packs rose from 201 in 2021 to 395 in 2024 (Taylor Wessing 2025)

**Criticisms**: Pre-packs have faced sustained criticism for allowing "Phoenix" companies —
where directors shed liabilities and re-start with same assets — at expense of unsecured creditors
(including HMRC, trade creditors, landlords). SIP 16 revisions and 2021 Regulations partly address
these concerns.

### Part 26A Restructuring Plans — Companies Act 2006

**Introduction**: Introduced by Corporate Insolvency and Governance Act 2020 (CIGA 2020),
effective 26 June 2020, as Part 26A of the Companies Act 2006.

**Key features compared to CVA and Scheme of Arrangement:**

| Feature                   | CVA                         | Scheme (Part 26)                  | Restructuring Plan (Part 26A)                |
| ------------------------- | --------------------------- | --------------------------------- | -------------------------------------------- |
| Eligibility               | Any company                 | Any company                       | Financial difficulty (new requirement)       |
| Secured creditors         | Cannot bind without consent | Can bind (separate class)         | Can bind (separate class)                    |
| Cross-class cramdown      | No                          | No                                | Yes                                          |
| Voting threshold          | 75% by value                | 75% by value + majority in number | 75% by value per class                       |
| Court involvement         | Limited                     | Sanction hearing                  | Convening + sanction hearings                |
| Administration moratorium | No (standalone)             | No                                | No (but company can enter administration)    |
| Best-for-creditors test   | No (unfair prejudice test)  | No (strict)                       | Yes (no worse off than relevant alternative) |

**Cross-class cramdown (§901G Companies Act 2006)**: Court may sanction a plan even if a class
dissents (votes below 75%) provided:

1. The dissenting class would be no worse off than in the "relevant alternative" (typically
   administration or liquidation)
2. At least one class that is "in the money" in the relevant alternative votes in favor

**Cramdown up**: English courts have permitted "cramming up" — imposing a plan on a senior class
that voted against, where the senior class is no worse off and junior classes support (Norton Rose
Fulbright note on unitranche structures).

**Post-Petrofac/Saipem fairness standard (2025)**: The Court of Appeal in _Saipem & Ors v
Petrofac Limited_ [2025] EWCA Civ 821 significantly tightened requirements for plan sanction:

- Plan company must ensure **fair distribution of restructuring benefits to ALL classes**,
  including out-of-the-money classes — not just dissenting class "no worse off" test
- Burden of proving fairness rests entirely on the plan company
- Bilateral negotiation between plan company and ad hoc senior creditor group insufficient — must
  genuinely engage all stakeholder classes from the outset
- New money terms must be market-tested; unexplained disconnect between work fees and post-
  restructuring equity value (as in Petrofac) will defeat sanction
- _Waldorf_ (2025): Further plan declined sanction on fairness/judicial discretion grounds

---

## Module E: German Insolvenzverfahren and StaRUG

### Insolvenzordnung (InsO) — Insolvency Proceedings

**Filing triggers (§§17-19 InsO)**:

- **Zahlungsunfähigkeit (cash-flow insolvency)** — inability to pay debts as they fall due
  (current and within 3 weeks); **mandatory filing** within 3 weeks for management
- **Drohende Zahlungsunfähigkeit (imminent illiquidity)** — will be unable to pay debts when
  due; voluntary trigger only
- **Überschuldung (over-indebtedness)** — liabilities exceed assets AND no positive going-concern
  prognosis; **mandatory filing** within 6 weeks (as of 2022 reform: 6 weeks extended from 3)

**Directors' duty to file**: Under §15a InsO, directors (Geschäftsführer of GmbH; Vorstand of AG)
have a personal obligation to file for insolvency within the statutory deadlines. Late filing
exposes directors to civil liability and criminal sanctions (§15a(4) InsO).

**Insolvency administrator (Insolvenzverwalter)**: Court-appointed; takes control of the debtor's
assets and business. Duties include: investigation of claims; realization of assets or
restructuring; avoidance actions; distribution to creditors. Historical concern: liquidation
bias due to administrator compensation incentives — addressed in part by ESUG 2012.

**Insolvenzplan (§§217-269 InsO)**: Equivalent to a plan of reorganization. Must include
descriptive part (Darstellungsteil — current position, causes of insolvency, proposed measures)
and planning part (Gestaltungsteil — rights of creditors, equity holders). Creditor groups vote:

- Each group requires majority in number AND majority by value (simple majority — not 75%)
- Plan confirmed if majority of groups approve or court finds holdout groups no worse off
  (German cramdown)

### ESUG 2012 Reforms

**Key changes introduced by ESUG (Gesetz zur weiteren Erleichterung der Sanierung von Unternehmen,
effective March 1, 2012)**:

1. **Eigenverwaltung (debtor-in-possession)**: Strengthened; debtor management remains in control
   under supervision of a Sachwalter (monitor) rather than an Insolvenzverwalter
2. **Schutzschirmverfahren (protective umbrella)**: New procedure allowing debtor to prepare an
   Insolvenzplan with court protection for up to 3 months
3. **Creditor influence on administrator selection**: Creditors now have greater influence in
   selecting the preliminary insolvency administrator (vorläufiger Insolvenzverwalter)
4. **Debt-to-equity swaps in Insolvenzplan**: Explicitly permitted

### Eigenverwaltung (§§270-285 InsO)

**Concept**: German equivalent of Chapter 11 DIP (debtor-in-possession). Company management
retains operational control; a Sachwalter (supervisor, not a full administrator) is appointed
by the court to monitor and check the debtor's actions.

**Requirements**: Court grants Eigenverwaltung if no circumstances known that would lead to
disadvantage for creditors. Creditor committee (if formed) must not object.

**Enhanced Eigenverwaltung rules (SanInsFoG 2021)**: Reforms made Eigenverwaltung more
predictable. Debtor must submit a comprehensive restructuring concept (Eigenverwaltungsplanung)
before or at filing; court must assess viability more rigorously.

### Schutzschirmverfahren (§270b InsO)

**Process**: Available where debtor is only "imminent illiquidity" or "over-indebted" (not yet
actually insolvent). Debtor applies to court; court appoints provisional Sachwalter; debtor has
up to **3 months** to prepare Insolvenzplan under court protection (moratorium on enforcement).
Debtor may propose the Sachwalter.

**Similarities to Chapter 11**: Debtor in control; court protection from creditor actions; plan-
based restructuring. Key difference: significantly shorter timeframe (3 months vs. Chapter 11's
typical 6-18 months); mandatory filing triggers more rigid.

**Historical cases**: Gerry Weber (fashion retailer) combined Schutzschirmverfahren for one
subsidiary (to terminate leases and employment contracts) with StaRUG for balance-sheet
restructuring — illustrating hybrid use of tools.

### StaRUG — Stabilisierungs- und Restrukturierungsrahmen (2021)

**Introduction**: Effective January 1, 2021, implementing EU Directive 2019/1023 (Preventive
Restructuring Directive). Created a pre-insolvency restructuring framework for the first time
in German law.

**Key distinction from Insolvenzverfahren**: StaRUG does NOT require insolvency; only "imminent
illiquidity" (drohende Zahlungsunfähigkeit) over a planning horizon of 24 months.

**Confidential nature**: StaRUG proceedings are generally non-public (unlike insolvency
proceedings) — significant competitive advantage for debtors with reputational concerns.

**Management control**: Management remains in control throughout; no administrator is appointed
unless there are specific protection orders. Court involvement is minimal in uncontested cases.

**Flexible creditor inclusion**: Debtor may selectively include creditor groups in the
restructuring plan. Cannot include claims arising from criminal activity, tort, or pension
obligations.

**Restructuring plan voting**:

- Creditors divided into groups (similar classes to Chapter 11)
- Each group approves by **75% of voting rights** (value-based)
- Simple majority of groups must approve the plan (or court applies cross-class cramdown)

**Cross-class cramdown (§26 StaRUG)**: A dissenting class may be crammed down if:

1. Majority of voting classes approve the plan
2. Members of dissenting class are no worse off than in the relevant alternative
3. Members of dissenting class receive adequate share of the value created by the restructuring

**Shareholder consent controversy**: Courts divided on whether StaRUG plan affecting shareholder
rights requires board-level approval only (GmbH) or also shareholder approval (AG). LEONI case
involved 100% shareholder equity to anchor investor — resolved by consent but flags risk.

**Court stabilization tools**: Debtor can apply for court orders to:

- Suspend individual enforcement actions (Vollstreckungssperre) for up to 3 months (extendable)
- Block termination rights of counterparties (Verwertungssperre)
- Obtain "restructuring moderation" (Restrukturierungsbeauftragte) — court-appointed expert

**Key StaRUG cases (2023-2025)**:

- **LEONI** (2023): Automotive supplier; €1.1B RCF restructured; anchor shareholder received 100%
  equity for €150M new capital; demonstrated large-scale applicability
- **EMAG GmbH** (2024): Industrial sector; further demonstrated StaRUG viability
- **Spark Networks SE** (2024): Dating platform; cross-border application
- **Varta AG** (2024): Battery manufacturer; high-profile case involving shareholder disputes
- **Galapagos ECJ ruling (2024)**: First insolvency/restructuring filing blocks subsequent
  applications in other jurisdictions until first court decides — "race to court" implications
  for cross-border debtors

**StaRUG vs. Chapter 11 comparison:**

| Feature              | StaRUG                                    | Chapter 11                           |
| -------------------- | ----------------------------------------- | ------------------------------------ |
| Trigger              | Imminent illiquidity (24-month horizon)   | Voluntary (no minimum solvency test) |
| Confidentiality      | Generally non-public                      | Public docket                        |
| Management control   | Retained                                  | Retained as DIP (usually)            |
| Creditor selection   | Debtor chooses which creditors to include | All creditors included               |
| Voting threshold     | 75% per group                             | 2/3 value + 1/2 number per class     |
| Timeline             | Months                                    | Months to years                      |
| New money/DIP        | No statutory DIP mechanism                | Robust DIP financing framework       |
| Employment contracts | Cannot be terminated via StaRUG           | §365 rejection available             |
| Lease termination    | Cannot be terminated via StaRUG           | §365 rejection available             |
| Tax claims           | Cannot be restructured                    | Can be restructured in plan          |

---

## Module F: Avoidance Actions

### Preferences (§547)

The trustee/DIP may recover payments made by the debtor:

- **Elements**: (1) To or for benefit of a creditor; (2) on account of an antecedent debt;
  (3) while debtor was insolvent; (4) within the lookback period; (5) that enables the creditor
  to receive more than it would in a Chapter 7 liquidation
- **Lookback period**: 90 days for arms-length creditors; **1 year for insiders** (if insider had
  reasonable cause to believe debtor was insolvent)
- **Presumption of insolvency**: Debtor is presumed insolvent during the 90 days before filing

**Defenses to preference actions (§547(c))**:

- **Contemporaneous exchange for new value**: Payment exchanged for new value given to the debtor
  at the same time (e.g., C.O.D. payments)
- **Ordinary course of business**: Payment made in the ordinary course of debtor's and creditor's
  business affairs OR consistent with ordinary business terms in the industry
- **New value**: Creditor gave new value after the preferential payment (reduces exposure by
  amount of new value)
- **Enabling loan**: Payment of purchase-money security interest perfected within 30 days of
  debtor's receipt of collateral
- **Statutory lien**: Payment to holder of statutory lien that could not be avoided under §545

**Settlement practice**: Most preference cases settle for 10-50 cents on the dollar, depending
on strength of defenses. Large estates pursue preference claims systematically.

### Fraudulent Transfers (§548 and State Law via §544)

**§548 — Federal fraudulent transfer**: Covers transfers within **2 years** before filing:

- **Actual fraud**: Transfer made with actual intent to hinder, delay, or defraud creditors
- **Constructive fraud**: Transfer made for less than reasonably equivalent value while debtor was
  insolvent, undercapitalized, or unable to pay debts

**§544 — State law fraudulent transfer**: The trustee may also use state fraudulent transfer laws
(UVTA / UFTA), which typically have **4-year or 6-year** lookback periods. This significantly
extends avoidance reach for transactions funded by leveraged buyouts, dividend recaps, and
intercompany transfers.

**Leveraged buyout (LBO) avoidance**: In an LBO, target's assets are pledged to secure
acquisition debt. If the LBO was a constructive fraudulent transfer (target received no value but
became liable for acquisition debt), the liens can be avoided. Courts are split on applying
§548 vs. §544/state law in LBO contexts.

---

## Module G: Tax Considerations in Restructuring

### US — Cancellation of Debt Income (COD / CODI)

When a debtor's debt is forgiven, reduced, or modified, the amount discharged may constitute
taxable income (IRC §61(a)(12)) — "cancellation of debt income" (CODI).

**Amount of CODI**: Excess of outstanding principal of debt over fair market value of
consideration given (cash, equity, new debt) to satisfy the debt.

**Bankruptcy exclusion (IRC §108(a)(1)(A))**: CODI is fully excluded from gross income when
the discharge occurs in a Title 11 bankruptcy case — even if the debtor is solvent on emergence.
This is the most powerful COD exclusion.

**Insolvency exclusion (IRC §108(a)(1)(B))**: CODI excluded to the extent the debtor was
insolvent immediately before the discharge. Available for out-of-court restructurings.

**Tax attribute reduction (IRC §108(b))**: Use of the bankruptcy or insolvency exclusion
triggers a mandatory reduction of tax attributes in this order:

1. Net operating losses (NOLs)
2. General business credits (34 cents per dollar of CODI)
3. Minimum tax credits
4. Capital loss carryovers
5. Basis in property (limited to aggregate adjusted basis of all property held after discharge)
6. Passive activity loss/credit carryovers
7. Foreign tax credit carryovers

**Section 382 limitation**: An ownership change (>50% change in beneficial ownership within
3 years) triggers IRC §382 annual limitation on use of pre-change NOLs. In restructuring:

- Debt-for-equity swaps typically cause an ownership change
- §382(l)(5) bankruptcy exception: If in Title 11, old shareholders and historic creditors
  (who held debt for 18 months before filing) own ≥50% of post-emergence equity, §382 limitation
  does not apply — but any NOLs used within 2 years before filing trigger reduction
- §382(l)(6) bankruptcy alternative: If §382(l)(5) unavailable, §382 limitation equals value of
  debtor stock immediately after emergence × long-term tax-exempt rate

**Debt modification and OID**: Significant modification of a debt instrument is treated as a
deemed exchange of old debt for new debt (Treas. Reg. §1.1001-3). If new debt issued at a
discount to face value, the difference is OID — taxable as interest income to lender over the
life of the instrument. Surprisingly routine modifications (rate changes, PIK interest, fees)
can trigger deemed exchanges and phantom OID income.

### UK Tax Considerations

**Loan relationship rules (CTA 2009 Part 5)**: UK companies are taxed on profits/deficits of
loan relationships under the "fair value" accounting rules. Debt releases and modifications create
credit entries (taxable income) for the debtor.

**'Relevant debts' exemption**: Releases of debt in formal insolvency (administration, CVL,
liquidation) are generally exempt from UK tax under the loan relationship rules.

**Group relief and debt restructuring**: Intercompany debt releases within a group may be neutral
for tax purposes if within the same UK tax group, but cross-border group restructurings can create
mismatch issues.

**Debt-for-equity UK treatment**: Where debt is converted to equity, the lender recognizes the
exchange at fair value; the borrower may have a credit under loan relationship rules (subject to
insolvency exemptions). Stamp duty and stamp duty reserve tax considerations apply to equity
issued.

### German Tax Considerations

**Sanierungsgewinn (debt restructuring gain)**: When debt is waived as part of a restructuring,
a taxable gain arises for the debtor. The BMF Schreiben (Federal Ministry of Finance letter) from
2003 provided a tax-free treatment for "Sanierungsgewinne" — but the Federal Fiscal Court (BFH)
ruled this was an illegal state aid in 2016. The SanInsFoG 2021 introduced a statutory exemption
for restructuring gains in certain insolvency and pre-insolvency contexts.

**Section 8c KStG (corporate tax act)**: Ownership changes of more than 25% result in partial
forfeiture of loss carryforwards; changes of more than 50% result in complete forfeiture. In
insolvency contexts, special exceptions (Sanierungsklausel) may preserve losses.

---

## Module H: Out-of-Court Workouts and Restructuring

### Fundamentals of Out-of-Court Restructuring

Out-of-court workouts offer significant advantages over formal proceedings:

- No automatic publicity or court docket
- Confidentiality — participants bound by NDAs
- Flexibility — parties define process, timeline, payment terms
- No automatic stay complications (but no stay protection either)
- Avoidance of administration/US trustee oversight
- Lower professional costs (absent complex negotiation)
- Trade credit and customer relationships less disrupted
- Interest accrues; no Section 502(b) claim objection risk

**Disadvantages:**

- No automatic stay — creditors may accelerate or enforce during negotiations
- Holdout problem: minority creditors can refuse without court compulsion
- No avoidance action benefits available to debtor
- Cannot force assignment of executory contracts
- No ability to cram down dissenting creditors
- Consent of all material creditors required (or risk of holdout-triggered insolvency filing)

### Standstill and Forbearance Agreements

**Forbearance agreement**: Lender agrees to refrain from exercising default remedies for a
defined period while debtor and creditors negotiate. Key terms:

- Duration: Typically 2-3 weeks initial period, 30-day second period; extendable by consent
- Conditions: Debtor must comply with information covenants, budget, and cooperation requirements
- Representations: Debtor acknowledges defaults; no waiver of creditor's rights
- Short duration preserves creditor pressure and flexibility

**Standstill**: In intercreditor context, a junior lienor's agreement not to exercise remedies
against collateral while senior lienor's debt remains outstanding. Standstill periods in first/
second lien intercreditor agreements typically run 90-180 days.

### Workout Agreements

A fully negotiated out-of-court restructuring agreement typically covers:

- **Debt restructuring terms**: Maturity extension, interest rate reduction/PIK election,
  principal haircut, covenant relief, new equity injection
- **Governance**: Lender consent rights, board observer seats, financial covenants
- **New money**: Conditions for new capital injection or revolving credit availability
- **Intercreditor mechanics**: Waterfall, payment blockage triggers, enforcement standstill
- **Milestones**: Agreed operational and financial targets; consequences of breach
- **Releases**: Mutual releases of claims arising from period of distress

**LSTA and LMA standards**: The Loan Syndications and Trading Association (LSTA) in the US and
Loan Market Association (LMA) in Europe provide standard documentation and trading conventions
for distressed loan trading, including par and distressed settlement mechanics, NACK procedures,
and trading representations.

### Distressed Debt Exchanges

**Exchange offer**: Company offers existing debt holders new debt (or equity) in exchange for
cancellation of old debt. Typically conducted outside bankruptcy.

**Exit consent**: In connection with an exchange offer, tendering holders consent to amend the
terms of the remaining (non-tendered) notes — stripping covenants, events of default, and
collateral provisions. This makes holdout notes effectively worthless, pressuring participation.
(Assenagon Asset Management v Irish Bank Resolution Corp [2012] EWHC 2090 (Ch) — English court
found exit consent equivalent to improper use of power in English law context.)

**UK Assenagon doctrine**: English courts have restricted the use of majority bondholders
consenting on behalf of all to strip holdout rights — exit consents that damage holdout
economic interests may be invalidated as improper use of voting power.

---

## Module I: Debt-for-Equity Swaps

### Mechanics

A debt-for-equity swap converts outstanding debt claims into equity ownership. Mechanics:

1. Debtor and creditors agree on exchange ratio (debt face value or market value vs. equity %)
2. In formal proceedings (Chapter 11, Insolvenzplan): swap implemented through plan; court
   confirms plan; new equity issued to former debt holders
3. In out-of-court: new equity issued to creditors in exchange for debt cancellation (requires
   consent of existing equity holders or sufficient contractual flexibility)

**Valuation disputes**: The critical battleground. Creditors want equity valued low (preserving
debt priority); management and sponsors want equity valued high (preserving existing equity).
Independent valuation is almost always required and frequently contested.

**Holdout problem**: Minority creditors may refuse to swap, hoping to be repaid at par while
others receive equity. Solutions:

- Formal insolvency proceedings with cramdown (eliminates holdouts)
- Exchange offer with exit consent strip (out-of-court pressure mechanism)
- Majority lender provisions in credit agreement (majority can bind minority to restructuring)

### Equitization in Restructuring Plans

**US Chapter 11**: Debt-for-equity swaps are the most common outcome for heavily leveraged
companies. In a plan:

- Secured debt can be equitized in satisfaction of secured claim (§1129(b)(2)(A)(iii))
- Unsecured notes frequently equitized if company insolvent and equity is wiped
- Absolute priority rule constrains what junior classes receive when senior classes not paid in full

**UK Part 26A**: Restructuring plans can implement debt-for-equity swaps against dissenting
creditors through cross-class cramdown. LEONI-style anchor investor structures comparable.

**Germany StaRUG**: ESUG 2012 explicitly permitted debt-to-equity swaps in the Insolvenzplan;
StaRUG carries this forward. Shareholder consent issues remain unresolved in non-insolvency context.

---

## Module J: Intercreditor Agreements

### First Lien / Second Lien Structure

**Standard terms:**

- **Payment priority/waterfall**: First lien paid in full before second lien receives anything
  (lien subordination), with all proceeds applied first to first-lien obligations
- **Standstill**: Second lien lender cannot enforce remedies against shared collateral while first
  lien is outstanding. Standstill period: typically 90-180 days
- **DIP financing waiver**: Second lien lender agrees in advance not to object to any DIP
  financing, cash collateral use, or adequate protection arrangement agreed to by first lien lender
- **Plan voting**: First lien lender may have right to vote (or instruct vote of) second lien
  lender's claim in bankruptcy
- **Adequate protection waiver**: Second lien lender may waive right to receive adequate protection
  payments, agreeing not to receive any payments ahead of first lien
- **363 sale consent**: Second lien consents in advance to any §363 sale approved by first lien

**"Sacred rights" / pro-rata provisions**: Syndicated credit agreements typically include
provisions requiring all lenders to be treated equally (pro-rata). Non-pro-rata DIP roll-ups
violate these provisions and can be challenged by excluded lenders (American Tire Distributors).

### Senior / Subordinated Note Structures

In leveraged finance structures with senior secured bank debt and high-yield notes:

- **Payment blockage**: Subordinated noteholders cannot receive payment while a payment default
  exists on senior debt (blockage period: typically 179 days maximum)
- **Standstill on enforcement**: Subordinated noteholders cannot sue or accelerate during blockage
- **Turnover**: Any amounts received by subordinated noteholders in violation of subordination
  provisions must be turned over to senior lenders

---

## Module K: Assignment for Benefit of Creditors (ABC) and Receivership

### Assignment for Benefit of Creditors (ABC)

**Nature**: State law liquidation mechanism (governed by state statute or common law; over 30
states have codified ABC statutes; California, Texas, and Illinois most frequently used). Not
a federal bankruptcy proceeding.

**Process**:

1. Debtor (assignor) voluntarily transfers all assets to an assignee (fiduciary)
2. Assignee liquidates assets and distributes proceeds to creditors in priority order
3. Creditors file claims with assignee; assignee determines validity and priority
4. No court order needed to initiate (in most states); court involvement varies by state

**Key advantages over Chapter 7 bankruptcy**:

- Assignor selects the assignee (vs. court-appointed trustee in Chapter 7)
- Faster process — typically 6-12 months vs. Chapter 7's 12-24+ months
- Lower cost than federal bankruptcy
- Less public visibility; media attention typically lower
- Assets typically sold free of unsecured creditor claims (in most states)

**Key limitations**:

- **No automatic stay** — creditors may still file involuntary bankruptcy or seek court remedies
- **No discharge** — individual principals do not receive discharge of personal guarantees
- **Preference and fraudulent transfer law**: Some states apply preference-like rules; buyers
  seek protection through court-supervised process
- **Involuntary bankruptcy risk**: Any creditor can file an involuntary Chapter 7 during the ABC
  process, potentially converting it to federal proceedings

**Popular use case**: Technology startups in California; companies seeking fast, low-profile
wind-down without formal bankruptcy. Delaware ABCs allow for court supervision providing
greater creditor comfort.

### Receivership

**Nature**: Court-appointed receiver manages and/or liquidates assets of a debtor for the benefit
of a creditor (typically a secured creditor). Governed by state law and federal equity power.

**Appointment**: Secured creditor petitions state or federal court to appoint receiver upon
default. Court grants order; receiver steps into management of collateral.

**Advantages over Chapter 11**:

- Faster and less expensive (especially for real estate or single-asset entities)
- Secured creditor retains significant control of the process
- Less regulatory oversight
- No US Trustee involvement

**Limitations**:

- No automatic stay — receiver does not stop all litigation (though appointing court protects
  receivership estate)
- Cannot confirm a plan of reorganization or bind all creditors
- Cannot compel assumption/rejection of executory contracts (no §365)
- Limited avoidance action powers (varies by state)

**Receivership vs. Chapter 11**: Secured creditors generally prefer receivership when collateral
is clearly in excess of debt, assets are discrete (real property, operating business unit), and
quick realization is the goal. Chapter 11 preferred when going-concern value significantly exceeds
liquidation value and multiple creditor constituencies require binding.

---

## Module L: Liability Management Exercises (LME)

### Overview and Evolution

Liability management exercises (LMEs) are out-of-court transactions that restructure a company's
debt without formal insolvency proceedings, typically using majority lender provisions in credit
agreements to disadvantage holdout creditors.

**Early forms (2019-2023)**: "Lender-on-lender violence." Aggressive transactions:

- **Uptier / uptiering**: Majority of lenders agree to exchange existing debt for new senior
  secured debt, which primes (ranks senior to) the non-participating minority lenders. Non-
  participating lenders' debt subordinated in priority without their consent. Classic examples:
  Serta Simmons (2020), Boardriders (2021), Chewy (2020).
- **Dropdown**: Company transfers valuable assets to an unrestricted subsidiary outside the credit
  group; new senior debt issued at subsidiary level (secured by transferred assets), leaving
  original lenders with claims against a hollowed-out entity. Example: J. Crew.

**Court response**: Serta Simmons cases (2023-2025) resulted in split outcomes — some circuits
permitting uptiers if majority provisions unambiguous; 5th Circuit (2024) found Serta uptier
violated pro-rata payment provisions of the credit agreement. Post-Serta, borrowers are adjusting
documentation and tactics.

**Modern evolution**: "Inclusive inequality" through lender co-ops (cooperation agreements):

- Groups of lenders pre-coordinate via co-op agreements restricting side deals
- Creates a steering committee that negotiates preferential economics with the borrower
- Reduces litigation risk by appearing consensual while still delivering unequal outcomes
- Private credit funds increasingly compete for co-op economics

**UK/European LMEs (2025-2026)**: Hunkemöller and Selecta cases are primary test cases for
LME validity in English-law governed credits. English courts expected to rule on fairness to
minority lenders in 2026, with Assenagon principles as potential constraint.

---

## Module M: Cross-Border Restructuring and Forum Selection

### Chapter 15 — Recognition of Foreign Proceedings (US)

Chapter 15 of the Bankruptcy Code (11 U.S.C. §§1501-1532) implements UNCITRAL Model Law on
Cross-Border Insolvency. A "foreign representative" (administrator, liquidator) may petition
a US Bankruptcy Court to recognize a foreign proceeding.

**Recognition effects**: Upon recognition as "foreign main proceeding" (where COMI is located):

- Automatic stay applies to US assets
- Right to administer US assets
- Right to seek US discovery
- Foreign representative may appear in US courts

**Center of Main Interests (COMI)**: The COMI of a debtor (analogous to EU Insolvency Regulation
Art. 3) determines whether a foreign proceeding is recognized as "main" or "non-main."

### EU Insolvency Regulation (2015/848)

Governs jurisdiction and recognition of insolvency proceedings within EU member states. Key:

- COMI determines which member state has jurisdiction for "main" insolvency proceedings
- Proceedings opened in COMI state automatically recognized in all other EU states
- Secondary proceedings (territorial, liquidation only) possible in member states where debtor
  has an establishment

**Galapagos ECJ ruling (2024)**: First filing in a member state blocks subsequent filings in
other member states until the first court rules on jurisdiction. Creates a "race to court"
dynamic for cross-border debtors choosing between jurisdictions.

### Forum Shopping Considerations

| Forum                  | Advantages                                                                  | Disadvantages                                                                                 |
| ---------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **US (SDNY/D.Del.)**   | Mature, predictable law; robust DIP market; sophisticated judges            | Public; creditor committees; US Trustee oversight; potentially long                           |
| **England & Wales**    | Flexible Part 26A; fast administration; pre-pack available; CIGA moratorium | Post-Petrofac fairness requirements; no DIP financing mechanism; CVA no secured bind          |
| **Germany**            | Confidential StaRUG; management control; selective creditor inclusion       | Shorter timelines; no employment/lease termination in StaRUG; shareholder consent uncertainty |
| **Out-of-court (all)** | Fastest; cheapest; confidential                                             | No holdout compulsion; no automatic stay; no court protection                                 |

---

## Module N: Anti-Patterns and Common Pitfalls

The following 21 anti-patterns represent the most common errors and traps encountered by
practitioners in corporate restructuring across US, UK, and German law.

---

### AP-01: Triggering the Preference Window Through Late Payments

**Problem**: In the 90 days before a Chapter 11 filing (1 year for insiders), large payments
to creditors are preference-exposed under §547. Companies in distress often make last-ditch
payments to critical suppliers, landlords, or lenders — creating significant avoidance exposure.

**Consequence**: Trustee/DIP may claw back payments; payees may need to return funds and instead
file unsecured claims; can destabilize vendor relationships if trade creditors are targeted.

**Mitigation**: Analyze all significant payments in the 90-day window before filing. Assert
ordinary-course and contemporaneous-exchange defenses proactively. Seek critical vendor orders
(judicially created exception for truly essential suppliers; courts vary in granting).

---

### AP-02: Fraudulent Transfer Exposure from Pre-Filing Asset Transfers or Dividends

**Problem**: Asset transfers, dividend recapitalizations, and intercompany payments made while
the debtor was insolvent or rendered insolvent may be unwound under §548 (2-year lookback) or
state fraudulent transfer law via §544 (4-6 year lookback). LBO target companies are
particularly vulnerable: pledging target assets to secure acquisition financing is a classic
constructive fraudulent transfer if the target was insolvent at closing.

**Consequence**: Lenders who received payments on a fraudulently transferred lien may lose
the lien; sellers who received LBO purchase price may face disgorgement.

**Mitigation**: Conduct solvency analysis at time of each suspect transaction. Obtain solvency
opinion from independent financial advisor. Document business purpose. Ensure reasonably
equivalent value exchange.

---

### AP-03: Undervalued Section 363 Sales — Creditor Challenges

**Problem**: A §363 sale approved by the court is generally entitled to good-faith purchaser
protections and finality (§363(m)). However, if the sale process was inadequate — insufficient
marketing, no auction, undisclosed stalking horse side deals, collusive bidding arrangements —
courts may refuse good-faith protections and allow challenges.

**Consequence**: Secured creditors or unsecured committee may object at the sale hearing; delays
increase professional costs and deteriorate going-concern value; buyer walks if certainty lost.

**Mitigation**: Run a proper competitive marketing process with investment banker; document all
marketing efforts; ensure stalking horse was selected through a fair process; no side agreements
with winning bidder that were not disclosed to court; no bid-rigging (§363(n) permits unwinding
of sale influenced by undisclosed agreements among bidders).

---

### AP-04: DIP Financing That Entrench Lenders and Foreclose Reorganization

**Problem**: DIP lenders (often existing secured lenders) negotiate milestone provisions and
covenants that effectively dictate the outcome of the case — forcing a §363 sale to the DIP
lender or mandating a plan that benefits the DIP lender — before the estate has had time to
explore reorganization alternatives or run a genuine sale process.

**Consequence**: Unsecured creditor committee objects to DIP at final hearing; court may modify
milestones to provide adequate time for plan process; judge may scrutinize DIP terms as a
"sub rosa plan" imposing an outcome without §1129 confirmation.

**Mitigation**: DIP lenders should ensure milestones are commercially reasonable and provide
genuine marketing periods. Debtors should push back on milestones that leave no meaningful
planning time. Courts increasingly apply heightened scrutiny to DIP terms that functionally
determine case outcome without plan confirmation.

---

### AP-05: Excessive DIP Roll-Ups — Sacred Rights Violations

**Problem**: Large roll-up ratios (3:1, 4:1) convert prepetition debt to super-priority post-
petition status, dramatically improving the roll-up lender's position at the expense of other
creditors. Where the roll-up is non-pro-rata (only some prepetition lenders participate),
remaining prepetition lenders are primed without consent — potentially violating sacred rights
(pro-rata) provisions in the syndicated credit agreement.

**Consequence**: Excluded prepetition lenders object to DIP; claim the roll-up is an improper
priming; may seek to enforce contractual sacred rights in state court; case disruption and
litigation costs.

**Mitigation**: Ensure roll-up is pro-rata among all holders of the applicable prepetition
facility; obtain consent of requisite majority under existing credit agreement before filing;
keep roll-up ratios commercially defensible (2:1 generally accepted; 3:1+ requires strong
justification).

---

### AP-06: Exclusivity Period Misuse

**Problem**: Chapter 11 debtors have an exclusive right to file a plan for 120 days (§1121(b)),
extendable up to 18 months (§1121(d)(2)). Some debtors use exclusivity as a shield — repeatedly
extending exclusivity to prevent creditor plans while failing to advance their own reorganization.
Creditors may become trapped, burning through professional fees, while the debtor delays.

**Consequence**: Unsecured creditor committee, frustrated with delay, moves to terminate
exclusivity; court may grant termination if debtor cannot demonstrate good-faith progress toward
a confirmable plan; contested exclusivity litigation increases cost.

**Mitigation**: Debtors should use exclusivity to negotiate in good faith, not as a stalling
tactic. Courts will terminate exclusivity where debtor has failed to make meaningful progress.
Monitor §1121(d) case law in the relevant venue for tolerance levels.

---

### AP-07: Good-Faith Violation in Plan Confirmation

**Problem**: §1129(a)(3) requires a plan to be proposed in "good faith." A plan designed
primarily to benefit insiders, to achieve an improper purpose, or to strip dissenting creditors
without legitimate reorganization objective may fail the good-faith test.

**Consequence**: Plan denied confirmation; debtor must renegotiate; creditors may move for
conversion to Chapter 7.

**Mitigation**: Plan must reflect genuine reorganization purpose, not primarily serve to benefit
insiders or frustrate creditor rights. Document the business rationale for each element of the
plan. Ensure plan is not a de facto liquidation disguised as a reorganization.

---

### AP-08: New Value Exception Failure — No Market Testing

**Problem**: The new value exception to the absolute priority rule allows existing equity to
retain interest if they contribute "money or money's worth" that is new, substantial, necessary,
and reasonably equivalent to value retained. Courts in several circuits require the new value
contribution to be market-tested — i.e., competing bids invited to demonstrate no higher value
can be obtained.

**Consequence**: Plan denied confirmation; existing equity cannot retain interest without
paying market value (i.e., essentially what any bidder would pay at arm's length).

**Mitigation**: Structure new value contribution as a competitive process where equity's bid
is tested against third-party offers. Follow In re Philadelphia Newspapers principles. Engage
experienced restructuring counsel in the relevant circuit.

---

### AP-09: CVA Arbitrary Discount on Landlord Claims — Unfair Prejudice

**Problem**: UK CVAs commonly apply discounts to landlord claims for voting purposes (since
future rent obligations are contingent). In _In re Regis_ (2021), a 75% blanket discount on
landlord claims was held unfair — the discount must be a reasonable estimate of minimum value,
not an arbitrary number designed to minimize landlord voting power.

**Consequence**: Court revokes CVA on unfair prejudice grounds (IA 1986 §6); debtor must restart
process; creditor confidence destroyed; administration or liquidation may follow.

**Mitigation**: Any discount applied to contingent landlord claims must be supportable as a
reasonable estimate of minimum claim value. Engage surveyors to value landlord claims. Document
the valuation methodology in the CVA proposal.

---

### AP-10: Pre-Pack Administration — Connected Party Without Independent Evaluator

**Problem**: Since April 2021, UK connected-party pre-packs (where assets are sold to existing
directors, shareholders, or related parties) without creditor approval or an independent evaluator
opinion violate the Administration (Restrictions on Disposal) Regulations 2021.

**Consequence**: Transaction may be voidable; administrator personally liable; regulatory action
by RPB (Recognized Professional Body); criminal sanctions in egregious cases.

**Mitigation**: For any connected-party pre-pack, obtain either (a) written creditor approval
(consent from majority of creditors) before completion, or (b) a written opinion from an
independent evaluator (from the Pre-Pack Pool) that the transaction is reasonable for creditors.
Document all marketing efforts per SIP 16.

---

### AP-11: UK Part 26A Restructuring Plan — Insufficient Stakeholder Engagement Post-Petrofac

**Problem**: The traditional approach — bilateral negotiation between plan company and an ad hoc
group of senior creditors, then imposing plan on out-of-the-money classes — no longer satisfies
the English court's sanction test post-_Saipem v Petrofac_ [2025] EWCA Civ 821. Failure to
genuinely engage junior classes and out-of-the-money creditors from the outset will defeat sanction.

**Consequence**: Court declines to sanction the restructuring plan; debtor forced to restart
process (potentially in administration); time and cost wasted; restructuring value destroyed.

**Mitigation**: Engage ALL creditor classes from the outset of plan negotiations, not just the
relevant/senior class. Ensure new money terms are market-tested. Document why any unequal
distribution of restructuring benefits is justified. Ensure work fees bear reasonable relationship
to actual work performed (not disguised equity upside as in Petrofac).

---

### AP-12: German StaRUG — Including Ineligible Claims

**Problem**: StaRUG does not permit restructuring of tax claims, claims arising from criminal
liability, tort damages, employment-related claims, or pension obligations. Attempting to include
these claims in a StaRUG plan will invalidate the plan or require exclusion.

**Consequence**: StaRUG plan fails confirmation; debtor must file for Insolvenzverfahren if
these claims are material to the restructuring.

**Mitigation**: Map all claims before selecting StaRUG. If material claims fall outside StaRUG's
scope (taxes, pensions, employment), consider whether Schutzschirmverfahren or Insolvenzverfahren
is more appropriate — or use a hybrid (StaRUG for financial debt restructuring + separate
processes for out-of-scope claims).

---

### AP-13: StaRUG — Shareholder Consent Ambiguity (GmbH vs. AG)

**Problem**: Courts remain divided on whether a StaRUG plan affecting shareholders' economic
rights requires shareholder approval (in addition to board approval). For a GmbH, the board
(Geschäftsführer) typically acts for the company; for an AG, the supervisory board and
potentially shareholders may need to consent. Proceeding without clarity creates plan challenge risk.

**Consequence**: Shareholder challenge to plan confirmation; delay; potential invalidity.

**Mitigation**: Obtain shareholder consent by contract (as in LEONI) or seek early legal opinion
on the specific corporate form. Consult specialist German restructuring counsel before filing.

---

### AP-14: Tax Trap — COD Income Without Bankruptcy Protection (Out-of-Court Workout)

**Problem**: In an out-of-court debt restructuring (workout), CODI can only be excluded to the
extent the debtor was insolvent immediately before the discharge (insolvency exclusion, §108(a)
(1)(B)). If the debtor was balance-sheet solvent (e.g., significant asset values), the CODI
above the insolvency cushion is fully taxable — potentially creating a massive tax bill at the
worst possible moment.

**Consequence**: Company receives large tax bill on phantom income from debt forgiveness; cannot
pay tax; forced to file for bankruptcy anyway — but now has exhausted resources on failed workout.

**Mitigation**: Always model the tax consequences of any proposed debt restructuring before
agreeing to out-of-court terms. Compare insolvency cushion to proposed debt forgiveness. If
CODI exceeds insolvency cushion, consider whether a prepackaged Chapter 11 (with bankruptcy
exclusion from §108(a)(1)(A)) would be more tax-efficient.

---

### AP-15: Tax Trap — Section 382 NOL Destruction in Debt-for-Equity Swap

**Problem**: A debt-for-equity swap causes an ownership change under IRC §382 (>50% change in
ownership within 3 years). The §382 annual limitation on pre-change NOLs equals the value of
the company's equity immediately before the ownership change × the long-term tax-exempt rate.
If the company is distressed, this value may be near zero, making the §382 limitation
essentially zero — destroying all pre-change NOLs.

**Consequence**: NOLs that the restructured company needed to offset future income tax are
eliminated or rendered useless; future tax liabilities increase dramatically; business plan
projections based on NOL utilization are wrong.

**Mitigation**: Analyze §382 impact before finalizing debt-for-equity structure. If in Chapter 11,
structure plan to qualify for §382(l)(5) bankruptcy exception (historic creditors own ≥50% of
post-emergence equity; no NOLs used in 2 years before filing). If §382(l)(5) unavailable, use
§382(l)(6) and model the resulting limitation against projected taxable income.

---

### AP-16: Debt Modification Triggering OID — Phantom Income for Lenders

**Problem**: Even routine modifications to debt terms (interest rate change, PIK election,
covenant waiver, fee payment) may constitute a "significant modification" under Treas. Reg.
§1.1001-3, triggering a deemed exchange of old debt for new debt. If new debt is issued at a
discount (fair value below face value), OID arises — phantom interest income taxable to lender
over the life of the instrument, even without cash payments.

**Consequence**: Lenders face unexpected taxable income on amendments they thought were
administrative; may demand "gross-up" payments or refuse to amend; transaction economics
disrupted.

**Mitigation**: Before agreeing to any debt modification, conduct a significant modification
analysis. If modification is deemed significant, model OID consequences. Consider whether any
modification can be structured to avoid OID (e.g., keeping effective yield within 25 basis
points of original). Consult tax counsel before execution.

---

### AP-17: Intercreditor Voting Waivers — Second Lien Lender Cannot Block DIP

**Problem**: Most first/second lien intercreditor agreements contain provisions where the second
lien lender waives the right to object to any DIP financing or cash collateral use consented to
by the first lien lender. Second lien lenders sometimes forget or overlook these waivers when a
DIP is presented, and attempt to object — only to learn their objection rights were waived at
the intercreditor level.

**Consequence**: Court enforces intercreditor waiver and overrules second lien objections; second
lien lender loses leverage at a critical stage of the case; may also have waived adequate
protection rights.

**Mitigation**: Second lien lenders must review their intercreditor agreement before any Chapter
11 filing and understand exactly what rights they have waived. If rights are waived, focus on
ensuring adequate protection payments are not waived and plan confirmation participation is
preserved. Negotiate intercreditor agreements carefully at origination.

---

### AP-18: Liability Management Exercise — Excluded Lenders Litigate

**Problem**: Uptier transactions that subordinate non-participating lenders without their consent
create litigation risk. The Serta Simmons 5th Circuit decision (2024) found the uptier violated
pro-rata provisions. Excluded lenders in other circuits have succeeded in challenging LMEs on
breach of contract grounds. Even where LMEs are upheld, litigation costs and delays may negate
the economic benefit.

**Consequence**: Court may unwind the LME; debtor's restructuring strategy collapses; excluded
lenders recover full priority; debtor may need to file Chapter 11 anyway.

**Mitigation**: Before executing any LME, conduct careful analysis of the credit agreement
language — particularly pro-rata, sacred rights, and "open market purchase" provisions. Post-
Serta, borrowers are restructuring LMEs to avoid direct priming of non-participating lenders.
Consider whether a prepackaged bankruptcy achieves the same result with greater certainty.

---

### AP-19: Insolvenzverwalter Conflicts — Liquidation Bias

**Problem**: German insolvency administrators (Insolvenzverwalter) are compensated as a
percentage of assets realized. This creates a structural incentive toward liquidation (higher
asset realizations) over restructuring (ongoing business value). Even under ESUG reforms,
concerns remain that preliminary administrators appointed by the court may not be aligned with
restructuring outcomes.

**Consequence**: Administrator recommends liquidation when restructuring would deliver higher
value for creditors; going-concern value destroyed; employees lose jobs.

**Mitigation**: Use Eigenverwaltung or Schutzschirmverfahren where possible (management retains
control; Sachwalter acts as monitor, not manager). Under ESUG, creditor committee can influence
Insolvenzverwalter selection. Consider StaRUG for pre-insolvency financial restructuring where
management control is paramount.

---

### AP-20: ABC Without Automatic Stay — Involuntary Bankruptcy Risk

**Problem**: ABC proceedings lack the federal automatic stay of Chapter 11/7. During the ABC
process, any creditor owed at least $18,600 (or three or more creditors owed $18,600 in
aggregate) may file an involuntary Chapter 7 bankruptcy petition against the debtor. If the
court grants the petition, the ABC is superseded by federal bankruptcy, disrupting the assignee's
work and adding cost and delay.

**Consequence**: ABC converted to Chapter 7 by hostile creditor; assignee's authority challenged;
asset sales disrupted; additional professional fees; creditors who preferred ABC's speed and
flexibility now face federal bankruptcy timeline.

**Mitigation**: Consider whether the creditor base will cooperate with an ABC or whether a
hostile creditor is likely to file involuntary. If involuntary risk is high, pre-emptive Chapter
7 or Chapter 11 filing may be preferable. In California ABCs, expedited sale process can close
before hostile creditor can organize. Obtain consent from major creditors before initiating ABC.

---

### AP-21: Receivership Without Adequate Protection of Junior Creditors

**Problem**: A secured creditor-initiated receivership focuses on realizing the secured
creditor's collateral. Junior secured creditors and unsecured creditors may receive no notice,
no adequate protection, and no meaningful participation. State court receivers appointed ex parte
may take drastic actions (lock out directors, freeze accounts) before other parties can respond.

**Consequence**: Junior creditors receive no value; debtor's management loses control without
Chapter 11's DIP protections; employee wages and trade obligations unpaid; no structured claim
resolution process.

**Mitigation**: Junior creditors facing a senior creditor receivership should consider whether
to support a voluntary Chapter 11 filing (which triggers automatic stay and prevents receivership
appointment) or intervene in the receivership action immediately. Debtors facing imminent
receivership should evaluate whether voluntary Chapter 11 filing (even emergency) is preferable
to loss of management control in receivership.

---

## Output Format

### Standard Restructuring Analysis Report

Structure every restructuring analysis as follows:

```
CORPORATE RESTRUCTURING ANALYSIS
Date: [date]
Jurisdiction(s): [US / UK / DE / Multi]
Perspective: [Debtor / Secured Creditor / Unsecured Committee / Buyer / Neutral]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. SITUATION OVERVIEW
   - Capital structure summary
   - Current solvency status
   - Immediate pressures and triggers
   - Strategic objective

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. MECHANISM OPTIONS MATRIX
   [Table comparing available mechanisms with pros/cons for this situation]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. RECOMMENDED PATH
   - Primary recommendation with rationale
   - Alternative(s) if primary not available
   - Key conditions for success

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. KEY LEGAL ISSUES
   - Jurisdiction-specific statutory analysis
   - Relevant case law
   - Unresolved legal questions

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. ANTI-PATTERNS IDENTIFIED
   [Each anti-pattern: name | risk level | mitigation]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. TAX CONSIDERATIONS
   - COD income exposure
   - §382 / NOL analysis
   - Jurisdiction-specific issues

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7. TIMELINE AND NEXT STEPS
   - Recommended immediate actions
   - Key milestones and deadlines
   - Advisors required

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
8. GLASS BOX AUDIT TRAIL
   - Modules activated: [list]
   - Key statutory provisions relied upon: [list]
   - Anti-patterns checked: [AP-01 through AP-21]
   - Assumptions made: [list]
   - Items requiring specialist verification: [list]
```

### Severity Notation

Use consistent severity markers throughout analysis:

- **GREEN** — Low risk; standard practice; well-settled law
- **YELLOW** — Moderate risk; requires attention; unsettled or jurisdiction-dependent
- **RED** — High risk; significant exposure; escalate to qualified counsel immediately
- **STRUCTURAL** — Fundamental issue with chosen mechanism; requires mechanism reassessment

---

## Key Statutory Citations Quick Reference

### United States

| Provision             | Subject                                            |
| --------------------- | -------------------------------------------------- |
| 11 U.S.C. §362        | Automatic stay                                     |
| 11 U.S.C. §363        | Use, sale, lease of property (§363 sales)          |
| 11 U.S.C. §364        | Obtaining credit (DIP financing)                   |
| 11 U.S.C. §365        | Executory contracts and unexpired leases           |
| 11 U.S.C. §502        | Allowance of claims or interests                   |
| 11 U.S.C. §510        | Subordination                                      |
| 11 U.S.C. §547        | Preferences (90-day / 1-year lookback)             |
| 11 U.S.C. §548        | Fraudulent transfers (2-year lookback)             |
| 11 U.S.C. §1121       | Who may file plan; exclusivity                     |
| 11 U.S.C. §1123       | Contents of plan                                   |
| 11 U.S.C. §1125       | Postpetition disclosure and solicitation           |
| 11 U.S.C. §1126       | Acceptance of plan                                 |
| 11 U.S.C. §1129       | Confirmation of plan (including §1129(b) cramdown) |
| 11 U.S.C. §1191       | Subchapter V confirmation and cramdown             |
| 28 U.S.C. §1408       | Venue for bankruptcy cases                         |
| IRC §108              | COD income exclusions (bankruptcy/insolvency)      |
| IRC §382              | NOL limitation on ownership change                 |
| Treas. Reg. §1.1001-3 | Significant modification of debt instruments       |

### United Kingdom

| Provision                                           | Subject                                                  |
| --------------------------------------------------- | -------------------------------------------------------- |
| Insolvency Act 1986 Schedule B1                     | Administration                                           |
| IA 1986 Part I (§§1-7)                              | Company Voluntary Arrangements                           |
| IA 1986 §6                                          | CVA challenge (unfair prejudice / material irregularity) |
| Companies Act 2006 Part 26                          | Schemes of arrangement                                   |
| Companies Act 2006 Part 26A                         | Restructuring plans (CIGA 2020)                          |
| CA 2006 §901G                                       | Cross-class cramdown power                               |
| Corporate Insolvency and Governance Act 2020        | CIGA — Part 26A; moratorium                              |
| SIP 16                                              | Pre-pack administration disclosure                       |
| Administration (Restrictions on Disposal) Regs 2021 | Connected party pre-packs                                |

### Germany

| Provision      | Subject                                                                    |
| -------------- | -------------------------------------------------------------------------- |
| InsO §15a      | Director obligation to file for insolvency                                 |
| InsO §§17-19   | Insolvency triggers (illiquidity, imminent illiquidity, over-indebtedness) |
| InsO §§217-269 | Insolvenzplan                                                              |
| InsO §§270-285 | Eigenverwaltung                                                            |
| InsO §270b     | Schutzschirmverfahren                                                      |
| StaRUG §§1-100 | Stabilisierungs- und Restrukturierungsrahmen                               |
| StaRUG §26     | Cross-class cramdown in StaRUG                                             |
| KStG §8c       | Limitation of loss carryforwards on ownership change                       |

---

## Key Case Law Reference

### United States

| Case                                                            | Principle                                             |
| --------------------------------------------------------------- | ----------------------------------------------------- |
| _RadLAX Gateway Hotel v. Amalgamated Bank_, 566 U.S. 639 (2012) | Credit bid right in §363 sale vs. plan                |
| _In re Serta Simmons Bedding_ (5th Cir. 2024)                   | Uptier LME violated pro-rata sacred rights            |
| _Mission Product Holdings v. Tempnology_, 139 S.Ct. 1652 (2019) | Executory contract rejection = breach, not rescission |
| _In re Philadelphia Newspapers_ (3d Cir. 2010)                  | New value exception requires market testing           |
| _Czyzewski v. Jevic Holding Corp._, 580 U.S. 451 (2017)         | Priority-skipping structured dismissal prohibited     |
| _In re DBSD North America_ (2d Cir. 2011)                       | Gifting plan cannot skip intermediate class           |
| _In re 203 N. LaSalle Street Partnership_ (7th Cir. 2000)       | New value exception standards                         |

### United Kingdom

| Case                                                      | Principle                                                                 |
| --------------------------------------------------------- | ------------------------------------------------------------------------- |
| _Saipem & Ors v Petrofac Limited_ [2025] EWCA Civ 821     | Fairness to all classes; burden on plan company; new money market testing |
| _In re New Look Retailers_ [2021]                         | Differential landlord treatment in CVA not inherently unfair              |
| _In re Regis UK Ltd_ [2021]                               | Arbitrary landlord claim discount = unfair prejudice; CVA revoked         |
| _Assenagon Asset Management v IBRC_ [2012] EWHC 2090 (Ch) | Exit consent strip = improper use of voting power                         |
| _Re Hunkemöller_ (2025-2026 proceedings)                  | LME validity under English law (pending)                                  |

### Germany

| Case                     | Principle                                                                    |
| ------------------------ | ---------------------------------------------------------------------------- |
| _LEONI AG_ StaRUG (2023) | Large-scale StaRUG with €1B+ financial debt; equitization to anchor investor |
| _Galapagos_ (ECJ 2024)   | First insolvency filing blocks jurisdiction in other EU member states        |
| _Varta AG_ (2024)        | Shareholder disputes in StaRUG; management vs. equity holder conflicts       |

---

## Glossary of Key Terms

| Term                                      | Jurisdiction | Definition                                                                                                                                             |
| ----------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Absolute Priority Rule (APR)              | US           | Under §1129(b), junior classes receive nothing unless senior classes paid in full (or senior class consents)                                           |
| Adequate Protection                       | US           | Protection of secured creditor's interest in collateral during automatic stay (cash payments, replacement liens, or indubitable equivalent)            |
| Administration                            | UK           | Court-supervised process where administrator manages company with goal of rescue, better outcome, or distribution to secured/preferential creditors    |
| Automatic Stay                            | US           | Injunction taking effect immediately upon bankruptcy filing; stops all collection actions, foreclosures, and litigation against debtor or its property |
| ABC (Assignment for Benefit of Creditors) | US (state)   | Voluntary state law liquidation; debtor transfers assets to assignee who liquidates and pays creditors                                                 |
| CODI / COD Income                         | US/UK        | Cancellation of Debt Income; taxable income arising from forgiveness or reduction of debt                                                              |
| Cramdown                                  | US/UK/DE     | Confirmation of a plan over the objection of a dissenting class; "cram down" imposes plan on non-consenting creditors                                  |
| Credit Bid                                | US           | Secured creditor's right to bid the amount of its secured claim at a §363 auction without paying cash                                                  |
| CVA                                       | UK           | Company Voluntary Arrangement; unsecured creditor compromise requiring 75% by value approval; does not bind secured creditors without consent          |
| DIP Financing                             | US           | Debtor-in-possession financing; post-petition credit facility with super-priority administrative claim and lien rights                                 |
| Drohende Zahlungsunfähigkeit              | DE           | Imminent illiquidity; trigger for StaRUG eligibility and optional InsO filing                                                                          |
| Eigenverwaltung                           | DE           | German debtor-in-possession equivalent; management retains control; Sachwalter appointed as monitor                                                    |
| Equitization                              | All          | Conversion of debt into equity as part of a restructuring plan or agreement                                                                            |
| Exclusivity Period                        | US           | Statutory period (120 days, extendable to 18 months) during which only the debtor may file a plan of reorganization                                    |
| Exit Consent                              | US/UK        | In a bond exchange offer, tendering holders amend remaining notes to remove covenants — pressuring non-tendering holdouts                              |
| Forbearance Agreement                     | All          | Short-term agreement by creditor not to exercise default remedies while restructuring is negotiated                                                    |
| Free and Clear                            | US           | §363(f) principle — assets may be sold in bankruptcy free of all liens, claims, and encumbrances                                                       |
| Insolvenzplan                             | DE           | German plan of reorganization filed in formal insolvency; equivalent to US plan of reorganization                                                      |
| Insolvenzverfahren                        | DE           | German formal insolvency proceedings; Insolvenzverwalter (administrator) appointed; assets realized or plan confirmed                                  |
| Intercreditor Agreement                   | All          | Contract governing priority, enforcement rights, and voting between lenders of different seniority                                                     |
| LMA                                       | UK/EU        | Loan Market Association; publishes standard European leveraged finance and distressed trading documentation                                            |
| LME                                       | All          | Liability Management Exercise; out-of-court transaction restructuring debt via majority provisions in credit agreement                                 |
| LSTA                                      | US           | Loan Syndications and Trading Association; publishes standard US leveraged loan and distressed trading documentation                                   |
| NOL                                       | US           | Net Operating Loss; carried forward to offset future taxable income; subject to §382 limitation on ownership change                                    |
| OID                                       | US           | Original Issue Discount; discount between face value and issue price of debt; accretes as interest income over life                                    |
| Plan of Reorganization                    | US           | Court-confirmed plan binding all creditors; specifies treatment of each class of claims and interests                                                  |
| Pre-Pack Administration                   | UK           | Sale arranged before administration appointment; completed immediately upon appointment                                                                |
| Priming Lien                              | US           | Post-petition lien granted senior to existing prepetition lien on same collateral; requires adequate protection of primed creditor                     |
| Roll-Up                                   | US           | Conversion of prepetition debt into post-petition DIP facility, gaining super-priority status                                                          |
| RSA (Restructuring Support Agreement)     | US/UK        | Agreement binding signatories to vote for a specific restructuring plan                                                                                |
| Sachwalter                                | DE           | German court-appointed monitor in Eigenverwaltung or Schutzschirmverfahren; oversees debtor-in-possession                                              |
| Schutzschirmverfahren                     | DE           | German "protective umbrella" procedure allowing debtor to prepare Insolvenzplan with court protection for up to 3 months                               |
| Stalking Horse                            | US           | Initial bidder in §363 auction who sets floor price and receives bid protections                                                                       |
| StaRUG                                    | DE           | Stabilisierungs- und Restrukturierungsrahmen; German pre-insolvency preventive restructuring framework (effective Jan 1, 2021)                         |
| Subchapter V                              | US           | SBRA 2019 fast-track Chapter 11 for small businesses (<$2.725M debt); APR does not apply; no creditors' committee                                      |
| Uptier                                    | US/UK        | LME where majority of lenders exchange debt for new senior debt, priming minority non-participating lenders                                            |
| Workout                                   | All          | Out-of-court negotiated restructuring of debt terms without formal insolvency proceedings                                                              |
| Zahlungsunfähigkeit                       | DE           | Cash-flow insolvency; triggers mandatory InsO filing obligation within 3 weeks                                                                         |
| Überschuldung                             | DE           | Over-indebtedness (liabilities exceed assets + no positive going-concern prognosis); triggers mandatory InsO filing within 6 weeks                     |

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis drawing on:

- US Bankruptcy Code (Title 11 U.S.C.), PACER case research, and restructuring practitioner
  guides (Weil, Goodhart & Manges; Kirkland & Ellis; Milbank restructuring memos)
- UK Insolvency Act 1986, Companies Act 2006 Part 26A (CIGA 2020), SIP 16, and High Court
  restructuring plan decisions (_Saipem v Petrofac_ [2025] EWCA Civ 821, _New Look_, _Regis_)
- German InsO and StaRUG 2021 with reference to LEONI (2023), Varta AG (2024), and Galapagos
  ECJ (2024) decisions
- LSTA and LMA distressed trading and leveraged loan documentation standards
- Web research conducted March 2026 on DIP financing market practice, LME developments
  post-_Serta Simmons_ (5th Cir. 2024), and StaRUG market adoption
- Structural patterns from `legalcode-contract-review` (reference standard), `legalcode-venture-financing-suite`,
  and `legalcode-shareholders-agreement-review` skills

Attribution: Legalcode original synthesis. Not derived from any third-party skill.
