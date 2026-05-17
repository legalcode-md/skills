---
name: legalcode-third-party-due-diligence
description: >
  Conduct anti-corruption due diligence on agents, distributors, joint venture partners,
  consultants, and other third-party intermediaries. Covers risk tiering, red flag analysis,
  due diligence questionnaire (DDQ) design, sanctions and debarment screening, contractual
  anti-corruption provisions, and ongoing monitoring. Aligns with DOJ FCPA guidance and DOJ
  Guidelines for Evaluation of Corporate Compliance Programs, UK Bribery Act 2010 Section 7
  "adequate procedures" and Ministry of Justice six principles, OECD Good Practice Guidance
  on Internal Controls Ethics and Compliance, and World Bank / multilateral development bank
  debarment framework. Use when onboarding a new agent, distributor, or JV partner in a
  high-risk jurisdiction; when reviewing the adequacy of an existing third-party compliance
  program; when designing or improving a third-party risk management (TPRM) workflow; when
  preparing for DOJ/SEC FCPA inquiry or UK SFO investigation; or when a specific third party
  has raised red flags. Triggers on: "third-party due diligence," "TPRM," "agent screening,"
  "distributor compliance," "JV partner vetting," "FCPA third-party risk," "UK Bribery Act
  adequate procedures," "World Bank debarment," "PEP screening," "anti-corruption
  questionnaire," "beneficial ownership," "intermediary risk," "kickback risk," "sanctions
  screening agent," "government-official connection," "OECD third-party guidance."
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-6
context: fork
agent: general-purpose
---

# Legalcode Third-Party Anti-Corruption Due Diligence

> **Disclaimer**: This skill provides a framework for AI-assisted third-party due diligence.
> It does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional or compliance specialist licensed in the relevant jurisdiction before use.
> Laws, regulations, and enforcement guidance change; verify current applicability before
> relying on any provision described here. Statutory and regulatory references cited from
> training data carry hallucination risk — verify against authoritative sources including DOJ,
> SEC, SFO, UK Ministry of Justice, OECD, and World Bank official publications before
> relying on them.

---

## Purpose and Scope

This skill conducts structured anti-corruption due diligence on third-party intermediaries —
agents, distributors, joint venture partners, consultants, representatives, resellers, and
similar counterparties through whom a company transacts with or on behalf of foreign entities.

**Covers:**
- Third-party risk tiering (HIGH / MEDIUM / LOW) with documented rationale
- Due diligence questionnaire (DDQ) design and analysis
- Sanctions and debarment screening scope (OFAC, UN, EU, UK, World Bank/MDB cross-debarment)
- Beneficial ownership and Politically Exposed Person (PEP) analysis
- Red flag identification and escalation
- Contractual anti-corruption provisions (representations, audit rights, termination)
- Ongoing monitoring framework and re-screening triggers
- Suitability determination: APPROVED / CONDITIONAL / NOT APPROVED

**Does not:**
- Replace a full ABAC program assessment (see `legalcode-anti-bribery-compliance`)
- Constitute a legal opinion on FCPA, UK Bribery Act, or local anti-corruption exposure
- Perform automated database screening (manual analysis only — screening platforms required
  for sanctions lists)
- Apply exclusively to one jurisdiction — jurisdiction-agnostic with [JURISDICTION-SPECIFIC]
  markers; the user must verify local anti-corruption law requirements

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic. Third-party due diligence obligations arise under
multiple overlapping regimes simultaneously; the organization's legal counsel must
determine which regimes apply.

**Primary regimes addressed:**

| Regime | Jurisdiction | Third-Party Liability Hook |
|--------|-------------|---------------------------|
| FCPA (Foreign Corrupt Practices Act) | US (extraterritorial) | "Knowing" use of intermediaries; agency theory |
| UK Bribery Act 2010, s. 7 | UK (extraterritorial) | Corporate offence — inadequate procedures defense |
| OECD Anti-Bribery Convention Good Practice Guidance | International | Signatory states' implementing legislation |
| French Sapin II (Law No. 2016-1691) | France + multinationals | Third-party mapping and corruption risk map |
| Brazil Clean Company Act (Lei 12.846/2013) | Brazil | Strict liability for acts of representatives |
| German Supply Chain Due Diligence Act (LkSG) | Germany | Supply chain risk management obligations |

[JURISDICTION-SPECIFIC] When the engagement involves a specific jurisdiction:
- Identify whether local anti-corruption law imposes independent obligations
- Verify whether local law requires conducting due diligence in the local language
- Check whether beneficial ownership disclosure is required under local corporate law
- Confirm whether engagement of a particular third-party type requires government approval

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
scope, risk appetite, or organizational context, the workflow pauses and asks when:

- The answer would change the risk tier or scope of due diligence required
- A red flag requires an escalation decision
- The organization's prior relationship or playbook is needed to assess adequacy
- A finding could be interpreted as either acceptable or disqualifying depending on
  organizational policy

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

### Step 1: Accept the Request

Accept the due diligence request in any of these formats:
- **Third-party profile**: Name, type, jurisdiction, proposed role, contract value
- **Completed DDQ**: Questionnaire responses from the third party
- **Existing relationship review**: "We need to re-screen [Third Party X] who has been
  active for 3 years"
- **Red flag alert**: "We received a complaint about [Third Party Y] — can you assess?"
- **Program design request**: "Help us design our TPRM workflow"

If only a name or entity type is provided, proceed to Step 2 to gather context.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask for any information not already provided:

1. **Third-party type**: What type of intermediary is this?
   - Options: Sales agent / distributor, JV partner, Consultant / advisor, Government
     relations / lobbying firm, Customs broker / freight forwarder, Subcontractor /
     supplier, Other
   - *Why this matters*: Different third-party types carry different FCPA/Bribery Act
     risk profiles. Sales agents and government-facing consultants are the highest-risk
     category; pure product suppliers are generally lower risk.

2. **Geographic scope**: In which jurisdiction(s) will the third party operate?
   - Free text. Prompt: list all countries where the third party will act on the
     organization's behalf.
   - *Why this matters*: Corruption Perceptions Index (CPI) score drives initial risk
     tier. Operating in a Tier 1 CPI jurisdiction (high corruption) automatically
     elevates risk.

3. **Government nexus**: Will the third party interact with foreign officials or
   government entities on the organization's behalf?
   - Options: Yes — routine government contact, Yes — occasional government contact,
     No — purely private-sector engagement, Unknown
   - *Why this matters*: Government-facing third parties are the primary FCPA/Bribery
     Act risk vector. Nearly 90% of FCPA enforcement actions involve intermediaries.

4. **Contract value / compensation structure**: What is the approximate value and how
   will the third party be compensated?
   - Free text. Prompt: annual contract value, commission rate, or flat fee.
   - *Why this matters*: Unusually high commissions relative to market benchmarks are
     a red flag. Commission structures must be reasonable and documented.

5. **Prior relationship**: Is this a new engagement or a renewal?
   - Options: New engagement (no prior history), Renewal of existing relationship,
     Change of ownership or control in existing relationship, Post-M&A integration
   - *Why this matters*: New engagements require full initial due diligence. Renewals
     require re-screening. M&A integration requires retroactive assessment.

6. **Existing DDQ responses**: Has the third party completed a questionnaire?
   - Options: Yes — DDQ provided, No — DDQ to be issued, Third party refuses to
     complete DDQ
   - *Why this matters*: Third-party refusal to complete a DDQ is itself a red flag.

If proceeding with incomplete context, state assumptions explicitly and flag what
information would change the analysis.

### Step 3: Assign Risk Tier

Assign an initial risk tier using the **Risk Tiering Matrix** below. Document the
rationale for every factor assessed.

#### Risk Tiering Matrix

| Risk Factor | HIGH (Score: 3) | MEDIUM (Score: 2) | LOW (Score: 1) |
|-------------|----------------|-------------------|----------------|
| **Geography** | CPI score ≤ 40 (Tier 1 high-corruption country) | CPI score 41–60 (moderate-corruption country) | CPI score > 60 (low-corruption country) |
| **Government nexus** | Routine interaction with foreign officials or government entities | Occasional government contact; regulated industry | No government interaction; purely private sector |
| **Third-party type** | Agent, distributor, government-affairs consultant, customs broker | Professional services firm, reseller, consortium member | Raw material supplier, equipment vendor, IT provider |
| **Compensation** | Commission > 15% or > market benchmark; advance payments; offshore payment routing | Commission 5–15%; partial advance; standard payment terms | Fixed fee at market rate; no commission; standard payment |
| **Ownership transparency** | Offshore / shell company structure; beneficial owner undisclosed | Partial disclosure; complex but traceable structure | Fully transparent; publicly listed or fully disclosed |
| **PEP connection** | Owner, officer, or key employee is a PEP or has direct PEP family ties | PEP-adjacent connection (close associate, former official) | No PEP connections identified |
| **Business rationale** | Vague or unconvincing rationale; services undefined; recommended by government official | Services defined but partially verified; some justification gaps | Clear, independently verified business rationale |
| **Compliance track record** | Prior enforcement action, conviction, debarment, or investigation | Adverse media; civil disputes involving ethics questions | Clean record; no adverse media or enforcement history |

**Tier calculation:**
- Sum the scores for all applicable factors
- **HIGH (Tier 1)**: Any single factor scores 3 AND total ≥ 12, OR any two factors score 3
- **MEDIUM (Tier 2)**: Total score 8–11, or any one factor scores 3
- **LOW (Tier 3)**: Total score ≤ 7, no factors score 3

**⟁ CLARIFY** — If the risk tier is borderline (total score 7–9 or 11–13):
- Present the factors and ask: "Based on this scoring, the third party falls at the
  boundary of [Tier]. Does your organization's policy require escalation to the next tier
  for any of these specific factors?"

### Step 4: Define Due Diligence Scope

Map the risk tier to the required due diligence scope:

| Due Diligence Element | Tier 1 (HIGH) | Tier 2 (MEDIUM) | Tier 3 (LOW) |
|----------------------|:---:|:---:|:---:|
| Corporate registration verification | ✅ | ✅ | ✅ |
| Sanctions / debarment screening (OFAC, UN, EU, UK, World Bank) | ✅ | ✅ | ✅ |
| Standard DDQ (ownership, compliance, government connections) | ✅ | ✅ | ✅ |
| Beneficial ownership mapping (UBO chain ≥ 25% threshold) | ✅ | ✅ | — |
| PEP screening (owners, officers, key employees) | ✅ | ✅ | — |
| Adverse media screening (structured search protocol) | ✅ | ✅ | — |
| Enhanced DDQ (financial health, litigation, extended PEP) | ✅ | — | — |
| Open-source intelligence (OSINT) review | ✅ | — | — |
| Independent reference checks (prior clients, regulators) | ✅ | — | — |
| Financial statement review | ✅ | — | — |
| On-site visit or management interview | Consider | — | — |
| Independent third-party investigation firm | Consider | — | — |

**⟁ CLARIFY** — For Tier 1 (HIGH) third parties requiring enhanced due diligence elements:
- "This third party is Tier 1 (HIGH). Enhanced due diligence is required, including
  independent reference checks and potentially an on-site visit. Does your organization
  want to proceed with an independent investigation firm, or conduct the review internally
  with documented OSINT?"

### Step 5: Issue and Analyze the DDQ

#### Standard DDQ — Core Question Areas

Design or analyze the DDQ against these required question areas. Every area must be
covered in a Tier 1 or Tier 2 DDQ.

**Module A — Corporate Identity and Structure**
- Full legal name, registered address, and company registration number
- Corporate structure chart including all subsidiaries and affiliates
- All jurisdictions in which the entity is incorporated or operates
- Is the entity a shell company? If so, identify all operating entities
- Has the entity undergone a name change or merger in the past 5 years?

**Module B — Beneficial Ownership**
- Identify all beneficial owners holding ≥ 10% (FCPA) or ≥ 25% (UK/EU standard) interest
- For each beneficial owner: full name, nationality, percentage interest, method of holding
- Describe any arrangements through which beneficial ownership is held (trusts, nominees)
- Confirm whether any beneficial owner is a government entity or state-owned enterprise
- Provide evidence of beneficial ownership (corporate registry extract, certified chart)

**Module C — Government and Official Connections**
- Do any owners, directors, officers, or key employees hold or have held government office?
- Are any owners, directors, officers, or key employees Politically Exposed Persons (PEPs)?
- Include family members and close associates of owners for PEP analysis
- Has the entity or any individual been recommended or introduced by a government official?
- Does the entity have any contracts with, or provide services to, government entities?
- Identify any ownership by or financial relationship with a state-owned enterprise

**Module D — Compliance History**
- Has the entity ever been subject to investigation for bribery, corruption, or fraud?
- Has the entity ever been convicted, or entered a plea, for any criminal offense?
- Has the entity ever been debarred, suspended, or sanctioned by any government body,
  multilateral development bank, or international organization?
- Has the entity ever settled a regulatory or civil matter involving ethics or compliance?
- Is the entity currently under investigation or aware of any pending proceeding?
- Has the entity ever been listed on OFAC, EU, UN, or UK sanctions lists?

**Module E — Anti-Corruption Compliance Program**
- Does the entity have a written anti-bribery and anti-corruption policy?
- Does the entity conduct anti-corruption training for relevant employees?
- Does the entity have a confidential reporting mechanism (hotline or equivalent)?
- Does the entity conduct due diligence on its own sub-agents and sub-distributors?
- Will the entity agree to undergo compliance audits by the contracting organization?

**Module F — Business Rationale and Services**
- Describe in detail the services the entity will provide
- What is the entity's relevant expertise, experience, and capability?
- How was this entity identified and selected?
- What languages does the entity's team speak?
- Provide references from at least two other major clients
- Describe the entity's government relations capabilities and network

**Module G — Financial Information (Tier 1/Enhanced)**
- Provide the most recent 2 years of audited or reviewed financial statements
- Identify the entity's principal bank(s) and primary bank account jurisdiction(s)
- Are there any adverse financial events (insolvency, administration, restructuring)?
- Describe the compensation structure expected under this engagement

#### Analyzing DDQ Responses

For each module, assess responses against these standards:

| Response Quality | Classification | Action Required |
|-----------------|---------------|-----------------|
| Complete, verified, consistent with independent sources | PASS | Document; proceed |
| Incomplete or vague but explainable; minor inconsistency | FLAG | Request clarification; document explanation |
| Materially incomplete; inconsistent; evasive | RED FLAG | Escalate; do not proceed without resolution |
| Refusal to answer; implausible claims; falsification suspected | DISQUALIFYING | Do not proceed; consult compliance/legal |

**⟁ CLARIFY** — When a DDQ response is a FLAG or RED FLAG requiring a judgment call:
- Present the specific response and ask: "Module [X] response is [vague/inconsistent].
  The third party explains [their explanation]. Does this explanation satisfy your
  organization's standards, or should we escalate?"

### Step 6: Screening Analysis

#### Sanctions and Debarment Screening Protocol

Confirm that the following lists have been screened. Mark each as SCREENED / PENDING /
NOT SCREENED. The organization's screening platform vendor should perform actual list checks;
this step documents scope and gaps.

| Screening List | Description | Frequency | Status |
|---------------|-------------|-----------|--------|
| **OFAC SDN List** | US Treasury Specially Designated Nationals | Continuous (automated) + manual at onboarding | __ |
| **OFAC Consolidated Sanctions** | 30+ OFAC sanctions programs | Continuous (automated) + manual at onboarding | __ |
| **UN Security Council List** | Consolidated list — all UN member state obligations | Onboarding + annual | __ |
| **EU Consolidated Sanctions List** | EU Common Foreign and Security Policy | Onboarding + annual | __ |
| **UK HM Treasury Sanctions List** | Post-Brexit independent UK list | Onboarding + annual | __ |
| **World Bank Debarred Firms** | WB Group debarred and cross-debarred entities | Onboarding + annual | __ |
| **ADB, IADB, AfDB, EBRD Cross-Debarment** | MDB Mutual Enforcement Agreement (2010) — debarments > 1 year trigger cross-debarment | Onboarding + annual | __ |
| **Home jurisdiction government exclusion list** | [JURISDICTION-SPECIFIC] | Onboarding + annual | __ |
| **PEP Database** | Commercial PEP data (FATF-defined; family + close associates) | Onboarding + annual; continuous for Tier 1 | __ |
| **Adverse Media / Negative News** | Structured media search for bribery, corruption, fraud, sanctions | Onboarding + annual; continuous for Tier 1 | __ |

**MDB Cross-Debarment Note**: Under the 2010 Agreement for Mutual Enforcement of Debarment
Decisions, a debarment of more than one year by any signatory MDB (World Bank, ADB, IADB,
AfDB, EBRD) is generally recognized by all other signatories. A party debarred by the
World Bank for more than one year is typically ineligible for contracts under all five MDB
financing programs. [VERIFY current signatories and any amendments to the Agreement]

#### Red Flag Identification

Classify each identified issue:

| Red Flag Category | Examples | Severity |
|------------------|----------|----------|
| **Government official connection** | Owner/officer is current/former government official; entity recommended by official; entity holds government contracts | HIGH |
| **PEP match** | Owner, officer, or key employee is a PEP per FATF definition; includes family and close associates | HIGH |
| **Sanctions / debarment hit** | Name or entity matches OFAC, UN, EU, UK, or MDB list | CRITICAL |
| **Ownership opacity** | Shell company in offshore jurisdiction; beneficial owner undisclosed; nominee shareholders | HIGH |
| **Compensation red flags** | Commission > 15% / above market benchmark; large advance payment; offshore payment request; cash payment request | HIGH |
| **Business rationale gap** | Services vague; entity lacks apparent expertise; recommended by government official; no verifiable track record | HIGH |
| **Prior enforcement or litigation** | Prior FCPA/Bribery Act settlement; criminal conviction; regulatory sanction | HIGH |
| **Adverse media** | Credible reports of bribery, fraud, corruption, or sanctions violations | MEDIUM–HIGH |
| **Financial instability** | Inability to demonstrate financial capacity; insolvency; unusual financial structure | MEDIUM |
| **Compliance program gaps** | No anti-corruption policy; no training; no hotline; refuses audit rights | MEDIUM |
| **Inconsistent information** | DDQ responses inconsistent with public records; name/address discrepancies | MEDIUM |

**⟁ CLARIFY** — For any CRITICAL or HIGH red flag:
- "We have identified the following red flag: [description]. This finding is [CRITICAL/HIGH]
  severity. Proceeding with this engagement without resolving this finding would create
  significant FCPA/Bribery Act exposure. Options: (A) Halt and investigate further,
  (B) Obtain written explanation from third party and escalate to senior compliance/legal,
  (C) Decline the engagement. What would you like to do?"

### Step 7: Contractual Provisions Review

Assess whether the draft or existing contract contains the required anti-corruption
provisions. Flag any gaps.

#### Required Anti-Corruption Contract Provisions

| Provision | What It Should Cover | Present | Classification |
|-----------|---------------------|---------|---------------|
| **Anti-corruption representations and warranties** | Third party warrants compliance with FCPA, UK Bribery Act, and all applicable anti-corruption laws; no payments to officials; no prior violations | __ | REQUIRED |
| **No improper payments covenant** | Affirmative covenant to make no payments, gifts, or offers of value to any government official or private party for improper purpose | __ | REQUIRED |
| **Compliance with company ABAC policy** | Third party acknowledges and agrees to comply with company's anti-corruption policy (attach as exhibit) | __ | REQUIRED |
| **Audit rights** | Company may audit third party's books and records related to the engagement, including payment records; right to engage independent auditors | __ | REQUIRED |
| **Training obligation** | Third party employees involved in the engagement must complete anti-corruption training | __ | RECOMMENDED |
| **Annual certification** | Third party provides annual written certification of ongoing compliance | __ | RECOMMENDED |
| **Disclosure of government connections** | Third party must promptly disclose any new government official relationship, PEP connection, or conflict of interest | __ | REQUIRED |
| **Sub-agent/sub-distributor restriction** | Third party may not engage sub-agents or sub-distributors to perform the contracted services without company prior written approval and equivalent due diligence | __ | REQUIRED |
| **Termination for compliance breach** | Company may terminate immediately upon reasonable belief of anti-corruption violation; no penalty for such termination | __ | REQUIRED |
| **Clawback provision** | Company may recover fees paid to third party if it is determined that fees were used for improper payments | __ | RECOMMENDED |
| **Cooperation with investigations** | Third party must cooperate with any government investigation or internal investigation touching on the engagement | __ | REQUIRED |
| **Record retention** | Third party must maintain records of all transactions related to the engagement for minimum [5/7] years | __ | REQUIRED |
| **Governing law and jurisdiction** | Agreement governed by the company's home jurisdiction law; dispute resolution mechanism specified | __ | REQUIRED |

**Industry benchmark**: Per White & Case 2023 Global Compliance Benchmarking Survey:
- 64% of companies include anti-corruption representations and warranties
- 61% include audit rights
- 66% include termination rights
- Only 14% include clawback provisions (gap vs. best practice)
- Only 39% include compliance training requirements [VERIFY current survey figures]

**⟁ CLARIFY** — For any REQUIRED provision that is absent:
- Present the specific gap and ask whether to generate model language for insertion into
  the contract.

### Step 8: Suitability Determination

Synthesize the Risk Tiering, DDQ Analysis, Screening Analysis, and Contract Review into
a suitability determination.

#### Suitability Classification

| Classification | Criteria | Effect |
|---------------|----------|--------|
| **APPROVED** | No unresolved red flags; DDQ complete and satisfactory; all REQUIRED contract provisions present; no sanctions hits; compensation within market range | Proceed with engagement; document file; set monitoring schedule |
| **CONDITIONAL APPROVAL** | Minor flags resolved with documented explanation; enhanced monitoring required; compensating controls in place; all REQUIRED contract provisions present | Proceed with engagement under enhanced monitoring; senior compliance sign-off required; re-screen at reduced interval |
| **PENDING** | Outstanding DDQ responses; screening results pending; legal review of red flag ongoing | Do not proceed until all pending items resolved |
| **NOT APPROVED** | Unresolved CRITICAL or HIGH red flag; sanctions hit; debarment; evidence of prior corrupt conduct; refusal to cooperate with due diligence | Decline engagement; document rationale; escalate if existing relationship |

#### Suitability Summary Card

Populate this card for every third-party due diligence file:

```
Third Party:        [Full legal name]
Type:               [Agent / Distributor / JV Partner / Consultant / Other]
Jurisdiction(s):    [Countries of operation]
Risk Tier:          [HIGH / MEDIUM / LOW]
Tier Basis:         [Key risk factors driving tier assignment]
DDQ Status:         [Complete / Incomplete / Missing modules]
Screening Status:   [All lists screened / Pending / Gaps]
Red Flags:          [Number and severity]
Open Items:         [List any unresolved items]
Contract Provisions: [REQUIRED provisions: present / absent / pending]
Determination:      [APPROVED / CONDITIONAL / PENDING / NOT APPROVED]
Approved By:        [Name, title, date — must be compliance or legal officer for Tier 1]
Next Review Date:   [Tier 1: 12 months / Tier 2: 24 months / Tier 3: 36 months]
```

### Step 9: Ongoing Monitoring

Establish an ongoing monitoring protocol for all approved third parties.

#### Monitoring Schedule

| Monitoring Activity | Tier 1 (HIGH) | Tier 2 (MEDIUM) | Tier 3 (LOW) |
|--------------------|:---:|:---:|:---:|
| Automated sanctions screening | Continuous | Continuous | Continuous |
| PEP database refresh | Quarterly | Semi-annual | Annual |
| Adverse media monitoring | Continuous | Quarterly | Annual |
| Full DDQ refresh | Annual | Every 2 years | Every 3 years |
| Audit rights exercise | Annual | As warranted | As warranted |
| Annual compliance certification | ✅ | ✅ | — |
| Transaction pattern monitoring | Ongoing | Ongoing | Periodic |

#### Monitoring Triggers — Immediate Re-Screening

The following events require immediate re-screening regardless of scheduled cycle:

| Trigger Event | Action |
|--------------|--------|
| Change in ownership or beneficial ownership | Full DDQ refresh + tier re-assessment |
| New senior officer or key employee | PEP screening + background review |
| Merger, acquisition, or significant restructuring | Full enhanced due diligence |
| Adverse media report involving bribery, fraud, or corruption | Immediate escalation to compliance/legal |
| Regulatory investigation or enforcement action | Immediate escalation; potential suspension |
| Debarment or sanctions listing | CRITICAL escalation; immediate suspension |
| Complaint or whistleblower allegation | Internal investigation trigger; suspension pending outcome |
| Change in operating jurisdiction | Risk tier re-assessment |
| Unusual payment requests or patterns | Financial forensics review |
| Government official requests third party involvement | Immediate escalation |

#### Transaction Monitoring Red Flags

Monitor for these patterns in ongoing transactions:

- Commission payments larger than contractually specified
- Payments routed through jurisdictions not contemplated by the agreement
- Payments to individuals rather than the contracted entity
- Advance payments larger than agreed; multiple advance payment requests
- Requests for payments to third parties introduced by a government official
- Payments timed to coincide with government decision-making events
- Split transactions below reporting thresholds
- Cash payment requests of any amount
- Payments to accounts in offshore jurisdictions not aligned with risk profile

### Step 10: Deliver Output

Assemble the complete due diligence file using the **Output Format Template** below.
Apply the **Writing Standards** before delivering.

---

## Deep Analysis Reference: FCPA and UK Bribery Act Standards

### FCPA Third-Party Risk Framework

The DOJ FCPA Resource Guide (Second Edition, 2020) and the DOJ Guidelines for Evaluation
of Corporate Compliance Programs identify these third-party risk management requirements:

**Adequate procedures elements (DOJ):**
1. Risk-based due diligence applied to all third-party relationships before engagement
2. Documented business rationale for engaging the specific third party
3. Contractual provisions covering anti-corruption representations, audit rights, and
   termination
4. Ongoing monitoring and continued oversight after engagement, including periodic
   re-screening
5. Automated screening against governmental exclusion lists running continuously
6. Due diligence refreshes periodic, calibrated to risk level

**Knowing standard under FCPA**: "Knowing" includes "conscious disregard" and "willful
blindness." A company that fails to conduct adequate due diligence despite available
information signaling risk may be held to have "known" of the corrupt conduct.

**Successor liability**: FCPA liability can transfer in M&A transactions. Acquiring
entities should conduct FCPA due diligence on target companies' third-party relationships
before closing and remediate issues discovered post-close. [VERIFY]

### UK Bribery Act Section 7 Adequate Procedures

The Ministry of Justice six principles for adequate procedures:

| Principle | Key Requirements |
|-----------|----------------|
| **1. Proportionality** | Procedures proportionate to bribery risks faced; clear, practical, accessible, and effectively enforced |
| **2. Top-level commitment** | Board/senior management demonstrably committed to bribery prevention; tone-from-the-top |
| **3. Risk assessment** | Periodic, informed, documented assessment of external and internal bribery risks |
| **4. Due diligence** | Proportionate, risk-based due diligence on persons performing services for or on behalf of the organization |
| **5. Communication and training** | Anti-corruption policies embedded through internal/external communication; training proportionate to risk |
| **6. Monitoring and review** | Ongoing monitoring and improvement of anti-corruption procedures |

**"Associated persons" under the UK Bribery Act**: Section 8 defines an "associated person"
broadly as anyone who "performs services for or on behalf of" the organization. This captures
agents, distributors, JV partners, and subsidiaries. The corporate offense under Section 7
applies whenever an associated person pays a bribe to obtain or retain business — even
without the company's knowledge. [VERIFY current case law on associated person definition]

### OECD Good Practice Guidance

The OECD Anti-Bribery Convention Good Practice Guidance requires companies to apply
risk-based due diligence to:
- Agents and other intermediaries
- Consultants and representatives
- Distributors
- Contractors and suppliers
- Consortium members and JV partners

The OECD emphasizes: "where applicable and in line with contractual arrangements, ethics
and compliance programmes should extend to business partners through a risk-based approach."

---

## Severity Classification

Classify each finding from the due diligence process:

| Classification | Definition | Required Action |
|---------------|------------|-----------------|
| **PASS** | No concerns; element satisfactorily addressed | Document and proceed |
| **FLAG** | Minor concern; explanation obtained; risk accepted with controls | Document explanation; enhanced monitoring |
| **FAIL** | Material concern not resolved; risk unacceptable without remediation | Cannot proceed; remediation required before approval |
| **CRITICAL** | Sanctions hit; active debarment; evidence of prior corrupt conduct; PEP ownership without disclosure | Immediate escalation; suspend engagement; legal review required |

For each FAIL or CRITICAL finding, apply the **Self-Interrogation** protocol below before
finalizing the determination.

---

## Prioritization Framework

Prioritize findings and remediation actions:

**Tier 1 — Deal-Blocking / Relationship-Ending**
- Sanctions match (OFAC, UN, EU, UK)
- World Bank or MDB active debarment
- Evidence of prior corrupt conduct (conviction, plea, settlement)
- Beneficial owner is an undisclosed government official
- Third party refuses to disclose beneficial ownership

**Tier 2 — Material / Requires Resolution Before Approval**
- Unverified PEP connection for key personnel
- Compensation structure that cannot be benchmarked to market
- Missing REQUIRED contract provisions (anti-corruption reps, audit rights, termination)
- Adverse media reports not yet investigated
- Government-official recommendation without documented business rationale
- Sub-agent arrangement without equivalent due diligence

**Tier 3 — Enhance Controls / Ongoing Monitoring**
- Minor DDQ gaps (non-material, explanation provided)
- Compliance program deficiencies (no hotline, no training — addressable by contract
  obligation)
- Financial statement gaps for otherwise low-risk engagement
- Borderline compensation structure within range with documented justification

---

## Citation Quality Gates

Run these 5 gates silently before delivering any finding. If any gate fails, revise
before delivering.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every legal claim cites a specific statute, regulation, guidance document, or established enforcement principle | Add citation or mark "[UNVERIFIED]" |
| **Format** | All citations follow a consistent format (statute: "15 U.S.C. § 78dd-1"; guidance: "DOJ FCPA Resource Guide, 2nd ed. (2020)") | Fix format |
| **Currency** | Statutory thresholds, enforcement guidance, and debarment lists checked for amendment; MDB cross-debarment list verified | Flag "[CHECK CURRENCY]" |
| **Domain** | Analysis stays within anti-corruption scope; does not bleed into unrelated legal regimes without flagging | Remove or flag out-of-scope content |
| **Confidence** | Uncertainty about legal standards, enforcement trends, or local law requirements explicitly stated | Add confidence qualifier |

---

## Self-Interrogation for CRITICAL and FAIL Findings

For any finding classified CRITICAL or FAIL, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**: Does this finding follow logically from the cited
legal authority or enforcement precedent? Would a US or UK enforcement authority actually
reach this conclusion? Is the FCPA "knowing" standard correctly applied? Is the UK Bribery
Act "associated person" analysis correct?

**Pass 2 — Completeness**: Have all available sources of information been considered?
Are there alternative explanations for the red flag that have not been investigated? Has
the relevant jurisdiction's local law been assessed? Are there MDB-specific rules or
exceptions that apply?

**Pass 3 — Challenge**: What is the strongest argument that this finding is not a
disqualifying issue? Under what circumstances would a reasonable compliance officer accept
this risk with enhanced controls? Is the remediation path actually proportionate to the risk?

---

## Confidence Scoring

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95–1.0 | Confirmed sanctions hit; confirmed debarment; confirmed criminal conviction | State with full confidence; immediate escalation |
| **High** | 0.80–0.94 | Strong adverse media; compelling evidence of government official connection | State with brief caveat; escalate for investigation |
| **Probable** | 0.60–0.79 | Good indication of risk; could be explained; needs further investigation | State with reasoning and request further information |
| **Possible** | 0.40–0.59 | Suggestive but inconclusive evidence | Flag for professional review with explanation of uncertainty |
| **Unlikely** | 0.0–0.39 | Weak basis; speculative | Do not assert; note as low-confidence observation |

---

## Glass Box Audit Trail

Include this template in every completed due diligence file:

```yaml
glass_box:
  skill_name: "legalcode-third-party-due-diligence"
  version: "1.0 (2026-03-21)"
  third_party:
    name: "[Full legal name]"
    type: "[Agent / Distributor / JV Partner / Consultant / Other]"
    jurisdiction: "[Countries of operation]"
  engagement_context:
    proposed_role: "[Describe role]"
    contract_value: "[Approximate value or 'Not disclosed']"
    government_nexus: "[Yes / No / Unknown]"
  risk_tier:
    assigned: "[HIGH / MEDIUM / LOW]"
    score: "[Total risk score] / [Maximum possible]"
    driving_factors: "[List the 2-3 highest-scoring factors]"
  ddq_analysis:
    modules_complete: "[List complete modules]"
    modules_incomplete: "[List incomplete modules and gaps]"
    red_flags_identified: "[Number and severity list]"
  screening_status:
    ofac: "[Screened / Pending / Not screened — result: Clean / Match]"
    un_security_council: "[Screened / Pending — result: Clean / Match]"
    eu_consolidated: "[Screened / Pending — result: Clean / Match]"
    uk_hm_treasury: "[Screened / Pending — result: Clean / Match]"
    world_bank_mdb: "[Screened / Pending — result: Clean / Match]"
    pep_screening: "[Screened / Pending — result: Clean / Match]"
    adverse_media: "[Screened / Pending — result: Clean / Findings]"
  contract_provisions:
    required_present: "[List present provisions]"
    required_absent: "[List absent provisions — gaps]"
  suitability_determination: "[APPROVED / CONDITIONAL / PENDING / NOT APPROVED]"
  determination_rationale: "[Brief rationale]"
  approver: "[Name, title — required for Tier 1]"
  legalcode_mcp: "[Connected / Not connected]"
  citations_status: "[N verified / N unverified]"
  confidence: "[HIGH / MEDIUM / LOW — rationale]"
  limitations:
    - "[Scope limitations, information gaps, or assumptions made]"
  next_review_date: "[Date — Tier 1: +12mo / Tier 2: +24mo / Tier 3: +36mo]"
  file_retention_date: "[Engagement end date + 7 years]"
  reviewer: "AI-assisted — requires qualified compliance/legal review before reliance"
```

---

## Anti-Patterns

What NOT to do in third-party anti-corruption due diligence:

1. **Checkbox due diligence**: Running sanctions screening and calling it done. Effective
   due diligence requires all three pillars: background investigation, DDQ analysis, and
   ongoing monitoring. Sanctions screening is the floor, not the ceiling.

2. **Onboarding-only mindset**: Treating due diligence as a one-time event at engagement
   start. DOJ guidance explicitly requires ongoing monitoring and periodic re-screening.
   A third party who was clean at onboarding may be debarred or involved in enforcement
   action later.

3. **Ignoring sub-agents and sub-distributors**: Approving a distributor without requiring
   it to apply equivalent due diligence to its own sub-distributors. FCPA liability flows
   through the chain. Contract provisions must restrict sub-agent use and require equivalent
   screening downstream.

4. **Undocumented business rationale**: Approving a high-risk third party with a compelling
   explanation but failing to document that explanation in the file. The business rationale
   must be in writing in the file — "we knew why at the time" is not a defense.

5. **Market-benchmark avoidance**: Accepting an unusually high commission structure without
   benchmarking it against comparable engagements in the market. DOJ enforcement actions
   repeatedly cite above-market commissions as evidence of a slush fund for bribes.

6. **PEP family member blind spot**: Screening the third party's named officers against PEP
   lists but not screening family members and close associates. FATF guidance explicitly
   includes family and close associates. Beneficial ownership must extend to PEP-adjacent
   relationships.

7. **Shell company tolerance**: Accepting a beneficial ownership response that identifies
   a Cayman or BVI holding company as the owner without probing further. Offshore beneficial
   ownership opacity is itself a red flag requiring escalation, not acceptance.

8. **Government-official recommendation acceptance**: Approving a third party primarily
   because a foreign official recommended them. A government official's recommendation is
   a red flag under FCPA guidance, not a credential. It raises the question of whether the
   engagement itself is intended as a benefit to the official.

9. **Conflict between DDQ and public records**: Accepting DDQ responses without cross-
   checking against corporate registry, litigation databases, or news sources. DDQ responses
   are self-reported — verification against independent sources is required for Tier 1 and
   Tier 2 third parties.

10. **Missing termination provisions**: Negotiating anti-corruption representations but
    omitting the right to terminate immediately for compliance breach. Without a clean
    termination right, the company is contractually obligated to continue payments even
    after discovering misconduct.

11. **Clawback omission**: Including termination rights but not clawback provisions. If
    fees paid to the third party were used to fund improper payments, the company's ability
    to recover those fees is legally and reputationally important. Industry surveys show
    this is the most commonly missing provision.

12. **Audit rights without exercise**: Negotiating audit rights but never exercising them.
    DOJ guidance evaluates whether companies actually use their controls, not just whether
    they have them on paper. For Tier 1 third parties, audit rights should be exercised on
    a documented schedule.

13. **Risk tier inflation avoidance**: Systematically assigning MEDIUM or LOW risk tiers
    to avoid the resource burden of Tier 1 due diligence. DOJ and SFO enforcement decisions
    show that prosecutors examine how the risk tier was assigned and whether the assessment
    was genuine or self-serving.

14. **Post-M&A neglect**: Acquiring a company with an existing distributor network and
    continuing to operate those relationships without assessing whether the inherited third
    parties meet the acquirer's due diligence standards. Successor liability under FCPA
    extends to pre-acquisition third-party conduct if the acquirer continues the relationship
    without assessment.

15. **Local-law compliance confusion**: Treating compliance with local anti-corruption law
    as sufficient. FCPA and UK Bribery Act operate extraterritorially. A third party
    engagement that is legal under local law may still violate FCPA or Bribery Act if US
    nexus or UK nexus exists. Both regimes apply simultaneously with local law, not instead
    of it.

16. **Alert fatigue management by lowering thresholds**: Responding to excessive sanctions
    screening alerts by reducing match thresholds rather than investigating legitimate hits.
    Systematic threshold reduction to reduce workload is a compliance control failure.

17. **Annual re-screening — calendar only**: Scheduling re-screening on a calendar basis
    without defining event-triggered re-screening. Material changes in ownership, government
    connections, or adverse media require immediate reassessment regardless of the scheduled
    cycle.

18. **Confidential file erosion**: Maintaining due diligence files inadequately — missing
    DDQ responses, undated screening results, missing approval records. DOJ guidance on
    program evaluation specifically checks whether records are maintained to document
    decisions and their rationale. Files with gaps are treated as evidence of inadequate
    procedures.

---

## Writing Standards

Apply these standards before delivering any due diligence output:

**Precision requirements:**
- Name specific statutes, regulations, and guidance documents — not just "applicable law"
- Identify specific risk factors driving tier assignment — not just "high risk"
- Describe specific red flags found — not just "concerns identified"
- Specify which contract provisions are present, absent, or deficient — not just "reviewed"

**Prohibited language patterns:**

| Prohibited | Preferred |
|-----------|-----------|
| "The third party appears to be compliant" | "The DDQ and screening review show no unresolved red flags. Classification: PASS" |
| "There are some concerns about ownership" | "Beneficial ownership is undisclosed. This is a Tier 1 RED FLAG requiring resolution before approval." |
| "Standard due diligence has been completed" | "Modules A–G complete. Sanctions screening complete against [list]. PEP screening: [result]." |
| "The commission seems high" | "Commission rate of [X]% exceeds the [Y]% market benchmark for comparable engagements in [jurisdiction]. Classification: FLAG — requires documented business justification." |
| "Ongoing monitoring should be conducted" | "Next full DDQ refresh: [date]. Automated sanctions screening: continuous. Quarterly PEP monitoring per Tier 1 protocol." |

**Uncertainty discipline:**
- Mark every legal claim not verified against authoritative sources with [VERIFY]
- Mark local-law claims with [JURISDICTION-SPECIFIC — verify with local counsel]
- Do not state a legal conclusion without citing the authority it rests on
- Do not state a conclusion with higher confidence than the underlying evidence supports

---

## External Tool Integration

### legalcode-mcp

Use **legalcode-mcp** to search for jurisdiction-specific anti-corruption statutes, case
law on FCPA "knowing" standard, UK Bribery Act "associated person" case law, and local
anti-corruption law in the relevant jurisdiction.

**With legalcode-mcp connected:**
1. Search for the applicable jurisdiction's anti-corruption statutes and any recent
   legislative amendments
2. Search for recent enforcement actions in the relevant industry or jurisdiction
3. Search for case law on PEP and beneficial ownership definitions in the relevant regime
4. Save results to `/tmp/legalcode-tpdd-research.md`
5. Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**
- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Advise the user to verify legal authority against DOJ, SFO, MoJ, OECD, and World Bank
  official publications before relying on any legal standard cited

### Companion Skills

- **`legalcode-anti-bribery-compliance`**: Use for full organizational ABAC program
  assessment; this skill handles individual third-party due diligence files
- **`legalcode-sanctions-export-control-screening`**: Use for detailed sanctions
  analysis where the third party has a potential sanctions nexus
- **`legalcode-aml-kyc-compliance`**: Use where the engagement involves financial
  services and AML/KYC obligations overlap with ABAC due diligence

---

## Localization Notes

When applying this skill to specific jurisdictions, verify these local requirements:

| Jurisdiction | Key Local Requirements | [VERIFY] Items |
|-------------|----------------------|----------------|
| **US (FCPA)** | DOJ/SEC extraterritorial reach; "issuers" and "domestic concerns" plus third parties; successor liability | Current DOJ evaluation criteria version |
| **UK (Bribery Act)** | Section 7 corporate offence; "associated person" breadth; SFO Deferred Prosecution Agreement practice | Current SFO enforcement guidance |
| **France (Sapin II)** | Mandatory third-party mapping and risk map for companies ≥ 500 employees / €100M turnover; AFA guidelines | Current AFA recommended practices |
| **Germany (LkSG)** | Third-party due diligence for human rights and environment; BAFA oversight; tiered by supply chain tier | LkSG scope (direct suppliers vs. indirect) |
| **Brazil (Clean Company Act)** | Strict liability for third-party acts; CGU compliance program assessment; leniency agreements | Current CGU guidelines |
| **High-corruption jurisdictions** | Local anti-bribery statutes; local corporate registry accessibility; local language DDQ requirements | Country-specific statutory requirements |

---

## Output Format Template

```markdown
# Third-Party Due Diligence Report

**Third Party**: [Full legal name]
**Engagement Type**: [Agent / Distributor / JV Partner / Consultant / Other]
**Jurisdiction(s) of Operation**: [List countries]
**Report Date**: [Date]
**Prepared By**: AI-assisted — requires qualified compliance/legal review
**File Retention Date**: [Engagement end + 7 years]

---

## Executive Summary

**Risk Tier**: [HIGH / MEDIUM / LOW]
**Suitability Determination**: [APPROVED / CONDITIONAL / NOT APPROVED / PENDING]
**Critical Issues**: [Number of CRITICAL findings]
**Material Issues**: [Number of FAIL findings]
**Open Items**: [Number of unresolved items]

[2–3 sentence summary of the key factors driving the determination]

---

## Risk Tier Assessment

**Assigned Tier**: [HIGH / MEDIUM / LOW]
**Risk Score**: [X] / [Maximum]

| Risk Factor | Score | Rationale |
|-------------|-------|-----------|
| Geography | [1/2/3] | [Country and CPI score] |
| Government nexus | [1/2/3] | [Description] |
| Third-party type | [1/2/3] | [Description] |
| Compensation | [1/2/3] | [Rate and benchmark] |
| Ownership transparency | [1/2/3] | [Description] |
| PEP connection | [1/2/3] | [Description] |
| Business rationale | [1/2/3] | [Description] |
| Compliance track record | [1/2/3] | [Description] |
| **TOTAL** | **[X]** | **[Tier]** |

---

## DDQ Analysis

**DDQ Status**: [Complete / Incomplete — modules missing: X, Y, Z]
**Response Quality**: [Overall assessment]

| Module | Status | Issues |
|--------|--------|--------|
| A — Corporate Identity | [PASS / FLAG / FAIL] | [Summary] |
| B — Beneficial Ownership | [PASS / FLAG / FAIL] | [Summary] |
| C — Government Connections | [PASS / FLAG / FAIL] | [Summary] |
| D — Compliance History | [PASS / FLAG / FAIL] | [Summary] |
| E — ABAC Program | [PASS / FLAG / FAIL] | [Summary] |
| F — Business Rationale | [PASS / FLAG / FAIL] | [Summary] |
| G — Financial (Tier 1) | [PASS / FLAG / FAIL / N/A] | [Summary] |

---

## Screening Results

| List Screened | Date | Result | Notes |
|--------------|------|--------|-------|
| OFAC SDN | [Date] | [Clean / Match] | [Notes] |
| OFAC Consolidated | [Date] | [Clean / Match] | [Notes] |
| UN Security Council | [Date] | [Clean / Match] | [Notes] |
| EU Consolidated | [Date] | [Clean / Match] | [Notes] |
| UK HM Treasury | [Date] | [Clean / Match] | [Notes] |
| World Bank / MDB | [Date] | [Clean / Match] | [Notes] |
| PEP Database | [Date] | [Clean / Match] | [Notes] |
| Adverse Media | [Date] | [Clean / Findings] | [Notes] |

---

## Red Flags and Findings

### CRITICAL Issues
[If none: None identified.]

### FAIL Issues (Material — Resolution Required)
[Each issue with: description / classification / action required / deadline]

### FLAG Issues (Minor — Controls Required)
[Each issue with: description / resolution / compensating control]

---

## Contract Provisions Assessment

| Provision | Status | Action |
|-----------|--------|--------|
| Anti-corruption reps and warranties | [Present / Absent / Deficient] | [Action] |
| No improper payments covenant | [Present / Absent] | [Action] |
| Company ABAC policy compliance | [Present / Absent] | [Action] |
| Audit rights | [Present / Absent / Deficient] | [Action] |
| Training obligation | [Present / Absent] | [Action] |
| Annual certification | [Present / Absent] | [Action] |
| Disclosure of government connections | [Present / Absent] | [Action] |
| Sub-agent restriction | [Present / Absent] | [Action] |
| Termination for compliance breach | [Present / Absent] | [Action] |
| Clawback | [Present / Absent] | [Note] |

---

## Suitability Determination

**Determination**: [APPROVED / CONDITIONAL / PENDING / NOT APPROVED]
**Rationale**: [1–2 sentences]
**Conditions** (if Conditional): [Specific conditions and deadlines]
**Approver**: [Name, title — required for Tier 1]

---

## Monitoring Plan

| Activity | Frequency | Responsible Party | Next Due |
|----------|-----------|------------------|----------|
| Automated sanctions screening | Continuous | [Platform] | Ongoing |
| PEP database refresh | [Quarterly / Semi-annual / Annual] | [Compliance] | [Date] |
| Adverse media monitoring | [Continuous / Quarterly / Annual] | [Compliance] | [Date] |
| Full DDQ refresh | [Annual / 2yr / 3yr] | [Compliance] | [Date] |
| Annual compliance certification | [Annual / N/A] | [Relationship owner] | [Date] |

---

## Prioritized Action Items

### Tier 1 — Immediate (Blocking)
[List items]

### Tier 2 — Material (Before Approval)
[List items]

### Tier 3 — Enhanced Controls (Ongoing)
[List items]

---

## Glass Box Audit Trail

[Insert populated YAML from Step 10 template]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis via Mode A skill creation workflow.
Deep web research pipeline using 35+ authoritative sources covering DOJ FCPA Resource Guide
(Second Edition, 2020); DOJ Guidelines for Evaluation of Corporate Compliance Programs
(2023); UK Bribery Act 2010 Sections 7–8 and Ministry of Justice Guidance on Adequate
Procedures; OECD Good Practice Guidance on Internal Controls, Ethics and Compliance (updated
2021) and 2025 Governments' Assessments report; World Bank Group Sanctions System and OSD
Information Note; 2010 Agreement for Mutual Enforcement of Debarment Decisions (World Bank,
ADB, IADB, AfDB, EBRD); OFAC, UN Security Council, and EU Consolidated Sanctions frameworks;
FATF Recommendations 12 and 22 on Politically Exposed Persons; Transparency International
Anti-Bribery Guidance Chapter 13; White & Case 2023 Global Compliance Benchmarking Survey
(third-party management module); ICC Anti-Corruption Third Party Due Diligence Guide for
SMEs; WEF Good Practice Guidelines on Third-Party Due Diligence; Ethixbase360 EDD Checklist;
and authoritative law firm practice guides (K&L Gates, White & Case, Mayer Brown, Gibson
Dunn, Global Investigations Review). Positioned as a companion to `legalcode-anti-bribery-
compliance` (program-level assessment) — this skill handles individual third-party due
diligence files and operational TPRM workflow design.

Quality score: 18/18 Legalcode quality elements present. All legal references marked [VERIFY]
where not independently verified; user must confirm currency with DOJ, SFO, MoJ, OECD, and
World Bank official publications.
