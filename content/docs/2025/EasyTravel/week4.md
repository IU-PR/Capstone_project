---
title: "Week #4"
---

# Week #4

## Testing and QA

**Strategy & types of tests implemented**
- **Manual endpoint testing** via Swagger UI and Postman:
    - Verified `/api/poi` search and `/api/poi/recommendations` endpoints.
    - Checked authentication (`/api/token/get-token`, `/api/token/refresh`, `/api/token/current-user`).
- **Data‐quality validation** on a hand‐labeled set of 60 real-world queries.
- **Performance measurements** with three custom scripts:
    - `measure_index_load.py` (index load time & memory),
    - `measure_search_latency.py` (SBERT.encode vs FAISS.search latency),
    - `compute_precision.py` (precision@5/10).

### Evidence of test execution
- **Index load**: 6 ms, RSS ↑ from 103.84 MB to 106.16 MB
- **Latency** (60 queries):
    - encode_time_ms: mean ≈ 92.6 ms
    - search_time_ms: mean ≈ 0.77 ms
- **Accuracy** on validation set (top-5 judgments):
    - precision@5 ≈ 0.84
    - precision@10 ≈ 0.76

All raw results are in `DLS/experiments/results/*.csv`.

---

## CI/CD

- **Current status**: No CI/CD pipeline yet.
- **Tools planned**: GitHub Actions + Docker Compose.
- **Next steps**:
    1. Add a GitHub Actions workflow to build the backend image, run lint/tests, and push to a container registry.
    2. Integrate frontend build and unit tests into the pipeline.

---

## Deployment

### Staging
- **Local staging** via `docker-compose up --build` (services: backend, Postgres).
- Configuration variables in `.exampleenv`; mounts include code and DLS data.

### Production
- **Not yet implemented** — planned for next sprint.
- **Goals**:
    - Cloud VM or Kubernetes deployment.
    - Domain name, SSL, environment configs, autoscaling.

---

## Vibe Check

- **Progress**: Core search & recommendation service working; experiments completed.
- **Roadblocks**: CI/CD missing;
- **Team dynamics**: Emil led backend/DLS; Vlad drove frontend integration;

---

## Weekly commitments

| Participant  | Contribution                                                                                                                                                                  | Link to Commit                                                                                                                                                                                                                                                                                                                       |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Emil**     | • Implemented FAISS‐based search service, query encoding, alcohol filtering<br>• Wrote scripts for latency & precision measurement<br>• Authored documentation & Docker setup | • https://github.com/IU-Capstone-Project-2025/EasyTravel/pull/19<br/> • https://github.com/IU-Capstone-Project-2025/EasyTravel/pull/20<br/> • https://github.com/IU-Capstone-Project-2025/EasyTravel/pull/21                                                                                                                         |
| **Teammate** | • Built frontend UI for search and recommendations<br>• Integrated with backend API & auth<br>• Resolved UI bugs and styling issues                                           | • https://github.com/IU-Capstone-Project-2025/EasyTravel/commit/dd1efbaae6f44ca0a654affbf98670556c934a6c<br/> • https://github.com/IU-Capstone-Project-2025/EasyTravel/commit/856bf37d8f61022ac76043867366b9b832463214<br/> • https://github.com/IU-Capstone-Project-2025/EasyTravel/commit/a04cd3ca9e2ed0c82cbaedce3af0f86ec8f621ef |

### Plan for Next Week

1. Write unit & integration tests for backend.
2. Configure CI pipeline (GitHub Actions).
3. Finalize production deployment docs & scripts.
4. Harden frontend, add E2E tests.

---

## Confirmation of the code’s operability

We confirm that the code in `main` branch:
- [x] is in working condition
- [x] can be started via `docker-compose up --build` (see **Backend/README.md**)
