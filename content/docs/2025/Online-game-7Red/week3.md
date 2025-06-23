---
title: "Week #3"
---

# **Week #3**

## Implemented MVP features

This is the minimal viable version focused on launching the essential mechanics of the game:

- User Authentication: Basic sign-up and sign-in functionality

- Private Game Rooms: Players can create and join private rooms using a unique room ID and password to play with friends, see the list of players in the room

- Game Session Implementation: Once the game starts, the core gameplay loop will be fully functional. This includes turn-based mechanics, timer,  player interactions, and enforcing the game’s basic rules

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

    9. Makes his moves, monitors the timer and the moves of the other player

    10. Receives a notification of victory → return to the lobby

## Demonstration of the working MVP

Link - 


## Project specific progress

### Frontend

*...*

### Backend

*...*

### AI

*...*


# Weekly commitments

## Individual contribution of each participant

**Palkina Sofia** – organized 4 discussion meetings (20.06 - meeting with TA Mary and after discussion of the amendments she proposed; 21.06 - discussion of the interaction between the back and the front during the players' moves; 22.06 - meeting with a server and deployment specialist/advisor; 23.06 - regular midweek meeting to evaluate progress; 25.06 - discussion of plan for next Week), did research on servers, selected and tested a server for deployment  and wrote this report

https://trello.com/c/Nb1LzlsF

https://trello.com/c/LzUnNNMV


**Polina Kostikova** – 

**Lev Permiakov** – 

**Arina Petuhova** – 

**Amir Bairamov** – 

## Plan for Next Week

1. *...*


## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).