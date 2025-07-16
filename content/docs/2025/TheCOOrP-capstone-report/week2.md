---
title: "Week #2"
---
# Week 2

## New responsibilities

| Team Member            | Track             | Responsibilities                                        |
| ---------------------- | ----------------- | ------------------------------------------------------- |
| Andrey Vasiliev        | TechLead          | Task distribution, Lead Development                     |
| Danil Nesterov         | DevOps/Programmer | Deployment, Repo management, Programming                |
| Anastasia Varfolomeeva | Visual Designer   | Creating sprites and Deciding the general art direction |

## Detailed Requirements Elaboration

### Reasoning

> Due to the nature of our project, we were unable to extract all acceptance criteria from our stakeholder, but we have partially provided it in our backlog.

Our project consists of several mechanics that are correlating to the user stories:

- **Energy:**
  - Main goal of the game.
  - Anomalies generate energy on interaction with Agents.
- **Resources:**
  - Main currency of the game.
  - Used for unlocking new interactions with Anomalies, and equipment like armor and weapons for Agents.
  - We plan to have four kinds of Resources in the game.
- **Anomaly interactions:**
  - Agents interact with Anomalies to generate Energy (and maybe die in the process).
  - Every Anomaly have default interactions that are general for some groups of Anomalies, and unique interactions that have different consequences (random events) and can be unlocked using the Resources.
- **COOPerative Multiplayer:**
  - Multiple players should be able to play together via local multiplayer.
- **Anomaly Escaping:**
  - Anomalies have different behaviors that can cause them to Escape the containment and start attacking the Agents in the case of mistreatment.
  - Agents are equipped with armor and weapons to suppress the escaped Anomalies.
- **Map:**
  - Facility consists of corridors, stairs, and containment chambers for the Anomalies.
  - Players should be able to select the Agents and assign them to a Chamber to interact with the Anomaly.
  - Agents then should navigate to the chamber autonomously.

### Prioritized backlog

<https://github.com/orgs/TheTopSecretTeam/projects/1/views/1>

## Project specific progress

### General development

- Boilerplate code instantiated in repository (we just created a new project)
- A facility Map was created in accordance to the user story.
- All progress committed to repository. [[Github]](https://github.com/TheTopSecretTeam/TheCOOrP)

### UI & Design

- Basic sprites were made to define the general art direction and setting of the game.
- Link to the Anastasia's artifacts [[Google Drive]](https://drive.google.com/drive/folders/16fva8mOxD3vZrQjgF18O-hzLGfr8AgfS)

### Network

- Basic network code was made.
- 2 peers are able to host and connect to each other their cursors are visible to each other.
- All progress committed to repository. [[Github]](https://github.com/TheTopSecretTeam/TheCOOrP)

# Weekly commitments

## Individual contribution of each participant

| Who          | Did what                                                                                                                                                    |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Danil N.     | Filled the Kanban backlog, started learning Godot to assist with development, initialized the CI workflow, deployed the project to Itch.io and GitHub Pages |
| Andrey V.    | Implemented the general development progress, connected ready code to the main branch                                                                       |
| Anastasia V. | Updated the design (from pixelart to rasterized), redrew some game sprites                                                                                  |

## Plan for Next Week

| Who          | Plans to do what                                           |
| ------------ | ---------------------------------------------------------- |
| Danil N.     | Assemble the capstone MVP1                                 |
| Andrey V.    | Develop the Battle system (Anomaly escape and suppression) |
| Anastasia V. | Finish drawing sprites, assist with writing code           |

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
