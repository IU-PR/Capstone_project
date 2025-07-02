---
title: "Week #4"
---

# **Week #4**

## Testing and QA

*Summary of testing strategy and types of tests implemented.*

*Screenshots of test reports, CI logs, code coverage report.*

## CI/CD

*Description of CI/CD setup, tools used, and any challenges faced.*

Links to CI/CD configuration files


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

1. 

### Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).