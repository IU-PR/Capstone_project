---
title: "Week #5"
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

# Week 5

## Play our Demo

[Also avaliable with multiplayer capabilities for Windows, Linux, and MacOS on Itch\.io.](https://localt0aster.itch.io/thecoorp)

Or you can play the single player version here:

<iframe loading="lazy" frameborder="0" src="https://itch.io/embed-upload/14046546?color=333333" allowfullscreen="" width="640" height="380"><a href="https://localt0aster.itch.io/thecoorp">Play TheCOOrP on itch.io</a></iframe>

## Feedback

### Sessions

#### First session:

- A visual cue is needed to show which room they can be sent to.
- The controls feel awkward: scrolling the map with the mouse-wheel is great, but both selecting and sending employees are on the left-click. It would be clearer if sending were done with the right mouse button to avoid mis-click errors.
- If player clicks outside the panel, the anomaly-work menu stays open. With the employee list already open, clicking the anomaly again stacks the job list on top of it.
- The employee list should appear under the chosen job, and the job list itself should stay open after you pick one.
- Holding a modifier key (e.g., <kbd>Shift</kbd>) should let player left-click-drag to select several employees at once; the whole group then moves to the target room together. When working with an anomaly, every selected employee can be shown at the top of the list.

#### Second session:

- Fix cursor display bug, during which the cursor is shown twice and in the wrong place.
- Ability to select multiple agents using drag select.
- Ability to close all menus with X button.
- Nicknames should be shown under cursors.
- Visual cue is needed to show selected room?

#### Third session:

- Most of the feedback were overlapping with previous sessions.
- Highlighted bugs related to battle system.
- Ability to restart the day would be nice.

### Analyze

<!-- *Describe the important points that you received from the user feedback, what issues and with which priority you created.* -->
All sessions underlined a lack of polishing, which is expected because we were prioritizing the core mechanics first.
We have prioritized and created GitHub issues for a majority of stated issues

## Iteration & Refinement

### Implemented features based on feedback

- Agent and room highlighting
- Adjusted controls
- UI fixes

### Performance & Stability

Our project is very lightweight with insignificant load times and low frame time, so performance is not our issue.

### Documentation

Our project documentation consists of the terminology, and occasional inline comments. Game projects may need documentation for modding implementation, but we don't have plans for that. Gameplay documentation (wikis) is traditionally a community's job.

# Weekly commitments

## Individual contribution of each participant

| Who          | Did what                                                                                                                                     | Proof                                                                                                                                                                                                                                                                                                                                                            |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Andrey V.    | Expanded anomaly behaviour script, battle system fixes, connected equipment system, merged branches, conducted playtest sessions             | [[issue#55]](https://github.com/TheTopSecretTeam/TheCOOrP/issues/55), [[issue#9]](https://github.com/TheTopSecretTeam/TheCOOrP/issues/9), [[issue#83]](https://github.com/TheTopSecretTeam/TheCOOrP/issues/83), [[issue#86]](https://github.com/TheTopSecretTeam/TheCOOrP/issues/86)                                                                             |
| Danil N.     | Agent and room highlighting, adjusted controls, implemented procedural room placement to make game feel bigger, merged branches, this report | [[issue#59]](https://github.com/TheTopSecretTeam/TheCOOrP/issues/59), [[84be4a8]](https://github.com/TheTopSecretTeam/TheCOOrP/commit/84be4a87a2fef1fa2408fdf13d40c274fbdd5ec7), [[issue#73]](https://github.com/TheTopSecretTeam/TheCOOrP/issues/73)                                                                                                            |
| Anastasia V. | UI fixes, agent HP and SP display, created monsters                                                                                          | [[issue#85]](https://github.com/TheTopSecretTeam/TheCOOrP/issues/85), [[issue#84]](https://github.com/TheTopSecretTeam/TheCOOrP/issues/84), [[1b8fa91]](https://github.com/TheTopSecretTeam/TheCOOrP/commit/1b8fa91fc728b840c72939ec1cd7166bf06a134e), [[c83c98d]](https://github.com/TheTopSecretTeam/TheCOOrP/commit/c83c98de5b1a9a867dee5807401979422044f55b) |

## Plan for Next Week

| Who          | Plans to do what |
| ------------ | ---------------- |
| Andrey V.    | polishing        |
| Danil N.     | polishing (🇵🇱) |
| Anastasia V. | polishing        |

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).