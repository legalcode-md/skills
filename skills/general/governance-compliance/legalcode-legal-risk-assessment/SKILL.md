---
name: legalcode-legal-risk-assessment
description: Assess legal risk across an organization, transaction, product, or initiative — identify
  risks by category (regulatory, contractual, litigation, IP, data privacy, employment, corporate governance),
  score probability and impact, classify severity as CRITICAL / HIGH / MEDIUM / LOW, and produce a confidence-scored,
  auditable risk register with prioritized mitigation strategies. Use when evaluating legal exposure for
  a new product launch, market entry, M&A transaction, regulatory change, contract portfolio, operational
  initiative, or enterprise-wide legal risk review. Jurisdiction-agnostic with localization markers for
  any governing law. Supports risk-appetite playbook or general-standard assessment. Produces a structured
  risk register with Glass Box audit trail.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Legal Risk Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted legal risk identification
> and assessment. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional licensed in the relevant jurisdiction before use. Laws change;
> verify current applicability before relying on any provision described here. Statutory and
> case law references cited from memory carry hallucination risk — verify against
> authoritative sources before relying on them. Risk scores are indicative — they reflect
> structured analysis, not actuarial certainty.

## Purpose and Scope

This skill systematically identifies, scores, classifies, and prioritizes legal risks across
an organization, transaction, product, or initiative. It produces an actionable risk register
with probability-impact scoring, mitigation strategies, and a confidence-scored, auditable
output aligned with ISO 31000:2018 risk management principles.

**Covers:**

- Risk identification across 8 legal risk categories (regulatory, contractual, litigation,
  IP, data privacy, employment, environmental/ESG, corporate governance)
- Probability x Impact scoring with 5x5 heat map methodology
- Severity classification (CRITICAL / HIGH / MEDIUM / LOW) with clear decision rules
- Mitigation strategy recommendations (avoid, mitigate, transfer, accept)
- Multi-jurisdictional risk assessment with [JURISDICTION-SPECIFIC] markers
- Risk-appetite playbook or general-standard assessment
- Quality-verified output with Glass Box audit trail

**Does not:**

- Draft contracts or legal documents (see `legalcode-contract-review` for contract analysis,
  `nda-mutual` for NDA drafting)
- Provide actuarial or quantitative financial risk modeling (Monte Carlo, VaR)
- Replace qualified legal counsel or regulatory advisors
- Perform compliance audits (see jurisdiction-specific compliance skills for detailed audits)
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with localization markers

**Related skills:**

- `legalcode-contract-review` — clause-level contract risk analysis
- `legalcode-nda-triage` — NDA-specific risk screening
- `ccpa-cpra-consumer-rights-operations` — California data privacy compliance
- `ai-act-prohibited-practices-and-literacy-readiness` — EU AI Act compliance
- `litigation-hold-notice` — litigation risk preservation workflow

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The assessment adapts to the jurisdictions relevant
to the subject matter. When a specific governing law applies (e.g., to a contract or
transaction), that jurisdiction's legal framework governs the risk analysis.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- Local regulatory enforcement regimes and penalty structures
- Statute of limitations for relevant claims and causes of action
- Litigation culture and frequency of class actions / group litigation
- Regulatory investigation powers and cooperation obligations
- Data protection regime (GDPR, CCPA/CPRA, LGPD, PIPA, etc.)
- Employment law protections and termination risk
- IP registration and enforcement mechanisms
- Corporate governance and director liability standards
- Whistleblower protection and mandatory reporting obligations
- Anti-corruption and bribery frameworks (FCPA, UK Bribery Act, etc.)
- ESG disclosure and climate-related financial risk requirements
- Cross-border enforcement mechanisms and treaty obligations

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would change the direction or scope of the assessment
- Multiple valid risk frameworks exist and the user's preference matters
- Business context is needed to score probability or impact correctly
- Jurisdictional ambiguity creates a fork that only the user can resolve
- The organization's risk appetite determines whether a risk is acceptable

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

### Step 1: Accept the Assessment Subject

Accept the subject of the legal risk assessment in any of these formats:

- **Document(s)**: Contracts, corporate filings, regulatory submissions, policies
- **Description**: Business initiative, product launch, market entry, transaction overview
- **Specific question**: "What legal risks do we face if we do X?"
- **Portfolio**: Set of contracts, matters, or entities to assess collectively

If the subject is unclear or too broad, prompt the user to narrow the scope.

### Step 2: Gather Context

**CLARIFY** — Before beginning the assessment, ask the user these questions. Present them
as structured options:

1. **What is the scope of this assessment?**
   - Options: Single transaction or agreement, Product or service launch, Market entry
     (new geography), Enterprise-wide legal risk review, Specific regulatory change impact,
     M&A due diligence
   - _Why this matters_: A product launch assessment focuses on regulatory and IP risks;
     an M&A assessment emphasizes contractual and governance risks. Scope determines which
     risk categories to weight most heavily.

2. **Which jurisdictions are relevant?**
   - Options: Single jurisdiction (specify), Multiple jurisdictions (specify), Global
     operations (list primary), Not sure — identify from the materials
   - _Why this matters_: Each jurisdiction has different regulatory regimes, enforcement
     cultures, and penalty structures. A US-only assessment differs fundamentally from a
     multi-jurisdictional one.

3. **What is the organization's risk appetite?**
   - Options: Conservative (risk-averse — flag broadly, lower thresholds),
     Moderate (balanced — standard thresholds), Aggressive (risk-tolerant — flag only
     material items), Let me define specific tolerances
   - _Why this matters_: A regulated financial institution has different risk thresholds
     than a startup. Risk appetite determines whether borderline items are MEDIUM or HIGH.

4. **Industry or sector?**
   - Options: Technology / AI, Financial services, Healthcare / pharma, Manufacturing /
     industrial, Government / public sector, Other (specify)
   - _Why this matters_: Industry determines which risk categories are most relevant and
     which regulatory regimes apply. Healthcare faces HIPAA and FDA risks; fintech faces
     securities and AML risks.

5. **Time horizon?**
   - Options: Immediate (0-6 months), Near-term (6-18 months), Strategic (18+ months),
     Ongoing / recurring assessment
   - _Why this matters_: Regulatory risks that are LOW today may become CRITICAL when a
     new regulation takes effect. Time horizon affects probability scoring.

If the user provides partial context, proceed with reasonable defaults but **state
assumptions explicitly** (e.g., "I'm assuming this is a US-focused technology company
assessment — let me know if that's wrong"). Do not silently assume.

### Step 3: Load the Risk Appetite Playbook

Check for the organization's risk assessment criteria in local settings (e.g.,
`legal.local.md` or similar configuration files).

The risk appetite playbook should define:

- Organizational risk tolerance thresholds by category
- Specific regulatory regimes of concern
- Known risk exposures and accepted risks
- Materiality thresholds (financial, operational, reputational)
- Escalation rules (who reviews HIGH, who reviews CRITICAL)
- Industry-specific risk factors
- Existing mitigation controls and insurance coverage

**If no risk appetite playbook is configured:**

**CLARIFY** — Inform the user that no playbook was found, and ask:

- **Option A: Set up a risk appetite profile now** — Define the organization's risk
  tolerances, materiality thresholds, and key concerns. Takes a few minutes but makes this
  and all future assessments more precise.
- **Option B: Proceed with general standards** — Use the ISO 31000-aligned default criteria
  below. Faster, but may not reflect the organization's specific risk appetite.
- **Option C: I'll provide context as we go** — Start the assessment and I'll ask when the
  organization's position matters.

**Default Standards** (when no playbook is configured):

- Probability scored 1-5 (Very Low to Very High) using objective indicators
- Impact scored 1-5 (Negligible to Severe) across financial, operational, reputational,
  and legal dimensions
- Risk Score = Probability x Impact (range 1-25)
- CRITICAL: 20-25 | HIGH: 12-19 | MEDIUM: 5-11 | LOW: 1-4
- Conservative bias for regulatory and litigation risks (round up when borderline)
- All 8 risk categories assessed unless explicitly scoped out

Clearly label when defaults are being used: "Based on ISO 31000-aligned general standards
— not organizational risk appetite playbook."

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Identify the jurisdiction(s) relevant to the assessment subject.

**CLARIFY** — If any of the following are true, ask the user before proceeding:

- **Multiple conflicting jurisdictions**: Ask which jurisdiction takes priority, or whether
  to assess under all applicable frameworks.
- **Unclear regulatory applicability**: Ask whether a specific regulation applies (e.g.,
  "Does the EU AI Act apply to your product's use in the EU?").
- **Extraterritorial reach**: Flag where a regulation may apply extraterritorially (e.g.,
  GDPR applies to non-EU companies processing EU resident data).

**With legalcode-mcp connected (preferred):**

- Search for jurisdiction-relevant statutes, regulations, and enforcement guidance across
  all applicable risk categories
- Save results to a local temp file (`/tmp/legalcode-risk-assessment-authority.md`)
- Reference verified authority throughout the assessment
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark every statutory and case law reference with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with general legal knowledge, but flag that legal authority has not been
  independently verified
- Focus the assessment on structural risk identification rather than legal certainty

### Step 5: Risk Identification

Systematically evaluate each of the 8 risk categories. For each category, identify
specific risks, assess their current status, and note existing controls.

Read **all provided materials** before scoring — risks interact across categories (e.g.,
a data breach creates simultaneous privacy, litigation, regulatory, and reputational risks).

#### Category 1: Regulatory and Compliance Risk

Risks arising from non-compliance with laws, regulations, and regulatory requirements.

- [ ] **Applicable regulatory regimes identified**: List all regulations that apply to the
      organization's activities in each relevant jurisdiction
- [ ] **Licensing and authorization**: All required licenses, registrations, and
      authorizations are current and in good standing
- [ ] **Reporting obligations**: Mandatory filings, disclosures, and reports are identified
      and current
- [ ] **Regulatory change exposure**: Pending or proposed regulations that could affect
      operations (regulatory horizon scanning)
- [ ] **Enforcement trends**: Recent enforcement actions in the sector that signal
      regulatory priorities
- [ ] **Cross-border compliance**: Where operations span jurisdictions, compliance with
      each applicable regime is addressed
- [ ] **AI and technology regulation**: Applicable AI-specific regulations (EU AI Act,
      state-level AI laws, sector-specific AI guidance)
- [ ] **Anti-corruption and bribery**: FCPA, UK Bribery Act, or local anti-corruption
      regime compliance

[JURISDICTION-SPECIFIC] Regulatory penalty structures vary significantly. The EU AI Act
imposes fines up to EUR 35M or 7% of global turnover for prohibited practices; GDPR up to
EUR 20M or 4% of global turnover; CCPA up to USD 7,500 per intentional violation. Local
enforcement culture (proactive vs. complaint-driven) affects probability scoring. [VERIFY]
current penalty structures and recent enforcement actions for each applicable regime.

#### Category 2: Contractual Risk

Risks arising from contractual obligations, exposures, and counterparty performance.

- [ ] **Material contract obligations**: Key performance, delivery, and milestone
      obligations that create liability exposure
- [ ] **Limitation of liability**: Caps, exclusions, and carveouts across material
      contracts — identify uncapped exposures
- [ ] **Indemnification exposure**: Scope of indemnification obligations (especially
      broad-form, IP, and data breach indemnities)
- [ ] **Warranty obligations**: Express and implied warranties that create performance risk
- [ ] **Termination risk**: Counterparty termination rights, change-of-control triggers,
      and convenience termination exposure
- [ ] **Force majeure and frustration**: Adequacy of force majeure provisions for current
      risk landscape
- [ ] **Assignment and subcontracting**: Restrictions that could affect corporate
      transactions or operational flexibility
- [ ] **Dispute resolution mechanisms**: Arbitration vs. litigation exposure across
      contract portfolio
- [ ] **Key contract dependencies**: Single-supplier risk, essential vendor dependencies

#### Category 3: Litigation Risk

Risks arising from actual, threatened, or potential litigation and dispute exposure.

- [ ] **Active litigation**: Current lawsuits, arbitrations, and regulatory proceedings
- [ ] **Threatened claims**: Demand letters, pre-action correspondence, dispute notices
- [ ] **Potential claims**: Known exposures where no claim has been asserted but risk exists
- [ ] **Class action / group litigation exposure**: Activities or practices that could
      attract collective action
- [ ] **Product liability**: Exposure from products or services that could cause harm
- [ ] **Discovery and legal hold obligations**: Preservation duties triggered by
      anticipated or pending litigation
- [ ] **Statute of limitations exposure**: Claims approaching or within limitation periods
- [ ] **Litigation cost exposure**: Estimated defense costs and potential adverse outcomes

[JURISDICTION-SPECIFIC] Litigation culture varies significantly by jurisdiction. The US has
broader discovery, contingency fee arrangements, and class action mechanisms. The UK has
loser-pays costs rules (Part 36 offers, qualified one-way costs shifting in certain claims).
Civil law jurisdictions have different procedural frameworks. [VERIFY] for each applicable
jurisdiction.

#### Category 4: Intellectual Property Risk

Risks arising from IP creation, protection, enforcement, and third-party claims.

- [ ] **IP portfolio protection**: Key IP assets (patents, trademarks, copyrights, trade
      secrets) are identified and protected
- [ ] **Third-party IP infringement risk**: Products or services that could infringe
      third-party IP rights
- [ ] **Freedom-to-operate**: FTO analysis for key products in target markets
- [ ] **Open-source compliance**: Use of open-source software and compliance with license
      terms (copyleft, attribution, patent grants)
- [ ] **Trade secret protection**: Adequate measures to maintain trade secret status
      (NDAs, access controls, employee agreements)
- [ ] **IP ownership**: Clear ownership of IP created by employees, contractors, and
      collaborators (assignment agreements, work-for-hire)
- [ ] **AI-generated content**: IP rights in AI-generated or AI-assisted output (unsettled
      law in most jurisdictions)
- [ ] **Licensing compliance**: Compliance with inbound IP licenses and restrictions

[JURISDICTION-SPECIFIC] IP protection regimes vary by jurisdiction. Patent scope and
enforcement mechanisms differ (US utility patents vs. European patent system). Trade secret
protection is statutory in some jurisdictions (DTSA in the US, Trade Secrets Directive in
the EU) and common law in others. Work-for-hire doctrine exists in the US but not in most
civil law systems. AI-generated content patentability and copyrightability remain unsettled
globally. [VERIFY] for each relevant jurisdiction.

#### Category 5: Data Privacy and Cybersecurity Risk

Risks arising from personal data processing, data breaches, and cybersecurity obligations.

- [ ] **Data processing lawfulness**: Legal basis for all personal data processing
      activities across jurisdictions
- [ ] **Cross-border data transfers**: Transfer mechanisms (SCCs, adequacy decisions, BCRs)
      for international data flows
- [ ] **Data subject rights compliance**: Processes for handling access, deletion,
      portability, and opt-out requests
- [ ] **Data breach preparedness**: Incident response plan, notification obligations,
      and breach simulation history
- [ ] **Vendor data processing**: Data processing agreements with all processors and
      sub-processors
- [ ] **AI and automated decision-making**: Compliance with restrictions on automated
      decision-making (GDPR Art. 22, AI-specific regulations)
- [ ] **Cybersecurity obligations**: Sector-specific cybersecurity requirements (NIS2,
      CMMC, HIPAA Security Rule)
- [ ] **Data retention and deletion**: Retention schedules and deletion capabilities aligned
      with legal requirements

[JURISDICTION-SPECIFIC] Data privacy regimes differ significantly: GDPR (consent,
legitimate interest, and other bases), CCPA/CPRA (opt-out right for sales/sharing),
Brazil's LGPD, China's PIPL. Breach notification timelines vary: GDPR requires 72-hour
notification; US state breach laws vary from 30 to 90 days. Global average data breach
cost is USD $4.88M (2024). [VERIFY] applicable privacy regimes and notification
requirements.

#### Category 6: Employment and Labor Risk

Risks arising from the employment relationship, workforce management, and labor law
compliance.

- [ ] **Employment classification**: Correct classification of workers as employees vs.
      independent contractors
- [ ] **Discrimination and harassment**: Policies, training, and complaint mechanisms
      to prevent claims
- [ ] **Wage and hour compliance**: Overtime, minimum wage, exempt/non-exempt
      classification compliance
- [ ] **Restrictive covenants**: Enforceability of non-competes, non-solicitation, and
      garden leave provisions
- [ ] **Termination risk**: Wrongful termination exposure, at-will limitations,
      redundancy/layoff process compliance
- [ ] **Workplace safety**: OSHA or equivalent compliance, remote work obligations
- [ ] **AI in employment**: Legal risks from AI-driven hiring, monitoring, performance
      evaluation, and termination decisions
- [ ] **International workforce**: Compliance with local labor law in each jurisdiction
      where employees are located

[JURISDICTION-SPECIFIC] Employment law is heavily jurisdiction-specific. US at-will
employment differs fundamentally from European employment protections. Non-compete
enforceability varies by US state (banned in California, limited in many others) and by
country. Redundancy processes range from at-will termination to mandatory works council
consultation. AI in hiring faces scrutiny under NYC Local Law 144 and emerging regulations.
[VERIFY] for each employment jurisdiction.

#### Category 7: Environmental and ESG Risk

Risks arising from environmental obligations, sustainability commitments, and ESG
disclosure requirements.

- [ ] **Environmental compliance**: Permits, emissions, waste disposal, and contamination
      obligations
- [ ] **ESG disclosure**: Mandatory and voluntary ESG reporting obligations (CSRD, SEC
      climate disclosure, TCFD)
- [ ] **Greenwashing risk**: Marketing claims that could be challenged as misleading
      environmental representations
- [ ] **Climate-related financial risk**: Physical and transition risks from climate change
      affecting operations or assets
- [ ] **Supply chain ESG**: Modern slavery, conflict minerals, deforestation, and supply
      chain due diligence obligations
- [ ] **Sustainability commitments**: Legally binding sustainability targets or pledges
      that create enforceable obligations

[JURISDICTION-SPECIFIC] ESG disclosure requirements are rapidly evolving. EU CSRD requires
detailed sustainability reporting. SEC climate disclosure rules (scope and effective dates
subject to legal challenge). National and sub-national ESG mandates vary widely. [VERIFY]
applicable ESG disclosure obligations for each jurisdiction.

#### Category 8: Corporate Governance Risk

Risks arising from governance structure, director duties, and corporate compliance.

- [ ] **Director and officer liability**: D&O exposure for board decisions, fiduciary
      duty compliance, business judgment rule protection
- [ ] **Board oversight obligations**: Duty to monitor (Caremark duties in US; Companies
      Act 2006 s.174 in UK) for material risks
- [ ] **Shareholder activism and derivative actions**: Exposure to shareholder challenges,
      derivative suits, or activist campaigns
- [ ] **Securities law compliance**: Disclosure obligations, insider trading policies,
      beneficial ownership reporting
- [ ] **Related-party transactions**: Conflicts of interest, related-party transaction
      approval processes
- [ ] **Corporate record-keeping**: Minutes, resolutions, filings, and statutory registers
      maintained and current
- [ ] **M&A and transaction risk**: Due diligence adequacy, representation and warranty
      exposure, post-closing integration risks
- [ ] **Insurance coverage**: D&O, E&O, cyber liability, general liability, and specialty
      coverage adequacy

---

### Step 6: Risk Scoring

For each identified risk, assign a Probability score and an Impact score using the
following scales:

#### Probability Scale

| Score | Level         | Indicators                                                                                                            |
| ----- | ------------- | --------------------------------------------------------------------------------------------------------------------- |
| 1     | **Very Low**  | No history of occurrence; strong preventive controls in place; regulatory environment stable                          |
| 2     | **Low**       | Rare occurrence in industry; adequate controls exist; minor regulatory attention                                      |
| 3     | **Medium**    | Occasional occurrence in industry; controls exist but have gaps; regulatory scrutiny increasing                       |
| 4     | **High**      | Regular occurrence in industry; known control weaknesses; active regulatory focus                                     |
| 5     | **Very High** | Near-certain occurrence; inadequate controls; enforcement actions against peers; new regulation imminent or in effect |

#### Impact Scale

| Score | Level           | Financial      | Operational                                   | Reputational                                | Legal                                                            |
| ----- | --------------- | -------------- | --------------------------------------------- | ------------------------------------------- | ---------------------------------------------------------------- |
| 1     | **Negligible**  | < 0.1% revenue | No disruption                                 | No media attention                          | Minimal legal exposure                                           |
| 2     | **Some**        | 0.1-1% revenue | Minor disruption, recoverable                 | Local media coverage                        | Moderate legal costs, settled quickly                            |
| 3     | **Moderate**    | 1-5% revenue   | Significant disruption, 1-3 month recovery    | National media coverage                     | Substantial litigation, uncertain outcome                        |
| 4     | **Significant** | 5-15% revenue  | Major disruption, 3-12 month recovery         | Sustained negative coverage, customer churn | Major litigation or regulatory action, material loss likely      |
| 5     | **Severe**      | > 15% revenue  | Existential disruption, business unit failure | Crisis-level coverage, leadership changes   | Existential litigation, criminal exposure, or license revocation |

#### Risk Score Matrix (Probability x Impact)

```
Impact →    1         2         3         4         5
Prob ↓   Negligible  Some     Moderate  Significant  Severe
  5       5 [M]     10 [M]    15 [H]    20 [C]      25 [C]
  4       4 [L]      8 [M]    12 [H]    16 [H]      20 [C]
  3       3 [L]      6 [M]     9 [M]    12 [H]      15 [H]
  2       2 [L]      4 [L]     6 [M]     8 [M]      10 [M]
  1       1 [L]      2 [L]     3 [L]     4 [L]       5 [M]

[C] = CRITICAL (20-25)  [H] = HIGH (12-19)  [M] = MEDIUM (5-11)  [L] = LOW (1-4)
```

**Scoring rules:**

- Score Probability and Impact independently before multiplying
- When evidence supports two adjacent scores, choose the higher one for conservative risk
  appetite, lower for aggressive risk appetite, and state the rationale
- A risk with Probability 1 but Impact 5 is still MEDIUM — low-probability catastrophic
  risks require monitoring
- Consider time horizon: a risk that is LOW today but will become HIGH in 12 months should
  be flagged with a time-based escalation note
- Aggregate risks: multiple MEDIUM risks in the same category may warrant a HIGH category
  rating if they interact or compound

### Step 7: Risk Classification

Based on the risk scores, assign a severity classification using the rules below:

#### CRITICAL (Score 20-25) — Immediate Action Required

**Any** of the following:

- Risk score 20-25 on the probability-impact matrix
- Active regulatory investigation or enforcement proceeding
- Existential litigation or credible threat of criminal prosecution
- Regulatory non-compliance where the regulation is already in effect and penalties are
  material (> 5% revenue or operational license at risk)
- Active data breach with notification obligations triggered
- Known violation of law that has not been remediated

**Confidence required**: HIGH (0.80+) — Confident the risk is material and imminent.

**Action**: Board-level or C-suite escalation. Immediate remediation plan. Engage external
counsel. Consider voluntary disclosure if regulatory matter.

#### HIGH (Score 12-19) — Active Management Required

**One or more** of the following:

- Risk score 12-19 on the probability-impact matrix
- Regulatory change that will materially affect operations within 12 months
- Contract portfolio with material uncapped liability exposure
- Pending litigation with adverse outcome probability > 50%
- IP infringement risk for a revenue-critical product
- Data privacy non-compliance in a jurisdiction with active enforcement
- Employment practices with significant class action exposure

**Confidence required**: PROBABLE (0.60+) — Strong basis but reasonable minds could differ
on severity.

**Action**: Assign risk owner. Develop mitigation plan with timeline. Regular reporting to
legal leadership. Budget for remediation or litigation reserves.

#### MEDIUM (Score 5-11) — Monitoring and Managed Controls

**One or more** of the following:

- Risk score 5-11 on the probability-impact matrix
- Regulatory change that may affect operations beyond 12 months
- Contractual provisions that deviate from preferred terms but do not create material
  exposure
- Potential litigation where exposure is manageable and probability is moderate
- IP portfolio gaps that do not affect current products but could affect future plans
- Data privacy practices that are compliant but could be strengthened

**Confidence required**: PROBABLE (0.60+) — Issues identified but could be wrong about
probability or impact.

**Action**: Monitor with periodic review. Include in regular risk reporting. Strengthen
controls as resources allow. Track regulatory developments.

#### LOW (Score 1-4) — Accept and Monitor

**All** of the following:

- Risk score 1-4 on the probability-impact matrix
- No current regulatory attention or enforcement trends
- Adequate controls in place
- Exposure is manageable within existing resources and insurance coverage

**Confidence required**: HIGH (0.80+) — Confident the risk is genuinely low, not just
under-analyzed.

**Action**: Accept the risk. Include in risk register for completeness. Review annually
or when triggered by a material change.

### Step 8: Mitigation Strategy Development

For each CRITICAL and HIGH risk, and optionally for MEDIUM risks, recommend a mitigation
strategy using the ISO 31000 treatment framework:

#### Treatment Options

| Strategy     | Description                                        | When to Use                                                  | Examples                                                               |
| ------------ | -------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------- |
| **Avoid**    | Eliminate the activity that creates the risk       | Intolerable risk with no business justification              | Exit a market, discontinue a product feature, decline a transaction    |
| **Mitigate** | Implement controls to reduce probability or impact | Most common; cost-effective controls available               | Strengthen compliance program, amend contracts, implement training     |
| **Transfer** | Shift risk to a third party                        | Risk is quantifiable; insurance or indemnification available | Purchase insurance, negotiate indemnification, outsource to specialist |
| **Accept**   | Acknowledge and monitor the residual risk          | Low residual risk; mitigation cost exceeds benefit           | Document acceptance rationale, set review triggers                     |

**For each risk requiring treatment, provide:**

- **Recommended strategy**: Which treatment option and why
- **Specific actions**: Concrete steps to implement (not generic advice)
- **Timeline**: When each action should be completed
- **Responsible party**: Who should own the mitigation (role, not name)
- **Cost estimate**: Qualitative (low / medium / high) or quantitative if possible
- **Residual risk**: Expected severity after mitigation is implemented
- **Monitoring**: How to track effectiveness of the mitigation

#### Mitigation Priority Framework

| Priority   | Category   | Criteria                                                      | Timeline                  |
| ---------- | ---------- | ------------------------------------------------------------- | ------------------------- |
| **Tier 1** | Must-Do    | CRITICAL risks; active violations; regulatory deadlines       | Immediate (0-30 days)     |
| **Tier 2** | Should-Do  | HIGH risks; material exposures; approaching deadlines         | Near-term (30-90 days)    |
| **Tier 3** | Plan-To-Do | MEDIUM risks with upward trajectory; strategic risk reduction | Medium-term (90-180 days) |
| **Tier 4** | Monitor    | LOW risks; accepted risks; risks with adequate controls       | Ongoing (annual review)   |

### Step 9: Interactions and Compound Risk Analysis

After scoring individual risks, analyze how risks interact:

- **Cascade risks**: Where one risk event triggers others (e.g., data breach → litigation →
  regulatory investigation → reputational harm → customer churn)
- **Compound risks**: Where multiple moderate risks in the same area create elevated
  aggregate exposure
- **Correlation**: Where risks share common root causes that could be addressed together
- **Offsetting controls**: Where mitigation of one risk also reduces another
- **Regulatory pile-up**: Where multiple regulatory regimes create overlapping or
  conflicting obligations for the same activity

For any compound risk that would score higher than the sum of its parts, flag it separately
with a compound risk score and specific analysis.

### Step 10: Quality Verification

Before delivering the risk assessment, run the quality checks:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every CRITICAL-classified risk, run the 3-pass Self-Interrogation. Revise if any
   pass reveals a weakness.
3. Assign a Confidence Score to the overall assessment and to each material risk.
4. Verify completeness: confirm all 8 risk categories have been addressed (or explicitly
   scoped out with stated rationale).
5. Generate the Glass Box Audit Trail and append it to the output.
6. Run the Writing Standards quality gates.
7. Verify that mitigation strategies are specific and actionable (not generic advice).
8. Confirm that the risk heat map is internally consistent (no scoring contradictions).

### Step 11: Delivery and Next Steps

Based on the assessment results, provide a structured deliverable with clear next steps:

| Overall Risk Profile     | Recommended Action                               | Typical Follow-Up                                                               |
| ------------------------ | ------------------------------------------------ | ------------------------------------------------------------------------------- |
| Predominantly LOW/MEDIUM | Accept with monitoring plan; annual reassessment | Integrate into regular risk reporting                                           |
| Mixed with HIGH items    | Active mitigation program; quarterly review      | Engage counsel on HIGH items; budget for remediation                            |
| Any CRITICAL items       | Immediate escalation and remediation             | Board briefing; external counsel engagement; voluntary disclosure consideration |

For the delivery:

- Lead with the executive summary and risk heat map
- Provide the full risk register for detailed reference
- Include specific, time-bound action items for each risk requiring treatment
- Identify the appropriate escalation path for CRITICAL and HIGH risks
- Recommend a reassessment cadence based on the risk profile and industry dynamics

---

## Severity / Status Classification

| Risk Level   | Score Range | Meaning                                                  | Action                                                        |
| ------------ | ----------- | -------------------------------------------------------- | ------------------------------------------------------------- |
| **CRITICAL** | 20-25       | Immediate, material threat requiring executive attention | Escalate immediately; remediate; engage external counsel      |
| **HIGH**     | 12-19       | Active management required; material exposure            | Assign risk owner; develop mitigation plan; regular reporting |
| **MEDIUM**   | 5-11        | Managed through standard controls and monitoring         | Monitor; include in risk reporting; strengthen controls       |
| **LOW**      | 1-4         | Acceptable risk with adequate controls                   | Accept and monitor; annual review                             |

---

## Prioritization Framework Summary

| Priority   | Category   | Criteria                                                 | Timeline      | Owner                         |
| ---------- | ---------- | -------------------------------------------------------- | ------------- | ----------------------------- |
| **Tier 1** | Must-Do    | CRITICAL risks, active violations, regulatory deadlines  | 0-30 days     | C-suite / General Counsel     |
| **Tier 2** | Should-Do  | HIGH risks, material exposures, approaching deadlines    | 30-90 days    | Legal leadership / Risk owner |
| **Tier 3** | Plan-To-Do | MEDIUM risks with upward trend, strategic risk reduction | 90-180 days   | Legal team / Business unit    |
| **Tier 4** | Monitor    | LOW risks, accepted risks, adequate controls in place    | Annual review | Risk register owner           |

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Identify the assessment scope, jurisdictions, industry context, and risk appetite.
Determine whether a risk appetite playbook exists. Assess whether special considerations
apply (M&A context, regulatory change, market entry, crisis response).

**DO**: Execute the 8-category risk identification. Score probability and impact. Classify
CRITICAL/HIGH/MEDIUM/LOW. Develop mitigation strategies. Analyze compound risks.

**CHECK**: Run the Citation Quality Gates. Verify legal claims in the risk rationale. For
CRITICAL classifications, run the Self-Interrogation. Confirm all 8 categories addressed.
Verify scoring consistency across the assessment.

**ACT**: If the assessment reveals systemic risk patterns, recommend structural changes
(governance, compliance program, insurance coverage, contract standards). If the
organization's risk appetite needs recalibration, flag for leadership discussion.

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                    | Fail Action                                              |
| -------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established principle                                        | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction                                             | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments or repeal against authoritative sources where accessible                   | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the applicable jurisdiction's legal framework. No assumptions from other jurisdictions leaking in | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden. If uncertain, say so                                                         | Add confidence qualifier                                 |

### Self-Interrogation for CRITICAL Items

For any risk classified as CRITICAL, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the
cited authority? Is the regulatory or legal basis actually applicable to this organization's
activities in this jurisdiction? Is the probability score supported by objective evidence
(enforcement trends, peer actions, regulatory signals)?

**Pass 2 — Completeness**: Have all relevant statutes, regulations, and principles been
considered? Are there regulatory dimensions not yet addressed? Could other risks in the
register interact with this one to mitigate or worsen it?

**Pass 3 — Challenge**: What is the strongest argument that this risk is actually HIGH
rather than CRITICAL? Under what circumstances might a reasonable legal professional accept
this risk? Is the CRITICAL classification proportionate, or is this actually HIGH with
a strong mitigation plan? Would general counsel at a leading company in this sector treat
this as a board-level issue?

If any pass reveals a weakness, revise the analysis before delivery. Mark the audit trail
with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For the overall assessment and each material risk, assign a confidence level:

| Level        | Range     | Meaning                                                      | Action                                                |
| ------------ | --------- | ------------------------------------------------------------ | ----------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled law, clear regulatory requirement, no ambiguity      | State with confidence                                 |
| **High**     | 0.80-0.94 | Strong basis, minor interpretation questions                 | State with brief caveat                               |
| **Probable** | 0.60-0.79 | Good arguments but reasonable minds could differ             | State with reasoning and contra-indicators            |
| **Possible** | 0.40-0.59 | Genuinely uncertain, evolving law, competing interpretations | Flag for counsel review with both sides               |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative                                      | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every risk assessment output MUST include a Glass Box audit section at the end:

```yaml
glass_box:
  assessment_subject: "[Subject description]"
  scope: "[Single transaction / Product launch / Enterprise-wide / etc.]"
  jurisdictions: "[List of jurisdictions assessed]"
  industry: "[Industry / sector]"
  time_horizon: "[Immediate / Near-term / Strategic / Ongoing]"
  risk_appetite: "[Conservative / Moderate / Aggressive / Playbook-defined]"
  review_basis: "[Organizational playbook / ISO 31000-aligned general standards]"
  categories_assessed: 8
  category_summary:
    regulatory_compliance: "[CRITICAL/HIGH/MEDIUM/LOW] — [top risk brief]"
    contractual: "[CRITICAL/HIGH/MEDIUM/LOW] — [top risk brief]"
    litigation: "[CRITICAL/HIGH/MEDIUM/LOW] — [top risk brief]"
    intellectual_property: "[CRITICAL/HIGH/MEDIUM/LOW] — [top risk brief]"
    data_privacy: "[CRITICAL/HIGH/MEDIUM/LOW] — [top risk brief]"
    employment: "[CRITICAL/HIGH/MEDIUM/LOW] — [top risk brief]"
    environmental_esg: "[CRITICAL/HIGH/MEDIUM/LOW] — [top risk brief]"
    corporate_governance: "[CRITICAL/HIGH/MEDIUM/LOW] — [top risk brief]"
  total_risks_identified: "[number]"
  risk_distribution:
    critical: "[number]"
    high: "[number]"
    medium: "[number]"
    low: "[number]"
  compound_risks_flagged: "[number]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to temp file or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL items)"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified legal review"
```

---

## Anti-Patterns

What NOT to do in legal risk assessment:

1. **Scoring everything as MEDIUM "to be safe"** — If every risk is MEDIUM, the assessment
   provides no prioritization value. CRITICAL means CRITICAL — escalate immediately. LOW
   means LOW — accept and move on. The purpose of risk assessment is to differentiate, not
   to hedge.

2. **Conflating probability with impact** — A risk with Very High probability but Negligible
   impact (Score 5) is not HIGH — it is MEDIUM. A risk with Very Low probability but Severe
   impact (Score 5) is also MEDIUM but demands a different response (monitoring vs. insurance).
   Score each dimension independently.

3. **Assessing risks in isolation** — A data privacy risk, a cybersecurity risk, and a
   contractual risk may all stem from the same underlying issue (inadequate vendor management).
   The compound risk is greater than the sum of parts. Always analyze interactions in Step 9.

4. **Ignoring the time dimension** — A regulatory risk that is LOW today because the
   regulation takes effect in 18 months will be CRITICAL in 17 months if no preparation has
   started. Score for the assessment time horizon, and flag time-based escalations.

5. **Generic mitigation recommendations** — "Strengthen compliance program" is not
   actionable. "Appoint a DPO, complete Article 30 records of processing, and implement
   consent management for marketing cookies by Q3 2026" is actionable. Every mitigation must
   be specific enough to assign to a person and track to completion.

6. **Applying one jurisdiction's framework universally** — US employment law assumptions
   do not apply in the EU. GDPR concepts do not map directly to CCPA. Common law tort
   principles differ from civil law delict. Always check whether a legal concept applies
   under the relevant jurisdiction's framework.

7. **Risk identification without materiality assessment** — Every organization faces
   hundreds of theoretical legal risks. The purpose of assessment is to identify which risks
   are material for this specific organization. An AI startup does not have the same risk
   profile as a pharmaceutical company. Filter for relevance.

8. **Treating risk assessment as a one-time exercise** — Legal risk is dynamic. Regulations
   change, litigation develops, markets shift. A risk assessment is a snapshot. Always
   recommend a reassessment cadence and identify trigger events for ad hoc reassessment.

9. **Citing statutes from memory without verification** — Statutes are amended, repealed,
   and renumbered. Regulatory guidance is updated. Enforcement trends shift. If you cannot
   verify a citation against an authoritative source, mark it [VERIFY] or "[UNVERIFIED —
   counsel to confirm]." Never present an unverified citation as settled law.

10. **Underweighting reputational risk** — Legal risk assessment often focuses on financial
    exposure and regulatory penalties. But reputational harm from a data breach, a workplace
    scandal, or an environmental incident can exceed the direct legal costs by orders of
    magnitude. Include reputational impact in the Impact scoring.

11. **Ignoring existing controls and insurance** — A risk with high inherent severity may
    have low residual severity because of existing controls, contractual protections, or
    insurance coverage. Always assess both inherent and residual risk. An insured risk is
    still a risk, but the residual financial impact is different.

12. **Over-engineering the output** — A risk assessment for a single product launch does
    not need the same depth as an enterprise-wide annual review. Match the assessment depth
    to the scope. A focused assessment should be concise and actionable, not exhaustive.

13. **Failing to identify the risk owner** — Every CRITICAL and HIGH risk must have a clear
    owner (role or function). An unowned risk is an unmanaged risk. If the owner is unclear,
    flag it as a finding — that itself is a governance risk.

14. **Treating accepted risks as resolved** — Risk acceptance is a deliberate decision, not
    the absence of action. Accepted risks must be documented with rationale, reviewed
    periodically, and have trigger conditions for re-evaluation.

---

## Writing Standards

Apply plain-language discipline to all assessment output:

**For the risk register**:

- Plain language. No jargon or filler.
- Active voice: "The organization processes EU resident data without a DPA" not "It was
  identified that data processing activities may not fully comply"
- Short sentences. One point per sentence.
- Name the source: cite the specific regulation, contract clause, or factual basis for
  each risk
- Specific, not vague: "Appoint a DPO by Q3 2026 to comply with GDPR Art. 37" not
  "consider data protection improvements"

**For each risk entry**:

- State what the risk is (factual basis and legal framework)
- State the probability assessment with supporting evidence
- State the impact assessment across relevant dimensions
- State the recommended mitigation (specific actions, timeline, owner)

**Quality gates before delivery**:

1. Is the overall risk profile (CRITICAL/HIGH/MEDIUM/LOW distribution) clearly stated at
   the top?
2. Is every risk supported by a specific legal basis or factual foundation?
3. Can the reader understand and act on the mitigation recommendations without further
   research?
4. Are legal claims in the rationale backed by authority (or flagged [VERIFY])?
5. Is the assessment appropriately scoped (not too broad for the subject, not too narrow)?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.
legalcode-mcp is a law, regulatory, and case law database with powerful search across
jurisdictions.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for jurisdiction-relevant statutes, regulations, and enforcement
  guidance across all applicable risk categories
- Save the most relevant results to `/tmp/legalcode-risk-assessment-authority.md`
- Reference verified authority throughout the assessment
- For CRITICAL items, search for additional case law and enforcement actions to support
  or challenge the classification
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Include a notice that legal citations require independent verification
- Focus the assessment on structural risk identification and commercial risk analysis

---

## Output Format Template

Structure the risk assessment deliverable as:

```markdown
## Legal Risk Assessment Report

**Assessment Subject**: [subject description]
**Scope**: [single transaction / product launch / enterprise-wide / etc.]
**Jurisdictions**: [list]
**Industry**: [sector]
**Risk Appetite**: [conservative / moderate / aggressive]
**Review Basis**: [Organizational Playbook / ISO 31000-Aligned General Standards]
**Time Horizon**: [immediate / near-term / strategic / ongoing]
**Date**: [date]

---

## Executive Summary

**Overall Risk Profile**: [CRITICAL / HIGH / MEDIUM / LOW — based on highest-severity risk]
**Confidence**: [level with numeric range]

**Risk Distribution**:

- CRITICAL: [count] — [brief description of top critical risk]
- HIGH: [count] — [brief description of top high risk]
- MEDIUM: [count]
- LOW: [count]

**Top 3 Risks Requiring Immediate Attention**:

1. [Risk name — Category — Score — One-line description]
2. [Risk name — Category — Score — One-line description]
3. [Risk name — Category — Score — One-line description]

**Key Recommendation**: [One paragraph summary of the most important action to take]

---

## Risk Heat Map

|                   | Negligible (1) | Some (2) | Moderate (3) | Significant (4) | Severe (5) |
| ----------------- | -------------- | -------- | ------------ | --------------- | ---------- |
| **Very High (5)** | [risks]        | [risks]  | [risks]      | [risks]         | [risks]    |
| **High (4)**      | [risks]        | [risks]  | [risks]      | [risks]         | [risks]    |
| **Medium (3)**    | [risks]        | [risks]  | [risks]      | [risks]         | [risks]    |
| **Low (2)**       | [risks]        | [risks]  | [risks]      | [risks]         | [risks]    |
| **Very Low (1)**  | [risks]        | [risks]  | [risks]      | [risks]         | [risks]    |

---

## Risk Register

### [Risk ID] — [Risk Name] | [Category] | [CRITICAL/HIGH/MEDIUM/LOW]

**Score**: Probability [X] x Impact [X] = [Score]
**Risk description**: [What the risk is — factual basis and legal framework]
**Legal basis**: [statute/regulation/principle — or "[VERIFY]"]
**Probability rationale**: [Why this probability score — evidence, enforcement trends, etc.]
**Impact rationale**: [Why this impact score — financial, operational, reputational, legal]
**Existing controls**: [What is already in place to manage this risk]
**Mitigation strategy**: [Avoid / Mitigate / Transfer / Accept]
**Specific actions**:

1. [Action — responsible party — timeline]
2. [Action — responsible party — timeline]
   **Residual risk after mitigation**: [Expected severity level]
   **Confidence**: [level]
   **Time sensitivity**: [Immediate / Near-term / Strategic / Stable]

[Repeat for each risk, ordered by severity (CRITICAL first, then HIGH, MEDIUM, LOW)]

---

## Compound Risk Analysis

### [Compound Risk Name]

**Contributing risks**: [Risk IDs that interact]
**Compound effect**: [How the risks interact to create elevated exposure]
**Compound score**: [Adjusted score accounting for interaction]
**Mitigation**: [How addressing the root cause reduces multiple risks]

---

## Mitigation Roadmap

### Tier 1 — Must-Do (0-30 days)

1. [Action item — risk addressed — owner — deadline]

### Tier 2 — Should-Do (30-90 days)

1. [Action item — risk addressed — owner — deadline]

### Tier 3 — Plan-To-Do (90-180 days)

1. [Action item — risk addressed — owner — deadline]

### Tier 4 — Monitor (Ongoing)

1. [Risk to monitor — trigger for re-evaluation — review cadence]

---

## Next Steps

1. [Action item 1]
2. [Action item 2]
3. [Action item 3]

**Recommended reassessment cadence**: [Quarterly / Semi-annual / Annual / Trigger-based]
**Trigger events for ad hoc reassessment**: [List of events that should prompt reassessment]

---

## Glass Box Audit Trail

[YAML block per Glass Box section above]
```

---

## Localization Notes

This skill is jurisdiction-agnostic by design. To create a jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with jurisdiction-specific legal content
2. Replace [VERIFY] tags with verified statutory references
3. Add jurisdiction-specific risk factors and regulatory regimes
4. Adjust probability scoring for local enforcement culture and litigation frequency
5. Add jurisdiction-specific anti-patterns
6. Update the frontmatter name and description to reference the specific jurisdiction
7. Add relevant case law citations and enforcement action examples

Localization Checklist:

- [ ] Identify all applicable regulatory regimes for the jurisdiction
- [ ] Verify penalty structures and enforcement mechanisms
- [ ] Assess litigation culture (class action availability, costs rules, discovery scope)
- [ ] Check employment law framework (at-will vs. protected, works council requirements)
- [ ] Verify data protection regime and breach notification requirements
- [ ] Assess IP protection mechanisms (patent system, trade secret regime)
- [ ] Check corporate governance framework (director duties, fiduciary standards)
- [ ] Identify ESG disclosure obligations
- [ ] Add local legal terminology alongside English translations (if non-English
      jurisdiction)

---

## Provenance

Created by Legalcode (2026-02-27). Original synthesis combining:

- **ISO 31000:2018** risk management framework — probability-impact methodology, treatment
  options (avoid, mitigate, transfer, accept), PDCA cycle
- **COSO ERM Framework** — enterprise risk management structure and governance integration
- **Legalcode reference skills** (`legalcode-contract-review`, `legalcode-nda-triage`) —
  quality assurance frameworks (Glass Box, Citation Quality Gates, Self-Interrogation,
  Confidence Scoring), interactive CLARIFY patterns, playbook architecture, writing
  standards, anti-patterns methodology
- **Industry research** (2025-2026) — Gartner emerging risk surveys, Protiviti legal top
  risks, MetricStream legal risk frameworks, Wolters Kluwer risk management best practices

Enhanced with: 8-category legal risk taxonomy, 5x5 probability-impact scoring matrix,
compound risk analysis, time-horizon awareness, mitigation roadmap with tiered prioritization,
and jurisdiction-agnostic architecture with localization support.
