---
title: "Week #6"

---

# **Week #6**

## Links

- **Deployment**: [try.it](https://tryit.selnastol.ru)
- **Design**: [Figma](https://www.figma.com/design/D82E6kH1Kquc3ImEO8IHto/InnoQuiz)
- **Demo**: [Video](https://drive.google.com/file/d/1dH8i_0Nj8AbUPCqEjWgJhVMHAH21dJU8/view)

## Final deliverables

### Project overview

The Quiz Platform is a scalable, microservice-based application for conducting interactive online quizzes in real time. It solves the problem of coordinating question delivery, answer collection, and scoring across potentially large numbers of simultaneous participants. Key implemented features include WebSocket-based real-time communication for question broadcasts and answer submissions, asynchronous service-to-service messaging via RabbitMQ to decouple components, and Redis-backed persistence of session state and participant answers to ensure resilience and horizontal scalability.

### Features

#### Functionality for Admin

* **User Registration & Login**  
  Register or log in securely with email and password.

* **Quiz Creation**  
  Create quizzes by entering a quiz title, adding multiple questions with multiple-choice options, and marking the correct option.

* **Session Creation**  
  Start a quiz session by selecting a quiz and generating a unique session code to share with participants.

* **Real-time Session Control**
  
  * Start the quiz session.
  
  * Manually trigger questions one by one.
  
  * End the session when the quiz is over.

* **Live Leaderboard View**  
  See the live leaderboard with:
  
  * Each participant’s total score.
  
  * Popular (most selected) answers for each question.

#### Functionality for Participants

* **Join Session**  
  Join an ongoing session using the session code provided by the organizer.

* **Live Question Display**  
  See questions in real time as the organizer triggers them.

* **Submit Answers**  
  Select and submit an answer to each question within the allowed time.

* **Leaderboard Updates**  
  After each question, view an updated leaderboard with:
  
  * Your current score.
  
  * Ranking compared to others.
  
  * Popular answers.

* **Answer Feedback**  
  Know whether your answer was correct after each question (based on leaderboard data).

### Tech stack

**Backend**  

- **Language:** Go 
- **Real‑Time:** Gorilla WebSocket  
- **Messaging:** RabbitMQ (`amqp091-go`)  
- **Storage & Cache:** Redis (`go-redis/v9`)  
- **Authentication:** JWT (`github.com/golang-jwt/jwt/v5`)  
- **API Docs:** Swagger/OpenAPI  
- **Monitoring:** Prometheus (`client_golang`), Grafana  
- **Testing:** Testcontainers, `stretchr/testify`  
- **Containerization:** Docker, Docker Compose  

**Frontend**  

- **Library:** React  
- **Services communication:** Native WebSocket API, REST API
- **Styling:** CSS   

**Infrastructure**  

- **Orchestration:** Docker Compose (local) 
- **CI/CD:** GitHub Actions, DockerHub
- **Monitoring:** Grafana, Promethus, Loki/Promtail 

### Setup instructions

#### 1. Clone the repository

```sh
git clone https://github.com/IU-Capstone-Project-2025/Vanguard.git
cd Vanguard
```

#### 2. Build and start the services

```sh
docker compose --env-file .env.dev.example up -d --build
```

or just make .env and launch as following

```sh
docker compose --env-file .env up -d --build
```

#### 3. Access the platform

- Link to the platform: http://localhost:3000

#### 4. Shut down the deployment

```sh
docker compose down
```



## Presentation draft

[Presentation](https://drive.google.com/file/d/1ra3mImyRRaYkeYb2n2zW_HlUO3VkqeLE/view?usp=sharing)



# Weekly commitments

## Individual contribution of each participant

##### Ramazan Nazmiev

- **Redis-backed QuizTracker**:  
  QuizTracker now uses Redis to persist quiz state and user answer data. This ensures that:
  
  - The service can restore state upon restart or redeployment.
  - Stateful information is no longer lost if the pod/container crashes.
  - The system can scale horizontally (multiple instances) without losing quiz consistency.

- **Quiz State and Answer Tracking**:
  
  - Each session’s quiz data (questions, current index, etc.) is stored under a Redis key:  
    `session:<sessionId>:quiz_state`
  - Each user's answers per session are stored as JSON-encoded entries in Redis hashes:`session:<sessionId>:user:<userId>:answers`

- **State Restoration**:
  
  - On service startup, `QuizTracker` attempts to restore all available session data from Redis.
  
  - Ensures continuity of active sessions even after service downtime.

- **Leaderboard retrieving:**
  
  - Linked the functionality of LeaderBoard Service to the RealTime Service:
    
    - After each question Admin receives Leaderboard, that shows calculated rating points for each user.
    
    - After each question Participant receiver question statistics (how many people have chosen each option), and the information about answer correctness.

    **Contributions:** [#89](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/89), [#91](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/91)

##### Niyaz Gubaidullin

## Update: LeaderBoard + WebSocket Enhancements

##### New:

- **Added LeaderBoard service**
  - New endpoint that returns users' scores.
  - Tracks top users by session/quiz.
  - Integration with Redis / database (depending on implementation).

##### Changes in SessionService:

- Updated WebSocket message format:
  - WS messages now include up-to-date information about users in a session.
  - Session user list is updated on connect/disconnect/user removal.

##### Tests:

- Added or updated integration tests for WebSocket connections and message delivery.
- Verifies correct user removal handling and broadcasting updates to remaining users.

    [Contribution](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/88)

##### Nurmukhammet Adagamov

###### New Features

- Added Prometheus `/metrics` endpoints for:  
  - Auth service (user registrations, logins, token operations)  
  - Quiz service (CRUD operations, image uploads)  
- Implemented Grafana dashboards for all services  
- Added centralized logging with Loki/Promtail  
- Configured alerting rules in Prometheus  

###### Improvements

- Standardized API prefixes (`/api` for all python services)  
- Enhanced logging middleware with:  
  - Path exclusions for monitoring endpoints  
  - Structured JSON logging  
  - Client IP tracking  

###### Fixes

- Resolved auth dependency import issues  
- Fixed metric collection for excluded paths  
- Improved error handling in logging middleware

    **Contributions:** [#92](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/92)

##### Ramil Aminov

- Auto-focus on input fields when pages load for better UX
- Transition to next page by "Enter" where actual

## Changes

- Added auto-focus functionality to input fields
- Updated related navigation logic
- Cypress end-to-end test that simulates a full interaction flow between an **Admin** and a **User** during session creation and joining.

 **Contributions:** [#85](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/85), [#87](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/87)

##### Dmitriy Lukiyanov

**Quiz Management**

- Implemented a full-featured quiz store with an improved design. Add a child components(like `QuizPreviewModal.jsx`), to enhance the experience.

- Built protected routes to secure access to quiz management pages.

- Developed a dynamic quiz constructor to create and edit quizzes.

**Game Process**

- Added a unique and consistent button style for use during live quizzes.

- Improved communication logic between WebSocket services.

- Fixed several bugs affecting gameplay behavior and responsiveness.

**Miscellaneous Updates**

- Enforced protected routes throughout the app for better access control.

- Polished overall UI with design improvements.

- Fixed minor visual and layout bugs.

 [Contribution](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/93)

## Plan for Next Week

- Fix existing bugs and test under high load

- Add leaderboard in frontend side

- Change the design parts

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
