---
title: "Week 3"
---

# Week 3 Progress Report

## Executive Summary

In Week 3, the Kolobok project reached a critical milestone: the full implementation of the two major user stories — tread depth estimation and spike condition analysis — through both Telegram bot and a newly designed web interface. Brand recognition, the third major component, is in active R&D, with promising results achieved using GPT-4o-mini.

The team responded to performance issues by building a synthetic dataset via Unity and bootstrapping thousands of new spike annotations. On the OCR side, several modern pipelines were evaluated, and GPT-based OCR emerged as a practical and highly accurate solution. Security, deployment, and UX were improved, and all core models are now integrated and responding in production-ready APIs.

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

- **Tesseract** (Google OCR)
- **MMOCR pipelines**:
  - DBNet++ + ABINet
  - PSENet + ABINet
  - TextSnake + ABINet
  - PANet + ABINet
- **GPT-4o-mini** (LLM-based OCR)

All MMOCR pipelines used ABINet for text recognition, isolating detection model impact. Input images were tested with:
- Raw images
- **Polar unwrapping** (flattening sidewall curvature)
- **CLAHE** (Contrast-Limited Adaptive Histogram Equalization)

### OCR Evaluation Results

Each tire image was annotated with 3 text fields (marking, brand, size). The team used lenient Levenshtein-ratio based matching for OCR and strict field-level accuracy for GPT-4o-mini.

| Pipeline | Raw | Polar Unwrapping | CLAHE |
|----------|-----|------------------|--------|
| Tesseract | 4/45 | 9/45 | 8/45 |
| DBNet++ + ABINet | 6 | 10 | 15 |
| PSENet + ABINet | 5 | 11 | 14 |
| **TextSnake + ABINet** | 7 | 12 | 16 |
| PANet + ABINet | 3 | 8 | 9 |
| **GPT-4o-mini** | 37 | **45** | **45** |

### Decision

The team selected **GPT-4o-mini + Polar Unwrapping + CLAHE** as the future OCR pipeline, pending integration. MMOCR-based options remain viable if vendor-free models are later required.

---

## ML Model Development

### Pipeline Progress

The ML team finalized the MVP training pipeline with major enhancements:

- **Tread Depth**:
  - Regression models using CNN backbones and ensemble stacking
  - Synthetic dataset generated via Unity with various tread patterns and angles
- **Spike Quality**:
  - New dataset of over 6000 samples bootstrapped using a pretrained model
  - Included negative samples from tires with no spikes to reduce false positives

### Accuracy Metrics

| Task | Model Type | Dataset Source | Metric | Value |
|------|------------|----------------|--------|-------|
| Tread Depth | CNN + Ensemble | Real + Synthetic (Unity) | MAE | ~0.93 mm |
| Spike Condition | CNN classifier | Bootstrapped dataset | FP + FN | ~7.5 on test set |
| OCR (brand) | GPT-4o-mini | 15 real photos | Text field accuracy | 45/45 |

### Improvements

- Introduced **manual correction hooks** in bot and site
- All models refactored into callable Python packages (no more notebooks)
- Preprocessing pipeline unified across models

---

## Deployment and Integration

### Backend & API

- FastAPI backend fully connected to models and Telegram bot
- No new endpoints, but final logic and error handling now in place
- Bearer token auth prevents misuse
- Custom error messages and graceful model fallbacks implemented

### Telegram Bot Enhancements

- “Cancel” functionality added mid-conversation
- Correction interface for users to fix prediction
- Refined feedback messages for low-quality input

### Web Platform

- Frontend and backend for web platform completed
- Design tested and iterated on after team demo
- UX now mirrors Telegram workflow with added usability for uploads

---

## Data Handling and Ethics

- No persistent user data saved (privacy-first policy)
- Previous brand DB approach abandoned in favor of LLM
- All information flows transiently through logs and in-memory structures

---

## Internal Testing and Demos

A team-wide test session revealed:
- **Lighting variation** still harms model accuracy
- **Tread textures and stones** reduce spike classification accuracy
- UX improved based on flow interruption and user correction needs

---

## Team Contributions

| Team Member | Contributions |
|-------------|---------------|
| **Nikita Menshikov** | Authored the report, managed Kanban and discussions on dataset enrichment |
| **Nikita Zagainov** | Developed final training pipeline, added stacking, helped refactor ML modules |
| **Dmitry Tetkin** | Created synthetic tire tread dataset using Unity environment |
| **Vladislav Strelkov** | Built the backend for the web platform, updated Docker deployment |
| **Darya Stepanova** | Designed and refined UX for the web interface, adjusted flows after testing |
| **Sergey Aitov** | Connected all endpoints, refactored model codebase, backend utilities |
| **Ekaterina Petrova** | Implemented the web frontend, maintained datasets, wrote test scripts |

---

## Confirmation of the Code's Operability

We confirm that all code in the main branch:

- [x] Compiles and runs without errors
- [x] Deploys successfully via docker-compose (as per README)
- [x] Has integrated inference pipeline for tread + spike via bot and web

