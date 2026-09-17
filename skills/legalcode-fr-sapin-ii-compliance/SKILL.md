---
name: legalcode-fr-sapin-ii-compliance
description: 'Assess an organization''s anti-corruption compliance program against France''s Loi Sapin
  II (Loi n° 2016-1691 du 9 décembre 2016) and its Loi Waserman (2022) whistleblower amendments. Covers
  all eight Article 17 pillars: code of conduct, internal whistleblowing system, risk mapping, third-party
  due diligence, accounting controls, training, disciplinary sanctions, and monitoring. Also assesses
  AFA (Agence Française Anticorruption) control readiness, Commission des Sanctions exposure, CJIP risk,
  and interaction with the Loi de Vigilance and international anti-bribery regimes (FCPA, UK Bribery Act).
  Use when auditing a Sapin II compliance program, preparing for an AFA control, conducting M&A anti-corruption
  due diligence in France, or advising a multinational group on group-wide Sapin II rollout. France-specific
  skill with extraterritorial reach analysis for French parent company groups.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode — Sapin II Compliance Assessment (France)

> **Disclaimer**: This skill provides a framework for AI-assisted anti-corruption compliance
> assessment under France's Loi Sapin II. It does not constitute legal advice. All outputs
> should be reviewed by a qualified French legal professional (avocat) or certified compliance
> officer before use. Laws, AFA recommendations, and enforcement guidance change; verify
> current applicability before relying on any provision described here. Statutory and
> regulatory references carry hallucination risk — verify against authoritative sources
> (Légifrance, AFA official publications) before relying on them. This skill does not assess
> criminal corruption exposure — for criminal risk, engage the Parquet National Financier (PNF)
> specialists.

---

## Purpose and Scope

This skill assesses an organization's anti-corruption compliance program against the requirements
of Loi Sapin II (Loi n° 2016-1691 du 9 décembre 2016 relative à la transparence, à la lutte
contre la corruption et à la modernisation de la vie économique), as amended by Loi Waserman
(Loi n° 2022-401 du 21 mars 2022).

**Covers:**

- Applicability determination (500-employee / €100M threshold analysis for French entities and
  group structures)
- All eight Article 17 pillars of the mandatory anti-corruption program
- Whistleblower system assessment under Loi Waserman reforms (effective 1 September 2022)
- AFA control readiness assessment
- Commission des Sanctions exposure analysis
- CJIP (Convention Judiciaire d'Intérêt Public) risk profiling
- Interaction with Loi de Vigilance (corporate duty of care), FCPA, and UK Bribery Act
- M&A anti-corruption due diligence (target assessment framework)
- Group structure compliance: parent company obligations for subsidiaries

**Does not:**

- Investigate actual corruption or provide criminal defense advice
- Replace an AFA-accredited compliance review or auditor opinion
- Cover the Loi de Vigilance (human rights/environmental duty of care) in full — for that,
  use a dedicated Loi de Vigilance skill
- Provide advice on pending criminal proceedings before the PNF

---

## Jurisdiction and Governing Law

**Primary Jurisdiction**: France (République Française)

**Governing Statute**: Loi n° 2016-1691 du 9 décembre 2016, Title III (Articles 1-18),
as amended by Loi n° 2022-401 du 21 mars 2022 [VERIFY current consolidated version on Légifrance]

**Regulatory Authority**: Agence Française Anticorruption (AFA) — established by Article 1
of Sapin II, placed under the joint authority of the Minister of Justice and the Minister
for the Budget. AFA publishes binding recommendations (dernière version: January 12, 2021)
and sector-specific practical guides. [VERIFY: check AFA website for guidance updated since
January 2021]

**Sanctions Authority**: Commission des Sanctions — independent 6-member body within AFA.
Operates with prosecutorial separation (AFA inspection teams cannot vote on sanctions).

**Territorial Reach**:

| Entity Type                         | Sapin II Applies?    | Conditions                                                     |
| ----------------------------------- | -------------------- | -------------------------------------------------------------- |
| French-registered company           | Yes                  | If ≥500 employees AND >€100M turnover (consolidated)           |
| French subsidiary of foreign parent | Yes                  | If subsidiary individually meets 500/€100M                     |
| Foreign subsidiary of French parent | Yes                  | French parent must extend compliance program group-wide        |
| Foreign company, no French parent   | Generally no         | Unless individually meets thresholds in France                 |
| SME below thresholds                | No direct obligation | May face indirect requirements as supplier to covered entities |

> [VERIFY] A proposed legislative amendment (status uncertain as of 2026) would extend Sapin II
> obligations to foreign parent companies of French subsidiaries where the global group exceeds
> 500/€100M thresholds. Monitor Légifrance for legislative updates.

**International Overlay**:
Sapin II-covered entities active internationally may also face concurrent obligations under:

- **US FCPA** (any USD transaction, US-listed company, or conduct involving US persons)
- **UK Bribery Act 2010** (any entity carrying on business in the UK)
- **OECD Anti-Bribery Convention** (binding on France; Sapin II was France's Phase 4 OECD response)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
organizational context, the workflow pauses and asks when:

- The answer would materially change the assessment scope or approach
- Applicability is unclear due to group structure complexity
- The organization's program maturity determines the depth of review
- AFA control readiness vs. general program improvement is the primary objective

Use the **⟁ CLARIFY** pattern wherever marked. If the user has already provided the information,
skip the question and proceed. For batch or non-interactive runs, use the defaults stated at
each CLARIFY point.

---

## Workflow

### Step 1: Accept Input

Accept the assessment input in any of these formats:

- **Compliance program documentation**: Code of conduct, whistleblower policy, risk mapping
  documents, due diligence procedures, training records, disciplinary policy, audit reports
- **Self-assessment questionnaire**: Organization's own assessment against the eight pillars
- **AFA control preparation package**: Documentation assembled in response to an AFA notice
- **M&A due diligence materials**: Target company compliance program documentation
- **Description only**: User describes the program from memory — lower confidence output

If no documentation is provided, inform the user that the assessment will be based on
described program elements only, and all findings will be flagged as [LOW CONFIDENCE — based
on description only].

---

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, gather the following context:

1. **Assessment trigger** — What prompted this review?
   - Options: **AFA control notice received** (highest urgency — prepare for inspection),
     **Annual internal program review**, **M&A due diligence** (assess target's program),
     **Program build** (build/redesign from scratch), **Regulatory change response** (Waserman
     update), **Other**
   - _Why this matters_: AFA control notice triggers an urgent gap-closure focus; program build
     requires a different step sequence (build vs. audit).

2. **Organization type** — Is the assessed entity the covered entity or a subsidiary?
   - Options: **French parent company assessing its own program**, **French subsidiary of
     foreign group**, **Foreign subsidiary being assessed for Sapin II group compliance**,
     **Target company in M&A transaction**
   - _Why this matters_: Parent vs. subsidiary changes which obligations apply and how group
     governance is evaluated.

3. **Sector** — What industry does the entity operate in?
   - Options: Defense/aerospace, Energy/extractives, Infrastructure/construction, Pharma/
     healthcare, Financial services, Technology, Consumer goods/retail, Professional services,
     Public procurement-dependent, Other
   - _Why this matters_: AFA applies sectoral risk scrutiny; high-risk sectors (defense, energy,
     infrastructure) face heightened standard.

4. **Program maturity** — How mature is the existing compliance program?
   - Options: **No formal program** (starting from zero), **Basic program** (some elements exist
     but incomplete), **Established program** (all 8 pillars exist but quality uncertain),
     **Mature program** (all 8 pillars, documented, updated, AFA-control-tested before)
   - _Why this matters_: Shapes the depth of remediation guidance and the urgency of Tier 1
     findings.

5. **International exposure** — Does the entity operate internationally?
   - Options: France only, EU/EEA operations, Operations in high-corruption-risk jurisdictions
     (Africa, Middle East, CIS, APAC emerging), Global with varied risk profile
   - _Why this matters_: International exposure intensifies risk mapping and due diligence
     requirements; also triggers FCPA/UK Bribery Act overlay analysis.

_Default (non-interactive)_: Treat as an established program, annual review trigger, French
parent company, mid-risk sector, and EU-plus operations unless otherwise stated.

---

### Step 3: Applicability Determination

Before assessing program quality, confirm that Sapin II's Article 17 obligations apply.

**Threshold Analysis:**

Apply the conjunctive test under Article 17 of Sapin II:

| Criterion       | Threshold                         | Notes                                                                      |
| --------------- | --------------------------------- | -------------------------------------------------------------------------- |
| Employees       | ≥ 500                             | Counted on consolidated basis (group employees worldwide if French parent) |
| Annual turnover | > €100 million                    | Calculated on consolidated basis; financial year average                   |
| Entity type     | Legal entity registered in France | OR foreign subsidiary of French-registered parent                          |

**Group Structure Rules:**

- French parent company must implement Sapin II group-wide, including foreign subsidiaries,
  regardless of whether those subsidiaries individually meet the thresholds [VERIFY: pending
  legislative reform may extend coverage further]
- Controlled subsidiaries (>50% ownership or de facto control) are included in threshold
  calculation
- French-registered holding companies with operating subsidiaries abroad: consolidated headcount
  and turnover determines obligation

**⟁ CLARIFY** — If threshold application is unclear due to group structure complexity:

- Ask the user to provide consolidated headcount and turnover figures
- Identify whether a French parent company controls the entity
- If uncertain, proceed on the assumption that Sapin II applies and flag the assumption

**Output:**
State clearly: **SAPIN II ARTICLE 17 APPLIES / MAY NOT APPLY / REQUIRES FURTHER VERIFICATION**

If Sapin II does not apply: note whether any indirect obligations may arise as a supplier to
covered entities, and whether the Loi de Vigilance (for entities ≥5,000/10,000 employees) may
instead apply.

---

### Step 4: Gather Legal Authority

Use **legalcode-mcp** to build a working legal reference file for this assessment.

**Research process:**

1. Search for the current consolidated text of Sapin II (Loi n° 2016-1691), with all Waserman
   amendments incorporated
2. Retrieve the current AFA Recommendations (Recommandations de l'AFA, last updated 12 January 2021)
3. Search for Commission des Sanctions decisions issued since 2019 (Sonepar and subsequent)
4. Search for applicable CJIP jurisprudence and DOJ/SFO cooperation frameworks
5. Search for any AFA practical guides issued in 2023-2024 relevant to the assessed sector

**Save results** to `/tmp/legalcode-sapin2-authority.md`:

```markdown
# Legal Authority — Sapin II Assessment

## Entity: [entity name or 'Unnamed']

## Date: [date]

### Primary Statutes

- [Statute, Article, current text]

### AFA Recommendations and Guidance

- [Publication, date, key points]

### Commission des Sanctions Decisions

- [Case, date, finding, sanction]

### CJIP Framework

- [CJIP parties, date, key compliance undertakings]
```

**Without legalcode-mcp**: Mark all statutory citations [VERIFY] and note in Glass Box:
`legalcode_mcp: "Not connected — manual verification required"`

---

### Step 5: Eight-Pillar Assessment

Assess the organization's compliance program against each of the eight mandatory pillars under
Article 17. Use the **Pillar Analysis Reference** section (below) for the detailed review
criteria for each pillar.

For each pillar, produce:

- **Status**: COMPLIANT ✅ / PARTIAL ⚠️ / NON-COMPLIANT ❌ / CRITICAL DEFICIENCY 🚨
- **Confidence**: DEFINITE / HIGH / PROBABLE / POSSIBLE / UNLIKELY
- **Findings**: Specific gaps or strengths identified
- **AFA Control Risk**: LOW / MODERATE / HIGH — the likelihood this pillar triggers an AFA finding
- **Remediation**: Specific, actionable steps with priority tier

**⟁ CLARIFY** — For long or complex programs (multiple subsidiaries, foreign components):

- Ask whether to perform a full eight-pillar deep assessment, or a priority assessment focused
  on the pillars most at risk given the organization's sector and geography
- If AFA control notice received, ask whether to focus on the specific pillars identified in the
  AFA's preliminary information request

**The Eight Pillars:**

| #   | Pillar (French)             | English                        | Assessment Depth       |
| --- | --------------------------- | ------------------------------ | ---------------------- |
| 0   | Engagement de la direction  | Governing Body Commitment      | Prerequisite condition |
| 1   | Code de conduite            | Code of Conduct                | Deep                   |
| 2   | Dispositif d'alerte interne | Internal Whistleblowing System | Deep (Waserman)        |
| 3   | Cartographie des risques    | Risk Mapping                   | Deep                   |
| 4   | Évaluation des tiers        | Third-Party Due Diligence      | Deep                   |
| 5   | Contrôles comptables        | Accounting Controls            | Standard               |
| 6   | Formation                   | Training Programs              | Standard               |
| 7   | Sanctions disciplinaires    | Disciplinary Sanctions         | Standard               |
| 8   | Suivi et évaluation         | Monitoring and Evaluation      | Standard               |

> Note: "Governing Body Commitment" is treated by AFA as a foundational prerequisite (Pilier 0),
> not one of the eight statutory pillars, but its absence typically renders the entire program
> non-credible to AFA inspectors.

---

### Step 6: Waserman Whistleblower Compliance Assessment

Given the significance of the Loi Waserman reforms (effective 1 September 2022), conduct a
dedicated sub-assessment of the whistleblowing system beyond the standard Pillar 2 review.

**Waserman Reform Checklist:**

| Requirement                | Pre-Waserman Sapin II                            | Waserman (from 1 Sept 2022)                                           | Compliant? |
| -------------------------- | ------------------------------------------------ | --------------------------------------------------------------------- | ---------- |
| Whistleblower definition   | Disinterested; personal knowledge                | No direct financial benefit; indirect knowledge permitted             |            |
| Reporting channel sequence | Mandatory internal → external → public hierarchy | Free choice of channel (internal, external, or public)                |            |
| Protected persons scope    | Whistleblower only                               | + facilitators, colleagues, and family members                        |            |
| Retaliation categories     | Dismissal/demotion                               | 17+ measures including blacklisting, social media harm, medical abuse |            |
| Burden of proof            | Whistleblower proves connection                  | Employer must disprove causal link                                    |            |
| Channel response time      | Not specified                                    | Acknowledge within 7 days; provide feedback within 3 months           |            |
| Anonymous reporting        | Permitted but not required                       | Channels must be capable of receiving anonymous reports               |            |
| Confidentiality obligation | General obligation                               | Specific obligation to protect reporter identity throughout process   |            |

**⟁ CLARIFY** — If the organization has not yet updated its whistleblower system since
1 September 2022:

- Flag as NON-COMPLIANT on all Waserman-specific requirements
- Treat update as Tier 1 (must-have) remediation item

---

### Step 7: AFA Control Readiness Assessment

Assess whether the organization is prepared to respond to an AFA control (audit). AFA controls
assess:

1. **Existence**: Does each of the eight pillars formally exist (documented)?
2. **Quality**: Does each pillar meet the AFA recommendations standard?
3. **Effectiveness**: Is there evidence each pillar is actually implemented and functioning?

**Key AFA Control Risk Factors:**

| Risk Factor                                                      | Weight       | Assessment |
| ---------------------------------------------------------------- | ------------ | ---------- |
| No governing body validation of risk map                         | HIGH         |            |
| Risk map not updated in >2 years                                 | HIGH         |            |
| Whistleblower system not updated post-Waserman                   | HIGH         |            |
| Third-party due diligence scope limited to direct suppliers only | MODERATE     |            |
| No documented beneficial ownership verification                  | MODERATE     |            |
| Training records incomplete or not role-differentiated           | MODERATE     |            |
| Accounting controls not formally documented                      | MODERATE     |            |
| No sanction applied for any code of conduct violation            | LOW-MODERATE |            |
| Group compliance not formally extended to subsidiaries           | HIGH         |            |

**CJIP Exposure Assessment:**

If the assessment reveals material compliance failures, assess CJIP (Convention Judiciaire
d'Intérêt Public) risk — the out-of-court resolution mechanism available to the PNF (Parquet
National Financier) for certain corruption-related offenses:

- CJIP requires implementation of a full Sapin II-compliant compliance program as a condition
- Financial penalty under CJIP may be up to 30% of average annual turnover [VERIFY]
- Voluntary disclosure and cooperation with PNF may reduce CJIP financial terms
- Material Sapin II compliance failures discovered during M&A can trigger inherited liability
  under Supreme Court precedent (Cass. crim. novembre 2020, mai 2024) [VERIFY citations]

---

### Step 8: M&A Due Diligence Assessment (if applicable)

**⟁ CLARIFY** — If the assessment was triggered by M&A:

- Confirm whether the target is the acquirer or target
- Confirm whether a pre-closing or post-closing assessment is needed

**M&A Anti-Corruption Due Diligence Framework:**

| Phase            | Scope                        | Sapin II Implications                                                                   |
| ---------------- | ---------------------------- | --------------------------------------------------------------------------------------- |
| **Pre-signing**  | Preliminary red flags only   | Identify deal-breaker compliance failures; inform representations and warranties        |
| **Pre-closing**  | Full eight-pillar assessment | Confirm existence of program; identify mandatory day-1 remediation needs                |
| **Post-closing** | Integration assessment       | Assess gap between target's program and acquirer's standards; build integration roadmap |

**Inherited Liability Risk:**
Under French Supreme Court jurisprudence (November 2020, May 2024), [VERIFY exact citations]
an acquiring entity may inherit liability for a target's pre-merger compliance failures. This
creates a specific due diligence obligation to:

- Obtain Sapin II compliance representations in the SPA
- Conduct full eight-pillar assessment prior to closing
- Implement corrective measures within an agreed post-closing period
- Retain escrow or indemnity protection for discovered non-compliance

**SPA Representations and Warranties — Standard Positions:**

| W&R                       | Minimum Standard               | Best Practice                                              |
| ------------------------- | ------------------------------ | ---------------------------------------------------------- |
| Sapin II applicability    | Confirm whether thresholds met | Confirm with specific numbers                              |
| Program existence         | All eight pillars in place     | All eight pillars in place, documented, and updated        |
| AFA control history       | No pending AFA proceedings     | No proceedings ever, or disclose all history               |
| No violations             | No known violations            | No violations and no whistleblower reports in past 3 years |
| CJIP/criminal proceedings | None pending                   | None pending or disclosed with details                     |

---

### Step 9: Remediation Roadmap

Synthesize findings from Steps 5-8 into a prioritized remediation roadmap. Use the
Prioritization Framework in the Quality Assurance section below.

**Roadmap Structure:**

1. **Tier 1 — Immediate (0-30 days)**: Critical deficiencies creating immediate AFA
   enforcement exposure, CJIP risk, or Waserman non-compliance
2. **Tier 2 — Near-term (30-90 days)**: Material gaps that would be flagged in an AFA
   control and require documented remedial plans
3. **Tier 3 — Program Enhancement (90-180 days)**: Quality improvements to raise program
   from functional to mature

For each remediation item:

- Identify the pillar or requirement
- Describe the specific gap
- Prescribe the corrective action
- Identify the owner (governing body / compliance officer / HR / finance / legal)
- Set a deadline consistent with the tier
- Estimate the effort (low / medium / high)

---

### Step 10: Quality Verification

Before delivering the assessment, run the full Quality Assurance Framework:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every CRITICAL DEFICIENCY item, run the 3-pass Self-Interrogation. Revise if any
   pass reveals a weakness.
3. Assign Confidence Scores to each pillar assessment.
4. Verify completeness: confirm all eight pillars have been addressed (present or flagged
   as absent).
5. Generate the Glass Box Audit Trail and append to the output.

---

### Step 11: Deliver Assessment

Deliver the output using the Output Format Template in the final section of this skill.

---

## Pillar Analysis Reference

### Pilier 0 — Governing Body Commitment (Engagement de la Direction)

This is a prerequisite condition assessed before the eight pillars. AFA treats absence of
genuine governing body engagement as undermining the entire program.

**Assessment criteria:**

- Has the governing body (conseil d'administration, conseil de surveillance, or equivalent)
  formally adopted a zero-tolerance anti-corruption policy?
- Are adequate resources (budget, personnel, reporting lines) allocated to the compliance
  function?
- Does the governing body receive regular compliance reports and demonstrate active oversight
  (not ceremonial prefatory endorsement)?
- When violations have occurred, has the governing body responded with appropriate disciplinary
  measures demonstrating firm attitude?
- Is the CEO/leadership team visibly committed to the compliance program?

**AFA standard (2021 Recommendations)**: Governing body commitment is the "sine qua non"
condition. A program lacking genuine leadership commitment will fail on effectiveness regardless
of documentation quality.

**Common deficiency**: Compliance officer develops the program in isolation; board merely
approves without substantive engagement; no board-level review of risk map results.

---

### Pilier 1 — Code de Conduite

**Assessment criteria:**

- Does the code of conduct address both active and passive corruption and influence peddling
  (trafic d'influence)?
- Does it specifically address hospitality, gifts, and entertainment (including gifts to and
  from public officials)?
- Does it address facilitation payments — and take the correct position (all facilitation
  payments prohibited, even small amounts)?
- Does it address conflicts of interest, political contributions, and charitable donations?
- Is it accessible to all employees in their working language?
- Does it include consequences for violations (cross-reference to disciplinary policy)?
- Has it been formally adopted by the governing body?
- Is it integrated into onboarding and updated when AFA guidance changes?
- Does it extend to agents, intermediaries, and business partners?

**Red flags:**

- Code permits "reasonable" facilitation payments — Sapin II position is zero tolerance
- No reference to influence peddling (trafic d'influence) — this is an Article 17 requirement
  distinct from corruption
- No coverage of third parties (agents, intermediaries) — most corruption risk flows through
  intermediaries
- Not translated into local languages for foreign subsidiaries

---

### Pilier 2 — Dispositif d'Alerte Interne (Post-Waserman)

**Assessment criteria (post-Loi Waserman, effective 1 September 2022):**

_Channel design:_

- Does the system accept both written and oral reports?
- If oral reporting offered, is telephone/voicemail available? Is video/in-person meeting
  available within 20 business days on request?
- Can the channel receive anonymous reports?
- Is the channel accessible to employees, former employees, job applicants, contractors,
  and agents?

_Procedure:_

- Is acknowledgment provided within 7 days of receipt?
- Is feedback on follow-up action provided within 3 months of acknowledgment?
- Is reporter identity kept strictly confidential throughout the process?

_Protected persons:_

- Are facilitators (persons assisting the reporter) explicitly protected?
- Are colleagues and family members protected from collateral retaliation?

_Free-channel choice:_

- Does the policy acknowledge the reporter's right to report directly to external authorities
  (AFA, PNF, ombudsman) without first exhausting internal channels?

_Burden of proof:_

- Does the policy acknowledge that if retaliation is alleged, the employer bears the burden
  of demonstrating the adverse action was unrelated to the report?

_GDPR interaction:_

- Is the whistleblower system covered by a GDPR Article 30 Record of Processing Activities?
- Has a DPIA been conducted?
- Are retention periods defined (typically: reports retained for up to 2 years from closure)?

**Waserman penalty for non-compliance**: Retaliation against a whistleblower can result in
criminal sanctions under Article 13 of Loi Waserman [VERIFY current penalty amounts], plus
civil liability for damages.

---

### Pilier 3 — Cartographie des Risques

**Assessment criteria (AFA 6-step methodology):**

| Step                            | Requirement                                        | Documents/Evidence Needed                |
| ------------------------------- | -------------------------------------------------- | ---------------------------------------- |
| 1. Roles & responsibilities     | Designated team; governance structure              | Written mandate; organization chart      |
| 2. Inherent risk identification | By business line, function, geography, stakeholder | Risk register (initial draft)            |
| 3. Exposure assessment          | Likelihood × impact for each risk                  | Risk matrix with scoring methodology     |
| 4. Control adequacy assessment  | Evaluation of existing mitigating controls         | Control inventory with gap analysis      |
| 5. Residual risk prioritization | Risks ranked by residual exposure                  | Prioritized risk map; action plans       |
| 6. Periodic update              | Mechanism for annual/trigger-based update          | Update history; board validation records |

**AFA non-delegability rule**: The governing body must validate the risk map. This responsibility
cannot be delegated to the compliance officer. Evidence of board validation (resolution, signed
cover sheet, minutes) is mandatory.

**Documentation standard**: The risk map must be formal, documented, and "capable of immediate
submission to AFA during a control."

**Trigger events requiring update:**

- M&A activity (acquiring or being acquired)
- Entry into new geographic markets (especially high-corruption-risk jurisdictions)
- New business lines or products
- Change in ownership structure
- Material changes in third-party relationships
- Following any corruption incident or whistleblower report

**Common AFA control findings on risk mapping:**

- Risk map prepared reactively after AFA notice, not as ongoing management tool
- Board involvement only nominal (rubber stamp, not substantive review)
- Generic assessments not adapted to company's actual business activities
- No assessment of control adequacy — gross risk only, no residual risk calculation
- No defined update schedule; maps becoming stale without triggers

---

### Pilier 4 — Évaluation des Tiers

**Assessment criteria:**

_Scope of covered third parties:_

- Does the due diligence program cover customers, first-tier suppliers, intermediaries/agents,
  and joint venture partners as a minimum?
- Are third parties in high-corruption-risk jurisdictions subject to enhanced due diligence?
- Are intermediaries earning fees for facilitating government relationships subject to
  heightened scrutiny?

_Due diligence process:_

- Phase 1 (information collection): Are beneficial ownership chains verified? Are sanctions
  lists checked (OFAC, EU, UN, national lists)?
- Phase 2 (risk assessment): Is the assessment holistic (geographic + relationship + sector
  - prior misconduct history)?
- Phase 3 (approval/decision): Are approvals documented with reasoned rationale (not just
  "approved")?

_Ongoing monitoring:_

- Are high-risk third parties subject to more frequent re-assessment than low-risk ones?
- Are triggering events (negative news, M&A, volume changes) monitored?
- Are transaction patterns in high-risk relationships reviewed for anomalies?

_Loi de Vigilance interaction:_

- Is Sapin II third-party assessment coordinated with Loi de Vigilance supply chain mapping
  to avoid duplicate processes?

**Deficiency thresholds:**

- No beneficial ownership verification → CRITICAL DEFICIENCY for agent/intermediary relationships
- No ongoing monitoring → NON-COMPLIANT (one-time-only due diligence is insufficient)
- Due diligence limited to Google search → PARTIAL at best (AFA expects structured, documented
  process with defined risk criteria)

---

### Pilier 5 — Contrôles Comptables

**Assessment criteria (AFA 3-level framework, April 2022 Practical Guide):**

| Level   | Owner                                            | Focus                            | Examples                                                                               |
| ------- | ------------------------------------------------ | -------------------------------- | -------------------------------------------------------------------------------------- |
| Level 1 | Accounting teams                                 | Daily operational controls       | Invoice matching; approval before payment; segregation of duties; duplicate prevention |
| Level 2 | Internal audit / compliance / finance management | Monitoring Level 1 effectiveness | Exception log review; spot checks; deviation investigation                             |
| Level 3 | Internal audit oversight                         | Comprehensive assessment         | Control design testing; operating effectiveness evaluation; gap remediation            |

**Sapin II-specific focus areas (distinct from standard audit):**

- Are controls applied systematically to risk-mapped high-risk transaction categories (not
  sampled)?
- Do controls specifically address: intermediary commissions, government-related payments,
  charitable donations/sponsorships, payments to entities in high-risk jurisdictions?
- Is segregation of duties enforced for high-risk payment flows?
- Are vendor validation controls in place for new vendor onboarding and periodic re-validation?
- Are unusually structured or rush payments flagged for compliance review?

**Key distinction from traditional audit**: Sapin II accounting controls are permanent and
systematic (applied to defined risk categories), not periodic and sampled.

---

### Pilier 6 — Formation

**Assessment criteria:**

| Element       | Requirement                                                                                                       |
| ------------- | ----------------------------------------------------------------------------------------------------------------- |
| Coverage      | At minimum: executives and employees with highest corruption/influence peddling exposure                          |
| Content       | Sapin II regulations; company anti-corruption policies; whistleblowing procedures; consequences of non-compliance |
| Customization | Role-specific training differentiated by risk exposure                                                            |
| Records       | Documentation of who was trained, when, and on what content                                                       |
| Frequency     | AFA does not specify but recommends regular refresher; annual cycle is standard practice                          |
| Format        | No mandatory format; e-learning, in-person, or hybrid acceptable                                                  |
| Third parties | Training (or equivalent awareness) for high-risk agents/intermediaries                                            |

**Common gap**: Training is generic and not differentiated by role. AFA expects that employees
in procurement, sales to government entities, and high-risk geographies receive more intensive
training than back-office staff.

**Documentation failure**: Inability to produce training records showing which employees
completed training and when is one of the most common AFA control deficiencies.

---

### Pilier 7 — Sanctions Disciplinaires

**Assessment criteria:**

- Is there a documented disciplinary process for code of conduct violations?
- Does the process apply proportionate and consistent sanctions?
- Has the company actually applied sanctions for violations when they occurred?
- Is the disciplinary process legally compliant with French labor law (Code du travail)?
- Are disciplinary procedures aligned across group entities?

**AFA standard**: An active, applied disciplinary system demonstrates genuine governing body
commitment. A disciplinary framework that has never been used for any violation, despite
a functioning whistleblower system, raises credibility questions.

**Key French labor law interaction [VERIFY]:**

- Sanctions must follow the rules of the Convention Collective (industry collective agreement)
  applicable to the employee
- Major disciplinary measures (licenciement pour faute grave/lourde) require specific procedural
  compliance (entretien préalable, délais)
- HR must be involved; the compliance officer cannot impose disciplinary sanctions unilaterally

---

### Pilier 8 — Suivi et Évaluation

**Assessment criteria:**

- Is there a regular internal audit of the compliance program's effectiveness (not just
  existence)?
- Does audit scope cover all eight pillars?
- Are audit findings documented and presented to the governing body?
- Is there a documented process for implementing remedial actions?
- Is the compliance program's overall maturity assessed periodically against AFA recommendations?
- Are external auditors or independent compliance reviewers used?

**AFA standard**: The monitoring pillar closes the loop — without it, deficiencies in other
pillars may go undetected. AFA treats absence of monitoring as evidence of program superficiality.

---

## Compliance Status Classification

### Four-Tier System

#### COMPLIANT ✅

- All AFA recommendation requirements are met for this pillar
- Documentation is current, complete, and in format ready for AFA submission
- Regulatory risk: **LOW**
- **Required action**: Maintain; schedule periodic review

#### PARTIAL ⚠️

- Core requirements partially met; material gaps remain
- Some documentation exists but is incomplete, outdated, or below AFA standard
- Regulatory risk: **MODERATE** — likely to trigger AFA observations or improvement orders
- **Required action**: Near-term remediation (Tier 2 priority)

#### NON-COMPLIANT ❌

- Pillar does not meet AFA minimum requirements
- Documentation absent, superficial, or demonstrably not implemented
- Regulatory risk: **HIGH** — likely to trigger AFA enforcement referral to Commission des Sanctions
- **Required action**: Immediate remediation (Tier 1 priority)

#### CRITICAL DEFICIENCY 🚨

- Pillar entirely absent, or a specifically prohibited practice is occurring (e.g., facilitation
  payments permitted by code of conduct; whistleblower retaliation occurring; risk map never
  prepared)
- Regulatory risk: **IMMEDIATE** — exposes governing body and senior individuals to Commission
  des Sanctions fines; may trigger PNF attention
- **Required action**: Escalate to governing body immediately; engage external compliance
  counsel; implement crisis remediation plan

---

## Prioritization Framework

### Tier 1 — Must-Have (0-30 days)

Findings that:

- Create immediate AFA enforcement exposure (NON-COMPLIANT or CRITICAL DEFICIENCY status)
- Involve Waserman non-compliance (since 1 September 2022, any failure is immediately
  material)
- Represent risk mapping failures where governing body has not validated
- Expose the entity to CJIP risk (no compliance program at all, or sham program)
- Would disqualify the entity from AFA-monitored programs (CJIP, moniteur)

**Governing body escalation required for all Tier 1 items.**

### Tier 2 — Should-Have (30-90 days)

Findings that:

- Result in PARTIAL status on any pillar
- Would trigger AFA observations in a control (but not automatic referral to Commission des
  Sanctions)
- Represent documentation gaps (program exists but is not "ready for immediate submission")
- Require updating following organizational changes (M&A, new markets)

**Compliance officer can own Tier 2 items with governance oversight.**

### Tier 3 — Program Enhancement (90-180 days)

Findings that:

- Represent quality improvements above minimum AFA standard
- Address best practices (not just baseline compliance)
- Improve alignment with international standards (FCPA/OECD)
- Enhance program maturity (from "functional" to "mature")

**Compliance function implements with periodic governance reporting.**

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise any failures before delivery.

| Gate           | Rule                                                                                               | Fail Action                                                |
| -------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Source**     | Every Sapin II obligation cites Article 17 or specific AFA recommendation provision                | Add citation or mark "[UNVERIFIED — verify on Légifrance]" |
| **Format**     | All citations use standard French legal citation format (Loi n° / Article / Décret n°)             | Fix format                                                 |
| **Currency**   | Every cited provision checked for Waserman amendments and AFA guidance updates                     | Flag "[CHECK CURRENCY — verify AFA website for updates]"   |
| **Domain**     | Analysis stays within Sapin II scope; no FCPA or UK Bribery Act obligations asserted as French law | Remove or flag jurisdictional bleed                        |
| **Confidence** | Uncertainty explicitly stated; Commission des Sanctions decisions have limited precedential force  | Add confidence qualifier                                   |

### Self-Interrogation for CRITICAL DEFICIENCY Items

For any finding classified as CRITICAL DEFICIENCY, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**: Does the critical deficiency classification follow logically
from Article 17 and AFA recommendations? Would AFA inspectors actually reach this conclusion?
Is this a clear violation, or a gray area being over-classified?

**Pass 2 — Completeness**: Are there mitigating factors (interim measures, compensating controls,
prior remediation efforts) that should reduce severity? Have all eight pillars been assessed
before reaching this conclusion?

**Pass 3 — Challenge**: What is the strongest argument that this is PARTIAL rather than CRITICAL
DEFICIENCY? Under what circumstances might a reasonable AFA inspector accept the current state
as an acceptable work-in-progress?

If any pass reveals a weakness, revise the classification before delivery. Record in Glass Box:
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                             | Action                                                     |
| ------------ | --------- | --------------------------------------------------- | ---------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled AFA standard; clear Article 17 requirement  | State with confidence                                      |
| **High**     | 0.80-0.94 | Strong AFA guidance; minor interpretation questions | State with brief caveat                                    |
| **Probable** | 0.60-0.79 | AFA likely view; could differ based on sector/size  | State with reasoning and caveats                           |
| **Possible** | 0.40-0.59 | Genuinely uncertain; competing interpretations      | Flag for qualified counsel review                          |
| **Unlikely** | 0.0-0.39  | Speculative; beyond current AFA guidance            | Do not assert; flag "[UNCERTAIN — seek specialist advice]" |

---

## Glass Box Audit Trail

Include this YAML block at the end of every assessment output:

```yaml
glass_box:
  skill_name: "legalcode-fr-sapin-ii-compliance"
  assessment_date: "[date]"
  entity: "[entity name or 'Unnamed']"
  entity_type: "[French parent / French subsidiary / Foreign subsidiary / M&A target]"
  sector: "[sector identified in Step 2]"
  trigger: "[AFA control / Annual review / M&A / Program build / Other]"
  applicability: "APPLIES / MAY NOT APPLY / REQUIRES VERIFICATION"
  pillars_assessed: "[number — 0 through 8]"
  waserman_assessment: "COMPLIANT / PARTIAL / NON-COMPLIANT"
  critical_deficiencies: "[number]"
  non_compliant_pillars: "[list by number]"
  partial_pillars: "[list by number]"
  compliant_pillars: "[list by number]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "Loi n° 2016-1691 du 9 décembre 2016, Article 17 — VERIFIED / UNVERIFIED"
    - "Loi n° 2022-401 du 21 mars 2022 (Waserman) — VERIFIED / UNVERIFIED"
    - "AFA Recommandations, 12 janvier 2021 — VERIFIED / UNVERIFIED"
  afa_guidance_consulted:
    - "[AFA guide title, date]"
  citations_verified: "[X VERIFIED] / [Y UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL DEFICIENCY items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  ma_diligence_conducted: "Yes / No"
  fcpa_overlap_flagged: "Yes / No / Not applicable"
  uk_bribery_act_overlap_flagged: "Yes / No / Not applicable"
  limitations:
    - "[Any scope limitations: document review only; no site visits conducted; etc.]"
    - "[AFA guidance currency: recommendations from 2021; verify for updates]"
    - "[Assessment based on description only, not reviewed documentation (if applicable)]"
  reviewer: "AI-assisted — requires review by qualified French avocat or AFA-accredited compliance officer"
```

---

## Anti-Patterns

What NOT to do when conducting or advising on Sapin II compliance:

1. **Treating AFA as a criminal enforcement agency** — AFA does not investigate corruption or
   pursue criminal sanctions. AFA's remit is prevention: assessing compliance program existence,
   quality, and effectiveness. Criminal proceedings for corruption remain with the PNF and
   criminal courts. Confusing these authorities leads to wrong risk assessments.

2. **Applying the 500/€100M thresholds per entity rather than on a consolidated basis** —
   The thresholds are calculated on a consolidated group basis. A French parent company with
   10 subsidiaries each with 60 employees still exceeds 500. Advising subsidiary-by-subsidiary
   misses the legal framework.

3. **Treating Sapin II whistleblower obligations as unchanged since 2016** — Loi Waserman
   (effective 1 September 2022) fundamentally reformed the whistleblower regime. A compliance
   program that has not been updated since 2020 is materially non-compliant with current law.

4. **Treating the code of conduct as the whole program** — A code of conduct without the
   other seven pillars provides no Sapin II protection. AFA explicitly treats codes of conduct
   as only one of eight equally required elements.

5. **Permitting facilitation payments in the code of conduct** — Unlike OECD Convention, Sapin II
   and AFA guidance take a zero-tolerance position on facilitation payments at any amount and
   frequency. A code that explicitly or implicitly permits facilitation payments is NON-COMPLIANT.

6. **Risk mapping by the compliance officer without board validation** — AFA explicitly requires
   that the governing body validate risk map results and that this responsibility cannot be
   delegated. A risk map signed off only by the compliance officer fails the non-delegability
   rule regardless of its analytical quality.

7. **One-time third-party due diligence without ongoing monitoring** — Sapin II requires ongoing
   monitoring of third parties, not a one-time onboarding check. An organization that due-
   diligences on relationship initiation and never re-assesses is NON-COMPLIANT.

8. **Restricting due diligence to direct suppliers** — AFA expects due diligence on customers,
   first-tier suppliers, intermediaries/agents, and joint venture partners at a minimum.
   Excluding agents and intermediaries — the highest-risk category for corruption — is a
   critical gap.

9. **Generic training not differentiated by risk exposure** — AFA expects training to be
   tailored to employees' risk exposure. Deploying the same generic e-learning to all employees
   regardless of whether they interact with public officials, work in high-risk geographies,
   or handle procurement is a common deficiency.

10. **Building a program that lives only in documents** — AFA assesses effectiveness, not
    existence. A program with policies but no evidence of implementation (training records,
    due diligence files, risk map validation minutes, disciplinary actions) is deemed
    non-functional. "If it isn't documented, it didn't happen" applies directly.

11. **Not extending the program to foreign subsidiaries** — French parent companies must
    implement Sapin II group-wide. Assuming that foreign subsidiaries below the individual
    500/€100M threshold are exempt from the group compliance program is incorrect.

12. **Treating accounting controls as equivalent to standard external audit** — Sapin II
    accounting controls are systematic, risk-based, and permanent — not periodic and sampled
    like statutory audit procedures. The three-level AFA framework (operational / monitoring /
    audit) is a distinct obligation parallel to, not satisfied by, the annual statutory audit.

13. **Ignoring CJIP implications during M&A** — A target with material Sapin II compliance
    failures carries potential CJIP liability that survives acquisition. Post-acquisition
    discovery of pre-merger compliance failures cannot easily be separated from the acquirer's
    exposure under Supreme Court precedent. M&A due diligence must include full Sapin II
    program review.

14. **Conflating Sapin II and Loi de Vigilance obligations** — These are distinct statutes
    with different thresholds, regulatory authorities, and covered risks. Sapin II: corruption/
    influence peddling risk; AFA oversight; 500/€100M threshold. Loi de Vigilance: human
    rights/environmental risk; no dedicated regulator; 5,000/10,000 threshold. An integrated
    third-party due diligence process is best practice, but separate compliance analyses are
    required.

15. **Assuming AFA sanctions are purely financial** — While the Commission des Sanctions can
    impose fines (up to €1M for companies, €200K for individuals), its preferred enforcement
    approach is remediation injunctions (injonction de se mettre en conformité). Failure to
    implement an injunction within the prescribed period escalates to financial sanctions and
    potential public disclosure of the non-compliance.

16. **Treating AFA's pedagogical approach as low enforcement risk** — AFA's preference for
    remediation over punishment is not an absence of teeth. Non-compliance or failure to
    implement improvement orders can result in public decisions naming the entity and
    individuals, significant reputational damage, and PNF referrals for underlying conduct.

---

## Writing Standards

Apply plain-language discipline to all assessment outputs:

**For executive summary** (shared with governing body):

- State pillar status (COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY) at the
  outset — no burying the lead
- Use plain French administrative language for technical terms; include English glosses for
  non-French-speaking board members where relevant
- One finding per sentence; no compound findings
- Active voice: "The risk mapping documentation lacks governing body validation" — not
  "It was found that governing body validation of risk mapping documentation was absent"

**For remediation roadmap** (used by compliance team):

- Prescribe specific, actionable steps — not "improve risk mapping" but "schedule governing
  body risk map validation session by [date]; obtain signed board resolution adopting map"
- Identify the responsible owner for each action
- Include a realistic deadline
- Avoid legal jargon in operational instructions

**Quality gates before delivery:**

1. Does the executive summary lead with the most critical findings (not methodology)?
2. Can the compliance officer translate every Tier 1 finding into a specific action within
   30 seconds of reading?
3. Is every AFA recommendation citation in correct French legal format?
4. Are all jurisdiction-specific French law terms used accurately and consistently?
5. Would a non-French-speaking general counsel understand the overall compliance posture
   from the executive summary alone?

---

## External Tool Integration

This skill uses **legalcode-mcp** as its primary legal research tool for France.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for consolidated Sapin II text (Article 17 and all amendments)
- Retrieve current AFA Recommendations text (2021 version; check for updates)
- Search Commission des Sanctions decisions for precedent on specific pillar deficiencies
- Verify Waserman reform provisions (Loi n° 2022-401, Articles 1-17)
- Check for any AFA sectoral guides published in 2023-2026 relevant to the assessed entity
- Mark all legalcode-mcp-sourced citations as VERIFIED in Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and AFA guidance citations with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Include a prominent notice: "All legal citations in this assessment require independent
  verification against current Légifrance text and AFA website publications"
- Focus assessment on structural quality and program design rather than specific Article
  citations
- Do not create the local authority reference file

---

## Localization Notes

Sapin II is France-specific, but its obligations have cross-border reach:

**For French parent companies with foreign subsidiaries:**

- The parent must extend all eight pillars to controlled subsidiaries
- Foreign subsidiaries may need country-specific overlays (UK Bribery Act, FCPA, local
  anti-bribery laws)
- Risk mapping must address high-corruption-risk jurisdictions where subsidiaries operate

**For French subsidiaries of foreign groups:**

- Confirm whether the French subsidiary individually meets 500/€100M thresholds
- If yes, the French subsidiary has independent Sapin II obligations regardless of group program
- Group programs designed for FCPA or UK Bribery Act compliance may not satisfy all Sapin II
  specifics (e.g., AFA non-delegability rule for risk map validation; Waserman whistleblower
  reforms differ from EU Directive minimum transposition in other Member States)

**French language requirements:**

- The code of conduct must be accessible to employees in French
- AFA controls are conducted in French; compliance documentation submitted to AFA must be
  in French (or accompanied by certified translation)
- Risk maps and due diligence records submitted to AFA must be in French

**Interaction with EU Whistleblower Directive (2019/1937):**

- Loi Waserman is France's transposition of the EU Whistleblower Directive
- France's transposition exceeds the Directive minimum (particularly on protected persons
  and prohibited retaliation categories)
- For comparison with other EU member states' implementations, the legalcode-eu-whistleblower-
  directive skill provides the cross-border framework

---

## Output Format Template

Structure the final assessment deliverable as follows:

````markdown
## Sapin II Compliance Assessment

**Entity**: [entity name or 'Unnamed']
**Assessment Date**: [date]
**Trigger**: [AFA control / Annual review / M&A due diligence / Program build]
**Applicability**: [APPLIES / MAY NOT APPLY / REQUIRES VERIFICATION]
**Program Maturity**: [Starting out / Basic / Established / Mature]
**Governing Law**: Loi n° 2016-1691 du 9 décembre 2016 (Sapin II) as amended by Loi n° 2022-401 du 21 mars 2022 (Waserman)
**Assessment Basis**: [Document review / Description only / Mixed]

---

## Executive Summary

**Overall Compliance Posture**: [CRITICAL / HIGH RISK / MODERATE RISK / LOW RISK]

[2-3 sentences: what is most significant about the overall posture — where the program
succeeds and where it fails. Lead with the most critical finding.]

### Pillar Status Summary

| Pillar                              | Status                                                       | AFA Control Risk | Priority |
| ----------------------------------- | ------------------------------------------------------------ | ---------------- | -------- |
| 0. Governing Body Commitment        | [COMPLIANT ✅ / PARTIAL ⚠️ / NON-COMPLIANT ❌ / CRITICAL 🚨] | LOW / MOD / HIGH | T1/T2/T3 |
| 1. Code of Conduct                  | [status]                                                     |                  |          |
| 2. Whistleblowing System (Waserman) | [status]                                                     |                  |          |
| 3. Risk Mapping                     | [status]                                                     |                  |          |
| 4. Third-Party Due Diligence        | [status]                                                     |                  |          |
| 5. Accounting Controls              | [status]                                                     |                  |          |
| 6. Training                         | [status]                                                     |                  |          |
| 7. Disciplinary Sanctions           | [status]                                                     |                  |          |
| 8. Monitoring & Evaluation          | [status]                                                     |                  |          |

---

## Applicability Analysis

[Threshold analysis conclusion with supporting numbers if available]

---

## Pillar-by-Pillar Assessment

### Pilier 0 — Governing Body Commitment | [STATUS] | Confidence: [level]

**Evidence assessed**: [what was reviewed]
**Findings**: [specific gaps or strengths]
**AFA control risk**: [LOW / MODERATE / HIGH]
**Remediation** (if applicable): [specific actions]

### Pilier 1 — Code de Conduite | [STATUS] | Confidence: [level]

[Repeat format for each pillar]

### Pilier 2 — Dispositif d'Alerte Interne (Waserman) | [STATUS] | Confidence: [level]

**Waserman reform compliance**: [specific checklist findings]

[Continue for all pillars 3-8]

---

## Waserman Reform Assessment

**Overall Waserman Status**: [COMPLIANT / PARTIAL / NON-COMPLIANT]

[Summary of Waserman-specific gaps with reform comparison table]

---

## AFA Control Readiness

**Control Readiness Level**: [READY / NEEDS PREPARATION / NOT READY]

[Key preparation actions before AFA control; documentation gaps; risk of Commission des Sanctions referral]

---

## CJIP Risk Profile (if applicable)

**CJIP Exposure**: [LOW / MODERATE / HIGH / NOT ASSESSED]

[Summary of factors increasing or decreasing CJIP exposure]

---

## M&A Findings (if applicable)

**Due Diligence Conclusion**: [PASS / FLAG / FAIL]

**Deal-Breaker Items**: [list any findings that require resolution before closing]
**SPA Recommendations**: [recommended representations, warranties, or conditions]

---

## Prioritized Remediation Roadmap

### Tier 1 — Immediate (0-30 days)

| Finding | Pillar   | Gap               | Action            | Owner   | Deadline | Effort       |
| ------- | -------- | ----------------- | ----------------- | ------- | -------- | ------------ |
| [item]  | [pillar] | [gap description] | [specific action] | [owner] | [date]   | Low/Med/High |

### Tier 2 — Near-Term (30-90 days)

[Repeat table format]

### Tier 3 — Program Enhancement (90-180 days)

[Repeat table format]

---

## International Overlay (if applicable)

**FCPA Overlap**: [YES — specific concerns / NO — no US nexus identified]
**UK Bribery Act Overlap**: [YES — specific concerns / NO — no UK nexus identified]

[Brief summary of any concurrent international anti-bribery obligations]

---

## Next Steps

1. [Immediate action with owner and deadline]
2. [Next action]
3. [Next action]

---

## Glass Box Audit Trail

```yaml
[YAML block per Glass Box template above]
```
````

```

---

## Provenance

Created by Legalcode (2026-03-21). Legalcode original synthesis. Research basis: comprehensive
web research on Loi n° 2016-1691 du 9 décembre 2016 (Sapin II); Loi n° 2022-401 du 21 mars
2022 (Waserman); AFA Recommendations (12 January 2021); AFA Commission des Sanctions decisions
(2019-2024); CJIP framework analysis; interaction with FCPA, UK Bribery Act, OECD Anti-Bribery
Convention, and Loi de Vigilance; M&A due diligence implications under French Supreme Court
precedent. Sources consulted include: agence-francaise-anticorruption.gouv.fr, légifrance.gouv.fr,
GAN Integrity Sapin II reference, Dechert, Ashurst, Osborne Clarke, Hughes Hubbard, HM Labrousse,
Soulier Bunch, Navacelle, Lexing, Lefebvre Dalloz, Implid, and Protiviti France. Structural
patterns adapted from the legalcode-contract-review gold standard (18-element quality framework,
Citation Quality Gates, Self-Interrogation, Confidence Scoring, Glass Box YAML audit trail) and
legalcode-anti-bribery-compliance (compliance domain 4-tier classification and pillar structure).
```
