---
title: "Week #4"
---

# **Week #4**

## Testing and QA

- #### Unit Tests:

  Unit tests were written for the backend API responsible for course search and retrieval of popular courses. These tests include mocking the vectorization process and validating the correct handling of Stepik API responses to ensure the expected results are returned for different scenarios.
  
- #### Integration Tests:
  
  Integration tests verify the entire flow of search and popular courses endpoints (`/api/courses/search`, `/api/courses/popular`), including actual interactions with Qdrant and external Stepik API. This ensures end-to-end correctness of API logic and external dependencies.
  
- #### E2E (End-to-End) Tests:
  
  End-to-end live tests (`test_live_search_and_popular`) were performed against the production API, sending real HTTP requests to confirm availability, valid responses (status 200 or 404), and correct handling of live data after deployment.
  
- #### Test Runner:
  All backend tests are executed in a dedicated Docker test container (`backend/Dockerfile.test`) using `pytest`.
  
- #### Frontend Tests:
  (Pending / In progress)

### Evidence of test execution

Reports and loggs are in the assets/week4: [Link](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/tree/master/assets/week4)

## CI/CD

### CI:
  CI runs on every push or pull request to `master` or `develop` using `.github/workflows/ci.yml`.
The pipeline consists of two parallel jobs: backend and frontend testing.

#### Backend Testing:

- **Builds and starts services** via `docker compose build` and `docker compose up -d`, including all dependencies.
- **Creates a specialized test container** (`backend/Dockerfile.test`), isolated from production containers.
- **Runs unit and integration tests** with `pytest` to check API logic and component interactions.
- **Waits for backend readiness** by polling the live service before running E2E tests.
- **Executes end-to-end (E2E) tests** simulating user scenarios through live HTTP requests.
- **Cleans up** by shutting down all containers and removing volumes for a clean state.

**Frontend Testing:**

Uses `pnpm` for installing dependencies and running Jest-based tests for React/TypeScript code, ensuring frontend reliability.

### Continuous Deployment (CD)

There are **separate CD workflows for staging and production**:

#### Staging Deployment (`.github/workflows/deploy_to_staging.yml`):**

- Triggered after CI passes on `develop`.
- Uses SSH keys from secrets to securely sync the latest code to the staging server via `rsync`.
- Restarts the application using Docker Compose, rebuilding images to reflect changes.

#### Production Deployment (`.github/workflows/deploy_to_prod.yml`):**

* Triggered after CI passes on `master`.
* Mirrors the staging process, but targets the production server and uses separate credentials for isolation.


- #### Tools:

  - Docker, Docker Compose for environment management
  - Nginx as reverse proxy
  - Certbot for HTTPS
  - VPS servers (Ubuntu)

- #### Challenges:

- Setting up isolated staging and production environments on separate VPS servers
- Automating SSL certificate renewal and Nginx reload
- Ensuring database persistence across deployments


### Links to CI/CD configuration files

- [.github/workflows/ci.yml](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/blob/master/.github/workflows/ci.yml) - Continuous Integration

- [.github/workflows/deploy_to_staging.yml](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/blob/master/.github/workflows/deploy_to_staging.yml) - Staging Deployment

- [ .github/workflows/deploy_to_prod.yml](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/blob/master/.github/workflows/deploy_to_prod.yml) - Production Deployment


## Deployment

### Staging

### Staging

Deployment to staging is fully automated and runs after CI passes on the `develop` branch. The process:

- #### Trigger: Deploys only when all tests pass (`workflow_run` after CI on `develop`).
- #### SSH Setup: Uses a private key from GitHub Secrets to securely connect to the staging server.
- #### Code Sync: Updates the server via `rsync`, ensuring the codebase exactly matches the repo.
- #### Deployment:

  - Stops old containers (`docker compose down`)
  - Rebuilds and restarts the stack (`docker compose up --build -d --remove-orphans`)

#### Stack includes:
 
- FastAPI backend (port 8000)
- React frontend (port 3000)
- Qdrant vector database (persistent volumes)

#### Requirements:

- Docker & Docker Compose installed
- SSH access for deploy user
- Open ports: 8000, 3000

- #### Verification:

- After deployment, health can be checked via:

  ```
  curl http://staging-server:8000/health
  curl http://staging-server:3000
  ```


## Production

Deployment to production is **fully automated** and triggered after CI passes on the `master` branch (no manual steps required). The process:

- **Trigger:** Deploys only on successful CI (`workflow_run` after CI on `master`)—ensures only tested, stable code is deployed.
- **SSH Setup:** Uses a private key from GitHub Secrets to securely connect to the production VDS.
- **Code Sync:** Uses `rsync` to mirror the repo to `/home/[user]/skillsnavigator/` on the server.
- **Deployment:**

  - Stops existing containers: `docker compose down`
  - Rebuilds and restarts stack: `docker compose up --build -d --remove-orphans`

#### Production stack includes:

- FastAPI backend (port 8000)
- React frontend (served via Nginx, port 3000)
- Qdrant vector database (persistent volumes)

#### Recommended infrastructure & config:

- Docker, Docker Compose, and Nginx installed on the server
- Certbot/Let's Encrypt for HTTPS
- DNS: `skillsnavigator.ru` and `www.skillsnavigator.ru` point to VDS IP
- Firewall allows only ports 22 (SSH), 80 (HTTP), and 443 (HTTPS); blocks direct access to 3000/8000
- GitHub Secrets hold SSH credentials and connection details

#### Current limitations:

- Brief downtime during deploy (`docker compose down`)
- No automated SSL/HTTPS or reverse proxy shown in compose file (should be managed via Nginx on the host)
- No zero-downtime, monitoring, or automated health checks yet

#### Post-deployment:

- App available at [https://skillsnavigator.ru](https://skillsnavigator.ru)
- Health can be checked via `curl https://skillsnavigator.ru/api/health`

## Vibe Check

The team is satisfied with the progress made so far, however  this week was the most challenging yet. Two team members had to balance Practicum Project work with Deep Learning for Search project defense and final exam, while another was out sick. Despite these hurdles, the team has done a great job staying strong, supporting each other, doing everything we could and remains motivated to deliver a high-quality product.

| Name (Role)             | GitHub         | Email                                    | Role(s)                       | Main contributions / Notable PRs/Commits |
|-------------------------|----------------|------------------------------------------|-------------------------------|------------------------------------------|
| Lana Ermolaeva (lead)   | @oELYAo        | l.ermolaeva@innopolis.university         | Project/Product Management, ML| PM: Report writing, ML architecture planning [Click-up whiteboard](https://app.clickup.com/9015876757/whiteboards/8cp6q4n-395); ML: Augmented search [Commit](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/6934fdd21748c0d52873eb9ca58c33eafdce9d4d) |
| Adilya Saifetdiarova    | @sayfetik      | a.saifetdiarova@innopolis.university     | Frontend, UX/UI design       | Implemented Roadmap page, Log-in popup, loading screen [PR #9](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/pull/9); Frontend unit tests [PR #8](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/pull/8) |
| Ivan Ershov             | @spiritonchiс  | i.ershov@innopolis.university            | ML                            | Tests for Deepseek API [Commit]() |
| Bulat Gazizov           | @BulatGazizov0 | b.gazizov@innopolis.university           | Backend, DevOps               | Added env variables for project URL and Stepik OAuth (client ID/secret);<br>Endpoints for Stepik OAuth URL, callback, access token in cookies;<br>Endpoint to get current user data [Commit](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/65c64745e8f88d0acc97dfc0dce1f1c71fc55554) |
| Arthur Popov            | @ee_boooy      | ar.popov@innopolis.university            | Backend, MLOps, CI/CD         | CI/CD setup and maintenance, backend integration (excluding frontend & ML tests) [PR #8](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/pull/8) |


## Plan for Next Week
Link logging in via Stepik to frontend, display "Мой Путь" properly, save chat & roadmap history, enhance ML (place courses by complexity, constrain by money & duration).


## Confirmation of the code's operability

We confirm that the code in the main branch:
- [✔] In working condition.
- [✔] Run via docker-compose (or another alternative described in the `README.md`).
