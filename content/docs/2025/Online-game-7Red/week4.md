---
title: "Week #4"
---

# **Week #4**

## Main links

Figma - https://www.figma.com/design/ttrFjZlaz8jyuKQAzcHHkm/Untitled?node-id=0-1&p=f&t=c6lLIGjvjL40mOyM-0

Github - https://github.com/IU-Capstone-Project-2025/Online-game-7Red/tree/main

Trello - https://trello.com/b/D9ajdsG7/online-game-7red

Server - http://192.145.30.253:8080


## Testing and QA

### Backend Testing

**Unit Tests** (test_unit.py) - fast execution, isolated from external dependencies, Tests edge cases and main logic

*Coverage:*

1. Game state initialization (test_initialize_deck_unique_cards)

2. Game rule implementations:

    - Most cards of one color rule (test_most_of_one_color_rule)

    - Highest card rule (test_highest_card_rule)

    - Most cards of one number rule (test_most_of_one_number_rule)


**API Integration Tests** (test_api_integration.py) - test API endpoints and their interactions, tests complete request/response cycles, verifies status codes and response formats, includes error case testing, uses unique identifiers to avoid test collisions

*Coverage:*

1. Authentication flows:

    - User signup (test_signup)

    - User signin (test_signin)

2. Game room management:

    - Room creation (test_signup_and_create_room)

    - Player ready state (test_player_is_ready)

    - Leaving rooms (test_leave_room)

**Widgets tests**(widget_test.dart) - cover the main UI components and user interactions of the Flutter frontend, verify the presence of key widgets, navigation between pages, and correct display of dynamic content, simulate user actions and check that the UI responds as expected.

Coverage:

1. Main menu:

    - START NEW GAME button: Ensures the main menu displays the "START NEW GAME" button.

    - Waiting room: Verifies that a player's name is shown in the waiting room. Checks that the app navigates to the game room page when all players are ready.

2. Game page: Confirms that the "SUBMIT" button appears when it is the player's turn. Ensures that all cards in the player's hand are rendered and visible.

3. General: Tests use widget pumping and navigation simulation to mimic real user flows. All tests check for correct widget presence and UI state after simulated actions.

**CI logs** - https://drive.google.com/drive/folders/1HWuIwyp-_aQKcnsKuXFBWfVtbLBoRDX1

**Link to pipeline** - https://drive.google.com/file/d/1D3ij9lNX1_S6gXeeOs-VMb4Hf-cDN_0k/view?usp=sharing

## CI/CD

### Tools Used

- GitHub Actions: For the entire CI/CD workflow

- Docker: Containerization of both frontend and backend

- Docker Compose: For service management in production

- PostgreSQL: Used when connecting to the NEON database

- Flutter: For frontend development

- FastAPI: For backend API development

- Pytest: For backend testing

### Pipeline Stages

1. Backend Testing

    - Sets up Python 3.11 environment

    - Installs dependencies from requirements.txt

    - Runs unit and API integration tests

    - Uses database secrets for test environment

2. Frontend Testing

    - Requires backend tests to pass first

    - Sets up Flutter 3.32.1 

    - Installs frontend dependencies

    - Runs widget tests

3. Build and Push Docker Images

    - Logs into Docker Hub using secrets

    - Builds and pushes both backend and frontend images with:

        - SHA-tagged versions (for traceability)

        - "latest" tags (for production)

    - Verifies images were successfully pushed

4. Deployment

    - Sets up SSH connection to VPS

    - Performs cleanup of previous deployment

    - Copies updated docker-compose.yml to server

    - Pulls new images and restarts services


### Configuration Files

1. docker-compose.yml

- Defines two services:

    - backend: Exposed on port 8000, uses database env file

    - frontend: Exposed on port 8080 (mapped to container's 80), depends on backend

2. requirements.txt

- Standard Python dependencies for FastAPI backend

- Includes testing and database dependencies

3. deploy.yml (GitHub Actions)


**Links to CI/CD configuration files** - https://github.com/IU-Capstone-Project-2025/Online-game-7Red/blob/main/requirements.txt

https://github.com/IU-Capstone-Project-2025/Online-game-7Red/blob/main/docker-compose.yml

https://github.com/IU-Capstone-Project-2025/Online-game-7Red/blob/main/.github/workflows/deploy.yml

### Challenges

**Docker Image Tag Mismatch**

- Pipeline builds images with commit-SHA tags, but deployment tries to pull latest tags, causing "manifest not found" errors.

**Environment Configuration Issues**

- .env file parsing errors (line number mismatch suggests hidden formatting problems).

- Missing DATABASE_URL and other PostgreSQL variables in CI/CD.

- GitHub Secrets not properly injected during testing.

**Flutter Project Errors**

- Incorrect directory navigation in GitHub Actions caused flutter pub get failures.

- Widget tests failed due to improper context setup for navigation/state management.

**Python Dependency Problems**

- Missing packages (sqlalchemy, databases, python-dotenv).

- Relative import issues and PYTHONPATH misconfiguration.

- Malformed requirements.txt formatting.

**Deployment Obstacles**

- Docker network conflict (deploy_default already exists).

- Backend database connection failure despite correct .env placement.

- SSH connection failures (incorrect keys/host verification).

- Permission issues with ~/deploy/database directory.

**General Warnings**

- Non-terminal SSH warnings during execution.

- depends_on not waiting for backend readiness.

- Using latest tags is not production-safe.


## Deployment

The deployment process for the environment involves several carefully defined steps to ensure that the application runs smoothly before it is moved into production. The staging environment closely mirrors the production environment and can be used to test new features, bug fixes, and configuration changes.

### Server Specifications

The staging server is VPS provisioned with the following specifications:

- 1 vCPU, which offers a single virtual processor core 

- 1 GB of DDR4 ECC RAM

- 20 GB SSD storage

- 100 Mbps unlimited bandwidth, which ensures sufficient network speed for accessing resources and deploying updates.

- KVM virtualization, which allows full virtualization with dedicated kernel support, improving isolation and performance.

- The server runs on a Linux operating system, offering stability and compatibility with various deployment tools.

### Deployment Process

**Access and Authentication**

Secure shell (SSH) access is configured to allow secure remote login. 

**System Preparation**

The Linux system is updated to ensure all packages and dependencies are current. Essential tools such as Git, Docker, Docker Compose, and YAML interpreters are installed.

**Environment Configuration**

Environment variables are defined to distinguish between development, staging, and production settings. These include database credentials, API keys, and application-specific configurations.

**Cloning the Repository**

The application source code is cloned from the version control system (GitHub) into the server. The branch used is main.

**Building the Application**

Any necessary build steps, such as compiling code, installing dependencies, or bundling frontend assets, are executed using defined commands or scripts.

**Using Docker**

According to the deploy.yml file, Docker Compose is used to manage services. Containers are built and started in detached mode. This ensures that all required services (e.g., web server, application backend, and database) are started together with defined configurations.

**Configuration and Volume Setup**

Docker volumes are used for persistent storage. Network settings, environment files, and mounted volumes are configured to ensure proper communication between containers.

**Rollback Plan**

If any issues arise, a rollback mechanism is in place. Previous stable container images or Git commits can be redeployed quickly.

## Vibe Check

| Team Member | Start of the week | Description   | End of the week  | Description   |
|-------------|-------------------|---------------|------------------|---------------|
| Palkina Sofia     | 4/5 | Overall everything is fine | 3/5 | Tired after ci/cd |
| Polina Kostikova  | 5/5 | I'm happy | 5/5 | I'm happy |
| Lev Permiakov     | 3/5 | Tired of the same actions when writing a neural network | 5/5 | I'm fine |
| Arina Petuhova    | 5/5 | Everything is great | 3/5 | Big assessments started in other subject |
| Amir Bairamov     | 2/5 | I'm very tired, but I'm glad I finished mvp | 4/5 | I had a little rest, but then big assessments started in other subjects |

Having received different responses from the participants, we partially restructured the workload during this week.

## Project specific progress

### Frontend

The size of widgets on pages has been normalized, an animation timer has been added to visually regulate the order of turns between players, email validation has been added during registration, the “Ready” button in the waiting room has been fixed, the error display for incorrect connection to the room has been fixed, new http requests have been added to exit the Game Room, error alerts have been added to control the player’s connection to a room with a game running inside it or to a room where a person is already present, a template has been added for the page with the result, a file has been added to switch the mode between localhost for working in Docker and ip for working on the server.

### Backend

The following work was done: wrote tests for critical backend logic and frontend components (unit tests and widget tests), wrote tests for API endpoints (including basic end-to-end tests), wrote validation function for future testing of ml, created fully working functions for tracking achievements (namely: 5 wins in a row, 7 days of logging into the game in a row, and 3 wins over a bot). Logic for playing with a bot has appeared (it includes accepting a player's move, checking the player's move, sending a response from the bot - if the bot has moved correctly, then the game continues and the player moves again). In addition, the project has a full-fledged CI/CD with deployment to a separate 24/7-worked VPS server.

### AI

Over the past week, the AI ​​reward system has been reworked and the parameters during training have been changed, the mask of acceptable choices at the end of each move has been changed, which has significantly increased the level of the AI ​​game, the MCTS model running on the CPU has been integrated, it has been adapted to work in the DQN model environment, a function has been added that shows how the AI ​​works on specific data. Due to the very strong slowdown of the AI ​​training process, the MCTS has been redesigned on the GPU, which has significantly increased the training speed and made it possible to create a higher-quality model and reduce the time of heavy operations that are used when working with the MCTS.

## Weekly commitments

### Individual contribution of each participant

**Palkina Sofia** – organized 3 discussion meetings (20.06 - meeting with TA Mary and after discussion of the amendments she proposed; 23.06 - regular midweek meeting to evaluate progress; 25.06 - discussion of plan for next week), help with rule creation, do the implementation of CI/CD and wrote this report

https://trello.com/c/Nb1LzlsF

https://trello.com/c/pYW2GGDA


**Polina Kostikova** – wrote all the backend and frontend tests and created functions for tracking achievements

https://trello.com/c/FaYMMEld

https://trello.com/c/pDxqBjgG

**Lev Permiakov** – reworked the AI ​​reward system, changed the parameters during training and the mask of acceptable choices, integrated the MCTS model, implemented the function of AI operation on specific data, made a validation test for ML, prepared rules and pictures for them

https://trello.com/c/dt8ZgOfR

https://trello.com/c/FaYMMEld

https://trello.com/c/pYW2GGDA

**Arina Petuhova** – made back-logic for the game with the bot and debugged errors, helped in creating hosting for the project on the server

https://trello.com/c/Mqy2qftL

https://trello.com/c/Nb1LzlsF

https://trello.com/c/dt8ZgOfR

**Amir Bairamov** – testing the application and fixing the bugs found, add the *** in password

https://trello.com/c/Mqy2qftL

## Plan for Next Week

1. Screens for 3 and 4 players and make a page with game rules

2. Implement the whole work of AI mod

3. Collecting feedback from test users of our app


### Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).