---
name: legalcode-complaint-drafter
description: Drafts civil complaints, petitions, and originating applications by mapping client facts
  to the legal elements of each cause of action. Validates plausibility under Twombly/Iqbal (US federal),
  applies heightened pleading for fraud (Rule 9(b)) and securities claims (PSLRA), and structures jurisdictional
  allegations, factual narratives, causes of action, and prayer for relief. Supports US federal, state,
  England & Wales (Particulars of Claim under CPR Part 16), and Australia (Statement of Claim under Federal
  Court Rules). Produces court-ready complaints with numbered paragraphs, element-mapped causes of action,
  exhibit references, and verification where required. Includes pre-suit requirement checks, Rule 11 compliance
  validation, and strategic claim selection guidance.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Complaint Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted complaint
> drafting. It does not constitute legal advice. All outputs must be reviewed,
> verified, and signed by qualified legal counsel licensed in the relevant
> jurisdiction before filing with any court. Procedural rules, pleading
> standards, and case law change frequently; verify all authoritative sources
> before relying on any conclusion. AI-generated pleadings may contain errors
> in element identification, jurisdictional analysis, or factual
> characterization — all allegations must be verified against actual evidence
> and client instructions. Any cited authority marked `[VERIFY]` has not been
> independently validated and must be confirmed before reliance. Filing a
> complaint constitutes a Rule 11 / professional conduct certification that
> the claims are well-grounded in fact and law.

---

## Purpose and Scope

This skill drafts civil complaints and equivalent originating pleadings by
systematically mapping client facts to the legal elements of each cause of
action, structuring jurisdictional and venue allegations, building a
persuasive factual narrative, and formatting the document for court filing.

The skill operates in two primary modes:

1. **Full Draft Mode**: Generates a complete, court-ready complaint from
   client facts, instructions, and legal research — including caption,
   jurisdictional allegations, parties, factual narrative, causes of action
   (each element-mapped), prayer for relief, jury demand, and certificates.

2. **Element Validation Mode**: Takes an existing draft complaint and
   validates it against pleading standards — checking each cause of action
   for element completeness, verifying Twombly/Iqbal plausibility, flagging
   Rule 9(b) compliance issues for fraud claims, and identifying missing
   jurisdictional allegations.

**Covers:**

- **Element mapping**: Systematic identification and pleading of every element for each cause of action
- **Plausibility validation**: Twombly/Iqbal analysis for each claim (US federal)
- **Heightened pleading**: Rule 9(b) fraud specificity, PSLRA scienter requirements
- **Jurisdictional analysis**: Federal question, diversity, supplemental jurisdiction, personal jurisdiction, venue
- **Complaint structure**: Caption, parties, facts, counts, prayer, certificates — properly formatted
- **Pre-suit requirements**: Administrative exhaustion (EEOC), tort claims notices, certificates of merit, demand letters
- **Claim selection**: Strategic guidance on which claims to include, alternative pleading, preservation
- **Class action**: Rule 23 class allegations when applicable
- **Multi-defendant**: Proper attribution of conduct to specific defendants
- **Remedies**: Compensatory, punitive, equitable, statutory, and injunctive relief
- **Cross-jurisdictional**: US federal, US state, England & Wales (Particulars of Claim), Australia (Statement of Claim)

**Does not:**

- Replace counsel's professional judgment on claim viability or litigation strategy
- Certify compliance with Rule 11 (only counsel may sign and certify)
- Conduct independent factual investigation or verify client representations
- Provide final legal opinions on the merits of claims
- File documents with any court
- Determine whether evidence is admissible
- Make ethical judgments about claim merit (flags concerns for counsel review)

**Related skills:**

- `legalcode-brief-analyzer` — Analyzes briefs for argument strength and authority quality
- `legalcode-damages-calculation` — Structures damages calculations for prayer for relief
- `legalcode-early-case-assessment` — Pre-filing case evaluation and strategy
- `legalcode-case-timeline-builder` — Builds chronologies from document corpora
- `legalcode-discovery-request-drafter` — Drafts discovery after complaint is filed

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic at baseline. Identify the forum, governing
procedural rules, and substantive law first, then adapt complaint format,
pleading standards, and element definitions accordingly.

**[JURISDICTION-SPECIFIC]** Localize at minimum:

- Pleading standard (notice pleading, fact pleading, plausibility)
- Complaint format and required sections
- Heightened pleading requirements (fraud, securities, specific claim types)
- Pre-suit requirements (administrative exhaustion, notices, certificates)
- Jurisdictional allegation requirements
- Party identification conventions
- Verification/statement of truth requirements
- Damages pleading restrictions (ad damnum rules)
- Service of process requirements and timing
- Statute of limitations / limitation periods
- Filing fees and fee waiver procedures

**Reference anchors frequently needed:**

- **U.S. federal**: FRCP Rules 3, 4, 7, 8, 9, 10, 11, 12, 15, 23, 38, 65; 28 USC 1331-1367, 1391, 1441; Twombly (550 U.S. 544 (2007)); Iqbal (556 U.S. 662 (2009)) [VERIFY]
- **England & Wales**: CPR Part 7 (claim form), Part 16 (statements of case), PD 16; Limitation Act 1980; CPR Part 25 (interim remedies) [VERIFY]
- **Australia**: Federal Court Rules 2011 (Cth) Div 5.1-5.4; Limitation Acts (state/territory); General Steel Industries v Commissioner for Railways (1964) 112 CLR 125 [VERIFY]
- **Canada**: Federal Courts Rules SOR/98-106 Part 4; provincial rules vary; Limitation Acts [VERIFY]

---

## Interactive Clarification

Use interactive clarification whenever the answer materially changes claim
selection, complaint structure, or drafting approach. If information is already
provided, skip the question. Proceed with stated defaults when the user does
not respond.

**CLARIFY block 1: Drafting mode**

- Options: `full draft (from client facts)`, `element validation (review existing draft)`, `amendment drafting (add claims/parties to existing complaint)`
- Default: `full draft (from client facts)`
- Why it matters: Full draft builds from scratch; validation mode audits an existing complaint; amendment mode adds to an existing pleading under Rule 15.

**CLARIFY block 2: Court and jurisdiction**

- Options: `U.S. federal district court (specify)`, `U.S. state court (specify)`, `England & Wales High Court`, `England & Wales County Court`, `Australia Federal Court`, `Australia state court (specify)`, `other (specify)`
- Default: `U.S. federal district court`
- Why it matters: Determines pleading standard (plausibility vs. fact pleading vs. notice), complaint format, required sections, and applicable rules. Some state courts use different standards than federal.

**CLARIFY block 3: Subject matter jurisdiction basis (US federal only)**

- Options: `federal question (28 USC 1331)`, `diversity (28 USC 1332)`, `both federal question and diversity`, `supplemental (28 USC 1367)`, `CAFA (28 USC 1332(d))`, `removal (already removed from state court)`, `N/A (state court or non-US)`
- Default: `federal question (28 USC 1331)`
- Why it matters: Determines jurisdictional allegations, amount-in-controversy requirements, citizenship pleading, and whether supplemental jurisdiction is needed for state-law claims.

**CLARIFY block 4: Claim types (multi-select)**

- Options: `contract claims`, `tort claims (negligence, fraud, etc.)`, `employment claims (discrimination, retaliation, wrongful termination)`, `IP claims (patent, copyright, trademark, trade secret)`, `securities claims`, `antitrust claims`, `civil rights claims`, `class action`, `statutory claims (specify)`, `other (specify)`
- Default: Determined from client facts
- Why it matters: Each claim type has different elements, pleading standards, pre-suit requirements, and remedies. Fraud and securities claims require heightened pleading.

**CLARIFY block 5: Client materials available**

- Options: `written narrative/summary`, `documents and evidence`, `prior correspondence/demand letters`, `client interview notes`, `existing draft complaint`, `opposing party's prior filings`, `all of the above`
- Default: `written narrative/summary`
- Why it matters: More materials enable better fact-specific pleading. Documents allow direct exhibit attachment. Prior correspondence may establish pre-suit demand.

**CLARIFY block 6: Strategic preferences**

- Options: `aggressive (maximum claims, punitive damages, injunctive relief)`, `measured (strong claims only, proportionate relief)`, `conservative (safest claims, minimal sanctions risk)`, `preservation (include claims to preserve for amendment/discovery)`
- Default: `measured (strong claims only, proportionate relief)`
- Why it matters: Affects claim selection, alternative pleading approach, and prayer for relief scope. Aggressive may include weaker claims; conservative omits marginal claims.

**CLARIFY block 7: Special complaint types**

- Options: `standard complaint`, `class action complaint`, `qui tam / False Claims Act`, `shareholder derivative`, `RICO`, `multi-district litigation`, `counterclaim / cross-claim / third-party complaint`, `amended complaint`
- Default: `standard complaint`
- Why it matters: Each type has additional structural requirements beyond a standard complaint. Class actions need Rule 23 allegations; qui tam has seal requirements; derivatives need demand futility.

**CLARIFY block 8: Jury demand**

- Options: `yes — jury trial demanded`, `no — bench trial preferred`, `determine from claims (some claims jury, some equity)`
- Default: `yes — jury trial demanded`
- Why it matters: Jury demand must be made in the complaint or within 14 days of the last pleading (FRCP 38). Failure to demand may waive the right. Some equitable claims have no jury right.

---

## Workflow

### Step 1: Accept client input

Accept facts and instructions in any format:

- **Written narrative**: Client summary, intake memo, or instruction email
- **Documents**: Contracts, correspondence, evidence files (PDF, DOCX, email)
- **Existing complaint**: For validation mode or amendment
- **Interview notes**: Attorney-client discussion notes
- **Prior filings**: Demand letters, administrative complaints, related litigation

If documents are PDFs, convert:

```bash
pandoc "$FILE" -t markdown -o "${FILE%.pdf}.md" 2>/dev/null || pdftotext "$FILE" "${FILE%.pdf}.txt"
```

### Step 2: Gather context via interactive clarification

Run through CLARIFY blocks 1-8, skipping any already answered. Record all
responses and defaults in the Glass Box audit trail.

### Step 3: Pre-suit requirement check

Before drafting, verify all pre-suit requirements are satisfied:

| Requirement                       | Applicable Claims                                                            | Check                                              |
| --------------------------------- | ---------------------------------------------------------------------------- | -------------------------------------------------- |
| EEOC charge / state agency filing | Title VII, ADA, ADEA, state employment discrimination                        | Right-to-sue letter obtained? Filing deadline met? |
| Tort claims notice                | Claims against government entities (FTCA, state tort claims acts)            | Notice served within statutory period?             |
| Certificate of merit / affidavit  | Medical malpractice (varies by state), professional negligence               | Expert review completed? Certificate ready?        |
| Pre-suit demand                   | Contractual demand requirements, statutory demand (some consumer protection) | Demand letter sent? Cure period expired?           |
| Administrative exhaustion         | Agency-adjudicated claims, IDEA, some environmental claims                   | Agency proceedings completed or deemed exhausted?  |
| DMCA takedown notice              | Copyright infringement (ISP safe harbor)                                     | DMCA notice sent? Response received? [VERIFY]      |
| Right to sue / exhaustion         | Some statutory claims have mandatory agency review periods                   | Waiting period expired or waived?                  |

**[JURISDICTION-SPECIFIC]** Additional pre-suit requirements vary by jurisdiction.

If a pre-suit requirement is not satisfied, flag as **CRITICAL** and advise
that filing may result in dismissal.

### Step 4: Identify and select causes of action

From the client facts, identify all viable causes of action:

**4a. Fact-to-element mapping:**

For each potential cause of action:

1. State the elements (from the Causes of Action Elements Library below)
2. Map specific client facts to each element
3. Assess whether each element can be plausibly pled
4. Flag elements with weak factual support as `[NEEDS STRENGTHENING]`
5. Flag elements that cannot be pled as `[CANNOT PLEAD — OMIT CLAIM]`

**4b. Claim selection assessment:**

| Criterion                                | Include                             | Consider Omitting                                   |
| ---------------------------------------- | ----------------------------------- | --------------------------------------------------- |
| All elements supported by facts          | Yes                                 | —                                                   |
| Most elements supported, 1-2 weak        | Include with strengthening          | Consider if weak element is essential               |
| Heightened pleading required (Rule 9(b)) | Include if specifics available      | Omit if "who, what, when, where, how" not available |
| Pre-suit requirement not met             | Flag CRITICAL                       | Likely must omit                                    |
| Statute of limitations concern           | Include if arguable                 | Flag for counsel decision                           |
| Alternative to stronger claim            | Include as alternative (Rule 8(d))  | Omit if adds confusion without value                |
| Litigation strategy value                | Include if discovery/leverage value | Omit if sanctions risk outweighs benefit            |

**4c. Alternative and inconsistent pleading:**

Under FRCP 8(d)(2)-(3), a party may plead alternative or inconsistent claims.
Use this when:

- Breach of contract AND unjust enrichment (alternative theories for same conduct)
- Fraud AND negligent misrepresentation (alternative scienter theories)
- Direct liability AND respondeat superior (alternative defendant theories)

Label alternative counts clearly: "In the Alternative" or "Alternatively."

### Step 5: Draft jurisdictional and venue allegations

**5a. Subject matter jurisdiction (US federal):**

For **federal question** (28 USC 1331):

```
This Court has subject matter jurisdiction under 28 U.S.C. § 1331
because this action arises under [federal statute or constitutional
provision].
```

For **diversity** (28 USC 1332):

```
This Court has subject matter jurisdiction under 28 U.S.C. § 1332
because the matter in controversy exceeds the sum or value of $75,000,
exclusive of interest and costs, and is between citizens of different
States. Plaintiff [Name] is a citizen of [State]. Defendant [Name] is
a citizen of [State / incorporated in State X with principal place of
business in State Y].
```

For **supplemental** (28 USC 1367):

```
This Court has supplemental jurisdiction over the state-law claims
under 28 U.S.C. § 1367(a) because they form part of the same case or
controversy as the federal claims.
```

**5b. Personal jurisdiction:**

For **general jurisdiction** (defendant "at home" in forum — Daimler, 2014):

```
This Court has personal jurisdiction over Defendant [Name] because
Defendant is [incorporated in / has its principal place of business
in / is domiciled in] this District, making Defendant subject to
general jurisdiction here.
```

For **specific jurisdiction** (minimum contacts related to claims):

```
This Court has personal jurisdiction over Defendant [Name] because
Defendant purposefully directed its activities toward residents of
this District, the claims arise out of those activities, and the
exercise of jurisdiction is reasonable. Specifically, Defendant
[describe contacts: executed the contract in this District / directed
tortious conduct toward residents / transacted business / maintained
an office / solicited customers / shipped products into the forum].
```

**Personal jurisdiction checklist:**

| Factor                               | Allegation Required                                   | Key Cases                                                             |
| ------------------------------------ | ----------------------------------------------------- | --------------------------------------------------------------------- |
| **General — individual**             | Domicile (not mere residence)                         | Daimler AG v. Bauman (2014) [VERIFY]                                  |
| **General — corporation**            | State of incorporation OR principal place of business | Daimler; BNSF Ry. v. Tyrrell (2017) [VERIFY]                          |
| **General — LLC/partnership**        | Citizenship of all members (not entity registration)  | Check circuit law [VERIFY]                                            |
| **Specific — purposeful availment**  | Defendant deliberately engaged with the forum         | Burger King v. Rudzewicz (1985) [VERIFY]                              |
| **Specific — arise out of contacts** | Claims relate to defendant's forum contacts           | Ford Motor Co. v. Montana Eighth Jud. Dist. (2021) [VERIFY]           |
| **Specific — reasonableness**        | Exercise of jurisdiction comports with fair play      | Asahi Metal v. Superior Court (1987) [VERIFY]                         |
| **Consent**                          | Forum selection clause or voluntary appearance        | Carnival Cruise Lines v. Shute (1991) [VERIFY]                        |
| **Long-arm statute**                 | State long-arm statute authorizes jurisdiction        | [JURISDICTION-SPECIFIC] — some states extend to constitutional limits |

**Personal jurisdiction red flags:**

- Mass tort claims against out-of-state defendant without forum-specific injury (Bristol-Myers Squibb, 2017) [VERIFY]
- Suing foreign parent based solely on domestic subsidiary's contacts (Daimler)
- Registration-based general jurisdiction (contested in many jurisdictions post-Daimler) [VERIFY]

**5b-2. Diversity jurisdiction — citizenship pleading guide:**

Proper citizenship allegations are critical for diversity jurisdiction. Common errors lead to dismissal.

| Entity Type                    | Citizenship Rule                                                                     | How to Allege                                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| **Individual**                 | State of domicile (intent to remain + physical presence)                             | "[Name] is a citizen of the State of [State], domiciled at [address]"                                  |
| **Corporation**                | State of incorporation AND principal place of business (Hertz "nerve center" test)   | "[Corp] is a citizen of [State] (incorporated) and [State] (principal place of business at [address])" |
| **LLC**                        | Citizenship of ALL members (not where organized)                                     | Must allege citizenship of every member; if member is an entity, trace through                         |
| **Partnership (GP)**           | Citizenship of ALL general partners                                                  | Same tracing requirement as LLC                                                                        |
| **Limited partnership**        | Citizenship of ALL partners (general and limited)                                    | Must identify and allege citizenship of every partner                                                  |
| **Trust**                      | Citizenship of ALL trustees (traditional) or trustee + beneficiaries (some circuits) | Check circuit law [VERIFY]                                                                             |
| **Unincorporated association** | Citizenship of ALL members                                                           | Must allege or identify                                                                                |
| **Estate**                     | Citizenship of the decedent                                                          | Allege decedent's domicile at death                                                                    |

**Common diversity pitfalls:**

- Stating "resides in" instead of "is a citizen of" — residence ≠ domicile
- Failing to allege LLC members' citizenships (most common diversity error)
- Failing to allege both state of incorporation AND principal place of business for corporations
- Not meeting the amount-in-controversy threshold ($75,000+ exclusive of interest and costs)
- Forum defendant rule: Diversity removal is defeated if any properly joined defendant is a citizen of the forum state (28 USC 1441(b)(2)) [VERIFY]

**5c. Venue:**

```
Venue is proper in this District under 28 U.S.C. § 1391(b) because
[a substantial part of the events or omissions giving rise to the
claim occurred in this District / Defendant resides in this District].
```

### Step 6: Draft party identification

For each party, include:

- Full legal name (individual or entity)
- Entity type (corporation, LLC, partnership, individual)
- State of incorporation/organization and principal place of business (for diversity)
- Capacity in which sued (individual, official, representative)
- Relationship to other parties or claims
- Doe defendants where identity unknown (with basis for inclusion)

**Template:**

```
Plaintiff [Full Legal Name] ("Plaintiff" or "[Short Name]") is a
[natural person residing / corporation organized under the laws of
State X with its principal place of business in State Y] at [address].

Defendant [Full Legal Name] ("Defendant" or "[Short Name]") is a
[corporation organized under the laws of State X with its principal
place of business in State Y / natural person residing] at [address].
Upon information and belief, Defendant [Name] [conducted business /
committed the acts described herein] in this District.
```

### Step 7: Draft factual allegations

Build the factual narrative following these principles:

**7a. Organization strategy:**

| Strategy          | When to Use                            | Structure                                 |
| ----------------- | -------------------------------------- | ----------------------------------------- |
| **Chronological** | Single transaction, clear timeline     | Events in time order                      |
| **Thematic**      | Multiple issues, complex relationships | Grouped by topic/issue                    |
| **By defendant**  | Multi-defendant, different conduct     | Separate fact sections per defendant      |
| **Hybrid**        | Complex cases with timeline + themes   | Background → Theme 1 → Theme 2 → Timeline |

**7b. Drafting rules for factual allegations:**

1. **Numbered paragraphs**: Each paragraph states one factual allegation (Rule 10(b))
2. **Simple, declarative sentences**: Active voice, concrete facts
3. **Specific over general**: Names, dates, amounts, locations — not abstractions
4. **"Upon information and belief"**: Use for facts not within plaintiff's direct knowledge
5. **No legal conclusions in fact section**: Save legal characterization for counts
6. **Exhibit references**: "A true and correct copy of the [document] is attached as Exhibit [X]"
7. **Attribution to specific defendants**: Never "Defendants did X" when only one defendant acted
8. **Chronological markers**: Dates or time references for every material event
9. **Plausibility signals**: Include enough circumstantial facts to cross the Twombly/Iqbal line
10. **Preserve favorable inferences**: State facts in a way that supports the strongest inference

**7c. Twombly/Iqbal plausibility check:**

For each cause of action, verify the factual allegations meet plausibility:

| Element     | Factual Allegation      | Conclusory?          | Plausible? | Fix Needed?                 |
| ----------- | ----------------------- | -------------------- | ---------- | --------------------------- |
| [Element 1] | [Specific fact alleged] | No                   | Yes        | —                           |
| [Element 2] | [Allegation]            | Yes — too conclusory | —          | Rewrite with specific facts |
| [Element 3] | [Allegation]            | No                   | Marginal   | Add supporting context      |

If an element's factual support is conclusory or implausible, either:

- Rewrite with more specific factual detail, OR
- Flag as `[NEEDS STRENGTHENING]` for attorney review, OR
- Recommend omitting the claim if the element cannot be cured

### Step 8: Draft causes of action (counts)

Each count follows this structure:

```
COUNT [NUMBER]
[CAUSE OF ACTION NAME]
(Against Defendant[s] [Name(s)])

[Paragraph number]. Plaintiff incorporates by reference paragraphs
[X] through [Y] above as if fully set forth herein.

[Element-specific allegations — one paragraph per element]

[Paragraph number]. As a direct and proximate result of Defendant's
[conduct], Plaintiff has suffered [damages description] in an amount
to be proven at trial [, but not less than $X].
```

**For each count, verify:**

- [ ] All elements of the cause of action are specifically alleged
- [ ] The allegations are fact-specific, not conclusory
- [ ] The count identifies which defendant(s) it targets
- [ ] Incorporation by reference is used (no need to repeat background facts)
- [ ] Damages/harm are connected to the specific conduct
- [ ] Heightened pleading requirements are met (Rule 9(b) for fraud, PSLRA for securities)
- [ ] Pre-suit requirements are satisfied and alleged where required
- [ ] Statute of limitations has not expired (or tolling is alleged)

### Step 9: Draft prayer for relief

Structure the prayer for relief covering all requested remedies:

```
PRAYER FOR RELIEF

WHEREFORE, Plaintiff [Name] respectfully requests that this Court
enter judgment in Plaintiff's favor and against Defendant(s) and
award the following relief:

a. Compensatory damages in an amount to be proven at trial [, but
   not less than $X] [omit specific amount if ad damnum prohibited];

b. Consequential damages for [specific consequential harm];

c. Punitive damages in an amount sufficient to punish Defendant and
   deter similar conduct [where supported by allegations of malice,
   willfulness, or wanton conduct];

d. [Injunctive relief — specific injunction requested];

e. [Declaratory relief — specific declaration requested];

f. [Statutory damages / treble damages / attorney fees under
   specific statute];

g. Pre-judgment and post-judgment interest as allowed by law;

h. Costs of suit and reasonable attorney fees [under specific
   fee-shifting statute];

i. Such other and further relief as the Court deems just and proper.
```

**[JURISDICTION-SPECIFIC]** Check:

- Ad damnum restrictions (NY CPLR 3017, others)
- Punitive damages leave requirements (NJ, FL)
- Amount-in-controversy implications for diversity jurisdiction
- Statutory damages ranges (Copyright Act § 504(c), TCPA, etc.)

### Step 10: Add required components

**10a. Jury demand (FRCP 38):**

```
DEMAND FOR JURY TRIAL

Plaintiff demands a trial by jury on all claims so triable.
```

**10b. Verification / Statement of Truth (where required):**

- **US**: Required for qui tam, some statutory claims, certain state courts
- **England & Wales**: Statement of truth required on all statements of case (CPR 22)
- **Australia**: Verification requirements vary by court [VERIFY]

**10c. Certificate of compliance:**

- Local rule requirements
- Certificate of interested parties (some courts)
- Corporate disclosure statement (FRCP 7.1)

**10d. Exhibits:**

- Attach key documents referenced in the complaint
- Number sequentially (Exhibit A, B, C or 1, 2, 3)
- Include in table of exhibits if numerous

### Step 11: Rule 11 compliance review

Before delivering the complaint, run a final compliance check:

| Rule 11(b) Certification                         | Check                                                          | Status |
| ------------------------------------------------ | -------------------------------------------------------------- | ------ |
| (1) Not for improper purpose                     | No indication of harassment, delay, or cost imposition         | ☐      |
| (2) Legal contentions warranted                  | Each claim supported by existing law or nonfrivolous extension | ☐      |
| (3) Factual contentions have evidentiary support | Each factual allegation has basis in evidence or investigation | ☐      |
| (4) Denials warranted                            | Any denials of fact are based on evidence or reasonable belief | ☐      |

If any certification cannot be made, flag the specific claim or allegation
for counsel review. Do not include claims that would violate Rule 11.

### Step 12: Deliver complaint

Output the complete complaint with:

- Formatted document ready for filing
- Element-mapping table (showing which facts support which elements)
- Pre-suit requirement status summary
- Plausibility assessment per count
- Strategic notes on claim selection
- Glass Box audit trail

---

## Forum Selection Strategy

When the client has a choice of forum, evaluate the following factors to recommend
the optimal filing venue. This analysis should be included in the Strategic Notes
section of the deliverable.

### Federal vs. State Court Decision Matrix

| Factor              | Federal Court Favors                                                 | State Court Favors                                             |
| ------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Judge quality**   | Life-tenured, experienced with complex civil litigation              | May have specialized courts (business, IP, landlord-tenant)    |
| **Jury pool**       | Drawn from wider geographic area (entire district)                   | Local jury pool — may favor local party                        |
| **Discovery**       | Mandatory initial disclosures (Rule 26(a)); proportionality standard | Varies by state; some states broader discovery                 |
| **Motion practice** | Twombly/Iqbal pleading standard; active MTD practice                 | Some states retain Conley notice pleading (lower bar) [VERIFY] |
| **Speed**           | Varies by district; some very slow                                   | State court may be faster in some jurisdictions                |
| **Removal risk**    | N/A — already in federal                                             | Defendant may remove if diversity or federal question exists   |
| **Class actions**   | CAFA may require (or permit) federal court for large classes         | State court may be friendlier to class certification           |
| **Precedent**       | Binding circuit precedent may be favorable or unfavorable            | State law may be more developed on specific claims             |
| **Appeal**          | Circuit courts of appeal; en banc; certiorari                        | State appellate courts; may be more predictable                |

### State-to-State Forum Considerations

When multiple states have jurisdiction, evaluate:

1. **Substantive law differences**
   - Statute of limitations (varies significantly by state for same claim type)
   - Damages caps (medical malpractice, punitive damages)
   - Comparative fault rules (pure comparative, modified, contributory)
   - Anti-SLAPP statutes (available in some states, not others) [JURISDICTION-SPECIFIC]
   - Prejudgment interest availability and rate
   - Attorney fee shifting rules

2. **Procedural differences**
   - Pleading standards (some states still use Conley notice pleading) [VERIFY]
   - Discovery scope and e-discovery rules
   - Summary judgment standards
   - Trial procedures and motion practice

3. **Practical considerations**
   - Court congestion and time to trial
   - Quality and predictability of judiciary
   - Jury verdict history for similar claims
   - Distance and convenience for witnesses
   - Enforceability of eventual judgment

### Removal Analysis (When Filing in State Court)

Before recommending state court, assess removal risk:

- **Federal question removal** (28 U.S.C. § 1441(a)): If complaint includes any federal claim, entire case removable. Strategy: consider filing federal claims separately or omitting if state claims sufficient [VERIFY]
- **Diversity removal** (28 U.S.C. § 1441(b)): If complete diversity exists and amount exceeds $75,000. Strategy: consider joining non-diverse defendant (if legitimate) to defeat diversity [VERIFY]
- **Forum defendant rule**: No diversity removal if any defendant is a citizen of the forum state — file where defendant is located to prevent removal [VERIFY]
- **CAFA removal**: Class actions with minimal diversity and $5M+ aggregate — very difficult to avoid removal for large classes [VERIFY]
- **1-year time limit**: Diversity-based removal must be filed within 1 year of state filing (but bad-faith exception exists) [VERIFY]

### Forum Selection Clause Analysis

If the relevant contract contains a forum selection clause:

1. **Mandatory vs. permissive**: "Shall be brought in" (mandatory) vs. "may be brought in" (permissive)
2. **Enforceability**: Atlantic Marine (2013) — forum selection clauses generally enforced; heavy burden to show enforcement unreasonable [VERIFY]
3. **Scope**: Does the clause cover tort claims arising from the contractual relationship, or only contractual claims?
4. **Third parties**: Does the clause bind non-signatories (e.g., through agency, estoppel, or third-party beneficiary theories)?
5. **Workaround**: If clause is unfavorable, can claims be framed to fall outside its scope?

---

## Causes of Action Elements Library

### Contract Claims

**Breach of Contract**

1. Existence of a valid contract
2. Plaintiff's performance or excuse for non-performance
3. Defendant's breach (specific contractual obligation violated)
4. Damages resulting from the breach

- Heightened pleading: No (notice pleading sufficient)
- Key variations: UCC vs. common law; written vs. oral; express vs. implied terms

**Breach of Implied Covenant of Good Faith and Fair Dealing**

1. Existence of a contract between the parties
2. Plaintiff's performance or excuse for non-performance
3. Defendant's conduct that frustrated plaintiff's right to receive benefits of the contract
4. Damages resulting from defendant's conduct

- Key issue: Cannot contradict express contract terms; gap-filling doctrine
- [JURISDICTION-SPECIFIC]: Not recognized as independent tort in all states

**Promissory Estoppel**

1. Clear and definite promise
2. Promisor expected or should have expected reliance
3. Promisee actually and reasonably relied on the promise
4. Injustice can be avoided only by enforcing the promise

- Key issue: Alternative theory when no enforceable contract exists

**Unjust Enrichment / Quantum Meruit**

1. Plaintiff conferred a benefit on defendant
2. Defendant had knowledge of the benefit
3. Defendant accepted or retained the benefit
4. It would be inequitable/unjust for defendant to retain the benefit without paying

- Key issue: Cannot recover if an express contract governs the same subject matter (in most jurisdictions)
- Plead as alternative to breach of contract (FRCP 8(d)(2))

### Tort Claims

**Negligence**

1. Defendant owed a duty of care to plaintiff
2. Defendant breached that duty
3. The breach was the actual and proximate cause of plaintiff's injury
4. Plaintiff suffered damages

- Key variations: Professional negligence (standard of care), premises liability, products liability
- [JURISDICTION-SPECIFIC]: Comparative vs. contributory negligence, damage caps

**Fraud / Intentional Misrepresentation** (Rule 9(b) — heightened pleading)

1. Defendant made a false statement of material fact
2. Defendant knew the statement was false (scienter) or made it recklessly
3. Defendant intended to induce plaintiff's reliance
4. Plaintiff actually and justifiably relied on the statement
5. Plaintiff suffered damages as a result

- **Heightened pleading (Rule 9(b))**: Must plead with particularity — WHO made the statement, WHAT was said, WHEN it was said, WHERE it was said, WHY it was false (HOW it was misleading)
- Cannot use "upon information and belief" for the core misrepresentation (but can for scienter in some circuits)

**Negligent Misrepresentation**

1. Defendant made a false statement in a business or professional context
2. Defendant failed to exercise reasonable care in communicating the information
3. Plaintiff justifiably relied on the statement
4. Plaintiff suffered damages as a result

- Rule 9(b): Some circuits require particularity; others apply only to intentional fraud [VERIFY]

**Tortious Interference with Contract**

1. Existence of a valid contract between plaintiff and a third party
2. Defendant's knowledge of the contract
3. Defendant's intentional and improper interference causing breach
4. Damages to plaintiff resulting from the breach

- Key issue: Must identify the specific contract and third party

**Tortious Interference with Prospective Economic Advantage**

1. Existence of a valid business relationship or expectancy
2. Defendant's knowledge of the relationship or expectancy
3. Defendant's intentional and improper interference
4. Plaintiff lost the anticipated economic benefit
5. Damages

- Key issue: Higher bar than contractual interference; must show independently wrongful conduct in many jurisdictions

**Breach of Fiduciary Duty**

1. Existence of a fiduciary relationship (trust, corporate officer/director, attorney-client, etc.)
2. Breach of the duty owed (duty of care, loyalty, good faith, disclosure)
3. Damages resulting from the breach
4. Causation between breach and damages

- Key variations: Business judgment rule defense (corporate context); duty of loyalty vs. care

**Conversion**

1. Plaintiff had ownership or right to possession of personal property
2. Defendant intentionally exercised dominion or control over the property
3. Defendant's exercise of dominion was inconsistent with plaintiff's rights
4. Damages

- Key issue: Applies to personal property and in some jurisdictions to intangible property (funds, digital assets)

**Defamation (Libel / Slander)**

1. Defendant made a false statement of fact (not opinion)
2. The statement was published (communicated) to a third party
3. The statement was about (of and concerning) the plaintiff
4. The statement was defamatory (tending to harm reputation)
5. Damages (per se categories vs. special damages requirement)

- For public figures: Must also plead actual malice (New York Times v. Sullivan — knowledge of falsity or reckless disregard) [VERIFY]
- [JURISDICTION-SPECIFIC]: Anti-SLAPP statutes, single publication rule, retraction statutes

### Business / Commercial Claims

**Trade Secret Misappropriation (DTSA / UTSA)**

1. Existence of a trade secret (derives independent economic value from not being generally known; subject to reasonable secrecy measures)
2. Defendant misappropriated the trade secret (acquisition by improper means, or disclosure/use without consent)
3. Damages (actual loss, unjust enrichment, or reasonable royalty)

- DTSA (18 USC 1836): Federal cause of action; requires interstate or foreign commerce nexus
- UTSA: State law versions in 48+ states; elements vary slightly
- Must identify the trade secret with reasonable particularity

**Unfair Competition (Lanham Act § 43(a))**

1. Defendant made a false or misleading statement of fact
2. The statement was used in commercial advertising or promotion
3. The statement deceived or had tendency to deceive a substantial segment of the audience
4. The deception was material (likely to influence purchasing decisions)
5. Plaintiff suffered or is likely to suffer injury as a result

- Standing: Must be a competitor or have competitive injury

**RICO (18 USC 1962)**

1. Existence of an enterprise (association-in-fact or legal entity)
2. Pattern of racketeering activity (at least two predicate acts within 10 years, related, with continuity)
3. Defendant conducted or participated in the conduct of the enterprise through the pattern
4. Plaintiff was injured in business or property by reason of the RICO violation

- Heightened pleading: Predicate acts of fraud must meet Rule 9(b)
- Treble damages and attorney fees available (18 USC 1964(c))
- [VERIFY]: Current circuit splits on RICO elements

**Antitrust — Sherman Act § 1 (Conspiracy in Restraint of Trade)**

1. Agreement or conspiracy between two or more entities
2. Unreasonable restraint of trade (per se or rule of reason)
3. Effect on interstate commerce
4. Antitrust injury (injury of the type the antitrust laws were intended to prevent)
5. Antitrust standing (direct purchaser doctrine / Illinois Brick)

- Twombly standard originated in this context — parallel conduct alone is insufficient

**Antitrust — Sherman Act § 2 (Monopolization)**

1. Possession of monopoly power in a relevant market
2. Willful acquisition or maintenance of that power through anticompetitive conduct
3. Antitrust injury and standing

- Must define relevant product and geographic market

### Employment Claims

**Employment Discrimination (Title VII / ADA / ADEA)**

1. Plaintiff is a member of a protected class
2. Plaintiff was qualified for the position
3. Plaintiff suffered an adverse employment action
4. Circumstances give rise to an inference of discrimination

- Pre-suit: EEOC charge required; right-to-sue letter
- McDonnell Douglas framework applies at summary judgment but complaint need only satisfy Iqbal
- [JURISDICTION-SPECIFIC]: State equivalents may have different procedures and broader protections

**Retaliation (Title VII § 704(a) / other statutes)**

1. Plaintiff engaged in protected activity (complaint, charge, testimony, opposition)
2. Defendant took an adverse action against plaintiff
3. Causal connection between the protected activity and the adverse action

- Adverse action broadly defined: Burlington Northern (any action that might dissuade a reasonable worker) [VERIFY]
- Must allege temporal proximity or other facts suggesting causation

**Wrongful Termination (Common Law)**

1. Employment relationship existed
2. Termination occurred
3. Termination violated public policy / implied contract / covenant of good faith
4. Damages

- [JURISDICTION-SPECIFIC]: Varies enormously by state; some states (at-will) have very limited wrongful termination claims

### Intellectual Property Claims

**Patent Infringement (35 USC 271)**

1. Plaintiff owns a valid, enforceable patent
2. Defendant made, used, sold, offered for sale, or imported the patented invention
3. The accused product or process meets every limitation of at least one claim (literal infringement or doctrine of equivalents)

- Must identify patent number(s) and asserted claims
- Must identify accused instrumentality with specificity
- Form 18 (abolished 2015) — but its level of specificity remains instructive
- [VERIFY]: Current pleading requirements post-Form 18 abolition

**Copyright Infringement (17 USC 501)**

1. Plaintiff owns a valid copyright (registration required for suit, but not for claim accrual)
2. Defendant copied original elements of the work

- Must allege registration or pre-registration (Fourth Estate Public Benefit Corp. v. Wall-Street.com, 2019) [VERIFY]
- For statutory damages: timely registration required (within 3 months of publication or before infringement)

**Trademark Infringement (Lanham Act § 32 / § 43(a))**

1. Plaintiff owns a valid, protectable mark
2. Defendant used a confusingly similar mark in commerce
3. Likelihood of confusion among consumers

- Multi-factor likelihood of confusion test (varies by circuit — Polaroid, Sleekcraft, etc.)
- Must identify the registered or common law mark

---

## Pleading Standards Quick Reference

### Twombly/Iqbal Two-Step Analysis

**Step 1 — Strip legal conclusions:**
Identify and set aside allegations that are merely legal conclusions
couched as factual assertions. Examples:

- "Defendant acted negligently" (conclusion)
- "Defendant breached the contract" (conclusion)
- "Defendant conspired to restrain trade" (conclusion)

**Step 2 — Assess plausibility of remaining factual allegations:**
Do the remaining factual allegations, taken as true and with all
reasonable inferences drawn in plaintiff's favor, state a claim that
is plausible on its face?

| Assessment                        | Meaning                                                                                       | Action                      |
| --------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------- |
| **Plausible**                     | Facts alleged "allow the court to draw the reasonable inference that the defendant is liable" | Claim survives              |
| **Conceivable but not plausible** | Possible but does not cross the line from speculation                                         | Claim fails — add facts     |
| **Conclusory**                    | Bare legal conclusions without factual backing                                                | Rewrite with specific facts |

### Rule 9(b) Heightened Pleading (Fraud)

The "who, what, when, where, and how" requirement:

| Element     | Must Plead                                    | Example                                                                                               |
| ----------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Who**     | Identity of person making the false statement | "Defendant John Smith, CEO of Acme Corp."                                                             |
| **What**    | The specific false statement or omission      | "stated that Acme's revenue had grown 40% year-over-year"                                             |
| **When**    | Date or time period of the statement          | "during the March 15, 2025 investor presentation"                                                     |
| **Where**   | Location or medium of the statement           | "at Acme's headquarters in New York City"                                                             |
| **Why/How** | Why the statement was false or misleading     | "when in fact Acme's revenue had declined 5%, as shown by its internal financial reports (Exhibit A)" |

### PSLRA Heightened Pleading (Securities Fraud)

In addition to Rule 9(b), the PSLRA (15 USC 78u-4) requires:

1. **Misleading statement**: Specify each statement alleged to be misleading and why
2. **Strong inference of scienter**: Facts giving rise to a "strong inference" that defendant acted with scienter — must be "at least as compelling" as any opposing inference (Tellabs, Inc. v. Makor Issues & Rights, Ltd., 2007) [VERIFY]
3. **Loss causation**: Allege that the misrepresentation caused the economic loss (Dura Pharmaceuticals v. Broudo, 2005) [VERIFY]

---

## Common Complaint Structures by Type

### Standard Civil Complaint (US Federal)

```
[CAPTION]
UNITED STATES DISTRICT COURT
[DISTRICT] DISTRICT OF [STATE]

[Plaintiff Name],
          Plaintiff,
                                    Case No. [to be assigned]
     v.
                                    COMPLAINT
[Defendant Name],                   [AND DEMAND FOR JURY TRIAL]
          Defendant.

[SECTIONS — in order]
I.    INTRODUCTION / PRELIMINARY STATEMENT (optional but recommended)
II.   PARTIES
III.  JURISDICTION AND VENUE
IV.   FACTUAL ALLEGATIONS
      A. [Thematic subsection or chronological narrative]
      B. [Thematic subsection]
V.    CAUSES OF ACTION
      COUNT I — [Cause of Action] (Against [Defendant])
      COUNT II — [Cause of Action] (Against [Defendant])
      [etc.]
VI.   PRAYER FOR RELIEF
VII.  JURY DEMAND

[Signature block]
[Exhibits]
```

### Class Action Complaint (Rule 23)

Add after Party section:

```
CLASS ALLEGATIONS

[Para]. Plaintiff brings this action on behalf of themselves and
all others similarly situated pursuant to Rule 23(b)([1/2/3]) of
the Federal Rules of Civil Procedure.

[Para]. The Class is defined as: [precise class definition with
temporal and geographic scope].

[Para]. Numerosity: The Class is so numerous that joinder of all
members is impracticable. Upon information and belief, the Class
consists of [estimated number] members.

[Para]. Commonality: There are questions of law and fact common to
the Class, including: [list common questions].

[Para]. Typicality: Plaintiff's claims are typical of the claims
of the Class because [explanation].

[Para]. Adequacy: Plaintiff will fairly and adequately protect the
interests of the Class because [no conflicts; competent counsel].

[Para]. [Rule 23(b)(3)]: Common questions of law and fact predominate
over individual questions, and a class action is superior to other
available methods of adjudication because [reasons].
```

### England & Wales — Particulars of Claim (CPR Part 16)

```
IN THE HIGH COURT OF JUSTICE
[DIVISION]
[DISTRICT REGISTRY if applicable]

BETWEEN:
                    [CLAIMANT NAME]                    Claimant
                    - and -
                    [DEFENDANT NAME]                   Defendant

PARTICULARS OF CLAIM

1. [Introduction — nature of claim]
2. [Parties]
3. [Material facts — chronological, concise]
   ...
[n]. [Relief sought — statement of value required]
[n+1]. [Interest claim under Senior Courts Act 1981 s.35A or
        County Courts Act 1984 s.69]

STATEMENT OF TRUTH
I believe that the facts stated in these Particulars of Claim are true.
I understand that proceedings for contempt of court may be brought
against anyone who makes, or causes to be made, a false statement in a
document verified by a statement of truth without an honest belief in
its truth.

Signed: _______________
[Party/Litigation friend/Legal representative]
Date: _______________
```

### Australia — Statement of Claim (Federal Court)

```
FEDERAL COURT OF AUSTRALIA
[REGISTRY]
[DISTRICT]

                                    No. [number] of [year]

[APPLICANT NAME]
     Applicant

[RESPONDENT NAME]
     Respondent

STATEMENT OF CLAIM

A. PARTIES
1. [Party details]

B. BACKGROUND FACTS
2. [Material facts — concise]

C. [CAUSE OF ACTION]
[n]. [Element-specific allegations]

D. RELIEF SOUGHT
The Applicant claims:
(a) [Specific relief]
(b) [Damages]
(c) [Costs]
(d) [Further or other relief]

Date: _______________
[Solicitor / Applicant signature]
```

---

## Pre-Suit Requirements — Detailed Reference

### Administrative Exhaustion Requirements

| Claim Type                      | Agency                     | Requirement                            | Deadline                                                 | Consequence of Non-Exhaustion                     |
| ------------------------------- | -------------------------- | -------------------------------------- | -------------------------------------------------------- | ------------------------------------------------- |
| Title VII discrimination        | EEOC (or state equivalent) | File charge of discrimination          | 180 days (300 with state agency) from discriminatory act | Dismissal — jurisdictional prerequisite [VERIFY]  |
| ADA employment                  | EEOC                       | File charge                            | 180/300 days                                             | Dismissal                                         |
| ADEA                            | EEOC                       | File charge (or skip in some circuits) | 180/300 days                                             | Dismissal in most circuits [VERIFY]               |
| Section 1983 (civil rights)     | None                       | No exhaustion required                 | N/A — direct filing                                      | N/A                                               |
| FTCA (federal tort claims)      | Federal agency             | Present administrative claim (SF-95)   | 2 years from accrual                                     | Jurisdictional bar; cannot file in court [VERIFY] |
| State tort claims (govt entity) | State/local agency         | File notice of claim                   | Varies by state (30-365 days) [JURISDICTION-SPECIFIC]    | Dismissal; may be jurisdictional                  |
| IDEA (special education)        | School district/state      | Due process hearing                    | Before filing suit                                       | Exhaustion required                               |
| ERISA benefits                  | Plan administrator         | File claim under plan procedures       | Per plan terms                                           | Must exhaust internal remedies first [VERIFY]     |
| Copyright infringement          | US Copyright Office        | Register copyright                     | Before filing suit (Fourth Estate, 2019)                 | Cannot file — registration required [VERIFY]      |

### Certificate of Merit / Affidavit of Merit Requirements

| State  | Claim Type               | Requirement                                   | Deadline                       |
| ------ | ------------------------ | --------------------------------------------- | ------------------------------ |
| **NJ** | Professional malpractice | Affidavit of merit from licensed professional | 60 days after answer [VERIFY]  |
| **TX** | Medical malpractice      | Expert report                                 | 120 days after answer [VERIFY] |
| **PA** | Professional liability   | Certificate of merit                          | Filed with complaint [VERIFY]  |
| **CA** | Medical malpractice      | Certificate of merit (CCP 411.35)             | Filed with complaint [VERIFY]  |
| **NY** | Medical malpractice      | Certificate of merit (CPLR 3012-a)            | Filed with complaint [VERIFY]  |
| **GA** | Professional malpractice | Expert affidavit                              | Filed with complaint [VERIFY]  |
| **FL** | Medical malpractice      | Pre-suit investigation + notice to defendant  | 90 days before filing [VERIFY] |

**[JURISDICTION-SPECIFIC]** Always check state-specific requirements before filing professional malpractice claims.

### Demand Letter Requirements

| Context                      | Requirement                                                  | Effect                                                                |
| ---------------------------- | ------------------------------------------------------------ | --------------------------------------------------------------------- |
| Contractual pre-suit demand  | Many contracts require written demand and cure period        | Filing without demand may be premature                                |
| UCC perfect tender           | Notice of breach required (UCC 2-607(3)(a))                  | Failure to notify may bar remedy                                      |
| Consumer protection statutes | Many require pre-suit demand letter with opportunity to cure | May affect damages, fee-shifting, or standing [JURISDICTION-SPECIFIC] |
| Warranty claims              | Notice to seller required (UCC 2-607)                        | Failure bars recovery                                                 |
| Insurance bad faith          | Demand / proof of loss required                              | Prerequisite in most jurisdictions                                    |

---

## Statute of Limitations Quick Reference

### US Federal Claims

| Claim                              | Limitation Period                           | Accrual Rule                           | Tolling                                         |
| ---------------------------------- | ------------------------------------------- | -------------------------------------- | ----------------------------------------------- |
| **Breach of contract (state law)** | 3-6 years [JURISDICTION-SPECIFIC]           | Breach occurs                          | Discovery rule in some states                   |
| **Fraud**                          | 3-6 years [JURISDICTION-SPECIFIC]           | Discovery of fraud                     | Discovery rule applies                          |
| **Negligence**                     | 2-3 years [JURISDICTION-SPECIFIC]           | Date of injury                         | Discovery rule; minority tolling                |
| **Section 1983**                   | Borrowed from state personal injury         | Date of constitutional deprivation     | Discovery; equitable tolling                    |
| **Title VII**                      | 90 days after right-to-sue letter           | Receipt of EEOC right-to-sue           | Equitable tolling in limited circumstances      |
| **ADEA**                           | 90 days after right-to-sue letter           | Receipt of right-to-sue                | Similar to Title VII                            |
| **ADA**                            | 90 days after right-to-sue letter           | Receipt of right-to-sue                | Similar to Title VII                            |
| **Securities fraud (10b-5)**       | 2 years / 5 years (inquiry notice / repose) | Discovery + SOX outer limit            | Equitable tolling [VERIFY]                      |
| **Antitrust (Sherman Act)**        | 4 years                                     | Each overt act; continuing violation   | Fraudulent concealment                          |
| **RICO**                           | 4 years                                     | Discovery of injury + pattern          | Discovery rule [VERIFY]                         |
| **Patent infringement**            | 6 years (damages look-back)                 | Each act of infringement               | Equitable estoppel; laches                      |
| **Copyright infringement**         | 3 years                                     | Each act of infringement               | Discovery rule (Warner Chappell, 2024) [VERIFY] |
| **Trademark infringement**         | No federal SOL; laches defense              | Ongoing infringement                   | Laches (analogize to state SOL)                 |
| **DTSA (trade secret)**            | 3 years                                     | Discovery or should have discovered    | Discovery rule                                  |
| **FTCA**                           | 2 years                                     | Accrual + 6 months after agency denial | Administrative filing tolls                     |

### England & Wales [VERIFY]

| Claim                       | Limitation Period          | Statute                   |
| --------------------------- | -------------------------- | ------------------------- |
| Breach of contract          | 6 years (12 if under seal) | Limitation Act 1980, s.5  |
| Tort (negligence, nuisance) | 6 years                    | Limitation Act 1980, s.2  |
| Personal injury             | 3 years                    | Limitation Act 1980, s.11 |
| Defamation                  | 1 year                     | Limitation Act 1980, s.4A |
| Fraud                       | 6 years from discovery     | Limitation Act 1980, s.32 |

### Australia [VERIFY]

| Claim                    | Limitation Period               | Notes                             |
| ------------------------ | ------------------------------- | --------------------------------- |
| Contract                 | 6 years                         | Varies by state/territory         |
| Tort                     | 6 years (3 for personal injury) | State limitation acts             |
| Misleading conduct (ACL) | 6 years (3 for damages)         | Competition and Consumer Act 2010 |

**Drafting note:** Do NOT affirmatively address statute of limitations in the complaint unless needed to show timeliness (e.g., alleging tolling or discovery). Statute of limitations is an affirmative defense for the defendant to raise.

---

## Doe Defendant Practice

### When to Use Doe Defendants

| Scenario                                             | Appropriate?                          | Approach                                                         |
| ---------------------------------------------------- | ------------------------------------- | ---------------------------------------------------------------- |
| Identity unknown but discoverable                    | Yes                                   | "Doe 1-10" with description of role                              |
| Government employee acting under color of law        | Yes                                   | "Officer John Doe, Badge #XXX"                                   |
| Corporate employee who participated but name unknown | Yes                                   | "John Doe, employee of Defendant Corp responsible for [conduct]" |
| Fictitious defendant to preserve diversity           | No — violates 28 USC 1441(b) [VERIFY] | Do not use                                                       |
| Generic placeholder with no factual basis            | No                                    | Rule 11 concern                                                  |

### Doe Defendant Template

```
Defendants DOE 1 through DOE 10 are individuals and/or entities
whose true names and capacities are unknown to Plaintiff at this
time. Plaintiff is informed and believes, and thereon alleges, that
each DOE Defendant is responsible in some manner for the events and
happenings alleged herein, and that Plaintiff's damages as alleged
herein were proximately caused by such DOE Defendants. Plaintiff
will seek leave to amend this Complaint to allege the true names
and capacities of the DOE Defendants when the same have been
ascertained through discovery.
```

### Relation-Back for Doe Replacement (Rule 15(c))

To replace a Doe defendant with a named defendant after the statute
of limitations has run, plaintiff must show (Rule 15(c)(1)(C)):

1. The claim arose from the same conduct as the original complaint
2. The new defendant received notice within 90 days of filing (Rule 4(m) service period)
3. The new defendant knew or should have known the action would have been brought against them
4. The new defendant will not be prejudiced

**Key case:** Krupski v. Costa Crociere S.p.A., 560 U.S. 538 (2010) — relation-back focuses on what the prospective defendant knew, not what the plaintiff knew [VERIFY]

---

## Common 12(b)(6) Dismissal Patterns

Understanding why complaints fail helps draft complaints that survive:

### Most Common Grounds for Dismissal

| Ground                                           | Frequency                          | How to Avoid                                                                              |
| ------------------------------------------------ | ---------------------------------- | ----------------------------------------------------------------------------------------- |
| **Conclusory allegations**                       | Very common                        | Replace "Defendant was negligent" with specific facts showing how duty was breached       |
| **Missing elements**                             | Common                             | Use element checklist for each cause of action; verify all elements are specifically pled |
| **Failure to plead fraud with particularity**    | Common for fraud claims            | Include who, what, when, where, and how/why for every misrepresentation                   |
| **Insufficient factual detail for plausibility** | Common                             | Add dates, names, amounts, documents, and circumstantial facts                            |
| **Group pleading**                               | Common in multi-defendant cases    | Attribute specific conduct to specific defendants                                         |
| **Statute of limitations on face**               | Occasional                         | Do not include dates that defeat your claim; let defendant raise as affirmative defense   |
| **Lack of standing**                             | Occasional                         | Clearly allege injury in fact, causation, and redressability                              |
| **Failure to exhaust**                           | Common for employment/admin claims | Verify and allege exhaustion of administrative remedies                                   |
| **Shotgun pleading**                             | Common in 11th Circuit             | Be selective in incorporation by reference; keep counts focused                           |
| **Immunity**                                     | Government defendants              | Address qualified/sovereign immunity if applicable                                        |

### Surviving a Motion to Dismiss — Checklist

For each count, before filing:

- [ ] Every element is alleged with specific factual support
- [ ] Factual allegations are not conclusory (would survive Iqbal Step 1)
- [ ] Remaining facts make the claim plausible, not merely conceivable (Iqbal Step 2)
- [ ] If fraud: who, what, when, where, and why/how are specified (Rule 9(b))
- [ ] If securities fraud: strong inference of scienter alleged (PSLRA)
- [ ] Conduct is attributed to specific defendants (not "Defendants generally")
- [ ] Pre-suit requirements are satisfied and alleged
- [ ] Statute of limitations is not expired (or tolling/discovery rule is pled)
- [ ] Standing is established (injury, causation, redressability)
- [ ] Jurisdiction and venue are properly alleged

---

## Sub-Agent Architecture (For Complex Multi-Claim Complaints)

When drafting complaints with 5+ causes of action or involving multiple
jurisdictions, delegate to parallel sub-agents:

```
┌─────────────────────────────────────────────────────────────┐
│                    ORCHESTRATOR (Opus)                       │
│                                                             │
│   Accepts facts → Selects claims → Delegates elements →     │
│   Assembles complaint → Validates plausibility →             │
│   Delivers package                                          │
└──────┬──────────┬──────────┬──────────┬────────────────────┘
       │          │          │          │
       ▼          ▼          ▼          ▼
┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐
│ Contract  │ │   Tort    │ │  Statutory│ │Jurisdiction│
│ Claims    │ │  Claims   │ │  Claims   │ │ & Venue   │
│ (Sonnet)  │ │ (Sonnet)  │ │ (Sonnet)  │ │ (Sonnet)  │
│           │ │           │ │           │ │           │
│ Elements  │ │ Elements  │ │ Elements  │ │ SMJ, PJ,  │
│ for each  │ │ for each  │ │ for each  │ │ venue,    │
│ contract  │ │ tort      │ │ statutory │ │ standing  │
│ count     │ │ count     │ │ count     │ │ analysis  │
└───────────┘ └───────────┘ └───────────┘ └───────────┘
```

Each sub-agent receives:

- The factual narrative relevant to its claim category
- The specific causes of action to draft
- Element definitions from the Elements Library
- Instructions to return numbered paragraphs and element-mapping table
- The applicable pleading standard (notice, plausibility, heightened)

---

## Classification System

Each element assessment is classified:

| Classification | Definition                                                                                   | Confidence Threshold | Action                                      |
| -------------- | -------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------- |
| **WELL-PLED**  | Element fully supported by specific factual allegations meeting applicable pleading standard | ≥ 0.80               | No changes needed                           |
| **ADEQUATE**   | Element pled with sufficient facts for plausibility but could be strengthened                | ≥ 0.60               | Suggest strengthening language              |
| **VULNERABLE** | Element pled but likely insufficient under Twombly/Iqbal; susceptible to 12(b)(6) motion     | ≥ 0.80               | Provide rewrite with stronger factual basis |
| **DEFICIENT**  | Element missing, conclusory, or fatally flawed; claim will not survive dismissal motion      | ≥ 0.90               | Must rewrite or recommend omitting claim    |

**Classification decision rules:**

- DEFICIENT: Missing element, purely conclusory allegation, or clear failure to meet heightened pleading — confidence ≥ 0.90
- VULNERABLE: Element pled but with insufficient specificity or plausibility concerns — confidence ≥ 0.80
- ADEQUATE: Element pled with basic facts but room for improvement — confidence ≥ 0.60
- WELL-PLED: Element fully supported with specific, plausible factual allegations — confidence ≥ 0.80

---

## Actionable Output Per Finding

```yaml
finding:
  id: "F-001"
  count: "Count III — Fraud"
  element: "Scienter (knowledge of falsity)"
  classification: "VULNERABLE"
  confidence: 0.82
  pleading_standard: "Rule 9(b) — heightened"
  summary: "Scienter allegation relies on conclusory statement that 'Defendant knew the representations were false.' Under Rule 9(b), plaintiff must allege specific facts showing Defendant's knowledge — e.g., access to contradicting internal reports, prior warnings, or pattern of similar misrepresentations."
  current_text: "Defendant knew or should have known that its representations regarding the product's safety were false and misleading."
  suggested_fix: "Defendant knew its representations regarding the product's safety were false because: (a) Defendant's internal testing reports dated March 2024 (Exhibit D) showed failure rates exceeding 15%, contradicting its public representations of a less-than-1% failure rate; (b) Defendant's Chief Engineer, Jane Smith, emailed Defendant's CEO on April 5, 2024 warning that 'our safety claims cannot be substantiated' (Exhibit E); and (c) Defendant had received 47 customer complaints regarding product failures before making the representations at issue."
  priority: "Tier 1 — Must fix before filing"
  self_interrogation:
    pass_1: "Rule 9(b) is clear — scienter must be pled with particularity. A bare 'knew or should have known' will not survive a motion to dismiss for fraud claims."
    pass_2: "Check whether the jurisdiction allows 'upon information and belief' for scienter where facts are peculiarly within defendant's knowledge."
    pass_3: "If client lacks specific facts showing knowledge, consider pleading negligent misrepresentation instead (lower scienter bar)."
```

---

## Prioritization Framework

### Tier 1 — Must Fix Before Filing

- Missing elements for any cause of action
- Conclusory allegations that fail Twombly/Iqbal
- Rule 9(b) deficiencies in fraud/securities claims
- Missing jurisdictional or venue allegations
- Unsatisfied pre-suit requirements
- Rule 11 compliance concerns
- Statute of limitations issues

### Tier 2 — Should Fix Before Filing

- Weak factual support for elements (plausible but thin)
- Inadequate party identification or capacity allegations
- Missing or incomplete prayer for relief
- Formatting non-compliance with local rules
- Failure to attribute conduct to specific defendants
- Missing jury demand (if jury trial desired)

### Tier 3 — Consider Improving

- Narrative organization and persuasiveness
- Alternative pleading structure
- Additional causes of action that could be included
- Stronger exhibit references
- More specific damages allegations
- Strategic claim ordering (strongest first)

---

## Citation Quality Gates

| Gate           | Rule                                                                          | Fail Action                              |
| -------------- | ----------------------------------------------------------------------------- | ---------------------------------------- |
| **Source**     | Every element assessment cites specific complaint paragraph and factual basis | Add citation or mark `[CITATION NEEDED]` |
| **Format**     | Rule and case citations use correct format for jurisdiction                   | Normalize format                         |
| **Currency**   | Procedural rules and case law are current (post-Twombly/Iqbal for pleading)   | Add `[VERIFY CURRENCY]`                  |
| **Domain**     | Element definitions match the selected jurisdiction's law                     | Remove jurisdiction bleed                |
| **Confidence** | Confidence score aligns with classification threshold                         | Downgrade if below threshold             |

---

## Self-Interrogation (For VULNERABLE and DEFICIENT Findings)

**Pass 1 — Element Accuracy**
Is this actually a required element in this jurisdiction? Are there jurisdictions
or circuits that define the elements differently? Could the claim survive under
a different formulation of the elements?

**Pass 2 — Factual Sufficiency**
Is the factual allegation truly conclusory, or does it contain enough specific
facts to cross the plausibility line? Would a sympathetic reading (as required
at the motion-to-dismiss stage) save this allegation?

**Pass 3 — Strategic Alternative**
If this element cannot be adequately pled, is there an alternative cause of
action that captures the same conduct without this problematic element? Would
pleading in the alternative solve the problem?

---

## Confidence Scoring

| Level        | Range     | Interpretation                                                           | Action                              |
| ------------ | --------- | ------------------------------------------------------------------------ | ----------------------------------- |
| **Definite** | 0.95-1.00 | Element clearly and specifically pled with strong factual support        | No action needed                    |
| **High**     | 0.80-0.94 | Element well-pled; minor improvements possible                           | Report with brief caveat            |
| **Probable** | 0.60-0.79 | Element pled but some vulnerability; alternative reading could challenge | Note vulnerability                  |
| **Possible** | 0.40-0.59 | Element weakly pled; likely needs strengthening to survive motion        | Flag for attorney review            |
| **Unlikely** | 0.00-0.39 | Element not adequately pled; claim likely fails at motion to dismiss     | Recommend rewrite or claim omission |

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-complaint-drafter"
  skill_version: "1.0"
  topic: "civil complaint drafting"
  jurisdiction: "[selected jurisdiction]"

  # Drafting metadata
  drafting_mode: "[full draft | element validation | amendment]"
  court: "[court name]"
  jurisdiction_basis: "[federal question | diversity | supplemental | state | UK | AU]"
  claim_types: "[list of claim categories]"
  strategic_approach: "[aggressive | measured | conservative | preservation]"
  complaint_type: "[standard | class action | qui tam | derivative | RICO | amended]"

  # Input summary
  input_summary:
    materials_provided: "[list of client materials]"
    fact_sources: "[narrative | documents | interview notes | existing draft]"

  # CLARIFY responses
  clarify_responses:
    block_1_mode: "[response or default]"
    block_2_court: "[response or default]"
    block_3_jurisdiction: "[response or default]"
    block_4_claims: "[response or default]"
    block_5_materials: "[response or default]"
    block_6_strategy: "[response or default]"
    block_7_type: "[response or default]"
    block_8_jury: "[response or default]"

  # Pre-suit requirements
  pre_suit_check:
    requirements_identified: "[list]"
    requirements_satisfied: "[list]"
    requirements_unsatisfied: "[list — CRITICAL if any]"

  # Causes of action
  causes_of_action:
    total_counts: "[number]"
    claims_included: "[list with element count per claim]"
    claims_considered_but_omitted: "[list with reason]"
    heightened_pleading_claims: "[list — Rule 9(b), PSLRA, etc.]"
    alternative_pleading_used: "[yes/no, which counts]"

  # Element assessment
  element_assessment:
    total_elements: "[count across all counts]"
    well_pled: "[count]"
    adequate: "[count]"
    vulnerable: "[count]"
    deficient: "[count]"

  # Plausibility assessment
  plausibility:
    overall: "[STRONG | ADEQUATE | MARGINAL | DEFICIENT]"
    per_count: "[list with classification per count]"

  # Rule 11 compliance
  rule_11:
    legal_basis_confirmed: "[yes/no per claim]"
    factual_basis_confirmed: "[yes/no per allegation]"
    concerns_flagged: "[list or none]"

  # Limitations
  limitations:
    - "Element definitions based on general federal/majority rule — confirm for specific jurisdiction"
    - "Factual allegations based on client-provided materials — not independently verified"
    - "Case currency not independently verified — all [VERIFY] flags require confirmation"
    - "[additional context-specific limitations]"

  completed_at: "[ISO timestamp]"
```

---

## Remedies and Prayer for Relief — Detailed Reference

### Compensatory Damages

| Type                              | Description                                             | Pleading Requirement                                                                  |
| --------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **General / Direct**              | Natural and probable consequence of the wrongful act    | Plead generally; no specific amount required                                          |
| **Special / Consequential**       | Not natural consequence; must be foreseeable and proven | Must be specifically pled in many jurisdictions [JURISDICTION-SPECIFIC]               |
| **Lost profits**                  | Future income stream lost due to defendant's conduct    | Must plead with reasonable certainty; methodology matters                             |
| **Medical expenses**              | Past and future medical costs                           | Plead past costs with specificity; future costs with basis                            |
| **Lost wages / earning capacity** | Past and future lost income                             | Plead employment details, salary, duration of loss                                    |
| **Property damage**               | Cost of repair or diminution in value                   | Plead which measure applies and factual basis                                         |
| **Emotional distress**            | Psychological harm                                      | Requirements vary: some claims require physical manifestation [JURISDICTION-SPECIFIC] |

### Punitive / Exemplary Damages

| Jurisdiction             | Standard                                                                                                         | Pleading Rules                                                             | Constitutional Limits                                                                       |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **US federal (general)** | Malice, willfulness, wanton conduct, or reckless disregard                                                       | Plead in complaint (most jurisdictions)                                    | Single-digit ratio to compensatory (State Farm) [VERIFY]                                    |
| **California**           | Malice, oppression, or fraud (Cal. Civ. Code § 3294)                                                             | Plead facts supporting malice/oppression/fraud                             | State Farm limits apply                                                                     |
| **New Jersey**           | Clear and convincing evidence; punitive damages act                                                              | Must obtain leave of court to amend to add (NJ Stat. 2A:15-5.12) [VERIFY]  | Statutory cap: 5x compensatory or $350K, whichever greater                                  |
| **Florida**              | Clear and convincing evidence; financial misconduct                                                              | Must obtain leave of court (Fla. Stat. § 768.72) [VERIFY]                  | Statutory cap: 3x compensatory or $500K (general)                                           |
| **Texas**                | Clear and convincing evidence; fraud, malice, or gross negligence                                                | Plead in original petition                                                 | Statutory cap: greater of 2x economic + equal to non-economic (max $750K) or $200K [VERIFY] |
| **England & Wales**      | Rookes v. Barnard categories: (1) oppressive government action, (2) calculated profit, (3) authorized by statute | Very limited availability                                                  | Not subject to US constitutional limits [VERIFY]                                            |
| **Australia**            | Conscious wrongdoing, contumelious disregard                                                                     | Available in common law; restricted by Civil Liability Acts in some states | Varies by state [VERIFY]                                                                    |

### Equitable Relief

| Remedy                           | Requirements                                                                                                                                    | Pleading Approach                                                              |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **TRO / Preliminary injunction** | (1) Likelihood of success, (2) Irreparable harm, (3) Balance of hardships, (4) Public interest (Winter v. NRDC, 2008)                           | Separate motion; complaint must allege facts supporting each factor            |
| **Permanent injunction**         | (1) Irreparable injury, (2) Inadequate legal remedies, (3) Balance of hardships, (4) Public interest not disserved (eBay v. MercExchange, 2006) | Allege in prayer; full proof at trial                                          |
| **Specific performance**         | (1) Valid contract, (2) Plaintiff ready/willing/able, (3) Inadequacy of money damages, (4) Feasibility of enforcement                           | Allege why money damages are inadequate (unique property, irreplaceable goods) |
| **Declaratory judgment**         | (1) Actual controversy, (2) Ripeness, (3) Not advisory                                                                                          | Allege specific declaration sought and why controversy exists                  |
| **Constructive trust**           | (1) Unjust enrichment, (2) Wrongful acquisition of property, (3) Identifiable property                                                          | Allege specific property and basis for equitable claim                         |
| **Accounting**                   | Defendant has duty to account; plaintiff cannot determine amount owed                                                                           | Allege fiduciary or contractual duty and inability to calculate                |
| **Rescission**                   | (1) Grounds (fraud, mutual mistake, incapacity), (2) Restoration of status quo                                                                  | Allege specific grounds and willingness to restore consideration               |

### Statutory Damages and Fee-Shifting

| Statute                           | Statutory Damages                                         | Fee-Shifting                        | Treble Damages                   |
| --------------------------------- | --------------------------------------------------------- | ----------------------------------- | -------------------------------- |
| **Copyright Act (17 USC 504(c))** | $750-$30,000 per work ($150,000 if willful)               | Yes (17 USC 505)                    | No                               |
| **Lanham Act (15 USC 1117)**      | Attorney fees in exceptional cases                        | Yes (exceptional cases)             | Up to treble (15 USC 1117(a))    |
| **TCPA (47 USC 227)**             | $500 per violation ($1,500 if willful)                    | No federal; some state              | Treble for willful               |
| **FDCPA (15 USC 1692k)**          | Up to $1,000 (individual) / $500K or 1% net worth (class) | Yes                                 | No                               |
| **FCRA (15 USC 1681n)**           | $100-$1,000 per violation (willful)                       | Yes                                 | No                               |
| **Sherman Act (15 USC 15)**       | N/A                                                       | Yes                                 | Treble (mandatory)               |
| **RICO (18 USC 1964(c))**         | N/A                                                       | Yes                                 | Treble (mandatory)               |
| **Patent Act (35 USC 284)**       | Adequate to compensate; up to treble                      | Yes (exceptional cases, 35 USC 285) | Up to treble (willful)           |
| **Title VII (42 USC 2000e-5(k))** | Compensatory + punitive caps by employer size             | Yes (prevailing plaintiff)          | No                               |
| **DTSA (18 USC 1836(b))**         | N/A                                                       | Yes (bad faith)                     | Up to double (willful/malicious) |

### Ad Damnum Restrictions

Some jurisdictions prohibit stating a specific dollar amount:

| Jurisdiction   | Rule                                           | Effect                                                              |
| -------------- | ---------------------------------------------- | ------------------------------------------------------------------- |
| **New York**   | CPLR 3017(c) — personal injury/wrongful death  | Cannot state specific amount in complaint; state in separate notice |
| **California** | CCP 425.10(b) — personal injury/wrongful death | Cannot state amount; "damages according to proof"                   |
| **New Jersey** | Rule 4:5-2 — general                           | Ad damnum clause stating "in excess of" the jurisdictional amount   |
| **Virginia**   | Statute — personal injury                      | Cannot specify amount [VERIFY]                                      |
| **Federal**    | No prohibition                                 | May specify; affects amount in controversy for diversity            |

**Strategic note:** Even where not prohibited, consider whether stating a specific dollar amount helps (establishes amount-in-controversy for diversity) or hurts (creates a ceiling, invites media attention).

---

## Special Complaint Types — Additional Requirements

### Shareholder Derivative Complaint

Additional requirements beyond standard complaint:

1. **Standing**: Allege plaintiff was a shareholder at the time of the challenged transaction and remains a shareholder
2. **Demand requirement**: Either (a) allege demand was made and refused, or (b) allege demand futility
3. **Demand futility test**: Directors unable to exercise disinterested business judgment — typically uses Aronson v. Lewis (Delaware) or Universal Demand rule (MBCA) [VERIFY]
4. **Contemporaneous ownership**: Must allege share ownership at time of challenged conduct (FRCP 23.1)
5. **Fair and adequate representation**: Plaintiff must fairly represent shareholders' interests
6. **Verified complaint**: FRCP 23.1 requires complaint to be verified

### Qui Tam / False Claims Act Complaint

Additional requirements:

1. **Filed under seal**: Must be filed under seal for at least 60 days (31 USC 3730(b)(2))
2. **Served on government**: Copy served on US Attorney General and local US Attorney
3. **Written disclosure**: Must provide government with material evidence and information
4. **Rule 9(b)**: FCA claims sound in fraud — must plead with particularity
5. **Original source**: Relator must be original source of information (public disclosure bar)
6. **Government intervention**: Government has 60 days (extendable) to decide whether to intervene

### RICO Complaint

Additional requirements:

1. **Enterprise allegation**: Describe the association-in-fact enterprise or legal entity
2. **Pattern of racketeering**: At least 2 predicate acts within 10 years, with relationship and continuity
3. **Predicate acts**: Specifically allege each predicate act (if fraud-based, must meet Rule 9(b))
4. **Nexus**: Connection between pattern and enterprise
5. **RICO standing**: Injury to business or property (not personal injury)
6. **Causation**: "By reason of" the RICO violation

### Amended Complaint (Rule 15)

When drafting an amended complaint:

1. **Complete document**: Amended complaint is a stand-alone document replacing the original — do not reference "as previously alleged"
2. **Amendment as of right**: Within 21 days of serving original, OR within 21 days of service of responsive pleading or Rule 12 motion
3. **Leave of court**: After the as-of-right period; freely given "when justice so requires" (Foman v. Davis) [VERIFY]
4. **Relation-back**: New claims relate back to original filing date if they arise from the same conduct (Rule 15(c)(1)(B))
5. **New parties**: Relation-back for new parties requires notice within Rule 4(m) period and knew-or-should-have-known test (Rule 15(c)(1)(C))
6. **Identify changes**: Some local rules require redlining or identification of new material

---

## Anti-Patterns

### Drafting Anti-Patterns

1. **Shotgun pleading** — Incorporating all preceding paragraphs into every count without selectivity; courts (especially 11th Circuit) may dismiss or strike
2. **Group pleading without attribution** — "Defendants did X" when only one defendant acted; each defendant's conduct must be specifically alleged
3. **Conclusory element satisfaction** — "Defendant was negligent" without specific facts showing how duty was breached
4. **Kitchen sink claims without assessment** — Including every conceivable claim regardless of merit; dilutes strong claims and risks Rule 11 sanctions
5. **Narrative without structure** — Long fact section without paragraph numbering, headings, or logical organization
6. **Legal argument in the complaint** — Complaints allege facts, not legal arguments; save argument for briefs
7. **Inflammatory language** — Adjective-heavy, emotional language undermines credibility ("outrageous," "shocking," "unconscionable")
8. **Vague damages** — "Plaintiff suffered damages" without any specifics of harm type, causation, or magnitude

### Jurisdictional Anti-Patterns

9. **Missing jurisdiction** — Filing without adequate jurisdictional allegations; immediate dismissal under 12(b)(1)
10. **Citizenship vs. residence confusion** — For diversity, citizens (domicile) not residents; LLC citizenship requires all members
11. **Amount-in-controversy gap** — Failing to allege amount exceeds $75K for diversity (or exceeds by including non-compensatory relief not available under applicable law)
12. **Forum defendant rule ignorance** — Defendant sued in home state defeats removal; must be pled or addressed strategically

### Pleading Standard Anti-Patterns

13. **Pre-Twombly drafting** — Using Conley "no set of facts" notice pleading approach; complaints must now satisfy plausibility
14. **Rule 9(b) for non-fraud claims** — Applying heightened pleading when not required (wastes effort)
15. **Rule 9(b) avoidance for fraud claims** — Not meeting heightened pleading and hoping court won't notice; opposing counsel will move to dismiss
16. **PSLRA non-compliance** — Securities fraud complaint that fails to plead strong inference of scienter; automatic dismissal

### Strategic Anti-Patterns

17. **Statute of limitations ostrich** — Not checking limitations periods before filing; expired claims waste resources and invite sanctions
18. **Pre-suit requirement skip** — Filing Title VII without EEOC charge or tort claim without notice; dismissal for failure to exhaust
19. **Wrong defendant** — Suing parent instead of subsidiary (or vice versa) without piercing-the-veil allegations; wrong entity cannot be liable
20. **Doe defendant overuse** — Using Doe defendants without plan to identify through discovery; statute of limitations may expire
21. **Amendment afterthought** — Not preserving factual basis for potential additional claims; hard to add claims later without relation-back
22. **Ignoring local rules** — Federal districts have local rules on formatting, page limits, ECF requirements; non-compliance leads to rejection
23. **Prayer for relief incompleteness** — Omitting available remedies (attorney fees, injunctive relief, statutory damages) that must be requested

### Ethical Anti-Patterns

24. **Rule 11 disregard** — Filing claims without reasonable investigation of factual and legal basis
25. **Frivolous claims for leverage** — Including meritless claims to increase settlement pressure; sanctionable
26. **Misrepresenting facts** — Allegations contradicted by known evidence; duty of candor

---

## Writing Standards

1. **Numbered paragraphs**: Every allegation in its own numbered paragraph (FRCP 10(b))
2. **Active voice**: "Defendant breached the Agreement" not "The Agreement was breached by Defendant"
3. **Specific facts**: Names, dates, amounts, locations — not abstractions or conclusions
4. **Short paragraphs**: 1-3 sentences per paragraph; complex facts may require 4-5
5. **Present tense for ongoing matters**: "Plaintiff is a citizen of..." Present for status; past for events
6. **Defined terms**: Introduce defined terms at first use: "[Name] ('Defendant' or 'Smith')"
7. **Exhibit references**: "attached hereto as Exhibit A and incorporated herein by reference"
8. **Incorporation by reference**: "Plaintiff incorporates by reference paragraphs X through Y" at the start of each count
9. **Transitional language**: Minimal — complaints are structured documents, not narrative prose
10. **Professional tone**: Factual and dispassionate; let the facts speak for themselves

---

## External Tool Integration

### legalcode-mcp (Legal Research)

When available, use legalcode-mcp for:

- Verifying elements of causes of action in specific jurisdictions
- Checking statute of limitations periods
- Confirming pre-suit requirements
- Verifying current procedural rules and local rules

### WebSearch (Live Research)

Use WebSearch for:

- Confirming current pleading standards in specific courts
- Checking local rules for formatting requirements
- Verifying statute of limitations and tolling doctrines
- Finding recent case law on element definitions

**Search patterns:**

```
[cause of action] elements [jurisdiction] [year]
[court] local rules complaint format requirements
[claim type] pre-suit requirements [state]
[statute] statute of limitations [state] tolling
```

### Task Tool (Sub-Agent Delegation)

Use the Task tool for:

- Parallel element research across multiple causes of action
- Jurisdiction-specific rule verification
- Extended plausibility analysis for complex claims

### legalcode-damages-calculation (Companion Skill)

Use for structuring the prayer for relief:

- Calculate compensatory damage ranges
- Assess punitive damages availability and constitutional limits
- Identify applicable statutory damages and fee-shifting provisions

---

## Output Format Template

### Complete Complaint Package

The deliverable includes:

1. **Complaint Document** — Court-ready formatted complaint
2. **Element Mapping Table** — Shows which facts support which elements for each count
3. **Pre-Suit Requirement Status** — Checklist of all requirements and their status
4. **Plausibility Assessment** — Per-count analysis of Twombly/Iqbal compliance
5. **Strategic Notes** — Claims considered but omitted, alternative pleading rationale, amendment preservation
6. **Glass Box Audit Trail** — Full YAML audit block

### Element Mapping Table

| Count | Cause of Action    | Element                 | Factual Basis (¶¶)                          | Classification | Confidence | Notes                             |
| ----- | ------------------ | ----------------------- | ------------------------------------------- | -------------- | ---------- | --------------------------------- |
| I     | Breach of Contract | Valid contract          | ¶¶ 15-18 (Agreement attached as Ex. A)      | WELL-PLED      | 0.95       | Written agreement with signatures |
| I     | Breach of Contract | Plaintiff's performance | ¶¶ 19-22 (deliverables, invoices)           | WELL-PLED      | 0.90       | Supported by exhibits             |
| I     | Breach of Contract | Defendant's breach      | ¶¶ 23-28 (non-payment, specific amounts)    | WELL-PLED      | 0.92       | Dates and amounts specified       |
| I     | Breach of Contract | Damages                 | ¶¶ 29-30 ($250,000 unpaid + consequentials) | ADEQUATE       | 0.75       | Could specify consequentials more |
| III   | Fraud              | Scienter                | ¶ 45 ("knew or should have known")          | VULNERABLE     | 0.82       | Too conclusory for Rule 9(b)      |

---

## Common Weaknesses by Complaint Type

### Contract Complaints

- **Missing contract identification**: Failing to attach or specifically identify the contract (date, parties, subject matter)
- **Vague breach allegations**: "Defendant breached the contract" without specifying which provisions were breached and how
- **Conditions precedent gap**: Failing to allege plaintiff's own performance or excuse for non-performance
- **Damages conclusory**: Stating a damages number without alleging how damages flow from the breach
- **Missing consideration**: For oral contracts, failing to allege consideration exchanged
- **Integration clause blind spot**: Not addressing whether oral representations survived a written integration clause

### Tort Complaints

- **Duty generalization**: Alleging a "duty of care" without identifying its source (statutory, common-law relationship, voluntary undertaking)
- **Causation chain breaks**: Jumping from duty/breach to damages without specific proximate cause allegations
- **Foreseeability gap**: Failing to allege that harm was foreseeable (critical for negligence claims)
- **Comparative fault exposure**: Not anticipating affirmative defenses — proactively allege facts negating plaintiff's fault where possible
- **Emotional distress without physical manifestation**: In jurisdictions requiring physical injury for NIED, omitting physical symptom allegations
- **Statute of repose oversight**: For product liability, not checking whether the statute of repose (distinct from limitations) bars claims

### Fraud Complaints

- **Rule 9(b) failures**: The most common dismissal ground — missing who, what, when, where, how of the misrepresentation
- **Scienter by formula**: "Defendant knew or should have known" without specific facts showing knowledge
- **Reliance assumed**: Failing to allege that plaintiff actually relied on the misrepresentation and that reliance was reasonable
- **Omission claims without duty**: For fraud by omission, failing to establish the duty to disclose
- **Loss causation conflation**: Confusing transaction causation (induced the deal) with loss causation (caused the specific losses)

### Employment Complaints

- **Administrative exhaustion failures**: Filing suit before EEOC right-to-sue letter received or before state agency requirements met
- **Temporal gaps**: Long delay between protected activity and adverse action undermines retaliation claims — must allege close temporal proximity or continuing pattern
- **Comparator weakness**: Alleging disparate treatment without identifying similarly-situated comparators who received better treatment
- **At-will problem**: Wrongful termination claims that fail to identify the public policy, contractual, or statutory exception to at-will employment
- **Mixed-motive confusion**: Not distinguishing between pretext theory (the stated reason was false) and mixed-motive theory (both legitimate and illegitimate reasons, but the illegitimate one was a motivating factor)

### Class Action Complaints

- **Ascertainability failure**: Class defined by merits criteria rather than objective, administratively feasible criteria
- **Overbroad class**: Including persons not injured by defendant's conduct
- **Individual issues dominance**: Allegations that inherently require individualized proof (e.g., reliance in fraud) without addressing class-wide mechanism
- **Adequacy gaps**: Failing to allege why named plaintiff is adequate representative (no conflicts, will fairly protect class)
- **Numerosity by fiat**: "The class is so numerous that joinder is impracticable" without any factual basis for the number or why joinder fails

### Intellectual Property Complaints

- **Registration gaps**: Patent infringement without patent number and claim identification; copyright without registration number (or pending application) [JURISDICTION-SPECIFIC]
- **Indirect infringement without direct**: Alleging inducement or contributory infringement without first adequately alleging direct infringement by a third party
- **Trade secret identification**: Failing to identify the trade secret with reasonable particularity while maintaining its secrecy
- **Likelihood of confusion conclusory**: Trademark claims stating "confusion is likely" without alleging specific factors (similarity of marks, channels of trade, sophistication of consumers)

---

## Ethical Obligations Quick Reference

### Rule 11 / Certification Obligations [JURISDICTION-SPECIFIC]

**What you certify when filing** (FRCP Rule 11(b)):

1. **Not for improper purpose** — not filed to harass, cause unnecessary delay, or needlessly increase litigation cost
2. **Legal basis** — claims are warranted by existing law or by a non-frivolous argument for extending, modifying, or reversing existing law or establishing new law
3. **Factual basis** — factual contentions have evidentiary support or, if specifically identified, will likely have evidentiary support after a reasonable opportunity for further investigation or discovery
4. **Factual denials** — denials of factual contentions are warranted on the evidence or, if specifically identified, are reasonably based on belief or a lack of information

**Safe harbor**: Before filing a Rule 11 motion, the moving party must serve it on the other side and wait 21 days for correction. The drafting skill should flag any allegations that could trigger a Rule 11 challenge.

**Sanctions available**:

- Monetary (attorney's fees and expenses)
- Non-monetary (requiring legal education, reprimand)
- Against the attorney, law firm, or party (or both)
- Sanctions under § 1927 for "unreasonably and vexatiously" multiplying proceedings

### ABA Model Rule 3.1 — Meritorious Claims

> A lawyer shall not bring or defend a proceeding, or assert or controvert an issue therein, unless there is a basis in law and fact for doing so that is not frivolous. [VERIFY]

**Key implications for complaint drafting:**

- Each cause of action must have a good-faith factual and legal basis
- Alternative pleading is permitted — can plead inconsistent claims
- Criminal defense has a lower bar (may require prosecution to prove its case)
- "Not frivolous" is a lower bar than "will win" — a good-faith argument for a change in law suffices

### ABA Model Rule 3.3 — Candor to the Tribunal

- Cannot make false statements of fact or law to the court
- Applies to complaint allegations and verification/declaration under penalty of perjury
- Duty to correct if a material fact or law statement becomes false during the case

### Practical Ethical Checkpoints

Before filing, verify:

- [ ] Every factual allegation has a basis in client interview, documents, or identified investigation plan
- [ ] Every legal theory is supported by existing law or a non-frivolous extension argument
- [ ] No cause of action is included solely for settlement leverage without factual basis
- [ ] If using "upon information and belief," the belief has a reasonable factual basis
- [ ] Client has reviewed the complaint and confirmed factual accuracy (to the extent known)
- [ ] If verified complaint required, client understands they are signing under penalty of perjury
- [ ] Any "John Doe" defendants have a reasonable basis for inclusion (not fishing)
- [ ] Damages allegations have a factual basis (even if precise calculation is for later)
- [ ] Prior counsel's work product, if any, has been properly reviewed for accuracy
- [ ] No allegations are included that would waive attorney-client privilege or work product protection

---

## Complaint Drafting Quick-Start Checklist

Use this checklist to rapidly assess complaint readiness before detailed analysis:

**Phase 1 — Threshold Requirements**

- [ ] Statute of limitations checked for each cause of action
- [ ] Pre-suit requirements identified and satisfied (demand letters, exhaustion, certificates of merit)
- [ ] Standing confirmed (injury-in-fact, causation, redressability)
- [ ] Subject matter jurisdiction identified (federal question, diversity, supplemental)
- [ ] Personal jurisdiction basis identified for each defendant
- [ ] Venue proper under applicable rules
- [ ] Correct court identified (district, division, department)
- [ ] Filing fee known and prepared

**Phase 2 — Structural Completeness**

- [ ] Caption complete (court, parties, case number placeholder)
- [ ] Jurisdictional allegations present and specific
- [ ] All parties identified with sufficient detail (names, addresses, roles, citizenship for diversity)
- [ ] Factual allegations organized chronologically or thematically
- [ ] Each count clearly identified with cause of action label
- [ ] Each count incorporates relevant prior paragraphs by reference
- [ ] All elements of each cause of action pled with supporting facts
- [ ] Prayer for relief specifies each type of relief sought
- [ ] Jury demand included (if applicable)
- [ ] Verification/declaration included (if required)
- [ ] Attorney signature block with bar number

**Phase 3 — Pleading Standard Compliance**

- [ ] All allegations meet Twombly/Iqbal plausibility standard (not just conclusory)
- [ ] Fraud/mistake claims meet Rule 9(b) particularity (who, what, when, where, how)
- [ ] Securities fraud claims meet PSLRA requirements (if applicable)
- [ ] "Information and belief" allegations identify basis for belief
- [ ] No impermissible legal conclusions stated as factual allegations
- [ ] Hypothetical/alternative pleading clearly labeled as such

**Phase 4 — Strategic Review**

- [ ] Strongest claims presented first (or in most strategic order)
- [ ] Redundant claims evaluated (keep for safety or consolidate for clarity?)
- [ ] Amendment preservation — facts support potential future claims
- [ ] Discovery hooks — allegations positioned to unlock needed discovery
- [ ] No unnecessary admissions or damaging concessions
- [ ] Anticipated defenses addressed proactively where possible
- [ ] Co-defendant strategy — allegations attribute conduct to specific defendants
- [ ] Class action considerations (if applicable): ascertainability, commonality, typicality, adequacy, predominance, superiority

**Phase 5 — Final Quality Control**

- [ ] Paragraph numbering consecutive and correct
- [ ] Exhibit references match actual exhibits to be filed
- [ ] Dates, names, and amounts consistent throughout
- [ ] No placeholder text remaining ("[INSERT]", "TBD", etc.)
- [ ] Local rules formatting requirements met (font, margins, page limits)
- [ ] ECF/e-filing requirements reviewed
- [ ] Service requirements identified for each defendant
- [ ] Civil cover sheet prepared (if required)
- [ ] Corporate disclosure statement prepared (if applicable)
- [ ] Summons prepared for each defendant

---

## Localization Notes

### US Federal Localization

- Pleading standard: Twombly/Iqbal plausibility
- Complaint format: FRCP Rules 8, 9, 10
- Heightened pleading: Rule 9(b) (fraud), PSLRA (securities)
- Jurisdictional allegations: 28 USC 1331/1332/1367
- Jury demand: FRCP 38
- Pre-suit: Varies by claim type
- Local rules: Check specific district

### US State Localization

- [JURISDICTION-SPECIFIC]: Some states retain notice pleading; others adopt plausibility
- California: Judicial Council forms, CCP requirements, fact pleading standard
- New York: CPLR, verification requirements, ad damnum restrictions (CPLR 3017)
- Texas: TRCP, fact pleading in many claim types
- Florida: Specific requirements for punitive damages (leave of court required)

### England & Wales Localization

- Document: Particulars of Claim under CPR Part 16
- Statement of truth required (CPR 22)
- Statement of value required
- No jury (except defamation, fraud, malicious prosecution, false imprisonment) [VERIFY]
- Pre-action protocols mandatory [VERIFY]
- Limitation periods: Limitation Act 1980

### Australia Localization

- Document: Statement of Claim under Federal Court Rules 2011
- Concise statement of material facts (not evidence or law)
- General Steel Industries test for summary dismissal [VERIFY]
- Limitation periods vary by state/territory
- Originating application required in addition to statement of claim

### Localization Checklist

- [ ] Pleading standard matches jurisdiction
- [ ] Document format matches court requirements
- [ ] Element definitions reflect jurisdiction's substantive law
- [ ] Pre-suit requirements complete for jurisdiction
- [ ] Jurisdictional allegations appropriate for court
- [ ] Damages/prayer restrictions addressed
- [ ] Local rules reviewed and incorporated
- [ ] Citation format matches jurisdiction convention
- [ ] Verification/statement of truth included if required
- [ ] Service requirements noted

---

## Provenance

This skill was created as a Legalcode original synthesis using multi-agent
research methodology.

**Research methodology:**

- 6 parallel research agents (Opus) conducted domain-specific web research
- Research domains: pleading standards (Twombly/Iqbal/Rule 9(b)), causes of action elements (23 claim types), complaint structure (US/UK/AU formats), jurisdiction and venue (SMJ/PJ/standing), strategic drafting (claim selection/amendment/pitfalls), remedies and prayer for relief
- Findings synthesized into unified skill by orchestrator agent

**Key reference frameworks:**

- Bell Atlantic Corp. v. Twombly, 550 U.S. 544 (2007) — plausibility pleading [VERIFY]
- Ashcroft v. Iqbal, 556 U.S. 662 (2009) — extending plausibility to all civil actions [VERIFY]
- FRCP Rules 8, 9, 10, 11, 12, 15, 23 — federal complaint requirements [VERIFY]
- CPR Part 16, PD 16 — England & Wales Particulars of Claim [VERIFY]
- Federal Court Rules 2011 (Australia) — Statement of Claim [VERIFY]
- ABA Model Rule 3.1 — meritorious claims and contentions [VERIFY]
- Restatement (Second) of Torts — element definitions for tort claims [VERIFY]
- Restatement (Second) of Contracts — element definitions for contract claims [VERIFY]

**Research artifacts:**

- Research findings from 6 parallel agents available in team workspace
- Web search results cached for verification

**Skill version:** 1.0
**Created:** 2026-03-01
**Created by:** Legalcode multi-agent research pipeline
