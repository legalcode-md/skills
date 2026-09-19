---
name: legalcode-fr-bail-commercial
description: Draft or review a French commercial lease (bail commercial) governed by the statut des baux
  commerciaux — Code de commerce Art. L145-1 to L145-60, as reformed by Loi Pinel 2014 and Décret 2014-1317.
  Use when reviewing a tenant's or landlord's draft bail commercial, negotiating renewal terms, assessing
  eviction indemnity entitlement, advising on rent revision disputes, or drafting a new bail commercial
  under French law.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Draft or review a French commercial lease (bail commercial) governed by the statut des baux commerciaux — Code de commerce Art. L145-1 to L145-60, as reformed by Loi Pinel 2014 and Décret 2014-1317. Covers the mandatory 9-year term and triennial break rights (Art. L145-4), rent review using ILC (Indice des Loyers Commerciaux) or ILAT (Indice des Loyers des Activités Tertiaires) with plafonnement and déplafonnement rules, lissage (10% annual cap), clause tunnel (Art. L145-39 at 25% indexation variance), renewal rights (renouvellement), refusal without indemnity (motif sérieux et légitime), eviction indemnity (indemnité d'éviction — Art. L145-14) calculation and components, lease assignment (cession du bail / cession du fonds de commerce — Art. L145-16), subletting (sous-location — Art. L145-31), charges and property tax allocation (Art. L145-40-2, Décret 2014-1317), propriété commerciale, déspécialisation partielle and plénière (Art. L145-47 to L145-55), and guarantees (dépôt de garantie, cautionnement). Use when reviewing a tenant's or landlord's draft bail commercial, negotiating renewal terms, assessing eviction indemnity entitlement, advising on rent revision disputes, or drafting a new bail commercial under French law. France-specific skill; not for residential leases (bail d'habitation), professional leases (bail professionnel), or bail dérogatoire exceeding 3 years.


# Legalcode — Bail Commercial (France)

> **Avertissement / Disclaimer**: Ce skill fournit un cadre pour l'assistance juridique par IA
> en matière de baux commerciaux français. Il ne constitue pas un conseil juridique. Toutes les
> sorties doivent être examinées par un avocat qualifié en droit immobilier commercial français
> ou un notaire habilité avant toute utilisation. Le droit des baux commerciaux évolue —
> vérifiez l'applicabilité actuelle des dispositions citées, notamment la jurisprudence de la
> Cour de cassation (3ème chambre civile). Les références aux articles de loi et à la
> jurisprudence provenant de la mémoire entraînent un risque d'hallucination — vérifiez sur
> légifrance.gouv.fr avant de vous y fier.
>
> **Disclaimer**: This skill provides a framework for AI-assisted French commercial lease
> drafting and review. It does not constitute legal advice. All outputs must be reviewed by a
> qualified French commercial property lawyer (avocat en droit immobilier) or authorised notary
> before use. French commercial lease law changes frequently — verify current applicability of
> all provisions cited. Statutory and case law references cited from memory carry hallucination
> risk — verify against légifrance.gouv.fr before relying on them.

---

## Purpose and Scope

This skill enables an AI agent to **draft and review** French commercial leases (baux
commerciaux) governed by the statut des baux commerciaux under the Code de commerce.

**Covers:**

- Clause-by-clause review of any bail commercial with GREEN / YELLOW / RED severity
  classification and bilingual redline generation
- Compliance check against Loi Pinel 2014 mandatory provisions and Décret 2014-1317 charges
- Rent revision analysis — ILC / ILAT index selection, plafonnement, déplafonnement, lissage,
  clause tunnel (Art. L145-39)
- Renewal strategy — renouvellement procedure, tacit renewal risk, congé formalities
- Eviction indemnity (indemnité d'éviction) analysis and indicative calculation
- Assignment and subletting assessment — Art. L145-16 statutory rights and contractual limits
- Charges and property tax allocation — Décret 2014-1317 exhaustive non-transferable list
- Déspécialisation partielle and plénière — procedure, landlord challenge rights, rent
  adjustment
- Guarantee structures — dépôt de garantie, cautionnement solidaire, garantie bancaire
- Drafting a new bail commercial from scratch, including all mandatory provisions
- Glass Box audit trail for traceability and auditability

**Does not:**

- Cover bail d'habitation (residential leases) or bail professionnel (professional leases)
- Apply to bail dérogatoire / bail précaire (max 3 years — Art. L145-5) in full depth
- Constitute a legal opinion on any specific situation
- Replace qualified French commercial property counsel or notarial advice

---

## Jurisdiction and Governing Law

**Jurisdiction: France (métropole and DOM-TOM).**

The bail commercial is governed by the **statut des baux commerciaux** — **Code de commerce,
Chapitre V (Art. L145-1 à L145-60)**, which constitutes mandatory public order law (ordre
public). Parties cannot derogate from its protections to the tenant's detriment unless
expressly authorised by the Code itself.

**Key governing texts:**

- **Code de commerce** — Art. L145-1 à L145-60 (statut des baux commerciaux)
- **Loi n° 2014-626 du 18 juin 2014** (Loi Pinel) — major reform of commercial lease law
- **Décret n° 2014-1317 du 3 novembre 2014** — implementing decree on charges, taxes, works
  distribution and triennial reporting obligations
- **Ordonnance n° 2016-131 du 10 février 2016** — reform of contract law (supplementary Code
  civil provisions now apply to bail commercial where not displaced by Code de commerce)
- **Code civil** — Art. 606 (major repairs / grosses réparations), Art. 1196 et seq.
  (supplementary obligations)
- **Code général des impôts** — treatment of pas-de-porte, droit au bail, rent supplements

**Applicable index framework (post-Loi Pinel, effective 1 September 2014):**

- **ILC (Indice des Loyers Commerciaux)** — for commercial and craft activities (commerçants
  RCS, artisans RM). Published quarterly by INSEE.
- **ILAT (Indice des Loyers des Activités Tertiaires)** — for tertiary service activities,
  offices, storage (not fitting RCS/RM merchant category). Published quarterly by INSEE.
- **ICC (Indice du Coût de la Construction)** — prohibited for triennial revision of new leases
  since 1 September 2014; may still appear in legacy leases predating Loi Pinel.

**Primary court (tribunal compétent):**

- **Tribunal judiciaire** du lieu de situation de l'immeuble — general jurisdiction over all
  bail commercial disputes.
- **Président du tribunal judiciaire (juge statuant seul)** — exclusive jurisdiction for rent
  revision disputes (Art. L145-38), rent fixing at renewal, clause d'indexation
  implementation, and rent adjustment following full déspécialisation.
- Territorial derogation clauses are valid only when both landlord and tenant are registered
  merchants (commerçants immatriculés RCS); void as against non-merchant parties.

---

## Interactive Clarification

This skill uses **interactive clarification** (⟁ CLARIFY) at key decision points where the
user's context materially changes the analysis, the applicable protections, or the drafting
direction. The skill pauses and asks when:

- Which party the user represents (bailleur / preneur) — this flips the entire analysis
- Whether the lease is a new draft or existing document under review
- Whether the tenant's activity qualifies for ILC or ILAT (or neither)
- Whether a bail dérogatoire was previously in place (conversion risk assessment)
- Whether renewal is approaching and what form of congé has been served
- Ambiguities in the clause on déspécialisation, charges inventory, or triennial break
  waiver require a binary decision the user must make

If the user has already supplied the information, skip the question and proceed. For
batch/non-interactive runs, state the assumption explicitly and flag it for human review.

---

## Workflow

### Step 1: Accept the Lease

Accept the bail commercial in any of these formats:

- **File**: PDF, DOCX, or other document format
- **Pasted text**: Lease text pasted directly into the conversation
- **Partial text**: User provides specific clauses for targeted analysis

If the user is drafting a new lease rather than reviewing an existing one, proceed to
Step 2 for context-gathering, then go directly to the Drafting Instructions section.

---

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user these questions:

1. **Which party do you represent?**
   - Options: Bailleur (landlord), Preneur (tenant), Both / Neutral analysis
   - _Why this matters_: Nearly every clause analysis reverses depending on which party you
     represent. What protects the tenant burdens the landlord. An uncapped eviction indemnity
     exposure is a tenant protection and a landlord risk — and vice versa.

2. **Task mode:**
   - Options: Review existing lease, Draft new lease from scratch, Negotiate renewal terms,
     Assess eviction indemnity entitlement, Dispute a rent revision, Analyse specific clause(s)
   - _Why this matters_: Determines which workflow steps are activated and how the output is
     structured.

3. **Tenant's commercial activity:**
   - _Why this matters_: Determines (a) whether the statut des baux commerciaux applies at
     all (requires RCS/RM registration or eligible activity), (b) which rent index applies
     (ILC for commerce/craft, ILAT for tertiary activities), and (c) which déspécialisation
     rules are relevant.
   - Ask for: nature of business, RCS or RM registration status, main SIC/NAF activity code.

4. **Current lease status and timeline:**
   - Options: Pre-execution (draft), Early term (< 3 years elapsed), Mid-term, Approaching
     triennial break, Approaching renewal, Post-congé (notice already served)
   - _Why this matters_: Determines urgency, which rights are immediately actionable, and
     whether any statutory deadlines are imminent (triennial break notice: 6 months advance;
     eviction indemnity claim: 2-year prescription from congé date).

5. **Key focus areas** (allow multiple selections):
   - Rent and indexation, Charges allocation, Triennial break rights, Renewal and congé,
     Assignment or subletting, Déspécialisation, Guarantees, Full clause-by-clause review
   - _Why this matters_: Allows the analysis to prioritise what matters most to the user
     while still flagging all RED items regardless of focus.

If the user provides partial context, proceed with what you have but **state your assumptions
explicitly** (e.g., "Je suppose que vous représentez le preneur — corrigez-moi si ce n'est
pas le cas"). Do not silently assume.

---

### Step 3: Identify Lease Status — Statut or Dérogatoire?

Before analysing the lease provisions, verify that the **statut des baux commerciaux** (Code
de commerce Art. L145-1) applies. If it does not, the entire analysis framework changes.

**Conditions for the statut to apply (Art. L145-1):**

| Condition                 | What to Verify                                                                                                                                                                                                                                                                                                      |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Party qualification**   | Tenant must be (a) a merchant (commerçant) registered at RCS, or (b) an artisan registered at RM, or (c) a company registered at RCS. Professions libérales and farmers are excluded unless expressly extended by the lease.                                                                                        |
| **Business exploitation** | Tenant must operate a fonds de commerce (clientele, goodwill) from the premises. A purely administrative office or storage-only use without customer contact may not qualify.                                                                                                                                       |
| **Premises registration** | The premises must correspond to the address registered with RCS/RM and where the fonds de commerce is actually exploited.                                                                                                                                                                                           |
| **Lease term**            | If the lease was written as a bail dérogatoire (Art. L145-5, max 3 years), and the tenant has remained beyond 1 month after expiry without a new bail dérogatoire being signed, a standard 9-year bail commercial has automatically been created by operation of law — assess whether this conversion has occurred. |

**⟁ CLARIFY** — If any condition is uncertain:

- "Is the tenant registered at RCS or RM? If not, the statut des baux commerciaux may not
  apply and a different lease type (bail professionnel, bail civil) governs. Please confirm."
- "Was a bail dérogatoire previously in place? If yes, has it expired and has the tenant
  remained beyond 1 month? If so, a 9-year bail commercial may already have been created
  by Art. L145-5 — this is a material risk to assess immediately."

---

### Step 4: Gather Legal Authority

Use **legalcode-mcp** to build a working legal reference file for this review.

**Research process:**

1. Search for the current text of Code de commerce Art. L145-1 to L145-60 and any recent
   amendments.
2. Search for recent Cour de cassation (3ème chambre civile) decisions on:
   - Triennial break notice formalities
   - Plafonnement / déplafonnement criteria (modification des facteurs locaux de commercialité)
   - Charges allocation enforceability under Décret 2014-1317
   - Eviction indemnity calculation methodology
   - Déspécialisation procedure and landlord challenge rights
   - Clause résolutoire enforcement and délai de grâce
3. Search for current ILC and ILAT index values (INSEE, most recent quarter).
4. Save results to `/tmp/legalcode-bail-commercial-authority.md`.

**If legalcode-mcp is not connected:**

- Mark all statutory references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Proceed with the analysis using general knowledge of French commercial lease law
- Flag all ILC/ILAT index values as requiring verification against current INSEE data

---

### Step 5: Clause-by-Clause Analysis

Analyse the lease systematically. Read the **entire document** before flagging issues —
clauses interact (e.g., a broad charges clause may be partially invalidated by Décret
2014-1317; a déspécialisation restriction may be void if it prevents the exercise of a
statutory right).

**⟁ CLARIFY** — For long leases (50+ pages) or leases with multiple schedules (états des
lieux, inventaires de charges, actes additionnels):

- Ask whether to perform a **full review** of all 14 clause categories or a **priority
  review** focused on the user's stated focus areas plus all RED items.
- If the lease incorporates external documents by reference (e.g., règlement de copropriété,
  charging schedule), ask whether those documents are available for review.

Analyse all 14 clause categories below. For each, assess compliance with mandatory law and
flag deviations.

| #   | Clause Category                       | Depth    | Key Review Points                                                                                                                                                                                             |
| --- | ------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Champ d'application et Parties**    | Deep     | RCS/RM registration status; fonds de commerce; correct legal entity names; capacity                                                                                                                           |
| 2   | **Durée et Terme**                    | Deep     | 9-year minimum; bail dérogatoire conversion risk; fixed-term vs. indefinite after tacit renewal                                                                                                               |
| 3   | **Résiliation Triennale**             | Deep     | Tenant's right under Art. L145-4; notice form (acte extrajudiciaire or LRAR); 6-month notice period; valid waiver or restriction clauses; retirement/invalidity exceptions                                    |
| 4   | **Loyer Initial et Révision**         | Deep     | Initial rent; index selected (ILC / ILAT / ICC); triennial revision (Art. L145-38); plafonnement; déplafonnement criteria; lissage (10% cap); clause tunnel (Art. L145-39 at 25%)                             |
| 5   | **Destination des Locaux**            | Deep     | Scope of permitted activity; exclusivity clauses; déspécialisation rights (Art. L145-47 to L145-55); restrictions on change of activity                                                                       |
| 6   | **Cession et Sous-Location**          | Deep     | Art. L145-16 assignment rights (cession fonds / cession bail); prohibition clauses and their limits; 3-year assignor guarantee cap; subletting prohibition (Art. L145-31); landlord participation requirement |
| 7   | **Charges et Taxe Foncière**          | Deep     | Inventory completeness (Art. L145-40-2 mandatory); non-transferable charges (Décret 2014-1317); taxe foncière allocation; annual statement obligation (by 30 Sept); triennial works reporting                 |
| 8   | **Travaux et Entretien**              | Deep     | Art. 606 CC major repairs (bailleur); routine repairs (preneur); allocation of refurbishment / compliance works; état des lieux obligations                                                                   |
| 9   | **Garanties**                         | Standard | Dépôt de garantie amount and capping; cautionnement solidaire (guarantor, scope, duration); garantie bancaire; renewal of guarantees at lease renewal                                                         |
| 10  | **Renouvellement et Congé**           | Deep     | Art. L145-8 et seq. renewal rights; congé formalities (acte extrajudiciaire; 6 months; end of calendar quarter); tacit renewal risk; grounds for refusal; motif sérieux et légitime                           |
| 11  | **Indemnité d'Éviction**              | Deep     | Art. L145-14 entitlement; Art. L145-17 grounds to avoid payment; components of indemnity (valeur marchande, déménagement, frais de transfert); 2-year prescription from congé; right to remain (Art. L145-28) |
| 12  | **Clause Résolutoire et Résiliation** | Standard | Clause résolutoire conditions and procedure; commandement de payer (1-month notice); référé TJ; délai de grâce (Art. L145-41)                                                                                 |
| 13  | **Assurances**                        | Standard | Landlord building insurance; tenant contents / liability / business interruption; mutual coverage requirements; notification obligations                                                                      |
| 14  | **Dispositions Générales**            | Standard | Governing law and court (TJ lieu de l'immeuble); territorial jurisdiction clause validity; notices; amendments; entire agreement (intégralité des accords)                                                    |

---

### Step 6: Missing Clause Detection

After analysing the clauses present, identify important provisions entirely absent from the
lease. A missing clause can be as material as a defective one — and some omissions
automatically invalidate linked provisions.

**Mandatory provisions under Loi Pinel / Décret 2014-1317 — if absent, flag RED:**

| Missing Element                                                              | Severity | Risk if Absent                                                                               |
| ---------------------------------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------- |
| Precise inventory of charges, taxes, and works (Art. L145-40-2)              | RED      | Charges clause unenforceable; all costs default to landlord                                  |
| Annual charges statement obligation (by 30 Sept)                             | RED      | Landlord loses right to regularise charges; disputed amounts                                 |
| Triennial works statement obligation (within 2 months of 3-year anniversary) | YELLOW   | Landlord loses right to pass forward-looking works costs                                     |
| Index clause specifying ILC or ILAT                                          | RED      | If ICC retained post-Sept 2014, triennial revision provision may be void                     |
| Lissage clause (10% annual cap on déplafonnement)                            | YELLOW   | Lissage applies by law regardless, but omission creates disputes                             |
| État des lieux at entry and exit                                             | YELLOW   | Presumption that premises returned in same condition as delivered (tenant's burden to rebut) |

**Common gaps in tenant-drafted leases:**

- No explicit triennial break notice procedure → dispute risk on formalities
- No Art. L145-39 clause tunnel → tenant/landlord must rely on Art. L145-39 anyway (public
  order), but explicit language avoids disputes

**Common gaps in landlord-drafted leases:**

- No charges inventory → all charges default to landlord under Décret 2014-1317
- Charges clause broader than Décret 2014-1317 → excess charges void

**⟁ CLARIFY** — When severity of absence depends on context:

- "This lease has no charges inventory as required by Art. L145-40-2. This means the charges
  clause is likely unenforceable in its entirety and all charges default to the landlord. Is
  this lease already signed and in force, or is this a draft that can still be corrected?"
- "There is no congé clause addressing the form of notice required. The statutory default
  (acte extrajudiciaire) applies. Does your client need to serve notice imminently, in which
  case this is urgent?"

---

### Step 7: Flag Deviations

Classify each deviation using the four-tier system in the **Severity Classification** section
below. For each deviation:

- **GREEN**: Note for awareness.
- **YELLOW**: Generate specific redline language, provide a fallback position, and explain the
  business/legal impact of accepting vs. negotiating.
- **RED**: Explain the specific risk (citing the legal basis), provide market-standard
  alternative language, estimate exposure, and recommend action.
- **CRITIQUE**: Flag immediately for urgent legal action — cannot be remedied by redline alone.

**⟁ CLARIFY** — For borderline classifications:

- "This charges clause attempts to pass the cost of major structural repairs (Art. 606 CC)
  to the tenant. This is void under Décret 2014-1317. Should I treat this as RED (void clause
  requiring deletion) or CRITIQUE (ongoing payments may need recovery)?"
- "The lease prohibits triennial breaks for the first 9 years. This waiver of Art. L145-4
  rights is only valid for leases of initial duration exceeding 9 years, leases of offices, or
  leases of storage-only premises. Does this lease exceed 9 years or fall within an exception?"

---

### Step 8: Rent Revision Deep-Dive

When the user's focus includes rent and indexation, perform this additional analysis:

1. **Index audit**: Identify the index clause (ILC, ILAT, or ICC). If ICC is used in a lease
   signed after 1 September 2014, flag RED — ICC is prohibited for triennial revision of new
   leases since Loi Pinel.

2. **Triennial revision timeline**: Calculate the next revision date from the lease start date
   or last revision. If within 6 months, flag as time-sensitive.

3. **Plafonnement vs. déplafonnement**: Assess whether déplafonnement conditions are met:
   - Has there been a **modification notable des facteurs locaux de commercialité** (pedestrian
     traffic change, new transport link, nearby development, demographic shift)?
   - Has the modification caused a **more than 10% change in rental value** (valeur locative)?
   - Both conditions must be met (Cass. Civ. 3ème, 18 September 2025, n°24-13488 [VERIFY]).
   - If déplafonnement applies: lissage caps annual increase at 10% of prior year's rent.

4. **Clause tunnel** (Art. L145-39): If cumulative indexation causes a variance of >25% from
   the contractually fixed rent, either party may demand judicial revision to market rental
   value (valeur locative), subject to the 10% annual lissage cap.

5. **Valeur locative reference criteria** (Art. L145-33): If judicial revision to market value
   is at issue, the valeur locative is determined by reference to: characteristics of the
   premises, local economic conditions, advantages granted to the tenant, obligations borne by
   the tenant, and prices practised for comparable premises in the vicinity.

---

### Step 9: Renewal and Eviction Strategy

When approaching renewal or post-congé scenarios, apply this additional framework:

**If renewal is approaching (bailleur perspective):**

1. Calculate the congé deadline: 6 months before the end of a calendar quarter at or after the
   9-year (or renewal) term expires. Serve by acte extrajudiciaire.
2. If refusing renewal: identify the ground. Is it Art. L145-17 (motif sérieux et légitime —
   no indemnity) or a commercial decision (indemnity required)?
3. If Art. L145-17 applies: verify that the breach was preceded by a mise en demeure and that
   the breach continued or resumed >1 month after that notice.
4. Quantify the indemnity d'éviction exposure if renewal is refused commercially.

**If renewal is approaching (preneur perspective):**

1. Assess whether a demande de renouvellement has been served (or should be) by acte
   extrajudiciaire within 6 months before lease expiry.
2. Check for tacit renewal (reconduction tacite) risk: if the 9-year term expired without
   congé from either party, the lease has renewed indefinitely — either party may now give
   6 months' notice ending on the last day of a calendar quarter.
3. If the landlord has refused renewal: assess (a) whether a motif sérieux et légitime exists
   to deny indemnity, and (b) the quantum of indemnité d'éviction.

---

## Clause Analysis — Deep Topics

### 1. Durée et Résiliation Triennale

**Legal framework:** Art. L145-4 and L145-5 Code de commerce.

**9-year minimum rule:**

- The bail commercial must be at least 9 years (Art. L145-4). This is mandatory public order —
  any clause purporting to reduce duration below 9 years is deemed unwritten (réputée non
  écrite).
- Bail dérogatoire exception (Art. L145-5): parties may agree a short-term lease of maximum
  3 years total duration, derogating entirely from the statut des baux commerciaux. Once the
  3-year maximum is reached (even across successive bails dérogatoires), and the tenant
  remains beyond 1 month after expiry, a 9-year commercial lease arises automatically by law.

**Triennial break (résiliation triennale):**

- The tenant has a statutory right to give notice at the expiry of each 3-year period (Art.
  L145-4). This right cannot be contractually excluded, except:
  - Leases with an initial term **exceeding 9 years** (can waive triennial break by express
    clause)
  - Leases of **office-exclusive premises** (locaux à usage exclusif de bureaux)
  - Leases of **storage premises** (entrepôts)
  - Leases of a **single-use property** (monovalent)
- Notice requirements: **6 months in advance** of the triennial period end; served by **acte
  extrajudiciaire** (huissier/commissaire de justice) or registered letter with
  acknowledgement of receipt (lettre recommandée avec avis de réception — LRAR). Acte
  extrajudiciaire is strongly preferred to avoid formal validity challenges.
- **Retirement / invalidity exception** (Art. L145-4 al. 2): A tenant who has retired or
  receives invalidity benefits may give notice at any time, not just at triennial intervals,
  with 6 months' advance notice. The same right extends to heirs upon tenant's death, and to
  sole shareholders of EURL or majority gérants of SARL who have held their position for ≥2
  years.

**Review checkpoints:**

- Is the triennial break right expressly preserved, or is there an attempt to exclude it
  outside of the permitted exceptions?
- Is the notice procedure specified? If acte extrajudiciaire is not required, LRAR is valid
  but creates evidentiary risk.
- Does the lease purport to require the tenant to give more than 6 months' notice? If so,
  any excess beyond 6 months is void (ordre public).

---

### 2. Loyer et Révision

**Legal framework:** Art. L145-33 to L145-40 Code de commerce.

**Index selection:**

- **ILC**: For tenants exercising commercial or craft activities (commerçants RCS / artisans
  RM). Published quarterly by INSEE. [VERIFY current value at time of review]
- **ILAT**: For tertiary service activities, logistics, professional offices. Published
  quarterly by INSEE. [VERIFY current value at time of review]
- **ICC**: Prohibited for triennial revision in leases signed after 1 September 2014 (Loi
  Pinel). Legacy leases may still reference ICC — flag for renegotiation at renewal.

**Triennial revision (révision légale — Art. L145-38):**

- Either party may demand rent revision at the expiry of each 3-year period from the initial
  lease date or last contractual renewal.
- Revision takes effect from the date of the demand (not the date of the tribunal decision).
- **Plafonnement rule**: New rent is capped at the variation of the applicable index (ILC or
  ILAT) between the last revision and the current demand. Even if the market rental value
  (valeur locative) has risen significantly, the index cap applies.
- **Déplafonnement exception** (Art. L145-34): Plafonnement does not apply if there has been
  a **modification notable des facteurs locaux de commercialité** that has had a favourable
  impact (>10% change in rental value) on the tenant's business. The landlord bears the
  burden of proving both the modification and the >10% impact.
  - Examples of local commercial factors: new public transport, pedestrian traffic change,
    significant nearby retail development, urban regeneration project, change in consumer
    demographics.
  - The Cour de cassation has confirmed that the change must have had a favourable impact
    specifically on the tenant's activity at this location (Cass. Civ. 3ème, 18 September
    2025, n°24-13488 [VERIFY]).
- **Lissage du déplafonnement** (Loi Pinel 2014): Even when déplafonnement is justified, the
  rent increase is capped at **10% of the prior year's rent per year** until the market rent
  level is reached. This lissage applies by operation of law and cannot be waived.

**Conventional indexation clause (clause d'échelle mobile):**

- Parties frequently include annual indexation tied to ILC or ILAT.
- **Clause tunnel (Art. L145-39)**: When cumulative indexation causes a variance of >25%
  (upward or downward) from the contractually fixed rent, either party may petition the
  President of the Tribunal judiciaire for a revision to current market rental value (valeur
  locative). The 10% lissage cap applies even to clause tunnel revisions.
- This right is ordre public — it cannot be contractually waived.

**Review checkpoints:**

- Is the index clause ILC or ILAT (appropriate to the tenant's activity)? RED if ICC is used
  in a post-September 2014 lease.
- Is the triennial revision timing correctly calculated from the initial entry date?
- Does the lease correctly reflect the lissage cap? Absence does not invalidate lissage
  (statutory) but causes disputes.
- Is the clause tunnel (Art. L145-39) included or at least not excluded?

---

### 3. Charges et Taxe Foncière

**Legal framework:** Art. L145-40-2 Code de commerce; Décret n° 2014-1317 du 3 novembre 2014.

**Mandatory inventory (Art. L145-40-2):**

- The lease **must** contain a precise and exhaustive inventory of all charges, taxes, duties,
  and works, distributed by category between landlord and tenant. A provision that does not
  comply with this requirement is deemed unwritten (réputée non écrite) — meaning no charges
  can be recovered from the tenant for categories not precisely listed.
- The landlord must provide an **annual expense statement** (état des charges) by 30 September
  of the following year (or 3 months after year-end for co-owned properties).
- The landlord must provide a **triennial works statement** within 2 months of each 3-year
  anniversary: (a) completed works in the prior 3 years with costs; (b) planned works in the
  next 3 years with budget estimates.

**Non-transferable charges (Décret 2014-1317 — exhaustive list of what landlord must bear):**

| Category                                | Non-Transferable to Tenant                                                                                |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Property management                     | Landlord's fees for rent collection and property management                                               |
| Major repairs                           | Art. 606 CC grosses réparations (structure, roof, foundations, main walls)                                |
| Compliance works                        | Works to remedy obsolescence or bring premises into regulatory compliance when constituting major repairs |
| Vacant space costs                      | Charges attributable to vacant parts of the building or to other tenants                                  |
| Territorial Economic Contribution (CET) | Where the landlord is the taxpayer                                                                        |
| Co-ownership charges                    | Where the landlord is the sole owner of the ground floor and common parts                                 |

**Transferable charges (tenant can be required to pay):**

- **Taxe foncière** (property tax): may be passed to tenant by express lease clause — this is
  one of the most commercially significant items. If the lease is silent, taxe foncière
  defaults to the landlord. Verify: is taxe foncière clearly included in the charges clause
  with annual statement obligations?
- Taxes and duties related to use of premises or services from which the tenant benefits
- Utilities (electricity, water, gas, heating)
- Routine maintenance and repairs (excluding Art. 606 CC major repairs)
- Cleaning, security, fire safety equipment maintenance, elevator maintenance
- Building insurance (or the tenant's proportionate share in multi-tenant buildings)

**Review checkpoints:**

- Is the charges inventory attached to the lease as a schedule? If not, flag RED.
- Does the charges clause attempt to pass any of the Art. 606 CC / Décret 2014-1317
  non-transferable items to the tenant? If yes, those provisions are void.
- Is taxe foncière explicitly included in transferable charges with a proper reference?
- Is the annual statement obligation (30 September deadline) specified?
- Is the triennial works statement obligation (2-month deadline per anniversary) specified?

---

### 4. Destination des Locaux et Déspécialisation

**Legal framework:** Art. L145-47 to L145-55 Code de commerce.

**Destination clause:**

- The lease must specify the authorised activity (destination) of the premises. The tenant
  may only carry out activities within the contractually defined destination, unless the
  déspécialisation procedure is followed.
- Broad destination clauses ("toutes activités commerciales") give the tenant maximum
  flexibility and reduce déplafonnement risk; narrow clauses expose the tenant to need for
  déspécialisation.

**Déspécialisation partielle (Art. L145-47):**

- The tenant may add activities that are complementary or ancillary to those in the lease
  (e.g., a florist adding gifts and stationery).
- Procedure: tenant notifies landlord by LRAR or acte extrajudiciaire specifying the new
  activities. Landlord has **2 months to contest** (forfeiture if silent). The Tribunal
  judiciaire decides if contested.
- Landlord may claim a rent increase if the partial déspécialisation materially enhances the
  commercial value of the premises.

**Déspécialisation plénière (Art. L145-48 to L145-55):**

- The tenant may entirely change the destination of the premises to a different type of
  activity, on the grounds of rational organisation of the commercial distribution in the
  area, or the evolution of the neighbourhood's commercial character.
- The tenant must demonstrate that the new activities are compatible with the premises and
  neighbourhood and that local economic and commercial conditions justify the change.
- Procedure: notification by acte extrajudiciaire; landlord has 2 months to contest; silence
  = acceptance; Tribunal judiciaire decides if contested.
- Landlord may claim a rent increase; co-tenants may claim compensation if the change
  affects shared commercial factors.
- Tenant may withdraw the déspécialisation request at any time until 15 days after a final
  judgment; tenant bears all costs if withdrawing.

**Review checkpoints:**

- Is the destination clause drafted broadly enough for the tenant's current and anticipated
  future activities?
- Does the lease purport to exclude or restrict déspécialisation rights beyond what the Code
  permits?
- If a narrow destination clause is proposed, advise the tenant to consider requesting a
  broader clause or a déspécialisation partielle clause.

---

### 5. Cession et Sous-Location

**Legal framework:** Art. L145-16 and L145-31 Code de commerce.

**Cession du bail / cession du fonds de commerce (Art. L145-16):**

- **Clauses prohibiting assignment to a purchaser of the fonds de commerce are void** (Art.
  L145-16, alinéa 1 — réputées non écrites). The landlord cannot prevent the tenant from
  assigning the lease as part of a business sale.
- However, the landlord may require prior notification and the right to oppose the
  assignee on legitimate grounds (e.g., assignee's financial incapacity).
- **Assignor's ongoing guarantee**: If the lease requires the assignor to guarantee the
  assignee's obligations, this guarantee is **limited to a maximum of 3 years** from the
  assignment date (Art. L145-16-2). Any clause extending the guarantee beyond 3 years is
  void for the excess period.
- **Company mergers, divisions, and universal asset transfers** (apports d'universalité)
  automatically substitute the new entity as lessee without triggering assignment formalities.

**Sous-location (Art. L145-31):**

- All subletting (partial or total) is **prohibited** unless expressly authorised by the
  landlord.
- If the landlord authorises subletting: the landlord must **participate in the subletting
  agreement** (être partie à l'acte or signatory). A sublease without landlord participation
  in the deed is void.
- The landlord may impose conditions: minimum subrent, use restrictions, notification
  obligations.
- **Rent cap on subletting**: If the agreed subrent exceeds the head lease rent, the landlord
  may demand a corresponding increase in the head lease rent at the next triennial revision.

**Review checkpoints:**

- Does the lease contain a total prohibition on assignment, even with the fonds de commerce?
  If yes, this prohibition is void for cession du fonds — flag as misleading / void clause.
- Does the lease correctly limit the assignor's guarantee to 3 years maximum?
- Does the subletting clause require landlord participation in the subletting agreement? If
  the clause merely requires landlord consent without participation, it is below the statutory
  minimum — any sublease under such a clause may be void.

---

### 6. Renouvellement, Congé et Propriété Commerciale

**Legal framework:** Art. L145-8 to L145-17 Code de commerce.

**Propriété commerciale:**

- The statut grants the tenant a right to the **renewal of the lease** at the end of each
  term — this is the foundation of propriété commerciale. The tenant's business and clientele
  derive economic value from this security of tenure.
- The lease right (droit au bail) has economic value separate from the business goodwill
  (fonds de commerce) — it represents the difference between actual rent and market rent when
  actual < market.

**Congé — notice to quit (Art. L145-9):**

- Either party may give congé: minimum **6 months in advance**, expiring at the **end of a
  calendar quarter** (dernier jour du trimestre civil).
- Form: **acte extrajudiciaire** (commissaire de justice). Registered letter is legally valid
  under the Cour de cassation's interpretation, but acte extrajudiciaire is the standard in
  practice and avoids all formality challenges.
- The landlord's congé must state whether renewal is offered or refused and, if refused, on
  what grounds.

**Tenant's renewal demand (Art. L145-10):**

- The tenant may serve a demande de renouvellement by acte extrajudiciaire or LRAR in the
  last 6 months before the lease expires, or at any time during tacit renewal.
- The landlord must respond within 3 months — silence is deemed acceptance of renewal.

**Tacit renewal (reconduction tacite):**

- If neither party serves congé or a renewal demand, the lease continues **indefinitely** at
  the end of its fixed term under the existing terms. Either party may then give 6 months'
  congé expiring at the end of a calendar quarter.
- Tacit renewal does not reset the rent to market value — the statutory triennial revision
  mechanism applies.

**Refusal to renew without indemnity (Art. L145-17 — motif sérieux et légitime):**

- The landlord may refuse renewal without paying eviction indemnity only if there is a
  **motif sérieux et légitime** — a serious and legitimate ground. This concept is undefined
  by statute; courts exercise sovereign appreciation.
- Must be preceded by a formal notice to remedy (mise en demeure) where the ground is non-
  performance of lease obligations, and the breach must continue or resume >1 month after the
  mise en demeure.
- Examples recognised by courts: concealed subletting without authorisation, unapproved
  change of destination, degradation of premises, employment of undeclared workers.
- Note: the ground need not be a breach of the lease — it can be any conduct that makes
  renewal incompatible with the landlord's legitimate interests.

---

### 7. Indemnité d'Éviction

**Legal framework:** Art. L145-14, L145-28, and L145-30 Code de commerce.

**Entitlement:**

- If the landlord refuses renewal (without a motif sérieux et légitime), the tenant is
  entitled to an **indemnité d'éviction** designed to fully compensate all loss caused by
  the non-renewal.

**Calculation components:**

- **If the tenant can relocate and re-establish the business elsewhere:**
  - **Valeur marchande du fonds de commerce** (market value of the business as a going concern)
    — calculated by reference to turnover, goodwill, net assets, and market comparables.
  - Alternatively: **Valeur du droit au bail** (if this exceeds business value) — the economic
    value of the lease right (market rent minus actual rent × years remaining).
  - **Frais de déménagement** (removal costs).
  - **Frais de réinstallation** (reinstallation and fit-out costs at new premises).
  - **Droits de mutation** (transfer taxes and fees for comparable premises, unless the
    landlord proves actual prejudice is lower).
  - **Perte de clientèle transitoire** (transitional loss of clientele during move).

- **If the tenant cannot relocate (clientele is location-specific):**
  - **Full value of the fonds de commerce**, including the entire goodwill attributed to the
    location — because the tenant effectively loses the entire business.
  - Additional items: loss of future profits, business closure costs.

**Tenant's right to remain (Art. L145-28):**

- The tenant **cannot be compelled to vacate** until the eviction indemnity has been paid (or
  consigned by the landlord with the Caisse des dépôts). The tenant continues to occupy under
  the original lease terms during this period.
- The landlord owes an **indemnité d'occupation** during this period — typically set at market
  rental value by the court.

**Prescription:**

- The tenant has **2 years from the date the congé was served** to claim the eviction
  indemnity before the Tribunal judiciaire. Failure to claim within 2 years extinguishes the
  right.

**Review checkpoints:**

- Has a congé refusing renewal been received? Flag the 2-year claim deadline immediately.
- Does the lease include any clause purporting to limit the eviction indemnity? Such clauses
  are void (ordre public).
- If the landlord invokes Art. L145-17 (motif sérieux et légitime), was a mise en demeure
  served and did the breach continue >1 month?

---

### 8. Garanties

**Types of guarantee:**

- **Dépôt de garantie**: Cash deposit held by landlord, returned at lease end net of deductions
  for outstanding obligations. No statutory cap on amount in commercial leases (unlike
  residential). Common market practice: 2-3 months' rent. If held for more than 2 months'
  rent, interest at the statutory rate (taux d'intérêt légal) accrues to the tenant (Art.
  L145-40 Code de commerce [VERIFY current article text]).
- **Cautionnement solidaire**: A third party (corporate parent, shareholder, or individual)
  guarantees all of the tenant's obligations under the lease. In commercial leases, the scope,
  duration, and cap must be carefully negotiated — there is no equivalent of the residential
  "Acte Bouygues" limitation.
- **Garantie bancaire**: Bank guarantee — typically on-demand (garantie autonome), easier for
  the landlord to call but requires tenant to maintain bank facilities.

**Review checkpoints:**

- Is the dépôt de garantie return obligation clearly stated (timeline, conditions for
  deductions)?
- Does the cautionnement solidaire expire at lease expiry, or does it extend through any
  tacit renewal? If it extends indefinitely, this is onerous for the guarantor — flag YELLOW.
- Is the cautionnement limited to the original lease term, or does it cover renewal and
  déspécialisation?

---

## Severity Classification System

### GREEN — Conforme / Aucune action requise

The clause:

- Complies with mandatory Code de commerce provisions (Loi Pinel, Décret 2014-1317)
- Falls within market practice for French commercial leases
- Creates no elevated legal risk for the user's client

**Action**: Note for awareness only. No redline needed.

---

### YELLOW — À améliorer / Négocier

The clause:

- Is technically valid but creates elevated risk or falls below best practice
- Could be improved without materially changing the commercial deal
- Is common in the market but not optimal for the user's client

**Action**: Generate alternative language. Explain the specific risk. Recommend negotiation
before signature or correction at the next contractual update.

**Examples:**

- LRAR used for triennial break notice instead of acte extrajudiciaire (valid but creates
  formality risk)
- Déspécialisation restricted beyond statutory permitted scope (may be void but creates
  dispute risk)
- Cautionnement solidaire extending indefinitely through all renewals (onerous but not void)
- No explicit lissage clause (statutory lissage applies regardless, but absence causes
  disputes)

---

### RED — Non-conforme / Corriger avant signature

The clause:

- Violates a mandatory Code de commerce provision, Loi Pinel rule, or Décret 2014-1317
  requirement
- Is void (réputée non écrite) or unenforceable under French commercial lease law

**Automatic RED triggers — any one of these:**

- [ ] Lease term shorter than 9 years without valid bail dérogatoire framework
- [ ] Complete prohibition on cession du bail upon sale of the fonds de commerce (Art. L145-16
      — void)
- [ ] Assignor's guarantee purporting to exceed 3 years (Art. L145-16-2 — void for excess)
- [ ] No charges inventory attached or incorporated by reference (Art. L145-40-2 — clause
      unenforceable)
- [ ] Charges clause purporting to pass Art. 606 CC major repairs to tenant (Décret 2014-1317
      — void)
- [ ] ICC index used for triennial revision in a lease signed after 1 September 2014
- [ ] Subletting purportedly authorised without landlord participation in the agreement (Art.
      L145-31 — sublease void)
- [ ] Triennial break right excluded in a standard 9-year lease that is not offices, storage,
      or monovalent (Art. L145-4 — clause void)
- [ ] Eviction indemnity contractually capped or excluded (Art. L145-14 — void)
- [ ] Clause tunnel (Art. L145-39 >25% indexation variance) contractually excluded (public
      order — void)

**Action**: Explain the specific risk with citation. Provide compliant alternative language.
Recommend immediate correction.

---

### CRITIQUE — Action juridique urgente requise

The defect:

- Creates immediate or imminent legal liability, procedural deadline, or right forfeiture
- Cannot be remedied by contract amendment alone
- Requires urgent intervention by qualified counsel

**Examples:**

- Congé refusing renewal has been served and the 2-year eviction indemnity prescription
  (Art. L145-14) is approaching expiry
- Bail dérogatoire has expired >1 month ago and the tenant remains in occupation — a 9-year
  commercial lease has arisen by operation of law; landlord may not realise this
- A commandement de payer has been served under the clause résolutoire and the 1-month cure
  period is running
- A triennial break notice has been received and the 6-month notice period is in progress

---

## Prioritization Framework

### Tier 1 — Avant signature / Action immédiate

Must-resolve items. If unaddressed, the lease (or specific clause) is void, unenforceable,
or creates material immediate liability:

- All RED automatic triggers (void or unlawful provisions)
- All CRITIQUE items (procedural deadlines, imminent rights)
- Missing mandatory charges inventory (Art. L145-40-2)
- Wrong index (ICC post-September 2014)

---

### Tier 2 — Dans les 30 jours / Lors de la prochaine réunion

Should-resolve items. Valid but suboptimal; if unaddressed, creates elevated risk without
immediate legal consequence:

- YELLOW items on rent revision, triennial break formalities, or subletting
- Cautionnement scope and duration issues
- Missing lissage clause (statutory application is a backstop, but clarity prevents disputes)
- Annual and triennial statement obligations not expressly included

---

### Tier 3 — À la prochaine révision contractuelle

Nice-to-have improvements. Minimal risk if deferred:

- Green improvements that optimise negotiating positions
- Drafting clarity enhancements that have no legal consequence if absent
- Best-practice clauses not required by statute

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivery.

| Gate           | Rule                                                                                                                                                                           | Fail Action                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific Code de commerce article, Décret 2014-1317 provision, or Cour de cassation decision                                                         | Add citation or mark "[VÉRIFIER — source non confirmée]" |
| **Format**     | All citations follow French legal citation format: Art. L145-XX Code de commerce; Cass. Civ. 3ème, [day] [month] [year], n°[number]; Décret n° 2014-1317                       | Fix format                                               |
| **Currency**   | Every cited provision checked against légifrance.gouv.fr for amendments; ILC/ILAT index values verified against current INSEE publication                                      | Flag "[VÉRIFIER LA VALEUR ACTUELLE]"                     |
| **Domain**     | Analysis stays within French commercial lease law; do not apply residential lease rules (bail d'habitation), professional lease rules, or foreign commercial property concepts | Remove or flag domain bleed                              |
| **Confidence** | Uncertainty explicitly stated; ambiguous areas of jurisprudence flagged; court interpretations described as [VERIFY] where not settled                                         | Add confidence qualifier                                 |

---

## Self-Interrogation for RED Items

For any clause classified RED or CRITIQUE, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity:** Does the finding follow logically from the cited statutory
provision? Would the Tribunal judiciaire or Cour de cassation (3ème chambre civile) actually
reach this conclusion on these facts? Is the Code de commerce article cited still in force
and unamended since Loi Pinel 2014?

**Pass 2 — Completeness:** Have all relevant sources been considered — Code de commerce, Code
civil (supplementary obligations), Décret 2014-1317, Loi Pinel provisions, and recent Cour
de cassation decisions? Are there procedural dimensions (commandement de payer, acte
extrajudiciaire formalities, prescription periods) not yet addressed?

**Pass 3 — Challenge:** What is the strongest argument that the clause is actually valid or
enforceable? Under what circumstances (valid exception under Art. L145-4, contractual waiver
validly obtained under the permitted exception, lease type falling outside the statut) might
a reasonable French commercial property lawyer accept this clause? State this contra-indicator
explicitly before delivering.

If any pass reveals a weakness, revise the analysis before delivery. Mark the audit trail
with `self_interrogation: "PASS"` or `self_interrogation: "REVISED — [reason]"`.

---

## Confidence Scoring

| Level         | Range     | Meaning                                                                                  | Action                                                      |
| ------------- | --------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Définitif** | 0.95–1.0  | Settled Cour de cassation doctrine; clear statutory text of Loi Pinel / Décret 2014-1317 | State with confidence                                       |
| **Élevé**     | 0.80–0.94 | Strong authority; minor interpretive questions; recent Civ. 3ème decisions supportive    | State with brief caveat                                     |
| **Probable**  | 0.60–0.79 | Good arguments; lower courts have applied inconsistently; doctrine uncertain             | State with reasoning and contra-indicators                  |
| **Possible**  | 0.40–0.59 | Genuinely uncertain; Cour de cassation has not yet ruled; competing expert opinions      | Flag for avocat review with both sides                      |
| **Incertain** | 0.0–0.39  | Weak basis; speculative; area of active legislative change                               | Do not assert; flag "[INCERTAIN — VÉRIFIER AVEC UN AVOCAT]" |

---

## Glass Box Audit Trail

Append this YAML block to every output:

```yaml
glass_box:
  skill_name: "legalcode-fr-bail-commercial"
  mode: "[Révision / Rédaction / Négociation renouvellement / Indemnité d'éviction / Révision loyer]"
  perspective: "[Bailleur / Preneur / Neutre]"
  lease_type: "[Bail commercial 9 ans / Bail dérogatoire / Bail commercial renouvelé / Tacite reconduction]"
  tenant_activity: "[Commercial RCS / Artisan RM / Tertiaire ILAT / Non qualifié]"
  applicable_index: "[ILC / ILAT / ICC (legacy) / Non déterminé]"
  legalcode_mcp: "[Connecté — résultats enregistrés dans /tmp/legalcode-bail-commercial-authority.md / Non connecté — vérification manuelle requise]"
  clauses_reviewed: "[number]"
  red_findings: "[number]"
  yellow_findings: "[number]"
  green_findings: "[number]"
  critique_flags: "[number]"
  charges_inventory_present: "[Oui / Non / Partiel]"
  triennial_break_assessed: "[Oui / Non applicable]"
  renewal_deadline_imminent: "[Oui — [date] / Non]"
  eviction_indemnity_prescription_assessed: "[Oui — expiry [date] / Non applicable]"
  citations_verified: "[number VERIFIED / number [VÉRIFIER] flaggés]"
  self_interrogation: "[PASS / REVISED — reason / NON APPLICABLE (aucun item RED)]"
  confidence: "[DÉFINITIF / ÉLEVÉ / PROBABLE] — [brief rationale]"
  limitations:
    - "ILC/ILAT index values must be verified against current INSEE quarterly publication — values cited from memory may be outdated"
    - "Cour de cassation jurisprudence on déplafonnement and facteurs locaux de commercialité evolves; verify recent Civ. 3ème decisions"
    - "Décret 2014-1317 charges list should be verified against légifrance.gouv.fr for any subsequent amendment"
    - "Valeur locative assessments require professional surveyor expertise (expert immobilier) — AI estimates are indicative only"
    - "Eviction indemnity quantification depends on business-specific financial data not available from document review alone"
  reviewer: "AI-assisté — doit être examiné par un avocat en droit immobilier commercial ou un notaire qualifié avant toute décision"
```

---

## Anti-Patterns

Ce qu'il NE FAUT PAS faire lors de la rédaction ou de la révision d'un bail commercial
français :

1. **Confondre bail dérogatoire et bail commercial.** Un bail dérogatoire (Art. L145-5, max
   3 ans) soustrait entièrement le bailleur au statut des baux commerciaux. Si le preneur
   se maintient >1 mois après expiration sans nouveau bail dérogatoire, un bail commercial
   de 9 ans prend effet de plein droit. Ne pas rédiger un bail comme étant dérogatoire si
   la durée cumulée des baux successifs excède 3 ans — cela crée un bail commercial non voulu.

2. **Interdire totalement la cession du bail.** La clause interdisant la cession du bail lors
   de la vente du fonds de commerce est réputée non écrite (Art. L145-16 al. 1). L'inclure
   crée une fausse sécurité pour le bailleur et peut induire en erreur l'acheteur du fonds.
   La vraie protection du bailleur est le droit d'agrément de l'acquéreur (clause d'agrément),
   qui est licite.

3. **Étendre la garantie du cédant au-delà de 3 ans.** L'Art. L145-16-2 plafonne
   impérativement la garantie du cédant à 3 ans. Toute clause prévoyant une garantie plus
   longue est nulle pour l'excédent. Ne pas insérer une garantie de durée indéterminée pour
   le cédant en croyant qu'elle est licite.

4. **Omettre l'inventaire des charges obligatoire.** L'absence d'inventaire précis et
   exhaustif des charges, taxes et travaux (Art. L145-40-2) rend la clause de charges
   inopposable au preneur dans son ensemble — le bailleur ne peut plus récupérer aucun de
   ces postes. C'est l'erreur de rédaction la plus coûteuse d'un bail commercial post-Pinel.

5. **Facturer des grosses réparations au preneur.** Les réparations visées à l'Art. 606 du
   Code civil (structure, toiture, fondations, gros murs) sont à la charge impérative du
   bailleur sous le Décret 2014-1317. Toute clause contractuelle contraire est réputée non
   écrite. Les redresser après signature est impossible — la clause ne peut pas être régularisée.

6. **Utiliser l'ICC pour la révision triennale dans un bail signé après le 1er septembre 2014.**
   L'ICC est interdit pour les révisions triennales des nouveaux baux depuis la Loi Pinel.
   Utiliser l'ICC dans ce contexte prive le bailleur de l'outil légal de révision — la
   clause peut être déclarée nulle et la révision bloquée.

7. **Confondre déplafonnement et révision libre.** Le déplafonnement n'est pas une révision
   libre au prix du marché — il reste soumis à la preuve d'une modification notable des
   facteurs locaux de commercialité ayant eu un impact favorable >10% sur la valeur locative.
   Sans cette preuve, le plafonnement s'applique. Et même avec déplafonnement, le lissage (10%
   par an) s'impose impérativement.

8. **Omettre la clause tunnel dans un contrat d'indexation annuelle.** L'Art. L145-39 est
   d'ordre public — les parties ne peuvent pas l'écarter. Tenter de l'exclure crée une
   fausse sécurité et, à l'inverse, inclure une clause tunnel explicite aide à délimiter
   contractuellement les conditions d'application.

9. **Autoriser la sous-location sans participation du bailleur à l'acte.** Une sous-location
   consentie par le bailleur mais sans qu'il soit partie à l'acte de sous-location est nulle
   (Art. L145-31). Le sous-locataire n'a alors aucun droit direct contre le bailleur. Cette
   erreur expose le bailleur à des conflits sur les paiements et le statut du sous-locataire.

10. **Limiter contractuellement l'indemnité d'éviction.** L'Art. L145-14 est d'ordre public.
    Toute clause plafonnant ou excluant l'indemnité d'éviction est réputée non écrite. Les
    bailleurs qui croient avoir négocié une telle limitation découvrent lors du contentieux
    qu'elle est sans effet.

11. **Ignorer le délai de prescription de 2 ans pour l'indemnité d'éviction.** Le preneur
    a 2 ans à compter du congé pour saisir le tribunal judiciaire (prescription biennale, Art.
    L145-14). Passé ce délai, le droit à l'indemnité est définitivement perdu. Ne pas manquer
    ce délai ; le mettre à l'agenda dès réception du congé.

12. **Donner congé par LRAR sans précaution pour les situations litigieuses.** Si le
    destinataire refuse la LRAR ou si la notification pose problème, le congé peut être
    contesté. Pour tout congé dont les enjeux sont significatifs (refus de renouvellement,
    indemnité d'éviction), recourir à l'acte extrajudiciaire (commissaire de justice) est
    indispensable.

13. **Exclure le droit de résiliation triennale hors des exceptions légales.** L'exclusion
    de la résiliation triennale n'est licite que pour les baux de durée initiale supérieure à
    9 ans, les locaux à usage exclusif de bureaux, les entrepôts, et les locaux monovalents.
    Tenter de l'exclure dans un bail commercial standard de 9 ans rend la clause nulle — le
    preneur peut résilier de plein droit à chaque triennale.

14. **Laisser le bail en tacite reconduction sans stratégie.** La reconduction tacite crée un
    bail à durée indéterminée résiliable à tout moment par l'une ou l'autre des parties avec
    6 mois de préavis. Pour le bailleur souhaitant récupérer ses locaux, c'est une opportunité
    à saisir rapidement. Pour le preneur, c'est une exposition à un congé inattendu. Ne pas
    laisser s'installer la reconduction tacite sans décision consciente.

15. **Confondre la valeur du fonds et la valeur du droit au bail.** Dans le calcul de
    l'indemnité d'éviction, ces deux composantes sont alternatives (le plus élevé des deux est
    retenu). La valeur du droit au bail (différence entre loyer de marché et loyer réel × durée
    résiduelle) peut excéder la valeur du fonds pour un commerce à loyer très favorable dans un
    emplacement prime. Ne pas omettre cette alternative dans l'évaluation pour le preneur.

16. **Négliger la taxe foncière dans la clause de charges.** La taxe foncière est transférable
    au preneur par clause expresse — mais si elle n'est pas explicitement mentionnée dans
    l'inventaire des charges (Art. L145-40-2), elle ne peut pas être réclamée. Pour le bailleur,
    l'omettre revient à la supporter indéfiniment. Pour le preneur, l'absence est protectrice.

17. **Traiter la déspécialisation comme un simple changement d'activité.** La déspécialisation
    partielle et plénière sont des procédures formelles (acte extrajudiciaire ou LRAR,
    notification au bailleur, délai de 2 mois pour contestation). Un changement d'activité sans
    suivre cette procédure constitue une violation de la clause de destination — motif de
    résiliation du bail et de refus de renouvellement sans indemnité.

18. **Sous-estimer la force de la clause résolutoire en contentieux.** La clause résolutoire
    (Art. L145-41) permet au bailleur de résilier automatiquement le bail après commandement
    de payer resté sans effet 1 mois. Mais le juge dispose d'un pouvoir de délai de grâce
    (Art. L145-41 — délai de grâce accordable par le tribunal en référé). Ne pas anticiper
    que le preneur demandera systématiquement ce délai, et calibrer la stratégie contentieuse
    en conséquence.

---

## Writing Standards

### Discipline rédactionnelle (Plain-Language)

Before delivering any output:

1. **Audience check**: Who will read this? A real estate lawyer → technical precision
   acceptable. An entrepreneur tenant → explain French legal terms with English or plain-French
   parenthetical. A corporate real estate team → balance precision with business impact.

2. **Bilingual clarity**: For French-specific legal terms with no direct English equivalent,
   provide the French term with an explanatory gloss:
   - "propriété commerciale (security of tenure — the tenant's statutory right to lease renewal
     and protection against eviction without compensation)"
   - "déspécialisation (change of business activity — partial or total change from the use
     authorised in the lease)"
   - "indemnité d'éviction (eviction indemnity — compensation owed when the landlord refuses
     to renew the lease without a serious and legitimate ground)"
   - "plafonnement (rent capping — the rule limiting triennial rent increases to index movement,
     preventing step-up to market rent)"
   - "lissage (smoothing cap — the Loi Pinel rule capping déplafonnement increases at 10% per
     year)"
   - "clause tunnel (index variance trigger — Art. L145-39 allowing judicial revision when
     cumulative indexation exceeds 25%)"

3. **No false certainty**: Acknowledge where French commercial lease law is contested.
   Déplafonnement fact patterns are heavily litigated; the definition of motif sérieux et
   légitime is judge-made; valeur locative assessments vary by expert. Flag these areas.

4. **Lead with the finding**: Cut preamble. State the article. State the risk. Provide the fix.
   Do not bury a RED finding in a long analysis.

5. **Consistency gate**: All French legal terms must be used consistently — no synonym drift
   (e.g., do not switch between "preneur" and "locataire" without explanation; do not switch
   between "bailleur" and "propriétaire" without noting the distinction).

### Quality gates before delivery

1. Can a non-lawyer business owner understand the executive summary?
2. Can counterparty's counsel understand and respond to each redline?
3. Is every legal claim backed by a specific citation (or flagged [VÉRIFIER])?
4. Are any phrases vague, hedging, or ambiguous? Fix them.
5. Could any sentence be shorter without losing meaning? Shorten it.
6. Do all French legal terms have a gloss on first use?

---

## External Tool Integration

### legalcode-mcp

**With legalcode-mcp connected (preferred):**

- In Step 4, search for current ILC and ILAT index values (INSEE quarterly publication).
- Search for Cour de cassation (3ème chambre civile) decisions from the past 12 months on:
  déplafonnement, charges allocation, déspécialisation, clause résolutoire.
- Verify current text of Art. L145-1 to L145-60 and Décret 2014-1317 against légifrance.gouv.fr.
- Save all results to `/tmp/legalcode-bail-commercial-authority.md` and reference throughout.
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box.

**Without legalcode-mcp:**

- Mark all index values with [VÉRIFIER — INSEE].
- Mark all statutory references with [VÉRIFIER — légifrance.gouv.fr].
- Mark all case law references with [VÉRIFIER — base de données jurisprudentielle].
- Note in Glass Box: `legalcode_mcp: "Non connecté — vérification manuelle requise"`.
- Focus enhancement on structural quality, workflow design, and clause-by-clause analysis.

---

## Output Format Template

Deliver the analysis or draft in this structure:

---

# Analyse du Bail Commercial — [Identification du bail / Adresse des locaux]

**Date:** [date]
**Mode:** [Révision / Rédaction / Négociation renouvellement / Indemnité d'éviction / Révision loyer]
**Perspective:** [Bailleur / Preneur / Neutre]
**Activité du preneur:** [Commercial RCS / Artisan RM / Tertiaire (ILAT) / Non déterminé]
**Indice applicable:** [ILC / ILAT / ICC (legacy — à corriger)]
**Statut du bail:** [Statut baux commerciaux applicable / Bail dérogatoire / Statut incertain]

---

## Synthèse (Executive Summary)

**Profil de risque global:** [FAIBLE / MOYEN / ÉLEVÉ / CRITIQUE]

**Points critiques à adresser avant signature (Tier 1):**

- [RED / CRITIQUE item 1 — one sentence with citation]
- [RED / CRITIQUE item 2 — one sentence with citation]

**Points à améliorer (Tier 2):**

- [YELLOW item summary]

**Conformité confirmée (Tier 3 / GREEN):**

- [GREEN finding summary — brief]

---

## Analyse Clause par Clause

### [Clause category] — [GREEN / YELLOW / RED / CRITIQUE]

**Texte analysé:** "[Relevant clause text from the lease]"

**Analyse:**
[Finding — specific, citing the legal authority (Art. L145-XX Code de commerce or Décret
2014-1317 or relevant Cass. Civ. 3ème decision)]

**Risque:** [If YELLOW/RED/CRITIQUE — precise risk description with quantification where
possible (e.g., "le bailleur ne peut pas récupérer la taxe foncière — perte estimée à
€X/an")]

**Modèle de rédaction:** [If YELLOW/RED — replacement or additional clause language]

**Priorité:** [Tier 1 / Tier 2 / Tier 3]

---

_(Répéter pour chacune des 14 catégories de clauses)_

---

## Tableau Récapitulatif

| #   | Clause                            | Statut               | Priorité   | Action requise |
| --- | --------------------------------- | -------------------- | ---------- | -------------- |
| 1   | Champ d'application et Parties    | GREEN / YELLOW / RED | Tier 1/2/3 | [Action]       |
| 2   | Durée et Terme                    | …                    | …          | …              |
| 3   | Résiliation Triennale             | …                    | …          | …              |
| 4   | Loyer et Révision                 | …                    | …          | …              |
| 5   | Destination des Locaux            | …                    | …          | …              |
| 6   | Cession et Sous-Location          | …                    | …          | …              |
| 7   | Charges et Taxe Foncière          | …                    | …          | …              |
| 8   | Travaux et Entretien              | …                    | …          | …              |
| 9   | Garanties                         | …                    | …          | …              |
| 10  | Renouvellement et Congé           | …                    | …          | …              |
| 11  | Indemnité d'Éviction              | …                    | …          | …              |
| 12  | Clause Résolutoire et Résiliation | …                    | …          | …              |
| 13  | Assurances                        | …                    | …          | …              |
| 14  | Dispositions Générales            | …                    | …          | …              |

---

## Calcul Indicatif de l'Indemnité d'Éviction (si applicable)

**Scénario:** [Preneur pouvant se réinstaller / Preneur ne pouvant pas se réinstaller]

**Valeur marchande du fonds de commerce:**

- Chiffre d'affaires de référence: €[X]
- Méthode de valorisation: [Multiples de CA / EBE / Comparables de marché]
- Valeur estimée: €[X] (indicatif — expertise professionnelle requise)

**Valeur du droit au bail (alternative):**

- Loyer de marché: €[X]/an
- Loyer actuel: €[X]/an
- Différentiel annuel: €[X]
- Années résiduelles: [X]
- Valeur indicative: €[X] (avant actualisation)

**Composantes supplémentaires:**

- Frais de déménagement: €[X] (estimatif)
- Frais de réinstallation: €[X] (estimatif)
- Droits de mutation à l'acquisition d'un fonds équivalent: €[X] (estimatif)
- Perte de clientèle transitoire: €[X] (estimatif)

**Total indicatif:** €[X]

_Note: Ces calculs sont indicatifs uniquement. L'indemnité d'éviction requiert une expertise
immobilière et commerciale professionnelle pour être opposable._

---

## [Glass Box Audit Trail — YAML block per template above]

---

## Recommandations Prioritaires

### ⚡ Tier 1 — Avant signature / Action urgente

1. [Action item + legal basis]
2. [Action item + legal basis]

### ⚠️ Tier 2 — Dans les 30 jours / Lors de la prochaine réunion

1. [Action item + legal basis]

### 💡 Tier 3 — À la prochaine révision contractuelle

1. [Action item + legal basis]

---

_Avertissement final: Cette analyse est générée par intelligence artificielle et ne constitue
pas un conseil juridique. Elle doit être vérifiée et validée par un avocat qualifié en droit
immobilier commercial français ou un notaire habilité avant toute prise de décision. Les
références aux articles de loi et à la jurisprudence comportent un risque d'hallucination —
vérifiez sur légifrance.gouv.fr._

---

## Drafting Instructions (Mode Rédaction)

When drafting a new bail commercial from scratch, follow this sequence:

### Phase 1 — Gather Information

**⟁ CLARIFY** — Before drafting, collect:

1. **Parties**: Full legal name, legal form, RCS registration number, registered address, and
   signatory authority for both bailleur and preneur.
2. **Premises**: Precise address, surface area (in m²), cadastral reference, description of
   premises (nature, floor, dependencies), and any special characteristics.
3. **Duration**: Confirmed 9-year term with start date, or bail dérogatoire with explicit
   maximum 3-year term.
4. **Rent**: Initial rent (excluding taxes / hors taxes), payment frequency, indexation index
   (ILC or ILAT), base period for indexation.
5. **Destination**: Precise description of authorised activities (narrow vs. broad) — discuss
   with client the trade-off between restriction and déspécialisation flexibility.
6. **Charges**: Full list of charges to be allocated to tenant (taxe foncière yes/no;
   specific utilities; insurance; maintenance items).
7. **Guarantees**: Type (dépôt de garantie amount; cautionnement with guarantor details;
   garantie bancaire); duration and renewal obligations.
8. **Special conditions**: Franchise periods (franchise de loyer), fit-out works allocation,
   works condition precedents, pre-emption rights.

### Phase 2 — Mandatory Structure

Every bail commercial must include in this order:

1. Préambule / Parties (with RCS references)
2. Objet et destination (with precise activity description)
3. Durée (9-year start and end date, with triennial break provisions)
4. Loyer (initial amount, indexation clause specifying ILC or ILAT, revision procedure)
5. Charges, taxes, et travaux (full inventory per Art. L145-40-2 + Décret 2014-1317)
6. Dépôt de garantie (amount, return conditions)
7. Obligations du preneur (maintenance, use compliance, insurance, sub-letting prohibition)
8. Obligations du bailleur (delivery, major repairs, peaceful enjoyment)
9. Cession et sous-location (statutory rights preserved + any permitted contractual limits)
10. Clause résolutoire (Art. L145-41 — commandement de payer procedure)
11. Renouvellement and congé provisions
12. Juridiction et droit applicable (Tribunal judiciaire du lieu de l'immeuble)
13. Annexes: état des lieux (to be completed at entry); attestation d'assurance; inventory of
    charges (échéancier de charges).

### Phase 3 — Quality Checks Before Delivery

- [ ] All mandatory charges inventory elements included (Art. L145-40-2)?
- [ ] Annual statement obligation (30 September) included?
- [ ] Triennial works reporting obligation (2-month deadline) included?
- [ ] ILC or ILAT correctly selected for tenant's activity?
- [ ] Triennial break clause correctly drafted (6 months; acte extrajudiciaire or LRAR)?
- [ ] No absolute prohibition on cession du fonds de commerce?
- [ ] Assignor's guarantee capped at 3 years maximum?
- [ ] Subletting clause requires landlord participation in the deed?
- [ ] No attempt to pass Art. 606 CC major repairs to tenant?
- [ ] Clause résolutoire includes the 1-month commandement de payer cure period?
- [ ] Eviction indemnity (Art. L145-14) not excluded or capped?

---

## Localization Notes

This skill is specific to **France (Code de commerce)**. It does not apply to:

- Belgium, Luxembourg, or other French-speaking jurisdictions with distinct commercial lease
  laws
- French overseas territories (DOM-COM) where local variations may apply
- Commercial leases governed by the Code civil rather than the statut des baux commerciaux
  (e.g., where tenant lacks RCS/RM registration)

**Regional variations within France:**

- Paris and Île-de-France: highest eviction indemnity valuations due to prime real estate
  values; significant jurisprudence from Paris Tribunal judiciaire.
- Provincial markets: lower absolute indemnity values but same legal framework.
- DOM-TOM: same Code de commerce statut applies, but local market conditions, costs, and
  professional practices differ.

---

## Provenance

**Created by**: Legalcode original synthesis (2026-03-21).

**Research basis**: Deep research on French commercial lease law (Code de commerce Art. L145-1
à L145-60), Loi Pinel n° 2014-626 du 18 juin 2014, Décret n° 2014-1317 du 3 novembre 2014,
Ordonnance 2016-131, and Cour de cassation (3ème chambre civile) jurisprudence including
decisions through September 2025. Structural patterns drawn from the `legalcode-contract-review`
reference standard and `legalcode-fr-contrat-de-travail-cdi` French jurisdiction patterns.

**Primary sources consulted:**

- Code de commerce, Chapitre V, Art. L145-1 à L145-60 (légifrance.gouv.fr)
- Décret n° 2014-1317 du 3 novembre 2014 (légifrance.gouv.fr)
- Loi n° 2014-626 du 18 juin 2014 (Loi Pinel) analysis via practitioner commentary
- Cass. Civ. 3ème, 18 September 2025, n°24-13488 (déplafonnement — facteurs locaux) [VERIFY]
- Cass. Civ. 3ème, September 2025, n°24-24005 (tenant's exception of non-performance) [VERIFY]
- INSEE ILC / ILAT quarterly publications [VERIFY current values]

**Attribution**: Legalcode original — no third-party skill content incorporated.
