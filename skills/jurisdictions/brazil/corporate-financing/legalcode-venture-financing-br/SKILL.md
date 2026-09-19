---
name: legalcode-venture-financing-br
description: Brazilian venture financing advisor covering the full lifecycle from pre-seed to exit. Use
  when a lawyer, founder, angel investor, VC fund manager, or in-house counsel asks to review or draft
  startup investment documents governed by Brazilian law, analyze a Brazilian term sheet, structure a
  FIP, assess IOF exposure on a convertible loan, advise on MISTO vs. Mútuo Conversível, check CVM compliance
  for a startup financing round, evaluate a Ltda-to-S.A. transformation, plan an offshore flip, or understand
  Brazilian venture capital regulatory requirements.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Brazilian venture financing advisor covering the full lifecycle from pre-seed to exit. Analyze, draft, and review MISTO (Latitud open-source), CICC (Contrato de Investimento em Capital Conversível), and Mútuo Conversível instruments. Assess Ltda vs. S.A. corporate structure selection, Acordo de Quotistas and Acordo de Acionistas terms, FIP (Fundo de Investimento em Participações) fund vehicle structuring under CVM Resolution 175/22 and its Normative Annex IV, Marco Legal das Startups (Lei Complementar 182/2021), CICC legislative framework (PLP 252/2023), CVM sandbox exemptions, IOF tax analysis, LGPD compliance, FGTS equity-compensation interaction, anti-dilution mechanics (broad-based weighted average), liquidation preference (preferência de liquidação), tag-along, drag-along, offshore flip structures, CADE antitrust thresholds, and ABStartups/ABVCAP market standards. Use when a lawyer, founder, angel investor, VC fund manager, or in-house counsel asks to review or draft startup investment documents governed by Brazilian law, analyze a Brazilian term sheet, structure a FIP, assess IOF exposure on a convertible loan, advise on MISTO vs. Mútuo Conversível, check CVM compliance for a startup financing round, evaluate a Ltda-to-S.A. transformation, plan an offshore flip, or understand Brazilian venture capital regulatory requirements.


# Legalcode Brazilian Venture Financing

> **Disclaimer**: This skill provides a framework for AI-assisted analysis of Brazilian
> venture financing instruments and structures. It does not constitute legal advice and
> is not a substitute for qualified Brazilian legal counsel (advogado). All outputs should
> be reviewed by a qualified professional licensed to practice law in Brazil (inscrito na
> OAB) before use. Brazilian securities, tax, and corporate law changes frequently —
> verify current applicability before relying on any provision described here. Statutory
> references, CVM resolutions, and pending legislative information carry hallucination risk
> — verify against authoritative sources (CVM portal, Planalto, Diário Oficial da União).
> Tax analysis (IOF, IRPJ, CSLL) requires engagement of a qualified Brazilian tax advisor.

---

## Purpose and Scope

This skill advises on the full Brazilian venture financing lifecycle from pre-seed
convertible instruments through institutional FIP fund investment, term sheet review,
corporate structure selection, regulatory compliance, and exit planning.

**Covers:**

- **Instruments:** MISTO, CICC (Contrato de Investimento em Capital Conversível), and
  Mútuo Conversível — mechanics, tax treatment, IOF exposure, conversion economics
- **Corporate structures:** Ltda (Sociedade Limitada) vs. S.A. (Sociedade Anônima) —
  selection criteria, Acordo de Quotistas, Acordo de Acionistas, transformação
- **Fund vehicles:** FIP (Fundo de Investimento em Participações) under CVM Resolution
  175/22 and prior CVM Instruction 578/2016 — types, governance, taxation, portfolio
  company requirements
- **Economic terms:** liquidation preference, anti-dilution, tag-along, drag-along,
  preemptive rights, ESOP/phantom equity, board composition
- **Regulatory compliance:** CVM sandbox exemptions, Marco Legal das Startups (LC
  182/2021), IOF, LGPD (Lei 13.709/2018), FGTS, CADE antitrust thresholds
- **Exit and cross-border structuring:** offshore flip mechanics, MISTO pre-approved
  flip, Delaware and Cayman Island restructurings, CADE notification requirements

**Does not:**

- Constitute legal advice or replace qualified Brazilian counsel (OAB-licensed advogado)
- Provide binding tax opinions — IOF, IRPJ, and CSLL analysis requires a tax advisor
- Cover public company securities offerings (IPO, CVM-registered offerings)
- Apply to real estate investment funds (FII), credit receivables funds (FIDC), or
  other non-PE/VC fund categories
- Draft final execution-ready documents — outputs are analysis and precedent language

---

## Jurisdiction and Governing Law

**Primary jurisdiction:** Federal Republic of Brazil (República Federativa do Brasil)

**Legal tradition:** Civil Law (direito civil codificado)

**Primary legislation:**

| Statute / Regulation                                 | Relevance                                                          |
| ---------------------------------------------------- | ------------------------------------------------------------------ |
| Código Civil (Lei 10.406/2002), Arts. 586–592        | Legal basis for mútuo (loan contract)                              |
| Código Civil, Arts. 1.052–1.087                      | Sociedade Limitada (Ltda) governance                               |
| Lei das S.A. (Lei 6.404/1976)                        | S.A. structure, preferred shares, shareholder agreements           |
| Lei Complementar 182/2021 (Marco Legal das Startups) | Startup legal framework, sandbox, CICC enablement                  |
| CVM Resolution 175/22                                | New investment fund framework; FIP in Normative Annex IV           |
| CVM Instruction 578/2016 (consolidated 2019)         | Prior FIP framework (superseded in part by CVM 175)                |
| Lei 13.709/2018 (LGPD)                               | Data privacy requirements                                          |
| Lei 8.036/1990 (FGTS)                                | Severance fund — payroll/equity interaction                        |
| PLP 252/2023 (CICC)                                  | Pending: Senate-approved April 2024; awaiting Câmara vote [VERIFY] |
| Lei 14.754/2023                                      | FIP taxation modernization                                         |
| Decreto-Lei 1.783/1980 / Lei 8.894/1994 (IOF)        | Tax on financial operations (convertible loans)                    |

[JURISDICTION-SPECIFIC] Brazilian corporate law is a federal matter (Código Civil, Lei
das S.A.); securities regulation is federal (CVM); tax is federal (Receita Federal).
Labor regulation (CLT, FGTS) is federal. Notarization requirements (tabelionato de
notas) vary by state.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming intent, the workflow pauses and asks when:

- The answer changes the instrument or structure recommended
- Multiple valid approaches exist depending on investor type or deal stage
- Tax treatment differs materially based on facts not yet provided
- Legislative status of pending law (CICC/PLP 252/2023) affects the analysis

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

Accept the engagement in any of these formats:

- **Document:** Term sheet, investment contract (Mútuo Conversível, MISTO document,
  Acordo de Quotistas/Acionistas), Contrato Social, or FIP fund documents
- **Scenario description:** Founder or investor describing the planned transaction
- **Specific question:** "Should we use MISTO or Mútuo Conversível?" / "How does IOF
  apply to our convertible loan?" / "How do we structure a FIP for seed investment?"

If no document or scenario is provided, prompt the user to supply one.

### Step 2: Gather Context

**⟁ CLARIFY** — Before analysis, ask these questions (skip any already answered):

1. **Deal stage and ticket size:**
   - Options: Pre-seed (< R$ 500K), Seed (R$ 500K–R$ 5M), Series A (R$ 5M–R$ 30M),
     Series B+ (R$ 30M+)
   - _Why this matters:_ Stage determines instrument suitability (MISTO/Mútuo for
     pre-seed/seed; equity rounds for Series A+) and CVM exemption applicability.

2. **Investor type:**
   - Options: Pessoa física (angel — individual), Pessoa jurídica (corporate angel),
     FIP/institutional fund, Latitud-connected fund, Family office, Strategic/corporate
     investor, Cross-border (foreign investor)
   - _Why this matters:_ IOF exposure (0% for pessoa física mutuante; 0.38% for PJ),
     CVM investor qualification, and offshore structuring needs all depend on investor type.

3. **Target company current structure:**
   - Options: Ltda, S.A. fechada, Not yet incorporated, Ltda transforming to S.A.
   - _Why this matters:_ Instrument mechanics differ by structure; transformação
     requirements may delay closing.

4. **Preferred instrument (if known):**
   - Options: MISTO (Latitud), Mútuo Conversível (custom), CICC (pending LC), Direct
     equity (Ltda quota or S.A. share subscription), FIP, Not yet decided
   - _Why this matters:_ Each instrument has distinct IOF, balance-sheet, and tax profiles.

5. **Cross-border / international dimension:**
   - Options: All-Brazilian (investors and company), Latam/international investor,
     Offshore holding already exists, Planning offshore flip for future round
   - _Why this matters:_ Offshore flip mechanics, MISTO pre-approved conversion,
     and foreign capital registration (FEMA-equivalent: Banco Central RDE-ROF) all
     depend on cross-border structure.

6. **Focus areas:**
   - Options: IOF / tax treatment, Instrument mechanics and conversion, Corporate
     structure (Ltda vs. S.A.), FIP fund structuring, CVM compliance, Exit / offshore
     flip, LGPD compliance, Full comprehensive review
   - Allow multiple selections.

If partial context is provided, state assumptions explicitly and proceed.

### Step 3: Load Legal Framework Reference

Use **legalcode-mcp** to retrieve current Brazilian legal authority:

**Search for:**

- CVM Resolution 175/22 and its Normative Annex IV (FIP rules)
- Lei Complementar 182/2021 (Marco Legal das Startups) current status
- PLP 252/2023 / CICC legislative status (Senate approval confirmed; Câmara vote pending)
- IOF Decree-Law 1.783/1980 current rate schedule for credit operations
- Lei 14.754/2023 FIP taxation provisions
- LGPD (Lei 13.709/2018) startup compliance guidance from ANPD

Save results to `/tmp/legalcode-br-vc-authority.md`.

**If legalcode-mcp is not connected:**

- Proceed with built-in knowledge; mark all statutory references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`

**⟁ CLARIFY** — If the governing instrument references foreign law (e.g., a MISTO with
offshore flip provisions referencing Delaware law), ask whether the user wants:

- Brazilian-law analysis only (instrument mechanics + IOF)
- Brazilian + Delaware dual-analysis (full offshore flip review)
- Just the Brazilian side flagged for foreign counsel

### Step 4: Instrument Selection Analysis

Assess which instrument is appropriate for the transaction. Apply the selection matrix
in **Module A** (Deep Topic Analysis) below.

**⟁ CLARIFY** — If the instrument is not yet decided, present the selection matrix
output and ask:

- "Based on the transaction profile, [MISTO / Mútuo Conversível / CICC / Direct Equity]
  appears most appropriate because [reason]. Do you want to proceed with this instrument
  or analyze an alternative?"

### Step 5: Corporate Structure Assessment

Assess the target company's current structure against the transaction requirements.
Apply **Module E** (Corporate Structure) below.

**⟁ CLARIFY** — If the company is an Ltda and the investor requires S.A. structure
(common for FIP investors), ask:

- "The investor's requirements may necessitate transformation from Ltda to S.A.
  (transformação). Do you want me to include transformação mechanics and timeline in
  the analysis, or assume the structure is acceptable as-is?"

### Step 6: Instrument-Specific Deep Analysis

Apply the relevant module from Deep Topic Analysis (Modules B, C, or D) to the
provided instrument document. For each term:

- Classify severity (CONFORME / ATENÇÃO / RISCO / CRÍTICO)
- Generate recommended language or remediation for ATENÇÃO, RISCO, and CRÍTICO items

**⟁ CLARIFY** — If reviewing an existing document with non-standard terms:

- "The [term] deviates from MISTO/market standard in [way]. Should I treat this as
  RISCO (flag for negotiation) or CRÍTICO (recommend not proceeding without amendment)?"

### Step 7: Economic Terms Review

Apply **Module F** (Economic Terms) to analyze the deal economics:

- Liquidation preference (preferência de liquidação)
- Anti-dilution mechanism (broad-based weighted average is Brazilian market standard)
- Tag-along and drag-along rights
- Preemptive rights (direito de preferência)
- Board composition
- Information and reporting rights
- ESOP / phantom equity / VSOP pool

### Step 8: Regulatory and Tax Compliance Check

Apply **Module G** (Regulatory Compliance) to verify:

- IOF analysis (0% pessoa física; 0.38% PJ-to-PJ credit operations)
- CVM sandbox or exemption applicability
- LGPD compliance status of the target company
- FGTS implications of equity compensation structures
- Simples Nacional eligibility impact (only Ltda; S.A. ineligible)

**⟁ CLARIFY** — For IOF:

- "Is the investor a pessoa física (individual) or pessoa jurídica (company/fund)?
  This determines whether IOF applies at 0% or 0.38% on the mútuo principal."

### Step 9: Fund Vehicle Analysis (if applicable)

If the investor is a FIP or institutional fund, or if the user is structuring a fund,
apply **Module H** (FIP Fund Structure). Cover:

- FIP type selection (Capital Semente / Empresas Emergentes / IE / PD&I)
- CVM Resolution 175/22 Normative Annex IV compliance
- Investor qualification requirements
- Taxation (15% IRRF; FIP-IE individual exemption)
- Portfolio company governance requirements

### Step 10: Quality Verification and Delivery

Before delivering analysis:

1. Run the 5 Citation Quality Gates silently. Revise failures before delivery.
2. For every CRÍTICO item, run the 3-pass Self-Interrogation.
3. Apply Confidence Scoring to all legal conclusions.
4. Complete the Glass Box Audit Trail template.
5. Deliver using the Output Format Template.

---

## Deep Topic Analysis

### Module A: Instrument Selection Matrix

Evaluate the appropriate instrument for the transaction stage and investor profile.

| Criterion                   | MISTO                        | Mútuo Conversível                                     | CICC (PLP 252/2023)                                      | Direct Equity                             |
| --------------------------- | ---------------------------- | ----------------------------------------------------- | -------------------------------------------------------- | ----------------------------------------- |
| **Legal nature**            | Mútuo (loan) with conversion | Mútuo (loan) with conversion                          | Patrimonial instrument (non-debt) [VERIFY — pending law] | Quota (Ltda) or share (S.A.)              |
| **Balance sheet treatment** | Liability (debt)             | Liability (debt)                                      | Equity instrument [VERIFY]                               | Equity                                    |
| **Interest rate**           | Zero                         | Market rate (≤1%/month typical) + monetary correction | Negotiable                                               | N/A                                       |
| **IOF (PJ investor)**       | 0.38% on principal           | 0.38% on principal                                    | Potentially exempt [VERIFY]                              | IOT on share subscription — no IOF credit |
| **IOF (PF investor)**       | 0%                           | 0%                                                    | 0% [VERIFY]                                              | 0%                                        |
| **Maturity date**           | None                         | Specified                                             | Negotiable                                               | N/A                                       |
| **Repayment obligation**    | Yes (if no conversion)       | Yes (if no conversion)                                | No (funds remain in company) [VERIFY]                    | N/A                                       |
| **Conversion trigger**      | Next equity round            | Next qualified round                                  | Negotiable event                                         | N/A                                       |
| **Offshore flip**           | Pre-approved (tax-efficient) | Requires renegotiation                                | TBD [VERIFY]                                             | Requires restructuring                    |
| **Template availability**   | Open source (Latitud)        | Custom negotiation                                    | Pending law [VERIFY]                                     | ABVCAP market standards                   |
| **Valuation required**      | No (cap + discount)          | No (cap + discount)                                   | Flexible                                                 | Yes (for investment)                      |
| **Best for stage**          | Pre-seed / Seed              | Pre-seed / Seed                                       | Pre-seed / Seed (pending)                                | Series A+                                 |
| **Tax certainty**           | High (by design)             | Medium (interpretive)                                 | High (via legislation) [VERIFY]                          | High                                      |
| **Investor control**        | None required                | Negotiable                                            | Negotiable                                               | Negotiated rights                         |

**Instrument selection guidance:**

1. **Choose MISTO when:** (a) investor is Latitud-connected or familiar with MISTO docs,
   (b) offshore flip anticipated within 24 months, (c) zero-interest structure preferred,
   (d) speed and low legal cost are priorities, (e) pre-seed or early seed stage.

2. **Choose Mútuo Conversível when:** (a) MISTO not familiar to investor, (b) highly
   customized conversion mechanics required, (c) all-Brazilian structure (no offshore
   flip planned), (d) investor requires specific investor protections not in MISTO template.

3. **Choose CICC when:** (a) PLP 252/2023 has been enacted [VERIFY before advising],
   (b) non-debt balance sheet treatment is critical to founder, (c) no repayment obligation
   upon non-conversion is required.

4. **Choose Direct Equity when:** (a) Series A or later, (b) FIP investor requires equity
   governance rights, (c) valuation has been established, (d) S.A. structure already in place.

### Module B: MISTO — Mútuo para Investimento Simplificado com Termos Otimizados

**Legal basis:** Código Civil Arts. 586–592 (mútuo/loan contract). MISTO is an
open-source convertible loan template developed by Latitud in collaboration with
law firms (Gunderson Dettmer, Pinheiro Neto, and BZCP). Available at latitud.com/misto.

**Key terms to review in any MISTO document:**

| Term                                   | Description                                         | Market Standard                                                  | Red Flags                                                             |
| -------------------------------------- | --------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------- |
| **Valor do Investimento**              | Principal amount of the mútuo                       | Market-driven                                                    | Verify correct amount stated                                          |
| **Teto de Avaliação (Valuation Cap)**  | Maximum pre-money valuation at conversion           | R$ 5M–R$ 50M (pre-seed/seed)                                     | No cap = uncapped conversion at market price; exposes investor        |
| **Desconto (Discount)**                | Reduction applied to next-round price               | 15%–30% typical                                                  | >30% discount suggests undervalued cap or investor aggression         |
| **Evento de Conversão**                | Trigger for conversion                              | Next qualified equity round                                      | Overly narrow definition may defer conversion indefinitely            |
| **Valor Mínimo do Evento**             | Minimum round size to trigger conversion            | R$ 2M–R$ 5M typical                                              | Too high = conversion never triggers; too low = triggers on any raise |
| **Direito de Participação (Pro-Rata)** | Investor right to participate in next round         | Optional; common for larger angels                               | Mandatory pro-rata can create drag on follow-on fundraising           |
| **MFN (Most Favored Nation)**          | Investor receives best terms from subsequent MISTOs | Common for early investors                                       | Unlimited MFN chain can create complex cap table mechanics            |
| **Cláusula de Mudança de Controle**    | Change of control conversion right                  | Conversion at lower of cap or 100% of principal returned         | Ensure trigger covers all M&A scenarios                               |
| **Conversão Offshore**                 | Pre-approved offshore flip mechanics                | MISTO includes pre-approved flip clause                          | Verify clause covers target offshore structure (Delaware/Cayman)      |
| **Flip Tributário**                    | Tax treatment of offshore flip                      | MISTO designed to minimize tax on flip [VERIFY with tax advisor] | Incorrect flip structure can trigger capital gains                    |

**MISTO conversion mechanics:**

Upon a qualifying Evento de Conversão, the investor converts at the lower of:

- **(a)** Teto de Avaliação (valuation cap) ÷ post-money capitalization × investment amount
- **(b)** Price per share/quota in the qualifying round × (1 − desconto)

**Example:**

- MISTO principal: R$ 500,000
- Valuation cap: R$ 10,000,000 (post-money)
- Series A round: R$ 30,000,000 post-money at R$ 0.30/share, 20% discount
- Conversion price (cap path): R$ 10M / [shares at Series A] per share
- Conversion price (discount path): R$ 0.30 × (1 − 0.20) = R$ 0.24/share
- Investor converts at R$ 0.24/share (discount path is lower)

**CRÍTICO triggers in MISTO review:**

- No valuation cap → investor has no downside protection on conversion price
- Evento de Conversão definition excludes insider rounds or strategic investors
- Flip clause absent or referencing wrong offshore entity type
- MISTO used for amounts exceeding R$ 10M (consider structured equity instead)
- Signing party lacks authority (procuração not attached for corporate signatories)

### Module C: CICC — Contrato de Investimento em Capital Conversível

**Legislative status:** PLP 252/2023 was approved by the Senate in April 2024 and is
pending vote in the Câmara dos Deputados as of 2026-03-21. [VERIFY current status before
advising — this skill cannot confirm enactment.]

**Key distinctions from Mútuo Conversível (once enacted):**

| Feature                     | CICC (Proposed)                                               | Mútuo Conversível (Current)                                 |
| --------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------- |
| **Debt classification**     | No — patrimonial instrument                                   | Yes — liability on balance sheet                            |
| **Repayment obligation**    | None — funds remain in company if not converted               | Yes — investor has liquid, certain credit if not converted  |
| **IOF treatment**           | Expected exemption [VERIFY post-enactment]                    | 0.38% (PJ investor)                                         |
| **Tax on non-conversion**   | No tax consequence [VERIFY]                                   | Risk of donation characterization [VERIFY with tax advisor] |
| **Tax on conversion**       | Cost basis = invested amount; gains taxed on future sale only | Same                                                        |
| **Balance sheet treatment** | Equity (not debt) [VERIFY]                                    | Liability                                                   |
| **Legislative clarity**     | High (once enacted)                                           | Medium — relies on interpretive guidance                    |

**How to advise on CICC before enactment:**

- Continue using Mútuo Conversível as the operative instrument
- Include CICC migration clause: "Upon enactment of CICC legislation (PLP 252/2023 or
  successor), the parties agree to reclassify this agreement as a CICC at the Investor's
  election, subject to mutual consent"
- Mark all CICC-specific legal conclusions with [VERIFY — pending legislation]

### Module D: Mútuo Conversível — Brazilian Convertible Loan

**Legal basis:** Código Civil Arts. 586–592 (mútuo — loan of fungible goods). The
conversion clause transforms the loan into an equity instrument upon a triggering event.

**Key terms analysis:**

**D.1 Interest Rate and Monetary Correction**

| Element                | Legal Requirement                                                                     | Market Standard                               | Red Flags                                                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Taxa de juros**      | No statutory minimum floor [VERIFY with tax advisor — some argue SELIC floor applies] | 0.5%–1.0% per month, or zero (MISTO-inspired) | Zero interest combined with favorable conversion may raise donation characterization risk [VERIFY with tax advisor] |
| **Correção monetária** | Optional                                                                              | IPCA or IGP-M indexation common               | Avoid combining SELIC rate + IPCA correction (double inflation accounting)                                          |
| **SELIC reference**    | Controversial — some practitioners apply as floor                                     | Better to use fixed rate + correction index   | SELIC includes inflation; adding IPCA creates double-counting                                                       |

**D.2 IOF — Imposto sobre Operações Financeiras**

| Investor Type                    | IOF Rate                      | Basis                                                                              |
| -------------------------------- | ----------------------------- | ---------------------------------------------------------------------------------- |
| Pessoa física (individual angel) | 0%                            | IOF-crédito does not apply to PF-to-PJ or PF-to-PF loans [VERIFY with tax advisor] |
| Pessoa jurídica (company, fund)  | 0.38% of principal            | IOF-crédito Decreto 6.306/2007 [VERIFY current rate with tax advisor]              |
| FIP                              | Subject to FIP-specific rules | [VERIFY with tax advisor and CVM counsel]                                          |

IOF is typically due at disbursement, paid by the borrower (startup). Include an IOF
responsibility clause specifying which party bears the cost.

**D.3 Conversion Mechanics**

Standard Mútuo Conversível conversion formula:

```
Shares/Quotas received = Principal + Accrued Interest + Monetary Correction
                         ──────────────────────────────────────────────────
                         MIN(Teto de Avaliação / Total Shares, Round Price × (1 − Desconto))
```

**Key terms:**

- **Teto de Avaliação (Cap):** Maximum effective per-share price at conversion
- **Desconto:** Discount to next-round price (15%–30% market standard)
- **Evento de Qualificação (Qualifying Event):** Equity round above minimum threshold
  (R$ 2M–R$ 5M typical), change of control, IPO, or specified date
- **Prazo de Vencimento (Maturity):** Date after which investor can demand repayment or
  conversion; typically 24–36 months; MISTO has no maturity

**D.4 Protective Provisions in Mútuo Conversível**

Common investor protections to review:

- **Direito de Informação:** Quarterly financials, annual audit, budget; standard
- **Direito de Participação Pro-Rata:** Right to invest in next round; optional
- **Cláusula MFN:** Most Favored Nation — investor receives best conversion terms of
  any subsequent mútuo; standard for early investors
- **Direito de Tag-Along:** If founders sell, investor converts and participates or
  receives pro-rata liquidation proceeds
- **Representações e Garantias (Reps & Warranties):** Typically limited in mútuo;
  standard reps on authority, no litigation, no MAC
- **Negative Covenants:** Restrictions on taking on debt, new equity, change of control
  without investor consent — flag if overly restrictive

**CRÍTICO triggers in Mútuo Conversível review:**

- No maturity date AND no conversion trigger → instrument may never convert or mature
- Conversion formula missing or ambiguous → litigation risk on conversion event
- No IOF allocation clause → tax liability unclear
- PJ investor; IOF not addressed → undisclosed tax liability for startup
- Donation characterization risk if interest is zero and conversion terms are
  excessively favorable → [VERIFY with tax advisor]
- Interest rate exceeds 1%/month → potential usury characterization [VERIFY]
- No cap on conversion → investor receives windfall at high valuation; founders
  severely diluted
- Governing law is foreign law → Brazilian mútuo law may still apply (mandatory norms)

### Module E: Corporate Structure — Ltda vs. S.A.

**E.1 Ltda (Sociedade Limitada)**

Governed by Código Civil Arts. 1.052–1.087. The most common early-stage startup vehicle.

**Key features:**

- Capital divided into **cotas** (quotas), not shares
- No minimum capital requirement
- Governed by **Contrato Social** (articles of organization) + optional **Acordo de Quotistas**
- Transfers of cotas require consent of quotaholders (unless Contrato Social waives)
- Cannot issue preferred quotas with full S.A.-equivalent rights (limited flexibility)
- **Simples Nacional eligible** (if annual revenue ≤ R$ 4.8M and activity qualifies)
- Transformation to S.A. (transformação) requires unanimous approval of all quotaholders
  under default Civil Code rule [VERIFY — some practitioners argue simple majority;
  confirm in Contrato Social]

**When Ltda is appropriate:**

- Pre-seed / seed stage with 2–4 founders
- No institutional FIP investor (most FIPs accept Ltda [VERIFY fund documents])
- Simples Nacional tax regime desired (revenue < R$ 4.8M)
- Speed of incorporation (Ltda registration faster and cheaper)
- No immediate plan for preferred share classes requiring full S.A. mechanics

**Acordo de Quotistas (Quotaholders' Agreement):**

| Provision                          | What to Review                                     | Market Standard                                  |
| ---------------------------------- | -------------------------------------------------- | ------------------------------------------------ |
| **Direito de Preferência**         | Pre-emptive right on quota transfer                | 30-day exercise period; proportional to holding  |
| **Tag-Along**                      | Minority investor right to sell alongside majority | 100% tag-along right for all investors           |
| **Drag-Along**                     | Majority right to force minority sale              | Threshold 75%–85%; 30-day notice; fair valuation |
| **Vesting do Fundador**            | Founder quota vesting schedule                     | 4 years, 12-month cliff; standard                |
| **Restrição de Transferência**     | Lock-up on quota transfers                         | 12–24 months from closing                        |
| **Quórum Especial**                | Supermajority required for key decisions           | 75%–85% for M&A, new debt, ESOP, equity rounds   |
| **Direitos de Informação**         | Investor information rights                        | Quarterly unaudited + annual audited financials  |
| **Non-Compete**                    | Founder non-compete post-exit                      | 12–24 months; geographic scope limited to Brazil |
| **Cláusula de Saída (Liquidação)** | Liquidation waterfall                              | 1x non-participating preference; market standard |

**E.2 S.A. — Sociedade Anônima**

Governed by Lei 6.404/1976 (Lei das S.A.). Required for Series A+ institutional investment,
FIP structures, and eventual IPO path.

**Key advantages over Ltda:**

- Issuance of **ações preferenciais** (preferred shares) with full VC-standard rights
  (liquidation preference, conversion, anti-dilution, protective provisions)
- **Acordo de Acionistas** enforced directly against company under Art. 118 (board and
  voting agreement binding on company secretary/CFO)
- Easier share transfer (no consent required for registered shares unless restricted
  by articles)
- IPO-ready (CVM registration requirement; minimum 25% free float)
- Foreign direct investment more straightforward (Banco Central RDE-IED registration)

**Acordo de Acionistas (Art. 118, Lei das S.A.):**

- Must be filed with company and recorded in share registry to bind third parties
- Covers: voting, share purchase/sale, preemptive rights, governance
- Board composition agreements binding on company under Art. 118

**E.3 Transformação — Ltda to S.A.**

Process to convert a Ltda into a S.A.:

1. Quotaholders approve transformação (unanimous vote under default rules; check Contrato
   Social for any alternative threshold)
2. Prepare new Estatuto Social (articles of association for S.A.)
3. Appoint board (Conselho de Administração) and CEO (Diretor Executivo)
4. Junta Comercial registration (JUCESP, JUCERJ, etc.)
5. Update all bank accounts, contracts, and tax registrations
6. Banco Central update if foreign investors present (RDE-IED reclassification)

**Timeline:** 30–90 days depending on state Junta Comercial backlog.

**CRÍTICO triggers in structure assessment:**

- Investor requires preferred shares → Ltda cannot adequately accommodate → S.A. required
- FIP investor has fund documents requiring portfolio company governance per Lei das S.A.
  → Ltda transformation mandatory
- Company in Simples Nacional planning S.A. transformation → Simples Nacional eligibility
  lost → tax regime change required → [VERIFY with tax advisor]
- Unanimous transformação approval required but dissenting quotaholder exists → deal blocker

### Module F: Economic Terms — Term Sheet Analysis

**F.1 Liquidation Preference (Preferência de Liquidação)**

Brazilian market standard: **1x non-participating** liquidation preference.

| Type                      | Description                                                             | Brazil Market Standard                            |
| ------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------- |
| **1x Non-Participating**  | Investor receives 1× investment back OR converts pro-rata — not both    | Standard (96%+ of deals per ABVCAP data) [VERIFY] |
| **1x Participating**      | Investor receives 1× back PLUS pro-rata share of remainder              | Founder-unfavorable; rare in Brazil               |
| **>1x Non-Participating** | Investor receives multiple of investment back                           | Aggressive; occurs in distressed or down rounds   |
| **Full Ratchet**          | Anti-dilution converts enough shares to fully compensate for down round | Uncommon; considered punitive to founders         |

CRÍTICO trigger: Participating liquidation preference above 1× without founder-approved
override → flag for founder negotiation.

**F.2 Anti-Dilution (Proteção contra Diluição)**

Brazilian market standard: **Broad-Based Weighted Average (BWAA)**.

**BWAA formula:**

```
New Conversion Price = (Old CP × Old Shares Outstanding + Investment Amount)
                       ─────────────────────────────────────────────────────
                       (Old Shares Outstanding + New Shares Issued in Down Round)
```

| Mechanism           | Description                                                            | Brazil Market Standard           |
| ------------------- | ---------------------------------------------------------------------- | -------------------------------- |
| **Broad-Based WA**  | Weighted average using all outstanding shares (including options pool) | ✅ Standard                      |
| **Narrow-Based WA** | Uses only preferred shares in denominator                              | ❌ More aggressive; minority use |
| **Full Ratchet**    | Conversion price drops to down-round price                             | ❌ Punitive; avoid               |
| **Pay-to-Play**     | Non-participating investors lose anti-dilution rights                  | Negotiable; growing use          |

CRÍTICO trigger: Full ratchet anti-dilution without market justification → red flag.

**F.3 Tag-Along and Drag-Along**

| Right                                     | What It Is                                                            | Market Standard (Brazil)                                                                                                        |
| ----------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Tag-Along (Direito de Acompanhamento)** | Minority investor can sell at same price/conditions if majority sells | 100% tag-along for all investors; mandatory under Lei das S.A. Art. 254-A for public companies; negotiate for private companies |
| **Drag-Along (Direito de Arrasto)**       | Majority forces minority to sell in approved M&A                      | Threshold 75%–85%; fair valuation; 30-day notice; investors typically carved out below $X threshold                             |
| **Co-Sale (Direito de Venda Conjunta)**   | Alternative to tag-along; investor sells pro-rata alongside founder   | Less common; used where tag-along is limited                                                                                    |

ATENÇÃO: Tag-along absent → minority investor has no exit protection in founder-sale
scenario.

**F.4 Preemptive Rights (Direito de Preferência)**

Under Lei das S.A. Art. 171, shareholders have preemptive rights in capital increases
proportional to their holdings (30-day exercise period unless statute shortens). For Ltda,
Código Civil Art. 1.081 applies equivalent right.

Review for:

- Exercise period (30 days statutory minimum; often shortened by agreement)
- Waiver mechanics (board authority to waive for strategic investors)
- ROFR (Right of First Refusal) on secondary transfers between shareholders

**F.5 Board Composition**

| Structure                             | When Used                                    | Market Standard                                                  |
| ------------------------------------- | -------------------------------------------- | ---------------------------------------------------------------- |
| **Conselho de Administração (Board)** | S.A. (mandatory if public; optional private) | Required for FIP portfolio companies with governance obligations |
| **Conselho Fiscal (Fiscal Council)**  | Oversight body (not a board)                 | Activated by minority shareholders in conflict scenarios         |
| **Advisory Board**                    | Informal; common in Ltda                     | No fiduciary duties; founders retain control                     |

Typical seed-stage board: 2 founders + 1 investor seat + 1 independent. Series A: 5
members (2 founders + 2 investors + 1 independent).

**F.6 ESOP / Phantom Equity**

Brazilian startups use two equity compensation structures:

| Structure                   | Description                                                                        | Tax Treatment                                                                                                                  |
| --------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Stock Option Plan (SOP)** | Right to purchase quotas/shares at fixed price; typically 4-year vest/1-year cliff | Capital gains on sale (15%–22.5% IRPF scale) — no income tax at grant or vest if properly structured [VERIFY with tax advisor] |
| **Phantom Equity / VSOP**   | Cash settled; mirrors equity upside without actual share issuance                  | Income tax (IRRF) at settlement — less tax-efficient than real options; avoid for key employees [VERIFY]                       |
| **Restricted Quota Grant**  | Actual quota granted subject to vesting conditions                                 | Potential income characterization on grant if below fair market value [VERIFY with tax advisor]                                |

ATENÇÃO: Poorly structured options can be characterized as employment compensation →
INSS (social security) and IRRF withholding obligations → [VERIFY with tax advisor and
employment counsel].

### Module G: Regulatory and Tax Compliance

**G.1 CVM Sandbox and Startup Exemptions**

The CVM Sandbox (Resolução CVM 29/2021 and successors) allows fintech and startup
companies to test innovative business models with regulatory relaxation. For standard
venture financing rounds:

- Mútuo Conversível and MISTO are **not securities** → no CVM registration required [VERIFY]
- Direct equity subscription (S.A. shares) to closed investor group (< 50 investors) →
  CVM exemption under Instrução 588/2017 (crowdfunding) or private placement exception [VERIFY]
- FIP offering to qualified investors → CVM registration of fund required

**⟁ CLARIFY** — If the round has more than 50 investors or uses any form of public
solicitation, ask: "Is this round limited to private solicitation with fewer than 50
investors? Public solicitation may trigger CVM registration requirements."

**G.2 Marco Legal das Startups (Lei Complementar 182/2021)**

Key provisions for venture financing:

- **Sandbox de inovação:** Startups may apply for CVM or Banco Central sandbox to test
  innovative financial structures for up to 2 years with regulatory relaxation
- **Investidor-Anjo (Angel Investor) framework:** Defines angel investment model allowing
  investment in Ltda startups without quotaholder liability (Art. 61-A to 61-D of Lei
  Complementar 123/2006 as amended) [VERIFY current rules post-LC 182]
- **CICC enablement:** LC 182/2021 created the framework for CICC as a recognized
  instrument; PLP 252/2023 expands CICC definition

**G.3 LGPD (Lei Geral de Proteção de Dados — Lei 13.709/2018)**

LGPD compliance has become a standard investor due diligence item. For portfolio companies:

| LGPD Area                      | What to Assess                                                      | Risk if Non-Compliant                                               |
| ------------------------------ | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Legal basis for processing** | All personal data processing mapped to LGPD legal bases (Art. 7/11) | ANPD fine up to 2% of revenue in Brazil (max R$ 50M per infraction) |
| **Data subject rights**        | Rights exercise process (access, correction, deletion, portability) | ANPD enforcement; reputational risk                                 |
| **DPO appointment**            | Encarregado (DPO) designated (ANPD simplified rules for startups)   | Non-material for very small startups under ANPD simplified regime   |
| **Third-party data sharing**   | Data processing agreements with processors                          | Liability transfer to startup if processor violates LGPD            |
| **Privacy policy**             | Publicly accessible, specific to data types collected               | ANPD enforcement; customer trust                                    |
| **Security measures**          | Technical and organizational measures for data protection           | Incident notification obligation (Art. 48)                          |

**G.4 IOF — Summary**

| Transaction                              | Investor Type              | IOF Rate                                                    | Charged On          |
| ---------------------------------------- | -------------------------- | ----------------------------------------------------------- | ------------------- |
| Mútuo Conversível or MISTO               | Pessoa física (PF)         | 0%                                                          | N/A                 |
| Mútuo Conversível or MISTO               | Pessoa jurídica (PJ), fund | 0.38% + 0.0041%/day (up to 365 days) [VERIFY current rates] | Principal disbursed |
| Direct equity subscription (S.A. shares) | Any                        | No IOF-crédito                                              | N/A                 |
| CICC (once enacted)                      | Any                        | Expected exemption [VERIFY]                                 | TBD                 |

Note: IOF-crédito accrues daily on the outstanding principal at 0.0041%/day up to the
annual 0.38% ceiling. Prepayment reduces effective IOF. [VERIFY current rate schedule
with Receita Federal or tax advisor]

**G.5 FGTS and Labor Considerations**

Equity compensation structures interact with Brazilian labor law:

- FGTS is calculated on cash salary only; equity grants are not FGTS-subject if properly
  structured as options (not salary substitutes) [VERIFY with labor/tax advisor]
- TST (Superior Tribunal do Trabalho) has case law characterizing options as salary
  in some circumstances → proper vesting structure critical [VERIFY]
- Employee ESOP grants: use SOP (stock option plan) with exercise price, vesting cliff,
  and shareholder agreement treatment to minimize salary-characterization risk

### Module H: FIP Fund Structure (CVM Resolution 175/22)

**H.1 FIP Types Under CVM 175**

| FIP Type                    | Target Company Revenue         | Stage Focus            | Tax Benefit                                   |
| --------------------------- | ------------------------------ | ---------------------- | --------------------------------------------- |
| **FIP-Capital Semente**     | ≤ R$ 16M annual gross revenue  | Pre-seed / Seed        | Standard IRRF 15%                             |
| **FIP-Empresas Emergentes** | ≤ R$ 300M annual gross revenue | Series A/B             | Standard IRRF 15%                             |
| **FIP-IE (Infraestrutura)** | Infrastructure projects        | Growth/Project finance | Individual investors: 0% IRRF (isenção total) |
| **FIP-PD&I (P&D)**          | R&D and innovation companies   | Technology/Innovation  | Tax incentives [VERIFY current regime]        |
| **FIP-Multiestratégia**     | Any                            | Multiple stages        | Standard IRRF 15%                             |

**H.2 Key CVM Resolution 175/22 Requirements (Normative Annex IV — FIP)**

**Compartmentalization (Compartimentos):**

- CVM 175 permits FIPs to establish multiple share classes and compartments
- Each compartment can have distinct investment objectives, expense structures, and
  investor profiles
- Enables single FIP vehicle to run seed + growth capital strategies simultaneously
- **Practice application:** Structure FIP-Capital Semente compartment for early-stage
  investments; FIP-Empresas Emergentes compartment for follow-on growth investments

**Effective Influence Requirement:**

- FIP must maintain "efetiva influência" (effective influence) over portfolio companies
- Satisfied by: board seat, veto rights over material decisions, or other governance
  mechanisms providing active influence [VERIFY CVM 175 Annex IV exact text]
- **Venture carve-out:** CVM has historically permitted relief for early-stage investments
  where control is impractical [VERIFY current CVM guidance]

**Valuation Requirements:**

- Quarterly mark-to-market valuation of portfolio companies
- Permissible methodologies: DCF, comparable company analysis, cost basis (for early-stage)
- FIP administrator (administrador fiduciário) bears fiduciary duty on valuations

**Investor Qualification:**

- FIP open only to **investidores qualificados** (qualified investors): institutional
  investors, high-net-worth individuals, professional investors meeting CVM thresholds
- Minimum investment typically R$ 1M (fund-dependent)

**H.3 FIP Taxation (Lei 14.754/2023)**

| Investor Type                   | Tax Rate                        | Notes                                                |
| ------------------------------- | ------------------------------- | ---------------------------------------------------- |
| Pessoa física                   | 15% IRRF on gains/distributions | Semi-annual "come-cotas" rule does NOT apply to FIPs |
| Pessoa jurídica (non-financial) | 15% on FIP quota gains          | CSLL additional                                      |
| FIP-IE individual investor      | 0% (isenção total)              | Infrastructure projects only                         |
| Foreign investor                | 15% IRRF                        | Subject to tax treaty relief [VERIFY DTA]            |

**H.4 FIP Deal Terms for Portfolio Companies**

Institutional FIP investors typically require:

- S.A. structure (or Ltda with S.A.-equivalent governance protections)
- Conselho de Administração with FIP-designated board observer or director
- Quarterly unaudited financial statements; annual audited (Big Four preferred)
- Budget approval rights (annual budget requires FIP consent)
- Drag-along at 75%+ threshold; tag-along at 100%
- Anti-dilution (BWAA)
- 1x non-participating liquidation preference
- ROFR on secondary transfers among shareholders
- LGPD compliance covenant in investment agreement
- ESG policy covenant (growing ABVCAP requirement)

### Module I: Exit and Cross-Border Structuring

**I.1 Offshore Flip — MISTO Pre-Approved Structure**

MISTO includes pre-approved mechanics for converting a Brazilian structure into a foreign
holding company (typically Delaware LLC or Cayman Islands structure):

- Designed to allow Brazilian founders to flip to offshore structure for international
  investor rounds without renegotiating MISTO terms
- Tax treatment: MISTO documentation includes provisions designed to minimize Brazilian
  capital gains tax on the flip [VERIFY with Brazilian tax advisor — tax treatment of
  offshore flip remains subject to interpretation]

**I.2 Offshore Flip — Traditional Mútuo Conversível Structure**

Without MISTO-specific provisions:

1. Create foreign holding company (Delaware C-Corp, Cayman exempted company, or BVI)
2. Brazilian founders exchange Ltda/S.A. equity for holding company equity
3. MISTO/Mútuo holder must consent and renegotiate conversion rights into foreign entity
4. Potential Brazilian capital gains tax on founder equity exchange [VERIFY with tax advisor]
5. Banco Central registration of foreign direct investment (RDE-IED) required

**I.3 CADE Antitrust Notification**

For M&A exits, CADE (Conselho Administrativo de Defesa Econômica) review required when:

- Target company: annual Brazilian revenues ≥ R$ 75M (check current thresholds — revised
  2022 [VERIFY]) OR
- Acquirer (or its economic group): revenues ≥ R$ 750M in Brazil

**For early-stage startups:** CADE review rarely applies (revenues below threshold).
However, acquirer must confirm its own Brazilian revenue against CADE thresholds.

**Notification timeline:** File within 15 business days of transaction signing.
CADE Phase I: 30 days. Phase II: 240 days (if competition concerns).

**I.4 Tax on Exit (Founder Perspective)**

| Event                                    | Tax Type                      | Rate                                       |
| ---------------------------------------- | ----------------------------- | ------------------------------------------ |
| Sale of S.A. shares (Brazilian resident) | IRPF ganho de capital         | 15%–22.5% progressive (gain > R$ 35K/year) |
| Sale of Ltda quotas                      | IRPF ganho de capital         | 15%–22.5% progressive                      |
| IPO (retention of post-lockup shares)    | IRPF on sale of listed shares | 15% (above R$ 20K/month threshold)         |
| FIP quota redemption (PF)                | IRRF 15%                      | Deferred to redemption/distribution        |

---

## Severity Classification

Use this 4-tier system for every finding:

| Tier | Label        | Portuguese                             | What It Means                                           | Required Action                                             |
| ---- | ------------ | -------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------- |
| 🟢   | **CONFORME** | Conforme                               | Term is market-standard and appropriate                 | Note for awareness only                                     |
| 🟡   | **ATENÇÃO**  | Atenção                                | Term deviates from market standard; negotiable          | Generate recommended language; present as negotiation point |
| 🔴   | **RISCO**    | Risco                                  | Term creates material legal, tax, or financial risk     | Escalate to counsel; provide remediation language           |
| ⛔   | **CRÍTICO**  | Crítico — Não Prosseguir Sem Resolução | Term creates deal-breaking risk or is legally deficient | Do not execute until resolved; provide corrected language   |

**CRÍTICO auto-triggers (flag immediately without CLARIFY):**

- Zero interest rate in Mútuo Conversível where investor is PJ → IOF characterization risk +
  potential donation characterization if conversion terms are excessively favorable [VERIFY]
- Conversion formula absent or ambiguous → litigation risk
- S.A. transformation required but dissenting quotaholder → deal blocker
- FIP with no "effective influence" over portfolio company → CVM 175 compliance failure [VERIFY]
- Liquidation preference > 1× participating → serious founder dilution risk; flag as CRÍTICO
  and present alternatives
- Offshore flip without Brazilian tax analysis → unquantified capital gains exposure

---

## Actionable Output per Finding

For each ATENÇÃO, RISCO, or CRÍTICO item, provide:

1. **Issue identified** (plain language description)
2. **Severity** (ATENÇÃO / RISCO / CRÍTICO + basis)
3. **Legal basis** ([statute/article] + [VERIFY] if unconfirmed)
4. **Recommended language** (substitute clause or amendment)
5. **Negotiation rationale** (why this matters to the party represented)
6. **Fallback position** (minimum acceptable alternative)

**Example output format:**

```
⛔ CRÍTICO — Ausência de Fórmula de Conversão

Issue: The Mútuo Conversível does not define the conversion price formula.
Upon a qualifying equity round, the parties will be unable to agree on conversion
mechanics without litigation risk.

Legal basis: CC Arts. 586–592 (mútuo); absence of essential term (Art. 104, II CC)
may render the conversion clause void for uncertainty. [VERIFY with Brazilian counsel]

Recommended language:
  "O Valor de Conversão será igual ao menor valor entre: (i) o Teto de Avaliação
  dividido pelo número total de Cotas/Ações na base pós-dinheiro do Evento de
  Qualificação; e (ii) o preço por Cota/Ação pago pelos novos investidores no
  Evento de Qualificação multiplicado por (1 menos o Desconto)."

Negotiation rationale: Without a defined formula, the convertible loan cannot
convert automatically — the investor must negotiate separately at each round,
creating delay and dispute risk.

Fallback position: Accept any deterministic formula (cap + discount, or cap-only)
as long as the mechanics are unambiguous.
```

---

## Prioritization Framework

| Priority                | Label                                                 | When to Apply                                      |
| ----------------------- | ----------------------------------------------------- | -------------------------------------------------- |
| **P1 — Essencial**      | Deal will fail or be void without resolution          | CRÍTICO items; missing essential terms             |
| **P2 — Material**       | Significant financial or legal exposure if unresolved | RISCO items; IOF unaddressed; conversion ambiguity |
| **P3 — Negociação**     | Below-standard terms worth negotiating                | ATENÇÃO items; below-market economics              |
| **P4 — Administrativa** | Minor drafting improvements                           | Missing boilerplate; notice provisions             |

Typical issue prioritization for a seed-stage Mútuo Conversível review:

- P1: Conversion formula present/correct; IOF clause present; signing authority confirmed
- P2: Cap/discount in market range; maturity date appropriate; negative covenants not
  overly restrictive
- P3: Information rights; MFN clause; pro-rata right mechanics
- P4: Governing law clause; notice provisions; counterparts provision

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate                       | Rule                                                                                                 | Fail Action                                             |
| -------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **Fonte (Source)**         | Every legal claim cites a specific statute, CVM resolution, or established principle                 | Add citation or mark [VERIFY]                           |
| **Formato (Format)**       | Citations follow Brazilian legal format: "Lei X.XXX/YYYY, Art. XX" or "CVM Resolução XXX/YY, Art. X" | Fix format                                              |
| **Vigência (Currency)**    | Every cited provision checked for amendment, revocation, or pending reform                           | Flag [VERIFICAR VIGÊNCIA]                               |
| **Domínio (Scope)**        | Analysis stays within Brazilian law scope; no inadvertent application of US/EU concepts              | Remove or flag cross-jurisdictional bleed               |
| **Confiança (Confidence)** | Uncertainty explicitly stated; pending legislation flagged                                           | Add confidence qualifier; mark [VERIFY] for pending law |

### Self-Interrogation for CRÍTICO Items

For any CRÍTICO finding, apply this 3-pass review before delivery:

**Pass 1 — Cadeia Legal:** Does the risk assessment follow logically from the cited
statutory or regulatory authority? Would a Brazilian court or the CVM actually reach
this conclusion on these facts?

**Pass 2 — Completude:** Have all relevant statutes (Código Civil, Lei das S.A., CVM
regulations, IOF legislation, LGPD, Marco Legal das Startups) been considered? Are there
regulatory dimensions not yet addressed?

**Pass 3 — Contra-Argumento:** What is the strongest argument against this CRÍTICO
classification? Under what circumstances might a qualified Brazilian practitioner accept
this risk or structure it differently?

### Confidence Scoring

| Level        | Range     | Meaning                                         | Action                                      |
| ------------ | --------- | ----------------------------------------------- | ------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled Brazilian law; explicit statutory text  | State with confidence                       |
| **High**     | 0.80–0.94 | Strong authority; limited judicial disagreement | State with brief caveat                     |
| **Probable** | 0.60–0.79 | Good arguments; court decisions vary or sparse  | State with reasoning and alternatives       |
| **Possible** | 0.40–0.59 | Genuinely uncertain; no clear authority         | Flag for qualified Brazilian counsel review |
| **Unlikely** | 0.0–0.39  | Weak basis; pending legislation; speculation    | Do not assert; flag [INCERTO]               |

**Brazilian law calibration examples:**

- IOF at 0% for PF investor: Definite (0.95)
- CICC enactment date: Unlikely (0.15) — pending legislation
- Donation characterization risk on zero-interest mútuo: Possible (0.45) — interpretive
- MISTO offshore flip tax efficiency: Probable (0.65) — requires tax advisor confirmation
- Full ratchet anti-dilution being ABVCAP non-standard: High (0.85)

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-venture-financing-br"
  mode: "Created from scratch (Mode A)"
  topic: "Brazilian venture financing — MISTO, CICC, Mútuo Conversível, FIP, Ltda/S.A."
  jurisdiction: "Brazil (federal)"
  source_skills_analyzed: 0
  enhancement_type: "Create"
  legalcode_mcp: "[Connected / Not connected — state per session]"
  research_reference_file: "[/tmp/legalcode-br-vc-authority.md or 'Not created']"
  instruments_reviewed: "[MISTO / Mútuo Conversível / CICC / Direct Equity / FIP]"
  corporate_structure: "[Ltda / S.A. / FIP / Not reviewed]"
  iof_analysis_completed: "[Yes / No / N/A]"
  lgpd_assessment_completed: "[Yes / No / N/A]"
  cvm_compliance_checked: "[Yes / No / N/A]"
  offshore_flip_analyzed: "[Yes / No / N/A]"
  cicc_status_flagged: "[Yes — pending legislation noted / N/A]"
  quality_score: "[X]/40"
  completeness: "18/18 elements"
  citations_verified: "[N VERIFIED] / [N UNVERIFIED — marked [VERIFY]]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  findings_summary:
    critico: "[N]"
    risco: "[N]"
    atencao: "[N]"
    conforme: "[N]"
  limitations:
    - "CICC (PLP 252/2023) status is pending as of skill creation — verify enactment before advising"
    - "IOF rates and calculation methodology require verification with current Receita Federal guidance"
    - "Tax conclusions (IRPJ, CSLL, FGTS equity interaction) require qualified Brazilian tax advisor"
    - "FIP structuring requires CVM-registered administrator (administrador fiduciário)"
    - "Offshore flip mechanics require bilateral analysis (Brazilian + foreign jurisdiction counsel)"
    - "legalcode-mcp connectivity not verified — all citations marked [VERIFY] if not connected"
  reviewer: "AI-assisted — requires qualified Brazilian counsel (OAB-licensed advogado) review"
```

---

## Anti-Patterns

What NOT to do when advising on or reviewing Brazilian venture financing:

1. **Using a SAFE directly without adaptation.** US SAFE (Y Combinator) is not suited
   to Brazilian law — it does not address IOF, lacks mútuo legal foundation, and may
   be characterized as a donation or irregular financial operation. Always use MISTO,
   Mútuo Conversível, or (once enacted) CICC instead.

2. **Ignoring IOF on PJ investor loans.** Failing to address IOF when the investor is
   a pessoa jurídica creates an unbooked tax liability for the startup (0.38% of
   principal). Always include an IOF allocation clause in PJ-investor mútuos.

3. **Using zero interest in a Mútuo Conversível with a PJ investor without tax advice.**
   Zero-interest loans between jurídicas may be challenged as taxable donations by
   Receita Federal if conversion terms are excessively favorable. MISTO is designed
   to address this; custom mútuos must include tax counsel sign-off.

4. **Combining SELIC interest with IPCA monetary correction.** SELIC already incorporates
   inflation; adding IPCA creates double inflation accounting. Use one or the other, not both.

5. **Advising on CICC as if it is enacted.** PLP 252/2023 was Senate-approved but the
   Câmara vote had not occurred as of March 2026. [VERIFY.] Never rely on CICC as
   operative law without confirming enactment and checking for any revisions.

6. **Structuring a FIP without CVM-registered administrator.** FIPs require a registered
   administrador fiduciário. Operating without one is a CVM violation. Fund managers
   must also be registered with CVM as gestores.

7. **Omitting the valuation cap in a convertible instrument.** A Mútuo Conversível or
   MISTO without a Teto de Avaliação provides no economic protection to early investors;
   they convert at full next-round valuation, losing their early risk premium.

8. **Allowing FIP "effective influence" requirement to go unaddressed.** CVM 175 Annex IV
   requires FIPs to maintain effective influence over portfolio companies. Failing to
   negotiate governance rights creates regulatory exposure for the fund manager.

9. **Recommending full ratchet anti-dilution.** Full ratchet is punitive to founders,
   nearly unknown in Brazilian market practice, and may deter future investors. Always
   recommend broad-based weighted average unless there are extraordinary circumstances.

10. **Failing to address Simples Nacional loss on S.A. transformation.** A Ltda in Simples
    Nacional that transforms to S.A. automatically loses Simples Nacional eligibility.
    Tax regime transition to Lucro Presumido or Lucro Real must be planned and budgeted.

11. **Treating offshore flip as tax-free without Brazilian tax advisor confirmation.**
    MISTO is designed for tax-efficient offshore flip, but the Brazilian tax treatment
    of the flip depends on facts not visible in the contract document. Always recommend
    Brazilian tax advisor engagement before executing any offshore restructuring.

12. **Ignoring LGPD in VC due diligence.** ANPD fines can reach 2% of Brazilian annual
    revenue (up to R$ 50M per infraction). A portfolio company with LGPD violations
    creates liability that survives acquisition and reduces exit value. LGPD compliance
    covenant in investment agreement is market standard.

13. **Structuring phantom equity (VSOP) without IRRF analysis.** Cash-settled phantom
    equity (VSOP) is treated as ordinary income (IRRF withheld by employer at payment)
    — less tax-efficient than a properly structured option plan. Founders often prefer
    VSOPs for speed, but employees bear significantly higher tax. Disclose the difference.

14. **Drafting a drag-along below 75% threshold.** Drag-along at 50%+1 means a bare
    majority of investors can force a sale over founders' and minority objections. Market
    standard in Brazil is 75%–85% threshold; below this, the clause is founder-unfavorable
    and creates closing risk in institutional rounds.

15. **Assuming unanimous transformação approval.** Default Código Civil rule for Ltda
    transformation to S.A. requires unanimous quotaholder approval. A single dissenting
    angel investor can block the transformation needed for a Series A. Negotiate a lower
    threshold (e.g., 85%) in the Acordo de Quotistas at seed stage.

16. **Omitting CADE analysis in M&A exit planning.** Even when the startup revenue is
    low, the acquirer's Brazilian revenue may independently trigger CADE notification.
    Failure to notify CADE is a civil infraction (fine up to R$ 60M) regardless of
    competitive effects. Always run CADE threshold check at term sheet stage.

17. **Treating all FIP distributions as taxed identically.** FIP-IE individual investor
    distributions are entirely exempt from IRRF; standard FIP distributions at 15%.
    Incorrect tax characterization creates investor reporting errors and potential
    Receita Federal audit. Confirm FIP category before advising on distributions.

---

## Writing Standards

Before delivering any output:

- [ ] **Plain language:** Legal terms are explained in Portuguese with English gloss
      where helpful (e.g., "Teto de Avaliação (valuation cap)")
- [ ] **Active voice:** Use "O investidor recebe" not "Será recebido pelo investidor"
- [ ] **Specificity:** Every recommendation includes specific clause language, not
      general guidance
- [ ] **No silent assumptions:** Every assumption stated explicitly; jurisdiction-specific
      assumptions marked [JURISDICTION-SPECIFIC]
- [ ] **Pending law flagged:** Every reference to CICC or PLP 252/2023 marked [VERIFY
      — pending legislation]
- [ ] **Tax conclusions guarded:** Every tax conclusion marked [VERIFY with qualified
      Brazilian tax advisor (tributarista)]
- [ ] **No jurisdiction bleed:** No inadvertent application of US VC, UK, or EU legal
      concepts without explicit [JURISDIÇÃO-ESPECÍFICA ORIGINAL] flagging
- [ ] **Bilingual key terms:** Major legal terms provided in Portuguese (primary) with
      English translation parenthetical

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

Search the Legalcode law and case law database for:

```
Search 1: "CVM Resolução 175 FIP Fundo Investimento Participações Anexo Normativo IV"
Search 2: "Lei Complementar 182 2021 Marco Legal Startups CICC"
Search 3: "Código Civil mútuo conversível startups IOF"
Search 4: "Lei das SA Acordo Acionistas preferência liquidação anti-diluição"
Search 5: "LGPD ANPD startups compliance requisitos"
```

Save the top 10 most relevant results to `/tmp/legalcode-br-vc-authority.md` for
reference throughout the analysis. Mark as VERIFIED in Glass Box.

**Without legalcode-mcp:**

- Mark all statutory and regulatory citations with [VERIFY]
- Focus enhancement on structural quality, instrument mechanics, and market-standard
  terms rather than statutory depth
- Note: `legalcode_mcp: "Not connected — manual verification required"`
- Direct user to: CVM portal (cvm.gov.br), Planalto federal legislation (planalto.gov.br),
  ANPD portal (gov.br/anpd), ABVCAP guides (abvcap.com.br)

---

## Localization Notes

### Bilingual Legal Terminology Glossary

| Portuguese Term                                        | English Gloss                                                   | Context                                                  |
| ------------------------------------------------------ | --------------------------------------------------------------- | -------------------------------------------------------- |
| Mútuo Conversível                                      | Convertible loan                                                | Core pre-seed/seed instrument                            |
| Contrato de Investimento em Capital Conversível (CICC) | Convertible capital investment contract                         | Proposed new instrument (PLP 252/2023)                   |
| Teto de Avaliação                                      | Valuation cap                                                   | Conversion economics                                     |
| Desconto                                               | Discount                                                        | Conversion economics                                     |
| Evento de Qualificação                                 | Qualifying event / qualifying financing                         | Conversion trigger                                       |
| Sociedade Limitada (Ltda)                              | Limited liability company                                       | Startup corporate form (civil law)                       |
| Sociedade Anônima (S.A.)                               | Joint-stock company / corporation                               | Institutional-investor corporate form                    |
| Cota / Quota                                           | Quota / membership interest                                     | Ltda ownership unit                                      |
| Ação / Ações                                           | Share / shares                                                  | S.A. ownership unit                                      |
| Ações Preferenciais                                    | Preferred shares                                                | S.A. VC instrument                                       |
| Ações Ordinárias                                       | Ordinary / common shares                                        | S.A. founder shares                                      |
| Contrato Social                                        | Articles of organization                                        | Ltda governing document                                  |
| Estatuto Social                                        | Articles of association                                         | S.A. governing document                                  |
| Acordo de Quotistas                                    | Quotaholders' agreement                                         | Ltda investor protections                                |
| Acordo de Acionistas                                   | Shareholders' agreement                                         | S.A. investor protections (Lei das S.A. Art. 118)        |
| Transformação                                          | Conversion / transformation                                     | Ltda-to-S.A. change of form                              |
| Preferência de Liquidação                              | Liquidation preference                                          | Exit economics                                           |
| Direito de Preferência                                 | Preemptive right / right of first refusal                       | Transfer restrictions                                    |
| Tag-Along                                              | Tag-along right                                                 | Minority co-sale right                                   |
| Drag-Along (Direito de Arrasto)                        | Drag-along right                                                | Majority M&A forcing mechanism                           |
| Fundo de Investimento em Participações (FIP)           | Private equity / venture capital fund                           | Institutional investment vehicle                         |
| Administrador Fiduciário                               | Fund administrator                                              | CVM-registered fund administrator                        |
| Gestor                                                 | Fund manager / portfolio manager                                | CVM-registered investment manager                        |
| Investidor Qualificado                                 | Qualified investor                                              | CVM-defined eligible FIP investor                        |
| IOF                                                    | Tax on Financial Operations                                     | Tax on loans and financial transactions                  |
| IRPF                                                   | Individual income tax                                           | Personal capital gains tax                               |
| IRPJ                                                   | Corporate income tax                                            | Entity-level income tax                                  |
| CSLL                                                   | Social Contribution on Net Profit                               | Entity-level social contribution                         |
| FGTS                                                   | Severance Indemnity Fund                                        | Mandatory employer payroll contribution                  |
| INSS                                                   | National Social Security Institute                              | Social security contributions                            |
| LGPD                                                   | Brazilian General Data Protection Law                           | GDPR equivalent                                          |
| ANPD                                                   | National Data Protection Authority                              | LGPD regulator                                           |
| CVM                                                    | Securities and Exchange Commission of Brazil                    | Capital markets regulator                                |
| Banco Central (BCB)                                    | Central Bank of Brazil                                          | Monetary authority; RDE-IED registration                 |
| CADE                                                   | Administrative Council for Economic Defense                     | Brazilian antitrust authority                            |
| ABVCAP                                                 | Brazilian Association of PE and VC                              | Industry best-practice body                              |
| ANBIMA                                                 | Brazilian Financial and Capital Markets Association             | Self-regulatory organization                             |
| ABStartups                                             | Brazilian Startup Association                                   | Startup ecosystem association                            |
| Simples Nacional                                       | Simplified National Tax Regime                                  | SME tax regime (Ltda only; <R$4.8M revenue)              |
| Lucro Presumido                                        | Presumed Profit Regime                                          | Mid-tier tax regime                                      |
| Lucro Real                                             | Actual Profit Regime                                            | Full-accounting tax regime                               |
| Opção de Compra (SOP)                                  | Stock option plan                                               | Equity compensation structure                            |
| Phantom Equity / VSOP                                  | Phantom equity / virtual stock option plan                      | Cash-settled equity compensation                         |
| Flip Offshore                                          | Offshore flip / corporate restructuring                         | Redomiciliation to foreign holding company               |
| Marco Legal das Startups                               | Startup Legal Framework                                         | Lei Complementar 182/2021                                |
| Efetiva Influência                                     | Effective influence                                             | CVM 175 FIP governance requirement                       |
| Compartimento                                          | Compartment                                                     | FIP sub-fund structure (CVM 175)                         |
| Correção Monetária                                     | Monetary correction / inflation indexation                      | Loan interest indexation                                 |
| Registro Declaratório Eletrônico (RDE-IED)             | Electronic Declaratory Registration — Direct Foreign Investment | Banco Central registration for foreign equity investment |

### Brazil vs. US VC Comparison Notes

For practitioners familiar with US VC:

| Concept                   | US Standard                   | Brazilian Equivalent / Adaptation                             |
| ------------------------- | ----------------------------- | ------------------------------------------------------------- |
| SAFE                      | Y Combinator SAFE             | MISTO (Latitud) — adapted for Brazilian law                   |
| Convertible Note          | Custom convertible note       | Mútuo Conversível — CC Arts. 586–592 basis                    |
| Delaware C-Corp           | Delaware Corp.                | S.A. under Lei 6.404/1976                                     |
| LLC                       | N/A (not a direct equivalent) | Ltda (Sociedade Limitada) — closer analog                     |
| Series Preferred Share    | NVCA-standard preferred       | Ações Preferenciais under Lei das S.A.                        |
| Shareholder Agreement     | NVCA model                    | Acordo de Acionistas (Lei das S.A. Art. 118)                  |
| VC Fund (LP/GP structure) | Limited Partnership           | FIP (Fundo de Investimento em Participações)                  |
| Fund GP                   | General Partner               | Gestor (CVM-registered fund manager)                          |
| Fund LP                   | Limited Partner               | Cotista (FIP quota holder)                                    |
| Angel Tax Relief          | Section 1202 QSBS             | No direct equivalent; isenção FIP-IE for infrastructure       |
| IOF                       | N/A                           | Tax on financial operations — applies to PJ convertible loans |

---

## Output Format Template

Deliver all analysis in this format:

```markdown
# Brazilian Venture Financing Analysis

**Transaction:** [Deal name or description]
**Instrument:** [MISTO / Mútuo Conversível / CICC / Direct Equity / FIP]
**Corporate Structure:** [Ltda / S.A. / FIP]
**Date of Analysis:** [Date]
**Prepared by:** legalcode-venture-financing-br (AI-assisted — not legal advice)

---

## Sumário Executivo (Executive Summary)

**Overall assessment:** [CONFORME / ATENÇÃO / RISCO / CRÍTICO — overall rating]
**Top 3 issues:**

1. [Issue] — [Severity]
2. [Issue] — [Severity]
3. [Issue] — [Severity]

**Recommended immediate actions:**

- [Action 1]
- [Action 2]
- [Action 3]

---

## Análise do Instrumento (Instrument Analysis)

### [Instrument Type] — Clause-by-Clause Review

| Cláusula                   | Status        | Observação |
| -------------------------- | ------------- | ---------- |
| Valor do Investimento      | [🟢/🟡/🔴/⛔] | [Note]     |
| Teto de Avaliação          | [🟢/🟡/🔴/⛔] | [Note]     |
| Desconto                   | [🟢/🟡/🔴/⛔] | [Note]     |
| Evento de Qualificação     | [🟢/🟡/🔴/⛔] | [Note]     |
| Fórmula de Conversão       | [🟢/🟡/🔴/⛔] | [Note]     |
| Juros e Correção Monetária | [🟢/🟡/🔴/⛔] | [Note]     |
| Prazo de Vencimento        | [🟢/🟡/🔴/⛔] | [Note]     |
| Disposições IOF            | [🟢/🟡/🔴/⛔] | [Note]     |
| Tag-Along / Drag-Along     | [🟢/🟡/🔴/⛔] | [Note]     |
| Direito de Preferência     | [🟢/🟡/🔴/⛔] | [Note]     |
| MFN / Pro-Rata             | [🟢/🟡/🔴/⛔] | [Note]     |
| Conversão Offshore         | [🟢/🟡/🔴/⛔] | [Note]     |

---

## Análise Detalhada por Prioridade (Findings by Priority)

### ⛔ CRÍTICO — Ação Imediata Necessária

[For each CRÍTICO finding:]
**[Finding number]. [Short title]**

- **Descrição:** [What the issue is]
- **Base legal:** [Statute/regulation + [VERIFY] if unconfirmed]
- **Risco:** [What happens if not resolved]
- **Linguagem recomendada:** [Draft clause text in Portuguese]
- **Posição de recuo:** [Minimum acceptable alternative]

### 🔴 RISCO — Escalar para Assessoria Jurídica

[Same format]

### 🟡 ATENÇÃO — Recomendar Negociação

[Same format — abbreviated]

### 🟢 CONFORME — Para Conhecimento

[List only; no detailed analysis needed]

---

## Estrutura Societária (Corporate Structure Assessment)

**Current structure:** [Ltda / S.A.]
**Recommended structure:** [Same / Transformation to S.A. / FIP investment]
**Transformation required:** [Yes / No / Conditional]
**Simples Nacional impact:** [None / Loss on transformation — plan tax regime change]
**Estimated timeline:** [If transformation needed]

---

## Análise de IOF (IOF Tax Analysis)

**Investor type:** [PF / PJ / FIP]
**IOF applicable:** [Yes / No]
**Estimated IOF amount:** [R$ X or "0% — PF investor"]
**IOF responsibility:** [Borrower (startup) / Investor / Split — as per contract]
**Recommendation:** [[VERIFY with qualified Brazilian tax advisor (tributarista)]]

---

## Compliance Regulatório (Regulatory Compliance)

| Area                      | Status                                             | Notes   |
| ------------------------- | -------------------------------------------------- | ------- |
| CVM registration          | [Required / Exempt / Not applicable]               | [Basis] |
| Marco Legal das Startups  | [Applicable / Not applicable]                      |         |
| LGPD compliance           | [Adequate / Gaps identified / Not assessed]        |         |
| FGTS equity compensation  | [Compliant / Risk]                                 |         |
| CADE threshold (M&A exit) | [Below threshold / Above threshold / Not assessed] |         |

---

## Análise FIP (FIP Analysis — if applicable)

**FIP type:** [Capital Semente / Empresas Emergentes / IE / PD&I]
**CVM 175 Annex IV compliance:** [CONFORME / Issues identified]
**Effective influence:** [Satisfied / Gap]
**Investor qualification:** [Confirmed / Not confirmed]
**Tax treatment:** [15% IRRF / FIP-IE exempt]
**Portfolio company governance gaps:** [List]

---

## Estratégia de Saída (Exit Strategy)

**Exit scenarios analyzed:** [M&A / IPO / Secondary / Offshore flip]
**CADE threshold:** [Below / Check required / Above — notification needed]
**Offshore flip readiness:** [MISTO pre-approved / Manual restructuring / Not analyzed]
**Tax on exit (founder):** [[VERIFY with Brazilian tax advisor]]

---

## Estratégia de Negociação (Negotiation Recommendations)

**Priority negotiation points (P1):** [List]
**Should-negotiate points (P2):** [List]
**Nice-to-have (P3):** [List]

**Suggested negotiation sequence:**

1. [First: resolve CRÍTICO items as conditions to signing]
2. [Then: negotiate P2 economic terms]
3. [Concede: P3 or P4 items as goodwill gestures]

---

## Glass Box Audit Trail

[Paste completed YAML from Glass Box template above]

---

## Isenção de Responsabilidade (Disclaimer)

This analysis was produced by the legalcode-venture-financing-br AI skill and does not
constitute legal advice (parecer jurídico). It is not a substitute for a qualified
Brazilian lawyer (advogado inscrito na OAB) or a qualified Brazilian tax advisor
(tributarista). All conclusions marked [VERIFY] require confirmation with authoritative
Brazilian legal sources. Legislative references to PLP 252/2023 (CICC) reflect the
status as of the skill's knowledge cutoff and must be verified against the Diário Oficial
da União. Tax conclusions require engagement of a qualified tributarista.
```

---

## Provenance

**Created by:** Legalcode original (2026-03-21)

**Mode:** Mode A — Created from scratch

**Research methodology:** 2-agent parallel web research pipeline deployed prior to
skill drafting. Agent 1 covered MISTO, CICC, and Mútuo Conversível mechanics (Latitud
documentation, law firm alerts from Baptista Luz, FAS Advogados, Conjur, Baptista
Advogados, Carta.com, StarupHero). Agent 2 covered Ltda/S.A. structure, FIP regulation
(CVM 175/22), tax treatment (IOF, IRPF), and ABVCAP/ANBIMA market practice (Mattos
Filho VC Guide, Machado Meyer, ABVCAP, CVM portal, ANBIMA, government investor portal,
Jusbrasil).

**Key legal sources consulted:**

- Código Civil (Lei 10.406/2002) Arts. 586–592 (mútuo) and 1.052–1.087 (Ltda)
- Lei das S.A. (Lei 6.404/1976) Arts. 118, 171, 254-A
- Lei Complementar 182/2021 (Marco Legal das Startups)
- CVM Resolution 175/22 and Normative Annex IV (FIP)
- CVM Instruction 578/2016 (FIP prior framework)
- PLP 252/2023 (CICC — pending legislation, Senate-approved April 2024)
- Lei 14.754/2023 (FIP taxation)
- Lei 13.709/2018 (LGPD)
- Latitud MISTO documentation (latitud.com/misto)
- ABVCAP Governance and Best Practices Guides (abvcap.com.br)
- ANBIMA Fund Standards
- Conjur, Baptista Luz, FAS Advogados law firm analyses on CICC and Mútuo Conversível

**Attribution:** Legalcode original synthesis
