# **Week #5**

## Feedback

### Sessions

| User | Context | Key Comments |
|------|---------|--------------|
| **User 1** (classmate, competitive-FPS fan) | Played staging build on gaming laptop (Wi-Fi). | • Wanted visible armor/health pick-ups.<br>• Asked for an in-match leaderboard.<br>• Noticed brief stutter when > 6 players shoot simultaneously. |
| **User 2** (neighbor, casual gamer) | Tested Windows build with Xbox controller. | • Spawn points felt “too exposed”, died quickly.<br>• Couldn’t change nickname after launch.<br>• Jump-pads are fun but need SFX cue. |
| **User 3** (TA, network-engineering background) | Joined public server over 4 G. | • RTT good but memory grew after ~15 min.<br>• Suggested clearer domain/transport split for scaling.<br>• Recommended Prometheus metrics endpoint. |

### Analyze

| Issue | Priority | Backlog Ticket |
|-------|----------|----------------|
| Missing in-game leaderboard | P1 | `feat/leaderboard-ui` |
| Visual cues for armor/health pick-ups | P1 | `feat/pickup-devices` |
| Stutter on mass shooting | P1 | `perf/bullet-pool-optimization` |
| Change nickname post-launch | P2 | `ui/nickname-input` |
| Spawn safety | P2 | `level/spawn-balancing` |
| Server memory climb | P2 | `ops/memory-leak-investigation` |
| Prometheus metrics endpoint | P3 | `ops/prometheus-endpoint` |

## Iteration & Refinement

### Implemented features based on feedback

* **Armor system & pick-up devices** — models, logic, UI.  
* **Leaderboard UI** — real-time ranking panel.  
* **Nickname input dialog** — local storage + send to server.  
* **Multiplayer fixes**.  
* **Map update & safer spawns**.  
* **DDD + Clean Architecture refactor** — domain split, graceful shutdown.  
* **Server documentation** — build/run guide & diagrams.

### Performance & Stability

**Collected metrics**

| Metric | Measured value | Target |
|--------|----------------|--------|
| **Avg. server tick duration** | **2 ms** | ≤ 5 ms |
| **95-th percentile RTT (EU stage)** | **45 ms** | ≤ 60 ms |
| **Max concurrent players without GC spikes** | **14** | ≥ 12 |

**Improvements**

Much more concurrent players could be obtained if we will take more powerfull server with better configuration.

### Documentation

* **README.md** — quick-start, compose, FAQ.  
* **Inline XML-comments** — public API & packet definitions.  
* **CI/CD notes** — workflow explanations inside `.github/`.

# Weekly commitments

## Individual contribution of each participant

| Team-member | Detailed work this week | Commits / Links |
|-------------|------------------------|-----------------|
| **Almas Bagishaev** | • Implemented full armor system and pick-up devices.<br>• Added in-match leaderboard UI. | <https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/7d8e638fbb76472dee96762dd206c12258fbe5ea> |
| **Igor Kuzmenkov** | • Researched Kubernetes autoscaling for in-memory server instances.<br>• Set up local K8s cluster prototypes.<br>*(No code committed yet — research phase and server configuration.)* | — |
| **Rodion Krainov** | • Migrated server to DDD & Clean Architecture: split **Domain / Application / Backend / Common**.<br>• Authored detailed server documentation.<br>• Wrote this weekly report. | Refactor commit: <https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/f2e55f27d5e8ab4676be4bd8c159f589514bfef1><br>Docs commit: <https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/7054ea85f62902e5927ab1655a290368bed99daa> |
| **Ilyas Khatipov** | • Fixed and configured multiplayer client-side logic.<br>• Implemented nickname input dialog. | Multiplayer: <https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/77c3fd315e06155baf8a1b9eae7d384a5a9c1ee4><br>Fixes batch: <https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/b1953a32502edb95e10fd6cb1cf7cd6469292d1b><br>Nickname input: <https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/f6ee4f2e398ed135cc7308df8e5e996c87f39aab> |
| **Slava Molchanov** | • Co-implemented multiplayer client fixes (paired with Ilyas). | Same fixes:<br><https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/77c3fd315e06155baf8a1b9eae7d384a5a9c1ee4><br><https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/b1953a32502edb95e10fd6cb1cf7cd6469292d1b> |
| **Gleb Lobov** | • Updated and polished game map. | PR commit: <https://github.com/IU-Capstone-Project-2025/DeathRoom/pull/29/commits/0695079fbf6c154a86d6c9a4aecce732f30cb613> |
| **Vsevolod Nazmudinov** | • Performed code reviews across refactor PRs.<br>• Fixed numerous bugs and logic errors reported during reviews. | <https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/72047be9904d53042dbf770fec21c0e1dffcd50f> |

## Plan for Next Week

* Complete migration to DDD branch across all modules.  
* Re-engineer server hit-detection & damage logic.  
* Add Prometheus metrics exporter and enhance logging.  
* Identify and patch memory leak.  
* Polish codebase and write final slide deck for project defense.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
