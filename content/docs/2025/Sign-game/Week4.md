Week \#4

## Post-MVP optimization and automation 

### **Deliverables**

* Code repository: [GitHub](https://github.com/IU-Capstone-Project-2025/SignGame)

* Project TaskBoard: [Trello](https://trello.com/b/g98QWgRE/sign-game)

* Interactive board of ideas: [Miro](https://miro.com/welcomeonboard/NjllanVudnhUd2Fhd3RGQUpCMlN0S3d2Nm9SakkrNzI1YVhsK0VKYmZpQkR6Titjc2xycjRyNnpYRTNGRTlvNyt5anpZa3R4TkZVUEdwNjIwdDVTcjdqQksyeUJBbTcreDg3cXNHWllsZFk2VWlhSHRvTTJ2aU5uU3BuR2hvRG5NakdSWkpBejJWRjJhRnhhb1UwcS9BPT0hdjE=?share_link_id=131423753479)

* CI/CD configuration: [web version](https://github.com/IU-Capstone-Project-2025/SignGame/blob/main/.github/workflows/lint_build_deploy.yml) and [OS autobuild](https://github.com/IU-Capstone-Project-2025/SignGame/blob/main/.github/workflows/platform_builds.yml)

* Deployed game version: [deploy](https://iu-capstone-project-2025.github.io/SignGame/WebGL/)

In this week we should update our project to ensure quality through testing, automate processes, and prepare for future deployment.

## Testing and QA

### Testing strategy 

* Base testing system:

  1. Feature developer is **locally testing** a new game update and pushes

  2. In case of success, **pushes** changes to the optional branch

  3. Makes **pull request** to the main branch

  4. **Linting** of the incoming code occurs

  5. In case of success, **pushes** changes to the [main branch](https://github.com/IU-Capstone-Project-2025/SignGame)

* Additionally system for ML model:

  1. Dataset **creation**
 
  2. Dataset is **divided** into teaching, validation and test

  *Here you can see [ML tests](https://github.com/IU-Capstone-Project-2025/SignGame/blob/main/static_ml/model.py)*

### Evidence of test execution

#### C# Linter log and result 

![linter](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/assets/lint.png)

#### WebGL Lint & Build & Deploy result

![webgl](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/assets/web.png)

#### OS build 

![os](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/assets/OS.png)

## CI/CD

### Description

CI/CD s a technology for testing and delivery of new features/modules of the project being developed. We use this technology and build special *.yml* files, which can:

- Lint all C# code

- Build game for any existing operationg system

- Deploy web version as a website

### Tools used

- **GitHub Pages** - GitHub module which can deploy project as a [website](https://iu-capstone-project-2025.github.io/SignGame/WebGL/)

- **csharpier** - C# linter library

- [Game.ci](https://game.ci) builder module - Feature to build Unity project in any OS

### Challenges faced

1. Too hard to manage C# code issues

    * Since C# is a OOP-structured language with syntax structure.
  
    * Even if the code is written bad, but in compliance with the syntax rules, that won't count as an issue.

2. Project delivery (CI)

    * Since project total size is too big to *game.ci builder*, there is need to minimize it with *archiving*

    * Without *Decompression fallback* setting, there is no possibility to unpack our project

3. Project deployment (CD)

    * Due to the fact that we badly worked out the window parameters, depending on the browser, the game UI can change 

### CI/CD configuration files

#### Web lint & build & deploy

[web version](https://github.com/IU-Capstone-Project-2025/SignGame/blob/main/.github/workflows/lint_build_deploy.yml) 

#### Windows, MacOS and Linux builds

[OS autobuild](https://github.com/IU-Capstone-Project-2025/SignGame/blob/main/.github/workflows/platform_builds.yml)


### Deployment 

#### Staging deployment

1. **Build WebGL Version in Unity:**
   - Open `File → Build Settings` and switch the platform to **WebGL**.
   - Disable unused or incompatible plugins/features for WebGL.
   - Export the build as a pre-release archive.

2. **Deploy to GitHub Pages (*gh-pages* branch):**
   - We use a separate Git branch to host the staging version.
   - We use GitHub Actions to automate the upload build to this branch.

3. **Access Staging Build:**
   - The staging version is accessible at:
     ```
     https://iu-capstone-project-2025.github.io/SignGame/WebGL/
     ```

## Vibe check

Our members is steadily progressing with the Unity project ans work as a team. The core gameplay loop is in place, and WebGL builds are successfully generated and deployed to GitHub Pages for both staging and production environments. 

- We usually meet (3 times in a week) and discuss our successes and problems

- Everyone is contributing consistently

- Tasks are well-distributed across game development, ML, DevOps and Design areas.

## Weekly commitments

### Individual contribution of each participant

#### Danil Valiev

- **All CI/CD content**

- [Pull Request template](https://github.com/IU-Capstone-Project-2025/SignGame/blob/main/.github/pull_request_template.md)

- [Week 4 report](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/week4.md)

- Main branch rulesets

- Repository cleaning

#### Valeriia Kolesnikova

- Restoting HP nearly checkpoint, removing const HP saving 

- Obtaining damage [vizualize](https://github.com/IU-Capstone-Project-2025/SignGame/commit/f564732d90c28fa11ca3f15b4aee64e51195a227)  

- Storekeeper [vanishing animations](https://github.com/IU-Capstone-Project-2025/SignGame/commit/7e2a7f97ab1783836fdf0a449682b1ac5cf53f4c)

- Interaction mechanic change:

  1. [Checkpoint](https://github.com/IU-Capstone-Project-2025/SignGame/commit/63d73d4335faa8d5ed9a74010252589bc6c5db4c): option to activate checkpoint replaced from **bind E nearly** to **stay nearly checkpoint a few seconds**

  2. [Storekeeper](https://github.com/IU-Capstone-Project-2025/SignGame/commit/7e2a7f97ab1783836fdf0a449682b1ac5cf53f4c): option to open shop replaced from **bind F nearly** to **stay nearly storekeeper a few seconds**

#### Sviatoslav Fediaev

- [Patrolling enemies](https://github.com/IU-Capstone-Project-2025/SignGame/pull/41) in a small radius

- Design of the new enemy with Stanislav

- Assisting in the new player spell attacks 

#### Egor Savchenko

- [Map](https://github.com/IU-Capstone-Project-2025/SignGame/pull/43) logic and first action

- [Moving platform](https://github.com/IU-Capstone-Project-2025/SignGame/pull/45) logic

- Merging all members work into a main branch

#### Stanislav Delyukov

- Main menu music OST applied

- Design of the new enemy with Sviatoslav

#### Nikita Stepankov

- Finalize [ML model](https://github.com/IU-Capstone-Project-2025/SignGame/blob/main/static_ml/model.py) work

- Start work in integration model into C# code

#### Fanis Zinnurov

- Spell code optimization

- New [water spell](https://github.com/IU-Capstone-Project-2025/SignGame/commit/2d52e97ef4020c768fc20cf60a37b322036cb7a8)

- Changed [enemy status](https://github.com/IU-Capstone-Project-2025/SignGame/commit/d93ea70ed3618959918f500f15c6e3bea487dbec) realizing 

  * Now the effects are in an enemy state. It allows to interact with them (elemental reaction)

- Reworked [spell logic](https://github.com/IU-Capstone-Project-2025/SignGame/tree/946b9798749c98363d11b427beaa91030758e84b)

  * Now spells works as **ScriptableObject**

### Plan for the next week

*In Week 5, we plan to:*

- Release Week 4 bugfix 

- Start work with music assets

- Start work with boss location and boss himself

- Realize total game progress saving  

## Confirmation of the code's operability

We confirm that the code in the main branch:

* [✓] In working condition.
* [✓] Run via docker-compose (or another alternative described in the README.md).

*Innopolis University    |   Capstone project    |   Summer 2025*
