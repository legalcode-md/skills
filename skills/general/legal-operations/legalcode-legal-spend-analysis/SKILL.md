---
name: legalcode-legal-spend-analysis
description: 'Analyze, benchmark, and optimize legal department spending — covering outside counsel rate
  benchmarking, matter-type cost analysis, rate card comparison, alternative fee arrangement (AFA) evaluation,
  legal operations efficiency metrics, self-service deflection rates, budget forecasting, CLOC Core 12
  maturity alignment, and legal tech ROI analysis. Use when a legal ops team needs to understand where
  money is going, how rates compare to the market, whether the inside/outside counsel ratio is optimal,
  how to evaluate a proposed AFA, whether a CLM or e-billing platform is delivering ROI, or how to build
  an annual legal budget. Also triggers on: legal spend management, cost per matter, total legal spend
  as percentage of revenue, outside counsel benchmarking, LEDES invoice analysis, UTBMS code analysis,
  legal department efficiency, legal ops dashboard, outside counsel convergence, rate review, matter budget
  variance, accrual management, self-service legal portal, legal technology investment.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Legal Spend Analysis

> **Disclaimer**: This skill provides a framework for AI-assisted legal spend analysis
> and benchmarking. It does not constitute legal, financial, or investment advice. All
> outputs should be reviewed by qualified legal operations and finance professionals
> before use in budget decisions or vendor negotiations. Benchmark figures cited from
> published surveys (ACC, CLOC, Wolters Kluwer, Bloomberg Law) represent snapshot data
> from specific survey periods and respondent populations — verify currency and
> applicability to your organization's industry, size, and geographic footprint before
> relying on them. Methodological references carry standard hallucination risk — verify
> against authoritative sources before applying.

---

## Purpose and Scope

This skill enables AI-assisted analysis and optimization of legal department spending.
It applies CLOC-aligned frameworks, ACC benchmarking data, LEDES/UTBMS standards, and
legal operations best practices to turn raw spend data into actionable intelligence.

**Covers:**

- Total legal spend as a percentage of company revenue (baseline assessment)
- Inside vs. outside counsel cost ratio analysis
- Outside counsel rate benchmarking against market data
- Matter-type cost analysis by UTBMS task code category
- Rate card review and rate comparison across law firms
- Alternative fee arrangement (AFA) evaluation and financial modeling
- Legal operations efficiency metrics (cycle time, matter volume, team utilization)
- Self-service and deflection rate measurement
- Budget forecasting using EAC (Estimate at Completion) methodology
- Budget vs. actual variance analysis with driver identification
- Legal technology ROI calculation (CLM, e-billing, AI tools)
- CLOC Core 12 maturity gap analysis for financial management function

**Does not:**

- Provide legal advice on substantive legal matters
- Replace the judgment of qualified legal finance professionals
- Guarantee that benchmarks apply to any specific organization without adjustment
- Produce GAAP/IFRS financial statements or auditable management accounts
- Apply to any single jurisdiction exclusively — benchmarks are primarily US-centric
  with [JURISDICTION-SPECIFIC] markers where international variation is material

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic analytical skill. Legal spend management methodology
transcends jurisdictional boundaries; however, the primary benchmarking data sources
(ACC, CLOC, Wolters Kluwer ELM, Bloomberg Law) are US-centric.

[JURISDICTION-SPECIFIC] Where this skill references benchmarks, billing standards,
or regulatory frameworks, consider these local variations:

- **LEDES/UTBMS**: Standard in the US and UK; less prevalent in continental Europe,
  APAC, and Latin America — adapt to local invoice formats where needed
- **Rate benchmarks**: US partner rates (avg. $500–$1,200+/hr) diverge significantly
  from UK, EU, Australian, and APAC market rates — use geography-adjusted data
- **AFA adoption**: Varies significantly by jurisdiction and legal culture [VERIFY
  current adoption rates for your jurisdiction]
- **VAT/GST**: Where applicable, ensure spend analysis reflects net or gross
  consistently — mixing the two will distort benchmarks [JURISDICTION-SPECIFIC]
- **Currency normalization**: Multi-jurisdiction legal departments should normalize
  to a single reporting currency before applying any benchmark ratio

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming the organization's size, industry, or analysis objective, the workflow pauses
and asks when:

- The answer would change the analysis direction or benchmark set to apply
- Multiple valid approaches exist and the organization's priorities matter
- Data gaps mean assumptions must be made explicitly
- The analysis covers multiple jurisdictions with different benchmarks

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

Accept spend data in any of these formats:

- **LEDES file(s)**: One or more LEDES-format billing files from law firms
- **Invoice export**: CSV, Excel, or PDF export from an e-billing platform
  (Brightflag, SimpleLegal, Onit, Thomson Reuters Legal Tracker, Wolters Kluwer ELM)
- **Manual data**: Spend figures provided directly by the user (total spend by firm,
  matter type, or time period)
- **Budget document**: Budget vs. actual spreadsheet or ELM system export
- **Rate card**: Law firm rate card for review and benchmarking
- **AFA proposal**: Proposed AFA terms from outside counsel for evaluation
- **Prompt only**: A description of the legal department and its spend profile (the
  skill will perform benchmark-based analysis without raw data)

If no data is provided, proceed with benchmark-based analysis using the user's described
profile. Clearly label all outputs: "Benchmark-based estimates — validate against your
actual spend data."

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the analysis, gather this context. Ask the user for
any information not already provided:

1. **Analysis objective**: What is the primary goal?
   - Options: Understand current spend baseline, Benchmark outside counsel rates,
     Evaluate a specific AFA proposal, Build or validate the annual legal budget,
     Calculate legal tech ROI, Assess legal ops efficiency, Full spend dashboard,
     Other (describe)
   - _Why this matters_: Different objectives require different analytical depth and
     benchmark sets. A rate review focuses on firm-by-firm rate cards; a budget
     forecast requires matter-level EAC calculations.

2. **Company profile**:
   - Revenue range: Under $100M / $100M–$500M / $500M–$1B / $1B–$5B / $5B–$20B /
     Over $20B
   - Industry: Financial services, Technology/SaaS, Life sciences/Healthcare,
     Manufacturing, Retail/Consumer, Professional services, Other
   - _Why this matters_: Benchmarks for "total legal spend as % of revenue" vary
     significantly by size and industry. A tech startup at 0.5% may be above median
     while a regulated financial institution at 0.5% may be unusually lean.

3. **Legal department structure**:
   - In-house team size (approximate FTE attorneys + legal ops)
   - Number of primary outside counsel firms (convergence program or broad panel)
   - Primary jurisdictions of legal work
   - _Why this matters_: Inside/outside ratio benchmarks depend on team composition.
     Convergence programs change the rate negotiation dynamic.

4. **Time period**: What period does this analysis cover?
   - Options: Current fiscal year to date, Full fiscal year, Rolling 12 months,
     Multi-year trend (specify years)
   - _Why this matters_: Budget forecasting requires year-to-date actuals; trend
     analysis requires multiple periods.

5. **Existing tools**: What systems does the legal department use?
   - E-billing platform (if any), CLM system (if any), Matter management system (if any)
   - _Why this matters_: Tool integration affects data availability and ROI calculation
     approach.

If the user provides partial context, state your assumptions explicitly before proceeding.

### Step 3: Data Preparation and Normalization

Before analysis, normalize the spend data for consistency.

**Data quality checks:**

- [ ] Currency: All amounts in a single reporting currency. Flag any multi-currency
      data and confirm the exchange rate basis.
- [ ] Time period: All data covers the same period. Flag partial-year data and
      annualize where needed.
- [ ] Vendor mapping: Confirm that law firm names are consistent (e.g., "Baker
      McKenzie," "Baker & McKenzie," and "BakerMcKenzie" are the same firm).
- [ ] Matter classification: Confirm that matters are classified by UTBMS task code
      or an equivalent matter taxonomy. If not, propose a classification scheme.
- [ ] Inside vs. outside separation: Confirm that inside counsel costs (compensation,
      benefits, overhead) are separated from outside counsel costs (invoices, expert
      fees, filing costs).

**LEDES/UTBMS normalization** (if billing files provided):

- Map activity codes to the UTBMS Phase/Task/Activity hierarchy
- Identify non-standard codes and flag for review
- Calculate spend by UTBMS Phase: L100–L600 (Litigation phases), A100–A115
  (Counseling phases), C100–C300 (Business Transactions phases), B100–B400
  (Bankruptcy phases)
- Calculate hours and fees separately by timekeeper level (Partner, Of Counsel,
  Associate, Paralegal, Other)

**⟁ CLARIFY** — If data has significant quality issues (missing matter codes,
inconsistent firm names, mixed currencies without a stated exchange rate), ask the user
how to proceed:

- Option A: Proceed with available data and flag gaps in the output
- Option B: Identify and resolve the specific data issues before analysis
- Option C: Proceed with benchmark-only analysis and note the data limitations

### Step 4: Spend Baseline Assessment

Establish the overall spend profile before drilling into components.

**Calculate the following baseline metrics:**

| Metric                             | Formula                                                  | Purpose                      |
| ---------------------------------- | -------------------------------------------------------- | ---------------------------- |
| **Total Legal Spend**              | Inside costs + Outside counsel costs + Other legal costs | Foundation for all ratios    |
| **Total Legal Spend % Revenue**    | Total Legal Spend / Company Revenue × 100                | Primary efficiency benchmark |
| **Inside/Outside Ratio**           | Inside Costs / Outside Counsel Costs                     | Staffing model efficiency    |
| **Spend Per Attorney (FTE)**       | Total Legal Spend / Total FTE attorneys                  | Productivity proxy           |
| **Outside Counsel Concentration**  | Top 3 firms' spend / Total outside spend × 100           | Panel management health      |
| **Cost Per Matter**                | Total outside counsel spend / Number of active matters   | Matter economics             |
| **Average Billing Rate (blended)** | Total outside counsel fees / Total outside counsel hours | Rate efficiency              |

**Benchmark comparison** (ACC 2023 Law Department Management Benchmarking Report
[VERIFY currency]):

| Metric                                      | 25th Percentile | Median | 75th Percentile |
| ------------------------------------------- | --------------- | ------ | --------------- |
| Total legal spend % revenue                 | 0.27%           | 0.63%  | 1.43%           |
| Inside/outside ratio                        | 40/60           | 52/48  | 65/35           |
| Outside counsel concentration (top 3 firms) | 35%             | 52%    | 70%             |

**Industry adjustments** [VERIFY against current survey data]:

| Industry                     | Typical Spend % Revenue |
| ---------------------------- | ----------------------- |
| Financial services / Banking | 0.8–1.5%                |
| Life sciences / Healthcare   | 0.7–1.2%                |
| Technology / SaaS            | 0.2–0.6%                |
| Manufacturing                | 0.3–0.7%                |
| Retail / Consumer            | 0.3–0.7%                |
| Professional services        | 0.4–0.9%                |

**⟁ CLARIFY** — If the organization's spend falls outside the 25th–75th percentile
range, ask the user:

- "Your total legal spend is [X]% of revenue, which is [above/below] the industry
  median of [Y]%. Would you like me to investigate the primary drivers of this
  variance, or is the current level a known and accepted business decision?"

### Step 5: Outside Counsel Rate Benchmarking

Compare the organization's outside counsel rates against market benchmarks.

**Rate analysis process:**

1. **Extract the rate card**: For each law firm, list current hourly rates by
   timekeeper level (Partner, Of Counsel, Senior Associate, Associate, Paralegal).

2. **Apply market benchmarks** using Wolters Kluwer ELM Real Rate Report and ACC data
   [VERIFY current rates — billing rates change annually]:

   | Timekeeper Level          | US National Median Rate | Range (25th–75th %ile) |
   | ------------------------- | ----------------------- | ---------------------- |
   | Partner                   | $600–$900/hr            | $450–$1,200/hr         |
   | Of Counsel                | $450–$700/hr            | $350–$900/hr           |
   | Senior Associate (5+ yrs) | $350–$550/hr            | $275–$700/hr           |
   | Associate (1–4 yrs)       | $250–$400/hr            | $175–$550/hr           |
   | Paralegal                 | $150–$250/hr            | $100–$350/hr           |

   [JURISDICTION-SPECIFIC] UK, EU, APAC, and other markets have materially different
   rate structures. Apply geography-adjusted benchmarks when outside counsel is
   located outside the US. [VERIFY current rates for applicable geography]

3. **Calculate rate variance** for each timekeeper level:

   ```
   Rate Variance = (Actual Rate – Market Median Rate) / Market Median Rate × 100
   ```

   - Positive variance: Organization is paying above median
   - Negative variance: Organization is paying below median (favorable)

4. **Assess blended rate efficiency**: Compare the firm's weighted average blended
   rate to the market median for the matter type:
   - Complex litigation: typically higher blended rates (partner-heavy)
   - Routine transactions: mid-tier rates acceptable (associate-heavy is efficient)
   - Regulatory/compliance: varies by specialization premium

5. **Staffing mix analysis**: Review the ratio of partner hours to associate hours
   to paralegal hours. For each matter type, flag deviations from efficient staffing:
   - Over-partnering: Partner hours > 40% on routine matters is typically inefficient
   - Under-staffing paralegal/associate: Missing delegation opportunities

**Rate deviation classification:**

| Classification | Rate vs. Median      | Action                                     |
| -------------- | -------------------- | ------------------------------------------ |
| **EFFICIENT**  | Within 10% of median | No action required                         |
| **MONITOR**    | 10–25% above median  | Review at next rate negotiation cycle      |
| **OPTIMIZE**   | 25%+ above median    | Immediate negotiation or firm substitution |

**⟁ CLARIFY** — If the organization has a long-standing relationship with a firm
charging OPTIMIZE-level rates, ask:

- "This firm is billing at [X]% above market median. Does the relationship justify the
  premium (e.g., specialized expertise, strategic relationship, outcome track record),
  or should we model a rate negotiation scenario?"

### Step 6: Matter-Type Cost Analysis

Analyze spending by matter type to identify where the most significant costs arise and
whether they reflect appropriate legal priorities.

**Matter taxonomy** (adapt to the organization's actual classification):

| Matter Category              | UTBMS Phase | Typical Cost Drivers                            |
| ---------------------------- | ----------- | ----------------------------------------------- |
| Litigation & Disputes        | L100–L650   | Partner hours, discovery, expert fees           |
| M&A / Corporate Transactions | C100–C300   | Deal complexity, diligence depth, timeline      |
| Employment & Labor           | L100 + A115 | Settlement costs, compliance, HR disputes       |
| Intellectual Property        | B100–B400   | Patent prosecution, licensing, enforcement      |
| Regulatory & Compliance      | A100–A115   | Specialist rates, regulatory complexity         |
| Commercial Contracts         | C100–C300   | Contract volume, complexity, negotiation cycles |
| Real Estate                  | C100        | Deal size, lease complexity                     |
| Data Privacy                 | A100        | Regulatory complexity, jurisdiction count       |
| Routine / Self-Service       | N/A         | Internal resource cost only                     |

**Analysis outputs:**

- **Spend by category** (pie chart values or % table)
- **Year-over-year trend** by category (where multi-year data is available)
- **Cost per matter by category**: Compare to industry benchmarks where available
- **Matter volume trend**: Rising volume with falling cost per matter = efficiency gain

**Cost concentration analysis:**

```
Top N Matter Concentration = Spend on Top N Matters / Total Outside Counsel Spend × 100
```

If the top 10 matters represent more than 50% of outside counsel spend, flag this as
high concentration risk — loss of a key matter could significantly alter spend patterns.

**⟁ CLARIFY** — When a matter category shows significantly higher spend than industry
norms, ask whether this reflects:

- A specific known legal event (litigation, regulatory investigation, major transaction)
- An ongoing structural pattern that may warrant insourcing or AFA structuring
- A data classification issue (matters miscoded to the wrong category)

### Step 7: Alternative Fee Arrangement (AFA) Evaluation

Evaluate existing AFAs for financial performance, or model a proposed AFA against
the historical hourly cost baseline.

#### 7a. AFA Type Reference

| AFA Type                    | Description                                                     | Best For                                          | Key Risk                                                         |
| --------------------------- | --------------------------------------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------- |
| **Fixed/Flat Fee**          | Single price for defined scope                                  | Routine matters, standard transactions            | Scope creep undermines economics                                 |
| **Capped Fee**              | Hourly billing with a ceiling                                   | Matters with variable scope and known upper bound | Firm may slow-walk work near the cap                             |
| **Blended Rate**            | Single hourly rate across all timekeepers                       | Simplified billing; all timekeeper levels         | May incentivize over-staffing at senior level                    |
| **Success/Performance Fee** | Contingent on outcome (win, settlement, recovery)               | Litigation, regulatory defense                    | Creates misaligned incentives if not structured carefully        |
| **Subscription/Retainer**   | Monthly/annual fixed fee for a defined scope of ongoing service | High-volume routine matters, ongoing advisory     | Underuse is value leakage; overuse is a loss leader for the firm |
| **Collared Fee**            | Hourly billing with floor and ceiling (e.g., ±15% variance)     | Standard complexity matters                       | Complex to administer                                            |
| **Portfolio AFA**           | Bundled pricing across a portfolio of similar matters           | High-volume litigation, regulatory filings        | Requires accurate matter taxonomy                                |

#### 7b. AFA Financial Modeling

For any proposed AFA, model the economics against the historical hourly baseline:

**For a flat fee proposal:**

```
Historical Cost Baseline = Historical avg. hours for this matter type × Blended hourly rate
AFA Premium/Discount = (Proposed Flat Fee – Historical Baseline) / Historical Baseline × 100
Break-even Hours = Proposed Flat Fee / Blended Hourly Rate
```

Classify the AFA proposal:

- **FAVORABLE**: AFA ≤ 90% of historical baseline (≥10% savings)
- **MARKET**: AFA 90–110% of historical baseline (within 10% variance)
- **REVIEW**: AFA > 110% of historical baseline (>10% above baseline)
- **REJECT**: AFA > 125% of historical baseline without special justification

**For a portfolio AFA:**

- Calculate weighted average cost per matter at hourly rates
- Model expected matter volume and complexity distribution
- Test sensitivity: what if volume is 20% lower than expected? 20% higher?
- Identify the breakeven matter volume above which the portfolio AFA is favorable

**Adoption trend context** [VERIFY current data]:

- 84% of large law firms offer some form of AFA
- Flat fees and capped arrangements are the most commonly adopted
- 61% of legal departments use flat fees for at least some matter types (ACC data)

**⟁ CLARIFY** — When modeling an AFA, ask the user:

- "Do you have historical data on hours and fees for this matter type? Accurate modeling
  requires at least 6–12 months of comparable matter history."
- "Who bears the risk of scope change? This is the key question for any fixed-fee
  arrangement — the answer determines who benefits from an efficient resolution."

#### 7c. AFA Performance Tracking

For existing AFAs, assess performance:

| Metric               | Formula                                                                            | Target                  |
| -------------------- | ---------------------------------------------------------------------------------- | ----------------------- |
| AFA Savings Rate     | (Estimated Hourly Equivalent – Actual AFA Fee) / Estimated Hourly Equivalent × 100 | ≥10%                    |
| Scope Adherence Rate | Matters completed within original AFA scope / Total AFA matters × 100              | ≥85%                    |
| Scope Creep Rate     | Matters requiring out-of-scope fees / Total AFA matters × 100                      | <15%                    |
| AFA Coverage Rate    | Outside counsel spend under AFA / Total outside counsel spend × 100                | Target per org strategy |

### Step 8: Legal Operations Efficiency Metrics

Measure the operational performance of the legal department against CLOC-aligned benchmarks.

#### 8a. CLOC Core 12 Functional Area Assessment

The CLOC Core 12 defines 12 functional areas for legal department management maturity.
Assess the organization's current maturity level (Reactive → Emerging → Developing →
Leading) for each function:

| #   | Functional Area              | Key Indicators of Maturity                                             |
| --- | ---------------------------- | ---------------------------------------------------------------------- |
| 1   | Strategic Planning           | Legal aligned to business strategy; defined mission; OKRs/KPIs tracked |
| 2   | Financial Management         | Budget ownership; cost centers; EAC forecasting; spend analytics       |
| 3   | Firm and Vendor Management   | Preferred panel; OCGs in place; AFA adoption; performance scorecards   |
| 4   | Technology                   | E-billing; CLM; matter management; AI adoption; documented tech stack  |
| 5   | Information Governance       | Document retention; matter files organized; knowledge management       |
| 6   | Organization Design          | Right-sizing model; staffing mix; org chart; roles defined             |
| 7   | Sourcing                     | Insourcing vs. outsourcing analysis; ALSPs used where appropriate      |
| 8   | Practice Operations          | Standardized workflows; self-service tools; intake processes           |
| 9   | Training and Development     | Legal team learning paths; compliance training tracked                 |
| 10  | Support and Customer Service | SLAs for internal clients; satisfaction tracking                       |
| 11  | Regulatory Compliance        | Compliance posture tracked; horizon scanning                           |
| 12  | Litigation Management        | Litigation hold process; matter portfolio oversight                    |

For spend analysis, **Financial Management (#2)** and **Firm and Vendor Management (#3)**
are the primary CLOC functions engaged.

#### 8b. Key Efficiency Metrics

| KPI                                    | Formula                                                        | Target / Benchmark                                   |
| -------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------- | -------------- | ------------------------------------ |
| **Time to Respond (intake)**           | Time from request submitted to legal team acknowledgment       | <24 hours for standard; <2 hrs for urgent            |
| **Matter Cycle Time**                  | Average days from matter open to matter closed, by matter type | Baseline varies by type; track trend                 |
| **Contract Turnaround Time**           | Days from contract request to fully executed agreement         | 5–10 days for standard commercial contracts [VERIFY] |
| **Matter Volume per Attorney (FTE)**   | Total open matters / FTE attorneys                             | Varies by matter type; track capacity utilization    |
| **Team Capacity Utilization**          | Hours on matters / Total available hours × 100                 | Target 70–85% billable capacity                      |
| **Outside Counsel Invoice Compliance** | Invoices meeting OCG requirements / Total invoices × 100       | ≥95% for active OCG programs                         |
| **Outside Counsel Rejection Rate**     | Rejected invoice line items / Total invoice line items × 100   | <5% for well-managed relationships                   |
| **Budget Accuracy**                    |                                                                | Actual Spend – Budget                                | / Budget × 100 | <10% variance for mature departments |

#### 8c. Self-Service and Deflection Rate Metrics

Self-service deflection measures how effectively the legal department scales through
automation and templates rather than headcount.

**Key metrics:**

| Metric                           | Formula                                                                  | Interpretation                                                      |
| -------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| **Self-Service Deflection Rate** | Requests resolved via self-service tools / Total legal requests × 100    | Higher = better scaling; leading programs achieve 20–40% deflection |
| **Self-Service Adoption Rate**   | Active users of self-service tools / Total eligible users × 100          | Target ≥70% adoption within 12 months of deployment                 |
| **Automation Deflection Rate**   | Matters auto-routed or auto-resolved / Total intake volume × 100         | Tracks smart triage effectiveness                                   |
| **Template Utilization Rate**    | Contracts completed using pre-approved templates / Total contracts × 100 | Higher = reduced attorney time per contract                         |
| **Legal FAQs Served**            | Count of self-service FAQ views that prevented a legal request           | Proxy metric; requires intake system to track                       |

**Interpreting deflection rates:**

| Deflection Rate | Maturity Level | Interpretation                                                        |
| --------------- | -------------- | --------------------------------------------------------------------- |
| <5%             | Reactive       | Minimal self-service investment; high attorney time per request       |
| 5–15%           | Emerging       | Basic templates and FAQs deployed; adoption building                  |
| 15–30%          | Developing     | Structured self-service portal; automated routing; CLM adoption       |
| >30%            | Leading        | AI-assisted triage; integrated with business systems; high automation |

**⟁ CLARIFY** — If self-service data is not tracked, ask:

- "Does your legal department use a legal intake portal, contract self-service tool, or
  legal FAQ system? If so, do you have data on requests handled without attorney
  involvement? This metric is one of the best indicators of legal ops scalability."

### Step 9: Budget Forecasting and Variance Analysis

Build or validate the legal department budget using structured financial management
methodology.

#### 9a. Annual Budget Framework

Structure the legal budget in three layers:

**Layer 1 — Inside Counsel Costs:**

- Attorney compensation (salary + bonus + benefits): typically 65–75% of inside costs
- Legal ops and paralegal staff compensation: typically 15–20% of inside costs
- Overhead allocation (space, IT, etc.): typically 10–15% of inside costs

**Layer 2 — Outside Counsel Costs:**

- Budget by matter category (from Step 6 taxonomy)
- Budget by law firm (for convergence programs)
- Reserve for unplanned/emergency matters (typically 10–15% contingency)

**Layer 3 — Legal Technology and Other Costs:**

- E-billing and matter management platform fees
- CLM platform fees
- Other legal tech subscriptions
- Training and professional development
- Filing fees, court costs, expert fees (if not embedded in outside counsel)

#### 9b. EAC (Estimate at Completion) for Active Matters

For matters in progress, forecast the final cost using the EAC methodology:

```
EAC = ACWP + ETC

Where:
  ACWP = Actual Cost of Work Performed to date
  ETC  = Estimate to Complete (remaining work)

For steady-pace matters (performance consistent with plan):
  ETC = (BAC – BCWP) / CPI
  CPI = BCWP / ACWP (Cost Performance Index)

Where:
  BAC  = Budget at Completion (original estimate)
  BCWP = Budgeted Cost of Work Performed (% complete × BAC)
```

**Variance classification:**

| Variance (EAC vs. BAC) | Status       | Action                                                            |
| ---------------------- | ------------ | ----------------------------------------------------------------- |
| EAC ≤ BAC              | **ON-TRACK** | No intervention needed                                            |
| EAC = BAC + 10–25%     | **MONITOR**  | Investigate drivers; may need supplemental budget                 |
| EAC > BAC + 25%        | **OPTIMIZE** | Escalate; review matter strategy; consider AFA or scope reduction |

**Portfolio EAC:** Sum all individual matter EACs to forecast total outside counsel
spend for the period. Compare to the annual outside counsel budget to project year-end
variance.

#### 9c. Accrual Management

For accurate financial reporting, manage accruals for legal fees not yet invoiced:

- **Outstanding work estimate**: Request quarterly (or monthly) estimates from all
  active outside counsel for work performed but not yet invoiced
- **Accrual aging**: Track accruals by quarter and clear stale accruals
- **Invoice lag**: Measure average days from work performed to invoice receipt — flag
  firms with chronic >60-day lag as a financial management risk
- **Accrual accuracy**: Track variance between accrual estimates and actual invoices
  received — firms with consistent >20% variance should be placed on tighter accrual
  protocols

**⟁ CLARIFY** — If the organization does not currently manage accruals formally, ask:

- "Is accrual-based financial reporting required for your legal budget (e.g., for public
  company accounting, GAAP/IFRS compliance)? If yes, I can prioritize building an
  accrual management framework. If no, cash-basis tracking may be sufficient."

### Step 10: Legal Technology ROI Analysis

Calculate the financial return on legal technology investments.

#### 10a. ROI Framework

```
ROI = (Total Value of Benefits – Total Costs) / Total Costs × 100

Where ROI > 100% indicates benefits exceed costs in the measurement period
Payback Period = Total Costs / Annual Net Benefits (in years)
```

**Cost categories:**

- Licensing fees (annual SaaS subscription or per-seat fee)
- Implementation costs (professional services, customization, data migration)
- Internal resource costs (FTE time for implementation and ongoing administration)
- Training costs
- Integration costs (with other systems)

**Benefit categories:**

| Technology              | Primary Benefits                                                                 | How to Quantify                                                                      |
| ----------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **E-Billing Platform**  | Invoice review time reduction; guideline compliance enforcement; rate validation | Hours saved × attorney/paralegal hourly cost + % reduction in overbilling            |
| **CLM System**          | Contract cycle time reduction; template compliance; obligation tracking          | Hours saved × attorney cost + revenue value of faster contract execution             |
| **Matter Management**   | Matter tracking efficiency; reporting automation; outside counsel oversight      | FTE hours saved on reporting + improved outside counsel performance (cost reduction) |
| **AI Legal Tools**      | Research time reduction; document review acceleration; drafting assistance       | Hours saved × attorney cost + risk reduction value                                   |
| **Self-Service Portal** | Deflection rate × average attorney cost per deflected request                    | Deflected requests × avg. attorney hourly cost × avg. hours per request              |

#### 10b. Legal Tech ROI Scorecard Template

For each legal technology investment, calculate:

```
Tool: [e.g., CLM Platform X]
Annual License Cost: $[X]
Implementation Cost (amortized): $[Y]/year
Internal Admin Cost: $[Z FTE × cost]
Total Annual Cost (TAC): $[sum]

Annual Benefits:
  Time savings: [hours saved] × $[fully-loaded hourly rate] = $[A]
  Compliance savings (avoided rework, overbilling): $[B]
  Risk reduction (value of prevented incidents): $[C] [VERIFY methodology]
  Revenue acceleration (faster contract execution): $[D]
Total Annual Benefits (TAB): $[sum]

ROI = (TAB – TAC) / TAC × 100 = [X]%
Payback Period = TAC / TAB = [Y] years
```

**Adoption leading indicator**: Target 80% active user adoption within 90 days of
deployment. Tools below 50% adoption at 90 days are unlikely to deliver projected ROI —
flag for adoption intervention before the ROI model is considered reliable.

**⟁ CLARIFY** — When calculating ROI for AI tools, ask:

- "How are you measuring attorney time savings — tracked time in a matter management
  system, self-reported surveys, or controlled before/after studies? The methodology
  significantly affects the reliability of the ROI calculation."

### Step 11: Quality Verification

Before delivering the analysis, run the quality checks below.

1. Run the 5 **Data Quality Gates** silently. Revise failures before delivery.
2. For every **OPTIMIZE-tier finding**, run the 3-pass **Self-Interrogation**. Revise
   if any pass reveals a weakness.
3. Assign a **Confidence Score** to each major finding.
4. Verify that all benchmark comparisons state the source and survey date.
5. Confirm that all [JURISDICTION-SPECIFIC] markers are correctly placed.
6. Generate the **Glass Box Audit Trail** and append to the output.

### Step 12: legalcode-mcp Integration

**⟁ CLARIFY** — If legalcode-mcp is connected, ask whether to use it to:

- Verify current CLOC State of the Industry report data
- Confirm current ACC benchmarking figures
- Search for regulatory requirements affecting the legal department's spend
  (e.g., SOX documentation requirements, GDPR DPA compliance costs)

**With legalcode-mcp connected (preferred):**

- Search for current benchmark data and regulatory frameworks relevant to the
  organization's industry and jurisdiction
- Verify currency of billing ethics rules affecting AFA structuring
- Mark all legalcode-mcp-sourced data as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with benchmark data cited in this skill (marked [VERIFY])
- Note in the Glass Box: `legalcode_mcp: "Not connected — benchmark data requires
verification against current survey sources"`

---

## Spend Analysis Reference

### CLOC Core 12 Financial Management Maturity Levels

For the Financial Management function (Core 12, Area #2), assess maturity against these
indicators:

| Maturity Level | Budget                                        | Forecasting                             | Reporting           | Spend Analytics                   |
| -------------- | --------------------------------------------- | --------------------------------------- | ------------------- | --------------------------------- |
| **Reactive**   | No formal budget; reactive to invoices        | No forecasting                          | Ad hoc, if any      | None                              |
| **Emerging**   | Annual budget exists; limited tracking        | Simple accrual estimates                | Quarterly summary   | Basic spend totals                |
| **Developing** | Budget by category; variance tracked          | EAC per matter                          | Monthly dashboard   | Spend by firm/category            |
| **Leading**    | Budget by matter type with EAC; AFA-optimized | Predictive modeling; automated accruals | Real-time dashboard | CLOC benchmarked; driver analysis |

### LEDES and UTBMS Code Reference

**UTBMS Phase Categories for Spend Analysis:**

| Phase                           | Code Range | Typical Work                                  |
| ------------------------------- | ---------- | --------------------------------------------- |
| Case Assessment / Dev. & Admin. | L100       | Initial case evaluation, strategy             |
| Pre-Trial Pleadings             | L200       | Complaint, answer, motions                    |
| Discovery                       | L300       | Depositions, document review, interrogatories |
| Trial Preparation               | L400       | Exhibits, witness prep, pre-trial motions     |
| Trial / Hearing                 | L500       | Court appearances, testimony                  |
| Appeal                          | L600       | Appellate briefing, oral argument             |
| Counseling (General)            | A100       | General advice and guidance                   |
| Regulatory / Administrative     | A106–A115  | Agency proceedings, compliance                |
| Business Transactions           | C100–C300  | M&A, finance, commercial contracts            |
| Bankruptcy / Insolvency         | B100–B400  | Restructuring, creditor matters               |

**LEDES File Versions Commonly in Use:** LEDES 1998B (most common), LEDES 2000
(XML-based), LEDES 1998BI (insurance), LEDES Timekeeper (rate cards)

### Outside Counsel Rate Benchmarks (US-Centric) [VERIFY against current surveys]

**Rate benchmarks vary by practice area, firm size, and geography:**

| Practice Area           | Typical Premium/Discount to National Average |
| ----------------------- | -------------------------------------------- |
| M&A (elite firms)       | +50–150%                                     |
| IP Litigation           | +30–80%                                      |
| General Litigation      | Market                                       |
| Employment              | Market to –10%                               |
| Real Estate             | –10–20%                                      |
| Regulatory / Government | +20–60% (specialist premium)                 |
| Routine Contracts       | –15–30%                                      |

**Firm tier adjustments:**

- Am Law 1–50: +40–100% above national median
- Am Law 51–200: +10–40% above median
- Am Law 201+: Near median to –10%
- Regional / Boutique: –20–40% (with specialist exceptions)

[JURISDICTION-SPECIFIC] Non-US rate structures differ significantly. UK magic circle
average partner rates (£900–£1,500+/hr); German top-tier (€500–€900/hr); Singapore
(SGD 700–1,200+/hr) — apply market-specific benchmarks [VERIFY current data].

### Key Financial Formulas Reference

```
Total Legal Spend % Revenue = (Inside + Outside + Other legal costs) / Revenue × 100
Inside/Outside Ratio = Inside legal costs / Outside legal costs
Cost Per Matter = Total outside counsel fees / Total matter count
AFA Savings Rate = (Estimated hourly equivalent – Actual AFA fee) / Estimated hourly equivalent × 100
EAC = ACWP + ETC
Budget Variance % = (Actual – Budget) / Budget × 100
Self-Service Deflection Rate = Deflected requests / Total requests × 100
Legal Tech ROI = (Annual Benefits – Annual Costs) / Annual Costs × 100
Rate Variance = (Actual Rate – Market Median) / Market Median × 100
Invoice Rejection Rate = Rejected line items / Total line items × 100
```

---

## Status Classification

Legal spend findings are classified in a three-tier system adapted to financial performance:

### EFFICIENT — Performing at or Better Than Benchmark

The metric is within or below the benchmark range. No material action required. Document
the positive performance as a baseline for future periods.

**Examples:**

- Total legal spend at 0.5% of revenue (industry median 0.63%)
- Outside counsel rates within 10% of market median
- AFA savings rate consistently ≥15%
- Self-service deflection rate ≥25%
- Invoice rejection rate <3%

**Action**: Note for benchmarking record. No intervention needed.

### MONITOR — Approaching or Slightly Above Benchmark

The metric is within a negotiable or improvable range. The department is slightly above
industry benchmarks or showing a deteriorating trend that warrants attention.

**Examples:**

- Total legal spend at 0.9% of revenue (above median but within 75th percentile)
- Outside counsel rates 10–25% above market median
- AFA savings rate 5–10% (below target but not negative)
- Deflection rate 5–15% (low but shows some self-service investment)
- EAC 10–25% above BAC on key matters

**Action**: Investigate drivers. Set a 90-day improvement target. Monitor monthly.

### OPTIMIZE — Significantly Above Benchmark or Negative Trend

The metric significantly exceeds industry benchmarks, shows a negative trend, or
represents a material cost optimization opportunity. Requires active intervention.

**Examples:**

- Total legal spend >1.5% of revenue without known business reason (e.g., major litigation)
- Outside counsel rates >25% above market median
- AFA savings rate negative (AFA costs more than hourly equivalent)
- Deflection rate <5% despite stated intent to build self-service capability
- EAC >25% above BAC on key matters
- Invoice rejection rate >10% (indicative of OCG non-compliance or billing issues)

**Action**: Develop a specific optimization plan. Set quantified targets. Assign ownership.
Escalate to GC/CFO level if material.

---

## Actionable Recommendations

For each MONITOR or OPTIMIZE finding, generate a recommendation using this format:

```
**Finding**: [Metric name and current value vs. benchmark]
**Classification**: [MONITOR / OPTIMIZE]
**Driver Analysis**: [1–2 sentences identifying the likely root cause]
**Recommended Action**: [Specific, actionable step — not vague guidance]
**Expected Impact**: [Quantified estimate of cost reduction or efficiency gain]
**Timeline**: [Immediate (30 days) / Near-term (90 days) / Strategic (6–12 months)]
**Owner**: [GC / Legal Ops / Finance / Outside Counsel Manager]
**Success Metric**: [How to measure that the action worked]
```

---

## Prioritization Framework

Organize findings by cost impact and implementation effort:

### Tier 1 — High Impact, Immediate Action (Cost Reduction > 10% of Category Budget)

- Outside counsel rates >25% above market for high-volume matter types
- AFA proposals priced significantly above historical hourly equivalent
- Top 3 law firms with consistent OPTIMIZE-level billing behavior
- EAC overruns >25% on matters in active phases (scope/strategy review needed)
- Invoice line items consistently rejected at >10% rate (OCG enforcement needed)

### Tier 2 — Strategic Improvements (Cost Reduction 5–10% of Category Budget)

- Matter type insourcing opportunities (high-volume routine matters)
- AFA conversion of matters currently priced at hourly with predictable scope
- Self-service portal deployment for contract templates and legal FAQs
- LEDES/UTBMS adoption to enable accurate matter-type cost tracking
- Convergence program rationalization (reduce to 3–5 primary firms per practice area)

### Tier 3 — Long-Term Optimization (Process and Technology)

- Legal tech ROI improvement (adoption intervention for underperforming tools)
- CLOC Core 12 maturity advancement (from Emerging to Developing in Financial Management)
- Predictive spend modeling capability development
- Cross-departmental chargeback implementation to align legal cost transparency
- Annual rate negotiation calendar and benchmark-driven rate card review process

---

## Quality Assurance Framework

### Data Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate              | Rule                                                                                           | Fail Action                                                    |
| ----------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Source**        | Every benchmark figure cites a specific survey, report, or dataset with a date                 | Add source or mark "[SOURCE REQUIRED]"                         |
| **Currency**      | All benchmark data checked for age — surveys >3 years old should be flagged                    | Flag as "[CHECK CURRENCY — survey may be outdated]"            |
| **Comparability** | Benchmarks are applied to comparable populations (same industry tier, company size, geography) | Note population difference and apply adjustment factor or flag |
| **Domain**        | Analysis stays within the scope of the data provided — no extrapolation beyond the dataset     | Remove or flag extrapolation                                   |
| **Confidence**    | Uncertainty explicitly stated, not hidden. If a finding depends on estimated data, say so      | Add confidence qualifier                                       |

### Self-Interrogation for OPTIMIZE-Tier Findings

For any metric classified as OPTIMIZE, apply this 3-pass review before delivering:

**Pass 1 — Data Integrity**: Does the finding follow logically from the data? Is there a
data normalization issue (e.g., multi-currency mixing, incomplete period data) that could
explain the result? Would a finance professional reach the same conclusion?

**Pass 2 — Completeness**: Have all relevant cost drivers been considered? Are there known
exceptional factors (major litigation, M&A, regulatory investigation) that legitimately
explain the elevated spend? Is this a trend or a one-time event?

**Pass 3 — Challenge**: What is the strongest argument that this finding does NOT require
intervention? What would the organization lose if the recommended action is taken? Are
there relationship, quality, or strategic factors that justify the spend premium?

If any pass reveals a weakness, revise the finding before delivery. Mark the audit trail
with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each major finding or benchmark comparison:

| Level        | Range     | Meaning                                                     | Action                                                  |
| ------------ | --------- | ----------------------------------------------------------- | ------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Based on verified organizational data vs. current benchmark | State with confidence                                   |
| **High**     | 0.80–0.94 | Based on reasonable data with minor estimation              | State with brief caveat                                 |
| **Probable** | 0.60–0.79 | Based on partial data or estimated figures                  | State with explicit reasoning                           |
| **Possible** | 0.40–0.59 | Significant estimation; limited data                        | Flag for validation before acting                       |
| **Unlikely** | 0.0–0.39  | Highly speculative; benchmark may not apply                 | Do not assert; flag "[UNCERTAIN — requires validation]" |

---

## Glass Box Audit Trail

Every legal spend analysis MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-legal-spend-analysis"
  analysis_date: "[date]"
  company_profile:
    revenue_range: "[<$100M / $100M-$500M / $500M-$1B / $1B-$5B / $5B-$20B / >$20B]"
    industry: "[industry]"
    jurisdiction: "[primary jurisdiction(s)]"
  analysis_scope:
    period_covered: "[year / months]"
    data_provided: "[LEDES files / ELM export / Manual figures / Prompt only]"
    modules_run: "[list of workflow steps executed]"
  benchmark_sources:
    - "[ACC 2023 LDMB Report — VERIFY currency]"
    - "[Wolters Kluwer ELM Real Rate Report — VERIFY currency]"
    - "[CLOC State of the Industry — VERIFY currency]"
    - "[Other sources used]"
  legalcode_mcp: "Connected / Not connected"
  data_quality: "HIGH / MEDIUM / LOW — [notes on data completeness and limitations]"
  findings_count:
    efficient: "[number]"
    monitor: "[number]"
    optimize: "[number]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no OPTIMIZE findings)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, data gaps, or caveats]"
    - "[Benchmarks are from [year] surveys — verify currency before acting]"
  reviewer: "AI-assisted — requires qualified legal operations and finance review"
```

---

## Anti-Patterns

Catalogue of what NOT to do in legal spend analysis:

1. **Applying industry benchmarks without size adjustment** — A 50-attorney legal
   department's 0.8% spend-to-revenue ratio may be perfectly normal for a $500M company
   but severely high for a $5B company. Always size-adjust before flagging.

2. **Mixing inside and outside counsel costs in a single rate metric** — Total legal
   spend as % of revenue is a portfolio metric. Conflating it with outside counsel-only
   metrics produces distorted comparisons. Keep inside and outside costs clearly separated
   throughout.

3. **Using stale benchmark data** — Legal billing rate surveys are published annually.
   Using 2020 rate benchmarks for 2026 rate negotiations is worse than no benchmark —
   it will produce systematically low comparisons as rates have increased materially in
   the interim. Always cite the survey year and check for updates.

4. **Treating LEDES as billing accuracy** — A cleanly formatted LEDES file only means
   the invoice was submitted in the correct format. It does not mean the underlying time
   entries are accurate, reasonable, or guideline-compliant. LEDES is a data standard,
   not a quality guarantee.

5. **Recommending AFA conversion without matter history** — Proposing that a matter type
   move to a flat fee without 6–12 months of comparable matter cost data is speculation.
   The firm will price the AFA based on their own history; without yours, you have no
   basis for evaluating whether their proposal is fair.

6. **Conflating rate with value** — The cheapest hourly rate is not always the best value
   if it comes with inefficient staffing (over-partnering), longer timelines, or weaker
   outcomes. Rate benchmarking is necessary but not sufficient; augment with matter
   outcome and cycle time data.

7. **Self-service deflection without user experience data** — A legal portal that deflects
   40% of requests is only valuable if users are getting accurate answers. A high
   deflection rate masking a high "re-engagement rate" (users who couldn't get what they
   needed and came back) is a false efficiency. Track completion rates, not just deflection
   rates.

8. **Building budget from historical spend without driver analysis** — "Last year we spent
   $X, so we'll budget $X + inflation" is a reactive approach. Legal spend is driven by
   matter volume and complexity, not time. Budget from expected matter pipeline, then
   validate against historical cost-per-matter data.

9. **Over-indexing on invoice rejection rate** — A very high rejection rate (>15%) does not
   always indicate firm misbehavior; it may indicate that OCG requirements are unclear,
   outdated, or inconsistently applied. Before attributing a high rejection rate to the
   firm, audit the OCG for ambiguity.

10. **EAC without regular refresh** — Estimate at Completion forecasts are only useful if
    updated as the matter progresses. An EAC calculated at matter inception and never
    refreshed is as useless as no forecast at all. Require monthly EAC updates for
    matters exceeding budget thresholds.

11. **Panel consolidation as a substitute for rate discipline** — Reducing from 40 firms to
    10 is a management improvement, not a rate negotiation. Consolidation creates leverage;
    leverage must be converted to actual rate reductions through negotiation. Consolidation
    without rate renegotiation does not save money.

12. **Ignoring alternative legal service providers (ALSPs)** — For high-volume, lower-complexity
    work (document review, contract abstraction, due diligence support), ALSPs typically
    price at 30–60% below traditional law firm rates for comparable quality. A spend
    analysis that does not consider ALSP alternatives for eligible matter types is incomplete.

13. **Legal tech ROI based on vendor projections alone** — Every vendor claims significant
    ROI. Use the vendor's projections as a starting point, then validate against
    organizations of comparable size and industry that have deployed the same tool.
    Conduct a pilot with a defined success metric before committing to a multi-year contract.

14. **Currency and time period inconsistency** — Multi-jurisdiction legal departments that
    analyze spend in mixed currencies without normalizing to a single reporting currency
    will produce meaningless benchmarks. Similarly, comparing Q1 actuals to a full-year
    budget without annualizing produces systematically misleading variance analysis.

15. **Ignoring accruals in budget variance reporting** — Cash-basis spend reporting that
    omits accruals for work performed but not yet invoiced will systematically understate
    the run rate in Q4 (when firms submit year-end invoices) and overstate savings. Accrual
    management is not optional for accurate budget variance reporting.

16. **Treating all law firm relationships as purely economic** — Legal spend optimization
    is necessary but must account for non-economic factors: relationship tenure, matter
    outcome track record, specialty expertise, and market reputation. A purely economic
    model that recommends firing the firm with the best track record to save 8% on rates
    may be technically correct and strategically wrong.

17. **Snapshot analysis without trend** — A single period's spend figures tell you where
    you are; they do not tell you whether you are improving or deteriorating. Always
    include at least two periods of comparison before recommending structural changes.

---

## Writing Standards

Apply plain-language discipline to all output:

**For executive summaries** (read by GC, CFO, or CLT):

- One key finding per bullet
- Quantify: "$X saved" not "significant savings achieved"
- State the benchmark source and date
- Lead with the finding, not the methodology

**For recommendation sections** (read by legal ops team):

- Action-oriented imperative verbs: "Renegotiate," "Deploy," "Measure," "Eliminate"
- Owner and timeline for each action
- Success metric defined

**Quality gates before delivery:**

1. Can a non-lawyer CFO understand the executive summary?
2. Is every benchmark comparison sourced and dated?
3. Are any estimates labeled as estimates (not stated as facts)?
4. Has every OPTIMIZE finding been through self-interrogation?
5. Is the Glass Box audit trail complete and honest about data limitations?

---

## External Tool Integration

**With legalcode-mcp connected:**

- Search for current ACC, CLOC, and Wolters Kluwer survey data relevant to the
  organization's industry and size
- Verify current billing ethics rules affecting AFA structuring in applicable jurisdiction
- Search for ALSP market data and legal tech adoption benchmarks
- Mark all legalcode-mcp-sourced data as VERIFIED in the Glass Box audit trail
- Save research results to `/tmp/legalcode-spend-analysis-research.md`

**With e-billing platform connected (Brightflag, SimpleLegal, Onit, Legal Tracker):**

- Extract actual LEDES data for the analysis period
- Pull real-time matter-level EAC from the platform
- Generate rate card comparison against embedded benchmarks
- Automate accrual collection from connected law firms

**Without external tools:**

- Proceed with benchmark-based analysis using data cited in this skill
- Mark all benchmark figures with [VERIFY] and the survey source
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Instruct the user to validate all benchmarks against current survey sources before
  using figures in negotiations or board presentations

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Legal Spend Analysis Report

**Organization Profile**: [Industry | Revenue Range | FTE Attorneys]
**Analysis Period**: [period covered]
**Data Basis**: [LEDES files / ELM export / Manual figures / Benchmark-based]
**Date of Analysis**: [date]
**Prepared Using**: Legalcode Legal Spend Analysis Skill

---

## Executive Summary

**Total Legal Spend**: $[X] ([Y]% of revenue — [EFFICIENT / MONITOR / OPTIMIZE] vs.
industry median of [Z]%)
**Inside/Outside Split**: [A]% / [B]% — [classification vs. benchmark]
**Top Finding**: [Single most important finding in 1–2 sentences]
**Key Opportunity**: [Top cost optimization opportunity with estimated $ impact]

---

## 1. Spend Baseline Assessment

| Metric                      | Current | Benchmark (25th %ile) | Benchmark (Median) | Benchmark (75th %ile) | Classification |
| --------------------------- | ------- | --------------------- | ------------------ | --------------------- | -------------- |
| Total Legal Spend % Revenue | [X]%    | [A]%                  | [B]%               | [C]%                  | [Status]       |
| Inside/Outside Ratio        | [X]/[Y] | [A]/[B]               | [C]/[D]            | [E]/[F]               | [Status]       |
| [Other metrics...]          |         |                       |                    |                       |                |

**Benchmark source**: [ACC 2023 LDMB Report or other — date] [VERIFY currency]

---

## 2. Outside Counsel Rate Analysis

**Overall Assessment**: [Summary of rate performance vs. market]

| Law Firm      | Timekeeper Level | Current Rate | Market Median | Variance | Classification |
| ------------- | ---------------- | ------------ | ------------- | -------- | -------------- |
| [Firm A]      | Partner          | $[X]/hr      | $[Y]/hr       | [+/-Z]%  | [Status]       |
| [Firm A]      | Associate        | $[X]/hr      | $[Y]/hr       | [+/-Z]%  | [Status]       |
| [Continue...] |                  |              |               |          |                |

**Recommendations**:

- [Finding + Recommended Action + Expected Impact]

---

## 3. Matter-Type Cost Analysis

**Spend by Category**:

| Matter Category | Spend | % of Total | Cost Per Matter | YoY Change | Classification |
| --------------- | ----- | ---------- | --------------- | ---------- | -------------- |
| [Category]      | $[X]  | [Y]%       | $[Z]            | [+/-A]%    | [Status]       |
| [Continue...]   |       |            |                 |            |                |

---

## 4. AFA Performance and Opportunities

**Current AFA Coverage**: [X]% of outside counsel spend
**AFA Savings Rate**: [Y]%

[For each existing AFA or proposed AFA: model and classification]

---

## 5. Efficiency Metrics Dashboard

| KPI                          | Current  | Target   | Classification |
| ---------------------------- | -------- | -------- | -------------- |
| Contract Turnaround Time     | [X] days | [Y] days | [Status]       |
| Self-Service Deflection Rate | [X]%     | [Y]%     | [Status]       |
| Invoice OCG Compliance Rate  | [X]%     | ≥95%     | [Status]       |
| [Other metrics...]           |          |          |                |

---

## 6. Budget Forecast

**Annual Budget**: $[X]
**YTD Actuals**: $[Y]
**Outstanding Accruals**: $[Z]
**Portfolio EAC**: $[A]
**Forecast Year-End Variance**: [+/-B]% vs. budget — [Status]

**Matters Trending Above Budget (Top 5)**:
| Matter | BAC | EAC | Variance | Action Required |
|--------|-----|-----|---------|----------------|
| [Matter] | $[X] | $[Y] | +[Z]% | [Action] |

---

## 7. Legal Tech ROI Summary

| Tool   | Annual Cost | Annual Benefits | ROI  | Classification |
| ------ | ----------- | --------------- | ---- | -------------- |
| [Tool] | $[X]        | $[Y]            | [Z]% | [Status]       |

---

## 8. Priority Recommendations

### Tier 1 — Immediate Action (High Impact)

1. [Specific recommendation] — Estimated savings: $[X] — Owner: [Role] — Due: [date]

### Tier 2 — Strategic (90-day horizon)

1. [Specific recommendation] — Expected benefit: [X] — Owner: [Role]

### Tier 3 — Long-Term Optimization

1. [Specific recommendation] — Timeline: [X months]

---

## Glass Box Audit Trail

[Insert YAML audit trail from the Glass Box template above]
```

---

## Localization Notes

This skill uses primarily US-centric benchmark data. When applying to non-US
organizations, make these adjustments:

| Adjustment          | Guidance                                                                                                                                                                   |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Rate benchmarks** | Apply geography-adjusted benchmarks. UK, EU, APAC rates differ materially from US medians. Use Wolters Kluwer, PwC, or Lexology local market data [VERIFY]                 |
| **LEDES/UTBMS**     | Standard in US and UK. Continental Europe, APAC, and LATAM may use different invoice formats — adapt normalization step accordingly                                        |
| **ACC benchmarks**  | ACC survey data is US-weighted; international departments should supplement with CLOC State of the Industry (more international) or local equivalents                      |
| **AFA prevalence**  | AFA adoption varies by jurisdiction and legal culture. UK, Australia, and Singapore show strong AFA adoption; continental Europe is growing but less mature [VERIFY]       |
| **VAT/GST**         | Ensure consistent treatment of taxes across all spend data before applying benchmarks — outside counsel fees in VAT-registered jurisdictions require gross/net consistency |
| **Currency**        | Normalize all spend to a single reporting currency before analysis. State the exchange rate basis and date                                                                 |

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis covering legal spend analysis,
outside counsel benchmarking, CLOC-aligned metrics, AFA evaluation, efficiency KPIs,
budget forecasting using EAC methodology, self-service deflection measurement, and
legal tech ROI analysis. Research pipeline included ACC 2023 Law Department Management
Benchmarking Report, CLOC Core 12 Maturity Framework, Wolters Kluwer ELM Solutions
benchmarking data, Brightflag 2025 Outside Counsel Benchmarking Report, LEDES/UTBMS
standards documentation, and PERSUIT/LeanLaw AFA adoption research. Benchmarks require
verification against current survey data before operational use. All citations marked
[VERIFY] require confirmation against authoritative current sources.
