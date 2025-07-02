# Week #3

## Implemented MVP features

### User Journey

1. The user launches our Unity game build.
2. The client (game) automatically connects to the server.
3. The player is spawned at a random location on the map and can start playing immediately.
4. All player actions (movement, rotation, shooting, hits) are sent as packets to the server.
5. The server processes these packets, maintains tick synchronization, and sends world state updates (positions, shots, etc.) back to the client.
6. If a player is killed, they are disconnected from the server.
7. The player can open the in-game menu at any time and exit the game through it.

### Client-side Features

- Weapon selection system: players can choose which weapon to use for shooting.
- In-game menu: accessible at any time, allows the player to exit the game.
- Player health and armor system: displays both a bar and a numeric value next to it.
- Advanced player movement and shooting mechanics.
- Real-time communication with the server via LiteNetLib (UDP).
- Player is spawned at a random point on the map at the start of the game.
- All player actions (movement, rotation, shooting, hits) are sent to the server as packets.
- The client receives and processes world state updates from the server.

### Server-side Features

- Tick-based architecture: the server maintains a tick counter and synchronizes it with clients.
- Lag compensation: the server reconstructs world state for accurate hit registration.
- All data is stored in-memory for fast access.
- Processes and validates all client packets (movement, shooting, hit registration).
- Disconnects players when their HP reaches zero.
- For each shot, the client sends a packet with the bullet's direction; the server verifies hits using mathematical calculations and updates player HP accordingly.
- Sends world state updates to all clients.

### Features Implemented This Week

#### General

Refactored the codebase and conducted code reviews for both client and server.
!Links to relevant commits where changes were made, if applicable

#### Client

Selected player, weapon, and tool models tailored to the target audience. Implemented functionality for player health, shooting, advanced player movement, and set up communication with the server via LiteNetLib (sending and receiving UDP packets). The game map was created and designed with the genre and multiplayer in mind, taking inspiration from popular maps in similar games.
Commits where this was implemented: !links to commits

![Map](https://drive.google.com/file/d/1sEYntfkl0PKLVjqo_d-9Z3BeH25kSk4D/view?usp=sharing)

![Player 1](https://drive.google.com/file/d/1KTOdkfteie6OdUK2xPvUguvv-6RRXVRq/view?usp=sharing)

![Player 2](https://drive.google.com/file/d/1c0V9LNoXCVEdUz-MQdzjjC1uSi_dDtP5/view?usp=sharing)

Implemented complex character animations triggered by user events and reflecting player actions:

- Idle animation
- Walking animation
- Jump animation
- Shooting animation

A rich arsenal of weapons was implemented, each with unique properties:

**Phantom (Riffle)**

![Phantom](https://drive.google.com/file/d/16OzPF0kqmCoaWSWPPPD1wySQt4Y0F3rz/view?usp=sharing)

- Medium damage
- Fire rate: 0.1 seconds per shoot
- Large magazine (27 rounds)
- Total ammo: 200 rounds

#### Game Server Logic

- Implemented a tick-based architecture: the server maintains a tick counter and stores world state snapshots every N ticks, allowing for lag compensation and accurate event processing.
- Added in-memory storage for player and session data, replacing DB usage for real-time operations to significantly improve performance.
- Implemented lag compensation: the server can reconstruct the world state at any tick, enabling fair hit registration even with network delays.
- Developed a new packet exchange protocol:
  - PlayerShootPacket now includes a direction vector.
  - Introduced PlayerHitPacket for client-side hit registration, which the server verifies using world history.
- Refactored hit logic: all hit checks are now performed against historical world states, not just current positions.
- Added health (HP) to players, with logic for reducing HP on hit and removing/disconnecting players when HP reaches zero.
- All legacy DB-based session/player logic is commented out but preserved for reference.
- Codebase was refactored, bugs fixed, and code review practices established.
- Database migrations were created and proper server-DB interaction was set up.

## Demonstration of the working MVP

![Demo](https://drive.google.com/file/d/12i58A0bwZgNKO3cwemIaAfPdsZBHryTR/view?usp=sharing)

## Internal demo

Demo demonstrates client view of the game including moving and shooting on map.

# Weekly commitments

## Individual contribution of each participant

Vsevolod Nazmudinov

- Participated in the development of the updated client-server packet exchange logic.
- Implemented server tick logic, enabling features like lag compensation.
- Led brainstorming for choosing the client-server communication platform.
- Connected the client to the server using LiteNetLib.
- Organized team meetings and managed development processes.
- Managed and distributed tasks in Asana. Asana link: https://app.asana.com/1/1210569831287734/project/1210570004733565/list/1210570197020283
- Conducted code reviews and merged pull requests.
- Fixed previous server bugs.
- Commits: https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/22b4c31af6abd1934f9c6bf436df9569903eb20a
  https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/5117513fae1f219e27f52f7c8fe847a2c15f80f1
  https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/e87ff5a4c2335dbb375f676b5b5234824f8581f9
  https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/249989db8bbfddfeaf21dbb651cbab4ada1a2f0a
  https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/2d132cbb42a4aab1b7a4434364eba5650fa603c7
  https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/e00b239eb49baafc9c09c0e5201c7007c10c8b04
  https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/ef2d443150b7b402f3e85d281db45c8b94a944c2
  https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/17f1cf69cd7f67a1629a35fbabccd07e07d721c0
  https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/1bf718b9b31bd55673df91a120ddb9b7ca733866
  https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/1791d7597b591fc8c58b9d5e7734067e34443b90
  https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/fc9e456318165f5470dd1e1e4e37e0c472a8d5a6
  https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/abd43fb35ef6bbd189ff9fdefacae23811a5be30
  https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/6aa2d9fb149ebda6b2ae3f177b12c9c11676c7ee
  https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/541a50a2c36c678a11f535c7accc8aad642d8aab
  https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/f7d140e758c2a04dbe1a3db14602752cb826ce7a
  https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/2ebbf8ab9fb3fa2a3e4cb7fc94a262f57c694db2
  Rodion Krainov
- Participated in the development of the updated client-server packet exchange logic.
- Developed tick synchronization logic between server and client. Commit link: https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/206784adb71436d32a2b2ca81504503b4d2bad6e
- Implemented world state history and event processing by tick, enabling lag compensation. Commit link: https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/206784adb71436d32a2b2ca81504503b4d2bad6e
- Implemented the new PlayerHitPacket logic. Commit link: https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/206784adb71436d32a2b2ca81504503b4d2bad6e
- Migrated world/session state from DB to in-memory storage for faster event processing. Commit link: https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/206784adb71436d32a2b2ca81504503b4d2bad6e
- Refactored server code and fixed bugs. Commit link: https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/206784adb71436d32a2b2ca81504503b4d2bad6e
- Finalized shooting and HP logic, including player removal on death. Commit link: https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/206784adb71436d32a2b2ca81504503b4d2bad6e

Igor Kuzmenkov

- Developed a migration and deployment system for databases, although we later decided to abandon the use of a traditional database.
- Collaborated with Vsevolod to implement the client-server connection.
- Started writing tests to cover the backend.
- Commits: https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/5d4e7d2ce646acc9e197b11f7f44f54806b92277 https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/3d66bddcdd111e66a4b41fbfbea826c78b2109a5 https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/16d1a3310d269a2b71133cd36666104b303fd90f

Ilyas Khatipov

- Led all client-side development:
  - Implemented player, weapon, and tool models.
  - Developed player movement, shooting, and health logic.
  - Set up LiteNetLib communication.
  - Implemented all player and weapon animations.
- Commit: https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/ea3987870d21302620607303fef8d7a923c0bdea

Gleb Lobov

- Authored the design document. Link: https://docs.google.com/document/d/1kdaqDS6iQa7g32GWyoYNd155X4573cyyWMIlz3Tq7Ys/edit?tab=t.0
- Assisted in map creation
- Developed the work plan
- Oversaw launcher development

Slava Molchanov

- Participated in the development of the updated client-server packet exchange logic.
- Developed advanced mathematical models for hit detection using 3D shot direction vectors and complex hitboxes (composed of 3D geometric shapes). Commit link: https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/086eaa290421608a144687e903cb40982d54de4c
- Implemented V1.0 of damage registration. Commit link: https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/086eaa290421608a144687e903cb40982d54de4c
- Helped connect the client and server via LiteNetLib.

Almas Bagishaev

- Made significant contributions to client development and key decisions.
- Implemented the game menu. Commit link: https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/9b4f1973fbdb6010d57651d589f86d592a56484e
- Added the ability to enter/exit the game via the menu. Commit link: https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/9b4f1973fbdb6010d57651d589f86d592a56484e
- Implemented the player health and armor system, including both a visual bar and a numeric value displayed next to it. Commit: https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/844d361763f02d17ae1076d8330d2f03c6c61687

## Plan for Next Week

At this stage, we have all the core logic required for a shooter, but the project has great potential for further development, optimization, and new features. Next week we plan to:

- Conduct a full code review, discuss architectural and functional decisions
- Improve server-side hit detection logic
- Analyze and, if necessary, revise the game map
- Perform load testing on the game server and determine optimal configuration (tickrate, world state history length, etc.)
- Refine existing weapons and add new ones if needed
- Optimize current algorithms and solutions
- Finalize database interaction logic
- Hold several team meetings
- Explore further use of LiteNetLib to optimize packet exchange between server and clients

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [✓] Is in working condition.
- [✓] Runs via docker-compose (or another alternative described in the README.md).
