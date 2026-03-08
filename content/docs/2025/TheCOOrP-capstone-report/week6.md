---
title: "Week #6"
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

# Week 6

## TheCOOrP

<!-- Badges section -->
![Godot Engine](https://img.shields.io/badge/GODOT-%23FFFFFF.svg?style=for-the-badge&logo=godot-engine) ![GDScript](https://img.shields.io/badge/GDScript-%2374267B.svg?style=for-the-badge&logo=godotengine&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![Itch.io](https://img.shields.io/badge/Itch-%23FF0B34.svg?style=for-the-badge&logo=Itch.io&logoColor=white)

![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)

## Play our Demo

[Also avaliable with multiplayer capabilities for Windows, Linux, and MacOS on Itch\.io.](https://localt0aster.itch.io/thecoorp)

[<img height="64em" src="https://static.itch.io/images/badge-color.svg" alt="available on itch.io" />](https://localt0aster.itch.io/thecoorp)

Or you can play the single player version here:

<iframe loading="lazy" frameborder="0" src="https://itch.io/embed-upload/14046546?color=333333" allowfullscreen="" width="640" height="380"><a href="https://localt0aster.itch.io/thecoorp">Play TheCOOrP on itch.io</a></iframe>

## Links

- **Deployment/Demo**: <https://localt0aster.itch.io/thecoorp>
- **Web Deployment**: <https://thetopsecretteam.github.io/TheCOOrP>
- **GitHub Repo**: <https://github.com/TheTopSecretTeam/TheCOOrP>

## Final deliverables

### Project overview

*Cooperative anomaly management simulator (like Lobotomy Corporation) written in Godot engine.*

*It solves a problem presented by our stakeholder.*

### Features

- **Energy:**
  - Main goal of the game.
  - Anomalies generate energy on interaction with Agents.
- **Resources:**
  - Main currency of the game.
  - Used for unlocking new interactions with Anomalies, and equipment like armor and weapons for Agents.
  - We plan to have four kinds of Resources in the game.
- **Anomaly interactions:**
  - Agents interact with Anomalies to generate Energy (and maybe die in the process).
  - Every Anomaly have default interactions that are general for some groups of Anomalies, and unique interactions that have different consequences (random events).
- **COOPerative Multiplayer:**
  - Multiple players are able to play together via local multiplayer.
- **Anomaly Escaping:**
  - Anomalies have different behaviors that can cause them to Escape the containment and start attacking the Agents in the case of mistreatment.
  - Agents are equipped with armor and weapons to suppress the escaped Anomalies.
- **Map:**
  - Facility consists of corridors, elevators, and containment chambers for the Anomalies.
  - Players should be able to select the Agents and assign them to a Chamber to interact with the Anomaly.
  - Agents then should navigate to the chamber autonomously.

### Tech stack

- Godot Engine
- GDScript
- GitHub Actions

### Development setup instructions

- Clone the repository to a desired location using `git clone https://github.com/TheTopSecretTeam/TheCOOrP.git`
- Just import it into [Godot Engine](https://godotengine.org/download), and you're all set. 👍

## Presentation draft

> <https://docs.google.com/presentation/d/1ttr42u8XmLADHM7Z3rkxbxGosgItds1s3R11Z0HsP54>

<iframe loading="lazy" src="https://docs.google.com/presentation/d/e/2PACX-1vTOitogWHCQ68KWyPUHaCzNEnU5rDeFGikCVov68tagF4LiymGtNofMpIVBvYoBfJAFjyDV02VoDbW-/pubembed?start=false&loop=false&delayms=15000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

# Weekly commitments

## Individual contribution of each participant

| Who          | Did what  | Proof                                                                                                                                                                                                                                                                                              |
| ------------ | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Andrey V.    | polishing | [[ticket #101]](https://github.com/TheTopSecretTeam/TheCOOrP/issues/101), [[ticket #25]](https://github.com/TheTopSecretTeam/TheCOOrP/issues/25), [[ticket #103]](https://github.com/TheTopSecretTeam/TheCOOrP/issues/103), [[ticket #99]](https://github.com/TheTopSecretTeam/TheCOOrP/issues/99) |
| Danil N.     | polishing | [[ticket #105]](https://github.com/TheTopSecretTeam/TheCOOrP/issues/105), [[ticket #60]](https://github.com/TheTopSecretTeam/TheCOOrP/issues/60), [[ticket #67]](https://github.com/TheTopSecretTeam/TheCOOrP/issues/67), [[ticket #65]](https://github.com/TheTopSecretTeam/TheCOOrP/issues/65)   |
| Anastasia V. | polishing | [[ticket #95]](https://github.com/TheTopSecretTeam/TheCOOrP/issues/95), [[ticket #93]](https://github.com/TheTopSecretTeam/TheCOOrP/issues/93)                                                                                                                                                     |

## Plan for Next Week

| Who          | Plans to do what             |
| ------------ | ---------------------------- |
| Andrey V.    | Fix bugs and finish the game |
| Danil N.     | Fix bugs and finish the game |
| Anastasia V. | Fix bugs and finish the game |

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
