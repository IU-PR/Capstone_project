---
title: "Week #1"
---

# Week #1

## Project description

### Project name: Project fly

**Code repository**: https://github.com/IU-Capstone-Project-2025/ProjectFly

This project is a request for the development of a solution for agricultural drone use. 
The task is involve development of the a system for measuring the liquid level in a UAV tank for spraying agricultural crops.

### **Team Members**

| Team Member							| Telegram Alias	| Email Address   					| Track												| Responsibilities   |
|---------------------------------------|-------------------|-----------------------------------|---------------------------------------------------|--------------------|
| Dmitriy Vizitei (Lead)				| @otkisaev			| d.vizitei@innopolis.university 	| Low level (embedded) + Testing engineer  			| Project coordination, task delegation, programming and testing prototypes |
| Senea Belykh							| @SenyaZenya		| s.belykh@innopolis.university		| Low level (embedded) + Electric circuit engineer	| Programming and testing prototypes |
| Dmitry Ryabov							| @theDioxider		| d.ryabov@innopolis.university 	| Low level (embedded) + Electric circuit engineer 	| Programming and testing prototypes |
| Anas Hamrouni							| @reachnasta		| a.hamrouni@innopolis.university   | Design engineer 									| Designing 3D models |
| Andrew Pavlov							| @chaleshka_0		| and.pavlov@innopolis.university	| Tech writer 										| Document the work and write reports |


## Brainstorming

### Ideas during brainstorming

During the brainstorming, several sensor options were proposed:
- A conventional float sensor
- A sensor that detects the presence of liquid based on the resistance of the liquid

### Brief market research / problem validation

As drones become more and more popular, they are becoming more widely used in various industries. 
In this case, we received a request from the customer with a problem with UAV tank on agricultural drone, that he can't solve more then year.


## Basic requirements

### Target users and their primary needs

People that use drones in the agricultural industry.

### User stories

The customer is faced with the problem that the liquid from a UAV tank stops being transferred, although there is still enough liquid in a UAV tank.

### Initial scope


Development of sensor prototypes using an existing board. 
Development of an embedded sensor. 
Testing prototypes on the raw version of the tank.

## Tech-stack

| Field					| Stack							|
|-----------------------|-------------------------------|
| Embeded programming	| C/C++, Cube IDE, Arduino IDE	|
| Design engineer		| NX Seimens					|
| Sensors Mechanics		| Math + physics				|


# Weekly commitments

## Individual contribution of each participant

| Member					| Contribution					|
|---------------------------|-------------------------------|
| Dmitriy Vizitei			| Core repository structure: [initialized repository](https://github.com/IU-Capstone-Project-2025/ProjectFly/commit/19ece8dd689269b8877637c0cdd9e248106d6f66); [created README with min. info](https://github.com/IU-Capstone-Project-2025/ProjectFly/commit/e50a447534157cbb9bf82c0cbb02ca23cbfe9245), meetings organization, [coding for sonar sensor](https://drive.google.com/file/d/1LidOm8-sfzgR6SBzXvL8MPFwJuZYcI2e/view) and [drew conclusions](https://drive.google.com/file/d/1uPqIGXmfji8wScobm7uN8mmkmz8bqaa-/view)  |
| Senea Belykh				| Experiments with sonar sensor and potential measure across different liquids: [1 photo](https://drive.google.com/file/d/1iks-ICr-Jj6YDTbC_7g15NeuBZ0NiNc6/view), [2 photo](https://drive.google.com/file/d/1U9N12xxdES-TP-YdTxnyD7aCKuFkxgFy/view) |
| Dmitry Ryabov				| Developing the sketch model for float - measuring solution and mechanical approach to it: [1 photo](https://drive.google.com/file/d/1B1FFSR7dEByimEyTBBDzXpCQsAIk3exs/view), [2 photo](https://drive.google.com/file/d/1paRiFeqJcF4dm9tiB3F9iAVMbtcniBE8/view) |
| Anas Hamrouni				| Assembly and 3d printing of prepared slice of given fuel tank: [1 photo](https://drive.google.com/file/d/1lN4BLDHryvy0sIiT8JNs3DoKl2EEyYCS/view), [2 photo](https://drive.google.com/file/d/1RkKiIEnV-A94Wn-GcgxEGb1zZ3Kr0lAV/view), [3 photo](https://drive.google.com/file/d/1N7Sre0JA2KTpTBYblD5QK42kd-GkthfW/view), [4 photo](https://drive.google.com/file/d/1aHhj54TxobaaM10KJL29bydH0yrErl8g/view), [5 photo](https://drive.google.com/file/d/1IxX14vZsZe_04kBdniVQ5BPaV8_wYsOM/view)|
| Andrew Pavlov				| Designed the repository: [made simple dockerfile && docker-compose, filled README](https://github.com/IU-Capstone-Project-2025/ProjectFly/commit/1e72d54a43d55706654bb48358b227a1712d22fd) |

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).