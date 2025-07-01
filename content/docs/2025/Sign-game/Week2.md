Week \#2

## Detailed Requirements Elaboration

### **Sources**

* Code repository: [GitHub](https://github.com/IU-Capstone-Project-2025/SignGame)

* Project TaskBoard: [Trello](https://trello.com/b/g98QWgRE/sign-game)

* Interactive board of ideas: [Miro](https://miro.com/welcomeonboard/NjllanVudnhUd2Fhd3RGQUpCMlN0S3d2Nm9SakkrNzI1YVhsK0VKYmZpQkR6Titjc2xycjRyNnpYRTNGRTlvNyt5anpZa3R4TkZVUEdwNjIwdDVTcjdqQksyeUJBbTcreDg3cXNHWllsZFk2VWlhSHRvTTJ2aU5uU3BuR2hvRG5NakdSWkpBejJWRjJhRnhhb1UwcS9BPT0hdjE=?share_link_id=131423753479)

* Week 2 demo preview: [Demo](https://drive.google.com/file/d/1ZlTNwjkXILwU5iktKVtxvfjICnNpqr_m/view?usp=sharing)

* Week 2 release: [Release](https://github.com/IU-Capstone-Project-2025/SignGame/releases/tag/w2)

This week our project is prepared for the **MVP stage** - the functionality of the tasks required for it is *gradually added and tested*.

### Changes

After meeting with TA, we came to the conclusion that we need to change a little the distribution of member roles in our team:

| Team Member |  Email Address | Track | 
| :----  | :---- | :---- |
| Sviatoslav Fediaev *(Lead)*  | [s.fediaev@innopolis.university](mailto:s.fediaev@innopolis.university) | Unity developer | 
| Valeriia Kolesnikova  | [v.kolesnikova@innopolis.university](mailto:v.kolesnikova@innopolis.university) | Unity developer | 
| Fanis Zinnurov  | [f.zinnurov@innopolis.university](mailto:f.zinnurov@innopolis.university) | Unity developer | 
| Egor Savchenko  | [e.savchenko@innopolis.university](mailto:e.savchenko@innopolis.university) | Unity developer | 
| Danil Valiev  | [d.valiev@innopolis.university](mailto:d.valiev@innopolis.university) | Project Manager<br>DevOps| 
| Nikita Stepankov  | [n.stepankov@innopolis.university](mailto:n.stepankov@innopolis.university) | Machine Learning | 
| Stanislav Delyukov  | [s.delyukov@innopolis.university](mailto:s.delyukov@innopolis.university) | UX/UI<br>Design | 

## Project specific progress

### Game development

1. Added **release** with **test location** to check current project progress;

2. **Main hero** *design* and *animations*, *dash* ability;

3. Created **enemies**, their *taunt* logic and base *movement*;

4. **Main menu** for future management of various play settings;

5. Basic **signs**, their **combinations**, the ability to **draw**, as well as a **model for their recognition**;

6. **Checkpoints** and *saving overall progress* when leaving the game.


### Design

1. Created all location textures in front and background, stone assets for platforms; 

2. Developed main character movement and animations in different states;

3. Checkpoint logic and design;

4. Created test location. 

### ML

1. Detailed dataset creation with different object positions;

2. Model training for existing symbols;

3. Model attaching to C# code from Unity.

### DevOps

1. Check of existing and new scenes from the incoming commit;

2. Code check for grammatical errors and evaluation system.


## Weekly commitments

### Individual contribution of each participant

Each member of the team made significant changes this week!

Sviatoslav Fediaev:

* Enemies base movement
  
* Enemies taunt mechanics to the main character
  
* [Signs](https://trello.com/c/EogBRSpp/11-паттерны-символов), their effects and patterns

Valeriia Kolesnikova:

* Implemented the functionality of the [starting menu](https://github.com/IU-Capstone-Project-2025/SignGame/tree/MainMenuScene)
  
* Created a [store functionality](github.com/IU-Capstone-Project-2025/SignGame/commits/TheStorageSystem/)
  
* [Checkpoint mechanics](https://github.com/IU-Capstone-Project-2025/SignGame/commit/3f190782281aeec257330792547c0222a0084cff)

* Implemented the collection of coins, as well as the saving and tracking of their number

Fanis Zinnurov:

* Applying effects on the target
  
* Implemented combos
  
* 3 types of [attacks](https://github.com/IU-Capstone-Project-2025/SignGame/tree/Attacks) for 3 different elements

Egor Savchenko:

* Main hero [movement](https://github.com/IU-Capstone-Project-2025/SignGame/commit/855b1ef1dc5ca194d613dba6b07f91a550649d32) 
  
* Drawing signs on the screen
  
* [Combining features](https://github.com/IU-Capstone-Project-2025/SignGame/tree/Development) of all participants of this week in a single job

Danil Valiev:

* Creation and actively management [TaskBoard](https://trello.com/b/g98QWgRE/sign-game);
  
* Creation [CI/CD](https://github.com/IU-Capstone-Project-2025/SignGame/tree/main/.github/workflows) for directory validation, as well as code lint;
  
* Organization of team meetings, as well as meetings with TA;

* [Week 1 report](https://github.com/IU-Capstone-Project-2025/SignGame/blob/reports/week1.md) editing and creating [Week 2 report](https://github.com/IU-Capstone-Project-2025/SignGame/edit/reports/week2.md).

Nikita Stepankov:

* Developed Dataset Creation
  
* Model [training](https://github.com/IU-Capstone-Project-2025/SignGame/blob/feature_ml/static_ml/model.py)
  
* Connecting a recognition model to all project

Stanislav Delyukov:

* Assets and sprites of all textures were developed to build the first levels
  
* Created [test location](https://drive.google.com/file/d/1ZlTNwjkXILwU5iktKVtxvfjICnNpqr_m/view?usp=sharing) 
  
* Main hero texture and animations

* Created checkpoint design and logic 

### Plan for Week #3

The main goal of this week is to *prepar*e a project *for MVP stage*. To fulfill this goal, we need to **finalize or complete the following tasks**:

* **Achievement system**: their *list* and mechanics of *achieve*

* A full opportunity to **buy items in a store**

* **Design** of a merchant, items, currencies for purchase, main menu and enemies

* The mechanics of **revival** of enemies

* **Spell testing** using the keyboard

*For more information about the tasks, their distribution and responsibilities for each development week, you can visit our [TaskBoard](https://trello.com/b/g98QWgRE/sign-game)*

##

Innopolis University, Capstone project, June 2025
