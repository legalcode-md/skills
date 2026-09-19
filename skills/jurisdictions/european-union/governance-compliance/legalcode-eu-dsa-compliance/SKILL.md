---
name: legalcode-eu-dsa-compliance
description: Assess compliance with the EU Digital Services Act (Regulation (EU) 2022/2065, "DSA") for
  any provider of intermediary services, online platforms, or online search engines serving EU users.
  Use when onboarding a new digital service under DSA, conducting a DSA compliance audit, preparing for
  a DSC inspection, responding to an enforcement inquiry, or building a DSA compliance programme from
  scratch.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Assess compliance with the EU Digital Services Act (Regulation (EU) 2022/2065, "DSA") for any provider of intermediary services, online platforms, or online search engines serving EU users. Covers: platform tier classification (basic intermediary / online platform / VLOP / VLOSE), notice-and-action mechanisms (Art. 16), transparency reporting (Arts. 15 and 42), trusted flaggers (Art. 20), online advertising transparency (Arts. 24, 27), dark patterns prohibition (Arts. 25, 39), recommender system transparency (Arts. 26, 38), protection of minors (Art. 28), trader traceability for online marketplaces (Arts. 22, 30), systemic risk assessment (Art. 34), risk mitigation measures (Art. 35), independent third-party auditing (Art. 37), researcher data access (Art. 40), crisis response (Art. 36), Digital Services Coordinator cooperation, enforcement exposure (up to 6% global turnover), and GDPR/DMA interplay. Use when onboarding a new digital service under DSA, conducting a DSA compliance audit, preparing for a DSC inspection, responding to an enforcement inquiry, or building a DSA compliance programme from scratch.


# Legalcode EU Digital Services Act Compliance Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted DSA compliance assessment.
> It does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before reliance. The DSA is a live
> regulatory framework — guidelines, delegated acts, and enforcement decisions are issued
> regularly. Statutory and regulatory references cited from memory carry hallucination risk —
> verify against authoritative sources (EUR-Lex, the European Commission's Digital Services
> Act policy hub, and your Member State's Digital Services Coordinator) before relying on them.

## Purpose and Scope

This skill assesses compliance with Regulation (EU) 2022/2065 (Digital Services Act) for
any provider of intermediary services that serves users in the European Union.

**Covers:**

- Platform tier classification and applicable obligation mapping
- Notice-and-action mechanism (Art. 16) readiness
- Statement of reasons process (Art. 17)
- Internal complaint-handling (Art. 18) and out-of-court dispute settlement (Art. 21)
- Transparency reporting obligations (Arts. 15 and 42)
- Trusted flagger programme (Art. 20)
- Advertising transparency and repository (Arts. 24 and 27)
- Dark patterns prohibition (Arts. 25 and 39)
- Recommender system disclosure and non-profiling options (Arts. 26 and 38)
- Protection of minors (Art. 28)
- Trader traceability for online marketplaces (Arts. 22 and 30)
- VLOP/VLOSE systemic risk assessment (Art. 34) and mitigation (Art. 35)
- Independent third-party auditing (Art. 37)
- Researcher data access (Art. 40)
- Crisis response obligations (Art. 36)
- Legal representative requirement for non-EU providers (Art. 13)
- Enforcement exposure and fine calculation (Art. 52)
- GDPR, DMA, and AI Act interplay
- Remediation prioritisation and DSC cooperation guidance

**Does not:**

- Provide legal advice or replace qualified DSA counsel
- Cover the Digital Markets Act (DMA) gatekeeper obligations (separate skill)
- Assess individual content moderation decisions for legality
- Substitute for independent audit under Art. 37

## Jurisdiction and Governing Law

This is an EU-specific skill. The DSA applies to:

- Any provider of intermediary services offering services to recipients in the EU, regardless
  of where the provider is established (Art. 2(1))
- All three tiers: basic intermediary services, online platforms, and very large online
  platforms/online search engines

**Key regulatory instruments:**

- Regulation (EU) 2022/2065 — main DSA text (full application from 17 February 2024;
  VLOPs/VLOSEs from 25 April 2023 designation date, with 4-month compliance period)
- Commission Delegated Regulation (EU) 2023/1080 — DSA Article 37 audit procedures
- Commission Implementing Regulation (EU) 2023/1092 — transparency reporting templates
- Commission Delegated Regulation on Art. 40 researcher data access (adopted July 2025)
- EDPB Guidelines 3/2025 on the DSA–GDPR interplay (adopted September 2025)
- Commission Guidelines on Art. 28 protection of minors (published July 14, 2025)

[EU-SPECIFIC] The DSA does not harmonise all national intermediary liability rules. Member
State transposing measures, DSC designation orders, and national procedural rules for
enforcement actions may add requirements. Check the DSC of the Member State of establishment
for national implementation instruments.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
provider context, the workflow pauses and asks when:

- The platform tier is ambiguous and determines the entire obligation set
- VLOP/VLOSE designation status is uncertain
- The provider's service architecture spans multiple DSA categories
- Risk tolerance or business context would affect remediation prioritisation

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

### Step 1: Accept the Assessment Scope

Accept the assessment scope in any of these formats:

- **Compliance questionnaire**: Answers to structured questions about service type, user
  counts, content moderation practices, advertising model, etc.
- **Existing compliance documentation**: Internal compliance memos, gap analyses, audit
  reports, or DSC correspondence
- **Service description**: Free-text description of what the service does and how it operates
- **URL or documentation package**: Links to terms of service, privacy policy, transparency
  reports, and content moderation policy

If no information is provided, prompt the user to supply a description of the service and
its approximate monthly active EU user count.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user these questions. Skip any already answered:

1. **Service type**: What does the service do?
   - Options: Search engine, Social media network, App store / software marketplace,
     Online marketplace (goods/services), Video-sharing platform, Messaging platform,
     Cloud hosting / storage, Website hosting, Online advertising intermediary, Other
   - _Why this matters_: Determines the primary DSA obligation cluster. A marketplace
     has trader traceability obligations; a social network has recommender system obligations;
     a search engine has VLOSE-specific obligations.

2. **Monthly active EU users (MAU-EU)**: Approximate count?
   - Options: Under 1 million, 1–10 million, 10–45 million, Over 45 million (potential
     VLOP/VLOSE), Unknown (research needed)
   - _Why this matters_: The 45-million threshold distinguishes online platforms from VLOPs
     and VLOSEs, triggering the most extensive obligations.

3. **Designation status**: Has the service been formally designated as a VLOP or VLOSE by
   the European Commission?
   - Options: Yes — designated (provide date), No — not yet designated, Under investigation
     by the Commission, Unknown
   - _Why this matters_: Designation triggers Chapter III obligations (Arts. 33–43) within
     4 months. Currently designated services include Amazon Store, Apple App Store, Facebook,
     Google Play, Google Maps, Google Shopping, Instagram, LinkedIn, Pinterest, Snap, TikTok,
     Twitter/X, WhatsApp, YouTube, Bing, Google Search, Shein, Temu, and XNXX. [VERIFY
     current list at digital-strategy.ec.europa.eu/en/policies/list-designated-vlops-and-vloses]

4. **Establishment**: Where is the provider legally established?
   - Options: EU Member State (specify), Non-EU (with EU legal representative), Non-EU
     (no legal representative yet), Multiple entities across jurisdictions
   - _Why this matters_: Non-EU providers without an EU establishment must appoint a legal
     representative under Art. 13. The country of establishment determines the competent DSC.

5. **Assessment objective**: What does this assessment need to produce?
   - Options: Initial gap analysis for a new compliance programme, Pre-audit readiness
     review, Response to a DSC information request, Preparation for Commission investigation,
     Annual compliance refresh, Other
   - _Why this matters_: Determines depth of analysis and output format.

6. **Prior compliance work**: Has the service already implemented any DSA compliance measures?
   - Options: No measures in place, Partial measures (list available), Full initial
     programme in place (documentation available), Prior gap analysis exists (share it)
   - _Why this matters_: A gap analysis over existing documentation is more efficient
     than building from scratch; prior work reveals specific risk areas.

If the user provides partial context, proceed with what is available and **state assumptions
explicitly** at the outset of the analysis.

### Step 3: Classify Platform Tier

Apply the DSA's tiered classification framework (Art. 3 definitions):

**Tier 1 — Basic Intermediary Services (Arts. 4–6):**
Mere conduit, caching, and hosting services limited to storage at recipient request with no
distribution to the public.

- Applicable obligations: Arts. 11 (points of contact), 12 (recipient contact point),
  13 (legal representative), 15 (transparency reporting — but micro/small exempt), and
  general prohibitions.

**Tier 2 — Online Platforms (Art. 3(i)):**
Hosting services that **disseminate information to the public** at recipient request.

- Applicable obligations: All Tier 1 obligations, plus Arts. 16–30.
- Key distinction from hosting: the service actively distributes third-party content to
  a wider audience (not just stores it).

**Tier 3 — Very Large Online Platforms / Very Large Online Search Engines (Art. 33):**
Online platforms or search engines with ≥ 45 million average monthly EU recipients that
have been formally designated by the European Commission.

- Applicable obligations: All Tier 2 obligations, plus Arts. 33–43.
- Designation is formal — a service at the threshold does not self-qualify; it is designated.

**Micro/small enterprise exemption (Art. 2(g)):** Services with fewer than 50 employees
and annual turnover below EUR 10 million are exempt from most online-platform-specific
obligations under Arts. 16–28, though basic intermediary obligations (Arts. 11–15) still
apply. [VERIFY current threshold definitions in the DSA implementing regulation.]

**⟁ CLARIFY** — If the service spans multiple categories (e.g., a social media platform
that also hosts a marketplace), ask:

- "Your service appears to operate across multiple DSA categories. Should I assess each
  component separately or treat the integrated service as the higher-obligation tier?"
- "If the marketplace component is separate from the social feed, the obligations may
  differ by module. Do you have separate legal entities or products for each?"

### Step 4: Research Current DSA Authority

Use **legalcode-mcp** to gather current DSA regulatory material for this assessment.

**Research process:**

1. Search for: the DSA full text (Regulation (EU) 2022/2065), relevant delegated and
   implementing regulations, European Commission guidelines applicable to the service type,
   and any enforcement decisions relevant to the platform's category.

2. Save the most relevant results to a local reference file:

   ```
   /tmp/legalcode-dsa-authority.md
   ```

   Structure it as:

   ```markdown
   # DSA Authority Reference — [Service Name]

   ## Assessment Date: [date]

   ### Primary Regulation

   - Regulation (EU) 2022/2065 — [relevant articles]

   ### Implementing / Delegated Acts

   - [Act, article, relevance]

   ### Commission Guidelines

   - [Guideline, date, relevance to this platform type]

   ### Enforcement Decisions

   - [Decision, date, platform, finding, fine if any]

   ### DSC Guidance (Member State of establishment)

   - [DSC, guideline, relevance]
   ```

3. Check the Commission's official VLOP/VLOSE designation list for any recent updates
   (designations, revocations, or threshold reviews).

**⟁ CLARIFY** — If the service is close to the 45-million MAU-EU threshold, ask:

- "The threshold assessment matters for VLOP/VLOSE designation. Does the service have
  data on average monthly active EU recipients under Art. 24(2) counting rules? The DSA
  definition of 'monthly active recipient' may differ from internal product MAU definitions."

**If legalcode-mcp is not connected:**

- Mark all regulatory references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed using general DSA knowledge, flagging that current authority has not been
  independently verified

### Step 5: Obligation Mapping

Based on the platform tier established in Step 3, map the applicable obligations:

**⟁ CLARIFY** — For online marketplaces specifically, confirm:

- "Online marketplaces have specific trader traceability obligations under Arts. 22 and 30.
  Does your service allow third-party traders to sell goods or services to consumers? If yes,
  I'll apply the full marketplace obligation set."

Produce an obligation map in the output:

```
Applicable Obligations for [Service Name] ([Tier])

CATEGORY                          | ARTICLE   | APPLICABLE? | NOTES
----------------------------------|-----------|-------------|------
Points of contact (authorities)   | Art. 11   | YES         |
Points of contact (users)         | Art. 12   | YES         |
Legal representative (non-EU)     | Art. 13   | [IF NON-EU] |
Terms and conditions              | Art. 14   | [IF PLATFORM]|
Transparency reporting            | Art. 15   | YES*        | *Micro/small exempt
Notice-and-action mechanism       | Art. 16   | [IF PLATFORM]|
Statement of reasons              | Art. 17   | [IF PLATFORM]|
Notification of criminal offences | Art. 18   | [IF PLATFORM]|
Internal complaint-handling       | Art. 18-2 | [IF PLATFORM]|
Out-of-court dispute settlement   | Art. 21   | [IF PLATFORM]|
Trader traceability               | Art. 22   | [IF MARKETPLACE]|
Advertising transparency          | Art. 24   | [IF PLATFORM]|
Dark patterns prohibition         | Art. 25   | [IF PLATFORM]|
Recommender system transparency   | Art. 26   | [IF PLATFORM w/recommenders]|
Protection of minors              | Art. 28   | [IF PLATFORM, not micro/small]|
Know Your Business Customer       | Art. 30   | [IF MARKETPLACE]|
VLOP risk assessment              | Art. 34   | [IF VLOP/VLOSE]|
VLOP risk mitigation              | Art. 35   | [IF VLOP/VLOSE]|
Crisis response                   | Art. 36   | [IF VLOP/VLOSE]|
Independent audit                 | Art. 37   | [IF VLOP/VLOSE]|
Non-profiling recommender option  | Art. 38   | [IF VLOP only]|
Enhanced dark patterns (VLOPs)    | Art. 39   | [IF VLOP/VLOSE]|
Researcher data access            | Art. 40   | [IF VLOP/VLOSE]|
Enhanced transparency reporting   | Art. 42   | [IF VLOP/VLOSE]|
```

### Step 6: Compliance Gap Analysis

Assess each applicable obligation systematically. For each, classify the compliance status
using the **Compliance Status Classification** defined below, then generate a finding.

**⟁ CLARIFY** — For large or complex platforms:

- Ask whether to perform a **full-scope assessment** of all applicable obligations or a
  **priority assessment** focused on the highest-risk obligations first.
- For VLOP/VLOSE platforms, Art. 34 systemic risk assessment is always a priority item.

Cover all applicable obligation categories from Step 5. For each, assess:

- Whether the obligation is present, absent, or partially implemented
- Whether the implementation meets the DSA's substantive requirements
- What specific gaps exist and their regulatory risk

Use the **DSA Obligation Reference** section below for detailed assessment criteria.

### Step 7: Risk Scoring and Enforcement Exposure

For each finding, assess:

- **Enforcement risk**: Likelihood of DSC or Commission scrutiny based on recent
  enforcement priorities
- **Fine exposure**: Maximum potential fine under Art. 52 (up to 6% of global annual
  turnover for VLOPs/VLOSEs; DSC fines for non-VLOPs vary by Member State)
- **Reputational risk**: Whether the gap has been the subject of recent enforcement actions
  against peer platforms

Calculate a headline risk score:

```
HIGH RISK:   Art. 34/35 systemic risk failures; notice-and-action mechanism absent;
             advertising targeting minors; dark patterns confirmed by audit
MEDIUM RISK: Transparency report delayed or incomplete; statement of reasons inadequate;
             recommender system not disclosed; trader traceability gaps
LOW RISK:    Minor procedural deficiencies; borderline classification questions; internal
             documentation gaps not yet externally visible
```

### Step 8: Remediation Prioritisation

For each finding, provide a prioritised remediation recommendation. Structure
recommendations by the **Prioritisation Framework** defined below.

**⟁ CLARIFY** — If multiple HIGH RISK items exist and resources are constrained, ask:

- "I've found [N] high-risk compliance gaps. Would you like me to sequence the remediation
  plan by enforcement risk, implementation effort, or both?"
- "For the systemic risk assessment obligation, has your team already done a preliminary
  risk mapping exercise even if not formally documented? This would significantly reduce
  the time to close this gap."

### Step 9: Quality Verification

Before delivering the assessment, run the **Quality Assurance Framework** checks:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every NON-COMPLIANT finding, run the 3-pass Self-Interrogation.
3. Assign a Confidence Score to each material finding.
4. Verify the obligation map against the platform tier.
5. Generate the Glass Box Audit Trail and append it to the output.

### Step 10: Deliver Assessment Report

Deliver the assessment using the **Output Format Template** below.

---

## DSA Obligation Reference

This section defines the substantive compliance criteria for each major DSA obligation.
Use this as the analytical framework for Step 6.

---

### Art. 11 — Points of Contact for Authorities

**Requirement**: All intermediary service providers must designate a single point of contact
for communications from Member State authorities and the Commission (Art. 11(1)).

**Assessment criteria:**

- [ ] Designated point of contact exists
- [ ] Contact information is publicly available and up to date
- [ ] Point of contact is capable of responding in all relevant EU official languages
- [ ] Contact is documented in terms of service or on the service's website

**Common gaps:**

- Generic customer support email used rather than a dedicated regulatory contact
- No language capability for communications from DSCs in non-English Member States
- Contact details not publicly accessible

**Severity if missing**: NON-COMPLIANT — basic administrative obligation, immediately
rectifiable but creates DSC access problems during investigations.

---

### Art. 12 — Points of Contact for Recipients

**Requirement**: Online platforms must enable recipients to communicate directly and rapidly
with the service (Art. 12(1)).

**Assessment criteria:**

- [ ] Accessible point of contact for users (separate from authority contact)
- [ ] Easy to find within the platform interface
- [ ] Capable of handling complaints, inquiries, and notice submissions

**Common gaps:** Buried deep in help centre; chatbot-only response without escalation path.

---

### Art. 13 — Legal Representative (Non-EU Providers)

**Requirement**: Providers established outside the EU that offer services in the EU must
appoint a legal representative in a Member State where they offer services (Art. 13(1)).
The legal representative must have the power to be addressed alongside or instead of the
provider by DSCs, the Board, and the Commission.

**Assessment criteria:**

- [ ] Legal representative appointed (if non-EU provider)
- [ ] Appointment documented and publicly accessible
- [ ] Legal representative mandated to accept enforcement communications
- [ ] DSC of the Member State of establishment notified

**Common gaps:** Appointment not formally documented; representative lacks authority to
accept enforcement service; not notified to the competent DSC.

**Severity if missing**: NON-COMPLIANT — Commission can consider a non-EU provider that
fails to designate a legal representative as offering services in the Member State of the
legal representative for enforcement purposes, compounding exposure.

---

### Art. 14 — Terms and Conditions Transparency

**Requirement**: Providers must include in their terms and conditions:

- Information on restrictions imposed on recipient content (Art. 14(1)(a))
- Information on content moderation policies and procedures (Art. 14(1)(b))
- Any use of algorithmic decision-making (Art. 14(1)(c))
- Out-of-court dispute settlement options (Art. 14(1)(d) — online platforms)

**Assessment criteria:**

- [ ] ToC includes clear description of content restrictions
- [ ] Content moderation policies described in plain language
- [ ] Algorithmic decision-making disclosed in ToC
- [ ] ToC accessible in all languages in which the service is offered

**Common gaps:** Generic references to "community guidelines" without substance; no
description of algorithmic moderation tools; ToC not available in all EU official languages
in which the service operates.

---

### Art. 15 — Transparency Reporting (General)

**Requirement**: Online platforms (not micro/small) must publish annual transparency
reports covering content moderation statistics (Art. 15(1)).

**Assessment criteria:**

- [ ] Transparency report published at least annually
- [ ] Published within 2 months of the end of the reporting period
- [ ] Covers: orders received from authorities (Arts. 9 and 10), notices received under
      Art. 16, internal complaint-handling statistics (Art. 20(4)), use of automated tools
- [ ] Follows Commission's mandatory template (from 1 July 2025 — Implementing Reg.)
- [ ] Published in machine-readable format and submitted to the DSA Transparency Database
      (transparency.dsa.ec.europa.eu)

**Common gaps:** Reports published late; missing mandatory statistical categories; not
submitted to the DSA Transparency Database; templates not used after 1 July 2025 deadline.

**Severity if missing or materially incomplete**: NON-COMPLIANT — transparency reporting
has been a primary enforcement focus (X fined EUR 120M in December 2024 partly for
advertising transparency failures).

---

### Art. 16 — Notice-and-Action Mechanism

**Requirement**: Hosting services must implement mechanisms to allow individuals and entities
to notify them of specific items of information that the notifier considers illegal (Art. 16(1)).

**Assessment criteria:**

- [ ] Mechanism is easy to access and user-friendly
- [ ] Allows electronic submission
- [ ] Notice must contain: (a) sufficiently substantiated explanation of illegality,
      (b) clear indication of electronic location, (c) name and email of notifier (individuals),
      (d) statement of belief in good faith accuracy
- [ ] Service provides confirmation of receipt (Art. 16(4))
- [ ] Service acts on notices expeditiously (Art. 16(5))
- [ ] Service notifies notifier of decision taken and provides statement of reasons (Art. 16(5))
- [ ] Decisions are based on Art. 17 statement-of-reasons criteria
- [ ] Statistics reported in transparency report

**Common gaps:**

- Generic "report content" buttons that do not collect the Art. 16(2) required fields
- No confirmation of receipt sent to notifiers
- Decisions taken without notifying the notifier of the outcome
- No differentiated workflow for authority notices vs. individual notices

**Severity if missing**: NON-COMPLIANT — core systemic obligation; enforcement focus for
the Commission and DSCs.

---

### Art. 17 — Statements of Reasons

**Requirement**: Online platforms must provide a clear and specific statement of reasons to
each affected recipient when restricting access to information (Art. 17(1)).

**Assessment criteria:**

- [ ] Statement of reasons issued for all restriction types: removal, disabling, demotion,
      visibility restriction, monetisation restriction, suspension/termination of account
- [ ] Statement includes: (a) basis for decision (ToC or specific legal basis), (b) relevant
      facts and circumstances leading to the decision, (c) information on automated tools used,
      (d) reference to applicable redress mechanisms
- [ ] Statement submitted to the DSA Transparency Database
- [ ] Language accessible to the recipient

**Common gaps:** Generic "your content violated our policies" messages without specificity;
no reference to automated tool use; not submitted to the Transparency Database; no redress
pathway disclosed.

**Severity if incomplete**: PARTIAL/NON-COMPLIANT — Transparency Database submissions
are publicly visible; incomplete statements attract regulatory and civil society scrutiny.

---

### Art. 18 — Internal Complaint-Handling System

**Requirement**: Online platforms must provide an accessible, effective, free-of-charge
internal complaint-handling system for recipients to challenge platform decisions (Art. 20
[renumbered in practice as Art. 18 for internal complaints]).

**Assessment criteria:**

- [ ] Internal complaint system exists and is electronic
- [ ] Free of charge to recipients
- [ ] Covers all types of platform decisions (content restriction, account suspension, etc.)
- [ ] Processes complaints within a reasonable timeframe
- [ ] Platform provides specific reasoning for the complaint outcome
- [ ] System logs and reporting statistics available for Art. 15 transparency report

**Common gaps:** Appeal system exists but is not accessible for all decision types;
no timeframe commitment; responses are generic.

---

### Art. 21 — Out-of-Court Dispute Settlement

**Requirement**: Online platforms must enable recipients to access certified, independent
out-of-court dispute settlement (ODS) bodies (Art. 21(1)).

**Assessment criteria:**

- [ ] ODS body access provided (link or referral)
- [ ] At least one certified ODS body available per Member State in which the service operates
- [ ] ODS body is impartial, independent, expertise in platform legal and ToC issues
- [ ] Free or nominal-fee access for users
- [ ] Platform engages in good faith with ODS proceedings
- [ ] Platform informs recipients of ODS option in the context of dispute resolution

**Common gaps:** ODS access not disclosed in ToC or complaint-handling flow; no ODS body
certified for the platform in some Member States; platform refuses to engage with ODS
proceedings.

[EU-SPECIFIC] Certified ODS bodies are designated by DSCs. The availability of certified
bodies varies by Member State and service type. The Commission maintains a register. [VERIFY]

---

### Art. 20 — Trusted Flaggers

**Requirement**: Online platforms must give notices from trusted flaggers (entities certified
by a DSC) priority treatment, processing them expeditiously (Art. 20(1)).

**Assessment criteria:**

- [ ] Technical and organisational measures to identify trusted flagger notices
- [ ] Trusted flagger notices processed with priority — "without undue delay"
- [ ] Mechanism to receive notices from trusted flaggers electronically
- [ ] Platform reports abuse by a trusted flagger to the awarding DSC
- [ ] Annual transparency reporting on trusted flagger engagement

**Common gaps:** No differentiation between trusted flagger and general notices in technical
systems; no process to identify trusted flagger status; no monitoring for flagger misuse.

---

### Art. 22 / Art. 30 — Trader Traceability (Online Marketplaces)

**Requirement**: Online marketplace operators must, before allowing traders to offer products
or services on their platform, obtain specific trader identification information (Art. 30(1)).

**Assessment criteria:**

- [ ] Name, address, telephone number, and email address collected
- [ ] National identification number or trade register number collected
- [ ] Bank account details collected (where applicable)
- [ ] Self-certification by trader of compliance with applicable EU law obtained
- [ ] "Best efforts" assessment of information reliability conducted
- [ ] Verified traders only (or stops participation if information cannot be verified)
- [ ] Trader information made available to consumers upon request (Art. 22(1)(f))
- [ ] Platform explains KYBC procedure in terms and conditions

**Common gaps:** Trader onboarding collects information but does not verify reliability;
no consumer access mechanism for trader data; self-certification step absent; no procedure
for stopping unverifiable traders.

**Severity if missing**: NON-COMPLIANT — consumer protection obligation with direct civil
liability implications; DSC enforcement focus for marketplace operators.

---

### Art. 24 — Online Advertising Transparency

**Requirement**: Online platforms showing advertising must ensure recipients can identify
advertising clearly (Art. 24(1)).

**Assessment criteria:**

- [ ] Ads identified in clear, unambiguous, real-time manner
- [ ] Advertiser identity (name of legal or natural person) displayed
- [ ] Targeting parameters or criteria disclosed ("meaningful information")
- [ ] No use of special categories of personal data (ethnicity, religion, political opinion,
      sexual orientation, health, etc.) for targeting [GDPR Art. 9 interplay]
- [ ] No targeting of minors with advertising (Art. 28(2))
- [ ] Clear mechanism for recipients to identify each ad shown to them

**Common gaps:** Advertiser identity shows trading name but not legal entity; targeting
parameters disclosed only in aggregate (not for individual ad); minor age verification
absent in ad serving pipeline.

[GDPR INTERPLAY] Special category data targeting prohibition under Art. 24(1)(b) DSA
operates alongside GDPR Art. 9; DSA prohibition is absolute — no explicit consent exception
available under DSA (cf. EDPB Guidelines 3/2025). [VERIFY current EDPB position]

---

### Art. 25 — Dark Patterns Prohibition

**Requirement**: Online platforms must not design, organise, or operate their online
interfaces in a manner that deceives or manipulates recipients or that otherwise impairs
or distorts their ability to make free and informed decisions (Art. 25(1)).

**Prohibited design patterns (illustrative):**

- Confusing or manipulative consent mechanisms (e.g., large "Accept" button, small "Decline")
- False urgency or artificial scarcity indicators
- Subscription cancellation made harder than subscription sign-up
- Automatic pre-selection of options that are not privacy-friendly
- Repeated requests for the same consent decision after denial
- Visual hierarchy manipulation favouring platform commercial interests over user autonomy

**Assessment criteria:**

- [ ] User interface audit conducted for dark patterns
- [ ] Consent mechanisms comply with both DSA Art. 25 and GDPR Art. 7
- [ ] Subscription cancellation is as straightforward as sign-up
- [ ] No false urgency cues or fake scarcity mechanisms
- [ ] Options presented with neutral visual hierarchy
- [ ] Internal design review process covers dark patterns prior to deployment

**Common gaps:** UI review limited to GDPR consent; no specific Art. 25 checklist applied;
cancellation flow requires more steps than sign-up flow.

**Case law signal**: Amsterdam District Court (2025) — non-persistent video player settings
constituted dark patterns under DSA Art. 39 (VLOP context). [VERIFY citation]

---

### Art. 26 — Recommender System Transparency

**Requirement**: Online platforms using recommender systems must describe in plain language
the main parameters used, their relative importance, and options for users to modify or
influence the parameters (Art. 26(1)).

**Assessment criteria:**

- [ ] Plain-language description of recommender system parameters published
- [ ] Relative importance of main parameters explained (not just listed)
- [ ] At least one user-accessible option to modify or influence parameters offered
- [ ] Description is accessible within the platform interface (not only in privacy policy)
- [ ] Description covers all recommender systems used (feed, search ranking, content discovery)

**Common gaps:** High-level description available but no explanation of relative weighting;
user-facing controls exist but not linked from the recommender system disclosure; description
in privacy policy rather than in the relevant interface.

---

### Art. 27 — Advertising Repository (VLOPs/VLOSEs Only)

**Requirement**: VLOPs and VLOSEs must maintain a publicly accessible, searchable repository
of all advertising displayed on their interfaces during a given period (Art. 39 [renumbered
— cross-reference Art. 27 for general advertising, Art. 39 for VLOP interface design]).

**Assessment criteria (for VLOPs/VLOSEs):**

- [ ] Advertising repository maintained and publicly searchable
- [ ] Repository includes: ad content, advertiser identity, targeting parameters used,
      delivery period, total number of recipients reached (by country)
- [ ] Repository accessible via API for researchers
- [ ] Updated in real-time or near-real-time
- [ ] Repository available for at least 1 year after last display

**Common gaps:** Repository exists but API access is restricted; targeting parameters
disclosed at category level only; data for terminated campaigns not retained for full period.

[ENFORCEMENT ALERT] X (Twitter) was fined EUR 120M in December 2024 partly for advertising
repository and transparency failures. [VERIFY current enforcement status]

---

### Art. 28 — Protection of Minors

**Requirement**: Online platforms accessible to minors must implement appropriate and
proportionate measures to ensure a high level of privacy, safety, and security for minors
(Art. 28(1)). Must not show targeted advertising to minors based on profiling (Art. 28(2)).

**Assessment criteria:**

- [ ] Risk assessment conducted on likelihood of minor access and specific risks to minors
- [ ] Age assurance or age verification measures proportionate to risk implemented
- [ ] Targeted advertising to minors prohibited in ad-serving pipeline
- [ ] Privacy-by-default settings for minor accounts (where detectable)
- [ ] Harmful content risks assessed and mitigated (Commission 5Cs guidance: content,
      conduct, contact, consumer, cross-cutting)
- [ ] Commission guidelines on Art. 28 (July 2025) reviewed and applied [VERIFY]

**Common gaps:** Age verification relies solely on user self-declaration; ad-serving
pipeline not filtering by verified minor status; risk assessment for minor access not
documented; Commission guidelines not yet reviewed post-July 2025.

---

### Art. 34 — Systemic Risk Assessment (VLOPs/VLOSEs)

**Requirement**: VLOPs and VLOSEs must annually identify, analyse, and assess any systemic
risks stemming from the functioning and use of their service in the EU (Art. 34(1)).

**Four risk categories (Art. 34(1)):**

| Category                       | Description                                                                        | Platform Examples                                 |
| ------------------------------ | ---------------------------------------------------------------------------------- | ------------------------------------------------- |
| 1. Illegal content             | Dissemination of illegal content on the service                                    | CSAM, terrorist content, illegal goods            |
| 2. Fundamental rights          | Negative effects on freedom of expression, non-discrimination, consumer protection | Algorithmic suppression, discriminatory targeting |
| 3. Civic discourse & elections | Impact on democratic processes, electoral integrity                                | Disinformation, coordinated inauthentic behaviour |
| 4. Physical & mental wellbeing | Harms to physical or mental health, especially of vulnerable users                 | Harmful content patterns, addiction mechanisms    |

**Assessment criteria:**

- [ ] Initial systemic risk assessment completed within 4 months of designation
- [ ] Annual risk assessment conducted thereafter (at minimum)
- [ ] Assessment covers all four risk categories
- [ ] Assessment factors include: recommender system design, algorithmic systems, intentional
      manipulation, rapid dissemination vectors
- [ ] Assessment proportionate to platform's size, reach, and nature of service
- [ ] Assessment submitted to Commission and DSC of establishment [VERIFY submission procedure]
- [ ] Risk assessment published in Art. 42 transparency report (6-monthly)

**Common gaps:** Assessment conducted once and not updated annually; fundamental rights
impact analysis cursory; electoral risk category not assessed for general-purpose platforms;
assessment not proportionate to platform complexity; not submitted to DSC.

---

### Art. 35 — Risk Mitigation Measures (VLOPs/VLOSEs)

**Requirement**: VLOPs and VLOSEs must put in place reasonable, proportionate, effective
mitigation measures for the systemic risks identified under Art. 34 (Art. 35(1)).

**Assessment criteria:**

- [ ] Mitigation measures documented for each identified risk
- [ ] Measures are tailored to the specific risks identified (not generic)
- [ ] Measures take into account effects on fundamental rights (e.g., removal measures
      may suppress legitimate speech)
- [ ] Effectiveness of measures monitored and evaluated
- [ ] Measures updated following annual risk assessment
- [ ] Commission guidelines on electoral risk mitigation reviewed [VERIFY]

**Possible mitigation measures (illustrative, Art. 35(2)):**

- Enhanced content moderation for specific categories
- Trusted flagger programme engagement
- Transparency measures for advertising and recommenders
- Researcher access for independent review
- User empowerment tools (content filters, reporting mechanisms)
- De-amplification strategies for borderline content
- Fact-checking partnerships

**Common gaps:** Generic "we review content against our community standards" not specific
to Art. 34 risk categories; no fundamental rights impact assessment of mitigation measures;
measures not reviewed for effectiveness.

---

### Art. 36 — Crisis Response Mechanism (VLOPs/VLOSEs)

**Requirement**: When the Commission declares an extraordinary circumstance posing a serious
threat to public security or health, VLOPs/VLOSEs must assess whether their service
significantly contributes to the crisis and may be required to take specific measures
(Art. 36(1)).

**Assessment criteria:**

- [ ] Crisis response protocol documented internally
- [ ] Clear governance chain for crisis response decisions
- [ ] Process to assess service contribution to declared crisis within required timeframe
- [ ] Capacity to implement moderation adaptations rapidly (e.g., promotion of authoritative
      health/safety information)
- [ ] Reporting capability to Commission during crisis periods
- [ ] Voluntary crisis protocol participation assessed (Art. 48)

**Common gaps:** No crisis protocol; unclear ownership of crisis response decisions; no
pre-defined moderation playbooks for likely crisis scenarios (pandemic, major security event).

---

### Art. 37 — Independent Third-Party Audit (VLOPs/VLOSEs)

**Requirement**: VLOPs and VLOSEs must commission an independent audit of their compliance
with Chapter III (Arts. 33–43) at least annually (Art. 37(1)).

**Assessment criteria:**

- [ ] Annual audit commissioned from a qualified, independent auditor
- [ ] Auditor is independent (no financial or other relationship with the platform)
- [ ] Audit scope covers: Art. 34 risk assessment methodology, Art. 35 mitigation measures,
      Art. 36 crisis protocols, Art. 38/39 recommender/interface compliance, Art. 40 researcher
      access, Art. 42 transparency reporting
- [ ] Audit conducted per Delegated Regulation (EU) 2023/1080 procedures
- [ ] Audit report published within 3 months of receipt (Art. 37(4))
- [ ] Audit report submitted to Commission and DSC of establishment
- [ ] Audit Implementation Report (platform's response to recommendations) prepared

**Common gaps:** Audit scope limited to specific articles rather than full Chapter III;
publication timeline missed; no formal Audit Implementation Report; auditor independence
compromised by pre-existing relationship.

---

### Art. 38 — Non-Profiling Recommender Option (VLOPs Only)

**Requirement**: VLOPs using recommender systems must provide at least one option not
based on profiling (Art. 38(1)).

**Assessment criteria:**

- [ ] At least one non-profiling recommender option exists (e.g., chronological feed)
- [ ] Option is easily accessible within the platform interface
- [ ] Users can modify their selection at any time
- [ ] Non-profiling option is meaningfully different from profiling-based defaults

**Common gaps:** Non-profiling option exists but is buried in settings; option resets to
default after session end (dark pattern); "non-profiling" option still uses session-level
data that constitutes profiling under GDPR.

---

### Art. 40 — Researcher Data Access (VLOPs/VLOSEs)

**Requirement**: VLOPs and VLOSEs must provide vetted researchers with data access for
research on systemic risks (Art. 40(4)). Public data must be provided to any researcher
without undue delay (Art. 40(1)).

**Assessment criteria:**

- [ ] API or mechanism for public data access operational
- [ ] Public data requests fulfilled "without undue delay"
- [ ] Application procedure for vetted researcher status documented and operational
- [ ] Vetted researcher applications processed by the competent DSC
- [ ] Non-public data access provided to vetted researchers per Delegated Act (July 2025)
- [ ] Research data subject to GDPR-compliant protections
- [ ] Data access logs maintained and reported in Art. 42 transparency report

**Common gaps:** No public data API; researcher applications rejected without substantiated
reasons; data provided too slowly; Delegated Act (July 2025) not yet implemented.

[ENFORCEMENT ALERT] Meta and TikTok received preliminary findings of DSA violations for
inadequate researcher data access in October 2025 (non-final). [VERIFY current status]

---

### Art. 42 — Enhanced Transparency Reporting (VLOPs/VLOSEs)

**Requirement**: VLOPs and VLOSEs must publish enhanced transparency reports every six
months (Art. 42(2)), covering content moderation statistics, advertising data, and researcher
data access (more detailed than Art. 15 general reporting).

**Assessment criteria:**

- [ ] 6-monthly reports (not just annual)
- [ ] Report covers all Art. 42 requirements including advertising exposure data by advertiser
- [ ] Content moderation statistics disaggregated by content category and decision type
- [ ] Researcher data access logs and outcomes reported
- [ ] Systemic risk assessment summaries included (or by reference to published assessment)
- [ ] Published in machine-readable format
- [ ] Submitted to DSA Transparency Database

**Common gaps:** Annual report published but 6-monthly cycle not established; advertising
exposure data by advertiser not included; researcher access data not reported separately.

---

## Compliance Status Classification

### COMPLIANT

The obligation is met in full. The platform's measures satisfy the DSA's substantive
requirements and are operationally effective.

**Action**: Note for awareness. Document evidence in compliance record.

### PARTIAL

The obligation is partially implemented. Core elements are in place but material gaps exist.
May be sufficient to avoid a formal infringement finding in the short term but carries
medium-term enforcement risk.

**Action**: Document specific gaps. Generate prioritised remediation steps. Set remediation
timeline proportionate to enforcement risk.

### NON-COMPLIANT

The obligation is not implemented, is entirely absent, or is implemented in a way that
does not meet DSA requirements. Carries direct enforcement risk including fines and
operational orders.

**Action**: Explain specific non-compliance. Provide market-standard implementation
approach. Identify enforcement risk (fine range). Recommend immediate escalation to
senior legal/compliance leadership.

### MISSING (NOT ASSESSED)

The obligation applies but could not be assessed due to insufficient information.

**Action**: Flag as requiring further investigation. List the specific information needed.
Treat as NON-COMPLIANT for risk-scoring purposes until confirmed otherwise.

---

## Prioritisation Framework

Organise remediation recommendations by tier:

### Tier 1 — Immediate (0–30 days)

Obligations where non-compliance carries the highest enforcement risk or where the gap is
structurally disabling:

- Absence of notice-and-action mechanism (Art. 16)
- No legal representative for non-EU providers (Art. 13) — DSC enforcement access issue
- Advertising targeting minors in violation of Art. 28(2) — direct civil liability
- No transparency reporting filed for completed reporting periods
- VLOP/VLOSE designation with no Art. 34 systemic risk assessment initiated
- Active enforcement investigation open with DSC or Commission

### Tier 2 — Near-Term (30–90 days)

Material compliance gaps that create significant enforcement risk but can be remediated
with structured effort:

- Notice-and-action mechanism incomplete (Art. 16 partial implementation)
- Statement of reasons inadequate (Art. 17) — Transparency Database exposure
- Dark patterns confirmed in UI audit (Art. 25)
- Art. 37 audit not commissioned (for designated VLOPs/VLOSEs)
- Researcher data access mechanism absent (Art. 40) for VLOPs/VLOSEs
- Out-of-court dispute settlement not accessible to users (Art. 21)

### Tier 3 — Medium-Term (90–180 days)

Systemic and programme-level improvements that prevent future exposure:

- Art. 34 risk assessment methodology improvement
- Art. 35 mitigation measure effectiveness review
- Art. 42 6-monthly transparency reporting cycle established
- Recommender system disclosure improvement (Art. 26)
- Non-profiling recommender option accessibility improvement (Art. 38)
- Internal complaint-handling system enhancement (Art. 18)
- Trusted flagger programme establishment (Art. 20)

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Identify the platform tier, obligation set, and prior compliance work. Classify
assessment complexity (basic intermediary / online platform / VLOP/VLOSE). Identify which
DSA obligations are engaged and which require legalcode-mcp research.

**DO**: Execute the obligation gap analysis (Step 6). Generate findings. Score compliance
status and enforcement risk.

**CHECK**: Run the Citation Quality Gates. For every NON-COMPLIANT finding, run the
Self-Interrogation. Verify obligation mapping against platform tier. Confirm all applicable
obligations addressed.

**ACT**: Document new enforcement decisions or Commission guidance that affects the analysis.
Flag any obligations where the regulatory position has evolved since the last assessment.

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise if any gate fails.

| Gate           | Rule                                                                                                                                  | Fail Action                                                                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Source**     | Every compliance finding cites a specific DSA article, delegated act, or established regulatory position                              | Add citation or mark "[UNVERIFIED — counsel to confirm]"                            |
| **Format**     | All citations follow a consistent format: Regulation (EU) YYYY/NNNN, Art. X(Y)                                                        | Fix format                                                                          |
| **Currency**   | Every cited provision checked against the current DSA text and any amending instruments                                               | Flag "[CHECK CURRENCY — may have been amended or supplemented by implementing act]" |
| **Domain**     | Analysis stays within DSA scope; does not conflate GDPR, DMA, AI Act, or national law obligations without clearly distinguishing them | Remove or flag regulatory bleed                                                     |
| **Confidence** | Uncertainty about interpretation explicitly stated; evolving areas flagged                                                            | Add confidence qualifier                                                            |

### Self-Interrogation for NON-COMPLIANT Findings

For any finding classified as NON-COMPLIANT, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the non-compliance finding follow from the cited DSA article?
- Is there a counter-argument the platform's counsel could advance?
- Does the Commission's published guidance or a DSC decision support this interpretation?

**Pass 2 — Completeness**:

- Have all relevant DSA provisions been considered (including implementing/delegated acts)?
- Have GDPR and DMA interactions been checked?
- Are there regulatory safe harbours, micro/small exemptions, or proportionality defences
  not yet assessed?

**Pass 3 — Challenge**:

- What is the strongest argument that the platform is actually PARTIAL rather than
  NON-COMPLIANT?
- Under what circumstances might a DSC or the Commission exercise enforcement discretion?
- Is the NON-COMPLIANT classification proportionate to the actual regulatory risk?

Mark the audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material finding, assign a confidence level:

| Level        | Range     | Meaning                                                                  | Action                                                                  |
| ------------ | --------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear DSA text, confirmed by Commission guidance or enforcement decision | State with confidence                                                   |
| **High**     | 0.80–0.94 | Strong DSA authority, minor interpretation questions only                | State with brief caveat                                                 |
| **Probable** | 0.60–0.79 | Good reading of the text but genuine interpretive uncertainty            | State with explicit reasoning and contra-indicators                     |
| **Possible** | 0.40–0.59 | Evolving regulatory position; pending guidance or case                   | Flag for counsel review with both interpretations                       |
| **Unlikely** | 0.0–0.39  | Speculative; no authority support                                        | Do not assert; flag "[UNCERTAIN — regulatory position not yet settled]" |

---

## Glass Box Audit Trail

Every assessment output MUST include a Glass Box audit section:

```yaml
glass_box:
  skill: "legalcode-eu-dsa-compliance"
  assessment_date: "[date]"
  service_assessed: "[Service name or description]"
  platform_tier: "[Basic intermediary / Online platform / VLOP / VLOSE]"
  designated_vlop_vlose: "Yes [date] / No / Under investigation / Unknown"
  monthly_active_eu_users: "[number or range or Unknown]"
  provider_establishment: "[EU Member State / Non-EU with rep / Non-EU without rep]"
  assessment_scope: "[Full / Priority / Specific articles]"
  obligations_in_scope: "[count]"
  obligations_assessed: "[count]"
  compliant_findings: "[count]"
  partial_findings: "[count]"
  non_compliant_findings: "[count]"
  missing_information: "[count]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  regulations_consulted:
    - "Regulation (EU) 2022/2065 — [VERIFIED / UNVERIFIED]"
    - "[Other instrument] — [VERIFIED / UNVERIFIED]"
  enforcement_decisions_reviewed:
    - "[Decision, date, platform, finding] — [VERIFIED / UNVERIFIED]"
  citations_verified: "[count VERIFIED] / [count UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no NON-COMPLIANT findings)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, platform information gaps, or caveats]"
    - "DSA regulatory landscape is evolving; Commission guidelines and delegated acts
      issued regularly. Verify all findings against current authority before reliance."
  reviewer: "AI-assisted — requires review by qualified DSA counsel before action"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in a DSA compliance assessment:

1. **Conflating DSA tier with company size** — The DSA micro/small enterprise exemption
   (under 50 employees, under EUR 10M turnover) is distinct from the VLOP/VLOSE 45M MAU-EU
   threshold. A company can be large in revenue but operate a small-reach platform;
   conversely a large-reach platform may be operated by a small company. Apply each
   threshold independently.

2. **Treating designation as self-executing** — VLOPs and VLOSEs are formally designated
   by the European Commission. A platform that reaches 45M MAU-EU does not automatically
   acquire VLOP/VLOSE obligations; it must report its user numbers and await designation.
   Do not apply Chapter III obligations before designation, but do flag the threshold risk.

3. **Applying DSA only to social media** — The DSA applies to any provider of intermediary
   services serving EU users: cloud hosting, messaging apps, search engines, online
   marketplaces, app stores, comparison websites, and more. Scope assessment must not
   assume the only DSA-regulated entities are social networks.

4. **Conflating DSA and GDPR obligations** — DSA Art. 24 advertising transparency
   obligations operate alongside but distinct from GDPR Art. 6 lawful basis and Art. 7
   consent. A platform can be GDPR-compliant on advertising consent but DSA-non-compliant
   on Art. 24 advertiser identity disclosure, and vice versa. Assess each framework separately.

5. **Ignoring implementing and delegated acts** — The DSA text is only the starting point.
   Implementing regulations (transparency reporting templates), delegated regulations
   (audit procedures, researcher data access), and Commission guidelines (minors, electoral
   risk) add substantive requirements. An assessment based only on the main regulation text
   will miss material obligations.

6. **Treating "best efforts" as no obligation** — DSA Arts. 22 and 30 require marketplaces
   to make "best efforts" to verify trader information. This is not a no-obligation safe
   harbour; it requires documented, reasonable verification procedures. Assess what
   verification procedures exist.

7. **Omitting the fundamental rights assessment** — DSA Art. 35 explicitly requires risk
   mitigation measures to take into account effects on fundamental rights (freedom of
   expression, privacy, non-discrimination). An Art. 35 assessment that focuses solely on
   illegal content without assessing chilling effects on legitimate speech is incomplete.

8. **Assuming non-EU companies are outside DSA scope** — The DSA applies to providers
   established outside the EU if they offer services to EU users (Art. 2(1)). The
   Art. 13 legal representative requirement is the primary procedural consequence. Never
   assume a non-EU company is exempt without verifying its EU user footprint.

9. **Failing to distinguish DSA from DMA** — The Digital Markets Act targets competition
   concerns of "gatekeepers" with significant market power. The DSA targets content safety
   and transparency for all intermediary services. The designation criteria, obligations,
   and enforcement authorities differ. A DMA-compliant platform may have DSA gaps and
   vice versa.

10. **Single-cycle risk assessment** — DSA Art. 34 requires annual systemic risk assessment.
    A platform that conducted an initial assessment at designation but has not updated it
    annually — especially following major product changes or enforcement developments —
    is non-compliant. Risk assessments are not one-time events.

11. **Treating the Transparency Database as optional** — Statements of reasons (Art. 17)
    must be submitted to the DSA Transparency Database (transparency.dsa.ec.europa.eu).
    This is a mandatory submission, not a voluntary disclosure. Omission creates publicly
    visible compliance gaps.

12. **Overlooking the Art. 28 minor protection obligation for general platforms** — Art. 28
    is not limited to platforms primarily targeting children. Any online platform accessible
    to minors must conduct a risk assessment and implement proportionate safeguards. General
    social media, gaming platforms, and entertainment services are all in scope.

13. **Misclassifying internal complaint-handling scope** — Art. 18 complaint-handling
    systems must cover all types of platform restriction decisions: content removal,
    demotion, visibility restriction, account suspension, and monetisation restriction.
    A system that only handles content removal appeals is incomplete.

14. **Citing enforcement decisions as settled law** — Commission preliminary findings
    (such as those issued against Meta and TikTok in October 2025) are not final
    decisions. Distinguish between preliminary findings (non-binding), non-compliance
    decisions (binding), and final decisions with fines when characterising regulatory
    risk.

15. **Under-scoping the advertising repository** — For VLOPs and VLOSEs, the advertising
    repository obligation (often referenced as Art. 27 in practice) requires the repository
    to be publicly searchable and API-accessible to researchers. An advertising dashboard
    available only to advertisers does not satisfy this obligation.

16. **Assuming the DSA is fully static** — The DSA is supplemented by a rolling programme
    of delegated and implementing acts, Commission guidelines, and enforcement decisions.
    Any assessment older than 6 months should be refreshed. Flag the assessment date
    prominently and recommend periodic review.

---

## Writing Standards

Apply plain-language discipline to all assessment output:

**For compliance findings:**

- State the finding plainly: "The platform does not have an Art. 16 notice-and-action
  mechanism" not "There may be certain deficiencies in the platform's approach to the
  notice-and-action obligations contemplated by the Regulation."
- Cite the specific article and the specific gap. Not "transparency obligations" but
  "Art. 17 — statements of reasons are not submitted to the DSA Transparency Database."
- Active voice: "The platform must implement..." not "It is required that the platform..."
- Use the COMPLIANT / PARTIAL / NON-COMPLIANT status labels consistently.

**For remediation recommendations:**

- Begin with the action: "Implement a structured Art. 16 notice submission form that
  collects the four required fields."
- State the timeframe explicitly.
- Reference the specific DSA article.
- Do not use vague guidance ("consider improving transparency").

**Quality gate before delivery:**

- [ ] Every finding cites a specific DSA article
- [ ] Every NON-COMPLIANT finding has an associated remediation recommendation
- [ ] All VLOP/VLOSE-specific findings are clearly labelled as such
- [ ] Glass Box audit trail is complete
- [ ] No regulatory bleed (GDPR obligations presented as DSA obligations without distinction)

---

## External Tool Integration

This skill uses **legalcode-mcp** as its primary source for current DSA regulatory
material. The DSA is subject to frequent supplementary instruments and enforcement
developments.

**With legalcode-mcp connected (preferred):**

- Search for the current DSA text and any amending instruments
- Search for Commission implementing and delegated acts for the relevant year
- Search for enforcement decisions from the Commission and DSCs
- Search for Commission guidelines applicable to the platform type
- Save verified references to `/tmp/legalcode-dsa-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed using general DSA knowledge
- Mark all regulatory references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Recommend that the user verify key findings against EUR-Lex and the Commission's
  digital-strategy.ec.europa.eu portal before reliance

**Recommended external resources (manual verification):**

- EUR-Lex: Full DSA text and all supplementary acts
- digital-strategy.ec.europa.eu: Commission DSA policy hub, guidelines, VLOP designation
  list
- transparency.dsa.ec.europa.eu: DSA Transparency Database (statements of reasons, risk
  assessments, audit reports)
- dsa-observatory.eu: Independent analysis and enforcement tracking

---

## Localization Notes

The DSA is an EU regulation — directly applicable in all 27 Member States without national
transposition. However, practical compliance involves national-level elements:

- **Digital Services Coordinators (DSCs)**: One per Member State. The DSC of the Member
  State of establishment has primary jurisdiction for non-VLOP platforms. DSC contact
  information, national guidelines, and enforcement priorities vary by Member State.
  Check the DSC of your Member State of establishment for national implementation guidance.

- **Out-of-court dispute settlement (Art. 21)**: Certified ODS bodies are designated at
  Member State level. Availability varies by country and service type. Check the DSC
  certification register for the Member States in which the service is offered. [VERIFY]

- **National enforcement procedures**: For non-VLOP platforms, fines and enforcement
  orders are issued by DSCs under national procedural law. Maximum fine levels under the
  DSA (Art. 52) are set as percentages of global turnover, but procedural rules (appeal
  mechanisms, judicial review) are national. [VERIFY with qualified counsel in the relevant
  Member State]

- **Language requirements**: While the DSA does not impose EU-wide language mandates for
  terms of service, Art. 14 requires ToC to be in the language(s) in which the service
  is offered. Member State DSCs may have additional guidance on language accessibility.

---

## Output Format Template

Use this template for the final assessment report:

```markdown
# DSA Compliance Assessment — [Service Name]

**Assessment Date:** [date]
**Assessed by:** legalcode-eu-dsa-compliance (AI-assisted — requires qualified legal review)

---

## 1. Platform Classification

**Platform tier:** [Basic intermediary / Online platform / VLOP / VLOSE]
**VLOP/VLOSE designation status:** [Yes/No/Under investigation]
**Monthly active EU recipients (estimated):** [count]
**Provider establishment:** [EU Member State / Non-EU]
**Competent Digital Services Coordinator:** [DSC name and Member State]
**Applicable obligation set:** [Summary or reference to obligation map]

---

## 2. Executive Summary

**Overall compliance posture:** [COMPLIANT / PARTIAL / NON-COMPLIANT] — [1–2 sentence summary]

| Risk Category                           | Status   | Finding Count |
| --------------------------------------- | -------- | ------------- |
| Immediate remediation required (Tier 1) | [status] | [count]       |
| Near-term gaps (Tier 2)                 | [status] | [count]       |
| Programme improvements (Tier 3)         | [status] | [count]       |

**Top 3 priority issues:**

1. [Issue 1] — [status] — [article]
2. [Issue 2] — [status] — [article]
3. [Issue 3] — [status] — [article]

**Maximum fine exposure (if all gaps unresolved):** [range, e.g., up to X% of global annual
turnover]

---

## 3. Obligation-by-Obligation Findings

For each applicable obligation:

### [Article number] — [Obligation name]

**Status:** [COMPLIANT / PARTIAL / NON-COMPLIANT / MISSING]
**Confidence:** [Definite / High / Probable / Possible / Unlikely]

**Finding:** [Specific description of the compliance status and gap, if any]

**Evidence reviewed:** [What documentation or information was assessed]

**Remediation:** [Specific steps to close any gap, with timeframe]

**Legal basis:** [Specific DSA article and sub-article]

---

## 4. Remediation Plan

### Tier 1 — Immediate (0–30 days)

| Finding   | Action   | Owner  | Deadline |
| --------- | -------- | ------ | -------- |
| [finding] | [action] | [team] | [date]   |

### Tier 2 — Near-Term (30–90 days)

| Finding   | Action   | Owner  | Deadline |
| --------- | -------- | ------ | -------- |
| [finding] | [action] | [team] | [date]   |

### Tier 3 — Medium-Term (90–180 days)

| Finding   | Action   | Owner  | Deadline |
| --------- | -------- | ------ | -------- |
| [finding] | [action] | [team] | [date]   |

---

## 5. Regulatory Cross-Reference

**GDPR interplay findings:** [Any obligations where GDPR and DSA interact — cite EDPB
Guidelines 3/2025 where relevant]

**DMA interplay findings:** [If the platform is also a DMA gatekeeper — note where DMA
and DSA obligations overlap or conflict]

**AI Act interplay:** [If the service deploys AI systems regulated under the EU AI Act —
note where AI Act transparency obligations interact with DSA recommender system disclosures]

---

## 6. Glass Box Audit Trail

[Insert Glass Box YAML block from template above]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on:

- Regulation (EU) 2022/2065 (DSA) full text via EUR-Lex
- Commission implementing and delegated acts (Delegated Reg. 2023/1080 on audits;
  Implementing Reg. 2023/1092 on transparency reporting templates; Art. 40 Delegated Act
  July 2025)
- EDPB Guidelines 3/2025 on the DSA–GDPR interplay
- Commission enforcement decisions (X/Twitter EUR 120M, December 2024)
- Commission preliminary findings (Meta and TikTok, October 2025)
- DSA Observatory independent analysis (dsa-observatory.eu)
- ACM (Netherlands DSC) published guidelines (February 2025)
- Commission Article 28 minors guidelines (July 2025)
- 2-agent research pipeline: Structural Analyst + DSA Legal Research Agent
- Legalcode quality framework: Citation Quality Gates, Self-Interrogation, Confidence
  Scoring, Glass Box Audit Trail (calibrated to legalcode-contract-review gold standard)

All regulatory references should be verified against authoritative sources before reliance.
The DSA regulatory landscape evolves continuously; verify the current status of all cited
acts and decisions.
