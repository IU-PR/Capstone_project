---
title: "Week #5"
---

# **Week #5**

## Team

### **Team Members**

| Team Member							| Telegram Alias	| Email Address   					| Track												| Responsibilities   |
|---------------------------------------|-------------------|-----------------------------------|---------------------------------------------------|--------------------|
| Dmitriy Vizitei (Lead)				| @otkisaev			| d.vizitei@innopolis.university 	| Low level (embedded) + Electric circuit engineer + testing  | Project coordination, task delegation, programming and testing prototypes |
| Senea Belykh							| @SenyaZenya		| s.belykh@innopolis.university		| Low level (embedded) + Electric circuit engineer	| Programming and testing prototypes |
| Dmitry Ryabov							| @theDioxider		| d.ryabov@innopolis.university 	| Low level (embedded) 								| Programming |
| Anas Hamrouni							| @reachnasta		| a.hamrouni@innopolis.university   | Design engineer 									| Designing 3D models |
| Andrew Pavlov							| @chaleshka_0		| and.pavlov@innopolis.university	| Tech writer 										| Document the work and write reports |

## Feedback

Through Alexander Maloletov (Director of the Robotics Development Center in Innopolis), we agreed that upon completion of the order, the project participants will receive a lump sum payment.

## Iteration & Refinement

### Performance & Stability

When the magnet slides post reed switches, there is a chance to get a value equal to 0. This is due to the current solution and design. There is a metric associated with the gaps between switches. <br />
An iteration solution would be to reduce the size of reed switches to such an extent that a negligibly small gap between the switches is reached, which would guarantee a constant and unambiguously set position of the float.

# Weekly commitments

## Individual contribution of each participant

| Member					| Contribution					|
|---------------------------|-------------------------------|
| Dmitriy Vizitei			| Assembly of a product, communication, testing: [photo](https://drive.google.com/file/d/11ErTu5s1axHB51JZw7vPIAQcNcZdXoS1/view?usp=drive_link), [video 1](https://drive.google.com/file/d/17mmQQElqiJNetmurcGpcXXFE-Ebcmi8j/view?usp=drive_link), [video 2](https://drive.google.com/file/d/1X96Me4vulu15EC3oLPyxjKNYTdaBQLdP/view?usp=drive_link), [video 3](https://drive.google.com/file/d/1RMR0l2JPTSWMmnUTkXt8X2qB1T35l_1s/view?usp=drive_link) |
| Senea Belykh				| [Littel change design of board and design of a microcontroller board](https://github.com/IU-Capstone-Project-2025/ProjectFly/commit/9250cefd38d36df9182ef802b712d2c060db03d2) | 
| Dmitry Ryabov				| Determining reed switch based on voltage: [photo](https://drive.google.com/file/d/1ix-wG_TddyOyOhTqer4dDWPdwUh-kQOK/view?usp=drive_link), [commit 1](https://github.com/IU-Capstone-Project-2025/ProjectFly/commit/e2bc04ccc3fc08e8e42fd3654ed2149dc4a043e4), [commit 2](https://github.com/IU-Capstone-Project-2025/ProjectFly/commit/748511da521208b3848574d846316bceeffb3a55) |
| Anas Hamrouni				| [PCB design + review of dimensions](https://github.com/IU-Capstone-Project-2025/ProjectFly/commit/1565ed656107ac8c0a5cf2ffb28c307ee85f2cba) |
| Andrew Pavlov				| [5nd week report.](https://github.com/IU-Capstone-Project-2025/ProjectFly/blob/main/docs/reports/week5.md) |

## Plan for Next Week

- Build the microcontroller board
- Complete the prototype assembly
- Сontact the customer to confirm our product solution

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).