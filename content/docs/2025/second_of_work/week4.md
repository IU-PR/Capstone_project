---
title: "Week #4"
---

# **Week #4**

## CI/CD

### Overview

The repository defines **three GitHub Actions workflows**—one per delivery target:

| Workflow (path)                                   | Scope              | Trigger paths       |
| ------------------------------------------------- | ------------------ | ------------------- |
| **Backend CI/CD Pipeline** (`admin/backend/**`)   | Go API             | `admin/backend/**`  |
| **Mobile CI/CD Pipeline** (`mobile/**`)           | Flutter app        | `mobile/**`         |
| **Frontend CI/CD Pipeline** (`admin/frontend/**`) | Nuxt admin console | `admin/frontend/**` |

Each workflow reacts to:

* **`workflow_dispatch`** (manual run, environment selector)
* **`push`** to `main` touching its scope
* **`pull_request`** into `main` touching its scope


### Backend pipeline (`.github/workflows/backend.yml`)

| Job            | Purpose                                                    | Key actions                                                                                  |
| -------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `lint`         | Static analysis with **golangci‑lint** (Go 1.24)           | `setup-go` → `golangci-lint-action`                                                          |
| `test`         | Unit & integration tests                                   | `go test ./... -v` (uses cached modules)                                                     |
| `build-deploy` | Build Docker image and roll out **backend** service on VPS | `appleboy/ssh-action` → `git pull` → `docker compose up -d --force-recreate --build backend` |

Graph: `lint → test → build-deploy` (deploy gated on green tests via `needs`).

---

### Mobile pipeline (`.github/workflows/mobile.yml`)

| Job      | Purpose                                | Key actions                                      |
| -------- | -------------------------------------- | ------------------------------------------------ |
| `lint`   | Dart static checks (`flutter analyze`) | `flutter-action@v2` (Flutter 3.13.x)             |
| `deploy` | Rebuild & restart **mobile** container | SSH same as backend, `docker compose ... mobile` |

> **Note** – the `needs: lint` line is commented out, so `deploy` currently runs even if analysis fails. A fix PR is queued for Week 5.

---

### Frontend pipeline (`.github/workflows/frontend.yml`)

| Job      | Purpose                               | Key actions                                                         |
| -------- | ------------------------------------- | ------------------------------------------------------------------- |
| `lint`   | ESLint & stylelint checks             | `setup-node` (LTS) → `yarn install --frozen-lockfile` → `yarn lint` |
| `deploy` | Rebuild & restart **frontend** (Nuxt) | SSH script identical to other workflows                             |

Like the mobile workflow, the `needs: lint` guard is commented; we plan to re‑enable it together with Playwright smoke tests.

---

### Secrets & infrastructure

All deploy jobs reference shared GitHub Secrets:

| Secret            | Purpose                          |
| ----------------- | -------------------------------- |
| `SSH_HOST`        | Linode VPS IP / domain           |
| `SSH_USERNAME`    | Non‑root SSH user (sudo allowed) |
| `SSH_PRIVATE_KEY` | 4096‑bit RSA private key         |

On the VPS the repo lives at `~/gym-genius/` behind **Traefik v3** with LetsEncrypt certificates. `docker compose up -d --force-recreate --build <service>` keeps downtime under 2 s thanks to Traefik’s request buffering.

### Challenges

Mobile CI was unpredictable and it was decided to drop so far since mobile application is built, not web.

In the future, FastPlane pipeline will be introduced with deploying to TestFlight and optionally to AppStore. 

### Links to CI/CD configuration files

[links](https://github.com/IU-Capstone-Project-2025/gym-genius/tree/main/.github/workflows)

## Deployment

### Staging

Do not have staging environment so far.

### Production

We already deployed our project on a particular domain, will show on meeting.

## Vibe Check

Everyone's happy and respective!

# Weekly commitments

## Individual contribution of each participant

1. Ivan Chabanov
    - Developed a statistics page. Implemented a grid github-like statistic widget
    - Added mocked data and made a function for generating random workouts for mocking
    - Orchestrated team and made sure everyone's happy and has work to do
    - [Pull Request](https://github.com/IU-Capstone-Project-2025/gym-genius/pull/24)

2. Vladislav Kuznetsov
    - Created full ci/cd pipelines for backend frontend and mobile 
    - [Frontend pipeline](https://github.com/IU-Capstone-Project-2025/gym-genius/pull/23)
    - [Backend pipeline](https://github.com/IU-Capstone-Project-2025/gym-genius/pull/20)
    - [fix: pipelines
](https://github.com/IU-Capstone-Project-2025/gym-genius/commit/062e8a5c2172cad336139caa3befeaf922148644)

3. Aleksandr Mikhailov
    - add logging for requests (json and text)
    - add db tables for users, exercises, and workouts
    - add crud methods for users
    - fix minor status code bugs
    - [Artifacts](https://github.com/IU-Capstone-Project-2025/gym-genius/pull/21)

4. Kirill Nosov
    - Complete authorization.
    - Made create, read, update, delete methods for the training.
    - Made create and delete methods for the exercises.
    - Write Swagger for the new methods.
    - Started writing method for the exercise photos get.
    - [Artifacts](https://github.com/IU-Capstone-Project-2025/gym-genius/pull/21)

## Plan for Next Week

- In **mobile** we plan to fully connect backend parts to our application and build local DB to actually save workouts.
- On **backend** we plan to finish authorization part and implement other endpoints.
- On **admin** we plan to connect backend and build some more informative graphs to display data.
- Devopsing - improving current state of servers, reconfiguring ci on mobile.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
