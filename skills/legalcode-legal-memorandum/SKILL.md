---
name: legalcode-legal-memorandum
description: >
  Draft objective IRAC/CREAC-structured legal research memoranda with balanced risk
  assessment, calibrated probability language, and Bluebook/OSCOLA/AGLC citation
  frameworks. Use when drafting internal predictive research memos, litigation risk
  assessment memos, deal advisory memos, regulatory compliance memos, or board-ready
  executive summaries. Produces Glass Box audit-trailed memoranda across US (federal
  and state), England & Wales, and Australia jurisdictions. Covers issue framing,
  rule synthesis from statutory and case authority, counterargument steelmanning,
  probability-weighted conclusions, privilege marking, and mandatory citation
  verification. Distinguishes settled law from open questions requiring judicial
  interpretation. Supports multi-issue memos with separate Questions Presented.
allowed-tools: Read, Bash(grep:*), Glob, WebSearch, WebFetch
model: claude-opus-4-6
context: fork
agent: general-purpose
---

# Legalcode Legal Memorandum

> **Disclaimer**: This skill provides a framework for AI-assisted legal memorandum
> drafting. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional licensed in the relevant jurisdiction before use or
> reliance. Statutory and case law references cited from AI memory carry a significant
> hallucination risk — every citation **must** be independently verified in Westlaw,
> LexisNexis, or official reporters before the memo is finalized. Laws change; verify
> current applicability before relying on any provision described here. Probability
> estimates in legal memos reflect analytical judgment, not actuarial certainty.

---

## Purpose and Scope

Use this skill to produce a structured, professionally formatted, internally objective
legal research memorandum that can support litigation decisions, transactional advisory,
regulatory compliance analysis, or board-level risk reporting.

**Covers:**
- Internal predictive research memos (IRAC/CREAC structure, objective tone)
- Litigation risk assessment memos (four-dimensional risk analysis, expected value)
- Deal advisory / transaction advisory memos (risk mapping, structure alternatives)
- Regulatory compliance memos (agency guidance, safe harbor analysis)
- Board-ready executive summaries (plain English, quantified risk, action items)
- Multi-issue memos with separate Questions Presented and Brief Answers
- Issue framing with the "whether-when-and" precision technique
- Rule synthesis from primary and secondary authority in hierarchical order
- Counterargument steelmanning and adverse authority treatment
- Probability-weighted conclusions with calibrated language
- Privilege and work product marking by memo type and jurisdiction
- Bluebook 21st edition Practitioner format (US), OSCOLA 4th edition (E&W),
  AGLC 4th edition (Australia)
- US/UK/AU authority hierarchy mapping
- Mandatory citation verification checklist before finalization

**Does not:**
- Draft court pleadings, briefs, or motions (see `legalcode-complaint-drafter`,
  `legalcode-brief-analyzer`)
- Perform granular damages calculation (see `legalcode-damages-calculation`)
- Execute full litigation risk matrix (see `legalcode-litigation-risk-assessment`)
- Draft settlement agreements or demand letters
  (see `legalcode-settlement-negotiation`)
- Provide legal advice or substitute for qualified licensed counsel
- Constitute a formal legal opinion letter (which requires partner sign-off and
  express reliance qualifications)
- Guarantee citation accuracy — all citations require independent verification

**Related skills:**
- `legalcode-litigation-risk-assessment` — full four-dimensional risk matrix; the
  litigation risk memo type in this skill is a lighter wrapper; use the dedicated
  skill for full quantitative analysis
- `legalcode-early-case-assessment` — deep element-level merits analysis; feeds
  research for litigation memos
- `legalcode-brief-analyzer` — deconstructs opposing briefs; can feed the
  counterargument section of a research memo
- `legalcode-privilege-review` — assessing privilege status of existing documents
- `legalcode-complaint-drafter` — drafting pleadings from the research memo's
  conclusions

---

## Jurisdiction and Governing Law

This skill operates across three primary jurisdiction tracks. Identify the controlling
jurisdiction in Step 3 before any rule synthesis begins; the analysis framework and
citation format then lock to that jurisdiction.

**[JURISDICTION-SPECIFIC]** For each jurisdiction, localize at minimum:

**United States (Federal or State):**
- Identify the controlling circuit (or state jurisdiction) — mandatory vs. persuasive
  authority varies by circuit; circuit splits require explicit treatment
- Apply textualist/purposivist interpretation canon as appropriate to the court
  (note: *Chevron* deference overruled by *Loper Bright Enterprises v. Raimondo*,
  603 U.S. ___ (2024) [VERIFY current status]; *Skidmore* deference remains
  available)
- Distinguish federal question jurisdiction from diversity jurisdiction — state
  substantive law applies under *Erie R.R. Co. v. Tompkins*, 304 U.S. 64 (1938)
  [VERIFY citation] for diversity cases
- Note any circuit-specific procedural rules affecting memo structure
  (e.g., Seventh Circuit's preference for plain-English briefs)
- Cite in Bluebook 21st edition Practitioner format

**England & Wales:**
- Apply the E&W court hierarchy: UKSC → Court of Appeal → High Court → Crown/County Courts
- Distinguish legal advice privilege (dominant purpose: giving legal advice) from
  litigation privilege (*Three Rivers District Council v Bank of England (No 6)*
  [2004] UKHL 48 [VERIFY citation])
- Apply statutory interpretation: literal, golden, mischief rules; purposive
  approach post-*Pepper v Hart* [1993] AC 593 [VERIFY citation]; *Assange v Swedish
  Prosecution Authority* purposive methodology
- EU retained law: post-*Retained EU Law (Revocation and Reform) Act 2023* (UK),
  identify whether EU-derived law applies and whether any sunset provisions
  have taken effect [VERIFY current status of each relevant retained provision]
- Note: Scottish law, Northern Irish law, and Welsh devolved law are distinct
  systems requiring separate treatment
- Cite in OSCOLA 4th edition format

**Australia:**
- Apply the federal/state hierarchy: High Court of Australia → Federal Court /
  State Supreme Courts (by jurisdiction) → intermediate courts
- Apply *Acts Interpretation Act 1901* (Cth) s 15AA purposive interpretation for
  Commonwealth statutes; equivalent state legislation for state law
- Note that Australia has no general statutory codification of common law — identify
  whether the matter is governed by federal or state law and the applicable
  jurisdiction's court hierarchy
- High Court statutory interpretation methodology: *Project Blue Sky Inc v Australian
  Broadcasting Authority* (1998) 194 CLR 355 [VERIFY] (text and purpose read
  together); *SZTAL v Minister for Immigration and Border Protection* [2017] HCA 34
  [VERIFY] (ordinary meaning of words)
- Cite in AGLC 4th edition format

**[JURISDICTION-SPECIFIC] Other jurisdictions:** For matters outside US/E&W/AU, identify
the applicable authority hierarchy, citation standard, and privilege framework before
proceeding. Flag that local counsel review is mandatory for jurisdictions not covered
by this skill's core three tracks.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming context, the workflow pauses and asks when:

- The answer would change the memo structure or tone materially
- Multiple valid approaches to an issue exist and the user's position matters
- Jurisdiction or governing law is ambiguous
- The memo type determines fundamentally different output formats

Use the **⟁ CLARIFY** pattern wherever marked below. If the user has already provided
the information, skip the question and proceed with the stated information.

---

## Workflow

### Step 1: Accept the Request

Accept the memo request in any of these formats:
- **Structured request**: Matter description, legal question(s), factual background,
  jurisdiction, memo type, and any relevant documents
- **Conversational request**: Free-form description of the legal issue and what the
  user needs to know
- **Document upload**: Legal documents, contracts, pleadings, or prior research that
  the memo should analyze
- **Prior research**: Existing research notes, case summaries, or partial analysis
  that the memo should synthesize into formal CREAC structure

If insufficient information is provided to identify the legal question and controlling
jurisdiction, prompt the user before proceeding.

---

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the memo, ask the following questions. Present as
structured options. Skip questions already answered by the user's input.

**1. Memo type — What output format is needed?**
- **Internal research memo (predictive)** — Objective CREAC analysis for a supervising
  attorney or GC. Answers "How will a court likely rule?" Tone: analytical, balanced.
  *Why this matters*: Determines tone, conclusion format, and probability language.
- **Litigation risk assessment memo** — Assesses litigation exposure for settlement
  or reserve-setting decisions. Adds expected value modeling and strategic
  recommendation. *Why this matters*: Requires probability × magnitude framing,
  not just doctrinal analysis.
- **Deal advisory memo** — Identifies legal risks and structural alternatives in a
  proposed transaction. Tone: practical, risk-ranked. *Why this matters*: Output is
  a risk ranking with recommended deal modifications, not a court prediction.
- **Regulatory compliance memo** — Analyzes whether a proposed course of conduct
  complies with regulations. Cites agency guidance and safe harbors. *Why this
  matters*: Regulatory memos use COMPLIANT/PARTIAL/NON-COMPLIANT classification
  rather than a court-outcome prediction.
- **Board executive summary** — 1–2 page plain-English risk summary for non-lawyers.
  Strips citations; quantifies risk in business terms. *Why this matters*: Completely
  different format — no footnotes, no legal jargon, action-item focus.
- **Full memo + board summary** — Produce both the detailed research memo and a
  derived 1-page board executive summary.

**2. Jurisdiction — What law controls?**
- **US Federal** — specify circuit (e.g., 9th Circuit, D.C. Circuit)
- **US State** — specify state (e.g., Delaware, California, New York)
- **England & Wales** — note any devolved law considerations
- **Australia (Federal)** — Commonwealth law matters
- **Australia (State/Territory)** — specify jurisdiction (NSW, Vic, Qld, WA, etc.)
- **Multi-jurisdictional** — identify which jurisdiction is primary controlling law
  and which are secondary; this memo applies primary jurisdiction with comparison notes

**3. Side and purpose — Who is the memo for?**
- **Plaintiff / claimant advisory** — Assesses whether to file or pursue a claim
- **Defendant advisory** — Assesses exposure and defense strategy
- **Transactional (party-neutral)** — Identifies legal risks in a proposed transaction
  without taking a side
- **Regulatory / compliance advisory** — Assesses regulatory compliance for the
  regulated entity
- **Board / senior management** — Aggregates legal risks for governance purposes
  *Why this matters*: "Side" affects framing of probability assessments and strategic
  recommendations.

**4. Scope — How many issues?**
- **Single-issue memo** — one Question Presented, focused analysis
- **Multi-issue memo** — multiple Questions Presented (specify issues or describe
  and let this skill identify discrete issues)
- **Comprehensive memo** — full treatment of all legal issues arising from the
  described matter (this skill identifies and frames all issues)

**5. Depth**
- **Standard analysis** — CREAC per issue, key authority cited, conclusion
- **Deep analysis** — Extended rule synthesis, multi-level counterargument treatment,
  sensitivity analysis on key factual assumptions, comparative jurisdiction notes
  *Why this matters*: Deep analysis is appropriate for novel questions, bet-the-company
  matters, or cases going before a court that has not directly addressed the issue.

---

### Step 3: Jurisdiction Lock and Authority Hierarchy

Before drafting any legal analysis, establish the controlling legal framework.

**3a. Identify controlling law:**
1. State the controlling jurisdiction and court system
2. Identify the governing substantive law (constitutional, statutory, common law,
   regulatory)
3. Identify the procedural forum if relevant (e.g., FRCP for federal civil procedure)
4. Confirm the citation format for the memo: Bluebook Practitioner (US), OSCOLA
   (E&W), AGLC (Australia)

**3b. Authority Hierarchy Map** — Document the applicable authority hierarchy:

| Tier | Authority Type | Examples | Effect |
|------|---------------|----------|--------|
| **Mandatory Primary** | Highest applicable court + controlling statutes | SCOTUS, Circuit CA, State Supreme Court; applicable statutes | Binding — must apply |
| **Persuasive Primary** | Other courts, other jurisdictions | Sister circuits, foreign courts, state courts on federal questions | Persuasive — cite with signal (*see, cf., accord*) |
| **Secondary** | Treatises, Restatements, Law Review, Guidance | Restatement (Third), ABA guidance, agency no-action letters | Background only — "see also" citations; not dispositive |

**3c. Privilege marking selection:**
- Internal research memo + no litigation context: `ATTORNEY-CLIENT PRIVILEGED AND CONFIDENTIAL`
- Memo prepared in anticipation of litigation: add `ATTORNEY WORK PRODUCT — Prepared in Anticipation of Litigation`
- E&W equivalent: `LEGALLY PRIVILEGED AND CONFIDENTIAL — LEGAL ADVICE PRIVILEGE`
- AU equivalent: `CLIENT LEGAL PRIVILEGE — CONFIDENTIAL LEGAL ADVICE`
- Opinion work product (mental impressions of supervising attorney): near-absolute
  protection — add `OPINION WORK PRODUCT — DO NOT DISCLOSE`

---

### Step 4: Issue Identification and Framing

**4a. Identify all discrete legal issues** arising from the matter description.
For each issue:
- Is it a question of law (pure legal interpretation), a mixed question of law and
  fact, or a primarily factual question?
- Which issues are threshold/dispositive (must be resolved first)?
- Which issues are independent vs. contingent on resolution of another issue?

Order issues logically: threshold issues first, then substantive issues, then
remedies/damages.

**4b. Frame each Question Presented (QP)** using the "whether-when-and" technique:

> *Whether [legal conclusion to be tested], when [legally relevant fact(s)], and
> [additional dispositive fact(s) or legal element that creates the tension].*

**Well-framed example** (Delaware corporate law):
> Whether a Delaware corporation's board of directors breached its fiduciary duty
> of care under the business judgment rule, when the board approved a $50M acquisition
> without obtaining a fairness opinion, and the CEO had a disclosed financial interest
> in the target company.

**Poorly-framed (too broad)**: "Whether the contract is enforceable."

**Poorly-framed (begs the question)**: "Whether the defendant wrongfully terminated
the agreement, entitling plaintiff to consequential damages."

**Rules for QP framing:**
1. Include the legal standard by name ("under the business judgment rule," "applying
   strict scrutiny," "for purposes of UCTA 1977 s 2(2)")
2. Include only legally relevant facts — facts that are elements or factors under the
   rule
3. Neutral framing — do not prejudge the outcome
4. One issue per QP; use separate QPs for multiple issues
5. US format: begin with "Whether" (no question mark required)
6. E&W format: direct question acceptable — "Is the clause a limitation or exclusion
   clause for purposes of UCTA 1977?"
7. AU format: "Whether [conclusion] within the meaning of [provision of Act or
   doctrine], where [facts]."

**4c. Write a Brief Answer for each QP** — 1–3 sentences, no new facts or citations.
The Brief Answer should tell the reader the conclusion and the single most important
reason for it.

> *Probably yes. The board's failure to obtain a fairness opinion in a self-interested
> transaction is unlikely to receive business judgment rule protection under Van
> Gorkom, and the disclosed conflict does not, on its own, satisfy the entire fairness
> standard.*

---

### Step 5: Statement of Facts

Write a focused, objective Statement of Facts. Include only facts that are legally
relevant to the Issues — do not narrate the entire matter chronology.

**Rules:**
1. Include both favorable and unfavorable facts — objectivity is mandatory in
   internal memos
2. Flag disputed facts explicitly: "The parties dispute whether notice was given on
   Day 1 (plaintiff's position) or Day 14 (defendant's position)."
3. Indicate the source of each fact: document citation, deposition reference,
   pleading paragraph (e.g., "Compl. ¶ 12," "Smith Dep. 45:3-7," "Agreement § 8(c)")
4. Include dates, dollar amounts, and timeframes — these often determine limitation
   periods, notice requirements, and remedy availability
5. Do not characterize facts as "wrongful," "fraudulent," or "unreasonable" —
   characterization belongs in the Analysis
6. Mark uncertain or unverified facts: "[Unverified — confirm with client]"

**Structural options:**
- **Narrative**: Chronological paragraph form; appropriate for complex matters
  with a story arc
- **Tabular**: Key facts table; appropriate for document-heavy or date-intensive
  analysis (e.g., limitation period analysis, notice analysis)
- **Element-mapped**: Facts organized by legal element; appropriate for
  well-defined multi-element tests

---

### Step 6: Rule Synthesis

For each issue, synthesize the applicable rule from the authority hierarchy established
in Step 3.

**⟁ CLARIFY** — If legalcode-mcp is connected, query it for the primary authority
on the legal question before drafting the Rule section. If not connected, proceed
with in-memory synthesis and mark all authority with [VERIFY CITATION].

**Rule synthesis structure (CREAC):**

**Rule Statement** — State the black-letter rule from the highest applicable authority:
> *Under Delaware law, directors owe a fiduciary duty of care requiring them to act
> on an informed basis in good faith and in the honest belief that the action taken
> is in the best interests of the company. Smith v. Van Gorkom, 488 A.2d 858, 872
> (Del. 1985) [VERIFY CITATION]. The business judgment rule presumes compliance with
> this standard unless plaintiff rebuts the presumption by showing self-dealing,
> bad faith, or waste. Aronson v. Lewis, 473 A.2d 805, 812 (Del. 1984) [VERIFY
> CITATION].*

**Synthesis for multi-element rules** — Organize by element:

| Element | Statement | Leading Authority |
|---------|-----------|-------------------|
| 1. [element name] | [rule statement] | [citation] [VERIFY] |
| 2. [element name] | [rule statement] | [citation] [VERIFY] |
| … | … | … |

**Handling circuit splits / unsettled questions:**
> *The circuits are split on whether X. The Fifth and Seventh Circuits hold [Y].
> See [cite] [VERIFY]; [cite] [VERIFY]. The Third Circuit has adopted a narrower
> rule. See [cite] [VERIFY]. This memo applies [circuit] precedent as controlling.*

**Statutory text rule — quote, do not paraphrase:**
> *Section 2(2) of the Unfair Contract Terms Act 1977 provides: "In the case of
> other loss or damage, a person cannot so exclude or restrict his liability for
> negligence except in so far as the contract term or notice satisfies the
> requirement of reasonableness." UCTA 1977, s 2(2) [VERIFY current text].*

**Recent developments note:**
For any area of law with significant developments after 2023, explicitly flag:
> *[Note: This area of law has seen significant recent development. Verify whether
> any post-[date] legislative amendments, regulations, or appellate decisions affect
> this analysis. The rule as stated reflects law through [knowledge cutoff — state
> explicitly].]*

---

### Step 7: Application / Analysis

Apply each element of the synthesized rule to the client's facts. This is the
analytical core of the memo.

**⟁ CLARIFY** — For each element, confirm whether the relevant facts are established,
disputed, or unknown. Conditional analysis is required for disputed or unknown facts.

**Core analytical disciplines:**

**7a. Element-by-element analysis:**
Address each element in order. For elements clearly satisfied (or not), state
briefly and move on. Spend analytical depth on contested elements.

> *Element 1 — [rule standard]: [client fact]. This element is satisfied / not
> satisfied / genuinely uncertain because [reason with citation to factual record].*

**7b. The "because" discipline:**
Every legal conclusion must be followed by "because" and a factual/legal reason:

> *The limitation clause is likely unenforceable [because] it purports to exclude
> liability for personal injury caused by negligence — an exclusion categorically
> prohibited by UCTA 1977 s 2(1), irrespective of reasonableness. [VERIFY citation]*

Never: "The clause is likely unenforceable." (conclusory — no reason given)

**7c. Fact-citation discipline:**
Every factual assertion in the Application must cite to a specific source:

> *Defendant gave written notice on 14 January 2025 (Letter, 14 Jan. 2025, at 2),
> which is 47 days after the contractual deadline of 28 November 2024 (Agreement
> s 12(b)).*

**7d. Counterargument block (mandatory for every Analysis section):**

> **Counterargument**: [Opposing party] will argue that [their best argument],
> relying on [best authority for their position] [VERIFY citation], which held
> [what the case held].
>
> **Rebuttal**: However, [case] is distinguishable because [specific factual or
> legal distinction]. Additionally, [additional rebuttal if available]. Under
> [controlling authority], [your conclusion] notwithstanding this contrary argument.

**The steelman requirement**: Present the opposing argument in its strongest form,
not a strawman. If you cannot articulate why the opposing argument is reasonable
and supported by authority, the analysis is incomplete.

**7e. Conditional analysis for uncertain facts:**

> *If the court finds that [Fact A — plaintiff's version], then [legal consequence A]
> and [conclusion A with probability]. If instead the court finds [Fact B —
> defendant's version], then [legal consequence B] and [conclusion B with probability].
> The more likely factual finding is [A/B] because [factual reasoning].*

**7f. Adverse authority treatment (mandatory):**
Never omit adverse controlling authority. Structure as:

> *It should be noted that [adverse case] [VERIFY citation] appears to support
> [opposing position]. That decision held [what it held]. However, [case] is
> distinguishable because [reason] / has been limited by [subsequent case] [VERIFY] /
> predates [statutory amendment effective date] [VERIFY]. Even applying [adverse
> case]'s reasoning, [your conclusion holds / carries increased risk] because [reason].*

**7g. Classification tiers by memo type:**

| Memo Type | Classification System |
|-----------|----------------------|
| Predictive research | STRONG (>75%) / PROBABLE (55-75%) / UNCERTAIN (40-55%) / ADVERSE (<40%) |
| Litigation risk | HIGH RISK / MEDIUM RISK / LOW RISK (tied to expected value ranges) |
| Deal advisory | CRITICAL / MATERIAL / MINOR (by business impact) |
| Regulatory compliance | COMPLIANT / PARTIAL / NON-COMPLIANT |
| Board summary | HIGH / MEDIUM / LOW (plain English risk rating) |

---

### Step 8: Probability and Conclusion

**8a. Probability calibration table** — Use this table for all probability language.
Never use hedging language ("may," "could") when the analysis supports a directional
conclusion.

| Language | Approximate Probability | When to Use |
|----------|------------------------|-------------|
| "Will" / "clearly will" | 90%+ | Settled law, unambiguous application to facts |
| "Should" / "very likely" | 75–90% | Strong authority, clear application, minor risk only |
| "Likely" / "probably" | 60–75% | Good authority, reasonable arguments on both sides, one side stronger |
| "More likely than not" | 55–60% | Marginal probability advantage; opposing argument is substantial |
| "Genuinely uncertain" / "may" | 40–55% | Both outcomes are plausible; result depends on fact-finding or unsettled law |
| "Unlikely" / "probably will not" | 25–40% | Adverse outcome more probable; one viable path to favorable result |
| "Very unlikely" / "should not" | 10–25% | Strong adverse precedent; viable only on exceptional facts |
| "Will not" / "clearly will not" | <10% | Controlling adverse authority; no realistic favorable path |

**Calibration discipline**: Every probability statement must include the primary reason
for that confidence level. Example: "We assess a 65–75% likelihood that the clause is
enforceable [because the California courts have consistently applied the blue pencil
doctrine to preserve severabie provisions, and this clause contains an explicit
severability instruction — however, the 5-year restriction exceeds the 3-year maximum
approved in the most recent comparable case, creating meaningful uncertainty]."

**8b. Conclusion format by memo type:**

**Predictive research memo conclusion:**
> *For the reasons set forth above, we conclude that [legal conclusion], with a
> probability assessment of approximately [X%]. The primary basis for this conclusion
> is [primary reason]. The primary risk to this conclusion is [adverse authority or
> uncertain fact]. If [adverse condition], the probability shifts to approximately [Y%].*

**Litigation risk assessment memo conclusion:**
> *Overall Litigation Risk: [HIGH / MEDIUM / LOW]*
> *Exposure range: $[low] – $[high], expected value approximately $[midpoint]*
> *Recommended posture: [file/defend/settle at $X / seek mediation]*
> *Key uncertainties: [list 2-3 most material unknowns that could shift the analysis]*

**Deal advisory memo conclusion:**
> *Overall Deal Risk: [CRITICAL / MATERIAL / MINOR]*
> *Recommended modifications: [list top 3 in priority order]*
> *Acceptable risk if not modified: [yes/no + conditions]*
> *Alternative structures considered: [list with relative risk profile]*

**Regulatory compliance memo conclusion:**
> *Compliance status: [COMPLIANT / PARTIAL / NON-COMPLIANT]*
> *Regulatory exposure: [describe risk if non-compliant — penalties, enforcement]*
> *Required remediation steps: [prioritized action list with deadlines if applicable]*
> *Safe harbor availability: [yes/no + conditions]*

---

### Step 9: Board Executive Summary (if requested)

Produce a 1–2 page plain-English risk summary derived from the research memo. Strip
all citations and legal jargon. Translate every legal risk into a business consequence.

**Board summary template:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ATTORNEY-CLIENT PRIVILEGED AND CONFIDENTIAL]
LEGAL RISK SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MATTER: [Matter name / description]
DATE:   [Date]
PREPARED FOR: [Board / Audit Committee / Executive Team]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OVERALL RISK RATING: ■ HIGH  □ MEDIUM  □ LOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RECOMMENDATION:
[One sentence — what the board should approve, decide, or be aware of.
Use business language: "We recommend against proceeding with the proposed
structure because it exposes the company to potential liability of $X–Y."]

KEY FINDINGS:
• [Business consequence in plain English — e.g., "The non-compete clause
  is unlikely to be enforced in California, leaving [Business Unit] exposed
  to competitive solicitation by departing employees immediately."]
• [Quantified exposure where available — e.g., "Estimated damages exposure
  if litigation proceeds: $2.5M–$7M, representing 4–12% of FY25 EBITDA."]
• [Timeline or trigger — e.g., "The statute of limitations expires
  [date]. A decision on filing must be made by [earlier date] to allow
  for investigation."]
• [Key uncertainty — e.g., "The analysis depends on how the court
  characterizes [X]. This is currently unsettled law."]

DECISION REQUIRED:
[What specific authorization, approval, or direction is sought from the board]

RISKS IF NO ACTION TAKEN:
[Plain English consequence of inaction — regulatory penalty, statute of
limitations expiry, default judgment, loss of insurance coverage trigger, etc.]

DETAILED ANALYSIS: See attached legal memorandum dated [date].
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Board summary discipline:**
- Every sentence must answer "So what?" from a business perspective
- No legal citations in the summary body (moved to underlying memo)
- Risk ratings must be calibrated consistently within your organization
  (define what "High/Medium/Low" means in dollar or probability terms)
- Action items must include ownership and a decision deadline
- Quantify exposure in dollar terms or percentage of revenue/EBITDA
  where any basis for quantification exists

---

### Step 10: Quality Assurance

Before delivering any memo, run these quality gates silently and revise if any fail.

#### Citation Quality Gates

Run all five gates before delivering. Fail any gate → revise before output.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every legal claim cites a specific statute, regulation, case, or authoritative secondary source | Add citation or mark "[UNVERIFIED]" |
| **Format** | All citations follow the correct format for the jurisdiction (Bluebook Practitioner / OSCOLA / AGLC) | Fix format |
| **Currency** | Every cited provision checked for amendments, repeal, or subsequent limiting authority | Flag "[CHECK CURRENCY — [year of cited authority]]" |
| **Domain** | Analysis stays within the identified controlling jurisdiction; no jurisdiction bleed | Remove or re-flag any jurisdictional bleed |
| **Confidence** | Uncertainty is explicitly stated, not hidden | Add confidence qualifier or probability statement |

#### Self-Interrogation for HIGH RISK / Adverse Conclusions

For any issue classified as HIGH RISK or reaching an adverse conclusion for the
client, apply this three-pass review before finalizing:

**Pass 1 — Legal Chain Integrity**: Does the risk conclusion follow logically from
the cited authority and the facts as stated? Would a court or regulator actually
reach this conclusion on these facts? Is the adverse authority being applied at the
correct level of generality?

**Pass 2 — Completeness**: Have all relevant statutes, regulations, and case law
been considered? Is there a safe harbor, exception, or defense that has not been
analyzed? Has the most recent authority been checked?

**Pass 3 — Challenge (Steelman of Client Position)**: What is the strongest argument
that the client's preferred outcome is correct? Under what circumstances might a
reasonable practitioner advise that the risk is manageable? Incorporate this
analysis into the counterargument section if not already present.

#### Verification Checklist (Mandatory Delivery Requirement)

Every delivered memo must include this verification checklist appended to it,
listing every citation that requires independent verification before the memo
is finalized:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MANDATORY VERIFICATION CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The following items MUST be independently verified
before this memo is finalized or relied upon:

CITATIONS REQUIRING VERIFICATION:
□ [Case citation 1] — verify in [Westlaw/LexisNexis/
  official reporter]; confirm no overruling or adverse
  subsequent history
□ [Statute reference 1] — verify current text; confirm
  no amendments effective after [date]
□ [Regulation reference 1] — verify current CFR/SI/
  Commonwealth Register text; confirm no amendment
  or revocation
[… list all citations]

FACTUAL MATTERS REQUIRING CONFIRMATION:
□ [Disputed fact 1 — confirm with client]
□ [Date/deadline 1 — verify against underlying documents]

RECENT DEVELOPMENTS — VERIFY FOR CHANGES AFTER [cutoff date]:
□ [Area of law 1 — check for post-[year] developments]
□ [Agency guidance 1 — check for updated guidance]

SCOPE CONFIRMATION:
□ The attorney supervising this matter has confirmed
  that this memo covers all material legal issues.
□ Any issues outside the scope of this memo have been
  separately identified and are being addressed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Complete Memo Output Template

The final delivered memo should follow this structure precisely:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[PRIVILEGE MARKING — see Step 3c for applicable marking]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MEMORANDUM

TO:      [Recipient — attorney name / GC / client]
FROM:    [AI-Assisted Draft — Requires Attorney Review and Adoption]
DATE:    [Date]
RE:      [Matter name — brief descriptive title]
         [Matter number if applicable]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONTROLLING JURISDICTION: [Jurisdiction]
CITATION FORMAT: [Bluebook Practitioner / OSCOLA / AGLC]
GOVERNING LAW: [Statute(s) / Common law / Regulatory framework]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

QUESTION(S) PRESENTED

  I.  Whether [Issue 1 — using "whether-when-and" structure].

 II.  Whether [Issue 2].

[… additional Issues as needed]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BRIEF ANSWER(S)

  I.  [Probable / Likely / Uncertain / etc.] [1–3 sentences
      stating the conclusion and primary reason. No citations.
      No new facts.]

 II.  [Answer to Issue II]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STATEMENT OF FACTS

  [Focused, objective narration of legally relevant facts.
  Cite to specific documents, depositions, or pleadings for
  each factual assertion. Flag disputed facts. Flag
  unverified facts as [UNVERIFIED — CONFIRM WITH CLIENT].]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DISCUSSION

I.  [Heading restating Issue I in affirmative or question form]

    A. [Sub-issue or element heading, if applicable]

       [CONCLUSION UP FRONT — CREAC structure]
       [State the conclusion on this issue first, then prove it.]

       Rule: [Rule statement with citations [VERIFY CITATION]]

       Explanation: [How courts have applied the rule — case
       illustrations with citations [VERIFY CITATION]]

       Application: [Element-by-element application to facts.
       "Because" discipline throughout. Fact citations to record.]

       Counterargument: [Opposing party will argue... Rebuttal:]

       Conclusion: [Restate conclusion with probability calibration
       and any conditions.]

    B. [Sub-issue B if applicable — same structure]

II. [Heading for Issue II — same structure]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONCLUSION

  [Consolidated conclusion addressing all Issues.
  Include overall probability assessment or risk rating.
  State the primary recommendation.]

  [For litigation risk memos — expected value range and
  strategic recommendation.]

  [For deal advisory memos — top risk modifications
  recommended.]

  [For compliance memos — compliance status and
  remediation priorities.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[BOARD EXECUTIVE SUMMARY — if requested; see Step 9 template]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[MANDATORY VERIFICATION CHECKLIST — always appended]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Jurisdiction-Specific Analysis Deep Dive

### United States

#### Authority Hierarchy (Federal)

Apply this hierarchy in strict order:
1. US Constitution (supreme law)
2. Federal statutes (USC) — look for implied preemption of state law
3. Federal regulations (CFR) — notice: *Chevron* deference overruled by *Loper
   Bright* (2024) [VERIFY]; *Skidmore* deference (weight proportional to agency
   persuasiveness) remains
4. SCOTUS decisions — binding on all lower courts
5. Circuit Court decisions — binding within circuit; "circuit split" triggers
   explicit treatment when it exists
6. District Court decisions — persuasive only

**Erie doctrine** [VERIFY citation]: In diversity jurisdiction cases, federal courts
apply state substantive law. Identify whether the question is governed by state or
federal law before citing any authority.

**Statutory interpretation canons** (apply per circuit's preferred methodology):
- Textualist: "plain meaning of the statutory text"; *King v. Burwell* [VERIFY]
- Purposivist: "interpret to effectuate congressional purpose"
- Whole act rule: interpret provision consistently with entire statute
- Surplusage canon: every word should have independent meaning
- Rule of lenity: ambiguous penal statutes resolved in favor of defendant

#### Bluebook Practitioner Format — Key Rules

**Cases** (Practitioner):
```
First citation:   Smith v. Jones, 123 F.3d 456, 460 (5th Cir. 1997).
Short form:       Smith, 123 F.3d at 461.
Immediately preceding: Id. at 461.
Unpublished:      Smith v. Jones, No. 23-1234, slip op. at 3 (5th Cir. Jan. 15, 2025).
```

**Federal statutes**:
```
17 U.S.C. § 101 (2018).
Sherman Antitrust Act, 15 U.S.C. §§ 1–7 (2018).
```

**Federal regulations**:
```
17 C.F.R. § 240.10b-5 (2024).
```

**Signal hierarchy** (before citation in Practitioner format):
- No signal: directly on point, cited for stated proposition
- *See*: supports proposition by clear inference, not directly stated
- *See also*: additional support (less direct than *see*)
- *Accord*: same legal proposition held in different jurisdiction/context
- *Cf.*: analogous but different; comparison supports proposition
- *But see*: contrary position; court has reached different result
- *Contra*: directly opposed to stated proposition
- *See generally*: general background; not directly on point

#### Work Product and Privilege (US)

Internal research memos prepared in anticipation of litigation are **opinion work
product** if they reflect the attorney's mental impressions and legal theories.
Near-absolute protection from discovery. *Hickman v. Taylor*, 329 U.S. 495 (1947)
[VERIFY citation]; Fed. R. Civ. P. 26(b)(3).

**Waiver risk**: Sharing memo with third parties outside the attorney-client
relationship can waive privilege. Common interest doctrine preserves privilege
when shared with co-defendants under a written common interest agreement.

**AI-generated content and work product** [VERIFY — actively developing area]:
Conservative practice requires supervising attorney to review, annotate, and
materially adopt AI-generated analysis before treating it as protected opinion
work product. The skill's output should always be identified as "AI-Assisted Draft —
Requires Attorney Review and Adoption" in the memo heading.

---

### England & Wales

#### Authority Hierarchy

Apply in order:
1. Acts of Parliament (primary legislation)
2. Statutory Instruments (secondary/delegated legislation)
3. UK Supreme Court decisions (post-2009; previously House of Lords)
4. Court of Appeal decisions
5. High Court decisions (strongly persuasive; binding in some contexts)
6. Privy Council decisions (highly persuasive — near-mandatory on many points)
7. EU retained law: apply EU-derived provisions retained under the *Retained EU
   Law (Revocation and Reform) Act 2023* [VERIFY current sunset status of specific
   retained provisions]
8. Decisions from other Commonwealth jurisdictions (persuasive)

**Statutory interpretation (E&W):**
- Literal rule: ordinary meaning of words
- Golden rule: modify literal reading to avoid absurdity
- Mischief rule: interpret to remedy the mischief Parliament intended to address
- Purposive approach (post-*Pepper v Hart* [1993] AC 593 [VERIFY]): Hansard
  admissible in limited circumstances to clarify ambiguous legislation
- Human Rights Act 1998 s 3: read and give effect to legislation compatibly with
  ECHR Convention rights "so far as it is possible to do so"

**Privilege in E&W:**
- Legal advice privilege: dominant purpose test (*Three Rivers (No 6)* [2004]
  UKHL 48 [VERIFY]) — communications between lawyer and client dominant purpose
  of giving/obtaining legal advice
- Litigation privilege: communications dominant purpose of pending or reasonably
  contemplated litigation
- Inadvertent disclosure: courts have discretion to restrain use

**Marking:** `LEGALLY PRIVILEGED AND CONFIDENTIAL — LEGAL ADVICE PRIVILEGE`

#### OSCOLA 4th Edition — Key Rules

**Cases:**
```
First citation:   R v Brown [1994] 1 AC 212 (HL).
Modern neutral:   Smith v Jones [2023] EWCA Civ 456, [12].
Short form:       Brown (n 3) 215.  [n 3 = footnote where full citation appears]
Immediately preceding: ibid 215.
```

**Statutes:**
```
Unfair Contract Terms Act 1977, s 2(1).
Consumer Rights Act 2015, s 62(1).
```

**Statutory instruments:**
```
Consumer Contracts (Information, Cancellation and Additional Charges)
Regulations 2013, SI 2013/3134, reg 9.
```

**EU retained legislation (post-Brexit UK):**
```
UK GDPR, art 6(1)(a).  [distinguish from EU GDPR, art 6(1)(a) — [VERIFY
current citation convention in UK practice]]
```

**Footnote structure**: First full citation in footnote; subsequent citations
use short form with cross-reference: `(n X)`. Use `ibid` for immediately
preceding footnote authority.

---

### Australia

#### Authority Hierarchy

Federal matters:
1. Australian Constitution (Commonwealth, State law may need to be read
   consistently with constitutional grants of power)
2. Commonwealth Acts; State Acts (for state matters)
3. Delegated legislation (Regulations, Rules, Ordinances)
4. High Court of Australia decisions — binding on all Australian courts
5. Full Court of the Federal Court of Australia decisions
6. State Supreme Court and Court of Appeal decisions (binding within that
   state; persuasive elsewhere in Australia)

Persuasive:
- Decisions from other Australian jurisdictions (strong persuasive weight)
- UK decisions (highly persuasive in common law areas; weaker in statutory
  interpretation)
- New Zealand, Canada, Singapore decisions (persuasive)
- Privy Council (historical; persuasive but not binding post-1986)

**Statutory interpretation (Australia):**
Apply *Acts Interpretation Act 1901* (Cth) s 15AA: "In interpreting a provision
of an Act, the interpretation that would best achieve the purpose or object of
the Act is to be preferred to each other interpretation." [VERIFY current text]

High Court methodology:
- *Project Blue Sky* (1998) 194 CLR 355 [VERIFY]: purpose and text read together;
  no hierarchy between text and purpose
- *SZTAL* [2017] HCA 34 [VERIFY]: begin with the ordinary meaning of words;
  context and purpose illuminate ambiguity

**Privilege in Australia:**
Legal professional privilege / client legal privilege under *Evidence Act 1995*
(Cth) ss 118–119 [VERIFY]: confidential communications for dominant purpose
of legal advice. *Esso Australia Resources Ltd v Commissioner of Taxation*
(1999) 201 CLR 49 [VERIFY] established the dominant purpose test.

**Marking:** `CLIENT LEGAL PRIVILEGE — CONFIDENTIAL LEGAL ADVICE`

#### AGLC 4th Edition — Key Rules

**Cases:**
```
High Court:  Mabo v Queensland (No 2) (1992) 175 CLR 1 (HCA).
              [round brackets when volume number present]
NSWCA:       Smith v Jones [2023] NSWCA 123, [45].
              [square brackets when year identifies volume]
Short form:  Mabo (No 2) (n 12) 66.  [n 12 = footnote number]
```

**Australian statutes (italicized):**
```
Competition and Consumer Act 2010 (Cth) s 18.
Corporations Act 2001 (Cth) s 181(1).
Fair Work Act 2009 (Cth) s 385.
Environmental Planning and Assessment Act 1979 (NSW) s 4.15.
```

**Key AGLC difference from OSCOLA**: Statute names are *italicized* in AGLC.
Jurisdiction in round brackets after statute name.

---

## Confidence Scoring

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95–1.0 | Settled law, clear statute, unambiguous application | State with full confidence; no caveat needed |
| **High** | 0.80–0.94 | Strong authority, minor factual uncertainty only | State with brief caveat ("subject to confirmation of [fact]") |
| **Probable** | 0.60–0.79 | Good arguments for the conclusion; meaningful contrary arguments | State conclusion with probability calibration and contra-indicators noted |
| **Uncertain** | 0.40–0.59 | Genuinely uncertain outcome; both sides have substantial arguments | Flag for professional review; present both sides with probability ranges |
| **Adverse** | 0.0–0.39 | Weak basis; adverse authority controls; favorable outcome requires exceptional facts | Do not assert favorably; clearly flag adverse risk; recommend alternative strategies |

---

## Anti-Patterns Catalogue

What NOT to do when drafting legal memoranda:

1. **Conclusory analysis without element-by-element work** — Writing "the clause is
   likely unenforceable because it is overbroad" without applying each element of
   the applicable test to the specific facts. Every conclusion must be earned through
   analysis, not asserted.

2. **Omitting adverse controlling authority** — The most common failure identified
   by supervising attorneys. An internal research memo that omits adverse authority
   is not an honest analysis — it is advocacy masquerading as research.

3. **Jurisdiction bleed** — Citing California law on a New York matter, applying
   federal circuit authority to a state court case, or applying English law to a
   Scottish law issue. Every citation must be verified as being from a court
   with authority over the controlling jurisdiction.

4. **Paraphrasing statutory text** — Summarizing the statute in your own words
   instead of quoting the operative text verbatim. Paraphrasing introduces error
   and masks ambiguity that may be central to the analysis.

5. **Citation hallucination (AI-specific)** — Generating plausible-sounding but
   non-existent case citations, incorrect reporter volumes, or fabricated holdings.
   Every AI-generated citation must be independently verified before delivery.
   The verification checklist is non-negotiable.

6. **Hedging every sentence** — Using "may," "could," or "might" throughout to
   avoid taking a position. A memo that hedges every conclusion is useless for
   decision-making. Calibrate probability language using the probability table
   in Step 8a and take a reasoned position.

7. **The passive voice problem** — "Notice was given" instead of "The contractor
   gave written notice by email at 3:47 PM on 14 January 2025 (Email, 14 Jan.
   2025, Exh. C)." Legal analysis requires precision about who did what, when,
   and how. Passive voice obscures legally material agency.

8. **Issue framing that begs the question** — Framing the QP as: "Whether the
   defendant wrongfully terminated the contract" prejudges the conclusion. The
   issue should be framed neutrally using the "whether-when-and" technique.

9. **Scope creep** — Addressing legal issues not raised in the Questions Presented.
   Memos should be scoped carefully; addressing unrequested issues creates
   potential professional responsibility exposure by creating advice the client
   did not request and may not have wanted.

10. **Outdated authority without verification** — Citing a statute that has been
    amended or a case that has been overruled. For any authority more than
    3 years old in a rapidly developing area, always flag [CHECK CURRENCY].

11. **Treating persuasive authority as mandatory** — Citing a district court opinion
    from another circuit as if it controls, or citing a law review article as
    establishing the rule. Authority tier must be explicitly stated.

12. **String citations without explanation** — Citing six cases in a footnote
    without explaining what each adds. Each citation must have a reason; if
    you cannot articulate it, cut the citation.

13. **No specific record citation in the Application section** — Every factual
    assertion in the Analysis must cite to a specific document, deposition page,
    or pleading paragraph. "The contract provides for a 5-year restriction" without
    citing "Agreement § 12(c)" is sloppy practice.

14. **Board summary that repeats legal jargon** — The board executive summary
    must be completely free of legal terminology and citations. Every sentence
    must answer "So what?" from a business perspective.

15. **Failing to distinguish the client's facts from cited case facts** — Spending
    two paragraphs reciting the facts of a cited case without explicitly connecting
    them to the client's facts through comparison or distinction.

16. **No explicit conclusion** — Writing analysis that leads to an implicit
    conclusion without explicitly stating it. Every Question Presented must receive
    an explicit, stated answer in the Conclusion section.

17. **Opinion letter format for internal memo** — Using first-person opinion
    language ("It is our opinion that") in an internal predictive memo. Opinion
    letters create professional responsibility obligations and are only appropriate
    when signed by a partner with explicit reliance qualifications.

18. **Failing to mark privilege** — Delivering a legal memo without privilege
    markings. Legal memos are targets in litigation discovery; every memo should
    carry the appropriate privilege marking from the moment of creation.

19. **Over-confident AI output** — Presenting AI-generated probability assessments
    as equivalent to calibrated professional legal judgment without disclosing the
    AI-assisted nature of the draft. The memo heading must always note "AI-Assisted
    Draft — Requires Attorney Review and Adoption."

20. **No verification checklist** — Finalizing a memo without appending the
    mandatory verification checklist that lists every citation and factual matter
    requiring independent confirmation. This is the primary safeguard against
    citation hallucination in AI-assisted drafting.

---

## Writing Standards

Apply these quality gates before delivering the memo:

**Precision:**
- Every legal conclusion is supported by cited authority or explicit factual reasoning
- Probability language is calibrated per the probability table — no untargeted hedging
- Factual assertions cite specific sources — documents, deposition pages, pleading paragraphs
- Statutory text is quoted verbatim, not paraphrased

**Objectivity:**
- Both favorable and unfavorable authority and facts are addressed
- Counterarguments are presented in their strongest form (steelman, not strawman)
- Probability assessments are calibrated, not advocacy-toned
- Adverse controlling authority is not omitted or minimized

**Clarity:**
- Plain English for non-legal sections (board summary, executive sections)
- Active voice where legally possible — "the contractor failed to deliver" not
  "delivery was not made"
- Each paragraph has one main point
- Issue headings clearly restate the issue in affirmative or question form

**Completeness:**
- All Questions Presented receive explicit answers in Brief Answers and Conclusion
- All elements of the applicable test are addressed in the Application section
- The verification checklist is appended and populated
- Scope statement identifies what the memo does and does not cover

**Format integrity:**
- Privilege marking is present and correct for memo type and jurisdiction
- Controlling jurisdiction and citation format are stated in the memo header
- CREAC structure is maintained in each Discussion section
- Heading hierarchy is consistent (Issue I / Sub-issue A / Sub-issue B)

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**
- In Step 6 (Rule Synthesis), query legalcode-mcp for primary authority on each
  legal question — statutes, regulations, leading cases
- Save research results to a local reference file (e.g.,
  `/tmp/legal-memo-research-[matter].md`) before drafting
- Mark all legalcode-mcp-verified citations as VERIFIED in the Glass Box audit trail
- For regulatory compliance memos, query for current agency guidance and
  enforcement actions
- For multi-jurisdiction memos, run separate queries per jurisdiction to prevent
  cross-jurisdiction authority contamination

**Without legalcode-mcp:**
- Proceed with in-memory rule synthesis
- Mark every citation with [VERIFY CITATION] — mandatory, not optional
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus analytical quality on structure, counterargument treatment, and
  probability calibration rather than legal substance depth
- The verification checklist becomes even more critical — flag all citations
  for independent confirmation before the memo is relied upon

**WebSearch / WebFetch (fallback):**
If legalcode-mcp is unavailable and the matter involves a recent legislative
development (post-2023 statutes, new regulations, recent enforcement actions),
use WebSearch to confirm the current legal landscape before drafting the Rule
section. Cite web sources with full URL and access date; note they require
verification against official sources.

---

## Glass Box Audit Trail

Append this audit section to every produced memo for traceability:

```yaml
glass_box:
  skill_name: "legalcode-legal-memorandum"
  memo_type: "[Predictive Research / Litigation Risk / Deal Advisory /
               Regulatory Compliance / Board Summary]"
  controlling_jurisdiction: "[Jurisdiction — court system]"
  governing_law: "[Primary statute or doctrine]"
  citation_format: "[Bluebook Practitioner / OSCOLA / AGLC]"
  privilege_marking: "[Marking applied]"
  issues_addressed: "[Number of Questions Presented]"
  analysis_depth: "[Standard / Deep]"
  legalcode_mcp: "[Connected — N citations verified / Not connected]"
  citations_generated: "[N total]"
  citations_verified: "[N verified / N requiring independent verification]"
  counterarguments_addressed: "[Yes — N counterarguments steelmanned]"
  adverse_authority_addressed: "[Yes / None identified — [VERIFY]]"
  probability_calibration_applied: "[Yes — probability table used]"
  verification_checklist_appended: "[Yes]"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "All citations require independent verification — [N] citations flagged"
    - "Knowledge cutoff: [date] — recent developments require separate verification"
    - "[Any scope limitations, assumptions, or caveats specific to this memo]"
  reviewer: "AI-Assisted Draft — requires review and adoption by qualified
             legal professional licensed in [jurisdiction]"
```

---

## Localization Notes

This skill covers US, England & Wales, and Australia as primary jurisdiction tracks.
For other jurisdictions, it provides the structural framework (IRAC/CREAC, privilege
marking, probability calibration) but cannot provide reliable primary authority.

**For jurisdictions outside US/UK/AU:**
1. Apply the memo structure (Questions Presented, Brief Answers, Facts, Discussion,
   Conclusion) — this is jurisdiction-agnostic
2. Apply the analytical disciplines (element-by-element, steelmanning, adverse
   authority, probability calibration) — these are jurisdiction-agnostic
3. Mark all legal authority with [VERIFY — local counsel required] rather than
   providing specific citations
4. Note explicitly in the memo header: "Primary legal authority requires research by
   counsel admitted in [jurisdiction]; this memo provides structural framework only"
5. The verification checklist applies with even greater force

For Canada, Singapore, New Zealand, Ireland, and other common law jurisdictions,
the CREAC structure and analytical disciplines apply directly; the citation format
and authority hierarchy require localization by counsel admitted in that system.

---

## Provenance

Created by Legalcode (2026-03-01). Legalcode original synthesis. Research conducted
via 2-agent parallel research pipeline covering: IRAC/CREAC structural methodology,
US/E&W/AU authority hierarchies, Bluebook 21st/OSCOLA 4th/AGLC 4th citation formats,
attorney-client privilege and work product doctrine across three jurisdictions,
probability language calibration standards, board executive summary format, AI-specific
risks in legal memo drafting, and anti-patterns from legal writing pedagogy and law
firm practitioner guidance. No third-party skill inputs. All legal authority marked
[VERIFY CITATION] per AI hallucination risk protocol.
