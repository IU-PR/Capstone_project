# **Week #6**

## Links

- **Deployment (Prod)**: 77.233.222.200:9050  
- **Deployment (Staging)**: 77.233.222.200:8050  
- **API Docs & Full Project Documentation**: [GitHub /docs/ folder](https://github.com/IU-Capstone-Project-2025/DeathRoom/tree/dev/docs)  
- **Design Document**: [Google Docs Design](https://docs.google.com/document/d/1kdaqDS6iQa7g32GWyoYNd155X4573cyyWMIlz3Tq7Ys/edit?tab=t.0)  
- **Final Presentation**: [Google Drive Presentation Folder](https://drive.google.com/drive/folders/1YU7Lw0bzuPI1iVpSspkpJTK51fQ5S7f9)

## Final deliverables

### Project overview

**DeathRoom Online** is a fast-paced, competitive multiplayer arena shooter inspired by classics like Quake and Call of Duty. The project solves the problem of providing a modern, responsive FPS experience with low-latency online play, fair hit registration, and fun core gameplay without excessive complexity.  
Key implemented features include server-authoritative mechanics, health/armor systems, respawning, live leaderboards, map selection, and a complete documentation set for both client and server.

### Features

- Server-authoritative gameplay logic
- Real-time multiplayer for up to 12+ players
- Player movement (jump, strafe, slide, jump-pads)
- Health, armor, and pick-up system
- Accurate damage and respawn mechanics
- Multiple maps, new spawn point balancing
- Pause menu, health/armor/nickname UI
- Fully documented backend and client architecture

### Tech stack

- **Backend:** .NET (C#), custom UDP networking via LiteNetLib, Docker, GitHub Actions CI/CD
- **Frontend (Game client):** Unity, C#, UI Toolkit
- **Infrastructure:** Docker Compose, manual deployment to VDS (Ubuntu), in-memory game state
- **Docs:** Markdown (C4 model), Google Docs for design

### Setup instructions

1. **Clone the repository:**  
   `git clone https://github.com/IU-Capstone-Project-2025/DeathRoom.git`
2. **Read deployment instructions in `/docs/README.md`**  
   for full backend/server setup.
3. **Build and run server with Docker Compose:**  
   In project root:  
   `docker-compose up --build`
4. **Build the client in Unity** (instructions in `/docs/client.md`).
5. **Connect the built game client** to the server IP (see Deployment links).

## Presentation draft

- [Presentation folder (Google Drive)](https://drive.google.com/drive/folders/1YU7Lw0bzuPI1iVpSspkpJTK51fQ5S7f9)

# Weekly commitments

## Individual contribution of each participant

- **Rodion Krainov**  
  - Finalized backend: fixed bugs, added armor logic, improved damage & respawn mechanics, implemented HP/armor restoration via updated packet system ([commit](https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/c819888a48357c35c0db6448918e94fd198f4c59)).
  - Switched server to respawn (not disconnect) on player death ([commit](https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/084fdc9d7dd7960b970a158760ed6e1d5eeb6763)).
  - Updated CI/CD pipelines for new server architecture ([commit](https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/48c6dce35387207efca942d9ab27a9fd029772b9)).
  - Wrote comprehensive project documentation ([commit](https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/05d4b7d8364a7f215e57d270863b7f3becf46a20)).
  - Wrote this report
- **Slava Molchanov**  
  - Assisted with setup and refinement of the new backend architecture ([commit](https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/c819888a48357c35c0db6448918e94fd198f4c59)).
- **Gleb Lobov**  
  - Finalized and improved the project’s design document.
  - Enhanced map design, created new maps ([newMap branch](https://github.com/IU-Capstone-Project-2025/DeathRoom/tree/newMap)).
  - Created the final project presentation ([presentation link](https://drive.google.com/drive/folders/1YU7Lw0bzuPI1iVpSspkpJTK51fQ5S7f9)).
- **Igor Kuzmenkov**  
  - *No contributions this week.*
- **Almas Bagishaev**  
  - *No contributions this week.*
- **Vsevolod Nazmudinov**  
  - Managed team work and coordination.
  - Implemented client shooting logic and additional bug fixes ([commit](https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/ae1e9c63c694c90e0de775ab4b4cb0c40515dd0c)).
- **Ilyas Khatipov**  
  - Created new spawn points on the map ([commit](https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/157f82f11467d11a3d73424774006bed972e4523)).
  - Developed UI for pause menu, HP/armor display, and nicknames ([commit](https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/b5f45388e605dd299f857fdef4c339c7869bce40)).

## Plan for Next Week

- Final project defense and demonstration.
- Post-release polish, feedback collection, and potential bug fixing.
- Prepare project hand-off and archival.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
