---
name: legalcode-uk-bribery-act-compliance
description: UK Bribery Act 2010 compliance assessment for England and Wales covering all four criminal
  offences (s.1 active bribery, s.2 passive bribery, s.6 bribery of foreign public officials, s.7 corporate
  failure to prevent bribery), the adequate procedures defence and its six Ministry of Justice principles
  (proportionate procedures, top-level commitment, risk assessment, due diligence, communication, monitoring
  and review), associated person analysis under s.8 (employees, agents, subsidiaries, intermediaries,
  distributors, joint venture partners), facilitation payment prohibition, hospitality and gifts framework,
  and territorial scope for UK-incorporated and UK-nexus organisations.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

UK Bribery Act 2010 compliance assessment for England and Wales covering all four criminal offences (s.1 active bribery, s.2 passive bribery, s.6 bribery of foreign public officials, s.7 corporate failure to prevent bribery), the adequate procedures defence and its six Ministry of Justice principles (proportionate procedures, top-level commitment, risk assessment, due diligence, communication, monitoring and review), associated person analysis under s.8 (employees, agents, subsidiaries, intermediaries, distributors, joint venture partners), facilitation payment prohibition, hospitality and gifts framework, and territorial scope for UK-incorporated and UK-nexus organisations. Produces COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY gap analysis with remediation roadmap, programme design guidance, third-party due diligence checklists, gifts and hospitality policy review, self-reporting and cooperation credit analysis, and Glass Box audit trail. Use when assessing an existing anti-bribery and corruption (ABC) programme, designing adequate procedures from scratch, responding to an SFO investigation or DPA negotiation, conducting third-party due diligence on agents or intermediaries, reviewing a gifts and hospitality policy, performing M&A pre-acquisition ABC due diligence, or benchmarking compliance posture ahead of a board review or external audit. Applies to any commercial organisation subject to the Bribery Act (UK-incorporated or carrying on business in the UK). Jurisdiction: England and Wales (primary); Scotland and Northern Ireland share the same Bribery Act but have separate prosecution authorities.


# UK Bribery Act 2010 Compliance Assessment

> **Disclaimer**: This skill provides an AI-assisted framework for assessing compliance with
> the Bribery Act 2010 (c.23). It does not constitute legal advice, regulatory guidance, or
> a compliance certification. The Bribery Act is applied by courts and the Serious Fraud
> Office (SFO) on a case-by-case basis; no compliance programme guarantees immunity from
> prosecution. All statutory references, enforcement guidance, and DPA terms cited here carry
> hallucination risk — verify against current legislation (legislation.gov.uk), SFO guidance
> (sfo.gov.uk), Ministry of Justice guidance (gov.uk), and Crown Prosecution Service (CPS)
> joint prosecution guidance before relying on them. This skill does not replace advice from
> a qualified solicitor or barrister experienced in UK anti-bribery law. The SFO's approach
> to prosecution and DPAs evolves; confirm current enforcement priorities before use.

---

## Purpose and Scope

This skill assesses an organisation's anti-bribery and corruption (ABC) programme against
the requirements of the Bribery Act 2010, the Ministry of Justice (MoJ) six-principle
guidance, SFO enforcement practice, and leading DPA precedents.

**Covers:**

- All four Bribery Act offences (ss.1, 2, 6, 7) — nature, elements, and corporate exposure
- Section 7 adequate procedures defence — gap analysis against all six MoJ principles
- Associated person analysis (s.8) — mapping who can trigger corporate liability
- Facilitation payment prohibition — policy review and incident response
- Hospitality and gifts — threshold review, register assessment, policy compliance
- Territorial scope — UK-nexus analysis for multinational organisations
- Third-party ABC due diligence — agent, intermediary, and JV partner risk assessment
- Programme design — policy, training, monitoring, and board-level governance
- Enforcement and DPA landscape — self-reporting and cooperation credit analysis
- M&A pre-acquisition ABC due diligence workflow
- COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY gap classification
- Prioritised remediation roadmap with IMMEDIATE / NEAR-TERM / BACKGROUND tiers
- Glass Box audit trail for board and counsel use

**Does not:**

- Certify adequate procedures — that determination rests with courts and the SFO
- Provide legal opinions on specific prosecution risk or enforcement exposure
- Constitute legal advice or replace qualified anti-bribery counsel
- Assess related but distinct regimes in full depth: Criminal Finances Act 2017
  (failure to prevent facilitation of tax evasion), Modern Slavery Act 2015, or
  Economic Crime and Corporate Transparency Act 2023 (failure to prevent fraud) —
  those overlap but differ and should be assessed separately
- Apply to Scotland (same Act, but Crown Office and Procurator Fiscal Service (COPFS)
  is the prosecution authority) or Northern Ireland (Public Prosecution Service NI)
  without noting those differences

**Related skills:**

- `legalcode-uk-criminal-finances-act-compliance` — s.45/46 failure to prevent
  facilitation of tax evasion; use when assessing CFA 2017 alongside Bribery Act
- `legalcode-anti-bribery-compliance` — jurisdiction-agnostic ABC programme builder;
  use when assessing multi-jurisdiction exposure (FCPA, ECHR, OECD Convention)
- `legalcode-sanctions-export-control-screening` — sanctions screening for third-party
  relationships identified in the Bribery Act due diligence workflow
- `legalcode-outside-counsel-guidelines` — for structuring SFO self-report and
  cooperation credit engagement with outside ABC counsel

---

## Jurisdiction and Governing Law

**Primary legislation**: Bribery Act 2010 (c.23), in force 1 July 2011.

**Key secondary and guidance materials:**

- Ministry of Justice, _Bribery Act 2010: Guidance_ (2011) — six adequate procedures
  principles; non-prescriptive and outcome-focused
- Joint Prosecution Guidance of the Director of the SFO and the Director of Public
  Prosecutions (2011) — prosecution decision criteria, public interest factors
- SFO Corporate Co-operation Guidance (2019) — factors for self-reporting and
  cooperation credit
- SFO DPA Code of Practice (2014, updated) — DPA framework, judicial approval
  requirement, conditions
- Transparency International UK, _How to Conduct an Anti-Bribery Risk Assessment_ — best
  practice reference

**Territorial scope:**

- Covers UK-incorporated companies and partnerships regardless of where bribery occurs
- Covers foreign commercial organisations "carrying on a business or part of a business
  in the United Kingdom" — s.7(5); extraterritorial application
- Individual criminal liability (ss.1, 2, 6): covers UK nationals and residents
  wherever the act occurs; covers non-UK nationals for conduct in the UK

**Prosecution authorities:**

- England and Wales: Serious Fraud Office (SFO), Crown Prosecution Service (CPS)
- Scotland: Crown Office and Procurator Fiscal Service (COPFS)
- Northern Ireland: Public Prosecution Service NI (PPS NI)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's context, the workflow pauses and asks when:

- The answer would change the scope or depth of the analysis
- Multiple valid approaches exist (full programme review vs. targeted gap analysis)
- Information about the organisation's industry, geography, or third-party relationships
  is needed to calibrate risk and classify gaps accurately
- Enforcement context (investigation, DPA negotiation, board review) changes priorities

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

Accept input in any of these formats:

- **Policy documents**: Anti-bribery policy, gifts and hospitality policy, due diligence
  procedures, training records, risk assessment reports
- **Third-party materials**: Agent agreements, due diligence questionnaires, KYC/AML records
- **Programme description**: A description of the organisation's ABC programme elements
- **Incident or investigation context**: A specific allegation, SFO inquiry, or DPA scenario
- **M&A target profile**: A description of a target company for pre-acquisition ABC due
  diligence

If no materials are provided, proceed to gather context (Step 2) and then conduct a
framework-driven assessment against the six MoJ principles.

### Step 2: Gather Organisational Context

**⟁ CLARIFY** — Before beginning, ask the user (skip questions already answered by the input):

1. **Assessment purpose**: What is driving this review?
   - Options: Board/senior management periodic review, SFO investigation or inquiry,
     DPA negotiation, M&A pre-acquisition due diligence, Regulatory audit or third-party
     certification, Annual programme health check, Post-incident remediation, Building
     programme from scratch
   - _Why this matters_: An SFO investigation context demands different focus (self-report
     analysis, cooperation credit) than a routine board review (programme design, gap
     analysis).

2. **Organisation profile**:
   - Size: Small (<50 employees), Medium (50-500), Large (>500), FTSE-listed / multinational
   - Industry: Defence, Construction, Oil & gas, Pharmaceutical, Financial services, Mining,
     Technology, Professional services, Consumer goods, Other
   - _Why this matters_: Proportionality of adequate procedures is assessed relative to
     scale and industry; high-risk sectors face closer SFO scrutiny.

3. **Geographic footprint**:
   - Operations in high-risk jurisdictions? (Transparency International CPI <50)
   - Interactions with foreign public officials?
   - Third-party agents or intermediaries in foreign markets?
   - _Why this matters_: Triggers Section 6 (foreign official bribery) and heightened
     third-party due diligence obligations.

4. **Current programme status**:
   - Options: No programme in place, Basic policy only, Partial programme, Full programme
     claimed, Programme under review post-incident
   - _Why this matters_: Determines whether to assess for adequacy or design from scratch.

5. **Specific focus areas** (allow multiple selections):
   - Third-party / agent due diligence
   - Gifts and hospitality thresholds
   - Facilitation payment policy
   - Training and communication effectiveness
   - Board governance and top-level commitment
   - Monitoring and whistleblowing
   - M&A target diligence
   - SFO self-report / cooperation analysis

If the user provides partial context, proceed with reasonable defaults and state assumptions
explicitly.

### Step 3: Establish the Adequate Procedures Baseline

Before analysing the programme, establish the legal standard against which it will be
measured.

**The Section 7 defence** requires the organisation to prove (on the balance of
probabilities) that it had adequate procedures designed to prevent bribery by associated
persons. "Adequate" is not defined in the Act — it is judged by:

1. The Ministry of Justice six-principle framework (2011 guidance)
2. Court and prosecutorial interpretation (principally _R v Skansen Interiors Ltd_ [2018],
   which rejected the s.7 defence for the first time in a jury trial)
3. DPA precedents (Standard Bank 2015, Rolls-Royce 2017, Airbus 2020) — the SFO's
   implied standards for what it regards as adequate or inadequate
4. Proportionality — what is adequate for a FTSE 100 multinational differs from what is
   adequate for a 30-person SME

**Use legalcode-mcp** to gather current legislative text and enforcement guidance:

- Search for: "Bribery Act 2010 section 7", "adequate procedures guidance", "SFO DPA"
- Save results to `/tmp/bribery-act-research.md`
- Mark citations as VERIFIED in the Glass Box audit trail

**If legalcode-mcp is not connected:**

- Mark all statutory and case citations with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Proceed using the framework below, relying on research and general knowledge

### Step 4: Six-Principle Gap Analysis

Assess the organisation's programme against each of the six Ministry of Justice principles.
For each principle, classify the organisation's position as:

| Classification          | Meaning                                                                                                                             |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **COMPLIANT**           | Procedures meet or exceed the standard for this organisation's scale and risk profile                                               |
| **PARTIAL**             | Procedures exist but have material gaps, are incomplete, or lack genuine effectiveness                                              |
| **NON-COMPLIANT**       | Procedures are absent, wholly inadequate, or exist only on paper                                                                    |
| **CRITICAL DEFICIENCY** | Absence creates acute criminal exposure — no adequate procedures defence is available for this area; immediate remediation required |

**⟁ CLARIFY** — For any principle where the assessment is unclear without specific
programme information, ask before classifying:

- "Do you have a documented, board-approved anti-bribery policy? Has it been reviewed
  in the last 12 months?"
- "Is the board or a sub-committee (e.g., Audit Committee) formally accountable for ABC
  compliance?"
- "Has the organisation conducted a documented risk assessment identifying specific bribery
  risks by geography, sector, transaction type, and business partner?"

For each principle below, the analysis produces:

1. Classification (COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY)
2. What was found (evidence or absence of procedures)
3. Gap description (specific deficiency)
4. Remediation action (specific step to close the gap)
5. Priority (IMMEDIATE / NEAR-TERM / BACKGROUND)

---

## Six-Principle Deep Analysis

### Principle 1: Proportionate Procedures

**What the law requires**: An organisation's bribery prevention procedures must be
proportionate to the bribery risks it faces and to the nature, scale, and complexity of
its activities (MoJ Guidance, Principle 1).

**Assessment framework:**

| Sub-element                   | What to assess                                            | Red flags                                                            |
| ----------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------- |
| Policy existence              | Written anti-bribery policy adopted by board              | No policy; undated policy; unsigned policy                           |
| Proportionality to risk       | Policy addresses the organisation's specific risk profile | Generic boilerplate policy not tailored to industry/geography        |
| Code of conduct integration   | ABC requirements embedded in broader code of conduct      | Code exists but says nothing about bribery                           |
| Practical accessibility       | Policy accessible in languages spoken by staff            | Policy only in English for multi-language workforce                  |
| Review currency               | Policy reviewed within last 12-24 months                  | Policy not updated since 2011; fails to reflect current risk profile |
| Subsidiary/affiliate coverage | Policy applies to entire group                            | Policy applies only to HQ; overseas subsidiaries excluded            |

**Critical case reference**: In _R v Skansen Interiors Ltd_ [2018], a 30-employee company
was convicted under s.7 after arguing its small size meant sophisticated procedures were
unnecessary. The jury rejected this. Proportionality does not mean minimal — it means
appropriate to the scale of the risk, not the scale of the company. [VERIFY citation]

**Assessment questions to ask:**

- Is there a documented, board-approved anti-bribery policy?
- Does the policy specifically address facilitation payments, gifts and hospitality, and
  third-party risk?
- Is the policy tailored to the organisation's specific industry and geographic footprint?
- Is the policy accessible to all employees and relevant third parties?
- Has the policy been reviewed and updated within the last two years?

---

### Principle 2: Top-Level Commitment

**What the law requires**: The top-level management of a commercial organisation (be it a
board of directors, the owners, or any other equivalent body or person) are committed to
preventing bribery and foster a culture within the organisation in which bribery is never
acceptable (MoJ Guidance, Principle 2).

**Assessment framework:**

| Sub-element          | What to assess                                                        | Red flags                                                                               |
| -------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Board ownership      | Named board member or committee owns ABC compliance                   | No board-level owner; compliance delegated entirely to legal/HR without board oversight |
| Tone from top        | Board and C-suite visibly champion anti-bribery                       | CEO has never communicated on anti-bribery; no board meeting agenda items on compliance |
| Governance structure | Audit Committee, Risk Committee, or equivalent has explicit ABC remit | No formal ABC governance; ad hoc oversight only                                         |
| Resource allocation  | Adequate budget and headcount allocated to ABC programme              | ABC compliance managed part-time; no dedicated resource                                 |
| Culture indicators   | Compliance culture assessed (e.g., speak-up surveys, hotline use)     | Culture of results at any cost; compliance concerns dismissed                           |
| Anti-retaliation     | Policy and practice protecting reporters of ABC concerns              | No whistleblowing protection; known retaliation against complainants                    |

**Assessment questions to ask:**

- Which individual at board level is accountable for ABC compliance?
- When did the board last receive a formal ABC programme update?
- Does the organisation have a speak-up or whistleblower hotline?
- Has the CEO or equivalent publicly communicated the organisation's zero-tolerance stance
  on bribery (in all-hands communications, annual reports, supplier communications)?
- Has anyone been disciplined or terminated for ABC violations? If so, was this communicated
  to reinforce the culture?

---

### Principle 3: Risk Assessment

**What the law requires**: The organisation assesses the nature and extent of its exposure
to potential external and internal risks of bribery on its behalf by persons associated
with it. The assessment is periodic, informed, and documented (MoJ Guidance, Principle 3).

**The risk assessment must cover four risk categories:**

#### Country Risk

- Use authoritative indices: Transparency International Corruption Perceptions Index (CPI),
  World Bank Governance Indicators, TRACE International BribeScape
- Flag jurisdictions with CPI scores below 50 as elevated risk; below 30 as high risk
- Consider regulatory environment, rule of law, judicial independence
- Map all jurisdictions where the organisation operates or transacts

#### Sector Risk

- High-risk sectors identified by SFO and MoJ include:
  - Defence and aerospace (government procurement, export licences)
  - Construction and infrastructure (planning permissions, project contracts)
  - Oil, gas, and extractives (concessions, government-owned enterprises)
  - Pharmaceutical (regulatory approvals, clinical trials, prescribing influence)
  - Financial services (regulatory dealings, government client transactions)
  - Mining and natural resources (licences, environmental approvals)
  - Telecommunications (spectrum licences, government contracts)
- Assess whether the organisation's sector is identified as elevated risk

#### Transaction Risk

- Identify transaction types carrying elevated bribery risk:
  - Public procurement and government contracts
  - Licences, permits, and regulatory approvals
  - Joint ventures with government-linked partners
  - High-value, one-off contracts in high-risk jurisdictions
  - Contracts requiring payment of substantial commissions to intermediaries
  - Contracts awarded through undisclosed third parties

#### Business Partnership Risk

- Map all third parties that perform services for or on behalf of the organisation (s.8
  associated persons):
  - Agents, sales representatives, and intermediaries
  - Distributors and resellers
  - Joint venture partners and consortium members
  - Sub-contractors and professional service firms
  - Lobbyists and government affairs advisors
- Assess each for bribery risk factors (see Due Diligence section below)

**Assessment questions to ask:**

- Has the organisation produced a written bribery risk assessment within the last three years?
- Does the risk assessment cover all four categories (country, sector, transaction, business
  partnership)?
- Is the risk assessment reviewed and updated following material changes (new markets, new
  products, M&A, new agent relationships)?
- Is the risk assessment approved at board or senior management level?
- Does the organisation maintain an inventory of its third-party relationships with
  associated person status assessed for each?

---

### Principle 4: Due Diligence

**What the law requires**: The organisation applies due diligence procedures, taking a
proportionate and risk-based approach, in respect of persons who perform or will perform
services for or on behalf of the organisation, in order to mitigate identified bribery
risks (MoJ Guidance, Principle 4).

**The Associated Person Test (s.8 Bribery Act 2010):**

A person is an "associated person" if they perform services for or on behalf of the
organisation. This is a **broad functional test** — it does not matter whether the
relationship is a formal employment contract, an agency agreement, a distribution
agreement, or something else. What matters is the nature of what is done.

| Category              | Associated person? | Notes                                                                |
| --------------------- | ------------------ | -------------------------------------------------------------------- |
| Employees             | Yes (presumed)     | Unless clearly acting outside role                                   |
| Agents and sales reps | Yes                | Highest bribery risk category                                        |
| Distributors          | Yes                | If performing services on the organisation's behalf                  |
| Subsidiaries          | Yes                | Both wholly-owned and minority-owned                                 |
| Sub-contractors       | Yes                | If performing the organisation's work                                |
| Consultants           | Yes                | Particularly government affairs, regulatory, or lobbying consultants |
| JV partners           | Yes                | If performing services for the JV on behalf of the organisation      |
| Mere goods suppliers  | Potentially no     | But assess — risk depends on nature of supply                        |
| Passive investors     | No                 | But assess if they also perform services                             |

**Third-party due diligence framework:**

| Risk tier                | Criteria                                                                                                                  | Due diligence required                                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Tier 1 — High risk**   | Agent or intermediary in high-risk jurisdiction; government-facing role; commission-based; significant transaction values | Enhanced DD: background check, PEP screening, sanctions screening, reference checks, site visit, detailed questionnaire, annual refresh |
| **Tier 2 — Medium risk** | Distributor in moderate-risk jurisdiction; limited government contact; standard commercial relationship                   | Standard DD: questionnaire, public record check, sanctions screening, biennial refresh                                                  |
| **Tier 3 — Low risk**    | Supplier in low-risk jurisdiction; no government interface; established relationship                                      | Simplified DD: contractual warranties, periodic review                                                                                  |

**What due diligence must establish:**

- [ ] Identity and ownership structure (including ultimate beneficial owner)
- [ ] Absence of known ABC violations or criminal convictions
- [ ] No current sanctions or PEP status for key individuals
- [ ] Legitimate business presence and experience proportionate to contracted role
- [ ] Reasonableness of remuneration relative to services provided
- [ ] No undisclosed conflicts of interest or government connections
- [ ] Explanation for any negative media or adverse findings
- [ ] Agreement to anti-bribery contractual warranties and audit rights

**Contractual protections required for associated persons:**

Every contract with an associated person should include:

1. Anti-bribery representation and warranty (counterparty represents it complies with
   the Bribery Act and applicable anti-corruption laws)
2. Obligation to maintain adequate ABC procedures
3. Prohibition on facilitation payments
4. Right to audit ABC compliance (on notice, or without notice if cause exists)
5. Reporting obligation for any ABC concerns or violations
6. Termination right for breach of ABC obligations
7. Cooperation with investigations
8. No sub-agent or sub-intermediary appointment without prior written consent
9. Annual ABC compliance certification

**Assessment questions to ask:**

- Does the organisation have a documented third-party due diligence process?
- Is due diligence tiered by risk level?
- Are enhanced due diligence checks conducted on agents and intermediaries in high-risk
  jurisdictions?
- Do all agent and intermediary contracts contain anti-bribery warranties and audit rights?
- Is due diligence refreshed periodically (at least biennially for high-risk third parties)?
- Is there a register or inventory of all associated persons?

---

### Principle 5: Communication and Training

**What the law requires**: The organisation seeks to ensure that its bribery prevention
policies and procedures are embedded and understood throughout the organisation through
internal and external communication, including training, that is proportionate to the
risks it faces (MoJ Guidance, Principle 5).

**Communication requirements:**

| Audience                        | Minimum requirement                                                                                                                                      |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| All employees                   | ABC policy awareness; annual acknowledgement of policy                                                                                                   |
| High-risk roles                 | Role-specific training covering practical scenarios (e.g., what to do if asked for a facilitation payment; how to respond to a lavish hospitality offer) |
| Senior management and directors | Board-level training on personal and corporate liability; legal framework briefing                                                                       |
| Third parties                   | Policy communicated to agents, intermediaries, and key suppliers; contractual obligation to train their own staff                                        |
| New joiners                     | ABC training as part of onboarding within 30 days                                                                                                        |

**Training programme requirements:**

- [ ] Training is documented and completion rates tracked
- [ ] Training is role-specific, not purely generic
- [ ] Training uses practical scenarios relevant to the organisation's industry and geography
- [ ] Training is refreshed at minimum every two years; annually for high-risk roles
- [ ] Training outcomes assessed (not just completion; comprehension checked)
- [ ] Training records retained as evidence of adequate procedures

**Communication frequency and methods:**

- Annual ABC communication from CEO or Board (e-mail, video message, all-hands)
- Inclusion of ABC content in town halls, induction, and performance management
- ABC topics covered in intranet, policy portal, and code of conduct
- Regular practical guidance: "What would you do if...?" scenario communications

**Assessment questions to ask:**

- Does the organisation have a documented ABC training programme?
- When was training last delivered? What percentage of employees completed it?
- Is training role-specific (differentiated for high-risk roles)?
- Are training records retained?
- Has the CEO or equivalent communicated ABC expectations within the last 12 months?
- Is ABC included in the onboarding programme for new employees?

---

### Principle 6: Monitoring and Review

**What the law requires**: The organisation monitors and reviews its bribery prevention
procedures and where necessary makes improvements. Mechanisms exist to report bribery
concerns (MoJ Guidance, Principle 6).

**Monitoring mechanisms required:**

| Mechanism                            | What it does                                                                      | Minimum standard                                                                               |
| ------------------------------------ | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Gifts and hospitality register**   | Records all G&H given/received above threshold; approval required above threshold | Maintained and reviewed quarterly; threshold set by risk assessment                            |
| **Whistleblowing hotline**           | Anonymous reporting channel for ABC concerns                                      | Third-party managed; available in all jurisdictions; management response SLA                   |
| **ABC policy compliance monitoring** | Audits of policy adherence across the organisation                                | Annual compliance reviews or internal audit coverage of ABC                                    |
| **Third-party monitoring**           | Ongoing review of associated persons' conduct                                     | Periodic refreshes; triggers for enhanced monitoring (large payments, new government contacts) |
| **Transaction monitoring**           | Review of commission payments, agent fees, and high-value transactions            | Data analytics on payment patterns; escalation thresholds                                      |
| **Programme review**                 | Periodic review of the entire ABC programme                                       | Annual review by Compliance and/or Internal Audit; board sign-off                              |

**Gifts and hospitality thresholds (common market benchmarks):**

| Category                         | Typical threshold (UK market)                | Required process                                        |
| -------------------------------- | -------------------------------------------- | ------------------------------------------------------- |
| Receipt (from third party)       | £50-£100 per gift/occasion                   | Register; disclosure to manager                         |
| Receipt — elevated               | Above threshold up to £250                   | Register; manager approval                              |
| Receipt — requiring refusal      | Above £250 or offered by government official | Decline or register and escalate                        |
| Provision (to third party)       | £50-£100 per gift/occasion                   | Register; pre-approval                                  |
| Provision to foreign officials   | Any value                                    | Enhanced approval; legal review                         |
| Hospitality (entertainment)      | £150-£250 per occasion                       | Register; manager approval; business purpose documented |
| Hospitality to foreign officials | Any material value                           | Legal approval required                                 |

**Note on facilitation payments:**

- Any facilitation payment demand must be refused and reported — no threshold applies
- Maintain a facilitation payment refusal register to evidence programme effectiveness
- Train employees on the specific response protocol for facilitation payment demands

**Assessment questions to ask:**

- Does the organisation maintain a gifts and hospitality register?
- Are approval thresholds set, documented, and enforced?
- Is there a third-party anonymous whistleblowing channel?
- When was the ABC programme last formally reviewed?
- Does Internal Audit cover ABC in its annual plan?
- Are there data analytics or monitoring tools applied to payment patterns?

---

## Facilitation Payments: Detailed Assessment

### The Absolute Prohibition

The Bribery Act 2010 contains **no exception** for facilitation payments. Any payment
made to a government or public official to expedite or secure the performance of a routine
governmental action (processing a visa, clearing customs, issuing a permit) is a criminal
bribe under s.1 and/or s.6. [VERIFY: Bribery Act 2010 ss.1, 6]

This distinguishes the Bribery Act from the US Foreign Corrupt Practices Act (FCPA),
which historically exempted certain facilitation payments (though US policy has moved to
discourage even FCPA-permissible facilitation payments). Under UK law, all such payments
are unlawful regardless of value, frequency, or whether the recipient was "just doing
their job."

### Assessing the Organisation's Facilitation Payment Position

**Questions to assess:**

1. Does the anti-bribery policy include an explicit, unconditional prohibition on
   facilitation payments?
2. Does the policy describe what a facilitation payment is, with examples relevant to the
   organisation's industry?
3. Is there a documented protocol for what employees should do when a facilitation payment
   is demanded?
4. Has the prohibition been communicated to employees working in high-risk jurisdictions?
5. Does the policy address "grease payments," "speed money," or other colloquial terms?
6. Does the third-party due diligence process ask specifically about facilitation payment
   practices?
7. Does the organisation have a facilitation payment refusal register?

**Required incident response protocol for facilitation payment demands:**

| Step | Action                                                                         |
| ---- | ------------------------------------------------------------------------------ |
| 1    | Do not pay — under any circumstances                                           |
| 2    | Document the demand (date, location, official, amount demanded, context)       |
| 3    | Escalate to Compliance/Legal immediately                                       |
| 4    | Assess whether reporting to the SFO, CPS, or relevant authority is appropriate |
| 5    | Reassess the third-party relationship or jurisdictional exposure               |
| 6    | Use as training example (appropriately anonymised)                             |
| 7    | Review adequacy of ABC procedures in the relevant jurisdiction                 |

**Gap classification for facilitation payment policy:**

- No explicit prohibition → **CRITICAL DEFICIENCY**
- Prohibition exists but lacks incident response protocol → **PARTIAL**
- Prohibition exists but not communicated to high-risk employees → **NON-COMPLIANT**
- Full prohibition, protocol, training, and register in place → **COMPLIANT**

---

## Hospitality and Gifts: Detailed Assessment

### The Legal Test

The Act does not prohibit corporate hospitality per se. What it prohibits is hospitality
intended to induce or reward **improper performance** of a function. The test is whether
a reasonable person in the UK would regard the recipient's conduct (or the expected
conduct) as a breach of an expectation of good faith, impartiality, or fidelity to a
position of trust (Bribery Act 2010, ss.1-3). [VERIFY]

### Assessing Hospitality and Gifts Policy

**Questions to assess:**

1. Is there a written gifts and hospitality policy with specific monetary thresholds?
2. Are thresholds appropriate for the organisation's size, industry, and geographic
   exposure?
3. Are government officials (domestic and foreign) treated separately, with enhanced
   requirements or a near-zero threshold?
4. Is there a mandatory register for gifts and hospitality given and received?
5. Are pre-approval processes in place for hospitality above threshold?
6. Is the business purpose for hospitality required to be documented?
7. Does the policy address entertainment for procurement decision-makers or government
   officials separately from general business hospitality?
8. Is there guidance on what to do when a hospitality offer is received that may cross
   the threshold (e.g., lavish event tickets, international travel)?
9. Is the gifts register reviewed by Compliance or Internal Audit?

**Factors indicating acceptable hospitality (MoJ Guidance):**

- Proportionate in value and nature to the occasion
- Transparent — would not cause embarrassment if publicly disclosed
- Complies with the recipient's own rules and professional obligations
- Genuinely business-related, not a pretext for improper influence
- Documented with stated purpose and approval trail
- Infrequent — does not create a sense of obligation

**Factors indicating potential bribery:**

- Entertainment of government officials with discretionary authority over relevant
  decisions
- Hospitality offered during active procurement or regulatory decision-making
- Lavish entertainment without legitimate business purpose
- Secret or undisclosed entertainment
- Gifts to family members of officials
- Repeated hospitality creating a pattern of obligation
- Hospitality that the recipient's own policy would prohibit

**Gap classification for gifts and hospitality:**

- No policy, no register → **CRITICAL DEFICIENCY**
- Policy exists but no register; no approval process → **NON-COMPLIANT**
- Policy and register exist; no separate government official treatment → **PARTIAL**
- Full policy, tiered thresholds, register, government official rules, review process → **COMPLIANT**

---

## M&A Pre-Acquisition ABC Due Diligence

**⟁ CLARIFY** — If the assessment is for M&A purposes, ask:

- Is this pre-bid due diligence, exclusivity/confirmatory, or post-completion?
- What is the target company's primary jurisdiction and sector?
- Does the target use agents or intermediaries in high-risk jurisdictions?
- Are there any known investigations, government inquiries, or whistleblower complaints
  involving the target?

**M&A ABC due diligence scope:**

| Area                         | What to assess                                                              |
| ---------------------------- | --------------------------------------------------------------------------- |
| Historical conduct           | Any past investigations, settlements, DPAs, or adverse findings             |
| Third-party relationships    | All agents, intermediaries, and JV partners; due diligence records          |
| Government contracts         | Whether target holds government contracts in high-risk jurisdictions        |
| Gifts and hospitality        | Historical register; patterns indicating systemic issues                    |
| Policy and procedures        | Whether adequate procedures were in place and effective                     |
| Known government connections | PEP relationships; SOE ownership; government-linked shareholders            |
| Whistleblower history        | Any past internal reports; how investigated and resolved                    |
| Financial forensics          | Payment patterns to third parties; off-book payments; commission structures |

**Post-acquisition obligations:**

- Disclosure obligations: If buyer discovers bribery post-completion, consider self-report
  to SFO (SFO Corporate Co-operation Guidance 2019 applies)
- Successor liability: UK law generally does not impose criminal successor liability for
  historic acts of a predecessor entity, but contractual and civil remedies are available
  to the buyer; voluntary disclosure remains good practice
- Remediation: Implement buyer's ABC programme in acquired entity within agreed timeline
- Integration: Ensure target employees are trained on buyer's ABC policy within 90 days

---

## Enforcement Landscape and DPA Analysis

### Deferred Prosecution Agreements (DPAs)

DPAs in England and Wales operate under the Crime and Courts Act 2013, Sch. 17. They
require judicial approval by a Crown Court judge, who must confirm the DPA is in the
interests of justice and that its terms are fair, reasonable, and proportionate. [VERIFY]

**Key DPA precedents and what they reveal about SFO standards:**

#### Standard Bank plc (2015) — First UK DPA

- **Conduct**: USD 6 million payment by Stanbic Bank Tanzania (associated person) to
  a company part-owned by a Tanzanian Revenue Authority official to secure a USD 600
  million sovereign bond mandate
- **Issue**: Grossly inadequate due diligence on the intermediary
- **DPA terms**: USD 25.2 million financial penalty, USD 7 million compensation to Tanzania,
  independent review of compliance controls
- **Lesson**: Due diligence on intermediaries is a core element of adequate procedures.
  Failure to perform meaningful due diligence on an agent with obvious government connections
  is not mitigated by having an anti-bribery policy

#### Rolls-Royce plc (2017) — Largest DPA at the Time

- **Conduct**: Corrupt intermediary payments in seven countries (Nigeria, Indonesia,
  Malaysia, Thailand, India, China, Russia) over nearly 30 years across civil aerospace,
  defence, and energy divisions
- **Penalty**: £497.25 million
- **Key fact**: Rolls-Royce had implemented a Global Intermediaries Policy by 2010, but
  inappropriate payments continued after its implementation
- **Lesson**: Having a policy on paper does not establish adequate procedures. Effectiveness
  in practice is what counts. Monitoring and enforcement of the policy are essential

#### Airbus SE (2020) — Largest Global Settlement to Date

- **Conduct**: Section 7 bribery across Sri Lanka, Malaysia, Indonesia, Taiwan, Ghana;
  UK portion €984 million out of a global USD 3.96 billion settlement (France, UK, US)
- **Key fact**: Airbus self-reported after discrepancies emerged in ECGD export credit
  disclosures in 2016
- **Lesson**: Self-reporting and cooperation with the SFO can significantly reduce penalties;
  the SFO DPA Code of Practice requires the SFO to consider cooperation as a substantial
  mitigating factor

### Self-Reporting and Cooperation Credit

**SFO Corporate Co-operation Guidance (2019):**

- The SFO will consider cooperation credit when deciding whether to pursue a DPA rather
  than prosecution
- Cooperation includes: voluntary disclosure, preserving and producing evidence,
  identifying all witnesses, not pursuing a "cut-throat" strategy
- A company that self-reports promptly, cooperates fully, and remediates its programme
  is far more likely to achieve a DPA than prosecution

**Decision to self-report — key considerations:**

| Factor                                    | Favours self-report                             | Favours non-disclosure              |
| ----------------------------------------- | ----------------------------------------------- | ----------------------------------- |
| Severity of conduct                       | Serious, systematic                             | Isolated incident, low value        |
| Duration                                  | Extended period                                 | Short-term, one-off                 |
| Internal discovery vs. external knowledge | Discovered internally before authorities        | Already known to SFO/CPS            |
| Cooperation opportunities                 | Significant evidence to provide                 | Little additional evidence to offer |
| Remediation                               | Programme significantly enhanced post-discovery | No meaningful change possible       |
| Legal privilege                           | Privilege review complete                       | Significant privilege conflicts     |

**Note**: The decision to self-report is a major strategic decision with criminal law
consequences. This skill can structure the analysis but the decision must be made with
specialist outside counsel. [VERIFY: SFO Corporate Co-operation Guidance current version]

---

## Severity Classification Reference

### COMPLIANT

The organisation's procedures in this area meet the standard for an organisation of its
size, sector, and risk profile. The adequate procedures defence is likely available for
this element. No immediate remediation required; schedule periodic review.

### PARTIAL

Procedures exist but have material gaps. The adequate procedures defence is uncertain for
this element — a court might accept the partial procedures as adequate (if supported by
strong performance in other areas) but the gap should be remediated. Near-term action
required.

### NON-COMPLIANT

Procedures are absent or wholly inadequate for this area. No adequate procedures defence
is available for this element. This creates direct criminal exposure under s.7 for
corporate bribery involving this topic area. Immediate action required.

### CRITICAL DEFICIENCY

A specific, acute gap creates immediate criminal exposure that the existing programme
cannot mitigate. Examples: no anti-bribery policy at all; an agent in a high-corruption
jurisdiction with no due diligence and no contractual protections; no facilitation payment
prohibition communicated to staff in high-risk jurisdictions. Immediate escalation to board
and outside counsel required before the next business cycle.

---

## Actionable Output per Finding

For each gap identified, generate a finding in this format:

```
**Finding**: [Short description of the gap]
**Principle**: [MoJ Principle 1-6 / Facilitation Payments / Gifts & Hospitality / Other]
**Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]
**Confidence**: [Definite / High / Probable / Possible — see Confidence Scoring section]
**Evidence basis**: [What was reviewed; what was found or absent]
**Risk**: [What bribery scenario this gap enables; what criminal exposure it creates]
**Legal basis**: [Relevant section of Bribery Act or MoJ Guidance]
**Remediation**: [Specific action to close the gap]
**Owner**: [Who is responsible — typically Compliance, Legal, CHRO, Board, specific BU]
**Priority**: [IMMEDIATE / NEAR-TERM / BACKGROUND — see Prioritisation Framework]
**Timeline**: [Suggested completion timeframe]
```

---

## Prioritisation Framework

### IMMEDIATE — Critical Path

Gaps that require escalation to the board or outside counsel and remediation before the
next operational cycle or high-risk transaction:

- No written anti-bribery policy
- No facilitation payment prohibition for staff in high-risk jurisdictions
- Agent or intermediary in high-risk jurisdiction with no due diligence and no
  contractual ABC protections
- Active investigation, known regulator inquiry, or a whistleblower report pending
- CRITICAL DEFICIENCY classifications in any principle

### NEAR-TERM — Material Improvement

Gaps that are material but do not require emergency escalation. Address within 90 days
for programme health:

- Policy exists but outdated (>2 years), not board-approved, or not tailored to risks
- Risk assessment absent or not updated within 3 years
- Training programme exists but completion rates poor or content outdated
- Due diligence tiering not formalised or tier 1 gaps not remediated
- Gifts and hospitality register not maintained or not reviewed
- Whistleblowing channel absent or untested

### BACKGROUND — Programme Enhancement

Improvements that strengthen the programme and reduce future risk, but do not create
immediate criminal exposure:

- Enhanced data analytics for payment monitoring
- Formalising refresher training cycle
- Adding ABC content to supplier onboarding
- Benchmarking hospitality thresholds against industry peers
- Improving training metrics (moving from completion rates to comprehension scores)
- Board reporting dashboard formalisation
- Annual external ABC programme review

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                          | Fail action                                              |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific provision of the Bribery Act 2010, MoJ Guidance, SFO Guidance, or established case law                     | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | Citations use consistent, recognisable format: [Statute] [section/paragraph]; [Case name] [[year]]; [Guidance title] [para]                   | Fix format                                               |
| **Currency**   | Statutory provisions checked for amendments; guidance references checked for superseding versions                                             | Flag "[CHECK CURRENCY — may have been updated]"          |
| **Domain**     | Analysis stays within UK Bribery Act framework. No FCPA, EU, or other jurisdictional standards imported unless explicitly noted as comparison | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden. Where SFO practice or prosecutorial interpretation is uncertain, say so                            | Add confidence qualifier                                 |

### Self-Interrogation for CRITICAL DEFICIENCY and NON-COMPLIANT Findings

For any finding classified at CRITICAL DEFICIENCY or NON-COMPLIANT, apply this 3-pass
self-interrogation before delivering:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the
cited section of the Bribery Act or MoJ Guidance? Would a court or the SFO actually
classify this as an inadequacy? Has the proportionality principle been applied (could a
small organisation reasonably rely on simpler procedures here)?

**Pass 2 — Completeness**: Are there other MoJ principles or elements of the adequate
procedures defence that could mitigate this gap? Are there compensating controls elsewhere
in the programme that reduce the overall risk? Has relevant DPA precedent been considered?

**Pass 3 — Challenge**: What is the strongest argument that this gap is actually PARTIAL
rather than NON-COMPLIANT or CRITICAL DEFICIENCY? Under what circumstances might the SFO
accept this as adequate? Is this classification proportionate to the organisation's size
and actual risk exposure?

If any pass reveals a weakness, revise the classification before delivery. Mark the audit
trail: `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material finding, assign a confidence level:

| Level        | Range     | Meaning                                                          | Action                                                               |
| ------------ | --------- | ---------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled Bribery Act requirement; clear MoJ Guidance provision    | State with confidence                                                |
| **High**     | 0.80-0.94 | Strong authority, minor interpretation questions                 | State with brief caveat                                              |
| **Probable** | 0.60-0.79 | Good arguments but SFO/court discretion could differ             | State with explicit reasoning and contra-indicators                  |
| **Possible** | 0.40-0.59 | Genuinely uncertain; depends on facts or SFO enforcement posture | Flag for counsel review with both sides                              |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative classification                           | Do not assert; flag "[UNCERTAIN — specialist ABC counsel to advise]" |

---

## Anti-Patterns

Explicit catalogue of what NOT to do when assessing or building UK Bribery Act compliance
programmes:

1. **Treating "no prosecution so far" as evidence of adequacy** — The SFO does not audit
   compliance programmes. Absence of prosecution is not evidence that procedures are
   adequate. The s.7 defence is only tested when a prosecution is brought.

2. **Relying on the FCPA framework as a proxy** — The UK Bribery Act is materially
   stricter. There is no facilitation payments exception. The private sector is fully
   covered. The corporate offence is strict liability. The FCPA framework is not adequate
   for Bribery Act compliance.

3. **Adopting a boilerplate anti-bribery policy without tailoring it** — The _Skansen
   Interiors_ conviction showed that generic policies are rejected. Procedures must be
   tailored to the organisation's specific risk profile. "Off-the-shelf" is not adequate.

4. **Treating small company size as a complete answer** — Proportionality does not mean
   a small company has no obligations. A 30-employee company with agents in high-risk
   jurisdictions needs proportionate but real procedures. Small size is not an excuse;
   it adjusts what is required, not whether it is required.

5. **Ignoring the "on behalf of" element of s.8** — Organisations frequently undercount
   their associated persons by limiting the analysis to formal employees and disclosed
   agents. Sub-contractors, consultants, distributors, and JV partners can all be
   associated persons. Map all of them.

6. **Conducting one-off due diligence and never refreshing it** — Third-party due diligence
   must be ongoing. An intermediary who passes due diligence in 2019 may have new government
   connections, new criminal history, or new ownership in 2024. Periodic refresh is required.

7. **Setting hospitality thresholds without a government official carve-out** — Standard
   commercial hospitality thresholds are inappropriate for government officials (domestic
   or foreign). Officials often have their own rules that may prohibit any gifts. A
   separate, near-zero threshold (or pre-approval requirement) for officials is essential.

8. **Allowing agents to appoint sub-agents without prior written consent** — Sub-agent
   chains are a classic red flag for bribery. If an agent can appoint a sub-agent and the
   sub-agent bribes, the organisation remains liable. Restrict sub-agent appointments
   contractually and conduct fresh due diligence on each sub-agent.

9. **Paying commissions or fees disproportionate to the services received** — The SFO and
   courts will look at whether agent fees are commercially justifiable relative to the
   services provided. Excessive commissions (particularly as a percentage of contract value
   in high-risk jurisdictions) are a classic red flag and indicate potential bribery.

10. **Implementing procedures post-investigation rather than pre-emptively** — The
    adequate procedures defence requires procedures to have been in place **before** the
    bribery occurred. Scrambling to create procedures after the SFO has opened an inquiry
    cannot establish the defence retroactively.

11. **Failing to act on whistleblower reports** — A pattern of receiving ABC-related
    reports and not investigating them is powerful evidence against adequate procedures.
    The SFO will obtain the organisation's whistleblowing records. Unresolved or
    suppressed reports are extremely damaging.

12. **Training everyone the same way** — Training must be role-specific. A finance
    director with signing authority over agent commissions faces different risks than a
    junior employee. Blanket e-learning with no scenario-based content will not impress
    a court or the SFO.

13. **Treating the risk assessment as a one-off exercise** — Risks change. New markets,
    new products, new regulatory environments, M&A, and high-profile incidents all change
    the risk landscape. Risk assessments must be reviewed and updated periodically and
    following material changes.

14. **Assuming a DPA is always the right outcome** — DPAs require acceptance of a
    Statement of Facts and payment of a substantial penalty. For organisations where
    the evidence is genuinely ambiguous, a DPA may not always be preferable to defending
    the charge. DPA vs. prosecution strategy requires qualified outside ABC counsel.

15. **Separating ABC from the broader compliance programme** — Bribery Act compliance
    does not exist in isolation. It overlaps with AML (suspicious transaction reports),
    Criminal Finances Act (tax evasion facilitation), sanctions (third-party screening),
    and Modern Slavery Act (supply chain due diligence). An ABC programme that does not
    connect to these related regimes will have gaps.

16. **Not preserving evidence promptly when a concern arises** — If a potential violation
    is identified, immediately implement legal hold procedures. Destruction or loss of
    evidence after the organisation becomes aware of a potential ABC issue can result in
    criminal liability for obstruction. This must happen before any further investigation
    steps.

---

## Writing Standards

Apply plain-language discipline to all output:

**For gap findings and remediation recommendations** (may be shared with board or outside
counsel):

- Plain English. No unnecessary jargon or Latin.
- Active voice: "The organisation must implement..." not "It is recommended that procedures
  be implemented..."
- Short sentences. One point per sentence.
- Specific, not vague: "Conduct enhanced due diligence on Agent X in Nigeria, including
  PEP screening, background check, and site visit" not "improve third-party due diligence"
- Name the owner: "The Chief Compliance Officer must..." not "It is required that..."

**For legal analysis sections**:

- May include technical legal analysis
- Confidence qualifiers required for any uncertain position
- All legal claims must be cited (or marked [VERIFY] if not independently verified)
- Citations: Bribery Act 2010 s.X; MoJ Guidance (2011) p.X; SFO Guidance para X

**Quality gates before delivery:**

1. Can the General Counsel understand the executive summary without reading the full report?
2. Can the board member responsible for ABC compliance understand the top 3 priority findings?
3. Is every legal claim backed by a specific citation (or flagged [VERIFY])?
4. Are all remediation steps specific, with an owner and a timeframe?
5. Could any finding description be shorter without losing meaning? If yes, shorten.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 3, search for current text of Bribery Act 2010, MoJ Guidance (2011), SFO
  DPA Code of Practice, and SFO Corporate Co-operation Guidance
- Search for recent SFO enforcement actions and DPA approvals
- Save results to `/tmp/bribery-act-research.md`
- Reference verified authority throughout the gap analysis
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail
- Check currency of all statutory references (Bribery Act 2010 as amended; confirm no
  relevant amendments since 2011)

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Include a prominent notice that legal citations require independent verification
- Focus the analysis on programme structure and gap identification rather than legal
  authority precision
- Do not create the local authority reference file

---

## Output Format Template

Structure the final deliverable as:

````markdown
## UK Bribery Act 2010 Compliance Assessment

**Organisation**: [Name or description]
**Assessment date**: [Date]
**Assessment scope**: [Full programme / Targeted gap analysis / M&A due diligence / Other]
**Assessment basis**: [Documents reviewed / Programme description provided / Framework-only assessment]
**Prepared by**: AI-assisted — requires qualified legal review before reliance

---

## Executive Summary

[2-4 sentences: overall compliance posture, most critical gaps, and priority actions.
Written for board or General Counsel level.]

**Overall programme classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]

---

## Six-Principle Gap Analysis Summary

| MoJ Principle                 | Classification   | Key Gap                        | Priority   |
| ----------------------------- | ---------------- | ------------------------------ | ---------- |
| 1. Proportionate Procedures   | [classification] | [key gap or "None identified"] | [priority] |
| 2. Top-Level Commitment       | [classification] | [key gap or "None identified"] | [priority] |
| 3. Risk Assessment            | [classification] | [key gap or "None identified"] | [priority] |
| 4. Due Diligence              | [classification] | [key gap or "None identified"] | [priority] |
| 5. Communication and Training | [classification] | [key gap or "None identified"] | [priority] |
| 6. Monitoring and Review      | [classification] | [key gap or "None identified"] | [priority] |
| Facilitation Payments         | [classification] | [key gap or "None identified"] | [priority] |
| Gifts and Hospitality         | [classification] | [key gap or "None identified"] | [priority] |

---

## Critical and Immediate Findings

[List CRITICAL DEFICIENCY and NON-COMPLIANT findings in order of severity, using the
standard Finding format. For each finding:]

**Finding**: [description]
**Principle**: [MoJ Principle / Area]
**Classification**: [CRITICAL DEFICIENCY / NON-COMPLIANT]
**Confidence**: [confidence level]
**Evidence basis**: [what was reviewed/found]
**Risk**: [what bribery exposure this creates]
**Legal basis**: [statutory/guidance reference or [VERIFY]]
**Remediation**: [specific action]
**Owner**: [responsibility]
**Priority**: IMMEDIATE
**Timeline**: [timeframe]

---

## Near-Term Findings (PARTIAL)

[List PARTIAL findings using the same format. Prioritised by severity within the tier.]

---

## Compliant Elements

[Table listing areas assessed as COMPLIANT, for completeness and board reporting purposes.]

| Area   | Evidence                      | Notes         |
| ------ | ----------------------------- | ------------- |
| [Area] | [What establishes compliance] | [Any caveats] |

---

## Remediation Roadmap

### Immediate Actions (0-30 days)

[Numbered list of specific actions]

### Near-Term Actions (31-90 days)

[Numbered list of specific actions]

### Background Programme Enhancements (90+ days)

[Numbered list of specific actions]

---

## Third-Party Risk Register (if applicable)

[Table of associated persons assessed, with due diligence tier, current DD status, and
required actions]

| Third Party | Category | Tier | DD Status | Required Action |
| ----------- | -------- | ---- | --------- | --------------- |

---

## Next Steps

1. [Specific immediate action with owner]
2. [Board communication / legal counsel engagement if CRITICAL DEFICIENCY found]
3. [Timeline for full programme review]

---

```yaml
glass_box:
  skill_name: "legalcode-uk-bribery-act-compliance"
  mode: "Created from scratch"
  topic: "UK Bribery Act 2010 compliance assessment"
  jurisdiction: "England and Wales (Bribery Act 2010 extends to UK; prosecution varies)"
  source_skills_analyzed: 0
  enhancement_type: "Create"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[/tmp/bribery-act-research.md or 'Not created']"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  statutes_consulted:
    - "Bribery Act 2010 (c.23) — [VERIFIED / UNVERIFIED]"
    - "Crime and Courts Act 2013 Sch.17 (DPA framework) — [VERIFIED / UNVERIFIED]"
    - "Proceeds of Crime Act 2002 Parts 2 and 5 — [VERIFIED / UNVERIFIED]"
  guidance_consulted:
    - "MoJ Bribery Act 2010 Guidance (2011) — [VERIFIED / UNVERIFIED]"
    - "SFO DPA Code of Practice — [VERIFIED / UNVERIFIED]"
    - "SFO Corporate Co-operation Guidance (2019) — [VERIFIED / UNVERIFIED]"
    - "CPS/SFO Joint Prosecution Guidance (2011) — [VERIFIED / UNVERIFIED]"
  dpa_precedents_considered:
    - "Standard Bank plc (2015) — [VERIFIED / UNVERIFIED]"
    - "Rolls-Royce plc (2017) — [VERIFIED / UNVERIFIED]"
    - "Airbus SE (2020) — [VERIFIED / UNVERIFIED]"
  case_law_considered:
    - "R v Skansen Interiors Ltd [2018] — [VERIFIED / UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "[PASS / REVISED / NOT APPLICABLE — no CRITICAL DEFICIENCY items]"
  confidence: "[HIGH / MEDIUM / LOW — rationale]"
  limitations:
    - "DPA and enforcement guidance reflects position as of knowledge cutoff; verify current SFO priorities"
    - "Adequate procedures defence ultimately decided by courts on specific facts; no AI assessment can guarantee adequacy"
    - "This assessment is not a substitute for a formal compliance audit by a qualified ABC professional"
    - "Scotland and Northern Ireland: same Bribery Act applies but separate prosecution authorities (COPFS; PPS NI)"
  reviewer: "AI-assisted — requires review by qualified solicitor or barrister experienced in UK anti-bribery law"
```
````

---

## Localization Notes

This skill is jurisdiction-specific to England and Wales under the Bribery Act 2010.
The Act applies UK-wide but prosecution authorities differ:

| Jurisdiction      | Prosecution authority                              | Notes                                 |
| ----------------- | -------------------------------------------------- | ------------------------------------- |
| England and Wales | SFO (complex/serious), CPS (others)                | Primary jurisdiction for this skill   |
| Scotland          | Crown Office and Procurator Fiscal Service (COPFS) | Same Bribery Act; different procedure |
| Northern Ireland  | Public Prosecution Service NI (PPS NI)             | Same Bribery Act; different procedure |

**For multinationals with US operations**: Cross-reference with the US FCPA. The Bribery
Act is generally stricter (no facilitation payment exception; private sector coverage;
strict liability for s.7). A programme that meets Bribery Act standards will generally
meet or exceed FCPA requirements for the foreign official bribery elements, but FCPA has
its own accounting and books-and-records provisions that require separate assessment.

**For organisations in EU member states**: Post-Brexit, UK law and EU anti-corruption
directives diverge. The EU has been developing a broader anti-corruption framework;
organisations with both UK and EU operations should assess both regimes.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

- Bribery Act 2010 (c.23), legislation.gov.uk
- Ministry of Justice, _Bribery Act 2010: Guidance_ (2011)
- SFO DPA Code of Practice; SFO Corporate Co-operation Guidance (2019)
- CPS/SFO Joint Prosecution Guidance (2011)
- DPA precedents: Standard Bank (2015), Rolls-Royce (2017), Airbus (2020)
- _R v Skansen Interiors Ltd_ [2018] — first jury test of s.7 adequate procedures defence
- Transparency International UK anti-bribery guidance
- Legalcode legal research (March 2026)

Jurisdiction: England and Wales (Bribery Act 2010 has UK-wide application but England
and Wales is the primary prosecution jurisdiction under SFO/CPS). Legalcode original.
