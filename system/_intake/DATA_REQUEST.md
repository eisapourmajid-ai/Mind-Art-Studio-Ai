# DATA REQUEST — Undefined Items Register

> Purpose: a complete, itemized list of every part of the system that is **structure only** — the template, the field list, and the admission rule exist, but the real data does not.
> Scope: `00_IDENTITY.md`, `01_CORE.md`, `02_LIBRARY.md`, `PROJECT_INSTRUCTIONS.md`.
> Rule: nothing in this file is knowledge. An item becomes knowledge only after it is filled, verified, and migrated into its destination section.
> Population order follows `02_LIBRARY.md` Section 03.12.

---

## Status Summary

| Tier | Meaning | Items |
|------|---------|-------|
| A | Blocking — the system cannot make a real project statement without it | DR-01 … DR-06 |
| B | Operational — the system works, but with generic instead of studio-specific behavior | DR-07 … DR-16 |
| C | Accumulative — fills naturally as projects complete | DR-17 … DR-23 |
| D | Governance — decisions, not data | DR-24 … DR-27 |

| Field state | Meaning |
|-------------|---------|
| EMPTY | No record exists |
| GENERIC | A placeholder value exists that is not studio-specific |
| UNVERIFIED | Named but never confirmed against an official source |

---

## TIER A — Blocking

### DR-01 · Studio Identity Record

**Destination:** `00_IDENTITY.md` → new `01.01` (before System Purpose)
**State:** EMPTY — the files never name the studio, the city of practice, or the practice scale.

```text
Studio name (Latin):
Studio name (Persian):
Architect full name:
Professional registration / license no.:
City and country of practice:
Year established:
Team size:
Practice scale:            [Solo / Small studio / Studio with consultants]
Primary project typologies: [ranked list]
Typical project size range: [m²]
Typical client types:       [from 01_CORE.md 14.06]
Service radius:             [City / Province / National / International]
Default client-deliverable language: [Persian / English / Bilingual]
Website / portfolio:
```

### DR-02 · Iranian National Building Regulations — Mabhath Records

**Destination:** `02_LIBRARY.md` → 02.01
**State:** UNVERIFIED — 22 Mabahes and 2 supplementary modules are named; no edition, no article, no verification date. `LIB-REG-002` stays LOW until this is filled.
**Needed:** one record per Mabhath actually used by the studio (not all 22 at once — start with 03, 04, 15, 19, 21, plus whichever the current projects touch).

```text
Mabhath no.:
Title (Persian):
Title (English):
Edition / revision year:
Publisher and document ID:
Applicability:            [Building types / scales this edition governs]
Articles used by studio:  [article numbers + one-line summary each]
Known local exceptions:
Verification date:
Verified by:              [Majid / Consultant / Authority]
Source link or file name:
```

### DR-03 · Municipal Parameter Register

**Destination:** `02_LIBRARY.md` → 02.02 · mirrors the template in `01_CORE.md` 36.04
**State:** EMPTY — no city, no district, no single stored municipal value.
**Needed:** one record per city/district where the studio actually works.

```text
Municipality:
District / zone:
Land use permitted:
Plot area basis:            [m², per official document]
Density (occupancy):        [% of plot]
Floor area ratio:
Permitted floors:
Maximum height:             [m]
Setbacks:                   [front / rear / side]
Projection allowance:       [depth and conditions]
Parking requirement:        [spaces per unit or per m²]
Green space requirement:    [% or m²]
Access restrictions:        [street width, corner conditions]
Known local interpretation: [what this office decides differently in practice]
Source document and date:
Verification status:        [Verified / Requires verification]
```

### DR-04 · Dimensional Standards

**Destination:** `02_LIBRARY.md` → 02.04
**State:** EMPTY — the admission rule exists, zero dimensions are stored.
**Needed:** the dimensions the studio actually reuses. Suggested first set: parking stall and aisle, ramp slope and width, stair tread/riser/width/headroom, corridor widths, door widths, minimum room dimensions by use, ceiling heights by use, elevator car and shaft, WC and accessible WC, balcony depth, shaft and duct spaces.

```text
Item:
Value and unit:
Tolerance / range:
Jurisdiction:            [National Mabhath no. / Municipality / Professional practice]
Project typology:
Source and version:
Verification date:
Use limitation:
```

### DR-05 · Material Library — Real Records

**Destination:** `02_LIBRARY.md` → 02.05 and the `Material Library` family in 03.05
**State:** EMPTY of products — only behavioral rules exist (`LIB-CON-001` … `LIB-CON-005`).
**Needed:** the studio's actual working palette, one record per material or product.

```text
Material / product name:
Category:                 [Facade / Interior / Floor / Roof / Glazing / Metal / Timber / Stone]
Manufacturer or supplier:
Origin:                   [Domestic / Imported]
Local availability:       [Readily available / Order lead time / Difficult]
Typical lead time:
Cost level:               [Economy / Standard / Premium / Luxury — 01_CORE.md 21.08]
Indicative unit price and date:
Climate behavior:         [Which climate zones it performs in]
Aging behavior:
Maintenance requirement:
Fixing / installation method:
Known failure or defect:
PBR reference:            [roughness / reflectance / texture scale notes]
Datasheet link or file:
Projects used in:
Verification date:
```

### DR-06 · Local Context Records

**Destination:** `02_LIBRARY.md` → 03.07
**State:** EMPTY — eight required fields defined, zero locations recorded.
**Needed:** one record per city or site the studio works in.

```text
Location:                    [City / district / site]
Climate and weather:         [Zone, temperature range, humidity, rainfall, wind, snow — with source]
Culture and social patterns:
Local construction capability: [What contractors here can actually build]
Material availability:
Economic and budget reality:  [Typical construction cost level, date]
Maintenance culture:
Municipal process:            [Permit path, typical duration, known friction]
Neighborhood / urban pattern:
Source:
Confidence:                   [HIGH / MEDIUM / LOW]
Review date:
```

---

## TIER B — Operational

### DR-07 · Studio Graphic DNA — Typography

**Destination:** `01_CORE.md` → 35.06, 35.07, 35.09
**State:** GENERIC — roles are defined ("one neutral grotesque or one restrained serif"), no typeface is named.

```text
Primary Latin family and weights:
Secondary Latin family (if used):
Primary Persian family and weights:
Monospaced family for data / annotation:
Licensing status:            [Owned / Open source / To purchase]
Fallback families:
Deviation from the 35.07 type scale (if any):
```

### DR-08 · Studio Graphic DNA — Color

**Destination:** `01_CORE.md` → 35.10, 35.11 · `00_IDENTITY.md` → 07.05
**State:** GENERIC — roles are defined, no value exists. The **amber-gold signature** in `00_IDENTITY.md` 07.05 has no color specification anywhere in the system.

```text
Base (paper):        HEX / RGB / CMYK
Structure (near-black):
Neutral grey 01:
Neutral grey 02:
Neutral grey 03:
Amber-gold signature: HEX / RGB / CMYK / Pantone
Signature opacity range:      [% for glow / trace / line use]
Accent (if different from signature):
Print profile:                [Coated / Uncoated, ICC profile]
```

### DR-09 · Studio Brand Assets

**Destination:** `01_CORE.md` → 35.74, 35.75
**State:** EMPTY — the mark is governed by rules but does not exist as a file or a definition.

```text
Studio mark file:            [Vector file name]
Mark variants available:     [Full / Compact / Single-color]
Minimum size:                [mm print / px screen]
Clear space rule confirmed:  [Yes — mark height / Custom]
Studio mark on drawings:     [Position]
Sheet template files:        [Per format: A3 / A2 / A1 / A0]
Document template files:     [Proposal / Report / Specification / Transmittal]
```

### DR-10 · Tool Map — Actual Versions

**Destination:** `01_CORE.md` → 16.02, 16.10 · `02_LIBRARY.md` → 03.02
**State:** GENERIC — "Rendering engine of the project standard" and "Approved AI image tools" are placeholders.

```text
BIM:                     [Revit version]
Conceptual modeling:     [SketchUp / Rhino + version]
Rendering engine:        [Corona / V-Ray / Lumion / Twinmotion / Enscape + version]
Post-production:         [Photoshop version]
Layout:                  [InDesign / Illustrator version]
Approved AI image tools: [Tool + plan/version + what it is approved for]
Rejected AI tools:       [Tool + why]
Coordination / clash:    [Navisworks / BIM 360 / other]
Exchange formats used:   [IFC / DWG / FBX + version and unit convention]
Hardware limit:          [Anything that constrains render resolution or time]
```

### DR-11 · Fee and Cost Reality

**Destination:** `01_CORE.md` → 14.03, 14.08, 21.08, 21.09 · `02_LIBRARY.md` → new 02.06
**State:** GENERIC — fee methods and cost levels are listed as categories with no values.

```text
Percentage-of-construction-cost range:  [% by project size]
Area-based rate:                        [currency per m², by typology]
Fixed-fee typical range:                [by deliverable]
Hourly / daily consultation rate:
Per-deliverable visualization rate:     [per image / per sheet / per series]
Payment split actually used:            [% at each stage of 14.08]
Cost level bands:                       [Economy / Standard / Premium / Luxury — currency per m², with date]
Currency and reference date:
Inflation handling rule:                [How long a quote stays valid]
```

### DR-12 · Fee Benchmarking Record — Historical Projects

**Destination:** `01_CORE.md` → 37.05 · `02_LIBRARY.md` → new 02.06
**State:** EMPTY — the record structure exists, no project is recorded.

```text
Project code:
Building type:
Area (m²):
Service scope:
Fee agreed:
Effort actually spent:   [hours or weeks]
Outcome:                 [Profitable / Break-even / Loss]
Cause of variance:
Year:
```

### DR-13 · Project Code Convention and Active Project List

**PARTIALLY RESOLVED:** `MA24` occurrences in `01_CORE.md` 16.02 and 35.79 are now labelled `Example Reference Only`, so the system cannot read them as a declared convention. The real project code convention and active project list are still required.

**Destination:** `01_CORE.md` → 16.04, 35.80 · `01_CORE.md` → 28.04
**State:** GENERIC — the examples use `MA24`, which is illustrative, not a declared convention. No project is registered.

```text
Project code format:      [Confirm MA + YY + NN, or state the real one]
Code register:            [Code → project name, one line each]

Per active project (01_CORE.md 28.04):
Project name:
Project code:
Type:
Location:
Client type:
Area (m²):
Budget level:
Phase:
Status:                   [Active / Hold / Closed]
Classification:           [A Technical Optimization / B Design Development / C Architectural Design / D Signature Project]
```

### DR-14 · Visual Benchmark Assets

**Destination:** `02_LIBRARY.md` → 03.04
**State:** EMPTY — seven categories declared (Exterior PBR, Glass, Lighting/Exposure, Geometry Preservation, Early Client Visual, Final Editorial Board, Social Story), zero entries.
**Needed:** for each category, at least one **Approved Positive** and one **Rejected Negative** asset, with the file supplied.

```text
Benchmark_ID:
Image file name:
Reference_Status:         [Approved Positive / Rejected Negative / Diagnostic]
Visual_Profile:
Task_Type:
Source_Level:
Confidence:
Rights / Permission Status: [Own work / Licensed / Client-owned / Do not publish]
What Works / Fails:
Defect Tags:              [use 02_LIBRARY.md 04.06 pattern names]
Expected QA Result:
Applicable Tools:
Review Date:
```

### DR-15 · Reference Projects

**Destination:** `02_LIBRARY.md` → 03.06
**State:** EMPTY — the template exists, no reference project is recorded.

```text
Name:
Architect / Source:
Source Level / Rights Status:
Applicable Project Type:
Learn:                    [Light strategy / Material language / Spatial experience / Climate response / Detail logic]
Do Not Copy:              [Form / Appearance / Proprietary layout / Signature elements]
Transferable Principle:
Why it matters to this studio:
```

### DR-16 · Discipline Knowledge Catalog Entries

**Destination:** `02_LIBRARY.md` → 03.05
**State:** EMPTY of content — seven families are named, each holds zero knowledge items.
**Needed:** per family, the knowledge items the studio actually relies on.

```text
Catalog family:           [Façade / Interior / Urban-Site / Landscape / BIM-Revit / Visualization / Material]
Knowledge item:
Statement:                [One precise sentence]
Source Level:             [LEVEL 01–05]
Confidence:               [HIGH / MEDIUM / LOW]
Applicable scope:
Limitation:
```

---

## TIER C — Accumulative

### DR-17 · Completed Project Lessons

**Destination:** `02_LIBRARY.md` → 04.02, 04.04
**State:** PARTIAL — all current learnings are generalized from Project 0218 and from studio practice. No completed-project record exists.

```text
Project code:
Lesson category:          [Design / Technical / Visualization / Process / Failure]
What happened:
Generalizable lesson:
Transfer test answer:     [from 04.04]
Source Level / Confidence:
Destination:              [Core Rule / Library Knowledge / Project Memory Only / Benchmark Only]
```

### DR-18 · Failure Archive — Real Events

**Destination:** `02_LIBRARY.md` → 04.05, 04.06
**State:** PARTIAL — SIN-001…SIN-006 and 13 visual patterns are catalogued as pattern knowledge. No dated project-linked failure event is recorded.

```text
Note ID:                  [SIN-007 onward]
Date:
Project code:
Observed failure:
Failure code:             [P0–P6 per 01_CORE.md 39.18]
Root cause:
Classification:           [Project specific / Core systemic]
Proposed change:
Status:                   [Open / Approved / Implemented / Rejected]
```

### DR-19 · Lighting Styles — Measurable Parameters

**Destination:** `01_CORE.md` → 04.16 · related 39.12
**State:** GENERIC — four styles named by feeling, no reproducible parameters.

```text
Style name:
Sun altitude / azimuth:
Color temperature (K):
Sky model / HDRI:
Exposure target (EV):
Shadow softness:
Contrast ratio target:
Reference benchmark image:
```

### DR-20 · Client Communication Assets

**Destination:** `01_CORE.md` → 14.05, 38.07 · `02_LIBRARY.md`
**State:** GENERIC — the proposal structure (14.05) and meeting structure (38.07) are defined; the actual studio wording does not exist.

```text
Standard proposal file:
Standard exclusions list:      [The studio's real exclusions]
Standard assumptions list:
Contract template:
Discovery questionnaire:       [Actual questions used with clients]
Meeting minutes template:
```

### DR-21 · Sheet and Drawing Templates

**Destination:** `01_CORE.md` → 35.13, 35.78, 35.90, 35.91
**State:** GENERIC — anatomy and title-block positions are ruled; no template file exists.

```text
Sheet formats used:            [A3 / A2 / A1 / A0]
Default presentation format:
Title block layout file:
Standard scales used:          [Per drawing type]
Line weight standard:          [Per element]
Hatch / poché standard:
North point and scale bar style:
```

### DR-22 · Archive and Storage Reality

**Destination:** `01_CORE.md` → 16.05, 28.02, 35.79
**State:** GENERIC — the folder trees are prescribed; the real storage location and backup regime are not recorded.

```text
Primary storage:               [Local / NAS / Cloud service]
Backup regime:                 [Frequency, retention, off-site copy]
Naming convention exceptions:
Archive retention period:
Who has access:
```

### DR-23 · Social and Portfolio Channels

**Destination:** `01_CORE.md` → 35.66–35.70, 35.71 · `00_IDENTITY.md` → 07.05
**State:** EMPTY — social and portfolio standards exist; the channels, formats, and confidentiality defaults are not declared.

```text
Active channels:
Post formats and dimensions:
Caption language:              [Persian / English / Bilingual]
Watermark rule:
Client confidentiality default: [Publish only after handover / Case by case]
Portfolio format:              [PDF / Print / Web]
```

---

## TIER D — Governance Decisions (no external data required)

> **All four items in this tier are RESOLVED and applied.** Retained as a decision record.

### DR-24 · Section 10.21–10.23 vs Section 39

**Decision needed:** keep `01_CORE.md` 10.21 Source Fidelity Principle, 10.22 Geometry Lock Register, and 10.23 Design Drift Detection as the quality-gate expression of Section 39, or merge them into 39 and leave cross-references in Section 10.
**Recommendation:** keep them. Deleting them breaks the Quality Gate chain. Section 39.00 already declares authority.

**RESOLVED — Majid:** keep both chains independent. Applied.

### DR-25 · PROJECT_INSTRUCTIONS Character Budget

**Decision needed:** the file is at 7,996 of 8,000 characters. Any future addition requires removing something first.
**Recommendation:** declare a fixed migration rule — new operational rules go to `01_CORE.md`; `PROJECT_INSTRUCTIONS.md` changes only when a routing behavior changes.

**RESOLVED — Majid:** `PROJECT_INSTRUCTIONS.md` is scoped to Routing + Behavior + Permission only. All new rules go to `01_CORE.md`. Applied in v3.0 and recorded in `01_CORE.md` 40.09 and `docs/DEVELOPMENT_GOVERNANCE.md` 03.

### DR-26 · Persian Strings Inside Core Files

**Decision needed:** `01_CORE.md` 08.05, 13.16, 15.04, 15.16 and `02_LIBRARY.md` 03.13 retain Persian text (command examples and local terms). Keep verbatim, or translate with the Persian original in parentheses.

**RESOLVED — Majid:** bilingual labels permitted — English heading with a Persian gloss in parentheses. Persian command examples are Majid's literal input strings under test and are retained verbatim as data. Rule written into `01_CORE.md` 12.09.

### DR-27 · Missing Repository Files

**State:** referenced but absent.

```text
docs/DEVELOPMENT_GOVERNANCE.md   — linked from README, does not exist
LICENSE                          — README states MIT, no file exists
system/_intake/INTAKE_LOG.md     — stale: reports "PARTS received: 0" and "Core files created: No"
02_LIBRARY.md Section 05         — four rows dated 2026-08-04 carry "—" in the Reason column
```

**RESOLVED — Majid:** all three files created or refreshed; MIT confirmed.

| Item | State |
|------|-------|
| `docs/DEVELOPMENT_GOVERNANCE.md` | Created — 13 sections, summarizes `01_CORE.md` 12 and 40 |
| `LICENSE` | Created — MIT, Copyright (c) 2026 Majid Eisapour |
| `system/_intake/INTAKE_LOG.md` | Rewritten as a placement ledger with the M01–M13 destination map |
| `02_LIBRARY.md` Section 05 `—` rows | Open — the four 2026-08-04 rows still need a Reason from Majid |

---

## Delivery Format

For each item, supply data in any of these forms:

1. Filled text block copied from this file, one block per record.
2. A table (CSV or pasted) using the field names above as headers.
3. A document or photograph of the source, with the fields named in the message.
4. Image files for DR-14, with the benchmark fields written beside each file name.

Every record must carry a **source** and a **date**. A record without a source enters the system as `Requires Verification` and cannot be used for a project statement.
