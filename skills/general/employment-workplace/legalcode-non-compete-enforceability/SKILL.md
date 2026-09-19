---
name: legalcode-non-compete-enforceability
description: Analyse non-compete clause enforceability across all 50 US states and DC — screen for ban
  states (California, Minnesota, North Dakota, Oklahoma, Wyoming), evaluate income threshold requirements,
  assess reasonableness of duration/geographic/activity scope, apply blue-pencil/red-pencil/reformation
  doctrine, review consideration adequacy, and generate a jurisdiction-specific enforceability risk matrix
  with recommended structural modifications. Use when reviewing non-compete provisions in employment agreements,
  executive offer letters, severance agreements, or acquisition-related restrictions; evaluating post-employment
  covenant litigation risk; auditing a workforce's non-compete portfolio for compliance with recent state
  law changes (Minnesota 2023, California SB 699 2024, Wyoming 2025, FTC rule vacatur August 2024); advising
  on multi-state employee populations; or structuring new non-competes to maximise enforceability.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Analyse non-compete clause enforceability across all 50 US states and DC — screen for ban states (California, Minnesota, North Dakota, Oklahoma, Wyoming), evaluate income threshold requirements, assess reasonableness of duration/geographic/activity scope, apply blue-pencil/red-pencil/reformation doctrine, review consideration adequacy, and generate a jurisdiction-specific enforceability risk matrix with recommended structural modifications. Use when reviewing non-compete provisions in employment agreements, executive offer letters, severance agreements, or acquisition-related restrictions; evaluating post-employment covenant litigation risk; auditing a workforce's non-compete portfolio for compliance with recent state law changes (Minnesota 2023, California SB 699 2024, Wyoming 2025, FTC rule vacatur August 2024); advising on multi-state employee populations; or structuring new non-competes to maximise enforceability. Covers: full 50-state + DC enforceability matrix; FTC Non-Compete Rule status (vacated, Section 5 pivot); garden leave mechanics; DTSA/UTSA trade secret overlay; industry-specific exemptions (physicians, broadcasters, healthcare workers); choice-of-law enforceability; and remediation redlines. Produces GREEN/YELLOW/RED/BAN-STATE classification with confidence-scored enforceability assessment and auditable Glass Box trail.


# Legalcode Non-Compete Enforceability

> **Disclaimer**: This skill provides a framework for AI-assisted non-compete enforceability
> analysis. It does not constitute legal advice. All outputs require review by a qualified
> employment lawyer licensed in the relevant jurisdiction(s) before relying on them for any
> enforcement, litigation, compliance, or negotiation decision. Non-compete law — particularly
> state statutory bans, salary thresholds, and blue-pencil doctrine — changes frequently and
> varies dramatically by jurisdiction; verify current applicability before acting. Salary
> thresholds are adjusted annually by regulation in Colorado, Illinois, Washington, Oregon,
> and other states — always verify current figures. Statutory and case law references cited
> from memory carry hallucination risk — verify against authoritative sources before relying
> on them. This skill does not substitute for individual legal advice regarding specific
> employment situations, non-compete enforcement strategy, or litigation defence.

---

## Purpose and Scope

This skill analyses whether a non-compete clause is enforceable under the applicable
jurisdiction's law, identifies risk factors that courts consider when determining
enforceability, generates confidence-scored enforceability assessments, and produces
actionable redline suggestions and structural modifications to maximise enforceability
or litigation-defence position.

**Covers:**

- Full 50-state + DC non-compete enforceability matrix with statutory citations
- Ban state identification (CA, MN, ND, OK, WY) with jurisdiction-override analysis
- Income threshold screening (10+ states + DC) with current salary figures [VERIFY annually]
- Consideration requirement evaluation (at-will vs. additional; mid-employment timing)
- Duration, geographic scope, and activity scope reasonableness analysis
- Blue-pencil / red-pencil / reformation doctrine — state-by-state application
- Garden leave mechanics and payment requirements (US + international)
- FTC Non-Compete Rule status: vacated Aug 20, 2024; Section 5 case-by-case enforcement pivot
- DTSA / UTSA trade secret overlay and enforceability interaction
- Industry-specific exemptions (physicians, broadcasters, healthcare workers, technology)
- Choice-of-law and forum selection enforceability analysis
- Enforceability risk matrix by jurisdiction with remediation redlines
- Confidence scoring (0.0–1.0) with Glass Box audit trail

**Does not:**

- Draft new non-compete clauses from scratch (see `legalcode-employment-agreement-review`)
- Provide personal legal advice or guarantee court outcomes — courts apply fact-specific tests
- Analyse non-solicitation or non-disclosure covenants separately (see `legalcode-nda-triage`)
- Perform comprehensive trade secret misappropriation analysis beyond the DTSA/UTSA overlay
- Cover non-compete provisions in franchise agreements (different legal framework applies)
- Cover international jurisdictions as primary analysis (US-focused; international markers provided)

**Related skills:**

- `legalcode-employment-agreement-review` — full employment agreement clause-by-clause review
- `legalcode-nda-triage` — NDA and non-disclosure covenant review
- `legalcode-contract-review` — general commercial contract review methodology

---

## Jurisdiction and Governing Law

Non-compete law is **entirely state-law governed**. There is no operative federal non-compete
statute. The FTC Non-Compete Rule (16 CFR Part 910) was vacated August 20, 2024 and never
took effect; the FTC's appeal was abandoned September 5, 2025. The FTC now pursues
case-by-case enforcement via Section 5 of the FTC Act (see Section 12: FTC Status).

**The critical principle: Work location governs enforceability.** The employee's primary
work location jurisdiction determines enforceability, which may **override** the contractual
choice-of-law clause. A Texas governing-law clause does not make a California non-compete
enforceable.

**Jurisdiction detection — identify at Step 2:**

1. Contractual choice of law (stated in agreement)
2. Employee's primary work location (actual work state, not just employer HQ)
3. States where the employee may occasionally work (secondary nexus)
4. Employee's state of residence (relevant in some jurisdictions)

**Mandatory override states (choice of law cannot save the non-compete):**

| State            | Override Rule                                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **California**   | Cal. Bus. & Prof. Code § 16600 voids non-competes regardless of contractual choice of law; SB 699 (eff. Jan. 1, 2024) — any non-compete signed outside CA is void if employee works in CA |
| **Minnesota**    | Minn. Stat. § 181.988 — employers may not require any non-compete (post-July 1, 2023 agreements); void regardless of choice of law                                                        |
| **North Dakota** | NDCC § 9-08-06 — void as against public policy; applies regardless of choice of law                                                                                                       |
| **Oklahoma**     | 15 Okla. Stat. § 219A — void; sale-of-business exception only; applies regardless of choice of law                                                                                        |
| **Wyoming**      | Senate File 107 (eff. July 1, 2025) — void for employment relationships regardless of choice of law [VERIFY implementation details]                                                       |

**Restricted states:** Washington, Colorado, Illinois, Oregon, Massachusetts, Maine, Maryland,
Nevada, New Hampshire, Rhode Island, Virginia, and DC impose income thresholds, duration limits,
notice requirements, or garden leave obligations. The **work location state's requirements apply**
regardless of the contractual choice of law in many of these states.

[JURISDICTION-SPECIFIC] For international employees, apply the governing law of the employee's
work location (see Section 11 for UK, Germany, France, Australia, India overview). International
non-competes require local employment law advice.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points marked **⟁ CLARIFY**
throughout the workflow. Rather than assuming context, the analysis pauses when:

- The employee's work location is ambiguous (critical for jurisdiction override analysis)
- The choice of law differs from the work location (triggering override analysis)
- The agreement timing (new hire vs. mid-employment) affects consideration adequacy
- The employee's compensation level is unknown (triggers income threshold screening)
- Additional consideration beyond continued employment is unclear
- The industry or role is unclear (triggers industry-exemption screening)

Present clarification questions as structured options with brief "Why this matters" explanations.
If context has already been provided, skip the question and **state your assumption explicitly**
(e.g., "I'm assuming the employee works in Texas; correct me if different").

---

## Workflow

### Step 1: Accept Input

Accept the non-compete clause in any of these formats:

- **Clause text:** Pasted directly from the employment agreement
- **Full agreement:** PDF, DOCX, or full employment agreement text (skill extracts the clause)
- **Description:** User describes the non-compete terms verbally (duration, geography, activity)
- **Multiple clauses:** Set of non-compete clauses from a workforce audit or M&A diligence

If no clause is provided, ask: "Please share the non-compete clause text or describe its key
terms (duration, geographic scope, restricted activities, and any compensation during restriction)."

---

### Step 2: Gather Jurisdictional and Factual Context

**⟁ CLARIFY** — Before analysing enforceability, confirm these facts. Present as structured
questions. If any are already answered, skip and state the assumption.

**1. Where does the employee work?** (Primary work location — this is the critical question.)

- Options: [Specific US state], Multiple states (identify primary + secondary), Remote (identify
  home state), International (identify country + US nexus if any)
- _Why this matters_: Work-location state law governs enforceability. A Texas choice-of-law
  clause is irrelevant if the employee works in California — the non-compete is void.

**2. What does the agreement say about governing law?**

- Options: States [specific state], Silent / no governing law clause, Ambiguous
- _Why this matters_: Identifies whether a choice-of-law override analysis is needed.

**3. When was (or will be) the agreement signed?**

- Options: New hire / pre-employment (signed at or before start date), Mid-employment (signed
  after start date during employment), Promotion or amendment (existing employee, new terms),
  Separation / severance (signed at termination or layoff), Unknown
- _Why this matters_: At-will continuation of employment is insufficient consideration for
  mid-employment amendments in many restricted states. Timing is a binary enforceability gate.

**4. What is the employee's compensation level?**

- Options: State the annual salary (helps me screen income thresholds), Unknown, Not applicable
- _Why this matters_: Ten states + DC ban non-competes for employees below statutory income
  thresholds. If the employee earns below the threshold, the non-compete is void regardless
  of other enforceability factors.

**5. What is the employee's role / industry?**

- Options: General professional / office worker, Healthcare practitioner (physician, nurse, etc.),
  Broadcaster / media professional, Technology / software engineer, Sales professional, Other
  (describe), Unknown
- _Why this matters_: Some states have industry-specific bans or exemptions — physicians,
  broadcasters, and healthcare workers may be treated differently regardless of salary.

---

### Step 3: Extract Clause Terms

From the provided non-compete text or description, extract:

| Element                           | Extracted Value                                                                       | Notes                           |
| --------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------- |
| Duration                          | [X months / years]                                                                    |                                 |
| Geographic scope                  | [Nationwide / State / County / Customer-based / None stated]                          |                                 |
| Activity scope                    | [All competing business / Specific role / Specific products / Specific customers]     |                                 |
| Compensation during restriction   | [None / Garden leave amount / Other]                                                  |                                 |
| Legitimate interest stated        | [Trade secrets / Customer relationships / Confidential info / Training / None stated] |                                 |
| Blue-pencil / severability clause | [Present / Absent]                                                                    | Quote exact language if present |
| Consideration stated              | [Employment offer / Salary increase / Equity / Continued employment / None stated]    |                                 |
| Notice requirements               | [X days advance notice / None / Unknown]                                              |                                 |
| Carve-outs / exceptions           | [List any expressly carved out activities, customers, or geographies]                 |                                 |

If any element is absent or ambiguous, **⟁ CLARIFY** with the user before proceeding.

---

### Step 4: Apply Ban State and Income Threshold Screening

**4a. Ban state check** — Apply immediately before any further analysis.

Check the employee's work location against the **Non-Compete Enforceability Matrix** (Section 7).
If the work location is a ban state, stop and return:

> **⛔ BAN STATE — NON-COMPETE IS VOID**
> Employee works in [State]. [State] law voids non-compete agreements [with/without exceptions].
> No enforceability analysis is possible. The clause cannot be enforced regardless of its terms
> or the contractual choice of law.
> **Recommended action**: [See Section 7 for state-specific exceptions; focus on DTSA/UTSA
>
> > trade secret protection as the alternative enforcement mechanism — see Section 13.]

**4b. Income threshold check** — For non-ban states with salary minimums.

If the employee's compensation is below the applicable state threshold (see matrix), flag:

> **⚠️ INCOME THRESHOLD FAILURE — NON-COMPETE IS VOID**
> Employee earns $[X], below [State]'s minimum threshold of $[Y] [VERIFY current year figure].
> The non-compete cannot be enforced regardless of its scope or other terms.
> **Recommended action**: Omit non-compete for this employee. Consider whether non-disclosure
> and limited non-solicitation protections would be valid (different thresholds may apply).

---

### Step 5: Apply the Three-Prong Reasonableness Test

For states not subject to ban or income-threshold failure, apply the common-law three-prong test:

**Prong 1 — Legitimate Protectable Interest**
The employer must have a legitimate business interest the non-compete protects. Accepted interests:

- Trade secrets and confidential proprietary information
- Substantial relationships with specific prospective or existing customers
- Customer goodwill associated with a specific geographic area or trade name
- Extraordinary or specialised employee training (where employer invested significantly)

**Prong 2 — Reasonableness of Scope**
The restriction must be reasonably necessary to protect the legitimate interest:

- **Duration**: See duration benchmarks in Section 6 (Scope Analysis)
- **Geographic scope**: Must correlate to where the employer actually operates or where the
  employee had customer contact — nationwide restrictions are presumptively overbroad unless
  the business is truly national and employee had national responsibility
- **Activity scope**: Must be limited to competitive activities that would harm the protectable
  interest — "any competing business regardless of role" is presumptively overbroad

**Prong 3 — Not Unduly Harmful to Public Interest**
The restriction must not be contrary to the public interest. Courts examine:

- Healthcare access (physician non-competes in underserved areas attract heightened scrutiny)
- Consumer choice and competition
- Employee's ability to earn a living in their field

**If any prong fails:** Classify as RED. Apply blue-pencil/red-pencil analysis (Step 7) to
determine whether a court would modify the clause or void it entirely.

---

### Step 6: Consideration Adequacy Analysis

Evaluate whether the non-compete is supported by adequate consideration.

**At new hire (pre-employment offer stage):**

- Employment offer alone is sufficient consideration in virtually all US states
- Exception: Some states require advance notice (e.g., Massachusetts: 7 business days;
  Illinois: 14 calendar days)
- Exception: Some states require the agreement to be provided before the first day of work
- Risk level: LOW — consideration is generally adequate

**At mid-employment (existing employee, new agreement or amendment):**

- Continued at-will employment alone is insufficient in many restricted states
- States requiring additional consideration for mid-employment amendments:
  - **Washington** (RCW 49.62): "garden leave or equivalent consideration" required
  - **Colorado** (CRS § 8-2-113): "adequate consideration" required (more than continued employment)
  - **Illinois** (820 ILCS 90/5): "adequate consideration" — minimum two years of employment
    after signing, or some other adequate consideration
  - **Massachusetts** (M.G.L. c. 149, § 24L): 10 business days advance notice; "garden leave
    or other mutually-agreed-upon consideration"
  - **Texas**: Continued at-will employment is insufficient post-_Light v. Centel Cellular_,
    883 S.W.2d 642 (Tex. 1994) unless the covenant is ancillary to an otherwise-enforceable
    agreement with independent consideration
- Risk level: HIGH if only consideration is continued employment
- **Redline**: Add specific additional consideration (salary increase, equity grant, signing
  bonus, or defined garden leave) and document it in the agreement

**At separation / severance (signed at termination):**

- Consideration: Severance payment serves as consideration (must be specific — "two weeks'
  pay in exchange for these restrictive covenants")
- Risk: If the employee has already resigned and is signing a separation agreement, confirm
  the severance amount is more than nominal
- **Redline**: Explicitly tie the restriction to the severance: "In consideration of the
  [X weeks / months] severance payment described in Section [Y], Employee agrees to the
  restrictions set forth in Section [Z]."

**⟁ CLARIFY** — If the consideration is ambiguous from the clause text, ask: "Was additional
consideration (such as a salary increase, bonus, equity grant, or defined garden leave) provided
alongside this agreement, beyond continued employment?"

---

### Step 7: Scope Analysis — Duration, Geography, and Activity

#### 7a. Duration Analysis

| Duration     | Enforceability Assessment                                                                                                  |
| ------------ | -------------------------------------------------------------------------------------------------------------------------- |
| ≤ 6 months   | Presumptively reasonable in virtually all states; strong enforceability signal                                             |
| 7–12 months  | Generally reasonable for most professional employees; standard market range                                                |
| 13–18 months | Elevated scrutiny; supportable if employee had significant customer relationships or access to long-term trade secrets     |
| 19–24 months | High scrutiny; many courts view as outer limit of reasonableness                                                           |
| > 24 months  | Presumptively unreasonable in most jurisdictions; Florida's § 542.335 explicitly creates this presumption; strong RED flag |

State-specific duration limits (see matrix): Colorado (12 months), Massachusetts (12 months),
Oregon (12 months), Washington (18 months), UK (typically 3–12 months reasonableness test).

#### 7b. Geographic Scope Analysis

| Scope                                             | Enforceability Assessment                                                                                                    |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Nationwide / global                               | Presumptively overbroad unless business is truly nationwide and employee had nationwide responsibility; scrutinise carefully |
| Multi-state (defined region)                      | Acceptable if employee's actual responsibilities covered the region                                                          |
| Single state                                      | Generally reasonable for state-level operations; widely enforced                                                             |
| County / metro area                               | Strong enforceability; correlates to actual competitive harm zone                                                            |
| Customer-based ("wherever customers are located") | Acceptable only if paired with specific customer identification; "wherever any customer exists" is overbroad                 |
| Activity-based only (no geographic limit)         | Permissible in some states; check state-specific rules                                                                       |

**⟁ CLARIFY** — If the geographic scope is ambiguous (e.g., "in any market where the Company
does business"), ask: "What was the employee's actual geographic territory or responsibility area?"

#### 7c. Activity Scope Analysis

| Activity Scope                                                              | Enforceability Assessment                                        |
| --------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Limited to employee's actual role or product lines                          | Strong — correlates to protectable interest                      |
| Specific named competitors                                                  | Strong — clear and limited scope                                 |
| "Competing business" in the same industry                                   | Moderate — acceptable if industry-specific and duration is short |
| "Any business that competes with any product or service the Company offers" | OVERBROAD — RED flag; many courts will void or blue-pencil       |
| "Any business in which Company has an interest"                             | Void as overbroad in most jurisdictions                          |

---

### Step 8: Blue-Pencil / Red-Pencil / Reformation Doctrine

Apply the appropriate doctrine for the work-location state (see Section 8 for full state list).

**Blue-Pencil Doctrine:** Courts strike out the offending provision but do not rewrite it.
Only provisions that can be excised without rewriting the remaining clause are saved.

- Effect: An overbroad geographic restriction might be struck; the temporal restriction survives
- Limitation: Courts cannot add language — they can only delete
- States (partial list): Arizona, Connecticut, Georgia (by statute), Indiana, Louisiana,
  Maryland, North Carolina, Rhode Island

**Reformation / Purple-Pencil Doctrine:** Courts rewrite the clause to make it reasonably
enforceable. This is the most employer-friendly approach.

- Effect: A 36-month nationwide restriction might be reformed to 12 months in a specific state
- Florida: **Mandatory** reformation by statute (Fla. Stat. § 542.335 — court shall modify)
- States (partial list): Colorado, Florida (mandatory), Illinois, Massachusetts, Nevada, Ohio,
  Pennsylvania, Texas, Washington

**Red-Pencil / Anti-Blue-Pencil Doctrine:** If any provision is unreasonable, the entire
non-compete covenant is void. Courts do not modify or save any part of it.

- Effect: A single overbroad term voids the entire clause
- States (partial list): Nebraska [VERIFY], South Carolina [VERIFY], Virginia [VERIFY],
  Wisconsin [VERIFY]
- Risk implication: Drafting a somewhat overbroad clause hoping a court will reform it is
  **dangerous** in red-pencil states — the entire clause may be voided

**Drafting guidance based on doctrine:**

- In **reformation** states: Include explicit severability language: "If any restriction in
  this Section is found unenforceable as written, the reviewing court is authorised and
  directed to modify such restriction to the minimum extent necessary to make it enforceable."
- In **blue-pencil** states: Draft each restriction as a separate, severable clause so that
  voiding one does not void others
- In **red-pencil** states: Draft conservatively — do not overreach, as there is no judicial
  safety net

---

### Step 9: Generate Enforceability Score and Redlines

**9a. Enforceability Classification**

Assign one of four classifications based on the analysis:

| Classification   | Score Range | Meaning                                  | Action                                                        |
| ---------------- | ----------- | ---------------------------------------- | ------------------------------------------------------------- |
| **🟢 GREEN**     | 0.80–1.0    | Highly likely to be enforced             | Enforce as written; minor redlines only                       |
| **🟡 YELLOW**    | 0.60–0.79   | Moderately enforceable; overbreadth risk | Redline to reduce scope; enforceable if modifications adopted |
| **🔴 RED**       | 0.20–0.59   | Significant unenforceability risk        | Substantial redlines required; litigation risk is high        |
| **⛔ BAN STATE** | 0.0         | Void by operation of law                 | Cannot be enforced; focus on DTSA/UTSA protection             |

**9b. Redline Generation**

For each enforceability weakness identified, generate a redline suggestion:

_Duration overbreadth:_

> **Current:** "for a period of thirty-six (36) months following termination"
> **Redline:** "for a period of twelve (12) months following termination"
> **Rationale:** 36 months exceeds reasonableness benchmarks in [State]; 12 months is
> within the defensible range and consistent with the protection of the stated legitimate
> interest ([specify interest]).
> **Confidence:** [HIGH / PROBABLE] — [brief rationale]

_Geographic overbreadth:_

> **Current:** "in any state or country where Company does business"
> **Redline:** "within the [specific geographic area correlating to employee's territory]"
> **Rationale:** Current scope is nationwide/global; court in [State] is unlikely to enforce
> absent evidence that employee had nationwide responsibility. Narrowing to actual territory
> preserves the protectable interest while reducing litigation risk.

_Activity scope overbreadth:_

> **Current:** "from engaging in any business that competes with any product or service
> offered by Company"
> **Redline:** "from engaging in [specific role or product line] for any company that
> directly competes with Company's [specific business line or named competitors]"
> **Rationale:** "Any business that competes" without limitation is overbroad in virtually
> all jurisdictions; ties restriction to employee's actual knowledge and role.

_Consideration deficiency:_

> **Current:** No explicit consideration stated; continued employment only
> **Redline:** Add: "In consideration of the [describe: equity grant / salary increase of
>
> > $X / signing bonus of $X], the sufficiency of which Employee acknowledges, Employee agrees
> > to the following restrictive covenants..."
> > **Rationale:** Continued at-will employment is insufficient consideration in [State];
> > specific additional consideration is required for this agreement to be binding.

---

### Step 10: Glass Box Audit Trail

Append a completed Glass Box audit section to every output (template in Section 15).

---

## Section 6: Enforceability Frameworks

### 6.1 Protectable Interest Categories

Courts recognise these categories as supporting non-compete enforcement:

| Interest                                            | Enforceability Weight                                     | Notes                                                                                    |
| --------------------------------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Trade secrets / proprietary formulas**            | HIGH — clearest protectable interest                      | Must actually be secret; public information doesn't qualify                              |
| **Confidential customer lists and relationships**   | HIGH — well-established in most states                    | Must be genuinely non-public; customer names found in public directories may not qualify |
| **Specially trained employees (employer-invested)** | MODERATE — some states have reduced this post-FTC climate | Training must be extraordinary, not standard industry education                          |
| **Customer goodwill in a territory**                | MODERATE — geographically specific                        | Supports geographic limitation; supports shorter restrictions                            |
| **Confidential business strategies / pricing**      | MODERATE — must actually be confidential                  | NDCA alone (without non-compete) may be sufficient protection                            |

---

## Section 7: Non-Compete Enforceability Matrix — All 50 States + DC

> **Currency Warning:** State non-compete law is changing rapidly (2023–2025 legislative
> activity is unusually high). Salary thresholds in Colorado, Washington, Oregon, Illinois,
> DC, Maine, Maryland, New Hampshire, Rhode Island, and Virginia adjust annually. Always
> verify current figures before relying on this matrix. Entries marked [VERIFY] carry higher
> hallucination risk — confirm against current state statutes.

### 7.1 Full Ban States — Non-Compete is Void

| State            | Key Statute                                                            | Effective Date                                 | Exceptions                                                                                         | Override Rule                                                                                                                                                            |
| ---------------- | ---------------------------------------------------------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **California**   | Cal. Bus. & Prof. Code §§ 16600–16600.5; SB 699 (2024); AB 1076 (2024) | § 16600 longstanding; SB 699 eff. Jan. 1, 2024 | Sale of business (§ 16601); dissolution / disassociation of partnership (§ 16602); LLC (§ 16602.5) | Any NC signed anywhere is void if employee works in CA; private right of action for violations; employer must notify employees of unenforceable NCs                      |
| **Minnesota**    | Minn. Stat. § 181.988                                                  | July 1, 2023 (new / amended agreements)        | Sale of business [VERIFY scope]                                                                    | Agreements entered into or materially amended after July 1, 2023 are void; prior agreements not retroactively voided; employee may seek treble damages and attorney fees |
| **North Dakota** | NDCC § 9-08-06                                                         | Longstanding                                   | Sale of business (§ 9-08-06(3)); sale of goodwill; dissolution of partnership                      | Void as against public policy; choice-of-law clause cannot override                                                                                                      |
| **Oklahoma**     | 15 Okla. Stat. § 219A                                                  | Longstanding                                   | Sale of business; dissolution of partnership [VERIFY]                                              | All employment non-competes void; limited non-solicitation of customers may be permitted [VERIFY]                                                                        |
| **Wyoming**      | Senate File 107                                                        | July 1, 2025                                   | Sale of business [VERIFY]; possible professional exceptions [VERIFY]                               | [VERIFY full implementation details — very recent enactment]                                                                                                             |

**Ban state enforcement exposure:** California AB 1076 (2024) imposes an obligation on employers
to notify employees with void non-competes that the clauses are unenforceable. Failure to
notify may expose employers to civil penalties. [VERIFY current enforcement posture]

---

### 7.2 Heavily Restricted States — Income Thresholds + Additional Requirements

| State             | Statute                                                  | Income Threshold (NC)       | Income Threshold (Non-Solicit) | Max Duration | Garden Leave / Consideration                                                                              | Notice Required                                                                             | Doctrine    |
| ----------------- | -------------------------------------------------------- | --------------------------- | ------------------------------ | ------------ | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ----------- |
| **Colorado**      | CRS § 8-2-113 (eff. Aug. 10, 2022)                       | $127,091/yr [VERIFY 2026]   | $76,254.60/yr [VERIFY 2026]    | 12 months    | Yes — garden leave or equivalent consideration                                                            | Yes — must provide copy with offer letter                                                   | Reformation |
| **Illinois**      | 820 ILCS 90/10 (eff. Jan. 1, 2022)                       | $75,000/yr [VERIFY current] | $45,000/yr [VERIFY current]    | 2 years      | Yes — "adequate consideration" (incl. garden leave ≥ 14 calendar days)                                    | Yes — 14 calendar days to review                                                            | Reformation |
| **Massachusetts** | M.G.L. c. 149, § 24L (eff. Oct. 1, 2018)                 | No threshold [VERIFY]       | Different rules apply          | 12 months    | Yes — garden leave (≥50% of base salary) OR other mutually-agreed consideration                           | Yes — 10 business days before start / before material change; advance notice on signed copy | Reformation |
| **Oregon**        | ORS 653.295 (eff. 2022 amendments)                       | $113,241/yr [VERIFY 2026]   | Different rules                | 12 months    | Yes — garden leave or base salary equivalent                                                              | Yes — written agreement; advance notice                                                     | Reformation |
| **Washington**    | RCW 49.62 (eff. Jan. 1, 2020; SB 5935 eff. June 6, 2024) | $120,559/yr [VERIFY 2026]   | Narrower definition            | 18 months    | Yes — garden leave (or equivalent) required; SB 5935 adds garden leave requirement for laid-off employees | Yes — must disclose before or at acceptance                                                 | Reformation |

**Colorado 2025 thresholds note:** CDLE adjusts thresholds annually based on Colorado Average
Weekly Wage (CAWW). The 2025 figures ($127,091 NC / $76,254.60 NS) are effective January 1, 2025.
[VERIFY 2026 figures with CDLE]

**Washington SB 5935 (2024) note:** Added garden leave requirements specifically for employees
who are **laid off** — a laid-off employee subject to a non-compete must receive garden leave
pay equal to base salary throughout the restricted period, or the clause is unenforceable.

---

### 7.3 Moderately Restricted States — Salary Minimums for Low-Wage Workers

| State             | Key Restriction                                                       | Income Threshold                             | Key Statute                                                 |
| ----------------- | --------------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------- |
| **DC**            | Non-compete prohibited for covered workers                            | $154,200/yr (highly paid exception) [VERIFY] | DC Code § 32-581.01 et seq.                                 |
| **Maine**         | Non-compete restricted; advance disclosure required                   | $60,240/yr (low-wage exemption)              | M.R.S.A. §599-A (2019 amendments)                           |
| **Maryland**      | Non-compete void for low-wage workers; healthcare restrictions 2025   | $46,800/yr threshold [VERIFY]                | Md. Lab. & Empl. Code Ann. § 3-716; HB 1388 (2025) [VERIFY] |
| **Nevada**        | Narrowly construed; limited to employees with access to trade secrets | No threshold                                 | NRS 613.195 (2017)                                          |
| **New Hampshire** | Non-compete void for certain employees                                | $30,160/yr [VERIFY]                          | RSA 275:70-a                                                |
| **New York**      | Evolving; 2024 bill signed — implementation disputed [VERIFY]         | TBD — [VERIFY 2026 status]                   | NY S3100A (signed Jan. 2024) [VERIFY enforceability]        |
| **Rhode Island**  | Non-compete void for low-wage workers                                 | $37,650/yr [VERIFY]                          | R.I. Gen. Laws § 28-59-3 (2016)                             |
| **Virginia**      | Non-compete void for "low-wage employees"                             | $73,320/yr [VERIFY 2026]                     | Va. Code § 40.1-28.7:8 (2020)                               |

**New York 2024 note:** Governor Hochul signed legislation restricting non-competes in January 2024. Implementation and enforceability have been subject to legal challenge and regulatory
interpretation. [VERIFY current status with New York State Department of Labor]

---

### 7.4 Healthcare-Specific Restrictions

Several states have enacted or are enacting special rules for healthcare practitioners:

| State            | Restriction                                                                                               | Statute / Source                                                    | Effective    |
| ---------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------ |
| **Pennsylvania** | Non-competes for healthcare practitioners limited to 1 year; void if employer terminates the practitioner | Fair Contracting for Health Care Practitioners Act (Act 74 of 2024) | Jan. 1, 2025 |
| **Indiana**      | Hospital-employed physicians — additional restrictions on non-competes                                    | HEA 1289 (2025)                                                     | July 1, 2025 |
| **Kentucky**     | Physician non-competes — additional limitations [VERIFY scope]                                            | KRS § 311.371 [VERIFY]                                              | Longstanding |
| **Colorado**     | Physicians: non-compete must allow patients to be notified of departure                                   | CRS § 8-2-113(3)(b)                                                 | Existing     |
| **Tennessee**    | Healthcare professionals — limitations apply                                                              | Tenn. Code § 63-6-204 [VERIFY]                                      | [VERIFY]     |
| **Texas**        | Physician exception: non-compete must allow patient records access; buyout right                          | Tex. Bus. & Com. Code § 15.50(b)                                    | Existing     |

**Trend note:** Physician non-compete restrictions are accelerating at the state level.
17+ states have existing healthcare-specific restrictions as of 2025. This is a high-velocity
legislative area — always verify current state statutes for healthcare-practitioner clients.

---

### 7.5 Generally Enforceable States — Common Law Reasonableness

The following states apply the common-law three-prong reasonableness test (see Section 5)
without statutory income thresholds or bans, though all have case law limiting overbroad clauses:

**Employer-Friendly (strong enforcement culture):**

| State           | Key Features                                                                        | Statute / Case Law                                                      |
| --------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Florida**     | Mandatory reformation; statutory presumptions; employer-friendly burden-shifting    | Fla. Stat. § 542.335; CHOICE Act (July 1, 2025) strengthens further     |
| **Georgia**     | Codified common law; blue-pencil by statute                                         | O.C.G.A. § 13-8-50 et seq. (2011)                                       |
| **Texas**       | Common law; requires ancillary enforceable agreement with independent consideration | Tex. Bus. & Com. Code § 15.50; _Light v. Centel_, 883 S.W.2d 642 (1994) |
| **Alabama**     | Statutory reform (2015) allows enforcement                                          | Ala. Code § 8-1-190 et seq.                                             |
| **Delaware**    | Common law reasonableness; courts generally enforce reasonable clauses              | Common law                                                              |
| **Connecticut** | Blue-pencil doctrine; reasonable scope analysis                                     | Common law                                                              |

**Florida CHOICE Act (2025) note:** Signed July 1, 2025. Parties may contractually agree
to enhance enforceability of non-compete provisions. Prior agreements governed by § 542.335.
[VERIFY full scope of CHOICE Act expansion]

**Moderate enforcement states (applying reasonableness strictly):**
Arizona, Arkansas, Connecticut, Georgia, Idaho, Indiana, Iowa, Kansas, Michigan,
Missouri, Montana, Nebraska, New Jersey, New Mexico, North Carolina, Ohio, Pennsylvania,
South Carolina, Tennessee, Utah, Vermont, West Virginia, Wisconsin

**Notable state-specific rules (selected):**

- **Arizona:** Moderate enforcement; blue-pencil; healthcare practitioner concerns [VERIFY]
- **Michigan:** Reasonable restrictions enforced; duration typically ≤ 2 years for most roles
- **New Jersey:** Moderate; courts scrutinise closely for adequate consideration
- **Ohio:** Reformed / purple-pencil approach; courts enforce reasonable portions
- **Pennsylvania:** Blue-pencil + reformation hybrid; requires adequate consideration for existing employees

---

## Section 8: Blue-Pencil / Red-Pencil / Reformation — State-by-State

| Doctrine                                                                               | States                                                                                                         | Practical Effect                                                   |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Mandatory Reformation** (court MUST modify)                                          | Florida (Fla. Stat. § 542.335)                                                                                 | Most employer-friendly; drafting error is judicially correctable   |
| **Reformation / Purple-Pencil** (court may rewrite)                                    | Colorado, Illinois, Massachusetts, Nevada, Ohio, Pennsylvania, Texas, Washington (and many others by case law) | Employer-friendly; drafting overreach carries some correction risk |
| **Blue-Pencil / Severance** (court strikes overbroad portions, does not rewrite)       | Arizona, Connecticut, Georgia, Indiana, Louisiana, Maryland, North Carolina, Rhode Island                      | Moderate; individual overbroad provisions can be excised           |
| **Red-Pencil / Anti-Blue-Pencil** (entire covenant void if any provision unreasonable) | Nebraska, Virginia [VERIFY], Wisconsin [VERIFY], South Carolina [VERIFY]                                       | Employee-friendly; drafting overreach voids entire covenant        |

**Drafting guidance:**

- In **red-pencil** states: Draft conservatively with no overreach — there is no judicial
  safety net. A single overbroad term voids the entire restriction.
- In **blue-pencil** states: Structure each restriction (duration, geography, activity) as
  a separately severable clause. Explicitly label each as independently severable.
- In **reformation** states: Include reformation language inviting the court to modify:
  > "If any restriction in this Section is found by a court of competent jurisdiction to
  > exceed the scope permissible under applicable law, the parties request that the court
  > modify such restriction to the maximum extent permissible under applicable law and
  > enforce it as so modified."

---

## Section 9: Garden Leave Mechanics

**Definition:** Garden leave (also called "gardening leave") means the employee is placed on
paid leave during the restricted period — they remain technically employed, on full (or
partial) salary, but do not perform work. The clock on the restriction runs from the date
garden leave begins (not from termination of payroll).

### US Garden Leave Requirements

| State             | Requirement                                                       | Amount                                            | Notes                                                                             |
| ----------------- | ----------------------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Colorado**      | Required for new/amended agreements above threshold               | "Garden leave or equivalent consideration"        | Statutory alternative: equivalent monetary compensation during restriction period |
| **Illinois**      | Garden leave OR adequate consideration                            | "At least equivalent to 14 calendar days" if used | Alternative: other adequate consideration plus 14-day advance notice              |
| **Massachusetts** | Garden leave OR mutual consideration                              | ≥ 50% of base salary for the duration             | Employer may elect to waive garden leave (and the restriction falls away)         |
| **Oregon**        | Garden leave or base salary equivalent                            | Base salary equivalent for restriction period     | Must be stated in the agreement                                                   |
| **Washington**    | Garden leave or equivalent; SB 5935 extends to laid-off employees | Equivalent base salary                            | Laid-off employees cannot be subject to non-compete without garden leave          |

**US states without explicit garden leave requirement:** Majority of US states. In these states,
post-employment non-competes are unpaid unless the parties contractually agree otherwise.

### International Garden Leave (Reference)

| Jurisdiction  | Standard Practice                          | Legal Requirement                                                                        |
| ------------- | ------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **UK**        | Full base salary during restriction period | Required for enforceability (reasonableness standard)                                    |
| **Germany**   | Karenzentschädigung (indemnification)      | **Mandatory** — at least 50% of last total remuneration; without payment, clause is void |
| **France**    | Compensation during restriction            | Required — typically 30–60% of gross salary; varies by collective bargaining agreement   |
| **Australia** | Not required by statute                    | Common law only; no statutory requirement                                                |

**Strategic note:** Offering garden leave can significantly strengthen enforceability in
jurisdictions that require or favour it. It also signals good faith that the employer is
actually willing to pay for the restriction, which some courts weight as evidence of
genuine legitimate interest.

---

## Section 10: Industry-Specific Exemptions

### 10.1 Physicians and Healthcare Practitioners

Healthcare professionals receive elevated scrutiny in many states due to public policy
concerns about access to medical care:

- **California, Minnesota, North Dakota, Oklahoma, Wyoming:** Ban applies equally to physicians
- **Pennsylvania:** Non-competes for healthcare practitioners capped at 1 year (Act 74, 2024);
  void if employer terminates the practitioner for any reason
- **Indiana:** Hospital-employed physicians — extended restrictions (2025, HEA 1289)
- **Texas:** Physician non-competes must allow: (a) patient access to medical records;
  (b) patient notification of physician's new location; (c) physician buyout right at
  reasonable price (Tex. Bus. & Com. Code § 15.50(b))
- **Colorado:** Physician non-competes must allow patient notification and records access
- **17+ other states** have varying physician-specific limitations [VERIFY current state]

**AMA position:** The American Medical Association Code of Medical Ethics discourages
physician non-competes that restrict access to patient care.

### 10.2 Broadcasters / Media Professionals

- Some states specifically limit non-compete enforcement for broadcasting employees
- **California:** Void for all employees including broadcasters (§ 16600)
- FCC has historically not regulated employment non-competes in broadcasting; state law governs
- Broadcasters may argue First Amendment free speech concerns in extreme cases [VERIFY]

### 10.3 Technology Workers

- No federal or state statute specifically exempts technology workers as a class
- **California:** Void for all tech workers (§ 16600)
- **Minnesota:** Void for all workers post-July 2023
- Practical note: Courts in tech-hub states (California, Washington, Massachusetts) apply
  reasonableness standards more strictly for software engineers and technical professionals
  where the competitive landscape is large and knowledge quickly becomes industry-standard

### 10.4 Sale-of-Business Context

Sale-of-business non-competes (protecting a business purchaser from the seller competing)
are treated **much more favourably** than employment non-competes in virtually all states:

- California §§ 16601–16602.5: Sale-of-business non-competes explicitly permitted (vs. employment NCs, which are void)
- Most ban states include a sale-of-business carve-out
- Duration and scope may be longer than employment non-competes (3–5 years is common)
- **Caution:** Do not apply ban-state analysis to sale-of-business covenants without checking
  the specific state statute's exemption scope

---

## Section 11: Choice-of-Law and Forum Selection

### 11.1 Choice-of-Law Enforceability

**General rule:** The work-location state's mandatory protective law overrides a contractual
choice-of-law clause in virtually all ban states and many restricted states.

| Scenario                                                               | Analysis                                                                 |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Agreement says "Texas law governs" but employee works in California    | California law applies; non-compete is void under § 16600                |
| Agreement says "New York law governs" but employee works in Colorado   | Colorado income threshold and garden leave requirements apply            |
| Agreement says "Florida law governs" and employee works in Florida     | Florida § 542.335 applies (employer-friendly)                            |
| Agreement says "Delaware law governs" but employee works in Washington | Washington RCW 49.62 applies; income threshold and garden leave required |
| Agreement is silent on governing law; employee works in Texas          | Texas common law applies                                                 |

**Why this matters:** Employers may include a choice-of-law clause for an employer-friendly
state (Texas, Florida) while employing workers in ban or restricted states. Those clauses are
generally ineffective for the non-compete covenant — the work-location state's employment
law protections cannot be waived by contract.

**California SB 699 (2024) extraterritorial reach:** California employees cannot be subject
to non-competes even if: (a) the agreement was signed outside California; (b) the choice
of law is non-California; (c) the employee worked outside California when the agreement was
signed. If the employee works in California at the time of alleged enforcement, the clause
is void.

### 11.2 Forum Selection Clause Interaction

**Risk:** An employer may try to enforce a non-compete in a forum-selection state (e.g., Texas)
against a California employee, hoping to obtain an injunction before the employee can contest.

**Employee protection:** Courts increasingly refuse to enforce forum-selection clauses that
would deprive employees of their home-state statutory protections. California courts will
not enforce forum-selection clauses that circumvent § 16600 protections.

**⟁ CLARIFY** — If the agreement contains a forum-selection clause that differs from the
employee's work location, flag this for the user: "This agreement selects [State X] courts
but the employee works in [State Y]. This creates a race-to-courthouse risk — employees in
[State Y] should understand their state-law defences and consult local counsel immediately
if the employer attempts enforcement."

### 11.3 Multi-State Employees (Remote Work)

**Remote employee scenario:** Employee signed a Texas-law agreement from Texas but now
works remotely from California.

- Majority view: Work-location law governs (California law applies after move)
- Employer risk: Prior agreement may become unenforceable as to a remote-California employee
  without any modification
- **Best practice:** Review non-compete portfolio when employees relocate to new states.
  Update agreements to reflect new work location and ensure compliance with the new state's law.

---

## Section 12: FTC Non-Compete Rule Status

### 12.1 Timeline

| Date              | Event                                                                                                                                               |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| June 2023         | FTC proposes rulemaking to ban all employment non-competes                                                                                          |
| April 23, 2024    | FTC issues Final Rule (16 CFR Part 910) — would have banned virtually all employment non-competes                                                   |
| August 20, 2024   | Northern District of Texas vacates the Final Rule in _Ryan, LLC v. FTC_, No. 3:24-CV-00986 (N.D. Tex.) — rule never took effect                     |
| September 4, 2025 | FTC charges Gateway Services Inc. under Section 5 of the FTC Act for requiring 12-month post-employment non-competes (1,900+ employees affected)    |
| September 5, 2025 | FTC votes 3-1 to dismiss its appeals in _Ryan, LLC_ and _Properties of the Villages v. FTC_ — rulemaking approach abandoned                         |
| September 2025    | FTC establishes Joint Labor Task Force (chairman Ferguson) to pursue case-by-case enforcement on non-competes, no-poach agreements, and wage-fixing |

### 12.2 Current Federal Landscape

**The FTC Non-Compete Rule is dead.** State law governs entirely. Do not cite 16 CFR Part 910
as operative law — it was vacated before it took effect.

**FTC Section 5 enforcement is live.** The FTC has pivoted to case-by-case enforcement of
non-competes as "unfair methods of competition" under FTC Act § 5. The _Gateway Services_
action (September 2025) signals:

- Non-competes applied broadly to non-executive, lower-income workers draw FTC scrutiny
- Industries with concentrated enforcement risk: gig economy, home services, healthcare staffing
- Employers with large non-compete portfolios should conduct proactive risk assessments

**Joint Labor Task Force:** Created February 2025 by Chairman Ferguson. Coordinates FTC
enforcement on: (a) non-competes; (b) no-poach agreements; (c) wage-fixing by employers.
Employment-law practitioners should monitor enforcement actions and consent orders.

### 12.3 Implications for Practice

- **Drafting:** Do not rely on a future federal rule to save an overbroad state-law violation
- **Portfolio audits:** Review existing non-compete agreements for state-law compliance; FTC
  scrutiny adds reputational and enforcement risk to overbroad portfolios
- **Low-wage workers:** Particular risk target — both state statutory bans and FTC attention
  focus on non-competes applied to lower-income employees

---

## Section 13: DTSA / UTSA Trade Secret Overlay

### 13.1 Relationship Between Non-Compete and Trade Secret Law

Non-compete covenants and trade secret law protect the employer from competitive harm via
**different mechanisms** and operate independently:

|                               | Non-Compete                                | Trade Secret Law                                         |
| ----------------------------- | ------------------------------------------ | -------------------------------------------------------- |
| **Nature**                    | Contractual covenant (future-oriented)     | Statutory / common law remedy (remedial)                 |
| **Source**                    | Employment agreement                       | Federal DTSA (18 U.S.C. § 1836); State UTSA              |
| **What it protects**          | Employer from competition generally        | Employer's specifically identifiable trade secrets       |
| **Employee liability**        | For accepting employment with a competitor | For misappropriating (using or disclosing) trade secrets |
| **Continues despite void NC** | N/A — covenant is void                     | Yes — DTSA/UTSA applies even if NC is void               |

### 13.2 Strategic Interaction

**In ban states (CA, MN, ND, OK, WY):** The non-compete is void, but trade secret law is
fully applicable. Employers cannot prevent competition, but can prevent misappropriation.

**Practical strategy in ban states:**

1. Rely on DTSA / California CUTSA (Cal. Civ. Code § 3426 et seq.) for trade secret protection
2. Ensure employment agreements include robust NDAs and DTSA whistleblower notice
3. Implement information-access controls (need-to-know basis; audit logs)
4. Use customer relationship management systems to document that customer lists are maintained
   as trade secrets (not available from public sources)
5. Consider narrowly tailored non-solicitation of customers (different legal test in some states)

**California note:** California courts apply CUTSA broadly. Non-solicitation of specific
customers may also be challengeable post-_AMN Healthcare Services, Inc. v. Aya Healthcare
Services, Inc._, 28 Cal. App. 5th 923 (2018). [VERIFY current treatment]

### 13.3 DTSA Whistleblower Immunity Notice Requirement (18 U.S.C. § 1836(b)(3)(C))

Every employment agreement or NDA entered into after May 11, 2016, must include the
whistleblower immunity notice OR cross-reference the employer's whistleblower policy.
**Failure to include it results in forfeiture of:**

- Exemplary damages (up to 2× actual damages)
- Attorney fees in any subsequent DTSA trade secret action

**The notice is separate from and independent of the non-compete clause.** Even in ban
states where the non-compete is void, the DTSA notice remains necessary for the employer
to preserve DTSA remedies.

**Model DTSA notice language:**

> "Pursuant to 18 U.S.C. § 1836(b)(3)(C), Employee will not be held criminally or civilly
> liable under any Federal or State trade secret law for the disclosure of a trade secret
> that (A) is made in confidence to a Federal, State, or local government official, either
> directly or indirectly, or to an attorney; and solely for the purpose of reporting or
> investigating a suspected violation of law; or (B) is made in a complaint or other
> document filed in a lawsuit or other proceeding, if such filing is made under seal."

---

## Section 14: Enforceability Risk Matrix Output

After completing Steps 2–9, generate a consolidated **Enforceability Risk Matrix** for the
reviewed clause(s):

```
NON-COMPETE ENFORCEABILITY RISK MATRIX
Generated: [date]

CLAUSE SUMMARY
  Duration: [X months]
  Geographic scope: [description]
  Activity scope: [description]
  Consideration: [description]
  Garden leave: [yes/no/amount]

JURISDICTION ANALYSIS
  Work location: [State]
  Choice of law: [State if different]
  Override applicable: [yes/no — reason]

ENFORCEABILITY GATES
  Ban state: [Yes — VOID / No — continue]
  Income threshold: [Met / Failed — void / Not applicable]
  Advance notice: [Compliant / Non-compliant / Not required]
  Garden leave: [Compliant / Non-compliant / Not required]

THREE-PRONG ANALYSIS (if applicable)
  Protectable interest: [Identified / Absent / Weak]
  Reasonableness of scope: [GREEN / YELLOW / RED — details]
  Public policy: [No issue / Flag — details]

CONSIDERATION ADEQUACY
  Timing: [New hire / Mid-employment / Separation]
  Consideration type: [Describe]
  Adequacy: [Adequate / Insufficient — reason]

BLUE-PENCIL DOCTRINE
  Work-location doctrine: [Reformation / Blue-pencil / Red-pencil]
  Overbreadth detected: [Yes — specify / No]
  Likely court treatment: [Would modify to [X] / Would void entirely]

ENFORCEABILITY CLASSIFICATION
  Overall: [🟢 GREEN / 🟡 YELLOW / 🔴 RED / ⛔ BAN STATE]
  Confidence score: [0.0–1.0]
  Rationale: [1–2 sentence explanation]

RECOMMENDED MODIFICATIONS
  1. [Redline 1 — describe change and reason]
  2. [Redline 2 — if applicable]
  3. [Redline 3 — if applicable]

DTSA NOTICE
  Present: [Yes / No — recommend adding immediately]
```

---

## Section 15: Prioritisation Framework

When multiple weaknesses are identified, prioritise remediation in this order:

**Tier 1 — Must Fix (Agreement May Be Void):**

- [ ] Ban state violation (void by operation of law)
- [ ] Income threshold failure (void if below threshold)
- [ ] Advance notice deficiency (voids agreement in MA, CO, IL, WA)
- [ ] Garden leave payment missing in required jurisdiction
- [ ] Missing DTSA whistleblower immunity notice (forfeits exemplary damages + fees)

**Tier 2 — Should Fix (High Litigation Risk):**

- [ ] Consideration deficiency for mid-employment agreement
- [ ] Duration overbreadth (> 18–24 months in most jurisdictions)
- [ ] Nationwide geographic scope for non-national role
- [ ] Activity scope covering all competition regardless of role
- [ ] Red-pencil state — any overbreadth provision

**Tier 3 — Recommended (Strengthens Enforceability):**

- [ ] No explicit legitimate protectable interest stated
- [ ] No severability / blue-pencil clause in reformation or blue-pencil state
- [ ] Forum selection clause misaligned with employee work location
- [ ] Absence of garden leave even in non-required states (strengthens enforceability)
- [ ] Choice-of-law clause selecting non-work-location state

---

## Section 16: Citation Quality Gates

Run these five gates before delivering any enforceability analysis. If any gate fails,
revise or mark before delivering.

| Gate           | Rule                                                                                                                  | Fail Action                                                                       |
| -------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Source**     | Every enforceability determination cites a specific statute (with section number) or case (with citation and holding) | Add citation or mark "[VERIFY]" and flag for counsel confirmation                 |
| **Format**     | US statutes cited as "State. Code Ann. § [section]"; US cases as "_Name_, [Reporter] (Court Year)"                    | Standardise format                                                                |
| **Currency**   | Every statute verified for 2023–2025 amendments; salary thresholds flagged as "[VERIFY current year figure]"          | Flag "[VERIFY CURRENCY — threshold adjusts annually]" for income threshold states |
| **Domain**     | Analysis applies only the work-location jurisdiction's law unless explicitly analysing choice-of-law override         | Remove jurisdictional bleed; clearly label which state's law is being applied     |
| **Confidence** | Every enforceability determination includes explicit confidence score (0.0–1.0)                                       | Add confidence level before delivering                                            |

---

## Section 17: Self-Interrogation for RED Classifications

For any non-compete clause classified as RED, apply this three-pass review before confirming:

**Pass 1 — Statutory Clarity:** Is the RED classification grounded in clear statute (e.g., ban-state
prohibition, income threshold failure) or in common-law reasonableness analysis? If based on
reasonableness, is the assessment well-grounded in case law from the specific jurisdiction?
Would blue-pencil or reformation doctrine result in partial enforcement despite the overreach?

**Pass 2 — Completeness:** Have all relevant state statutes, recent legislative changes
(2023–2025 are high-activity years), and regulatory guidance been considered? Is there any
recent appellate decision in the jurisdiction that might change the analysis? Would the
classification differ if the employee's position level, compensation, or access to trade secrets
were different?

**Pass 3 — Realistic Enforcement:** What is the employer's strongest argument for enforcing
the clause as written? Under what fact pattern might a court in this jurisdiction enforce
the clause? What is the realistic litigation cost and burden — many employers choose not
to litigate non-competes even when the clause may be technically enforceable?

**Revise RED to YELLOW** if any pass reveals: (a) the overreach could be cured by
blue-pencil severance; (b) the statutory analysis is uncertain; (c) a reasonable court
in this jurisdiction might enforce the clause. **Retain RED** if all three passes confirm
the clause is void or enforcement would likely fail. Document the self-interrogation result
in the Glass Box.

---

## Section 18: Confidence Scoring

For each enforceability assessment, assign a confidence level:

| Level        | Range     | Meaning                                                                                | Action                                                             |
| ------------ | --------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Definite** | 0.95–1.0  | Clear statute; settled law; no jurisdictional ambiguity (e.g., California § 16600 ban) | State with full confidence; no caveat required                     |
| **High**     | 0.80–0.94 | Strong statutory or case law authority; minor application questions                    | State with brief caveat noting remaining questions                 |
| **Probable** | 0.60–0.79 | Good arguments; outcome could differ depending on specific facts                       | State with explicit reasoning and contra-indicators                |
| **Possible** | 0.40–0.59 | Genuinely uncertain; case law is mixed or evolving                                     | Flag for professional review; present both sides                   |
| **Unlikely** | 0.0–0.39  | Weak enforceability basis; strong factors militate against enforcement                 | Do not assert enforceability; mark "[QUESTIONABLE ENFORCEABILITY]" |

**Critical caveat:** Non-compete enforceability is inherently fact-specific and varies
dramatically within jurisdictions. Courts apply multi-factor reasonableness tests with
unpredictable outcomes. **No analysis should exceed High (0.80–0.94) confidence** for
reasonableness-based determinations (i.e., not ban-state analysis) without recent verified
case law from the specific jurisdiction and facts.

---

## Section 19: Anti-Patterns

**What NOT to do when analysing non-compete enforceability:**

1. **Citing the FTC Non-Compete Rule as operative law.** The FTC Final Rule (16 CFR Part 910)
   was vacated on August 20, 2024, before it took effect. The FTC abandoned its appeals
   September 5, 2025. Do not cite it as binding authority or active law. State law governs entirely.

2. **Treating ban states as "strongly disfavouring" non-competes.** California, Minnesota,
   North Dakota, Oklahoma, and Wyoming (July 2025) do not merely disfavour non-competes —
   they void them completely by operation of law. "Unenforceability risk" framing is incorrect;
   the correct framing is "void and unenforceable."

3. **Assuming the contractual choice-of-law clause controls enforceability.** In ban states
   and many restricted states, the work-location state's mandatory employment law overrides
   the contractual choice of law. A Texas-law clause does not make a California non-compete
   enforceable.

4. **Applying a single state's law to multi-state or remote employees without work-location
   analysis.** Remote employees who work from California are subject to California § 16600
   even if they signed agreements designating another state's law.

5. **Treating continued at-will employment as sufficient consideration in all states.** In
   Colorado, Illinois, Washington, Massachusetts, and Texas (with caveats), continued at-will
   employment is insufficient consideration for new or amended non-competes. Additional
   consideration is required.

6. **Confusing durational limits with the reasonableness test.** Duration is one prong of
   the three-prong test, not the only prong. A 6-month non-compete with nationwide scope
   and no legitimate interest may still be unenforceable despite the short duration.

7. **Assuming blue-pencil doctrine applies in every state.** Nebraska, Virginia, Wisconsin,
   and South Carolina apply the red-pencil doctrine — if any term is overbroad, the entire
   covenant is void. A single overreach can eliminate all protection.

8. **Treating garden leave as legally equivalent to a post-employment non-compete for purposes
   of enforceability analysis.** Garden leave (employee remains on payroll during restriction)
   and unpaid post-employment non-compete are legally distinct. Some states (Colorado, Illinois,
   Washington, Massachusetts) require garden leave or equivalent for the non-compete to be
   enforceable. The absence of garden leave voids the clause in those states.

9. **Treating physician non-competes identically to general employee non-competes.** Multiple
   states (Texas, Colorado, Pennsylvania, Indiana) have physician-specific rules that layer
   additional requirements or outright bans. Always check for healthcare-practitioner-specific
   statutes.

10. **Overlooking the DTSA whistleblower immunity notice requirement.** Even in ban states
    where the non-compete clause is void, the DTSA notice protects the employer's trade secret
    remedies. Failure to include it forfeits exemplary damages and attorney fees in any future
    DTSA action.

11. **Using stale salary thresholds.** Income thresholds in Colorado, Washington, Oregon,
    Illinois, DC, Virginia, Maine, Maryland, New Hampshire, and Rhode Island adjust annually.
    Thresholds from the prior year may already be out of date. Always verify current figures
    with the state's labor department or CDLE equivalent before applying them.

12. **Failing to distinguish employment non-competes from sale-of-business non-competes.**
    Ban states (California, North Dakota, Oklahoma) have explicit statutory carve-outs for
    sale-of-business non-competes. A California employer selling a business can include a
    non-compete on the selling business owner — the § 16600 ban does not apply.

13. **Assuming a non-compete that survived a prior lawsuit is still enforceable.** Non-compete
    law changes rapidly; a clause that was reasonable and enforced in 2020 may not be
    enforceable under 2024 or 2025 statutory amendments.

14. **Ignoring non-compete implications in M&A.** Acquisition targets' employee non-compete
    portfolios carry compliance risk that affects deal value. Minnesota's retroactive void
    (for post-July 1, 2023 agreements) and California SB 699's extraterritorial reach can
    affect acquired employees immediately.

15. **Relying solely on the employer's choice of forum to avoid ban-state law.** Courts in
    California, Minnesota, and other ban states will enjoin enforcement in a foreign forum
    that would deprive employees of their home-state statutory protections.

16. **Over-stating enforceability confidence in reasonableness-based analysis.** Courts apply
    highly fact-specific tests. Even in employer-friendly states, an overbroad clause may
    fail on its specific facts. Never assert "Definite" or "High" confidence for
    reasonableness-based determinations without verified recent jurisdiction-specific case law.

17. **Failing to address FTC Section 5 enforcement exposure separately from state law.**
    Even where state law permits a non-compete, the FTC's new case-by-case Section 5 enforcement
    posture (Gateway Services, September 2025) creates additional exposure for employers with
    broad non-compete portfolios applied to lower-income workers.

18. **Missing the California AB 1076 (2024) notification obligation.** California employers
    are obligated to notify employees with void non-competes that the clauses cannot be
    enforced. Failure to notify is a civil violation under AB 1076. This is a proactive
    obligation — employers do not wait for the employee to ask.

19. **Treating non-solicitation clauses identically to non-competes for enforceability
    purposes.** Many states with income thresholds for non-competes have separate, lower
    thresholds for non-solicitation of customers or employees. Some ban states (California)
    also void non-solicitation of specific customers post-_AMN Healthcare_ [VERIFY current
    California treatment]. Analyse separately.

20. **Using non-compete analysis as a substitute for litigation strategy advice.** This skill
    produces an enforceability assessment; it does not provide litigation strategy, injunction
    risk analysis, or advice on whether to enforce. A clause may be technically enforceable
    but not worth litigating for cost/reputational reasons.

---

## Section 20: Writing Standards

Before delivering any output, apply these writing quality gates:

1. **Clarity**: Every finding is stated in a single clear sentence before explanation.
   Avoid legal jargon without definition.

2. **Specificity**: Name the specific statute, case, or principle. Do not write "applicable
   law requires" — write "Colorado CRS § 8-2-113 requires..."

3. **[VERIFY] markers**: Every citation whose currency or accuracy is uncertain carries
   a "[VERIFY]" marker with a note on what to verify and against which source.

4. **Confidence attribution**: Every enforceability determination carries its confidence
   score inline — "HIGH (0.85)" or "PROBABLE (0.70)" — so the user can calibrate reliance.

5. **Dual-framing where appropriate**: For clients representing employers, frame findings
   as enforceability risks and remediation opportunities. For clients representing employees,
   frame the same findings as defences and voidability arguments.

6. **Hedged where legally appropriate**: Reasonableness-based determinations are hedged;
   ban-state determinations are stated with confidence (no hedging needed — the law is clear).

7. **No gratuitous legalese**: Do not use Latin phrases, defined terms without definition,
   or unexplained acronyms. If a term must be defined, define it on first use.

---

## Section 21: External Tool Integration

### With legalcode-mcp connected (preferred):

At Step 3 (Extract Terms) and Step 5 (Three-Prong Test), search for:

- Current state statute text for the work-location state
- Recent case law (2022–2026) on non-compete enforceability in the specific jurisdiction
- Recent legislative changes affecting the relevant state
- Any current state attorney general guidance on non-compete enforcement

Save the most relevant results to `/tmp/legalcode-non-compete-research-[state].md`.
Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box.

### Without legalcode-mcp:

Proceed with the matrix and frameworks in this skill. Mark all statutory citations and
case law references with [VERIFY] — especially income thresholds (adjust annually) and
any 2023–2025 legislative changes. Note in the Glass Box:
`legalcode_mcp: "Not connected — all citations require independent verification"`

---

## Section 22: Glass Box Audit Trail

Every non-compete enforceability output MUST include a Glass Box section for traceability
and auditability:

```yaml
glass_box:
  skill_name: "legalcode-non-compete-enforceability"
  analysis_date: "[ISO date]"
  employee_work_location: "[State — the governing jurisdiction]"
  governing_law_clause: "[State if stated in agreement / Silent / Ambiguous]"
  jurisdiction_override_applied: "[yes — work location overrides choice of law / no / N/A]"
  ban_state: "[yes — clause void / no]"
  ban_state_name: "[State if applicable / N/A]"
  income_threshold_applicable: "[yes / no]"
  income_threshold_met: "[yes / no / not applicable]"
  income_threshold_verified: "[yes — current year figure confirmed / no — mark VERIFY]"
  agreement_timing: "[new hire / mid-employment / separation]"
  consideration_adequate: "[yes / no / unclear]"
  consideration_type: "[employment offer / additional consideration — describe / unclear]"
  garden_leave_required: "[yes / no / state does not require]"
  garden_leave_compliant: "[yes / no / not required]"
  duration_extracted: "[X months / years]"
  geographic_scope_extracted: "[description]"
  activity_scope_extracted: "[description]"
  three_prong_applied: "[yes / no (ban state or threshold failure)]"
  prong_1_interest: "[identified / absent / weak]"
  prong_2_scope: "[reasonable / overbroad — specify dimension]"
  prong_3_public_policy: "[no concern / flag — describe]"
  blue_pencil_doctrine: "[reformation / blue-pencil / red-pencil — state name]"
  overbreadth_detected: "[yes — describe / no]"
  dtsa_notice_present: "[yes / no — recommend adding immediately]"
  industry_exemption_checked: "[yes — result / no — not applicable]"
  choice_of_law_conflict: "[yes — describe / no]"
  classification: "[GREEN / YELLOW / RED / BAN STATE]"
  confidence_score: "[0.0–1.0]"
  confidence_level: "[Definite / High / Probable / Possible / Unlikely]"
  self_interrogation_applied: "[yes — passed / yes — revised to YELLOW / not applicable]"
  ftc_rule_note: "N/A — FTC Non-Compete Rule vacated Aug 20 2024; FTC abandoned appeal Sept 5 2025; Section 5 case-by-case enforcement active"
  legalcode_mcp: "[Connected — citations verified / Not connected — citations marked VERIFY]"
  redlines_generated: "[yes — N redlines / no]"
  limitations:
    - "Enforceability is fact-specific; courts apply multi-factor tests with jurisdiction variation"
    - "Income thresholds adjust annually; verify current figures before acting"
    - "Non-compete law changed rapidly in 2023–2025; verify recent amendments for work-location state"
    - "[Additional scope limitations or assumptions specific to this analysis]"
  reviewer: "AI-assisted — requires review by qualified employment attorney licensed in [work-location state]"
```

---

## Section 23: Output Format Template

Every non-compete enforceability analysis delivers this structured output:

```markdown
# Non-Compete Enforceability Analysis

**Date:** [ISO date]
**Employee work location:** [State]
**Governing law (contractual):** [State if stated]

---

## ⟁ Initial Screening

| Check            | Result                                                                        |
| ---------------- | ----------------------------------------------------------------------------- |
| Ban state        | [✅ Not a ban state / ⛔ BAN — clause void]                                   |
| Income threshold | [✅ Met ($X > threshold $Y) / ⛔ Failed ($X < threshold $Y) / Not applicable] |
| Advance notice   | [✅ Compliant / ⚠️ Non-compliant / Not required]                              |
| Garden leave     | [✅ Compliant / ⚠️ Non-compliant / Not required]                              |
| DTSA notice      | [✅ Present / ⚠️ Missing — recommend adding]                                  |

---

## Three-Prong Reasonableness Analysis

### Prong 1 — Legitimate Protectable Interest

**Finding:** [GREEN / YELLOW / RED]
[Specific finding — what interest was identified, whether it is legally cognisable in this state]
**Confidence:** [HIGH / PROBABLE / POSSIBLE] ([score])

### Prong 2 — Reasonableness of Scope

**Duration:** [GREEN / YELLOW / RED] — [X months; reasoning]
**Geographic scope:** [GREEN / YELLOW / RED] — [scope; reasoning]
**Activity scope:** [GREEN / YELLOW / RED] — [scope; reasoning]
**Confidence:** [HIGH / PROBABLE / POSSIBLE] ([score])

### Prong 3 — Public Policy

**Finding:** [No issue / Flag — healthcare access / Flag — anticompetitive]
**Confidence:** [score]

---

## Consideration Analysis

**Timing:** [New hire / Mid-employment / Separation]
**Consideration identified:** [Description]
**Adequacy:** [✅ Adequate / ⚠️ Insufficient — reason]

---

## Judicial Modification Analysis

**Applicable doctrine in [State]:** [Reformation / Blue-pencil / Red-pencil]
**Overbreadth detected:** [Yes — [detail] / No]
**Likely court treatment if challenged:** [Would modify to [X] / Would void entirely / Likely enforce]

---

## Overall Classification

> **[🟢 GREEN / 🟡 YELLOW / 🔴 RED / ⛔ BAN STATE]**
> **Confidence score:** [0.0–1.0] — [one-sentence rationale]

---

## Recommended Modifications

### Tier 1 — Must Fix

[List must-fix items with specific redlines]

### Tier 2 — Should Fix

[List high-priority redlines]

### Tier 3 — Recommended

[List strengthening modifications]

---

## DTSA / Trade Secret Overlay

[If ban state or RED: explain how DTSA/UTSA still protects employer]
[If GREEN: confirm DTSA notice is present or recommend adding]

---

[Glass Box audit trail — YAML block per Section 22]
```

---

## Provenance

Created by Legalcode, 2026-03-02. Original synthesis from scratch via 2-agent research
pipeline (Structural Analyst + Legal Research Agent). Structural patterns derived from
`legalcode-contract-review` and `legalcode-employment-agreement-review` reference standards.
Legal content researched via web search across FTC.gov, Duane Morris, National Law Review,
CDLE (Colorado), state labor department publications, and law firm client alerts covering
2023–2025 legislative developments. Key authorities verified: _Ryan, LLC v. FTC_ (N.D. Tex.
Aug. 20, 2024); Cal. Bus. & Prof. Code §§ 16600-16600.5 + SB 699 (2024); Minn. Stat. §
181.988 (eff. July 1, 2023); Wyoming Senate File 107 (eff. July 1, 2025); Florida CHOICE
Act (eff. July 1, 2025); Pennsylvania Act 74 of 2024 (eff. Jan. 1, 2025). All statutory
citations carry [VERIFY] unless confirmed by primary source research.
