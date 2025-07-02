---
title: "Week #2"
---

# **Week #2**

## Detailed Requirements Elaboration

- The UI for new pages such as “quiz catalog”, “connect to room”, “create room”, “waiting for players”, and “page with current question and answer options” has been created. Several of them have been laid out.

- Completed the core functionality of the Session and Real-Time backend services. The Session Service now supports creating new sessions, generating connection codes, handling participant joins, and communicating with the Real-Time Service via RabbitMQ. The initial implementation of the Real-Time Service enables session initialization and real-time participant management through WebSocket connections.

- Backend was transited to a modular microservices structure for improved scalability and maintainability. The system now separates authentication and quiz logic into independent services, backed by a shared core module for database models, schemas, and business logic. The update also includes automated database migrations, streamlined Docker orchestration, and general project cleanup.

## Project specific progress

### Frontend

- The UI for new pages such as “quiz catalog”, “connect to room”, “create room”, “waiting for players”, and “page with current question and answer options” has been created. 

- The `Joinig Room` and `Proceed Quiz` pages have been laid out. The HTTP page routes has been configured in `React`.

### Backend

* `Session Service` backend general functionality has been finished, such as *New session creation and its connection code generation*, *communication with _Real Time Service_ via* `RabbitMQ`, *joining new participants to the session and ephemeral token generation*.

* `Real Time Service` backend first part functionality has been added:
  
  * *Receiving the start_session event and its session code to prepare environment*
  
  * *Establishing the websocket connection and adding new participants that join the room*

* **Service Decoupling**: The `auth` and `quiz` functionalities are now independent FastAPI microservices.

* **Shared Core**: A new `shared` module was added, containing:
  
  * Unified SQLAlchemy ORM models (e.g., Users, Quizzes)
  
  * Pydantic schemas for consistent data validation
  
  * A reusable Unit of Work pattern and repository abstraction used across services

### DevOps

* Start PostgreSQL with healthchecks
  Apply migrations automatically before services start
  Install the shared module into each microservice container
  Adjusted service-specific Dockerfiles to support shared logic

# Weekly commitments

## Individual contribution of each participant

##### Ramazan Nazmiev

- Developed detailed [FlowChart](https://www.mermaidchart.com/app/projects/20d2e5e6-3ee0-4596-8a65-03a7d98870b3/diagrams/a86a8c3a-8e4a-47d3-8ad6-36a0bf6afdac/version/v0.1/edit) containing all project layers, microservices and storages that should be used and their connections (**IN-MVP services ONLY**).

- Developed detailed [Sequence Diagram](https://www.mermaidchart.com/app/projects/20d2e5e6-3ee0-4596-8a65-03a7d98870b3/diagrams/d9e83469-d539-481a-a965-0f79de4f9419/version/v0.1/edit) containing all processes flow and communication between services: Creating the room, joining it, and Loading the next question.

- **RabbitMQ Exchange Declarations**
  
  - Defined and initialized `session.events` topic exchange at service startup.
  - Ensures consistent messaging structure for inter-service communication.

- **RabbitMQ Event Consumption from Session Service**
  
  - Subscribed to and handled `session.start` and `session.end` events.
    - `session.start`: Prepares in-memory session structures and allows WebSocket connections to proceed.
    - `session.end`: Cleans up connections and data associated with the session.

- **WebSocket Endpoint and Connection Management**
  
  - All users (admins and participants) connect via a unified `/ws` WebSocket endpoint.
  - On connection:
    - Ephemeral token is passed via query parameter.
    - Token is verified and decoded to extract userID, sessionID, and role.
    - User is registered in in-memory structures: `map[sessionID][userID]*Conn`.
    - New session IDs are tracked dynamically as users connect.

- **Ephemeral Token Decoding for WS Auth**
  
  - JWT-based ephemeral tokens issued by the Session Service are verified during WS handshake.
  - Decoded token provides:
    - Session ID
    - User role (admin/participant)
    - User ID
  - Enables role-based message routing and secure access control for each user connection.

     [Contribution](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/16)



##### Niyaz Gubaidullin

* **Session Creation**
  
  * Generates a unique session ID (UUID).
  
  * Generates a 6-digit alphanumeric code to connect players.
  
  * Generates a token for the session administrator (includes nickname, session_code, expiration).
  
  * Saves session information in Redis under key: `session:{code}`.

* **New Member Code Verification**
  
  * Processes client requests containing a receipt code.
  
  * Checks the existence of the session in Redis.
  
  * Generates a JWT token for the player (includes session_code, nickname, expiration).

* **Server Startup**
  
  * Runs on `localhost:8000`.
  
  * Supports 3 GET endpoints:
    
    * `/validate` — verifies the new member's code.
    
    * `/create` — creates a new session.
    
    * `/next` — sends a request for the next question.

     [Contribution](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/14)



##### Nurmukhammet Adagamov

* **Microservices Split**: Separated `auth` and `quiz` into standalone FastAPI services.

* **Shared Module**: Introduced a `shared` package containing:
  
  * Centralized SQLAlchemy ORM models (Users, Quizzes, etc.)
  * Pydantic schemas for User and Quiz models
  * Implemented the Unit of Work pattern and repository layer for both services

* **Alembic Migrations**: Set up and configured Alembic for DB migrations in the shared module

* **Docker Improvements**:
  
  * Updated `docker-compose.yml` to:
    
    * Start PostgreSQL with healthchecks
    * Apply migrations automatically before services start
    * Install the shared module into each microservice container
  
  * Adjusted service-specific Dockerfiles to support shared logic

* **Miscellaneous**:
  
  * Cleaned up `.gitignore` to exclude virtual envs, **pycache**, and Python artifacts

    [Contribution](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/13)



##### Ramil Aminov

- **JoinGamePage**
  
  - Allows users to enter a quiz code provided by the quiz creator.
  - Includes styled input fields and buttons with a responsive layout.
  - Navigates to the nickname entry page using the entered code.

- **EnterNicknamePage**
  
  - Prompts users to enter their nickname after providing a valid quiz code.
  - Includes input validation and clean UI interactions.
  - On clicking "Play", navigates the user to the waiting game page.
    
    

   [Contribution](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/12)



##### Dmitriy Lukiyanov

- **Design Work in [Figma](https://www.figma.com/design/D82E6kH1Kquc3ImEO8IHto/InnoQuiz)**
  
  - The UI design is 90% complete.
  - All pages have been carefully planned to ensure visual consistency and user-friendly layouts.
  - Special attention was given to details such as button colors, spacing, and element placement.

- **Layout and UI Implementation**
  
  - Pages that are independent of backend functionality were prioritized to enable early UI/UX testing.
  - Backend-dependent pages have also been implemented and are ready for integration.
    
    

     [Contribution](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/15)

## Plan for Next Week

### Frontend (React)

#### Must Have

- [ ] Create Quiz Page
  
  - Form to select or create a quiz
  - Connect to Session Service to start a game

- [ ] Quiz Flow UI
  
  - Display questions from Session Service
  - Show timer, options, and progress

- [ ] Results Page
  
  - Display user score or performance
  - Option to restart or go back to lobby

#### Backend Integration

- [ ] Use Session Service API to manage game state
- [ ] Fetch sample quiz via Quiz Service API

### Go Services

#### Session Service

- [ ] Integrate with Redis to store session/game state
- [ ] Use RabbitMQ to communicate with Real-Time Service
- [ ] Fetch quiz data via Quiz Service API
- [ ] Provide API endpoints to:
  - Start session
  - Join session
  - Get current question
  - Submit answer

#### Real-Time Service

- [ ] Connect to Session Service via RabbitMQ
- [ ] Manage game loop
  - Receive quiz from Session
  - Emit questions and collect answers in real time
- [ ] Store live game state in Redis

### Python Services

#### Quiz Service

##### Must Have

- [ ] GET /quizzes/{id} – return full quiz data for session start

##### Nice to Have

- [ ] POST /quizzes – create a new quiz
- [ ] PUT /quizzes/{id} – update existing quiz
- [ ] DELETE /quizzes/{id} – delete a quiz
- [ ] GET /quizzes/search – search and filter quizzes
- [ ] POST /tags – manage tags for quizzes

### DevOps and Infrastructure

#### Redis and RabbitMQ

- [ ] Add Redis and RabbitMQ to docker-compose
- [ ] Add healthchecks and expose ports
- [ ] Ensure Go services connect via internal network

#### Microservices Integration

- [ ] Ensure Quiz Service is reachable from Session Service
- [ ] Enable communication between Real-Time Service and Session Service via RabbitMQ

#### NGINX Setup

- [ ] Add reverse proxy to route:
  - /api/auth/ → Auth Python service
  - /api/quiz/ → Quiz Python service
  - /api/session/ → Session Go service
  - /api/ws/ → Real-Time Go WebSocket service
- [ ] Configure CORS and fallback routing for frontend

### Final Checklist

- [ ] All MVP features implemented and integrated
- [ ] System health confirmed via docker-compose
- [ ] Manual QA of quiz flow (create, play, score)
- [ ] Internal demo ready before deadline

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
