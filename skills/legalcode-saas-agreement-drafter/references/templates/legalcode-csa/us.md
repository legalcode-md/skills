---
title: Cloud Service Agreement — United States (Delaware default + CCPA + multi-state)
jurisdictions: [us, us-ca, us-de, us-ny, us-co, us-ct, us-tx, us-or]
statutes: [CCPA, CPRA, CPA, VCDPA, CTDPA, TDPSA, OCPA, DTSA, ROSCA, FTC-Click-to-Cancel, EAR, ITAR, OFAC, FCPA]
audience: [B2B]
license: MIT
last_updated: 2026-04-28
---

# Cloud Service Agreement — United States Variant

This Cloud Service Agreement (the "**CSA**") is entered into between `{{Vendor Legal Name}}`, a `{{Vendor State Of Formation}}` `{{Vendor Entity Type}}` with its principal place of business at `{{Vendor Address}}` ("**Vendor**"), and `{{Customer Legal Name}}`, a `{{Customer State Of Formation}}` `{{Customer Entity Type}}` with its principal place of business at `{{Customer Address}}` ("**Customer**"), as of `{{Effective Date}}`. Vendor and Customer are each a "**Party**".

---

## 1. Plain-language summary

In one paragraph: this is a B2B contract for a hosted cloud product. Customer pays subscription fees on an Order Form, Vendor delivers the Service over the public internet, each Party keeps the data and IP it brings, and disputes default to Delaware law unless the Order Form says otherwise. The remainder describes renewal, security, privacy, AI, exports, indemnities, and liability caps. If the summary conflicts with any later section, the later section controls.

---

## 2. Agreement structure (Master Agreement + Order Forms)

In one sentence: the CSA is the master frame; each Order Form adds commercial detail for a specific deployment.

2.1. **Components.** The "**Agreement**" = (a) this CSA; (b) executed Order Forms; (c) the Exhibits; (d) the DPA (Exhibit C); and (e) the AUP (Exhibit D).

2.2. **Precedence.** Where components conflict: Order Form (only as to terms it expressly modifies) → DPA → CSA → Exhibits → AUP. Click-through or shrink-wrap terms inside the Service do not modify the Agreement.

2.3. **Order Form formation.** An Order Form is binding when signed by both Parties (handwritten, e-signature, or counterpart PDFs). Pre-printed Customer purchase-order terms are rejected.

2.4. **Affiliates.** An entity controlled by, controlling, or under common control with Customer (an "**Affiliate**") may sign its own Order Form. Customer is not liable for an Affiliate's separate Order Form unless Customer signs as guarantor.

2.5. **Amendments.** Modifications require a writing signed by both Parties, except Vendor may update the AUP and operational security documentation on notice, provided the update does not materially decrease security or expand Customer's obligations.

---

## 3. Definitions

In one sentence: this section gives the controlling meaning of capitalised terms, importing CCPA-specific terms from Cal. Civ. Code §1798.140 and the DTSA Trade Secret definition from 18 U.S.C. §1839(3).

3.1. "**AUP**" — the policy in Exhibit D. "**Affiliate**" — defined in §2.4. "**Documentation**" — the user/admin documentation Vendor publishes. "**Subprocessor**" — a third party engaged by Vendor to process Customer Data on Vendor's behalf.

3.2. "**Aggregated Data**" — data derived from Customer Data that has been deidentified, combined with data from other sources, and rendered such that it does not identify and cannot reasonably be linked to Customer or any individual.

3.3. "**Authorised User**" — an employee, contractor, or agent of Customer (or a permitted Affiliate) granted credentials to the Service.

3.4. "**Business**" — meaning in Cal. Civ. Code §1798.140(d). Customer is the Business where it determines purposes and means of processing PI through the Service.

3.5. "**Confidential Information**" — defined in §7.

3.6. "**Contractor**" — meaning in Cal. Civ. Code §1798.140(j). Vendor accepts the Contractor role where so designated on the Order Form and the conditions of §1798.140(j)(1) are met.

3.7. "**Cross-Context Behavioral Advertising**" — meaning in Cal. Civ. Code §1798.140(k). Vendor does not engage in it on Customer Data.

3.8. "**Customer Data**" — electronic data and content submitted to or generated through Customer's account, including PI processed on Customer's behalf, excluding Service Generated Data and Aggregated Data.

3.9. "**DTSA**" — the federal Defend Trade Secrets Act, 18 U.S.C. §§1836 et seq.

3.10. "**Order Form**" — a document referencing this CSA stating Service tier, fees, term, and other commercial terms.

3.11. "**Personal Information**" or "**PI**" — meaning in Cal. Civ. Code §1798.140(v) and the equivalent term in any other applicable State Privacy Law.

3.12. "**Sale**" / "**Sharing**" — meanings in Cal. Civ. Code §1798.140(ad) / (ah). Vendor does not Sell or Share Customer Data.

3.13. "**Sensitive Personal Information**" — meaning in Cal. Civ. Code §1798.140(ae) (precise geolocation, government IDs, financial credentials, genetic and biometric identifiers, content of non-public communications).

3.14. "**Service**" — the cloud product identified on the Order Form, including Documentation, SDKs, and CLIs delivered with the subscription.

3.15. "**Service Generated Data**" — telemetry, audit logs, error reports, performance metrics, and security signals produced by the Service.

3.16. "**Service Provider**" — meaning in Cal. Civ. Code §1798.140(ag). Vendor accepts this role for Customer Data, subject to §6.

3.17. "**State Privacy Law**" — CCPA/CPRA, the Colorado Privacy Act ("CPA"), the Virginia CDPA ("VCDPA"), the Connecticut Data Privacy Act ("CTDPA"), the Texas Data Privacy and Security Act ("TDPSA"), the Oregon Consumer Privacy Act ("OCPA"), and any other comprehensive consumer-privacy statute applicable to processing under this CSA.

3.18. "**Trade Secret**" — meaning in 18 U.S.C. §1839(3): financial, business, scientific, technical, economic, or engineering information that the owner has taken reasonable measures to keep secret and that derives independent economic value from not being generally known.

3.19. "**Vendor IP**" — the Service, underlying software, ML models, infrastructure, brand assets, Documentation, Aggregated Data, Service Generated Data, and any improvement, fix, or feedback-derived enhancement, with all Intellectual Property Rights in any of them.

3.20. "**`{{Service Provider Designation}}`**" — Vendor's CCPA role per the Order Form (Service Provider, Contractor, or Third Party).

---

## 4. Use of the Service

In one sentence: Vendor grants Customer a non-exclusive right to use the Service for internal business operations during the subscription term.

4.1. **Grant.** Subject to the Agreement and payment of fees, Vendor grants Customer a non-exclusive, non-transferable (except as §18.5 permits), non-sublicensable, worldwide right during the subscription term to access and use the Service for internal business purposes, and to permit Authorised Users to do the same.

4.2. **Affiliate use.** Customer may permit Affiliates and their Authorised Users to use the Service under Customer's account. Customer remains responsible for each Affiliate's compliance.

4.3. **Customer-Favorable variant.** *OPTIONAL — only if Customer is a regulated financial institution or federal contractor.* Rights granted include access by Customer's regulators, contracting agency, or external auditors for audit and supervisory review on reasonable notice and under appropriate confidentiality.

4.4. **Vendor-Favorable variant.** *OPTIONAL — only if usage is metered.* Use is bounded by the metric on the Order Form. Vendor will give 80% and 100% notices and will not throttle for the first 14 days after the 100% notice.

4.5. **Documentation.** Customer may copy and distribute Documentation internally as reasonably required.

4.6. **Reservation.** All rights not expressly granted are reserved.

---

## 5. Customer responsibilities & restrictions

In one sentence: Customer is responsible for its Authorised Users, must protect credentials, and must comply with US export, sanctions, and anti-bribery laws when using the Service.

5.1. **Credentials.** Customer must keep credentials confidential and is responsible for activity under its account, except activity caused by Vendor's breach of §11.

5.2. **Acceptable use.** Customer will follow the AUP and will not (a) reverse-engineer the Service except where contractual prohibitions are unenforceable; (b) resell, sublicense, or operate the Service as a service bureau for unaffiliated third parties; (c) build a directly competing product; (d) circumvent rate limits or security controls; or (e) submit content that infringes third-party rights or violates law.

5.3. **Export controls.** Customer is responsible for compliance with the US Export Administration Regulations (EAR, 15 C.F.R. parts 730–774); the International Traffic in Arms Regulations (ITAR, 22 C.F.R. parts 120–130); and OFAC sanctions. Customer represents that (i) Customer is not located in, organised under the laws of, or ordinarily resident in a country or region subject to a comprehensive US embargo (as of the Effective Date: Cuba, Iran, North Korea, Syria, and the Crimea, Donetsk, and Luhansk regions of Ukraine); (ii) Customer is not on the SDN, NS-PLC, SSI, or Foreign Sanctions Evaders list; and (iii) Customer will not export, re-export, or transfer the Service or its outputs in violation of EAR, ITAR, or OFAC.

5.4. **ITAR data.** Customer will not submit ITAR-controlled technical data to the Service unless an Order Form expressly authorises ITAR processing and Vendor confirms the environment is so configured. Submission outside an authorised environment is a material breach.

5.5. **Anti-bribery.** Customer will comply with the FCPA (15 U.S.C. §§78dd-1, 78dd-2, 78dd-3, 78ff), the UK Bribery Act 2010, and other applicable anti-bribery laws. Neither Party will offer, promise, give, or accept anything of value in connection with the Agreement other than reasonable, lawful business courtesies.

5.6. **AML / sanctions screening.** *OPTIONAL — only if Customer is a regulated financial institution.* Customer warrants it has implemented an AML / sanctions-screening programme reasonably designed to comply with the Bank Secrecy Act and OFAC.

5.7. **Lawful content.** Customer warrants it has the right to submit Customer Data and that submission will not violate third-party rights or law.

---

## 6. Customer Data

In one sentence: Customer owns Customer Data and Vendor processes it only as a CCPA Service Provider/Contractor on Customer's documented instructions, with no Sale, no Sharing, and no Cross-Context Behavioral Advertising.

6.1. **Ownership.** As between the Parties, Customer owns Customer Data. Vendor receives no rights in Customer Data except the licence in §6.2.

6.2. **Limited licence.** Customer grants Vendor a non-exclusive, worldwide, royalty-free licence to host, transmit, copy, display, modify (only as technically required), and process Customer Data solely to (a) provide and support the Service; (b) prevent or address security or technical issues; (c) comply with law; and (d) produce Aggregated Data and Service Generated Data consistent with §3 and §15.

6.3. **CCPA Service Provider commitments.** Vendor is a Service Provider, and a Contractor where the Order Form so states, for Customer Data that is PI under CCPA/CPRA, and commits to the restrictions of Cal. Civ. Code §1798.140(ag)(1)(A)–(D):

- **(A) Purpose limitation.** Use only for the business purposes specified in the Agreement (Service delivery and the support, security, billing, and improvement activities in §§6.2 and 15); no "commercial purpose" within §1798.140(f) outside those business purposes.
- **(B) No Sale; no Sharing.** No Sale of Customer Data; no Sharing for Cross-Context Behavioral Advertising.
- **(C) No retention, use, or disclosure outside the direct business relationship** between Vendor and Customer.
- **(D) No combining** with PI received from or on behalf of another person, except as permitted by Cal. Civ. Code §1798.145(a)(1)–(7).

6.4. **Multi-state addenda.** §19 (Multi-State Service Provider Addenda) is incorporated into this §6 by reference. Where a State Privacy Law imposes a stricter or additional processor obligation than CCPA, Vendor will comply with that stricter obligation for processing within scope.

6.5. **Subprocessors.** Vendor maintains a Subprocessor list at `{{Subprocessor List URL}}`. Vendor will (a) impose written terms on each Subprocessor at least as protective as §6.3 and the DPA; (b) remain liable for Subprocessor acts and omissions affecting Customer Data; and (c) provide ≥30 days' notice of a new Subprocessor with a reasonable objection mechanism. If Vendor cannot resolve a reasonable objection, Customer may terminate the affected Order Form for cause and receive a pro-rata refund of prepaid unused fees.

6.6. **Customer instructions.** "Documented instructions" are (a) the Agreement; (b) configurations Customer makes; and (c) written instructions to Vendor's privacy contact. Vendor will inform Customer if it believes an instruction violates a State Privacy Law.

6.7. **Data subject requests.** Vendor will assist with verifiable consumer requests under State Privacy Laws (right to know, delete, correct, opt out of Sale/Sharing, limit use of Sensitive PI, portability), to the extent technically feasible. The DPA describes the mechanism and SLA.

6.8. **Sensitive PI.** Customer remains responsible for any consent required and for honouring the right to limit use or disclosure of Sensitive PI. Vendor will not use Sensitive PI to infer consumer characteristics beyond Service delivery.

6.9. **Deletion at termination.** Vendor will delete or, at Customer's election, return Customer Data within 30 days of termination, except where law requires retention. Backup copies that cannot be selectively deleted are overwritten on Vendor's standard rotation (≤90 days) and remain subject to §6.3 until destroyed.

6.10. **Dual-perspective variants.**

- *Customer-Favorable.* No use of Customer Data to train, retrain, fine-tune, or improve any ML model offered to or used for any other customer or Vendor's general benefit, except security/abuse-detection models on metadata.
- *Vendor-Favorable.* Vendor may use Service Generated Data and Aggregated Data for any lawful purpose, including improving the Service, security analytics, benchmarking, and product research.
- *Market-standard.* Vendor may use Customer Data only to deliver and improve the Service for Customer; Aggregated Data for any lawful purpose; no training of general foundation models on Customer content unless Customer opts in on the Order Form.

---

## 7. Confidentiality

In one sentence: each Party keeps the other's non-public information confidential, with carve-outs for information that is public, independently developed, or compelled by law.

7.1. **Definition.** "**Confidential Information**" is non-public information disclosed by one Party (the "Discloser") to the other (the "Recipient") that is marked confidential or a reasonable person would understand to be confidential. Customer Data is Customer's. Vendor IP, Service architecture, security documentation, and pricing are Vendor's. Order Form terms are mutual.

7.2. **Obligations.** Recipient will (a) use Confidential Information only to perform the Agreement; (b) protect it with at least the care it uses for its own information of similar sensitivity, and not less than reasonable care; and (c) limit access to personnel, advisors, and contractors with a need to know who are bound by at least equivalent confidentiality.

7.3. **Exclusions.** §7.2 does not apply to information that (a) becomes public through no fault of Recipient; (b) was known without restriction before disclosure; (c) is independently developed without use of Confidential Information; or (d) is rightfully obtained from a third party without restriction.

7.4. **Compelled disclosure.** Recipient may disclose to the extent compelled by law, with prompt notice to Discloser unless prohibited, reasonable cooperation on protective orders, and disclosure of only the minimum required.

7.5. **Trade Secrets.** Confidential Information may include Trade Secrets under 18 U.S.C. §1839(3). Nothing in §7 limits remedies under DTSA, including exemplary damages and attorneys' fees under 18 U.S.C. §1836(b)(3)(C). Per 18 U.S.C. §1833(b), no individual is liable under federal or state Trade Secret law for disclosing a Trade Secret in confidence to a government official solely to report a suspected violation, or in a complaint filed under seal.

7.6. **California §16600 carve-out.** This §7 is a confidentiality obligation, not a non-compete. Nothing here prohibits a Party's personnel from accepting employment or consulting work with a competitor in California, in compliance with Cal. Bus. & Prof. Code §16600. The clause must not be construed as a de facto non-compete.

7.7. **FTC Non-Compete Rule.** *`[VERIFY enforceability]`* — to the extent the FTC's final Non-Compete Rule (16 C.F.R. Part 910) is in force at the time of dispute, this §7 is construed consistently with it, and any portion that would constitute a "non-compete clause" is severed to the extent required.

7.8. **Survival.** §7 survives for five years post-termination, except Trade Secret protection continues so long as the information qualifies under DTSA.

---

## 8. Fees, billing, taxes

In one sentence: Customer pays the Order Form fees, taxes are added on top, and renewals are governed by ROSCA and the state auto-renewal statutes summarised below.

8.1. **Fees.** Customer pays Order Form fees in US dollars within 30 days of an undisputed invoice. Late amounts accrue interest at the lower of 1.0%/month and the maximum rate permitted by law.

8.2. **Disputes.** Customer must dispute an invoice in good faith within 30 days, in writing. Undisputed amounts remain due; the Parties cooperate to resolve disputes within 30 days.

8.3. **Taxes.** Fees are tax-exclusive. Customer pays sales, use, VAT, gross-receipts, and similar transactional taxes, except those on Vendor's net income, payroll, or property. Customer remits required withholding and provides Vendor a receipt.

8.4. **Expenses.** Professional services fees and expenses are stated on the Order Form or SOW.

8.5. **Price changes.** Vendor may adjust list prices at renewal with ≥60 days' notice, capped at the lower of (a) Vendor's published list for the same tier and (b) the prior-term price plus the greater of 7% and the BLS CPI-U change over the prior 12 months. *Customer-Favorable: cap at prior + 5%. Vendor-Favorable: replace cap with "Vendor's reasonable discretion".*

8.6. **California ARLDA.** For Order Forms with initial term ≥1 year and automatic renewal, Vendor will provide the disclosures and reminders required by Cal. Bus. & Prof. Code §17600 et seq., including (a) clear and conspicuous disclosure of auto-renewal terms before acceptance, (b) a pre-renewal reminder sent 15–45 days before the renewal date stating the date and next-term cost, and (c) an online cancellation mechanism that does not require speaking with a representative.

8.7. **New York GBL §527-a.** For New York-billing Customers, Vendor will present auto-renewal terms clearly and conspicuously before acceptance, provide a written acknowledgement, and honour cancellation rights as N.Y. Gen. Bus. Law §527-a requires.

8.8. **Oregon HB 2479 (ORS 646A.293).** For Oregon Customers, Vendor will give the disclosures and cancellation mechanism required, including a pre-renewal notice ≥30 days before each annual-or-longer auto-renewal.

8.9. **Colorado HB 21-1063.** For Colorado Customers, Vendor provides the required disclosures and cancellation mechanism, including online cancellation parity with online sign-up.

8.10. **Illinois ARLDA (815 ILCS 601/).** For Illinois Customers with a term ≥12 months and automatic renewal, Vendor will provide written notice 30–60 days before the renewal date.

8.11. **ROSCA (15 U.S.C. §§8401–8405).** As a federal floor, Vendor (a) discloses material terms clearly and conspicuously before billing, (b) obtains express informed consent to be charged, and (c) provides a simple stop-recurring mechanism.

8.12. **FTC Click-to-Cancel (16 C.F.R. Part 425).** *`[VERIFY commencement]`* — to the extent in force, Vendor will (a) provide cancellation at least as easy as sign-up; (b) obtain express informed consent to any negative-option feature before charging; and (c) honour cancellation requests promptly.

8.13. **State-by-state matrix.** For billing addresses outside §§8.6–8.10, Vendor follows the corresponding state auto-renewal statute (if any) per the matrix maintained in the companion `legalcode-tos` Annex C ("US Auto-Renewal Matrix").

8.14. **Dual-perspective variants.**

- *Customer-Favorable.* No mid-term increases; renewal cap = CPI-U for the prior 12 months.
- *Vendor-Favorable.* Vendor may pass through Subprocessor cost increases mid-term on 30 days' notice, capped at 10% of the affected line item.
- *Market-standard.* Renewal cap per §8.5; no mid-term increases other than for additional usage.

---

## 9. Term, renewal, termination & suspension

In one sentence: each Order Form has its own term and renewal cadence, and either Party can terminate for material uncured breach or insolvency.

9.1. **CSA term.** Effective until the last Order Form has expired or been terminated.

9.2. **Order Form term.** As stated on the Order Form; default 12 months.

9.3. **Auto-renewal.** Unless marked "non-renewing", Order Forms auto-renew for successive periods equal to the initial term, on §8.5 price terms and subject to §§8.6–8.13. Either Party may opt out with ≥30 days' notice before the end of the then-current term. Vendor will provide pre-renewal reminders required by applicable state law as a matter of policy.

9.4. **Termination for material breach.** Either Party may terminate on 30 days' notice for material breach not cured during the notice period. Customer's failure to pay an undisputed invoice within 15 days of a written reminder is a material breach.

9.5. **Termination for insolvency.** Either Party may terminate immediately on written notice on the other's bankruptcy petition not dismissed within 60 days, assignment for the benefit of creditors, receivership over a material portion of assets, or cessation of business in the ordinary course.

9.6. **Termination for convenience by Customer.** *OPTIONAL — Customer-Favorable.* Customer may terminate any Order Form on 60 days' notice with a pro-rata refund of prepaid unused fees.

9.7. **Suspension.** Vendor may suspend the Service or part of it on reasonable notice (or with prompt subsequent notice if not feasible) where (a) Customer's use poses an imminent security or legal risk; (b) Customer is materially breaching §5; or (c) payment is more than 30 days overdue and undisputed and Vendor has given ≥10 days' notice. Suspension is limited to the affected functionality where technically feasible.

9.8. **Effects.** On termination: (a) access ends; (b) refunds under §9.4 or §9.6 issue; (c) §6.9 governs Customer Data return/deletion; (d) §§3, 6.9, 7, 8 (accrued), 14, 15.4, 16, 17, 18 survive.

9.9. **Dual-perspective variants.**

- *Customer-Favorable.* Add §9.6; refund of prepaid unused fees on Vendor's material breach.
- *Vendor-Favorable.* Remove §9.6; any unpaid invoice (disputed or not) overdue 30 days is a material breach.
- *Market-standard.* §§9.4–9.5; no convenience termination by either Party.

---

## 10. Service Level Agreement

In one sentence: Vendor commits to a monthly uptime target and Customer's exclusive remedy for missing it is the service credit in Exhibit B.

10.1. **Uptime commitment.** Monthly Uptime Percentage ≥99.9% (or higher, as the Order Form states), measured per Exhibit B.

10.2. **Service credits.** If Vendor misses the target, Customer is entitled to a credit per Exhibit B. Credits are the sole and exclusive remedy, except where the failure also constitutes a material breach under §9.4.

10.3. **Excluded events.** Unavailability caused by (a) maintenance announced ≥72 hours in advance; (b) emergency security maintenance; (c) force majeure under §18.4; (d) Customer's actions, integrations, or systems; or (e) trial/Beta features is excluded.

10.4. **Reporting.** Vendor publishes monthly availability metrics on the status page named on the Order Form. Credit claims must be made within 30 days of the affected month.

10.5. **Customer-Favorable variant.** *OPTIONAL — enterprise tiers.* Tiered credit schedule, chronic-failure termination on three SLA misses in any rolling six months, annual SLA review.

---

## 11. Security & data protection

In one sentence: Vendor maintains a written information-security programme, holds an annual SOC 2 Type II report, and notifies Customer of Security Incidents per the strictest applicable state breach-notification law.

11.1. **Programme.** Vendor maintains a written information-security programme proportionate to the Service and Customer Data sensitivity, covering administrative, technical, and physical safeguards (access control, network security, encryption, vulnerability management, incident response, BC/DR, personnel security).

11.2. **Encryption.** TLS 1.2+ in transit; AES-256 (or equivalent) at rest.

11.3. **Access control.** Need-to-know, MFA for administrative access, quarterly access review.

11.4. **Personnel.** Background checks where lawful; security and privacy training at hire and annually.

11.5. **Subprocessors.** Per §6.5.

11.6. **Audit.** On ≥30 days' notice, not more than once per 12 months (and after a Security Incident), Customer may request the latest SOC 2 Type II report and a §11 attestation. No physical audits except where Customer's regulator requires and on terms protecting Vendor's other customers.

11.7. **DPA.** Exhibit C is incorporated into §11 and supplements (without limiting) the operational commitments here.

11.8. **California cybersecurity audit.** *`[VERIFY commencement]`* — to the extent the CPPA Cybersecurity Audit Regulations (Cal. Code Regs. tit. 11 §§7120–7129) apply, Vendor will (a) conduct or commission the annual audit on the regulatory schedule, (b) provide a summary on request, and (c) reasonably cooperate with Customer's own audit obligations.

11.9. **State breach notification.** On confirmation of a Security Incident affecting Customer Data, Vendor notifies Customer in writing without undue delay, and in any event within the lesser of 72 hours and the strictest applicable state statutory window (including Cal. Civ. Code §1798.82 and the equivalents in the other 49 states and DC). Notice will include the information the statute requires and reasonable detail on scope, root cause, and remediation. "**Security Incident**" is a confirmed unauthorised access, acquisition, disclosure, or loss; routine unsuccessful attempts are excluded.

11.10. **Standards and overlays.** Vendor maintains an annual SOC 2 Type II and ISO/IEC 27001 (or active certification roadmap). Where the Order Form so states, Vendor maintains controls aligned to (a) NYDFS Cybersecurity Regulation (23 NYCRR Part 500); (b) Texas Cybersecurity Risk Management Standard SB 820 (where Customer is a Texas state agency or contractor); and (c) Massachusetts 201 CMR 17.00 (where Customer Data includes Massachusetts-resident PI).

11.11. **HIPAA.** Vendor is not a HIPAA business associate by default. If Customer's use involves PHI under 45 C.F.R. §160.103, the Parties must execute a HIPAA Business Associate Agreement before submission; the BAA is referenced on the Order Form.

11.12. **Financial-services oversight.** *OPTIONAL — only if Customer is a regulated financial institution.* Where Customer is supervised by the Federal Reserve, OCC, CFPB, or a state banking regulator, Vendor cooperates with examination requests directed through Customer (Interagency Guidance on Third-Party Relationships, June 2023), under confidentiality and a mutually-agreed timeline.

11.13. **GLBA.** *OPTIONAL — only if Customer is a "financial institution" under 15 U.S.C. §6801 et seq.* Vendor treats NPI received per the GLBA Safeguards Rule (16 C.F.R. Part 314) and limits use to the purposes in the Agreement.

11.14. **Dual-perspective variants.**

- *Customer-Favorable.* 24-hour breach notice; one-time on-site audit per 24-month period; annual pen-test executive summary.
- *Vendor-Favorable.* "Without undue delay" notice; SOC 2 + questionnaires only, no on-site audit.
- *Market-standard.* §11 as drafted, with the 72-hour-or-shorter-statutory-window notice.

---

## 12. Trials & beta features

In one sentence: trials and Beta features are "AS IS" with no SLA or performance warranty and Vendor may discontinue them.

12.1. **Trials.** Free for the Order Form period; converts to paid (if so stated) or terminates automatically.

12.2. **Beta features.** Pre-release features marked "Beta" are "AS IS" without warranty, support, or SLA. Vendor may discontinue, promote to GA, or retire them at any time.

12.3. **No warranty.** §16 does not apply to trial or Beta usage. Vendor's aggregate liability for trial and Beta usage is capped at US $100, except for liability that cannot be limited under applicable law.

12.4. **Customer responsibility.** Customer should not place mission-critical workloads or regulated data into trial or Beta deployments without Vendor's written confirmation of fitness for that use.

---

## 13. Third-party services & integrations

In one sentence: Customer's use of third-party connectors is governed by the third party's own terms, and Vendor is not responsible for the third party.

13.1. **Third-party services.** The Service may interoperate with third-party services (email, SSO, payment, analytics, AI models). Customer's use is subject to the third party's terms and privacy policy, not this CSA. Vendor is not responsible for the third party's acts, omissions, fees, security, or availability.

13.2. **Authorisation.** Enabling an integration authorises Vendor to exchange Customer Data with the third party as needed for the integration to function.

13.3. **Discontinuation.** Vendor uses commercially reasonable efforts to notify Customer of a material third-party change and to offer a workaround, but is not liable for the third party's discontinuation.

13.4. **Open source.** Open-source components are listed in the Documentation. Nothing in the Agreement limits Customer's rights under an open-source licence as to that licence's components.

---

## 14. Intellectual property

In one sentence: Vendor owns the Service and Vendor IP, Customer owns Customer Data, and Vendor may use Feedback freely.

14.1. **Vendor IP.** Vendor and its licensors retain all rights in Vendor IP. No rights are granted to Customer except as expressly stated in §4.

14.2. **Customer IP.** Customer retains all rights in Customer Data and any Customer-provided trademarks. The §6.2 licence is Vendor's only right in Customer Data.

14.3. **Feedback.** If Customer voluntarily provides suggestions or feedback ("Feedback"), Customer grants Vendor a perpetual, irrevocable, worldwide, royalty-free, sublicensable licence to use Feedback for any purpose. Feedback is non-confidential and not required.

14.4. **Aggregated and Service Generated Data.** Subject to §6.3, Vendor may use these for any lawful purpose, including improving the Service, security analytics, benchmarking, and product research.

14.5. **Trademarks and publicity.** Neither Party may use the other's name, marks, or logos without prior written consent, except that Vendor may identify Customer in tasteful, non-endorsing customer lists and marketing. Customer may revoke this permission on written notice.

14.6. **California §16600.** This §14 does not restrict personnel mobility in California; it preserves confidentiality under §7.

14.7. **FTC Non-Compete Rule.** *`[VERIFY enforceability]`* — to the extent 16 C.F.R. Part 910 is in force, this §14 is construed consistently and any "non-compete clause" portion is severed.

14.8. **"Intellectual Property Rights"** means patents, copyrights (including waivable moral rights), Trade Secrets, trademarks, service marks, trade dress, database rights, and similar proprietary rights, registered or unregistered, anywhere in the world.

---

## 15. AI & machine learning

In one sentence: Vendor will not train general models on Customer Data unless Customer opts in, will provide reasonable model documentation, and will comply with applicable US AI laws as they take effect.

15.1. **Training restriction (default).** Default = no training. Vendor will not use Customer Data to train, retrain, or fine-tune any ML model offered to or used for any other customer or for Vendor's general benefit unless Customer opts in on the Order Form. Vendor may use Customer Data to (a) train, evaluate, or fine-tune a model dedicated to Customer's instance and not offered to any other customer; (b) operate diagnostic and QA models on metadata; and (c) operate abuse-, fraud-, and security-detection models that classify content but do not retain Customer's content beyond the operational window in the Documentation.

15.2. **Model documentation.** On request, Vendor provides a model card (or equivalent) for each AI feature describing intended use, known limitations, evaluation methods, and high-level training-data characteristics.

15.3. **Output disclaimer.** AI features may produce inaccurate, biased, or unsuitable outputs. Customer is responsible for reviewing outputs before relying on them, especially for legal, medical, financial, employment, or safety decisions. Output is "AS IS" with respect to factual accuracy, subject to §16.

15.4. **Post-termination.** On Customer's written request, Vendor deletes fine-tunes and embeddings derived from Customer Data within 30 days of termination, except for security/abuse-detection models on metadata.

15.5. **No automated decisions about consumers.** Vendor will not use AI features to make decisions producing legal or similarly significant effects on consumers (within State Privacy Laws) without Customer's written authorisation; Customer remains the controller/Business.

15.6. **California ADMT.** *`[VERIFY adoption]`* — to the extent the CPPA Automated Decisionmaking Technology Regulations (Cal. Code Regs. tit. 11 §§7150–7158, 7200–7222) are adopted and in force, Vendor will (a) operate AI features consistently with their notice, opt-out, and assessment requirements, and (b) reasonably assist Customer's own ADMT obligations.

15.7. **Colorado AI Act (SB 24-205).** *`[VERIFY commencement]`* — to the extent in force and the AI feature is a "high-risk artificial intelligence system", Vendor will (a) provide developer-side disclosures, (b) reasonably cooperate with Customer's deployer-side disclosures and impact assessments, and (c) treat algorithmic discrimination as a material defect for §16.

15.8. **NYC Local Law 144.** *OPTIONAL — only if the Service is an "automated employment decision tool" (NYC Admin. Code §20-870 et seq.) used to screen NYC candidates.* Vendor will (a) make a current bias-audit summary available, (b) disclose AEDT data sources and types, and (c) reasonably cooperate with Customer's notice and recordkeeping obligations.

15.9. **California SB 942 (AI Transparency Act).** *`[VERIFY]`* — to the extent in force and applicable, Vendor will provide AI-detection tools or content-provenance signals as the statute requires and document its compliance approach.

15.10. **Dual-perspective variants.**

- *Customer-Favorable.* No training (incl. dedicated instances) without prior written consent; mandatory derivative deletion within 14 days; Subprocessor flow-down of model-card obligations.
- *Vendor-Favorable.* Vendor may use Customer Data and Service Generated Data to improve the Service, provided resulting models do not memorise Customer content; opt-out, not opt-in.
- *Market-standard.* §15.1 as drafted.

---

## 16. Warranties, disclaimers & limitations of liability

In one sentence: Vendor warrants the Service will materially conform to the Documentation and be free of malicious code, with all other warranties disclaimed and total liability capped except for the carve-outs US law does not permit to be capped.

16.1. **Performance warranty.** During the term, (a) the Service will materially conform to the Documentation and (b) Vendor will not knowingly introduce malicious code. Customer's exclusive remedy is, at Vendor's option, repair, replacement, or refund of fees pre-paid for the affected portion for the period of non-conformance.

16.2. **Mutual warranties.** Each Party warrants that it has corporate power to execute and perform, that performance does not violate its organisational documents or another agreement, and that the Agreement is enforceable against it.

16.3. **Disclaimer.** EXCEPT AS EXPRESSLY STATED IN §§16.1–16.2, AND TO THE FULLEST EXTENT PERMITTED BY LAW, THE SERVICE IS PROVIDED "AS IS" AND "AS AVAILABLE" AND VENDOR DISCLAIMS ALL OTHER WARRANTIES, EXPRESS OR IMPLIED, INCLUDING IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT, AND ANY ARISING FROM COURSE OF DEALING OR USAGE OF TRADE. VENDOR DOES NOT WARRANT THAT THE SERVICE WILL BE UNINTERRUPTED, ERROR-FREE, OR SECURE AGAINST ALL THREATS. THIS IS A "CONSPICUOUS" DISCLAIMER FOR UCC §2-316.

16.4. **Magnuson-Moss.** The Magnuson-Moss Warranty Act addresses consumer products and is generally not in scope for this B2B Agreement; to the extent it applies, §16.3 is construed consistently with it.

16.5. **Direct-damages cap.** EXCEPT AS PROVIDED IN §16.7, EACH PARTY'S AGGREGATE LIABILITY UNDER OR RELATED TO THE AGREEMENT IS LIMITED TO THE GREATER OF (A) FEES PAID OR PAYABLE UNDER THE AFFECTED ORDER FORM IN THE 12 MONTHS BEFORE THE FIRST EVENT GIVING RISE TO LIABILITY AND (B) `{{Liability Cap Floor}}` (a negotiated USD floor, typically USD 100,000–1,000,000). The cap applies in aggregate and is not multiplied by claims or claimants.

16.6. **Exclusion of consequential damages.** EXCEPT AS PROVIDED IN §16.7, NEITHER PARTY IS LIABLE FOR LOST PROFITS, LOST REVENUES, LOST DATA (BEYOND RESTORATION COSTS FROM CUSTOMER'S OWN BACKUPS), LOST GOODWILL, OR INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, OR PUNITIVE DAMAGES, EVEN IF ADVISED OF THE POSSIBILITY. THIS APPLIES REGARDLESS OF CAUSE OF ACTION.

16.7. **Carve-outs.** §§16.5–16.6 do not apply to (a) payment obligations; (b) §17 indemnities; (c) §7 breaches, except that for non-Trade-Secret, non-PI Confidentiality breaches, liability is capped at three times the §16.5 amount; (d) wilful misconduct or fraud; (e) Customer's breach of §5.3 (exports), §5.5 (FCPA), or §4 licence scope; (f) death or bodily injury caused by negligence; (g) DTSA exemplary damages and attorneys' fees under 18 U.S.C. §1836(b)(3)(C); and (h) any other liability that cannot be limited under applicable law.

16.8. **New Jersey TCCWNA carve-out.** For New Jersey-domiciled Customers, §16 will not be enforced in a manner violating the Truth-in-Consumer Contract, Warranty and Notice Act (N.J.S.A. §56:12-14 et seq.) to the extent it applies to Customer's use of the Service.

16.9. **Limitations period.** No action arising out of the Agreement (other than for non-payment) may be brought more than two years after the cause of action accrues, except where applicable law prohibits a shorter period than the statutory default.

16.10. **Dual-perspective variants.**

- *Customer-Favorable.* Cap = 2x prior 12 months' fees, with a super-cap of 3x the standard cap for Confidentiality and Security Incidents; carve-out for gross negligence in addition to wilful misconduct.
- *Vendor-Favorable.* Cap = lower of prior 12 months' fees and the Liability Cap Floor; consequential damages excluded, carve-outs limited to indemnities and payment.
- *Market-standard.* §16 as drafted.

---

## 17. Indemnification & insurance

In one sentence: Vendor defends Customer against IP-infringement claims arising from use of the Service, Customer defends Vendor against claims from Customer Data or misuse, and each Party maintains commercially reasonable insurance.

17.1. **Vendor defence.** Vendor will defend Customer (and its officers, directors, employees, and Affiliates) against any third-party claim alleging that Customer's use of the Service in accordance with the Agreement infringes a US patent, copyright, trademark, or Trade Secret (a "**Vendor IP Claim**") and will pay damages and reasonable attorneys' fees finally awarded (or agreed in a settlement Vendor approves in writing).

17.2. **Vendor mitigation.** If a Vendor IP Claim is made or threatened, Vendor may at its option (a) procure for Customer the right to continue using the Service; (b) modify or replace it to be non-infringing while substantially preserving functionality; or (c) if (a) and (b) are not commercially reasonable, terminate the affected Order Form and refund prepaid unused fees.

17.3. **Vendor exclusions.** §17.1 does not apply to claims arising out of (a) Customer Data; (b) modifications by anyone other than Vendor or its authorised personnel; (c) combinations with software, hardware, or data not provided or authorised by Vendor where the claim would not have arisen but for the combination; (d) continued use of an allegedly infringing version after Vendor has provided a non-infringing replacement; (e) trial or Beta features; or (f) use in violation of the Agreement.

17.4. **Customer defence.** Customer will defend Vendor (and its officers, directors, employees, and Affiliates) against third-party claims arising out of (a) Customer Data; (b) breach of §5; or (c) Customer's combination of the Service with other software, hardware, or data in violation of the Agreement, and will pay damages and reasonable attorneys' fees finally awarded (or agreed in a settlement Customer approves in writing).

17.5. **Procedure.** The indemnified Party will (a) give prompt written notice (the indemnifier is relieved only to the extent prejudiced); (b) give the indemnifier sole control of defence and settlement (a settlement that admits liability or imposes a non-monetary obligation requires the indemnified Party's prior written consent, not unreasonably withheld); and (c) reasonably cooperate at the indemnifier's expense.

17.6. **Insurance.** During the term and for two years after, Vendor maintains insurance with carriers rated A.M. Best "A-" or better, with the following minimums:

- Commercial General Liability `{{CGL Limit}}` (floor: USD 1M per occurrence / USD 2M aggregate).
- Professional Liability / E&O `{{E&O Limit}}` (floor: USD 5M per claim / aggregate).
- Cyber Liability `{{Insurance Cyber Limit}}` (technology E&O, network-security and privacy liability; floor: USD 5M per claim / aggregate).
- Workers' Compensation and Employer's Liability: as state law requires.

On request, Vendor provides certificates of insurance. Customer may, on reasonable notice and not more than annually, request additional-insured status on the CGL policy where commercially available.

17.7. **Mutual IP indemnity.** *OPTIONAL — Customer-Favorable.* Replace §17.1 with a mutual IP indemnity in which each Party defends the other against IP-infringement claims arising from that Party's content (Vendor for the Service; Customer for Customer Data), with mirror-image carve-outs.

17.8. **EXCLUSIVE REMEDY.** §17 IS THE INDEMNIFIED PARTY'S EXCLUSIVE REMEDY FOR THIRD-PARTY CLAIMS WITHIN §§17.1, 17.4, OR 17.7.

---

## 18. General provisions

In one sentence: this section is the boilerplate — notices, compliance, force majeure, assignment, governing law, forum, and signatures.

18.1. **Notices.** Legal notices must be in writing and sent by hand, US first-class mail with delivery confirmation, or reputable overnight courier to the Order Form cover-page address. Routine operational notices may be sent by email to the registered address. Notices for material breach, termination, indemnity claim, and renewal opt-out are valid only if sent with read or delivery receipt to the legal-notices email on the Order Form.

18.2. **Compliance with law.** Each Party will comply with the laws applicable to its performance, including (a) the EAR (15 C.F.R. parts 730–774); (b) the ITAR (22 C.F.R. parts 120–130) where applicable; (c) OFAC sanctions programmes, including the SDN, NS-PLC, SSI, and Foreign Sanctions Evaders lists; (d) the FCPA (15 U.S.C. §§78dd-1, 78dd-2, 78dd-3, 78ff); and (e) Bank Secrecy Act and AML obligations applicable to its operations.

18.3. **No personal liability; federal-contractor carve-out.** No officer, director, employee, or agent of either Party has personal liability under the Agreement except where personal liability cannot be waived under applicable law (e.g., fraud or wilful misconduct). *OPTIONAL — only if Customer is the US Government or a federal contractor.* The flow-down clauses listed on the Order Form (which may include FAR 52.227-14, FAR 52.227-19, DFARS 252.227-7013, and FAR 52.204-21) are incorporated by reference and modify the corresponding sections to the extent required.

18.4. **Force majeure.** Neither Party is liable for failure or delay in non-monetary performance caused by an event beyond its reasonable control, including (a) acts of God, fire, flood, earthquake, severe weather, pandemic, or epidemic; (b) war, terrorism, civil unrest, or governmental order; (c) widespread internet outage or cyber attack on infrastructure outside the affected Party's control; (d) labour disturbance not specific to the affected Party; or (e) failure of utility, telecommunication, or cloud-infrastructure providers. The affected Party gives prompt notice and uses reasonable efforts to resume. After 60 days of continued force majeure, either Party may terminate the affected Order Form on notice.

18.5. **Assignment.** Neither Party may assign the Agreement without the other's prior written consent (not unreasonably withheld), except that either Party may assign on notice and without consent to (a) an Affiliate, (b) a successor in a merger, acquisition, internal reorganisation, or sale of all or substantially all assets or equity, or (c) any entity acquiring substantially all of the business line to which the Agreement relates, in each case where the assignee assumes the assignor's obligations in writing. Vendor may freely assign to an Affiliate or successor. Any assignment in violation of §18.5 is void.

18.6. **Independent contractors.** The Parties are independent contractors. Nothing creates a partnership, joint venture, agency, fiduciary, or employment relationship. Neither Party may bind the other.

18.7. **Entire agreement; severability.** The Agreement (CSA + Order Forms + Exhibits + DPA + AUP) is the entire agreement on the subject and supersedes prior or contemporaneous agreements. If a court holds a provision unenforceable, it is reformed to the minimum extent required to be enforceable, and the remainder remains in effect.

18.8. **Counterparts and electronic signatures.** The Agreement may be executed in counterparts, each an original. The Parties consent to electronic signatures and delivery by email, PDF, or e-signature platform, complying with E-SIGN (15 U.S.C. §7001 et seq.) and UETA as enacted in the applicable state.

18.9. **Governing law.** Governed by the law of `{{Choice Of Law State}}` (default: State of Delaware), excluding conflict-of-laws principles. The UN Convention on Contracts for the International Sale of Goods does not apply.

- *Alternative — New York.* For Order Forms with transaction value ≥USD 250,000, the Parties may select New York law per N.Y. Gen. Obligations Law §5-1401, which permits selection of New York law without a "reasonable relationship" requirement at that threshold.
- *Alternative — California.* For California-domiciled Customers, the Parties may select California law, in which case Cal. Civ. Code §1717 applies to attorneys'-fee provisions on a mutual basis.

18.10. **Forum.** Subject to §18.11, the Parties consent to the exclusive jurisdiction and venue of (a) the Delaware Court of Chancery for equitable relief or actions involving the internal affairs of a Delaware entity, and (b) the US District Court for the District of Delaware (or, if federal subject-matter jurisdiction is lacking, the Delaware state courts) for damages. As an alternative, the Order Form may submit disputes (other than emergency or interim equitable relief) to binding arbitration administered by the American Arbitration Association under its Commercial Arbitration Rules, seated at `{{Arbitration Seat}}` (default: Wilmington, Delaware), with one arbitrator below USD 1,000,000 in controversy and three above. Where the Order Form selects another `{{Arbitration Provider}}` (e.g., JAMS or NAM), that provider's rules apply with comparable seat and panel defaults. Either Party may seek emergency or interim equitable relief from a court without waiving the agreement to arbitrate.

18.11. **Class waiver — B2B only.** Each Party waives the right to participate in a class, collective, or representative action arising out of the Agreement. *`[VERIFY enforceability]`* — this waiver is intended to be enforced under the Federal Arbitration Act (9 U.S.C. §§1 et seq.) and is presented in a B2B context; it is not intended to apply to consumer relationships.

18.12. **Headings; construction.** Section headings are for convenience only and do not affect interpretation. "Including" means "including without limitation". Lists are illustrative. References to a statute or regulation include amendments and successors.

18.13. **No third-party beneficiaries.** Except for indemnified Affiliates, officers, directors, and employees identified in §17, the Agreement creates no third-party beneficiary rights.

---

## 19. Multi-State Service Provider Addenda

In one sentence: this section incorporates the state-specific processor/service-provider commitments needed under each comprehensive State Privacy Law that applies to processing under this CSA.

### 19.1 Colorado CPA service-provider terms (C.R.S. §6-1-1305)

For Personal Data of Colorado consumers within scope of the Colorado Privacy Act, Vendor acts as a "processor" under C.R.S. §6-1-1303(19), and the contractual terms of C.R.S. §6-1-1305(5) are incorporated. Vendor will: (a) process Personal Data only on Customer's documented instructions; (b) ensure personnel confidentiality; (c) assist Customer with consumer-rights requests, security obligations, data-protection assessments, and breach response; (d) at Customer's choice, return or delete Personal Data at the end of the engagement; (e) make available the information Customer reasonably requires to demonstrate compliance and allow and contribute to reasonable assessments; and (f) engage Subprocessors only under written equivalent terms after giving Customer an opportunity to object. Duration, nature and purpose, types of Personal Data, and categories of consumers are described in the Order Form and DPA.

### 19.2 Virginia VCDPA processor terms (Va. Code §59.1-579)

For Personal Data of Virginia consumers within scope of the VCDPA, Vendor acts as a "processor" under Va. Code §59.1-575, and the contractual terms of §59.1-579 are incorporated. Vendor will: (a) follow Customer's instructions; (b) assist with consumer-rights requests, security, breach notification, and data-protection assessments; (c) ensure personnel confidentiality; (d) at Customer's election, delete or return Personal Data at the end of services; (e) make available all information necessary to demonstrate compliance and allow and cooperate with reasonable assessments by Customer or a qualified independent assessor (assessment reports may be made available to Customer on request); and (f) engage Subprocessors only under a written equivalent contract. Sub-paragraphs (c)–(f) of §59.1-579 govern in case of conflict with the CSA's general provisions to the extent the VCDPA applies.

### 19.3 Connecticut CTDPA processor terms (Conn. Gen. Stat. §42-520)

For Personal Data of Connecticut consumers within scope of the CTDPA, Vendor acts as a "processor" under Conn. Gen. Stat. §42-515, and the contractual terms of §42-520 are incorporated. Vendor will: (a) follow Customer's instructions; (b) assist with consumer-rights responses, security duties, breach notification, and data-protection assessments; (c) maintain personnel confidentiality; (d) at Customer's choice, delete or return Personal Data at the end of services; (e) make information available to demonstrate compliance and cooperate with reasonable assessments; and (f) engage Subprocessors only under written equivalent terms after giving Customer a reasonable opportunity to object.

### 19.4 Texas TDPSA processor terms (Tex. Bus. & Com. Code §§541.101 et seq.) `[VERIFY]`

For Personal Data of Texas consumers within scope of the Texas Data Privacy and Security Act, Vendor acts as a "processor" under Tex. Bus. & Com. Code §541.001, and the processor terms under §541.104 (or successor) are incorporated. *`[VERIFY]`* — TDPSA is in force from 1 July 2024; review against the current statute and any AG regulations. Vendor will: (a) act on Customer's documented instructions; (b) assist with consumer-rights requests, security and breach obligations, and data-protection assessments; (c) maintain personnel confidentiality; (d) at Customer's election, delete or return Personal Data at end of services; (e) make available the information necessary to demonstrate compliance and contribute to reasonable assessments; and (f) engage Subprocessors only under written equivalent terms.

### 19.5 Oregon OCPA processor terms (ORS 646A.578)

For Personal Data of Oregon consumers within scope of the Oregon Consumer Privacy Act, Vendor acts as a "processor" under ORS 646A.570, and the contractual terms of ORS 646A.578 are incorporated. Vendor will: (a) process Personal Data only on Customer's documented instructions; (b) assist with consumer-rights requests, security, breach response, and data-protection assessments; (c) ensure personnel confidentiality; (d) at Customer's choice, delete or return Personal Data at end of services; (e) make information available to demonstrate compliance and cooperate with reasonable assessments; and (f) engage Subprocessors only under written equivalent terms after a reasonable opportunity for Customer to object.

### 19.6 Forward-looking principle

For each comprehensive State Privacy Law that takes effect after the Effective Date and applies here, the corresponding statutory processor/service-provider terms are deemed incorporated into §19, and Vendor performs consistently. Where a later statute imposes a stricter or additional processor obligation than CCPA, the stricter obligation governs processing within scope.

---

## Exhibit A — Order Form template

```
ORDER FORM

Order Form No.: {{Order Form Number}}
Effective Date: {{Order Effective Date}}

Customer: {{Customer Legal Name}}
Address: {{Customer Address}}
Billing contact: {{Customer Billing Contact}}
Legal-notices email: {{Customer Legal Notices Email}}

Vendor: {{Vendor Legal Name}}
Address: {{Vendor Address}}

1. Service tier and scope: {{Service Tier}}; {{Scope Description}}.
2. Service Provider Designation (CCPA): {{Service Provider Designation}} (Service Provider / Contractor / Third Party).
3. Authorised Affiliates: {{Authorised Affiliates}}.
4. Term: Initial {{Initial Term Months}} months; auto-renewal: {{Yes/No}}; renewal {{Renewal Term Months}} months.
5. Fees: {{Annual Fee}} USD per year, billed {{Billing Cadence}}; net {{Payment Days}} days.
6. Usage metric (if any): {{Metric}} = {{Metric Limit}} per {{Period}}.
7. SLA target: {{Uptime Target Percent}}% Monthly Uptime Percentage; credit schedule per Exhibit B.
8. Data residency: {{Data Residency Region}}.
9. Subprocessors list URL: {{Subprocessor List URL}}.
10. Liability cap floor (§16.5): {{Liability Cap Floor}} USD.
11. Insurance limits (§17.6): CGL {{CGL Limit}}; E&O {{E&O Limit}}; Cyber {{Insurance Cyber Limit}}.
12. Choice of law / forum (§§18.9–18.10): {{Choice Of Law State}}; arbitration {{Arbitration Provider}}; seat {{Arbitration Seat}}.
13. State-specific overlays elected: {{State Overlays}} (e.g., NYDFS Reg 500, MA 201 CMR 17, Texas SB 820, NYC Local Law 144).
14. AI training opt-in: {{Yes/No}}.
15. HIPAA BAA required: {{Yes/No}}; BAA reference: {{BAA Reference}}.
16. Federal-contractor flow-downs (§18.3): {{Flow-Down Clauses}}.
17. Special terms: {{Special Terms}}.

By signing below, each Party agrees this Order Form is bound by and incorporates the Cloud Service Agreement dated {{CSA Effective Date}}.

Customer signature: ____________________________  Date: __________
Name / Title: {{Customer Signatory Name}} / {{Customer Signatory Title}}

Vendor signature: ____________________________  Date: __________
Name / Title: {{Vendor Signatory Name}} / {{Vendor Signatory Title}}
```

---

## Exhibit B — SLA skeleton

**B.1. Definitions.** "**Monthly Uptime Percentage**" = (Total Minutes in Month − Downtime Minutes) ÷ Total Minutes in Month, as a percentage. "**Downtime Minutes**" = consecutive minutes the Service is materially unavailable to Customer for reasons other than the Excluded Events in §10.3.

**B.2. Service-credit schedule (default).**

| Monthly Uptime Percentage | Service Credit |
| --- | --- |
| < 99.9% but ≥ 99.0% | 10% of monthly fees for the affected Service |
| < 99.0% but ≥ 95.0% | 25% of monthly fees for the affected Service |
| < 95.0% | 50% of monthly fees for the affected Service |

**B.3. Tiered "enterprise" schedule (Customer-Favorable, optional).**

| Monthly Uptime Percentage | Service Credit |
| --- | --- |
| < 99.95% | 10% |
| < 99.9% | 25% |
| < 99.5% | 50% |
| < 99.0% | 100% |

**B.4. Chronic-failure termination.** Three SLA misses in any rolling six months entitle Customer to terminate the affected Order Form for cause and receive a pro-rata refund of prepaid unused fees.

**B.5. Reporting and claims.** Vendor publishes monthly availability metrics on the status page identified on the Order Form. Customer must claim a credit within 30 days of the affected month; approved credits apply to the next invoice.

---

## Exhibit C — DPA cross-reference

**C.1.** The Data Processing Addendum (the "**DPA**") is incorporated by reference. The current version is at `{{DPA URL}}` and is provided on request.

**C.2.** The DPA contains the operational detail required by CCPA/CPRA, CPA, VCDPA, CTDPA, TDPSA, OCPA, and any other comprehensive State Privacy Law applicable here, including the description of processing (subject matter, duration, nature and purpose, categories of PI, categories of data subjects), Subprocessor terms, security measures, breach-notification mechanics, data-subject-request workflow, and data retention/return.

**C.3.** Where the Order Form selects a HIPAA BAA, the BAA is a separate document referenced on the Order Form and supplements (without limiting) the DPA.

**C.4.** Where this CSA's general terms conflict with the DPA on a privacy-specific matter, the DPA controls to the extent necessary to satisfy the applicable State Privacy Law.

---

## Exhibit D — AUP cross-reference

**D.1.** The Acceptable Use Policy (the "**AUP**") is incorporated by reference. The current version is at `{{AUP URL}}`.

**D.2.** Customer's compliance with the AUP is a condition of the §4.1 licence; a material AUP breach is a material breach of the Agreement for §9.4 purposes.

**D.3.** Vendor may update the AUP from time to time on notice, provided an update does not (a) materially expand Customer's obligations beyond the AUP's stated purpose or (b) materially decrease Vendor's security or privacy commitments. Continued use after the update's effective date constitutes acceptance.

---

## Appendix — Merge fields used

| Field | Description |
| --- | --- |
| `{{Vendor Legal Name}}` / `{{Customer Legal Name}}` | Legal entity names |
| `{{Vendor State Of Formation}}` / `{{Customer State Of Formation}}` | State of organisation |
| `{{Vendor Entity Type}}` / `{{Customer Entity Type}}` | Entity type (corporation, LLC, etc.) |
| `{{Vendor Address}}` / `{{Customer Address}}` | Principal places of business |
| `{{Customer Billing Contact}}` / `{{Customer Legal Notices Email}}` | Customer contacts |
| `{{Customer Signatory Name}}` / `{{Customer Signatory Title}}` | Customer signing official |
| `{{Vendor Signatory Name}}` / `{{Vendor Signatory Title}}` | Vendor signing official |
| `{{Effective Date}}` / `{{CSA Effective Date}}` | CSA effective dates |
| `{{Order Form Number}}` / `{{Order Effective Date}}` | Order Form identifiers |
| `{{Service Tier}}` / `{{Scope Description}}` | Tier and scope |
| `{{Service Provider Designation}}` | CCPA role: Service Provider / Contractor / Third Party |
| `{{Authorised Affiliates}}` | Affiliates entitled to use under the Order Form |
| `{{Initial Term Months}}` / `{{Renewal Term Months}}` | Term durations |
| `{{Annual Fee}}` / `{{Billing Cadence}}` / `{{Payment Days}}` | Pricing and payment terms |
| `{{Metric}}` / `{{Metric Limit}}` / `{{Period}}` | Usage metering |
| `{{Uptime Target Percent}}` | SLA uptime target (e.g., 99.9) |
| `{{Data Residency Region}}` | Hosting region for Customer Data |
| `{{Subprocessor List URL}}` | URL of Vendor's Subprocessor list |
| `{{Liability Cap Floor}}` | Negotiated minimum liability cap |
| `{{CGL Limit}}` / `{{E&O Limit}}` / `{{Insurance Cyber Limit}}` | Insurance limits |
| `{{Choice Of Law State}}` | Selected governing-law state (default Delaware) |
| `{{Arbitration Provider}}` / `{{Arbitration Seat}}` | AAA / JAMS / NAM and seat (default Wilmington, DE) |
| `{{State Overlays}}` | Elected state overlays (e.g., NYDFS Reg 500, MA 201 CMR 17) |
| `{{Flow-Down Clauses}}` | Federal-contractor flow-downs, if any |
| `{{Special Terms}}` | Free-text special terms |
| `{{DPA URL}}` / `{{AUP URL}}` | URLs to the DPA and AUP |
| `{{BAA Reference}}` | Reference to a HIPAA BAA, if applicable |

---

## Appendix — Authoritative references

Public-domain US government sources and permissively-licensed reference materials (CC0, CC-BY-4.0, MIT, Apache-2.0, BSD, OGL, MPL-2.0). No proprietary SaaS templates were consulted.

- **US Code (uscode.house.gov).** 15 U.S.C. §§78dd-1–78ff (FCPA); 15 U.S.C. §§6801 et seq. (GLBA); 15 U.S.C. §§7001 et seq. (E-SIGN); 15 U.S.C. §§8401–8405 (ROSCA); 18 U.S.C. §§1836, 1839 (DTSA); 9 U.S.C. §§1 et seq. (FAA).
- **CFR.** 15 C.F.R. parts 730–774 (EAR); 22 C.F.R. parts 120–130 (ITAR); 16 C.F.R. Part 314 (GLBA Safeguards Rule); 16 C.F.R. Part 425 (FTC Click-to-Cancel) `[VERIFY commencement]`; 16 C.F.R. Part 910 (FTC Non-Compete Rule) `[VERIFY enforceability]`.
- **California (oag.ca.gov; cppa.ca.gov).** Cal. Civ. Code §1798.82, §1798.140 et seq. (CCPA/CPRA); Cal. Bus. & Prof. Code §16600; §17600 et seq. (ARLDA); Cal. Code Regs. tit. 11 §§7120–7129 (CPPA Cybersecurity Audit) `[VERIFY commencement]`; tit. 11 §§7150–7158, 7200–7222 (CPPA ADMT) `[VERIFY adoption]`; SB 942 (AI Transparency Act) `[VERIFY]`.
- **Other state statutes.** Colorado Privacy Act (C.R.S. §§6-1-1301 et seq.); Colorado HB 21-1063; Colorado SB 24-205 (Colorado AI Act) `[VERIFY commencement]`; Connecticut Data Privacy Act (Conn. Gen. Stat. §§42-515 et seq.); Illinois ARLDA (815 ILCS 601/); Massachusetts 201 CMR 17.00; New Jersey TCCWNA (N.J.S.A. §56:12-14 et seq.); 23 NYCRR Part 500; N.Y. GBL §527-a; N.Y. Gen. Obligations Law §5-1401; NYC Admin. Code §§20-870 et seq. (Local Law 144); Oregon Consumer Privacy Act (ORS §§646A.570 et seq.); Oregon HB 2479 (ORS 646A.293); Texas SB 820; Texas TDPSA (Tex. Bus. & Com. Code §§541.001 et seq.) `[VERIFY]`; Virginia VCDPA (Va. Code §§59.1-575 et seq.).
- **Federal regulators.** FTC negative-option / data-security guidance (ftc.gov); BIS export-control guidance (bis.doc.gov); OFAC sanctions lists and FAQs (treasury.gov/ofac); Interagency Guidance on Third-Party Relationships (Fed/OCC/FDIC, June 2023).
- **Arbitration providers.** AAA Commercial Arbitration Rules (adr.org); JAMS Comprehensive Arbitration Rules (jamsadr.com); NAM Commercial Arbitration Rules (namadr.com).
- **Permissively-licensed templates.** Common Paper Cloud Service Agreement v2.1 [CC-BY-4.0]; Common Paper Order Form [CC-BY-4.0]; Common Paper AI Addendum [CC-BY-4.0]; Bonterms Cloud Terms [CC-BY-4.0]; Bonterms PSA v1.2 [CC0]; GitHub site-policy [CC0]; Mozilla Terms [MPL-2.0]. Consultations were structural; no five-or-more-word verbatim runs were copied.

---

## Not legal advice

This template is for general information only and does not constitute legal, tax, or other professional advice. No lawyer-client relationship is created by use of this template. Statutes, regulations, and case law cited here change frequently; items flagged `[VERIFY]`, `[VERIFY commencement]`, `[VERIFY enforceability]`, or `[VERIFY adoption]` should be checked against current sources before execution. The template is a B2B starting point and is not suitable for consumer-facing transactions, transactions in regulated industries with their own form-contract regimes (e.g., government procurement, healthcare provider contracting, insured banking deposit relationships), or transactions involving highly sensitive data such as classified information or ITAR-controlled technical data. Each Party should consult qualified US counsel licensed in the relevant state(s) before signing. Use is at the user's sole risk and the authors disclaim all liability arising from its use to the fullest extent permitted by law.
