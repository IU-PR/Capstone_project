Week \#1

## Project description

### **Sign Game**

Code repository: [link](https://github.com/IU-Capstone-Project-2025/SignGame)

**Sign game** project is a *2D Unity platformer*, about *a mysterious wizard*, seeking to defeat evil in its world by his power \- *magical runes*.

### Team members

| Team Member | Telegram Alias | Email Address | Track | Responsibilities |
| :---- | :---- | :---- | :---- | :---- |
| Sviatoslav Fediaev *(Lead)* | [@SfedBro](http://t.me/SfedBro) | [s.fediaev@innopolis.university](mailto:s.fediaev@innopolis.university) | Game development | Enemy intelligence;<br>Enemy movement |
| Danil Valiev | [@Dorley](http://t.me/Dorley) | [d.valiev@innopolis.university](mailto:d.valiev@innopolis.university) | DevOps <br>Documentation | Linting;<br>Build optimizing;<br>Report structure   |
| Valeriia Kolesnikova | [@Codekd](http://t.me/Codekd) | [v.kolesnikova@innopolis.university](mailto:v.kolesnikova@innopolis.university) | Game development | Shop concept;<br>Characteristics display;<br>GUI |
| Stanislav Delyukov | [@shines\_light](http://t.me/shines_light) | [s.delyukov@innopolis.university](mailto:s.delyukov@innopolis.university) | UX/UI <br>Design | Draw models;<br>Sign patterns;<br>Game field structure   |
| Fanis Zinnurov | [@qobz1e](http://t.me/qobz1e) | [f.zinnurov@innopolis.university](mailto:f.zinnurov@innopolis.university) | Testing <br>Documentation | Bug finding;<br>GitHub repo structure |
| Egor Savchenko | [@KOSMOGOR](http://t.me/KOSMOGOR) | [e.savchenko@innopolis.university](mailto:e.savchenko@innopolis.university) | Game development | Base movement;<br>Character abilities  |
| Nikita Stepankov | [@NikitaXLV](http://t.me/NikitaXLV) | [n.stepankov@innopolis.university](mailto:n.stepankov@innopolis.university) | Machine Learning | Sign recognition;<br>Accuracy of drawn figures  |

## Brainstorming

### Ideas during brainstorming 

We decide to complete our Ideas in order, by their priority:

1. **Drawing symbols for battle** *(main idea)*  
   The player *fights with enemies*, quickly *drawing* the *symbols* that appear on the screen.   
   The more accurately and faster it draws \- the stronger and faster the attack. 

2. **Symbols combo**  
   Several symbols drawn *in a row and for a small period* of time will create a *combo*.   
   Combo delivers a *critical damage* depending on the complexity of the symbols.  
     
3. **Increasing the complexity of enemies and values**  
   The player *defeats the enemies*, uses progressively more *complex combos*, learning new symbols and getting new abilities.  
     
4. **Progressing with store purchases**  
   From the defeated enemies and some places on the map, the player will receive *coins* that can be exchanged with the merchant in the *store*.   
   Store \- a *single (small) shop* at a *certain point on the map.*	  
     
5. **Setting up the skills of the character**  
   The possibility of *customization* of the hero: set some of *available symbols/abilities.*

 

### Brief market research / problem validation 

We analyzed the market of such games and collected a small sum of information about them:

| Game                         | Short description                                     | Advantages                                | Disadvantages               |
|------------------------------|------------------------------------------------------|-------------------------------------------|-----------------------------|
| Divineko                     | Draw symbols to defeat enemy                         | Same fight principle;<br>2D;<br>Simple game design | Rare gameplay changes;<br>Monotonous |
| Turgor                      | Manage resources used to draw symbols, to live       | Economy strategy;<br>3D                   | Old game;<br>Too “innovative” |
| Magic Touch: Wizard for Hire| Draw symbols as fast as you can to make score better | Simple game structure;<br>Max-score principle | No progression;<br>Monotonous  |

## Basic requirements

### Target users and their primary needs

**Target audience:**

* Casual players looking for fast and unique combat mechanics.  
    
* Fans of original games with elements of reaction skills.  
    
* Players interested in visually aesthetic 2D games with fantasy stylistics.

**Primary needs:**

* Dynamic and intuitive gameplay with understandable mechanics.  
    
* Satisfaction from overcoming the call: to draw accurately and quickly.  
    
* Progress and reward for the development of skills (new symbols, abilities, enemies).  
    
* A clear visual feedback of actions.

### User stories

* As a user, I want controls to be plain and responsive.   
    
* As a user, I want a detailed tutorial to easily acknowledge basic mechanics.  
    
* As a user, I want a high-quality atmosphere for complete/full immersion.

* As a user of complex games, I want an interesting battle with the boss to acquire pleasant memories after passing.  
    
* As a user, I want to see interesting mechanics in the game, so that it is interesting to play throughout the game.


### 

### Initial scope

* Drawing signs to win enemies;  
    
* Pumping, opening interesting mechanics;  
    
* Vertical 2D game;  
    
* Boss at the end of the location;  
    
* Reviving enemies;  
    
* One resource for pumping and access to the boss.

## 

## Tech stack

While sharing the work, we also discussed the technologies that we will use in the project. Convenient and practical technologies were selected for each IT sphere.

### Technology distribution

| IT sphere  | Technology                                                                  |
| ----- | ----- |
| Game development | Unity (2D), C\#, Unity Engine |
| Machine Learning | Python, Tensorflow, ML.NET, Keras.NET |
| DevOps | Git, GitHub Actions |
| Testing | NUnit, Unity Test Framework |
| Version Control | Git, GitHub |
| UX/UI | Unity UI Toolkit, Canvas System, Figma, Miro |
| Asset Management | Unity Asset Store |

### 

### 

## 

## Weekly commitments

### Individual contribution of each participant

| Member name          | Week #1 contribution                                                                                          |
|----------------------|---------------------------------------------------------------------------------------------------------------|
| Sviatoslav Fediaev   | Setting up team members and their roles;<br>Repository setup;<br>Participation in Miro;<br>Assisting in meeting organization; |
| Danil Valiev         | The biggest part in PDF Report creating;<br>Assisting in first code setup;<br>Participation in Miro;<br>Technologies Stack organization. |
| Valeriia Kolesnikova | Assisting with member recruiting;<br>Meeting and stand-ups organization;<br>Participation in Miro.            |
| Stanislav Delyukov   | Miro board creation and management;<br>Ready-made concepts of a character and enemies.                        |
| Fanis Zinnurov       | Completing a GitHub part of week #1 work report;<br>Assisting in selection of stack technologies;<br>Participation in Miro. |
| Egor Savchenko       | Discussing the concept of the game;<br>Formatting Main branch;<br>Loading the first Build.                    |
| Nikita Stepankov     | Writing the first ML algorithm on a separate branch;<br>Work in dataset generation and model design;<br>Participation in Miro |


### Contribution references:

1. Main branch in GitHub repository: [https://github.com/IU-Capstone-Project-2025/SignGame](https://github.com/IU-Capstone-Project-2025/SignGame)  
2. ML branch in GitHub repository: [https://github.com/IU-Capstone-Project-2025/SignGame/tree/feature\_ml](https://github.com/IU-Capstone-Project-2025/SignGame/tree/feature_ml)  
3. First project release: [https://github.com/IU-Capstone-Project-2025/SignGame/releases/tag/0b](https://github.com/IU-Capstone-Project-2025/SignGame/releases/tag/0b)  
4. Miro board: [https://miro.com/welcomeonboard/NjllanVudnhUd2Fhd3RGQUpCMlN0S3d2Nm9SakkrNzI1YVhsK0VKYmZpQkR6Titjc2xycjRyNnpYRTNGRTlvNyt5anpZa3R4TkZVUEdwNjIwdDVTcjdqQksyeUJBbTcreDg3cXNHWllsZFk2VWlhSHRvTTJ2aU5uU3BuR2hvRG5NakdSWkpBejJWRjJhRnhhb1UwcS9BPT0hdjE=?share\_link\_id=131423753479](https://miro.com/welcomeonboard/NjllanVudnhUd2Fhd3RGQUpCMlN0S3d2Nm9SakkrNzI1YVhsK0VKYmZpQkR6Titjc2xycjRyNnpYRTNGRTlvNyt5anpZa3R4TkZVUEdwNjIwdDVTcjdqQksyeUJBbTcreDg3cXNHWllsZFk2VWlhSHRvTTJ2aU5uU3BuR2hvRG5NakdSWkpBejJWRjJhRnhhb1UwcS9BPT0hdjE=?share_link_id=131423753479)

### How to install and start the game

1. Come to releases page by the link: [https://github.com/IU-Capstone-Project-2025/SignGame/tags](https://github.com/IU-Capstone-Project-2025/SignGame/tags)
2. Choose the latest one
3. Download archive file (**.zip**) and extract files in any folder
4. Open installing (**.exe**) file
5. Enjoy our game!
