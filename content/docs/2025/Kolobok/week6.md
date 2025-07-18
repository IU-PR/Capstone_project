---
title: "Week 6"
---

# Week 6 Progress Report – Final Touches & Presentation Preparation  
---

## 1 Executive Summary  

Week 6 concluded the implementation phase and opened the release-preparation window.  
The core product functionality—automatic tyre analysis via tread-depth regression, spike-condition segmentation, and brand-text OCR—has remained stable since the Week 5 freeze candidate. This final sprint therefore emphasised four themes:

1. **Performance & Portability** – critical models were exported to ONNX, yielding up-to-10× CPU speed-ups (2 s → 0.3 s per inference) and lowering memory overhead;  
2. **UX Polish** – the Web application gained quick-action buttons, friendlier waiting dialogues, local chat-history persistence, and was re-deployed to Vercel for improved availability;  
3. **Synthetic-Data Pipeline Kick-off** – a Blender workflow capable of rendering tyres with programmatically varied tread depth produced its first sample set, seeding future augmentation;  
4. **Release Governance** – a dated code-freeze was declared, documentation targets enumerated, and a roadmap for slide-deck authoring plus live-demo logistics drafted.

The system now meets functional requirements and is locked for presentation, with only critical hot-fixes allowed until final defence.

---

## 2 Final-Week Technical Work  

### 2.1 Model Optimisation & Conversion  

| Model / Module                | Action this week                          | Resulting Runtime (CPU) | Speed-up | Notes                         |
|-------------------------------|-------------------------------------------|-------------------------|----------|------------------------------|
| **SegFormer spike-segmenter** | PyTorch → ONNX export & graph simplifier | 0.30 s / image          | ≈10×     | previous pure-PyTorch 2 s; precision unchanged |
| **Tyre Unwrapper v2**         | Re-trained SegFormer variant on mixed dataset; exported to ONNX | 0.45 s   | ≈8×      | IOU gain 5 pp on wheel-mounted tyres |


*Conversion process.* All exports use opset 17, validated with onnx-runtime 1.17.1. Batch-norm folding and constant-fold passes were applied via onnx-optimizer; the resulting artefacts live under `artifacts/onnx/`. Automated integrity tests confirm numerical parity (<1e-5 MSE) with the reference PyTorch graphs.

### 2.2 Web-Site Enhancements  

*Quick-action buttons.* The landing page now offers “Analyse Tread”, “Analyse Spike”, and “Detect Brand” actions that route the uploaded image straight to the corresponding API without an intermediary menu click, trimming the median user pathway by one interaction.

*Waiting dialogue.* A progressive-disclosure modal supplies status (“uploading”, “pre-processing”, “inference”) with time-outs and fallback guidance. This reduced observed early-abandon events during internal tests.

*Local-storage chat history.* User conversations (image thumbnails plus textual results) persist in `window.localStorage`. A newly-added toolbar icon allows clearing the cache, satisfying privacy feedback gathered in Week 5.

*Deployment.* The static React bundle and serverless proxy were re-deployed to **Vercel** (region fra1).

### 2.3 New Unwrapper Model & Dataset Expansion  

The earlier open-source tyre-ring detector lacked robustness when wheels were mounted or background clutter appeared. This week’s replacement:

* **Architecture** – SegFormer-B2 backbone with mixed-scale deformable-attention decoder;  
* **Training corpus** – 1 260 pre-labelled “bare” tyres plus 200 new wheel-mounted instances (manual correction after auto-label seeding);  
* **Augmentation** – random perspective warp, synthetic background compositing, Gaussian-noise injection;  
* **Metrics** – mIoU 91 % (old model 86 %);  
* **Inference** – ONNX FP32 on CPU 0.45 s median.

The improved mask regularity produces tighter ellipse-fitting, which in turn sharpens ROI cropping for downstream OCR.

### 2.4 Blender Variable-Depth Tyre Model  

*Pipeline overview.*

1. Vectorise a 2-D tread-pattern image;  
2. Extrude along normal to form height field;  
3. Parameterise depth δ ∈ [1 mm, 10 mm];  
4. Render colour pass (1024 × 1024) plus Z-buffer;  
5. Export depth in millimetres via normalised EXR.  

*Current status.* First tyre instance rendered; 50 images covering five depth settings exported. Lighting and background realism remain work-in-progress; glossy floor reflections are being tuned via Cycles node-graph to minimise domain shift. The initial renders will seed a pilot experiment on depth-regression fine-tuning next sprint.

---

## 3 Governance & Release Management  

### 3.1 Code-Freeze Declaration  

* Date / time: **28 July 2025 18:00 UTC+3**  
* Allowed post-freeze commits: P0 bug-fixes only, subject to double-review.  
* Branch protections: `main` requires CI green and two approvals; squash merges enforced.

### 3.2 Testing & Coverage (post-freeze)  

* Backend unit tests: 212 / 212 pass – 96 % statement coverage.  
* API integration: 64 scenarios pass; schema validation automated via `prance`.  
* Front-end Cypress: 34 tests pass; Lighthouse accessibility score 95 / 100.  
* Telegram-bot scripted flows: 15/15 pass.  
* Synthetic load: 50 parallel requests sustain 1.4 s p95 latency.

No critical defects surfaced; minor UI mis-alignment in Safari patched before tag `v1.0.0-release`.

---

## 5 Presentation Preparation  

*Slide deck.* Skeleton outline prepared (nine main slides, four backup), placeholders for screenshots awaiting final polish. Located at `docs/presentation/kolobok_final.pptx`.

*Speaker allocation.* Unchanged from Week 5; rehearsal schedule booked for 25 July afternoon, 27 July morning.

*Demo logistics.* Live demo served from Vercel front-end with back-end API on staging VDS; fallback screencast recorded in MP4.

---

## 7 Team Contributions  

| Member                   | Contribution Highlights                                                                      |
|--------------------------|----------------------------------------------------------------------------------------------|
| **Nikita Menshikov**     | Managed pipeline enhancement research; created advanced version of tire model; validated site deployment on Vercel; wrote report. |
| **Nikita Zagainov**      | Exported spike-segmenter and unwrapper to ONNX; benchmarked 10× CPU speed-up; updated API to expose confidence scores. |
| **Dmitry Tetkin**        | Implemented Blender tread-depth variability pipeline; produced first 50 synthetic samples; profiled Cycles lighting. |
| **Vladislav Strelkov**   | Hardened CI/CD around release tag; tested container startup with ONNX-runtime; published public Swagger docs. |
| **Sergey Aitov**         | Extended integration test suite to cover ONNX inference path; fixed rare null-pointer error on zero-spike images. |
| **Ekaterina Petrova**    | Added quick-action buttons, waiting dialogues, and local-storage chat cache; managed Vercel build/config. |
| **Darya Stepanova**      | Refined UI, enhanced usability through interactive elements and engagement management ([1](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/5033bf3d6e9960f1d50a952f69dbc3256fc16055), [2](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/e22026b9614cc735c30740e6ee7c6d6545249032)) |

---

## 8 Project Readiness Checklist  

The project is therefore ready for final rehearsal, stakeholder review, and subsequent public defence. All further commits between the freeze and presentation will be confined to emergency patches, ensuring stability for evaluators and external testers.
