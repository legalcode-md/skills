---
name: legalcode-services-agreement-drafter
description: >
  Draft and review standalone commercial services agreements for defined-scope engagements
  — fixed-price projects, time-and-materials assignments, milestone-based delivery,
  and hybrid fee structures. Covers scope of work and deliverable specification, change
  control, fees and payment (including acceptance testing, disputed invoices, and audit
  rights), intellectual property ownership and licensing (background/foreground IP,
  assignment formalities, license-back, moral rights), professional and fitness-for-purpose
  warranties, limitation of liability, indemnification (IP, data breach, gross negligence),
  data protection obligations, subcontracting controls, termination (cause, convenience,
  insolvency), and transition/wind-down assistance. Use when drafting or reviewing a
  single-document services agreement for a specific project or discrete engagement — as
  distinct from a two-tier Master Services Agreement / Statement of Work framework. Suitable
  for consulting, IT delivery, creative services, advisory, research, engineering, and any
  professional services engagement where scope, timeline, and deliverables are defined in
  a single instrument. Jurisdiction-agnostic with localization markers for US, UK, AU, and EU.
  Produces confidence-scored, auditable drafts or redlines with Glass Box audit trail.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-6
context: fork
agent: general-purpose
---

# Legalcode Services Agreement Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted drafting and review of
> commercial services agreements. It does not constitute legal advice. All outputs should
> be reviewed by a qualified legal professional licensed in the relevant jurisdiction before
> use. Laws change; verify current applicability before relying on any provision described
> here. IP assignment formality requirements, implied warranty terms, unfair contract terms
> rules, data protection obligations, and liability exclusion enforceability vary materially
> across jurisdictions — verify jurisdiction-specific requirements against authoritative
> sources before finalising any agreement. Statutory and case law references cited from
> memory carry hallucination risk — verify against authoritative sources before relying
> on them.

---

## Purpose and Scope

This skill drafts and reviews standalone commercial services agreements — single-document
contracts for a specific, defined engagement between a service provider and a client. It
provides clause-by-clause guidance from **both service provider and client perspectives**,
classifies deviations, and generates actionable redlines or draft language with confidence
scoring.

**Covers (dual-mode: Draft and Review):**
- Standalone services agreements (consulting, IT delivery, creative, advisory, research,
  engineering, and other professional services)
- Fixed-price, time-and-materials (T&M), milestone-based, retainer, and hybrid fee structures
- Scope of work and deliverable specification within the main agreement body
- Change control procedures (unilateral, bilateral, and hybrid mechanisms)
- Acceptance testing: criteria, review periods, deemed acceptance, cure, rejection
- IP ownership: background/foreground allocation, assignment formalities (US/UK/AU), license-back,
  moral rights waivers, open source taint risk
- Warranties: professional standard, fitness for purpose, compliance, title and non-infringement
- Limitation of liability: cap mechanics, carveouts, consequential damages exclusions
- Indemnification: IP infringement, data breach, death/personal injury, gross negligence
- Data protection: GDPR/UK GDPR Article 28 processor obligations, DPA requirement, sub-processors
- Subcontracting: consent requirements, flow-down obligations, liability allocation
- Term and termination: cause triggers, cure periods, convenience, insolvency events
- Transition/wind-down: knowledge transfer, post-termination cooperation, successor support
- Quality-verified output with Glass Box audit trail and confidence scoring

**Does not:**
- Draft two-tier Master Services Agreement / Statement of Work frameworks (see
  `legalcode-master-services-agreement`)
- Provide clause-by-clause review of any commercial agreement (see `legalcode-contract-review`)
- Draft SaaS or platform subscription agreements (see `legalcode-saas-agreement-drafter`)
- Replace specialist counsel for regulated-sector engagements (financial services, healthcare,
  defence, government), high-value complex outsourcing, or cross-border transactions requiring
  country-specific advice
- Apply to any single jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC]
  markers throughout

**Related skills:**
- `legalcode-master-services-agreement` — two-tier MSA + SOW/Order Form framework for
  recurring, managed, or enterprise service lines
- `legalcode-contract-review` — clause-by-clause review of any commercial agreement
- `legalcode-nda-triage` — standalone NDA triage and analysis
- `legalcode-dpa-review-and-negotiation` — specialist DPA analysis under GDPR/UK GDPR/CCPA
- `legalcode-contract-risk-scorer` — quantified risk scoring of agreed terms
- `legalcode-redline-generator` — standalone redline generation from analysed positions
- `legalcode-limitation-of-liability-review` — deep analysis of limitation and exclusion clauses

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The governing law clause in the services agreement
determines which legal framework applies. The workflow identifies the governing law early
and adapts analysis and draft language accordingly.

[JURISDICTION-SPECIFIC] When localising, research and apply the following:

**United States**
- IP: Work-for-hire doctrine (17 U.S.C. § 101) — applies only to works within scope of
  employment or nine categories of specially commissioned works where parties agree in
  writing. For software and most deliverables, a written assignment is required; "work-for-hire"
  language alone may not suffice if the work does not qualify under the statutory categories.
  Copyright assignment requires a signed writing; no witness or notarisation requirement [VERIFY]
- CISG: applies by default to international sales of goods; commonly excluded by express
  opt-out. Courts are split on whether services contracts are CISG-exempt [VERIFY]
- Liability exclusions: subject to unconscionability doctrine (state law); conspicuous form
  may be required for warranty disclaimers if goods are involved (UCC § 2-316) [VERIFY]
- Non-competes: state-specific — void in California (Cal. Bus. & Prof. Code § 16600),
  with varying enforceability in New York, Texas, and others [VERIFY]
- Arbitration: governed by Federal Arbitration Act (9 U.S.C.); class action waivers
  generally enforceable in commercial B2B contexts [VERIFY]

**United Kingdom**
- IP: No work-for-hire doctrine for independent contractors. Copyright in contractor-created
  works belongs to the contractor by default unless validly assigned. Copyright assignment
  must be in writing signed by or on behalf of the assignor (CDPA 1988, s.90(3)). Design
  right assignment: CDPA 1988, s.222(3). Patent assignment: Patents Act 1977, s.30(6) [VERIFY]
- Moral rights: Cannot be assigned, only waived (CDPA 1988, ss.77-85). Blanket waivers are
  enforceable in B2B contracts [VERIFY]
- Liability exclusions: UCTA 1977 — B2B exclusions must satisfy the reasonableness test
  (s.11 and Sched. 2); death/personal injury exclusions void (s.2(1)); negligence exclusions
  require reasonableness (s.2(2)). Consumer Rights Act 2015 — applies where any party is a
  consumer [VERIFY]
- Third-party rights: Contracts (Rights of Third Parties) Act 1999 — third-party rights
  may attach unless expressly excluded [VERIFY]
- IR35 / off-payroll working: ITEPA 2003, Pt. 2, Ch. 8 and Ch. 10 — medium/large clients
  bear responsibility for status determination from April 2021; PSC engagement triggers
  deemed employment risk [VERIFY]

**Australia**
- IP: No work-for-hire doctrine for independent contractors. Copyright in contractor works
  belongs to the contractor unless assigned. Copyright assignment must be in writing
  (Copyright Act 1968, s.196(3)). Patent assignment requires writing and registration
  (Patents Act 1990, s.14) [VERIFY]
- Unfair contract terms: Australian Consumer Law (CCA 2010, Sched. 2) — small business
  unfair terms regime (eff. November 2023): financial threshold removed, penalties up to
  A$50 million [VERIFY]
- Implied terms: Fair Work Act 2009 — contractor vs. employee distinction; High Court in
  CFMMEU v Personnel Contracting [2022] HCA 1 and ZG Operations v Jamsek [2022] HCA 2
  confirmed primacy of contract terms (with caveats) [VERIFY]

**European Union**
- IP: Copyright transfer may require specifying fields of exploitation (varies by member
  state). Moral rights are often inalienable under civil law systems. Software-specific
  rules apply under Directive 2009/24/EC [VERIFY]
- Data protection: GDPR Art. 28 processor contract requirements are mandatory and non-waivable
  for personal data processing. Standard Contractual Clauses (SCCs) required for data
  transfers outside EEA [VERIFY]
- Liability: Many civil law jurisdictions prohibit excluding liability for intentional
  misconduct (dolus/faute intentionnelle/Vorsatz) or gross negligence [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the direction of the draft or analysis
- The user's side, risk appetite, or business context is needed to classify a finding
- Ambiguity in the engagement scope creates a fork that only the user can resolve
- Multiple valid approaches exist and the user's preference matters

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

**Draft mode:**
- **Engagement brief**: key terms described in natural language (parties, scope, fees, IP, timeline)
- **Term sheet or heads of terms**: agreed commercial terms to convert to contract language
- **Prior draft**: an existing draft to complete or restructure

**Review mode:**
- **File**: PDF, DOCX, or other document
- **URL**: link to the agreement in a CLM, cloud storage, or document system
- **Pasted text**: contract text pasted directly into the conversation

If no input is provided, prompt the user to supply one.

### Step 2: Determine Mode and Side

**⟁ CLARIFY** — Before proceeding, ask:

1. **Mode**: Are you drafting a new services agreement from scratch, or reviewing an
   existing agreement?
   - Options: **Draft from scratch**, **Review and redline an existing draft**, **Complete
     or restructure a partial draft**

2. **Which side are you on?**
   - Options: **Service Provider / Supplier**, **Client / Customer**, **Neutral / Neither
     (advising both parties)**
   - *Why this matters*: The entire analysis and drafting posture flips depending on which
     party you represent. IP defaults, liability caps, and termination rights that protect
     a provider burden a client and vice versa.

3. **Contract structure preference** (Draft mode only):
   - Options: **Fully integrated agreement** (scope embedded in the main body), **Agreement
     + Schedule** (scope and pricing in a schedule), **Agreement + Exhibit / Annex** (terms
     in the body, technical specs as an exhibit)

### Step 3: Gather Engagement Context

**⟁ CLARIFY** — Gather the following context. Skip any already answered by the input:

1. **Engagement type and scope**: What services are being provided?
   - Free text with examples: IT development, management consulting, creative design, research,
     engineering, advisory, outsourced function, training delivery
   - *Why this matters*: Scope definition drives IP clause design (software vs. creative vs.
     advisory output), warranty standard (professional vs. fitness for purpose), and change
     control complexity.

2. **Fee structure**:
   - Options: **Fixed price** (total price for defined scope), **Time and materials** (hourly/
     daily rates plus expenses), **Milestone payments** (payments tied to deliverable acceptance),
     **Retainer** (recurring fee for access to services), **Hybrid** (fixed fee for defined
     deliverables + T&M for extensions)
   - *Why this matters*: Fee structure determines billing mechanics, change order pricing, and
     risk allocation for scope growth.

3. **IP outcome**: Who should own the work product?
   - Options: **Client owns all deliverables** (full assignment, provider retains no rights),
     **Provider retains ownership, grants client a license**, **Client owns deliverables, provider
     retains license to pre-existing tools/methodologies**, **Jointly owned** (unusual — discuss
     drawbacks), **To be determined per category of output**
   - *Why this matters*: IP ownership drives the assignment clause design, license-back scope,
     and moral rights waiver requirements. "Full assignment" is more complex than it appears due
     to jurisdiction-specific formality requirements.

4. **Data protection**: Will the provider process personal data on behalf of the client?
   - Options: **Yes — GDPR/UK GDPR processor relationship applies**, **No — provider does not
     process personal data**, **Uncertain — need to assess the scope**
   - *Why this matters*: A GDPR Article 28 Data Processing Agreement/Addendum is legally
     mandatory where personal data is processed. Absence is a critical compliance gap.

5. **Governing law preference**:
   - Options: **England and Wales**, **US — specify state**, **Australia**, **EU member state —
     specify**, **Other jurisdiction**, **No preference — use the provider's/client's home
     jurisdiction**

6. **Subcontracting**:
   - Options: **Provider may not subcontract without written consent**, **Provider may subcontract
     to approved or named subcontractors**, **Provider may subcontract freely (subject to notice)**
   - *Why this matters*: Subcontracting consent requirements interact with liability (client
     cannot exclude liability for subcontractor acts in some jurisdictions) and security
     obligations (particularly for data processing subcontracts).

If the user provides partial context, proceed with stated assumptions and flag them explicitly
(e.g., "Assuming client-side analysis — let me know if that's wrong and I'll adjust").

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Identify the governing law from the input or the user's answer in Step 3. Then use
**legalcode-mcp** to build a working legal reference file for this engagement.

**Research process:**

1. **Identify the governing law** from the contract or user's answer. If absent or ambiguous:
   - **⟁ CLARIFY** — Flag the absence as a mandatory gap (RED), and ask which jurisdiction
     the user expects to apply.

2. **Search legalcode-mcp** for jurisdiction-relevant authority across these categories:
   - IP assignment and licensing formality requirements (statute and case law)
   - Implied terms for services (professional standard, fitness for purpose)
   - Liability exclusion enforceability (reasonableness, unconscionability, civil law rules)
   - Data protection applicable regime (GDPR, UK GDPR, CCPA, AU Privacy Act, etc.)
   - Contractor/employee classification rules if worker classification is a concern
   - Penalty/liquidated damages doctrine if termination fees are included
   - Mandatory terms that cannot be excluded by agreement

3. **Save results** to `/tmp/legalcode-services-authority.md`. Structure:

   ```markdown
   # Legal Authority Reference — Services Agreement
   ## Governing Law: [Jurisdiction]
   ## Date: [date]

   ### IP Formalities
   - [Statute, provision, formality requirement]

   ### Services Implied Terms
   - [Statute or common law principle]

   ### Liability Exclusion Rules
   - [Statute, case, principle]

   ### Data Protection Regime
   - [Applicable regime, key provisions]

   ### Penalty/LD Doctrine
   - [Case or statute]
   ```

4. Use this reference throughout. Mark all legalcode-mcp-sourced citations VERIFIED in the
   Glass Box audit trail.

**Without legalcode-mcp:**
- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — manual verification required"`
- Focus on structural quality, commercial risk, and workflow rather than legal authority depth

### Step 5: Scope of Services and Deliverables

**This is the foundational clause.** Vague scope generates every other dispute in a services
agreement — from change order battles to acceptance failures to IP ownership uncertainty.

**In Draft mode — draft the scope clause:**

1. **Services description**: Draft a specific, bounded description of the services. Avoid
   "as further described in discussions" or "as mutually agreed." Name the outcome, not just
   the activity.

2. **Deliverables list**: List each discrete deliverable with:
   - Description (what it is, format, medium)
   - Specification reference (where applicable, attach specs as an exhibit)
   - Delivery date or milestone trigger
   - Acceptance procedure reference (cross-reference the acceptance clause)

3. **Exclusions**: Expressly state what is NOT in scope where ambiguity could arise. Exclusions
   prevent scope creep claims.

4. **Dependencies**: State client obligations (data, access, approvals, third-party consents)
   that the provider's delivery schedule depends upon. Include a delay mechanism: if client
   fails to provide, the provider's timeline extends by a corresponding period.

5. **Standards of performance**: Specify the applicable standard:
   - **Professional/reasonable care standard** (default for advisory/consulting — "consistent
     with reasonable professional skill and care")
   - **Specification compliance standard** (for IT delivery with defined specs — "materially
     conforming to the Specification")
   - **Fitness-for-purpose standard** (for bespoke deliverables with defined business purpose)
   - Avoid mixing standards — be explicit about which applies to which deliverable

**In Review mode — assess the scope clause:**

| Element | REQUIRED | Common Gap |
|---------|----------|------------|
| Services bounded and specific | ✓ | Vague "services as agreed" language |
| Deliverables listed with specifications | ✓ | No formal deliverable list |
| Exclusions from scope | Recommended | Scope creep exposure without exclusions |
| Client dependencies and delay mechanics | Recommended | Provider bears all delay risk |
| Performance standard clearly specified | ✓ | Mixed or absent standard |
| Conflict between scope and governing law | RED | Watch for SOW terms conflicting with main body |

**⟁ CLARIFY** — When the scope is ambiguous and it would materially affect IP, acceptance, or
change control, ask:
- "The scope description is broad. Should I draft it narrowly (defined deliverables only, all
  else requires a change order) or broadly (all activities reasonably necessary to achieve the
  stated purpose)? Narrow scope protects the provider; broad scope protects the client."

### Step 6: Fees, Payment, and Audit Rights

**In Draft mode — draft the fee clause:**

**Fixed-price structure:**
```
Fees: The Client shall pay the Provider a fixed fee of [£/$/€ amount] ("Fee") for the
Services, payable as follows:
  - [amount] on execution of this Agreement;
  - [amount] upon acceptance of [Milestone 1/Deliverable X]; and
  - [amount] upon final acceptance of all Deliverables.
```

**Time and Materials structure:**
```
Fees: The Client shall pay the Provider at the rates set out in Schedule [X] ("Rates")
for time spent providing the Services, plus reimbursable expenses in accordance with
Clause [Y]. The Provider shall invoice [monthly / on completion of each milestone], and
invoices shall be accompanied by time records in [daily / weekly] increments.
```

**Key payment provisions to draft or review:**

| Provision | REQUIRED | Guidance |
|-----------|----------|---------|
| Payment terms (e.g., Net 30) | ✓ | Net 30 is market standard for B2B; shorter for smaller providers |
| Late payment interest | Recommended | UK: Late Payment of Commercial Debts Act 1998 (8% over BoE base) [VERIFY]; US: state-specific; AU: courts may imply |
| Disputed invoice procedure | Recommended | "Undisputed amounts paid; disputed amounts notified within [10] days with written reasons" |
| Expenses policy | As applicable | Define pre-approval threshold, categories, and documentation requirements |
| Price escalation (multi-year) | As applicable | CPI/RPI index or fixed annual percentage |
| Audit rights (T&M contracts) | Strongly recommended | Right to audit time records and expenses on [30] days' notice |
| Set-off rights | Negotiate | Client: right to set off against disputed claims; Provider: exclude set-off rights |
| Currency and payment method | ✓ | Specify to avoid FX disputes |
| Taxes / VAT / GST | ✓ | Allocate who bears withholding taxes, sales taxes, VAT/GST |

**In Review mode:**
- Classify each payment provision as GREEN / YELLOW / RED using the Deviation Severity
  Classification section below.
- Flag missing audit rights in T&M contracts as YELLOW.
- Flag absent dispute procedure as YELLOW.
- Flag payment terms of Net 60+ without corresponding interest provisions as YELLOW.

### Step 7: Change Control

**The change control clause prevents scope creep disputes more than any other provision.**
Without it, informal "small changes" accumulate into large uncompensated work.

**Draft a change order mechanism:**

```
Change Control: Either party may request a change to the Services or Deliverables by
submitting a written Change Request in the form set out in [Exhibit/Schedule X] ("Change
Request"). Within [10] Business Days of receipt, the Provider shall submit a Change
Order proposal specifying:
  (a) a description of the proposed changes;
  (b) the impact on Fees (additional, reduced, or neutral);
  (c) the impact on the delivery timeline and any affected Milestones;
  (d) any other material impacts.

No change shall be implemented without a Change Order signed by authorised representatives
of both parties. The Provider is not obliged to implement any change pending execution of
a Change Order. The Provider shall continue performing the existing Services during the
change evaluation period.
```

**Key design decisions:**

| Issue | Provider-Favourable | Client-Favourable |
|-------|--------------------|--------------------|
| Who can initiate a change? | Both parties | Both parties (mutual) |
| Is the provider obliged to implement client-requested changes? | No — at provider's discretion | Yes — mandatory within agreed price range |
| What counts as a "change"? | Any deviation from Specification, however small | Only material changes exceeding [X%] of original scope |
| Impact on timeline | All changes extend timeline by amount in Change Order | Client-requested changes may not extend timeline |
| Oral change prohibition | Express: "No oral changes are effective" | — |
| Rate for additional work | Rates in Schedule [X] | Agreed in each Change Order |

**⟁ CLARIFY** — If the client's team is known to request frequent informal changes, ask:
- "Should I include a de minimis threshold (e.g., changes under [£5,000] or [20 hours] do
  not require a formal Change Order)? This speeds up small changes but creates a habit of
  informal requests."

### Step 8: Acceptance Testing

**Acceptance is the gateway event for both IP transfer and milestone payments.** Without
a defined acceptance procedure, disputes arise over whether deliverables are "accepted" and
whether the provider has earned payment.

**Draft an acceptance procedure:**

```
Acceptance Testing:
(a) On delivery of each Deliverable, the Client shall have [10] Business Days ("Review Period")
    to review the Deliverable against the Acceptance Criteria set out in [Schedule/Exhibit X].

(b) If the Deliverable meets the Acceptance Criteria, the Client shall issue a written
    Acceptance Notice. Acceptance is deemed given if no written rejection is issued within
    the Review Period.

(c) If the Deliverable does not meet the Acceptance Criteria, the Client shall issue a
    written Rejection Notice specifying, in reasonable detail, the defects or non-conformities.
    The Provider shall remedy the defects within [15] Business Days and re-submit the
    Deliverable for re-assessment under this Clause.

(d) If the Provider fails to remedy the defects within [2] re-submission cycles, the Client
    may: (i) accept the Deliverable subject to an agreed price reduction; or (ii) terminate
    the relevant portion of this Agreement under Clause [X].

(e) Partial use of a Deliverable by the Client shall constitute deemed acceptance of that
    Deliverable.
```

**Key design tensions:**

| Element | Provider Priority | Client Priority |
|---------|------------------|----------------|
| Review period length | Shorter (5 BD) | Longer (15-20 BD) |
| Acceptance criteria | Defined spec compliance | Fitness for purpose |
| Deemed acceptance | Include (use = acceptance) | Exclude or narrow |
| Rejection specificity | Client must itemise each defect | General rejection notice sufficient |
| Number of cure cycles | Limited (2 cycles, then terminate) | Unlimited until conforming |
| Partial use = acceptance | Include | Exclude |

### Step 9: Intellectual Property

**IP is the highest-stakes clause in most services agreements.** Poorly drafted IP provisions
are a frequent source of litigation. The core tension: the provider embeds general skills,
methodologies, and tools ("Background IP") into bespoke outputs ("Foreground IP") and may
need to reuse the approach for other clients.

#### Background IP vs. Foreground IP Framework

**Background IP** — IP owned by a party **before** the engagement, or developed independently
of it. Each party retains ownership of its own Background IP.

**Foreground IP** — IP created specifically **for and during** the engagement (the deliverables
and bespoke outputs). The key drafting question is who owns Foreground IP.

**Draft the IP clause:**

```
Intellectual Property:
(a) Background IP. Each party retains all Intellectual Property Rights in its Background IP.
    Nothing in this Agreement assigns or transfers any Background IP.

(b) Foreground IP — [Option A: Full Assignment to Client]:
    The Provider hereby assigns (and, to the extent the assignment is of future copyright,
    agrees to assign) to the Client, with full title guarantee, all Intellectual Property
    Rights in the Deliverables created under this Agreement ("Foreground IP"), effective
    upon payment of all outstanding Fees.

    [Option B: Provider Retains, Grants License]:
    The Provider retains all Intellectual Property Rights in the Deliverables. The Provider
    grants to the Client a [non-exclusive / exclusive], [royalty-free / royalty-bearing],
    perpetual, irrevocable, worldwide licence to use, copy, modify, and exploit the
    Deliverables for the Client's internal business purposes.

    [Option C: Assignment with License-Back]:
    The Provider assigns all Intellectual Property Rights in the Foreground IP to the Client
    [upon payment in full]. The Client grants back to the Provider a non-exclusive, royalty-free,
    worldwide, perpetual licence to use the underlying methodologies, know-how, and non-
    bespoke components for the purposes of providing services to other clients, provided
    that the Provider does not reproduce the Client's Confidential Information.

(c) Provider Tools and Methodologies. The Provider's general methodologies, proprietary
    tools, frameworks, and know-how embedded in the Deliverables ("Provider Tools") are
    Background IP. Where Option A or C applies, the Client receives a licence to use the
    Provider Tools solely to the extent necessary to use and exploit the Deliverables.

(d) Moral Rights. To the extent permitted by applicable law, the Provider waives (and shall
    procure the waiver of) all moral rights in the Deliverables in favour of the Client.
    [JURISDICTION-SPECIFIC: Moral rights are inalienable in many civil law jurisdictions —
    waiver may not be effective. Research the governing law's position.]

(e) Open Source. The Provider shall not incorporate any open source software into the
    Deliverables without prior written consent and shall provide a full inventory of any
    open source components used, including licence terms. [JURISDICTION-SPECIFIC: GPL/AGPL
    copyleft terms may require client to release derivative works — always assess open
    source licence obligations.]

(f) IP Encumbrances. The Provider represents that it has full right, title, and authority
    to assign or license the Foreground IP and that the Deliverables do not infringe any
    third-party Intellectual Property Rights.

(g) Assignment Formalities. The Provider shall, upon request and at the Provider's expense,
    execute all documents and do all acts necessary to perfect the assignment of Foreground
    IP to the Client. [JURISDICTION-SPECIFIC: UK — CDPA 1988 s.90(3) requires written
    signed assignment; AU — Copyright Act 1968 s.196(3); EU — field-of-exploitation
    requirements vary by member state [VERIFY].]
```

**In Review mode — IP assessment checklist:**

| Element | Classification if Absent/Deficient |
|---------|-----------------------------------|
| Background IP ownership preserved | RED (risk of inadvertent assignment) |
| Foreground IP ownership clearly stated | RED (ownership dispute inevitable) |
| Assignment formality compliant with governing law | RED (void assignment risk) |
| License-back for provider tools | YELLOW if provider has no license to reuse methodology |
| Moral rights waiver (where possible) | YELLOW |
| Open source inventory obligation | YELLOW (copyleft taint risk) |
| IP encumbrances representation | YELLOW (infringement indemnity without this is hollow) |
| Feedback clause (does client grant IP in feedback?) | YELLOW if broad |

**⟁ CLARIFY** — If the client wants full ownership but the provider has proprietary tools, ask:
- "Should the provider retain a license-back to reuse their methodologies (Option C) rather
  than a full assignment without license-back? Full assignment without license-back prevents
  the provider from applying learned knowledge to future clients, which is commercially
  unusual and typically results in a higher price."

### Step 10: Warranties, Liability, and Indemnities

#### Warranties

**Draft a warranties clause:**

```
Warranties:
(a) Provider Warranties. The Provider warrants that:
    (i)  [Professional standard:] the Services will be performed with reasonable skill and
         care and to a professional standard consistent with good industry practice;
    (ii) [Specification compliance:] each Deliverable will materially conform to the
         Specification as at the date of delivery;
    (iii) [Non-infringement:] the Deliverables do not, as delivered, infringe any third-party
          Intellectual Property Rights;
    (iv) [Compliance:] the Provider will comply with all applicable laws and regulations
         in the performance of the Services;
    (v)  [Authority:] the Provider has full authority to enter into and perform this Agreement.

(b) Warranty Period. The Provider's warranty obligations in Clause (a)(ii) apply for
    [60/90] days following acceptance of the relevant Deliverable ("Warranty Period").
    During the Warranty Period, the Provider shall remedy any material non-conformity
    at its own cost within [15] Business Days of written notification.

(c) Warranty Disclaimer. EXCEPT AS EXPRESSLY SET OUT IN THIS AGREEMENT, AND TO THE
    FULLEST EXTENT PERMITTED BY APPLICABLE LAW, THE PROVIDER MAKES NO WARRANTIES,
    WHETHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTY OF FITNESS FOR A
    PARTICULAR PURPOSE OR SATISFACTORY QUALITY.
    [JURISDICTION-SPECIFIC: UK — Consumer Rights Act 2015 and Supply of Goods and Services
    Act 1982 (now superseded for consumers) imply terms of reasonable care and skill. Some
    implied terms cannot be excluded in B2B contracts. UCTA 1977 applies to B2B exclusions
    of implied terms. [VERIFY]]
```

#### Limitation of Liability

**The single most commercially negotiated clause.** Draft starting positions:

```
Limitation of Liability:
(a) Cap. Each party's total aggregate liability to the other under or in connection with
    this Agreement, whether arising in contract, tort (including negligence), breach of
    statutory duty, or otherwise, shall not exceed [the greater of (i) the total Fees
    paid or payable in the [12] months immediately preceding the event giving rise to the
    claim, or (ii) [£/$/€ [X]]].

(b) Consequential Loss Exclusion. Neither party shall be liable to the other for any:
    (i)  loss of profits;
    (ii) loss of revenue or business;
    (iii) loss of anticipated savings;
    (iv) loss of goodwill;
    (v)  loss of data; or
    (vi) indirect or consequential loss,
    in each case, whether or not advised of the possibility of such loss.

(c) Carveouts. Clauses (a) and (b) shall not apply to:
    (i)  death or personal injury caused by negligence;
    (ii) fraud or fraudulent misrepresentation;
    (iii) [the indemnification obligations in Clause [X] (IP infringement)];
    (iv) [any wilful default or gross negligence]; and
    (v)  any other liability that cannot be limited by applicable law.
    [JURISDICTION-SPECIFIC: UK — UCTA 1977 s.2(1) voids exclusion of death/personal injury
    caused by negligence. UCTA s.2(2) requires reasonableness test for negligence exclusions.
    Civil law — intentional misconduct (dolus) and gross negligence (culpa lata) cannot be
    excluded in many jurisdictions [VERIFY].]
```

**Liability cap benchmarks (professional services):**

| Cap Level | Characterisation | Typical Context |
|-----------|-----------------|-----------------|
| < 6 months' fees | AGGRESSIVE (provider) | Consumer-facing or low-margin services |
| 6–12 months' fees | Provider-standard | Mid-market B2B professional services |
| 12 months' fees | Market standard | Most B2B services agreements |
| > 12 months' fees | Client-favourable | High-value, high-risk, regulated sector |
| Uncapped specific heads | Unusual | IP infringement, fraud, data breach |

**In Review mode:**

| Issue | Classification |
|-------|---------------|
| No liability cap | RED — escalate |
| Cap below 6 months' fees with no justification | RED |
| Cap between 6-12 months | YELLOW — negotiate to 12 months |
| No consequential damages exclusion for one party | YELLOW |
| Carveouts that effectively eliminate the cap | YELLOW-RED (assess scope) |
| No death/personal injury carveout | RED — void in many jurisdictions |
| Asymmetric cap (provider capped, client uncapped) | YELLOW |

#### Indemnification

**Draft the indemnification clause:**

```
Indemnification:
(a) IP Indemnity. The Provider shall indemnify, defend, and hold harmless the Client from
    any third-party claims, losses, damages, and costs (including reasonable legal fees)
    arising from any allegation that the Deliverables, as delivered and used in accordance
    with this Agreement, infringe any third-party Intellectual Property Rights, provided that:
    (i)  the Client promptly notifies the Provider in writing of the claim;
    (ii) the Provider has sole control of the defence and settlement; and
    (iii) the Client provides reasonable assistance at the Provider's expense.

(b) IP Indemnity Remedies. If the Deliverables are, or may be, the subject of an IP claim,
    the Provider may (at its discretion and expense): (i) procure the right to continued
    use; (ii) modify the Deliverables to be non-infringing; or (iii) replace the Deliverables
    with a non-infringing equivalent. If none of the foregoing is commercially practicable,
    either party may terminate the Agreement on written notice, with a pro-rata fee refund.

(c) Data Protection Indemnity. Each party shall indemnify the other for losses arising from
    its breach of the Data Protection obligations in Clause [X] (Data Protection), subject
    to the liability cap in Clause [Y].

(d) Provider Gross Negligence / Wilful Misconduct. [Optional/negotiated:] The Provider shall
    indemnify the Client from third-party claims arising from the Provider's gross negligence
    or wilful misconduct in the performance of the Services.

(e) Client Indemnity. The Client shall indemnify, defend, and hold harmless the Provider from
    any third-party claims arising from the Client's Materials, the Client's acts or omissions,
    or the Client's use of the Deliverables in a manner not permitted by this Agreement.
```

**In Review mode — indemnification assessment:**

| Element | Issue if Absent or Deficient |
|---------|------------------------------|
| IP infringement indemnity | YELLOW — IP exposure uninsured |
| Defence control right | YELLOW — provider/client exposed to uncontrolled settlement |
| IP remedies waterfall (procure / modify / replace) | YELLOW — no resolution path if infringement found |
| Sole remedy language for IP indemnity | Negotiate — limits other breach claims |
| Data breach indemnity | YELLOW if GDPR applies |
| Mutual vs. unilateral indemnity | Flag asymmetry as YELLOW |

### Step 11: Data Protection, Compliance, and Subcontracting

#### Data Protection

**⟁ CLARIFY** — Confirm whether personal data is processed:
- "Confirm: will the provider access or process any personal data (e.g., employee records,
  customer data, health data) on behalf of the client under this engagement? If yes, a Data
  Processing Agreement or Addendum is legally required under GDPR/UK GDPR."

**Draft the data protection clause:**

```
Data Protection:
(a) Compliance. Each party shall comply with all applicable data protection and privacy
    legislation, including (where applicable) the UK GDPR, the EU GDPR (Regulation (EU)
    2016/679), the Data Protection Act 2018, and any successor legislation.

(b) DPA Requirement. Where the Provider processes Personal Data as a Processor on behalf
    of the Client as Controller, the parties shall enter into a Data Processing Agreement
    ("DPA") in the form set out in Schedule [X] (or such other form as the parties may agree)
    before any Personal Data is processed. The DPA shall comply with the requirements of
    Article 28 GDPR [VERIFY].

(c) Sub-Processors. The Provider shall not engage any sub-processor to process Personal
    Data without the Client's prior written consent (or, where the Client provides general
    authorisation, prior notice of at least [30] days). The Provider shall impose data
    protection obligations on sub-processors equivalent to those imposed on the Provider
    under this Agreement.

(d) Data Security. The Provider shall implement and maintain technical and organisational
    measures appropriate to the risk to protect Personal Data, including measures against
    accidental or unauthorised destruction, loss, alteration, or disclosure.

(e) Breach Notification. The Provider shall notify the Client without undue delay (and in
    any event within [24/48] hours) upon becoming aware of any Personal Data breach and
    shall provide the Client with sufficient information to meet its notification obligations
    to supervisory authorities.
    [JURISDICTION-SPECIFIC: GDPR/UK GDPR — 72-hour notification obligation to supervisory
    authority. ICO in the UK; lead authority under GDPR one-stop-shop mechanism [VERIFY].]

(f) Return/Deletion. Upon termination, the Provider shall, at the Client's election, return
    all Personal Data in a portable format or securely delete it within [30] days and provide
    written confirmation of deletion.
```

**[JURISDICTION-SPECIFIC — EU Financial Services] DORA Compliance (effective 17 January 2025):**
The EU Digital Operational Resilience Act (DORA, Regulation (EU) 2022/2554) mandates specific
contractual provisions in all ICT third-party service agreements where the client is a regulated
financial entity (banks, insurers, investment firms, crypto-asset service providers, CCPs, etc.).
The DPA clause alone is insufficient — DORA requires the contract itself to address [VERIFY]:
- Full description of all ICT services, data locations (country of processing and storage),
  and data classification
- ICT incident reporting obligations and minimum notification timelines
- Audit and access rights for the financial entity, its competent authorities, and ESAs
- Termination rights triggered by the provider's material ICT failure
- Exit strategies and transition assistance provisions (minimum 12-month lock-in of rates and obligations)
- Business continuity and disaster recovery co-operation obligations
- Sub-ICT service provider controls with equivalent flow-down

For IT or data services agreements with EU financial entities governed by DORA, run a dedicated
DORA contractual compliance review before finalising any data protection, audit, termination,
or transition clause.

#### Subcontracting

```
Subcontracting:
(a) The Provider shall not subcontract any part of the Services without the Client's
    prior written consent (not to be unreasonably withheld or delayed).

(b) Approved Subcontractors. The parties agree that the Provider may engage the
    subcontractors listed in Schedule [X] ("Approved Subcontractors") without further
    consent.

(c) Flow-Down. The Provider shall impose on each subcontractor obligations consistent
    with those imposed on the Provider under this Agreement, including (without limitation)
    confidentiality, IP assignment, data protection, and compliance obligations.

(d) Liability. The Provider shall remain fully responsible for the acts and omissions of
    its subcontractors as if they were its own acts and omissions.
```

#### Compliance Provisions

**For cross-border or regulated engagements, include:**

```
Compliance:
(a) Each party shall comply with all applicable laws and regulations, including:
    (i)   anti-bribery and corruption laws (including, where applicable, the UK Bribery
          Act 2010 and the US Foreign Corrupt Practices Act) [VERIFY];
    (ii)  applicable sanctions and export control regimes;
    (iii) modern slavery legislation (including, where applicable, the Modern Slavery Act
          2015 (UK)) [VERIFY];
    (iv)  applicable employment and labour laws; and
    (v)   applicable data protection laws.

(b) Each party shall promptly notify the other of any actual or suspected breach of this
    Clause and shall cooperate with any resulting investigation.
```

### Step 12: Termination and Transition

#### Term and Termination

**Draft the term and termination clause:**

```
Term:
This Agreement shall commence on [date] ("Effective Date") and, unless terminated earlier
in accordance with this Clause, shall continue until [completion date / acceptance of all
Deliverables / [date]] ("Term").

Termination for Cause:
Either party may terminate this Agreement with immediate effect by written notice if the
other party:
(a) commits a material breach and fails to remedy the breach within [30] Business Days of
    written notice specifying the breach in reasonable detail; or
(b) becomes insolvent, enters administration, receivership, or liquidation (other than for
    solvent reorganisation), or makes an arrangement with creditors; or
(c) suspends or ceases to carry on a material part of its business.

[Provider additional trigger:] The Provider may terminate immediately if the Client fails
to pay any undisputed invoice within [30] days of its due date following a written payment
notice.

Termination for Convenience:
[Option A — Provider only:] The Client may terminate this Agreement for convenience on
[60] days' written notice, subject to payment of all Fees for Services performed up to
the termination date plus reasonable demobilisation costs.

[Option B — Either party:] Either party may terminate this Agreement for convenience on
[60] days' written notice. [If Client terminates:] the Client shall pay all Fees for
Services performed, plus [a cancellation fee of [X]% of the remaining Fees / reasonable
demobilisation costs.]

Effects of Termination:
On termination or expiry:
(a) the Client shall pay all Fees outstanding for Services performed to the date of termination;
(b) each party shall return or destroy the other's Confidential Information;
(c) the following provisions shall survive termination: [Confidentiality, IP, Limitation
    of Liability, Data Protection, Indemnification, Governing Law, Survival].
```

**Termination issue analysis:**

| Issue | Provider Position | Client Position |
|-------|------------------|----------------|
| Termination for convenience: available? | No (or limited) | Yes — unrestricted |
| Notice period | 90+ days | 30 days |
| Fees on termination for convenience | Fees + cancellation fee | Fees pro-rated only |
| Cure period for breach | Long (30 BD) | Short (10 BD) or none |
| Insolvency trigger | Immediate | Cross-default from other agreements |

**In Review mode — key classification triggers:**

| Issue | Classification |
|-------|---------------|
| No termination for convenience in long-term engagement | YELLOW |
| Termination fees disproportionate to actual losses | YELLOW (penalty doctrine risk) |
| No insolvency termination trigger | YELLOW |
| No cure period for breach | YELLOW (unfair surprise risk) |
| Termination triggers payment of unearned fees | RED |

[JURISDICTION-SPECIFIC — UK] **Corporate Insolvency and Governance Act 2020 (CIGA 2020):**
Since CIGA 2020, **ipso facto clauses** — contract terms that allow termination or modification
of services solely because a counterparty has entered a formal insolvency process — are
**restricted for essential supplier relationships** in England and Wales. A provider cannot
terminate or withhold supply to an insolvent client solely because of the insolvency event;
an application to court is required for permission. CIGA 2020 s.14 and Schedule 4. This is
a significant departure from pre-2020 drafting practice. Review termination for insolvency
clauses in UK-governed agreements carefully — a clause that is valid for a non-essential
supplier may be unenforceable for an essential one. [VERIFY]

#### Transition Assistance

```
Transition Assistance:
Following notice of termination or expiry, the Provider shall, for a period of [90] days
(or such longer period as the parties may agree) ("Transition Period"):
(a) cooperate with the Client and any successor provider in the orderly transfer of
    the Services and Deliverables;
(b) provide the Client with copies of all work product, documentation, data, and materials
    required to continue the Services;
(c) provide [up to X hours per month of] transition assistance at [the Rates in Schedule X /
    no additional charge]; and
(d) not take any action designed to impair or delay the transfer.

The Provider's obligations under this Clause shall survive termination for the duration
of the Transition Period.
```

**Transition rate lock:** During the Transition Period, the Provider shall not increase the
Rates or introduce new charges. Clause should expressly freeze rates at pre-termination levels
to prevent artificial fee inflation when the client has no alternative provider.

**[JURISDICTION-SPECIFIC — UK] TUPE:**
Where services are transferred from one provider to another (or brought back in-house), the
Transfer of Undertakings (Protection of Employment) Regulations 2006 (TUPE) may automatically
transfer the employment of the provider's staff who were dedicated to the engagement to the
incoming provider or the client. TUPE obligations are non-waivable and arise by operation of
law. Services agreements should:
- Require the outgoing provider to promptly disclose the identity, terms, and employment
  information of all assigned employees (under TUPE reg. 11)
- Allocate TUPE liability (for ETO reasons, unfair dismissal, and any pre-transfer liabilities)
  between outgoing provider and incoming provider
- Address employee liability indemnities in the transition provisions
Equivalent obligations arise under the EU Acquired Rights Directive (2001/23/EC) across EU
member states. [VERIFY]

### Step 13: Review Additional Provisions

For the following standard provisions, apply a checklist review:

**Confidentiality**
- [ ] Scope of Confidential Information defined and reasonable
- [ ] Term: typically 2-5 years post-termination (indefinite for trade secrets)
- [ ] Standard carveouts: public domain, independent development, required by law
- [ ] Return or destruction on termination
- [ ] Permitted disclosures (affiliates, advisors, under NDA)

**Insurance**
- [ ] Professional Indemnity (Errors & Omissions): typically £/$/€1M per claim
- [ ] Public / General Liability: typically £/$/€2M per occurrence
- [ ] Cyber / Data and Privacy Liability: £/$/€1M or higher where data is processed
- [ ] Workers' Compensation / Employers' Liability: as required by law
- [ ] Evidence of coverage (certificates on request)

**Assignment**
- [ ] Neither party may assign without the other's written consent
- [ ] Change-of-control provisions addressed (acquisition of provider = deemed assignment?)
- [ ] Exceptions for affiliate transfers and corporate reorganisations
- [ ] Assignment of benefit (receivables assignment) permitted

**Force Majeure**
- [ ] Events specifically enumerated (not just "acts of God")
- [ ] Notification and mitigation obligations
- [ ] Duration threshold for termination rights (typically 60-90 days)
- [ ] Pandemic/epidemic explicitly addressed (post-2020 standard)

**Governing Law and Disputes**
- [ ] Governing law clause present and unambiguous
- [ ] Dispute resolution: escalation to senior management, then arbitration or litigation
- [ ] Venue and jurisdiction clear
- [ ] Arbitration institution, rules, seat specified (if arbitration)
- [ ] No jurisdiction that is unusual or impractical for both parties

**Boilerplate (Definitions and General)**
- [ ] Key defined terms consistent throughout
- [ ] Entire agreement / integration clause (prevents reliance on pre-contract statements)
- [ ] Severability (preserves agreement if one clause void)
- [ ] No implied waiver (failure to enforce is not waiver)
- [ ] Order of precedence (if main body conflicts with schedules)
- [ ] Notices clause (method, address, deemed receipt)
- [ ] Amendment in writing only
- [ ] Counterparts and electronic execution

**⟁ CLARIFY** — For provisions where the governing law has specific requirements that are
not clear from the input, ask the user to confirm the applicable jurisdiction before
classifying.

### Step 14: Quality Verification

Before delivering output, run the following checks:

1. **Citation Quality Gates**: Run all 5 gates silently. Revise failures before delivery.
2. **Self-Interrogation**: For every RED item, run the 3-pass self-interrogation. Revise
   if any pass reveals a weakness.
3. **Completeness check**: Confirm all 18 clause categories addressed (drafted or flagged
   as absent).
4. **IP formality check**: Verify the assignment language is valid under the stated governing
   law (or marked [VERIFY] if uncertain).
5. **GDPR compliance check**: If personal data is processed, confirm DPA obligation flagged.
6. **Confidence Scoring**: Assign confidence levels to all material clause analyses.
7. **Glass Box**: Generate the Glass Box audit trail.

---

## Services Agreement Clause Architecture

A complete standalone services agreement covers these 18 clause categories:

| # | Clause Category | Depth | Key Issues |
|---|----------------|-------|-----------|
| 1 | Scope of Services and Deliverables | **Deep** | Specification completeness, exclusions, dependencies, performance standard |
| 2 | Change Control | **Deep** | Change order mechanism, oral change prohibition, timeline impact |
| 3 | Fees and Payment | **Deep** | Structure (fixed/T&M/milestone), payment terms, late interest, audit rights |
| 4 | Acceptance Testing | **Deep** | Criteria, review period, deemed acceptance, cure cycles, partial use |
| 5 | Intellectual Property | **Deep** | Background/foreground split, assignment formalities, license-back, moral rights, open source |
| 6 | Warranties | **Deep** | Professional standard vs. spec compliance, warranty period, disclaimer, implied terms |
| 7 | Limitation of Liability | **Deep** | Cap level, carveouts, consequential damages exclusion, jurisdiction enforceability |
| 8 | Indemnification | **Deep** | IP, data breach, negligence, procedure, settlement control |
| 9 | Data Protection | **Deep** | DPA obligation, Art. 28 compliance, sub-processors, breach notification, deletion |
| 10 | Subcontracting | Standard | Consent, approved list, flow-down, provider retains liability |
| 11 | Term and Termination | Standard | Cause, cure period, convenience, insolvency, effects |
| 12 | Transition Assistance | Standard | Duration, cooperation obligations, data/documentation transfer |
| 13 | Confidentiality | Standard | Scope, term, carveouts, return/destroy |
| 14 | Insurance | Standard | PI/E&O, public liability, cyber, evidence of coverage |
| 15 | Compliance | Standard | Anti-bribery, sanctions, modern slavery, audit rights |
| 16 | Assignment | Standard | Consent, change of control, affiliate exceptions |
| 17 | Governing Law and Disputes | Standard | Choice of law, escalation, arbitration/litigation |
| 18 | Definitions and Boilerplate | Standard | Entire agreement, severability, notices, amendment, order of precedence |

---

## Deviation Severity Classification

### Drafting Mode — Clause Classification

| Status | Meaning | Action |
|--------|---------|--------|
| **REQUIRED** | Essential for an enforceable, market-standard services agreement | Draft; cannot be omitted |
| **RECOMMENDED** | Strongly advisable; absence creates meaningful risk | Draft; explain risk if omitted |
| **OPTIONAL** | Useful in specific contexts; not universally needed | Include if applicable; explain when |

### Review Mode — Deviation Classification

#### GREEN — Acceptable
Clause aligns with or exceeds the standard position. No negotiation needed.

**Examples:**
- Liability cap at 18 months' fees (better than 12-month market standard)
- Confidentiality term of 5 years (longer than 3-year standard — favours receiving party)
- Mutual termination for convenience with 60-day notice

#### YELLOW — Negotiate
Outside standard position but negotiable. Generate specific redlines with fallback positions.

**Examples:**
- Liability cap at 6 months' fees (below market — negotiate to 12)
- No audit rights in T&M contract (missing standard protection)
- Acceptance deemed given after 5 Business Days (shorter than market 10-15 BD)
- IP assignment without assignment formality language (void in UK without written assignment)

#### RED — Escalate
Outside acceptable range; requires senior counsel review or decision-maker sign-off.

**Examples:**
- No limitation of liability clause
- Foreground IP assigned to provider (client gets no ownership of bespoke deliverables)
- No DPA offered when personal data is clearly being processed
- Oral change control provision (renders all scope protections ineffective)
- Scope clause so vague that deliverables cannot be identified
- Fee clause that entitles provider to fees without delivering any identified work product

---

## Redline Format

For each YELLOW or RED finding:

```
**Clause**: [Section reference and clause name]
**Current language**: "[exact quote or description]"
**Issue**: [what is wrong and why]
**Proposed redline**: "[specific alternative language ready to insert]"
**Rationale**: [1-2 sentences, professional, suitable for external sharing]
**Legal basis**: [Relevant statute, regulation, or principle — or "General commercial practice"]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative position if the primary redline is rejected]
**Confidence**: [Definite / High / Probable / Possible]
```

---

## Negotiation Priority Framework

### Tier 1 — Must-Haves (Deal-Level Issues)

Items where the agreement cannot proceed without resolution:
- Absence of any liability limitation (risk of catastrophic exposure)
- IP ownership provisions that assign client's pre-existing IP to the provider
- Absence of a DPA where GDPR-regulated data is processed
- Assignment of future IP without formality compliance (void under governing law)
- Scope clause that cannot identify what the provider is actually obliged to deliver
- Missing or oral change control (every change becomes a dispute)
- Terms void or unenforceable under the governing law

### Tier 2 — Should-Haves (Material Preferences)

Items that materially affect risk but have negotiation room:
- Liability cap amount adjustment (6 months → 12 months)
- Consequential damages exclusion scope and carveouts
- Acceptance testing timelines and deemed acceptance triggers
- IP license-back scope and exclusivity
- Subcontracting consent requirements
- Termination for convenience availability and notice period
- Warranty period duration and standard

### Tier 3 — Nice-to-Haves (Concession Candidates)

Items that improve the position but can be conceded strategically:
- Insurance coverage minimums (within reasonable range)
- Expense pre-approval thresholds
- Governing law preferences (where the alternative is acceptable)
- Notice period preferences (within market range)
- Boilerplate refinements
- Minor definitional improvements

**Strategy**: Lead with Tier 1 items. Trade Tier 3 concessions to secure Tier 2 wins. Never
concede Tier 1 without escalation to senior counsel or decision-maker.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every legal claim cites a specific statute, regulation, or established principle | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format** | All citations follow a consistent, recognisable format for the jurisdiction | Fix format |
| **Currency** | Every cited provision checked for amendments or repeal | Flag "[CHECK CURRENCY — may have been amended]" |
| **Domain** | Analysis stays within the contract's governing law. No bleed from other jurisdictions | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated, not hidden | Add confidence qualifier |

### Self-Interrogation for RED Items

For any finding classified as RED, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity:**
- Does the risk assessment follow logically from the statute or principle cited?
- Would a court or regulator in this jurisdiction actually reach this conclusion on these facts?
- What counter-argument will the counterparty's counsel make?

**Pass 2 — Completeness:**
- Have all relevant statutes, regulations, and principles been considered?
- Are there regulatory dimensions not yet addressed (data protection, employment law, sector
  regulation)?
- Has the interaction with other clauses been assessed (e.g., uncapped indemnity partially
  mitigated by limitation clause)?

**Pass 3 — Challenge:**
- What is the strongest argument that this provision IS acceptable?
- Under what commercial circumstances might a reasonable lawyer accept this risk?
- Is the RED classification proportionate, or is this actually a YELLOW with mitigants?

If any pass reveals a weakness, revise the analysis before delivery. Mark the audit trail
with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material clause analysis, assign a confidence level:

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95-1.0 | Settled law, clear statute, no ambiguity | State with confidence |
| **High** | 0.80-0.94 | Strong authority, minor interpretation questions | State with brief caveat |
| **Probable** | 0.60-0.79 | Good arguments but reasonable minds could differ | State with explicit reasoning and contra-indicators |
| **Possible** | 0.40-0.59 | Genuinely uncertain, competing authorities | Flag for counsel review with both sides |
| **Unlikely** | 0.0-0.39 | Weak basis, speculative | Do not assert; flag as "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every output MUST include a Glass Box audit section at the end:

```yaml
glass_box:
  skill_name: "legalcode-services-agreement-drafter"
  mode: "[Draft from scratch / Review and redline / Complete partial draft]"
  engagement_type: "[Consulting / IT delivery / Creative / Advisory / Research / Engineering / Other]"
  user_side: "[Service Provider / Client / Neutral]"
  governing_law: "[Jurisdiction identified or specified]"
  fee_structure: "[Fixed-price / T&M / Milestone / Retainer / Hybrid]"
  ip_outcome: "[Full assignment / Provider license / Assignment + license-back / Joint / TBD]"
  personal_data_processed: "[Yes / No / Uncertain]"
  dpa_required: "[Yes / No / Uncertain]"
  legalcode_mcp: "[Connected / Not connected — manual verification required]"
  authority_reference_file: "[/tmp/legalcode-services-authority.md / Not created]"
  clauses_reviewed_or_drafted: 18
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  statutes_consulted:
    - "[Statute 1 — VERIFIED (legalcode-mcp) or UNVERIFIED]"
    - "[Statute 2 — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  red_items: "[number]"
  yellow_items: "[number]"
  self_interrogation: "[PASS / REVISED / NOT APPLICABLE (no RED items)]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "[Scope limitations, assumptions, caveats]"
  reviewer: "AI-assisted — requires qualified legal review"
```

---

## Multi-Stakeholder Mapping

Identify ALL affected stakeholders — not just the two contracting parties:

| Stakeholder | Role | Affected Clauses | Impact | Action Required |
|-------------|------|-----------------|--------|-----------------|
| Service Provider | Primary party | All | Commercial and legal obligations | Negotiate / sign |
| Client | Primary party | All | Commercial and legal obligations | Negotiate / sign |
| Provider's employees / contractors | Performing work | IP, confidentiality | Indirect | Ensure employment / contractor agreements include IP assignment and confidentiality flow-down |
| Subcontractors | Performing subset of work | Subcontracting, IP, data protection | Indirect | Flow-down agreements required |
| Data subjects | If personal data processed | Data protection | Indirect | DPA required; GDPR Art. 28 compliance |
| Supervisory authority | If GDPR applies | Data protection | Regulatory | Breach notification obligations |
| Third-party IP holders | If open source or licensed IP used | IP | Indirect | Open source audit; licence compliance |
| Successor provider | On termination | Transition assistance | Indirect | Transition cooperation obligations |

---

## Anti-Patterns

Explicit catalogue of what NOT to do when drafting or reviewing services agreements:

1. **Vague scope as a "flexibility" strategy** — Deliberately vague scope descriptions favour
   neither party in practice: they generate disputes, scope creep claims, and acceptance
   failures. A well-defined scope benefits both parties by setting clear expectations.

2. **Omitting the change control clause entirely** — Without change control, every informal
   client request becomes a potential variation claim. "We just need to be flexible" is the
   most common reason agreements without change control lead to fee disputes.

3. **Confusing professional standard with specification compliance** — "Reasonable skill and
   care" means the provider performs like a competent professional; it does not guarantee
   the deliverable meets any particular technical specification. These are different standards
   and must not be conflated or left ambiguous.

4. **Relying on "work-for-hire" language in all jurisdictions** — Work-for-hire is a US
   doctrine that applies only to specific categories of specially commissioned works where
   the parties agree in writing. It does not exist in England, Australia, or most civil law
   systems. A UK or Australian services agreement relying only on "work-for-hire" language
   will not validly transfer copyright [VERIFY].

5. **Omitting the assignment formality clause** — Saying "the client owns all IP" without
   complying with jurisdiction-specific formality requirements for copyright, patent, or
   design right assignment produces an unenforceable transfer. Draft both the substantive
   assignment and the further-assurances obligation.

6. **Ignoring open source taint** — Permissive open source licences (MIT, Apache 2.0) are
   usually fine. Copyleft licences (GPL, AGPL) may require the client to release derivative
   works under the same licence, which can be commercially catastrophic. Always include an
   obligation to inventory and disclose open source components.

7. **Deemed acceptance without a defined review period** — If the agreement says a deliverable
   is deemed accepted after [X] days, that period must be specified and realistic. "Delivery
   = acceptance" is RED for clients. Absent any acceptance procedure, disputes arise over
   when the provider has earned milestone payments.

8. **Ambiguous aggregate vs. per-claim liability cap language** — *TCS v. DBS Bank Ltd
   [2024] EWHC 1185 (TCC)*: the High Court (Technology and Construction Court) held that
   ambiguous cap language ("aggregate liability...in respect of all other claims...shall in
   no event exceed £10m") constituted a single aggregate cap, not a series of per-claim caps.
   Following TCS v. DBS and earlier Drax cases, English courts now default to aggregate
   interpretation where the language is unclear [VERIFY]. Always state expressly: "a single
   aggregate cap applying cumulatively to all claims" or "a separate cap applies per independent
   claim arising from a separate event." Draft for the result you intend; never rely on
   implication for the cap structure.

9. **Uncapped indemnities alongside a capped liability clause** — An uncapped IP indemnity
   alongside a liability cap of 12 months' fees is commercially incoherent. Determine which
   wins: typically, IP and data breach indemnities are carved out of the general cap, but
   the cap should still apply to the indemnity wherever legally permitted.

10. **Mixing fee structures without clear definitions** — "Fixed-price with T&M for additional
    work" requires defining what is "additional." Without it, the boundary between fixed scope
    and T&M scope is a perennial dispute.

11. **No data protection provision where personal data is obviously in scope** — A developer
    building a customer-facing application, or a consultant reviewing HR files, is a GDPR
    processor. Omitting a DPA is a regulatory compliance failure, not just a commercial gap.

12. **Missing transition assistance obligation** — An agreement that ends without requiring
    the provider to cooperate in handover leaves the client unable to switch providers without
    service disruption. For IT or outsourced services, transition assistance should be a
    specific, timed obligation with defined deliverables.

13. **Moral rights blindness in creative services** — Authors of creative works (designers,
    writers, photographers) may retain moral rights (right of attribution, right of integrity)
    even after copyright assignment. In many civil law systems, moral rights are inalienable.
    Address moral rights explicitly; do not assume they transfer with copyright.

14. **Asymmetric termination for convenience** — A client-only right to terminate for
    convenience with no fee consequence severely disadvantages the provider. A provider who
    has committed resources to an engagement should be compensated for demobilisation costs
    or a reasonable portion of remaining fees.

15. **Oral change control accepted in practice** — Including a written-change-only clause
    while routinely implementing informal verbal instructions creates an argument that the
    parties varied the agreement by conduct. Enforce the clause consistently.

16. **Sub-processor blanket authorisation without notice** — GDPR Article 28(2) allows
    general authorisation but requires the processor to give the controller prior notice of
    new sub-processors. "General authorisation with no notice requirement" violates GDPR.

17. **Omitting the sub-processor flow-down obligation** — The provider remains fully liable
    for sub-processor breaches, but without a contractual obligation to impose matching
    obligations on sub-processors, the provider has no recourse against the sub-processor.

18. **Reviewing limitation clauses without checking jurisdiction-specific enforceability** —
    In England, UCTA 1977 applies a reasonableness test to B2B liability exclusions. In
    France and Germany, exclusions of liability for intentional misconduct are void. The cap
    amount alone does not determine enforceability — the jurisdiction's mandatory rules do.

19. **Treating boilerplate as irrelevant** — Entire agreement clauses, severability, and
    order of precedence can have significant legal consequences. An absent entire agreement
    clause may allow pre-contract representations to create liability. An incorrect order of
    precedence can invert the deal terms if a schedule contradicts the main body.

---

## Localization Notes

When drafting or reviewing under a specific governing law, adjust the analysis as follows:

### England and Wales
- Verify UCTA 1977 reasonableness for all liability exclusions and caps [VERIFY]
- Ensure IP assignment complies with CDPA 1988 s.90(3) (copyright), s.222(3) (design right),
  PA 1977 s.30(6) (patent)
- Exclude third-party rights under Contracts (Rights of Third Parties) Act 1999 unless intentionally granted
- Address IR35/off-payroll working rules if workers are engaged via PSC
- **Liability cap — aggregate vs. per-claim**: Following *TCS v. DBS Bank Ltd [2024] EWHC
  1185 (TCC)*, English courts default to a single aggregate cap where language is ambiguous.
  Draft expressly: "a single aggregate cap applying cumulatively to all claims" or "a separate
  cap applies per independent claim" — do not rely on inference [VERIFY]
- **Consequential loss exclusion — substance over form**: *EE Ltd v. Virgin Mobile Telecoms
  Ltd [2025] EWCA Civ 70* — courts look to the substance of what is excluded, not just the
  label. "Lost charges" characterised as "anticipated profits" were barred by a loss-of-profits
  exclusion. Scope consequential loss exclusions carefully; do not rely on labels alone [VERIFY]
- **Termination for insolvency**: CIGA 2020 restricts ipso facto clauses for essential supplier
  relationships — termination solely on the basis of an insolvency event may be unenforceable
  without a court order. Consider whether the engagement is an "essential supply" [VERIFY]
- TUPE: Transfer of Undertakings (Protection of Employment) Regulations 2006 — where services
  transfer to a new provider or in-house, dedicated employees may automatically transfer. Include
  TUPE information-sharing obligations and liability allocation in transition provisions [VERIFY]
- Late Payment of Commercial Debts Act 1998 implies interest at 8% over BoE base rate [VERIFY]
- Dispute resolution: no jury trials; "loser pays" default costs principle; LCIA/ICC for arbitration

### United States (Federal + State)
- Work-for-hire: confirm the deliverable falls within one of the § 101 specially commissioned categories;
  otherwise, draft an express assignment
- State unconscionability doctrine varies — check the specific state
- Non-compete enforceability: check the specific state (void in California; varying in NY/TX/FL)
- FAA governs arbitration; class action waivers generally enforceable B2B
- UCC Article 2: predominantly services contracts are governed by common law, not UCC [VERIFY]
- State-specific data breach notification laws overlap with any federal obligations

### Australia
- IP assignment must comply with Copyright Act 1968 s.196(3) (copyright) and Patents Act 1990 s.14 (patent)
- Unfair contract terms: ACL small business protections (eff. November 2023) — financial threshold removed
- Privacy Act 1988 and Australian Privacy Principles (APPs) apply if the provider is an APP entity
- Competition and Consumer Act 2010 — implied guarantees for consumer contracts; check if ACL applies

### EU / Civil Law Jurisdictions
- Copyright transfer may require specifying fields of exploitation (varies by member state) [VERIFY]
- Moral rights generally inalienable — waiver language should be narrowly tailored and may not be effective
- Exclusions of liability for intentional misconduct (dolus) or gross negligence are void in many member states [VERIFY]
- GDPR Art. 28 DPA is mandatory and non-waivable; SCCs required for EEA → third-country data transfers

---

## Writing Standards

Apply plain-language discipline to all output:

**For draft contract language:**
- Precise and unambiguous — every defined term used consistently
- Active voice where contract interpretation requires clarity about who bears the obligation
- Short sentences — one obligation or condition per sentence
- Define before using — capitalise all defined terms; include a Definitions clause
- No "shall" vs. "will" inconsistency — pick one and use throughout (UK practice: "shall";
  US practice: "will" or "shall")
- Positive obligations before exceptions — state what must happen before carving out what does not

**For analysis and redlines:**
- Plain language, no jargon or filler
- Active voice: "The clause excludes the provider's liability for negligence" not "Liability
  for negligence is excluded by the clause"
- Short sentences, one point per sentence
- Name the actor: "The client must notify..." not "Notification is required..."
- Specific, not vague: cite the clause reference and the specific issue

**Quality gates before delivery:**
1. Can a non-lawyer business owner understand the scope, fees, and IP outcome from the draft?
2. Can the counterparty's counsel understand and respond to each redline?
3. Is every legal claim backed by a specific citation or flagged [VERIFY]?
4. Are any phrases vague, hedging, or ambiguous? If yes, fix.
5. Could any sentence be shorter without losing meaning? If yes, shorten.
6. Do all cross-references point to the correct clauses?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**
- In Step 4, search for IP formality requirements, services implied terms, liability exclusion
  rules, and data protection obligations for the governing law
- Save results to `/tmp/legalcode-services-authority.md`
- Cross-reference the authority file throughout clause drafting and analysis
- For RED items, search for case law to support or challenge the classification
- Verify statutory currency (amendments, repeal)
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**
- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — manual verification required"`
- Focus on structural quality, commercial risk, and workflow
- Do not create the local authority reference file

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Services Agreement [Draft / Review] Summary

**Mode**: [Draft / Review]
**Your Side**: [Service Provider / Client / Neutral]
**Engagement**: [Brief description of services]
**Fee Structure**: [Fixed-price / T&M / Milestone / Hybrid]
**IP Outcome**: [Full assignment / License / Assignment + license-back]
**Governing Law**: [Jurisdiction]
**Personal Data**: [Yes / No / Uncertain] — DPA Required: [Yes / No]
**Date**: [date]
**Review Basis**: [Organisational playbook / Market standards]

---

## Key Findings [Review mode] / Key Drafting Decisions [Draft mode]

[Top 3-5 issues or decisions with severity (RED/YELLOW) or classification (REQUIRED/RECOMMENDED)]

---

## Clause-by-Clause Analysis [Review] / Draft Language [Draft]

### [Clause Name] — [GREEN / YELLOW / RED] | [REQUIRED / RECOMMENDED / OPTIONAL] | Confidence: [level]

**Current language / Draft**: [summary or draft text]
**Standard position**: [playbook or market standard]
**Issue / Decision**: [description]
**Business impact**: [practical consequence]
**Redline / Draft language** (if YELLOW/RED or REQUIRED):
> [Specific language]

[Repeat for each clause category]

---

## Negotiation / Drafting Strategy

**Tier 1 (Must-Haves)**: [list]
**Tier 2 (Should-Haves)**: [list]
**Tier 3 (Concession Candidates)**: [list]

**Recommended approach**: [specific strategy]

---

## Stakeholder Impact Map

[Table — see Multi-Stakeholder Mapping section]

---

## Open Issues and Next Steps

[Specific actions, outstanding questions, recommended follow-up]

---

## Glass Box Audit Trail

[YAML audit trail — see Glass Box section]
```

---

## Provenance

Created by Legalcode (2026-03-22). Mode A — new skill created from scratch. Designed as
the standalone-engagement complement to `legalcode-master-services-agreement` (two-tier
MSA/SOW framework). Legal research basis: deep analysis of IP assignment formality
requirements across US (17 U.S.C. § 101, work-for-hire doctrine), UK (CDPA 1988 ss.90-92,
PA 1977 s.30(6)), and AU (Copyright Act 1968 s.196(3), Patents Act 1990 s.14); liability
exclusion enforceability under UCTA 1977 (UK), unconscionability doctrine (US), and civil
law mandatory rules; GDPR Article 28 processor contract requirements; acceptance testing
and deemed-acceptance mechanics from professional services contract practice; change control
design patterns; and the legalcode-contract-review reference standard for all 18 quality
elements (Glass Box, Citation Quality Gates, Self-Interrogation, Confidence Scoring,
Anti-Patterns, Writing Standards, Output Format Template).
