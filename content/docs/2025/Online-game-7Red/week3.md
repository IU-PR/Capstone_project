---
title: "Week #3"
---

# **Week #3**

## Implemented MVP features

This is the Minimum Viable Product focused on launching the essential mechanics of the game:

- User Authentication: Basic sign-up and sign-in functionality

- Private Game Rooms: Players can create and join private rooms using a unique room ID and password to play with friends, see the list of players in the room

- Game Session Implementation: Once the game starts, the core gameplay loop will be fully functional. This includes turn-based mechanics, player interactions, and enforcing the game’s basic rules

## User journey

- Registration / Login

    1. Opens the application → sees the login screen (Sign In / Sign Up)

    2. Registers or logs into an account

    3. After successful authorization, gets to the main lobby

- Main lobby

    4. Press "Start game" → a menu with 4 options opens: create a private room (working button), connect to a private room (working button), find an opponent (stub), play with a bot (stub)

    5. Select "Create a private room" -> The system generates a Room ID and password

    6. Tells a friend the Room ID and password

    7. When the second player connects → players can press the ready button

    8. When everyone has pressed the ready button -> the game starts

- Game Session

    9. Makes his moves, monitors the moves of the other player

    10. Receives a notification of victory → return to the lobby

## Demonstration of the working MVP

Link - https://drive.google.com/drive/folders/1HRr739W4mQVXr8u17mUc_5_-wxz0-LN2?usp=sharing

## Internal demo

While testing the app with the team, we found the following set of bugs that need to be fixed:  fixing rooms persisting in the database, missing error messages for invalid room IDs, the Ready button state reset problem, oversized application windows, inconsistent local variable usage in game.py backend logic, wrong error message during email registration, bug during exit (after leaving the room another person doesn't know about leaving).


## Project specific progress

### Frontend

There are 2 new functional buttons in the Main Menu Page for creating and connecting to the game room via HTTP requests (for communication with the backend). There are 2 new pages: Waiting Room Page and Game Room Page.  In the Waiting Room Page, the design was drawn and functions were implemented for updating the team's state (connecting players and their readiness), changing its own state from ready to unready and vice versa, and exiting the room via HTTP requests.  In the Game Room Page, the design was drawn and communication with the backend was implemented via WebSocket for the initial distribution of cards, passing the move between players, sending moves, checking the rules, and ending the game.

### Backend

The backend has implemented a number of very significant tasks. Additional database functionality was written that was needed for the new functional endpoints for creating a room, joining a room, leaving a room, sending room status, and receiving a player ready/unready message. An endpoint for playing in a room was written that uses players' websockets to support multiplayer capabilities. The logic for exchanging data between the backend and frontend during the game and the logic for checking each move the player makes for correctness was implemented. A successful connection was made between the backend and frontend with full functionality for creating, joining, and playing a room. Basic functional endpoints for playing with a bot (DQN) were written: the initial connection was made between the DQN and the backend.


### AI

In the AI ​​section, the following work for this week: fixed errors in the logic of the environment in DQN and MCTS (when processing the green and purple rules), which caused an incorrect result. The first fully functioning model was created (parameters were selected to improve the model's performance), code was written for convenient manual testing of the model against the user. An analysis of the game style of exiting different situations with the need to play a certain set of cards was also conducted (As a result of comparing the MCTS and DQN models, the MCTS showed the best statistical outcome from artificially created situations). Work was started to improve the DQN game level by integrating a stronger opponent in the form of MCTS into its training, which will allow for more effective training of the model and its use of better strategies.


# Weekly commitments

## Individual contribution of each participant

**Palkina Sofia** – organized 4 discussion meetings (20.06 - meeting with TA Mary and after discussion of the amendments she proposed; 21.06 - discussion of the interaction between the back and the front during the players' moves; 22.06 - meeting with a server and deployment specialist/advisor; 23.06 - regular midweek meeting to evaluate progress; 25.06 - discussion of plan for next Week), did research on servers, selected and tested a server for deployment, start implementation of CI/CD, do the demo video and wrote this report

https://trello.com/c/Nb1LzlsF

https://trello.com/c/LzUnNNMV

https://trello.com/c/shxiMPyq


**Polina Kostikova** – wrote endpoints for creating rooms, wrote additional database functions, connected the backend and frontend for creating rooms, wrote basic functional endpoints for playing with a bot (DQN) and performed the initial connection of the backend and DQN

https://trello.com/c/q9JbeV6a

https://trello.com/c/dt8ZgOfR

**Lev Permiakov** – fixed bugs in DQN and created its first fully functional model, wrote manual testing of the model against the user, conducted a comparison of MCTS and DQN, started work to improve the level of the game DQN

https://trello.com/c/t4D4WcS6

https://trello.com/c/dt8ZgOfR

**Arina Petuhova** – wrote endpoints for the game in the room, implemented the main logic inside the game and the logic for checking each move, connected the backend and frontend, fixed errors in the logic of MCTS

https://trello.com/c/47ewU2hC

**Amir Bairamov** – Implemented the work of 2 buttons in the Main Menu Page, wrote 2 new pages, drew the design and implemented functions for creating rooms, drew the design for the main game and implemented communication with the backend via WebSocket

https://trello.com/c/47ewU2hC

https://trello.com/c/E7695U7s

https://trello.com/c/xeM2qJKi

https://trello.com/c/q9JbeV6a

https://trello.com/c/6Z0LGesP

## Plan for Next Week

1. Finish the deployment process to the VPS(Unit tests, CI/CD)

2. Improve the size and visual appearance of the pages (timer, alerts, test all possible errors)

3. Write rules and design for them


## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).