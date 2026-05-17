---
name: legalcode-nda-triage
description: >
  Screen and triage incoming NDAs — classify as GREEN (standard approval), YELLOW (counsel
  review), or RED (significant issues) with confidence-scored, auditable analysis. Use when
  a new NDA arrives from sales, business development, or a counterparty, when assessing NDA
  risk level before signature, when deciding whether an NDA needs full counsel review, or
  when routing NDAs through an in-house legal workflow. Jurisdiction-agnostic with
  localization markers for any governing law. Supports playbook-based or general-standard
  screening. Produces a structured triage report with Glass Box audit trail.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode NDA Triage

> **Disclaimer**: This skill provides a framework for AI-assisted NDA screening. It does
> not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before use. Laws change; verify current
> applicability before relying on any provision described here. Statutory and case law
> references cited from memory carry hallucination risk — verify against authoritative
> sources before relying on them.

## Purpose and Scope

This skill rapidly screens incoming non-disclosure agreements against standard criteria or
an organizational playbook, classifies them by risk level (GREEN / YELLOW / RED), generates
actionable findings with suggested fixes, and produces a confidence-scored, auditable triage
report with routing recommendations.

**Covers:**
- Mutual and unilateral NDAs (standalone agreements)
- Confidentiality sections embedded in larger commercial agreements (with caveats)
- NDAs in any jurisdiction (jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers)
- Playbook-based or general-standard screening
- Quality-verified output with Glass Box audit trail

**Does not:**
- Draft new NDAs (see the `nda-mutual` skill for drafting)
- Perform full contract review (see `legalcode-contract-review` for comprehensive review)
- Provide legal advice or replace qualified counsel
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with localization markers

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The NDA's own governing law clause determines which
legal framework applies. The triage identifies the governing law early and adapts the
analysis accordingly.

[JURISDICTION-SPECIFIC] When localizing, research and apply:
- Enforceability of injunctive relief / equitable remedy language under local law
- Treatment of residual knowledge clauses
- Confidentiality duration limits for trade secrets vs. other information
- Public policy restrictions on non-solicitation and non-compete provisions in NDAs
- Penalty clause enforceability rules (liquidated damages, kary umowne, etc.)
- Compelled disclosure procedures and notice requirements
- Evidentiary and signature formalities for enforcement
- Trade secret protection regime (statutory vs. common law vs. both)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- Multiple valid approaches exist and the user's preference matters
- Business context is needed to classify severity correctly
- Ambiguity in the NDA creates a fork that only the user can resolve

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

### Step 1: Accept the NDA

Accept the NDA in any of these formats:
- **File**: PDF, DOCX, or other document format
- **URL**: Link to the NDA in a document system
- **Pasted text**: NDA text pasted directly into the conversation

If no NDA is provided, prompt the user to supply one.

### Step 2: Gather Context

**CLARIFY** — Before beginning the triage, ask the user these questions. Present them as
structured options:

1. **Which side are you on?**
   - Options: Receiving party, Disclosing party, Both (mutual NDA), Not sure
   - *Why this matters*: Determines which protections to scrutinize — a receiving party
     needs strong carveouts and reasonable obligations; a disclosing party needs broad
     protection scope and strong remedies.

2. **Business context**: What is the purpose of this NDA?
   - Options: Exploratory / pre-sales discussions, Vendor evaluation, M&A due diligence,
     Technology evaluation / proof of concept, Employment / contractor, Other
   - *Why this matters*: An M&A NDA may legitimately include standstill provisions; a
     sales-stage NDA should not. Context determines whether unusual clauses are appropriate.

3. **Jurisdiction**: Do you know the governing law of this NDA?
   - Options: I know it (specify), Not sure — I'll let you identify it, I want analysis
     under [specific jurisdiction]
   - *Why this matters*: Determines which legal framework to apply and which
     [JURISDICTION-SPECIFIC] issues to flag.

4. **Risk tolerance**: How should borderline items be classified?
   - Options: Conservative (flag more, safer), Pragmatic (flag only material items),
     Let me decide case by case
   - *Why this matters*: A liability cap that is RED for a risk-averse enterprise may be
     YELLOW for a startup that needs the deal.

If the user provides partial context, proceed with reasonable defaults but **state
assumptions explicitly** (e.g., "I'm assuming this is a mutual exploratory NDA — let me
know if that's wrong"). Do not silently assume.

### Step 3: Load the NDA Playbook

Check for the organization's NDA screening criteria in local settings (e.g.,
`legal.local.md` or similar configuration files).

The NDA playbook should define:
- Mutual vs. unilateral requirements
- Acceptable term lengths
- Required carveouts
- Prohibited provisions
- Organization-specific requirements (e.g., standard form NDA for counterproposals)
- Routing rules (who reviews YELLOW, who reviews RED)

**If no NDA playbook is configured:**

**CLARIFY** — Inform the user that no playbook was found, and ask:

- **Option A: Set up a playbook now** — Define the organization's NDA positions for key
  criteria (acceptable terms, required carveouts, prohibited provisions). Takes a few
  minutes but makes this and all future triages more precise.
- **Option B: Proceed with general market standards** — Use the default criteria below.
  Faster, but may not reflect the organization's specific risk appetite.
- **Option C: I'll provide positions as we go** — Start the triage and I'll ask when
  your preferred position matters.

**Default Standards** (when no playbook is configured):
- Mutual obligations required unless the organization is only disclosing
- Term: 1-3 years standard; confidentiality survival: 2-5 years
- All 5 standard carveouts required (public knowledge, prior possession, independent
  development, third-party receipt, legal compulsion)
- No non-solicitation, non-compete, exclusivity, or standstill provisions
- No residuals clause (or narrowly scoped if present)
- No IP assignment or license grants
- Governing law in a reasonable commercial jurisdiction
- Return/destruction with retention exception for legal/compliance copies

Clearly label when defaults are being used: "Based on general market standards — not
organizational playbook positions."

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Read the NDA's governing law clause and identify the applicable jurisdiction.

**CLARIFY** — If any of the following are true, ask the user before proceeding:
- **No governing law clause found**: Ask which jurisdiction the user expects to apply,
  and flag the absence as a RED item.
- **Governing law is unusual or unexpected** for the business relationship (e.g., a
  US-to-US NDA governed by Cayman Islands law): Confirm the user is aware and ask whether
  to analyze under the stated law or flag as an issue.

**With legalcode-mcp connected (preferred):**
- Search for jurisdiction-relevant statutes governing: trade secret protection,
  confidentiality obligations, penalty/liquidated damages enforceability, injunctive
  relief standards, non-compete/non-solicitation enforceability in NDAs
- Save results to a local temp file (`/tmp/legalcode-nda-triage-authority.md`)
- Reference verified authority throughout the screening
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**
- Mark every statutory and case law reference with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with general commercial knowledge, but flag that legal authority has not been
  independently verified
- Focus the analysis on structural screening rather than legal certainty

### Step 5: NDA Screening

Read the **entire NDA** before flagging issues — clauses interact with each other (e.g.,
a broad definition may be partially mitigated by strong carveouts, or a residuals clause
may be offset by a trade secret exception).

Evaluate the NDA against each of the 10 screening criteria systematically:

#### Criterion 1: Agreement Structure
- [ ] **Type identified**: Mutual NDA, Unilateral (disclosing party), or Unilateral
  (receiving party)
- [ ] **Appropriate for context**: Is the NDA type appropriate for the business
  relationship? (e.g., mutual for exploratory discussions, unilateral for one-way
  disclosures)
- [ ] **Standalone agreement**: Confirm the NDA is a standalone agreement, not a
  confidentiality section embedded in a larger commercial agreement
- [ ] **Party identification**: Are parties correctly identified (full legal names,
  registration numbers where applicable, authorized signatories)?

#### Criterion 2: Definition of Confidential Information
- [ ] **Reasonable scope**: Not overbroad (avoid "all information of any kind whether or
  not marked as confidential")
- [ ] **Marking requirements**: If marking is required, is it workable? (Written marking
  within 30 days of oral disclosure is standard)
- [ ] **Exclusions present**: Standard exclusions defined (see Criterion 4)
- [ ] **No problematic inclusions**: Does not define publicly available information or
  independently developed materials as confidential
- [ ] **Alignment with purpose**: Definition is tied to the stated purpose, not unlimited

[JURISDICTION-SPECIFIC] Check whether the definition aligns with the local trade secret
protection regime (e.g., Trade Secrets Regulations 2018 in England; art. 11 UZNK in
Poland; DTSA in the US). Where local law provides a statutory definition of trade secrets,
note whether the NDA's definition is broader, narrower, or aligned.

#### Criterion 3: Obligations of Receiving Party
- [ ] **Standard of care**: Reasonable care or at least the same care as for own
  confidential information
- [ ] **Use restriction**: Limited to the stated purpose
- [ ] **Disclosure restriction**: Limited to those with need to know who are bound by
  similar obligations
- [ ] **No onerous obligations**: No impractical requirements (e.g., encrypting all
  communications, maintaining physical logs of every disclosure)
- [ ] **Incident reporting**: Reasonable breach notification obligation (if included)

#### Criterion 4: Standard Carveouts
All of the following carveouts should be present:
- [ ] **Public knowledge**: Information that is or becomes publicly available through no
  fault of the receiving party
- [ ] **Prior possession**: Information already known to the receiving party before
  disclosure
- [ ] **Independent development**: Information independently developed without use of or
  reference to confidential information
- [ ] **Third-party receipt**: Information rightfully received from a third party without
  restriction
- [ ] **Legal compulsion**: Right to disclose when required by law, regulation, or legal
  process (with notice to the disclosing party where legally permitted)

#### Criterion 5: Permitted Disclosures
- [ ] **Employees**: Can share with employees who need to know
- [ ] **Contractors/advisors**: Can share with contractors, advisors, and professional
  consultants under similar confidentiality obligations
- [ ] **Affiliates**: Can share with affiliates / group companies (if needed for the
  business purpose)
- [ ] **Legal/regulatory**: Can disclose as required by law, regulation, or regulatory
  authority
- [ ] **Professional advisors**: Can share with legal counsel, auditors, and accountants
  under professional duties of confidence

#### Criterion 6: Term and Duration
- [ ] **Agreement term**: Reasonable period for the business relationship (1-3 years is
  standard)
- [ ] **Confidentiality survival**: Obligations survive for a reasonable period after
  termination (2-5 years is standard; trade secrets may be longer)
- [ ] **Not perpetual**: Avoid indefinite or perpetual confidentiality obligations
  (exception: trade secrets, which may warrant protection for as long as they remain
  trade secrets)

[JURISDICTION-SPECIFIC] Check whether the jurisdiction imposes limits on confidentiality
duration. In some civil law jurisdictions, perpetual obligations may be unenforceable
under freedom-of-contract principles. In jurisdictions with statutory trade secret
protection, the NDA's survival clause should align with (not undermine) statutory
protection.

#### Criterion 7: Return and Destruction
- [ ] **Obligation triggered**: On termination or upon request
- [ ] **Reasonable scope**: Return or destroy confidential information and all copies
- [ ] **Retention exception**: Allows retention of copies required by law, regulation,
  or internal compliance/backup policies (including regulatory record-keeping)
- [ ] **Certification**: Certification of destruction is reasonable; sworn affidavit or
  statutory declaration is onerous

#### Criterion 8: Remedies
- [ ] **Injunctive relief**: Acknowledgment that breach may cause irreparable harm and
  equitable relief may be appropriate is standard
- [ ] **No pre-determined damages**: Avoid liquidated damages clauses in NDAs (unusual
  and potentially problematic)
- [ ] **Not one-sided**: Remedies provisions apply equally to both parties (in mutual
  NDAs)

[JURISDICTION-SPECIFIC] The standard for interim injunctions varies significantly by
jurisdiction. Common law jurisdictions use different tests (American Cyanamid in England,
irreparable harm in the US). Civil law jurisdictions have their own procedural
mechanisms. Penalty/liquidated damages enforceability also varies (penalty doctrine in
England per Cavendish Square v Makdessi; miarkowanie per art. 484 s.2 KC in Poland;
unconscionability in the US). [VERIFY] specific standards for the governing law.

#### Criterion 9: Problematic Provisions to Flag
- [ ] **No non-solicitation**: NDA should not contain employee non-solicitation
  provisions
- [ ] **No non-compete**: NDA should not contain non-compete provisions
- [ ] **No exclusivity**: NDA should not restrict either party from entering similar
  discussions with others
- [ ] **No standstill**: NDA should not contain standstill or similar restrictive
  provisions (unless M&A context — ask if unclear)
- [ ] **No residuals clause** (or narrowly scoped): If present, must be limited to
  information retained in unaided memory of individuals who had authorized access; must
  not apply to trade secrets or patentable information; must not grant an IP license
- [ ] **No IP assignment or license**: NDA should not grant any intellectual property
  rights
- [ ] **No audit rights**: Unusual in standard NDAs; flag if present

[JURISDICTION-SPECIFIC] Non-solicitation and non-compete provisions embedded in NDAs may
be unenforceable restraints of trade in many jurisdictions. In England, the restraint of
trade doctrine applies (Nordenfelt; Egon Zehnder v Tillman [2019] UKSC 32). In Poland,
non-compete clauses may require separate agreement and compensation (art. 101^1 KP). In
the US, enforceability varies by state (some states ban non-competes entirely). [VERIFY]
for the governing law.

#### Criterion 10: Governing Law and Jurisdiction
- [ ] **Reasonable jurisdiction**: A well-established commercial jurisdiction
- [ ] **Consistent**: Governing law and jurisdiction should be aligned
- [ ] **Dispute resolution**: Litigation is generally preferred for NDA disputes;
  arbitration may be appropriate for international NDAs (New York Convention enforcement)
- [ ] **Exclusive vs. non-exclusive**: Exclusive jurisdiction is generally preferred
  (prevents parallel proceedings)

### Step 6: Classify

Based on the screening results, assign a classification using the rules below:

#### GREEN -- Standard Approval

**All** of the following must be true:
- NDA is mutual (or unilateral in the appropriate direction for the relationship)
- All 5 standard carveouts are present
- Term is within standard range (1-3 years, survival 2-5 years)
- No non-solicitation, non-compete, exclusivity, or standstill provisions
- No residuals clause, or residuals clause is narrowly scoped
- Reasonable governing law jurisdiction
- Standard remedies (no liquidated damages)
- Permitted disclosures include employees, contractors, advisors, and professional
  advisors
- Return/destruction provisions include retention exception for legal/compliance
- Definition of confidential information is reasonably scoped and tied to purpose

**Confidence required**: HIGH (0.80+) — Confident this meets all standard criteria.

**Routing**: Approve via standard delegation of authority. No counsel review required.
Same-day turnaround.

#### YELLOW -- Counsel Review Needed

**One or more** of the following are present, but the NDA is not fundamentally
problematic:
- Definition of confidential information is broader than preferred but not unreasonable
- Term is longer than standard but within market range (e.g., 5 years agreement term,
  7 years survival)
- Missing one standard carveout that could be added without difficulty
- Residuals clause present but narrowly scoped to unaided memory
- Governing law in an acceptable but non-preferred jurisdiction
- Minor asymmetry in a mutual NDA (e.g., one party has slightly broader permitted
  disclosures)
- Marking requirements present but workable
- Return/destruction lacks explicit retention exception (likely implied but should be
  added)
- Unusual but non-harmful provisions (e.g., obligation to notify of potential breach)
- Non-exclusive jurisdiction clause when exclusive would be preferred
- Arbitration where litigation would be preferred (or vice versa)

**Confidence required**: PROBABLE (0.60+) — Issues identified but could be wrong about
materiality. If confidence is below 0.60, flag for counsel review regardless.

**Routing**: Flag specific issues for counsel review. Counsel can likely resolve with
minor redlines in a single review pass. Target: 1-2 business days.

#### RED -- Significant Issues

**One or more** of the following are present:
- **Unilateral when mutual is required** (or wrong direction for the relationship)
- **Missing critical carveouts** (especially independent development or legal compulsion)
- **Non-solicitation or non-compete provisions** embedded in the NDA
- **Exclusivity or standstill provisions** without appropriate business context
- **Unreasonable term** (10+ years, or perpetual without trade secret justification)
- **Overbroad definition** that could capture public information or independently
  developed materials
- **Broad residuals clause** that effectively creates a license to use confidential
  information
- **IP assignment or license grant** hidden in the NDA
- **Liquidated damages or penalty provisions**
- **Audit rights** without reasonable scope or notice requirements
- **Highly unfavorable jurisdiction** with mandatory arbitration in a problematic forum
- **The document is not actually an NDA** (contains substantive commercial terms,
  exclusivity, or other obligations beyond confidentiality)
- **Assignment clause** allowing the counterparty to assign obligations without consent
- **Clauses potentially void or unenforceable** under the governing law

**Confidence required**: HIGH (0.80+) — Confident the issue is material. If confidence
is below 0.80, classify as YELLOW and flag for counsel review rather than RED. It is
better to send a borderline item for review than to escalate unnecessarily.

**Routing**: Full legal review required. Do not sign. Requires negotiation,
counterproposal with the organization's standard form NDA, or rejection. Target: 3-5
business days.

### Step 7: Generate Common Issue Analysis

For each YELLOW or RED finding, provide actionable analysis:

#### Common NDA Issues and Standard Positions

**Issue: Overbroad Definition of Confidential Information**
- **Standard position**: Confidential information should be limited to non-public
  information disclosed in connection with the stated purpose, with clear exclusions.
- **Redline approach**: Narrow the definition to information that is marked or identified
  as confidential, or that a reasonable person would understand to be confidential given
  the nature of the information and circumstances of disclosure.
- **Priority**: Tier 2 (Should-Have)

**Issue: Missing Independent Development Carveout**
- **Standard position**: Must include a carveout for information independently developed
  without reference to or use of the disclosing party's confidential information.
- **Risk if missing**: Could create claims that internally-developed products or features
  were derived from the counterparty's confidential information.
- **Redline approach**: Add standard independent development carveout.
- **Priority**: Tier 1 (Must-Have) — Missing this carveout is RED.

**Issue: Non-Solicitation of Employees**
- **Standard position**: Non-solicitation provisions do not belong in NDAs. They are
  appropriate in employment agreements, M&A agreements, or specific commercial agreements.
- **Redline approach**: Delete the provision entirely. If the counterparty insists, limit
  to targeted solicitation (not general recruitment or responses to advertisements) and
  set a short term (6-12 months).
- **Priority**: Tier 1 (Must-Have) — This is always RED in an NDA context.
- [JURISDICTION-SPECIFIC] In many jurisdictions, a non-solicitation clause in an NDA
  context is vulnerable to challenge as an unreasonable restraint of trade. [VERIFY]

**Issue: Broad Residuals Clause**
- **Standard position**: Resist residuals clauses. If required, limit to: (a) general
  ideas, concepts, know-how, or techniques retained in the unaided memory of individuals
  who had authorized access; (b) explicitly exclude trade secrets and patentable
  information; (c) does not grant any IP license.
- **Risk if too broad**: Effectively grants a license to use the disclosing party's
  confidential information for any purpose.
- **Redline approach**: Narrow to unaided memory with trade secret and IP carveouts.
- **Priority**: Tier 1 if broad (RED), Tier 2 if narrowly scoped (YELLOW).

**Issue: Perpetual Confidentiality Obligation**
- **Standard position**: 2-5 years from disclosure or termination, whichever is later.
  Trade secrets may warrant protection for as long as they remain trade secrets.
- **Redline approach**: Replace perpetual obligation with a defined term. Offer a trade
  secret carveout for longer protection of qualifying information.
- **Priority**: Tier 2 (Should-Have) unless term is truly unreasonable (10+ years = RED).
- [JURISDICTION-SPECIFIC] In jurisdictions with statutory trade secret protection, the
  NDA's duration clause should complement (not replace) statutory protection. [VERIFY]

**Issue: Liquidated Damages / Penalty Clauses**
- **Standard position**: Liquidated damages clauses are unusual in NDAs and should be
  flagged. The difficulty of pre-estimating loss from a confidentiality breach makes
  such clauses harder to justify.
- [JURISDICTION-SPECIFIC] Enforceability varies significantly: penalty doctrine in
  England (Cavendish Square v Makdessi [2015] UKSC 67 — proportionality test); kary
  umowne in Poland (art. 483-485 KC — permitted for non-monetary obligations, subject to
  judicial reduction per art. 484 s.2 KC); unconscionability analysis in the US. [VERIFY]
- **Priority**: Tier 1 (RED) if amounts are disproportionate; Tier 2 (YELLOW) if amounts
  are reasonable and mutual.

### Step 8: Negotiation Priority Framework

Organize findings by negotiation priority:

#### Tier 1 -- Must-Haves (Deal Blockers)
Issues where the organization cannot proceed without resolution:
- Missing critical carveouts (independent development, legal compulsion)
- Non-solicitation or non-compete provisions in an NDA
- Broad residuals clause that creates an effective IP license
- IP assignment or license hidden in the NDA
- Document is not actually an NDA (embedded commercial terms)

#### Tier 2 -- Should-Haves (Strong Preferences)
Issues that materially affect risk but have negotiation room:
- Overbroad confidential information definition
- Term adjustments (longer than standard but negotiable)
- Missing retention exception in return/destruction
- Jurisdiction preference
- Marking requirement modifications
- Certification of destruction scope

#### Tier 3 -- Nice-to-Haves (Concession Candidates)
Issues that improve the position but can be conceded strategically:
- Preferred governing law (if alternative is acceptable)
- Minor asymmetries in mutual NDA
- Notification obligations (unusual but not harmful)
- Specific dispute resolution mechanism preference

**Strategy**: Lead with Tier 1 items. Trade Tier 3 concessions to secure Tier 2 wins.
Never concede on Tier 1 without escalation.

### Step 9: Quality Verification

Before delivering the triage report, run the quality checks:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every RED-classified item, run the 3-pass Self-Interrogation. Revise if any pass
   reveals a weakness.
3. Assign a Confidence Score to the overall classification and to each material finding.
4. Verify completeness: confirm all 10 screening criteria have been addressed.
5. Generate the Glass Box Audit Trail and append it to the output.
6. Run the Writing Standards quality gates.

### Step 10: Routing and Delivery

Based on the classification, recommend the appropriate next step:

| Classification | Recommended Action | Typical Timeline |
|---|---|---|
| GREEN | Approve and route for signature per delegation of authority | Same day |
| YELLOW | Send to designated reviewer with specific issues flagged | 1-2 business days |
| RED | Engage counsel for full review; prepare counterproposal or standard form | 3-5 business days |

For YELLOW and RED classifications:
- Identify the specific person or role that should review (if the organization has defined
  routing rules in the playbook)
- Include a brief summary of issues suitable for the reviewer to quickly understand the
  key points
- If the organization has a standard form NDA, recommend sending it as a counterproposal
  for RED-classified NDAs (reference the `nda-mutual` skill if drafting is needed)
- For international NDAs, note whether the jurisdiction/arbitration position is appropriate
  for enforcement across borders

---

## Severity / Status Classification

| Finding Status | Meaning | Action |
|---------------|---------|--------|
| **PASS** | Criterion met; no issues | No action needed |
| **FLAG** | Minor deviation; YELLOW | Generate redline with fallback position |
| **FAIL** | Material deviation; RED | Escalate with risk explanation and legal basis |

---

## Prioritization Framework Summary

| Priority | Category | Examples | Negotiation Posture |
|----------|----------|----------|---------------------|
| **Tier 1** | Must-Haves | Missing carveouts, non-compete, IP assignment, broad residuals | Non-negotiable; escalate if rejected |
| **Tier 2** | Should-Haves | Overbroad definition, term adjustments, retention exception | Push firmly; accept fallback |
| **Tier 3** | Nice-to-Haves | Governing law preference, minor asymmetries | Concede strategically for Tier 2 wins |

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Identify the NDA type, counterparty, business context, and governing law.
Determine whether a playbook exists. Assess whether any special considerations apply
(M&A context, regulated sector, international counterparty, high-value relationship).

**DO**: Execute the 10-criteria screening. Classify GREEN/YELLOW/RED. Generate findings
with legal basis and suggested fixes. Assign negotiation priorities.

**CHECK**: Run the Citation Quality Gates. Verify legal claims in the triage rationale.
For RED classifications, run the Self-Interrogation. Confirm all 10 criteria addressed.

**ACT**: If the NDA reveals a new pattern (e.g., a clause structure becoming common in
the market), note it for playbook update. If the organization's standard form NDA is
missing a protection that this NDA exposed, flag for standard form revision.

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every legal claim cites a specific statute, regulation, or established principle | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format** | All citations follow a consistent, recognizable format for the jurisdiction | Fix format |
| **Currency** | Every cited provision checked for amendments or repeal against authoritative sources where accessible | Flag "[CHECK CURRENCY — may have been amended]" |
| **Domain** | Analysis stays within the NDA's governing law. No assumptions from other jurisdictions leaking in | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated, not hidden. If uncertain, say so | Add confidence qualifier |

### Self-Interrogation for RED Items

For any item classified as RED, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the
cited authority? Would a court or tribunal in this jurisdiction actually reach this
conclusion on these facts? Is there a counter-argument the counterparty's counsel will
make?

**Pass 2 — Completeness**: Have all relevant statutes, regulations, and principles been
considered? Are there regulatory dimensions not yet addressed? Could the clause interact
with another clause to mitigate or worsen the risk?

**Pass 3 — Challenge**: What is the strongest argument that this clause IS acceptable?
Under what circumstances might a reasonable legal professional accept this risk? Is the
RED classification proportionate, or is this actually YELLOW with redlines? Would a
commercial practitioner at a leading firm send this back, or mark it up and proceed?

If any pass reveals a weakness, revise the analysis before delivery. Mark the audit trail
with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For the overall classification and each material finding, assign a confidence level:

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95-1.0 | Settled law, clear contractual provision, no ambiguity | State with confidence |
| **High** | 0.80-0.94 | Strong basis, minor interpretation questions | State with brief caveat |
| **Probable** | 0.60-0.79 | Good arguments but reasonable minds could differ | State with reasoning and contra-indicators |
| **Possible** | 0.40-0.59 | Genuinely uncertain, competing interpretations | Flag for counsel review with both sides |
| **Unlikely** | 0.0-0.39 | Weak basis, speculative | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every NDA triage output MUST include a Glass Box audit section at the end:

```yaml
glass_box:
  nda_counterparty: "[Counterparty name]"
  nda_type: "[Mutual / Unilateral — direction]"
  governing_law: "[Jurisdiction identified from the NDA]"
  classification: "GREEN / YELLOW / RED"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  review_basis: "[Organizational playbook / General market standards]"
  criteria_screened: 10
  criteria_summary:
    structure: "PASS / FLAG — [brief note]"
    definition_scope: "PASS / FLAG — [brief note]"
    obligations: "PASS / FLAG"
    carveouts: "PASS / FLAG — [missing: independent development]"
    permitted_disclosures: "PASS / FLAG"
    term: "PASS / FLAG — [3 years / 5 years survival]"
    return_destruction: "PASS / FLAG"
    remedies: "PASS / FLAG"
    problematic_provisions: "PASS / FLAG — [non-compete found]"
    governing_law: "PASS / FLAG"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to temp file or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified legal review"
```

---

## Anti-Patterns

What NOT to do in NDA triage:

1. **Classifying everything as YELLOW "to be safe"** — If everything needs counsel
   review, the triage process adds no value. GREEN means GREEN — approve and sign. Trust
   the framework. The purpose of triage is to route efficiently, not to defer every
   decision.

2. **Missing the embedded commercial agreement** — The most dangerous NDA is one that
   isn't really an NDA. If the document contains IP assignment, exclusivity, non-compete,
   or standstill provisions, it's a commercial agreement wearing NDA clothing. This is
   always RED. Read every clause, not just the title.

3. **Ignoring the business context** — An NDA for exploratory due diligence in an M&A
   context may legitimately include standstill provisions. The same clause in a sales-
   stage NDA is a RED flag. Context determines whether unusual clauses are appropriate.

4. **Treating all non-standard terms as problems** — A well-drafted NDA from a reputable
   counterparty may use different language from your standard form but achieve the same
   legal effect. Read for substance, not just form. A 4-year term is not automatically
   YELLOW just because your standard is 3 years.

5. **NDA triage without reading the whole document** — Scanning the first page and the
   signature block misses the problematic provisions buried in the middle. The non-
   solicitation clause is in Section 8.2, not the recitals.

6. **Citing statutes from memory without verification** — Statutes are amended, repealed,
   and renumbered. Case citations may not exist. If you cannot verify a citation against
   an authoritative source, mark it [VERIFY] or "[UNVERIFIED — counsel to confirm]."
   Never present an unverified citation as settled law.

7. **Applying jurisdiction-specific concepts universally** — "Irreparable harm" is a US
   injunction standard, not English law (American Cyanamid applies in England). Kary
   umowne are a Polish concept with no direct common law equivalent. Work-for-hire exists
   in the US but not in England or most civil law systems. Always check whether a concept
   applies under the NDA's governing law.

8. **Assuming residuals clauses are always bad** — A narrowly-scoped residuals clause
   (unaided memory, excluding trade secrets, no IP license) is increasingly market-
   standard in technology transactions. A broad residuals clause is RED. Distinguish.

9. **Flagging "irreparable harm" language as a material problem** — While different
   jurisdictions use different injunction tests, the phrase is not legally wrong in most
   contexts — it simply may not reflect how courts in the governing jurisdiction decide
   injunctions. This is at most YELLOW (suggest jurisdiction-appropriate language), not
   RED.

10. **Single-pass analysis** — A triage that reads each criterion once, in order, will
    miss interactions between clauses. A broad definition may be partially mitigated by
    strong carveouts. An uncapped remedy may be offset by a well-scoped limitation
    elsewhere. Read the whole NDA, then screen.

11. **Triage without identifying the governing law first** — A New York-law NDA requires
    completely different analysis from an English-law NDA or a Polish-law NDA. Check
    governing law in the first 30 seconds. If it's not the expected jurisdiction, flag
    immediately — the user may need foreign counsel.

12. **Over-engineering the triage output** — The purpose of NDA triage is to route, not
    to provide full legal analysis. The report should fit on one page. If the NDA is RED,
    it goes to counsel — they don't need a 10-page analysis from the triage tool. Be
    concise.

13. **Ignoring what is NOT in the NDA** — Focusing only on clauses that are present and
    ignoring absent clauses. An NDA with no independent development carveout, no legal
    compulsion carveout, or no retention exception has material gaps that must be flagged.

14. **Failing to recommend a counterproposal** — When an NDA is RED, don't just say
    "reject." Recommend the organization's standard form NDA as a counterproposal, or
    reference the `nda-mutual` skill for drafting one.

---

## Writing Standards

Apply plain-language discipline to all triage output:

**For the triage report**:
- Plain language. No jargon or filler.
- Active voice: "This NDA contains a non-compete clause (Section 8.2)" not "A non-
  compete clause was identified"
- Short sentences. One point per sentence.
- Name the section: cite the specific NDA section reference for each finding
- Specific, not vague: "Remove Section 7.3 (non-solicitation)" not "consider the
  non-solicitation provision"

**For each finding**:
- State what the NDA says (with section reference)
- State what the standard position is
- State the risk of accepting the current language
- State the suggested fix (specific language or approach)

**Quality gates before delivery**:
1. Is the classification (GREEN/YELLOW/RED) clearly stated at the top?
2. Is every FLAG/FAIL supported by a specific section reference in the NDA?
3. Can the routing recipient understand the issues without reading the full NDA?
4. Are legal claims in the rationale backed by authority (or flagged [VERIFY])?
5. Is the report concise enough to fit on one page?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.
legalcode-mcp is a law, regulatory, and case law database with powerful search across
jurisdictions.

**With legalcode-mcp connected (preferred):**
- In Step 4, search for jurisdiction-relevant statutes governing trade secrets,
  confidentiality, penalties, injunctions, and restrictive covenants
- Save the most relevant results to `/tmp/legalcode-nda-triage-authority.md`
- Reference verified authority throughout the screening
- For RED items, search for additional case law to support or challenge the classification
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**
- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Include a notice that legal citations require independent verification
- Focus the analysis on structural screening and commercial risk assessment

---

## Output Format Template

Structure the triage deliverable as:

```markdown
## NDA Triage Report

**Classification**: [GREEN / YELLOW / RED]
**Confidence**: [level with numeric range]
**Parties**: [party names]
**Type**: [Mutual / Unilateral (disclosing) / Unilateral (receiving)]
**Term**: [agreement duration] | **Survival**: [confidentiality survival period]
**Governing Law**: [jurisdiction]
**Review Basis**: [Organizational Playbook / General Market Standards]
**Date**: [date]

---

## Screening Results

| # | Criterion | Status | Notes |
|---|-----------|--------|-------|
| 1 | Agreement Structure | [PASS/FLAG/FAIL] | [details] |
| 2 | Definition Scope | [PASS/FLAG/FAIL] | [details] |
| 3 | Receiving Party Obligations | [PASS/FLAG/FAIL] | [details] |
| 4 | Standard Carveouts | [PASS/FLAG/FAIL] | [details] |
| 5 | Permitted Disclosures | [PASS/FLAG/FAIL] | [details] |
| 6 | Term and Duration | [PASS/FLAG/FAIL] | [details] |
| 7 | Return/Destruction | [PASS/FLAG/FAIL] | [details] |
| 8 | Remedies | [PASS/FLAG/FAIL] | [details] |
| 9 | Problematic Provisions | [PASS/FLAG/FAIL] | [details] |
| 10 | Governing Law/Jurisdiction | [PASS/FLAG/FAIL] | [details] |

---

## Issues Found

### [Issue 1 — YELLOW/RED] | Section [X.X] | Priority: Tier [1/2/3]
**NDA says**: "[exact quote or summary from the NDA]"
**Standard position**: [what it should say]
**Risk**: [what could go wrong if accepted]
**Legal basis**: [statute/principle — or "[VERIFY]"]
**Suggested fix**: [specific language or approach]
**Fallback**: [alternative if primary fix is rejected]
**Confidence**: [level]

[Repeat for each issue]

---

## Recommendation

[Specific next step: approve, send for review with specific notes, or reject/counter]

---

## Negotiation Priority

**Tier 1 (Must-Haves)**: [list]
**Tier 2 (Should-Haves)**: [list]
**Tier 3 (Concession Candidates)**: [list]

---

## Next Steps

1. [Action item 1]
2. [Action item 2]
3. [Action item 3]

---

## Glass Box Audit Trail

[YAML block per Glass Box section above]
```

---

## Localization Notes

This skill is jurisdiction-agnostic by design. To create a jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with jurisdiction-specific legal content
2. Replace [VERIFY] tags with verified statutory references
3. Add jurisdiction-specific screening criteria (e.g., English law penalty doctrine,
   Polish kary umowne analysis, US state-specific non-compete rules)
4. Add jurisdiction-specific anti-patterns
5. Update the frontmatter name and description to reference the specific jurisdiction
6. Add relevant case law citations

Existing jurisdiction-specific resources that can inform localization:
- **England & Wales**: `imported-uk-legal-plugins--skills-uk-legal-nda-triage/SKILL.md`
  — includes American Cyanamid test, Cavendish Square penalty doctrine, Trade Secrets
  Regulations 2018, restraint of trade analysis
- **Poland**: `imported-iura-plugins--iura-pl-skills-nda-triage/SKILL.md` — includes KC
  articles, UZNK trade secret framework, kary umowne analysis, IURA MCP integration

Localization Checklist:
- [ ] Select governing law and verify jurisdiction-specific screening adjustments
- [ ] Validate injunctive relief / equitable remedy language for the jurisdiction
- [ ] Validate confidentiality duration legality and trade secret protection regime
- [ ] Check non-compete/non-solicitation enforceability rules in NDA context
- [ ] Verify penalty/liquidated damages doctrine for the jurisdiction
- [ ] Confirm evidentiary and signature formalities
- [ ] Add local legal terminology alongside English translations (if non-English
  jurisdiction)

---

## Provenance

Created by Legalcode (2026-02-27). Original synthesis merging best elements from 8
NDA-triage skills across 4 source repositories:
- **Anthropic knowledge-work-plugins** (`nda-triage` skill and `triage-nda` command) —
  comprehensive 10-criteria checklist and structured report template
- **45black/uk-legal-plugins** (`uk-legal-nda-triage`) — quality frameworks (PDCA, Glass
  Box, Citation Quality Gates, RLM Challenge, Confidence Scoring), anti-patterns,
  writing standards, English law annotations
- **iura-ai/IURA-Plugins** (`iura-pl nda-triage` skill and command) — anti-hallucination
  warnings, Polish law context, IURA MCP integration, legal basis per finding
- **In-repo original** (`nda-mutual`) — jurisdiction-agnostic design with
  [JURISDICTION-SPECIFIC] markers, localization checklist

Enhanced with: interactive CLARIFY points (from legalcode-contract-review reference
standard), negotiation priority framework, playbook loading with defaults, and
jurisdiction-agnostic architecture with localization support.
