---
name: legalcode-compliance-risk-assessment
description: Conducts systematic enterprise compliance risk assessments aligned with ISO 37301:2021 (Clause
  6.1.2), DOJ Evaluation of Corporate Compliance Programs (ECCP) September 2024 risk assessment element,
  COSO ERM Framework (20 principles), and ISO 31000 risk management principles. Use when preparing for
  DOJ/regulatory examination, conducting annual compliance risk review, building or validating risk appetite
  statements, identifying compliance program investment priorities, responding to an enforcement trigger,
  or satisfying ISO 37301 Clause 6.1.2 documentation requirements.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Conducts systematic enterprise compliance risk assessments aligned with ISO 37301:2021 (Clause 6.1.2), DOJ Evaluation of Corporate Compliance Programs (ECCP) September 2024 risk assessment element, COSO ERM Framework (20 principles), and ISO 31000 risk management principles. Identifies and maps regulatory obligations across applicable frameworks and jurisdictions; assesses inherent risk using a 5×5 likelihood-impact matrix; evaluates control design effectiveness and operational effectiveness using a five-level maturity model; calculates residual risk scores with confidence scoring; and generates board-ready risk heat maps. Covers regulatory/legal risk domains (anti-corruption/FCPA, AML/CTF, sanctions/OFAC, data privacy/GDPR, cybersecurity/NIS2, export controls, employment/labor, competition/antitrust, tax, ESG/supply chain/CSDDD, AI/emerging tech), plus operational, financial, reputational, and strategic compliance risks. Supports risk heat mapping, control testing methodology, key risk indicator (KRI) development, risk appetite framework definition, trend analysis, and peer benchmarking. Produces board-ready risk assessment reports with CRITICAL/HIGH/MEDIUM/LOW classifications, confidence-scored findings, Glass Box audit trail, KRI monitoring dashboard, and prioritized remediation roadmap. Use when preparing for DOJ/regulatory examination, conducting annual compliance risk review, building or validating risk appetite statements, identifying compliance program investment priorities, responding to an enforcement trigger, or satisfying ISO 37301 Clause 6.1.2 documentation requirements. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers; cross-references ISO 37301:2021, COSO ERM, ISO 31000, OCEG Red Book 3.5, US Sentencing Guidelines §8B2.1, DOJ ECCP 2024, NIS2 Directive 2022/2555, GDPR, FATF 40 Recommendations, and sector-specific overlays.


# Legalcode Compliance Risk Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted compliance risk
> assessment. It does not constitute legal advice and does not create an attorney-client
> relationship. All outputs should be reviewed by qualified legal counsel and compliance
> professionals licensed in the relevant jurisdictions before use. This skill does not
> replace a formal risk assessment conducted by a qualified risk management professional
> or external auditor. It produces a structured framework to support a human-led risk
> assessment — not a substitute for one. All HIGH and CRITICAL residual risk findings
> require validation through primary evidence and control testing before board
> presentation. Laws, regulations, and enforcement priorities change; verify current
> applicability before relying on any provision described here. Statutory references,
> regulatory citations, and enforcement data cited from memory carry hallucination risk —
> always verify against authoritative sources before using in regulatory submissions or
> board reporting. ISO 37301:2021 requires licence purchase for the full standard text;
> consult the official ISO publication for authoritative requirements.

---

## Purpose and Scope

This skill assesses the current-state compliance risk profile of an organization across
all applicable regulatory domains. It quantifies inherent risk (what is the exposure
before controls?), evaluates control effectiveness (design and operational), calculates
residual risk (what exposure remains after controls?), and produces board-ready outputs
including risk heat maps, KRI frameworks, and remediation roadmaps.

**Covers:**

- Enterprise regulatory obligation mapping across all applicable jurisdictions
- Inherent risk quantification: 5×5 likelihood-impact matrix per risk domain
- Control effectiveness evaluation: five-level maturity model (design + operating)
- Residual risk calculation with confidence-scored findings
- Risk heat map generation (domain × jurisdiction visualization)
- Risk appetite and tolerance framework definition and gap analysis
- Key Risk Indicator (KRI) development with monitoring thresholds
- Trend analysis: improving / stable / deteriorating trajectory
- Peer benchmarking context using enforcement data
- Board-ready risk assessment report with CRITICAL/HIGH/MEDIUM/LOW classification
- Prioritized remediation roadmap (IMMEDIATE / NEAR-TERM / BACKGROUND)
- ISO 37301 Clause 6.1.2 compliance documentation output
- DOJ ECCP risk assessment documentation for enforcement defense

**Does not:**

- Design or assess compliance program architecture (see `legalcode-compliance-program-builder`)
- Provide legal advice or substitute for qualified compliance counsel
- Guarantee immunity from enforcement — risk assessment does not eliminate liability
- Perform deep domain-specific assessments (for AML/KYC see `legalcode-aml-kyc-compliance`;
  for HIPAA see `legalcode-hipaa-compliance-assessment`; for NIST CSF see
  `legalcode-nist-csf-mapping`)
- Conduct actual investigations or review documents for evidence of wrongdoing

**Related skills:**

- `legalcode-compliance-program-builder` — program design and maturation once risks identified
- `legalcode-aml-kyc-compliance` — deep AML/KYC-specific assessment
- `legalcode-hipaa-compliance-assessment` — deep HIPAA Security Rule assessment
- `legalcode-nist-csf-mapping` — NIST CSF 2.0 cybersecurity posture assessment
- `legalcode-eu-ai-act-high-risk-compliance` — EU AI Act high-risk system assessment
- `legalcode-incident-response-plan-builder` — incident response program after risk identified
- `legalcode-regulatory-change-tracker` — ongoing monitoring of regulatory changes

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The regulatory universe applicable to an
organization is determined by its industry, geographic footprint, data flows, and
business activities — not by a single governing law.

[JURISDICTION-SPECIFIC: United States] Apply DOJ ECCP September 2024 three-question
framework (well-designed? adequately resourced? works in practice?). Verify USSG §8B2.1
seven elements for culpability score reduction. For public companies: SOX §302/404
internal controls overlap. For financial institutions: BSA/AML program requirements
under 31 U.S.C. §§ 5311–5336, OCC Compliance Risk Assessment guidance, CFPB
supervisory standards. For healthcare: HIPAA Security Rule risk analysis per 45 CFR
164.308(a)(1)(ii)(A). For defense contractors: CMMC 2.0 requirements per DFARS.

[JURISDICTION-SPECIFIC: European Union] ISO 37301 certification pathway (Type A
certifiable under IAF MD 26). GDPR Article 32 security measures risk assessment
integration. NIS2 Directive 2022/2555 risk management measures (Article 21) for
essential and important entities — transposed nationally by October 2024 (with
significant member-state variation). CSDDD Directive 2024/1760 supply chain due
diligence (phased: 2027–2029). EU AI Act 2024/1689 risk assessment for high-risk
AI systems. AMLR 2024/1624 (mandatory from July 2027). CSRD Directive 2022/2464
sustainability due diligence with compliance risk dimensions.

[JURISDICTION-SPECIFIC: United Kingdom] UK Bribery Act 2010 adequate procedures
defence (Section 7): MoJ Six Principles risk assessment requirement. NIS2 equivalent:
UK NIS Regulations 2018 (under review for 2025 reform). UK GDPR and Data (Use and
Access) Act 2025 security risk assessment. FCA systems and controls (SYSC) framework
for regulated firms.

[JURISDICTION-SPECIFIC: Other Key Jurisdictions] Brazil: LGPD Arts. 46–49 security
risk assessment. India: DPDP Act 2023 and DPDP Rules 2025 (compliance deadline May
2027). Australia: Privacy Act 1988 and Privacy and Other Legislation Amendment Act
2024 security and privacy risk assessment requirements.

**[VERIFY]** — All regulatory references above should be verified against authoritative
sources before use in regulatory submissions. Enforcement priorities and specific
thresholds change; verify current enforcement posture before board presentation.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
organizational context, the workflow pauses and asks when:

- The answer would materially change the scope or depth of the assessment
- Multiple valid methodologies exist for the risk domain in question
- Risk appetite and tolerance levels are needed to classify residual risk correctly
- Control testing depth options have significantly different time and cost implications

Use the **⟁ CLARIFY** pattern (structured options with rationale) wherever marked below.
If the user has already provided the information, skip the question and proceed.

For **batch / non-interactive runs**: use these defaults:

- Operating mode: Full Enterprise Assessment with Remediation Roadmap
- Scope: All 20 risk domains unless otherwise specified
- Jurisdiction: Global baseline with [JURISDICTION-SPECIFIC] markers
- Control testing depth: Desktop review (documentation-based)
- Risk appetite: Conservative defaults (see Step 2) pending board-approved statement

---

## Workflow

### Step 1: Accept Input and Determine Operating Mode

**⟁ CLARIFY** — What is the primary purpose of this risk assessment?

1. **Annual Enterprise Compliance Risk Assessment** — Full assessment of all applicable
   risk domains; produces board-ready risk report with heat map, KRI dashboard, and
   remediation roadmap. Satisfies ISO 37301 Clause 6.1.2 and DOJ ECCP documentation
   requirements.

2. **Focused Domain Assessment** — Deep assessment of a specific compliance domain
   (e.g., anti-corruption, data privacy, AML). Specify the domain(s). Produces domain-
   specific heat map and control testing recommendations.

3. **Pre-Examination Assessment** — Preparing for an upcoming regulatory examination or
   DOJ/enforcement inquiry. Prioritizes examination-ready documentation and defensibility.
   Produces examination evidence file with Glass Box audit trail.

4. **Risk Appetite Calibration** — Assess current risk profile to inform board risk
   appetite statement or validate existing appetite thresholds. Identifies domains where
   actual risk exceeds stated appetite.

5. **Trigger Assessment** — Following an enforcement action, incident, or significant
   regulatory change. Rapid assessment of the affected domain and adjacent risks.

_If operating mode unclear, default to (1) Annual Enterprise Assessment._

Accept organizational context in any format:

- Questionnaire responses (Step 2 below)
- Existing risk assessment document to update
- Compliance program documentation, audit reports, or control inventories
- Free-text description of the organization and its activities

---

### Step 2: Gather Organizational Context

**⟁ CLARIFY** — Gather this context before beginning. For batch runs, state all
assumptions explicitly in the Glass Box audit trail.

**2a. Organization Profile**

- Industry sector (financial services, healthcare, technology, manufacturing, retail,
  professional services, energy/extractives, public sector, other)
- Approximate size (headcount; revenue if available)
- Geographic footprint (US-only, EU-only, UK-only, multi-regional, global)
- Ownership and listing status (private, public/listed, PE-backed, non-profit)
- Regulatory status (licensed/registered entities? Which regulators?)

**2b. Primary Business Activities Driving Compliance Risk**

- Business activities: (payments, lending, data processing, defense contracts, healthcare
  services, cross-border transactions, government contracting, emerging tech deployment)
- Third-party relationships: (agents, distributors, joint venture partners, vendors
  handling regulated data or government contracts)
- High-risk geographies: (operations in FATF high-risk jurisdictions, OFAC-sanctioned
  countries, high-corruption-index markets)

**2c. Existing Compliance Infrastructure**

- Compliance function: (None / Part-time / Dedicated CCO / Full team)
- Board/Audit Committee engagement: (None / Ad hoc / Periodic / Active)
- Existing risk assessment: (None / Informal / Formal <12 months old / Formal >12 months)
- Control inventory: (None / Informal documentation / Formal framework)
- Prior regulatory findings: (None / Examination findings / Consent order / Enforcement)

**2d. Risk Appetite Reference Point** (if available)

- Board-approved risk appetite statement: (Yes / No / In progress)
- If yes: provide or summarize the appetite thresholds by domain
- If no: proceed with **conservative default thresholds** (see Risk Appetite section below)

**State assumptions explicitly** if context is incomplete. Example:
_"Assuming US + EU footprint based on [context]. Assuming no board-approved risk appetite
statement — applying conservative defaults. Adjust if this is incorrect."_

---

### Step 3: Map the Regulatory Universe

Map all compliance obligations applicable to the organization. Produce a **Regulatory
Applicability Matrix** as the output of this step.

#### 3a. Primary Framework Applicability Screening

For each domain below, determine: **MANDATORY** (legal obligation) / **VOLUNTARY**
(industry standard or certification) / **NOT APPLICABLE** (no legal nexus).

| Domain                              | Key Frameworks                                                                                                      | Applicability Trigger                                                                              |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Anti-Corruption / Anti-Bribery      | FCPA 15 U.S.C. §78dd-1; UK Bribery Act 2010; OECD Anti-Bribery Convention                                           | US nexus (issuer/domestic concern) or UK nexus; cross-border payments; high-risk market operations |
| AML / Counter-Terrorist Financing   | BSA 31 U.S.C. §§5311–5336; EU AMLR 2024/1624; UK POCA 2002; FATF 40 Recommendations                                 | Financial services; MSB; real estate; VASP; professional services (legal, accounting)              |
| Sanctions Compliance                | OFAC 50 U.S.C. §§1701–1706; EU Council Regulations; UK Russia/Iran/Syria sanctions                                  | Any US nexus (USD clearing), EU/UK nexus, or transactions with sanctioned jurisdictions            |
| Data Privacy                        | GDPR Reg. 2016/679; UK GDPR; CCPA/CPRA Cal. Civ. Code §1798.100; LGPD Brazil; DPDP India 2023                       | Processing personal data of EU/UK/CA/BR/IN residents; California threshold                         |
| Cybersecurity                       | NIS2 Directive 2022/2555; NIST CSF 2.0; ISO/IEC 27001:2022; HIPAA 45 CFR Part 164; DORA Reg. 2022/2554              | Essential/important entity EU; healthcare; financial; government; critical infrastructure          |
| Export Controls / Trade             | EAR 15 C.F.R. Parts 730–774; ITAR 22 C.F.R. Parts 120–130; EU Dual-Use Regulation 2021/821                          | Technology company; defense; dual-use goods; non-US persons with controlled technology             |
| Employment / Labor Practices        | FLSA 29 U.S.C. §201; NLRA 29 U.S.C. §151; EU Platform Work Directive 2024/2831; GDPR HR; WARN Act                   | Any employer; independent contractor relationships; platform/gig arrangements                      |
| Competition / Antitrust             | Sherman Act 15 U.S.C. §§1–7; EU TFEU Arts. 101–102; UK Competition Act 1998                                         | Market leadership; agreements with competitors; pricing decisions; merger activity                 |
| Tax Compliance                      | IRC §482 (transfer pricing); OECD BEPS Pillar Two (Global Minimum Tax); CBCR; local tax                             | Multi-jurisdiction operations; intra-group transactions; IP holding structures                     |
| ESG / Supply Chain / Modern Slavery | CSDDD Directive 2024/1760; UK Modern Slavery Act 2015; German LkSG; CSRD Directive 2022/2464                        | EU large company; UK annual revenue >£36M; German supply chain >1,000 employees                    |
| Financial Reporting / Fraud         | SOX §§302, 404 (public companies); FCPA books & records §78m(b); FRC UK Governance                                  | Listed companies; audit committee oversight; government contracting (False Claims Act)             |
| AI / Emerging Technology            | EU AI Act 2024/1689; NIST AI RMF 1.0; FTC Act §5 AI unfair practices; EEOC AI employment                            | Deploying AI systems; automated decision-making affecting individuals                              |
| Third-Party / Vendor Risk           | FCPA third-party liability; AML vendor oversight; GDPR Art. 28 processor requirements; NIS2 Art. 21(d) supply chain | Any organization with third-party relationships handling regulated activities or data              |
| Government Contracting              | FAR/DFARS; False Claims Act 31 U.S.C. §3729; CMMC 2.0 for DoD contractors                                           | US government contracts; defense sector; federal procurement                                       |
| Environmental / EHS                 | OSHA 29 U.S.C. §651; Clean Air Act 42 U.S.C. §7401; EU ETS; UK Emissions Trading                                    | Manufacturing; energy; chemicals; construction; any physical operations                            |
| Sector-Specific Overlays            | HIPAA (healthcare); FINRA/SEC (securities); FCA SYSC (UK financial); FDA 21 CFR (pharma/med device)                 | Regulated industry sector — apply relevant overlay in addition to cross-sector domains             |

[JURISDICTION-SPECIFIC] When a domain is triggered for multiple jurisdictions, note
the **highest-penalty** regime: this determines inherent risk weighting in Step 4.

#### 3b. Produce Regulatory Applicability Matrix

| Framework          | Applicable?      | Highest-Penalty Provision                   | Most Recent Key Update                    | Current Enforcement Focus                            |
| ------------------ | ---------------- | ------------------------------------------- | ----------------------------------------- | ---------------------------------------------------- |
| FCPA               | [Yes/No/Partial] | Criminal up to $2M/count + disgorgement     | DOJ ECCP Sept 2024                        | AI-enabled fraud schemes; third-party intermediaries |
| UK Bribery Act     | [Yes/No/Partial] | Unlimited fine + 10 years imprisonment      | SFO active prosecution posture 2024–2025  | Facilitation payments; hospitality limits            |
| GDPR               | [Yes/No/Partial] | €20M or 4% global annual turnover           | EDPB Guidelines 2024–2025                 | Consent, cross-border transfers, AI decisions        |
| NIS2               | [Yes/No/Partial] | Up to €10M or 2% global turnover            | Member-state transposition deadlines 2024 | Supply chain security; board liability               |
| OFAC               | [Yes/No/Partial] | Up to $1M+ per violation (strict liability) | Russia/Iran/DPRK SDN updates 2024–2025    | Crypto, sanctions evasion, third-party exposure      |
| [Other applicable] |                  |                                             |                                           |                                                      |

---

### Step 4: Assess Inherent Risk

For each **MANDATORY** regulatory domain identified in Step 3, assess **inherent risk**
assuming all controls are absent. This isolates the raw regulatory exposure before any
mitigating controls are applied.

#### 4a. Inherent Risk Scoring Methodology

Inherent Risk = **Likelihood (L) × Impact (I)** on a 5×5 matrix.

**Likelihood (1–5):** How probable is a compliance failure in this domain, given
the organization's business activities, geographic footprint, and industry?

| Score | Label          | Definition                                                                              |
| ----- | -------------- | --------------------------------------------------------------------------------------- |
| 1     | Rare           | Failure highly improbable given activities; no history; very low inherent exposure      |
| 2     | Unlikely       | Failure could occur in unusual circumstances; limited inherent exposure                 |
| 3     | Possible       | Failure might occur given current activities; moderate inherent exposure; some history  |
| 4     | Likely         | Failure expected in some circumstances; high inherent exposure; or prior findings exist |
| 5     | Almost Certain | Failure expected to occur frequently without controls; very high inherent exposure      |

**Impact (1–5):** What is the consequence of a compliance failure in this domain?
Consider: regulatory penalty, criminal liability, business disruption, reputational harm,
third-party claims.

| Score | Label        | Definition                                                                                        |
| ----- | ------------ | ------------------------------------------------------------------------------------------------- |
| 1     | Negligible   | Minimal financial impact; no criminal exposure; regulatory warning only                           |
| 2     | Minor        | Modest financial penalty; administrative sanction; limited reputational impact                    |
| 3     | Moderate     | Significant penalty ($100K–$5M range); potential licensing risk; reputational damage              |
| 4     | Major        | Substantial penalty ($5M–$50M range); criminal exposure for individuals; market disruption        |
| 5     | Catastrophic | Existential penalty (>$50M or disgorgement); criminal indictment; license revocation; market exit |

**Inherent Risk Score = L × I** (range: 1–25)

| Score Range | Tier     | Color |
| ----------- | -------- | ----- |
| 20–25       | CRITICAL | 🔴    |
| 13–19       | HIGH     | 🟠    |
| 7–12        | MEDIUM   | 🟡    |
| 1–6         | LOW      | 🟢    |

#### 4b. Inherent Risk Scoring by Domain

For each applicable domain, assign L and I scores with **written rationale and source
evidence** for each score. Do not use scores without justification.

Example inherent risk assessment entry:

```
Domain: Anti-Corruption / FCPA
Likelihood: 4 (Likely)
  Rationale: Operations in 3 high-CPI-index markets (Brazil CPI 37, India CPI 39,
  Indonesia CPI 34 — Transparency International 2024); 40% of revenue through local
  agents with discretionary commission structures; no documented agent vetting beyond
  basic KYC [VERIFY — confirm agent count and market list with business]
Impact: 5 (Catastrophic)
  Rationale: FCPA criminal penalties up to $2M per count for companies plus
  disgorgement; prior DOJ FCPA resolutions in same industry averaged $48M (2022–2024)
  [VERIFY — confirm enforcement data currency]; personal liability for senior officers;
  potential loss of government contract eligibility
Inherent Risk Score: 4 × 5 = 20 (CRITICAL)
Confidence: HIGH (0.85) — well-documented enforcement pattern and geographic exposure
```

**⟁ CLARIFY** — For each CRITICAL or HIGH inherent risk domain, ask:
_"Is [domain] a known area of regulatory attention for your industry? Has the organization
received prior examination findings or enforcement in this area? The answer affects
both the Likelihood score and the Prioritization tier."_

#### 4c. Produce Inherent Risk Register

| Domain                 | Likelihood (L) | Impact (I) | Inherent Score (L×I) | Tier                     | Confidence                       |
| ---------------------- | -------------- | ---------- | -------------------- | ------------------------ | -------------------------------- |
| Anti-Corruption        | [1–5]          | [1–5]      | [L×I]                | CRITICAL/HIGH/MEDIUM/LOW | [VERIFIED/LIKELY/VERIFY/ASSUMED] |
| AML/CTF                |                |            |                      |                          |                                  |
| Sanctions              |                |            |                      |                          |                                  |
| Data Privacy           |                |            |                      |                          |                                  |
| Cybersecurity          |                |            |                      |                          |                                  |
| Export Controls        |                |            |                      |                          |                                  |
| Employment             |                |            |                      |                          |                                  |
| Competition            |                |            |                      |                          |                                  |
| Tax                    |                |            |                      |                          |                                  |
| ESG/Supply Chain       |                |            |                      |                          |                                  |
| Financial Reporting    |                |            |                      |                          |                                  |
| AI/Emerging Tech       |                |            |                      |                          |                                  |
| Third-Party Risk       |                |            |                      |                          |                                  |
| Government Contracting |                |            |                      |                          |                                  |
| [Sector Overlay]       |                |            |                      |                          |                                  |

---

### Step 5: Evaluate Control Effectiveness

For each domain with an inherent risk score ≥7 (MEDIUM or above), evaluate the
effectiveness of controls currently in place. Assess **Design Effectiveness** and
**Operational Effectiveness** separately.

#### 5a. Control Effectiveness Scoring Methodology

**Design Effectiveness (DE):** Is the control designed to address the regulatory
requirement? Is it fit for purpose given the organization's risk profile?

**Operational Effectiveness (OE):** Is the control operating as designed? Is there
evidence of consistent execution?

Both scored on a **five-level maturity scale**:

| Level | Label            | Design Description                                                                  | Operating Description                                                           |
| ----- | ---------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| 1     | Non-existent     | No control exists; requirement not addressed                                        | No evidence of control operation; never tested                                  |
| 2     | Initial / Ad Hoc | Control partially addresses requirement; incomplete or not tailored to organization | Control operates inconsistently; no documented procedures; no testing evidence  |
| 3     | Defined          | Control addresses requirement; documented procedure; reasonably fit for purpose     | Control operates with some consistency; limited testing; some gaps in execution |
| 4     | Managed          | Control is well-designed; comprehensively addresses requirement; regularly reviewed | Control operates consistently; periodic testing; minor execution gaps           |
| 5     | Optimized        | Control is best-practice; exceeds minimum requirement; integrated with monitoring   | Control operates effectively; continuous monitoring; evidence of improvement    |

**Use the MINIMUM CONTROL SCORE rule**: For a domain with multiple controls, the
domain Control Effectiveness = the **lowest-scored** individual control. Averaging masks
critical gaps (e.g., a Level 5 encryption policy does not compensate for a Level 1
incident response process).

**⟁ CLARIFY** — Control testing depth. Choose the approach appropriate to the
operating mode:

- **Option A — Desktop Review (2–3 hours):** Assess control design effectiveness via
  documentation review only. Operating effectiveness assessed as ASSUMED pending testing.
  All OE scores marked [ASSUMED — desktop review only].

- **Option B — Light Testing (1–2 days):** Sample key controls for basic operating
  effectiveness: request 5–10 evidence examples per CRITICAL/HIGH domain; review recent
  audit reports; interview compliance owner. OE scores based on sampled evidence;
  remaining controls marked [VERIFY — limited sample].

- **Option C — Comprehensive Testing (1–2 weeks):** Full control testing per domain:
  sample 25+ items, conduct design and operating effectiveness procedures, review last
  3 audit cycles. Produces exam-ready evidence file. OE scores marked [VERIFIED] where
  evidence is confirmed.

_Default for batch run: Option A (Desktop Review)._

#### 5b. Control Assessment Template per Domain

For each MEDIUM+ domain:

```
Domain: [Name]
Key Controls:

Control 1: [Name — e.g., Anti-Corruption Policy and Code of Conduct]
  Design Effectiveness: [1–5] — [Rationale: policy scope, tailoring, regulatory alignment]
  Operating Effectiveness: [1–5] — [Evidence: last review date, training completion, attestation rate]
  Testing Evidence: [VERIFIED (source + date) / LIKELY / [VERIFY] / ASSUMED]

Control 2: [Name — e.g., Third-Party Due Diligence Program]
  Design Effectiveness: [1–5]
  Operating Effectiveness: [1–5]
  Testing Evidence: [...]

[Additional controls as applicable]

Domain Operating Effectiveness (MINIMUM OE score across all controls): [Level]
Domain Design Effectiveness (MINIMUM DE score): [Level]
Control Gap: DE > OE? (If DE – OE ≥ 2: flag as DESIGN-OPERATION GAP)
```

---

### Step 6: Calculate Residual Risk

#### 6a. Residual Risk Formula

**Residual Risk Score = Inherent Risk Score × (1 − OE/5)**

Where:

- **Inherent Risk Score** = L × I from Step 4 (range: 1–25)
- **OE** = Domain Operating Effectiveness from Step 5 (MINIMUM score, 1–5)
- **OE/5** = Control Effectiveness Ratio (0.20–1.00)
- **Residual Range** = 0.20 × Inherent (if OE=5) to 0.80 × Inherent (if OE=1)

**Design-Operation Gap Adjustment**: If DE − OE ≥ 2 points, apply a **1.25×
multiplier** to the residual risk score. This accounts for the heightened risk when
controls are designed but not operating — a red flag for regulators and examiners.

**Residual Classification:**

| Residual Score | Tier        | Description                                                                                                                               |
| -------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| ≥15            | CRITICAL 🔴 | Residual risk exceeds risk appetite by a material margin; immediate regulatory exposure; control breakdown at design or operational level |
| 9–14           | HIGH 🟠     | Residual risk elevated; likely to exceed conservative risk appetite; requires near-term remediation and enhanced monitoring               |
| 5–8            | MEDIUM 🟡   | Residual risk at or near risk appetite boundary; tolerable with enhanced monitoring and KRI tracking                                      |
| 1–4            | LOW 🟢      | Residual risk within acceptable range for most organizations; routine monitoring sufficient                                               |

#### 6b. Residual Risk Register

| Domain          | Inherent | OE Level | OE Ratio | Residual (Raw) | D-O Gap?         | Adj. Multiplier | Residual (Final) | Tier     |
| --------------- | -------- | -------- | -------- | -------------- | ---------------- | --------------- | ---------------- | -------- |
| Anti-Corruption | 20       | 2        | 0.40     | 12.0           | Yes (DE=4, OE=2) | 1.25×           | 15.0             | CRITICAL |
| Data Privacy    | 16       | 3        | 0.60     | 6.4            | No               | 1.00×           | 6.4              | MEDIUM   |
| [Etc.]          |          |          |          |                |                  |                 |                  |          |

#### 6c. Apply Self-Interrogation to CRITICAL and HIGH Residuals

For every domain classified CRITICAL or HIGH, apply this **3-pass review** before
finalizing the residual score:

**Pass 1 — Risk Chain Integrity:**
Does the CRITICAL/HIGH classification follow logically from the inherent risk score
and control effectiveness evidence? Would the board or a regulator agree with this
residual? Is the score based on verified evidence, or primarily on assumptions?

_Specific test_: State the single weakest evidence point supporting this classification.
If it is ASSUMED rather than VERIFIED, what would change if the assumption were wrong?

**Pass 2 — Compensating Controls:**
Have all relevant controls been considered? Is there a compensating control, mitigating
factor, or control interaction that could lower the score?

_Example_: If encryption is OE Level 2 (weak), has the detective control (audit logging

- incident response) been separately assessed for its ability to contain a breach?
  If so, does applying the MINIMUM CONTROL SCORE still produce the CRITICAL result?

**Pass 3 — Regulatory and Enforcement Context:**
Does this residual risk reflect a known area of regulatory examination focus for this
industry and jurisdiction? Is there an enforcement pattern supporting the CRITICAL
classification, or is this organization's exposure lower than industry baseline?

_If Pass 3 reveals the organization is below industry average_: Consider adjusting from
CRITICAL to HIGH and noting the benchmarking context in the risk narrative.

Mark each reviewed domain: `self_interrogation: PASS | REVISED — [reason]`

---

### Step 7: Define Risk Appetite and Identify Appetite Gaps

#### 7a. Risk Appetite Framework

**Risk Appetite** = the maximum residual risk the board is willing to accept in pursuit
of organizational objectives.

**Risk Tolerance** = the acceptable variance around the risk appetite (the buffer before
escalation is required).

If no board-approved risk appetite statement exists, apply **conservative default
thresholds** pending board approval:

| Tier     | Conservative Default Appetite                                    | Tolerance Buffer    | Escalation Trigger                              |
| -------- | ---------------------------------------------------------------- | ------------------- | ----------------------------------------------- |
| CRITICAL | Not acceptable; immediate remediation required                   | No tolerance        | Board escalation + Audit Committee notification |
| HIGH     | Not acceptable absent documented remediation plan within 30 days | ±0.5 residual score | Board notification at next scheduled meeting    |
| MEDIUM   | Acceptable with documented KRI monitoring and semi-annual review | ±1.0 residual score | Report at next compliance committee meeting     |
| LOW      | Acceptable with annual review                                    | ±1.5 residual score | Standard annual reporting                       |

**[JURISDICTION-SPECIFIC: Financial Institutions]** FFIEC/OCC risk appetite frameworks
require specific board policy approval for all high-risk activities. BSA/AML programs
must document risk appetite for customer categories, products, and geographies per
the Interagency Risk Management Guidelines [VERIFY — confirm current OCC guidance].

#### 7b. Risk Appetite Gap Analysis

For each domain, compare residual risk against appetite:

| Domain          | Residual Score | Appetite Threshold | Gap                              | Action Required                         |
| --------------- | -------------- | ------------------ | -------------------------------- | --------------------------------------- |
| Anti-Corruption | 15.0           | 9.0 (HIGH max)     | +6.0 (CRITICAL exceeds appetite) | IMMEDIATE remediation; board escalation |
| Data Privacy    | 6.4            | 8.0 (MEDIUM max)   | Within appetite                  | Enhanced KRI monitoring                 |
| [Etc.]          |                |                    |                                  |                                         |

**Appetite Outlier Definition**: A domain where residual risk exceeds appetite threshold
by more than **2 residual score points** is an appetite outlier requiring board decision:

- Accept temporarily pending remediation (time-limited board approval required)
- Reject and remediate immediately
- Transfer risk (insurance, contractual indemnity, exit market/activity)

---

### Step 8: Develop KRI Framework

For each CRITICAL and HIGH domain, define **Key Risk Indicators (KRIs)** — measurable
leading indicators that signal deteriorating risk conditions before a compliance failure
occurs.

#### 8a. KRI Design Principles

A well-designed KRI must be:

- **Leading** (predicts risk escalation, not lagging/historical)
- **Measurable** (quantifiable; not qualitative or subjective)
- **Timely** (data available within the monitoring period)
- **Actionable** (when threshold is breached, a specific action is triggered)
- **Linked** to the residual risk (its movement correlates to residual risk trajectory)

#### 8b. KRI Framework per Domain (Reference Examples)

| Domain           | KRI                                                                            | Green Threshold | Yellow Warning | Red Alert | Monitoring Frequency | Owner           |
| ---------------- | ------------------------------------------------------------------------------ | --------------- | -------------- | --------- | -------------------- | --------------- |
| Anti-Corruption  | % of third-party agents with completed due diligence on file                   | ≥95%            | 85–95%         | <85%      | Monthly              | CCO             |
| Anti-Corruption  | % of high-risk employees with annual FCPA training completed                   | ≥98%            | 90–98%         | <90%      | Quarterly            | Compliance      |
| AML/CTF          | Transaction monitoring alert closure rate within 30 days                       | ≥90%            | 75–90%         | <75%      | Monthly              | BSA Officer     |
| AML/CTF          | % of new customer CDD completed before first transaction                       | ≥99%            | 95–99%         | <95%      | Weekly               | Compliance      |
| Data Privacy     | % of DSARs responded to within regulatory deadline (30 days GDPR)              | ≥99%            | 95–99%         | <95%      | Monthly              | Privacy Officer |
| Data Privacy     | # of unresolved high/critical findings from last data protection audit         | 0               | 1–2            | 3+        | Quarterly            | Privacy Officer |
| Sanctions        | % of transaction screening false positive rate staying within model parameters | ≤5%             | 5–10%          | >10%      | Daily                | Compliance      |
| Cybersecurity    | % of critical vulnerabilities patched within 30 days of identification         | ≥95%            | 80–95%         | <80%      | Monthly              | CISO            |
| Competition      | # of active internal investigations for potential competition concerns         | 0               | 1              | 2+        | Quarterly            | Legal           |
| ESG/Supply Chain | % of Tier 1 suppliers with current ESG/human rights assessment on file         | ≥90%            | 75–90%         | <75%      | Semi-annual          | Procurement     |

**⟁ CLARIFY** — For each CRITICAL domain: _"Do you have existing reporting on [KRI]?
If not, what data source would make this measurable within your current systems?"_

#### 8c. KRI Escalation Protocol

Define the escalation chain for each Red Alert KRI breach:

1. Compliance officer or domain owner: immediate notification + root cause analysis
2. CCO: escalation report within 5 business days
3. Audit Committee: included in next scheduled meeting agenda
4. Board: escalation within 30 days if not remediated

---

### Step 9: Trend Analysis and Benchmarking

#### 9a. Trend Analysis

For each domain assessed in a prior period, calculate the **risk trajectory**:

| Domain          | Prior Residual (date) | Current Residual | Change | Trajectory  |
| --------------- | --------------------- | ---------------- | ------ | ----------- |
| Anti-Corruption | 12.0 (Q4 2024)        | 15.0 (Q1 2025)   | +3.0   | ⬆ WORSENING |
| Data Privacy    | 7.0 (Q4 2024)         | 6.4 (Q1 2025)    | -0.6   | ⬇ IMPROVING |
| [Etc.]          |                       |                  |        |             |

**Trajectory Definitions:**

- **IMPROVING**: Residual score decreased by >0.5 since last assessment
- **STABLE**: Residual score within ±0.5 of last assessment
- **WORSENING**: Residual score increased by >0.5 since last assessment
- **NEW**: Domain assessed for the first time; no prior comparison

**Flag for board** any domain where trajectory is WORSENING and residual exceeds appetite.

#### 9b. Enforcement Benchmarking

Provide regulatory enforcement context to validate residual risk classifications.
This calibrates whether the organization's exposure is above, at, or below industry
baseline.

Key enforcement data points (verify currency against authoritative sources):

**Anti-Corruption / FCPA:**

- 2024 DOJ enforcement: 7 FCPA corporate resolutions; average penalty $56M [VERIFY]
- Highest single penalty 2020–2024: Goldman Sachs $2.9B (2020) [VERIFY currency]
- DOJ ECCP Sept 2024: Increased focus on AI-generated false approvals and third-party
  intermediary screening adequacy

**AML/CTF:**

- 2024 US: Transaction monitoring penalties $3.3B+ (100% YoY increase); top violators
  in financial services and crypto [VERIFY — Fenergo 2025 report]
- EU AMLR 2024: New harmonized regime effective 2027; anticipated enforcement 2027–2028

**Data Privacy / GDPR:**

- 2024 GDPR enforcement: Top 10 fines exceeded €1.1B total; Ireland DPC active (Meta,
  LinkedIn); EDPB consistency mechanism increasing cross-border enforcement [VERIFY]
- 2025 trend: Consent-or-pay models, cookie compliance, cross-border transfers under
  active scrutiny (EDPB 2025 work programme)

**[VERIFY all enforcement statistics before board presentation — enforcement data changes
frequently and specific figures should be confirmed against current authoritative sources.]**

---

### Step 10: Produce Board-Ready Risk Assessment Report

**⟁ CLARIFY** — Report format. Choose one:

1. **Board Risk Summary** — 2-3 pages; executive heat map; top 5 risks; appetite
   comparison; KRI dashboard; recommended board decisions. Suitable for board presentation.

2. **Full Assessment Report** — Complete risk register; all domain narratives; control
   effectiveness evidence; KRI framework; remediation roadmap; Glass Box audit trail.
   Suitable for Audit Committee, CCO, and regulatory examination purposes.

3. **ISO 37301 / DOJ ECCP Documentation Package** — Structured to satisfy ISO 37301
   Clause 6.1.2 risk assessment requirements and demonstrate DOJ ECCP "well-designed"
   criterion. Includes regulatory citation index and evidence map.

_For batch runs, produce all three if no preference specified._

Structure the output per the **Output Format Template** section below.

---

### Step 11: Quality Verification

Before delivering any output, run all quality checks below. If any check fails, revise
and re-verify before delivery.

#### 11a. PDCA Quality Cycle

**PLAN**: Identify regulatory scope, geographic footprint, operating mode, and risk
appetite reference point. Confirm all applicable frameworks from Step 3. Identify
which inherent risk domains are CRITICAL/HIGH (these require self-interrogation).

**DO**: Execute inherent risk scoring with written rationale for each score. Evaluate
control effectiveness using the MINIMUM CONTROL SCORE rule. Calculate residual risk.
Apply Design-Operation Gap multiplier where applicable.

**CHECK**: Run the 5 Citation Quality Gates below. Apply Self-Interrogation to all
CRITICAL and HIGH residual risks. Verify all regulatory citations against authoritative
sources where accessible. Confirm all applicable domains (from Step 3) are addressed.

**ACT**: Note any gaps in evidence that require follow-up control testing. Identify
domains where KRI data is unavailable and flag for data source development. Update
the Glass Box audit trail to reflect any revisions made during the CHECK phase.

#### 11b. Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                                                                         | Fail Action                                                                                                                                  |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Source**     | Every risk score cites (a) inherent risk driver with source evidence, and (b) control effectiveness with test/audit reference or explicit [ASSUMED] notation | Add citation or mark `[EVIDENCE MISSING — control testing required]`                                                                         |
| **Format**     | All regulatory citations use jurisdiction-standard format (15 U.S.C., 45 C.F.R., Reg. EU 2016/679, SI 2017/692)                                              | Fix format inconsistencies across all regulatory references                                                                                  |
| **Currency**   | Every cited regulatory provision checked for amendments, pending NPRMs, or replacement                                                                       | Mark `[CHECK CURRENCY]` for any provision that may have changed since last verification; mark `[PROPOSED — not yet final]` for pending rules |
| **Domain**     | Risk classifications stay within each domain's applicable regulatory framework; no cross-jurisdiction contamination without [JURISDICTION-SPECIFIC] labeling | Remove or clearly label any cross-jurisdiction assumptions                                                                                   |
| **Confidence** | All uncertainty explicitly stated; no hidden caveats in risk scoring; every ASSUMED score is labeled [ASSUMED]                                               | Rewrite any score that presents uncertain evidence as settled; add confidence qualifier                                                      |

#### 11c. Confidence Scoring

Apply to each key risk classification and residual risk score:

| Level         | Meaning                                                                                                                                             | Notation     | Action                                                                                              |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------------------------------------------------------------------------------------------- |
| **VERIFIED**  | Evidence gathered directly from control testing, audit reports, regulatory filings, or authoritative regulatory text (within 12 months)             | `✓ VERIFIED` | Use as-is in board reports and regulatory submissions                                               |
| **LIKELY**    | Scoring inferred from secondary evidence (industry benchmarks, regulatory guidance, prior audit findings); reasonable professional judgment applied | `[LIKELY]`   | Flag for confirmation in next control testing cycle; acceptable for board reporting with disclosure |
| **[VERIFY]**  | Scoring based on assumptions not yet validated; regulatory citations unconfirmed                                                                    | `[VERIFY]`   | Require primary evidence before board presentation; disclose assumption explicitly                  |
| **[ASSUMED]** | Fallback scoring using conservative defaults; user has acknowledged the assumption applies                                                          | `[ASSUMED]`  | State assumption clearly in risk narrative; recommend targeted control testing to validate          |

---

## Risk Categories — Deep Analysis Framework

For each applicable domain, the assessment should analyze these dimensions:

### Domain 1: Anti-Corruption / Anti-Bribery

**Regulatory Basis:** FCPA 15 U.S.C. §§78dd-1, 78dd-2, 78dd-3, 78m(b) (books and
records); UK Bribery Act 2010 §§1–7, 14 (corporate offence); OECD Anti-Bribery
Convention 1997; local anti-bribery statutes (Brazil LACF No. 12.846/2013; France
Sapin II Law 2016; Germany § 299 StGB). [VERIFY currency]

**Inherent Risk Drivers:**

- Operations in jurisdictions with Corruption Perceptions Index (CPI) <50
  [VERIFY current Transparency International rankings]
- Revenue through third-party intermediaries (agents, distributors, JV partners)
- Government contracting or licensing activities
- Industry classification (pharmaceutical/healthcare, defense, energy/extractives,
  telecoms historically high FCPA exposure)
- Prior enforcement history in same industry/geography

**Key Controls:**

- Anti-corruption policy and Code of Conduct (DE assessment)
- Third-party due diligence program: risk-tiering, enhanced due diligence procedures,
  monitoring (OE assessment)
- Training program: scope (all employees vs. high-risk), frequency, completion rates
- Gifts, hospitality, and entertainment pre-approval process
- Confidential reporting mechanism with non-retaliation protection
- Books and records internal controls per FCPA §78m(b) [JURISDICTION-SPECIFIC: US]

[JURISDICTION-SPECIFIC: UK] UK Bribery Act §7 adequate procedures defence requires
proportionate procedures, top-level commitment, risk assessment, due diligence,
communication, monitoring and review. Corporate offence applies even without senior
management knowledge or approval (strict liability subject to adequate procedures
defence). Facilitation payments not permitted (unlike FCPA).

### Domain 2: AML / Counter-Terrorist Financing

_(Cross-reference `legalcode-aml-kyc-compliance` for deep assessment)_

**Regulatory Basis:** BSA 31 U.S.C. §§5311–5336 + FinCEN regulations 31 C.F.R. Parts
1010–1030; EU AMLR 2024/1624 (from July 2027; currently AMLD6 2018/1673); UK POCA 2002
ss.327–333, TACT 2000, MLR 2017 SI 2017/692; FATF 40 Recommendations.

**Inherent Risk Drivers:** Financial products/services; customer risk (PEP exposure,
high-risk jurisdictions, cash-intensive businesses); transaction risk (wire volume,
cross-border, crypto); geographic risk (FATF high-risk jurisdictions, OFAC nexus).

**Key Controls:** CDD/EDD program; transaction monitoring system calibration; SAR
filing process; CTR compliance [US]; independent audit of AML program.

### Domain 3: Sanctions Compliance

**Regulatory Basis:** OFAC 50 U.S.C. §§1701–1706 (IEEPA) + program-specific regulations
31 C.F.R. Parts 500–600; EU Council Regulations (Russia: 833/2014, 269/2014; Iran:
267/2012); UK Sanctions and Anti-Money Laundering Act 2018. Strict liability for most
violations; no knowledge requirement.

**Key Controls:** Sanctions screening system (coverage of SDN/OFAC lists, EU/UK lists,
UN lists); 50% Rule [VERIFY — OFAC guidance on entities 50%+ owned by SDN]; transaction
screening vs. customer screening coverage; escalation procedures for blocked transactions.

### Domain 4: Data Privacy

_(Cross-reference `legalcode-gdpr-legal-basis-assessment`, `legalcode-dpia-generator`,
`legalcode-vendor-privacy-assessment` for deep assessments)_

**Regulatory Basis:** GDPR Reg. 2016/679; UK GDPR and DUA Act 2025; CCPA/CPRA Cal. Civ.
Code §1798.100 et seq.; LGPD Brazil Lei No. 13.709/2018; DPDP India 2023 (Rules 2025,
compliance deadline May 2027). [JURISDICTION-SPECIFIC: apply all applicable regimes]

**Key Controls:** Privacy notice and consent mechanisms; data subject rights request
fulfillment process; DPA/DPA review for processors; cross-border transfer mechanisms
(SCCs, adequacy, BCRs); data retention and deletion procedures; DPIA process for high-
risk processing; breach notification procedures.

### Domain 5: Cybersecurity

_(Cross-reference `legalcode-nist-csf-mapping`, `legalcode-nis2-compliance-assessment`)_

**Regulatory Basis:** NIS2 Directive 2022/2555 Art. 21 (10 minimum measures); NIST CSF
2.0 (voluntary but DOJ ECCP examines); ISO/IEC 27001:2022; HIPAA 45 C.F.R. §164.306
(healthcare); DORA Reg. 2022/2554 (financial); FTC Safeguards Rule 16 C.F.R. Part 314.

**Key Controls:** Risk management framework; access controls (MFA, privileged access);
incident response plan; business continuity/disaster recovery; vulnerability management;
cryptography policy; supply chain security; security awareness training.

### Domain 6–15: Additional Risk Domains

_Apply the same inherent risk driver + key control framework for each applicable domain
from the Regulatory Applicability Matrix (Step 3). The assessment template from
Step 5b provides the structure; populate with domain-specific regulatory basis,
inherent risk drivers, and key controls._

For each domain not fully analyzed in this skill, cross-reference the dedicated
Legalcode skills:

- **Export Controls**: Research EAR/ITAR classification; assess denied party screening;
  license determination process; [JURISDICTION-SPECIFIC: EU Dual-Use Regulation]
- **Employment / Labor**: See `legalcode-employee-handbook-review`,
  `legalcode-independent-contractor-classification`
- **Competition / Antitrust**: Assess internal compliance program for price-fixing
  risk; dominance/abuse reviews; M&A HSR/EU merger filing compliance
- **Tax**: Transfer pricing documentation; Country-by-Country Reporting;
  OECD Pillar Two (Global Minimum Tax, effective for large MNEs)
- **ESG / Supply Chain**: CSDDD due diligence program (phased EU companies 2027+);
  UK/Australian Modern Slavery Act reporting; CSRD sustainability reporting
- **AI / Emerging Technology**: EU AI Act conformity assessment for high-risk systems;
  see `legalcode-eu-ai-act-high-risk-compliance`, `legalcode-ai-governance-framework-builder`

---

## Risk Appetite Framework Reference

When no board-approved risk appetite statement exists, these **conservative defaults**
apply as a starting baseline for board discussion:

| Risk Appetite Dimension                        | Conservative Default                                              | Board Decision Point                                                              |
| ---------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Maximum acceptable residual risk (any domain)  | MEDIUM (score ≤8)                                                 | "We accept residual risk up to MEDIUM with KRI monitoring"                        |
| CRITICAL residual risk tolerance               | Zero tolerance; immediate escalation                              | "Any CRITICAL residual requires board resolution within 30 days"                  |
| High-corruption-risk third-party relationships | Only with enhanced DD + contractual FCPA reps/warranties          | "Documented due diligence required for all high-risk third parties"               |
| Data privacy risk appetite                     | MEDIUM maximum (regulatory fines can reach 4% of global turnover) | "We accept MEDIUM residual privacy risk with DPA coverage and quarterly KRI"      |
| Cybersecurity incident risk                    | MEDIUM maximum (operational and regulatory disruption)            | "We accept MEDIUM residual cyber risk with ISO 27001 or NIST CSF Tier 3 controls" |

**Risk Tolerance Guidance:**

- Risk Appetite = the aspired maximum residual risk level (set by board policy)
- Risk Tolerance = the acceptable variance above appetite before escalation
- When residual risk > appetite + tolerance: mandatory board escalation

---

## Anti-Patterns

Explicit catalogue of what NOT to do in compliance risk assessment:

1. **Scoring residual risk without isolating inherent risk** — Inherent risk must be
   assessed assuming ALL controls are absent. A commonly observed error is implicitly
   crediting controls during inherent risk scoring (e.g., "We encrypt data so our
   inherent privacy risk is only Medium"). Inherent risk is the raw regulatory exposure;
   controls reduce it to residual risk. Conflating the two undermines the assessment.

2. **Averaging control effectiveness scores** — A domain with three controls rated 5,
   5, and 1 does not have average OE of 3.67. The weakest control determines domain
   effectiveness. A single Level 1 control (e.g., no incident response procedure in a
   domain with strong access controls) can turn a LOW residual into CRITICAL.

3. **Scoring operating effectiveness from design alone** — An approved policy with no
   evidence of operation should be scored OE Level 1–2, not Level 4–5. Design
   Effectiveness and Operational Effectiveness are distinct questions. "We have a policy"
   answers the first question. "We can demonstrate the policy is being followed" answers
   the second.

4. **Ignoring the Design-Operation Gap** — When DE = 5 and OE = 1, the control is
   designed correctly but not executed. This is a higher-risk situation than DE = OE = 2
   (consistently weak) because it indicates management awareness of the requirement
   without operational follow-through — a pattern examiners and prosecutors flag.

5. **One-size-fits-all risk scoring** — Applying the same inherent risk score to a
   financial services firm and a technology startup for AML risk ignores that the
   regulatory obligation itself is entirely different. Regulatory applicability must be
   correctly scoped before inherent risk scoring begins.

6. **Residual risk that consistently equals risk appetite** — If every domain produces a
   residual risk score that perfectly meets the appetite threshold, this signals the
   scoring was calibrated to match appetite rather than derived from evidence. An honest
   assessment will produce some domains above appetite (requiring remediation) and some
   below (demonstrating control strength). Suspiciously uniform outputs warrant
   re-interrogation.

7. **Static risk appetite without KRI escalation triggers** — A risk appetite statement
   without corresponding KRI thresholds is aspirational, not operational. Risk appetite
   must be operationalized: "When KRI X drops below threshold Y, the residual risk for
   domain Z escalates from MEDIUM to HIGH, triggering the following response..."

8. **KRIs that are lagging indicators only** — Reporting the number of regulatory fines
   received last year is a lagging indicator of past failures, not a leading indicator
   of future risk. Effective KRIs predict deteriorating conditions before failures occur
   (e.g., declining training completion rates, rising policy exception requests, aging
   audit findings).

9. **Regulatory citation without currency verification** — Enforcement priorities,
   penalty thresholds, and regulatory interpretations change. A risk assessment that
   cites enforcement penalties from three years ago without verifying current levels
   may materially understate or overstate impact scores. All enforcement data and
   regulatory citations should be marked with a verification date.

10. **Third-party risk scored as organizational risk** — Third-party compliance failures
    can create direct liability for the organization (FCPA third-party, GDPR joint
    controller, AML vendor obligation). Third-party risk must be separately assessed
    against the organization's due diligence program, not subsumed into the organization's
    own inherent risk score.

11. **Board presentation of unverified CRITICAL findings** — Presenting a CRITICAL
    residual risk to the board without completing the Self-Interrogation 3-pass review
    may create unnecessary alarm or trigger overreaction. Equally, presenting CRITICAL
    risks without board escalation violates ISO 37301 Clause 9.1.2 and DOJ ECCP
    expectations. Both errors are harmful; the 3-pass review exists to calibrate
    classification accuracy before presentation.

12. **Missing cross-risk dependencies** — Some risks amplify each other. Weak AML
    controls plus weak sanctions screening creates a combined exposure greater than either
    in isolation. Weak GDPR controls plus weak incident response creates heightened data
    breach exposure. Cross-risk dependency analysis prevents underestimating correlated
    risk pockets.

13. **Trend analysis omitted** — A point-in-time residual risk score is insufficient for
    board risk governance. Without trend analysis, the board cannot determine whether
    the compliance function is improving or deteriorating. ISO 37301 Clause 9.1 and
    DOJ ECCP both evaluate whether controls are improving over time.

14. **Substituting self-assessment for independent testing** — Management self-assessment
    of control effectiveness systematically overstates OE levels due to optimism and
    confirmation bias. For CRITICAL and HIGH domains, independent evidence (audit report,
    external assessment, regulator finding) is required to achieve a VERIFIED confidence
    level. Self-assessment alone supports only LIKELY or [ASSUMED] confidence.

15. **Scope limited to the organization without third-party lens** — Modern compliance
    risk increasingly flows through supply chains, fintech partnerships, and API
    integrations. An assessment that covers only the organization's own operations
    without mapping third-party relationships will materially understate AML, FCPA,
    sanctions, and cybersecurity exposures.

16. **Jurisdiction bleed** — Applying GDPR-style consent requirements to a purely US-
    domestic operation, or applying FCPA strict liability to a UK-only entity without US
    nexus. Regulatory applicability must be correctly scoped first; then inherent risk
    follows. Jurisdiction bleed overstates or understates inherent risk depending on
    direction.

17. **Ignoring enforcement context** — Failing to benchmark the organization's residual
    risk against industry enforcement patterns. An organization with AML residual score
    of 8 (MEDIUM) in an industry where regulators have issued $3B in AML penalties in
    the past year is exposed differently than the same score in an industry with no
    recent enforcement. Enforcement benchmarking is a required element of DOJ ECCP
    risk assessment adequacy.

18. **Remediation roadmap without owners or deadlines** — A risk assessment that
    identifies CRITICAL gaps but produces a remediation list without named owners,
    specific deadlines, and success metrics is not actionable. DOJ ECCP evaluates
    whether remediation is "adequately resourced and empowered to work in practice."
    Generic "improve controls" recommendations fail this test.

19. **Assessing risk domains in isolation from business strategy** — Compliance risk
    assessment should be integrated with COSO ERM — risks are assessed in the context
    of the organization's strategic objectives. A new market entry into a high-CPI
    country raises inherent anti-corruption risk specifically because of the strategic
    decision. The assessment must track organizational change triggers.

20. **Delivering without Glass Box audit trail** — An assessment that identifies CRITICAL
    residual risks without a traceable, auditable reasoning trail exposes the CCO and
    board to credibility challenges in enforcement proceedings. The Glass Box audit trail
    documents how every finding was derived, what evidence it is based on, and what
    assumptions were made. In DOJ ECCP evaluations, this documentation is the difference
    between a "well-designed" risk assessment and an undocumented guess.

---

## Writing Standards

Apply plain-language discipline to all output:

**For executive summary and board presentation:**

- Plain language; no legal jargon
- Active voice: "The anti-corruption controls are insufficient" not "Insufficiency in
  anti-corruption controls has been identified"
- Short sentences; one point per sentence
- Name the actor and the action: "The CCO must remediate the third-party due diligence
  gap within 30 days" not "The third-party due diligence gap requires remediation"
- Specific quantification: "Residual risk score 15.0 (CRITICAL; appetite 9.0)" not
  "high residual risk"

**For technical risk register:**

- Include all scoring rationale, evidence references, and confidence levels
- All [VERIFY] and [ASSUMED] tags visible (not hidden in footnotes)
- Glass Box audit trail appended to final report

**Quality gates before delivery:**

1. Can a non-compliance board member understand the executive summary in 5 minutes?
2. Are all CRITICAL findings self-interrogated and evidence-supported?
3. Is every regulatory citation marked as VERIFIED, LIKELY, [VERIFY], or [ASSUMED]?
4. Does the remediation roadmap include a named owner and specific deadline for every
   CRITICAL and HIGH finding?
5. Has the Glass Box audit trail been completed with frameworks, assumptions, and
   confidence levels documented?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool
for verifying regulatory citations, current enforcement data, and emerging developments.

**With legalcode-mcp connected (preferred):**

- In Step 3, search for current regulatory requirements and most recent guidance updates
  for each applicable framework
- In Step 4, verify current enforcement penalty ranges and recent enforcement actions
  to calibrate Impact scores
- Save key findings to `/tmp/legalcode-compliance-risk-research.md`
- Mark all legalcode-mcp-sourced citations as `✓ VERIFIED` in the Glass Box audit trail
- For domains where recent regulatory changes affect inherent risk, search for the
  specific amendment or enforcement action date

**Without legalcode-mcp:**

- Mark all regulatory references with `[VERIFY]` and note in the Glass Box audit trail:
  `legalcode_mcp: "Not connected — all citations require independent verification"`
- Note prominently in the output that enforcement data and regulatory citations require
  independent verification before board presentation or regulatory submission
- Focus the assessment on structural risk analysis and control effectiveness evaluation
  rather than regulatory substance depth

---

## Output Format Template

Structure the final assessment report as:

```markdown
# Compliance Risk Assessment

**Organization**: [Name]
**Assessment Date**: [YYYY-MM-DD]
**Assessment Scope**: [Annual Enterprise / Focused Domain / Pre-Examination / etc.]
**Operating Mode**: [Full Assessment with Roadmap / Risk Quantification Only / ISO 37301 Package]
**Frameworks Applied**: [ISO 37301, DOJ ECCP 2024, COSO ERM, ISO 31000, ...]
**Prepared by**: AI-assisted | Reviewed by: **\*\***\_\_\_**\*\***
**Next Scheduled Review**: [date]

---

## Executive Summary

[One-paragraph summary of overall compliance risk posture: total domains assessed,
number CRITICAL/HIGH/MEDIUM/LOW, enterprise residual risk score, comparison to appetite,
top 3 priority actions]

### Risk Posture Scorecard

| Metric                                        | Value                            | vs. Prior Period   | vs. Appetite              |
| --------------------------------------------- | -------------------------------- | ------------------ | ------------------------- |
| Domains Assessed                              | [N]                              | —                  | —                         |
| CRITICAL Residual Risks                       | [N]                              | [+/-N vs. Q4 2024] | Not acceptable            |
| HIGH Residual Risks                           | [N]                              |                    | Requires remediation plan |
| MEDIUM Residual Risks                         | [N]                              |                    | Within appetite with KRI  |
| LOW Residual Risks                            | [N]                              |                    | Acceptable                |
| Enterprise Residual Risk Score (weighted avg) | [X.X]                            | [+/-X.X]           | Appetite: [X.X]           |
| Trend                                         | [IMPROVING / STABLE / WORSENING] |                    |                           |

### Top 3 Priority Actions

| Priority | Domain   | Finding        | Owner        | Deadline | Post-Remediation Residual |
| -------- | -------- | -------------- | ------------ | -------- | ------------------------- |
| 1        | [Domain] | [One-line gap] | [Name/Title] | [Date]   | [Projected score]         |
| 2        |          |                |              |          |                           |
| 3        |          |                |              |          |                           |

---

## Regulatory Applicability Summary

[Regulatory Applicability Matrix from Step 3b]

---

## Overall Risk Heat Map

| Domain              | Inherent (1–25) | OE Level | Residual (1–25) | Tier        | Trend |
| ------------------- | --------------- | -------- | --------------- | ----------- | ----- |
| Anti-Corruption     |                 |          |                 | 🔴/🟠/🟡/🟢 | ⬆/➡/⬇ |
| AML/CTF             |                 |          |                 |             |       |
| Sanctions           |                 |          |                 |             |       |
| Data Privacy        |                 |          |                 |             |       |
| Cybersecurity       |                 |          |                 |             |       |
| Export Controls     |                 |          |                 |             |       |
| Employment          |                 |          |                 |             |       |
| Competition         |                 |          |                 |             |       |
| Tax                 |                 |          |                 |             |       |
| ESG/Supply Chain    |                 |          |                 |             |       |
| Financial Reporting |                 |          |                 |             |       |
| AI/Emerging Tech    |                 |          |                 |             |       |
| Third-Party Risk    |                 |          |                 |             |       |

---

## Domain-by-Domain Risk Analysis

### [Domain Name] — [CRITICAL 🔴 / HIGH 🟠 / MEDIUM 🟡 / LOW 🟢] | Residual: [X.X] | Confidence: [VERIFIED/LIKELY/VERIFY/ASSUMED]

**Inherent Risk Assessment**

- Likelihood: [1–5] — [Written rationale citing specific organizational drivers]
- Impact: [1–5] — [Written rationale citing applicable penalties and exposure]
- Inherent Risk Score: [L×I = score]
- Confidence: [VERIFIED / LIKELY / [VERIFY] / [ASSUMED]] — [basis]

**Control Effectiveness Assessment**

| Control             | Design (1–5) | Operating (1–5) | Testing Evidence | Confidence |
| ------------------- | ------------ | --------------- | ---------------- | ---------- |
| [Control 1]         |              |                 | [Source + date]  |            |
| [Control 2]         |              |                 |                  |            |
| Domain OE (MINIMUM) | —            | **[X]**         |                  |            |

**Design-Operation Gap**: [Yes/No — if Yes, DE-OE = [X]; 1.25× multiplier applied]

**Residual Risk Calculation**

- Formula: [Inherent] × (1 − [OE]/5) [× 1.25 if D-O Gap] = [Residual]
- Residual Risk Score: [X.X] → **[CRITICAL / HIGH / MEDIUM / LOW]**

**Self-Interrogation** (CRITICAL/HIGH only)

- Pass 1 — Risk Chain Integrity: [Assessment + conclusion]
- Pass 2 — Compensating Controls: [Assessment + conclusion]
- Pass 3 — Regulatory Context: [Enforcement benchmarking + conclusion]
- Outcome: `self_interrogation: PASS | REVISED — [reason if revised]`

**Risk Appetite Comparison**

- Board Appetite: [X.X]
- Current Residual: [X.X]
- Status: [Within appetite / Exceeds by X.X / Appetite outlier]

**Key Risk Indicators**

| KRI     | Green | Yellow | Red | Frequency | Owner   | Current Status |
| ------- | ----- | ------ | --- | --------- | ------- | -------------- |
| [KRI 1] | ≥X%   | X–Y%   | <X% | Monthly   | [Owner] | [Current data] |

**Remediation Actions** (if CRITICAL or HIGH)

| Action     | Priority  | Owner  | Deadline | Est. Post-Remediation Residual |
| ---------- | --------- | ------ | -------- | ------------------------------ |
| [Action 1] | IMMEDIATE | [Name] | [Date]   | [Score]                        |

---

## Risk Appetite vs. Actual Exposure

[Appetite comparison table with outliers highlighted; board decision items]

---

## Remediation Roadmap

| Domain | Finding | Action | Priority             | Owner | Deadline | Success Metric | Est. Residual Post |
| ------ | ------- | ------ | -------------------- | ----- | -------- | -------------- | ------------------ |
|        |         |        | IMMEDIATE (0–30d)    |       |          |                |                    |
|        |         |        | NEAR-TERM (30–90d)   |       |          |                |                    |
|        |         |        | BACKGROUND (90–180d) |       |          |                |                    |

---

## Board Decisions Required

1. [Decision 1 — e.g., Accept residual risk [X.X] in [domain] pending remediation?]
   [ ] Accept with remediation plan [ ] Reject — immediate remediation required
   [ ] Transfer (insurance/contract) [ ] Exit activity/market

2. [Decision 2 — e.g., Approve remediation budget of $[X]?]
   [ ] Approve [ ] Modify to $[X] [ ] Defer

---

## Glass Box Audit Trail

[YAML block per template below]
```

---

## Glass Box Audit Trail Template

```yaml
glass_box:
  skill_name: "legalcode-compliance-risk-assessment"
  assessment_date: "[YYYY-MM-DD]"
  organization_profile: "[Industry, size, footprint — one line]"
  assessment_scope: "[Annual Enterprise / Focused / Pre-Examination / Trigger]"
  operating_mode: "[Risk Quantification / Quantification + Roadmap / ISO 37301 Package]"

  frameworks_applied:
    - "ISO 37301:2021 Clause 6.1.2 — [VERIFIED / [VERIFY]]"
    - "DOJ ECCP September 2024 — [VERIFIED / [VERIFY]]"
    - "COSO ERM Framework 2017 — [VERIFIED / [VERIFY]]"
    - "ISO 31000:2018 — [VERIFIED / [VERIFY]]"
    - "[Additional frameworks as applicable]"

  domains_assessed: "[N domains from Step 3 Regulatory Applicability Matrix]"
  domains_critical: "[N]"
  domains_high: "[N]"
  domains_medium: "[N]"
  domains_low: "[N]"

  control_testing_depth: "[Desktop Review / Light Testing / Comprehensive Testing]"
  risk_appetite_source: "[Board-approved statement / Conservative defaults / Provided by user]"

  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "[/tmp/legalcode-compliance-risk-research.md / Not created]"

  self_interrogation_applied_to:
    - "[Domain 1 — PASS]"
    - "[Domain 2 — REVISED — reason]"

  confidence_summary:
    verified_scores: "[N out of total]"
    likely_scores: "[N]"
    verify_needed: "[N]"
    assumed_scores: "[N]"

  design_operation_gaps:
    - "[Domain where DE-OE ≥ 2 — multiplier applied]"

  key_assumptions:
    - "[Assumption 1 — e.g., 'US + EU footprint assumed based on [context]']"
    - "[Assumption 2 — e.g., 'No board-approved risk appetite statement — conservative defaults applied']"

  enforcement_data_verification:
    all_penalty_figures_marked: "[VERIFIED / [VERIFY]]"
    data_currency_confirmed_as_of: "[date or 'Not confirmed']"

  limitations:
    - "[Any scope limitations, exclusions, or caveats]"
    - "[Control testing not performed; all OE scores require validation]" # include if desktop review only

  reviewer: "AI-assisted — requires qualified legal and compliance professional review before board presentation or regulatory submission"
  next_assessment_recommended: "[Annual / Semi-annual / Trigger-based]"
```

---

## Localization Notes

This skill is jurisdiction-agnostic by design. When creating jurisdiction-specific
variants:

1. Replace [JURISDICTION-SPECIFIC] markers with verified local regulatory requirements
2. Replace [VERIFY] tags with confirmed statutory references from legalcode-mcp or
   authoritative national regulatory sources
3. Add jurisdiction-specific inherent risk drivers (e.g., UK: SFO prosecutorial posture;
   Germany: NIS2UmsuCG December 2025 BSI registration requirements; France: Sapin II
   Agence Française Anticorruption audit requirements)
4. Update enforcement benchmarking data with local regulator enforcement statistics
5. Adjust control standards to local professional guidance (e.g., UK: FCA SYSC;
   US financial: OCC Compliance Handbook; AU: ASIC Regulatory Guides)
6. Add jurisdiction-specific KRI thresholds where regulatory safe harbors exist
   (e.g., GDPR DSAR response time KRI: 30-day threshold per Article 12)

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis combining:

- DOJ Evaluation of Corporate Compliance Programs (ECCP) September 2024 risk assessment
  element requirements
- ISO 37301:2021 Clause 6.1.2 risk assessment documentation framework
- COSO ERM Framework (2017) 20-principle structure and likelihood-impact scoring
- ISO 31000:2018 risk management principles
- OCEG Red Book 3.5 GRC capability model
- Legalcode repository quality standards: Citation Quality Gates, Self-Interrogation,
  Confidence Scoring, and Glass Box audit trail from `legalcode-contract-review` and
  `legalcode-compliance-program-builder` reference standards
- Structural analysis from Legalcode agent team (2026-03-02):
  compliance-program-builder patterns + AML/KYC classification system +
  NIST CSF gap severity framework + contract-review quality assurance
- Prompt engineering analysis from Legalcode agent team (2026-03-02):
  HIPAA confidence-gate adaptation + AML self-interrogation adaptation +
  risk-specific anti-patterns (12 items extracted; expanded to 20)
- Web research: DOJ ECCP September 2024 AI/emerging tech risk requirements; COSO ERM
  compliance risk guidance; control effectiveness maturity scoring methodology;
  KRI development best practices; 2024–2025 regulatory penalty enforcement data
- Distinguishes from `legalcode-compliance-program-builder` (program design) by focusing
  on risk quantification, control effectiveness scoring, residual risk calculation,
  and board-ready risk heat mapping as primary outputs
