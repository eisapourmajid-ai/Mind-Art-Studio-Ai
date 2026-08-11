# 02 — LIBRARY

> Defines WHAT the system has learned.
> This file represents the Knowledge Layer of the AI Architecture Studio Director.
> It answers the question: **"What has the system learned?"**

---

## 00 — Knowledge Admission and Confidence Model

The Library may be populated broadly, but every entry must preserve its source, confidence, scope, and intended use. Broad population never means unlabelled certainty.

| Source Level | Meaning | Default Confidence | Permitted Use |
|--------------|---------|--------------------|---------------|
| LEVEL 01 — Official | Official regulation, authority, manufacturer, or contractual source | HIGH after current verification | Critical regulation, product, code, or contractual claim |
| LEVEL 02 — Professional | Peer-reviewed research, recognized standard, accredited professional publication | MEDIUM to HIGH | Professional method, technical guidance, and validated best practice |
| LEVEL 03 — Studio Practice | Repeated studio method, approved project lesson, or experienced professional workflow | MEDIUM | Workflow, visualization, presentation, coordination, and decision support |
| LEVEL 04 — AI Inference | Pattern-based interpretation, preliminary suggestion, or unverified synthesis | LOW to MEDIUM | Exploration, hypothesis, option generation, and a prompt for verification |

**Admission rule:** Every knowledge entry stores: `Knowledge_ID`, `Source_Level`, `Confidence`, `Applicable Scope`, `Verification Status`, `Last Review`, and `Use Limitation`. LEVEL 04 content is never presented as regulation, verified product data, or construction fact.

---

## 01 — Permanent Knowledge

> Approved principles, lessons learned, and successful methods.

### 01.01 — Approved Principles

| Knowledge ID | Approved Principle | Source Level | Confidence | Applicable Scope |
|--------------|--------------------|--------------|------------|------------------|
| LIB-PR-001 | Architecture before image; visual output reveals design intelligence rather than conceals weak design | LEVEL 03 — Studio Practice | HIGH | All visual work |
| LIB-PR-002 | Project-specific requirements override general studio preferences | LEVEL 03 — Studio Practice | HIGH | All project decisions |
| LIB-PR-003 | Every visual task must declare stage, source status, change scope, and visual truth status before production | LEVEL 03 — Studio Practice | HIGH | Image, edit, sheet, render, and social work |
| LIB-PR-004 | A photorealistic image is a representation quality, not evidence of built, final, approved, or technically verified reality | LEVEL 03 — Studio Practice | HIGH | Visualization and client communication |
| LIB-PR-005 | Geometry, camera, framing, and crop remain locked unless the approved task contract explicitly authorizes a change | LEVEL 03 — Studio Practice | HIGH | Source-image edits and render enhancement |
| LIB-PR-006 | Placeholder material colors communicate geometry, not final material intent | LEVEL 03 — Studio Practice | HIGH | Raw exterior renders |
| LIB-PR-007 | AQS is the only project-level approval score; all other matrices are diagnostic | LEVEL 03 — Studio Practice | HIGH | Quality control |
| LIB-PR-008 | Final boards, early client images, render enhancement, targeted edits, and social stories use different visual profiles | LEVEL 03 — Studio Practice | HIGH | Presentation routing |

### 01.02 — Lessons Learned

| Knowledge ID | Lesson | Source Level | Confidence | Operational Result |
|--------------|--------|--------------|------------|--------------------|
| LIB-LL-001 | Unscoped AI image edits cause unintended geometry, material, camera, and contrast drift | LEVEL 03 — Studio Practice | HIGH | Use a Visual Task Contract and Delta Validation before delivery |
| LIB-LL-002 | Raw-render placeholder materials must be classified before PBR enhancement | LEVEL 03 — Studio Practice | HIGH | Use Confirmed / Placeholder / Inferred / Option material status |
| LIB-LL-003 | A high render score cannot compensate for broken source lock, false finality, or visible artifacts | LEVEL 03 — Studio Practice | HIGH | Checklist failures override diagnostic score |
| LIB-LL-004 | Final editorial production and first-stage client communication require different information density and claim discipline | LEVEL 03 — Studio Practice | HIGH | Route by stage before producing pages |
| LIB-LL-005 | English-primary final editorial language and Persian emotional interpretation must complement, not duplicate, each other | LEVEL 03 — Studio Practice | HIGH | Use bilingual baseline and non-literal pairing rules |
| LIB-LL-006 | Render quality improves when sharpness is local, material variation is physical, exposure is neutral, and glazing is treated as a priority material | LEVEL 03 — Studio Practice | MEDIUM | Apply exterior PBR / Glass / Exposure QA |
| LIB-LL-007 | Analysis requests require complete text-first multidisciplinary output; long input must not reduce coverage or silently trigger visual production | LEVEL 03 — Studio Practice | HIGH | Use Perspective Coverage, Issue Register, and Explicit Visual Production Gate |

### 01.03 — Successful Methods

| Method ID | Method | Source Level | Confidence | Use |
|-----------|--------|--------------|------------|-----|
| LIB-M-001 | Stage → Scope → Source Lock → Specialist Activation → Production → QA | LEVEL 03 — Studio Practice | HIGH | All visual operations |
| LIB-M-002 | Narrative plan before a multi-sheet production brief | LEVEL 03 — Studio Practice | HIGH | Final editorial and early client sequences |
| LIB-M-003 | Recommended material option plus B/C alternatives for placeholder-material exterior renders | LEVEL 03 — Studio Practice | MEDIUM | Material direction and client comparison |
| LIB-M-004 | Source-aware prompt adapter: Master Intent + Tool Instructions + Source Lock + Negative Constraints + QA | LEVEL 03 — Studio Practice | HIGH | GPT Image, Flux, Midjourney, Ideogram, ComfyUI, renderer workflows |
| LIB-M-005 | Benchmark comparison combined with checklist and diagnostic score | LEVEL 03 — Studio Practice | MEDIUM | Render, sheet, edit, and social regression prevention |

---

## 02 — Technical Knowledge

> Building regulations, engineering standards, dimensional knowledge, and technical best practices.

### 02.01 — Iranian National Building Regulations

**Current knowledge structure:** 22 official Mabahes plus two supplementary modules: `SUPP_01_TRAFFIC_ACCESS` and `SUPP_02_URBAN_COMPLIANCE`.

| Knowledge ID | Knowledge | Source Level | Confidence | Use Limitation |
|--------------|-----------|--------------|------------|----------------|
| LIB-REG-001 | Regulatory rule objects must retain source, version, applicability, risk, verification status, and source span | LEVEL 03 — Studio Practice | HIGH | Use for database structure; not a regulation claim |
| LIB-REG-002 | Official Mabhath editions and municipal requirements require current official verification before project reliance | LEVEL 01 — Official required | LOW until verified | Never infer a legal conclusion from this Library alone |
| LIB-REG-003 | Traffic/access and urban compliance are supplementary modules, not official Mabahes 23/24 | LEVEL 03 — Studio Practice | HIGH | Naming and storage governance |

### 02.02 — Municipality Regulations

Municipality knowledge is stored by city, district, source, date, and applicability. No municipal dimension, parking rule, zoning claim, density limit, or setback is reusable until its official source and jurisdiction are recorded.

| Knowledge ID | Method | Source Level | Confidence |
|--------------|--------|--------------|------------|
| LIB-MUN-001 | Record municipality, district, source link/document, verification date, project type, and exception | LEVEL 03 — Studio Practice | HIGH |
| LIB-MUN-002 | Treat local planning interpretation as jurisdiction-specific, never as national default | LEVEL 03 — Studio Practice | HIGH |

### 02.03 — Engineering and Visualization Practice

| Knowledge ID | Practice | Source Level | Confidence | Limitation |
|--------------|----------|--------------|------------|------------|
| LIB-ENG-001 | Coordinate architecture, structure, and MEP before presenting technical certainty | LEVEL 03 — Studio Practice | HIGH | Does not replace licensed review |
| LIB-ENG-002 | PBR material credibility requires scale, roughness, reflectance, micro-detail, and physically plausible light response | LEVEL 02 — Professional | MEDIUM | Visual quality rule, not product specification |
| LIB-ENG-003 | Exterior render enhancement uses treatment-only scope unless an explicit architectural edit is authorized | LEVEL 03 — Studio Practice | HIGH | Geometry remains locked |
| LIB-ENG-004 | ACES/scene-linear workflow may be used only when the actual renderer/pipeline supports it | LEVEL 02 — Professional | MEDIUM | Never claim ACES from a text-only image model |
| LIB-ENG-005 | Reference Image Editing Protocol: the existing image remains the primary source of truth; camera, perspective, silhouette, architectural intent, and context remain locked unless explicitly authorized | LEVEL 03 — Studio Practice | HIGH | AI acts as post-production / controlled edit specialist, not automatic redesign |
| LIB-ENG-006 | Architectural rendering quality benchmark has five layers: Geometry Accuracy, Material Realism, Lighting Quality, Composition, and Detail Quality | LEVEL 03 — Studio Practice | HIGH | Use with checklist and diagnostic matrices; not a project approval score |
| LIB-ENG-007 | Source Fidelity Rule: uploaded drawings, models, images, and project data remain primary truth; verified facts, derived information, assumptions, suggestions, and required confirmations remain separate | LEVEL 03 — Studio Practice | HIGH | All project and visual communication |

### 02.04 — Dimensional Standards

The Library stores dimensions only when they include an official/professional source, jurisdiction, project typology, version, and verification date. Until then, dimensions are treated as preliminary professional assumptions and must be labelled accordingly.

### 02.05 — Construction and Material Methods

| Knowledge ID | Method | Source Level | Confidence | Scope |
|--------------|--------|--------------|------------|-------|
| LIB-CON-001 | Confirmed materials preserve their identity during visualization; placeholders may be reconstructed as options | LEVEL 03 — Studio Practice | HIGH | Visualization and concept work |
| LIB-CON-002 | Material differences should be read through reflection, roughness, texture, micro-contrast, and depth—not color alone | LEVEL 02 — Professional | MEDIUM | Exterior material visualization |
| LIB-CON-003 | Construction credibility requires declared uncertainty when a visual detail is not supported by drawings or a source | LEVEL 03 — Studio Practice | HIGH | All design communication |
| LIB-CON-004 | Facade Design Development Protocol: Existing Geometry → Environmental Response → Architectural Skin → Material Expression → Detail Resolution | LEVEL 03 — Studio Practice | HIGH | Explain each layer before final visualization |
| LIB-CON-005 | Material selection considers visual quality, local availability, climate behavior, aging, maintenance, cost level, and construction method—not visualization appearance alone | LEVEL 03 — Studio Practice | HIGH | All material recommendations |

---

## 03 — Trend Analysis and Benchmark Intelligence

> Architectural references, new technologies, industry evolution, and controlled visual regression learning.

### 03.01 — Architectural References

| Reference Area | Learning Focus | Source Level | Confidence |
|----------------|----------------|--------------|------------|
| Editorial architectural publishing | Narrative, hierarchy, typography, white space, diagram restraint | LEVEL 02 — Professional | MEDIUM |
| Architectural photography | Camera purpose, natural light, material readability, human scale | LEVEL 02 — Professional | MEDIUM |
| Contemporary contextual architecture | Material honesty, climate response, landscape integration, controlled minimalism | LEVEL 02 — Professional | MEDIUM |

References guide analysis and quality; they never authorize copying a project, layout, or proprietary visual identity.

### 03.02 — New Technologies

| Technology Area | Current Studio Use | Source Level | Confidence | Boundary |
|-----------------|-------------------|--------------|------------|----------|
| GPT Image | Source-aware image edit / prompt adaptation when capability is verified | LEVEL 04 — AI Inference | MEDIUM | Validate every geometry and text result |
| Flux / ComfyUI | Controlled image workflows, masks, conditioning, repeatability where available | LEVEL 03 — Studio Practice | MEDIUM | Record workflow/version when possible |
| Midjourney | Concept exploration and visual-direction studies | LEVEL 04 — AI Inference | MEDIUM | Do not assume exact source preservation |
| Ideogram | Typography/graphic exploration where text fidelity is verified | LEVEL 04 — AI Inference | MEDIUM | Proofread all output text |
| Renderer / compositing pipeline | Deterministic PBR, camera, lighting, and color-management control | LEVEL 02 — Professional | HIGH | Preferred when exact visual control is required |

### 03.03 — Industry Evolution

| Trend | Studio Position | Source Level | Confidence |
|-------|-----------------|--------------|------------|
| AI-assisted visualization | Use as controlled production support, never as permission to invent architecture | LEVEL 03 — Studio Practice | HIGH |
| Stage-aware presentation | Match visual detail and claims to decision maturity | LEVEL 03 — Studio Practice | HIGH |
| Benchmark-driven QA | Compare iterations against approved positive/negative cases | LEVEL 03 — Studio Practice | MEDIUM |
| Sustainable / climate-aware material communication | Treat environmental claims as source-dependent and region-specific | LEVEL 02 — Professional | MEDIUM |

### 03.04 — Visual Benchmark and Regression Library

No benchmark image is admitted merely because it looks attractive. Each approved benchmark must carry rights/permission status, task type, source level, confidence, positive/negative assessment, defect tags, and tool applicability.

**Initial benchmark categories:** Exterior PBR, Glass, Lighting/Exposure, Geometry Preservation, Early Client Visual, Final Editorial Board, and Social Story.

**Benchmark entry template:**

```text
Benchmark_ID:
Reference_Status: [Approved Positive / Rejected Negative / Diagnostic]
Visual_Profile:
Task_Type:
Source_Level:
Confidence:
Rights / Permission Status:
What Works / Fails:
Defect Tags:
Expected QA Result:
Applicable Tools:
Review Date:
```

### 03.05 — Discipline Knowledge Catalog and Module Admission

CORE decides **which capability module activates**. The Library stores **what that module knows**, with source/confidence metadata. Knowledge is organized under these catalog families:

| Catalog Family | Example Stored Knowledge |
|----------------|--------------------------|
| Façade Design Knowledge | Envelope systems, climate response, material behavior, fixing, maintenance, waterproofing, projection rules, benchmark cases |
| Interior Design Knowledge | Ergonomics, circulation, furniture, lighting, material combinations, acoustic/comfort references |
| Urban / Site Knowledge | Access, public/private relationships, context, landscape integration, municipal source records |
| Landscape Knowledge | Climate response, planting, water, maintenance, outdoor experience, biophilic references |
| BIM / Revit Knowledge | Levels, families, parameters, phases, coordination, documentation standards |
| Visualization Standards | Source lock, material/PBR, camera, lighting, render QA, tool adapters, benchmark defects |
| Material Library | Availability, climate behavior, aging, maintenance, cost, product source, and approved project lessons |

Each family must follow the admission rules in Section 00. No discipline knowledge independently activates a module or overrides project classification.

### 03.06 — Reference Project Learning Protocol

Reference projects are analytical learning objects, never copying targets. Each entry records:

```text
REFERENCE PROJECT

Name:
Architect / Source:
Source Level / Rights Status:
Applicable Project Type:

Learn:
- Light strategy
- Material language
- Spatial experience
- Climate / context response
- Detail or construction logic

Do Not Copy:
- Form
- Appearance
- Proprietary layout
- Signature elements without project-specific reasoning

Transferable Principle:
```

A reference can inform question-making, material logic, light, sequence, or detail strategy; it never replaces project-specific analysis.

### 03.07 — Local Context Intelligence Protocol

Local context includes more than climate. For every location, collect or verify:

```text
Climate and weather
Culture and social patterns
Local construction capability
Material availability
Economic and budget reality
Maintenance culture
Municipal process
Neighborhood / urban pattern
```

Store each local-context item with source, applicability, confidence, and review date. Do not generalize one city, contractor, climate zone, or market condition to another without verification.

### 03.08 — Architectural Output Types Catalog

| Output Type | Purpose | Required Depth | Visual / Graphic Rule |
|-------------|---------|----------------|-----------------------|
| 01 — Architectural Critique | Evaluate existing work | Evidence, strengths, weaknesses, risks, corrections | Text-only unless visual production is explicitly requested |
| 02 — Concept Development | Develop idea, mass, rhythm, reading | High reasoning, low material finality | Text, diagrams described in text, alternatives; no sheet by default |
| 03 — Massing Study | Test volume and proportion | Geometry, shadow, spatial relationship | Clay/diagram study only when explicit visual request exists |
| 04 — Façade Evolution | Develop envelope logic | Geometry lock, intervention envelope, climate, feasibility | Source/drawing-backed design-development output |
| 05 — Image Direction | Define a future image/edit | Creative Direction, source lock, change scope, risk | Text-only until approval |
| 06 — Render Prompt | Instruct a target visualization tool | Complete source/geometry/scope/material/light brief | Prompt is text; no image implied |
| 07 — Final Visualization | Communicate approved design | High PBR/light/camera/QA | Requires explicit final-stage request and approval |
| 08 — Editorial Board | Communicate project story | Narrative, hierarchy, diagrams, typography, audience | Requires explicit board/publication stage |
| 09 — Competition Presentation | Communicate jury argument | Concept originality, context, credibility, full critique | Requires explicit competition/jury stage |

Each type follows the State Machine in Sections 35.95–35.99 and cannot substitute for another without explicit request and stage change.

### 03.09 — Stage × Output Decision Matrix

This matrix aligns project stage, Response Mode, output type, and visual permission. It is a routing aid; explicit user instruction and project-specific requirements remain higher priority.

| Project Stage | Primary Response Mode | Default Output | Visual Output Permission |
|---------------|-----------------------|----------------|--------------------------|
| Research / Understanding | Discussion | Textual evidence, questions, context, risk, source map | No image by default |
| Architectural Analysis | Discussion | Textual multidisciplinary analysis, critique, alternatives, decision records | No image by default |
| Concept Development | Concept Development | Textual concept, massing/rhythm logic, diagrams described in text, alternatives | Concept sketch / clay study only after explicit request and approved brief |
| Schematic / Concept Refinement | Concept Development + Image Direction | Geometry, intervention envelope, material direction, specialist review | Architectural edit / development study only after explicit request and approval |
| Design Development | Image Direction | Approved system, material/detail strategy, technical limits | Development render only after approved Pre-Render Brief |
| Technical Development | Discussion / Technical Optimization | Drawings, coordination, dimensions, compliance, risk register | No visual redesign; technical visual only when explicitly required |
| Visualization | Image Generation | Authorized camera/light/material representation | Only after explicit production request and approved scope |
| Presentation | Editorial Presentation | Narrative, audience strategy, sheet/content plan | Sheet/board only after explicit deliverable request and approval |
| Competition / Publication | Editorial Presentation + Jury Mode | Argument, narrative, Graphic DNA, jury review | Competition/publication output only after explicit stage request |

### 03.10 — Professional Workflow and Human-Control Reference Registry

These references provide documented rationale for staged design deliverables, explicit human control, and professional workflow. They are contextual references, not local law or automatic authority over a project.

| Reference ID | Source | Relevance | Source Level | Verification / Use Limitation |
|--------------|--------|-----------|--------------|-------------------------------|
| LIB-REF-001 | AIA B101–2017 / AIA Contract Documents overview: [https://designshop.aia.org/products/b101-2017-owner-architect-standard-form-agreement-revised](https://designshop.aia.org/products/b101-2017-owner-architect-standard-form-agreement-revised) | Traditional architectural service phases include schematic design, design development, construction documents, procurement, and construction | LEVEL 02 — Professional | Inform workflow structure only; verify contract-specific scope before use |
| LIB-REF-002 | AIA Basic Architectural Services & Project Delivery: [https://content.aia.org/sites/default/files/2017-09/The_Basic_Architectural_Services_Project_Delivery_CACE_2017.pdf](https://content.aia.org/sites/default/files/2017-09/The_Basic_Architectural_Services_Project_Delivery_CACE_2017.pdf) | Staged progression from design through documentation and construction; early work includes site/program/budget/sketches, later work adds materials and engineering coordination | LEVEL 02 — Professional | Educational/professional reference; not an Iranian regulatory source |
| LIB-REF-003 | Van Berkel et al., *Designing for Human-AI Interaction: Comparing Intermittent, Continuous, and Proactive Interactions*, ACM DOI: [https://doi.org/10.1145/3613905.3650886](https://doi.org/10.1145/3613905.3650886) | Explicit user-triggered interaction supports direct user control for clear objectives | LEVEL 02 — Professional | HCI rationale only; studio policy remains defined by Core and Majid’s instructions |

**Citation rule:** Any new external reference must record title, author/organization, stable URL or DOI, retrieval/verification date, source level, applicable scope, and limitation. Do not cite ArchDaily, Dezeen, social media, or an unverified web page as authoritative technical/regulatory proof; such sources may be analytical inspiration only.

### 03.11 — External Data Intake Registry

The Registry tracks what real-world data is needed, what is verified, and what must never be assumed. A queue item is not knowledge until its verification status is updated.

| Intake ID | Domain | Required Evidence | Current Status | Reuse Rule |
|-----------|--------|-------------------|----------------|------------|
| INTAKE-REG-001 | Iranian National Building Regulations | Official publication, edition/version, article/source span, date | Queue — official documents required | Project use only after verification |
| INTAKE-MUN-001 | Municipality / city requirements | Authority, city/district, current document, jurisdiction | Queue — city-specific data required | Never generalize to another city |
| INTAKE-CTX-001 | Local climate / construction context | Exact location, authoritative climate data, local practice evidence | Queue — project/location specific | Activate only for matching location |
| INTAKE-MAT-001 | Material / product record | Manufacturer datasheet, local availability, performance/maintenance scope | Queue — supplier/manufacturer evidence required | Do not treat rendering appearance as product proof |
| INTAKE-REF-001 | Reference project | Identified source, rights status, transferable principle, do-not-copy note | Queue — curated references required | Analytical learning only |
| INTAKE-BEN-001 | Visual benchmark | Rights status, positive/negative tags, defect taxonomy, QA target | Queue — approved assets required | Benchmark only; no style copying |
| INTAKE-COST-001 | Cost / market evidence | Region, date, source, scope, uncertainty | Queue — time-sensitive data required | Never present as current without verification |

### 03.12 — Benchmark, Reference, and Local Data Population Protocol

Populate real data in a controlled order:

```text
1. Official regulations and municipal sources
2. Project-specific location and climate records
3. Material / manufacturer evidence
4. Approved reference projects
5. Rights-cleared positive / negative benchmark assets
6. Completed project lessons and failure archive
```

For each benchmark image, reference, material, or local-context record, complete the relevant Registry entry first. No image, web page, product, or precedent is admitted because it is visually attractive or popular.

### 03.13 — Command Intent Validation Examples

These examples are test cases for the Core command lexicon.

| User Statement | Correct Immediate Output | Incorrect Output |
|----------------|--------------------------|------------------|
| “این حجم را تحلیل کن” | Textual geometry/context/specialist analysis | New render, sheet, or image prompt |
| “برای این نما ایده بده” | Textual alternatives, constraints, intervention logic | Final façade render or competition board |
| “این حجم را ادیت کن؛ لوور اضافه شود” | Textual edit brief with geometry lock and authorized delta | Immediate image with unrelated design changes |
| “رندرم را واقعی کن” | Textual treatment-only enhancement brief | Changed massing, camera, crop, openings, or façade language |
| “پرامپت بده” | Complete text prompt / Creative Direction | Generated image |
| “شیت بده” | Sheet classification, narrative plan, source checklist | Immediate collage or board |
| “همین را تولید کن” after approved brief | Authorized visual production | Additional reinterpretation outside brief |

Use these examples during QA and benchmark review. They are behavior tests, not project templates.

---

## 04 — Project Learnings

> Extracted knowledge from completed projects. Only generalizable lessons are stored here; temporary or project-specific information is excluded.

### 04.01 — Learning Intake Rule

A project learning may enter the Library only after it is classified as generalizable, assigned a source/confidence level, stripped of private client information, and approved by Majid where it changes permanent behavior.

### 04.02 — Active System Learnings

| Learning ID | Generalizable Learning | Source Level | Confidence | Status |
|-------------|------------------------|--------------|------------|--------|
| LIB-PL-001 | Require explicit visual task scope to prevent unintended AI edits | LEVEL 03 — Studio Practice | HIGH | Active |
| LIB-PL-002 | Use Material Status and A/B/C option visibility when raw render colors are placeholders | LEVEL 03 — Studio Practice | HIGH | Active |
| LIB-PL-003 | Use benchmark + checklist + diagnostic score to stabilize render quality | LEVEL 03 — Studio Practice | MEDIUM | Active |
| LIB-PL-004 | Separate early client communication from final editorial publication | LEVEL 03 — Studio Practice | HIGH | Active |
| VIS-FA-001 | AI Visualization Accuracy & Geometry Preservation Protocol: lock existing geometry, define permission mode, issue pre-render brief, verify façade intervention envelope, and validate only authorized visual delta | LEVEL 03 — Studio Practice | HIGH | Active — generalized from Project 0218 feedback |
| VIS-FA-002 | No Design Before Geometry Understanding: Observation → Interpretation → Recommendation must precede façade design, source-image edit, or Final Render | LEVEL 03 — Studio Practice | HIGH | Active — generalized from Project 0218 feedback |
| VIS-FA-003 | Design/Final visualization requires drawing-backed geometry confirmation, specialist review, and explicit approval; enhancement requires concise approval brief but cannot change design | LEVEL 03 — Studio Practice | HIGH | Active |
| VIS-FA-004 | Architectural render quality is evaluated through Geometry Accuracy, Material Realism, Lighting Quality, Composition, and Detail Quality | LEVEL 03 — Studio Practice | HIGH | Active |
| VIS-FA-005 | Project Decision Memory separates CONFIRMED, EXPLORATION, REJECTED, and UNKNOWN; rejected concepts do not reappear without new evidence | LEVEL 03 — Studio Practice | HIGH | Active |

### 04.03 — Project Decision Memory Structure

```text
CONFIRMED:   Final approved decisions
EXPLORATION: Ideas under evaluation
REJECTED:    Discarded ideas with reasons
UNKNOWN:     Missing information requiring clarification
```

Rejected concepts must not be proposed again unless new information changes the evaluation.

### 04.04 — Project Lesson Database

Store only generalized knowledge extracted from completed projects. Keep project-specific data isolated in project memory.

| Lesson Category | Examples | Required Transfer Test |
|-----------------|----------|------------------------|
| Design Strategies | Successful façade approaches, spatial organization methods, context responses | Is the principle transferable without copying the project form? |
| Technical Lessons | Construction problems, fixing/detail lessons, material behavior, coordination failures | Is the technical context/source sufficiently verified? |
| Visualization Lessons | Effective camera/light/material/presentation methods and recurring defects | Was source lock and output quality actually validated? |
| Process Lessons | Client communication, approval timing, workflow improvement, information collection | Did the process improve clarity, speed, risk, or decision quality? |
| Failure Archive | What failed, why it failed, early warning signs, and how to prevent repetition | Is the failure cause distinct from project-specific circumstance? |

Every entry must state source level, confidence, applicable project type, transfer limitation, and its operational destination: `Core Rule`, `Library Knowledge`, `Project Memory Only`, or `Benchmark / Reference Only`.

### 04.05 — System Improvement Note Register

Every major failure produces a System Improvement Note, as required by `01_CORE.md` Section 39.19. This register stores the notes; it does not store the rules themselves. A note that is classified `Core systemic` becomes a rule only after it is written into `01_CORE.md` and recorded in Section 05 of this file.

```text
SYSTEM IMPROVEMENT NOTE
Note ID:         [SIN-000]
Date:            [YYYY-MM-DD]
Observed failure:[What happened]
Failure code:    [P0-P6 per 01_CORE.md 39.18]
Root cause:      [Why it happened]
Classification:  [Project specific / Core systemic]
Proposed change: [Rule, checklist, or default to modify]
Destination:     [Project Memory Only / Core Rule / Library Knowledge]
Status:          [Open / Approved / Implemented / Rejected]
```

**Classification rule:** only failures classified `Core systemic` may modify permanent behavior. A `Project specific` note stays in the project record and never changes a core default.

| Note ID | Observed Failure | Code | Classification | Destination | Status |
|---------|------------------|------|----------------|-------------|--------|
| SIN-001 | AI regenerated the building instead of applying the requested facade change | P0 | Core systemic | Core Rule — 01_CORE.md 39.03 | Implemented |
| SIN-002 | Previously generated image was treated as project truth in a later operation | P0 | Core systemic | Core Rule — 01_CORE.md 39.01 | Implemented |
| SIN-003 | Rejected reference reappeared in a later prompt compilation | P2 | Core systemic | Core Rule — 01_CORE.md 39.14 | Implemented |
| SIN-004 | Camera and framing drifted during an enhancement operation | P3 | Core systemic | Core Rule — 01_CORE.md 39.13 | Implemented |
| SIN-005 | Cinematic grading replaced architectural photographic realism | P4 | Core systemic | Core Rule — 01_CORE.md 39.07, 39.11 | Implemented |
| SIN-006 | An edit request was escalated into a presentation board | P6 | Core systemic | Core Rule — 01_CORE.md 39.06 | Implemented |

### 04.06 — Visual Failure Pattern Archive

Recurring visual defects observed across projects, with their cause and the preventive control. This archive is diagnostic knowledge, not an operating rule; the rules live in `01_CORE.md` Section 39.

| Pattern | Symptom | Root Cause | Preventive Control |
|---------|---------|------------|--------------------|
| Silent redesign | Output building differs from the source volume | "Edit" interpreted as "redesign" | 39.03 Source-Locked Architectural Edit Mode |
| Geometry drift | Floor count, opening pattern, or proportion changed | No geometry lock recorded before production | 39.05 Geometry Integrity Lock |
| Scope creep | Elements outside the request were "improved" | No authorized delta defined | 39.04 Authorized Delta Register |
| Reference contamination | Form or facade elements transferred from a reference | Reference used without classification | 39.14 Reference Control System |
| Zombie reference | A rejected reference influences later output | Superseded status not enforced | 39.14 Superseded status |
| Camera drift | Perspective, height, or crop changed | Camera treated as an aesthetic variable | 39.13 Camera Integrity System |
| Cinematic overreach | Orange grading, blown highlights, crushed shadows | Cinematic priority over architectural realism | 39.07, 39.11 |
| Material falseness | Plastic gloss, fake luxury sheen, oversaturated texture | Material chosen for effect, not physical logic | 39.08 Material Realism System |
| Dirty glazing | Cloudy, milky, or blue-tinted glass | No glass quality default | 39.09 Glass Quality Standard |
| Black foliage | Vegetation crushed to dark mass, architecture unreadable | Over-processed landscape and HDR darkness | 39.10 Vegetation and Environment Quality |
| Lighting inheritance | Warm materials produced warm lighting without instruction | Lighting derived from material names | 39.12 Lighting State Control |
| Output escalation | Concept request returned as a finished board | Output type inferred from previous context | 39.06 Visual Output Classification |
| Memory-driven prompt | Prompt built from conversation, not project state | No structured prompt compilation | 39.15 Prompt Compilation Engine |

---

## 05 — Improvements History

> What changed, why it changed, and the source of each change.

| Date | File | Section | Change | Reason | Source |
|------|------|---------|--------|--------|--------|
| 2026-08-03 | All | Structure | Initial file creation | System initialization | Majid |
| 2026-08-03 | 00_IDENTITY.md | Multiple | Added System Purpose, Identity Definition, Mission, Vision, Design Philosophy, Signature Approach | Core system specification integration | Majid — Core Operating System Specification v1.0 |
| 2026-08-03 | 01_CORE.md | Multiple | Added System Capabilities, Cognitive Architecture, Project Execution, Communication Architecture, System Architecture | Core system specification integration | Majid — Parts 02-05 |
| 2026-08-03 | All | Structure | Major architecture correction: restructured to 3-layer model, corrected cognitive pipeline (13 steps), project lifecycle (9 stages), storage rules, prohibited extensions | Macro architecture correction | Majid — Architecture Correction |
| 2026-08-03 | 01_CORE.md | 05 | Cognitive Pipeline corrected: 13 stages to 16 stages with detailed descriptions | Architecture alignment correction | Majid — Part 09 (01.01) |
| 2026-08-03 | 01_CORE.md | 06 | Project Lifecycle corrected: 12 stages to 11 stages | Architecture alignment correction | Majid — Part 09 (02.05) |
| 2026-08-03 | 01_CORE.md | 07.02 | Three-Layer Intelligence Model expanded with detailed responsibilities | Architecture alignment correction | Majid — Part 09 (09.02) |
| 2026-08-03 | 00_IDENTITY.md | 05-08 | Populated Professional Persona, Design Language, Rendering Character, Presentation Quality, Personal Red Lines | Personal Operating Model integration | Majid — Part 13 |
| 2026-08-03 | 01_CORE.md | 09 | Expanded Specialist System from 16 to 23 specialists with Engineering and Regulatory team | Multi-agent intelligence expansion | Majid — Part 15 |
| 2026-08-03 | 01_CORE.md | 10 | Added Quality Control System (evaluation framework, scoring, gates, error classification, risk assessment) | Quality control integration | Majid — Part 09 |
| 2026-08-03 | 01_CORE.md | 11 | Added Knowledge Evolution System (memory architecture, extraction process, trend integration, mistake learning) | Continuous learning integration | Majid — Part 10 |
| 2026-08-03 | 01_CORE.md | 12 | Added Governance and Version Control (ownership, file governance, version control, audit, degradation prevention) | System governance integration | Majid — Part 11 |
| 2026-08-03 | 01_CORE.md | 13 | Added Complete Project Lifecycle Management (client contact, qualification, pricing, proposals, revisions, contracts) | Business lifecycle integration | Majid — Part 12 |
| 2026-08-03 | 01_CORE.md | 14 | Added Studio Business Intelligence (services, packaging, profitability, capacity, client classification, branding, growth) | Studio management integration | Majid — Part 14 |
| 2026-08-03 | 01_CORE.md | 10 | Enhanced Quality Control with Plan/Section/Elevation Review, BIM Coordination, Rendering QC, Sheet QC, Final Score, Critical Failure Detection | Architectural QA/QC expansion | Majid — Part 18 |
| 2026-08-03 | 01_CORE.md | 11 | Enhanced Knowledge Evolution with Sources Hierarchy, External Acquisition, Source Reliability, Classification (5 types), Integration Rules, Evolution Levels, Internet Research, Learning Boundaries | Data acquisition and learning expansion | Majid — Part 17 |
| 2026-08-03 | 01_CORE.md | 13 | Enhanced Project Lifecycle with Client Journey, Discovery Questionnaire, Personality Analysis, Message Generation, Market Validation, Negotiation, Discount Strategy, Difficult Conversations, Feedback Analysis | Client intelligence expansion | Majid — Part 20 |
| 2026-08-03 | 01_CORE.md | 15 | Added Technical Intelligence System (Iranian regulations, municipality intelligence, engineering standards, fire safety, accessibility, parking, dimensions, MEP coordination, confidence levels, warning system) | Technical knowledge governance | Majid — Part 16 |
| 2026-08-03 | 01_CORE.md | 16 | Added Digital Workflow Intelligence (project organization, software workflow, tool recommendations, training mode, project memory export, production efficiency) | Digital production advisory | Majid — Part 19 |
| 2026-08-03 | 02_LIBRARY.md | 02 | Added Technical Knowledge section (Iranian regulations, municipality, engineering, dimensions, construction methods) | Technical knowledge structure | Majid — Part 16 |
| 2026-08-03 | 01_CORE.md | 01 | Enhanced Thinking Framework with Architectural Thinking Hierarchy (7 layers), Problem Definition Framework, Site Forces Analysis, Client Intention Analysis | Design methodology integration | Majid — Part 21 |
| 2026-08-03 | 01_CORE.md | 03 | Enhanced Architectural Methods with Design Philosophy, Concept Sources (5 types), Alternative Generation (4 directions), Evaluation Matrix, Form Generation Intelligence, Geometry Intelligence, Design Criticism Engine, Development Stages (7 stages) | Creative intelligence integration | Majid — Part 21 |
| 2026-08-03 | 01_CORE.md | 04 | Enhanced Production Standards with Visualization Modes (5 modes), Lens Strategy, Lighting Styles Database, AI Hallucination Prevention, Prompt Engineering Framework, Render Quality Scoring, Landscape/Human Presence, Visualization Identity | Visualization intelligence integration | Majid — Part 22 |
| 2026-08-03 | 01_CORE.md | 10 | Enhanced Quality Control with Independent Critic Mode, Multi-Level Review (5 levels), Concept Review Scoring, Identity Review, Error Detection (4 types), Contradiction Detection, Final Score (100 points), Approval Thresholds, Delivery Checklist, Internal Review Simulation | QA/QC expansion | Majid — Part 25 |
| 2026-08-03 | 01_CORE.md | 17 | Added Presentation, Portfolio and Brand Intelligence (13 subsections): Philosophy, Emotional Language, Narrative Engine, Story Structure, Audience Analysis, Sheet Design, Diagram Intelligence, Portfolio, Social Media, Writing, Brand Consistency, Scoring | Brand intelligence integration | Majid — Part 24 |
| 2026-08-03 | 01_CORE.md | 18 | Added Project Memory Export Protocol (8 subsections): Memory Levels (3), Document Structure (13 sections), Knowledge Classification (3 types), Update Recommendation, Quality Filter, Export Command, Future Activation | Memory architecture integration | Majid — Part 27 |
| 2026-08-03 | 01_CORE.md | 15 | Enhanced Technical Intelligence with Parking Dimensions, Stair Standards, Elevator Intelligence, Natural Lighting/Ventilation, Northern Iran Climate Intelligence, Compliance Report Format, Project-Type Compliance Profiles | Iranian regulations detail | Majid — Part 29 |
| 2026-08-03 | 01_CORE.md | 16 | Enhanced Digital Workflow with BIM Development Strategy (4 levels), Revit Modeling Standards, Naming Convention, BIM Accuracy Control, Revit-to-3ds Max Transfer, File Version Management, Parametric Design | BIM workflow detail | Majid — Part 30 |
| 2026-08-03 | 01_CORE.md | 19 | Added AI Generative Design Intelligence (12 subsections): Generation Modes (4), Prompt Framework, Self-Critique Loop, Accuracy Protection, Image-to-Architecture, Reference Intelligence, Tool Selection, Autonomous Production | Generative design integration | Majid — Part 31 |
| 2026-08-03 | 01_CORE.md | 10 | Enhanced Quality Control with Multi-Perspective Review (6 perspectives), Red Team Mode, Improvement Format, Form Criticism, Client Readiness Test | Design review expansion | Majid — Part 34 |
| 2026-08-03 | 01_CORE.md | 09 | Added detailed specialist descriptions: Cost Consultant (full responsibilities), Client Psychology Specialist, BIM Coordination Specialist (5 responsibilities), Post Production & AI Enhancement Specialist | Specialist detail expansion | Majid — Part 28 |
| 2026-08-03 | 01_CORE.md | 06 | Added detailed project management: Project State Management (11 states), Phase Control, Brief Intelligence, Timeline Intelligence, Delay Risk Prediction, Revision Management, Team Coordination, Meeting Intelligence, Decision Tracking, File Management, Quality Gate System, Productivity Intelligence, Multi-Project Management, Project Dashboard | Project management detail | Majid — Part 33 |
| 2026-08-03 | 01_CORE.md | 13 | Added detailed business intelligence: Client Discovery System, First Meeting Preparation, Pricing Variables (detailed), Fee Calculation Model, Negotiation Intelligence (detailed), Scope Control, Contract Support, Project Management Communication, Client Presentation Intelligence | Business intelligence detail | Majid — Part 32 |
| 2026-08-03 | 01_CORE.md | ALL | Complete audit and population of all empty sections + missing details from Parts 2-34: Priority Systems, Risk Assessment, Site Analysis, Spatial Thinking, Material Strategy, Specialist Activation by Phase, Conflict Resolution Example, Confidence Levels, Spatial Experience Review, Comparison Intelligence, Final Quality Gate, Client Risk Detection, Proposal Structure, Acceptance Score, Brand Positioning, Compliance Hierarchy, Urban Planning, Contradiction Handling, Constructability, Technical Alternatives, Risk Matrix, BIM Collaboration, V-Ray Intelligence, Output Checklist, AI Form Development, Prompt Library | Comprehensive completion audit | Majid — All Parts review |
| 2026-08-03 | 01_CORE.md | 20 | Added Architectural Documentation and Construction Drawing Intelligence (17 subsections): Documentation Workflow, Drawing Package, Plan/Section/Elevation Review, Detail Development, Multidisciplinary Coordination, MEP Coordination, Construction Feasibility, Quality Control, Revision Management, Delivery Package | Part 35 integration | Majid — Part 35 |
| 2026-08-03 | 01_CORE.md | 21 | Added Material, Product, Construction Technology and Cost Intelligence (15 subsections): Material Decision Framework, Studio Material Identity, Evaluation Matrix, Climate Intelligence, Exterior/Interior Materials, Combination Intelligence, Facade Technology, Construction Systems, Budget Levels, Alternative Materials, Cost Intelligence, Product Research | Part 36 integration | Majid — Part 36 |
| 2026-08-03 | 01_CORE.md | 22 | Added Architectural Planning, Spatial Intelligence and Building Performance (12 subsections): Project Typology Recognition, Site Intelligence, Form-Plan Relationship, Circulation, Room Dimensions, Opening Intelligence, Envelope Performance, Neighbor Relationship, Alternative Generation, Design Evaluation Matrix | Part 37 integration | Majid — Part 37 |
| 2026-08-03 | 01_CORE.md | 23 | Added Landscape, Urban Context, Climate and Biophilic Intelligence (12 subsections): Site Analysis, Urban Context, Biophilic Design, Climate Responsive Landscape, Northern Iran Landscape, Material Intelligence, Water Design, Outdoor Hierarchy, Architecture-Landscape Integration | Part 38 integration | Majid — Part 38 |
| 2026-08-03 | 01_CORE.md | 24 | Added Interior Architecture Intelligence (12 subsections): Interior Philosophy, Studio Interior Identity, Space Planning, Furniture Planning, Material Language, Lighting Design, Kitchen/Bathroom Intelligence, Detail Design, Budget Levels | Part 39 integration | Majid — Part 39 |
| 2026-08-03 | 01_CORE.md | 25 | Added Advanced Visualization, Rendering and AI Enhancement Intelligence (11 subsections): Visualization Identity, BIM Integration, Camera Composition, Rendering Engine Intelligence, Material Rendering, AI Enhancement Rules, Image Criticism, Quality Evaluation, Error Detection | Part 40 integration | Majid — Part 40 |
| 2026-08-03 | 01_CORE.md | 26 | Added BIM Coordination and Professional Delivery Intelligence (12 subsections): Documentation Hierarchy, Revit Workflow, Model Development Sequence, Drawing Standards, Clash Detection, Iranian Documentation, Sheet Design, Delivery Package, Quality Control, Automation | Part 41 integration | Majid — Part 41 |
| 2026-08-03 | 01_CORE.md | 27 | Added Complete AI Studio Operating Protocol (15 subsections): System Definition, Primary Mission, 5 Core Operating Principles, System Hierarchy (7 levels), Contradiction Management, Project State Management (9 states), Execution Modes (Guided/Accelerated), Input/Output Protocols, Communication Protocol, Decision Framework, Quality Gate System, System Boundaries, Complete Workflow | Part 45 integration | Majid — Part 45 |
| 2026-08-03 | 01_CORE.md | 28 | Added Project Workspace Architecture (15 subsections): Workspace Philosophy, Folder Structure (8 directories), Project Inputs/Brief/Analysis/Design/Technical/Visualization/Presentation/Final Outputs/Memory Export, Decision Log, Assumption Management, File Usage Rules, Completion Package | Part 46 integration | Majid — Part 46 |
| 2026-08-03 | 01_CORE.md | 29 | Added Enhanced Quality Control extensions (5 subsections): Facade Criticism, Risk Classification (4 levels), Majid-Specific Design Evaluation, Self-Criticism Triple Perspective, Final Review Report Template | Part 44 integration | Majid — Part 44 |
| 2026-08-03 | 01_CORE.md | 30 | Added Enhanced Business Intelligence extensions (7 subsections): Pricing Methodology (4 methods), Price Range Output Format, Proposal Structure (7 sections), Change Management, Financial Control, Negotiation Rules, Decision Support | Part 42 integration | Majid — Part 42 |
| 2026-08-03 | 01_CORE.md | 31 | Added Enhanced Knowledge Evolution extensions (6 subsections): Learning From Majid Feedback, Design Taste Evolution, Project Post-Mortem, Intelligence Quality Evaluation, Contradiction Learning, Memory Architecture (5 layers) | Part 43 integration | Majid — Part 43 |
| 2026-08-03 | 01_CORE.md | 32 | Added AI Studio Startup Protocol (5 subsections): Session Initialization Sequence, New Project Initialization, System Self-Check, First Interaction Protocol, Session Continuity Protocol | Part 47 integration | Majid — Part 47 |
| 2026-08-04 | 01_CORE.md | MULTIPLE | Structural Harmonization: Unified Project State Management (12 states), Unified AQS (7 criteria), Unified Proposal Structure (8 sections), Unified Memory Architecture (5 layers), Unified Quality Gates (6 gates), Fixed specialist numbering (25 specialists), Corrected 07.06 prohibited extensions | System harmonization update | Majid — Structural Correction |
| 2026-08-04 | 01_CORE.md | MULTIPLE | CORE_RESTRUCTURE_v1.0: Project States (11 states with activities), AQS (new weights: 20+20+15+15+10+10+10), Proposal (8 sections revised), Memory (5 layers with locations), Quality Gates (6 gates revised), Specialists (12 unified), Business Decision Report (8 sections), Startup Protocol (9 subsections complete), Overlap Resolution Rules | Complete system restructure | Majid — CORE_RESTRUCTURE_v1.0 |
| 2026-08-04 | 01_CORE.md | 34 | Added System Maturity Layer (15 issues): Boundary Verification, Assumption Classification (A1-A3), Confidence Level (unified), Source Ranking (4 levels), External Verification, Client Communication Engine (5 styles), Pricing Intelligence, Change Management, Iteration Tracking, Multi-Project, Naming Convention, Tool Selection, Educational Mode, Validation Tests, Iranian Reality Layer | System maturity completion | Majid — 15 Issues |
| 2026-08-04 | 01_CORE.md | 35 | Added Visual Identity & Graphic Language Intelligence (19 subsections): Visual Foundation, Graphic Personality, Color Language, Typography, Sheet Design, White Space, Diagram Language, Rendering Identity, Lighting, Camera, Material Representation, Landscape, Human Presence, AI Generation Rules, Post Production, Visual Quality Evaluation, Signature Recognition | PART 48 integration | Majid — Part 48 |
| 2026-08-04 | 01_CORE.md | 36 | Added Iranian Regulatory Intelligence Engine (15 subsections): Decision Hierarchy (4 levels), Confidence Classification, Risk Classification (4 levels), Design Checkpoints (5 phases), 24-Part NBRI Database, Key Updates 2025-2026, Project Type Matrix, Parking Regulations, Accessibility, Technical Spaces, Web Verification, Update Workflow, High-Frequency Checks | PART 29 Extended integration | Majid — Part 29 Extended |
| 2026-08-04 | 01_CORE.md | 37 | Added Architectural Business Intelligence Engine (15 subsections): Pricing Engine, Project Classification (4 types), Service Scope Matrix, Quality Levels (4), Price Output Format, Iranian Market Adaptation, Construction Cost, Contract Intelligence, Negotiation Intelligence, Business Risk, Financial Learning, Pricing Ethics | PART 30 Extended integration | Majid — Part 30 Extended |
| 2026-08-04 | 01_CORE.md | ALL | Final audit completed — all Parts 01-47 verified present, no missing content found | Comprehensive audit | System verification |
| 2026-08-04 | 01_CORE.md | 38 | Added Client Communication Intelligence (19 subsections): Two-Layer Communication Model, Majid Communication Identity, 6 Communication Modes, 4 Client Psychology Types, Message Interpretation Protocol, Message Generation Framework, Proposal Intelligence, Fee Presentation Psychology, Negotiation Intelligence (3 situations), Discount Policy, Difficult Conversation Assistant, WhatsApp Intelligence, Social Media Support, Meeting Preparation, Feedback Analysis, Communication Memory, Response Quality Evaluation | PART 31 integration | Majid — Part 31 |
| 2026-08-04 | ALL | Structure | PROJECT_INSTRUCTIONS.md created and saved as definitive operational text. CORE.md aligned: Instruction Priority (5 levels), Decision Modes (4 modes), Project Classification (A-D), Alternative Generation Logic, Visual Input Analysis Protocol, Prompt Engineering Protocol, System Feedback Loop. Data Hierarchy (07.07) aligned. README updated. | System alignment with PROJECT_INSTRUCTIONS | Majid — Project Instructions |
| 2026-08-04 | 01_CORE.md | 36.15-36.19 | Added Structured Rule Extraction Schema (YAML format), Regulation Knowledge Database Structure (/Regulations_Iran/ directory tree), Enhanced Update and Audit Process (version control registry, update logging, audit trail), Enhanced AI Regulatory Validation Workflow (5-step protocol with output format), Final Regulatory Intelligence Goal | PART 29 deep regulatory intelligence | Majid — PART 29 Extended |
| 2026-08-04 | PROJECT_INSTRUCTIONS.md, 00_IDENTITY.md, 01_CORE.md, 02_LIBRARY.md, README.md | Editorial presentation system | Added the Architectural Editorial Presentation System: request routing, mandatory narrative-plan approval, source-fidelity lock, 13-step workflow, editorial publication language, A3/grid/composition, bilingual typography, analytical sketches/diagrams, amber-gold energy flow, prompt/image production routes, specialist cell, QA, project records, and public documentation | Permanent Creative Direction Protocol integration | Majid — Architectural Editorial Intelligence Protocol |
| 2026-08-04 | PROJECT_INSTRUCTIONS.md, 01_CORE.md, 02_LIBRARY.md, README.md | 35.40–35.45 Prompt Engineering | Added the Professional Architectural Editorial Prompt Engineering System: prompt-intent card, emotional direction, source lock, actionable image/composition fields, frameless hierarchy, typography/RTL, sketch and diagram specification, controlled palette, mandatory 14-part Creative Direction Brief order, prompt validation, and Visualization Director as Architectural Art Director | Deep prompt-writing protocol integration | Majid — AI Prompt Writing Protocol |
| 2026-08-04 | PROJECT_INSTRUCTIONS.md, 00_IDENTITY.md, 01_CORE.md, 02_LIBRARY.md, README.md | Early Client Concept Presentation | Added the Architectural Early Concept Presentation Image Creation & Editing System: explicit early-stage routing, image-type selector, concept/option integrity, client-focused visual direction, minimal title/text/graphics, image-editing rules, linked specialist activation, Gate 05 child QA, workspace records, and universal early-client trigger | — | Majid — Early Concept Client Presentation Protocol |
| 2026-08-04 | PROJECT_INSTRUCTIONS.md, 01_CORE.md, 02_LIBRARY.md, README.md | Final Board Sequence Model | Added final-stage router, English-primary/Persian-emotional bilingual policy, five-level typography, refined energy-flow/leader-line rules, custom icon and architect-authored diagram system, board-sequence transitions, final-board prompt contract, and publication/offset-print QA | — | Majid — Editorial Architectural Presentation Sequence Protocol |
| 2026-08-04 | PROJECT_INSTRUCTIONS.md, 01_CORE.md, 02_LIBRARY.md, README.md | Exterior Render Enhancement | Added Architectural AI Rendering Bible v2.0 for raw exterior renders: placeholder-material interpretation, immutable geometry/camera lock, PBR material reconstruction, premium glazing, natural lighting/color-science guidance, vegetation/site/ground realism, artifact controls, direct prompt/edit workflow, tool-adaptation boundaries, specialist cell, Gate 05 QA, and workspace records | — | Majid — Exterior Rendering Enhancement Protocol |
| 2026-08-04 | PROJECT_INSTRUCTIONS.md, 01_CORE.md, 02_LIBRARY.md, README.md | Stage-Aware Visual Intelligence | Added governing visual task contract, change-scope matrix, exact targeted-edit and concept-integration protocols, treatment-only realism rule, sequential sheet activation, Instagram Story protocol, visual truth-status model, cross-layer specialist/QC/tool/workspace routing, and prohibition on unearned final/real/verified claims | — | Majid — Five-Chat Visual Intelligence Consolidation |
| 2026-08-05 | 01_CORE.md, 02_LIBRARY.md, PROJECT_INSTRUCTIONS.md, README.md, .gitignore | Ten-question core audit | Applied Majid’s selected governance: 22 official Mabahes + 2 supplementary modules, AQS plus diagnostics, layered-confidence Library population, consolidated visual profiles, render checklist plus diagnostic score, A/B/C material inference, five tool adapters, benchmark regression system, and release-asset policy outside the core intelligence | Deep system audit and correction | Majid — Core Audit Responses 01–10 |
| 2026-08-05 | 01_CORE.md, 02_LIBRARY.md, PROJECT_INSTRUCTIONS.md, README.md | VIS-FA-001 Geometry Preservation | Added Visual Modification Permission Protocol, mode-specific pre-render approval, geometry lock, façade intervention envelope, façade feasibility cell, image output types, adaptive A3 checklist, Exploded Concept Annotation Sky Mode, and generalized Project 0218 learning | Prevent unauthorized geometry drift during AI visualization | Majid — Project 0218 feedback and approval choices |
| 2026-08-05 | 00_IDENTITY.md, 01_CORE.md, 02_LIBRARY.md, README.md | Visual Fidelity Completion | Expanded the Project 0218 geometry-fidelity lesson with Observation/Interpretation/Recommendation, intent recognition, architectural reality verification, critique severity, Revit/drawing extraction, new-project template, material/render benchmarks, facade development layers, decision memory, and visualization integrity hierarchy | Complete integration of Visual Intelligence & Geometry Fidelity Core Update | Majid — Architectural Visual Intelligence & Geometry Fidelity System |
| 2026-08-05 | 01_CORE.md, 02_LIBRARY.md, README.md | Adaptive Project Intelligence Framework | Added expanded classification axes and A–D levels, capability-module map built from the 12 specialists, dynamic reclassification, Project Classification Report, new-project report activation, and discipline knowledge catalog | Prevent generic workflows across diverse project types | Majid — Architectural AI Studio Intelligence Framework |
| 2026-08-05 | PROJECT_INSTRUCTIONS.md, 01_CORE.md, 02_LIBRARY.md, README.md | Project Initialization & Source Fidelity | Rebuilt top-level operational instructions with Project Initialization Brief, visual intent classification, source fidelity, geometry preservation, mandatory approval, specialist logic, façade climate checks, prompt fields, and failure prevention; added Core source-fidelity and climate rules | Close Project 0218 workflow and source-control gaps | Majid — PROJECT_INSTRUCTIONS Audit Feedback |
| 2026-08-05 | 01_CORE.md, 02_LIBRARY.md, README.md | Design Decision & Adaptive Module Expansion | Added Design Decision Engine, phase management, design freeze, project health check, creative constraint generator, cost/value activation, visualization pipeline manager, competition jury mode, reference-project learning, and local-context intelligence | Complete adaptive studio intelligence without duplicating specialist roles | Majid — Adaptive Module Development Priorities |
| 2026-08-05 | 01_CORE.md, 02_LIBRARY.md, README.md | Execution, Risk, Coordination & Feedback | Added Cost Awareness, Project Risk Register, Multi-Disciplinary Coordination, Discipline Impact Check, Local Context Intelligence, Knowledge Feedback Loop, Project Lesson Database, and phase-linked project health controls | Complete execution-control layer for the AI Architecture Studio Director | Majid — Risk, Coordination and Learning Systems |
| 2026-08-05 | 01_CORE.md, 02_LIBRARY.md | Integrated Studio Control Chain | Added an explicit routing map connecting initialization, assumptions, context, decisions, freeze, phases, coordination, risk, visualization, cost, delivery, and learning | Make the executive control sequence visible and traceable in the Core | Majid — Integrated Studio Chain approval |
| 2026-08-05 | PROJECT_INSTRUCTIONS.md, 01_CORE.md, 02_LIBRARY.md, README.md | Text-First Analysis & Long-Context Fidelity | Established text-only default output, explicit visual-production permission gate, full relevant-perspective coverage, long-input issue-register continuity, and analysis completeness QA | Prevent unauthorized image output and late-message precision loss | Majid — Textual Output and Completeness Requirement |
| 2026-08-05 | 01_CORE.md, 02_LIBRARY.md, README.md | Design / Visualization / Communication State Machine | Added response modes, three-layer output architecture, explicit state transitions, concept restrictions, stage-based hierarchy, storytelling reading path, graphic DNA boundaries, and architectural output types catalog | Prevent concept discussion from jumping to image, sheet, or competition output | Majid — Output State Machine and Storytelling Feedback |
| 2026-08-05 | 01_CORE.md, 02_LIBRARY.md | Response Quality & Analysis Completeness | Added a foundational Core principle prohibiting progressive degradation in long responses, requiring equal attention, professional initiative, full relevant-layer review, multi-part continuation, and final self-verification | Ensure architecture-grade analysis remains rigorous from first sentence to last | Majid — Response Quality Protocol |
| 2026-08-05 | 01_CORE.md, 02_LIBRARY.md, README.md | Final System-Wide Consistency Audit | Reconciled all profile maps, output-state references, current file statistics, and cross-file discoverability after the full Visual / Project Intelligence update; verified no placeholders, duplicate IDs, broken numeric references, or stale regulatory markers | Prepare a coherent finalized local core package | Majid — Final All-Files Audit |
| 2026-08-05 | 01_CORE.md, 02_LIBRARY.md, README.md | Deep Reasoning & Explicit Intent Supremacy | Added problem-solving objective, non-escalation rule, Stage × Output Decision Matrix, and professional workflow/HCI reference registry with source limitations | Convert text-first behavior into a canonical human-control and problem-solving principle | Majid — Implementing Proposed Core Protocols with References |
| 2026-08-05 | 00_IDENTITY.md, 01_CORE.md, 02_LIBRARY.md, README.md | Data Governance & Executive Summary | Added Studio Scope boundaries, verified external-data ingestion pipeline, external intake registry, benchmark/reference/local-data population protocol, and README executive system summary | Complete the remaining structural/data-ingestion gaps without fabricating external facts | Majid — Comprehensive Core Files Research Report |
| 2026-08-05 | 01_CORE.md, 02_LIBRARY.md | Operational Contract Expansion | Expanded the integrated control chain, phase transitions, freeze change requests, classification execution, coordination hand-off, feedback transfer, and lesson-transfer tests with Trigger/Input/Output/Approval/Next-State relationships | Convert framework headings into executable cross-system contracts | Majid — Expand Previous Systems and Correct Relationships |
| 2026-08-05 | PROJECT_INSTRUCTIONS.md, 01_CORE.md, 02_LIBRARY.md, README.md | Command Intent & Visual Handshake | Added command intent lexicon, textual operation direction, explicit production handshake, output-permission QA, visual operation handshake, and command validation examples | Prevent image/render/sheet escalation from analysis or design discussion | Majid — Explicit Command Behavior Requirement |
| 2026-08-11 | 01_CORE.md | Sections 01–38 (full file) | Populated the complete Intelligence Layer: thinking framework, decision engine, cognitive pipeline, project execution, intelligence architecture, communication, specialist system, quality control, knowledge evolution, governance, lifecycle, business, technical, digital workflow, presentation, project memory, AI generative design, documentation, material/cost, planning, landscape, interior, visualization, BIM, operating protocol, workspace, enhanced QC/business/evolution, startup, overlap resolution, maturity, visual identity (35.00–35.100), Iranian regulation, business intelligence, client communication | Complete the three-layer permanent intelligence architecture and resolve all forward references from 00_IDENTITY.md and 02_LIBRARY.md | Majid — 01 CORE full dictation |
| 2026-08-11 | 01_CORE.md | 39 | Added Core Evolution Patch v2.0: Visual Fidelity, Source Lock, Edit Integrity and Rendering Quality System (39.00-39.20) | Prevent redesign-on-edit, reference contamination, and cinematic drift across all projects | Majid — Core Evolution Patch v2.0 |
| 2026-08-11 | 00_IDENTITY.md | 04.03 | Added Foundational Operating Principles: Source Truth, Architectural Partner, Precision First | Identity-level anchor for the Core Evolution Patch | Majid — Core Evolution Patch v2.0 |
| 2026-08-11 | 02_LIBRARY.md | 04.05, 04.06 | Added System Improvement Note Register and Visual Failure Pattern Archive | Store failure patterns and improvement notes as knowledge, not as operating rules | Majid — Core Evolution Patch v2.0 |
| 2026-08-11 | PROJECT_INSTRUCTIONS.md | 01-10 | Restructured from instruction list to Project Operating Contract with 10 numbered modules: State Initialization, Source Authority, Decision State, Workflow Routing, Visual Task Contract, Edit Preservation, Output Permission, Quality Gate, Memory Update | Enforce state, lock, delta, and validation before any output reaches the Core | Majid — PROJECT_INSTRUCTIONS v2.0 |
