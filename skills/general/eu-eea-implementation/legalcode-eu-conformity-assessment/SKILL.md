---
name: legalcode-eu-conformity-assessment
description: Runs the substantive, per-provision conformity assessment of a Member State's National Implementing
  Measures (NIM) against the operative obligations of an EU directive.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Runs the substantive, per-provision conformity assessment of a Member State's National Implementing Measures (NIM) against the operative obligations of an EU directive. For each obligation extracted by `legalcode-eu-directive-analyzer` and mapped by `legalcode-eu-correlation-table-builder`, this skill applies the Commission's published methodology — the Better Regulation Toolbox 2023 (Chapter 4: Compliance, Implementation and Preparing Proposals) and the conformity-assessment template used in published Commission tenders such as the ECN+ Directive (Directive (EU) 2019/1, CELEX 32019L0001) tender (Belgian publication reference 765714) — to classify each provision as correctly transposed, partially transposed, incorrectly transposed, or not transposed. Anchors the binding-as-to-result test in Article 288(3) TFEU and the duty of sincere cooperation in Article 4(3) TEU. Operationalises the case-law standard for incomplete transposition (*Commission v Germany*, Case C-543/09, ECLI:EU:C:2010:778), substantive non-conformity (*Commission v Italy*, Case C-456/03, ECLI:EU:C:2005:388), the *Marleasing* doctrine of conforming interpretation (Case C-106/89, ECLI:EU:C:1990:395), the direct-effect line (*Becker* C-8/81, ECLI:EU:C:1982:7; *Faccini Dori* C-91/92, ECLI:EU:C:1994:292), and Article 260(3) TFEU first-referral penalties as applied in *Commission v Belgium*, Case C-543/17, ECLI:EU:C:2019:573. Reconciles the 24 equally authentic language versions per *CILFIT* (Case C-283/81), *Codan* (Case C-236/97), and *EMU Tabac* (Case C-296/95). Produces a Better-Regulation-Toolbox-format conformity report (Markdown), a machine-readable JSON conformity schema, an AKN4EU `<judgment>` stub, a LegalRuleML `<lrml:Constitutive>` rule set, and a Glass Box audit trail. Supports four operating modes — government self-assessment, Commission-view comparative review, law-firm advisory, and company impact analysis — and covers both the EU pillar (Commission infringement risk) and the EEA pillar (ESA assessment under Article 31 SCA). Worked example: NIS2 Article 21(2)(a) against the German NIS2UmsuCG transposition. Jurisdictional scope: EU-27 and EEA-EFTA (Iceland, Liechtenstein, Norway).


# Legalcode EU Conformity Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted EU directive
> conformity assessment. It does not constitute legal advice and does not create
> an attorney-client relationship. All outputs should be reviewed by qualified
> legal counsel licensed in the relevant jurisdictions before use. This skill
> does not replace formal legal review by qualified EU and Member State counsel.
> It produces a structured framework to support a human-led review — not a
> substitute for one.
> Citations to EU directives, regulations, CJEU/EFTA Court judgments, and
> Member State implementing measures must be verified against authoritative
> sources (EUR-Lex, CURIA, national official journals) before use in regulatory
> submissions, infringement proceedings, or board reporting. EU law evolves
> continuously; transposition status, infringement procedures, and consolidated
> text versions change frequently. The 24 official EU language versions of
> every act are equally authentic; reconcile divergent versions before relying
> on any single language for a definitive interpretation (CILFIT C-283/81;
> Codan C-236/97; EMU Tabac C-296/95).

## Purpose and Scope

This skill performs the substantive conformity check that sits at the heart of
the Commission's directive lifecycle work. Notification is not the same as
conformity: a Member State that has notified its National Implementing
Measures (NIM) and rendered the Single Market Scoreboard "transposition
deficit" green may still be subject to infringement under Article 258 TFEU
for **incorrect transposition** if the substance of the NIM diverges from the
obligations the directive imposes.

The test rests on the binding character of directives under Article 288(3)
TFEU (binding "as to the result to be achieved", leaving form and method to
the Member State), underwritten by the duty of sincere cooperation in
Article 4(3) TEU. Every operative provision defines a result; this skill
answers, provision-by-provision, whether the NIM achieves it.

The Commission's published methodology — Better Regulation Toolbox 2023,
Chapter 4 (Compliance, Implementation and Preparing Proposals), and the
conformity-assessment templates used in Commission outsourcing tenders such
as the ECN+ Directive (EU) 2019/1 conformity assessment (Belgian publication
reference 765714) — defines a four-verdict taxonomy: **correctly transposed**,
**partially transposed**, **incorrectly transposed**, **not transposed**.
This skill operationalises that taxonomy in a deterministic, evidence-anchored,
audit-trailable workflow. Where a NIM is ambiguous, the skill applies the
_Marleasing_ doctrine (Case C-106/89, ECLI:EU:C:1990:395) before reaching a
non-conformity verdict; where an obligation is unconditional and sufficiently
precise, it is flagged direct-effect-ready under the _Becker_ / _Faccini
Dori_ line.

**Covers:**

- Per-obligation substantive conformity test (scope, addressee, operative
  content, sanction architecture, derogation use)
- Better-Reg-Toolbox four-verdict taxonomy (correct / partial / incorrect /
  not transposed)
- Multi-language reconciliation across the 24 authentic versions (CILFIT
  methodology at conformity stage)
- _Marleasing_-conforming interpretation salvage analysis
- Direct-effect readiness flag (vertical, unconditional, sufficiently
  precise)
- Operational-equivalence test (different mechanism, equivalent result)
- Conformity deficit aggregation (Single Market Scoreboard methodology)
- EEA pillar conformity (ESA Art. 31 SCA, EFTA Court cross-reference)
- Remediation recommendations per finding (amend NIM, interpretive guidance,
  withdraw, etc.)
- Standards-based outputs: Markdown, JSON, AKN4EU `<judgment>`, LegalRuleML
  `<lrml:Constitutive>`
- Glass Box YAML audit trail of every verdict, evidence chain, and language
  reconciliation

**Does not:**

- Extract the obligation register (skill B), build the implementation matrix
  (skill C), or produce the correlation table (skill D)
- Flag national over-implementation (skill F), track JCD EEA incorporation
  (skill G), or score TFEU 258/260 procedural risk (skill H)
- Provide formal legal advice or substitute for qualified Member State
  counsel
- Guarantee any particular outcome in an infringement procedure or
  preliminary reference

### Sibling Skills in the Suite

This skill is part of the seven-skill EU Legislative Compliance suite.

- **Consumes**: obligation register from `legalcode-eu-directive-analyzer`
  (skill B); per-MS implementation matrix from
  `legalcode-eu-transposition-tracker` (skill C); correlation table from
  `legalcode-eu-correlation-table-builder` (skill D)
- **Produces**: per-obligation conformity verdict + evidence chain +
  remediation recommendation. Consumed by
  `legalcode-eu-gold-plating-detector` (skill F) for over-coverage
  cross-check and by `legalcode-eu-infringement-procedure-tracker` (skill H)
  for incorrect-transposition risk scoring

Sibling skills:

- `legalcode-eu-directive-analyzer` (B) — obligation register
- `legalcode-eu-transposition-tracker` (C) — per-MS implementation matrix
- `legalcode-eu-correlation-table-builder` (D) — directive-to-NIM
  correlation table
- `legalcode-eu-conformity-assessment` (E, this skill) — per-article verdict
- `legalcode-eu-gold-plating-detector` (F) — over-implementation flag
- `legalcode-eea-incorporation-tracker` (G) — EEA Joint Committee Decision
- `legalcode-eu-infringement-procedure-tracker` (H) — TFEU 258/260 timeline

See [shared EU legislative-data pack](references/eu-legislative-data/)
for CELEX/ELI/ECLI conventions, language codes, official-journal
abbreviations, and treaty cross-reference.

---

## Jurisdiction and Governing Law

This skill is pan-European and supports both the EU pillar and the EEA pillar.

**EU pillar (EU-27).** The conformity duty rests on Article 288(3) TFEU read
with Article 4(3) TEU. The Commission's mandate under Article 17(1) TEU is
operationalised through Article 258 TFEU (LFN → reasoned opinion → CJEU
referral); Article 260(2) TFEU provides for penalty payments after
non-compliance with an Article 258 judgment; Article 260(3) TFEU — a Lisbon
innovation first applied in _Commission v Belgium_, Case C-543/17,
ECLI:EU:C:2019:573 — allows the Commission to seek a financial penalty
already on first referral where a Member State has failed to notify
transposition measures. Substantive conformity is governed by CJEU case-law:
_Commission v Germany_, Case C-543/09, ECLI:EU:C:2010:778, sets the
incomplete-transposition standard; _Commission v Italy_, Case C-456/03,
ECLI:EU:C:2005:388, the substantive non-conformity standard.

**EEA pillar (Iceland, Liechtenstein, Norway).** Where the EU act has been
incorporated into the EEA Agreement by Joint Committee Decision under
Article 102 EEA, equivalent conformity duties bind the three EEA-EFTA States.
Surveillance is conducted by the EFTA Surveillance Authority (ESA) under
Article 31 of the Surveillance and Court Agreement (SCA), and adjudication by
the EFTA Court. EFTA Court case-law generally tracks CJEU case-law under the
homogeneity principle (Article 6 EEA). For EEA-relevant directives, run this
skill in parallel against the EEA-EFTA NIM, cross-checked through
`legalcode-eea-incorporation-tracker` (skill G).

[JURISDICTION-SPECIFIC: EU-27] Apply Article 288(3) TFEU + Article 4(3) TEU.
Verdict authority: Commission (Better Regulation Toolbox 2023, Chapter 4) and
ultimately the CJEU under Article 258/260 TFEU. Penalty regime: Article 260(2)
and Article 260(3) TFEU.

[JURISDICTION-SPECIFIC: EEA-EFTA (IS/LI/NO)] Apply the corresponding EEA
provisions plus Article 31 SCA. Verdict authority: ESA and ultimately the EFTA
Court. Penalty regime: declaratory judgments only — there is no EEA equivalent
of Article 260(3) TFEU; recurrent failure can attract Joint Committee scrutiny
under Article 102 EEA.

[JURISDICTION-SPECIFIC: pre-accession candidate countries] The accession
_acquis_ requires substantive conformity at point of accession. The Commission
applies the same Better-Reg-Toolbox methodology in its annual enlargement
reports. This skill can be run on accession-NIM, but its outputs are advisory
only — they do not bind the Commission's accession assessment.

---

## Interactive Clarification

This skill uses **⟁ CLARIFY** markers at key decision points. When you reach a
CLARIFY marker, ask the user before proceeding — do not silently assume
defaults. Only ask when the answer will materially change the analysis; if the
context has already been provided, skip that question and proceed.

Use the harness's structured question tool when one is available:

- **Claude Code / Agent SDK:** invoke the `AskUserQuestion` tool. Limits: 1–4
  questions per call, 2–4 options each, header ≤ 12 characters. Pass the
  CLARIFY options as the `options` array.
- **OpenAI Codex CLI:** invoke `ask_user_question` (runtime) or, in plan mode,
  `request_user_input`. Pass the CLARIFY options as choices.
- **No structured tool available (other harnesses, CI, headless mode without a
  `canUseTool` callback):** emit the CLARIFY questions as numbered plain text
  and **stop until the user replies**. Do not proceed with assumed answers.

When you proceed with partial context, state every assumption explicitly so the
user can correct it.

**Standard clarification format:**

```
⟁ CLARIFY — [Decision point name]

[Short context: why this question matters]

1. **[Option A]**: [Description]
2. **[Option B]**: [Description]
3. **[Option C]**: [Description]

**Why this matters**: [One sentence on how the answer changes the analysis direction]
```

For batch / non-interactive runs, use these defaults:

- Persona: Government / EU institution self-assessment
- Pillar: EU-27 (skip EEA pillar unless directive is EEA-relevant)
- Language reconciliation: EN as working language, plus the Member State's
  national language; flag CILFIT issues if EN and national diverge
- Verdict floor: classify ambiguity as PARTIAL, not CORRECT, until _Marleasing_
  salvage analysis is performed
- Direct-effect flag: emit only where obligation is plainly unconditional and
  sufficiently precise; otherwise omit

---

## Workflow

### Step 1: Accept Input

This skill consumes structured input from sibling skills B, C, and D.
Minimum required:

- **Obligation register** (skill B JSON schema) — each obligation carrying
  provision reference, addressee, scope, modal operator, and recital
  cross-references.
- **Implementation matrix** (skill C JSON schema) — NIM(s) + official-journal
  references.
- **Correlation table** (skill D JSON schema) — directive Article (and
  paragraph/sub-paragraph) ↔ NIM provision.
- Directive text in at least one official language (working language) and
  NIM text in the MS official language(s).

If any input is missing, run the upstream sibling skill first; do not extract
the obligation register inline (that is skill B's job, and inline extraction
short-circuits the audit trail).

Accepted input formats: JSON files at filesystem paths; inline JSON pasted
into the prompt; Markdown reports from upstream skills with embedded JSON
blocks. Where the user provides only directive name + Member State (e.g.
"NIS2, Germany"), invoke skills B/C/D first; do not synthesise the
register from memory.

### Step 2: Establish Persona and Operating Mode

⟁ CLARIFY — Persona

Treyst-style EU compliance work serves four distinct persona profiles whose
deliverables diverge sharply. The same directive analysis becomes a transposition
draft for a ministry, a comparative briefing for a law firm, an impact assessment
for a company, or a policy position for a trade federation.

1. **Government / EU institution**: Drafting national implementing measures,
   running internal conformity checks, preparing Commission notification
   packages, producing self-assessment for ESA (EFTA pillar) or DG-level review.
2. **Legal firm**: Producing client advisories, comparative cross-MS tables for
   client briefings, gap analyses for client compliance programmes.
3. **Company**: Building internal compliance impact assessments, identifying
   operational changes required, scoping internal policy updates, preparing for
   regulator engagement.
4. **Trade federation**: Industry-wide impact summaries, draft policy positions
   for engagement during legislative or transposition phases.

**Why this matters**: Persona determines output format, level of detail,
audience language, citation density, and which workflow branches to execute. A
government self-assessment requires correlation tables in Commission format; a
company impact assessment requires obligation extraction filtered to
private-actor addressees; a federation position needs comparative scoreboarding
across MS.

For conformity assessment specifically, persona also drives **verdict tone**:
government self-assessment uses defensive framing ("the NIM achieves the
result required by Article X because..."); Commission-view review uses
prosecutorial framing with explicit Better-Reg-Toolbox-taxonomy citation;
law-firm advisory uses risk framing with infringement-risk score; company
impact uses operational framing focused on what the company must do
differently.

⟁ CLARIFY — Operating mode

1. **EU-pillar (single MS)**: Better-Reg-Toolbox-format per-article report.
2. **EU-pillar (multi-MS comparative)**: per-article scoreboard across MS.
3. **EEA-pillar**: Article 31 SCA assessment in ESA-format.
4. **Pre-LFN dossier (Commission view)**: Article 258 LFN-supporting dossier
   with heavier case-law citation and infringement-risk framing.
5. **Pre-court submission**: Court-ready assessment with full _Marleasing_
   analysis, direct-effect flags, language-reconciliation appendix.

**Why this matters**: Modes 4 and 5 require a higher confidence floor (no
ASSUMED on verdict-driving claims) and obligatory adversarial review; Modes
1–3 tolerate VERIFY-marked findings provided they are flagged.

### Step 3: Resolve Inputs

**3a. Validate the obligation register (skill B output).** Per obligation,
confirm: `obligation_id` (stable), `directive_celex`, `provision_reference`
(Art. + para + sub-para), `addressee`, `modal_operator`, `operative_content`,
`language_versions_loaded`. Optional: `derogation_options`,
`interpretive_recital`. If `language_versions_loaded` contains only one
entry, flag the obligation **single-language-anchored** and require Step 6
before final verdict.

**3b. Validate the implementation matrix (skill C output).** Per NIM:
official-journal reference (e.g. `BGBl. I 2024 Nr. 305`); publication date
and entry-into-force date; status (in force / pending / consolidated /
amended); plain-text excerpt of provisions referenced in the correlation
table.

**3c. Validate the correlation table (skill D output).** Per directive
provision, confirm one of: non-empty NIM citation; or explicit "no NIM"
entry with a documented reason (`already_in_force_pre_directive`,
`not_applicable_to_MS`, `relied_on_existing_constitutional_provision`,
`not_yet_transposed`). If neither is present, escalate to the user and
rerun skill D. Do not invent reasons.

**3d. Resolve working and reconciliation languages.**

⟁ CLARIFY — Working language

1. **EN-only**: English authentic version only.
2. **EN + national language**: English working + MS national language(s) for
   reconciliation. _Default._
3. **Full multi-language**: All 24. _Court-ready submissions and
   divergence-suspected cases._

**Why this matters**: Single-language anchoring is, under _CILFIT_, an
inadequate basis for either CORRECT or INCORRECT in a divergent-text case.

### Step 4: Per-Obligation Conformity Test

Apply the Commission's three-step methodology — completeness → substantive
correspondence → operational equivalence — to each obligation. Where the
correlation table records "no NIM", the test still runs and produces a
NOT-TRANSPOSED verdict unless the documented reason is itself a permissible
basis for non-transposition (e.g. `already_in_force_pre_directive`).

#### Step 4a — Completeness Test

Decompose the obligation into atomic elements (addressee, conduct, scope,
exceptions, sanctions, procedural rights). Check each against the NIM:

| Element                  | Covered? | Notes                                                    |
| ------------------------ | -------- | -------------------------------------------------------- |
| Addressee                | Y/N      | Narrowed addressee class → partial                       |
| Conduct                  | Y/N      | Substantive (not verbatim) equivalence suffices          |
| Scope                    | Y/N      | Same triggers, same thresholds?                          |
| Exceptions / derogations | Y/N      | Permitted derogation = Y; new unauthorised exception = N |
| Sanctions                | Y/N      | Effective, proportionate, dissuasive (CJEU)              |
| Procedural rights        | Y/N      | Right to be heard, judicial review                       |

A "no" against any element opens a **completeness gap**. Note it; do not yet
classify — gaps may be reconciled at 4b or salvaged via _Marleasing_ (Step 7).

#### Step 4b — Substantive Correspondence Test

For each atomic element marked covered at 4a, test substantive
correspondence. The Commission's methodology distinguishes:

- **Verbatim**: NIM reproduces directive text. Can still fail if context
  subverts meaning.
- **Equivalent**: NIM uses different drafting preserving the same effect.
  Permissible — _Commission v Germany_, Case C-543/09, ECLI:EU:C:2010:778,
  paras 51–53.
- **Divergent**: different drafting, different effect. Substantive
  non-conformity — _Commission v Italy_, Case C-456/03, ECLI:EU:C:2005:388.

For each element ask: same protected interest? same addressee class? same
modal operator (mandatory vs. optional)? matching triggers/thresholds?
derogation tracked in scope or exceeded? sanctions effective, proportionate,
dissuasive?

#### Step 4c — Operational Equivalence Test

Where an obligation is framed as a _result_, the Member State chooses the
_mechanism_. Test whether a different mechanism produces the same result.

Common pairings:

- **Licensing vs. notification**: notification permissible if supervision is
  effective; impermissible if nominal.
- **Public authority vs. private body**: independent self-regulator
  permissible only if genuinely independent and resourced (_cf._ _Commission
  v Germany_ (DPA independence), Case C-518/07, ECLI:EU:C:2010:125).
- **Civil vs. administrative remedy**: civil action permissible if
  accessible, effective, dissuasive.
- **Ex ante vs. ex post review**: ex post permissible unless directive
  structurally presupposes ex ante.

Different mechanism, same result → **CORRECTLY TRANSPOSED — operational
equivalence**. Different mechanism, no result → **INCORRECTLY TRANSPOSED —
operational divergence**.

### Step 5: Classify Verdict

Assign one of four verdicts per the Better-Regulation Toolbox 2023, Chapter 4
taxonomy.

**CORRECTLY TRANSPOSED** — all of: every atomic element covered (Step 4a);
six-question substantive correspondence checklist passed (Step 4b);
operational equivalence demonstrated where mechanism choice was made (Step
4c); no multi-language divergence affecting result (Step 6); no _Marleasing_
reliance required (or reliance genuinely available — Step 7).

**PARTIALLY TRANSPOSED** — any of: one or more atomic elements not covered
without destroying the obligation's core; substantive correspondence weakened
in one or more elements (narrower addressee class, higher trigger threshold,
fewer procedural rights); sanctions limb omitted or under-implemented but
conduct rule in place; exception/derogation omitted or under-implemented but
rest of provision in place.

**INCORRECTLY TRANSPOSED** — any of: NIM contradicts the directive (permits
conduct directive prohibits); fundamentally different mechanism fails
operational-equivalence test; reliance on unauthorised derogation, or on
authorised derogation outside its conditions; multi-language reconciliation
reveals NIM anchored in minority cluster diverging from authentic-version
result; _Marleasing_ salvage unavailable.

**NOT TRANSPOSED** — any of: correlation table records "no NIM" without
permissible basis; named NIM provision does not in fact address the
obligation (false correlation); transposition deadline passed without
notification (Article 260(3) TFEU trigger — _Commission v Belgium_,
C-543/17).

#### Verdict-confidence levels

Five-level scale (matches the rest of the Legalcode compliance family):

| Level        | Score     | Definition                                                                                                   |
| ------------ | --------- | ------------------------------------------------------------------------------------------------------------ |
| **VERIFIED** | 0.90–1.00 | Multi-language reconciliation completed; NIM excerpt independently confirmed; checklist applied without gaps |
| **LIKELY**   | 0.70–0.89 | Working-language NIM excerpt confirmed; checklist applied; some reconciliations not yet performed            |
| **POSSIBLE** | 0.50–0.69 | Working-language NIM excerpt provisional; checklist partially applied                                        |
| **VERIFY**   | 0.30–0.49 | Assumption made about NIM content/scope; placeholder pending information                                     |
| **ASSUMED**  | < 0.30    | No NIM excerpt; verdict inferred from typical transposition patterns                                         |

Modes 4 (pre-LFN) and 5 (pre-court) require VERIFIED or LIKELY on every
verdict; POSSIBLE / VERIFY / ASSUMED are not deliverable in those modes.

### Step 6: Apply Multi-Language Cross-Check

The 24 official EU language versions are equally authentic (Regulation
1/1958, ELI: `https://eur-lex.europa.eu/eli/reg/1958/1(1)/oj/eng`). Leading
authority: _CILFIT_, Case C-283/81, ECLI:EU:C:1982:335; reinforced by
_Codan_, Case C-236/97, ECLI:EU:C:1998:208, and _EMU Tabac_, Case C-296/95,
ECLI:EU:C:1998:152.

NIM are typically drafted against a single language version. If that version
diverges from the others (translation drift, post-adoption erratum), the NIM
may faithfully transpose its anchor language but fail the directive's
authentic meaning. Run the conformity test against the meaning reconciled
across versions, not against any single version.

**Light reconciliation** (default): where the working-language and
MS-language versions yield the same NIM mapping, spot-check 2–3 additional
versions (EN, FR, DE) for divergence in operative noun, verb, modal, or
scope marker.

**Full reconciliation** (triggered): where divergence is suspected, pull all
24 versions from EUR-Lex Cellar
(`https://publications.europa.eu/webapi/rdf/sparql`); cluster semantically;
apply _CILFIT_ / _Codan_ / _EMU Tabac_ purpose-directed reconciliation. A
NIM anchored in a minority cluster cannot, on its own, support a CORRECTLY
verdict — at least PARTIALLY with reconciliation noted.

The verdict record's `language_reconciliation` block must list languages
compared, operative noun/verb/modal per language, divergence detected
(yes/no), cluster mapping, NIM anchor language, and effect on verdict (see
Step 11 for the canonical entry shape). Detailed methodology is in the
Multi-Language Reconciliation reference section below.

### Step 7: Identify _Marleasing_-Salvageable vs. Direct-Effect-Ready Provisions

#### _Marleasing_-conforming interpretation

For each obligation classified PARTIALLY or INCORRECTLY at Step 5, test
whether _Marleasing_ salvage (Case C-106/89, ECLI:EU:C:1990:395) is
available:

1. **Is the NIM ambiguous?** If unambiguous and contradicts the directive,
   _Marleasing_ is unavailable; verdict stands.
2. **Can national interpretive method bridge the gap?** Consider purposive
   vs. textual construction, legal-certainty principle, and any
   administrative guidance.
3. **If yes**: _Marleasing_-salvageable. Reclassify INCORRECTLY → PARTIALLY
   with annotation noting practical risk depends on national-court adoption.
4. **If no**: verdict stands. Annotate that conforming interpretation has
   been considered and rejected.

_Marleasing_ moves INCORRECT to PARTIAL; it cannot move PARTIAL to CORRECT.
Detailed limits and case-law (Pupino C-105/03, Adeneler C-212/04) are in the
_Marleasing_-Conforming Interpretation reference section below.

#### Direct effect

For each obligation classified PARTIALLY, INCORRECTLY, or NOT TRANSPOSED,
flag direct-effect readiness against four elements:

- **Unconditional**: no further measure required for the obligation to
  operate.
- **Sufficiently precise**: addressee, protected interest, and required/
  prohibited conduct identifiable from the text.
- **Vertical**: invoked against the Member State or a State emanation
  (_Foster v British Gas_, Case C-188/89, ECLI:EU:C:1990:313). Horizontal
  direct effect is unavailable (_Faccini Dori_, Case C-91/92,
  ECLI:EU:C:1994:292).
- **After deadline**: transposition deadline has passed.

Annotate each verdict record with `direct_effect_ready` (true/false) and a
brief reason.

### Step 8: Compute Conformity Deficit

Aggregate per-obligation verdicts into a Member-State-level **conformity
deficit** following the Single Market Scoreboard methodology. The Scoreboard
distinguishes the **transposition deficit** (un-notified directives) from
the **compliance deficit** (notified directives subject to
incorrect-transposition infringement). This skill computes the latter at the
directive level.

| Metric                        | Formula                                            |
| ----------------------------- | -------------------------------------------------- |
| Total obligations             | count(obligations)                                 |
| Correctly transposed          | count(verdict = CORRECTLY)                         |
| Partially transposed          | count(verdict = PARTIALLY)                         |
| Incorrectly transposed        | count(verdict = INCORRECTLY)                       |
| Not transposed                | count(verdict = NOT)                               |
| Conformity rate               | correctly / total                                  |
| Compliance-deficit weight     | (incorrectly + 0.5 × partially) / total            |
| CRITICAL non-conformity flags | count(verdict ≠ CORRECTLY AND severity = CRITICAL) |

**Obligation severity** is inherited from skill B (CRITICAL / HIGH / MEDIUM
/ LOW), driven by directive sanctions architecture, current Commission
enforcement priorities, and CJEU enforcement record. CRITICAL severity
includes obligations carrying the directive's headline penalty (e.g. NIS2
Art. 21(2)(a)–(j) — €10M or 2% turnover under Art. 34(4)).

**Trend reporting**: where this skill has been run on the same directive-MS
pair before, compute the verdict-change delta and direction (improvement /
deterioration / no change). The delta feeds skill H.

### Step 9: Generate Remediation Recommendations

For every obligation classified PARTIALLY, INCORRECTLY, or NOT TRANSPOSED,
emit a recommendation from the standard menu:

| Recommendation                                   | When to use                                                         | Audience                     | Timeline    |
| ------------------------------------------------ | ------------------------------------------------------------------- | ---------------------------- | ----------- |
| **Amend the NIM**                                | Non-conformity not curable by interpretation                        | Government / legislature     | 6–24 months |
| **Issue interpretive guidance**                  | NIM ambiguous and _Marleasing_-salvageable                          | National competent authority | 3–6 months  |
| **Issue secondary legislation**                  | Gap at implementing-regulation level                                | Executive / ministry         | 3–12 months |
| **Withdraw the NIM provision**                   | Existing NIM _contra legem_ and amend more disruptive than withdraw | Government / legislature     | 6–12 months |
| **Notify the Commission of an existing measure** | Pre-existing constitutional or statutory measure not notified       | Government / PermRep         | Immediate   |
| **No action — _Marleasing_ salvage**             | Conforming interpretation available                                 | Legal community              | n/a         |
| **No action — operational equivalence**          | Different mechanism, same result                                    | n/a                          | n/a         |
| **Pre-empt Article 258 LFN**                     | INCORRECTLY-transposed and Commission likely to pick up             | Government / PermRep         | 3–9 months  |

Each recommendation outputs: obligation ID, recommendation type, legal basis
(directive provision + CJEU case-law if relevant), recommended owner,
estimated timeline, dependencies (parliamentary calendar, JCD pending,
etc.), success metric (criterion converting verdict to CORRECTLY TRANSPOSED).

### Step 10: Adversarial Review for INCORRECTLY-TRANSPOSED Verdicts

Every INCORRECTLY-TRANSPOSED verdict must pass a three-pass adversarial
review before delivery (the conformity-assessment analogue of the
policy-gap 3-pass interrogation).

**Pass 1 — Verdict Chain Integrity.** Does the verdict follow from Steps
4a–4c and Step 6 reconciliation? State the single piece of evidence most
critical to the verdict; if ASSUMED, what would the verdict be under the
opposite assumption? If verdict changes, lower confidence.

**Pass 2 — _Marleasing_ Salvage Re-test.** Re-run Step 7 explicitly: identify
the most plausible conforming interpretation under national law and state
why it is or is not available. If available, downgrade INCORRECTLY →
PARTIALLY.

**Pass 3 — Operational Equivalence Re-test.** Re-run Step 4c against the
directive's _purpose_, not just its form. Re-state the protected interest;
does the NIM mechanism deliver it? If yes, downgrade INCORRECTLY → CORRECTLY
with the operational-equivalence annotation.

The Pass-3 result must be in the audit trail. An INCORRECTLY-TRANSPOSED
verdict without a documented Pass-3 outcome is an invalid output.

### Step 11: Worked Example — NIS2 Article 21(2)(a) Against the German NIS2UmsuCG

NIS2 Directive (Directive (EU) 2022/2555, CELEX 32022L2555, OJ L 333,
27.12.2022, p. 80); German NIS2UmsuCG (Gesetz zur Umsetzung der
NIS-2-Richtlinie). Confirm `[VERIFY]` references against the
Bundesgesetzblatt at runtime.

**Obligation.** Art. 21(2)(a) — Member States ensure that essential and
important entities take appropriate and proportionate technical, operational
and organisational measures to manage cybersecurity risks, including
"policies on risk analysis and information system security".

**Step 4a — Completeness test.**

| Element                  | Directive (EN)                                                                              | NIM (German)                                                                                                      | Covered? |
| ------------------------ | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | -------- |
| Addressee                | "Member States shall ensure" + "essential and important entities"                           | §28/§29 BSIG (revised) [VERIFY] — essential and important entities by sector annex + size                         | Y        |
| Conduct                  | Risk-analysis and information-system-security policies                                      | Duty to adopt written info-security policy + risk analysis (_Informationssicherheitsleitlinie_ / _Risikoanalyse_) | Y        |
| Scope                    | Network and information systems "in their operations or in the provision of their services" | Tracks the same scope                                                                                             | Y        |
| Exceptions / derogations | None for Art. 21(2)(a)                                                                      | None purported                                                                                                    | Y        |
| Sanctions                | Effective, proportionate, dissuasive — Art. 34 NIS2 (essential entity max €10M or 2%)       | Art. 34 architecture transposed into administrative-fine catalogue                                                | Y        |
| Procedural rights        | Implicit (right to challenge supervisory measure)                                           | Verwaltungsverfahrensgesetz; right to administrative-court review                                                 | Y        |

Every element covered. No completeness gap.

**Step 4b — Substantive correspondence.** Same protected interest (high
common level of cybersecurity); same addressee class (NIS2 Annexes I/II
transposed); same modal operator (_müssen / haben zu_); same triggers (entry
into force, no narrowing); no derogation in scope; sanctions ceiling matches
Art. 34. Confirmed.

**Step 4c — Operational equivalence.** Same mechanism (statutory duty +
administrative supervision); no mechanism substitution; test trivially
satisfied.

**Step 5 — Verdict.** CORRECTLY TRANSPOSED.

**Step 6 — Multi-language reconciliation.**

| Language | Operative phrase                                                                           | Cluster  |
| -------- | ------------------------------------------------------------------------------------------ | -------- |
| EN       | "policies on risk analysis and information system security"                                | Majority |
| DE       | "Konzepte für die Risikoanalyse und die Sicherheit von Informationssystemen"               | Majority |
| FR       | "politiques relatives à l'analyse des risques et à la sécurité des systèmes d'information" | Majority |
| IT       | "politiche di analisi dei rischi e di sicurezza dei sistemi informativi"                   | Majority |

No divergence; single majority cluster. NIM faithfully renders the majority
cluster.

**Step 7 — _Marleasing_ / direct effect.** CORRECTLY-TRANSPOSED does not
require _Marleasing_ salvage. Vertical direct effect against State
emanations is conceivable on the "Member States shall ensure" framing but
unnecessary given the NIM in place. `direct_effect_ready: false`.

**Confidence.** LIKELY (0.82) — pending confirmation of enacted §-numbers
and BGBl. reference.

#### Worked example — output formats for the same obligation

**Markdown conformity report excerpt.**

```markdown
### Article 21(2)(a) — Policies on Risk Analysis and Information System Security

**Verdict: CORRECTLY TRANSPOSED** (Confidence: LIKELY 0.82)

NIS2 Directive (Directive (EU) 2022/2555, CELEX 32022L2555, OJ L 333,
27.12.2022, p. 80), Art. 21(2)(a) — essential and important entities to
adopt "policies on risk analysis and information system security".

NIM: Germany — NIS2UmsuCG (BGBl. I [VERIFY]), §28 / §29 BSIG (revised)
[VERIFY].

Conformity test: completeness — every atomic element covered. Substantive
correspondence — same protected interest, addressee class, modal operator,
triggers, sanctions ceiling. Operational equivalence — same mechanism
(statutory duty + administrative supervision); trivially satisfied.

Multi-language reconciliation: EN, DE, FR, IT compared; single majority
cluster; no divergence. NIM anchored in DE majority-cluster wording.

Direct effect: not required (NIM in place). Vertical direct effect against
State emanations would be available on the "Member States shall ensure"
framing in the absence of the NIM, but unnecessary here.

Remediation: none. Adversarial Pass 3 confirmed operational equivalence
trivially. Confidence LIKELY pending confirmation of §-numbers and BGBl.
reference.
```

**JSON conformity schema.**

```json
{
  "$schema": "https://legalcode.example/eu-conformity/v1.json",
  "directive": {
    "celex": "32022L2555",
    "short_title": "NIS2 Directive",
    "eli": "https://eur-lex.europa.eu/eli/dir/2022/2555/oj"
  },
  "member_state": "DE",
  "obligations": [
    {
      "obligation_id": "NIS2-21-2-a",
      "provision_reference": "Art. 21(2)(a)",
      "addressee": "essential_and_important_entities",
      "modal_operator": "shall",
      "operative_content": "policies on risk analysis and information system security",
      "nim_citations": [
        {
          "instrument": "NIS2UmsuCG",
          "official_journal": "BGBl. I [VERIFY]",
          "in_force": true,
          "provision": "§28/§29 BSIG (revised) [VERIFY]"
        }
      ],
      "completeness": {
        "addressee_covered": true,
        "conduct_covered": true,
        "scope_covered": true,
        "exceptions_covered": true,
        "sanctions_covered": true,
        "procedural_rights_covered": true
      },
      "substantive_correspondence": {
        "same_protected_interest": true,
        "same_addressee_class": true,
        "same_modal_operator": true,
        "same_triggers": true,
        "derogation_in_scope": null,
        "sanctions_effective_proportionate_dissuasive": true
      },
      "operational_equivalence": {
        "mechanism_substitution": false,
        "result_delivered": true
      },
      "language_reconciliation": {
        "languages_compared": ["en", "de", "fr", "it"],
        "divergence_detected": false,
        "cluster_summary": "single_majority_cluster",
        "anchor_language_of_nim": "de"
      },
      "marleasing_salvage_required": false,
      "direct_effect_ready": false,
      "verdict": "CORRECTLY_TRANSPOSED",
      "confidence_label": "LIKELY",
      "confidence_score": 0.82,
      "adversarial_review": {
        "pass_1_verdict_chain": "consistent",
        "pass_2_marleasing_retest": "n_a",
        "pass_3_operational_equivalence_retest": "confirmed_trivially"
      },
      "remediation_recommendation": null,
      "verify_markers": ["official_journal_reference", "section_numbers_in_nim"]
    }
  ]
}
```

**AKN4EU `<judgment>` stub.**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<akomaNtoso xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0"
            xmlns:lc="https://legalcode.example/akn-extensions/1.0">
  <judgment name="conformityAssessment">
    <meta>
      <identification source="#legalcode-eu-conformity-assessment">
        <FRBRWork>
          <FRBRthis value="/akn/eu/lc/conformity/2022-2555/de/art-21-2-a"/>
          <FRBRuri value="/akn/eu/lc/conformity/2022-2555/de"/>
          <FRBRalias value="NIS2 21(2)(a) — DE conformity"/>
          <FRBRdate date="[ASSESSMENT-DATE]" name="assessmentDate"/>
          <FRBRauthor href="#legalcode-eu-conformity-assessment"/>
          <FRBRcountry value="DE"/>
        </FRBRWork>
        <FRBRExpression>
          <FRBRthis value="/akn/eu/lc/conformity/2022-2555/de/art-21-2-a/eng@/main"/>
          <FRBRuri value="/akn/eu/lc/conformity/2022-2555/de/eng@"/>
          <FRBRdate date="[ASSESSMENT-DATE]" name="expressionDate"/>
          <FRBRauthor href="#legalcode-eu-conformity-assessment"/>
          <FRBRlanguage language="eng"/>
        </FRBRExpression>
        <FRBRManifestation>
          <FRBRthis value="/akn/eu/lc/conformity/2022-2555/de/art-21-2-a/eng@.xml"/>
          <FRBRuri value="/akn/eu/lc/conformity/2022-2555/de/eng@.xml"/>
          <FRBRdate date="[ASSESSMENT-DATE]" name="manifestationDate"/>
          <FRBRauthor href="#legalcode-eu-conformity-assessment"/>
        </FRBRManifestation>
      </identification>
      <references source="#legalcode-eu-conformity-assessment">
        <TLCConcept eId="dir-2022-2555"
                    href="https://eur-lex.europa.eu/eli/dir/2022/2555/oj"
                    showAs="NIS2 Directive"/>
        <TLCConcept eId="art-21-2-a"
                    href="https://eur-lex.europa.eu/eli/dir/2022/2555/oj#art_21.par_2.lit_a"
                    showAs="Art. 21(2)(a)"/>
        <TLCOrganization eId="ms-de" showAs="Federal Republic of Germany"/>
        <TLCConcept eId="nim-nis2umsucg" showAs="NIS2UmsuCG"/>
      </references>
    </meta>
    <judgmentBody>
      <decision>
        <p lc:verdict="CORRECTLY_TRANSPOSED" lc:confidence="LIKELY">
          The NIM transposes the obligation correctly: every atomic element
          covered; substantive correspondence and operational equivalence
          satisfied; multi-language reconciliation discloses no divergence.
        </p>
      </decision>
      <motivation>
        <p>Under Art. 288(3) TFEU the directive binds Germany as to the
           result to be achieved — adoption by essential and important
           entities of risk-analysis and information-security policies. The
           NIM imposes that result through statutory duty and administrative
           supervision.</p>
      </motivation>
    </judgmentBody>
  </judgment>
</akomaNtoso>
```

**LegalRuleML `<lrml:Constitutive>` stub.**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<lrml:LegalRuleML xmlns:lrml="http://docs.oasis-open.org/legalruleml/ns/v1.0/"
                  xmlns:ruleml="http://ruleml.org/spec"
                  xmlns:lc="https://legalcode.example/lrml-extensions/1.0">
  <lrml:Source>
    <lrml:appliesSource>
      <lrml:LegalSource refID="dir-2022-2555-art-21-2-a"
                        sameAs="https://eur-lex.europa.eu/eli/dir/2022/2555/oj"/>
    </lrml:appliesSource>
  </lrml:Source>
  <lrml:Constitutive key="conformity-NIS2-21-2-a-DE">
    <lrml:Party iri="urn:lrml:party:essential_and_important_entity_DE"/>
    <lrml:hasStrength>
      <lrml:DefeasibleStrength/>
    </lrml:hasStrength>
    <lrml:then>
      <lrml:Obligation iri="urn:lrml:obligation:adopt_risk_analysis_and_information_security_policy">
        <ruleml:Atom>
          <ruleml:Rel iri="lc:adoptPolicy"/>
          <ruleml:Var>entity</ruleml:Var>
          <ruleml:Ind iri="lc:RiskAnalysisAndInformationSystemSecurityPolicy"/>
        </ruleml:Atom>
      </lrml:Obligation>
    </lrml:then>
    <lc:conformityVerdict value="CORRECTLY_TRANSPOSED"/>
    <lc:confidence value="LIKELY" score="0.82"/>
    <lc:nimReference iri="lc:NIS2UmsuCG-§28-§29-BSIG"/>
    <lc:directEffectReady value="false"/>
    <lc:marleasingRequired value="false"/>
  </lrml:Constitutive>
</lrml:LegalRuleML>
```

**Glass Box audit-trail entry (excerpt).**

```yaml
glass_box:
  obligation_id: "NIS2-21-2-a"
  member_state: "DE"
  verdict: "CORRECTLY_TRANSPOSED"
  confidence_score: 0.82
  confidence_label: "LIKELY"
  evidence_chain:
    - step: "completeness"
      result: "all_elements_covered"
      sources:
        [
          "NIS2 Art. 21(2)(a) authentic EN",
          "NIS2UmsuCG §28/§29 BSIG (revised) [VERIFY]",
        ]
    - step: "substantive_correspondence"
      result: "satisfied"
      checklist_passed: 6
    - step: "operational_equivalence"
      result: "trivially_satisfied"
    - step: "multi_language_reconciliation"
      result: "no_divergence"
      languages_compared: ["en", "de", "fr", "it"]
    - step: "marleasing_salvage"
      result: "not_required"
    - step: "direct_effect_flag"
      result: "false"
    - step: "adversarial_review_pass1"
      result: "consistent"
    - step: "adversarial_review_pass2"
      result: "n_a"
    - step: "adversarial_review_pass3"
      result: "confirmed_trivially"
  verify_markers:
    - "Confirm BGBl. citation of NIS2UmsuCG"
    - "Confirm §-numbers in NIM enacted text"
  reviewer_note: "AI-assisted. Verdict requires validation by qualified DE counsel before infringement-procedure use."
```

### Step 12: Emit Outputs

Emit a single deliverable containing: (1) Markdown executive summary; (2)
per-obligation conformity report; (3) Markdown scoreboard table; (4) JSON
conformity schema; (5) AKN4EU `<judgment>` document (one element per
obligation); (6) LegalRuleML `<lrml:Constitutive>` rule set; (7) Glass Box
YAML audit trail (per-obligation + aggregate). The four structured formats
are complementary, not alternatives — round-trippability is the
differentiator. Detailed templates appear in the Output Format Template
section below.

---

## Conformity Verdict Taxonomy

The four verdicts are the formal Better-Regulation-Toolbox 2023, Chapter 4
output values. They map directly to the Commission's infringement-decision
logic and to the Single Market Scoreboard compliance-deficit metric.

### Correctly transposed

The NIM achieves the result the directive prescribes. Drafting may differ
from the directive — the difference is form, not substance.
Operational-equivalence cases are correctly transposed. Verbatim
transposition is correctly transposed unless context subverts the verbatim
text. _Example_: directive requires "an independent authority"; NIM
designates an existing regulator that meets the directive's independence
criteria.

### Partially transposed

The NIM transposes some atomic elements but leaves gaps that materially
affect the result, without wholly missing the obligation. _Example_:
directive imposes duties on "essential and important entities"; NIM
transposes for essential entities only, leaving important entities uncovered.

### Incorrectly transposed

The NIM purports to transpose the obligation but its substance diverges.
Reserved for cases where the NIM exists, was notified, and has been relied on
by the Member State — but its content is divergent. _Example_: directive
requires an absolute prohibition; NIM permits the prohibited conduct subject
to authorisation.

### Not transposed

No NIM exists, or the NIM is so disconnected from the obligation that it
cannot reasonably be regarded as transposition. This is the trigger for
Article 260(3) TFEU first-referral penalty (cf. _Commission v Belgium_, Case
C-543/17). _Example_: deadline passed, no NIM notified; correlation table
records "no NIM" without permissible basis.

---

## Substantive Correspondence Test

Substantive correspondence is the heart of conformity. Six atomic elements
are tested independently.

### Scope test

- Directive scope reproduced in NIM (geography, sector, size threshold,
  activity threshold)?
- Class of addressee entities reproduced with the same boundaries?
- Volume/turnover threshold preserved or narrowed?
- Note: narrowed scope is not necessarily incorrect. Minimum-harmonisation
  directives permit extension; maximum-harmonisation directives do not.
  Verify harmonisation type from skill B's obligation register.

### Operative content test

- Directive verb reproduced as a binding command?
- Modal operator preserved ("shall" → "shall" or national-law equivalent;
  "may" → "may", not "shall")?
- Directive standards ("appropriate and proportionate", "effective",
  "transparent") reproduced or preserved by national equivalents?
- Specified procedural mechanism (notification, publication, registration)
  reproduced or operationally equivalent?

### Addressee test

- Directive's addressee reproduced as the NIM's addressee?
- Where directive addresses Member States ("shall ensure"), NIM duty must
  flow through to the substantive addressee.
- Where directive addresses a non-State actor, NIM must impose the duty on
  that actor — not on the State alone.

### Sanction test

- NIM provides for sanctions on breach?
- Sanctions **effective, proportionate, dissuasive** — long-standing CJEU
  standard?
- Where directive prescribes a maximum ceiling (e.g. NIS2 Art. 34 essential
  entity max €10M or 2% global turnover), NIM ceiling reaches at least that
  level. Lower ceiling is partial at best.
- Both administrative fines and natural-person sanctions, where directive
  prescribes both?

### Derogation test

- Directive permits derogation? If yes, NIM reliance within its scope?
- NIM purports to derogate where no derogation is permitted? → INCORRECT.
- Conditional derogations: criteria satisfied?

### Procedural-rights test

- Procedural rights conferred by directive (hearing, judicial review, time
  limits, challenge of supervisory measure) preserved in NIM?
- Where directive is silent but Charter Art. 47 requires effective remedy,
  NIM preserves Charter-compliant procedure?

---

## Multi-Language Reconciliation in Conformity Assessment

The 24 official EU language versions are equally authentic. Methodology rests
on three CJEU judgments:

- _CILFIT_, Case C-283/81, ECLI:EU:C:1982:335 — comparison of language
  versions when reasonable doubt arises as to interpretation.
- _Codan_, Case C-236/97, ECLI:EU:C:1998:208 — divergence resolved by
  reference to the purpose and general scheme of the rule.
- _EMU Tabac_, Case C-296/95, ECLI:EU:C:1998:152 — no single language version
  may be privileged.

### When to perform light vs. full reconciliation

| Trigger                                                                         | Light (EN, FR, DE + MS language) | Full (all 24) |
| ------------------------------------------------------------------------------- | -------------------------------- | ------------- |
| No divergence suspected                                                         | yes                              | no            |
| NIM faithfully renders MS-language directive                                    | yes                              | no            |
| NIM anchored in one version where another reads differently                     | no                               | yes           |
| Post-adoption erratum or corrigendum to language version                        | no                               | yes           |
| Interpretation subject of CJEU preliminary reference on language reconciliation | no                               | yes           |
| Pre-court submission (Mode 5)                                                   | no                               | yes           |

### Reconciliation procedure

1. Pull the operative provision in the languages required.
2. Record operative noun, verb, modal, and scope-defining adjective verbatim
   per language.
3. Cluster by semantic equivalence (use EUR-Lex Cellar SPARQL or the web
   service for canonical retrieval).
4. Check divergence; if present, apply _Codan_ and _EMU Tabac_ —
   purpose-directed reconciliation.
5. Identify NIM anchor cluster. A NIM anchored in a minority cluster is at
   least PARTIALLY transposed regardless of faithfulness to the anchor.
6. Record reconciliation in the audit trail.

### Authority for equal authenticity

Regulation 1/1958, ELI:
`https://eur-lex.europa.eu/eli/reg/1958/1(1)/oj/eng`. The 24 official
languages are: Bulgarian, Croatian, Czech, Danish, Dutch, English, Estonian,
Finnish, French, German, Greek, Hungarian, Irish, Italian, Latvian,
Lithuanian, Maltese, Polish, Portuguese, Romanian, Slovak, Slovenian,
Spanish, Swedish. Norwegian and Icelandic are not EU official languages but
are EEA-EFTA national languages used for EEA-pillar NIM reconciliation.

---

## _Marleasing_-Conforming Interpretation

### The duty

National courts and authorities must, so far as possible, interpret national
law in a directive-conforming manner. The duty is grounded in Article 288(3)
TFEU and Article 4(3) TEU and articulated as a discrete doctrine in
_Marleasing_, Case C-106/89, ECLI:EU:C:1990:395, paras 8–9.

### Limits on the duty

- Bounded by national interpretive method; _contra legem_ interpretation is
  not required.
- Does not impose or aggravate criminal liability ex lege.
- Applies only after transposition deadline has passed; before the deadline,
  the pre-transposition-effect doctrine (_Inter-Environnement Wallonie_,
  Case C-129/96, ECLI:EU:C:1997:628) operates differently.

### How the conformity assessment uses _Marleasing_

The skill is interested in the **substance of the NIM**, not in any particular
national-court interpretation. _Marleasing_ is relevant in two ways:

1. As verdict modulator. Where NIM language is ambiguous, conforming
   interpretation may move the verdict from INCORRECTLY to PARTIALLY. It does
   not move PARTIALLY to CORRECTLY.
2. As remediation modulator. _Marleasing_-salvageable findings attract "issue
   interpretive guidance"; non-salvageable findings attract "amend the NIM".

### When _Marleasing_ salvage is **unavailable**

- NIM language is unambiguous and contradicts the directive.
- National interpretive tradition (e.g. criminal-law textualism) prohibits
  the conforming reading.
- Conforming interpretation would contradict legal certainty (_Adeneler_,
  Case C-212/04, ECLI:EU:C:2006:443, para 110).
- Conforming interpretation would impose criminal liability ex lege
  (_Pupino_, Case C-105/03, ECLI:EU:C:2005:386).

In any of these cases the verdict stands at INCORRECTLY transposed.

---

## Direct Effect Tests

A directive provision may be invoked directly by a private party against the
State (or a State emanation) where the provision is unconditional and
sufficiently precise (_Becker_, Case C-8/81, ECLI:EU:C:1982:7). Direct effect
does not run horizontally between private parties (_Faccini Dori_, Case
C-91/92, ECLI:EU:C:1994:292).

### Four-element test

For each obligation classified PARTIALLY, INCORRECTLY, or NOT transposed:

1. **Unconditional** — no further measure required for the obligation to
   operate.
2. **Sufficiently precise** — the right or duty is identifiable from the text
   without further specification.
3. **Vertical** — invoked against the Member State or a State emanation
   (_Foster v British Gas_, Case C-188/89, ECLI:EU:C:1990:313 — under State
   control, public-interest service, special powers).
4. **After deadline** — transposition deadline has passed.

All four satisfied: flag `direct_effect_ready: true`. The flag is
informational; the skill does not predict litigation outcomes.

### Triangular cases

Where a directive provision is invoked against a private party in a way that
adversely affects another private party, direct effect is generally
unavailable on the _Faccini Dori_ line. _Marleasing_ interpretive route is
the only available bridge.

### Direct effect is not a substitute for conformity

A NIM that fails conformity is not "rescued" by direct effect. Direct effect
operates downstream of the State's failure; it does not absolve the State
under Article 288(3) TFEU and does not remove Article 258 TFEU exposure.

---

## Operational Equivalence

A Member State may transpose a directive obligation through a different
mechanism provided the mechanism delivers the same result — Article 288(3)
TFEU; _Commission v Germany_, Case C-543/09, ECLI:EU:C:2010:778, paras 51–53.

### When operational equivalence applies

- Directive obligation defines a result, not a specific mechanism.
- NIM uses a different mechanism that, in operation, delivers the result.
- Mechanism choice does not undermine other directive provisions or
  Union-law principles (effectiveness, equivalence, sincere cooperation).

### Examples

| Directive mechanism | NIM mechanism                      | Equivalence ordinarily found?                                              |
| ------------------- | ---------------------------------- | -------------------------------------------------------------------------- |
| Licensing           | Notification + ex post supervision | Often yes, if supervision is genuinely effective                           |
| Public authority    | Independent self-regulatory body   | Sometimes yes, if independence and resourcing match                        |
| Civil action        | Administrative remedy              | Often yes, if administrative remedy accessible and dissuasive              |
| Ex ante review      | Ex post review                     | Sometimes yes; turns on whether directive structurally presupposes ex ante |

### When operational equivalence fails

- NIM mechanism is nominal or symbolic (_Commission v Germany_, Case
  C-543/09, paras 53–55).
- NIM transfers the directive's result to a body lacking capacity to deliver.
- NIM is contingent on action that does not occur — result is latent, not
  delivered.

In any of these cases, classify INCORRECTLY transposed and emit "amend the
NIM".

---

## EEA Pillar Conformity

For EEA-relevant directives (marked "Text with EEA relevance" or incorporated
into the EEA Agreement by Joint Committee Decision under Article 102 EEA),
the EEA-EFTA States — Iceland, Liechtenstein, Norway — are bound to
substantive conformity in their NIM. Three architectural differences from
the EU pillar:

- **Surveillance**: ESA under Article 31 SCA, not the Commission under
  Article 17 TEU. ESA methodology tracks the Better-Reg Toolbox; ESA
  publishes the EFTA Internal Market Scoreboard at `https://www.efta.int/`.
- **Adjudication**: EFTA Court, not CJEU. EFTA Court case-law tracks CJEU
  case-law under the homogeneity principle (Article 6 EEA). Cross-check
  authorities at `https://eftacourt.int/`.
- **Penalty regime**: no EEA equivalent of Article 260(3) TFEU. ESA's
  enforcement ends at declaratory infringement judgments. Recurrent
  non-compliance can attract Joint Committee scrutiny and, in extreme cases,
  suspension of incorporation under Article 102 EEA.

### Cross-reference

Use `legalcode-eea-incorporation-tracker` (skill G) to confirm Joint
Committee Decision incorporation and any Article 103 EEA constitutional
reservations. Run this skill (E) against the resulting EEA-EFTA NIM.

### EEA-pillar verdict labels and remediation

Four-verdict taxonomy preserved. Remediation menu preserved except that
"Pre-empt Article 258 LFN" becomes "Pre-empt ESA reasoned-opinion procedure
under Article 31 SCA".

---

## Anti-Patterns

What NOT to do when running a conformity assessment.

1. **Treating notification as conformity.** Notification is procedural;
   conformity is substantive. The Single Market Scoreboard's compliance-deficit
   metric exists because notification and conformity diverge in practice. This
   skill assesses substantive conformity; it does not interpret notification
   status.

2. **Verbatim transposition as automatic conformity.** A NIM that reproduces
   directive text verbatim can still fail conformity if the verbatim text is
   placed in a context that subverts its meaning (e.g. a sanctions ceiling
   reproduced verbatim but rendered inapplicable by a procedural rule
   elsewhere in the NIM, or a derogation reproduced without the conditions on
   which it depends).

3. **Single-language anchoring.** Reading the directive only in the working
   language and the NIM only in its national language without reconciliation.
   Light reconciliation is mandatory; full reconciliation is triggered by the
   Step 6 heuristic. A verdict reached without reconciliation is not
   deliverable.

4. **Outsourcing the conformity verdict to _Marleasing_.** Treating
   _Marleasing_ as a backstop that "saves" any ambiguous NIM. _Marleasing_
   moves INCORRECTLY → PARTIALLY only; it does not move PARTIALLY → CORRECTLY,
   and its applicability depends on national interpretive method, not on
   assessor judgment.

5. **Direct effect as a substitute for conformity.** Annotating an
   INCORRECTLY-transposed NIM as direct-effect-ready and concluding that the
   transposition issue is solved. Direct effect is a remedial doctrine; it
   does not absolve the Member State under Article 288(3) TFEU and does not
   remove Article 258 TFEU exposure.

6. **Operational-equivalence over-application.** Classifying every
   mechanism-substitution case as operationally equivalent without testing
   whether the substitute mechanism in fact delivers the result — _cf._ the
   _Commission v Germany_ independent-DPA line.

7. **Skipping the adversarial Pass-3 review.** Issuing an INCORRECTLY-TRANSPOSED
   verdict without the documented Pass-3 (operational-equivalence retest).
   This is the highest-risk verdict in the taxonomy because it drives
   infringement-procedure exposure; it must be reviewed adversarially.

8. **Conflating obligation severity with verdict.** Severity drives only the
   priority of remediation; it does not raise or lower the verdict itself.

9. **Inventing a "no NIM" reason to close out a correlation gap.** Escalate to
   the user; do not invent a reason. Invented reasons contaminate the audit
   trail.

10. **Applying maximum-harmonisation logic to minimum-harmonisation directives,
    or vice versa.** Read the harmonisation type from the obligation register
    before classifying.

11. **Ignoring the recital context.** Recitals shape operative-provision
    meaning. Skill B's obligation register includes recital cross-references
    for this reason.

12. **Confusing partial transposition with gold-plating.** Partial transposition
    is _under_-coverage; gold-plating is _over_-coverage. This skill emits the
    under-coverage signal; skill F emits the over-coverage signal.

13. **Running the EU pillar and ignoring the EEA pillar for an EEA-relevant
    directive.** EEA relevance is not optional for IS, LI, and NO.

14. **Treating ESA's annual scoreboard as a conformity verdict.** The EFTA
    Internal Market Scoreboard reports a transposition deficit, not a
    conformity verdict. ESA reasoned opinions and EFTA Court judgments are
    the conformity authorities on the EEA pillar.

15. **Quoting CJEU case-law without ECLI.** Use the `Case C-XXX/YY` plus
    `ECLI:EU:C:YYYY:NNN` form. Multiple cases share party-name pairs.

16. **Producing only a Markdown report.** The four-format output (Markdown,
    JSON, AKN4EU, LegalRuleML) is the differentiator. A Markdown-only
    deliverable cannot round-trip to LEOS or to policy-as-code engines.

17. **Reporting verdicts without confidence labels.** Every verdict carries a
    label from VERIFIED / LIKELY / POSSIBLE / VERIFY / ASSUMED.

18. **Producing a Court-ready submission with VERIFY-marked findings.** Modes
    4 and 5 require VERIFIED or LIKELY on every verdict-driving claim;
    POSSIBLE / VERIFY / ASSUMED must be cleared before delivery.

---

## Writing Standards

1. **Evidence-first verdicts.** Lead with the evidence chain — Step 4a
   completeness, Step 4b substantive correspondence, Step 4c operational
   equivalence — not the conclusion.

2. **Active voice, imperative form.** Write "Amend Section 12 of the NIM to
   include the addressee class 'important entities'" rather than "It is
   suggested that consideration be given...".

3. **Specificity.** "Article 21(2)(a) NIS2 transposed via §28 BSIG (revised)
   — completeness gap: addressee class limited to essential entities;
   important entities omitted" is preferred over "NIS2 partially transposed".

4. **One verdict per obligation.** Each obligation gets its own scoreboard
   row, its own `<judgment>` element, and its own `<lrml:Constitutive>`.

5. **Confidence transparency.** Every verdict carries a confidence label and
   score. Do not present ASSUMED findings as fact or POSSIBLE findings as
   VERIFIED.

6. **Citation density.** Every case-law-driven verdict cites with ECLI; every
   treaty-article-driven verdict uses TFEU/TEU/EEA prefix; every
   directive-driven verdict uses CELEX plus short title.

7. **Citation format.** EU acts: `[Short title] (Directive (EU) [year]/[number],
CELEX [code], OJ L [number], [date], p. [page])`. Treaty articles:
   `Article [number]([para])([sub-para]) [TFEU|TEU]`. Case law:
   `[Party A] v [Party B], Case C-[number]/[year], ECLI:EU:C:[year]:[seq]`
   with paragraph numbers where supporting specific points. ELI URIs inline
   in prose; full URIs in JSON.

8. **Deontic operator usage.** Use "shall", "must", and "may" as the
   directive does. "Should" is non-binding (reserved for recital-derived
   guidance); "will" is informational. Skill's own normative output adopts
   the directive's deontic level, not a softened register.

9. **Language-version reconciliation rules.** The Step 6 light/full matrix is
   mandatory. Where divergence is detected, the audit trail lists the
   diverging languages, operative phrasing in each, and reconciliation
   outcome. Reconciliation not performed caps confidence at LIKELY (0.89).

10. **EEA-relevance flag.** Every output states the directive's EEA-relevance
    status and, where EEA-relevant, whether the EEA-pillar conformity has
    been assessed in this run, deferred to a parallel skill-G/E run, or
    placed out of scope by the user.

11. **CELEX/ELI/ECLI placement.** In prose: short title + CELEX inline; ELI
    in footnote or structured output. In tables: compact short-title + CELEX
    form. ECLI always inline with the case name.

12. **No false precision.** Where verdict depends on unconfirmed NIM excerpt
    or deferred reconciliation, use confidence label + `[VERIFY]` marker;
    round confidence scores to bands rather than spurious decimals.

13. **Glass Box inline.** The Glass Box YAML is part of the deliverable, not
    an appendix. It is the audit trail a regulator follows to trace verdicts
    to evidence.

14. **No silent verdict edits.** Where adversarial Pass-1 / Pass-2 / Pass-3
    review changes a verdict, both the original and revised verdict, with the
    reason for the change, are recorded in the audit trail.

15. **Worked-example anchoring.** When in doubt about format, follow the
    NIS2 Art. 21(2)(a) — DE worked example in Step 11.

---

## External Tool Integration

### With Legalcode MCP connected (preferred)

Delegate the following to the `legalcode-search-agent` subagent (per
repository policy):

- Pull directive authentic text per language from EUR-Lex Cellar SPARQL
  (`https://publications.europa.eu/webapi/rdf/sparql`).
- Pull NIM authentic text from national official journals (Bundesgesetzblatt,
  Journal Officiel, Gazzetta Ufficiale, etc.) or N-Lex
  (`https://eur-lex.europa.eu/collection/n-law/mne.html`).
- Verify CJEU and EFTA-Court ECLIs against CURIA / InfoCuria
  (`https://curia.europa.eu/`) and EFTA Court register
  (`https://eftacourt.int/`).
- Retrieve Commission Better-Reg-Toolbox studies and Single Market Scoreboard
  fiches for comparison.

Save research outputs to `/tmp/legalcode-eu-conformity-research.md` and set
Glass Box field `legalcode_mcp: "Connected — research file at [path]"`.

### Without Legalcode MCP

Proceed with user-supplied inputs; mark unverifiable claims `[VERIFY]`. Set
Glass Box `legalcode_mcp: "Not connected — primary-source citations require independent verification"`.

Downward confidence adjustments:

- ECLIs and case-law paragraph references: LIKELY → POSSIBLE
- Directive language-version excerpts: VERIFIED → LIKELY
- NIM excerpts: LIKELY → POSSIBLE
- ESA / EFTA-Court references: LIKELY → POSSIBLE
- Single Market Scoreboard percentages: any → VERIFY (quarterly changes)

### Related skills integration

| Trigger                         | Invoke                                                              |
| ------------------------------- | ------------------------------------------------------------------- |
| Obligation register required    | skill B                                                             |
| Implementation matrix required  | skill C                                                             |
| Correlation table required      | skill D                                                             |
| Over-coverage findings          | skill F (gold-plating detector)                                     |
| EEA incorporation status        | skill G (EEA tracker)                                               |
| TFEU 258/260 risk               | skill H (infringement tracker)                                      |
| Compliance-program gap analysis | `legalcode-policy-gap-analysis`                                     |
| GDPR-specific deep-dive         | `legalcode-gdpr-legal-basis-assessment`, `legalcode-dpia-generator` |
| AI Act deep-dive                | `legalcode-eu-ai-act-high-risk-compliance`                          |

### Source endpoints

Directive text: EUR-Lex Cellar SPARQL
(`https://publications.europa.eu/webapi/rdf/sparql`); EUR-Lex web service
(`https://eur-lex.europa.eu/content/help/data-reuse/webservice.html`). NIM
retrieval prefers national-parliament APIs where available — Riksdagen (SE,
`https://data.riksdagen.se`); Storting (NO, `https://data.stortinget.no`);
Folketinget (DK, `https://oda.ft.dk`); Althingi (IS, `https://www.althingi.is`);
Bundestag (DE, `https://dip.bundestag.de`); Assemblée nationale (FR,
`https://data.assemblee-nationale.fr`); fall back to N-Lex.

---

## Output Format Template

The deliverable contains five outputs in a single document, in the following
order. The four structured formats (JSON, AKN4EU, LegalRuleML, Glass Box) are
not alternatives — they are complementary representations.

### 1. Executive summary (Markdown)

```markdown
## Conformity Assessment — Executive Summary

Directive: [Short title] (Directive (EU) [year]/[number], CELEX [code], OJ L [number], [date], p. [page])
Member State: [MS code + name]
Assessment date: [YYYY-MM-DD] | Mode: [EU pillar | EEA pillar | pre-LFN | pre-court] | Persona: [Government | Law firm | Company | Trade federation]
Working language: [code] | Reconciliation languages: [list]

### Verdict tally

- Correctly: [N] / [Total] | Partially: [N] | Incorrectly: [N] | Not: [N]
- Conformity rate: [X.X%] | Compliance-deficit weight: [X.X%]

### CRITICAL findings

1. [obligation_id] [provision] — [verdict] — [one-sentence summary] — [remediation]
2. [...]
3. [...]

### Top remediation recommendations

1. [type] — [obligation_ids] — [timeline]
2. [...]

### EEA-pillar status

[Assessed | Deferred to parallel skill-G/E run | Out of scope]
```

### 2. Per-obligation conformity report (Markdown)

For each obligation, in the format of the worked example in Step 11.

### 3. Conformity scoreboard table (Markdown)

```markdown
| Obligation ID | Provision     | Verdict   | Confidence    | Severity | _Marleasing_? | Direct-effect-ready? | Remediation |
| ------------- | ------------- | --------- | ------------- | -------- | ------------- | -------------------- | ----------- |
| NIS2-21-2-a   | Art. 21(2)(a) | CORRECTLY | LIKELY (0.82) | CRITICAL | n/a           | false                | none        |
| [...]         | [...]         | [...]     | [...]         | [...]    | [...]         | [...]                | [...]       |
```

### 4. JSON conformity schema

A single JSON document. Per-obligation shape follows the Step 11 worked
example. Top-level wraps the directive identification, assessment
metadata, tally, obligations array, remediation recommendations array, and
Glass Box block:

```json
{
  "$schema": "https://legalcode.example/eu-conformity/v1.json",
  "directive": { "celex": "string", "short_title": "string", "eli": "URI" },
  "member_state": "string",
  "assessment": {
    "date": "ISO-8601",
    "mode": "EU_PILLAR | EEA_PILLAR | PRE_LFN | PRE_COURT",
    "persona": "GOVERNMENT | LAW_FIRM | COMPANY | TRADE_FEDERATION",
    "working_language": "ISO-639-1",
    "reconciliation_languages": ["ISO-639-1"]
  },
  "tally": {
    "correctly_transposed": "integer",
    "partially_transposed": "integer",
    "incorrectly_transposed": "integer",
    "not_transposed": "integer",
    "conformity_rate": "number 0..1",
    "compliance_deficit_weight": "number 0..1"
  },
  "obligations": [
    {
      /* per Step 11 */
    }
  ],
  "remediation_recommendations": [
    {
      /* per Step 9 */
    }
  ],
  "glass_box": {
    /* per Glass Box section */
  }
}
```

### 5. AKN4EU `<judgment>` document

A single `<akomaNtoso>` document containing one `<judgment>` element per
obligation, each with the FRBR identification block, references to the
directive and the NIM, and a verdict-bearing `<decision>` plus reasoning
`<motivation>`. Use the `lc:` extension namespace declared in the worked
example for the verdict, confidence, and adversarial-review attributes.

### 6. LegalRuleML rule set

A single `<lrml:LegalRuleML>` document containing one `<lrml:Constitutive>`
per obligation. Each `<lrml:Constitutive>` declares the obligation's
`<lrml:Party>` (the addressee), the directive `<lrml:Source>`, the deontic
operator (`<lrml:Obligation>`, `<lrml:Permission>`, or `<lrml:Prohibition>`),
the verdict, the confidence, the NIM reference, and the _Marleasing_ / direct
effect flags via `lc:` extension elements.

### 7. Glass Box YAML audit trail

Deterministic record of every verdict's reasoning. The full
per-obligation record shape is illustrated in Step 11. Aggregate block
shape:

```yaml
glass_box:
  skill_name: "legalcode-eu-conformity-assessment"
  assessment_date: "[YYYY-MM-DD]"
  assessed_by: "[Role — AI-assisted; must be validated by qualified EU/MS counsel]"
  directive_celex: "[code]"
  directive_short_title: "[short title]"
  directive_eli: "[URI]"
  member_state: "[ISO 3166-1 alpha-2]"
  pillar: "EU | EEA"
  mode: "[mode]"
  persona: "[persona]"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[path or Not created]"
  total_obligations_assessed: [N]
  verdict_tally:
    correctly_transposed: [N]
    partially_transposed: [N]
    incorrectly_transposed: [N]
    not_transposed: [N]
  conformity_rate: [0.00–1.00]
  compliance_deficit_weight: [0.00–1.00]
  obligation_records:
    - { /* per Step 11 worked example */ }
  assumptions: ["..."]
  limitations: ["..."]
  reviewer_note: "AI-assisted — every verdict requires validation by qualified EU and Member State counsel before infringement-procedure use."
```

Glass Box must be parseable YAML. No prose outside the YAML structure; every
comment goes in `reviewer_note` or per-obligation `evidence_chain[].sources`.

---

## Localization Notes

1. Replace `[VERIFY]` markers in the worked example with verified national
   official-journal references (BGBl., JOuRF, GU, Stb., RTS, etc.); confirm
   citation, date, and entry-into-force against the national official journal
   directly, not secondary aggregations.
2. For deadline-passed directives, confirm whether the Commission has opened
   any Article 258 TFEU procedure (skill H).
3. For EEA-EFTA NIM (IS, LI, NO), cross-check the Joint Committee Decision
   incorporating the directive into the EEA Annex (skill G) first. A
   directive not yet incorporated does not bind the EEA-EFTA States.
4. National interpretive method varies. The _Marleasing_ salvage analysis
   must reflect the national tradition (purposive vs. textual; constitutional
   limits on conforming interpretation; criminal-law lex stricta).
5. Sanction ceilings transpose into national-currency equivalents in
   non-Eurozone Member States; preserve the EUR-ceiling logic when applying
   the effective-proportionate-dissuasive standard.
6. For amended directives, confirm whether the NIM was drafted against the
   original or the consolidated text. NIM drafted against an outdated
   consolidated text may have a hidden conformity gap with the latest
   amendment.
7. Mark all locally-researched provisions `[VERIFY]` with confidence
   scoring; record jurisdiction-specific research and sources consulted in
   Glass Box.

---

## Provenance

Created by Legalcode (2026-04-28) as skill E in the seven-skill EU
Legislative Compliance suite. Synthesis based on:

- **TFEU/TEU primary text** — Art. 288(3) TFEU (binding-as-to-result, ELI:
  `https://eur-lex.europa.eu/eli/treaty/tfeu_2008/art_288/oj/eng`); Art. 4(3)
  TEU (sincere cooperation); Art. 17(1) TEU; Art. 258 TFEU; Art. 260(2)
  TFEU; Art. 260(3) TFEU.
- **EEA primary text** — Art. 7, 102, 103 EEA; Art. 31 SCA.
- **CJEU case-law** — _Commission v Belgium_, C-543/17, ECLI:EU:C:2019:573
  (Art. 260(3) penalty); _Commission v Germany_, C-543/09,
  ECLI:EU:C:2010:778 (incomplete transposition); _Commission v Italy_,
  C-456/03, ECLI:EU:C:2005:388 (substantive non-conformity); _Marleasing_,
  C-106/89, ECLI:EU:C:1990:395; _Becker_, C-8/81, ECLI:EU:C:1982:7;
  _Faccini Dori_, C-91/92, ECLI:EU:C:1994:292; _Pfeiffer_, Joined Cases
  C-397/01 to C-403/01, ECLI:EU:C:2004:584; _Foster v British Gas_,
  C-188/89, ECLI:EU:C:1990:313; _Pupino_, C-105/03, ECLI:EU:C:2005:386;
  _Adeneler_, C-212/04, ECLI:EU:C:2006:443; _Inter-Environnement Wallonie_,
  C-129/96, ECLI:EU:C:1997:628; _Commission v Germany_ (DPA independence),
  C-518/07, ECLI:EU:C:2010:125; _CILFIT_, C-283/81, ECLI:EU:C:1982:335;
  _Codan_, C-236/97, ECLI:EU:C:1998:208; _EMU Tabac_, C-296/95,
  ECLI:EU:C:1998:152.
- **Multilingualism** — Regulation 1/1958, ELI:
  `https://eur-lex.europa.eu/eli/reg/1958/1(1)/oj/eng`.
- **Methodology** — Better Regulation Toolbox 2023, Chapter 4
  (`https://commission.europa.eu/document/download/a21336e2-2a7c-43d2-bb35-d4eee7aa4cd3_en?filename=BRT-2023-Chapter+4-Compliance+implementation+and+preparing+proposals_0.pdf`);
  ECN+ Directive (EU) 2019/1, CELEX 32019L0001 — conformity-assessment
  tender, Belgian publication reference 765714.
- **Data feeds** — EUR-Lex Cellar SPARQL
  (`https://publications.europa.eu/webapi/rdf/sparql`); EUR-Lex web service;
  N-Lex; CURIA / InfoCuria (`https://curia.europa.eu/`); EFTA Court register
  (`https://eftacourt.int/`); EEA-Lex (`https://www.efta.int/eealaw`);
  Single Market Scoreboard
  (`https://single-market-scoreboard.ec.europa.eu/`); EFTA Internal Market
  Scoreboard (`https://www.efta.int/`); IATE (`https://iate.europa.eu/`).
- **Standards** — Akoma Ntoso (OASIS LegalDocML 1.0, 2018), AKN4EU subschema
  as used by LEOS; ELI; ECLI; CELEX; LegalRuleML (OASIS, 2021)
  (`https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/`).
- **Worked example** — NIS2 Directive (Directive (EU) 2022/2555, CELEX
  32022L2555, OJ L 333, 27.12.2022, p. 80) and German NIS2UmsuCG —
  Bundesgesetzblatt citation, entry-into-force date, and enacted §-numbers
  marked `[VERIFY]` and confirmed at runtime.
- All statutory references, ECLIs, ELIs, and CELEX codes carry hallucination
  risk and must be verified against authoritative sources (EUR-Lex, CURIA,
  EFTA Court register, national official journals) before use in regulatory
  submissions, Commission infringement-procedure dossiers, ESA reasoned-
  opinion submissions, EFTA Court pleadings, or board reporting.
