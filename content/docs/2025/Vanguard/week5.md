---
title: "Week #5"
---

# **Week #5**

## Feedback

### Sessions

**Session 1: Student 1**

- **Setup:** Played the game as an **admin** with the participant on another laptop.

- **Experience:**
  
  - The connection setup worked as expected.
  - Game flow was understandable but occasionally felt abrupt between turns.

- **Feedback:**
  
  - Suggested adding a **timer** between moves to keep the pace consistent.
  - Requested a more intuitive and **clearer UI**, especially for player actions.
  - Recommended implementing a **leaderboard** to track winners across games.

**Session 2: Student 2**

- **Setup:** Played the game as a **participant** while a teammate acted as the admin.

- **Experience:**
  
  - Game mechanics were clear, but transitions between rounds could be smoother.
  - Found the command-line prompts occasionally confusing.

- **Feedback:**
  
  - Wanted a more **streamlined game flow** and clearer indications for turns.
  - Mentioned that the UI could be made more **user-friendly**.
  - Agreed that a **leaderboard** feature would make it more engaging.

**Session 3: Student 3**

- **Setup:** Played as a **participant** with all team members involved, one acting as admin.

- **Experience:**
  
  - Experienced bugs that crashed the fame flow, when was playing in parallel with other users (parallel session)
  - Enjoyed the multiplayer interaction, but some delays were unclear.

- **Feedback:**
  
  - Requested a **visible countdown or timer** for each move.
  - Suggested improving **visual feedback** for game state updates.
  - Liked the idea of a **leaderboard** to enhance replayability.
    
    

### Analyze

Based on the user sessions, the following key points were identified:

- **Parallel Session Bug**: One user experienced a crash when multiple sessions ran in parallel.  
  _Priority: High_

- **Game Flow Issues**: Users felt the game flow was sometimes abrupt and unclear.  
  _Priority: High_

- **Timer Between Questions**: Users suggested a countdown timer to improve pacing and awareness of turns.  
  _Priority: Medium_

- **Leaderboard Feature**: Users wanted a leaderboard to track performance and add competitiveness.  
  _Priority: Medium_

- **UI Clarity**: Users had difficulty understanding prompts and game state changes.
  _Priority: Low_

## Iteration & Refinement

### Implemented features based on feedback

- Fixed a critical deadlock caused by overlapping RabbitMQ queue consumers that processed the same event across multiple sessions.
  
  

### Performance & Stability

 **How to Measure These Metrics**

* **Monitoring Tools:**
  
  * Use Prometheus + Grafana to track backend performance (e.g., message delay, queue length, active sessions).
  
  * Use WebSocket and RabbitMQ client metrics (latency, retries, failures).

### Documentation

**1. General `README.md` (Root Level)**  

- **Purpose:** Provides an overview of the project and instructions to **run the entire system manually** using Docker Compose.  
- **Includes:**  
  - System architecture description  
  - How to start services (manual and Docker-based)  
  - Environment variable setup  
  - Useful development and testing commands

**2. Swagger Documentation (OpenAPI) for REST Services**  

- **Purpose:** Each REST-based service includes **auto-generated Swagger documentation** to help developers and external integrators understand and test the APIs.

| Service             | Description                                                    |
| ------------------- | -------------------------------------------------------------- |
| **Auth Service**    | Endpoints for registration, login, logout, token validation    |
| **Quiz Service**    | Endpoints to create, read, and manage quizzes/questions        |
| **Session Service** | Endpoints for managing game sessions (create/join/leave/start) |

- **Why:** These Swagger docs are crucial for frontend integration and for testing APIs independently during development.

**3. `README.md` for Real-Time (WebSocket) Service**  

- **Purpose:** Documents how to **interact with the WebSocket server** (used for real-time multiplayer communication).  
- **Includes:**  
  - How to connect  
  - Event types (e.g., `join`, `next_question`, `start_session/end_session`)  
  - Example messages  
  - Error handling and connection lifecycle

# Weekly commitments

## Individual contribution of each participant

##### Ramazan Nazmiev

- Deadlock Fix & RabbitMQ Consumer Isolation
  
  - Fixed a critical deadlock caused by overlapping RabbitMQ queue consumers that processed the same event across multiple sessions.
  
  - Refactored ConsumeQuestionStart to create one queue and consumer per session, eliminating duplicate message handling and ensuring session isolation.
  
  - Cleaned up queue lifecycle: consumer tag generation, binding to session-specific routing keys, and proper teardown on session end to prevent stale consumers.

- Enhanced Test Coverage for Parallel Sessions
  
  - Updated integration tests to spawn multiple sessions in parallel, validating that messages (session start, question start, leaderboard, etc.) are dispatched independently.
  
  - Added assertions to catch race conditions and ensure clean teardown of websockets and RabbitMQ consumers after each session cycle.
  
  - Overall, tests now verify:
    
    - Single question per session start
    - Correct session/topic segregation
    - Absence of cross-session data contamination

- Redis Support & Thorough Testing
  
  - Introduced Redis-backed state storage for quiz progress:
    
    - SetSessionQuiz, GetSessionQuiz, SetQuestionIndex, RecordAnswer, GetAllAnswers, DeleteSession.
    - Implements TTL for session data and per-user answer hashes.
  
  - Added full Testcontainers-based integration tests (in redis package) to validate Redis operations, TTL logic, and cleanup behavior.
  
  - Ensures compatibility in both in-memory and containerized test environments.

     [Contribution](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/72)

##### Niyaz Gubaidullin

**Added `/healthz` Endpoint**

- Introduced a new HTTP endpoint `/healthz` to verify service health.
- The endpoint returns `200 OK` if:
  - The service is running,
  - RabbitMQ connection is healthy,
  - Redis connection is healthy.
- Returns `500` with error details if any check fails.

**Removed Waiting Users**

- Implemented logic to automatically remove users who are stuck in a "waiting for game" state.
- Helps prevent inactive or orphaned sessions and improves session management.

**Purpose**

- Improves monitoring and observability of the service.
- Enables better integration with load balancers, CI/CD pipelines, and orchestration tools.
- Enhances overall system stability by cleaning up unused user states.

    [Contribution](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/62)



##### Nurmukhammet Adagamov

**Development Environment:**

- Added `docker-compose` setup for frontend with hot reload (`npm start` + `Dockerfile.dev`)
- Implemented environment-aware API path constants (`constants/api.js`):
  - Direct service URLs for dev
  - Nginx-proxied paths (`/api` prefix) for prod
- Fixed CORS policy for session service

**CI/CD Pipeline:**

- Added workflow dispatch UI for manual job triggering
- Enhanced release branch support (`release**` pattern)
- Improved deploy logic:
  - Now runs on:
    - Push to `main` **OR**
    - Manual trigger with `deploy=true` on `main`
  - DockerHub push now works for manual triggers (previously only main pushes)

**Security Improvements:**

- Replaced hardcoded RabbitMQ secrets with `envsubst` for production
  - Kept existing dev setup unchanged
  - Secrets now injected during CI/CD deployment

    **Contributions:** [#68](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/68), [#73](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/73)

##### Ramil Aminov

**Cypress Integration for E2E Testing**

- Introduces Cypress end-to-end testing infrastructure to ensure critical user flows are properly validated. 

- The implementation includes full setup of Cypress with custom commands and test examples.

**Core Setup**

- Installed Cypress v14.5.1 and @testing-library/cypress

- Configured Cypress with custom project structure outside /app

- Added base configuration in cypress.config.js

- Implemented custom commands in support/commands.js

- Created global test hooks in support/e2e.js

 **Contributions:** [#63](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/63)

##### Dmitriy Lukiyanov

**WebSocket Improvements**

* Fully fixed all WebSocket connection issues.

* Added proper handling of WebSocket closure events to prevent silent disconnects.

* Ensures stable real-time updates across all flows.

**Authentication Flow**

* Removed mandatory authorization — users can now access the app without being forced to log in.

* Simplifies onboarding and demo experience while keeping optional auth in place.

**UI Enhancements**

* Updated button design on the Homepage for a more modern and consistent look.

* Improved answer variant rendering:
  
  * Students now see only the options relevant to them.
  
  * Admins are shown full control and visibility of choices.

 [Contribution](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/77)

## Plan for Next Week

**Image Support For Question**

- Add ability to send the image to frontend when send question payload.

- Show it on user side.

**Leaderboard Service Development**

* Design data structures and storage format (Redis/Postgres).

* Implement initial service skeleton and API endpoints for score updates and leaderboard retrieval.

* Integrate with RealTime service to receive final scores.

**Quiz CRUD Operations & Catalogue on Frontend**

- Implement Quiz List component to fetch and display all quizzes with metadata (title, description, number of questions).

- Create Quiz Detail view to show individual quiz data in read-only mode.

- Build Quiz Form component for creating new quizzes, including dynamic question inputs.

- Add functionality to edit existing quizzes by pre-filling Quiz Form with current data and submitting updates.

- Implement quiz deletion with confirmation modal.

- Develop Catalogue page combining quiz list with search, filtering (by tags/difficulty), and pagination or infinite scroll.

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
