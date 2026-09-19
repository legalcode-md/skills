---
name: legalcode-sox-compliance-assessment
description: SOX (Sarbanes-Oxley Act of 2002, Pub. Use when a public company must assess readiness for
  annual Section 302/404 certifications, when a material weakness has been identified or disclosed, when
  preparing for PCAOB audit or inspection, when transitioning from private to public company (IPO, de-SPAC),
  when material business changes require ICFR scope updates, or when building a SOX compliance program
  from scratch.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

SOX (Sarbanes-Oxley Act of 2002, Pub. L. 107-204) compliance assessment for SEC-reporting companies covering Section 302 CEO/CFO disclosure controls and procedures (DC&P) certification (17 CFR § 240.13a-14), Section 404(a) management assessment of internal controls over financial reporting (ICFR) under the COSO 2013 Internal Control — Integrated Framework (5 components, 17 principles), Section 404(b) auditor attestation requirements (large accelerated filers and accelerated filers under PCAOB AS 2201), Section 301 audit committee independence and confidential whistleblower complaint procedures, Section 906 criminal certification obligations (18 U.S.C. § 1350), and Section 304/SEC Rule 10D-1 executive compensation clawback. Determines Section 404(b) applicability by filer category: large accelerated filer (≥$700M public float, §404(b) required), accelerated filer ($75M–$700M, §404(b) required), non-accelerated filer/SRC/EGC (§404(b) exempt). Assesses all four IT General Controls (ITGC) domains: access to programs and data, program change management, computer operations, and systems development/implementation. Evaluates SOC 1 Type II report reliance mechanics (SSAE 18/AT-C 320) including complementary user entity controls (CUECs), bridge letters, and carve-out vs. inclusive method for service organizations. Classifies deficiencies using PCAOB AS 2201 terminology: EFFECTIVE / CONTROL DEFICIENCY / SIGNIFICANT DEFICIENCY / MATERIAL WEAKNESS, with automatic Material Weakness triggers for fraud by senior management, prior-period restatement, auditor-detected material misstatement, and ineffective audit committee (AS 2201 §§ 69-70). Covers December 2023 SEC cybersecurity disclosure Rule (Form 8-K Item 1.05, 4-business-day reporting, Form 10-K governance disclosure) and its interaction with ICFR. Produces management's ICFR assessment documentation framework, deficiency remediation roadmap with IMMEDIATE/NEAR-TERM/BACKGROUND prioritization, and an annual SOX compliance calendar. Use when a public company must assess readiness for annual Section 302/404 certifications, when a material weakness has been identified or disclosed, when preparing for PCAOB audit or inspection, when transitioning from private to public company (IPO, de-SPAC), when material business changes require ICFR scope updates, or when building a SOX compliance program from scratch.


# SOX Compliance Assessment

> **Disclaimer**: This skill provides an AI-assisted framework for assessing compliance
> with the Sarbanes-Oxley Act of 2002 (Pub. L. 107-204, 116 Stat. 745), as amended,
> and related SEC rules and PCAOB standards. It does not constitute legal advice,
> accounting advice, audit services, or a compliance certification. SOX requirements,
> SEC rules, PCAOB standards, and enforcement interpretations evolve — verify all
> statutory references, regulatory thresholds, and penalty amounts against current
> sources before relying on them. AI-generated legal and accounting analysis carries
> hallucination risk for cited authority: any Section references, CFR citations, PCAOB
> AS citations, or enforcement precedents should be independently verified by a qualified
> securities attorney, CPA, or SOX compliance professional. This skill does not replace
> management's formal assessment of ICFR, does not constitute an attestation engagement
> under PCAOB standards, and does not replace the independent audit required under
> Section 404(b). It produces a structured framework to support human-led SOX compliance
> work, not a substitute for it.

## Purpose and Scope

This skill assesses an organization's SOX compliance posture across four core domains:
CEO/CFO certifications (Section 302), internal controls over financial reporting (Section
404), audit committee governance (Section 301), and criminal accountability provisions
(Section 906). It supports both initial assessments and annual refresh cycles.

**Covers:**

- Filer category determination (large accelerated filer / accelerated filer / non-accelerated
  filer / SRC / EGC / FPI) and Section 404(b) applicability
- Section 302 disclosure controls and procedures (DC&P) evaluation framework
- COSO 2013 Internal Control — Integrated Framework: all 5 components, 17 principles
- Entity-level controls (ELCs) — the foundation of ICFR
- ICFR scope: significant accounts, locations, processes identification and risk ranking
- Process-level control testing (design effectiveness and operating effectiveness)
- IT General Controls (ITGC) across all four domains
- SOC 1 Type II report reliance: CUEC testing, bridge letters, carve-out/inclusive method
- Audit committee independence, financial expertise, and Section 301 complaint procedures
- Deficiency classification per PCAOB AS 2201 §§ 7-9: control deficiency, significant
  deficiency, material weakness
- Automatic material weakness triggers per AS 2201 §§ 69-70
- Remediation planning and status tracking for previously disclosed deficiencies
- December 2023 SEC cybersecurity disclosure Rule (Form 8-K Item 1.05) ICFR interaction
- Section 304 / SEC Rule 10D-1 executive compensation clawback readiness
- Annual SOX compliance calendar and management's report documentation framework

**Does not:**

- Constitute an audit, review, or attestation — those are regulated services
- Certify SOX compliance — certifications require qualified CPA/auditor engagement
- Provide legal opinions on specific SEC enforcement exposure or securities litigation
- Assess GAAP/IFRS accounting treatment — ICFR controls assume accounting is correct
- Replace the PCAOB-required auditor attestation under Section 404(b)
- Apply to private companies, non-US-listed entities, or entities not required to file
  periodic reports under Section 13(a) or 15(d) of the Exchange Act

**Related skills:**

- `legalcode-compliance-program-builder` — build or assess a holistic corporate compliance
  program incorporating SOX, data privacy, anti-bribery, and trade compliance
- `legalcode-corporate-governance-audit` — broader board governance assessment including
  independence standards, committee structures, and fiduciary duty compliance
- `legalcode-whistleblower-program-builder` — build Section 301(4) SOX whistleblower intake
  system integrated with SEC Dodd-Frank Rule 21F award program
- `legalcode-anti-bribery-compliance` — FCPA/UK Bribery Act books-and-records and internal
  controls provisions that overlap with SOX Section 404 ICFR requirements
- `legalcode-aml-kyc-compliance` — financial institution regulatory compliance with BSA/AML
  that intersects with SOX ICFR for regulated financial companies

---

## Jurisdiction and Governing Law

**Primary legislation**: Sarbanes-Oxley Act of 2002, Pub. L. 107-204, 116 Stat. 745.
Applies to companies that file periodic reports with the SEC under Section 13(a) or 15(d)
of the Securities Exchange Act of 1934 (15 U.S.C. § 78m(a) or § 78o(d)). This includes
most domestic issuers with registered securities and many foreign private issuers (FPIs).

**Primary SEC implementing rules**:

- 17 CFR § 240.13a-14: CEO/CFO certification requirements (Section 302)
- 17 CFR § 240.13a-15: Disclosure controls and procedures
- 17 CFR § 240.13a-15(f): Definition of ICFR
- Regulation S-K Item 308: Management's Report on Internal Control Over Financial Reporting

**PCAOB standards** [binding on registered public accounting firms]:

- AS 2201: An Audit of Internal Control Over Financial Reporting That Is Integrated with
  an Audit of Financial Statements (primary standard for Section 404(b) audits)
- AS 2110: Identifying and Assessing Risks of Material Misstatement
- AS 2301: The Auditor's Responses to the Risks of Material Misstatement
- AS 2401: Consideration of Fraud in a Financial Statement Audit
- AS 2805: Management Representations

**Required control framework**: The SEC has not mandated a specific framework but recognizes
the Committee of Sponsoring Organizations (COSO) 2013 Internal Control — Integrated Framework
as suitable for ICFR assessment and the framework predominantly used in practice. [VERIFY
current SEC guidance on acceptable frameworks — COSO 2013 is the current de facto standard.]

**Enforcement authorities**:

- SEC Division of Enforcement: civil enforcement of Section 302, 404, 409, and related
  Regulation S-K requirements; disgorgement, civil monetary penalties, officer/director bars
- PCAOB: oversight of registered public accounting firms; sanctions, fines [VERIFY current
  maximum: up to $15M per firm and $750K per individual as of 2024, subject to adjustment]
- DOJ (Criminal Division): criminal enforcement of Section 906 (18 U.S.C. § 1350),
  Section 802 document falsification (18 U.S.C. § 1519), Section 1107 retaliation
- Federal courts: private securities actions under Exchange Act Sections 10(b)/Rule 10b-5

**Section 906 criminal penalties** (18 U.S.C. § 1350):
| Violation | Fine | Imprisonment |
|-----------|------|-------------|
| Knowing false certification | Up to $1,000,000 | Up to 10 years |
| Willful false certification | Up to $5,000,000 | Up to 20 years |

---

## Interactive Clarification

This skill uses **⟁ CLARIFY** markers at key decision points. When you encounter a
CLARIFY marker, pause and ask the structured questions shown before proceeding. Only
ask when the answer will materially change the analysis. If context has already been
provided, skip that question and proceed.

**Standard clarification format:**

```
⟁ CLARIFY — [Decision point name]

[Short context: why this question matters]

1. [Option A]: [Description]
2. [Option B]: [Description]
3. [Option C]: [Description]

**Why this matters**: [One sentence on how the answer changes the analysis direction.]
```

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:

- **Company description**: Name, exchange listing, fiscal year end, number of locations,
  significant subsidiaries, business segments, primary technology systems
- **Document set**: Uploaded ICFR documentation, risk assessment matrices, process narratives,
  control matrices (RCM), prior management assessment reports, external auditor findings,
  prior-year 10-K ICFR disclosures, audit committee materials
- **Annual refresh**: Prior assessment findings for update to current-year assessment cycle
- **Deficiency trigger**: Post-material-weakness or post-restatement remediation review
- **IPO/de-SPAC transition**: New public company building SOX compliance from scratch
- **Acquisition integration**: Newly acquired entity requiring SOX scope inclusion assessment

**Minimum required context**: Company name, filer category (or information needed to
determine it), most recent fiscal year end, whether a material weakness was previously
disclosed, and current assessment purpose (readiness / annual / remediation / scope update).

### Step 2: Gather Context

**⟁ CLARIFY** — Gather context before beginning. Ask (skip questions already answered):

1. **Assessment mode**: What is the primary objective?
   - _Annual readiness assessment_: Comprehensive evaluation for upcoming 10-K filing
   - _Mid-year status review_: Quarterly check on ICFR program health (before 10-Q §302
     certifications)
   - _Post-incident assessment_: Following identification of a potential material weakness,
     error, or restatement
   - _IPO/de-SPAC transition readiness_: First-year SOX compliance program build
   - _Acquisition integration scoping_: Assessing whether and how to include acquired entity
     in ICFR scope
   - _Remediation tracking_: Update on previously disclosed significant deficiency or
     material weakness remediation progress
   - **Why this matters**: Assessment mode determines scope depth, output format, and
     whether the Binary Gate applies or can be skipped.

2. **Filer category**: What is the company's SEC filer category?
   - _Large accelerated filer (LAF)_: Public float ≥ $700M as of most recent second fiscal
     quarter — Section 404(b) auditor attestation required
   - _Accelerated filer (AF)_: Public float $75M–<$700M — Section 404(b) required
   - _Non-accelerated filer (NAF)_: Public float < $75M or no public float — Section 404(b)
     exempt
   - _Smaller reporting company (SRC)_: Meets SRC definition (revenues < $250M and public
     float < $700M; or revenues < $100M with no public float) — Section 404(b) exempt
   - _Emerging growth company (EGC)_: JOBS Act 2012 — revenues < $1.235B [VERIFY current
     threshold] in last fiscal year; Section 404(b) exempt for up to 5 fiscal years after IPO
   - _Foreign private issuer (FPI)_: Annual report on Form 20-F; Section 404 equivalent
     obligations with some timeline differences — see Localization Notes
   - _Unknown — need to calculate_: Provide public float, revenue, and filing history
   - **Why this matters**: Filer category determines whether Section 404(b) applies;
     if it does not, the scope of this assessment is limited to management's assessment
     (§404(a)) and auditor attestation steps can be skipped.

3. **COSO framework status**: Has a COSO 2013 framework assessment been conducted?
   - _Yes — documented and current_: Provide documentation; assessment will verify
     and update
   - _Yes — documented but last updated >12 months ago_: Full refresh required
   - _Partial — some components documented, others not_: Identify gaps; targeted assessment
   - _No formal COSO assessment documented_: Build from scratch — this is the highest-risk
     starting point and most common first-year challenge
   - **Why this matters**: Absence of a documented COSO framework assessment is itself
     a potential significant deficiency in the control environment.

4. **Prior deficiencies**: Were any deficiencies disclosed in the most recent annual report?
   - _No — clean ICFR opinion_: Confirm control environment stability and address any
     new risks
   - _Significant deficiency disclosed (not material weakness)_: Track remediation status;
     assess whether remediation has been tested for operating effectiveness
   - _Material weakness disclosed_: Highest priority — assess remediation completion and
     operating effectiveness re-testing before next §302 certification
   - _Restatement occurred_: Document root cause; assess ICFR scope adequacy; management
     certification process implications
   - **Why this matters**: Previously disclosed deficiencies require remediation evidence
     before management can conclude ICFR is effective.

5. **IT environment**: What is the primary technology architecture?
   - _On-premises ERP (SAP/Oracle/Microsoft Dynamics)_: Standard ITGC assessment
   - _Cloud ERP (Workday/NetSuite/Sage Intacct/SAP S/4HANA Cloud)_: Cloud ITGC assessment
     with SOC 1 reliance; shared responsibility model analysis required
   - _Hybrid (on-premises + cloud systems)_: Both assessment streams required
   - _Multiple ERPs (common in M&A situations)_: Map by significant account to identify
     which systems fall in ICFR scope
   - **Why this matters**: Cloud and hybrid environments change the ITGC assessment
     methodology and trigger SOC 1 reliance review.

6. **External auditor relationship**: What is the current relationship with the external auditor?
   - _Integrated audit (§404(b) applicable)_: Coordinate assessment scope with PCAOB AS 2201
     requirements; auditor will rely on management's work to the extent it is reliable
   - _Financial statement audit only (§404(b) not applicable)_: Management assessment scope
     is independent; external audit does not include ICFR opinion
   - _Auditor has communicated ICFR concerns_: Obtain communication details; treat as
     potential significant deficiency or material weakness
   - _No relationship yet (IPO/de-SPAC)_: Include auditor selection timeline in compliance
     calendar
   - **Why this matters**: Section 404(b) auditor reliance on management testing work
     changes the evidence requirements and documentation standards.

### Step 3: Gather Legal Authority

Use **legalcode-mcp** (if connected) to retrieve current versions of key regulatory provisions.
Save results to `/tmp/sox-assessment-authority.md`.

Search for:

- Current SEC Release Nos. for Rule 13a-14 and 13a-15 (most recent amendments) [VERIFY]
- Current PCAOB AS 2201 effective text (check for any amendments post-2007 original) [VERIFY]
- Current COSO 2013 framework description from PCAOB/SEC staff guidance references [VERIFY]
- SEC staff guidance on management's report on ICFR (June 2003 Release No. 33-8238) [VERIFY]
- SEC Release No. 33-8810 (Management's Report on Internal Control Over Financial
  Reporting and Certification of Disclosure in Exchange Act Periodic Reports, 2007) [VERIFY]
- SEC cybersecurity disclosure Final Rule Release No. 33-11216 (effective Dec. 18, 2023)
  [VERIFY current status and any subsequent amendments]
- SEC Rule 10D-1 (Dodd-Frank § 954 clawback — effective December 2022; listing standard
  deadlines — LAFs/AFs required clawback policy effective November 2023) [VERIFY]
- Current PCAOB enforcement sanction maximums [VERIFY — subject to Dodd-Frank adjustments]

**If legalcode-mcp is not connected:**

- Mark all statutory and PCAOB citations with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed using general SOX compliance knowledge; flag that authority has not been
  independently verified against current official sources

### Step 4: Filer Category Determination Gate

Before conducting substantive assessment, determine whether the entity is subject to SOX
and at what level. Apply this gate; if the entity is out of scope, stop and explain why.

**SOX applicability test:**

An entity is subject to SOX if it is required to file periodic reports (10-K, 10-Q) with
the SEC under Section 13(a) or Section 15(d) of the Exchange Act. This generally includes:

- Companies with a class of securities registered under Exchange Act Section 12 (registered
  on a national securities exchange or by filing with the SEC)
- Companies that filed a registration statement under the Securities Act of 1933 that
  became effective (triggering Section 15(d) reporting until voluntarily terminated)
- Foreign private issuers filing Form 20-F (different timelines — see Localization Notes)

**Entities NOT subject to SOX:**

- Private companies with no registered securities and no effective registration statement
- Registered investment companies (subject to Investment Company Act, not SOX directly)
- Certain smaller issuers fully exempt from periodic reporting

**⟁ CLARIFY** — If the entity's SOX applicability is uncertain (e.g., recently deregistered,
potential Exchange Act Section 12(g) threshold, or foreign issuer with ADRs only), pause
and clarify before proceeding.

**Section 404(b) applicability table:**

| Filer Category                        | Public Float                | Revenue Condition                                                 | §404(a)      | §404(b)                                     |
| ------------------------------------- | --------------------------- | ----------------------------------------------------------------- | ------------ | ------------------------------------------- |
| Large accelerated filer (LAF)         | ≥ $700M                     | No revenue test                                                   | Required     | Required                                    |
| Accelerated filer (AF)                | $75M – <$700M               | No revenue test                                                   | Required     | Required                                    |
| Non-accelerated filer (NAF)           | < $75M                      | No revenue test                                                   | Required     | Exempt                                      |
| Smaller reporting company (SRC)       | < $700M + revenue condition | <$250M revenues if float <$700M; or <$100M revenues with no float | Required     | Exempt                                      |
| Emerging growth company (EGC)         | Any                         | Revenues < $1.235B [VERIFY]                                       | Required     | Exempt (up to 5 years post-IPO)             |
| Foreign private issuer (FPI) — LAF/AF | ≥ $700M or $75M–<$700M      | FPI equivalent                                                    | 20-F Item 15 | 20-F Item 15T → 15 (see Localization Notes) |

Note: An EGC that also qualifies as a LAF or AF loses EGC status at end of fiscal year
in which public float exceeds the LAF/AF threshold. [VERIFY current threshold amounts.]

If entity is **out of scope** (private company, non-filer): Stop, inform user, and recommend
whether voluntary SOX-equivalent controls are advisable (e.g., pre-IPO readiness build).

### Step 5: Section 302 — Disclosure Controls and Procedures Assessment

Section 302 (15 U.S.C. § 7241; 17 CFR § 240.13a-14(a)) requires the principal executive
officer (CEO) and principal financial officer (CFO) to certify each annual (10-K) and
quarterly (10-Q) report. Assess the following elements:

**5.1 — Certification Process Infrastructure**

| Assessment Area                   | Assessment Questions                                                                                                                                                       | Evidence Required                                                            |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| DC&P evaluation procedure         | Is there a documented procedure for evaluating DC&P within 90 days before each filing? Who is responsible? Is the evaluation documented?                                   | Written procedure; evaluation workpapers dated before filing                 |
| ICFR evaluation procedure         | Is there a documented procedure for evaluating ICFR changes during the reporting period?                                                                                   | Quarter-end ICFR change assessment documentation                             |
| Sub-certification program         | Does management obtain sub-certifications from officers and process owners responsible for significant accounts and disclosures?                                           | Sub-certification forms signed by relevant officers for each filing period   |
| Supporting controls documentation | Are the controls that support the CEO/CFO certifications identified, tested, and documented?                                                                               | Control matrix; test workpapers; disclosure committee meeting minutes        |
| Disclosure committee              | Is there a disclosure committee that reviews financial reports before CEO/CFO certification?                                                                               | Disclosure committee charter; meeting minutes; sign-off on each report       |
| Significant changes disclosure    | Are changes in ICFR that materially affect or are reasonably likely to materially affect ICFR tracked and disclosed in Item 9A(b) of Form 10-K and Item 4(b) of Form 10-Q? | Quarterly ICFR change log; 10-Q/10-K disclosures reviewed against change log |

**5.2 — DC&P vs. ICFR Relationship**

DC&P (17 CFR § 240.13a-15(e)) covers all controls and procedures designed to ensure that
information required to be disclosed in Exchange Act reports is recorded, processed,
summarized, and reported within required timeframes. ICFR (17 CFR § 240.13a-15(f)) is a
subset of DC&P — it covers controls over financial reporting specifically.

A deficiency in ICFR is automatically a deficiency in DC&P. Assess both independently
and confirm the DC&P conclusion reflects the ICFR conclusion.

**Classification guidance for Section 302:**

- **EFFECTIVE**: CEO/CFO conclusion of effective DC&P with supporting workpapers; no
  significant changes in ICFR; disclosure committee functioning; sub-certifications obtained
- **CONTROL DEFICIENCY**: Missing sub-certifications from certain business units; disclosure
  committee minutes incomplete; minor gaps in change-in-ICFR tracking
- **SIGNIFICANT DEFICIENCY**: No sub-certification program; disclosure committee inactive;
  no documented DC&P evaluation procedure; CEO/CFO conclusion not supported by workpapers
- **MATERIAL WEAKNESS**: CEO/CFO determines DC&P is ineffective; ICFR material weakness
  requires adverse Item 9A disclosure; § 302 certifies DC&P as ineffective

### Step 6: COSO 2013 Framework — Entity-Level Controls Assessment

Entity-level controls (ELCs) permeate the organization and affect all five COSO components.
Assess each COSO component and its constituent principles. A deficiency at the entity level
may affect multiple process-level controls simultaneously.

**COSO 2013 — Five Components and Seventeen Principles:**

**Component 1: Control Environment (Principles 1–5)**

| Principle                             | Key Assessment Questions                                                                                                                                                                         | Classification |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| P1 — Integrity and Ethics             | Does the organization have a code of conduct? Is it communicated to all employees? Is it enforced with consequences for violations? Is tone-at-the-top visible from senior management and board? |                |
| P2 — Board Independence and Oversight | Does the board exercise oversight of ICFR? Is the audit committee independent? Does the board review management's ICFR assessment?                                                               |                |
| P3 — Organizational Structure         | Are reporting lines and authorities clearly defined? Is the finance function adequately staffed? Are responsibilities for ICFR explicitly assigned?                                              |                |
| P4 — Commitment to Competence         | Are accounting and finance personnel qualified and trained? Is staff turnover in key roles tracked? Are competency gaps identified and remediated?                                               |                |
| P5 — Accountability                   | Does the organization hold personnel accountable for ICFR responsibilities? Are performance evaluations linked to control responsibilities? Are consequences applied for control failures?       |                |

**Component 2: Risk Assessment (Principles 6–9)**

| Principle                             | Key Assessment Questions                                                                                                                                                                                       | Classification |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| P6 — Objectives Specification         | Are financial reporting objectives clearly defined at the financial statement level? Are relevant GAAP/IFRS standards identified for significant accounting policies?                                          |                |
| P7 — Risk Identification and Analysis | Is there a formal ICFR risk assessment process? Are significant accounts and disclosures identified through a risk-based approach? Is the assessment updated at least annually?                                |                |
| P8 — Fraud Risk Assessment            | Does the risk assessment include fraud risks (financial statement fraud, misappropriation of assets, management override)? Does the organization have a fraud risk program?                                    |                |
| P9 — Change Identification            | Are significant business, operational, regulatory, or technology changes identified and assessed for ICFR impact? Is there a trigger-based reassessment process for major transactions (M&A, systems changes)? |                |

**Component 3: Control Activities (Principles 10–12)**

| Principle                          | Key Assessment Questions                                                                                                                                                             | Classification |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| P10 — Control Activities Selection | Are control activities identified at the process level for each significant account? Are both preventive and detective controls present? Is there appropriate segregation of duties? |                |
| P11 — Technology General Controls  | Are ITGCs documented and tested? Do ITGCs support the reliability of IT-dependent controls and automated controls? (See Step 9 for detailed ITGC assessment.)                        |                |
| P12 — Policies and Procedures      | Are control activities deployed through documented policies and procedures? Are procedures current, approved, and accessible to relevant personnel?                                  |                |

**Component 4: Information and Communication (Principles 13–15)**

| Principle                    | Key Assessment Questions                                                                                                                                                               | Classification |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| P13 — Relevant Information   | Are systems of record identified for each significant account? Is financial data captured completely and accurately? Are interfaces between systems reconciled?                        |                |
| P14 — Internal Communication | Are ICFR responsibilities communicated to relevant personnel? Are deficiency findings communicated to management and the audit committee on a timely basis?                            |                |
| P15 — External Communication | Are external financial reports complete and accurate? Are disclosures in the MD&A and Notes consistent with financial data? Is the external auditor communication process functioning? |                |

**Component 5: Monitoring Activities (Principles 16–17)**

| Principle                                      | Key Assessment Questions                                                                                                                                                                                        | Classification |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| P16 — Ongoing and Separate Evaluations         | Are ongoing monitoring activities embedded in business operations? Are separate evaluations (internal audit, management's annual ICFR assessment) conducted?                                                    |                |
| P17 — Deficiency Communication and Remediation | Are control deficiencies documented, communicated to responsible parties, and tracked through remediation? Is escalation to the audit committee occurring for significant deficiencies and material weaknesses? |                |

**ELC Assessment and Documentation Checklist:**

- [ ] COSO 2013 framework selection documented in writing
- [ ] All 5 components and 17 principles assessed with supporting evidence
- [ ] Entity-level risk assessment completed and documented
- [ ] Fraud risk assessment completed and documented separately (COSO P8 / AS 2401)
- [ ] COSO assessment updated for the current fiscal year; changes since prior year documented
- [ ] No points of failure identified at the entity level (tone at the top, override risk,
      competency gaps) that would indicate a pervasive control environment deficiency

### Step 7: Section 404 — ICFR Scoping and Risk Assessment

ICFR scope is determined through a risk-based process. Not all accounts and processes need
to be included — only those where misstatement could be material to the financial statements.

**7.1 — Significant Accounts and Disclosures Identification**

Classify each balance sheet account and income statement line item using quantitative and
qualitative criteria:

**Quantitative threshold**: AS 2201 § 21 — significance is based on whether a reasonable
possibility of material misstatement of the account could result in a material misstatement
of the financial statements. Materiality is typically 5% of pre-tax income or 0.5–1% of
total assets [VERIFY: materiality thresholds are professional judgment; no fixed SEC rule].

**Qualitative factors that can elevate lower-dollar accounts to in-scope**:

- High volume / complexity of transactions
- Significant judgment or estimation (revenue recognition, allowances, goodwill impairment)
- Related-party transactions
- History of misstatement or audit adjustments
- Fraud risk indicators
- Recent accounting standard changes affecting the account
- Non-routine or unusual transactions

**⟁ CLARIFY** — If the company has undergone a significant transaction (M&A, new business
line, major system implementation, or IPO) since the prior ICFR scope was set, ask:
"Has the ICFR scope been updated to reflect [transaction/change]? If not, an out-of-scope
significant account could result in a material weakness in the ICFR scoping process itself."

**7.2 — Location/Business Unit Scoping**

For multi-location or multi-entity companies, apply the coverage concept:

| Coverage Method       | Description                                                                              | Use When                                        |
| --------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Full coverage         | All locations assessed annually                                                          | Fewer than 5 significant locations              |
| Principal locations   | Locations representing majority of revenues/assets assessed annually; others on rotation | 5–20 significant locations                      |
| Risk-based rotation   | High-risk locations annually; lower-risk locations on 3-year rotation                    | 20+ locations with similar control environments |
| Entity-level reliance | Strong entity-level controls reduce location-specific testing needs                      | Centralized processing environments             |

Document the basis for location scoping decisions. A scoping decision that omits a location
where a material misstatement subsequently occurs can itself be a material weakness finding.

**7.3 — Significant Account and Risk Matrix (SARM)**

Prepare or verify the SARM for the current year. The SARM should document for each
significant account:

- Account balance / disclosure
- Assertion(s) at risk (existence, completeness, rights/obligations, valuation, presentation)
- Relevant risks of material misstatement
- Key controls that address each risk
- Control type (automated / manual / IT-dependent manual)
- Relevant financial reporting system(s)
- Control owner

### Step 8: Section 404 — Process-Level and Transaction-Level Controls Assessment

For each significant account in scope, assess the controls that address the risks of
material misstatement. Assess both design effectiveness and operating effectiveness.

**8.1 — Key Control Identification**

A key control is a control that, if absent or ineffective, could allow a material misstatement
to occur without detection or correction. Distinguish:

- **Key controls**: Must be tested; failure = potential significant deficiency or material weakness
- **Non-key controls**: May provide additional coverage; failure alone unlikely to be material
- **Compensating controls**: Detective controls that compensate for absent preventive controls;
  acceptable if properly documented but weaker than primary controls

**8.2 — Design Effectiveness Assessment**

For each key control, assess whether the control, if operating as designed, would prevent
or detect a material misstatement. Document:

- Control description (who performs, what they do, when, how often)
- Control precision (does the control operate at a level of precision to detect material misstatements?)
- Control attributes (manual / automated / IT-dependent manual; preventive / detective; period-end / continuous)
- Evidence produced by the control
- Management override risk for the control

**8.3 — Operating Effectiveness Testing**

Test controls for operating effectiveness by verifying that the control operated consistently
throughout the testing period (typically a 12-month period for annual assessment):

| Control Frequency   | Minimum Sample Size (Management Testing)             | Evidence Type                                       |
| ------------------- | ---------------------------------------------------- | --------------------------------------------------- |
| Daily or continuous | 25–40 items [VERIFY: per AS 2201 and PCAOB guidance] | Inspection of evidence; re-performance              |
| Weekly              | 10–15 items                                          | Inspection of evidence                              |
| Monthly             | 3–6 items                                            | Inspection of evidence; inquiry + observation       |
| Quarterly           | 2–4 items                                            | Inspection of evidence                              |
| Annual              | All occurrences (typically 1–2)                      | Inspection of all evidence; in-depth re-performance |

Note: Sample sizes above reflect management's assessment. External auditor sample sizes
under PCAOB AS 2201 may be larger; auditor reliance on management testing requires the
auditor to assess management's work as part of their independent procedures.

**Testing period note**: For controls implemented or significantly modified during the year,
only the period during which the redesigned control was operating can be covered. A control
operating for less than 6 months generally cannot demonstrate sufficient operating
effectiveness for a full-year ICFR conclusion without additional testing or compensating
controls for the earlier period.

**⟁ CLARIFY** — If there are gaps in the testing period (e.g., personnel changes, system
outages, process redesigns during the year), ask: "Are there controls where testing cannot
cover the full 12-month period? If so, what compensating controls or additional procedures
are planned to address the gap periods?"

**8.4 — Period-End Financial Reporting Process**

The period-end financial reporting process (PEFRP) is always a key process regardless of
dollar materiality. Assess:

- [ ] Trial balance accuracy and completeness
- [ ] Journal entry controls (authorization, documentation, segregation of duties,
      review of manual journal entries — especially top-side and non-standard entries)
- [ ] Account reconciliation process (completeness, timeliness, reviewer qualifications)
- [ ] Financial statement consolidation controls
- [ ] Disclosure preparation and review process (quantitative and qualitative disclosures)
- [ ] Management review controls over accounting estimates
- [ ] Financial statement close calendar with defined responsibilities and sign-offs

**⟁ CLARIFY** — If there are significant manual journal entries or unusual entries at or
near period end, escalate: "Unusual or inadequately reviewed period-end manual journal
entries are among the most common sources of material weakness findings. Confirm that
management review controls over top-side entries are documented and tested."

### Step 9: IT General Controls (ITGC) Assessment

ITGCs provide the foundation for reliance on automated controls and IT-dependent manual
controls. A failure in ITGCs undermines the reliability of all controls that depend on
those systems, potentially cascading into multiple process-level control failures.

Assess all four ITGC domains for each in-scope system:

**Domain 1: Access to Programs and Data**

| Control Area                       | Key Assessment Questions                                                                                                                                                         | Classification |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| User access provisioning           | Is there a formal process for provisioning user access aligned with job function? Is least-privilege principle applied?                                                          |                |
| User access deprovisioning         | Are terminated or transferred employees' access removed within defined timeframe (ideally same-day or within 24 hours)? Is there evidence of timely execution?                   |                |
| Privileged access management (PAM) | Are privileged accounts (admin, DBA, super-user) limited in number, reviewed regularly, and require additional authentication? Are privileged access logs retained and reviewed? |                |
| Segregation of duties (SOD)        | Are SOD conflicts identified and documented? Are SOD violations mitigated by compensating controls? Is there a formal SOD matrix for in-scope systems?                           |                |
| Access review                      | Are user access reviews performed at least annually (quarterly for privileged access)? Are access review exceptions tracked to resolution?                                       |                |
| Multi-factor authentication (MFA)  | Is MFA required for remote access, privileged accounts, and cloud environments?                                                                                                  |                |
| Shared/generic accounts            | Are shared accounts prohibited for in-scope systems? If exceptions exist, are they documented and compensated?                                                                   |                |

**Domain 2: Program Change Management**

| Control Area                    | Key Assessment Questions                                                                                                                                  | Classification |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| Change authorization            | Are all changes to in-scope systems formally authorized before implementation? Is there a documented change approval workflow?                            |                |
| Change testing                  | Are changes tested in a non-production environment before deployment to production? Is test evidence retained?                                            |                |
| Change approval and segregation | Is the same individual prohibited from developing, testing, and approving a change? Is there documented approval by someone independent of the developer? |                |
| Emergency change procedures     | Is there a formal emergency change procedure (break-glass)? Are emergency changes reviewed and approved after the fact within a defined timeframe?        |                |
| Change inventory                | Is a complete inventory of changes to in-scope systems maintained? Are ITGC change population completeness controls documented?                           |                |

**Domain 3: Computer Operations**

| Control Area                  | Key Assessment Questions                                                                                                                                                  | Classification |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| Job scheduling and monitoring | Are automated batch jobs and interfaces monitored? Are failures identified and resolved before financial reports are produced?                                            |                |
| Incident management           | Is there a formal incident management process? Are incidents affecting financial data escalated appropriately?                                                            |                |
| Backup and recovery           | Are critical financial systems backed up on a defined schedule? Is recovery tested at least annually? Is backup storage secured and offsite/cloud-redundant?              |                |
| Data center physical security | Is physical access to data centers restricted? Are access logs retained and reviewed? (Less relevant for fully cloud environments — assess cloud provider SOC 1 instead.) |                |
| System performance monitoring | Are systems monitored for availability and performance? Are SLAs with critical vendors tracked?                                                                           |                |

**Domain 4: Systems Development and Implementation**

| Control Area                          | Key Assessment Questions                                                                                                                              | Classification |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| SDLC governance                       | Is there a formal systems development lifecycle policy? Are new systems and major enhancements subject to documented project management and sign-off? |                |
| Requirements and design documentation | Are business requirements documented and approved before development?                                                                                 |                |
| Pre-implementation testing and UAT    | Is user acceptance testing (UAT) performed and documented for significant system changes? Are test results reviewed and approved?                     |                |
| Post-implementation review            | Is there a formal post-implementation review for major system projects? Are open issues tracked?                                                      |                |

**Cloud ITGC Considerations**:
For cloud-hosted in-scope systems (AWS, Azure, GCP, SaaS ERPs), the shared responsibility
model means certain ITGC controls are operated by the cloud provider, not the company.
Assess via SOC 1 report reliance (see Step 10). The company remains responsible for:

- User access provisioning/deprovisioning within the cloud environment
- MFA and identity management (often via cloud IAM tools)
- Configuration management and change control within the company's cloud tenant
- Business continuity and data backup (within the shared responsibility scope)

### Step 10: Service Organization Controls (SOC 1/SOC 2) Reliance Assessment

When the company relies on third-party service organizations (cloud ERPs, payroll
processors, data centers, transfer agents) to process transactions relevant to ICFR,
the company must obtain and evaluate the service organization's SOC 1 Type II report.

**10.1 — Service Organization Inventory**

Identify all service organizations processing transactions in-scope for ICFR:

- [ ] Cloud ERP providers (Workday, NetSuite, Sage Intacct, SAP S/4HANA Cloud)
- [ ] Payroll processing (ADP, Paychex, Ceridian)
- [ ] Treasury and banking platforms
- [ ] Transfer agents and stock plan administrators
- [ ] Data center / managed IT providers
- [ ] Tax provision software providers (with data flows)

**10.2 — SOC 1 Report Evaluation Checklist**

For each SOC 1 Type II report received, verify:

- [ ] **Report type**: Is it a SOC 1 Type II (not Type I)? Type I tests design only; Type II
      tests design and operating effectiveness over a period. Only Type II provides ICFR reliance.
- [ ] **Coverage period**: Does the SOC 1 report cover the company's testing period?
      If the SOC 1 covers January–December but the company needs coverage through March
      (Q1 10-Q), a bridge letter or additional procedures covering the gap period are required.
- [ ] **Auditor's opinion**: Is the opinion unqualified (no exceptions)? If qualified,
      assess whether exceptions affect controls the company relies upon.
- [ ] **Carve-out vs. inclusive method**: If the SOC 1 uses carve-out for subservice
      organizations that process company data, obtain and evaluate the subservice organization's
      SOC 1 report or apply the inclusive method.
- [ ] **Complementary User Entity Controls (CUECs)**: Has the company identified all
      CUECs? Is there a control in place at the company that satisfies each CUEC? CUECs are
      controls that the service organization has assumed the user entity will implement; if
      they are absent, the SOC 1 reliance is incomplete.
- [ ] **Trust Services Categories (SOC 2)**: If relying on a SOC 2 for IT systems in ICFR
      scope (e.g., cloud infrastructure), verify the SOC 2 covers Security and Availability
      criteria relevant to the financial data being processed.

**Bridge Letter Assessment**:
A bridge letter covers the period from the end of the SOC 1 report to the company's
assessment date (gap period). Request bridge letters for all SOC 1 reports that do not
cover the full assessment period. Assess whether the bridge letter contains any exceptions
or material changes in the service organization's controls during the gap period.

**⟁ CLARIFY** — If any SOC 1 report for a critical service organization is unavailable,
qualified, or stale (>12 months old), ask: "This service organization processes transactions
material to [significant account]. Without a current, clean SOC 1 Type II report, an
alternative testing procedure (direct inspection at the service organization, or testing of
compensating controls at the user entity) is required. Which approach is feasible?"

### Step 11: Audit Committee and Governance Assessment (Section 301/407)

**11.1 — Audit Committee Independence (Section 301)**

Each audit committee member must be an independent member of the board of directors, meaning:

- Not accepting any consulting, advisory, or compensatory fees from the company other than
  director fees and committee fees [VERIFY Exchange Act § 10A(m)(3) exact text]
- Not being an "affiliated person" of the company or its subsidiaries

**Audit committee responsibilities assessment:**

| Responsibility                 | Assessment Questions                                                                                                                                                                                                                  | Classification |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| External auditor oversight     | Is the audit committee directly responsible for appointing, compensating, and overseeing the external auditor? Does the committee pre-approve all audit and permissible non-audit services?                                           |                |
| Internal controls oversight    | Does the audit committee review management's ICFR assessment and conclusions? Does it review deficiency findings and remediation plans?                                                                                               |                |
| Complaint procedures (§301(4)) | Does the company have procedures for (a) receipt, (b) retention, and (c) treatment of complaints regarding accounting, internal accounting controls, or auditing? Are procedures anonymous and confidential for employee submissions? |                |
| Financial expertise (§407)     | Has the board determined that at least one audit committee member is a "financial expert" as defined by SEC rules? Is the determination disclosed in the proxy statement?                                                             |                |
| Auditor communications         | Does the audit committee receive required communications from the external auditor (critical audit matters, disagreements with management, management's consultations with other accountants)?                                        |                |

**11.2 — Management Override Risk Assessment**

Management override is the highest fraud risk in any ICFR program. Assess:

- [ ] Controls over management's ability to override automated controls (e.g., posting
      restrictions, system access limitations)
- [ ] Journal entry review controls with explicit management override detection focus
- [ ] Anti-fraud program effectiveness (code of conduct, ethics hotline, whistleblower
      program, management certifications)
- [ ] Audit committee awareness of top-side and non-standard journal entries

### Step 12: Emerging Requirements — Cybersecurity, Clawback, and PCAOB Developments

**12.1 — SEC Cybersecurity Disclosure Rule (Effective December 18, 2023)**

The SEC Final Rule Release No. 33-11216 requires:

- **Form 8-K Item 1.05**: Disclosure of material cybersecurity incidents within 4 business
  days of determining materiality. [VERIFY current Rule text — assess whether any
  amendments have been issued since December 2023]
- **Form 10-K Item 1C**: Annual disclosure of cybersecurity risk management, strategy,
  and governance (including board oversight and management expertise)

**ICFR interaction**: A material cybersecurity incident affecting financial systems may
trigger a change in ICFR evaluation (Section 302 Item 4(b)). Assess whether cybersecurity
incident response procedures include an ICFR impact assessment trigger.

- [ ] Incident materiality determination process documented (4-business-day clock trigger)
- [ ] CISO / CIO included in disclosure controls evaluation process
- [ ] Board cybersecurity oversight structure disclosed in 10-K Item 1C
- [ ] Cybersecurity risk integrated into COSO P7/P9 (risk assessment / change identification)

**12.2 — Executive Compensation Clawback (Section 304 / SEC Rule 10D-1)**

SEC Rule 10D-1 (effective for fiscal years ending on or after December 1, 2023 for LAFs
and AFs) requires listed companies to maintain and enforce a written clawback policy covering:

- Recovery of erroneously awarded incentive-based compensation from current and former
  executive officers in the event of a financial restatement
- The clawback policy applies regardless of fault; the standard is "no fault" recovery
- Applies to incentive compensation received in the 3 fiscal years preceding the restatement

Assess:

- [ ] Clawback policy adopted and filed as Exhibit 97 to Form 10-K
- [ ] Policy covers all required executive officers (all Section 16 officers)
- [ ] Policy covers the 3-year look-back period
- [ ] Policy covers all incentive-based compensation including equity awards
- [ ] Disclosure of any clawback triggers or recoveries in current fiscal year
- [ ] Section 304 (pre-Rule 10D-1) remains in effect for fraud-based restatements with
      narrower scope (CEO/CFO only; 12-month look-back; misconduct required)

**12.3 — PCAOB Standard-Setting and Enforcement Developments**

| Development                       | Description                                                                                                               | ICFR Assessment Relevance                                                               | Status                                                    |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| PCAOB NOCLAR Proposal (Dec. 2023) | Proposed standard requiring auditors to evaluate noncompliance with laws and regulations beyond financial reporting fraud | Would expand auditor scrutiny of compliance programs including SOX itself               | Proposed — [VERIFY finalization status]                   |
| PCAOB China Audit Access          | PCAOB access to audit workpapers for China-based issuers post-HFCA Act                                                    | Relevant for Chinese-American companies and companies with significant China operations | Ongoing — [VERIFY current PCAOB inspection access status] |
| AI in Internal Controls           | No formal PCAOB/SEC guidance yet on AI-generated controls or AI-assisted financial reporting                              | Assess whether AI tools in financial reporting have adequate human review controls      | Emerging — watch for guidance                             |
| PCAOB AS 1000                     | Effective for audits of fiscal years ending on or after December 15, 2024                                                 | Updates auditor performance standards; may affect documentation expectations            | [VERIFY effective date and content]                       |

### Step 13: Synthesize, Quality Verification, and Generate Assessment

After completing all domain assessments (Steps 5–12), synthesize findings into the final
assessment. Run all quality checks before generating output.

**13.1 — Automatic Material Weakness Triggers**

Per PCAOB AS 2201 §§ 69-70 and SEC guidance, the following situations are strong indicators
that a material weakness exists. If any of the following are identified, the material
weakness classification applies without further quantitative analysis:

| Trigger                                                                                              | Basis                 | Classification                            |
| ---------------------------------------------------------------------------------------------------- | --------------------- | ----------------------------------------- |
| Fraud by senior management, whether or not material                                                  | AS 2201 § 69          | MATERIAL WEAKNESS — automatic             |
| A restatement of previously issued financial statements to correct a material misstatement           | AS 2201 § 69          | MATERIAL WEAKNESS — automatic             |
| Auditor identifies a material misstatement in financial statements that ICFR would not have detected | AS 2201 § 69          | MATERIAL WEAKNESS — automatic             |
| Ineffective audit committee oversight of financial reporting                                         | AS 2201 § 69          | MATERIAL WEAKNESS — automatic             |
| No documented Section 302 certification process with supporting workpapers                           | Management assessment | MATERIAL WEAKNESS — automatic             |
| CEO/CFO cannot make affirmative §302 certification in good faith                                     | Management assessment | MATERIAL WEAKNESS — automatic             |
| No COSO or equivalent framework documented as the basis for ICFR assessment                          | Management assessment | MATERIAL WEAKNESS — automatic             |
| Previously disclosed material weakness with no remediation plan or past remediation deadline         | Management assessment | MATERIAL WEAKNESS — automatic             |
| No IT General Controls program for systems processing material financial data                        | Management assessment | MATERIAL WEAKNESS — strong indicator      |
| No SOC 1 or alternative procedures for critical service organizations                                | Management assessment | SIGNIFICANT DEFICIENCY — strong indicator |

**13.2 — Classification System**

Apply the following definitions from PCAOB AS 2201 §§ 7-9 to each finding:

**EFFECTIVE** (No Deficiency):
Control exists, is suitably designed to prevent or detect material misstatements, and
operated effectively throughout the testing period. Evidence supports operating
effectiveness. No remediation action required; document and maintain.

**CONTROL DEFICIENCY** (Design or Operating):
A deficiency in the design or operation of a control that does not rise to a significant
deficiency or material weakness. Lower probability of misstatement. Remediate in the
next control cycle; document corrective action.

- _Design deficiency_: Control does not prevent/detect/correct misstatements on a timely
  basis, even if it operates as designed.
- _Operating deficiency_: Control is suitably designed but did not operate effectively
  (e.g., deviations in sample testing, insufficient evidence retained).

**SIGNIFICANT DEFICIENCY**:
A deficiency, or combination of deficiencies, in ICFR that is less severe than a material
weakness, yet important enough to merit attention by those responsible for oversight of
the company's financial reporting (AS 2201 § 8). Requires:

- Communication to management and audit committee in writing
- Disclosure in the auditor's communication to the audit committee
- Management tracking and remediation plan
  _Note_: A significant deficiency does not require adverse ICFR opinion or Item 9A
  disclosure. However, multiple significant deficiencies in combination may constitute
  a material weakness.

**MATERIAL WEAKNESS**:
A deficiency, or combination of deficiencies, in ICFR, such that there is a reasonable
possibility that a material misstatement of the company's annual or interim financial
statements will not be prevented, or detected and corrected, on a timely basis (AS 2201 § 7).

- Requires adverse management's report in Item 9A of Form 10-K
- Prohibits CEO/CFO §302 certification of effective ICFR (must certify a material weakness exists)
- Triggers §404(b) adverse opinion from external auditor (if §404(b) applicable)
- Requires immediate escalation to audit committee
- Requires public disclosure in Form 10-K and potentially on Form 8-K (if material to
  investors and not previously disclosed)
- Remediation must occur AND operating effectiveness must be tested before management
  can re-certify ICFR as effective

**Severity factors** (consider when classifying between significant deficiency and material weakness):

- **Magnitude**: What is the potential dollar magnitude of a misstatement that could result?
  The closer to materiality, the more severe.
- **Likelihood**: What is the probability that a misstatement would occur and not be detected
  by other controls? Higher likelihood = more severe.
- **Population**: Does the deficiency affect a large volume of transactions or a high-risk
  account?
- **Compensating controls**: Are there other controls that would catch the misstatement?
  Document any compensating controls relied upon to downgrade a potential material weakness.
- **Pervasiveness**: Does the deficiency affect multiple accounts, processes, or business
  units? Pervasive deficiencies trend toward material weakness.

**13.3 — Prioritization Framework**

| Priority | Classification                      | Effort            | Action                                                                                                                 | Deadline               |
| -------- | ----------------------------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| P1       | Material Weakness                   | Any effort        | Immediate escalation to audit committee; public disclosure; remediation with re-testing before next §302 certification | Before next SEC filing |
| P2       | Significant Deficiency              | Any effort        | Written communication to management and audit committee; formal remediation plan; remediation tracked quarterly        | 30–90 days             |
| P3       | Control Deficiency                  | Low–medium effort | Corrective action in normal cycle; document and track                                                                  | 90–180 days            |
| P4       | Control Deficiency                  | High effort       | Annual planning cycle; document risk acceptance if not remediated before year-end                                      | Next annual cycle      |
| P5       | EFFECTIVE — enhancement opportunity | Any effort        | Best practice improvement; not required; monitor                                                                       | Ongoing monitoring     |

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                                                  | Fail Action                                                                |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Source**     | Every compliance finding cites a specific SOX section, SEC rule (17 CFR), PCAOB AS, or established principle                                                          | Add citation or mark "[UNVERIFIED]"                                        |
| **Format**     | All citations use consistent format: "SOX § [section]", "17 CFR § 240.[rule]", "PCAOB AS [number] § [paragraph]", "COSO 2013 P[number]"                               | Fix format                                                                 |
| **Currency**   | Every cited provision checked for amendments, PCAOB amendments, or SEC rule updates                                                                                   | Flag "[CHECK CURRENCY]"                                                    |
| **Domain**     | Analysis stays within SOX/SEC/PCAOB scope; findings under other frameworks (GAAP, ERISA, FCPA) are labeled as cross-framework and not conflated with SOX deficiencies | Remove or flag framework bleed                                             |
| **Confidence** | Uncertainty explicitly stated; proposed rules distinguished from final rules; pending guidance marked as advisory                                                     | Add confidence qualifier; mark proposed rules "[PROPOSED — NOT YET FINAL]" |

---

## Self-Interrogation

For every finding classified as **MATERIAL WEAKNESS**, apply this 3-pass adversarial
review before delivering:

**Pass 1 — Regulatory Necessity**: Does the classification follow logically from AS 2201
§ 7 (reasonable possibility of material misstatement) or the automatic triggers (AS 2201
§§ 69-70)? Would the SEC or PCAOB actually require this disclosure? Would management's
independent external auditor reach the same conclusion? Document the logical chain.

**Pass 2 — Completeness**: Have all relevant compensating controls been considered?
Has the fraud risk analysis (COSO P8, AS 2401) been incorporated? Are there other controls
in the system that reduce the likelihood or magnitude of potential misstatement such that
the classification should be downgraded to significant deficiency?

**Pass 3 — Challenge**: What is the strongest argument that this finding is a significant
deficiency rather than a material weakness? What facts, if established, would change the
classification? Under what circumstances would a qualified SOX professional accept the
existing control state as adequate? Document the contra-argument and explain why the
material weakness classification still holds.

Mark audit trail: `self_interrogation: "PASS"` (finding confirmed) or `self_interrogation:
"REVISED"` (classification adjusted based on passes, with explanation).

---

## Confidence Scoring

| Level        | Range     | Meaning                                                          | Action                                                        |
| ------------ | --------- | ---------------------------------------------------------------- | ------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled rule, explicit AS provision, clear SEC guidance          | State with confidence                                         |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions                 | State with brief caveat                                       |
| **Probable** | 0.60–0.79 | Good arguments, reasonable professionals could differ            | State with reasoning and contra-indicators                    |
| **Possible** | 0.40–0.59 | Genuinely uncertain (e.g., proposed rule, ambiguous AS guidance) | Flag for qualified professional review; present both sides    |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                                          | Do not assert; flag "[UNCERTAIN — counsel/auditor to advise]" |

---

## Glass Box Audit Trail Template

Include the following YAML in every assessment output:

```yaml
glass_box:
  skill_name: "legalcode-sox-compliance-assessment"
  assessment_date: "[YYYY-MM-DD]"
  entity_name: "[Company name or 'Not specified']"
  exchange_listing: "[NYSE / Nasdaq / OTC / Not listed]"
  fiscal_year_end: "[Month DD]"
  filer_category: "[LAF / AF / NAF / SRC / EGC / FPI / Not determined]"
  section_404b_required: "[Yes / No / Not determined]"
  assessment_mode: "[Annual / Mid-year / Post-incident / IPO-transition / Acquisition / Remediation]"
  prior_material_weakness: "[Yes — [description] / No / Unknown]"
  coso_framework_documented: "[Yes / Partial / No]"
  it_environment: "[On-premises / Cloud / Hybrid]"
  assessment_scope:
    section_302_assessed: "[Yes / No]"
    entity_level_controls_assessed: "[Yes / No]"
    icfr_scoping_completed: "[Yes / No / Partial]"
    process_level_controls_assessed: "[Yes / No / Partial — [areas covered]]"
    itgc_assessed: "[Yes / No / Partial — [domains covered]]"
    soc1_reliance_reviewed: "[Yes / No / N/A — no service organizations in scope]"
    audit_committee_assessed: "[Yes / No]"
    emerging_requirements_reviewed: "[Yes / No]"
  service_organizations_reviewed: "[N reports reviewed; N CUECs tested]"
  section_302_classification: "[EFFECTIVE / CONTROL DEFICIENCY / SIGNIFICANT DEFICIENCY / MATERIAL WEAKNESS]"
  coso_classification: "[EFFECTIVE / CONTROL DEFICIENCY / SIGNIFICANT DEFICIENCY / MATERIAL WEAKNESS]"
  icfr_scoping_classification: "[EFFECTIVE / CONTROL DEFICIENCY / SIGNIFICANT DEFICIENCY / MATERIAL WEAKNESS]"
  process_controls_classification: "[EFFECTIVE / CONTROL DEFICIENCY / SIGNIFICANT DEFICIENCY / MATERIAL WEAKNESS]"
  itgc_classification: "[EFFECTIVE / CONTROL DEFICIENCY / SIGNIFICANT DEFICIENCY / MATERIAL WEAKNESS]"
  soc1_reliance_classification: "[EFFECTIVE / CONTROL DEFICIENCY / SIGNIFICANT DEFICIENCY / MATERIAL WEAKNESS / N/A]"
  audit_committee_classification: "[EFFECTIVE / CONTROL DEFICIENCY / SIGNIFICANT DEFICIENCY / MATERIAL WEAKNESS]"
  overall_icfr_conclusion: "[EFFECTIVE / SIGNIFICANT DEFICIENCY(IES) PRESENT / MATERIAL WEAKNESS(ES) PRESENT]"
  automatic_mw_triggers_fired: "[List any automatic Material Weakness triggers that apply, or 'None']"
  material_weakness_count: [N]
  significant_deficiency_count: [N]
  control_deficiency_count: [N]
  self_interrogation: "[PASS / REVISED / N/A — no Material Weakness findings]"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[/tmp/sox-assessment-authority.md / Not created]"
  citations_verified: "[N VERIFIED via legalcode-mcp / N marked [VERIFY]]"
  clawback_policy_reviewed: "[Yes / No / N/A — not LAF or AF]"
  cybersecurity_disclosure_reviewed: "[Yes / No]"
  confidence_overall: "[HIGH / MEDIUM / LOW] — [Rationale]"
  limitations:
    - "[Scope limitations — e.g., specific business units not assessed, prior-year control matrices not available]"
    - "[Documentation gaps — e.g., process narratives unavailable for [process area]]"
    - "[legalcode-mcp not connected — all citations unverified]"
    - "[Testing period gaps — [description] not covered by controls testing]"
  reviewer: "AI-assisted — requires review by qualified SOX compliance professional, CPA, and securities attorney"
```

---

## Anti-Patterns

What NOT to do when conducting or managing SOX compliance:

**1. Confusing significant deficiency with material weakness** — A significant deficiency
does not require an adverse ICFR opinion or §302 disclosure of ineffective ICFR. Misclassifying
upward (calling a significant deficiency a material weakness) is over-disclosure with potential
market impact. Misclassifying downward (calling a material weakness a significant deficiency)
is an SEC/PCAOB enforcement risk and potentially a false certification under §302/906.

**2. Scoping ICFR too narrowly** — Excluding significant accounts or locations from ICFR
scope to reduce compliance burden. If a material misstatement occurs in an out-of-scope account,
the scoping decision itself may be the material weakness. ICFR scope decisions must be defensible
under a reasonable possibility of material misstatement standard, not a convenience standard.

**3. Treating IT General Controls as optional for cloud systems** — "Our ERP is in the cloud,
so the vendor handles security." The shared responsibility model means the company retains ITGC
responsibilities for access management, change controls within its tenant, and interface
monitoring. Undocumented or untested cloud ITGCs cascade into unreliable automated controls.

**4. Relying on a SOC 1 report without testing CUECs** — A clean SOC 1 Type II report covers
only the service organization's controls. If the report specifies complementary user entity
controls (CUECs) that the company must implement, and those CUECs are absent or untested,
the SOC 1 reliance is incomplete. The company has the deficiency — not the service organization.

**5. Using a SOC 1 Type I for operating effectiveness reliance** — A Type I report assesses
the design of controls at a single point in time. Only a Type II report, covering a minimum
testing period (typically 6–12 months), supports reliance on operating effectiveness for ICFR.

**6. Failing to obtain a bridge letter for gap periods** — If the SOC 1 report covers
January–December and the company's assessment extends through March (for a Q1 filing), the
3-month gap is unaddressed. A bridge letter with no exceptions extends the reliance; a bridge
letter with exceptions requires additional company-level procedures.

**7. Remediating a material weakness without re-testing operating effectiveness** — Management
may implement the remediated control and prematurely certify effective ICFR before the control
has been tested for operating effectiveness over a sufficient period. The control must operate
for a sufficient period (typically at least one quarter, often longer) and be tested before
the material weakness can be considered remediated for certification purposes.

**8. Conflating §404(a) management responsibilities with §404(b) auditor responsibilities** — Management assesses ICFR independently under §404(a). The external auditor opines independently under §404(b). Management cannot substitute the auditor's testing for its own assessment. Similarly, management cannot wait for the auditor to identify deficiencies — management is independently responsible for identifying and disclosing material weaknesses.

**9. Treating the COSO framework assessment as a one-time event** — The COSO framework
assessment must be updated annually, and more frequently when significant business changes
occur (major acquisitions, system implementations, significant personnel changes, business
model shifts). An outdated COSO assessment is itself a deficiency in monitoring activities
(COSO Principle 16).

**10. Using prior-year testing for current-year reliance without rollforward** — Controls
tested in the prior year that have not been retested or rolled forward provide limited current-year
support. Operating effectiveness testing must cover the current-year testing period; rollforward
procedures (typically inquiries, observation, and limited re-testing) are only appropriate for
lower-risk, stable controls.

**11. Ignoring the period-end financial reporting process** — The PEFRP is always a key process.
Journal entry controls, account reconciliation procedures, and consolidation controls are the
most common source of fraud risk and material misstatement. Omitting these from key control
testing because the dollar amount of any individual entry is below materiality is an incorrect
application of the materiality concept.

**12. Documenting controls based on interviews alone** — "We talked to the controller and she
confirmed the reconciliation process." Without documentation of the control procedure, review
evidence (sign-offs, timestamps, system logs), and testing results, interview-based documentation
does not meet PCAOB workpaper standards for §404(b) integrated audits, and provides weak support
for management's §404(a) assessment.

**13. Underestimating sub-certification scope** — Sub-certifications from business unit CFOs
and process owners are not legally required, but are industry standard and expected by external
auditors as a component of the CEO/CFO certification support infrastructure. Limiting sub-certifications
to the CFO of the parent company, while excluding subsidiary officers who sign off on material
transactions, leaves gaps in the certification chain.

**14. Treating segregation of duties as an IT problem only** — SOD is a human controls issue
as much as a system access issue. Even in systems where SOD conflicts are locked out by the
ERP, manual override processes (direct database access, emergency access procedures, manual
journal entries) can bypass system controls. Assess SOD in both the system and the manual
control environment.

**15. Disclosing a material weakness in one year and releasing it the next without sufficient
re-testing** — Remediation must be complete (new control in place), and operating effectiveness
must be tested over a sufficient period (typically one complete quarter, often longer depending
on control frequency), before management can conclude the material weakness has been remediated.
Premature release of a material weakness disclosure is a common SEC comment letter issue.

**16. Applying COSO 2013 without the 17 principles** — COSO 2013 updated the 1992 framework
by formalizing 17 principles that must each be present and functioning for a component to be
assessed as effective. Using the 5-component COSO 1992 framework or treating the 17 principles
as optional detail rather than required assessment points is not consistent with PCAOB AS 2201
expectations.

**17. Inadequate management override detection controls** — AS 2401 and COSO P8 require explicit
consideration of fraud risk, including the risk that management could override otherwise effective
controls. Controls that only prevent lower-level employee errors but do not address executive
override (e.g., no audit committee review of unusual top-side entries, no statistical analysis
of journal entries) leave a critical ICFR gap.

**18. Ignoring small acquisitions in ICFR scope** — The SEC rule for newly acquired businesses
provides a one-year grace period for §404 assessment of acquired entities. However, if the
acquired entity represents a significant portion of consolidated assets or revenues before the
grace period expires, and a material misstatement originates in that entity, the grace period
exclusion may not shield management's overall ICFR conclusion. Size and risk should drive
the decision, not administrative convenience.

**19. Conflating §302 DC&P with §404 ICFR** — DC&P is broader than ICFR. DC&P includes all
controls over Exchange Act disclosure obligations; ICFR is the financial reporting subset. A
company can have effective ICFR and still have a DC&P deficiency (e.g., a failure to disclose
a significant related-party transaction that does not affect financial statement amounts). Assess
both independently.

**20. Not updating ICFR assessment for the SEC cybersecurity disclosure Rule** — The December
2023 cybersecurity disclosure Rule requires inclusion of cybersecurity risk management and
governance in ICFR-adjacent controls. A cybersecurity incident affecting financial systems may
require immediate evaluation of whether ICFR has been affected, triggering a §302 Item 4(b)
change-in-ICFR disclosure. Siloed cybersecurity and ICFR programs that do not communicate
present a disclosure control deficiency.

**21. Omitting the annual SOX compliance calendar from program management** — SOX compliance
is deadline-driven. CEO/CFO certifications accompany every 10-K and 10-Q. PCAOB integrated
audit timelines dictate when management testing must be complete. Without a formal compliance
calendar, testing and documentation activities may compress into the period-end close window,
reducing quality and increasing risk of missed deficiencies.

**22. Treating SOX as solely a finance function responsibility** — ICFR depends heavily on IT,
legal/compliance, HR (access deprovisioning), procurement, and business operations. A SOX program
managed exclusively within the finance function without cross-functional engagement will have
blind spots in IT General Controls, segregation of duties in business systems, and control
environment tone at the operational level.

---

## Writing Standards

Apply these standards to all deliverables:

1. **Use PCAOB/SEC terminology precisely**. "Material weakness" has a specific legal definition
   (AS 2201 § 7). Do not use it colloquially or interchangeably with "significant deficiency."
   Sloppy terminology creates disclosure risk.

2. **Separate finding from recommendation**. Every finding describes what is absent or deficient
   and why it matters (AS 2201 basis, reasonable possibility analysis). Every recommendation
   prescribes the specific corrective action, responsible owner, and timeline.

3. **Active voice in all finding and recommendation language**. Write: "Management has not
   documented a sub-certification process supporting the CEO/CFO §302 certification" — not
   "A sub-certification process has not been documented."

4. **Qualify proposed rules explicitly**. Proposed PCAOB rules and SEC NPRMs must be marked
   "[PROPOSED — NOT YET FINAL]" and must not be presented as current compliance obligations.

5. **Distinguish management's assessment from auditor conclusions**. Management's assessment
   under §404(a) and the auditor's attestation under §404(b) are independent processes.
   Do not conflate them. Management may have effective ICFR (in management's view) while
   the auditor issues an adverse opinion, and vice versa.

6. **Be explicit about compensating controls**. When a primary control is absent or deficient,
   and a compensating control is present, document both: the compensating control description,
   why it reduces (but may not eliminate) the risk, and what residual risk remains.

7. **Do not assert legal conclusions about SEC enforcement exposure**. Statements like "the
   company will face SEC action" are beyond the skill's scope. Use: "This finding presents
   material weakness disclosure obligations and creates enforcement risk that a qualified
   securities attorney should assess."

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 3, retrieve current SEC Release Nos., CFR text, and PCAOB AS current versions
- Save results to `/tmp/sox-assessment-authority.md`
- Use verified authority to support findings in Steps 5–12
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with general SOX knowledge
- Mark all regulatory citations with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Recommend that management verify all cited thresholds (filer category thresholds, penalty
  amounts, sample sizes) against current SEC.gov and PCAOB.org sources before reliance

---

## Output Format Template

```markdown
# SOX Compliance Assessment — [Company Name]

**Assessment Date**: [Date] | **Fiscal Year End**: [FYE] | **Filer Category**: [Category]
**Section 404(b) Required**: [Yes / No] | **Assessment Mode**: [Mode]
**Prepared by**: AI-assisted (legalcode-sox-compliance-assessment) — requires qualified human review

---

## Executive Summary

**Overall ICFR Conclusion**: [EFFECTIVE / SIGNIFICANT DEFICIENCY(IES) PRESENT / MATERIAL WEAKNESS(ES) PRESENT]

| Domain                     | Classification   | Material Weaknesses | Significant Deficiencies | Control Deficiencies |
| -------------------------- | ---------------- | ------------------- | ------------------------ | -------------------- |
| Section 302 — DC&P         | [classification] | [N]                 | [N]                      | [N]                  |
| COSO Entity-Level Controls | [classification] | [N]                 | [N]                      | [N]                  |
| ICFR Scoping               | [classification] | [N]                 | [N]                      | [N]                  |
| Process-Level Controls     | [classification] | [N]                 | [N]                      | [N]                  |
| IT General Controls        | [classification] | [N]                 | [N]                      | [N]                  |
| SOC 1/SOC 2 Reliance       | [classification] | [N]                 | [N]                      | [N]                  |
| Audit Committee (§301)     | [classification] | [N]                 | [N]                      | [N]                  |
| **Total**                  |                  | [N]                 | [N]                      | [N]                  |

**Automatic Material Weakness Triggers Identified**: [None / List]

**Top 3 Priority Actions**:

1. [IMMEDIATE] [Finding] — [Action] — Owner: [Role] — Deadline: [Date]
2. [NEAR-TERM] [Finding] — [Action] — Owner: [Role] — Deadline: [Date]
3. [NEAR-TERM] [Finding] — [Action] — Owner: [Role] — Deadline: [Date]

---

## Filer Category Determination

**Determination**: [Filer Category]
**Public Float**: [Amount] as of [Date]
**Revenue (if SRC/EGC test applied)**: [Amount]
**Section 404(b) applicable**: [Yes / No]
**Basis**: [Explanation]
**Next reclassification test date**: [Date]

---

## Section 302 Assessment

[Per-area assessment table from Step 5.1]
**Section 302 Classification**: [EFFECTIVE / CONTROL DEFICIENCY / SIGNIFICANT DEFICIENCY / MATERIAL WEAKNESS]

---

## COSO Entity-Level Controls Assessment

[Per-principle table from Step 6 with classifications]
**Component Summary**:
| Component | Classification |
|-----------|---------------|
| Control Environment | |
| Risk Assessment | |
| Control Activities | |
| Information and Communication | |
| Monitoring Activities | |
**Overall COSO Classification**: [Classification]

---

## Section 404 — ICFR Scoping

**Significant Accounts In Scope**: [List]
**Locations In Scope**: [List / coverage method]
**Scoping Classification**: [Classification]

---

## Process-Level Controls Assessment

### [Process Area] — [Classification] | Confidence: [Level]

**Key Control**: [Description]
**Design Effectiveness**: [Assessment]
**Operating Effectiveness**: [Sample size / Testing period / Result]
**Finding (if any)**: [Description]
**AS 2201 Basis**: [Citation]
**Recommended Action**: [Action / Owner / Deadline]

[Repeat for each key control / finding]

---

## IT General Controls Assessment

### Domain 1: Access to Programs and Data — [Classification]

[Per-control-area table]

### Domain 2: Program Change Management — [Classification]

[Per-control-area table]

### Domain 3: Computer Operations — [Classification]

[Per-control-area table]

### Domain 4: Systems Development/Implementation — [Classification]

[Per-control-area table]

---

## SOC 1/SOC 2 Reliance Assessment

| Service Organization | Service   | Report Type   | Period   | Opinion           | CUECs Tested | Bridge Letter | Classification   |
| -------------------- | --------- | ------------- | -------- | ----------------- | ------------ | ------------- | ---------------- |
| [Name]               | [Service] | SOC 1 Type II | [Period] | [Clean/Qualified] | [Y/N]        | [Y/N/N/A]     | [Classification] |

**Gaps Identified**: [Description or None]

---

## Audit Committee Assessment

[Per-responsibility table from Step 11.1]
**Audit Committee Classification**: [Classification]

---

## Deficiency Finding Detail

### MW-[N]: [Finding Title] — MATERIAL WEAKNESS

- **Classification**: Material Weakness
- **AS 2201 Basis**: [Citation]
- **Current State**: [Description of deficiency]
- **Root Cause**: [Design deficiency / Operating deficiency / Entity-level deficiency]
- **Magnitude/Likelihood Analysis**: [Reasonable possibility assessment]
- **Automatic Trigger Applied**: [Yes — [trigger] / No]
- **Self-Interrogation Result**: [PASS / REVISED — [explanation]]
- **Required Disclosure**: Item 9A of Form 10-K (adverse management's report); §302
  Item 4(b) change-in-ICFR disclosure
- **Remediation Action**: [Specific corrective action]
- **Responsible Owner**: [Role]
- **Target Remediation Date**: [Date]
- **Re-testing Requirements**: [Minimum testing period and sample size for remediation confirmation]
- **Confidence**: [Level]

### SD-[N]: [Finding Title] — SIGNIFICANT DEFICIENCY

[Same structure as above; no public disclosure required; communication to management
and audit committee in writing required]

### CD-[N]: [Finding Title] — CONTROL DEFICIENCY

[Abbreviated structure; remediation action and owner sufficient]

---

## Remediation Roadmap

### Immediate (Before Next SEC Filing)

| Priority | Finding | Corrective Action | Owner | Deadline | Evidence Required |
| -------- | ------- | ----------------- | ----- | -------- | ----------------- |

### Near-Term (30–90 Days)

| Priority | Finding | Corrective Action | Owner | Deadline | Evidence Required |
| -------- | ------- | ----------------- | ----- | -------- | ----------------- |

### Background (90–180 Days / Next Annual Cycle)

| Priority | Finding | Corrective Action | Owner | Deadline | Evidence Required |
| -------- | ------- | ----------------- | ----- | -------- | ----------------- |

---

## SOX Compliance Calendar

| Milestone                                              | Timing                             | Owner                           | Description                                                                                        |
| ------------------------------------------------------ | ---------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------- |
| ICFR risk assessment refresh                           | Q1 of fiscal year                  | VP Finance / CAO                | Annual update to SARM; scope confirmation                                                          |
| Entity-level controls assessment                       | Q1–Q2                              | Finance / Internal Audit        | COSO framework assessment; tone at top evaluation                                                  |
| Process-level controls design assessment               | Q2                                 | Process owners / Internal Audit | Documentation updates; new risk assessment                                                         |
| Process-level controls operating effectiveness testing | Q3–Q4                              | Internal Audit / Finance        | Sample testing per SARM; document and resolve exceptions                                           |
| ITGC testing                                           | Q3–Q4                              | IT / Internal Audit             | Four-domain ITGC assessment; SOD analysis                                                          |
| SOC 1/SOC 2 reports obtained and reviewed              | Q3–Q4                              | Finance / IT                    | CUECs verified; bridge letters requested                                                           |
| Sub-certifications obtained                            | FYE + 30 days                      | CFO / Controllers               | Sub-certifications supporting CEO/CFO §302 certifications                                          |
| Draft management's report (§404(a))                    | FYE + 45 days                      | CFO / Finance                   | Conclusion; deficiency summary; disclosure language                                                |
| External auditor ICFR testing completion               | FYE + 60 days                      | External Auditor                | AS 2201 integrated audit; management testing reliance review                                       |
| Final ICFR conclusion and 10-K filing                  | FYE + 60–90 days                   | CEO/CFO                         | §302 and §906 certifications; §404(a) management report; §404(b) auditor opinion                   |
| Audit committee ICFR communication                     | Before 10-K filing                 | Audit Committee                 | Material weaknesses and significant deficiencies communication; AS 2805 management representations |
| Q1/Q2/Q3 10-Q filings                                  | 40–45 days after quarter end (LAF) | CEO/CFO                         | §302 certification; §404 change-in-ICFR disclosure                                                 |
| Clawback policy review                                 | Annually                           | Compensation Committee / Legal  | Rule 10D-1 compliance; Exhibit 97 update                                                           |
| Cybersecurity incident ICFR trigger review             | Ongoing                            | CISO + Finance                  | Form 8-K Item 1.05 materiality determination; ICFR impact assessment                               |

---

## Regulatory Readiness Checklist

- [ ] Filer category confirmed and documented; §404(b) applicability determined
- [ ] COSO 2013 framework adopted as basis for ICFR assessment (documented in writing)
- [ ] ICFR scope (significant accounts, processes, locations) documented and approved
- [ ] All 17 COSO principles assessed with supporting evidence
- [ ] Entity-level controls documented and evaluated
- [ ] Process narratives / risk-control matrices current and approved
- [ ] Key controls identified and tested for design and operating effectiveness
- [ ] ITGC assessment complete for all four domains for all in-scope systems
- [ ] SOC 1 Type II reports obtained for all material service organizations; CUECs tested
- [ ] Bridge letters obtained for gap periods; no unresolved exceptions
- [ ] Segregation of duties analysis complete; conflicts documented and mitigated
- [ ] Management override detection controls documented and tested
- [ ] Sub-certification program executed; supporting certifications on file
- [ ] Disclosure committee operational; meetings documented
- [ ] CEO/CFO §302 certification workpapers complete
- [ ] Any significant deficiencies communicated to audit committee in writing
- [ ] Any material weaknesses disclosed in Item 9A; adverse management's report drafted
- [ ] Audit committee independence confirmed; financial expert disclosed in proxy
- [ ] Section 301(4) complaint procedures (accounting/audit complaints) operational
- [ ] Rule 10D-1 clawback policy in effect and filed as Exhibit 97
- [ ] Cybersecurity disclosure controls operational; ICFR impact trigger documented
- [ ] §906 certifications executed by CEO and CFO (included in 10-K/10-Q)

---

## Quality Assurance

**Self-interrogation applied to**: [List of Material Weakness findings — "None" if no MWs]
**Citation Quality Gates**: [PASSED — all 5 gates cleared / FLAGGED — [issue description]]
**Confidence scores**:

- Section 302 Assessment: [Level]
- COSO Assessment: [Level]
- ITGC Assessment: [Level]
- Overall Assessment: [Level]

---

[GLASS BOX YAML — copy completed YAML from Glass Box Audit Trail Template section above]

---

## Recommended Next Steps

1. **Legal counsel review**: Have a qualified securities attorney review any Material Weakness
   findings and proposed Item 9A disclosure language before filing.
2. **Auditor coordination**: Share assessment findings with the external auditor; confirm
   alignment on deficiency classifications before finalization.
3. **Audit committee communication**: Present findings to the audit committee in accordance
   with AS 2201 § 78 (required communication of significant deficiencies and material weaknesses).
4. **Remediation tracking**: Establish a formal remediation tracking system with assigned owners,
   milestone dates, and regular status reporting to the audit committee.
5. **Re-testing planning**: For remediated findings, plan re-testing procedures with sufficient
   operating effectiveness period before the next §302 certification.
6. **Annual calendar alignment**: Confirm the SOX compliance calendar above with internal audit,
   external auditor, and finance leadership before the next fiscal year.

**Disclaimer**: This assessment is AI-assisted and does not constitute legal advice, accounting
advice, or a compliance certification. All findings, classifications, and recommendations must
be reviewed and verified by a qualified SOX compliance professional, CPA, and securities
attorney before reliance. Statutory references, regulatory thresholds, penalty amounts, and
PCAOB standards should be independently verified against current official sources
(SEC.gov, PCAOB.org, COSO.org) before use in management's annual report or SEC filings.
```

---

## SOX Compliance Calendar (Reference)

See the output format template above for the full annual calendar. Key fixed deadlines by
filer category for the annual filing:

| Filer Category            | 10-K Deadline (FYE December 31)        | 10-Q Deadline                |
| ------------------------- | -------------------------------------- | ---------------------------- |
| Large accelerated filer   | 60 days after FYE                      | 40 days after quarter end    |
| Accelerated filer         | 75 days after FYE                      | 40 days after quarter end    |
| Non-accelerated filer     | 90 days after FYE                      | 45 days after quarter end    |
| Smaller reporting company | 90 days after FYE (as non-accelerated) | 45 days after quarter end    |
| Emerging growth company   | Same as filer category above           | Same as filer category above |
| Foreign private issuer    | 4 months after FYE (Form 20-F)         | Semi-annual (Form 6-K)       |

[VERIFY all deadlines against current Exchange Act rules — these are general approximations
and specific deadlines may differ based on filer history and any SEC relief granted.]

---

## Glossary

| Term                              | Definition                                                                                                                                                                                                                    |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **COSO**                          | Committee of Sponsoring Organizations of the Treadway Commission — private sector body that issued the Internal Control — Integrated Framework (2013) used as the basis for ICFR assessment                                   |
| **Control Deficiency**            | A deficiency in the design or operation of a control that does not prevent or detect misstatements on a timely basis; the least severe deficiency tier                                                                        |
| **DC&P**                          | Disclosure Controls and Procedures — all controls designed to ensure required Exchange Act disclosure information is recorded, processed, summarized, and reported timely; defined in 17 CFR § 240.13a-15(e)                  |
| **EGC**                           | Emerging Growth Company — company with annual revenues below the applicable threshold in its most recent fiscal year; eligible for §404(b) exemption for up to 5 years post-IPO under the JOBS Act                            |
| **ICFR**                          | Internal Controls Over Financial Reporting — a subset of DC&P; controls reasonably designed to provide reasonable assurance that financial statements are prepared in conformity with GAAP; defined in 17 CFR § 240.13a-15(f) |
| **IT General Controls (ITGC)**    | Overarching IT controls supporting the reliability of all IT-dependent business application controls; four domains: access, change management, operations, systems development                                                |
| **Large Accelerated Filer (LAF)** | SEC reporting company with public float ≥ $700M; subject to both §404(a) and §404(b)                                                                                                                                          |
| **Material Weakness**             | A deficiency, or combination of deficiencies, in ICFR such that there is a reasonable possibility that a material misstatement will not be prevented, detected, or corrected on a timely basis (AS 2201 § 7)                  |
| **PCAOB**                         | Public Company Accounting Oversight Board — SEC-supervised board that sets auditing standards (AS) and inspects registered public accounting firms                                                                            |
| **PEFRP**                         | Period-End Financial Reporting Process — controls over the financial statement close, journal entries, reconciliations, and financial statement preparation                                                                   |
| **Reasonable Possibility**        | AS 2201 §7 threshold for material weakness — at least a more-than-remote likelihood that a material misstatement will not be caught; this standard is lower than "more likely than not"                                       |
| **SAR / SARM**                    | Significant Account Risk Matrix — document mapping significant accounts to assertions, risks, and key controls                                                                                                                |
| **Significant Deficiency**        | A deficiency, or combination of deficiencies, in ICFR that is less severe than a material weakness, yet important enough to merit attention by those responsible for oversight of financial reporting (AS 2201 § 8)           |
| **SOC 1**                         | Service Organization Control 1 — SSAE 18 / AT-C 320 attestation report on a service organization's controls over financial reporting; Type I (design) and Type II (design and operating effectiveness)                        |
| **SRC**                           | Smaller Reporting Company — SEC filer meeting revenue/public float thresholds; §404(b) exempt                                                                                                                                 |
| **Sub-certification**             | Voluntary certification by an officer or process owner below the CEO/CFO level, supporting the CEO/CFO §302 certification by confirming the accuracy of information in their area of responsibility                           |

---

## Localization Notes

**Foreign Private Issuers (FPIs):**
FPIs file annual reports on Form 20-F and are subject to SOX requirements including §302
and §404 equivalents. Key differences:

- Form 20-F Item 15(a): CEO/CFO certifications equivalent to §302 (with minor differences)
- Form 20-F Item 15(b)/(c): Equivalent to §404(a) management's report and §404(b)
  auditor attestation; §404(b) required for FPIs classified as LAFs or AFs based on
  public float as of June 30 of prior fiscal year
- Form 20-F filing deadline: 4 months after fiscal year end (vs. 60 days for domestic LAFs)
- FPIs may use home-country GAAP (IFRS) rather than US GAAP; ICFR assessment covers the
  applicable GAAP framework
- FPIs from certain jurisdictions may use management reports consistent with home-country
  corporate governance codes [VERIFY SEC guidance on FPI management report exemptions]

**[JURISDICTION-SPECIFIC]** For FPIs with US-listed shares (ADRs or direct listing), assess
whether home-country laws impose additional internal control requirements that interact with
SOX. Many jurisdictions (EU, UK, Japan, Canada) have their own corporate governance codes
with internal control disclosure requirements. The skill is US-SOX focused; those parallel
obligations require jurisdiction-specific analysis.

---

## Related Skills

- `legalcode-compliance-program-builder` — build or assess a holistic corporate compliance
  program incorporating SOX, data privacy, anti-bribery, and trade compliance
- `legalcode-corporate-governance-audit` — broader board governance assessment including
  independence standards, committee structures beyond audit committee, and fiduciary duty
- `legalcode-whistleblower-program-builder` — build Section 301(4) SOX whistleblower intake
  plus SEC Rule 21F Dodd-Frank award program integration
- `legalcode-anti-bribery-compliance` — FCPA books-and-records and internal controls
  provisions (15 U.S.C. §§ 78m(b)(2)(A)/(B)) that overlap with SOX §404 ICFR obligations
- `legalcode-internal-investigation` — management's independent investigation into potential
  ICFR material weakness root causes or fraud discoveries triggering §302/§906 concerns

---

## Provenance

Created by Legalcode (2026-03-20). Mode A creation from scratch via 2-agent parallel
research pipeline (Legal Research Agent: deep web research across 12 SOX domains covering
SOX Pub. L. 107-204 full text, PCAOB AS 2201, SEC Rules 13a-14/13a-15, COSO 2013 Internal
Control — Integrated Framework all 17 principles, Section 404 filer category matrix,
Section 906 criminal penalties, IT General Controls four-domain framework, SOC 1 SSAE 18
reliance mechanics, Section 301 audit committee independence standards, Rule 10D-1 clawback,
SEC cybersecurity disclosure Rule December 2023, PCAOB enforcement trends 2024-2025;
Structural Analysis Agent: analyzed legalcode-contract-review, legalcode-hipaa-compliance-assessment,
and legalcode-dora-compliance-assessment reference standards and extracted structural patterns,
quality frameworks, writing conventions, compliance-specific anti-patterns, and output
format templates). Quality: 18/18 required elements; PCAOB AS 2201 §§ 7-9 deficiency
classification system with EFFECTIVE/CONTROL DEFICIENCY/SIGNIFICANT DEFICIENCY/MATERIAL
WEAKNESS tiers and 10 automatic Material Weakness triggers; COSO 2013 five-component
seventeen-principle assessment framework; SOC 1 reliance checklist with CUECs and bridge
letter analysis; four-domain ITGC assessment framework; P1-P5 prioritization; 5 Citation
Quality Gates; 3-pass Self-Interrogation; 5-level Confidence Scoring; Glass Box YAML with
per-domain classification fields; 22 anti-patterns; annual SOX compliance calendar;
regulatory readiness checklist (23 items); glossary; 13-step workflow with 8 CLARIFY points.
All citations marked [VERIFY] against current SEC.gov and PCAOB.org sources.
