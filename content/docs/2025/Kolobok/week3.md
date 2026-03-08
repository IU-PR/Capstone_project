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

- Ensemble regression with Swin Transformer, DenseNet, ConvNeXt (in development)
- Unity-generated dataset used for pretraining and edge case augmentation
- MAE on test set: ~0.6 mm
- Augmentations: rotations, crops

### Spike Classification

- Binary classifier using ResNet-like CNN
- Dataset expanded with 6000+ bootstrapped samples
- Tires without spikes used for hard negatives
- Final FP + FN on test set: 10

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
- Error codes: 400 (bad image), 401 (auth)

### Telegram Bot
- Manual correction of predictions
- Robust state handling

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
| **Nikita Menshikov** | Wrote the report, set [tasks](https://github.com/orgs/IU-Capstone-Project-2025/projects/9), pitched dataset augmentation techniques, setup labelling for new spikes dataset |
| **Nikita Zagainov** | Conducted OCR [research](https://github.com/IU-Capstone-Project-2025/Kolobok/blob/ed78b4e0b0b67be7354dd563dff40f31b930f34a/ML/research/ocr_research/main.pdf) for brand and parameter recognition, built tire segmentator ([1](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/7e1d76340241c2b0d7eae70280ae11b379062aeb), [2](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/bcc83732147af72a135a84e0081dd4a582900dd9), [3](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/5e3cecfc353964a78755964403c2ceb53065b0cc)) |
| **Dmitry Tetkin** | [Modeled](https://github.com/IU-Capstone-Project-2025/Kolobok/blob/9d6bb4c74b963ff3a24c0d905d55409a1d611338/TireDataset/Assets/Report/SyntheticDatasetReport.pdf) synthetic tires in [Unity](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/630504b7e7c95a6aa170bd7cd5975c615b8d6a0e), expanded training data |
| **Vladislav Strelkov** | Connected endpoints to [tg bot](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/d793d9c2fb92914455a948b099a3064ad265c0fa), refined user paths, enhanced it with functionality for the demo |
| **Darya Stepanova** | Developed the first version of site [frontend](https://www.figma.com/design/llkM7QUkBNkwm0pit8qUhn/KolobokBoard?node-id=5-2&t=C5HOXlHhL0asVBw2-1), basic [back](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/5337ae775e5aebe0b5c78d0287dedf40def59712) and [landing](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/f2849fdf6f740b934fdeb6c14302f839a1a3cb79) |
| **Sergey Aitov** | [Improved](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/cac19b9d3b80f2c2e5a04f4510201babbd4f99b8) spikes labelling by running pretrained model on it, implemented spikes counter ([1](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/0006e78fd1479492908f15dc8922d9221a5d435c), [2](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/63431f9bfcd3c9bec4a53c665e4f9c81b52f6194))|
| **Ekaterina Petrova** | Performed research on tire [thread depth](https://github.com/IU-Capstone-Project-2025/Kolobok/blob/032ee4c674269be130f41fff3f2107ef410912ab/ML/research/thread_depth_research/main.pdf) and implemented a [module](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/d961ab52291b071812d864540a5ebd1f6d3aa337) |

---

## Confirmation of the code's operability
We confirm that the code in the main branch:
- [x] In working condition
- [x] Run via method described in README.md
