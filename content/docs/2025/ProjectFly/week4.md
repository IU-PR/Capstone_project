---
title: "Week #4"
---

# **Week #4**

## Team

### **Team Members**

| Team Member							| Telegram Alias	| Email Address   					| Track												| Responsibilities   |
|---------------------------------------|-------------------|-----------------------------------|---------------------------------------------------|--------------------|
| Dmitriy Vizitei (Lead)				| @otkisaev			| d.vizitei@innopolis.university 	| Low level (embedded) + Electric circuit engineer + testing  | Project coordination, task delegation, programming and testing prototypes |
| Senea Belykh							| @SenyaZenya		| s.belykh@innopolis.university		| Low level (embedded) + Electric circuit engineer	| Programming and testing prototypes |
| Dmitry Ryabov							| @theDioxider		| d.ryabov@innopolis.university 	| Low level (embedded) 								| Programming |
| Anas Hamrouni							| @reachnasta		| a.hamrouni@innopolis.university   | Design engineer 									| Designing 3D models |
| Andrew Pavlov							| @chaleshka_0		| and.pavlov@innopolis.university	| Tech writer 										| Document the work and write reports |

## CI/CD

During CI/CD, we encountered the problem that the github workflow does not have a compilation environment for our product, so we did manual tests on cubeIDE.

### Links to CI/CD configuration files

https://github.com/IU-Capstone-Project-2025/ProjectFly/blob/main/.github/workflows/c-linter.yaml

## Vibe Check

The team leader is on sick leave, and the rest of the team is healthy. <br />
Due to logistical problems, the laser needed for the work was delivered to us very late in time for the deadline, which caused a lot of stress during its setup and operation in the last hours before the deadline.

# Weekly commitments

## Individual contribution of each participant

| Member					| Contribution					|
|---------------------------|-------------------------------|
| Dmitriy Vizitei			| Testing: [photo 1](https://drive.google.com/file/d/11sWm9Eje6SpBsuDrlUKM9gq9MjP24NQu/view?usp=drive_link), [photo 2](https://drive.google.com/file/d/1dNQqF_wJioakaVgUDXrWjnx1O2QSEEL4/view?usp=drive_link); laying out the board using laser: [video 1](https://drive.google.com/file/d/1wMU_KEni9PQ2VG3ThoixvVIlINiCmWOo/view?usp=drive_link), [video 2](https://drive.google.com/file/d/13v9Dhd8rFhSDY7FK-wtBonQAqTI9EYGV/view?usp=drive_link), [photo](https://drive.google.com/file/d/1k83NPXRmFJaZUlnCxQowFRZGzRzlfGT7/view?usp=drive_link) |
| Senea Belykh				| The renewed version of the board: [screenshot 1](https://drive.google.com/file/d/1f35pPph8MtAH_zsE1N_wpZU_w1E1n0Zs/view?usp=drive_link), [screenshot 2](https://drive.google.com/file/d/1TuTwNzNpZY1UzZ-rh-VTb_SV1s4rwtpJ/view?usp=drive_link), [files](https://github.com/IU-Capstone-Project-2025/ProjectFly/commit/5295f774d12a0047f9f7b59432f5d1f2cc4458eb); [testing](https://drive.google.com/file/d/1BBwjxaTWTiUZHPBcxWp0rQVh082nHvK7/view?usp=drive_link) |
| Dmitry Ryabov				| [CI/CD](https://github.com/IU-Capstone-Project-2025/ProjectFly/blob/main/.github/workflows/c-linter.yaml), [filter (embedded development)](https://github.com/IU-Capstone-Project-2025/ProjectFly/commit/508749f63c032bdbdd70469d089fd19ae9c99970#diff-dc4e1a81013be86ffd6e574b70bc84c12b231c098fe0eead90074bb35eec9755) |
| Anas Hamrouni				| The design of lever, the renewed design of float, design of the rod: [photo 1](https://drive.google.com/file/d/11sWm9Eje6SpBsuDrlUKM9gq9MjP24NQu/view?usp=drive_link), [photo 2](https://drive.google.com/file/d/1dNQqF_wJioakaVgUDXrWjnx1O2QSEEL4/view?usp=drive_link), [files](https://github.com/IU-Capstone-Project-2025/ProjectFly/commit/2ea619bedeee6b55bfc94a4936219a47339772bb) |
| Andrew Pavlov				| [4nd week report.](https://github.com/IU-Capstone-Project-2025/ProjectFly/blob/main/docs/reports/week4.md) |


## Plan for Next Week

- Layout the final pcb using laser
- Assemble the renewed configuration of a product
- Connect the pcb to the layout of reed switches

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [X] In working condition.
- [X] Run via docker-compose (or another alternative described in the `README.md`).