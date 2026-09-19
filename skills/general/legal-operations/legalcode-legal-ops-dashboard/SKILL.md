---
name: legalcode-legal-ops-dashboard
description: Generate legal department operational reports and dashboards covering contract turnaround
  time, matter cycle time, spend analysis, outside counsel utilization, self-service adoption, SLA compliance,
  and budget variance. Use when a legal operations team needs to build a metrics dashboard, produce a
  quarterly legal department report, measure legal ops performance against CLOC benchmarks, assess self-service
  portal adoption, track SLA compliance across contract types, evaluate outside counsel performance, analyze
  budget variance, identify bottlenecks in contract or matter workflows, present legal ops ROI to finance,
  or generate a data-driven legal operations health assessment.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Generate legal department operational reports and dashboards covering contract turnaround time, matter cycle time, spend analysis, outside counsel utilization, self-service adoption, SLA compliance, and budget variance. Supports CLOC Core 12 operational metrics, ACC benchmarking, and executive reporting for general counsel, CFO, and board audiences. Use when a legal operations team needs to build a metrics dashboard, produce a quarterly legal department report, measure legal ops performance against CLOC benchmarks, assess self-service portal adoption, track SLA compliance across contract types, evaluate outside counsel performance, analyze budget variance, identify bottlenecks in contract or matter workflows, present legal ops ROI to finance, or generate a data-driven legal operations health assessment. Also triggers on: legal department KPIs, legal ops metrics, contract cycle time, matter throughput, outside counsel scorecard, legal spend dashboard, CLOC operational metrics, legal operations benchmarking, GC reporting, board reporting for legal, legal team capacity utilization, e-billing analytics, UTBMS spend analysis.


# Legalcode Legal Ops Dashboard

> **Disclaimer**: This skill provides a framework for AI-assisted legal operations reporting
> and metrics analysis. It does not constitute legal, financial, or management advice. All
> outputs should be reviewed by qualified legal operations and finance professionals before
> use in executive reporting, budget decisions, or vendor evaluations. Benchmark figures
> cited from CLOC, ACC, Wolters Kluwer ELM, and Bloomberg Law surveys represent snapshot
> data from specific survey periods and respondent populations — verify currency and
> applicability to your organization's industry, size, and geography before relying on them.
> Methodological references (CLOC Core 12, IILPM, UTBMS/LEDES codes, PDCA) carry standard
> hallucination risk — verify against authoritative sources before applying operationally.

---

## Purpose and Scope

This skill generates structured legal operations reports and dashboards. It turns raw legal
department data (matter logs, contract records, billing files, survey results) into
actionable intelligence aligned with CLOC Core 12 competency areas and ACC benchmarking
standards.

**Covers:**

- Contract turnaround time (CTT) by contract type and complexity tier
- Matter cycle time by practice area and matter type
- Legal spend analysis vs. budget and prior periods
- Outside counsel utilization: spend concentration, rate compliance, budget adherence, diversity
- Self-service adoption: portal utilization, template usage, tier-1 deflection rates
- SLA compliance: response time, resolution time, escalation rate by request type
- Budget variance: actuals vs. forecast, EAC (Estimate at Completion), burn-down
- CLOC Core 12 maturity assessment with gap identification
- Executive reporting packages for GC, CFO, and board audiences

**Does not:**

- Provide legal advice on the substantive merits of any matter
- Replace qualified legal operations or finance professionals
- Guarantee that published benchmarks apply to any specific organization without adjustment
- Produce GAAP/IFRS financial statements or auditable management accounts
- Substitute for purpose-built ELM/CLM analytics platforms (Brightflag, SimpleLegal, Wolters Kluwer ELM, Ironclad, Juro)

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. Legal operations methodology and CLOC/ACC metrics
frameworks apply across jurisdictions; however, primary benchmarking data is US-centric.

[JURISDICTION-SPECIFIC] Where this skill references benchmarks, billing standards, or
regulatory frameworks, consider these local variations:

- **LEDES/UTBMS**: Standard in the US and UK; less prevalent in continental Europe, APAC,
  and Latin America — adapt to local e-billing formats where needed [VERIFY]
- **Rate benchmarks**: US partner rates (avg. $500–$1,200+/hr [VERIFY current]) diverge
  significantly from UK, EU, Australian, and APAC market rates — use geography-adjusted data
- **Currency normalization**: Multi-jurisdiction departments must normalize to a single
  reporting currency before applying benchmark ratios
- **VAT/GST**: Ensure spend analysis reflects net or gross consistently — mixing distorts benchmarks
- **GDPR/privacy**: Dashboard data may contain personal data of employees, clients, or outside
  counsel timekeepers — confirm processing basis and retention periods comply with applicable
  data protection law [JURISDICTION-SPECIFIC]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the organization's size, industry, reporting audience, or data availability, the workflow
pauses and asks when:

- The answer would change the dashboard scope or benchmark set to apply
- Data gaps mean assumptions must be made explicitly
- Audience requirements differ materially (CFO vs. GC vs. board)
- Multiple valid presentation approaches exist

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

### Step 1: Accept Input Data

Accept data in any of these formats:

- **Structured files**: CSV, XLSX, or JSON exports from CLM, ELM, matter management, or
  billing systems (SimpleLegal, Brightflag, Wolters Kluwer ELM, TeamConnect, Ironclad, Juro, etc.)
- **Unstructured data**: Matter logs, contract registers, spreadsheet trackers, or
  narrative descriptions of the legal department's operational state
- **Partial data + benchmarks only**: If no internal data is available, the skill can
  produce a benchmark-based gap assessment and dashboard template
- **Prior report for update**: An existing dashboard or report to refresh with new data

If no data is provided, prompt the user to supply it or confirm that a benchmark-only
assessment is the goal.

### Step 2: Gather Context

**⟁ CLARIFY** — Before building the dashboard, ask the user these questions (skip any
already answered by the input):

1. **Organization profile**:
   - Options: Small (under $500M revenue / <5 attorneys), Mid-market ($500M–$5B / 5–30 attorneys),
     Large ($5B–$20B / 30–100+ attorneys), Enterprise ($20B+ / 100+ attorneys)
   - _Why this matters_: Benchmark sets and metric priorities vary significantly by size.
     CLOC/ACC data is segmented by revenue band and headcount.

2. **Primary audience for this report**:
   - Options: Legal Operations team (internal), General Counsel / CLO, CFO / Finance,
     CEO / Executive team, Board of Directors, All stakeholders (executive summary + detail)
   - _Why this matters_: Each audience needs different metrics, depth, and framing.
     Finance wants cost management; the board wants risk posture and governance.

3. **Reporting period**:
   - Options: Monthly, Quarterly (standard), Annual, Ad hoc (specific date range)
   - _Why this matters_: Determines trend analysis depth and benchmark period alignment.

4. **Metric priorities** — Which domains are most important for this report?
   - Options (multiple): Contract Turnaround Time, Matter Cycle Time, Spend Analysis,
     Outside Counsel Performance, Self-Service Adoption, SLA Compliance, Budget Variance,
     CLOC Maturity Assessment, Full dashboard (all domains)
   - _Why this matters_: Allows the report to lead with what matters most to this audience.

5. **Data availability**:
   - Options: Full data for all domains, Partial (specify which domains have data),
     Benchmarks-only assessment (no internal data available yet)
   - _Why this matters_: Determines whether to produce actuals-based analysis, a gap
     assessment, or a hybrid.

If the user provides partial context, proceed with stated assumptions and clearly label
which sections are benchmark-only vs. data-driven.

### Step 3: Establish Benchmarks

Load the relevant benchmark set based on the organization profile gathered in Step 2.
Use this reference table for CLOC/ACC industry benchmarks:

**Total Legal Spend as % of Revenue** [VERIFY current year]:

| Company Size      | Median %    | Top Quartile | Bottom Quartile |
| ----------------- | ----------- | ------------ | --------------- |
| Under $1B revenue | ~0.5–1.0%   | <0.4%        | >1.5%           |
| $1B–$5B revenue   | ~0.3–0.6%   | <0.25%       | >0.9%           |
| $5B–$20B revenue  | ~0.15–0.35% | <0.15%       | >0.5%           |
| $20B+ revenue     | ~0.10–0.20% | <0.10%       | >0.35%          |

[VERIFY: CLOC State of the Industry report and ACC Chief Legal Officer Survey for current
year data. Figures above are directional and may not reflect your industry, geography, or
specific business model.]

**Inside vs. Outside Counsel Spend Ratio** [VERIFY]:

- Median split: ~50–55% outside / 45–50% inside for mid-to-large departments
- Trend: rising outside counsel costs (rates +6–7% p.a. as of 2024–2025 [VERIFY])

**Contract Turnaround Time Benchmarks** [VERIFY]:

| Contract Type                  | Best-in-Class | Median     | Needs Improvement |
| ------------------------------ | ------------- | ---------- | ----------------- |
| NDA / Mutual NDA               | <1 day        | 1–3 days   | >5 days           |
| Standard PO / T&Cs             | <2 days       | 2–5 days   | >7 days           |
| Statement of Work (SOW)        | <7 days       | 7–14 days  | >21 days          |
| Master Service Agreement (MSA) | <15 days      | 20–40 days | >60 days          |
| Complex strategic / custom     | <30 days      | 30–60 days | >90 days          |

**Outside Counsel Concentration** [VERIFY]:

- Best practice: top 5 firms = <50% of outside counsel spend
- Median: top 10 firms = 70–80% of outside counsel spend

**⟁ CLARIFY** — If the organization is in a specialized sector (financial services,
pharma, TMT, energy), ask whether sector-specific benchmarks should be applied, as
general-purpose CLOC/ACC data may not reflect sector norms.

### Step 4: Analyze Each Metric Domain

Analyze each domain selected in Step 2. For each domain, produce:

1. **Actuals** (if data provided): key metrics for the period
2. **Benchmark comparison**: performance vs. relevant CLOC/ACC percentile
3. **Status classification**: ON-TARGET / WATCH / CRITICAL (see classification below)
4. **Trend**: improving / stable / deteriorating vs. prior period (if data available)
5. **Top 3 findings**: material observations requiring action
6. **Recommended actions**: specific, concrete next steps for each finding

Refer to the **Metric Domain Reference** section for the detailed analysis framework for
each domain.

**⟁ CLARIFY** — For any domain where the data appears inconsistent, incomplete, or
anomalous (e.g., contract turnaround times longer than 180 days for NDAs, or outside
counsel spend exceeding 300% of budget), flag the anomaly before proceeding:

- "The NDA cycle time data shows a median of 45 days, which is significantly above market
  benchmarks. Should I flag this as a data quality issue to investigate, or treat it as
  accurate and classify as CRITICAL?"

### Step 5: Build the Dashboard Structure

Organize the dashboard in the format appropriate for the audience selected in Step 2.

**Format A — Executive Summary (GC, CFO, CEO, Board)**:

- One-page overview: 5–7 headline KPIs with RAG status indicators
- Narrative summary: 3–5 sentences on overall department performance
- Key risks and opportunities: top 3 actions recommended

**Format B — Operational Detail (Legal Ops team, GC deep-dive)**:

- Domain-by-domain analysis with full metric tables
- Trend charts (described in text if no rendering capability)
- Root cause analysis for WATCH and CRITICAL items
- Action register with owners, timelines, and success metrics

**Format C — Finance Reporting (CFO package)**:

- Three-part spend structure: Historical actuals → Accruals/WIP → Forecast
- Budget variance table: all cost categories vs. budget, vs. prior period
- EAC (Estimate at Completion) for open matters and active engagements
- Outside counsel rate compliance and billing guideline adherence

**⟁ CLARIFY** — If reporting for multiple audiences simultaneously, ask:

- "Should I produce separate sections per audience, or a single layered report that
  executives can read as a summary and legal ops can use for operational detail?"

### Step 6: Apply Quality Assurance

Before delivering the dashboard, run the Citation Quality Gates (see Quality Assurance
Framework section). For any CRITICAL finding, run the Self-Interrogation protocol.

Verify:

- [ ] All benchmark figures are marked [VERIFY] or sourced to a named publication
- [ ] All [JURISDICTION-SPECIFIC] markers are correctly placed
- [ ] Calculations (variance %, trend %) are internally consistent
- [ ] Status classifications are applied consistently across comparable metrics
- [ ] Audience-appropriate framing is used (avoid internal jargon for board reports)

### Step 7: Deliver the Report

Structure the final output using the **Output Format Template** at the end of this skill.
Include the **Glass Box Audit Trail** at the end of every report.

**⟁ CLARIFY** — Before finalizing, ask:

- "Should I include a recommended action register with owners and suggested timelines,
  or keep the report to analysis and findings only?"
- "Are there any metrics, business units, or law firms that should be excluded from the
  report for sensitivity reasons?"

### Step 8: Post-Delivery — Roadmap and Next Steps

After delivering the current period's dashboard, offer to:

1. **Establish a reporting cadence**: Set up the dashboard template for next period
2. **Build a metrics improvement plan**: Identify 3–5 high-impact metric improvements
3. **CLOC maturity gap analysis**: If not already included, assess Core 12 maturity
4. **Benchmark refresh**: Note which benchmarks should be verified against current-year
   CLOC/ACC publications

---

## Metric Domain Reference

### Domain 1: Contract Turnaround Time (CTT)

**Definition**: Elapsed calendar days from contract request (or first draft received) to
fully executed agreement.

**Key metrics to calculate:**

- **Average CTT** by contract type (NDA, MSA, SOW, custom)
- **Median CTT** by contract type (less sensitive to outliers than average)
- **P90 CTT**: 90th percentile cycle time — the "worst normal" experience
- **% contracts within SLA target** by type
- **CTT trend**: current period vs. prior 3 periods
- **Bottleneck stage**: where time is spent (legal review, counterparty negotiation, signature collection, procurement review)

**Segmentation dimensions:**

- By contract type (NDA, MSA, SOW, license, amendment)
- By contract value tier (under $50K, $50K–$500K, $500K+)
- By business unit (which teams generate the most delays)
- By counterparty type (new vendor, existing vendor, customer, partner)
- By legal reviewer (team capacity and workload distribution)

**Status classification thresholds** (adjust for your organization's SLA targets):

| Metric                 | ON-TARGET           | WATCH          | CRITICAL       |
| ---------------------- | ------------------- | -------------- | -------------- |
| NDA median CTT         | ≤2 days             | 3–7 days       | >7 days        |
| MSA median CTT         | ≤21 days            | 22–50 days     | >50 days       |
| % contracts within SLA | ≥85%                | 70–84%         | <70%           |
| CTT trend              | Stable or improving | Worsening ≤15% | Worsening >15% |

**Common findings and recommended actions:**

| Finding                           | Likely Root Cause                              | Recommended Action                                             |
| --------------------------------- | ---------------------------------------------- | -------------------------------------------------------------- |
| NDA CTT >5 days                   | Manual review of standard forms                | Deploy self-service NDA portal; pre-approve template           |
| MSA CTT >60 days                  | Iterative rounds of counterparty negotiation   | Publish playbook to sales; reduce negotiation scope            |
| High P90 vs. median               | A small number of outlier contracts distorting | Segment outliers; apply enhanced triage process                |
| Business unit X consistently slow | Procurement or finance holds, not legal        | Map multi-party approval chain; identify non-legal bottlenecks |

[JURISDICTION-SPECIFIC] In regulated industries (financial services, healthcare, government
contracting), mandatory approval steps (compliance, data protection review, security review)
legitimately extend CTT. Adjust benchmarks and SLAs accordingly.

---

### Domain 2: Matter Cycle Time

**Definition**: Elapsed time from matter opening to matter closure, by practice area and
matter type.

**Key metrics to calculate:**

- **Average and median matter cycle time** by practice area (M&A, litigation, employment,
  commercial contracts, regulatory, IP, real estate)
- **Matter closure rate**: matters closed / matters opened in period
- **Open matter inventory**: total open matters, aged >90 days / >180 days / >365 days
- **Matters per FTE**: total matters / legal FTE headcount (capacity indicator)
- **Matter backlog trend**: growing / stable / shrinking
- **Escalation rate**: matters escalated to outside counsel vs. handled in-house

**Status classification thresholds**:

| Metric                          | ON-TARGET                  | WATCH              | CRITICAL               |
| ------------------------------- | -------------------------- | ------------------ | ---------------------- |
| Matter closure rate             | ≥100% (closing ≥ opening)  | 90–99%             | <90% (backlog growing) |
| Matters per attorney FTE        | Within 20% of prior period | 21–40% above prior | >40% above prior       |
| Aged matters >180 days          | <15% of open inventory     | 15–25%             | >25%                   |
| Outside counsel escalation rate | Stable or declining        | Rising ≤10%        | Rising >10%            |

**Segmentation dimensions:**

- By practice area (litigation / transactional / advisory / regulatory)
- By matter type (contract dispute, employment claim, regulatory inquiry, M&A, routine advice)
- By originating business unit
- By inside vs. outside counsel handling

---

### Domain 3: Legal Spend Analysis

**Definition**: Total legal expenditure — internal costs (salaries, benefits, overhead,
technology) and external costs (outside counsel fees, court costs, expert fees, legal tech).

**Key metrics to calculate:**

- **Total legal spend as % of company revenue** — primary CLOC benchmark
- **Inside / outside counsel spend ratio**
- **Outside counsel spend by firm** (concentration analysis)
- **Spend by practice area / matter type**
- **Spend by business unit** (departmental allocation)
- **Rate trend**: average blended hourly rate, year-over-year change
- **Accruals and WIP**: estimated unbilled work in progress at period end
- **EAC (Estimate at Completion)**: current EAC vs. approved matter budget

**Spend analysis table structure:**

| Law Firm / Vendor | Total Spend | % of Outside Budget | Budget Compliance           | Rate Compliance        | Blended Rate |
| ----------------- | ----------- | ------------------- | --------------------------- | ---------------------- | ------------ |
| [Firm 1]          | $X          | XX%                 | XX% matters on/under budget | XX% invoices compliant | $X/hr        |
| [Firm 2]          | $X          | XX%                 |                             |                        |              |

**Status classification thresholds**:

| Metric                                | ON-TARGET                    | WATCH      | CRITICAL  |
| ------------------------------------- | ---------------------------- | ---------- | --------- |
| Total spend vs. budget                | ≤5% variance                 | 6–15% over | >15% over |
| Outside counsel concentration (top 5) | <50% of OC spend             | 50–65%     | >65%      |
| Rate inflation YoY                    | ≤5%                          | 6–10%      | >10%      |
| Budget compliance rate (firms)        | ≥85% matters on/under budget | 70–84%     | <70%      |

**UTBMS/LEDES analytics** [VERIFY applicability to your e-billing setup]:

- Identify top 10 UTBMS task codes by spend
- Flag task codes with material YoY spend variance
- Identify billing guideline non-compliance patterns (block billing, vague descriptions,
  excessive administrative time)

[JURISDICTION-SPECIFIC] US and UK law departments: LEDES format invoicing and UTBMS code
analysis is standard. Continental Europe, APAC: adapt to local invoice format conventions
and apply equivalent spend categorization [VERIFY].

---

### Domain 4: Outside Counsel Utilization

**Definition**: How effectively the legal department manages its external legal service
providers across performance, cost, and diversity dimensions.

**Key metrics:**

- **Panel concentration**: number of active law firms; % of spend in top 5 / top 10
- **Budget compliance rate**: % of matters delivered within initial budget estimate
- **Billing guideline compliance rate**: % of invoices compliant with OCGs on first submission
- **Matter cycle time by firm**: average closure time by firm vs. department median
- **Rate compliance**: % of timekeeper rates within agreed rate schedule
- **Blended hourly rate by firm**: for benchmarking across panel
- **Staffing efficiency**: partner/associate/contract lawyer ratio by firm
- **Diversity metrics** [VERIFY data availability]: % of billing hours by female timekeepers,
  % by racially/ethnically diverse timekeepers (often requires firm self-reporting)

**Outside Counsel Scorecard template:**

| Metric                            | Weight | Firm A | Firm B | Firm C |
| --------------------------------- | ------ | ------ | ------ | ------ |
| Budget compliance                 | 25%    |        |        |        |
| Billing guideline compliance      | 20%    |        |        |        |
| Matter cycle time vs. benchmark   | 20%    |        |        |        |
| Rate compliance                   | 20%    |        |        |        |
| Diversity (% diverse timekeepers) | 15%    |        |        |        |
| **Weighted score**                | 100%   |        |        |        |

**Status classification thresholds**:

| Metric                       | ON-TARGET | WATCH  | CRITICAL |
| ---------------------------- | --------- | ------ | -------- |
| Budget compliance rate       | ≥80%      | 65–79% | <65%     |
| Billing guideline compliance | ≥90%      | 80–89% | <80%     |
| Rate compliance              | ≥95%      | 90–94% | <90%     |
| Panel concentration (top 5)  | <50%      | 50–65% | >65%     |

**Recommended actions for common findings:**

| Finding                               | Recommended Action                                                                |
| ------------------------------------- | --------------------------------------------------------------------------------- |
| Billing guideline non-compliance >15% | Issue billing guideline reminder; auto-reject non-compliant invoices              |
| Budget overruns >20% on >3 matters    | Require matter budget updates at 75% of approved budget                           |
| Diversity metrics below target        | Activate diversity bonus or fee reduction program; require diverse staffing plans |
| High concentration in 1–2 firms       | Conduct panel review; expand to 2–3 competitive alternative firms                 |

---

### Domain 5: Self-Service Adoption

**Definition**: Degree to which business users resolve legal requests without direct legal
team intervention, using self-service portals, templates, or guided workflows.

**Key metrics:**

- **Self-service utilization rate**: requests handled via self-service / total legal requests (%)
- **Template usage rate**: contracts generated from pre-approved templates / total contracts
- **Tier-1 deflection rate**: % of requests resolved without attorney review
- **Portal adoption by business unit**: which teams use self-service vs. routing to legal
- **Self-service CTT vs. full-review CTT**: efficiency gain from self-service
- **Error/escalation rate**: % of self-service contracts requiring subsequent legal correction

**Self-service tier model:**

| Tier       | Description                                              | Target % of Total Volume |
| ---------- | -------------------------------------------------------- | ------------------------ |
| **Tier 0** | Fully automated (click-through T&Cs, online forms)       | 20–40%                   |
| **Tier 1** | Self-service template (pre-approved, no attorney needed) | 30–40%                   |
| **Tier 2** | Template + light touch review (<1 hr attorney time)      | 15–25%                   |
| **Tier 3** | Full attorney review                                     | 10–20%                   |

**Status classification thresholds**:

| Metric                                     | ON-TARGET              | WATCH  | CRITICAL |
| ------------------------------------------ | ---------------------- | ------ | -------- |
| Overall self-service rate (Tier 0+1)       | ≥40%                   | 25–39% | <25%     |
| Template usage for standard forms          | ≥70%                   | 50–69% | <50%     |
| Self-service error/escalation rate         | ≤5%                    | 6–10%  | >10%     |
| Portal adoption (teams using self-service) | ≥75% of business units | 50–74% | <50%     |

**⟁ CLARIFY** — If the organization does not yet have a self-service portal, ask:

- "Should I include a self-service readiness assessment instead — identifying which contract
  types and request categories are candidates for self-service automation?"

---

### Domain 6: SLA Compliance

**Definition**: Performance against the legal department's service level commitments to
internal business clients, measured by response time, resolution time, and escalation rate
by request type.

**Key metrics:**

- **SLA compliance rate by request type**: % of requests met within SLA target
- **Average response time**: time from request submission to first attorney contact
- **Average resolution time**: time from request submission to closure
- **SLA breach rate by severity**: breach rate for Urgent / Standard / Routine requests
- **Escalation rate**: requests escalated beyond initial assignee / total requests
- **Repeat request rate**: requests reopened or returned for rework

**Standard SLA tiers** (customize to your department's commitments):

| Request Type                                 | Urgent Target    | Standard Target | Routine Target  |
| -------------------------------------------- | ---------------- | --------------- | --------------- |
| Urgent legal advice (regulatory, litigation) | 2 hours response | 4 hours         | —               |
| Contract review (NDA, standard)              | Same day         | 2 business days | 5 business days |
| Contract review (complex)                    | 3 days           | 7 days          | 14 days         |
| Employment / HR advice                       | 4 hours          | 1 day           | 3 days          |
| Compliance query                             | 2 hours          | 1 day           | 3 days          |
| IP / trademark query                         | 1 day            | 3 days          | 7 days          |

**Status classification thresholds**:

| Metric                 | ON-TARGET           | WATCH         | CRITICAL      |
| ---------------------- | ------------------- | ------------- | ------------- |
| Overall SLA compliance | ≥90%                | 80–89%        | <80%          |
| Urgent request SLA     | ≥95%                | 85–94%        | <85%          |
| Standard request SLA   | ≥88%                | 75–87%        | <75%          |
| SLA trend QoQ          | Stable or improving | Worsening ≤5% | Worsening >5% |

**Root cause framework for SLA breaches:**

| Root Cause            | Indicators                                           | Remediation                                               |
| --------------------- | ---------------------------------------------------- | --------------------------------------------------------- |
| Capacity constraint   | High matters/FTE ratio; consistent miss across types | Hire, redistribute, or deflect via self-service           |
| Routing failure       | Requests assigned to wrong reviewer or team          | Improve intake triage; update routing rules               |
| Scope creep           | Requests expanding beyond initial scope              | Enforce scope at intake; use scoping templates            |
| External dependencies | Missing counterparty response; awaiting approvals    | Flag external holds in reporting; remove from SLA clock   |
| Priority conflict     | Urgent matters displacing standard requests          | Implement priority queuing with transparent communication |

---

### Domain 7: Budget Variance

**Definition**: Comparison of actual legal department expenditure against approved budgets
and prior period, with forward-looking EAC for open matters.

**Key metrics:**

- **Total budget variance**: actual vs. approved budget ($ and %)
- **Variance by cost category**: personnel, outside counsel, technology, court costs, other
- **Variance by practice area / matter type**
- **Variance by business unit** (cost allocation)
- **EAC (Estimate at Completion)**: current projected year-end spend vs. approved annual budget
- **Accruals accuracy**: estimated WIP at prior period-end vs. actual invoices received
- **Budget re-forecast frequency**: number of budget revisions required in the period

**Budget variance report structure (CFO-ready):**

| Cost Category                   | Annual Budget | YTD Actual | YTD Budget | Variance $ | Variance % | Projected Year-End |
| ------------------------------- | ------------- | ---------- | ---------- | ---------- | ---------- | ------------------ |
| Personnel (salaries + benefits) | $X            | $X         | $X         | $X         | X%         | $X                 |
| Outside counsel                 | $X            | $X         | $X         | $X         | X%         | $X                 |
| Technology / SaaS               | $X            | $X         | $X         | $X         | X%         | $X                 |
| Court costs / filing fees       | $X            | $X         | $X         | $X         | X%         | $X                 |
| Travel / expert fees            | $X            | $X         | $X         | $X         | X%         | $X                 |
| **Total**                       | **$X**        | **$X**     | **$X**     | **$X**     | **X%**     | **$X**             |

**Status classification thresholds**:

| Metric                   | ON-TARGET            | WATCH      | CRITICAL  |
| ------------------------ | -------------------- | ---------- | --------- |
| Total budget variance    | ≤5% over             | 6–15% over | >15% over |
| Outside counsel variance | ≤10%                 | 11–25%     | >25%      |
| EAC vs. annual budget    | ≤5%                  | 6–15%      | >15%      |
| Accruals accuracy        | Within 10% of actual | 11–20% off | >20% off  |

**EAC formula** [VERIFY methodology with finance team]:

```
EAC = Actual costs to date + (Remaining budget / Cost Performance Index)
Cost Performance Index (CPI) = Budgeted cost of work performed / Actual cost of work performed
```

A CPI < 1.0 means the department is spending more than budgeted per unit of work completed.

---

### Domain 8: CLOC Core 12 Maturity Assessment

The CLOC Core 12 framework defines 12 competency areas for legal operations functions.
Assess the department's maturity in each area:

| CLOC Core 12 Area                   | Maturity Levels                        | Assessment Questions                                                      |
| ----------------------------------- | -------------------------------------- | ------------------------------------------------------------------------- |
| **1. Business Intelligence**        | Ad hoc → Defined → Managed → Optimized | Are legal ops metrics tracked systematically? Is data used for decisions? |
| **2. Financial Management**         | Ad hoc → Defined → Managed → Optimized | Are budgets tracked? Is spend benchmarked? Is EAC used?                   |
| **3. Firm / Vendor Management**     | Ad hoc → Defined → Managed → Optimized | Is there a panel? Are scorecards used? Are AFAs in place?                 |
| **4. Information Governance**       | Ad hoc → Defined → Managed → Optimized | Is a CLM/DMS in use? Is retention policy enforced?                        |
| **5. Knowledge Management**         | Ad hoc → Defined → Managed → Optimized | Are playbooks maintained? Is institutional knowledge captured?            |
| **6. Organization Optimization**    | Ad hoc → Defined → Managed → Optimized | Is staffing model designed? Are roles clearly defined?                    |
| **7. Practice Operations**          | Ad hoc → Defined → Managed → Optimized | Are workflows documented? Is matter management in place?                  |
| **8. Project / Program Management** | Ad hoc → Defined → Managed → Optimized | Is LPM methodology used? Are milestones tracked?                          |
| **9. Service Delivery**             | Ad hoc → Defined → Managed → Optimized | Are SLAs defined? Is self-service in place?                               |
| **10. Strategic Planning**          | Ad hoc → Defined → Managed → Optimized | Is there a legal ops roadmap? Is it aligned with company strategy?        |
| **11. Technology**                  | Ad hoc → Defined → Managed → Optimized | Is the tech stack mapped? Is ROI measured? Is AI explored?                |
| **12. Training and Development**    | Ad hoc → Defined → Managed → Optimized | Is legal training tracked? Are CPD requirements met?                      |

**Maturity levels defined:**

- **Ad hoc**: No defined process; reactive; dependent on individuals
- **Defined**: Process exists and is documented; inconsistently applied
- **Managed**: Process consistently applied; measured; reported
- **Optimized**: Continuously improved; benchmarked externally; driving competitive advantage

**⟁ CLARIFY** — If the user wants a full CLOC maturity assessment, ask whether to:

- Score all 12 areas (comprehensive gap analysis)
- Focus on the 3–5 lowest-maturity areas (targeted improvement plan)
- Benchmark against peer departments using CLOC SOTI data

---

## Status Classification

### ON-TARGET — Performing at or above benchmark

Department performance meets or exceeds CLOC/ACC benchmark medians for this size and
industry segment. No immediate action required; maintain and monitor.

**Indicators**: Metrics within or better than benchmark range; stable or improving trend;
SLAs met consistently; budget within tolerance.

**Report framing**: "Department is performing well against market benchmarks. [Specific
area] is a standout strength."

### WATCH — Below benchmark; action warranted

Department performance falls below benchmark medians but has not reached critical threshold.
Trend analysis needed. Proactive management will prevent escalation to CRITICAL.

**Indicators**: 1–2 metrics below benchmark; trend worsening but not acute; SLA compliance
declining; budget variance growing.

**Report framing**: "Performance in [area] is trending below benchmark and warrants focused
attention. Recommended actions are [X]."

### CRITICAL — Material gap; urgent remediation required

Department performance is materially below benchmark or has breached a threshold requiring
escalation to GC, CFO, or CEO. Underlying root cause analysis and a remediation plan are
required within 30 days.

**Indicators**: Multiple metrics below benchmark; deteriorating trend; SLA breach rate >20%;
budget variance >15%; outside counsel concentration or non-compliance above thresholds.

**Report framing**: "The [area] metric is CRITICAL. [Specific impact]. Root cause analysis
identifies [X]. Immediate actions recommended: [Y]. Escalation recommendation: [Z]."

---

## Prioritization Framework

Organize findings and recommended actions by priority tier:

### Priority 1 — Immediate Action (0–30 days)

Issues with material financial, legal, or operational impact if unaddressed:

- Budget overrun projected to exceed annual approved amount
- SLA breach rate affecting key business relationships
- Outside counsel billing non-compliance creating financial exposure
- Contract turnaround time critically impacting revenue-generating deals
- CRITICAL-classified metrics with a deteriorating trend

### Priority 2 — Near-Term Action (30–90 days)

Issues that are WATCH-classified and require a managed improvement plan:

- Template adoption below 50% for standard contract types
- Matter backlog growing at >10% per quarter
- CLOC Core 12 maturity below "Defined" in 3+ areas
- Outside counsel diversity metrics materially below department commitments
- Accruals accuracy >15% off actual

### Priority 3 — Strategic Action (90+ days / roadmap)

Issues that are important for long-term competitiveness but not immediately material:

- CLOC maturity advancement from "Managed" to "Optimized" in specific areas
- Technology investment evaluation (CLM, AI tools, analytics platforms)
- Self-service expansion to new contract types or business units
- Panel review and outside counsel convergence program
- Reporting infrastructure improvements and automation

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any dashboard output. If any gate fails,
revise before delivering.

| Gate           | Rule                                                                                   | Fail Action                                                              |
| -------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Source**     | Every benchmark figure cites a named publication or data source                        | Add source or mark "[UNVERIFIED — verify against current CLOC/ACC data]" |
| **Format**     | All financial figures use consistent currency, rounding, and notation                  | Fix format inconsistencies                                               |
| **Currency**   | Every benchmark checked for applicable year and respondent population                  | Flag as "[CHECK CURRENCY — benchmark may be from prior year]"            |
| **Domain**     | Analysis stays within the department's applicable size / industry / geography segment  | Remove or flag out-of-scope benchmark bleed                              |
| **Confidence** | Data gaps, assumptions, and estimates explicitly labeled — not presented as hard facts | Add confidence qualifier or "[ESTIMATED]" label                          |

### Self-Interrogation for CRITICAL Classifications

For any metric classified as CRITICAL, apply this 3-pass review before delivering:

**Pass 1 — Data Integrity**: Is the CRITICAL classification based on reliable data? Could
the finding be explained by a data quality issue, a change in counting methodology, or a
one-time anomaly? Have outliers been investigated?

**Pass 2 — Root Cause Completeness**: Has every plausible root cause been considered?
Is the root cause analysis looking beyond symptoms to underlying drivers? Are external
factors (economic conditions, regulatory change, M&A activity) adequately considered?

**Pass 3 — Challenge**: What is the strongest argument that this metric is actually
acceptable for this organization's specific context? Under what circumstances would a
peer department accept this performance level? Is escalation proportionate, or would
WATCH with a remediation plan be more appropriate?

If any pass reveals a weakness, revise the classification before delivery. Mark the audit
trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material finding or dashboard metric, assign a confidence level:

| Level        | Range     | Meaning                                                                | Action                                                                  |
| ------------ | --------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Based on complete, verified data from authoritative system             | State with confidence                                                   |
| **High**     | 0.80–0.94 | Based on reliable data; minor gaps or estimates                        | State with brief caveat                                                 |
| **Probable** | 0.60–0.79 | Based on partial data or self-reported figures; reasonable assumptions | State with explicit assumptions and caveats                             |
| **Possible** | 0.40–0.59 | Based on extrapolation, outdated data, or benchmarks-only              | Flag for verification; present as directional                           |
| **Unlikely** | 0.0–0.39  | Insufficient data basis; highly speculative                            | Do not assert; flag as "[INSUFFICIENT DATA — collect before reporting]" |

---

## Glass Box Audit Trail

Every dashboard output MUST include a Glass Box audit section at the end:

```yaml
glass_box:
  skill_name: "legalcode-legal-ops-dashboard"
  report_period: "[Q1 2026 / FY2025 / etc.]"
  report_date: "[date]"
  organization_profile: "[Small / Mid-market / Large / Enterprise]"
  primary_audience: "[Legal Ops / GC / CFO / Board]"
  domains_analyzed: "[list of domains covered]"
  data_basis: "[Actuals / Benchmarks-only / Hybrid]"
  data_sources: "[CLM export, LEDES billing data, matter management extract, etc.]"
  benchmark_sources:
    - "CLOC State of the Industry [year — VERIFIED / UNVERIFIED]"
    - "ACC Chief Legal Officer Survey [year — VERIFIED / UNVERIFIED]"
    - "[Other named source — VERIFIED / UNVERIFIED]"
  legalcode_mcp: "Connected / Not connected"
  metrics_classified:
    on_target: "[N domains]"
    watch: "[N domains]"
    critical: "[N domains]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, data gaps, or caveats]"
    - "[Benchmarks not verified against current-year publications — mark CHECK CURRENCY]"
  reviewer: "AI-assisted — requires qualified legal ops and finance review before distribution"
```

---

## Anti-Patterns

What NOT to do when building a legal ops dashboard:

1. **Averaging without segmenting**: Reporting a single average contract turnaround time
   that blends NDAs (should be <2 days) with MSAs (may legitimately take 30+ days) produces
   a meaningless metric that obscures both good and poor performance.

2. **Benchmarking without adjustment**: Applying generic CLOC median data to a pharmaceutical
   company, financial services firm, or government contractor without recognizing that
   regulatory burden, deal complexity, and risk tolerance differ materially from the
   general-purpose benchmark population.

3. **Reporting outputs without inputs**: Measuring contract cycle time without tracking
   what drives it (counterparty negotiation, internal approvals, signature collection)
   creates no actionable insight — you know things are slow but not why.

4. **Conflating legal team speed with legal team quality**: A department that closes
   contracts in 2 days by accepting all counterparty positions scores well on CTT but
   creates business risk. Dashboard metrics must be read alongside contract quality and
   risk metrics.

5. **Outside counsel spend concentration without context**: A 70% spend concentration in
   top 5 firms is a warning sign for most departments — but may be appropriate for a
   department with a very narrow, specialized practice (e.g., complex patent litigation)
   where 2–3 firms dominate the market.

6. **Self-service rate as a vanity metric**: A high self-service rate is only valuable if
   the escalation/correction rate is low. A 60% self-service rate where 20% of self-served
   contracts require correction is worse than a 30% self-service rate with <3% corrections.

7. **Budget compliance measured at year-end only**: Waiting until December to assess budget
   variance means overruns are discovered too late to remediate. Accruals-based monthly
   tracking (WIP + committed + actuals) enables proactive management.

8. **SLA compliance measured without defining what an SLA is**: Many legal departments
   track response time without having formally defined SLA targets. A 72-hour response time
   is good or bad depending on the commitment. Define SLAs before measuring them.

9. **Diversity metrics reported without a denominator**: Reporting that "15% of billing
   hours were from diverse partners" is meaningless without knowing what the benchmark is,
   what the prior period was, and what the department's commitment level is.

10. **CLOC maturity assessment as a one-time exercise**: Maturity assessments are only
    useful if repeated at regular intervals (annually) and tied to specific improvement
    initiatives. A maturity score without an improvement roadmap is a status report, not
    a management tool.

11. **Dashboard without audience-appropriate framing**: A legal ops operational dashboard
    filled with UTBMS code analysis, billing guideline compliance rates, and CLOC maturity
    scores is not the right tool for a board of directors. Translate operational data into
    business impact language for executive audiences.

12. **Treating all outside counsel spend as controllable**: Litigation costs driven by
    counterparty behavior, regulatory investigations, or court orders are not directly
    manageable in the same way as transactional outside counsel spend. Separate
    "controllable" from "non-controllable" spend before applying variance analysis.

13. **Matter volume as a proxy for attorney productivity**: The number of matters an
    attorney handles says nothing about the quality, complexity, or risk level of those
    matters. Supplement volume metrics with complexity weighting or risk-adjusted matter counts.

14. **Single-period dashboard without trend data**: A quarterly snapshot with no prior
    period comparators has limited diagnostic value. A dashboard without at least 4 periods
    of trend data cannot distinguish a systemic problem from a one-time anomaly.

15. **Ignoring data quality before reporting**: Distributing a dashboard with obviously
    anomalous data (e.g., contracts with 0-day cycle times, matters with negative cost
    variances) without investigation damages credibility with the audience. Validate and
    clean data before reporting.

---

## Writing Standards

Apply these standards to every dashboard output before delivery:

**Headline KPIs**: State the metric, the comparator (vs. budget / vs. prior period / vs.
benchmark), and the status classification in one line. Example:

- "Contract Turnaround Time (NDA): Median 3.2 days | Benchmark: ≤2 days | Status: WATCH"

**Narrative summaries**: Write in plain language accessible to a non-legal audience.
Avoid legal jargon in CFO and board reports. Use active voice. Lead with the finding,
not the methodology.

**Financial figures**: Use consistent notation (thousands = $Xk, millions = $XM). Round
to appropriate precision (percentages to one decimal place; dollar figures to nearest
thousand for operational reports, nearest million for board reports).

**Benchmark citations**: Always name the benchmark source and year. Use "[VERIFY]" for
benchmarks not confirmed against current publications.

**Recommendations**: Phrase all recommendations as specific actions with an actor and a
timeframe. Not "improve contract turnaround time" but "Deploy self-service NDA portal for
standard NDAs by Q2 2026 (Owner: Legal Ops, in partnership with IT)."

**Quality gate before delivery**:

- [ ] All CRITICAL classifications have been self-interrogated
- [ ] All benchmarks are sourced or marked [VERIFY]
- [ ] Audience-appropriate language used throughout
- [ ] Action register includes owner, timeline, and success metric for each Priority 1 item
- [ ] Glass Box audit trail is complete

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for current-year CLOC State of the Industry data and ACC benchmarks
- Retrieve applicable regulatory requirements for the dashboard's jurisdiction(s)
- Verify billing standard references (LEDES, UTBMS code definitions)
- Save research results to `/tmp/legalcode-legal-ops-research.md` for traceability

**Without legalcode-mcp:**

- Proceed using the benchmark tables embedded in this skill (Sections 3 and Metric
  Domain Reference)
- Mark all benchmark figures with [VERIFY] and note in the Glass Box:
  `legalcode_mcp: "Not connected — benchmarks from skill knowledge base, verify currency"`
- Recommend the user verify current-year CLOC/ACC data before executive distribution

---

## Localization Notes

This skill's frameworks apply globally; the following localization adaptations apply:

**United States**: LEDES/UTBMS standard for e-billing; CLOC and ACC are the primary
benchmark sources; GDPR/CCPA requirements for dashboard data handling vary by state [VERIFY].

**United Kingdom**: LEDES used for outside counsel billing; UK GDPR governs dashboard
data; Law Society and GC100 may publish relevant benchmarks [VERIFY].

**European Union**: Local e-billing formats vary; GDPR strictly applies to all personal
data in dashboards (timekeeper data, employee matter records); local language requirements
may apply to reports submitted to regulators [JURISDICTION-SPECIFIC].

**APAC / Latin America**: CLOC/ACC benchmarks are less applicable — seek local in-country
benchmarks from regional law associations or legal ops networks [VERIFY].

---

## Output Format Template

Every Legal Ops Dashboard report should follow this structure:

```markdown
# Legal Operations Dashboard — [Organization Name] — [Period]

**Prepared**: [Date] | **Audience**: [Legal Ops / GC / CFO / Board] | **Status**: [Draft / Final]

---

## Executive Summary

[2–4 sentence narrative: overall department performance, key wins, key concerns, and
primary recommended action for the period.]

### Headline KPI Summary

| Domain                   | Key Metric         | Actual | Benchmark    | Status   |
| ------------------------ | ------------------ | ------ | ------------ | -------- |
| Contract Turnaround Time | Median NDA CTT     | X days | ≤2 days      | 🟢/🟡/🔴 |
| Matter Cycle Time        | Closure rate       | X%     | ≥100%        | 🟢/🟡/🔴 |
| Legal Spend              | Spend as % revenue | X%     | [benchmark]% | 🟢/🟡/🔴 |
| Outside Counsel          | Budget compliance  | X%     | ≥80%         | 🟢/🟡/🔴 |
| Self-Service Adoption    | Tier 0+1 rate      | X%     | ≥40%         | 🟢/🟡/🔴 |
| SLA Compliance           | Overall SLA rate   | X%     | ≥90%         | 🟢/🟡/🔴 |
| Budget Variance          | Total vs. budget   | X%     | ≤5%          | 🟢/🟡/🔴 |

🟢 ON-TARGET | 🟡 WATCH | 🔴 CRITICAL

---

## Domain Analysis

### 1. Contract Turnaround Time (CTT)

**Period**: [Q]
**Status**: [ON-TARGET / WATCH / CRITICAL]
**Confidence**: [HIGH / MEDIUM / LOW]

| Contract Type | Median CTT | Benchmark | Status   | Trend |
| ------------- | ---------- | --------- | -------- | ----- |
| NDA           | X days     | ≤2 days   | 🟢/🟡/🔴 | ↑/→/↓ |
| MSA           | X days     | ≤21 days  | 🟢/🟡/🔴 | ↑/→/↓ |
| SOW           | X days     | ≤7 days   | 🟢/🟡/🔴 | ↑/→/↓ |

**Key Findings:**

1. [Finding 1]
2. [Finding 2]
3. [Finding 3]

**Root Cause Analysis:**
[Where is time being spent? Bottleneck identification.]

**Recommended Actions:**

- [Action 1] | Owner: [X] | Timeline: [Y] | Success metric: [Z]

---

### 2. Matter Cycle Time

[Same structure as CTT section]

---

### 3. Legal Spend Analysis

**Period**: [Q] / YTD
**Status**: [ON-TARGET / WATCH / CRITICAL]

[Budget variance table]

**Outside Counsel Concentration:**

- Top 5 firms represent X% of outside counsel spend

**Key Findings:**
[Top 3 findings]

**Recommended Actions:**
[Prioritized actions]

---

### 4. Outside Counsel Performance

[Scorecard table + findings + actions]

---

### 5. Self-Service Adoption

[Tier breakdown + portal adoption by BU + findings + actions]

---

### 6. SLA Compliance

[SLA compliance table by request type + root cause analysis + actions]

---

### 7. Budget Variance

[Full budget variance table + EAC + accruals accuracy + actions]

---

## Priority Action Register

| Priority | Action             | Owner   | Timeline  | Success Metric | Status  |
| -------- | ------------------ | ------- | --------- | -------------- | ------- |
| 1        | [Immediate action] | [Owner] | [30 days] | [Metric]       | Open    |
| 2        | [Near-term action] | [Owner] | [90 days] | [Metric]       | Open    |
| 3        | [Strategic action] | [Owner] | [Roadmap] | [Metric]       | Planned |

---

## CLOC Core 12 Maturity (if assessed)

| CLOC Area             | Current Maturity | Target  | Gap   | Priority   |
| --------------------- | ---------------- | ------- | ----- | ---------- |
| Business Intelligence | [Level]          | [Level] | [Gap] | [P1/P2/P3] |
| Financial Management  | [Level]          | [Level] | [Gap] | [P1/P2/P3] |
| [... all 12 areas]    |                  |         |       |            |

---

## Data Notes and Limitations

[List any data gaps, estimation methodologies, benchmarks pending verification, or
periods where data was unavailable or estimated.]

---

## Glass Box Audit Trail

[Include complete YAML audit trail as defined in the Glass Box section above.]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on:

- CLOC Core 12 framework and State of the Industry report [VERIFY current year at cloc.org]
- ACC Chief Legal Officer Survey benchmarking data [VERIFY current year at acc.com]
- Bloomberg Law / Wolters Kluwer ELM legal spend benchmarking data [VERIFY]
- UTBMS/LEDES billing standards (utbms.com) [VERIFY]
- Legal operations practitioner resources: Brightflag, EY Law, Wolters Kluwer ELM documentation
- Legalcode repository reference standards: legalcode-contract-review, legalcode-legal-spend-analysis,
  legalcode-legal-project-management quality frameworks
- Attribution: Legalcode original synthesis
