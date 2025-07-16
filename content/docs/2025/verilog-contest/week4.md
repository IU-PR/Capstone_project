---
title: "Week #4"
---

# **Week #4**

## Testing and QA

*Summary of testing strategy and types of tests implemented.*
We have implemented a combination of unit tests and Postman-based integration tests for API endpoints. All tests are automatically executed in the CI pipeline on every pull request and push to dev.

### Evidence of test execution

- Link to Postman collection: https://www.postman.com/collections/f38f971d0b2e5a4c65bb
- CI logs: https://github.com/IU-Capstone-Project-2025/verilog-contest/actions/runs/16031851882/job/45234142892

## CI/CD

The CI/CD pipeline is built with GitHub Actions, triggered by PRs to main, pushes to dev/devops, and manual dispatch. It includes four stages:

**1. Backend checks:** staticcheck, gofmt, go test

**2. Frontend checks:** npm ci, Prettier formatting, ESLint linting

**3. Compose tests:** Docker Compose up, container health checks, HTTP response validation

**4. Push images:** Authenticate to GHCR, build & push Docker images for all services



### Links to CI/CD configuration files

- CI/CD file: https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/.github/workflows/ci.yaml

## Deployment

### Staging

We deploy to staging using Docker Compose orchestrated by Coolify + Nixpacks, exposing services through a Cloudflare tunnel. ICD club servers host the environment; secrets and .env are managed securely.

### Production

Currently, our production environment is hosted on a single VPS (ICD club server) using docker-compose. The deployment steps are:

 - **Image build & push:** On merge to main, GitHub Actions builds Docker images and pushes them to GHCR.

- **Compose deployment:** The server pulls images from GHCR and runs docker-compose to update services.

 - **DNS:** The domain is **https://platform.innochipdesign.ru/**.

## Vibe Check

- **Resources & Expertise:** Team generally has sufficient capacity, though Diana feels she needs deeper backend guidance for faster frontend integration.
- **Blockers:** Task distribution and management could be streamlined for clearer ownership.
- **Team Value:** All members acknowledge their contributions.

# Weekly commitments

## Individual contribution of each participant

| Team Member            | Week #2 Contributions                                                                      | Commits| 
| ---------------------- | ------------------------------------------------------------------------------------------ | ----------------------|
| **Mikhail Panteleev**  | Social communication for finding server (+ domen), initial service and bugs fix in backend, hard thinking about jadger parser, deploy.                       | [db6086f](https://github.com/IU-Capstone-Project-2025/verilog-contest/commit/db6086f5fba1f8f33c6293805b3c128b6ed54334), [062f3bc](https://github.com/IU-Capstone-Project-2025/verilog-contest/commit/062f3bcd11bc41ad3c8b70a89cffe9aaa8a67ebf), [aa54f9f](https://github.com/IU-Capstone-Project-2025/verilog-contest/commit/aa54f9f558415d8cdade189205b199f5280b1c31)
| **Vladislav Merkulov** | Runner integration into system, testing.                       | [8af80eb](https://github.com/IU-Capstone-Project-2025/verilog-contest/commit/8af80eb5319c486b3821b6f58d15828b77d446ca), [fb4008d](https://github.com/IU-Capstone-Project-2025/verilog-contest/commit/fb4008d8f561c514bee4c4be9bde82a48a351db4) |
| **Aleksei Fominykh**   | Developing Judger parser, staging, kuber.                                         |
| **Sofia Kulagina**     | CI/CD using docker-compose instead of build and pushing in GitHub container, initial service in CI/CD.             | [bcc9ad5](https://github.com/IU-Capstone-Project-2025/verilog-contest/commit/bcc9ad51ce4dfc9e025068e9f5f96666ba2ec22e)|
| **Diana Yakupova**     | Meeting organization, report, backend api in contest components, configure api in api client with auth.| [a03c80e](https://github.com/IU-Capstone-Project-2025/verilog-contest/commit/a03c80e09087f9f571e8b822f71a164a3a7c6890)|


## Plan for Next Week

In Week #5, our goal is to finilize testing, provide more backend API in frontend, bug fixing and finilizing judger-parser in backend. We will also work on deploying the application to production.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [✔] In working condition.
- [✔] Run via docker-compose.