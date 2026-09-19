---
name: legalcode-judge-profile
description: Compile a comprehensive judicial profile for US federal or state court judges covering ruling
  tendencies, motion grant/denial rates, case management preferences, trial management style, reversal
  rates, biographical intelligence, judicial philosophy, and strategic recommendations. Use when conducting
  venue strategy analysis, preparing for oral argument, tailoring briefs to a specific judge, evaluating
  a transfer motion under 28 USC § 1404(a), sizing up a newly assigned judge, preparing a settlement strategy
  informed by the judge's resolution tendencies, or building a litigation plan that accounts for the assigned
  forum. Supports US federal district courts, circuit courts of appeal, US bankruptcy courts, state trial
  courts, and state appellate courts. Draws on analytics platforms (Westlaw, Bloomberg Law, Lex Machina,
  Pre/Dicta, Trellis, Docket Alarm, CourtListener), biographical databases (FJC Biographical Directory,
  Senate questionnaires, ABA ratings), and the judge's own published opinions.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Judge Profile

> **Disclaimer**: This skill provides a framework for AI-assisted judicial profiling for
> US litigation practice. It does not constitute legal advice. All outputs should be
> reviewed by a qualified legal professional licensed in the relevant jurisdiction before
> use. Judicial tendency data reflects historical patterns and does not predict future
> rulings in any specific case. Analytics data is only as reliable as the underlying
> docket databases — small sample sizes and data gaps can produce misleading results.
> Statistical tendencies do not establish judicial bias sufficient for recusal under
> 28 USC § 455; use this analysis for preparation, not for unsupported recusal motions.
> Laws, procedural rules, and individual judge preferences change; verify standing orders
> and recent rulings before relying on any element of this profile.

---

## Purpose and Scope

Use this skill to build a structured, research-backed judicial profile that supports
strategic litigation decision-making across the full case lifecycle — from venue selection
before filing through settlement timing, briefing strategy, oral argument preparation,
and trial readiness.

**Covers:**

- Biographical and career intelligence for all US federal Article III judges and most
  state trial and appellate judges
- Motion practice analytics: grant/denial rates by motion type with directional lean
- Case management profile: scheduling, discovery, and case-management-conference style
- Trial management: bench vs. jury, voir dire approach, evidentiary ruling patterns
- Reversal and appeal posture: rate, by issue type, and by reviewing court tendency
- Judicial philosophy: textualism/purposivism, statutory interpretation, doctrinal anchors
- Settlement pressure profile: mandatory settlement conferences, timing, resolution rate
- Strategic recommendations: venue choice, briefing approach, oral argument strategy,
  settlement timing, and filing sequencing
- Ethics and recusal screening: conflict analysis using financial disclosures,
  appointment history, and prior career

**Does not:**

- Predict outcomes in a specific pending case (see `legalcode-case-outcome-prediction`)
- Replace actual litigation strategy from licensed counsel with local court expertise
- Substitute for reading the judge's actual opinions in analogous cases
- Provide analysis for non-US jurisdictions — use jurisdiction-specific skills for
  England & Wales, Australia, EU commercial courts, etc.
- Establish sufficient basis for a recusal motion — statistical tendencies alone do not
  satisfy 28 USC § 455

**Related skills:**

- `legalcode-case-outcome-prediction` — Probabilistic outcome modeling; consumes the
  judicial tendency assessment produced by this skill
- `legalcode-litigation-risk-assessment` — Four-dimensional risk matrix; judicial factor
  feeds into the legal merit and procedural leverage dimensions
- `legalcode-early-case-assessment` — Element-level merits analysis; use alongside this
  skill for a complete pre-filing assessment
- `legalcode-mediation-preparation` — Settlement strategy; judicial settlement pressure
  profile from this skill informs the ZOPA/BATNA timing analysis

---

## Jurisdiction and Governing Law

This skill is US-specific. It covers:

- **US federal courts**: All Article III district courts, circuit courts of appeal,
  the Supreme Court, and specialist courts (ITCJ, FISA Court) [VERIFY scope per matter]
- **US federal magistrate judges**: Where a judge has been assigned under 28 USC § 636
  for pretrial matters or has consented jurisdiction over the full case
- **US bankruptcy courts**: Where the assigned judge is a bankruptcy judge
- **US state courts**: State trial courts and appellate courts across all 50 states and
  DC; coverage depth varies by state (Trellis and Docket Alarm are strongest in CA, TX,
  NY, FL; rural county courts have thinner data)

**[JURISDICTION-SPECIFIC]** For federal courts, integrate:

- 28 USC § 455 (recusal standards based on financial interest or appearance of partiality)
- 28 USC § 144 (affidavit of personal bias procedure)
- Ethics in Government Act of 1978 (financial disclosure requirements for federal judges)
- ABA Model Code of Judicial Conduct Rules 2.9/2.11 (ex parte; disqualification)
- Court local rules and individual standing orders (available on each court's website)
- Federal Rules of Civil Procedure [FRCP] as amended through December 1, 2023 [VERIFY
  current amendment cycle]

**[JURISDICTION-SPECIFIC]** For state courts, additionally research:

- State judicial conduct code (based on ABA Model Code but often with local amendments)
- State-specific recusal statute and disclosure requirements
- Campaign finance records (for elected judges) — publicly available from state ethics
  commissions
- Judicial retention vote history (for retention-election states)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
proceeding on assumptions, the workflow pauses and asks when:

- The answer would change the depth or focus of the profile
- Multiple valid strategic approaches exist (e.g., pursue transfer vs. adapt to assigned judge)
- The judge's identity or court assignment is unclear
- The use case determines which profile sections to prioritize

Use the ⟁ CLARIFY pattern (structured options with descriptions) wherever marked below.
If the user has already provided the information, skip that question and proceed.

---

## Workflow

### Step 1: Accept the Profiling Request

Accept the judicial profiling request in any of these formats:

- **Judge name + court**: "Judge Jane Doe, SDNY" or "Hon. John Smith, N.D. Tex."
- **Case number**: Docket number from PACER or a state court e-filing system
- **Venue only**: "Compare judges in the Northern District of California for patent cases"
- **Transfer context**: "I have a motion to transfer from E.D. Tex. to N.D. Cal. — profile
  both judges"

If insufficient identifying information is provided, ask the user to supply the judge's
full name, court, and (if known) division or docket number.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user these questions. Skip any already answered:

1. **Court system**: Federal or state?
   - Options: US Federal District Court, US Circuit Court of Appeals, US Bankruptcy Court,
     State Trial Court, State Appellate Court, Multiple courts for venue comparison
   - _Why this matters_: Determines available data sources, biographical database coverage,
     and which procedural rules govern.

2. **Side and posture**: Who are you representing, and what is the current stage?
   - Options: Plaintiff / Claimant (pre-filing), Defendant (just served), Plaintiff
     (mid-discovery), Defendant (approaching trial), Both sides (neutral analysis for
     settlement), Other
   - _Why this matters_: The profile emphasis shifts — defendants weight MTD/MSJ rates
     heavily; plaintiffs weight class cert tendencies, discovery scope, and trial
     inclination.

3. **Case type and primary legal theory**:
   - Options: Patent/IP, Commercial contract, Securities/class action, Antitrust,
     Employment (individual), Employment (collective/class), Product liability, Bankruptcy,
     Regulatory/admin, Real estate/property, Criminal (rare for this skill), Other
   - _Why this matters_: Motion grant rates and judicial philosophy vary significantly
     by case type. A judge's MTD grant rate for breach of contract cases may differ
     sharply from their patent MTD rate.

4. **Primary use case for this profile**:
   - Options: Venue selection (pre-filing), Transfer motion strategy (§1404(a)), Briefing
     strategy (how to write for this judge), Oral argument preparation, Settlement timing
     (is this judge pushing parties to resolve?), Trial preparation, Full litigation plan,
     Recusal conflict screening, Other
   - _Why this matters_: Prioritizes which profile sections to lead with and what depth
     is needed in each area.

5. **Data access**:
   - Options: Full (access to Westlaw, Lex Machina, Pre/Dicta, Bloomberg Law, Trellis),
     Partial (access to some platforms), Free only (CourtListener, Google Scholar, PACER,
     judge's own website), I'll tell you what I find
   - _Why this matters_: Determines how to direct the research instructions and what
     data quality caveats to include.

If proceeding without commercial analytics access, the profile will rely on CourtListener,
PACER, Google Scholar opinions, FJC biographical directory, and Senate questionnaire
responses. State assumptions explicitly in the profile.

### Step 3: Gather Biographical and Career Intelligence

Build the biographical layer of the profile from publicly available sources. This layer
is foundational — career background correlates with measurable ruling tendencies and
frames the entire quantitative analysis.

**Sources (in order of reliability):**

| Source                                                 | Cost         | What It Provides                                                                                                      |
| ------------------------------------------------------ | ------------ | --------------------------------------------------------------------------------------------------------------------- |
| FJC Biographical Directory (fjc.gov/history/judges)    | Free         | All Article III federal judges since 1789: appointment info, appointing president, career history, service dates      |
| CourtListener Judge API (courtlistener.com)            | Free         | Education, political affiliation (with source and date range), ABA rating, financial disclosures, career positions    |
| Senate Judiciary Committee questionnaires (senate.gov) | Free         | Written philosophy statements, list of prior rulings, recusal disclosures, financial interests                        |
| Almanac of the Federal Judiciary                       | Subscription | Attorney evaluations from practitioners who appeared before the judge; biographical depth including personality notes |
| Court's own website / chambers page                    | Free         | Individual standing orders, preferred motion practice, contact information, clerk details                             |
| Google Scholar / SSRN / HeinOnline                     | Free         | Law review articles, book chapters, speeches authored by the judge                                                    |
| Westlaw / Bloomberg Law / Lexis                        | Subscription | Full career biography and evaluations                                                                                 |

**Biographical fields to compile:**

```
Full Name and Title:
Court and Division:
Date of Appointment / Date Assumed Bench:
Appointing Authority: [President / Governor / election result]
Political Affiliation: [if traceable; source it]
ABA Rating at Nomination: [Well Qualified / Qualified / Not Qualified]
Law School and Year:
Notable Law Clerk Experience (if any):
Prior Career Path:
  - Private practice (BigLaw / Boutique / Solo): [firm, dates, practice areas]
  - Government service: [AUSA / DOJ / regulatory agency / public defender / AG's office]
  - Academic: [school, subjects taught, articles authored]
  - State court: [court, dates, notable cases]
  - Other: [...]
Known Judicial Philosophy Notes:
  - Self-described (from Senate questionnaire or published writings)
  - Observed by practitioners (Almanac evaluations; [VERIFY])
Financial Disclosures: [Publicly available via CourtListener / uscourts.gov]
Prior Cases of Note: [list 2-3 most widely cited or controversial decisions]
Reversal or Notable Appellate History: [any major reversals or en banc corrections]
```

**Career background interpretation — research-backed tendencies [VERIFY individually]:**

| Prior Role                                   | Observed Tendency                                                                                                | Confidence |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------- |
| Former AUSA / federal prosecutor             | More receptive to government positions; thorough on factual records; may apply Twombly/Iqbal rigorously          | Probable   |
| Former BigLaw litigator (defense)            | Sophisticated on discovery disputes and litigation economics; may be skeptical of expansive plaintiffs' theories | Probable   |
| Former plaintiffs' counsel / public defender | More attuned to individual litigant procedural fairness; may read pro se filings generously                      | Probable   |
| Former academic / law professor              | More willing to engage complex doctrinal arguments in depth; opinions tend to be longer and more analytical      | Probable   |
| Former state court judge                     | More comfortable with docket management and scheduling strictness; efficiency-focused                            | Probable   |
| Former in-house / transactional              | May be skeptical of satellite litigation tactics; focused on business resolution                                 | Possible   |

> **[VERIFY]**: These are population-level tendencies, not predictions for any individual
> judge. Always verify against the specific judge's actual ruling record before relying on
> biographical proxies.

### Step 4: Motion Practice Analytics

Compile the judge's motion grant/denial rates by motion type. This is the quantitative
core of the profile.

**Data sources (ordered by reliability and specificity):**

1. Pre/Dicta JudicialIQ — most granular federal predictions; 85% stated accuracy [VERIFY];
   covers 10 motion types with confidence intervals
2. Lex Machina — strong for IP; good for commercial and employment; district-level and
   judge-level data
3. Westlaw Litigation Analytics / CourtAdvisor — broad federal coverage; intuitive UI
4. Bloomberg Law Litigation Analytics — federal dockets; useful for quick comparisons
5. Trellis — best available for state trial courts
6. Docket Alarm (vLex) — broadest docket coverage; searchable; integrates with Vincent AI
7. CourtListener + PACER — free; raw docket data requires manual analysis

**⟁ CLARIFY** — If you are using commercial analytics platforms, ask the user which
platforms they have access to. Tailor the data-gathering instructions accordingly. If
no commercial access exists, instruct on manual PACER/CourtListener searches.

**Motion types to compile:**

| Motion Type                             | FRCP Rule            | Why It Matters                                       |
| --------------------------------------- | -------------------- | ---------------------------------------------------- |
| Motion to Dismiss (12(b)(6))            | FRCP 12(b)(6)        | Core early-case leverage; Twombly/Iqbal threshold    |
| Motion for Summary Judgment             | FRCP 56              | Dispositive milestone; critical for defense planning |
| Motion for Class Certification          | FRCP 23              | Plaintiff class action; drives settlement leverage   |
| Motion to Compel Discovery              | FRCP 37              | Discovery scope signal; proportionality approach     |
| Daubert / Expert Challenge              | FRE 702              | Expert evidence gatekeeping; trial readiness signal  |
| Motion in Limine                        | Trial management     | Evidentiary rulings; shapes trial landscape          |
| Motion for TRO / Preliminary Injunction | FRCP 65              | Urgency leverage; four-factor analysis approach      |
| Motion for Judgment on the Pleadings    | FRCP 12(c)           | Comparable to MTD; post-answer pleading challenge    |
| Motion to Transfer Venue                | 28 USC § 1404(a)     | Transfer strategy; forum non conveniens analysis     |
| Motion to Remand                        | 28 USC § 1447        | State-to-federal removal disputes                    |
| Motion to Strike                        | FRCP 12(f) / FRCP 23 | Class action; sham affidavit doctrine                |

**Data format to compile per motion type:**

```
Motion Type: [e.g., Motion to Dismiss (12(b)(6))]
Grant Rate: [X%]
Denial Rate: [Y%]
Benchmark (District Average): [Z%]
Benchmark (National Average): [W%]
Pro-Plaintiff Lean: [Y/N — at or above district average denial rate]
Pro-Defendant Lean: [Y/N — at or above district average grant rate]
Pendency Time (days from filing to ruling): [X days avg]
Sample Size: [N rulings] — [SMALL SAMPLE WARNING if N < 20]
Data Source: [Platform name, date accessed]
Practitioner Notes: [Almanac evaluations; local bar intelligence if available]
Notable Outlier Rulings: [cite 1-2 notable opinions where the judge departed from
  typical tendency — these nuance the statistics]
```

**Directional lean summary:**

After compiling individual motion rates, calculate a directional index:

```
Directional Index:
  Motions analyzed: [N]
  Favorable to our side: [X motions where grant rate favors us]
  Unfavorable to our side: [Y motions where grant rate disfavors us]
  Neutral / within 5% of average: [Z motions]
  Overall lean: FAVORABLE / NEUTRAL / CAUTION / ADVERSE
```

**Classification definitions:**

| Classification | Meaning                                                                                                  |
| -------------- | -------------------------------------------------------------------------------------------------------- |
| **FAVORABLE**  | Judge's motion rates materially favor your side across 3+ motion types relevant to this case             |
| **NEUTRAL**    | Rates within ±5% of district averages on most motion types; no material directional lean                 |
| **CAUTION**    | Rates modestly disfavor your side on 1-2 key motion types; manageable with briefing strategy             |
| **ADVERSE**    | Rates materially disfavor your side on 3+ motion types relevant to this case; consider transfer analysis |

> **Sample size discipline**: Do not produce a directional classification where the
> relevant motion types each have fewer than 10 rulings. Mark the result [LOW CONFIDENCE
>
> > — SMALL SAMPLE] and recommend local practitioner intelligence as supplement.

### Step 5: Case Management and Scheduling Profile

Compile the judge's case management tendencies — how strictly they manage the docket,
how they conduct scheduling conferences, and how they approach discovery disputes.

**Sources**: Judge's court page (standing orders), PACER docket entries in prior cases,
Almanac evaluations, Trellis "Milestones" and "At a Glance" tabs for state courts.

**Fields to compile:**

**Scheduling and Docket Management:**

```
Average Case Duration (filing to termination): [X months]
  Benchmark (district average): [Y months]
  Relative speed: FAST / AVERAGE / SLOW
Average Time to Trial (filing to first trial date): [X months]
Average Time to Ruling on Motions (days from submission): [X days]
  Breakdown by motion type if available
Extension Grant Rate: [HIGH / MODERATE / LOW — qualitative from practitioner sources]
Rule 16 Strictness: [Does the judge enforce scheduling orders strictly?]
CMC / Scheduling Conference Style: [Letter-based / in-person / telephonic /
  videoconference; level of judicial involvement in setting discovery scope]
```

**Individual Rules and Standing Orders** (read the judge's standing orders directly):

```
Brief Page Limits: [per motion type — often stricter than default local rules]
Pre-Motion Conference Requirement: [letter brief required before filing certain motions?]
Discovery Dispute Procedure: [letter briefs vs. full briefing vs. telephone call]
Interrogatory Limits: [same as FRCP 25, or modified?]
Deposition Hour Limits: [same as FRCP, or modified?]
Expert Disclosure Timing: [same as FRCP, or modified?]
ESI / Proportionality Stance: [active involvement in ESI disputes vs. hands-off?]
Proposed Scheduling Order Template: [does the court require a specific format?]
Jury Trial vs. Bench Trial Preference: [does the judge express a preference?]
```

**Discovery Management Style:**

```
Discovery Scope: EXPANSIVE / BALANCED / RESTRICTIVE
  (Does the judge tend to grant motions to compel? Does the judge limit broad
   discovery requests on proportionality grounds?)
Proportionality Enforcement: [Active — invokes FRCP 26(b)(1) proportionality factors
  frequently; or Passive — largely defers to party agreements]
Magistrate Referral Practice: [Does the judge refer discovery disputes to a magistrate
  judge, or handle personally?]
Spoliation and Sanctions Approach: [How aggressively does the judge sanction discovery
  misconduct under FRCP 37(e) and inherent authority?]
ESI-Specific Notes: [special ESI protocol required? Preferred e-discovery vendors?]
```

### Step 6: Trial Management Profile

Compile how the judge manages trials — critical for trial preparation strategy and for
assessing whether pre-trial settlement pressure is likely to succeed.

**Sources**: PACER trial transcripts (where available), Almanac evaluations, local bar
intelligence, prior voir dire transcripts (CourtListener audio for appellate, PACER for
district).

**Fields to compile:**

```
Jury Trial Frequency: [% of cases reaching jury trial; district/state average for context]
Bench Trial Rate: [% of non-jury trials; bench trial win rate for plaintiff/defendant]
Average Trial Length (days): [district average for comparison]

Voir Dire Approach:
  Conducted by: [Judge-led / Attorney-led / Hybrid]
  Scope: [Brief / Moderate / Extensive]
  Strike for cause threshold: [Strict / Liberal]
  Notable customs: [...]

Evidentiary Ruling Patterns:
  Daubert grant rate (from Step 4 data): [X%]
  MIL grant rate (overall): [X%]
  MIL patterns by category: [Prior bad acts — HIGH/LOW grant rate;
    Expert MILs — HIGH/LOW; Hearsay MILs — HIGH/LOW; 404(b) character evidence]
  Hearsay rulings: [Strict / Moderate / Liberal interpretation]
  FRE 403 balancing: [Does the judge exclude more on prejudice grounds than peers?]

Jury Instructions:
  Pattern instructions preference: [Prefers circuit pattern / open to party proposals /
    requires justification for deviations]
  Verdict form: [General / Special / General with interrogatories — and judge's default]

Oral Argument Practice (for motions):
  Grant rate for oral argument requests: [HIGH / MODERATE / LOW / RARELY GRANTS]
  Hot bench: [YES — active questioning; NO — cold bench; MIXED]
  Format preference: [Time-allocated round / conversational / questions from opening]
  Notable style: [Record-bound vs. hypotheticals; policy-receptive vs. text-focused]

Sanctions and Contempt:
  Willingness to sanction conduct: [HIGH / MODERATE / LOW]
  Notable sanctions orders: [cite if relevant]
```

### Step 7: Reversal Rate and Appellate Posture

Analyze how the judge's rulings have fared on appeal. This informs both the probability
of preserving trial court wins and the strategic value of litigating aggressively to
generate a strong record.

**Sources**: Westlaw Litigation Analytics (Judicial Reversal report), Bloomberg Law,
Pre/Dicta appellate forecasting (launched August 2025), CourtListener citation network.

**Fields to compile:**

```
Reviewing Circuit: [e.g., Fifth Circuit, Ninth Circuit]
Overall Reversal Rate: [X%]
  Benchmark (district average): [Y%]
  Benchmark (circuit average): [Z%]
  Relative standing: LOWER THAN AVERAGE / AVERAGE / HIGHER THAN AVERAGE

Reversal Rate by Case Type:
  [Case type 1 — X% reversal; n = Y rulings]
  [Case type 2 — X% reversal; n = Y rulings]
  [...]

Issue-Specific Reversal Patterns:
  [e.g., Daubert exclusions reversed at X% — above/below average]
  [e.g., MSJ grants reversed at X% — above/below average]
  [e.g., Class cert denials reversed at X% — above/below average]
  [Note any issue type where the judge is notably more or less affirmed than peers]

Circuit Relationship:
  [Is the circuit generally deferential to this district judge?]
  [Any notable circuit court corrections involving this judge?]
  [En banc or SCOTUS reversals: list if any]

Strategic Implication:
  [LOW REVERSAL RATE]: Rulings likely to stand; aggressive early dispositive motion
    strategy may succeed or fail decisively — little uncertainty about where the case ends
  [AVERAGE REVERSAL RATE]: Normal appellate risk calculus
  [HIGH REVERSAL RATE]: Rulings are less durable; appeals are more viable;
    trial court wins may be pyrrhic if the reversal rate in the relevant issue area is high
```

### Step 8: Judicial Philosophy and Notable Opinions

Compile the judge's jurisprudential worldview — how they approach statutory interpretation,
their treatment of precedent, and their doctrinal anchors in the relevant legal area.

**Sources**: Senate questionnaire responses, law review articles authored by the judge,
publicly reported speeches, Ravel View citation analytics (Lexis), Westlaw Litigation
Analytics citation patterns, direct reading of key opinions.

**Fields to compile:**

```
Statutory Interpretation Approach:
  Primary method: [Textualist / Purposivist / Pragmatist / Mixed]
  Evidence: [cite Senate questionnaire, speech, or key opinion]

Precedent Treatment:
  SCOTUS adherence: [Strict / Moderate / Occasionally distinguishes aggressively]
  Circuit precedent: [Follows circuit strictly / occasionally pushes at edges]
  Willingness to certify difficult questions for circuit review: [Y/N]

Legislative History Use:
  [Does the judge consult legislative history where text is ambiguous?]
  [Or does the judge refuse legislative history on textualist grounds?]
  Evidence: [cite at least one opinion]

Doctrinal Anchors in [Relevant Case Type]:
  Key precedents the judge relies on: [top 3-5, from citation analysis or direct reading]
  Doctrinal preferences: [Does the judge prefer bright-line tests? Balancing tests?
    Multi-factor standards? Structural constitutional arguments?]

Published Scholarship / Speeches:
  [List law review articles, book chapters, speeches with titles and dates]
  [Summarize any views directly relevant to the case type]
  [Note: citing a judge's own scholarship in a brief is generally a favorable signal
   if the argument is consistent with the judge's expressed views]

Senate Questionnaire Highlights:
  [Summarize any philosophy statements from the questionnaire that are relevant
   to the case type — e.g., views on class actions, expert evidence, regulatory deference]
  [Source: senate.gov/judiciary; CourtListener API]

Notable Opinions in Relevant Area:
  [Cite 3-5 of the judge's most important or widely cited opinions in the relevant
   case type. For each: citation, brief holding, strategic implication for this case]
```

### Step 9: Settlement Pressure Profile

Assess how the judge manages settlement — whether the judge actively pushes parties to
resolve, and if so, when and how.

**Sources**: Local rules and standing orders, Trellis "Milestones" data (average time to
first dismissal order), Almanac attorney evaluations, PACER docket review in comparable
prior cases.

**Fields to compile:**

```
Mandatory Settlement Conference:
  Required: [Y/N]
  Timing: [Early (within 6 months of filing) / Mid-case (post-discovery) / Pre-trial]
  Conducted by: [Judge personally / Referred to magistrate judge / Private mediator]
  Style: [Evaluative (judge gives candid views) / Facilitative (judge moderates only) /
    Mixed (evaluative if parties stuck)]

Settlement Conference Style (if handled personally):
  Caucus format: [Shuttles between parties individually? Joint sessions?]
  Judge's directness: [Will the judge express views on case merits? Or stay neutral?]
  Pressure tactics: [Does the judge apply direct settlement pressure, e.g.,
    "I'm sending this to trial in 90 days"?]
  Practitioner reputation: [cite Almanac evaluations or local bar intelligence if known]

Case Resolution Rate:
  % of filed cases settling or resolving before trial: [X%]
  Average time to first dispositive ruling: [X months from filing — Trellis data]
  Resolution trajectory: [Cases before this judge tend to resolve
    EARLY (pre-MTD) / AT MTD / POST-DISCOVERY / PRE-TRIAL / AT/AFTER TRIAL]

Settlement Timing Strategic Notes:
  [If the judge applies early settlement pressure, pre-filing settlement leverage
   may be lower — opposing party may be willing to wait for the judge to weigh in]
  [If the judge's MSJ grant rate is low for defendants, defense settlement leverage
   increases at the MTD stage — window closes at MSJ]
  [If the judge has a fast track to trial, urgency of settlement is higher for
   risk-averse defendants or plaintiffs with thin damages cases]
```

### Step 10: Conflict and Recusal Screening

Run a basic conflict screening to identify potential recusal issues under 28 USC § 455.

**Sources**: CourtListener financial disclosure API, FJC directory, uscourts.gov
financial disclosure database, Senate questionnaire prior representation disclosures.

**⟁ CLARIFY** — Ask the user to provide:

- Names of all parties and their corporate parents / affiliates
- Names of outside counsel firms on both sides
- Any known former law firms or clients of the judge
- Any publicly known financial holdings of the judge (e.g., stock in a public company
  that is a party)

**Screening checklist:**

```
§ 455(a) — Impartiality question:
  [ ] Judge has a financial interest in any party or affiliate [VERIFY via disclosure]
  [ ] Judge or immediate family member has been involved in the matter as counsel,
      witness, or party [check FJC directory]
  [ ] Judge has publicly expressed views that predetermine the outcome [check speeches,
      law review articles for direct statements on the facts at issue]

§ 455(b) — Specific grounds:
  [ ] Personal bias or prejudice [requires specific facts — statistics do not suffice]
  [ ] Prior service as a material witness
  [ ] Prior service as a lawyer in the proceeding
  [ ] Prior interest as private practitioner or government lawyer in the matter
  [ ] Financial interest in subject matter of the proceeding
  [ ] Party relative relationship (spouse, child, parent, or their spouses —
      within third degree)

Ethics Rules:
  [ ] ABA Model Code Rule 2.11 — substantially parallels § 455
  [ ] Court local conflict screening requirements (some courts require parties to
      submit conflict disclosure forms at case opening)

Result:
  NO APPARENT CONFLICT — profile is clear for standard case management
  FLAG FOR COUNSEL REVIEW — one or more items warrant investigation by licensed
    counsel before deciding whether to file a recusal motion
  RECUSAL MOTION WARRANTED — specific articulable conflict under § 455
    (note: statistical tendencies alone do NOT meet this standard)
```

> **CRITICAL**: A statistical lean (e.g., "this judge grants MTDs 70% of the time for
> defendants") is preparation intelligence, not bias. It does not constitute grounds for
> recusal under § 455. Recusal requires a specific, articulable conflict — financial
> interest, prior representation, personal relationship, or similar. Do not use this
> profile to support a recusal motion unless a concrete legal basis exists.

### Step 11: Strategic Recommendations

Synthesize the profile into actionable strategic recommendations by use case.

**⟁ CLARIFY** — Ask the user which use case recommendations to prioritize. Generate
all applicable sections below, but lead with the sections most relevant to the user's
stated objective from Step 2.

#### 11a. Venue Selection and Transfer Strategy

```
Pre-filing Venue Analysis (if filing has not yet occurred):
  [Assess whether this judge is favorable, neutral, or adverse for this case type]
  [Compare to other judges in the same district who might be randomly assigned]
  [Assess whether the district as a whole (local rules, appellate climate, jury pool)
   is favorable — separate from the individual judge]

Transfer Motion Analysis (if already filed, 28 USC § 1404(a)):
  For Transfer (if current judge is adverse):
    Private interest factors: [party locations, witness locations, document locations]
    Public interest factors: [court congestion data, local interest, familiarity with law]
    Best destination: [identify the most favorable alternative venue with comparable
      motion rates and judicial philosophy — use Pre/Dicta Venue Strategist if available]

  Against Transfer (if current judge is favorable):
    Arguments to emphasize in opposition to a transfer motion filed by opposing party
    [Court congestion: is the current court less congested?]
    [Local interest: is there a genuine local connection that weighs against transfer?]

Practical note: Venue selection based on judicial analytics is standard and permissible
practice. Avoid overstating statistical tendencies in any transfer motion papers —
present the traditional § 1404(a) factors, not a statistics-based argument.
```

#### 11b. Briefing Strategy

```
Brief Architecture:
  [ ] Lead with [textualist / purposivist / pragmatic] framing based on judge's
      stated interpretive approach
  [ ] Cite judge's own opinions in the relevant area as anchor precedents where
      they support your position
  [ ] If judge has authored law review articles directly relevant to the legal
      issue, cite them prominently where consistent with your argument
  [ ] Comply with page limits in individual standing orders — check before filing
  [ ] Comply with pre-motion conference requirements if applicable
  [ ] Minimize footnotes if judge's standing orders or practitioner notes suggest
      the judge disfavors footnote-heavy briefs

Citation Strategy:
  [ ] Pull top-cited precedents from Ravel View or Westlaw citation analytics
      for this judge — lead with those cases if they support your position
  [ ] If the judge cites a specific circuit precedent heavily, frame your argument
      within that precedent's structure rather than arguing around it

Style Notes:
  [ ] [Hot bench note if oral argument likely]: anticipate top 2-3 concerns from
      prior opinions and address preemptively in opening paragraph of brief
  [ ] [Cold bench note]: make the brief self-contained and persuasive without
      expecting deep questions from the bench
```

#### 11c. Oral Argument Preparation

```
Determine likelihood of oral argument:
  [Based on Step 4 oral argument grant rate — is this motion type heard or ruled
   on the papers?]
  [If grant rate is LOW: tailor the brief for a judge who will rule without
   argument; front-load the strongest arguments]

If oral argument is likely:
  Hot bench preparation:
    [ ] Identify 3 hardest questions based on prior opinions in the legal area
    [ ] Address each proactively in opening remarks
    [ ] Prepare concise, direct answers — this judge wants exchanges, not speeches
    [ ] Bring record cites for every factual statement

  Cold bench preparation:
    [ ] Prepare a standalone argument structure that persuades without knowing
        the judge's concerns
    [ ] Open with the one-sentence bottom line: what do you want and why
    [ ] Use the limited time to reinforce the brief's strongest arguments

  Time management:
    [ ] Determine judge's time allocation practice from standing orders
    [ ] Reserve appropriate rebuttal time if representing moving party
    [ ] Comply strictly with time limits — this judge [does / does not] cut off
        counsel mid-sentence per Almanac practitioner notes [VERIFY]
```

#### 11d. Settlement Timing

```
Settlement windows based on judicial profile:
  [Based on Step 9 data]

  If judge applies early settlement pressure:
    [ ] Settlement conversation should begin before or immediately after filing;
        plaintiff leverage is highest before the judge can weigh in on merits
    [ ] If defendant, use the settlement conference as an opportunity for the judge
        to hear weaknesses in plaintiff's case

  If judge rarely grants MTDs (low grant rate):
    [ ] Defense settlement leverage is materially lower post-filing
    [ ] Consider whether pre-suit settlement is worth pursuing more aggressively

  If judge has a fast path to trial:
    [ ] Calendar risk arrives quickly; defendants with significant damages exposure
        should price in trial risk early
    [ ] Plaintiffs with a strong case may benefit from rejecting early lowball offers

  Optimal settlement window: [Based on average time to first dispositive ruling
    from Trellis/Step 9 data — identify the window before the court's natural
    case triage occurs]
```

---

## Severity Classification System

Use this classification for each profile element to signal strategic impact:

| Classification | Symbol | Meaning                                                                                                                       |
| -------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------- |
| **FAVORABLE**  | ✅     | This element materially helps your side — motion rates, philosophy, or tendencies align with your position                    |
| **NEUTRAL**    | ⚪     | This element is within normal ranges; no material strategic advantage or disadvantage                                         |
| **CAUTION**    | ⚠️     | This element modestly disfavors your side or requires specific strategic adaptation                                           |
| **ADVERSE**    | 🔴     | This element materially disfavors your side and should factor into venue, settlement, or briefing strategy decisions          |
| **UNVERIFIED** | 🔷     | This element is based on limited data, small sample sizes, or unverified practitioner intelligence; treat as directional only |

Apply these classifications to:

- Each motion type rate (from Step 4)
- Overall directional lean
- Case management speed
- Trial inclination
- Settlement pressure tendency
- Reversal rate
- Jurisprudential alignment

---

## Prioritization Framework

After completing all profile steps, organize findings into three tiers for the
strategic action plan:

| Tier                                 | Criteria                                                                                                                        | Action                                                                      |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Tier 1 — Immediate**               | ADVERSE findings on motion types central to this case; recusal flags; individual rule violations that could result in sanctions | Address before any filing; raise with supervising counsel immediately       |
| **Tier 2 — Briefing & Strategy**     | CAUTION findings that require briefing adaptation; oral argument preparation notes; settlement window analysis                  | Incorporate into case planning before the next filing deadline              |
| **Tier 3 — Background Intelligence** | NEUTRAL or FAVORABLE findings; biographical intelligence; philosophy notes for long-term relationship building                  | Maintain as reference; consult at decision points throughout case lifecycle |

---

## Citation Quality Gates

Run these five gates silently before delivering any profile element. If any gate fails,
revise before delivering.

| Gate           | Rule                                                                                                                                       | Fail Action                                                                    |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| **Source**     | Every statistical claim cites a specific platform, database, or published source                                                           | Add source or mark "[UNVERIFIED — practitioner intelligence only]"             |
| **Format**     | All citations to cases follow Bluebook or the applicable court's citation format                                                           | Fix format                                                                     |
| **Currency**   | Every standing order, rule reference, and data point checked against the current version                                                   | Flag "[CHECK CURRENCY — standing orders and analytics data change frequently]" |
| **Domain**     | Analysis stays within the judge's actual jurisdiction and case type; do not apply one judge's tendencies to a different court or case type | Remove or flag scope error                                                     |
| **Confidence** | Uncertainty is explicitly stated, especially for small sample sizes, state court data gaps, and practitioner intelligence                  | Add confidence qualifier and [SMALL SAMPLE] warning                            |

---

## Self-Interrogation for ADVERSE Classifications

For any element classified as ADVERSE (🔴), apply this 3-pass review before including it
in the final profile:

**Pass 1 — Data Integrity**: Is the ADVERSE classification based on sufficient data
(N ≥ 20 for motion rates)? Is the data from a reliable, current source? Could the result
be an artifact of a specific case type, time period, or data gap rather than a genuine
tendency?

**Pass 2 — Completeness**: Are there countervailing data points that soften the ADVERSE
classification? Has the judge's tendency shifted in recent years? Does the judge's
philosophy in the relevant legal area cut against what the raw motion rates suggest?

**Pass 3 — Challenge**: What is the strongest argument that this ADVERSE classification
is overstated? What would a practitioner with extensive experience before this judge say
about this tendency? Has the Almanac been updated to reflect a different characterization?

---

## Confidence Scoring

| Level        | Range     | Meaning                                      | Application to Judge Profiles                                                                  |
| ------------ | --------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Verified data from multiple reliable sources | Motion rates with N ≥ 50 from 2+ commercial platforms; biographical facts from FJC directory   |
| **High**     | 0.80–0.94 | Strong single-source data; minor questions   | Motion rates with N ≥ 20 from one commercial platform; standing orders directly read           |
| **Probable** | 0.60–0.79 | Good basis; some uncertainty                 | Motion rates with N 10–19; practitioner intelligence from Almanac evaluations                  |
| **Possible** | 0.40–0.59 | Genuinely uncertain                          | Small sample sizes (N < 10); state court data with limited coverage; secondhand intelligence   |
| **Unlikely** | 0.0–0.39  | Speculative                                  | Biographical correlations applied without any specific ruling data; hearsay practitioner notes |

Annotate each profile section with its confidence level. Do not present LOW-confidence
elements without flagging them explicitly.

---

## Glass Box Audit Trail

Complete this template at the end of every profile:

```yaml
glass_box:
  skill_name: "legalcode-judge-profile"
  judge_name: "[Full name and title]"
  court: "[Court name and division]"
  case_type: "[Primary case type analyzed]"
  side: "[Plaintiff / Defendant / Neutral]"
  use_case: "[Venue selection / Briefing / Oral argument / Settlement / Full plan]"
  profile_date: "[YYYY-MM-DD]"

  data_sources_used:
    fjc_biographical_directory: "[Accessed / Not accessed]"
    courtlistener_judge_api: "[Accessed / Not accessed]"
    senate_questionnaire: "[Accessed / Not accessed]"
    almanac_federal_judiciary: "[Available / Not available — subscription required]"
    westlaw_litigation_analytics: "[Accessed / Not accessed]"
    bloomberg_law: "[Accessed / Not accessed]"
    lex_machina: "[Accessed / Not accessed]"
    pre_dicta: "[Accessed / Not accessed]"
    trellis: "[Accessed / Not accessed — state courts only]"
    docket_alarm: "[Accessed / Not accessed]"
    pacer_direct: "[Accessed / Not accessed]"
    google_scholar: "[Accessed / Not accessed]"
    standing_orders_read: "[Yes — [URL] / No]"
    legalcode_mcp: "[Connected / Not connected]"

  motions_profiled: "[N motion types with data]"
  average_sample_size: "[X rulings per motion type]"
  low_sample_warnings: "[N motion types flagged as LOW CONFIDENCE due to sample size]"

  overall_directional_lean: "[FAVORABLE / NEUTRAL / CAUTION / ADVERSE]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"

  limitations:
    - "[Small sample size for key motion types if applicable]"
    - "[State court data gap if applicable]"
    - "[No commercial analytics access if applicable]"
    - "[Almanac evaluations not accessed if applicable]"
    - "[Profile based on data through [date] — verify standing orders for currency]"

  recusal_screened: "[Yes / No]"
  conflict_flags: "[None / Flagged — see Step 10]"

  reviewer: "AI-assisted — requires qualified legal review before relying on any
    element for actual litigation strategy"
```

---

## Anti-Patterns

What NOT to do when building and using judicial profiles:

1. **Over-relying on aggregate statistics without context** — A 60% MTD grant rate is
   meaningless without knowing the case type, time period, and bench composition.
   Always segment by the motion type and case category most relevant to your matter.

2. **Small sample size fallacy** — Treating 5 MSJ rulings as a reliable grant rate.
   The profile must flag [SMALL SAMPLE] for any motion type with fewer than 20 rulings
   and explicitly warn the user to supplement with practitioner intelligence.

3. **Ignoring standing orders** — Practitioners who violate a judge's individual rules
   (page limits, pre-motion conference requirements, discovery dispute procedures) create
   an immediately negative impression before the substance of their argument is even
   considered. Read standing orders before filing anything.

4. **Confusing district average for judge-specific data** — Many practitioners see a
   district-level statistic and apply it to the assigned judge. Individual judges in the
   same district often deviate significantly from the district average. Use judge-level
   data wherever possible.

5. **Treating analytics as a substitute for reading opinions** — Statistics identify
   patterns; the judge's actual opinions reveal the reasoning, the doctrinal framework,
   and what quality of argument the judge finds persuasive. Build the profile from data
   AND direct opinion reading.

6. **Using stale profile data** — A judge's tendencies from 5+ years ago may not reflect
   current approach. Weight recent rulings more heavily. Check for circuit precedent
   changes that may have altered the judge's legal landscape since earlier data was
   gathered. Verify standing orders are current.

7. **Over-interpreting biographical correlations** — Career background tendencies are
   population-level observations. Individual judges deviate substantially from group
   averages. Never substitute a biographical proxy for analysis of the judge's actual
   ruling record.

8. **Using judicial profiles for unsupported recusal motions** — Statistical tendencies
   do not establish bias under 28 USC § 455. Filing a recusal motion based solely on
   motion rates risks irritating the judge and damaging the client relationship with the
   court for the duration of the case. Recusal requires specific, articulable conflicts.

9. **Judge shopping that backfires** — Aggressive venue selection or transfer motions
   grounded primarily in analytics (rather than legally cognizable § 1404(a) factors)
   can harm the client if the motion fails and the judge is now aware of the tactic.
   Present traditional § 1404(a) factors; let analytics inform the decision internally.

10. **Missing the soft intelligence layer** — Quantitative analytics capture observable
    patterns but miss courthouse culture, clerk preferences, and informal reputation
    intelligence that only local counsel and veteran practitioners possess. The Almanac's
    attorney evaluations provide partial coverage; always supplement with local bar
    relationships for high-stakes matters.

11. **Failing to read the judge's own opinions in the relevant area** — Citation analytics
    and motion rates are inputs; the opinions themselves are the authoritative source.
    Before finalizing any strategic recommendation, read at least 3–5 of the judge's own
    opinions in the case type at issue.

12. **Applying federal judge analytics to a state court judge** — Federal and state court
    data sources, docket structures, and even the judicial role differ substantially.
    Do not use federal-court analytics tools for state court judges or vice versa.

13. **Ignoring the reviewer circuit's tendencies** — A judge with a high reversal rate may
    be a weaker trial court win for a defendant who needs durability on appeal. Factor in
    the circuit's own tendencies when assessing how valuable a trial court victory would
    actually be.

14. **Misattributing orders** — Analytics tools attribute rulings to the judge who signed
    the order, but magistrate-recommended reports and orders adopted by the district judge
    reflect the magistrate's analysis. Verify which judge actually analyzed the legal
    issue before attributing a tendency.

15. **Skipping the conflict screen** — Even a brief conflict check (party names against
    financial disclosure database) is valuable pre-filing diligence. Discovering a
    recusal issue mid-case is more disruptive than catching it pre-filing.

16. **Ignoring political affiliation context** — Appointing president and political
    affiliation are relevant background but should never be used as a proxy for
    predicting individual rulings. Use only as supplemental context; never as a primary
    analytical driver.

17. **Failing to update the profile when the judge's standing orders change** — Judges
    update individual standing orders periodically. A page limit violated because the
    attorney was relying on a 12-month-old version of the standing orders is not an
    acceptable error.

---

## Writing Standards

Apply these standards before delivering any judicial profile output:

1. **Specificity over generality**: Every tendency claim must cite a source. "Grant rate:
   68%, N = 45 rulings, source: Westlaw Litigation Analytics (accessed 2026-03-21)" is
   correct. "This judge frequently grants motions to dismiss" is not.

2. **Confidence annotation discipline**: Every section that relies on practitioner
   intelligence, small sample data, or biographical proxies must be annotated with its
   confidence level. Never present LOW-confidence findings without explicit qualification.

3. **Sample size transparency**: State the number of rulings underlying every motion
   rate. Flag [SMALL SAMPLE] for N < 20. Do not calculate a directional index from
   motion types with insufficient data.

4. **No outcome prediction**: The profile describes historical tendencies and strategic
   preparation levers. It does not predict how this judge will rule on this specific
   motion. Every recommendation section should include a statement to this effect.

5. **Actionability**: Every ADVERSE or CAUTION finding must be paired with a concrete
   strategic response — what to do differently because of this finding.

6. **Currency check**: Note the date every standing order was accessed. Note the date
   range of the analytics data. Flag any element that is more than 12 months old.

7. **Ethics compliance note**: Include a note in the output reminding the user that passive
   research (reading public docket data, opinions, and analytics) is permissible and is
   standard due diligence. Ex parte communication with the presiding judge during a
   pending matter is prohibited by ABA Model Rule 3.5(b).

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as a supplementary legal research
tool for jurisdiction-specific motion standards, statutory authority, and circuit
precedent context.

**With legalcode-mcp connected (preferred):**

- In Step 8, search for circuit-level precedents the judge has cited in opinions in the
  relevant case type — verify citation accuracy before including in the profile
- Search for any statutory changes or circuit en banc decisions that may have altered the
  judge's legal landscape since the analytics data was gathered
- Save verified legal authority to `/tmp/legalcode-judge-profile-research.md`
- Mark legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp connected:**

- Proceed with web research (WebSearch, WebFetch) for opinion research and legal authority
- Mark any legal authority references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Supplement with Google Scholar for opinion research

**For analytics data access:**

- When the user has access to commercial platforms (Westlaw, Lex Machina, Pre/Dicta,
  Trellis), provide targeted search queries to run within those platforms
- When access is limited to free tools, provide instructions for manual PACER/CourtListener
  docket analysis and Google Scholar opinion search
- Always include data source and access date in every statistics citation

---

## Localization Notes

**Federal vs. State Courts:**

- Federal court profiling: Full complement of FJC biographical directory, Senate
  questionnaire, CourtListener API, PACER, and commercial analytics platforms available.
  Strongest data quality.
- State trial courts: Trellis is the primary aggregator; coverage is strongest in CA, TX,
  NY, FL and weakens in smaller states and rural counties. Supplement heavily with
  Almanac evaluations and local practitioner intelligence.
- State appellate courts: Limited analytics; rely primarily on opinion analysis, Almanac,
  and state bar resources.

**Specialist Courts:**

- **Bankruptcy courts**: Most analytics platforms have some bankruptcy coverage; Lex
  Machina covers PTAB extensively for patent disputes; treat bankruptcy judges like
  district judges for biographical purposes.
- **International Trade Commission (ITC) ALJs**: USITC maintains its own proceedings;
  consult USITC docket for judge assignment analytics; treat similarly to administrative
  law judge profiling.
- **PTAB / TTAB**: Lex Machina covers PTAB institution rates and TTAB outcomes
  comprehensively; use for patent and trademark inter partes review strategy.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis combining web-backed research via
multi-platform analysis of US judicial analytics practice (Westlaw Litigation Analytics,
Bloomberg Law, Lex Machina, Pre/Dicta, Trellis, Docket Alarm, CourtListener), FJC
biographical database conventions, ABA Litigation Section guidance on judicial analytics
tools, ABA Model Rules of Professional Conduct (Rules 1.1, 3.5, 8.4), 28 USC §§ 455/144
recusal framework, and practitioner resources including the Almanac of the Federal
Judiciary. Research sources include: ABA Journal judicial analytics coverage; Colorado
Lawyer litigation analytics guide; Trellis support documentation (judge analytics tabs);
Pre/Dicta platform documentation (JudicialIQ, Venue Strategist, Comparative Predictions);
Docket Alarm/vLex documentation; CourtListener Judge API documentation; FJC Biographical
Directory about page; France judicial analytics ban (Artificial Lawyer, ABA Journal, 2019,
Art. 33 Justice Reform Act — for comparative ethics context); Harvard Law School Center
on the Legal Profession "Data in the Court"; Boston College Law Review hot bench research;
Loyola Law Library analytics guide; AskLexi federal judge research guide.

---

## Output Format Template

Deliver the completed profile using this template:

```markdown
# Judicial Profile: [Judge Full Name]

## [Court Name] | [Division if applicable]

_Profile prepared: [YYYY-MM-DD] | Data as of: [date range] | Case type: [type]_
_Side: [Plaintiff / Defendant / Neutral] | Use case: [primary use case]_

---

## EXECUTIVE SUMMARY

**Overall Strategic Assessment**: [FAVORABLE / NEUTRAL / CAUTION / ADVERSE]

| Dimension                 | Classification | Key Finding                          |
| ------------------------- | -------------- | ------------------------------------ |
| Motion Practice (MTD)     | [✅/⚪/⚠️/🔴]  | Grant rate: X% (district avg: Y%)    |
| Motion Practice (MSJ)     | [✅/⚪/⚠️/🔴]  | Grant rate: X% (district avg: Y%)    |
| Case Management Speed     | [✅/⚪/⚠️/🔴]  | Avg case duration: X months (avg: Y) |
| Discovery Approach        | [✅/⚪/⚠️/🔴]  | [Expansive / Balanced / Restrictive] |
| Settlement Pressure       | [✅/⚪/⚠️/🔴]  | [Description]                        |
| Reversal Rate             | [✅/⚪/⚠️/🔴]  | X% (district avg: Y%)                |
| Trial Inclination         | [✅/⚪/⚠️/🔴]  | [Description]                        |
| Jurisprudential Alignment | [✅/⚪/⚠️/🔴]  | [Description]                        |

**Top 3 Strategic Actions (Tier 1 — Immediate):**

1. [Action 1]
2. [Action 2]
3. [Action 3]

---

## 1. BIOGRAPHICAL PROFILE

[Full biographical fields from Step 3]

---

## 2. MOTION PRACTICE ANALYTICS

[Table of motion types with grant rates, benchmarks, and directional classifications]

**Directional Index**: [FAVORABLE / NEUTRAL / CAUTION / ADVERSE]
_Based on [N] motion types analyzed. Confidence: [level]_

---

## 3. CASE MANAGEMENT AND SCHEDULING PROFILE

[Fields from Step 5, including standing orders summary]

---

## 4. TRIAL MANAGEMENT PROFILE

[Fields from Step 6]

---

## 5. REVERSAL RATE AND APPELLATE POSTURE

[Fields from Step 7]

---

## 6. JUDICIAL PHILOSOPHY AND NOTABLE OPINIONS

[Fields from Step 8, including top 3-5 opinions in the case type]

---

## 7. SETTLEMENT PRESSURE PROFILE

[Fields from Step 9]

---

## 8. CONFLICT AND RECUSAL SCREEN

[Checklist from Step 10 with result classification]

---

## 9. STRATEGIC RECOMMENDATIONS

### Venue / Transfer

[From Step 11a]

### Briefing Strategy

[From Step 11b]

### Oral Argument

[From Step 11c]

### Settlement Timing

[From Step 11d]

---

## 10. PRIORITIZED ACTION PLAN

### Tier 1 — Immediate (before next filing)

- [Action 1 — addresses ADVERSE/FLAG finding]
- [Action 2]
- [...]

### Tier 2 — Briefing and Strategy Cycle

- [Action 1 — addresses CAUTION finding]
- [Action 2]
- [...]

### Tier 3 — Background Intelligence

- [Item 1 — biographical / philosophy reference]
- [Item 2]
- [...]

---

## 11. DATA QUALITY AND CONFIDENCE SUMMARY

| Section              | Confidence                                 | Sample Size             | Notes                        |
| -------------------- | ------------------------------------------ | ----------------------- | ---------------------------- |
| Biographical profile | [Definite/High/Probable/Possible/Unlikely] | N/A — FJC/CourtListener | [Notes]                      |
| MTD rate             | [level]                                    | N = [X] rulings         | [SMALL SAMPLE if applicable] |
| MSJ rate             | [level]                                    | N = [X] rulings         | [Notes]                      |
| [Other motion types] | [...]                                      | [...]                   | [...]                        |
| Reversal rate        | [level]                                    | N = [X] reversals       | [Notes]                      |
| Judicial philosophy  | [level]                                    | [N opinions read]       | [Notes]                      |

---

## 12. GLASS BOX AUDIT TRAIL

[Complete YAML from the Glass Box section]

---

_Ethics note: This profile is based entirely on publicly available information and
commercial analytics tools. The research methodology — reading public docket data,
published opinions, biographical databases, and analytics platforms — is standard legal
due diligence and does not constitute improper ex parte contact under ABA Model Rule 3.5.
This profile should not be used as the basis for a recusal motion under 28 USC § 455
unless a specific, articulable conflict exists beyond statistical tendencies._
```
