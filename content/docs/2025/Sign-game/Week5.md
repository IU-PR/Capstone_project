Week \#4

## Feedback changes

### **Deliverables**

* Code repository: [GitHub](https://github.com/IU-Capstone-Project-2025/SignGame)

* Project TaskBoard: [Trello](https://trello.com/b/g98QWgRE/sign-game)

* Interactive board of ideas: [Miro](https://miro.com/welcomeonboard/NjllanVudnhUd2Fhd3RGQUpCMlN0S3d2Nm9SakkrNzI1YVhsK0VKYmZpQkR6Titjc2xycjRyNnpYRTNGRTlvNyt5anpZa3R4TkZVUEdwNjIwdDVTcjdqQksyeUJBbTcreDg3cXNHWllsZFk2VWlhSHRvTTJ2aU5uU3BuR2hvRG5NakdSWkpBejJWRjJhRnhhb1UwcS9BPT0hdjE=?share_link_id=131423753479)

* Web deploy: [Build](https://iu-capstone-project-2025.github.io/SignGame/WebGL/)

In this week we should update our project, use all feedback sessions with potential users.

## Feedback

### Sessions

*Conduct at least three sessions with potential users, describe detailed user reviews*

In this week we present our current project progress to three groups of people (distributed by age) and collect some information from their feedback to improve our game.

1. **School company**. We presented SignGame during a break between their IU school lessons. *They liked* the concept of the *game and its design*, but they said that *the game is not enough fight content.* 

2. **Innopolis University students**. We asked to play the game our friends who study at the university.
They also *liked it*, especially they note the *design is great*.
But they added that in our game there are *no variety of levels, deceptions and traps*, which is very *base feature of the platformer genres games*,
and that there are more places where code *needs to be optimized*.

3. **Parents**. We also asked some of our own parents (with average 40 y.o.) to play our game to identify problems with the older generation.
They liked the *playstyle*, as well as *its dynamism*.
But they replied that due to the *lack of any train content*, they were *hard to understand the game mechanics*.

There were main takes that we bring from all groups

### Analyze

*Describe the important points that you received from the user feedback, what issues and with which priority you created.*

We came to the conclusion that, regardless of age, our game everyone likes, but there are several problems or game misunderstanding. To solve them, we need:

- Add game-learning content to describe players main game mechanics

- Add boss content and a few enemy types

- Remake level logic to room generation  

- Improve level content, adding some traps or other dangerous entities

- Improve and optimize code style

- Resolve bugs due code conflicts

We are completely focused on the performance of these tasks. At the moment, we have not completed some of these issues, but are configured to be resolved to project demo.

## Iteration & Refinement

### Implemented features based on feedback

#### Lights and particles

![lights](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/assets/week5/particles.gif)

#### Traps

![traps](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/assets/week5/traps.gif)

#### Damage receiving

![receive](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/assets/week5/damage.gif)

#### Vertical platform

![platform](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/assets/week5/platform.gif)

#### Store items

![shop](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/assets/week5/shop.gif)

#### Death Screen

![death](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/assets/week5/death.png)

#### Settings (BETA)

![settings](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/assets/week5/settings.gif)

#### New level logic: room generation (BETA)

![rooms](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/assets/week5/room.gif)

#### Minimap

![map](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/assets/week5/minimap.gif)

### Performance & Stability

*How would we measure the performance of SignGame?*

To measure performance, we will analyze 2 most popular metrics:

1. Frames Per Second (*FPS*).

    * Purpose: have as minimum 60 FPS for target platforms

2. Memory Usage (*RAM*).

    * Purpose: minimize RAM usage to deny some game freezes and crushes.

*Note: now we almost do not observe pr control these parameters. These are our musthave goals after the implementation of all the necessary features*

### Documentation

In this moment we have only [README](https://github.com/IU-Capstone-Project-2025/SignGame/blob/main/README.md) file which describes

- Main game lore

- Team members: their names and project tracks

- Install instruction

- Some additional technical information

*For futute we will improve this documentation, adding some useful and technical information*

### ML Model Refinement

For this week, we improve model accuarcy by increasing dataset and add variarity in size of syntetic images in dataset. For future increase input demension to 256x256, also find with gridSearch best hyperparameters like batch_size and threshlod

## Weekly commitments

### Individual contribution of each participant

#### Danil Valiev

- [Week 5 report](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/week5.md?plain=1)

- Feedback [tasks distribution](https://trello.com/b/g98QWgRE/sign-game), Taskboard managing

- Team and TA meetings organization

#### Valeriia Kolesnikova

- UI and design of [Death Screen](https://github.com/IU-Capstone-Project-2025/SignGame/commit/cd3a8595da0c6132a985653155a32d51a31122fd)

- Changed shop view, added shop [item animation](https://github.com/IU-Capstone-Project-2025/SignGame/commit/1a3e0561b1c6e09cd98e34c540ff6e3ef5cf05e1)

- 3 new shop [items](https://github.com/IU-Capstone-Project-2025/SignGame/commit/0cfedef927f8f31578c26c1d22d43ef59785a4b7)

- Shop buying logic

#### Sviatoslav Fediaev

- Fully developed enemies land movement

- New enemy type: [Patrolmen](https://github.com/IU-Capstone-Project-2025/SignGame/commit/a177749d6e3ce279154d0eaa47ace7c3baf3df7e) 

- Enemy attacks: [optimize old and added new](https://github.com/IU-Capstone-Project-2025/SignGame/commit/0fb1ea23b42157afb86c67f48700747685f4fb10) for new enemies

#### Egor Savchenko

- Added new [level system](https://github.com/IU-Capstone-Project-2025/SignGame/commit/4ee7d495b1877b0d41e2942ae51921d3a636c2c8)

- Added [level minimap](https://github.com/IU-Capstone-Project-2025/SignGame/commit/d2f635bf33284a9c805ee3488514ffb89068de28)

- Resolving conflicts while merging content into Development and Main branches

#### Stanislav Delyukov

- New enemies animation: moving

- Remade gameplay, [graphics updates](https://github.com/IU-Capstone-Project-2025/SignGame/commit/59f464ca905efd3b1bea73a871594b6eab8a453f)

- Attack [sprites and particles](https://github.com/IU-Capstone-Project-2025/SignGame/commit/1bb84bc5ae579f794a648ee9048761160977e9fe) in coins, damage receive, checkpoint 

#### Nikita Stepankov

- Add [saving](https://github.com/IU-Capstone-Project-2025/SignGame/tree/main/static_ml) of user drawnings

- Partially integrate model to Unity code

- Improve [model accuracy](https://github.com/IU-Capstone-Project-2025/SignGame/blob/main/static_ml/model.py)

#### Fanis Zinnurov

- Developed [spell book](https://github.com/IU-Capstone-Project-2025/SignGame/commit/b8208c519ca9242407bdca3cf1bc0fa3c6f69228): the history of casted spells

- [Corrected](https://github.com/IU-Capstone-Project-2025/SignGame/commit/4bf4643c7def6ea7dfa13088158a56109af83d7e) the effect of the spell that causes the effect on the cursor

### Plan for the next week

*In Week 6, we plan to:*

- Release Week 5 bugfix 

- Prepare project for **release production**

- Develop bossfight, add new rooms

- Optimize code and project size

## Confirmation of the code's operability

We confirm that the code in the main branch:

* [✓] In working condition.
* [✓] Run via docker-compose (or another alternative described in the README.md).

*Innopolis University    |   Capstone project    |   Summer 2025*
