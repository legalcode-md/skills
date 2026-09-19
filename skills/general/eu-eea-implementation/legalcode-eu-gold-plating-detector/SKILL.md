---
name: legalcode-eu-gold-plating-detector
description: Detects "gold-plating" in a Member State's National Implementing Measure (NIM) for an EU
  directive — that is, situations where the national text imposes additional scope, requirements, sanctions,
  or deadlines beyond the EU minimum, fails to use available derogations or opt-outs, or omits review
  and sunset clauses included in the directive.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Detects "gold-plating" in a Member State's National Implementing Measure (NIM) for an EU directive — that is, situations where the national text imposes additional scope, requirements, sanctions, or deadlines beyond the EU minimum, fails to use available derogations or opt-outs, or omits review and sunset clauses included in the directive. Operates on the published five-category taxonomy from the Commission High Level Group on Administrative Burden (HLG, 2014 conclusions and recommendations on gold-plating) and from the UK BIS Gold-Plating Review (2013). Anchors burden quantification on the German Nationaler Normenkontrollrat (NKR) cost-opinion methodology and the Standard Cost Model (SCM). Cross-references the Austrian Anti-Gold-Plating-Gesetz 2019 (BGBl. I Nr. 46/2019) and the French projet de loi portant suppression de sur-transpositions de directives européennes en droit français (2019) as concrete national anti-gold-plating instruments. Designed to operate on a directive + Member State pair using upstream artefacts from sibling skills: obligation register from `legalcode-eu-directive-analyzer`, per-MS NIM citations from `legalcode-eu-transposition-tracker`, the directive↔NIM correlation table from `legalcode-eu-correlation-table-builder`, and the per-provision conformity verdicts from `legalcode-eu-conformity-assessment`. Concrete worked examples drawn from CSRD (Directive (EU) 2022/2464, CELEX 32022L2464), MiFID II (Directive 2014/65/EU, CELEX 32014L0065 — see CFA Society Poland gold-plating in EU Capital Markets, 2024), AIFMD (Directive 2011/61/EU, CELEX 32011L0061), Prospectus Regulation contrast, NIS2 (Directive (EU) 2022/2555, CELEX 32022L2555), and CSDDD (Directive (EU) 2024/1760, CELEX 32024L1760). Operates under Art. 288 TFEU (directive obligation as to result) read with the Better Regulation Toolbox 2023 Tool #28 (proportionality and subsidiarity). Serves four operating personas — government cost-cleanup self-review, legal firm advising clients on multi-MS divergence, company quantifying compliance burden, and trade federation building policy-engagement positions. Produces a gold-plating findings table, JSON schema output, AKN4EU stub, LegalRuleML stub, and Glass Box audit trail. EU/EEA scope: EU-27 plus Iceland, Norway, and Liechtenstein where the act has been incorporated by EEA Joint Committee Decision (Art. 7, 102 EEA). Switzerland is excluded.


# Legalcode EU Gold-Plating Detector

> **Disclaimer**: This skill provides a framework for AI-assisted detection of
> gold-plating in Member State transposition of EU directives. It does not constitute
> legal advice and does not create an attorney-client relationship. All outputs should
> be reviewed by qualified legal counsel licensed in the relevant jurisdictions before
> use. This skill does not replace formal legal review by qualified EU and Member
> State counsel. It produces a structured framework to support a human-led review —
> not a substitute for one.
> Citations to EU directives, regulations, CJEU/EFTA Court judgments, and Member State
> implementing measures must be verified against authoritative sources (EUR-Lex, CURIA,
> national official journals) before use in regulatory submissions, infringement
> proceedings, or board reporting. EU law evolves continuously; transposition status,
> infringement procedures, and consolidated text versions change frequently. The 24
> official EU language versions of every act are equally authentic; reconcile divergent
> versions before relying on any single language for a definitive interpretation
> (CILFIT C-283/81; Codan C-236/97; EMU Tabac C-296/95).

## Purpose and Scope

This skill flags where a Member State's NIM for a specified EU directive imposes
requirements **beyond** what the directive requires, and classifies each finding into
the five-category gold-plating taxonomy used by the Commission HLG (2014) and adopted
by national better-regulation bodies. It then attempts to **quantify the burden** of
each finding using the NKR cost-opinion / Standard Cost Model approach, and recommends
remediation in line with the Better Regulation Toolbox 2023 Tool #28 proportionality
test.

Gold-plating is not the same as non-conformity. A non-conformity finding (skill E)
says "the NIM does not transpose Article X of the directive correctly." A gold-plating
finding says "the NIM transposes Article X **and** adds something the directive does
not require." Many provisions of an NIM are simultaneously conformant (no infringement
risk under Art. 258 TFEU) and gold-plated (excess burden by reference to the EU
minimum). The two analyses run on the same correlation table but answer different
questions and serve different audiences:

- A conformity assessment (skill E) is consumed by the Commission DG legal service or
  the EFTA Surveillance Authority Internal Market unit; it speaks to enforcement risk.
- A gold-plating assessment (this skill) is consumed by national budget offices, trade
  federations, and management boards; it speaks to competitiveness, cost, and the
  question of whether a national legislator has stretched discretion further than
  political circumstances justified.

Under Art. 288 TFEU a directive binds Member States "as to the result to be achieved"
but leaves "to the national authorities the choice of form and methods." That choice
is constrained by general principles of EU law — proportionality, equal treatment,
non-discrimination — but is otherwise wide. Gold-plating is therefore generally
**lawful**: it is a domestic policy choice, not a breach of EU law (with narrow
exceptions where the directive sets a maximum harmonisation ceiling, e.g. several
provisions of MiFID II Title II governing the passport, or where it expressly
prohibits stricter rules). The point of the analysis is therefore not to allege
illegality but to surface the **policy and economic** consequences of the choice.

**Covers:**

- Per-provision gold-plating test against the EU minimum, applying the five-category
  taxonomy below
- Burden quantification using NKR / Standard Cost Model methodology where data permit
- Cross-Member-State comparison (sister-MS benchmarking) using the implementation
  matrix from `legalcode-eu-transposition-tracker`
- Subsidiarity / proportionality test per Better Regulation Toolbox 2023 Tool #28
- Distinction between gold-plating proper and use of explicit MS options or
  derogations
- EEA pillar treatment (IS / NO / LI gold-plating in JCD-incorporated acts; ESA
  monitoring posture under Art. 31 SCA)
- Remediation recommendations for each finding (revoke, narrow scope, add review
  clause, time-limit the gold-plate)
- Output in Markdown, JSON, AKN4EU, and LegalRuleML, with Glass Box audit trail

**Does not:**

- Run the conformity assessment itself (use `legalcode-eu-conformity-assessment` first)
- Build the directive↔NIM correlation table (use
  `legalcode-eu-correlation-table-builder`)
- Track infringement procedures arising from non-transposition
  (use `legalcode-eu-infringement-procedure-tracker`)
- Track EEA incorporation status (use `legalcode-eea-incorporation-tracker`)
- Produce stand-alone economic impact assessments that are not anchored to the
  directive's text — those are policy work, not transposition analysis
- Provide legal advice or substitute for qualified EU and MS counsel

### Sibling Skills in the Suite

This skill is part of the seven-skill EU Legislative Compliance suite. It consumes /
produces the following artefacts:

- **Consumes**:
  - Obligation register from `legalcode-eu-directive-analyzer`, with the `ms_option`
    flag identifying provisions that the directive expressly leaves to MS discretion
    (those provisions can never be classified as gold-plating category 1, 2, or 3 —
    they may only be evaluated under category 4, "failure to use available
    derogations / opt-outs," when the MS exercised the option in a maximalist
    direction)
  - Per-MS NIM citations and ELI links from `legalcode-eu-transposition-tracker`
  - Two-column directive↔NIM correlation table from
    `legalcode-eu-correlation-table-builder` (Commission format)
  - Per-provision conformity verdicts and over-coverage rows from
    `legalcode-eu-conformity-assessment` (over-coverage rows are the natural input set
    for gold-plating classification)
- **Produces**: gold-plating findings (Markdown, JSON, AKN4EU, LegalRuleML, Glass
  Box) consumed by:
  - Government persona — as the cleanup target for a national sur-transposition
    review (cf. France 2019, Austria 2019)
  - Legal firm persona — as the basis for client cross-MS divergence advisories
  - Company persona — as the operational-adjustment target list per Member State of
    establishment
  - Trade federation persona — as the policy-engagement target list, anchoring
    advocacy in published HLG categories rather than in subjective "the rules are
    too tough" complaint

Sibling skills (use whichever is appropriate for the user's stage in the lifecycle):

- `legalcode-eu-directive-analyzer` — extracts the obligation register from a directive
- `legalcode-eu-transposition-tracker` — per-MS implementation matrix
- `legalcode-eu-correlation-table-builder` — directive-to-NIM correlation table
- `legalcode-eu-conformity-assessment` — per-article transposition verdict
- `legalcode-eu-gold-plating-detector` — flags national over-implementation (this skill)
- `legalcode-eea-incorporation-tracker` — EEA Joint Committee Decision tracking
- `legalcode-eu-infringement-procedure-tracker` — TFEU 258/260 procedure timeline

See the [shared EU legislative-data pack](references/eu-legislative-data/)
for cross-skill reference data (CELEX/ELI/ECLI conventions, EUR-Lex SPARQL endpoints,
language reconciliation rules, Better Regulation Toolbox cross-walks, and the curated
list of named gold-plating examples drawn from the literature).

---

## Jurisdiction and Governing Law

This skill applies to all EU-27 Member States. The taxonomy and burden methodology
work identically across MS, but several jurisdictions have **statutory anti-gold-
plating regimes** of their own that bear on the remediation phase and must be
identified before recommendations are drafted.

[JURISDICTION-SPECIFIC: Austria] _Anti-Gold-Plating-Gesetz 2019_ (BGBl. I Nr. 46/2019)
amends multiple substantive statutes specifically to remove provisions identified as
gold-plating during the 2018 federal review. The methodological lesson is that
Austria treats gold-plating cleanup as a horizontal legislative exercise, bundling
amendments across many subject-matter statutes into a single anti-gold-plating
omnibus. Cite this statute as the model for federal-level cleanup recommendations.
[VERIFY current consolidated text via RIS.]

[JURISDICTION-SPECIFIC: France] _Projet de loi portant suppression de
sur-transpositions de directives européennes en droit français_ (2019). The Conseil
d'État (Section du rapport et des études) had earlier produced a 2018 study on
"sur-transposition" identifying recurring patterns. The 2019 bill targeted financial
services, environment, and social provisions. Cite as model for ministry-led
sectoral cleanup with explicit Conseil d'État impact assessment annexes.
[VERIFY enactment status of all titles.]

[JURISDICTION-SPECIFIC: United Kingdom] Pre-Brexit, the UK's Department for Business,
Innovation and Skills (BIS) "Gold-Plating Review" (2013) embedded a "copy-out"
principle and a five-year review template. After Brexit the UK is no longer a Member
State, but its 2013 review remains the most-cited published anti-gold-plating
methodology in the literature and is referenced here for taxonomy and review-clause
design — not as currently applicable EU-MS law.

[JURISDICTION-SPECIFIC: Germany] No statutory anti-gold-plating instrument, but the
_Nationaler Normenkontrollrat_ (NKR) issues cost opinions on every federal bill,
including transposition bills, applying the Standard Cost Model. NKR opinions are
the de facto burden-quantification baseline for German transposition and are cited
verbatim in many gold-plating studies. Cite NKR opinion number on first reference.

[JURISDICTION-SPECIFIC: Netherlands] _Adviescollege toetsing regeldruk_ (ATR) plays
a comparable burden-assessment role to NKR.

[JURISDICTION-SPECIFIC: Sweden] _Tillväxtverket_ maintains a regulatory-burden
register; _Regelrådet_ issues opinions on regulatory impact assessments including
transposition bills.

[JURISDICTION-SPECIFIC: Poland] CFA Society Poland's 2024 study "Gold-Plating in EU
Capital Markets" enumerates concrete gold-plating instances in MiFID II, Prospectus,
and AIFMD transposition. Use as a primary worked-example source for capital markets
findings.

[JURISDICTION-SPECIFIC: EEA — Iceland / Norway / Liechtenstein] Acts incorporated by
EEA Joint Committee Decision (Art. 102 EEA) bind the EFTA-pillar States as to the
result, on the same Art. 7 EEA / Art. 288 TFEU logic. Gold-plating in IS/NO/LI is
monitored by the EFTA Surveillance Authority under Art. 31 SCA rather than by the
European Commission. Findings should flag the EEA pillar where applicable; the ESA
Internal Market Scoreboard tracks transposition delay but does not currently publish
a gold-plating index.

[JURISDICTION-SPECIFIC: Switzerland] Switzerland is not in the EEA. Sectoral
agreements may import particular EU acts (e.g. air transport via the Air Transport
Agreement) but Swiss federal acts implementing those agreements are out of scope of
this skill. Re-route to a Swiss federal law analysis if requested.

The output of this skill is **not** a finding of EU law breach unless the directive
contains a maximum-harmonisation ceiling that the NIM crosses. In nearly all cases,
gold-plating is lawful national policy — possibly bad policy, but not unlawful
policy. The Glass Box must record this status explicitly.

---

## Interactive Clarification

This skill uses **⟁ CLARIFY** markers at key decision points. When you reach a CLARIFY
marker, ask the user before proceeding — do not silently assume defaults. Only ask when
the answer will materially change the analysis; if the context has already been provided,
skip that question and proceed.

Use the harness's structured question tool when one is available:

- **Claude Code / Agent SDK:** invoke the `AskUserQuestion` tool. Limits: 1–4 questions per
  call, 2–4 options each, header ≤ 12 characters. Pass the CLARIFY options as the `options`
  array.
- **OpenAI Codex CLI:** invoke `ask_user_question` (runtime) or, in plan mode,
  `request_user_input`. Pass the CLARIFY options as choices.
- **No structured tool available (other harnesses, CI, headless mode without a `canUseTool`
  callback):** emit the CLARIFY questions as numbered plain text and **stop until the user
  replies**. Do not proceed with assumed answers.

When you proceed with partial context, state every assumption explicitly so the user can
correct it.

**Standard clarification format:**

```
⟁ CLARIFY — [Decision point name]

[Short context: why this question matters]

1. **[Option A]**: [Description]
2. **[Option B]**: [Description]
3. **[Option C]**: [Description]

**Why this matters**: [One sentence on how the answer changes the analysis direction]
```

Skip any CLARIFY block already answered upstream. For batch / non-interactive runs,
apply these defaults:

- Persona: Legal firm (multi-MS comparative output)
- Operating mode: Detection-and-classification (not full burden quantification, which
  needs MS-supplied data)
- Burden quantification depth: Qualitative tier only (LOW / MEDIUM / HIGH / SEVERE)
  unless an SCM dataset is supplied
- Sister-MS comparison: Top-5 implementation peers from the transposition matrix
- Subsidiarity / proportionality: Apply Better Regulation Toolbox 2023 Tool #28 with
  default weighting
- EEA pillar: Out-of-scope unless the directive is JCD-incorporated and an EFTA-pillar
  MS is named in the input

---

## Workflow

### Step 1: Accept Input

Accept any of these input shapes:

- **Directive + MS pair**: e.g. "CSRD (Directive (EU) 2022/2464, CELEX 32022L2464) ×
  Germany". The skill expects the upstream skills to have produced an obligation
  register and a per-provision conformity assessment for that pair, but it can run on
  partial inputs and flag missing data.
- **Conformity assessment artefact**: a JSON file or Markdown report from
  `legalcode-eu-conformity-assessment` with at least one row classified as
  "over-coverage" or "stricter-than-directive."
- **Pre-built correlation table**: a Commission-format two-column table from
  `legalcode-eu-correlation-table-builder` plus the directive obligation register.
- **NIM-only request**: a request to compare a national text (with citation) against a
  directive (with CELEX) without upstream artefacts; the skill will run a slimmed
  analysis and flag the missing dependencies in the Glass Box.

Minimum required context:

- Directive short title + CELEX
- Member State (ISO 3166-1 alpha-2)
- NIM citation (national official journal reference and, if available, ELI)
- Domain (financial services, environment, social, digital, etc.) — informs which
  sectoral patterns to load

If anything is missing, do not silently fabricate. Ask the user. The Glass Box must
record any input the skill could not resolve.

### Step 2: Establish Persona and Operating Mode

⟁ CLARIFY — Persona

Treyst-style EU compliance work serves four distinct persona profiles whose deliverables
diverge sharply. The same directive analysis becomes a transposition draft for a ministry,
a comparative briefing for a law firm, an impact assessment for a company, or a policy
position for a trade federation.

1. **Government / EU institution**: Drafting national implementing measures, running
   internal conformity checks, preparing Commission notification packages, producing
   self-assessment for ESA (EFTA pillar) or DG-level review.
2. **Legal firm**: Producing client advisories, comparative cross-MS tables for client
   briefings, gap analyses for client compliance programmes.
3. **Company**: Building internal compliance impact assessments, identifying operational
   changes required, scoping internal policy updates, preparing for regulator engagement.
4. **Trade federation**: Industry-wide impact summaries, draft policy positions for
   engagement during legislative or transposition phases.

**Why this matters**: Persona determines output format, level of detail, audience
language, citation density, and which workflow branches to execute. A government
self-assessment requires correlation tables in Commission format; a company impact
assessment requires obligation extraction filtered to private-actor addressees; a
federation position needs comparative scoreboarding across MS.

Persona-specific branching applied throughout the rest of the workflow:

- **Government**: emphasise Step 8 remediation recommendations in legislative-drafting
  form (revocation clause text, narrowing-amendment text, sunset clause text). Use
  Austrian Anti-Gold-Plating-Gesetz 2019 and French 2019 sur-transposition cleanup
  bill as drafting templates. Output the gold-plating findings table as an annex to a
  draft cleanup omnibus.
- **Legal firm**: emphasise Step 6 cross-MS comparison and Step 7 subsidiarity
  analysis. Output a client memo that distinguishes "this MS is an outlier" findings
  from "this is a uniform pattern across the EU" findings, because the operational
  implications for the client differ sharply.
- **Company**: emphasise Step 5 burden quantification per finding, with euros-and-FTE
  estimates derived from NKR opinion data where available. Output an operational
  adjustments register keyed to the company's establishment footprint per MS.
- **Trade federation**: emphasise Step 6 cross-MS pattern recognition and Step 7
  subsidiarity / proportionality conclusions. Output a policy-engagement brief
  citing the HLG taxonomy verbatim and benchmarking the MS against the EU peer group.

⟁ CLARIFY — Operating Mode

1. **Detection-and-classification only**: identify gold-plating findings and assign
   them to the five-category taxonomy. No burden quantification beyond a qualitative
   tier. Suitable for early-stage cross-MS scans and federation-level scoping.
2. **Full burden quantification**: layer NKR-style cost-of-compliance estimates
   onto each finding using either supplied SCM data or sector-default tariffs.
   Suitable for company impact assessments and government cost-cleanup self-reviews.
3. **Remediation drafting**: in addition to detection and classification, produce
   draft amendment text for each finding (revocation, narrowing scope, adding a
   review clause, time-limiting the over-coverage). Suitable for ministry self-review.
4. **Cross-MS scoreboard**: run the analysis across multiple MS for the same
   directive and rank MS by gold-plating intensity. Suitable for federation policy
   engagement and Commission Single Market Scoreboard contributions.

**Why this matters**: Mode 1 is light-weight (hours), Mode 2 needs SCM tariff inputs
(days), Mode 3 needs draftsperson review (legal team), Mode 4 needs the implementation
matrix from `legalcode-eu-transposition-tracker` to be populated for the directive
across the EU-27. Each mode has different output fields.

⟁ CLARIFY — Burden quantification depth (only if Operating Mode = 2 or 3)

1. **Qualitative tiers only**: LOW / MEDIUM / HIGH / SEVERE per finding, anchored on
   number of addressees, frequency of obligation, and reversibility.
2. **Standard Cost Model lite**: time-per-action × wage-rate × frequency × addressee
   count, using sector-default wage rates from Eurostat NACE.
3. **Full NKR-style cost opinion**: SCM-lite plus one-off implementation cost,
   investment cost, and any "Erfüllungsaufwand für die Wirtschaft" decomposition.
   Requires NKR-equivalent input data or an in-house cost engineer.

**Why this matters**: Determines what number you can defensibly put on a finding.

### Step 3: Resolve Inputs

3a. **Obligation register** (output of skill B). Captures, per Article/paragraph,
the addressee, deontic operator, trigger condition, and `ms_option` flag. The flag
is decisive at Step 4: a provision flagged `ms_option=true` can only be classified
into category 4 (failure to use derogation) — never into categories 1, 2, or 3 —
because the directive itself authorises MS choice.

3b. **Per-MS NIM** (output of skill C). Capture NIM ELI, official-journal
reference, entry-into-force date, consolidated-text version, and any sector-
specific implementing decree. Record every instrument: many MS implement a single
directive across a primary act, secondary regulations, and ministerial decrees.

3c. **Over-coverage rows** (output of skill E). The conformity assessment
classifies each correlation-table row as correct / partial / incorrect / not
transposed / **over-coverage** / not applicable. The over-coverage rows are this
skill's seed set; other rows are out of scope unless the user requests re-
evaluation.

3d. **Review and sunset clauses**. Note the directive's review periodicity, scope,
and reporting addressee. NIMs that omit equivalent national review obligations are
category-5 candidates.

3e. **Expressly-permitted maximalism**. Some directives (notably social-policy
directives under Art. 153 TFEU and older consumer-protection instruments) include
"this Directive shall not prevent... more stringent... measures" clauses. The
NIM's stricter rule is then legally authorised but still policy-relevant — tag
"authorised gold-plating" in the Glass Box.

3f. **Maximum-harmonisation provisions**. Where the directive prohibits stricter
rules (e.g. Unfair Commercial Practices Directive 2005/29/EC; MiFID II passporting
provisions), NIM excess is prima facie an EU-law breach. Mark severity = SEVERE
and route to `legalcode-eu-infringement-procedure-tracker`.

### Step 4: Per-Provision Gold-Plating Test

For each over-coverage row from Step 3c, run the following decision procedure to
classify the finding into one of the five categories — or to reject the
classification ("not gold-plating").

**4a. Identify the EU minimum**.

Read the directive provision. Extract: (i) the addressees (which actors are bound),
(ii) the substantive obligation (what they must do or not do), (iii) any threshold
(when the obligation triggers), (iv) any sanction floor or grace period, and
(v) whether the directive grants a derogation, opt-out, or "may" choice.

**4b. Identify the NIM excess**.

Read the NIM provision. Extract the same five fields. Compute the delta against the
EU minimum. The delta may exist on any of the five fields — addressees, substance,
threshold, sanction, or unused derogation.

**4c. Classify the finding**.

Apply the following decision tree, evaluating each branch in order. The first
matching branch wins.

- **Category 1 — Scope extension**: NIM applies the directive rule to actors,
  transactions, products, or sectors outside the directive's stated personal or
  material scope. (Worked examples in the dedicated five-category section below.)
- **Category 2 — Additional substantive requirements**: NIM imposes extra
  disclosures, reports, capital, organisational standards, or process steps not
  required by the directive.
- **Category 3 — Stricter sanctions or earlier deadlines**: NIM imposes higher
  sanctions or shorter deadlines than the directive's floor or grace period.
- **Category 4 — Failure to use available derogations / opt-outs**: directive
  expressly permits MS to derogate, exempt categories, or set a lower threshold,
  and the MS declines to do so. The only category that can apply to use of an
  explicit `ms_option` provision.
- **Category 5 — Missing review / sunset clauses**: directive includes a review
  or sunset; NIM omits an equivalent national-level review.
- **Not gold-plating — reject the classification** if any of the following holds:
  - The directive expressly leaves the matter to MS discretion (`ms_option=true`)
    and the MS choice does not exceed the directive's outer bounds.
  - The NIM merely transposes the directive verbatim into national legal language;
    apparent excess is a translation artefact (reconcile via Art. 55 TEU equally-
    authentic-language rule and CILFIT case law).
  - The NIM rule is not a transposition rule at all but a pre-existing national
    rule on a related but distinct subject; the over-coverage is a recital-only
    issue and should be re-classified.
  - The NIM rule covers the same field as the directive but enacts a parallel
    domestic regime that does not interact with the directive's addressees or
    obligations.

If a finding fits more than one category (e.g. the NIM both extends scope and
imposes additional substantive requirements on the extended scope), file two
findings with cross-references — do not collapse them. The taxonomy is non-mutually-
exclusive on purpose: each category drives a distinct remediation pattern.

**4d. Severity scoring** (LOW / MEDIUM / HIGH / SEVERE).

Severity is a function of (i) addressee count × frequency × reversibility, (ii)
whether the gold-plating is "authorised" (recital permits stricter rules) or
"unauthorised" (in maximum-harmonisation field), and (iii) whether comparable MS
have not gold-plated.

| Severity | Indicators                                                                                                                                                         |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| LOW      | Few addressees, one-off action, recital-permitted, more than half of EU-27 has the same rule.                                                                      |
| MEDIUM   | Sector-wide addressees, recurring action, recital-permitted, half of EU-27 or fewer has the same rule.                                                             |
| HIGH     | Sector-wide or economy-wide, recurring, recital-permitted but MS is in the bottom quartile of EU-27 stringency, or measure cannot be reversed without legislation. |
| SEVERE   | Maximum-harmonisation field (gold-plating may be unlawful), or economy-wide, irreversible without legislation, and MS is the only EU-27 outlier.                   |

A SEVERE finding routes to the infringement-procedure tracker for follow-up; the
Glass Box must record this routing.

### Step 5: Quantify Burden

For each finding classified at Step 4, run the burden quantification appropriate to
the operating-mode depth selected at Step 2.

**5a. Standard Cost Model.** Annual cost = (time per action × hourly cost ×
frequency) × affected entities × (1 + overhead factor). Hourly cost from
Eurostat NACE wage data plus 25% (non-financial) or 40% (financial) overhead;
overhead factor 1.25 default / 1.4 financial. The gold-plating cost is the
**delta** between NIM SCM and directive-minimum SCM. See the dedicated Burden
Quantification reference section for the worked formulas.

**5b. NKR cost-opinion methodology.** The German NKR decomposes regulatory
cost into Erfüllungsaufwand für Bürgerinnen und Bürger (natural persons),
Erfüllungsaufwand für die Wirtschaft (businesses, with recurring and one-off
separated), Erfüllungsaufwand für die Verwaltung (public administration), and
Bürokratiekosten (information-obligation cost, narrow SCM definition). For
gold-plating, NKR opinions explicitly flag the share attributable to
"über die EU-Vorgaben hinausgehende nationale Regelungen." Cite the NKR
opinion number on first reference and reproduce the quantification table.

**5c. Qualitative tier mapping** (fall-back when SCM data insufficient):

| Tier   | Indicators                                                   |
| ------ | ------------------------------------------------------------ |
| LOW    | <100 addressees, one-off, EU-27 cost <€10k.                  |
| MEDIUM | 100–10,000 addressees, recurring, EU-27 cost €10k–€10m.      |
| HIGH   | >10,000 addressees, recurring, EU-27 cost €10m–€1bn.         |
| SEVERE | Economy-wide, EU-27 cost >€1bn, or material structural cost. |

Stay qualitative if the underlying data are not available; do not invent
precise euros figures.

**5d. Burden record per finding.** Capture: `directive_minimum_burden`,
`nim_burden`, `delta_burden`, `methodology` (SCM-lite / NKR / qualitative),
`confidence` (VERIFIED / LIKELY / POSSIBLE / VERIFY / ASSUMED), and `source`
(NKR opinion / national IA / Eurostat / industry survey).

### Step 6: Compare Against Sister MS

A finding gains policy weight when the MS is an outlier and loses weight when
the MS is part of an EU-wide pattern. Using the implementation matrix from
`legalcode-eu-transposition-tracker`, score each finding's MS position as
**outlier high** (top quartile, only this MS or a small cluster), **outlier
low** (bottom quartile — record for completeness; not gold-plating),
**cluster** (e.g. Nordic, DACH+NL, or all MS predating the directive's
harmonisation), or **pattern** (>half of EU-27 — the rule is the de facto
European standard, often worth re-classifying as not gold-plating).
"Outlier high" carries highest policy weight; pattern is the lowest. Generate
a 1–2-sentence sister-MS narrative naming the most relevant comparators.

Example narrative: "Germany's CSRD-Umsetzungsgesetz extends scope to medium-
sized unlisted undertakings; France's _ord. n° 2023-1142 du 6 décembre 2023_,
Italy's _D.Lgs. 125/2024_, and the Netherlands' _Implementatiewet richtlijn
duurzaamheidsrapportering_ track the directive. Germany is the EU-27 outlier
on this provision." [VERIFY all three ELIs.]

### Step 7: Apply Subsidiarity / Proportionality Test

Per Better Regulation Toolbox 2023 Tool #28, a national measure must satisfy
proportionality — be no more restrictive than necessary to achieve the public-
interest objective. Per finding:

**7a. State the public-interest objective.** Examples: investor protection
beyond the EU minimum (DK Financial Business Act gold-plating in MiFID II);
environmental protection (FR sur-transposition in chemicals); workforce-
stability (NL flex-work gold-plating in temporary-agency-work transposition).

**7b. Necessity.** Could the objective be achieved by a less-burdensome
measure? If yes, the gold-plate fails.

**7c. Proportionality stricto sensu.** Is the burden proportionate to the
marginal benefit? Judgement call informed by the Step 5 burden estimate. A
€1bn EU-27 cost for a marginal benefit fails.

**7d. Subsidiarity.** Is the matter better addressed at EU level? If yes, the
MS gold-plate may pre-empt a future Commission proposal — flag for federation
engagement to push harmonisation rather than national cleanup.

**7e. Record result** (PROPORTIONATE / DISPROPORTIONATE / INDETERMINATE) and
reasoning. Disproportionate findings are the priority remediation targets.

### Step 8: Generate Remediation Recommendations

For each finding (or each cluster of findings), draft a recommendation in one of
four forms. Choose form by category and persona.

**Form A — Revocation.** The NIM provision is repealed; the EU minimum applies.
Use when the gold-plate has no remaining national policy justification.

_Drafting template (government persona):_

> Article [N] of [NIM Act] is repealed. The application of [Directive Article X]
> shall thereafter follow the directive minimum as transposed by Article [N-1].

**Form B — Narrowing scope.** The NIM provision is amended to track the directive
scope. Use for category 1 (scope extension) findings that retain a residual
justification on a sub-set.

_Drafting template:_

> In Article [N] of [NIM Act], the words "and [extended addressee class]" are
> deleted. The article shall apply only to the addressees listed in [Directive
>
> > Article X(1)].

**Form C — Adding a review or sunset clause.** The NIM provision is preserved but
becomes subject to a five-year review on the UK BIS 2013 model. Use for
authorised-gold-plating findings the MS does not wish to repeal but that should
be evidence-tested.

_Drafting template:_

> Article [N] of [NIM Act] shall be reviewed five years after entry into force.
> The review shall consider: (a) whether the article continues to be necessary
> to achieve [stated objective]; (b) the cost of compliance against the directive
> minimum; (c) whether comparable Member States have introduced similar rules.
> The review report shall be laid before Parliament. If no decision to retain
> the article is taken within six months of the report, the article ceases to
> have effect.

**Form D — Time-limiting the gold-plate.** The NIM provision is preserved for a
fixed period and lapses automatically. Use for transitional or grandfathering
gold-plating that is not intended to be permanent.

_Drafting template:_

> Article [N] of [NIM Act] ceases to have effect on [date five years after entry
>
> > into force] unless an Act of [legislature] adopted before that date provides
> > otherwise.

For company persona: skip the legislative-drafting forms and produce instead an
operational-adjustments register: "to comply with the German CSRD over-implementation
on supply-chain ESRS disclosures, the company must: (i) extend the data-collection
boundary to all DE-resident subsidiaries below the EU CSRD threshold, (ii) align
the reporting calendar with German fiscal year, (iii)..." etc.

For federation persona: skip the operational forms and produce a policy-engagement
brief: position statement, requested action of MS legislator, requested action of
the Commission (if cross-MS pattern), peer-MS benchmark.

### Step 9: Emit Outputs

Produce four output formats plus the Glass Box. See [Output Format Template]
below for full templates.

- **Markdown findings table**: one row per finding.
- **JSON findings schema**: machine-readable, per the JSON section.
- **AKN4EU stub**: each finding as a `<doc>` annotation referencing both the
  directive ELI and the NIM ELI.
- **LegalRuleML stub**: each finding as a `<lrml:Constitutive>` block expressing
  "NIM provision X imposes obligation O₂; directive provision Y imposes obligation
  O₁; O₂ ⊃ O₁" (over-coverage logic).
- **Glass Box**: deterministic audit trail of every decision in Steps 3–8.

### Step 10: Self-Interrogation Pass

Before finalising, run three passes of self-interrogation on every finding:

- **Pass 1 — Specificity check**: every finding must cite the exact directive
  Article + paragraph and the exact NIM Article + paragraph. No bare "the directive"
  or "the NIM."
- **Pass 2 — Discretion check**: re-confirm that no finding misclassifies a
  legitimate use of an `ms_option=true` discretion as gold-plating. If the
  directive permits the choice, it is not category 1, 2, or 3.
- **Pass 3 — Sister-MS sanity check**: re-confirm the sister-MS comparison.
  Findings that are part of an EU-wide pattern should not be labelled "outlier."

Findings that fail any pass are demoted from CRITICAL/HIGH to LIKELY/POSSIBLE
confidence, or removed altogether.

---

## The Five-Category Taxonomy

### Category 1 — Scope extension

The NIM applies the directive rule to actors, transactions, products, or sectors
that the directive expressly excludes or that fall outside its stated personal
or material scope.

**Indicators:** the directive's Art. 1 / Art. 2 lists addressees and the NIM
extends past the list; the directive contains a size-cap or sectoral threshold
and the NIM lowers it; the directive exempts certain transactions / products
and the NIM removes the exemption.

**Real-world examples:**

- **CSRD scope extension** (Directive (EU) 2022/2464, CELEX 32022L2464). The
  directive phases CSRD reporting across large undertakings (Year 1), listed
  SMEs and other large undertakings (Years 2–3). NIMs that bring unlisted
  medium-sized undertakings forward are category 1. [VERIFY against current
  consolidated text and 2024 Omnibus phase-in amendments.]
- **MiFID II conduct-of-business extension** (per CFA Society Poland 2024).
  Several MS applied MiFID II Arts. 24–30 conduct rules to non-MiFID firms
  (domestic asset-managers below AIFMD thresholds, retail intermediaries)
  outside the Directive 2014/65/EU (CELEX 32014L0065) Art. 4(1)(1) perimeter.
- **NIS2 scope extension** (Directive (EU) 2022/2555, CELEX 32022L2555). Art. 2
  defines addressees by sector (Annex I/II) and size; a NIM capturing small
  entities below the size-cap is category 1. [VERIFY MS-by-MS via Single Market
  Scoreboard NIS2 transposition section.]

**Remediation pattern:** Form B (narrow scope) is first-choice; Form A (revoke)
where the extended scope has no policy justification; Form D (time-limit) for
grandfathered domestic rules pre-dating the directive.

### Category 2 — Additional substantive requirements

The NIM imposes extra disclosures, reports, capital, organisational standards,
governance steps, or process steps not required by the directive.

**Indicators:** the directive sets a minimum content list and the NIM adds
items; the directive sets a minimum frequency and the NIM increases it; the
directive requires an internal process and the NIM adds external attestation.

**Real-world examples:**

- **CSRD national disclosure annexes.** MS layering national taxonomy / national-
  form annexes on top of ESRS (delegated act under Art. 29b of Directive
  2013/34/EU as amended). [VERIFY MS-by-MS — France's *Plan Climat* taxonomy
  and Germany's potential supplementary disclosure expectations.]
- **AIFMD quarterly portfolio reporting** on top of Art. 22 annual reports
  (per CFA Society Poland 2024).
- **MiFID II national product-governance overlays** on Art. 16(3) (per CFA
  Society Poland 2024).
- **Whistleblower bi-annual audit** of the internal channel where Directive
  (EU) 2019/1937 only sets minimum content.

**Remediation pattern:** Form B (narrow content) or Form C (review clause).
Full revocation is rare because the underlying obligation tracks the directive.

### Category 3 — Stricter sanctions or earlier deadlines

The directive sets a sanction floor or deadline grace period; the NIM imposes
higher sanctions or shorter deadlines.

**Indicators:** directive specifies "effective, proportionate and dissuasive"
penalties with a minimum-maximum range and the NIM sets a higher fixed amount;
directive specifies a notification deadline and the NIM shortens it; directive
permits a transition period and the NIM omits it.

**Real-world examples:**

- **NIS2 incident-reporting deadlines** (Directive (EU) 2022/2555 Art. 23
  sets 24h early warning / 72h notification / 1-month final report). An MS
  NIM shortening early warning to 12h is category 3. [VERIFY MS list.]
- **GDPR national criminal sanctions.** Reg. (EU) 2016/679 Art. 84 permits MS
  criminal sanctions on top of Art. 83 administrative fines; treat case-by-
  case (often properly category 4, but layered stringency in harmonised-
  dissuasion fields can be category 3).
- **Whistleblower retaliation sanctions.** Directive (EU) 2019/1937 Art. 25
  sets effective-proportionate-dissuasive sanctions; MS-imposed fixed minima
  in the millions for legal persons can be category 3 if materially above peer.
- **CSDDD enforcement deadlines** [VERIFY article]. NIMs shortening
  authority response or extending company compliance windows are category 3.

**Remediation pattern:** Form A (revoke, revert to directive minimum); Form C
(review clause) for "experimental" higher sanctions.

### Category 4 — Failure to use available derogations / opt-outs

The directive grants MS the option to derogate, exempt categories, set a lower
threshold, or otherwise relax the rule, and the MS declines to use it. This is
gold-plating by **omission**, not addition: the MS chose the most-stringent
reading of a permissive rule.

**Indicators:** "Member States may..." or "may exempt..." language unused;
opt-out granted but not exercised; phased entry-into-force ignored.

**Real-world examples:**

- **AIFMD sub-threshold exemption** (Art. 3 Directive 2011/61/EU). MS that
  decline the exemption bring sub-threshold managers into full AIFMD scope
  (per CFA Society Poland 2024).
- **GDPR Art. 23 restrictions.** Reg. (EU) 2016/679 permits MS to restrict
  data-subject rights for public-interest objectives; non-use in well-
  established cases (national security, tax collection, civil-law enforcement)
  imposes fuller rights than peer MS.
- **Posting-of-Workers Enforcement Directive 2014/67/EU permissive exemptions**
  for short-term postings — non-use is category 4.
- **ATAD I CFC opt-outs** (Directive (EU) 2016/1164) — non-use is category 4
  (policy evaluation depends on underlying tax position).

**Remediation pattern:** Form B (activate the unused derogation) or Form C
(review whether non-use should be revisited). Form A is rarely available
because the rule itself tracks the directive — the gold-plate is in the
_non-use_, not in any extra rule.

### Category 5 — Missing review / sunset clauses

The directive includes a Commission-level review or sunset clause and the NIM
omits an equivalent national-level review obligation.

**Indicators:** directive's final articles contain "By [date], the Commission
shall review..."; directive contains a sunset; directive recitals contemplate
review mechanisms.

Omission forecloses the national legislator's ability to revisit the gold-
plate, leaving it to drift even after the directive itself has been refreshed.

**Real-world examples:**

- **NIS2 review.** Directive (EU) 2022/2555 Art. 40 requires Commission review
  by 17 October 2027; MS NIM without a parallel review is category 5.
- **CSRD review.** Directive (EU) 2022/2464 contains a Commission review
  obligation; MS NIM without a parallel review is category 5.
- **CSDDD review** [VERIFY article]. Directive (EU) 2024/1760 review obligation
  without parallel national review is category 5.
- **Whistleblower Directive review.** Directive (EU) 2019/1937 Art. 27 review
  obligation without parallel national review is category 5.

**Remediation pattern:** Form C (add review clause on UK BIS 2013 model). The
cleanest approach is a horizontal review clause applying to every NIM by
reference, but most MS handle this per-NIM.

---

## Per-Sector Gold-Plating Patterns

Sector-specific patterns recur and inform Step 4 classification. Use this
reference when the user supplies a directive in one of the listed sectors.

### Financial services (per CFA Society Poland 2024)

The CFA Society Poland 2024 study _Gold-Plating in EU Capital Markets_ is the
densest published catalogue of capital-markets gold-plating across MiFID II,
Prospectus, and AIFMD. Recurring patterns: MiFID II conduct-of-business
extension to non-MiFID firms applying Arts. 24–30 to domestic asset-managers
and retail intermediaries (categories 1 and 2 simultaneously); MiFID II
product-governance overlays on Art. 16(3) (category 2); MiFID II ex-ante
inducement bans ahead of the Retail Investment Strategy (category 3); AIFMD
sub-threshold derogation non-use (category 4); AIFMD quarterly portfolio
transparency on top of Art. 22 annual reports (category 2); Prospectus
Regulation (EU) 2017/1129 national content overlays in MS-choice margins
(category 2 functionally, though Prospectus is a regulation); IFR / IFD
(Regulation (EU) 2019/2033 / Directive (EU) 2019/2034) national capital floors
above the EU minimum (categories 2 and 3). Cite CFA Society Poland 2024 page
numbers where applicable [VERIFY named MS list against current paper text].

### Environmental policy (per French sur-transposition law)

The 2019 French sur-transposition cleanup bill identified recurring environmental
patterns: REACH national safety-data-sheet content overlays on top of Regulation
(EC) No 1907/2006 (category 2); Industrial Emissions Directive 2010/75/EU
permitting thresholds below Annex I capturing sub-scope installations (categories
1 and 3); Waste Framework Directive 2008/98/EC national classification annexes
(category 2); Bathing Water Directive 2006/7/EC Annex I parameter overlays
(category 2); Habitats Directive 92/43/EEC national species-list extensions to
Annex II/IV/V (category 1). Cite the 2019 bill's annexes for the named MS list
[VERIFY the bill's final adopted scope].

### Employment / labour (per UK BIS 2013 review)

The UK BIS 2013 Gold-Plating Review identified recurring patterns: Working Time
Directive 2003/88/EC Art. 3 daily-rest extensions (category 3); Agency Workers
Directive 2008/104/EC Art. 5(4) equal-treatment scope expansion past the
qualifying-period limits (categories 1 and 2); Posting of Workers Enforcement
Directive 2014/67/EU Art. 9 prior-notification enrichment (category 2);
Information and Consultation Directive 2002/14/EC Art. 3 lower workforce
thresholds (category 1); Collective Redundancies Directive 98/59/EC lower
thresholds (category 1). The "copy-out" principle (transpose the directive
verbatim and resist policy-driven additions) remains the most-cited heuristic
in the literature.

### Cybersecurity and digital (NIS2, AI Act, DORA, DSA/DMA)

NIS2 (Directive (EU) 2022/2555) attracts size-cap extensions (category 1), sub-
24-hour early-warning shortening (category 3), and national board-training overlays
beyond Art. 20 (category 2). The AI Act, DORA, and DSA/DMA are regulations rather
than directives, so true gold-plating vocabulary is misapplied; national
supplementary fields in the margins where each regulation permits MS choice are
functionally similar (national supervisory register-overlays for DORA Reg. (EU)
2022/2554; conformity-assessment supplements at MS level for AI Act Reg. (EU)
2024/1689). DSA / DMA leave little room because the Commission has reserved
enforcement competence over VLOPs and gatekeepers; overlays there are mainly in
procedural-cooperation provisions.

### Sustainability and corporate reporting (CSRD, CSDDD)

For CSRD (Directive (EU) 2022/2464): national taxonomy annexes (category 2),
scope acceleration ahead of the directive's phase-in (category 1), and assurance-
scope extensions beyond Art. 34a Directive 2013/34/EU as amended (category 2).
For CSDDD (Directive (EU) 2024/1760): scope extension to smaller groups ahead
of the phase-in (category 1); civil-liability regimes broader than Art. 29
(category 2 or 3); national supervisory authorities with broader powers than
the directive's minimum (category 2). Cite the Linklaters and Bird & Bird CSRD /
CSDDD trackers and the Commission's transposition notices for verified per-MS
positions [VERIFY with current trackers].

---

## Burden Quantification

### NKR cost-opinion approach

The German Nationaler Normenkontrollrat is the most-developed institutional
practice for assessing the burden of national legislation, including transposition
bills. Every federal-government draft statute that goes through the Bundeskabinett
attracts an NKR opinion (Stellungnahme). The opinion decomposes burden into:

- **Erfüllungsaufwand für Bürgerinnen und Bürger** — compliance cost for natural
  persons, in hours and euros.
- **Erfüllungsaufwand für die Wirtschaft** — compliance cost for businesses,
  separately quantifying recurring and one-off cost. One-off cost (Umstellungs-
  aufwand) is reported separately because it is not annualised.
- **Erfüllungsaufwand für die Verwaltung** — compliance cost for public
  administration, federal and Länder.
- **Bürokratiekosten** — information-obligation cost specifically (a sub-set of
  Erfüllungsaufwand für die Wirtschaft using the narrow SCM definition).

For transposition bills, NKR opinions explicitly flag the share attributable to
"über die EU-Vorgaben hinausgehende nationale Regelungen" — that is, gold-plating.
Use that share as the gold-plating cost figure for German findings; cite the NKR
opinion number.

Where the user is analysing a non-German MS, look for the MS's analogue:

- Netherlands: _Adviescollege toetsing regeldruk_ (ATR).
- Sweden: _Tillväxtverket_ register and _Regelrådet_ opinions.
- France: _Conseil d'État_ impact assessment annexes.
- Austria: _RIS Wirkungsorientierte Folgenabschätzung_ (WFA).
- Spain: _MEMORIA del Análisis de Impacto Normativo_ (MAIN).
- Italy: _Analisi di impatto della regolamentazione_ (AIR).

### Standard Cost Model derivation

The SCM was developed in the Netherlands and is the backbone of every national
burden-assessment regime listed above and of the EU Better Regulation Toolbox 2023. Core formula: Annual cost = (time per action × hourly cost × frequency) ×
affected entities × (1 + overhead factor). For gold-plating, compute the
directive-minimum cost and the NIM cost separately, then take the delta.

Inputs in practice. **Time per action**: from a process map (e.g. quarterly
reporting ≈12 hours per occurrence; annual ≈36 hours). **Hourly cost**:
Eurostat NACE-level wage data plus 25% overhead (non-financial) or 40%
(financial). For DE 2024 compliance roles, indicative fully-loaded €70–€110
[VERIFY Destatis]. **Frequency**: per-year count. **Affected entities**:
Eurostat structural business statistics, NACE Rev. 2 sub-sector breakdown.
**Overhead**: 1.25 default; 1.4 financial services.

Worked illustration: category 2 "MS X requires quarterly AIFMD portfolio
reporting on top of the directive's annual cadence." Time 12h × €100 × 3
additional reports × 200 AIFMs × 1.4 = **€1.008m per year MS-X**. Illustrative
only — supply real entity counts and time-per-action estimates from the user's
data.

### Delta, public-admin burden, recurring vs. one-off, confidence

The gold-plating cost is the **delta** between NIM SCM and directive-minimum
SCM. Capture public-administration burden separately ("Erfüllungsaufwand für
die Verwaltung") — sometimes dominant when the MS sets up a stand-alone
supervisor for the gold-plating regime. Always separate one-off implementation
cost (Umstellungsaufwand) from recurring cost: a €10m sunk one-off does not
drive present-value remediation rationale; only the recurring delta does.

Confidence labelling (apply to every burden figure):

- **VERIFIED**: NKR opinion or equivalent national IA cited.
- **LIKELY**: SCM-lite estimate from Eurostat + disclosed entity counts.
- **POSSIBLE**: SCM-lite estimate from sector-default tariffs + estimated counts.
- **VERIFY**: NKR opinion not cited, entity counts not validated.
- **ASSUMED**: no underlying data; placeholder. Range-quote, never point-quote.

---

## Cross-MS Comparison

Cross-MS comparison turns a finding into a policy-relevant outlier statement.
The implementation matrix from `legalcode-eu-transposition-tracker` is the
natural input. Where the matrix is populated for the directive, this step is
mechanical.

### Position scoring per finding

Score the MS's position on the relevant directive provision against the EU-27:
**outlier high** (top quartile — only this MS or a small cluster); **cluster**
(a clear group shares the rule, e.g. Nordic / DACH / Benelux); **pattern**
(>half of EU-27 — the directive itself is arguably the outlier); **singleton**
(only this MS — strongest outlier signal).

### Pattern-recognition heuristics

Recurring clusters: Nordic (SE / DK / FI, with IS / NO at EEA pillar) on
consumer-protection, employment, sustainability; DACH (DE / AT, LI at EEA
pillar) on financial-services governance; Benelux (BE / NL / LU, though LU
often departs to preserve cross-border attractiveness) on passporting and tax
cooperation; Mediterranean (ES / IT / FR / EL / CY / MT) on labour protection
and consumer rights; CEE (PL / CZ / HU / SK / RO / BG) on lighter transposition
and lower stringency, sector-fragmented. Heuristics only — the matrix is the
source of truth.

### EU-27 stringency scoreboard

In operating mode 4, produce a table with one row per MS and one column per
directive provision, marking each cell with gold-plating intensity (none /
category 1–5 / multiple). Compute a per-MS aggregate stringency score (simple
sum or burden-tier-weighted). Scoreboards are the natural federation policy-
engagement artefact.

### Gold-plating index — methodological cautions

Avoid building a single-number "gold-plating index" without methodological
disclosure. The index is sensitive to (i) which directive provisions are
included, (ii) how categories are weighted, (iii) burden-tier weighting. Always
report the underlying matrix alongside any index.

The Single Market Scoreboard published by the European Commission and the
Internal Market Scoreboard published by the EFTA Surveillance Authority track
transposition delay and infringement counts but do not currently publish a
gold-plating index. If the user requests one, build it for the specific directive
in question and document the methodology fully — do not generalise.

---

## Distinguishing Gold-Plating from Legitimate Discretion

The most common misclassification is treating a legitimate use of MS discretion
as gold-plating. Discretion has four shapes; the analyst must run all four
checks before settling a category-1/2/3 classification.

### Directives with explicit MS options

Many directives use "Member States may..." language. Examples include GDPR
Art. 8(1) (digital-services consent age 13–16), GDPR Art. 23 (restrictions on
data-subject rights), GDPR Art. 84 (criminal-sanction option), AIFMD Art. 3
(sub-threshold exemption), ATAD I Arts. 7–8 (alternative CFC formulations),
Whistleblower Directive Art. 8(3) (channel-size threshold), and the Industrial
Emissions Directive (tighter permit conditions). Where the directive expressly
grants the discretion, exercising it cannot be gold-plating in categories 1,
2, or 3 — the MS is doing what the directive authorised. The only category
applicable is **category 4** (failure to use the derogation in a maximalist
direction).

### Directives with minimum-harmonisation clauses

Some directives expressly permit MS to maintain or adopt more stringent
provisions (notably social-policy directives under Art. 153 TFEU and older
consumer-protection instruments). The NIM's stricter rule is then **legally
authorised** but still classifiable as gold-plating in the policy sense. Tag
"authorised gold-plating" in the Glass Box.

### Directives with maximum-harmonisation provisions

Some directives prohibit MS from adopting stricter rules (Unfair Commercial
Practices Directive 2005/29/EC; MiFID II Title II passporting provisions; the
exclusivity logic in DSA / DMA, regulations though they are). NIM excess in
those fields is **prima facie unlawful** under Art. 258 TFEU — escalate to
SEVERE and route to `legalcode-eu-infringement-procedure-tracker`.

### Translation artefacts

NIM wording that looks stricter may simply reflect local-language drafting
against a different equally-authentic EU language version (Reg. 1/1958; CILFIT
C-283/81). Slovenian, Latvian, and Maltese drafts are common pitfalls: their
modal verbs read as more peremptory than the English or French. Cross-check at
least three EU language versions before concluding gold-plating on wording
grounds alone.

### Pre-existing national rules

A NIM that restates a pre-existing national rule on a related but distinct
subject is not gold-plating — it is a parallel domestic regime. Distinguish by
reading the legislator's explanatory memorandum: was the rule enacted as a
transposition measure, or as a free-standing domestic policy?

### Recommended four-step discretion check

Before classifying any finding as gold-plating in categories 1, 2, or 3:

1. Does the directive expressly grant `ms_option=true` on the matter? If yes,
   drop to category 4 or reject classification.
2. Does the directive expressly permit stricter rules (minimum-harmonisation
   clause)? If yes, tag "authorised gold-plating" and continue.
3. Does the directive expressly prohibit stricter rules (maximum-harmonisation
   clause)? If yes, escalate to SEVERE and route to infringement tracker.
4. Is the apparent excess a translation artefact? If yes, reject classification.

Findings that pass all four steps are properly gold-plating.

---

## EEA Pillar Considerations

For acts incorporated by EEA Joint Committee Decision under Art. 102 EEA, the
EFTA-pillar Member States — Iceland, Norway, and Liechtenstein — are bound to
implement the act in their national legal orders. The same gold-plating analysis
applies, with three institutional twists:

### ESA monitoring (Art. 31 SCA)

The European Commission has no enforcement competence in respect of IS / NO / LI
NIMs. Monitoring is conducted by the EFTA Surveillance Authority under Art. 31 of
the Surveillance and Court Agreement. Infringement procedures run before the
EFTA Court rather than the CJEU. ESA does not currently publish a gold-plating
index, but its case practice in transposition surveillance occasionally surfaces
gold-plating issues incidentally to non-conformity proceedings.

### EEA Joint Committee Decision adaptations

When an act is incorporated into the EEA Annexes by JCD, the JCD often makes
"adaptations" — sectoral or constitutional carve-outs negotiated by the EFTA
States. Read the JCD before running gold-plating analysis on an EFTA-pillar
NIM: an apparent gold-plate may simply be the consequence of a JCD adaptation
that narrowed the EFTA-pillar scope of the act compared to the EU-pillar version.
In that case, the EFTA-pillar NIM may be following an adapted text that differs
from the directive as it applies in EU-27.

The list of JCDs is published on EEA-Lex (https://www.efta.int/eealaw). For each
relevant JCD, capture the JCD number, the date, the EEA Annex affected, and any
adaptation language.

### Article 103 EEA constitutional reservations

Some EFTA States have constitutional rules requiring parliamentary approval
before specific JCDs take effect (e.g. Norwegian Storting consent for new EEA
obligations of significance; Icelandic Althingi consent in some cases;
Liechtenstein constitutional procedures). When an Art. 103 reservation is
pending, the act has not yet entered into force in the EFTA pillar — there is no
NIM to gold-plate-analyse, and the analysis must wait. Record this status in
the Glass Box.

### Cross-pillar comparison

For the cross-MS step, EFTA-pillar States can be included in the comparison set
for acts incorporated into the EEA, but tag them clearly so the user knows the
finding does not feed into EU-27 Single Market Scoreboard inputs.

---

## Anti-Patterns

The following twenty anti-patterns recur in gold-plating analysis. Avoid each.

1. **Treating any divergence from the directive as gold-plating.** Most
   divergences are uses of explicit MS options (`ms_option=true`) and are not
   gold-plating in categories 1–3. Run the four-step discretion check at the
   start of every classification.

2. **Skipping the directive-minimum baseline computation.** Burden quantification
   that does not separately compute the directive's own SCM cost cannot
   produce a defensible delta. Always compute the baseline.

3. **Confusing maximum-harmonisation breaches with gold-plating.** Where the
   directive prohibits stricter rules, the NIM's stricter rule is potentially
   unlawful — that is an Art. 258 TFEU question, not a gold-plating question.
   Route to the infringement tracker.

4. **Assuming the directive's English version is authoritative.** All 24
   language versions are equally authentic (CILFIT C-283/81). Apparent excess in
   one NIM may be a translation artefact. Cross-check at least three language
   versions.

5. **Conflating one-off and recurring costs.** Reporting "the gold-plate costs
   €X annually" when a third of X is actually one-off implementation cost
   inflates the figure and discredits the analysis. Always report separately.

6. **Building a single-number gold-plating index without methodological
   disclosure.** Indices are sensitive to weighting choices. Report the
   underlying matrix; never publish an index alone.

7. **Misclassifying use of GDPR Art. 23 derogations as gold-plating.** GDPR
   Art. 23 expressly grants MS the option to restrict data-subject rights. Use
   of the option is not gold-plating; non-use in defensible cases is category 4.

8. **Ignoring authorised gold-plating.** Where the directive expressly permits
   stricter rules (minimum-harmonisation clause), the gold-plate is lawful but
   still policy-relevant. Tag "authorised gold-plating" and continue — do not
   reject the classification.

9. **Failing to cross-check sister MS.** A finding tagged "outlier" without a
   sister-MS check is fragile. The MS may in fact be in a cluster the analyst
   missed. Always run the cross-MS step before finalising severity.

10. **Treating regulations as susceptible to gold-plating.** Regulations apply
    directly and prohibit national supplementary rules in the harmonised field.
    Apparent overlays in regulation-fields are infringement candidates, not
    gold-plating findings. Use this skill for directives only.

11. **Producing remediation drafts without persona match.** Government wants
    amendment text; companies want operational adjustments; federations want
    policy briefs. Form A–D drafting templates only fit the government persona.

12. **Conflating EFTA-pillar JCD adaptations with gold-plating.** A JCD
    adaptation may have narrowed the EFTA-pillar scope; the resulting NIM may
    look gold-plated against the EU-pillar text but is actually tracking the
    JCD-adapted text. Read the JCD first.

13. **Bundling multiple findings into one row.** Each gold-plating finding has
    a distinct directive Article + NIM Article pairing and a distinct
    classification. Bundling collapses traceability. One finding per row.

14. **Treating gold-plating as inherently bad.** Some gold-plating reflects
    genuine national policy preferences (heterogeneous risk-tolerance, sectoral
    structure, legal tradition). Burden quantification surfaces the cost; the
    policy judgement is a separate exercise. Avoid normative framing in the
    analytical output — reserve it for the Step 8 remediation recommendations.

---

## Writing Standards

Follow these standards when producing gold-plating detector outputs:

1. **Evidence-first findings, citation pair upfront.** Every finding opens with
   "Directive [short title], Art. [N(p)] (CELEX [code]); NIM [short title], Art.
   [N(p)] (ELI [link])." No bare "the directive said." Without the pair, the
   finding is not actionable.

2. **Active voice, imperative form.** "The NIM extends scope to medium-sized
   unlisted undertakings" beats "scope was extended by the NIM to..." — passive
   voice obscures the actor.

3. **Specificity in delta descriptions, one finding per row.** Quantify the
   delta with directive-vs-NIM thresholds, addressee counts, and Eurostat NACE
   references. Do not bundle multiple distinct findings; use cross-references
   instead.

4. **Confidence transparency and Glass Box inline reference.** Every finding
   shows VERIFIED / LIKELY / POSSIBLE / VERIFY / ASSUMED. Every CRITICAL or
   HIGH severity finding references the corresponding Glass Box decision
   sequence inline.

5. **EU citation format.** Use consistently: "[Short title] Art. [N(p)] ([CELEX
   or ELI])." Examples: "GDPR Art. 35(1) (Reg. (EU) 2016/679, CELEX 32016R0679)";
   "NIS2 Art. 21(2)(d) (Dir. (EU) 2022/2555, CELEX 32022L2555)"; "AIFMD Art. 3
   (Dir. 2011/61/EU, CELEX 32011L0061)". Second reference may use short form.

6. **NIM citation format.** "[National short title], [article], [official journal
   reference], [ELI if available]." Use BGBl. (DE), JORF (FR), BOE (ES), GU (IT),
   Stb. (NL), RIS (AT), Sb. (SE) conventions.

7. **Deontic operator and 24-language reconciliation.** Track the directive's
   modal — "shall ensure" (result-obligation), "may" (discretion), "Where a
   Member State..." (conditional). For wording-sensitive findings, name the
   language-version basis in the Glass Box (CILFIT C-283/81; Codan C-236/97;
   EMU Tabac C-296/95).

8. **EEA-relevance flag.** Mark whether the directive is EEA-relevant. For
   relevant findings, capture the JCD citation and confirm IS / NO / LI status
   before extending the analysis.

9. **CELEX / ELI / ECLI in prose on first reference.** First reference to an
   act in prose carries CELEX; first reference to a national instrument carries
   ELI; first reference to case law carries ECLI. Short form thereafter.

10. **No false precision; [VERIFY] inline; board-ready summary.** ASSUMED-
    confidence figures must be range-quoted, not given as point estimates.
    [VERIFY] sits immediately after the unconfirmed claim. The Executive
    Summary speaks to a board member with no EU-law background — 3–5 bullets,
    no untranslated Latin or French.

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

When legalcode-mcp is available, route legal research through it. Use cases by
workflow phase: Step 3 — search EUR-Lex for directive consolidated text and
CELEX↔ELI resolution; Step 4 — search EUR-Lex N-Lex for latest NIM text and
24-language reconciliation; Step 5 — search NKR / ATR / equivalent national IA
databases for the transposition bill's burden-decomposition table; Step 6 —
search Single Market Scoreboard, ESA Internal Market Scoreboard, Linklaters /
Bird & Bird trackers for per-MS positions; Step 7 — search Better Regulation
Toolbox 2023 Tool #28 working papers and Conseil d'État studies; Step 8 —
search Austrian Anti-Gold-Plating-Gesetz 2019 and French 2019 sur-transposition
bill text for drafting templates. Save results to
`/tmp/legalcode-gold-plating-research.md` and note in Glass Box.

### Without legalcode-mcp

Proceed with the [shared EU legislative-data pack](references/eu-legislative-data/)
and the published authority anchors in this skill. Mark all statutory references
with [VERIFY] and note in Glass Box: `legalcode_mcp: "Not connected — references
require independent verification"`.

Apply downward confidence adjustments:

- Directive text citations: VERIFIED → LIKELY (consolidated-text version-stamping
  not validated).
- NIM text citations: LIKELY → POSSIBLE (national-journal currency not
  validated).
- Burden figures: LIKELY → VERIFY (source databases not consulted).
- Sister-MS positions: LIKELY → POSSIBLE (matrix not refreshed).

### Related Skills Integration

| Trigger                                                     | Invoke This Skill                             |
| ----------------------------------------------------------- | --------------------------------------------- |
| Need to extract directive obligation register               | `legalcode-eu-directive-analyzer`             |
| Need per-MS NIM citations / dates                           | `legalcode-eu-transposition-tracker`          |
| Need Commission-format correlation table                    | `legalcode-eu-correlation-table-builder`      |
| Need per-Article conformity verdict (predecessor)           | `legalcode-eu-conformity-assessment`          |
| SEVERE finding (max-harmonisation breach)                   | `legalcode-eu-infringement-procedure-tracker` |
| EFTA-pillar finding                                         | `legalcode-eea-incorporation-tracker`         |
| Underlying risk register / company impact map               | `legalcode-policy-gap-analysis`               |
| Sectoral compliance follow-on (e.g. NIS2 Art. 21 deep-dive) | `legalcode-nis2-compliance-assessment`        |

---

## Output Format Template

### 1. Executive Summary

```
## Gold-Plating Detection — Executive Summary

Directive: [Short title] ([Full title], CELEX [code], OJ [reference])
Member State: [Name + ISO code]
NIM: [Short title], [Official journal reference], [Date], [ELI]
Assessment Date: [YYYY-MM-DD]
Operating Mode: [1 / 2 / 3 / 4]
Persona: [Government / Legal firm / Company / Trade federation]

### Overall Gold-Plating Intensity: [LOW / MEDIUM / HIGH / SEVERE]

**Findings by category:**
- Category 1 (Scope extension): [N]
- Category 2 (Additional substantive requirements): [N]
- Category 3 (Stricter sanctions or earlier deadlines): [N]
- Category 4 (Failure to use derogations / opt-outs): [N]
- Category 5 (Missing review / sunset clauses): [N]
- TOTAL: [N]

**By severity:**
- SEVERE: [N] (route to infringement tracker)
- HIGH: [N]
- MEDIUM: [N]
- LOW: [N]

**Key findings (3–5 bullets, board-ready):**
1. [Finding-001 short description]
2. [Finding-002 short description]
3. [Finding-003 short description]

**Aggregate burden estimate (delta vs. directive minimum):**
- Recurring annual delta: €[X] [confidence] — [methodology]
- One-off implementation delta: €[Y] [confidence] — [methodology]
- Affected addressee count: [N]

**Decisions required:**
1. [Decision A — typically: approve cleanup omnibus / accept findings / commission
   external counsel review of SEVERE findings]
2. [Decision B — typically: approve burden-quantification deepening for HIGH
   findings]
3. [Decision C — typically: schedule sister-MS revalidation in [N] months]
```

### 2. Findings Table (Markdown)

The findings table is the main artefact for human review. One row per finding.

```
| ID | Category | Severity | Directive Article | NIM Article | Description | Authorised? | Burden Tier | Sister-MS Position | Recommendation |
|----|----------|----------|-------------------|-------------|-------------|-------------|-------------|---------------------|----------------|
| GP-001 | 1 (scope) | HIGH | Art. 1a(1)(a) Dir. 2013/34/EU as amended (CELEX 32022L2464) | § 289b HGB (BGBl. I [year]) | NIM extends CSRD reporting to mid-sized unlisted undertakings (>500 employees) ahead of EU phase-in. | YES (recital authorises stricter rules in some MS contexts) [VERIFY] | HIGH (≈4,500 entities; €100m–€300m recurring delta DE) | Outlier high — FR, IT, NL track directive scope. | Form B narrowing scope OR Form C review clause [GOV persona]. |
| GP-002 | 2 (additional) | MEDIUM | Art. 22 Dir. 2011/61/EU (CELEX 32011L0061) | [NIM Art.] | NIM mandates quarterly portfolio-transparency reporting on top of directive annual cadence. | YES | MEDIUM | Cluster — SE, DK, FI same. | Form C review clause. |
| GP-003 | 3 (stricter deadline) | HIGH | Art. 23 Dir. (EU) 2022/2555 (CELEX 32022L2555) | [NIM Art.] | NIM shortens NIS2 early-warning deadline from 24h to 12h. | YES | HIGH (sector-economy-wide, ≈12,000 entities). | Singleton — only this MS in EU-27. | Form A revoke and revert to 24h. |
| GP-004 | 4 (non-use) | MEDIUM | Art. 3 Dir. 2011/61/EU (CELEX 32011L0061) | (no NIM provision — non-use of derogation) | MS declines AIFMD sub-threshold exemption; ≈600 sub-threshold managers in full AIFMD scope. | YES | MEDIUM (€10m–€30m recurring delta MS-X). | Cluster — SK, EE same. | Form B activate sub-threshold derogation. |
| GP-005 | 5 (review) | LOW | Art. 40 Dir. (EU) 2022/2555 (CELEX 32022L2555) | (no NIM provision) | NIM omits parallel national review obligation. | (n/a) | LOW (one-off legislative) | Pattern — most MS omit. | Form C add review clause. |
```

Each row links to a JSON object (next section) and to a Glass Box decision
sequence (later section).

### 3. JSON Findings Schema

```json
{
  "$schema": "https://legalcode.example/schema/eu-gold-plating-findings/v1.json",
  "metadata": {
    "directive": {
      "short_title": "CSRD",
      "full_title": "Directive (EU) 2022/2464 of the European Parliament and of the Council of 14 December 2022 amending Regulation (EU) No 537/2014, Directive 2004/109/EC, Directive 2006/43/EC and Directive 2013/34/EU, as regards corporate sustainability reporting",
      "celex": "32022L2464",
      "eli": "http://data.europa.eu/eli/dir/2022/2464/oj",
      "oj_reference": "OJ L 322, 16.12.2022, p. 15"
    },
    "member_state": {
      "name": "Germany",
      "iso3166": "DE",
      "pillar": "EU"
    },
    "nim": [
      {
        "short_title": "CSRD-Umsetzungsgesetz",
        "official_journal": "BGBl. I [year, page]",
        "eli": "http://data.europa.eu/eli/[…]",
        "entry_into_force": "[YYYY-MM-DD]",
        "consolidated_version": "[YYYY-MM-DD]",
        "verify_status": "VERIFY"
      }
    ],
    "assessment_date": "[YYYY-MM-DD]",
    "operating_mode": 2,
    "persona": "company",
    "burden_quantification_depth": "scm_lite",
    "legalcode_mcp_status": "connected",
    "language_version_basis": "DE",
    "language_reconciliation_done": ["DE", "EN", "FR"]
  },
  "findings": [
    {
      "id": "GP-001",
      "category": 1,
      "category_label": "scope_extension",
      "severity": "HIGH",
      "directive_provision": {
        "article": "1a(1)(a)",
        "text_short": "[directive minimum scope statement]",
        "ms_option": false,
        "max_harmonisation": false,
        "min_harmonisation_clause_authorising_stricter": true,
        "min_harmonisation_clause_citation": "Recital [N] / Art. [N]",
        "celex": "32022L2464"
      },
      "nim_provision": {
        "article": "§ 289b HGB",
        "text_short": "[NIM scope statement]",
        "official_journal": "BGBl. I [year, page]",
        "eli": "http://data.europa.eu/eli/[…]"
      },
      "delta": {
        "field": "addressees",
        "directive_addressees": "Large undertakings + listed SMEs (phased)",
        "nim_addressees": "Large undertakings + listed SMEs + non-listed mid-cap (>500 employees)",
        "additional_addressees_count_estimated": 4500,
        "data_source": "Eurostat NACE 64–82 [VERIFY year]"
      },
      "authorised": true,
      "authorisation_basis": "Recital [N] minimum-harmonisation clause",
      "burden": {
        "methodology": "scm_lite",
        "directive_minimum_recurring_eur": 0,
        "nim_recurring_eur": 200000000,
        "delta_recurring_eur": 200000000,
        "delta_recurring_currency": "EUR",
        "delta_recurring_confidence": "POSSIBLE",
        "one_off_implementation_eur": 50000000,
        "one_off_implementation_confidence": "POSSIBLE",
        "qualitative_tier": "HIGH",
        "burden_per_entity_recurring_eur": 44000,
        "data_source": "Eurostat compliance-cost survey 2024 [VERIFY]"
      },
      "sister_ms_position": {
        "score": "outlier_high",
        "comparators": [
          {
            "ms": "FR",
            "position": "tracks_directive",
            "nim_citation": "ord. n° 2023-1142 du 6 décembre 2023 [VERIFY]"
          },
          {
            "ms": "IT",
            "position": "tracks_directive",
            "nim_citation": "D.Lgs. 125/2024 [VERIFY]"
          },
          {
            "ms": "NL",
            "position": "tracks_directive",
            "nim_citation": "Implementatiewet richtlijn duurzaamheidsrapportering [VERIFY]"
          }
        ],
        "matrix_source": "legalcode-eu-transposition-tracker",
        "matrix_freshness_date": "[YYYY-MM-DD]"
      },
      "subsidiarity_proportionality": {
        "tool_28_applied": true,
        "stated_objective": "Wider corporate-sustainability transparency in DE economy",
        "necessity_test": "FAIL — directive scope plus voluntary national reporting could achieve substantially the same objective",
        "proportionality_test": "FAIL — burden disproportionate to marginal benefit at 4,500 additional entities",
        "subsidiarity_test": "INDETERMINATE — case for EU-level action exists but EU phase-in already addresses it",
        "result": "DISPROPORTIONATE"
      },
      "recommendation": {
        "form": "B_narrowing_scope_OR_C_review_clause",
        "rationale_short": "Authorised gold-plate, but disproportionate per Tool #28; either narrow to directive scope or add 5-year UK BIS-style review.",
        "draft_amendment_text": "In § 289b HGB, the words 'sowie weitere Unternehmen mit mehr als 500 Beschäftigten' are deleted, OR a new § 289b(N) HGB is added: 'Diese Vorschrift wird fünf Jahre nach Inkrafttreten überprüft. ...'",
        "persona_specific_alternatives": {
          "company": "Extend data-collection boundary to all DE-resident subsidiaries ≥500 employees; align reporting calendar with DE fiscal year; engage external assurance.",
          "federation": "Joint position with BDA / BDI requesting Bundestag amendment; benchmark vs. FR / IT / NL who track directive scope."
        }
      },
      "infringement_routing": {
        "route_to_tracker": false,
        "rationale": "Authorised gold-plating; no max-harmonisation breach"
      },
      "confidence": "LIKELY",
      "verify_flags": [
        "Final adopted DE text against BGBl",
        "Directive recital authorising stricter rules — exact recital number",
        "NIM scope-clause comparator FR / IT / NL"
      ],
      "glass_box_decision_sequence_ref": "GB-GP-001"
    }
  ],
  "aggregate": {
    "intensity_overall": "HIGH",
    "by_category": { "1": 1, "2": 1, "3": 1, "4": 1, "5": 1 },
    "by_severity": { "SEVERE": 0, "HIGH": 2, "MEDIUM": 2, "LOW": 1 },
    "aggregate_recurring_delta_eur": 230000000,
    "aggregate_one_off_eur": 75000000,
    "aggregate_burden_confidence": "POSSIBLE"
  }
}
```

### 4. AKN4EU Stub

Each finding is expressed as a `<doc>` annotation referencing both the directive
ELI and the NIM ELI. The AKN4EU subschema for cross-document annotations uses
`<doc>` with embedded `<references>` blocks.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<akomaNtoso xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <doc name="goldPlatingFindings">
    <meta>
      <identification source="#legalcode">
        <FRBRWork>
          <FRBRthis value="/akn/eu/doc/goldPlatingFindings/2026/csrd-de"/>
          <FRBRuri value="/akn/eu/doc/goldPlatingFindings/2026/csrd-de"/>
          <FRBRdate date="2026-04-28" name="Generation"/>
          <FRBRauthor href="#legalcode"/>
          <FRBRcountry value="eu"/>
        </FRBRWork>
        <FRBRExpression>
          <FRBRthis value="/akn/eu/doc/goldPlatingFindings/2026/csrd-de/eng@2026-04-28"/>
          <FRBRuri value="/akn/eu/doc/goldPlatingFindings/2026/csrd-de/eng@2026-04-28"/>
          <FRBRdate date="2026-04-28" name="Generation"/>
          <FRBRauthor href="#legalcode"/>
          <FRBRlanguage language="eng"/>
        </FRBRExpression>
        <FRBRManifestation>
          <FRBRthis value="/akn/eu/doc/goldPlatingFindings/2026/csrd-de/eng@2026-04-28.xml"/>
          <FRBRuri value="/akn/eu/doc/goldPlatingFindings/2026/csrd-de/eng@2026-04-28.xml"/>
          <FRBRdate date="2026-04-28" name="Generation"/>
          <FRBRauthor href="#legalcode"/>
        </FRBRManifestation>
      </identification>
      <references source="#legalcode">
        <TLCDocument eId="ref_directive_csrd"
                     href="http://data.europa.eu/eli/dir/2022/2464/oj"
                     showAs="Directive (EU) 2022/2464 (CSRD)"/>
        <TLCDocument eId="ref_nim_de"
                     href="http://data.europa.eu/eli/[…CSRD-UmsG…]"
                     showAs="CSRD-Umsetzungsgesetz (DE)"/>
        <TLCConcept eId="cat_scope_extension"
                    href="/ontology/goldplating/category/scope-extension"
                    showAs="Gold-plating category 1 — Scope extension"/>
        <TLCOrganization eId="org_legalcode"
                         href="/ontology/legalcode"
                         showAs="Legalcode"/>
      </references>
    </meta>
    <mainBody>
      <hcontainer name="finding" eId="finding_GP-001">
        <num>GP-001</num>
        <heading>CSRD scope extension to mid-cap unlisted undertakings (DE)</heading>
        <content>
          <p>The NIM at <ref href="#ref_nim_de">§ 289b HGB</ref> extends the CSRD
          reporting obligation to undertakings with more than 500 employees, ahead
          of the phase-in scope established by <ref href="#ref_directive_csrd">
          Article 1a(1)(a) of Directive (EU) 2022/2464</ref>.</p>
          <p>Classification: <ref href="#cat_scope_extension">category 1 — scope
          extension</ref>. Severity: HIGH. Authorised: YES (per recital
          authorising stricter rules). Sister-MS position: outlier high —
          FR / IT / NL track the directive scope.</p>
          <p>Recommendation: Form B (narrow scope to directive minimum) or Form C
          (add 5-year UK BIS-style review clause).</p>
        </content>
      </hcontainer>
      <!-- additional <hcontainer> blocks per finding -->
    </mainBody>
  </doc>
</akomaNtoso>
```

The structure validates against the AKN4EU `doc` subschema. Replace `[…CSRD-UmsG…]`
with the actual ELI when generating output for a real NIM. The `TLCConcept`
references for the gold-plating ontology terms can be hosted in a stable Legalcode
ontology namespace; if that namespace is not yet published, mark the URI
provisional with `[VERIFY ontology URI]`.

### 5. LegalRuleML Stub

Each finding is expressed as a `<lrml:Constitutive>` assertion that the NIM
provision imposes obligation O₂; the directive provision imposes obligation O₁;
and O₂ ⊃ O₁ (the over-coverage logic). LegalRuleML's `Constitutive` block is the
appropriate container because the assertion is a status / classification, not a
direct deontic command.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<lrml:LegalRuleML
  xmlns:lrml="http://docs.oasis-open.org/legalruleml/ns/v1.0/"
  xmlns:ruleml="http://ruleml.org/spec"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <lrml:Context key="ctx_csrd_de_GP-001">
    <lrml:appliesSource>
      <lrml:Source key="src_directive_csrd"
        sameAs="http://data.europa.eu/eli/dir/2022/2464/oj"/>
      <lrml:Source key="src_nim_de_csrdumsg"
        sameAs="http://data.europa.eu/eli/[…CSRD-UmsG…]"/>
    </lrml:appliesSource>
  </lrml:Context>

  <lrml:Constitutive key="finding_GP-001">
    <lrml:Paraphrase>
      NIM provision § 289b HGB imposes obligation O₂ (CSRD reporting on
      undertakings with ≥500 employees). Directive provision Article 1a(1)(a)
      Directive (EU) 2022/2464 imposes obligation O₁ (CSRD reporting on large
      undertakings + listed SMEs, phased). O₂ ⊃ O₁ — the NIM obligation is a
      proper superset of the directive obligation: every entity bound by the
      directive is also bound by the NIM, and additional entities are bound by
      the NIM only.
    </lrml:Paraphrase>

    <ruleml:Implies>
      <ruleml:if>
        <ruleml:And>
          <ruleml:Atom>
            <ruleml:Rel>boundBy</ruleml:Rel>
            <ruleml:Var>entity</ruleml:Var>
            <ruleml:Ind>directive_csrd_art_1a_1_a</ruleml:Ind>
          </ruleml:Atom>
        </ruleml:And>
      </ruleml:if>
      <ruleml:then>
        <ruleml:Atom>
          <ruleml:Rel>boundBy</ruleml:Rel>
          <ruleml:Var>entity</ruleml:Var>
          <ruleml:Ind>nim_de_hgb_289b</ruleml:Ind>
        </ruleml:Atom>
      </ruleml:then>
    </ruleml:Implies>

    <ruleml:Implies>
      <ruleml:if>
        <ruleml:And>
          <ruleml:Atom>
            <ruleml:Rel>boundBy</ruleml:Rel>
            <ruleml:Var>entity</ruleml:Var>
            <ruleml:Ind>nim_de_hgb_289b</ruleml:Ind>
          </ruleml:Atom>
          <ruleml:Atom>
            <ruleml:Rel>employeeCount</ruleml:Rel>
            <ruleml:Var>entity</ruleml:Var>
            <ruleml:Var>n</ruleml:Var>
          </ruleml:Atom>
          <ruleml:Atom>
            <ruleml:Rel>greaterThanOrEqual</ruleml:Rel>
            <ruleml:Var>n</ruleml:Var>
            <ruleml:Ind>500</ruleml:Ind>
          </ruleml:Atom>
        </ruleml:And>
      </ruleml:if>
      <ruleml:then>
        <ruleml:Atom>
          <ruleml:Rel>obligedToReport</ruleml:Rel>
          <ruleml:Var>entity</ruleml:Var>
          <ruleml:Ind>esrs_full_set</ruleml:Ind>
        </ruleml:Atom>
      </ruleml:then>
    </ruleml:Implies>

    <lrml:hasClassification>
      <lrml:Classification>
        <lrml:hasCategory>category_1_scope_extension</lrml:hasCategory>
        <lrml:hasSeverity>HIGH</lrml:hasSeverity>
        <lrml:hasAuthorisation>authorised</lrml:hasAuthorisation>
      </lrml:Classification>
    </lrml:hasClassification>
  </lrml:Constitutive>

  <!-- additional <lrml:Constitutive> blocks per finding -->

</lrml:LegalRuleML>
```

The `<ruleml:Implies>` blocks express the over-coverage logic in conditional form:
the first asserts that everything bound by the directive is also bound by the NIM
(supersetness); the second asserts that the NIM additionally binds entities that
satisfy the NIM-specific size threshold. Reasoners (e.g. SWRL-aware engines or
OASIS LegalRuleML reference implementations) can derive the gold-plating
implication directly. The `<lrml:Classification>` block carries the analyst's
category and severity assignment, which is non-deductive metadata.

### 6. Glass Box Audit Trail

The Glass Box is a YAML-formatted decision sequence reproducing every
classification, burden quantification, sister-MS check, and remediation choice
in deterministic form. It is the audit trail consumed by qualified counsel,
ministry budget reviewers, and regulator staff in formal review.

```yaml
glass_box:
  schema_version: "1.0"
  generated_at: "2026-04-28T00:00:00Z"
  generator: "legalcode-eu-gold-plating-detector v[skill version]"
  legalcode_mcp_status: "Connected — research file at /tmp/legalcode-gold-plating-research.md"

  inputs_resolved:
    directive_celex: "32022L2464"
    directive_eli: "http://data.europa.eu/eli/dir/2022/2464/oj"
    directive_consolidated_version: "[YYYY-MM-DD] [VERIFY]"
    member_state: "DE"
    nim_eli: "[…CSRD-UmsG ELI …]"
    nim_official_journal: "BGBl. I [year, page]"
    nim_entry_into_force: "[YYYY-MM-DD]"
    obligation_register_source: "legalcode-eu-directive-analyzer output, file [path]"
    correlation_table_source: "legalcode-eu-correlation-table-builder output, file [path]"
    conformity_assessment_source: "legalcode-eu-conformity-assessment output, file [path]"
    over_coverage_rows_count: 7
    operating_mode: 2
    persona: "company"
    burden_depth: "scm_lite"
    language_version_basis: "DE"
    language_reconciliation_done: ["DE", "EN", "FR"]

  per_finding_decisions:
    - id: "GP-001"
      sequence:
        - step: "Step 4a — identify EU minimum"
          decision: "Article 1a(1)(a) Directive (EU) 2022/2464 binds large undertakings + listed SMEs (phased)"
          source: "Directive consolidated text [VERIFY consolidation date]"
        - step: "Step 4b — identify NIM excess"
          decision: "§ 289b HGB binds large undertakings + listed SMEs + non-listed mid-cap >500 employees"
          source: "BGBl. I [year, page]"
        - step: "Step 4c — classify"
          decision: "Category 1 — scope extension"
          rationale: "NIM extends scope to addressees outside directive's stated personal scope"
          discretion_check_step_1: "ms_option=false on Article 1a(1)(a) — not an MS option provision"
          discretion_check_step_2: "min-harmonisation clause authorising stricter rules — present (recital [N])"
          discretion_check_step_3: "max-harmonisation clause prohibiting stricter rules — absent"
          discretion_check_step_4: "translation reconciliation done across DE / EN / FR"
        - step: "Step 4d — severity"
          decision: "HIGH"
          rationale: "Sector-economy-wide addressees, recurring action, recital-permitted but DE in bottom quartile of EU-27 stringency on this provision"
        - step: "Step 5 — burden"
          decision: "SCM-lite estimate: recurring delta €200m DE annually; one-off €50m"
          methodology: "scm_lite"
          inputs:
            time_per_action_hours: 80
            hourly_cost_eur: 100
            frequency_per_year: 1
            additional_addressees: 4500
            overhead_factor: 1.4
          confidence: "POSSIBLE"
          data_sources:
            ["Eurostat NACE 64–82", "BDA compliance-cost survey 2024 [VERIFY]"]
        - step: "Step 6 — sister-MS"
          decision: "outlier_high — FR / IT / NL track directive scope"
          matrix_source: "legalcode-eu-transposition-tracker"
          matrix_freshness_date: "[YYYY-MM-DD]"
        - step: "Step 7 — Tool #28"
          decision: "DISPROPORTIONATE"
          necessity: "FAIL"
          proportionality: "FAIL"
          subsidiarity: "INDETERMINATE"
        - step: "Step 8 — remediation"
          decision: "Form B (narrowing scope) OR Form C (review clause); persona = company → operational adjustments register populated"
        - step: "Step 9 — emit"
          decision: "Findings table row + JSON object + AKN4EU <hcontainer> + LegalRuleML <Constitutive>"
        - step: "Step 10 — self-interrogation"
          pass_1_specificity: "PASS — directive Art. 1a(1)(a) and NIM § 289b HGB cited"
          pass_2_discretion: "PASS — ms_option=false, max-harmonisation absent, authorised by recital"
          pass_3_sister_ms: "PASS — outlier_high confirmed against tracker"

      verify_flags:
        - "Final adopted DE text against BGBl"
        - "Directive recital authorising stricter rules — exact recital number"
        - "Sister-MS comparator NIMs"

      confidence_overall: "LIKELY"
      infringement_routing: false

  aggregate:
    findings_total: 5
    by_category: { "1": 1, "2": 1, "3": 1, "4": 1, "5": 1 }
    by_severity: { "SEVERE": 0, "HIGH": 2, "MEDIUM": 2, "LOW": 1 }
    aggregate_recurring_delta_eur: 230000000
    aggregate_one_off_eur: 75000000
    aggregate_burden_confidence: "POSSIBLE"
    runtime_self_interrogation_failures: 0
```

The Glass Box must be reproducible: given the same inputs and the same skill
version, the same Glass Box must emerge. Mark sections regenerated since the
last run with their previous and current decisions in a `revision_log` block
when the skill is run incrementally.

### 7. Worked Example — CSRD scope extension (Germany)

**Inputs.** Directive: CSRD (Directive (EU) 2022/2464, CELEX 32022L2464, OJ L
322, 16.12.2022, p. 15) amending Directive 2013/34/EU. Member State: Germany.
NIM: CSRD-Umsetzungsgesetz [VERIFY full short title and BGBl reference].
Persona: Company (multinational with DE-resident subsidiaries). Operating mode:
2 (full burden quantification).

**Comparison table — directive minimum vs. NIM:**

| Field              | Directive (Art. 1a(1)(a) Dir. 2013/34/EU as amended) | NIM (§ 289b HGB)                                                     | Delta                        |
| ------------------ | ---------------------------------------------------- | -------------------------------------------------------------------- | ---------------------------- |
| Addressees         | Large undertakings + listed SMEs (phased)            | Large undertakings + listed SMEs + non-listed mid-cap >500 employees | +≈4,500 entities DE [VERIFY] |
| Threshold          | Art. 3(4) Dir. 2013/34/EU size class                 | §§ 267–267a HGB size class extended                                  | Lower employee threshold     |
| Reporting standard | ESRS (delegated act)                                 | ESRS (delegated act)                                                 | none                         |
| Assurance          | Art. 34a (limited assurance)                         | Art. 34a (limited assurance)                                         | none                         |
| Sanctions          | Art. 51 Dir. 2013/34/EU minimum                      | National admin sanctions                                             | none [VERIFY]                |
| Review             | Commission review (Art. [N])                         | (no parallel national review)                                        | category-5 secondary finding |

**Classification.** Category 1 — scope extension; authorised gold-plating
(min-harmonisation recital permits stricter scope) [VERIFY recital number].
Severity: HIGH. ms_option=false on scope; max-harmonisation absent; translation
reconciliation done across DE / EN / FR.

**Burden estimate.** SCM-lite (illustrative): 80 hours per entity per cycle
× €100 fully-loaded compliance hourly × 1 cycle/year × 4,500 additional
entities × 1.4 overhead ≈ **€50m per year** floor; richer treatment with ESRS
data-collection and assurance cost reaches **€200m per year** ceiling. Range:
€50m–€200m DE annually (POSSIBLE). One-off ≈€50m DE on €11k per-entity
implementation [VERIFY BDA survey].

**Sister-MS.** FR (ord. n° 2023-1142 du 6 décembre 2023), IT (D.Lgs. 125/2024),
NL (Implementatiewet richtlijn duurzaamheidsrapportering) all track the
directive scope [VERIFY all three]. Position: outlier_high — DE alone in the
top quartile.

**Tool #28.** Necessity FAIL (voluntary national framework could substitute);
proportionality FAIL (€50m–€200m disproportionate to marginal disclosure
benefit on entities already inside LkSG supply-chain due diligence);
subsidiarity INDETERMINATE (EU phase-in addresses mid-caps by Year 3). Result:
**DISPROPORTIONATE.**

**Remediation (persona = company).** Operational adjustments register: extend
ESRS data-collection boundary to all DE-resident subsidiaries ≥500 employees;
align reporting calendar with DE fiscal year; engage external assurance under
Art. 34a; build reconciliation control between consolidated-group ESRS report
and DE supplementary subsidiary-level reports; forecast DE-specific assurance
cost in 2025–2026 budgets.

_Government-persona alternative:_ Form B amendment "In § 289b HGB, the words
'sowie weitere Unternehmen mit mehr als 500 Beschäftigten' are deleted" or
Form C 5-year UK BIS-style review clause. _Federation-persona alternative:_
joint position with BDA / BDI requesting Bundestag amendment narrowing § 289b
HGB scope; benchmark vs. FR / IT / NL.

**Self-interrogation.** Pass 1 (specificity), Pass 2 (discretion), Pass 3
(sister-MS) all PASS.

**All four output formats above are populated for this finding**: Markdown row
GP-001 (§ 2), JSON `findings[0]` (§ 3), AKN4EU `<hcontainer eId="finding_GP-001">`
(§ 4), LegalRuleML `<lrml:Constitutive key="finding_GP-001">` (§ 5), Glass Box
`per_finding_decisions[id=GP-001]` (§ 6).

[VERIFY: the precise scope of the German CSRD-Umsetzungsgesetz against the
directive's phased timeline must be confirmed against the final adopted BGBl
text and against current Linklaters / Bird & Bird trackers. The pattern is
consistent with the HLG (2014) categorisation, the CFA Society Poland 2024
capital-markets analogue, and the Better Regulation Toolbox 2023
proportionality test, but the specific German CSRD scope decision should be
confirmed before the worked example is presented in client work.]

---

## Localization Notes

When adapting this skill for a specific Member State or jurisdiction:

1. **Identify the national anti-gold-plating regime** (if any) and cite its
   statute / framework in the Step 8 remediation drafting templates. The most
   developed regimes: Austria (Anti-Gold-Plating-Gesetz 2019), France (2019
   sur-transposition cleanup bill), Germany (NKR cost-opinion practice), the
   Netherlands (ATR), Sweden (Tillväxtverket / Regelrådet). For other MS,
   identify the equivalent better-regulation body and methodology.

2. **Confirm the NIM short title and ELI** against the national official
   journal. Each MS uses different naming conventions (BGBl. for Germany, JORF
   for France, BOE for Spain, GU for Italy, Stb. for the Netherlands, Sb. for
   Sweden, RIS for Austria, etc.). Mark all unconfirmed citations [VERIFY].

3. **Verify the EU-pillar / EFTA-pillar status** of the act for the MS. EU-27
   are bound directly via Art. 288 TFEU; IS / NO / LI are bound via JCD under
   Art. 102 EEA only when the JCD has been adopted and any Art. 103 EEA
   constitutional reservations resolved.

4. **Cross-check the multilingual versions** of the directive. Use IATE for
   terminology consistency. Apply CILFIT C-283/81 reasoning for any wording-
   sensitive finding.

5. **Verify the burden methodology**. NKR-style cost opinions exist for federal
   bills only. Länder-level transposition or Lander-level burden does not
   appear in NKR opinions. Equivalent regional / sub-national mechanisms may
   not exist; flag this gap in the Glass Box.

6. **Note the local language version of the gold-plating taxonomy**. The five-
   category taxonomy is often translated with slight variations:
   - DE: "Goldplating" / "über die EU-Vorgaben hinausgehende nationale
     Regelungen"
   - FR: "sur-transposition"
   - IT: "_gold plating_" / "_sovra-trasposizione_"
   - ES: "_sobre-transposición_" / "_sobrerregulación_"
   - NL: "kop-op" / "_gold plating_"
   - SE: "_gold plating_" / "_övergödning_" (rare)

   Use the local term in the Markdown output for native readability where the
   user's persona is government.

7. **Cross-reference the Single Market Scoreboard / Internal Market Scoreboard**
   for the latest transposition-status data on the directive in the named MS.

---

## Provenance

Created by Legalcode (2026-04-28). Original synthesis based on:

- Commission High Level Group on Administrative Burden, _Conclusions and
  Recommendations on Gold-Plating_ (2014):
  https://ec.europa.eu/futurium/en/system/files/ged/hlg_16_0008_00_conclusions_and_recomendations_on_goldplating_final.pdf
  — the operative Commission definition of gold-plating, source of the
  five-category taxonomy.
- UK Department for Business, Innovation and Skills, _Gold-Plating Review:
  The Operation of the Transposition Principles in the Government's Guiding
  Principles for EU Legislation_ (2013):
  https://assets.publishing.service.gov.uk/media/5a7a30e3e5274a34770e4e5e/bis-13-683-gold-plating-review-the-operation-of-the-transposition-principles-in-the-governments-guiding-principles-for-eu-legislation.pdf
  — "copy-out" principle and 5-year review template.
- Austrian _Anti-Gold-Plating-Gesetz 2019_ (BGBl. I Nr. 46/2019) — explicit
  statutory anti-gold-plating measure, model for federal cleanup omnibus.
- French _Projet de loi portant suppression de sur-transpositions de directives
  européennes en droit français_ (2019) — horizontal cleanup statute, model for
  ministry-led sectoral cleanup.
- CFA Society Poland, _Gold-Plating in EU Capital Markets_ (2024):
  https://cfapoland.org/application/media/images/pdf_pliki/2024-gold-plating-in-eu-capital-markets.pdf
  — concrete examples across MiFID II, Prospectus, AIFMD.
- Epicenter, _How to identify and avoid gold-plating EU regulations_ (2024):
  https://www.epicenternetwork.eu/wp-content/uploads/2024/01/How-to-identify-avoid-gold-plating.pdf
  — practical heuristics.
- German _Nationaler Normenkontrollrat_ (NKR) cost-opinion methodology — used
  for transposition cost analysis.
- European Commission, _Better Regulation Toolbox 2023_, Chapter 4
  (Compliance, Implementation and Preparing Proposals):
  https://commission.europa.eu/document/download/a21336e2-2a7c-43d2-bb35-d4eee7aa4cd3_en?filename=BRT-2023-Chapter+4-Compliance+implementation+and+preparing+proposals_0.pdf
  Tool #28 (proportionality and subsidiarity).
- Standard Cost Model Network — _International Standard Cost Model Manual_.
- Art. 288 TFEU (instrument hierarchy):
  https://eur-lex.europa.eu/eli/treaty/tfeu_2008/art_288/oj/eng
- Art. 258 TFEU (infringement procedure); Art. 260(2)/(3) TFEU (penalty
  payments); _Commission v Belgium_, Case C-543/17, ECLI:EU:C:2019:573.
- Art. 7 EEA, Art. 102 EEA, Art. 103 EEA (EEA incorporation framework).
- Art. 31 SCA (ESA monitoring mandate).
- Reg. 1/1958 (EU language regime); CILFIT (Case C-283/81, ECLI:EU:C:1982:335);
  Codan (Case C-236/97, ECLI:EU:C:1998:208); EMU Tabac (Case C-296/95,
  ECLI:EU:C:1998:152).
- Akoma Ntoso (OASIS LegalDocML 1.0, 2018) — AKN4EU subschema.
- LegalRuleML (OASIS, 2021):
  https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/
- ELI (European Legislation Identifier):
  https://eur-lex.europa.eu/eli-register/technical_information.html
- ECLI (European Case Law Identifier).
- EUR-Lex N-Lex (national execution measures):
  https://eur-lex.europa.eu/collection/n-law/mne.html
- Single Market Scoreboard:
  https://single-market-scoreboard.ec.europa.eu/
- ESA Internal Market Scoreboard: https://www.efta.int/
- EEA-Lex: https://www.efta.int/eealaw

Worked example draws on the German CSRD-Umsetzungsgesetz transposition pattern
as discussed in the Linklaters CSRD tracker and corroborated against the CFA
Society Poland 2024 capital-markets gold-plating analogue. The specific
scope-extension claim must be verified against the final adopted BGBl text and
the current Linklaters / Bird & Bird trackers before publication. The pattern is
consistent with the literature; the verification flag is on the precise factual
description.

All statutory and regulatory references carry hallucination risk and should be
verified against authoritative sources (EUR-Lex, CURIA, national official
journals, EFTA Court InfoCuria-equivalent, EEA-Lex) before use in regulatory
submissions, infringement proceedings, or board reporting.

Sibling skills in the seven-skill EU Legislative Compliance suite consume and
produce shared artefacts via the [shared EU legislative-data pack](references/eu-legislative-data/);
see the Sibling Skills subsection of Purpose and Scope.
