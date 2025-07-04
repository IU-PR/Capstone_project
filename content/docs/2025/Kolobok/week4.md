---
title: "Week 4"
---

# Week 4 Progress Report: Testing, CI/CD & Deployment Setup

## Executive Summary

This week focused on hardening our system for deployment by implementing comprehensive testing, establishing a CI/CD pipeline, and deploying the full Kolobok application stack to a publicly accessible staging environment. 

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
  - Real-tire test batch: 82% within 1.0mm
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
  - Build Docker images for backend and bot
  - Deploy to staging

### CD Setup (in progress) 

We implemented a CD hook using secrets and SSH-based `deploy.sh`. On push to `main`, the CI server connects to our staging VDS and runs:

```bash
docker compose pull
docker compose down
docker compose up -d
```

⸻

Environment Setup

We deployed our service to a free trial on Yandex Cloud, but this instance will be kept running only during one demo hour (due to large costs for resources required for our models).

Staging Details
	•	Domain: (under negotiation with the customer)
	•	Security: Bearer tokens
	•	Services exposed:
	•	/api/v1/analyze_tread
	•	/api/v1/identify_tire

Stack Summary

Component	Technology
Backend	FastAPI + Docker
Bot	python-telegram-bot
ML Models	PyTorch, callable endpoints
Deployment	GitHub Actions + Docker Compose
Monitoring	Logs + manual probes


⸻

Code Coverage Report

Backend: 100%
JS Frontend: 100%


⸻

PM Team Vibe Check

Team Member	Status	Note
Nikita M.	✅ Engaged	Coordinating next week’s strategy
Nikita Z.	✅ Motivated	Finalized model testing and validation
Vlad S.	✅ Energized	Resolved Docker network bug
Sergey A.	✅ Positive	Led coverage push for backend
Ekaterina P.	✅ Focused	Finished test loop for frontend
Darya S.	✅ Productive	Validated bot UX with edge cases
Dmitry T.	✅ Curious	Opened PR for synthetic validation overlay tool

Team Contributions

Team Member	Contributions
Nikita Menshikov	Wrote the report, pitched CI/CD planning, ran team vibe check
Nikita Zagainov	Added tests to ML pipeline, facilitate logging in the backend, conducted experiments on enhancing tread depth recognition, hosted the service on Yandex Cloud
Dmitry Tetkin	Conducted research on how synthetic dataset influence precision, integrated synthetic data into pipeline
Vladislav Strelkov	Built full CI pipeline, assisted in depth evaluation research
Sergey Aitov	Built OCR MVP
Ekaterina Petrova	Enhanced bot logging and authentification, assisted in shaping the final version of the pipeline
Darya Stepanova	Webpage frontend and backend huge update


⸻

Confirmation of System Operability
	•	✅ All tests passing locally and in CI
	•	✅ Docker builds succeed for all services

