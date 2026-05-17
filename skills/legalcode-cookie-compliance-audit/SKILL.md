---
name: legalcode-cookie-compliance-audit
description: >
  Audit cookie and tracking technology implementations for ePrivacy Directive and GDPR
  compliance. Tests consent banner functionality including pre-consent cookie blocking,
  granular category controls, reject-all parity with accept-all, consent withdrawal
  mechanisms, and consent record retention. Identifies tracking technologies beyond cookies
  (pixels, fingerprinting, local storage, ETags). Evaluates compliance with CNIL, ICO, and
  EDPB guidance on cookie walls, analytics exceptions, and essential cookie classifications.
  Covers US state requirements (CCPA opt-out signals, Global Privacy Control, and state
  universal opt-out mechanisms). Produces remediation checklist with technical implementation
  guidance and confidence-scored compliance findings. Use when auditing a website, mobile app,
  or digital platform for cookie consent compliance, preparing for supervisory authority review,
  or assessing a consent management platform (CMP) implementation.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-6
context: fork
agent: general-purpose
---

# Legalcode Cookie Compliance Audit

> **Disclaimer**: This skill provides a framework for AI-assisted audit of cookie and
> tracking technology implementations under ePrivacy Directive, GDPR, UK GDPR, and US
> state privacy law. It does not constitute legal advice. All outputs must be reviewed by
> a qualified privacy counsel or Data Protection Officer licensed or operating in the
> relevant jurisdiction before any reliance, action, or regulatory submission. Privacy law,
> EDPB guidelines, and supervisory authority guidance evolve rapidly — verify currency
> before treating any provision here as current. Statutory, case law, and regulatory
> references cited from training data carry hallucination risk — verify against
> authoritative primary sources before use. Mark any unverified citation **[VERIFY]**
> before delivery.

---

## Purpose and Scope

This skill conducts a systematic audit of cookie and tracking technology implementations
against ePrivacy Directive Article 5(3), GDPR consent conditions, EDPB guidance, and
applicable national supervisory authority requirements. It identifies specific compliance
failures, classifies their severity, and produces a prioritised remediation checklist with
technical implementation guidance.

**Covers:**
- Pre-consent blocking verification (scripts, pixels, SDKs firing before consent)
- Consent banner UX compliance (reject-all parity, dark patterns, information adequacy)
- Cookie category classification (strictly necessary vs. analytics vs. marketing)
- Granular category controls (per-category toggles, independence testing)
- Withdrawal mechanism availability and effectiveness
- Consent record retention requirements (Article 5(2) GDPR accountability)
- Tracking technology scope beyond HTTP cookies (pixels, local storage, fingerprinting, ETags,
  server-side tagging, CNAME cloaking)
- Analytics cookie exemption eligibility (CNIL France, ICO UK post-DUAA)
- Cookie wall and "consent or pay" analysis (EDPB Opinion 08/2024)
- Google Consent Mode v2 signal accuracy (mandatory since March 2024)
- US state requirements: CCPA opt-out of sale/sharing, GPC mandatory honoring, state UOOM compliance
- IAB TCF v2.2 / Global Privacy Platform (GPP) string integrity (ad-tech-integrated sites)

**Does not:**
- Draft privacy policies — see `legalcode-privacy-policy-drafter`
- Assess lawful bases for general data processing — see `legalcode-gdpr-legal-basis-assessment`
- Conduct a full DPIA — see `legalcode-dpia-generator`
- Draft Data Processing Agreements with cookie vendors — see `legalcode-data-processing-agreement-drafter`
- Generate a full Record of Processing Activities — see `legalcode-ropa-generator`
- Assess cross-border data transfers — see `legalcode-cross-border-transfer-assessment`
- Provide legal advice or replace qualified privacy counsel
- Guarantee against supervisory authority enforcement action

**Complementary skills in the privacy skill family:**
- `legalcode-gdpr-legal-basis-assessment` — verify consent is the correct basis for cookie-linked processing
- `legalcode-legitimate-interest-assessment` — assess LI basis for analytics (note: LI cannot substitute for ePrivacy consent in EU/UK)
- `legalcode-dpia-generator` — triggered by high-risk tracking identified here (fingerprinting, cross-site profiling)
- `legalcode-privacy-policy-drafter` — receives cookie disclosure language and vendor list from this audit
- `legalcode-vendor-privacy-assessment` — deeper assessment of individual third-party cookie vendors

---

## Jurisdiction and Governing Law

This skill covers three regulatory layers that frequently apply simultaneously.

### Layer 1: EU ePrivacy Framework (Governs All EU/EEA Sites)

| Instrument | Key Provision | Scope |
|------------|--------------|-------|
| ePrivacy Directive 2002/58/EC (amended 2009/136/EC) | Article 5(3) — prior informed consent before storing or accessing info on terminal equipment, unless strictly necessary | Any website/app with EU/EEA visitors |
| GDPR Regulation 2016/679 | Article 4(11) + Article 7 — defines valid consent conditions; Article 5(2) — accountability obligation | Consent given under ePrivacy Art. 5(3) must meet GDPR standard |
| EDPB Guidelines 2/2023 v2.0 (October 2024) | Technical scope of Art. 5(3): all storage or access to terminal equipment — cookies, local storage, pixels, fingerprinting, ephemeral RAM cache | All forms of tracking technology |
| EDPB Guidelines 05/2020 on Consent (v1.1) | Six consent conditions; prohibited mechanisms; withdrawal requirements | All consent-based cookie processing |
| EDPB Cookie Banner Taskforce Report (January 2023) | Minimum threshold for banner design — reject must be accessible at first layer | Banner UX compliance |
| EDPB Guidelines 03/2022 on Dark Patterns (v2.0, February 2023) | Prohibits deceptive UI design in consent interfaces | Banner visual design and UX |
| EDPB Opinion 08/2024 on "Consent or Pay" | Cookie walls impermissible; Large Online Platforms face heightened threshold | Cookie wall analysis |

### Layer 2: National Transpositions (Member-State-Specific)

[JURISDICTION-SPECIFIC] Each EU/EEA member state has transposed Article 5(3) into national
law. Research the applicable national transposition for the site's primary audience:

| Jurisdiction | Transposing Instrument | Key Additional Requirements |
|-------------|----------------------|---------------------------|
| **France** | Article 82 Loi Informatique et Libertés | Reject All required at first layer; analytics exemption available under strict conditions (13-month cookie lifetime, single-site scope, no cross-referencing, IP pseudonymised, no session replay, anonymous output only); Google Analytics does NOT qualify for the exemption; CNIL active enforcement — €325M Google (Sept 2025), €150M SHEIN (Sept 2025) |
| **Germany** | §25 TDDDG (Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz, in force December 2021) | Active opt-in required; browser-level cookie settings do not constitute valid consent under German law; DSK Orientierungshilfe v1.2 (November 2024) — strict CMP blocking requirements |
| **UK (post-Brexit)** | Regulation 6 PECR 2003 (Data (Use and Access) Act 2025, Royal Assent 19 June 2025) | Consent required for analytics (existing position); DUAA introduces potential exceptions for low-risk statistical analysis functions [VERIFY — ICO guidance under revision as of mid-2025]; ICO reviewing top 1,000 UK websites (announced January 2025) |
| **Netherlands** | Telecommunicatiewet Article 11.7a | Strict consent requirement; cookie walls prohibited |
| **Spain** | LSSI-CE | AEPD enforcement active; record €35.5M total fines FY2024 |

### Layer 3: US State Privacy Requirements (Opt-Out / GPC)

[JURISDICTION-SPECIFIC] US state law does not require opt-in consent for analytics cookies.
Instead, it requires opt-out mechanisms and mandatory honoring of GPC signals:

| State | Law | Key Cookie-Related Requirement | Effective Date |
|-------|-----|-------------------------------|----------------|
| California | CCPA/CPRA (revised regs effective Jan 1, 2026) | Mandatory GPC honoring as opt-out of sale and sharing; "Do Not Sell or Share My PI" link; opt-in consent required for under-16s | GPC mandatory now; revised dark-patterns regs Jan 1, 2026 |
| Colorado | CPA | GPC approved as first UOOM; must honor GPC as opt-out of targeted advertising and data sales | July 1, 2024 |
| Connecticut | CTDPA | UOOM honoring required | January 1, 2025 |
| Delaware, Montana, Nebraska, New Hampshire, New Jersey, Oregon, Texas | Various | UOOM / opt-out signal honoring required | Varies — verify state-specific effective dates [VERIFY] |
| Virginia | VCDPA | No UOOM provision in statute; standard opt-out rights apply | January 1, 2023 |

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points, marked with **⟁ CLARIFY**
below. Rather than assuming, the workflow pauses and asks when:

- The answer changes which regulatory layer applies
- Multiple valid approaches exist and the user's preference matters
- Technical access limitations restrict the audit scope
- Business context is needed to classify severity correctly

If the user has already provided the relevant information, skip the clarification and proceed.
For non-interactive/batch runs, use these defaults: EU primary jurisdiction, B2C site, full
audit scope, no existing scan report.

---

## Workflow

### Step 1: Accept Input

Accept the audit target in any of these formats:

- **Website URL**: The site's homepage or a specific page to audit (most common)
- **Cookie audit report**: An existing automated scan report (Cookiebot, OneTrust, Termly, etc.)
- **Description or specification**: Written description of the cookie implementation
- **CMP configuration export**: Tag manager or CMP configuration file
- **Cookie policy document**: The site's existing cookie notice/policy

If no specific audit target is provided, prompt the user to supply a URL, document, or
description.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user the following questions. Present as structured
options where possible. Skip any question already answered by the input.

1. **Primary regulatory jurisdiction?**
   - Options: EU (specify primary country or "all EU"), UK only, US only, EU + UK + US (multinational), Other
   - *Why this matters*: Determines which regulatory layer(s) apply. A US-only audience may need GPC/UOOM compliance but not ePrivacy pre-consent requirements. An EU site needs all layers.

2. **Site type and audience?**
   - Options: Consumer website (B2C), SaaS/business platform (B2B), E-commerce, News/media, Mobile app, Other
   - *Why this matters*: CNIL analytics exemption requires single-site scope; mobile apps face CNIL 2025 investigation campaign; B2C consumer sites face higher enforcement scrutiny; news/media sites commonly implement cookie walls.

3. **CMP currently deployed?**
   - Options: OneTrust, Cookiebot / Usercentrics, TrustArc, Didomi, iubenda, Axeptio, No CMP, Unknown
   - *Why this matters*: Different CMPs have known configuration patterns and common compliance gaps. Identifying the CMP helps focus the audit on platform-specific failure modes.

4. **Ad tech or behavioral advertising in use?**
   - Options: Yes (Google Ads, Meta Ads, programmatic/DSP), Analytics only, No advertising, Unknown
   - *Why this matters*: Advertising tracking requires the strictest consent controls and mandatory Google Consent Mode v2 analysis. Ad-tech-integrated sites must also address IAB TCF/GPP string accuracy.

5. **Audit scope?**
   - Options: Full audit (all domains), Banner UX only, Pre-consent blocking only, US GPC/UOOM only, Analytics exemption eligibility only
   - *Why this matters*: Scopes the analysis depth and output format.

If the user provides partial context, proceed with what is available but **state assumptions
explicitly** (e.g., "Assuming EU primary jurisdiction and full audit scope — advise if different").

### Step 3: Identify Applicable Regulatory Obligations

Based on Step 2 context, determine and document the regulatory scope:

1. **EU/EEA ePrivacy obligations?**
   - Apply if: Site targets EU/EEA users OR site operator is established in EU/EEA
   - Triggers: ePrivacy Directive Art. 5(3), GDPR consent conditions (Arts. 4(11), 7), EDPB Guidelines, national transposition(s)
   - Identify primary supervisory authority: CNIL (France), DPC (Ireland — Big Tech one-stop-shop), AEPD (Spain), DSK/Länder (Germany), ICO (UK, separate layer)

2. **UK PECR obligations?**
   - Apply if: Site targets UK users OR UK establishment
   - Triggers: PECR Regulation 6, UK GDPR, Data (Use and Access) Act 2025
   - Note: DUAA analytics exceptions are forthcoming from ICO [VERIFY — check current ICO guidance]

3. **US state obligations?**
   - Apply if: Site collects personal information from residents of California, Colorado, Connecticut, Delaware, Montana, Nebraska, New Hampshire, New Jersey, Oregon, or Texas
   - Check California first — largest enforcement risk, mandatory GPC, CPPA + AG joint enforcement sweeps

4. **Special considerations?**
   - Large Online Platform (LOP) status → EDPB Opinion 08/2024 stricter cookie wall standard
   - Site serves children → COPPA (US) or GDPR Art. 8 (EU/UK) apply — flag separately; outside scope of this skill
   - Mobile app → CNIL 2025 investigation campaign; app-specific consent mechanisms require platform-specific review

Mark applicable layers clearly in the audit output:
`EU APPLICABLE | UK APPLICABLE | US (CA / CO / CT / ...) APPLICABLE`

### Step 4: Pre-Consent Blocking Test

**⟁ CLARIFY** — Ask: "Do you have live technical access to test the site in a fresh browser
session, or should I analyse an existing automated scan report?"

**If live technical access is available**, conduct the pre-consent blocking test:

1. **Clear all site data** — Open Chrome in Incognito mode (no prior cookies or local storage)
2. **Open Chrome DevTools** (F12 → Network tab) → Enable "Preserve log"
3. **Navigate to the site** — Do NOT interact with the cookie banner
4. **Inspect for pre-consent tracking**:
   - Application tab → Storage → Cookies → [site domain]: any cookies set on page load?
   - Network tab: search for requests to known tracking domains (list below)
   - Inspect Set-Cookie response headers on any network request
5. **Inspect local storage**: Application tab → Local Storage → [site domain]: any tracking identifiers?
6. **Document findings**: List every cookie/request found before any consent interaction

**Known tracking domains to monitor (non-exhaustive):**

| Category | Domains to Monitor |
|----------|-------------------|
| Google Analytics / Ads | `google-analytics.com`, `analytics.google.com`, `googletagmanager.com`, `doubleclick.net`, `googlesyndication.com` |
| Meta / Facebook | `facebook.net`, `connect.facebook.net`, `fbcdn.net` |
| Microsoft | `clarity.ms`, `bing.com`, `bat.bing.com` |
| Session recording | `hotjar.com`, `hj.com`, `fullstory.com`, `logrocket.com` |
| LinkedIn | `licdn.com`, `linkedin.com` |
| Twitter/X | `ads-twitter.com`, `t.co` |
| Trade Desk | `adsrvr.org` |
| A/B testing | `optimizely.com`, `vwo.com` |

**Classify pre-consent blocking findings:**
- **NON-COMPLIANT**: Any non-essential cookie, tracker, or pixel fires before consent interaction
- **REQUIRES REMEDIATION**: Tracking domain receives a request but no cookie is set; or scripts load but are not initialised
- **COMPLIANT**: Only strictly necessary cookies present; no third-party tracking requests before consent

**If only an automated scan report is available:**
- Extract all cookies listed as "set before consent" or in the "strictly necessary" bucket that appear to serve analytics/advertising purposes
- Note automated scan limitations (JavaScript-only trackers may be missed)
- Document scan tool name, version, and scan date

### Step 5: Cookie Category Classification Audit

Misclassification of cookies is among the most cited EDPB Cookie Banner Taskforce findings.
Audit each cookie against the strictly necessary exemption test.

#### Strictly Necessary Cookies — Two-Part Eligibility Test

A cookie is strictly necessary ONLY if BOTH conditions are met:
1. It is technically required for a service **explicitly requested by the user** (not merely beneficial)
2. Without it, the service cannot function at all (not merely degrades or becomes less convenient)

**Always legitimately strictly necessary:**
- [ ] Session authentication tokens (login state persistence)
- [ ] Shopping cart / basket state cookies (e-commerce only)
- [ ] CSRF (Cross-Site Request Forgery) protection tokens
- [ ] Load-balancing cookies where session affinity is technically required
- [ ] Cookie consent preference record (the cookie recording the user's own consent choice)
- [ ] TLS/SSL session handling cookies
- [ ] User interface preference cookies set by explicit user action (e.g., chosen language)

**Common misclassifications — never strictly necessary:**

| Cookie / Tool | Why NOT strictly necessary | Common justification (rejected) |
|---------------|--------------------------|--------------------------------|
| Google Analytics / GA4 | Measures audience behaviour — not technically required for service delivery | "We need it to improve the site" |
| Google Tag Manager data layer | Loads third-party scripts — not technically required | "It's just a container" |
| Meta Pixel / Facebook tracking | Advertising attribution — explicitly not necessary for service delivery | "Our marketing depends on it" |
| Hotjar / Microsoft Clarity | Session recording and heatmapping — optional analytics | "It's for performance monitoring" |
| Optimizely / VWO (A/B testing) | Conversion optimisation — not technically necessary | "It improves user experience" |
| Google Ads conversion tracking | Advertising ROI measurement — never technically necessary | "We need to measure ad spend" |
| Intercom / Drift chatbot | Customer support enhancement — service accessible by other means | "It's a core support tool" |
| Social media share/like buttons (SDK) | Social platform data transfer — no user explicitly requested it | "They're standard site features" |

**Audit test for each "strictly necessary" claim:** Apply the two-part test above. If the
answer to part (1) is "No" or the answer to part (2) is "No," the cookie fails the test.

#### Analytics Cookie Exemption Eligibility

[JURISDICTION-SPECIFIC — France/CNIL] CNIL permits analytics cookies without consent if
ALL of the following conditions are met simultaneously:

- [ ] Single site/application scope only — no cross-site tracking, no cross-brand data sharing
- [ ] No cross-referencing with any other dataset (CRM, advertising data, social profiles)
- [ ] Cookie lifetime maximum: **13 months**
- [ ] IP addresses pseudonymised — at minimum the final byte removed after city-level geolocation
- [ ] No session replay functionality (Hotjar, Clarity, FullStory are explicitly excluded)
- [ ] All exported reports contain only anonymous aggregate statistics (no individual user data)
- [ ] Fingerprinting components must be site-specific and time-limited (no cross-site fingerprinting)

**Qualifying tools** (with correct configuration): Matomo (on-premises/EU-hosted, no cross-site
tracking), AT Internet/Piano Analytics (CNIL-compliant configuration)

**Disqualifying tools** (do NOT qualify): Google Analytics / GA4, Adobe Analytics with audience
sharing, any tool that passes data to advertising or CRM systems

[JURISDICTION-SPECIFIC — UK/ICO] Analytics cookies currently require consent under PECR. The
Data (Use and Access) Act 2025 introduces a potential exception for low-risk statistical
analysis functions. ICO guidance implementing this exception is pending as of mid-2025.
[VERIFY — confirm current ICO guidance before advising on UK analytics exemption]

### Step 6: Consent Banner UX Audit

Audit the consent banner against EDPB Guidelines 05/2020, Cookie Banner Taskforce Report
(January 2023), and EDPB Guidelines 03/2022 (Dark Patterns).

**⟁ CLARIFY** — If live banner access is unavailable, ask the user to provide a screenshot or
describe the banner design (number of layers, button labels, colour/size of Accept vs. Reject).

#### A. Reject All / Accept All Parity (Highest Enforcement Priority)

- [ ] "Accept All" and "Reject All" (or semantically equivalent) both appear at the **same layer** of the banner
- [ ] Both buttons have **equivalent visual prominence** — comparable colour, size, and contrast ratio
- [ ] Rejection does **not** require navigating to a second layer or sub-menu that acceptance bypasses
- [ ] Rejection requires the **same number of clicks** as acceptance (click parity)

**NON-COMPLIANT markers:**
- "Accept All" at first layer; rejection requires "Manage Preferences" → second layer
- "Reject" is text-only (hyperlink or body text), not a button element
- "Accept" is bright/prominent; "Reject" is grey, small, or low-contrast
- Rejection requires 3+ clicks while acceptance requires 1

**Enforcement precedent:** CNIL fined Google €150M and Facebook €60M (January 2022) for absence
of equivalent Reject All at first layer. This remains the most frequently cited EU violation.

#### B. Absence of Dark Patterns (EDPB Guidelines 03/2022)

- [ ] No pre-ticked checkboxes at any layer (first or second layer)
- [ ] No misleading button labelling (e.g., "Accept" vs. "Close" where "Close" implies rejection but accepts)
- [ ] No consent-by-continued-browsing (scrolling or page views treated as acceptance)
- [ ] No consent-by-page-close (X button without reject option treated as acceptance)
- [ ] No artificial urgency (countdown timers, "offer expires" language without legal basis)
- [ ] No complexity asymmetry (accepting requires significantly fewer steps than rejecting)
- [ ] No emotionally manipulative labelling (e.g., "No thanks, I prefer not to be protected")

#### C. First-Layer Information Adequacy

Minimum information required at first layer or via immediately accessible link:
- [ ] Identity of the data controller (organisation name)
- [ ] Purpose of each cookie category (specific description, not just the category label)
- [ ] Categories of recipients or named third-party vendors
- [ ] Data retention periods per category
- [ ] Right to withdraw consent at any time with link to withdrawal mechanism
- [ ] Link to full cookie policy / privacy notice

**Common failure:** Banner displaying only "We use cookies — Accept / Decline" with no
information about purpose or recipients. Cookie Banner Taskforce Report (January 2023)
identifies this as below the minimum threshold.

#### D. Cookie Wall Test

- [ ] Is access to the service conditional on accepting non-essential cookies?
  → **NON-COMPLIANT** (unless EDPB Opinion 08/2024 "truly equivalent" alternative is offered — only applies to Large Online Platforms)
- [ ] Is a "consent or pay" model used?
  → If Large Online Platform: essentially impermissible; "truly equivalent free option" required
  → If standard site: generally impermissible under EDPB Guidelines 05/2020; some national DPA latitude [JURISDICTION-SPECIFIC]

#### E. Second-Layer / Preference Centre Requirements

- [ ] Each cookie category has an independently controllable toggle/checkbox
- [ ] "Strictly necessary" cookies are disclosed but non-toggleable (with clear explanation)
- [ ] Category descriptions are specific (not "personalisation" or "improve experience")
- [ ] Individual vendor list or categories of recipients accessible (IAB TCF requirement for ad-tech sites)
- [ ] Preference state persists correctly when user returns to the preference centre

### Step 7: Tracking Technology Scope Audit

Per EDPB Guidelines 2/2023 v2.0 (October 2024), the consent requirement extends to ALL
mechanisms that store information on or access information from terminal equipment —
not only HTTP cookies.

#### Full Scope of Article 5(3) — Technology Inventory

Identify and classify each technology found:

| Technology | Audit Method | Pre-Consent Test | Common Non-Compliance |
|------------|-------------|-----------------|----------------------|
| **HTTP cookies** (session, persistent, first/third-party) | Application tab → Cookies | Steps 4-6 | Pre-consent firing |
| **Local storage** (`localStorage`, `sessionStorage`) | Application tab → Local Storage; look for tracking IDs | Check for identifiers written before consent | Analytics or ad tech writing tracking IDs before consent |
| **IndexedDB** | Application tab → IndexedDB; inspect structured databases | Check for fingerprinting data | Fingerprinting scripts using IndexedDB for identifier persistence |
| **Tracking pixels / web beacons** | Network tab → filter image requests; look for 1×1 pixel GIF patterns to ad domains | Check for pixel requests before consent | Meta Pixel, LinkedIn Insight Tag firing on page load |
| **ETags** (HTTP cache-based tracking) | Network response headers → ETag values that could serve as identifiers | Check for consistent ETag values across page loads | Rarely detected by basic scans; flag where ETag values are sent to analytics domains |
| **Browser fingerprinting** (canvas, WebGL, audio, font) | Inspect page JS for canvas API, WebGL renderer, AudioContext calls | Check script execution timing | Scripts fingerprinting user before consent; used as cookie-less tracking alternative |
| **CNAME cloaking** | DNS lookup of analytics subdomain; check if first-party subdomain proxies third-party analytics | DNS/network check | `analytics.yourdomain.com` resolving to `googleanalytics.com` — bypasses third-party cookie blocking but does not eliminate consent obligation |
| **Service worker caches** | Application tab → Service Workers, Cache Storage | Check for tracking data stored in SW cache | Service worker used to persist identifiers after cookie deletion |
| **URL tracking parameters** (UTM, gclid, fbclid) | Inspect page URLs; check if parameters are captured by analytics scripts | Check analytics script execution timing | UTM parameters captured by analytics before consent interaction |
| **Social media embed SDKs** | Network tab → look for requests to `connect.facebook.net`, `platform.twitter.com`, `platform.linkedin.com` | Check request timing on page load | "Like," "Share," and "Follow" buttons loading social media SDKs before consent |
| **Server-side tagging** (GTM server-side, Segment, etc.) | Review server-side container configuration; inspect network requests for first-party proxy endpoints | CMP consent signal propagation to server-side container | Server-side tags receiving data before CMP consent signal; first-party proxy endpoints bypassing client-side consent gating |
| **IP-based tracking** | Review server logs and analytics configuration | Server-side signal reception | Server-side analytics collecting full IP before browser consent signal received |

For each technology identified, record:
- Technology type and vendor name
- Purpose / which cookie category it serves
- Pre-consent? (Yes / No / Uncertain)
- Category assigned in CMP
- Assessment (COMPLIANT / REQUIRES REMEDIATION / NON-COMPLIANT)

### Step 8: Withdrawal Mechanism and Re-Consent Audit

#### Withdrawal Mechanism (Article 7(3) GDPR)

Consent must be "as easy to withdraw as to give." Test each criterion:

- [ ] **Persistent access mechanism exists**: Permanent, visible mechanism to access cookie preferences on all pages (e.g., footer link labelled "Cookie Settings," floating icon, privacy preference centre link)
- [ ] **Withdrawal is functional**: After withdrawing consent, non-essential cookies are deleted or expired from the current session — not merely blocked for future sessions
- [ ] **Withdrawal ease**: Withdrawal requires comparable steps to giving consent (no multi-step withdrawal from single-click accept)
- [ ] **Effect is immediate**: Withdrawal takes effect without requiring page reload or additional confirmation steps (best practice)
- [ ] **State persists**: After withdrawal, preference is persisted across browser sessions

**Test procedure:**
1. Accept all cookies; verify non-essential cookies are set
2. Access withdrawal mechanism (footer link / settings icon / preference centre)
3. Withdraw consent for all non-essential categories
4. Check Application → Cookies: verify non-essential cookies are deleted or expired (not just flagged for future deletion)
5. Reload page: verify non-essential tracking does not resume

**Common failures:**
- CMP updates consent preference but does not delete previously set cookies (failure to "unset")
- Withdrawal only affects future visits; persisted cookies remain active for current session
- Withdrawal mechanism hidden — only accessible via buried link in privacy policy body text
- After withdrawal, analytics/advertising scripts continue to fire using a stale consent state

#### Re-Consent Trigger Analysis

Re-consent must be collected when any of these events occur:

- [ ] A materially new tracking purpose is added to any existing cookie category
- [ ] A new category of cookies is introduced to the implementation
- [ ] A new third-party vendor is added whose data use is materially different from prior disclosures
- [ ] The data controller's identity changes materially (merger, acquisition, rebranding)
- [ ] Consent was collected more than 12 months ago (best practice — EDPB has not set a universal maximum period [VERIFY]; 12 months is widely adopted)
- [ ] A significant CMP or banner version change materially alters what users were consenting to

**Audit check:** Review CMP version history and purpose change log. Identify the date consent
was last re-collected. Have purposes or vendors changed materially since?

### Step 9: Consent Record Integrity Audit

GDPR Article 5(2) (accountability) requires the controller to demonstrate that consent was
validly obtained. Test the consent record system.

#### Required Consent Record Fields

Each consent interaction must generate a record containing:

- [ ] **Timestamp** — precise timestamp of consent interaction (to-second precision minimum)
- [ ] **User/device identifier** — cookie ID, hashed user ID, or pseudonymised device identifier
- [ ] **Consent decision** — complete record of acceptance, rejection, or partial acceptance per category
- [ ] **Banner version** — which version of the consent banner/notice was displayed
- [ ] **CMP version** — version of the Consent Management Platform at time of interaction
- [ ] **IP address** — full or pseudonymised (country-level minimum; pseudonymise if in EU context)
- [ ] **Geolocation** — at minimum country-level; ideally region-level
- [ ] **Device / browser information** — user agent string
- [ ] **Interaction method** — how consent was given (button click, toggle selection, etc.)

**Retention:** Retain consent records for the duration of the processing they authorise plus
sufficient time to respond to regulatory investigations. **3 years minimum** is widely recommended
(aligns with common limitation periods) [VERIFY — GDPR Art. 5(2) does not specify a minimum
retention period; best practice guidance varies from 2-5 years].

**Audit test:**
1. Give consent on the site
2. Request from the CMP operator or technical team: a sample consent record for a specific cookie/device ID
3. Verify all required fields are present and accurately reflect the interaction
4. Test CMP's ability to retrieve and export a specific user's consent history upon regulatory request

#### Consent Record Anti-Patterns
- Records stored in the same database as personal data without segregation
- Records not encrypted at rest
- Consent logs deleted after a short period (30–90 days) with no backup
- CMP records only a "consent given" flag without preserving per-category decisions
- Re-consent overwrites prior records without maintaining a version history

### Step 10: US Opt-Out Signal Audit (GPC and UOOM)

[JURISDICTION-SPECIFIC — US STATES] Apply this step only if the site has US users and falls
within scope of CCPA or applicable state privacy laws.

#### Global Privacy Control (GPC) Testing

GPC is a browser-level signal indicating the user's preference to opt out of the sale and
sharing of personal information. Honoring GPC is mandatory in California and Colorado.

**Test procedure:**
1. Install a GPC-enabled browser extension (e.g., Privacy Badger, OptMeowt) or use a browser
   with native GPC support (Firefox with GPC enabled; Brave with "Global Privacy Control" active)
2. Navigate to the site with GPC signal active
3. Verify site behavior:
   - **COMPLIANT**: Site detects `Sec-GPC: 1` header or `navigator.globalPrivacyControl === true`
     and processes as an opt-out of sale and sharing
   - **NON-COMPLIANT**: Site ignores GPC signal; advertising cookies and data sharing continue
     regardless of the browser signal

**California requirements (as of January 1, 2026 revised regulations):**
- [ ] GPC signal honored as opt-out of sale and sharing of personal information
- [ ] "Do Not Sell or Share My Personal Information" link present on homepage (unless GPC is the sole mechanism)
- [ ] Opt-out processed without requiring user account creation or login
- [ ] No dark pattern barriers to exercising opt-out rights (per 2026 revised CCPA regulations)
- [ ] No financial or service discrimination against users who opt out

**Colorado UOOM (effective July 1, 2024):**
- [ ] GPC honored as the approved UOOM for opt-out of targeted advertising and data sales
- [ ] Opt-out applies to all Colorado residents' data, not only users who actively send the signal

**Multi-state UOOM:** Verify the current state list with active UOOM requirements. As of mid-2025,
active UOOM requirements exist in California, Colorado, Connecticut, Delaware, Montana, Nebraska,
New Hampshire, New Jersey, Oregon, and Texas [VERIFY — confirm current state list against each
state AG's published guidance].

#### IAB GPP / TCF String Audit (Ad-Tech-Integrated Sites)

If the site uses IAB TCF v2.2 or IAB Global Privacy Platform:
- [ ] TCF/GPP consent string accurately reflects the user's actual consent decision
- [ ] Consent string is correctly propagated to all integrated ad tech vendors
- [ ] All consent parameters default to "denied" before consent interaction
- [ ] No mismatch between CMP UI state and GPP/TCF string values

**Test:** In Chrome DevTools console, after consent interaction, execute
`__tcfapi('getTCData', 2, (data) => console.log(JSON.stringify(data)))` to inspect the TCF
string. Verify consent values match the user's banner selections.

### Step 11: Google Consent Mode v2 Compliance

[JURISDICTION-SPECIFIC — applies where Google Ads or GA4 are deployed] Google made
Consent Mode v2 mandatory for all Google advertising and analytics functionality from
March 2024. Sites that do not implement Consent Mode v2 lose access to Google Ads
conversion tracking and remarketing features — this is the correct technical outcome when
consent is not given.

#### Consent Mode v2 Signal Audit

All four signals must default to `denied` before any user consent interaction:

| Signal | Controls | Required Default | Risk if Incorrect |
|--------|----------|-----------------|--------------------|
| `ad_storage` | Advertising cookies | `denied` | Advertising cookies load before consent |
| `analytics_storage` | Analytics cookies | `denied` | Analytics data collected before consent |
| `ad_user_data` | Sending user data to Google Ads | `denied` | User data sent to Google without consent |
| `ad_personalization` | Personalised advertising | `denied` | Ad personalisation without consent |

**Test procedure:**
1. Open Chrome DevTools → Console tab
2. Navigate to site in Incognito mode (no prior cookies)
3. Before any consent interaction, check: `window.dataLayer` → look for `gtag('consent', 'default', {...})` event with all signals set to `denied`
4. Accept all cookies; verify all four signals update to `granted`
5. Accept only analytics; verify: `analytics_storage: 'granted'`, `ad_storage: 'denied'`, `ad_user_data: 'denied'`, `ad_personalization: 'denied'`

**Common failures:**
- Consent Mode initialised with `ad_storage: 'granted'` as default (non-compliant with GDPR consent conditions)
- `analytics_storage` updates to `granted` when user only accepted "functional" cookies
- `ad_user_data` set to `granted` without separate, specific consent for data sending to Google
- Consent Mode v2 not implemented at all (Google Ads measurement ceases — technically correct outcome but many sites have not implemented any signals)

**EDPB/CNIL position on Consent Mode "Advanced Mode":** Consent Mode with "modelled conversions"
from non-consented users creates legal risk. The EDPB and CNIL have signalled that modelled
conversions derived from users who rejected consent may not be permissible. [VERIFY — exact
regulatory position on Advanced Mode modelled conversions is evolving as of 2025]

### Step 12: Quality Verification

Before delivering the audit report, apply these quality checks silently.

#### Citation Quality Gates

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every non-compliance finding cites a specific EDPB Guideline, Directive article, or SA guidance document | Add citation or mark "[UNVERIFIED]" |
| **Format** | All citations follow a consistent format: Authority, document title, article/section, date | Fix format |
| **Currency** | Verify against known regulatory updates: DUAA (UK 2025), CCPA revised regs (CA Jan 2026), DSK v1.2 (Nov 2024), EDPB Guidelines 2/2023 v2.0 (Oct 2024) | Flag "[CHECK CURRENCY]" |
| **Domain** | Analysis stays within cookie/ePrivacy scope; do not conflate general GDPR data processing analysis with ePrivacy consent requirements | Remove or flag scope bleed |
| **Confidence** | Uncertainty (DUAA analytics exception, multi-state UOOM evolution, Consent Mode Advanced Mode) explicitly stated, not hidden | Add confidence qualifier |

#### Self-Interrogation for NON-COMPLIANT Findings

For any finding classified as **NON-COMPLIANT**, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the non-compliance finding follow logically from the
cited authority? Would a supervisory authority with jurisdiction actually reach this conclusion
under current guidance? Is the applicable national transposition considered?

**Pass 2 — Completeness**: Have all relevant EDPB Guidelines, national SA guidance, and
2024-2025 updates been considered? Is there a national exemption (e.g., CNIL analytics
exemption, UK DUAA exception) that might apply? Has the most recent guidance version been used?

**Pass 3 — Challenge**: What is the strongest argument that this implementation is actually
compliant? Under what narrow reading of the law could it be defensible? Note any genuine
ambiguity clearly in the audit report alongside the finding.

#### Confidence Scoring

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95–1.0 | Clear violation per settled EDPB/SA guidance; enforcement action has been taken for this exact failure | State non-compliance with confidence; cite enforcement precedent |
| **High** | 0.80–0.94 | Strong authority; minor interpretive questions | Assert with brief caveat noting the uncertainty |
| **Probable** | 0.60–0.79 | Good arguments; some national DPA latitude possible | State assessment with contra-indicators and jurisdictional notes |
| **Possible** | 0.40–0.59 | Genuinely uncertain law (e.g., DUAA analytics exception scope) | Flag for legal review with both sides of the argument presented |
| **Unlikely** | 0.0–0.39 | Weak or speculative non-compliance basis | Do not assert violation; note factual observation without legal conclusion |

---

## Audit Domains and Severity Classification

### Severity Classification System

| Classification | Definition | Regulatory Risk | Remediation Priority |
|----------------|-----------|----------------|----------------------|
| **NON-COMPLIANT** | Clear violation of ePrivacy Directive, GDPR consent requirements, or applicable national law. Enforcement action has been taken for this exact failure type. | HIGH — regulators have fined this violation; immediate risk if audited | **Critical** — remediate within 30 days |
| **REQUIRES REMEDIATION** | Implementation does not meet current EDPB/SA guidance or best practice, but may not yet have triggered enforcement. Or: clear violation of US opt-out requirements. | MEDIUM — active enforcement risk, especially under ICO top-1,000 review | **High** — remediate within 90 days |
| **COMPLIANT** | Implementation meets applicable legal requirements and EDPB/SA guidance | LOW | No action required; note best practice gaps where applicable |

### Domain 1: Pre-Consent Blocking

| Criterion | NON-COMPLIANT | REQUIRES REMEDIATION | COMPLIANT |
|-----------|--------------|---------------------|-----------|
| Analytics scripts | Analytics fires + sets cookie before consent | Analytics domain receives request; no cookie set | No analytics request before consent |
| Advertising pixels | Advertising pixel fires before consent | Advertising domain request; no cookie or data sent | No advertising request before consent |
| Session recording | Hotjar / Clarity / FullStory loads and initialises before consent | Recording library loads; not initialised | Library not loaded before consent |
| Social media embeds | Social SDK loads and sets cookies before consent | SDK loads; no cross-domain cookie | Social embed not loaded before consent |
| Tag manager configuration | GTM fires all tags before CMP initialisation | GTM loads; consent triggers partially configured | GTM configured to wait for CMP consent state |

**Enforcement precedent:** CNIL fined SHEIN €150M (September 2025) for pre-consent cookie
placement. Google €150M (January 2022) and Yahoo €10M (December 2023) for the same violation.
This is the single most-fined violation category across EU supervisory authorities.

### Domain 2: Accept/Reject Parity

| Criterion | NON-COMPLIANT | REQUIRES REMEDIATION | COMPLIANT |
|-----------|--------------|---------------------|-----------|
| Reject All at first layer | No rejection option at first layer; only "Accept All" | Reject accessible but requires extra navigational step | Accept and Reject both visible at first layer |
| Visual parity | Strong visual asymmetry (bright/prominent Accept; grey/tiny Reject) | Mild asymmetry; both identifiable as interactive buttons | Equivalent visual prominence, colour, and size |
| Click parity | Rejection requires 3+ clicks vs. 1 click to accept | Rejection requires 1 additional step vs. acceptance | Equal number of steps for both actions |

**Enforcement precedent:** Cookie Banner Taskforce Report (January 2023) — 5 of 7 identified
violation types relate to reject-all parity. CNIL fines Google €150M and Facebook €60M for this
specific violation (January 2022).

### Domain 3: Dark Patterns

| Criterion | NON-COMPLIANT | REQUIRES REMEDIATION | COMPLIANT |
|-----------|--------------|---------------------|-----------|
| Pre-ticked boxes | Pre-ticked checkbox at any layer | Pre-ticked but visually prominent (clear opt-out available) | No pre-ticked boxes at any layer |
| Misleading labels | "Accept" vs. "Close" where "Close" actually accepts | Unclear but not actively misleading | Unambiguous labelling throughout |
| Passive consent | Scrolling or continued browsing treated as consent | Banner disappears on scroll (ambiguous) | Explicit positive affirmative action required |
| Consent-by-close | Closing banner (X button only) treated as acceptance | X button dismisses banner; preference state unclear | X button maintains prior state without implying consent |
| Emotional manipulation | Guilt-tripping or fear-based labels on rejection option | Mild framing asymmetry | Neutral, equivalent labelling for both options |

### Domain 4: Cookie Classification Accuracy

| Criterion | NON-COMPLIANT | REQUIRES REMEDIATION | COMPLIANT |
|-----------|--------------|---------------------|-----------|
| GA4 / analytics in "strictly necessary" | Google Analytics classified as strictly necessary | Analytics tool in analytics category but fires before consent | Analytics gated behind analytics consent |
| Session recording in "performance" | Hotjar / Clarity classified as strictly necessary or performance | Recording tools in analytics category (misnamed) | Recording tools in appropriate category, gated on consent |
| Advertising in "functional" | Advertising trackers classified as functional or strictly necessary | Advertising tracker in analytics (not marketing) | Advertising trackers in marketing category; gated on consent |

### Domain 5: Granular Category Controls

| Criterion | NON-COMPLIANT | REQUIRES REMEDIATION | COMPLIANT |
|-----------|--------------|---------------------|-----------|
| All-or-nothing consent | Single Accept/Decline toggle; no category granularity | Categories visible but not fully independent (some coupling) | Independent per-category toggles at second layer |
| Category descriptions | Vague descriptions ("enhance experience," "personalisation") | Category names accurate; descriptions minimal | Specific descriptions of purpose, data types, and third parties per category |
| Vendor transparency | No vendor list disclosed anywhere | Categories of recipients disclosed; no individual names | Named third-party vendor list accessible in preference centre |

### Domain 6: Cookie Wall

| Criterion | NON-COMPLIANT | REQUIRES REMEDIATION | COMPLIANT |
|-----------|--------------|---------------------|-----------|
| Service conditioned on consent (non-LOP) | Access denied without accepting non-essential cookies | Reduced functionality threatened (not full denial) | Full service accessible without non-essential consent |
| "Consent or pay" (non-LOP) | Pay-or-consent model with no alternative | Pay-or-consent with very low-cost alternative | No pay-or-consent model |
| "Consent or pay" (Large Online Platform) | Any pay-or-consent model without "truly equivalent" free option | Free option available but materially inferior in features | Not applicable (not a Large Online Platform) |

### Domain 7: Withdrawal Mechanism

| Criterion | NON-COMPLIANT | REQUIRES REMEDIATION | COMPLIANT |
|-----------|--------------|---------------------|-----------|
| Withdrawal mechanism exists | No persistent mechanism accessible on site | Link exists but not in standard location (footer/header) | Persistent, clearly labelled mechanism on all pages |
| Withdrawal effectiveness | Previously set cookies not deleted on withdrawal | Cookies expire on next visit (not current session) | Cookies deleted or expired immediately on withdrawal |
| Withdrawal ease | Withdrawal requires significantly more steps than giving consent | Withdrawal requires 1-2 extra steps | Comparable steps for withdrawal and acceptance |

### Domain 8: Tracking Technology Scope

| Criterion | NON-COMPLIANT | REQUIRES REMEDIATION | COMPLIANT |
|-----------|--------------|---------------------|-----------|
| Local storage tracking | Tracking identifiers written to localStorage before consent | Local storage used post-consent but gating inconsistent | localStorage tracking gated behind consent |
| Fingerprinting | Canvas/WebGL/audio fingerprinting on page load | Fingerprinting script present; timing uncertain | No fingerprinting; or gated behind explicit consent |
| Pixel tracking | Tracking pixels fire before consent | Pixel request detected; no data confirmed sent | Pixels blocked until consent given |
| Server-side tagging | Server-side tags bypass CMP consent gating | Server-side tags present; consent signal propagation unverified | Server-side tags receive and honour CMP consent signal |
| CNAME cloaking | First-party subdomain proxies third-party analytics; no consent gating | CNAME proxying present; consent mechanism in place | No CNAME cloaking; or CNAME proxy with correct consent gating |

### Domain 9: Consent Record Completeness

| Criterion | NON-COMPLIANT | REQUIRES REMEDIATION | COMPLIANT |
|-----------|--------------|---------------------|-----------|
| Records exist | No consent records maintained | Records maintained but with incomplete required fields | Full records containing all required fields |
| Retrievability | Records cannot be retrieved for a specific user/device ID | Retrievable but only through slow, manual process | Records retrievable on demand by cookie/device ID |
| Retention period | Records deleted within 90 days | Records retained 1–2 years | Records retained 3+ years |
| Tamper evidence | Records stored in mutable plain text | Records in database with basic integrity controls | Records in tamper-evident, encrypted storage |

### Domain 10: US GPC and UOOM Compliance

[JURISDICTION-SPECIFIC — US STATES]

| Criterion | NON-COMPLIANT | REQUIRES REMEDIATION | COMPLIANT |
|-----------|--------------|---------------------|-----------|
| GPC honoring (California) | GPC signal completely ignored | GPC detected; processing delayed or partial | GPC honored immediately as full opt-out |
| DNSS link (California) | No "Do Not Sell or Share" link on homepage | Link present but below the fold or hard to find | Prominent link or functional GPC mechanism on homepage |
| Multi-state UOOM | No UOOM honoring in any applicable state | Partial state coverage (e.g., California only) | All applicable state UOOMs honored |
| Non-discrimination | Service degraded or pricing changed for GPC opt-out users | Minor service differences for opt-out users | Full service and pricing parity for opt-out users |

### Domain 11: Google Consent Mode v2

[JURISDICTION-SPECIFIC — where Google Ads / GA4 deployed]

| Criterion | NON-COMPLIANT | REQUIRES REMEDIATION | COMPLIANT |
|-----------|--------------|---------------------|-----------|
| Default signal states | Any signal defaults to `granted` before consent | Signals initialised late (after page load, before consent) | All four signals default to `denied` on page load |
| Signal accuracy | Signals do not reflect user's actual consent choice | Signals update correctly but with noticeable delay | Signals update accurately and immediately on consent |
| Signal granularity | Single granted/denied for all four signals (no differentiation) | Partial granularity | All four signals independently and accurately set per consent category |

### Domain 12: Analytics Exemption Claims

[JURISDICTION-SPECIFIC — French sites claiming CNIL analytics exemption; UK sites post-DUAA]

| Criterion | NON-COMPLIANT | REQUIRES REMEDIATION | COMPLIANT |
|-----------|--------------|---------------------|-----------|
| Tool qualification | Google Analytics claimed as exempt tool | Qualifying tool (Matomo) deployed but configuration not verified | Qualifying tool with documented CNIL-compliant configuration |
| Cookie lifetime | Analytics cookies > 13 months | Analytics cookies 13–25 months | Analytics cookies ≤ 13 months |
| IP pseudonymisation | Full IP addresses in analytics data | Last byte removed for city-level tracking only | Final byte (or more) removed after geolocation |
| Session replay | Session replay tool included in analytics exemption | Session replay on separate consent category (not exemption) | No session replay under any analytics exemption claim |
| Cross-referencing | Analytics data merged with CRM or advertising data | Analytics and advertising use separate IDs with possible linkage | Strict data silo; verifiable non-referencing |

---

## Prioritisation Framework

### Critical (Remediate within 30 days)

These violations trigger the largest enforcement fines and are the primary focus of CNIL
and ICO sweeps:

- Pre-consent script/pixel/cookie firing — most-fined violation; CNIL enforcement sweeps target this first
- No "Reject All" equivalent at first layer — core EDPB/CNIL requirement; fined Google €150M, Facebook €60M
- Cookie wall (service conditioned on non-essential consent) — prohibited; EDPB Opinion 08/2024
- GPC honoring failure in California — mandatory; CPPA/AG joint enforcement sweeps (September 2025)
- All Consent Mode v2 signals defaulting to `granted` — directly contradicts GDPR consent conditions

### High (Remediate within 90 days)

- Pre-ticked checkboxes at any banner layer
- Consent-by-scrolling or browsing mechanisms
- Withdrawal mechanism absent or non-functional (Article 7(3) GDPR)
- Analytics or session recording tools classified as "strictly necessary"
- Consent records not retained or not retrievable
- Multi-state UOOM non-compliance (Colorado, Connecticut, and others)
- Server-side tagging bypassing CMP consent gating

### Medium (Remediate within 180 days)

- Mild visual asymmetry in accept/reject buttons (not extreme; not enforcement-level yet)
- Vague category descriptions (imprecise but not deceptive)
- Withdrawal mechanism present but marginally harder than giving consent
- Consent records retained < 3 years (but > 1 year)
- IAB TCF/GPP string minor inaccuracies that may not affect actual vendor behaviour
- Analytics exemption claim with 1–2 conditions partially satisfied

### Low (Best Practice — Address in next CMP refresh)

- Cookie policy last updated > 12 months ago (even if currently accurate)
- Third-party vendor categories listed rather than individual vendor names
- Consent UI not tested on mobile devices for parity with desktop
- No explicit re-consent trigger mechanism configured in CMP version control
- Re-consent period not configured in CMP (relying on users returning voluntarily)

---

## Anti-Patterns Catalogue

What NOT to do in cookie and tracking technology compliance. These are the most common
mistakes observed across EU enforcement actions, EDPB audit findings, and practical
implementation review.

1. **"GTM loads before the CMP"** — Google Tag Manager is deployed with all tags configured
   to fire on page load, bypassing consent gating. GTM must be configured to wait for the CMP
   consent state before any tag fires. Use the built-in GTM Consent Mode integration or a
   CMP-triggered trigger in GTM.

2. **"Analytics is strictly necessary"** — Google Analytics, GA4, or any third-party analytics
   tool is classified as strictly necessary to avoid consent requirements. No analytics tool
   meets the two-part strictly necessary test. CNIL has explicitly rejected this argument.

3. **"We just need one toggle"** — Consent UI offers a single Accept/Decline toggle with no
   category granularity. Where GDPR applies, separate consent is required for separate purposes.
   A single toggle is non-compliant.

4. **"We'll put the Reject button in preferences"** — "Accept All" appears at the first banner
   layer; rejection requires clicking "Manage Preferences" and navigating a preference centre.
   Cookie Banner Taskforce Report (January 2023) identifies this structure as a core violation.

5. **"Grey reject button is fine"** — "Accept" is a bright, branded-colour button; "Reject" is
   grey, smaller, or styled as plain text. EDPB Guidelines 03/2022 (Dark Patterns) prohibits this
   visual asymmetry. Both buttons must have equivalent visual prominence.

6. **"Hotjar is a performance tool"** — Session recording tools (Hotjar, Microsoft Clarity,
   FullStory, LogRocket) are classified in a "performance" or "functional" category and treated as
   strictly necessary or low-risk. Session recording is not technically necessary for any user-requested
   service and requires explicit consent. The CNIL analytics exemption explicitly excludes session replay.

7. **"We use Consent Mode v2 — we're fine"** — Consent Mode v2 is a data collection mechanism, not
   a consent substitute. The consent banner must still collect genuine, informed consent. Consent Mode
   Basic Mode is the minimum compliant configuration; Advanced Mode with "modelled conversions" from
   non-consented users creates additional legal risk.

8. **"Our CMP fires a 'default granted' signal"** — Consent Mode v2 signals default to `granted`
   for analytics or advertising before user interaction. The EDPB position: defaulting to `granted`
   without explicit user action violates GDPR consent conditions.

9. **"Scrolling equals consent"** — Site treats continued scrolling, page views, or "using the site"
   as acceptance of non-essential cookies. Explicitly prohibited since EDPB Guidelines 05/2020. This
   alone would constitute a reportable NOYB complaint.

10. **"Cookie withdrawal would delete our data"** — Organisation resists implementing a functional
    withdrawal mechanism because it would require deleting associated personal data. Withdrawal of
    consent triggers the obligation to cease processing and delete associated data (Article 17 GDPR).
    This is not a compliance problem to avoid — it is the correct legal outcome.

11. **"We don't need consent logs — we use a CMP"** — Deploying a CMP does not automatically satisfy
    the Article 5(2) accountability obligation. The organisation must be able to produce a specific
    consent record for a specific user upon regulatory request. CMP consent logs must be actively
    configured, tested, and retained.

12. **"The CNIL exemption covers Google Analytics"** — Google Analytics does not qualify for the CNIL
    analytics exemption. CNIL has explicitly confirmed this. Only site-specific, single-scope analytics
    tools configured without cross-site tracking may qualify.

13. **"Our CNAME cloaking makes analytics first-party"** — Using a CNAME record to proxy Google
    Analytics or similar tools through a first-party subdomain does not change the legal analysis.
    The third-party data controller still processes the data; the consent obligation applies
    regardless of the DNS configuration.

14. **"We updated our cookie policy — re-consent isn't needed"** — Updating the cookie policy text
    without re-collecting consent when tracking purposes have materially changed is non-compliant.
    Re-consent is required whenever the scope of what users consented to changes materially.

15. **"We handle GPC for California only"** — GPC must be honored in all applicable US states. As of
    mid-2025, this includes at least 10 states. Limiting GPC honoring to California creates multi-state
    regulatory exposure, particularly with the September 2025 joint enforcement sweep.

16. **"Local storage is not a cookie"** — Using `localStorage` or `sessionStorage` to persist tracking
    identifiers before consent is non-compliant. EDPB Guidelines 2/2023 confirm that Article 5(3)
    applies to all storage on terminal equipment, not only HTTP cookies. Local storage is in scope.

17. **"'We use cookies' is sufficient disclosure"** — A bare statement that cookies are used, without
    identifying the controller, purposes, third parties, retention periods, and right to withdraw, is
    below the Cookie Banner Taskforce Report (January 2023) minimum threshold. Bare disclosure notices
    are routinely cited in NOYB complaints.

18. **"Analytics tracking is not a 'sale' of data"** — If analytics data is shared with third parties
    (including Google, Meta, or ad networks) for any purpose, it may constitute "sharing" under
    California CCPA/CPRA even without monetary exchange. "Do Not Sell or Share" covers cross-context
    behavioral advertising, not only direct commercial sales.

19. **"Social media share buttons are decorative"** — Social media "Like," "Share," and "Follow" buttons
    that embed SDK code from social platforms (Facebook, Twitter/X, LinkedIn) automatically initiate
    data transfer to those platforms on page load. They are not decorative; they require consent gating.

20. **"Server-side tagging is first-party data collection"** — Server-side tagging does not exempt the
    organisation from consent obligations. If server-side tags collect and process data before the CMP
    has transmitted a valid consent signal, the processing is non-compliant regardless of whether the
    endpoint appears first-party from the client side.

21. **"Analytics exemption means no cookie lifetime limit"** — The CNIL analytics exemption specifies a
    maximum cookie lifetime of 13 months. Analytics cookies with longer lifetimes do not qualify for
    the exemption, even if all other conditions are satisfied.

22. **"Consent records are just server logs"** — Web server access logs are not consent records. Consent
    records must specifically capture: what the user consented to per category, when, under which banner
    version, from which device. Generic server access logs cannot satisfy the GDPR accountability
    obligation under Article 5(2).

23. **"We checked compliance once at launch"** — Cookie compliance requires ongoing monitoring. Third-party
    vendors update their tracking implementations; CMP configurations drift; new trackers are added
    through ad campaigns. Static one-time audits become stale within months.

---

## Writing Standards

Apply these standards before delivering any audit output:

1. **Classify before explaining** — State the classification (NON-COMPLIANT / REQUIRES REMEDIATION /
   COMPLIANT) before the explanation. Legal and technical teams need the conclusion first.

2. **Cite the authority** — Every non-compliance finding must name the specific EDPB Guideline, Directive
   article, SA decision, or national law. Vague references to "GDPR" or "cookie law" are insufficient.

3. **Specify the exact failure** — "Pre-consent cookies detected" is insufficient. State: which cookies
   or domains, at what point in the user journey, what the cookie/script does, and which consent
   category it should be in.

4. **Include the remediation step** — Every finding must be paired with a concrete, technically actionable
   remediation step. Do not describe the problem without describing the fix.

5. **Distinguish EU from US findings** — Do not conflate ePrivacy opt-in consent requirements (EU/UK)
   with CCPA opt-out rights (US). Present them in separate sections where both apply.

6. **Flag evolving law explicitly** — UK DUAA analytics exceptions, multi-state UOOM expansion, CCPA 2026
   revised regulations, and Consent Mode Advanced Mode status are all evolving. Mark these clearly with
   [VERIFY — evolving law] and recommend re-audit once guidance is finalised.

7. **Avoid speculation** — Do not classify a finding as NON-COMPLIANT if the confidence score is below
   0.60. At Possible/Uncertain levels, present both sides and recommend professional legal review.

8. **Quantify enforcement risk** — Where enforcement precedent exists, cite the enforcement data. Fine
   amounts and violation types drive remediation urgency more effectively than abstract legal citations.

9. **Separate technical observations from legal conclusions** — Describe what was technically observed
   (network request, cookie name, consent signal value) and then separately state the legal conclusion.
   This makes the report defensible and easier for technical teams to act on independently.

10. **Plain language for technical remediations** — The remediation section will be read by engineers.
    Avoid legal jargon in technical remediation steps. Use specific instructions (CMP setting names,
    GTM configuration steps, Chrome DevTools paths).

---

## External Tool Integration

### legalcode-mcp (Preferred for Legal Research)

Use **legalcode-mcp** to verify and supplement legal authority in audit output:

**Queries to run:**
- EDPB Guidelines on cookie consent and ePrivacy Directive Article 5(3) — verify current versions and any updates post-October 2024
- National SA guidance (CNIL, ICO, DSK) — retrieve current guidance documents and verify publication dates
- Enforcement decisions — verify fine amounts, violation types, and dates for enforcement precedents cited
- DUAA (UK) cookie exceptions — verify current ICO guidance implementing the DUAA analytics exceptions
- US state UOOM status — verify the current list of states with active UOOM requirements

**Save verified sources** to `/tmp/legalcode-cookie-research.md` and reference in the Glass Box audit trail.

**Without legalcode-mcp connected:**
- Mark all statutory and SA guidance references with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Direct the user to verify enforcement precedents via the GDPR Enforcement Tracker
  (enforcementtracker.com) and official supervisory authority websites
- Note: all fine amounts and regulatory guidance in this skill are current as of 2026-03-02
  training data [VERIFY — check official SA sources for updates]

### Automated Cookie Scanning Tools

The audit may be informed by output from external scanning tools:

| Tool | Best For | Limitations |
|------|----------|-------------|
| **Cookiebot** | Comprehensive cookie inventory; automated category detection | May miss JavaScript-only trackers |
| **OneTrust Cookie Scan** | Enterprise sites; maps cookies to CMP categories | Requires OneTrust CMP deployment |
| **Termly** | SME sites; automated classification | Limited deep technical audit depth |
| **Chrome DevTools** | Manual pre-consent blocking test; Consent Mode v2 signal inspection | Requires manual execution; examiner expertise needed |
| **Google PSAT** | Privacy Sandbox / cookie analysis; debugging first-party sets | Google-specific focus |
| **Privado.ai** | Automated CMP compliance monitoring; ongoing drift detection | Commercial service |
| **Nixon Digital scanner** | Specifically identifies cookies firing before consent | Focused scope |

---

## Glass Box Audit Trail

Every audit must complete this template, included at the end of the audit report:

```yaml
glass_box:
  skill_name: "legalcode-cookie-compliance-audit"
  audit_target: "[URL or site description]"
  audit_date: "[YYYY-MM-DD]"
  jurisdiction:
    eu_eprivacy: "[Applicable / Not applicable]"
    uk_pecr: "[Applicable / Not applicable]"
    us_ccpa_gpc: "[Applicable / Not applicable]"
    us_state_uoom: "[States: list / Not applicable]"
  cmp_deployed: "[CMP name and version / None identified / Unknown]"
  ad_tech_in_scope: "[Yes / No / Unknown]"
  google_consent_mode_v2: "[In scope / Not in scope]"
  audit_scope: "[Full / Pre-consent only / Banner UX only / US GPC only / Analytics exemption only]"
  automated_scan_used: "[Tool name and version / None — live technical access used / None]"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[/tmp/legalcode-cookie-research.md / Not created]"
  findings_summary:
    non_compliant: "[number]"
    requires_remediation: "[number]"
    compliant: "[number]"
  top_3_critical_findings: "[list by enforcement risk]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED — marked [VERIFY]]"
  evolving_law_flags:
    - "[UK DUAA analytics exception: ICO guidance pending as of mid-2025]"
    - "[US state UOOM: verify current state list against state AG guidance]"
    - "[CCPA 2026 revised regulations: verify final text effective January 1, 2026]"
    - "[Consent Mode Advanced Mode: EDPB/CNIL position evolving — mark [VERIFY]]"
  limitations:
    - "[Technical live-site audit not performed — analysis based on scan report only (if applicable)]"
    - "[Mobile app not in scope (if applicable)]"
    - "[Server-side tagging configuration not reviewed (if applicable)]"
    - "[Any other material scope limitations]"
  reviewer: "AI-assisted — requires qualified privacy counsel review"
```

---

## Output Format Template

Deliver the audit report in this format:

---

# Cookie Compliance Audit Report

**Site:** [URL or description]
**Audit date:** [YYYY-MM-DD]
**Prepared by:** legalcode-cookie-compliance-audit (AI-assisted)
**Jurisdiction scope:** [EU / UK / US / Multinational]
**Audit scope:** [Full / Limited — describe]

> This report is AI-assisted and does not constitute legal advice. All findings should
> be reviewed by qualified privacy counsel before remediation decisions are finalized.

---

## Regulatory Obligations Summary

| Regime | Applicable? | Primary SA | Enforcement Risk Level |
|--------|------------|-----------|------------------------|
| EU ePrivacy / GDPR | [Yes/No] | [CNIL / DPC / AEPD / DSK / other] | [HIGH/MEDIUM/LOW] |
| UK PECR / UK GDPR | [Yes/No] | ICO | [HIGH/MEDIUM/LOW] |
| US CCPA / GPC | [Yes/No] | CPPA / CA AG | [HIGH/MEDIUM/LOW] |
| US State UOOMs | [Yes/No — list states] | State AGs | [HIGH/MEDIUM/LOW] |

---

## Executive Summary

[2–3 paragraph summary of overall compliance posture, top 3 findings by enforcement risk,
and overall remediation recommendation.]

**Overall Assessment:** [NON-COMPLIANT / PARTIALLY COMPLIANT / COMPLIANT]

| Priority | Count |
|----------|-------|
| Critical findings | [N] |
| High priority | [N] |
| Medium priority | [N] |
| Best practice gaps | [N] |

---

## Critical Findings (Remediate within 30 days)

### Finding C-[N]: [Finding Title]

**Classification:** NON-COMPLIANT
**Audit domain:** [Domain name]
**Confidence:** [Definite/High/Probable] ([score range])
**Regulatory basis:** [Specific EDPB Guideline / Directive Article / SA guidance citation]
**Enforcement precedent:** [Cite relevant SA fine or enforcement action if applicable]

**Observed behaviour:**
[Precise technical description of what was found — cookie name, domain, network request,
console output, or scan report finding]

**Why it is non-compliant:**
[Legal analysis citing the specific provision and how the observation maps to the violation]

**Remediation:**
[Specific, technically actionable steps to fix — CMP configuration, GTM trigger change,
script removal, developer action required]

**Verification test:**
[How to confirm the fix is effective — DevTools step, scan to re-run, or signal to check]

---

[Repeat structure for each Critical finding]

---

## High Priority Findings (Remediate within 90 days)

[Same structure as Critical findings, abbreviated where appropriate]

---

## Medium Priority Findings (Remediate within 180 days)

[Same structure]

---

## Best Practice Gaps (Address in next CMP refresh)

- [Brief description and recommendation for each]

---

## US Opt-Out Compliance Assessment

### GPC Test Results

| State | GPC Honoring Status | DNSS Link Present | Assessment |
|-------|--------------------|--------------------|------------|
| California | [Honored / Ignored / Partial] | [Yes/No] | [COMPLIANT/NON-COMPLIANT] |
| Colorado | [Honored / Ignored / Partial] | N/A (UOOM-based) | [COMPLIANT/NON-COMPLIANT] |
| [Other applicable states] | | | |

### UOOM Compliance Summary
[State-by-state assessment of universal opt-out mechanism compliance]

---

## Analytics Exemption Assessment

[JURISDICTION-SPECIFIC — complete only if French site claiming CNIL exemption or UK site post-DUAA]

| Condition | Status | Notes |
|-----------|--------|-------|
| Tool qualification | [Met / Not met] | [Tool name; qualifying status] |
| Cookie lifetime ≤ 13 months | [Met / Not met] | [Actual lifetime observed] |
| IP pseudonymisation | [Met / Not met] | [Configuration verified / unverified] |
| No session replay | [Met / Not met] | [Tools found] |
| No cross-referencing | [Met / Not met] | [Data flows identified] |
| Anonymous output only | [Met / Not met] | [Verification method] |

**Exemption eligibility:** [ELIGIBLE / NOT ELIGIBLE / UNCERTAIN — requires verification]

---

## Tracking Technology Inventory

| Technology | Vendor | Pre-consent? | CMP Category | Assessment |
|------------|--------|-------------|-------------|------------|
| Google Analytics (GA4) | Google | [Yes/No] | [Strictly necessary / Analytics] | [NON-COMPLIANT / COMPLIANT] |
| Meta Pixel | Meta | [Yes/No] | [Marketing] | [NON-COMPLIANT / COMPLIANT] |
| [Additional entries] | | | | |

---

## Consent Record Assessment

| Criterion | Status | Evidence |
|-----------|--------|---------|
| Records maintained | [Yes/No] | [CMP name; confirmation source] |
| All required fields present | [Yes/Partial/No] | [Missing fields if partial] |
| Records retrievable by user/device ID | [Yes/No] | [Tested / Untested] |
| Retention period | [X months/years] | [Source] |
| Tamper evidence | [Present/Absent] | [Storage method] |

---

## Remediation Checklist

| Priority | Finding | Remediation Action | Owner | Target Date | Status |
|----------|---------|-------------------|-------|-------------|--------|
| Critical | [finding title] | [specific action] | [Technical/Legal/Both] | [YYYY-MM-DD] | ☐ |
| High | [finding title] | [specific action] | | | ☐ |
| Medium | [finding title] | [specific action] | | | ☐ |

---

## Glass Box Audit Trail

[Insert completed YAML template from Step 12]

---

## Recommended Next Steps

1. **Immediate (Week 1)**: [Critical remediations — pre-consent blocking, reject-all parity, GPC]
2. **Short-term (30 days)**: [High-priority remediations]
3. **Legal review**: Engage qualified privacy counsel to review [specific findings with legal ambiguity, especially DUAA analytics exception scope and Consent Mode Advanced Mode status]
4. **Re-audit**: Schedule follow-up audit 60 days after remediation implementation
5. **Ongoing monitoring**: Configure automated CMP compliance monitoring to detect drift (new tags, CMP configuration changes, third-party vendor updates)
6. **Documentation**: Update cookie policy, ROPA entry (Art. 30 record), and vendor DPAs to reflect current post-remediation implementation

---

*Report generated by legalcode-cookie-compliance-audit. AI-assisted analysis — not legal advice. Qualified privacy counsel review required before action.*

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis from deep legal research across:
- EDPB Guidelines 05/2020 on Consent (v1.1); EDPB Guidelines 2/2023 v2.0 (Technical Scope of
  Art. 5(3) ePrivacy Directive, October 2024); EDPB Cookie Banner Taskforce Report (January 2023);
  EDPB Guidelines 03/2022 on Deceptive Design Patterns (v2.0, February 2023); EDPB Opinion
  08/2024 on "Consent or Pay" Models
- CNIL cookie guidelines including July 2025 analytics exemption update; CNIL enforcement
  actions (Google €325M, SHEIN €150M, September 2025; Google €150M, Facebook €60M, January 2022;
  Yahoo €10M, December 2023)
- ICO storage and access technologies guidance (current as of mid-2025; DUAA update pending)
- German DSK Orientierungshilfe v1.2 (November 2024) on TDDDG requirements and CMP implementation
- California CCPA/CPRA and CPPA GPC guidance; revised CCPA regulations (effective January 1, 2026)
- Multi-state UOOM requirements (Colorado July 2024; Connecticut January 2025; additional states)
- IAB Tech Lab Global Privacy Platform (GPP) Implementation Guidelines (February 2025)
- GDPR Enforcement Tracker enforcement precedents and DPC €652M 2024 enforcement report
- Chrome DevTools and Google Consent Mode v2 technical audit methodology
- Agent-team-assisted research pipeline: Structural Analyst agent (repository pattern extraction +
  domain analysis) and Legal Research Agent (web-backed regulatory research with source citations)
  operating in parallel

No external skills were imported. All legal content is synthesized from primary regulatory sources,
enforcement precedents, and supervisory authority guidance.
