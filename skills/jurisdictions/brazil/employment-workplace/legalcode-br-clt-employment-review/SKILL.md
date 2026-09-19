---
name: legalcode-br-clt-employment-review
description: Reviews Brazilian employment contracts, HR policies, payroll calculations, and termination
  packages for CLT (Consolidação das Leis do Trabalho) compliance. Use when auditing Brazilian employment
  agreements, reviewing severance packages, validating payroll calculations, assessing vínculo empregatício
  (misclassification) exposure, or conducting HR compliance reviews for Brazilian operations.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Reviews Brazilian employment contracts, HR policies, payroll calculations, and termination packages for CLT (Consolidação das Leis do Trabalho) compliance. Covers all contract types (prazo indeterminado, experiência, intermitente, teletrabalho), 13th salary (décimo terceiro salário), férias and dobra de férias, FGTS deposits and multa rescisória, overtime (horas extras) and banco de horas, termination types and calculations (rescisão, aviso prévio proporcional, TRCT), union obligations, and eSocial event deadlines. Applies 2017 Reforma Trabalhista (Lei 13.467/2017) and Lei 14.442/2022 (teletrabalho update). Use when auditing Brazilian employment agreements, reviewing severance packages, validating payroll calculations, assessing vínculo empregatício (misclassification) exposure, or conducting HR compliance reviews for Brazilian operations. Triggers on: CLT review, Brazilian labor law, horas extras, FGTS, férias, 13th salary, rescisão, aviso prévio, banco de horas, eSocial, pejotização, reforma trabalhista, sindicato, CCT, contrato de trabalho Brasil.


# Legalcode BR: CLT Employment Compliance Review

> **Disclaimer**: This skill provides a framework for AI-assisted Brazilian labor law compliance
> review. It does not constitute legal advice (_assessoria jurídica_). All outputs must be
> reviewed by a qualified _advogado trabalhista_ (Brazilian labor attorney) licensed by the OAB
> before use. Brazilian labor law evolves continuously through TST (_Tribunal Superior do
> Trabalho_) and STF decisions; verify current applicability before relying on any provision.
> Statutory and case law references cited here carry hallucination risk — verify against
> authoritative sources (CLT text, TST Súmulas, Diário Oficial) before relying on them.

---

## Purpose and Scope

This skill reviews Brazilian employment contracts, HR documents, payroll practices, and
termination packages against the CLT (_Consolidação das Leis do Trabalho_, Decreto-Lei
5.452/1943) and its principal amendments, including the 2017 Reforma Trabalhista
(Lei 13.467/2017) and Lei 14.442/2022 (teletrabalho update).

**Covers:**

- Contract type classification and mandatory written clauses
- 13th salary (_décimo terceiro_) calculation and payment deadlines
- Férias (_annual leave_) entitlement, abono pecuniário, and dobra de férias penalty
- FGTS deposit obligations and multa rescisória calculation
- Overtime (_horas extras_) limits, premium rates, and banco de horas validity
- All termination types and their TRCT (_Termo de Rescisão_) calculation
- Aviso prévio proporcional (Lei 12.506/2011)
- Union obligations: CCT/ACT applicability, imposto sindical (now voluntary), contribuição assistencial
- eSocial mandatory events and deadlines
- Vínculo empregatício (misclassification) risk — pejotização and PJ fraud exposure
- 2017 Reforma Trabalhista changes: what CLT provisions now yield to collective bargaining

**Does not:**

- Cover public-sector employment (_Regime Jurídico Único_, Lei 8.112/1990)
- Cover domestic workers (_Lei Complementar 150/2015_) in full detail
- Provide legal advice or replace a qualified _advogado trabalhista_
- Analyze collective bargaining agreements (_CCTs/ACTs_) in full — but flags when they apply
- Apply to self-employed workers, MEI, or autonomous contractors who genuinely lack CLT elements

---

## Jurisdiction and Governing Law

**Jurisdiction:** Federal Republic of Brazil — applicable nationwide to all private-sector
employment relationships.

**Primary statutes:**

- CLT (Decreto-Lei 5.452/1943) — foundational labor code
- CF/88 (Constituição Federal 1988, Art. 7) — constitutional labor rights floor
- Lei 8.036/1990 — FGTS
- Lei 4.090/1962 + Lei 4.749/1965 — 13th salary
- Lei 12.506/2011 — proportional aviso prévio
- Lei 13.467/2017 — 2017 Reforma Trabalhista
- Lei 14.442/2022 — teletrabalho update
- LGPD (Lei 13.709/2018) — privacy law (for employee data handling)

**Judicial authority:** TST (_Tribunal Superior do Trabalho_) Súmulas and OJ
(Orientações Jurisprudenciais) are binding guidance on how labor courts interpret CLT.
STF has validated the 2017 reform's collective bargaining provisions (2022 ruling on
Art. 611-A).

**Localization note:** Some states and sectors have additional health/safety NR
(_Norma Regulamentadora_) obligations and sector-specific CCTs that may modify base CLT
entitlements within the limits of CLT Art. 611-A and 611-B.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses and asks when:

- The review focus would change the analysis (e.g., payroll audit vs. termination review)
- The contract type is ambiguous (e.g., PJ contractor who may have vínculo empregatício)
- Termination type is unclear (affects which verbas rescisórias are owed)
- A CCT/ACT may modify statutory entitlements

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

### Step 1: Accept the Document or Facts

Accept input in any of these formats:

- **Document**: Employment contract, termination letter, TRCT, payroll extract, HR policy
  document — PDF, DOCX, or pasted text
- **URL**: Link to a document in a cloud storage or HR system
- **Stated facts**: "Employee hired [date], dismissed without cause, salary R$X, [N] years
  of service" — sufficient for TRCT calculation and aviso prévio review
- **Payroll data**: Monthly payroll extract for FGTS and overtime compliance review

If no document or facts are provided, prompt the user to supply them.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask the user these questions:

1. **Review objective**: What is the primary goal?
   - Options: Full CLT compliance audit, Termination package review, Payroll/FGTS audit,
     Contract type validation, Vínculo empregatício risk assessment, Overtime/banco de horas
     review, eSocial compliance check
   - _Why this matters_: Determines which CLT modules to prioritize.

2. **Worker classification**: How is the worker currently classified?
   - Options: CLT employee (formal, CTPS registered), PJ contractor (Pessoa Jurídica),
     Intermittent worker (CLT Art. 452-A), Apprentice (Lei 10.097/2000), Intern (Lei 11.788/2008),
     Unclear — that's part of the review
   - _Why this matters_: If worker is PJ, the vínculo empregatício analysis is central.
     If CLT, the full entitlements audit applies.

3. **Sector-level collective agreement**: Is there a CCT (_Convenção Coletiva_) or ACT
   (_Acordo Coletivo de Trabalho_) in force for this worker's category?
   - Options: Yes (provide the CCT/ACT reference or key terms), No / Not known
   - _Why this matters_: Post-2017 reform, CCTs and ACTs can modify about 15 CLT provisions
     (Art. 611-A). Missing a CCT can invalidate a banco de horas or shift arrangement.

4. **Termination context** (if applicable): How was or will the contract be terminated?
   - Options: Sem justa causa (employer dismissal without cause), Por justa causa (employer
     dismissal with cause — specify ground), Pedido de demissão (voluntary resignation),
     Rescisão indireta (constructive dismissal), Distrato (mutual termination), Contract
     expiry (fixed-term), Not applicable
   - _Why this matters_: Determines which verbas rescisórias are owed and whether
     40%, 20%, or 0% FGTS multa applies.

5. **Key dates** (for calculations): Can you provide:
   - Hire date (_data de admissão_)
   - Termination date or review date
   - Monthly gross salary (_salário bruto mensal_)
   - Last férias grant date (if reviewing vacation compliance)
   - _Why this matters_: Required for accurate TRCT, aviso prévio, and férias calculations.

If the user provides partial context, proceed with what is available and **state assumptions
explicitly** (e.g., "Assuming unjust dismissal (_rescisão sem justa causa_) — confirm if
incorrect").

### Step 3: Gather Legal Authority

Use **legalcode-mcp** (if connected) to pull current CLT text and relevant TST Súmulas for:

- The specific termination type identified in Step 2
- The relevant overtime/banco de horas regime
- Any applicable NR (Norma Regulamentadora) for sector-specific hazard pay

Save results to `/tmp/legalcode-br-clt-research.md` structured as:

```markdown
# CLT Legal Authority — [Review Subject]

## Date: [date]

### Primary Statutes

- [CLT article, current text or summary]

### TST Súmulas and OJs

- [Súmula number, content, relevance]

### Recent STF/TST Decisions

- [Case, holding, impact]
```

**Without legalcode-mcp:** Proceed with research from memory. Mark all statutory citations
[VERIFY] and note in the audit trail: `legalcode_mcp: "Not connected"`.

### Step 4: Run the CLT Compliance Matrix

Analyze the document or stated facts against each module in the CLT Compliance Matrix
(Section below). For each module:

1. Classify status as **VERDE** (compliant), **AMARELO** (attention/partial), or
   **VERMELHO** (violation/non-compliant)
2. Identify the specific CLT article or TST Súmula triggered
3. Quantify the liability exposure where calculable
4. State the remediation action

**⟁ CLARIFY** — If the contract references a CCT/ACT that modifies any CLT entitlement
(e.g., banco de horas, shift schedule, interval reduction), pause and confirm:

- "The contract references [CCT X]. Do you have the CCT text? If so, I will check whether
  the modification falls within CLT Art. 611-A (permissible) or Art. 611-B (non-waivable)."

### Step 5: Vínculo Empregatício Assessment (if PJ or ambiguous)

If the worker is classified as a PJ contractor or the classification is ambiguous, apply
the 4-element test from CLT Arts. 2–3. See the Vínculo Empregatício module in the
Compliance Matrix.

**⟁ CLARIFY** — If 3 or more of the 4 elements are present, pause before completing the
analysis and ask:

- "The facts suggest the existence of a CLT employment relationship (_vínculo empregatício_).
  Should I calculate the estimated retroactive CLT liabilities (FGTS, INSS, overtime,
  férias, 13th salary) for the period in question?"

### Step 6: TRCT Calculation (if termination review)

If the objective is a termination review, calculate all verbas rescisórias using the
TRCT Calculator in the Compliance Matrix. Present the calculation in itemized format
with gross and net amounts.

Apply the applicable FGTS multa rate:

- Sem justa causa → 40% of total FGTS balance
- Distrato → 20%
- Justa causa / pedido de demissão → 0%

Flag any items paid late or omitted as **VERMELHO** with the CLT Art. 477 penalty note.

### Step 7: Quality Verification

Before delivering output, run the Citation Quality Gates (see Quality Assurance section).
Apply Self-Interrogation for all VERMELHO findings. Score confidence for each finding.

### Step 8: Deliver Output

Structure the output using the Output Format Template at the end of this skill. Append
the Glass Box Audit Trail YAML.

---

## CLT Compliance Matrix

### Module 1: Contract Type and Written Form

**Applicable law:** CLT Arts. 443–445, 452-A, 75-B–75-E; Lei 14.442/2022

#### 1.1 Employment Relationship Elements (Vínculo Empregatício)

All four elements must be present for CLT to apply (CLT Arts. 2–3):

| Element              | Portuguese                          | What to Look For                                                          |
| -------------------- | ----------------------------------- | ------------------------------------------------------------------------- |
| **Personal service** | _Pessoalidade_                      | Services rendered by the individual personally; cannot substitute another |
| **Non-occasional**   | _Não-eventualidade / habitualidade_ | Regular, recurring work — not sporadic or project-based                   |
| **Subordination**    | _Subordinação jurídica_             | Employer controls how, when, and where work is done                       |
| **Remuneration**     | _Onerosidade_                       | Compensation (monetary or in-kind) paid for services                      |

**Pejotização risk:** If all 4 elements exist but the worker is engaged via a Pessoa Jurídica
company, courts will recognize the CLT bond regardless of contractual labeling. Employer
owes all retroactive CLT entitlements from inception of the relationship.

**Classification:** VERMELHO if 4/4 elements present on a PJ contract. AMARELO if 3/4
elements present (investigate further). VERDE if genuinely independent relationship.

#### 1.2 Contract Type Requirements

| Contract Type           | CLT Basis                                 | Maximum Duration             | Written Form Required                                  | Key Restrictions                                  |
| ----------------------- | ----------------------------------------- | ---------------------------- | ------------------------------------------------------ | ------------------------------------------------- |
| Prazo indeterminado     | Art. 443                                  | None                         | Recommended; CTPS mandatory                            | Default type; all CLT rights                      |
| Prazo determinado       | Art. 443–445                              | 2 years; 1 renewal           | **Yes**                                                | Justification required; no aviso prévio on expiry |
| Contrato de experiência | Art. 443, §2c + Art. 445, parágrafo único | **90 days total**; 1 renewal | **Yes**                                                | Auto-converts if exceeded                         |
| Contrato intermitente   | Art. 452-A                                | None                         | **Yes**                                                | Hourly rate ≥ minimum wage; 3-day call-out notice |
| Teletrabalho            | Arts. 75-A–75-E                           | None                         | **Yes** — must specify activities, equipment, expenses | 15-day notice to reverse                          |

**VERMELHO triggers:**

- Fixed-term contract exceeding 2 years or renewed more than once → automatic conversion to indefinite
- Experiência contract exceeding 90 days total → automatic conversion to indefinite
- Intermittent contract lacking written form or hourly rate below minimum wage
- Teletrabalho without written specification of equipment and expense allocation (Art. 75-D)
- CTPS (_Carteira de Trabalho e Previdência Social_) not annotated within 5 business days of hiring

#### 1.3 Mandatory Written Clauses (All Contract Types)

Flag as VERMELHO if absent:

- Parties' full identification (CNPJ, CPF, addresses)
- Job function (_cargo/função_) and salary
- Work location (or teletrabalho designation)
- Start date (_data de admissão_)
- Work schedule (_jornada de trabalho_)
- For fixed-term: end date and legal justification
- For intermittent: hourly wage and call-out procedure
- For teletrabalho: activity description, equipment responsibility, expense reimbursement

---

### Module 2: 13th Salary (Décimo Terceiro Salário)

**Applicable law:** Lei 4.090/1962; Lei 4.749/1965; CF/88 Art. 7, VIII

#### 2.1 Entitlement and Calculation

- **Entitled:** All CLT employees, rural workers, domestic workers, INSS retirees
- **Not entitled:** Self-employed (autônomos), MEI, interns, workers with valid PJ classification

**Calculation formula:**

```
Décimo terceiro bruto = (Salário bruto mensal ÷ 12) × meses trabalhados
```

Each month in which the employee worked **15 or more days** counts as a full month.
Variable salary workers use the average salary of the period.

#### 2.2 Payment Deadlines

| Installment                | Amount       | Deadline                        | INSS/IR Deducted? |
| -------------------------- | ------------ | ------------------------------- | ----------------- |
| 1ª parcela                 | 50% of gross | **30 November**                 | No                |
| 2ª parcela                 | Remainder    | **20 December**                 | Yes (INSS + IRRF) |
| Variable salary adjustment | Difference   | **10 January** (following year) | Yes               |

**Exception:** First installment may be paid with the June–November vacation advance if
the employee requests in writing during January–November.

**VERMELHO triggers:**

- First installment not paid by November 30 (or by vacation advance if requested)
- Second installment not paid by December 20
- Proportional 13th omitted from TRCT on termination (except justa causa dismissal)
- Calculation excludes habitual overtime, commissions, or other remuneration components
  that integrate into salary (TST Súmula 60, 132)

**AMARELO triggers:**

- Variable salary components not averaged correctly
- Partial months calculated without the 15-day rule

---

### Module 3: Férias (Annual Leave)

**Applicable law:** CLT Arts. 129–153; CF/88 Art. 7, XVII

#### 3.1 Entitlement by Absence Rate

After each 12-month _período aquisitivo_ (acquisition period):

| Unjustified absences | Vacation days           |
| -------------------- | ----------------------- |
| 0–5                  | **30 days**             |
| 6–14                 | 24 days                 |
| 15–23                | 18 days                 |
| 24–32                | 12 days                 |
| 33 or more           | None — period forfeited |

Absences that do NOT reduce vacation: maternity/paternity leave, INSS-certified illness,
work-related injury, authorized employer absences.

#### 3.2 Terço Constitucional (Mandatory 1/3 Bonus)

Every vacation payment must include an additional **1/3 of the vacation salary**
(CF/88 Art. 7, XVII). This applies to:

- Standard vacation salary
- Abono pecuniário (cash conversion)
- Dobra de férias (penalty for late grant)
- Férias payment in TRCT

#### 3.3 Period Rules

| Rule                      | Requirement                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------- |
| _Período concessivo_      | Employer must grant vacation within **12 months** after the acquisition period ends               |
| Advance notice            | Employer must notify employee in writing **at least 30 days** before vacation start               |
| Payment timing            | Vacation salary paid **at least 2 days** before vacation begins (CLT Art. 145)                    |
| Fractionation (post-2017) | Up to **3 periods** with employee consent — minimum **14 days** + two minimums of **5 days** each |

#### 3.4 Abono Pecuniário (Cash Conversion, CLT Art. 143)

- Employee may convert **1/3 of vacation entitlement** to cash at the vacation rate + 1/3 bonus
- Request must be made **at least 15 days before** the end of the acquisition period
- Not available: part-time workers, teachers under special regime

#### 3.5 Dobra de Férias (Double-Pay Penalty, CLT Art. 137)

Triggers automatically when vacation is **not granted within the concessional period**.

```
Dobra = Salary × 2 + 1/3 = Salary × 2.6667
```

- Has salary nature → FGTS, 13th, and INSS reflexes apply
- Each ungranted period generates an independent dobra
- **At termination:** Férias vencidas (accrued but not taken) paid in dobro; férias
  proporcionais paid at single rate + 1/3

**VERMELHO triggers:**

- Vacation not granted within 12-month concessional period → dobra liability
- Vacation salary not paid at least 2 days before start → risk of court-ordered dobra
- 1/3 constitutional bonus absent from any vacation payment
- Fractionation without employee consent or below minimum periods
- Abono pecuniário requested less than 15 days before acquisition period end (invalid)

---

### Module 4: FGTS (Fundo de Garantia do Tempo de Serviço)

**Applicable law:** Lei 8.036/1990; CF/88 Art. 7, III

#### 4.1 Monthly Deposit Obligations

| Worker type                   | Rate                   | Deposit deadline                    |
| ----------------------------- | ---------------------- | ----------------------------------- |
| Standard CLT workers          | **8% of gross salary** | 7th business day of following month |
| Apprentices (Lei 10.097/2000) | **2% of salary**       | 7th business day                    |

_Gross salary_ includes all remuneration: base salary, overtime pay (if habitual), commissions,
hazard pay (_adicional de insalubridade/periculosidade_), night premium, and other regular
salary components.

**Via eSocial/GFIP** to Caixa Econômica Federal.

#### 4.2 Multa Rescisória (Termination Penalty on FGTS Balance)

| Termination type                 | FGTS penalty                  | Legal basis                              |
| -------------------------------- | ----------------------------- | ---------------------------------------- |
| Rescisão sem justa causa         | **40%** of total FGTS balance | Lei 8.036/90, Art. 18, §1                |
| Rescisão indireta (CLT Art. 483) | **40%**                       | Lei 8.036/90, Art. 18, §1                |
| Distrato (CLT Art. 484-A)        | **20%**                       | CLT Art. 484-A                           |
| Culpa recíproca                  | **20%**                       | CLT Art. 484-A (by analogy)              |
| Rescisão por justa causa         | **0%**                        | None — employee loses FGTS right         |
| Pedido de demissão               | **0%**                        | None — no multa on voluntary resignation |

**VERMELHO triggers:**

- FGTS deposits missing or inconsistent for any month of the employment
- 40% multa not paid within 10 days of termination on unjust dismissal
- Gross salary base for FGTS calculation excludes habitual overtime or regular benefits
- Apprentice rate (2%) used for workers who are not legally registered apprentices

**AMARELO triggers:**

- FGTS deposit amount inconsistently calculated across months
- Late deposits (past 7th business day) without correction + interest
- Worker has elected _saque-aniversário_ (FGTS anniversary withdrawal scheme) — confirm
  this affects the worker's right to access balance on dismissal

---

### Module 5: Overtime and Banco de Horas

**Applicable law:** CLT Arts. 58–65; CF/88 Art. 7, XVI; TST Súmulas 85, 291, 437

#### 5.1 Standard Work Hours

| Standard         | Limit                      |
| ---------------- | -------------------------- |
| Daily            | **8 hours**                |
| Weekly           | **44 hours**               |
| Maximum overtime | **2 additional hours/day** |

#### 5.2 Overtime Premiums

| Day                  | Minimum premium            | Note                                    |
| -------------------- | -------------------------- | --------------------------------------- |
| Normal weekday       | **50%** above hourly rate  | CLT Art. 59, §1                         |
| Sundays and holidays | **100%** above hourly rate | CF/88 Art. 7, XVI; common CCT provision |

Higher rates may be established by CCT/ACT.

#### 5.3 Banco de Horas (Hour Bank)

| Agreement type                 | Maximum compensation window | Requirement                           |
| ------------------------------ | --------------------------- | ------------------------------------- |
| Individual written agreement   | **6 months**                | Post-2017 reform (CLT Art. 59, §5)    |
| Collective agreement (CCT/ACT) | **12 months**               | CCT or ACT required                   |
| Tacit/unwritten                | **Same month**              | Very limited; effectively impractical |

**Validity conditions (TST Súmula 85):**

- Must be formalized in writing (individual or collective)
- Cannot habitually exceed **10 hours/day** (TST OJ 394)
- Must record hours accurately
- Uncompensated excess hours must be paid as overtime at 50%+ premium

#### 5.4 12×36 Shift

Established by **individual written agreement** (post-2017 reform, CLT Art. 59-A) — no
longer requires collective bargaining. Monthly wage includes DSR (_descanso semanal
remunerado_) and holiday compensation.

#### 5.5 Overtime-Exempt Workers (CLT Art. 62)

| Category                                     | Condition                                                                                                |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| External workers with variable schedule      | CLT Art. 62, I — activities incompatible with fixed-hour control                                         |
| _Cargo de confiança_ (trust/management role) | CLT Art. 62, II — **salary must be at least 40% above base**; real management powers; registered in CTPS |
| Teletrabalho workers                         | CLT Art. 62, III (added 2017) — unless individual agreement stipulates otherwise                         |

**VERMELHO triggers:**

- Overtime worked but not paid and no valid banco de horas agreement in place
- Banco de horas established without written agreement or exceeding 6/12-month windows
- _Cargo de confiança_ exemption claimed but salary does not include the 40% function bonus
- _Cargo de confiança_ exemption claimed but worker has no real managerial powers
- Daily hours habitually exceeding 10 hours under purported banco de horas arrangement
- Habitual overtime not reflected in FGTS base salary (TST Súmula 63, 132)

**AMARELO triggers:**

- Banco de horas agreement exists but hours records are incomplete or absent
- Overtime premiums paid at 50% when CCT may require higher rate (verify CCT)
- 12×36 shift established by individual agreement — confirm no sector CCT requires collective bargaining for this modality

---

### Module 6: Termination and Rescisão

**Applicable law:** CLT Arts. 477, 482, 483, 484-A, 487; Lei 8.036/90; Lei 12.506/2011

#### 6.1 Just Cause Grounds (Taxative List — CLT Art. 482)

Just cause must fall within one of these 14 grounds (no others valid):

| Code  | Ground                                        | Note                                                                 |
| ----- | --------------------------------------------- | -------------------------------------------------------------------- |
| a     | _Ato de improbidade_                          | Dishonesty, theft, fraud                                             |
| b     | _Incontinência de conduta / mau procedimento_ | Moral misconduct, harassment                                         |
| c     | Unauthorized competition                      | Habitually negotiating for own account without permission            |
| d     | Criminal conviction                           | Final, unappealable sentence not suspended                           |
| e     | _Desídia_                                     | Habitual negligence, repeated low performance                        |
| f     | Habitual intoxication                         | At the workplace — true addiction may trigger rehabilitation instead |
| g     | Breach of confidentiality                     | Causing damage to the employer                                       |
| h     | _Indisciplina / insubordinação_               | Disobedience of lawful, proportionate orders                         |
| i     | _Abandono de emprego_                         | 30+ consecutive unjustified absences (intent to abandon presumed)    |
| j     | Assault / offense at workplace                | Against any person; self-defense excluded                            |
| k     | Assault / offense against superiors           | Specifically against the employer or hierarchical supervisors        |
| l     | Habitual gambling at work                     | Interfering with duties                                              |
| m     | _Perda de habilitação_                        | Loss of required professional license (e.g., driver's license)       |
| único | Acts against national security                | —                                                                    |

**VERMELHO triggers:**

- Just cause invoked on a ground not listed in CLT Art. 482
- Just cause applied without prior evidence documentation (courts require proportionality and
  contemporaneous evidence; long-delayed application may be void — _perdão tácito_)
- Just cause applied for abandonment without the employer first sending a registered notice
  (_carta registrada_) demanding return
- Worker dismissed for just cause but paid only saldo de salário + férias vencidas + 1/3
  when no valid just cause ground exists → reclassified as unjust dismissal

#### 6.2 Aviso Prévio Proporcional

**Base (Lei 12.506/2011):**

```
Aviso prévio = 30 days + (3 days × complete years of service)
Maximum: 90 days total
```

| Years of service | Aviso prévio      |
| ---------------- | ----------------- |
| Less than 1 year | 30 days           |
| 1 year           | 33 days           |
| 5 years          | 45 days           |
| 10 years         | 60 days           |
| 20 years         | 90 days (maximum) |

**Important nuances:**

- Proportional increase **benefits only the employee** — employer giving notice is entitled
  to only 30 days from the employee
- Employee subject to aviso prévio may work the notice period or accept _aviso indenizado_
  (payment in lieu)
- Even if worked, aviso prévio value integrates into FGTS base for the notice period
- Habitual overtime integrates into aviso prévio indenizado value (TST Súmula 291)

**VERMELHO triggers:**

- Aviso prévio calculated at flat 30 days for a worker with more than 1 year of service
- Aviso prévio indenizado calculated without habitual overtime reflexes
- Employee given aviso prévio but then prevented from working the notice period without
  receiving aviso indenizado

#### 6.3 TRCT Calculation Matrix

Use this matrix to verify the termination package. All values due within **10 calendar
days** of termination (CLT Art. 477, §6). Failure triggers a 1-month salary penalty.

| Verba                               | Sem justa causa | Justa causa | Pedido demissão |     Distrato     | Fixed-term expiry |
| ----------------------------------- | :-------------: | :---------: | :-------------: | :--------------: | :---------------: |
| Saldo de salário                    |        ✓        |      ✓      |        ✓        |        ✓         |         ✓         |
| Férias vencidas + 1/3               |        ✓        |      ✓      |        ✓        |        ✓         |         ✓         |
| Férias proporcionais + 1/3          |        ✓        |      ✗      |        ✓        |        ✓         |         ✓         |
| 13º proporcional                    |        ✓        |      ✗      |        ✓        |        ✓         |         ✓         |
| Aviso prévio (indenizado or worked) |     ✓ full      |      ✗      |   ✗ (owes AP)   |      ✓ 50%       |         ✗         |
| FGTS all deposits                   |        ✓        |  ✓ collect  |    ✓ collect    |    ✓ collect     |     ✓ collect     |
| Multa FGTS                          |      ✓ 40%      |      ✗      |        ✗        |      ✓ 20%       |         ✗         |
| FGTS withdrawal by worker           | ✓ full balance  |      ✗      |        ✗        | ✓ 80% of balance |  ✓ full balance   |
| Seguro-desemprego eligibility       |        ✓        |      ✗      |        ✗        |        ✗         |         ✓         |

**Saldo de salário calculation:**

```
Saldo de salário = (Salário bruto ÷ dias úteis no mês) × dias trabalhados no mês parcial
```

**Férias proporcionais:**

```
Férias proporcionais = (Dias de férias entitlement ÷ 12) × meses no período aquisitivo atual
(months with 15+ days worked count as full months)
```

**VERMELHO triggers:**

- Any verba marked ✓ above omitted from the TRCT
- Payment made after the 10-day deadline → CLT Art. 477, §8 one-month salary penalty
- FGTS multa rate wrong (40% vs. 20% vs. 0%) for the termination type
- Férias vencidas (accrued but not taken) not paid in dobro if applicable
- TRCT not formally registered via eSocial S-2299

---

### Module 7: Union Obligations

**Applicable law:** CLT Arts. 511–625, 578–582, 611-A, 611-B; CF/88 Art. 8

#### 7.1 Imposto Sindical (Now Voluntary)

**Pre-2017:** Mandatory annual deduction of 1 day's salary from all workers.
**Post-2017 reform (CLT Art. 579):** Entirely voluntary. Employer may only deduct with
**individual, express, written authorization** from the employee.

**VERMELHO triggers:**

- Union tax (_imposto sindical_) deducted without individual written employee authorization
- Employer failing to forward authorized deductions to the union within the required period

#### 7.2 Contribuição Assistencial / Confederativa

These CCT/ACT-negotiated contributions remain legally contested.
Workers who are **not** union members may formally oppose (_oposição_) the deduction.

**VERMELHO triggers:**

- Contribuição assistencial deducted from non-union members without providing an opt-out
  mechanism (_oposição_) — per TST precedents and STF rulings, this right must be respected

#### 7.3 Collective Bargaining — What Can and Cannot Be Modified

**CLT Art. 611-A (post-2017): CCT/ACT may modify (not exhaustive):**

- Banco de horas (annual window via CCT)
- Interval reduction (_intervalo intrajornada_ — minimum 30 minutes)
- 12×36 shift formalization
- Teletrabalho and hybrid work arrangements
- Cargo de confiança criteria
- Insalubrity classification levels
- Overtime premiums (subject to CF/88 Art. 7, XVI minimum)
- Work hour recording methods
- Productivity-based pay structures

**CLT Art. 611-B: CCT/ACT CANNOT reduce (absolute floor):**

- Minimum wage
- Prohibition of discrimination
- Freedom of association and union rights
- Prohibition on child labor
- Access to unemployment insurance (_seguro-desemprego_)
- FGTS right itself
- 30-day annual vacation minimum
- Maternity leave (120 days) and paternity leave
- NR health and safety standards
- 1-hour minimum meal break for shifts over 6 hours (though 30-minute minimum can be negotiated)

**VERMELHO triggers:**

- CCT/ACT clause attempting to reduce entitlements listed in CLT Art. 611-B
- Employer treating an expired CCT/ACT as still in force after its 2-year validity period
  (ultraativity abolished by 2017 reform — expired CCTs cease to apply)
- Applying a CCT for the wrong professional category (_categoria profissional_)

---

### Module 8: eSocial Compliance

**Applicable law:** Decreto 8.373/2014; eSocial Resolução 2/2016 and subsequent updates

#### 8.1 Key Events and Deadlines

| eSocial Event | Description                           | Deadline                                   | CLT Risk if Late                           |
| ------------- | ------------------------------------- | ------------------------------------------ | ------------------------------------------ |
| **S-2200**    | New hire registration (_admissão_)    | **Before the first day of work**           | Administrative fine; labor inspection risk |
| **S-2190**    | Simplified preliminary registration   | Before first day                           | Alternative to S-2200 for urgent hires     |
| **S-2299**    | Employee termination (_desligamento_) | Within **10 days** of last working day     | Fine; blocks issuance of CND               |
| **S-1200**    | Monthly payroll (_remuneração_)       | By **7th business day** of following month | INSS/FGTS fine                             |
| **S-1210**    | Payment of wages and withholdings     | By date of payment                         | Fine                                       |
| **S-1299**    | Payroll closing                       | By **15th of following month**             | Fine                                       |
| **S-2230**    | Leave of absence (_afastamento_)      | Within 10 days of event                    | Fine                                       |
| **S-2240**    | Environmental health risk records     | Ongoing                                    | NR violations                              |

**Current version:** eSocial layout S-1.3 (in force since December 2024).

**VERMELHO triggers:**

- S-2200 sent on or after the employee's first day of work
- S-2299 not sent within 10 days of termination
- S-1200 filed without including all salary components (overtime, commissions, hazard pay)
- Payroll closed (S-1299) without matching S-1200 data

**AMARELO triggers:**

- eSocial records not reconciled with physical employment records (CTPS annotations)
- S-2240 environmental risk records not updated following a change in work conditions

---

## Severity Classification

Every finding is classified using the following three-tier system:

### 🟢 VERDE — Compliant

The practice is fully in compliance with the CLT and applicable CCT/ACT. No action required.
Confirm in the audit trail with the specific CLT article satisfied.

### 🟡 AMARELO — Attention Required

The practice has a gap or ambiguity that **creates litigation risk** if not remediated, but
does not yet constitute a clear violation. Common causes:

- Records incomplete but the underlying obligation was likely met
- CCT/ACT modifies the statutory rule — need to verify the CCT
- Practice is lawful but could be strengthened to reduce judicial uncertainty
- Calculation methodology unclear

**Action:** Identify what documentation or process change would resolve the finding.
Estimate the litigation risk probability if left unremediated.

### 🔴 VERMELHO — Violation

The practice **violates a specific CLT provision**, TST Súmula, or constitutional labor
right. Creates near-certain liability exposure in a _Reclamação Trabalhista_ if challenged.

**Action required:** Quantify the financial exposure where possible. State the corrective
action and its urgency. Apply Self-Interrogation (3-pass review) before finalizing the
VERMELHO classification.

---

## Severity-to-Action Mapping

| Severity                                      | Action                                                 | Timeline                                      |
| --------------------------------------------- | ------------------------------------------------------ | --------------------------------------------- |
| VERMELHO — active violation, ongoing exposure | Immediate remediation + legal counsel                  | Urgent                                        |
| VERMELHO — past violation, terminated worker  | Assess litigation risk; consider pro-active settlement | Within 2 years of termination (prescricional) |
| AMARELO — recordkeeping gap                   | Obtain missing documentation; update HR practice       | 30–60 days                                    |
| AMARELO — CCT verification needed             | Obtain and review applicable CCT text                  | 15–30 days                                    |
| VERDE                                         | No action required                                     | —                                             |

---

## Prioritization Framework

Findings are prioritized in three tiers based on financial exposure and litigation
probability:

**Tier 1 — Critical (Address immediately)**

- Active FGTS non-deposit (unlimited retroactive recovery; 30-year prescricional)
- Vínculo empregatício (misclassification) exposure with large workforce → mass liability
- Unpaid overtime that is habitual and undocumented
- Termination payment not made within 10-day deadline (CLT Art. 477 penalty)
- TRCT verbas missing for a terminated employee still within the 2-year prescricional window

**Tier 2 — High (Address within 30 days)**

- Banco de horas without valid written agreement
- Dobra de férias exposure for accrued vacation beyond concessional period
- eSocial S-2200 filed late — administrative fine exposure
- _Cargo de confiança_ overtime exemption without 40% salary supplement
- Just cause dismissal on grounds not listed in CLT Art. 482

**Tier 3 — Moderate (Address within 60–90 days)**

- Union contribution deductions without opt-out mechanism
- Férias fractionation without employee consent documentation
- Variable salary components missing from FGTS base
- Teletrabalho contract lacking expense reimbursement provision
- eSocial S-2240 environmental risk records not current

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates before delivering any finding. If any gate fails, revise before delivery.

| Gate           | Rule                                                                                                                | Fail Action                                                                 |
| -------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Source**     | Every CLT violation cites a specific article, TST Súmula, or OJ                                                     | Add citation or mark "[UNVERIFIED — OAB counsel to confirm]"                |
| **Format**     | Citations follow Brazilian legal citation format: "CLT Art. X", "TST Súmula XXX", "Lei XXXXX/XXXX, Art. Y"          | Fix format                                                                  |
| **Currency**   | Each cited provision checked for 2017 reform amendments or subsequent repeal                                        | Flag "[CHECK CURRENCY — may have been amended by Lei 13.467/2017 or later]" |
| **Domain**     | Analysis stays within Brazilian federal labor law. No conflation with foreign employment law or public-sector rules | Remove or flag cross-domain bleed                                           |
| **Confidence** | Uncertainty explicitly stated. If TST jurisprudence is divided on a point, say so                                   | Add confidence qualifier; cite the divergent positions                      |

### Self-Interrogation for VERMELHO Findings

For any finding classified VERMELHO, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the violation finding follow logically from the specific CLT article or TST Súmula cited?
- Would a _Juiz do Trabalho_ (labor judge) actually rule against the employer on these facts?
- Is there a defense the employer's labor attorney would raise (e.g., CCT modifying the statutory rule)?

**Pass 2 — Completeness**:

- Have all relevant CLT provisions, TST Súmulas, and CF/88 rights been considered?
- Is there a 2017 reform change that modified this obligation (e.g., banco de horas by
  individual agreement, distrato, teletrabalho)?
- Are there INSS, FGTS, and 13th salary _reflexos_ (knock-on effects) that must also
  be flagged?

**Pass 3 — Challenge**:

- What is the strongest argument that this practice is actually compliant?
- Could a CCT/ACT validly modify this obligation under CLT Art. 611-A?
- Is the VERMELHO classification proportionate, or should this be AMARELO with remediation guidance?

If any pass reveals a weakness, revise before delivery. Mark the audit trail with
`self_interrogation: "PASS"` or `self_interrogation: "REVISED — [reason]"`.

### Confidence Scoring

Assign a confidence level to each finding:

| Level        | Range     | Meaning                                          | Action                                                                 |
| ------------ | --------- | ------------------------------------------------ | ---------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear CLT/CF/88 violation; settled TST Súmula    | State with confidence; cite article and Súmula                         |
| **High**     | 0.80–0.94 | Strong basis; minor interpretation questions     | State with brief caveat; cite TST OJ if available                      |
| **Probable** | 0.60–0.79 | Good arguments but TST jurisprudence not uniform | State with reasoning and contra-indicators; note split                 |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing TST precedents    | Flag for OAB counsel review with both sides                            |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                          | Do not assert as violation; flag "[UNCERTAIN — OAB counsel to advise]" |

---

## Anti-Patterns

Explicit catalogue of what NOT to do in Brazilian CLT compliance review:

1. **Treating the 2017 reform as uniformly worker-unfriendly** — The Reforma Trabalhista
   created new protections too (written teletrabalho rules, explicit intermittent contract
   rights, distrato). Analyze each reform change on its own terms; do not assume it removed
   protections wholesale.

2. **Ignoring CCT/ACT applicability** — The single most common analytical error. Many CLT
   defaults are modified by sector CCTs (work hours, overtime premiums, profit sharing,
   meal allowances). Never classify a practice as a violation without checking whether a
   valid CCT/ACT applies.

3. **Applying the just cause list loosely** — CLT Art. 482 is a **taxative** (closed) list.
   There is no "catch-all" just cause. Inventing grounds or stretching listed grounds beyond
   their scope turns a justa causa dismissal into a sem justa causa with full FGTS 40% multa
   exposure.

4. **Treating pejotização as automatically fraudulent** — Genuine PJ engagements exist. The
   analysis must apply the 4-element test (Arts. 2–3). If any element is missing (e.g., no
   _pessoalidade_ because the contractor routinely substitutes others), the CLT bond may not
   be recognized. Avoid predetermined conclusions.

5. **Calculating aviso prévio without the Lei 12.506/2011 proportionality rule** — The flat
   30-day notice rule is wrong for any worker with more than 1 year of service. Miscalculating
   aviso prévio indenizado undermines the entire TRCT.

6. **Forgetting habitual overtime reflexes** — Habitual overtime, commissions, and bonuses
   integrate into the salary basis for FGTS, 13th salary, aviso prévio indenizado, férias,
   and DSR calculations. Missing reflexos is the most financially significant systematic error
   in TRCT calculations.

7. **Assuming the FGTS balance is only what the employer deposited** — The 40% multa is
   calculated on the **total FGTS balance**, which includes all prior employers' deposits
   and investment returns credited by Caixa Econômica Federal. Never calculate just on current
   employer's deposits.

8. **Treating the imposto sindical as still mandatory** — Since Lei 13.467/2017, it is
   entirely voluntary. Deducting it without individual written authorization is a violation
   with potential labor court and union liability.

9. **Confusing _férias vencidas_ and _férias proporcionais_** — Vencidas are accrued periods
   not yet granted (subject to dobra if beyond concessional period); proporcionais are the
   fraction accruing in the current acquisition period. They have different rates and
   different consequences at termination.

10. **Ignoring eSocial S-2200 timing** — Sending the admission event on or after the first
    day of work (rather than before) is a violation regardless of how minor it seems. Labor
    inspectors use eSocial logs to identify unregistered workers. The timing creates
    administrative fine exposure and weakens the employer's position in any subsequent dispute.

11. **Overlooking the prazo prescricional trap** — The 2-year window after termination and
    5-year retroactive reach means a worker terminated today can sue for violations going back
    5 years. A TRCT that looks complete today may still expose the employer to retroactive
    payroll underpayment claims from prior years.

12. **Accepting banco de horas without records** — A banco de horas agreement is legally
    worthless without accurate time records showing the hours deposited and compensated. Without
    records, courts treat all excess hours as unpaid overtime.

13. **Applying cargo de confiança exemption without the 40% salary supplement** — The
    exemption from overtime rules (CLT Art. 62, II) requires a salary at least 40% above the
    base rate. If the employer has not formally paid this supplement, the exemption is invalid
    and all overtime claims are reopened.

14. **Overlooking moral damages (_dano extrapatrimonial_) as a standalone risk** — Since the
    2017 reform codified moral damages in CLT Arts. 223-A–223-G, workers routinely include
    _pedidos de dano moral_ in _Reclamações Trabalhistas_. The STF clarified (2022, ADI 6050)
    that the caps are parameters not ceilings. Any VERMELHO finding may carry a moral damages
    tail that should be noted in the risk assessment.

15. **Delivering TRCT calculations without flagging CCT meal/transport allowances** — Many
    sector CCTs require meal allowances (_vale-refeição_), transport vouchers (_vale-transporte_),
    and health insurance as conditions of employment. If these are omitted from the rescission
    calculation or their nature (salary vs. non-salary) is misclassified, the TRCT may be
    incomplete. Always flag "CCT verification required for benefits" when CCT is unconfirmed.

---

## Writing Standards

Apply plain-language discipline adapted for Brazilian legal contexts:

**For compliance findings** (shared with HR and legal teams):

- Plain language. No unnecessary jargon.
- Active voice: "The employer did not deposit FGTS for March 2025" not "FGTS deposits for
  March 2025 were not made"
- Name the legal consequence: "This exposes the employer to a Reclamação Trabalhista claim
  for R$X" not "this may create issues"
- Use Brazilian Portuguese legal terms with English glosses on first use:
  _rescisão sem justa causa_ (unjust dismissal without cause)
- Cite the specific CLT article — not just the section name

**For TRCT calculations:**

- Show all arithmetic: formula, variable values, result
- Present gross and net figures separately
- Note every INSS and IRRF deduction line
- State the total due, total paid (if known), and any shortfall

**Quality gates before delivery:**

1. Can an HR manager without legal training understand which specific practice violates which
   specific CLT article?
2. Is every VERMELHO finding backed by a CLT article, TST Súmula, or CF/88 provision?
3. Is every TRCT calculation line itemized and mathematically verifiable?
4. Are all Brazilian legal terms glossed in English on first use?
5. Has each VERMELHO finding passed the 3-pass Self-Interrogation?

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

Search for:

- Current CLT text for the articles most relevant to the review
- TST Súmulas and OJs on the specific compliance topic (e.g., Súmula 85 on banco de horas,
  Súmula 291 on aviso prévio reflexos, Súmula 437 on interval)
- Recent TST or STF decisions affecting the specific practice under review
- ANPD or MTE regulatory guidance relevant to eSocial or specific industry NRs

Save results to `/tmp/legalcode-br-clt-research.md`. Mark all legalcode-mcp-sourced
citations as VERIFIED in the Glass Box audit trail.

### Without legalcode-mcp

- Proceed with CLT knowledge from training data
- Mark all TST Súmula and case law references [VERIFY]
- Note in the audit trail: `legalcode_mcp: "Not connected"`
- Recommend the user verify all citations against the TST website (www.tst.jus.br) and
  the CLT on Planalto (www.planalto.gov.br)

---

## Glass Box Audit Trail

Append this YAML block to every output:

```yaml
glass_box:
  skill_name: "legalcode-br-clt-employment-review"
  review_subject: "[Contract title / Worker name / Review scope]"
  review_objective: "[Full audit / Termination review / Payroll audit / etc.]"
  worker_classification: "[CLT employee / PJ contractor / Intermittent / etc.]"
  termination_type: "[Sem justa causa / Justa causa / Distrato / etc. or N/A]"
  governing_law: "CLT (Decreto-Lei 5.452/1943) + Lei 13.467/2017 (Reforma Trabalhista)"
  cct_act_applied: "[CCT/ACT reference or 'Not identified']"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-br-clt-research.md or 'Not created']"
  modules_reviewed:
    - "Module 1: Contract Type"
    - "Module 2: 13th Salary"
    - "Module 3: Férias"
    - "Module 4: FGTS"
    - "Module 5: Overtime / Banco de Horas"
    - "Module 6: Termination / TRCT"
    - "Module 7: Union Obligations"
    - "Module 8: eSocial"
  findings_count:
    vermelho: "[number]"
    amarelo: "[number]"
    verde: "[number]"
  self_interrogation: "PASS / REVISED — [reason if revised]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  confidence_overall: "HIGH / MEDIUM / LOW — [rationale]"
  prescricional_window: "[Termination date + 2 years, if applicable]"
  estimated_financial_exposure: "[R$X or 'Not calculated']"
  limitations:
    - "CCT/ACT not reviewed — findings based on CLT statutory defaults only if not supplied"
    - "FGTS balance not verified — multa calculation based on stated deposit history"
    - "[Any other scope limitations or assumptions]"
  reviewer: "AI-assisted — requires qualified advogado trabalhista review (OAB)"
```

---

## Output Format Template

Structure the final deliverable as:

```markdown
## CLT Compliance Review

**Subject**: [Contract / employee name / scope]
**Objective**: [Full audit / Termination review / Payroll audit / etc.]
**Worker Classification**: [CLT employee / PJ / Intermittent]
**Review Basis**: CLT (Decreto-Lei 5.452/1943) + Lei 13.467/2017
**CCT/ACT Applied**: [Reference or "Not identified — statutory defaults used"]
**Date of Review**: [date]

---

## Executive Summary

[2–4 sentences: overall compliance posture, number of VERMELHO/AMARELO findings,
most critical exposure, recommended immediate action]

---

## Critical Findings (VERMELHO)

### [Finding Title] — 🔴 VERMELHO | Confidence: [level]

**CLT basis**: [Article / TST Súmula cited]
**Facts**: [What the document or practice shows]
**Violation**: [Specific non-compliance]
**Estimated exposure**: [R$X or describe]
**Reflexos**: [Knock-on effects on FGTS, 13th, férias if applicable]
**Remediation**: [Specific action to take]

[Repeat for each VERMELHO finding]

---

## Attention Items (AMARELO)

### [Finding Title] — 🟡 AMARELO | Confidence: [level]

**CLT basis**: [Article or principle]
**Issue**: [Description of the gap or ambiguity]
**Litigation risk**: [Low / Medium / High if unresolved]
**Remediation**: [What documentation or process change resolves this]

[Repeat for each AMARELO finding]

---

## Compliant Modules (VERDE)

| Module        | Basis            | Notes                |
| ------------- | ---------------- | -------------------- |
| [Module name] | [CLT Art. cited] | [Brief confirmation] |

---

## TRCT Calculation (if applicable)

**Termination type**: [e.g., Rescisão sem justa causa]
**Hire date**: [date] | **Termination date**: [date] | **Years of service**: [N]
**Gross monthly salary**: R$[X]

| Verba                               | Gross (R$) | INSS (R$) | IR (R$) | Net (R$) |
| ----------------------------------- | ---------- | --------- | ------- | -------- |
| Saldo de salário ([N] days)         |            |           |         |          |
| Férias vencidas + 1/3               |            |           |         |          |
| Férias proporcionais ([N/12]) + 1/3 |            |           |         |          |
| 13º proporcional ([N/12])           |            |           |         |          |
| Aviso prévio indenizado ([N] days)  |            |           |         |          |
| Multa FGTS (40% / 20% / 0%)         |            | —         | —       |          |
| **Total due**                       |            |           |         |          |
| **Amount paid**                     |            |           |         |          |
| **Shortfall / Overpayment**         |            |           |         |          |

**Payment deadline**: [date + 10 calendar days from termination]
**Late payment penalty**: R$[1 month salary] if paid after [deadline]

---

## Prioritization

**Tier 1 — Address Immediately**:
[List of critical VERMELHO findings with urgency rationale]

**Tier 2 — Address Within 30 Days**:
[List of high-priority VERMELHO and significant AMARELO findings]

**Tier 3 — Address Within 60–90 Days**:
[List of moderate AMARELO findings]

---

## Recommended Next Steps

1. [Specific action] — [Owner] — [Deadline]
2. [...]

---

## Glass Box Audit Trail

[YAML block per Glass Box section above]
```

---

## Localization Notes

This skill covers **Brazilian federal CLT** applicable nationwide. Be aware of:

- **Sector CCTs**: Every professional category in Brazil has a _sindicato_ and typically a
  CCT or ACT. The Ministério do Trabalho e Emprego (MTE) maintains the _SisNeg_ database
  of registered collective agreements. Always verify which CCT governs a given worker's
  category and municipality.
- **Municipal and state laws**: Some states have supplemental employment obligations
  (e.g., São Paulo state wage floor for certain categories). These are subordinate to CLT
  but may impose additional minimums.
- **Simples Nacional employers**: Small companies under Simples Nacional have reduced INSS
  rates and some different compliance obligations. Note if this applies.
- **Hazardous / Unhealthy work environments**: NRs (_Normas Regulamentadoras_) issued by MTE
  impose specific health and safety obligations. Workers in insalubrious or hazardous
  conditions are entitled to _adicional de insalubridade_ (10%, 20%, or 40% of minimum wage)
  or _adicional de periculosidade_ (30% of base salary). This skill flags when these may apply
  but does not conduct a full NR audit.
- **International employees and expats**: Brazilian CLT applies to work performed in Brazil
  regardless of nationality. For expatriates, tax treaty obligations and social security
  totalization agreements may modify INSS exposure.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

- CLT (Decreto-Lei 5.452/1943) text and 2017 Reforma Trabalhista amendments (Lei 13.467/2017)
- Lei 14.442/2022 (teletrabalho update)
- TST Súmulas and OJs (Súmulas 60, 85, 132, 291, 437 and related OJs)
- STF rulings on Reforma Trabalhista constitutionality (2022, ADI 6050 on moral damages caps)
- Lei 12.506/2011 (proportional aviso prévio)
- Lei 8.036/1990 (FGTS) and Lei 4.090/1962 / Lei 4.749/1965 (13th salary)
- eSocial Resolução 2/2016, NT 06/2026, and current S-1.3 layout
- Structural patterns from `legalcode-contract-review` (reference standard for quality frameworks)

All citations should be verified against current CLT text on Planalto
(www.planalto.gov.br) and TST jurisprudence (www.tst.jus.br) before reliance.
