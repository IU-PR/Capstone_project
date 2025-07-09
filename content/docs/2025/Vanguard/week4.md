---
title: "Week #4"

---

# **Week #4**

## Testing and QA

Our testing strategy focuses on ensuring the reliability and correctness of real-time ans session sessions handling and WebSocket communication. We've implemented:

* **Unit tests** for core logic and message-handling functions.

* **Integration tests** covering interactions of services fully, including storages and other external tools usage.

* **End-to-end tests** simulating full user flows betwen several services (host starts session, users join, answer questions, and leaderboard is generated).

This layered approach ensures each component works individually and together under real conditions.

### Evidence of test execution

* All services passed integration tests in CI pipeline
* Python services: `pytest` with 85%+ coverage
* Go services: `go test -integration` with testcontainers
* Screenshots attached:   
  ![Test Results](https://github.com/IU-Capstone-Project-2025/Vanguard/blob/report-images/report_assets/test_results.jpg?raw=true)  
  ![Coverage Report](https://github.com/IU-Capstone-Project-2025/Vanguard/blob/report-images/report_assets/coverage_report.jpg?raw=true)

## CI/CD

**Implemented modular CI/CD with:**

- Separate workflows for each service (auth, quiz, real-time, session, frontend, migrations)
- GitHub Actions with Docker build/test/push
- Automatic triggers on path changes
- Artifact passing between jobs

**Challenges Solved**:

- Fixed port conflicts between services
- Resolved certificate generation issues
- Configured proper test database setup

### Links to CI/CD configuration files

- [Main workflow](https://github.com/IU-Capstone-Project-2025/Vanguard/blob/ci-pipeline/.github/workflows/main.yml)
- [Frontend workflow](https://github.com/IU-Capstone-Project-2025/Vanguard/blob/ci-pipeline/.github/workflows/frontend.yml)
- [Auth service workflow](https://github.com/IU-Capstone-Project-2025/Vanguard/blob/ci-pipeline/.github/workflows/auth-service.yml)
- [Quiz service workflow](https://github.com/IU-Capstone-Project-2025/Vanguard/blob/ci-pipeline/.github/workflows/quiz-service.yml)
- [Real-time service workflow](https://github.com/IU-Capstone-Project-2025/Vanguard/blob/ci-pipeline/.github/workflows/real-time-service.yml)
- [Session service workflow](https://github.com/IU-Capstone-Project-2025/Vanguard/blob/ci-pipeline/.github/workflows/session-service.yml)

## Deployment

### Production

**Manually deployed via:**

```bash
./setup.sh  # Handles certificates and initial setup
docker compose -f docker-compose.prod.yaml up -d
```

**Link to deployed project:** [tryit.selnastol.ru](tryit.selnastol.ru)

## Vibe Check

The team is making solid progress, with most planned features advancing steadily. The only roadblock is that backend development is moving slower than expected, creating minor integration delays. Due to this small problem, the frontend team is forced to complete their tasks in a short-period time. Despite this, communication is effective, and team dynamics are positive. Agreed to improve backend task distribution and maintain close coordination to stay on track.

# Weekly commitments

## Individual contribution of each participant

##### Ramazan Nazmiev

**1. WebSocket Communication Logic (Real Time Service)**

- Implemented full WebSocket-based interaction between session host (admin) and participants.
- Sent `question` payload to the admin when a new question is triggered by them.
- Handled participant answers: received responses, validated correctness, and tracked answers internally.
- Sent per-user feedback messages with correctness information.
- Broadcasted a `game_start` message when the host starts the quiz session.
- Implemented broadcasting of a boilerplate `leaderboard` message to all participants after the session ends.

**2. WebSocket Endpoint Documentation**

- Wrote and formatted `real_time/docs/README.md` documentation describing:
  - When and how the WebSocket endpoint should be used.
  - Message types for both admin and participant flows.
  - Expected request and response structures for real-time quiz interaction.
  - Sequence of message exchanges during a session.

**3. Testing**

- Updated and extended integration tests to validate:
  
  - End-to-end WS interaction between host and participants.
  - Message dispatching over RabbitMQ and proper synchronization.
  - Correct handling of user answers and feedback.

- Successfully executed an e2e flow test covering:
  
  - Session creation and quiz start.
  - Question lifecycle and participant response handling.
  - Completion of session and leaderboard broadcast.

     [Contribution](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/58)

##### Niyaz Gubaidullin

* ###### Store and Retrieve Session Players
  
  **Added**
  
  - `AddPlayerToSession(sessionCode, playerName)` — adds a player to a Redis set based on the session code.
  - `GetPlayersForSession(sessionCode)` — retrieves all players for a given session.
  - Players are stored in Redis under the key format: `session:<code>:players`.
  - 📡 **WebSocket connection**: Added a WebSocket endpoint that streams player names to the frontend in real time.
    - When a player connects, they receive the full list of existing player names in the session.
    - As new players join, the frontend receives real-time updates with the new names.
  
  **Example**
  
  ```redis
  SADD session:ABC123:players "Alice"
  SMEMBERS session:ABC123:players
  ```
  
   **WebSocket Behavior**
  
  - on connection
  
  ```json
  { "type": "players_list", "players": ["Alice", "Bob"]}
  ```
  
  **When a new player joins:**
  
  ```json
  { "type": "new_player", "name": ["Charlie"]}
  ```
  
       Contribution: [#47](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/47)

* ###### Add Endpoint to Check If Session Code Exists
  
  **Changes**
  
  - Added a new handler to check the existence of a session code.  
  - Integrated the endpoint into the routing layer.  
  - Added basic validation and error handling.  
  - Updated relevant models and service logic as needed.  
  
  **Usage**
  **Endpoint: /sessionis/{id}/validate**
  **Path Parameters:**
  
  - `code` — The session code to be checked.
  
  **Responses:**
  
  - `200 OK` – The session exists.
  - `404 Not Found` – No session with the given code.
  - `500 Internal Server Error` – Unexpected error.
  
  Contribution: [#52](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/52)
  Contribution: [#57](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/57)

##### Nurmukhammet Adagamov

**Description:**  
This PR introduces a dedicated Auth service backed by PostgreSQL that handles user registration, login, token issuance, token refresh, and token revocation and solves #42. Key changes:

- **Database**  
  
  - Added `refresh_tokens` table (with `token`, `user_id`, `user_agent`, `ip_address`, `expires_at`, `revoked` flag).  
  - Indexed `user_id` and `expires_at` for performance.

- **Models & Schemas**  
  
  - `UserCreate`, `UserLogin`, `TokenResponse`, `UserResponse`, `UpdateProfile`, `RefreshTokenRequest`.  
  - SQLAlchemy model  `RefreshToken`.

- **Repositories**  
  
  - `RefreshTokenRepository` (`create_token`, `get_token`, `revoke`, `revoke_all_for_user`).

- **Service Layer** (`AuthService`)  
  
  - Password hashing/verification via bcrypt.  
  - JWT access tokens with `jti` claim.  
  - Refresh token issuance, storage, expiration check, revocation.  
  - Endpoints: `/register`, `/login`, `/refresh`, `/me`, `/me (PUT)`, `/logout`, `/logout/all`.

- **API Endpoints & Docs**  
  
  - Full FastAPI router with summaries, descriptions, and response schemas.  
  - Centralized exception handling with custom exceptions mapped to HTTP status codes.

- **Tests**  
  
  - Integration tests covering happy paths and edge cases (duplicate registration, invalid credentials, token refresh & revocation).
  - Fixed integration tests for quiz service to consider authorization

- **DevOps**  
  
  - Alembic migration for `refresh_tokens` includes `revoked` column and indexes.  
  - Docker Compose fixes for env vars

    [Contribution](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/46)

##### Ramil Aminov

- Added login form with input fields and submit button

- Added viewing players on user's and admin's screen

- Implemented WebSocket support for receiving player data from the Session Service.
  
  - On connection, the client establishes a WebSocket session using a provided token.
  
  - The server sends:
    
    - A full list of player names on initial connection (as a string array).
    - Subsequent messages with new player names (as single-element arrays).
  
  - Incoming names are parsed from JSON and used to dynamically update the players state.

 **Contributions:** [#49](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/49), [#54](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/54), [#56](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/56)

##### Dmitriy Lukiyanov

* **Authorization**
  
  - Added `ProtectedComponent` to protect routes and ensure that only authenticated users can access certain pages.
  - Centralized authentication logic for route-level access control.
  - Seamless redirection for unauthenticated users.
  
  **WebSocket Context**
  
  - Introduced **WebSocket context providers** to maintain WebSocket connections across route changes.
  - Prevents unnecessary reconnects when navigating between pages.
  - Simplifies socket management and improves real-time feature reliability.
  
  **Bug Fixes**
  
  | Bug                   | Description                                                                                           |
  | --------------------- | ----------------------------------------------------------------------------------------------------- |
  | `null-session-code`   | Fixed issue where the session code could randomly become `null` on reload or during reconnection.     |
  | Cookies bug           | Resolved incorrect handling of cookies during login and logout, ensuring proper session persistence.  |
  | API communication bug | Fixed broken API interactions caused by improper headers, token propagation, or serialization issues. |
  
   [Contribution](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/60)

## Plan for Next Week

* **Start Leaderboard Service Development**
  
  * Design data structures and storage format (Redis/Postgres).
  
  * Implement initial service skeleton and API endpoints for score updates and leaderboard retrieval.
  
  * Integrate with RealTime service to receive final scores.

* **Design Updates**
  
  * Review and refactor UI components where needed based on team feedback.
  
  * Align frontend display with updated backend response formats (e.g., updated leaderboard, new game states).

* **Real-Condition Testing of Quiz Games**
  
  * Conduct simulated multiplayer sessions involving both admin and users.
  
  * Monitor behavior of question flow, answer submission, and result broadcasting.
  
  * Track edge cases like unexpected disconnects or race conditions in answers.

* **Bug Fixing & Error Handling**
  
  * Backend: improve resilience (e.g., panic recovery, WebSocket timeout handling, Redis availability).
  
  * Frontend: fix unhandled UI states, incorrect message rendering, or sync issues.
  
  * Prioritize known issues raised during testing and retrospective review.

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
