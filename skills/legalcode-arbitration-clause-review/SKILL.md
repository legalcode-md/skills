---
name: legalcode-arbitration-clause-review
description: Review and analyze arbitration clauses for enforceability, pathological defects, and commercial
  suitability — identify unclear scope, missing essential elements, inconsistent provisions, and jurisdiction-specific
  risks. Use when reviewing dispute resolution provisions in commercial contracts, evaluating arbitration
  clauses for New York Convention enforceability, assessing institutional arbitration clause compliance
  (ICC, LCIA, AAA/ICDR, SIAC, HKIAC, SCC), checking for multi-tiered escalation clause defects, or advising
  on seat selection and procedural adequacy.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review and analyze arbitration clauses for enforceability, pathological defects, and commercial suitability — identify unclear scope, missing essential elements, inconsistent provisions, and jurisdiction-specific risks. Use when reviewing dispute resolution provisions in commercial contracts, evaluating arbitration clauses for New York Convention enforceability, assessing institutional arbitration clause compliance (ICC, LCIA, AAA/ICDR, SIAC, HKIAC, SCC), checking for multi-tiered escalation clause defects, or advising on seat selection and procedural adequacy. Covers ad hoc and institutional arbitration, emergency arbitrator provisions, consolidation rights, joinder clauses, confidentiality obligations, cost allocation mechanisms, and waiver provisions (class action, jury, punitive damages). Detects pathological clauses (Eisemann defects), forum non conveniens risks, and consumer/employment-specific enforceability issues under US federal law (FAA, EFAA) and state unconscionability doctrines. Produces severity-classified findings (GREEN/YELLOW/RED), redline suggestions with fallback positions, and a Glass Box audit trail. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers for US, UK, EU, Singapore, Hong Kong, and civil law systems. Integrates with legalcode-contract-review for full contract analysis and legalcode-mcp for legal authority verification.


# Legalcode Arbitration Clause Review

> **Disclaimer**: This skill provides a framework for AI-assisted arbitration clause review. It
> does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before use. Arbitration law varies
> significantly by jurisdiction and evolves frequently; verify current applicability before
> relying on any provision described here. Statutory and case law references cited from memory
> carry hallucination risk — verify against authoritative sources before relying on them.

## Purpose and Scope

This skill reviews arbitration and dispute resolution clauses in commercial contracts to identify
enforceability risks, pathological defects, missing essential elements, and misalignment with
the parties' commercial objectives. It produces severity-classified findings, actionable redline
suggestions, and a Glass Box audit trail for traceability.

**Covers:**

- Pathological clause detection (Eisemann's four functions framework)
- Essential element completeness (seat, rules, institution, number of arbitrators, language)
- Multi-tiered dispute resolution clause analysis (negotiation, mediation, arbitration sequencing)
- Institutional arbitration clause compliance (ICC, LCIA, AAA/ICDR, SIAC, HKIAC, SCC, JAMS)
- New York Convention enforceability assessment
- Seat selection analysis and lex arbitri implications
- Consumer and employment arbitration special rules (FAA, EFAA, state unconscionability)
- Emergency arbitrator, consolidation, and joinder provisions
- Confidentiality and cost allocation mechanisms
- Waiver provisions (class action, jury, punitive damages)
- Conflict detection with other contract provisions (forum selection, governing law)

**Does not:**

- Draft complete arbitration agreements from scratch (see drafting-specific skills)
- Provide legal advice or replace qualified counsel
- Replace institutional guidance on model clause usage
- Apply to criminal proceedings or regulatory enforcement actions

**Related skills:**

- `legalcode-contract-review` — Full contract clause-by-clause analysis (includes dispute resolution as one of 14 categories)
- `legalcode-mediation-preparation` — Mediation strategy and preparation
- `legalcode-settlement-negotiation` — Settlement corridor modeling and BATNA analysis

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill with deep coverage of common arbitration frameworks.
The analysis identifies the arbitration seat (juridical seat) and adapts to the applicable
lex arbitri (procedural law governing the arbitration).

[JURISDICTION-SPECIFIC] When localizing, research and apply:

**United States:**

- Federal Arbitration Act (FAA) — 9 U.S.C. § 1 et seq.
- Ending Forced Arbitration of Sexual Assault and Sexual Harassment Act (EFAA) — voids
  mandatory pre-dispute arbitration for claims accruing on or after March 3, 2022
- State unconscionability doctrines (procedural + substantive unconscionability)
- Class action waiver enforceability under Epic Systems Corp. v. Lewis (2018)
- State-specific restrictions (note: California AB 51 enjoined as FAA-preempted)

**United Kingdom:**

- Arbitration Act 1996 (as amended by Arbitration Act 2025)
- Law of the seat as default governing law for arbitration agreement (2025 Act codification)
- Emergency arbitrator recognition
- London as arbitration-friendly seat with extensive case law

**European Union:**

- UNCITRAL Model Law adoption varies by member state
- Brussels I Recast — arbitration exclusion (Article 1(2)(d))
- Consumer protection limitations on arbitration clauses (Directive 93/13/EEC)

**Singapore:**

- International Arbitration Act (Cap 143A)
- SIAC Rules 2025 — expedited procedures, third-party funding disclosure
- Singapore as New York Convention signatory with strong pro-enforcement record

**Hong Kong:**

- Arbitration Ordinance (Cap 609)
- HKIAC Administered Arbitration Rules
- One Country, Two Systems — separate enforcement regime from Mainland China

**Civil Law Systems:**

- Varying approaches to arbitrability of certain disputes
- Mandatory requirements for arbitration agreements (e.g., written form)
- Penalty clause interaction with arbitration costs provisions

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- Multiple valid interpretations of a clause exist
- The user's commercial objectives or risk tolerance are unclear
- The clause intersects with jurisdiction-specific rules requiring localization

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

### Step 1: Accept the Arbitration Clause

Accept the arbitration clause in any of these formats:

- **File**: PDF, DOCX, or other document containing the full contract or just the dispute resolution section
- **Pasted text**: Arbitration clause pasted directly into the conversation
- **Contract review context**: Output from `legalcode-contract-review` with dispute resolution section flagged

If the input is a full contract, locate the dispute resolution provisions first:

- Check for a standalone "Dispute Resolution" or "Arbitration" section
- Check the governing law clause for embedded arbitration provisions
- Check definitions for arbitration-related defined terms
- Check schedules and exhibits for supplemental arbitration terms
- Check incorporated documents (e.g., terms of service, master agreements)

If no arbitration clause is found, report this and ask whether to:

- Analyze the forum selection clause instead
- Draft an arbitration clause recommendation
- Conclude that litigation is the default dispute mechanism

### Step 2: Gather Context

**CLARIFY** — Before beginning the review, ask the user these questions. Present them
as a structured set of options where possible:

1. **Which side are you on?**
   - Options: **Drafting party** (proposing the clause), **Reviewing party** (receiving
     the clause), **Neutral reviewer** (advising on the clause's quality)
   - _Why this matters_: A drafting party wants enforcement certainty; a reviewing party
     wants fairness protections; a neutral reviewer assesses both.

2. **What is the commercial context?**
   - Options: **B2B commercial** (two sophisticated parties), **Consumer contract**
     (one consumer party), **Employment agreement** (employer-employee), **International
     transaction** (cross-border with enforcement considerations), **Domestic transaction**
     (same jurisdiction)
   - _Why this matters_: Consumer and employment arbitration clauses face heightened
     scrutiny and statutory restrictions in many jurisdictions.

3. **What are the enforcement priorities?**
   - Options: **Maximize enforceability** (avoid any risk of clause being struck down),
     **Balance fairness and enforceability** (standard commercial), **Speed and cost
     efficiency** (expedited procedures, sole arbitrator), **Confidentiality** (private
     proceedings, no public record)
   - _Why this matters_: Different priorities lead to different recommendations on seat
     selection, institutional rules, and procedural choices.

4. **Are there related agreements?**
   - Options: **Standalone contract** (no related agreements), **Part of a suite**
     (multiple related agreements — check for inconsistent dispute mechanisms), **Master
     agreement with work orders** (hierarchy to consider)
   - _Why this matters_: Inconsistent arbitration clauses across related agreements
     create fragmented disputes and potential pathological issues.

If the user provides partial context, proceed with what you have but **state your
assumptions explicitly**.

### Step 3: Gather Jurisdiction-Relevant Legal Authority

Identify the seat of arbitration from the clause and determine the applicable lex arbitri.
Then use **legalcode-mcp** to build a working legal reference file.

**Research process:**

1. **Identify the seat** from the clause (e.g., "The seat of arbitration shall be London,"
   "Arbitration shall be held in Singapore"). Note:
   - If no seat is specified, this is a **pathological defect** — flag immediately
   - If the seat conflicts with the venue/hearing location, clarify the distinction
   - If multiple seats are specified, this is an **internal contradiction** defect

2. **Identify the institutional rules** (e.g., ICC Rules, LCIA Rules, AAA/ICDR Rules,
   SIAC Rules, ad hoc under UNCITRAL Rules). Note:
   - If no rules are specified, check whether the institution implies its rules
   - If there is a mismatch (e.g., "SIAC under ICC Rules"), this is a **hybrid clause** defect

3. **Search legalcode-mcp** for jurisdiction-relevant authority:
   - Arbitration legislation of the seat jurisdiction
   - New York Convention status and reservations of enforcement jurisdictions
   - Consumer/employment arbitration restrictions in relevant jurisdictions
   - Recent case law on pathological clause interpretation and severability
   - Institutional rule updates (ICC 2021, LCIA 2020/2025, SIAC 2025, AAA 2025)

4. **Save results** to a local temporary reference file:

   ```markdown
   # Legal Authority Reference — Arbitration Clause Review

   ## Seat: [Jurisdiction]

   ## Institution: [Name and Rules version]

   ## Date Gathered: [date]

   ### Arbitration Legislation

   - [Statute, key provisions relevant to this clause]

   ### New York Convention

   - [Enforcement jurisdiction status, reservations]

   ### Consumer/Employment Restrictions

   - [Applicable statutory restrictions, case law]

   ### Recent Case Law

   - [Case name, citation, holding on clause interpretation]

   ### Institutional Rule Highlights

   - [Relevant rule provisions for this clause type]
   ```

**If legalcode-mcp is not connected:**

- Mark every statutory and case law reference with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with general arbitration law knowledge but flag verification requirements

### Step 4: Essential Elements Check

Analyze the clause against the essential elements required for an enforceable arbitration
agreement. For each element, classify as PRESENT (GREEN), AMBIGUOUS (YELLOW), or MISSING (RED).

| Element                                    | Description                                                                     | Pathological Risk if Absent                       |
| ------------------------------------------ | ------------------------------------------------------------------------------- | ------------------------------------------------- |
| **Intent to arbitrate**                    | Clear, mandatory language requiring arbitration                                 | Clause may be optional or unenforceable           |
| **Scope of disputes**                      | What disputes are covered ("arising out of or in connection with")              | Disputes may fall outside clause                  |
| **Seat of arbitration**                    | Juridical seat determining lex arbitri                                          | Unknown procedural law; court supervision unclear |
| **Arbitration rules**                      | Institutional or ad hoc (UNCITRAL) rules                                        | Procedural gaps; potential deadlock               |
| **Number of arbitrators**                  | One or three (or mechanism to determine)                                        | Delay in constitution; cost uncertainty           |
| **Appointment mechanism**                  | How arbitrators are selected if parties disagree                                | Deadlock risk; incomplete tribunal                |
| **Language of arbitration**                | Working language for proceedings                                                | Communication issues; translation costs           |
| **Governing law of arbitration agreement** | Law governing the agreement to arbitrate (may differ from seat or contract law) | Validity disputes; separability issues            |

**Additional elements to check:**

- Confidentiality obligations (if confidentiality is a priority)
- Consolidation/joinder rights (for multi-party disputes)
- Emergency arbitrator provisions (for urgent interim relief)
- Cost allocation and fee-shifting
- Time limits and expedited procedures
- Discovery/disclosure scope
- Waiver provisions (class action, jury, punitive damages)
- Survival clause (arbitration survives contract termination)
- Interaction with other dispute resolution mechanisms

### Step 5: Pathological Clause Detection

Apply Eisemann's four-function framework to detect pathological defects. A pathological
clause fails one or more of these core functions:

| Function                                    | Test                                                                     | Common Defects                                                                |
| ------------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| **1. Mandatory effect**                     | Does the clause require arbitration, or is it optional?                  | "May" instead of "shall"; "either party may elect"; optional arbitration      |
| **2. Exclude premature court intervention** | Does the clause prevent courts from hearing disputes before arbitration? | Parallel forum selection clause; "or courts" language; non-exclusive          |
| **3. Empower arbitrators**                  | Can arbitrators be appointed and function?                               | Non-existent institution; unavailable rules; impossible appointment mechanism |
| **4. Enable enforceable award**             | Will the award be enforceable under New York Convention?                 | Non-signatory jurisdiction; unconscionable terms; arbitrability issues        |

**Categories of pathological defects:**

1. **Unavailable forum**: References a non-existent institution or rules
   - Example: "Arbitration under the Acme Arbitration Association" (does not exist)
   - Consequence: May void clause or require court substitution

2. **Bare/blank clause**: States arbitration but omits essential elements
   - Example: "All disputes shall be resolved by arbitration."
   - Consequence: Delay while courts fill gaps; uncertainty

3. **Ambiguous/optional language**: Includes both arbitration and courts, or non-mandatory wording
   - Example: "Disputes may be resolved by arbitration or litigation at either party's election."
   - Consequence: Uncertainty; validity challenges

4. **Internal contradictions**: Conflicting seats, institutions, or rules
   - Example: "Arbitration in New York under the LCIA Rules with the seat in London."
   - Consequence: Confusion over lex arbitri; potential invalidity

5. **Hybrid clauses**: Mismatched institution and rules
   - Example: "Arbitration administered by SIAC under ICC Rules."
   - Consequence: Procedural confusion; institutional rejection

6. **Asymmetric/one-sided**: One party has arbitration rights, other has litigation rights
   - Example: "Company may bring claims in court; Customer must arbitrate."
   - Consequence: Unconscionability challenge (especially consumer/employment)

7. **Overly narrow scope**: Excludes key disputes from arbitration
   - Example: "Disputes regarding payment only shall be arbitrated."
   - Consequence: Related disputes may require separate proceedings

8. **Conflicting provisions**: Contradicts other contract terms
   - Example: Forum selection clause says "exclusive jurisdiction in Delaware courts" but arbitration clause requires ICC arbitration in Paris
   - Consequence: Uncertainty; which prevails?

### Step 6: Institutional Compliance Check

If the clause specifies an arbitration institution, verify compliance with that institution's
model clause and current rules.

#### ICC (International Chamber of Commerce)

**Model clause (2021 Rules):**

> "All disputes arising out of or in connection with the present contract shall be finally
> settled under the Rules of Arbitration of the International Chamber of Commerce by one
> or more arbitrators appointed in accordance with the said Rules."

**Key ICC requirements:**

- [ ] References ICC Rules (not "ICC arbitration" alone)
- [ ] Mandatory language ("shall be finally settled")
- [ ] Broad scope ("arising out of or in connection with")
- [ ] Optional: seat, number of arbitrators, language, governing law

**ICC rule highlights (2021):**

- Award scrutiny by ICC Court (unique among major institutions)
- Emergency arbitrator available unless excluded
- Expedited procedure for claims under USD 3 million (unless excluded)
- Consolidation and joinder permitted under specific conditions

#### LCIA (London Court of International Arbitration)

**Model clause:**

> "Any dispute arising out of or in connection with this contract, including any question
> regarding its existence, validity or termination, shall be referred to and finally
> resolved by arbitration under the LCIA Rules, which Rules are deemed to be incorporated
> by reference into this clause."

**Key LCIA requirements:**

- [ ] References LCIA Rules with incorporation language
- [ ] Covers existence, validity, and termination questions (separability)
- [ ] Optional: seat (defaults to London), number of arbitrators, language

**LCIA rule highlights (2020, updated 2025 for UK Arbitration Act):**

- No award scrutiny (faster awards)
- Hourly rate billing for arbitrators (GBP 250-650/hour)
- Emergency arbitrator codified under 2025 UK Act
- Median total costs (tribunal + admin): USD 117,653 (2017-2024 data)

#### AAA/ICDR (American Arbitration Association / International Centre for Dispute Resolution)

**Model clause (international):**

> "Any controversy or claim arising out of or relating to this contract, or the breach
> thereof, shall be determined by arbitration administered by the International Centre for
> Dispute Resolution in accordance with its International Arbitration Rules."

**Key AAA/ICDR requirements:**

- [ ] Specifies ICDR for international or AAA for domestic US
- [ ] References current rules version
- [ ] Optional: seat, number of arbitrators, language

**AAA/ICDR rule highlights (2025 updates):**

- Fee schedule: USD 1,450 initial + USD 1,150 final for claims under USD 75,000; scales up
- Expedited procedures available
- 2025 updates include longer stays for judicial review, administrative consolidation

#### SIAC (Singapore International Arbitration Centre)

**Model clause (2025 Rules):**

> "Any dispute arising out of or in connection with this contract, including any question
> regarding its existence, validity or termination, shall be referred to and finally
> resolved by arbitration administered by the Singapore International Arbitration Centre
> in accordance with the Arbitration Rules of the Singapore International Arbitration
> Centre for the time being in force, which rules are deemed to be incorporated by
> reference in this clause."

**Key SIAC requirements:**

- [ ] References SIAC administration and SIAC Rules
- [ ] "For the time being in force" ensures current rules apply
- [ ] Optional: seat (defaults to Singapore), number of arbitrators, language

**SIAC rule highlights (2025):**

- Streamlined/expedited procedures with broader scope
- Mandatory third-party funding disclosure
- Enhanced emergency arbitration (available pre-filing)
- Digital case management via SIAC Gateway
- 6-month award deadline for expedited procedure

#### HKIAC (Hong Kong International Arbitration Centre)

**Model clause:**

> "Any dispute, controversy, difference or claim arising out of or relating to this
> contract, including the existence, validity, interpretation, performance, breach or
> termination thereof or any dispute regarding non-contractual obligations arising out of
> or relating to it shall be referred to and finally resolved by arbitration administered
> by the Hong Kong International Arbitration Centre under the HKIAC Administered
> Arbitration Rules in force when the Notice of Arbitration is submitted."

**Key HKIAC requirements:**

- [ ] References HKIAC administration and HKIAC Rules
- [ ] Broad scope including non-contractual obligations
- [ ] Optional: seat (defaults to Hong Kong), number of arbitrators, language

**HKIAC rule highlights:**

- Arbitrator hourly rate cap: HKD 7,500 (~USD 960) effective late 2025
- Emergency arbitrator available
- Expedited procedure available

### Step 7: Multi-Tiered Clause Analysis

If the clause includes escalation tiers (negotiation, mediation before arbitration), analyze
the enforceability and clarity of each tier.

**Tier analysis framework:**

| Tier            | Required Elements                                                                         | Common Defects                                                                     |
| --------------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Negotiation** | Timeframe, level (operational/executive), notice mechanism                                | Vague "good faith negotiation" without deadline; no escalation trigger             |
| **Mediation**   | Mandatory vs. optional, institution/rules, timeframe, mediator selection, cost allocation | "Agreement to agree" on mediator; no deadline; unclear if condition precedent      |
| **Arbitration** | Full essential elements (Step 4)                                                          | Triggered only after mediation "success" (impossible); no bypass for urgent relief |

**Key questions:**

1. Is each tier mandatory or optional?
2. Are there clear timeframes for each tier?
3. What triggers escalation to the next tier?
4. Is there a bypass for urgent interim relief (emergency arbitrator, court injunctions)?
5. What happens if a party refuses to participate in a tier?
6. Is mediation a condition precedent to arbitration, or merely a procedural step?

**CLARIFY** — If the multi-tiered clause is ambiguous about mandatory vs. optional tiers:

- Ask: "Does your organization intend mediation to be a mandatory step before arbitration,
  or a good-faith effort that can be bypassed if unsuccessful?"
- _Why this matters_: Mandatory mediation as a condition precedent can delay urgent relief;
  optional mediation may be ignored entirely.

### Step 8: Consumer and Employment Special Analysis

If the contract involves a consumer or employee, apply heightened scrutiny.

#### US Federal Law

**Federal Arbitration Act (FAA) — 9 U.S.C. § 1 et seq.**

- Generally enforces arbitration agreements in commerce
- Preempts most state laws restricting arbitration
- Exception: transportation workers (§ 1)

**Ending Forced Arbitration Act (EFAA) — effective March 3, 2022**

- Voids mandatory pre-dispute arbitration for sexual assault and sexual harassment claims
- Claimant has the option to void the arbitration agreement for covered claims
- Court (not arbitrator) decides whether EFAA applies

**Class action waivers:**

- Generally enforceable after Epic Systems Corp. v. Lewis (2018)
- Check for specific carveouts (e.g., PAGA claims in California may not be waivable)

#### Unconscionability Analysis

Apply two-prong unconscionability test (procedural + substantive):

**Procedural unconscionability:**

- [ ] Contract of adhesion (take-it-or-leave-it)?
- [ ] Hidden in fine print or buried in lengthy terms?
- [ ] Unequal bargaining power?
- [ ] No opportunity to negotiate?
- [ ] No meaningful choice?

**Substantive unconscionability:**

- [ ] Asymmetric arbitration rights (company can litigate, consumer must arbitrate)?
- [ ] Prohibitive costs for claimant (filing fees, arbitrator fees)?
- [ ] Inconvenient forum (far from consumer's residence)?
- [ ] Shortened statute of limitations?
- [ ] Limits on discovery that prevent effective claim prosecution?
- [ ] Limits on remedies (no punitive damages, no injunctive relief)?
- [ ] Confidentiality that benefits only one party?

**Severity classification for consumer/employment:**

| Issue                     | GREEN                               | YELLOW                        | RED                                          |
| ------------------------- | ----------------------------------- | ----------------------------- | -------------------------------------------- |
| Cost allocation           | Institution covers consumer's share | Consumer pays filing fee only | Consumer bears arbitrator fees               |
| Forum                     | Consumer's home state/city          | Neutral location              | Company's headquarters far from consumer     |
| Discovery                 | Reasonable for claim value          | Limited but adequate          | Severely restricted                          |
| Remedies                  | All statutory remedies available    | Some limits acceptable        | Punitive damages or injunctive relief barred |
| Asymmetry                 | Mutual arbitration obligation       | Minor asymmetries             | One-sided (company can sue, consumer cannot) |
| Sexual harassment/assault | EFAA-compliant carveout             | No carveout but pre-2022      | Post-March 2022 with no EFAA compliance      |

### Step 9: Seat Selection Analysis

Evaluate the appropriateness of the chosen seat (or recommend one if missing).

**Seat selection factors:**

| Factor                          | Consideration                                                                                                 |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Neutrality**                  | Is the seat neutral to both parties? Avoid party's home jurisdiction if possible                              |
| **Arbitration-friendly courts** | Does the seat have a strong track record of enforcing arbitration agreements and limiting court intervention? |
| **New York Convention**         | Is the seat a signatory? Are there reservations?                                                              |
| **Arbitration legislation**     | Is the lex arbitri modern and based on UNCITRAL Model Law?                                                    |
| **Enforcement jurisdictions**   | Where will the award need to be enforced? Is the seat recognized there?                                       |
| **Practical factors**           | Time zone, language, accessibility, cost of living for hearings                                               |
| **Institutional presence**      | Does the chosen institution have offices/facilities at the seat?                                              |

**Common arbitration-friendly seats:**

- **London** — Extensive case law, Arbitration Act 1996/2025, LCIA headquarters
- **Paris** — ICC headquarters, strong civil law arbitration tradition
- **Singapore** — SIAC headquarters, International Arbitration Act, efficient courts
- **Hong Kong** — HKIAC headquarters, gateway to China (with One Country, Two Systems limitations)
- **New York** — FAA, major financial center, extensive arbitration case law
- **Geneva/Zurich** — Swiss arbitration tradition, neutrality
- **Stockholm** — SCC, historically used for East-West disputes

**Seats to flag with caution:**

- Jurisdictions not party to New York Convention
- Jurisdictions with history of court interference in arbitration
- Jurisdictions with mandatory arbitrability restrictions
- Party's home jurisdiction (may appear biased)

### Step 10: Flag Deviations and Generate Findings

Classify each finding using the three-tier severity system:

### GREEN — Acceptable

The provision is present, clear, and aligns with best practices. No action needed.

**Examples:**

- Model clause from reputable institution used verbatim
- Clear seat selection in arbitration-friendly jurisdiction
- Appropriate number of arbitrators for dispute value
- Mutual arbitration obligations

**Action**: Note for awareness. No redline needed.

### YELLOW — Negotiate

The provision is suboptimal but not necessarily unenforceable. Worth addressing but not
a deal-breaker.

**Examples:**

- Missing optional element that would improve clarity (e.g., language not specified)
- Seat in acceptable but not optimal jurisdiction
- Multi-tiered clause with unclear but interpretable timelines
- Minor asymmetries in a B2B context
- Institutional rules not specified but institution named

**Action**: Generate specific redline language. Provide fallback position. Assess
enforceability risk if unchanged.

### RED — Escalate

The provision is pathological, likely unenforceable, or poses material risk. Requires
immediate attention.

**Examples:**

- Missing seat (pathological)
- Non-existent institution referenced (pathological)
- Internal contradictions between seat and venue
- Consumer arbitration with prohibitive costs
- Employment arbitration without EFAA carveout (post-March 2022)
- Conflicting forum selection clause
- One-sided arbitration in consumer contract
- Optional arbitration language ("may" instead of "shall")

**Action**: Explain specific risk. Provide market-standard alternative. Recommend escalation
or immediate revision.

### Step 11: Generate Redlines

For each YELLOW and RED finding, generate a redline using this format:

```
**Finding**: [Section reference and issue name]
**Severity**: [GREEN / YELLOW / RED]
**Current language**: "[exact quote from the clause]"
**Issue**: [1-2 sentences explaining the problem]
**Proposed redline**: "[specific alternative language]"
**Rationale**: [1-2 sentences suitable for external sharing]
**Legal basis**: [Relevant statute, rule, or principle — or mark [VERIFY]]
**Enforceability impact**: [What happens if this is not fixed]
**Fallback**: [Alternative position if primary redline is rejected]
```

### Step 12: Quality Verification

Before delivering the analysis, run quality checks:

1. **Run Citation Quality Gates** (see Quality Assurance Framework below)
2. **For RED items, run Self-Interrogation** (3-pass adversarial review)
3. **Assign Confidence Scores** to each material finding
4. **Verify completeness**: confirm all essential elements analyzed
5. **Generate Glass Box Audit Trail**

### Step 13: Deliver Output

Structure the final deliverable using the Output Format Template below.

---

## Deviation Severity Classification

### GREEN — Acceptable

The clause element is clear, enforceable, and aligned with best practices for the
contract type and parties involved.

**Criteria (all must be met):**

- Element is present and unambiguous
- Complies with institutional model clause (if applicable)
- No pathological defects
- Appropriate for the commercial context
- No jurisdictional enforceability concerns

### YELLOW — Negotiate

The clause element is suboptimal or unclear but likely enforceable. Improvement would
reduce risk or enhance clarity.

**Criteria (any triggers YELLOW):**

- Element missing but institution/court would supply default
- Minor deviation from model clause
- Ambiguity that courts would likely resolve favorably
- Suboptimal but not unconscionable in context
- Could be improved but not strictly necessary

### RED — Escalate

The clause element is pathological, unenforceable, or poses material risk. Requires
immediate revision or escalation.

**Criteria (any triggers RED):**

- Pathological defect under Eisemann framework
- Missing essential element with no default available
- Likely unconscionable in consumer/employment context
- Conflicting provisions within contract
- Non-existent institution or rules referenced
- Seat in non-New York Convention jurisdiction with enforcement needs
- Post-EFAA employment clause without sexual harassment carveout

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering output. If any gate fails, revise before delivery.

| Gate           | Rule                                                                       | Fail Action                         |
| -------------- | -------------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every legal claim cites a specific statute, rule, or established principle | Add citation or mark "[VERIFY]"     |
| **Format**     | All citations follow consistent format for jurisdiction                    | Fix format                          |
| **Currency**   | Every cited rule version checked (e.g., ICC 2021, SIAC 2025)               | Flag "[CHECK CURRENCY]"             |
| **Domain**     | Analysis stays within identified seat's lex arbitri                        | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated, not hidden                                  | Add confidence qualifier            |

### Self-Interrogation for RED Items

For any finding classified as RED, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**:

- Does the defect classification follow logically from the rule/principle cited?
- Would a court in this seat jurisdiction actually find this clause problematic?
- Is there a counter-argument for enforceability despite the defect?

**Pass 2 — Completeness**:

- Have all relevant arbitration statutes and rules been considered?
- Have leading cases on pathological clauses been reviewed?
- Are there institutional policies that might cure the defect?

**Pass 3 — Challenge**:

- What is the strongest argument that this clause IS enforceable despite the defect?
- Under what circumstances might a court sever the defect and enforce the remainder?
- Is the RED classification proportionate, or is this actually YELLOW with caveats?

If any pass reveals a weakness, revise before delivery. Mark audit trail with
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material finding, assign a confidence level:

| Level        | Range     | Meaning                                                   | Action                                     |
| ------------ | --------- | --------------------------------------------------------- | ------------------------------------------ |
| **Definite** | 0.95-1.0  | Clear statutory/rule violation; established precedent     | State with confidence                      |
| **High**     | 0.80-0.94 | Strong authority; minor interpretation questions          | State with brief caveat                    |
| **Probable** | 0.60-0.79 | Good arguments but reasonable minds could differ          | State with reasoning and contra-indicators |
| **Possible** | 0.40-0.59 | Genuinely uncertain; novel issue or conflicting authority | Flag for counsel review with both sides    |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative                                   | Do not assert; flag "[UNCERTAIN]"          |

---

## Glass Box Audit Trail

Every arbitration clause review output MUST include a Glass Box audit section:

```yaml
glass_box:
  clause_reviewed: "[Section reference or 'Full dispute resolution section']"
  contract_type: "[Commercial / Consumer / Employment / International]"
  user_side: "[Drafting party / Reviewing party / Neutral reviewer]"
  seat_identified: "[Jurisdiction or 'Not specified — pathological']"
  institution_identified: "[Institution or 'Not specified / Ad hoc']"
  rules_version: "[e.g., ICC 2021, SIAC 2025, or 'Not specified']"
  new_york_convention_status: "[Signatory / Not signatory / Signatory with reservations]"
  essential_elements:
    intent_to_arbitrate: "[PRESENT / AMBIGUOUS / MISSING]"
    scope_of_disputes: "[PRESENT / AMBIGUOUS / MISSING]"
    seat_of_arbitration: "[PRESENT / AMBIGUOUS / MISSING]"
    arbitration_rules: "[PRESENT / AMBIGUOUS / MISSING]"
    number_of_arbitrators: "[PRESENT / AMBIGUOUS / MISSING]"
    appointment_mechanism: "[PRESENT / AMBIGUOUS / MISSING]"
    language: "[PRESENT / AMBIGUOUS / MISSING]"
    governing_law_of_agreement: "[PRESENT / AMBIGUOUS / MISSING]"
  pathological_defects_found: "[number] — [list types]"
  multi_tiered_clause: "[Yes / No]"
  consumer_employment_special_rules: "[Applicable / Not applicable]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  findings_summary:
    green: "[number]"
    yellow: "[number]"
    red: "[number]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified legal review"
```

---

## Anti-Patterns

What NOT to do in arbitration clause review:

1. **Ignoring the distinction between seat and venue** — The seat is the legal domicile
   that determines lex arbitri; the venue is just where hearings physically occur. Confusing
   these leads to incorrect analysis of which courts supervise the arbitration.

2. **Assuming institutional rules are interchangeable** — ICC, LCIA, SIAC, and AAA have
   materially different procedures, costs, and default provisions. Analyzing a clause under
   the wrong institution's rules produces incorrect findings.

3. **Overlooking the "for the time being in force" issue** — If a clause references a
   specific rules version (e.g., "ICC Rules 2012"), the outdated rules may apply even if
   newer rules exist. Check whether the clause locks in a version or adopts current rules.

4. **Missing conflicts with other contract provisions** — An arbitration clause can be
   undermined by a forum selection clause, governing law clause, or incorporated terms
   that contradict it. Always check the full contract for conflicts.

5. **Failing to check New York Convention status** — An award is only as good as its
   enforceability. If the seat jurisdiction is not a Convention signatory, or if enforcement
   jurisdictions have reservations, flag this immediately.

6. **Applying US unconscionability analysis to international B2B contracts** — Sophisticated
   commercial parties in international arbitration face much lower unconscionability scrutiny
   than US consumers. Do not import US consumer protections into international commercial
   analysis.

7. **Ignoring EFAA for post-March 2022 employment clauses** — The Ending Forced Arbitration
   Act voids mandatory pre-dispute arbitration for sexual harassment and assault claims.
   Any employment arbitration clause without this carveout is a RED flag.

8. **Treating pathological defects as always fatal** — Courts often try to save arbitration
   clauses through interpretation, severance, or default rules. A pathological defect is
   a serious issue but may not void the entire clause.

9. **Missing multi-tiered clause enforceability issues** — A "negotiate in good faith for
   30 days" tier may be unenforceable for vagueness. Analyze each tier separately for
   clarity and enforceability.

10. **Assuming ad hoc arbitration is always problematic** — Ad hoc arbitration under
    UNCITRAL Rules is common and enforceable. The issue is clauses that specify no rules
    at all, creating procedural gaps.

11. **Overlooking emergency arbitrator provisions** — If urgent relief is contemplated,
    check whether the clause allows emergency arbitrator applications or carves out court
    jurisdiction for interim measures.

12. **Failing to check cost allocation for consumers** — Prohibitive arbitration costs can
    render a consumer arbitration clause unconscionable. Check whether the institution's
    rules, the clause, or applicable law addresses consumer cost protection.

13. **Treating all "either/or" clauses as pathological** — Some clauses allow either party
    to elect arbitration or litigation. While suboptimal, these may be enforceable depending
    on jurisdiction and precise wording.

14. **Missing confidentiality gaps** — Parties often assume arbitration is confidential,
    but confidentiality depends on the institutional rules, lex arbitri, and explicit
    contractual provision. An arbitration clause without confidentiality language may
    not guarantee confidential proceedings.

15. **Ignoring the survival clause issue** — If the underlying contract is terminated or
    found void, does the arbitration clause survive? Check for separability language.

---

## Writing Standards

Apply plain-language discipline to all output:

**For redline rationales** (shared with counterparty's counsel):

- Plain language. No unnecessary jargon.
- Active voice: "This clause requires arbitration" not "Arbitration is required by this clause"
- Short sentences. One point per sentence.
- Specific, not vague: cite the rule or defect type rather than "this may have issues"

**For internal analysis**:

- Same plain-language standards
- May include more technical arbitration law analysis
- Confidence qualifiers where appropriate
- Glass Box audit trail appended

**Quality gates before delivery**:

1. Can a business stakeholder understand the executive summary?
2. Can the counterparty's counsel understand and respond to each redline?
3. Is every legal claim backed by a specific citation (or flagged [VERIFY])?
4. Are any phrases vague, hedging, or ambiguous? If yes, fix.
5. Could any sentence be shorter without losing meaning? If yes, shorten.

---

## External Tool Integration

This skill works with **legalcode-mcp** for legal authority verification.

**With legalcode-mcp connected (preferred):**

- Search for arbitration legislation of the seat jurisdiction
- Verify New York Convention status and reservations
- Check recent case law on pathological clause interpretation
- Verify institutional rule versions and updates
- Mark all legalcode-mcp-sourced citations as VERIFIED in Glass Box

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus on structural analysis and defect detection
- Include prominent notice that legal citations require verification

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Arbitration Clause Review Summary

**Contract**: [contract name/identifier]
**Clause Location**: [section reference]
**Your Side**: [drafting party / reviewing party / neutral]
**Context**: [B2B commercial / consumer / employment / international]
**Date of Review**: [date]

---

## Executive Summary

[2-3 sentence overview: Is this clause enforceable? What are the top issues?]

**Overall Assessment**: [GREEN: Well-drafted, enforceable / YELLOW: Needs improvement /
RED: Material defects requiring revision]

---

## Essential Elements Status

| Element                    | Status             | Notes        |
| -------------------------- | ------------------ | ------------ |
| Intent to arbitrate        | [GREEN/YELLOW/RED] | [brief note] |
| Scope of disputes          | [GREEN/YELLOW/RED] | [brief note] |
| Seat of arbitration        | [GREEN/YELLOW/RED] | [brief note] |
| Arbitration rules          | [GREEN/YELLOW/RED] | [brief note] |
| Number of arbitrators      | [GREEN/YELLOW/RED] | [brief note] |
| Appointment mechanism      | [GREEN/YELLOW/RED] | [brief note] |
| Language                   | [GREEN/YELLOW/RED] | [brief note] |
| Governing law of agreement | [GREEN/YELLOW/RED] | [brief note] |

---

## Pathological Defect Analysis

[List any Eisemann defects found, or "No pathological defects identified"]

---

## Institutional Compliance

**Institution**: [name or "Not specified / Ad hoc"]
**Rules**: [version or "Not specified"]
**Model Clause Compliance**: [Compliant / Deviates — see findings]

---

## Multi-Tiered Analysis (if applicable)

| Tier     | Mandatory? | Timeframe | Clarity           | Issues   |
| -------- | ---------- | --------- | ----------------- | -------- |
| [Tier 1] | [Yes/No]   | [X days]  | [Clear/Ambiguous] | [issues] |
| [Tier 2] | [Yes/No]   | [X days]  | [Clear/Ambiguous] | [issues] |

---

## Consumer/Employment Special Issues (if applicable)

[Analysis of unconscionability, EFAA compliance, cost allocation, etc.]

---

## Findings

### [Finding 1: Title] — [RED/YELLOW/GREEN] | Confidence: [level]

**Current language**: "[quote]"
**Issue**: [description]
**Proposed redline**: "[alternative language]"
**Rationale**: [explanation]
**Fallback**: [alternative if rejected]

[Repeat for each finding]

---

## Redline Priority

**Tier 1 (Must-Fix)**: [list RED items]
**Tier 2 (Should-Fix)**: [list YELLOW items]
**Tier 3 (Nice-to-Have)**: [list minor improvements]

---

## Recommended Actions

1. [Specific action with owner/deadline if applicable]
2. [...]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

To create a jurisdiction-specific variant of this skill:

1. Replace [JURISDICTION-SPECIFIC] markers with verified local arbitration law
2. Replace [VERIFY] tags with verified statutory references
3. Add jurisdiction-specific pathological clause case law
4. Add jurisdiction-specific consumer/employment protections
5. Add local language arbitration clause examples
6. Update frontmatter name and description to reference specific jurisdiction

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis combining:

- Eisemann's four-function framework for pathological clause detection (1974)
- ICC, LCIA, AAA/ICDR, SIAC, HKIAC model clause requirements and 2024-2025 rule updates
- New York Convention enforcement framework
- US FAA and EFAA employment/consumer arbitration law
- Multi-tiered dispute resolution enforceability analysis
- Seat vs. venue distinction and lex arbitri implications
- Web research via perplexity-search (arbitration drafting best practices, institutional
  comparison, enforcement, seat significance, consumer/employment enforceability, costs)
- Quality frameworks adapted from legalcode-contract-review reference standard
