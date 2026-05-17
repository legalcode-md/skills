---
title: Cookie Policy — EU/EEA (ePrivacy + GDPR + DE-TTDSG/TDDDG)
jurisdictions: [eu, eea, de]
statutes: [ePrivacy-2002/58/EC, GDPR, TTDSG, TDDDG, BDSG]
license: MIT
last_updated: 2026-04-28
---

# Cookie Policy — EU/EEA (ePrivacy + GDPR + DE-TTDSG/TDDDG)

**Effective date:** {{Effective Date}}
**Operator:** {{Company Legal Name}} ({{Company Trading Name}})
**Establishment:** {{Member State Of Establishment}}
**Lead supervisory authority:** {{Supervisory Authority}}

---

## 1. Plain-language summary

In short: when you visit `{{Website Domain}}` or use `{{Service Name}}`, we and selected partners place small files (cookies) and use comparable technologies on your device. For anything not strictly necessary to deliver what you asked for, we ask permission before reading or writing to your device, and you can change your mind at any time.

The legal anchor is **Article 5(3) of the ePrivacy Directive (2002/58/EC, as amended)**: storing information, or gaining access to information already stored, on a user's terminal equipment is only lawful with prior informed consent — except where strictly necessary to deliver an information-society service the user explicitly requested, or to carry out the transmission of a communication.

Where consent is required, the **GDPR** sets the bar. **Article 6(1)(a)** establishes consent as a lawful basis, and **Article 7** with **recital 32** requires consent to be:

- **Freely given** — without coercion, bundling, or detriment for refusal
- **Specific** — granular per purpose
- **Informed** — based on clear information about who, what, why, and how long
- **Unambiguous** — through a clear affirmative action (no pre-ticked boxes, no inferred consent)
- **Revocable** — as easy to withdraw as to give

This policy is read alongside our companion {{Privacy Policy URL}} and, where applicable, our Data Processing Addendum {{DPA URL}}.

---

## 2. What cookies and similar technologies are

A cookie is a small text file that a website asks your browser to store and return on later visits. The legal regime, however, reaches well beyond cookies.

The **EDPB Guidelines 2/2023 on the technical scope of Article 5(3) of the ePrivacy Directive** clarify that Article 5(3) applies to *any* operation that stores information on, or accesses information stored in, a user's terminal equipment — regardless of underlying technology `[VERIFY EDPB Guidelines 2/2023 specifics]`. This includes:

- HTTP cookies (session and persistent)
- HTML5 local storage, session storage, and IndexedDB entries
- Service workers and cache storage
- Pixel tags, web beacons, and tracking pixels
- Device fingerprinting (active and passive)
- IoT device identifiers and connected-device telemetry
- Identifiers conveyed in URLs and linked to information already on the device
- IP-based identifiers, in some cases, where they function as device identifiers `[VERIFY EDPB scope]`
- SDKs embedded in mobile applications that read or write to local storage

**Plain English:** if a feature on `{{Website Domain}}` writes anything to your device or reads anything already there, the same rules apply — even if the word "cookie" never appears.

---

## 3. Why we use them

We use cookies and similar technologies for two broad reasons: to make the service work, and — only if you opt in — to measure usage, improve the service, and (where applicable) help fund it.

European law splits this into two regimes:

- **Strictly necessary — exempt from consent.** Article 5(3) ePrivacy carves out two narrow exemptions: the *carrier exception* (sole purpose of carrying out a communication transmission) and the *service-requested-by-the-user exception* (strictly necessary for delivering a service the user has explicitly requested). Authentication tokens, load-balancer routing, shopping-cart state, and CSRF protections fall here.
- **All others — consent required.** Anything else — most analytics, A/B testing, personalisation, advertising, social-media plug-ins, re-marketing — requires prior Article 5(3) consent meeting the Article 6(1)(a) / Article 7 GDPR quality standard described in §1.

We do not rely on **legitimate interests (Art. 6(1)(f) GDPR)** as a substitute for Article 5(3) consent.

---

## 4. Categories of cookies we use

We group the technologies we deploy into five categories. For each, we set out the Article 5(3) treatment and the consent posture we apply.

### 4.1 Strictly necessary

**Examples:** session authentication, CSRF tokens, load-balancer affinity, cookie-consent state, shopping-cart contents, fraud-prevention tokens.

**Art. 5(3) treatment:** exempt under the *service-requested-by-the-user* or *carrier* exception. We still disclose them under **GDPR Articles 13/14**.

**Posture:** load on first visit; cannot meaningfully be disabled without breaking the service.

### 4.2 Functional / preferences

**Examples:** language and locale selection, region settings, UI theme, recently viewed items.

**Art. 5(3) treatment:** consent required. Neither Article 5(3) nor the EDPB recognise a generic "functional" exemption.

**Posture:** off by default; loaded only after opt-in.

### 4.3 Analytics / performance

**Examples:** aggregate page-view counts, error and crash telemetry, feature-usage measurement, heat-mapping.

**Art. 5(3) treatment:** consent required as a default. Some Member-State authorities (notably France's CNIL) and the EDPB Guidelines 2/2023 recognise a narrow "audience-measurement" carve-out for first-party, non-shared, strictly-scoped analytics meeting specific safeguards `[VERIFY MS-specific audience-measurement carve-out]`. We do not rely on this carve-out by default.

**Posture:** off by default; loaded only after opt-in.

### 4.4 Advertising / marketing

**Examples:** retargeting pixels, conversion-tracking tags, ad-platform identifiers, attribution measurement.

**Art. 5(3) treatment:** consent required. The **EDPB Cookie Banner Taskforce Report (January 2023)** addresses common failures — unequal Accept/Reject prominence, deceptive design, pre-ticked checkboxes — and we designed our banner against those findings.

**Posture:** off by default. We do not deploy IAB Transparency and Consent Framework signals.

### 4.5 Social media

**Examples:** embedded share buttons, "log in with" buttons, embedded video / post players that set identifiers on load.

**Art. 5(3) treatment:** consent required. Social-media plug-ins frequently raise **GDPR Article 26** joint-controllership concerns. The CJEU held in **Wirtschaftsakademie Schleswig-Holstein (C-210/16)** and **Fashion ID (C-40/17)** that an operator embedding a social-media component can be a *joint controller* with the platform for the collection and transmission triggered by the embed.

**Posture:** off by default. Where you opt in, we disclose the joint-controller relationship and link to the platform's joint-controller arrangement.

---

## 5. Specific cookies we use

A current inventory — name, provider, purpose, category, duration, first/third party — is set out in **Annex A**.

We update Annex A whenever we add, remove, or materially change a cookie or vendor. If Annex A and the body of this policy disagree, Annex A controls.

DPOs and auditors may request a current Cookie Register and an Article 30 GDPR Records of Processing Activities extract from {{Company Email Privacy}}.

---

## 6. Third-party cookies & subprocessors

Some cookies on `{{Website Domain}}` are set by third parties whose code we have embedded. The **legal relationship** with each determines responsibility and the contractual instrument governing the data flow. We classify every third-party cookie into one of three categories:

### 6.1 Processor (GDPR Art. 28)

The third party processes personal data **on our behalf and on our documented instructions**. We are the controller; they are the processor, governed by an **Article 28 GDPR DPA**. The processor may not use the data for its own purposes.

Typical examples: hosted analytics in a controller-only mode, error-monitoring, session-replay tools.

Our companion **Data Processing Addendum** ({{DPA URL}}) lists each Art. 28 subprocessor, processing purpose, location, transfer mechanism, and audit rights.

### 6.2 Joint controller (GDPR Art. 26)

We and the third party **jointly determine the purposes and means of processing**. Article 26 requires us to make the *essence* of the joint-controllership arrangement available to you.

Typical examples: the **Meta Pixel** (joint controllership for the collection-and-transmission step under **Fashion ID, C-40/17**), Facebook Page-Insights integrations (**Wirtschaftsakademie Schleswig-Holstein, C-210/16**), certain LinkedIn Insight Tag deployments.

For each joint-controller relationship in Annex A, we link to the platform's joint-controller arrangement and summarise the allocation of responsibilities.

### 6.3 Independent controller

The third party determines the purposes and means of processing **for its own purposes**. We cause your browser to contact the third party (typically via an embedded tag or pixel); the third party then processes under its own controllership and privacy notice.

Typical examples: embedded video providers in cookie-enabled mode, payment processors setting anti-fraud cookies, CDNs setting device-level identifiers for their own services.

For each independent-controller entry in Annex A we identify the controller and link to its privacy notice.

---

## 7. Your choices & how to manage cookies

You control every non-essential cookie. The fastest path is the cookie settings centre at `{{Cookie Settings URL}}`, also reachable from a persistent footer link on every page.

From the cookie settings centre you can:

- See every category we offer and what is currently enabled
- Toggle each non-essential category on or off
- Where feasible, toggle individual vendors within a category
- Save preferences (applied prospectively)
- Withdraw consent at any time, with friction equivalent to giving it

Key properties:

- **Default state.** Non-essential categories are **off** by default until you opt in.
- **"Reject all" parity.** "Reject all" appears on the first layer with **equal prominence** to "Accept all".
- **Granularity.** You can accept some categories and reject others.
- **Prospective effect.** Withdrawing consent stops further processing; it does not retroactively delete data lawfully collected via strictly-necessary cookies (which rest on the Art. 5(3) exemption, not consent).
- **No cookie wall.** Access does not require accepting non-essential cookies. Per **EDPB Guidelines 5/2020 §§ 39–41**, cookie walls generally invalidate consent absent compelling justification.
- **Consent management platform.** Our banner is operated by `{{Consent Management Platform}}`. We — not the CMP vendor — remain responsible for compliance.

---

## 8. Browser controls

Your browser also offers device-level controls that operate independently of our cookie settings centre. These are coarser — they affect every site — but they are a useful backstop.

In every major browser you can: block all third-party cookies; block all cookies (which will break most sites); delete stored cookies; set the browser to delete cookies on close; use private / incognito mode; configure per-site exceptions.

Provider documentation:

- Mozilla Firefox — `https://support.mozilla.org/kb/cookies-information-websites-store-on-your-computer`
- Google Chrome — `https://support.google.com/chrome/answer/95647`
- Apple Safari — `https://support.apple.com/guide/safari/manage-cookies-sfri11471/mac`
- Microsoft Edge — `https://support.microsoft.com/microsoft-edge`
- Brave — `https://support.brave.com/`

If you block or delete cookies, we will treat your next visit as fresh and re-prompt for consent.

---

## 9. Global Privacy Control (GPC) & Do Not Track (DNT)

**GPC** is a browser-level signal communicating a "do not sell or share" preference. **DNT** is an older header expressing a generic objection to tracking.

In the EEA, neither signal **substitutes for** ePrivacy consent:

- **Art. 5(3) requires affirmative opt-in.** A signal that says "I have not opted in" cannot, by itself, satisfy the *prior, specific, informed, unambiguous* consent standard.
- **GPC.** We treat GPC as a strong "do not collect" preference. If your browser sends GPC, we refrain from setting non-essential cookies and firing non-essential pixels even before you engage the banner. The banner remains available if you choose to opt in.
- **DNT.** Informational only. We log the header but do not change behaviour based on DNT alone. Where both are present, GPC controls.

---

## 10. How we obtain and record consent

Consent is engineered, not assumed. Our banner is designed against the **EDPB Cookie Banner Taskforce Report (January 2023)**, **EDPB Guidelines 5/2020 on consent**, **EDPB Guidelines 3/2022 on deceptive design patterns**, and the expectations of national supervisory authorities.

### 10.1 Before any non-essential cookie is set

The banner appears on the **first request** to `{{Website Domain}}` and **before** any non-essential cookie is written or read. Only strictly-necessary cookies (including the consent-state cookie itself) load before your choice.

### 10.2 Banner design

- **First layer.** "Accept all", "Reject all", and "Manage preferences" appear together with **equal visual prominence** — same colour, size, position; no nudging.
- **No pre-ticked boxes.** Confirmed by **Planet49 (CJEU C-673/17)** and the German **BVerwG / BGH** decisions cited in §15.
- **No cookie walls** (see §7).
- **No deceptive design patterns** — no confirmshaming, no hidden reject controls, no double-negative copy, no perpetually-reappearing modals.
- **Granular controls** — per-category toggles minimum, per-vendor where feasible.

### 10.3 Consent record

For every consent event we log: a pseudonymous user reference; UTC timestamp; banner version; vendor list and category descriptions shown; choices made (which categories accepted/rejected, in what order); language / locale; mechanism (banner, settings centre, API).

Records are retained for at least **12 months** after consent expires or is withdrawn (longer where a national supervisory authority expects it).

### 10.4 Re-prompt cadence

We re-prompt when: we add or materially change a category; we add a vendor that materially changes the scope of processing; previous consent reaches **12–24 months** (default: 12); a regulator or court ruling requires it.

### 10.5 Withdrawal

Withdraw at any time from `{{Cookie Settings URL}}` (footer link, every page). Withdrawal is **as easy as giving consent** — one click, no friction asymmetry.

---

## 11. International data transfers

Several third-party cookies — particularly analytics, advertising, and embedded social-media tags — transfer personal data outside the EEA. Common destinations: the US, the UK, and recipient group locations.

For each such transfer we rely on one of the **Chapter V GDPR** mechanisms:

- An **adequacy decision** under Art. 45 — including the EU-US Data Privacy Framework for certified US recipients
- **Standard Contractual Clauses** under Art. 46(2)(c)
- **Binding Corporate Rules** under Art. 47
- A **derogation** under Art. 49 — used sparingly

Where SCCs apply, we conduct a **Transfer Impact Assessment** in line with **EDPB Recommendations 01/2020** and **Schrems II (C-311/18)**, applying supplementary measures where warranted.

The detailed transfer-mechanism map per subprocessor is in our companion privacy policy (§9) and DPA (§14) at {{DPA URL}}.

---

## 12. Children's data

We do not direct `{{Website Domain}}` or `{{Service Name}}` at children, and we do not target advertising at children.

**Article 8 GDPR** sets the *age of digital consent* for information-society services offered directly to a child. The default age is **16**; Member States may lower it to **13**. An illustrative map `[VERIFY MS-specific Art. 8 ages]`:

| Member State | Age of digital consent |
| --- | --- |
| Germany, Ireland, Netherlands, Luxembourg, Slovakia | 16 |
| Austria, Hungary, Czechia, Lithuania, Cyprus, Bulgaria, Croatia | 16 (default) |
| France, Slovenia, Greece | 15 |
| Italy, Spain, Finland, Estonia, Malta | 14 |
| Belgium, Denmark, Portugal, Sweden, Latvia, Poland | 13 |

Below the applicable age, processing for an information-society service requires consent given or authorised by the holder of parental responsibility. We do not set non-essential cookies on a visitor we know or reasonably suspect to be below the applicable age without verified parental consent.

If you believe a child has interacted with `{{Website Domain}}` without the necessary parental consent, contact {{Company Email Privacy}} and we will delete the data and revoke any non-essential cookies set in that session.

---

## 13. Changes to this policy

We update this policy when the cookie inventory changes, EDPB or national supervisory authority guidance changes our practice, a court ruling requires it, or we add or remove a vendor.

For any **material** change (new processing purpose, new vendor expanding scope, change in transfer mechanism or retention) we will: update the "last updated" date; post a notice on `{{Website Domain}}` for a reasonable period; re-prompt for consent for the affected category before any new non-essential cookie is set on that basis.

For **non-material** changes (wording, typos, duration-column updates without scope change) we update in place and refresh the "last updated" date.

We maintain an internal change log; request it at {{Company Email Privacy}}.

---

## 14. Contact & complaints

You can reach us at:

- **Privacy enquiries:** {{Company Email Privacy}}
- **OPTIONAL — only if a DPO is appointed under Art. 37 GDPR.** Data Protection Officer: {{Company Email DPO}}
- **Postal address:** {{Company Postal Address}}
- **OPTIONAL — only if controller is established outside the EEA.** EU representative under Art. 27 GDPR: {{EU Representative}}

You have the right to lodge a complaint with a **supervisory authority** under **Article 77 GDPR** — at the supervisory authority of your habitual residence, place of work, or place of the alleged infringement. Our **lead supervisory authority** under the one-stop-shop (Arts. 56 / 60 GDPR) is `{{Supervisory Authority}}`. Exercising your Article 77 right does not require contacting us first.

---

## 15. Germany (DE-TTDSG / TDDDG) addendum

This addendum applies where `{{Website Domain}}` or `{{Service Name}}` is offered to users in **Germany** or otherwise falls within the scope of German telemedia / digital-services law. It supplements — and does not replace — sections 1–14 above.

### 15.1 Statute name and renaming

The German implementation of Article 5(3) of the ePrivacy Directive is **§ 25** of the **Telekommunikation-Telemedien-Datenschutz-Gesetz (TTDSG)**, which entered into force on 1 December 2021. With effect from **14 May 2024**, the TTDSG was renamed to the **Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz (TDDDG)** to align with the **Digital Services Act (Regulation (EU) 2022/2065)** terminology — "Telemedien" giving way to "digitale Dienste" `[VERIFY rename and effective date]`. The substantive cookie regime of § 25 was carried over essentially unchanged. Both names — TTDSG and TDDDG — may appear in regulator guidance, court decisions, and CMP documentation during the transition period; in this policy, references to "§ 25 TTDSG" and "§ 25 TDDDG" should be read as referring to the same provision.

### 15.2 § 25 TTDSG / TDDDG — the German Article 5(3)

**§ 25 (1) TTDSG / TDDDG** provides that the storage of information in the user's terminal equipment, and access to information already stored there, is only permissible with the user's **consent on the basis of clear and comprehensive information**. The information requirement is express; transparency is part of lawfulness, not an afterthought.

**§ 25 (2) TTDSG / TDDDG** sets out two narrow exceptions tracking Article 5(3) of the ePrivacy Directive:

1. The sole purpose is to carry out the transmission of a communication over an electronic communications network (the *carrier* exception), or
2. The storage or access is **strictly necessary** so that the provider of a digital service expressly requested by the user can deliver that service (the *strictly-necessary* exception).

Anything outside those two exceptions requires consent. § 25 (1) sentence 2 expressly requires that consent meet the **GDPR Article 4(11) and Article 7** standard — there is no German-specific lower bar.

### 15.3 DSK guidance

The **Datenschutzkonferenz (DSK)** — the standing conference of the German federal and Land data-protection supervisory authorities — has published guidance on consent under § 25 TTDSG / TDDDG, most prominently the **Orientation Guide for Telemedia Providers (Orientierungshilfe der Aufsichtsbehörden für Anbieter von Telemedien, OH Telemedien)**, updated in **December 2021** and in further iterations after the TDDDG rename `[VERIFY current DSK guidance version]`. Key DSK positions:

- "Accept all", "Reject all", and "Manage preferences" must be of **equal prominence** on the first layer.
- **No dark patterns**, no nudging, no asymmetric friction.
- **No pre-ticked checkboxes** for non-essential categories.
- **No cookie walls** without compelling justification, and equivalent alternatives must be offered.
- **Vendor-supplied consent management platforms** (Cookiebot, OneTrust, Usercentrics, and similar) are *not inherently compliant* — the controller remains responsible for verifying that the deployed configuration meets § 25 TTDSG / TDDDG and the GDPR. Buying a CMP does not buy compliance.

### 15.4 Competent supervisory authority — BfDI vs. Land LDA

The **Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)** is the federal supervisory authority. Each Land has its own data-protection authority (commonly the *Landesbeauftragte(r) für Datenschutz*, "LfD" or "LDA"). Competence is allocated as follows `[VERIFY current BfDI / LDA allocation]`:

- **B2C cookies on consumer-facing digital services (Telemedien / digitale Dienste)** — generally a Land LDA, determined by the establishment of the controller in Germany.
- **Federal authorities and telecoms-heavy services (TKG)** — generally the BfDI.

For our service, the competent German authority is `{{Supervisory Authority}}`.

### 15.5 Planet49 and the German case law

The Court of Justice's ruling in **Planet49 (C-673/17)**, applied by the **Bundesgerichtshof (BGH)** in **BGH I ZR 7/16, judgment of 28 May 2020 (Cookie-Einwilligung II)**, settled the active opt-in question for German law: a pre-ticked checkbox does not produce valid consent for non-essential cookies, and continued use of a site does not, by itself, constitute consent. The reasoning carries through to § 25 TTDSG / TDDDG.

**Bundesverwaltungsgericht (BVerwG)** decisions — including those in the freedom-of-information context (IFG opinions on consent and pre-ticked boxes) — have reinforced that pre-ticked controls are inadmissible where consent is the legal basis `[VERIFY specific BVerwG citations]`.

### 15.6 Transparency obligations: § 1 TMG / TDDDG, plus Art. 13/14 GDPR

The transparency obligations of the former **§ 1 TMG (Telemediengesetz)** carry over, in substance, to the **TDDDG**. They apply *on top of* the **GDPR Articles 13 and 14** transparency duties, not in place of them. In practice, this means:

- A separate, accessible **Impressum** under § 5 DDG / TMG.
- A privacy notice meeting **Art. 13/14 GDPR** for processing of personal data.
- A cookie disclosure meeting **§ 25 (1) TTDSG / TDDDG** ("clear and comprehensive information") *before* consent is requested.

### 15.7 The TKG / TDDDG dual regime

Two German statutes share the cookie/transparency landscape:

- **Telekommunikationsgesetz (TKG)** — traditional electronic-communications services (telecoms).
- **Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz (TDDDG)** — privacy in digital services and the cookie / terminal-equipment rule in § 25.

A typical website operator falls within the TDDDG (as a digital-service provider) and not within the TKG, but a service that combines hosted communications functionality with a website may touch both. Where both apply, we follow the stricter of the two.

### 15.8 Specific German banner-design notes

To the standard EU banner described in §10, we add for German users:

- The first-layer copy is available in **German** and labelled as such.
- The **Impressum** and **Datenschutzerklärung** links are accessible from the banner, not buried.
- The "Manage preferences" option is presented at the same prominence as "Accept all" and "Reject all" — DSK guidance treats unequal prominence between *Accept / Reject / Manage* as a compliance failure, not just unequal prominence between *Accept* and *Reject*.

### 15.9 German-language contact

For German-language privacy enquiries, please contact {{Company Email Privacy}}. Where applicable, the German DPO (**Datenschutzbeauftragte(r)**) is reachable at {{Company Email DPO}}. The competent German supervisory authority is `{{Supervisory Authority}}`.

---

## Annex A — Cookie inventory (Art. 5(3) ePrivacy classifications)

This annex lists every cookie and similar technology deployed on `{{Website Domain}}` and `{{Service Name}}`. It is the canonical source; if the body of this policy and Annex A diverge, Annex A controls.

| # | Name / identifier | Provider | First / third party | Category (§4) | Purpose | Duration | Domain | Art. 5(3) treatment | Relationship (§6) | Transfer destination (§11) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `{{Cookie Name 1}}` | `{{Provider 1}}` | First | Strictly necessary | Session authentication | Session | `{{Website Domain}}` | Exempt — service requested by user | n/a (controller) | EEA |
| 2 | `{{Cookie Name 2}}` | `{{Provider 2}}` | First | Strictly necessary | CSRF protection | Session | `{{Website Domain}}` | Exempt — service requested by user | n/a (controller) | EEA |
| 3 | `{{Cookie Name 3}}` | `{{Provider 3}}` | First | Strictly necessary | Cookie consent state | 12 months | `{{Website Domain}}` | Exempt — service requested by user | n/a (controller) | EEA |
| 4 | `{{Cookie Name 4}}` | `{{Provider 4}}` | First | Functional | Language / locale preference | 12 months | `{{Website Domain}}` | Consent required | Processor (Art. 28) | EEA |
| 5 | `{{Cookie Name 5}}` | `{{Provider 5}}` | First | Analytics | Aggregate page-view measurement | 13 months | `{{Website Domain}}` | Consent required | Processor (Art. 28) | EEA |
| 6 | `{{Cookie Name 6}}` | `{{Provider 6}}` | Third | Advertising | Conversion tracking | 90 days | `{{Provider 6 Domain}}` | Consent required | Joint controller (Art. 26) | US (SCCs + DPF where applicable) |
| 7 | `{{Cookie Name 7}}` | `{{Provider 7}}` | Third | Social media | Embedded share button | 24 months | `{{Provider 7 Domain}}` | Consent required | Joint controller (Art. 26) | US (SCCs + DPF where applicable) |
| 8 | `{{Cookie Name 8}}` | `{{Provider 8}}` | Third | Analytics | Crash and error telemetry | 90 days | `{{Provider 8 Domain}}` | Consent required | Processor (Art. 28) | EEA |

**Annex A last updated:** {{Annex A Last Updated}}

For every entry classified as **Joint controller**, see the joint-controller arrangement linked in the cookie settings centre. For every entry classified as **Independent controller**, see the third party's own privacy notice.

---

## Annex B — Consent banner UX requirements (EDPB-aligned)

This annex sets out the UX requirements our consent banner must meet. We restate them here so that auditors, supervisory authorities, and our own engineers have a single specification to point at.

### B.1 First-layer requirements

- "Accept all", "Reject all", and a "Manage preferences" entry-point are all visible on the **first layer** without scrolling.
- All three controls have **equal visual prominence**: same colour treatment, same size, same position, same affordance.
- No control is the default-focused state in a way that biases keyboard-only users towards acceptance.
- No category is enabled by default for non-essential cookies; "Reject all" is the operative default if the user closes the banner without choosing.
- The banner does not set non-essential cookies before the user makes a choice; only the consent-state cookie itself loads.

### B.2 No dark patterns

- No pre-ticked checkboxes for any non-essential category.
- No "confirmshaming" copy ("are you sure you want a worse experience?").
- No layout, contrast, or motion treatment that nudges towards acceptance.
- No reject controls hidden under "more options", "settings", or other indirection beyond the first layer.
- No double-negative copy ("uncheck the boxes you do not want to opt out of").
- No infinite-loop or perpetually-reappearing modals after a refusal.

### B.3 Granularity

- Per-category toggles are mandatory.
- Per-vendor toggles are required where feasible, and at minimum for advertising and social-media categories.
- The granular layer is reachable from the first layer in **one click**.

### B.4 Persistent access

- A **footer link** to the cookie settings centre is present on every page of `{{Website Domain}}`.
- The footer link is reachable by keyboard, by screen reader, and on mobile viewports.
- Clicking the footer link re-opens the same controls used during the initial consent, including the "Reject all" control.

### B.5 Consent record retention

- Each consent event is logged with: pseudonymous user reference, timestamp (UTC), banner version, vendor list shown, choices made, language / locale, mechanism (banner / settings centre / API).
- Records are retained for at least **12 months** after expiry or withdrawal.
- Records are retrievable on a per-user basis for **GDPR Article 15** access requests.

### B.6 Re-prompt cadence

- Default re-prompt at **12 months**.
- Earlier re-prompt on material category change, material vendor change, or regulator / court ruling.
- Re-prompts present the same "Accept all" / "Reject all" / "Manage preferences" parity as the initial banner.

### B.7 Cookie wall justification

- Cookie walls are off by default. Where a cookie wall is contemplated, it must:
  - Be backed by a documented compelling justification under **EDPB Guidelines 5/2020 §§ 39–41**.
  - Disclose the alternative path (paid access, alternative service, etc.).
  - Be reviewed and approved by the DPO (where appointed) before deployment.

### B.8 Germany (DSK) — additional requirements

- The first-layer trio "Accept all" / "Reject all" / "Manage preferences" must all be of **equal prominence** to one another (not just Accept vs. Reject).
- German-language copy is available and labelled.
- Impressum and Datenschutzerklärung links are reachable from the banner.

---

## Appendix — Merge fields used

The following Mustache merge fields appear in this policy and must be populated before publication.

| Field | Description | Example |
| --- | --- | --- |
| `{{Effective Date}}` | The effective date of this policy | 2026-04-28 |
| `{{Company Legal Name}}` | Full legal name of the controller | Example Holdings Ltd. |
| `{{Company Trading Name}}` | Trading / brand name | Example |
| `{{Member State Of Establishment}}` | EU/EEA Member State of main establishment | Ireland |
| `{{Supervisory Authority}}` | Lead supervisory authority under Art. 56 GDPR | Data Protection Commission (Ireland) |
| `{{Website Domain}}` | The domain this policy governs | example.com |
| `{{Service Name}}` | The user-facing name of the service | Example |
| `{{Privacy Policy URL}}` | URL of the companion privacy policy | https://example.com/privacy |
| `{{DPA URL}}` | URL of the companion Data Processing Addendum | https://example.com/dpa |
| `{{Cookie Settings URL}}` | URL of the cookie settings centre | https://example.com/cookies |
| `{{Consent Management Platform}}` | Vendor name of the deployed CMP | (vendor name) |
| `{{Company Email Privacy}}` | Privacy enquiries inbox | privacy@example.com |
| `{{Company Email DPO}}` | DPO inbox (if appointed) | dpo@example.com |
| `{{Company Postal Address}}` | Postal address of the controller | (street, city, postcode, country) |
| `{{EU Representative}}` | Article 27 representative (if controller is outside EEA) | (name and address) |
| `{{Cookie Name N}}` / `{{Provider N}}` / `{{Provider N Domain}}` | Annex A row fields | (per row) |
| `{{Annex A Last Updated}}` | Last update date of Annex A | 2026-04-28 |

---

## Appendix — Authoritative references

The following primary materials are the authoritative basis for this policy. Citations to secondary materials (commentary, treatises) are out of scope here.

**EU primary law and regulations**

- **ePrivacy Directive 2002/58/EC**, as amended by Directive 2009/136/EC, especially Article 5(3). EUR-Lex: `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32002L0058`
- **General Data Protection Regulation (GDPR), Regulation (EU) 2016/679**, especially Articles 4(11), 6(1)(a), 7, 8, 13, 14, 26, 28, 30, 37, 45–49, 56, 60, 77. EUR-Lex: `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679`
- **Digital Services Act, Regulation (EU) 2022/2065**, for the German renaming context. EUR-Lex: `https://eur-lex.europa.eu/eli/reg/2022/2065/oj`

**EDPB guidelines and reports**

- **EDPB Guidelines 5/2020 on consent under Regulation 2016/679**.
- **EDPB Guidelines 3/2022 on deceptive design patterns in social media platform interfaces** (read across to consent design).
- **EDPB Guidelines 2/2023 on Technical Scope of Art. 5(3) of ePrivacy Directive** `[VERIFY EDPB Guidelines 2/2023]`.
- **EDPB Cookie Banner Taskforce Report (January 2023)**.
- **EDPB Recommendations 01/2020 on supplementary measures** (Schrems II transfer impact assessments).

**CJEU case law**

- **Wirtschaftsakademie Schleswig-Holstein, C-210/16** (joint controllership for Facebook fan pages).
- **Fashion ID, C-40/17** (joint controllership for Facebook "Like" button).
- **Planet49, C-673/17** (no consent from pre-ticked boxes).
- **Schrems II, C-311/18** (international transfers and supplementary measures).

**German materials** (gesetze-im-internet.de, bundestag.de, BfDI, DSK)

- **Telekommunikation-Telemedien-Datenschutz-Gesetz (TTDSG)** / **Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz (TDDDG)**, especially § 25. `https://www.gesetze-im-internet.de/`
- **Bundesdatenschutzgesetz (BDSG)**.
- **Telemediengesetz (TMG)** / **Digitale-Dienste-Gesetz (DDG)**.
- **Telekommunikationsgesetz (TKG)**.
- **DSK Orientierungshilfe der Aufsichtsbehörden für Anbieter von Telemedien** (most recent edition).
- **BGH I ZR 7/16, judgment of 28 May 2020 (Cookie-Einwilligung II)**.
- **BVerwG** decisions on pre-ticked consent in the IFG context `[VERIFY specific BVerwG citations]`.

---

## Not legal advice

This document is a template and an information resource. It is **not legal advice** and does not create a lawyer-client relationship between you and `{{Company Legal Name}}` or any of its affiliates, contractors, or contributors. European data-protection law evolves rapidly through EDPB guidelines, national supervisory-authority decisions, and Court of Justice rulings, and Member-State implementations diverge. Before publishing a cookie policy based on this template, have the final text reviewed by a qualified data-protection lawyer admitted in your relevant jurisdiction, and have the underlying cookie inventory and banner implementation audited against current EDPB and national supervisory-authority guidance.

If you find an error or an out-of-date citation in this template, please report it to {{Company Email Privacy}} so we can correct it for the next revision.
