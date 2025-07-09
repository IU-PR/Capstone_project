---
title: "Week #4"
---

# **Week #4**

## Testing and QA

To ensure quality and stability, we implemented automated Edit Mode tests covering key gameplay interactions and dialogue logic using the Unity Test Framework with NUnit.

Our testing approach includes:
- Unit tests for backend logic (e.g., destination setting in the ClickToMove component).
- Integration-like tests for UI and dialogue components (ClickableChoiceNPC, ClickableNPC) written in EditMode using UnityTest and coroutines.
- Although written in Edit Mode, some tests simulate runtime behavior such as player interaction with NPCs and dialogue state changes.

We focused on:
- Core user interaction logic
- NPC dialogue flow and feedback
- UI state updates based on input

We grouped all tests under the EditMode folder for simplicity and CI integration. No PlayMode folder was used at this stage, though test logic simulates in-game behavior using coroutines and Unity APIs.



### Evidence of test execution

We configured GitHub Actions to automatically run Edit tests on every push to main. This ensures immediate feedback on regressions.

For know its covered most core functionallity implemented parts of the game.

Evidence includes:
- Console output confirming test case execution and results
- CI test passed or not  
![photo](https://github.com/IU-Capstone-Project-2025/UniTrip/blob/main/assets/week4/tests.png)
## CI/CD

We used GitHub Actions to implement a Continuous Integration (CI) pipeline that automatically builds and tests the Unity project upon each push or pull request.

 CI (Continuous Integration)
Tool: GameCI  
Jobs:  
- Install Unity via game-ci/unity-installer  
- Run tests via game-ci/unity-test-runner
- Shows the output
- Triggers: push to main branch

During the creating test we faced many issues, most of them with pipeline and unity licence activation. Then with tests and showing it. It was hard without hard knowledges in unity and ci.

Also we asked for help for another team and thanks them for help, also they suggested us to add password and email to the pipeline, which help to solve problem with licence

🎯 CD (Continuous Deployment)

We are preparing to deploy the project as a WebGL build to GitHub Pages.  
But also faced many issues and decided to stop this week on partially manualy deploy (will be fixed next week).


### Links to CI/CD configuration files
[yml file](https://github.com/IU-Capstone-Project-2025/UniTrip/tree/main/.github/workflows).  
[pipeline with tests](https://github.com/IU-Capstone-Project-2025/UniTrip/actions/runs/16034371739)

## Deployment

For now we have a manual deploy by using gh-pages, becuase we had a lot of issues with github actions and with leak of knowledge is hard.  
The pipeline for now is following:
1) Build new WebGL folder from Unity
2) Push it manually into branch gh-pages
3) Get the web verison of the game on ph-pages 

## Vibe Check

We expressed everything from vibe check meet in note below.
If summarize - everything is okay, just keep going, try do our best, finish tasks fitted in deadlines and not burn out. Because of leakage of time the most part of team feel stressful, but our PM tried their best to balances the load on people to reduce it, however in some cases it is unavoidable.

[Note](https://docs.google.com/document/d/1f6m22t6EfzSDliiiNOmndoccPE47s9JppX4Eyub-HZk/edit?tab=t.0)


# Weekly commitments

## Individual contribution of each participant

**Marina Lavrova(Lead)** - organized work and 2 team meets, including team [vibe check](https://docs.google.com/document/d/1f6m22t6EfzSDliiiNOmndoccPE47s9JppX4Eyub-HZk/edit?usp=sharing), help with solving problem of broken project, ci/ci pipeline and communicate with other teams for help, support team during difficulties and trim [backlog](https://unitrip.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog?selectedIssue=SCRUM-59) to prioritize tasks  

**Merkulov Leonid** - Fix bugs noticed in first location, upload 2nd location to Unity and implement first part of interactions(Student and professor Shilov without 3d models), add unit tests and ci/cd pipline with deploy. 
all commits are [here](https://github.com/IU-Capstone-Project-2025/UniTrip/commits/main/) 

**Ivan Makarov** - trained a [model](https://drive.google.com/drive/folders/1tLW5yMGEfuf8ABdVGM7FMp_B2li4KbN-?ths=true) more, add a [connection](https://github.com/IU-Capstone-Project-2025/UniTrip/commits/main/) of model to Unity

**Tarubarova Nadia** - created 3D model of [2nd location](https://drive.google.com/drive/folders/1DzZf5G3drAUxYQ7efT0owwVSzABO9ym5), fixed [texts](https://docs.google.com/document/d/1mmvHvr4fpMwKyKiBfT46mgTayXwXYcIJl-K7-KaqPdQ/edit?usp=sharing)  

**Pokhodyaeva Polina** - сreated [sprites](https://drive.google.com/drive/folders/1IYyMJyNqzhusT-nD66-ULbLXSscwRTMB?ths=true) for the 108 auditorium, created [sprites](https://drive.google.com/drive/folders/18uRJz-ha5B0eQUZthT0oTfeQjx_a9wBX?ths=true) for background for the 2nd location, collected fonts and fixed [text sprites](https://drive.google.com/drive/folders/1KsW154ZuQXik0OXDuvlWU6mL0Q5XtTSD?usp=sharing)


## Plan for Next Week

- Create prototypes for characters on the second location
- Create a characters for the second location
- Fix 2nd location 3D model and update in Unity
- Create sprites for vending mashine
- Implement the second part of interactions in the second location
- Provide QA session with feedback 
- Finalize training a model
- Add chat with ML model to the information desk(without design)
- Find soundtracks and sound effects

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [✓] In working condition.
- [✓] Run via docker-compose (or another alternative described in the `README.md`).