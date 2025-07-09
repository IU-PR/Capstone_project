---
title: "Week #5"
---

# **Week #5**

## Main links

Figma - https://www.figma.com/design/ttrFjZlaz8jyuKQAzcHHkm/Untitled?node-id=0-1&p=f&t=c6lLIGjvjL40mOyM-0

Github - https://github.com/IU-Capstone-Project-2025/Online-game-7Red/tree/main

Trello - https://trello.com/b/D9ajdsG7/online-game-7red

Server - http://192.145.30.253:8080


## Feedback

### Sessions

We asked our friends to test our game. 7 people took the survey (https://forms.gle/C8rxDCWrHB2nxoey9). We had a personal session with 3 of them. At the same time, two of them have never played the physical version of the game, and only saw us do it 1-2 times. Each user played 2-3 games.

During this process, we realized that users were not very keen on using the rules before the game, and preferred to look at them during the game.
### Analyze

**Positive Aspects:**

- Design & Usability: Users appreciated the app's design, including the color gradient on the background and the intuitive placement of cards.

- Quick Access: Easy access to rules and in-app guides was highlighted as a strong point.

- Responsive Interface: The app's responsiveness and functionality were praised.

**Areas for Improvement:**

- Social Features: Users requested the ability to add friends, create permanent rooms, and send invites to prepared rooms (similar to Steam).

- Interaction Tools: Suggestions included adding emojis, quick reactions, or an in-game chat for better player interaction.

- Confirmation Prompts: A need for confirmation prompts (e.g., "Are you sure you want to exit?") to prevent accidental clicks.

**Bugs and Technical Issues:**

- Statistics Calculation: incorrect statistics calculation was reported.

- Full room: 5 players in 1 room

**Prioritized Issues:**

High Priority:

- https://trello.com/c/aRMvdPi1 (already done)

Medium Priority:

- https://trello.com/c/Q55XSzep

Low Priority:

- https://trello.com/c/yfRshZKt


## Iteration & Refinement

### Implemented features based on feedback

We have already managed to fix the biggest bugs:

- more than 5 people in a room

- improved email validation

- found out that the statistics bug is related to internet outages, and not a bug in the game

### Performance & Stability


**Completed:**

- The user can register by providing: Email (must be valid, uniqueness check);Password (minimum 6 characters, maximum 16); Username (unique, between 1 and 10 characters)

- The user can log in via: Email + password

- Passwords stored in hashed form 

- Server response time for authentication — no more than 10 seconds

- Buttons for game modes (Play with Friends, Play with AI)

- Navigation buttons for Statistics, Rules

- Data in achievements updates in real time

- Transition animations between sections take no more than 2 seconds

- The interface is expected to accommodate screen sizes between 8 and 17 inches

- Main menu load time — no more than 2 seconds

- Join via room ID ( length: 5 number) and password ( length: 5 number)

- AI must make a move within 5 seconds (to avoid delays)

- Rules Page include text description and examples

- Game state syncs every 30 ms

- Maximum latency between clients — 30 ms

- Each error must include clear error message (e.g., "Room is full (max 4 players)") and error code (for diagnostics)


**Remaining to achieve:**

- Session expires after 30 minutes of inactivity

- Data transmission only over HTTPS

- Buttons for game modes ( Play Online)

- Navigation buttons for Settings

- If the room is not filled within 20 minutes, it closes automatically

- if there are at least 2 players, the room starts after 60 seconds

- if during this time the room is filled with 4 players, it starts immediately

- if there are not enough players, an apology message is displayed and the player is transferred to the main menu

- The user can switch interface language (2 options: russian and english)

- The user can change his nickname, password or email

- If connection drops, the game attempts to reconnect for 20 seconds before declaring timeout-exit

- Error logs are stored on the server for 1 days

- Scalability: The system must support 50 concurrent players

### Documentation

#### 1. **Project Overview Documentation**

**README.md** 

  - **Purpose**: Serves as the primary entry point for understanding your project

  - **Contents**: Project description, setup instructions, Docker commands, gameplay instructions

  - **Why it's important**: First impression for developers, contributors, and users; provides essential setup and usage information

#### 2. **Change Management Documentation**

**CHANGELOG.md**

  - **Purpose**: Tracks all notable changes, features, bug fixes, and improvements over time

  - **Structure**: Organized by MVP versions with categorized sections (Features, Bug Fixes, Documentation, 🧪 Testing, etc.)

  - **Why it's essential**: Helps team members and stakeholders understand project evolution, track progress, and identify when specific features were added

#### 3. **License Documentation**

**LICENSE** (MIT License)

  - **Purpose**: Defines legal terms for project usage, distribution, and modification

  - **Why it's critical**: Protects intellectual property while allowing open-source collaboration

#### 4. **Technical Documentation**

**Database Documentation**:

  - db_creation.ipynb - Interactive notebook for database setup and testing

  - db_erd.png - Entity Relationship Diagram showing database structure

  - **Purpose**: Documents database architecture, setup procedures, and relationships between tables

#### 5. **Code Documentation  in ML**

**Python Docstrings**: ML modules (validate_model.py and Trainer.py)

  - **Purpose**: Explains function parameters, return values, and usage

**Inline code comments**

  - **Purpose**: Explains code details

#### 7. **Test Documentation**

**Test Files**: 

  - test_api_integration.py - API endpoint testing

  - test_unit.py - Unit tests for game logic

  - test_db.py - Database function testing

  - **Purpose**: Demonstrates expected behavior, validates functionality, and serves as usage examples

#### 8. **Configuration Documentation**

**requirements.txt** - Python dependency documentation

  - **Purpose**: describes the libraries and modules required for installation

### AI Model Refinement

At the moment, as planned, the game corresponds to the average level of the game, which was necessary for the current development of the project. In the future (MVP 2), it will be necessary to develop models for the complex and simple levels. There are two solutions for this, the first most likely solution will be to select the necessary parameters, optimize the training of the model and refine its structure. The second least likely option is only if for a difficult level of the game, it will be necessary to increase the complexity of the model, and if this cannot be done with the current Double DQN model, RNN/LSTM models can be used.

## Project specific progress

### Frontend

This week, functionality was added for the button to play with a bot, GamePage was redesigned to allow playing with a bot, the ability to play 3-4 players in GamePage was added, an alert dialog was added to display the rules in GamePage, a new page with all the rules was added — RulePage, a page with player achievements was added (updated thanks to the connection with the backend), a ResultPage page was added to display the game results, spectator-mode was added to GamePage, the icon for the web tab was changed, email validation was improved, based on a special library, the error "Room is full" was added when connecting to a room with four players, as well as a minor debug of the old functionality.

### Backend

The following work was done: endpoints for searching for random online opponents were studied and written, research was done on email verification (we can do this by creating another email service), endpoints were written for the settings page (changing nickname, avatar and password), the frontend and backend were fully connected when playing with a bot, debugging of games between 2,3,4 players and games with a bot was performed, the CI/CD and Dockerfiles was updated

### AI

This week, the AI integration process began. The model has been added to the backend. And a connection to the backup has been created. We also added a pre-saved model with adjusted parameters for the game at an intermediate level.

# Weekly commitments

## Individual contribution of each participant

**Palkina Sofia** – organized 3 discussion meetings (04.07 - meeting with TA Mary and after discussion of the amendments she proposed; 07.07 - regular midweek meeting to evaluate progress; 09.07 - discussion of plan for next week),collect feedback, do new backlog, redesign Figma,  update the CI/CD for ML and wrote this report

https://trello.com/c/zFzJoY5Y

https://trello.com/c/xawsGzOm

https://trello.com/c/rRSMoPSo

**Polina Kostikova** – wrote endpoints for searching for random online opponents, did research on email verification, wrote endpoints for the settings page (change nickname and password)

https://trello.com/c/qDemn9nK

https://trello.com/c/l8tFeh88

https://trello.com/c/ATG9PXsJ

**Lev Permiakov** – looking for ways to depict achievements, studied the work of the backend, began the logical implementation of the play again button, debug in the implementation of the AI model 

https://trello.com/c/pDxqBjgG

https://trello.com/c/4pCoURGG

https://trello.com/c/aRMvdPi1

**Arina Petuhova** – made endpoints for receiving, loading and deleting the player's avatar, participated in connecting the front with the back (game with a bot), debugged games between 2,3,4 players and games with a bot

https://trello.com/c/7kjRNcsr

https://trello.com/c/aRMvdPi1

https://trello.com/c/nbZKLOLy

**Amir Bairamov** – redesigned GamePage to allow playing with a bot, implemented a game for 3-4 players, implemented pages with rules, a page with player achievements and a page with game results, added spectator-mode, changed the application icon, debugged

https://trello.com/c/PMqao7Tl

https://trello.com/c/a1JLRjhC

https://trello.com/c/pYW2GGDA

https://trello.com/c/bfGN15nD

https://trello.com/c/7kjRNcsr

https://trello.com/c/pDxqBjgG

https://trello.com/c/aRMvdPi1


**All** - Play games and record bugs, write comments to the code

https://trello.com/c/xd09Xhew

https://trello.com/c/oqVQ2zVH

## Plan for Next Week

1. Finish and debug random player mode

2. Create setting page (without avatars)

3. Fix bugs found during feedback session

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).