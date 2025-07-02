---
title: "Week #3"
---

<!-- Iframe filter counteract -->
<style>
body.dark-mode iframe:not(:fullscreen) {
  filter:
      contrast(calc(1 / 0.85))
      brightness(calc(1 / 1.05))
      hue-rotate(180deg)
      invert(100%);
  -webkit-filter:
      contrast(calc(1 / 0.85))
      brightness(calc(1 / 1.05))
      hue-rotate(180deg)
      invert(100%);
}
body:not(.dark-mode) iframe,
body.dark-mode iframe:fullscreen {
  filter: none !important;
  -webkit-filter: none !important;
}
</style>

# Week 3

## Implemented MVP features

- **Energy:**
  - Main goal of the game.
  - Anomalies generate energy on interaction with Agents.
- **Anomaly interactions:**
  - Agents interact with Anomalies to generate Energy.
- **COOPerative Multiplayer:**
  - Multiple players are able to play together via local multiplayer.
- **Map:**
  - All planned facility modules are implemented.
  - Agents can be selected and sent to any location.
  - Agents can navigate the complex with ease.
- **Anomaly research menu:**
  - In this menu, you can unlock info about anomalies and read their description.
  - It is planned to give player an ability to unlock and manufacture the gear for the employees by spending the resources.

### User Journey

#### Main Loop:

- **Energy Collection Goal:** Each day has a quota of (energy) you must produce by working on Anomalies.
- **Order Agents to Work:** Agents perform tasks on Abnormalities (e.g., Instinct, Insight, Attachment, Repression), each with different risks and rewards.
- Success yields energy.
- Failure may trigger the Abnormality’s negative effects.
- When you collect enough energy for the quota you will be able to move onto the next day.

## Demonstration of the working MVP

### MVP1 demo recording

<iframe loading="lazy" src="https://player.vimeo.com/video/1096339635?title=0&byline=0&portrait=0&pip=1&badge=0&quality=720p&dnt=1" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" width="640" height="360" title="TheCOOrP-MVP1-demo"></iframe>

### Latest Itch\.io build

<iframe loading="lazy" frameborder="0" src="https://itch.io/embed-upload/14046546?color=333333" allowfullscreen="" width="640" height="380"><a href="https://localt0aster.itch.io/thecoorp">Play TheCOOrP on itch.io</a></iframe>

## Internal demo

After conducting the internal demo, we identified a few major bugs:

- Shop Research Currency counter does not update after purchase.
- Work is not synced between clients.
- You can move working Agent, which breaks the game state.
- You can move Agent into an occupied chamber, which resets current working progress.
- Our stakeholder highlighted the lack of polishing.

# Weekly commitments

## Individual contribution of each participant

| Who          | Did what                                                                                | Proof                                                                                                                                                                                                                                                                                   |
| ------------ | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Andrey V.    | Made new game sprites, connected all assets into MVP1                                   | [[29dbb93]](https://github.com/TheTopSecretTeam/TheCOOrP/commit/29dbb9367a24a8ec2bd8796726ec36e19de9f4b0)                                                                                                                                                                               |
| Danil N.     | Assembled and redacted assets for MVP1, embedded the web build into the capstone report | [[bd865e7]](https://github.com/TheTopSecretTeam/TheCOOrP/commit/bd865e7c89d5fcdd75193fe7c040f7e0ccf27d4e) (redid the scripting), [[6448f24]](https://github.com/TheTopSecretTeam/TheCOOrP/commit/6448f243331d729db31dd580c4824cfe9fe80785), committer for many others (due to rebasing) |
| Anastasia V. | Helped with anomaly research menu script                                                | [[GDrive]](https://drive.google.com/drive/folders/1bim_RES0xtbw3b0T58dC509Yp944mw-7) (original commit is lost due to multiple rebases)                                                                                                                                                  |

## Plan for Next Week

| Who          | Plans to do what                                 |
| ------------ | ------------------------------------------------ |
| Andrey V.    | Implement Anomaly logic and connect Resources     |
| Danil N.     | Implement Anomaly logic, documentation           |
| Anastasia V. | Create instances of Anomalies and help with code |

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
