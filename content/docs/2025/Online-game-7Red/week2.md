---
title: "Week #2"
---

# **Week #2**

## Detailed Requirements Elaboration

#### User Authentication

- Functional Requirements:

    - The user can register by providing: Email (must be valid, uniqueness check);Password (minimum 6 characters, maximum 10); Username (unique, between 1 and 10 characters)

    - The user can log in via: Email + password

    - Session expires after 30 minutes of inactivity

- Non-Functional Requirements:

    - Data transmission only over HTTPS

    - Passwords stored in hashed form 

    - Server response time for authentication — no more than 10 seconds

#### Main Menu Interface

- Functional Requirements:

    - Buttons for game modes (Play with Friends, Play Online, Play with AI)

    - Navigation buttons for Statistics, Rules, Settings

    - Transition animations between sections take no more than 2 seconds

- Non-Functional Requirements:

    - The interface is expected to accommodate screen sizes between 8 and 17 inches

    - Main menu load time — no more than 2 seconds

#### Game Modes

1. Play with Friends

- The user can:

    - Create a new room and invite friends by telling them the room ID amd password

    - Join via room ID ( length: 5 number) and password ( length: 5 number)

- If the room is not filled within 20 minutes, it closes automatically

2. Play Online (Matchmaking)

- Matchmaking wait time should not exceed 60 seconds during peak hours

3. Play with AI

- AI must make a move within 5 seconds (to avoid delays)

#### Statistics and Achievements

- Tracks:

    - Total games played (wins/losses, win rate)

    - Win/loss streaks

- Achievements are categorized as:

    - One-time (e.g., "First Win")

    - Progressive (e.g., "Win 5 games in a row")

- Data updates in real time

#### Rules Page

- Must include text description and examples

#### Settings Page

- The user can switch interface language (2 options: russian and english)

- The user can change his nikname, password or email

#### Real-Time Multiplayer Infrastructure

- Game state syncs every 30 ms

- Maximum latency between clients — 30 ms

- If connection drops, the game attempts to reconnect for 20 seconds before declaring timeout-exit

#### Error Handling

- Each error must include clear error message (e.g., "Room is full (max 4 players)") and error code (for diagnostics)

- Error logs are stored on the server for 1 days

#### Additional Requirements

- Scalability: The system must support 50 concurrent players

- Localization: RTL language support (if required)

## user stories



### Prioritized backlog

Link to backlog: https://trello.com/b/D9ajdsG7/online-game-7red

## Project specific progress

## Design

Regarding design work in Figma, the following was completed: A shared color palette was selected for the project, error types for sign_in_page and sign_up_page were defined, and the structure of main_menu_page was adjusted (the second button was removed, and icons for utility buttons were chosen). The statistics_page was finalized (with placeholders for achievement icons), the rules_page was completed (with a placeholder for rules), and the profile_page was polished (including additional windows for data editing). A game mode selection window was added to main_menu_page, while searching_timer_page and waiting_room_page (featuring two windows for ready/unready states) were also finalized. A template for game_room_page was created, along with dedicated windows for 2-player, 3-player, and 4-player setups, an example_of_gameplay, a button with a pop-up rules window, an exit warning dialog, and a results dialog. The result_page was also completed. Approximately 50% of the design was overhauled based on feedback and a more experienced review. Additionally, a Prototype view was built to test the application’s full functionality, after which the entire team conducted tests to identify errors and propose adjustments. All noted issues were subsequently addressed.

### Frontend  

Regarding frontend development, the following work was completed: The initial pages—welcome_page, sign_in_page, and sign_up_page—were implemented, and the connection between the frontend and backend was established using HTTP requests via API (the frontend utilized the http library and the Flutter framework). Successfully implemented requests included creating a new account and receiving backend responses such as "User registered successfully" or "Email already registered" (since the requests were fully functional, it was possible to receive "duplicate email" notifications).

### Backend

An automated CHANGELOG system was implemented to track project changes. Core functionality for game management was developed, including database operations for creating, deleting, and searching game rooms. After evaluating both desktop and web options, the project direction was finalized as a web application. The backend architecture was properly configured with initial API contracts established using Swagger for MVP endpoints, including several basic non-functional endpoints with mock data. Functional endpoints for user registration and authentication were implemented with full database integration. Successful backend-frontend connectivity was achieved through HTTP requests, enabling account creation workflows with proper response handling ("User registered successfully" or "Email already registered"). The system validates email uniqueness by checking against database records in real-time during registration attempts.

### AI

This week, a thorough investigation was conducted to determine the most suitable algorithms for the task at hand. Based on the research findings (https://trello.com/c/oAvDRkgy/8-define-the-type-of-algorithm-for-bot-need-research-and-summary#:~:text=data%20collection%20plan%3A-,ML%20Research,-Comments%20and%20activity), 4 algorithms were identified as the optimal approaches. Parallel development of Deep Q-Networks (DQN) and Monte Carlo Tree Search (MCTS)  algorithms has been initiated  to explore their potential in practice. 

# Weekly commitments

## Individual contribution of each participant

**Palkina Sofia** – organized 2 discussion meetings (12.06 - meeting with TA Mary and after discussion of the amendments she proposed; 16.06 - discussion of plans taking into account the backlog and board rules), crate backlog, development of non-functional parts of the design (color palettes, etc.), database operations for creating, deleting, and searching users and wrote this report

https://trello.com/c/qBfP0f4T

https://trello.com/c/a7IDHP1u


**Polina Kostikova** – create CHANGELOG, database operations for creating, deleting, and searching game rooms, defined the project type (do the research), established initial API contracts, create endpoints, connect  backend to frontend, functional endpoints for user registration and authentication

https://trello.com/c/r9LVNZPN

https://trello.com/c/Ygcpk6n6

https://trello.com/c/xvm6OXVK

https://trello.com/c/x3WiT45h

**Lev Permiakov** – crate backlog, determine the most suitable algorithms, start development of Deep Q-Networks (DQN)

https://trello.com/c/a7IDHP1u

https://github.com/IU-Capstone-Project-2025/Online-game-7Red/commit/1f8522fd45c6cac27c1a0b3a04719370e416332d

**Arina Petuhova** – determine the most suitable algorithms (do the re), developed basic vertion Monte Carlo Tree Search (MCTS) 

https://trello.com/c/oAvDRkgy

https://github.com/IU-Capstone-Project-2025/Online-game-7Red/commit/e21ccd78d0c71cac061d311029b2d91cd0e66566

**Amir Bairamov** – Сreated functional window designs in Figma(core UI elements and optimized component layouts), implemented prototype view , completed coding the entire frontend portion ( three full pages with all their interactive elements) and established stable connections with backend

https://trello.com/c/qBfP0f4T

https://trello.com/c/x3WiT45h


## Plan for Next Week

1. Сreating the ability to connect to private game rooms, requiring the development of two frontend pages, implementation of database functions and establishment of backend connection components
2. Implementing the core gameplay for 2-4 players, including developing the main logic to comply with game rules, creating the frontend game room page, building the backend components for gameplay, adding victory/defeat popup windows (both frontend and backend), and implementing database update functions to track game progress and outcomes
3. Сreating a game modes selection page with non-functional prototype buttons for online matchmaking and bot gameplay, requiring frontend development and corresponding backend integration
4. Сomplete development of Deep Q-Networks (DQN)

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition
- [+] Run via docker-compose (described in the `README.md`)