---
name: legalcode-technology-license-review
description: Review technology and IP license agreements comprehensively across US, EU, and UK jurisdictions.
  Use when reviewing any technology license agreement, IP license, software license, patent license, AI
  model license, or technology transfer agreement where IP rights, royalties, or software use rights are
  being licensed or assigned.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review technology and IP license agreements comprehensively across US, EU, and UK jurisdictions. Covers software licenses (perpetual, subscription, SaaS, EULA), patent licenses, technology transfer agreements, AI/ML model licenses, open source license compatibility analysis, and mixed IP bundle licenses. Performs deep clause-by-clause review of: grant scope and exclusivity (exclusive, non-exclusive, sole licenses), field- of-use restrictions, sublicensing rights, royalty structures (running royalties, milestones, MARs, MFL clauses, royalty stacking), audit rights, improvement and grant-back provisions, source code escrow, patent exhaustion, IP indemnification, termination effects on licensed rights, sublicense survival, and technology-specific considerations including SEP/FRAND obligations. Applies EU TTBER 2023/1066, DOJ/FTC Antitrust IP Guidelines, UK CMA VABEO guidance, GDPR Article 28 data licensing overlay, and open source GPL/LGPL/Apache/MIT/ OpenRAIL compatibility matrix. Produces severity-classified findings (GREEN/YELLOW/RED/ ANTITRUST-RISK), redline suggestions, and Glass Box audit trail. Use when reviewing any technology license agreement, IP license, software license, patent license, AI model license, or technology transfer agreement where IP rights, royalties, or software use rights are being licensed or assigned.


# Legalcode Technology License Agreement Review

> **Disclaimer**: This skill provides a framework for AI-assisted review of technology and
> IP license agreements. It does not constitute legal advice. All outputs should be reviewed
> by a qualified legal professional licensed in the relevant jurisdiction before use. Laws
> change; verify current applicability before relying on any provision described here.
> Statutory and case law references are derived from research and carry hallucination risk —
> verify against authoritative sources (EUR-Lex, LII, BAILII, national patent offices) before
> relying on them. Competition law analysis requires jurisdiction-specific counsel as fines
> can reach 10% of worldwide turnover (EU) or treble damages (US). IP licensing interacts
> with antitrust, bankruptcy, export control, and data protection law in ways that require
> multidisciplinary review.

---

## Purpose and Scope

This skill reviews technology and IP license agreements against market standards, statutory
requirements, and competition law. It identifies deviations from market-standard positions,
classifies severity, generates actionable redline suggestions, and flags legal compliance
risks across US, EU, and UK frameworks.

**Covers:**

- Grant scope and exclusivity (exclusive vs. non-exclusive vs. sole licenses)
- Sublicensing rights — default rules and express conditions
- Royalty structures: running royalties, milestones, MARs, MFL, royalty stacking solutions
- Royalty audit rights (GAAP/IFRS standards, frequency, penalties)
- Improvement and grant-back provisions (antitrust screening)
- Source code escrow (trigger events, verification, SaaS alternatives)
- Patent exhaustion (Quanta, Impression Products, EU/UK divergence)
- IP indemnification (structure, carveouts, remedy waterfall, caps)
- Termination effects on licensed rights and sublicenses
- Technology-specific issues: software perpetual/subscription, SaaS, AI/ML, open source
- SEP/FRAND obligations
- EU TTBER 2023/1066 and UK CMA vertical guidance compliance
- GDPR Article 28 overlay when licensed data includes personal data
- Anti-patterns: at least 15 specific drafting errors

**Does not:**

- Draft new technology license agreements from scratch (use a drafting skill)
- Provide legal advice or replace qualified IP, antitrust, or technology counsel
- Perform a full patent validity or freedom-to-operate analysis
- Replace export control screening (ITAR/EAR/UK Strategic Export Controls)

---

## Jurisdiction and Governing Law

This skill covers three primary frameworks. Identify the governing law clause early and
apply the correct framework throughout the review.

**US Framework:**

- Patent rights: 35 U.S.C. §§ 154, 261-262, 271 (Patent Act)
- Copyright: 17 U.S.C. §§ 101, 106, 204 (Copyright Act)
- Antitrust: DOJ/FTC Antitrust Guidelines for the Licensing of IP (2017 update)
- Exhaustion: Quanta Computer v. LG Electronics, 553 U.S. 617 (2008); Impression Products
  v. Lexmark International, 581 U.S. \_\_ (2017), 137 S. Ct. 1523
- Bankruptcy: 11 U.S.C. § 365(n) (IP licenses in bankruptcy)
- Software: Vernor v. Autodesk, 621 F.3d 1102 (9th Cir. 2010) (license vs. sale)

**EU Framework:**

- Technology Transfer Block Exemption Regulation: Reg. 2023/1066 (TTBER 2023, in force
  from 1 May 2023, valid to 30 April 2035) [VERIFY current OJ reference]
- Prior TTBER: Reg. 316/2014 (expired 30 April 2023)
- Software Directive: Directive 2009/24/EC (exclusive rights, decompilation, backup copies)
- InfoSoc Directive: Directive 2001/29/EC (exhaustion of distribution right)
- Enforcement Directive: Directive 2004/48/EC
- Data licensing overlay: GDPR Regulation 2016/679, Article 28
- SEP/FRAND: Huawei v. ZTE, CJEU C-170/13 (2015) (pre-injunction obligations)
- Software resale: UsedSoft v. Oracle, CJEU C-128/11 (2012) (download exhaustion)

**UK Framework (Post-Brexit):**

- Patents Act 1977: ss. 67-68 (exclusive licensee rights), s. 130 (definitions), s. 46
  (licenses of right)
- CDPA 1988: s. 92 (exclusive license definition), s. 101 (exclusive licensee remedies),
  ss. 50A-50C, 296A (mandatory software permitted acts, unenforceable restrictions)
- Competition: UK VABEO (Vertical Agreements Block Exemption Order, SI 2022/516)
- IP Exhaustion: UK currently applies "UK+" regime — EEA-to-UK imports still treated as
  exhausted; non-EEA parallel imports remain subject to consent [VERIFY current UKIPO
  policy; subject to review per call for views completed 2021]
- SEP: Unwired Planet v. Huawei, [2020] UKSC 37 (global FRAND licenses, injunction)

[JURISDICTION-SPECIFIC] When governing law is outside US/EU/UK (e.g., Japan, China,
Canada, Australia), research mandatory local IP licensing rules, compulsory license
regimes, government use rights, and any technology transfer approval requirements.

---

## Interactive Clarification

This skill uses interactive clarification at key decision points. Pause and ask when:

- The license type (patent only vs. copyright only vs. mixed bundle) is unclear
- The market share of the parties is unknown and TTBER safe harbor determination depends on it
- Whether the licensee is a direct competitor of the licensor (affects TTBER thresholds)
- Whether open source components are included in the licensed technology
- Whether the licensed technology includes personal data (GDPR Article 28 overlay needed)
- Whether the agreement concerns SEPs with FRAND obligations
- Whether AI/ML model weights, training data, or outputs are included

---

## SECTION 1: Grant Scope and Exclusivity

### 1.1 Legal Definitions and Distinctions

**Exclusive License** grants rights to the exclusion of all others, including the licensor.

- US (Patent): Under 35 U.S.C. § 261, a patent "shall have the attributes of personal
  property." An exclusive licensee has standing to sue for infringement; a non-exclusive
  licensee generally does not (standing requires an exclusive right). [VERIFY: the precise
  standing doctrine — courts apply a "all substantial rights" test for whether exclusive
  licensee can sue without joining the patent owner.]
- UK (Patent): Patents Act 1977, s. 130(1) defines "exclusive licence" as a licence
  "conferring on the licensee, or on him and persons authorised by him, to the exclusion
  of all other persons (including the proprietor or applicant), any right in respect of
  the invention." UK Patents Act 1977, s. 67: an exclusive licensee has the same right
  as the proprietor to bring infringement proceedings.
- UK (Copyright): CDPA 1988, s. 92(1) defines exclusive licence as "a licence in writing
  signed by or on behalf of the copyright owner authorising the licensee to the exclusion
  of all other persons, including the person granting the licence, to exercise a right
  which would otherwise be exercisable exclusively by the copyright owner." Section 101:
  exclusive licensee has same rights and remedies as if the licence had been an assignment.
- EU (Copyright): Directive 2004/48/EC allows exclusive licensees to bring enforcement
  actions subject to national implementation. Under Directive 2009/24/EC, software
  exclusive licensees hold actionable rights against infringers.

**Non-Exclusive License** permits the licensor to grant the same rights to multiple parties.
No standing to sue for infringement (US); no direct infringement action right without
joinder (UK, varies by instrument). Under 35 U.S.C. § 262, each joint owner may make,
use, offer for sale, or sell without the other's consent, but § 262 does not grant
unilateral licensing authority to co-owners.

**Sole License**: Licensor grants to one licensee only but retains the right to practice
the technology itself. Intermediate between exclusive and non-exclusive. [VERIFY: US
treatment varies by drafting — the word "sole" does not have a uniform legal meaning;
must be defined in the agreement.]

### 1.2 What Makes Exclusivity Meaningful and Enforceable

For exclusivity to be enforceable, the following must be clear:

- **Scope dimensions**: geographic territory, field of use, term, channel
- **Licensor's retained rights**: can the licensor practice in the field? Can affiliates?
- **Exclusivity against sublicensees**: does exclusivity bind downstream?
- **Recording**: US — exclusivity should be recorded with USPTO under 35 U.S.C. § 261
  within 3 months or before a subsequent purchase without notice; UK — recordal at UKIPO
  recommended; EU — national patent office recordal per applicable Member State law
- **Written form**: US exclusive copyright licenses require 17 U.S.C. § 204 signed writing;
  UK copyright exclusive licences require signed writing per CDPA 1988 s. 92(1)

Red flags: exclusivity granted without any defined scope dimensions; exclusivity not
recorded within statutory timeframe; affiliate carveouts that swallow the exclusivity.

### 1.3 Field-of-Use Restrictions

**Definition**: Limits a license to a defined technical, commercial, or application domain.

**Procompetitive function**: Allows licensors to price-discriminate efficiently, reward
commercialization investment, and prevent free-riding across markets. DOJ/FTC Antitrust
Guidelines for the Licensing of IP (2017): field-of-use restrictions allow licensors to
"exploit its property as efficiently and effectively as possible" and are generally analyzed
under the rule of reason.

**Drafting standards:**

- Define the field using objective technical or commercial criteria, not subjective intent
- Address "adjacent field" creep: what happens when the licensee's product straddles fields?
- Address improvements: do improvements fall within or outside the field?
- Cross-license interaction: does the FOU interact with grant-back scope?

**Antitrust limits (US)**: Field-of-use restrictions become problematic when:

- Licensor and licensee are actual horizontal competitors in the restricted field
  (raises market division concerns under Sherman Act § 1)
- Restrictions are naked market division not reasonably necessary for the license
- Combined with exclusive dealing or tying to exclude rivals from inputs

**Antitrust limits (EU TTBER 2023/1066)**: Article 4 prohibits "hardcore restrictions"
including allocation of markets or customers between competing undertakings [VERIFY: exact
Article 4 text of 2023/1066; likely matches prior TTBER 2014/316 Article 4 which prohibited
restrictions on determining prices, allocation of markets, output limits, and restricting
active or passive sales in vertical agreements to the extent they exceed what is necessary].
TTBER safe harbor: 20% combined market share for competing undertakings; 30% for
non-competing undertakings.

**Patent exhaustion interaction**: A field-of-use license does NOT prevent exhaustion if
the patent holder makes an authorized, unrestricted sale. After Impression Products v.
Lexmark (2017), a patent owner cannot restrict downstream use of a product through
post-sale conditions imposed in a license — the product is exhausted once sold by the
patentee or with patentee's authorization without restriction. Field-of-use restrictions
survive in the license grant itself but cannot be enforced against downstream purchasers
through patent law after exhaustion. See Section 6 (Patent Exhaustion).

RED FLAG: Field-of-use restrictions that purport to impose use conditions on purchasers
of the licensed product rather than limiting the licensee's own scope of use.

---

## SECTION 2: Sublicensing Rights

### 2.1 Default Rules

**US Patent Law**: A non-exclusive licensee has NO sublicensing right without express
grant. The general rule is that a patent license is personal and non-transferable unless
the agreement expressly permits sublicensing. [VERIFY: Speedplay, Inc. v. Bebop, Inc.,
211 F.3d 1245 (Fed. Cir. 2000) — licensee that has no right to sublicense cannot transfer
its license rights even by operation of law without express authority; confirm exact
citation.] An exclusive licensee similarly cannot sublicense without express authority,
unless sublicensing power is implicit from the grant of "all substantial rights."

**US Copyright Law**: 17 U.S.C. § 101 definition of "transfer of copyright ownership"
excludes nonexclusive licenses. A non-exclusive licensee cannot sublicense. An exclusive
licensee holding "all substantial rights" approximating an assignment may sublicense.

**UK Patent Law**: No statutory default sublicensing right. Must be express. Patents Act
1977 s. 67 gives exclusive licensees rights against infringers but does not grant
sublicensing power by implication.

**UK Copyright Law**: CDPA 1988 s. 92(2): exclusive licensee has the same rights against
a successor in title bound by the licence. Sublicensing requires express grant. An
exclusive licensee cannot sublicense without authority.

**EU Approach**: No unified EU rule; governed by national law of Member States under choice
of law principles. German, French, and other civil law systems typically require express
sublicensing authority. Under TTBER 2023/1066, sublicensing within the safe harbor is
generally permissible but subject to flow-down obligations.

### 2.2 Conditions on Sublicensing

When sublicensing is expressly permitted, the following conditions are market standard:

1. **Written consent**: Prior written consent from licensor for each sublicense, or deemed
   consent for defined categories (affiliates, contractors providing services to licensee)
2. **Flow-down obligations**: Sublicenses must bind the sublicensee to all material
   restrictions applicable to the licensee (IP protection, audit rights, restrictions,
   confidentiality, field-of-use)
3. **No greater rights**: Sublicensee cannot receive rights greater than those held by the
   licensee (nemo dat)
4. **Licensor as third-party beneficiary**: Licensor should be expressed as a third-party
   beneficiary of the sublicense for enforcement purposes
5. **Copy to licensor**: Copies of all sublicenses (or at minimum notice and key terms)
6. **Survival upon termination**: See Section 8 below — what happens to sublicenses when
   the master license terminates?

**Liability for sublicensees**: The licensee remains primarily liable to the licensor for
its sublicensees' compliance with the license terms. This mirrors the sub-processor
liability model under GDPR Article 28(4) and should be expressly stated.

### 2.3 Key Cases

**Jacobsen v. Katzer**, 535 F.3d 1373 (Fed. Cir. 2008): The Federal Circuit held that open
source license conditions (here, Artistic License conditions requiring attribution, retention
of copyright notices, and documentation of modifications) are conditions, not covenants.
Violation of a condition is copyright infringement (not merely breach of contract), enabling
injunctive relief and statutory damages without proving actual harm. This is the foundation
of open source license enforcement: conditions create rights-limiting boundaries, not merely
promises. The distinction conditions vs. covenants determines available remedies.
[VERIFY: exact Federal Circuit citation.]

**Vernor v. Autodesk**, 621 F.3d 1102 (9th Cir. 2010): The Ninth Circuit held that
software is licensed (not sold) when the copyright holder: (1) specifies the transaction
is a license; (2) imposes significant restrictions on use; and (3) imposes significant
restrictions on transfer. The "first sale" doctrine under 17 U.S.C. § 109 (exhaustion for
tangible copies) does not apply to software licensed under these conditions. This confirms
that a well-drafted EULA/software license prevents downstream resale exhaustion. Note:
UsedSoft v. Oracle CJEU C-128/11 (2012) reaches the opposite conclusion for EU — a
downloaded copy once paid for is exhausted for purposes of resale, regardless of license
terms, under Software Directive 2009/24/EC.

[VERIFY: "Sunni v Dyson" — the research request cites this case for sublicensing rights.
This citation could not be confirmed through available research. It may be a misremembering
or jurisdictional variant. Do not rely without verification. If this referred to a UK or
Commonwealth case on sublicensing, verify through BAILII before using.]

---

## SECTION 3: Royalty Structures

### 3.1 Running Royalties — Base Definitions

The royalty base is the single most negotiated financial term. Precise definition is critical.

**Net Sales / Net Revenues / Net Receipts**: The agreed base for calculating running
royalties. Market standard components:

| Term             | Typical Deductions Allowed                                                                                                        |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Net Sales**    | Returns, allowances, trade discounts, freight/insurance/customs if separately stated, sales taxes, VAT/GST, rebates actually paid |
| **Net Revenues** | Above plus allocated portions of bundled prices                                                                                   |
| **Net Receipts** | Cash actually received after returns and chargebacks                                                                              |

Red flags: deductions so broad they materially erode the royalty base (e.g., "all selling,
general and administrative expenses"); deductions that are not "actually paid and not
recouped"; vague terms like "reasonable expenses"; no definition of bundling allocation
methodology.

**Bundling and combination products**: Where a licensed product is sold as part of a
bundle, the agreement must specify: (a) whether the royalty is on the entire bundle price;
(b) a reasonable allocation methodology (e.g., proportionate fair value allocation per GAAP
ASC 606 / IFRS 15); or (c) a floor price for the licensed component.

### 3.2 Milestone Payments

Standard milestone categories:

- **Development milestones**: Initiation of clinical or technical development phase,
  completion of proof of concept, filing of patent applications
- **Regulatory milestones**: First IND/CTA filing, Phase I/II/III initiation, NDA/MAA
  submission, first regulatory approval in specified jurisdiction
- **Commercial milestones**: First commercial sale, reaching annual net sales thresholds

Drafting requirements: Each milestone must have (a) an objective definition of the trigger
event; (b) a single-payment or recurring structure clarified; (c) a designation as one-time
or recurring for each sales threshold; (d) a mechanism to handle parallel regulatory
approvals in multiple jurisdictions.

### 3.3 Hybrid Structures, Minimum Annual Royalties (MARs), Most-Favored Licensee (MFL)

**MARs (Minimum Annual Royalties)**: Guarantee the licensor a floor payment regardless of
actual commercialization. If actual running royalties fall below the MAR, the licensee pays
the difference. MARs function as a performance incentive and commercialization backstop.
Drafting considerations:

- Escalating vs. flat MAR over time
- Whether MAR payments are creditable against future running royalties (most common) or
  forfeited
- Whether failure to hit MAR thresholds triggers licensor's right to terminate or convert
  exclusive to non-exclusive

**MFL (Most-Favored Licensee)**: Obligates the licensor to offer the licensee terms no
less favorable than those offered to any future licensee for the same or similar IP.
Significant antitrust and commercial considerations:

- Can chill licensing if licensor must re-price all licensees when offering new terms
- May require price notifications that create MFN-linkage antitrust risk
- Must be carefully scoped: comparable licensees, comparable use, comparable field of use
- EU: MFL clauses in technology licensing may be scrutinized under TTBER if they result
  in price coordination between licensees [VERIFY: whether current TTBER guidance addresses
  MFL specifically.]

**Royalty Rate Stacking — The Problem**: When a product practices multiple patents held by
different owners, cumulative royalties can exceed the product's value. Known as the
"royalty stack." Particularly acute for: complex electronics, smartphones, standard-essential
patent (SEP) pools, software platforms incorporating multiple third-party APIs.

**Royalty Stacking Solutions (standard contractual approaches)**:

1. **Aggregate royalty cap**: Cap on total royalties payable under all licenses covering
   the licensed technology (e.g., "In no event shall aggregate royalties payable to [all
   parties] exceed X% of Net Sales")
2. **Royalty offset/credit**: If licensee pays royalties to third parties for rights
   necessary to practice the licensed IP, those payments credit against royalties owed to
   licensor (typically 50%-100% credit, often with a floor)
3. **Most-favored royalty + stacking awareness**: Licensor commits that if a similarly
   situated licensee receives better stacking protection, this licensee receives the same
4. **Portfolio cross-license**: Replace per-patent royalties with a portfolio-level
   payment
5. **FRAND commitment**: For SEPs, the FRAND undertaking inherently accounts for stacking
   (though courts continue to debate how stacking adjusts the FRAND rate — see Ericsson
   v. D-Link, 773 F.3d 1201 (Fed. Cir. 2014) [VERIFY citation])

### 3.4 Royalty Base — SSPPU Doctrine

**Smallest Saleable Patent-Practicing Unit (SSPPU)**: In patent infringement damages
(and by extension in negotiated FRAND licenses), when a patent covers only a component
of a larger product, the royalty base should be the smallest saleable unit that practices
the patent, not the entire end product.

**LaserDynamics, Inc. v. Quanta Computer, Inc.**, 694 F.3d 51 (Fed. Cir. 2012): The
Federal Circuit held that when only one feature of a multi-component product is patented,
the royalty base must be the smallest saleable patent-practicing unit, not the entire
product. The "entire market value rule" (EMVR) — which allows the entire product as the
royalty base — applies only when the patented feature drives demand for the entire product
(a demanding standard). [VERIFY citation.]

**Ericsson, Inc. v. D-Link Systems, Inc.**, 773 F.3d 1201 (Fed. Cir. 2014): The Federal
Circuit applied the SSPPU framework to SEP/FRAND cases. The court modified the Georgia-
Pacific reasonable royalty framework for SEPs: courts must apportion to the value of the
patented feature, must not award royalties that capture the value of standardization
itself (i.e., the benefit of being in the standard, not the patent's technical merit), and
must instruct juries on royalty stacking as a factor in FRAND rate determination.
[VERIFY citation.]

**Drafting implication**: In negotiated technology licenses, the royalty base definition
should specify whether it is the entire product price, a component price, or an allocated
functional portion. Failure to define this clearly creates SSPPU/EMVR litigation exposure.

### 3.5 Audit Rights

Market-standard audit provisions:

| Element                    | Market Standard                                                                                               | Red Flag                               |
| -------------------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **Frequency**              | Once per calendar year maximum                                                                                | More than once per year without cause  |
| **Notice period**          | 30-60 days advance written notice                                                                             | No notice requirement                  |
| **Auditor qualification**  | Independent nationally recognized accounting firm (Big Four or equivalent)                                    | No auditor qualification requirement   |
| **Accounting standards**   | Auditor reviews royalty reports against licensor's GAAP or IFRS records                                       | No specified accounting standard       |
| **Underpayment threshold** | Licensee pays audit costs if underpayment exceeds 5-10% of amount owed                                        | Licensee always pays audit costs       |
| **Underpayment penalty**   | Underpaid amount plus interest (often prime + 2-3%); some agreements add 10-15% penalty                       | No penalty for systematic underpayment |
| **Records retention**      | 3-5 years from report date                                                                                    | Less than 3 years                      |
| **Dispute mechanism**      | Auditor's findings are binding unless disputed within 30-60 days; escalation to second auditor or arbitration | No dispute mechanism                   |
| **Confidentiality**        | Audit results confidential to licensor; auditor bound by confidentiality                                      | No auditor confidentiality obligation  |

Red flags: No audit right at all; audit results shared with third parties; no records
retention obligation; audit costs borne by licensor regardless of findings (creates adverse
incentive); no underpayment cure period before penalty accrues.

---

## SECTION 4: Improvement Rights and Grant-Backs

### 4.1 Types of Grant-Back Provisions

A **grant-back clause** (or "improvements clause") requires the licensee to license back
to the licensor any improvements the licensee makes to the licensed technology.

| Type                           | Description                                                                                                              | Antitrust Profile                                                                                                     |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| **Non-exclusive grant-back**   | Licensee grants licensor a non-exclusive right to use improvements; licensee retains full rights                         | Lowest risk; generally safe under US and EU rules                                                                     |
| **Exclusive grant-back**       | Licensee must grant licensor exclusive rights to improvements, preventing licensee from licensing improvements to others | Significant antitrust risk; excluded from EU TTBER safe harbor (Art. 5)                                               |
| **Assignment of improvements** | Licensee must assign all improvements to licensor outright                                                               | Highest antitrust risk; effectively suppresses licensee innovation; likely Article 5 excluded restriction under TTBER |

### 4.2 Antitrust Treatment

**US (DOJ/FTC IP Licensing Guidelines 2017)**: Non-exclusive grant-backs "generally do not
present antitrust concerns" because the licensee retains rights to practice and license
its improvements. Exclusive grant-backs are analyzed under the rule of reason, focusing
on whether they reduce licensee incentives to innovate, and whether procompetitive
benefits (e.g., facilitating technology dissemination) outweigh the harm. Mandatory
exclusive grant-backs can constitute patent misuse if combined with other terms that extend
the patent's scope beyond its grant.

**Hartford-Empire Co. v. United States**, 323 U.S. 386 (1945): The Supreme Court struck
down a comprehensive cross-licensing and patent pooling scheme among glass manufacturers
that included compulsory grant-backs as part of a scheme to dominate the industry and
foreclose competition. The combination of grant-backs with broader anticompetitive conduct
— not the grant-back alone — drove the antitrust violation. [VERIFY citation: some sources
cite Hartford-Empire as 323 U.S. 386 (1945); confirm.]

**Transparent-Wrap Machine Corp. v. Stokes and Smith Co.**, 329 U.S. 637 (1947): The
Supreme Court held that a mandatory exclusive grant-back in a patent license was not per se
patent misuse but cautioned that it could become misuse if used as part of a scheme to
suppress competition. [VERIFY citation and holding; this is frequently cited but confirm
through primary source.]

**EU TTBER 2023/1066**: Article 5 lists "excluded restrictions" — provisions that cannot
benefit from the block exemption even when market share thresholds are met:

- Exclusive grant-back obligations on the licensee (Art. 5(1)(b)): the licensee cannot
  be required to assign or grant exclusive back-licences for improvements to the licensor
- Non-challenge clauses (Art. 5(1)(c)): provisions preventing the licensee from
  challenging the validity of the licensed IP (though licensor may terminate upon challenge)
  [VERIFY: exact Article 5 numbering in 2023/1066 — cross-check against EUR-Lex official
  text, as Article numbers may differ slightly from the 2014/316 predecessor.]

Non-exclusive, royalty-bearing grant-back obligations remain within the TTBER safe harbor
provided other conditions are met.

### 4.3 Improvements vs. Derivative Works

**Critical drafting distinction**: Patent improvements and copyright derivative works are
different legal concepts:

- A **patent improvement** is an invention that would infringe the licensed patent if
  practiced without a license but adds independent patentable subject matter
- A **derivative work** (copyright) is a work based upon one or more preexisting works
  per 17 U.S.C. § 101; under 17 U.S.C. § 106(2), the copyright owner has exclusive
  rights to prepare derivative works

In technology licensing:

- Software modifications by the licensee may be both patent improvements AND derivative
  works; the grant-back must cover both separately
- AI/ML fine-tuned models trained on licensed model weights are likely derivative works
  for copyright purposes, triggering any grant-back in the ML license
- Clearly define: what constitutes an "improvement" (new functionality? bug fix? port?),
  what constitutes "based on" the licensed technology, and whether severable innovations
  that are merely related to the licensed field are captured

---

## SECTION 5: Source Code Escrow

### 5.1 Purpose and Rationale

Source code escrow protects technology licensees against the risk that the licensor
becomes unable or unwilling to support, maintain, or deliver the licensed software.
A neutral escrow agent holds a deposit of:

- Source code (all versions in active use or support)
- Build scripts, make files, and compilation instructions
- Technical documentation enabling a competent developer to build the software
- Third-party dependencies and open source components list
- Test suites, integration specifications, and related materials

### 5.2 Standard Trigger Events (Release Conditions)

The escrow release to the licensee is triggered by one or more of:

1. **Licensor insolvency**: Filing for bankruptcy, receivership, administration (UK), or
   insolvency proceedings under applicable law. Note: Under 11 U.S.C. § 365(n) (US),
   licensees may elect to retain IP rights when a licensor trustee rejects an executory
   IP license — escrow release provides the practical mechanism. In UK administration, IP
   licenses are treated as contracts subject to administrator's election.
2. **Cessation of support**: Licensor materially breaches its support/maintenance
   obligations and fails to cure within a defined period (typically 30-90 days)
3. **Licensor wind-down or dissolution**: Licensor ceases to carry on business
4. **Change of control / M&A**: Licensor is acquired by a competitor of the licensee or
   a company in a conflicting field (note: this is the most negotiated trigger — licensors
   resist it; frame as a future consent right or notification trigger instead)
5. **Abandonment of technology**: Licensor announces end-of-life and ceases all development
   and maintenance with no third-party continuation plan

### 5.3 Escrow Providers and Verification Levels

**Major providers:**

- **NCC Group** (formerly Iron Mountain IP Escrow; also EscrowTech US): Global provider;
  UK, US, continental Europe. Standard tri-party escrow agreement structure. UK escrow
  framework aligned with British Computer Society and BSIA standards [VERIFY current UK
  standards applicable to software escrow].
- **Iron Mountain**: US and international escrow services; acquired NCC Group escrow
  division in some markets [VERIFY current corporate structure of these providers as of
  2024-2026].
- **EscrowTech International**: US-focused; SaaS and traditional software escrow.

**Verification levels (market standard framework)**:
| Level | What Is Verified | Recommended For |
|-------|-----------------|-----------------|
| **Level 1 (Basic)** | Deposit exists; media readable; content matches agreed specification | Low-risk, commodity software |
| **Level 2 (Content)** | Source code compiles; build scripts execute; basic functionality verified | Standard enterprise software |
| **Level 3 (Technical)** | Full build and deployment tested; functional testing against specifications | Mission-critical or bespoke systems |

Annual re-deposit and periodic verification are market standard. Re-deposit should be
triggered upon each major software release.

### 5.4 SaaS Escrow Alternatives

Traditional source code escrow is insufficient for SaaS products where the licensee
accesses a hosted service and cannot independently deploy source code. SaaS escrow
alternatives:

**Continuity-of-service escrow** (offered by providers such as Vaultinum and others):

- Continuous monitoring of the SaaS provider's operational status
- Automated snapshots of configuration, data schema, and deployment scripts
- Release triggers activate deployment to licensee-controlled cloud environment

**Data escrow for SaaS**:

- Automated export of licensee's data in a portable format (CSV, JSON, API export)
- Triggered on the same release events
- Distinct from IP escrow — protects licensee's own data, not licensor's software

**Contractual alternatives to escrow (where escrow is infeasible)**:

- Obligation to provide migration assistance and data export for 12 months post-termination
- SLA-backed availability commitments with financial penalties
- Documented API/data portability standard
- Right to retain a third-party operational copy under escrow arrangement

[VERIFY: Vaultinum and CodeGuard are referenced in the request — confirm their current
product offerings and market status as of 2024-2026.]

### 5.5 Drafting Checklist for Escrow Provisions

- [ ] Escrow agent named or selection procedure specified
- [ ] Deposit materials fully defined (not just "source code")
- [ ] Initial deposit deadline specified (typically within 30-60 days of signing)
- [ ] Update obligations on each new release, major version, or annually
- [ ] Verification level specified and frequency
- [ ] Trigger events exhaustively listed; dispute mechanism for contested releases
- [ ] Release conditions: what licensee may do with released materials (deployment, maintenance
      only; no redistribution or commercial exploitation)
- [ ] Licensor's right to contest release (cure period, independent technical arbitration)
- [ ] Escrow agent costs allocation (market: licensor pays, with contribution by licensee)
- [ ] Integration with bankruptcy/insolvency provisions (11 U.S.C. § 365(n) election, UK)

---

## SECTION 6: Patent Exhaustion

### 6.1 US Patent Exhaustion

**Foundational principle**: Once a patented item is sold in an authorized sale, all patent
rights in that specific item are exhausted. The patent holder cannot sue downstream
purchasers under patent law for using or reselling an exhausted item.

**Quanta Computer, Inc. v. LG Electronics, Inc.**, 553 U.S. 617 (2008):

- Authorized sale triggers exhaustion even for method patents, provided the product
  "sufficiently embodies" the patent
- A product embodies a patent when it practices the "essential features" of every
  limitation of the patent and has no commercially significant use other than practicing
  the patent
- An authorized sale to a third party (here, Intel selling chips with LGE's authorization)
  exhausts LGE's patents against downstream purchasers (here, Quanta)
- Notice alone (telling Intel customers they lack licenses) does not prevent exhaustion;
  the license to Intel must have actually restricted Intel's sales to prevent exhaustion

**Impression Products, Inc. v. Lexmark International, Inc.**, 137 S. Ct. 1523 (2017):

- A patent holder cannot use patent law to enforce post-sale restrictions on a product it
  has sold, even if those restrictions were clearly communicated at time of sale
- Lexmark could not use patent infringement claims to prevent remanufacturers from
  refilling empty toner cartridges after authorized sale
- **International exhaustion**: The Court held that a US patent is exhausted by an
  authorized foreign sale — Lexmark could not use US patent law against a product it sold
  abroad and re-imported. Overruled prior Federal Circuit precedent (Jazz Photo Corp.)
- Post-sale restrictions remain enforceable through contract law (between buyer and seller)
  but are not enforceable through patent law against downstream purchasers who are not
  parties to the original contract

**Drafting implication**: Field-of-use restrictions must limit the license grant itself
(what the licensee may do), not restrict downstream uses through patent enforcement.
Conditional sales to licensees do NOT restore post-sale patent enforcement against
downstream buyers.

### 6.2 EU Exhaustion

Under EU law (Directive 2001/29/EC, Article 4(2); Software Directive 2009/24/EC):

- The distribution right is exhausted after the "first sale or other transfer of ownership"
  within the EEA with the right holder's consent
- **UsedSoft GmbH v. Oracle International Corp.**, CJEU C-128/11 (2012): A downloaded
  software copy that has been permanently paid for is "sold" for exhaustion purposes under
  the Software Directive, even without a tangible medium. Oracle could not prevent resale
  of used software licenses for perpetually-licensed downloads. This is a significant
  departure from US law (compare Vernor v. Autodesk). [VERIFY: exact holding and whether
  it extends beyond the Software Directive to other digital content post-Tom Kabinet
  CJEU C-263/18 (2019).]
- EU exhaustion is regional (EEA-wide), not global — imports from outside the EEA are not
  automatically exhausted

### 6.3 UK Post-Brexit Exhaustion

UK currently applies a "UK+" (or "national plus EEA") regime as of the Withdrawal Agreement:

- Goods placed on the market in the EEA or UK before end of transition (31 December 2020)
  continue to benefit from exhaustion
- UK government reviewed its regime post-Brexit and as of 2021-2023 has maintained EEA
  imports as exhausted (i.e., goods lawfully placed on the EEA market may be imported to
  UK without IP owner's consent)
- UK does NOT currently apply global exhaustion for imports from non-EEA countries —
  parallel imports from the US, Japan, or other markets require IP owner's consent
- [VERIFY: UKIPO has conducted a call for views (completed 2021). As of 2024, the UK
  government has not moved to either pure national or global exhaustion. Confirm current
  policy position before advising on UK parallel import rights in technology licensing.]

**Technology licensing implication**: UK licensors granting exclusive UK rights must address
whether EEA parallel imports undercut the exclusivity. Consider carving out EEA parallel
import rights or addressing them explicitly in the grant.

---

## SECTION 7: IP Indemnification

### 7.1 Standard Structure

IP indemnification protects the licensee (and its customers) against third-party claims
that the licensed technology infringes a third party's IP rights. The licensor indemnifies
because it controls the technology and is best positioned to assess and defend IP risk.

**Standard structure:**

1. **Obligation to defend and indemnify**: Licensor defends, indemnifies, and holds
   harmless the licensee against third-party IP infringement claims arising from the
   licensee's authorized use of the licensed technology
2. **Notification**: Licensee must provide prompt written notice of the claim (typically
   within 10-30 days of becoming aware); failure to give timely notice may relieve licensor
   of obligation to the extent of prejudice
3. **Control**: Licensor has the right to control the defense, including choice of counsel
   and settlement decisions (subject to licensee consent where settlement imposes ongoing
   obligations on licensee)
4. **Cooperation**: Licensee cooperates, provides reasonable assistance, does not make
   admissions, and permits licensor to manage the defense

### 7.2 Standard Carveouts (Licensor's Indemnification Exclusions)

Licensor typically excludes indemnification obligations where the infringement arises from:

1. **Licensee modifications**: Licensee's modification of the licensed technology
2. **Combination**: Use in combination with third-party products not specified by the
   licensor, where the infringement arises from the combination
3. **Specification compliance**: Licensor's compliance with the licensee's specifications
   or designs (licensor is essentially a custom developer following instruction)
4. **Continued use after notice**: Licensee's continued use after licensor provides a
   non-infringing workaround or notice to cease
5. **Open source**: Infringement arising from open source components incorporated by the
   licensee (distinct from open source included in the licensor's technology)
6. **Prior use**: The licensee's independent use of the same technology before receipt
   of the license

### 7.3 IP Remedy Waterfall

Before paying damages, the licensor should have the right to remedy the infringement.
Market-standard waterfall (in order of preference):

1. **Procure a license**: Obtain a license from the third-party patent or copyright holder
   that permits continued use
2. **Modify the technology**: Provide a modified version that avoids infringement while
   remaining substantially functionally equivalent
3. **Replace the technology**: Replace the infringing component with a non-infringing
   equivalent
4. **Refund and termination**: If none of the above is feasible within a reasonable period
   (typically 60-180 days), licensor may terminate the license for the affected technology
   and refund pre-paid fees (often pro-rated; sometimes subject to a cap)

Red flags: No waterfall — licensor must pay damages without first having a remedy
opportunity; refund cap tied to aggregate liability cap (which may be very low); termination
right exercised by licensor without licensee's migration assistance.

### 7.4 Indemnification Caps and Limitation of Liability Interaction

**The carve-out structure**: Most technology agreements cap aggregate liability at 12
months of fees paid. However, IP indemnification is typically carved out from the cap,
or given a separate (higher) cap:

- **Uncapped IP indemnity**: Licensor bears full IP risk as it controls the technology
  (market position for sophisticated licensees of mission-critical technology)
- **Separate IP indemnity cap**: Often 2x-3x aggregate annual fees, or a specified amount
- **Mutual indemnity**: Both parties indemnify for their respective IP infringements
  (relevant where the licensee also provides specifications that become part of the product)

Under UK law (UCTA 1977), clauses excluding liability for "negligence" (including in a
business context) may be unenforceable; IP indemnification caps that amount to an
exclusion of liability for gross negligence or fraud will not be upheld. Civil law
jurisdictions (France, Germany) have analogous mandatory rules.

### 7.5 IP Warranty

**US**: Licensors of technology typically disclaim all implied warranties of non-
infringement (UCC § 2-312 applies to goods; software is often treated as a service
or mixed transaction). Express IP indemnification replaces the warranty claim.

**UK**: Sale of Goods Act implied terms do not apply to software licenses (software is
not "goods" for SGA purposes). Terms implied by Supply of Goods and Services Act 1982
(reasonable care and skill) may apply to service-like delivery. Express indemnification
is the appropriate mechanism.

**EU**: Directive 2019/771 on sale of goods and Directive 2019/770 on digital content
supply impose conformity requirements for digital services/content provided to consumers,
including that the content is free from third-party IP claims that prevent conformity.
For B2B technology licensing, no comparable mandatory non-infringement warranty exists
at EU level; national contract law supplies the gaps.

---

## SECTION 8: Termination Effects on Licensed Rights

### 8.1 What Happens When a Technology License Terminates

**Termination vs. Expiration**: Distinguish (a) expiration by efflux of time (end of
agreed term); (b) termination for cause (material breach, insolvency, non-payment); (c)
termination for convenience; (d) termination by election.

### 8.2 Survival of Licenses Post-Termination

Express survival language is required for any rights intended to survive termination.
Standard provisions that survive:

- Accrued payment obligations (unpaid royalties, milestone payments)
- Confidentiality obligations (often 3-7 years post-termination or indefinitely for
  trade secrets)
- Audit rights (for the period before termination, typically 2 years post-termination)
- IP ownership provisions
- Limitation of liability
- Governing law and dispute resolution
- Any license to retain royalty reports or financial records

**Licensed rights do NOT survive** absent express agreement. Upon termination, the licensee
must cease all use of the licensed technology.

[VERIFY: "S&R Accounting v. Xerox" — this citation appears in the research request as
an authority on survival of licenses post-termination. A case by this name in the technology
licensing context could not be confirmed through available sources. Do not rely without
verification through Westlaw/LexisNexis.]

### 8.3 Sublicense Survival Upon Licensor Termination

This is one of the most disputed and commercially critical issues in technology licensing.

**The problem**: If the master license between licensor and licensee terminates, what
happens to sublicenses granted by the licensee to its customers?

**US approach**: No single statutory answer. Courts look to:

- The agreement's express terms on sublicense survival
- Whether the licensor consented to the sublicense (consent may constitute independent
  license to the sublicensee)
- Whether the sublicensee is a good-faith purchaser relying on the sublicense
- 11 U.S.C. § 365(n): where termination arises from licensor's bankruptcy, a sublicensee
  who is a "licensee" under § 365(n) may elect to retain its rights [VERIFY: whether
  sublicensees of sub-licenses qualify under § 365(n); case law is divided]

**Market standard**: Express sublicense survival provision. Two common approaches:

1. **Sublicense survival**: All sublicenses entered into by licensee before the termination
   date survive termination and are deemed direct licenses between licensor and sublicensee
   on the same terms as the sublicense (licensee's obligations "flow down" to licensor)
2. **Sublicense lapse**: All sublicenses terminate simultaneously with the master license
   (creates risk of customer disruption; licensee may seek damages from licensor)

**For enterprise software**: Approach 1 is essential. End customers cannot be left without
a license to software they have purchased and rely on due to a dispute between vendor and
its upstream licensor.

### 8.4 Transition Assistance

Market standard: Upon any termination or expiration, a transition assistance period of
12-24 months during which:

- Licensor continues to provide access at current pricing
- Licensee is permitted to move data, re-platform, or migrate
- Licensor provides reasonable technical assistance at cost
- Source code escrow release is triggered (if applicable trigger events are met)

### 8.5 Return or Destruction of Licensed IP

Upon termination:

- Licensee must return or certify destruction of all copies of licensed technology and
  confidential information
- Certification of destruction must be in writing, signed by an officer
- Cloud/SaaS: Licensee must delete all data exports and copies obtained under the license
- Retained archival copies: Licensee typically permitted to retain one archival copy for
  legal compliance purposes only (not for operational use)

### 8.6 Catch-Up Royalties on Termination

If the agreement includes MARs that were not met, or if royalty payments are due for
the period between the last royalty statement and the termination date:

- All accrued and unpaid royalties become immediately due on termination
- Licensor's audit right should survive for 2-3 years to verify pre-termination royalties
- Where a licensee terminates without cause (convenience termination), consideration
  should be given to whether termination creates a deemed MAR breach for the
  remainder of the term (i.e., the MAR accelerates)

### 8.7 Improvements Made During the License Period

Upon termination:

- Improvements made by licensee that are subject to a grant-back obligation: the grant-back
  survives termination and licensor retains the granted right
- Improvements made by licensee that are NOT subject to grant-back: licensee retains full
  ownership and rights (confirm the grant-back clause covers post-termination improvements
  made during the licensed period)
- Jointly developed improvements: require separate joint development agreement or clear
  ownership allocation; do not leave "jointly developed" undefined in the main agreement

---

## SECTION 9: Technology-Specific Considerations

### 9.1 Software Licenses

**Perpetual vs. Subscription**:

- **Perpetual**: One-time license fee for indefinite use of a specific version. Licensee
  owns the right to use that version forever. Annual maintenance/support is typically
  separate and optional. No termination-for-convenience right typically accrues for
  non-payment of maintenance (only obligation is loss of support).
- **Subscription/Term**: Recurring fee; license expires when subscription lapses. Licensor
  can effectively force upgrades by discontinuing support for old versions. Provides more
  predictable revenue for licensor; more flexible for licensee with lower upfront cost.

**Seat-based vs. Enterprise/Unlimited**:

- **Seat-based**: Named user or concurrent user count. Define: named users vs. concurrent
  users; are contractors and affiliates counted? What happens when users are added?
  True-up mechanism for overuse.
- **Enterprise/Unlimited**: Licensee may use without per-user or per-seat limit within
  defined scope (company, affiliate, global). Often priced based on revenue, employee
  count, or other proxy. Requires careful definition of "Enterprise" and affiliate scope.

**SaaS overlay**: SaaS creates additional complexity:

- License grant is to the service, not the software — define acceptable use, data storage
  location, security requirements, and SLA
- IP in customer data: licensor needs a limited license to process customer data to
  provide the service; licensee retains ownership of its data
- Business continuity: SaaS-specific provisions for data portability, service continuity,
  and escrow alternatives (see Section 5.4)
- Termination/data return: SaaS agreements must address customer data return upon
  termination (typically 30-90 days); GDPR Article 28 requires personal data deletion
  or return upon controller's request

### 9.2 AI/ML Licenses

AI and ML model licensing raises novel IP questions that are not fully settled as of 2026.

**Training Data Rights**:

- Licensor should warrant that training data was collected with appropriate rights for
  use in training AI models (licensed datasets, licensed web scrapes, proprietary data)
- Where training data includes CC-licensed content: NC (NonCommercial) licenses restrict
  commercial AI training; SA (ShareAlike) licenses may create contamination issues for
  the model's outputs [VERIFY: current legal consensus on whether SA propagates through
  training]
- GDPR implications: training on personal data requires a lawful basis; licensee must
  assess whether use of the model could constitute processing of personal data
- EU AI Act (Regulation 2024/1689, in force from August 2024; GPAI provisions apply from
  August 2025): GPAI model providers must maintain a publicly available "summary" of
  training data and implement a copyright compliance policy; open source GPAI models with
  limited systemic risk qualify for reduced obligations [VERIFY specific article numbers
  and implementation timeline]

**Model Weight Licenses**:

- **Fully open (Apache 2.0 / MIT)**: No commercial use restrictions; patent grant included
  in Apache 2.0. Most permissive.
- **OpenRAIL licenses**: Open access with use-based restrictions — prohibits specified
  harmful applications; copyleft-style propagation requires derivatives to maintain
  restrictions. Used by BigScience BLOOM, Stable Diffusion.
- **Meta Llama Community License (Llama 2/3)**: Commercial use permitted below 700M MAU
  threshold; above threshold requires Meta's permission; cannot use outputs to improve
  competing LLMs; no model improvement clause. Note the "no model improvement" restriction
  — this is a form of grant-back prohibition, protecting Meta's competitive position.
- **Proprietary closed-weight licenses**: Model weights not distributed; access only via
  API. License is to the API service, not the model. Output IP belongs to user (typically)
  subject to usage policies.

**Output IP Ownership**:

- Current US copyright office position: AI-generated content without human creative
  contribution is not copyrightable. Where a human provides sufficient creative input to
  AI-assisted output, copyright may subsist in that human-authored element.
- EU: No equivalent CJEU ruling as of 2026; national copyright law of Member States
  applies; most EU civil law jurisdictions require human author for copyright [VERIFY].
- UK: CDPA 1988, s. 9(3) provides copyright protection for "computer-generated works"
  without human author for 50 years; "author" is the person who makes the necessary
  arrangements for the creation of the work — potentially the licensee using the AI model.
  [VERIFY: whether this applies to generative AI outputs.]
- In AI licenses, clarify: does the licensee own outputs? Can outputs be used commercially?
  Can outputs be used to train competing models (see Llama grant-back prohibition)?

**Open Source License Compatibility for AI**:

- GPL/AGPL copyleft risk for model code: if model inference code is GPL-licensed, any
  software linking to or incorporating that code may trigger copyleft obligations
- GPL does NOT attach to the model weights themselves (weights are not "source code" under
  the GPL; no consensus on whether fine-tuned weights are derivative works of GPL-licensed
  training code) [VERIFY: highly unsettled area]
- AGPL specifically: network service use (including SaaS) triggers source disclosure
  obligations — an AGPL model used in a SaaS product may require disclosure of all
  AGPL-covered source code in the service

### 9.3 Open Source License Compatibility

**GPLv2 vs. GPLv3 key differences for technology licensing**:

| Issue                   | GPLv2                          | GPLv3                                                          |
| ----------------------- | ------------------------------ | -------------------------------------------------------------- |
| **Termination**         | Automatic on violation         | 60-day automatic; 30-day cure for first-time violators         |
| **Patent grant**        | No express patent grant        | Affirmative patent grant from all contributors                 |
| **Tivoization**         | Not addressed                  | GPLv3 §6: "Installation Information" required for user devices |
| **Compatibility**       | Not compatible with Apache 2.0 | Compatible with Apache 2.0 (explicitly)                        |
| **Network interaction** | Not triggered by network use   | Not triggered (see AGPL for that)                              |

**Jacobsen v. Katzer (Fed. Cir. 2008)**: Conditions in an open source license (attribution,
retention of notices, documentation of modifications) are copyright license conditions,
not mere contractual covenants. Violation = copyright infringement, enabling statutory
damages and injunctive relief. This remains the controlling US precedent on open source
license enforcement.

**GPL contamination (copyleft propagation) — when does it apply?**:

- GPLv2/v3: triggered by **distribution** of a modified or combined work
- A "combined work" under GPL includes works that link to GPL'd code (static or dynamic
  linking — disputed; FSF position is both trigger; LGPL provides an explicit exception)
- LGPLv2.1: provides a linking exception — proprietary software may link to LGPL'd
  libraries provided the user can modify and relink the LGPL'd library; in practice, this
  means the LGPL library itself remains under LGPL but the proprietary application is not
  infected
- Apache 2.0: No copyleft; permissive; contains patent grant (contributor grants licensee
  a patent license for patents necessarily infringed by the contribution); compatible with
  GPLv3 but NOT GPLv2 (Apache 2.0 patent termination clause is an "additional restriction"
  incompatible with GPLv2)
- MIT: No copyleft; no patent grant; compatible with GPL; most permissive in terms of
  attribution and patent risk

**In technology license review**:

- Require licensor to disclose all open source components in the licensed technology
  with licenses (Software Composition Analysis / SBOM requirement)
- Confirm LGPL and permissive licenses (MIT, Apache 2.0, BSD) are used for any linked
  components (not GPL/AGPL in commercial software delivered to customers)
- For licensees redistributing technology: verify that any GPL-triggered obligations
  are met (source code availability, notices)
- [VERIFY: the GPL FAQ (gnu.org/licenses/gpl-faq.html) is authoritative on FSF's
  interpretation; note that courts may not always follow FSF interpretation.]

### 9.4 APIs and SDKs

API and SDK licensing requires special attention to:

- **Rate limits and throttling**: Maximum number of API calls per second/day/month;
  overage pricing; whether limits are contractually binding or SLA-level commitments
- **Commercial use restrictions**: Many free-tier APIs restrict commercial use; define
  "commercial" precisely (charging end users? Embedding in a commercial product?)
- **Usage restrictions**: Prohibited uses (competing products, competitive intelligence,
  benchmarking, model training without consent)
- **API versioning and deprecation**: Licensor's right to modify or deprecate API without
  notice; minimum notice period for breaking changes (market standard: 12-24 months for
  breaking changes in enterprise API agreements)
- **Data portability**: Does the API agreement permit data export? In what format?
- **Output restrictions**: Are outputs from the API subject to restrictions (not for
  training, not for resale, not for disclosure)?

### 9.5 Standard Essential Patents (SEPs) and FRAND

**Definition**: A **Standard Essential Patent (SEP)** is a patent that must be practiced
to implement a technical standard (e.g., WiFi/IEEE 802.11, 5G/3GPP, USB, Bluetooth).
The standard-setting body typically requires SEP holders to commit to license on **FRAND**
(Fair, Reasonable, and Non-Discriminatory) terms.

**FRAND obligations**:

- **Fair and Reasonable**: Royalty rate reflects the actual technical contribution of
  the patent to the standard, not the value of standardization itself (i.e., the "hold-up"
  problem — once a standard is adopted, every implementer needs the patent, granting
  monopoly pricing power absent FRAND)
- **Non-discriminatory**: Similarly situated licensees must receive materially similar
  terms (Unwired Planet v. Huawei [2020] UKSC 37 confirms this in UK)

**US FRAND litigation framework**:

- Georgia-Pacific factors modified for SEPs: apportion the patent's contribution to the
  standard's value, account for royalty stacking (aggregate royalties across all SEPs in
  the standard), and avoid applying the "hold-up" premium
- Ericsson v. D-Link (Fed. Cir. 2014): Courts must instruct juries on royalty stacking
  and apportion to the smallest saleable patent-practicing unit
- TCL Communication Technology v. Ericsson AB (C.D. Cal. 2017): Court set FRAND rates
  using a "top-down" approach (starting from aggregate reasonable royalty across all SEPs
  and apportioning) [VERIFY citation]

**EU FRAND framework (Huawei v. ZTE, CJEU C-170/13, 2015)**:

- A SEP holder who seeks an injunction for infringement may abuse a dominant position
  under TFEU Article 102 unless, before seeking the injunction, the SEP holder: (1) has
  alerted the infringer of the infringement; (2) has presented a written FRAND offer to
  the infringer; (3) the infringer has not diligently responded
- If the implementer responds in good faith and requests a FRAND license, the SEP holder
  must not seek an injunction; the implementer must provide a security deposit

**UK**: Unwired Planet v. Huawei [2020] UKSC 37 held that UK courts can determine global
FRAND licensing terms and grant injunctions to SEP holders against non-FRAND licensees.

**EU SEP Regulation**: The EU has proposed a regulation on SEPs (currently in legislative
process as of 2026) that would create a mandatory ESSENTIALITY CHECK and FRAND arbitration
mechanism for certain standards. [VERIFY: current status of EU SEP Regulation; as of early
2026, the regulation had not been finally adopted.]

**In technology license review involving SEPs**:

- Identify whether the licensed technology practices any declared SEPs
- Verify whether the licensor has outstanding FRAND commitments that encumber the licensed IP
- Confirm that royalty rates claimed are consistent with FRAND obligations; challenge
  royalties that embed hold-up premium
- Review SSPPU compliance: royalty base must be the smallest saleable patent-practicing
  unit, not the entire end product

---

## SECTION 10: EU/UK-Specific Technology Licensing

### 10.1 EU Technology Transfer Block Exemption Regulation (TTBER) 2023/1066

**Current regulation**: Regulation (EU) 2023/1066 of 1 June 2023, extending and amending
the Technology Transfer Block Exemption Regulation. In force from 1 May 2023 to
30 April 2035. [VERIFY: OJ reference and precise dates against EUR-Lex.]

**Scope**: Applies to technology transfer agreements (TTA) between two undertakings
permitting production of contract products. A TTA is an agreement where a licensor
licenses technology rights (patents, know-how, software copyright, or combinations) to a
licensee for production purposes.

**Safe harbor thresholds**:

- **Competing undertakings**: Combined market share ≤ 20% on the relevant technology and
  product markets — agreement benefits from block exemption
- **Non-competing undertakings**: Each party's market share ≤ 30% on the relevant market

**Article 4 — Hardcore Restrictions** (automatically outside the safe harbor):
For competing undertakings:

- Price fixing (directly or indirectly)
- Output limitations
- Allocation of markets or customers (including territorial allocation)
- Restriction of licensee's ability to exploit its own technology

For non-competing undertakings:

- Price restrictions on sales to third parties
- Restrictions on active or passive sales in territories or to customer groups (with
  specified exceptions for exclusive territories/customer groups)

[VERIFY: exact Article 4 text of 2023/1066 against EUR-Lex, as the 2023 regulation may
have introduced additional nuances vs. the 2014/316 predecessor. Prior research confirmed
hardcore restrictions exist in the same categories but exact sub-article numbering needs
verification.]

**Article 5 — Excluded Restrictions** (cannot benefit from block exemption even if below
market share threshold):

- **Exclusive grant-back obligations**: Requiring the licensee to exclusively license
  or assign improvements back to the licensor
- **No-challenge clauses** (with exception: licensor may terminate the agreement if
  licensee challenges the licensed IP)
- Restrictions on licensee's right to exploit its own technology in cases of cross-licenses

[VERIFY: Article 5 numbering and exact text in 2023/1066 vs. prior version. The 2023
renewal may have maintained the same excluded restrictions as 2014/316 Art. 5, but confirm
any changes introduced in the renewal.]

**Practical application**:

- If market shares are below safe harbor: agreement benefits from block exemption provided
  it contains no hardcore or excluded restrictions
- If market shares exceed safe harbor: agreement requires individual assessment under
  TFEU Article 101(1)/(3) — benefit from exemption is not automatic
- Non-exclusive grant-backs remain within the safe harbor (provided other conditions met)

### 10.2 UK CMA Approach Post-Brexit

**UK VABEO (SI 2022/516)**: The UK Vertical Agreements Block Exemption Order 2022 applies
to vertical agreements (supplier-buyer, licensor-licensee) with market shares ≤ 30%.
Key points:

- Market share threshold: 30% for both supplier and buyer
- Hardcore restrictions include: RPM, absolute territorial restrictions, cross-supply
  bans in selective distribution, component restrictions, wide retail parity obligations
- IP provisions: agreements with IP licensing provisions qualify if the IP provisions are
  "directly related to the use, sale or resale" and "do not constitute the primary object"
  of the agreement
- Note: the UK does NOT have a separate Technology Transfer Block Exemption; technology
  licensing pure-play agreements (where the primary object IS the technology license) fall
  outside VABEO. They require individual assessment under UK Chapter I Prohibition
  (Competition Act 1998)

**CMA guidance**: The CMA has issued guidance on vertical agreements (2022) [VERIFY
guidance document reference; no specific technology transfer guidance has replaced the
retained EU TTBER guidance post-Brexit as of 2024]. Technology-specific licensing is
assessed under general competition principles.

**[JURISDICTION-SPECIFIC]**: For complex technology licensing under UK law (e.g., cross-
licensing between competitors; patent pools; exclusive technology transfer agreements),
seek CMA informal guidance or review retained EU TTBER principles (which the CMA may
consider persuasive though not binding).

### 10.3 GDPR Article 28 Data Licensing Overlay

Where a technology license includes rights to process, use, or access personal data:

**Article 28 requirements apply when**:

- The licensor processes personal data on behalf of the licensee (licensor as processor)
- The license grants rights to a dataset that includes personal data
- A SaaS-delivered licensed technology processes personal data of licensee's customers

**Required contractual provisions**:

1. Subject matter, duration, nature, and purpose of processing
2. Categories of personal data and data subjects
3. Processing only on documented instructions from the controller (licensee)
4. Confidentiality obligations on all personnel with access
5. Appropriate technical and organizational security measures (Article 32)
6. Sub-processor control: prior specific or general written authorization for sub-processors;
   identical obligations flow down to sub-processors; processor remains fully liable
7. Assistance with data subject rights (Articles 12-22)
8. Deletion or return of all personal data upon request/end of service
9. Compliance documentation and audit assistance

**[VERIFY]**: Whether the EU AI Act (2024/1689) Articles 53-55 on GPAI impose additional
data licensing obligations above and beyond Article 28 for AI systems processing personal
data.

---

## SECTION 11: Anti-Patterns and Common Drafting Errors

The following are 15 specific anti-patterns that legal reviewers frequently encounter in
technology license agreements:

### AP-1: The Vanishing Grant — Undefined Scope Dimensions

**Pattern**: License grant defines IP type (e.g., "patents") but omits one or more scope
dimensions: no geographic territory; no field of use; no defined term; or no defined
delivery method.
**Risk**: Dispute over scope; license may be interpreted as global, unlimited, and
perpetual — or conversely, as too narrow to be commercially useful.
**Fix**: Express definition of all five dimensions: IP type, geography, field of use,
term, and channel/delivery mode.

### AP-2: Floating Royalty Base — Undefined "Net Sales"

**Pattern**: Agreement requires royalties on "Net Sales" or "Net Revenues" without
defining what deductions are permitted or how bundled products are allocated.
**Risk**: Systematic under-royalty reporting; dispute over deductions. If licensor is
aggressive, it might add SG&A expenses; if licensee is aggressive, it may deduct
everything below gross revenue.
**Fix**: Define "Net Sales" exhaustively, cap deduction categories, specify bundling
allocation methodology (fair value, standalone selling price per ASC 606/IFRS 15).

### AP-3: The Sublicense Trap — No Sublicense Survival Clause

**Pattern**: Licensee has sublicensed the technology to end customers. The master license
terminates (e.g., licensor insolvency or breach). No sublicense survival clause.
**Risk**: All end customer sublicenses terminate with the master license. Licensee faces
catastrophic customer liability.
**Fix**: Express sublicense survival clause converting sublicenses to direct licenses
from the licensor upon master license termination.

### AP-4: The Audit Deterrent — Audit Costs Always Borne by Licensor

**Pattern**: Audit clause states licensor pays all costs of audit regardless of findings.
**Risk**: Licensor has no financial incentive to exercise audit right; systematic
underpayment goes undetected.
**Fix**: Licensee pays audit costs only if underpayment is below a threshold (typically
5-10% or $X); licensor pays if underpayment exceeds threshold.

### AP-5: Grant-Back Without Antitrust Screen

**Pattern**: Agreement includes an exclusive grant-back of all improvements without any
consideration of the EU TTBER excluded restriction analysis or the DOJ/FTC rule-of-reason
assessment.
**Risk**: EU: agreement falls outside TTBER safe harbor (Article 5 excluded restriction);
may violate TFEU Article 101. US: rule-of-reason challenge if dominant licensor using
grant-back to suppress licensee innovation.
**Fix**: Use non-exclusive, royalty-free grant-back only; include antitrust savings clause;
limit grant-back to improvements that are within the licensed technology field.

### AP-6: No Escrow Re-Deposit Obligation

**Pattern**: Software escrow agreement requires an initial deposit but no obligation to
re-deposit on new software versions or major releases.
**Risk**: Escrow deposit becomes stale; upon release, licensee receives version from two
years ago that is incompatible with current infrastructure.
**Fix**: Mandatory re-deposit on each major release, at minimum annually; verification
re-run after each re-deposit.

### AP-7: IP Indemnity Capped at Aggregate Liability Cap

**Pattern**: IP indemnification is included in the aggregate liability cap (e.g., 12
months of fees). For a $100K/year license, IP infringement exposure is capped at $100K,
while the licensee's business disruption from an injunction could be worth millions.
**Risk**: Licensor's IP indemnity is commercially meaningless; licensee has no protection
for the most material IP risk.
**Fix**: IP indemnification carved out of or given a separate (higher) cap.

### AP-8: Post-Sale Restrictions Drafted as Patent Enforcement Rights

**Pattern**: License agreement purports to restrict downstream use of licensed products
through patent infringement claims post-sale (e.g., "products sold under this license
may only be used in [field]").
**Risk**: After Impression Products v. Lexmark (2017), post-sale restrictions on authorized
sales cannot be enforced through patent law. Restriction is unenforceable as drafted.
**Fix**: Post-sale restrictions must be implemented as contract terms between the licensor
and the downstream purchaser, not through patent infringement claims.

### AP-9: Open Source Contamination — No SBOM or Disclosure Obligation

**Pattern**: Technology license makes no representation about open source components in
the licensed technology. Licensee later discovers the licensed software incorporates
GPLv2-covered components and its commercial product now has copyleft obligations.
**Risk**: GPL copyleft propagation; mandatory source code disclosure requirement; injunction
risk from GPL enforcement (typically by Software Freedom Conservancy or similar).
**Fix**: Licensor represents and warrants that all open source components are disclosed
in an attached SBOM; warrants no GPLv2/v3/AGPL components used in a way that contaminates
the licensee's proprietary code; commits to SBOM update upon each software release.

### AP-10: Exclusive License Without Standing Provisions

**Pattern**: Purportedly exclusive patent license but agreement fails to convey "all
substantial rights" necessary for the licensee to have standing to sue for infringement
without joining the licensor.
**Risk**: Licensee cannot enforce the patent portfolio it has exclusively licensed without
the licensor's cooperation; licensor becomes an unintentional gatekeeper to enforcement.
**Fix**: Include an express right to bring enforcement proceedings independently; or
confirm "all substantial rights" are transferred; address whether licensor must join as
co-plaintiff.

### AP-11: The Evergreen Grant-Back — Captures Post-Termination Improvements

**Pattern**: Grant-back clause is drafted to apply to all improvements "arising from"
the licensed technology, including those developed after termination of the license.
**Risk**: Licensee's post-termination innovation is encumbered by a former licensor's
rights, chilling future development.
**Fix**: Limit grant-back obligation expressly to improvements developed during the
license term; include a sunset for the grant-back obligation post-termination.

### AP-12: FRAND Ignore — No Screening for SEP Exposure

**Pattern**: Technology license for communications, networking, or consumer electronics
technology does not disclose whether any licensed patents are declared SEPs with FRAND
obligations.
**Risk**: FRAND commitments run with the patent and bind all licensors; royalty rates
agreed in the license may exceed FRAND, exposing the licensor to antitrust challenge
(EU Article 102; US § 2) or creating a defense for the licensee.
**Fix**: Require licensor to disclose all declared SEP/FRAND commitments; confirm that
royalty rates are FRAND-compliant; include FRAND savings clause.

### AP-13: No GDPR Article 28 DPA in a Data License

**Pattern**: Technology license grants rights to use a dataset including personal data
without including a Data Processing Agreement under GDPR Article 28.
**Risk**: Both parties violate GDPR; the licensor (as data controller or joint controller)
has not documented the processing relationship; fines up to €20M / 4% of worldwide turnover.
**Fix**: Attach a compliant DPA as an exhibit; identify controller/processor roles; include
all Article 28 required elements.

### AP-14: AI License Without Output IP Clarity

**Pattern**: AI/ML model license is silent on who owns the outputs generated by using the
model. Licensee assumes it owns all outputs; licensor's terms of service assert rights.
**Risk**: Commercial dispute over IP ownership of AI-generated content; potential infringement
if outputs closely reproduce training data (unresolved US/EU copyright questions as of 2026).
**Fix**: Expressly state that outputs generated by the licensee using the licensed model
are owned by the licensee, subject to (a) the licensor's right to use aggregate/anonymized
data for model improvement; (b) compliance with applicable copyright law regarding outputs.

### AP-15: Termination Without Migration Assistance

**Pattern**: Technology license provides licensor with a termination-for-convenience right
on 30 days' notice, with no transition assistance obligation.
**Risk**: Licensee builds operations on the licensed technology; licensor terminates;
licensee has 30 days to migrate — operationally impossible for complex enterprise software.
**Fix**: Minimum 12-month notice for termination-for-convenience affecting a mission-
critical system; 12-24 month transition assistance period at current pricing; data export
and portability obligations; source code escrow release triggered upon termination.

---

## Review Methodology

### Step 1 — Agreement Classification

Identify:

- IP type(s) licensed: patent only / copyright only / know-how / mixed bundle
- Parties: are they competing undertakings? (affects TTBER thresholds)
- Technology type: software / AI-ML / hardware / SEP portfolio / database / mixed
- License model: perpetual / subscription / SaaS / API / distribution
- Governing law: US / UK / EU Member State / other

### Step 2 — Grant Scope Review

For each licensed right, verify all five scope dimensions are defined (IP type, geography,
field, term, channel). Flag exclusive grants lacking recordal, written form requirements,
and standing provisions.

### Step 3 — Sublicensing and Assignment Review

- Is sublicensing permitted? Express or implied?
- Is sublicense survival clause present? Does it address licensor bankruptcy?
- Are flow-down obligations mandatory?
- Is the licensor named as a third-party beneficiary of sublicenses?

### Step 4 — Financial Terms Review

- Define Net Sales/Net Revenues with permitted deductions list
- Review MAR structure and credit/forfeiture mechanics
- Identify royalty stacking risk; review stacking protection clauses
- Verify SSPPU compliance for patent-specific royalties
- Review audit clause against market standard (Section 3.5)

### Step 5 — Grant-Back and Improvements Review

- Type of grant-back: exclusive or non-exclusive?
- Does it constitute an EU TTBER Article 5 excluded restriction (exclusive)?
- Does it satisfy DOJ/FTC rule-of-reason (non-exclusive, procompetitive)?
- Does it clearly separate "improvements" from "derivative works"?
- Termination of grant-back post-expiry of license?

### Step 6 — Escrow Review

- Is escrow present for mission-critical software licenses?
- Deposit materials defined? Verification level specified?
- Re-deposit obligation on new releases?
- Trigger events comprehensive (insolvency, support abandonment, M&A)?
- SaaS-specific escrow alternatives if applicable?

### Step 7 — Patent Exhaustion Screen

- Do any provisions attempt to impose post-sale restrictions enforceable through patent law?
- After Impression Products (2017), flag any language purporting to restrict downstream use
  of sold products through patent infringement claims
- Verify field-of-use restrictions are framed as license grant limitations, not post-sale
  use conditions

### Step 8 — IP Indemnification Review

- Is indemnification present?
- Are carveouts reasonable and not so broad as to swallow the indemnity?
- Is the remedy waterfall present (modify / replace / license / refund)?
- Is IP indemnification carved out of or given a separate cap from the aggregate liability cap?
- Does the agreement address the UK UCTA 1977 and civil law mandatory rules on
  liability exclusion?

### Step 9 — Termination Effects Review

- Are accrued royalties and audit rights expressly stated to survive?
- Is there a sublicense survival clause?
- What transition assistance is provided?
- Are return/destruction obligations clear (with certification)?
- Are post-termination improvements addressed?
- Is the catch-up royalty mechanism clear for MARs?

### Step 10 — Technology-Specific Checks

For software: seat counting, true-up, upgrade rights, SaaS data portability
For AI/ML: training data warranty, output IP, OpenRAIL/model license compatibility
For open source: SBOM, GPL contamination screen, Apache/MIT/LGPL compatibility
For APIs: rate limits, commercial restrictions, deprecation notice
For SEPs: FRAND disclosure, SSPPU compliance, stacking protection

### Step 11 — Competition Law Screen

- TTBER safe harbor: competing (<20%) or non-competing (<30%)?
- Hardcore restrictions: any Article 4 violations?
- Excluded restrictions: any Article 5 violations (exclusive grant-back, no-challenge)?
- UK VABEO: any hardcore violations?
- MFL/MFN clause: does it create pricing coordination risk?

---

## Severity Classification

Each finding is classified as:

| Level              | Definition                                                                                                | Required Action                                     |
| ------------------ | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **GREEN**          | Compliant; meets or exceeds market standard                                                               | No action required                                  |
| **YELLOW**         | Deviation from market standard; commercially suboptimal but not legally deficient                         | Flag for negotiation; suggest redline               |
| **RED**            | Legally deficient, creates material commercial or legal risk, or contains an unenforceable provision      | Redline required; do not execute without resolution |
| **ANTITRUST-RISK** | Potential hardcore or excluded restriction under TTBER/VABEO; US Sherman Act risk; SEP/FRAND pricing risk | Requires competition law counsel before execution   |

---

## Glass Box Audit Trail

For every material finding, record:

1. **Provision identified**: Article/section number and quoted text
2. **Legal framework applied**: Specific statute, regulation, or case law
3. **Finding**: What the issue is, why it is a risk
4. **Market standard**: What market-standard drafting looks like
5. **Suggested redline**: Proposed replacement or addition language
6. **Severity**: GREEN / YELLOW / RED / ANTITRUST-RISK
7. **Jurisdiction**: Which framework(s) the finding applies under

---

## Localization Notes

**[JURISDICTION-SPECIFIC — Additional US Considerations]**:

- Export controls: ITAR (22 CFR 120-130) and EAR (15 CFR 730-774) may restrict
  technology licensing to certain countries, entities, or uses; conduct restricted party
  screening before execution
- State law: California, New York, and Delaware have significant technology licensing
  case law; Delaware courts are often chosen for enforceability
- Section 365(n) election: ensure the agreement expressly acknowledges Section 365(n)
  protection for the licensee in the event of licensor's bankruptcy

**[JURISDICTION-SPECIFIC — Additional UK Considerations]**:

- CDPA 1988 ss. 50A-50C, 296A: Cannot contractually restrict backup copies, decompilation
  for interoperability, or observation of program functionality — any such restrictions
  are void
- UK post-Brexit exhaustion: confirm current UKIPO position on parallel imports from EEA
  at time of drafting; do not rely on EU exhaustion precedents without verification
- Unwired Planet global FRAND: UK courts will set global FRAND rates for SEP licensors;
  include a FRAND safe harbor provision for SEP-encumbered licenses

**[JURISDICTION-SPECIFIC — Additional EU Considerations]**:

- Software Directive 2009/24/EC: Cannot restrict legitimate user's decompilation right
  for interoperability under Article 6; backup copy right under Article 5(2)
- GDPR Article 28: Mandatory DPA for any processing of personal data — include as exhibit
- EU AI Act 2024/1689: For GPAI providers, mandatory copyright compliance policy and
  training data summary (Articles 53-55) [VERIFY implementation dates and scope]
- TTBER safe harbor: confirm market share calculations; if uncertain, treat as above
  threshold and conduct individual assessment

---

## Provenance

This skill was created using a 2-agent research pipeline on 2026-03-20 by Legalcode's
legal-skill-creator workflow. Research covered:

**Legal sources directly verified:**

- 35 U.S.C. §§ 154, 261, 262, 271 (Cornell LII)
- 17 U.S.C. §§ 101, 106, 204 (Cornell LII)
- 11 U.S.C. § 365(n) (Cornell LII)
- UK Patents Act 1977 ss. 46, 67, 130 (legislation.gov.uk)
- CDPA 1988 ss. 50A, 50B, 92, 101, 296A (legislation.gov.uk)
- UK VABEO SI 2022/516 (legislation.gov.uk)
- GDPR Article 28 (gdpr.eu)
- OpenRAIL license framework (Hugging Face blog)
- Meta Llama 2 Community License (ai.meta.com)
- GPL compliance guide (softwarefreedom.org)
- Unwired Planet v Huawei [2020] UKSC 37 (supremecourt.uk)

**Case law cited from research (verify through primary sources before relying):**

- Quanta Computer v. LG Electronics, 553 U.S. 617 (2008)
- Impression Products v. Lexmark International, 137 S. Ct. 1523 (2017)
- LaserDynamics v. Quanta Computer, 694 F.3d 51 (Fed. Cir. 2012) [VERIFY]
- Ericsson v. D-Link Systems, 773 F.3d 1201 (Fed. Cir. 2014) [VERIFY]
- Jacobsen v. Katzer, 535 F.3d 1373 (Fed. Cir. 2008) [VERIFY exact citation]
- Vernor v. Autodesk, 621 F.3d 1102 (9th Cir. 2010) [VERIFY]
- UsedSoft v. Oracle, CJEU C-128/11 (2012)
- Huawei v. ZTE, CJEU C-170/13 (2015)
- Hartford-Empire Co. v. United States, 323 U.S. 386 (1945) [VERIFY]
- Transparent-Wrap Machine Corp. v. Stokes and Smith Co., 329 U.S. 637 (1947) [VERIFY]

**Unverified or uncertain citations (marked [VERIFY] in text):**

- "Sunni v Dyson" (sublicensing rights — could not be confirmed; may be erroneous)
- "S&R Accounting v Xerox" (termination effects — could not be confirmed)
- EU TTBER 2023/1066 exact Article 4/5 text (regulation text was not directly retrievable
  through web fetch during research; framework confirmed from multiple secondary sources
  but exact article text needs EUR-Lex verification)
- EU AI Act GPAI article numbers and implementation dates
- UK UKIPO 2024 exhaustion regime position

**Key sources consulted:**

- DOJ/FTC Antitrust Guidelines for the Licensing of Intellectual Property (2017)
- SFLC Guide to GPL Compliance (softwarefreedom.org)
- Creative Commons FAQ on AI training
- UK Patents Act 1977 (legislation.gov.uk)
- CDPA 1988 (legislation.gov.uk)
- UK VABEO SI 2022/516 (legislation.gov.uk)
- Pinsentmasons/Out-Law: UK VABEO analysis

**Build date**: 2026-03-20
**Status**: Complete (research-backed, all [VERIFY] items flagged for primary source confirmation)
