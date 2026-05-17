---
name: legalcode-statute-analysis
description: >
  Analyze statutes, acts, and regulations section by section — deconstruct structure,
  parse definitions, classify operative verbs, map exceptions and conditions, assess
  penalty tiers, determine authority boundaries, flag interpretive ambiguities, and
  identify implementation consequences. Use when a lawyer, compliance officer, policy
  analyst, or legal researcher needs to understand what a statute actually says and
  requires — as distinct from verifying that a citation is in-force (use
  legalcode-legislation-verification for that). Covers primary legislation, delegated
  legislation (statutory instruments, regulations, ordinances, executive orders, decrees),
  and secondary regulatory frameworks. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC]
  markers; supports common law and civil law systems. Triggers when the user provides
  statute text or a statutory reference and asks what it means, what it requires, who
  it applies to, what the penalties are, how it interacts with other law, or what
  they need to do to comply. Pairs with legalcode-legislation-verification (citation
  accuracy), legalcode-cross-border-checklist (multi-jurisdiction mapping), and
  legalcode-plain-language (readability rewriting).
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-6
context: fork
agent: general-purpose
---

# Legalcode Statute Analysis

> **Disclaimer**: This skill provides a framework for AI-assisted statutory analysis.
> It does not constitute legal advice. All outputs should be reviewed by a qualified
> legal professional licensed in the relevant jurisdiction before use. Statutory
> interpretation is inherently uncertain — courts regularly reach different conclusions
> from the same text. Statutory and case law references cited from memory carry
> hallucination risk; verify against authoritative sources before relying on them.
> This skill does not independently verify that cited provisions are currently in force —
> use `legalcode-legislation-verification` for citation currency checks.

## Purpose and Scope

This skill systematically deconstructs the text of statutes and regulations, producing
structured analysis that reveals what a provision says, what it requires, and what
it means to implement it.

**Covers:**
- Structural mapping (anatomy, hierarchy, part/section/schedule architecture)
- Definitions analysis (defined terms, inclusive vs. exhaustive, gaps, traps)
- Operative verb classification (mandatory, permissive, prohibitory, facultative)
- Exception and proviso architecture (exceptions vs. provisos vs. saving clauses vs. transitional provisions)
- Conditions and conditional logic (if/then, conjunctive/disjunctive, deeming provisions)
- Penalty and enforcement tiers (criminal vs. civil, strict liability vs. mens rea)
- Authority boundary analysis (ultra vires, delegated power scope, enabling vs. limiting)
- Interpretive issue flagging (ambiguities, gaps, conflicts with other law)
- Implementation consequence mapping (compliance obligations, deadlines, notification chains)

**Does not:**
- Verify that cited provisions are currently in force (use `legalcode-legislation-verification`)
- Map multi-jurisdiction compliance requirements across a transaction (use `legalcode-cross-border-checklist`)
- Rewrite statute text into plain language (use `legalcode-plain-language`)
- Draft compliance programmes or policies (use compliance-specific skills)
- Provide legal advice or replace qualified counsel

**Distinguishing statute analysis from contract review**: Contracts are negotiated; statutes are
imposed. Statutory analysis requires identifying not just what the text says but what courts will
likely say it means — and the tools for answering that question (purposive construction, legislative
history, comparative law) are themselves contested. This skill maps that interpretive landscape
alongside the text.

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. Every statute belongs to a specific legal system,
and that system determines how the statute is read, which interpretive tools are available,
and how courts resolve ambiguity. The skill adapts its analysis based on the jurisdiction
identified in Step 2.

[JURISDICTION-SPECIFIC] When localizing, research and apply:
- The applicable rules of statutory interpretation (common law literal/golden/mischief
  rules vs. civil law systematic/teleological interpretation vs. hybrid approaches)
- Legislative history tools available to courts (Hansard/Pepper v Hart in UK, travaux
  préparatoires in civil law, legislative history in the US)
- Administrative deference doctrines (Chevron/post-Loper Bright in US, Anisminic in UK,
  proportionality in EU/ECHR contexts)
- Constitutional limits on legislative power (parliamentary sovereignty in UK; federal
  division of powers in US, Australia, Canada, Germany; EU supremacy and proportionality)
- Local drafting conventions (UK parliamentary counsel style; US USC/CFR structure;
  EU regulation vs. directive vs. decision hierarchy; civil code article architecture)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- The interpretive approach differs materially by jurisdiction or system
- The user's purpose (compliance, litigation, policy, drafting) shapes what matters
- Scope decisions must be made (full analysis vs. targeted sections)

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

### Step 1: Accept the Statute

Accept the statute in any of these formats:
- **Full text**: The complete text of the statute or regulation pasted or uploaded
- **Specific sections**: One or more sections/articles identified by reference
- **Citation only**: A statutory citation (e.g., "s.14 Equality Act 2010", "42 U.S.C. § 1983",
  "Art. 17 GDPR") — in this case, note that the skill will work from the text as available
  in training data, which may not reflect amendments; recommend pairing with
  `legalcode-legislation-verification` first
- **Document upload**: A PDF or document file containing statute text

If no statute is provided, prompt the user to supply one.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning analysis, ask these questions. Skip any the user has already answered.

1. **Purpose of the analysis**:
   - Options: **Compliance mapping** (what must we do and by when), **Litigation / defence** (does the statute apply and was it breached), **Regulatory advice** (what does this require of regulated entities), **Policy analysis** (what was intended and what are the effects), **Legislative drafting** (how does this interact with what we are drafting), **Due diligence** (does this regime affect the target), **General understanding** (explain what this says)
   - *Why this matters*: Compliance mapping prioritizes obligations and deadlines; litigation analysis prioritizes the scope of duties and defences; policy analysis prioritizes legislative intent and purpose. The same text produces different priority outputs.

2. **Jurisdiction and legal system**:
   - Options: Identify the jurisdiction (e.g., England and Wales, US federal, EU, Australia, Germany, France, etc.) and the applicable legal system (common law / civil law / mixed)
   - *Why this matters*: Interpretive tools, authority hierarchy, and drafting conventions differ fundamentally across systems.

3. **Instrument type**:
   - Options: **Primary legislation** (Act of Parliament, federal statute, Loi, Gesetz), **Delegated/secondary legislation** (statutory instrument, regulation, ordinance, executive order, decree), **Supra-national instrument** (EU Regulation, EU Directive — if so, transposed or direct effect?), **Quasi-legislative instrument** (guidance with regulatory effect, industry standard incorporated by reference)
   - *Why this matters*: Delegated legislation must be authorised by primary legislation; if it exceeds the enabling power, it is ultra vires and void. Directives require transposition and may not be directly enforced against private parties.

4. **Scope of analysis**:
   - Options: **Full analysis** — complete section-by-section decomposition of the whole instrument, **Priority analysis** — focus on the operative provisions most relevant to the user's stated purpose (definitions, key obligations, penalties), **Targeted section analysis** — analyse only the sections the user specifies, **Interaction analysis** — focus on how this statute interacts with another named statute
   - *Why this matters*: A full analysis of a complex statute (Companies Act, Tax Code) may produce unwieldy output. Targeted scope is more actionable.

5. **Audience for the output**:
   - Options: **Internal legal team** (full technical analysis), **Business stakeholders** (plain-language summary alongside technical analysis), **Regulated entity compliance team** (obligation-focused with deadline mapping), **Counsel's brief / memo** (issue-spotting with authority references)
   - *Why this matters*: Shapes whether to produce the full technical analysis only or to include a plain-language layer alongside it.

6. **Known related statutes**:
   - Free text. Are there other statutes, regulations, or instruments this one interacts with that should be noted in the analysis?
   - *Why this matters*: Many statutory provisions only make sense in the context of enabling legislation, parent regulations, or amendment acts that must be read together.

Proceed with reasonable defaults if the user provides partial context. State assumptions explicitly (e.g., "I'm proceeding on the basis that this is English law — please correct me if wrong").

### Step 3: Classify and Map the Instrument

Before section-by-section analysis, build a structural map of the instrument as a whole.

**3a. Instrument Type Classification**

| Category | Description | Key Analytical Implication |
|----------|-------------|----------------------------|
| **Primary / Head Legislation** | Act, Statute, Code article | Interpreted according to jurisdiction's rules of statutory interpretation; courts can declare incompatible (EU/ECHR) but usually not void |
| **Delegated / Secondary Legislation** | SI, Regulation, Order, Decree, Ordinance | Must stay within the enabling power; ultra vires provisions void; courts can quash |
| **EU Regulation** | Directly applicable in EU member states | No transposition required; directly enforceable against all parties |
| **EU Directive** | Requires member-state transposition | Direct effect (vertical, not horizontal) if not transposed; Francovich liability |
| **Quasi-legislative / Regulatory Guidance** | Guidance, code of practice, industry standard incorporated by reference | Persuasive / admissible in enforcement; not technically law unless incorporated |

**3b. Structural Map**

Identify and list the major structural components:

| Component | Present? | Location | Description |
|-----------|----------|----------|-------------|
| Long/Short Title | | | |
| Preamble / Recitals | | | |
| Commencement Provisions | | | |
| Interpretation/Definitions Section | | | |
| Parts, Chapters, Sections | | | |
| Schedules / Annexures | | | |
| Penalty Provisions | | | |
| Enforcement Provisions | | | |
| Transitional Provisions | | | |
| Amendment/Repeal Provisions | | | |
| Enabling / Henry VIII Powers | | | |

**3c. Hierarchy Identification**

Map the regulatory hierarchy for this instrument:

```
Constitutional / Treaty level:       [e.g., EU Treaties, US Constitution, ECHR]
  ↓
Primary Legislation:                 [e.g., Parent Act, Enabling Act]
  ↓
Secondary / Delegated Legislation:   [e.g., This instrument, if secondary]
  ↓
Regulatory Rules / Guidance:        [e.g., Regulator's rules, codes of practice]
  ↓
Individual Decisions / Licences:    [e.g., Regulatory approvals, conditions]
```

Flag any provisions that appear to conflict with a higher level in the hierarchy — these
may be ultra vires, incompatible, or subject to displacement.

**3d. Commencement Analysis**

**⟁ CLARIFY** — If the commencement structure is complex (staged commencement, provisions
in force by order, some sections not yet commenced):
- Ask the user for the relevant reference date ("As of which date are you analysing this instrument?")
- Note any provisions that are not yet in force as of that date

Flag:
- Whether the whole instrument commenced on a single date or in stages
- Any sections where commencement orders are required and whether those orders have been made
- Any transitional provisions that affect whether the current text applies to historical facts

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** to build a working legal reference for this analysis.

**Research process:**

1. Identify the enabling legislation (for secondary legislation) and verify the vires.
2. Search for authoritative interpretive sources:
   - Key case law on the interpretation of this specific provision
   - Cases on the interpretive methodology applicable in this jurisdiction
   - Regulatory guidance or official explanatory notes
   - Academic commentary and treatise analysis where authoritative
3. Search for related legislation that interacts with or affects interpretation.
4. Save results to a local temporary reference file (e.g., `/tmp/legalcode-statute-analysis-reference.md`):

```markdown
# Legal Authority Reference — [Statute/Regulation Name]
## Jurisdiction: [Jurisdiction]
## Reference Date: [date]
## Analysis Purpose: [purpose from Step 2]

### Enabling Legislation (for secondary instruments)
- [Parent Act, section conferring power]
- [Scope of delegated power]

### Case Law on This Provision
- [Case name, citation, key holding, confidence level]

### Case Law on Interpretive Methodology
- [Case name, citation, relevant principle, confidence level]

### Regulatory / Administrative Guidance
- [Regulator, guidance title, relevance]

### Explanatory Notes / Travaux Préparatoires
- [Source, date, key points relevant to interpretation]

### Related Statutes
- [Statute, relevance, interaction type: amends / interacts / conflicts / replaces]
```

5. Use this reference file throughout the analysis. Mark citations sourced from
   legalcode-mcp as VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**
- Proceed with analysis from available training data
- Mark all statutory and case law references [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — all citations require independent verification"`
- Recommend the user cross-check key provisions and case law against an authoritative legal database

---

### Step 5: Definitions Analysis

The definitions section is the foundation of every statute. Errors here cascade throughout
the analysis. Analyse every defined term before analysing operative provisions.

**⟁ CLARIFY** — If the statute has an extensive definitions section (30+ terms) and the
user has specified a targeted analysis: ask whether to analyse all definitions or only
those relevant to the sections in scope.

**5a. Definition Classification**

For each defined term, classify it:

| Classification | Description | Legal Significance |
|----------------|-------------|-------------------|
| **Exhaustive definition** | "means X and nothing else" / "means A, B, or C" | Closed — anything not listed is excluded |
| **Inclusive definition** | "includes X" / "includes but is not limited to X" | Open — listed items plus other qualifying items |
| **Purposive definition** | Definition references the purpose or effect | Interpreted expansively to serve legislative purpose |
| **Cross-reference definition** | Defined by reference to another statute | Imports that statute's definition and amendments to it |
| **Deeming definition** | "X is deemed to be Y for purposes of this Act" | Legal fiction — X is treated as Y regardless of factual reality |
| **Exclusionary definition** | "does not include X" | Removes items that might otherwise qualify |
| **Temporal definition** | Applies only for a specified period or as of a specific date | Must track commencement and amendment dates |

**5b. Definition Quality Analysis**

For each definition:

1. **Scope**: Does the definition operate throughout the whole instrument, or only in specified sections?
2. **Consistency**: Is the same term used with the same meaning throughout? Flag any inconsistent usage.
3. **Gaps**: Are key terms used in operative provisions but left undefined? Flag as INTERPRETIVE RISK.
4. **Interaction**: Does this definition import the meaning from another statute? If so, does that statute's definition match the parent statute's apparent purpose?
5. **Temporal traps**: Has the definition been amended since the events in question? (Particularly important for litigation analysis.)
6. **Deeming effects**: Where a deeming definition applies, map the full scope of the legal fiction — what real-world facts does it override?

**5c. Definitions Register**

Produce a consolidated definitions register:

```
| Term | Definition | Type | Scope | Issues / Notes |
|------|-----------|------|-------|----------------|
| [term] | [quoted definition] | [Exhaustive / Inclusive / Deeming / etc.] | [Whole Act / Part X only] | [Any gaps, ambiguities, or interaction notes] |
```

---

### Step 6: Operative Provisions Analysis

Analyse each substantive section for its operative verb, conditions, subjects, objects,
exceptions, and consequences.

**6a. Operative Verb Classification**

The operative verb is the most legally significant word in any provision. Classify every
operative verb encountered:

| Verb / Form | Legal Effect | Classification |
|-------------|-------------|----------------|
| **shall** (common law statutory drafting) | Mandatory obligation | MANDATORY |
| **must** (modern drafting, preferred in UK since 2000) | Mandatory obligation | MANDATORY |
| **is required to** | Mandatory obligation | MANDATORY |
| **may** | Discretionary permission — the subject may, but need not, act | PERMISSIVE |
| **is entitled to** | Confers a right — the subject may exercise it or not | RIGHTS-CONFERRING |
| **shall not** / **must not** | Prohibition — acting is unlawful | PROHIBITORY |
| **may not** | Prohibition (modern equivalent of shall not) | PROHIBITORY |
| **is not to** / **is prohibited from** | Prohibition | PROHIBITORY |
| **is to** | Obligation — same as must/shall in modern drafting | MANDATORY |
| **will** (in some US/international instruments) | Either mandatory or predictive depending on context | AMBIGUOUS — flag for analysis |
| **should** | Directory (guidance), not mandatory | DIRECTORY — flag if appearing in apparently binding provisions |
| **may, with the consent of X** | Permission conditional on third-party consent | CONDITIONAL PERMISSION |

[JURISDICTION-SPECIFIC] Note:
- In some civil law systems, articles may not use explicit modal verbs; obligation flows from the article structure and position within the code rather than a modal verb. Apply the equivalent analysis to the grammatical subject and predicate.
- In EU law, "shall" in Regulations is always mandatory; in Directives it sets the minimum result to be achieved.

**6b. Conditional Logic Analysis**

Map the conditional structure of each operative provision:

**Simple condition**: "If [condition], then [obligation/right/prohibition]."
- Identify the condition precisely — what triggers or disapplies the obligation?
- Is the condition precedent (must occur before obligation arises) or condition subsequent (obligation arises and ceases if condition occurs)?

**Conjunctive conditions** (AND logic): ALL conditions must be met.
- Risk: Adding one more condition narrows the operative scope. Check whether courts would read conjunctive conditions strictly or interpret one as subsuming another.

**Disjunctive conditions** (OR logic): ANY one condition suffices.
- Risk: Either/or conditions are sometimes drafting errors. Check legislative history if the provision seems unexpectedly broad.

**Nested conditions**: Conditions within conditions.
- Map as a decision tree and verify each branch.

**Deeming provisions**: "Where X is deemed to be Y..."
- Deeming provisions create legal fictions that override factual reality. Identify:
  - What is being deemed
  - For what purpose(s) is the deeming effective
  - Whether the deeming is limited or unlimited in scope
  - Whether courts have interpreted the deeming narrowly (typical) or broadly

**6c. Exception Architecture**

Distinguish between structurally different types of exceptions — they have different
legal effects and allocation of the burden of proof:

| Type | Form | Effect | Burden |
|------|------|--------|--------|
| **Exception / Exclusion** | "Subject to X..." / "except that..." / "other than..." | Narrows the operative provision from its terms | User must rely on exception (generally) |
| **Proviso** | "Provided that..." | Qualifies or limits the main provision — creates a carveout | Dependent on wording; often on the party seeking to invoke |
| **Saving clause** | "Nothing in this Act shall affect..." / "This Act does not prejudice..." | Preserves existing rights, liabilities, or instruments that would otherwise be affected | No burden shift — it is declaratory |
| **Transitional provision** | "For acts or omissions before [date]..." | Determines which version of the law applies to historical facts | Depends on wording |
| **Non-derogation clause** | "This Act does not limit or affect rights under [other Act]..." | Prevents this Act from reducing rights under named legislation | Interpretive tool |

For each exception encountered:
1. Identify the type (above)
2. State what the exception removes from or adds to the operative provision's scope
3. Note which party bears the burden of relying on the exception
4. Flag if the exception is broad enough to swallow the rule

**6d. Section Analysis Register**

For each material section, produce a structured entry:

```
### Section [X] — [Short Title / Subject Matter]

**Text**: [Quoted or paraphrased text]
**Operative verb**: [verb] → [MANDATORY / PERMISSIVE / PROHIBITORY / RIGHTS-CONFERRING]
**Subject (who)**: [Who is bound or entitled]
**Object (what)**: [What must/may/must not be done]
**Conditions**: [Conditions that trigger or modify the obligation]
**Exceptions**: [Any exceptions, provisos, or saving clauses]
**Interaction**: [Cross-references to other sections or statutes]
**Interpretive issues**: [Ambiguities, gaps, or contested meanings]
**Confidence**: [Definite / High / Probable / Possible / Unlikely]
```

---

### Step 7: Penalty and Enforcement Analysis

Map the enforcement architecture. This is often the most practically consequential part
of statutory analysis — the difference between a strict liability offence and one requiring
intent can mean the difference between conviction and acquittal; between a civil penalty
and a regulatory warning.

**7a. Criminal Penalty Analysis**

For each criminal offence provision:

| Element | Description | Questions to Answer |
|---------|-------------|---------------------|
| **Actus reus** | The prohibited act, omission, or state of affairs | What physical conduct is prohibited? Is it conduct, result, or circumstance? |
| **Mens rea** | Mental element required | Strict liability (no mens rea), negligence, recklessness, knowledge, intention, specific intent? |
| **Mode of liability** | How can liability attach | Principal offender only, or vicarious / corporate liability? |
| **Defences** | Statutory defences available | Due diligence, reasonable precautions, innocent dissemination, regulatory approval |
| **Penalty tier** | Maximum penalty | Summary only / Triable either way / Indictable only [JURISDICTION-SPECIFIC] |
| **Penalty range** | Fine and/or custodial sentence | Unlimited fine? Fixed tariff? Regulatory vs. criminal fine? |
| **Enforcement authority** | Who can prosecute or enforce | Police, regulatory agency, private prosecution rights |
| **Limitation period** | Time limit for prosecution | [JURISDICTION-SPECIFIC] |

[JURISDICTION-SPECIFIC] Strict liability note:
- Common law systems: Strict liability (no mens rea) is exceptional and must be clearly imposed by statute or necessary implication. The court considers the subject matter and severity of the offence (Sweet v Parsley [1970] AC 132 [VERIFY]; Gammon v AG Hong Kong [1985] AC 1 [VERIFY]).
- Civil law systems: Culpability requirements are typically embedded in general code provisions; strict liability (responsabilité stricte / Gefährdungshaftung) is the exception and normally requires express provision.

**7b. Civil Penalty and Regulatory Enforcement Analysis**

For regulatory enforcement provisions (administrative fines, compliance orders, licence suspension):

| Element | Questions to Answer |
|---------|---------------------|
| **Standard of proof** | Balance of probabilities (civil) or beyond reasonable doubt (criminal)? |
| **Penalty structure** | Fixed penalty, percentage of turnover (e.g., GDPR 4%), tiered bands by severity |
| **Aggravating/mitigating factors** | Is there a published penalty matrix? Proportionality requirement? |
| **Escalation mechanism** | Can a civil penalty escalate to criminal prosecution on repeat? |
| **Daily/continuing penalties** | Do penalties accrue per day of non-compliance? |
| **Third-party rights** | Can affected parties bring private civil claims alongside regulatory action? |
| **Right to appeal** | Is there a statutory right of appeal, and to what body? |
| **Limitation periods** | Time limits for regulatory action |
| **Publication powers** | Can the regulator name and shame or publish findings? |

**7c. Penalty Register**

Produce a consolidated penalty register:

```
| Section | Offence/Breach | Type | Mens Rea | Maximum Penalty | Enforcement Authority |
|---------|---------------|------|----------|-----------------|----------------------|
```

---

### Step 8: Authority Boundary Analysis

Particularly important for secondary legislation and regulatory action. Map the scope
of the statutory power and identify any provisions that may exceed it.

**8a. Ultra Vires Analysis (for Secondary Legislation)**

1. **Identify the enabling provision**: Which section(s) of the parent Act confer power to make this instrument?
2. **Map the scope of the power**: Does the enabling provision:
   - Limit the subject matter (can only regulate X, not Y)?
   - Limit the territorial scope?
   - Require ministerial consent, parliamentary approval, or consultation before exercise?
   - Exclude certain kinds of provision (e.g., cannot create criminal liability without express Parliamentary authorisation)?
3. **Test each provision against the enabling power**:
   - Does this provision fall within the scope of the enabling section?
   - Does it fall within any general incidental powers?
   - Flag any provision as VIRES RISK where it appears to exceed the enabling power.

**8b. Henry VIII Powers**

Henry VIII powers allow secondary legislation to amend primary legislation. They are:
- Viewed with suspicion by courts and parliamentary scrutiny committees
- Strictly construed: the power must be express and will not be implied
- Subject to additional parliamentary scrutiny in some jurisdictions

Flag any Henry VIII power in the instrument and identify:
- What primary legislation can it amend?
- What limits (if any) are placed on the power?
- Has it been used? If so, what amendments have been made?

**8c. Regulatory Power Scope**

For regulatory authority provisions (powers to make directions, publish guidance, issue notices):
- What is the scope of the power — can the regulator bind regulated entities unilaterally?
- Is there a procedural requirement before exercise (consultation, notice, reasons)?
- Is the exercise of the power subject to judicial review / administrative appeal?
- Are there proportionality constraints [JURISDICTION-SPECIFIC: particularly in EU/ECHR jurisdictions]?

[JURISDICTION-SPECIFIC] Administrative deference:
- **US federal**: Post-Loper Bright Enterprises v Raimondo (2024) [VERIFY], courts no longer defer to agency interpretation of ambiguous statutes (overruling Chevron). Agencies must stay within the best interpretation of their enabling Act.
- **UK**: Courts apply judicial review principles; statutory interpretation is a matter for courts; agency guidance is persuasive but not binding on courts (R (UNISON) v Lord Chancellor [2017] UKSC 51 [VERIFY]).
- **EU**: Proportionality review of EU institutions' acts; subsidiarity review of member-state legislation implementing EU law.

---

### Step 9: Interpretive Issues and Conflicts

Surface ambiguities, gaps, and conflicts that create legal risk — the areas where
reasonable practitioners disagree and where courts may be called upon to resolve.

**9a. Ambiguity Taxonomy**

| Ambiguity Type | Description | Approach |
|----------------|-------------|----------|
| **Semantic ambiguity** | A word has two or more distinct meanings | Purposive construction: which meaning best serves the statute's purpose? Dictionary definitions as starting point; technical vs. ordinary meaning |
| **Syntactic ambiguity** | The grammar of the provision admits two or more readings | Apply the interpretation that avoids absurd or unjust results; consider punctuation (read restrictively) |
| **Referential ambiguity** | A pronoun or descriptor is unclear — who or what does "it" or "such" refer to? | Read the provision as a whole; apply the nearest antecedent rule unless it produces absurdity |
| **Elliptical ambiguity** | Something has been omitted from the text | Courts generally cannot fill gaps that represent deliberate omissions; may fill clearly accidental omissions (purposive construction) |
| **Definitional gap** | Key term used without definition | Courts will assign ordinary meaning; technical terms get technical meaning; some jurisdictions allow recourse to legislative history |
| **Conflict ambiguity** | Two provisions of the same statute appear to contradict | Later provision usually prevails (within same statute); specific provision prevails over general; courts prefer reading that gives both provisions meaning |

**9b. Conflict with Other Law**

For each significant provision, check for conflicts with:

| Conflict Type | Description | Resolution Principle |
|---------------|-------------|---------------------|
| **Intra-statute conflict** | Two sections of the same statute contradict | Specific overrides general; later overrides earlier (within the instrument) |
| **Inter-statute conflict (same level)** | Two statutes of the same rank conflict | Later Act impliedly repeals inconsistent earlier provisions (but only pro tanto); courts prefer constructions that avoid implied repeal |
| **Constitutional / superior law conflict** | Provision conflicts with constitution, treaty, or superior legislation | Superior law prevails; provision may be void or severable |
| **EU/ECHR incompatibility** | Provision conflicts with EU law (EU member states) or ECHR | EU law supremacy; ECHR incompatibility declarations do not automatically void [JURISDICTION-SPECIFIC] |
| **Regulatory conflict** | Two regulatory regimes impose conflicting requirements | Identify which regime is lex specialis; seek regulatory guidance; flag for counsel review |

**9c. Legislative Intent Tools**

Map the available tools for resolving ambiguity in the applicable jurisdiction:

| Tool | Availability |
|------|-------------|
| **Explanatory Notes / Memoranda** | [JURISDICTION-SPECIFIC] — Available in UK, Australia; less so in civil law; officially non-binding but frequently used |
| **Legislative history / Hansard** | [JURISDICTION-SPECIFIC] — UK: Pepper v Hart [1993] AC 593 [VERIFY] (limited); US: Congressional Record widely used; civil law: travaux préparatoires available but weight varies |
| **Purpose / Long Title** | Generally available; courts use long title to identify statutory purpose |
| **Preamble / Recitals** | [JURISDICTION-SPECIFIC] — EU instruments: Recitals used to interpret operative provisions; common law: preamble of limited weight if operative text is clear |
| **Related legislation in pari materia** | Generally available — other statutes dealing with the same subject matter inform interpretation |
| **International conventions** | [JURISDICTION-SPECIFIC] — Relevant if statute implements a treaty; courts may use treaty text and official commentaries |
| **Regulatory impact assessments** | Non-binding; may reflect legislative intention |

**9d. Interpretive Issue Register**

Produce a structured register of ambiguities and interpretive risks:

```
### Interpretive Issue [N] — [Short Description]

**Section(s)**: [X]
**Issue type**: [Semantic / Syntactic / Referential / Gap / Conflict]
**Description**: [What the ambiguity or conflict is]
**Competing interpretations**: [Interpretation A: ...; Interpretation B: ...]
**Current authority (if any)**: [Case or regulatory guidance, with confidence level]
**Preferred interpretation**: [Which interpretation is more likely to be adopted and why]
**Risk if wrong**: [INTERPRETIVE RISK — MATERIAL / MODERATE / LOW]
**Recommended action**: [Verify with counsel / Seek regulatory guidance / Monitor litigation / Other]
**Confidence**: [Definite / High / Probable / Possible / Unlikely]
```

---

### Step 10: Implementation Consequence Mapping

Translate the statutory analysis into actionable implementation consequences. This step
converts statutory text analysis into operational compliance intelligence.

**10a. Obligation Inventory**

Extract every positive obligation imposed by the statute on the regulated entity and
classify it:

| Category | Description |
|----------|-------------|
| **Absolute obligation** | Must be done regardless of circumstances or resources |
| **Reasonable efforts obligation** | Best endeavours / all reasonable steps — conduct-based |
| **Result obligation** | Must achieve a specified outcome; means are discretionary |
| **Notification obligation** | Must notify a person, authority, or the public |
| **Registration / licensing obligation** | Must register or obtain a licence before acting |
| **Record-keeping obligation** | Must create, maintain, or preserve specified records |
| **Reporting obligation** | Must file periodic or event-triggered reports |
| **Consultation obligation** | Must consult stakeholders before acting |

**10b. Deadline and Trigger Analysis**

For each obligation, identify:
- **Trigger event**: What starts the clock? (Commencement date, an event, a notification, a calculation)
- **Deadline**: Fixed date, relative period, or rolling obligation?
- **Grace period**: Is there a grace period before enforcement action is possible?
- **Extension mechanism**: Can the deadline be extended, and if so how?

Produce a compliance timeline:

```
| Obligation | Trigger | Deadline | Grace Period | Responsible Party | Notes |
|-----------|---------|----------|--------------|-------------------|-------|
```

**10c. Extraterritorial Effect**

**⟁ CLARIFY** — If the entity is not domiciled in the jurisdiction of the statute,
or the activity crosses borders, ask whether extraterritorial application is relevant.

Assess whether the statute:
- Has explicit extraterritorial reach (common in data protection, financial services, competition law)
- Applies to effects within the territory regardless of where the actor is located
- Contains a targeting test (directed at the jurisdiction's consumers / markets)
- Creates conflicts with other jurisdictions' mandatory laws

[JURISDICTION-SPECIFIC] Common extraterritorial regimes:
- **GDPR**: Applies to processing of EU residents' data regardless of processor location (Art. 3)
- **US securities regulation**: Effects/conduct tests for US nexus (Morrison v National Australia Bank 561 U.S. 247 (2010) [VERIFY])
- **UK Competition Act 1998**: Applies to agreements with effect in UK regardless of parties' location [VERIFY]

**10d. Third-Party Impact Analysis**

Identify obligations that flow down to or create rights for third parties:

| Third Party | How Affected | Rights Created | Obligations on Third Party |
|-------------|-------------|----------------|---------------------------|
| Sub-contractors | | | |
| End users / consumers | | | |
| Data subjects | | | |
| Regulatory bodies | | | |
| Other affected parties | | | |

---

### Step 11: Quality Verification

Before delivering the analysis, run the quality checks below.

**11a. Citation Quality Gates**

Run these 5 gates silently before delivering any output. If any gate fails, revise before delivering.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every legal claim about a provision cites the specific section and statute | Add citation or mark "[SECTION NOT CITED — verify]" |
| **Format** | All citations follow a consistent, recognisable format for the jurisdiction | Fix format |
| **Currency** | All provisions noted as in force have been checked for amendments | Flag "[CHECK CURRENCY — may have been amended]" |
| **Domain** | Analysis stays within the identified jurisdiction and legal system | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty is explicitly stated, not hidden | Add confidence qualifier |

**11b. Self-Interrogation for INTERPRETIVE RISK — MATERIAL Items**

For any provision classified as INTERPRETIVE RISK — MATERIAL, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the interpretive risk follow logically from the text and the identified ambiguity? Would a competent court or tribunal actually face this uncertainty on these facts, or is the ambiguity academic?

**Pass 2 — Completeness**: Have all relevant interpretive tools been considered? Is there regulatory guidance, case law, or legislative history that resolves the apparent ambiguity? If so, downgrade the risk.

**Pass 3 — Challenge**: What is the strongest argument that the provision is clear and unambiguous? Under what circumstances might a court or regulator decline to apply the uncertain interpretation? Is the risk rating proportionate?

Mark the Glass Box with `self_interrogation: PASS` or `self_interrogation: REVISED`.

**11c. Confidence Scoring**

Assign a confidence level to each material analytical finding:

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95–1.0 | Settled law, unambiguous text, authoritative case | State with confidence |
| **High** | 0.80–0.94 | Strong authority, minor interpretation questions | State with brief caveat |
| **Probable** | 0.60–0.79 | Good arguments, reasonable minds differ | State with explicit reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuinely uncertain, competing authorities | Flag for professional review with both sides |
| **Unlikely** | 0.0–0.39 | Weak basis, speculative, no supporting authority | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Severity Classification System

Use this three-tier system when classifying findings across the analysis:

### CLEAR — Provision is Unambiguous

The provision's meaning, application, and effect are settled by text, authority, or
regulatory guidance. Minor variation in drafting style does not affect the outcome.

**Indicators:**
- Definition is precise and consistent with other statutory usage
- Operative verb is unambiguous (must/shall with no proviso)
- Case law or regulatory guidance has settled the interpretation
- Drafting follows standard parliamentary counsel conventions

**Action**: State the meaning confidently. Note supporting authority.

### INTERPRETIVE RISK — Provision is Ambiguous or Contested

The provision admits more than one plausible reading, lacks authoritative interpretation,
or contains drafting that creates genuine legal uncertainty.

**Sub-tiers:**
- **MATERIAL**: The uncertain interpretation would substantially change compliance obligations, exposure, or rights. Seek legal advice before acting on either interpretation.
- **MODERATE**: The uncertainty exists but both readings lead to manageable outcomes. Note and monitor.
- **LOW**: Technical ambiguity that is unlikely to be litigated or create practical risk.

**Action**: Present both interpretations, assess which is more likely to be adopted, and
recommend professional review proportionate to materiality.

### ENFORCEMENT / VIRES RISK — Provision Creates Enforcement Exposure or Vires Problem

The provision imposes obligations with significant penalty exposure, or (for secondary
legislation) appears to exceed the enabling power.

**Sub-tiers:**
- **ENFORCEMENT RISK — CRITICAL**: Strict liability criminal offence, unlimited fine, or licence revocation exposure. Immediate legal advice required.
- **ENFORCEMENT RISK — HIGH**: Civil penalty with significant financial consequence, regulatory sanction, or reputational risk.
- **ENFORCEMENT RISK — MODERATE**: Civil penalty with limited exposure, compliance notice, or warning.
- **VIRES RISK**: Provision may exceed the enabling power and be ultra vires / void.

**Action**: Flag immediately. Provide the operative provision, penalty exposure, and
recommended immediate steps. Escalate CRITICAL and HIGH findings.

---

## Interpretive Methodologies Reference

This reference is drawn upon throughout the analysis. Adapt to the applicable jurisdiction.

### Common Law Jurisdictions

**Literal rule**: Give words their plain, ordinary, grammatical meaning.
- Starting point in most common law systems
- Can produce absurd results if applied mechanically

**Golden rule**: Adopt the literal meaning unless it produces an absurdity or repugnancy.
- Applies the literal meaning but permits modification to avoid clear absurdity
- More conservative than the purposive approach

**Mischief rule** (Heydon's Case (1584) [VERIFY]):
- What was the law before the Act?
- What mischief did the Act seek to cure?
- What remedy did Parliament provide?
- Courts interpret the Act to suppress the mischief and advance the remedy

**Purposive / Contextual approach** (dominant modern approach in UK, Australia, NZ, Canada):
- Read the provision in light of the statute's purpose as a whole
- Long title, preamble, explanatory notes, and policy objectives inform interpretation
- Wider than the mischief rule — not limited to the specific defect, but the whole purpose

**Pepper v Hart principle** (UK) [VERIFY]:
- Where the legislation is ambiguous or obscure, courts may consult Hansard (Parliamentary debates)
- Limited to ministerial or promoter statements that are clear and directly address the point

### Civil Law Jurisdictions

**Literal interpretation**: Start with the text
**Systematic interpretation**: Read within the broader code or legislation structure
**Historical / genetic interpretation**: Consult travaux préparatoires and legislative history
**Teleological / purposive interpretation**: Apply the law's purpose and social function
**Comparative interpretation**: Consider how other jurisdictions have approached the same issue

[JURISDICTION-SPECIFIC] EU law: The Court of Justice of the EU applies a predominantly
purposive and systematic approach. Recitals (preambles) are extensively used. The principle
of effet utile (effectiveness) requires interpretations that give the provision practical effect.

### Interpretive Presumptions (Common Law)

Courts presume, unless the contrary is clear:
- Statutes do not operate retrospectively (no retroactive application)
- Statutes do not bind the Crown without express words
- Statutes do not derogate from fundamental rights without express and unambiguous language
- The legislature does not intend to produce absurd results
- Parliament is presumed to know the existing law (continuity presumption)
- Every word has a purpose — surplusage is avoided

---

## Glass Box Audit Trail

Every statute analysis output MUST include a Glass Box audit section. This makes
the reasoning traceable and auditable.

```yaml
glass_box:
  skill_name: "legalcode-statute-analysis"
  statute: "[Name and citation of statute analysed]"
  instrument_type: "[Primary / Secondary / EU Regulation / EU Directive / Other]"
  jurisdiction: "[Jurisdiction identified in Step 2]"
  legal_system: "[Common law / Civil law / Mixed]"
  reference_date: "[Date as of which the statute was analysed]"
  analysis_purpose: "[Compliance / Litigation / Policy / Due diligence / etc.]"
  scope: "[Full / Priority / Targeted sections: X, Y, Z]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to /tmp file or 'Not created']"
  sections_analysed: "[number]"
  definitions_registered: "[number]"
  operative_provisions_classified: "[number]"
  penalty_provisions_mapped: "[number]"
  interpretive_issues_flagged: "[number]"
  enforcement_risk_items:
    - critical: "[number]"
    - high: "[number]"
    - moderate: "[number]"
  vires_risk_items: "[number or 'None identified']"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no MATERIAL interpretive risks)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
    - "[Commencement or amendment status not independently verified]"
    - "[Training data cutoff — provisions may have been amended since]"
  reviewer: "AI-assisted — requires qualified legal review before reliance"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in statutory analysis:

1. **Reading sections in isolation** — Every section of a statute must be read in context of the
   whole instrument. Definitions, saving clauses, and transitional provisions in other sections
   routinely modify what apparently clear operative provisions mean. Always read the definitions
   section and any general provisions before analysing operative sections.

2. **Treating headings as operative** — Section headings (and margin notes in older UK statutes)
   are guides to structure, not operative text. Headings cannot override or limit the plain meaning
   of the section text. Courts may refer to headings to resolve ambiguity but not to cut down clear
   language.

3. **Confusing "shall" and "may"** — In older drafting, "shall" was sometimes used for both
   mandatory obligations and permissive provisions (grammatical "shall"). Modern statutory drafting
   uses "must" for obligations and "may" for permissions, but older statutes may use "shall" for both.
   Always check context and, if in doubt, apply the purposive approach.

4. **Assuming "includes" is exhaustive** — An inclusive definition ("X includes A, B, and C") is
   NOT a closed list. Items not listed may still fall within the term's ordinary meaning. An exhaustive
   definition ("X means A, B, or C") is closed. Confusing these is a material analytical error.

5. **Ignoring deeming provisions** — Deeming provisions create legal fictions that override factual
   reality. Where a statute deems X to be Y, that deeming governs the legal analysis regardless of
   what is factually true. Failing to trace all deeming provisions produces wrong answers.

6. **Conflating exceptions, provisos, and saving clauses** — These have different legal structures
   and different effects on burden of proof. An exception narrows the provision from its terms; a
   proviso qualifies it; a saving clause preserves something that would otherwise be affected.
   They are not interchangeable.

7. **Applying the literal rule mechanically** — The literal rule is the starting point, not the
   end point. Courts in all major common law jurisdictions now apply some form of purposive
   construction. Mechanically applying the literal reading without testing it against the statute's
   purpose can produce wrong results and wrong advice.

8. **Importing interpretive tools from the wrong jurisdiction** — Pepper v Hart allows resort to
   Hansard in UK law under specific conditions. US courts use Congressional Record with different
   rules. Travaux préparatoires are a civil law tool. Do not apply one jurisdiction's interpretive
   methodology to another's statute.

9. **Citing cases from memory without verification** — Case citations hallucinated by AI are
   a serious professional risk. Never present a case as authority without marking it [VERIFY] if
   it cannot be independently confirmed. This applies equally to the ratio (holding) of verified
   cases — mischaracterising a case's ratio is as dangerous as citing a fictitious case.

10. **Assuming that secondary legislation is valid** — Secondary legislation (statutory instruments,
    regulations, executive orders) must stay within the scope of its enabling power. Ultra vires
    provisions are void. Do not analyse secondary legislation without first identifying the enabling
    power and checking whether the instrument stays within it.

11. **Treating guidance as law** — Regulatory guidance, codes of practice, and administrative
    circulars are not law unless incorporated by reference in a binding instrument. They may be highly
    persuasive evidence of good faith in enforcement proceedings but cannot impose obligations beyond
    what the statute provides.

12. **Ignoring commencement** — Many statutes (and regulations) commence in stages or require
    commencement orders. Analysing a provision as if it is in force when it has not been commenced
    is a fundamental error. Always verify commencement before analysing any provision as currently
    operative.

13. **Overstating regulatory deference post-Loper Bright** — In the US, courts no longer defer to
    agencies' interpretations of ambiguous statutes (Loper Bright Enterprises v Raimondo (2024)
    [VERIFY], overruling Chevron). Analytical frameworks that assumed strong deference to agency
    interpretation of enabling statutes must be revised for post-2024 US federal law.

14. **Ignoring the interaction between criminal and civil enforcement** — Many regulatory regimes
    have both criminal offences and civil/administrative penalties for the same conduct. These often
    have different standards of proof, different enforcement authorities, and can run in parallel.
    Analysing only one regime is incomplete.

15. **Treating "reasonable" as determinative** — Provisions requiring "reasonable" conduct are
    notoriously fact-specific. The word reasonable delegates a judgment to the court or decision-maker
    that cannot be resolved by text analysis alone. Flag provisions using "reasonable" or "reasonably"
    as areas where conduct will be judged contextually, not by bright-line rules.

16. **Skipping the definitions section** — Failing to read every defined term before analysing
    operative provisions is the single most common statutory analysis error. Key terms often have
    statutory meanings that differ materially from their ordinary-language meanings. This cannot be
    discovered after the fact.

17. **Treating all obligations as self-executing** — Many statutory obligations require implementing
    regulations, ministerial orders, or formal decisions before they become operative. Identifying
    obligations that depend on further implementing measures is essential for accurate compliance
    advice.

18. **Conflating "may" with an obligation to act** — Where a public body "may" do something, that
    is a permission, not an obligation. Courts will not compel a public authority to exercise a
    permissive power unless it has misdirected itself or fettered its discretion. This is commonly
    misread by those accustomed to private-law "may" (which sometimes means "must" in context).

---

## Writing Standards

Apply plain-language discipline to all output:

**For the section analysis**:
- State what the provision says before stating what it means
- Attribute operative verbs precisely: "Section 14(1) imposes a mandatory obligation on [X] to..."
- Use active voice: "The Act prohibits..." not "It is prohibited by the Act..."
- Identify the actor, the act, and the consequence in each analysis
- Name the legal effect clearly: "This is a strict liability offence" not "this provision may have
  implications for liability"

**For interpretive issues**:
- State the competing interpretations before the preferred one
- Explain why the preferred interpretation is more likely without dismissing the alternative
- Use confidence qualifiers precisely: "probable" means something different from "possible"
- Cite authority (even if marked [VERIFY]) for every interpretive preference

**For implementation outputs**:
- State obligations in plain-language terms suitable for compliance teams
- Include deadlines with trigger events: "Within 30 days of [trigger event]..."
- Flag uncertainty where implementation requires further regulatory guidance

**Quality gates before delivery**:
1. Has every section that was analysed been included in the output registers?
2. Is every legal claim backed by a specific section reference or case citation (or flagged [VERIFY])?
3. Has the definitions register been checked against every defined term used in the operative provisions?
4. Are interpretive risks proportionately rated — not over-stated and not understated?
5. Can a compliance professional act on the implementation consequences section without further interpretation?

---

## External Tool Integration

This skill works with **legalcode-mcp** as its primary legal research tool for verified
statutory authority, case law, and regulatory guidance.

**With legalcode-mcp connected (preferred):**
- In Step 4, search for the statute's enabling legislation, key case law, and regulatory guidance
- Save verified authority to `/tmp/legalcode-statute-analysis-reference.md`
- Reference the verified authority file when classifying interpretive risks
- For ENFORCEMENT RISK — CRITICAL items, search for additional enforcement precedents
- Check commencement status and amendment history
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**
- Proceed with analysis using training data
- Mark all case law and statutory cross-references [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — all citations require independent verification"`
- Recommend the user verify commencement status, amendment history, and key case law independently
- The analysis remains structurally complete but legal authority confidence is reduced

---

## Output Format Template

Structure the final deliverable as follows. Adjust sections based on the scope of analysis
agreed in Step 2.

```markdown
## Statute Analysis

**Instrument**: [Full name, citation, and jurisdiction]
**Instrument type**: [Primary / Secondary / EU Regulation / etc.]
**Jurisdiction and legal system**: [Jurisdiction, Common law / Civil law]
**Reference date**: [Date of analysis]
**Analysis purpose**: [From Step 2]
**Scope**: [Full / Priority / Targeted sections]
**Date of analysis**: [date]

---

## Executive Summary

[3–5 bullets covering: what the statute does, who it applies to, key obligations,
highest-priority findings (ENFORCEMENT RISK — CRITICAL / MATERIAL INTERPRETIVE RISK),
recommended immediate actions]

---

## Structural Map

[Table from Step 3b: components, locations, descriptions]

**Regulatory Hierarchy:**
[Hierarchy diagram from Step 3c]

**Commencement:** [Summary from Step 3d]

---

## Definitions Register

[Table from Step 5c: terms, definitions, types, scope, issues]

---

## Operative Provisions Analysis

[Section Analysis Register entries from Step 6d, organised by part/section]

---

## Penalty and Enforcement Register

[Penalty Register table from Step 7c]

**Criminal offence analysis**: [Step 7a findings]
**Civil/regulatory enforcement**: [Step 7b findings]

---

## Authority Boundary Analysis

[Step 8 findings: ultra vires analysis, Henry VIII powers, regulatory power scope]

---

## Interpretive Issues Register

[Register entries from Step 9d, classified by severity]

---

## Implementation Consequences

**Obligation Inventory**: [Table from Step 10a]
**Compliance Timeline**: [Table from Step 10b]
**Extraterritorial Effect**: [Step 10c findings]
**Third-Party Impact**: [Table from Step 10d]

---

## Recommended Next Steps

[Specific actions, owners, and deadlines. Distinguish:
- Immediate (ENFORCEMENT RISK — CRITICAL)
- Near-term (INTERPRETIVE RISK — MATERIAL requiring professional advice)
- Background (ongoing compliance obligations, monitoring requirements)]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

This skill is jurisdiction-agnostic. [JURISDICTION-SPECIFIC] markers throughout indicate
where local counsel review is mandatory. To create a jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with verified jurisdiction-specific content
2. Embed the applicable rules of statutory interpretation (e.g., apply Pepper v Hart
   for England and Wales; Loper Bright framework for US federal; purposive CJEU
   methodology for EU instruments)
3. Replace [VERIFY] tags with verified statutory references from authoritative sources
4. Add jurisdiction-specific drafting convention notes (parliamentary counsel style,
   US CFR structure, EU legislative format, civil code article structure)
5. Update penalty analysis with jurisdiction-specific sentencing frameworks and
   regulatory fine structures
6. Add jurisdiction-specific interpretive presumptions and rules
7. Update the frontmatter name and description to reference the jurisdiction

**Jurisdictions with notable statute analysis requirements:**

**England and Wales**: Parliamentary Sovereignty; purposive construction; Pepper v Hart
Hansard access [VERIFY]; REUL/Assimilated Law post-Brexit transition. Check Legislation.gov.uk
for current text and commencement status. Explanatory Notes are authoritative on purpose.

**EU**: Recitals extensively used; effet utile principle; proportionality review;
Directive vs. Regulation distinction (direct effect, horizontal vs. vertical); supremacy
doctrine; CJEU preliminary references for authoritative interpretation.

**US federal**: Post-Chevron deference landscape (Loper Bright [VERIFY]); major questions
doctrine (West Virginia v EPA [VERIFY]); nondelegation doctrine revival; textualist vs.
purposivist circuit splits; use of legislative history contested.

**Australia**: Purposive construction (Acts Interpretation Act 1901 s.15AA [VERIFY]);
use of extrinsic materials (s.15AB [VERIFY]); constitutional division of powers
(Commonwealth / States); delegated legislation under relevant Acts.

**Germany**: Systematic interpretation within the BGB/HGB/specific code framework;
teleological interpretation; Bundesverfassungsgericht constitutional review; EU-conform
interpretation.

---

## Provenance

Created by Legalcode (2026-03-22). Legalcode original synthesis. Designed as a native
replacement for imported statute-analysis content and as a foundation for legal research
workflows. Based on:
- 2-agent research pipeline (structural analysis + prompt engineering pattern extraction)
- Deep analysis of `legalcode-contract-review` reference standard (Gold Standard)
- Pattern extraction from `legalcode-legislation-verification`, `legalcode-precedent-analyzer`,
  `legalcode-plain-language`, and `legalcode-cross-border-checklist`
- Statutory interpretation methodology: Heydon's Case, Pepper v Hart, purposive construction
  principles, post-Loper Bright US framework, EU interpretive methodology
- Legislative drafting conventions: UK Parliamentary Counsel, US Office of Legislative Counsel,
  Australian Parliamentary Counsel
- Quality frameworks: 18-element Legalcode completeness standard, 5 Citation Quality Gates,
  3-pass Self-Interrogation, 5-level Confidence Scoring, Glass Box audit trail
