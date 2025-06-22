---
title: "Week 3"
---

# Week 3 Progress Report

## Executive Summary

In Week 3, the Kolobok project reached a critical milestone: the full implementation of the two major user stories — tread depth estimation and spike condition analysis — through both Telegram bot and newly designed web interface. While brand recognition is still in progress, we’ve significantly expanded our dataset, enhanced model robustness using synthetic and bootstrapped data, and finalized the full backend-frontend-model integration pipeline.

The team also addressed real-world challenges with data variance, particularly in spike detection and lighting inconsistencies, by collecting 6000+ new images and building a synthetic Unity-based tread depth dataset. In parallel, security and API reliability were improved via bearer token authorization and robust error handling.

This week's progress brings the MVP into a functional and testable state, setting us up for user testing and final polishing in the coming sprint.

---

## Feature Implementation

### System Integration Overview

All major components of the system are now operational and tightly integrated. When a user submits a photo (via Telegram or web interface), the following end-to-end flow executes:

- The backend decodes the image and authenticates the request
- The system processes the photo using ML models for tread depth and spike analysis
- Results are returned with model confidences and human-correctable options
- The user can accept or manually adjust the prediction

**Brand recognition** remains the only core feature not yet deployed; the team is transitioning its implementation from a static brand database to a more flexible, text-based approach using LLMs.

---

## Improvements & Challenges

### Addressing Real-World Issues

During testing, we observed the following major issues:

- **Spike detection** suffered from false positives caused by tread patterns and embedded stones.
- **Tread depth prediction** showed inconsistency in photos taken under poor lighting or unusual angles.

To combat these, we introduced two major dataset enrichment strategies:

1. **Bootstrapped Spike Dataset**:  
   - Used our pretrained model to semi-automatically detect spike candidates in 6000 images.
   - All detections were manually verified to build a high-precision annotated set.
   - In addition, we processed tire images with *no spikes*, automatically marking all detected regions as incorrect (hard negatives).

2. **Synthetic Depth Dataset from Unity**:  
   - We built a custom Unity environment to model tire treads with varying depths and angles.
   - Simulated backlighting and shadows helped replicate real-world photo variance.
   - These synthetic images improved model generalization, especially under edge cases.

---

## API and Integration Layer

### Endpoints and Communication

No new endpoints were added this week, but all existing endpoints were finalized and connected to both ML models and the user-facing Telegram bot. Key highlights include:

- **Security**: Bearer token authentication is now enforced across all endpoints.
- **Error Handling**:
  - Proper HTTP codes for all failure scenarios (e.g., invalid token = 401, malformed image = 400)
  - Graceful model fallbacks with informative messages
- **User Feedback**: Both frontend and bot support correcting model predictions

---

## User Interfaces: Telegram Bot and Web Platform

### Telegram Bot Updates

The Telegram bot received several critical UX upgrades:

- **Cancel Flow**: Users can now abort actions mid-process
- **Correction Loop**: Predictions are shown with options for manual override
- **User State Handling**: Improved robustness under unexpected input or skipped steps

### Web Interface Prototype

Given user feedback and the need for better image uploads, we prototyped a **web interface**:

- **Frontend**: Developed using lightweight React/HTML (details below)
- **Backend**: Same FastAPI endpoints reused seamlessly
- **Design**: Provided by UX designer with team-tested corrections

---

## ML Model Development

### Final MVP Pipeline

By Week 3, the MVP pipeline reached its final form:

- **Stacked ensemble for depth estimation** across multiple backbones (e.g., ViT, Swin Transformer, DenseNet)
- **Spike classification** refined via new dataset
- **Preprocessing**: Unified transforms, sidewall cropping, and dynamic normalization
- **Packaging**: All models converted from notebooks to callable Python modules

### Performance Summary

| Task | Metric | Current Performance |
|------|--------|---------------------|
| Tread Depth | MAE (mm) | ~0.93 on augmented test set |
| Spike Condition | FP + FN | ~7.5 on 400 image subset |
| Brand Detection | N/A | In progress (LLM + OCR pipeline) |

---

## Data Handling and Ethics

Despite building and using rich datasets, **no user data is stored** on the backend:

- No database setup required (post-switch from embedding DB to LLM)
- Logs are the only retained artifacts, used strictly for monitoring
- All user data is transient and cleared after inference

This design aligns with our internal privacy policy and reduces infrastructure complexity.

---

## Internal Testing and Demos

An internal MVP test was performed, yielding valuable insights:

- **Challenge**: Lighting variance remains a performance bottleneck for both depth and spike models
- **Adjustment**: Increased augmentation for shadows, rotation, and exposure
- **Result**: Improved test set generalization post-augmentation

Design and flow issues identified in the bot were addressed by adding clearer feedback and more fallback options.

---

## Deliverables

> 🔗 **GitHub PRs:** [placeholder]  
> 📦 **Model Training Notebook:** [placeholder]  
> 🧪 **API Documentation:** [placeholder]  
> 🌐 **Web UI Mockup:** [placeholder]  
> 📊 **Synthetic Dataset Samples:** [placeholder]  
> 📽️ **Demo Video or GIFs:** [placeholder]

---

## Team Contributions

| Team Member | Contributions |
|-------------|---------------|
| **Nikita Menshikov** | Wrote the weekly report, led discussions on dataset enrichment strategies, managed task flow via Kanban |
| **Nikita Zagainov** | Integrated all enrichment techniques into the training pipeline, experimented with stacking and finalized the full model package |
| **Dmitry Tetkin** | Built the Unity environment and generated a synthetic dataset for tread depth estimation |
| **Vladislav Strelkov** | Developed the backend API for the new web platform, made key changes to the deployment setup |
| **Darya Stepanova** | Designed the web interface and revised Telegram bot UX based on demo feedback |
| **Sergey Aitov** | Linked ML models to API endpoints and Telegram bot, helped convert training code into production-grade Python modules |
| **Ekaterina Petrova** | Wrote the frontend for the web interface, maintained the dataset post-enrichment, and implemented test routines |

---

## Confirmation of the Code's Operability

We confirm that all code in the main branch:

- [x] Compiles and runs without errors
- [x] Deploys successfully via docker-compose (as per README.md)