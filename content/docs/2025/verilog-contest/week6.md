---
title: "Week #6"
---

# **Week #6**

## Links

- **Deployment**: https://platform.innochipdesign.ru/
- **API Docs**: We used swagger to generate docs automatically from annotations on endpoints. You can find them at `http://localhost:8081/swagger/index.html#/` after launching the app locally.
- **Demo**: https://drive.google.com/file/d/1xFZqDkaBlVOI4KM5uIv7dLdIxhPjhkPA/view?usp=drive_link
- **Arcgitecture diagram:** 
  - General: https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/architecture-diagram.png
  - Runner: https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/inside-runner.png
- **Submission-flow:** https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/submission-flow.png

- **User flow:** https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/user-flow.png

- **Frontend components with API:** https://excalidraw.com/#json=dhm9VrgFtowewja70TNCk,uZGGNYJ0-tBXG5Y154f8Jg

- **System architecture:** https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/system-architecture.md

- **Specifications:** https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/specifications.md

- **README:** https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/README.md

## Final deliverables

### Project overview

_The Verilog Contest Platform_ is an online contest platform for practicing digital design using hardware description languages, allowing students to solve problems by writing and testing code in a sandboxed environment with automated verification.

### Features

* **User authentication & authorization:** JWT with GoTrue, role‑based access with Casbin.
* **CRUD:** Contests, tasks, users and submissions REST APIs.
* **Submission Flow:** Frontend integration, file upload, status polling.
* **Sandboxed runner:** Docker + Seccomp isolation, gRPC Runner‑Manager orchestration.
* **Results Page:** Displays pass/fail.
* **Kubernetes deployment:** Manifests for staging, seamless rolling updates for new versions.
* **Monitoring:** Grafana + Prometheus monitoring setup, go admin dashboard.
* **Testing:** Unit tests for CRUD, integration tests.

### Tech stack

* **Frontend:** TypeScript, React, Vite, Tailwind CSS
* **Backend:** Go, Fiber, gRPC
* **Auth:** GoTrue, Casbin
* **Database & Storage:** PostgreSQL, Redis, MinIO
* **Runner:** Docker, Nsjail sandbox
* **CI/CD:** GitHub Actions, Docker Hub, Coolify
* **Monitoring:** Grafana, Prometheus, go admin
* **Infrastructure:** Docker Compose, Kubernetes manifests

### Setup instructions
Please, try to use deployment link first: https://platform.innochipdesign.ru/

If you want to run it locally follow these steps:
1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/verilog-contest.git
   cd verilog-contest
   ```

2. Create an `.env` file based on the example:

   ```bash
   cp .env.example .env
   ```

   Then edit the `.env` file and adjust settings as needed.

3. Build and start the services using Docker Compose:

   ```bash
   docker-compose up -d
   ```

4. Access the services:
   - Frontend: http://localhost
   - Backend API: http://localhost:8081


## Presentation draft

https://drive.google.com/file/d/18C_HRpKfIm9pbjdf3sI3I0sChCtjmm1C/view?usp=drive_link

# Weekly commitments

## Individual contribution of each participant

| Team Member            | Week #2 Contributions                                                                     
| ---------------------- | ------------------------------------------------------------------------------------------ |
| **Mikhail Panteleev**  |         Bug fixing in frontend and backend, system testing.               
| **Vladislav Merkulov** | Added tempo instead of jaeger and some spans in runner.      
| **Aleksei Fominykh**   | Complete k8s manifests, start to add monitoring.                                     
| **Sofia Kulagina**     | Go admin set up.            |
| **Diana Yakupova**     | Meetings organization, report, kanban-board, integration tests, presentation. |

## Plan for Next Week

Complete testing of the project, add monitoring, prepare documentation and presentation speach.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [✔] In working condition.
- [✔] Run via docker-compose.