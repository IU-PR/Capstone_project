---
title: "Week #3"
---

# **Week #3**

## Team

### **Team Members**

| Team Member							| Telegram Alias	| Email Address   					| Track												| Responsibilities   |
|---------------------------------------|-------------------|-----------------------------------|---------------------------------------------------|--------------------|
| Dmitriy Vizitei (Lead)				| @otkisaev			| d.vizitei@innopolis.university 	| Low level (embedded) + Electric circuit engineer  | Project coordination, task delegation, programming and testing prototypes |
| Senea Belykh							| @SenyaZenya		| s.belykh@innopolis.university		| Low level (embedded) + Electric circuit engineer	| Programming and testing prototypes |
| Dmitry Ryabov							| @theDioxider		| d.ryabov@innopolis.university 	| Low level (embedded) 								| Programming |
| Anas Hamrouni							| @reachnasta		| a.hamrouni@innopolis.university   | Design engineer 									| Designing 3D models |
| Andrew Pavlov							| @chaleshka_0		| and.pavlov@innopolis.university	| Tech writer 										| Document the work and write reports |

## Implemented MVP features
- Functional fragment of sensor
- Programmed stm microcontroller that read, process and output signals from the sensor
- 3d model of sensor road and float with assembly tool
- Finished PCB layout

## Demonstration of the working MVP

https://github.com/user-attachments/assets/4fa052ff-b1a2-4596-b420-3efbf912d3e5

## Internal demo

The demonstration shows a fragment of the sensor consisting of two parallel circuits with reed switches. The second circuit is needed to validate the readings. Readings from two circuits are displayed separately on the screen.
In the future, with the help of a filter and two readings, a smooth and reliable output of values will be realized.

# Weekly commitments

## Individual contribution of each participant

| Member					| Contribution					|
|---------------------------|-------------------------------|
| Dmitriy Vizitei			| [Build and testing of the float sensor](https://github.com/IU-Capstone-Project-2025/ProjectFly/blob/main/docs/reports/week3_demo.mp4)	|
| Senea Belykh				| Design of a printing board model: [.dip file of model](https://drive.google.com/file/d/1kAshYWK63EGtSO8ugL8LIpLLuq3zHijo/view?usp=drive_link), [Screenshot 1](https://drive.google.com/file/d/1b59gKXb-_gpLtJmoub-71Or28Qxjg9nt/view?usp=drive_link), [Screenshot 2](https://drive.google.com/file/d/1cMnjLT8AdKEfaEngB_d79zmb4BKwSN_p/view?usp=drive_link), [Screenshot 3](https://drive.google.com/file/d/19lfl12A_gvJT9DxeMLiNG9lB-w_u033m/view?usp=drive_link), [Screenshot 4](https://drive.google.com/file/d/15qXjzGLoRry6YyHDq0xQBWc0gWb6dqjc/view?usp=sharing)	|
| Dmitry Ryabov				| [Data processing and multitasking implementation](https://github.com/IU-Capstone-Project-2025/ProjectFly/commit/427cdca47f92fd35336689fed5b88d71be1657ca)	|
| Anas Hamrouni				| CAD design for MVP float sensor and and its installation: [Screenshot 1](https://drive.google.com/file/d/1yXhJFeNlo0ktXdDd30qICJDR3P5ZgBRc/view?usp=drive_link), [Screenshot 2](https://drive.google.com/file/d/1Cs98SicpZ4TfVprqYWIeNAE5lt_2MkrX/view?usp=drive_link), [Screenshot 3](https://drive.google.com/file/d/1mO2JWQUNWl51_XnYHGpag1vgucJC9s4t/view?usp=drive_link), [Screenshot 4](https://drive.google.com/file/d/1EVLHVlt_bsYl2PFsscmXYxY9q6P1DE29/view?usp=sharing), [Screenshot 5 (The brown color is one piece to be assembled as a tool) ](https://drive.google.com/file/d/1q62NgHWZDSAhbYw4ZfM8Jk9xgEBASD9l/view?usp=drive_link), [archive with models of parts](https://drive.google.com/file/d/1Xy0XBJnHxUWf5-DdJJCfNiPBmoh62PsU/view?usp=drive_link)	|
| Andrew Pavlov				| [3nd week report.](https://github.com/IU-Capstone-Project-2025/ProjectFly/blob/main/docs/reports/week3.md)	|

## Plan for Next Week

- Lay out the board
- Prepare MVP 
- Test the MVP 
- Analyze the numerical data after the test and consider alternative approaches based on it

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [X] In working condition.
- [X] Run via docker-compose (or another alternative described in the `README.md`).
