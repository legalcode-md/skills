---
name: legalcode-litigation-budget
description: Create phase-based litigation budgets using LEDES/UTBMS task codes with cost benchmarking,
  variance analysis, and alternative fee arrangement modeling. Use when building matter budgets for civil
  litigation, arbitration, or regulatory proceedings; estimating legal spend by phase (assessment, pleadings,
  discovery, trial, appeal); comparing proposed fees against market benchmarks; structuring alternative
  fee arrangements (fixed, capped, phased, success-based); forecasting total litigation exposure; or preparing
  budget submissions for outside counsel guidelines compliance. Jurisdiction-agnostic with localization
  markers for US, UK, and EU rate environments. Integrates with legalcode-early-case-assessment for matter
  framing and legalcode-damages-calculation for exposure modeling.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Litigation Budget

> **Disclaimer**: This skill provides a framework for AI-assisted litigation budgeting and
> legal spend estimation. It does not constitute legal advice, financial advice, or a
> substitute for professional cost consultants or legal operations specialists. All outputs
> should be reviewed by qualified legal counsel, legal operations professionals, and
> finance stakeholders before use in matter planning, fee negotiations, or board reporting.
> Market rate data, benchmarks, and historical spend patterns cited from memory carry
> inaccuracy risk -- verify against current market data, e-billing analytics, and firm-
> specific historical records before relying on any figure described here. Legal billing
> practices and fee structures vary significantly by jurisdiction, practice area, and firm.

---

## Purpose and Scope

This skill creates structured, defensible litigation budgets using industry-standard
LEDES/UTBMS task codes. It produces phase-based cost estimates suitable for:

- **Matter planning**: Pre-engagement budget development for new litigation
- **Outside counsel management**: Budget submissions compliant with corporate guidelines
- **Fee negotiation**: Supporting data for rate discussions and AFA structuring
- **Board/executive reporting**: Litigation exposure forecasting and spend tracking
- **Variance analysis**: Comparing actual spend against budgeted amounts by phase
- **Alternative fee arrangements**: Modeling fixed, capped, phased, and success-based fees

**Covers:**

- **Phase-based budgeting**: L100 (Case Assessment) through L600 (E-Discovery) phases
- **Task-level estimation**: Hours by role (partner, associate, paralegal) per UTBMS task
- **Rate benchmarking**: Comparison against AmLaw 100, regional, and practice-specific rates
- **Expense forecasting**: Expert witnesses, depositions, e-discovery, court costs, travel
- **Scenario modeling**: Best case, expected case, worst case budget ranges
- **AFA structuring**: Fixed fee, capped fee, phased billing, blended rate, success fee models
- **Variance tracking**: Budget vs. actual analysis with phase-level granularity
- **Outside counsel guidelines compliance**: LEDES format requirements and billing rules

**Does not:**

- Replace legal operations professionals or cost consultants
- Provide binding fee quotes or guarantees
- Generate actual invoices or e-billing submissions
- Apply to transactional matters (M&A, real estate) -- see separate skills
- Cover criminal defense or government investigations budgets (different frameworks)

**Related skills:**

- `legalcode-early-case-assessment` -- Matter framing and strategy that informs budget
- `legalcode-damages-calculation` -- Exposure modeling for settlement/litigation decisions
- `legalcode-discovery-request-drafter` -- Discovery scope that drives L300 phase costs
- `legalcode-settlement-negotiation` -- Settlement posture informed by litigation costs

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic at baseline. Identify the forum and governing law first,
then localize rate assumptions, expense norms, and procedural cost drivers accordingly.

**[JURISDICTION-SPECIFIC]** Localize at minimum:

- Billing rate norms (AmLaw 100 vs. regional US vs. UK Magic Circle vs. EU national firms)
- Court fee structures and filing costs
- Discovery/disclosure cost drivers (US-style discovery vs. UK CPR disclosure vs. civil law)
- Expert witness fee ranges by jurisdiction
- Cost-shifting rules affecting exposure (American Rule vs. English Rule vs. civil law norms)
- E-discovery preservation and review cost norms
- ADR costs (arbitration institution fees, mediator rates)
- Currency and exchange rate considerations for cross-border matters

**Reference anchors frequently needed:**

**United States (Federal/State):**

- UTBMS Code Set: Litigation (L-codes), Counseling (C-codes), Projects (P-codes) [VERIFY]
- LEDES formats: 1998B (US standard), 1998BI (international), XML 2.2 (current) [VERIFY]
- AmLaw 100 partner rates: $1,200-$2,000+/hour (2024-2025 range) [VERIFY CURRENT]
- AmLaw 100 associate rates: $600-$1,200/hour (2024-2025 range) [VERIFY CURRENT]
- Regional firm rates: 30-50% below AmLaw 100 for comparable expertise [VERIFY]
- Discovery cost drivers: Document review at $25-$75/hour (contract reviewers) to
  $300-$500/hour (senior associate review); e-discovery processing at $0.50-$5.00/GB [VERIFY]
- Expert witness fees: $300-$1,500/hour depending on specialty [VERIFY]
- Deposition costs: $2,500-$5,000/day (transcript, videographer, facilities) [VERIFY]

**United Kingdom:**

- Solicitor rates: Magic Circle partners GBP 800-1,500+/hour; regional GBP 250-500/hour [VERIFY]
- Barrister fees: Junior counsel GBP 5,000-15,000/day; QC/KC GBP 15,000-50,000+/day [VERIFY]
- Court fees: Issue fees vary by claim value (Civil Proceedings Fees Order) [VERIFY]
- CPR costs rules: Loser pays (qualified one-way costs shifting in some matters) [VERIFY]
- Disclosure costs: Electronic disclosure (PD 57AD) document review and hosting [VERIFY]
- Expert fees: GBP 200-800/hour depending on specialty [VERIFY]

**European Union (Civil Law General):**

- Hourly rates: Major city partners EUR 400-800/hour; regional EUR 150-350/hour [VERIFY]
- Court fees: Vary significantly by member state and claim value [VERIFY]
- Procedural costs: Generally lower discovery burden reduces phase costs vs. US [VERIFY]
- Expert appointment: Court-appointed experts common (different cost structure) [VERIFY]
- Cost recovery: Varies by jurisdiction (Germany: RVG schedules; France: Art. 700) [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
budget parameters, the workflow pauses and asks when:

- The answer would materially change the budget structure or totals
- Multiple valid estimation methodologies exist and the user's preference matters
- Risk tolerance affects scenario ranges or contingency buffers
- Fee arrangement preferences change the budget presentation format

Use the structured-options pattern wherever marked with **CLARIFY** below. If the user has
already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept Matter Inputs

Accept matter information in any of these formats:

- **Case summary**: Narrative description of the dispute, parties, claims, and forum
- **Early case assessment**: Output from legalcode-early-case-assessment
- **Existing budget**: Prior budget to update, refine, or benchmark
- **RFP/engagement letter**: Outside counsel proposal or fee estimate request
- **Historical matter data**: Comparable closed matters with actual spend data

If insufficient information is provided to structure a budget, prompt the user to supply:

- Nature of the matter (litigation type, complexity, stakes)
- Forum and governing law
- Anticipated procedural posture and timeline
- Key cost drivers known at this stage (e.g., document volume, expert needs)

### Step 2: Gather Budget Context

**CLARIFY** -- Before building the budget, ask the user these questions:

1. **What is the purpose of this budget?**
   - Options: `Initial matter planning`, `Outside counsel submission`, `Board/executive
reporting`, `Fee negotiation support`, `Variance analysis (actual vs. budget)`,
     `Alternative fee arrangement structuring`
   - _Why this matters_: Purpose determines precision level, format, and emphasis.

2. **Which side are you on?**
   - Options: `Plaintiff/Claimant`, `Defendant/Respondent`, `Intervenor/Third party`
   - _Why this matters_: Plaintiff matters often front-load costs in case development;
     defendant matters may have more reactive cost profiles.

3. **What is the forum and governing law?**
   - Options: `US federal court`, `US state court (specify)`, `UK High Court/County Court`,
     `UK Commercial Court`, `EU member state court (specify)`, `International arbitration
(institution)`, `Domestic arbitration`, `Other (specify)`
   - _Why this matters_: Procedural rules drive phase costs dramatically.

4. **What is the matter complexity?**
   - Options: `Simple (single claim, limited discovery, short timeline)`,
     `Moderate (multiple claims, standard discovery, 12-24 month timeline)`,
     `Complex (multi-party, extensive discovery, multi-year timeline)`,
     `Bet-the-company (existential stakes, unlimited discovery, trial expected)`
   - _Why this matters_: Complexity determines hours multipliers and expense drivers.

5. **What is the anticipated timeline to resolution?**
   - Options: `6 months or less`, `6-12 months`, `12-24 months`, `24-36 months`,
     `36+ months`, `Uncertain`
   - _Why this matters_: Timeline affects phase sequencing and total spend.

6. **What fee arrangement is preferred or required?**
   - Options: `Hourly (standard)`, `Hourly with cap`, `Fixed fee (all phases)`,
     `Phased fixed fees`, `Blended rate`, `Success-based/contingency component`,
     `Hybrid (combination)`, `To be determined`
   - _Why this matters_: Fee arrangement changes budget structure and presentation.

7. **What rate environment applies?**
   - Options: `AmLaw 100 / Magic Circle rates`, `AmLaw 200 / Silver Circle rates`,
     `Regional / Boutique rates`, `In-house benchmark rates`, `Specify rates`
   - _Why this matters_: Rate assumptions drive the entire budget calculation.

If the user provides partial context, proceed with reasonable assumptions and state them
explicitly in the Glass Box audit trail.

### Step 3: Define Matter Scope and Assumptions

Based on the inputs, define the scope boundaries and key assumptions that will drive the
budget.

**Scope parameters to establish:**

- Claims and defenses to be budgeted (all or specific subset)
- Phases in scope (L100-L600 or specific phases)
- Timeline milestones and phase triggers
- Staffing model (partner/associate/paralegal ratios)
- Known cost drivers (document volume estimates, number of depositions, expert needs)
- Exclusions from scope (appeals, enforcement, related matters)

**CLARIFY** -- If any of the following are ambiguous, ask:

- **Document volume**: "How many documents (or custodians) are potentially discoverable?
  This drives L300/L600 phase costs significantly."
  - Options: `Small (<10,000 docs or <5 custodians)`, `Medium (10,000-100,000 docs)`,
    `Large (100,000-1M docs)`, `Massive (>1M docs)`, `Unknown`

- **Deposition count**: "How many depositions are anticipated?"
  - Options: `None expected`, `1-3 depositions`, `4-10 depositions`, `10-20 depositions`,
    `20+ depositions`, `Unknown`

- **Expert witnesses**: "How many expert witnesses are anticipated?"
  - Options: `None`, `1-2 (single discipline)`, `3-5 (multiple disciplines)`,
    `6+ (complex multi-expert case)`, `Unknown`

- **Trial likelihood**: "What is the expected trial probability?"
  - Options: `Low (<10% -- likely to settle)`, `Moderate (10-40%)`,
    `High (40-70%)`, `Very high (>70% -- trial expected)`, `Unknown`

Document all assumptions in the Glass Box audit trail.

### Step 4: Build Phase-Based Budget Structure

Structure the budget using UTBMS litigation phase codes. For each phase in scope, estimate
hours by role and apply applicable rates.

#### UTBMS Litigation Phase Codes (L-Codes)

| Phase               | Code | Description                                                  | Typical Cost Share |
| ------------------- | ---- | ------------------------------------------------------------ | ------------------ |
| Case Assessment     | L100 | Investigation, analysis, strategy, experts, administration   | 5-15%              |
| Pre-Trial Pleadings | L200 | Complaints, answers, motions, court conferences              | 10-20%             |
| Discovery           | L300 | Written discovery, production, depositions, expert discovery | 40-60%             |
| Trial               | L400 | Preparation, trial, post-trial motions                       | 15-30%             |
| Appeal              | L500 | Appellate motions, briefs, oral argument                     | 5-15%              |
| E-Discovery         | L600 | Electronic discovery (often embedded in L300)                | (varies)           |

#### Phase Budget Template

For each phase, build a budget with this structure:

```
Phase: [L-code] [Phase Name]
Timeline: [Start] to [End] (estimated)

Task Breakdown:
| Task Code | Task Description | Partner Hrs | Associate Hrs | Paralegal Hrs | Total Hrs |
|-----------|------------------|-------------|---------------|---------------|-----------|
| [code]    | [description]    | [hrs]       | [hrs]         | [hrs]         | [sum]     |

Hours Subtotal:
- Partner: [total hrs] x $[rate] = $[subtotal]
- Associate: [total hrs] x $[rate] = $[subtotal]
- Paralegal: [total hrs] x $[rate] = $[subtotal]
- Attorney fees subtotal: $[sum]

Expenses:
| Expense Code | Description | Estimated Cost |
|--------------|-------------|----------------|
| [code]       | [description] | $[amount]    |
- Expenses subtotal: $[sum]

Phase Total: $[grand total]
Contingency ([%]): $[buffer]
Phase Total with Contingency: $[final]
```

### Step 5: L100 -- Case Assessment and Development

**Task codes and typical activities:**

| Task Code | Description         | Activities                                                 |
| --------- | ------------------- | ---------------------------------------------------------- |
| L110      | Fact Investigation  | Document collection, witness interviews, site visits       |
| L120      | Analysis/Strategy   | Legal research, case theory development, strategy sessions |
| L130      | Experts             | Expert identification, retention, preliminary opinions     |
| L140      | Case Administration | File setup, conflict checks, engagement letters            |
| L150      | Budgeting           | Budget development and updates                             |

**Hour estimation guidance by complexity:**

| Complexity      | Partner    | Associate   | Paralegal  | Expense Range |
| --------------- | ---------- | ----------- | ---------- | ------------- |
| Simple          | 10-20 hrs  | 20-40 hrs   | 5-15 hrs   | $2K-$10K      |
| Moderate        | 20-40 hrs  | 40-80 hrs   | 15-30 hrs  | $10K-$30K     |
| Complex         | 40-80 hrs  | 80-150 hrs  | 30-60 hrs  | $30K-$75K     |
| Bet-the-company | 80-150 hrs | 150-300 hrs | 60-120 hrs | $75K-$200K    |

**Common expenses:**

- E110: Litigation hold implementation
- E115: Initial document collection and processing
- E120: Preliminary expert consultation

### Step 6: L200 -- Pre-Trial Pleadings and Motions

**Task codes and typical activities:**

| Task Code | Description             | Activities                                                  |
| --------- | ----------------------- | ----------------------------------------------------------- |
| L210      | Pleadings               | Complaint/answer drafting, amendments, third-party practice |
| L220      | Preliminary Injunctions | TRO/PI motion practice                                      |
| L230      | Court Conferences       | Case management, scheduling, status conferences             |
| L240      | Dispositive Motions     | Motion to dismiss, summary judgment                         |
| L250      | Other Motions           | Discovery motions, sanctions, evidentiary motions           |

**Hour estimation guidance:**

| Task                           | Partner   | Associate  | Paralegal |
| ------------------------------ | --------- | ---------- | --------- |
| Complaint/Answer (simple)      | 5-15 hrs  | 15-40 hrs  | 3-10 hrs  |
| Complaint/Answer (complex)     | 20-50 hrs | 60-120 hrs | 15-40 hrs |
| Motion to Dismiss (movant)     | 15-40 hrs | 40-100 hrs | 10-25 hrs |
| Motion to Dismiss (opposition) | 10-30 hrs | 30-80 hrs  | 8-20 hrs  |
| Summary Judgment (movant)      | 30-80 hrs | 80-200 hrs | 20-50 hrs |
| Summary Judgment (opposition)  | 25-60 hrs | 60-150 hrs | 15-40 hrs |

**[JURISDICTION-SPECIFIC] Variations:**

- US federal: FRCP 12(b)(6), Rule 56 standards affect motion scope [VERIFY]
- UK: Strike-out (CPR 3.4) and summary judgment (CPR 24) different procedural posture [VERIFY]
- Arbitration: Limited motion practice; adjust L200 downward [VERIFY]

### Step 7: L300 -- Discovery

**Discovery is typically the largest cost driver (40-60% of total budget).**

**Task codes and typical activities:**

| Task Code | Description         | Activities                                         |
| --------- | ------------------- | -------------------------------------------------- |
| L310      | Written Discovery   | Interrogatories, RFPs, RFAs drafting and responses |
| L320      | Document Production | Review, privilege logging, production              |
| L330      | Depositions         | Preparation, attendance, follow-up                 |
| L340      | Expert Discovery    | Expert reports, rebuttals, expert depositions      |
| L350      | Discovery Motions   | Motions to compel, protective orders               |

**Hour estimation guidance:**

| Task                            | Partner   | Associate  | Paralegal/Contract |
| ------------------------------- | --------- | ---------- | ------------------ |
| Interrogatories (draft)         | 3-8 hrs   | 10-30 hrs  | 5-15 hrs           |
| RFPs (draft, per set)           | 5-15 hrs  | 20-50 hrs  | 10-25 hrs          |
| Discovery responses             | 10-30 hrs | 40-100 hrs | 20-50 hrs          |
| Document review (per 10K docs)  | 2-10 hrs  | 20-50 hrs  | 150-300 hrs        |
| Privilege log (per 1K docs)     | 1-5 hrs   | 5-15 hrs   | 30-60 hrs          |
| Deposition prep (per depo)      | 5-15 hrs  | 15-40 hrs  | 5-15 hrs           |
| Deposition attendance (per day) | 8-10 hrs  | 8-10 hrs   | 4-8 hrs            |

**Document review cost estimation:**

| Volume        | Review Method                 | Estimated Cost |
| ------------- | ----------------------------- | -------------- |
| <10K docs     | Attorney review               | $15K-$50K      |
| 10K-100K docs | TAR-assisted review           | $50K-$200K     |
| 100K-1M docs  | TAR + contract reviewers      | $200K-$1M      |
| >1M docs      | Advanced TAR + managed review | $500K-$3M+     |

**Common expenses (L300/L600):**

- E-discovery processing: $0.50-$5/GB
- E-discovery hosting: $15-$50/GB/month
- Document review (contract): $25-$75/hour
- Deposition transcripts: $5-$15/page
- Videographer: $500-$1,500/day
- Court reporter: $300-$800/day
- Deposition facilities: $200-$1,000/day

**[JURISDICTION-SPECIFIC] Variations:**

- US: Broad discovery scope; document review is dominant cost [VERIFY]
- UK: CPR disclosure more limited; PD 57AD disclosure review [VERIFY]
- Civil law: Court-driven document requests; much lower discovery burden [VERIFY]
- Arbitration: Varies by institution rules (IBA Rules on Evidence) [VERIFY]

### Step 8: L400 -- Trial Preparation and Trial

**Task codes and typical activities:**

| Task Code | Description        | Activities                                                   |
| --------- | ------------------ | ------------------------------------------------------------ |
| L410      | Trial Preparation  | Witness prep, exhibits, motions in limine, jury instructions |
| L420      | Trial              | Trial attendance, argument, examination                      |
| L430      | Post-Trial Motions | JNOV, new trial, remittitur motions                          |

**Hour estimation guidance:**

| Task                              | Partner     | Associate     | Paralegal   |
| --------------------------------- | ----------- | ------------- | ----------- |
| Trial prep (simple, 1-week trial) | 80-150 hrs  | 150-300 hrs   | 50-100 hrs  |
| Trial prep (complex, multi-week)  | 200-500 hrs | 400-1,000 hrs | 150-400 hrs |
| Trial attendance (per day)        | 10-14 hrs   | 10-14 hrs     | 8-12 hrs    |
| Post-trial motions                | 20-50 hrs   | 40-100 hrs    | 10-25 hrs   |

**Trial contingency**: Apply 20-40% contingency buffer to L400 estimates given high
variability in trial length, last-minute motions, and jury deliberation time.

**Common expenses (L400):**

- Trial graphics/demonstratives: $20K-$200K
- Trial technology (hot seat, presentation): $5K-$50K
- Witness fees and travel: $5K-$50K
- Jury consultants: $50K-$250K
- War room / trial site office: $5K-$25K
- Daily transcripts: $500-$2,000/day

### Step 9: L500 -- Appeal

**Task codes and typical activities:**

| Task Code | Description       | Activities                          |
| --------- | ----------------- | ----------------------------------- |
| L510      | Appellate Motions | Stay pending appeal, record motions |
| L520      | Appellate Briefs  | Opening, answering, reply briefs    |
| L530      | Oral Argument     | Preparation and argument            |

**Hour estimation guidance:**

| Task                         | Partner     | Associate   | Paralegal |
| ---------------------------- | ----------- | ----------- | --------- |
| Appeal (simple/single issue) | 40-80 hrs   | 80-150 hrs  | 10-30 hrs |
| Appeal (complex/multi-issue) | 100-200 hrs | 200-400 hrs | 30-80 hrs |
| Oral argument prep           | 20-50 hrs   | 30-60 hrs   | 5-15 hrs  |

**Common expenses (L500):**

- Appellate record preparation: $2K-$10K
- Appendix/joint appendix printing: $1K-$5K
- Oral argument travel: $2K-$10K

### Step 10: Build Scenario Analysis

Present the budget in three scenarios to capture uncertainty:

| Scenario          | Assumption Basis                              | Multiplier    |
| ----------------- | --------------------------------------------- | ------------- |
| **Best Case**     | Early resolution, limited discovery, no trial | 0.5-0.7x base |
| **Expected Case** | Standard progression, settlement before trial | 1.0x base     |
| **Worst Case**    | Full discovery, trial, potential appeal       | 1.5-2.5x base |

**Build scenario drivers:**

For each scenario, identify the key variables that change:

- Settlement timing (pre-discovery, post-discovery, post-MSJ, at trial)
- Discovery scope (limited, standard, expanded)
- Motion practice (none, one major motion, multiple motions)
- Trial duration (no trial, short trial, full trial)
- Appeal (no appeal, limited appeal, full appeal)

**Output format:**

```
Scenario Analysis Summary

| Phase | Best Case | Expected | Worst Case |
|-------|-----------|----------|------------|
| L100 Assessment | $[X] | $[Y] | $[Z] |
| L200 Pleadings | $[X] | $[Y] | $[Z] |
| L300 Discovery | $[X] | $[Y] | $[Z] |
| L400 Trial | $[X] | $[Y] | $[Z] |
| L500 Appeal | $[X] | $[Y] | $[Z] |
| Expenses | $[X] | $[Y] | $[Z] |
| **Total** | **$[X]** | **$[Y]** | **$[Z]** |

Key Scenario Assumptions:
- Best Case: [assumptions]
- Expected Case: [assumptions]
- Worst Case: [assumptions]
```

### Step 11: Benchmark Against Market Data

Compare the budget against available benchmarks:

**Rate benchmarking:**

- Compare proposed rates against AmLaw 100/200, regional, or practice-specific benchmarks
- Note rate position (above/at/below market) with percentage variance
- Flag rates that are >15% above market without justification

**Matter benchmarking:**

- Compare total budget against historical comparable matters (same type, complexity, forum)
- Compare phase allocation percentages against industry norms
- Flag significant deviations from benchmarks with explanations

**Phase allocation benchmarks (litigation industry norms):**

| Phase           | Typical Range | Notes                                                 |
| --------------- | ------------- | ----------------------------------------------------- |
| L100 Assessment | 5-15%         | Higher in complex cases with extensive investigation  |
| L200 Pleadings  | 10-20%        | Higher if dispositive motion practice expected        |
| L300 Discovery  | 40-60%        | Dominant phase; can be 70%+ in document-heavy cases   |
| L400 Trial      | 15-30%        | Only if trial expected; can be 40%+ if trial proceeds |
| L500 Appeal     | 5-15%         | Only if appeal budgeted                               |

**CLARIFY** -- If the budget deviates significantly from benchmarks:

- "The proposed discovery phase is [X]% of total, which is [above/below] the typical
  40-60% range. Is this intentional based on case specifics, or should we adjust?"
- "The blended rate of $[X]/hour is [X]% above AmLaw 200 benchmarks for this practice
  area. Is this justified by firm expertise, or should we seek rate reductions?"

### Step 12: Structure Alternative Fee Arrangements (If Applicable)

If the fee arrangement is not standard hourly, structure the AFA:

#### Fixed Fee Model

```
Fixed Fee Budget

Phase | Fixed Fee | Scope Included | Exclusions |
------|-----------|----------------|------------|
L100 Assessment | $[X] | [scope] | [exclusions] |
L200 Pleadings | $[X] | [scope] | [exclusions] |
L300 Discovery | $[X] | [scope] | [exclusions] |
L400 Trial | $[X] | [scope] | [exclusions] |

Total Fixed Fee: $[sum]
Change Order Rate: $[hourly rate for out-of-scope work]
Expense Handling: [pass-through / included / capped]
```

#### Capped Fee Model

```
Capped Fee Budget

Phase | Estimated Fee | Cap | Trigger for Cap Review |
------|--------------|-----|------------------------|
L100 Assessment | $[X] | $[cap] | [trigger] |
L200 Pleadings | $[X] | $[cap] | [trigger] |
...

Total Cap: $[sum]
Cap Review Events: [list events that trigger cap renegotiation]
```

#### Phased Billing Model

```
Phased Billing Budget

Phase 1: Case Assessment (L100)
- Budget: $[X]
- Deliverable: [deliverable]
- Go/No-Go Decision Point: [date/milestone]

Phase 2: [Next Phase]
...

Phase Budget Updates: [frequency and process]
```

#### Success Fee / Contingency Component

```
Hybrid Fee Structure

Base Fee: $[X] (reduced hourly or fixed)
Success Fee: [%] of [recovery/savings/defined outcome]
Cap on Success Fee: $[X]
Success Fee Trigger: [definition of success]
No Success Scenario: [what happens if outcome not achieved]
```

### Step 13: Apply Variance Analysis Framework (If Actual Data Available)

If comparing budget to actual spend, apply variance analysis:

```
Budget vs. Actual Analysis

| Phase | Budget | Actual | Variance | Variance % | Explanation |
|-------|--------|--------|----------|------------|-------------|
| L100 | $[X] | $[Y] | $[Z] | [%] | [explanation] |
| L200 | $[X] | $[Y] | $[Z] | [%] | [explanation] |
...

Total | $[X] | $[Y] | $[Z] | [%] |

Key Variance Drivers:
1. [Driver 1]: [explanation and quantification]
2. [Driver 2]: [explanation and quantification]
...

Lessons Learned for Future Budgeting:
1. [lesson]
2. [lesson]
...
```

**Variance thresholds:**

- GREEN: Within +/- 10% of budget
- YELLOW: +/- 10-25% variance (requires explanation)
- RED: >25% variance (requires escalation and remediation)

### Step 14: Quality Verification

Before delivering the budget, run quality checks:

1. **Arithmetic verification**: Confirm all calculations (hours x rates, phase totals, grand totals)
2. **Completeness check**: All phases in scope addressed; all expenses identified
3. **Benchmark check**: Budget compared against market data; deviations explained
4. **Assumption audit**: All assumptions documented; sensitivity to key assumptions tested
5. **Format compliance**: UTBMS codes used correctly; LEDES format requirements met
6. **Citation gates**: Rate and benchmark data sources cited or marked [VERIFY]
7. **Glass Box generation**: Audit trail completed

### Step 15: Deliver Budget Package

Produce the final budget using the Output Format Template below.

---

## UTBMS Code Reference

### Litigation Task Codes (L-Codes) -- Complete Reference

#### L100 -- Case Assessment, Development, and Administration

| Code | Task                           | Description                                 |
| ---- | ------------------------------ | ------------------------------------------- |
| L110 | Fact Investigation/Development | Gathering facts through non-discovery means |
| L120 | Analysis/Strategy              | Legal analysis and strategy development     |
| L130 | Experts/Consultants            | Expert retention and consultation           |
| L140 | Document/File Administration   | Matter management and administration        |
| L150 | Budgeting                      | Budget development and tracking             |
| L160 | Settlement/Non-Binding ADR     | Settlement discussions and mediation        |
| L190 | Other                          | Other L100 activities                       |

#### L200 -- Pre-Trial Pleadings and Motions

| Code | Task                                         | Description                     |
| ---- | -------------------------------------------- | ------------------------------- |
| L210 | Pleadings                                    | Complaints, answers, amendments |
| L220 | Preliminary Injunctions/Provisional Remedies | TRO, PI, attachment             |
| L230 | Court-Mandated Conferences                   | Status, scheduling, CMC         |
| L240 | Dispositive Motions                          | MTD, MSJ                        |
| L250 | Other Written Motions/Submissions            | Non-dispositive motions         |
| L260 | Class Action Certification                   | Class certification proceedings |
| L290 | Other                                        | Other L200 activities           |

#### L300 -- Discovery

| Code | Task                  | Description                       |
| ---- | --------------------- | --------------------------------- |
| L310 | Written Discovery     | Interrogatories, RFPs, RFAs       |
| L320 | Document Production   | Production preparation and review |
| L330 | Depositions           | Fact witness depositions          |
| L340 | Expert Discovery      | Expert reports and depositions    |
| L350 | Discovery Motions     | Compel, protect, sanctions        |
| L360 | Third Party Discovery | Subpoenas to non-parties          |
| L390 | Other                 | Other L300 activities             |

#### L400 -- Trial Preparation and Trial

| Code | Task                           | Description                          |
| ---- | ------------------------------ | ------------------------------------ |
| L410 | Fact Witnesses                 | Witness preparation                  |
| L420 | Expert Witnesses               | Expert preparation for trial         |
| L430 | Written Motions/Submissions    | Motions in limine, jury instructions |
| L440 | Other Trial Preparation        | Exhibits, demonstratives, logistics  |
| L450 | Trial/Evidentiary Hearing      | Trial attendance                     |
| L460 | Post-Trial Motions/Submissions | JNOV, new trial, remittitur          |
| L490 | Other                          | Other L400 activities                |

#### L500 -- Appeal

| Code | Task                          | Description                           |
| ---- | ----------------------------- | ------------------------------------- |
| L510 | Appellate Motions/Submissions | Stay, record motions                  |
| L520 | Briefs                        | Appellate brief drafting              |
| L530 | Oral Argument                 | Argument preparation and presentation |
| L540 | Post-Appellate Motions        | Rehearing, cert petitions             |
| L590 | Other                         | Other L500 activities                 |

#### L600 -- E-Discovery

| Code | Task           | Description                            |
| ---- | -------------- | -------------------------------------- |
| L610 | ESI Collection | Custodian collection, forensic imaging |
| L620 | ESI Processing | Processing, de-duplication, filtering  |
| L630 | ESI Review     | Document review (first-pass, QC)       |
| L640 | ESI Production | Production formatting and delivery     |
| L650 | ESI Legal Hold | Hold implementation and tracking       |
| L690 | Other          | Other L600 activities                  |

### Activity Codes (A-Codes)

| Code | Activity                            | Description                      |
| ---- | ----------------------------------- | -------------------------------- |
| A101 | Plan and prepare                    | Planning and preparation         |
| A102 | Research                            | Legal research                   |
| A103 | Draft/revise                        | Document drafting                |
| A104 | Review/analyze                      | Document review and analysis     |
| A105 | Communicate (in firm)               | Internal communications          |
| A106 | Communicate (with client)           | Client communications            |
| A107 | Communicate (other outside counsel) | Co-counsel communications        |
| A108 | Communicate (other external)        | Opposing counsel, court, experts |
| A109 | Appear for/attend                   | Court appearances, depositions   |
| A110 | Manage data/files                   | File management                  |
| A111 | Other                               | Other activities                 |

### Expense Codes (E-Codes)

| Code | Expense                | Description                    |
| ---- | ---------------------- | ------------------------------ |
| E101 | Copying/reproduction   | Internal copying               |
| E102 | Outside copying        | External copy services         |
| E103 | Word processing        | Word processing services       |
| E104 | Fax                    | Fax transmissions              |
| E105 | Telephone              | Telephone charges              |
| E106 | Online research        | Westlaw, Lexis, other research |
| E107 | Delivery/messenger     | Courier services               |
| E108 | Postage                | Mailing costs                  |
| E109 | Local travel           | Local transportation           |
| E110 | Out-of-town travel     | Air, hotel, meals              |
| E111 | Meals                  | Working meals                  |
| E112 | Court fees             | Filing fees, service fees      |
| E113 | Subpoena fees          | Witness fees, service          |
| E114 | Witness fees           | Expert and fact witness fees   |
| E115 | Deposition transcripts | Reporter fees, transcripts     |
| E116 | Trial transcripts      | Trial transcripts              |
| E117 | Trial exhibits         | Exhibit preparation            |
| E118 | Litigation support     | E-discovery, database          |
| E119 | Other                  | Other expenses                 |

---

## Budget Classification System

Classify budget line items by confidence level:

| Level           | Meaning                                                          | Action                               |
| --------------- | ---------------------------------------------------------------- | ------------------------------------ |
| **Firm**        | High confidence estimate based on historical data or fixed scope | Include at face value                |
| **Estimated**   | Reasonable estimate with moderate uncertainty                    | Include with notation                |
| **Placeholder** | Rough order of magnitude pending further information             | Flag for update                      |
| **Contingent**  | Depends on case developments; may not occur                      | Show separately with trigger         |
| **TBD**         | Cannot estimate without additional information                   | Exclude from totals; list separately |

---

## Actionable Output Per Line Item

For each budget line item above a materiality threshold, provide:

| Field            | Content                                          |
| ---------------- | ------------------------------------------------ |
| Phase/Task       | UTBMS code and description                       |
| Estimated Amount | Dollar amount                                    |
| Basis            | How estimated (benchmark, historical, bottom-up) |
| Confidence       | Firm / Estimated / Placeholder                   |
| Key Assumptions  | What must hold true for estimate to be accurate  |
| Variance Drivers | What could cause this to exceed estimate         |
| Mitigation       | How variance risk can be reduced                 |

---

## Prioritization Framework

Use these tiers for budget management focus:

| Tier       | Label    | Criteria                                      | Management Focus                     |
| ---------- | -------- | --------------------------------------------- | ------------------------------------ |
| **Tier 1** | Critical | >20% of total budget; high variance risk      | Weekly monitoring; partner oversight |
| **Tier 2** | Material | 5-20% of total budget; moderate variance risk | Monthly review; scope management     |
| **Tier 3** | Routine  | <5% of total budget; low variance risk        | Quarterly review; standard controls  |

---

## Citation Quality Gates

Before delivery, verify:

| Gate             | Rule                                                                  | Fail Action                       |
| ---------------- | --------------------------------------------------------------------- | --------------------------------- |
| **Source**       | Rate data cites source (AmLaw survey, firm rates, benchmark database) | Add source or mark [VERIFY]       |
| **Currency**     | Rate data is current year or explicitly dated                         | Add year or mark [CHECK CURRENCY] |
| **Benchmark**    | Budget compared against at least one benchmark                        | Add benchmark comparison          |
| **Calculation**  | All arithmetic verified                                               | Correct errors                    |
| **Completeness** | All phases in scope addressed                                         | Add missing phases                |

---

## Self-Interrogation for High-Value Budgets

For budgets exceeding $500K (or organization's materiality threshold), apply this 3-pass
review:

**Pass 1 -- Assumption Stress Test**:

- What if discovery volume is 2x estimated?
- What if trial actually proceeds?
- What if the timeline extends 12 months?
- Would the budget hold, or is contingency inadequate?

**Pass 2 -- Benchmark Reasonableness**:

- Is this budget consistent with comparable historical matters?
- Are rate assumptions at/above/below market, and is that appropriate?
- Is the phase allocation consistent with case type norms?

**Pass 3 -- Challenge**:

- What would opposing counsel's budget look like for the same case?
- Are there scope efficiencies being missed?
- Could alternative staffing models reduce cost without quality impact?

Mark audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

---

## Confidence Scoring

For each phase estimate, assign a confidence level:

| Level           | Range     | Meaning                                           | Contingency     |
| --------------- | --------- | ------------------------------------------------- | --------------- |
| **High**        | 0.85-1.0  | Historical data available; scope well-defined     | 0-10%           |
| **Moderate**    | 0.60-0.84 | Reasonable estimate; some scope uncertainty       | 10-25%          |
| **Low**         | 0.40-0.59 | Significant uncertainty; case-dependent variables | 25-50%          |
| **Speculative** | <0.40     | Cannot estimate reliably; placeholder only        | 50%+ or exclude |

---

## Glass Box Audit Trail

Every budget output MUST include a Glass Box audit section:

```yaml
glass_box:
  matter: "[Matter name/number]"
  matter_type: "[Litigation type]"
  forum: "[Court/arbitration institution]"
  budget_purpose: "[Planning / Submission / Reporting / Variance]"
  user_side: "[Plaintiff / Defendant]"
  complexity: "[Simple / Moderate / Complex / Bet-the-company]"
  timeline: "[Anticipated duration]"
  fee_arrangement: "[Hourly / Fixed / Capped / Hybrid]"
  rate_basis: "[AmLaw 100 / Regional / Specified / Historical]"
  phases_budgeted: "[L100, L200, etc.]"
  total_budget_expected: "$[X]"
  total_budget_range: "$[low] - $[high]"
  key_assumptions:
    - "[Assumption 1]"
    - "[Assumption 2]"
  benchmarks_used:
    - "[Benchmark 1 — source]"
    - "[Benchmark 2 — source]"
  variance_from_benchmark: "[%] [above/below/at market]"
  rate_data_sources:
    - "[Source — VERIFIED or UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  confidence: "HIGH / MODERATE / LOW — [rationale]"
  limitations:
    - "[Limitation 1]"
    - "[Limitation 2]"
  prepared_by: "AI-assisted — requires legal ops and counsel review"
```

---

## Anti-Patterns

What NOT to do when building litigation budgets:

1. **Single-point estimates without ranges** -- Litigation is inherently uncertain. A
   budget that shows only one number without best/expected/worst case ranges is misleading.
   Always provide scenario analysis.

2. **Ignoring discovery as the cost driver** -- In US litigation, discovery is typically
   40-60% of total cost. Budgets that underweight L300/L600 or fail to account for document
   volume are systematically wrong.

3. **Using stale rate data** -- Legal rates increase 5-10% annually. Using last year's
   (or older) rate data produces inaccurate budgets. Always verify rate currency and mark
   [VERIFY] if uncertain.

4. **Omitting expenses** -- Attorney fees are only part of the cost. Expert witnesses,
   e-discovery, depositions, court reporters, and travel can add 20-40% to total spend.
   Always budget expenses separately.

5. **Assuming settlement without budgeting trial** -- Many budgets assume "likely to
   settle" and exclude L400 trial costs. If there is any realistic trial probability
   (>10%), include L400 in worst-case scenario.

6. **Flat-rate benchmarking** -- Comparing a patent litigation budget to a simple breach
   of contract benchmark is meaningless. Benchmark against comparable case types, forums,
   and complexity levels.

7. **Ignoring jurisdictional differences** -- US discovery costs have no equivalent in
   civil law jurisdictions. UK barrister fees are structured differently than US partner
   fees. Always localize for the forum.

8. **No contingency buffer** -- Even well-estimated budgets face variance. Failing to
   include 10-25% contingency for moderate-complexity matters (and 25-50% for complex
   matters) understates likely spend.

9. **Budget without assumptions** -- A budget number without documented assumptions is
   unauditable. When assumptions change, the budget should change. Always document.

10. **Ignoring staffing leverage** -- A budget built at partner rates for work that could
    be done by associates or paralegals is inefficient. Apply appropriate leverage ratios
    (2:1 to 4:1 associate:partner for most litigation).

11. **AFA structuring without scope definition** -- A fixed fee without clear scope
    boundaries is a recipe for disputes. Always define inclusions, exclusions, and
    change-order mechanisms.

12. **Variance analysis without explanations** -- Showing budget vs. actual without
    explaining the drivers provides no actionable intelligence. Always explain material
    variances.

13. **Treating e-discovery as a rounding error** -- E-discovery (L600) can dwarf all
    other phases in document-intensive cases. Budget e-discovery explicitly with volume-
    based assumptions.

14. **Confusing UTBMS codes** -- Misclassifying work (e.g., putting document review
    under L120 Analysis instead of L320 Document Production) makes phase analysis
    meaningless. Use codes correctly.

15. **Budget without client input** -- A budget that does not reflect client risk
    tolerance, strategic priorities, or historical preferences will not meet expectations.
    Always clarify client context before finalizing.

---

## Writing Standards

Apply clear, professional standards to budget deliverables:

**For budget submissions:**

- Use consistent currency and formatting throughout
- Round to appropriate precision (whole dollars for items >$1K; nearest $100 for smaller)
- Use tables for phase summaries; narrative for assumptions and explanations
- Clearly separate fees from expenses
- State all assumptions explicitly

**For variance analysis:**

- Lead with the headline (total variance, direction, key drivers)
- Provide phase-level detail for material variances only
- Include both absolute dollars and percentage variance
- Offer forward-looking remediation where variance is negative

**Quality gates before delivery:**

1. Do all calculations check (sum of phases = total; hours x rates = fees)?
2. Are all assumptions documented?
3. Is rate data sourced or marked [VERIFY]?
4. Is the budget benchmarked against at least one comparator?
5. Is contingency appropriate for the confidence level?

---

## External Tool Integration

This skill integrates with legal spend management platforms and e-billing systems.

**With e-billing/legal ops platform connected (CounselLink, Legal Tracker, Brightflag):**

- Import historical matter data for benchmark comparisons
- Pull actual spend data for variance analysis
- Export budget in LEDES format for submission
- Access real-time rate benchmarks by firm, practice, and geography

**With legalcode-mcp connected:**

- Research jurisdictional procedural rules affecting cost drivers
- Verify filing fee and court cost schedules
- Research arbitration institution fee schedules

**Without external tools:**

- Use published benchmark data (mark [VERIFY])
- Apply industry-standard assumptions
- Note in Glass Box: `external_tools_used: "None — manual verification required"`
- Include prominent notice that rate and benchmark data require independent verification

---

## Output Format Template

Structure the final budget deliverable as:

```markdown
## Litigation Budget

**Matter**: [matter name/number]
**Parties**: [party names]
**Your Side**: [plaintiff/defendant]
**Forum**: [court/arbitration]
**Governing Law**: [jurisdiction]
**Prepared Date**: [date]
**Budget Type**: [Initial / Updated / Final]
**Fee Arrangement**: [Hourly / Fixed / Capped / Hybrid]

---

## Executive Summary

**Total Budget (Expected Case)**: $[X]
**Budget Range**: $[low] - $[high]
**Timeline**: [anticipated duration]
**Key Cost Drivers**: [top 3 cost drivers]
**Budget Confidence**: [HIGH / MODERATE / LOW]

---

## Scenario Summary

| Scenario   | Total | Key Assumptions |
| ---------- | ----- | --------------- |
| Best Case  | $[X]  | [assumptions]   |
| Expected   | $[X]  | [assumptions]   |
| Worst Case | $[X]  | [assumptions]   |

---

## Phase-by-Phase Budget

### L100 -- Case Assessment | $[total] | [confidence]

[Phase budget detail per Step 5 template]

### L200 -- Pre-Trial Pleadings | $[total] | [confidence]

[Phase budget detail per Step 6 template]

### L300 -- Discovery | $[total] | [confidence]

[Phase budget detail per Step 7 template]

### L400 -- Trial | $[total] | [confidence]

[Phase budget detail per Step 8 template]

### L500 -- Appeal | $[total] | [confidence]

[Phase budget detail per Step 9 template]

---

## Expense Budget

| Category           | Estimated Cost | Confidence | Assumptions   |
| ------------------ | -------------- | ---------- | ------------- |
| E-Discovery        | $[X]           | [level]    | [assumptions] |
| Expert Witnesses   | $[X]           | [level]    | [assumptions] |
| Depositions        | $[X]           | [level]    | [assumptions] |
| Court Fees         | $[X]           | [level]    | [assumptions] |
| Travel             | $[X]           | [level]    | [assumptions] |
| Other              | $[X]           | [level]    | [assumptions] |
| **Expenses Total** | **$[X]**       |            |               |

---

## Rate Summary

| Role        | Rate        | Benchmark        | Position                |
| ----------- | ----------- | ---------------- | ----------------------- |
| Partner     | $[X]/hr     | $[Y]/hr [source] | [above/at/below] market |
| Associate   | $[X]/hr     | $[Y]/hr [source] | [above/at/below] market |
| Paralegal   | $[X]/hr     | $[Y]/hr [source] | [above/at/below] market |
| **Blended** | **$[X]/hr** | **$[Y]/hr**      |                         |

---

## Budget vs. Benchmark

| Metric       | This Budget | Benchmark     | Variance |
| ------------ | ----------- | ------------- | -------- |
| Total Budget | $[X]        | $[Y] [source] | [%]      |
| Discovery %  | [X]%        | [Y]%          | [%]      |
| Blended Rate | $[X]/hr     | $[Y]/hr       | [%]      |

---

## Key Assumptions

1. [Assumption 1]
2. [Assumption 2]
3. [Assumption 3]
   ...

---

## Risk and Variance Drivers

| Phase | Risk                        | Impact | Likelihood | Mitigation   |
| ----- | --------------------------- | ------ | ---------- | ------------ |
| L300  | Document volume > estimated | +$[X]  | [H/M/L]    | [mitigation] |
| L400  | Trial proceeds              | +$[X]  | [H/M/L]    | [mitigation] |

...

---

## Alternative Fee Arrangement (If Applicable)

[AFA structure per Step 12]

---

## Next Steps

1. [Action item 1] -- [owner] -- [date]
2. [Action item 2] -- [owner] -- [date]
   ...

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

This skill is jurisdiction-agnostic by design. To create a jurisdiction-specific variant:

1. Replace rate assumptions with jurisdiction-specific market data
2. Replace procedural assumptions (discovery scope, motion practice) with local norms
3. Add jurisdiction-specific expense items (e.g., barrister fees for UK; translation for
   cross-border)
4. Adjust phase allocation percentages for local procedural framework
5. Add jurisdiction-specific UTBMS extensions if used (e.g., UK Legal Aid codes)
6. Update cost-shifting assumptions for local rules

**Jurisdictional considerations:**

- **US Federal/State**: Full UTBMS L-code set; broad discovery; high e-discovery costs
- **UK High Court**: CPR disclosure (not US-style discovery); barrister + solicitor split;
  loser-pays costs
- **International Arbitration**: Limited discovery; institution-specific fee schedules;
  tribunal costs separate
- **Civil Law Jurisdictions**: Court-directed proceedings; limited discovery; lower overall
  costs for comparable disputes

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis combining LEDES/UTBMS billing
standards, litigation phase budgeting methodology, market rate benchmarking frameworks,
alternative fee arrangement structures, and legal operations best practices into a
comprehensive litigation budget skill. Research sources include LEDES Oversight Committee
standards, ABA/ACC UTBMS code sets, and legal industry benchmarking data.
