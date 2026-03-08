---
title: "Week 4"
---

# Week 4 Progress Report: Testing, CI/CD & Deployment Setup

## Executive Summary

This week focused on hardening our system for deployment by implementing comprehensive testing, establishing a CI/CD pipeline, and deploying the full Kolobok application to Yandex Cloud. 

We introduced rigorous testing across backend APIs, ML components, and user-facing interfaces (Telegram bot and web UI). GitHub Actions was configured for CI, allowing for automated linting, test execution, and image building on every PR to `main`. A lightweight CD system was also added, automatically deploying the updated backend to our staging server.

Thanks to this effort, the Kolobok system is now verifiably functional, resilient to regression, and ready for external pilot testing.

---

## Testing Strategy

We structured our testing strategy around four pillars: backend unit testing, API integration, ML model validation, and end-user interaction coverage.

### Backend (FastAPI)

- **Tools**: `unittest`, `httpx`
- **Coverage**: 100% overall
- **Tests written**:
  - Input validation (bad image, invalid tokens)
  - Response formatting for successful and failed inferences
  - Token authentication & permissions

### API Integration Tests

- End-to-end test cases simulating:
  - Base64 image upload → inference → JSON response
  - Token failure handling
  - Spike-only and tread-only photo behavior
- Tools: `requests`, `pytest`, custom mock images

### Telegram Bot & Frontend Testing

#### Telegram Bot

- Covered flows:
  - Image sent too early
  - Cancel operation
  - Prediction correction
  - Token missing from config

- Manual testing was conducted

#### Web Platform

- Covered flows:
  - File drag/drop
  - Predict + correct
  - Network error fallback
  - Invalid file warning

- Testing via browser devtools and form mocking

### Machine Learning Validation

- **Tread Depth**:
  - Average error: 0.62mm (on synthetic test set)
  - Real-tire test batch: 83% within 1.0mm
- **Spike Classifier**:
  - FP+FN: ~7.4
  - ROC AUC: 0.91
- **OCR (GPT-4o)**:
  - Strict match: 100% on test set
  - Format compliance: 100%

Model interface was tested by simulating raw API calls and observing prediction JSON structure.

---

## CI/CD Setup

### CI Configuration

CI is set up via GitHub Actions:

- Triggers: PR/push to `main`
- Steps:
  - Install dependencies
  - Run formatting/linting
  - Run tests (`pytest`)

## Environment Setup 

We successfully deployed our application to Yandex Cloud (using free trial plan). 

Note: our service requires high computing power, which implies huge costs. We will power on the service only during demo.

### Staging Details

* Services exposed:
  * `/api/v1/analyze_tread`
  * `/api/v1/identify_tire`

### Stack Summary

| Component  | Technology                      |
| ---------- | ------------------------------- |
| Backend    | FastAPI + Docker                |
| Bot        | `python-telegram-bot`           |
| ML Models  | PyTorch, callable endpoints     |
| Deployment | GitHub Actions + Docker Compose |
| Monitoring | Logs + manual probes            |

---

## Code Coverage Report

We have implemented autolinting and autotesting for ML backend and JS frontend parts of our codebase.
Current state of the codebase coverage:

| Service  | Status       | 
| ------------ | ------------ |
| Backend (linting)    | ✅ 100% |
| Backend (tests)    | ✅ 100%  | 
| Frontend (tests)      | ✅ 100%  | 

---

## PM Team Vibe Check

| Team Member  | Status       | Note                                            |
| ------------ | ------------ | ----------------------------------------------- |
| Nikita M.    | ✅ Engaged    | Coordinating next week’s strategy          |
| Nikita Z.    | ✅ Motivated  | Finalized model testing and validation          |
| Vlad S.      | ✅ Energized  | Resolved Docker network bug                     |
| Sergey A.    | ✅ Positive   | Led coverage push for backend                   |
| Ekaterina P. | ✅ Focused    | Finished test loop for frontend                 |
| Darya S.     | ✅ Productive | Validated bot UX with edge cases                |
| Dmitry T.    | ✅ Curious    | Opened PR for synthetic validation overlay tool |

## Team Contributions

| Team Member            | Contributions                                            |
| ---------------------- | -------------------------------------------------------- |
| **Nikita Menshikov**   | Wrote the report, pitched CI/CD planning, ran team vibe check |
| **Nikita Zagainov**    | Added [tests](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/525d63a61452e9ad0815c060b0779ae282f800d6) to ML pipeline, facilitate [logging](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/399f2d04cc62a2e93aa5acce3fed7f71b2d32367) in the backend, conducted [experiments](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/e745eec8031d679f587587bb61d7e1c0d19f0b66) on enhancing tread depth recognition  |
| **Dmitry Tetkin**      | Assisted [research](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/07d1f331cf621ee1823b4ae1c9b6c321c00fa235) on how synthetic dataset influence precision, helped [integration](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/14c7b72d1a9c209696eedca49963cb8d97fa9925) synthetic data into pipeline, developed MacOS desktop [app](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/bac0805aab35fdb2466d17a27e5a5f7dcddf3903) |
| **Vladislav Strelkov** | Built full CI [pipeline](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/e1fe85b0771bb09a30fd453578bd7603ee84242b#diff-d398e54a64ae971408747d5cec234a6e2f610c8c8517e98b6fad3da618c97f02), [assisted](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/812d7ccc87561480c8e0a0640e50427a625b5d6a) in depth evaluation research          |
| **Sergey Aitov**       | [Built](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/143feba243b9d5280a7d41c4b306ae0371dc1ad7) OCR MVP                   |
| **Ekaterina Petrova**  | [Enhanced](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/8bf464be7c85b54369a3e6c526f714fbf1e24ece) bot logging and authentification, [assisted](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/36eb54d806a458b5fe413633c27f090cd4eca42c) in shaping the final version of the pipeline        |
| **Darya Stepanova**    | Webpage frontend and backend huge [update](https://github.com/IU-Capstone-Project-2025/Kolobok/commits/my-frontend-update/)    |

---

## Confirmation of System Operability

* ✅ All tests passing locally and in CI
* ✅ Docker builds succeed for all services
