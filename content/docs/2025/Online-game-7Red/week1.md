---
title: "Week #1"
---

# Week #1

## Project description

### Project name: Online game 7Red

**Code repository**: https://github.com/IU-Capstone-Project-2025/Online-game-7Red

### Problem Statement:
Traditional card games like "7Red" are culturally significant but often lack modern digital representations.Players currently have no reliable way to play 7Red online with friends, track their progress, or compete against others globally. The absence of online versions limits the game’s exposure and playability, especially during times when in-person gatherings are not feasible.

This project aims to solve these problems by:

- Digitizing "7Red" with faithful adherence to its rules.

- Enabling multiplayer capabilities, including friend-based private rooms.

- Creating a persistent ecosystem with account tracking, in-game statistics, and achievements.

- Providing options for solo play against AI when other players are not available 

### Project Description:

The application includes the following core components:

1) User Authentication: Secure login and registration system to manage individual player accounts.

2) Main Menu Interface: A central hub for users to access game modes, settings, and statistics.

3) Game Modes:

- Play with Friends: Create and join private game rooms using custom IDs.

- Play Online: Match with random players through a smart matchmaking system.

- Play with AI: Option to play against computer-controlled opponents.

4) Statistics & Achievements Page: Tracks wins, losses, game history, and unlockable achievements to enhance engagement and competition.

5) Rules Page: Provides users with clear instructions and gameplay rules.

6) Settings Page: Allows users to update profile data, change their avatar, and switch languages.

7) Real-Time Multiplayer Infrastructure: A database system to store user accounts and manage the state of live games, ensuring synchronization across devices.

8) Error Handling and UI Feedback: Friendly error messages and loading states for smoother UX.

### **Team Members**

| Team Member                             | Telegram Alias   | Email Address   | Track                                       | Responsibilities   |
|-----------------------------------------|------------------|-----------------|---------------------------------------------|--------------------|
| Palkina Sofia     | @angel_sofia2005 | s.palkina@innopolis.university | Manager and  Backend developer | Project coordination, task delegation, backend development |
| Polina Kostikova  | @poolinna_k | p.kostikova@innopolis.university | Backend developer | Server-side logic, database interactions, API development |
| Lev Permiakov     | @arhitc | l.permiakov@innopolis.university | ML and DB developer | Machine learning models,ML model training,  generation game-data |
| Arina Petuhova    | @lyutnya | a.petuhova@innopolis.university | ML and DB developer | Machine learning models,ML model training,   database design|
| Amir Bairamov     | @Mr_DeBuFF | a.bairamov@innopolis.university | Frontend developer and Designer | Figma design, frontend development |



## Brainstorming

### Ideas during brainstorming

1) **Multiplayer 7Red (Card Game)** – An online version of the Russian  game "7Red" with statistics, achievements and private rooms for friends. 

2) **Digital Menu & Order System for Happiness** – A lightweight web app for cafés to manage pickup orders, with real-time kitchen updates, SMS notifications, and prep time estimates. (Note: The "Happiness" café said they don’t need it)

3) **Dorm Room Swap Platform** – A matchmaking system for students to trade dorm rooms based on preferences like floor/campus or roommate compatibility (Note: already exists in our dorm).

4) **Smart Moving Checklist Generator** – A web app that creates personalized packing lists based on room size, distance, and season, integrating with Google Keep/Todoist for tracking (Note: though AI can do this now).



### Brief market research


#### 1. **Multiplayer 7Red (Russian Card Game)**

Market Opportunity:

- Card games like UNO Online, Hearts, and Exploding Kittens have strong online player bases.

- Traditional 7Red board game have loyal followings but no digital adaptations.

Competitors:

- No major polished, standalone 7Red online versions exist. The only competitors  suffer from poor design, bad UX, and slow performance: https://ru.boardgamearena.com/gamepanel?game=redsevengame

Conclusion:

- Strong niche demand with little competition—worth developing 


##### 2. **Digital Menu & Order System for Happiness**
Market Opportunity:

- Small cafés often rely on Telegram or phone calls — leading to errors and slow customer service.

Competitors:

- Yandex Eats: Expensive, overkill for small businesses.

Conclusion: 

- Interviews with café owners reveal -"Happiness café" rejection suggests lack of immediate pain point—indicating a need for better problem-sales fit.

## Basic requirements

### Target users and their primary needs

**Primary Audience**: Gamers who enjoy strategy and card games

**Primary needs**: 

Simple rules, but deep strategy - to make it easy to start, but have room to grow

Fast and fair fights - so that victory cannot be bought

Progress and rewards - to see your statistics and progress

Play with friends - to make it more interesting


### User stories

1. As a player, I want to join and play the 7Red game online so that I can compete with others in real time.

2. As a new user, I want to register and log in securely so that my game progress and stats are saved.

3. As a player, I want to view my game history and statistics so that I can track my performance over time.

4. As a player, I want to invite friends to private matches so that we can play together in a controlled environment.

5. As a player, I want to customize my profile and avatar so that I can express my identity within the game.

### Initial scope

#### **MVP 0** – Core Functionality (3 week)

This is the minimal viable version focused on launching the essential mechanics of the game:

- User Authentication: Basic sign-up and sign-in functionality.

- Private Game Rooms: Players can create and join private rooms using a unique room ID and password to play with friends.

- No UI enhancements, statistics, or additional features are included at this stage.

#### **MVP 1** – Fully Functional Release (week 7)
This version delivers the complete intended functionality for the course project:

- Three Game Modes: private Rooms with friends, online matchmaking with random players, playing against AI (bot).

- Language Switching: Users can change the application language from the settings.

- Modern Design: Polished and user-friendly interface with a consistent design system.

- Statistics Tracking: Displays number of games played, wins, and other basic metrics.

- Achievements: Three unlockable achievements to encourage player engagement.

- Profile Editing: Users can update their avatar, username, and other account-related preferences.

#### **MVP 2** – Future Enhancements (Beyond Current Scope)

These features are potential improvements that may be added later but are not planned for the current course period:

- Email Verification: Validate email addresses through code-based confirmation.

- Two AI Difficulty Levels: Players can choose between easy and hard bots.

- Extended Achievements: Add a larger variety of in-game achievements.

- Chat Functionality: Implement a basic chat with restricted input for communication during games.

## Tech-stack

Frontend - Flame, Flutter (Material, Provider, Riverpod, Shared Preferences)

Backend - Python (psycopg2) 

Database - 

ML - Python (pandas, numpy, pytorch, alpha-zero-general, postgresql(sqlalchemy))


# Weekly commitments

## Individual contribution of each participant

**Palkina Sofia** – organized 3 discussion meetings and wrote this report.

**Polina Kostikova** – set up Docker and created the basic Git structure.

**Lev Permiakov** – wrote code for generating data for the neural network.

**Arina Petuhova** – designed the database and implemented its initial version.

**Amir Bairamov** – completed the basic Figma version of the project (excluding the game board) and started expanding it.

**All team members** - researched and explored the best tools for the project and discussed the project logic together in meetings.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).