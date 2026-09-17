---
name: legalcode-dmca-takedown-workflow
description: Manages DMCA takedown and counter-notification workflows under 17 USC 512, and EU Digital
  Services Act (DSA, Regulation 2022/2065) notice-and-action obligations. Use when drafting, sending,
  or evaluating DMCA takedown notices; handling counter-notifications and put-back timelines; assessing
  safe harbor eligibility for online service providers; building or auditing repeat infringer policies;
  registering or verifying a designated DMCA agent; responding to wrongful takedowns; assessing 512(f)
  misrepresentation liability; or mapping DSA Art. 16 notice obligations, DSA Art. 20 internal complaint
  procedures, and CDSM Directive Art. 17 upload-filter obligations for OCSSPs.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Manages DMCA takedown and counter-notification workflows under 17 USC 512, and EU Digital Services Act (DSA, Regulation 2022/2065) notice-and-action obligations. Use when drafting, sending, or evaluating DMCA takedown notices; handling counter-notifications and put-back timelines; assessing safe harbor eligibility for online service providers; building or auditing repeat infringer policies; registering or verifying a designated DMCA agent; responding to wrongful takedowns; assessing 512(f) misrepresentation liability; or mapping DSA Art. 16 notice obligations, DSA Art. 20 internal complaint procedures, and CDSM Directive Art. 17 upload-filter obligations for OCSSPs. Also triggers when asked about platform copyright liability, user-generated content safe harbors, notice-and-takedown abuse, Lumen Database, Trusted Flaggers, repeat infringer termination, copyright safe harbor loss, or the interaction between US DMCA and EU DSA regimes. Covers US law (17 USC 512), EU law (DSA Reg. 2022/2065; CDSM Dir. 2019/790), and UK law (s.97A CDPA 1988; UK-DSA post-Brexit position) with jurisdiction-agnostic markers for other jurisdictions.


# Legalcode DMCA Takedown & Counter-Notification Workflow

> **Disclaimer**: This skill provides a framework for AI-assisted DMCA and DSA takedown
> workflow management. It does not constitute legal advice. All outputs should be reviewed by
> a qualified IP/internet law attorney licensed in the relevant jurisdiction before use.
> Copyright law evolves rapidly — cases cited may have been reversed, distinguished, or
> superseded; verify all citations against authoritative sources before relying on them.
> Statutory references from memory carry hallucination risk — all citations marked [VERIFY]
> should be confirmed against official sources (law.cornell.edu/uscode, eur-lex.europa.eu,
> Copyright Office at copyright.gov) before use.

---

## Purpose and Scope

This skill manages the full lifecycle of DMCA takedown and counter-notification workflows,
and maps the parallel EU DSA notice-and-action regime. It addresses two perspectives:

- **Rights Holder / Complainant**: Sending valid takedown notices, assessing fair use before
  sending, avoiding 512(f) liability, and following up when platforms fail to act.
- **Platform / Service Provider**: Achieving and maintaining safe harbor eligibility,
  processing notices, handling counter-notifications, running repeat infringer programs,
  and registering designated agents.
- **Alleged Infringer / Content Creator**: Evaluating wrongful takedowns, drafting
  counter-notifications, and asserting 512(f) misrepresentation claims.

**Covers:**

- US DMCA safe harbor framework — four harbor categories (17 USC 512(a)-(d))
- Valid takedown notice construction — all six 512(c)(3) elements
- Counter-notification procedure and put-back timeline — 512(g)
- Designated DMCA agent registration — 37 CFR Part 201 / Copyright Office
- Repeat infringer policy design and implementation — 512(i)
- 512(f) misrepresentation liability — wrongful takedown claims
- EU DSA notice-and-action — Art. 16 notice obligations, Art. 20 internal appeals
- CDSM Directive Art. 17 upload-filter obligations for OCSSPs
- DSA Trusted Flagger system — Art. 22
- DMCA vs. DSA regime comparison and dual-compliance mapping
- UK post-Brexit position — s.97A CDPA 1988 and UK Online Safety Act 2023

**Does not:**

- Draft licensing agreements (see `legalcode-technology-license-agreement`)
- Assess substantive copyright infringement (see `legalcode-copyright-infringement-assessment`)
- Cover trademark or patent takedown procedures
- Constitute legal advice or replace qualified counsel

---

## Jurisdiction and Governing Law

| Jurisdiction                | Primary Statute/Regulation                                                       | Key Standard                                                                     |
| --------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **United States**           | 17 USC 512 (DMCA, enacted 1998)                                                  | Notice-and-takedown; safe harbor; repeat infringer policy; designated agent      |
| **European Union**          | DSA Reg. 2022/2065 (applicable Feb 2024)                                         | Notice-and-action; expeditious removal; Art. 16 elements; DSA Art. 6 safe harbor |
| **EU (copyright-specific)** | CDSM Dir. 2019/790, Art. 17                                                      | Upload-filter obligations for OCSSPs; licensing-first approach                   |
| **United Kingdom**          | CDPA 1988 s.97A; UK OSA 2023; E-Commerce Regs 2002 [VERIFY post-Brexit position] | Site-blocking; hosting safe harbor; [VERIFY: UK DSA equivalent status]           |

[JURISDICTION-SPECIFIC] For jurisdictions outside US/EU/UK, research:

- Local copyright notice-and-takedown statutes (Canada: NISA/Notice-and-Notice; Australia: graduated response proposals)
- Whether jurisdiction has enacted safe harbor legislation analogous to DMCA 512 or EU E-Commerce Directive
- Designated agent or single point-of-contact requirements
- Repeat infringer termination obligations

**Note on EU Territorial Scope**: DSA applies to intermediary service providers that offer
services to recipients located in the EU, regardless of the provider's place of establishment.
A US-based platform with EU users must comply with DSA notice-and-action obligations.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses and asks when:

- The answer changes which regime(s) apply (US-only vs. dual US/EU compliance)
- The user's role determines which perspective (rights holder, platform, or alleged infringer)
  shapes the entire analysis
- Platform type affects which safe harbor(s) are available
- A notice is borderline defective or borderline 512(f)-abusive

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

### Step 1: Accept Input and Identify Scenario

Accept input in any of these forms:

- A takedown notice (submitted for drafting, review, or compliance check)
- A counter-notification (submitted for drafting or review)
- A platform compliance question (repeat infringer policy, designated agent, safe harbor audit)
- A wrongful takedown complaint (from content creator or platform)
- A dual-compliance question (DMCA + DSA for a platform with US and EU users)

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask:

1. **User's role in this workflow:**
   - Options: Rights Holder (sending takedowns) | Platform/Service Provider (receiving/processing notices) | Content Creator/Alleged Infringer (received wrongful takedown) | Legal Counsel (advising one of the above)
   - _Why this matters_: The entire analysis, risk profile, and recommended actions depend on perspective.

2. **Platform type (for platform-side work):**
   - Options: Hosting/UGC Platform (512(c)) | Search Engine/Aggregator (512(d)) | ISP/Transit Provider (512(a)) | CDN/Cache Service (512(b)) | Multi-category platform
   - _Why this matters_: Different safe harbors apply and have different requirements.

3. **Jurisdictions in scope:**
   - Options: US only | EU only | US + EU (dual compliance) | UK only | Global (all major regimes)
   - _Why this matters_: DMCA and DSA have materially different notice elements, timelines, and put-back procedures.

4. **Nature of content at issue:**
   - Options: Music/audio | Video/film | Images/photography | Text/written content | Software/code | Mixed/unknown
   - _Why this matters_: Affects fair use assessment, CDSM Art. 17 OCSSP applicability, and notice strategy.

5. **Urgency:**
   - Options: Imminent harm requiring immediate takedown | Standard (days to weeks) | Compliance audit (no active dispute)
   - _Why this matters_: Affects whether to lead with formal legal process or first send informal notice.

---

### Step 3: Assess Safe Harbor Eligibility (Platform-Side) or Notice Strategy (Rights Holder)

#### 3A. For Platforms — Safe Harbor Eligibility Assessment

Assess eligibility under each applicable safe harbor category. Run this assessment before
processing any notice or designing any compliance program.

##### US DMCA Safe Harbor Grid

| Safe Harbor                       | Statute       | Applies To                                        | Core Eligibility Conditions                                                                                                                                       |
| --------------------------------- | ------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **512(a) — Transitory**           | 17 USC 512(a) | ISPs, transit providers                           | No initiation of transmission; automatic technical process; no selection of content/recipients; no storage beyond transitory transmission                         |
| **512(b) — Caching**              | 17 USC 512(b) | CDNs, proxy servers, caching services             | Material made available by third party; automatic intermediate storage; no modification; expeditious removal on notice; compliance with refresh conditions        |
| **512(c) — Hosting/UGC**          | 17 USC 512(c) | Hosting platforms, UGC platforms (YouTube, Vimeo) | No actual/red-flag knowledge; no direct financial benefit + right to control; designated agent registered; repeat infringer policy; expeditious removal on notice |
| **512(d) — Information Location** | 17 USC 512(d) | Search engines, link directories, aggregators     | Same knowledge and financial benefit requirements as 512(c); designated agent registered; repeat infringer policy; expeditious removal on notice                  |

**Common conditions for 512(c) and 512(d) — all four must be met:**

1. **No Actual or Red-Flag Knowledge** (512(c)(1)(A)):
   - "Actual knowledge": Platform does not know specifically that material is infringing.
   - "Red flag knowledge": Platform is not "aware of facts or circumstances from which infringing activity is apparent." [VERIFY: *Capitol Records v. Vimeo*, 2d Cir. 2025 — standard requires that infringement would be apparent to an ordinary person, not just a copyright expert]
   - Willful blindness can substitute for actual knowledge (_Viacom Int'l v. YouTube_, 2d Cir. 2012) [VERIFY]

2. **No Direct Financial Benefit + Right to Control** (512(c)(1)(B)):
   - Platform must not receive "a financial benefit directly attributable to the infringing activity" AND simultaneously have "the right and the ability to control such activity."
   - "Right and ability to control" requires "something more" than mere legal/technical capacity to block content. Courts require substantial influence over users' infringing activity. [VERIFY current circuit standards]
   - Analysis: (i) Does platform have the power to supervise the activity? (ii) Is there a direct causal link between infringing activity and financial gain?

3. **Designated Agent Registered** (512(c)(2) / 512(d)):
   - Platform must have registered a designated DMCA agent with the Copyright Office.
   - See Step 5 (Designated Agent Registration) for full requirements.

4. **Repeat Infringer Policy Implemented** (512(i)):
   - Platform must have "reasonably implemented" a policy of terminating repeat infringers.
   - See Step 6 (Repeat Infringer Policy) for full requirements.

##### EU DSA Safe Harbor Grid

| Safe Harbor      | DSA Article | Applies To                       | Core Eligibility Conditions                                                                                                                                              |
| ---------------- | ----------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Mere Conduit** | Art. 4      | ISPs, DNS providers              | Does not initiate/select/modify; does not select recipients; no storage (or transitory only); expeditious removal on actual knowledge                                    |
| **Caching**      | Art. 5      | CDNs, proxy caches               | Automatic intermediate temporary storage; does not modify; expeditious removal on actual knowledge of origin removal; complies with industry refresh protocols           |
| **Hosting**      | Art. 6      | UGC platforms, hosting providers | No actual knowledge of illegal activity; not aware of facts/circumstances from which illegality apparent; upon knowledge/awareness, acts expeditiously to remove/disable |

**DSA Art. 6 "Actual Knowledge" defined narrowly:**

- Knowledge = knowledge of the unlawful nature of **specific content**, obtained via court order or a sufficiently substantiated Art. 16 notice enabling identification of content as **manifestly illegal** without detailed legal examination.
- **Key difference from DMCA**: DSA does NOT include a constructive "red flag" knowledge standard. Circumstantial awareness (e.g., volume of DMCA notices for a user) does not trigger DSA actual knowledge without a specific manifestly illegal notice.

**⟁ CLARIFY** — If the platform serves EU users and receives DSA notices for the same
content covered by DMCA notices, ask: "Does the platform have separate DMCA and DSA notice
processing workflows, or a unified system? This determines whether dual-compliance analysis
applies."

---

### Step 4: Draft or Review a Takedown Notice

#### 4A. DMCA Takedown Notice (17 USC 512(c)(3))

A valid DMCA takedown notice must **substantially comply** with all six elements below.
Failure to substantially comply means the notice does not trigger the platform's takedown
obligation and does not give the platform "actual knowledge" of infringement.

##### Six Required Elements (17 USC 512(c)(3)(A))

| #   | Element                          | Statutory Requirement                                                                                                                                                               | Practical Guidance                                                                                                                                                                                                   |
| --- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Signature**                    | Physical or electronic signature of person authorized to act on behalf of copyright owner                                                                                           | Typed name, digital signature, or email from authorized account suffices                                                                                                                                             |
| 2   | **Work Identification**          | Identification of the copyrighted work(s) claimed infringed; if multiple works at a single online site, a "representative list" is permitted                                        | Include title, registration number (if registered), or URL of original work                                                                                                                                          |
| 3   | **Infringing Material Location** | Identification of material claimed to be infringing, with information "reasonably sufficient to permit the service provider to locate the material"                                 | Provide specific URL(s) — not category descriptions; [*Perfect 10 v. CCBill*, 488 F.3d 1102 (9th Cir. 2007): notice must enable provider to locate material without piecing together scattered information] [VERIFY] |
| 4   | **Contact Information**          | Information reasonably sufficient to permit the service provider to contact the complaining party: name, address, telephone number, email                                           | All three identifiers (address, phone, email) are best practice; email alone may be insufficient                                                                                                                     |
| 5   | **Good Faith Statement**         | Statement that the complaining party "has a good faith belief that use of the material in the manner complained of is not authorized by the copyright owner, its agent, or the law" | Must consider fair use before submitting — [*Lenz v. Universal Music*, 9th Cir. 2016: failure to consider fair use is "willful blindness" to fair use rights] [VERIFY]                                               |
| 6   | **Perjury Statement**            | Statement, under penalty of perjury, that: (i) information in notice is accurate; and (ii) complaining party is the copyright owner or authorized to act on owner's behalf          | Both sub-elements required; perjury penalty under 18 USC 1621; false statements also trigger 512(f) civil liability                                                                                                  |

##### Pre-Sending Checklist for Rights Holders

Before sending a DMCA takedown notice, confirm:

- [ ] **Copyright ownership confirmed**: Do you own the copyright, or have authorization from the owner? If work is unregistered, do you have evidence of authorship/ownership?
- [ ] **Fair use considered**: Have you genuinely evaluated whether the allegedly infringing use qualifies as fair use under 17 USC 107 (purpose and character, nature of work, amount used, market effect)? Document this analysis.
- [ ] **Registration not required, but affects remedies**: Copyright registration before infringement (or within 3 months of publication) enables statutory damages and attorney's fees under 17 USC 504-505. [VERIFY current registration status]
- [ ] **Specific URL(s) identified**: Can you provide exact URL(s) for each infringing item? Bulk or category-based notices without specific URLs may fail.
- [ ] **Authorized signatory confirmed**: Is the person signing the notice authorized to act for the copyright owner?
- [ ] **All six elements present**: Review the draft against the table above.
- [ ] **512(f) risk assessed**: Is there any plausible fair use argument or legitimate license the alleged infringer might assert? Document your analysis.

##### DMCA Notice Template

```
[Date]

To: DMCA Designated Agent, [Platform Name]
[Agent Name and Address from Copyright Office Directory]
[Agent Email from Copyright Office Directory]

DMCA TAKEDOWN NOTICE PURSUANT TO 17 U.S.C. § 512(c)(3)

I. SIGNATURE
[Electronic signature or typed name of authorized person]
Authorized Agent for: [Copyright Owner Name]

II. IDENTIFICATION OF COPYRIGHTED WORK(S)
[Full title of work(s)]
[Registration number if registered: [Reg. No.]]
[URL or description of original work(s)]
[Note: If multiple works at one site: "See Representative List attached as Exhibit A."]

III. IDENTIFICATION OF INFRINGING MATERIAL AND LOCATION
The following URL(s) host material that infringes the above copyright(s):
- [Exact URL 1]
- [Exact URL 2]
[Continue as needed]

IV. CONTACT INFORMATION
[Full name]
[Mailing address]
[Phone number]
[Email address]

V. GOOD FAITH BELIEF STATEMENT
I have a good faith belief that the use of the material in the manner described above is
not authorized by the copyright owner ([Owner Name]), its agent, or the law. I have
considered whether the use constitutes fair use under 17 U.S.C. § 107 and concluded that
it does not, for the following reasons: [Brief statement].

VI. PERJURY STATEMENT
I swear, under penalty of perjury, that the information in this notification is accurate
and that I am the copyright owner or am authorized to act on behalf of the copyright owner
of an exclusive right that is allegedly infringed.

[Signature]
[Printed Name]
[Date]
```

#### 4B. EU DSA Notice (Art. 16, Regulation 2022/2065)

A valid DSA notice must contain four elements under Art. 16(2). Unlike DMCA notices, DSA
notices cover **all illegal content** — not just copyright.

##### Four Required Elements (DSA Art. 16(2))

| #   | Element                  | DSA Requirement                                                                                                                                                                                           | Practical Guidance                                                                                                                                                       |
| --- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | **Legal Substantiation** | "A sufficiently substantiated explanation of the reasons why the individual or entity alleges the information in question to be illegal content"                                                          | Identify the specific EU/national law provision violated; explain why the content violates it; enable provider to identify illegality without detailed legal examination |
| 2   | **Precise Location**     | "A clear indication of the exact electronic location of that information, such as the exact URL or URLs, and, where necessary, additional information enabling the identification of the illegal content" | Exact URL(s) required; for dynamic content, describe additional identifying information                                                                                  |
| 3   | **Submitter Identity**   | Name and email address of notifier                                                                                                                                                                        | Exception: anonymous notices permitted for child sexual abuse material to avoid re-traumatization                                                                        |
| 4   | **Good Faith Statement** | "A statement confirming the bona fide belief of the individual or entity submitting the notice that the information and allegations contained therein are accurate and complete"                          | Intentionally less formal than DMCA perjury statement; bad faith notices trigger potential liability                                                                     |

**Key DSA notice-processing obligations for platforms:**

- Confirm receipt without undue delay
- Process in "timely, diligent, non-arbitrary and objective manner"
- Notify submitter of decision (with reasons)
- Inform submitter of redress options (Art. 20 internal complaint; Art. 21 out-of-court settlement)
- No prescribed response deadline — "without undue delay" evaluated by Digital Services Coordinators

##### DMCA vs. DSA Notice Comparison

| Dimension                        | DMCA 512(c)(3)                                                                | DSA Art. 16                                                                              |
| -------------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Scope**                        | Copyright infringement only                                                   | All illegal content (copyright, hate speech, terrorism, CSAM, consumer protection, etc.) |
| **Elements**                     | 6 mandatory elements                                                          | 4 mandatory elements                                                                     |
| **Signature/Perjury**            | Perjury statement (under penalty of perjury; both accuracy and authorization) | Good faith statement (no perjury language; accuracy only)                                |
| **Fair use consideration**       | Required (_Lenz_, 9th Cir.)                                                   | N/A — no equivalent good faith analysis requirement                                      |
| **URL specificity**              | Specific URL(s) required                                                      | Exact URL(s) required (plus additional identification information if necessary)          |
| **Response timeline**            | "Expeditiously" (24-72 hours typical)                                         | "Without undue delay" and "timely" (no specific deadline)                                |
| **Misrepresentation liability**  | 17 USC 512(f) — actual damages + profits + attorney's fees                    | DSA Recital 52 — potential liability under national law; Art. 23 (misuse of service)     |
| **Counter-notification**         | Formal 512(g) procedure with 10-14 business day put-back                      | Art. 20 internal complaint + Art. 21 out-of-court settlement                             |
| **Put-back procedure**           | Mandatory 10-14 business day waiting period                                   | No equivalent formal put-back procedure                                                  |
| **Penalties for non-compliance** | Safe harbor loss → copyright liability                                        | DSC enforcement; VLOPs: up to 6% global annual revenue                                   |

---

### Step 5: Designated DMCA Agent Registration

Every platform relying on 17 USC 512(c) or 512(d) safe harbors **must** have a registered
designated agent with the US Copyright Office. Failure to have a validly registered agent
means the platform is not eligible for either safe harbor, regardless of other compliance.

#### Registration Requirements

**Register at**: Copyright Office DMCA Agent Directory (https://www.copyright.gov/dmca-directory/) [VERIFY URL is current]

**Required information for registration:**

- Legal name of the service provider
- All alternative names by which the service provider is known (including domain names)
- Agent's name
- Agent's mailing address
- Agent's telephone number
- Agent's email address

**Cost**: $6 per registration (as of 2024; [VERIFY current fee])

**Renewal**: Registration must be renewed every **three years** from the date of registration (37 CFR Part 201 2017 interim rule). Failure to renew = safe harbor ineligibility. [VERIFY renewal date for existing registrations]

**Post-registration obligations:**

- Publish agent's contact information on the platform's publicly accessible website (e.g., in Terms of Service, DMCA Policy page)
- Keep registration current if agent's details change — update within 48 hours of change
- Maintain registration even if no takedown notices received

**⟁ CLARIFY** — For platforms: "Do you currently have a registered DMCA agent in the Copyright Office directory? If yes, please provide the registration date to assess whether renewal is due. If no, this is the highest-priority compliance action."

#### DSA Single Point of Contact (Art. 11)

Platforms subject to DSA must designate a **single point of contact** for direct communications with DSA Digital Services Coordinators and the European Commission. Note: this is distinct from DMCA agent registration and does not substitute for it.

---

### Step 6: Repeat Infringer Policy

Both US DMCA (17 USC 512(i)) and EU DSA (Art. 23 — misuse of service) require platforms
to address repeat infringers, though the frameworks differ materially.

#### DMCA Repeat Infringer Policy (17 USC 512(i))

**Statutory requirement**: Platform must have "adopted and reasonably implemented, and inform subscribers and account holders of, a policy that provides for the termination in appropriate circumstances of subscribers and account holders of the service provider's system or network who are repeat infringers."

All four elements must be satisfied:

| Element                                      | Requirement                                           | Compliance Markers                                                               |
| -------------------------------------------- | ----------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Adopted**                                  | Written policy exists                                 | Published in Terms of Service, DMCA Policy, or Help Center                       |
| **Reasonably implemented**                   | Policy is actually enforced, not just nominal         | Documented enforcement actions; not selectively applied to disfavored users only |
| **Informed**                                 | Subscribers/account holders are told about the policy | Notice in ToS, registration flow, or DMCA policy page                            |
| **Termination in appropriate circumstances** | Repeat infringers actually get terminated             | Termination (not just warning) as eventual consequence                           |

##### Key Case Law on Reasonable Implementation

| Case                                                                             | Holding                                                                                                                                                                                                         | Practical Impact                                                                                      |
| -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **BMG Rights Mgmt. v. Cox Communications**, 4th Cir. 2018 [VERIFY]               | Cox's repeat infringer policy was not "reasonably implemented" because Cox continued reinstating accounts after termination (DMCA agent instructed to reinstate ~95% of terminated accounts) — safe harbor lost | Reinstatement undermines "reasonably implemented" standard; document reinstatement criteria carefully |
| **Warner Records v. Charter Communications**, D. Colo. (ongoing) [VERIFY status] | Pending litigation on whether Charter's repeat infringer program was sufficiently robust                                                                                                                        | Monitoring active litigation for guidance on minimum required warning thresholds                      |
| **Perfect 10 v. CCBill**, 9th Cir. 2007 [VERIFY]                                 | A policy is reasonably implemented if it "substantially" terminates repeat infringers; minor failures tolerated                                                                                                 | Policy need not be perfect — good faith implementation suffices                                       |
| **Viacom v. YouTube**, 2d Cir. 2012 [VERIFY]                                     | YouTube's repeat infringer policy was adequately implemented — terminated accounts of users who received repeated notices                                                                                       | Documenting systematic enforcement supports reasonableness                                            |

##### Repeat Infringer Policy Design Framework

**Recommended tiered approach:**

```
Strike 1: Warning notice sent to account holder; infringing content removed
Strike 2: Second warning; content removed; content upload privileges restricted
Strike 3+: Account suspension or termination (depending on severity and time window)

Escalation triggers (automatic to Strike 3):
- Court judgment of infringement
- Notice from law enforcement
- Blatant commercial piracy (obvious infringement at scale)
```

**Key design decisions** (address in the policy):

1. **Definition of "infringement"**: Is a repeat infringer someone who receives N takedown notices, or someone against whom N notices are sustained (i.e., counter-notification not filed)?
2. **Time window**: Does the strike counter reset after a period (e.g., 12 months)?
3. **Reinstatement criteria**: Under what circumstances can a terminated account be reinstated? Document the criteria and apply them consistently.
4. **Escalating sanctions**: Is there a graduated warning system before termination?
5. **Business account vs. personal account**: Different treatment may be justified (business accounts may trigger earlier termination given commercial scale).

**⟁ CLARIFY** — "Does your current policy define 'repeat infringer' by reference to notices received, notices sustained (after counter-notification), or infringement actually adjudicated by a court? This definition is critical to whether your policy is 'reasonably implemented.'"

#### DSA Art. 23 — Misuse of Service (EU Equivalent)

DSA Art. 23 requires platforms to suspend users who "frequently provide manifestly illegal content." Key differences from DMCA:

| Dimension             | DMCA 512(i)                                | DSA Art. 23                                                              |
| --------------------- | ------------------------------------------ | ------------------------------------------------------------------------ |
| **Trigger**           | "Repeat infringer" (copyright)             | Frequent provision of "manifestly illegal content" (any illegal content) |
| **Threshold**         | Not specified — reasonable implementation  | "Frequently" — no fixed number                                           |
| **Response required** | Termination "in appropriate circumstances" | "Suspension, for a reasonable period of time"                            |
| **Notice to user**    | Not explicitly required                    | Prior warning required before suspension                                 |
| **Content type**      | Copyright infringement only                | All illegal content under DSA                                            |
| **Due notice**        | Policy must be published                   | Warning before suspension mandated                                       |

---

### Step 7: Counter-Notification Procedure (DMCA 512(g))

When a platform removes content in response to a DMCA takedown notice, the content creator
(alleged infringer) may submit a counter-notification under 17 USC 512(g) to request
reinstatement.

#### When Counter-Notification Is Appropriate

Consider counter-notification when:

- The takedown notice was factually wrong (you do not infringe the claimed copyright)
- The use qualifies as fair use (17 USC 107) — _Lenz v. Universal_
- The copyright claim is invalid (work is in public domain, claimant does not own copyright)
- The DMCA notice misidentified your content (wrong URL, wrong work)
- There is a license or authorization that the claimant overlooked

**Do NOT file a counter-notification if:**

- The infringement is undeniable — counter-notification does not resolve liability; it only restores the content while litigation remains possible
- The claimant has already filed suit in federal court (counter-notification is then superseded by litigation)
- You lack US jurisdiction (the perjury statement and consent to federal court jurisdiction have legal weight)

#### Counter-Notification Required Elements (17 USC 512(g)(3))

| #   | Element                         | Requirement                                                                                                                                                                                                                                                                                               |
| --- | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Signature**                   | Physical or electronic signature of subscriber                                                                                                                                                                                                                                                            |
| 2   | **Content Identification**      | Identification of the material removed or disabled, and the location at which it appeared before removal                                                                                                                                                                                                  |
| 3   | **Perjury Statement**           | Statement, under penalty of perjury, that the subscriber has a good faith belief that the material was removed or disabled as a result of mistake or misidentification                                                                                                                                    |
| 4   | **Consent to Jurisdiction**     | Subscriber's name, address, telephone number, AND a statement that the subscriber consents to the jurisdiction of the federal district court for the judicial district in which the subscriber's address is located (or, if outside US, any judicial district in which the service provider may be found) |
| 5   | **Statement to Accept Service** | Statement that subscriber will accept service of process from the person who sent the takedown notice                                                                                                                                                                                                     |

**Note on consent to jurisdiction**: Filing a counter-notification is a significant legal step.
By consenting to US federal court jurisdiction, the alleged infringer agrees to litigate in
the US if the claimant files suit. Consult qualified counsel before filing.

#### Put-Back Timeline (17 USC 512(g)(2))

After receiving a valid counter-notification, the platform must:

1. Forward the counter-notification to the original complainant "promptly"
2. Inform the complainant that the platform will restore the content in **10 to 14 business days**
3. **Restore the content** after 10 business days unless the platform receives notice that the complainant has filed an action seeking a court order to restrain the subscriber from infringing the material

**If complainant files suit**: Content stays down pending litigation (or settlement).

**If complainant does not file suit within 10-14 business days**: Platform must restore content.
Failure to restore exposes the platform to potential liability to the content creator under
512(g)(1) (good faith restoration immunity is lost if platform fails to follow 512(g)(2)).

#### DSA Art. 20 — Internal Complaint Mechanism (EU Equivalent)

DSA Art. 20 requires hosting providers to offer users a free, easy-to-access internal
complaint mechanism for any content moderation decision, including content removals triggered
by Art. 16 notices.

**Key requirements:**

- Platform must handle complaints **in a timely, non-discriminatory, diligent, and non-arbitrary manner**
- Decision must include reasons
- Notifier who submitted the Art. 16 notice also has the right to complain if the platform fails to act
- Art. 21 provides for out-of-court settlement via certified dispute settlement bodies

**Key difference from DMCA**: DSA provides no statutory put-back timeline equivalent. Content
removal/restoration is governed by the platform's own internal processes, subject to DSA
proportionality requirements.

---

### Step 8: Assess 512(f) Misrepresentation Liability

Both rights holders and content creators risk legal exposure for knowingly false representations
in DMCA notices and counter-notifications.

#### 17 USC 512(f) Standard

**Liability for**: Any person who "knowingly materially misrepresents" under 17 USC 512 that:

1. Material or activity is infringing (→ rights holder sending false takedown notice)
2. Material was removed or disabled by mistake or misidentification (→ content creator sending false counter-notification)

**Remedy**: Damages — including actual damages, lost profits, and attorney's fees — incurred
by anyone injured as a result of the service provider's reliance on the misrepresentation.

**Who can be injured**:

- Alleged infringer whose content was wrongly removed
- Copyright owner whose notice the platform disregarded based on counter-notice misrepresentation
- The platform itself (if it incurred costs processing a notice in bad faith)

#### Knowing Misrepresentation — Proof Standard

| Standard                                            | Jurisdiction                | Holding                                                                                                                                                                                       |
| --------------------------------------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Rossi standard** (subjective good faith)          | 9th Cir. 2004 [VERIFY]      | 512(f) requires actual knowledge of falsity, not merely negligence or recklessness; an honest but incorrect belief in infringement does not constitute "knowing" misrepresentation            |
| **Lenz standard** (fair use consideration required) | 9th Cir. 2015/2016 [VERIFY] | Failure to consider fair use constitutes "willful blindness," which can satisfy "knowing" misrepresentation if fair use is obvious; rights holder must analyze fair use before sending notice |

**Circuit split note**: Different circuits may apply different standards. [VERIFY current state of law in relevant jurisdiction before advising on 512(f) exposure.]

#### High-Risk 512(f) Scenarios

| Scenario                                                                                 | Risk Level | Analysis                                                                                                                             |
| ---------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Sending notices for content that is obviously fair use (parody, commentary, short clips) | HIGH       | _Lenz_-style willful blindness claim likely viable if fair use consideration was absent                                              |
| Sending bulk notices without reviewing individual URLs                                   | HIGH       | Misidentification of non-infringing content creates 512(f) exposure; automated mass notices without human review carry elevated risk |
| Claiming ownership of public domain works                                                | HIGH       | Knowing misrepresentation of copyright ownership                                                                                     |
| Claiming copyright in user interface elements or style that are not protectable          | MEDIUM     | Borderline copyright claims may be poor faith if rights holder knows the claim is weak                                               |
| Sending notices based on competitor intelligence to suppress competition                 | HIGH       | DMCA abuse for anti-competitive purposes — both 512(f) and potential antitrust exposure                                              |
| Content creator filing false counter-notification to get content restored                | HIGH       | Perjury exposure + 512(f) liability to original claimant                                                                             |

#### Anti-Abuse Mechanisms and the Lumen Database

- **Lumen Database** (lumendatabase.org): Nonprofit database of DMCA takedown notices and counter-notices submitted to major platforms. Provides transparency; researchers use it to identify patterns of abuse.
- **Notice-and-stay-down**: Some rights holders argue that platforms should keep content down after a valid notice (not just remove once). DMCA text does not require stay-down; EU CDSM Art. 17 imposes an "effective and proportionate" obligation on OCSSPs. [VERIFY current debate status]
- **Section 512 Study**: Copyright Office conducted a study (2020) recommending modest reforms; no major legislative action as of March 2026. [VERIFY current status of DMCA reform proposals]

---

### Step 9: CDSM Directive Art. 17 — OCSSPs (EU Upload Filters)

**Applies only to**: Online Content Sharing Service Providers (OCSSPs) — platforms whose main
purpose or one of their main purposes is to give the public access to a large amount of
copyright-protected content uploaded by users, and that optimise and promote it.

**Does NOT apply to**: Non-profit online encyclopedias, open-source software platforms,
cloud storage services with no public access, B2B software platforms, online marketplaces.

#### Art. 17 Key Obligations

OCSSPs must:

1. **Obtain a license** from rights holders for works uploaded by users (Art. 17(1)). This is the "licensing-first" approach — the OCSSP becomes the primary licensee.

2. **Best efforts to obtain authorization**: If no license available, demonstrate best efforts to obtain one (Art. 17(4)(a)).

3. **Best efforts to ensure unavailability**: Act diligently according to high industry standards to prevent unauthorized content (Art. 17(4)(b)). This is the upload filter obligation — widely implemented via Content ID-type systems.

4. **Best efforts on notice**: After receiving "sufficiently substantiated" notice from rights holders, act expeditiously to disable access or remove notified works (Art. 17(4)(c)). This CDSM Art. 17 notice is distinct from a DSA Art. 16 notice — it triggers upload-filter obligations, not merely individual removal.

5. **Complaint and redress mechanism** (Art. 17(9)): Provide users with an effective and expeditious complaint mechanism; restore content where takedown unjustified; refer unresolved disputes to out-of-court redress or judicial review.

**Interaction with DSA Art. 16**: Art. 17 CDSM is a lex specialis — for OCSSPs, Art. 17 notices and obligations operate alongside (and may supplement) DSA Art. 16 general notice-and-action obligations. The filtering obligation under Art. 17(4)(b) goes beyond the notice-triggered removal model of DSA Art. 16. [VERIFY current guidance from European Commission on CDSM-DSA interaction]

**Key ECJ ruling**: _Poland v. European Parliament and Council_ (C-401/19, July 2022) — ECJ upheld Art. 17 as compatible with freedom of expression, rejecting Poland's challenge; safeguards for users (Art. 17(7) — upload filters must not block lawful uses; Art. 17(9) complaints mechanism) provide adequate protection. [VERIFY]

**Practical compliance**: Platforms qualifying as OCSSPs should implement a licensed content identification system (equivalent to YouTube Content ID) alongside an Art. 16 notice mechanism and Art. 17(9) complaint process.

---

### Step 10: Quality Verification

Before delivering any analysis or draft notice, run the following quality checks.

#### 10a. Citation Quality Gates (5 gates — run silently)

| Gate           | Rule                                                                                                        | Fail Action                         |
| -------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established principle                            | Add citation or mark "[UNVERIFIED]" |
| **Format**     | All citations follow a consistent, recognizable format (e.g., 17 USC 512(c)(3)(A)(i); DSA Art. 16(2)(a))    | Fix format                          |
| **Currency**   | Every cited provision checked for amendments or repeal; DMCA case law checked for current circuit authority | Flag "[CHECK CURRENCY]"             |
| **Domain**     | Analysis stays within the skill's scope (DMCA, DSA, CDSM — not general copyright infringement assessment)   | Remove or flag out-of-scope claims  |
| **Confidence** | Uncertainty explicitly stated, not hidden                                                                   | Add confidence qualifier            |

#### 10b. Self-Interrogation for Critical Findings (3-pass review)

For any finding classified at RED severity (e.g., safe harbor ineligibility, high 512(f) exposure):

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the cited authority? Would a court actually reach this conclusion on these facts?

**Pass 2 — Completeness**: Have all relevant statutory provisions, regulatory guidance, and leading cases been considered? Have recent circuit developments been checked?

**Pass 3 — Challenge**: What is the strongest counter-argument? Under what circumstances might a reasonable attorney disagree with this assessment?

#### 10c. Confidence Scoring

| Level        | Range     | Meaning                                   | Action                                           |
| ------------ | --------- | ----------------------------------------- | ------------------------------------------------ |
| **Definite** | 0.95–1.0  | Settled law; clear statutory text         | State with confidence                            |
| **High**     | 0.80–0.94 | Strong authority; minor circuit questions | State with brief caveat                          |
| **Probable** | 0.60–0.79 | Good arguments; possible variation        | State with reasoning and contra-indicators       |
| **Possible** | 0.40–0.59 | Genuine uncertainty                       | Flag for professional review; present both sides |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                   | Do not assert; flag "[UNCERTAIN]"                |

---

## Severity Classification System

Classify all findings using the following four-tier system:

| Tier            | Label                                                     | Definition                                                                                                                                          | Required Action                                         |
| --------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| 🔴 **CRITICAL** | Safe harbor loss risk; affirmative infringement liability | Missing designated agent; no repeat infringer policy; known infringer not terminated; willful blindness finding likely                              | Immediate remediation; escalate to qualified counsel    |
| 🟠 **RED**      | Significant compliance gap; material legal exposure       | Notice missing required elements; counter-notification defective; 512(f) exposure HIGH; OCSSP Art. 17 non-compliance                                | Remediate before submitting notice or publishing policy |
| 🟡 **YELLOW**   | Suboptimal compliance; moderate risk                      | Notice missing best-practice elements (not all required); policy does not address reinstatement criteria; DSA single point of contact not published | Address in next compliance cycle                        |
| 🟢 **GREEN**    | Compliant; minor improvement opportunities                | Notice fully compliant; policy comprehensive; designated agent registered and current                                                               | Note for awareness; no action required                  |

---

## Prioritization Framework

When multiple compliance gaps exist, address in this order:

**Tier 1 — Foundation (address immediately):**

- Designated DMCA agent registration (without this, no safe harbor available)
- Repeat infringer policy existence (even a basic written policy addresses the "adopted" element)
- Notice processing workflow (no expeditious removal = safe harbor ineligibility)

**Tier 2 — Material compliance (address within 30 days):**

- Repeat infringer policy "reasonable implementation" — enforcement documentation
- Notice review process for 512(f) risk (fair use consideration before sending)
- DSA Art. 16 notice mechanism (if serving EU users)
- DMCA agent renewal check (3-year renewal requirement)

**Tier 3 — Best practice (address within 90 days):**

- Tiered warning system for repeat infringer policy
- Lumen Database transparency reporting
- DSA Art. 20 internal complaint mechanism
- CDSM Art. 17 compliance for OCSSPs

---

## Anti-Patterns

The following are common errors that practitioners must avoid in DMCA/DSA workflows:

1. **Sending notices without considering fair use**: Ignoring _Lenz_ requirement to analyze fair use before sending a DMCA takedown notice. Automated bulk notices with no human fair use review carry the highest 512(f) risk.

2. **Failing to register (or renew) a designated DMCA agent**: The 3-year renewal requirement under 37 CFR Part 201 is frequently overlooked. Lapsed registration = no safe harbor. Search the Copyright Office directory at the start of every compliance audit.

3. **Reinstatement undermines the repeat infringer policy**: _BMG v. Cox_ held that systematically reinstating terminated accounts (Cox reinstated ~95%) defeats "reasonable implementation." If reinstatement policy is too permissive, the entire repeat infringer defense collapses.

4. **Treating 512(f) as toothless**: Many rights holders believe that because _Rossi_ sets a high "actual knowledge of falsity" standard, 512(f) is unenforceable. Post-_Lenz_, failure to consider obvious fair use can satisfy the "knowingly" element. Maintain a documented fair use analysis file.

5. **Not publishing the designated agent on the website**: Even with Copyright Office registration, the platform must also publish the agent's contact information on a publicly accessible website. Failure to publish is a separate compliance gap.

6. **Using category notices instead of URL-specific notices**: Per _Perfect 10 v. CCBill_, notices must be specific enough for the provider to locate the material without piecing together scattered information. "All infringing music on your platform" is not a valid notice.

7. **Confusing DMCA counter-notification with a full defense**: Counter-notification only restores content during the litigation window — it is not a finding that you did not infringe. If the rights holder files suit within 10-14 business days, the content stays down. Filing a counter-notification without assessing litigation exposure is dangerous.

8. **Applying DMCA notice format to DSA notices (and vice versa)**: The six-element DMCA notice format does not map to the four-element DSA Art. 16 format. The DSA requires substantiation of the legal basis for illegality (not just identification of the infringing material) — a pure copyright notice citing "17 USC 107 violation" does not satisfy DSA Art. 16. Build separate notice intake workflows for DMCA and DSA.

9. **Assuming DSA "actual knowledge" equals DMCA "red flag knowledge"**: DSA Art. 6 actual knowledge is deliberately narrower than DMCA's red flag knowledge standard. Platforms that lose DMCA safe harbor for red flag knowledge may retain DSA Art. 6 hosting harbor. Do not conflate the two standards when assessing dual-jurisdiction liability.

10. **Ignoring the OCSSP / Art. 17 distinction**: Platforms that qualify as OCSSPs under CDSM Art. 17 have upload-filter obligations that go beyond DSA Art. 16 notice-and-action. A standard DSA Art. 16 notice mechanism is insufficient for OCSSP compliance — Content ID-equivalent systems are required.

11. **Building a repeat infringer policy for copyright only (ignoring DSA Art. 23)**: Platforms serving EU users must also suspend frequent providers of manifestly illegal content under DSA Art. 23, which covers non-copyright illegal content (hate speech, terrorist content, etc.). Copyright-only repeat infringer policies may be DSA Art. 23 non-compliant.

12. **Failing to send the counter-notification to the original complainant before restoring content**: Under 512(g)(2)(B), the platform must forward the counter-notification to the original complainant and wait the full 10-14 business days before restoring. Restoring content immediately after receiving a counter-notice without waiting forfeits the 512(g) safe harbor.

13. **Missing the DSA enforcement timeline**: DSA became applicable to VLOPs in August 2023, and to all platforms (including non-VLOP intermediaries) in February 2024. Platforms that have not yet implemented DSA Art. 16 notice mechanisms and Art. 20 complaint mechanisms are already non-compliant.

14. **Treating designated agent registration as a one-time event**: The 2017 Copyright Office rule (37 CFR Part 201) requires renewal every 3 years. Platforms registered in 2017-2018 were required to renew in 2020-2021 and again in 2023-2024. Check registration dates.

15. **Using notice-and-takedown to suppress competition or free speech**: Section 512(f) and general abuse of process doctrine provide remedies for weaponized takedown notices. The Lumen Database makes patterns of abuse visible. Courts have awarded attorney's fees in egregious 512(f) cases.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for current case law on DMCA safe harbor (17 USC 512), particularly in the 2d, 4th, and 9th Circuits
- Search for DSA enforcement actions by Digital Services Coordinators (2024-2025)
- Verify current Copyright Office guidance on designated agent registration and renewal
- Search for CDSM Art. 17 guidance from national courts and European Commission
- Save verified legal authority to `/tmp/legalcode-dmca-research.md`

**Without legalcode-mcp:**

- Mark all case citations with [VERIFY]
- Use Copyright Office website (copyright.gov) for designated agent registration guidance
- Use EUR-Lex (eur-lex.europa.eu) for DSA and CDSM Directive text
- Use Lumen Database (lumendatabase.org) for notice practice research
- Proceed with structure and statutory analysis but flag that case law is from memory

---

## Writing Standards

Enforce these standards before delivering any output:

- **Precise legal citation**: Cite specific subsections (17 USC 512(c)(3)(A)(v), not just "DMCA"); cite DSA articles with regulation number (DSA Art. 16, Reg. 2022/2065)
- **Jurisdiction clarity**: Always specify which jurisdiction's law is being applied; never state a jurisdiction-specific rule as universally applicable
- **Active voice in recommendations**: "Register a designated DMCA agent" not "A designated DMCA agent should be registered"
- **Distinguish "CRITICAL" from "RED"**: CRITICAL = safe harbor lost (affects all traffic, all content, all liability); RED = significant gap (affects compliance posture but may be remediable)
- **Flag the [VERIFY] items prominently**: Do not bury [VERIFY] tags in footnotes; they must be visible to the reviewing attorney
- **No DMCA–DSA conflation**: When both regimes apply, address them in separate sections with explicit comparison where needed

---

## Localization Notes

| Jurisdiction    | Key Adaptation                                                                                                                                                                                                                                                                       |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Canada**      | NISA (Notice-and-Notice regime) — ISPs forward notices to subscribers but do not remove content; no counter-notification procedure; Copyright Act RSC 1985 c C-42 ss.41.25-41.26 [VERIFY]                                                                                            |
| **Australia**   | Safe harbor under Copyright Act 1968 ss.116AA-116AJ applies only to carriage service providers; proposed expansion to cover UGC platforms (Copyright Amendment (Online Infringement) Act 2018 and subsequent proposals) [VERIFY current status]                                      |
| **UK**          | s.97A CDPA 1988 (injunctions against service providers); E-Commerce Regulations 2002 (SI 2002/2013) hosting safe harbor survives Brexit; Online Safety Act 2023 adds content moderation obligations (different from DMCA/DSA); no direct UK DSA equivalent as of March 2026 [VERIFY] |
| **Japan**       | Provider Liability Limitation Act 2001 (amended 2021) — DMCA-analogous notice-and-takedown with mandatory response within 7 days; more rights for content creators to demand disclosure of poster identity [VERIFY]                                                                  |
| **South Korea** | Copyright Act Art. 102-104 — OSP safe harbor with designated agent; repeat infringer policy required; notice-and-takedown analogous to DMCA [VERIFY]                                                                                                                                 |

---

## Glass Box Audit Trail

Include this YAML block in any formal output delivered to legal counsel or uploaded to a CLM:

```yaml
glass_box:
  skill_name: "legalcode-dmca-takedown-workflow"
  mode: "Created from scratch — Legalcode original"
  topic: "DMCA 17 USC 512 safe harbor + EU DSA notice-and-action + CDSM Art. 17"
  jurisdiction: "US / EU (with UK and comparative notes)"
  source_skills_analyzed: 0
  enhancement_type: "Create"
  legalcode_mcp: "[Connected / Not connected — fill in at runtime]"
  research_reference_file: "[/tmp/legalcode-dmca-research.md or 'Not created']"
  quality_score: "[X]/40"
  completeness: "18/18 elements"
  citations_verified: "[N VERIFIED] / [N UNVERIFIED — marked [VERIFY]]"
  confidence: "HIGH for statutory analysis; MEDIUM for case law (verify citations before relying)"
  limitations:
    - "DMCA case law evolves rapidly — 2d, 4th, 9th Circuit developments require verification"
    - "DSA enforcement by Digital Services Coordinators is nascent (applicable Feb 2024) — enforcement precedent is limited"
    - "CDSM Art. 17 national implementation varies across EU member states — verify member-state-specific rules"
    - "UK post-Brexit safe harbor position requires verification against current UK government guidance"
    - "Platform-specific policies (YouTube, Meta, etc.) may exceed or differ from statutory minimums"
  reviewer: "AI-assisted — requires review by qualified IP/internet law attorney"
```

---

## Output Format Template

```markdown
# DMCA / DSA Takedown Workflow Analysis

**Date**: [Date]
**Prepared for**: [Client/Platform name]
**User's role**: [Rights Holder / Platform / Content Creator]
**Jurisdictions in scope**: [US / EU / UK / Global]

---

## Executive Summary

[2-4 sentence summary of key findings and recommended actions]

**Critical items requiring immediate attention**: [N]
**Red items requiring prompt remediation**: [N]
**Yellow items for next compliance cycle**: [N]

---

## 1. Safe Harbor Eligibility Assessment

### 1.1 US DMCA (17 USC 512)

| Safe Harbor                   | Applicable?      | Status        | Key Gap(s)              |
| ----------------------------- | ---------------- | ------------- | ----------------------- |
| 512(a) — Transitory           | [Yes/No/Partial] | [🟢/🟡/🟠/🔴] | [description or "None"] |
| 512(b) — Caching              | [Yes/No/Partial] | [🟢/🟡/🟠/🔴] | [description or "None"] |
| 512(c) — Hosting              | [Yes/No/Partial] | [🟢/🟡/🟠/🔴] | [description or "None"] |
| 512(d) — Information Location | [Yes/No/Partial] | [🟢/🟡/🟠/🔴] | [description or "None"] |

### 1.2 EU DSA (Reg. 2022/2065)

| Safe Harbor           | Applicable?      | Status        | Key Gap(s)              |
| --------------------- | ---------------- | ------------- | ----------------------- |
| Art. 4 — Mere Conduit | [Yes/No/Partial] | [🟢/🟡/🟠/🔴] | [description or "None"] |
| Art. 5 — Caching      | [Yes/No/Partial] | [🟢/🟡/🟠/🔴] | [description or "None"] |
| Art. 6 — Hosting      | [Yes/No/Partial] | [🟢/🟡/🟠/🔴] | [description or "None"] |

---

## 2. Notice Analysis

### 2.1 DMCA Takedown Notice Review

| Element                         | Present? | Compliant?    | Issue (if any)       |
| ------------------------------- | -------- | ------------- | -------------------- |
| 1. Signature                    | [Yes/No] | [🟢/🟠/🔴]    | [description or "—"] |
| 2. Work Identification          | [Yes/No] | [🟢/🟡/🟠/🔴] | [description or "—"] |
| 3. Infringing Material Location | [Yes/No] | [🟢/🟡/🟠/🔴] | [description or "—"] |
| 4. Contact Information          | [Yes/No] | [🟢/🟡/🟠/🔴] | [description or "—"] |
| 5. Good Faith Statement         | [Yes/No] | [🟢/🟡/🟠/🔴] | [description or "—"] |
| 6. Perjury Statement            | [Yes/No] | [🟢/🟡/🟠/🔴] | [description or "—"] |

**Fair use consideration documented**: [Yes / No / Not applicable]
**512(f) exposure assessment**: [Low / Medium / High — rationale]

### 2.2 DSA Art. 16 Notice Review (if applicable)

| Element                 | Present? | Compliant?    | Issue (if any)       |
| ----------------------- | -------- | ------------- | -------------------- |
| 1. Legal Substantiation | [Yes/No] | [🟢/🟡/🟠/🔴] | [description or "—"] |
| 2. Precise Location     | [Yes/No] | [🟢/🟡/🟠/🔴] | [description or "—"] |
| 3. Submitter Identity   | [Yes/No] | [🟢/🟡/🟠/🔴] | [description or "—"] |
| 4. Good Faith Statement | [Yes/No] | [🟢/🟡/🟠/🔴] | [description or "—"] |

---

## 3. Designated Agent Status

| Item                                   | Status                                  | Detail                     |
| -------------------------------------- | --------------------------------------- | -------------------------- |
| Copyright Office registration          | [Registered / Not registered / Unknown] | [Registration date or "—"] |
| Renewal required?                      | [Yes / No / Check required]             | [Due date if known]        |
| Published on website                   | [Yes / No]                              | [URL or "—"]               |
| DSA single point of contact designated | [Yes / No / N/A]                        | [Contact info or "—"]      |

---

## 4. Repeat Infringer Policy Assessment

| Element                                  | Status                 | Evidence                                      |
| ---------------------------------------- | ---------------------- | --------------------------------------------- |
| Policy adopted (written)                 | [✅ / ❌ / ⚠️ Partial] | [ToS reference or "Not found"]                |
| Policy published to users                | [✅ / ❌ / ⚠️ Partial] | [Publish location or "Not found"]             |
| Policy reasonably implemented            | [✅ / ❌ / ⚠️ Unclear] | [Enforcement documentation or "Not assessed"] |
| Termination in appropriate circumstances | [✅ / ❌ / ⚠️ Unclear] | [Evidence or "Not assessed"]                  |
| DSA Art. 23 misuse-of-service policy     | [✅ / ❌ / N/A]        | [Status]                                      |

---

## 5. Counter-Notification Assessment (if applicable)

**Counter-notification appropriate**: [Yes / No / Conditional — rationale]
**Risk of litigation if counter-notification filed**: [Low / Medium / High]
**All required elements present**: [Yes / No / Partial — specify missing elements]
**Jurisdiction consent acceptable**: [Yes / No / Review required]

---

## 6. Recommendations

### Priority 1 — Immediate (Critical/Red)

- [ ] [Specific action 1]
- [ ] [Specific action 2]

### Priority 2 — Within 30 Days (Red/Yellow)

- [ ] [Specific action 3]

### Priority 3 — Within 90 Days (Yellow/Green)

- [ ] [Specific action 4]

---

## 7. Confidence and Limitations

[Confidence scoring per section, citing where [VERIFY] tags have been left for attorney review]

---

[Glass Box YAML block as specified above]
```

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis based on:

- Deep legal research via two-agent research pipeline (DMCA + EU DSA dedicated research agents)
- Primary sources: 17 USC 512 (DMCA); DSA Regulation 2022/2065; CDSM Directive 2019/790; 37 CFR Part 201; CDPA 1988 s.97A
- Key case law: _Viacom Int'l v. YouTube_ (2d Cir. 2012); _Lenz v. Universal Music_ (9th Cir. 2015/2016); _BMG Rights Mgmt. v. Cox Communications_ (4th Cir. 2018); _Perfect 10 v. CCBill_ (9th Cir. 2007); _Capitol Records v. Vimeo_ (2d Cir. 2025); _Poland v. European Parliament and Council_ (ECJ C-401/19, 2022)
- Regulatory guidance: Copyright Office Section 512 Study (2020); EDPB Guidelines 3/2025 on DSA-GDPR interplay
- Repository reference standards: `legalcode-contract-review`, `legalcode-copyright-infringement-assessment`
- All case citations marked [VERIFY] — review against authoritative sources before use in legal proceedings
