---
name: legalcode-pay-equity-audit
description: Conducts a comprehensive pay equity audit — from data scoping and similarly situated employee
  group (SSEG) construction through statistical regression design, LNDF validation, gap classification,
  remediation budget modeling, and reporting. Use when analyzing workforce compensation for gender, race,
  or other protected-class pay disparities; preparing for OFCCP contractor audits; complying with California
  SB 1162, New York pay transparency requirements, Colorado Equal Pay for Equal Work Act, or Illinois
  EPRC obligations; implementing the EU Pay Transparency Directive (2023/970/EU) joint pay assessment;
  managing pre-litigation pay equity risk; or building a proactive annual pay equity program. Supports
  both US multi-state and EU multinational engagements. Covers statistical regression methodology (OLS,
  adjusted/unadjusted gaps), attorney-client privilege structuring, and remediation waterfall modeling.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Pay Equity Audit

> **Disclaimer**: This skill provides a framework for AI-assisted pay equity analysis. It
> does not constitute legal advice. All outputs — including gap classifications, exposure
> estimates, remediation recommendations, and statistical analyses — must be reviewed by a
> qualified employment attorney and a credentialed compensation analyst before use in any
> employment action, litigation matter, regulatory filing, or public disclosure. Statistical
> conclusions about pay disparities require validation against actual payroll data; model
> outputs are indicative only. Laws and regulations change frequently; verify current
> applicability before relying on any provision described here. Statutory and case law
> references carry hallucination risk — verify against authoritative sources before use.

---

## Purpose and Scope

This skill guides a pay equity audit from intake through final deliverable. It equips an
AI agent to structure the analysis, identify similarly situated employee groups, design a
regression model, classify pay gaps by severity, model remediation cost, and draft the
audit report.

**Covers:**

- SSEG (Similarly Situated Employee Group) construction and validity testing
- Legitimate non-discriminatory factor (LNDF) selection and taint analysis
- Statistical regression model design (adjusted vs. unadjusted gaps, significance thresholds)
- Gap classification (EQUITABLE / AT-RISK / DISPARITY / SYSTEMIC)
- Remediation budget modeling (waterfall, targeted, and blanket approaches)
- EU Pay Transparency Directive 2023/970/EU compliance assessment
- US federal law (EPA, Title VII, Lilly Ledbetter) and multi-state compliance matrix
- Attorney-client privilege structuring for proactive audits
- Intersectionality analysis design
- Exposure estimation and prioritization
- Regulatory reporting requirement mapping

**Does not:**

- Execute statistical computations or run regression software (requires a qualified
  compensation analyst)
- Provide legal advice or substitute for qualified employment counsel
- Certify compliance with any specific regulatory requirement
- Replace the judgment of a credentialed compensation expert

---

## Jurisdiction and Governing Law

This skill is **US/EU dual-coverage** by design but structurally jurisdiction-agnostic —
the analysis framework adapts to the governing legal regime identified in Step 2.

**US Coverage:**

- Federal: Equal Pay Act of 1963 (29 U.S.C. § 206(d)), Title VII of the Civil Rights Act
  of 1964 (42 U.S.C. § 2000e), Lilly Ledbetter Fair Pay Act of 2009, Executive Order
  11246 (federal contractors — substantially modified by E.O. revocation January 2025
  [VERIFY CURRENT STATUS])
- State spotlight: California (SB 1162 / FEHA § 1197.5), New York (Labor Law § 194-b),
  Colorado (SB19-085 / CDLE rules), Illinois (EPRC program), Washington (SB 5761)

**EU Coverage:**

- EU Pay Transparency Directive 2023/970/EU — transposition deadline **7 June 2026**
- TFEU Article 157 (equal pay for equal work or work of equal value)
- Applies to all 27 EU member states via national transposition legislation

[JURISDICTION-SPECIFIC] For other jurisdictions:

- **UK**: Equality Act 2010, Gender Pay Gap Regulations 2017 (250+ employee mandatory
  reporting; April 5 snapshot; March 31 publication deadline) [VERIFY current rules;
  EU Directive does **not** apply post-Brexit]
- **Canada**: Employment Equity Act; Ontario Pay Equity Act 1987; Federal Pay Equity
  Act 2021 (phased implementation) [VERIFY current phase and FPED guidance]
- **Australia**: Workplace Gender Equality Act 2012; WGEA employer pay gap publication
  began February 2024 [VERIFY current publication thresholds and obligations]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses and asks when:

- The answer changes which legal framework applies (US-only, EU-only, or multinational)
- Audit purpose affects privilege structuring (proactive legal audit vs. HR initiative)
- Data scope decisions affect SSEG construction or minimum sample size
- Remediation budget or timeline constraints affect the modeling approach

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

Accept the engagement in any of these formats:

- **Payroll data description**: Summary of available data fields (job codes, levels,
  demographics, compensation elements, tenure, location, performance ratings)
- **Audit scope document**: HR or legal memo defining the audit population and purpose
- **Regulatory inquiry or audit notice**: OFCCP scheduling letter, EEOC charge, state
  agency request, or EU competent authority inquiry
- **Existing analysis**: Prior pay equity report to update or benchmark against
- **Abstract question**: "We need to run a pay equity analysis before our EU Directive
  deadline" or "Help us prepare for an OFCCP audit" or "We just received an EEOC charge"

If only a general question is provided, proceed to Step 2 to gather context.

---

### Step 2: Gather Context

**⟁ CLARIFY** — Ask the user (skip questions already answered by the input):

1. **Audit purpose** — This determines privilege structuring:
   - **Proactive legal audit** (directed by counsel for legal advice on discrimination
     exposure): Attorney-client privilege and work product protections may apply if
     properly structured. Strongly recommended as the default.
   - **HR compensation review** (initiated by HR/Total Rewards without formal legal
     direction): No privilege protection; findings fully discoverable in litigation.
   - **Regulatory compliance** (OFCCP audit, state agency request, EU Directive
     reporting): Specific disclosure obligations apply; privilege may be limited.
   - **Due diligence** (M&A, IPO, or other corporate transaction): Acquirer may demand
     disclosure; privilege waiver risk is high.

2. **Jurisdiction(s)** — Which legal frameworks apply?
   - US federal only
   - US federal + specific states (list states)
   - EU member states (list countries)
   - US + EU multinational
   - Other jurisdiction(s) (specify)

3. **Employer profile**:
   - Total US employee headcount (determines federal contractor obligations, SB 1162
     threshold, EPRC applicability, EU Directive reporting tier)
   - Federal contractor status (yes / no / uncertain — affects OFCCP exposure even
     post-January 2025 rollback for existing obligations [VERIFY CURRENT STATUS])
   - Industries with special pay structures (healthcare, financial services, tech, retail,
     professional services — affects SSEG complexity)
   - Presence of collective bargaining agreements (union and non-union employees must be
     in separate SSEGs)

4. **Protected classes to analyze** (select all that apply):
   - Gender / sex (required for most jurisdictions)
   - Race / ethnicity (required for California CRD, Illinois EPRC, Title VII analysis)
   - Intersectionality (gender × race) — recommended; requires larger sample sizes
   - Age (ADEA / EU Framework Directive 2000/78/EC)
   - Other (disability, national origin, religion — specify)

5. **Data available** — Which of these fields exist in the HR/payroll system?
   - Demographics: gender, race/ethnicity, age
   - Job identifiers: job code, job title, job family, job level/grade, FLSA status
   - Compensation: base salary, target bonus, actual bonus, LTIP/equity, total cash
   - Human capital: company tenure, position tenure, prior relevant experience, education
   - Performance: performance rating, last rating cycle, multi-year average
   - Location: work location, geographic pay zone, remote/hybrid status
   - Structural: full/part-time, union/non-union, regular/contract/intern, shift

6. **Audit scope**:
   - All employees in all locations
   - Specific business unit(s), function(s), or geography
   - Specific demographic concern (follow-up on a charge or complaint)
   - Promotion/hiring analysis in addition to compensation

7. **Remediation context**:
   - Budget or timeline constraints for remediation?
   - Plans to communicate adjustments to employees?
   - Prior pay equity analysis available for trend comparison?

**If the user provides partial context**, proceed with reasonable defaults and state
assumptions explicitly (e.g., "I'll assume US federal + California given the employee
profile — confirm if additional states apply").

---

### Step 3: Build Legal Authority Reference

Use **legalcode-mcp** to build a working reference file for this audit.

**Research targets:**

1. **Active statutory obligations** for each identified jurisdiction:
   - Current federal regulatory guidance (EPA, Title VII, any post-2025 EEOC rule changes)
   - State equal pay statute version and current enforcement priorities
   - EU Directive transposition status for relevant member states (as of 7 June 2026
     deadline) [VERIFY transposition progress per country]

2. **Enforcement priorities and recent agency guidance**:
   - EEOC strategic enforcement plan for the relevant period [VERIFY CURRENT]
   - OFCCP directive status post-January 2025 executive orders [VERIFY CURRENT —
     enforcement posture has changed dramatically]
   - State agency enforcement actions and public audit settlements (especially California
     CRD, Illinois IDOL)

3. **Case law** relevant to the audit's design:
   - _Castaneda v. Partida_, 430 U.S. 482 (1977) — 2-standard-deviation rule for
     inferring discrimination [VERIFY]
   - _Hazelwood School District v. United States_, 433 U.S. 299 (1977) — statistical
     disparity standard in employment discrimination [VERIFY]
   - _Ledbetter v. Goodyear Tire & Rubber Co._, 550 U.S. 618 (2007) / Lilly Ledbetter
     Fair Pay Act — tolling and paycheck accrual rule [VERIFY]
   - _Rizo v. Yovanovitch_, 950 F.3d 1217 (9th Cir. 2020) (en banc) — prior salary
     alone cannot justify a pay differential under the EPA in the 9th Circuit [VERIFY
     current circuit split status]
   - _Corning Glass Works v. Brennan_, 417 U.S. 188 (1974) — "equal work" functional
     equivalence standard [VERIFY]

4. **Save the most relevant results** to `/tmp/legalcode-pay-equity-authority.md`:

   ```markdown
   # Legal Authority Reference — Pay Equity Audit

   ## Employer: [name]

   ## Jurisdictions: [list]

   ## Date Gathered: [date]

   ### US Federal Statutes

   - [Statute, section, key rule]

   ### State Statutes and Regulations

   - [Statute, state, current requirement]

   ### EU Directive Requirements (Transposition Status)

   - [Country, transposition status, key obligations]

   ### Case Law

   - [Case, citation, key holding]

   ### Recent Enforcement Actions

   - [Agency, action, settlement amount, key facts]
   ```

**If legalcode-mcp is not connected:**

- Proceed with the general legal analysis in this skill
- Mark all specific citations with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Urgently flag the OFCCP enforcement posture section — it has changed fundamentally
  since January 2025 and this skill's general description may be stale [VERIFY CURRENT]

---

### Step 4: Scope Similarly Situated Employee Groups (SSEGs)

SSEGs (also called Pay Analysis Groups / PAGs) define the populations within which
like-for-like comparisons are made. SSEG construction is the most consequential
methodological decision in any pay equity analysis — it determines what comparisons
are legally and statistically valid.

**⟁ CLARIFY** — Identify the SSEG construction approach:

- **Option A — Narrow SSEGs** (job code/title + level + function): Creates many small
  groups; may fall below the statistical minimum (30 employees total, 5 per demographic
  group). More transparent but may miss cross-title disparities. Commonly used in OFCCP
  compliance reviews.
- **Option B — Broad SSEGs** (pay grade/band + broad function): Creates fewer, larger
  groups with more statistical power. Risks obscuring within-band discrimination.
  Better aligned to EU Directive "equal work or work of equal value" standard.
- **Option C — Pooled model with fixed effects** (single model with SSEG membership as
  a control variable): Maximum statistical efficiency; used by leading analytics platforms
  (Syndio, Trusaic, Mercer EDGE). Requires more sophisticated model design.
- **Option D — Iterative** (start broad; subdivide where sample sizes permit):
  Best practice for organizations without established pay architecture.

**SSEG Validity Check** — Evaluate each proposed SSEG:

| Check                      | Minimum Standard                                                                    | If Fails                                                                        |
| -------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Total size                 | ≥ 30 employees                                                                      | Merge with adjacent SSEG or flag as "below threshold — qualitative review only" |
| Protected class count      | ≥ 5 members of each demographic group                                               | Suppress quantitative results; flag for qualitative review                      |
| Job content comparability  | Employees perform substantially similar work at similar skill/effort/responsibility | Further subdivide if job content is materially different                        |
| Pay band span              | Employees are within 1–2 pay grades of each other                                   | Split by pay band if span exceeds 2 grades                                      |
| Union/non-union separation | Collectively bargained and non-CBR employees should not be mixed                    | Create separate SSEG for each union bargaining unit                             |

**Document the SSEG rationale** for each group — courts and OFCCP economists scrutinize
grouping decisions as potential manipulation of the analysis.

---

### Step 5: Validate Legitimate Non-Discriminatory Factors (LNDFs)

LNDFs are the control variables in the regression model. They must be:

- **Documented**: Consistently recorded in the HRIS and available for the full audit period
- **Job-related**: Directly relevant to compensation under the organization's pay structure
- **Non-tainted**: Not themselves the product of discriminatory practices

**Standard LNDF Checklist:**

| LNDF Category         | Variables                                                          | Validation Check                                                                        |
| --------------------- | ------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| **Job-related**       | Job level/grade, job function, FLSA status, pay grade              | Confirm grades are consistently applied; check for grade inflation by demographic       |
| **Performance**       | Annual rating (numeric), last rating, multi-year average           | Check rating distribution by demographic group for rater bias patterns                  |
| **Tenure/Experience** | Company tenure (years), position tenure, prior industry experience | Verify consistent HRIS recording; confirm experience claims validated at hire           |
| **Education**         | Highest degree level, field of study, certifications               | Verify required vs. preferred; confirm applied consistently across comparators          |
| **Market / Location** | Geographic pay zone, MSA labor market index, remote/hybrid tier    | Verify market data source is current and applied consistently                           |
| **Structural**        | Full-time/part-time, shift differential indicator, employment type | Verify consistent classification; check for classification discrepancies by demographic |

**Taint Analysis — Flag these LNDFs for legal review:**

| LNDF                                    | Taint Risk  | Analysis Required                                                                                                                                                                                                                                                       |
| --------------------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Prior salary**                        | HIGH        | EPA 9th Cir.: cannot justify differential standing alone (_Rizo v. Yovanovitch_) [VERIFY circuit]. Salary history inquiry banned in CA, NY, CO, IL, WA, MA, NJ, OR, and others [VERIFY current state list]. Recommend testing the model with and without this variable. |
| **Negotiation outcome**                 | MEDIUM-HIGH | If women or minorities systematically negotiate less, using negotiation as an LNDF launders the structural barrier. Test empirically: is there a demographic pattern in negotiated adjustments?                                                                         |
| **Performance ratings**                 | MEDIUM      | If calibration data shows demographic disparity in how ratings are awarded, using them as LNDFs embeds discrimination in the model. Run a rating distribution analysis by demographic group before including.                                                           |
| **Time-in-band**                        | MEDIUM      | If promotion rates into higher bands differ by demographic, time-in-band reflects cumulative promotion barriers, not neutral tenure. Check promotion equity before using.                                                                                               |
| **"Market pricing" for specific roles** | LOW-MEDIUM  | If market rates correlate with race (e.g., systematically undervalued roles held predominantly by women of color), using market as an LNDF perpetuates systemic undervaluation — a recognized phenomenon the EU Directive explicitly addresses.                         |

**⟁ CLARIFY** — If any high-taint LNDFs are in the proposed model:

- "Prior salary is proposed as a control variable. This carries legal risk in the 9th
  Circuit and is prohibited by salary history ban statutes in [list applicable states].
  Do you want to (a) include it with a legal risk flag, (b) test the model with and
  without it, or (c) exclude it entirely? Running both versions is often the most
  defensible approach — it allows you to quantify how much the prior salary variable
  is explaining."

---

### Step 6: Statistical Analysis Design

This step produces a statistical analysis specification — a document the compensation
analyst uses to execute the model. The AI designs the analytical approach; it does not
run regressions.

#### 6a. Regression Model Specification

**Standard specification for a single SSEG:**

```
Model type: OLS with log-transformed dependent variable
Dependent variable: ln(Total_Cash_Compensation_i)
  [Consider modeling base, bonus, and total separately for triangulation]

Independent variables:
  Demographic (primary test variables):
    Female_i          [1 = female; 0 = male — or per available gender coding]
    Minority_i        [or separate race/ethnicity indicators if multiple groups]

  Job-related LNDFs:
    Job_Level_i       [ordinal or dummy variables per level]
    Job_Function_FE_i [fixed effects per function/department]
    Pay_Grade_i       [if distinct from job level]

  Performance:
    Performance_Rating_i [lag one cycle where available — avoids contemporaneous bias]

  Tenure/Experience:
    Company_Tenure_i         [years]
    Company_Tenure_Squared_i [captures diminishing returns to tenure]

  Market / Location:
    Geographic_Zone_FE_i [fixed effects per location tier]

  Structural:
    Part_Time_Indicator_i
    Shift_Differential_i

  Optional — add if sample size permits:
    Female_i × Minority_i [interaction term for intersectional analysis]
    Year_FE_i             [fixed effects for multi-year panel analysis]
```

**Report from each model:**

1. Coefficient on each demographic variable (β₁ for Female, β₂ for Minority, etc.)
2. Standard error and t-statistic
3. p-value (flag p ≤ 0.10 for monitoring; p ≤ 0.05 for formal gap finding)
4. 95% confidence interval for the coefficient
5. Dollar magnitude: (exp(β) − 1) × median total cash = estimated median dollar gap
6. Effect size (Cohen's d) for practical significance assessment
7. R-squared and adjusted R-squared (model fit quality — low R-squared suggests
   important LNDFs may be missing)
8. Individual outlier analysis: identify employees whose actual pay is ≥1.5 SD below
   predicted pay in the direction of their protected class

#### 6b. Statistical Significance Thresholds

| Threshold           | Standard               | Classification                                      |
| ------------------- | ---------------------- | --------------------------------------------------- |
| p ≤ 0.01 (≥2.58 SD) | High significance      | DISPARITY — Tier 1: highest remediation priority    |
| p ≤ 0.05 (≥2.0 SD)  | Significant            | DISPARITY — Tier 2: remediate in current cycle      |
| p ≤ 0.10 (≥1.65 SD) | Borderline significant | AT-RISK: monitor; remediate if budget allows        |
| p > 0.10            | Not significant        | EQUITABLE (subject to practical significance check) |

**Apply the practical significance override**: If a gap is not statistically significant
but the median dollar gap is ≥$2,500/year per affected employee AND ≥10 employees are
affected, flag as AT-RISK regardless of p-value — aggregate exposure and ethical
considerations apply even without statistical significance.

#### 6c. Unadjusted vs. Adjusted Gap Reporting

Always report **both** metrics:

| Metric             | What It Shows                                                                              | Where Required                                                                                    |
| ------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| **Unadjusted gap** | Raw mean/median difference; includes structural job-level differences                      | EU Directive mandatory public reporting; public-facing pay gap statements; California CRD reports |
| **Adjusted gap**   | Unexplained residual after controlling for LNDFs; the legally relevant discrimination test | Internal audit; OFCCP compliance analysis; litigation analysis                                    |

**EU Directive note**: The Directive requires reporting of the **unadjusted** pay gap by
worker category in the mandatory public report. The **joint pay assessment** (triggered
at 5%+ gap) then requires root cause analysis — effectively an adjusted analysis. Both
metrics are required for full EU compliance.

#### 6d. Cohort and Trend Analysis

In addition to the cross-sectional regression, design these supplemental analyses:

1. **Hire-cohort analysis**: Compare starting salaries for men vs. women (or majority vs.
   minority) who entered the organization in the same year at the same level. Isolates
   initial pay-setting discrimination from subsequent drift.

2. **Merit increase distribution analysis**: Compare mean merit increase percentage by
   demographic group within each performance rating tier. Tests whether raises are applied
   consistently for equivalent performance. A significant difference in merit rates across
   demographic groups at the same rating tier is a strong indicator of discriminatory
   compensation system operation.

3. **Year-over-year trend**: If prior year data is available, compare the adjusted gap
   coefficient across years to measure whether remediation is working.

---

### Step 7: Classify Gaps and Assign Severity

After receiving statistical analysis results from the analyst's model, classify each
finding using the four-tier system below.

#### EQUITABLE — No remediation required

- Adjusted pay gap not statistically significant (p > 0.10)
- No practically significant dollar magnitude (median gap < $2,500/year or < 10 affected
  employees)
- Unadjusted gap fully explained by documented, non-tainted LNDFs
- Data quality sufficient for reliable inference
- **Response**: Document for audit record. Monitor at next scheduled audit cycle.
  No corrective action required.

#### AT-RISK — Monitor and legal review required

Any of the following:

- Gap borderline significant (0.05 < p ≤ 0.10)
- Gap not statistically significant but practically significant (≥$2,500/year median,
  ≥10 employees)
- SSEG below minimum threshold — results unreliable; qualitative review required
- One or more LNDFs fail the taint test — model reliability impaired
- Data quality issues prevent reliable inference (missing demographics, inconsistent
  job coding)
- Gap in a prior year has been reduced but not fully eliminated
- State or EU reporting shows unadjusted gap >5% that has not been fully explained

- **Response**: Schedule legal review. Implement data quality remediation. Plan for
  targeted analysis in next cycle. Estimate contingent exposure. Do not remediate without
  further analysis — premature remediation can be used as evidence of prior knowledge.

#### DISPARITY — Remediation required

Any of the following:

- Adjusted gap statistically significant at p ≤ 0.05
- Individual outlier analysis identifies ≥5 employees ≥1.5 SD below predicted pay in
  the direction of the protected class driving the disparity
- Cohort analysis shows statistically significant starting salary differential
- Merit increase analysis shows significant under-allocation to one demographic group at
  equivalent performance ratings
- EU Directive joint pay assessment trigger: unadjusted gap > 5% in any worker category
  not explained by objective, gender-neutral criteria

- **Response**: Remediate in the current compensation cycle (or next cycle if mid-cycle).
  Calculate individual remediation amounts. Model total budget. Implement structural fixes
  (pay band correction, job evaluation update, merit process calibration). Document
  rationale for each adjustment. Report as required by applicable law.

#### SYSTEMIC — Escalate immediately

Any of the following:

- Statistically significant adjusted gaps across 3+ SSEGs affecting the same protected
  class
- Pattern of disparity at initial hire + merit + promotion — consistent with
  enterprise-wide structural discrimination
- Disparity exceeds 3% adjusted gap with p ≤ 0.01 affecting 50+ employees
- Evidence of intentional pay-setting discrimination (documented differential treatment
  in compensation committee records, hiring manager instructions, or comp planning data)
- Active EEOC charge or OFCCP investigation that has identified similar patterns
- EU Directive failure: employer has not conducted a joint pay assessment within 6 months
  of identifying a 5%+ gap, and the 12-month remediation window is expiring

- **Response**: Escalate to General Counsel and C-suite immediately. Engage outside
  counsel. Prepare for class action exposure analysis (FLSA collective action; Title VII
  Rule 23 class; PAGA in California). Assess voluntary disclosure vs. defensive posture.
  Consider interim remediation for the most severely affected individuals while the full
  analysis is completed.

#### Severity Tiers Within DISPARITY and SYSTEMIC

| Tier | Median Dollar Gap | Affected Population | p-value | Examples |
|------|------------------|--------------------|---------|---------||
| **Tier 1 — Immediate** | ≥$5,000/year | ≥50 employees | ≤ 0.01 | Engineering SSEG: 3.5% female adjusted gap; 120 affected women |
| **Tier 2 — High** | $2,500–$5,000/year | 10–49 employees | ≤ 0.05 | Regional sales SSEG: 2.8% minority adjusted gap; 23 affected employees |
| **Tier 3 — Standard** | < $2,500/year | < 10 employees | ≤ 0.10 | Small specialized SSEG; borderline significance; limited dollar exposure |

---

### Step 8: Remediation Budget Modeling

For each DISPARITY or SYSTEMIC finding, model the remediation cost before presenting
recommendations.

#### 8a. Individual Outlier Identification

1. From the regression model output, extract the predicted compensation for each employee
2. Flag employees whose actual compensation is ≥1.5 SD below predicted and who belong to
   the protected class driving the disparity
3. Rank by severity (standard deviations below predicted)
4. Calculate the delta: amount needed to bring each individual to their predicted
   compensation (or to a peer midpoint, if that is higher)

#### 8b. Remediation Approaches

| Approach                    | Description                                                                                      | Cost Profile                   | Best Used When                                                                       |
| --------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------ | ------------------------------------------------------------------------------------ |
| **Targeted**                | Adjust only identified statistical outliers to predicted pay or peer midpoint                    | Lowest cost; most defensible   | Clear outlier pattern; budget-constrained; preference for precision                  |
| **Waterfall**               | Rank by severity; adjust most severely underpaid first; cascade upward until budget is exhausted | Moderate; controllable         | Budget is binding; need to show demonstrable progress within cycle                   |
| **Statistical threshold**   | Remediate until adjusted gap drops below the p ≤ 0.10 significance threshold                     | Efficient; analytically driven | Goal is demonstrable statistical compliance; optimization over pure equity           |
| **Band midpoint alignment** | Bring all protected-class employees below band midpoint up to midpoint                           | Higher cost; structural fix    | Systemic band-positioning problem identified; midpoint compression is the root cause |
| **Blanket percentage**      | Apply flat % increase to all members of the affected group                                       | Highest cost; blunt instrument | Simple communication required; significant union pressure; small group sizes         |

**⟁ CLARIFY** — For large or budget-sensitive remediation findings:

- "The DISPARITY finding in the [SSEG] SSEG affects [N] employees with an estimated [X]%
  adjusted gap. Targeted remediation of identified outliers is estimated at $[amount].
  Full elimination of the statistical gap would cost approximately $[amount]. Do you want
  to model (a) full remediation, (b) targeted remediation to the statistical significance
  threshold, or (c) a phased approach over [2–3 merit cycles]?"

#### 8c. Remediation Budget Template

For each DISPARITY or SYSTEMIC finding, complete:

```
SSEG: [name]
Protected class affected: [gender / race / intersectional]
Adjusted gap: [X]% (p = [value]) | Median dollar gap: $[Y]/year
Total affected employees: [number]
Outliers identified (≥1.5 SD below predicted in protected class direction): [number]

Individual remediation amounts:
  Employee [anonymized ID]: Current $[X] → Target $[Y] = $[delta]/year
  [repeat for each flagged individual]

Remediation approach selected: [targeted / waterfall / threshold / blanket]
Total annual remediation cost: $[amount]
Total 3-year Ledbetter lookback cost: $[amount × 3]
Liquidated damages risk if litigated (1× back pay): $[amount]

Budget timing recommendation:
  [Incorporate in next merit cycle / Immediate off-cycle adjustment / Phased over 2 cycles]

Communication recommendation:
  [Proactive with individual adjustment letters — route through counsel /
   Quiet system adjustment — counsel to advise on notification risk /
   Legal counsel to determine approach before any communication]

Structural fix required:
  [Pay band recalibration / Job evaluation review / Merit calibration change / Other]

Post-remediation monitoring:
  [Rerun model at next cycle to confirm gap closure]
```

#### 8d. EU Directive Joint Pay Assessment Budget Modeling

For employers triggering the EU 5%+ threshold in any worker category:

1. Identify the specific worker category (per Article 9 job architecture) with the gap
2. Separate the legitimately explainable portion from the unexplained residual
3. Calculate the cost to reduce the total gap to below 5% in that category
4. Model the timeline for remediation vs. the 12-month Directive window
5. Document the joint assessment process: who is involved (employer + workers'
   representatives), what criteria are being reviewed, what corrective measures are
   proposed, and by when they will be implemented

---

### Step 9: Compliance Reporting Requirements Check

Systematically check all mandatory reporting obligations for the employer's jurisdiction
profile identified in Step 2.

#### US Reporting Matrix

| Obligation | Trigger | Deadline | Content Required |
|-----------|---------|----------|-----------------||
| **California SB 1162 pay data report** | 100+ CA employees (or labor contractor) | Second Wednesday of May annually | Median and mean hourly rate by job category × race/ethnicity × sex; establishment-level; labor contractor report separate |
| **Illinois EPRC renewal** | 100+ IL private employees | IDOL-assigned staggered deadline; every 2 years | Pay equity analysis; EEO-1 data; wage data by gender/race/ethnicity; certification of compliance |
| **Colorado promotion posting** | Any employer with ≥1 CO employee | Same day as external posting | Salary range; benefits description; all promotion opportunities to current CO employees on same day |
| **NY pay transparency** | 4+ NY employees | Ongoing — all postings | Compensation range (min/max base rate); applies to remote roles reportable to NY |
| **WA pay transparency** | 15+ employees (any with WA presence) | Ongoing — all postings | Salary scale (genuine range); general description of all benefits and other compensation |
| **Federal contractor AAP comp analysis** | Existing AAPs under prior E.O. 11246 [VERIFY CURRENT — E.O. rescinded January 2025] | Annual for AAPs in force [VERIFY] | Compensation analysis demonstrating non-discrimination; consult counsel on current obligations |

#### EU Directive Reporting Matrix

| Employer Size     | First Report Due                     | Frequency     | Key Content                                                                                                                              |
| ----------------- | ------------------------------------ | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| 250+ employees    | **7 June 2027** (covering 2026 data) | Annually      | Gender pay gap in base pay and supplementary/variable pay by worker category; quartile distribution; proportion receiving bonuses by sex |
| 150–249 employees | **7 June 2027** (covering 2026 data) | Every 3 years | Same content as above                                                                                                                    |
| 100–149 employees | **7 June 2031** (covering 2030 data) | Every 3 years | Same content                                                                                                                             |
| < 100 employees   | Member state discretion              | —             | No EU-level obligation; verify national transposition for broader coverage                                                               |

**5% joint assessment trigger (all size bands)**:

If the mandatory report reveals a gender pay gap exceeding **5%** in any worker category
that cannot be justified by objective, gender-neutral criteria:

1. Employer and workers' representatives must conduct a **joint pay assessment**
2. Must be initiated within **6 months** of the report identifying the gap
3. Corrective measures must be implemented within **12 months** of the joint assessment
4. Failure to comply shifts the **burden of proof** in any subsequent equal pay litigation
   to the employer — non-compliance is not just a regulatory fine risk, it creates a
   rebuttable presumption of discrimination in litigation (Article 18)

**Burden of proof implication (Article 18)**: Where an employer has failed to comply with
pay transparency or reporting obligations, a rebuttable presumption of discrimination
arises in any equal pay litigation. This direct litigation consequence means that
non-compliance is not merely a penalty risk — it can determine the outcome of lawsuits.

---

### Step 10: Quality Verification

Before delivering the audit report, run all quality checks:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every SYSTEMIC or Tier 1 DISPARITY finding, run the 3-pass Self-Interrogation.
3. Assign a Confidence Score to each gap classification.
4. Verify: Have all identified SSEGs been assessed? Are all applicable reporting deadlines
   flagged? Has the privilege structuring recommendation been addressed?
5. Generate the Glass Box Audit Trail.

---

## Analysis Reference

### Federal Law Summary

**Equal Pay Act of 1963 (29 U.S.C. § 206(d))**

Prohibits sex-based wage discrimination for equal work on jobs requiring equal skill,
effort, and responsibility performed under similar working conditions at the same
establishment. Key rules:

- **Functional equivalence standard**: "Equal work" means substantially equal job content
  based on actual duties performed, not job titles or descriptions. A few extra incidental
  duties do not defeat EPA coverage (_Corning Glass Works v. Brennan_, 417 U.S. 188
  (1974) [VERIFY]).
- **Same-establishment limitation**: EPA requires comparison within the same physical
  establishment. California has eliminated this limitation — comparisons can be drawn
  across all California locations of the same employer (FEHA § 1197.5).
- **Employer bears the burden**: The employer must prove one of the four affirmative
  defenses. The employee need not disprove them.
- **Prior salary debate**: In the 9th Circuit, prior salary standing alone cannot justify
  a pay differential (_Rizo v. Yovanovitch_, 950 F.3d 1217 (9th Cir. 2020) (en banc)
  [VERIFY current circuit split — other circuits may differ]).

**Four EPA Affirmative Defenses:**

| Defense                             | Description                                                                               | Audit Relevance                                                                                                                          |
| ----------------------------------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Seniority system**                | Bona fide system based on length of service; consistently applied                         | Verify the system is documented and applied without demographic exceptions                                                               |
| **Merit system**                    | Formalized performance-based system; documented; known to employees; consistently applied | Check for demographic bias in the underlying rating distributions before accepting as LNDF                                               |
| **Production-based system**         | Piece rates, commissions, incentive pay tied to measurable output                         | Verify the output standard is facially neutral and applied equally                                                                       |
| **Any other factor other than sex** | Legitimate, job-related business reason not based on sex                                  | Most litigated defense; courts require a genuine business justification; prior salary in the 9th Circuit does not qualify standing alone |

**Title VII (42 U.S.C. § 2000e)**

Covers all protected classes; supports both disparate treatment (intentional) and
disparate impact (facially neutral policy with discriminatory effect) theories:

- Title VII pay claims **do not require a same-establishment comparator** (broader reach
  than EPA)
- Disparate impact theory allows challenge to facially neutral compensation systems
  (e.g., a merit-pay system that produces systematic racial gaps) without proving intent
- Employer must demonstrate **business necessity** once the employee establishes a
  statistically significant disparate impact; employee may then show a less discriminatory
  alternative existed

**Lilly Ledbetter Fair Pay Act of 2009**

The limitations period (180-day EEOC charge deadline) resets with each discriminatory
paycheck. Each paycheck, paycheck deposit, or other compensation payment that reflects
a discriminatory decision constitutes a new unlawful practice.

**Critical audit implication**: An employer must analyze the **origins** of current pay
disparities, not just their present state. A discriminatory salary offer made 10 years
ago that persists in today's pay structure continues to accrue new violations with every
payroll run. Historical audit scope should extend to the origins of identified disparities,
not just the current year.

---

### State Law Spotlight

#### California

**FEHA § 1197.5 (as amended)**

- "Substantially similar work" standard — broader than federal "equal work"
- Eliminates same-establishment limitation — comparisons across California locations
  of the same employer are permitted
- Prior salary alone cannot justify wage differentials [VERIFY current CRD enforcement
  position and any updated regulatory guidance]
- Statute of limitations: 3 years for Labor Code § 1197.5 claims

**SB 1162 (effective January 1, 2023)**

- Employers with 15+ employees must include salary or hourly wage range in all job
  postings (internal and external, including promotions and transfers)
- Employers with 100+ CA employees must file annual pay data report to CRD with
  **median and mean hourly rate** by job category × race/ethnicity × sex
- Labor contractor reports filed separately (100+ workers obtained through contractor)
- Penalties: $100/employee first failure; $200/employee subsequent failures
- CRD makes pay data reports publicly available — plaintiffs' firms actively mine them

#### New York

**NY Labor Law § 194-b (effective September 17, 2023)**

- Applies to employers with 4+ employees statewide
- All job postings (including promotions and internal transfers) must include the
  minimum and maximum base compensation range
- Applies to remote roles that are or could be performed by a New York-based employee
  and are reportable to a New York supervisor
- Does not require disclosure of bonuses, tips, or supplemental compensation
- Retaliation against employees who discuss compensation is prohibited

#### Colorado

**SB19-085 / Equal Pay for Equal Work Act (effective January 1, 2021)**

- "Substantially similar work" standard
- All job postings must include salary range + a general description of benefits and
  other compensation (applies to remote positions performable by a Colorado resident)
- All current Colorado employees must be notified of promotional opportunities on the
  **same calendar day** as external posting; employers cannot make a hiring decision
  before the same-day notification requirement is met
- Record retention: job descriptions and wage rate history must be maintained during
  employment and **2 years after separation**; failure to retain creates a **rebuttable
  presumption** that the missing records contained information favorable to the employee
- CDLE civil penalty: $500–$10,000 per violation [VERIFY CURRENT CDLE enforcement rules]

#### Illinois

**Equal Pay Registration Certificate (EPRC)**

- Private employers with 100+ Illinois employees must obtain an EPRC from IDOL
- Renewal required every 2 years; staggered IDOL-assigned deadlines
- Submission includes: (a) pay equity analysis; (b) statement of compliance with
  anti-discrimination laws; (c) EEO-1 data; (d) total wages paid by gender/race/ethnicity
- Certification that the employer reviews and addresses wage disparities
- Penalty for non-compliance: civil penalty up to $10,000; risk of loss of state contracts

#### Washington State

**SB 5761 / RCW 49.58.110 (effective January 1, 2023)**

- Applies to employers with 15+ employees (including those with at least one WA employee)
- All job postings must include: (a) wage scale or salary range (genuine range, not
  open-ended); (b) general description of all benefits and other compensation
- Applies to remote positions that could be performed by a Washington-based employee
- Must also disclose salary range for internal transfers and promotions
- Benefits disclosure is broad: healthcare, retirement, PTO (sick, parental, vacation),
  and any taxable fringe benefits must be described

---

### EU Pay Transparency Directive (2023/970/EU) Deep Dive

**The core structural shift**: The Directive moves EU employers from a reactive model
(respond to individual equal pay complaints) to a proactive one (identify and remediate
systemic pay gaps before complaints arise). It operationalizes TFEU Article 157 with
binding, uniformly enforced mechanisms across all 27 member states.

**Five operational requirements for employers:**

**Requirement 1 — Pay Structure (Article 9)**
Establish and maintain pay criteria based on objective, gender-neutral factors. The four
criteria: **skills, effort, responsibility, and working conditions**. Job evaluation
systems must be transparent and available to workers and their representatives. Where
workers' representatives exist, criteria must be agreed with them. This is the most
operationally demanding requirement — it requires a formalized job architecture that
most European employers lack.

**Requirement 2 — Recruitment Transparency (Article 5)**
Disclose the starting salary or pay range for every advertised position. Prohibit asking
candidates about salary history. Job titles and recruitment processes must be
gender-neutral.

**Requirement 3 — Right to Information (Article 7)**
Respond within **60 days** to employee requests for: (a) their own individual pay level;
and (b) the average pay levels, broken down by sex, for employees doing equal work or
work of equal value. Employers must inform workers of this right **annually**.

**Requirement 4 — Pay Gap Reporting (Article 9)**
Report gender pay gap data to the national competent authority and publish it. Report
must cover: unadjusted gender pay gap in base pay and supplementary/variable pay; gaps
within worker categories; proportion of male and female workers in each pay quartile;
gender gap in median bonus pay; proportion receiving bonuses and in-kind benefits by sex.

**Requirement 5 — Joint Pay Assessment (Article 10)**
Triggered where any reported pay gap exceeds 5% in any worker category and cannot be
justified by objective, gender-neutral criteria. Requires joint work with workers'
representatives to identify root causes and implement corrective measures within 12 months.

**"Equal work or work of equal value" standard**: The Directive adopts the broader "equal
value" standard from TFEU Article 157 — a lower bar for establishing comparability than
the US EPA's "substantially similar work" standard. Historically undervalued job
categories predominantly held by women cannot be compared only to themselves; they must
be assessed against male-dominated roles of equivalent value. This cross-role comparison
is the most analytically demanding aspect for US-trained pay equity practitioners.

---

## Pay Equity Classification System

### Classification Decision Tree

```
                         GAP PRESENT IN SSEG?
                                │
               ┌────────────────┴────────────────┐
              YES                                NO
               │                                 │
    STATISTICALLY SIGNIFICANT?              → EQUITABLE
               │
    ┌──────────┴──────────┐
   YES                    NO
    │                      │
  TAINTED      PRACTICALLY SIGNIFICANT?
  LNDFs?            │
    │         ┌─────┴─────┐
    │        YES           NO
    │         │             │
  AT-RISK  AT-RISK      EQUITABLE
    │
  (quantitative analysis
   impaired — legal review)
    │
  MULTI-SSEG PATTERN (3+)?
         │
  ┌──────┴──────┐
 YES            NO
  │              │
SYSTEMIC      DISPARITY
```

### Classification Summary Table

| Classification | Statistical Test                              | Practical Test                    | Action Required                                              | Escalation Level     |
| -------------- | --------------------------------------------- | --------------------------------- | ------------------------------------------------------------ | -------------------- |
| **EQUITABLE**  | p > 0.10                                      | Gap < $2,500/yr OR < 10 employees | Document; monitor next cycle                                 | None                 |
| **AT-RISK**    | 0.05 < p ≤ 0.10 OR tainted LNDFs              | May be present                    | Legal review; data quality fix; contingent exposure estimate | Internal legal       |
| **DISPARITY**  | p ≤ 0.05                                      | ≥$2,500/yr AND ≥10 employees      | Remediate this cycle; structural fix                         | Employment counsel   |
| **SYSTEMIC**   | p ≤ 0.05 across 3+ SSEGs OR p ≤ 0.01 at scale | ≥$5,000/yr, ≥50 employees         | Immediate escalation; class action analysis                  | GC + outside counsel |

---

## Prioritization Framework

| Priority           | Classification                                          | Dollar Threshold      | Population             | Timeline                                            | Typical Example                                                                            |
| ------------------ | ------------------------------------------------------- | --------------------- | ---------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **P1 — Immediate** | SYSTEMIC or DISPARITY Tier 1                            | ≥$5,000/yr median gap | ≥50 affected employees | Remediate before next payroll cycle; escalate to GC | Engineering SSEG: 3.5% female adjusted gap; 120 women affected; active EEOC charge pending |
| **P2 — High**      | DISPARITY Tier 2 or EU 5%+ threshold triggered          | $2,500–$5,000/yr      | 10–49 affected         | Remediate in current merit cycle or within 60 days  | Regional sales: 2.8% minority gap; 22 employees; EU reporting deadline in 90 days          |
| **P3 — Standard**  | DISPARITY Tier 3 or AT-RISK with practical significance | < $2,500/yr           | < 10 affected          | Remediate in next merit cycle (90–180 days)         | Small specialized SSEG; borderline significance; $1,600/yr median gap                      |
| **P4 — Watch**     | AT-RISK (no current violation)                          | Any                   | Any                    | Monitor; legal review; data quality improvement     | SSEG below 30-employee threshold; tainted LNDF under review; state reporting gap           |

---

## Attorney-Client Privilege Framework

Pay equity audits are routinely sought in discovery. Proactive audits that identify
unremediated disparities are particularly dangerous if privilege is not established.

**Required steps to establish protection:**

1. **Legal direction**: Documented instruction from outside counsel or General Counsel
   retaining the compensation analyst as a consultant to assist counsel in providing
   legal advice. An engagement letter between employer (through counsel) and the
   analytics firm is the standard vehicle.

2. **Legal purpose framing**: The engagement documentation must state that the purpose
   is obtaining legal advice on litigation exposure and compliance risk — not an HR
   compensation benchmarking or compensation equity improvement exercise.

3. **Communication routing**: All draft reports, findings, and recommendations must be
   addressed to and routed through counsel. Limit distribution strictly to those who
   need the information for the privileged legal purpose. Log all recipients.

4. **Dual-purpose separation**: If the audit must also satisfy a regulatory compliance
   purpose (historical OFCCP AAP compensation analysis; Illinois EPRC certification),
   structure the work products as two separate documents where possible — one privileged
   legal analysis, one regulatory compliance submission.

5. **Waiver risk events** — These actions waive privilege:
   - Disclosing findings to employees beyond what counsel specifically authorizes
   - Sharing the report with a compensation consultant not retained through counsel
   - Using audit findings to support a publicly issued pay equity statement without
     redacting privileged methodology
   - Disclosing to an insurer or auditor without appropriate waiver management

**⟁ CLARIFY** — If the engagement has not been structured through counsel:

- "This audit has not been described as attorney-client privileged. Once we identify
  statistical disparities, any unremediatedfindings will be fully discoverable in
  subsequent litigation. Do you want guidance on restructuring the engagement to protect
  the results before we proceed to findings? The privilege analysis is most important
  before any disparity is documented."

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any audit output. If any gate fails, revise
before delivery.

| Gate           | Rule                                                                                                                                                                                                                                    | Fail Action                                              |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute section, CFR provision, case citation, or regulatory guidance document                                                                                                                       | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a recognizable format (e.g., "29 U.S.C. § 206(d)", "2023/970/EU Art. 10", "950 F.3d 1217 (9th Cir. 2020)")                                                                                                         | Fix format                                               |
| **Currency**   | All threshold figures (headcount triggers, penalty amounts, reporting deadlines, salary thresholds), OFCCP enforcement posture, and EU transposition status flagged [VERIFY CURRENT] unless confirmed from current authoritative source | Flag "[CHECK CURRENCY — may have changed]"               |
| **Domain**     | Analysis stays within pay equity law — does not stray into benefits design, tax, ERISA, or other domains without noting the scope shift                                                                                                 | Remove or flag out-of-domain content                     |
| **Confidence** | Uncertainty is stated explicitly — enforcement positions that have changed (OFCCP post-January 2025; circuit-split LNDF rules) are flagged as "[VERIFY CURRENT STATUS]", not stated as settled law                                      | Add confidence qualifier                                 |

### Self-Interrogation for SYSTEMIC and Tier 1 DISPARITY Findings

For any finding classified as SYSTEMIC or DISPARITY Tier 1, apply this 3-pass review
before delivering the classification:

**Pass 1 — Statistical Chain Integrity**: Does the disparity finding follow logically from
the regression output? Is the SSEG construction defensible? Are the LNDFs appropriately
validated for taint? Would an OFCCP or EEOC economist, or a plaintiffs' expert, using the
same data, reach the same conclusion? Are there model specification weaknesses (low
R-squared, omitted variable bias, heteroskedasticity) that would undermine the finding?

**Pass 2 — Completeness**: Have all possible LNDFs been considered and tested? Are there
legitimate explanatory variables missing from the model that could account for part of the
gap? Has prior salary / negotiation LNDF taint risk been explicitly addressed? Has
intersectionality been checked? Has cohort analysis been run to confirm the cross-sectional
finding?

**Pass 3 — Challenge**: What is the strongest defense the employer can mount against this
classification? Under what circumstances might a court or arbitrator find this gap
adequately explained by legitimate factors? Is the SYSTEMIC classification proportionate —
could the multi-SSEG pattern be explained by a single localized cause (e.g., one business
unit, one manager cohort) rather than enterprise-wide structural discrimination? If
remediated now, is future re-emergence likely without a structural fix?

Mark the audit trail: `self_interrogation: PASS` or `self_interrogation: REVISED —
[explanation of what changed after interrogation]`.

### Confidence Scoring

Apply to each gap classification:

| Level        | Range     | Meaning                                                                                                | Action                                                                                           |
| ------------ | --------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| **Definite** | 0.95–1.0  | Settled disparity on clean data; clear statutory or regulatory basis                                   | State with full confidence                                                                       |
| **High**     | 0.80–0.94 | Strong statistical result; minor data quality questions; well-understood legal framework               | State with brief data quality caveat                                                             |
| **Probable** | 0.60–0.79 | Borderline statistical result; good arguments but data-dependent; emerging or contested legal question | State with explicit reasoning and contra-indicators                                              |
| **Possible** | 0.40–0.59 | Below significance threshold; genuine uncertainty; model sensitivity concerns                          | Flag for legal review; present both sides                                                        |
| **Unlikely** | 0.0–0.39  | Insufficient data; speculative; SSEG below minimum threshold; conflicting signals                      | Do not classify; flag as "[INSUFFICIENT DATA — further analysis required before classification]" |

---

## Anti-Patterns

What NOT to do in a pay equity audit. Every member of the audit team should review this list.

1. **Failing to establish attorney-client privilege before the analysis begins.** The
   moment findings are recorded, they are potentially discoverable. HR-initiated audits
   without legal direction are never privileged. A proactive audit that identifies
   unremediated disparities and is not privileged becomes a roadmap for plaintiffs' counsel.
   Structure correctly at the start — this cannot be corrected retroactively.

2. **Building SSEGs using job titles rather than actual job content.** Job titles are
   inconsistently administered, subject to inflation, and do not reliably reflect
   skill/effort/responsibility equivalence. Grouping by title either over-groups (places
   dissimilar roles together) or under-groups (separates equivalent roles with different
   titles), producing results that are neither accurate nor defensible.

3. **Omitting variable pay and equity components from the analysis.** Analyzing only base
   salary and ignoring bonuses, commissions, LTIP, and equity grants misses where many
   gender and race disparities are concentrated — particularly in roles with large
   discretionary variable pay. The EU Directive explicitly requires analyzing supplementary
   and variable components separately.

4. **Using tainted control variables.** Including prior salary (prohibited in many states,
   legally risky in the 9th Circuit), biased performance ratings, or discriminatory
   promotion ladders as LNDFs embeds the discrimination into the model and produces a
   result that purports to "explain away" a gap that is actually a violation. Perform
   explicit taint analysis on every proposed LNDF before including it.

5. **Treating a statistically insignificant result as a clean bill of health.** In SSEGs
   below the 30-employee minimum, non-significance reflects insufficient statistical power,
   not the absence of disparity. Apply qualitative review and practical significance tests
   to all SSEGs below the minimum threshold.

6. **Treating a statistically significant result in a very large SSEG as automatically
   material.** In a group of 10,000 employees, a 0.3% adjusted gap can reach p < 0.001
   while representing a $250/year median difference. Always assess both statistical
   significance and dollar magnitude before classifying. The two-standard-deviation rule
   from _Castaneda_ was never intended to establish materiality at any scale.

7. **Ignoring intersectionality.** Running gender-only and race-only models without
   examining the intersection misses compound disadvantage that is frequently larger than
   either standalone analysis. Black women, Latinas, and Asian women in many sectors face
   adjusted gaps that significantly exceed either their gender cohort or their racial
   cohort alone.

8. **Analyzing only cross-sectional compensation and skipping cohort and trend analysis.**
   An organization can show no adjusted gap at a given point in time while systematically
   under-allocating merit increases to women over 5 years, producing compounding gaps that
   will appear fully developed in the next audit cycle. The cross-sectional model is a
   necessary but insufficient picture.

9. **Remediating individual pay without fixing the structural cause.** Paying outliers
   more without correcting the pay band structure, job evaluation system, or merit
   allocation process that generated the gap will recreate the same disparity within
   2–3 compensation cycles. The structural fix costs more upfront and is the only durable
   solution.

10. **Broadcasting audit findings before privilege is confirmed.** Each additional recipient
    who receives audit findings and does not need them for the privileged legal purpose
    weakens or destroys the privilege. Findings must be routed through counsel; every
    distribution must be controlled and logged. Do not include business unit leaders,
    finance stakeholders, or communications teams on draft audit results.

11. **Conducting a dual-purpose audit without understanding OFCCP disclosure risk.**
    An audit that simultaneously satisfies OFCCP compliance requirements and serves as a
    privileged legal analysis is a disclosure target. Structure as two separate work
    products where both purposes apply. Note: OFCCP enforcement has been substantially
    curtailed since January 2025 [VERIFY CURRENT STATUS] — but the disclosure risk
    for state agencies and private litigation remains fully intact.

12. **Failing to document the legitimate business reason for compensation decisions at the
    time they are made.** When an audit later reveals an outlier, the inability to explain
    why an individual was paid above or below their predicted compensation converts a
    potentially defensible business decision into an unexplained statistical anomaly.
    Real-time documentation of comp decisions is a foundational preventive control.

13. **Applying the Lilly Ledbetter lookback only to recent compensation decisions.** Given
    that each paycheck resets the limitations period, liability can extend to the original
    discriminatory pay-setting decision — potentially decades ago. An audit covering only
    the current year does not address historical exposure embedded in the existing pay
    structure.

14. **Ignoring the hiring and promotion pipeline in favor of compensation-only analysis.**
    Pay gaps are frequently the downstream result of discriminatory patterns in initial
    placement levels, hiring rates, and promotion decisions, not compensation-setting per se.
    A compensation-only audit will report "no gap within levels" while missing the
    structural barrier preventing women or minorities from reaching higher levels.

15. **Relying on HRIS data without validation.** Missing demographic data, inconsistent
    job classification codes, stale performance ratings, and inaccurate tenure records are
    endemic in HR information systems. An analysis built on dirty data will produce
    unreliable results regardless of statistical sophistication. Data quality remediation
    is a prerequisite — not an afterthought — to the analysis.

16. **Applying a one-size-fits-all significance threshold.** p ≤ 0.05 is a useful
    guideline, not a universal rule. For small SSEGs (n < 30), qualitative review and
    practical significance should dominate. For very large SSEGs, both statistical and
    practical significance are required. For SSEGs with active enforcement risk (pending
    charges, recent similar settlements), consider pre-emptive remediation of borderline
    findings regardless of p-value.

17. **Failing to account for the EU "equal value" standard when analyzing multinational
    employers.** US audits based on "equal work" or "substantially similar work" may
    satisfy US legal standards while missing the cross-role comparisons required by the
    EU Directive's "equal value" standard. The Directive requires assessing whether roles
    that are of equal value — even if they involve different types of work — are paid
    equally. This can reveal systematic undervaluation of predominantly female job
    categories that would not be captured by a US-style within-function analysis.

18. **Treating the EU Pay Transparency Directive as a reporting exercise only.** The
    Directive's substantive obligations — proactive job architecture documentation,
    gender-neutral job evaluation criteria, annual right-to-information compliance — are
    ongoing operational requirements, not a one-time reporting event. Employers who build
    their compliance program around the reporting deadlines without implementing the
    underlying job evaluation framework will face the 5%+ trigger with no analytical
    infrastructure to respond to it.

---

## Writing Standards

Apply plain-language discipline to all audit output before delivery.

**For executive summaries and classification findings** (shared with leadership):

- Define every abbreviation on first use: SSEG (Similarly Situated Employee Group),
  LNDF (Legitimate Non-Discriminatory Factor), EEOC (Equal Employment Opportunity
  Commission). Do not assume familiarity.
- Active voice: "The gender gap in the Engineering SSEG is statistically significant at
  the 5% level" not "A statistically significant gender gap was found to exist."
- Every finding must name: the affected group, the magnitude (% and dollar), the
  confidence level, and what the employer must do about it.
- Every DISPARITY or SYSTEMIC finding must include a one-sentence remediation action
  so the reader knows immediately what response is required.

**For statistical methodology sections** (reviewed by analysts and counsel):

- Define all statistical terms on first use (p-value, adjusted gap, Cohen's d, SSEG).
- Report figures to 2 decimal places. Do not over-precision.
- Explicitly flag model limitations: small n, missing LNDFs, data quality issues.
- Include confidence intervals, not just point estimates. The interval communicates
  precision; a point estimate alone overstates certainty.

**Quality gates before delivery:**

1. Can a non-technical HR leader or business executive read the executive summary and
   know exactly what the problem is and what to do next?
2. Can outside employment counsel understand each gap classification and defend or
   explain it in a regulatory or litigation context?
3. Is every legal claim backed by a specific citation (or flagged [VERIFY])?
4. Are all threshold figures (headcount triggers, penalty amounts, reporting deadlines,
   enforcement posture) marked [VERIFY CURRENT] or confirmed from a current source?
5. Does every DISPARITY and SYSTEMIC finding include a specific remediation action?
6. Is the Glass Box audit trail complete and accurate?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 3, search for current versions of each applicable statute (EPA, Title VII,
  California FEHA § 1197.5 / SB 1162, Illinois Equal Pay Act / EPRC, EU Directive
  transposition status per country)
- Verify current EEOC strategic enforcement plan and recent pay discrimination settlements
- Verify current OFCCP enforcement posture [CRITICAL — dramatically changed post-January
  2025; general skill description may be stale]
- Search for recent state agency pay equity enforcement actions in the employer's
  industry and states
- Verify current headcount thresholds, penalty amounts, and reporting deadlines
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with the analysis framework and general legal analysis in this skill
- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Flag the following as requiring urgent independent verification before any filing or
  external communication:
  - OFCCP enforcement posture and obligations post-January 2025 executive orders
    [VERIFY CURRENT — posture has fundamentally changed]
  - California CRD reporting deadlines, format requirements, and current enforcement
  - EU Directive transposition status in specific member states (as of June 2026 deadline)
  - Current circuit split on prior salary as LNDF [VERIFY jurisdiction-specific status]
  - All penalty amounts and headcount thresholds (frequently amended by state legislatures)

---

## Output Format Template

Deliver the audit in the following format:

```markdown
# Pay Equity Audit Report

## [Employer Name] — [Audit Scope]

**Audit Date**: [date]
**Audit Period Covered**: [date range — based on available data and Ledbetter lookback]
**Jurisdictions Analyzed**: [list all]
**Protected Classes Analyzed**: [gender; race/ethnicity; intersectional — list]
**Total SSEGs Analyzed**: [number] (SSEGs below threshold — suppressed: [number])
**Audit Purpose**: [Proactive legal audit / HR review / Regulatory compliance / Due diligence]
**Privilege Status**: [Directed by counsel — [name] / Not privileged / To be confirmed]
**Prepared by**: AI-assisted (legalcode-pay-equity-audit) — requires employment attorney
and credentialed compensation analyst review before any remediation, filing, or disclosure

---

## Executive Summary

### Overall Risk Profile

| Dimension                             | Finding                                                        | Classification                               |
| ------------------------------------- | -------------------------------------------------------------- | -------------------------------------------- |
| Adjusted gender pay gap               | [X]% overall weighted average; [N] SSEGs with significant gaps | [EQUITABLE / AT-RISK / DISPARITY / SYSTEMIC] |
| Adjusted race/ethnicity pay gap       | [X]% overall; [N] SSEGs with significant gaps                  | [EQUITABLE / AT-RISK / DISPARITY / SYSTEMIC] |
| Intersectional analysis               | [finding or "Not analyzed — below sample size threshold"]      | [classification]                             |
| EU Directive exposure (if applicable) | [5%+ threshold triggered: Y/N; which worker categories]        | [COMPLIANT / AT-RISK / TRIGGER]              |
| US state reporting compliance         | [outstanding obligations or "All current"]                     | [COMPLIANT / AT-RISK / NON-COMPLIANT]        |

### Priority Findings

| Priority | Finding       | SSEG        | Adjusted Gap     | Affected Population | Est. Annual Remediation |
| -------- | ------------- | ----------- | ---------------- | ------------------- | ----------------------- |
| P1       | [description] | [SSEG name] | [X]% (p=[value]) | [N] employees       | $[amount]               |
| P2       | [description] | [SSEG name] | [X]% (p=[value]) | [N] employees       | $[amount]               |
| [repeat] |               |             |                  |                     |                         |

**Total estimated annual remediation cost**: $[range]
**Total estimated litigation exposure** (Ledbetter 3yr + liquidated damages): $[range]
**Highest-priority action**: [one clear sentence]

---

## SSEG-by-SSEG Analysis

### SSEG: [Name]

**Total employees**: [count] | **Gender**: [X% F / Y% M] | **Race/ethnicity**: [breakdown]

#### Statistical Results

| Analysis                      | Adjusted Gap | p-value | Std. Error | 95% CI         | Cohen's d | Confidence |
| ----------------------------- | ------------ | ------- | ---------- | -------------- | --------- | ---------- |
| Gender (Female vs. Male)      | [X]%         | [value] | [value]    | [[low]–[high]] | [value]   | [level]    |
| Race/Ethnicity                | [X]%         | [value] | [value]    | [[low]–[high]] | [value]   | [level]    |
| Intersectional (F × Minority) | [X]%         | [value] | —          | —              | —         | [level]    |

**Unadjusted gap** (for EU reporting): [X]% gender; [Y]% race/ethnicity
**Model fit**: R-squared = [value] (adequate / note if low — potential omitted LNDFs)

**Classification**: [EQUITABLE / AT-RISK / DISPARITY / SYSTEMIC] — Tier [1/2/3 if DISPARITY]
**LNDFs Used**: [list each with taint status: CLEAN / AT-RISK / EXCLUDED]
**Data Quality**: [GOOD / FAIR / POOR — description of any data quality concerns]

#### Individual Outliers (if DISPARITY or SYSTEMIC)

| ID (anonymized)           | Group | Actual Comp | Predicted Comp | Delta/yr | SD Below Predicted |
| ------------------------- | ----- | ----------- | -------------- | -------- | ------------------ |
| EMP-[001]                 | F     | $[X]        | $[Y]           | $[Z]     | [N] SD             |
| [repeat for each outlier] |       |             |                |          |                    |

#### Remediation Estimate

| Approach                 | Outliers Adjusted | Annual Cost | 3-yr Ledbetter Cost | Est. Post-Remediation p-value |
| ------------------------ | ----------------- | ----------- | ------------------- | ----------------------------- |
| Targeted (outliers only) | [N]               | $[amount]   | $[amount]           | [estimated]                   |
| Statistical threshold    | [N]               | $[amount]   | $[amount]           | > 0.10                        |
| Full elimination         | All affected      | $[amount]   | $[amount]           | > 0.10                        |

**Recommended approach**: [specific approach with rationale]
**Structural fix required**: [yes/no — description]

[Repeat for each SSEG]

---

## Compliance Reporting Check

| Obligation                         | Applicable?                 | Status                                 | Next Deadline                | Action Required |
| ---------------------------------- | --------------------------- | -------------------------------------- | ---------------------------- | --------------- |
| California SB 1162 pay data report | [Y/N]                       | [Filed / Pending / Overdue]            | [second Wed. of May]         | [action]        |
| Illinois EPRC renewal              | [Y/N]                       | [Certified / Pending / Not certified]  | [IDOL-assigned date]         | [action]        |
| Colorado promotion posting         | [Y/N]                       | [Compliant / Gap identified]           | Ongoing                      | [action]        |
| NY pay transparency                | [Y/N]                       | [Compliant / Gap identified]           | Ongoing                      | [action]        |
| Washington pay transparency        | [Y/N]                       | [Compliant / Gap identified]           | Ongoing                      | [action]        |
| EU Directive reporting             | [Y/N + countries]           | [Not yet due / Filed / Overdue]        | [June 2027 for 250+]         | [action]        |
| EU 5%+ joint assessment            | [Triggered / Not triggered] | [In progress / Not required / Overdue] | [within 6 months of trigger] | [action]        |

---

## Remediation Roadmap

| Priority | SSEG   | Classification   | Action                                           | Owner                                | Deadline         | Budget    |
| -------- | ------ | ---------------- | ------------------------------------------------ | ------------------------------------ | ---------------- | --------- |
| P1       | [name] | DISPARITY Tier 1 | Individual pay adjustments + pay band correction | Total Rewards + GC + outside counsel | [date]           | $[amount] |
| P2       | [name] | DISPARITY Tier 2 | Integrate into next merit cycle                  | HR Business Partner + Compensation   | Next merit cycle | $[amount] |
| P3       | [name] | AT-RISK          | Data quality remediation; LNDF taint review      | HRIS + Compensation Analytics        | 90 days          | Ops cost  |
| P4       | [name] | AT-RISK          | Quarterly monitoring; schedule next analysis     | Employment Counsel                   | Ongoing          | —         |

---

## Total Exposure Summary

| Category                   | Affected Population | Annual Pay Gap | 3-yr Ledbetter Exposure | Liquidated Damages Risk | Conservative Total |
| -------------------------- | ------------------- | -------------- | ----------------------- | ----------------------- | ------------------ |
| Gender — all SSEGs         | [N]                 | $[amount]      | $[amount]               | $[amount × 1]           | $[amount]          |
| Race/ethnicity — all SSEGs | [N]                 | $[amount]      | $[amount]               | $[amount × 1]           | $[amount]          |
| **TOTAL**                  | [N]                 | **$[amount]**  | **$[amount]**           | **$[amount]**           | **$[amount]**      |

**Conservative total reserve estimate**: $[low range]
**Aggressive plaintiff class action estimate**: $[high range]
**Recommended reserve**: $[suggested amount — counsel to advise]

---

## Recommended Next Steps

1. **Immediate** (within 5 business days): [e.g., Confirm privilege structure with GC;
   retain outside counsel; identify P1 employees for interim review]
2. **Short-term** (within 30 days): [e.g., Complete targeted remediation for P1 findings;
   confirm LNDF taint analysis with legal team; validate data quality for AT-RISK SSEGs]
3. **Medium-term** (within 90 days): [e.g., Implement pay band corrections for root cause;
   rerun merit increase distribution analysis; refresh HRIS demographic data]
4. **Annual cadence**: [e.g., Integrate pay equity analysis into annual merit cycle planning;
   establish EU Directive joint assessment calendar; schedule next full audit]
5. **Structural fix**: [e.g., Commission formal job architecture and job evaluation review;
   implement structured merit calibration by level; revise hiring salary-setting guidelines
   to eliminate market-pricing-from-prior-salary approach]

---

## Glass Box Audit Trail

[YAML block — see Glass Box Audit Trail section below]
```

---

## Glass Box Audit Trail

Complete this template and append to every audit output:

```yaml
glass_box:
  skill_name: "legalcode-pay-equity-audit"
  audit_date: "[date]"
  employer: "[employer name or anonymized identifier]"
  jurisdictions:
    us_federal: true
    us_states: "[list of states analyzed or 'N/A']"
    eu_member_states: "[list of countries or 'N/A']"
  employer_headcount_us: "[number or 'Not provided']"
  federal_contractor_status: "[Yes / No / Unknown / E.O. 11246 rescinded Jan 2025 — VERIFY CURRENT OBLIGATIONS]"
  protected_classes_analyzed: "[gender / race/ethnicity / intersectional / age / other]"
  total_ssegs_constructed: "[number]"
  ssegs_below_threshold: "[number — qualitative review only]"
  ssegs_with_findings:
    equitable: "[number]"
    at_risk: "[number]"
    disparity: "[number]"
    systemic: "[number]"
  tier_1_disparity_findings: "[number]"
  audit_purpose: "[proactive legal audit / HR review / regulatory compliance / due diligence]"
  privilege_status: "[attorney-client privileged — directed by [counsel name] / Not privileged / To be confirmed]"
  lndf_taint_flags: "[list any tainted LNDFs identified, with disposition]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "/tmp/legalcode-pay-equity-authority.md / Not created"
  statutes_consulted:
    - "29 U.S.C. § 206(d) (Equal Pay Act of 1963) — [VERIFIED / UNVERIFIED]"
    - "42 U.S.C. § 2000e (Title VII, Civil Rights Act) — [VERIFIED / UNVERIFIED]"
    - "Lilly Ledbetter Fair Pay Act of 2009 — [VERIFIED / UNVERIFIED]"
    - "2023/970/EU Arts. 5, 7, 9, 10, 18 (EU Pay Transparency Directive) — [VERIFIED / UNVERIFIED]"
    - "Cal. FEHA § 1197.5 / SB 1162 — [VERIFIED / UNVERIFIED]"
    - "[Additional statutes as applicable]"
  case_law_consulted:
    - "Castaneda v. Partida, 430 U.S. 482 (1977) — 2-SD rule — [VERIFIED / UNVERIFIED]"
    - "Rizo v. Yovanovitch, 950 F.3d 1217 (9th Cir. 2020) — prior salary — [VERIFIED / UNVERIFIED]"
    - "Corning Glass Works v. Brennan, 417 U.S. 188 (1974) — [VERIFIED / UNVERIFIED]"
    - "[Additional cases as applicable]"
  estimated_remediation_range: "$[low] – $[high]"
  estimated_litigation_exposure: "$[low] – $[high]"
  self_interrogation: "PASS / REVISED — [explanation] / NOT APPLICABLE (no SYSTEMIC or Tier 1 findings)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  citations_verified: "[number VERIFIED via legalcode-mcp] / [number UNVERIFIED — counsel to confirm]"
  key_verify_flags:
    - "OFCCP enforcement posture and obligations post-January 2025 E.O. revocation [VERIFY CURRENT]"
    - "Circuit split on prior salary as LNDF under EPA — verify applicable circuit [VERIFY]"
    - "EU Directive transposition status in [specific member states] [VERIFY — June 2026 deadline]"
    - "California CRD current reporting format and deadline [VERIFY CURRENT]"
    - "[Any additional verification items]"
  limitations:
    - "All statistical conclusions require validation by a credentialed compensation analyst against actual payroll data — this skill designs the analysis, it does not execute it"
    - "Exposure estimates are illustrative — actual exposure depends on complete payroll records, available affirmative defenses, class composition, and litigation dynamics"
    - "EU Directive analysis assumes transposition by June 2026 — verify national implementing legislation for each member state before relying"
    - "OFCCP enforcement obligations have fundamentally changed post-January 2025 executive orders — verify current contractor obligations before any regulatory submission"
    - "Intersectional analysis results are indicative only where cell sizes are below 30 employees"
    - "Ledbetter lookback exposure is theoretical maximum — actual liability depends on available defenses, class certification, and statute of limitations arguments"
    - "[Any additional scope limitations or data quality caveats]"
  reviewer: "AI-assisted — requires review by qualified employment attorney AND credentialed compensation analyst before any remediation action, regulatory filing, public disclosure, or communication to employees"
```

---

## Localization Notes

### United Kingdom

Gender Pay Gap Regulations 2017 (Equality Act 2010, s. 78):

- Mandatory annual reporting for employers with 250+ UK employees
- Snapshot date: **April 5**; publication deadline: March 31 (private sector) / March 30
  (public sector) of the following year
- Must report: mean and median gender pay gap in hourly pay; mean and median bonus pay gap;
  proportion of men and women receiving bonuses; proportion of men and women in each pay
  quartile band
- No proactive "equal value" job assessment required for the report itself, but Equality
  Act 2010 equal pay claims can be brought on an "equal value" basis
- EU Pay Transparency Directive does **not** apply in Great Britain post-Brexit
- [VERIFY current UK reporting obligations and any post-2025 regulatory changes]

### Canada

- **Federal Pay Equity Act 2021**: Proactive pay equity regime for federally regulated
  private and public-sector employers with 10+ employees; requires formal job evaluation
  using gender-neutral comparison systems and a pay equity plan [VERIFY current
  implementation phase and FPEC guidance]
- **Ontario Pay Equity Act 1987**: Applies to Ontario public and private employers with
  10+ employees; requires job evaluation and pay equity maintenance [VERIFY current
  enforcement under OPEO]
- Provincial variations significant: Quebec, Manitoba, and Nova Scotia have pay equity
  legislation; other provinces rely on human rights codes [VERIFY province-specific]

### Australia

- **Workplace Gender Equality Act 2012 (WGEA)**: Non-public-sector employers with 100+
  employees must submit annual WGEA reports
- **Major 2023–2024 change**: WGEA began publishing individual employer gender pay gap
  data in February 2024 — employers can no longer treat their pay gap as confidential
  internal data [VERIFY current publication thresholds and scope]
- Employers with a gap above the WGEA threshold must develop a gender equality strategy
  [VERIFY current threshold and strategy requirements]

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on comprehensive research
into: EU Pay Transparency Directive 2023/970/EU (EUR-Lex publication; Ogletree, Debevoise,
Pinsent Masons, and Littler transposition analysis; Syndio transposition tracker); US
federal pay equity law (Equal Pay Act 1963; Title VII Civil Rights Act 1964; Lilly Ledbetter
Fair Pay Act 2009; EEOC enforcement guidance and FY 2024 recovery data); multi-state
compliance requirements (California SB 1162 / FEHA § 1197.5; New York Labor Law § 194-b;
Colorado SB19-085 / CDLE rules; Illinois EPRC program; Washington SB 5761); statistical
methodology for pay equity analysis (OLS regression design; SSEG/PAG construction; LNDF
selection and taint analysis; Castaneda/Hazelwood 2-SD standard; Berkshire Associates,
Edgeworth Economics, and Equity Methods methodology sources); attorney-client privilege
structuring (OFCCP Directive 2022-02; revised August 2022 position; Gibson Dunn, Davis
Wright Tremaine, and K&L Gates analysis; post-January 2025 OFCCP rollback from Hunton
and GCCUpdate sources); remediation budget modeling approaches (Trusaic pay equity deep
dive series; Equity Methods remediation strategy analysis); enforcement landscape (EEOC
FY 2024 recovery data; OFCCP settlement database pre-rollback; EEOC notable litigation
fact sheet; Seyfarth Shaw pay equity litigation key developments). Structural quality
frameworks adapted from the legalcode-contract-review reference standard (Citation Quality
Gates, Self-Interrogation, Confidence Scoring, Glass Box audit trail, Anti-patterns
catalogue, Writing Standards) and the legalcode-wage-hour-compliance-audit compliance
classification framework (COMPLIANT/AT-RISK/VIOLATION tiering, exposure quantification,
prioritization). All statutory and case law references require independent verification
before reliance in any legal matter.
