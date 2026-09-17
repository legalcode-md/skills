---
name: legalcode-non-compete-analysis-cn
description: Deep enforceability analysis of Chinese non-compete clauses (竞业限制) governed by Labor Contract
  Law of the PRC (劳动合同法) Articles 23-24 and the SPC Consolidated Judicial Interpretation on Labor Disputes
  (最高人民法院关于审理劳动争议案件适用法律问题的解释(一), effective 1 January 2021) and SPC Judicial Interpretation II (Fa Shi
  [2025] No. 12, effective 1 September 2025). Use when reviewing a non-compete clause (竞业限制条款) in a Chinese
  employment contract (劳动合同), executive agreement, severance package, or standalone restrictive covenant
  agreement; advising on waiver strategy at termination; assessing an employee's ability to join a competitor;
  planning workforce restructuring; or reviewing non-compete provisions in M&A employment due diligence
  for a Chinese target or acquiree.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Deep enforceability analysis of Chinese non-compete clauses (竞业限制) governed by Labor Contract Law of the PRC (劳动合同法) Articles 23-24 and the SPC Consolidated Judicial Interpretation on Labor Disputes (最高人民法院关于审理劳动争议案件适用法律问题的解释(一), effective 1 January 2021) and SPC Judicial Interpretation II (Fa Shi [2025] No. 12, effective 1 September 2025). Covers the three eligible employee categories (senior management / senior technical staff / confidentiality-obligation holders), mandatory monthly economic compensation (国家默认30%上一年月均工资; Shenzhen 50% minimum), the 2-year hard duration cap, geographic and activity scope reasonableness, employer waiver mechanics and timing (pre-termination vs. post-termination), employee breach consequences (liquidated damages + compelled continued performance), employer non-payment release trigger (3 consecutive months), employer early-termination 3-month compensation penalty, mandatory pre-litigation labor arbitration, and the 2025 SPC Interpretation II proportionality and access-gating rules. Produces ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID classification with confidence-scored enforceability assessment, per-deficiency remediation steps, and Glass Box audit trail. Use when reviewing a non-compete clause (竞业限制条款) in a Chinese employment contract (劳动合同), executive agreement, severance package, or standalone restrictive covenant agreement; advising on waiver strategy at termination; assessing an employee's ability to join a competitor; planning workforce restructuring; or reviewing non-compete provisions in M&A employment due diligence for a Chinese target or acquiree. Routes from legalcode-non-compete-analysis (cross- jurisdictional router) for China-specific deep analysis. China only — not for commercial non-competes in M&A seller/shareholder agreements (Anti-Monopoly Law context) or in franchise agreements.


# Legalcode — Chinese Non-Compete Analysis (竞业限制)

> **免责声明 / Disclaimer**
>
> 本技能提供基于人工智能的竞业限制条款分析框架，不构成法律意见（法律咨询）。所有分析结果
> 在用于任何执行、放弃、诉讼或谈判决策之前，必须由具备中国劳动法执照的合格律师进行审核。
> 竞业限制相关法律通过司法解释和各地方法院判决持续演进——2025年9月施行的《最高人民法院
> 关于审理劳动争议案件适用法律问题的解释（二）》已实质性更改分析框架，请核实现行法律规定。
> 本技能引用的法规和判例存在幻觉风险——使用前请在 pkulaw.com、北大法宝、法信 或最高人民
> 法院官方网站核实原文。
>
> **Disclaimer**: This skill provides a framework for AI-assisted analysis of Chinese
> non-compete clauses (竞业限制). It does not constitute legal advice (法律咨询). All
> outputs must be reviewed by a qualified Chinese labor lawyer (劳动法律师) before any
> enforcement, waiver, litigation, or negotiation decision. Chinese non-compete law evolves
> through SPC interpretations and local court decisions — the September 2025 SPC
> Interpretation II has materially changed the analytical framework; verify current law.
> Statutory and case law references cited from memory carry hallucination risk — verify
> against pkulaw.com, PKU Law, or the SPC's official portal before relying on them.

---

## Purpose and Scope

This skill performs deep enforceability analysis of Chinese post-employment non-compete
agreements (竞业限制协议/条款) under the Labor Contract Law framework and the SPC
Judicial Interpretations. It operates as the China-specific deep-analysis route from
the cross-jurisdictional `legalcode-non-compete-analysis` router skill.

**Covers:**

- Complete enforceability assessment under LCL Arts. 23-24 and SPC Interpretation I/II
- Eligible employee scope (3 statutory categories + 2025 access-gating rule)
- Written form requirement and integration with employment contract or separate agreement
- Mandatory economic compensation: national 30% default; Shenzhen 50% floor; regional variations
- Geographic scope reasonableness analysis (city / regional / national / global)
- Activity scope reasonableness and "genuine competitive relationship" functional test
- Duration assessment against the 2-year hard statutory cap
- Employer waiver mechanics: at-termination (preferred) vs. post-termination (costly)
- Employee breach: liquidated damages, continued performance obligation, new employer liability
- Employer non-payment: 3-month trigger for employee release from obligation
- Employer early-termination: 3-month additional compensation penalty
- 2025 SPC Interpretation II: during-employment non-competes; proportionality codification;
  access-gating invalidity rule
- Mandatory labor arbitration pre-litigation requirement; 1-year limitation period
- Interaction with trade secret protection under AUCL (反不正当竞争法)
- M&A context: share vs. asset acquisition treatment of employee non-competes
- Glass Box audit trail for full traceability

**Does not:**

- Analyse non-solicitation of customers (客户非招揽条款) or non-disclosure agreements
  in isolation — see `legalcode-nda-triage` and `legalcode-employment-agreement-review`
- Apply to commercial non-competes in M&A seller / founding-shareholder agreements,
  which are reviewed under the Anti-Monopoly Law (反垄断法) framework with different
  (more permissive) standards; note this and advise separate M&A counsel
- Apply to non-competes in Chinese franchise agreements (特许经营协议) — see
  `legalcode-franchise-agreement-review` for franchise-context analysis
- Cover non-Chinese employment relationships governed by foreign law
- Substitute for qualified Chinese legal counsel in any specific matter

**Related skills:**

- `legalcode-non-compete-analysis` — Cross-jurisdictional router (entry point)
- `legalcode-employment-agreement-review` — Full employment agreement clause-by-clause review
- `legalcode-nda-triage` — NDA and trade secret covenant review
- `legalcode-severance-agreement-review` — Severance agreement with non-compete interaction
- `legalcode-non-compete-analysis-de` — Germany HGB §§ 74-75a deep analysis
- `legalcode-non-compete-analysis-fr` — France clause de non-concurrence deep analysis

---

## Jurisdiction and Governing Law

**Governing law**: Labor Contract Law of the People's Republic of China (中华人民共和国
劳动合同法), promulgated 29 June 2007, effective 1 January 2008. Non-compete provisions
at Articles 23-24.

**Primary judicial authority**: SPC Consolidated Judicial Interpretation on Several
Issues Concerning the Application of Law in the Trial of Labor Dispute Cases (I)
(最高人民法院关于审理劳动争议案件适用法律问题的解释(一)), effective 1 January 2021
(consolidating the prior four separate interpretations, including the former "SPC
Interpretation III" and "SPC Interpretation IV"). References to the "former SPC
Interpretation IV" Articles 6-10 are now codified in Interpretation (I).

**2025 development**: SPC Judicial Interpretation II on Labor Dispute Cases (Fa Shi
[2025] No. 12, issued 1 August 2025, effective 1 September 2025) — materially changes
non-compete analysis, particularly: (1) express recognition of during-employment non-
competes without additional compensation; (2) invalid clause if employee lacked trade
secret access; (3) proportionality codification (scope must be commensurate with
actual trade secret exposure).

**Mandatory employment law principle**: An employer cannot contract around China's
non-compete protections by choosing the law of a more-permissive jurisdiction. The LCL
applies as mandatory law to all employment relationships performed on Chinese territory.
The "most protective law" principle means that even a foreign-law governing clause does
not disapply the LCL when the work is performed in China.

**Regional overlay**: Shenzhen Special Economic Zone imposes a 50% minimum compensation
floor above the national 30% default. Other provincial rules (Jiangsu, Zhejiang, Beijing)
also vary. Identify employee work location before applying the compensation rules.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming context, the workflow pauses and asks when:

- The applicable regional compensation floor is unclear (work location ambiguous)
- The employee's role and trade secret access are disputed
- The employer is deciding whether to enforce or waive at the time of termination
- The governing document type may affect which SPC Interpretation provision applies
- The analysis reveals the non-compete is in an M&A context (commercial vs. employment law)

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

### Step 1: Accept the Clause or Agreement

Accept the non-compete provision in any of these formats:

- **Full employment contract** (劳动合同) or standalone non-compete agreement
  (竞业限制协议) — paste text or provide file path
- **Clause extract** — the 竞业限制 provision extracted from a larger document
- **Summary of key terms** — duration, geographic scope, activity scope, compensation
  amount (if full text unavailable — note this limitation in output)
- **Verbal description** — for planning/structuring queries (output is advisory only;
  actual enforceability assessment requires the clause text)

If only a summary or verbal description is provided, flag all findings with [TEXT NOT
REVIEWED — BASED ON DESCRIBED TERMS] and note that actual enforceability may differ
once full clause language is assessed.

### Step 2: Gather Context

**⟁ CLARIFY** — Ask the user (skip questions already answered):

1. **Work location / employee's Chinese city**:
   - Options: Shenzhen (50% minimum applies), Beijing, Shanghai, Guangzhou, Other
     specific city (specify province), Unknown / not yet determined
   - _Why this matters_: Regional compensation floors vary materially. Shenzhen's
     50% statutory minimum overrides the national 30% default.

2. **Perspective**:
   - Options: Employer (enforcement strategy / waiver planning), Employee (challenge /
     exit planning), In-house counsel (full risk picture), HR / people operations,
     M&A due diligence
   - _Why this matters_: The analysis, output framing, and recommendations differ
     significantly by perspective.

3. **Employee's role and seniority** (free text):
   - "Describe the employee's title, functional role, salary (approximate annual RMB),
     actual access to trade secrets or confidential technology, and any proprietary
     client/customer relationships managed."
   - _Why this matters_: Post-2025 SPC Interpretation II, a non-compete is invalid if
     the employee never had access to trade secrets or IP-related confidential information.
     This is now the threshold validity question.

4. **Document type**:
   - Options: Clause in the main employment contract, Standalone 竞业限制协议,
     Amendment (added during employment), Severance agreement (离职协议), Other
   - _Why this matters_: Mid-employment amendments have different analysis under
     2025 SPC Interpretation II; during-employment non-competes are now expressly valid.

5. **Timing context**:
   - Options: Pre-hire review (drafting), During-employment review, Employee is
     departing NOW (waiver decision), Employee has already left (enforcement),
     Dispute in progress (arbitration / litigation)
   - _Why this matters_: Waiver mechanics and compensation obligations are timing-
     dependent. A late waiver triggers payment for the gap period.

### Step 3: Identify the Applicable Legal Framework

Based on context, identify:

**3a. Applicable compensation floor**

| Employee work location             | Applicable minimum                                                                     |
| ---------------------------------- | -------------------------------------------------------------------------------------- |
| Shenzhen SEZ                       | 50% of average monthly salary (12 months pre-departure)                                |
| Jiangsu Province (default)         | 1/3 of average salary [VERIFY local regulations]                                       |
| Zhejiang Province (default)        | 2/3 of average salary [VERIFY local regulations]                                       |
| Beijing (contract silent)          | 20-60% court discretion (typical ~30%)                                                 |
| All other China (national default) | 30% of average monthly salary (12 months pre-departure), floored at local minimum wage |

**3b. Key SPC Interpretation provisions**

| SPC Rule                          | Substance                                                                                                                                            |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Art. 6 equivalent (Interp. I)     | Contract silent on amount → 30% of prior 12-month average monthly salary, not less than local minimum wage                                           |
| Art. 7 equivalent (Interp. I)     | Both clause and compensation amount agreed → enforceable; employee must comply or compensate                                                         |
| Art. 8 equivalent (Interp. I)     | Employer fails to pay for **3 consecutive months** post-termination → employee may seek release                                                      |
| Art. 9 equivalent (Interp. I)     | Employer terminates the non-compete early (post-departure) → owes **3 additional months** of agreed compensation                                     |
| Art. 10 equivalent (Interp. I)    | Employee pays liquidated damages → does NOT discharge obligation to continue complying; employer can claim both damages AND continued compliance     |
| 2025 Interp. II Art. 13           | During-employment non-compete: valid without additional compensation                                                                                 |
| 2025 Interp. II Art. 14           | During-employment breach: liquidated damages available                                                                                               |
| 2025 Interp. II Art. 15           | **Access-gating invalidity rule**: clause void if employee never accessed or was not informed of trade secrets / IP-related confidential information |
| 2025 Interp. II (proportionality) | Scope, geography, and duration must be commensurate with the actual trade secrets the employee accessed; excess provisions are invalid               |

### Step 4: Scope and Eligibility Assessment

Assess the four foundational validity elements:

#### 4a. Eligible Employee Category

Evaluate whether the employee falls within one of the three statutory categories under
Article 24:

**Category 1 — Senior Management Personnel (高级管理人员)**

Defined by reference to the Company Law of the PRC: General Manager (经理), Deputy
General Manager (副经理), person responsible for financial affairs (财务负责人), Secretary
of the Board of Directors of a listed company (上市公司董事会秘书), and any person
designated as senior management in the company's articles of association (公司章程).

Analysis checklist:

- [ ] Is the employee listed in the articles of association as senior management?
- [ ] Does the employee hold functional authority commensurate with a statutory role?
- [ ] Courts look to actual decision-making power, not job title alone
- [ ] Department heads (R&D, procurement, legal) may qualify IF designated in articles

**Category 2 — Senior Technical Personnel (高级技术人员)**

No statutory definition. Court interpretation:

- [ ] Holds specialized technical expertise with significant commercial value to the employer
- [ ] Actually accessed core proprietary technology, processes, or formulas
- [ ] "Senior" qualifier is substantive — not all engineers or developers qualify
- [ ] Consider: seniority level, IP portfolio involvement, R&D decision-making authority

**Category 3 — Others with Confidentiality Obligation (其他负有保密义务的人员)**

Broadest category; most frequently contested.

- [ ] Employer expressly designated this employee in writing (employment contract, company policy, confidentiality agreement)
- [ ] Employee was actually informed of, and had access to, trade secrets or IP-related confidential information — **critical post-2025 SPC Interpretation II**
- [ ] Blanket application to all employees (including salespersons, security guards, administrative staff) who lack trade secret exposure → clause is VOID under 2025 rules
- [ ] Assess: what specific confidential information did this employee actually access?

**⟁ CLARIFY** — If the employee's category is ambiguous: "Does the employee's employment
contract or company articles of association expressly designate them as senior management
or state they have confidentiality obligations? And what specific trade secrets or
confidential information did they actually access in their role?"

**Eligibility classification:**

| Finding                                                                  | Classification                                              |
| ------------------------------------------------------------------------ | ----------------------------------------------------------- |
| Clearly within Category 1 or 2 with documented trade secret access       | ✅ ELIGIBLE — proceed                                       |
| Within Category 3 with documented access and written designation         | ✅ ELIGIBLE — proceed                                       |
| Title suggests eligibility but no evidence of actual trade secret access | ⚠️ AT-RISK — may be invalid post-2025 SPC Interpretation II |
| Low-level employee; no trade secret access; Category 3 claimed broadly   | ❌ VOID — access-gating rule applies                        |
| Non-eligible role (junior admin, cleaner, security, basic salesperson)   | ❌ VOID — cannot be bound                                   |

#### 4b. Written Form Requirement

Under Article 23, the non-compete obligation must be stated in:

- The employment contract (劳动合同) itself, OR
- A separate confidentiality agreement (保密协议) or non-compete agreement (竞业限制协议)

Assessment:

- [ ] Written instrument in place? (Oral agreements are not enforceable)
- [ ] Employee signed and received a copy? (Delivery/signature evidence)
- [ ] Is the agreement in Chinese? (Or bilingual with Chinese as controlling version?)
- [ ] For mid-employment amendments: mutual written consent documented?

**Beijing practice note**: Beijing courts have found non-competes unenforceable where
the employer could not prove the employee was delivered a copy of the signed agreement —
maintain signature records and delivery receipts.

#### 4c. Duration Assessment

- Article 24 hard cap: **maximum 2 years (24 months)** post-employment termination
- Any provision purporting to extend beyond 24 months is void by operation of statute
- Courts will not blue-pencil (reduce) a 3-year clause to 2 years — void provisions
  are severable but the employer may lose the entire restriction in some cases
- Clauses tolling the period for arbitration/litigation time → VOID under SPC Guiding
  Case No. 184 (July 6, 2022): "an anti-competition restriction cannot lawfully exclude
  the period during which the restricted person seeks judicial remedies"
- Typical enforceable durations: 6 months to 2 years; 1 year is market standard

#### 4d. Geographic and Activity Scope

**Geographic scope — reasonableness factors:**

- Proportional to the employer's actual geographic operations (not ambitions)
- Senior executive with national/global exposure → national or global scope typically upheld
- Mid-level technical employee → city-level or provincial scope more defensible
- "All countries globally" for a factory-floor software engineer → likely void
- No bright-line rule; courts apply a proportionality/reasonableness analysis

**Activity scope — "genuine competitive relationship" functional test (实质竞争关系):**

- Must restrict activities that genuinely compete with the former employer
- Courts conduct functional analysis of actual business model, target customers, and markets
- Do NOT rely solely on business license registration scope — courts look at actual commercial activities
- Key case: _Wang v Wande Information Technology_ [(2021) Hu 01 Min Zhong No. 12282]
  — financial data analytics firm and entertainment video platform were both "IT companies"
  but court found no genuine competitive relationship; non-compete breach not established
- 2025 SPC Interpretation II: scope must be commensurate with the specific trade secrets
  the employee accessed; restrictions "exceeding a reasonable proportion are invalid"

**Scope red flags:**

- Clause that prohibits employment in any company in the same industry (行业) rather than
  genuinely competing activities → likely overbroad and AT-RISK or VOID
- "New business" scope not yet launched by the employer at departure date → AT-RISK
- Scope broader than what the employee was actually exposed to → AT-RISK under 2025 rules

### Step 5: Compensation Analysis

Mandatory economic compensation (竞业限制经济补偿金) is a prerequisite for enforceability
in the post-employment context. Failure to pay = agreement invalid or voidable.

#### 5a. Agreed Compensation Assessment

| Compensation level                                                                 | Classification                                                                             |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Contract silent on amount                                                          | Apply 30% national default (or regional floor if higher); enforceable if employer pays     |
| ≥ 30% of prior 12-month average monthly salary (national) or ≥ 50% (Shenzhen)      | COMPLIANT                                                                                  |
| < 30% but > local minimum wage, and employer pays regularly                        | AT-RISK — courts may substitute 30%                                                        |
| Set at local minimum wage only (e.g., 5-8% of actual salary)                       | NON-COMPLIANT — courts will invalidate and substitute 30% per SPC; Shanghai precedent 2023 |
| Set nominally (e.g., RMB 100/month for a senior engineer earning RMB 50,000/month) | VOID as unconscionable / in bad faith                                                      |

**Calculation baseline** (unless regional rules differ):

- 30% × [(sum of monthly wages over the 12 months immediately preceding contract termination) ÷ 12]
- Floor: local monthly minimum wage for the city of work

**Shenzhen-specific calculation**:

- 50% × [(sum of monthly wages over the 12 months immediately preceding contract termination) ÷ 12]
- Source: Regulations of the Shenzhen Special Economic Zone on Labor Contracts
  (深圳经济特区劳动合同条例) [VERIFY current version and article number]

**Regional variations** (verify current local regulations before relying):

| Region            | Minimum rate                                        | Verification status                            |
| ----------------- | --------------------------------------------------- | ---------------------------------------------- |
| National default  | 30% of prior 12-month monthly average               | Codified in SPC Interpretation I               |
| Shenzhen SEZ      | 50% of prior 12-month monthly average               | [VERIFY — Shenzhen Labor Contract Regulations] |
| Jiangsu Province  | 1/3 of average salary (approx. 33%)                 | [VERIFY — Jiangsu provincial regulations]      |
| Zhejiang Province | 2/3 of average salary (approx. 67%)                 | [VERIFY — Zhejiang provincial regulations]     |
| Beijing           | 20-60% court discretion (typically applied at ~30%) | [VERIFY — Beijing court practice]              |

#### 5b. Payment Mechanics Assessment

Compensation must be paid **monthly** during the restriction period post-employment:

| Payment issue                                                  | Risk classification                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Paid monthly on time throughout restriction period             | ✅ COMPLIANT                                                               |
| Paid in arrears but before 3-month trigger                     | ⚠️ AT-RISK — employer in technical breach; cure risk                       |
| 3 consecutive months of non-payment due to employer            | ❌ NON-COMPLIANT — employee entitled to seek release; must apply to LDAC   |
| Employer attempts to pay lump sum at termination only          | [VERIFY local court practice — some courts accept, others require monthly] |
| Employer made partial payments below agreed or required amount | ⚠️ AT-RISK — courts may find non-payment if materially short               |

#### 5c. Employer Early Termination / Waiver

When the employer decides not to enforce the non-compete after employment ends:

| Timing of waiver                                               | Consequence                                                          |
| -------------------------------------------------------------- | -------------------------------------------------------------------- |
| Issued at termination date (preferred)                         | No ongoing compensation obligation; clean severance                  |
| Issued within agreed notice period during restriction          | 3 additional months of agreed compensation payable upon waiver       |
| Issued post-termination but before 3-month non-payment trigger | Still owe compensation for gap period to waiver date; then +3 months |
| Employer simply stops paying after 3 months                    | Employee released from obligation; employer still owes arrears       |

**Best practice**: Include a waiver provision allowing the employer to opt out by written
notice at or before termination, or at any time during the restriction period with a
notice period of 30 days and the 3-month additional payment obligation.

### Step 6: Enforce / Waive Decision Framework (Employer Perspective)

When advising an employer at the time of termination:

**⟁ CLARIFY** — "Has the employer decided whether to enforce this non-compete, or is
that decision still open?"

| Factor                                                             | Weight toward enforcement | Weight toward waiver |
| ------------------------------------------------------------------ | ------------------------- | -------------------- |
| Employee holds genuine trade secrets / core technical IP           | High                      | —                    |
| Competitive threat is immediate (joining direct competitor)        | High                      | —                    |
| Employee is leaving to competitor in a country without enforcement | —                         | High                 |
| Compensation rate creates ongoing financial burden                 | —                         | Moderate             |
| Evidentiary basis for eligible employee category is weak           | —                         | High (post-2025)     |
| Geographic or activity scope is questionable                       | —                         | Moderate             |
| Time remaining in restriction period is short                      | —                         | High                 |
| New employer is willing to indemnify employee for damages          | —                         | Moderate             |

**Cost of enforcement**: Monthly compensation payments + potential liquidated damages
litigation + labor arbitration costs + court costs.

**Cost of waiver**: 3-month additional compensation (per SPC Art. 9 equivalent). Cleaner
and cheaper than a contested enforcement when the non-compete has validity risks.

### Step 7: Generate Enforceability Classification

Assess the overall clause based on the findings from Steps 4-6. Apply the following
four-tier classification:

| Classification    | Criteria                                                                                                                                                                                                                   | Action Required                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **ENFORCEABLE**   | All four foundational elements valid; compensation adequate; employee eligible; scope proportionate; 2025 access test met                                                                                                  | Monitor payment compliance; advise on waiver mechanics                                                       |
| **AT-RISK**       | One or more elements questionable but not clearly void; compensation borderline adequate; scope arguably overbroad; employee category disputed                                                                             | Identify specific risks; recommend cure actions; assess litigation exposure                                  |
| **NON-COMPLIANT** | Serious deficiency in a mandatory element: inadequate compensation; employer failed to pay 3+ consecutive months; scope clearly disproportionate per 2025 rules                                                            | Immediate remediation required; arbitration risk is high                                                     |
| **VOID**          | Fatal structural defect: employee not in eligible category; employee never accessed trade secrets (2025 rule); duration exceeds 2 years; no compensation whatsoever; tolling provision invalidated by Guiding Case No. 184 | Clause cannot be enforced; waiver is the appropriate strategy; no compensation owed for void clause [VERIFY] |

For each deficiency found, assign a severity level:

| Level        | Description                                                                | Example                                                                                 |
| ------------ | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **CRITICAL** | Renders the clause void by operation of law                                | No trade secret access (2025 rule); no eligible category; duration >2 years             |
| **HIGH**     | Materially compromises enforceability; likely outcome adverse without cure | Compensation < 30% national minimum; employer not paying; scope significantly overbroad |
| **MEDIUM**   | Creates material AT-RISK finding; may be curable                           | Scope arguably broad; compensation adequacy borderline; delivery/signature gap          |
| **LOW**      | Technical or best-practice issue; unlikely to defeat enforcement alone     | No bilingual version; no explicit waiver mechanism; informal compensation notice        |

### Step 8: Apply Quality Assurance Frameworks

#### 8a. Citation Quality Gates

Run silently before delivering output. If any gate fails, revise before delivering.

| Gate           | Rule                                                                                                                                                | Fail Action                                                      |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Source**     | Every legal claim cites LCL Arts. 23-24, SPC Interpretation I/II, or identified case law                                                            | Add citation or mark "[UNVERIFIED]"                              |
| **Format**     | All citations follow Chinese legal citation format: legislation full name + article number; case format (year) Court Level + Min Zhong No. X        | Fix format                                                       |
| **Currency**   | 2025 SPC Interpretation II is applied for post-1 September 2025 analysis; regional rules verified as current                                        | Flag "[CHECK CURRENCY — regional regulations change frequently]" |
| **Domain**     | Analysis stays within Chinese domestic labor law; do not apply foreign law concepts (e.g., blue-pencil doctrine, garden leave as defined in UK law) | Remove or flag jurisdictional bleed                              |
| **Confidence** | Uncertainty about regional rules, unreported cases, or evolving 2025 Interpretation II application explicitly stated                                | Add confidence qualifier                                         |

#### 8b. Self-Interrogation for CRITICAL and HIGH Findings

For any finding classified CRITICAL or HIGH, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the finding follow logically from LCL Art. 23-24
and the applicable SPC Interpretation? Would a Chinese labor arbitration tribunal or
People's Court actually reach this conclusion based on the cited authority?

**Pass 2 — Completeness**: Have all relevant SPC Interpretation provisions been applied?
Has the 2025 SPC Interpretation II access-gating rule been assessed? Have applicable
regional compensation rules been identified?

**Pass 3 — Challenge**: What is the strongest counter-argument an opposing party would
make? Under what factual circumstances might a tribunal find differently? (E.g., for a
"below-threshold compensation" finding: could the employer argue the clause is not void
but merely requires substitution of the 30% rate?)

#### 8c. Confidence Scoring

Apply to each major analytical conclusion:

| Level        | Range     | Meaning                                                  | Action                                       |
| ------------ | --------- | -------------------------------------------------------- | -------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled law; clear statute                               | State with confidence                        |
| **High**     | 0.80-0.94 | Strong authority; minor questions                        | State with brief caveat                      |
| **Probable** | 0.60-0.79 | Good arguments; local practice may differ                | State with reasoning and contra-indicators   |
| **Possible** | 0.40-0.59 | Genuinely uncertain (e.g., unreported regional practice) | Flag for professional review with both sides |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative                                  | Do not assert; flag "[UNCERTAIN]"            |

### Step 9: Deliver Output

Produce the output using the template in the Output Format section below.

Before delivery, verify:

- [ ] All 5 Citation Quality Gates passed
- [ ] CRITICAL and HIGH findings have completed 3-pass Self-Interrogation
- [ ] Each finding has a confidence score
- [ ] Compensation calculation is region-specific (not just national default)
- [ ] 2025 SPC Interpretation II access-gating has been applied
- [ ] Actionable remediation steps provided for every deficiency
- [ ] Employer perspective vs. employee perspective clearly framed if requested

---

## Deep Topic Analysis

### I. The Three-Category Eligibility Rule

Chinese law creates a hard ceiling: only three categories of employees can be validly
bound to post-employment non-competes. This is a mandatory limit that cannot be
contractually expanded.

**Legislative history and purpose**: Articles 23-24 were designed to strike a balance
between employer protection of legitimate business interests (trade secrets, client
relationships, key technology) and employee freedom to work. The PRC legislature
deliberately limited scope to protect ordinary workers from disproportionate restrictions.

**2025 SPC Interpretation II — Access-Gating Rule (Critical)**: As of 1 September 2025,
even a validly categorized employee's non-compete clause is **void** if the employee was
never informed of and never had access to the employer's trade secrets or IP-related
confidential information. This codifies a trend that had developed in Chinese courts
since approximately 2022-2023.

**Practical implication**: Companies must be prepared to document, for each non-compete
signatory:

1. The specific trade secrets or confidential IP information the employee accessed
2. The mechanism by which they were informed (training, system access logs, confidentiality briefings)
3. The factual basis for categorizing them as senior management, senior technical, or
   confidentiality-obligation holder

Courts will no longer accept "they signed the agreement" as sufficient — actual exposure
to protectable information must be evidenced.

### II. Compensation Regime — The Critical Mandatory Element

Unlike many jurisdictions where compensation is optional or negotiable, Chinese law
treats monthly economic compensation during the restriction period as a **mandatory
prerequisite** for enforceability in the post-employment context.

**The 30% national default** comes from the SPC Interpretation's Article 6 equivalent:
if the parties have agreed to a non-compete but the contract is silent on amount, courts
shall award the employee 30% of their average monthly salary for the 12 months
immediately preceding termination, or the applicable local minimum monthly wage,
whichever is higher. This is not a ceiling — it is the floor when the contract is silent.

**Inadequate compensation**: Courts have begun actively invalidating compensation
clauses set at nominal or minimum-wage levels. The Shanghai Second Intermediate People's
Court (2023) invalidated a compensation clause providing only 5.8% of the employee's
actual prior salary and ordered application of the 30% default. The emerging judicial
trend treats deliberately inadequate compensation as bad faith.

**Compensation is ongoing**: Monthly payments must be made throughout the restriction
period. Failure for 3 consecutive months triggers the employee's right to seek release
from the entire non-compete obligation — this is automatic upon tribunal application, not
subject to employer cure.

**Employer's waiver tool**: The most cost-effective way to avoid ongoing compensation
liability is to waive the non-compete at or before the termination date. Post-termination
waiver is permitted but triggers (a) compensation for the gap period plus (b) 3
additional months of compensation.

### III. Geographic and Activity Scope — Proportionality Framework

Chinese non-compete law has no bright-line geographic limits (unlike some US state laws).
Instead, courts apply a proportionality / reasonableness test that considers:

**Geographic proportionality factors:**

- The employer's actual geographic market presence (not registered business scope)
- The employee's geographic exposure in their role
- The nature of the trade secrets (global technology vs. local market knowledge)
- Whether enforcement is practically feasible in the restricted territory

**Activity scope — "genuine competitive relationship" standard:**
China's approach differs from many Western jurisdictions: courts look at actual commercial
activities, customer bases, and market positioning — not what the parties wrote in the
business license registration. Two companies can be in the same "industry" classification
without being genuine competitors.

The _Wang v Wande Information Technology_ [2021 Hu 01 Min Zhong No. 12282] case
illustrates: a financial data analytics company and an entertainment video platform were
both registered as "IT companies." The court conducted a detailed market analysis of
actual products, customers, and competitive dynamics, found no genuine competitive
relationship, and held the employee was not in breach despite joining the second company.

**2025 proportionality rule**: Scope restrictions that exceed what is commensurate with
the specific trade secrets and confidential IP the employee accessed are now expressly
invalid under SPC Interpretation II. This creates a "fit-to-exposure" principle: the
non-compete's coverage must match what the employee actually knew.

### IV. Labor Arbitration — The Mandatory Gateway

**All** non-compete disputes in China must go through labor arbitration before any civil
litigation. This is a mandatory procedural requirement under the Law on Mediation and
Arbitration of Labor Disputes (劳动争议调解仲裁法).

**Process:**

1. Mediation (optional; 15-day window before filing arbitration)
2. Labor Dispute Arbitration Commission (LDAC / 劳动争议仲裁委员会) arbitration
   — filing at the LDAC in the place of employment
   — Typical timeline: 45 days; extendable to 60 days for complex cases
   — Either party may appeal to the People's Court if unsatisfied
3. First-instance civil litigation (基层人民法院 or 中级人民法院 depending on amount)
4. Appellate litigation (中级人民法院 or 高级人民法院)

**Statute of limitations for labor arbitration**: 1 year from the date the party knew
or should have known of the violation (Art. 27 of the Mediation and Arbitration Law).
For continuing breaches, the 1-year period restarts with each month of non-payment.

**Enforcement of arbitration awards**: Labor arbitration awards are directly enforceable
against the respondent. Employers may also seek interim injunctions from courts during
arbitration in clear cases of ongoing competitive activity.

**Key point**: CIETAC and other commercial arbitration bodies are NOT used for domestic
employment disputes — they are used for commercial/M&A non-competes involving sellers
and shareholders, which are governed by commercial contract law.

### V. Employee Breach — Consequences and Litigation Strategy

When an employee violates the non-compete:

**Immediate remedies available to employer:**

- Claim agreed liquidated damages (违约金) — per the contract
- Claim actual losses if they exceed the agreed liquidated damages
- Seek continued performance of the non-compete obligation (even if liquidated damages
  are paid — the SPC Interpretation expressly allows both)
- Potentially join the new employer if it induced the breach

**Liquidated damages calibration:**

- If agreed damages are higher than actual employer losses by more than approximately
  30%, the employee can seek reduction through the tribunal on fairness grounds
- If agreed damages are lower than actual losses, the employer can seek an increase

**Courts have held** (SPC Interpretation Art. 10 equivalent): paying liquidated damages
does NOT buy the employee out of the non-compete obligation. The employer can
simultaneously receive liquidated damages AND obtain a compliance order for the
remaining restriction period.

**New employer liability**: Courts in some cases have held the new employer liable as
a third party if it actively induced the breach (e.g., by offering to indemnify the
employee against liquidated damages, or by knowingly recruiting from a competitor in
violation of the employee's known non-compete). This is an evolving area of law.

### VI. Interaction with Trade Secret Protection (AUCL)

Non-compete and trade secret protection are legally distinct but strategically layered:

| Feature                   | Non-compete (竞业限制)               | Trade secret / NDA (保密义务 + AUCL)                          |
| ------------------------- | ------------------------------------ | ------------------------------------------------------------- |
| **Applicable law**        | LCL Arts. 23-24                      | AUCL Art. 9; employment contract confidentiality provisions   |
| **Who is bound**          | Three eligible categories only       | All employees (implied by employment relationship)            |
| **Duration**              | Maximum 2 years                      | Indefinite (so long as information qualifies as trade secret) |
| **Compensation required** | Yes (post-employment)                | No                                                            |
| **Proof at enforcement**  | Employee working in competitive role | Must show specific disclosure / use of protected information  |
| **Protection purpose**    | Prevents competitive employment      | Prevents information disclosure/use                           |

**Strategic interaction**: Employers should layer both:

- Non-compete provides a per-se restriction without needing to prove disclosure of specific
  trade secrets — simpler to enforce for the 2-year post-departure period
- AUCL trade secret protection continues indefinitely but requires proof of actual
  information theft or misuse
- After the non-compete period expires, AUCL claims remain the primary enforcement
  vehicle if the former employee misuses proprietary information

---

## Severity Classification

**Apply to each deficiency found:**

| Severity                 | Definition                                                                                   | Examples                                                                                                                           |
| ------------------------ | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **CRITICAL — VOID**      | Defect voids the clause by operation of law                                                  | Employee not in eligible category; no trade secret access (2025 rule); duration > 2 years; tolling clause per Guiding Case No. 184 |
| **HIGH — NON-COMPLIANT** | Material defect that seriously undermines enforceability; likely adverse arbitration outcome | Compensation < 30% minimum; employer failed to pay 3+ consecutive months; scope clearly disproportionate to trade secret exposure  |
| **MEDIUM — AT-RISK**     | Significant issue that raises enforceability risk; outcome depends on facts                  | Compensation borderline (e.g., 28%); scope arguably overbroad; employee category classification disputed; delivery/signature gaps  |
| **LOW — ADVISORY**       | Technical or best-practice gap; unlikely to defeat enforcement alone                         | No bilingual version; no explicit waiver mechanism clause; informal payment notification process; no dispute resolution clause     |

---

## Prioritization Framework

| Tier       | Label                  | Timeframe                           | Description                                                                                                                     |
| ---------- | ---------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Tier 1** | Must-Fix / Must-Decide | Immediately (before/at termination) | CRITICAL and HIGH findings that, if unaddressed, create imminent arbitration risk or void the clause                            |
| **Tier 2** | Should-Fix             | 30-60 days                          | MEDIUM findings that create material risk if not remedied; requires clause amendment, compensation adjustment, or documentation |
| **Tier 3** | Best Practice          | 60-180 days                         | LOW advisory findings; improvements to drafting, process, and documentation that reduce future risk                             |

---

## Anti-Patterns

What NOT to do when drafting, enforcing, or advising on Chinese non-competes:

1. **Applying non-competes to all employees without distinction** — Blanket clauses
   covering low-level workers without trade secret access are void under the 2025 SPC
   Interpretation II. Conduct individual access assessments before signing.

2. **Setting compensation at minimum wage or nominal RMB amounts** — Courts treat
   this as bad faith and will substitute the 30% default or invalidate the clause
   entirely. Adequate compensation is a prerequisite, not a formality.

3. **Failing to pay post-departure compensation on time** — Even one missed month
   is a breach; three consecutive missed months gives the employee the right to seek
   full release. Set up automated payroll processes for non-compete compensation before
   the employee's last day.

4. **Failing to waive the non-compete at termination when you don't intend to enforce it**
   — If the employer decides not to enforce but fails to issue a written waiver, monthly
   compensation obligations run until the waiver date plus 3 additional months.

5. **Including duration-extension provisions** (e.g., "time spent in dispute not counted")
   — Void under SPC Guiding Case No. 184 (2022). These clauses are struck out, and
   courts may invalidate surrounding provisions.

6. **Relying solely on business license registration to define competitive activity** —
   Courts apply a functional "genuine competitive relationship" test to actual business
   models, not registered scope. A functional competitor analysis must accompany any
   enforcement action.

7. **Using nationwide or global geographic scope for mid-level employees** — Geographic
   scope must be proportionate to the employee's actual exposure and the geographic reach
   of the trade secrets they held. Overbroad scope is at-risk under 2025 proportionality
   rules.

8. **Ignoring the 2025 SPC Interpretation II access-gating rule** — Post-September
   2025, a non-compete clause is void if the employee cannot be shown to have accessed
   or been informed of trade secrets. Prior signed agreements are not grandfathered —
   the validity test applies at the time of enforcement.

9. **Failing to maintain documentation of trade secret exposure** — If enforcement
   becomes necessary, the employer must prove what trade secrets the employee accessed.
   Absence of system access logs, confidentiality briefing records, or project records
   is a significant evidentiary gap under current law.

10. **Treating Chinese non-competes like US or German ones** — Chinese law has no
    blue-pencil doctrine to save overbroad clauses (courts void the offending provision);
    no "garden leave" concept (garden leave during notice period is not a substitute for
    post-departure compensation); and no at-will employment context (termination grounds
    affect the non-compete trigger analysis).

11. **Assuming the new employer bears no risk** — Chinese courts have increasingly
    looked at whether new employers actively induced breaches. New employers who recruit
    from competitors knowing of a non-compete risk being joined as co-respondents or
    having award liability extended to them.

12. **Drafting the clause in English only** — Chinese courts require Chinese-language
    documents for labor disputes; English-only agreements may be rejected in arbitration.
    Use bilingual format with Chinese as the controlling version.

13. **Using the LDAC in the employer's city rather than the employee's work location** —
    Labor disputes are filed at the LDAC where the employment was performed. Employer-
    biased choice-of-arbitration-forum clauses are not binding in Chinese employment law.

14. **Confusing employment non-competes with M&A seller/shareholder non-competes** —
    M&A non-competes binding shareholders or sellers are governed by commercial contract
    law and the Anti-Monopoly Law, not the LCL. They have different validity rules (up to
    ~3 years is typical; no mandatory compensation to sellers). Applying LCL analysis to
    these clauses is a category error.

15. **Assuming the clause survives an asset acquisition automatically** — In an asset
    acquisition, the employees are not automatically transferred. Existing non-compete
    agreements bind the departing employee vis-à-vis the seller company; the acquirer
    must enter new non-compete agreements with employees it wishes to onboard.

16. **Drafting non-solicitation as a non-compete** — Non-solicitation of customer
    clauses are not expressly regulated under the LCL non-compete framework; courts require
    proof of actual losses to award damages for breach, and liquidated damages for non-
    solicitation without actual losses are frequently not upheld. These are legally distinct.

17. **Setting overly high liquidated damages without proportionality analysis** — Courts
    will reduce agreed liquidated damages that exceed actual employer losses by more than
    approximately 30%, on employee application. Extremely high penalties may actually
    weaken enforcement credibility.

---

## Writing Standards

Before delivering output, apply these quality gates:

- **Precision over breadth**: Every finding must identify the specific clause text at
  issue, the specific legal provision violated, and the specific consequence
- **Bilingual terminology**: Use Chinese legal terms alongside English equivalents for
  key concepts (竞业限制, 经济补偿金, 违约金, 劳动仲裁委员会, etc.)
- **Active voice**: "Article 24 caps the restriction period at 2 years" not "the
  restriction period is capped at 2 years under Article 24"
- **[VERIFY] discipline**: Any legal reference not drawn from the core LCL/SPC framework
  must be marked [VERIFY] — particularly regional regulations and unreported cases
- **Confidence qualified**: Every contested or evolving legal point carries an explicit
  confidence level from the scoring framework
- **No false certainty**: If regional practice is unclear (e.g., Jiangsu or Zhejiang
  compensation floors), state the range and recommend local counsel verification
- **Plain language for business conclusions**: After the legal analysis, one sentence
  per finding stating the business impact in plain terms
- **Structured output**: Never deliver raw narrative — always use the Output Format
  Template below

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for current versions of: Labor Contract Law Arts. 23-24; SPC Interpretation
  (I) 2021 labor dispute provisions; SPC Judicial Interpretation II (Fa Shi [2025] No. 12);
  Shenzhen SEZ Labor Contract Regulations; Shenzhen compensation floor provisions
- Search for recent SPC Guiding Cases on non-compete law (Nos. 179-185, 2022 and onwards)
- Search for recent model cases (最高人民法院典型案例) on non-compete enforcement 2023-2025
- Verify current local minimum wages for Beijing, Shanghai, Guangzhou, Shenzhen, and
  other relevant cities (updated annually — last update December 2025 / January 2026)
- Mark all verified citations with [VERIFIED] in the Glass Box audit trail
- Save research reference to `/tmp/legalcode-cn-noncompete-research.md`

**Without legalcode-mcp:**

- Proceed using LCL Arts. 23-24 and SPC Interpretation framework as documented in this skill
- Mark all statutory and case law references with [VERIFY — not confirmed via legalcode-mcp]
- Recommend that the user verify Shenzhen SEZ compensation floor and any regional
  variations with local counsel
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected — regional rules unverified"`

---

## Glass Box Audit Trail

Every output should include this audit trail, completed with actual values:

```yaml
glass_box:
  skill_name: "legalcode-non-compete-analysis-cn"
  skill_version: "1.0.0 (2026-03-21)"
  governing_law: "Labor Contract Law of the PRC, Arts. 23-24"
  spc_interpretation_applied: "SPC Interpretation I (effective 2021-01-01) + SPC Interpretation II (effective 2025-09-01, Fa Shi [2025] No. 12)"
  employee_work_location: "[city/province identified — determines compensation floor]"
  applicable_compensation_floor: "[30% national / 50% Shenzhen / other regional — specify]"
  employee_category_assessed: "[Category 1 / 2 / 3 / Not eligible]"
  access_gating_rule_applied: "[Yes — 2025 SPC Interp. II / Not applicable — pre-Sept 2025]"
  analysis_mode: "[Employer enforcement / Employee challenge / Pre-hire review / M&A due diligence]"
  overall_classification: "[ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID]"
  legalcode_mcp: "[Connected — citations VERIFIED / Not connected — citations UNVERIFIED]"
  research_reference: "[/tmp/legalcode-cn-noncompete-research.md / Not created]"
  critical_findings: "[number]"
  high_findings: "[number]"
  medium_findings: "[number]"
  low_findings: "[number]"
  compensation_compliant: "[Yes / No / Not assessed]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  confidence_overall: "[DEFINITE / HIGH / PROBABLE / POSSIBLE / UNLIKELY] — [rationale]"
  limitations:
    - "Regional compensation rules (Shenzhen SEZ, Jiangsu, Zhejiang, Beijing) require local verification against current provincial regulations"
    - "SPC Interpretation II (effective September 2025) is applied prospectively; pre-September 2025 agreements are assessed under prior law"
    - "Unreported local court decisions may apply additional standards not captured in national SPC framework"
    - "M&A context non-competes (seller/shareholder) are NOT covered by this skill — require Anti-Monopoly Law analysis"
  reviewer: "AI-assisted analysis — requires review by a qualified Chinese labor lawyer (劳动法律师) before any enforcement, waiver, or litigation decision"
```

---

## Output Format Template

Deliver the final analysis using this structured template:

```markdown
# Chinese Non-Compete Enforceability Analysis (竞业限制分析)

**Skill:** legalcode-non-compete-analysis-cn
**Date of analysis:** [date]
**Employee name / role:** [name/role or REDACTED]
**Work location (city):** [city]
**Applicable compensation floor:** [30% national / 50% Shenzhen / other]
**Perspective:** [Employer / Employee / In-house counsel / M&A due diligence]

---

## Overall Classification

**[ENFORCEABLE / AT-RISK / NON-COMPLIANT / VOID]**

**Confidence:** [Level: Definite / High / Probable / Possible / Unlikely] — [one-sentence rationale]

**Summary:** [2-3 sentences describing the overall enforceability status and the primary factors driving the classification]

---

## Eligibility Assessment (员工资格评估)

| Category                                  | Finding                                        | Confidence               |
| ----------------------------------------- | ---------------------------------------------- | ------------------------ |
| Eligible employee category                | [Category 1/2/3 / Not eligible]                | [High/Probable/Possible] |
| Trade secret access (2025 SPC Interp. II) | [Documented / Not documented / Not applicable] | [High/Probable]          |
| Written form requirement                  | [Met / Not met / Uncertain]                    | [Definite/High]          |

[Narrative analysis of eligibility issues, if any]

---

## Duration Assessment (期限评估)

- **Contractual duration:** [X months]
- **Statutory cap:** 24 months (LCL Art. 24)
- **Status:** [COMPLIANT / NON-COMPLIANT / VOID if > 24 months]
- **Notes:** [Any tolling provisions, guiding case analysis, etc.]

---

## Geographic and Activity Scope (地域和业务范围)

- **Geographic scope stated:** [Description]
- **Geographic proportionality assessment:** [PROPORTIONATE / BORDERLINE / OVERBROAD]
- **Activity scope stated:** [Description]
- **Genuine competitive relationship analysis:** [ESTABLISHED / DISPUTED / NOT ESTABLISHED]
- **2025 proportionality fit:** [PROPORTIONATE to trade secret exposure / EXCEEDS exposure]
- **Severity:** [CRITICAL / HIGH / MEDIUM / LOW]

[Narrative scope analysis, including functional competitive relationship assessment]

---

## Compensation Analysis (经济补偿金分析)

- **Agreed compensation:** [RMB X/month / % of salary / Contract silent]
- **Applicable minimum floor:** [30% national / 50% Shenzhen / other]
- **Employee's prior 12-month average monthly salary:** [RMB X — if known]
- **Minimum required monthly compensation:** [RMB X calculated]
- **Compensation status:** [COMPLIANT / AT-RISK / NON-COMPLIANT / VOID]
- **Payment record:** [Paid on time / Arrears / 3-month non-payment trigger reached]
- **Severity:** [CRITICAL / HIGH / MEDIUM / LOW]

[Narrative compensation analysis]

---

## Findings Summary

| #   | Finding               | Severity                   | Clause/Source      | Priority     |
| --- | --------------------- | -------------------------- | ------------------ | ------------ |
| 1   | [Finding description] | [CRITICAL/HIGH/MEDIUM/LOW] | [Clause reference] | [Tier 1/2/3] |
| ... |                       |                            |                    |              |

---

## Actionable Remediation

### Tier 1 — Immediate Action Required

**Finding [#]: [Title]**

- **Issue:** [Specific deficiency]
- **Legal basis:** [LCL Art. X / SPC Interpretation provision]
- **Risk if unaddressed:** [Specific consequence — e.g., "employee entitled to apply to LDAC for immediate release from non-compete obligation"]
- **Recommended action:** [Specific steps: e.g., "Issue written waiver by [date]; pay accrued compensation of RMB X; prepare waiver letter in Chinese with employee signature confirmation"]
- **Timeline:** [Days/date]

### Tier 2 — Should Address Within 30-60 Days

[Same structure per finding]

### Tier 3 — Best Practice

[Same structure per finding]

---

## Employer vs. Employee Strategy Summary

### If Employer Perspective:

[2-3 bullet points on enforcement/waiver strategy, cost analysis, litigation risk]

### If Employee Perspective:

[2-3 bullet points on enforceability challenge strategy, right to seek release, compensation entitlements]

---

## Interaction with Trade Secret Protection (AUCL)

[Brief assessment of whether AUCL trade secret claims should be layered with or
instead of the non-compete enforcement, based on facts]

---

## Glass Box Audit Trail

[Completed YAML block from the template above]
```

---

## Localization Notes

**Shenzhen SEZ**: Compensation floor of 50% applies specifically to employment relationships
performed in the Shenzhen Special Economic Zone. If an employee works partly in Shenzhen
and partly elsewhere, local counsel should advise on which rule applies. The 50% floor
cannot be contractually undercut, even by mutual agreement.

**Provincial variations**: Jiangsu (approx. 1/3), Zhejiang (approx. 2/3), and Beijing
(court discretion) all have local rules that deviate from the national 30% default.
These rules change — verify current provincial regulations and local court practice
before advising on compensation in these jurisdictions.

**Hong Kong and Macau**: Different legal systems (Hong Kong common law, Macau civil law).
Non-compete analysis for Hong Kong must use UK-derived reasonableness test (protectable
interests; geographic/temporal/activity scope proportionality; blue-pencil power). Do NOT
apply PRC LCL analysis to Hong Kong employment relationships.

**Taiwan**: Separate legal system (ROC civil law). Taiwan Labor Standards Act and specific
non-compete regulations apply. Not covered by this skill.

**Cross-border employees**: An employee who works across the PRC border (e.g., based in
Shenzhen but regularly working in Hong Kong or serving clients regionally) should be
analyzed under the law of their primary place of employment for Chinese law purposes.
The cross-border dimension should be flagged for local counsel.

**Language requirement**: Chinese labor tribunals and courts require documents in Chinese.
Bilingual agreements (Chinese + English) should specify Chinese as the controlling version
(中文版本为准). English-only non-compete agreements are highly unlikely to be enforced
in Chinese labor arbitration.

---

## Provenance

Created by Legalcode (2026-03-21). Legalcode original synthesis based on:

**Primary legal sources:**

- Labor Contract Law of the PRC (中华人民共和国劳动合同法), Arts. 23-24
- SPC Consolidated Judicial Interpretation on Labor Dispute Cases (I), effective 2021-01-01
- SPC Judicial Interpretation II (Fa Shi [2025] No. 12), effective 2025-09-01
- Shenzhen Special Economic Zone Labor Contract Regulations (深圳经济特区劳动合同条例) [VERIFY]
- Law on Mediation and Arbitration of Labor Disputes (劳动争议调解仲裁法), Art. 27
- Anti-Unfair Competition Law of the PRC (反不正当竞争法), 2019 amendment, Art. 9

**Key cases:**

- Wang v Wande Information Technology, (2021) Hu 01 Min Zhong No. 12282 (genuine competitive relationship test)
- SPC Guiding Case No. 184 (July 6, 2022) (tolling provision invalidity)
- Shanghai Second Intermediate People's Court (2023) (minimum wage compensation invalidated)

**Law firm research sources (web-backed research, 2025-2026):**

- Mayer Brown, DLA Piper, Taylor Wessing, Bird & Bird, Morgan Lewis, K&L Gates, Paul Hastings
- China Daily (September 2025 reporting on SPC Interpretation II)
- L&E Global, Law.asia

Routes from: `legalcode-non-compete-analysis` (cross-jurisdictional router).
Structurally informed by: `legalcode-non-compete-analysis-de` and `legalcode-non-compete-analysis-fr`.
