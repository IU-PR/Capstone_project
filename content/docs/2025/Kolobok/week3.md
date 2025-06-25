---
title: "Week 3"
---

# Week 3 Progress Report

## Executive Summary

In Week 3, the Kolobok team achieved major technical integration milestones while simultaneously pushing the boundaries of data engineering and model experimentation. The MVP is now operational for tread depth estimation and spike condition classification across both Telegram and web interfaces. Brand recognition, the third major component, is in active R&D, with promising results achieved using GPT-4o-mini.

This week also marked a shift in engineering philosophy — moving from static databases and hand-constructed logic to a more dynamic, learning-based system design. From synthetic dataset generation in Unity to CLAHE-enhanced unwrapping for OCR, we continuously prioritized robustness, real-world performance, and system modularity. Our architecture now accommodates user feedback and model corrections, reflecting a maturing product vision that emphasizes trust, usability, and ML-aided transparency.

---

## Feature Implementation

### End-to-End Flow

The core pipeline now works across both Telegram and web UI:
- User submits a photo (tread-side or sidewall)
- Backend authenticates and processes using deployed ML models
- Results include tread depth, spike count, and condition (brand OCR pending)
- Users may correct predictions manually (bot and site)

Only brand/model recognition is pending deployment. The LLM-based OCR pipeline is developed and tested but not yet integrated.

---

## OCR Research and Integration

### Investigation and Evaluation

The team explored and benchmarked six OCR pipelines, focusing on accuracy and preprocessing sensitivity. Models included:

- Tesseract (Google OCR)
- MMOCR (OpenMMLab) variants: DBNet++, PSENet, PANet, TextSnake
- GPT-4o-mini (OpenAI Vision Language Model)

Each was tested with raw images, polar unwrapping, and CLAHE enhancement.

### OCR Evaluation Results

| OCR Pipeline | Raw | Unwrapped | CLAHE |
|--------------|-----|-----------|--------|
| Tesseract | 4 | 9 | 8 |
| DBNet++ + ABINet | 6 | 10 | 15 |
| PSENet + ABINet | 5 | 11 | 14 |
| TextSnake + ABINet | 7 | 12 | 16 |
| PANet + ABINet | 3 | 8 | 9 |
| GPT-4o-mini | 37 | 45 | 45 |

GPT-4o-mini achieved perfect accuracy (45/45) on the benchmark using unwrapped CLAHE-enhanced images. It was selected for integration in Week 4.

---

## ML Pipeline Development

### Tread Depth Estimation

- Ensemble regression with Swin Transformer, DenseNet, ConvNeXt
- Unity-generated dataset used for pretraining and edge case augmentation
- MAE on test set: ~0.93 mm
- Augmentations: brightness, shadow, blur, perspective

### Spike Classification

- Binary classifier using ResNet-like CNN
- Dataset expanded with 6000+ bootstrapped samples
- Tires without spikes used for hard negatives
- Final FP + FN on test set: ~7.5

---

## Model Architecture and Configuration

### Regression Model
- Loss: MSE + MAE monitoring
- Optimizer: AdamW
- LR Scheduler: CosineAnnealingLR
- Batch size: 16
- Epochs: 40

### Spike Classification
- Loss: CrossEntropy + hard-negative mining
- Augmentations: crop, rotate, CLAHE

### Logging
- TensorBoard: MAE trends, misclassified visualizations, histograms
- Checkpointing: per-epoch with val metrics

---

## Experimental Insights

| Experiment | Finding | Outcome |
|------------|---------|---------|
| CLAHE vs HE | CLAHE outperformed consistently | Standardized CLAHE |
| Hard negatives | Reduced false positives by ~20% | Included in training |
| GPT OCR vs MMOCR | GPT superior on real-world samples | Adopted GPT-4o-mini |
| Ensemble vs single model | 0.2mm better MAE | Final model is stacked ensemble |
| Unwrapping for OCR | Boosted recognition by 3× | Pipeline requirement |

---

## API, Bot, and Web UI

### Backend (FastAPI)
- Auth: Bearer token
- Endpoints: `/analyze/tread`, `/identify_tire`
- Error codes: 400 (bad image), 401 (auth), 422 (model failure)

### Telegram Bot
- Cancel button
- Manual correction of predictions
- Robust fallback logic and state handling

### Web Interface
- Functional MVP with drag-and-drop upload
- Connects to same API backend
- Design aligns with Telegram UX

---

## Data Handling & Privacy

- No user data stored
- Brand/model database replaced by GPT queries
- Only temporary logs used for diagnostics

---

## Testing and Feedback

| Issue | Fix |
|-------|-----|
| Spike false positives | Added negative tire images |
| Lighting sensitivity | Unity-based shadow samples |
| OCR failures | Switched to GPT-4o-mini |
| User confusion | Improved error messages, cancel paths |

---

## Roadmap

- Integrate GPT-based OCR into full pipeline
- Conduct small user study (10 users)
- Add admin dashboard for request analysis
- Finalize dataset with versioning and backups
- Fine-tune depth model using correction feedback

---

## Lessons Learned

- Real-world variance must drive training strategy
- ML + UX = user trust
- LLMs simplify pipelines previously requiring deep tuning
- Good error design prevents user frustration

## Team Contributions

| Team Member | Contributions |
|-------------|---------------|
| **Nikita Menshikov** | Wrote the report, set direction, brainstormed dataset improvements |
| **Nikita Zagainov** | Built ML pipeline, stacked models, refactored training code |
| **Dmitry Tetkin** | Modeled synthetic tires in Unity, expanded training data |
| **Vladislav Strelkov** | Developed web backend, refined deployment scripts |
| **Darya Stepanova** | Designed and tested web UI, UX improvements based on feedback |
| **Sergey Aitov** | Integrated bot ↔ API ↔ model, stabilized backend responses |
| **Ekaterina Petrova** | Created web frontend, tested dataset loading, maintained repo hygiene |

---

## Confirmation of Code Operability

- ✅ Code compiles and runs
- ✅ Code deploys via docker-compose (as per README.md)
