---
name: legalcode-engagement-letter-drafter
description: 'Generate attorney/solicitor engagement letters from intake data. Use when drafting, reviewing,
  or auditing an engagement letter for a new or existing client matter. Covers all required elements:
  scope of representation, fee structures (hourly, flat fee, contingency, retainer, hybrid), billing practices,
  expense reimbursement, client responsibilities, conflict of interest disclosures, advance conflict waivers,
  confidentiality and attorney-client privilege, termination rights, file retention, ethics disclosures,
  and no-guarantee-of-outcome language. Aligned with ABA Model Rules 1.5, 1.6, 1.8, and 1.16; SRA Code
  of Conduct and Transparency Rules; New York 22 NYCRR Part 1215; California Business and Professions
  Code § 6148; and general bar requirements across US and UK jurisdictions. Produces jurisdiction-adapted,
  practice-area-specific engagement letters ready for attorney review. Also use for: client care letters,
  retainer agreements, letters of engagement, representation agreements, engagement audits.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Engagement Letter Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted drafting of attorney/solicitor
> engagement letters. It does not constitute legal advice or professional responsibility
> guidance. All outputs must be reviewed by a qualified attorney or solicitor licensed in
> the relevant jurisdiction before sending to a client. Professional responsibility rules,
> bar regulations, and statutory requirements change; verify current applicability before
> relying on any provision described here. Statutory and regulatory references cited from
> memory carry hallucination risk — verify against authoritative sources before relying on
> them.

## Purpose and Scope

This skill generates professional, jurisdiction-compliant engagement letters from client
intake data. It structures each section to meet applicable professional responsibility
requirements, selects the appropriate fee structure and billing framework, and produces
a complete letter ready for attorney review.

**Covers:**

- Engagement letter drafting from intake data (all practice areas and matter types)
- Engagement letter review and gap analysis (finding missing required elements)
- Fee structure selection and description (hourly, flat fee, contingency, retainer, hybrid)
- Billing practices and expense reimbursement terms
- Scope of representation and exclusions
- Conflict of interest disclosures and advance conflict waivers
- Confidentiality, attorney-client privilege, and work product disclosures
- Termination provisions (client's right to discharge; attorney's right to withdraw)
- File retention and post-engagement policies
- Ethics disclosures and no-guarantee-of-outcome language
- Practice-area-specific customizations (litigation, transactional, advisory)

**Does not:**

- Provide legal advice to clients
- Perform independent conflict checks (see `legalcode-conflict-check`)
- Execute KYC/AML due diligence (see `legalcode-client-intake-workflow`)
- Guarantee compliance with any specific jurisdiction's requirements without attorney review
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers

**Related skills:**

- `legalcode-client-intake-workflow` — full intake process including conflict check and KYC
- `legalcode-conflict-check` — deep-dive conflict screening
- `legalcode-outside-counsel-guidelines` — outside counsel billing and performance requirements

---

## Jurisdiction and Governing Law

This skill supports US and UK engagement letter requirements as primary reference frameworks,
with jurisdiction-agnostic structure adaptable to any common law jurisdiction.

**US Primary References** [VERIFY]:

- ABA Model Rule 1.5 — Fees: reasonable fees, written fee agreements, contingency fee requirements
- ABA Model Rule 1.5(e) — Fee division with other lawyers: written client consent required
- ABA Model Rule 1.6 — Confidentiality: scope of the duty; exceptions
- ABA Model Rule 1.8 — Business transactions with clients: written disclosure and consent
- ABA Model Rule 1.16 — Declining or terminating representation: mandatory and permissive withdrawal
- 22 NYCRR Part 1215 — New York mandatory engagement letter requirements (since March 4, 2002)
- NY Part 137 — Fee dispute resolution (arbitration notice required in NY)
- California Business and Professions Code § 6148 — Written fee agreements when total fees
  reasonably expected to exceed $1,000
- California Rules of Professional Conduct Rule 1.5 — Reasonable fees factors

**UK Primary References** [VERIFY]:

- SRA Code of Conduct for Solicitors — information disclosure obligations (paras. 8.6–8.9)
- SRA Transparency Rules — mandatory cost disclosure and complaints information at engagement
- Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013
  — applicable to consumer clients
- Legal Ombudsman Scheme Rules — right to complain; statutory time limits

[JURISDICTION-SPECIFIC] When localizing beyond US/UK, research and apply:

- Mandatory written agreement requirements (threshold amounts, matter types)
- Fee disclosure standards (level of detail required, timing)
- Contingency fee restrictions (many jurisdictions restrict or prohibit)
- Complaints and dispute resolution requirements
- File retention minimums under applicable ethics rules or statute
- Language requirements for client-facing documents
- Notarization requirements (some civil law jurisdictions require notarized retainer agreements)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the firm's practices, the applicable jurisdiction, or the client's situation, the workflow
pauses and asks when:

- The answer changes which provisions are legally required
- The fee structure choice materially affects multiple sections of the letter
- Practice-area-specific provisions are needed (litigation disclaimers, contingency rules)
- The client type (individual, entity, joint representation) affects privilege and scope

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

Accept intake data in any of these formats:

- **Intake form data**: Structured client information (name, matter type, fee agreed, etc.)
- **Verbal summary**: Free-text description of the engagement ("new client, estate planning,
  flat fee of $2,500, husband and wife joint representation")
- **Existing draft letter**: An engagement letter requiring review and gap analysis
- **Template request**: A request to build a firm-specific engagement letter template
  for a practice area

If insufficient information is provided to draft the letter, proceed to Step 2 immediately.

### Step 2: Gather Context

**⟁ CLARIFY** — Before drafting, ask for the following. Present options as a structured
list and allow free-text for detail. Skip questions already answered by the input.

1. **Jurisdiction / Bar requirements**
   - Options: US federal (ABA only), New York, California, Texas, another US state,
     England & Wales (SRA), Scotland, another jurisdiction, Unknown / general
   - _Why this matters_: Determines which mandatory provisions apply (NY Part 1215,
     CA § 6148, SRA Transparency Rules, etc.).

2. **Client type**
   - Options: Individual, Married couple / domestic partners, Business entity (corporation,
     LLC, partnership), Government entity, Nonprofit, Other
   - _Why this matters_: Entity representation requires identifying the specific legal
     entity and clarifying that officers/owners are not individually represented. Joint
     individual representations require separate disclosure of privilege implications.

3. **Practice area / matter type**
   - Options: Litigation (civil), Litigation (criminal), Transactional / corporate,
     Real estate, Estate planning / probate, Family / domestic relations, Immigration,
     Employment, Tax, Regulatory / compliance, General / ongoing counsel, Other
   - _Why this matters_: Determines required outcome disclaimers, fee structure options,
     practice-specific provisions, and applicable bar rules.

4. **Fee structure**
   - Options: Hourly billing, Flat fee, Contingency (percentage of recovery),
     Hybrid (flat + hourly / contingency + hourly), Retainer (advance fee, evergreen,
     or value-based), Not yet determined
   - _Why this matters_: The fee structure drives multiple sections of the letter
     (fee description, billing practices, expense responsibility, withdrawal consequences).

5. **Fee details** (follow-up after fee structure is chosen)
   - For hourly: billing rates per timekeeper, billing increments (1/10th or 1/6th hour),
     estimated range if available
   - For flat fee: amount, what is included, what triggers additional fees
   - For contingency: percentage (pre-trial vs. trial/appeal), expense responsibility
   - For retainer: initial amount, replenishment threshold (evergreen) or monthly scope
   - _Why this matters_: ABA Rule 1.5(b) and state rules require the basis of the fee
     to be communicated in writing.

6. **Retainer / advance fee** (if applicable)
   - Amount, whether placed in trust (IOLTA), when earned
   - _Why this matters_: Trust accounting rules govern advance fee handling. Labeling
     advance fees "non-refundable" is prohibited in many jurisdictions.

7. **Scope of representation**
   - What specific services are included in this engagement
   - What is explicitly excluded (appeals, ancillary matters, other practice areas)
   - _Why this matters_: Scope is the highest-risk element of any engagement letter.
     Vague scope is the leading cause of attorney malpractice claims.

8. **Conflict of interest status**
   - Options: Conflicts cleared (no conflicts), Conflict identified / waiver required,
     Advance waiver requested (for ongoing counsel), Conflicts not yet checked
   - _Why this matters_: A conflict waiver requires specific disclosure in the letter;
     advance waivers require heightened specificity.

9. **Co-counsel or referral arrangement** (if applicable)
   - Other firm(s) involved, fee-sharing arrangement
   - _Why this matters_: Rule 1.5(e) (US) requires written client disclosure and consent
     for fee division between firms.

**⟁ CLARIFY** — If any critical information cannot be gathered (fee structure unknown,
scope not yet defined), ask whether to:

- **Draft with placeholders**: Produce the letter with [SPECIFY: fee amount] and
  [SPECIFY: scope] markers for attorney completion
- **Wait for full intake**: Pause and return when the information is available
- **Draft a template**: Produce a practice-area template with all required provisions
  marked optional or required, for the attorney to populate

### Step 3: Identify Mandatory Disclosure Requirements

Identify which provisions are **legally required** vs. **recommended** based on the
jurisdiction and matter type established in Step 2.

**⟁ CLARIFY** — If the jurisdiction is unclear, ask the user to confirm before proceeding.
Mandatory requirements vary significantly by state:

- New York: written engagement letter required when fees will exceed $3,000 [VERIFY]
- California: written fee agreement required when fees will reasonably exceed $1,000 [VERIFY]
- Contingency fees: must be in writing in all US jurisdictions under ABA Rule 1.5(c) [VERIFY]
- England & Wales: client care letter required for all private client matters [VERIFY]

For the identified jurisdiction, flag:

| Provision                   | US (General)                    | New York                     | California                 | England & Wales              |
| --------------------------- | ------------------------------- | ---------------------------- | -------------------------- | ---------------------------- |
| Written agreement threshold | No general requirement [VERIFY] | >$3,000 [VERIFY]             | >$1,000 [VERIFY]           | All private matters [VERIFY] |
| Contingency fee in writing  | Required (Rule 1.5(c))          | Required                     | Required                   | Restricted [VERIFY]          |
| Fee arbitration notice      | Recommended                     | Required (Part 137) [VERIFY] | Not required               | N/A                          |
| Complaints procedure        | Recommended                     | Recommended                  | Recommended                | Required (SRA) [VERIFY]      |
| Legal Ombudsman notice      | N/A                             | N/A                          | N/A                        | Required [VERIFY]            |
| Costs estimate              | Recommended                     | Recommended                  | Recommended                | Required (SRA) [VERIFY]      |
| Rate change notice          | Recommended                     | Required [VERIFY]            | Prohibited without consent | Recommended                  |

Mark every provision as:

- **REQUIRED** — Mandated by applicable bar rule or statute
- **REQUIRED BY PRACTICE** — Not mandated but absence creates significant malpractice risk
- **RECOMMENDED** — Best practice; omission is acceptable but inadvisable

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** (if connected) to pull current text of:

- Applicable state rules of professional conduct (fee disclosure, contingency, withdrawal)
- Applicable statutory fee agreement requirements (CA B&P § 6148, NY CPLR § 474-a)
- SRA Transparency Rules and SRA Code of Conduct (for UK matters)
- Any recent bar opinions or formal ethics opinions on engagement letter requirements

Save results to a temporary reference file:

```markdown
# Legal Authority Reference — Engagement Letter

## Jurisdiction: [identified jurisdiction]

## Date Gathered: [date]

### Applicable Rules

- [Rule, current text or summary, relevance to engagement letter]

### Statutory Requirements

- [Statute, section, threshold/requirement]

### Bar Guidance / Ethics Opinions

- [Opinion citation, summary of requirement]
```

**If legalcode-mcp is not connected:**

- Proceed with general ABA Model Rule framework and the jurisdiction identified in Step 2
- Mark all specific statutory citations with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`

### Step 5: Draft the Engagement Letter

Draft the engagement letter section by section. For each section, produce:

- The complete draft text (client-ready language)
- A brief internal note on the rule or requirement driving the provision
- Any attorney review flag for items requiring judgment (REVIEW REQUIRED)

Use the **Section-by-Section Reference** below to ensure all required elements are present.
Produce sections in this order for the final letter:

**Structure of the Engagement Letter:**

```
1. Header and Salutation
2. Matter Identification / Subject Line
3. Identity of Client and Scope of Representation
4. Fee Structure and Billing Practices
5. Advance Fees / Retainer (if applicable)
6. Expense Reimbursement
7. Client Responsibilities
8. Conflict of Interest Disclosures (if applicable)
9. Confidentiality and Attorney-Client Privilege
10. No Guarantee of Outcome
11. Termination of Representation
12. File Retention
13. Ethics Disclosures and Regulatory Notices
14. Signature Block
```

**⟁ CLARIFY** — For engagement letters involving any of the following, ask the user
before drafting those sections:

- **Conflict waiver**: If a conflict waiver is required, ask for the specific conflict
  identified, the parties affected, and whether independent counsel has been recommended.
  Advance waivers require specific facts; generic blanket waivers are unenforceable [VERIFY].
- **Joint representation**: If the firm represents multiple clients in the same matter,
  ask whether a separate joint representation disclosure is being provided, or whether it
  should be integrated into this letter.
- **Business transaction with client (ABA Rule 1.8)**: If the firm is entering any
  business transaction with the client beyond standard legal services, ask for the details.
  Rule 1.8 requires the transaction to be fair and reasonable, disclosed in writing, and
  the client must be advised to seek independent counsel.
- **Fee-sharing with another firm (ABA Rule 1.5(e))**: Confirm each firm's share and
  whether the client's consent has been confirmed in writing separately.
- **Contingency fee in domestic relations**: Contingency fees in divorce/domestic matters
  are prohibited in most US jurisdictions [VERIFY]. Confirm the matter type before drafting.

### Step 6: Ethics Compliance Review

After drafting, verify the letter against the applicable bar requirements.

**Check each provision against the applicable rules:**

| Provision                   | Check                                                                             | Status            |
| --------------------------- | --------------------------------------------------------------------------------- | ----------------- |
| Fee description             | Is the basis of the fee communicated per Rule 1.5(b)?                             | PASS / FAIL       |
| Contingency fee             | If contingency: signed writing, percentage stated, expense responsibility stated? | PASS / FAIL / N/A |
| Fee division                | If co-counsel: client consent and division stated per Rule 1.5(e)?                | PASS / FAIL / N/A |
| Conflict waiver             | If waiver: specific disclosure, fair and reasonable, signed consent?              | PASS / FAIL / N/A |
| Business transaction        | If Rule 1.8: written, fair, independent counsel advised, signed consent?          | PASS / FAIL / N/A |
| No-guarantee language       | Is outcome disclaimer present?                                                    | PASS / FAIL       |
| Withdrawal right            | Is attorney's permissive/mandatory withdrawal addressed?                          | PASS / FAIL       |
| Client's right to discharge | Is client's absolute right to discharge at any time stated?                       | PASS / FAIL       |
| Prohibited provisions       | Are any prohibited terms present (see Anti-Patterns, items 1–7)?                  | CLEAN / FLAG      |

**Flag any FAIL items** with a [REVIEW REQUIRED] marker and the specific rule citation.

**⟁ CLARIFY** — For any FAIL item that cannot be resolved without attorney judgment (e.g.,
the conflict waiver lacks specificity, or the scope excludes a category the client may expect),
ask the user how to proceed:

- Provide placeholder language and flag for attorney review
- Request the missing information before finalizing

### Step 7: Completeness Classification

Classify each required section of the letter using the three-tier system:

**COMPLETE** — The provision is present and meets applicable requirements. No further action.

**PARTIAL** — The provision is present but missing one or more required elements. Draft
the missing elements and flag for attorney review.

**MISSING** — The provision is entirely absent. Draft the complete section and present
to the attorney for approval.

For any PARTIAL or MISSING classification, apply the 3-pass Self-Interrogation (see Quality
Assurance Framework) before flagging.

### Step 8: Quality Verification

Run all quality checks before delivering the draft letter:

1. **Citation Quality Gates** — Run the 5 gates silently. Revise any failures.
2. **Ethics Compliance Review** — Verify no prohibited provisions remain (Step 6).
3. **Self-Interrogation** — For any MISSING critical provision, run the 3-pass review.
4. **Confidence Scoring** — Assign confidence levels to jurisdiction-specific requirements.
5. **Glass Box Audit Trail** — Generate and append to the output.

### Step 9: Finalize and Deliver

Produce the final output in the **Output Format** below:

1. **Engagement Letter (draft)** — Complete client-ready text
2. **Attorney Review Checklist** — All [REVIEW REQUIRED] flags consolidated
3. **Completeness Summary** — COMPLETE/PARTIAL/MISSING classification per section
4. **Glass Box Audit Trail** — YAML audit block

---

## Section-by-Section Reference

### Section 1: Identity of Client and Represented Parties

**Required elements:**

- Full legal name of the client (and each client, if multiple)
- For entity clients: the specific legal entity name (not just a trade name)
- Explicit statement of who is NOT represented (officers, directors, affiliates, related parties)
- For joint representations: disclosure that the firm represents all named clients and explain
  that communications between co-clients are not privileged against each other

**Status: COMPLETE / PARTIAL / MISSING**

**Common issues:**

- Representing a company but implying the founders are also clients
- Using a trade name instead of the legal entity name (creates ambiguity about which entity is the client)
- Failing to identify parties NOT represented when ambiguity exists (e.g., a partnership matter
  where the firm represents the partnership entity, not the individual partners)

**Draft template (entity client):**

> "We are pleased to represent [Full Legal Name of Entity], a [state] [entity type] (the
> "Client"). This engagement is limited to the legal services described below. Our
> representation does not extend to [officers, directors, shareholders, affiliates, or any
>
> > other related parties] individually, unless we expressly agree otherwise in writing."

**Draft template (individual client):**

> "We are pleased to represent [Client Full Name] ("Client") in connection with [matter
>
> > description]. This engagement is limited to [Client Full Name] individually; it does not
> > extend to any spouse, family member, business associate, or other party unless expressly
> > agreed in writing."

[JURISDICTION-SPECIFIC] For joint representations (e.g., spouses in estate planning):

> "We are representing both [Name 1] and [Name 2] jointly in connection with [matter]. We
> will share with each of you information relevant to this matter. If a conflict arises
> between your interests, we may be required to withdraw from representing one or both of you.
> By proceeding with this engagement, you each consent to this arrangement. You should be
> aware that attorney-client communications in joint representations may not be protected
> against disclosure to the other joint client."

---

### Section 2: Scope of Representation

**Required elements:**

- Specific description of the legal services to be provided
- Explicit statement of what is NOT included in this engagement
- Geographic scope limitations (if applicable)
- Phase limitations (e.g., representation through trial only; appeals not included)
- Conditions that must be met before representation begins (e.g., payment of retainer)

**Status: COMPLETE / PARTIAL / MISSING**

**Classification: REQUIRED BY PRACTICE** — Scope definition is the highest-risk provision.
Vague scope creates implied obligations and is the leading cause of attorney malpractice claims.

**Common issues:**

- "We will handle your legal matter" — does not specify what matter or what services
- "We will handle any claims arising from the accident" — may be read to include product
  liability or workers' compensation claims the attorney did not intend to cover
- Missing explicit exclusions: "This engagement does not include appeals, post-judgment
  proceedings, immigration matters, tax advice, or [other excluded categories]"
- For ongoing counsel engagements: failure to define which practice areas are included
  vs. excluded from the retainer scope

**Draft template (matter-specific):**

> "The scope of our representation is limited to [specific description of services]. This
> engagement does not include [list specific exclusions such as: appeals, ancillary
>
> > litigation, tax advice, regulatory filings, post-closing matters, or any other matters
> > not expressly described above]. If you ask us to assist with matters outside this scope,
> > we will notify you and, if we agree to expand our engagement, we will confirm that
> > expansion in writing."

**Draft template (litigation — with phase limitation):**

> "Our representation in this matter covers [describe specific litigation through trial].
> It does not include appeals, post-judgment collection, or any related claims or
> proceedings not described above. If you wish to retain us for an appeal, we will discuss
> the scope and fee arrangement separately and confirm any such extension in writing."

**⟁ CLARIFY** — If scope is unclear, ask: "What specific services should be described
in the scope section? What should be explicitly excluded? This is the most important
provision — please provide as much detail as possible."

---

### Section 3: Fee Structure and Billing Practices

**Required elements vary by fee type.** All must state the basis of the fee in writing.

#### 3a. Hourly Billing

**Required elements:**

- Billing rates for each timekeeper who will work on the matter (by name or title)
- Billing increment (typically 1/10th or 1/6th of an hour)
- When and how rates may change (advance notice requirement)
- Estimated range of fees (recommended; required in some jurisdictions under SRA rules)
- Billing frequency and payment due date
- Consequences of non-payment (withdrawal right, interest, collection)

**Draft template:**

> "Our fees for this matter are based on the time spent by attorneys and legal staff,
> billed at the following rates:
>
> | Timekeeper | Title                             | Hourly Rate      |
> | ---------- | --------------------------------- | ---------------- |
> | [Name]     | [Partner / Associate / Paralegal] | $[rate] per hour |
>
> Time is billed in [1/10th-hour / 6-minute] increments. We will send invoices [monthly /
>
> > bi-monthly], with payment due within [30] days of the invoice date. If billing rates
> > change, we will notify you in writing at least [30] days before the new rates take effect.
> > Continued use of our services after that notice constitutes acceptance of the new rates."

[JURISDICTION-SPECIFIC] California: Rate increases require client consent, not just notice;
language automatically implementing new rates on continued representation may be unenforceable [VERIFY].

#### 3b. Flat Fee

**Required elements:**

- Total fixed amount
- What the flat fee includes (specific deliverables or phases)
- What triggers additional fees (if scope expands)
- Whether and when the flat fee is earned (upfront vs. upon completion)
- Refund policy if representation ends before completion

**Draft template:**

> "Our fee for [specific services] is a flat fee of $[amount], which covers the services
> described in Section [X] above. This flat fee [is due upon execution of this letter /
> is due as follows: [payment schedule]]. It covers [list what is included]. It does not
> cover [list what would trigger additional fees]. If the scope of your matter expands
> beyond what is described above, we will notify you before incurring additional time or
> fees and will confirm any additional charges in writing."

#### 3c. Contingency Fee

**Required elements** (ABA Rule 1.5(c)) [VERIFY]:

- Percentage of recovery (and whether it varies pre-trial vs. at trial vs. on appeal)
- Whether the percentage is calculated before or after deducting expenses
- How expenses are handled: whether client owes expenses if no recovery
- Signed writing (contingency fee agreements must be in a written, signed agreement)
- Statement that fees are negotiable (some jurisdictions require this)
- Refund or termination provisions

**Draft template:**

> "Our fee for this representation is contingent upon recovery. If we achieve a favorable
> result, our fee will be [X]% of the gross recovery [or X% of the net recovery after
>
> > deducting expenses — specify which]. If the matter proceeds to trial, our fee will be
> > [X]% of the gross recovery. If no recovery is obtained, you will owe no attorney's fees.
> > [Specify expense responsibility: Expenses are / are not payable by you regardless of
> >
> > > > the outcome.] Upon conclusion, we will provide you with a written statement of the
> > > > outcome, the remittance to you, and the method of determination."

[JURISDICTION-SPECIFIC]:

- **California**: No contingency fees in domestic relations matters [VERIFY]
- **England & Wales**: Conditional fee arrangements (CFAs) are permitted subject to specific
  regulatory requirements; contingency fees in the US sense are more restricted [VERIFY]
- **Many jurisdictions**: Contingency fees in criminal matters are prohibited [VERIFY]

**⟁ CLARIFY** — For contingency matters, ask: "Is the contingency percentage calculated
on the gross recovery (before deducting expenses) or the net recovery? Are the client
responsible for expenses if there is no recovery?"

#### 3d. Advance Fee / Retainer

**Required elements:**

- Amount of the initial retainer/advance fee
- Whether the funds are placed in a client trust account (IOLTA or equivalent)
- When and how funds are withdrawn (as fees are earned / as expenses are incurred)
- When the retainer must be replenished (evergreen) or whether it is a one-time deposit
- Refund obligation: unearned funds returned to client upon termination

**Draft template:**

> "We require an advance fee deposit of $[amount] before commencing representation. These
> funds will be deposited in our client trust account and will not be treated as earned
> until applied to fees or expenses as they are incurred. We will apply fees and expenses
> against this deposit as work is performed and will provide you with a statement of each
> application with your monthly invoice. [For evergreen:] When the balance in the trust
> account falls below $[threshold], you agree to replenish it to $[amount] within [10]
> days of our request. Unearned funds remaining at the conclusion of the engagement will
> be returned to you promptly."

[JURISDICTION-SPECIFIC] **Prohibited**: Language stating advance fees are "non-refundable"
is prohibited in most US jurisdictions [VERIFY]. California expressly prohibits this [VERIFY].

---

### Section 4: Expense Reimbursement

**Required elements:**

- Categories of expenses that will be billed to the client
- Whether expenses are charged at cost or marked up (and the markup rate)
- Prior approval requirements for expenses above a threshold
- How expenses appear on invoices

**Status: REQUIRED BY PRACTICE**

**Draft template:**

> "In addition to our fees, you will be responsible for the following categories of expenses
> incurred on your behalf: court filing fees, process server fees, deposition transcript
> costs, expert witness fees and costs, travel expenses, document reproduction at $[rate]
> per page, computerized legal research, postage and courier fees, and similar out-of-pocket
> costs. We charge these expenses [at cost / at cost plus [X]% to cover administrative
> costs]. We will not incur individual expenses in excess of $[amount] without your prior
> written approval. Expenses will be itemized on your monthly invoice."

**Common issues:**

- Not specifying who pays expenses in a contingency matter if there is no recovery
- Including vague categories like "miscellaneous" without defining what is included
- Not disclosing markup on copies or research (some bar rules require disclosure)

---

### Section 5: Client Responsibilities

**Required elements:**

- Obligation to provide accurate and complete information
- Cooperation with counsel's requests for documents and information
- Timely response to inquiries and decisions
- Payment obligations

**Status: REQUIRED BY PRACTICE**

**Draft template:**

> "Your effective representation depends on your cooperation. You agree to:
>
> - **Provide complete and accurate information**: Promptly disclose all facts, documents,
>   and circumstances relevant to your matter, including information that may be adverse
>   to your position.
> - **Respond to our requests**: Reply to our calls, emails, and correspondence within
>   [three / five] business days. Delays in response may affect our ability to meet
>   deadlines and may result in additional fees.
> - **Make timely decisions**: Authorize us to proceed, or decline to proceed, on matters
>   requiring your decision promptly. We cannot guarantee timely service if decisions are
>   delayed.
> - **Keep us informed**: Notify us promptly of any changes in your contact information,
>   circumstances, or objectives relevant to your matter.
> - **Pay invoices promptly**: Pay all invoices within [30] days of the invoice date."

---

### Section 6: Conflict of Interest Disclosures

**Required elements** (when a conflict waiver is obtained):

- Specific identification of the conflict: the parties, the nature of the adverse interest
- Assessment that the firm can competently represent both/all parties notwithstanding the conflict
- Disclosure of the implications, advantages, and risks of the waiver to the client
- Advice to seek independent counsel regarding the waiver
- Signed informed consent from the client

**Status: REQUIRED when a conflict exists**

[JURISDICTION-SPECIFIC] Advance conflict waivers (for ongoing counsel):

- Must identify the categories of potential future conflicts with specificity
- Must assess the likelihood that conflicts will arise
- Generic blanket waivers are unenforceable in most jurisdictions [VERIFY]
- ABA Formal Opinion 05-436 provides guidance on advance conflict waivers [VERIFY]

**Draft template (specific conflict with waiver):**

> "We have identified a potential conflict of interest in this engagement: [describe the
> specific conflict, e.g., 'We currently represent [Other Party] in an unrelated matter,
> and [Other Party] may have interests adverse to yours in [describe context].'] We believe
> we can represent you competently and diligently notwithstanding this conflict. However,
> you should be aware of the following implications: [describe specific implications].
>
> We recommend that you seek independent legal advice regarding this conflict waiver before
> signing. If you choose to waive this conflict, please sign below acknowledging that you
> understand the conflict and its implications and that you consent to our representation."

**⟁ CLARIFY** — If a conflict waiver is required, ask: "What is the specific conflict?
Who are the affected parties? Have you recommended that the client seek independent counsel
on the waiver?" A vague conflict waiver is legally insufficient and creates significant risk.

---

### Section 7: Confidentiality and Attorney-Client Privilege

**Required elements:**

- Basic explanation of the duty of confidentiality
- Explanation of the attorney-client privilege
- Limitations on privilege (joint representations, disclosure by client, etc.)
- Treatment of communications via electronic means

**Status: RECOMMENDED** (required for sophisticated clients and joint representations)

**Draft template:**

> "Our communications with you are protected by the attorney-client privilege and by our
> professional duty of confidentiality. This means we will not voluntarily disclose your
> confidential information to third parties without your consent, subject to limited
> exceptions required by applicable law (such as preventing imminent serious bodily harm).
>
> The attorney-client privilege protects our confidential communications from compelled
> disclosure in legal proceedings, subject to applicable exceptions (including the crime-fraud
> exception). The privilege belongs to you as the client; you may waive it, but we cannot.
>
> [For joint representations:] When we represent multiple clients jointly, our duty of
> confidentiality runs to all clients jointly. Communications shared among co-clients
> are not privileged as against each other. If a conflict arises requiring us to withdraw
> from representing one or more clients, communications made during the joint representation
> may be disclosed to all joint clients."

---

### Section 8: No Guarantee of Outcome

**Required elements:**

- Explicit disclaimer that no guarantee of outcome or result is made
- Statement that legal outcomes are inherently uncertain
- For litigation: specific acknowledgment that court results cannot be predicted

**Status: REQUIRED BY PRACTICE** — particularly for litigation; absence is a significant
malpractice risk factor across all practice areas.

**Draft template:**

> "We will apply our best professional efforts to advance your interests in this matter.
> However, we cannot guarantee any particular outcome or result. Legal proceedings are
> inherently uncertain, and past results do not guarantee future outcomes. No statement we
> make — verbally or in writing — should be construed as a promise or guarantee of a
> specific result. Our analysis and advice reflect our professional judgment based on the
> information available at the time; as circumstances change, our assessment may change."

---

### Section 9: Termination of Representation

**Required elements:**

- Client's absolute right to terminate representation at any time
- Client's obligation to pay fees and expenses incurred through termination date
- Circumstances under which the firm may withdraw (permissive) or must withdraw (mandatory)
- Notice requirements for termination or withdrawal
- Post-termination obligations (file transfer, transition assistance)

**Status: REQUIRED BY PRACTICE**

**Draft template:**

> "**Your right to terminate**: You may terminate this representation at any time, for any
> reason, by notifying us in writing. Termination does not affect your obligation to pay
> all fees and expenses incurred through the date we receive your notice.
>
> **Our right to withdraw**: We reserve the right to withdraw from this representation upon
> reasonable notice if: (a) you fail to pay fees or expenses within [30] days of the due
> date after written notice; (b) you request us to take actions we believe are illegal or
> unethical; (c) you fail to cooperate with our representation; (d) a conflict of interest
> arises that cannot be waived; or (e) continued representation would impose an unreasonable
> financial burden on us. We may also be required to withdraw if circumstances arise that
> require mandatory withdrawal under applicable professional responsibility rules. If
> representation in a court proceeding requires court approval to withdraw, we will seek
> such approval but cannot guarantee it will be granted.
>
> Upon termination or withdrawal, we will promptly provide you with your client file and
> take reasonable steps to protect your interests during any transition period."

[JURISDICTION-SPECIFIC]: In some jurisdictions, notice periods for withdrawal are regulated
by bar rules or court rules. [VERIFY] the applicable requirements.

---

### Section 10: File Retention

**Required elements:**

- How long the firm will retain the file after the matter closes
- What the client will receive at the end of the engagement
- When the client must request their file before destruction
- How the file will be destroyed

**Status: RECOMMENDED** (required by practice; some jurisdictions mandate disclosure)

**Draft template:**

> "Upon conclusion of this matter, we will retain your file for [specify number, typically
>
> > 5–10 years] from the date of closing, after which we may destroy the file without further
> > notice. Before destruction, we will [provide / make available upon request] a copy of
> > your documents. You may request your complete file at any time during the retention
> > period. We recommend that you retain a copy of your file for your own records.
>
> [Optional: If the file contains original documents with intrinsic value — such as
>
> > original wills, deeds, or corporate minutes — we will return those to you at the
> > conclusion of the matter.]"

[JURISDICTION-SPECIFIC] Minimum retention periods vary by jurisdiction and matter type.
Common guidance [VERIFY]:

- Litigation: 7–10 years (or until all appeals exhausted)
- Estate planning: life of the client or longer (original documents may have indefinite value)
- Corporate/transactional: 6–7 years
- Tax: 7–10 years

---

### Section 11: Ethics Disclosures and Regulatory Notices

**Required elements vary significantly by jurisdiction.**

#### 11a. Fee Dispute Arbitration (New York)

[JURISDICTION-SPECIFIC — NEW YORK] [VERIFY]:

> "If a dispute arises concerning our fees, you have the right to seek arbitration of the
> dispute pursuant to Part 137 of the Rules of the Chief Administrator of the Courts.
> We will provide you with information about arbitration upon request."

#### 11b. Complaints Procedure (England & Wales)

[JURISDICTION-SPECIFIC — ENGLAND & WALES] [VERIFY]:

> "We are committed to providing a high-quality legal service. If you are not satisfied
> with any aspect of our service, please contact [complaints partner / department] at
> [contact details]. If we are unable to resolve your complaint to your satisfaction, you
> may refer it to the Legal Ombudsman (LeO) at PO Box 6167, Slough SL1 0EH, or at
> legalombudsman.org.uk. You must ordinarily bring a complaint to the LeO within one year
> of the act or omission complained of, or within one year of when you should reasonably
> have known there was cause for complaint. We are regulated by the Solicitors Regulation
> Authority (SRA) in relation to our legal activities."

#### 11c. Insurance and Regulatory Status (England & Wales)

[JURISDICTION-SPECIFIC — ENGLAND & WALES] [VERIFY]:

> "We hold professional indemnity insurance as required by the SRA. Details of our
> insurance are available upon request. Our SRA registration number is [number]. You can
> verify our regulatory status at the SRA website."

#### 11d. AML Compliance Notice (applicable where regulated)

[JURISDICTION-SPECIFIC — required in UK, applicable in US for certain matters] [VERIFY]:

> "We are required by law to verify the identity of our clients and, in certain matters,
> to verify the source of funds. By engaging our services, you agree to provide
> documentation sufficient to satisfy our obligations under applicable anti-money laundering
> regulations. We may be required by law to report certain information to regulatory
> authorities without notifying you first."

---

## Completeness Classification System

For engagement letter audits or gap analysis mode, classify each required section:

### COMPLETE — All Required Elements Present

The section contains all elements required by applicable bar rules and best practice.
No further action required.

**Examples:**

- Fee description states the basis, rate, and billing method (ABA Rule 1.5(b))
- Contingency fee clause is in a signed written agreement, states the percentage,
  and explains expense responsibility (Rule 1.5(c))
- Scope specifically describes included and excluded services

### PARTIAL — Missing One or More Required Elements

The section exists but omits one or more required or important elements.
Draft the missing element and flag for attorney review.

**Examples:**

- Fee rate stated but billing increment not specified
- Termination right stated but post-termination file transfer not addressed
- Expense reimbursement listed but prior approval threshold missing

**Action**: Generate the missing sub-element language. Present to attorney as [ADD: proposed
language for attorney review].

### MISSING — Provision Entirely Absent

The provision is entirely absent from the letter.
Draft the complete section and flag for attorney review.

**Examples:**

- No conflict disclosure when a conflict exists
- No no-guarantee-of-outcome language in a litigation engagement
- No file retention provision

**Action**: Generate the complete section. Present to attorney as [MISSING — REVIEW REQUIRED:
proposed language for attorney approval].

---

## Prioritization Framework

When presenting gaps or required revisions to the attorney, organize by priority:

### Tier 1 — Required by Law (Mandatory)

Provisions mandated by applicable bar rules, statutes, or regulations. Absence creates
immediate ethics violation risk.

- Written fee disclosure per applicable rule (ABA Rule 1.5(b); CA § 6148; NY Part 1215)
- Contingency fee in a signed written agreement (ABA Rule 1.5(c))
- Conflict disclosure and signed waiver (ABA Rules 1.7, 1.9)
- Business transaction disclosure and consent (ABA Rule 1.8)
- Fee division disclosure (ABA Rule 1.5(e))
- SRA complaints procedure and Legal Ombudsman notice (England & Wales)

**Action**: Do not deliver the letter without these provisions. Flag as [CRITICAL — DO NOT
SEND WITHOUT ATTORNEY REVIEW AND ADDITION].

### Tier 2 — Required by Practice (Strong Preference)

Provisions not mandated by rule but absence creates significant malpractice or ethics risk.

- Scope of representation with explicit exclusions
- No-guarantee-of-outcome language
- Client's right to terminate at any time
- Attorney's right to withdraw (circumstances and notice)
- File retention policy

**Action**: Draft these provisions. Flag as [HIGH PRIORITY — STRONGLY RECOMMENDED].

### Tier 3 — Recommended (Best Practice)

Provisions that improve the engagement letter and reduce the risk of disputes but are not
strictly required.

- Communication protocol and response time expectations
- Billing dispute resolution process
- Joint representation privilege disclosure
- Electronic communication acknowledgment
- Expense pre-approval thresholds

**Action**: Include as a matter of course. Flag omissions as [RECOMMENDED ADDITION].

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering the draft letter. Revise any failures.

| Gate           | Rule                                                                                                       | Fail Action                                              |
| -------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every bar rule or statutory requirement cites a specific rule number or statute                            | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format (e.g., ABA Model Rule 1.5(b), 22 NYCRR Part 1215.1) | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments or repeal                                                     | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the applicable jurisdiction's rules; no assumptions from other jurisdictions         | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty about a legal requirement explicitly stated; not presented as settled                          | Add confidence qualifier                                 |

### Self-Interrogation for Missing Critical Provisions

For any provision classified MISSING at Tier 1 priority, apply this 3-pass review before
flagging to the attorney:

**Pass 1 — Regulatory Chain Integrity**:

- Does the bar rule or statute actually require this provision in this jurisdiction?
- Is there an exception that might apply (e.g., NY Part 1215 exceptions for fees under
  $3,000 or repeat clients)?
- Is the classification correct, or is this actually a Tier 2 provision?

**Pass 2 — Completeness**:

- Have all applicable rules been checked (not just the ABA Model Rules)?
- Is there a state-specific requirement that goes beyond the ABA baseline?
- Are there practice-area-specific rules that apply (domestic relations, criminal,
  contingency fee restrictions)?

**Pass 3 — Challenge**:

- What is the strongest argument that this provision is not required in this letter?
- Are there circumstances where omitting this provision is acceptable (e.g., existing
  client, prior engagement letter on file)?
- Is the MISSING classification proportionate to the actual risk?

Mark the audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each jurisdiction-specific requirement, assign a confidence level:

| Level        | Range     | Meaning                                             | Action                                                   |
| ------------ | --------- | --------------------------------------------------- | -------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear rule or statute, unambiguous application      | State with confidence                                    |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions    | State with brief caveat                                  |
| **Probable** | 0.60–0.79 | Good arguments but jurisdiction not fully confirmed | State with explicit reasoning                            |
| **Possible** | 0.40–0.59 | Genuinely uncertain — rule may vary by circumstance | Flag for attorney review                                 |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                             | Do not assert; flag as "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every engagement letter output MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-engagement-letter-drafter"
  client: "[Client name]"
  matter: "[Brief matter description]"
  matter_type: "[Practice area / litigation / transactional / advisory]"
  jurisdiction: "[State / SRA / general]"
  applicable_rules:
    - "[Rule 1.5(b) — VERIFIED or UNVERIFIED]"
    - "[State-specific rule — VERIFIED or UNVERIFIED]"
  fee_structure: "[hourly / flat fee / contingency / retainer / hybrid]"
  conflict_status: "[clear / waiver obtained / advance waiver / not checked]"
  sections_drafted:
    - identity_of_client: "COMPLETE / PARTIAL / MISSING"
    - scope_of_representation: "COMPLETE / PARTIAL / MISSING"
    - fee_structure: "COMPLETE / PARTIAL / MISSING"
    - expense_reimbursement: "COMPLETE / PARTIAL / MISSING"
    - client_responsibilities: "COMPLETE / PARTIAL / MISSING"
    - conflict_disclosures: "COMPLETE / PARTIAL / MISSING / N/A"
    - confidentiality: "COMPLETE / PARTIAL / MISSING"
    - no_guarantee: "COMPLETE / PARTIAL / MISSING"
    - termination: "COMPLETE / PARTIAL / MISSING"
    - file_retention: "COMPLETE / PARTIAL / MISSING"
    - ethics_disclosures: "COMPLETE / PARTIAL / MISSING"
  tier_1_issues: "[number or 'None']"
  tier_2_issues: "[number or 'None']"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / N/A"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  prohibited_provisions_check: "CLEAN / [list any flagged items]"
  limitations:
    - "[Any assumptions made, placeholders inserted, or scope limitations]"
  reviewer: "AI-assisted — requires attorney review before sending to client"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do when drafting or reviewing engagement letters:

1. **Using a one-size-fits-all boilerplate** — Generic engagement letters that are not
   adapted to the specific client, matter, and jurisdiction are the leading source of
   malpractice claims. Every engagement letter must be customized. This skill exists to
   make customization systematic, not to produce another template.

2. **Vague scope language** — "We will handle your legal matter" or "any and all claims
   arising from the accident" creates ambiguity about what is included. Vague scope creates
   implied obligations. Be specific about what is in scope and explicitly list what is out.

3. **Labeling advance fees as non-refundable** — Most US jurisdictions prohibit labeling
   advance fee retainers as "non-refundable." Unearned fees must be returned. [VERIFY] the
   applicable rule before using any language that restricts refund rights.

4. **Promising outcome or using outcome-suggesting language** — Phrases like "we will get
   you a settlement," "we expect a favorable result," or "we have a strong case" can
   constitute an implied guarantee. Always include the no-guarantee disclaimer and train
   attorneys not to make oral promises that contradict it.

5. **Failing to identify the actual client in entity representations** — "Representing ABC
   Corp" does not automatically exclude representing officers, directors, or affiliates. If
   the firm represents only the entity, state explicitly that it does not represent any
   individual associated with the entity.

6. **Advance conflict waivers without sufficient specificity** — A generic "you agree to
   waive any future conflicts of interest" clause is unenforceable in most jurisdictions.
   Advance waivers must describe the categories of potential future conflicts with
   sufficient detail to enable informed consent. [VERIFY] the applicable ethics rule.

7. **Contingency fee language without stating expense responsibility** — ABA Rule 1.5(c)
   requires the agreement to state how expenses are to be paid whether or not the client
   prevails. Failure to address this creates billing disputes when the client believes
   "no fee if no recovery" means no expenses either.

8. **Rate change provisions that automatically take effect without client consent** —
   In California and some other jurisdictions, billing rate increases require affirmative
   client consent, not just notice. Language that states "continued engagement constitutes
   acceptance" may be unenforceable [VERIFY]. Confirm the jurisdiction's rule before
   using this approach.

9. **Omitting the client's right to discharge counsel at any time** — This is an absolute
   right under the attorney-client relationship. Engagement letters that imply the client
   cannot terminate are both unenforceable and ethics violations. Always state this right
   clearly.

10. **Exceeding scope silently** — When the attorney performs work outside the scope of
    the engagement letter, the limited scope letter provides no protection in a malpractice
    claim. Scope expansions must be confirmed in a written amendment or supplemental letter.
    Train attorneys to recognize when scope is being exceeded and to document accordingly.

11. **Missing withdrawal provisions for fee non-payment** — Many attorneys intend to
    withdraw if unpaid but fail to specify this right in the engagement letter. Without the
    express right, withdrawal for non-payment may require additional bar approval. State the
    right and the notice required.

12. **No file retention policy** — The engagement letter is the ideal place to disclose the
    firm's file retention and destruction policy. Clients who later demand their file years
    after closing have a stronger claim if the policy was never disclosed. Communicate
    retention periods upfront.

13. **Ignoring applicable state-specific requirements** — ABA Model Rules are a floor,
    not a ceiling. Many states require more than the ABA baseline (NY Part 1215's mandatory
    engagement letter, NY Part 137's fee arbitration notice, California's $1,000 threshold
    and consent to rate increases). Always check the applicable state rule before relying
    solely on ABA Model Rules.

14. **Joint representation without privilege disclosure** — When multiple clients are
    represented jointly, they should be told that communications between co-clients are
    not privileged against each other and that the firm may need to withdraw if a conflict
    arises. Omitting this disclosure creates disclosure problems and malpractice exposure.

15. **Fee division without client disclosure** — ABA Rule 1.5(e) requires that fee-sharing
    arrangements between different firms be disclosed to the client in writing, with the
    division stated, and the client's consent confirmed. Omitting this is an ethics violation
    even if the arrangement is common in the practice area.

---

## Writing Standards

Apply plain-language discipline to all engagement letter output:

**For the client-facing engagement letter:**

- Plain language. Avoid unnecessary legalese and Latin terms.
- Active voice: "We will represent you" not "Representation shall be provided to you."
- Short sentences. One legal concept per paragraph.
- Clear headings for each topic. Clients should be able to find any provision easily.
- Define key terms on first use if they carry specific legal meaning.
- Never assume the client is a lawyer. Test each paragraph against the question: "Could
  a non-lawyer client understand this?"

**For attorney review notes and completeness summaries:**

- Same plain-language standards, with more precise legal references.
- Cite the specific rule or statute driving each requirement.
- Flag uncertainty explicitly; do not present uncertain requirements as settled.
- Format flag items consistently: [REVIEW REQUIRED], [MISSING], [ADD], [VERIFY].

**Quality gates before delivery:**

1. Can a non-lawyer client read and understand the entire letter without legal assistance?
2. Is every required provision present and clearly stated?
3. Is every jurisdiction-specific claim backed by a citation (or flagged [VERIFY])?
4. Are any provisions ambiguous about scope, fee amount, or client identity?
5. Has the no-guarantee language been included?
6. Are there any prohibited provisions (non-refundable retainer language, rate change
   without consent in California, contingency fee in a prohibited matter type)?
7. Would the letter survive bar association review in the applicable jurisdiction?

---

## External Tool Integration

This skill uses **legalcode-mcp** as its primary legal authority source.

**With legalcode-mcp connected:**

- In Step 4, search for current text of applicable bar rules, statutes, and formal ethics opinions
- Verify specific rule citations (ABA Rule 1.5(b), 22 NYCRR Part 1215.1, CA B&P § 6148, SRA
  Transparency Rules) against current authority
- Search for recent bar opinions on advance conflict waivers, fee disclosure requirements,
  or other evolving areas
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with general ABA Model Rule framework and the jurisdiction identified in Step 2
- Mark all specific statutory citations with [VERIFY]
- Focus the output on structural quality and required elements rather than precise rule text
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`

---

## Localization Notes

### US Jurisdiction Variations

| Jurisdiction        | Key Variation                                                                                                                                                               | Rule Citation                         |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **New York**        | Written engagement letter required for fees >$3,000; fee arbitration notice required; repeat clients and small fees excepted                                                | 22 NYCRR Part 1215 [VERIFY]           |
| **California**      | Written fee agreement required when fees expected to exceed $1,000; rate increases require client consent (not just notice); advance fees may not be labeled non-refundable | CA B&P § 6148; CRPC Rule 1.5 [VERIFY] |
| **Texas**           | Written fee agreements required for contingency fees and certain other matter types; specific State Bar referral rules                                                      | TX Disciplinary Rules [VERIFY]        |
| **Florida**         | Written fee agreements required for contingency fees; specific disclosure requirements                                                                                      | Florida Bar Rules [VERIFY]            |
| **Other US States** | Review applicable state Rules of Professional Conduct. ABA Model Rules are a minimum; most states have divergent requirements                                               | State RPCs [VERIFY]                   |

### UK / England & Wales Variations

| Requirement                | Standard                                                                                         | Rule Citation                                                       |
| -------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Client care letter         | Required for all private client matters                                                          | SRA Code of Conduct [VERIFY]                                        |
| Costs estimate             | Required — best possible information about overall cost                                          | SRA Transparency Rules [VERIFY]                                     |
| Complaints procedure       | Must be disclosed at engagement; LeO notice required                                             | SRA Transparency Rules [VERIFY]                                     |
| Regulatory status          | Must disclose whether and how services are regulated                                             | SRA Code of Conduct [VERIFY]                                        |
| AML verification           | Required for most matter types                                                                   | MLR 2017 [VERIFY]                                                   |
| Conditional fee agreements | Permitted subject to specific regulatory requirements; US-style contingency fees more restricted | Legal Aid, Sentencing and Punishment of Offenders Act 2012 [VERIFY] |

---

## Output Format Template

```markdown
---
ENGAGEMENT LETTER DRAFT
Generated: [date]
Jurisdiction: [identified jurisdiction]
Matter Type: [practice area]
Fee Structure: [structure type]
---

[FIRM LETTERHEAD]

[Date]

[Client Full Name]
[Client Address]

**Re: Engagement Letter — [Brief Matter Description]**

Dear [Client Name]:

---

## Our Representation

[Section 1: Identity of Client — drafted text]

---

## Scope of Representation

[Section 2: Scope — drafted text]

---

## Fee Structure and Billing

[Section 3: Fee structure — drafted text]

---

## Expenses

[Section 4: Expense reimbursement — drafted text]

---

## Your Responsibilities

[Section 5: Client responsibilities — drafted text]

---

## Conflict of Interest

[Section 6: Conflict disclosures — drafted text, or "No conflicts have been identified
in connection with this engagement." if conflicts clear]

---

## Confidentiality and Attorney-Client Privilege

[Section 7: Confidentiality — drafted text]

---

## No Guarantee of Outcome

[Section 8: No guarantee — drafted text]

---

## Termination of Representation

[Section 9: Termination — drafted text]

---

## File Retention

[Section 10: File retention — drafted text]

---

## Additional Disclosures

[Section 11: Ethics disclosures — jurisdiction-specific text]

---

If the foregoing accurately reflects your understanding of our engagement, please sign
below and return a copy to us [together with your retainer of $[amount]]. We look forward
to working with you.

Very truly yours,

[Attorney Name]
[Firm Name]
[Bar Number]
[Contact Information]

---

**Client Acknowledgment and Agreement**

The undersigned acknowledges receipt of this engagement letter and agrees to its terms.

Signature: **\*\***\*\*\*\***\*\***\_**\*\***\*\*\*\***\*\*** Date: **\*\***\_\_\_**\*\***

Printed Name: **\*\***\*\***\*\***\_\_\_**\*\***\*\***\*\***

[For entity clients:]
Title: **\*\*\*\***\*\***\*\*\*\***\_\_\_**\*\*\*\***\*\***\*\*\*\***
On behalf of: **\*\***\*\***\*\***\_\_\_\_**\*\***\*\***\*\***

---

## ATTORNEY REVIEW CHECKLIST

[List all [REVIEW REQUIRED] flags from the draft above]

| #   | Section   | Flag                         | Action Required   |
| --- | --------- | ---------------------------- | ----------------- |
| 1   | [Section] | [MISSING / PARTIAL / VERIFY] | [Specific action] |

---

## COMPLETENESS SUMMARY

| Section                 | Status                             | Notes  |
| ----------------------- | ---------------------------------- | ------ |
| Identity of Client      | COMPLETE / PARTIAL / MISSING       | [Note] |
| Scope of Representation | COMPLETE / PARTIAL / MISSING       | [Note] |
| Fee Structure           | COMPLETE / PARTIAL / MISSING       | [Note] |
| Expense Reimbursement   | COMPLETE / PARTIAL / MISSING       | [Note] |
| Client Responsibilities | COMPLETE / PARTIAL / MISSING       | [Note] |
| Conflict Disclosures    | COMPLETE / PARTIAL / MISSING / N/A | [Note] |
| Confidentiality         | COMPLETE / PARTIAL / MISSING       | [Note] |
| No Guarantee of Outcome | COMPLETE / PARTIAL / MISSING       | [Note] |
| Termination             | COMPLETE / PARTIAL / MISSING       | [Note] |
| File Retention          | COMPLETE / PARTIAL / MISSING       | [Note] |
| Ethics Disclosures      | COMPLETE / PARTIAL / MISSING       | [Note] |

**Tier 1 Issues (Required by Law):** [number] — [list if any]
**Tier 2 Issues (Required by Practice):** [number] — [list if any]

---

## GLASS BOX AUDIT TRAIL

[YAML block per Glass Box template above]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

- ABA Model Rules of Professional Conduct (Rules 1.5, 1.6, 1.8, 1.16)
- 22 NYCRR Part 1215 (New York engagement letter rules)
- California Business and Professions Code § 6148 and CRPC Rule 1.5
- SRA Code of Conduct for Solicitors and SRA Transparency Rules (England & Wales)
- ACTEC Engagement Letters: A Guide for Practitioners (2017)
- State bar guidance from NY State Bar Association, California State Bar, and SRA
- Legal malpractice risk management guidance from ALPS Insurance
- Law firm management resources from Clio, LeanLaw, and LawPay

Quality frameworks (Citation Quality Gates, Self-Interrogation, Confidence Scoring,
Glass Box Audit Trail, Anti-Patterns, Writing Standards) adapted from
`legalcode-contract-review` gold standard skill.

Structural patterns adapted from `legalcode-client-intake-workflow`.

All statutory citations require verification against current authoritative sources;
rules of professional conduct change and vary by jurisdiction.
