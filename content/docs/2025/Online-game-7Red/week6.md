---
title: "Week #6"
---

# **Week #6**

## Links

- **Deployment**:  [https://7red.ru](https://7red.ru)

- **API Docs**: [https://7red.ru/api/docs](https://7red.ru/api/docs)

- **Design**: [https://www.figma.com](https://www.figma.com/design/ttrFjZlaz8jyuKQAzcHHkm/Untitled?node-id=0-1&p=f&t=c6lLIGjvjL40mOyM-0)

- **Demo**: [https://drive.google.com](https://drive.google.com/drive/folders/19T_W_HOcX-3KzbpjSRU0x3DtEXiVTfmK?usp=sharing)

- **Github** - [https://github.com](https://github.com/IU-Capstone-Project-2025/Online-game-7Red/tree/main)

- **Trello** - [https://trello.com](https://trello.com/b/D9ajdsG7/online-game-7red)

## Final deliverables

### Project overview

Traditional card games like "7Red" are culturally significant but often lack modern digital representations. Players currently have no reliable way to play 7Red online with friends, track their progress, or compete against others globally. The absence of online versions limits the game’s exposure and playability, especially during times when in-person gatherings are not feasible.

This project aims to solve these problems by:


- Digitizing "7Red" with faithful adherence to its rules

- Enabling multiplayer capabilities, including friend-based private rooms

- Creating a persistent ecosystem with account tracking, in-game statistics, and achievements

- Providing options for solo play against AI when other players are not available 

### Features

The application includes the following core components:

1) User Authentication: Secure login and registration system to manage individual player accounts

2) Main Menu Interface: A central hub for users to access game modes, rules, settings, and statistics

3) Game Modes:

    - Play with Friends: Create and join private game rooms using custom IDs

    - Play Online: Match with random players through a smart matchmaking system

    - Play with AI: Option to play against computer-controlled opponents

4) Statistics and Achievements Page: Tracks wins, losses, game history, and unlockable achievements to enhance engagement and competition

5) Rules Page: Provides users with clear instructions and gameplay rules

6) Settings Page: Allows users to update profile data, change their avatar, and switch languages(will be completed by 21.07)

7) Real-Time Multiplayer Infrastructure: A database system to store user accounts and manage the state of live games, ensuring synchronization across devices

8) Error Handling and UI Feedback: Friendly error messages and loading states


### Tech stack

**Backend (Python)**

- Framework: FastAPI (async)

- Database: PostgreSQL + SQLAlchemy (asyncpg)

- Auth: JWT + bcrypt

- Real-time: WebSockets

- Libraries: Pydantic, httpx, Pillow

**Frontend (Flutter)**

- Framework: Flutter 3.8.1+

**AI (PyTorch)**

- Model: DQN (Deep Q-Network)

- Training: C++ game simulations → NumPy/PyTorch

**Dev Tools**

- Containerization: Docker + Docker Compose

- Testing: pytest

- Docs: OpenAPI/Swagger

- Versioning: Git

### Setup instructions

#### 1. **Clone the Repository**

https://github.com/IU-Capstone-Project-2025/Online-game-7Red.git

#### 2. **Prerequisites Installation**

Ensure you have the following installed on your system:

- **Docker** and **Docker Compose** (required for containerized deployment)

- **Python 3.8+** (for local backend development)

- **Flutter SDK** (for local frontend development)

- **Git** (for version control)

#### 3. **Environment Configuration**

 Copy the environment template and edit .env file with your configuration

Configure the following environment variables in .env:
- `PROJECT_ID`: Your project identifier
- `DB_USER`: Database username
- `DB_PASS`: Database password
- `BRANCH_ID`: Branch identifier
- `DATABASE_URL`: Complete database connection string
- `WS_URL`: WebSocket URL (`ws://localhost:8080/api` for local development)
- `SERVER_PW`: Server password

#### 4. Quick Start with Docker

**Option A**: Using Pre-built Images from DockerHub spalkkina/7red. Build and start all services with  `docker-compose up --build`

**Option B**: Local Development Build. Use the local development configuration
`docker-compose -f docker-compose.local.yml up --build`


#### 5. **Quick Start with access the Application (Recommended)**
- **Frontend**: [http://7red.ru](http://7red.ru)
- **Backend API Documentation**: [http://7red.ru/api/docs](http://7red.ru/api/docs)
- **Alternative API Documentation**: [http://7red.ru/api/redoc](http://7red.ru/api/redoc)

#### 6. **Testing the Application**

**For Local testing** - Open browser at [http://localhost:8080](http://localhost:8080)

**For Application testing** - Open browser at [http://7red.ru](http://7red.ru)

**For Multiplayer Testing:**
1. Open 2-4 browser tabs 
2. Create different accounts in each tab (Sign In/Sign Up)
3. From one account: Create private room (Start new game → Create private room)
4. From other accounts: Join using room ID and password (Start new game → Connect private room)
5. Click "Get Ready" button in each tab
6. Start playing by dragging cards and submitting moves

**For  Bot Testing:**
1. Open browser
2. Log in to your account
3. Select "Start new game → Vs Bot"
4. Play against the AI opponent

#### 9. **Development Tools**
- **Logs**: Monitor Docker logs with `docker-compose logs -f`

#### 10. **Stopping the Application**
 Stop Docker containers `docker-compose down -v`

## Presentation draft

[Presentation draft](https://docs.google.com/presentation/d/1m6bFVIICAVK5sPH7FYlUO_kWTxh5fU1Lt_GCO1eaT2s/edit?usp=sharing)

## Project specific progress

### Frontend

Made an animated window for online search. Added the ability to change the name, mail and login using terminal windows. Added a button to confirm the exit from the account. Changed the display of data in the online room. Added time before the player to view the damage definition. Fixed the display of the animated timer in GameRoom. Changed the size of widgets in GameRoom. Started creating a localization (ready to change the language in the settings and MainMenuPage)

### Backend
The following work was done:
- debugged online player search (rooms are created if at least 2 people are looking for opponents, other people join these rooms, if no players are found within a minute, the user is thrown out of the online search)

- deletion of users from the database after passing the tests was added to the integration tests

- a file for localization was written (change of languages: Russian and English)

- web sockets were studied for further rewriting of the project on them

- For the computer opponent, the centralized launch has been rewritten (so that only one bot model is created for several games and fewer resources are used)

- Logs have been rewritten and automatically saved to files on the server

- Database documentation has been updated

### AI

The development of the model for mvp2 (bot difficulty level 2) has begun. Various parameters of the model have been studied, the increase of layers has been tested, the change of existing parameters has not resulted in a significant increase in the level of the game, in connection with which it was decided to try another approach, some parameters have been removed and some new ones have been added.


# Weekly commitments

## Individual contribution of each participant

**Palkina Sofia** – organized 3 discussion meetings (11.07 - meeting with TA Mary and after discussion of the amendments she proposed; 14.07 - regular midweek meeting to evaluate progress; 16.07 - discussion of plan for next week), transferred the server to https and adapted the application code to these changes and wrote this report

https://trello.com/c/qLlTQjXo

**Polina Kostikova** – debugged online player search, fixed integration tests, wrote a file for localization, studied websockets

https://trello.com/c/EmA1iBku

https://trello.com/c/oK65JMcS

https://trello.com/c/7gQis62u

**Lev Permiakov** – start the development of the model for mvp2 (bot difficulty level 2)

https://trello.com/c/EhzsXR2N

**Arina Petuhova** – centralized the bot for several games, rewrote logs on the server, updated database documentation, fixed bugs

https://trello.com/c/Jwrj9iNb

https://trello.com/c/EmA1iBku

**Amir Bairamov** – Made a window for online search of opponents, finished the settings, confirmation of exit from the account, debug, started creating localization

https://trello.com/c/EmA1iBku

https://trello.com/c/Q55XSzep

https://trello.com/c/l8tFeh88

https://trello.com/c/ATG9PXsJ

https://trello.com/c/oK65JMcS

## Plan for Next Week

1. Final version of presentation slides

2. Finalize language mod

3. Add the ability to change avatars

4. Rehearse the presentation and demo multiple times.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).
