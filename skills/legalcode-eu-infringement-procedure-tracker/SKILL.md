---
name: legalcode-eu-infringement-procedure-tracker
description: Tracks the infringement-procedure timeline for a Member State / directive pair under TFEU
  Art. 258 (letter of formal notice → reasoned opinion → CJEU referral) and TFEU Art. 260 (judgment compliance,
  second-stage lump-sum and periodic-penalty proceedings, and the post-Lisbon Art. 260(3) first-referral
  penalty for non-notification of transposition of a legislative directive).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Tracks the infringement-procedure timeline for a Member State / directive pair under TFEU Art. 258 (letter of formal notice → reasoned opinion → CJEU referral) and TFEU Art. 260 (judgment compliance, second-stage lump-sum and periodic-penalty proceedings, and the post-Lisbon Art. 260(3) first-referral penalty for non-notification of transposition of a legislative directive). Mirrors the procedure for EFTA-pillar EEA States (IS, NO, LI) under the Surveillance and Court Agreement (SCA) Arts. 31–32 before the EFTA Surveillance Authority (ESA) and the EFTA Court. Consumes the per-MS implementation matrix from the EU Transposition Tracker (skill C), conformity verdicts from the EU Conformity Assessment (skill E), and EEA-incorporation status from the EEA Incorporation Tracker (skill G), and produces a stage-classified timeline (LFN / RO / CJEU / judgment / Art. 260(2) / Art. 260(3)), a calculated penalty estimate built from the Commission's 2023 Communication on Art. 260(3) methodology and the 2005/2010 Communications on financial sanctions, and a risk score per pair. Cites named instruments including the NIS2 Directive (Directive (EU) 2022/2555, CELEX 32022L2555), the AI Act (Regulation (EU) 2024/1689, CELEX 32024R1689), GDPR (Regulation (EU) 2016/679, CELEX 32016R0679), DORA (Regulation (EU) 2022/2554, CELEX 32022R2554), CSRD (Directive (EU) 2022/2464, CELEX 32022L2464), CSDDD (Directive (EU) 2024/1760, CELEX 32024L1760), and the Commission v Belgium (Case C-543/17, ECLI:EU:C:2019:573), Commission v France (Case C-304/02, ECLI:EU:C:2005:444), Commission v Germany (Case C-503/04, ECLI:EU:C:2007:432), and Commission v Greece (Case C-378/13, ECLI:EU:C:2014:2405) judgments. Operating modes: government persona (defending or self-monitoring), legal firm (client risk advisory), in-house company (exposure forecasting), trade federation (sector-wide pattern). Emits Markdown infringement timeline, JSON schema consumable by the Single Market Scoreboard rollup (transposition deficit, conformity deficit, average resolution time), AKN4EU `<doc>` of class `proceedingEvent`, LegalRuleML `<lrml:Prescriptive>` rule blocks expressing the obligation–violation logic, and a Glass Box audit trail. Jurisdictional scope: EU-27 plus the three EFTA-pillar EEA States (Iceland, Norway, Liechtenstein); not applicable to Switzerland (bilateral agreements; no EEA membership).


# Legalcode EU Infringement Procedure Tracker

> **Disclaimer**: This skill provides a framework for AI-assisted infringement-procedure
> tracking and risk scoring. It does not constitute legal advice and does not create an
> attorney-client relationship. All outputs should be reviewed by qualified legal counsel
> licensed in the relevant jurisdictions before use. This skill does not replace formal
> legal review by qualified EU and Member State counsel. It produces a structured
> framework to support a human-led review — not a substitute for one.
> Citations to EU directives, regulations, CJEU/EFTA Court judgments, and Member State
> implementing measures must be verified against authoritative sources (EUR-Lex, CURIA,
> national official journals) before use in regulatory submissions, infringement
> proceedings, or board reporting. EU law evolves continuously; transposition status,
> infringement procedures, and consolidated text versions change frequently. The 24
> official EU language versions of every act are equally authentic; reconcile divergent
> versions before relying on any single language for a definitive interpretation
> (CILFIT C-283/81; Codan C-236/97; EMU Tabac C-296/95).

## Purpose and Scope

This skill systematically reconstructs the infringement-procedure timeline for a given
Member State / directive pair (or a batch over either dimension) and assigns the pair to a
discrete procedural stage on the EU enforcement ladder: pre-procedural exchange (EU Pilot,
where applicable), letter of formal notice (LFN) under TFEU Art. 258, reasoned opinion (RO)
under Art. 258, referral to the Court of Justice of the European Union under Art. 258
second paragraph, judgment, Art. 260(1) compliance period, Art. 260(2) renewed proceedings
with lump-sum and periodic-penalty proposal, or — for legislative directives only — the
Lisbon-introduced Art. 260(3) first-referral penalty for failure to notify transposition.
For the EFTA pillar of the EEA, the skill mirrors the Commission/CJEU pathway against the
EFTA Surveillance Authority (ESA) and the EFTA Court under SCA Arts. 31–32.

Infringement-procedure tracking sits at the strategic edge of EU compliance work. It
converts the abstract status that "Member State X has not transposed Directive Y" into the
concrete enforcement state ("MS X received an LFN on date D, did not respond within two
months, RO issued on date D′, referral to the CJEU is now expected within Q[n] of [year]")
and quantifies the financial exposure under the Commission's published penalty methodology
(2005 Communication SEC(2005) 1658 as amended; 2023 Communication on Art. 260(3),
C/2022/9404 — verify exact OJ citation and amendments before submission). Because Art.
260(3) was first applied in _Commission v Belgium_ (Case C-543/17, ECLI:EU:C:2019:573) and
because subsequent practice has converged on a relatively predictable lump-sum + daily
penalty structure for non-notification cases, the skill can produce a defensible estimate
of expected sanction even at early procedural stages.

**Covers:**

- Stage classification across the seven procedural states from EU Pilot through Art. 260(2)
  iteration, including the parallel Art. 260(3) track for non-notification cases
- Reconstruction of LFN and RO dates and the response windows that govern escalation
- CJEU referral timing reconstruction from CURIA and Press Corner artefacts
- Calculation of the Commission-proposed lump sum and daily penalty under the 2023
  Communication methodology (flat-rate sanction × duration coefficient × seriousness ×
  n-factor) for both Art. 260(2) and Art. 260(3) cases
- Risk scoring per (MS, directive) pair combining current procedural stage, MS historical
  pattern factor, directive substantive importance, and verdict from the Conformity
  Assessment skill (skill E) where substantive non-conformity is at issue
- ESA / EFTA Court mirror pathway under SCA Arts. 31–32 for IS, NO, LI
- Single Market Scoreboard input computation (transposition deficit, conformity deficit,
  average resolution time, pending-case count, Art. 260 frequency)
- Mitigation-pathway analysis: notification cure for Art. 260(3); NIM amendment cure for
  Art. 258 substantive cases; CJEU settlement positioning; _Marleasing_ (Case C-106/89,
  ECLI:EU:C:1990:395) interpretive cure where the NIM is ambiguous rather than absent
- Standards-based outputs (Markdown, JSON, AKN4EU `proceedingEvent`, LegalRuleML
  prescriptive blocks) and a Glass Box audit trail tying every classification and number
  to its source

**Does not:**

- Run the substantive obligation extraction itself — see `legalcode-eu-directive-analyzer`
- Build the per-MS implementation matrix — see `legalcode-eu-transposition-tracker`
- Produce the Commission-format two-column correlation table — see
  `legalcode-eu-correlation-table-builder`
- Run the per-article conformity check that distinguishes correct / partial / incorrect /
  not transposed — see `legalcode-eu-conformity-assessment`
- Flag national over-implementation — see `legalcode-eu-gold-plating-detector`
- Track EEA Joint Committee Decision incorporation status — see
  `legalcode-eea-incorporation-tracker`
- Provide legal advice or substitute for qualified EU and Member State counsel
- Guarantee enforcement outcomes — Commission discretion governs case selection and the
  CJEU/EFTA Court determines final sanctions

### Sibling Skills in the Suite

This skill is part of the seven-skill EU Legislative Compliance suite. It consumes /
produces the following artefacts:

- **Consumes**: per-MS implementation matrix (skill C, `legalcode-eu-transposition-tracker`),
  per-article conformity verdicts for substantive non-conformity cases
  (skill E, `legalcode-eu-conformity-assessment`), and EEA incorporation status
  (skill G, `legalcode-eea-incorporation-tracker`) for the EFTA-pillar mirror.
- **Produces**: per-(MS, directive) infringement timeline plus risk score, consumed by the
  government persona (defending or self-monitoring), legal firm (client risk advisory),
  in-house company (exposure forecasting), and trade federation (sector-wide pattern).

Sibling skills (use whichever is appropriate for the user's stage in the lifecycle):

- `legalcode-eu-directive-analyzer` — extracts the obligation register from a directive
- `legalcode-eu-transposition-tracker` — per-MS implementation matrix
- `legalcode-eu-correlation-table-builder` — directive-to-NIM correlation table
- `legalcode-eu-conformity-assessment` — per-article transposition verdict
- `legalcode-eu-gold-plating-detector` — flags national over-implementation
- `legalcode-eea-incorporation-tracker` — EEA Joint Committee Decision tracking
- `legalcode-eu-infringement-procedure-tracker` — TFEU 258/260 procedure timeline (this skill)

See [shared EU legislative-data pack](references/eu-legislative-data/)
for the suite-wide reference data (CELEX-to-ELI mapping conventions, Member State
abbreviation table, OJ-language reconciliation rules, IATE termbase pointers, and
authoritative source URLs).

---

## Jurisdiction and Governing Law

This skill operates over the EU-27 Member States plus the three EFTA-pillar EEA States
(Iceland, Norway, Liechtenstein). Switzerland is excluded — it is neither an EU Member
State nor an EEA Contracting Party, and its bilateral-agreement relationship with the EU
does not produce CJEU- or EFTA-Court-mediated infringement procedures.

**EU pillar (TFEU Arts. 258, 260; Art. 288 instrument hierarchy):**

- Art. 258 TFEU — Commission infringement procedure: Commission delivers a reasoned opinion
  after giving the Member State an opportunity to submit observations; on continued
  non-compliance the Commission may bring the matter before the Court of Justice. ELI:
  `https://eur-lex.europa.eu/eli/treaty/tfeu_2008/art_258/oj/eng`
- Art. 260(1) TFEU — Member State obligation to take the measures necessary to comply with
  a CJEU judgment.
- Art. 260(2) TFEU — second-stage procedure: where the Commission considers a Member State
  has not taken the necessary measures, after giving the State the opportunity to submit
  observations, the Commission may bring the case before the Court and propose a lump-sum
  or penalty payment. ELI:
  `https://eur-lex.europa.eu/eli/treaty/tfeu_2008/art_260/oj/eng`
- Art. 260(3) TFEU — Lisbon-introduced power: where the Commission brings a case under
  Art. 258 because the Member State has failed to fulfil its obligation to notify measures
  transposing a directive adopted under a legislative procedure, it may, when it deems
  appropriate, specify the amount of the lump-sum or penalty payment to be paid; the
  Court may, if it finds that there is an infringement, impose a sanction not exceeding
  the amount specified by the Commission.
- Art. 288 TFEU — directives are binding as to the result to be achieved upon each Member
  State to which they are addressed but leave the choice of form and methods to the
  national authorities. ELI:
  `https://eur-lex.europa.eu/eli/treaty/tfeu_2008/art_288/oj/eng`

**EEA / EFTA pillar (SCA Arts. 31–32; EEA Art. 109):**

- SCA Art. 31 — ESA reasoned-opinion procedure mirroring TFEU Art. 258 against IS, NO, LI.
- SCA Art. 32 — referral to the EFTA Court mirroring CJEU referral.
- EEA Art. 109(1) — duty of EEA Joint Committee to ensure surveillance.
- ESA does not currently operate an Art. 260(3)-equivalent first-referral penalty
  mechanism, and the EFTA Court does not impose the structurally identical lump-sum +
  periodic-penalty regime; non-compliance findings are declaratory and politically
  enforceable through the EEA Joint Committee. [VERIFY current ESA practice and any 2024–2025
  updates to its penalty position.]

**Authority and methodology sources:**

- _Commission v Belgium_, Case C-543/17, ECLI:EU:C:2019:573 — first application of Art.
  260(3); Court accepted the Commission's proposed daily penalty structure for failure to
  notify transposition of Directive 2014/61/EU on broadband cost reduction; clarified that
  Art. 260(3) applies only where the failure is the failure to notify (whether complete or
  partial / incorrect) the transposing measures, not the failure to transpose substantively
  correctly. [VERIFY exact paragraph numbering and the precise penalty figure imposed.]
- _Commission v France_, Case C-304/02, ECLI:EU:C:2005:444 — first cumulation of lump sum
  and periodic penalty under Art. 228 EC (now Art. 260(2) TFEU); confirmed that the two
  sanction types serve different purposes (lump sum punishes past non-compliance, periodic
  penalty incentivises future compliance) and may therefore be cumulated. [VERIFY exact
  amounts.]
- _Commission v Germany_, Case C-503/04, ECLI:EU:C:2007:432 — Art. 228 EC (now 260(2))
  iteration confirming that compliance after the reasoned opinion but before judgment does
  not extinguish the lump-sum exposure for past non-compliance.
- _Commission v Greece_, Case C-378/13, ECLI:EU:C:2014:2405 — Art. 260(2) lump-sum and
  periodic penalty for failure to recover unlawful state aid.
- Commission Communication on the Application of Art. 260(3) TFEU (2023; superseding the
  2011 SEC(2010) 1371 final and 2017 update) — penalty calculation methodology for
  non-notification cases. URL:
  `https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:52023XC0104(01)`
  [VERIFY exact CELEX assignment for the 2023 Communication; the text on EUR-Lex should
  be checked against the current consolidated version before any submission.]
- Commission Communication on the application of Art. 228 EC, SEC(2005) 1658, with 2010,
  2018, 2019, 2020, 2022 and 2023 updates of the n-factor and the standard flat-rate
  amount. [VERIFY the most recent n-factor table and lump-sum / daily-penalty amounts on
  the date of any submission.]
- Single Market and Competitiveness Scoreboard infringement methodology:
  `https://single-market-scoreboard.ec.europa.eu/enforcement-tools/infringements_en`.
- ESA Internal Market Scoreboard (EFTA pillar): `https://www.efta.int/`.

**Multilingualism rule (binding):** every authentic-language version of an EU act has
equal legal force (Regulation 1/1958; CILFIT C-283/81; Codan C-236/97; EMU Tabac
C-296/95). Where this skill cites a specific provision in English, the user must
reconcile against the language version in which the LFN, RO or judgment was issued
before relying on the citation in any submission.

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

For batch / non-interactive runs, use these defaults:

- Persona: Government — self-monitoring (most defensive baseline)
- Procedure pillar: EU pillar (TFEU 258/260) only; mirror EFTA pillar only if the input
  identifies an EEA-pillar State
- Penalty methodology version: Commission 2023 Communication for Art. 260(3); 2005
  Communication SEC(2005) 1658 with most recent n-factor update for Art. 260(2)
- Risk-scoring weights: balanced (procedural stage 0.4, MS pattern 0.2, directive
  importance 0.2, conformity verdict 0.2)
- Output: all four formats (Markdown, JSON, AKN4EU, LegalRuleML) plus Glass Box

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:

- **Single (MS, directive) pair**: e.g. "DE × NIS2" — the canonical mode; produces one
  full timeline plus risk score
- **Batch over a directive**: a directive identifier (CELEX or short title) and a request
  to evaluate all 27 EU MS (and optionally the three EEA-pillar States); produces a
  cross-MS scoreboard for that directive
- **Batch over a Member State**: an MS code (DE, FR, IT, ES, …) and a request to evaluate
  every directive currently in an active infringement procedure against that MS;
  produces an MS-level exposure profile
- **Watchlist**: a curated set of (MS, directive) pairs and a request to monitor each
  for stage transitions
- **Re-assessment**: a previously emitted JSON timeline plus a request to update for
  new procedural events (e.g. new RO issued; case referred to CJEU)

**Minimum required context to proceed:**

- The directive's CELEX identifier (e.g. `32022L2555` for NIS2) or a short title
  unambiguous enough to resolve to a single CELEX
- The Member State (or batch dimension)
- The reference date for the assessment (defaults to today; explicit when reconstructing
  historical exposure for litigation or due-diligence purposes)

If any of these is missing, prompt the user. Do not invent a CELEX or guess a directive.

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

**Persona-driven branching for this skill specifically:**

- **Government — defending**: timeline is reconstructed from the MS Permanent
  Representation perspective; the output emphasises observable Commission state
  (LFN/RO sent on dates D, D′; outstanding response window; SOLVIT, EU Pilot, or
  pre-LFN dialogue evidence) and orders mitigation pathways by political cost
  (notification < remedial NIM amendment < CJEU defence < settlement). Penalty
  estimates are framed as upper-bound exposure; defensive arguments (force majeure;
  procedural irregularity; n-factor recalculation) are surfaced.
- **Government — self-monitoring**: timeline is reconstructed identically but the
  output is consumed by the ministry's transposition coordination unit; the
  emphasis is internal accountability (which department is responsible; which NIM
  amendment is overdue) rather than external defence.
- **Legal firm**: timeline is reconstructed from public sources; output is framed as
  client-risk advisory; cross-MS comparative scoreboard is produced where the
  client operates in multiple MS; penalty estimate is presented as expected value
  (Commission-proposed amount × probability of CJEU acceptance) rather than upper
  bound.
- **Company / in-house**: timeline is filtered to the directive(s) materially
  affecting the company's operations; the risk score is converted to the impact on
  the company (delayed market entry; regulatory uncertainty; supply-chain
  exposure) rather than the impact on the MS.
- **Trade federation**: timeline is aggregated across MS for a single directive to
  produce a sector-wide pattern view; the output supports federation policy
  positions calling for harmonised transposition or Commission action.

### Step 3: Resolve Inputs

Resolve the input pair into a fully-specified analytical context.

**3a. Directive resolution.** From the CELEX or short title, retrieve:

- Formal title and OJ reference
- Adoption date and entry-into-force date (Art. 297 TFEU rules; usually 20 days after
  OJ publication unless the directive specifies otherwise)
- **Transposition deadline** under the directive's final article — this is the date that
  starts the Art. 258 / Art. 260(3) clock for non-notification cases
- EEA-relevance flag (text "EEA relevance" in title; if present, route the EFTA-pillar
  mirror analysis through skill G's EEA-incorporation status)
- Whether adopted under the ordinary legislative procedure (Art. 294 TFEU) — required
  for Art. 260(3) eligibility (the provision applies only to legislative directives)

**3b. Member State resolution.** Confirm the MS belongs to:

- EU-27: route through Commission / CJEU pillar (TFEU 258/260)
- EFTA-pillar EEA States (IS, NO, LI): route through ESA / EFTA Court pillar (SCA 31/32)
- Switzerland: not in scope — emit the diagnostic and stop

**3c. Implementation status from skill C (transposition tracker).** Retrieve the
per-MS implementation matrix entry for the (MS, directive) pair. If skill C has not been
run against this pair, prompt the user to run it (or proceed with a `[VERIFY — implementation
status not confirmed via skill C]` flag and the publicly observable proxy: presence or
absence of the MS notification on the Commission's transposition database for the
directive).

**3d. Conformity verdict from skill E (conformity assessment) for substantive cases.**
Retrieve the per-article verdict matrix where any article is flagged `incorrect` or
`partial`. These verdicts feed Art. 258 substantive-non-conformity risk; non-notification
cases (Art. 260(3)) do not require this input. If skill E has not been run, proceed with
the implementation matrix alone and flag substantive risk as `[ASSUMED — no conformity
verdict available]`.

**3e. EEA incorporation status from skill G** for EFTA-pillar mirror cases. Retrieve the
EEA Joint Committee Decision (JCD) status for the directive — incorporation, with or
without adaptations, and whether constitutional reservations under EEA Art. 103 have
suspended entry-into-force in any EFTA State.

⟁ CLARIFY — Reference date

The reference date determines which procedural events are "in the past" and therefore
observed, versus "in the future" and therefore projected.

1. **Today (default)**: current state of play; produces actionable risk score
2. **Specific historical date**: e.g. acquisition due-diligence reference date
3. **Projected future date**: e.g. "what is the expected state in 6 months if no MS action"

**Why this matters**: A historical reference date excludes events occurring after that
date even if they are now public; a projected date adds estimated future events with
explicit confidence markers.

### Step 4: Discover Open Procedures

Reconstruct the publicly-observable procedural state of the (MS, directive) pair from the
following sources, in order of authoritativeness:

| Source                                                                     | Coverage                                                                                            | Authority                                             |
| -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Commission INFR database (via the Single Market Scoreboard linked dataset) | LFN, RO, CJEU referral, Art. 260 events                                                             | Authoritative for Commission-side events              |
| Commission Press Corner monthly infringements package                      | Public summary of LFN / RO / CJEU referral / closure decisions                                      | Authoritative date stamp                              |
| CURIA case search (`https://curia.europa.eu/`)                             | Pending and closed CJEU cases; case number; ECLI; oral hearing date; AG opinion date; judgment date | Authoritative for CJEU-side events                    |
| OJ C-series notices                                                        | Lodgement of an action (Art. 263 / 258 / 260 reference) and judgment publication                    | Authoritative date stamp                              |
| ESA Annual Report and EFTA Court register (`https://eftacourt.int/cases/`) | EFTA-pillar mirror events                                                                           | Authoritative for ESA / EFTA Court events             |
| National parliament and ministry archives                                  | Internal MS response records to LFN / RO                                                            | Persona-bounded; only available to government persona |

**4a. Commission-side events.** For each (MS, directive) pair, search the Commission
infringement decision databases for:

- LFN issuance date and INFR procedure number (format `INFR(YYYY)NNNN`)
- RO issuance date (if any)
- Referral decision date (College of Commissioners decision to refer to the CJEU)
- Press Corner reference for each event
- Closure date and ground (Art. 258 cases close on notification of compliance; Art. 260(3)
  cases close on notification of transposition)

**4b. CJEU-side events.** For pairs with a referral, retrieve from CURIA:

- Case number (format `C-NNN/YY`)
- Lodgement date (date the Registry recorded the action)
- ECLI for the eventual judgment
- Whether an Advocate General opinion has been delivered (date)
- Judgment date and operative-part summary
- For Art. 260(3) cases: the Commission's specified lump-sum and daily penalty amounts
  and whether the Court imposed those amounts, lower amounts, or no penalty

**4c. ESA / EFTA Court mirror.** For EFTA-pillar States, search the ESA register for:

- ESA reasoned opinion under SCA Art. 31
- EFTA Court action under SCA Art. 32 (case number format `E-NN/YY`)
- EFTA Court judgment

**4d. Provenance recording.** Every event recorded must carry:

- The source URL (Press Corner, CURIA, EFTA Court register)
- The retrieval timestamp
- A confidence marker (VERIFIED / LIKELY / VERIFY / ASSUMED) per Section: Confidence
  Scoring below

⟁ CLARIFY — Source set

Some pairs have multiple Commission procedure numbers (a non-notification case under
Art. 260(3) and a parallel substantive non-conformity case under Art. 258).

1. **Single procedure**: pair has one INFR identifier; full timeline reconstructed against
   that identifier
2. **Parallel procedures**: pair has both a non-notification track and a substantive
   non-conformity track; both are tracked, distinguished, and the risk score combines them
3. **Closed procedure with potential reopening**: pair previously had a closed procedure
   that may be reopened on new evidence

**Why this matters**: parallel-procedure pairs require both tracks to be reconstructed;
closing one does not extinguish the other.

### Step 5: Stage Classification

Assign the pair to exactly one primary stage on the EU enforcement ladder, plus zero or
one "parallel-track" stages where Art. 258 substantive and Art. 260(3) non-notification
proceedings run together.

**EU pillar stages (TFEU 258 → 260):**

| Stage code | Name                            | Trigger event                                                                                                                     | Typical duration to next stage                                                                             |
| ---------- | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `S0`       | No procedure open               | No INFR identifier; transposition deadline either not yet passed or compliance notified on time                                   | n/a — pair is not an enforcement subject                                                                   |
| `S1`       | EU Pilot / pre-procedural       | Commission informal dialogue; no LFN issued                                                                                       | Indefinite — Pilot is unstructured                                                                         |
| `S2`       | Letter of Formal Notice (LFN)   | LFN issued under Art. 258 first paragraph; MS has two months to respond                                                           | 6–18 months to RO if no resolution                                                                         |
| `S3`       | Reasoned Opinion (RO)           | Reasoned opinion issued under Art. 258 first paragraph; MS has two months (often extended) to comply                              | 6–18 months to CJEU referral if no resolution                                                              |
| `S4`       | CJEU referral                   | College decision to refer; lodgement at CJEU Registry                                                                             | 12–24 months to judgment for written procedure cases                                                       |
| `S5`       | Judgment under Art. 258         | CJEU judgment finding the infringement (declaratory)                                                                              | Art. 260(1) compliance period — informally 12 months unless directive substantive complexity dictates more |
| `S6`       | Art. 260(2) renewed proceedings | Commission considers MS has not complied; second LFN issued under Art. 260(2)                                                     | 6–18 months to second referral                                                                             |
| `S7`       | Art. 260(2) judgment            | Court imposes lump sum and / or periodic penalty                                                                                  | Compliance under Art. 260(1) restored                                                                      |
| `T3`       | Art. 260(3) parallel track      | Commission specifies lump sum / penalty in the Art. 258 referral for non-notification of transposition of a legislative directive | Resolved in the Art. 258 judgment — single judgment imposes Art. 260(3) sanction                           |

**EFTA pillar stages (SCA 31 → 32):**

| Stage code | Name                                   | Trigger event                                                                                           |
| ---------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `F0`       | No procedure                           | n/a                                                                                                     |
| `F1`       | ESA preliminary letter                 | Mirror of EU Pilot                                                                                      |
| `F2`       | ESA reasoned opinion under SCA Art. 31 | Mirror of S3                                                                                            |
| `F3`       | EFTA Court action under SCA Art. 32    | Mirror of S4                                                                                            |
| `F4`       | EFTA Court judgment                    | Mirror of S5; declaratory only — no Art. 260(3)-equivalent penalty regime [VERIFY current ESA practice] |

**Stage-classification rules:**

1. Assign the most advanced stage observed in publicly verifiable evidence, with a
   confidence marker.
2. Where the LFN date is known but no later event is publicly observable, classify as
   `S2` and project the expected `S3` window (LFN date + 12 months ± 6, with calibration
   from the MS historical pattern factor).
3. Where Art. 260(3) was specified in the LFN or RO (the Commission's standard practice
   since 2017), tag the case `T3` regardless of whether the substantive Art. 258 stage is
   `S2`, `S3`, or `S4`.
4. Where the procedure has been closed, record the closure date and tag the case `S0`
   with a `was=` predecessor stage in the JSON output.

### Step 6: Penalty Calculation

Apply the Commission's published methodology — see Section: Article 260(3) Penalty
Methodology and Section: Article 260(2) Penalty Methodology below for the full
parameter definitions, formulae, and worked examples (including the NIS2 worked
example for Art. 260(3) and the _Commission v France_ worked example for Art. 260(2)).
For each pair, populate the input table:

| Parameter               | Symbol                                                | Where it comes from                                            |
| ----------------------- | ----------------------------------------------------- | -------------------------------------------------------------- |
| Daily-penalty flat rate | `R_daily`                                             | 2023 Communication [VERIFY]                                    |
| Lump-sum flat rate      | `R_lump`                                              | 2023 Communication [VERIFY]                                    |
| Per-MS minimum lump sum | `LS_min`                                              | n-factor table [VERIFY]                                        |
| Seriousness coefficient | `C_s`                                                 | 1–20; Commission's per-case discretion (rationale required)    |
| Duration coefficient    | `C_d`                                                 | 1–3 typical; days past deadline / time since Art. 258 judgment |
| n-factor                | `n`                                                   | Most recent published n-factor table [VERIFY]                  |
| Days past deadline      | `N_days_past` (Art. 260(3)) or `N_days` (Art. 260(2)) | Computed                                                       |

Compute `Daily penalty = R_daily × C_s × C_d × n` and `Lump sum = max(LS_min × n,
R_lump × C_s × N_days × n)`. Mark the calculation `[VERIFY]` until the Commission's
specified figures for the actual case have been obtained from the LFN, RO, referral
application, or Press Corner summary.

⟁ CLARIFY — n-factor

The n-factor reflects MS GDP and institutional weight; the Commission updates it
periodically (2010, 2018, 2019, 2020, 2022, 2023).

1. **Current n-factor**: most recent table (2023 Communication or later)
2. **Historical n-factor at procedure-opening date**: for litigation reconstruction
3. **Projected n-factor**: not available; use current as proxy with explicit flag

**Why this matters**: Court practice is to apply the n-factor in force at the date of
the judgment, not the date of the LFN; a 2018-era versus 2023-era n-factor for the same
MS can differ by 5–15%.

### Step 7: Risk Scoring

The risk score combines four orthogonal axes. Each axis is scored 1–5; the composite is a
weighted sum.

**Axis 1 — Procedural stage (`R_stage`):**

| Stage                                   | Score |
| --------------------------------------- | ----- |
| `S0` / `F0`                             | 1     |
| `S1` / `F1`                             | 2     |
| `S2` / `T3`                             | 3     |
| `S3` / `F2`                             | 4     |
| `S4` / `S5` / `S6` / `S7` / `F3` / `F4` | 5     |

**Axis 2 — MS historical pattern factor (`R_pattern`):**

Calibrated from the MS's published infringement statistics in the Single Market Scoreboard.

| Pattern                                                                                                           | Score |
| ----------------------------------------------------------------------------------------------------------------- | ----- |
| MS rarely subject to LFN (< 25 open cases at last Scoreboard) and rarely loses (< 5 Art. 258 judgments / 5 years) | 1     |
| MS occasionally subject to LFN (25–50 open cases) and occasionally loses (5–10 judgments)                         | 2     |
| MS regularly subject to LFN (50–80 open cases) and regularly loses (10–15)                                        | 3     |
| MS frequently subject to LFN (80–110 open cases) and frequently loses (15–25)                                     | 4     |
| MS habitually subject to LFN (>110 open cases) or has Art. 260 history in the last 5 years                        | 5     |

[VERIFY exact thresholds against the most recent Single Market Scoreboard release.]

**Axis 3 — Directive substantive importance (`R_directive`):**

| Importance                                                                                                                                                                                       | Score |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----- |
| Implementing or technical / minor amending act with limited substantive obligations                                                                                                              | 1     |
| Directive of average policy weight; routine sectoral measure                                                                                                                                     | 2     |
| Directive cited by the Commission in current strategic priorities (e.g. Single Market, Digital, Green Deal); standard penalty parameters                                                         | 3     |
| Directive central to a current Commission flagship initiative (e.g. NIS2 cybersecurity; CSRD sustainability reporting; CSDDD due diligence); elevated seriousness coefficient typically proposed | 4     |
| Directive central to a Treaty-level value (e.g. internal market, fundamental rights, EU financial interests); maximum seriousness coefficient typically proposed                                 | 5     |

**Axis 4 — Conformity verdict (`R_conformity`):**

Drawn from skill E (Conformity Assessment) verdicts where available.

| Verdict mix                                                                      | Score |
| -------------------------------------------------------------------------------- | ----- |
| All articles correct (no substantive risk)                                       | 1     |
| Mostly correct with isolated `partial` verdicts                                  | 2     |
| Substantial `partial` mix; some `incorrect` verdicts on non-core articles        | 3     |
| `Incorrect` verdicts on core articles                                            | 4     |
| `Not transposed` on core articles or systematic `incorrect` across the directive | 5     |

If skill E has not run for this pair, default `R_conformity = 3` and flag `[ASSUMED]`.

**Composite risk score:**

```
R = w_stage × R_stage + w_pattern × R_pattern + w_directive × R_directive + w_conformity × R_conformity
```

Default weights: `w_stage = 0.4`, `w_pattern = 0.2`, `w_directive = 0.2`, `w_conformity =
0.2`. The result is a number in `[1, 5]`; tier the result:

| Score range     | Tier         | Meaning                                                                   |
| --------------- | ------------ | ------------------------------------------------------------------------- |
| `R ≥ 4.0`       | **CRITICAL** | CJEU referral imminent or judgment imposed; immediate mitigation required |
| `3.0 ≤ R < 4.0` | **HIGH**     | RO issued or pending; Art. 260(3) sanction risk material                  |
| `2.0 ≤ R < 3.0` | **MEDIUM**   | LFN issued or expected; mitigation pathway feasible                       |
| `R < 2.0`       | **LOW**      | No procedure or early dialogue; routine monitoring                        |

⟁ CLARIFY — Weighting

Default weights treat procedural stage twice as heavily as the other axes. Some persona
contexts justify reweighting.

1. **Default (balanced)**: `0.4 / 0.2 / 0.2 / 0.2`
2. **Stage-dominant** (litigation defence): `0.6 / 0.15 / 0.15 / 0.10`
3. **Substance-dominant** (in-house exposure): `0.25 / 0.15 / 0.30 / 0.30`
4. **Pattern-dominant** (cross-MS comparison): `0.25 / 0.4 / 0.2 / 0.15`

**Why this matters**: a litigation-defence persona cares overwhelmingly about the
imminent procedural stage; a federation cares about cross-MS pattern; a company cares
about whether the directive substantively matters to its operations.

### Step 8: 3-Pass Self-Interrogation for CRITICAL and HIGH

For every (MS, directive) pair classified CRITICAL or HIGH, apply this adversarial
3-pass review before delivering the finding.

**Pass 1 — Procedural-chain integrity.** Does the CRITICAL/HIGH classification follow
logically from the events recorded? State the single piece of evidence most critical to
this classification. If it is `[VERIFY]` or `[ASSUMED]` rather than `[VERIFIED]`, what
would the score be under the opposite assumption? If the classification changes
significantly, lower the confidence level and note it inline.

**Pass 2 — Mitigation already in flight.** Has the MS taken a public action that resolves
the underlying infringement (e.g. notified transposition since the last Press Corner
package; gazetted a remedial NIM; agreed a settlement-in-principle visible from a
ministry press release)? If yes, lower the stage score and flag `[mitigation observed]`.

**Pass 3 — Strategic Commission posture.** Is the Commission's current strategic posture
toward this MS / directive consistent with the elevated risk score? Examples:

- Commission has publicly identified the directive as a flagship enforcement priority
  (e.g. NIS2 in the 2024–2025 cybersecurity strategy) — maintain or elevate
- Commission has publicly de-prioritised this directive (e.g. announced a fitness check or
  proposed amendment) — consider lowering CRITICAL to HIGH
- Commission has settled similar cases informally — consider lowering with explicit
  `[VERIFY enforcement posture]`

### Step 9: Compute Single Market Scoreboard Inputs

For every directive analysed (single-pair mode produces a one-row scoreboard; batch modes
populate the full table), compute the inputs that the Commission's Single Market and
Competitiveness Scoreboard methodology aggregates. The Scoreboard is published periodically
by DG GROW; the methodology page is the authoritative reference:
`https://single-market-scoreboard.ec.europa.eu/enforcement-tools/infringements_en`.

| Indicator                                           | Definition                                                                                              | Source for this skill                                                 |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **Transposition deficit %**                         | Share of directives a MS has not yet notified as transposed by the deadline, of all directives in force | Skill C implementation matrix, restricted to directives past deadline |
| **Conformity deficit %**                            | Share of notified-but-incorrect transpositions, of all notified transpositions                          | Skill E conformity verdicts (`incorrect` or `partial`)                |
| **Average duration of open infringements (months)** | Mean of (now − LFN date) across all open INFR cases for the MS                                          | Step 4 event reconstruction                                           |
| **Long-overdue cases count**                        | Open INFR cases with LFN date > 18 months without RO; or RO date > 18 months without referral           | Step 4                                                                |
| **Art. 260 frequency**                              | Count of Art. 260(2) judgments delivered against the MS in the trailing 5 years                         | Step 4                                                                |
| **Average resolution time (months)**                | Mean of (closure date − LFN date) across closed INFR cases for the MS                                   | Step 4                                                                |

The skill emits these indicators per MS (in batch-over-directive mode) or per directive
(in batch-over-MS mode) and packages them into the JSON output's `scoreboard_inputs`
section.

### Step 10: Generate Mitigation Recommendations

Mitigation pathways for each (MS, directive, stage) combination. Order by political /
operational cost (lowest first):

| Stage                   | Pathway 1 (cheapest)                                                                                                              | Pathway 2                                                                    | Pathway 3 (highest cost)                                                                                            |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `S2` (LFN)              | Notification of transposition (cures Art. 260(3) immediately; cures Art. 258 on substantive non-notification)                     | Remedial NIM amendment (cures substantive non-conformity)                    | Defence on the merits in response to LFN                                                                            |
| `S3` (RO)               | Notification of transposition with remedial NIM if substantive                                                                    | Settlement dialogue with the Commission                                      | Pre-CJEU defence preparation                                                                                        |
| `S4` (referral)         | Compliance before judgment (extinguishes periodic penalty exposure but not lump-sum exposure per _Commission v Germany_ C-503/04) | CJEU defence on the merits                                                   | Preparation for adverse judgment and Art. 260(1) compliance                                                         |
| `S5` (judgment)         | Art. 260(1) compliance: NIM enactment, notification, evidence package to Commission                                               | Force-majeure / impossibility defence (rarely successful)                    | Politically negotiated extended compliance                                                                          |
| `S6`–`S7` (Art. 260(2)) | Compliance to extinguish periodic penalty                                                                                         | n-factor and seriousness-coefficient challenge in the CJEU written procedure | Settlement on a reduced lump-sum                                                                                    |
| `T3` (Art. 260(3))      | Notification — cures the procedure outright                                                                                       | n-factor and seriousness-coefficient challenge                               | Defence on the eligibility of Art. 260(3) (only available where the case is also a substantive non-conformity case) |

**Special pathway: _Marleasing_ interpretive cure.** Where the NIM is ambiguous rather than
absent or substantively wrong, national courts are obliged so far as possible to interpret
national law in conformity with the directive (_Marleasing_, Case C-106/89, ECLI:EU:C:1990:395,
paragraph 8). This is not a complete substitute for transposition but can defuse the
substantive Art. 258 case; it does not affect Art. 260(3) since that procedure tracks
notification rather than substantive conformity.

**Special pathway: SOLVIT for individual cases.** SOLVIT is not an enforcement tool but a
problem-solving network for cross-border individual cases; useful as evidence of MS
cooperation in submissions to the Commission.

### Step 11: Emit Outputs

Generate all four output formats plus the Glass Box audit trail per Section: Output
Format Template below.

### Step 12: Quality Gates

Apply the citation-quality gates per Section: Citation Quality Gates below before
delivering. Any gate failure requires rework or the addition of `[VERIFY]` markers and
a downward confidence adjustment.

---

## Infringement Procedure Lifecycle

The skill reconstructs procedural events from heterogeneous sources and projects the
next likely event with a defensible duration estimate. The durations below are medians
with substantial variance, calibrated from published Commission practice and Single
Market Scoreboard methodology.

### Stage S2 — Letter of Formal Notice (Art. 258 first paragraph)

**Trigger.** Commission identifies a potential infringement: (a) absence of transposition
notification by the deadline; (b) complaint by an individual, business, or another MS;
(c) own-initiative review (common for flagship directives — NIS2, AI Act); or (d)
conclusion of an EU Pilot dialogue.

**Statutory timing.** Art. 258 first paragraph requires "an opportunity to submit
observations"; Commission practice sets a two-month response window (sometimes one month
for non-notification). No statutory minimum period.

**Discretionary timing.** Extensions are routine on reasoned request for substantive
LFNs; rare for Art. 260(3) non-notification cases (cure is to notify, not to extend).

**Closure path.** Notification of transposition (non-notification track); convincing
observations on the merits; remedial NIM adoption and notification.

**Escalation path.** Window expires → College of Commissioners decides to issue an RO.

### Stage S3 — Reasoned Opinion (Art. 258 first paragraph)

**Trigger.** Commission formalises its position after considering the MS's observations
(or non-response) and sets a compliance period (standard: two months).

**Statutory timing.** Art. 258 first paragraph specifies a "period laid down by [the
Commission]"; extensions on reasoned request are conservative.

**Closure path.** Compliance and notification within the RO period.

**Escalation path.** Period expires → College decides referral to the CJEU under Art. 258
second paragraph.

### Stage S4 — CJEU Referral (Art. 258 second paragraph)

**Trigger.** College decision; Legal Service prepares the application; Registry lodges it.

**Procedure.** Written exchanges; AG opinion (sometimes dispensed with); oral hearing
(sometimes dispensed with); judgment.

**Statutory timing.** None. Median duration from lodgement to judgment: 12–18 months for
non-notification cases; 18–30 months for substantive non-conformity cases. [VERIFY against
the most recent CJEU Annual Report.]

**Art. 260(3) joinder.** Standard Commission practice since the 2017 Communication update
is to include Art. 260(3) lump-sum and daily-penalty specifications in the application
itself; the Court rules on Art. 258 and Art. 260(3) in a single judgment.

### Stage S5 — Art. 258 Judgment / Art. 260(1) Compliance Period

**Effect.** Declaratory finding plus order to take the measures necessary to comply. Where
Art. 260(3) was invoked, the operative part also imposes the lump-sum and/or daily
penalty up to the Commission's specified amount (the Court may impose less, but not more
— _Commission v Belgium_, Case C-543/17, ECLI:EU:C:2019:573, paragraph [VERIFY]).

**Compliance period.** Art. 260(1) requires "necessary measures to comply"; Commission
practice expects compliance "without undue delay" — typically 12 months for
non-notification cures, 18–24 months for substantive cases requiring new NIM.

### Stage S6 — Art. 260(2) Renewed Proceedings

**Trigger.** Commission considers compliance has not been achieved. Renewed LFN under
Art. 260(2); response window; College decision to refer with proposed lump-sum and/or
periodic-penalty amounts.

**Lisbon simplification.** Pre-Lisbon Art. 228 EC required a renewed reasoned opinion;
post-Lisbon Art. 260(2) goes directly from LFN to referral.

### Stage S7 — Art. 260(2) Judgment

**Effect.** Lump-sum, periodic penalty, or both (cumulation principle from _Commission v
France_, Case C-304/02, ECLI:EU:C:2005:444). Unlike Art. 260(3), the Court is not capped
at the Commission's proposed amount. Lump-sum payable on judgment; periodic penalty until
the Commission notifies the Court of compliance.

### Parallel track T3 — Art. 260(3) (Lisbon innovation)

**Eligibility (cumulative):**

1. Case brought under Art. 258 (LFN and RO issued; College referral decision);
2. Infringement is failure to notify measures transposing a directive;
3. Directive adopted under a legislative procedure (Art. 294 ordinary or Art. 289(2)
   special). Implementing/delegated acts (Arts. 290–291) are ineligible.

**Scope of "failure to notify".** _Commission v Belgium_ (C-543/17) confirmed that Art.
260(3) covers absent or partial notification of transposing measures, but does not cover
substantive non-conformity of measures already notified — that remains litigated under
Art. 258 alone or, after first judgment, Art. 260(2). [VERIFY paragraph numbers.]

**Procedure.** Commission specifies lump-sum and/or daily-penalty figures in the
referral application; Court rules on Art. 258 and Art. 260(3) in a single judgment.

**Court's capped discretion.** Art. 260(3) final sentence: the Court may impose a
sanction "not exceeding the amount specified by the Commission" — the structural
difference from Art. 260(2).

---

## Article 260(3) Penalty Methodology

The Commission's 2023 Communication on Art. 260(3) TFEU is the canonical methodology
reference; it consolidates the 2010 SEC(2010) 1371 final, the 2017 Communication update,
and the periodic n-factor table revisions. URL:
`https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:52023XC0104(01)`. **Verify
the CELEX assignment and the current text on EUR-Lex before any submission.**

### Calculation components

**Daily penalty** = `R_daily × C_s × C_d × n`. Where:

- `R_daily` — Commission flat-rate daily-penalty amount; recent practice in low thousands
  of euros (specific figure in the 2023 Communication; [VERIFY]).
- `C_s` — seriousness coefficient (1–20). Factors include directive importance for the
  internal market, fundamental rights, the four freedoms, Union policies, effects on
  individuals and economic operators, and impact on the EU budget. [VERIFY enumerated
  factors against the 2023 Communication.]
- `C_d` — duration coefficient (typically 1–3) based on time between the end of the
  transposition deadline and the Commission's referral decision.
- `n` — n-factor for the MS; updated periodically in the Communication.

**Lump sum** = `max(LS_min × n, R_lump × C_s × N_days_past × n)`. Where `LS_min × n` is
the per-MS minimum from the n-factor table, `R_lump` is the flat-rate lump-sum factor,
and `N_days_past` is days from the end of the transposition deadline to the date of
judgment (or the date of full notification, if earlier).

### _Commission v Belgium_ (C-543/17) worked example

The case concerned Belgium's failure to notify measures transposing Directive 2014/61/EU
on broadband cost reduction (transposition deadline 1 January 2016). The Commission
referred under Art. 258 in 2017 and specified under Art. 260(3) a daily penalty calculated
from the 2017 methodology. Judgment was delivered on 8 July 2019, finding the infringement
and imposing a daily penalty until full notification (operative part — [VERIFY paragraph
numbers and exact figure]).

Procedural significance:

1. **First application of Art. 260(3).** Established that the Commission's methodology is
   a permissible reference; the Court retains discretion within the cap.
2. **Scope clarification.** Art. 260(3) covers both absent and partial notification — the
   failure is to notify the measures required to give the directive its full effect.

[VERIFY all numerical figures, paragraph numbers, and operative-part wording against
CURIA before any submission.]

### Illustrative calculation

For a hypothetical `MSx`, `n = 1.0`, non-notification of NIS2 (deadline 17 October 2024)
for 365 days as of the reference date:

```
Inputs (all [VERIFY]):
  R_daily = 3,400; R_lump = 1,140; LS_min = 200,000
  C_s = 8 (NIS2 flagship); C_d = 1.6; n = 1.0; N_days_past = 365

Daily penalty   = 3,400 × 8 × 1.6 × 1.0       =    €43,520 / day
Lump sum        = max(200,000, 1,140 × 8 × 365 × 1.0)
                = max(200,000, 3,328,800)     = €3,328,800
```

Replace these illustrative figures with the Commission's actual specified figures (from
the LFN, RO, or referral application or the Press Corner summary thereof) before quoting
in any output.

### Court's deference and adjustments

The Court may impose less than the Commission's specified amount, or no sanction at all,
or a lump sum without the periodic penalty (or vice versa). It cannot impose more —
the Art. 260(3) final-sentence cap. Published Art. 260(3) practice since _Commission v
Belgium_ shows the Court tending to (i) accept the Commission's n-factor without
adjustment, (ii) occasionally adjust the seriousness coefficient downward, and (iii)
frequently impose a lump sum rather than a daily penalty where compliance has been
achieved between referral and judgment. [VERIFY against the most recent CJEU Annual
Report.]

---

## Article 260(2) Penalty Methodology

The 2005 Communication SEC(2005) 1658 (with periodic updates) is the canonical Art.
260(2) reference. Structural difference from Art. 260(3): no upward cap on the Court's
discretion, although the Court's deference to the Commission's methodology is high in
practice.

**Lump-sum component:** `LS = max(LS_min × n, R_lump × C_s × N_days × n)`. `N_days` =
days between the original Art. 258 judgment and compliance (or the Art. 260(2) judgment,
whichever is earlier). Per _Commission v Germany_ (C-503/04, ECLI:EU:C:2007:432),
compliance between referral and judgment does not extinguish lump-sum exposure for past
non-compliance.

**Periodic penalty component:** `R_daily × C_s × C_d × n` per unit of continued
non-compliance. The Court may set the penalty per day, per six-month period (as in
_Commission v France_, C-304/02), or otherwise.

### _Commission v France_ (C-304/02) worked example

Seminal case on cumulation of lump sum and periodic penalty under Art. 228 EC (now
Art. 260(2) TFEU). France had failed to comply with the 1991 judgment in C-64/88
concerning Common Fisheries Policy minimum mesh size and undersized-fish landing rules.

The Court held (paragraph [VERIFY]) that the two sanction types are not mutually
exclusive — lump sum punishes past non-compliance (general deterrence); periodic penalty
incentivises future compliance — and imposed both: a lump sum of €20 million [VERIFY]
plus €57.7 million per six-month period of continued non-compliance [VERIFY], even though
the Commission's application had proposed only the periodic penalty. The cumulation
principle is now standard Art. 260(2) practice.

### _Commission v Greece_ (C-378/13) worked example

The case concerned Greece's failure to recover unlawful state aid as ordered in the
original Art. 258 judgment. The Court imposed a lump sum and periodic penalty,
confirming that Art. 260(2) applies across all subject matters of EU law — not only
internal-market directives — and that recovery-order compliance failures attract
Art. 260(2) treatment. [VERIFY exact figures, paragraph numbers, and periodicity.]

### _Commission v Germany_ (C-503/04) worked example

Significant for the principle that compliance achieved after the Art. 260(2) LFN but
before the Art. 260(2) judgment does not extinguish lump-sum exposure for past
non-compliance — the lump-sum's general-deterrence function justifies imposition even
when periodic-penalty accrual has stopped.

---

## Risk Scoring Model

This section documents calibration considerations behind the four axis scores defined in
Step 7.

**`R_pattern`.** Drawn from public Single Market Scoreboard data: total open
infringements, average duration, Art. 260 referrals, transposition deficit. Calibrated
from the 2023–2024 Scoreboard releases; recalibrate against the most recent release
before any submission. Where the directive is an outlier in the MS's portfolio (e.g. an
MS habitually compliant on Single Market matters faces an unusual Art. 260(3) referral on
a Digital Decade directive), do not let `R_pattern` mask the pair-specific risk —
`R_stage`, `R_directive`, and `R_conformity` carry it through.

**`R_directive`.** Calibrated from (i) Commission strategic prioritisation (Work
Programme; State of the Union; flagship initiatives), (ii) seriousness coefficients
historically proposed for the directive or family, and (iii) policy area (internal
market, fundamental rights, climate, financial stability tend toward higher coefficients).

Calibrated examples (verify against the most recent strategic communications):

- NIS2 (CELEX 32022L2555): `R_directive = 4` — flagship in 2024–2025 cybersecurity
  strategy; Commission has publicly indicated willingness to use Art. 260(3) for
  non-notification.
- CSRD (CELEX 32022L2464): `R_directive = 4` — central to the Sustainable Finance agenda.
- CSDDD (CELEX 32024L1760): not yet exposed (deadline 26 July 2026); calibrate after
  deadline.

**`R_conformity`.** Drawn from skill E. Score 2 where a small number of articles are
`partial` but the substantive core is `correct`; score 4–5 where the core is `incorrect`
or `not transposed`. This skill does not re-run the conformity check.

**Combining the axes.** The composite weights `R_stage` heaviest because the procedural
stage captures imminence of financial exposure more directly than the other axes — a
pair at `S5` imposes immediate Art. 260(1) compliance obligations regardless of
directive exotica; a pair at `S0` is not yet a financial exposure regardless of conformity
gaps.

**Sensitivity testing.** For HIGH and CRITICAL classifications, the Glass Box records a
one-line sensitivity test under each alternative weight set; if the tier changes, the
Glass Box surfaces the change.

---

## Single Market Scoreboard Inputs

The Single Market and Competitiveness Scoreboard aggregates MS performance across
multiple infringement indicators. This skill computes per-pair inputs feeding the MS-level
rollup, and (in batch modes) directive-level or MS-level summaries directly comparable to
published Scoreboard tables.

**Indicators:**

1. **Transposition deficit (%)** — directives past deadline not notified complete /
   directives in force with deadlines past. Commission target historically 1.0%; ≥1.0%
   triggers Single Market Forum scrutiny. [VERIFY current target.]
2. **Conformity deficit (%)** — directives with skill E verdicts `incorrect` (and in some
   Scoreboard methodologies `partial`) / directives notified.
3. **Average duration of open procedures (months)** — mean of (now − LFN date) across
   open cases.
4. **Long-overdue cases** — LFN > 18 months without RO; RO > 18 months without referral.
5. **Art. 258 referrals (annual).**
6. **Art. 260 referrals (annual)** — Art. 260(2) and Art. 260(3) actions.
7. **Resolution time (months)** — mean of (closure date − LFN date) across closed cases.

**Outputs.** Single-pair mode: one-row contribution to the MS's transposition and
conformity deficit (the directive contributes 1 to numerator if non-notified or
non-conforming; 1 to denominator). Batch-over-MS: full MS-level contribution.
Batch-over-directive: directive-level cross-MS scoreboard.

**Single Market Forum positioning.** Where an MS's transposition deficit exceeds 1.0%,
the Commission has historically raised the matter at the Forum; the skill flags pairs
contributing to such an excess.

---

## ESA / EFTA Court Mirror

The EFTA pillar of the EEA (Iceland, Norway, Liechtenstein) operates a mirror enforcement
system under the Surveillance and Court Agreement (SCA). Switzerland is not in scope —
it is not an EEA Contracting Party.

### Procedural mirror

| EU pillar                                                    | EFTA pillar                                                                                               | Comparable scope                                                                          |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| TFEU Art. 258 first paragraph LFN                            | SCA Art. 31 first paragraph reasoned-opinion preliminary letter                                           | Substantively identical: opportunity to submit observations                               |
| TFEU Art. 258 first paragraph RO                             | SCA Art. 31 reasoned opinion                                                                              | Substantively identical                                                                   |
| TFEU Art. 258 second paragraph CJEU referral                 | SCA Art. 32 EFTA Court action                                                                             | Substantively identical                                                                   |
| Art. 258 judgment                                            | EFTA Court judgment                                                                                       | Declaratory; obligation to comply                                                         |
| TFEU Art. 260(2) renewed proceedings                         | None — ESA and the EFTA Court do not currently apply a structurally identical second-stage penalty regime | [VERIFY current ESA practice; the position has been debated within ESA]                   |
| TFEU Art. 260(3) first-referral penalty for non-notification | None                                                                                                      | The Lisbon innovation is EU-pillar only; the SCA does not currently provide an equivalent |

### Practical implications for the EFTA pillar

1. **No financial-sanction exposure under the SCA.** The EFTA Court's judgment is
   declaratory; financial sanctions analogous to Art. 260(2)/(3) do not currently apply.
   This significantly reduces the financial-risk component of the composite score for
   pairs in the EFTA pillar — but does not eliminate political-risk exposure (a sustained
   pattern of EFTA Court adverse judgments may attract attention from the EEA Joint
   Committee under EEA Art. 109).
2. **EEA incorporation as a precondition.** The skill must consult skill G (EEA
   Incorporation Tracker) before the EFTA-pillar mirror runs. If the directive has not
   been incorporated into the relevant EEA Annex by Joint Committee Decision (EEA Art.
   102), or has been incorporated but its entry into force is suspended pending an Art.
   103 constitutional reservation, no SCA Art. 31 procedure can be opened — there is no
   EEA-binding obligation to enforce.
3. **Adaptation texts.** The Joint Committee Decision incorporating the directive may
   include adaptations under EEA Art. 102(5); the skill must reflect those adaptations
   in the obligation it is testing for compliance.

### EFTA Court timing

The EFTA Court's published case-management practice indicates that SCA Art. 32 cases
typically run from lodgement to judgment in 9–15 months — somewhat faster than the CJEU
median for analogous cases, reflecting the smaller caseload. [VERIFY against the most
recent EFTA Court Annual Report.]

---

## Mitigation Pathways

Consolidates Step 10 pathways and adds stage-specific subtleties.

**Notification cure (Art. 260(3)).** Cleanest mitigation: notify transposition. Art.
260(3) tracks notification, not substantive conformity (_Commission v Belgium_,
C-543/17). Complete timely notification cures the procedure; the Commission closes the
case; the CJEU is informed; if judgment is pending, the case may be withdrawn or the
Court may decide there is no longer cause to rule. Notification does **not** cure
substantive non-conformity — non-conforming notified measures transition the case from
the Art. 260(3) track to a pure Art. 258 substantive track.

**Remedial NIM amendment (substantive Art. 258).** Enact and notify an amendment
bringing the NIM into conformity; the Commission considers conformity afresh upon
notification.

**Settlement positioning.** Formal settlement is rare; informal pre-litigation dialogue
routinely produces case closures — operationally a settlement: the MS commits in writing
to remedial steps; the Commission closes the procedure.

**Marleasing interpretive cure.** _Marleasing_ (Case C-106/89, ECLI:EU:C:1990:395,
paragraph 8) requires national courts to interpret national law, so far as possible, in
conformity with the directive. Where the NIM is ambiguous rather than absent or wrong,
_Marleasing_ may operationally resolve the substantive concern even before a formal
amendment — not a complete substitute for transposition, but capable of reducing
`R_conformity` from 4 to 2–3 in interpretive-deficit pairs. Does **not** affect the
Art. 260(3) track (which concerns notification, not substantive conformity).

**CJEU defence on the merits.** At `S4`, defences observed in the case-law include:
force majeure / impossibility (rarely successful — the bar is exceptional, unforeseeable
circumstances making compliance objectively impossible); procedural irregularity
(challenges to LFN specificity, RO reasoning, or n-factor application); and
proportionality of the proposed Art. 260(3) sanction (the Court has discretion within
the cap).

**Compliance before judgment.** In Art. 260(3) cases especially, the Court has on
several occasions imposed a lump sum but not the daily penalty where compliance was
achieved between referral and judgment.

**Politically negotiated extended compliance.** For Art. 260(2) cases on particularly
difficult substantive obligations (e.g. state-aid recovery in _Commission v Greece_
C-378/13), MS may negotiate an extended trajectory through PermRep channels — not formal
under the Treaties but observable in published Commission monitoring practice.

---

## Anti-Patterns

What NOT to do when running this skill:

1. **Treating absence of a Press Corner reference as evidence of no procedure.** The
   Commission's monthly infringements package summarises decisions taken at the College
   of Commissioners; cases in pre-Pilot, Pilot, or pre-LFN dialogue do not appear. Use
   the absence of a Press Corner reference as one signal among several, not as
   conclusive evidence.

2. **Conflating Art. 260(2) and Art. 260(3).** The two are structurally distinct: Art.
   260(2) follows an Art. 258 judgment; Art. 260(3) is a first-referral penalty in the
   Art. 258 application itself. Confusing the two leads to wildly wrong penalty
   estimates and missed mitigation pathways.

3. **Treating Art. 260(3) as substantive-non-conformity sanction.** _Commission v
   Belgium_ (C-543/17) limits Art. 260(3) to non-notification of transposition. The
   substantive Art. 258 procedure handles non-conformity; the Art. 260(3) track does
   not.

4. **Inventing case numbers, ECLIs, or penalty figures.** All four are publicly
   verifiable on EUR-Lex, CURIA, and the Commission Press Corner. Where verification
   is not possible, mark the figure `[VERIFY]` and present a range rather than a
   precise number.

5. **Using a stale n-factor.** The Commission updates the n-factor table periodically
   (2010, 2018, 2019, 2020, 2022, 2023). The Court applies the n-factor in force at the
   date of the judgment. Using the n-factor in force at the date of the LFN gives the
   wrong number.

6. **Assuming the Commission's specified amount equals the Court's imposed amount.**
   For Art. 260(3), the Court may impose less; for Art. 260(2), the Court may impose
   more or less. Present the Commission's specified amount as the upper bound (Art.
   260(3)) or the proposed amount (Art. 260(2)), and the Court's imposed amount (where
   judgment has been delivered) separately.

7. **Treating the EFTA pillar as a financial-exposure mirror.** ESA and the EFTA Court
   do not currently apply Art. 260-equivalent penalties; the EFTA-pillar exposure is
   political and declaratory. Treating the EFTA-pillar as financially equivalent to the
   EU-pillar overstates risk.

8. **Skipping skill C / skill E inputs.** The skill is designed to consume (not
   re-derive) the per-MS implementation matrix from skill C and the per-article
   conformity verdicts from skill E. Re-deriving these inputs in this skill produces
   noise; defer to the canonical skill output and flag `[VERIFY]` where unavailable.

9. **Aggregating pairs without weight transparency.** When emitting MS-level or
   directive-level rollups, always show the constituent (MS, directive) pair scores;
   never present an aggregated score without the per-pair detail underneath. Hidden
   aggregation breaks the audit trail.

10. **Ignoring the EEA Joint Committee Decision precondition.** EFTA-pillar mirror
    analysis is invalid if the directive has not been incorporated into the relevant
    EEA Annex (or has incorporation but suspended entry-into-force under EEA Art. 103).
    Always consult skill G first.

11. **Treating an MS Permanent Representation press release as authoritative on the
    Commission's procedural state.** PermRep statements reflect the MS position; the
    Commission's procedural state is established by the Commission's own publications
    (Press Corner, INFR database, College decisions). Cite both, distinguish both, and
    favour the Commission source for procedural-state assertions.

12. **Mixing authentic-language versions without reconciliation.** The LFN, RO, and
    judgment are issued in the language of the proceedings (typically the MS official
    language); the Commission's strategic communications are in English / French.
    Reconciling figures or wording across language versions without explicit handling
    risks misrepresenting either.

13. **Presenting projected stages as observed.** Where the analysis projects an
    expected `S3` six months from the LFN date, the projection must be flagged as
    such. Presenting projected events as observed events misrepresents the procedural
    state.

14. **Forgetting that Art. 260(3) does not apply to non-legislative directives.** The
    provision applies only to directives adopted under a legislative procedure (Art.
    294 ordinary legislative procedure or Art. 289(2) special legislative procedure).
    Implementing directives under Art. 290 / 291 are not eligible. Verify the
    legislative basis before invoking Art. 260(3).

15. **Missing parallel procedures.** A pair may have both a non-notification Art.
    260(3) track and a substantive Art. 258 / Art. 260(2) track open simultaneously;
    closing one does not close the other. Always check for parallel INFR identifiers.

16. **Assuming compliance after notification.** Notification of transposition cures
    Art. 260(3) but the Commission may then open a substantive Art. 258 procedure on
    the notified measures. The pair may transition from `T3` to `S2` rather than to
    `S0`.

17. **Risk-scoring the MS rather than the pair.** A risk score per MS that aggregates
    across all directives is meaningful for trade-federation persona use but is not
    actionable for in-house or government persona use, both of which need pair-level
    scores. Do not collapse to MS-level scoring without explicit persona instruction.

18. **Treating EU Pilot as a procedural stage equivalent to LFN.** EU Pilot is
    informal; it carries no statutory consequences. A pair in EU Pilot does not have
    LFN exposure and the risk score should reflect this. EU Pilot duration is not
    bounded; many pairs sit in Pilot for years before LFN.

---

## Writing Standards

Follow these standards when producing infringement-procedure-tracker outputs.

### Citation density

Every legal claim must carry a citation. The minimum unit:

| Claim type               | Citation required                                                                               |
| ------------------------ | ----------------------------------------------------------------------------------------------- |
| TFEU Article reference   | "Art. 258 TFEU" first use; ELI on first use only                                                |
| Directive reference      | Short title + formal title + CELEX + OJ reference on first use; CELEX or short title thereafter |
| Case-law reference       | Short name + ECLI on first use; ECLI thereafter                                                 |
| Commission communication | Year + identifying CELEX or COM number; URL on first use                                        |
| Single Market Scoreboard | Method-page URL on first use                                                                    |
| Press Corner             | URL plus retrieval timestamp                                                                    |
| CURIA                    | Case-page URL plus retrieval timestamp                                                          |

### Deontic operators

The skill describes the obligations of Member States and the discretion of the
Commission and the Court. Use deontic operators consistently:

- `must` — Treaty-level obligation (Art. 260(1) compliance; Art. 4(3) TEU sincere
  cooperation)
- `shall` — directive-level transposition obligation (Art. 288 TFEU)
- `may` — Commission or Court discretion
- `is required to` — derivative obligation flowing from a directive

Do not use `should` for Treaty obligations — `should` implies discretion that does not
exist for Member-State Treaty obligations.

### Language-version reconciliation

Every quotation from a directive, communication, or judgment must specify the language
version cited. Where the analysis depends on a contested provision, the skill must
reconcile across at least three language versions before relying on the wording — per
_CILFIT_ (Case C-283/81, ECLI:EU:C:1982:335), _Codan_ (Case C-236/97, ECLI:EU:C:1998:208),
and _EMU Tabac_ (Case C-296/95, ECLI:EU:C:1998:152). Use IATE
(`https://iate.europa.eu/`) for terminological reconciliation.

### EEA-relevance flag

Every directive cited must be checked for the "EEA relevance" flag in the OJ title. Where
the directive bears the flag, the EFTA-pillar mirror analysis is in scope (subject to
JCD incorporation under skill G). Where the flag is absent, the EFTA-pillar mirror is
not in scope and the skill emits the EU-pillar timeline only.

### CELEX, ELI, ECLI conventions

- CELEX is the Publications Office identifier (e.g. `32016R0679` for GDPR;
  `32022L2555` for NIS2). Use CELEX in JSON outputs and inline parenthetical citations.
- ELI is the European Legislation Identifier — an HTTP URI scheme for legislation.
  Use ELI on first citation of a Treaty article (e.g.
  `https://eur-lex.europa.eu/eli/treaty/tfeu_2008/art_258/oj/eng`).
- ECLI is the European Case Law Identifier (e.g. `ECLI:EU:C:2019:573`). Use ECLI for
  every case-law reference, on every use (not just first).

### `[VERIFY]` markers

Inline `[VERIFY]` markers must follow any unconfirmed claim — including penalty figures,
n-factor table values, paragraph numbers, and procedural dates not directly verified
against the Commission Press Corner or CURIA. Do not relegate `[VERIFY]` markers to
footnotes.

### No false precision

Where the skill projects a future event (e.g. expected `S3` window from LFN date),
present a range with explicit confidence: "Expected RO between 2025-09 and 2026-03
(LIKELY)". Do not present a precise projected date as if it were a known date.

### Persona-language adaptation

- Government persona: formal, defensive, MS-perspective; cite NIS2 deadline and
  MS-side coordination
- Legal firm persona: client-advisory; cite cross-MS comparison; expected-value
  framing of penalty estimates
- Company persona: operational; translate timeline events into business impact
- Trade federation persona: sectoral; cross-MS pattern view; policy-position framing

### One pair per row

In tabular outputs, each row is exactly one (MS, directive) pair. A pair with parallel
procedures (non-notification + substantive) appears as two rows distinguished by the
`procedure_type` column.

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

When legalcode-mcp is available, use it to:

1. Resolve CELEX → ELI → consolidated text via the EUR-Lex Cellar SPARQL endpoint
   (`https://publications.europa.eu/webapi/rdf/sparql`)
2. Verify case ECLIs and judgment dates against CURIA
3. Retrieve the most recent Press Corner monthly package and extract the relevant
   (MS, directive) events
4. Confirm the most recent n-factor table and Commission Communication updates
5. Pull Single Market Scoreboard MS-level statistics

Save research artefacts to `/tmp/legalcode-infringement-research-[YYYY-MM-DD].md` and
record the path in the Glass Box.

### Without legalcode-mcp

Proceed with built-in references plus user-supplied artefacts, marking every
non-verified figure `[VERIFY]`. Apply downward confidence adjustments:

- LFN / RO / referral dates: LIKELY → POSSIBLE
- Penalty figures: LIKELY → VERIFY
- n-factor values: LIKELY → VERIFY

### National parliament APIs

For government-persona deep-dives, use the relevant national parliament API to retrieve
the NIM enactment record:

- Riksdagen (SE): `https://data.riksdagen.se`
- Storting (NO, EFTA pillar): `https://data.stortinget.no`
- Folketinget (DK): `https://oda.ft.dk`
- Althingi (IS, EFTA pillar): `https://www.althingi.is`
- Bundestag (DE): `https://dip.bundestag.de`
- Assemblée nationale (FR): `https://data.assemblee-nationale.fr`

### Related skills integration

| Trigger                                              | Invoke                                   |
| ---------------------------------------------------- | ---------------------------------------- |
| Need obligation register for the directive           | `legalcode-eu-directive-analyzer`        |
| Need per-MS implementation matrix                    | `legalcode-eu-transposition-tracker`     |
| Need correlation table for CJEU defence preparation  | `legalcode-eu-correlation-table-builder` |
| Need per-article conformity verdicts                 | `legalcode-eu-conformity-assessment`     |
| Need gold-plating pattern                            | `legalcode-eu-gold-plating-detector`     |
| EFTA-pillar pair, EEA incorporation status uncertain | `legalcode-eea-incorporation-tracker`    |

---

## Citation Quality Gates

Run these silently before delivering any output. If any gate fails, revise before delivering.

| Gate                             | Rule                                                                                                      | Fail Action                                                       |
| -------------------------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **1. CELEX gate**                | Every directive cited has CELEX + OJ reference                                                            | Add or mark `[CELEX UNVERIFIED]`                                  |
| **2. ECLI gate**                 | Every case has ECLI on every reference                                                                    | Add ECLI or mark `[ECLI UNVERIFIED]`                              |
| **3. Procedural-event gate**     | Every LFN, RO, referral, judgment date carries Press Corner or CURIA URL                                  | Add URL or mark `[VERIFY procedural date]`                        |
| **4. Penalty-figure gate**       | Every euro figure in Art. 260(2)/(3) calculations carries a Commission-Communication or judgment citation | Add citation or mark `[VERIFY penalty figure]`                    |
| **5. n-factor gate**             | n-factor values cite the most recent Communication updating the table                                     | Add citation or mark `[VERIFY n-factor]`                          |
| **6. Multilingualism gate**      | Quotations specify the language version                                                                   | Add language label or remove the quotation                        |
| **7. EEA-relevance gate**        | EFTA-pillar analysis verified against skill G's JCD status                                                | Either confirm JCD incorporation or remove the EFTA-pillar branch |
| **8. Stage-classification gate** | Stage assigned matches the most advanced verifiable event                                                 | Lower stage or add `[VERIFY stage]`                               |

---

## Confidence Scoring

Every event, stage classification, penalty estimate, and risk-score input carries a
confidence level.

| Level        | Score range | Definition                                                                                                   | Action                                      |
| ------------ | ----------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------- |
| **VERIFIED** | 0.90–1.00   | Independently confirmed against Commission Press Corner / CURIA / EUR-Lex / CJEU Annual Report               | State with confidence                       |
| **LIKELY**   | 0.70–0.89   | Reliable secondary source (national gazette; ESA register) but not independently verified against EU primary | "Based on [source]; recommend verification" |
| **POSSIBLE** | 0.50–0.69   | Good-faith inference from structurally consistent evidence                                                   | State with explicit reasoning               |
| **VERIFY**   | 0.30–0.49   | Assumption based on procedural-stage defaults                                                                | Flag prominently                            |
| **ASSUMED**  | < 0.30      | Placeholder based on MS profile defaults                                                                     | Internal only; not for delivery             |

**Default confidences:**

- Date sourced from Press Corner package: VERIFIED (0.92)
- Date sourced from CURIA case page: VERIFIED (0.95)
- Date sourced from MS national gazette: LIKELY (0.80)
- Penalty figure from a closed-case CJEU judgment: VERIFIED (0.95)
- Penalty figure projected from the 2023 Communication formula: LIKELY (0.75)
- n-factor used: LIKELY (0.80) until verified against current Communication

---

## Output Format Template

Every run emits five artefacts: Markdown timeline, JSON schema, AKN4EU `<doc>`, LegalRuleML
prescriptive blocks, and Glass Box audit trail.

### 1. Markdown Infringement Timeline

```markdown
# Infringement procedure timeline — [Member State] × [Directive short title]

**Member State**: [Name] ([ISO code])
**Directive**: [short title] ([formal title], CELEX [code], OJ [reference])
**Transposition deadline**: [YYYY-MM-DD]
**EEA relevance**: [yes / no]
**Reference date**: [YYYY-MM-DD]
**Pillar**: [EU (TFEU 258/260) | EFTA (SCA 31/32)]
**Procedure type(s)**: [non-notification (Art. 260(3)) | substantive (Art. 258) | both]
**INFR identifier(s)**: [INFR(YYYY)NNNN, ...]
**CJEU case number(s)**: [C-NNN/YY, ...]
**Current stage**: [S0..S7 | T3 | F0..F4]
**Confidence**: [VERIFIED | LIKELY | POSSIBLE | VERIFY | ASSUMED] ([0.00–1.00])

## Stages

### S2 — Letter of Formal Notice

- **Date**: [YYYY-MM-DD] (source: Commission Press Corner [URL])
- **Response window**: 2 months (standard practice; Art. 258 first paragraph)
- **MS response**: [observed / not observed / [VERIFY]]
- **Confidence**: [level]

### S3 — Reasoned Opinion

- **Date**: [YYYY-MM-DD] (source: ...)
- ...

### S4 — CJEU referral

- **Lodgement date**: [YYYY-MM-DD] (source: CURIA case page [URL])
- **Case number**: C-NNN/YY
- **AG opinion**: [date / not delivered / not anticipated]
- **Hearing date**: [YYYY-MM-DD or not scheduled]
- **Judgment date**: [YYYY-MM-DD or pending]

### T3 — Art. 260(3) parallel track (where applicable)

- **Commission-specified daily penalty**: €[amount] / day
- **Commission-specified lump sum**: €[amount]
- **Court-imposed daily penalty (if judgment delivered)**: €[amount] / day
- **Court-imposed lump sum (if judgment delivered)**: €[amount]

## Penalty calculation (current best estimate)

Inputs (all [VERIFY] against current Commission Communication unless otherwise marked):

- R_daily = [value]
- R_lump = [value]
- LS_min = [value]
- C_s = [value]
- C_d = [value]
- n = [value]
- N_days_past = [value]

Computed:

- Daily penalty = €[amount] / day
- Lump sum = €[amount]

## Risk score

| Axis            | Score       | Rationale                                            |
| --------------- | ----------- | ---------------------------------------------------- |
| R_stage         | [1–5]       | [stage code]                                         |
| R_pattern       | [1–5]       | [MS pattern from Single Market Scoreboard, [VERIFY]] |
| R_directive     | [1–5]       | [directive importance basis]                         |
| R_conformity    | [1–5]       | [skill E verdict mix or ASSUMED]                     |
| **Composite R** | **[value]** | **[CRITICAL / HIGH / MEDIUM / LOW]**                 |

## Mitigation pathways (ordered by cost)

1. [Pathway 1] — [description]
2. [Pathway 2] — [description]
3. [Pathway 3] — [description]

## Sensitivity (HIGH / CRITICAL only)

Under stage-dominant weights: [tier]
Under substance-dominant weights: [tier]
Under pattern-dominant weights: [tier]

## Sources and provenance

- Commission Press Corner: [URLs and retrieval timestamps]
- CURIA: [URLs and retrieval timestamps]
- Single Market Scoreboard: [URL]
- Skill C output: [path or "not available"]
- Skill E output: [path or "not available"]
- Skill G output (EFTA-pillar only): [path or "not available"]

## Glass Box audit trail

[YAML — see Section: Glass Box below]
```

### 2. JSON infringement schema

```json
{
  "$schema": "https://legalcode/eu-infringement-procedure/1.0",
  "skill": "legalcode-eu-infringement-procedure-tracker",
  "version": "1.0",
  "reference_date": "YYYY-MM-DD",
  "pair": {
    "member_state": {
      "iso_code": "DE",
      "name": "Germany",
      "pillar": "EU"
    },
    "directive": {
      "celex": "32022L2555",
      "short_title": "NIS2",
      "formal_title": "Directive (EU) 2022/2555 of the European Parliament and of the Council of 14 December 2022 on measures for a high common level of cybersecurity across the Union",
      "oj_reference": "OJ L 333, 27.12.2022, p. 80",
      "transposition_deadline": "2024-10-17",
      "eea_relevant": true,
      "legislative_directive": true
    }
  },
  "procedures": [
    {
      "procedure_type": "non_notification",
      "infr_identifier": "INFR(YYYY)NNNN",
      "cjeu_case_number": "C-NNN/YY",
      "stage_current": "S4",
      "stage_history": [
        {
          "stage": "S2",
          "date": "YYYY-MM-DD",
          "source_url": "https://ec.europa.eu/commission/presscorner/...",
          "retrieval_timestamp": "YYYY-MM-DDTHH:MM:SSZ",
          "confidence": "VERIFIED"
        },
        {
          "stage": "S3",
          "date": "YYYY-MM-DD",
          "source_url": "https://ec.europa.eu/commission/presscorner/...",
          "retrieval_timestamp": "YYYY-MM-DDTHH:MM:SSZ",
          "confidence": "VERIFIED"
        },
        {
          "stage": "S4",
          "date": "YYYY-MM-DD",
          "source_url": "https://curia.europa.eu/...",
          "retrieval_timestamp": "YYYY-MM-DDTHH:MM:SSZ",
          "confidence": "VERIFIED"
        }
      ],
      "art_260_3": {
        "commission_specified_daily_penalty_eur": 0,
        "commission_specified_lump_sum_eur": 0,
        "court_imposed_daily_penalty_eur": null,
        "court_imposed_lump_sum_eur": null
      }
    }
  ],
  "penalty_calculation": {
    "communication_version": "2023",
    "communication_url": "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:52023XC0104(01)",
    "inputs": {
      "r_daily_eur": 0,
      "r_lump_eur": 0,
      "ls_min_eur": 0,
      "c_s": 0,
      "c_d": 0.0,
      "n": 0.0,
      "n_days_past": 0
    },
    "outputs": {
      "daily_penalty_eur": 0,
      "lump_sum_eur": 0
    },
    "verification": "[VERIFY against the 2023 Communication and the relevant Commission Press Corner notice]"
  },
  "risk_score": {
    "weights": {
      "stage": 0.4,
      "pattern": 0.2,
      "directive": 0.2,
      "conformity": 0.2
    },
    "axes": {
      "stage": 0,
      "pattern": 0,
      "directive": 0,
      "conformity": 0
    },
    "composite": 0.0,
    "tier": "MEDIUM",
    "sensitivity": {
      "stage_dominant": "TIER",
      "substance_dominant": "TIER",
      "pattern_dominant": "TIER"
    }
  },
  "scoreboard_inputs": {
    "transposition_deficit_contribution": 1,
    "conformity_deficit_contribution": 0,
    "duration_months": 0,
    "long_overdue": false
  },
  "mitigation_pathways": [
    {
      "pathway": "notification",
      "cures": ["Art. 260(3)"],
      "estimated_cost": "low",
      "expected_outcome": "case closure"
    },
    {
      "pathway": "remedial_nim_amendment",
      "cures": ["Art. 258 substantive"],
      "estimated_cost": "medium",
      "expected_outcome": "case closure subject to Commission re-evaluation"
    }
  ],
  "glass_box": {
    "see": "glass_box_yaml_block"
  }
}
```

### 3. AKN4EU stub — `proceedingEvent`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<akomaNtoso xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <doc name="proceedingEvent">
    <meta>
      <identification source="#legalcode-eu-infringement-procedure-tracker">
        <FRBRWork>
          <FRBRthis value="/akn/eu/proceeding/2024/INFR-YYYY-NNNN/!main"/>
          <FRBRuri value="/akn/eu/proceeding/2024/INFR-YYYY-NNNN"/>
          <FRBRdate date="YYYY-MM-DD" name="opening"/>
          <FRBRauthor href="#european-commission"/>
          <FRBRcountry value="eu"/>
          <FRBRsubtype value="infringement-art258"/>
        </FRBRWork>
        <FRBRExpression>
          <FRBRthis value="/akn/eu/proceeding/2024/INFR-YYYY-NNNN/eng@/!main"/>
          <FRBRuri value="/akn/eu/proceeding/2024/INFR-YYYY-NNNN/eng@"/>
          <FRBRdate date="YYYY-MM-DD" name="reference"/>
          <FRBRauthor href="#european-commission"/>
          <FRBRlanguage language="eng"/>
        </FRBRExpression>
        <FRBRManifestation>
          <FRBRthis value="/akn/eu/proceeding/2024/INFR-YYYY-NNNN/eng@.xml"/>
          <FRBRuri value="/akn/eu/proceeding/2024/INFR-YYYY-NNNN/eng@.xml"/>
          <FRBRdate date="YYYY-MM-DD" name="manifestation"/>
          <FRBRauthor href="#legalcode-eu-infringement-procedure-tracker"/>
        </FRBRManifestation>
      </identification>
      <references source="#legalcode-eu-infringement-procedure-tracker">
        <TLCOrganization eId="european-commission"
                         href="/akn/ontology/organization/eu/EuropeanCommission"
                         showAs="European Commission"/>
        <TLCOrganization eId="cjeu"
                         href="/akn/ontology/organization/eu/CourtOfJustice"
                         showAs="Court of Justice of the European Union"/>
        <TLCRole eId="member-state"
                 href="/akn/ontology/role/eu/MemberState"
                 showAs="Member State"/>
        <TLCReference eId="directive"
                      href="/akn/eu/act/directive/2022/2555"
                      showAs="Directive (EU) 2022/2555 (NIS2)"/>
      </references>
    </meta>
    <mainBody>
      <part eId="part_proceeding">
        <heading>Infringement procedure INFR(YYYY)NNNN</heading>
        <chapter eId="chp_lfn">
          <num>1</num>
          <heading>Letter of Formal Notice (Art. 258 TFEU)</heading>
          <paragraph eId="para_lfn_date">
            <content>
              <p>On <date date="YYYY-MM-DD">[date]</date>, the
              <ref href="#european-commission">Commission</ref> issued a letter of formal
              notice to the <ref href="#member-state">Member State</ref> concerned
              regarding non-notification of measures transposing
              <ref href="#directive">Directive (EU) 2022/2555 (NIS2)</ref>.</p>
            </content>
          </paragraph>
        </chapter>
        <chapter eId="chp_ro">
          <num>2</num>
          <heading>Reasoned Opinion (Art. 258 TFEU)</heading>
          <paragraph eId="para_ro_date">
            <content>
              <p>On <date date="YYYY-MM-DD">[date]</date>, the Commission delivered a
              reasoned opinion. The Member State was given two months to comply.</p>
            </content>
          </paragraph>
        </chapter>
        <chapter eId="chp_referral">
          <num>3</num>
          <heading>CJEU referral (Art. 258 TFEU; Art. 260(3) TFEU specification)</heading>
          <paragraph eId="para_referral_date">
            <content>
              <p>On <date date="YYYY-MM-DD">[date]</date>, the Commission referred the
              case to the <ref href="#cjeu">Court of Justice</ref> as Case C-NNN/YY,
              specifying under Art. 260(3) TFEU a daily penalty of EUR [amount] and a
              lump sum of EUR [amount].</p>
            </content>
          </paragraph>
        </chapter>
      </part>
    </mainBody>
  </doc>
</akomaNtoso>
```

### 4. LegalRuleML stub — `Prescriptive` rules

```xml
<?xml version="1.0" encoding="UTF-8"?>
<lrml:LegalRuleML xmlns:lrml="http://docs.oasis-open.org/legalruleml/ns/v1.0/"
                  xmlns:ruleml="http://ruleml.org/spec">
  <lrml:Context key="ctx-art2603">
    <lrml:appliesSource keyref="#src-tfeu-260-3"/>
  </lrml:Context>

  <lrml:Source key="src-tfeu-260-3">
    <lrml:hasSource>
      <ruleml:Atom>
        <ruleml:Rel>TFEU</ruleml:Rel>
        <ruleml:Ind>Article 260(3)</ruleml:Ind>
      </ruleml:Atom>
    </lrml:hasSource>
    <lrml:hasReference>https://eur-lex.europa.eu/eli/treaty/tfeu_2008/art_260/oj/eng</lrml:hasReference>
  </lrml:Source>

  <lrml:Source key="src-comm-2023">
    <lrml:hasSource>
      <ruleml:Atom>
        <ruleml:Rel>CommissionCommunication</ruleml:Rel>
        <ruleml:Ind>2023 Communication on Art. 260(3) TFEU</ruleml:Ind>
      </ruleml:Atom>
    </lrml:hasSource>
    <lrml:hasReference>https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:52023XC0104(01)</lrml:hasReference>
  </lrml:Source>

  <lrml:Prescriptive key="rule-non-notification-trigger">
    <lrml:hasStrength><lrml:DefeasibleStrength/></lrml:hasStrength>
    <lrml:hasContext keyref="#ctx-art2603"/>
    <lrml:hasSource keyref="#src-tfeu-260-3"/>
    <ruleml:Implies>
      <ruleml:if>
        <ruleml:And>
          <ruleml:Atom>
            <ruleml:Rel>isLegislativeDirective</ruleml:Rel>
            <ruleml:Var>Directive</ruleml:Var>
          </ruleml:Atom>
          <ruleml:Atom>
            <ruleml:Rel>transpositionDeadlinePassed</ruleml:Rel>
            <ruleml:Var>Directive</ruleml:Var>
            <ruleml:Var>MemberState</ruleml:Var>
          </ruleml:Atom>
          <ruleml:Atom>
            <ruleml:Rel>noCompleteNotification</ruleml:Rel>
            <ruleml:Var>Directive</ruleml:Var>
            <ruleml:Var>MemberState</ruleml:Var>
          </ruleml:Atom>
        </ruleml:And>
      </ruleml:if>
      <ruleml:then>
        <lrml:Obligation>
          <ruleml:Atom>
            <ruleml:Rel>liableUnderArt2603</ruleml:Rel>
            <ruleml:Var>MemberState</ruleml:Var>
            <ruleml:Var>Directive</ruleml:Var>
          </ruleml:Atom>
        </lrml:Obligation>
      </ruleml:then>
    </ruleml:Implies>
  </lrml:Prescriptive>

  <lrml:Prescriptive key="rule-mitigation-notification">
    <lrml:hasStrength><lrml:DefeasibleStrength/></lrml:hasStrength>
    <lrml:hasContext keyref="#ctx-art2603"/>
    <lrml:hasSource keyref="#src-comm-2023"/>
    <ruleml:Implies>
      <ruleml:if>
        <ruleml:And>
          <ruleml:Atom>
            <ruleml:Rel>liableUnderArt2603</ruleml:Rel>
            <ruleml:Var>MemberState</ruleml:Var>
            <ruleml:Var>Directive</ruleml:Var>
          </ruleml:Atom>
          <ruleml:Atom>
            <ruleml:Rel>completeNotification</ruleml:Rel>
            <ruleml:Var>Directive</ruleml:Var>
            <ruleml:Var>MemberState</ruleml:Var>
          </ruleml:Atom>
        </ruleml:And>
      </ruleml:if>
      <ruleml:then>
        <lrml:Permission>
          <ruleml:Atom>
            <ruleml:Rel>caseClosed</ruleml:Rel>
            <ruleml:Var>MemberState</ruleml:Var>
            <ruleml:Var>Directive</ruleml:Var>
          </ruleml:Atom>
        </lrml:Permission>
      </ruleml:then>
    </ruleml:Implies>
  </lrml:Prescriptive>

  <lrml:Prescriptive key="rule-art2602-cumulation">
    <lrml:hasStrength><lrml:DefeasibleStrength/></lrml:hasStrength>
    <lrml:hasSource keyref="#src-tfeu-260-3"/>
    <ruleml:Implies>
      <ruleml:if>
        <ruleml:And>
          <ruleml:Atom>
            <ruleml:Rel>art258JudgmentDelivered</ruleml:Rel>
            <ruleml:Var>MemberState</ruleml:Var>
            <ruleml:Var>Case</ruleml:Var>
          </ruleml:Atom>
          <ruleml:Atom>
            <ruleml:Rel>nonComplianceContinues</ruleml:Rel>
            <ruleml:Var>MemberState</ruleml:Var>
            <ruleml:Var>Case</ruleml:Var>
          </ruleml:Atom>
        </ruleml:And>
      </ruleml:if>
      <ruleml:then>
        <lrml:Obligation>
          <ruleml:Atom>
            <ruleml:Rel>liableLumpSumAndPeriodic</ruleml:Rel>
            <ruleml:Var>MemberState</ruleml:Var>
          </ruleml:Atom>
        </lrml:Obligation>
      </ruleml:then>
    </ruleml:Implies>
  </lrml:Prescriptive>
</lrml:LegalRuleML>
```

### 5. Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-eu-infringement-procedure-tracker"
  assessment_date: "[YYYY-MM-DD]"
  reference_date: "[YYYY-MM-DD]"
  assessed_by: "[Role — AI-assisted; must be validated by qualified EU and Member State counsel]"
  pair:
    member_state_iso: "[DE]"
    member_state_pillar: "[EU | EFTA]"
    directive_celex: "[32022L2555]"
    directive_short_title: "[NIS2]"
    transposition_deadline: "[YYYY-MM-DD]"
    eea_relevant: [true | false]
    legislative_directive: [true | false]
  inputs:
    skill_c_implementation_matrix: "[path | not available]"
    skill_e_conformity_verdicts: "[path | not available]"
    skill_g_eea_status: "[path | not available; not applicable for EU-pillar pair]"
    legalcode_mcp: "[Connected | Not connected]"
    research_artefact_path: "[/tmp/legalcode-infringement-research-YYYY-MM-DD.md | not created]"
  procedures_observed:
    - procedure_type: "[non_notification | substantive]"
      infr_identifier: "[INFR(YYYY)NNNN | not assigned]"
      cjeu_case_number: "[C-NNN/YY | not referred]"
      stage_history:
        - stage: "[S2]"
          date: "[YYYY-MM-DD]"
          source_url: "[URL]"
          retrieval_timestamp: "[ISO 8601]"
          confidence_level: "[VERIFIED | LIKELY | POSSIBLE | VERIFY | ASSUMED]"
          confidence_score: "[0.00–1.00]"
        - stage: "[S3]"
          date: "[YYYY-MM-DD]"
          source_url: "[URL]"
          retrieval_timestamp: "[ISO 8601]"
          confidence_level: "[level]"
          confidence_score: "[score]"
      stage_current: "[stage code]"
      stage_current_confidence: "[level]"
      art_260_3_specification:
        commission_daily_penalty_eur: "[value | not applicable]"
        commission_lump_sum_eur: "[value | not applicable]"
        court_daily_penalty_eur: "[value | judgment pending | not applicable]"
        court_lump_sum_eur: "[value | judgment pending | not applicable]"
        confidence: "[level]"
  penalty_calculation:
    communication_version: "[2023 | 2005-with-2022-update | other]"
    communication_url: "[URL]"
    inputs:
      r_daily_eur: "[value]"
      r_daily_source: "[Communication paragraph]"
      r_lump_eur: "[value]"
      r_lump_source: "[Communication paragraph]"
      ls_min_eur: "[value]"
      c_s: "[value]"
      c_s_rationale: "[explanation citing directive importance]"
      c_d: "[value]"
      c_d_rationale: "[explanation citing days past deadline]"
      n: "[value]"
      n_source: "[Communication / table]"
      n_days_past: "[value]"
    outputs:
      daily_penalty_eur: "[value]"
      lump_sum_eur: "[value]"
    confidence_level: "[level]"
    verify_markers: "[list of [VERIFY] items]"
  risk_score:
    weights:
      stage: 0.4
      pattern: 0.2
      directive: 0.2
      conformity: 0.2
    axes:
      r_stage:
        value: "[1–5]"
        rationale: "[stage classification rationale]"
      r_pattern:
        value: "[1–5]"
        rationale: "[Single Market Scoreboard data summary, with [VERIFY] markers]"
      r_directive:
        value: "[1–5]"
        rationale: "[directive importance rationale]"
      r_conformity:
        value: "[1–5]"
        rationale: "[skill E verdict mix, or ASSUMED]"
    composite: "[0.0–5.0]"
    tier: "[CRITICAL | HIGH | MEDIUM | LOW]"
    sensitivity:
      stage_dominant_tier: "[tier]"
      substance_dominant_tier: "[tier]"
      pattern_dominant_tier: "[tier]"
  three_pass_review:
    pass_1_procedural_chain_integrity:
      summary: "[did the classification follow from the events?]"
      single_weakest_evidence: "[event most critical to classification]"
      sensitivity_to_that_evidence: "[change in classification under opposite assumption]"
    pass_2_mitigation_in_flight:
      observed_mitigation: "[notification observed | NIM amendment observed | none]"
      effect_on_score: "[change applied | none]"
    pass_3_strategic_commission_posture:
      observation: "[Commission strategic posture toward the directive]"
      effect_on_score: "[change applied | none]"
  scoreboard_inputs:
    transposition_deficit_contribution: "[0 | 1]"
    conformity_deficit_contribution: "[0 | 1]"
    duration_months: "[value]"
    long_overdue: "[true | false]"
  mitigation_pathways:
    - pathway: "[notification | nim_amendment | settlement | marleasing | force_majeure | extended_compliance]"
      cures: "[list of stages cured]"
      estimated_cost: "[low | medium | high]"
      expected_outcome: "[narrative]"
  assumptions:
    - "[assumption 1 — what was assumed and why]"
    - "[assumption 2]"
  limitations:
    - "[scope limitation 1]"
    - "[what was not assessed]"
  reviewer_note:
    "AI-assisted — every CRITICAL or HIGH classification, every penalty
    figure, and every Art. 260(3) eligibility determination requires validation by
    qualified EU and Member State counsel before submission to the Commission, the
    CJEU, the EFTA Court, or any board / governance body."
```

---

## Worked Example — NIS2 (CELEX 32022L2555) Non-Notification

**Directive context.** NIS2 (Directive (EU) 2022/2555 on measures for a high common
level of cybersecurity across the Union, repealing Directive (EU) 2016/1148; CELEX
32022L2555; OJ L 333, 27.12.2022, p. 80) is a legislative directive bearing the "EEA
relevance" flag, with transposition deadline 17 October 2024 (Art. 41(1)).

**Procedural state.** As of [VERIFY against the Commission Press Corner monthly
infringements package and CURIA at the time of any submission], the Commission opened
non-notification procedures against multiple MS that had not notified complete
transposition by the deadline. Retrieve Press Corner references before quoting
MS-specific procedural states; the structural pattern below is calibrated from
published practice.

**Hypothetical pair `MSx` × NIS2 (illustrative).**

```
Member State: MSx (n-factor 1.0; recent transposition pattern: occasional LFN, no
              Art. 260 history)
Directive:    NIS2 (CELEX 32022L2555; deadline 2024-10-17; EEA relevant; legislative)
Reference:    2025-10-17 (one year past deadline)

Stage history (illustrative; [VERIFY all dates against Commission Press Corner]):
  2024-11-28  S2 (LFN issued; INFR(2024)NNNN)
  2025-05-15  S3 (RO issued; 2-month compliance window set)
  2025-10-02  S4 (CJEU referral; case C-NNN/25 lodged; Art. 260(3) specified)
                  Commission-specified daily penalty: €[VERIFY]
                  Commission-specified lump sum: €[VERIFY]

Penalty calculation under 2023 Communication (illustrative):
  R_daily         = 3,400 [VERIFY]
  R_lump          = 1,140 [VERIFY]
  LS_min × n      = 200,000 [VERIFY]
  C_s             = 8 (NIS2 flagship; high importance in 2024–2025 Commission strategy)
  C_d             = 1.6 (12 months past deadline at referral)
  n               = 1.0
  N_days_past     = 365 (referral one year past deadline)
  Daily penalty   = 3,400 × 8 × 1.6 × 1.0       = €43,520 / day
  Lump sum        = max(200,000, 1,140 × 8 × 365 × 1.0)
                  = max(200,000, 3,328,800)     = €3,328,800

Risk score:
  R_stage         = 5 (CJEU referral)
  R_pattern       = 2 (occasional LFN; no Art. 260)
  R_directive     = 4 (NIS2 flagship)
  R_conformity    = 3 (ASSUMED — skill E not run; non-notification track does not
                      strictly require it but the substantive shadow is significant)
  Composite R     = 0.4 × 5 + 0.2 × 2 + 0.2 × 4 + 0.2 × 3
                  = 2.0 + 0.4 + 0.8 + 0.6
                  = 3.8 → HIGH (just below CRITICAL threshold of 4.0)

Mitigation:
  Pathway 1: notification of complete NIM (cures Art. 260(3) outright; expected
             outcome: case closure; cost: low operationally; but may surface a
             substantive Art. 258 follow-up if the notified measures are non-conforming)
  Pathway 2: NIM enactment plus drafting confirmation by national legal services that
             measures fully reflect Annex I and II essential / important entity
             obligations
  Pathway 3: pre-CJEU procedural-irregularity defence (low success probability)
```

All numerical inputs above must be replaced with values verified against the 2023
Communication current text and the Commission's specified figures in the actual case.
Where the Commission Press Corner identifies the specific MS subject to NIS2 Art. 260(3)
referrals, retrieve the press release URL and substitute the MS name; until that
verification, this worked example is `[VERIFY procedural facts]` throughout.

---

## Localization Notes

When adapting this skill for a specific Member State or EFTA-pillar State:

1. Replace generic MS references with the named State and its ISO code; mark every
   procedural date `[VERIFY]` until verified against the Commission Press Corner.
2. For Art. 260(3) calculations, use the **n-factor for that specific MS** from the most
   recent Commission Communication update. The n-factor table is published periodically;
   verify currency.
3. For EFTA-pillar States (IS, NO, LI), confirm via skill G that the directive has been
   incorporated into the relevant EEA Annex by Joint Committee Decision before invoking
   the SCA Arts. 31–32 mirror.
4. For the ESA reasoned-opinion procedure, confirm the State's national gazette has
   recorded the transposition or the absence thereof; the Storting (NO) and Althingi (IS)
   data feeds are useful primary sources.
5. Mark every locally-researched procedural fact with confidence scoring per Section:
   Confidence Scoring. Note in the Glass Box the jurisdiction-specific research and
   sources consulted.
6. Where the analysis is run for the trade-federation persona at sector-wide scale,
   batch the analysis by directive across all 27 EU MS and the three EFTA-pillar
   States, and present the cross-MS scoreboard with explicit per-pair audit trails
   underneath the rollup.

---

## Provenance

Created by Legalcode (2026-04-28). Original synthesis based on:

- The seven-skill EU Legislative Compliance suite design brief
  (`references/eu-suite-design-brief.md`).
- The structural rigour of `legalcode-policy-gap-analysis` (1,408 lines) — Design /
  Operational Effectiveness distinction, MINIMUM Score rule, 3-Pass Self-Interrogation,
  Glass Box Audit Trail, 5-level Confidence Scoring — adapted to the EU
  infringement-procedure subject matter.
- TFEU primary text: Arts. 258, 260(1), 260(2), 260(3), 288, 294. ELI:
  `https://eur-lex.europa.eu/eli/treaty/tfeu_2008/`.
- EEA primary text and SCA: EEA Arts. 7, 102, 103, 109; SCA Arts. 31, 32.
- _Commission v Belgium_, Case C-543/17, ECLI:EU:C:2019:573 — first application of
  Art. 260(3).
- _Commission v France_, Case C-304/02, ECLI:EU:C:2005:444 — first cumulation of lump
  sum and periodic penalty under Art. 228 EC / Art. 260(2) TFEU.
- _Commission v Germany_, Case C-503/04, ECLI:EU:C:2007:432 — Art. 228 / 260(2) iteration
  on lump-sum exposure for past non-compliance.
- _Commission v Greece_, Case C-378/13, ECLI:EU:C:2014:2405 — Art. 260(2) penalty for
  state-aid recovery non-compliance.
- _Marleasing_, Case C-106/89, ECLI:EU:C:1990:395 — interpretive cure for ambiguous NIM.
- _CILFIT_, Case C-283/81, ECLI:EU:C:1982:335; _Codan_, Case C-236/97,
  ECLI:EU:C:1998:208; _EMU Tabac_, Case C-296/95, ECLI:EU:C:1998:152 — multilingualism /
  equal authenticity of language versions.
- Commission Communication on the Application of Art. 260(3) TFEU (2023), URL:
  `https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:52023XC0104(01)`
  [VERIFY exact CELEX assignment and current text on EUR-Lex].
- Commission Communication on Application of Art. 228 EC, SEC(2005) 1658, with periodic
  updates of n-factor and flat-rate amounts.
- Single Market and Competitiveness Scoreboard infringement methodology:
  `https://single-market-scoreboard.ec.europa.eu/enforcement-tools/infringements_en`.
- ESA Internal Market Scoreboard (EFTA pillar): `https://www.efta.int/`.
- CURIA / InfoCuria case database: `https://curia.europa.eu/`.
- EFTA Court register: `https://eftacourt.int/cases/`.
- Commission Press Corner monthly infringements package:
  `https://ec.europa.eu/commission/presscorner/`.
- N-Lex (national execution measures): `https://eur-lex.europa.eu/collection/n-law/mne.html`.
- IATE (terminology, 24 languages): `https://iate.europa.eu/`.
- AKN4EU (LegalDocML 1.0, OASIS, 2018) as the AKN4EU subschema for EU institutions —
  used by LEOS.
- LegalRuleML (OASIS, 2021) for the deontic rule encoding.
- Worked-example calibration: NIS2 Directive (Directive (EU) 2022/2555, CELEX
  32022L2555, OJ L 333, 27.12.2022, p. 80; transposition deadline 17 October 2024).
- All statutory references, judgment paragraph numbers, and penalty figures cited from
  memory carry hallucination risk and **must be verified against authoritative sources
  (EUR-Lex, CURIA, EFTA Court register, Commission Press Corner) before use in
  regulatory submissions, infringement-procedure defence, or board reporting**.
