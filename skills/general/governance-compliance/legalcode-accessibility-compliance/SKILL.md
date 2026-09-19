---
name: legalcode-accessibility-compliance
description: Assesses digital and physical accessibility compliance for websites, mobile apps, software,
  and built environments under the Americans with Disabilities Act Title III (42 U.S.C. §12181 et seq.),
  ADA Title II DOJ Final Rule (April 2024 WCAG 2.1 AA mandate), Section 508 of the Rehabilitation Act
  (29 U.S.C. §794d), WCAG 2.1 and WCAG 2.2 (Level A/AA/AAA), and the EU European Accessibility Act 2025
  (Directive 2019/882 / EN 301 549). Use when assessing a website, app, digital product, or physical premises
  for accessibility compliance; preparing a VPAT (Voluntary Product Accessibility Template) or ACR (Accessibility
  Conformance Report); responding to a demand letter or DOJ complaint; meeting EU EAA June 2025 deadline
  obligations; conducting Section 508 federal procurement assessment; or building an accessibility remediation
  roadmap.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Assesses digital and physical accessibility compliance for websites, mobile apps, software, and built environments under the Americans with Disabilities Act Title III (42 U.S.C. §12181 et seq.), ADA Title II DOJ Final Rule (April 2024 WCAG 2.1 AA mandate), Section 508 of the Rehabilitation Act (29 U.S.C. §794d), WCAG 2.1 and WCAG 2.2 (Level A/AA/AAA), and the EU European Accessibility Act 2025 (Directive 2019/882 / EN 301 549). Covers website and mobile app technical audits, VPAT/ACR documentation, reasonable accommodation analysis, architectural barrier assessment under the ADA 2010 Standards for Accessible Design, and remediation planning with IMMEDIATE/NEAR-TERM/BACKGROUND prioritization. Use when assessing a website, app, digital product, or physical premises for accessibility compliance; preparing a VPAT (Voluntary Product Accessibility Template) or ACR (Accessibility Conformance Report); responding to a demand letter or DOJ complaint; meeting EU EAA June 2025 deadline obligations; conducting Section 508 federal procurement assessment; or building an accessibility remediation roadmap. Also triggers on: ADA Title III, web accessibility audit, WCAG compliance, screen reader compatibility, accessible design, barrier removal, reasonable accommodation, disability discrimination risk, assistive technology, EAA compliance, EN 301 549 assessment.


# Legalcode Accessibility Compliance Assessment

> **Disclaimer**: This skill provides an AI-assisted framework for assessing accessibility
> compliance under the ADA, Section 508, WCAG, and the EU European Accessibility Act. It does
> not constitute legal advice, regulatory guidance, or a compliance certification. Accessibility
> law is rapidly evolving — the DOJ issued its first specific web accessibility rule for Title II
> entities in April 2024, and Title III litigation patterns change frequently. All statutory
> citations, WCAG criteria numbers, regulatory deadlines, and enforcement interpretations should
> be independently verified against current authoritative sources before relying on them. This
> skill does not replace a formal accessibility audit conducted by a qualified accessibility
> specialist, legal counsel licensed in the relevant jurisdiction, or a certified accessibility
> professional (CPACC/WAS). AI-generated legal and technical analysis carries hallucination
> risk — verify all legal authority before acting on it.

---

## Purpose and Scope

This skill assesses an organization's accessibility compliance posture across digital and
physical dimensions, covering the primary US and EU regulatory frameworks.

**Covers:**

- Digital accessibility audit against WCAG 2.1 AA and WCAG 2.2 (Level A and AA criteria)
- ADA Title III application to private-sector websites, mobile apps, and software
- ADA Title II DOJ Final Rule (April 2024) — WCAG 2.1 AA mandate for state/local governments
- Section 508 / ICT accessibility for federal agencies and federal contractors
- VPAT (Voluntary Product Accessibility Template) / ACR (Accessibility Conformance Report) review and drafting
- EU European Accessibility Act 2025 (Directive 2019/882) and EN 301 549 harmonized standard
- Physical accessibility under the 2010 ADA Standards for Accessible Design
- Readily achievable barrier removal analysis for existing facilities
- Reasonable accommodation protocol review (Title I/III interactive process)
- Remediation roadmap with prioritized action items
- Litigation risk assessment and demand letter response framework
- COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY classification

**Does not:**

- Constitute a legally binding WCAG conformance declaration
- Replace a hands-on technical audit with assistive technology (JAWS, NVDA, VoiceOver, TalkBack)
- Provide legal advice on specific litigation exposure or defense strategy
- Cover workplace employment accommodation in full depth (see `legalcode-employee-handbook-review`
  for employment law context)
- Apply exhaustively to air carrier, rail, or telecommunications-specific accessibility regimes
  (Air Carrier Access Act, CVAA, Telecommunications Act §255) — these require separate analysis
- Cover all 50 US state accessibility statutes — focus is federal ADA and EU EAA

**Related skills:**

- `legalcode-compliance-risk-assessment` — general compliance risk assessment framework
- `legalcode-eu-ai-act-high-risk-compliance` — AI Act obligations intersect with accessibility
  for AI-powered products deployed to users with disabilities

---

## Jurisdiction and Governing Law

This skill is **dual-jurisdiction** — covering US federal law and EU law in parallel. Most
organizations with a web presence face obligations under both frameworks.

**US Framework:**

- Americans with Disabilities Act of 1990, Pub. L. 101-336, 42 U.S.C. §§ 12101–12213
  - Title I: Employment (EEOC enforcement)
  - Title II: State and local governments (DOJ enforcement)
  - Title III: Public accommodations and commercial facilities (DOJ + private right of action)
- Rehabilitation Act of 1973, 29 U.S.C. § 794d (Section 508) — federal agencies and contractors
- ADA Standards for Accessible Design (2010 Standards), 28 C.F.R. Part 36 Appendix D
- DOJ Title II Final Rule, 28 C.F.R. Part 35 (published April 24, 2024 — effective June 24, 2024)
  - Mandates WCAG 2.1 Level AA for Title II entities' web content and mobile apps
  - Compliance deadlines: April 24, 2026 (populations ≥50,000); April 24, 2027 (smaller)
- Architectural Barriers Act of 1968, 42 U.S.C. §§ 4151–4157 (federal buildings)

**EU Framework:**

- European Accessibility Act — Directive (EU) 2019/882 of 17 April 2019
  - Application date: June 28, 2025 (products placed on market / services provided after this date)
  - Member state transposition deadline: June 28, 2022
  - Scope: broad range of products and services including e-commerce, banking, transport, telecom
- EN 301 549 v3.2.1 (2021) — Harmonized European Standard for ICT Accessibility
  - Incorporates WCAG 2.1 AA for web and non-web ICT
- Web Accessibility Directive (EU) 2016/2102 — public sector bodies (predates EAA; remains in force)
- SME exemption: microenterprises (< 10 employees AND ≤ €2M turnover) providing **services**
  are exempt from EAA. **No SME exemption for products.**

**International standard (both jurisdictions):**

- WCAG 2.1 (published June 2018) — W3C Recommendation — 78 success criteria (Level A/AA/AAA)
- WCAG 2.2 (published October 2023) — W3C Recommendation — 9 new/modified criteria vs. 2.1
- WCAG 3.0 (AGWG working draft) — in development; not yet an enforceable standard [VERIFY status]

[JURISDICTION-SPECIFIC] Additional jurisdictions to check:

- **Canada**: Accessible Canada Act (S.C. 2019, c. 10) — AODA (Ontario), Manitoba ADA equivalents
- **Australia**: Disability Discrimination Act 1992 + WCAG guidance
- **UK**: Equality Act 2010 s.20 duty to make reasonable adjustments + Public Sector Bodies Accessibility Regulations 2018 [VERIFY post-Brexit EAA alignment status]
- **US State laws**: California Unruh Civil Rights Act (Cal. Civ. Code § 51) creates state-law
  claims that can compound ADA Title III exposure

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses and asks when:

- The answer would materially change the scope or depth of the assessment
- Organization type determines which legal framework applies
- Prior audit findings or pending litigation change the analysis approach
- Scope decisions (digital only, physical only, or both) need user confirmation

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

- **URL(s)**: Website or app URL(s) to assess
- **Audit report**: Existing automated or manual audit results (axe, WAVE, Lighthouse, etc.)
- **VPAT/ACR**: Existing VPAT documentation for review
- **Demand letter / complaint**: DOJ complaint or plaintiff demand letter (respond mode)
- **Facility description**: Physical premises description for barrier removal analysis
- **Scope description**: What needs to be assessed (new product, procurement evaluation, etc.)

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user these questions:

1. **Organization type** — This determines the primary legal framework:
   - Options:
     - **US Federal agency / federal program** → Section 508 is primary; ADA overlaps
     - **US State or local government** → ADA Title II (DOJ Final Rule WCAG 2.1 AA mandate)
     - **US private business (Title III public accommodation)** → ADA Title III + state law
     - **EU-based organization or serving EU consumers** → EAA 2025 + EN 301 549
     - **Both US and EU exposure** → Full dual-jurisdiction assessment
     - **Federal contractor (selling ICT to US government)** → Section 508 + FAR clause
   - _Why this matters_: Different frameworks have different technical standards, deadlines,
     and enforcement mechanisms.

2. **Assessment scope** — What needs to be assessed?
   - Options: Website only, Mobile app only, Website + mobile app, Desktop software / ICT product,
     Physical premises (barrier removal), Full assessment (digital + physical), VPAT/ACR only
   - _Why this matters_: Scope determines which WCAG criteria and physical standards apply.

3. **Assessment purpose** — Why is this assessment being conducted?
   - Options:
     - **Proactive compliance** — determining current posture before any complaint
     - **Litigation response** — responding to a demand letter, DOJ complaint, or filed suit
     - **Procurement / vendor evaluation** — federal/enterprise procurement requiring VPAT
     - **EAA June 2025 deadline compliance** — EU products/services obligation
     - **New product launch** — building in accessibility from the start
     - **Post-remediation verification** — confirming prior deficiencies were fixed
   - _Why this matters_: Litigation response changes priorities; procurement evaluation focuses
     on VPAT completeness; proactive compliance calls for comprehensive gap analysis.

4. **Prior history** — Is there prior accessibility work or claims?
   - Options: No prior audit/assessment, Prior automated audit only (no manual testing),
     Prior full audit (automated + manual), Prior demand letter or DOJ complaint,
     Consent decree or settlement agreement in place
   - _Why this matters_: A consent decree creates legally binding remediation obligations;
     prior notice of deficiencies affects litigation posture.

5. **Deadline or compliance date**:
   - Options: Immediate (responding to complaint), Short-term (EAA June 2025 deadline),
     Medium-term (DOJ Title II April 2026/2027 deadline), Long-term (no immediate deadline),
     Procurement deadline (specify date)
   - _Why this matters_: Affects remediation sequencing and prioritization.

If the user provides partial context, proceed with stated assumptions and flag them explicitly.

### Step 3: Determine Applicable Framework and Standard

Based on the context gathered in Step 2, identify the primary applicable framework and
the technical standard that governs the assessment:

| Organization Type               | Primary Framework                     | Technical Standard                                       | Enforcement                       |
| ------------------------------- | ------------------------------------- | -------------------------------------------------------- | --------------------------------- |
| US Federal agency               | Section 508 (29 U.S.C. § 794d)        | WCAG 2.0 AA (2017 Standards) [VERIFY pending 2.1 update] | DOJ / agency IG                   |
| US Federal contractor (ICT)     | Section 508 + FAR 52.239-2            | WCAG 2.0 AA                                              | Contracting officer / GAO protest |
| US State/local government       | ADA Title II + DOJ Final Rule (2024)  | WCAG 2.1 AA                                              | DOJ + private right of action     |
| US private business (Title III) | ADA Title III + state law             | WCAG 2.1 AA (de facto; no final rule)                    | Private litigation + DOJ          |
| EU organization (EAA scope)     | Directive 2019/882 + EN 301 549       | WCAG 2.1 AA (via EN 301 549)                             | Member state authority            |
| EU public sector                | Web Accessibility Directive 2016/2102 | WCAG 2.1 AA (EN 301 549 v3.2.1)                          | Member state                      |

**⟁ CLARIFY** — If the organization faces both US Title III and EU EAA exposure, confirm:

- Should the assessment cover WCAG 2.2 criteria (in addition to 2.1)? WCAG 2.2 is not yet
  mandated by any regulation but represents best practice and future-proofing.
- Does the EU exposure include EN 301 549's non-web ICT requirements (native mobile apps,
  desktop software, documents), or web-only?

### Step 4: Digital Accessibility Audit

Assess the website, app, or digital product against the applicable WCAG standard.

**⟁ CLARIFY** — For large digital estates (multiple sites, mobile apps, enterprise software):

- Ask whether to assess **all digital properties** or a **representative sample**
  (homepage, checkout flow, login, key user journeys)
- Ask whether the user has existing automated scan results to incorporate, or needs a
  prompt-based architecture review only

#### WCAG 2.1 / 2.2 Core Criteria Assessment Framework

Assess against the four POUR principles and their success criteria:

---

**PRINCIPLE 1 — PERCEIVABLE**: Information and UI components must be presentable to users
in ways they can perceive.

| SC #   | Criterion                                             | Level | Common Issue                                                     |
| ------ | ----------------------------------------------------- | ----- | ---------------------------------------------------------------- |
| 1.1.1  | Non-text Content                                      | A     | Missing alt text on images, icons, CAPTCHAs                      |
| 1.2.1  | Audio-only and Video-only (Pre-recorded)              | A     | No transcript for audio; no description for silent video         |
| 1.2.2  | Captions (Pre-recorded)                               | A     | Missing or auto-generated-only captions                          |
| 1.2.3  | Audio Description or Media Alternative (Pre-recorded) | A     | No audio description for video with visual-only information      |
| 1.2.4  | Captions (Live)                                       | AA    | No live captions for real-time video/webinars                    |
| 1.2.5  | Audio Description (Pre-recorded)                      | AA    | No audio description track for pre-recorded video                |
| 1.3.1  | Info and Relationships                                | A     | Form fields not programmatically associated with labels          |
| 1.3.2  | Meaningful Sequence                                   | A     | Reading order in DOM doesn't match visual order                  |
| 1.3.3  | Sensory Characteristics                               | A     | Instructions rely on shape/color/location alone                  |
| 1.3.4  | Orientation                                           | AA    | Page/app locked to portrait or landscape only                    |
| 1.3.5  | Identify Input Purpose                                | AA    | Missing autocomplete attributes on personal data fields          |
| 1.4.1  | Use of Color                                          | A     | Color alone conveys information (error states, charts)           |
| 1.4.2  | Audio Control                                         | A     | Auto-playing audio with no pause/stop/mute control               |
| 1.4.3  | Contrast (Minimum)                                    | AA    | Text contrast ratio < 4.5:1 (< 3:1 for large text)               |
| 1.4.4  | Resize Text                                           | AA    | Text unreadable or layout breaks at 200% zoom                    |
| 1.4.5  | Images of Text                                        | AA    | Text rendered as images where CSS text could be used             |
| 1.4.10 | Reflow                                                | AA    | Content doesn't reflow at 400% zoom (320 CSS px width)           |
| 1.4.11 | Non-text Contrast                                     | AA    | UI components/graphics < 3:1 contrast against adjacent color     |
| 1.4.12 | Text Spacing                                          | AA    | Layout breaks when letter/word/line spacing is overridden        |
| 1.4.13 | Content on Hover or Focus                             | AA    | Tooltips/hover content not dismissible, persistent, or hoverable |

---

**PRINCIPLE 2 — OPERABLE**: UI components and navigation must be operable.

| SC #   | Criterion                                  | Level | Common Issue                                                             |
| ------ | ------------------------------------------ | ----- | ------------------------------------------------------------------------ |
| 2.1.1  | Keyboard                                   | A     | Interactive elements not reachable by keyboard alone                     |
| 2.1.2  | No Keyboard Trap                           | A     | Keyboard focus trapped in modal or widget                                |
| 2.1.4  | Character Key Shortcuts                    | A     | Single-key shortcuts active when not focused on component                |
| 2.2.1  | Timing Adjustable                          | A     | Session timeout < 20-hour or no warning/extension                        |
| 2.2.2  | Pause, Stop, Hide                          | A     | Auto-updating/moving content with no pause control                       |
| 2.3.1  | Three Flashes or Below Threshold           | A     | Content flashing > 3 times/second (seizure risk)                         |
| 2.4.1  | Bypass Blocks                              | A     | No skip navigation link to bypass repeated header                        |
| 2.4.2  | Page Titled                                | A     | Pages lack descriptive, unique titles                                    |
| 2.4.3  | Focus Order                                | A     | Keyboard focus order doesn't follow logical sequence                     |
| 2.4.4  | Link Purpose (In Context)                  | A     | "Click here" / "Read more" links with no context                         |
| 2.4.5  | Multiple Ways                              | AA    | Only one way to find pages (no search, sitemap, or navigation)           |
| 2.4.6  | Headings and Labels                        | AA    | Headings don't describe topic; form labels absent                        |
| 2.4.7  | Focus Visible                              | AA    | Keyboard focus indicator not visible                                     |
| 2.4.11 | Focus Not Obscured (Minimum) _(WCAG 2.2)_  | AA    | Focused component entirely hidden by sticky header/footer                |
| 2.4.12 | Focus Not Obscured (Enhanced) _(WCAG 2.2)_ | AAA   | Focused component partially obscured                                     |
| 2.5.1  | Pointer Gestures                           | A     | Multipoint/path-based gestures with no single-pointer alternative        |
| 2.5.2  | Pointer Cancellation                       | A     | Down-event triggers action with no up-event cancellation                 |
| 2.5.3  | Label in Name                              | A     | Visible label text absent from accessible name                           |
| 2.5.4  | Motion Actuation                           | A     | Device motion required with no alternative                               |
| 2.5.7  | Dragging Movements _(WCAG 2.2)_            | AA    | Drag operations (sliders, reordering) with no single-pointer alternative |
| 2.5.8  | Target Size (Minimum) _(WCAG 2.2)_         | AA    | Touch/click targets < 24×24 CSS pixels without spacing                   |

---

**PRINCIPLE 3 — UNDERSTANDABLE**: Information and operation of UI must be understandable.

| SC #  | Criterion                                        | Level | Common Issue                                                                        |
| ----- | ------------------------------------------------ | ----- | ----------------------------------------------------------------------------------- |
| 3.1.1 | Language of Page                                 | A     | `lang` attribute missing or wrong on `<html>` element                               |
| 3.1.2 | Language of Parts                                | AA    | Language changes within page not marked with `lang` attribute                       |
| 3.2.1 | On Focus                                         | A     | Unexpected context change on receiving focus                                        |
| 3.2.2 | On Input                                         | A     | Unexpected context change when changing form field value                            |
| 3.2.3 | Consistent Navigation                            | AA    | Navigation in different order across pages                                          |
| 3.2.4 | Consistent Identification                        | AA    | Same-function components identified differently across pages                        |
| 3.2.6 | Consistent Help _(WCAG 2.2)_                     | A     | Help mechanisms not in consistent location                                          |
| 3.3.1 | Error Identification                             | A     | Input errors described only by color or not described at all                        |
| 3.3.2 | Labels or Instructions                           | A     | Form fields lack labels or instructions for required format                         |
| 3.3.3 | Error Suggestion                                 | AA    | Error messages don't suggest how to correct the error                               |
| 3.3.4 | Error Prevention (Legal, Financial, Data)        | AA    | No confirmation or reversal for legal/financial submissions                         |
| 3.3.7 | Redundant Entry _(WCAG 2.2)_                     | A     | Previously entered information re-requested in same session                         |
| 3.3.8 | Accessible Authentication (Minimum) _(WCAG 2.2)_ | AA    | Authentication requires cognitive function test (puzzle/memory) with no alternative |

---

**PRINCIPLE 4 — ROBUST**: Content must be robust enough to be interpreted by assistive technologies.

| SC #  | Criterion         | Level | Common Issue                                                                                                  |
| ----- | ----------------- | ----- | ------------------------------------------------------------------------------------------------------------- |
| 4.1.1 | Parsing           | A     | Duplicate IDs; invalid HTML causing AT parsing errors [Note: obsolete in WCAG 2.2 — marked obsolete Oct 2023] |
| 4.1.2 | Name, Role, Value | A     | Custom widgets missing ARIA roles/states/properties; buttons implemented as `<div>`                           |
| 4.1.3 | Status Messages   | AA    | Status messages (success/error) not announced to screen readers                                               |

---

#### WCAG 2.2 New Criteria Summary

WCAG 2.2 (October 2023) added 9 new success criteria. The following are Level AA (enforceable
under frameworks requiring 2.2 AA) and are commonly missed:

| SC #   | Criterion                            | Level | Key Requirement                                         |
| ------ | ------------------------------------ | ----- | ------------------------------------------------------- |
| 2.4.11 | Focus Not Obscured (Minimum)         | AA    | Focused element not entirely hidden by sticky elements  |
| 2.4.12 | Focus Not Obscured (Enhanced)        | AAA   | Focused element not partially hidden                    |
| 2.5.7  | Dragging Movements                   | AA    | All drag operations have single-pointer alternative     |
| 2.5.8  | Target Size (Minimum)                | AA    | Targets ≥ 24×24 CSS px or have sufficient spacing       |
| 3.2.6  | Consistent Help                      | A     | Help mechanisms in consistent location                  |
| 3.3.7  | Redundant Entry                      | A     | No duplicate data entry required in same session        |
| 3.3.8  | Accessible Authentication (Minimum)  | AA    | No cognitive test in authentication without alternative |
| 3.3.9  | Accessible Authentication (Enhanced) | AAA   | No cognitive test in authentication at all              |

SC 4.1.1 (Parsing) was **deprecated/made obsolete** in WCAG 2.2 — do not flag as a current
violation under frameworks requiring WCAG 2.2 compliance.

---

### Step 5: Section 508 / ICT Assessment (Federal Scope)

For federal agencies, federal contractors, and vendors supplying ICT to the US government,
apply the additional Section 508 / ICT assessment:

**Scope of Section 508 ICT requirements:**

- Web-based information and applications
- Software applications and operating systems
- Telecommunications products
- Video and multimedia products
- Kiosks and transaction machines
- Electronic documents (PDF, Word, Excel)
- Hardware with information display or input

**VPAT / Accessibility Conformance Report (ACR):**

Review or produce a VPAT using the current template (VPAT 2.5, issued by ITI):

| VPAT Chapter | Standard                   | Product Types Covered        |
| ------------ | -------------------------- | ---------------------------- |
| Chapter 1    | Section 508 (revised 2017) | All federal ICT              |
| Chapter 2    | W3C WCAG 2.x               | Web and non-web ICT          |
| Chapter 3    | EN 301 549 (EU harmonized) | EU market / dual procurement |

**VPAT conformance notation:**

- **Supports**: Product supports the criterion without exception
- **Partially Supports**: Supports criterion but with some exceptions
- **Does Not Support**: Majority of functionality does not support the criterion
- **Not Applicable**: Criterion is not relevant to the product
- **Not Evaluated**: Criterion has not been evaluated

**⟁ CLARIFY** — For VPAT drafting or review:

- Is this a new VPAT or updating an existing one?
- Which VPAT edition is the procurement requiring (VPAT 2.5, earlier version, specific chapter)?
- Does the procurement require EN 301 549 (Chapter 3) in addition to Section 508?

**Section 508 critical assessment points:**

- [ ] Each WCAG 2.0 AA criterion addressed (or noted as N/A with explanation)
- [ ] Remarks and Explanations column populated for every "Partially Supports" or "Does Not Support"
- [ ] Non-web ICT criteria (Chapter 5–9 of EN 301 549) addressed for applicable product types
- [ ] Accessibility support contact information included
- [ ] Date of last evaluation disclosed
- [ ] Evaluation methodology (automated + manual) described

### Step 6: EU European Accessibility Act (EAA) Assessment

For organizations with EU market presence, assess compliance with Directive 2019/882 and
EN 301 549.

**EAA scope — products:**

- General purpose hardware (computers, smartphones, tablets)
- Payment terminals and ATMs
- Ticketing machines and check-in kiosks
- Interactive self-service terminals
- Consumer equipment with interactive capability (TV set-top boxes)
- E-readers

**EAA scope — services:**

- Electronic communications services
- Audiovisual media services (video streaming, OTT)
- Air/bus/rail/waterborne passenger transport services (transport service websites, apps, tickets)
- Banking services (consumer banking, payment cards, online banking)
- E-books and dedicated software
- **E-commerce** (websites/apps for online sale of products/services) — broad scope
- Services based on mobile devices

**EAA exclusions and exemptions:**

- Microenterprises providing **services** (< 10 employees AND ≤ €2M annual turnover) — full exemption
- **No exemption for products** (any size organization)
- Fundamental alteration / disproportionate burden exception available (must document annually)

**EAA enforcement (from June 28, 2025):**

- Market surveillance authorities in each member state enforce product requirements
- Designated authorities enforce service requirements
- Complaints can be filed by individuals, NGOs, and representative organizations
- Member state penalties vary — [JURISDICTION-SPECIFIC] check local implementing legislation

**EN 301 549 v3.2.1 key alignment with WCAG:**

- Chapter 9: Web — aligns with WCAG 2.1 AA
- Chapter 10: Non-web documents — WCAG 2.1 AA with adaptations
- Chapter 11: Non-web software — WCAG 2.1 AA with adaptations
- Chapter 12: ICT with two-way voice communication
- Chapter 13: ICT providing relay or emergency service access

**⟁ CLARIFY** — For EAA assessment:

- Does the organization provide services, products, or both (affects exemption analysis)?
- Does the organization qualify for the microenterprise services exemption?
- Has the organization assessed whether fundamental alteration or disproportionate burden
  applies to specific requirements? (Must be documented and updated annually)

### Step 7: Physical Accessibility Assessment (ADA Barrier Removal)

For assessments involving physical premises, assess compliance with the 2010 ADA Standards
for Accessible Design (28 C.F.R. Part 36 Appendix D).

**Readily achievable barrier removal obligation (Title III existing facilities):**
Title III public accommodations must remove architectural barriers that are "readily achievable"
(easily accomplishable and able to be carried out without much difficulty or expense).

**Priority order for barrier removal** (DOJ guidance):

1. **Access into the place of business** (parking, accessible route, entrance)
2. **Access to areas where goods/services are provided** (sales counters, service areas)
3. **Access to restrooms** (if available to public)
4. **Other barrier removal** (water fountains, phones, signage)

**Common architectural barriers to assess:**

_Exterior / Site Access:_

- [ ] Accessible parking spaces (ratio: 1 per 25 total, van-accessible spaces) — §208
- [ ] Accessible route from parking to entrance — §402 (36 in. min. width, < 5% running slope)
- [ ] Curb cuts where route crosses curb — §406
- [ ] Accessible route from public transportation stops — §402
- [ ] Entrance: 32 in. min. clear width, threshold ≤ 0.75 in. — §404
- [ ] Hardware: lever or push/pull (not round knobs) — §404.2.7

_Interior Access:_

- [ ] Accessible route throughout the accessible portions — §402
- [ ] Elevators required in multi-story buildings (threshold applies to new construction) — §206.2.3
- [ ] Counter heights: service counters ≤ 36 in. or 28 in. section — §904.4
- [ ] Aisle widths: 36 in. minimum clear — §403.5

_Restrooms:_

- [ ] Accessible route to restrooms — §206.2.4
- [ ] Turning space: 60-in. diameter or T-shaped — §603.2
- [ ] Accessible stall dimensions: 60 × 56 in. minimum — §604.8
- [ ] Grab bars: side and rear at toilet — §604.5
- [ ] Lavatory height: ≤ 34 in. to top surface — §606
- [ ] Faucet controls: push/lever/automatic (no tight grasping) — §606.4

_Other Facility Elements:_

- [ ] Signage: raised characters + Braille on permanent rooms — §703
- [ ] Accessible seating in assembly areas: dispersal requirement — §221
- [ ] Service animals: written policy permitting entry — non-physical requirement

**New construction and alterations** (Title III): Must comply with all ADA Standards; no
"readily achievable" limitation applies. Alterations to primary function areas trigger path
of travel requirements (up to 20% of alteration cost). — §202.4

[JURISDICTION-SPECIFIC] Note: Some jurisdictions (California, New York) have state accessibility
standards that are stricter than federal ADA Standards. Check state building codes. California
CBC Chapter 11B imposes additional requirements beyond ADA. [VERIFY current CBC edition]

### Step 8: Reasonable Accommodation Protocol Review

Review the organization's reasonable accommodation process for persons with disabilities.

**Title III public accommodation obligations (digital context):**

- Provide **effective communication** using accessible formats (28 C.F.R. § 36.303)
- Modify policies, practices, and procedures to provide equal access (28 C.F.R. § 36.302)
- Remove barriers as required (28 C.F.R. § 36.304)

**Effective communication alternatives when digital access fails:**

- Live telephone assistance (human agent, not IVR) for screen-reader-inaccessible processes
- Text relay services (711) and video relay services (for Deaf users)
- In-person service if digital channel is inaccessible
- Accessible alternative formats: large print, audio, Braille, electronic text

**Protocol checklist:**

- [ ] Organization has a documented process for receiving and responding to accessibility requests
- [ ] Accessible feedback mechanism for reporting accessibility barriers (e.g., accessibility@)
- [ ] Response time SLA defined (best practice: 1–2 business days)
- [ ] Alternative access methods documented and operational (not theoretical)
- [ ] Staff trained to handle accessibility requests without deferring to automated systems
- [ ] Accessibility statement published (URL, conformance level, known limitations, contact info)
- [ ] Commitment to ongoing monitoring and remediation documented

### Step 9: Classify Findings

Classify each accessibility finding using the four-tier system:

#### COMPLIANT

The site, app, or facility meets the applicable standard for this criterion. No action needed.

#### PARTIAL

The site, app, or facility partially meets the criterion. Deficiencies exist but fundamental
accessibility is not entirely blocked for the functional area.

**Examples:**

- Alt text present on most images but missing on a non-critical icon set
- Keyboard access available but focus indicator barely visible (fails contrast threshold)
- Accessible entrance exists but lacks directional signage from the parking lot
- VPAT covers WCAG 2.0 criteria but has not been updated to WCAG 2.1

**Action**: Document the specific gaps. Assign to NEAR-TERM remediation queue.

#### NON-COMPLIANT

The site, app, or facility fails to meet the criterion. The barrier materially impairs
access for users with the relevant disability.

**Examples:**

- Core transaction flow (checkout, form submission, login) not keyboard-operable
- Required form fields have no labels — screen reader users cannot complete the form
- Video content has no captions — Deaf users cannot access the information
- No accessible entrance to the facility
- Authentication requires solving a visual puzzle with no audio or text alternative (SC 3.3.8)

**Action**: Document specific failure, user impact, and proposed fix. Assign to IMMEDIATE
or NEAR-TERM queue based on criticality and litigation exposure.

#### CRITICAL DEFICIENCY

The finding creates immediate, material litigation risk, or represents a complete barrier to
access for an entire user population. Warrants immediate escalation to counsel.

**Examples:**

- Entire website is Flash-based or image-only with no accessible alternative (complete barrier)
- Primary service delivery channel (e.g., online application, patient portal) is inaccessible
- Active DOJ complaint or demand letter on the specific deficiency that remains unremediated
- New construction or alterations that fail ADA Standards (triggering legal violations, not
  just "readily achievable" standard)
- Serial plaintiff targeting pattern: site was previously audited and issues not remediated

**Action**: Escalate immediately. Implement emergency remediation or provide accessible
alternative channel. Do not issue a WCAG conformance claim until remediated.

---

## Severity-to-Remediation Priority Mapping

| Classification                          | Litigation Risk | Remediation Priority                                               |
| --------------------------------------- | --------------- | ------------------------------------------------------------------ |
| CRITICAL DEFICIENCY                     | Very High       | **IMMEDIATE** — within 30 days or faster if demand letter received |
| NON-COMPLIANT (core user journeys)      | High            | **IMMEDIATE** — within 60-90 days                                  |
| NON-COMPLIANT (secondary functionality) | Moderate        | **NEAR-TERM** — within 6 months                                    |
| PARTIAL                                 | Low-Moderate    | **NEAR-TERM** — within 6–12 months                                 |
| COMPLIANT                               | None            | **BACKGROUND** — maintain and retest on major releases             |

---

## Prioritization Framework

### Tier 1 — IMMEDIATE (Deal-Breakers / Litigation-Triggering)

Deficiencies that create the highest legal risk or block fundamental access:

- Inaccessible primary user journeys (purchase, application, account management, information access)
- Complete absence of captions on video (SC 1.2.2) — most-litigated criterion
- Non-keyboard-operable core functionality (SC 2.1.1)
- Login/authentication that excludes users with cognitive disabilities (SC 3.3.8 — WCAG 2.2)
- Complete absence of alt text on meaningful images in primary content
- ADA-non-compliant physical entrance or inaccessible primary service area
- Unfixed deficiencies after prior notice (demand letter, prior audit)

### Tier 2 — NEAR-TERM (Material Gaps)

Deficiencies that impair access but do not entirely block functionality:

- Insufficient color contrast on primary text (SC 1.4.3) — second most-litigated criterion
- Missing form labels (SC 1.3.1 / 3.3.2)
- Auto-playing media without controls (SC 1.4.2)
- Session timeouts without warning or extension (SC 2.2.1)
- Missing skip navigation (SC 2.4.1)
- Accessible alternative formats not operationally available (documented but broken)
- VPAT not updated within past 12 months for actively marketed products

### Tier 3 — BACKGROUND (Good Practice / Future-Proofing)

Items that represent best practice but are lower litigation risk:

- WCAG 2.2-specific criteria (2.4.11, 2.5.7, 2.5.8, 3.3.7, 3.3.8) where WCAG 2.1 is the current mandate
- AAA-level criteria (not legally required under any current framework, but beneficial)
- Minor wording improvements to accessibility statement
- Enhanced accessible authentication (SC 3.3.9 — AAA)
- Discretionary signage improvements beyond ADA minimums
- Third-party widget accessibility issues (while notifying vendor)

---

## Remediation Planning

### Remediation Record Template

For each NON-COMPLIANT or CRITICAL finding, create a remediation record:

```
Finding ID: [ACC-001]
Standard: [WCAG 2.1 SC 1.4.3 / ADA Title III / Section 508 / EAA Art. 5]
Criterion: [Contrast (Minimum)]
Classification: [NON-COMPLIANT]
Priority: [IMMEDIATE / NEAR-TERM / BACKGROUND]
Scope: [All body text on example.com homepage — 14px Inter font on #F0F0F0 background]
Contrast ratio measured: [2.8:1]
Required ratio: [4.5:1 for normal text; 3:1 for large text ≥ 18pt or 14pt bold]
User impact: [Low-vision users cannot read body text. Affects ~8% of users with low vision.]
Root cause: [CSS background color #F0F0F0 with font color #888888 — insufficient contrast]
Proposed fix: [Change font color to #595959 (5.1:1 ratio) or #767676 (4.54:1 — minimum pass)]
Verification test: [Retest with axe + manual check using browser contrast analyzer]
Responsible team: [Front-end engineering]
Target completion: [2026-04-15]
Completed: [ ]
```

### Remediation Approach by Barrier Type

| Barrier Type                    | Typical Fix                              | Complexity | Timeline          |
| ------------------------------- | ---------------------------------------- | ---------- | ----------------- |
| Missing alt text                | Content / CMS update                     | Low        | Days              |
| Missing form labels             | HTML attribute addition                  | Low        | Days              |
| Low contrast                    | CSS color change                         | Low        | Days              |
| Missing captions                | Caption file (SRT) creation + attachment | Medium     | 1–4 weeks         |
| Keyboard trap                   | JavaScript event handler fix             | Medium     | 1–4 weeks         |
| Non-keyboard-operable widget    | ARIA + keyboard event refactor           | High       | 1–8 weeks         |
| Inaccessible PDF                | PDF remediation (tagging/structure)      | Medium     | 1–2 weeks per doc |
| Inaccessible third-party widget | Vendor remediation or replacement        | High       | Depends on vendor |
| Physical barrier (minor)        | Hardware swap (lever handle, etc.)       | Low        | Days–weeks        |
| Physical barrier (construction) | Contractor scope + permitting            | High       | Months            |

---

## Litigation Risk Assessment (US ADA Title III)

When the assessment is triggered by or may lead to litigation, assess the litigation risk profile:

### Serial Plaintiff Indicators

High-litigation-risk indicators to document:

- [ ] Site has received prior demand letter(s) from accessibility plaintiffs
- [ ] Known serial plaintiff firms have sent demand letters to peers in the same industry
- [ ] The organization's industry is a frequent target (retail, hospitality, restaurant chains, financial services, healthcare portals)
- [ ] Site was audited previously and known deficiencies were not remediated within a reasonable period
- [ ] Automated scans show clear, easily-fixed violations left unaddressed for 12+ months

### Key ADA Title III Digital Accessibility Case Law [VERIFY all citations]

- _Robles v. Domino's Pizza LLC_, 913 F.3d 898 (9th Cir. 2019) — ADA applies to websites of
  public accommodations with a physical nexus; WCAG 2.0 can be a reasonable technical standard
- _Gil v. Winn-Dixie Stores_, 242 F. Supp. 3d 1315 (S.D. Fla. 2017), rev'd in part on other
  grounds, 993 F.3d 1266 (11th Cir. 2021) — first circuit-level ruling on web accessibility;
  Eleventh Circuit vacated injunction on standing grounds but did not reject ADA applicability
- _Nat'l Fed'n of the Blind v. Scribd Inc._, 97 F. Supp. 3d 565 (D. Vt. 2015) — WCAG
  compliance can constitute effective communication
- _Access Now, Inc. v. Southwest Airlines_, 227 F. Supp. 2d 1312 (S.D. Fla. 2002) — early
  ruling holding ADA does not apply to websites with no nexus to physical location (minority view)

**Circuit split on "nexus" requirement:** The 9th Circuit (Robles) holds ADA applies where
there is a nexus between the website and a physical location. Other circuits and district courts
vary. [VERIFY current state of circuit split — further developments expected]

**California Unruh Act (Cal. Civ. Code § 51):** Provides independent state-law claim parallel
to ADA Title III, with statutory damages of $4,000 per violation per visit — significant
exposure multiplier in CA.

### Defenses to Consider [VERIFY with counsel]

- **No nexus to physical place**: Website-only businesses in certain circuits
- **Undue burden**: Modification would fundamentally alter or create undue financial burden
  (must document and provide accessible alternative)
- **Effective alternative access**: An accessible alternative channel is available and operational
  (not theoretical)
- **Mootness**: Violation remediated before or during litigation
- **Statute of limitations**: Two-year statute in most federal circuits; California has 3-year
  Unruh Act window

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                       | Fail Action                                              |
| -------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, WCAG SC, or established principle                  | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All WCAG SC citations include number, name, and level (e.g., "SC 1.4.3 Contrast (Minimum) — Level AA")     | Fix format                                               |
| **Currency**   | Verify WCAG version, regulatory deadlines, and case citations are current                                  | Flag "[CHECK CURRENCY — may have changed]"               |
| **Domain**     | Analysis stays within the stated jurisdiction(s). No US-only conclusions applied to EU scope or vice versa | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden. If uncertain about a legal position, flag with [VERIFY]         | Add confidence qualifier                                 |

### Self-Interrogation for CRITICAL DEFICIENCY Items

For any finding classified CRITICAL DEFICIENCY, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the
statute/case law cited? Would a court or regulator actually find liability on these facts?
Is the nexus to a protected class of disability and the relevant digital/physical standard clear?

**Pass 2 — Completeness**: Have all applicable frameworks been checked? For a US entity:
have both ADA and state law been considered? Is the WCAG version correct for the applicable
framework? Has the EU EAA been checked if the organization has EU market presence?

**Pass 3 — Challenge**: What is the strongest defense against this finding? Is the accessible
alternative channel genuinely operational? Does the "nexus" requirement limit exposure in
this jurisdiction? Is the litigation exposure proportionate to the stated deficiency?

If any pass reveals a weakness, revise before delivery. Mark audit trail with
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                                   | Action                                                |
| ------------ | --------- | --------------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | WCAG criterion violation is unambiguous; statute is clear | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong authority; minor edge cases                        | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments but competing interpretations              | State with reasoning and contra-indicators            |
| **Possible** | 0.40–0.59 | Genuinely uncertain (e.g., unsettled circuit split)       | Flag for counsel review with both sides               |
| **Unlikely** | 0.0–0.39  | Weak basis or speculative                                 | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every accessibility assessment output MUST include this audit section:

```yaml
glass_box:
  skill: "legalcode-accessibility-compliance"
  organization: "[Organization name or 'Not provided']"
  assessment_scope: "[Website / Mobile app / Desktop software / Physical facility / Full]"
  organization_type: "[Federal agency / State/local gov / Private Title III / EU EAA]"
  assessment_purpose: "[Proactive / Litigation response / Procurement / EAA deadline / Launch]"
  primary_standard: "[WCAG 2.1 AA / WCAG 2.2 AA / Section 508 / EN 301 549 / ADA 2010 Standards]"
  secondary_standards: "[List any additional applicable frameworks]"
  wcag_version_used: "2.1 / 2.2 / both"
  criteria_assessed: "[Number of WCAG criteria assessed]"
  criteria_compliant: "[Number]"
  criteria_partial: "[Number]"
  criteria_non_compliant: "[Number]"
  critical_deficiencies: "[Number]"
  legalcode_mcp: "Connected / Not connected"
  external_audit_incorporated: "[axe report / WAVE report / Lighthouse / Manual / None]"
  statutes_cited:
    - "42 U.S.C. §§ 12181-12189 (ADA Title III) — UNVERIFIED"
    - "29 U.S.C. § 794d (Section 508) — UNVERIFIED"
    - "Directive (EU) 2019/882 (EAA) — UNVERIFIED"
  case_law_cited:
    - "Robles v. Domino's Pizza, 913 F.3d 898 (9th Cir. 2019) — UNVERIFIED"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL DEFICIENCY items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "Prompt-based assessment only — no automated scanning or assistive technology testing performed"
    - "Physical barrier assessment based on description only — on-site measurement not performed"
    - "[Any additional scope limitations]"
  reviewer: "AI-assisted — requires qualified accessibility specialist and legal review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in accessibility compliance assessment:

1. **Equating automated scan results with WCAG conformance** — Automated tools (axe, WAVE,
   Lighthouse) detect approximately 30–40% of WCAG failures. A passing automated scan does not
   mean WCAG conformance. Manual testing with keyboard and screen readers is required for a
   meaningful conformance assessment.

2. **Confusing WCAG levels** — Recommending AAA compliance when AA is required, or accepting
   partial A compliance as "WCAG compliant." Only Level A + AA together constitute the "WCAG
   2.x AA" standard referenced in law.

3. **Applying the Title II DOJ Final Rule to private-sector entities** — The April 2024 DOJ rule
   mandating WCAG 2.1 AA with a specific compliance deadline applies only to Title II entities
   (state and local governments). Title III private-sector entities face no equivalent final rule
   — though WCAG 2.1 AA is the de facto standard for litigation.

4. **Assuming the EAA only affects large enterprises** — SME exemption covers microenterprises
   providing _services_ (< 10 employees AND ≤ €2M turnover). Products have no size exemption.
   An 8-person startup selling consumer hardware in the EU must comply with EAA product requirements.

5. **Treating VPAT as a compliance certification** — A VPAT is a vendor self-assessment disclosure,
   not a certification. A VPAT that claims "Supports" for criteria the product does not support
   is a misrepresentation — treat "Partially Supports" with detailed remarks as more credible
   than blanket "Supports" claims.

6. **Ignoring third-party content on scope** — Inaccessible third-party widgets (live chat,
   payment processors, embedded maps, social media feeds) still create ADA/EAA exposure for the
   primary organization. "We can't control it" is not a defense — proactively notify vendors,
   document efforts, and provide alternatives.

7. **Outdated VPAT not triggered for review** — A VPAT more than 12–18 months old may not
   reflect the current product state after updates. Federal procurement regulations expect
   VPATs to be current. Flag stale VPATs for renewal.

8. **Conflating Section 508 and WCAG 2.0 vs. 2.1 vs. 2.2** — Section 508 (2017 refresh)
   references WCAG 2.0 AA (not 2.1 or 2.2). Title II DOJ Final Rule mandates WCAG 2.1 AA.
   EAA (via EN 301 549) mandates WCAG 2.1 AA. Applying the wrong version to the wrong framework
   produces incorrect gap analysis.

9. **Overlook cognitive accessibility** — Cognitive accessibility requirements in WCAG 2.2
   (SC 3.3.7, 3.3.8) and WCAG 2.1 SC 1.3.5, 2.5.1, 3.3.1 are frequently missed. Cognitive
   disability is the most common disability type yet accessibility programs often focus almost
   exclusively on blindness and motor impairment.

10. **"Accessible alternative" that doesn't actually work** — Claiming a telephone hotline as
    an accessible alternative for an inaccessible website when the hotline has no staff, uses an
    IVR that is itself inaccessible, or operates limited hours is not an effective alternative.
    The alternative must be genuinely equivalent and operational.

11. **Skipping the interactive process for individual accommodation requests** — Receiving an
    accessibility request and ignoring it, responding with boilerplate, or deferring indefinitely
    creates direct liability. Individual accessibility requests require an interactive process and
    documented response.

12. **Applying the "readily achievable" standard to new construction or alterations** — The
    readily achievable barrier removal standard applies only to _existing_ facilities. New
    construction and alterations must fully comply with ADA Standards — no cost-benefit
    exception applies.

13. **Assuming WCAG compliance eliminates all ADA exposure** — WCAG conformance is strong
    evidence of compliance but does not eliminate all ADA Title III exposure. Effective
    communication may still require accommodations beyond WCAG (e.g., real-time captioning,
    sign language interpretation for live events).

14. **Ignoring document accessibility** — PDFs, Word documents, Excel spreadsheets, and
    presentations are in scope for Section 508 and EAA. A fully accessible website that
    links to inaccessible PDFs for critical information fails the broader accessibility
    obligation.

15. **No monitoring or regression testing** — Achieving accessibility at launch and not
    retesting after feature releases or CMS updates. A site that was once compliant can
    regress quickly. WCAG conformance must be maintained, not just achieved once.

16. **EU member state variation ignored** — EAA sets minimum harmonized standards but member
    states can impose stricter requirements and differ in enforcement practice. A single EU-wide
    WCAG 2.1 AA assessment is a starting point, not a complete EU compliance analysis.

---

## Writing Standards

Apply plain-language discipline to all assessment output:

**For remediation records** (shared with engineering teams):

- Plain language. No legal jargon.
- Active voice: "The checkout button is not keyboard-operable" not "Keyboard operability is not supported by the checkout button"
- Specific, not vague: cite the WCAG SC number and criterion name, not just "there's an accessibility issue"
- Include the user impact in one sentence: who is affected and how (e.g., "Screen reader users cannot submit the form")
- Include the proposed fix in concrete terms: what the developer needs to change

**For legal risk sections** (reviewed by counsel):

- Clearly distinguish what is known (documented deficiency) from what is inferred (litigation risk)
- Use "[VERIFY]" for all case law citations and statutory references
- Distinguish the applicable standard (WCAG 2.1 vs. 2.2, Title II vs. Title III) explicitly
- Avoid overstating or understating risk — "material litigation risk" when material; not every
  WCAG violation is a lawsuit trigger

**Quality gate before delivery:**

- [ ] All WCAG criteria cited include SC number, name, and level
- [ ] All legal citations include [VERIFY] where not independently confirmed
- [ ] Each NON-COMPLIANT finding includes: the specific criterion, the specific failure, the user impact, and the proposed fix
- [ ] CRITICAL DEFICIENCY items have undergone 3-pass Self-Interrogation
- [ ] Jurisdiction scope is clear (US federal, US state, EU EAA, or combined)
- [ ] No WCAG 2.2 criteria cited as mandatory where only WCAG 2.1 is required

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for current DOJ enforcement actions, consent decrees, and guidance documents on
  digital accessibility
- Verify current WCAG version referenced in applicable federal regulations
- Search for member state EAA implementing legislation and enforcement guidance
- Search for relevant case law updates (Robles, Gil, and circuit split developments)
- Save research results to `/tmp/legalcode-accessibility-research.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus on WCAG technical analysis (criteria are publicly documented standards, not legal
  interpretations subject to hallucination risk)
- Advise the user to verify legal authority independently before taking action

---

## Localization Notes

### US State Law Overlay

Assess whether state law creates additional exposure:

| State      | Key State Statute                                                   | Additional Requirement                                                      |
| ---------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| California | Unruh Civil Rights Act, Cal. Civ. Code § 51; Cal. Gov. Code § 11135 | $4,000 statutory damages per violation per visit; state agency WCAG mandate |
| New York   | NY Exec. Law § 296 (Human Rights Law)                               | Broader definition of disability; independent state claim                   |
| Florida    | FL Stat. § 760.01 et seq.                                           | Used in Gil v. Winn-Dixie (federal and state claims combined)               |
| Texas      | TX Human Resources Code § 121.003                                   | Public accommodation obligations; enforcement by AG                         |

[VERIFY current state law provisions — state accessibility statutes evolve and pending legislation
may have passed]

### EU Member State EAA Implementation

As of June 2025, member states vary in implementing legislation:

- Most transposed EAA by June 2022 but enforcement approaches differ
- Germany, France, Netherlands, and Sweden have active accessibility enforcement bodies
- Penalties vary from administrative fines to market withdrawal
- [JURISDICTION-SPECIFIC] Check the specific member state's implementing law for:
  - Penalty amounts
  - Designated supervisory authority
  - Complaint procedures for individuals and NGOs
  - Transitional provisions for products placed on market before June 2025

---

## Output Format Template

Produce the accessibility compliance assessment in this format:

---

```markdown
# Accessibility Compliance Assessment

**Organization**: [Name]
**Date**: [Date]
**Assessment Scope**: [Website / App / Physical facility / Full]
**Applicable Framework**: [ADA Title III / Title II / Section 508 / EAA 2025 / Combined]
**Technical Standard**: [WCAG 2.1 AA / WCAG 2.2 AA / ADA 2010 Standards / EN 301 549]

---

## Executive Summary

**Overall Posture**: [COMPLIANT / SUBSTANTIALLY COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]

**Key Findings:**

- Critical Deficiencies: [N]
- Non-Compliant items: [N]
- Partial items: [N]
- Compliant items: [N]

**Litigation Exposure**: [LOW / MODERATE / HIGH / CRITICAL] — [1-2 sentence rationale]

**Top 3 Priorities:**

1. [Most critical finding — SC/standard, severity, user impact, action]
2. [Second finding]
3. [Third finding]

---

## Digital Accessibility Findings

### CRITICAL DEFICIENCY Items

| ID      | WCAG SC | Criterion        | Failure Description | User Impact          | Required Action |
| ------- | ------- | ---------------- | ------------------- | -------------------- | --------------- |
| ACC-[N] | [SC #]  | [Criterion name] | [Specific failure]  | [Who affected + how] | [Fix required]  |

### NON-COMPLIANT Items

[Same table format]

### PARTIAL Items

[Same table format]

### COMPLIANT Items (Summary)

[Brief list of areas meeting the standard]

---

## VPAT / ACR Assessment (if applicable)

**VPAT Version**: [2.5 / other]
**Date of VPAT**: [date]
**Currency**: [Current / Stale — last updated > 12 months ago]

| Chapter   | Standard    | Overall Representation                                  | Issues Found |
| --------- | ----------- | ------------------------------------------------------- | ------------ |
| Chapter 1 | Section 508 | [Supports / Partially / Does Not / N/A / Not Evaluated] | [Issues]     |
| Chapter 2 | WCAG 2.x    | [Same]                                                  | [Issues]     |
| Chapter 3 | EN 301 549  | [Same]                                                  | [Issues]     |

---

## Physical Accessibility Findings (if applicable)

### Priority 1 — Access Into the Building

[Findings and status]

### Priority 2 — Access to Goods/Services

[Findings and status]

### Priority 3 — Restrooms

[Findings and status]

### Priority 4 — Other Barriers

[Findings and status]

---

## EAA 2025 Assessment (if applicable)

**Organization type under EAA**: [Products / Services / Both]
**SME exemption applicable**: [Yes — microenterprise / No]
**EAA compliance deadline**: June 28, 2025 (products and services newly placed on market)

[Table of EAA obligations — Directive article, requirement, status: COMPLIANT/PARTIAL/NON-COMPLIANT]

---

## Remediation Roadmap

### IMMEDIATE Actions (0–90 days)

| ID      | Finding | Action         | Owner  | Target Date |
| ------- | ------- | -------------- | ------ | ----------- |
| ACC-[N] | [Brief] | [Specific fix] | [Team] | [Date]      |

### NEAR-TERM Actions (3–12 months)

[Same table]

### BACKGROUND Actions (12+ months / ongoing)

[Same table]

---

## Recommendations

1. **Accessibility Statement**: [Publish / Update] an accessibility statement at [URL]
   disclosing: conformance level, known limitations, contact for requests, and date of last review.
2. **Monitoring**: Implement automated accessibility testing in CI/CD pipeline.
3. **Manual Testing**: Schedule quarterly manual testing with screen reader (NVDA/JAWS + VoiceOver).
4. **VPAT Renewal**: [If applicable] Update VPAT to reflect current product state and WCAG 2.1.
5. **Training**: Ensure front-end engineers, content editors, and UX designers complete
   accessibility training.
6. **Legal counsel**: [If CRITICAL DEFICIENCY or demand letter received] Engage accessibility
   counsel before responding.

---

## Glass Box Audit Trail

[Insert complete glass_box YAML block]
```

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis based on:

- DOJ Title II Final Rule, 28 C.F.R. Part 35 (published April 24, 2024)
- ADA Title III, 42 U.S.C. §§ 12181–12189 and implementing regulations 28 C.F.R. Part 36
- Rehabilitation Act of 1973, 29 U.S.C. § 794d (Section 508)
- W3C WCAG 2.1 (June 2018) and WCAG 2.2 (October 2023) published specifications
- EU Directive 2019/882 (European Accessibility Act) and EN 301 549 v3.2.1 (2021)
- VPAT 2.5 template and ITI accessibility conformance report guidance
- ADA Standards for Accessible Design (2010 Standards), 28 C.F.R. Part 36 Appendix D
- Robles v. Domino's Pizza LLC, 913 F.3d 898 (9th Cir. 2019) and related case law
- Legalcode repository research pipeline — web-backed synthesis
- Legalcode HIPAA Compliance Assessment skill structural patterns (compliance framework adaptation)
- Legalcode Contract Review quality frameworks (Citation Gates, Self-Interrogation, Confidence Scoring, Glass Box)
