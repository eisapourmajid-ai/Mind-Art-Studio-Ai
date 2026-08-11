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
| 2026-08-11 | PROJECT_INSTRUCTIONS.md | 01-10 | Rebuilt as v3.0 Project Operating Contract: 12-state workflow machine, 5-step source conflict resolution, Edit Preservation A/B/C classification, output permission gate, ARCH VIZ quality fence | Scope PROJECT_INSTRUCTIONS to routing, behavior and permission only; move all new rules to 01_CORE.md | Majid — DR-25 |
| 2026-08-11 | 01_CORE.md | 40 | Added Knowledge Foundation Governance (40.00-40.11): Golden Rule, Knowledge Validation Record, Data Validity States, Undefined Is a Valid Value, Example Is Not Standard, Tool Is Not Standard, Failure Knowledge Record, System Change Record, File Responsibility Boundary, Knowledge Maturity Gate K0-K3 | Govern the data layer before populating it; prevent assumption entering the system as knowledge | Majid — Data Foundation Build |
| 2026-08-11 | 01_CORE.md | 12.09 | Added bilingual heading rule: Persian gloss permitted on headings as a reading aid, English text governs | Resolve Persian-content policy without weakening English-only core rule | Majid — DR-26 |
| 2026-08-11 | 01_CORE.md | 16.02, 35.79 | Relabelled MA24 file-naming examples as Example Reference Only | Prevent an illustrative project code being treated as a declared studio convention | Majid — DR-13 |
| 2026-08-11 | 00_IDENTITY.md | 04.04 | Added Studio Identity Database (04.04.01-04.04.08): Studio Profile, Scale, Service Architecture, Design Specialization, Geographic Identity, Declared Philosophy, Declared Language, Behavior Under Undefined Identity | Give identity a data structure; every field ships as Undefined rather than assumed | Majid — Data Foundation Build M01 |
| 2026-08-11 | 00_IDENTITY.md | 07.06 | Added Visual Identity Data Records: Typography Record, Brand Color Record | Register typography and brand colour as pending studio decisions, not invented values | Majid — Data Foundation Build M06 |
| 2026-08-11 | 00_IDENTITY.md | 09–16 | Added Studio Reality Layer: 09 Studio Reality Profile, 10 Design Intelligence, 11 Material DNA, 12 Visualization DNA, 13 Presentation DNA, 14 Decision Personality, 15 Learning Memory, 16 Identity Governance. Consolidated 04.04 and 07.06 into 09 and 13, retaining both as pointers | Extend identity with the studio's ground-truth reality layer without rewriting Sections 01–08; remove record duplication | Majid — Identity Data Extension v1.0 · Core Systemic Update |
| 2026-08-11 | 01_CORE.md | 41 | Added Operational Decision Engine: source authority order, conflict protocol, architectural priority matrix, minimum option rule, design review protocol, observation/interpretation separation, confidence axes, realism priority, benchmark scoring, material decision engine, cost rule, decision record, assumption register, escalation, anti-generic rule, completion criteria, failure modes | Add the decision-resolution layer as an extension; renumbered from Majid's proposed 36 because 36 is occupied by the Iranian Regulatory Intelligence Engine | Majid — Operational Decision Engine v2.0 · Core Systemic Update |
| 2026-08-11 | 02_LIBRARY.md | 11–23 | Added Sections 11 Typology, 12 Site and Orientation, 13 Cost, 14 Client, 15 Software and Tool, 16 AI Production, 17 Sustainability, 18 Project Lesson, 19 Presentation and Publication, 20 Competition, 21 Studio Practice, 22 Knowledge Gap Register, 23 Knowledge Integrity Rules | Extend the existing knowledge architecture rather than replacing it; Majid's proposed 00–32 renumbering was rejected because Sections 03, 04 and 05 carry 18 inbound references | Majid — Library Intelligence Expansion v2.0 · Core Systemic Update |
| 2026-08-11 | 02_LIBRARY.md | 06, 07 | Added Local Context Intelligence Database (four Mazandaran locations registered empty) and Material Intelligence Database with admission gate | Structure for context and material knowledge, with provenance required before use | Majid — Data Foundation Build M02, M03 |
| 2026-08-11 | 02_LIBRARY.md | 08, 09, 10 | Added Regulation/Dimension/Benchmark Databases, Visualization Knowledge Database with numeric lighting profiles and capability-based tool records, and Failure Knowledge Database | Satisfy 01_CORE.md 40.07 reference; enforce versioned regulations, paired benchmarks, numeric lighting, and tool-as-capability | Majid — Data Foundation Build M04, M05, M07, M08, M09, M11 |
| 2026-08-11 | INTAKE_LOG.md, docs/DEVELOPMENT_GOVERNANCE.md, LICENSE | ALL | Refreshed intake log as a placement ledger, published governance documentation, added MIT LICENSE file | Correct three stale or missing repository facts | Majid — DR-27 |

---

## 06 — Local Context Intelligence Database

> Verified place data. This is the difference between a general architecture AI and a studio AI: a recommendation that knows its climate, its risks, and its local construction reality.
>
> Admission is governed by `01_CORE.md` Section 40. Every field is `Undefined` until Majid supplies a verified value. Section 03.07 defines the collection protocol; this section stores the results.

### 06.01 — Location Record Schema

```yaml
LOCATION_PROFILE:
  Location_ID:            LOC-<CITY>-<NNN>
  City:
  Province:
  Country:
  Climate_Type:
  Geographical_Context:
  Urban_Context:
  Topography:
  Population_Context:
  Development_Pattern:
  Validation:             See 01_CORE.md 40.02
```

### 06.02 — Climate Record Schema

```yaml
CLIMATE_PROFILE:
  Location_ID:
  Temperature:            Seasonal range, with source
  Humidity:               Annual profile, not a single figure
  Rainfall:               Volume and seasonal distribution
  Solar_Condition:        Orientation consequences, cloud cover
  Wind:                   Prevailing direction, seasonal intensity
  Seasonal_Risks:
  Environmental_Challenges:
  Data_Source:            Meteorological authority and period
  Validation:
```

**Rule:** Climate figures require a named source and a measurement period. A remembered impression of a climate is `ASSUMED`, never `VERIFIED`.

### 06.03 — Regional Risk Record Schema

```yaml
RISK_PROFILE:
  Location_ID:
  Humidity_Risk:
  Corrosion_Risk:
  Water_Infiltration:
  Biological_Growth:
  Material_Aging:
  Maintenance_Challenges:
  Construction_Risks:
  Observed_Evidence:      Project, building, or documented case
  Validation:
```

### 06.04 — Design Implication Record Schema

Risks become design guidance only through an explicit implication record. A risk list is not a strategy.

```yaml
DESIGN_IMPLICATIONS:
  Location_ID:
  Facade_Strategy:
  Material_Strategy:
  Ventilation_Strategy:
  Shading_Strategy:
  Landscape_Strategy:
  Maintenance_Strategy:
  Rejected_Solutions:     What has failed locally, and why
  Validation:
```

`Rejected_Solutions` is as valuable as the recommendations. A locally failed solution that is not recorded will be proposed again.

### 06.05 — Registered Locations

Priority order for population, as directed: Babolsar, Babol, Ghaemshahr, Sari, then future target cities.

| Location ID | City | Province | Climate record | Risk record | Implications | State |
|-------------|------|----------|----------------|-------------|--------------|-------|
| LOC-BABOLSAR-001 | Babolsar | Mazandaran | Undefined | Undefined | Undefined | `Undefined` |
| LOC-BABOL-001 | Babol | Mazandaran | Undefined | Undefined | Undefined | `Undefined` |
| LOC-GHAEMSHAHR-001 | Ghaemshahr | Mazandaran | Undefined | Undefined | Undefined | `Undefined` |
| LOC-SARI-001 | Sari | Mazandaran | Undefined | Undefined | Undefined | `Undefined` |

**Note on Mazandaran:** High humidity, heavy rainfall, biological growth, metal corrosion, shading importance, natural ventilation, and durable coating selection are the expected subject areas for these records. They are listed here as the **collection agenda**, not as recorded findings. No figure or recommendation enters the table above without a source.

---

## 07 — Material Intelligence Database

> The system currently reasons well about materials but has no material to select from. This database closes that gap.
>
> One record per material. A material is admitted only with its climate behavior and its failure modes; a record listing only advantages is incomplete and is not admitted.

### 07.01 — Material Identity Schema

```yaml
MATERIAL_RECORD:
  Material_ID:      MAT-<CATEGORY>-<NNN>
  Name:
  Category:
  Sub_Category:
  Manufacturer:
  Origin:
  Application:
  Local_Availability:
  Cost_Level:
  Validation:
```

### 07.02 — Technical Properties Schema

```yaml
TECHNICAL_PROPERTIES:
  Material_ID:
  Durability:
  Water_Resistance:
  UV_Resistance:
  Thermal_Behavior:
  Fire_Behavior:
  Acoustic_Behavior:
  Maintenance_Level:
  Data_Source:      Manufacturer, standard, or studio observation
  Validation:
```

Manufacturer performance claims are recorded as `PARTIALLY VERIFIED` until confirmed by a standard or studio experience.

### 07.03 — Climate Compatibility Schema

```yaml
CLIMATE_RESPONSE:
  Material_ID:
  Suitable_Climate:
  Unsuitable_Climate:
  Humidity_Performance:
  Salt_Air_Performance:
  Aging_Behavior:
  Cleaning_Requirement:
  Evidence:             Observed case or documented source
  Validation:
```

### 07.04 — Visual Character Schema

```yaml
VISUAL_CHARACTER:
  Material_ID:
  Texture:
  Color_Range:
  Light_Response:
  Reflection:
  Perceived_Quality:
  Architectural_Message:
  Reference_Images:       Benchmark IDs from Section 08
  Validation:
```

This record feeds visualization directly. Material realism under `01_CORE.md` 39.08 depends on these values being real rather than imagined.

### 07.05 — Application Rules Schema

```yaml
APPLICATION_RULES:
  Material_ID:
  Recommended_Usage:
  Avoided_Usage:
  Combination_With:
  Detailing_Requirements:
  Construction_Notes:
  Known_Failures:           Linked FAILURE_RECORD IDs
  Validation:
```

### 07.06 — Material Register

| Material ID | Name | Category | Application | Climate suitability | State |
|-------------|------|----------|-------------|---------------------|-------|
| — | — | — | — | — | Register empty — awaiting Majid |

**Category namespace** (identifier structure only, not a recorded inventory): `MAT-STONE`, `MAT-CONCRETE`, `MAT-METAL`, `MAT-WOOD`, `MAT-GLASS`, `MAT-CERAMIC`, `MAT-COMPOSITE`, `MAT-COATING`, `MAT-INSULATION`.

**Admission gate:** A material enters the register only when 07.01, 07.03, and 07.05 are populated. Technical properties and visual character may follow. A material with no recorded failure mode or limitation is treated as an incomplete record.

---

## 08 — Regulation, Dimension and Benchmark Databases

> Three verification-critical databases. Each carries a stricter admission gate than general knowledge, because an error here becomes a legal, safety, or quality failure rather than an aesthetic one.

### 08.01 — Regulation Record Schema

The system must never claim to "know the national building code". It knows specific, versioned, sourced records.

```yaml
REGULATION:
  Regulation_ID:        REG-<COUNTRY>-<CODE>-<NN>
  Name:
  Category:
  Authority:
  Edition:
  Year:
  Region:
  Scope:
  Applicable_Projects:
  Verification_Status:
  Source:               Document reference or official link
```

**Status vocabulary:** `Verified` · `Needs Verification` · `Archived` · `Superseded`.

**Absolute rule:** A regulation record without `Edition`, `Year`, `Authority`, and `Source` is `Needs Verification` and may never support a compliance statement. No legal conclusion is ever drawn from this Library alone; see Section 02.01.

### 08.02 — Regulation Application Schema

```yaml
REGULATION_APPLICATION:
  Regulation_ID:
  Building_Type:
  Relevant_Stage:
  Design_Impact:
  Checking_Method:
  Responsible_Role:
```

### 08.03 — Municipal Rule Schema

Municipal rules are jurisdiction-bound and are never generalized between cities.

```yaml
LOCAL_REGULATION:
  Location_ID:              Links to Section 06
  City:
  Authority:
  Document_Name:
  Building_Height_Rules:
  Setback_Rules:
  Density:
  Parking_Rules:
  Facade_Rules:
  Special_Limitations:
  Verification_Date:
  Source:
```

**Expiry rule:** A municipal record older than its `Verification_Date` review cycle drops to `Needs Verification` automatically. Local planning interpretation changes faster than national code.

### 08.04 — Regulation Register

| Regulation ID | Name | Authority | Edition | Year | Status |
|---------------|------|-----------|---------|------|--------|
| — | — | — | — | — | Register empty — awaiting Majid |

Population target: the 22 official Mabahes referenced in Section 02.01, each as an individual record with its own edition and year. Until then, Section 02.01's warning governs.

### 08.05 — Dimension Standard Schema

```yaml
DIMENSION:
  Element:
  Building_Type:
  Minimum:
  Recommended:
  Maximum:
  Reference:            Standard, code, or studio practice
  Climate:
  Notes:
  Validation:
```

A dimension without `Reference` is a professional assumption and is labelled as such in every output, per Section 02.04.

### 08.06 — Dimension Categories

Collection agenda, not recorded values:

| Group | Elements |
|-------|----------|
| Residential | Living, bedroom, kitchen, bathroom, corridor, stair, balcony, parking |
| Public | Lobby, hall, service, accessibility |
| Interior | Furniture clearance, lighting distance, ergonomic standards |

### 08.07 — Visual Benchmark Schema

Quality assurance without a benchmark is opinion. Each category requires at least one approved and one rejected example before its QA criteria are considered operational.

```yaml
BENCHMARK:
  Benchmark_ID:         BM-<CATEGORY>-<NNN>
  Category:
  Image:                Path or reference
  Status:               Approved / Rejected / Diagnostic
  Why_Approved:
  Why_Rejected:
  Learning_Point:
  Applicable_Project:
  Rights_Status:
  Validation:
```

This schema is the operational form of the template in Section 03.04 and uses the same category set.

### 08.08 — Benchmark Coverage Register

| Category | Approved example | Rejected example | Coverage |
|----------|------------------|------------------|----------|
| Architecture | Undefined | Undefined | `Undefined` |
| Facade | Undefined | Undefined | `Undefined` |
| Interior | Undefined | Undefined | `Undefined` |
| Material | Undefined | Undefined | `Undefined` |
| Glass | Undefined | Undefined | `Undefined` |
| Lighting | Undefined | Undefined | `Undefined` |
| Landscape | Undefined | Undefined | `Undefined` |
| Presentation | Undefined | Undefined | `Undefined` |

**Illustrative pairing** (`Example Reference Only`, per `01_CORE.md` 40.05): for Glass, an approved example shows clear glazing with controlled reflection; a rejected example shows artificial blue mirror glazing. This illustrates the *pairing method*; it is not a recorded benchmark.

---

## 09 — Visualization Knowledge Database

> Converts visual intent into recorded, reproducible parameters. `01_CORE.md` Section 39 defines the quality rules; this section stores the values those rules operate on.

### 09.01 — Lighting Profile Schema

A named atmosphere is not a specification. "Golden hour" is a feeling; a lighting profile is a set of values that reproduces it.

```yaml
LIGHT_PROFILE:
  Profile_ID:           LP-<NNN>
  Name:
  Type:
  Sun_Position:         Angle above horizon
  Time:
  Color_Temperature:    Kelvin
  Sky_Model:
  Shadow_Character:
  Contrast:
  Exposure:             EV
  Application:
  Validation:
```

**Rule:** A lighting instruction referencing a named mood without a profile record is incomplete. The system requests the profile or states the values it is assuming.

### 09.02 — Lighting Profile Register

| Profile ID | Name | Sun position | Temperature | Contrast | Shadow | State |
|------------|------|--------------|-------------|----------|--------|-------|
| — | — | — | — | — | — | Register empty — awaiting Majid |

### 09.03 — Production Pipeline Schema

```yaml
VISUAL_PIPELINE:
  Modeling:
  Rendering:
  Post_Process:
  AI_Enhancement:
  Presentation:
  Archive:
  File_Exchange_Standard:
```

### 09.04 — Rendering Capability Record

Recorded as a capability, never as a product commitment; see `01_CORE.md` 40.06.

```yaml
RENDER_CAPABILITY:
  Capability_Required:      e.g. physically based path-traced rendering
  Geometry_Accuracy:
  Material_Accuracy:
  Lighting_Accuracy:
  Camera_Accuracy:
  Atmosphere:
  Resolution:
  Quality_Level:
  Approved_Tools:
  Version_In_Use:
  Review_Date:
```

### 09.05 — Visual Production Stack Register

| Role | Capability requirement | Approved tool | Version | State |
|------|------------------------|---------------|---------|-------|
| Primary render engine | Undefined | Undefined | Undefined | `Undefined` |
| Secondary engine | Undefined | Undefined | Undefined | `Undefined` |
| 3D software | Undefined | Undefined | Undefined | `Undefined` |
| AI tools | Undefined | Undefined | Undefined | `Undefined` |
| Image processing | Undefined | Undefined | Undefined | `Undefined` |

The general tool map in `01_CORE.md` 16.02 states tool *roles*. This register records the studio's actual confirmed tools and versions.

---

## 10 — Failure Knowledge Database

> Error experience is an asset. A failure that is not recorded is a failure that will repeat.
>
> Schema and governance: `01_CORE.md` 40.07. This section stores the records. Section 04.06 holds the visual failure *patterns* observed across projects; this section holds *individual incidents* with their causes and controls.

### 10.01 — Failure Record Schema

```yaml
FAILURE_RECORD:
  ID:           FAIL-<DOMAIN>-<NNN>
  Category:
  Problem:      What actually happened
  Cause:        Why it happened
  Impact:       Design, technical, schedule, or client impact
  Prevention:   The control that stops recurrence
  Future_Rule:  Proposed permanent rule, or None
  Date:
  Validation:
```

**Domain codes:** `VIS` visualization · `GEO` geometry and source · `REG` regulation · `MAT` material · `COM` communication · `PRO` process · `SYS` system and data.

### 10.02 — Failure Register

| ID | Category | Problem | Cause | Prevention | Future rule |
|----|----------|---------|-------|------------|-------------|
| FAIL-VIS-001 | Image editing | AI changed building geometry during an edit | Missing source lock before production | Activate Edit Preservation Mode | Implemented — `01_CORE.md` 39.03, 39.05 |

**Register state:** One record, supplied by Majid. The thirteen entries in Section 04.06 are generalized patterns derived from observation, not incident records, and are intentionally kept separate.

### 10.03 — Failure to Rule Promotion

A failure record does not become a rule by existing. Promotion requires:

1. The cause is systemic, not a one-off circumstance.
2. The preventive control is testable.
3. The rule does not duplicate an existing rule in `01_CORE.md`.
4. Majid approves it through the workflow in `01_CORE.md` Section 12.

Until all four conditions are met, `Future_Rule` remains a proposal and the system does not act on it as policy.

---

## 11 — Typology Intelligence

> What the studio has learned about building types. Each record is generalizable knowledge extracted from projects, never a description of one project.

### 11.01 — Typology Record Schema

```yaml
TYPOLOGY_RECORD:
  Typology_ID:            TYP-NNN
  Name:
  Typical_Program:
  Critical_Dimensions:
  Common_Constraints:
  Frequent_Mistakes:
  Success_Factors:
  Regulatory_Sensitivities:
  Source:
  Verification_Status:
  Confidence:
  Record_State:
```

### 11.02 — Typology Register

*(Empty. Records are admitted only from completed studio projects or named professional sources.)*

| Typology ID | Name | Verification | Confidence |
|-------------|------|--------------|------------|
| — | — | — | — |

### 11.03 — Admission Rule

A typology record requires evidence from at least two projects, or one named professional source. A single project produces a project lesson in Section 04, not a typology rule.

---

## 12 — Site and Orientation Intelligence

> Generalizable site reasoning. Specific locations belong to Section 06.

### 12.01 — Site Analysis Record Schema

```yaml
SITE_PATTERN:
  Pattern_ID:             SITE-NNN
  Condition:
  Implication:
  Design_Response:
  Evidence:
  Source:
  Verification_Status:
  Confidence:
  Record_State:
```

### 12.02 — Orientation Principles

*(Empty. No orientation rule is recorded without a climate source and a named region; a general rule stated without those is an assumption.)*

### 12.03 — Boundary With Section 06

| Question | Section |
|----------|---------|
| What is true of this specific city or site? | 06 |
| What is true of this *kind* of site condition? | 12 |

---

## 13 — Cost Intelligence

> Cost knowledge with mandatory provenance. Governed by `01_CORE.md` 41.12.

### 13.01 — Cost Record Schema

```yaml
COST_RECORD:
  Cost_ID:                COST-NNN
  Item:
  Scope:
  Unit:
  Amount:
  Currency:
  Location:
  Date:
  Source:
  Verification_Status:
  Confidence:
  Expiry:
  Record_State:
```

### 13.02 — Mandatory Fields

`Location` · `Date` · `Scope` · `Source`. A record missing any of the four cannot be admitted and cannot be quoted.

### 13.03 — Expiry Rule

Cost data carries an expiry date. Past expiry the record moves to `ARCHIVED` and may be cited only as historical context, never as a current price. In a high-inflation economy an unexpired date is the only thing separating a price from a fiction.

### 13.04 — Cost Register

*(Empty. No price is recorded from memory, estimate, or inference.)*

---

## 14 — Client Intelligence

> Patterns in client behavior, recorded without identifying anyone. Confidential client information is explicitly outside this file's responsibility.

### 14.01 — Client Pattern Schema

```yaml
CLIENT_PATTERN:
  Pattern_ID:             CLI-NNN
  Observed_Behavior:
  Typical_Context:
  Studio_Response:
  Outcome:
  Source:
  Verification_Status:
  Record_State:
```

### 14.02 — Confidentiality Rule

No client name, no project address, no contract term, no fee, and no private communication is stored in this file. A pattern is recorded only in a form that cannot be traced to an individual client.

### 14.03 — Client Pattern Register

*(Empty.)*

---

## 15 — Software and Tool Intelligence

> Tools are recorded as tested capabilities with versions, never as identity. Governed by `01_CORE.md` 40.06.

### 15.01 — Tool Record Schema

```yaml
TOOL_RECORD:
  Tool_ID:                TOOL-NNN
  Name:
  Version:
  Category:
  Purpose:
  Tested:
  Test_Date:
  Strengths:
  Limitations:
  Studio_Status:
  Record_State:
```

**`Studio_Status`:** `Approved` · `Under Evaluation` · `Rejected` · `Deprecated`

### 15.02 — Tool Is Not Identity

The studio's identity records a *capability*, not a product: `Preferred Renderer: Physical path traced renderer`, plus the currently approved tool and version. A renderer name is never written as the studio's identity, because replacing the tool would then require changing who the studio is.

### 15.03 — No Untested Tool Rule

No AI tool, plugin, or renderer is recorded as approved without the studio having tested it. A tool's marketing claim is not evidence, and a tool that performs well in a demonstration has not been tested.

### 15.04 — Tool Register

*(Empty.)*

---

## 16 — AI Production Intelligence

> What the studio has learned about using AI in architectural production. This is knowledge about the method, not instructions to the system — the operating rules are in `01_CORE.md` Section 39.

### 16.01 — AI Behavior Pattern Schema

```yaml
AI_PATTERN:
  Pattern_ID:             AIP-NNN
  Observed_Behavior:
  Trigger:
  Consequence:
  Mitigation:
  Enforcing_Control:
  Source:
  Verification_Status:
  Record_State:
```

### 16.02 — Known AI Failure Tendencies

Recorded as observed knowledge. The controls that prevent them live in `01_CORE.md` Section 39; this register explains *why* those controls exist.

| Tendency | Consequence | Enforcing control |
|----------|-------------|-------------------|
| Treating an edit as an invitation to redesign | Geometry silently changes | 39.03 |
| Smoothing detail to increase apparent quality | Material and edge information lost | 39.17 |
| Importing form language from a reference | Design contaminated by precedent | 39.14 |
| Improving what was not requested | Scope creep in production | 39.04 |

### 16.03 — Prompt Knowledge Rule

A prompt that produced a good result once is an observation. It becomes studio knowledge only when it reproduces across projects. Prompt records carry the tool and version they were tested against, because a prompt is not portable between models.

---

## 17 — Sustainability Intelligence

> Environmental knowledge with sources. No performance figure is recorded without one.

### 17.01 — Sustainability Record Schema

```yaml
SUSTAINABILITY_RECORD:
  Record_ID:              SUS-NNN
  Topic:
  Claim:
  Metric:
  Value:
  Measurement_Standard:
  Climate_Zone:
  Source:
  Verification_Status:
  Confidence:
  Record_State:
```

### 17.02 — No Unsourced Performance Claim

U-values, energy figures, embodied carbon, and payback periods require a named standard and a source. A number that circulates widely is not thereby verified, and a manufacturer's figure is recorded as a manufacturer's figure.

### 17.03 — Sustainability Register

*(Empty.)*

---

## 18 — Project Lesson Intelligence

> The canonical learning schema for the system. Section 04.04 holds the operating lesson database; this section defines the structure and the promotion path that governs it.

### 18.01 — Lesson Record Schema

```yaml
LESSON:
  Lesson_ID:              LES-NNN
  Project:
  Observation:
  Problem:
  Decision:
  Result:
  Lesson:
  Future_Rule:
  Scope:
  Source:
  Verification_Status:
  Record_State:
```

### 18.02 — Scope Classification

| Scope | Meaning | Destination |
|-------|---------|-------------|
| `Project Specific` | True for this project only | Project record; never generalized |
| `Studio Practice` | The studio's habitual method | Section 21 |
| `Core Systemic` | Changes how the system reasons | Proposal to `01_CORE.md`, requires approval |

### 18.03 — Future Rule Is a Proposal

The `Future_Rule` field is a candidate, never an active rule. It becomes operative only when written into `01_CORE.md` with Majid's approval. A rule that exists only in a lesson record has not been adopted, and the system must not behave as though it has.

### 18.04 — Promotion Gate

A lesson is promoted to a rule when all four hold:

```text
01. The pattern has repeated, or Majid has confirmed the reasoning independently
02. The rule is generalizable beyond the originating project
03. It does not contradict an existing rule
04. Majid has approved it explicitly
```

---

## 19 — Presentation and Publication Intelligence

> What the studio has learned about presenting work. Execution standards are in `01_CORE.md` Section 35.

### 19.01 — Presentation Pattern Schema

```yaml
PRESENTATION_PATTERN:
  Pattern_ID:             PRE-NNN
  Context:
  Approach:
  Audience_Response:
  Effectiveness:
  Source:
  Verification_Status:
  Record_State:
```

### 19.02 — Narrative Structure

The studio's presentation narrative, recorded from `00_IDENTITY.md` 07.04:

```text
Problem → Idea → Process → Solution → Experience
```

This is recorded here as an observed studio method. It is applied as a standard through `01_CORE.md` Section 35.

### 19.03 — Publication Register

*(Empty. A published or submitted project is recorded with its venue, date, and outcome — including rejections, which carry more information than acceptances.)*

---

## 20 — Competition and Opportunity Intelligence

### 20.01 — Competition Record Schema

```yaml
COMPETITION_RECORD:
  Record_ID:              COMP-NNN
  Name:
  Organizer:
  Type:
  Scale:
  Outcome:
  Lessons:
  Rights_Status:
  Source:
  Verification_Status:
  Record_State:
```

### 20.02 — Rights and Legal Status

No competition, benchmark, or reference project is recorded without its rights status. An image the studio cannot legally reproduce is not an asset, and discovering that after publication is expensive.

### 20.03 — Competition Register

*(Empty.)*

---

## 21 — Studio Practice Register

> Habitual studio methods that are not yet system rules. The waiting room between a preference and a standard.

### 21.01 — Practice Record Schema

```yaml
PRACTICE:
  Practice_ID:            PRA-NNN
  Description:
  Origin:
  Frequency:
  Rationale:
  Promotion_Candidate:
  Record_State:
```

### 21.02 — Practice Is Not Rule

A practice recorded here describes what the studio *tends to do*. It does not bind the system. Applying a practice as if it were a rule is a violation of `01_CORE.md` 40.01, which requires Source, Reason, and Approval for every permanent rule.

### 21.03 — Practice Register

*(Empty.)*

---

## 22 — Knowledge Gap Register

> An explicit record of what the system does not know. A named gap is safer than an unnoticed one.

### 22.01 — Gap Record Schema

```yaml
KNOWLEDGE_GAP:
  Gap_ID:                 GAP-NNN
  Domain:
  Missing_Knowledge:
  Impact:
  Blocks:
  Resolution_Path:
  Priority:
  Record_State:
```

### 22.02 — Open Gaps

Derived from the current state of the knowledge base. Each blocks a capability the system must not claim.

| Gap ID | Domain | Missing knowledge | Blocks |
|--------|--------|-------------------|--------|
| GAP-001 | Studio identity | All fields in `00_IDENTITY.md` Section 09 | Any studio-specific statement |
| GAP-002 | Visual identity | Typeface and brand colour values | Reproducible presentation output |
| GAP-003 | Local context | Climate and site data for the four target cities | Context-specific design reasoning |
| GAP-004 | Regulation | The 22 Mabahes of the Iranian National Building Regulations | Any compliance statement |
| GAP-005 | Material | The material register is empty | Evidence-based material selection |
| GAP-006 | Benchmark | No benchmark records in any of the eight categories | Comparative quality assessment |
| GAP-007 | Cost | No cost records | Any price indication |

### 22.03 — Gap Honesty Rule

While a gap is open, the system states the limitation rather than working around it. Filling a gap with a plausible answer converts a known unknown into an unknown error, which is strictly worse.

---

## 23 — Knowledge Integrity Rules

> The governing constraints for everything in this file. Where this section and a record disagree, this section governs.

### 23.01 — The Golden Rule

```text
Never store preference as fact.
Never store example as standard.
Never store assumption as knowledge.
Every permanent rule must have Source + Reason + Approval.
```

### 23.02 — Never Guess to Fill the Library

The following are prohibited as library entries under all circumstances:

- An assumed font name
- An assumed HEX value
- An assumed regulation edition or year
- An assumed price
- An assumed product or manufacturer
- A climate figure without a source
- A benchmark without its legal and rights status
- An AI tool the studio has not tested
- A material chosen from render appearance alone
- A reference chosen only because it is beautiful

An empty field is a valid state. A fabricated field is a defect that propagates.

### 23.03 — Library Non-Responsibilities

This file does **not** contain:

- Main behavioral instructions
- System personality
- Routing logic
- Permission logic
- The main workflow
- Decisions about a current project
- Confidential client information
- Unverified assumptions presented as fact

Behavioral instruction lives in `PROJECT_INSTRUCTIONS.md`; reasoning lives in `01_CORE.md`; identity lives in `00_IDENTITY.md`.

### 23.04 — Deactivation, Not Deletion

`REJECTED` and `SUPERSEDED` records are retained and deactivated. A rejected record is not an available option and a superseded record is not active knowledge, unless Majid explicitly reactivates it. Retention prevents a rejected idea from being rediscovered and proposed again as if it were new.

### 23.05 — Verification and Confidence

Every record carries both `Verification_Status` and `Confidence`, per `01_CORE.md` 41.08. They are independent. A record may be `ASSUMED` with `HIGH` confidence, and it is still an assumption.

### 23.06 — Maturity Honesty

The knowledge maturity of this file is assessed against `01_CORE.md` 40.10: `K0 Generic` · `K1 Identified` · `K2 Contextual` · `K3 Operational`.

**Current assessment: K1 for most domains, K0 for location, material, cost, and benchmark.** The schemas exist; the knowledge does not yet. The system must represent itself at its actual maturity level and not at the level its structure implies.
