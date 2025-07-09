---
title: "Week #5"
---

# **Week #5**

## Feedback

### Sessions
We conducted several meets with different categories of people.  
First of all - with our customer to check if the game suits his vision and if he likes it. So, if summarize his words - he accept the game interface and flow. Say to add more interactions and we imediately complete it during this sprint.  

Then - with our students to check if the game close to real university vibe and atmosphere. And they noticed that game has a calm mood, which close to their feelings in university, what is good.

And the last section - the potenial users. People from other cities, which never was here and interested in Innopolis as a city. They like the game, the flow and also say some suggestions to improve

Full feedback description you could see [here](https://docs.google.com/document/d/18jO7jkPARBSpUbOItuzbafxS_JxLzX5jkgCeENqB4MU/edit?tab=t.0)


### Analyze

*Describe the important points that you received from the user feedback, what issues and with which priority you created.*.  
We recieved that our game is interesting, funny and good looking, but we need to fix a lot of bugs to make user expereince better.  
People suggest us to add more interactions, shadows with light, fill the background and fix some bugs with walking, animation and interactions.

We created several issues, parts of them completed this week:  
1. Add more interactions - add 2 interactions(108 auditorium and vending mashine)
2. Fill the background with the color.  
Also for next week we planned to continue fixes according to feedback and will:

1. Add the correct characters to the 2nd location
2. Fig bug with Professor Burmyakov asset
3. Improve interaction flow
4. Improve moving of the main character
5. Improve the animation of character's moving
6. Add shadows and ligth to the scenes

All the tasks stays with priority order. We focused first of all on main things, which is crutial for our project and will do as much as we can, but in priority way to not miss important things.  
First priority - good performance without bugs, second - the better visual.

## Iteration & Refinement

### Implemented features based on feedback
As we wrote above, the implemented features are following:
1. Add more interactions - add 2 interactions(108 auditorium and vending mashine)
2. Add the correct characters to the 2nd location
3. Fill the background with the color.  


### Performance & Stability

Our main measure of performance is a user interess and involvement in game process. It is absolutely random and not consistent parameter, but we could increase the probability of fullfiling it by enhancing the stability and quality of our game.  
So, during final week we need to focus on the bug fixed to provide users more comfort user flow without some erros and easier in use. Also we need to focus on visual part, so will increase animations performance and add a main welcome screen to make a good first impression of the game. 

### Documentation

To be honest, for now we do not have any documentation, because our users will have only game and actually do not need nothing except the game. All user flow is intuitive and not needed to be explained.  

For futute we will make a documentation for the guides, which will provide our game during excoursions, with tips for better user experience. But for now we do not have any functionality and extra features in the game, which needed to be explain.  

So the only thing that we need to document - is to how download/open our game and we still want to complete autodeploy, but faced many issues which we cannot solve yet.  
So, we will add full description for setup the game in main [README](https://github.com/IU-Capstone-Project-2025/UniTrip) file in the repo.

### ML Model Refinement

To improve model we increased dataset size, update the marking and fine tune the model. Also we transfered it to cloud, because it takes a lot of time to train it locally.
Also to improve model we need to increased the dataset more and tune it, until we get the satisfied results.
# Weekly commitments

## Individual contribution of each participant

**Marina Lavrova(Lead)** - organized work and testing sessions with processing [feedback](https://docs.google.com/document/d/18jO7jkPARBSpUbOItuzbafxS_JxLzX5jkgCeENqB4MU/edit?usp=sharing), updated and re-prioritized the [backlog](https://unitrip.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog?selectedIssue=SCRUM-29), updated [ci/cd](https://github.com/IU-Capstone-Project-2025/UniTrip/commit/310fa3b88d0286b4436193e6a34e96bb3f90d6c2) and tried to fix bugs with deploy (for now still unsuccessful)

**Merkulov Leonid** -  implemented the second part of [interactions](https://github.com/IU-Capstone-Project-2025/UniTrip/commits/main/), added [background](https://github.com/IU-Capstone-Project-2025/UniTrip/commits/main/) with color to locations, fixed bug with [passing throug 1st guard](https://github.com/IU-Capstone-Project-2025/UniTrip/commit/fbcb8eeced956ba8cd1fa666020cf13539e4f766), fixed [bugs with dialogues](https://github.com/IU-Capstone-Project-2025/UniTrip/commit/a5384183b894242749f32dfdb6f3b5174caa31b0) on the second scene

**Ivan Makarov** - learned model, transfered model to the [cloud]() to finalize learning, created [script](https://github.com/IU-Capstone-Project-2025/UniTrip/commit/3e930e661fc34a4ecddb3c609ba8fdd2af5db01f) for the chat implementation in Unity

**Tarubarova Nadia** - created [3D models of characters](https://drive.google.com/drive/folders/1SCWUktnMDkrhyACH4vOi0N1BnLhQe6C3?usp=sharing) for the second location, participated in collecting [feedback](https://docs.google.com/document/d/18jO7jkPARBSpUbOItuzbafxS_JxLzX5jkgCeENqB4MU/edit?usp=sharing) with testing session  

**Pokhodyaeva Polina** - created prototypes for [characters](https://drive.google.com/drive/folders/19CA7RVZOQfAbg5DHafCf4LmoHkSbdUoy?ths=true) on the second location, created sprites for vending machine [interaction](https://drive.google.com/drive/folders/1l544Uui6k347hi8mKcw143-x9YVVuBGj?ths=true)
## Plan for Next Week
- Design of the first screen(logo and start button)
- Create sprites for chat with ML
- Add design of the welcome screen to Unity
- Add interaction with ML chat in Unity
- Improve the visual part and fix bugs
- Add soundtracks (if will have time)
- Create a final presentation


## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).