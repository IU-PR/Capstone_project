---
title: "Week #3"
---

# **Week #3**

## Implemented MVP features

### 1. Functional user journey

* **Start**: User visits **Main Page**
* **Views**: **List of Contests** → **Contest Page**
* **Personal Dashboard**: Personal account view
* **Submission user's solution**

### 2. MVP features
| Category           | Feature                                               | PR / Commit              |
| ------------------ | ----------------------------------------------------- | ------------------------ |
| **Authentication** | JWT login/signup (GoTrue) + Casbin RBAC               | [№19](https://github.com/IU-Capstone-Project-2025/verilog-contest/pull/19)                      |
| **CRUD Services**  | Contests, Submissions, Users, Tasks                   | [№19](https://github.com/IU-Capstone-Project-2025/verilog-contest/pull/19)                      |
| **gRPC**           | Client in API                     | [№22](https://github.com/IU-Capstone-Project-2025/verilog-contest/pull/22)                      |
| **Runner**         | Dockerized Verilog sandbox                | [№23](https://github.com/IU-Capstone-Project-2025/verilog-contest/pull/23)                      |
| **Frontend UI**    | Basic design: main page, contest list/page, personal account   | [№18](https://github.com/IU-Capstone-Project-2025/verilog-contest/pull/18)                       |
| **DevOps**         | Dockerfiles & docker-compose setup                    | Commits: [Improve Backend's Dockerfile and main.go](https://github.com/IU-Capstone-Project-2025/verilog-contest/commit/965c32eb9bf698e2bdc5fc2c9ddf2f059a0c5544), [fix(devops): GoTrue volume changed](https://github.com/IU-Capstone-Project-2025/verilog-contest/commit/38f67690b45b8b89c4c1bc17ed0fbfa01d337278)  |
|                    | CI/CD pipeline (lint, format, staticcheck, tests, Docker Hub) | Actions run [pushing changes to dockerhub](https://github.com/IU-Capstone-Project-2025/verilog-contest/actions/runs/15858289358) |
| **Kubernetes**     | Initial deployment manifests                          | Initial commit           |


## Demonstration of the working MVP
 [Demo video on google drive](https://drive.google.com/file/d/1Z-bZad2_4bDh9DcbkoxOxJVZvunxscqz/view?usp=sharing)

## Internal demo

*Notes from internal demo on 23 June 2025:*

* **Attendees**: Diana, Mikhail, Aleksei, Vladislav, Sofia
* **Feedback:**

  * Core CRUD & Auth: stable
  * Runner: functional
  * Runner: in process
  * CI/CD: staticcheck errors need fixes
  * Frontend: basic UI ready
* **Action Items:**

  1. Backend: Runner-Manager integration into API flow
  2. Frontend: implement Submit API wiring and Results page
  3. DevOps: complete Docker Hub pushes in CI/CD, initiate Kubernetes deployment

# Weekly commitments

## Individual contribution of each participant

| Team Member            | Week #2 Contributions                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| **Mikhail Panteleev**  | UI refactoring, submission flow and runner diagrams, Runner implementation, starting Runner-manager prototype.                        |
| **Vladislav Merkulov** | CRUD for submissions and contests, authentication and  authorization middleware, gRPC client in API.                       |
| **Aleksei Fominykh**   | Runner prototype, submission flow and runner diagrams, to start Kubernetes deployment.                                         |
| **Sofia Kulagina**     | Lint in frontend checks, staticcheks and gotest in backend checks, Docker Hub in CI/CD, runner research.             |
| **Diana Yakupova**     | Meeting organization, update kanban-board, assist with blockers, to define sprint goals for the next weeks, research devops responsobilities, report.|

## Plan for Next Week

In Week #4, we will integrate the Submit into the frontend and develop the Results page. On the backend, our goal is to finalize Runner‑Manager integration. We will also deploy the full stack in a staging environment via docker‑compose, enhance the CI/CD pipeline check new dev changes, deploy the Kubernetes.

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [✔] In working condition.
- [✔] Run via docker-compose.
