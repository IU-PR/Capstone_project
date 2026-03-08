Week \#6

## Final Touches & Presentation Preparation

### **Deliverables**

* Final code repository: [GitHub](https://github.com/IU-Capstone-Project-2025/SignGame)

* Project TaskBoard: [Trello](https://trello.com/b/g98QWgRE/sign-game)

* Interactive board of ideas: [Miro](https://miro.com/welcomeonboard/NjllanVudnhUd2Fhd3RGQUpCMlN0S3d2Nm9SakkrNzI1YVhsK0VKYmZpQkR6Titjc2xycjRyNnpYRTNGRTlvNyt5anpZa3R4TkZVUEdwNjIwdDVTcjdqQksyeUJBbTcreDg3cXNHWllsZFk2VWlhSHRvTTJ2aU5uU3BuR2hvRG5NakdSWkpBejJWRjJhRnhhb1UwcS9BPT0hdjE=?share_link_id=131423753479)

* Platform latest release: [Build](https://github.com/IU-Capstone-Project-2025/SignGame/releases)

* Web deployment: [WebGL](https://iu-capstone-project-2025.github.io/SignGame/WebGL/)

* Project demo presentation: [Presentation](https://docs.google.com/presentation/d/1RX8xcfw6oEav7Q2sfGo8DmW_MLkJcZ34UFYdDegXTGk/edit?usp=sharing)

* Game assets: [Design and sounds](https://github.com/IU-Capstone-Project-2025/SignGame/tree/main/Assets/Prefabs/Map), [Implemented features](https://github.com/IU-Capstone-Project-2025/SignGame/tree/reports/assets)

* Project documentation: [README](https://github.com/IU-Capstone-Project-2025/SignGame/blob/main/README.md)

In this week we finalize the project, prepare all deliverables, and craft a compelling presentation.

## Final deliverables

### Project overview

Nowadays, the majority of Rogue-Like or Platformer games are deprived of additional game improvement, and either their main game logic is only on the basic movement (WASD and Jumps), or this is a mobile game that initially has many technical problems. **Sign Game** is a solutions in this problems, because project solves this problems:

- Two interaction activities: walking and drawing

- Gameplay, based on levels with a special rooms and unique entities or items

- Providing setting to customize music and effect volume level

### Features

**Sign Game** includes the following core components

1. Main Menu Interface: A central hub for player to access game levels and settings

2. Settings Page: Allow players to change music volume and hero nickname, and access to the main game scenes

3. Level generation: Special script allows to create levels based on available rooms with unique exits

4. Spells: Allow players combine drawn signs to create a spells, which can be useful in some game situations

5. Fighting: Players may fight with level enemies using special spell that they can combine

6. Shop and Checkpoint: Entities with which players can interact to buy items or restore health

7. Progress saving: Project stores game progress and will restore him after any time where players starts the app

*More details about implemented game features described in previous report or [here](https://github.com/IU-Capstone-Project-2025/SignGame/tree/reports/assets)*

### Tech stack

This is the final technical stack that we used.

| IT sphere  | Technology                                                                  |
| ----- | ----- |
| Game development | Unity (2D), C\#, Unity Engine |
| Machine Learning | Python, Tensorflow, Barracuda |
| DevOps | Git, GitHub Actions, GitHub Pages |
| Version Control | Git, GitHub |
| UX/UI | Unity UI Toolkit, Canvas System, Figma, Miro |


### Setup instructions

There are 2 ways to start our project

#### Setup as a player

1. Come to game **[releases](https://github.com/IU-Capstone-Project-2025/SignGame/releases)**

2. Download the **latest one**

3. Extract **all files** from archive to any folder on your PC

4. Open **setup (.exe)** file

#### Setup as a developer

1. Clone repository to your PC:

```bash
git clone https://github.com/IU-Capstone-Project-2025/SignGame
cd SignGame
```

2. Choose option

* If you want to edit scripts and some assets, you need to install some IDE (for example, **Visual Studio Code**)

- IDE

* If you want to edit levels, prefabs or manage full project work, you need to work with **Unity Hub** and combine editing with previous method.

- Unity Hub

- Unity version: 6000.0.50f1 LTS 

- IDE

## Weekly commitments

### Individual contribution of each participant

#### Danil Valiev

- [Week 6 report](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/week6.md)

- Level [room scenes](https://github.com/IU-Capstone-Project-2025/SignGame/commit/b1ddc38b163f210e12285aff94d329868ae8fa78)

- Music and effect sounds source, shop items icons

- Team and TA meeting organization

#### Valeriia Kolesnikova

- Fixed the issue of [layering UI](https://github.com/IU-Capstone-Project-2025/SignGame/commit/3c35aee42a980420317c134f7f42a43c4b35dcd9)

- Adding an indicator that shows the player's approach to the merchant

- Implementing [scroll texture](https://github.com/IU-Capstone-Project-2025/SignGame/commit/3c35aee42a980420317c134f7f42a43c4b35dcd9) in the store and correcting animations

- Fixed and fully completed [settings](https://github.com/IU-Capstone-Project-2025/SignGame/commit/543b5baec97be6b557ff2a869fc46ed5f2238fb4)

#### Sviatoslav Fediaev

- Enemies bug&fix

- Boss [logic](https://github.com/IU-Capstone-Project-2025/SignGame/commit/a2726b370be2a0722f0da4cd93ad8a240b79ce1d) and fighting system

- Game design

#### Egor Savchenko

- Implemented [music and effect sounds](https://github.com/IU-Capstone-Project-2025/SignGame/commit/bccd3475a304a38156e85a17d1bb5d5e7ca60b0f) into scripts

- Level [generation](https://github.com/IU-Capstone-Project-2025/SignGame/commit/efbb11a290ed1905f155268ec9fbad31c3683e87) using room prefabs

- Assisting in boss logic and fighting system

#### Stanislav Delyukov

- Room template 

- Enemies [effect system](https://github.com/IU-Capstone-Project-2025/SignGame/commit/6153216c5574fde69399f7db6f68e987826257e7)

- Shop item scroll design

#### Nikita Stepankov

- Fully [integrate](https://github.com/IU-Capstone-Project-2025/SignGame/commit/8e9a24adef2361701e70af0071d2f7f5936e6148) ml model to unity code (to attack event)

- [Refactor ml model](https://github.com/IU-Capstone-Project-2025/SignGame/commit/f833a79ae249e8b65377be946b16bd99675b6bd0) to be more precise on human drawnings (7 out 12 class recognition)

- Refactor [dataset creation](https://github.com/IU-Capstone-Project-2025/SignGame/commit/f833a79ae249e8b65377be946b16bd99675b6bd0) with more real data instead of syntetic

#### Fanis Zinnurov

- [Linked](https://github.com/IU-Capstone-Project-2025/SignGame/commit/b4c0eb4983bfe047f89b9d99f3cb0c86664ab141) spell animation with their casts

- Spell book [animation](https://github.com/IU-Capstone-Project-2025/SignGame/commit/cd7128f0d3d398a19fd7bd41417000437db418cb) and freeze while opening

- New [spells](https://github.com/IU-Capstone-Project-2025/SignGame/commit/f8b2e0a1025ef09265d97470a9799c48524a060d)

### Plan for the next week

*In Week 7, we plan to:*

- Fix critical bugs before freeze date

- Prepare project presentation 

## Confirmation of the code's operability

We confirm that the code in the main branch:

* [✓] In working condition.
* [✓] Run via docker-compose (or another alternative described in the README.md).

*Innopolis University    |   Capstone project    |   Summer 2025*
