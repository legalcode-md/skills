---
title: Data Processing Agreement (Jurisdiction-Neutral Baseline)
jurisdictions: [global]
posture: dual-perspective (controller-favorable / processor-favorable / market-standard)
license: MIT
last_updated: 2026-04-28
---

# Data Processing Agreement — Jurisdiction-Neutral Baseline

This Data Processing Agreement ("**DPA**") is entered into between **{{Controller Legal Name}}** ("**{{Controller Short Name}}**" or "**Controller**"), of **{{Controller Address}}**, and **{{Processor Legal Name}}** ("**{{Processor Short Name}}**" or "**Processor**"), of **{{Processor Address}}**, and is effective on **{{Effective Date}}**. It supplements the **{{MSA Title}}** dated **{{MSA Effective Date}}** between the parties (the "**Parent Agreement**") with respect to the **{{Service Name}}** services made available at **{{Service URL}}** (the "**Services**"). This DPA was last updated on **{{Last Updated Date}}**.

---

## 1. Plain-language summary

*Plain-language: This first part of the DPA tells a non-lawyer what the document is for, what the rest of the document does, and how the schedules in the back fit together. Read this first and the operative clauses second.*

A Data Processing Agreement is the written contract the parties sign whenever one party (the Controller) hands personal data to another party (the Processor) so the Processor can perform a service. The Controller decided why the data is being handled and broadly how. The Processor handles that data on the Controller's behalf, doing only the things the Controller has asked it to do. This DPA is the rulebook that sits between them.

This baseline is jurisdiction-neutral and is meant to be combined with one or more jurisdictional addenda (for example, an EU/EEA addendum incorporating Standard Contractual Clauses, a UK addendum incorporating the International Data Transfer Addendum, a California addendum, a Brazilian LGPD addendum). The substantive backbone is shaped to satisfy Article 28 of the EU General Data Protection Regulation, because Article 28 is the most demanding processor-contract regime in current commercial use. Drafting to the higher standard here keeps the addenda short.

The annexes after Section 19 carry the operational facts. Annex 1 describes the actual processing activity. Annex 2 lists the technical and organizational measures the Processor maintains. Annex 3 is the sub-processor list, normally also published at a public URL. Annex 4 is a placeholder pointing at the per-jurisdiction transfer mechanism.

A small number of clauses come in three flavors — Controller-favorable, Processor-favorable, and market-standard compromise. Where the parties have not chosen, the market-standard compromise applies. Merge fields written as `{{Like This}}` are placeholders that the deploying party fills in before signature.

This DPA is not, and is not intended to be, legal advice. It is a starting framework. The closing paragraph after the annexes asks both parties to involve qualified counsel and a Data Protection Officer (or equivalent privacy lead) before signing.

---

## 2. Definitions

*Plain-language: This section gives the words used in the rest of the DPA a single, agreed meaning so the parties do not argue later about what something meant.*

In this DPA, capitalized terms have the meanings set out below. Terms used but not defined here have the meanings given to them in Applicable Data Protection Law or, failing that, the Parent Agreement.

**2.1 "Applicable Data Protection Law"** means each statute, regulation, binding regulator guidance, code of conduct, or certification scheme that applies to the Processing of Personal Data carried out under this DPA, as amended, replaced, or supplemented from time to time.

**2.2 "Controller"** means the natural or legal person who, alone or jointly with others, determines the purposes and means of the Processing of Personal Data. For the purposes of this DPA the Controller is **{{Controller Short Name}}**.

**2.3 "Data Subject"** means an identified or identifiable natural person to whom Personal Data relates.

**2.4 "Instructions"** means the documented directions issued by the Controller to the Processor concerning the Processing of Personal Data, including those captured in the Parent Agreement, in this DPA (including its annexes), and in any later writing exchanged between the parties' authorized representatives.

**2.5 "Personal Data"** means any information relating to a Data Subject that is Processed by the Processor on behalf of the Controller under the Parent Agreement.

**2.6 "Personal Data Breach"** means a breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to, Personal Data Processed by the Processor or any Sub-processor.

**2.7 "Processing"** (and its conjugations) means any operation or set of operations performed on Personal Data, whether or not by automated means, including collection, recording, organization, structuring, storage, adaptation, retrieval, consultation, use, disclosure, dissemination, alignment, restriction, erasure, or destruction.

**2.8 "Processor"** means the natural or legal person who Processes Personal Data on behalf of the Controller. For the purposes of this DPA the Processor is **{{Processor Short Name}}**.

**2.9 "Restricted Transfer"** means any transfer of Personal Data from a jurisdiction whose data protection law restricts transfers outside that jurisdiction (for example, the EEA, the United Kingdom, Switzerland, or other comparable regimes) to a jurisdiction that the originating regime has not declared to provide an adequate level of protection.

**2.10 "Services"** has the meaning given in the Parent Agreement and refers to the activities performed by the Processor for the Controller in connection with **{{Service Name}}**.

**2.11 "Sub-processor"** means any third party (including any affiliate of the Processor) engaged by the Processor to Process Personal Data on the Processor's behalf in connection with the Services.

**2.12 "Supervisory Authority"** means the public authority that has competence over the Processing under Applicable Data Protection Law.

**2.13 "Technical and Organizational Measures"** or "**TOMs**" means the technical and organizational security controls implemented by the Processor as set out in Annex 2 and as updated from time to time in accordance with this DPA.

Words such as "include", "including", and "in particular" are illustrative and not limiting. References to a statute include its successors and implementing instruments.

---

## 3. Subject matter, duration, nature & purpose of processing

*Plain-language: This section anchors the DPA to a specific real-world activity instead of leaving it abstract.*

**3.1 Subject matter.** The subject matter of the Processing under this DPA is the Processor's performance of the Services as described in the Parent Agreement and further particularized in Annex 1.

**3.2 Duration.** This DPA enters into effect on the Effective Date and continues for so long as the Processor Processes Personal Data on behalf of the Controller, irrespective of whether the Parent Agreement remains in force, and concludes only upon completion of the obligations in Section 16 (Return or deletion on termination).

**3.3 Nature and purpose.** The nature of the Processing reflects the technical operations the Processor performs to deliver the Services (such as hosting, transmission, storage, retrieval, analysis, support, and similar operations). The purpose is limited to enabling the Controller's lawful use of the Services and the Processor's performance of its obligations under the Parent Agreement. The Processor shall not Process Personal Data for any other purpose.

**3.4 Reference to Annex 1.** The particulars required by Article 28(3) of the EU General Data Protection Regulation, and any equivalent particulars required by other Applicable Data Protection Law, are set out in Annex 1 and shall be kept current by the parties.

---

## 4. Categories of data subjects and types of personal data

*Plain-language: This section says, at a high level, whose data is being handled and what kind of data it is. The detail is in Annex 1.*

**4.1 Data subjects.** The categories of Data Subjects whose Personal Data may be Processed under this DPA include those described in Annex 1, which may include the Controller's customers, end users, employees, contractors, prospective customers, and other natural persons whose Personal Data the Controller submits to or generates within the Services.

**4.2 Types of personal data.** The types of Personal Data Processed under this DPA include those described in Annex 1, which may include identifiers, contact information, account credentials, professional information, content submitted by Data Subjects, technical data such as IP addresses and device identifiers, and any other Personal Data that the Controller chooses to submit through the Services.

**4.3 Special categories.** The Controller shall not submit, and shall configure its use of the Services so as not to cause the Processor to Process, special categories of Personal Data (such as data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, genetic data, biometric data for identification, health data, or data concerning sex life or sexual orientation), or Personal Data relating to criminal convictions and offences, unless Annex 1 expressly contemplates such Processing and the Processor has confirmed in writing its ability to support that Processing under this DPA.

---

## 5. Roles & responsibilities

*Plain-language: This section says which party is the boss of the data and which party is the hired hand.*

**5.1 Controller role.** The Controller determines the purposes and means of the Processing. The Controller is responsible for the lawfulness of its Instructions and for establishing a valid legal basis for the Processing, for providing transparency information to Data Subjects, and for the accuracy and quality of the Personal Data submitted to the Services.

**5.2 Processor role.** The Processor Processes Personal Data only on documented Instructions from the Controller, including with regard to Restricted Transfers, except where Applicable Data Protection Law to which the Processor is subject requires otherwise. In that case the Processor shall inform the Controller of that legal requirement before Processing, unless Applicable Data Protection Law itself prohibits such notice on important grounds of public interest.

**5.3 Joint controllership not contemplated.** The parties intend to act as Controller and Processor under this DPA. Where, exceptionally, the parties' activities cause them to act as joint controllers within the meaning of Article 26 of the EU General Data Protection Regulation or any equivalent regime, the parties shall agree a separate joint controller arrangement; the joint controller relationship is outside the scope of this DPA.

**5.4 Independent controllers excluded.** Processing the Processor performs as an independent controller (for example, billing and account administration of the Processor's own commercial relationship with the Controller, internal security telemetry, defending legal claims, or compliance with the Processor's own legal obligations) is not Processing on behalf of the Controller and is not governed by this DPA, but is governed by the Processor's own privacy notice as a controller.

---

## 6. Documented processing instructions

*Plain-language: This section says where the Controller's instructions to the Processor live, and what happens if the Processor thinks an instruction is unlawful.*

**6.1 Initial instructions.** The Parent Agreement, this DPA (including its annexes), the Controller's documented configuration of the Services, and the Controller's lawful use of the Services together constitute the Controller's complete and final Instructions to the Processor at the Effective Date.

**6.2 Further instructions.** The Controller may issue further Instructions in writing (which includes electronic mail to the contacts listed in Section 6.5). The Processor shall comply with such Instructions to the extent they are within the scope of the Services and are technically and lawfully achievable. If an Instruction would require a material change to the Services, the Processor may treat it as a request for a change order under the Parent Agreement.

**6.3 Notice of unlawful instruction.** If the Processor reasonably believes that an Instruction infringes Applicable Data Protection Law, the Processor shall promptly notify the Controller and may suspend the affected Processing until the Controller confirms or modifies the Instruction. The Processor's notification under this Section 6.3 is not legal advice and does not transfer responsibility for the lawfulness of the Instruction to the Processor.

**6.4 Out-of-scope processing.** The Processor shall not Process Personal Data for its own purposes, and shall not sell, share, or rent Personal Data, in each case as those terms are used in Applicable Data Protection Law.

**6.5 Notices.** Notices to the Controller relating to Processing shall be sent to **{{Controller Email Privacy}}** (with copy to **{{Controller Email DPO}}** where applicable). Notices to the Processor shall be sent to **{{Processor Email Privacy}}** (with copy to **{{Processor Email DPO}}** where applicable). Either party may change its notice address by giving written notice to the other.

---

## 7. Confidentiality of personnel

*Plain-language: This section says that the people working on the Controller's data must be sworn to confidentiality.*

**7.1 Authorized personnel.** The Processor shall ensure that access to Personal Data is limited to personnel who need access to perform the Services and who have been authorized in writing by the Processor.

**7.2 Confidentiality undertakings.** The Processor shall ensure that its personnel authorized to Process Personal Data are bound by enforceable contractual or statutory obligations of confidentiality with respect to Personal Data, and that those obligations survive termination of their engagement with the Processor.

**7.3 Training.** The Processor shall ensure that its personnel authorized to Process Personal Data receive appropriate training on the protection of Personal Data and on the Processor's obligations under this DPA.

**7.4 Need-to-know.** The Processor shall apply the principle of least privilege so that authorized personnel access only the Personal Data, and only the systems, that they require to perform their assigned tasks.

---

## 8. Security measures (TOMs)

*Plain-language: This section says the Processor must have real, working security in place — and lets the parties pick how detailed the lock-in language is.*

**8.1 Baseline obligation.** Taking into account the state of the art, the costs of implementation, the nature, scope, context and purposes of Processing, and the risks of varying likelihood and severity for the rights and freedoms of natural persons, the Processor shall implement and maintain the Technical and Organizational Measures set out in Annex 2 and shall ensure that those measures are appropriate to the risk.

**8.2 Risk-based ongoing review.** The Processor shall periodically review and, where appropriate, update its TOMs to reflect changes in the threat landscape, in technology, in the nature of the Services, and in Applicable Data Protection Law. Updates shall not materially diminish the level of protection provided as of the Effective Date.

### 8.3 Variants — level of TOM detail

**Controller-favorable:** The Processor shall not modify or remove any TOM listed in Annex 2 without the Controller's prior written consent. Any change that could reduce the security posture of the Services shall be notified to the Controller at least thirty (30) days in advance and shall be accompanied by a written impact assessment. The Processor shall provide the Controller, on request and at no charge, with current copies of its information security policies, penetration test summaries, and remediation plans.

**Processor-favorable:** The Processor maintains a comprehensive information security program described at a high level in Annex 2. The Processor may, in its reasonable discretion, modify the controls comprising that program, provided the overall level of protection is not materially diminished. Detailed policy documents are confidential and may be made available under non-disclosure for the limited purpose of audit cooperation under Section 15.

**Market-standard compromise (recommended default):** The Processor shall maintain TOMs that, in the aggregate, are no less protective than those described in Annex 2. The Processor may modify individual measures provided the overall level of protection is not materially diminished. Material reductions require prior written notice to the Controller of at least thirty (30) days. Detailed control documentation is treated as confidential information of the Processor and is made available to the Controller through the audit mechanisms in Section 15.

---

## 9. Sub-processors

*Plain-language: This section says when, and how, the Processor may bring in other companies to help — and what veto rights the Controller has.*

**9.1 Existing sub-processors.** The Controller acknowledges and accepts the Sub-processors engaged by the Processor as of the Effective Date, listed in Annex 3 and at **{{Subprocessor List URL}}**.

**9.2 Flow-down.** The Processor shall enter into a written contract with each Sub-processor that imposes data protection obligations no less protective than those imposed on the Processor under this DPA, taking into account the nature of the services to be provided by that Sub-processor.

**9.3 Continued liability.** The Processor remains fully liable to the Controller for the performance of each Sub-processor's obligations under that Sub-processor's contract, as if the Processor were performing those obligations itself.

### 9.4 Variants — authorization mode

**Controller-favorable (specific authorization):** The Processor shall not engage any new Sub-processor, nor permit any change in the role or scope of an existing Sub-processor, without the Controller's prior written consent on a case-by-case basis. The Processor shall provide the Controller with the information necessary to evaluate the proposed Sub-processor (including its name, location, processing activities, and applicable transfer mechanism). The Controller may withhold consent in its reasonable discretion. Where consent is withheld, the parties shall cooperate in good faith to identify a workable alternative; if none is available within a reasonable period, either party may terminate the affected portion of the Services without penalty.

**Processor-favorable (general authorization, narrow opposition):** The Controller grants the Processor a general authorization to engage Sub-processors. The Processor shall maintain an up-to-date list of Sub-processors at **{{Subprocessor List URL}}** and shall update that list before any new Sub-processor begins Processing Personal Data. The Controller may object to a new Sub-processor only on documented grounds relating to that Sub-processor's data protection compliance, and only by written notice within **{{Notification Window}}** of the list update. Where an objection is sustained, the Processor's exclusive remedy is to propose a workable alternative; if none can be implemented, the Processor may continue with the disputed Sub-processor.

**Market-standard compromise (recommended default):** The Controller grants the Processor a general authorization to engage Sub-processors, subject to the obligations in this Section 9. The Processor shall provide notice of any intended addition or replacement of a Sub-processor by updating the list at **{{Subprocessor List URL}}** and, where the Controller has subscribed to such notifications, by sending notice to **{{Controller Email Privacy}}**. The Controller may object on reasonable data-protection grounds within **{{Notification Window}}** of receiving the notice. The parties shall cooperate in good faith to resolve the objection. If the parties cannot resolve the objection within a reasonable period, the Controller may terminate the portion of the Services that cannot be provided without the disputed Sub-processor without penalty, on written notice to the Processor.

---

## 10. Data subject rights assistance

*Plain-language: This section says the Processor will help the Controller respond when a person whose data is in the system asks to see it, correct it, delete it, or exercise some other right.*

**10.1 Cooperation duty.** Taking into account the nature of the Processing, the Processor shall assist the Controller by appropriate technical and organizational measures, insofar as this is possible, in fulfilling the Controller's obligation to respond to requests from Data Subjects exercising rights under Applicable Data Protection Law, including rights of access, rectification, erasure, restriction, portability, objection, and rights related to automated decision-making.

**10.2 Pass-through.** If a Data Subject contacts the Processor directly with a request that concerns Personal Data Processed on behalf of the Controller, the Processor shall, without undue delay and without responding to the substance of the request, forward the request to the Controller and shall await the Controller's instructions, except where Applicable Data Protection Law requires otherwise.

**10.3 Self-service tooling.** Where the Services include functionality that allows the Controller to access, correct, export, or delete Personal Data without the Processor's manual intervention, the Processor's provision and maintenance of that functionality satisfies its assistance obligation under this Section 10 with respect to the relevant rights, provided the functionality remains available and operative.

**10.4 Reasonable costs.** The Processor's standard assistance is provided at no additional charge. Where the Controller requests assistance that materially exceeds the standard support included in the Services, the Processor may charge a reasonable, cost-based fee, notified to the Controller in advance.

---

## 11. Assistance with controller compliance

*Plain-language: This section covers the Processor's duty to help the Controller with its broader data-protection paperwork — DPIAs, regulator consultations, breach response support, and records of processing.*

**11.1 Scope.** Taking into account the nature of the Processing and the information available to the Processor, the Processor shall provide reasonable assistance to the Controller in respect of the Controller's compliance with its obligations under Applicable Data Protection Law, including those described in this Section 11.

### 11.2 Variants — DPIA and prior consultation assistance scope

**Controller-favorable:** The Processor shall provide all information reasonably necessary for the Controller to conduct a data protection impact assessment ("**DPIA**") and, where required, to consult with a Supervisory Authority. The Processor shall participate in DPIA workshops and shall complete DPIA questionnaires within fifteen (15) business days of receipt. The Processor shall not charge for assistance up to a reasonable annual cap aligned with the size of the engagement.

**Processor-favorable:** The Processor shall make available to the Controller standard documentation that supports DPIA preparation (including the TOMs in Annex 2, summary security certifications, and any pre-prepared transfer impact assessment). Bespoke DPIA support, including responses to custom questionnaires or workshops, is provided as a chargeable professional service.

**Market-standard compromise (recommended default):** The Processor shall provide reasonable assistance, including by making available existing security documentation and answering reasonable Controller questions, to enable the Controller's DPIA and any required prior consultation with a Supervisory Authority. Where assistance materially exceeds standard cooperation (for example, custom workshops, bespoke questionnaires that go beyond the Processor's standard responses, or expert witness preparation), the Processor may charge reasonable, cost-based fees notified to the Controller in advance.

**11.3 Records of Processing assistance.** The Processor shall make available to the Controller the information about the Processor's Processing activities that the Controller reasonably requires to maintain its own records of processing under Applicable Data Protection Law.

**11.4 Breach assistance.** The Processor shall assist the Controller in complying with its obligations to notify Personal Data Breaches to a Supervisory Authority and, where required, to communicate Personal Data Breaches to Data Subjects. Operational details are set out in Section 12.

**11.5 Security obligation assistance.** The Processor shall assist the Controller in ensuring compliance with the security-of-processing, breach-notification, DPIA, and prior-consultation obligations of Applicable Data Protection Law, by maintaining the TOMs in Annex 2 and by providing the cooperation described in this DPA.

---

## 12. Personal data breach notification

*Plain-language: This section says the Processor must tell the Controller fast when something goes wrong with the data, and what that notification has to contain.*

**12.1 Detection.** The Processor shall maintain monitoring, alerting, and incident-response capabilities reasonably designed to detect Personal Data Breaches affecting the Services.

### 12.2 Variants — notification SLA

**Controller-favorable:** The Processor shall notify the Controller of any Personal Data Breach without undue delay and in any event within twenty-four (24) hours of becoming aware of the Personal Data Breach. The first notification shall be made even if the investigation is incomplete and may be supplemented as facts develop.

**Processor-favorable:** The Processor shall notify the Controller of confirmed Personal Data Breaches without undue delay after the Processor's incident response team has triaged the incident and confirmed its scope, and in any event within seventy-two (72) hours of confirmation. The Processor shall not be obliged to notify suspected events that, on initial triage, are determined not to constitute a Personal Data Breach.

**Market-standard compromise (recommended default):** The Processor shall notify the Controller of a Personal Data Breach **{{Breach Notification SLA}}** (default: without undue delay and in any event within forty-eight (48) hours of becoming aware of the Personal Data Breach). Initial notification may be partial; the Processor shall provide updates as further information becomes available.

**12.3 Content of notification.** Each notification under this Section 12 shall describe, to the extent then known and to the extent the Processor reasonably can disclose: (a) the nature of the Personal Data Breach, including the categories and approximate number of Data Subjects and Personal Data records concerned; (b) the likely consequences; (c) the measures the Processor has taken or proposes to take to address the Personal Data Breach, including measures to mitigate its possible adverse effects; and (d) the contact point at the Processor for further information.

**12.4 Cooperation and remediation.** The Processor shall cooperate with the Controller in investigating, mitigating, and remediating the Personal Data Breach, and shall provide the Controller with reasonable information to enable the Controller to comply with any notification or communication obligation under Applicable Data Protection Law.

**12.5 No admission.** Notification of a Personal Data Breach by the Processor is not, and shall not be construed as, an admission of fault or liability.

**12.6 Costs.** Each party bears its own internal costs of breach response. Direct external costs reasonably and necessarily incurred by the Controller as a result of a Personal Data Breach caused by the Processor's breach of this DPA are recoverable subject to Section 17.

---

## 13. Records of processing

*Plain-language: This section says the Processor keeps its own paperwork about what it does and helps the Controller keep its paperwork.*

**13.1 Processor's records.** The Processor shall maintain a written (which may be electronic) record of the categories of Processing activities carried out on behalf of the Controller, in the form and with the content required by Applicable Data Protection Law (including, where applicable, Article 30(2) of the EU General Data Protection Regulation).

**13.2 Provision to Supervisory Authority.** The Processor shall make its records of Processing available to a competent Supervisory Authority on request, where required by Applicable Data Protection Law. The Processor shall, where lawful and practicable, notify the Controller of any such request before responding.

**13.3 Assistance to Controller.** On reasonable written request, the Processor shall provide the Controller with the information about the Processor's Processing activities that the Controller reasonably needs to populate the Controller's own records of Processing.

---

## 14. International data transfers

*Plain-language: This section says that if the data crosses a border into a country whose laws are considered weaker, a special legal mechanism (such as the EU Standard Contractual Clauses) must be in place. The detail is in the per-jurisdiction addenda and Annex 4.*

**14.1 General principle.** Any Restricted Transfer of Personal Data carried out under this DPA shall be supported by a valid transfer mechanism under Applicable Data Protection Law.

**14.2 Annex 4.** The transfer mechanism applicable to a given flow of Personal Data is identified in Annex 4 by reference to the relevant per-jurisdiction addendum (for example, an EU/EEA addendum incorporating the European Commission's Standard Contractual Clauses, a UK addendum incorporating the International Data Transfer Addendum, or a Swiss addendum). This core DPA is jurisdiction-neutral and does not itself incorporate any particular set of Standard Contractual Clauses.

**14.3 Transfer impact assessment cooperation.** The Processor shall cooperate with the Controller, on reasonable request, in preparing or updating a transfer impact assessment, including by providing information about the destination jurisdiction's law as it relates to the Services and by describing supplementary measures that the Processor has implemented.

**14.4 Onward transfers.** Where the Processor relies on a Sub-processor located in a jurisdiction that triggers a Restricted Transfer, the Processor shall ensure that the onward transfer is itself supported by an appropriate transfer mechanism, and shall reflect the chosen mechanism in Annex 3 and Annex 4.

**14.5 Conflict.** If a per-jurisdiction addendum incorporates Standard Contractual Clauses or an equivalent instrument, those clauses prevail over this Section 14 to the extent of any conflict, in accordance with the order of precedence in Section 19.

---

## 15. Audits & inspections

*Plain-language: This section says how the Controller verifies that the Processor is actually doing what it promised. It strikes a balance between meaningful oversight and operational disruption.*

**15.1 Audit right.** The Processor shall make available to the Controller information necessary to demonstrate compliance with this DPA, and shall allow for and contribute to audits, including inspections, conducted by the Controller or a third-party auditor mandated by the Controller, in accordance with this Section 15.

### 15.2 Variants — audit frequency, on-site rights, and third-party auditor

**Controller-favorable:** The Controller may conduct an audit once every twelve (12) months on at least fifteen (15) business days' written notice, and additionally at any time following a Personal Data Breach or upon a regulator's written request. The Controller may conduct on-site inspections at any Processor facility used to Process Personal Data. The Controller may appoint any reputable third-party auditor of its choosing, subject only to a reasonable confidentiality undertaking. The Processor shall bear its own costs of cooperation; the Controller bears its auditor's fees.

**Processor-favorable:** The Controller's audit right is satisfied by the Processor's most recent SOC 2 Type II report or equivalent independent third-party assessment (such as ISO/IEC 27001 certification with a current statement of applicability), made available under non-disclosure on request. On-site inspections are not permitted except where Applicable Data Protection Law mandates them, in which case they shall be conducted at a mutually agreed time and scope, no more than once every twenty-four (24) months, and at the Controller's expense including the Processor's reasonable cooperation costs. Competitors of the Processor may not act as auditors.

**Market-standard compromise (recommended default):** The Controller may exercise its audit right (a) once per twelve (12)-month period, and (b) additionally following a Personal Data Breach affecting the Controller's Personal Data or upon the documented request of a Supervisory Authority. The Processor's obligation is satisfied in the first instance by the provision, under non-disclosure, of its most recent SOC 2 Type II report, ISO/IEC 27001 certification, or comparable independent assessment, together with reasonable written responses to follow-up questions. Where those materials are reasonably insufficient to address the Controller's documented concerns, the Controller may conduct an on-site inspection on at least thirty (30) days' written notice, during normal business hours, in a manner that does not unreasonably interfere with the Processor's operations, and using either the Controller's own personnel or a mutually acceptable independent third-party auditor (who shall not be a competitor of the Processor and shall be bound by confidentiality obligations no less protective than those in the Parent Agreement). Each party bears its own costs except where the audit identifies a material breach of this DPA by the Processor, in which case the Processor shall reimburse the Controller's reasonable, documented external audit costs.

**15.3 Confidentiality of audit output.** All information disclosed in connection with an audit constitutes confidential information of the disclosing party and shall be used solely to verify compliance with this DPA and Applicable Data Protection Law.

**15.4 Out-of-scope.** Audit rights under this Section 15 do not extend to Processor confidential information unrelated to the Processing of the Controller's Personal Data, to Sub-processor environments to which the Processor itself has no access, or to other Processor customers' data.

---

## 16. Return or deletion on termination

*Plain-language: This section says what happens to the data when the relationship ends.*

**16.1 Controller's choice.** On termination or expiry of the Parent Agreement, or on the Controller's earlier written request, the Processor shall, at the Controller's choice, return to the Controller, or delete, all Personal Data Processed on behalf of the Controller, and shall delete existing copies, except to the extent that retention is required by Applicable Data Protection Law.

**16.2 Default mode and timing.** Unless the Controller specifies otherwise within thirty (30) days of termination or expiry of the Parent Agreement, the Processor shall delete the Personal Data within sixty (60) days of that date.

**16.3 Certification.** On the Controller's written request, the Processor shall provide a written certification of deletion signed by an authorized officer.

**16.4 Backup retention carve-out — OPTIONAL — only if the Processor uses immutable backups.** The Processor may retain Personal Data in routine, encrypted backup media for a period not exceeding the Processor's documented backup retention cycle (and in any event not exceeding twelve (12) months), provided that during that period the Personal Data is logically isolated, is not Processed for any purpose other than backup integrity and disaster recovery, and is then deleted in the ordinary course of the Processor's backup rotation.

**16.5 Statutory retention carve-out.** Where Applicable Data Protection Law requires the Processor to retain Personal Data, the Processor shall: (a) inform the Controller of the requirement before retention (where lawful); (b) retain only the Personal Data and only for the period that the law requires; (c) maintain the confidentiality of the retained Personal Data; and (d) Process the retained Personal Data only as required by that law.

---

## 17. Liability & indemnity

*Plain-language: This section says how money flows if something goes wrong. It is normally the most negotiated section in any DPA.*

### 17.1 Variants — liability cap and indemnity carve-outs

**Controller-favorable:** The Processor's liability under or in connection with this DPA is uncapped to the extent it arises from (a) breach of confidentiality, (b) the Processor's indemnification obligations, (c) the Processor's gross negligence or willful misconduct, (d) breach of Section 6 (Documented processing instructions) or Section 9 (Sub-processors), or (e) administrative fines imposed on the Controller by a Supervisory Authority that are demonstrably and proximately caused by the Processor's breach of this DPA. The Processor shall indemnify, defend, and hold harmless the Controller from and against all third-party claims, regulatory investigations, and Data Subject claims arising out of the Processor's breach of this DPA.

**Processor-favorable:** Each party's aggregate liability under or in connection with this DPA is subject to the aggregate liability cap and exclusions set out in the Parent Agreement, and this DPA does not increase that cap. Liability for indirect, consequential, special, incidental, exemplary, or punitive damages is excluded to the maximum extent permitted by law. Indemnification is limited to direct third-party claims for which the indemnifying party has been given prompt written notice and sole control of the defense.

**Market-standard compromise (recommended default):** Each party's aggregate liability under or in connection with this DPA is subject to the limitations and exclusions set out in the Parent Agreement, except that the following matters are not subject to the aggregate cap (or are subject to a separately negotiated super-cap): (a) breach of confidentiality of Personal Data; (b) the Processor's indemnification of the Controller for third-party claims arising out of the Processor's breach of this DPA; (c) gross negligence or willful misconduct; and (d) liability that cannot be limited or excluded as a matter of Applicable Data Protection Law. Each party shall reasonably mitigate its losses. Where Personal Data is the subject of a single event of damage that triggers liability of both parties, each party shall bear its share according to its responsibility under Applicable Data Protection Law, and the parties shall settle accordings between themselves accordingly.

**17.2 Indemnification mechanics.** The party seeking indemnification shall give the indemnifying party prompt written notice of any indemnifiable claim, shall not make any admission or settlement without the indemnifying party's prior written consent, and shall provide reasonable cooperation in defense of the claim at the indemnifying party's expense.

**17.3 No third-party beneficiaries.** Except for Data Subjects' direct rights under Applicable Data Protection Law, this DPA confers no rights on any person other than the parties.

---

## 18. Governing law, jurisdiction, dispute resolution

*Plain-language: This section says which country's law governs the DPA and where disputes are heard.*

**18.1 Governing law.** This DPA is governed by **{{Governing Law}}**, except to the extent that Applicable Data Protection Law mandatorily applies its own rules.

**18.2 Forum.** Disputes arising out of or in connection with this DPA shall be resolved in the forum specified in the Parent Agreement, except that where Applicable Data Protection Law mandatorily reserves jurisdiction (for example, in favor of a Data Subject's habitual residence), that mandatory rule prevails.

**18.3 Jurisdictional override.** Where a per-jurisdiction addendum requires a particular governing law or forum (for example, the supervisory law applicable to Standard Contractual Clauses), that addendum prevails over this Section 18 to the extent of any conflict, in accordance with the order of precedence in Section 19.

**18.4 No hardcoded court.** This core DPA does not designate a specific court. The parties' chosen court is recorded in the Parent Agreement or the applicable addendum.

---

## 19. Order of precedence & miscellaneous

*Plain-language: This section says which document wins if two of the contracts say slightly different things, plus the usual housekeeping.*

**19.1 Order of precedence.** In the event of any conflict or inconsistency among the documents that govern the parties' relationship in respect of Processing, the following order of precedence applies, with each item taking precedence over those that follow it:

1. mandatory provisions of Applicable Data Protection Law;
2. Standard Contractual Clauses, the UK International Data Transfer Addendum, or any equivalent transfer instrument that the parties have incorporated;
3. any per-jurisdiction addendum to this DPA;
4. this DPA, including its annexes;
5. the Parent Agreement.

**19.2 Severability.** If any provision of this DPA is held to be invalid or unenforceable, that provision shall be modified to the minimum extent necessary to make it valid and enforceable, and the remaining provisions shall continue in full force and effect.

**19.3 No waiver.** A failure or delay by either party in exercising a right under this DPA does not waive that right.

**19.4 Assignment.** Neither party may assign this DPA without the other party's prior written consent, except that either party may assign this DPA to a successor in connection with a merger, acquisition, or sale of all or substantially all of its assets, provided the assignee is bound by terms no less protective than this DPA.

**19.5 Entire agreement on processing.** This DPA, together with the Parent Agreement and any per-jurisdiction addenda, is the complete and exclusive statement of the parties' agreement with respect to the Processing of Personal Data and supersedes all prior representations and agreements on that subject.

**19.6 Amendment.** This DPA may be amended only by a writing signed by authorized representatives of both parties, except that the Processor may update Annex 2 (TOMs) and Annex 3 (Sub-processor list) in accordance with Sections 8 and 9.

**19.7 Counterparts and electronic signature.** This DPA may be executed in counterparts, each of which is an original and all of which together constitute one instrument. Electronic signatures are valid and binding.

**19.8 Survival.** Sections 2, 5, 7, 12, 13, 15, 16, 17, 18, and 19, and any other provision that by its nature is intended to survive, survive termination of this DPA.

**19.9 Headings.** Section and subsection headings are for convenience only and do not affect interpretation.

---

## Annex 1 — Description of processing

*This Annex captures the Article 28(3) particulars and any equivalent particulars required by other Applicable Data Protection Law. The Controller is responsible for the accuracy of these particulars. The parties shall update this Annex as the Processing changes materially.*

| Particular | Value |
|---|---|
| Controller legal name | **{{Controller Legal Name}}** |
| Controller address | **{{Controller Address}}** |
| Controller privacy contact | **{{Controller Email Privacy}}** |
| Controller DPO contact (if applicable) | **{{Controller Email DPO}}** |
| Processor legal name | **{{Processor Legal Name}}** |
| Processor address | **{{Processor Address}}** |
| Processor privacy contact | **{{Processor Email Privacy}}** |
| Processor DPO contact (if applicable) | **{{Processor Email DPO}}** |
| Service | **{{Service Name}}** at **{{Service URL}}** |
| Subject matter of Processing | *The Processor's performance of the Services for the Controller, comprising [insert short description].* |
| Duration of Processing | *For the term of the Parent Agreement and any post-termination period required by Section 16.* |
| Nature of Processing | *[Insert nature: e.g., hosting, transmission, storage, analytics, support.]* |
| Purpose of Processing | *Enabling the Controller's lawful use of the Services and the Processor's performance of the Parent Agreement.* |
| Categories of Data Subjects | *[Insert: e.g., Controller's customers, end users, employees, contractors, prospects, other natural persons whose Personal Data the Controller submits.]* |
| Categories of Personal Data | *[Insert: e.g., identifiers, contact information, account credentials, technical data, content submitted by Data Subjects.]* |
| Special categories (if any) | *[Insert "None" if not applicable.]* |
| Frequency of Processing | *[Insert: continuous / on demand / batch.]* |
| Sensitive operations (e.g., automated decision-making) | *[Insert "None" if not applicable.]* |
| Retention period | *As described in the Parent Agreement and Section 16 of the DPA.* |
| Sub-processor list reference | **{{Subprocessor List URL}}** and Annex 3 |
| Transfer mechanism reference | Annex 4 and the applicable per-jurisdiction addendum |

---

## Annex 2 — Technical and organizational measures (TOMs)

*This Annex describes the security measures the Processor maintains. The Processor shall keep these measures under review and shall ensure that the overall level of protection is not materially diminished.*

**A2.1 Access control.** Identity and access management with unique accounts, role-based access control, the principle of least privilege, multi-factor authentication for administrative and remote access, periodic access reviews, and a documented joiner-mover-leaver process tied to HR systems.

**A2.2 Encryption at rest.** Encryption of Personal Data at rest using industry-recognized algorithms (such as AES-256 [VERIFY against current cryptographic guidance at deployment time]), with documented key management including key rotation, segregation of duties for key custodians, and protection of key material in a hardware security module or equivalent.

**A2.3 Encryption in transit.** Encryption of Personal Data in transit over public networks using current industry-standard transport protocols (such as TLS 1.2 or higher [VERIFY against current cryptographic guidance at deployment time]), with certificate management, deprecation of weak ciphers, and HSTS where applicable.

**A2.4 Pseudonymization.** Pseudonymization of Personal Data where technically appropriate, including the separation of identifiers from associated data, salted hashing for non-reversible references, and tokenization of high-risk fields.

**A2.5 Network security.** Defense-in-depth network architecture, including segmentation between trust zones, firewalls, intrusion detection and prevention, web application firewalls where applicable, denial-of-service protections, and continuous monitoring of perimeter and internal traffic.

**A2.6 Secure development.** A secure software development lifecycle that includes secure-by-design principles, peer code review, static and dynamic application security testing, dependency vulnerability scanning, secure coding training for engineers, and a documented change management process.

**A2.7 Vulnerability management.** Regular vulnerability scanning of infrastructure and applications, periodic third-party penetration testing (at least annually), risk-based prioritization, documented remediation timelines for critical and high-severity findings, and a coordinated disclosure program for externally reported vulnerabilities.

**A2.8 Incident response.** A documented incident response plan with defined roles, severity classification, escalation paths, customer notification procedures aligned with Section 12 of the DPA, post-incident review, and at least annual tabletop exercises.

**A2.9 Business continuity.** Documented business continuity and disaster recovery plans, with defined recovery time and recovery point objectives, redundant infrastructure across availability zones, regular backup testing, and at least annual recovery exercises.

**A2.10 Personnel training.** Onboarding and at least annual refresher training for personnel who Process Personal Data, covering the Processor's information security and privacy policies, secure handling of Personal Data, social-engineering awareness, and incident reporting.

**A2.11 Physical security.** Physical access controls at facilities used to Process Personal Data, including badge access, visitor logging, surveillance, and environmental controls. Where the Processor relies on third-party data centers, the Processor verifies that those facilities maintain comparable controls (for example through SOC 2, ISO/IEC 27001, or equivalent attestations).

**A2.12 Vendor management.** A vendor risk management program governing the selection, onboarding, and ongoing review of Sub-processors and other vendors that Process Personal Data, including due diligence proportionate to risk, contractual flow-down of obligations, and periodic reassessment.

**A2.13 Audit logging.** Audit logs covering authentication events, administrative actions, configuration changes, and access to Personal Data, with tamper-resistant storage, retention aligned with the Processor's documented log retention policy, and protection from unauthorized modification.

**A2.14 Data minimization.** Operational practices designed to ensure that the Processor Processes only the Personal Data necessary for the Services, including configuration defaults that favor minimization, periodic review of fields and retention, and the option for the Controller to disable optional Personal Data collection where supported by the Services.

---

## Annex 3 — Sub-processor list

*The Processor maintains an up-to-date Sub-processor list at **{{Subprocessor List URL}}**. The table below is a snapshot as of the Effective Date. The published list is the authoritative current version for the purposes of Section 9.*

| Sub-processor name | Address | Processing activity | Location of Processing | Transfer mechanism (if applicable) |
|---|---|---|---|---|
| *[Insert]* | *[Insert]* | *[Insert: e.g., infrastructure hosting, email delivery, payment processing, analytics]* | *[Insert country/region]* | *[Insert: e.g., adequacy decision, EU SCCs Module 3, UK IDTA, intra-group BCRs, none required]* |
| *[Insert]* | *[Insert]* | *[Insert]* | *[Insert]* | *[Insert]* |
| *[Insert]* | *[Insert]* | *[Insert]* | *[Insert]* | *[Insert]* |

---

## Annex 4 — International transfer mechanism

*This Annex is a jurisdiction-neutral placeholder. The applicable transfer mechanism is determined by the per-jurisdiction addendum that the parties incorporate by reference together with this DPA.*

**A4.1 Determination of mechanism.** Where Personal Data is the subject of a Restricted Transfer, the parties shall identify and incorporate, before the transfer occurs, the appropriate transfer mechanism under the originating jurisdiction's data protection law. The current selection is recorded below.

**A4.2 Selection (to be completed at deployment).**

| Originating jurisdiction | Selected mechanism | Reference document |
|---|---|---|
| EU/EEA | *[e.g., adequacy decision; EU SCCs 2021/914 Module __ ; binding corporate rules]* | *[Per-jurisdiction EU addendum]* |
| United Kingdom | *[e.g., adequacy regulations; UK IDTA; UK Addendum to the EU SCCs]* | *[Per-jurisdiction UK addendum]* |
| Switzerland | *[e.g., Federal Council adequacy list; Swiss SCC overlay]* | *[Per-jurisdiction Swiss addendum]* |
| Other | *[e.g., other jurisdictional mechanism]* | *[Per-jurisdiction addendum]* |

**A4.3 Reference to per-jurisdiction variant.** The substantive transfer-clause text (including any incorporated Standard Contractual Clauses, the UK International Data Transfer Addendum, or comparable instrument) is set out in the applicable per-jurisdiction addendum and is not duplicated here. Where the per-jurisdiction addendum and this core DPA conflict, the addendum prevails in accordance with Section 19.1.

---

## Merge fields used

The following Mustache merge fields appear in this DPA and must be filled before execution:

- `{{Controller Legal Name}}`
- `{{Controller Short Name}}`
- `{{Controller Address}}`
- `{{Controller Email Privacy}}`
- `{{Controller Email DPO}}`
- `{{Processor Legal Name}}`
- `{{Processor Short Name}}`
- `{{Processor Address}}`
- `{{Processor Email Privacy}}`
- `{{Processor Email DPO}}`
- `{{Service Name}}`
- `{{Service URL}}`
- `{{MSA Title}}`
- `{{MSA Effective Date}}`
- `{{Effective Date}}`
- `{{Last Updated Date}}`
- `{{Governing Law}}`
- `{{Subprocessor List URL}}`
- `{{Notification Window}}`
- `{{Breach Notification SLA}}`

---

## Authoritative references

The following permissively licensed sources were consulted as drafting guides only. No verbatim text was copied; this template is a clean-room original.

- Common Paper — Data Processing Agreement v1.0 and Standard DPA — `[CC-BY-4.0]` — https://commonpaper.com/standards/data-processing-agreement/
- Bonterms — Data Processing Agreement — `[CC-BY-4.0]` — https://bonterms.com/
- ICO (UK Information Commissioner's Office) — Sample Processor Contract / Article 28 controller-processor contract guidance — `[OGL]` — https://ico.org.uk/
- GitHub — `subprocessors.md` — `[CC0]` — https://github.com/github/site-policy/
- Mozilla — Data Processing Agreement and supporting policy texts — `[MPL-2.0]` — https://www.mozilla.org/about/legal/
- European Commission — Standard Contractual Clauses, Commission Implementing Decision (EU) 2021/914 — public domain — used for definitional alignment only; the SCC clauses themselves belong in the EU addendum, not this core baseline.

`[VERIFY]` flags in this document indicate items that should be checked against current authoritative guidance at the time of deployment:

- A2.2 — current cryptographic guidance for symmetric-key algorithms and key sizes (AES-256 baseline) `[VERIFY]`
- A2.3 — current cryptographic guidance for transport security protocol versions (TLS 1.2+ baseline) `[VERIFY]`

---

## Not legal advice

This template is a starting framework, not legal advice. It does not create a lawyer-client relationship, and it does not account for the specific facts of any organization, transaction, jurisdiction, or sector. Before signing any data processing agreement built from this template, the Controller and the Processor should each obtain advice from qualified privacy counsel admitted in the relevant jurisdictions, and should arrange review by a Data Protection Officer or equivalent privacy lead. Per-jurisdiction addenda (for example for the EU/EEA, the United Kingdom, Switzerland, California, or Brazil) must be incorporated where applicable; this jurisdiction-neutral baseline is not, on its own, a complete compliance solution.
