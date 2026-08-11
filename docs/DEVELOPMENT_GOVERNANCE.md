# Development Governance

> How this system changes, who approves change, and how change is recorded.
>
> This document is the public-facing summary of the governance rules that live in `system/01_CORE.md` Section 12 (Governance & Version Control) and Section 40 (Knowledge Foundation Governance). Where this document and the core files differ, **the core files govern**.

---

## 01 — Scope

Governance applies to the three permanent files and the operating contract:

| File | Layer | Governs |
|------|-------|---------|
| `system/00_IDENTITY.md` | Identity | Who the studio is; verified studio identity data |
| `system/01_CORE.md` | Intelligence | How the system thinks; all operating rules |
| `system/02_LIBRARY.md` | Knowledge | What the system knows; sources and confidence |
| `system/PROJECT_INSTRUCTIONS.md` | Contract | Routing, behavior, and permission at the entry point |

Supporting material in `system/PROTOCOL/`, `system/_intake/`, `docs/`, and `README.md` is documentation and is not authoritative over the four files above.

---

## 02 — Change Authority

| Change type | Authority |
|-------------|-----------|
| Project decisions | Majid |
| Core file modification | Majid approval required |
| Identity modification | Majid explicit approval required |
| Library addition | Majid approval required |
| Temporary working notes | May be created without approval |

No permanent rule changes without understanding, proposal, and approval.

---

## 03 — File Responsibility Boundary

```
PROJECT_INSTRUCTIONS.md  →  Routing, behavior, permission
01_CORE.md               →  Reasoning and intelligence
00_IDENTITY.md           →  Who the studio is, and its verified identity data
02_LIBRARY.md            →  What the system knows, and where it came from
```

**Placement rule.** A new operating rule belongs in `01_CORE.md`. `PROJECT_INSTRUCTIONS.md` changes only when routing, permission, or entry-point behavior changes. This keeps the operating contract within its hard character budget and prevents the same rule existing in two files.

**Character budget.** `system/PROJECT_INSTRUCTIONS.md` must never exceed **8,000 characters**. This is a hard limit, verified before every commit that touches the file.

---

## 04 — Change Proposal Format

Every proposed change is presented in this form before it is applied. The full template is in `system/PROTOCOL/UPDATE_PROPOSAL_TEMPLATE.md`.

```
File:        [00_IDENTITY.md / 01_CORE.md / 02_LIBRARY.md / PROJECT_INSTRUCTIONS.md]
Section:     [Number and title]
Action:      [Add / Modify / Remove]
Reason:      [Why this change improves the system]
New Content: [Final English text, ready for insertion]
```

---

## 05 — Update Workflow

```
INPUT → ANALYSIS → CLASSIFICATION → PLACEMENT DECISION
      → CONFLICT CHECK → UPDATE PROPOSAL → APPROVAL → FINAL VERSION
```

No stage is skipped. A change that fails the conflict check is reported, not silently reconciled.

---

## 06 — Versioning

| Version change | Trigger |
|----------------|---------|
| Major (X.0) | Structural change to a core file |
| Minor (0.X) | New section or significant content |
| Patch (0.0.X) | Correction, clarification, formatting |

---

## 07 — Change Record

Every approved change is recorded in `system/02_LIBRARY.md` Section 05 — Improvements History, with date, file, section, change, reason, and source.

The governance record schema for individual changes is defined in `system/01_CORE.md` 40.08:

```yaml
SYSTEM_CHANGE:
  Change_ID:
  Date:
  Requested_By:
  Reason:
  Affected_File:
  Impact:
  Approval:
  Status:       Proposed / Approved / Applied / Reverted
```

---

## 08 — Rollback

Any approved change must be reversible. The previous state must be recoverable from version history before a structural change is applied.

---

## 09 — Numbering Discipline

Section numbering is contiguous and ascending within each file. Original numbering supplied in dictation has no authority over final structure: content is placed where it belongs, then renumbered. Cross-references are updated in the same change.

---

## 10 — Language Governance

| Context | Language |
|---------|----------|
| Core files | English only |
| Communication with Majid | Persian only |
| Client deliverables | As required by the client |
| Prompts and technical instructions | English |

A Persian gloss may follow an English heading in parentheses as a reading aid. The English text always governs.

---

## 11 — Knowledge Admission

Data entering the permanent files is governed by `system/01_CORE.md` Section 40.

```
Never store preference as fact.
Never store example as standard.
Never store assumption as knowledge.

Every permanent rule must have:
Source + Reason + Approval.
```

**Validity states:** `VERIFIED` · `PARTIALLY VERIFIED` · `ASSUMED` · `EXPLORATORY` · `REJECTED`.

`Undefined` is a valid, informative value. Filling an unknown field with a plausible value is a P0 knowledge failure.

---

## 12 — Review Process

| Review | Trigger | Checks |
|--------|---------|--------|
| Contradiction detection | Any core file change | Identity, logic, priority, and duplicate conflicts |
| Overlap review | New section added | No rule stated in two places |
| Structural audit | Milestone transition | Numbering, cross-references, placeholders, orphan links |
| Data validity sweep | Scheduled | Expired verification dates, `Needs Verification` records |

Findings are reported with problem, location, impact, and recommended solution, and wait for approval before being applied.

---

## 13 — Governance Principle

```
A rule without data is a preference.
Data without a source is an assumption.
An assumption presented as knowledge is a system failure.
```
