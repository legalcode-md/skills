---
name: legalcode-venture-financing-fr
description: French venture financing suite covering BSPCE (Art. 163 bis G CGI; 2025 Finance Law reform),
  BSA (Bons de Souscription d'Actions), SAS structural flexibility (actions de préférence L228-11 to L228-19;
  pacte d'associés), AMF private placement rules (Art. L411-2 CMF; less than 150 investors; qualified
  investor exemption), obligations convertibles (OC/OCABSA/BSAR; Arts. L228-91–L228-106 Code de Commerce),
  and French Tech ecosystem instruments (BPI France; Tibi initiative; French Tech Visa).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

French venture financing suite covering BSPCE (Art. 163 bis G CGI; 2025 Finance Law reform), BSA (Bons de Souscription d'Actions), SAS structural flexibility (actions de préférence L228-11 to L228-19; pacte d'associés), AMF private placement rules (Art. L411-2 CMF; <150 investors; qualified investor exemption), obligations convertibles (OC/OCABSA/BSAR; Arts. L228-91–L228-106 Code de Commerce), and French Tech ecosystem instruments (BPI France; Tibi initiative; French Tech Visa). Use when a founder, investor, or counsel needs to: select BSPCE vs. BSA vs. ESOP for employee equity in a French SAS/SA; analyse BSPCE company and beneficiary eligibility after the Loi n° 2025-127 du 14 février 2025 reform; structure a French private placement under the <150 persons or qualified-investor exemption; review or draft obligations convertibles or OCABSA terms; analyse liquidation preference and anti-dilution provisions in a French SAS pacte d'associés; assess BPI France co-investment eligibility or Tibi sourcing; or compare French instruments against US SAFE/convertible note or UK ASA/SEIS structures. Also triggers on: gain de levée BSPCE 2025 flat-tax vs. income classification; BSA reclassification risk; actions de préférence liquidation waterfall; drag-along/tag-along SAS enforcement; BSPCE attribution collective decision; AMF NPAI requirements; OCABSA ratchet mechanics; BPI Prêt Amorçage Innovation eligibility; French Tech 2030 programme; SAS commissaire aux comptes threshold.


# Legalcode — French Venture Financing

> **Disclaimer**: This skill provides a framework for AI-assisted analysis of French venture
> financing. It does not constitute legal, tax, securities, or financial advice. All outputs must
> be reviewed by a qualified French avocat, expert-comptable, and securities counsel before any
> reliance or action. French tax and securities law change frequently; verify current applicability
> before relying on any provision. References to statutes (CGI Art. 163 bis G, CMF Art. L411-2,
> Code de Commerce Arts. L228-11 ff.), BOFiP guidance, and AMF positions carry currency risk —
> verify the latest edition. AI-generated cap table arithmetic and tax calculations require
> independent verification. Nothing here constitutes investment advice or an offer or solicitation
> to buy or sell securities. [VERIFY] markers indicate provisions requiring independent
> confirmation before reliance.

---

## Purpose and Scope

This skill analyses French venture financing end-to-end — from selecting the right employee
equity instrument to structuring private placements, reviewing convertible instruments, and
leveraging French Tech ecosystem programmes.

**Covers:**

- BSPCE eligibility, grant mechanics, and 2025 tax reform (Loi n° 2025-127 du 14 février 2025)
- BSA analysis: use cases, tax treatment, and reclassification risk
- SAS structural flexibility: actions de préférence, liquidation preferences, anti-dilution,
  drag-along/tag-along, and pacte d'associés architecture
- AMF private placement exemptions under Art. L411-2 CMF and EU Prospectus Regulation
  2017/1129 (<150 investors; qualified investor route)
- Obligations convertibles (OC), OCABSA, and BSAR: structure, conversion mechanics, and
  liquidation waterfall
- French Tech ecosystem: BPI France instruments (PAI, PTZ, CAP Innovation), Tibi initiative,
  French Tech Visa, and France 2030

**Does not:**

- Provide legal, tax, or investment advice or replace qualified counsel
- Perform a full term sheet analysis — route to `legalcode-term-sheet-analysis`
- Draft definitive documents (statuts, pacte d'associés, OC instrument)
- Cover listed-company securities regulation in depth (AMF full prospectus regime)
- Substitute for BOFiP advance ruling on BSPCE eligibility or AMF pre-clearance

**Relationship to other skills:**

| Task                                | Use This Skill  | Route To                              |
| ----------------------------------- | --------------- | ------------------------------------- |
| French employee equity analysis     | ✅ This skill   | —                                     |
| Full term sheet clause-by-clause    | Initial framing | `legalcode-term-sheet-analysis`       |
| International instrument comparison | ✅ This skill   | `legalcode-venture-financing-suite`   |
| French non-compete in pacte         | Cross-reference | `legalcode-non-compete-analysis-fr`   |
| French employment contract review   | Cross-reference | `legalcode-fr-contrat-de-travail-cdi` |
| French corporate formation          | Cross-reference | N/A (see SAS Module below)            |

---

## Jurisdiction and Governing Law

**Primary jurisdiction:** France (métropole and DOM-TOM where specified).

**Key legal frameworks:**

| Instrument                   | Primary Sources                                                                              |
| ---------------------------- | -------------------------------------------------------------------------------------------- |
| **BSPCE**                    | Art. 163 bis G CGI; Loi n° 2025-127 du 14 février 2025 Art. 92; BOFiP ACTU-2025-00124        |
| **BSA**                      | Art. L228-91 ff. Code de Commerce; Art. 150-0 A CGI (capital gains)                          |
| **SAS**                      | Arts. L227-1 to L227-20 Code de Commerce; actions de préférence Arts. L228-11 to L228-19     |
| **AMF exemptions**           | Art. L411-2 CMF; EU Prospectus Regulation 2017/1129                                          |
| **Obligations convertibles** | Arts. L228-91 to L228-106 Code de Commerce                                                   |
| **BPI France**               | Ordonnance n° 2012-1499 du 28 décembre 2012; BPI statutes                                    |
| **Tax base rules**           | CGI Arts. 150-0 A to 150-0 F (capital gains); Art. 80 quaterdecies (salary reclassification) |

**EU overlay:** EU Prospectus Regulation 2017/1129 applies directly to French law exemptions.
**GDPR** applies to investor data processing in placement documentation.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming intent,
the workflow pauses and asks when:

- Instrument eligibility depends on company or beneficiary characteristics not yet provided
- Tax treatment turns on facts (e.g., holding period, employment status, acquisition trigger)
- AMF exemption selection requires knowing investor count and qualification status
- Cross-border complexity creates forks only the user can resolve

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

- **Company profile**: SAS/SA structure, stage, amount raising, investor base, founder/employee equity needs
- **Document review**: BSPCE plan, BSA warrant terms, pacte d'associés, OC instrument, or AMF
  placement documentation as file/URL/pasted text
- **Specific question**: "Are we BSPCE-eligible after 2025 reform?", "Should we use BSPCE or BSA
  for an advisor?", "What exemption applies to our €3M seed round?"
- **Structured task**: Employee equity design, private placement structuring, OC review,
  BPI France eligibility assessment

If insufficient context is provided, proceed to Step 2 to gather what is needed.

### Step 2: Gather Context

**⟁ CLARIFY** — Before routing the analysis, ask the user these questions (skip any already
answered):

1. **Task type** — What is the primary objective?
   - Options: **Employee equity design** (BSPCE vs. BSA vs. actions gratuites), **BSPCE
     eligibility check** (company and beneficiary conditions after 2025 reform), **AMF
     exemption analysis** (private placement structuring), **OC/OCABSA review** (convertible
     instrument terms), **SAS pacte d'associés review** (governance, waterfall, anti-dilution),
     **BPI/French Tech** (ecosystem programme eligibility), **All of the above** (full
     financing suite)
   - _Why this matters_: Determines which modules to activate and what information to gather.

2. **Company form and characteristics** — Needed for BSPCE eligibility and AMF analysis:
   - Options: SAS, SA, SCA, SE, other (ineligible for BSPCE)
   - Key facts needed: date of incorporation, whether listed (if listed: market cap), whether
     subject to IS, ownership structure (≥25% natural persons?), whether formed through
     restructuring of an existing company
   - _Why this matters_: All five BSPCE company eligibility conditions must be satisfied
     cumulatively; failure on one disqualifies the entire BSPCE plan.

3. **Beneficiary type** — For BSPCE and BSA analysis:
   - Options: Employee (salarié), Corporate officer subject to IS (dirigeant soumis à l'IS),
     Consultant/advisor (not employee), Board observer or non-executive director
   - _Why this matters_: BSPCE is restricted to salariés and dirigeants soumis à l'IS. Advisors
     and consultants must use BSA or actions gratuites.

4. **Round stage and amount** — For AMF exemption routing:
   - Options: Pre-seed (<€500K), Seed (€500K–€3M), Series A (€3M–€10M), Growth (>€10M)
   - _Why this matters_: Determines which AMF exemption applies and whether the €8M 12-month
     rolling threshold under EU Prospectus Regulation triggers enhanced disclosure obligations.

5. **Investor composition** — For AMF exemption analysis:
   - Options: All qualified investors (investisseurs qualifiés), Fewer than 150 non-qualified
     persons (cercle restreint), Mixed (both qualified and non-qualified below 150), Uncertain
   - _Why this matters_: The Art. L411-2 CMF dual-exemption route must be selected correctly
     to avoid AMF prospectus obligation.

If the user provides partial context, proceed with what you have but **state assumptions
explicitly** (e.g., "Assuming you are raising from fewer than 150 investors — please confirm
if any non-qualified investors are included").

### Step 3: Load Legal Authority

Use **legalcode-mcp** to verify current versions of key provisions before analysis.

**Priority sources to verify:**

1. Art. 163 bis G CGI — BSPCE eligibility and tax treatment (post-2025 reform)
2. BOFiP ACTU-2025-00124 — administrative guidance on 2025 BSPCE reform [VERIFY]
3. Art. L411-2 CMF — current text of qualified investor and cercle restreint exemptions
4. Arts. L228-11 to L228-19 Code de Commerce — actions de préférence current text
5. EU Prospectus Regulation 2017/1129 — current exemption thresholds (€8M; 150 persons)

Save results to `/tmp/legalcode-venture-fr-authority.md`.

**If legalcode-mcp is not connected:**

- Mark all statutory references [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Focus analysis on structural and market-practice dimensions with enhanced [VERIFY] flags

### Step 4: Route to Active Modules

Based on Step 2 responses, activate the relevant modules from the Deep Analysis section:

| Module                           | Activate When                                                                           |
| -------------------------------- | --------------------------------------------------------------------------------------- |
| **A — BSPCE**                    | Employee equity with salarié/dirigeant IS beneficiaries; any BSPCE eligibility question |
| **B — BSA**                      | Advisor/consultant equity; non-BSPCE-eligible beneficiaries; BSA alongside BSPCE plan   |
| **C — SAS Structure**            | SAS governance review; pacte d'associés; liquidation preference; anti-dilution          |
| **D — AMF Private Placement**    | Any private fundraising; investor composition analysis                                  |
| **E — Obligations Convertibles** | OC, OCABSA, or BSAR in the round; bridge financing                                      |
| **F — French Tech Ecosystem**    | BPI France eligibility; Tibi sourcing; French Tech Visa                                 |

**⟁ CLARIFY** — For users requesting a full suite analysis (all modules), ask:

- "Should I prioritize any module for depth (e.g., BSPCE eligibility is most urgent) or give
  equal weight to all?"
- This helps scope the output for complex multi-module requests.

### Step 5: Run Module Analyses

Execute each active module per the Deep Analysis section. For each finding:

- Classify severity (COMPLIANT / FLAG / RISK / CRITICAL) per the classification framework
- Generate actionable output (next steps, redlines, or structuring alternatives)
- Apply Citation Quality Gates before finalizing each finding
- Apply Self-Interrogation for any CRITICAL findings

### Step 6: Cross-Module Integration

After completing individual module analyses, integrate findings across modules:

**Common cross-module issues to check:**

- BSPCE plan + pacte d'associés consistency: Do BSPCE exercise conditions align with
  drag-along triggers in the pacte? A drag-along before exercise may trigger income treatment.
- OC conversion + anti-dilution: Does OC ratchet interact with BBWA anti-dilution in the
  pacte? Check for double-trigger dilution protection.
- AMF exemption + investor count: Does the OC investor pool plus equity investors remain
  below 150 for the cercle restreint exemption?
- BPI France co-investment + round structure: Does BPI's pari passu requirement affect
  liquidation preference hierarchy?

**⟁ CLARIFY** — When cross-module conflicts are found, present them explicitly:

- "Your BSPCE plan allows exercise during a drag-along, but the OC conversion trigger
  coincides with the same acquisition event. Under the 2025 reform, this may reclassify
  BSPCE gains as income. Should I analyse this interaction in depth?"

### Step 7: Quality Verification

Before delivering output, run the quality framework:

- **Citation Quality Gates** (5 gates — see below): Run silently on all findings
- **Self-Interrogation** (3-pass — see below): Apply to all CRITICAL findings
- **Confidence Scoring** (5-level — see below): Assign to each finding
- **Completeness check**: Confirm all active modules have produced output

### Step 8: Deliver Output

Produce the output using the Output Format Template. Structure by module, with cross-module
integration section at the end. Include the Glass Box Audit Trail.

---

## Deep Analysis

### Module A — BSPCE (Bons de Souscription de Parts de Créateur d'Entreprise)

**Statutory basis:** Art. 163 bis G Code Général des Impôts (CGI); **2025 reform:** Loi
n° 2025-127 du 14 février 2025 (Loi de finances 2025), Article 92; BOFiP ACTU-2025-00124
(administrative guidance, August 2025). [VERIFY current BOFiP text]

#### A.1 Company Eligibility (Conditions Cumulatives)

All five conditions must be satisfied at the **date of BSPCE attribution**:

| #   | Condition      | Threshold / Rule                                                                                                                   | Common Failure Mode                                                                  |
| --- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| 1   | **Legal form** | SA, SAS, SCA, or SE only. SARL excluded.                                                                                           | Issuing company is a SARL — must convert to SAS first                                |
| 2   | **Age**        | Incorporated for fewer than **15 years** at attribution date                                                                       | Company too old; no grandfather rule for pre-reform grants                           |
| 3   | **Listed cap** | Either unlisted, or listed with market cap **≤ €150 million**                                                                      | Market cap exceeds threshold at subsequent grant tranches                            |
| 4   | **Tax status** | Subject to IS (impôt sur les sociétés) without permanent exemption                                                                 | Holding company exempt from IS; fiscal transparency entities                         |
| 5   | **Ownership**  | Minimum **25% of capital** held directly or indirectly by natural persons; or by entities themselves ≥75% owned by natural persons | Cap table diluted below 25% natural-person threshold after large institutional round |

**Additional restriction (post-2025 reform):** [VERIFY]

- Company must not have been formed through restructuring (apport partiel d'actif, fusion,
  scission) of an entity that would not itself qualify. [VERIFY under 2025 guidance]

**FLAG trigger:** If any condition fails → BSPCE issuance is invalid; existing unexercised
BSPCE may be void → reclassify as BSA or consider actions gratuites (AGAs).

#### A.2 Beneficiary Eligibility

BSPCE may only be attributed to:

- **Salariés** (employees with a contrat de travail) of the issuing company or a 75%+ owned
  subsidiary at the date of attribution
- **Dirigeants soumis à l'IS**: président of a SAS, president/directeur général of an SA,
  or gérant of an SCA, provided they are subject to French corporate income tax on their
  remuneration [VERIFY scope of covered officers post-2025 reform]

**Excluded beneficiaries:** Consultants, advisors, board observers (non-salariés),
non-executive directors who are not dirigeants. Use BSA (Module B) for these.

**Holding period at exercise:** No minimum holding period required to exercise. Tax
treatment differs based on when shares are sold (see A.4).

#### A.3 Plan and Grant Mechanics

**Attribution decision:** Requires a collective decision of shareholders (AGE or AGO
depending on statuts) or board delegation. The BSPCE plan must specify:

- Exercise price (prix d'exercice) ≥ fair market value at attribution date [VERIFY
  accepted valuation methodologies post-2025]
- Exercise conditions (conditions de performance, vesting schedule, good/bad leaver)
- Exercise window (délai d'exercice — typically 10 years from grant)
- Transferability: BSPCE are non-transferable (incessibles) by law

**Vesting structure:** French law does not mandate vesting but market practice is 4 years
with 1-year cliff (25% at 12 months, monthly thereafter). The pacte d'associés typically
contains leaver provisions linked to unvested BSPCE.

**Good leaver / bad leaver:** Define clearly — "bad leaver" BSPCE typically lapse or must
be exercised at a reduced price. French courts will scrutinize clauses that effectively
result in no compensation for vested warrants. [VERIFY under Cass. Com. recent case law]

#### A.4 Tax Treatment — 2025 Reform (Art. 163 bis G; Loi 2025-127)

The 2025 Finance Law fundamentally restructured BSPCE taxation. The prior two-tier regime
(flat 30% if held >3 years, or ordinary income if <3 years) was replaced. [VERIFY full
scope of reform under BOFiP ACTU-2025-00124]

**Key 2025 changes:** [VERIFY each element]

| Event                                                                    | Pre-2025 Regime                                                                      | 2025 Reform                                                                                                                                           |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Gain de levée** (exercise gain = FMV at exercise minus exercise price) | Taxed as capital gain: 12.8% IR + 17.2% PS = 30% PFU if >3yr activity; 47.2% if <3yr | Reclassified as income (revenu salarial) if company is acquired before beneficiary completes qualifying activity period [VERIFY exact holding period] |
| **Gain de cession** (sale gain = sale price minus FMV at exercise)       | Taxed as capital gain: 30% PFU (or barème option)                                    | Capital gains tax applies; PFU 30% [VERIFY]                                                                                                           |
| **Social charges**                                                       | No URSSAF on BSPCE gains (key advantage vs. stock-options)                           | Social charge exemption maintained [VERIFY 2025 reform preserved this]                                                                                |
| **Acquisition trigger**                                                  | Exercise followed by sale — two separate events                                      | If company acquired before qualifying period: gain de levée = ordinary income risk                                                                    |

**Critical 2025 risk:** Under the new regime, if the company is **acquired** (cession de
contrôle) before beneficiaries complete the required activity period, the gain de levée
may be reclassified as salary income, triggering marginal income tax rates + PS 17.2%
instead of PFU 30%. This "acquisition income trap" must be addressed in BSPCE plan design
and pacte d'associés drag-along provisions. [VERIFY under BOFiP ACTU-2025-00124]

**Practical structuring response:** Consider accelerated vesting provisions (double-trigger
acceleration) that allow full exercise before the acquisition closing date, converting the
gain de levée into a pre-acquisition capital gain. Requires legal and tax advice.

#### A.5 BSPCE vs. Alternative Instruments — Decision Matrix

| Instrument                  | Eligible Beneficiaries   | Social Charges                   | Tax Rate on Gain                                           | Formalities                                |
| --------------------------- | ------------------------ | -------------------------------- | ---------------------------------------------------------- | ------------------------------------------ |
| **BSPCE**                   | Salariés, dirigeants IS  | None on gain                     | PFU 30% (capital) if conditions met                        | AGE/plan; prix ≥ FMV                       |
| **Actions gratuites (AGA)** | Salariés, dirigeants IS  | Employer contribution (~20-30%)  | Income tax on acquisition gain; capital gains on sell gain | AGE; 1yr acquisition + 1yr lock-up minimum |
| **BSA**                     | Any natural/legal person | Depends on employment link       | Capital gains if no employment link                        | AGE or board                               |
| **Stock-options (SA only)** | Salariés, dirigeants IS  | Full social charges at exercise  | Income tax + PS                                            | AGE; SA only                               |
| **Carried interest**        | Fund managers via FPCI   | None if FPCI structure compliant | Capital gains if conditions met                            | Complex fund structuring                   |

---

### Module B — BSA (Bons de Souscription d'Actions)

**Statutory basis:** Art. L228-91 ff. Code de Commerce (general warrant regime); no specific
BSA statute (BSA are a subset of bons de souscription).

#### B.1 Use Cases for BSA in Venture

BSA are the correct instrument when BSPCE is unavailable or unsuitable:

- **Advisors and consultants** (non-salariés, non-dirigeants IS)
- **Foreign parent employees** of French subsidiaries that do not qualify for BSPCE
- Companies that exceed the BSPCE eligibility thresholds (>15 years; listed >€150M)
- **Investor warrants** attached to convertible instruments (OCABSA — see Module E)

#### B.2 BSA Tax Treatment

**If no employment / salary link:**

- BSA are a financial instrument; gain on exercise is typically treated as capital gain
  under Art. 150-0 A CGI
- PFU 30% (or barème option with 40% rebate if held >2 years as securities) [VERIFY rebate
  eligibility for BSA]
- No social charges if beneficiary is not an employee or corporate officer

**Reclassification risk (critical):**

- If BSA is granted to an advisor in lieu of remuneration (substitution de rémunération),
  tax authorities (DGFiP) may reclassify the exercise gain as professional income (BNC or
  traitements et salaires)
- Apply commercial pricing to BSA: prix de souscription of BSA itself + prix d'exercice
  should reflect arm's length value. Underpriced BSA = reclassification risk
- Document the commercial justification for BSA grants in board resolutions

**AMF considerations for BSA issuance:**

- BSA are "titres de créance" or warrants — if offered to more than 150 persons or to
  non-qualified investors above €8M, prospectus obligation may arise [VERIFY]
- For typical VC-round BSA attached to OC: cercle restreint or qualified investor exemption
  usually applies (see Module D)

---

### Module C — SAS Structural Analysis

**Statutory basis:** Arts. L227-1 to L227-20 Code de Commerce (SAS); Arts. L228-11 to
L228-19 (actions de préférence).

#### C.1 Why SAS Dominates French VC

The SAS (Société par Actions Simplifiée) is the near-universal French startup vehicle because:

- **Maximum contractual freedom**: Statuts can depart from most Companies Act defaults
- **Actions de préférence** (L228-11): Create any class of shares with any economic and
  governance rights — liquidation preferences, anti-dilution, enhanced voting, information
  rights, veto rights
- **No minimum capital**: Can be incorporated with €1 (vs. €37K for SA)
- **Single président** (no mandatory board unless statuts require): Faster decisions
- **BSPCE-eligible**: SAS is an eligible form for BSPCE
- **Flexible exit mechanisms**: Clause de sortie forcée (drag-along) and clause de cession
  préférentielle (tag-along) are standard in statuts or pacte

**Commissaire aux comptes (CAC) obligation** — mandatory if 2 of 3 thresholds exceeded:

- Total assets > €4M (raised from €1M post-2022 Loi DDADUE reform [VERIFY current threshold])
- Net turnover > €8M [VERIFY]
- Average employees > 50
- Also mandatory if any investor holds >5% and the SAS has 200+ shareholders [VERIFY]

#### C.2 Actions de Préférence — Clause Analysis

**Liquidation preference (clause de préférence de liquidation):**

| Preference Type            | Structure                                                          | Market Practice in France                                |
| -------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------- |
| **Non-participating 1x**   | Investor recovers invested amount OR converts to common (not both) | Standard at Seed/Series A                                |
| **Participating 1x**       | Investor recovers invested amount THEN participates in remainder   | Negotiated; above market at early stage                  |
| **Participating with cap** | Participation capped at 2x–3x invested amount                      | Compromise position                                      |
| **Multiple liquidation**   | 1.5x or 2x recovery before common                                  | Red flag for founders; associated with distressed rounds |

**Assess the following for each liquidation preference clause:**

- **Triggering events**: Is liquidation preference triggered only by dissolution, or also by
  M&A/asset sale/IPO? Broad definitions favour investors; narrow definitions favour founders.
- **Carve-outs**: Does an IPO at a sufficient valuation (e.g., 3x invested amount) result in
  automatic conversion to common, bypassing the preference?
- **Multiple series stacking**: When multiple series exist, are preferences pari passu or
  sequential (waterfall)? Sequential favours later investors at expense of earlier ones.
- **Deemed liquidation**: Does the clause treat a "significant" asset sale (e.g., >50% of
  revenue-generating assets) as a liquidation event? [VERIFY enforceability under Code de
  Commerce — potential conflict with Art. L228-11 actions de préférence]

**Anti-dilution clause (clause de protection contre la dilution):**

| Type                                    | Mechanism                                                                                        | French Law Implementation                                                                |
| --------------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **Broad-based weighted average (BBWA)** | New exercise price = weighted average of old price and down-round price using all diluted shares | Preferred; implemented via adjustment of BSA/BSPCE exercise price or OC conversion ratio |
| **Narrow-based weighted average**       | Same but uses only shares outstanding (not fully diluted)                                        | More aggressive for investors                                                            |
| **Full ratchet**                        | Exercise price reset to down-round price                                                         | Highly dilutive to founders; below market in EU                                          |

**French implementation note:** Under Arts. L228-11 to L228-19, economic rights of actions
de préférence must be defined in the statuts or an annexe. Anti-dilution adjustments are
typically implemented via adjustment clauses in the statuts tied to the ratio de conversion
or via BSA adjustment provisions. [VERIFY that statuts/pacte d'associés anti-dilution
mechanism meets Code de Commerce requirements for validity]

**Drag-along clause (clause de sortie forcée):**

- Valid under Art. L227-16 Code de Commerce (SAS freedom of contract)
- Must specify: threshold (e.g., >50% of shareholders; investor majority), exit price
  condition (typically ≥ preference recovery), minimum notice period
- **2025 BSPCE interaction**: If drag-along can be exercised before BSPCE exercise, BSPCE
  holders may face income reclassification risk under 2025 reform. Include BSPCE
  acceleration provision triggerable before drag-along completion.
- Good faith obligation: French courts (Art. 1104 Code Civil) may invalidate drag-along
  provisions exercised abusively (e.g., forcing exit at nominal value to dilute founders)

**Tag-along clause (clause de cession préférentielle):**

- Investor right to co-sell pro rata to any founder/investor share sale exceeding a
  threshold (e.g., >5% of shares in a single transaction)
- Boite aux lettres exception: Tag-along typically does not apply to intra-group transfers
  or transfers to family members (donateurs)
- Partial tag-along: Investor can participate proportionally even if acquiror does not
  accept all tagged shares (standard market position)

#### C.3 Pacte d'Associés Architecture

The pacte d'associés (shareholders' agreement) is the key governance document in a French
SAS venture round. Key modules:

| Clause                                              | French Standard                                                                                                  | Risk if Absent or Poorly Drafted                                  |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Information rights (droits d'information)           | Monthly management accounts; quarterly board report; annual audit access                                         | Investors cannot monitor investment; CLM triggers missed          |
| Board composition (composition du conseil)          | Investor board seat(s); observer rights; right to appoint if revenue milestone missed                            | Loss of governance control for investors                          |
| Reserved matters (matières réservées)               | List of decisions requiring investor consent (new BSPCE plan; new debt >€Xk; capex above threshold; key hirings) | Company takes major actions without investor consent              |
| ROFR / ROFO                                         | Right of first refusal / right of first offer on share transfers                                                 | Shares sold to third parties without investor ability to purchase |
| Representations and warranties                      | Financial condition; IP ownership; no material litigation; BSPCE eligibility                                     | Investor has no remedy for pre-closing misrepresentations         |
| Non-compete on founders (clause de non-concurrence) | Typically 24-month post-departure; limited geography and activity                                                | Founders can immediately compete after exit                       |
| Lock-up on founders                                 | Founders cannot sell > X% of shares before [date/event]                                                          | Founders exit before company reaches maturity                     |

---

### Module D — AMF Private Placement

**Statutory basis:** Art. L411-2 Code Monétaire et Financier (CMF); EU Prospectus
Regulation 2017/1129 Arts. 1(4) and 3(2).

#### D.1 Exemption Selection Framework

A French SAS/SA offering securities must either:

1. File an AMF-approved prospectus, OR
2. Qualify for an exemption under Art. L411-2 CMF

**Primary exemptions for venture-stage companies:**

| Exemption                                      | French Law Basis     | EU Reg Basis              | Key Condition                                                                 | Limit                                            |
| ---------------------------------------------- | -------------------- | ------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------ |
| **Qualified investor** (investisseur qualifié) | Art. L411-2 I 1° CMF | Art. 1(4)(a) PR 2017/1129 | All subscribers are investisseurs qualifiés per Art. L533-16 CMF              | No limit on amount                               |
| **Cercle restreint** (<150 persons)            | Art. L411-2 I 2° CMF | Art. 1(4)(b) PR 2017/1129 | <150 natural or legal persons per member state, excluding qualified investors | No limit on amount (but see €8M threshold below) |
| **Unit value ≥ €100,000**                      | Art. L411-2 I 3° CMF | Art. 1(4)(c) PR 2017/1129 | Each unit subscribed ≥ €100K                                                  | Typical for institutional rounds                 |
| **Below €8M threshold**                        | Art. L411-2 II CMF   | Art. 3(2)(b) PR 2017/1129 | Total consideration over 12 months < €8M                                      | Simplified disclosure may be required            |

**Typical French venture round exemption path:**

- **Pre-seed / Seed (≤€3M, family/friends/angels):** Cercle restreint (<150 persons) +
  qualified investor for institutional investors
- **Series A (€3M–€15M):** Qualified investor route for all investors (VCs, family offices)
- **Growth rounds (>€15M with broad LP base):** Require legal counsel to confirm exemption
  or prepare simplified documentation

**Note présentant les caractéristiques de l'opération (NPAI):**

- Under Art. L411-2 CMF, the AMF may require a simplified information note even when a
  full prospectus is not required. Check current AMF position for the relevant exemption.
  [VERIFY current AMF guidance on NPAI requirements]

#### D.2 Qualified Investor Definition

An **investisseur qualifié** is defined in Art. L533-16 CMF by reference to EU categories:

- Investment firms (PSI — prestataires de services d'investissement)
- Credit institutions
- Insurance companies and mutual funds (OPCVM, FIA)
- Pension funds
- Large companies meeting 2 of 3: balance sheet ≥ €20M; turnover ≥ €40M; own funds ≥ €2M
- Governments and supra-national bodies
- **Individuals optant in**: individuals who have requested to be treated as professional
  clients under MiFID II criteria (portfolio ≥ €500K; 10+ significant transactions per
  quarter; ≥1 year professional finance experience) [VERIFY current CMF/AMF criteria]

**Critical compliance requirement:** Obtain written confirmation of qualified investor status
from each investor before the offering. Document the basis for classification.

#### D.3 Marketing Restrictions

Even within exempted offerings:

- Do not advertise publicly (no general solicitation) — distinguishes EU/French practice
  from US Reg D 506(c) general solicitation approach
- Do not use social media, press releases, or public websites to solicit investment
  [VERIFY current AMF guidance on digital marketing and social media for exempt offerings]
- Limit distribution of placement materials to the exempt category
- Crowdfunding platforms are subject to separate EU Regulation 2020/1503 (ECSP Regulation)
  — not covered by these exemptions

---

### Module E — Obligations Convertibles (OC / OCABSA / BSAR)

**Statutory basis:** Arts. L228-91 to L228-106 Code de Commerce (convertible instruments);
Art. L225-149-1 (protection of OC holders in capital increases); Art. L228-98 (anti-dilution
protection for convertible holders).

#### E.1 Instrument Taxonomy

| Instrument                                       | Description                                                                              | Typical Use Case                                     |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| **OC** (Obligation Convertible)                  | Convertible note; fixed interest; converts to equity at maturity or qualifying financing | Bridge financing; early pre-Series A                 |
| **OCA** (OC avec option de conversion accélérée) | OC with accelerated conversion option triggered by events                                | Flexible bridge for multiple conversion scenarios    |
| **OCABSA**                                       | OC + BSA (warrants) attached; OC converts, BSA provides upside kicker                    | Complex rounds; ratchet mechanisms; bridge to Series |
| **BSAR**                                         | Bon de Souscription d'Action Remboursable; warrant redeemable for cash if not exercised  | Investor protection when exercise may not occur      |
| **ORA** (Obligation Remboursable en Actions)     | Mandatorily redeemable in shares; no cash repayment option                               | Strong conversion certainty; investor-preferred      |

#### E.2 OC Key Terms Checklist

Analyse each term for market conformity and risk classification:

**Economic terms:**

- **Interest rate** (taux d'intérêt): Typically 0–8% PIK for venture OC. Zero-interest OC
  may trigger gift-tax risk if below market rate — [VERIFY] French tax authority position.
- **Conversion discount** (décote de conversion): 10–20% typical. Assess whether trigger
  conditions are clear and whether discount applies to both qualified financing price and
  maturity conversion.
- **Valuation cap** (plafond de valorisation): Standard in pre-money SAFE-equivalent French
  OC structures. Verify cap applies to both qualifying financing and maturity conversion.
- **MFN clause** (clause de la nation la plus favorisée): Converts OC terms to most
  favourable terms offered to later investors. Verify scope (BSA, discount, cap).

**Structural terms:**

- **Maturity date** (date d'échéance): 18–24 months typical. Assess whether maturity
  conversion is at a reasonable formula or at potentially unfavourable pre-money valuation.
- **Qualifying financing threshold**: Define clearly — what constitutes a "qualified
  financing"? Amount raised? New investors? A poorly defined threshold is a common source
  of dispute.
- **Acceleration events**: What triggers immediate conversion or repayment? Change of
  control, IPO, insolvency? Ensure BSPCE holders can exercise before conversion if
  acquisition triggers both BSPCE reclassification risk and OC conversion.
- **Subordination** (rang): OC holders should be senior to equity in liquidation but
  typically subordinate to secured bank debt. Verify ranking in the context of any BPI
  France co-investment that has preferential rank. [VERIFY BPI loan ranking]

**Tax treatment of OC:**

- Interest on OC is **deductible** by the issuer for IS purposes if OC is debt-classified
- **Interest paid to investors:** Subject to PFU 30% (IR + PS) at investor level if
  individuals; or corporate IS at investor level if legal persons
- **Conversion gain:** Treated as capital gain (Art. 150-0 A CGI) at time of share sale —
  not at conversion. The conversion itself is typically a neutral event for tax. [VERIFY]
- **Thin capitalisation rules** (Art. 212 CGI): If OC holders are related parties, verify
  interest deductibility is not limited by thin capitalisation rules.

#### E.3 OCABSA Ratchet Mechanics

OCABSA combines an OC (which converts into shares) with attached BSA (which provide upside).
The ratchet mechanism adjusts the number of shares the BSA can subscribe at exercise:

- **Down-round ratchet**: BSA exercise price resets to new lower price in a down round.
  Anti-dilutive for OC/BSA holders; dilutive for founders.
- **Time-based ratchet**: BSA exercise price decreases over time if no qualifying financing.
  Penalises slow capital raising.
- **Performance ratchet**: Conversion ratio increases/decreases based on revenue or
  valuation milestones.

**Assess:** Is the ratchet formula defined with mathematical precision? Ambiguous ratchet
formulas are the most litigated provision in French VC documents. [VERIFY under Cass. Com.
recent OCABSA case law]

---

### Module F — French Tech Ecosystem

#### F.1 BPI France Instruments

**Banque Publique d'Investissement** (BPI France; created by Ordonnance n° 2012-1499) provides:

| Instrument                              | Description                                                        | Key Eligibility                                     | Interest Rate                  | Note                                  |
| --------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------- | ------------------------------ | ------------------------------------- |
| **Prêt Amorçage Innovation (PAI)**      | Pre-seed loan; no collateral; deferred repayment                   | Startup <5yr; IP-rich; EI or BS innovation label    | Variable (subsidised) [VERIFY] | Often combined with equity raise      |
| **Prêt à Taux Zéro Innovation (PTZ)**   | Zero-interest innovation loan                                      | SME status; innovation project; no BPI equity prior | 0%                             | Repayable over 5–7 years              |
| **CAP Innovation**                      | Working capital guarantee; extends bank lines for innovative firms | Bpifrance innovation label + bank partner           | N/A (guarantee fee)            | Enables bank leverage on BPI backstop |
| **Prêt Croissance International (PCI)** | International expansion loan                                       | Established turnover; export project                | Subsidised [VERIFY]            | Available from BPI regional offices   |
| **Fonds de co-investissement**          | Equity co-investment alongside certified VC investors              | VC lead investor required; SME or ETI               | N/A                            | Pari passu with lead VC               |

**BPI co-investment key rules:** [VERIFY current BPI guidelines]

- BPI typically requires a certified private lead investor (fonds labellisé BPI or AFIC member)
- BPI investment is pari passu with lead investor on price and terms
- BPI does not take board seat or blocking rights typically
- Minimum co-investment size and maximum BPI stake vary by programme [VERIFY]

**BPI labelling — French Tech label:**

- "French Tech" or "Bpifrance Excellence" labels help access preferential BPI financing
- French Tech 2030 programme: deeptech, green tech, health tech, sovereignty tech priorities

#### F.2 Tibi Initiative

The **Tibi Initiative** (2020, coordinated by Banque de France) committed French institutional
investors (insurance companies, pension funds) to allocate €30B to VC/growth funds by 2025.
[VERIFY current Tibi II status and targets for 2025–2030]

**Practical relevance:**

- Tibi creates a stable domestic LP base for French VC funds
- Startups raising from Tibi-certified funds benefit from more patient capital
- Tibi funds typically have longer investment horizons than non-Tibi US/UK funds

#### F.3 French Tech Visa

The **French Tech Visa** (created 2017) provides a simplified 4-year residence permit for:

- **Founders (porteurs de projet)**: Founders of French Tech–labelled startups
- **Employees (salariés)**: Employees of French Tech–labelled companies earning ≥€35K/year
  [VERIFY current salary threshold]
- **Investors (investisseurs)**: Investors who have committed ≥€300K in French startups

**For international hiring in French SAS:** The French Tech Visa for employees enables faster
and simpler visa processing than the standard salariat route. Verify the company holds a valid
French Tech label (or is in the process of obtaining one). [VERIFY current French Tech label
application procedures post-French Tech 2030 relaunch]

#### F.4 France 2030 / PIA

The **France 2030** investment plan (€54B total commitment) targets deeptech, green transition,
and sovereignty industries. For startups:

- AAP (Appels à Projets) — competitive grants and subsidies via Bpifrance
- I-Lab competition: Pre-creation award up to €600K for research-intensive startups [VERIFY]
- French Tech Émergence: Support for emerging French Tech ecosystems outside Paris

---

## Severity Classification

Classify each finding using the four-tier system:

| Level | Label         | Definition                                                                                        | Required Action                                                            |
| ----- | ------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| 🔴    | **CRITICAL**  | Immediate legal risk, invalid structure, or regulatory violation.                                 | Stop and resolve before proceeding. Mandatory legal counsel.               |
| 🟠    | **RISK**      | Significant risk that may not be immediately evident; adverse outcome possible without action.    | Resolve before closing or within 30 days. Recommend counsel review.        |
| 🟡    | **FLAG**      | Below market standard or unfavourable term; acceptable but warrants negotiation or documentation. | Flag to principals; negotiate if possible; document rationale if accepted. |
| 🟢    | **COMPLIANT** | Market standard or better; no action required.                                                    | Note for awareness; no action needed.                                      |

**Auto-CRITICAL triggers (escalate regardless of user preference):**

- BSPCE eligibility condition fails → existing BSPCE plan is legally invalid
- Offering to >150 non-qualified persons without AMF prospectus → regulatory violation
- OC interest rate structured to circumvent thin capitalisation rules → tax risk
- Drag-along triggered before BSPCE exercise without acceleration provisions → 2025 income tax trap
- SAS actions de préférence not defined in statuts (pacte d'associés alone is insufficient) → void preference rights

---

## Actionable Output Per Finding

For each finding, produce:

| Field                  | Content                                                               |
| ---------------------- | --------------------------------------------------------------------- |
| **Finding**            | Short description of the issue                                        |
| **Classification**     | CRITICAL / RISK / FLAG / COMPLIANT                                    |
| **Legal basis**        | Statutory provision or market practice source                         |
| **Impact**             | Consequence if unaddressed                                            |
| **Recommended action** | Specific next step (redline, restructure, obtain advice)              |
| **Draft language**     | Where applicable, suggested French-language clause or English summary |
| **Confidence**         | 0.0–1.0 with level label                                              |

---

## Prioritization Framework

Prioritize findings for action using four tiers:

| Priority             | Tier                      | Timing               | Typical Findings                                                                          |
| -------------------- | ------------------------- | -------------------- | ----------------------------------------------------------------------------------------- |
| **P1 — Blocking**    | Must resolve before close | Before signing       | CRITICAL findings; BSPCE invalidity; AMF violation; OC void provisions                    |
| **P2 — Material**    | Resolve within 30 days    | 0–30 days post-close | RISK findings; major waterfall misalignment; missing drag-along acceleration              |
| **P3 — Recommended** | Resolve within 90 days    | 30–90 days           | FLAG findings; below-market terms; missing information rights; incomplete representations |
| **P4 — Advisory**    | Background improvements   | 90–180 days          | Minor drafting improvements; French Tech label application; BPI programme exploration     |

---

## Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                  | Fail Action                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every legal claim cites a specific statute (e.g., Art. 163 bis G CGI), BOFiP guidance, AMF position, or established market practice   | Add citation or mark [UNVERIFIED]   |
| **Format**     | All citations follow French citation conventions (Art. L411-2 CMF; Loi n° 2025-127 du 14 février 2025; Cass. Com. [date] n° [number]) | Fix format                          |
| **Currency**   | Every provision checked for 2025 reform amendments; BOFiP guidance versions verified                                                  | Flag [CHECK CURRENCY]               |
| **Domain**     | Analysis stays within French law; do not import US/UK VC concepts without noting they require French law adaptation                   | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated; 2025 reform provisions marked [VERIFY] where BOFiP guidance is recent                                  | Add confidence qualifier            |

---

## Self-Interrogation for CRITICAL Findings

For any finding classified CRITICAL, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity:**
Does the risk assessment follow logically from the cited statutory provision? Would a French
tribunal de commerce or tax authority (DGFiP) actually reach this conclusion? Is the 2025
BOFiP guidance (ACTU-2025-00124) the authoritative source for the BSPCE tax position?

**Pass 2 — Completeness:**
Have all relevant statutory provisions been considered? Does the analysis cover both the
CGI (tax) and Code de Commerce (corporate) dimensions of the finding? Are there regulatory
dimensions (AMF; social charges URSSAF) not yet addressed?

**Pass 3 — Challenge:**
What is the strongest argument against this CRITICAL classification? Under what circumstances
might a reasonable French avocat accept this risk without modification? Is there a structuring
solution that resolves the issue without reopening the entire agreement?

---

## Confidence Scoring

| Level         | Range     | Meaning                                                                 | Action                                               |
| ------------- | --------- | ----------------------------------------------------------------------- | ---------------------------------------------------- |
| **Définitif** | 0.95–1.0  | Settled French law; unambiguous Code de Commerce provision              | State with confidence                                |
| **Élevé**     | 0.80–0.94 | Strong statutory authority; minor interpretive questions                | State with brief caveat                              |
| **Probable**  | 0.60–0.79 | Good arguments; BOFiP guidance recent or not yet published              | State with reasoning and contra-indicators; [VERIFY] |
| **Possible**  | 0.40–0.59 | Genuinely uncertain; 2025 reform implementing guidance still developing | Flag for avocat/expert-comptable review; both sides  |
| **Incertain** | 0.0–0.39  | Weak basis; speculative interpretation                                  | Do not assert; flag [UNCERTAIN]                      |

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-venture-financing-fr"
  mode: "Created from scratch"
  topic: "French venture financing — BSPCE, BSA, SAS, AMF, OC, French Tech"
  jurisdiction: "France (Code Général des Impôts; Code de Commerce; Code Monétaire et Financier)"
  reform_reference: "Loi n° 2025-127 du 14 février 2025 (Finance Law 2025), Article 92"
  bofip_reference: "ACTU-2025-00124 (August 2025) [VERIFY current status]"
  modules_activated: "[List modules from A–F that were run]"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "/tmp/legalcode-venture-fr-authority.md"
  quality_score: "[X]/40"
  completeness: "18/18 elements"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED / VERIFY-flagged]"
  critical_findings: "[number]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  assumptions:
    - "[Any assumptions made due to missing user context]"
  limitations:
    - "2025 BSPCE reform implementing guidance (BOFiP ACTU-2025-00124) is recent — verify current text"
    - "AMF guidance on digital marketing and exempt offerings evolves; verify current AMF position"
    - "BPI France programme terms change annually — verify current eligibility and rates"
    - "This analysis does not substitute for a BOFiP advance ruling or AMF pre-clearance"
    - "Cap table arithmetic and tax calculations require independent verification"
  reviewer: "AI-assisted — requires review by qualified French avocat and expert-comptable"
```

---

## Anti-Patterns

The following errors occur frequently in French VC practice. Identify and flag any that are
present in the documents or structure under review.

1. **BSPCE issued by a SARL**: SARL is not an eligible BSPCE issuer. Invalidates the entire
   plan. Solution: convert to SAS before attribution.

2. **BSPCE attributed to a consultant**: Non-salariés cannot hold BSPCE. Use BSA instead.
   Failing to distinguish means BSPCE warrants are invalid and may be reclassified.

3. **BSPCE exercise price below fair value at grant date**: Triggers income tax reclassification
   of the discount element. Must use an independent valuation or arm's-length board assessment.

4. **No acceleration provision in BSPCE plan on drag-along**: Post-2025 reform, an acquisition
   triggered by drag-along before exercise converts gain de levée from capital gains to
   ordinary income. Standard fix: double-trigger acceleration clause in BSPCE plan.

5. **Natural person ownership falls below 25% post-round**: Institutional investors taking
   large stakes can dilute natural-person ownership below the BSPCE eligibility threshold.
   Post-closing BSPCE attributions become invalid. Monitor cap table after each round.

6. **Liquidation preference only in pacte d'associés, not in statuts**: Under Art. L228-11
   Code de Commerce, actions de préférence rights must be defined in the statuts (or an annexe
   thereto). Preferences defined only in the pacte are enforceable only contractually and may
   not bind the company or future shareholders.

7. **AMF cercle restreint exceeded**: Offering to more than 150 persons (including employees in
   BSPCE/BSA plan) without a prospectus or without confirming their qualified investor status.
   Count all offerees per 12-month rolling period across all instruments.

8. **OC qualifying financing threshold undefined**: "A significant financing round" is not a
   qualifying financing threshold. Without a defined amount, maturity can be triggered
   prematurely, forcing conversion at an unfavourable valuation.

9. **OCABSA ratchet formula expressed in words, not mathematics**: "The BSA exercise price will
   be adjusted to reflect the new round price" is insufficient. The formula must be algebraically
   defined to avoid dispute.

10. **Zero-interest OC between related parties**: Art. 212 CGI thin capitalisation rules and
    gift-tax provisions can apply to related-party loans (including OC) where interest is below
    market rate. Document arm's-length rate justification or seek advance ruling.

11. **BSA granted to key employee as substitute for salary**: Triggers reclassification risk
    (revenu salarial rather than capital gain) and may subject the company to URSSAF social
    charges. BSA should be granted on commercial terms, not in lieu of compensation.

12. **Drag-along threshold too low**: A drag-along exercisable by a 50.1% majority in a
    fragmented cap table can be triggered by a single large investor against founders. Market
    standard is ≥60–75% of shareholders including majority of common and investor shares.

13. **Pacte d'associés signed but not disclosed to new investors**: A pacte d'associés binds
    only its signatories. New investors must accede to the pacte at closing. Failure to include
    accession clause (clause d'adhésion) leaves new investors outside governance structure.

14. **French Tech Visa applied for before label**: The French Tech Visa for employees requires
    a valid French Tech label. Applying before the label is confirmed results in visa refusal.
    Sequence label application before employee visa sponsorship.

15. **BPI co-investment without certified private lead**: BPI equity co-investment requires a
    certified private lead investor. Approaching BPI first without a committed private lead
    typically results in refusal or significant delay.

16. **Ignoring the CAC threshold at Series A**: A fast-growing SAS that exceeds 2 of 3 CAC
    thresholds post-round must appoint a commissaire aux comptes within the applicable grace
    period. Failure to do so is a criminal offence for the président. [VERIFY current thresholds
    and grace period post-Loi DDADUE]

17. **Assuming IPO conversion is automatic**: Some French SAS statuts do not include an
    automatic conversion of actions de préférence on IPO. Without explicit IPO conversion
    provisions, preference holders may retain preference rights post-listing, complicating
    the IPO structure.

18. **BSPCE plan not ratified by AGE**: BSPCE attribution requires a collective decision
    (typically AGE authorisation). BSPCE attributed on board authority alone — without AGE
    delegation — may be invalid. Review authorisation chain carefully.

19. **Missing good-leaver / bad-leaver definition**: BSPCE plans without clear leaver
    definitions create disputes on departure. Define "bad leaver" events (dismissal for
    cause, resignation during cliff period) and their consequences (lapse; exercise at strike
    price; forced transfer to company).

20. **Obligations convertibles interest not paid but accrued indefinitely**: PIK (payment-in-kind)
    interest compounds and can dramatically inflate the OC principal if no qualified financing
    occurs. Cap total OC amount including accrued PIK to protect against uncapped debt.

---

## Writing Standards

Before delivering any output, apply these standards:

1. **Bilingual terminology**: Use French legal terms with English translations on first use
   (e.g., "actions de préférence (preference shares)"). Subsequent references use the French
   term for precision.

2. **Imperative form for instructions**: "Verify that the BSPCE plan includes…" not "It would
   be advisable to verify…"

3. **Citation precision**: Always cite the specific article, not just the statute
   (Art. 163 bis G CGI; not just "the tax code").

4. **No false certainty**: The 2025 BSPCE reform is recent. Where BOFiP guidance is
   still developing, mark [VERIFY] and state the uncertainty explicitly.

5. **Findings first**: Lead with the finding and classification, then the legal basis and
   recommendation. Do not bury CRITICAL findings in analysis.

6. **Quantify where possible**: "The PFU flat tax is 30% (12.8% IR + 17.2% PS)" is more
   useful than "a flat tax applies."

7. **No generic advice**: Every recommendation must be specific to the documents under review,
   not a generic statement about French venture financing.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Verify Art. 163 bis G CGI text post-2025 amendment
- Confirm current BOFiP ACTU-2025-00124 guidance scope and effective date
- Retrieve current Art. L411-2 CMF text
- Confirm AMF General Regulation current provisions on qualified investor
- Search for recent Cour de cassation Commercial Chamber decisions on BSPCE, BSA
  reclassification, and OCABSA ratchet disputes
- Save verified results to `/tmp/legalcode-venture-fr-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Mark all statutory and case law references [VERIFY]
- Proceed with structural quality analysis and market-practice guidance
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Enhance [VERIFY] flagging density for all 2025 reform provisions

---

## Output Format Template

````markdown
# French Venture Financing Analysis

**Company:** [Name] **Date:** [YYYY-MM-DD] **Round:** [Stage / Amount]

> ⚠️ AI-assisted analysis — not legal or tax advice. Review with qualified French avocat and
> expert-comptable before reliance.

---

## Executive Summary

| Module            | Findings | Critical | Risk    | Flag    | Compliant |
| ----------------- | -------- | -------- | ------- | ------- | --------- |
| A — BSPCE         | [n]      | [n]      | [n]     | [n]     | [n]       |
| B — BSA           | [n]      | [n]      | [n]     | [n]     | [n]       |
| C — SAS Structure | [n]      | [n]      | [n]     | [n]     | [n]       |
| D — AMF Placement | [n]      | [n]      | [n]     | [n]     | [n]       |
| E — OC/OCABSA     | [n]      | [n]      | [n]     | [n]     | [n]       |
| F — French Tech   | [n]      | [n]      | [n]     | [n]     | [n]       |
| **Total**         | **[n]**  | **[n]**  | **[n]** | **[n]** | **[n]**   |

**Priority actions (P1 — Blocking):**

1. [CRITICAL finding]
2. [CRITICAL finding]

---

## Module A — BSPCE Analysis

### Eligibility Assessment

| Condition                     | Status                      | Finding  |
| ----------------------------- | --------------------------- | -------- |
| Legal form (SA/SAS/SCA/SE)    | ✅ / ❌                     | [detail] |
| Age ≤15 years                 | ✅ / ❌                     | [detail] |
| Listed cap ≤€150M or unlisted | ✅ / ❌                     | [detail] |
| IS subject without exemption  | ✅ / ❌                     | [detail] |
| ≥25% natural persons          | ✅ / ❌                     | [detail] |
| **Overall BSPCE eligibility** | ✅ ELIGIBLE / ❌ INELIGIBLE |          |

### Beneficiary Analysis

[Analyse each beneficiary category]

### 2025 Reform Risk Assessment

**Acquisition income trap analysis:**
[Assess whether drag-along / OC conversion could trigger income reclassification of gain
de levée under 2025 reform; recommend acceleration provisions]

### BSPCE Findings

| #   | Finding       | Classification | Legal Basis        | Action   | Confidence |
| --- | ------------- | -------------- | ------------------ | -------- | ---------- |
| A.1 | [description] | 🔴 CRITICAL    | Art. 163 bis G CGI | [action] | 0.90 Élevé |

---

## Module B — BSA Analysis

### BSA Tax Treatment Assessment

[Assess employment link; reclassification risk; AMF count implications]

### BSA Findings

| #   | Finding       | Classification | Legal Basis         | Action   | Confidence    |
| --- | ------------- | -------------- | ------------------- | -------- | ------------- |
| B.1 | [description] | 🟡 FLAG        | Art. L228-91 C.com. | [action] | 0.75 Probable |

---

## Module C — SAS Structure Analysis

### Actions de Préférence Waterfall

| Series   | Type               | Preference           | Participating? | Cap | Status           |
| -------- | ------------------ | -------------------- | -------------- | --- | ---------------- |
| Seed     | [actions de préf.] | 1x non-participating | No             | N/A | [COMPLIANT/FLAG] |
| Series A | [actions de préf.] | 1x participating     | Yes            | 2x  | [FLAG]           |

### Anti-Dilution Analysis

[BBWA vs. full ratchet; French law implementation]

### Drag-Along / Tag-Along

[Threshold; BSPCE interaction; good-faith risk]

### SAS Structure Findings

| #   | Finding       | Classification | Legal Basis         | Action   | Confidence |
| --- | ------------- | -------------- | ------------------- | -------- | ---------- |
| C.1 | [description] | 🟠 RISK        | Art. L228-11 C.com. | [action] | 0.85 Élevé |

---

## Module D — AMF Private Placement Analysis

### Exemption Assessment

| Criterion                          | Status                             | Detail                                            |
| ---------------------------------- | ---------------------------------- | ------------------------------------------------- |
| Total offerees                     | [n]                                | [COMPLIANT if <150]                               |
| Qualified investor status verified | ✅/❌                              | [detail]                                          |
| 12-month rolling amount            | €[X]M                              | [COMPLIANT if <€8M / or qualified investor route] |
| No general solicitation            | ✅/❌                              | [detail]                                          |
| **Applicable exemption**           | [Art. L411-2 I 1° / I 2° / II CMF] |                                                   |

### AMF Findings

| #   | Finding       | Classification | Legal Basis          | Action      | Confidence |
| --- | ------------- | -------------- | -------------------- | ----------- | ---------- |
| D.1 | [description] | 🟢 COMPLIANT   | Art. L411-2 I 2° CMF | None needed | 0.88 Élevé |

---

## Module E — Obligations Convertibles Analysis

### OC / OCABSA Key Terms

| Term                 | Current Provision | Market Standard | Classification   |
| -------------------- | ----------------- | --------------- | ---------------- |
| Interest rate        | [X%] PIK          | 0–8% PIK        | [COMPLIANT/FLAG] |
| Discount             | [X%]              | 15–20%          | [COMPLIANT/FLAG] |
| Cap                  | €[X]M pre-money   | N/A             | [COMPLIANT]      |
| Maturity             | [X] months        | 18–24 months    | [COMPLIANT/RISK] |
| Qualifying threshold | €[X]M new money   | Defined amount  | [COMPLIANT/RISK] |

### OC/OCABSA Findings

| #   | Finding       | Classification | Legal Basis         | Action   | Confidence |
| --- | ------------- | -------------- | ------------------- | -------- | ---------- |
| E.1 | [description] | 🔴 CRITICAL    | Art. L228-91 C.com. | [action] | 0.92 Élevé |

---

## Module F — French Tech Ecosystem

### BPI France Eligibility

[Programme eligibility assessment with specific programmes recommended]

### Tibi / French Tech Considerations

[Investor sourcing recommendations; French Tech label status]

---

## Cross-Module Integration

### Key Cross-Module Risks

| Risk                                         | Modules   | Classification | Action   |
| -------------------------------------------- | --------- | -------------- | -------- |
| BSPCE drag-along / OC conversion income trap | A + C + E | 🔴 CRITICAL    | [action] |
| AMF count: OC holders + equity investors     | D + E     | 🟡 FLAG        | [action] |
| BPI pari passu vs. investor preference       | E + F     | 🟡 FLAG        | [action] |

---

## Priority Action Plan

### P1 — Blocking (resolve before close)

- [ ] [CRITICAL action 1]
- [ ] [CRITICAL action 2]

### P2 — Material (resolve within 30 days)

- [ ] [RISK action 1]

### P3 — Recommended (resolve within 90 days)

- [ ] [FLAG action 1]

### P4 — Advisory (background improvements)

- [ ] [Advisory action 1]

---

## Glass Box Audit Trail

```yaml
[Populate from Glass Box template above]
```
````

---

_Generated by legalcode-venture-financing-fr. Not legal or tax advice._
_Verify all [VERIFY]-tagged provisions with a qualified French avocat and expert-comptable._

```

---

## Localization Notes

**Metropolitan France vs. Overseas Territories (DOM-TOM):**
- BSPCE eligibility applies in metropolitan France and DOM (Guadeloupe, Martinique,
  Guyane, La Réunion, Mayotte) under standard CGI rules. COM territories (Polynésie,
  Nouvelle-Calédonie) have autonomous tax regimes — [VERIFY] CGI applicability.
- AMF jurisdiction extends to all French territory including DOM-COM.

**Cross-border founders and investors:**
- Non-resident investors in French SAS: Verify withholding tax on dividends (typically
  15–30% under tax treaties; reduced under EU Parent-Subsidiary Directive for EU investors
  with ≥10% holding) [VERIFY applicable treaties]
- US investors in French SAS: FATCA compliance for French companies; US beneficial
  owner FBAR reporting; PFIC analysis for passive French companies [VERIFY with US tax
  counsel]
- UK post-Brexit: EU Parent-Subsidiary Directive no longer applies to UK investors in
  French companies; verify applicable FR-UK tax treaty [VERIFY]

**Comparison with US/UK instruments:**

| Dimension | French BSPCE | US ISO | UK EMI |
|-----------|-------------|--------|--------|
| Employee-only | Yes (+ dirigeants IS) | Yes | Yes |
| Social charges on gain | No | No (at exercise if AMT) | No |
| Capital gains rate | PFU 30% if conditions met | 20% LTCG if qualified | 10% BADR / 20% CGT |
| Company age limit | 15 years | None | None (but must be SME) |
| Listed company | Cap €150M | Any listed company | Must be unquoted |
| Annual individual limit | None (plan-level) | $100K per year vesting | £250K per employee |
| Company-level limit | None | None | £3M outstanding |

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:
- Primary legal research: Art. 163 bis G CGI (post-Loi n° 2025-127 du 14 février 2025 reform);
  BOFiP ACTU-2025-00124 [VERIFY]; Code de Commerce Arts. L228-11 to L228-19; Art. L411-2 CMF;
  EU Prospectus Regulation 2017/1129
- Repository patterns: `legalcode-venture-financing-de`, `legalcode-venture-financing-in`,
  `legalcode-venture-financing-suite` (structural patterns); `legalcode-fr-contrat-de-travail-cdi`,
  `legalcode-fr-bail-commercial` (French jurisdiction quality standard)
- Market practice: France Digitale position papers on BSPCE reform (2024–2025); AFIC/France
  Invest VC market benchmarks; BPI France programme documentation
- All [VERIFY]-tagged provisions require confirmation against current statutory text and BOFiP
  guidance before reliance
```
