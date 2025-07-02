---
title: "Week #4"
---

# **Week #4**

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



**CI logs** - https://drive.google.com/drive/folders/1HWuIwyp-_aQKcnsKuXFBWfVtbLBoRDX1

**Link to pipline** - 

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


**Links to CI/CD configuration files** - 

## Deployment

*Details about the deployment process, environment setup for staging environment*

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

Over the past week, the AI ​​reward system has been reworked and the parameters during training have been changed, the mask of acceptable choices at the end of each move has been changed, which has significantly increased the level of the AI ​​game, the MTS model running on the CPU has been integrated, it has been adapted to work in the DQN model environment, a function has been added that shows how the AI ​​works on specific data. Due to the very strong slowdown of the AI ​​training process, the MTS has been redesigned on the GPU, which has significantly increased the training speed and made it possible to create a higher-quality model and reduce the time of heavy operations that are used when working with the MTS.

## Weekly commitments

### Individual contribution of each participant

**Palkina Sofia** – organized 3 discussion meetings (20.06 - meeting with TA Mary and after discussion of the amendments she proposed; 23.06 - regular midweek meeting to evaluate progress; 25.06 - discussion of plan for next week), help with rule creation, do the implementation of CI/CD and wrote this report

https://trello.com/c/Nb1LzlsF

https://trello.com/c/pYW2GGDA


**Polina Kostikova** – wrote all the backend and frontend tests and created functions for tracking achievements

https://trello.com/c/FaYMMEld

https://trello.com/c/pDxqBjgG

**Lev Permiakov** – reworked the AI ​​reward system, changed the parameters during training and the mask of acceptable choices, integrated the MTS model, implemented the function of AI operation on specific data, made a validation test for ML, prepared rules and pictures for them

https://trello.com/c/dt8ZgOfR

https://trello.com/c/FaYMMEld

https://trello.com/c/pYW2GGDA

**Arina Petuhova** – made back-logic for the game with the bot and debugged errors, helped in creating hosting for the project on the server

https://trello.com/c/Mqy2qftL

https://trello.com/c/Nb1LzlsF

https://trello.com/c/dt8ZgOfR

**Amir Bairamov** – testing the application and fixing the bugs found

https://trello.com/c/Mqy2qftL

## Plan for Next Week

1. Screens for 3 and 4 players and make a page with game rules

2. Implement the whole work of AI mod

3. Collecting feedback from test users of our app


### Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).