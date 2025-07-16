Week \#3

## MVP Development

### **Deliverables**

* Code repository: [GitHub](https://github.com/IU-Capstone-Project-2025/SignGame)

* Project TaskBoard: [Trello](https://trello.com/b/g98QWgRE/sign-game)

* Interactive board of ideas: [Miro](https://miro.com/welcomeonboard/NjllanVudnhUd2Fhd3RGQUpCMlN0S3d2Nm9SakkrNzI1YVhsK0VKYmZpQkR6Titjc2xycjRyNnpYRTNGRTlvNyt5anpZa3R4TkZVUEdwNjIwdDVTcjdqQksyeUJBbTcreDg3cXNHWllsZFk2VWlhSHRvTTJ2aU5uU3BuR2hvRG5NakdSWkpBejJWRjJhRnhhb1UwcS9BPT0hdjE=?share_link_id=131423753479)

This week we developed the MVP of our project, making the main functionality of our future game.

### Implemented MVP features

* Built the main gameplay scene in Unity2D with core character movement and basic animations

* Designed and added UI and character sprites

* Configured colliders and in-scene navigation

* Integrated ML model into Unity2D to recognize signs

* Added area of economic strategy with items in the store 

In general, a finished MVP fragment was created in a week: the user can launch the game, go through the first scene, interact with objects and use jamming to move on.

### Full user journey

0. Launch the game

1. Click "Start game" button

2. Player enters the first location — the cave

3. Interact with objects (enemies, coins, store)

4. User is prompted to draw a symbol

5. ML model performs symbol recognition

6. Sign accuracy deals damage, using it, defeat all enemies

7. Progress to the next location

### Demonstration of the Working MVP

You can view the demo and screenshots [here](https://drive.google.com/file/d/1gOAShk36HPOXfU-XGOHnhAzwJOA_3oHy/view?usp=sharing)

### ML

We fully developed, trained and integrated ML model

- Training code source: [code](https://github.com/IU-Capstone-Project-2025/SignGame/blob/main/static_ml/model.py)

- Initial model artifacts: [artifacts](https://github.com/IU-Capstone-Project-2025/SignGame/blob/main/static_ml/test_dataset_generation.ipynb)

- Trained model: [ONNX model](https://github.com/IU-Capstone-Project-2025/SignGame/blob/main/static_ml/CNNModelC%23/CNN_model.onnx)

*We also have a [model documentation](https://github.com/IU-Capstone-Project-2025/SignGame/blob/main/static_ml/doc.md), where described how we trained your model, what data used and what parameters model uses to make decisions*

## Internal demo

During testing we identified the following issues:

* No clear instruction on what symbol to draw

* Sometimes a dash works incorrectly

* Sometimes the hero's spells are applied too slowly and are canceled when pressed again

* There is no accurate recipe for the spell, it is not known what to mix with

* There is no explanation of the game process lore

Then we discussed the priority of this ideas

### Priority tasks

This tasks will completed during next week

* Diversify the game with a second location and add a connection between the initial one
  
* Develop a level boss
  
* Impose visual effects on spells

* Adding traps to current and future levels

* Store design and full functionality

### Need to be discussed

This problems will fixed during next week

* Fix hero abilities work

* Fix spell cast- and tick rate

### Need to be done later 

This conflicts need to be resolved, but for now it is not prioriry target

* Optimize current game process

* Update some beta applied textures or models

### Core Feature Implementation

1. All game features were discussed between the participants, balancedly [distributed](https://trello.com/b/g98QWgRE/sign-game) and completed

2. Design textures and/or animations were issued on all the necessary models

3. Integrated ML model

4. All work merged in the [main branch](https://github.com/IU-Capstone-Project-2025/SignGame)

*You can view the process of forming individual areas of the game in more detail in the corresponding [branches](https://github.com/IU-Capstone-Project-2025/SignGame/branches)*

## Game features

### Main menu

![Main menu](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/assets/MainMenu.gif)

### Hero base movement

![Movement](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/assets/Movement.gif)

### Dash ability

![Dash](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/assets/dash.gif)

### Checkpoint

![Checkpoint](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/assets/checkpoint.gif)

### Game currency - Coins

![Coins](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/assets/coins.gif)

### Store

![Store](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/assets/store.gif)

### Spell cast

![Fireball](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/assets/spell.gif)

## Weekly commitments

### Individual contribution of each participant

Each member of the team made significant during MVP development!

Sviatoslav Fediaev:

* Enemy attacks
  
* Updated enemies taunt mechanics 
  
* Enemy [damage dealing](https://github.com/IU-Capstone-Project-2025/SignGame/commit/18d2caf8dafcbb240593fb164d7d68a8ad92d1f3) and respawn after small time

Valeriia Kolesnikova:

* Mechanics of [collecting coins](https://github.com/IU-Capstone-Project-2025/SignGame/commit/ea56c60c43a63636a54d5757b8e09d0fa6fcfdd1) and their logic

* Items purchase 

* Combining of an storekeeper animation with opening or closing the store 

* HP display in the interface and buying HP boost in the store

Fanis Zinnurov:

* Spells for the fire element and their bind to keys 1, 2 and 3

* Enemy taking damage and death
 
* Some [technical changes](https://github.com/IU-Capstone-Project-2025/SignGame/commit/10821f94f7dbe20b16831fcc2bb29088d6723e54) to attack scripts

Egor Savchenko:

* Creation of mechanics of trap-chip

* Mechanics of obtaining damage

* Merging and [resolving problems](https://github.com/IU-Capstone-Project-2025/SignGame/commit/dd100336a94ceae10005f302679562d22573ef12) of all Unity work

Danil Valiev:

* Creation and actively management [TaskBoard](https://trello.com/b/g98QWgRE/sign-game);
  
* Organization of team meetings, as well as meetings with TA;

* MVP location plan, CI/CD update

* Creating [Week 3 report](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/week3.md).

Nikita Stepankov:

* ML model [documentation](https://github.com/IU-Capstone-Project-2025/SignGame/blob/main/static_ml/doc.md);
  
* Generalize and automate process of generating [datasets](https://github.com/IU-Capstone-Project-2025/SignGame/blob/main/static_ml/test_dataset_generation.ipynb) and training of model;

* [Merge](https://github.com/IU-Capstone-Project-2025/SignGame/pull/11) model to actual branch.

Stanislav Delyukov:

* Special MVP location

* Storekeeper model and animation

* Cursor, HP bar, coins, coin bar and main menu design

* Dash [effect](https://github.com/IU-Capstone-Project-2025/SignGame/commit/9554e9ad7689ff3a1e4ffe88ca94c3b031f2cb0c) 

## Plan for the Week #4

The most important to us is to complete the main game features, then to move on to progression

* MVP bug fix

* Achievement system logic - separate menu of special achievements obtained in different ways

* Traps in any existing level

* Level boss with a special room 

## Confirmation of the code's operability

We confirm that the code in the main branch:

* [✓] In working condition.
* [✓] Run via docker-compose (or another alternative described in the README.md).

*Innopolis University    |   Capstone project    |   Summer 2025*
