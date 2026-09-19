---
name: legalcode-us-federal-regulatory-comment
description: Draft, structure, and sharpen federal regulatory comments for APA notice-and-comment rulemaking
  (5 U.S.C. § 553). Use when responding to a Notice of Proposed Rulemaking (NPRM), submitting comments
  to a federal agency docket on regulations.gov, challenging agency statutory authority, invoking the
  major questions doctrine (West Virginia v. EPA, 2022), analyzing the post-Chevron landscape after Loper
  Bright Enterprises v. Raimondo (2024), building an administrative record for judicial review, raising
  arbitrary and capricious arguments under APA § 706, analyzing Congressional Review Act implications,
  or preparing standing documentation. Covers comment structure, legal argument construction, policy argumentation,
  data and scientific evidence presentation, record preservation, and judicial review strategy. US federal
  jurisdiction only.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode US Federal Regulatory Comment

> **Disclaimer**: This skill provides a framework for AI-assisted drafting of federal
> regulatory comments. It does not constitute legal advice. All outputs should be reviewed
> by a qualified attorney licensed to practice before the relevant federal agency or in the
> relevant federal circuit before submission. Legal citations are drawn from research and
> carry hallucination risk — verify all statutory citations, case names, and holdings
> against authoritative sources (regulations.gov, govinfo.gov, Westlaw, Lexis) before
> relying on them. The administrative law landscape is evolving rapidly following Loper
> Bright (2024) and West Virginia v. EPA (2022); verify current doctrine before filing.

---

## Purpose and Scope

This skill drafts, structures, and strengthens federal regulatory comments for US
notice-and-comment rulemaking under the Administrative Procedure Act (APA), 5 U.S.C.
§ 553. It supports commenters at every stage — from the first read of an NPRM through
a polished, record-preserving submission ready for the docket.

**Covers:**

- Comment structure and format for any federal agency docket
- Statutory authority arguments, including major questions doctrine and nondelegation
- Arbitrary and capricious analysis under APA § 706 to build the judicial review record
- Post-Loper Bright (2024) statutory interpretation strategy
- Cost-benefit and regulatory impact analysis critique
- Scientific and empirical evidence submission best practices
- Standing documentation for entities seeking future judicial review
- Congressional Review Act (CRA) implications and framing
- Record preservation discipline — ensuring all arguments are in the administrative record
- Response to prior comments and preamble analysis

**Does not:**

- File comments directly to regulations.gov (submitter must do this)
- Constitute legal advice or substitute for qualified administrative law counsel
- Guarantee judicial review outcomes — courts exercise independent judgment post-Loper Bright
- Cover state-level notice-and-comment rulemaking (state APAs vary significantly)
- Cover formal APA rulemaking (5 U.S.C. §§ 556-557) or adjudications

---

## Jurisdiction and Governing Law

**Jurisdiction**: US federal exclusively.

**Primary authority**:

- Administrative Procedure Act, 5 U.S.C. §§ 551–559, 701–706
- Congressional Review Act, 5 U.S.C. §§ 801–808
- Loper Bright Enterprises v. Raimondo, 603 U.S. \_\_\_ (2024) — overruled Chevron deference [VERIFY citation when final reporter available]
- West Virginia v. EPA, 597 U.S. 697 (2022) — major questions doctrine
- Motor Vehicle Mfrs. Ass'n v. State Farm Mut. Auto. Ins. Co., 463 U.S. 29 (1983) — arbitrary and capricious standard
- Ohio v. EPA, 603 U.S. \_\_\_ (2024) — arbitrary and capricious, post-Loper Bright [VERIFY]
- Encino Motorcars, LLC v. Navarro, 579 U.S. 211 (2016) — unexplained agency reversals
- FCC v. Fox Television Stations, Inc., 556 U.S. 502 (2009) — agency policy changes
- NFIB v. OSHA, 595 U.S. 109 (2022) — major questions, healthcare/workplace
- Biden v. Nebraska, 600 U.S. 477 (2023) — major questions, HEROES Act

**Note**: The post-Loper Bright landscape is actively developing. Courts of appeals are
working through Loper Bright's implications. Verify current circuit precedents before
filing in a specific circuit. Mark all case citations with [VERIFY] until confirmed against
an authoritative legal database.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would substantially change comment strategy or argument selection
- The commenter's purpose (agency engagement vs. litigation preservation) is unclear
- Multiple valid argument architectures exist
- Statutory authority, standing, or record preservation questions require commenter-specific facts

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

### Step 1: Accept the NPRM and Context

Accept input in any format:

- **Docket ID**: Agency docket number (e.g., EPA-HQ-OAR-2021-0208) for lookup on
  regulations.gov
- **NPRM text**: The full or partial text of the Notice of Proposed Rulemaking pasted
  directly
- **Federal Register citation**: Volume, page, and date of the NPRM in the Federal
  Register
- **Summary**: User's summary of the NPRM and proposed rule

If no NPRM or docket is provided, ask for the docket ID or a description of the proposed
rule. Regulations.gov is the primary public access point for NPRM text and dockets.

### Step 2: Gather Commenter Context

**⟁ CLARIFY** — Before drafting, gather this information. Present as structured options
where possible:

1. **Who is the commenter?**
   - Options: Trade association / industry group, Individual company or regulated entity,
     Nonprofit or advocacy organization, Academic or research institution, State or local
     government, Private individual, Coalition (multiple organizations filing jointly)
   - _Why this matters_: Shapes standing documentation, institutional credibility, and
     appropriate tone. A trade association comment carries different weight than an
     individual comment.

2. **Primary purpose?**
   - Options:
     - **Persuade the agency** — primary goal is to get the agency to change the proposed
       rule or adopt the commenter's alternative
     - **Preserve the record for litigation** — primary goal is ensuring every legal
       argument is in the administrative record before the comment period closes
     - **Both** — persuade where possible, preserve everything regardless
     - **Procedural objection only** — challenge the agency's authority to promulgate
       this rule at all
   - _Why this matters_: Determines argument selection, depth, and whether record
     preservation dominates drafting decisions.

3. **What is the commenter's relationship to the proposed rule?**
   - Free text. Prompt: How does the rule affect the commenter? What is their economic,
     operational, or legal exposure? Any prior engagement with this rulemaking?
   - _Why this matters_: Grounds the standing analysis and shapes business-impact arguments.

4. **What is the deadline?**
   - Options: Imminent (days), Standard (1-2 weeks), Ample time (more than 2 weeks)
   - _Why this matters_: Depth of research and number of arguments to develop scales
     with available time.

5. **Focus areas?** (allow multiple selections)
   - Options: Statutory authority / major questions doctrine, Arbitrary and capricious /
     inadequate record, Cost-benefit and economic impact analysis, Scientific or technical
     evidence, Standing documentation, Alternative regulatory approaches, CRA implications,
     Procedural defects (inadequate notice, insufficient comment period), All of the above
   - _Why this matters_: Allows the analysis to lead with what matters most to the commenter.

### Step 3: Analyze the NPRM

Before drafting, systematically assess the NPRM across five dimensions:

**3a. Statutory Authority Analysis**

| Question                                                                    | What to Find                                                                                                  |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| What statute authorizes this rulemaking?                                    | Identify the enabling act, specific provision, and whether it was enacted recently or long ago                |
| Does the statute clearly authorize this rule?                               | Identify the specific delegation — is it a broad grant ("reasonable regulations") or a narrow one?            |
| Does the rule raise a major question?                                       | Apply the two-part test: (1) vast economic/political significance + (2) absent clear authorization            |
| Is the agency's statutory interpretation the "best reading"?                | Post-Loper Bright: courts give no deference — analyze the text, structure, history, and purpose independently |
| Has this statutory provision been relied on before for rules of this scope? | Agency precedent and historical practice inform whether the reading is novel or established                   |

**3b. Procedural Compliance**

| Requirement                   | Check                                                                                                                                       |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Notice adequacy               | Does the NPRM fairly apprise interested parties of the proposed rule? Logical outgrowth doctrine — can the final rule differ substantially? |
| Comment period length         | Is 60 days provided? Has the agency provided good cause justification for any shortened period?                                             |
| Regulatory impact analysis    | Has the agency complied with Executive Order 12866 / 13563 / 14094 cost-benefit requirements?                                               |
| Science and data transparency | Has the agency disclosed the data and models underlying the rule? Is the scientific basis reproducible and peer-reviewed?                   |
| Required consultations        | Has the agency complied with Small Business Regulatory Enforcement Fairness Act (SBREFA) if applicable? Regulatory Flexibility Act (RFA)?   |
| Major rule designation        | Has the agency correctly analyzed whether this is a "major rule" under the CRA?                                                             |

**3c. Arbitrary and Capricious Vulnerabilities**

Assess whether the agency has:

- Examined all relevant data
- Articulated a satisfactory explanation connecting facts to conclusions
- Relied on factors Congress did not intend the agency to consider
- Failed to consider important aspects of the problem
- Offered explanations that run counter to the evidence
- Ignored a significant alternative that was reasonably available
- Reversed prior policy without adequate explanation (Encino Motorcars)

**3d. Cost-Benefit and Impact Analysis**

Identify weaknesses in the agency's economic analysis:

- Underestimated compliance costs
- Overestimated benefits
- Discount rate choices (3% vs. 7% OMB circular guidance)
- Failure to analyze distributional impacts
- Inadequate treatment of uncertainty and sensitivity analysis
- Failure to consider indirect or cumulative regulatory burdens

**3e. Scientific and Technical Basis**

Assess the quality of the underlying scientific evidence:

- Is the cited research peer-reviewed?
- Are the underlying data publicly accessible?
- Has the agency's interpretation of the science been challenged in the literature?
- Are there contradictory studies the agency has not addressed?

**⟁ CLARIFY** — After the NPRM analysis, present a prioritized list of identified
vulnerabilities and ask the commenter:

"I've identified these potential comment angles. Which should be the primary arguments?
(You can select multiple.)

- [List each identified vulnerability with a 1-sentence description]
- **All of the above** — include all in a comprehensive filing

This affects comment length, depth, and the overall strategy."

### Step 4: Gather Supporting Evidence

Before drafting, identify and request supporting materials:

**⟁ CLARIFY** — Ask the commenter:

- "Do you have internal data, economic analyses, or technical studies that contradict the
  agency's assumptions? If so, these should be submitted as attachments and incorporated
  by reference in the comment."
- "Are there peer-reviewed studies, industry surveys, or government data the agency failed
  to consider? Identify them now so they can be properly cited and submitted."
- "Do you have a prior comment or regulatory history with this agency on this subject?
  Prior submissions in the same rulemaking are part of the record and can be incorporated
  by reference."

**Evidence Priority Framework**:

| Evidence Type                                     | Weight            | Submission Requirement                                            |
| ------------------------------------------------- | ----------------- | ----------------------------------------------------------------- |
| Peer-reviewed published research                  | Highest           | Attach or cite with DOI/URL accessible to agency                  |
| Agency's own prior statements or data             | Very High         | Cite Federal Register citation, agency website, or FOIA documents |
| Government agency data (BLS, BEA, EIA, CBO)       | High              | Cite with specific table/report reference                         |
| Industry economic studies (disclosed methodology) | Medium-High       | Attach with methodology documentation                             |
| Expert declarations or affidavits                 | Medium-High       | Attach signed declarations with CV                                |
| Trade association surveys (public methodology)    | Medium            | Attach with response rate and methodology                         |
| Anecdotal or case study evidence                  | Supplemental only | Use to illustrate but not as primary support                      |

### Step 5: Construct the Legal Arguments

Organize arguments using the **Argument Tier Classification** below. Draft each argument
using the **Argument Block Format**.

#### Argument Tier Classification

**TIER 1 — FOUNDATIONAL (Statutory / Constitutional)**

The agency lacks authority to promulgate this rule as written, or the rulemaking process
violated a mandatory procedural requirement. These arguments, if successful, prevent the
rule from taking effect entirely.

- Major questions doctrine (West Virginia v. EPA) — agency claims vast significance without clear congressional authorization
- Post-Loper Bright statutory interpretation — the agency's reading is not the "best reading" of the statute
- Nondelegation concerns — Congress has not set forth an intelligible principle governing this authority [VERIFY current doctrine]
- Procedural invalidity — inadequate notice (final rule not a logical outgrowth), shortened comment period without good cause, failure to publish required regulatory impact analysis

**TIER 2 — RECORD / ARBITRARY AND CAPRICIOUS**

The rule violates APA § 706(2)(A) as arbitrary and capricious — the agency failed to
engage in reasoned decision-making. These arguments do not challenge the agency's
authority but require the agency either to fix the record or have the rule vacated by
a reviewing court.

- Failure to consider relevant data or alternatives
- Unexplained policy reversal from prior agency positions
- Cost-benefit analysis deficiencies
- Inadequate treatment of contrary scientific evidence
- Inadequate response to significant comments in a prior NPRM or ANPRM

**TIER 3 — POLICY / TECHNICAL (Supplemental)**

The rule is within the agency's authority and the record may be adequate, but the
commenter proposes a better approach. These arguments seek voluntary modification and are
less likely to succeed on judicial review, but agencies frequently incorporate them.

- Proposed regulatory alternatives with lower cost/burden
- Phased compliance timelines
- Technical corrections, definitions, or exemptions
- Industry-specific adjustments
- Implementation guidance requests

#### Argument Block Format

For each argument, use this structure:

```
**[TIER X] — [Argument Name]**

**Legal basis**: [Specific statute, case, or principle. Mark [VERIFY] if not confirmed.]
**Summary of agency's position**: [What the NPRM says on this point]
**The flaw**: [Precisely what the agency got wrong — missing data, wrong legal standard,
  ignored alternative, contradiction in the record]
**Supporting evidence**: [Studies, data, prior agency statements, contrary scientific evidence]
**Requested action**: [Specifically what the agency should do: withdraw, revise, or explain]
**Record preservation note**: [If this argument is primarily for judicial review, note it
  explicitly so the commenter understands its purpose]
```

### Step 6: Draft the Comment

Write the comment following the **Output Format Template** at the end of this skill.

**Drafting discipline:**

1. **Lead with your strongest argument** — Agency staff read many comments. The first
   page determines whether the rest gets serious attention.

2. **Be specific, not conclusory** — "The proposed rule is arbitrary and capricious
   because the agency failed to consider the impact on small manufacturers, as documented
   in the attached EIA" is useful. "The rule is arbitrary and capricious" is not.

3. **State affirmative alternatives** — For every objection, propose a specific alternative.
   An agency that ignores a reasonable alternative it was presented faces stronger arbitrary
   and capricious exposure. A comment that only opposes gives the agency nothing to adopt.

4. **Submit all supporting materials** — Attach and incorporate by reference all studies,
   declarations, and data. Do not rely on hyperlinks for materials central to your argument —
   links can break, and the administrative record captures what was submitted, not what
   was linked.

5. **Preserve everything** — If the comment is also a record-preservation vehicle, include
   every material argument, even those the commenter does not expect to prevail on. Courts
   cannot review issues not raised during the comment period.

6. **Calibrate length to the stakes** — A short comment on a narrow technical rule can be
   effective at one page. A major rule with significant economic impact warrants a detailed
   submission with attachments.

### Step 7: Standing Documentation

If the commenter may seek judicial review if the rule is finalized over objection, include
a standing section in the comment (or in a separate declaration):

**Three-element standing documentation:**

1. **Injury-in-fact**: Describe the concrete, particular, and imminent harm the rule will
   cause the commenter. Use specific numbers: "Our members will incur estimated compliance
   costs of $X in Year 1 based on the attached economic analysis." Avoid speculative or
   generalized harms.

2. **Causation/Traceability**: Connect the injury directly to the agency's rule. "The
   proposed requirement to [specific obligation] directly causes [specific harm] because
   [causal mechanism]."

3. **Zone of interest**: Demonstrate that the commenter's injury falls within the type of
   harm the statute's protections were designed to address.

**⟁ CLARIFY** — Ask: "Is this commenter likely to seek judicial review if the rule is
finalized? If yes, the standing documentation must be specific and detailed. A vague
description of harm will not support Article III standing."

**Organizational standing** (for associations): Document that at least one member would
have standing in their own right, that the interests are germane to the association's
purpose, and that neither the claim nor relief requires individual member participation.

### Step 8: Congressional Review Act Analysis

If the proposed rule is major (annual economic effect ≥ $100 million, major increase in
costs, or significant adverse effects on competition/jobs/investment):

- Note that the agency must submit the rule to Congress and GAO under 5 U.S.C. § 802
- Identify whether the agency has correctly classified the rule as a "major rule"
- If the commenter believes the rule is a major rule that the agency misclassified as
  non-major, raise this in the comment — the classification affects the CRA congressional
  review period
- Frame any argument about agency overreach to flag that Congress retains authority to
  review and disapprove the rule
- If the comment opposes the rule on major questions grounds, note that Congress, not
  the agency, is the appropriate body to make the underlying policy decision

### Step 9: Review and Record-Preservation Check

Before finalizing the comment, run this review:

**⟁ CLARIFY** — If the primary purpose is record preservation for litigation, ask:
"Should I run a full record-preservation audit to identify any material argument that has
not been included in the comment? Missing an argument during the comment period may
prevent raising it in court."

**Record-preservation checklist:**

- [ ] Every statutory authority argument raised explicitly
- [ ] Every procedural violation identified and cited
- [ ] Every arbitrary and capricious vulnerability documented with specific factual support
- [ ] All contrary scientific evidence submitted or cited with accessible reference
- [ ] All economic impact data submitted or attached
- [ ] Standing elements documented for any entity likely to seek judicial review
- [ ] All proposed alternatives stated with enough specificity for the agency to adopt
- [ ] Comment cross-references any prior ANPRM/NPRM comments in this docket the commenter has submitted
- [ ] Attachments clearly labeled, paginated, and incorporated by reference in the comment text

### Step 10: Quality Verification

Before delivering the draft comment, run the Quality Assurance Framework:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every TIER 1 argument, run the 3-pass Self-Interrogation.
3. Assign a Confidence Score to each material legal claim.
4. Verify the comment is internally consistent — argument A should not undermine argument B.
5. Generate the Glass Box Audit Trail and append it.

---

## Comment Component Reference

### Statutory Authority Arguments (Post-Loper Bright, Post-WV v. EPA)

#### Major Questions Doctrine

Apply the two-part test from West Virginia v. EPA (2022) [VERIFY citation]:

**Part 1 — Vast economic and political significance:**

- The rule affects a large sector of the economy (billions in compliance costs)
- The rule resolves a highly contested political or social question
- Congress has not previously delegated this specific authority
- The rule represents a dramatic expansion of the agency's historical role
- Agencies in other domains have not exercised similar authority without specific authorization

**Part 2 — Absent clear congressional authorization:**

- The enabling statute does not specifically authorize this type of regulation
- The statutory language is at best ambiguous and requires interpretive stretch
- Congress has considered and declined to pass legislation on this specific topic
- The statutory provision relied on is a general grant or catch-all, not a specific delegation
- There is no longstanding historical practice of the agency exercising this authority

**Drafting the major questions argument:**

1. Name the doctrine and cite West Virginia v. EPA
2. Characterize the significance: quantify economic impact, political salience, and scope
3. Identify the specific statutory provision the agency relies on
4. Show the mismatch: the provision's ordinary meaning does not reach this type of action
5. Cite Biden v. Nebraska (2023) and NFIB v. OSHA (2022) for comparable patterns [VERIFY]
6. Conclude: agency must point to clear congressional authorization — it cannot

#### Post-Loper Bright Statutory Interpretation

Following Loper Bright Enterprises v. Raimondo (2024), courts will no longer defer to the
agency's interpretation of ambiguous statutes. Courts exercise independent judgment on the
"best reading" of the statute.

**Comment strategy:**

1. Do not concede statutory ambiguity — argue for the best reading, not just a permissible one
2. Deploy the traditional tools of statutory interpretation: text, structure, context,
   statutory history, and purpose
3. Where the agency argues an alternative reading is also "permissible," argue that it is
   not — and that even if permissible, it is not the best reading
4. Preserve the argument for judicial review: courts post-Loper Bright will independently
   resolve these interpretive disputes

**Argument components:**

- Textual analysis: what the statutory words actually mean in plain English
- Structural argument: how the provision fits within the broader statutory scheme
- Historical practice: what the agency has done for decades under this provision
- Congressional intent: what Congress was addressing when it enacted the provision
- Canon of constitutional avoidance: if the agency's reading raises major questions or
  constitutional concerns, the statute should be read to avoid those issues

#### Nondelegation [VERIFY current doctrine — developing area post-2024]

If the statutory delegation is extremely broad with no intelligible principle, a
nondelegation argument may be available. This remains a challenging doctrine [VERIFY
current circuit and Supreme Court approach before relying on this argument].

---

### Arbitrary and Capricious Arguments (APA § 706)

Under Motor Vehicle Mfrs. Ass'n v. State Farm (1983) [VERIFY], a rule is arbitrary and
capricious if the agency:

| Failure Mode                 | Comment Argument                                                                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Ignored relevant data        | "The agency failed to consider [specific study/data] that was submitted in [prior NPRM/comment] and contradicts the agency's core assumption that [X]" |
| No rational explanation      | "The agency's preamble on pages [X-Y] does not explain why [assumption A] leads to [conclusion B]. The logical gap is [specify]"                       |
| Relied on irrelevant factors | "The agency's cost-benefit analysis includes [irrelevant factor] that Congress did not authorize the agency to weigh under [statute]"                  |
| Missed important aspect      | "The agency's analysis ignores [specific population, sector, or effect]. This omission is material because [explain how it changes the analysis]"      |
| Contradicted by evidence     | "The agency states [X], but its own data at page [Y] of the preamble shows [not-X]. This internal contradiction is arbitrary"                          |
| Unexplained reversal         | "In [prior rule/guidance, cite Federal Register], the agency took the opposite position without adequate explanation [cite Encino Motorcars]"          |

**Record-building technique for A&C arguments:**
For each arbitrary and capricious argument, submit the specific, contrary data or analysis
that the agency failed to consider. Courts cannot find the agency acted arbitrarily by
ignoring evidence it was never presented with.

---

### Cost-Benefit Analysis Critique

Federal agencies promulgating significant rules must conduct regulatory impact analysis
under Executive Order 12866 (Clinton, 1993) and subsequent EOs. OMB Circular A-4 (2023
revision) governs analytical methodology [VERIFY current EO/OMB framework, which has
changed across administrations].

**Common cost-benefit vulnerabilities:**

| Issue                           | Argument                                                                                                                                                                           |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Underestimated compliance costs | Present industry-specific cost data; challenge agency's per-unit assumptions; demonstrate hidden or indirect costs                                                                 |
| Overestimated benefits          | Challenge the discount rate chosen for future benefits; challenge the dose-response or risk models underlying health/safety benefits                                               |
| Wrong discount rate             | OMB Circular A-4 (2023) recommends 2% for intergenerational rules; challenge if agency used a rate that systematically inflates or deflates benefits [VERIFY current OMB guidance] |
| Failure to analyze alternatives | Agency must assess regulatory alternatives, including less restrictive approaches — document the alternatives not considered                                                       |
| Distributional analysis absent  | For major rules, failure to analyze distributional impacts (who pays, who benefits) is increasingly required and challenged                                                        |
| Sensitivity analysis            | Demand sensitivity analysis on key uncertain parameters — agency's preferred scenario should not be the only one modeled                                                           |

---

### Scientific Evidence Arguments

**Framework for challenging the scientific basis of a rule:**

1. **Peer review adequacy**: Was the underlying research peer-reviewed? What was the
   quality of peer review (journal tier, replication, data sharing)?

2. **Data accessibility**: Has the agency made the underlying data publicly available?
   Reproducibility requirements (OMB guidelines) require agencies to use publicly
   accessible data where feasible [VERIFY current requirements].

3. **Methodological consistency**: Has the agency applied its stated methodology
   consistently? Are there arbitrary deviations from prior agency methodologies that
   benefit the regulatory outcome?

4. **Contrary literature**: Are there peer-reviewed studies in the scientific literature
   that contradict the agency's findings? The agency must respond to significant scientific
   objections.

5. **Uncertainty quantification**: Has the agency adequately represented the uncertainty
   in its scientific findings? Presenting a point estimate as settled when it has wide
   confidence intervals is misleading and may be arbitrary.

**Submission protocol for scientific evidence:**

- Attach the full study as a PDF exhibit (not just a citation)
- Provide an expert summary explaining the study's relevance to the agency's analysis
- Explicitly state the argument: "The attached study [name] contradicts the agency's
  assumption that [X]. The agency must either explain why it disregards this evidence or
  modify the rule to account for it."

---

## Argument Tier Classification Reference

| Tier   | Name                            | Legal Weight                                 | If Successful                                       | If Agency Ignores                                       |
| ------ | ------------------------------- | -------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------- |
| TIER 1 | Statutory / Constitutional      | Highest — challenges agency authority to act | Rule vacated or remanded                            | Strong grounds for pre-enforcement review               |
| TIER 2 | Record / Arbitrary & Capricious | High — challenges agency's reasoning         | Rule vacated or remanded for additional proceedings | Strong grounds for § 706 review after rule takes effect |
| TIER 3 | Policy / Technical              | Lower — requests voluntary modification      | Agency adopts commenter's preferred approach        | No judicial remedy — persuasion is the only avenue      |

---

## Standing Documentation Framework

Complete this framework for any commenter likely to seek judicial review:

```
**Commenter Identification**: [Full legal name, address, organization type]

**Injury-in-Fact**:
- Direct economic injury: [$ amount or quantified burden, with methodology]
- Operational impact: [Specific operational changes required by the rule]
- Regulatory exposure: [New legal obligations the rule imposes]
- Concrete, particularized, and imminent: [Explain why harm is not speculative]

**Causation/Traceability**:
- The [specific provision of the proposed rule] directly requires [specific action]
- This requirement causes [specific harm] because [causal mechanism]

**Zone of Interest**:
- The [enabling statute] was enacted to [purpose]
- Commenter's injury — [type of harm] — falls within the zone of protected interests
  because [connection to statutory purpose]

**Redressability**:
- A court order vacating the rule would remedy the harm by [how relief removes the injury]

**For Organizational Commenters — Representational Standing**:
- At least one member with standing: [describe category of affected member without
  naming a specific individual if not yet identified]
- Interests germane to organizational purpose: [connection to organization's mission]
- Individual participation not required: [the claim and relief are systemic]
```

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise if any gate fails.

| Gate           | Rule                                                                                                                                                   | Fail Action                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute (U.S.C. section), case (party names + year), or established regulatory principle                            | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow standard US legal citation (Bluebook or equivalent) — statute: 5 U.S.C. § 553; case: Party v. Party, volume U.S. page (year)      | Fix format                                               |
| **Currency**   | Every cited statute checked for amendments; every case checked for subsequent history (overruled, distinguished)                                       | Flag "[CHECK CURRENCY — verify current text]"            |
| **Domain**     | Analysis stays within US federal administrative law; do not import state APA concepts or non-APA procedures                                            | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty stated explicitly — developing areas of doctrine (nondelegation, Loper Bright implications in specific circuits) are not stated as settled | Add confidence qualifier                                 |

### Self-Interrogation for TIER 1 Arguments

For any TIER 1 argument included in the comment, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**:

- Does the statutory authority challenge follow logically from the cited authority?
- Would a reviewing court actually find this argument persuasive given the current circuit precedent?
- What is the agency's strongest response to this argument?

**Pass 2 — Completeness**:

- Have all relevant enabling statutes been analyzed?
- Have companion statutes (other provisions of the same Act, related Acts) been considered?
- Has the major questions doctrine analysis accounted for both prongs of the test?

**Pass 3 — Challenge**:

- What is the strongest argument that the agency does have statutory authority here?
- Under what circumstances might a reviewing court uphold the rule on statutory authority grounds?
- Is the TIER 1 classification proportionate, or is this a difficult question where TIER 2 is the stronger vehicle?

Mark the audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                                                            | Action                                                  |
| ------------ | --------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled authority, enacted statutory text, Supreme Court holding                   | State with confidence                                   |
| **High**     | 0.80-0.94 | Circuit court consensus, strong statutory basis, ACUS guidance                     | State with brief caveat                                 |
| **Probable** | 0.60-0.79 | Emerging doctrine, developing circuit split, agency practice                       | State with explicit reasoning and contra-indicators     |
| **Possible** | 0.40-0.59 | Genuinely unsettled area, conflicting circuits, evolving Loper Bright implications | Flag for counsel review with both sides of the argument |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative, doctrine explicitly rejected in circuit                   | Do not assert; flag "[UNCERTAIN — counsel to advise]"   |

---

## Glass Box Audit Trail

Every output MUST include this audit trail appended to the delivery:

```yaml
glass_box:
  skill_name: "legalcode-us-federal-regulatory-comment"
  jurisdiction: "US Federal"
  nprm_docket: "[Docket ID from regulations.gov or 'Not provided']"
  agency: "[Agency acronym and name]"
  commenter_type: "[Trade association / Corporation / NGO / Individual / Coalition]"
  primary_purpose: "[Persuade / Record-preservation / Both / Procedural objection]"
  tier1_arguments: "[number] — [list argument names]"
  tier2_arguments: "[number] — [list argument names]"
  tier3_arguments: "[number] — [list argument names]"
  major_questions_invoked: "Yes / No"
  loper_bright_invoked: "Yes / No"
  cra_analysis: "Yes / No / Not applicable"
  standing_documented: "Yes / No / Not applicable"
  attachments_identified: "[number] — [list attachment descriptions]"
  legalcode_mcp: "Connected / Not connected"
  statutes_cited:
    - "[5 U.S.C. § 553 — VERIFIED / UNVERIFIED]"
    - "[5 U.S.C. § 706 — VERIFIED / UNVERIFIED]"
  cases_cited:
    - "[West Virginia v. EPA, 597 U.S. 697 (2022) — VERIFIED / UNVERIFIED]"
    - "[Loper Bright Enterprises v. Raimondo (2024) — VERIFIED citation pending]"
    - "[Motor Vehicle Mfrs. Ass'n v. State Farm, 463 U.S. 29 (1983) — VERIFIED / UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no TIER 1 arguments)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "All case citations require verification against authoritative legal databases"
    - "Post-Loper Bright circuit-level implications are developing — verify in relevant circuit"
    - "EO and OMB analytical requirements subject to change across administrations"
    - "[Any commenter-specific scope limitations]"
  reviewer: "AI-assisted — requires qualified administrative law attorney review"
```

---

## Anti-Patterns

What NOT to do when drafting federal regulatory comments:

1. **Filing a form letter** — Mass form comments submitted through advocacy campaigns carry
   minimal weight with agencies and courts. Agencies do not count votes — they respond to
   substantive analysis. A single well-reasoned technical comment outweighs 10,000 identical
   form submissions.

2. **Conclusory legal arguments** — "The rule is arbitrary and capricious" is a legal conclusion,
   not an argument. Always provide the specific factual predicate: which data the agency
   ignored, which alternative it failed to consider, which assumption contradicts the evidence.

3. **Ignoring record preservation for litigation purposes** — If there is any chance the
   commenter will challenge the rule in court, all material arguments must be in the
   administrative record. Arguments not raised during the comment period are generally
   waived for purposes of judicial review. Never assume you can raise arguments later.

4. **Relying on hyperlinks for critical evidence** — Links break, content changes, and the
   administrative record captures what was actually submitted. Attach every document central
   to the comment as a PDF exhibit. Do not rely on a hyperlink to a study as a substitute
   for attaching the study.

5. **Conceding statutory ambiguity post-Loper Bright** — Under Chevron, conceding ambiguity
   triggered deference to the agency's interpretation. Post-Loper Bright (2024), there is no
   deference benefit from conceding ambiguity. Always argue for the best reading of the
   statute, not merely a permissible alternative.

6. **Invoking major questions doctrine for non-major issues** — Reserving the major questions
   doctrine for rules of genuinely vast economic and political significance. Crying "major
   questions" at every rule dilutes the argument and undermines credibility.

7. **Vague standing documentation** — "Our members will be harmed" is not sufficient for
   Article III standing. Document specific, concrete, and imminent injuries tied to specific
   rule provisions. Vague harm descriptions will fail in court.

8. **Ignoring agency's preamble** — The preamble is the agency's reasoning. Arbitrary and
   capricious arguments must be grounded in specific preamble passages — what the agency
   said, where it made the logical leap, what it ignored. "The agency failed to consider X"
   requires citing the preamble to show it was actually absent, not just underweighted.

9. **No alternative proposed** — A comment that only opposes without offering an alternative
   leaves the agency nothing to adopt. An agency that fails to consider a reasonable
   alternative it was presented with faces stronger arbitrary and capricious exposure. Always
   propose a specific alternative with enough detail to implement.

10. **Missing the deadline** — Comments received after the close of the comment period are
    not required to be considered and will typically not be included in the administrative
    record. Track the deadline on regulations.gov and build in buffer time for submission.
    After submission, preserve the confirmation/receipt from regulations.gov.

11. **Treating the comment period as a public forum** — The comment period is not a survey.
    The agency decides the rule on the merits of the record. Political arguments without legal
    or evidentiary support carry little weight. Frame all arguments in terms of statutory
    authority, factual record, and reasoned decision-making.

12. **Ignoring prior agency comments in the same docket** — If an ANPRM preceded this NPRM,
    comments submitted in response to the ANPRM are part of the record. Reference relevant
    prior submissions. If the agency promised to address an issue in response to an ANPRM
    comment and failed to do so, that is itself an arbitrary and capricious argument.

13. **Forgetting CRA classification** — If the rule likely qualifies as "major" under the CRA
    but the agency has classified it as non-major, challenge the classification in the comment.
    An incorrect CRA classification affects the congressional review timeline and the agency's
    obligations.

14. **Underspecifying proposed alternatives** — An alternative framed only as "the agency
    should regulate less" is not actionable. Specify the exact alternative: the regulatory
    threshold, the compliance date, the exemption category, or the definitional change. The
    more specific the alternative, the more difficult it is for the agency to ignore.

15. **Filing without verifying the comment was received** — After submission via regulations.gov,
    confirm the comment has been assigned a comment ID and appears in the docket. Technical
    failures happen. Preserve the confirmation and the comment text with a date/time stamp.

16. **Assuming the agency will make legally required responses** — Agencies sometimes fail to
    respond to significant comments. If the final rule is published without a response to
    your significant comment, this is grounds for an arbitrary and capricious challenge.
    Track whether the final rule's preamble responds to the specific arguments you raised.

17. **Single-pass draft without adversarial review** — Before submission, stress-test the
    comment from the agency's perspective. How will the agency's attorneys respond to each
    argument? Address the likely responses preemptively.

---

## Writing Standards

Apply plain-language discipline and professional drafting standards to all comment text:

**For legal arguments:**

- Active voice: "The proposed rule exceeds the agency's statutory authority" not "It is
  argued that the statutory authority may not extend to this rule"
- Name the legal standard: cite the doctrine, case, or statute governing each argument
- Short paragraphs: one argument per paragraph
- Internal citations: cite preamble pages and FR citations for every factual claim about
  what the NPRM says
- Precision over hedging: "The agency has not considered [X]" not "It is possible that
  additional consideration of [X] might have been beneficial"

**For economic and technical arguments:**

- Lead with the specific finding that is disputed
- Quantify wherever possible: "$X in annual compliance costs the agency did not include"
- Explain significance: why does this number matter to the analysis?
- Connect to legal standard: how does this factual error make the rule arbitrary and capricious?

**For the comment as a whole:**

- Executive summary at the top (agency officials read many submissions)
- Clear section headings that signal the argument
- Numbered paragraphs (facilitates agency preamble cross-reference responses)
- Attachments clearly labeled and incorporated by reference in the text

**Quality gates before submission:**

1. Would the agency's general counsel immediately understand the legal argument being made?
2. Is every factual claim grounded in a specific, accessible source in the record?
3. Is every proposed alternative specific enough that the agency could adopt it verbatim?
4. Are all [VERIFY] tags resolved (confirmed against authoritative sources)?
5. Does the comment include everything needed for judicial review if the rule proceeds unchanged?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for enabling statute text, recent amendments, and agency interpretation history
- Retrieve relevant circuit court opinions on the agency's rulemaking authority
- Search for prior Federal Register notices in the same rulemaking docket
- Verify case citations (party names, reporters, holdings, subsequent history)
- Search for ACUS recommendations relevant to the agency's procedural compliance
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law citations with [VERIFY]
- Instruct the commenter to verify against govinfo.gov (statutes), regulations.gov (dockets),
  and Westlaw/Lexis (case law) before filing
- Note in the Glass Box: `legalcode_mcp: "Not connected — all citations require verification"`
- Focus on comment structure, argument architecture, and record-preservation checklist
  rather than legal citation depth

---

## Output Format Template

Structure the delivered comment draft as follows:

```markdown
---
REGULATORY COMMENT DRAFT
Docket: [Docket ID]
Agency: [Agency Name]
Rule: [Rule Title and FR Citation]
Comment Period Closes: [Date]
Prepared For: [Commenter Name]
Prepared By: AI-assisted draft — requires attorney review before submission
Date: [Date]
---

## EXECUTIVE SUMMARY

[3-5 sentences: who is commenting, what the rule does, and the primary objections.
Designed to be read in under 60 seconds by a busy agency official.]

---

## I. INTRODUCTION AND INTEREST OF COMMENTER

[Who the commenter is, what they do, how many members/employees/facilities they represent,
and how this rule specifically affects them. This section also establishes standing for
any future judicial review.]

**Standing Documentation:**
[Complete standing elements per the Standing Documentation Framework above — injury, causation,
zone of interest, redressability.]

---

## II. SUMMARY OF COMMENTS

[Bullet list of each argument with its Tier classification and one-sentence description.
Roadmap for the agency's staff reading the full comment.]

| Tier   | Argument        | Requested Action |
| ------ | --------------- | ---------------- |
| TIER 1 | [Argument name] | [Specific ask]   |
| TIER 2 | [Argument name] | [Specific ask]   |
| TIER 3 | [Argument name] | [Specific ask]   |

---

## III. STATUTORY AUTHORITY ARGUMENTS [TIER 1]

### III.A. [Major Questions Doctrine / Statutory Interpretation Argument]

[Full argument using the Argument Block Format. Include:

- Statement of the legal standard (cite WV v. EPA, Loper Bright)
- Description of the rule's vast significance
- The specific statutory provision relied on by the agency
- Why that provision does not clearly authorize this rule
- Requested action: withdraw or substantially revise]

---

## IV. ARBITRARY AND CAPRICIOUS ARGUMENTS [TIER 2]

### IV.A. [Specific A&C Argument]

[Full argument using the Argument Block Format. Include:

- The specific failure mode (ignored data, unexplained reversal, etc.)
- Citation to the preamble passage that demonstrates the failure
- The specific evidence or analysis the agency failed to consider (attach as exhibit)
- Requested action: revise the record or provide adequate explanation]

---

## V. COST-BENEFIT ANALYSIS [TIER 2]

[Where applicable: specific critique of the agency's regulatory impact analysis.
Quantify discrepancies. Attach economic analysis as exhibit.]

---

## VI. SCIENTIFIC AND TECHNICAL BASIS [TIER 2]

[Where applicable: specific challenges to the scientific evidence underlying the rule.
Attach contradictory peer-reviewed studies as exhibits.]

---

## VII. PROPOSED ALTERNATIVES [TIER 3]

[Specific alternative regulatory approaches, with enough detail to implement.
Explain why each alternative better achieves the statute's purposes at lower cost or burden.]

---

## VIII. CONGRESSIONAL REVIEW ACT CONSIDERATIONS

[Where applicable: analysis of whether the rule is a "major rule" under the CRA,
and any concerns about agency overreach that Congress should address.]

---

## IX. CONCLUSION

[Summary paragraph: restate the primary asks, invite agency dialogue, note willingness
to provide additional information, and request that the agency respond to each argument
in the final rule's preamble.]

---

## ATTACHMENTS

| #   | Attachment | Description                                      |
| --- | ---------- | ------------------------------------------------ |
| A   | [Title]    | [Economic analysis / Study / Declaration / etc.] |
| B   | [Title]    | [Description]                                    |

[Note: All attachments incorporated by reference into this comment.]

---

[GLASS BOX AUDIT TRAIL — append per template above]
```

---

## Localization Notes

This skill is US federal only. The following topics are addressed differently at the
state level and require separate analysis:

| Topic                       | State-Level Difference                                                                                                                                                   |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| State APAs                  | Each state has its own administrative procedure act; the federal APA does not apply to state rulemaking                                                                  |
| Chevron/Loper Bright        | Many states have their own agency deference doctrines — some states have rejected Chevron-style deference independently of Loper Bright [VERIFY state-specific doctrine] |
| Standing                    | State courts may apply different standing requirements than Article III                                                                                                  |
| Comment period requirements | State notice-and-comment requirements vary; some are more demanding than 5 U.S.C. § 553                                                                                  |
| CRA equivalents             | Some states have legislative review mechanisms analogous to the CRA [VERIFY state-specific law]                                                                          |

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis for US federal administrative
law and notice-and-comment rulemaking strategy. Research sources include: 5 U.S.C. §§ 551–559,
701–706, 801–808; West Virginia v. EPA, 597 U.S. 697 (2022); Loper Bright Enterprises v.
Raimondo (2024); Motor Vehicle Mfrs. Ass'n v. State Farm, 463 U.S. 29 (1983);
Administrative Conference of the United States (ACUS) guidance on rulemaking and public
participation; Brookings Institution guidance on effective regulatory comments; OMB Circular A-4
(2023 revision); regulations.gov public access documentation; US GAO reports on federal
rulemaking; Yale Law Journal, "The Duty to Respond to Rulemaking Comments"; DLA Piper, ABA,
and Cleary Gottlieb analysis of Loper Bright implications (2024). Structural quality
frameworks adapted from legalcode-contract-review gold standard.

All citations marked [VERIFY] require confirmation against authoritative legal databases
before use in a filed comment.
