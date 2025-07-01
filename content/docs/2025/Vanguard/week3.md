---
title: "Week #3"
---

# **Week #3**

## Implemented MVP features

# ✅ Completed MVP Features (GitHub Project #22)

### Quiz Management

- **Quiz Data Model & CRUD API**  
  - Mongo-backed quiz schema (title, questions/options, correct answers)  
  - Endpoints: `POST /quizz`, `GET /quizz`, `GET /quizz/{id}`, `PUT /quizz/{id}`, `DELETE /quizz/{id}`  
  - PRs: #13

### Session

- **Session Creation (`POST /sessions`)**  
  - Generates session UUID, unique join code, admin JWT, persisted in Redis  
- **Participant Join (`POST /join`)**  
  - Validates code, returns participant JWT  
  - PR: #16

### Real-Time WebSocket Service

- **WebSocket Endpoint (`/ws`)**  
  - JWT auth, connection tracking per session, broadcasting support  
  - PR: #16, #22
- **Session Start Consumer**  
  - Listens to RabbitMQ `session_started` 
  - PR: #16

### Frontend Game Flow

- **Participant Flow**  
  
  - “Join Game” → enter nickname → call `/join` → open WS → wait for `session_started` → show question    

- **Admin Flow**  
  
  - “Host Lobby” → select quiz → create session → display code → manage participants → start quiz  
  
  PRs: #36

### Infrastructure & DevOps

- **Dockerized Services**  
  - Dockerfiles and `docker-compose` for all backend/frontend services and infrastructure  
  - PRs: #116–#117  
- **Testing**  
  - GitHub Actions for test runs, builds, image pushes  
  - E2E integration tests simulate quiz flow  
  - PRs: #22  

### Documentation

- **Architecture & API Docs**  
  - Mermaid diagrams and OpenAPI specs  
  - PRs: #24

---

## 🧭 Functional User Journeys

### 1. Admin Quiz Workflow

Admin enters → crates room → selects quiz → shares the generated room code

### 2. Host Game Workflow

Admin selects quiz → clicks “Host Game” → `POST /sessions` → receives code and JWT  
Lobby displays code and live participant list (via WebSocket)

### 3. Participant Join Flow

Participant enters code + nickname → `POST /join` → receives JWT  
Connects to WS and waits for quiz start event

### 4. Quiz Start & Live Play

Admin clicks “Start Quiz” → backend publishes `session.start` → clients receive `session_started`  
Participants receive question → submit answers via WS  
Repeat until quiz ends



## Demonstration of the working MVP



## Internal demo

**Project:** Vanguard – Quiz Game Platform  
**Date:** End of Week 3  
**Audience:** Capstone team members and instructors

---

### ✅ MVP Features Demonstrated

| Area                  | Feature                                  | Status    |
| --------------------- | ---------------------------------------- | --------- |
| **Frontend**          | Quiz selection and join lobby UI         | Not ready |
|                       | Real-time question view + answer buttons | Not ready |
| **Session Service**   | Game session creation and state handling | ✅ Done    |
| **Real-Time Service** | Live question broadcasting & answer sync | ✅ Done    |
| **Quiz Service**      | Fetching quiz data for gameplay          | ✅ Done    |
| **Integration**       | Docker-based deployment, internal comms  | ✅ Done    |

---

### 🔁 Flow Walkthrough (Live Demo)

1. User enters
2. Creates or joins a quiz session
3. Session starts and questions appear live
4. Users answer questions in real time
5. Results are shown at the end of the quiz

---

### 🛠 Known Gaps / Next Focus

- Add authentication (JWT) to all services
- Redis caching and reconnect handling in Real-Time Service
- Deploy entire web app to production server
- Begin Leaderboard Service implementation

---

# Weekly commitments

## Individual contribution of each participant

##### Ramazan Nazmiev

###### 1. Overview

Introduce end-to-end integration tests covering:

- Session creation in Session Service
- Participant join via Session Service (receive JWT + WS endpoint)
- WebSocket connections to Real-Time Service using returned JWT
- Session start in Session Service → RabbitMQ event
- Real-Time Service consumes event and broadcasts to connected clients
- Clients receive “session started” notification over WS

###### 2. Key Refactoring

- **Config via env vars**: both services read `MQ_URL`, `REDIS_ADDR`, `JWT_SECRET_KEY`, `SESSION_SERVICE_HOST/PORT`, `REALTIME_HOST/PORT`.
- **Startup functions**: encapsulate service initialization in functions accepting `context.Context`, returning errors; avoid untestable `main()`.
- **WebSocket handler**: validate JWT correctly, thread-safe connection registry, broadcast logic on RabbitMQ events.
- **Session endpoints**: 
  - `POST /sessions`: create session, return admin JWT, session ID, WS endpoint.
  - `POST /join`: validate code, return participant JWT + WS endpoint.
- **Logging**: add concise structured logs around startup, connections, event publish/consume, broadcasts.

###### 3. Integration Test Implementation

- **Location**: `integration_tests/e2e_test.go` (with `//go:build integration`).
- **Dependencies**: use `testcontainers-go` to spin up:
  - RabbitMQ container (expose container port 5672 to random host port; load definitions).
  - Redis container (expose 6379).
- **Port mapping**: obtain actual host:port via `MappedPort` and pass via env (`MQ_URL`, `REDIS_ADDR`).
- **Service startup**:
  1. Set env vars for each service (host/port, MQ_URL, REDIS_ADDR, JWT_SECRET_KEY).
  2. Launch Real-Time Service in a goroutine; wait for WS readiness (poll `/ws?token=invalid`).
  3. Launch Session Service in a goroutine; wait for HTTP readiness (`/healthz`).
- **E2E flow**:
  1. `POST /sessions` → admin token, session ID, WS endpoint.
  2. `POST /join` twice → participant tokens + same WS endpoint.
  3. Dial WS for each participant with `?token=<jwt>`.
  4. Real-Time Service consumes and broadcasts; test reads from each WS connection within timeout and asserts expected JSON (e.g., `type: "session_started"`).
- **Cleanup**: close WS connections; terminate containers; cancel service contexts.

     [Contribution](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/22)

##### Niyaz Gubaidullin

* **Added unit tests**
  
  * Covering the key components of session creation and validation logic.
  
  * Verification of token generation, connection codes, and interaction with Redis.

* **Swagger Integration**
  
  * The swaggo/swag library is used to generate documentation.
  * Swagger UI is available by endpoint /swagger/index.html.
  * All available routes are documented with examples of requests and responses.

* **Changed endpoints**
  
  * /create → POST /sessions
  
  * /validate → POST /join
  
  * /next → POST /session/{id}/nextQuestion

* **Updated request and response schemes**
  
  * Added CreateSessionRequest, ValidateSessionRequest, SessionResponse, and other models.
  
  * Responses are now returned in a single format with status, message.

* **The approach to token generation has been updated**
  
  * Registered fields in JWT (exp, iat, iss) have been added.

     [Contribution](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/24)

##### Nurmukhammet Adagamov

**Summary**

Introduced the core functionality of the Quiz microservice and related DevOps improvements.

**Features**

- Full CRUD for quizzes
- Tag support for quiz creation, filtering, and listing with search support
- Filtering by visibility, tags, search, user ID
- S3 image upload support
- Integration tests for main flows and edge cases
- Docker Compose updated to use env vars
- `.env.example` added
- Basic Swagger docs and README

**Endpoints**

**Quizzes**

- `POST /`: create quiz
- `GET /{quiz_id}`: get quiz by ID (public or own)
- `PUT /{quiz_id}`: update quiz (owner only)
- `DELETE /{quiz_id}`: delete quiz (owner only)
- `GET /`: list quizzes (supports `public`, `mine`, `user_id`, `search`, `tag`, pagination)

**Images**

- `POST /images/upload`: upload image (returns S3 URL)
- `DELETE /images/?img_url={S3_URL_of_image}`: deletes image from S3 by it's URL

> Note: Auth not yet implemented; `user_id` passed as query param where needed.

    [Contribution](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/23)

##### Ramil Aminov

* - Integrated WebSocket communication with a Go backend using the Gorilla WebSocket library.
  - Established WebSocket connections from the frontend after a successful session initialization via REST API.
  - Created a session lifecycle:
    
        1. User selects a quiz from the available list.
        2. A session is started via the POST /api/session/start endpoint.
        3. Response includes metadata such as serverWsEndpoint, userId, and userType.
  - Configured session metadata storage in sessionStorage, including quizId, userId, and session token.
  - Dynamically connected to WebSocket using the endpoint returned from the API and attaching a JWT token as a query parameter.
  - Used useRef to persist WebSocket instance across component renders, ensuring controlled message sending and connection lifecycle.
  - Implemented message handlers (onopen, onmessage, onerror, onclose) for receiving real-time updates from the server.
  
   [Contribution](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/37)

##### Dmitriy Lukiyanov

* Complete responsive layout and structured markup for all application pages  
  
  - Dynamic rendering of questions, participants, and responses with real-time updates  
  - WebSocket integration for bidirectional, live client-server communication  
  - Real-time subscription to data streams without page reloads  
  - Full REST API integration for fetching, creating, updating, and deleting data  
  - Robust error handling and response parsing for reliable user interactions  
  - Seamless, dynamic, and interactive UI across all sections of the application
  
   [Contribution](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/36)
  
  ## Plan for Next Week

### 1. Authentication & Authorization (Python + Go + Frontend)

- **Implement basic JWT-based auth**  
  - Design user model and token flow: access token + refresh token.  
  - Integrate login/register and token refresh logic in Python service.  
  - Add middleware in Go services to validate tokens and extract user identity/role.  
  - Frontend: build login/register pages, store tokens securely, handle refresh automatically.  
  - Tests: integration checks for login/logout flows.

---

### 2. Go Backend Updates

- **Integrate auth into existing services**  
  
  - Update session and real-time services to require valid tokens and respect user roles.  
  - Adjust logic so user identity comes from the token instead of anonymous IDs.  
  - Ensure error handling when auth fails (e.g., reject unauthorized actions).

- **Redis caching and state sync in Real-Time service**  
  
  - Configure Redis client: store current session state (active question, timer, partial results).  
  - On service start or client reconnect, load state from Redis so sessions continue smoothly.  
  - Clean up cached state when a session ends.

- **Leaderboard functionality (basic)**  
  
  - Add or refine a component/service to accumulate and cache scores in Redis (e.g., sorted sets).  
  - Ensure Real-Time service updates and uses this data to broadcast ranking updates to clients.  
  - simple integration test with Redis.

---

### 3. Frontend Enhancements

- **WebSocket communication robustness**  
  
  - Enhance WS client logic: detect and recover from connection errors, attempt reconnect with backoff.  
  - Handle auth failures on WS (e.g., token expiry), redirecting users to login or re-join flows.  
  - Expose connection status in UI (e.g., “Reconnecting…”).

- **Auth pages and integration**  
  
  - Build login and registration interfaces; integrate with backend auth flows.  
  - After login, propagate user identity into session creation/join flows.  
  - Handle token storage (e.g., secure cookies or appropriate storage) and include tokens in API/WS calls.

- **Quiz management UI tied to auth**  
  
  - Update quiz creation/editing pages to require a logged-in user.  
  - Connect UI actions to the Python quiz service under authenticated context.  
  - Show errors or permissions feedback if user is not authorized.

---

### 4. Deployment

- **Prepare deployment for entire web app**  
  
  - Dockerize or package all components: Python service, Go services, frontend.  
  - Create or update deployment scripts/CI pipeline to build images and deploy to target server or environment.  
  - Configure environment variables and secrets (e.g., JWT secret, Redis/RabbitMQ addresses) securely.  
  - Ensure HTTPS (TLS) is set up (e.g., via reverse proxy).

- **Infrastructure readiness**  
  
  - Verify Redis and RabbitMQ are available in target environment and services can connect.  
  - Add health checks and minimal monitoring/logging to confirm services are healthy after deploy.

---

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
