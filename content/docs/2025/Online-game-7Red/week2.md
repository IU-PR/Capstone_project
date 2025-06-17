---
title: "Week #2"
---

# **Week #2**

## Detailed Requirements Elaboration

*This is your main task on this week, so please, make it detailed enough*

### Prioritized backlog

Link to backlog: https://trello.com/b/D9ajdsG7/online-game-7red

## Project specific progress

## Design

Regarding design work in Figma, the following was completed: A shared color palette was selected for the project, error types for sign_in_page and sign_up_page were defined, and the structure of main_menu_page was adjusted (the second button was removed, and icons for utility buttons were chosen). The statistics_page was finalized (with placeholders for achievement icons), the rules_page was completed (with a placeholder for rules), and the profile_page was polished (including additional windows for data editing). A game mode selection window was added to main_menu_page, while searching_timer_page and waiting_room_page (featuring two windows for ready/unready states) were also finalized. A template for game_room_page was created, along with dedicated windows for 2-player, 3-player, and 4-player setups, an example_of_gameplay, a button with a pop-up rules window, an exit warning dialog, and a results dialog. The result_page was also completed. Approximately 50% of the design was overhauled based on feedback and a more experienced review. Additionally, a Prototype view was built to test the application’s full functionality, after which the entire team conducted tests to identify errors and propose adjustments. All noted issues were subsequently addressed.

### Frontend  

Regarding frontend development, the following work was completed: The initial pages—welcome_page, sign_in_page, and sign_up_page—were implemented, and the connection between the frontend and backend was established using HTTP requests via API (the frontend utilized the http library and the Flutter framework). Successfully implemented requests included creating a new account and receiving backend responses such as "User registered successfully" or "Email already registered" (since the requests were fully functional, it was possible to receive "duplicate email" notifications).

### Backend

*...*

### AI

This week, a thorough investigation was conducted to determine the most suitable algorithms for the task at hand. Based on the research findings, 4 algorithms were identified as the optimal approaches. Parallel development of Deep Q-Networks (DQN) and Monte Carlo Tree Search (MCTS)  algorithms has been initiated  to explore their potential in practice. 

# Weekly commitments

## Individual contribution of each participant

**Palkina Sofia** – organized 2 discussion meetings (12.06 - meeting with TA Mary and after discussion of the amendments she proposed; 16.06 - discussion of plans taking into account the backlog and board rules), crate backlog, development of non-functional parts of the design (color palettes, etc.) and wrote this report

https://www.figma.com/design/ttrFjZlaz8jyuKQAzcHHkm/Untitled?node-id=0-1&p=f&t=n2vrlDM307fsX1Nt-0

https://trello.com/b/D9ajdsG7/online-game-7red


**Polina Kostikova** – 

**Lev Permiakov** – 

**Arina Petuhova** – 

**Amir Bairamov** – 

https://www.figma.com/design/ttrFjZlaz8jyuKQAzcHHkm/Untitled?node-id=0-1&p=f&t=n2vrlDM307fsX1Nt-0


## Plan for Next Week

1. Сreating the ability to connect to private game rooms, requiring the development of two frontend pages, implementation of database functions and establishment of backend connection components
2. Implementing the core gameplay for 2-4 players, including developing the main logic to comply with game rules, creating the frontend game room page, building the backend components for gameplay, adding victory/defeat popup windows (both frontend and backend), and implementing database update functions to track game progress and outcomes
3. Сreating a game modes selection page with non-functional prototype buttons for online matchmaking and bot gameplay, requiring frontend development and corresponding backend integration

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition
- [+] Run via docker-compose (described in the `README.md`)