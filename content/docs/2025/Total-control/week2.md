# Week #2

## Detailed Requirements Elaboration

Initial use cases:
- Students use the system during labs and final year projects to apply PID, LQR, and state estimation techniques.
- Faculty integrate the cart-pole into structured lab modules or capstone projects for teaching applied control theory.
- Researchers deploy and benchmark RL agents (e.g., DQN, PPO) to test robustness and sample efficiency.

Expanded User stories:
- As a student I want understand the state of the system, is it working, got an error or standing still. Criteria - error handler and state displaying.
- As a student I want clear and concise API documentation, so that I can understand how to work with library. Criteria - documentation and comments are available.
- As a TA I want students easily connect to the system without my additional actions. Criteria - plug-n-play connection
- As a researcher I want fast and easy opertional process, so that discrete system might be considered as a continuous. Criteria - fast frequency response.

Acceptance Criteria:

-Simulation initializes with default parameters: M, m, L, g

-The system integrates equations of motion over time

-User can select time step dt

-The system returns states over time

-There is a form of interface to input

-Parameters are validated

-System uses updated parameters in the simulation or control

-UI renders cart and pendulum near real-time

-Plot shows I/O and angle (x,theta,u) of the system in real time 

### Prioritized backlog

[Link to the backlog](https://github.com/orgs/IU-Capstone-Project-2025/projects/17)

## Schematic diagram of the project

![maf](https://github.com/user-attachments/assets/fa981b79-580e-4ab4-a537-dd3b0887ffec)

This diagram shows a schematic diagram of the project. 

The left part describes the basic structure of the `inno_control` library, which will provide management of all laboratory installations and provide tools for working with them. 

The library will supply the `CarPole` class, which will have methods for receiving data and sending requests. 

A Universal Serial Bus (`USB`) will be used to provide communication between the computer with the library and the controller, which will be used to transmit data packets (maps) 

The `ESP32` was selected as the controller to ensure high performance and prototyping speed. 

The controller itself interacts with the peripherals (`button`, `encoders`, and `UART-CAN adapter`) via the built-in `GPIO outputs`. The motor is connected via the Controller Area Network (`CAN`) line, has its own ID and communicates via special packages.

## Project specific progress

### Backend

- The structure of the high-level library was outlined.
- The structure of the process of interaction between the controller and the user's computer via USB were discussed and outlined.
- The programs for testing the encoder and the motor were designed in a unified manner.
  
### Frontend & Design

- The initial setup of the Sphinx project was completed to create project documentation in the form of a tree-like site.

### Hardware

- It was decided empirically to use the esp32 controller to control the signals.
- All sensors and the motor were retested and now work properly.

# Weekly commitments

## Individual contribution of each participant

Anastasia - [Setup sphinx project for documntation](https://github.com/IU-Capstone-Project-2025/total_control/commit/a9f3840d564e7c5d53487f874f5dbcd4b7d9e0e6)

Evgenii - [Python library structure](https://github.com/IU-Capstone-Project-2025/total_control/commit/81fd9744186f035bbc3ae94edd9649d1cfd495db)

Artyom - [Motor tests for ESP32](https://github.com/IU-Capstone-Project-2025/total_control/commit/f9f691522e77aa500441cd81726b9a6e3b78c9a4)

Petr - [Write report](https://github.com/IU-Capstone-Project-2025/total_control/commit/0eb0a428ac47141bd399c90e6cde000a7ec91210)

Marat - [Motor command sender for ESP32](https://github.com/IU-Capstone-Project-2025/total_control/commit/c5304b5e67c4615f31bcf63bde02ca3f16cb2dd9)

## Plan for Next Week

- Combine sensor and motor tests into one file.
- Synchronize their operation using interrupts.
- Find the most suitable controller operating frequency.
- Start documenting the API and firmware

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [X] In working condition.
- [X] Run via docker-compose (or another alternative described in the `README.md`).
