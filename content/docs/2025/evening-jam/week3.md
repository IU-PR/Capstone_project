---
title: "Week #3"
---

# **Week #3**

## Implemented MVP features

Our MVP includes core mechanics implementation as a base for the developing gameplay. Right now, we have:

- the [movement](https://github.com/evolutionleo/Capstone-2025/commit/240ccae0369598a1a325bd159815cc488674264e) of the player is implemented

- a starting set of empty [levels](https://github.com/evolutionleo/Capstone-2025/commit/ea8649c54e851f08ec1a17e079e312ddde290510) with designed [backgrounds](https://github.com/evolutionleo/Capstone-2025/commit/a47ab97d76e9545cde6638aa1e28576505701782) 

- implemented [lamp mechanics](https://github.com/evolutionleo/Capstone-2025/commit/1c18e0b88c2564f7cc4d017136531a35d670034e): the player can pick them up, place into designated sockets and activate mechanisms (for example, a bridge)

- the [interaction with the npcs](https://github.com/evolutionleo/Capstone-2025/commit/1c18e0b88c2564f7cc4d017136531a35d670034e) and [dialogue window](https://github.com/evolutionleo/Capstone-2025/commit/c0892f44dac87e79c8824b6ed0d18ddd11f07f6f) are implemented 

- some mechanisms are now present in the form of placeholders to display the future functionality 

This MVP forms a base for the future detailed development in the following weeks. 

### The user journey 

Movement and world exploration

- The player can control the movement of the character using W, A, S, D and Space for jumping

Interaction with the lamps and mechanisms

- The player can pick up and put down a lamp by pressing E
- The player can activate the mechanism by putting a lamp into it 

NPC interaction

- If NPC are present, pressing F will trigger a dialogue 

Navigation shortcuts

- F4 to go to the previous level

- F5 to restart the current level

- F6 to skip to the next level

- Ctrl + F5 to restart the whole game

## Demonstration of the working MVP

[The repository with implementation](https://github.com/evolutionleo/Capstone-2025)

[Video demo](https://youtu.be/HfcIS501ZTU)


## Internal demo

### Strong sides

- Movement is responsive and goes without lagging
- Core lamp mechanics are done and work smoothly
- The shortcuts help with debugging
- The designs are harmonious and look good

### Functional weaknesses

- no animation makes the gameplay look too static
- placeholders should be replaced asap
- npcs should be added for storytelling opportunities
- no music is added yet, though is in progress

### Team organisation

- since two members are not able to be present at discussions physically, the group meetings are harder to organise, we should take it into account more and find means of easier communication 

# Weekly commitments

## Individual contribution of each participant

- Dmitry Korletynu: 
    - team organization
    - added an [npc sprite](https://github.com/evolutionleo/Capstone-2025/commit/0204721bdab40da21d7e5ba7a4a979881ce1bb75)
    - [level design](https://docs.google.com/document/d/1LlTyt_cxw3sljkO4-UPljxDbiX3mdZn26JJxUg8c63Q/edit?usp=sharing)
- Lev Ivanov: 
    - [a sequence of empty levels](https://github.com/evolutionleo/Capstone-2025/commit/ea8649c54e851f08ec1a17e079e312ddde290510)
    - [lighbulbs and npcs](https://github.com/evolutionleo/Capstone-2025/commit/1c18e0b88c2564f7cc4d017136531a35d670034e) and [dialogue box](https://github.com/evolutionleo/Capstone-2025/commit/c0892f44dac87e79c8824b6ed0d18ddd11f07f6f)
    - [energy system](https://github.com/evolutionleo/Capstone-2025/commit/91dee58a636d3ecb0f4405ad550ec76d77ce6cfd)
    - [level transition](https://github.com/evolutionleo/Capstone-2025/commit/1d3e90fd503edebc46616547b8938ea049b779d6) and [debug cheatcodes](https://github.com/evolutionleo/Capstone-2025/commit/b976c9c382fcb4eb44e4023e4b5410a1effe65cf)
    - [player controls improved](https://github.com/evolutionleo/Capstone-2025/commit/240ccae0369598a1a325bd159815cc488674264e)
    - [initializer room + lighting test](https://github.com/evolutionleo/Capstone-2025/commit/fbcd671a48caa658d0ac0bcd6ae531458679e1f3)
    - [level design](https://docs.google.com/document/d/1LlTyt_cxw3sljkO4-UPljxDbiX3mdZn26JJxUg8c63Q/edit?usp=sharing)
- Ulyana Yanovitskaya: 
    - [level design](https://docs.google.com/document/d/1LlTyt_cxw3sljkO4-UPljxDbiX3mdZn26JJxUg8c63Q/edit?usp=sharing)
- Veronika Levasheva:
    - this report
    - [extended version of the first track](https://drive.google.com/file/d/1KFaNlOjRa3GvwmQFbs7H60GLHEDfS87o/view?usp=sharing)
- Bulat Shigapov:
    - [designed backgrounds](https://docs.google.com/document/d/1Atrx-hVSO6tmEkwe1dREJji7B9UFaqKRLlV8gW07qBw/edit?usp=sharing)
    - [updated previous sprites](https://github.com/evolutionleo/Capstone-2025/commit/a36ab70cbb441e57c10807e9a730526df42bdf1e)

## Plan for Next Week

### Things to code

- code the jump pad
- put the second level together

### Narrative and level design

- formulate the level design for the second level
- write the second level dialogues

### Visual Design

- make backgrounds for the second level
- animate objects for interaction

### Sound design

- write the second soundtrack

### Organisation

- group call to discuss the process
- keep consistent chat communication

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [ ] Run via docker-compose (or another alternative described in the `README.md`).
