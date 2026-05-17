---
title: Master Services Agreement (US)
jurisdiction: us
statutes:
  - 17 USC §101 (work-for-hire)
  - 18 USC §1833(b) (DTSA whistleblower notice)
  - UCC Art. 2 (analog, services)
  - CCPA / CPRA (Cal. Civ. Code §§1798.100–1798.199.100)
  - FAR 52.227-14 / DFARS 252.227-7013, 7014
license: MIT
last_updated: 2026-04-29
---

# {{MSA Title}} — United States Variant

This is the US variant of the Legalcode Master Services Agreement (MSA). It pairs with one or more Statements of Work (SOWs) executed under `legalcode-sow` (see Annex A), or with Order Forms executed under `legalcode-order-form`. The MSA is the legal and commercial baseline; the SOW carries the deal-specific particulars.

The variant assumes Delaware law as the default governing law (with New York as an alternative), and is drafted around US federal copyright assignment formalities, the IRS / DOL worker-classification framework, state-by-state late-payment caps, and federal flow-down obligations under FAR / DFARS, OFAC, and CCPA / CPRA.

## Merge fields

In addition to the common merge fields documented in the pack `README.md`, the US variant uses the following:

```
{{State of Formation}}              # e.g., "Delaware", "California", "Texas"
{{Provider State of Formation}}     # State / jurisdiction of incorporation for Provider
{{Client State of Formation}}       # State / jurisdiction of incorporation for Client
{{Primary Performance State}}       # State where most services are performed
{{ABC Test State}}                  # If services performed in CA / NJ / MA / IL — list applicable
{{1099 Threshold}}                  # Default $600; bumped to $5,000 for tax year 2026 [VERIFY]
{{W-9 / W-8BEN-E Required}}         # "W-9" (US persons) or "W-8BEN-E" (foreign entity)
{{Sales Tax Allocation}}            # "Client bears" / "Provider bears" / "as separately stated on invoice"
{{State Late-Fee Cap}}              # statutory cap, e.g. "TX: 6% APR; NY: 9%; CA: reasonable"
{{Federal Flow-Down Trigger}}       # "yes — Client is federal prime"; "no"; "yes — state government"
{{Government Contract Clauses}}     # Listed FAR/DFARS clauses to incorporate
{{ITAR / EAR Applicability}}        # "yes" / "no" — drives §19 export reps
{{HIPAA BAA Required}}              # "yes" — execute companion BAA
{{GLBA Applicability}}              # "yes" / "no"
{{FERPA Applicability}}             # "yes" / "no"
{{State Breach Notification SLA}}   # Default "without undue delay; no later than 72 hours to Client"
{{Arbitration Forum}}               # "AAA Commercial" or "JAMS Comprehensive"
{{Arbitration Seat}}                # "Wilmington, DE" / "New York, NY"
{{Class Action Waiver}}             # "yes" / "no"
{{Jury Trial Waiver}}               # "yes" / "no"
{{Mediation Provider}}              # "AAA" / "JAMS" / "CPR Institute"
{{IP Carve-Out for Injunctive Relief}}  # default "yes"
{{Non-Solicit Period}}              # default "12 months"
{{Non-Solicit Geography}}           # default "United States"
{{Convenience Termination Fee}}     # e.g., "30 days fees + unrecovered hard costs"
{{Transition Period Length}}        # default "90 days"
{{Foreground IP Election}}          # "Client owns" / "Provider retains; Client license"
{{Open Source License Whitelist}}   # e.g., "MIT, Apache-2.0, BSD-2/3, ISC, CC0"
{{Open Source License Blacklist}}   # e.g., "AGPL, GPL v2/v3, SSPL, Commons Clause, BUSL"
{{DMCA Agent Designation}}          # only if Provider hosts user-generated content
{{Section 230 Carve-Out}}           # only if Provider operates an interactive computer service
```

Where a value is jurisdiction-specific or rapidly changing (state breach-notification deadlines, ABC-test state list, federal small-claims thresholds), an inline `[VERIFY: …]` flag identifies what to confirm before signature.

---

## 1. Plain-language summary

This summary is for orientation only and does not modify the operative provisions.

This is a framework agreement between {{Provider Legal Name}} ({{Provider Short Name}}) and {{Client Legal Name}} ({{Client Short Name}}). It does not by itself authorise any work. Each engagement is scoped through a Statement of Work (Annex A) or Order Form. The Agreement covers services, fees, change control, acceptance, IP, confidentiality, data protection, risk allocation, insurance, termination, and dispute resolution. It is governed by the laws of {{Governing Law}} and disputes follow §18. Either party may exit on the notice and cure rules in §16.

## 2. Definitions

This section defines the recurring capitalised terms; capitalised terms not defined here have the meaning given to them in the relevant SOW or in applicable law.

2.1 **"Affiliate"** means, with respect to a party, any entity that directly or indirectly controls, is controlled by, or is under common control with that party, where "control" means more than 50 % of the voting power or equivalent governing interest.

2.2 **"Agreement"** means this Master Services Agreement, every executed SOW or Order Form, every Change Order, and every annex and exhibit, taken as a single integrated agreement.

2.3 **"Background IP"** means intellectual property owned, licensed, or developed by a party before the Effective Date or independently of any Services, including methodologies, frameworks, libraries, tools, templates, know-how, and pre-existing software.

2.4 **"Business Day"** means a day other than a Saturday, Sunday, or US federal holiday in {{Primary Performance State}}.

2.5 **"Change Order"** means a written instrument executed under §6 modifying a SOW.

2.6 **"Confidential Information"** has the meaning in §10.

2.7 **"Deliverables"** means the tangible and intangible work product identified in a SOW as deliverables, in the form and to the standard required by the SOW.

2.8 **"DTSA"** means the Defend Trade Secrets Act of 2016, 18 USC §§1831 et seq.

2.9 **"Effective Date"** means {{MSA Effective Date}}.

2.10 **"Foreground IP"** means intellectual property created, conceived, reduced to practice, or first fixed in tangible form by Provider personnel in the course of performing Services under a SOW, excluding Background IP.

2.11 **"Government Contract"** means any prime contract, subcontract, grant, cooperative agreement, or other instrument with a federal, state, or local government for which Services constitute work performed in support of the Government Contract.

2.12 **"Intellectual Property Rights"** or **"IP Rights"** means all rights in patents, copyrights, mask works, trademarks, trade secrets, database rights, design rights, moral rights, and all analogous statutory or common-law rights, in each case worldwide and whether registered or unregistered.

2.13 **"Key Personnel"** means the individuals identified as key personnel in a SOW or in Annex B.

2.14 **"Personal Information"** means information that identifies, relates to, describes, or could reasonably be linked with an identified or identifiable individual or household, including under CCPA / CPRA.

2.15 **"Services"** means the services described in a SOW.

2.16 **"SOW"** or **"Statement of Work"** means a statement of work executed under this Agreement substantially in the form of Annex A.

2.17 **"Subcontractor"** means a third party engaged by Provider to perform a portion of the Services.

2.18 **"Term"** means the term of this Agreement as set out in §16.

## 3. Engagement structure (MSA + SOW / Order Form framework)

This section explains how the MSA, SOWs, and Order Forms fit together — the MSA carries the umbrella terms, and each SOW or Order Form carries the deal-specific particulars.

3.1 *Framework agreement.* This Agreement does not on its own create any obligation to engage Provider, to purchase Services, or to make any payment. Each engagement is scoped through an executed SOW or Order Form, signed by an authorised representative of each party.

3.2 *Order of precedence.* In the event of conflict among the documents that comprise this Agreement, the order of precedence is: (a) the body of this MSA; (b) any annex or exhibit to this MSA; (c) the SOW or Order Form applicable to the engagement at issue; (d) any Change Order to that SOW or Order Form, with later-dated Change Orders prevailing over earlier; and (e) any purchase order or other administrative document. A purchase order's pre-printed terms do not modify this Agreement notwithstanding any acceptance, performance, or payment by either party. Modifications to a SOW are effective only through a Change Order, consistent with UCC §2-209 [VERIFY: confirm UCC Art. 2 analog applies as drafting parallel given Services are not goods].

3.3 *SOW execution.* SOWs may be executed by countersigned PDF, by {{SOW Approval Method}}, or by another method the parties agree in writing. An SOW is effective when both parties have signed.

3.4 *Affiliates.* Either party's Affiliates may execute SOWs in their own name; in that case, the Affiliate is bound by this Agreement as if it were the original signatory, and the original signatory remains liable for its Affiliate's performance only if it expressly agrees in the SOW to do so.

## 4. Scope of services & SOW process

This section governs how Services are scoped, ordered, and modified, and how non-SOW work is handled.

4.1 *Required SOW contents.* Each SOW will identify, at minimum: the Services to be performed; the Deliverables; the schedule and any milestones; fees, expenses, and invoicing cadence; acceptance criteria and the acceptance period (default {{Acceptance Period}}); any Key Personnel; the location(s) of performance; and any Service-level commitments.

4.2 *No work without an SOW.* Provider shall not commence Services and Client shall have no obligation to pay for Services performed before the relevant SOW is fully executed, unless the parties have signed a separate written letter of authorisation referencing this Agreement.

4.3 *Provider responsibilities.* Provider shall perform the Services in a professional and workmanlike manner consistent with industry standards for similar services, using qualified personnel, and in accordance with the requirements set out in the SOW.

4.4 *Client responsibilities.* Client shall provide timely access to information, personnel, systems, and decision-makers reasonably necessary for Provider to perform; review and respond to Provider's requests within the time-frames set in the SOW; and timely review Deliverables.

4.5 *Dependencies and assumptions.* Each SOW will list Provider's material assumptions and Client's dependencies. If a Client dependency is not met or an assumption proves materially incorrect, Provider's schedule and fees may be adjusted through Change Order under §6.

## 5. Fees, expenses & invoicing

This section sets the commercial baseline for fees, expenses, taxes, and invoicing — including state-by-state late-fee rules. **Dual-perspective.**

5.1 *Fee structures.* Fees may be fixed-fee, time and materials, milestone-based, retainer, or any other structure agreed in the SOW. Rates and any rate-card escalation rules are stated in the SOW.

5.2 *Expenses.* Expenses are reimbursable only if pre-approved in the SOW or otherwise in writing, charged at cost without mark-up unless the SOW provides otherwise, and reasonable in light of the Services. Provider shall produce supporting documentation on request.

5.3 *Invoicing and payment terms.* Provider invoices on the cadence set in the SOW (default monthly in arrears). Invoices are payable {{Payment Terms}} from receipt by {{Client AP Email}}. Disputed amounts must be flagged in writing within {{Acceptance Period}} of invoice date with reasonable detail; undisputed amounts on the same invoice remain payable.

5.4 *Late fees.* Undisputed amounts not paid by the due date accrue interest at {{Late Fee Rate}}, subject to the lower of (a) that contract rate or (b) the maximum rate permitted under {{Governing Law}}. Where Services are performed in {{Primary Performance State}}, the parties acknowledge state usury and late-fee caps apply (illustrative: Texas — 6 % APR default civil judgment rate; New York — 9 % statutory; California — reasonable rate, no fixed cap; Florida — Wall Street Journal Prime + statutory adjustment) [VERIFY: state late-fee cap on Effective Date].

5.5 *Taxes.* Fees are exclusive of sales, use, gross-receipts, value-added, and similar transaction taxes, which are allocated as {{Sales Tax Allocation}}. Each party bears its own income, franchise, and net-worth taxes. Provider shall separately state any tax it is required by law to collect.

5.6 *Tax forms.* Provider shall furnish a current IRS Form W-9 (US persons) or W-8BEN-E (foreign entities) before the first invoice. Client may issue Form 1099-NEC or 1099-MISC for amounts at or above the {{1099 Threshold}} reporting threshold.

5.7 *Withholding.* If Client is required by law to withhold any amount from a payment, Client shall withhold the legally required minimum and remit the balance, and Provider shall furnish such certifications and treaty claims as may reduce the withholding.

5.8 *Dual-perspective triple — fees & invoicing.*

- *Client-favorable.* Net 60 from invoice receipt; 30-day dispute window; late fees only on undisputed amounts after a 10 Business Day grace period; no automatic rate increases during the SOW; expenses capped at the SOW expense budget; no expedite or after-hours premiums without prior written approval.
- *Provider-favorable.* Net 15 from invoice date; late fees accrue daily at the lesser of 1.5 % per month or maximum legal rate; suspension of Services right after 15 days past due; annual rate-card escalation indexed to CPI-U or 5 %, whichever is greater; expenses billed at cost plus 10 % handling.
- *Market-standard.* Net 30 from invoice receipt; 15-day dispute window; late fees at the lesser of 1 % per month or maximum legal rate; rate increases by Change Order with 60 days' notice; no SOW-time auto-escalation absent SOW provision; expenses at cost without mark-up.

## 6. Change control & change orders

This section governs how scope and price changes are made — written, signed, and tracked. **Dual-perspective.**

6.1 *Change Order required.* Any change to the scope, schedule, fees, Key Personnel, or acceptance criteria of a SOW is effective only by a Change Order signed by both parties. Pre-printed PO terms, internal ticket updates, and informal correspondence do not constitute a Change Order. This contractual modification rule is consistent with UCC §2-209 (analog application to services).

6.2 *Change Order process.* Either party may request a change. Provider shall provide a written change estimate (impact on schedule, fees, dependencies, risks) within five (5) Business Days of a written request, and the parties shall negotiate in good faith. Provider may decline a change that is technically infeasible or that would cause it to breach a third-party obligation.

6.3 *Pending change.* Pending execution of a Change Order, Provider shall continue to perform under the existing SOW unless the parties agree in writing to pause work. If Provider continues at Client's written direction pending a Change Order, Provider may invoice on a time-and-materials basis at the SOW rate, subject to reconciliation when the Change Order is signed.

6.4 *Dual-perspective triple — change control.*

- *Client-favorable.* Provider absorbs the first eight (8) hours of estimating effort per change request; Provider may not refuse a change purely for commercial reasons; Client may direct Provider to "stop and reprice" on any pending change at no termination cost; Provider's hourly rate for Change Order work is the SOW rate without uplift.
- *Provider-favorable.* All change-estimating effort is billable at the SOW rate; if Client cancels a request after Provider begins estimating, Client pays the estimating fee; Provider's standard rate for Change Order work is rate-card plus 15 %; Client must respond to a change estimate within ten (10) Business Days or it is deemed rejected.
- *Market-standard.* Provider absorbs estimating up to four (4) hours; estimating beyond that is billable at the SOW rate; Provider may decline only for technical-infeasibility, ethics, conflict-of-interest, or third-party-licence reasons; the parties act in good faith and document the basis of any decline.

## 7. Personnel, key personnel & subcontracting

This section governs who performs the Services — including IRS / DOL classification posture and ABC-test state overlays.

7.1 *Independent contractor status.* Provider is an independent contractor. Nothing in this Agreement creates a partnership, joint venture, agency, fiduciary, or employment relationship. Provider personnel are not Client employees and are not entitled to any Client employee benefits, tax withholding, or employment protections, regardless of the duration of the engagement.

7.2 *Classification representation.* Provider represents that, with respect to its personnel, it: (a) maintains the right to control the manner and means of performance consistent with the IRS twenty-factor / common-law test for independent-contractor status; (b) carries Workers' Compensation coverage as required by applicable state law and employer's liability coverage at no less than the limit in §15; and (c) classifies its personnel under the FLSA exempt / non-exempt framework consistent with 29 CFR §541. In any state where the ABC test applies (including {{ABC Test State}} — California (Lab. Code §2775 / AB-5), New Jersey, Massachusetts, Illinois HB1063, and others) [VERIFY: ABC test state list on Effective Date], Provider represents that its provision of Services satisfies all three prongs of the applicable test as to its own personnel.

7.3 *Section 2870 / state inventions.* Where personnel are California residents, the parties acknowledge California Labor Code §2870 limits the assignment of employee inventions developed entirely on the employee's own time without using employer resources and that do not relate to the employer's business. Provider's pre-engagement onboarding shall include the §2870 notice (and analogous notices in Delaware, Illinois, Kansas, Minnesota, North Carolina, Utah, Washington) [VERIFY: states with employee-invention statutes].

7.4 *Key Personnel.* The SOW (or Annex B) will identify Key Personnel. Provider shall not remove or reassign Key Personnel without Client's prior written consent, except for: (a) resignation; (b) termination for cause; (c) extended illness or family leave; (d) death; or (e) reassignment with Client's consent. Replacement Key Personnel must have substantially equivalent qualifications.

7.5 *Subcontracting.* Provider may engage Subcontractors only as listed in Annex B or as Client otherwise approves in writing (not unreasonably withheld). Provider remains primarily responsible for all Services performed by its Subcontractors, including the obligations in §10 (Confidentiality), §11 (Data Protection), §9 (IP), and §15 (Insurance). Subcontracts shall include flow-down terms substantially consistent with this Agreement.

7.6 *Non-solicit.* During the Term and for {{Non-Solicit Period}} after its expiry or termination, neither party shall directly solicit for employment any individual who is or was during the prior twelve months a Key Personnel of the other party engaged on the SOW, in {{Non-Solicit Geography}}. General job-postings, recruiter-databases, and unsolicited approaches initiated by the candidate are excluded. The non-solicit is intended to be enforceable only to the extent permitted in {{Primary Performance State}}; in California it is limited to confidentiality-protective non-solicits consistent with Bus. & Prof. Code §16600 [VERIFY: CA non-solicit enforceability].

7.7 *Background checks.* Each party may conduct, at its own cost, lawful background, reference, and credentialing checks of personnel proposed for the engagement, subject to FCRA, state ban-the-box laws, and the candidate's prior written authorisation.

## 8. Acceptance & deliverables

This section sets out how Deliverables are reviewed, accepted, or rejected — and the deemed-acceptance default.

8.1 *Acceptance criteria.* The SOW shall set out the acceptance criteria for each Deliverable. Where the SOW is silent, the criterion is conformance in all material respects with the Deliverable description and the requirements of the SOW.

8.2 *Acceptance period and notice of rejection.* Client has {{Acceptance Period}} from receipt of a Deliverable to inspect and either accept it in writing or send a written notice of rejection identifying with reasonable specificity each non-conformance and the required correction. Failure to send such a notice within the acceptance period results in deemed acceptance after {{Deemed Acceptance Window}}. Acceptance is not waived by use of a Deliverable for evaluation purposes during the acceptance period.

8.3 *Cure.* If Client timely rejects a Deliverable, Provider shall use commercially reasonable efforts to correct each identified non-conformance within a reasonable cure period (default fifteen (15) Business Days for software Deliverables, ten (10) Business Days for documents). After cure, Client has a re-inspection period equal to half the original acceptance period.

8.4 *Repeated failure.* If Provider fails to cure non-conformances after two (2) cure cycles, Client may, at its option: (a) accept the Deliverable as is with an equitable price adjustment; (b) terminate the affected SOW for cause under §16; or (c) require Provider to refund the fees paid for the non-conforming Deliverable, in each case in addition to other remedies in this Agreement.

8.5 *Partial acceptance.* Client may accept any portion of a Deliverable that materially conforms while rejecting non-conforming portions, provided that the accepted portion is independently usable.

8.6 *Cure analog to UCC.* The cure / inspection / rejection structure of this section is intended to parallel UCC Art. 2 §§2-508, 2-513, 2-606, 2-607 by analogy. The parties acknowledge Services are not "goods" within Art. 2 but adopt this framework as a contractual standard.

## 9. Intellectual property (foreground / background / open-source)

This section assigns intellectual property in Foreground IP, preserves Background IP, and governs open-source. **Dual-perspective.**

9.1 *Background IP.* Each party retains all right, title, and interest in its Background IP. Neither party acquires any rights in the other's Background IP except a non-exclusive licence to use it as embedded in or necessary to use Deliverables, on the terms of the SOW.

9.2 *Foreground IP — work-for-hire.* To the maximum extent permitted under 17 USC §101 and the U.S. Copyright Act, Foreground IP that constitutes a "work made for hire" by reason of being one of the nine enumerated categories (a contribution to a collective work; a translation; a part of a motion picture or other audiovisual work; a compilation; an instructional text; a test; answer material for a test; an atlas; or a supplementary work) and that is specially commissioned in writing under the SOW shall be deemed a work made for hire and Client shall be the author and owner of all such Foreground IP.

9.3 *Foreground IP — present-tense assignment.* To the extent any Foreground IP does not qualify as a work made for hire under §9.2, Provider hereby assigns to Client, by present-tense conveyance effective on creation, all right, title, and interest in and to that Foreground IP, including all IP Rights therein, free and clear of all liens and encumbrances. Provider shall execute such further instruments as are reasonably necessary to perfect, record, and enforce the assignment, at Client's expense, and irrevocably appoints Client as Provider's attorney-in-fact for the limited purpose of executing such instruments if Provider fails to do so within fifteen (15) Business Days of written request.

9.4 *Moral rights.* To the extent moral rights, droit moral, or analogous rights exist in any jurisdiction in which Foreground IP is created or used, Provider waives such rights in favour of Client to the maximum extent permitted by law and consents to all uses of the Foreground IP that would otherwise infringe such rights.

9.5 *Employee-invention carve-out.* Nothing in this section purports to assign to Client any invention that, under California Labor Code §2870 or analogous state laws (Delaware Code Title 19 §805, Illinois 765 ILCS 1060/2, Kansas Stat. Ann. §44-130, Minnesota Stat. §181.78, North Carolina Gen. Stat. §66-57.1, Utah Code §34-39-3, Washington RCW §49.44.140), an employee may not lawfully be required to assign. Each party will give its personnel any notice required under those statutes.

9.6 *Provider Background IP licence.* Provider grants Client a perpetual, irrevocable, worldwide, royalty-free, sublicensable (in connection with the Deliverables) licence to use, reproduce, modify, distribute, perform, display, and create derivative works of any Provider Background IP that is incorporated into Foreground IP, solely as required to use, exploit, modify, and maintain the Foreground IP.

9.7 *Open-source disclosure.* Provider shall disclose, on a per-Deliverable basis (a "FOSS Disclosure"), every third-party open-source or third-party-licensed component used in or required by the Deliverable, including the licence type, version, source URL or hash, and any known notice obligations. Provider shall use only open-source components consistent with {{Open Source Policy}}, the Open Source License Whitelist, and not on the Open Source License Blacklist; copyleft components (AGPL, GPL, SSPL) shall not be incorporated without Client's prior written consent. Provider shall comply with attribution and notice requirements (e.g., Apache NOTICE files, MIT / BSD attribution).

9.8 *Government contract IP.* Where any portion of the Services is performed under a Government Contract: (a) data deliverables under a civilian-agency prime are governed by FAR 52.227-14 (rights in data — general), with restricted-rights and limited-rights designations applied as identified in the SOW; (b) data deliverables under a DoD prime are governed by DFARS 252.227-7013 (technical data) and DFARS 252.227-7014 (computer software); and (c) any deliverables developed exclusively at private expense bear an SBIR data-rights or limited-rights legend as appropriate. Provider shall mark deliverables with the legends prescribed in the cited clauses.

9.9 *Pre-existing rights.* Each party represents it has the right to grant the licences granted in this section.

9.10 *Dual-perspective triple — IP ownership.*

- *Client-favorable.* All Foreground IP is work-for-hire and, to the extent not, is hereby assigned (per §9.2 / §9.3); Provider Background IP licence is perpetual and sublicensable to Client's customers; copyleft open-source is prohibited absent prior written consent; Provider warrants that Foreground IP does not incorporate AGPL, GPL, or SSPL components.
- *Provider-favorable.* Provider retains Foreground IP and grants Client a perpetual non-exclusive licence for internal business use; Background IP is reserved without licence beyond what is strictly necessary; open-source disclosure on request only; no §2870-style carve-out clause beyond minimum statutory requirements.
- *Market-standard.* Foreground IP assigned to Client as drafted in §9.2 / §9.3, with reservation by Provider of generally applicable methodologies, frameworks, and tools as Background IP; open-source disclosure required at Deliverable level; permissive licences only without prior approval; Provider retains residual-knowledge rights as defined in §10.

## 10. Confidentiality

This section governs Confidential Information, including the DTSA whistleblower notice required where Provider personnel could be DTSA-protected.

10.1 *Definition.* "Confidential Information" means any non-public information disclosed by a party (the "Discloser") to the other (the "Recipient") that is marked confidential, identified as confidential at the time of disclosure, or that a reasonable person would understand to be confidential under the circumstances. It includes business plans, customer lists, pricing, technical roadmaps, source code, security documentation, Personal Information, and the contents of this Agreement (but not its existence).

10.2 *Exclusions.* Confidential Information does not include information that the Recipient can show: (a) was lawfully in its possession without confidentiality restriction before disclosure; (b) is or becomes generally available to the public other than through Recipient's breach; (c) is rightfully received from a third party without confidentiality obligation; or (d) is independently developed by Recipient without use of or reference to the Discloser's Confidential Information.

10.3 *Obligations.* Recipient shall: (a) use the Confidential Information solely to perform under this Agreement or to receive the Services; (b) protect it with at least the care it uses for its own confidential information of like importance, and in any event no less than reasonable care; and (c) limit access to personnel, Subcontractors, and professional advisers who have a need to know and who are bound by written or professional confidentiality obligations no less protective.

10.4 *Compelled disclosure.* If the Recipient is compelled by law, subpoena, or government request to disclose Confidential Information, it shall (where lawfully permitted) notify the Discloser promptly and cooperate at the Discloser's expense in seeking a protective order or other remedy.

10.5 *DTSA whistleblower notice (18 USC §1833(b)).* The parties give the following notice to all Provider personnel and Subcontractor personnel who may have access to trade secrets under this Agreement:

> NOTICE OF IMMUNITY UNDER THE DEFEND TRADE SECRETS ACT OF 2016. Notwithstanding any other provision of this Agreement, you are hereby notified that, under 18 U.S.C. §1833(b), you cannot be held criminally or civilly liable under any federal or state trade-secret law for the disclosure of a trade secret that: (a) is made (i) in confidence to a federal, state, or local government official, either directly or indirectly, or to an attorney; and (ii) solely for the purpose of reporting or investigating a suspected violation of law; or (b) is made in a complaint or other document filed in a lawsuit or other proceeding, if such filing is made under seal. If you file a lawsuit for retaliation by an employer for reporting a suspected violation of law, you may disclose the trade secret to your attorney and use the trade-secret information in the court proceeding, if you (a) file any document containing the trade secret under seal; and (b) do not disclose the trade secret, except pursuant to court order.

10.6 *Residual knowledge.* Nothing in this section restricts the use, by Recipient personnel, of general knowledge, skills, and experience retained in unaided memory, provided that such use does not involve the disclosure or use of Discloser's Confidential Information in a form recognisable as such.

10.7 *Term of obligation.* Confidentiality obligations survive for five (5) years following expiry or termination of this Agreement, except that obligations with respect to information that constitutes a trade secret continue for so long as the information remains a trade secret under applicable law.

10.8 *Return or destruction.* On expiry or termination, or on Discloser's earlier written request, Recipient shall promptly return or destroy all Confidential Information and certify in writing that it has done so, except that Recipient may retain copies as required by law, regulatory record-keeping, or its bona fide back-up and disaster-recovery procedures, in each case subject to continuing confidentiality.

## 11. Data protection & information security

This section addresses Personal Information processing, US federal and state privacy obligations, and information-security minimums.

11.1 *Roles and applicability.* Where Provider processes Personal Information of Client's consumers, employees, or end-users, Provider acts as a "Service Provider" within the meaning of the California Consumer Privacy Act / California Privacy Rights Act (CCPA / CPRA, Cal. Civ. Code §§1798.100–1798.199.100) and as a "processor" or analogous role under other applicable US state privacy laws (CO CPA, CT DPA, VA CDPA, UT UCPA, TX TDPSA, OR CPA, MT CPA, IA ICDPA, DE DPDPA, NH SB-255) [VERIFY: state-privacy laws in force on Effective Date].

11.2 *Service Provider obligations.* Provider shall: (a) process Personal Information only for the limited and specified business purpose of performing the Services; (b) not retain, use, or disclose Personal Information for any commercial purpose other than the Services; (c) not "sell" or "share" Personal Information as those terms are defined under CCPA / CPRA; (d) not combine Personal Information received from Client with Personal Information from any other source, except to perform a permitted business purpose; (e) cooperate with Client's responses to consumer rights requests under applicable state privacy laws; (f) flow these obligations down to any Subcontractor that processes Personal Information; and (g) notify Client in writing if Provider determines it can no longer meet its obligations.

11.3 *Information security.* Provider shall maintain a written information-security programme that implements administrative, physical, and technical safeguards appropriate to the sensitivity and volume of Personal Information processed, consistent with NIST SP 800-171 (controlled unclassified information) and the NIST Cybersecurity Framework v2.0, and reasonably designed to: protect the confidentiality, integrity, and availability of Client data; protect against anticipated threats; and protect against unauthorised access. Specific controls include access controls, encryption in transit (TLS 1.2+) and at rest (AES-256), MFA for administrative access, vulnerability management, secure software-development life cycle, audit logging, secure disposal, and incident response.

11.4 *Incident notification.* Provider shall notify Client at {{Client Notice Email}} {{State Breach Notification SLA}} after determining a Security Incident affecting Client data has occurred. "Security Incident" means any unauthorised access, acquisition, use, disclosure, modification, or destruction of Client data, or any event reasonably likely to require notification under any state breach-notification law (including CA Civ. Code §1798.82, NY SHIELD Act, MA 201 CMR 17.00, and the 50-state matrix) [VERIFY: state breach-notification deadlines on Effective Date]. The notice shall include the information reasonably required for Client to make its own notification determinations.

11.5 *Sectoral overlays.*
*OPTIONAL — only if HIPAA Applicability is "yes".* The parties shall execute a Business Associate Agreement substantially in the form of `legalcode-baa` before any disclosure of protected health information.
*OPTIONAL — only if FERPA Applicability is "yes".* Provider shall act as a "school official" under 34 CFR §99.31(a)(1), shall comply with FERPA, and shall not redisclose education records.
*OPTIONAL — only if GLBA Applicability is "yes".* Provider shall comply with the FTC Safeguards Rule, 16 CFR Part 314, including risk-assessment, MFA, encryption, and incident-reporting requirements.

11.6 *Data-residency and cross-border.* Unless otherwise agreed in the SOW, Provider shall process Personal Information in the United States. Cross-border transfers, if any, are subject to a separate data-processing addendum (`legalcode-dpa`).

11.7 *Audit.* Once per calendar year, and at any time following a Security Incident, Client may, on at least thirty (30) days' written notice, audit Provider's compliance with this section through review of an industry-recognised third-party audit report (SOC 2 Type II, ISO 27001, or equivalent) or, where no such report covers the relevant controls, through an on-site or remote audit during business hours, in each case at Client's expense and subject to confidentiality.

11.8 *Subprocessors.* Provider's subprocessors are listed in Annex B. Provider shall give thirty (30) days' notice before adding or replacing a subprocessor; Client may object on reasonable data-protection grounds and the parties shall in good faith consider alternative arrangements.

## 12. Representations & warranties

This section sets out the legal warranties each party makes — including the Provider Services warranty. **Dual-perspective.**

12.1 *Mutual.* Each party represents and warrants that: (a) it is duly organised, validly existing, and in good standing under the laws of its {{State of Formation}}; (b) it has full corporate power and authority to execute and perform this Agreement; (c) execution and performance do not violate any law, regulation, or contract binding on it; and (d) it shall comply with all laws applicable to its performance, including export-control, anti-bribery, and sanctions laws.

12.2 *Provider — Services warranty.* Provider warrants that the Services will be performed in a professional and workmanlike manner consistent with industry standards for similar services, by suitably qualified personnel, free from material defects in workmanship for the warranty period stated in the SOW (default ninety (90) days from acceptance of the relevant Deliverable). Provider's sole obligation, and Client's sole remedy, for breach of this warranty is for Provider to re-perform the affected Services or, at Provider's election, refund the fees paid for the affected Services if re-performance is impracticable.

12.3 *Provider — IP warranty.* Provider warrants that the Foreground IP and Provider Background IP delivered or licensed under this Agreement do not, as of the date of delivery, infringe or misappropriate any third-party patent, copyright, trade secret, or trademark in {{Primary Performance State}}, and that Provider has the right to grant the assignments and licences in §9.

12.4 *Provider — open-source warranty.* Provider warrants that no Foreground IP incorporates open-source components inconsistent with §9.7 and the SOW.

12.5 *Provider — compliance warranty.* Provider warrants that it has not been debarred, suspended, or excluded from any federal procurement programme (SAM.gov), and is not on any OFAC-administered sanctions list.

12.6 *Disclaimer.* EXCEPT FOR THE EXPRESS WARRANTIES IN THIS SECTION, EACH PARTY DISCLAIMS ALL OTHER WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE, AND NON-INFRINGEMENT, AND ANY WARRANTIES ARISING OUT OF COURSE OF DEALING OR USAGE OF TRADE.

12.7 *Dual-perspective triple — warranties.*

- *Client-favorable.* 12-month workmanship warranty; IP warranty extends to all jurisdictions in which Client operates; Provider warrants Deliverables will materially conform to the SOW description for 12 months; warranty remedies are non-exclusive and additional to other remedies.
- *Provider-favorable.* 30-day workmanship warranty; IP warranty limited to US patents and copyrights and excluding trademark and trade-dress claims; warranty void if Client modifies Deliverables; sole remedy is re-performance with no refund; no warranty for Beta Deliverables.
- *Market-standard.* 90-day workmanship warranty; IP warranty for {{Primary Performance State}} and the United States; sole remedy is re-performance or refund (Provider's election if re-performance impracticable); IP warranty excludes Client modifications and combinations not made by Provider; no warranty for evaluation, alpha, or beta material.

## 13. Indemnification

This section sets out the indemnities each party gives, with carve-outs and process. **Dual-perspective.**

13.1 *Provider IP indemnity.* Provider shall defend, indemnify, and hold harmless Client and its Affiliates, officers, directors, employees, and agents from any third-party claim alleging that Foreground IP, or Provider Background IP delivered under this Agreement, infringes a US patent issued or copyright registered as of the delivery date, or misappropriates a trade secret, and shall pay damages and reasonable attorneys' fees finally awarded or settlement amounts agreed by Provider. Excluded are claims arising from: (a) Client modifications; (b) combinations with materials not supplied by Provider where the claim would not have arisen but for the combination; (c) use after Provider has provided a non-infringing replacement; or (d) Client-supplied specifications that necessarily caused the infringement. On an infringement claim, Provider shall, at its option: (i) procure for Client the right to continue use; (ii) modify the item to be non-infringing with substantially equivalent functionality; or (iii) if neither is commercially reasonable, refund fees paid for the affected item less straight-line depreciation over 36 months and accept termination of the affected SOW.

13.2 *Provider compliance indemnity.* Provider shall defend, indemnify, and hold harmless Client from third-party claims arising from: (a) Provider's gross negligence, fraud, or wilful misconduct; (b) bodily injury or tangible property damage caused by Provider personnel; (c) breach by Provider of §10 (Confidentiality) or §11 (Data Protection); (d) classification claims (e.g., misclassification of Provider personnel as independent contractors); or (e) Provider's breach of §19 (export, anti-bribery, sanctions).

13.3 *Client indemnity.* Client shall defend, indemnify, and hold harmless Provider from third-party claims arising from: (a) Client's modification of Deliverables; (b) Client-supplied specifications, materials, or data that infringe third-party rights; (c) Client's use of Deliverables outside the licence granted; or (d) Client's gross negligence, fraud, or wilful misconduct.

13.4 *Indemnification process.* The indemnified party shall: (a) promptly notify the indemnifying party of the claim (failure to notify reduces indemnity only to the extent of resulting prejudice); (b) give the indemnifying party sole control of defence and settlement, except that the indemnifying party may not enter a settlement that admits liability or imposes any non-monetary obligation on the indemnified party without that party's prior written consent (not unreasonably withheld); and (c) provide reasonable assistance at the indemnifying party's expense.

13.5 *Sole remedy.* The remedies in §13.1 are the indemnified party's sole and exclusive remedy for IP infringement claims relating to Foreground IP or Provider Background IP, except that nothing in this Agreement limits a party's right to seek injunctive or other equitable relief in connection with breach of §10 (Confidentiality), §9 (IP), or misuse of trade secrets.

13.6 *Dual-perspective triple — indemnification.*

- *Client-favorable.* Provider IP indemnity covers worldwide patents and copyrights, not just US; broader trigger including any allegation rather than only adjudicated infringement; no carve-out for combinations Provider could have foreseen; Provider also indemnifies for Provider personnel's privacy/security breaches up to 3× the liability cap.
- *Provider-favorable.* IP indemnity limited to US patents adjudicated in litigation through entry of final unappealable judgment; carve-outs for combinations, modifications, and post-replacement use; refund-and-terminate is sole remedy; no compliance indemnity beyond gross negligence; classification indemnity limited to direct fines, no consequential damages.
- *Market-standard.* IP indemnity covers US-issued patents and US-registered copyrights as of delivery date; standard combination, modification, and post-replacement carve-outs; procure-modify-refund three-step ladder; compliance indemnity for gross negligence, willful misconduct, bodily injury, property damage, confidentiality / data-protection breach, and classification.

## 14. Limitation of liability

This section caps each party's exposure under the Agreement, with carve-outs for items that cannot or should not be capped. **Dual-perspective.**

14.1 *Aggregate cap.* Except as set out in §14.3, each party's aggregate liability arising out of or related to this Agreement and every SOW, whether in contract, tort (including negligence), strict liability, statutory, indemnification, or otherwise, shall not exceed the greater of (a) {{Liability Cap Multiplier}} times the fees paid or payable by Client to Provider under the SOW giving rise to the liability in the twelve (12) months preceding the event giving rise to the claim, or (b) {{Liability Cap Floor}}.

14.2 *Excluded damages.* In no event shall either party be liable for any indirect, incidental, special, consequential, exemplary, punitive, or treble damages, or for lost profits, lost revenues, lost data, lost goodwill, or business interruption, however arising, even if advised of the possibility of such damages, except as set out in §14.3.

14.3 *Carve-outs.* The §14.1 cap and §14.2 excluded-damages exclusion do not apply to: (a) indemnification obligations under §13; (b) breach of §10 (sub-capped at 3× the §14.1 cap [VERIFY: confirm sub-cap on Effective Date for the deal]); (c) payment obligations for fees due; (d) gross negligence, wilful misconduct, or fraud; (e) bodily injury or tangible property damage caused by a party's negligence; (f) infringement of a party's IP Rights in violation of this Agreement; (g) violation of export-control or anti-corruption laws (§19); or (h) any liability that cannot be limited under applicable law. For Provider's IP and compliance indemnities (§13.1, §13.2), a separate super-cap equal to 3× the §14.1 cap applies, except that no super-cap applies to (d), (e), (g), or (h).

14.4 *Allocation.* The parties agree the limitations and exclusions in this section reflect the allocation of risk consistent with the fees and form an essential basis of the bargain.

14.5 *Dual-perspective triple — liability cap.*

- *Client-favorable.* Cap is 3× fees paid in 12 months with a {{Liability Cap Floor}} floor; super-cap of 5× for IP, security, privacy, classification, and confidentiality; no exclusion of consequential damages for the carve-outs; data-recovery costs are direct, not consequential; cap measured by aggregate fees over the entire MSA, not the single SOW.
- *Provider-favorable.* Cap is 1× fees paid in 12 months under the affected SOW; flat exclusion of all consequential damages including for indemnification obligations; carve-outs limited to gross negligence and willful misconduct; no super-cap; data-recovery and re-creation costs are excluded as consequential.
- *Market-standard.* Cap is 2× fees paid in 12 months under the affected SOW with a {{Liability Cap Floor}} floor; consequential-damages exclusion subject to standard carve-outs (indemnity, confidentiality with 3× sub-cap, gross negligence, willful misconduct, bodily injury, property damage, IP infringement, export / anti-corruption, payment obligations); super-cap 3× for IP and compliance indemnity.

## 15. Insurance

This section sets the insurance Provider must carry — with US-typical lines, limits, and ACORD requirements.

15.1 *Required coverages.* Provider shall maintain at its own cost, throughout the Term and any tail period required for claims-made policies, insurance with carriers rated A- VIII or better by AM Best, with limits no less than:

- Commercial General Liability — {{PL Insurance Minimum}} per occurrence / $2,000,000 aggregate, including products / completed operations and contractual liability;
- Professional Indemnity / Errors & Omissions — {{PI Insurance Minimum}} per claim and aggregate (claims-made acceptable, with two-year tail);
- Cyber Liability / Tech E&O — {{Cyber Insurance Minimum}} per claim and aggregate, covering first-party and third-party loss including notification costs, regulatory defence, and PCI fines where applicable;
- Workers' Compensation — statutory minimum required by the law of {{Primary Performance State}} (and any other state in which Provider personnel perform Services), and Employer's Liability — {{WC Insurance Minimum}} per accident / per disease / per disease aggregate;
- Commercial Auto Liability — $1,000,000 combined single limit, where Provider personnel use a vehicle for Services; and
- Excess / Umbrella — as needed to meet the limits above.

15.2 *Additional-insured / waiver-of-subrogation.* On Client's request, Provider's CGL and Auto policies shall name Client and its Affiliates as additional insureds with respect to liability arising out of Provider's performance, and Provider's policies shall be primary and non-contributory and shall include a waiver of subrogation in favour of Client where commercially available.

15.3 *Certificates.* Provider shall furnish ACORD certificates of insurance evidencing the coverages above (a) before commencing Services under the first SOW; (b) at each renewal; and (c) on Client's reasonable request. Provider shall give Client thirty (30) days' written notice of cancellation or material reduction, except in the case of cancellation for non-payment of premium (ten (10) days' notice).

15.4 *Carrier and form changes.* Material changes in carrier, retention, or coverage shall be communicated in advance. Self-insurance is acceptable only with Client's prior written consent.

15.5 *No limitation.* Insurance limits do not limit Provider's contractual liability under §13 or §14.

## 16. Term & termination

This section sets the Term and the parties' termination rights — convenience and for-cause — and survival. **Dual-perspective.**

16.1 *Term.* This Agreement starts on the Effective Date and continues for an Initial Term of {{Initial Term Length}}, then auto-renews for successive {{Renewal Term Length}} periods unless either party gives written notice of non-renewal at least {{Termination Notice Window}} before the end of the then-current term. Each SOW has its own term as set out in the SOW.

16.2 *Termination for convenience.* Either party may terminate this Agreement (and any SOW that is not subject to its own non-cancellable commitment) for convenience on {{Termination Notice Window}} written notice. If Client terminates a SOW for convenience, Client shall pay {{Convenience Termination Fee}} in addition to fees and reimbursable expenses accrued through the effective date of termination.

16.3 *Termination for cause.* Either party may terminate this Agreement or any SOW for material breach by the other on written notice if the breach is not cured within {{Cure Period}} after written notice of breach reasonably identifying the breach. Failure to pay undisputed amounts when due is a material breach not subject to cure beyond ten (10) Business Days after notice.

16.4 *Termination for insolvency.* Either party may terminate this Agreement immediately on written notice if the other (a) becomes insolvent or unable to pay its debts as they become due; (b) makes a general assignment for the benefit of creditors; (c) has a receiver, trustee, or similar officer appointed for it; (d) commences or has commenced against it a case under the Bankruptcy Code that is not dismissed within sixty (60) days; or (e) ceases to do business as a going concern.

16.5 *Termination for change of control.* *OPTIONAL.* Client may terminate this Agreement on thirty (30) days' written notice if Provider undergoes a change of control to a competitor of Client or to an entity on the OFAC SDN List.

16.6 *Effect of termination.* On expiry or termination: (a) all licences granted under this Agreement except those expressly designated as perpetual end; (b) accrued payment obligations remain payable; (c) §17 transition obligations apply; and (d) the survival provisions in §16.7 govern.

16.7 *Survival.* The following sections survive expiry or termination: §1 (only as the summary affects interpretation), §2 (Definitions), §5 (Fees, to the extent of accrued amounts), §9 (IP), §10 (Confidentiality), §11.4 (Incident notification, for incidents occurring during the Term and discovered after), §12 (only existing warranty claims), §13 (Indemnification), §14 (Limitation of liability), §16.6, §16.7, §17 (Transition), §18 (Dispute resolution), §19 (General provisions, to the extent applicable to surviving rights and obligations).

16.8 *Dual-perspective triple — termination.*

- *Client-favorable.* Convenience termination on 30 days' notice with no termination fee; for-cause cure period of 15 days; immediate termination for any breach of §10, §11, or §19; Client retains licence to all Foreground IP delivered through termination date plus a 90-day continuation right at SOW rates regardless of cause.
- *Provider-favorable.* Convenience termination only with 90 days' notice and a termination fee equal to 90 days of fees plus unrecovered hard costs; for-cause cure period of 60 days; on termination Client's licence to Foreground IP terminates with respect to anything not yet paid for; Provider may suspend (not terminate) for any past-due undisputed amount after 15 days.
- *Market-standard.* Convenience termination on 60 days' notice with a fee equal to 30 days of fees plus unrecovered hard costs; for-cause cure period of 30 days (10 Business Days for non-payment); Foreground IP licences perpetual for materials paid for; survival as drafted in §16.7.

## 17. Transition assistance & wind-down

This section covers what happens between notice of termination and final hand-over. **Dual-perspective.**

17.1 *Transition services.* On any termination or expiry, Provider shall, on Client's written request, provide reasonable transition assistance for up to {{Transition Period Length}} after the effective date of termination, at SOW rates and on the terms of this Agreement, to facilitate orderly transition of the Services to Client or to a successor provider. Transition assistance includes knowledge transfer, run-book hand-over, return of Client data and materials, support for parallel operation, and reasonable cooperation with the successor.

17.2 *Termination for cause by Client.* If Client terminates for Provider's uncured material breach, transition assistance is provided at fifty percent (50 %) of the SOW rate during the transition period.

17.3 *Termination for cause by Provider.* If Provider terminates for Client's uncured material breach (including non-payment), Provider's obligation to provide transition assistance is conditioned on Client paying transition fees in advance and bringing all undisputed amounts current.

17.4 *Return / destruction.* Within thirty (30) days after the end of the transition period (or, if no transition is requested, within thirty (30) days of termination), each party shall return or destroy the other's Confidential Information consistent with §10.8.

17.5 *Transition plan.* Where the SOW value exceeds {{Convenience Termination Fee}} in any twelve-month period, the parties shall maintain a written transition plan as part of the SOW, updated annually.

17.6 *Dual-perspective triple — transition.*

- *Client-favorable.* Transition period up to 180 days at SOW rates regardless of cause; Provider must return all Client data and Foreground IP within 7 days; Provider must cooperate with up to two parallel successor providers; in cause-termination by Client, transition is at 25 % of SOW rate.
- *Provider-favorable.* Transition limited to 30 days; Provider may decline transition assistance to a competitor; Client must pre-pay transition fees in full; data-return SLA is 60 days, not 7; cause-termination by Provider triggers no transition obligation absent cure.
- *Market-standard.* Transition up to 90 days at SOW rates; reduced to 50 % rate if Client terminates for cause; pre-payment by Client if Provider terminates for cause; data return within 30 days of end of transition; transition plan required for material SOWs.

## 18. Dispute resolution & governing law

This section sets the governing law, the mandatory mediation step, the arbitration framework, the IP / confidentiality court carve-out, and the jury-trial / class-action waivers.

18.1 *Governing law.* This Agreement is governed by the substantive laws of {{Governing Law}} (default Delaware), without regard to its conflict-of-laws principles. The UN Convention on Contracts for the International Sale of Goods does not apply.

18.2 *Negotiation and mediation.* The parties shall first attempt to resolve any dispute by good-faith negotiation between authorised business representatives (escalation within fifteen (15) Business Days). If negotiation fails, the parties shall submit the dispute to non-binding mediation administered by {{Mediation Provider}} (default AAA Commercial Mediation) in {{Venue}}, with the parties sharing mediator costs equally. Mediation is a condition precedent to arbitration or litigation, except for claims qualifying under §18.5.

18.3 *Arbitration.* Any dispute not resolved by mediation shall be finally resolved by binding arbitration under the {{Arbitration Forum}} rules in effect on the date arbitration is commenced (default AAA Commercial Arbitration Rules; alternative JAMS Comprehensive Arbitration Rules), by one (1) arbitrator (or three (3) arbitrators if the amount in controversy exceeds $1,000,000), seated in {{Arbitration Seat}} (default Wilmington, Delaware), with the proceeding governed by the Federal Arbitration Act (9 USC §§1 et seq.). Judgment on the award may be entered in any court of competent jurisdiction.

18.4 *Discovery in arbitration.* Discovery is governed by the {{Arbitration Forum}} rules and limited to what the arbitrator considers necessary. Each party bears its own attorneys' fees and costs unless the arbitrator awards otherwise; the arbitrator may award fees and costs to the prevailing party in cases of frivolous claims or bad-faith conduct.

18.5 *IP / confidentiality / injunctive-relief carve-out.* Notwithstanding §18.3, either party may seek temporary, preliminary, or permanent injunctive or other equitable relief (and ancillary monetary relief) from a court of competent jurisdiction to protect its IP Rights, Confidential Information, or trade secrets, or to enforce §10 or §11. Venue for such court actions is exclusive to the Court of Chancery of {{Governing Law}} (Delaware) or, if the Court of Chancery lacks jurisdiction, the federal and state courts located in {{Venue}} (default New Castle County, Delaware; New York alternative — Commercial Division of the Supreme Court of the State of New York, County of New York), and each party irrevocably submits to that jurisdiction and waives any objection on the basis of venue or forum non conveniens.

18.6 *Jury-trial waiver.* TO THE FULLEST EXTENT PERMITTED BY LAW, EACH PARTY KNOWINGLY, VOLUNTARILY, AND INTENTIONALLY WAIVES ITS RIGHT TO A TRIAL BY JURY IN ANY ACTION OR PROCEEDING ARISING OUT OF OR RELATED TO THIS AGREEMENT.

18.7 *Class-action waiver.* TO THE FULLEST EXTENT PERMITTED BY LAW, EACH PARTY WAIVES ITS RIGHT TO PARTICIPATE IN A CLASS, COLLECTIVE, REPRESENTATIVE, OR PRIVATE-ATTORNEY-GENERAL ACTION AGAINST THE OTHER. THE ARBITRATOR MAY NOT CONSOLIDATE OR JOIN MORE THAN ONE PERSON'S CLAIMS WITHOUT THE WRITTEN CONSENT OF THE PARTIES.

18.8 *Limitation period.* Any claim arising out of or related to this Agreement must be commenced within two (2) years of the date the cause of action accrued, except for IP infringement, unpaid amounts, or claims that cannot be limited by contract under applicable law.

18.9 *Confidentiality of dispute proceedings.* The existence and contents of any negotiation, mediation, or arbitration are Confidential Information.

## 19. General provisions & signature block

This section covers the boilerplate plus federal/state flow-downs, export, anti-corruption, and notice/signature.

19.1 *Notices.* Notices must be in writing and delivered to {{Provider Notice Email}} or {{Client Notice Email}} (with a courtesy copy by overnight courier to the registered address). Notices given by email are effective on confirmed delivery.

19.2 *Assignment.* Neither party may assign this Agreement without the other's prior written consent (not unreasonably withheld), except that either party may assign on written notice to (a) an Affiliate or (b) the surviving entity in a merger, change of control, or sale of substantially all assets. Any assignment in violation of this section is void.

19.3 *Entire agreement; amendment.* This Agreement, together with the SOWs, Order Forms, Change Orders, and annexes, is the entire agreement between the parties on its subject matter and supersedes all prior or contemporaneous agreements, whether oral or written, on the subject. Amendments must be in writing signed by authorised representatives of both parties.

19.4 *Waiver and severability.* No waiver is effective unless in writing. A failure to enforce any right is not a waiver of that right or any other. If any provision is held unenforceable, it shall be reformed to the minimum extent necessary, and the rest of the Agreement remains in force.

19.5 *Force majeure.* Neither party is liable for delay or non-performance to the extent caused by an event beyond its reasonable control (including acts of God, war, terrorism, pandemic-related government order, civil disturbance, internet failure unaffecting general internet access, or labour dispute not involving its own workforce), provided the affected party gives prompt notice and uses reasonable efforts to mitigate. Force majeure does not excuse payment of amounts already due.

19.6 *Government Contracts and federal flow-downs.* If Services support a Government Contract, the parties incorporate the FAR / DFARS clauses required by the prime, including (as applicable): FAR 52.203-13, 52.215-2, 52.222-26, 52.222-35/36/37, 52.225-13, 52.227-14, and where applicable DFARS 252.204-7012, 252.227-7013, 252.227-7014. Affirmative-action obligations under §503 of the Rehabilitation Act and §4212 of VEVRAA are flow-down requirements [VERIFY: applicable FAR / DFARS clause set on Effective Date].

19.7 *Anti-corruption.* Each party shall comply with the US Foreign Corrupt Practices Act (FCPA, 15 USC §§78dd-1 et seq.), the UK Bribery Act 2010 to the extent applicable, and analogous state-level public-corruption and bribery laws. Neither party shall, directly or indirectly, offer, give, or accept anything of value to influence official action.

19.8 *Export and sanctions.* Each party shall comply with applicable US export-control and sanctions laws, including the Export Administration Regulations (EAR, 15 CFR §§730–774), the International Traffic in Arms Regulations (ITAR, 22 CFR §§120–130) where applicable, and OFAC-administered sanctions. Neither party shall transfer Deliverables or Confidential Information to any restricted destination, end-user, or end-use without required authorisations. Provider represents it is not on any prohibited-party list. {{ITAR / EAR Applicability}}.

19.9 *California Transparency in Supply Chains Act and Modern Slavery Act.* Each party that meets the applicability thresholds of the California Transparency in Supply Chains Act of 2010 (Cal. Civ. Code §1714.43), the UK Modern Slavery Act 2015 §54, or analogous laws, shall comply with the disclosure obligations of those laws as applied to its supply chain. Provider warrants that it does not engage forced or compulsory labour or human trafficking in the performance of the Services [VERIFY: applicability thresholds on Effective Date].

19.10 *Buy America / domestic preferences.* *OPTIONAL — only if Government Contract Clauses identify a domestic-preference clause.* The parties shall comply with Buy American Act, Trade Agreements Act, and Berry Amendment requirements as flowed down from the prime.

19.11 *DMCA / Section 230 carve-out.* *OPTIONAL — only if Provider hosts user-generated content as part of the Services.* Provider shall designate a DMCA agent under 17 USC §512(c)(2) and maintain a notice-and-takedown procedure consistent with 17 USC §512. The parties acknowledge §230 of the Communications Decency Act (47 USC §230) provides separate protections for interactive computer services, which neither party waives.

19.12 *Counterparts and electronic signature.* This Agreement may be executed in counterparts, each an original and together one instrument. Electronic signatures (including DocuSign and similar) are valid under the federal ESIGN Act (15 USC §§7001 et seq.) and the Uniform Electronic Transactions Act as adopted in the relevant state.

19.13 *Headings and construction.* Headings are for convenience only. References to statutes include amendments and successors. No rule of construction operates against the drafter.

19.14 *Independent legal advice.* Each party has had the opportunity to obtain independent legal advice on this Agreement.

### Signature block

| | **{{Provider Legal Name}}** | **{{Client Legal Name}}** |
|---|---|---|
| Signature | ____________________________ | ____________________________ |
| Name | {{Provider Signatory Name}} | {{Client Signatory Name}} |
| Title | {{Provider Signatory Title}} | {{Client Signatory Title}} |
| Date | _____________ | _____________ |
| Address | {{Provider Address}} | {{Client Address}} |
| State of formation | {{Provider State of Formation}} | {{Client State of Formation}} |
| Notice email | {{Provider Notice Email}} | {{Client Notice Email}} |

---

## Annex A — Statement of Work (SOW) template

This is a short-form SOW shell. The full SOW pack lives at `legalcode-sow`; that pack should be used for any SOW of material value.

**SOW No.:** ______ **SOW Effective Date:** ______ **MSA Reference:** This SOW is governed by the {{MSA Title}} between {{Provider Legal Name}} and {{Client Legal Name}} dated {{MSA Effective Date}}.

A.1 *Description of Services.* [Narrative description.]

A.2 *Deliverables.* [Itemised list with description, format, and acceptance criteria.]

A.3 *Schedule and Milestones.* [Table of milestones with dates and dependencies.]

A.4 *Fees.* [Fee structure — fixed-fee / T&M / milestone — with rate-card if T&M.]

A.5 *Expenses.* [Expense budget and approval rules.]

A.6 *Acceptance.* [Acceptance period and any deviation from §8 default.]

A.7 *Key Personnel.* [Named individuals and minimum allocation %.]

A.8 *Approved Subcontractors.* [Named, or "none".]

A.9 *Service-level commitments.* *OPTIONAL.* [SLAs, response times, uptime, with credits.]

A.10 *Assumptions and dependencies.* [List Provider assumptions and Client dependencies.]

A.11 *Warranty period.* [If different from §12.2 default.]

A.12 *Termination-for-convenience fee.* [If different from §16.2 default.]

A.13 *Government Contract flow-down.* [If applicable, identify prime and flowed-down clauses.]

A.14 *Sectoral overlays.* [HIPAA / FERPA / GLBA / PCI / state privacy, where applicable.]

**SOW signature.** Signed by authorised representatives of each party.

---

## Annex B — Approved subcontractors & key personnel

| Role | Name / Entity | Country / State | Permitted scope | Approved on |
|------|--------------|-----------------|-----------------|-------------|
| Subcontractor | | | | |
| Key Personnel | | | | |
| Subprocessor (Personal Information) | | | | |

A change to this Annex is a Change Order under §6.

---

## Annex C — Service standards & acceptance criteria framework

C.1 *Default acceptance criteria.* A Deliverable conforms when it: (a) materially performs the functions described in the SOW; (b) is delivered in the required format and medium; (c) is free from material defects in workmanship; and (d) where software, runs without material error in the supported environment.

C.2 *Material vs. immaterial defects.* A defect is "material" if it: (i) prevents Client from using the Deliverable for its intended purpose; (ii) requires more than thirty (30) minutes of administrator-level work-around per occurrence; or (iii) creates a security, privacy, or regulatory exposure.

C.3 *Severity tiers.* Severity-1 (production down, no work-around) — Provider response within four (4) hours, fix or work-around within one (1) Business Day; Severity-2 (degraded; work-around exists) — response within eight (8) hours, fix within five (5) Business Days; Severity-3 (cosmetic; minor) — response within two (2) Business Days, fix in next maintenance window.

C.4 *Test evidence.* Provider shall preserve test evidence (test plans, test results, defect logs) for the warranty period and provide on Client's request.

C.5 *Acceptance form.* Acceptance is in writing using the form supplied with the SOW or, if none, by email from {{Client Notice Email}} to {{Provider Notice Email}}.

---

## Appendix 1 — Merge fields used

The merge fields used in this US variant are listed at the top of this document (under "Merge fields"). Search-and-replace each field before signature. Common merge fields are documented in the pack `README.md`.

## Appendix 2 — Authoritative references

- 17 USC §101 (definition of "work made for hire") — public domain.
- 17 USC §201(b) (works made for hire — ownership).
- 18 USC §1833(b) (Defend Trade Secrets Act whistleblower immunity notice).
- UCC Art. 2 §§2-209, 2-508, 2-513, 2-606, 2-607, 2-719 (cited as analog to services).
- IRS twenty-factor / common-law test for independent-contractor classification — Rev. Rul. 87-41; current guidance at IRS.gov.
- US Department of Labor, FLSA exempt-status framework, 29 CFR §541.
- California Labor Code §§2775 (AB-5 ABC test), 2870 (employee inventions); New Jersey N.J. Stat. §43:21-19(i)(6); Massachusetts Gen. Laws ch. 149 §148B; Illinois HB1063.
- California Civil Code §§1798.100–1798.199.100 (CCPA / CPRA); §1798.82 (data-breach notification).
- Defend Trade Secrets Act, 18 USC §§1831–1839.
- FAR 52.227-14 (Rights in Data — General); DFARS 252.227-7013 / 7014.
- FAR 52.222-26, 52.222-35, 52.222-36, 52.222-37 (EEO, VEVRAA, §503).
- Federal Arbitration Act, 9 USC §§1 et seq.
- Federal ESIGN Act, 15 USC §§7001 et seq.
- Foreign Corrupt Practices Act, 15 USC §§78dd-1 et seq.
- Export Administration Regulations, 15 CFR §§730–774; ITAR, 22 CFR §§120–130.
- NIST Cybersecurity Framework v2.0; NIST SP 800-171.
- AAA Commercial Arbitration Rules; JAMS Comprehensive Arbitration Rules.
- Bonterms Professional Services Agreement (PSA) v1.2 — CC0.
- Common Paper Standard Services Agreement and SOW — CC-BY-4.0.

## Appendix 3 — Not legal advice

This template is provided by Fordæmi ehf. (Legalcode) under the MIT licence, without warranty of any kind. It is a starting point for drafting, not legal advice. The accuracy and applicability of every clause depends on the specific facts of the engagement, the jurisdictions involved, and the parties' negotiating posture. Before signing, have the resulting document reviewed by qualified counsel admitted in the relevant jurisdiction. Where a clause is flagged `[VERIFY: …]`, confirm the cited rule, threshold, or list against the version in force on the date of execution. Where the engagement involves regulated data (PHI, education records, financial-services data, controlled unclassified information, ITAR-controlled technical data), consult sectoral counsel; the overlays in §11 are pointers, not full implementations.
