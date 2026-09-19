---
name: legalcode-insurance-coverage-analysis
description: Analyze insurance coverage for claims and disputes across policy types — CGL, D&O, E&O/professional
  liability, cyber/tech E&O, EPL, property, and umbrella/excess. Use when a claim has been filed or threatened,
  when tendering a claim to insurers, when evaluating insurer coverage denials, when managing a coverage
  dispute, or when performing pre-dispute coverage mapping.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Analyze insurance coverage for claims and disputes across policy types — CGL, D&O, E&O/professional liability, cyber/tech E&O, EPL, property, and umbrella/excess. Evaluates duty to defend (broader than duty to indemnify), duty to indemnify triggers, coverage grant analysis against claim allegations, policy exclusion applicability (intentional acts, contractual liability, professional services, pollution, employment-related practices), notice requirements and late notice consequences, consent-to-settle provisions, hammer clauses, priority and exhaustion across policy towers, and reservation of rights implications. Covers bad faith exposure for insurer-side analysis. Use when a claim has been filed or threatened, when tendering a claim to insurers, when evaluating insurer coverage denials, when managing a coverage dispute, or when performing pre-dispute coverage mapping. Produces a structured coverage opinion framework with findings classified COVERED / DISPUTED / EXCLUDED and strategic recommendations. Jurisdiction-calibrated for US, UK, and Australia.


# Legalcode Insurance Coverage Analysis

> **Disclaimer**: This skill provides a framework for AI-assisted insurance coverage analysis
> and does not constitute legal advice, a legal opinion, or a coverage opinion from qualified
> coverage counsel. All outputs should be reviewed by a qualified insurance attorney or
> coverage counsel licensed in the relevant jurisdiction before any coverage position is taken,
> denied, or communicated to a counterparty. Insurance coverage law varies materially by
> jurisdiction, policy form, and claim type. Policy forms, endorsements, and manuscript
> exclusions must be read in their entirety — this skill cannot substitute for a complete
> policy analysis by qualified counsel. Laws change; verify current applicability before
> relying on any provision described here. Statutory, regulatory, and case law references
> cited from memory carry hallucination risk — verify against authoritative sources before
> relying on them.

---

## Purpose and Scope

Use this skill to produce a structured, defensible insurance coverage analysis that evaluates
whether one or more insurance policies respond to a pending or threatened claim. The output
is a coverage opinion framework supporting decisions on tendering, accepting, defending, or
denying claims, and on managing insurer relationships across a policy tower.

**Covers:**

- Policy architecture mapping: identify all potentially responsive policy types
- Coverage grant analysis: match claim allegations against each insuring agreement
- Duty to defend analysis (broader standard) vs. duty to indemnify analysis (narrower standard)
- Exclusion applicability matrix: evaluate each material exclusion against claim facts
- Notice requirement compliance and late-notice consequence analysis
- Consent-to-settle provisions and hammer clause risk
- Policy tower priority, exhaustion, and "other insurance" clause conflicts
- Reservation of rights framework: when to reserve, how to reserve, consequences of inadequate reservation
- Bad faith exposure screening: for insurer-side practitioners evaluating claims handling exposure
- Coverage opinion framework with COVERED / DISPUTED / EXCLUDED classification
- Multi-policy coordination: primary, excess, umbrella, and DIC coverage interplay
- Claims-made vs. occurrence trigger analysis including tail coverage gaps

**Does not:**

- Draft demand letters, complaints, or coverage litigation pleadings (see `legalcode-demand-letter-drafter`, `legalcode-complaint-drafter`)
- Perform full actuarial reserve analysis or loss projection (actuarial function)
- Replace a signed, formal coverage opinion from admitted coverage counsel
- Address reinsurance coverage, captive arrangements, or self-insurance programs (separate frameworks)
- Cover workers' compensation insurance, life insurance, or health insurance (distinct regulatory regimes)
- Provide legal advice or substitute for qualified counsel

**Related skills:**

- `legalcode-litigation-risk-assessment` — Evaluate the underlying claim's merits and probability of success before coverage mapping
- `legalcode-damages-calculation` — Quantify potential covered loss for reserve-setting and settlement authority
- `legalcode-indemnification-analysis` — Analyze contractual indemnity obligations that affect coverage (e.g., insured contract exception)
- `legalcode-contract-review` — Review insurance procurement contractual requirements (additional insured, waivers of subrogation)
- `legalcode-early-case-assessment` — Element-level merits analysis; feeds into coverage grant and exclusion analysis

---

## Jurisdiction and Governing Law

Insurance coverage law is highly jurisdiction-dependent. The governing law of the policy
(which may differ from the underlying claim's governing law) determines interpretation rules.
Identify the policy's governing law clause and the forum at the start of every analysis.

**[JURISDICTION-SPECIFIC] — United States**

- **Duty to defend (eight-corners rule)**: Most US states apply the "eight-corners" (or
  "four-corners") rule — compare the complaint's allegations against the policy's terms.
  Any potential coverage triggers the duty. Texas, California, Florida, and New York follow
  this majority approach. A minority of states (e.g., Indiana, Michigan in some contexts)
  permit limited extrinsic evidence. [VERIFY current state-specific rule before advising]
- **Late notice**: Approximately half of US states require the insurer to demonstrate actual
  prejudice before disclaiming on late notice grounds (CA, NY, IL, FL among them). Other
  states treat notice as a condition precedent (TX, GA). [JURISDICTION-SPECIFIC — verify state]
- **Bad faith**: Most states recognize first-party and third-party bad faith as a tort claim.
  California (Brandt v. Superior Court), Texas (Stowers doctrine for third-party cases,
  Extra-Contractual Obligations for first-party), and Florida are particularly active bad
  faith jurisdictions. Punitive damages available in many states.
- **Independent / Cumis counsel**: California's Cumis rule (San Diego Navy Federal Credit
  Union v. Cumis Insurance Society) requires insurer to pay for independent counsel when
  a reservation of rights creates a conflict of interest. Other states have analogous rules
  (NY, TX) but the trigger varies. [JURISDICTION-SPECIFIC — verify state rule]
- **Pollution exclusion**: "Absolute" and "sudden and accidental" variants. Courts split on
  whether "pollution" extends beyond traditional environmental contamination to workplace
  chemicals, indoor air quality, etc. [VERIFY jurisdiction-specific interpretation]
- **ISO form reliance**: Most US CGL policies use Insurance Services Office (ISO) standard
  forms (CG 00 01). Endorsements and manuscript changes govern where they deviate.

**[JURISDICTION-SPECIFIC] — United Kingdom**

- **Policy interpretation**: UK courts apply ordinary principles of contract construction
  (Lord Neuberger in Arnold v Britton [2015] UKSC 36; Rainy Sky SA v Kookmin Bank [2011]
  UKSC 50). Exclusions construed narrowly against the insurer (contra proferentem, though
  reduced significance post-Persimmon Homes v Ove Arup [2017]).
- **Condition precedent vs. condition subsequent**: Notice clauses in UK policies are either
  conditions precedent (breach = automatic loss of cover regardless of prejudice) or
  conditions subsequent (breach = damages for any loss caused by breach, but cover not
  automatically forfeited). Classification turns on policy wording. Courts have become
  increasingly willing to construe notice clauses as conditions subsequent. [VERIFY
  current clause wording and leading authorities]
- **FCA ICOBS (Insurance Conduct of Business Sourcebook)**: Regulates how insurers handle
  claims; requires prompt, fair, and transparent claims handling. FCA enforcement exposure
  for systematic claims handling failures.
- **Insurance Act 2015**: Replaced MIA 1906 for commercial policies. Duty of fair
  presentation (not uberrimae fidei). Proportionate remedies replace avoidance as the
  default. Contracting out permitted for non-consumer policies within limits.
- **Enterprise Act 2016**: Added s.13A Insurance Act 2015 — insurer must pay undisputed
  amounts within a reasonable time; breach gives rise to damages claim (including
  consequential losses) on top of the policy benefit.
- **Good faith post-contract**: Limited implied duty (Sprung v Royal Insurance [1997] CLC
  70 — insurers do not owe a post-contract duty of good faith that mirrors pre-contract
  obligation; but Enterprise Act 2016 has substantially changed the practical landscape).
- **Lloyd's market**: Syndicate coverage governed by Lloyd's Wordings Library and
  Subscription Agreements; consult the lead underwriter's position.

**[JURISDICTION-SPECIFIC] — Australia**

- **Insurance Contracts Act 1984 (Cth) s.54**: Most significant AU-specific rule. Insurer
  cannot refuse to pay a claim solely because the insured failed to comply with a policy
  condition (including notice), UNLESS the insurer is prejudiced by the non-compliance.
  Courts apply a two-stage test: (1) did the act/omission cause or contribute to the claim?
  (2) what is the insurer's proportionate prejudice? This effectively abolishes automatic
  forfeiture for procedural breaches in most cases. See FAI General Insurance Co Ltd v
  Australian Hospital Care [2001] HCA 38.
- **Duty of utmost good faith (ICA 1984 s.13)**: Mutual — applies both to insured and
  insurer post-contract. Insurer breach of s.13 is grounds for damages and ASIC enforcement.
- **ASIC oversight**: Australian Securities and Investments Commission regulates general
  insurers under the Corporations Act 2001 and the ASIC Act 2001. ASIC has pursued
  insurers for unconscionable conduct and misleading claims handling.
- **General Insurance Code of Practice**: Industry self-regulatory code (administered by
  the Insurance Council of Australia); binding on subscribing insurers. Sets claims
  handling timeframes (10 business days initial response, 45 days for most claims decisions).
- **Proportionate liability**: Most AU states have enacted proportionate liability regimes
  (e.g., Civil Liability Act 2002 NSW Pt 4; Wrongs Act 1958 Vic Pt IVAA) that affect how
  liability is apportioned in multi-defendant cases — relevant to coverage analysis.
- **State-based differences**: AU insurance law is largely federal (ICA 1984) but state tort
  reform statutes and compulsory third-party schemes vary.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when the answer would change the direction of analysis.

Use the structured question pattern (options with descriptions) wherever marked with
**⟁ CLARIFY** below. If the user has already provided the information, skip the question
and proceed with explicit assumption statements.

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:

- **Policy documents**: Full policy with all endorsements and declarations page
- **Claim documents**: Complaint, demand letter, or summary of allegations
- **Both**: Policy + claim documents together (preferred for complete analysis)
- **Policy type + claim description**: If full documents unavailable, proceed on available facts with explicit gap assumptions

If only partial documents are available, state clearly what is missing and how gaps affect the analysis.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning analysis, ask:

1. **Which side are you representing?**
   - Options: Policyholder/insured (coverage-maximizing lens), Insurer (coverage analysis/denial lens), Neutral coverage counsel (objective opinion), Excess carrier evaluating underlying exhaustion
   - _Why this matters_: Analysis framing, duty emphasis, and strategic recommendations flip entirely between policyholder and insurer perspectives.

2. **Jurisdiction:**
   - Options: United States (specify state), United Kingdom, Australia (specify state/territory), Other (specify), Multi-jurisdictional
   - _Why this matters_: Late notice rules, duty-to-defend standard, bad faith doctrine, and good faith duties vary materially by jurisdiction.

3. **Stage of the claim:**
   - Options: Pre-tender (coverage mapping before claim), Just tendered (initial coverage analysis), Coverage dispute pending (insurer has denied or reserved), Litigation over coverage, Claim resolved — retroactive coverage review
   - _Why this matters_: Determines whether to focus on tender strategy, reservation of rights adequacy, bad faith risk, or exhaustion mechanics.

4. **Policy types to analyze:**
   - Options (multiselect): CGL, D&O (specify Sides A/B/C), E&O/Professional Liability, Cyber/Tech E&O, EPL, Property/BI, Umbrella/Excess, Other (specify)
   - _Why this matters_: Scopes the analysis; each policy type has distinct coverage triggers and exclusion structures.

5. **Primary coverage concern:**
   - Options: Whether duty to defend is triggered, Scope of indemnity (limits, sub-limits), Exclusion applicability, Notice compliance / late notice risk, Hammer clause or consent-to-settle risk, Reservation of rights adequacy, Bad faith exposure, Exhaustion and excess triggers, Full comprehensive analysis
   - _Why this matters_: Allows the analysis to prioritize the most material issue for the user's immediate need.

If context is partial, proceed with stated assumptions.

### Step 3: Map the Policy Architecture

Before analyzing coverage, map the full policy tower:

1. **Declarations Page Review**:
   - Named insured(s) and whether the claimant triggers additional insured status
   - Policy period and whether claim falls within it
   - Retroactive date (for claims-made policies)
   - Limits of liability: per-occurrence/per-claim, aggregate, sub-limits
   - Deductible, self-insured retention (SIR), or coinsurance

2. **Policy Type and Form Identification**:
   - Identify the ISO form number or manuscript form (e.g., CG 00 01 04 13 for standard CGL)
   - List all endorsements and their effective dates
   - Identify any manuscript exclusions or bespoke coverage grants

3. **Tower Map**:
   - Primary policy (carrier, limits, self-insured retention)
   - First-level excess (follow-form vs. standalone)
   - Additional excess layers
   - Umbrella (drop-down provisions? Defense coverage?)
   - D&O Difference-in-Conditions (DIC) or Side A excess
   - Any captive or self-insured layer

4. **Claims-Made vs. Occurrence Trigger**:
   - Claims-made: Is the claim made and reported within the policy period? If not, does an ERP/tail apply?
   - Occurrence: Did the bodily injury, property damage, or wrongful act occur within the policy period?
   - If trigger is disputed, note the relevant trigger theories (exposure, manifestation, continuous, injury-in-fact) and apply the governing law's preferred theory [JURISDICTION-SPECIFIC]

**⟁ CLARIFY** — If the full policy is not available:

- "I do not have the complete policy. Should I proceed based on the ISO standard form for [policy type], noting where endorsements could change the analysis?"

### Step 4: Coverage Grant Analysis

For each potentially responsive policy, analyze whether the claim allegations fall within
the insuring agreement. Apply the applicable standard:

**US — Eight-Corners Rule (majority)**:
Compare only the complaint's allegations and the policy's insuring agreement. If any
allegation could potentially be covered, the duty to defend is triggered. Do not look
behind the allegations to the actual facts (with limited exceptions in minority states).

**UK — Ordinary Contract Construction**:
Construe the insuring agreement according to its natural meaning in context, giving effect
to commercial common sense. Consider the entire policy as a whole.

**AU — ICA 1984 + Common Law**:
Interpret policy terms consistently with ICA 1984 s.13 duty of good faith. Construe
ambiguous terms in light of reasonable expectations but not contra proferentem alone.

#### CGL Coverage Grant Analysis

Evaluate whether the claim alleges:

- **Bodily injury or property damage** caused by an **occurrence** (accident):
  - [ ] Is there alleged bodily injury (physical injury, sickness, disease, death)?
  - [ ] Is there alleged property damage (physical injury to tangible property, or loss of use)?
  - [ ] Is the cause an "occurrence" (accident — including continuous or repeated exposure)?
  - [ ] Does the injury/damage occur during the policy period? (occurrence trigger)
  - [ ] Is there a legal obligation to pay damages?

- **Personal and advertising injury** (Coverage B):
  - [ ] Does the claim allege: false arrest, malicious prosecution, wrongful eviction, slander, libel, violation of privacy rights, copyright infringement in advertising, trade dress infringement?
  - [ ] Was the injury committed in the course of advertising, publishing, broadcasting, or telecasting (for advertising injury)?
  - [ ] Does Coverage B's intentional acts exclusion (intentional violation of a person's civil rights) apply?

#### D&O Coverage Grant Analysis (Side A / Side B / Side C)

- **Side A (non-indemnifiable loss)**: Does the claim allege a **wrongful act** (error, misstatement, misleading statement, omission, neglect, breach of duty) by a **director or officer**? Is the corporation refusing or unable to indemnify (insolvency, legal prohibition on indemnification)?
- **Side B (corporate reimbursement)**: Is the corporation indemnifying directors/officers? Is the loss otherwise covered?
- **Side C (entity coverage)**: Does the claim also name the entity as a defendant? Is it a securities claim (US — Section 10(b)/Rule 10b-5, Section 11/12 claims)?
- **DIC/excess Side A**: Has underlying Side A been exhausted? Is the loss truly non-indemnifiable?

Key questions:

- [ ] Is the claimant a shareholder, regulator, employee, third party, or the entity itself?
- [ ] Is the claim a "securities claim" triggering entity coverage under Side C?
- [ ] Does the insured vs. insured exclusion apply (e.g., derivative suit — check for securities claim exception and cross-employment exceptions)?
- [ ] Is the claim for a "wrongful act" or for conduct outside the definition (e.g., bodily injury, which is CGL territory)?

#### E&O / Professional Liability Coverage Grant Analysis

- [ ] Was the wrongful act committed in the performance of **professional services** as defined in the policy?
- [ ] Is the claimant a **client** or third party? (Some E&O policies cover only client claims; others extend to third-party claims)
- [ ] Is the claim for a **negligent act, error, or omission** (E&O trigger) vs. intentional misconduct?
- [ ] Does the claim fall within the retroactive date (claims-made)?
- [ ] Is the specific professional service type covered (check Schedule of Services)?

#### Cyber / Tech E&O Coverage Grant Analysis

- **First-party coverage** (direct loss to the insured):
  - [ ] Data breach response costs (forensics, notification, credit monitoring): allocated to privacy event coverage
  - [ ] Business interruption / system failure loss (network outage, ransomware)
  - [ ] Cyber extortion / ransomware payment
  - [ ] Data restoration costs

- **Third-party coverage** (liability to third parties):
  - [ ] Privacy liability (failure to protect PII, GDPR breach liability, CCPA)
  - [ ] Network security liability (failure to prevent transmission of malware, DDoS, unauthorized access that harms third parties)
  - [ ] Technology errors and omissions (failure of the insured's tech product/service)
  - [ ] Regulatory defense and penalties (where insurable [JURISDICTION-SPECIFIC])

- [ ] Is there a war/nation-state exclusion that could apply? Following _Merck & Co. v. ACE American Insurance_ (NJ Sup. Ct. 2023 — finding the war exclusion did not apply to the NotPetya state-sponsored attack), Lloyd's issued mandatory LMA21 cyberwar exclusion requirements for all syndicates effective March 2023. Check whether the policy pre- or post-dates the mandate and which LMA endorsement version applies. [VERIFY current LMA endorsement version]

#### EPL Coverage Grant Analysis

- [ ] Does the claim allege a **wrongful employment practice** (discrimination, harassment, retaliation, wrongful termination, failure to promote, equal pay violation)?
- [ ] Is the claimant a current, former, or prospective employee? (EPL covers employees; independent contractors may be excluded)
- [ ] Does the policy cover third-party harassment claims (customer/vendor harassment of employees)?
- [ ] Does the policy cover wage-and-hour claims (FLSA, state wage laws)? (Many EPL policies exclude wage-and-hour or provide sublimited coverage)
- [ ] Does the EEOC investigation trigger the duty to defend (most EPL policies cover EEOC charges)?

#### Property Coverage Grant Analysis

- [ ] Is the damaged property **covered property** under the declarations?
- [ ] Is the cause of loss a **covered peril** (named-perils) or excluded peril (all-risk/open-perils)?
- [ ] Are business interruption / extra expense losses claimed? Is there physical damage required to trigger BI?
- [ ] Is contingent business interruption (CBI) or dependent properties coverage triggered?
- [ ] Has the waiting period / deductible been satisfied?

#### Umbrella / Excess Coverage Grant Analysis

- [ ] Has the primary policy's aggregate limit been exhausted (or is it likely to be)?
- [ ] Does the umbrella / excess policy follow form to the primary, or does it have standalone coverage?
- [ ] Does the umbrella have a **drop-down** provision for uncovered or exhausted claims?
- [ ] Is there a self-insured retention (SIR) under the umbrella before it attaches?
- [ ] Does the **other insurance** clause in the primary create a priority conflict with the umbrella?

### Step 5: Duty to Defend Analysis

The duty to defend is broader than the duty to indemnify in nearly all jurisdictions.
Analyze separately from ultimate coverage.

**Key principle**: If any allegation in the complaint could potentially give rise to covered
liability — no matter how peripheral — the insurer must defend the entire action, including
non-covered claims. The duty to defend is triggered by a possibility of coverage, not a
probability.

**Duty to defend checklist**:

1. **Trigger question**: Do any allegations in the complaint (or demand letter) potentially
   fall within the policy's insuring agreement?
   - Apply the eight-corners rule (US majority), contract construction (UK), or ICA-modified
     analysis (AU)
   - Even a single potentially covered count triggers the full duty

2. **Defense scope**: The insurer must defend all claims in the action, including uncovered
   claims, once the duty is triggered by at least one covered claim

3. **Defense cost under limits**: Are defense costs "inside" or "outside" the limits?
   - Wasting / burning limits policies: defense costs erode the indemnity limit (common in
     D&O, E&O, and some EPL forms)
   - Non-eroding coverage: defense costs separate from indemnity limits (standard CGL)

4. **Consent to retain defense counsel**: Does the insurer have the right to select defense
   counsel, or has a reservation of rights created a conflict requiring independent counsel?

5. **Withdrawal from defense**: If coverage is later determined not to exist, can the insurer
   withdraw from the defense? In most jurisdictions, this requires court approval or consent
   once a defense has been undertaken. Abrupt withdrawal may itself constitute bad faith.

6. **No-action clause**: Does the policy contain a clause prohibiting direct action by
   third parties against the insurer? (Standard in most US CGL; less common in UK/AU)

**Classification**:

- **DUTY EXISTS**: Allegations clearly trigger potential coverage
- **DUTY DISPUTED**: Coverage arguably triggered; legitimate coverage question exists
- **NO DUTY**: No allegation could potentially be covered; duty clearly not triggered

Document the specific allegation(s) that trigger (or fail to trigger) the duty to defend.

### Step 6: Exclusion Applicability Matrix

For each material exclusion in the policy, analyze whether it applies to the claim facts.
Apply the principle that **exclusions are construed narrowly** against the insurer
(US and AU), with the insurer bearing the burden of proving the exclusion applies.
In the UK, apply ordinary contract construction (Arnold v Britton; narrowing construction
less automatic but still courts generally construes exclusions contra proferentem).

#### Exclusion 1: Expected or Intended Injury (Intentional Acts)

**Scope**: Excludes bodily injury or property damage that the insured **expected or intended**
from their standpoint (not the victim's standpoint — US standard).

**Analysis questions**:

- [ ] Is there an allegation of intentional conduct? (If the complaint alleges only negligence, exclusion likely does not apply)
- [ ] Did the insured subjectively intend the injury (not just the act)?
- [ ] Does the applicable law use a subjective test (intent to cause the specific harm) or objective test?
- [ ] Are there allegations of negligent supervision or negligent hiring alongside intentional acts? (Negligent claims may survive even if intentional acts excluded)
- [ ] Does the policy contain a **separation of insureds** clause? (Each insured's conduct evaluated separately — protects innocent co-insureds)

**Common jurisdictional variations**:

- US: Subjective intent standard for the insured (not a reasonable person standard)
- UK: Deliberate or intentional acts exclusion typically requires the specific harm to be intended
- AU: ICA 1984 s.54 generally applies unless the policy expressly excludes "deliberately caused loss"

#### Exclusion 2: Contractual Liability Exclusion (with Insured Contract Exception)

**Scope**: CGL excludes liability assumed in a contract or agreement. The **insured contract
exception** restores coverage for liability assumed in an "insured contract" (typically:
leases, easements, sidetrack agreements, elevator/escalator maintenance agreements,
obligations to indemnify a municipality, and — most importantly — **any contract
pertaining to the insured's business** where the insured assumes the tort liability of
another party).

**Analysis questions**:

- [ ] Does the claim arise from a contractual obligation (e.g., indemnification clause)?
- [ ] Is the underlying contract an "insured contract" as defined in the policy?
- [ ] Is the insured assuming the **tort liability** of another (required for the exception to restore coverage) vs. purely contractual liability?
- [ ] Does the policy's definition of "insured contract" expressly include or exclude the agreement at issue?
- [ ] Is the claim one where the insured's liability exists independently of the contract (concurrence doctrine)?

#### Exclusion 3: Professional Services Exclusion (on CGL)

**Scope**: CGL excludes claims arising from the rendering or failure to render **professional
services**. Intended to push professional liability claims to E&O coverage.

**Analysis questions**:

- [ ] Did the injury arise out of the performance of professional services?
- [ ] Is the activity in question a "professional service" as defined in the exclusion (typically narrow — not all services are "professional")?
- [ ] Is there an "operations" component separate from the professional services component? (Bifurcated claims may have CGL coverage for the operations portion)
- [ ] Does the CGL have a professional services endorsement (CG 22 43 or similar) that restores some coverage?
- [ ] Is there an E&O policy that should be primary for the professional liability component?

#### Exclusion 4: Pollution Exclusion

**Scope**: Absolute pollution exclusion bars coverage for bodily injury or property damage
arising from the release of "pollutants" (typically: irritants or contaminants in solid,
liquid, gaseous, or thermal form). Courts deeply split on scope.

**Analysis questions**:

- [ ] Does the alleged harm involve a traditional environmental pollutant (industrial chemicals, waste, hazardous materials)?
- [ ] Or does it involve a non-traditional substance (CO, silica dust, lead paint, indoor chemicals, mold)?
- [ ] Which interpretation does the applicable jurisdiction follow?
  - Broad interpretation (all chemicals = pollutants — majority in some circuits)
  - Narrow interpretation (only traditional environmental pollutants — CA, NY, others)
  - [JURISDICTION-SPECIFIC — verify current state/country rule]
- [ ] Is there a "sudden and accidental" exception that restores coverage for sudden releases?
- [ ] Does a Total Pollution Exclusion (TPE) vs. a Qualified Pollution Exclusion (QPE) apply?

#### Exclusion 5: Employment-Related Practices Exclusion (on CGL)

**Scope**: CGL excludes bodily injury or personal/advertising injury to employees arising
from employment-related practices. Pushes these claims to EPL coverage.

**Analysis questions**:

- [ ] Is the claimant an employee, former employee, or applicant?
- [ ] Does the claim arise from a wrongful employment practice (discrimination, harassment, wrongful termination, failure to promote)?
- [ ] Is there a bodily injury component (e.g., emotional distress) that might be covered under CGL even for employment claims?
- [ ] Does an EPL policy respond instead?

#### Exclusion 6: Insured vs. Insured Exclusion (D&O)

**Scope**: D&O policies typically exclude claims brought by one insured against another
(e.g., company suing its own officers; derivative suits in some constructions).

**Analysis questions**:

- [ ] Is the claimant an insured (director, officer, entity)?
- [ ] Does the exclusion have a carve-out for securities claims brought derivatively by shareholders?
- [ ] Is the suit a derivative action brought by shareholders on behalf of the entity (vs. the entity directly)?
- [ ] Does the exclusion have a carve-out for employment claims by insured persons?
- [ ] Are there cross-entity scenarios (one subsidiary suing officers of another subsidiary)?

#### Exclusion 7: Prior Acts / Prior Knowledge Exclusion (Claims-Made)

**Scope**: Claims-made policies typically exclude claims arising from wrongful acts that
the insured knew of (or should have known of) before the policy's retroactive date or
inception.

**Analysis questions**:

- [ ] When did the insured first become aware of circumstances that could give rise to a claim?
- [ ] Was that awareness before the retroactive date?
- [ ] Does the policy contain a "known circumstances" endorsement that preserves coverage if circumstances were reported prior to inception?
- [ ] Is there a prior policy (or tail policy from a prior insurer) that should respond instead?

#### Exclusion 8: War / Terrorism / Cyberwar (Cyber Policies)

**Scope**: Increasingly common in cyber policies following Lloyd's LMA21 cyberwar exclusion
mandate (effective March 2023). Excludes losses attributable to war, state-sponsored attacks,
or retaliatory cyber operations by or against nation-states.

**Analysis questions**:

- [ ] Is there any indication of nation-state attribution for a cyber incident?
- [ ] Does the policy use the Lloyd's LMA21 exclusion language (mandatory for Lloyd's syndicates from 2023)?
- [ ] Is there a "sole cause" or "proximate cause" trigger for the war exclusion vs. a "contributing cause" trigger?
- [ ] Does the insured's policy pre-date the Lloyd's mandate (prior policy forms may have broader coverage)?
- [VERIFY: *Merck & Co. v. ACE American Insurance* (NJ Sup. Ct. 2023); current state of Lloyd's LMA cyberwar endorsement versions]

### Step 7: Notice Requirements Analysis

Notice obligations are among the most litigated coverage issues. Analyze each notice requirement.

**Types of notice obligations**:

1. **Notice of occurrence/claim**: Notify the insurer upon occurrence or claim (occurrence policies) or upon claim receipt/demand (claims-made)
2. **Notice of suit**: Notify the insurer when a lawsuit is filed (typically separate requirement, with shorter deadline)
3. **Notice of circumstances** (claims-made): For extended reporting period (ERP) or to preserve rights under a current policy when circumstances are known but no claim yet filed

**Analysis framework**:

| Notice Element                                      | Question                                                                                  | Finding |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------- |
| What triggered notice obligation?                   | Occurrence, claim receipt, lawsuit filed, or known circumstances?                         |         |
| When did the insured first have notice?             | Date of first knowledge of occurrence/claim                                               |         |
| When did the insured notify the insurer?            | Date of tender                                                                            |         |
| Was notice timely?                                  | Per policy language ("as soon as practicable" vs. specific deadline)                      |         |
| If late: is the jurisdiction a prejudice state?     | Insurer must show prejudice to disclaim (CA, NY, IL, FL, etc.)                            |         |
| If late: was there actual prejudice to the insurer? | Lost investigation opportunity, loss of evidence, inability to control defense            |         |
| AU — s.54 analysis                                  | Does the late notice affect the claim, and what is the insurer's proportionate prejudice? |         |
| UK — condition precedent?                           | Does the policy's notice clause operate as a condition precedent to liability?            |         |

**Late notice consequences by jurisdiction**:

- **US (prejudice states)**: Insurer must prove actual prejudice to disclaim; mere lateness insufficient
- **US (non-prejudice states)**: Late notice may void coverage automatically as a condition precedent
- **UK**: Depends entirely on whether clause is condition precedent or subsequent (construe policy language)
- **AU**: ICA 1984 s.54 provides significant relief — insurer can only reduce liability to the extent of actual prejudice
- **AU (claims-made) — s.40(3) ICA**: For claims-made policies, s.40(3) allows the insured to notify the insurer of **facts or circumstances** (not yet a formal claim) during the policy period; coverage is then preserved as if the claim arose during that period, even if the formal claim is made after expiry. The interaction of s.40(3) and s.54 is complex — courts have held they cannot be combined to cure a failure to notify altogether; the insured must strictly comply with s.40(3) while any late compliance is analysed under s.54. [VERIFY current judicial treatment in applicable AU state/territory]

### Step 8: Consent-to-Settle and Hammer Clause Analysis

Most liability policies require the insured's consent before the insurer settles a claim.
Analyze the consent-to-settle and hammer clause mechanics.

**Standard consent-to-settle language**: "The insurer shall not settle any claim without
the insured's consent. Such consent shall not be unreasonably withheld."

**Hammer clause** (also called "consent-to-settle endorsement" or "blackmail clause"):
If the insured refuses a reasonable settlement offer that the insurer is willing to accept
within policy limits, the insurer's liability is capped at the settlement amount the insurer
was prepared to pay, plus defense costs to the date of refusal.

**Analysis checklist**:

- [ ] Does the policy have a consent-to-settle clause? (Standard in D&O, E&O, EPL; also appears in CGL)
- [ ] Does the policy have a hammer clause that limits insurer exposure if the insured refuses to consent?
- [ ] What is the settlement offer on the table?
- [ ] Is the insurer's proposed settlement within policy limits?
- [ ] Has the insurer advised the insured of the hammer clause risk in writing? (Failure to warn may estop insurer from asserting it)
- [ ] Does the jurisdiction recognize the **Stowers doctrine** (or equivalent) — obligating the insurer to accept a reasonable settlement within limits to protect the insured against excess judgment? (Texas primarily; similar obligations in most US states under duty to settle)
- [ ] Has the insured rejected a within-limits settlement demand, creating insurer exposure for any excess judgment? (Stowers/bad faith exposure)
- [ ] Is there a **Coblentz agreement** scenario — insured settling without insurer consent, then assigning coverage rights to the plaintiff? [VERIFY current enforceability in applicable jurisdiction]

### Step 9: Priority, Exhaustion, and Other Insurance Analysis

When multiple policies respond to a single claim, the order of payment is critical.

**Priority principles**:

1. **Horizontal exhaustion (US majority)**: All primary policies covering the same occurrence must be exhausted before any excess policy attaches. Prevents an excess carrier from being triggered before the insured's full primary layer pays.

2. **Vertical exhaustion (emerging US doctrine)**: Each policy tower (primary + its specific excess) is exhausted vertically before the next tower. Particularly argued in environmental and mass-tort cases. [JURISDICTION-SPECIFIC — verify controlling authority]

3. **Follow-form excess**: Excess policy adopts the terms of the primary; exclusions in the primary apply to excess. Check whether the excess form modifies follow-form provisions.

4. **Standalone excess**: Excess policy has its own terms, definitions, and exclusions. May be broader or narrower than underlying. Analyze independently.

5. **Umbrella drop-down**: Umbrella may "drop down" to provide primary coverage if: (a) underlying policy limit is exhausted; (b) the claim is covered by the umbrella but not the underlying primary; (c) the primary carrier is insolvent.

**Other Insurance Clauses**: When multiple primary policies could respond:

- **Pro-rata clause**: Each insurer pays its proportionate share of the loss
- **Excess clause**: This policy pays only after other insurance is exhausted
- **Escape clause**: This policy does not apply if other insurance exists

When two policies each have "other insurance" clauses that conflict:

- Two excess clauses: typically treated as pro-rata (courts usually find impasse requires proportional contribution)
- Escape vs. excess: courts typically require the policy with the escape clause to pay first (minority view) or find them mutually repugnant (majority — treat as pro-rata)
- [JURISDICTION-SPECIFIC — verify controlling doctrine]

**Defense cost erosion analysis**:

- For wasting/burning limits policies (many D&O, E&O, EPL): Track defense cost accumulation against limits
- Estimate remaining indemnity limit after defense costs
- Advise client on when to expect exhaustion and excess policy attachment
- Alert if aggregate erosion from other claims (multi-claim situation) risks depleting coverage

### Step 10: Reservation of Rights Framework

A **reservation of rights (ROR)** letter allows the insurer to defend under a policy while
preserving the right to later deny coverage or seek reimbursement of defense costs.

**When to issue an ROR** (insurer-side analysis):

- Any potentially applicable exclusion exists, even if coverage may ultimately be found
- The facts or law are genuinely disputed
- The complaint contains covered and uncovered claims
- The policy's retroactive date or trigger is unclear
- Late notice may be a defense
- The underlying facts, if proven, might fall within an exclusion

**ROR adequacy checklist**:

- [ ] Is the ROR letter **prompt** (issued within a reasonable time after tender)? Late ROR may constitute waiver or estoppel in some jurisdictions.
- [ ] Does the ROR identify **each specific coverage defense** being reserved? (Generic reservations may not preserve specific defenses)
- [ ] Does the ROR inform the insured of the potential conflict of interest created by the reservation?
- [ ] Does the ROR advise the insured of any right to independent counsel (Cumis/independent counsel entitlement)?
- [ ] Does the ROR avoid admitting coverage obligations that have not been established?
- [ ] Is the ROR followed by a **non-waiver agreement** (written confirmation insured accepts defense without waiver of coverage defenses)?

**Consequences of inadequate ROR**:

- **Waiver**: Voluntary relinquishment of a known right (e.g., insurer asserts exclusion after agreeing to defend without ROR)
- **Estoppel**: Insured changes position in reliance on insurer's conduct; insurer precluded from later denying
- **Bad faith**: Inadequate or delayed ROR may constitute bad faith claims handling in many jurisdictions

**Independent / Cumis counsel (conflict counsel)**:
When a reservation of rights creates a conflict of interest between the insurer's interest
(proving exclusion applies) and the insured's interest (defeating the exclusion), the insured
is entitled to independent counsel at the insurer's expense in many jurisdictions.

Conflict typically arises when:

- The insurer is defending while reserving the right to later argue the insured acted intentionally (which would trigger exclusion AND constitute a defense)
- The insurer's coverage defense turns on the same factual issues as the insured's liability
- [JURISDICTION-SPECIFIC — verify Cumis entitlement in applicable jurisdiction; strongest in CA, recognized in NY, TX, others]

### Step 11: Bad Faith Exposure Analysis

**Note**: Bad faith analysis is conducted from the insurer's perspective (exposure screening)
or the policyholder's perspective (potential claim). Label clearly which lens is applied.

#### US Bad Faith Framework

**First-party bad faith** (insurer's handling of direct claims):

- Insurer must conduct a **reasonable investigation** before denying or delaying payment
- Must acknowledge, investigate, and pay or deny within **reasonable time** (many states have specific statutory deadlines)
- Unreasonable denial of a covered claim = bad faith
- Remedy: policy benefits + consequential damages + attorneys' fees (statutory in many states) + **punitive damages** where conduct is "oppressive, fraudulent, or malicious" (CA, TX, FL, others)

**Third-party bad faith** (failure to settle within limits):

- Stowers doctrine (TX) and equivalent duty in most states: Insurer must accept a reasonable settlement demand within policy limits when liability appears reasonably clear and demand is within limits
- Failure to do so subjects insurer to the entire excess judgment, regardless of policy limits
- Key Stowers elements (Texas): (1) claim within policy coverage; (2) demand within policy limits; (3) demand reasonable under the circumstances
- Distinguish: insurer's duty to settle ≠ absolute duty to accept any settlement demand; insurer retains right to make reasonable tactical decisions

**Statutory bad faith** (UIPA / UCPA):

- Most states have Unfair Claims Practices Acts imposing specific claims handling obligations
- Systematic violations may support bad faith, class actions, or regulatory action
- [JURISDICTION-SPECIFIC — verify applicable statute and private right of action]

**Bad faith exposure checklist** (insurer-side):

- [ ] Was the coverage denial supported by a reasonable investigation?
- [ ] Were coverage defenses asserted in good faith (even if ultimately unsuccessful)?
- [ ] Were statutory claims handling deadlines met?
- [ ] Was the insured kept reasonably informed throughout the process?
- [ ] Was a reasonable within-limits settlement demand rejected without adequate consideration?
- [ ] Has the claim been pending unreasonably long without resolution?

#### UK Bad Faith / Good Faith Framework

- Post-contract implied duty of good faith is significantly narrower than US bad faith doctrine
- **Enterprise Act 2016** (s.13A Insurance Act 2015): Insurer must pay undisputed sums within a **reasonable time**; breach gives rise to a damages claim (including consequential losses) beyond just the policy amount
- No punitive damages generally available in UK commercial insurance disputes
- FCA ICOBS enforcement for systematic failure to handle claims fairly

#### AU Good Faith Framework

- ICA 1984 **s.13**: Mutual duty of utmost good faith. Insurer breach = entitlement to damages.
- **ASIC enforcement** under Corporations Act and ASIC Act for unconscionable conduct
- General Insurance Code of Practice: subscribing insurers must resolve most claims within 45 business days
- Court-awarded damages for breach of duty of good faith may include consequential losses

---

## Coverage Classification Framework

Classify each coverage position using the three-tier system:

| Classification | Definition                                                                                                              | Recommended Action                                                                                    |
| -------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **COVERED**    | Claim clearly falls within the insuring agreement; no exclusion applies; duty to defend and/or indemnify exists         | Acknowledge coverage; assign counsel; begin defense                                                   |
| **DISPUTED**   | Coverage arguably exists; legitimate question on trigger, exclusion, scope, or duty; reasonable arguments on both sides | Issue ROR; defend under reservation; seek declaratory judgment if needed                              |
| **EXCLUDED**   | Exclusion clearly bars coverage; duty to defend and indemnify do not exist; coverage defense is strong                  | Issue denial letter with specific exclusion identification; consult bad faith exposure before denying |

Apply classification separately to:

1. **Duty to defend** (broader standard)
2. **Duty to indemnify** (narrower standard)
3. **Each coverage part** (Coverage A, B, Coverage B Side A/B/C, etc.)

---

## Prioritization Framework

### Tier 1 — Immediate Action (Do First)

| Priority | Coverage Issue               | Rationale                                                                   |
| -------- | ---------------------------- | --------------------------------------------------------------------------- |
| **P1**   | Notice deadline compliance   | Missing a notice deadline can void all coverage; irreversible               |
| **P1**   | Duty to defend trigger       | Must defend promptly; failure to defend = potential waiver and bad faith    |
| **P1**   | Reservation of rights letter | If coverage is disputed, ROR must be issued promptly to preserve defenses   |
| **P1**   | Consent-to-settle deadline   | Hammer clause deadlines can cap insurer exposure or destroy insured's claim |

### Tier 2 — Near-Term Priority (Resolve within 30 Days)

| Priority | Coverage Issue                      | Rationale                                                                           |
| -------- | ----------------------------------- | ----------------------------------------------------------------------------------- |
| **P2**   | Exclusion applicability             | May narrow or eliminate defense obligation and indemnity exposure                   |
| **P2**   | Cumis / independent counsel trigger | Entitlement accrues from the moment conflict exists; delay = prejudice to insured   |
| **P2**   | Exhaustion analysis                 | Affects when excess layers are triggered; coordinate with excess carriers early     |
| **P2**   | Bad faith exposure screen           | Identify any practices that could convert a coverage dispute into punitive exposure |

### Tier 3 — Background Analysis (Resolve before Indemnity Decision)

| Priority | Coverage Issue                         | Rationale                                                               |
| -------- | -------------------------------------- | ----------------------------------------------------------------------- |
| **P3**   | Limits and sub-limits mapping          | Critical for reserve-setting; impacts settlement authority              |
| **P3**   | Defense cost erosion projection        | For burning-limits policies; track against aggregate                    |
| **P3**   | Coverage for anticipated counterclaims | If insured is asserting claims, those may not be covered losses         |
| **P3**   | Subrogation preservation               | Preserve insurer's subrogation rights before settlement forecloses them |

---

## Citation Quality Gates

Run these five gates silently before delivering any coverage opinion output. If any gate
fails, revise before delivering.

| Gate           | Rule                                                                                                   | Fail Action                                               |
| -------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------- |
| **Source**     | Every legal proposition cites a specific statute, regulation, ISO form number, or established doctrine | Add citation or mark "[UNVERIFIED]"                       |
| **Format**     | Citations follow a recognizable format for the jurisdiction (US — Bluebook; UK — OSCOLA; AU — AGLC)    | Fix format                                                |
| **Currency**   | Every cited statute or case has been checked for subsequent amendments or overruling                   | Flag "[CHECK CURRENCY]"                                   |
| **Domain**     | Analysis stays within the identified governing law; no inadvertent jurisdiction bleed                  | Remove or flag "[JURISDICTION-SPECIFIC — check]"          |
| **Confidence** | Uncertainty is stated explicitly, not hidden in assertive language                                     | Add confidence qualifier per the Confidence Scoring scale |

---

## Self-Interrogation for High-Severity Coverage Positions

For any finding classified **EXCLUDED** (coverage denial recommendation), apply this
three-pass adversarial review before finalizing:

**Pass 1 — Coverage Grant Chain**: Does the exclusion clearly and unambiguously apply to
the claim as alleged? Is the language of the exclusion plain, or is it susceptible to a
construction that preserves coverage? (Remember: exclusions are construed narrowly against
the insurer in most jurisdictions.)

**Pass 2 — Completeness**: Have all potentially responsive policies been analyzed? Is there
an excess, umbrella, or DIC policy that might respond even if the primary does not? Have
all endorsements been reviewed for exceptions to the exclusion?

**Pass 3 — Challenge**: What is the strongest argument a competent coverage counsel for
the insured would make? Under what construction of the policy, or under what jurisdictional
rule, might coverage be found? Has the analysis accounted for the prejudice requirement
for late notice (if applicable), and for ICA 1984 s.54 (if AU law applies)?

If the analysis does not survive all three passes at high confidence, downgrade from
**EXCLUDED** to **DISPUTED** and recommend seeking a declaratory judgment.

---

## Confidence Scoring

| Level        | Range     | Meaning                                                       | Action                                                    |
| ------------ | --------- | ------------------------------------------------------------- | --------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, clear policy language, plain application         | State with confidence                                     |
| **High**     | 0.80–0.94 | Strong authority, minor interpretive questions                | State with brief caveat                                   |
| **Probable** | 0.60–0.79 | Good arguments, some contrary authority or ambiguous language | State with reasoning and contra-indicators                |
| **Possible** | 0.40–0.59 | Genuinely uncertain; reasonable arguments on both sides       | Flag for coverage counsel review; present both sides      |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative position                              | Do not assert; flag "[UNCERTAIN — seek coverage counsel]" |

---

## Glass Box Audit Trail

Every coverage analysis delivered by this skill must include a Glass Box audit block
documenting the analysis basis and limitations:

```yaml
glass_box:
  skill_name: "legalcode-insurance-coverage-analysis"
  analysis_date: "[YYYY-MM-DD]"
  perspective: "Policyholder / Insurer / Neutral / Excess carrier"
  jurisdiction: "[US-[State] / UK / AU-[State] / Multi-jurisdictional]"
  governing_law_of_policy: "[Jurisdiction per policy choice-of-law clause]"
  policies_analyzed:
    - type: "[CGL / D&O / E&O / Cyber / EPL / Property / Umbrella/Excess]"
      carrier: "[Carrier name or 'Not identified']"
      policy_period: "[YYYY-MM-DD to YYYY-MM-DD]"
      trigger: "[Claims-made / Occurrence]"
      limits: "[Per occurrence/claim and aggregate]"
  claim_stage: "[Pre-tender / Tendered / Reservation / Denial / Coverage litigation]"
  documents_reviewed:
    - "[List policy forms, endorsements, complaint, demand letter reviewed]"
  documents_not_reviewed:
    - "[List missing documents that affect analysis completeness]"
  coverage_classifications:
    duty_to_defend: "COVERED / DISPUTED / EXCLUDED"
    duty_to_indemnify: "COVERED / DISPUTED / EXCLUDED"
    material_exclusions_triggered: "[List exclusions analyzed and findings]"
  notice_compliance: "TIMELY / LATE-EXCUSABLE / LATE-PREJUDICIAL / UNKNOWN"
  legalcode_mcp: "Connected / Not connected"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  confidence_overall: "HIGH / MEDIUM / LOW"
  limitations:
    - "[List any policy documents not reviewed, jurisdiction uncertainty, or gaps]"
  reviewer: "AI-assisted — requires review by qualified coverage counsel before reliance"
```

---

## Anti-Patterns

What NOT to do in insurance coverage analysis:

1. **Conflating duty to defend with duty to indemnify**: These are distinct obligations with
   different standards. The duty to defend is triggered by potentially covered allegations;
   the duty to indemnify requires actual covered liability. Treating them identically
   understates the defense obligation and overstates the indemnity obligation.

2. **Applying the same notice rule to every jurisdiction**: Notice as a condition precedent
   (automatic forfeiture) vs. prejudice requirement varies by jurisdiction, and even by state
   within the US. Always verify the specific jurisdiction's rule before recommending a late-
   notice defense.

3. **Ignoring the eight-corners rule and looking at actual facts**: In most US states, the
   duty to defend is determined solely by comparing the complaint to the policy — actual facts
   are irrelevant. Importing facts not in the complaint to defeat the duty to defend is a
   common error (and in some states, a bad faith violation).

4. **Overlooking the insured contract exception to the contractual liability exclusion**:
   The CGL contractual liability exclusion has a broad exception for "insured contracts"
   (including any contract pertaining to the insured's business where the insured assumes
   another's tort liability). Failing to analyze the exception leads to over-denying coverage
   on contractual indemnification claims.

5. **Applying the pollution exclusion too broadly**: Courts are deeply split on whether the
   absolute pollution exclusion reaches non-traditional pollutants (workplace chemicals, CO,
   lead paint, mold). Always verify the specific jurisdiction's scope of the exclusion before
   relying on it to deny coverage.

6. **Failing to issue a timely reservation of rights**: Delay in issuing an ROR can constitute
   waiver or estoppel of coverage defenses in many jurisdictions. Prompt issuance is a
   mandatory habit in coverage analysis — not optional.

7. **Issuing a generic ROR that does not identify specific defenses**: A reservation that says
   "we reserve all rights under the policy" without identifying specific coverage questions
   may not preserve those defenses. Specificity is required.

8. **Forgetting to analyze the Cumis/independent counsel trigger**: When a reservation of rights
   creates a conflict between the insurer's and insured's interests on factual issues, the
   insured is entitled to independent counsel at the insurer's expense in many jurisdictions.
   Failure to address this can constitute bad faith.

9. **Treating excess and umbrella policies identically**: Umbrella policies often have
   independent coverage grants (and drop-down provisions) that differ from straight excess
   policies. Analyze each separately using its own terms.

10. **Missing the hammer clause risk on consent-to-settle**: If the insured refuses a
    reasonable settlement within limits, the hammer clause may cap the insurer's exposure
    at the refused settlement amount. Failure to flag this risk for the insured or to
    document the insurer's recommendation is a litigation/malpractice trap.

11. **Ignoring wasting/burning limits in D&O and E&O policies**: Defense costs erode the
    indemnity limits in most D&O, E&O, and EPL policies. Failing to track and project this
    erosion leads to surprise exhaustion of limits before the underlying case resolves.

12. **Applying the insured vs. insured exclusion without analyzing exceptions**: Most D&O
    insured-vs.-insured exclusions have exceptions for derivative suits, securities claims,
    and employment claims. The exclusion often appears broad but is substantially narrowed
    by its exceptions.

13. **Not checking for the Lloyd's LMA21 cyberwar exclusion on cyber policies post-March 2023**:
    All Lloyd's syndicates are required to include cyberwar exclusions (LMA21) on cyber
    policies issued after March 2023. This materially affects coverage for state-sponsored
    cyberattacks. [VERIFY current Lloyd's requirements]

14. **Ignoring AU Insurance Contracts Act 1984 s.54 when advising on Australian policies**:
    Section 54 provides broad relief against automatic forfeiture for procedural breaches.
    Failure to account for s.54 leads to incorrect coverage denials and potential ICA 1984 s.13
    good faith violations.

15. **Treating the professional services exclusion on CGL as absolute**: The exclusion is
    narrow — it applies only to claims arising from the rendering of professional services.
    Operations-based claims (bodily injury or property damage from the insured's premises or
    activities, not from the professional service itself) remain covered. Bifurcate claims
    carefully.

16. **Failing to coordinate across the policy tower early**: Excess carriers have their own
    notice obligations and consent rights. Delayed notification to excess carriers (even if
    primary coverage is clear) can jeopardize excess coverage when the claim ultimately
    exhausts primary limits.

17. **Confusing "claims-made" reporting deadlines with "occurrence" policies**: For claims-made
    policies, both the claim and the report to the insurer must occur within the policy period
    (or ERP). Reporting a claim one day after policy expiration — absent an ERP — may forfeit
    all coverage even if the wrongful act occurred years before. This is the single most
    catastrophic notice trap in insurance coverage.

18. **Not screening for bad faith exposure before issuing a coverage denial**: In jurisdictions
    with robust bad faith doctrines (CA, TX, FL), a coverage denial that is later found to be
    unreasonable can result in extra-contractual damages and punitive damages far exceeding
    the original policy limits. Always screen bad faith exposure before recommending denial.

19. **Overlooking the Enterprise Act 2016 (UK) when advising on payment delays**: Under s.13A
    Insurance Act 2015 (as added by the Enterprise Act 2016), UK insurers who fail to pay
    undisputed claims within a reasonable time face damages claims beyond the policy amount.
    Advisers treating delay as cost-free are out of date with UK law.

20. **Assuming every "other insurance" clause conflict resolves with the excess clause prevailing**:
    When two policies each contain excess or escape clauses, courts typically treat them as
    mutually repugnant and impose pro-rata allocation. The outcome varies by jurisdiction and
    clause type. Always analyze the specific "other insurance" language and verify the applicable
    jurisdictional rule.

---

## Writing Standards

Before delivering any coverage analysis output, apply these quality gates:

1. **Plain language for coverage positions**: Classify each issue plainly (COVERED /
   DISPUTED / EXCLUDED) before detailed reasoning. Do not bury the conclusion in analysis.

2. **Separate duty to defend from duty to indemnify**: Always address these as distinct
   obligations with separate sections and classifications.

3. **Cite the policy language**: Every exclusion or coverage finding must reference the
   specific policy language being interpreted. Do not paraphrase policy terms without
   quotation.

4. **State jurisdiction explicitly**: For every jurisdictionally variable rule (late notice,
   bad faith, Cumis, pollution exclusion scope), identify the jurisdiction being applied and
   note if other jurisdictions would reach a different result.

5. **Flag missing documents**: If the analysis is based on incomplete policy information,
   prominently disclose what is missing and how it affects conclusions.

6. **No false precision**: Do not express a definitive coverage position (COVERED or EXCLUDED)
   on a genuinely uncertain issue. Use DISPUTED with a confidence score.

7. **Audience calibration**: Calibrate the level of detail and terminology to the reader —
   coverage opinion vs. executive summary vs. board briefing require different registers.

8. **Recommendation, not just analysis**: Every output must conclude with specific
   recommended actions, not just findings.

---

## External Tool Integration

**With legalcode-mcp connected (preferred)**:

- Search for current jurisdiction-specific late-notice, bad faith, and pollution exclusion
  case law in the applicable state/country
- Verify that cited statutes and cases are current and have not been overruled or amended
- Search for ISO form version history to confirm the applicable form's exclusion language
- Mark legalcode-mcp-verified citations as [VERIFIED]
- Note in Glass Box: `legalcode_mcp: "Connected"`

**Without legalcode-mcp**:

- Mark all statutory and case law references [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed with structural analysis, coverage framework, and exclusion matrix
- Recommend that coverage counsel independently verify all legal authority before reliance

**Perplexity / WebSearch (supplemental)**:

- Use for ISO form research, recent regulatory guidance, and market standard practices
- Use for verifying recent legislative developments (e.g., Lloyd's LMA21 mandate, Enterprise Act 2016 developments)
- Do not rely on web search alone for jurisdiction-specific case law — verify through primary sources

---

## Output Format Template

Deliver coverage analysis using the following template. Adapt sections based on which
policy types and coverage issues are relevant to the specific claim.

---

````markdown
# Insurance Coverage Analysis

**Claim**: [Brief description of the underlying claim]
**Claimant**: [Claimant name or role]
**Insured / Policyholder**: [Insured name]
**Date of Analysis**: [YYYY-MM-DD]
**Perspective**: [Policyholder / Insurer / Neutral / Excess carrier]
**Jurisdiction**: [Governing law jurisdiction]
**Prepared by**: AI-assisted (legalcode-insurance-coverage-analysis) — requires coverage counsel review

---

## 1. Executive Summary

[3–5 sentences summarizing: (1) which policies are triggered, (2) whether the duty to defend
exists, (3) the most material coverage issue, and (4) the recommended immediate action.]

**Overall Coverage Position**: COVERED / DISPUTED / EXCLUDED
**Confidence**: [HIGH / MEDIUM / LOW] ([0.XX])
**Immediate Action Required**: [Yes/No — specify if yes]

---

## 2. Policy Tower Map

| Layer         | Carrier | Policy Type | Limits | Trigger | Period |
| ------------- | ------- | ----------- | ------ | ------- | ------ |
| Primary       |         |             |        |         |        |
| First Excess  |         |             |        |         |        |
| Second Excess |         |             |        |         |        |
| Umbrella      |         |             |        |         |        |

---

## 3. Coverage Grant Analysis

### [Policy Type 1 — e.g., CGL]

**Coverage Position**: COVERED / DISPUTED / EXCLUDED
**Confidence**: [0.XX]

**Insuring Agreement**: [Quote relevant language]
**Claim Allegations**: [Match allegations to insuring agreement]
**Analysis**: [Step through coverage grant elements]
**Finding**: [Whether allegations fall within or outside the insuring agreement]

### [Policy Type 2 — e.g., D&O]

[Repeat structure]

---

## 4. Duty to Defend

**Position**: COVERED (duty exists) / DISPUTED / EXCLUDED (no duty)
**Standard Applied**: [Eight-corners (US) / Contract construction (UK) / ICA 1984 (AU)]
**Triggering Allegations**: [Specific allegations that potentially trigger coverage]

**Defense Cost Structure**: [Inside/outside limits; wasting policy?]
**Counsel**: [Insurer-appointed / Independent Cumis counsel required / TBD]

---

## 5. Exclusion Analysis

| Exclusion                     | Potentially Applicable? | Analysis | Finding                             | Confidence |
| ----------------------------- | ----------------------- | -------- | ----------------------------------- | ---------- |
| Expected/Intended             | Yes / No                |          | APPLIES / DOES NOT APPLY / DISPUTED |            |
| Contractual Liability         | Yes / No                |          |                                     |            |
| Professional Services         | Yes / No                |          |                                     |            |
| Pollution                     | Yes / No                |          |                                     |            |
| Employment Practices          | Yes / No                |          |                                     |            |
| [Other applicable exclusions] |                         |          |                                     |            |

**Material Exclusion Finding**: [Summarize which exclusions, if any, bar coverage]

---

## 6. Notice Analysis

| Element                          | Finding                       |
| -------------------------------- | ----------------------------- |
| Trigger date                     |                               |
| Insured's knowledge date         |                               |
| Tender date                      |                               |
| Notice timely?                   | Yes / No                      |
| If late: prejudice jurisdiction? | Yes / No ([State/Country])    |
| Prejudice demonstrated?          | Yes / No / Unknown            |
| Coverage impact of late notice   | None / Disputed / Significant |

---

## 7. Consent-to-Settle / Hammer Clause

**Consent-to-settle required?** Yes / No
**Hammer clause present?** Yes / No
**Current settlement demand**: [Amount, if applicable]
**Hammer clause risk**: [None / Low / High — explain]
**Recommendation**: [Accept / Reject / Negotiate — with reasoning]

---

## 8. Policy Tower Priority and Exhaustion

**Exhaustion doctrine**: [Horizontal / Vertical — per jurisdiction]
**Primary policy status**: [Active / Near exhaustion / Exhausted]
**Next excess trigger**: [Amount required to trigger excess; expected timeline]
**Excess carriers notified**: Yes / No / Pending
**Defense cost erosion**: [Remaining indemnity limit after defense costs; projected exhaustion date]

---

## 9. Reservation of Rights

**ROR Required?** Yes / No
**ROR Issued?** Yes (date) / No / Pending
**ROR Adequacy**: [Adequate / Deficient — specify gaps]
**Cumis Counsel Triggered?** Yes / No / Jurisdiction-dependent
**Action Required**: [Issue ROR by (date) / Identify independent counsel / No action needed]

---

## 10. Bad Faith Exposure Screen

**Jurisdiction's bad faith framework**: [Brief summary]
**Current exposure**: LOW / MEDIUM / HIGH
**Basis**: [Specific conduct or inaction creating exposure, if any]
**Mitigation actions**: [Steps to reduce bad faith exposure]

---

## 11. Coverage Findings Summary

| Issue              | Classification                             | Confidence | Priority |
| ------------------ | ------------------------------------------ | ---------- | -------- |
| Duty to Defend     | COVERED / DISPUTED / EXCLUDED              | [0.XX]     | P1       |
| Duty to Indemnify  | COVERED / DISPUTED / EXCLUDED              | [0.XX]     | P2       |
| [Exclusion 1]      | APPLIES / DISPUTED / DOES NOT APPLY        | [0.XX]     | P1/P2/P3 |
| Notice Compliance  | TIMELY / LATE-EXCUSABLE / LATE-PREJUDICIAL | [0.XX]     | P1       |
| Hammer Clause Risk | LOW / MEDIUM / HIGH                        | [0.XX]     | P1/P2    |
| Bad Faith Exposure | LOW / MEDIUM / HIGH                        | [0.XX]     | P2       |

---

## 12. Recommended Actions

**Immediate (within 48–72 hours):**

1. [Action 1]
2. [Action 2]

**Near-term (within 30 days):**

1. [Action 1]
2. [Action 2]

**Background:**

1. [Action 1]
2. [Action 2]

---

## 13. Glass Box Audit Trail

```yaml
[Insert completed Glass Box YAML block]
```
````

---

## 14. Limitations and Caveats

[List specific limitations: missing documents, unverified authority, jurisdictional gaps,
issues reserved for qualified coverage counsel.]

> **This analysis does not constitute a legal opinion or coverage opinion from qualified
> coverage counsel. Do not communicate any coverage position to any party, issue a denial
> letter, or settle any claim without review by qualified insurance attorneys licensed in
> the applicable jurisdiction.**

```

---

## Localization Notes

When localizing for a specific jurisdiction:
- **US state**: Verify the specific state's: (a) notice-as-condition-precedent vs. prejudice rule; (b) eight-corners rule or extrinsic evidence exceptions; (c) bad faith statutory framework; (d) Cumis/independent counsel entitlement; (e) pollution exclusion scope; (f) anti-subrogation statutes.
- **UK**: Verify Insurance Act 2015 (duty of fair presentation, proportionate remedies); Insurance Act 2015 s.13A / Enterprise Act 2016 (timely payment); whether policy is consumer or commercial; applicable FCA ICOBS obligations.
- **Australia**: Apply ICA 1984 s.54 to all late-notice and procedural compliance issues; s.13 good faith duty; General Insurance Code of Practice handling timelines; verify state tort reform statutes affecting proportionate liability in underlying case.
- **Canada**: [JURISDICTION-SPECIFIC — verify provincial vs. federal insurance Act; duty of good faith; Quebec civil law vs. common law provinces for policy interpretation; provincial unfair claims practices regulations]
- **EU / Continental Europe**: [JURISDICTION-SPECIFIC — verify Solvency II implementation; applicable national insurance contract law; EU Insurance Distribution Directive; jurisdiction of EIOPA guidance]

---

## Provenance

Created by Legalcode (2026-03-02). Legalcode original synthesis based on US, UK, and
Australian insurance coverage law, ISO CGL form architecture, D&O/E&O/Cyber policy market
standards, Lloyd's market practice (including LMA21 cyberwar exclusion), ICA 1984
(Australia), Insurance Act 2015 and Enterprise Act 2016 (UK), and Legalcode quality
frameworks drawn from `legalcode-contract-review` and `legalcode-litigation-risk-assessment`
reference standards. No external skill imports — original synthesis from primary law and
market practice sources.
```
