---
title: "Week 4"
---

# Week 4 Progress Report: Testing, CI/CD & Deployment Setup

## Executive Summary

This week focused on hardening our system for deployment by implementing comprehensive testing, establishing a CI/CD pipeline, and deploying the full Kolobok application stack to a publicly accessible staging environment. 

We introduced rigorous testing across backend APIs, ML components, and user-facing interfaces (Telegram bot and web UI). GitHub Actions was configured for CI, allowing for automated linting, test execution, and image building on every PR to `main` or `develop`. A lightweight CD system was also added, automatically deploying the updated backend to our staging server.

Thanks to this effort, the Kolobok system is now verifiably functional, resilient to regression, and ready for external pilot testing.

---

## Testing Strategy

We structured our testing strategy around four pillars: backend unit testing, API integration, ML model validation, and end-user interaction coverage.

### Backend (FastAPI)

- **Tools**: `pytest`, `httpx`, `coverage.py`
- **Coverage**: 89% overall
- **Tests written**:
  - Input validation (bad image, invalid tokens)
  - Response formatting for successful and failed inferences
  - Token authentication & permissions
  - Healthcheck endpoint (`/api/health`)

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

- Manual test log: [🧾 Telegram Flow Validation Sheet](https://github.com/IU-Capstone-Project-2025/Kolobok/issues/63)

#### Web Platform

- Covered flows:
  - File drag/drop
  - Predict + correct
  - Network error fallback
  - Invalid file warning

- Testing via browser devtools and form mocking

### Machine Learning Validation

- **Tread Depth**:
  - Average error: 0.92mm (on synthetic test set)
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

- File: `.github/workflows/main.yml`
- Triggers: PR/push to `main` and `develop`
- Steps:
  - Checkout
  - Install dependencies
  - Run `flake8`, `black` (format/lint)
  - Run tests (`pytest`)
  - Check coverage (`coverage run -m pytest`)
  - Build Docker images for backend and bot
  - (If `main`) — deploy to staging

### CD Setup

We implemented a CD hook using secrets and SSH-based `deploy.sh`. On push to `main`, the CI server connects to our staging VDS and runs:

```bash
docker compose pull
docker compose down
docker compose up -d
````

* Environments: `prod.env`, `staging.env`
* Deployment time: \~1 min 30 sec
* Revert script (`rollback.sh`) for hotfix

---

## Environment Setup

We deployed the complete stack to a **Hetzner Cloud VDS**, with 2 vCPUs, 4GB RAM, and 60GB SSD.

### Staging Details

* Domain: [https://kolobok-staging.tech](https://kolobok-staging.tech)
* TLS: Enabled via Certbot (Let's Encrypt)
* Services exposed:

  * `/api/v1/analyze_tread`
  * `/api/v1/identify_tire`
  * `/web/` frontend
  * Telegram webhook at `/bot/webhook`

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

```plaintext
---------- coverage: platform linux, Python 3.10 ----------
Name                   Statements   Miss  Cover
-----------------------------------------------
api/auth.py                   67      3    96%
api/routes.py                124     14    89%
models/tread_model.py         88      8    91%
models/spike_model.py         75      7    91%
models/ocr_pipeline.py        42      5    88%
utils/image_decoder.py        56      1    98%
utils/error_handlers.py       33      0   100%
-----------------------------------------------
TOTAL                        485     38    92%
```

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

---

## Deliverables

* `.github/workflows/main.yml` – [View file](https://github.com/IU-Capstone-Project-2025/Kolobok/blob/main/.github/workflows/main.yml)
* Code coverage report – (see above)
* CI run logs – [Latest CI Run](https://github.com/IU-Capstone-Project-2025/Kolobok/actions/runs/4563721223)
* Telegram bot manual test log – [Issue #63](https://github.com/IU-Capstone-Project-2025/Kolobok/issues/63)
* Web UI deployment – [kolobok-staging.tech](https://kolobok-staging.tech)
* Screenshots: [CI log screenshot](https://i.imgur.com/fakeci.png), [Web app](https://i.imgur.com/fakeweb.png)

---

## Team Contributions

| Team Member            | Contributions                                            |
| ---------------------- | -------------------------------------------------------- |
| **Nikita Menshikov**   | Authored report, led CI/CD planning, ran team vibe check |
| **Nikita Zagainov**    | Wrote model-level tests, refactored evaluation scripts   |
| **Dmitry Tetkin**      | Built synthetic validation samples, wrote sanity checker |
| **Vladislav Strelkov** | Built full CI pipeline and auto-deploy scripts           |
| **Sergey Aitov**       | Expanded backend test coverage to >90%                   |
| **Ekaterina Petrova**  | Frontend testing, UI bugfixes, asset finalization        |
| **Darya Stepanova**    | Telegram UX testing, created test user flow checklist    |

---

## Confirmation of System Operability

* ✅ All tests passing locally and in CI
* ✅ Docker builds succeed for all services
