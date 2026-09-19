---
name: legalcode-us-fcpa-compliance
description: Assesses Foreign Corrupt Practices Act (FCPA) compliance for US issuers, domestic concerns,
  and companies with US-nexus operations. Use when conducting FCPA compliance reviews, pre-enforcement
  self-assessments, compliance program gap analyses, VSD decision analyses, M&A FCPA due diligence, post-investigation
  remediation planning, or government contract qualification reviews.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Assesses Foreign Corrupt Practices Act (FCPA) compliance for US issuers, domestic concerns, and companies with US-nexus operations. Covers anti-bribery provisions (15 U.S.C. §§ 78dd-1 to 78dd-3), foreign official definition and instrumentality test (Esquenazi standard), books-and-records and internal controls (§ 78m(b)(2)), third-party due diligence (7-step lifecycle, 14-category red flag matrix), gifts/travel/ entertainment policy assessment, facilitation payment exposure, DOJ Corporate Enforcement Policy voluntary self-disclosure analysis (August 2024 120-day rule), DOJ Evaluation of Corporate Compliance Programs (ECCP September 2024) adequacy scoring, individual accountability framework, M&A successor liability analysis, and penalty structure (criminal/civil/disgorgement). Use when conducting FCPA compliance reviews, pre-enforcement self-assessments, compliance program gap analyses, VSD decision analyses, M&A FCPA due diligence, post-investigation remediation planning, or government contract qualification reviews. Jurisdiction: United States federal law (DOJ/SEC enforcement).


# Legalcode US FCPA Compliance Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted FCPA compliance assessment.
> It does not constitute legal advice. All outputs must be reviewed by qualified legal counsel
> admitted to practice in the United States before use. The FCPA and its enforcement standards
> evolve through DOJ/SEC guidance, court decisions, and enforcement policy changes. Statutory
> and case law references cited from memory carry hallucination risk — verify against DOJ/SEC
> authoritative sources before relying on them. The June 2025 DOJ enforcement guidelines
> represent a significant policy shift; verify current enforcement posture with specialized
> FCPA counsel before making voluntary self-disclosure or remediation decisions.

---

## Purpose and Scope

This skill performs a structured FCPA compliance assessment covering all major risk domains
under the Foreign Corrupt Practices Act (15 U.S.C. §§ 78dd-1 to 78dd-3 and § 78m(b)).

**Covers:**

- Anti-bribery provisions: foreign official definition, business purpose test, knowledge
  standard, covered payments, affirmative defenses, facilitation payment analysis
- Books-and-records and internal controls (accounting provisions)
- Third-party due diligence: program design, red flags, contractual protections
- Gifts, travel, and entertainment (GTE) policy adequacy
- Compliance program adequacy under DOJ ECCP (September 2024) including AI/data risk
- Voluntary self-disclosure (VSD) decision analysis under the Corporate Enforcement Policy
- Individual accountability exposure under current DOJ guidance
- M&A successor liability and pre/post-closing integration obligations
- Penalty exposure modeling (criminal fines, civil penalties, disgorgement, monitorship)

**Does not:**

- Cover UK Bribery Act 2010, Sapin II, or other non-US anti-bribery regimes
  (see `legalcode-anti-bribery-compliance` for multi-regime analysis)
- Provide legal advice or substitute for qualified FCPA counsel
- Guarantee declination, favorable enforcement outcomes, or VSD credit
- Apply to purely domestic US commercial bribery (covered by 18 U.S.C. § 666 and state law)

---

## Jurisdiction and Governing Law

**Statute**: Foreign Corrupt Practices Act of 1977, as amended (15 U.S.C. §§ 78dd-1,
78dd-2, 78dd-3; 78m(b)(2)-(3)).

**Enforcement authorities**:

- **DOJ Criminal Division, Fraud Section** — criminal anti-bribery enforcement; all
  persons; issues opinions under the FCPA Opinion Procedure Release process
- **SEC Division of Enforcement** — civil anti-bribery and accounting provisions for
  _issuers_ (public companies with registered securities)

**Subject matter jurisdiction**: All analysis in this skill is US-law-only. Where a
transaction also triggers UK Bribery Act, Sapin II, or Brazil Clean Company Act exposure,
this skill flags the intersection but defers to jurisdiction-specific skills for those regimes.

**Key governing authorities** (all citations require [VERIFY] absent legalcode-mcp connection):

- 15 U.S.C. §§ 78dd-1 (issuers), 78dd-2 (domestic concerns), 78dd-3 (foreign persons/entities) [VERIFY]
- 15 U.S.C. § 78m(b)(2)-(3) (books-and-records; internal controls) [VERIFY]
- _United States v. Esquenazi_, 752 F.3d 912 (11th Cir. 2014) — instrumentality definition [VERIFY]
- DOJ/SEC, _A Resource Guide to the U.S. Foreign Corrupt Practices Act_ (2d ed. 2020) [VERIFY]
- DOJ, _Evaluation of Corporate Compliance Programs_ (Sept. 2024) [VERIFY]
- DOJ, _FCPA Corporate Enforcement Policy_ (Nov. 2017, amended through 2024) [VERIFY]
- DOJ, _Guidelines for Investigations and Enforcement of FCPA_ (June 9, 2025) [VERIFY]
- _Liu v. SEC_, 591 U.S. 71 (2020) — disgorgement limits [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** (⟁ CLARIFY) at decision points where:

- The answer changes the scope or direction of the assessment
- Multiple valid analytical paths exist
- Context-specific facts are required to classify risk correctly
- Business judgment must supplement legal analysis

When marked ⟁ CLARIFY, present structured options. If the user has already provided the
information, skip the question and proceed. For batch/non-interactive runs, use the
default stated at each CLARIFY point.

---

## Workflow

### Step 1: Accept Input

Accept the assessment request in any format:

- **Compliance program documents**: Code of conduct, anti-corruption policy, GTE policy,
  third-party due diligence procedures, training records, internal audit reports
- **Transaction or incident description**: Narrative of specific conduct, payment, or
  practice to be assessed
- **M&A context**: Target company profile, geographic footprint, government-sector exposure
- **Prior enforcement context**: Existing DPA, NPA, declination with disgorgement, or
  monitorship terms
- **General program review request**: High-level ECCP compliance gap analysis without
  specific documents

If no input is provided beyond a general request for FCPA compliance review, proceed to
Step 2 and gather context before scoping the assessment.

---

### Step 2: Gather Organizational Context

**⟁ CLARIFY** — Before scoping the assessment, gather this context (skip what is already
known):

1. **Entity type and jurisdictional hook**:
   - Options: **Issuer** (securities registered/traded in US), **Domestic Concern**
     (US-incorporated entity or US citizen/resident/national), **Foreign Person/Entity
     with US nexus** (any person/entity with acts in US territory), Other/Unknown
   - _Why this matters_: Issuers face both DOJ and SEC enforcement; domestic concerns
     face DOJ criminal enforcement only; foreign persons/entities face DOJ if acts occurred
     in the US. Books-and-records provisions apply only to issuers.

2. **Geographic and sector risk profile**:
   - High-risk jurisdictions present? (FCPA enforcement concentrates in: China, Brazil,
     Russia, Middle East, Sub-Saharan Africa, Southeast Asia — but applies globally)
   - Government-sector exposure? (Transactions with state-owned enterprises, government
     agencies, foreign officials in regulatory/licensing roles)
   - Industry? (High-FCPA-enforcement industries: oil/gas, defense/aerospace,
     pharmaceutical/medical device, telecom, financial services, construction)
   - _Why this matters_: Risk-based scoping prioritizes higher-risk areas first.

3. **Assessment type**:
   - Options: **Full compliance program review** (all domains), **Focused risk assessment**
     (specific domain: third-party, GTE, books-and-records), **Incident response/VSD
     analysis** (specific alleged misconduct), **M&A pre-acquisition due diligence**,
     **Post-enforcement remediation review** (existing DPA/NPA/monitorship)
   - _Default for batch run_: Full compliance program review.

4. **Prior FCPA history**:
   - Existing DOJ/SEC resolution (DPA, NPA, declination, monitorship)?
   - Prior voluntary disclosure?
   - Current monitorship or self-reporting obligations?
   - _Why this matters_: Recidivism significantly affects enforcement outcomes and VSD credit.

5. **Priority output format**:
   - Options: **Executive compliance dashboard** (board/C-suite), **Detailed gap analysis**
     (compliance team/counsel), **Incident response brief** (immediate next steps for
     specific conduct), **M&A risk summary** (deal team)

State all assumptions explicitly before proceeding.

---

### Step 3: Load Legal Authority

Use **legalcode-mcp** to gather current FCPA authority relevant to the assessment scope.

**Research targets:**

1. Current version of DOJ FCPA Corporate Enforcement Policy (most recent amendment)
2. DOJ Evaluation of Corporate Compliance Programs (September 2024 version with AI/data updates)
3. DOJ June 2025 FCPA Enforcement Guidelines (Executive Order 14209 and post-pause policy)
4. Any recent DOJ Opinion Procedure Releases relevant to the industry/geography
5. Recent enforcement actions (declinations and resolutions) from the past 24 months
6. SEC enforcement actions against issuers for books-and-records violations in the sector
7. _United States v. Esquenazi_ and subsequent instrumentality case law

**Save results to** `/tmp/fcpa-assessment-authority.md` with structure:

```markdown
# FCPA Legal Authority Reference

## Date: [date]

## Assessment: [company/scope]

### DOJ Enforcement Policy — Current Status

- CEP version: [date of most recent amendment]
- June 2025 Guidelines: [key points]

### ECCP Key Requirements (September 2024)

- [AI/emerging tech risk element]
- [Data analytics access requirement]
- [Whistleblower protection standards]

### Recent Enforcement Benchmarks

- [Most recent penalty amounts for comparable violations]
- [Declination criteria applied]

### Instrumentality Case Law

- [Esquenazi standard and recent applications]
```

**Without legalcode-mcp**: Mark all citations [VERIFY]. Note in audit trail:
`legalcode_mcp: "Not connected — manual verification required"`. Proceed using
general knowledge, flagging uncertainty explicitly.

---

### Step 4: Anti-Bribery Provisions Assessment

Assess the organization's exposure and controls under 15 U.S.C. §§ 78dd-1/78dd-2/78dd-3
across five sub-domains. For each, classify the finding and generate a remediation action.

#### 4a. Foreign Official Identification and Interaction Controls

**Assess:**

- Does the organization maintain a current inventory of its interactions with "foreign
  officials" (government employees, officials of state-owned/controlled enterprises,
  political parties, and candidates for office)?
- Is the **instrumentality test** applied to counterparties?
  - _Esquenazi standard_: An entity is an "instrumentality" if (1) controlled by a foreign
    government and (2) performs a function the government treats as its own. [VERIFY]
  - Fact-specific inquiry: government ownership percentage, appointment of key officers,
    government designation, whether function is governmental in nature.
- Does the organization have a **government official interaction protocol** covering:
  - Pre-approval requirements for interactions with foreign officials?
  - Documentation standards (who, what, when, business purpose)?
  - Escalation procedures for unusual requests?
  - Prohibition on direct or indirect payments to officials' family members?

**⟁ CLARIFY** — If the organization operates in industries where SOE counterparties are
common (oil/gas, telecom, utilities, pharma, defense): "What percentage of the company's
revenue-generating interactions involve state-owned enterprise counterparties? This
determines whether instrumentality analysis should be a standard pre-contract step."

**Common issues:**

- Treating SOE employees as private parties without instrumentality analysis
- No definition of "anything of value" in training (e.g., internships for officials'
  relatives, scholarships, charitable donations with official connection)
- Missing controls for foreign subsidiaries operating with local staff

#### 4b. Business Purpose Test and Corrupt Intent Controls

**Assess:**

- Does the organization train on the **business purpose test**: payments or benefits to
  obtain or retain business, or to secure any improper advantage? The "business" element
  is construed broadly; DOJ does not require a specific contract award as the quo.
- Does training address **corrupt intent**: the payment must be intended to induce the
  official to misuse their position. Good-faith promotional expenditures without expectation
  of improper benefit are generally outside the statute.
- Does the organization prohibit **conduit payments**: routing prohibited payments through
  a subsidiary, agent, or shell company does not eliminate liability; the parent/principal
  retains liability if it knew or consciously avoided knowing of the routing.

#### 4c. Knowledge Standard and Willful Blindness Controls

**Assess:**

- Does the organization's anti-corruption policy address the **expanded knowledge standard**:
  "knowing" includes (a) actual knowledge, (b) firm belief that a circumstance exists, and
  (c) **conscious disregard / willful blindness** (awareness of high probability + deliberate
  failure to investigate)?
- Does the compliance program create accountability for employees who choose not to ask
  questions when faced with red flags?
- Are due diligence procedures designed to prevent the organization from claiming ignorance
  when warning signs were present?

**Note**: The 1988 FCPA amendments expressly excluded "simple negligence" or "mere
foolishness" from the knowledge standard. Corporate liability, however, extends to acts
of employees with apparent authority, even absent express authorization. [VERIFY]

#### 4d. Affirmative Defenses Assessment

Evaluate whether the organization can document either affirmative defense if needed:

| Defense                                            | Elements                                                                                                                            | Documentation Required                                                                                                                 |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Local law defense** (§ 78dd-1(c)(1))             | Payment is lawful under _written_ laws/regulations of the foreign official's country                                                | Written legal opinion from qualified local counsel confirming written legal authority; local practice/custom does NOT qualify          |
| **Bona fide promotional expense** (§ 78dd-1(c)(2)) | Reasonable and bona fide expenditure directly related to promotion/demonstration of products/services, or performance of a contract | Pre-approval records, vendor invoices, business purpose documentation, evidence government agency (not company) selected beneficiaries |

**Red flags indicating the defenses are unavailable:**

- Cash payments (no vendor invoices, no direct vendor payment)
- Company selected which officials would receive the benefit (not the government)
- Expenses include personal components (sightseeing, family expenses, luxury items)
- No prior legal opinion for local law defense
- Payment amount significantly exceeds actual costs

#### 4e. Facilitation Payment Analysis

**Assess:**

- Does the organization's policy address the **facilitation payment exemption**
  (15 U.S.C. § 78dd-1(b))? The exemption covers payments to a foreign official to
  expedite/secure performance of a "routine governmental action" — i.e., non-discretionary
  acts the official is already obligated to perform (processing papers, providing utilities,
  clearing goods through customs). [VERIFY]
- **Key distinction**: The exemption turns on the payment's purpose, not its value. A
  payment to obtain a _decision_ (e.g., permit approval, license grant, contract award)
  is NOT a facilitation payment even if small.
- **Enforcement trend (2020-2025)**: DOJ/SEC have narrowed their practical view of this
  exemption; companies should not rely on it for anything other than small, truly routine
  transactions. Several settlements have included conduct arguably within the exemption.
- Does the policy require **accurate recording** of facilitation payments where permitted?
  Mischaracterization as a business expense creates a separate books-and-records violation.

**⟁ CLARIFY** — "Does the organization currently maintain a facilitation payment policy?
Options: (1) Facilitation payments explicitly prohibited (zero-tolerance), (2) Facilitation
payments permitted up to a threshold with required documentation, (3) No specific policy
— addressed ad hoc, (4) Unknown."

---

### Step 5: Books and Records / Internal Controls Assessment

Assess compliance with 15 U.S.C. § 78m(b)(2)-(3). This section applies to **issuers only**;
however, DOJ/SEC frequently use it as an alternative or supplement to anti-bribery charges.

**⟁ CLARIFY** — If entity type not already confirmed: "Is the organization an issuer
(securities registered or traded on a US exchange or otherwise subject to SEC reporting
requirements)? If yes, § 78m accounting provisions apply directly. If not, proceed with
anti-bribery analysis only; note that non-issuers may still be charged under anti-bribery
provisions."

#### 5a. Books and Records (§ 78m(b)(2)(A))

**Requirements**: Books, records, and accounts must in _reasonable detail_ accurately and
fairly reflect all transactions and dispositions of assets. [VERIFY]

**Assess:**

- Are all payments — including gifts, entertainment, commissions to third parties,
  charitable donations, and sponsorships — accurately characterized in the books?
- Are commission/consulting arrangements documented with a clear business justification
  and output confirming the services were actually rendered?
- Does the organization prohibit **slush funds**, off-book accounts, or accounts maintained
  by third parties at the company's direction?
- Are payments to government officials (or officials' family members, related entities)
  accurately classified — not hidden as "marketing," "consulting fees," "processing fees,"
  or "government relations"?
- Are subsidiary records maintained to the same standard?

**Common violations:**

- Booking bribes as "promotional expenses," "consulting fees," or "commission payments"
- Maintaining petty cash funds for unofficial payments
- Using local agents to make payments and booking only the net amount received
- Inadequate documentation of commission arrangements with distributors/agents

#### 5b. Internal Controls (§ 78m(b)(2)(B))

**Requirements**: Issuers must devise and maintain a system of internal accounting controls
sufficient to provide reasonable assurance that transactions are executed in accordance
with management authorization, recorded properly for GAAP financial statement preparation,
access to assets is permitted only per management authorization, and recorded accountability
for assets is regularly reconciled with actual assets. [VERIFY]

**Assess against these control domains:**

| Control Domain                | Key Control Elements                                                                                                 | Common Weakness                                                            |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Payment authorization**     | Multi-level approval for payments involving government officials; pre-approval for anything above nominal thresholds | Single approver; no escalation for official-related payments               |
| **Commission/agent payments** | Contract with defined deliverables; payment conditioned on completion; per-transaction approval                      | Lump-sum retainers; payments without invoices or output                    |
| **GTE controls**              | Pre-approval workflow; business purpose required; aggregate tracking by official/agency                              | Post-hoc reconciliation only; no per-official tracking                     |
| **Charitable contributions**  | No contributions to charities nominated by officials; board-level approval for large donations                       | No screening for official connections; no board oversight                  |
| **Subsidiary oversight**      | Parent company approval for high-risk transactions; local finance reporting to group compliance                      | Fully autonomous subsidiaries; no parent review                            |
| **Segregation of duties**     | Finance/compliance independence from business; no single person controls payment and recording                       | Compliance embedded in business units; business head approves own expenses |

---

### Step 6: Third-Party Due Diligence Program Review

Third-party intermediaries are the source of approximately 90% of FCPA enforcement actions. [VERIFY]
Assess the organization's third-party due diligence program across the full lifecycle.

#### 6a. Program Architecture Assessment

Evaluate the seven-step lifecycle recommended by the DOJ FCPA Resource Guide (2d ed. 2020): [VERIFY]

| Step                             | Assessment Question                                                                                                                        | Compliant Indicator                                                                       |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| **1. Business justification**    | Does the organization document why the third party is needed and what services it will provide?                                            | Written business case; justification reviewed by compliance, not just business sponsor    |
| **2. Third-party questionnaire** | Does the organization use a structured questionnaire capturing ownership, government relationships, prior legal issues, beneficial owners? | Standardized questionnaire covering all required areas; annual re-certification           |
| **3. Risk scoring**              | Does the organization apply a risk-based framework to triage responses?                                                                    | Documented scoring methodology; residual risk thresholds triggering enhanced review       |
| **4. Risk-based due diligence**  | Does the depth of investigation match the risk level?                                                                                      | Tier 1: basic screening; Tier 2: deep internet/media; Tier 3: in-country/investigative    |
| **5. Red flag resolution**       | Does the organization document how identified red flags were resolved or mitigated before engagement?                                      | Written risk disposition memo; compliance sign-off required                               |
| **6. Contractual protections**   | Do contracts include FCPA representations, certifications, audit rights, and termination rights?                                           | Standard compliance contract language reviewed by legal; no exceptions without escalation |
| **7. Ongoing monitoring**        | Does the organization continuously monitor third parties post-engagement?                                                                  | Annual re-certification; periodic transaction auditing; renewal review                    |

#### 6b. Red Flag Matrix

**14-Category Red Flag Assessment** — For each engaged third party, evaluate against:

| #   | Category                        | Red Flag Indicators                                                                                                |
| --- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| 1   | **Government connection**       | Related to or recommended by a foreign official; spouse/child/associate of official has ownership interest         |
| 2   | **Qualifications**              | In a different line of business than retained for; lacks relevant experience, staff, or resources                  |
| 3   | **Value for money**             | Unusually high commission or fee without commercial justification; fee structure tied to government contracts won  |
| 4   | **Ownership opacity**           | Shell company in offshore jurisdiction; refusal to disclose beneficial owners/directors                            |
| 5   | **Payment routing**             | Requests payment to offshore account; requests cash or wire to unnamed account; requests unusual payment structure |
| 6   | **Contract resistance**         | Refuses written contract; insists on verbal arrangements; requests side letters inconsistent with main agreement   |
| 7   | **Audit resistance**            | Refuses audit rights clause; refuses compliance certifications; insists on confidentiality of its own identity     |
| 8   | **Compliance culture**          | Suggests anti-corruption policies don't need to apply; characterizes illegal conduct as "normal" locally           |
| 9   | **Track record**                | History of government investigations, sanctions, or adverse media; prior FCPA-adjacent issues                      |
| 10  | **Financial irregularities**    | History of unusual payment patterns; large undocumented cash transactions; prior fraud or bribery allegations      |
| 11  | **Third-party chain**           | Wants to use its own sub-agents unknown to company; multi-layer intermediary structures                            |
| 12  | **Urgency pressure**            | Unusual pressure to expedite due diligence or contract execution; engagement demanded before diligence complete    |
| 13  | **Government-business mixing**  | Acts simultaneously as a government official and commercial representative                                         |
| 14  | **Beneficial owner disconnect** | Named party is a front; actual decision-maker/beneficiary is different person with official connections            |

**⟁ CLARIFY** — For active third-party reviews: "How many active third parties with
government-sector exposure does the organization maintain? This determines whether sampling
or full-population review is appropriate."

#### 6c. Contractual Protections Assessment

**Required contract elements** for third parties with government-sector exposure:

- [ ] FCPA representations and warranties (third party represents compliance with anti-corruption laws)
- [ ] Annual written compliance certification
- [ ] Audit rights (right to audit books and records; right to audit third party's sub-agents)
- [ ] Termination for non-compliance (immediate termination right without penalty)
- [ ] No payment for undocumented services
- [ ] Payment terms aligned with actual services performed (milestone-based, not retainer)
- [ ] Disclosure obligation (third party to disclose changes in ownership, government relationships, legal proceedings)
- [ ] Flow-down obligations (third party ensures its sub-agents comply)
- [ ] Recordkeeping requirements (third party to maintain records of all interactions with officials)

---

### Step 7: Compliance Program Adequacy — ECCP Framework

Assess the organization's compliance program against the DOJ _Evaluation of Corporate
Compliance Programs_ (September 2024). The ECCP identifies three overarching questions:

1. **Is the compliance program well-designed?** (Risk-assessment, policies/procedures, training)
2. **Is the compliance program being applied earnestly and in good faith?** (Senior management
   commitment, resources, empowerment of compliance function)
3. **Does the compliance program work in practice?** (Testing, monitoring, investigation,
   continuous improvement)

**Note**: The ECCP is used by DOJ prosecutors to evaluate programs in _criminal enforcement
contexts_. Compliance with ECCP principles informs declination decisions, penalties, and
monitorship recommendations.

#### 7a. Program Design Assessment

| ECCP Element                | Assessment Question                                                                                   | Green Indicator                                                                                   | Common Gap                                                                         |
| --------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Risk Assessment**         | Is the risk assessment dynamic, data-driven, and updated based on changes in business or environment? | Annual formal assessment + interim updates; documented methodology                                | Static, calendar-driven checkbox exercise                                          |
| **Policies and Procedures** | Are FCPA-specific policies accessible, understandable, and kept current?                              | Searchable policy portal; version control; annual review cycle                                    | Outdated policies; policies inaccessible to field personnel                        |
| **Training**                | Is training tailored to role, jurisdiction, and risk level? Is comprehension measured?                | Role-based training modules; post-training assessment; high-risk employee certification           | Annual checkbox training; no comprehension testing; same content for all employees |
| **Reporting Mechanisms**    | Are confidential reporting channels available, widely communicated, and protected from retaliation?   | Multiple reporting channels (hotline, ombudsperson, web portal); multi-language; anonymous option | Single channel; fear of retaliation; management handles own reports                |
| **Third-Party Program**     | Is the third-party due diligence program risk-based and covers full lifecycle?                        | (Assessed in Step 6 above)                                                                        |                                                                                    |
| **M&A Integration**         | Is FCPA due diligence conducted pre-closing and integrated post-closing within 180 days?              | Pre-acquisition FCPA risk assessment; 180-day post-closing audit and integration plan             | No M&A-specific FCPA protocol; legacy practices uncorrected                        |

#### 7b. Earnestness and Culture Assessment

| ECCP Element                      | Assessment Question                                                                                           | Green Indicator                                                                                               | Common Gap                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Tone from the top**             | Do senior leaders visibly champion compliance? Do they create genuine "psychological safety" to raise issues? | CEO/Board messaging; senior leader participation in compliance activities                                     | Compliance treated as legal formality; leaders who made money on corrupt deals unpunished |
| **Compliance function resources** | Does compliance have adequate headcount, budget, technology, and data access equal to business functions?     | Compliance budget benchmarked to peers; compliance team has same data access as business (ECCP 2024 emphasis) | Compliance underfunded; compliance lacks access to transaction data                       |
| **Incentives and accountability** | Are compensation/promotion decisions tied to compliance performance? Are misconduct consequences enforced?    | Compliance component in performance reviews; documented clawback/discipline cases                             | Compliance failures overlooked for top revenue performers                                 |
| **Independence**                  | Does the compliance function have an independent reporting line (to board/audit committee)?                   | CCO reports directly to CEO and independently to Board Audit Committee                                        | CCO reports to General Counsel with no board access                                       |

#### 7c. AI and Emerging Technology Risks (ECCP September 2024)

The September 2024 ECCP update introduced heightened expectations for AI risk management: [VERIFY]

**Assess:**

- Does the compliance program identify, assess, and mitigate **AI-related corruption risks**?
  (e.g., AI-driven procurement decisions that could mask bribery, algorithmic selection of
  foreign agents, AI-assisted expense approvals that bypass human review)
- Does the compliance function have **equal access to data and analytics tools** as business
  functions? DOJ expects compliance to leverage data to identify anomalies, not just receive
  data on request.
- Are **automated decision-making systems** that affect government-related transactions
  subject to compliance review and audit?

#### 7d. Continuous Improvement Assessment

| ECCP Element               | Assessment Question                                                                                                                                   | Green Indicator                                                                        |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Lessons learned**        | Does the compliance program incorporate lessons from internal investigations, employee reports, industry peer incidents, and regulatory developments? | Documented lessons-learned process; policy updates triggered by incidents              |
| **Testing and monitoring** | Are compliance controls tested for design and operating effectiveness (not just documented)?                                                          | Annual control testing; transaction-level auditing in high-risk areas                  |
| **Investigation function** | Are allegations investigated promptly, independently, and with appropriate seniority?                                                                 | CCO/Legal involvement in all significant investigations; investigation metrics tracked |
| **Remediation**            | Are root causes identified and addressed after misconduct? Are controls improved?                                                                     | Post-investigation remediation tracked to closure; recurrence monitored                |

---

### Step 8: Enforcement Exposure Scoring

After completing Steps 4-7, calculate the overall enforcement exposure profile.

#### 8a. Anti-Bribery Exposure

| Factor                                                         | Weight | Assessment                                             |
| -------------------------------------------------------------- | ------ | ------------------------------------------------------ |
| Specific corrupt payments identified or suspected              | High   | CRITICAL if specific payments identified               |
| High-risk geography / government-sector exposure               | Medium | Escalates baseline risk                                |
| Weak foreign official identification and GTE controls          | Medium |                                                        |
| Poor third-party due diligence / multiple red flags unresolved | High   |                                                        |
| Prior FCPA resolution (recidivism factor)                      | High   | Significantly increases penalty and reduces VSD credit |

#### 8b. Books and Records Exposure (Issuers Only)

| Factor                                              | Weight   | Assessment                      |
| --------------------------------------------------- | -------- | ------------------------------- |
| Inaccurate characterization of payments in books    | High     | Direct § 78m(b)(2)(A) violation |
| Slush funds, off-book accounts                      | Critical |                                 |
| Inadequate commission/agent payment documentation   | Medium   |                                 |
| No internal controls over official-related payments | High     | § 78m(b)(2)(B) violation        |

#### 8c. Penalty Range Modeling

| Violation Type                             | Potential Penalty                                        | Notes                                                                                |
| ------------------------------------------ | -------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Anti-bribery — criminal (corporate)        | Up to $2M per violation, or twice the gain/loss [VERIFY] | Gain/loss measure typically drives outcomes in major cases                           |
| Anti-bribery — civil (corporate, SEC)      | Up to $16,000 per violation [VERIFY]                     | Rarely the limiting factor in major cases                                            |
| Books/records/internal controls — criminal | Up to $25M per violation [VERIFY]                        |                                                                                      |
| Disgorgement                               | Net profits from the conduct                             | _Liu v. SEC_ (2020): limited to net profits; must be distributed to victims [VERIFY] |
| Monitorship                                | Typically $1M-$5M+ per year for 2-5 years                | Imposed when compliance program is significantly deficient                           |
| Individual (criminal)                      | Up to $250K per violation (natural persons)              | Subject to Fine Reform Act alternative maximums [VERIFY]                             |

---

### Step 9: Voluntary Self-Disclosure Decision Analysis

The decision to voluntarily disclose to DOJ under the Corporate Enforcement Policy (CEP)
is one of the most consequential decisions an FCPA investigation triggers. This step
provides a structured decision framework.

#### 9a. Corporate Enforcement Policy (CEP) — Current Status

The CEP (most recently amended through 2024, with June 2025 policy guidance) provides: [VERIFY]

**If company voluntarily self-discloses, fully cooperates, and fully remediates:**

- **Presumption of declination** (no criminal charges) — even if aggravating factors are present
- If declination not appropriate (e.g., involvement of senior management, egregious conduct,
  recidivism): 50% reduction from low end of US Sentencing Guidelines fine range
- No monitorship if company has implemented effective compliance program at time of resolution

**August 2024 Update — 120-Day Rule**: A company that self-discloses within 120 days of
receiving an internal report (e.g., whistleblower complaint) — and before DOJ outreach —
qualifies for the full CEP presumption of declination. [VERIFY]

#### 9b. VSD Decision Matrix

Apply this decision framework sequentially:

| Question                                                                                                     | YES →                                                                        | NO →                                                                                              |
| ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| 1. Is there credible evidence of an FCPA violation?                                                          | Continue to Q2                                                               | VSD likely premature — complete investigation first                                               |
| 2. Has DOJ/SEC already commenced an investigation?                                                           | VSD still possible but full CEP credit unlikely; immediately consult counsel | Continue to Q3                                                                                    |
| 3. Was the violation limited to a small group without senior management involvement?                         | Continue to Q4                                                               | VSD strongly advised — senior involvement is aggravating factor that makes non-disclosure riskier |
| 4. Has the company conducted a thorough internal investigation establishing the full scope?                  | Continue to Q5                                                               | Disclose material known facts now; preserve right to supplement                                   |
| 5. Is the company prepared to cooperate fully (produce documents, make witnesses available, share findings)? | Continue to Q6                                                               | Assess whether cooperation obligations are feasible before disclosing                             |
| 6. Can the company remediate and disgorge the benefit of the violation?                                      | VSD likely to yield declination or significantly reduced penalty             | Assess whether remediation feasibility is a VSD prerequisite                                      |

**2025 Policy Shift**: The June 2025 DOJ Guidelines de-emphasize FCPA enforcement against
companies based on isolated employee conduct absent strong corporate culpability. Companies
with strong compliance programs may face lower enforcement risk even without VSD in certain
cases. **[VERIFY current enforcement posture with FCPA counsel before deciding]** [VERIFY]

#### 9c. VSD Timing and Process

**Key steps if VSD is determined appropriate:**

1. Confirm FCPA counsel engagement (specialized counsel, not generalist)
2. Implement litigation/investigation hold immediately
3. Conduct or confirm scope of internal investigation
4. Evaluate whether any whistleblower has already filed SEC Dodd-Frank complaint
5. Evaluate multi-jurisdiction exposure (UK SFO, EU prosecutors) before US disclosure
6. Prepare disclosure package: facts known, investigation plan, voluntary remediation steps
7. Disclose to DOJ Fraud Section (anti-bribery) and SEC (if issuer)
8. Execute cooperation and remediation plan fully and contemporaneously

---

### Step 10: M&A Successor Liability Analysis

**⟁ CLARIFY** — Apply this step only when an M&A context has been identified: "Is this
assessment for a pre-acquisition target, a recently acquired company, or a post-acquisition
integration review?"

#### 10a. Successor Liability Principles

- **Successor liability is a fundamental FCPA risk**: The acquiring entity inherits the
  target's criminal and civil FCPA exposure, regardless of deal structure (asset vs. stock
  acquisition distinction has limited practical impact in DOJ enforcement). [VERIFY]
- **No knowledge defense**: An acquirer cannot avoid successor liability by demonstrating
  it did not know of the target's misconduct — though pre-acquisition knowledge and
  diligence may affect penalty calculations.
- **Pre-closing window**: If FCPA violations are discovered during due diligence, the
  acquirer should consider: (1) deal price adjustment, (2) indemnification/escrow,
  (3) representations and warranties insurance, (4) pre-closing VSD to DOJ.
- **Post-closing obligations**: DOJ expects integration of target's compliance program
  within approximately 180 days of closing. Failure to integrate within this window
  (especially if post-closing violations occur) has resulted in successor liability being
  enforced against acquirers. [VERIFY]

#### 10b. Pre-Acquisition Due Diligence Checklist

| Diligence Area            | Key Questions                                                                                          | Risk Indicator                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| Geographic footprint      | What countries does the target operate in? Which have high FCPA enforcement history?                   | Multiple high-risk jurisdictions                            |
| SOE exposure              | What percentage of revenue comes from government contracts or SOE relationships?                       | >25% government revenue                                     |
| Agent/distributor network | Does the target use local agents/distributors for government-sector business?                          | Large agent network with high commissions, minimal controls |
| Prior allegations         | Any prior FCPA investigations, whistleblower complaints, internal audits flagging unusual payments?    | Prior complaints unresolved                                 |
| Accounting practices      | Are commissions, discounts, and promotional expenses accurately characterized?                         | Unusual patterns in marketing/promo spend                   |
| Compliance program        | Does the target have a documented FCPA compliance program? When was it last updated?                   | No program or program last updated >3 years ago             |
| Transaction records       | Are high-risk payment types (government permits, expediting fees, agent commissions) fully documented? | Missing invoices, cash payments                             |

---

## Severity Classification

Classify each compliance domain using the four-tier system:

### COMPLIANT — Controls Adequate

The organization has designed and implemented effective controls for this domain. No
material gaps identified. Program meets or exceeds ECCP expectations.

**Indicators**: Documented policies, regular training, effective monitoring, tested controls,
no unresolved red flags, compliance culture supported from top.

**Action**: Document as compliant. Note for next review cycle.

### PARTIAL — Gaps Identified, Low-to-Medium Risk

The organization has some controls in place but material gaps exist. The gaps do not
indicate an immediate enforcement risk but require remediation within 6-12 months to
maintain an adequate compliance posture.

**Indicators**: Policies exist but are outdated, training is generic, monitoring is limited,
some red flags exist but without evidence of actual violations.

**Action**: Identify gap, assign owner, set 90-day remediation target.

### NON-COMPLIANT — Material Deficiency, High Risk

The organization lacks controls in a material domain or has controls that are not
functioning effectively. Enforcement risk is elevated. If a violation occurs in this area,
inability to demonstrate an effective program significantly impacts enforcement outcome.

**Indicators**: No policy covering a key domain, training not conducted in >2 years,
third-party due diligence not performed for material counterparties, known red flags
unresolved for >90 days.

**Action**: Immediate remediation plan. Escalate to senior management and board.
Consider whether incident-specific investigation is warranted.

### CRITICAL DEFICIENCY — Immediate Enforcement Exposure

There is credible evidence of specific FCPA violations, or controls are so fundamentally
absent that any violation in this area would be treated by DOJ/SEC as evidence of willful
disregard of legal obligations.

**Indicators**: Specific payments to foreign officials that meet anti-bribery elements,
materially false books and records, third-party payments with no documentation for services
rendered, slush funds.

**Action**: Engage FCPA counsel immediately. Implement litigation hold. Begin internal
investigation. Evaluate VSD decision process (Step 9).

---

## Actionable Output Per Finding

For each finding, generate this structured output:

**COMPLIANT finding:**

```
Domain: [Anti-Bribery | Books/Records | Third-Party Due Diligence | GTE | ECCP Program]
Classification: COMPLIANT
Finding: [One-sentence description of what was assessed and found adequate]
Evidence: [Specific controls, policies, or practices that support COMPLIANT classification]
Next Review: [Date for next assessment of this domain]
```

**PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY finding:**

```
Domain: [Domain]
Classification: [PARTIAL | NON-COMPLIANT | CRITICAL DEFICIENCY]
Finding: [One-sentence description of the gap or deficiency]
Risk: [Why this matters: specific FCPA provision, enforcement precedent, or exposure]
Evidence: [Specific controls missing or failing]
Remediation: [Specific action required, not vague advice]
Owner: [Role responsible for remediation]
Deadline: [IMMEDIATE (72 hours) | 30 DAYS | 90 DAYS | 180 DAYS]
Escalation: [Required escalation: CCO | General Counsel | Audit Committee | Board]
```

---

## Prioritization Framework

### Tier 1 — IMMEDIATE (within 72 hours)

Address before any other action:

- Credible evidence of specific FCPA violations currently occurring
- Payments to foreign officials that have not been properly documented or are unexplained
- Employees or agents instructed to destroy or alter records
- Pending government inquiry or investigation for which a litigation hold is not yet in place
- Active facilitation of corrupt payments through company systems or accounts

### Tier 2 — NEAR-TERM (30-90 days)

Address with dedicated resources and tracking:

- Material gaps in third-party due diligence for high-risk counterparties currently active
- Absence of FCPA-specific policies covering material risk domains
- Unresolved third-party red flags for active engagements
- GTE controls absent or not functioning for government-sector activities
- Books and records practices that could constitute a § 78m violation if examined

### Tier 3 — BACKGROUND (90-180 days)

Address in normal compliance calendar:

- Program enhancements to close gap between PARTIAL and COMPLIANT classifications
- Training refresh for low-risk employee populations
- Third-party contract clause updates at next renewal cycle
- Risk assessment refresh based on geographic or business expansion
- ECCP alignment review against September 2024 updates (AI, data analytics, whistleblower)

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                              | Fail Action                                                         |
| -------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Source**     | Every FCPA legal claim cites 15 U.S.C. provision, DOJ/SEC guidance, or court decision                             | Add citation or mark "[UNVERIFIED — FCPA counsel to confirm]"       |
| **Format**     | All US citations use standard legal format (statute section, case name/citation, guidance title/date)             | Fix format                                                          |
| **Currency**   | DOJ enforcement policy and ECCP citations checked for amendment since September 2024; note June 2025 policy shift | Flag "[CHECK CURRENCY — DOJ enforcement posture changed June 2025]" |
| **Domain**     | Analysis stays within US FCPA law; no UK Bribery Act or other regime principles imported without flagging         | Remove or flag cross-regime bleed                                   |
| **Confidence** | Uncertainty stated explicitly, not hidden; never assert declination or enforcement outcome as guaranteed          | Add explicit qualifier                                              |

---

## Self-Interrogation for CRITICAL DEFICIENCY Items

For any finding classified as CRITICAL DEFICIENCY, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the risk follow logically from the FCPA provision cited?
- Would DOJ/SEC actually reach this conclusion based on the facts described?
- Is there a counter-argument the company's counsel would make (e.g., the facilitation
  payment exemption applies; the payment was genuinely promotional)?

**Pass 2 — Completeness**:

- Have all relevant provisions been considered (anti-bribery + books/records + internal controls)?
- Have relevant enforcement actions with comparable facts been reviewed?
- Are there regulatory dimensions not yet addressed (SEC vs. DOJ; individual vs. corporate)?

**Pass 3 — Challenge**:

- What is the strongest argument that this is NOT a CRITICAL DEFICIENCY?
- Under what circumstances would DOJ/SEC exercise prosecutorial discretion to decline?
- Is the classification proportionate, or could strong mitigating factors (robust compliance
  program, voluntary disclosure, cooperation) reduce the effective exposure?

Mark audit trail: `self_interrogation: PASS` or `self_interrogation: REVISED`.

---

## Confidence Scoring

For each material finding, assign a confidence level:

| Level        | Range     | Meaning                                           | FCPA Application                                                                                                          |
| ------------ | --------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled law, clear statute, direct precedent      | Payment to confirmed government official with documented corrupt intent; § 78m mischaracterization with documentary proof |
| **High**     | 0.80-0.94 | Strong authority, minor factual questions         | Instrumentality status clearly met under Esquenazi; control gap clearly documented against ECCP standard                  |
| **Probable** | 0.60-0.79 | Good arguments but factual development incomplete | SOE instrumentality analysis pending additional facts; red flag analysis where facts cut both ways                        |
| **Possible** | 0.40-0.59 | Genuinely uncertain; enforcement outcome unclear  | Novel fact pattern; 2025 enforcement posture change affects outcome prediction                                            |
| **Unlikely** | 0.0-0.39  | Speculative or weak basis                         | Do not assert; flag "[UNCERTAIN — FCPA counsel to advise]"                                                                |

---

## Glass Box Audit Trail

Every FCPA assessment output MUST include this audit section:

```yaml
glass_box:
  skill_name: "legalcode-us-fcpa-compliance"
  assessment_date: "[date]"
  entity: "[entity assessed — or 'Confidential']"
  entity_type: "[Issuer | Domestic Concern | Foreign Person/Entity | Unknown]"
  assessment_type: "[Full Program Review | Focused Domain | Incident Response | M&A | Post-Enforcement]"
  geographic_risk_profile: "[High-risk jurisdictions identified]"
  government_sector_exposure: "[percentage or 'Unknown']"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to temp file or 'Not created']"
  statutes_cited:
    - "15 U.S.C. § 78dd-1 — [VERIFIED/UNVERIFIED]"
    - "15 U.S.C. § 78dd-2 — [VERIFIED/UNVERIFIED]"
    - "15 U.S.C. § 78m(b)(2) — [VERIFIED/UNVERIFIED]"
  guidance_cited:
    - "DOJ FCPA Resource Guide 2d ed. 2020 — [VERIFIED/UNVERIFIED]"
    - "DOJ ECCP September 2024 — [VERIFIED/UNVERIFIED]"
    - "DOJ CEP / June 2025 Guidelines — [VERIFIED/UNVERIFIED]"
  case_law_cited:
    - "United States v. Esquenazi, 752 F.3d 912 — [VERIFIED/UNVERIFIED]"
    - "Liu v. SEC, 591 U.S. 71 (2020) — [VERIFIED/UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number total]"
  domains_assessed: "[list: Anti-Bribery | Books/Records | Third-Party DD | GTE | ECCP | VSD | M&A]"
  critical_deficiencies: "[number]"
  non_compliant: "[number]"
  partial: "[number]"
  compliant: "[number]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL DEFICIENCY items)"
  vsd_analysis_completed: "[Yes / No / Not applicable]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  june_2025_policy_note: "FCPA enforcement posture changed materially as of June 2025. Verify current enforcement guidance with FCPA counsel before making VSD or remediation decisions."
  limitations:
    - "[Scope limitations, documents not reviewed, facts not confirmed]"
    - "[Any factual assumptions made]"
  reviewer: "AI-assisted — requires qualified FCPA counsel review before reliance"
```

---

## Anti-Patterns

**20 common FCPA compliance failures that this skill is designed to surface:**

1. **Treating SOE employees as private counterparties** — State-owned enterprises may be
   government instrumentalities under Esquenazi. Failing to apply the foreign official
   analysis to SOE employees is one of the most common causes of inadvertent violations in
   high-risk markets.

2. **Overrelying on the facilitation payment exemption** — The exemption is narrow and
   increasingly prosecuted. Booking payments as "facilitation" when they involve any
   element of discretion by the official, or characterizing them as facilitation merely
   because they are small, creates compounded exposure (anti-bribery + books/records).

3. **Using agents to create distance from payments** — Routing prohibited payments through
   agents, consultants, or JV partners does not insulate the company. Wilful blindness to
   an agent's use of funds is sufficient for liability. "I didn't know how they got the
   permits" is not a defense if red flags were present.

4. **Generic annual training** — Checkbox training without role-specific content, real
   scenarios, or comprehension testing fails the ECCP standard. DOJ prosecutors look for
   evidence of genuine understanding, not attendance records.

5. **Quarterly GTE reports reviewed only by the approving manager** — GTE policies require
   independent review. Business-unit managers approving their own teams' expenses, without
   a compliance check, eliminate the control value of the approval process.

6. **High commissions treated as "market practice"** — Unusually high commissions (e.g.,
   15-30% on government-sector contracts) are a well-known red flag. Accepting them because
   "everyone does it in [country]" does not provide a defense and may constitute willful
   blindness.

7. **Post-hoc due diligence rationalization** — Conducting third-party due diligence after
   the business decision has been made, or treating due diligence as a compliance formality
   that validates a pre-determined outcome, defeats its purpose and will not satisfy the ECCP.

8. **M&A integration delay beyond 180 days** — Failing to audit and integrate an acquired
   company's compliance program within approximately 180 days post-closing, particularly
   when the target operates in high-risk markets, eliminates the "successor integrated
   compliance" argument and extends exposure.

9. **Local law defense without written legal opinion** — The local law defense requires that
   the payment be lawful under the _written_ laws of the relevant jurisdiction. Relying on
   verbal assurances from local counsel, customary practice, or "everyone does it" claims
   does not establish the defense.

10. **Charitable donations nominated by officials** — Directing charitable contributions
    to charities or causes suggested by or associated with foreign officials is a well-
    established enforcement pattern. The fact that the ultimate recipient is a charity does
    not make the donation to obtain business lawful.

11. **Training employees in low-risk roles and not those in high-risk roles** — A common
    inversion: companies train all employees on a generic version but provide minimal or no
    specialized training to the sales, procurement, and government relations personnel who
    face actual FCPA risk. ECCP requires risk-tailored training.

12. **Inadequate escalation path for field employees** — Compliance programs that are
    difficult to access, culturally discouraged, or where escalation is seen as career risk
    fail the earnestness element of the ECCP. Front-line employees in high-risk markets
    need practical, accessible guidance.

13. **No aggregate tracking of GTE by official or agency** — Individual expenses that are
    within nominal thresholds can aggregate to a pattern of systemic inducement. Companies
    that track expenses per transaction but not per official-agency combination miss the
    aggregate picture that DOJ/SEC will reconstruct.

14. **Subsidiary management compensation tied entirely to revenue** — Incentive structures
    that reward revenue without any compliance component create pressure toward corrupt
    conduct. The ECCP requires that compensation and promotion decisions incorporate
    compliance performance.

15. **Compliance function without data access** — The September 2024 ECCP update explicitly
    requires that compliance personnel have equal access to data as business functions. A
    compliance team that must request data from finance or IT on a case-by-case basis cannot
    perform the proactive monitoring the ECCP requires.

16. **VSD before scope is known** — Disclosing to DOJ before completing an internal
    investigation to understand the scope of the misconduct leads to incomplete initial
    disclosures that can damage credibility and complicate cooperation. Complete a reasonable
    scope of investigation before disclosing.

17. **VSD without FCPA-specialized counsel** — The CEP process involves complex negotiations
    with the DOJ Fraud Section. General corporate counsel, even with compliance experience,
    may not have the specialized knowledge of CEP mechanics, cooperation credit, and
    individual accountability considerations that a matter of this type requires.

18. **Recidivism-aggravated posture ignored** — Companies with prior FCPA resolutions face
    significantly higher penalties and reduced CEP credit. Assessment of a repeat offender
    should explicitly model the recidivism premium in penalty projections.

19. **Paper policies without operational testing** — Policies that exist in writing but have
    never been tested for whether they are understood, accessible, and followed in practice
    are explicitly targeted by the ECCP "does it work?" question. Paper compliance is not
    compliance.

20. **Ignoring the individual accountability dimension** — Focusing exclusively on corporate
    exposure while failing to identify and protect individual employees (and assess whether
    individual prosecutions are likely) is incomplete. Employees who participated in violations
    may become DOJ cooperators; employees who had supervisory responsibility may face
    individual charges even absent personal corrupt intent.

---

## Writing Standards

Apply plain-language discipline to all FCPA assessment output:

**For findings and remediation steps** (shared with compliance team, counsel, and potentially regulators):

- Active voice: "The company must implement pre-approval controls" not "Pre-approval controls
  should be implemented by the company"
- Specific, not vague: "No FCPA training has been conducted for the Brazil sales team since
  2022" not "Training may need improvement in some regions"
- Name the provision: cite the specific FCPA section or ECCP element, not just "applicable law"
- Actionable deadlines: "Implement by March 31" not "as soon as practicable"
- Distinguish finding from risk from remediation — these are three separate things

**For board/C-suite summaries**:

- Lead with the material findings, not process descriptions
- Translate legal risk into business terms (enforcement probability, penalty range,
  operational disruption, reputational impact)
- No legal jargon without plain-language explanation in the same sentence

**Quality gates before delivery**:

- [ ] No finding without a specific supporting fact
- [ ] No legal claim without a cited authority (or explicit [VERIFY] marker)
- [ ] No enforcement outcome asserted as certain (DOJ/SEC have prosecutorial discretion)
- [ ] All [VERIFY] markers represent genuine uncertainty, not general hedging
- [ ] Remediation steps are specific enough to be acted upon without further interpretation
- [ ] VSD decision analysis clearly distinguishes between "benefits of VSD" and "guarantee of outcome"

---

## External Tool Integration

**With legalcode-mcp connected (preferred)**:

- Search for: current DOJ FCPA enforcement policy and any 2025 amendments, ECCP current
  version with AI/emerging tech additions, recent CEP declination letters, _United States
  v. Esquenazi_ [752 F.3d 912] and subsequent instrumentality decisions, _Liu v. SEC_
  [591 U.S. 71] and disgorgement limits, SEC and DOJ Opinion Procedure Releases for the
  relevant industry/geography
- Save verified authority to `/tmp/fcpa-assessment-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp**:

- Proceed with general FCPA knowledge from training data
- Mark all statutory and case law citations [VERIFY]
- Add note to Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Specifically flag the June 2025 enforcement guidance as a high-currency-risk item
  requiring manual verification before reliance

**Related skills**:

- `legalcode-anti-bribery-compliance` — for multi-regime assessments including UK Bribery
  Act, Sapin II, and Brazil Clean Company Act alongside FCPA
- `legalcode-internal-investigation` — for FCPA investigation lifecycle management once
  misconduct is identified (includes VSD mechanics and cooperation protocol)
- `legalcode-compliance-risk-assessment` — for enterprise-wide compliance risk assessment
  incorporating FCPA within the broader risk universe
- `legalcode-policy-gap-analysis` — for detailed policy adequacy mapping against ECCP
  and FCPA-specific policy requirements

---

## Output Format Template

Deliver the assessment in this format:

---

```markdown
# FCPA Compliance Assessment

**Entity**: [Name / Confidential]
**Entity Type**: [Issuer | Domestic Concern | Foreign Person/Entity]
**Assessment Date**: [Date]
**Assessment Scope**: [Full Program | Focused Domain | Incident Response | M&A | Post-Enforcement]
**Prepared by**: AI-assisted (legalcode-us-fcpa-compliance) — requires FCPA counsel review

---

## Executive Summary

| Domain                           | Classification                                                    | Priority     |
| -------------------------------- | ----------------------------------------------------------------- | ------------ |
| Anti-Bribery Controls            | [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]       | [Tier 1/2/3] |
| Books & Records (Issuers only)   | [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY / N/A] | [Tier 1/2/3] |
| Internal Controls (Issuers only) | [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY / N/A] | [Tier 1/2/3] |
| Third-Party Due Diligence        | [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]       | [Tier 1/2/3] |
| Gifts / Travel / Entertainment   | [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]       | [Tier 1/2/3] |
| Compliance Program (ECCP)        | [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]       | [Tier 1/2/3] |
| M&A / Successor Liability        | [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY / N/A] | [Tier 1/2/3] |

**Overall Posture**: [COMPLIANT | PARTIAL | NON-COMPLIANT | CRITICAL DEFICIENCY]
**VSD Analysis Required**: [Yes / No / Monitor]
**FCPA Counsel Engagement Recommended**: [Immediate / Within 30 days / Next review cycle]

---

## Detailed Findings

### [Domain 1 — e.g., Anti-Bribery Controls]

**Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]
**Confidence**: [Definite / High / Probable / Possible / Unlikely] ([range])

#### Findings

| #   | Finding               | Classification   | Priority |
| --- | --------------------- | ---------------- | -------- |
| 1.1 | [Finding description] | [Classification] | [Tier]   |
| 1.2 | [Finding description] | [Classification] | [Tier]   |

#### Remediation Actions

| #   | Action            | Owner  | Deadline | Status |
| --- | ----------------- | ------ | -------- | ------ |
| 1.1 | [Specific action] | [Role] | [Date]   | Open   |

[Repeat for each domain]

---

## Enforcement Exposure Analysis

**Anti-Bribery**: [Summary of exposure if specific violations identified]
**Books/Records** (if issuer): [Summary]
**Penalty Range**: [Low estimate / High estimate based on gain/loss or violation count]
**Monitorship Risk**: [Low / Medium / High — rationale]

---

## VSD Decision Analysis

**VSD Trigger**: [Yes — specific conduct warrants analysis | No — no credible violation identified]

[If Yes:]
**CEP Qualification Assessment**:

- Timely disclosure: [Met / Not met / Unknown]
- Full cooperation: [Committed / Conditional / Unknown]
- Full remediation: [Complete / In progress / Not yet started]
- Disgorgement/forfeiture: [Amount estimated / Not yet calculated]

**Recommendation**: [Disclose now | Complete investigation before disclosing | Monitor | Engage FCPA counsel for decision]
**Note**: This recommendation is not legal advice. VSD decisions must be made with qualified FCPA counsel.

---

## Priority Remediation Roadmap

### Tier 1 — Immediate (within 72 hours)

- [ ] [Action 1]
- [ ] [Action 2]

### Tier 2 — Near-Term (30-90 days)

- [ ] [Action 1]
- [ ] [Action 2]

### Tier 3 — Background (90-180 days)

- [ ] [Action 1]
- [ ] [Action 2]

---

## Glass Box Audit Trail

[Insert completed glass_box YAML block]

---

_FCPA Compliance Assessment generated using legalcode-us-fcpa-compliance skill (Legalcode, 2026).
This output is AI-assisted and does not constitute legal advice. Verify all citations against
current DOJ/SEC authoritative sources. Engage qualified FCPA counsel before acting on any
finding in this report. The June 2025 DOJ enforcement guidelines represent a significant
policy shift — current enforcement posture must be independently verified._
```

---

## Localization Notes

This skill is US-law-only. When international exposure is present:

- **Multi-regime coverage**: If the organization is subject to UK Bribery Act 2010, Sapin II
  (France), or Brazil Clean Company Act in addition to the FCPA, use `legalcode-anti-bribery-compliance`
  for a combined multi-regime assessment.
- **Local law affirmative defense**: Requires qualified local counsel opinion on the _written_
  laws of each relevant jurisdiction. This skill identifies the defense but does not evaluate
  local law requirements — that requires jurisdiction-specific analysis.
- **Cross-border disclosure coordination**: VSD to DOJ/SEC may affect obligations to UK SFO,
  French PNF, or Brazilian CGU. Coordinate multi-jurisdictional disclosure strategy with
  counsel in each jurisdiction before disclosing.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

- DOJ/SEC FCPA Resource Guide (2d ed. 2020) [VERIFY]
- DOJ Evaluation of Corporate Compliance Programs (September 2024) [VERIFY]
- DOJ FCPA Corporate Enforcement Policy (November 2017, amended through August 2024) [VERIFY]
- DOJ Guidelines for Investigations and Enforcement of FCPA (June 9, 2025) [VERIFY]
- _United States v. Esquenazi_, 752 F.3d 912 (11th Cir. 2014) — instrumentality definition [VERIFY]
- _Liu v. SEC_, 591 U.S. 71 (2020) — disgorgement limits [VERIFY]
- Repository best practices from `legalcode-anti-bribery-compliance`, `legalcode-internal-investigation`,
  and `legalcode-compliance-risk-assessment`
- Legalcode Agent Team research synthesis (2-agent parallel analysis of reference skills and legal research)

**Related skills**: `legalcode-anti-bribery-compliance` (multi-regime),
`legalcode-internal-investigation` (investigation lifecycle), `legalcode-compliance-risk-assessment`
(enterprise risk assessment), `legalcode-policy-gap-analysis` (policy mapping).
