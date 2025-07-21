---
title: "Week #5"
---

# **Week #5**

## Feedback

### Sessions

We conducted three sessions with our potential users and gained the following insight: 

| Participant| Pros      | Cons                                                  | Suggestion |
| ------------------------------------- | --------- | -------------------------------------------------------- | ------- |
| Maxim - an experienced gamer who mostly plays on PC | Quickly understood the controls, liked the idea of using lamps | Graphics felt "unfinished", didn’t understand the purpose of the NPC | Make the lamps more noticeable and "interactable" |
| Artyom - a game designer interested in philosophy and indie games | Found the setting intriguing, liked the atmospheric lamps | Gameplay felt too short and overly simple | Add more interactive objects and expand on the idea of light as a symbolic element |
| Andrey - a hobbyist developer | Appreciated the bridge and energy mechanics | Lacked feedback during interactions (no sounds or visual effects) | Add visual and audio effects to enhance interaction feedback |

### Analyze

| Problem                               | Priority  | Comment                                                  | 
| ------------------------------------- | --------- | -------------------------------------------------------- |
| Underdeveloped graphics               | High      | Affects first impressions and overall atmosphere         |
| Short and simple gameplay             | Medium    | Needs at least 2–3 levels or some form of progression    |
| Lamps are not clearly key elements    | High      | Should be visually and narratively emphasized            |
| Lack of interaction feedback          | Medium    | Enhancing it will improve immersion                      |
| NPC lacks narrative purpose           | Medium    | Add dialogue, a quest, or some hint of a storyline       |

## Iteration & Refinement

### Implemented features based on feedback

In progress:

- NPC dialogue: Dialogue with light philosophical undertones is written and ready, but not yet added to the build

- Graphics enhancement: We've started reworking the background and interactive objects, focusing on a "paper-like" visual style

Will be added in the next runs:

- Visual and sound effects: We're planning to add animations for lamp activation and other mechanisms

- Level expansion: We plan to add 1–2 more scenes with new puzzles and interactions


### Performance & Stability

| Metric                | Current Value                           | Improvement Potential                                |
|-----------------------|-----------------------------------------|------------------------------------------------------|
| FPS on standard PC    | 60+ FPS                                 | Stable, but not tested on low-end devices            |
| Level loading time    | < 1 second                              | Acceptable, though resource optimization is possible |
| Stability             | No crashes                              | Stability level is acceptable                        |
| Number of bugs        | 0 found                                 | —                                                    |


### Documentation

We have multiple documentation documents for various parts of our project: 

- Technical documentation 
    - [Game Design Document](https://docs.google.com/document/d/1Vo9ULr0iiDlRrvzsPDKi_QGgH3iBMy6o6v2Kx9lyGMw/edit?usp=sharing). Contains general description, team information, the main mechanics ideas and plot summarisation. This document is the main reference for all game components
    - [Level design in Figma](https://www.figma.com/design/ug2Id0lJdqkA6U6IL1Cmds/Untitled?node-id=592-3&t=SLnBhW5YGFaIlANR-1). We had to keep the clean and consise workspace with a collaborative opportunities for the level design formulation and we chose to do it in Figma

- [Detailed plot with all dialogues](https://docs.google.com/document/d/1Ul-d97mPKF-ZTrO-CHl08b0JdEY6rSsgcE8PJKCeIiA/edit?usp=sharing). The document is up to date with all relevant changes and provides an opportunity for quick reviews, feedback and sharing

- [README with the project description](https://github.com/evolutionleo/Capstone-2025/blob/main/README.md). The DEADME currently only contains the descriptions but will be elaborated with the game local setup instructions in the next runs

# Weekly commitments

## Individual contribution of each participant

- Dmitry Korletynu: 
    - team organization
    - organised the sessions with the potential users and assessed the metrics
    - [worked on the level 2 design](https://docs.google.com/document/d/1W190nFbnwszOzWxLTKID2sHAAxvsDKtxP2FoA8v9g0U/edit?usp=sharing)
- Lev Ivanov: 
    - code revision
- Ulyana Yanovitskaya: 
    - [worked on the level 2 design](https://docs.google.com/document/d/1W190nFbnwszOzWxLTKID2sHAAxvsDKtxP2FoA8v9g0U/edit?usp=sharing)
- Veronika Levasheva:
    - put the report together
    - [worked on the dialogues for the second level](https://docs.google.com/document/d/1Ul-d97mPKF-ZTrO-CHl08b0JdEY6rSsgcE8PJKCeIiA/edit?usp=sharing)
- Bulat Shigapov:
    - worked on backgrounds and overall style 

## Plan for Next Week

### Things to code

- code the shutters (doors and platforms)
- put the second level together

### Narrative and level design

- finalise dialogues

### Visual Design

- animate walking
- make the backgrounds for the next scenes 
- refine and animate objects for interaction
- lamp animation

### Sound design

- add sound feedbacks 

### Organisation

- group call to discuss the process
- keep consistent chat communication

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [ ] Run via docker-compose (or another alternative described in the `README.md`).