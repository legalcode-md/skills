---
name: legalcode-eea-incorporation-tracker
description: Tracks the European Economic Area (EEA) Joint Committee Decision (JCD) process for incorporating
  EU acts into the EEA Agreement so that they apply in Iceland, Norway, and Liechtenstein on the EFTA
  pillar.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Tracks the European Economic Area (EEA) Joint Committee Decision (JCD) process for incorporating EU acts into the EEA Agreement so that they apply in Iceland, Norway, and Liechtenstein on the EFTA pillar. Operates against the EEA Agreement's two-pillar architecture (Art. 7 EEA on incorporation; Art. 102 EEA on the JCD procedure with its six-month timeline and "serious difficulty" clause; Art. 103 EEA on constitutional reservations and the suspension of entry into force pending parliamentary approval), the Surveillance and Court Agreement (Art. 31 SCA mandating ESA monitoring; Art. 32 SCA on referral to the EFTA Court — the EFTA-pillar mirror of TFEU Art. 258), and the homogeneity principle that drives the EFTA Court to track CJEU jurisprudence. Covers the full incorporation lifecycle for a named act — EEA-relevance assessment, EEA EFTA comments and technical adaptations, JCD adoption in the EEA Joint Committee, Art. 103 parliamentary approval in the Althingi (IS), Storting (NO), or Landtag (LI), entry into force, national transposition by IS/NO/LI for directives, and ESA Internal Market Scoreboard / Art. 31 SCA monitoring status. Worked examples drawn from the NIS2 Directive (Directive (EU) 2022/2555, CELEX 32022L2555), the AI Act (Regulation (EU) 2024/1689, CELEX 32024R1689), GDPR (Regulation (EU) 2016/679, CELEX 32016R0679), DORA (Regulation (EU) 2022/2554, CELEX 32022R2554), CSRD (Directive (EU) 2022/2464, CELEX 32022L2464), and CSDDD (Directive (EU) 2024/1760, CELEX 32024L1760), with EFTA Court anchors *EFTA Surveillance Authority v Norway* (E-3/00, ECLI:EFTA:E-3-00) and *EFTA Surveillance Authority v Iceland* (E-12/13, ECLI:EFTA:E-12-13). Operating modes: government persona dominates (EEA EFTA ministry running incorporation, ESA itself); also law firms advising IS/NO/LI clients, companies operating in IS/NO/LI, and trade federations engaging the EEA EFTA pillar. Jurisdictional scope: EEA Agreement (Iceland, Liechtenstein, Norway, plus the 27 EU Member States); EU pillar interaction via TFEU Art. 288.


# Legalcode EEA Incorporation Tracker

> **Disclaimer**: This skill provides a framework for AI-assisted EEA Joint Committee
> Decision tracking and EEA incorporation status analysis. It does not constitute legal
> advice and does not create an attorney-client relationship. All outputs should be
> reviewed by qualified legal counsel licensed in the relevant jurisdictions before use.
> This skill does not replace formal legal review by qualified EU and Member State
> counsel. It produces a structured framework to support a human-led review — not a
> substitute for one.
> Citations to EU directives, regulations, CJEU/EFTA Court judgments, and Member State
> implementing measures must be verified against authoritative sources (EUR-Lex, CURIA,
> national official journals) before use in regulatory submissions, infringement
> proceedings, or board reporting. EU law evolves continuously; transposition status,
> infringement procedures, and consolidated text versions change frequently. The 24
> official EU language versions of every act are equally authentic; reconcile divergent
> versions before relying on any single language for a definitive interpretation
> (CILFIT C-283/81; Codan C-236/97; EMU Tabac C-296/95).

## Purpose and Scope

This skill tracks where a given EU act sits in the EEA Joint Committee Decision (JCD)
pipeline that controls its application in Iceland, Liechtenstein, and Norway — the
three EEA EFTA states. The EEA Agreement does not extend EU law automatically; every
EU act with EEA relevance must be incorporated into one of the EEA Agreement's
twenty-two Annexes or thirty-seven Protocols by a JCD adopted under Art. 102 EEA.
Until that happens, the act has no legal effect on the EFTA pillar. After it happens,
the act may still be suspended pending parliamentary approval under Art. 103 EEA, and
the EEA EFTA states must transpose it (for directives) or accommodate it (for
regulations) within the timetable laid down in the JCD itself. This skill produces a
status snapshot for any named act across all four phases — relevance scoping, JCD
adoption, Art. 103 reservations, national transposition — together with the ESA
Art. 31 SCA monitoring posture.

EEA incorporation is the single largest source of "EU law" that does not arrive on
time in the EFTA pillar. The accumulated backlog of un-incorporated acts (the
"acquis backlog") is a recurring item in EEA Joint Committee communiqués and a
subject of repeated Norwegian and Icelandic political reporting. This skill names the
phases, dates, and decision-makers explicitly so that government counsel can plan
parliamentary timelines, ESA can size its surveillance docket, and private actors can
forecast when an EU obligation will become enforceable on them in IS/NO/LI.

**Covers:**

- EEA-relevance assessment for any EU act (consuming the relevance flag from the
  obligation register produced by `legalcode-eu-directive-analyzer`)
- JCD pipeline status discovery: scoping → EFTA comments → adaptation drafting →
  JCD adoption → Art. 103 reservation → entry into force
- Per-EFTA-state Art. 103 EEA constitutional reservation status (Althingi for IS,
  Storting for NO, Landtag for LI)
- National transposition status in IS/NO/LI after JCD entry into force (handing off
  to `legalcode-eu-transposition-tracker` extended to the EEA EFTA states)
- ESA Art. 31 SCA monitoring posture and Art. 32 SCA referral pipeline against
  Iceland, Norway, and Liechtenstein for the named act
- Two-pillar structure: how the EU pillar (Commission/CJEU) and the EFTA pillar
  (ESA/EFTA Court) interact under the homogeneity principle
- EEA-Lex queries (the EFTA register of EU acts under EEA consideration)
- Output as Markdown timeline, JSON status schema, AKN4EU stub for the JCD itself,
  LegalRuleML stub asserting homogeneity, and a Glass Box audit trail

**Does not:**

- Extract obligations from the EU act itself — that is the job of
  `legalcode-eu-directive-analyzer`. This skill consumes the analyzer's register.
- Track EU-pillar transposition by the 27 Member States — that is the job of
  `legalcode-eu-transposition-tracker`.
- Produce a per-article conformity verdict — that is the job of
  `legalcode-eu-conformity-assessment`.
- Track Commission-led TFEU 258/260 infringement procedures — that is the job of
  `legalcode-eu-infringement-procedure-tracker` (which also covers Art. 31/32 SCA
  cases against IS/NO/LI but for the procedure itself, not the underlying act's
  incorporation status).
- Operate in Switzerland (which is in EFTA but not in the EEA), or in the
  Faroe Islands (which are outside both).
- Provide legal advice or substitute for qualified Icelandic, Norwegian, or
  Liechtenstein constitutional counsel.

### Sibling Skills in the Suite

This skill is part of the seven-skill EU Legislative Compliance suite. It consumes /
produces the following artefacts:

- **Consumes**: EEA-relevance flag and obligation register from
  `legalcode-eu-directive-analyzer`; per-MS implementation matrix from
  `legalcode-eu-transposition-tracker` (extended to IS/NO/LI once a JCD has entered
  into force).
- **Produces**: EEA incorporation timeline + status object (per-act, per-EFTA-state),
  consumed by `legalcode-eu-infringement-procedure-tracker` (ESA Art. 31/32 cases
  parallel Commission Art. 258/260 cases) and by government persona for parliamentary
  approval planning.

Sibling skills (use whichever is appropriate for the user's stage in the lifecycle):

- `legalcode-eu-directive-analyzer` — extracts the obligation register from a directive
- `legalcode-eu-transposition-tracker` — per-MS implementation matrix
- `legalcode-eu-correlation-table-builder` — directive-to-NIM correlation table
- `legalcode-eu-conformity-assessment` — per-article transposition verdict
- `legalcode-eu-gold-plating-detector` — flags national over-implementation
- `legalcode-eea-incorporation-tracker` — EEA Joint Committee Decision tracking
- `legalcode-eu-infringement-procedure-tracker` — TFEU 258/260 procedure timeline

See [shared EU legislative-data pack](references/eu-legislative-data/)
for canonical identifiers (CELEX, ELI, ECLI), source feeds (Cellar SPARQL, EEA-Lex,
CURIA, EFTA Court), the multilingualism doctrine, the AKN4EU/LegalRuleML output
format specifications, and the worked examples that ground every skill in this suite.

---

## Jurisdiction and Governing Law

This skill operates on the EEA Agreement and the EFTA-pillar institutional framework.
It is jurisdictionally narrower than the EU pillar siblings: only EU acts with declared
or determined EEA relevance fall within scope, and only IS/NO/LI are subjected to per-
state status tracking.

### EEA primary law

- **Art. 1 EEA** — purpose: the most far-reaching free trade agreement ever concluded;
  homogeneous EEA based on common rules.
- **Art. 2(a) EEA** — defines "Agreement" as including the Protocols and Annexes.
- **Art. 6 EEA** — pre-signature CJEU jurisprudence (i.e. case law issued before 2 May 1992) is binding on the EEA EFTA states "in so far as [provisions] are identical in
  substance to corresponding rules of the [EU Treaties]". Together with Art. 3(2) SCA
  this drives the **homogeneity principle**.
- **Art. 7 EEA** — incorporation mechanics. Acts referred to or contained in the
  Annexes (or in JCDs) are binding on the Contracting Parties and form part of (or
  must be made part of) their internal legal order. Regulations "as such"; directives
  by choice of form and method.
- **Art. 102 EEA** — the JCD procedure. Triggered "as closely as possible" to EU
  adoption, with a six-month nominal target from transmission of the act to the JCD
  for taking the decision; if no agreement is reached, the affected part of the
  relevant EEA Annex is provisionally suspended (the "serious difficulty" clause in
  Art. 102(5)).
- **Art. 103 EEA** — constitutional reservations. If a JCD requires fulfilment of
  constitutional requirements (in EU EFTA practice: parliamentary approval), the JCD
  enters into force only when the EEA EFTA state lifts the reservation by notifying
  the Joint Committee. Art. 103(2) caps the suspension at six months from notification
  by the JCD before the affected part of the Annex is provisionally suspended.
- **Art. 104 EEA** — once in force, JCDs are binding on the Contracting Parties.
- **Art. 129 EEA** — language regime: the EEA Agreement is concluded in all official
  EU languages plus Icelandic and Norwegian, all equally authentic; JCDs are published
  in the EEA Supplement to the Official Journal.

EEA Agreement consolidated text on EUR-Lex:
`https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:21994A0103(01)`
EFTA Secretariat-curated EEA Agreement (with all subsequent JCDs incorporated):
`https://www.efta.int/legal-texts/eea-agreement`

### Surveillance and Court Agreement (SCA)

- **Art. 1 SCA** — establishes the EFTA Surveillance Authority (ESA) and the
  EFTA Court.
- **Art. 3(2) SCA** — homogeneity rule for ESA and the EFTA Court: "due account"
  shall be taken of post-signature CJEU jurisprudence in interpreting EEA-relevant
  rules.
- **Art. 31 SCA** — ESA monitoring mandate. ESA delivers reasoned opinions to EEA
  EFTA states that have failed to fulfil EEA obligations; this is the structural
  mirror of TFEU Art. 258. Its three operative pillars are transposition (was the
  act enacted at the national level on time?), conformity (does the national text
  match the EEA-incorporated act?), and enforcement (are the national authorities
  applying it?).
- **Art. 32 SCA** — referral to the EFTA Court. If the state does not comply with
  the reasoned opinion, ESA may bring the matter to the EFTA Court (mirror of
  TFEU Art. 258 second paragraph). Note: there is **no penalty-payment regime in
  the SCA** equivalent to TFEU Art. 260 — judgments against EEA EFTA states are
  declaratory.
- **Protocol 4 SCA** — competition; **Protocol 1 SCA** — internal-market matters.

SCA consolidated text (EFTA Secretariat):
`https://www.efta.int/legal-texts/the-surveillance-and-court-agreement`

### EU primary law referenced for cross-pillar mapping

- **Art. 288 TFEU** — instrument hierarchy. ELI:
  `https://eur-lex.europa.eu/eli/treaty/tfeu_2008/art_288/oj/eng`
- **Art. 258 TFEU** — Commission infringement procedure (mirrored in Art. 31 SCA on
  the EFTA pillar).
- **Art. 260 TFEU** — penalty-payment regime (no SCA equivalent).

### Authoritative EFTA Court anchors

- _EFTA Surveillance Authority v Norway_ (E-3/00, ECLI:EFTA:E-3-00) — Art. 31
  SCA conformity action proceeding to declaratory judgment.
- _EFTA Surveillance Authority v Iceland_ (E-12/13, ECLI:EFTA:E-12-13) —
  Art. 31 SCA non-compliance exemplar against Iceland.
- _Sveinbjörnsdóttir_ (Case E-9/97, ECLI:EFTA:E-9-97) — state liability for
  breach of EEA law (EFTA-pillar mirror of _Francovich_ C-6/90 + C-9/90).
- _L'Oréal_ (Cases E-9/07 and E-10/07, ECLI:EFTA:E-9-07; ECLI:EFTA:E-10-07) —
  homogeneity in trade-mark exhaustion.
- _Posten Norge_ (Case E-15/10, ECLI:EFTA:E-15-10) — competition under
  Protocol 4 SCA.

[VERIFY] flags are deliberate. The exact ECLI suffixes, judgment dates, and
subject-matters for the five EFTA Court anchors require re-verification
against `https://www.eftacourt.int/cases/` before any client-facing use.

### National constitutional law of the EEA EFTA states

- **Iceland**: Stjórnarskrá lýðveldisins Íslands Art. 21 (treaty-making);
  Althingi parliamentary-approval procedures; output in Stjórnartíðindi.
  Althingi API: `https://www.althingi.is`.
- **Norway**: Grunnloven §26(2) (treaty approval where "of special
  importance" or requiring legislation); Storting EU/EEA Committee scrutiny;
  output via Lovdata. Storting API: `https://data.stortinget.no`.
- **Liechtenstein**: Verfassung Art. 8 (treaties concluded by the Reigning
  Prince) plus parliamentary-approval provisions; output via LGBl. Landtag:
  `https://www.landtag.li`.

### Authoritative data sources

- **EEA-Lex** (`https://www.efta.int/eealaw`) — EFTA Secretariat register of
  EU acts under EEA consideration. Authoritative on "is the act on the radar
  at all?" and "what JCD number was assigned?".
- **EFTA Court** — `https://www.eftacourt.int/`.
- **EFTA Surveillance Authority** — `https://www.eftasurv.int/cases-decisions/`;
  Internal Market Scoreboard tracks transposition deficits per EEA EFTA state.
- **EUR-Lex EEA Supplement** — JCDs published at
  `https://eur-lex.europa.eu/oj/direct-access.html` (filter series S).
- **EFTA Joint Committee** —
  `https://www.efta.int/eea/eea-joint-committee`.
- **National parliament APIs** — Althingi, Storting (data.stortinget.no),
  Landtag (`https://www.landtag.li`).

The shared reference pack documents these endpoints — see
`source-playbook.md` (EEA-Lex section) in the [shared EU legislative-data pack](references/eu-legislative-data/).

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

- Persona: Government / EU institution (EEA EFTA ministry running incorporation).
- Operating mode: JCD pipeline status snapshot for a single named act.
- EFTA state focus: all three (IS, NO, LI).
- Stage entry point: scoping (i.e. start at EEA-relevance assessment).
- ESA monitoring scope: include if any open Art. 31/32 SCA case.

State every default applied and request correction.

---

## Workflow

The workflow has nine steps. Steps 1–3 establish scope and persona. Steps 4–7 walk
through the four phases of the EEA incorporation lifecycle (JCD pipeline, Art. 103
reservation, national transposition, ESA monitoring). Step 8 surfaces risk cases.
Step 9 emits outputs.

### Step 1: Accept Input

Capture exactly what the user has provided; do not infer. Required fields:

- **Target EU act**: short title + CELEX (e.g. "NIS2 Directive, CELEX 32022L2555").
  If only a short title is given, resolve to CELEX in Step 3 — never invent.
- **Current JCD process state if known**: e.g. JCD number, "still under EFTA
  scoping". If unknown, leave blank and let Step 4 discover it.
- **Persona context (if pre-declared)**: e.g. "Icelandic Ministry of Justice
  running incorporation". Used in Step 2.

If the user gives only a sectoral cue ("we need to know whether DORA is in
EEA-Lex yet"), accept it and proceed.

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

The **government persona dominates** for this skill: EEA EFTA ministries (MFA
Iceland, Norwegian MFA, Liechtenstein Office for Foreign Affairs) and ESA itself
run the incorporation pipeline. Law-firm and company personas in IS/NO/LI need the
**conditional applicability** answer ("not yet binding because Art. 103 reservation
still open"). Trade-federation users engage on incorporation lobbying.

⟁ CLARIFY — Operating mode

Five operating modes are supported:

1. **JCD pipeline status snapshot** (default): single-act, single-point-in-time
   status across all three EFTA states.
2. **Art. 103 watchlist**: enumerate JCDs currently parked under Art. 103 in
   IS/NO/LI; supports parliamentary calendar planning.
3. **National transposition catch-up**: post-JCD transposition status against
   the JCD-set deadline; hands off to `legalcode-eu-transposition-tracker`.
4. **ESA monitoring posture**: enumerate open Art. 31/32 SCA cases.
5. **Acquis backlog audit**: portfolio mode — for a given EEA Annex (e.g. Annex
   IX Financial Services, Annex XI Electronic Communications), enumerate all EU
   acts pending JCD adoption.

**Why this matters**: a JCD pipeline snapshot is per-act; an acquis backlog
audit is per-Annex and returns dozens of acts. Misclassifying produces either
an undersized output or a sprawling backlog dump.

⟁ CLARIFY — EFTA state focus

1. **All three (IS, NO, LI)**: default.
2. **Single state**: Iceland, Norway, or Liechtenstein only.
3. **Pair**: typical IS+NO for fishery/maritime acts where LI is non-relevant;
   NO+LI where IS has secured an opt-out.

**Why this matters**: state-specific Art. 103 timelines, ESA case loads, and
transposition trackers diverge.

### Step 3: Resolve Act and EEA-Relevance

This step pins down identifiers and determines EEA relevance. **Never invent
CELEX or ELI** — see `identifier-playbook.md` in the shared pack.

1. **Resolve identifiers**: CELEX (e.g. `32022L2555` for NIS2; `32024R1689` for
   the AI Act; `32016R0679` for GDPR; `32022R2554` for DORA; `32022L2464` for
   CSRD; `32024L1760` for CSDDD); ELI (e.g.
   `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng`); OJ reference (e.g.
   "OJ L 333, 27.12.2022, p. 80").
2. **Read the OJ "Text with EEA relevance" flag** at the head of the EU act.
   Confirm: the OJ-printed flag; whether `legalcode-eu-directive-analyzer` has
   produced an `eea-relevance` field; recitals naming the EEA Agreement;
   operative provisions naming EFTA institutions.
3. **Verify against EEA-Lex** (`https://www.efta.int/eealaw`) — the
   authoritative source for "has the EEA Joint Committee taken a position on
   this act?" If listed, capture the EFTA-side procedure number, current
   pipeline state, and any technical adaptations under negotiation.
4. **Resolve disagreements**: OJ flag is indicative; EEA-Lex is dispositive.
   If EEA-Lex shows non-relevance, stop — the rest of the workflow does not
   apply.

Emit a resolved-act block keyed by CELEX, ELI, OJ reference, EEA-relevance
flag, EEA-Lex status, target Annex, and any verification flags.

### Step 4: JCD Status Discovery

Walk the act through the five-stage incorporation lifecycle (detailed below in
**EEA Incorporation Process Stages**). For each stage the act has reached,
capture:

- Date entered.
- Expected exit date — the Art. 102 EEA six-month nominal target from EU
  adoption to JCD; the Art. 103(2) six-month cap on parliamentary suspension.
- Documents — EFTA Standing Committee minutes, JCD draft, JCD adopted text
  with OJ EEA Supplement reference, parliamentary motion numbers.
- Bottlenecks — technical adaptation under negotiation; constitutional review.

Stage assignment rules: no EEA-Lex entry → Stage 1; EFTA Working Group activity
without JCD draft → Stage 2; JCD adopted with number assigned → Stage 3, 4, or
5 depending on Art. 103 status. The JCD remains in Stage 4 federation-wide
until **all** triggered Art. 103 reservations are lifted.

**Worked example (NIS2)**: NIS2 (CELEX 32022L2555) carries "Text with EEA
relevance" in OJ L 333. Whether a JCD has been adopted and what its Art. 103
trajectory is **must be re-verified against EEA-Lex at runtime**. Cite the
EEA-Lex URL with access date in any output.

### Step 5: Per-EFTA-State Constitutional Status

When a JCD triggers Art. 103, three parliamentary tracks run in parallel. For
each state, capture procedure, motion number, committee report, floor vote,
and notification date to the Joint Committee. Detailed per-state procedure
in **Article 103 Constitutional Reservations** below.

**Aggregate status**: until **all** triggered notifications are received, the
JCD is suspended federation-wide. Single-state delays propagate.

**Art. 103(2) cap**: the six-month suspension cap from JCD-notification of the
need for parliamentary approval is the operative deadline. If breached, the
affected Annex part is provisionally suspended.

### Step 6: National Transposition Status

Once a JCD enters into force, IS/NO/LI are bound: regulations as such;
directives requiring transposition by the deadline set in the JCD (not the
underlying directive's deadline, which only bound the 27 EU MS). Hand off to
`legalcode-eu-transposition-tracker` with each EEA EFTA state treated as a
"Member State equivalent". Resolve NIMs via Stjórnartíðindi (IS), Lovdata (NO),
and Liechtensteinisches Landesgesetzblatt (LI). For regulations, capture
flanking legislation only (designated competent authority, penalty regime).

### Step 7: ESA Monitoring Position

Query `https://www.eftasurv.int/cases-decisions/` for cases citing the act's
CELEX. Query `https://www.eftacourt.int/` for EFTA Court cases. Capture case
number, type (Art. 31 letter; reasoned opinion; Art. 32 application), stage,
subject-matter, dates. Detail in **ESA Surveillance Mandate** below.

Score per state: **Green** (in force; transposed; no ESA case);
**Amber** (transposition overdue or open Art. 31 letter); **Red** (reasoned
opinion or Art. 32 application or EFTA Court non-compliance judgment).

### Step 8: Identify Risk Cases

Surface management-attention items. Four dominant risk patterns:

- **Art. 103 overdue**: Art. 103(2) cap expired or within 30 days of expiry.
- **JCD adoption overdue**: in scoping/drafting materially longer than the
  Art. 102 six-month nominal — an acquis-backlog marker.
- **National transposition overdue**: JCD-set deadline passed without NIM
  publication.
- **ESA escalation**: reasoned opinion or Art. 32 application pending/decided.

For each risk, produce: label; severity (RED/AMBER/GREEN); operative deadline;
recommended next step; decision-maker (e.g. "MFA Iceland", "Storting Foreign
Affairs Committee", "Landtag plenary", "ESA Internal Market Affairs
Directorate").

### Step 9: Emit Outputs

Produce all four standards-based artefacts plus the Glass Box audit trail —
templates below.

---

## EEA Incorporation Process Stages

The EEA incorporation lifecycle has five stages. This section describes each in
detail with timing expectations and known bottlenecks.

### Stage 1: EEA-relevance scoping

**Trigger**: EU adopts a new act, typically with a "Text with EEA relevance" line.
**Actors**: EFTA Secretariat; sectoral EFTA Working Groups; EFTA Standing
Committee. **Question**: is the act EEA-relevant in substance? Examined against
the four freedoms and EEA flanking policies; carve-outs for agriculture/fisheries
(largely outside the EEA), taxation (mostly outside), CFSP (outside), and
Liechtenstein customs-union files. **Output**: EFTA Standing Committee position —
relevant / partial / not relevant. **Timing**: weeks to months. **Bottlenecks**:
digital files cutting across all four freedoms (DSA, DMA, AI Act) take longest
because carve-outs are not obvious.

### Stage 2: EFTA comments and adaptation drafting

**Trigger**: Stage 1 confirms relevance. **Actors**: EFTA Working Groups; EFTA
Secretariat; Commission DG on the EU side. **Output**: a draft JCD text with
technical adaptations — institutional substitutions ("ESA" for "Commission";
"EFTA Court" for "CJEU"; "EEA Joint Committee" for "Council"); authority
designation language for IS/NO/LI; reconciliation of cross-references to
un-incorporated EU acts (a chronic source of delay); Liechtenstein small-state
derogations; transitional periods running from JCD entry into force, not from
EU adoption. **Timing**: months to years. **Bottlenecks**: EU-agency files
require resolving EFTA-state agency participation without voting rights — a
constitutional/political question, not a drafting one. DORA, AI Act, NIS2 sit
in this slow lane.

### Stage 3: JCD adoption

**Trigger**: adaptation drafting complete; EEA Joint Committee on calendar
(several meetings per year). **Actors**: EEA Joint Committee — Commission
representative and IS/NO/LI heads of mission; decisions by consensus.
**Output**: numbered JCD (e.g. "Decision of the EEA Joint Committee No N/202n")
amending the relevant Annex; published in OJ EEA Supplement. **Timing**: once
on the calendar, days. Getting onto the calendar is the slow part.
**Bottlenecks**: bundling — a JCD may bundle multiple acts; the laggard sets
the pace.

### Stage 4: Art. 103 constitutional reservation

**Trigger**: Stage 3 JCD requires parliamentary approval in any EFTA state.
**Process**: see Step 5 of the workflow and **Article 103 Constitutional
Reservations** below. **Output**: per-state notification to the Joint Committee.
**Timing**: Art. 103(2) caps suspension at six months from JCD-notification;
politically sensitive files (financial-services supervisory regulations;
Iceland's banking-supervision file in the early 2010s) have breached the cap,
triggering provisional suspension. **Bottlenecks**: coalition-government
scheduling; legal-service queries on whether approval is constitutionally
required at all.

### Stage 5: Entry into force

**Trigger**: all Art. 103 reservations lifted (or none triggered).
**Output**: JCD enters into force on the date specified — typically the day
after the last notification. The act, as adapted, becomes part of the relevant
Annex and binds the EEA EFTA states. The next clock — national transposition —
starts running on this date for directives.

### Total cycle time

- **Best case** (uncontroversial sectoral update, no Art. 103): months from EU
  adoption to JCD entry into force.
- **Typical**: 1–3 years.
- **Worst case** (politically sensitive or agency-heavy file, Art. 103 in all
  three states): 4+ years; the AML/CTF and financial-services files repeatedly
  hit this band.

---

## Article 103 Constitutional Reservations

Art. 103 EEA is the EFTA-pillar device that reconciles the EEA Joint Committee's
international decision-making with the constitutional sovereignty of IS, NO, and LI.
The article provides that where a JCD's binding effect "is subject to fulfilment of
constitutional requirements", the JCD enters into force only when the relevant state
has notified compliance with those requirements. Until notification, the affected
part of the EEA Annex does not apply on the EFTA pillar.

### When Art. 103 is triggered

The trigger is constitutional, not political. A reservation is appropriate where:

- **Iceland**: the JCD necessitates legislation (Lög) requiring Althingi enactment.
  The bare incorporation of an act is treated as a treaty change on the EEA side and
  is approved via parliamentary resolution; subsequent transposition into Icelandic
  law typically requires a separate Lög.
- **Norway**: the JCD is "of special importance" or requires legislation, per
  Grunnloven §26(2). Storting consent is the operative requirement.
- **Liechtenstein**: the JCD modifies Landesgesetzgebung or imposes financial
  obligations on the state, requiring Landtag approval.

A pure technical-update JCD (e.g. minor adjustments to a financial-services Annex
that already implement the EU framework) often does not trigger Art. 103 in any of
the three states.

### Operational workflow per state

**Iceland — Althingi**: MFA tables a þingsályktunartillaga (parliamentary
resolution) with explanatory Greinargerð under the EEA-treaty-approval procedure;
Utanríkismálanefnd (Foreign Affairs Committee) leads, sectoral committees
co-report; floor vote; MFA notifies the Joint Committee. Subsequent Lög
transposition tracked separately via Stjórnartíðindi.

**Norway — Storting**: government tables a Prop. S (consent proposition) for the
JCD and, where transposition needs primary legislation, a parallel Prop. L;
Utenriks- og forsvarskomiteen leads the Prop. S, sectoral committees lead the
Prop. L; floor vote; MFA notifies the Joint Committee.

**Liechtenstein — Landtag**: government tables a Bericht und Antrag (BuA) for
the JCD and, where needed, a parallel BuA for the transposition law; sectoral
committee leads; plenary vote (no upper chamber); Office for Foreign Affairs
notifies the Joint Committee.

### Worked examples

**AML/CTF directives**: each successive AMLD requires fresh parliamentary
approval in each EEA EFTA state; the file is chronically slow. [VERIFY against
EFTA Joint Committee communiqués and Linklaters / Wiersholm EEA bulletins.]

**Iceland's ESA-supervisory-authorities file**: post-2008 incorporation of the
ESMA/EBA/EIOPA regulations (1093/2010, 1094/2010, 1095/2010) ran into
substantial Art. 103 delay arising from constitutional concerns about delegating
supervisory powers to a non-Icelandic body. Resolved by JCDs adopted in 2016
substituting ESA for the relevant supervisory decisions. The canonical example
of a file where Art. 103 review of the procedure itself drove the timetable.
[VERIFY: JCD numbers and exact 2016 dates.]

### Risk patterns

- **Cap breach**: Art. 103(2) six-month cap exceeded → provisional suspension of
  the affected Annex part. Politically prominent.
- **Cascading reservation**: a JCD bundling several acts faces Art. 103 in only
  one state, but the entire JCD is suspended federation-wide.
- **Election dissolution**: an early IS/NO/LI election may extinguish a pending
  consent motion, requiring re-tabling.

---

## Two-Pillar Structure

The EEA Agreement runs two parallel pillars — **EU pillar** (Commission, CJEU,
Council, EP, EU agencies) and **EFTA pillar** (ESA, EFTA Court, EFTA Standing
Committee, EFTA Secretariat) — bridged by the **EEA Joint Committee** (JCD
adoption) and the **EEA Council** (political direction). This skill operates
predominantly on the EFTA pillar but reads from both: incorporation is by
definition cross-pillar.

| EU pillar                         | EFTA pillar                       | Bridging body                     |
| --------------------------------- | --------------------------------- | --------------------------------- |
| European Commission               | EFTA Surveillance Authority (ESA) | —                                 |
| Court of Justice of the EU (CJEU) | EFTA Court                        | —                                 |
| EU Council                        | —                                 | EEA Council                       |
| European Parliament               | —                                 | EEA Joint Parliamentary Committee |
| Council of Ministers              | EFTA Standing Committee           | EEA Joint Committee               |

ESA's Art. 31 SCA mandate is the explicit EFTA-pillar mirror of TFEU Art. 258 —
both authorities issue LFNs and reasoned opinions, both refer non-compliant
states to their respective courts.

### The homogeneity principle

The doctrine that drives the EFTA pillar to mirror EU pillar interpretive
outcomes. Sources: **Art. 1 EEA** (purpose — a "homogeneous EEA"); **Art. 6 EEA**
(pre-signature CJEU case law is authoritative where the EEA provision is
"identical in substance"); **Art. 3(2) SCA** (post-signature CJEU case law:
ESA and the EFTA Court "shall pay due account"); **EEA preamble recital 4**
("as uniform as possible interpretation").

EFTA Court jurisprudence has followed the CJEU consistently; where it diverges
it reasons expressly. The CJEU cites EFTA Court decisions where persuasive
(notably _Maglite_ on parallel imports). This is the reason the LegalRuleML
output emits a constitutive rule asserting equivalence between EU obligation
and EEA obligation in any incorporated act.

Practical consequences: definitional alignment (a GDPR "data controller" means
the same on both pillars); remedy parity (state liability on the EFTA pillar
under _Sveinbjörnsdóttir_ E-9/97 mirrors _Francovich_ C-6/90 + C-9/90);
procedural parity (rights of defence, effective judicial protection).

### Where homogeneity bends

- **No Art. 267 TFEU equivalent**: the EFTA Court has only an advisory
  preliminary-reference jurisdiction under Art. 34 SCA (in practice followed
  but not formally binding).
- **No Art. 260 TFEU equivalent**: the EFTA Court cannot impose penalty
  payments; ESA's toolbox ends at the declaratory judgment.
- **EU-agency governance**: EEA EFTA states participate as observers but
  cannot vote on supervisory decisions — the source of Stage 2 institutional
  adaptations.

---

## ESA Surveillance Mandate

ESA's surveillance mandate under Art. 31 SCA covers transposition (was the EEA-
incorporated act enacted into national law on time?), conformity (does the national
text faithfully implement the act?), and enforcement (are the national authorities
applying the act in practice?). This is the same three-pillar mandate that the
European Commission exercises under TFEU Art. 258 against EU MS, with two operative
differences: ESA only acts against IS/NO/LI, and the SCA has no Art. 260
penalty-payment regime.

### The ESA escalation ladder

1. **Pre-letter dialogue** (informal). ESA writes to the responsible ministry
   asking for explanation. No procedural deadline.
2. **Letter of formal notice** under Art. 31 SCA. Equivalent of the Commission LFN.
   The state has two months (or such other period as ESA fixes) to respond.
3. **Reasoned opinion** under Art. 31 SCA. Sets out ESA's view of the breach and a
   compliance deadline.
4. **Application to the EFTA Court** under Art. 32 SCA. Mirror of TFEU Art. 258
   second paragraph.
5. **Judgment** of the EFTA Court — declaratory only. The state is required to take
   the necessary measures to comply.
6. **Compliance step** by the state.

There is no equivalent of TFEU Art. 260: a non-complying state can be sued again
under Art. 31 SCA in respect of the new failure (the failure to comply with the
EFTA Court judgment) but no penalty-payment regime applies.

### Internal Market Scoreboard

ESA publishes an Internal Market Scoreboard tracking the EEA EFTA states'
transposition deficit (proportion of EEA-incorporated directives whose transposition
deadline has passed and that are not yet transposed). The Commission publishes a
parallel Single Market Scoreboard for the 27 EU MS. Together the two scoreboards
provide the EEA-wide compliance picture.

ESA Internal Market Scoreboard archive (current and historical):
`https://www.eftasurv.int/single-market/internal-market-scoreboard/` [VERIFY exact
URL slug; ESA periodically reorganises its publications structure.]

### Worked examples

_EFTA Surveillance Authority v Norway_ (Case E-3/00, ECLI:EFTA:E-3-00) — fixed
exemplar of an Art. 31 SCA action proceeding to declaratory judgment.
_EFTA Surveillance Authority v Iceland_ (Case E-12/13, ECLI:EFTA:E-12-13) —
exemplar of an Art. 31 SCA action against Iceland. **Verify substantive
subject-matter, dates, and ECLI suffixes against
`https://www.eftacourt.int/cases/`** before quoting in client-facing output.

### How to read ESA case status

ESA cases divide between "Internal Market Affairs" and "Competition and State
Aid" directorates; this skill operates in the former. Each case file carries the
LFN, state response, reasoned opinion, decision to refer, and (where filed) the
Art. 32 application numbered "Case E-XX/year". Report per state the count of
open cases at each rung of the ladder.

---

## EEA-Lex

EEA-Lex is the EFTA Secretariat's register of EU acts under EEA consideration —
the operational source of truth for the JCD pipeline. Located at
`https://www.efta.int/eealaw`.

**What EEA-Lex tracks**: EU acts identified as potentially EEA-relevant; EFTA
Working Group activity per act; draft JCD text; adopted JCDs with number and
OJ EEA Supplement reference; Art. 103 status per state; linked national
transposition citations where reported.

**How to query**: search by CELEX (e.g. `32022L2555` for NIS2). If listed,
capture procedure number, stage, and attached documents. If not listed, the
act is either not yet identified as EEA-relevant or too new to have been
catalogued; cross-check EFTA Standing Committee minutes.

**What EEA-Lex does not tell you**: conformity of national transpositions
(go to ESA Internal Market Scoreboard and N-Lex equivalents); detailed
technical adaptations (go to the JCD text in OJ EEA Supplement); the EU act
text itself (go to EUR-Lex).

**Citation discipline**: cite EEA-Lex URL with access date. The register is
live; status changes between access and analysis.

---

## Notable Backlog and Acquis Drift

The "acquis backlog" refers to the accumulated set of EU acts that are EEA-relevant
but have not yet been incorporated by JCD. The backlog has been a recurring item in
EEA Joint Committee communiqués and an active subject in Norwegian and Icelandic
parliamentary reporting. Its existence and political dimension shape user
expectations for this skill.

### Why backlog accumulates

- EU output volume has grown sharply since 2010 (Banking Union, Digital Single
  Market, Green Deal, AI Act): the EEA EFTA states and the Commission negotiate
  technical adaptations on each, in parallel with their existing workload.
- Files involving EU agencies (financial services, medicines, cybersecurity) require
  protracted institutional adaptation negotiations.
- Cross-references between EU acts trap "fresh" acts behind older, un-incorporated
  precursor acts.
- Political controversy (e.g. the Third Energy Package; the financial-services
  supervisory regulations) extends Stage 2 indefinitely.

### How backlog is reported

EFTA Secretariat annual report on EEA legal affairs (backlog metrics);
Norwegian Stortingsmelding White Papers on EEA cooperation; Icelandic
Greinargerð before Althingi Foreign Affairs Committee; Liechtenstein
government annual report to the Landtag; EEA Council joint communiqués.

### Operational implications

For a private-actor user (company, federation), the implication is
**contingent applicability**: an EU obligation announced at time T may not bite
on the EFTA pillar until time T + 3 years; project plans must factor in the
JCD timetable. For a government user, the implication is **prioritisation**:
ministries decide which laggard files to clear first; this skill's "acquis
backlog audit" mode supports prioritisation by listing all pending acts in a
named Annex, ordered by age.

---

## Anti-Patterns

This skill is to be run with discipline. The following anti-patterns produce
wrong, misleading, or non-actionable outputs.

### 1. Treating the OJ "EEA relevance" line as dispositive

The "Text with EEA relevance" line is a **Commission indicator**, not an
EEA-side determination. The relevance determination is made by the EFTA
Standing Committee in Stage 1; the act applies on the EFTA pillar only after
JCD entry into force. **Right approach**: capture the OJ flag, then verify
EEA-Lex.

### 2. Confusing EU and EEA transposition deadlines

EU directives carry deadlines binding the 27 EU MS. That deadline **does not
bind IS/NO/LI** — their deadline runs from JCD entry into force, set in the
JCD itself. Reporting an Icelandic transposition as "overdue" because the EU
deadline has passed (where no JCD has been adopted) is a factual error.
**Right approach**: read the deadline from the JCD; note when no JCD exists
yet (no EFTA-pillar obligation).

### 3. Conflating ESA and Commission cases

ESA Art. 31 SCA cases run against IS/NO/LI; Commission TFEU Art. 258 cases
run against the 27 EU MS. The two pipelines are parallel and distinct.
"The Commission has opened a case against Norway" is wrong — ESA, not the
Commission, has surveillance jurisdiction over Norway. **Right approach**:
route Commission proceedings to `legalcode-eu-infringement-procedure-tracker`;
route ESA proceedings here.

### 4. Inventing JCD numbers, ECLIs, or CELEX

JCD numbers follow "Decision of the EEA Joint Committee No N/YYYY"; ECLIs
follow `ECLI:EFTA:E-N-YY`; CELEXes follow the OJ pattern. Inventing any of
these is misuse. **Right approach**: verify against EEA-Lex (JCDs), the EFTA
Court database (ECLIs), and EUR-Lex (CELEX); tag every unverified value with
`[VERIFY]`.

### 5. Treating Art. 103 as a delay tactic

Art. 103 EEA is a constitutional safeguard, not a stalling mechanism. The
Art. 103 path is the constitutional path; absence in a relevant case would be
a constitutional defect. **Right approach**: report Art. 103 status factually
against the Art. 103(2) six-month cap.

### 6. Treating the EEA Agreement as static

Each JCD amends one of the Annexes or Protocols. Citing "Annex IX EEA" without
a consolidated-version date risks a superseded version. **Right approach**:
cite as `(consolidated as at <date>)` or pin to the introducing JCD.

### 7. Ignoring Liechtenstein

A JCD requires Liechtenstein's consent; an Art. 103 reservation in the Landtag
suspends the JCD federation-wide; ESA brings Art. 31 SCA cases against
Liechtenstein. Outputs reporting only IS and NO are operationally incomplete.
**Right approach**: include LI by default; state when excluded and why.

### 8. Skipping the constitutional layer

Focus on transposition deadlines without first establishing JCD entry into
force produces nonsense ("Liechtenstein has not transposed an act it is not
yet bound by"). The EFTA-pillar obligation arises only on JCD entry into force.
**Right approach**: process Stages 1–5 in order; do not jump to Stage 6
before Stage 5 resolves.

### 9. Flagging "no EEA relevance" too quickly

CSDDD looks supply-chain only but turns out, on EFTA Standing Committee
analysis, to be EEA-relevant in part; tax-coordination acts may carry the OJ
flag yet not be EEA-relevant. **Right approach**: defer to EFTA Standing
Committee; in default, mark relevance `pending` and continue.

### 10. Overlooking sui-generis instruments

Some EEA additions are not JCDs in the standard sense — they are protocols (e.g.
the EFTA accession of new EU MS to the EEA), framework agreements (financial
mechanism for EEA EFTA contributions to social and economic cohesion), or
declarations. Each has its own ratification procedure. This skill handles JCDs;
sui-generis instruments require separate handling.

**Right approach**: if the instrument under analysis is not a JCD, name what it is
and step back.

---

## Writing Standards

**Deontic operators** — Use **shall** for binding legal obligations under
primary EEA law (Art. 7 EEA "the acts referred to or contained in the
Annexes... shall be binding"). Use **must** for workflow procedural mandates.
Use **may** for optional steps; **should** for recommended practice. Quote
primary-law operators verbatim where the analytical question turns on them
(e.g. assessing whether Art. 102 EEA's "shall" or "may" governs a step) — do
not paraphrase deontic operators in primary EEA text.

**Citation density** — Every legal claim must be cited. Conventions: EU acts
in prose carry short title + (Regulation/Directive (EU) YYYY/NNN, CELEX, OJ
L NNN, DD.MM.YYYY, p. PP) on first use, e.g. "NIS2 Directive (Directive (EU)
2022/2555, CELEX 32022L2555, OJ L 333, 27.12.2022, p. 80)"; subsequent
references short title only. EEA Agreement and SCA cite as "Art. N EEA" /
"Art. N SCA" with consolidated-version date on first use. JCDs cite as
"Decision of the EEA Joint Committee No N/YYYY" with OJ EEA Supplement
reference. EFTA Court case law: ECLI required (`ECLI:EFTA:E-N-YY`); CJEU
case law: ECLI required (`ECLI:EU:C:YYYY:NN`); short case name in italics
on first reference. National measures: cite Stjórnartíðindi /
Lovtidende / Landesgesetzblatt with act number and year. Footnotes carry
URLs, access dates, internal procedure numbers.

**Language-version reconciliation** — The EEA Agreement is authentic in all
official EU languages plus Icelandic and Norwegian (Art. 129 EEA); the 24 EU
official languages are equally authentic (Reg. 1/1958; _CILFIT_ C-283/81).
When a transposition turns on a definitional term, reconcile across languages
per `multilingualism-playbook.md`. For IS-specific or NO-specific divergence,
the EEA-side authentic text anchors IS/NO domestic litigation; cross-pillar
matters require EU-side cross-check. Do not assume English is canonical.

**Handling the EEA-relevance flag** — Four-state value: `relevant` (EFTA
Standing Committee determined; pipeline active/complete); `pending` (OJ-flagged,
EFTA Standing Committee not yet positioned); `partial` (relevant in part with
carve-outs); `not_relevant` (EFTA Standing Committee determined non-relevance).
A Boolean reduction loses the `partial` and `pending` cases, both common.

**CELEX, ELI, ECLI in prose vs. footnotes** — In prose, parenthetical:
"NIS2 Directive (CELEX 32022L2555)". In structured artefacts (JSON, AKN4EU,
LegalRuleML), use the full ELI URI form. Do not embed bare ECLI strings
without an italicised case name on first reference.

**Tone** — Write for counsel: precise, citation-dense, no rhetorical flourish.
Avoid "obviously", "clearly", "of course". Where contingent, say so explicitly
("contingent on JCD entry into force, expected by [VERIFY]").

---

## External Tool Integration

### Legalcode MCP

The Legalcode MCP server provides the consolidated `legalcode_discover`,
`legalcode_search`, and `legalcode_fetch` tools. Use them via the
`legalcode-search-agent` subagent (per the project CLAUDE.md), not by direct invocation:

- `legalcode_discover`: inspect jurisdiction coverage, facets, and exact filter values.
- `legalcode_search` with `sourceTypes: ["law"]`: query EEA Agreement provisions,
  SCA provisions, and EU acts under consideration.
- `legalcode_search` with `sourceTypes: ["case"]`: query EFTA Court cases by act
  CELEX, legal-basis key, citation, or party.
- `legalcode_search` with `sourceTypes: ["guidance"]`: query ESA guidance papers
  and EFTA Standing Committee minutes.
- `legalcode_fetch`: verify the selected source text before relying on it.

For coverage gaps (notably EEA-Lex, which is not always indexed by general
search), see the source-playbook in the shared reference pack.

### Direct data sources (when MCP coverage is insufficient)

- **EEA-Lex** (`https://www.efta.int/eealaw`): search by CELEX or short title;
  capture procedure number, stage, JCD number where adopted.
- **EFTA Court database** (`https://www.eftacourt.int/`): search by case number,
  party, or subject; capture ECLI, judgment date, disposition.
- **ESA case database** (`https://www.eftasurv.int/cases-decisions/`): search by
  act CELEX or case number; capture LFN/RO/Art. 32 application dates.
- **EUR-Lex Cellar SPARQL** (`https://publications.europa.eu/webapi/rdf/sparql`):
  query for the EU act's metadata, recitals naming EEA, and consolidated versions.
- **OJ EEA Supplement** (via EUR-Lex direct access; filter on series S):
  authoritative text of adopted JCDs.
- **National parliament APIs**: Althingi (`https://www.althingi.is`), Storting
  (`https://data.stortinget.no`), Landtag Liechtenstein (`https://www.landtag.li`).

### Sibling skill handoffs

- Consume the obligation register from `legalcode-eu-directive-analyzer` if
  available; pass through the act's CELEX, ELI, OJ reference, and EEA-relevance
  flag.
- Pass the per-EFTA-state transposition status to `legalcode-eu-transposition-
tracker` (extending its matrix to IS/NO/LI) for downstream conformity work.
- Hand the Art. 31/32 SCA case list to `legalcode-eu-infringement-procedure-
tracker` (EFTA branch) for procedure-level analysis.

### File system

The skill writes to a stable artefact location:

- `eea_status_<celex>.md` — Markdown timeline.
- `eea_status_<celex>.json` — JSON status object.
- `eea_status_<celex>.akn.xml` — AKN4EU stub for the JCD.
- `eea_status_<celex>.legalruleml.xml` — LegalRuleML homogeneity assertion.
- `eea_status_<celex>.audit.json` — Glass Box audit trail.

Where the user requests batch mode (multiple acts), prefix with the EEA Annex
identifier: `annex_ix_eea_status.md`.

---

## Output Format Template

This skill emits five artefacts: Markdown, JSON, AKN4EU, LegalRuleML, and a Glass
Box audit trail. All five are produced for every run.

### Markdown EEA timeline (worked example: NIS2 Directive)

```markdown
# EEA Incorporation Status — NIS2 Directive (CELEX 32022L2555)

**Act**: NIS2 Directive (Directive (EU) 2022/2555 of 14 December 2022 on measures
for a high common level of cybersecurity across the Union, CELEX 32022L2555,
OJ L 333, 27.12.2022, p. 80; ELI https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng).

**OJ EEA-relevance flag**: yes (act published with "Text with EEA relevance" line).

**Verification status**: All EEA-Lex / EFTA Court / ESA / Althingi / Storting /
Landtag fields below are flagged for runtime verification. Cite EEA-Lex URL with
access date in any client-facing output.

## Pipeline state

| Stage                                  | Status                                          | Date     | Source                        |
| -------------------------------------- | ----------------------------------------------- | -------- | ----------------------------- |
| 1. EEA-relevance scoping               | [VERIFY: relevant per EFTA Standing Committee?] | [VERIFY] | EEA-Lex                       |
| 2. EFTA comments / adaptation drafting | [VERIFY]                                        | [VERIFY] | EEA-Lex                       |
| 3. JCD adoption                        | [VERIFY: JCD No N/202n issued?]                 | [VERIFY] | EEA-Lex; OJ EEA Supplement    |
| 4. Art. 103 reservations               | [VERIFY per state]                              | [VERIFY] | Althingi / Storting / Landtag |
| 5. Entry into force                    | [VERIFY]                                        | [VERIFY] | EEA-Lex                       |

## Per-EFTA-state Art. 103 status

| State         | Reservation triggered? | Resolution / motion                  | Date approved | Notification | Status   |
| ------------- | ---------------------- | ------------------------------------ | ------------- | ------------ | -------- |
| Iceland       | [VERIFY]               | [VERIFY: Althingi resolution number] | [VERIFY]      | [VERIFY]     | [VERIFY] |
| Norway        | [VERIFY]               | [VERIFY: Prop. S number]             | [VERIFY]      | [VERIFY]     | [VERIFY] |
| Liechtenstein | [VERIFY]               | [VERIFY: BuA number]                 | [VERIFY]      | [VERIFY]     | [VERIFY] |

## National transposition (post-incorporation)

| State         | Transposition deadline (per JCD) | Transposed? | National measure  | Source          |
| ------------- | -------------------------------- | ----------- | ----------------- | --------------- |
| Iceland       | [VERIFY]                         | [VERIFY]    | [VERIFY: Lög nr.] | Stjórnartíðindi |
| Norway        | [VERIFY]                         | [VERIFY]    | [VERIFY: Lov nr.] | Lovdata         |
| Liechtenstein | [VERIFY]                         | [VERIFY]    | [VERIFY: Gesetz]  | LGBl            |

## ESA Art. 31 / Art. 32 SCA monitoring posture

| State         | Open Art. 31 letters | Open reasoned opinions | Open Art. 32 applications | EFTA Court judgment(s) |
| ------------- | -------------------- | ---------------------- | ------------------------- | ---------------------- |
| Iceland       | [VERIFY]             | [VERIFY]               | [VERIFY]                  | [VERIFY]               |
| Norway        | [VERIFY]             | [VERIFY]               | [VERIFY]                  | [VERIFY]               |
| Liechtenstein | [VERIFY]             | [VERIFY]               | [VERIFY]                  | [VERIFY]               |

## Risk cases

- [Populated by Step 8 of the workflow.]

## Sources

- EEA-Lex (`https://www.efta.int/eealaw`) accessed [DATE]
- EFTA Court database (`https://www.eftacourt.int/`) accessed [DATE]
- ESA case database (`https://www.eftasurv.int/cases-decisions/`) accessed [DATE]
- EUR-Lex (`https://eur-lex.europa.eu/`) accessed [DATE]
- Stjórnartíðindi (`https://www.stjornartidindi.is/`) accessed [DATE]
- Lovdata (`https://lovdata.no/`) accessed [DATE]
- Liechtensteinisches Landesgesetzblatt (`https://www.gesetze.li/`) accessed [DATE]
```

### JSON EEA status schema (per-act, per-EFTA-state)

```json
{
  "$schema": "https://legalcode.dev/schemas/eea-incorporation-status/v1",
  "act": {
    "celex": "32022L2555",
    "short_title": "NIS2 Directive",
    "full_title": "Directive (EU) 2022/2555 of 14 December 2022 on measures for a high common level of cybersecurity across the Union",
    "eli": "https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng",
    "oj_reference": "OJ L 333, 27.12.2022, p. 80",
    "instrument_type": "directive",
    "eu_oj_eea_relevance_flag": true
  },
  "eea_relevance": {
    "status": "pending",
    "comment": "OJ-flagged; EFTA Standing Committee position requires verification",
    "verified_against": ["eu-oj"],
    "to_verify": ["efta-standing-committee", "eea-lex"]
  },
  "jcd_pipeline": {
    "stage": "<one of: scoping | drafting | adopted | reservation | in_force>",
    "stage_entered_date": null,
    "expected_exit_date": null,
    "jcd_number": null,
    "jcd_oj_eea_supplement_reference": null,
    "annex_target": null,
    "technical_adaptations": [],
    "bottlenecks": [],
    "verification_required": ["all fields above"]
  },
  "art_103": {
    "iceland": {
      "reservation_triggered": null,
      "motion_number": null,
      "motion_kind": "thingsalyktunartillaga",
      "session": null,
      "committee_report_date": null,
      "floor_vote_date": null,
      "notification_date": null,
      "status": "<not_triggered | pending | lifted>"
    },
    "norway": "<same shape as iceland; motion_kind 'Prop. S'; committee Innstilling reference under motion_number>",
    "liechtenstein": "<same shape; motion_kind 'BuA'>",
    "art_103_2_cap_breach": false,
    "aggregate_status": "<all_lifted | partial | suspended>"
  },
  "national_transposition": {
    "iceland": {
      "deadline_per_jcd": null,
      "transposed": null,
      "national_measure_citation": null,
      "official_journal_reference": null
    },
    "norway": "<same shape; OJ ref via Lovdata>",
    "liechtenstein": "<same shape; OJ ref via LGBl>"
  },
  "esa_monitoring": {
    "iceland": {
      "open_art_31_letters": [],
      "open_reasoned_opinions": [],
      "open_art_32_applications": [],
      "efta_court_judgments": []
    },
    "norway": "<same shape>",
    "liechtenstein": "<same shape>",
    "scoreboard_position": null
  },
  "risk_cases": [
    {
      "label": "<art_103_overdue | jcd_adoption_overdue | transposition_overdue | esa_escalation>",
      "severity": "<RED | AMBER | GREEN>",
      "deadline": null,
      "next_step": null,
      "decision_maker": null
    }
  ],
  "verification": {
    "access_date": "[DATE]",
    "sources_consulted": [
      "https://www.efta.int/eealaw",
      "https://www.eftacourt.int/",
      "https://www.eftasurv.int/cases-decisions/"
    ],
    "to_verify": ["jcd_pipeline.stage", "art_103.*", "esa_monitoring.*"]
  }
}
```

### AKN4EU stub for the JCD itself

A JCD is a sui-generis decision instrument, not an EU act of the Union. The AKN4EU
representation uses `<doc class="decision">` rather than `<act>`. The FRBR work URI
designates the EEA Joint Committee.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<akomaNtoso xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <doc name="eeaJointCommitteeDecision">
    <meta>
      <identification source="#legalcode-eea-incorporation-tracker">
        <FRBRWork>
          <FRBRthis value="/akn/eea/decision/jc/202n/N/main"/>
          <FRBRuri value="/akn/eea/decision/jc/202n/N"/>
          <FRBRalias name="JCD Number" value="No N/202n"/>
          <FRBRdate date="[VERIFY]" name="adoption"/>
          <FRBRauthor href="#eeaJointCommittee"/>
          <FRBRcountry value="eea"/>
          <FRBRsubtype value="jointCommitteeDecision"/>
        </FRBRWork>
        <FRBRExpression>
          <FRBRthis value="/akn/eea/decision/jc/202n/N/eng@/main"/>
          <FRBRuri value="/akn/eea/decision/jc/202n/N/eng@"/>
          <FRBRdate date="[VERIFY]" name="publication"/>
          <FRBRauthor href="#eeaJointCommittee"/>
          <FRBRlanguage language="eng"/>
        </FRBRExpression>
        <FRBRManifestation>
          <FRBRthis value="/akn/eea/decision/jc/202n/N/eng@.xml"/>
          <FRBRuri value="/akn/eea/decision/jc/202n/N/eng@.xml"/>
          <FRBRdate date="[ACCESS-DATE]" name="manifestation"/>
          <FRBRauthor href="#legalcode-eea-incorporation-tracker"/>
          <FRBRformat value="application/xml"/>
        </FRBRManifestation>
      </identification>
      <references source="#legalcode-eea-incorporation-tracker">
        <TLCOrganization eId="eeaJointCommittee"
                         href="/ontology/organization/eea/jointCommittee"
                         showAs="EEA Joint Committee"/>
        <TLCOrganization eId="esa"
                         href="/ontology/organization/eea/esa"
                         showAs="EFTA Surveillance Authority"/>
        <TLCConcept eId="homogeneity"
                    href="/ontology/concept/eea/homogeneity"
                    showAs="Homogeneity Principle (Art. 1 EEA, Art. 6 EEA, Art. 3(2) SCA)"/>
        <TLCReference eId="incorporated-act"
                      href="/akn/eu/dir/2022/2555/eng@"
                      showAs="NIS2 Directive (CELEX 32022L2555)"/>
        <TLCReference eId="annex-target"
                      href="/akn/eea/agreement/annex/xi"
                      showAs="Annex XI EEA — Electronic Communications, Audiovisual Services and Information Society"/>
      </references>
      <notes source="#legalcode-eea-incorporation-tracker">
        <note eId="vfy-1" type="verification">All [VERIFY]-tagged dates and JCD
        number to be confirmed against EEA-Lex.</note>
      </notes>
    </meta>
    <preface><p>Decision of the EEA Joint Committee No N/202n of [VERIFY]
    amending Annex XI to the EEA Agreement (incorporating Directive (EU)
    2022/2555).</p></preface>
    <preamble>
      <citations><citation>Having regard to the Agreement on the European
      Economic Area, and in particular Article 98 thereof.</citation></citations>
      <recitals><recital eId="rec_1"><num>(1)</num><p>Directive (EU) 2022/2555
      (CELEX 32022L2555) is to be incorporated into the EEA Agreement.</p>
      </recital></recitals>
    </preamble>
    <body>
      <article eId="art_1"><num>Article 1</num><heading>Incorporation</heading>
        <paragraph><content><p>Annex XI to the EEA Agreement is amended as set
        out in the Annex to this Decision.</p></content></paragraph>
      </article>
      <article eId="art_2"><num>Article 2</num><heading>Authentic texts</heading>
        <paragraph><content><p>The texts of Directive (EU) 2022/2555 in the
        Icelandic and Norwegian languages, to be published in the EEA Supplement
        to the Official Journal of the European Union, shall be authentic.</p>
        </content></paragraph>
      </article>
      <article eId="art_3"><num>Article 3</num><heading>Entry into force</heading>
        <paragraph><content><p>This Decision shall enter into force on [VERIFY],
        provided that all the notifications under Article 103(1) of the EEA
        Agreement have been made.</p></content></paragraph>
      </article>
    </body>
  </doc>
</akomaNtoso>
```

### LegalRuleML stub asserting homogeneity

The LegalRuleML output asserts a constitutive rule per obligation in the EU act:
the obligation under the EU act and the equivalent obligation under the EEA-
incorporated act are deontically equivalent. The structure uses
`<lrml:Constitutive>` for the equivalence assertion, `<lrml:Source>` for the act
ELI on each side, and `<lrml:Party>` for the addressee class (e.g. essential
entities under NIS2).

```xml
<?xml version="1.0" encoding="UTF-8"?>
<lrml:LegalRuleML xmlns:lrml="http://docs.oasis-open.org/legalruleml/ns/v1.0/"
                  xmlns:ruleml="http://ruleml.org/spec">
  <lrml:Statements>
    <lrml:ConstitutiveStatement key="hg-nis2-art-21">
      <lrml:hasQualification><lrml:Strength iri="defeasible"/></lrml:hasQualification>
      <ruleml:Implies>
        <ruleml:if><ruleml:And>
          <ruleml:Atom><ruleml:Rel>obligationApplies</ruleml:Rel><ruleml:Var>actor</ruleml:Var><lrml:Source iri="https://eur-lex.europa.eu/eli/dir/2022/2555/art_21/oj/eng"/></ruleml:Atom>
          <ruleml:Atom><ruleml:Rel>establishedIn</ruleml:Rel><ruleml:Var>actor</ruleml:Var><ruleml:Ind>EEA-EFTA-state</ruleml:Ind></ruleml:Atom>
          <ruleml:Atom><ruleml:Rel>jcdInForce</ruleml:Rel><lrml:Source iri="/akn/eea/decision/jc/202n/N"/></ruleml:Atom>
        </ruleml:And></ruleml:if>
        <ruleml:then>
          <lrml:Obligation>
            <lrml:Party iri="/ontology/eu/role/essentialEntity"/>
            <lrml:Source iri="/akn/eea/decision/jc/202n/N/art_1"/>
            <lrml:hasQualification><lrml:Strength iri="binding"/></lrml:hasQualification>
            <ruleml:Atom><ruleml:Rel>implementCybersecurityRiskManagementMeasures</ruleml:Rel><ruleml:Var>actor</ruleml:Var></ruleml:Atom>
          </lrml:Obligation>
        </ruleml:then>
      </ruleml:Implies>
    </lrml:ConstitutiveStatement>
    <lrml:ConstitutiveStatement key="hg-doctrine">
      <ruleml:Implies>
        <ruleml:if><ruleml:Atom><ruleml:Rel>incorporatedByJCD</ruleml:Rel><ruleml:Var>act</ruleml:Var></ruleml:Atom></ruleml:if>
        <ruleml:then>
          <ruleml:Atom>
            <ruleml:Rel>interpretedHomogeneously</ruleml:Rel><ruleml:Var>act</ruleml:Var>
            <lrml:Source iri="/akn/eea/agreement/art/1"/>
            <lrml:Source iri="/akn/eea/agreement/art/6"/>
            <lrml:Source iri="/akn/eea/sca/art/3#par_2"/>
          </ruleml:Atom>
        </ruleml:then>
      </ruleml:Implies>
    </lrml:ConstitutiveStatement>
  </lrml:Statements>
</lrml:LegalRuleML>
```

### Glass Box audit trail

Every run produces an audit trail capturing every decision, source consulted, and
[VERIFY] flag deferred to the user. The audit trail is the regulator-and-auditor-
facing record that the analysis was conducted with discipline.

```json
{
  "$schema": "https://legalcode.dev/schemas/glass-box-audit/v1",
  "skill": "legalcode-eea-incorporation-tracker",
  "skill_version": "1.0",
  "run_id": "<uuid>",
  "run_timestamp_utc": "[ISO-8601]",
  "input": {
    "celex": "32022L2555",
    "user_supplied_persona": null,
    "user_supplied_operating_mode": null,
    "user_supplied_state_focus": null
  },
  "decisions": [
    {
      "step": "1.AcceptInput",
      "decision": "Resolved short title 'NIS2 Directive' to CELEX 32022L2555.",
      "source": "EUR-Lex CELEX lookup",
      "verified": true
    },
    {
      "step": "2.Persona",
      "decision": "Persona defaulted to government / EEA EFTA ministry.",
      "source": "non-interactive default",
      "user_correction_pending": true
    },
    {
      "step": "3.ResolveAct",
      "decision": "OJ EEA-relevance flag observed.",
      "source": "OJ L 333, 27.12.2022, p. 80",
      "verified": true
    },
    {
      "step": "3.ResolveAct",
      "decision": "EEA-Lex pipeline state: pending verification.",
      "source": "https://www.efta.int/eealaw",
      "verified": false,
      "verification_required": true
    },
    {
      "step": "4.JCDStatusDiscovery",
      "decision": "Stage assigned: pending verification.",
      "verified": false,
      "verification_required": true
    }
  ],
  "clarifications_invoked": ["persona", "operating_mode", "state_focus"],
  "clarifications_skipped": [],
  "sources_consulted": [
    "https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng",
    "https://www.efta.int/eealaw",
    "https://www.eftacourt.int/",
    "https://www.eftasurv.int/cases-decisions/"
  ],
  "verify_flags": [
    "jcd_pipeline.stage",
    "art_103.iceland.*",
    "art_103.norway.*",
    "art_103.liechtenstein.*",
    "esa_monitoring.*"
  ],
  "outputs_emitted": [
    "eea_status_32022L2555.md",
    "eea_status_32022L2555.json",
    "eea_status_32022L2555.akn.xml",
    "eea_status_32022L2555.legalruleml.xml"
  ]
}
```

---

## Localization Notes

National-level outputs respect each EEA EFTA state's official languages and
citation conventions.

**Iceland** — Icelandic. Citation: "Lög nr. NN/YYYY um [topic]" or "Stjtíð. A
NNNN". Parliamentary docs: þingsályktun (resolution); frumvarp (bill); lög
(enacted act). Constitutional anchor: Stjórnarskrá lýðveldisins Íslands.

**Norway** — Bokmål and Nynorsk (both authentic for primary legislation).
Citation: "Lov om [topic] (NN-loven)" with date/number; or "Lov av YYYY-MM-DD
nr. NN". Parliamentary docs: Prop. S (consent), Prop. L (legislative), Innst.
(committee recommendation). Constitutional anchor: Grunnloven §26(2).

**Liechtenstein** — German. Citation: "Gesetz vom [date] über [topic] (LGBl.
YYYY Nr. NN)". Parliamentary docs: BuA Nr. N/YYYY. Constitutional anchor:
Verfassung des Fürstentums Liechtenstein.

**Cross-state harmonisation** — Per Art. 129 EEA, the EEA Agreement is
authentic in all official EU languages plus Icelandic and Norwegian; JCDs
publish in the EEA Supplement in all relevant languages. National parliamentary
materials are local-language only. The skill cites local-language sources in
the local language with an English gloss; it does not translate primary text.

**Liechtenstein customs-union complications** — LI is in a customs union with
Switzerland (EFTA but not EEA). Acts touching customs, certain veterinary
matters, or movement of goods carry parallel obligations to Switzerland that
modify EEA application; the skill flags these as `LI-customs-union-carve-out`
and refers to the LI Office for Foreign Affairs.

---

## Provenance

This skill is grounded in the following primary and authoritative secondary
sources. Every fact stated as legal fact in this skill's outputs must trace back
to at least one of these sources or to a properly cited substitute.

### EEA primary law

- **EEA Agreement** — consolidated text (EFTA Secretariat) at
  `https://www.efta.int/legal-texts/eea-agreement`; OJ-published version at
  `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:21994A0103(01)`.
- **Surveillance and Court Agreement (SCA)** — consolidated text at
  `https://www.efta.int/legal-texts/the-surveillance-and-court-agreement`.
- Articles cited: Art. 1 EEA; Art. 2(a) EEA; Art. 6 EEA; Art. 7 EEA; Art. 98 EEA;
  Art. 102 EEA; Art. 103 EEA; Art. 104 EEA; Art. 129 EEA; Art. 1 SCA;
  Art. 3(2) SCA; Art. 31 SCA; Art. 32 SCA; Art. 34 SCA.

### EU primary law

- **TFEU** Art. 288 (instrument hierarchy), Art. 258 (infringement), Art. 260
  (penalty payments). ELI: `https://eur-lex.europa.eu/eli/treaty/tfeu_2008/oj/eng`.
- **Regulation 1/1958** (language regulation), ELI:
  `https://eur-lex.europa.eu/eli/reg/1958/1(1)/oj/eng`.

### CJEU case law (referenced for cross-pillar interpretive doctrine)

- _CILFIT_ (Case C-283/81, ECLI:EU:C:1982:335) — equal authenticity of language
  versions.
- _Codan_ (Case C-236/97, ECLI:EU:C:1998:208) — definitional reconciliation across
  language versions.
- _EMU Tabac_ (Case C-296/95, ECLI:EU:C:1998:152) — language-version comparison.
- _Francovich_ (Joined Cases C-6/90 and C-9/90, ECLI:EU:C:1991:428) — state
  liability (mirrored on EFTA pillar in _Sveinbjörnsdóttir_).
- _Commission v Belgium_ (Case C-543/17, ECLI:EU:C:2019:573) — first application
  of TFEU Art. 260(3) penalty regime; cited for cross-pillar contrast (no SCA
  equivalent).

### EFTA Court case law

- _EFTA Surveillance Authority v Norway_ (Case E-3/00, ECLI:EFTA:E-3-00) —
  exemplar of Art. 31/32 SCA proceedings against Norway. [VERIFY judgment date,
  exact subject-matter, and ECLI suffix against
  `https://www.eftacourt.int/cases/`.]
- _EFTA Surveillance Authority v Iceland_ (Case E-12/13, ECLI:EFTA:E-12-13) —
  exemplar of Art. 31/32 SCA proceedings against Iceland. [VERIFY judgment date,
  exact subject-matter, and ECLI suffix.]
- _Sveinbjörnsdóttir_ (Case E-9/97, ECLI:EFTA:E-9-97) — EFTA Court doctrine of
  state liability for breach of EEA law. [VERIFY ECLI suffix.]
- _Posten Norge_ (Case E-15/10, ECLI:EFTA:E-15-10) — competition case anchoring
  Art. 31 SCA / Protocol 4 SCA practice. [VERIFY ECLI suffix.]
- _L'Oréal_ (Cases E-9/07 and E-10/07, ECLI:EFTA:E-9-07; ECLI:EFTA:E-10-07) —
  trade-mark exhaustion / homogeneity. [VERIFY ECLI suffixes.]

### Worked-example EU acts

- **NIS2 Directive** — Directive (EU) 2022/2555, CELEX 32022L2555, OJ L 333,
  27.12.2022, p. 80; ELI `https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng`.
- **AI Act** — Regulation (EU) 2024/1689, CELEX 32024R1689; ELI
  `https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng`.
- **GDPR** — Regulation (EU) 2016/679, CELEX 32016R0679, OJ L 119, 4.5.2016, p. 1;
  ELI `https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng`.
- **DORA** — Regulation (EU) 2022/2554, CELEX 32022R2554; ELI
  `https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng`.
- **CSRD** — Directive (EU) 2022/2464, CELEX 32022L2464; ELI
  `https://eur-lex.europa.eu/eli/dir/2022/2464/oj/eng`.
- **CSDDD** — Directive (EU) 2024/1760, CELEX 32024L1760; ELI
  `https://eur-lex.europa.eu/eli/dir/2024/1760/oj/eng`.
- **DSA** — Regulation (EU) 2022/2065, CELEX 32022R2065 (regulation contrast).
- **DMA** — Regulation (EU) 2022/1925, CELEX 32022R1925 (regulation contrast).

### Operational data sources

- **EEA-Lex** — `https://www.efta.int/eealaw`.
- **EFTA Court** — `https://www.eftacourt.int/`.
- **EFTA Surveillance Authority** — `https://www.eftasurv.int/`; cases at
  `https://www.eftasurv.int/cases-decisions/`; Internal Market Scoreboard
  under `https://www.eftasurv.int/single-market/internal-market-scoreboard/`
  [VERIFY slug].
- **EUR-Lex** — `https://eur-lex.europa.eu/` (EEA Supplement via direct
  access); Cellar SPARQL at `https://publications.europa.eu/webapi/rdf/sparql`.
- **EFTA Joint Committee documents** —
  `https://www.efta.int/eea/eea-joint-committee`.

### National data sources

- Iceland: Althingi `https://www.althingi.is`; Stjórnartíðindi
  `https://www.stjornartidindi.is/`.
- Norway: Storting `https://data.stortinget.no`; Lovdata `https://lovdata.no/`.
- Liechtenstein: Landtag `https://www.landtag.li`; Landesgesetzblatt
  `https://www.gesetze.li/`.

### Standards specifications

- **Akoma Ntoso (LegalDocML 1.0, OASIS, 2018)** with AKN4EU subschema (LEOS).
- **LegalRuleML (OASIS, 2021)** — deontic rule modelling; spec at
  `https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/`.
- **ELI** — registered URI scheme; technical info at
  `https://eur-lex.europa.eu/eli-register/technical_information.html`.
- **ECLI** — case-law URI scheme. **CELEX** — Publications Office identifier.

### Methodology references

- **Better Regulation Toolbox 2023, Chapter 4**:
  `https://commission.europa.eu/document/download/a21336e2-2a7c-43d2-bb35-d4eee7aa4cd3_en?filename=BRT-2023-Chapter+4-Compliance+implementation+and+preparing+proposals_0.pdf`.
- **Single Market Scoreboard** (comparator for ESA's Internal Market
  Scoreboard) — `https://single-market-scoreboard.ec.europa.eu/`.

### Verification flags

The following anchors require runtime verification before any client-facing
use:

- ECLI suffixes for the EFTA Court cases cited (E-3/00, E-12/13, E-9/97,
  E-15/10, E-9/07, E-10/07) — verify against `https://www.eftacourt.int/cases/`.
- Subject-matter and judgment dates for _ESA v Norway_ (E-3/00) and
  _ESA v Iceland_ (E-12/13).
- ESA Internal Market Scoreboard URL slug (periodically reorganised).
- NIS2 recital referencing the EEA — cited as "Recital 89", verify against
  the OJ-published text.
- Any specific JCD numbers in worked examples — illustrative only; resolve
  via EEA-Lex at runtime.
- Liechtenstein's exact constitutional provision for treaty approval — verify
  against the consolidated Verfassung at `https://www.gesetze.li/`.

This skill operates against a moving target: the EEA Joint Committee meets
regularly; ESA Internal Market Scoreboard updates twice a year; EFTA Court
judgments issue throughout the term; national parliaments sit on their own
calendars. Every output carries an `access_date` field and is a snapshot;
re-run before external publication or regulatory submission.
