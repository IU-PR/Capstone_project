---
title: "Week #4"
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

# Week 4

## Play our Demo

[Also avaliable with multiplayer capabilities for Windows, Linux, and MacOS on Itch\.io.](https://localt0aster.itch.io/thecoorp)

<iframe loading="lazy" frameborder="0" src="https://itch.io/embed-upload/14046546?color=333333" allowfullscreen="" width="640" height="380"><a href="https://localt0aster.itch.io/thecoorp">Play TheCOOrP on itch.io</a></iframe>

## Testing and QA

Due to the complex and rapid changing nature of our project, we could only afford to have a compilation and 1 frame survival test. The rest must be tested manually.

### Evidence of test execution

[![GdUnit4 Tests](https://github.com/TheTopSecretTeam/TheCOOrP/actions/workflows/gdunit.yml/badge.svg)](https://github.com/TheTopSecretTeam/TheCOOrP/actions/workflows/gdunit.yml)

<https://github.com/TheTopSecretTeam/TheCOOrP/actions/workflows/gdunit.yml>

![Image](https://github.com/user-attachments/assets/9625754b-7bfc-4756-8543-6526c873a74c)


## CI/CD

We used slightly modified [abarichello's godot-ci](https://github.com/abarichello/godot-ci) for building and deploying to [GitHub Pages](https://thetopsecretteam.github.io/TheCOOrP/) and [Itch\.io](https://localt0aster.itch.io/thecoorp), [GdUnit4](https://github.com/MikeSchulze/gdUnit4) Godot plugin with [gdunit4-action](https://github.com/marketplace/actions/gdunit4-test-runner-action) for Unit Testing.

It was a bit painful to implement, due to Godot export issues we did not know about. [[gdUnit4 issue]](https://github.com/MikeSchulze/gdUnit4/issues/627#issuecomment-2571567152)

The CI is built using GitHub Action with Secrets and Variables set in place.

### Links to CI/CD configuration files

<https://github.com/TheTopSecretTeam/TheCOOrP/blob/46d28a42124dea674efc0b8c8723f513c11c0cbb/.github/workflows/gdunit.yml>

<iframe frameborder="0" scrolling="no" style="width:100%; height:20em" allow="clipboard-write" src="https://emgithub.com/iframe.html?target=https%3A%2F%2Fgithub.com%2FTheTopSecretTeam%2FTheCOOrP%2Fblob%2F46d28a42124dea674efc0b8c8723f513c11c0cbb%2F.github%2Fworkflows%2Fgdunit.yml&style=default&type=code&showBorder=on&showLineNumbers=on&showFileMeta=on&showFullPath=on&showCopy=on&maxHeight=720"></iframe>

<https://github.com/TheTopSecretTeam/TheCOOrP/blob/46d28a42124dea674efc0b8c8723f513c11c0cbb/.github/workflows/godot-ci.yml>

<iframe frameborder="0" scrolling="no" style="width:100%; height:40em;" allow="clipboard-write" src="https://emgithub.com/iframe.html?target=https%3A%2F%2Fgithub.com%2FTheTopSecretTeam%2FTheCOOrP%2Fblob%2F46d28a42124dea674efc0b8c8723f513c11c0cbb%2F.github%2Fworkflows%2Fgodot-ci.yml&style=default&type=code&showBorder=on&showLineNumbers=on&showFileMeta=on&showFullPath=on&showCopy=on&maxHeight=720"></iframe>

## Deployment

### Staging

<!-- *Details about the deployment process, environment setup for staging environment* -->

We deploy the main (stable) branch to Itch\.io and GitHub Pages, the rest is tested for playability via Unit Tests and playtesting.

### Production

Our production is the Itch\.io website, which allows us to distribute our game freely and receive revenue. We don't have Steam in our plans yet.

## Vibe Check

<!-- *Facilitate a team health check. Discuss progress, roadblocks, and team dynamics. Ensure everyone feels heard.* -->
Our main challenge is teaching the first year bachelors how to work with Godot and git. They are making progress, but some still forget to pull the latest commits or somehow create an orphan branch. We have 2 meetings each week, because we have 2 reports.

## Weekly commitments

### Individual contribution of each participant

| Who          | Did what                                                                                                                                                | Proof                                                                                                                                                                                                                                                                                                                             |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Andrey V.    | Implemented anomaly logic and escaping sequence, merged branches, created sprites for Resources, conducted 2 meetings, and distributed tasks for week 4 | [[a688c31]](https://github.com/TheTopSecretTeam/TheCOOrP/commit/a688c31e18410b792ad050fc10c36ec3781862b6), [[f636aaa]](https://github.com/TheTopSecretTeam/TheCOOrP/commit/f636aaa7960404109f6c05071e0fd90313a5579b)                                                                                                              |
| Danil N.     | Proper Unit Testing, merged branches, selection highlight, researched complex tiling and expansion options, this report                                 | [[288ed1d]](https://github.com/TheTopSecretTeam/TheCOOrP/commit/288ed1d258704e38cd1f7f158ad2c1dc56e536e7), [[46d28a4]](https://github.com/TheTopSecretTeam/TheCOOrP/commit/46d28a42124dea674efc0b8c8723f513c11c0cbb), [[Issue\#59]](https://github.com/TheTopSecretTeam/TheCOOrP/issues/59)                                       |
| Anastasia V. | Fixed bugs with UI, created Resource Display node, polished research menu                                                                               | [[11935b7]](https://github.com/TheTopSecretTeam/TheCOOrP/commit/11935b7330aa24f70f31f1ef974e333fcb2207e5) , [[cf06f51]](https://github.com/TheTopSecretTeam/TheCOOrP/commit/cf06f5199061ebf9ae1905e3870b992bc46e8826) , [[e178329]](https://github.com/TheTopSecretTeam/TheCOOrP/commit/e178329c4c3c9b4c24c484ee39e4f8d522d17e31) |

### Plan for Next Week

| Who          | Plans to do what                     |
| ------------ | ------------------------------------ |
| Andrey V.    | Finish core mechanics of the game    |
| Danil N.     | Polishing                            |
| Anastasia V. | Create new Anomalies, help with code |

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
