---
title: "Week #1"
---
# Week 1

## Project description

### Project name: TheCOOrP

**Code repository**: [https://github.com/TheTopSecretTeam/TheCOOrP](https://github.com/TheTopSecretTeam/TheCOOrP)

*Cooperative anomaly management simulator (like Lobotomy Corporation) written in Godot engine.*

### **Team Members**

| Team Member            | Telegram Alias                                   | Email Address                                                                     | Track     | Responsibilities                  |
| ---------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------- | --------- | --------------------------------- |
| Andrey Vasiliev        | [@nncrn](https://t.me/nncrn)                     | [a.vasiliev@innopolis.university](mailto:a.vasiliev@innopolis.university)         | Backend   | Task distribution, Lead Developer |
| Danil Nesterov         | [@NeRaG0n7](https://t.me/NeRaG0n7)               | [d.nesterov@innopolis.university](mailto:d.nesterov@innopolis.university)         | DevOps    | AGILE, Repo management            |
| Anastasia Varfolomeeva | [@acecution](https://t.me/acecution)             | [a.varfolomeeva@innopolis.university](mailto:a.varfolomeeva@innopolis.university) | FullStack | UI Designer                       |
| Maksim Batuev          | [@FrapsSid](https://t.me/FrapsSid)               |                                                                                   |           |                                   |
| Karim Fajzanov         | [@fayzakar](https://t.me/fayzakar)               |                                                                                   |           |                                   |
| Gafur Abdullin         | [@gafur_0307](https://t.me/gafur_0307)           |                                                                                   |           |                                   |
| Aleksei Blinov         | [@qwertyzrO](https://t.me/qwertyzrO)             |                                                                                   |           |                                   |
| Danil Kudinov          | [@fortuno_alibaba](https://t.me/fortuno_alibaba) |                                                                                   |           |                                   |

>Also we are using some help from 1st year bachelor students (1st team).

## Brainstorming

### Ideas during brainstorming

*Put here your ranked ideas with short description*

Because we are doing project with 1st year students we have a stakeholder that provides project idea and instructions

But before that we had some other ideas.

1. The Lobotomy Corporation clone with COOP multiplayer feature. (Stakeholder Idea)
2. A CRM system for small businesses.
3. Referral system for small buisnesses.
4. Online booking system for events.

### Brief market research / problem validation

*Put here a brief market research/problem validation for 1–2 ideas*

#### CRM system

There is a growing market of small buisness owners who are looking for efficient solutions to manage customer relationships and time management.
By making a quick search, there are numerous CRM solutions available, but many are overly complex or expensive that do not cater specifically to the unique needs of small businesses.

#### Referral Client System

**Problem:** Its very hard for small businesses to gain new clients. **Solution:** Make a referral system so that they can keep track and employ influencers for advertisement.
**Target audience:** Small businesses in Russia.
**Copetitors:** As far as my research goes there are no competitors in small business domain.
#### TheCOOrP

The only project with the same idea is a fan game called [Lobotomy Corporation 13](https://wiki.lc13.net/view/Main_Page) (LC13) that is a mod for 2003 game SS13 which has similar gameplay mechanics.

## Basic requirements

### Target users

A. Demographics
Age Range (e.g., teens 13-19, young adults 20-35)
Location (global)
B. Psychographics & Gaming Preferences
Casual Gamers
C. Platforms & Play Habits
PC

### User primary needs

A. Core Needs (Why Do They Play Games?)
Escapism/Immersion (Story-rich, atmospheric games like Firewatch)

Challenge & Mastery (Roguelikes, precision platformers like Celeste)

Social Connection (Multiplayer games like Among Us)

B. Pain Points (What Frustrates Them?)
Overpriced games -> Our game will be cheap.

Games require powerful systems -> Smooth performance on ost devices is critical.

### User stories

- As a player, I want to play in COOP so that i can have fun with my friends.
- As a player, I want to have an interesting gameplay so that i wont get bored.
- As a player, I want to interact with anomalies so that i can progress the game.
- A a player i want to see appealing visuals so i can immerse myself in the game world.

### Initial scope

MVP should contain: Working Multiplayer, Basic Agent Management, Textures and Soundtrack and Basic gameplay loop.
MVP will NOT contain: Agent Customization, Anomalies Escape sequences, any progress beyond 1st level.

### Additional progress report

We will also include 1st year students progress into our report to avoid confusions in the future.

## Tech-stack

* Godot Engine
* GDScript
* Docker

# Weekly commitments

## Individual contribution of each participant

| Who          | Did what                                                                                                                         |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| Danil N.     | Initialized the GitHub Organization, Repos, Project and written some tickets based on the stakeholder's project description.     |
| Andrey V.    | Distributed tasks among 1st year bachelor students; Designed initial game infrastructure; Made basic `Room` and `Agent` Nodes.   |
| Anastasia V. | Began designing the UI and overall look of the game (sprites in repo are placeholders).                                          |
| Maksim B.    | Prepared a manual for the team on the game Lobotomy Corporation so that team members could familiarize themselves with the game. |
| Karim F.     | Prepared transcript for interview and developed skills in using GDScript and Godot.                                              |
| Gafur A.     | Prepared 1st team report and developed skills in using GDScript and Godot.                                                       |
| Aleksei B.   | Started developing the multiplayer component of the game.                                                                        |
| Danil K.     | Began compiling a glossary containing all the terms used in the manual.                                                          |


## Confirmation of the code's operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
