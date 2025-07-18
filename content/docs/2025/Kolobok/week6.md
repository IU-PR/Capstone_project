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
4. **Proxy Integration** – All outgoing requests are routed through TOR proxy network to avoid country-level blocks

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

### 3.1 Testing & Coverage (post-freeze)  

* Backend unit tests: 9 / 9 pass – 100 % statement coverage.  
* API integration: 6 scenarios pass.  
* Front-end Cypress: 34 tests pass; Lighthouse accessibility score 95 / 100.  
* Telegram-bot scripted flows: 3/3 pass.

--- 

## 4 TOR integration

* Added open-source `dperson/torproxy` container to docker-compose as a proxy
* Enabled routing all outgoing requests through proxy

*Result:* all VLM models from `openrouter.ai` are now available: no country-level blockages

---

## 5 Presentation Preparation  

*Slide deck.* Skeleton outline prepared (nine main slides, four backup), placeholders for screenshots awaiting final polish.

*Speaker allocation.* Unchanged from Week 5; rehearsal schedule booked for 25 July afternoon, 27 July morning.

*Demo logistics.* Live demo served from Vercel front-end with back-end API on staging VDS; fallback screencast recorded in MP4.

---

## 7 Team Contributions  

| Member                   | Contribution Highlights                                                                      |
|--------------------------|----------------------------------------------------------------------------------------------|
| **Nikita Menshikov**     | Managed pipeline enhancement research; created advanced version of tire model; validated site deployment on Vercel; wrote report. |
| **Nikita Zagainov**      | Led improvement patches development; added TOR [proxy](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/0b6b9538800ad3b4595997795f36cf7267539ad3) to access foreign models |
| **Dmitry Tetkin**        | [Implemented](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/25758a45a172de0de706a9664d87fb59698a20ed) new scene with more real light; produced 10k synthetic samples |
| **Vladislav Strelkov**   | [Converted](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/09f0072ccbf5ed6ac163d6a08ed3a56de5a0ef04) the most usage-intensive checkpoints to ONNX format; tested container startup with ONNX-runtime |
| **Sergey Aitov**         | Trained and incorporated new tire segmentation [model](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/7655888c94ee5fc4913c63e68abcb8feafbffe92) into pipeline |
| **Ekaterina Petrova**    | Trained and incorporated new tire unwrapper [model](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/d00e393b06f7373c2348ebd7d1eb1fcdb1419c83) into pipeline |
| **Darya Stepanova**      | Refined UI, enhanced usability through interactive elements and engagement management ([1](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/5033bf3d6e9960f1d50a952f69dbc3256fc16055), [2](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/e22026b9614cc735c30740e6ee7c6d6545249032)) |

---

## 8 Project Readiness Checklist  

The project is therefore ready for final rehearsal, stakeholder review, and subsequent public defence. All further commits between the freeze and presentation will be confined to emergency patches, ensuring stability for evaluators and external testers.
