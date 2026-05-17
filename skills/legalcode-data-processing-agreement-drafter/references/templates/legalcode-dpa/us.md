---
title: Data Processing Agreement — United States (CCPA/CPRA + multi-state Service Provider Exhibit)
jurisdictions: [us-ca, us-co, us-va, us-ct, us-ut, us-tx, us-or]
statutes: [CCPA, CPRA, CPA, VCDPA, CTDPA, UCPA, TDPSA, OCPA]
license: MIT
last_updated: 2026-04-28
---

# Data Processing Agreement — United States

**Service Provider / Contractor Exhibit to the {{MSA Title}}**

This Exhibit (the "**DPA**") is entered into by and between **{{Controller Legal Name}}** ("**{{Controller Short Name}}**" or the "**Business**"), and **{{Processor Legal Name}}** ("**{{Processor Short Name}}**" or the "**{{Service Provider Designation}}**"). It is incorporated into and forms part of the {{MSA Title}} dated {{MSA Effective Date}} (the "**Agreement**") between the parties. It is effective on {{Effective Date}}.

This DPA is a Service Provider Exhibit (or Contractor Exhibit, as elected by the parties under §5) under the California Consumer Privacy Act of 2018, as amended by the California Privacy Rights Act of 2020 (collectively the "**CCPA**"), together with the parallel statutes enumerated in §20 below. The United States has no single, federal GDPR-equivalent processor/controller framework; this Exhibit therefore uses Business / Service Provider / Contractor / Third Party terminology drawn from California law and applies the same operative obligations to processing governed by the other state laws listed in §20, with the state-specific deviations expressly noted.

**Merge fields used in this variant** are listed in the appendix at the end of this document. Standard fields shared with sibling templates are listed in the pack-level README. US-specific fields include `{{Service Provider Designation}}`, `{{Business Purposes}}`, `{{State Breach Notice Statutes}}`, `{{Authorized Agent Submission URL}}`, `{{DSAR Submission URL}}`, and `{{Do Not Sell URL}}`.

---

## 1. Plain-language summary

In plain English: {{Controller Short Name}} is the Business that decides why and how personal information about its consumers, employees, and other individuals is processed. {{Processor Short Name}} is the {{Service Provider Designation}} that handles personal information on the Business's behalf to deliver {{Service Name}}. This DPA sets out the terms that California's CCPA and the parallel state laws in §20 require: what the {{Service Provider Designation}} can and cannot do with personal information, how it must protect it, what to do if something goes wrong, how it must help the Business answer consumer requests, and what happens at the end of the engagement. The first sentence of each later section restates the rule in plain English. Defined terms are capitalized and explained in §2. Where this Exhibit and the Agreement disagree on privacy, this Exhibit wins (see §19). This is a contract, not legal advice — see the closing paragraph.

---

## 2. Definitions

Defined terms used here carry the meaning given by the CCPA, the cited California statutes, and the parallel state laws listed in §20, except where this DPA expressly says otherwise.

For purposes of this DPA:

- "**Business**" — Cal. Civ. Code §1798.140(d): an entity that determines the purposes and means of the Processing of Personal Information and meets a §1798.140(d)(1) threshold.
- "**Service Provider**" — Cal. Civ. Code §1798.140(ag): a person that Processes Personal Information on behalf of a Business under a written contract meeting §1798.140(ag)(1)(A)–(D). Used where the recipient performs a service for the Business itself (hosting, analytics, support tooling).
- "**Contractor**" — Cal. Civ. Code §1798.140(j): a person to whom a Business makes Personal Information available under a written contract with materially the same elements as a Service Provider contract, including a certification of understanding and compliance.
- "**Third Party**" — Cal. Civ. Code §1798.140(ai): a person that is neither the collecting Business nor a Service Provider/Contractor with a §1798.140(ag) or §1798.140(j) contract in place. Disclosing PI to a Third Party is a Sale or Sharing unless an exception applies.
- "**Personal Information**" or "**PI**" — Cal. Civ. Code §1798.140(v): information that identifies, relates to, or could reasonably be linked with a Consumer or household. For non-California state-law processing, the equivalent statutory term ("personal data") applies.
- "**Sensitive Personal Information**" or "**Sensitive PI**" — Cal. Civ. Code §1798.140(ae): SSNs, driver's-license/state-ID, financial account, precise geolocation, racial/ethnic origin, religious beliefs, union membership, mail/email/text contents, genetic data, biometric data used for unique identification, health, sex life, and sexual orientation information.
- "**Consumer**" — Cal. Civ. Code §1798.140(i): a California-resident natural person, including in B2B and employment contexts where applicable. For non-California state-law processing, the equivalent natural person under that state's law.
- "**Sale**" — Cal. Civ. Code §1798.140(ad): communicating PI to a Third Party for monetary or other valuable consideration; §1798.140(ad)(2) exceptions preserved.
- "**Sharing**" — Cal. Civ. Code §1798.140(ah): communicating PI to a Third Party for Cross-Context Behavioral Advertising, with or without consideration.
- "**Cross-Context Behavioral Advertising**" — Cal. Civ. Code §1798.140(k): targeting advertising based on a Consumer's activity across services other than the one with which the Consumer intentionally interacts.
- "**Process**", "**Processing**" — any operation performed on PI, automated or not, including collection, storage, use, disclosure, alignment, combination, erasure, or destruction.
- "**Business Purpose**" — Cal. Civ. Code §1798.140(e): use of PI for an operational purpose reasonably necessary and proportionate to the purpose for which it was collected or a compatible purpose.
- "**Sub-processor**" — any Service Provider, Contractor, or other person engaged by {{Processor Short Name}} to Process PI on the Business's behalf under this DPA.
- "**Security Incident**" — a "breach of the security of the system" within Cal. Civ. Code §1798.82(g) or the equivalent under any §20 state law, including any unauthorized acquisition of PI of the categories enumerated in §1798.81.5(d) and §1798.150(a)(1).
- "**Universal Opt-Out Signal**" or "**GPC**" — a Consumer-elected technical signal (e.g., Global Privacy Control) that must be honored as a Sale/Sharing opt-out under California regulations and the §20 state laws from each state's effective date.
- "**Authorized Agent**" — a natural person or registered entity authorized by a Consumer to submit rights requests under §1798.135 and Cal. Code Regs. tit. 11 §7063.
- "**Verifiable Consumer Request**" — Cal. Civ. Code §1798.140(aj).
- "**ADMT**" — automated decision-making technology under the CPPA's ADMT Regulations, Cal. Code Regs. tit. 11 §§ 7150–7158 and §§ 7200–7222 `[VERIFY]`.
- "**Cybersecurity Audit Regulations**" — Cal. Code Regs. tit. 11 §§ 7120–7129 `[VERIFY]`.
- "**Reasonable Security**" — reasonable security procedures and practices appropriate to the nature of the PI within Cal. Civ. Code §1798.81.5 and the equivalent §20 state-law standards.

Defined terms in the singular include the plural and vice versa; "**including**" means "including without limitation"; statutory references refer to the statute as amended and to its successor provisions.

---

## 3. Subject matter, duration, nature & purpose of processing

In plain English: this section says what the Processing is, how long it lasts, and why {{Processor Short Name}} is doing it.

- **Subject matter.** Processing of Personal Information by {{Processor Short Name}} solely as required to provide {{Service Name}} (the "**Services**") to {{Controller Short Name}}.
- **Duration.** This DPA applies for the term of the Agreement and survives termination for so long as {{Processor Short Name}} retains any Personal Information of {{Controller Short Name}}, until the deletion or return obligations in §16 are satisfied.
- **Nature.** The Processing operations consist of those operations described in **Annex 1** and any further operations strictly necessary to deliver the Services, comply with law, or carry out the Business's documented instructions under §6.
- **Purposes.** The permitted Business Purposes are those listed in Annex 1 under "**{{Business Purposes}}**" and those operational uses set out in §1798.140(e). {{Processor Short Name}} shall not Process Personal Information for any other purpose, and shall not retain, use, or disclose Personal Information outside of the direct business relationship between the parties (see §5).

---

## 4. Categories of data subjects and types of personal information

In plain English: this section lists who the Personal Information is about and what kinds of Personal Information are involved.

The categories of Consumers and other natural persons whose Personal Information may be Processed under this DPA, and the categories and types of Personal Information involved, are set out in **Annex 1**. {{Processor Short Name}} acknowledges that Annex 1 expressly identifies whether Sensitive Personal Information is in scope. Where Sensitive PI is in scope, the obligations in §1798.121 (right to limit use and disclosure of Sensitive PI) apply and {{Processor Short Name}} agrees to honor any Consumer election to limit such use and disclosure as relayed by the Business under §10.

If at any point during the engagement {{Controller Short Name}} contemplates introducing a new category of Consumer or a new type of Personal Information not described in Annex 1, the parties shall amend Annex 1 in writing before the new processing begins.

---

## 5. Roles & responsibilities

In plain English: this section says which party is the Business and which is the Service Provider or Contractor, and it pins down the four operative restrictions that California law requires the contract to contain.

### 5.1 Designation of roles

For all Personal Information Processed under this DPA:

- {{Controller Short Name}} is the **Business** within the meaning of Cal. Civ. Code §1798.140(d).
- {{Processor Short Name}} is the **{{Service Provider Designation}}** — that is, either a Service Provider within the meaning of §1798.140(ag) or a Contractor within the meaning of §1798.140(j), as elected in Annex 1.
- Neither party is the other's "**Third Party**" within the meaning of §1798.140(ai), and the disclosure of Personal Information from {{Controller Short Name}} to {{Processor Short Name}} under the Agreement is therefore not a Sale or Sharing.

### 5.2 Service Provider operative restrictions (§1798.140(ag)(1)(A)–(D))

Where {{Processor Short Name}} is the **Service Provider**, the following sub-clauses satisfy the §1798.140(ag)(1)(A)–(D) elements:

**(A) Limit processing to specified Business Purposes.** Process PI only for the limited and specified Business Purposes in Annex 1 under "**{{Business Purposes}}**" and as further restricted by the Business's instructions under §6.

**(B) No Sale or Sharing.** Not Sell PI and not Share PI for Cross-Context Behavioral Advertising, including for training generative-AI or similar models for {{Processor Short Name}}'s benefit, unless the Business has expressly authorized the use in writing as a Business Purpose.

**(C) No retention, use, or disclosure outside the direct business relationship.** Not retain, use, or disclose PI (i) for any purpose other than the Business Purposes in Annex 1, (ii) outside the direct business relationship, or (iii) for any commercial purpose other than those specified, including by combining or updating PI received from the Business with PI from another source. Possession is not, by itself, permission to use.

**(D) No combining with other-source PI except as permitted.** Not combine PI received from {{Controller Short Name}} with PI from another source, except as permitted by Cal. Civ. Code §1798.145(a)(1)–(7) (legal compliance, cooperation with public authorities, defense of legal claims, and similar uses).

{{Processor Short Name}} certifies that it understands and will comply with restrictions (A)–(D). This certification is given in satisfaction of §1798.140(ag)(2).

### 5.3 Contractor operative restrictions (§1798.140(j)) — alternative designation

OPTIONAL — only if the parties elect "Contractor" in Annex 1.

Where {{Processor Short Name}} is a **Contractor**, it accepts the same restrictions (A)–(D), reflecting §1798.140(j): it (i) acknowledges that PI was made available by the Business for a specified Business Purpose, (ii) certifies understanding and compliance, (iii) shall not Sell or Share PI, (iv) shall not retain, use, or disclose PI outside the direct business relationship, and (v) shall not combine PI from the Business with PI from another source except as permitted by §1798.145(a)(1)–(7). The Contractor and Service Provider obligations are materially the same; the label reflects the contractual posture.

### 5.4 Third Party — not applicable

The parties do not intend for {{Processor Short Name}} to act as a Third Party. If circumstances would convert a disclosure into a Sale or Sharing, the parties shall pause the affected Processing and consult in good faith before resumption.

---

## 6. Documented processing instructions

In plain English: the Agreement and this DPA are the {{Service Provider Designation}}'s instructions. If anything changes, the Business gives the new instruction in writing.

### 6.1 Source of instructions

{{Processor Short Name}} shall Process PI only on documented instructions from {{Controller Short Name}}. The Agreement, this DPA (including Annex 1), and any written instructions issued by {{Controller Short Name}} (including support tickets, control-plane configuration, and admin actions in {{Service Name}}) together constitute the Business's documented instructions. Ongoing administration of {{Service Name}} is itself a continuing instruction.

### 6.2 Instructions that conflict with law

If {{Processor Short Name}} reasonably believes a specific instruction would violate applicable US federal or state law, it shall promptly inform {{Controller Short Name}} in writing and may suspend that instruction (but not the broader Service) until {{Controller Short Name}} confirms, modifies, or withdraws it.

### 6.3 Notice of inability to comply (§1798.140(ag)(2))

{{Processor Short Name}} shall promptly notify {{Controller Short Name}} in writing if it determines it can no longer meet its obligations under the CCPA, the §20 state laws, or this DPA. {{Controller Short Name}} is then entitled to take reasonable and appropriate steps to stop and remediate the unauthorized use of PI, including (i) requiring deletion, (ii) suspending the affected Processing, (iii) requiring corrective action and verification, and (iv) terminating the Agreement for cause.

### 6.4 Government access requests

If {{Processor Short Name}} receives a legally binding request from a federal, state, local, or foreign governmental authority for PI, it shall, to the extent permitted by law: (i) promptly notify {{Controller Short Name}}; (ii) challenge any overbroad request or one lacking a valid legal basis; (iii) disclose only the minimum PI legally required; and (iv) document each request and disclosure for the §15 audit obligations.

---

## 7. Confidentiality of personnel

In plain English: anyone at {{Processor Short Name}} who touches Personal Information is under a duty of confidentiality and gets only the access they need.

{{Processor Short Name}} shall ensure that all personnel (employees, contingent workers, authorized contractors) who Process PI under this DPA:

(a) are bound by an enforceable written confidentiality obligation that survives termination of engagement;

(b) receive privacy and information-security training at hire and at least annually, addressing §1798.140(ag) restrictions and parallel state-law obligations;

(c) are granted PI access only on a least-privilege, need-to-know basis;

(d) are subject to documented joiner-mover-leaver controls; and

(e) are subject to disciplinary process for breach.

{{Processor Short Name}} shall make summary evidence of (a)–(e) available to {{Controller Short Name}} on reasonable request.

---

## 8. Security measures (TOMs)

In plain English: {{Processor Short Name}} must keep the Personal Information secure, using reasonable controls described in Annex 2.

### 8.1 Reasonable Security standard

{{Processor Short Name}} shall implement and maintain Reasonable Security within Cal. Civ. Code §1798.81.5(b) and the equivalent §20 standards. The TOMs are set out in **Annex 2**, mapped to the CIS Critical Security Controls and the NIST Cybersecurity Framework, and shall be kept current.

### 8.2 Risk-based controls

The TOMs shall address, at minimum: identity and access management; encryption at rest and in transit; secure SDLC and change management; vulnerability management; logging, monitoring, and incident detection; backup and recovery; physical security; sub-processor risk management; and personnel security. {{Processor Short Name}} shall review and update the TOMs to address evolving threats.

### 8.3 Cybersecurity Audit Regulations — when applicable

OPTIONAL — only if {{Controller Short Name}} is, or anticipates becoming, subject to the CPPA Cybersecurity Audit Regulations (Cal. Code Regs. tit. 11 §§ 7120–7129) `[VERIFY]`. If applicable, {{Processor Short Name}} shall (i) cooperate with the annual audit, (ii) provide auditor-relevant evidence of Annex 2 controls, and (iii) reasonably accommodate auditor-led testing.

### 8.4 Sensitive Personal Information

Where Annex 1 indicates Sensitive PI is in scope, {{Processor Short Name}} shall apply enhanced controls including encryption at rest, workload segregation, additional access logging, and reduced retention. Where the CPPA Risk-Assessment Regulations apply, {{Processor Short Name}} shall provide the information needed to complete the assessment.

---

## 9. Sub-processors

In plain English: if {{Processor Short Name}} hires anyone else to handle Personal Information, that other party must follow the same rules and the Business gets to know and to object.

### 9.1 General authorization

{{Controller Short Name}} grants {{Processor Short Name}} general authorization to engage Sub-processors, subject to this §9.

### 9.2 Current Sub-processor list

Current Sub-processors are listed in **Annex 3** and at {{Subprocessor List URL}}, identifying entity, processing location, function, and whether Sensitive PI is involved.

### 9.3 Notice of new or replacement Sub-processors

{{Processor Short Name}} shall give {{Controller Short Name}} at least {{Notification Window}} prior written notice (including via subscription to the maintained list) of any addition or replacement. {{Controller Short Name}} may object within the notice window on reasonable, documented privacy or security grounds.

### 9.4 Resolution of objections

If the parties cannot reach a workaround within thirty (30) days, {{Controller Short Name}} may terminate the affected portion of the Services for cause and receive a pro-rata refund of prepaid fees attributable to the terminated portion.

### 9.5 Flow-down

{{Processor Short Name}} shall execute a written agreement with each Sub-processor imposing obligations no less protective than this DPA, including the §1798.140(ag)(1)(A)–(D) restrictions. {{Processor Short Name}} remains liable for its Sub-processors' acts and omissions.

### 9.6 Sub-processor monitoring

{{Processor Short Name}} shall review each Sub-processor's compliance at least annually and maintain records of that review.

---

## 10. Data subject rights assistance

In plain English: when a Consumer asks the Business to use one of its CCPA rights, the {{Service Provider Designation}} must help.

### 10.1 The eight CCPA/CPRA Consumer rights

{{Processor Short Name}} shall provide reasonable assistance to {{Controller Short Name}} so that {{Controller Short Name}} can respond to Consumer requests asserting any of the following rights:

(a) the right to know what Personal Information has been collected, used, disclosed, Sold, or Shared (Cal. Civ. Code §§1798.100, 1798.110, 1798.115);

(b) the right to delete Personal Information (§1798.105);

(c) the right to correct inaccurate Personal Information (§1798.106);

(d) the right to opt out of Sale or Sharing (§1798.120), including via a Universal Opt-Out Signal honored under Cal. Code Regs. tit. 11 §7025;

(e) the right to limit use and disclosure of Sensitive Personal Information (§1798.121);

(f) the right to data portability (§1798.130(a)(3)(B));

(g) the right against unlawful discrimination or retaliation for exercising privacy rights (§1798.125, including the §1798.125(b) financial-incentive rules); and

(h) the right to designate an Authorized Agent to act on the Consumer's behalf (§1798.135 and Cal. Code Regs. tit. 11 §7063), with submission permitted at {{Authorized Agent Submission URL}} where applicable.

### 10.2 Service Levels

{{Controller Short Name}} has the §1798.130(a)(2) "**45+45 SLA**" — forty-five (45) days to respond, plus a further forty-five (45) days if reasonably necessary. To meet that SLA, {{Processor Short Name}} shall acknowledge requests for assistance within five (5) business days and provide a substantive response (export, deletion confirmation, opt-out evidence) within ten (10) business days, unless otherwise agreed in writing. Opt-out signals received at {{Do Not Sell URL}} or via the Business's admin tooling shall be propagated within fifteen (15) business days under §1798.135(c)(3).

### 10.3 Direct-to-Service-Provider requests

If {{Processor Short Name}} receives a rights request directly, it shall (i) not respond on the merits absent {{Controller Short Name}}'s instruction, (ii) forward the request without undue delay to {{DSAR Submission URL}} or the agreed channel, and (iii) provide reasonably available identity information for verification.

### 10.4 No discrimination

{{Processor Short Name}} shall not act in any way that would cause {{Controller Short Name}} to violate §1798.125, including by degrading service quality for Consumers who exercise rights.

---

## 11. Assistance with controller compliance

In plain English: the {{Service Provider Designation}} helps the Business with the broader compliance work that surrounds Consumer rights — risk assessments, regulator queries, contracts, and the like.

{{Processor Short Name}} shall, considering the nature of the Processing and information available, reasonably assist {{Controller Short Name}} with:

(a) **Risk assessments** under the CPPA Risk-Assessment Regulations and equivalent §20 obligations (high-risk Processing, Sensitive PI, ADMT) `[VERIFY]`;

(b) **Cybersecurity Audits** under Cal. Code Regs. tit. 11 §§ 7120–7129 where applicable `[VERIFY]`;

(c) **ADMT obligations** under Cal. Code Regs. tit. 11 §§ 7150–7158 and §§ 7200–7222 where {{Service Name}} involves ADMT `[VERIFY]`;

(d) **Regulator inquiries** from the California Attorney General, CPPA, Colorado Department of Law, Connecticut Attorney General, Texas Attorney General, Oregon Department of Justice, Utah Division of Consumer Protection, or Virginia Attorney General;

(e) **Privacy notices** by providing details required under §§1798.100, 1798.110, 1798.130, and parallel state-law notice rules;

(f) **Security Incident response** as in §12; and

(g) **Vendor onboarding**, including questionnaires, attestation reports, and due-diligence support under §1798.140(ag) and parallel state-law contract rules.

Demonstrable out-of-pocket costs for (a)–(c) and (g) are recoverable only as expressly agreed in the Agreement; routine cooperation under (d), (e), and (f) is at {{Processor Short Name}}'s expense.

---

## 12. Personal information breach notification

In plain English: if there's a Security Incident, {{Processor Short Name}} tells the Business fast, helps contain it, and supports notice to Consumers and regulators where the law requires it.

### 12.1 Notification SLA

{{Processor Short Name}} shall notify {{Controller Short Name}} of any Security Incident affecting Personal Information without undue delay and in no event later than the SLA elected in Annex 1, which the parties select from the following dual-perspective options:

- **Aggressive (controller-favorable):** within twenty-four (24) hours of becoming aware;
- **Market-standard:** within forty-eight (48) hours of becoming aware (this is the default if Annex 1 is silent);
- **Service-Provider-favorable:** {{Breach Notification SLA}}, in any event no later than seventy-two (72) hours of becoming aware.

For purposes of this clause, "becoming aware" means a member of {{Processor Short Name}}'s security or incident-response team has a reasonable degree of certainty that a Security Incident has occurred.

### 12.2 Content of notice

The initial notice shall describe, to the extent then known, (i) the nature of the Security Incident, (ii) the categories and approximate number of Consumers and records affected, (iii) the categories and approximate number of Personal Information records concerned, (iv) the likely consequences, (v) the measures taken or proposed to address the incident and mitigate adverse effects, and (vi) a point of contact at {{Processor Short Name}} for further information. {{Processor Short Name}} shall update the notice as further information becomes available.

### 12.3 Statutory notification framework

The parties acknowledge:

(a) **Cal. Civ. Code §1798.82** requires notice to California residents whose unencrypted-or-unredacted PI was, or is reasonably believed to have been, acquired by an unauthorized person, in the most expedient time possible and without unreasonable delay.

(b) **Cal. Civ. Code §1798.81.5** establishes the underlying Reasonable Security duty.

(c) **Cal. Civ. Code §1798.150** confers a private right of action on Consumers whose PI of the categories enumerated in §1798.81.5(d)(1)(A) is subject to a Security Incident due to failure to implement Reasonable Security, with statutory damages of $100–$750 per Consumer per incident or actual damages, whichever is greater. The right runs against the Business that owned or licensed the data, making prompt and accurate notice from {{Processor Short Name}} a material obligation.

(d) **State-by-state breach statutes.** The applicable state statutes are listed in {{State Breach Notice Statutes}}. {{Processor Short Name}} shall cooperate with each, including by providing facts in a format suitable for AG submission and Consumer notice.

### 12.4 Cooperation and remediation

{{Processor Short Name}} shall (i) take reasonable steps to contain and remediate, (ii) preserve forensic evidence, (iii) conduct a root-cause analysis, (iv) implement corrective actions reasonably designed to prevent recurrence, and (v) make personnel available to assist with regulator and class-action defense.

### 12.5 No admission

A §12 notification is not, by itself, an admission of fault. The parties shall coordinate external communications and, unless prohibited by law, neither shall make a public attribution without consulting the other.

---

## 13. Records of processing

In plain English: {{Processor Short Name}} keeps records of what it does with Personal Information so the Business and regulators can verify compliance.

{{Processor Short Name}} shall maintain a written record of its Processing under this DPA sufficient to demonstrate compliance with Cal. Civ. Code §1798.140(ag) and the §20 contract requirements, including: (a) categories of PI; (b) categories of Consumers; (c) Business Purposes; (d) categories of recipients including Sub-processors; (e) Processing and storage locations; (f) any non-US transfers and the safeguards relied upon; (g) retention periods or determining criteria; (h) a general description of the TOMs; and (i) a log of Sub-processor changes notified under §9. The records shall be made available to {{Controller Short Name}} on reasonable request and to regulators on lawful request.

---

## 14. International data transfers

In plain English: this section is about what happens when Personal Information leaves the United States or comes from outside it.

### 14.1 No CCPA SCC-equivalent

Neither the CCPA nor the §20 state laws currently prescribe SCCs (or any equivalent mandatory mechanism) for outbound transfers of PI from the United States. This DPA does not embed an SCC-style module. The parties remain free to localize or transfer PI consistent with the Agreement and applicable sectoral law (HIPAA, GLBA, export-control, sanctions).

### 14.2 Inbound restricted transfers — refer to controller-side DPAs

Where {{Controller Short Name}} or {{Processor Short Name}} receives personal data originating in the EEA, UK, Switzerland, or Iceland, the transfer is governed by the corresponding controller-side variant of this template pack — `eu.md`, `uk.md`, or `is.md`. The transfer mechanisms in those variants (SCCs Modules 1–4, UK IDTA, UK Addendum, EEA-framed Article 46 mechanisms) control over this §14 in the event of conflict, and this DPA's obligations flow down to any restricted transfer.

### 14.3 US surveillance-law disclosures — Schrems II posture

OPTIONAL — only if {{Processor Short Name}} is a US "electronic communications service" or "remote computing service" provider potentially subject to FISA §702 (50 U.S.C. §1881a), Executive Order 14086, or the CLOUD Act (18 U.S.C. §§2701–2713 as amended) `[VERIFY]`.

To the extent lawfully permitted, {{Processor Short Name}} shall (i) maintain the Annex 2 measures designed to minimize compelled disclosure; (ii) challenge overbroad requests, including via the Data Protection Review Court mechanism under EO 14086; (iii) publish a transparency report on government-request volume; and (iv) cooperate with any controller-side Transfer Impact Assessment. This clause supports the Schrems II analysis used in the EU/UK/IS variants but does not, by itself, satisfy any non-US jurisdiction's transfer-mechanism requirement.

### 14.4 Onward transfers

Any onward transfer (e.g., to a non-US Sub-processor) shall comply with §9 and any controller-side transfer mechanism under §14.2.

---

## 15. Audits & inspections

In plain English: the Business is entitled to verify that {{Processor Short Name}} actually does what this DPA says it will do, with reasonable limits.

### 15.1 Demonstrate-compliance obligation

{{Processor Short Name}} shall make available all information reasonably necessary to demonstrate compliance with §1798.140(ag) (or §1798.140(j) where applicable) and shall allow for and contribute to audits and inspections conducted by {{Controller Short Name}} or its mandated auditor.

### 15.2 Routine audit — third-party attestations

{{Processor Short Name}}'s most recent SOC 2 Type II report, ISO/IEC 27001, ISO/IEC 27701, or comparable independent attestation satisfies the routine audit requirement and shall be provided under NDA on reasonable request. {{Processor Short Name}} shall maintain at least one such attestation throughout the term.

### 15.3 For-cause on-site audit

{{Controller Short Name}} may conduct a for-cause on-site audit where (i) it reasonably believes {{Processor Short Name}} has materially breached this DPA, (ii) a regulator has directed an audit, or (iii) a notified Security Incident materially affected the PI. Thirty (30) days' notice is required (less for regulator-directed audits), at a mutually agreed time during business hours, with reasonable steps to avoid disruption and to respect other customers' confidentiality.

### 15.4 Cost allocation and frequency

Routine audits are not separately chargeable. For-cause audits are at {{Controller Short Name}}'s expense, except that if a material breach is substantiated, {{Processor Short Name}} reimburses reasonable audit costs. Audits are limited to once per twelve-month period absent for-cause grounds.

### 15.5 Confidentiality

The auditor shall sign confidentiality at least on Agreement terms; scope is limited to controls relevant to the Business's Processing; and {{Processor Short Name}} may redact information that would compromise other customers' or third parties' confidentiality.

---

## 16. Return or deletion on termination

In plain English: at the end of the engagement (or earlier if asked), {{Processor Short Name}} returns or deletes the Personal Information.

### 16.1 At termination

On termination or expiration of the Agreement, or earlier on written request, {{Processor Short Name}} shall, at {{Controller Short Name}}'s election: (a) return PI in a structured, commonly-used, machine-readable format (or the Annex 1 format); or (b) delete PI, including by securely overwriting primary storage and removing backup copies per the documented rotation schedule.

### 16.2 Certification

{{Processor Short Name}} shall deliver a written deletion certification within thirty (30) days of completion, signed by an authorized officer.

### 16.3 Statutory retention exceptions

If law requires retention beyond the deletion deadline (tax records, legal-claim defense, §1798.105(d) exceptions), {{Processor Short Name}} shall (i) inform {{Controller Short Name}} of the basis, (ii) limit further Processing to that basis, and (iii) delete once the basis ceases.

### 16.4 Backups

Backup-resident PI shall be deleted within ninety (90) days of backup rotation, or by the expiration of the Annex 2 retention window. Between primary deletion and backup deletion, {{Processor Short Name}} shall not Process residual PI other than for disaster recovery.

---

## 17. Liability & indemnity

In plain English: this section says how the parties allocate responsibility if something goes wrong. The default below is the market-standard compromise; parties with stronger or weaker bargaining positions should consider the controller-favorable or service-provider-favorable variants.

### 17.1 Allocation

Each party is responsible for damages it causes by Processing that infringes this DPA or the CCPA / §20 state laws. Liability between the parties is governed by the Agreement, except nothing limits liability to (i) Consumers under §1798.150, (ii) the California AG or CPPA under §1798.155, or (iii) equivalent state enforcement authorities under §20.

### 17.2 Indemnity

{{Processor Short Name}} shall indemnify {{Controller Short Name}} against third-party claims (including regulator penalties and §1798.150 class-action damages) to the extent arising from (i) breach of §1798.140(ag)(1)(A)–(D), (ii) failure to implement Reasonable Security under §8 resulting in a Security Incident, or (iii) any unauthorized Sale or Sharing. {{Controller Short Name}} shall similarly indemnify {{Processor Short Name}} for breach of its DPA obligations.

### 17.3 Caps and exclusions

The Agreement's liability cap and damages exclusions apply, except they do not limit liability for (i) breach of confidentiality, (ii) violation of §1798.140(ag)(1)(A)–(D), (iii) gross negligence or willful misconduct, or (iv) statutory penalties or private-right-of-action damages that cannot be capped contractually.

### 17.4 Insurance

{{Processor Short Name}} shall maintain commercial general liability, technology E&O, and cyber liability insurance commensurate with the volume and sensitivity of PI Processed, with certificates available on request.

---

## 18. Governing law, jurisdiction, dispute resolution

In plain English: California law governs this DPA in the first instance, but each state's law continues to govern its own Consumers' Personal Information.

### 18.1 Governing law

This DPA is governed by the laws of {{Governing Law}}, without regard to conflict-of-laws principles. The parties select California law as the default governing law in light of the centrality of CCPA terminology. Notwithstanding the preceding sentence, the substantive privacy law of each state listed in §20 governs the rights of the Consumers of that state and the parties' obligations with respect to the Personal Information of those Consumers.

### 18.2 Jurisdiction and venue

Disputes arising out of or relating to this DPA shall be resolved in accordance with the dispute-resolution clause of the Agreement, which the parties hereby incorporate by reference. Where the Agreement is silent, the parties submit to the exclusive jurisdiction of the state and federal courts located in San Francisco, California.

### 18.3 Equitable relief

Either party may seek injunctive or other equitable relief in any court of competent jurisdiction to prevent or stop a breach of this DPA, in addition to any other remedy available at law or in equity.

### 18.4 Severability and survival

If any provision of this DPA is held invalid or unenforceable, the remaining provisions remain in full force and effect, and the parties shall negotiate in good faith to replace the invalid provision with a valid provision that achieves, as closely as possible, the original economic and legal effect. Sections 5, 7, 8.1, 12, 13, 16, 17, and 18 survive termination.

---

## 19. Order of precedence & miscellaneous

In plain English: if this DPA contradicts the Agreement on a privacy question, this DPA wins; otherwise the Agreement wins.

### 19.1 Order of precedence

In the event of a conflict between this DPA and any other document forming part of the parties' contractual relationship, the order of precedence is: (1) this DPA on matters of privacy, security, and Personal Information handling; (2) any superseding mandatory regulator-issued contract template (where applicable); (3) the Agreement; (4) any subordinate ordering documents (statements of work, order forms, or schedules).

### 19.2 Amendments

This DPA may be amended only by a written instrument signed by both parties, except that {{Processor Short Name}} may update Annex 2 (TOMs) and Annex 3 (Sub-processors) in accordance with §8 and §9 respectively without a counter-signed amendment.

### 19.3 Entire agreement

This DPA, together with its annexes and the Agreement, constitutes the entire agreement between the parties with respect to the subject matter and supersedes any prior or contemporaneous agreements on the subject matter.

### 19.4 Counterparts and electronic signature

This DPA may be executed in counterparts, including by electronic signature, each of which is an original and all of which together constitute one instrument.

### 19.5 No third-party beneficiaries

Except for the Consumer rights expressly preserved by the CCPA and parallel state laws (which by their terms run to Consumers), this DPA confers no rights on any person other than the parties.

### 19.6 Notices

Notices under this DPA are given in accordance with the notices clause of the Agreement, with copies to {{Controller Email Privacy}} and {{Processor Email Privacy}}.

---

## 20. Multi-state addenda

The following addenda apply Personal Information of Consumers protected by the corresponding state law. The substantive obligations of §§1–19 above apply in their entirety to that Personal Information; the addenda below identify the state-specific deviations and pin-cites that supplement (or, where the state-law standard is stricter, override) the California-anchored body of this DPA.

### §20.1 Colorado (CPA)

For the Personal Data of Colorado consumers under the Colorado Privacy Act, Colo. Rev. Stat. §§ 6-1-1301 to 6-1-1313: {{Processor Short Name}} acts as a "**processor**" and {{Controller Short Name}} as a "**controller**" under §6-1-1303. The processor-contract requirements of §6-1-1305(5) — instructions, confidentiality, deletion/return, demonstrable compliance, audit cooperation, sub-processor flow-down, and assistance with controller obligations — are satisfied by §§5–11 and §15 above. {{Processor Short Name}} shall honor the Colorado Universal Opt-Out (Global Privacy Control) honored by Colorado from July 1, 2024 (4 CCR 904-3, Rule 5.06), and shall propagate opt-out signals through the Services. Data Protection Assessments under §6-1-1309 are supported by §11(a). Sensitive Data Processing requires controller-side opt-in consent under §6-1-1308(7); {{Processor Short Name}} shall not Process Sensitive Data of Colorado consumers unless Annex 1 expressly contemplates such Processing and {{Controller Short Name}} confirms a valid consent record. Enforcement is by the Colorado Attorney General; there is no private right of action.

### §20.2 Virginia (VCDPA)

For the Personal Data of Virginia consumers under the Virginia Consumer Data Protection Act, Va. Code §§ 59.1-575 to 59.1-585: {{Processor Short Name}} acts as a "**processor**" and {{Controller Short Name}} as a "**controller**" under §59.1-577. The processor-contract requirements of §59.1-579 (instructions, confidentiality, deletion/return, audits, sub-processor flow-down, assistance) are satisfied by §§5–11 and §15. The VCDPA grants consumers a sixty (60) day appeals window under §59.1-577(C) for controller responses; {{Processor Short Name}} shall provide assistance within timelines that allow {{Controller Short Name}} to meet that window. Data Protection Assessments under §59.1-580 are supported by §11(a). Sensitive Data Processing requires opt-in consent under §59.1-578. Enforcement is by the Virginia Attorney General; there is no private right of action.

### §20.3 Connecticut (CTDPA)

For the Personal Data of Connecticut consumers under the Connecticut Data Privacy Act, Conn. Gen. Stat. §§ 42-515 to 42-526: {{Processor Short Name}} acts as a "**processor**" and {{Controller Short Name}} as a "**controller**" under §42-516. The processor-contract requirements of §42-520 are satisfied by §§5–11 and §15. {{Processor Short Name}} shall recognize the Universal Opt-Out Signal honored by Connecticut from January 1, 2025 (§42-518), and shall propagate opt-out signals through the Services. Data Protection Assessments under §42-522 are supported by §11(a). Sensitive Data and child-data Processing carry heightened consent rules under §42-520(a); {{Processor Short Name}} shall not Process such data without Annex 1 authorization and a valid consent record. Enforcement is by the Connecticut Attorney General; there is no private right of action.

### §20.4 Utah (UCPA)

For the Personal Data of Utah consumers under the Utah Consumer Privacy Act, Utah Code §§ 13-61-101 to 13-61-404: {{Processor Short Name}} acts as a "**processor**" and {{Controller Short Name}} as a "**controller**" under §13-61-102. The processor-contract requirements of §13-61-301 (instructions, confidentiality, sub-processor flow-down, deletion/return) are satisfied by §§5–11 and §15. The UCPA's scope is narrower than the VCDPA's: it applies only to controllers with >$25M in revenue and certain processing-volume thresholds (§13-61-102(1)). Sensitive Data Processing requires "**clear notice and an opportunity to opt out**" rather than opt-in (§13-61-302(3)(b)) — note this departure from the other state laws in this addendum. Enforcement is by the Utah Attorney General after referral from the Utah Division of Consumer Protection (§13-61-402); there is no private right of action.

### §20.5 Texas (TDPSA)

For the Personal Data of Texas consumers under the Texas Data Privacy and Security Act, Tex. Bus. & Com. Code Ch. 541: {{Processor Short Name}} acts as a "**processor**" and {{Controller Short Name}} as a "**controller**" under §541.001. The processor-contract requirements of §541.104 are satisfied by §§5–11 and §15. Texas honors a Universal Opt-Out Signal effective January 1, 2025 `[VERIFY — confirm enforcement posture and opt-out signal recognition under §541.055]`. Sensitive Data Processing requires opt-in consent under §541.101(b)(3). Notably, the TDPSA applies regardless of consumer or controller revenue thresholds where the controller is not a "**small business**" as defined by the U.S. Small Business Administration. Enforcement is by the Texas Attorney General under §541.151–.155, with a 30-day cure period; there is no private right of action.

### §20.6 Oregon (OCPA)

For the Personal Data of Oregon consumers under the Oregon Consumer Privacy Act, Or. Rev. Stat. § 646A.570 to 646A.589 (with the principal processor obligations in § 646A.578): {{Processor Short Name}} acts as a "**processor**" and {{Controller Short Name}} as a "**controller**". The processor-contract requirements of § 646A.578 are satisfied by §§5–11 and §15. The OCPA contains a distinctive "**list of specific third parties**" right under § 646A.574(1)(b) — Oregon consumers are entitled, on request, to a list of specific third parties (not merely categories) to which the controller has disclosed their Personal Data; {{Processor Short Name}} shall provide the information necessary to populate this list. {{Processor Short Name}} shall recognize the Universal Opt-Out Signal honored by Oregon from January 1, 2026, and shall propagate opt-out signals through the Services. Sensitive Data Processing requires opt-in consent under § 646A.572(2)(g). Enforcement is by the Oregon Department of Justice; there is no private right of action.

---

## Annex 1 — Description of processing

| Field | Value |
|---|---|
| Business | {{Controller Legal Name}} ({{Controller Short Name}}), {{Controller Address}}, {{Controller Country}} |
| {{Service Provider Designation}} | {{Processor Legal Name}} ({{Processor Short Name}}), {{Processor Address}}, {{Processor Country}} |
| Service Provider Designation election | [ ] Service Provider (§1798.140(ag)) [ ] Contractor (§1798.140(j)) |
| Service | {{Service Name}} ({{Service URL}}) |
| Effective date | {{Effective Date}} |
| Subject matter | Processing of Personal Information necessary to provide the Service. |
| Duration | Term of the Agreement plus the wind-down period for return or deletion under §16. |
| Nature | Hosting, transmission, storage, indexing, retrieval, support, monitoring, and incident response operations carried out as part of the Service. |
| {{Business Purposes}} | [List the limited and specified business purposes — for example: providing the contracted Service; ensuring the integrity and security of the Service; preventing fraud; complying with law; performing internal operations reasonably aligned with consumer expectations.] |
| Categories of Consumers | [For example: customers and end-users of {{Controller Short Name}}; employees, applicants, and contractors; website visitors; B2B account contacts.] |
| Categories of Personal Information | [For example: identifiers; commercial information; internet/network activity; geolocation (general); audio/video; professional/employment information; education information; inferences.] |
| Sensitive PI in scope? | [ ] Yes — categories: ___ [ ] No |
| ADMT involved? | [ ] Yes — describe: ___ [ ] No |
| Cross-border transfers in scope? | [ ] Inbound EEA/UK/CH/IS — see §14.2 [ ] Outbound from US to: ___ [ ] None |
| Breach notification SLA | [ ] 24h [ ] 48h (default) [ ] 72h |
| Universal Opt-Out Signal recognition | [ ] Enabled at {{Do Not Sell URL}} [ ] N/A — no Sale/Sharing |

---

## Annex 2 — Technical and Organizational Measures

The TOMs below implement Reasonable Security under Cal. Civ. Code §1798.81.5. They are mapped to the CIS Critical Security Controls (current version) and the NIST Cybersecurity Framework Functions (Identify, Protect, Detect, Respond, Recover, Govern). {{Processor Short Name}} shall keep this Annex up to date.

| Control area | CIS Control / NIST CSF Function | Description |
|---|---|---|
| Asset & data inventory | CIS 1, 3 / Identify | Inventory of authorized devices, software, and Personal Information assets; data classification and labeling. |
| Access control | CIS 5, 6 / Protect | Role-based access; least privilege; SSO + MFA for administrative access; periodic access reviews; joiner-mover-leaver process. |
| Encryption | CIS 3 / Protect | Encryption in transit (TLS ≥1.2) and at rest (AES-256 or equivalent); secure key management with rotation; cryptographic erasure on deletion. |
| Secure development | CIS 16 / Protect | Secure SDLC; code review; dependency scanning; secrets management; segregation of duties; deployment approvals. |
| Vulnerability management | CIS 7 / Protect, Detect | Continuous vulnerability scanning; patch SLAs aligned to severity; annual third-party penetration test. |
| Logging & monitoring | CIS 8 / Detect | Centralized log collection; anomaly detection; alert tuning; log integrity and retention. |
| Network defense | CIS 12, 13 / Protect | Segmented network; firewalling and egress control; DDoS protection; intrusion detection. |
| Endpoint defense | CIS 10 / Protect | EDR on endpoints; hardened images; device management. |
| Incident response | CIS 17 / Respond | Documented IR plan; on-call rotation; tabletop exercises; coordination with the Business under §12. |
| Backup & recovery | CIS 11 / Recover | Backups with offsite/region redundancy; periodic restore tests; RPO/RTO targets stated for the Service. |
| Personnel security | CIS 14 / Govern | Background checks where lawful; confidentiality undertakings; security training at hire and annually. |
| Vendor risk | CIS 15 / Govern | Sub-processor due diligence; flow-down per §9; ongoing monitoring. |
| Physical security | CIS 12 / Protect | Controlled facility access; environmental controls; visitor management. |
| Audit & assurance | / Govern | SOC 2 Type II / ISO 27001 (or equivalent) maintained; report-sharing under §15.2. |
| Sensitive PI controls | CIS 3 / Protect | Enhanced encryption, segregation, access logging, and reduced retention as per §8.4. |

`[VERIFY]` Where the CPPA Cybersecurity Audit Regulations (Cal. Code Regs. tit. 11 §§ 7120–7129) are final and apply to the Business, {{Processor Short Name}} shall additionally maintain auditor-ready documentation aligned to the regulations' enumerated elements.

---

## Annex 3 — Sub-processor list

| Sub-processor (entity name) | Role / function | Processing locations | Sensitive PI? | Onboarded |
|---|---|---|---|---|
| [name] | [hosting / email / payments / etc.] | [country/region] | [Y/N] | [YYYY-MM-DD] |
| [name] | […] | […] | [Y/N] | [YYYY-MM-DD] |

The current list is also published at {{Subprocessor List URL}}. Notice of new or replacement Sub-processors is provided as set out in §9 with at least {{Notification Window}} prior notice.

---

## Annex 4 — International transfer mechanism

The CCPA and the parallel state laws listed in §20 do not currently mandate a Standard Contractual Clauses–equivalent transfer mechanism for outbound transfers from the United States. Where the Personal Information Processed under this DPA includes personal data originating in the European Economic Area, the United Kingdom, Switzerland, or Iceland, the transfer is governed by the corresponding controller-side DPA — `eu.md`, `uk.md`, or `is.md` — and the transfer mechanism it embeds (SCCs Modules 1–4, the UK IDTA, the UK Addendum, EEA-framed Article 46 mechanisms). This Annex serves as a routing reference rather than as an embedded transfer instrument.

| Direction | Governing instrument | Where embedded |
|---|---|---|
| US → US (intra-US) | Not applicable — no cross-border transfer | — |
| US → third country | Sectoral law and contract; no SCC-equivalent | This Annex 4 |
| EEA → US | EU SCCs (Modules 1–4) and US recipient commitments | `eu.md` Annex 4 |
| UK → US | UK IDTA or UK Addendum to the EU SCCs | `uk.md` Annex 4 |
| Switzerland → US | EU SCCs adapted for Switzerland under FDPIC guidance | `eu.md` Annex 4 |
| Iceland → US | EU SCCs as applied via the EEA framework | `is.md` Annex 4 |

OPTIONAL — only if {{Processor Short Name}} is a US "electronic communications service" or "remote computing service" provider potentially subject to FISA §702, EO 14086, or the CLOUD Act `[VERIFY]`. {{Processor Short Name}} represents that it has implemented the technical, legal, and organizational measures referenced in §14.3 designed to limit disclosure to government authorities to the minimum legally required and to support controller-side Transfer Impact Assessments.

---

## Merge fields used

In addition to the common merge fields listed in the pack-level README:

```
{{Service Provider Designation}}     # "Service Provider" or "Contractor"
{{Business Purposes}}                # list of permitted Business Purposes — Annex 1
{{State Breach Notice Statutes}}     # list of state breach-notification statutes that apply — §12.3
{{Authorized Agent Submission URL}}  # URL where Authorized Agents submit requests
{{DSAR Submission URL}}              # URL for direct Consumer rights requests
{{Do Not Sell URL}}                  # public-facing "Do Not Sell or Share My Personal Information" URL
```

---

## Authoritative references

- California Office of the Attorney General — CCPA materials and enforcement guidance — https://oag.ca.gov/privacy/ccpa
- California Privacy Protection Agency — regulations, enforcement, advisories — https://cppa.ca.gov
- California Civil Code §§ 1798.100–1798.199.100 (CCPA / CPRA)
- California Code of Regulations tit. 11 §§ 7000–7304 (CCPA Regulations, Cybersecurity Audit Regulations §§ 7120–7129, Risk-Assessment Regulations, ADMT Regulations §§ 7150–7158 and §§ 7200–7222) `[VERIFY]`
- Colorado Department of Law — CPA materials — https://coag.gov/resources/colorado-privacy-act/
- Connecticut Attorney General — CTDPA guidance — https://portal.ct.gov/ag
- Oregon Department of Justice — OCPA guidance — https://www.doj.state.or.us
- Texas Attorney General — TDPSA enforcement — https://www.texasattorneygeneral.gov
- Utah Division of Consumer Protection — UCPA materials — https://dcp.utah.gov
- Virginia Attorney General — VCDPA guidance — https://www.oag.state.va.us
- NIST Cybersecurity Framework (current version) — https://www.nist.gov/cyberframework
- CIS Critical Security Controls (current version) — https://www.cisecurity.org/controls
- Common Paper DPA v1.0 (CCPA Exhibit) — CC-BY-4.0 — https://commonpaper.com
- Bonterms DPA — CC-BY-4.0 — https://bonterms.com
- Mozilla DPA references — MPL-2.0 — https://www.mozilla.org

---

## Not legal advice

This Exhibit is a custom-built drafting template, not legal advice. It is a starting point for negotiation, not a substitute for qualified privacy counsel admitted in the relevant jurisdictions. The CCPA, the §20 state laws, and the CPPA regulations continue to evolve; `[VERIFY]` flags mark provisions in flux at the last update. Before execution, the parties should (i) confirm the Service Provider Designation election in Annex 1, (ii) populate Annexes 1–3 with accurate operational detail, (iii) confirm the §12 SLA election, (iv) verify the status of the Cybersecurity Audit, Risk-Assessment, and ADMT Regulations, and (v) align dispute-resolution and liability with the parent Agreement. Using this template does not create a lawyer-client relationship with Fordæmi ehf. or any contributor.
