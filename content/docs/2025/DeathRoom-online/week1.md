# Project Report: DeathRoom Online

## Project Description

**Project name:** DeathRoom Online  
**Code repository:** [https://github.com/IU-Capstone-Project-2025/DeathRoom](https://github.com/IU-Capstone-Project-2025/DeathRoom)

DeathRoom Online is a fast-paced arena shooter inspired by Quake and Call of Duty, designed for competitive multiplayer gaming. The project addresses the growing demand for skill-based, responsive FPS games that prioritize low-latency gameplay over complex progression systems.

**Problem Statement:** Modern arena shooters often sacrifice network responsiveness for graphical fidelity. Our solution combines precise movement mechanics with robust server validation, ensuring fair and responsive gameplay in 12-player matches.

## Team Members and Assigned Roles

| Role | Team Member | Responsibilities |
|------|------------|------------------|
| Project Lead, Backend-Frontend Developer | Vsevolod Nazmudinov | Oversees project direction |
| Backend Developer, Network Engineer | Igor Kuzmenkov | Handles UDP implementation and network optimization |
| Backend Developer | Slava Molchanov | Implements core game logic |
| Client Developer | Ilyas Khatipov | Responsible for client parts |
| Game Designer, UI/UX | Gleb Lobov | Creates models in Blender and manages animations |
| Backend Developer, DevOps Engineer | Rodion Krainov | Manages Docker deployment and server infrastructure |
| Backend Developer, Reporter | Almas Bagishaev | Responsible for reports |

## Chosen Project Idea

We are developing a fast-paced arena shooter featuring:
- 12-player multiplayer matches
- Competitive leaderboards and match statistics

## Basic Requirements

### Target Users
- Competitive players who need sub-50ms latency
- Esports enthusiasts who require spectator tools
- Casual players who want quick matchmaking

## High-Level User Stories & Initial Scope

### User Stories
- As a player, I want to join matches quickly to minimize waiting time
- As a competitor, I need responsive controls for precise gameplay
- As a spectator, I want to watch ongoing matches to learn from better players
- As an admin, I need server metrics to monitor performance

### Initial Scope
- Core movement mechanics (strafe jumping, crouch sliding)
- Weapon types (long range, projectile)
- Arena maps
- Basic matchmaking system
- Leaderboard system

## Chosen Tech Stack with Justification

### Backend
- **.NET + LiteNetLib/ENet** - High-performance networking for FPS games
- **Photon Fusion (Server-authority)** - Prevents client-side cheating
- **EF Core + PostgreSQL** - Reliable data storage for player stats
- **Redis** - Enables horizontal scaling

### Frontend
- **Unity 6** - Latest engine with improved networking
- **Blender + Mixamo** - Efficient 3D asset pipeline

### Infrastructure
- **Docker** - Consistent deployment across environments
- **UDP Protocol** - Essential for low-latency gameplay