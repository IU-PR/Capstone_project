# **Week #1**

## Project description

### Project name: *Total control*

**Code repository**: https://https://github.com/IU-Capstone-Project-2025/total_control

The Robotics Laboratory of Innopolis University and the Control Theory course faced the need to train students on real physical installations to hone their skills in developing control algorithms. Thanks to this, students will be able to take into account all the features of the real world, as well as quickly test their solutions without having troubles with hardware.

The Cart Pole system, also known as an inverted pendulum, is a control problem, where a pole is mounted on a wheeled cart that moves along a one-dimensional track. The goal is to control the movement of a cart such that the pole stays balanced around its vertical axis. The system is nonlinear and unstable, making it an excellent base for control theory, reinforcement learning and robotics.

The objective is to design a software and hardware product for the robotics laboratory of Innopolis University in order to study and improve skills in the field of Control Theory, Reinforcement Learning (RL), Shapers and other areas of Modern Robotics. To achieve this goal, it is necessary to solve the following tasks:
- Check the operability of the existing stand as a whole and its elements separately
- Develop and prepare the power supply and wiring of the system and connect it to the controller
- Develop low-level algorithms for managing components, with a particular focus on the physical limitations of the components to prevent damage to the structure, environment, and students.
- Develop a library in the Peyton language that provides interfaces and classes with a high level of abstraction for easy connection and management of the laboratory stand via the serial port

### **Team Members**

| Team Member                             | Telegram Alias   | Email Address                     | Track                  | Responsibilities                                  |
|-----------------------------------------|------------------|-----------------------------------|------------------------|---------------------------------------------------|
| (Lead) Evgenii Shlomov                  | @mook003         | e.shlomov@innopolis.iniversity    | High level programmist | Writing python library and docker                 |
| Artyom Tuzov                            | @artyomzifir     | a.tuzov@innopolis.iniversity      | Electrical engineer    | Inspecting and configuring hardware               |
| Anastasia Malakhova                     | @stasia_hay      | an.malakhova@innopolis.university | Low level programmist  | Building the interface betwenn higl and low level |
| Marat Shariev                           | @ficussss        | m.shariev@innopolis.university    | Low level programmist  | Testing hardware connection                       |
| Petr Belayev                            | @pbel1           | p.belayev@innopolis.university    | Technical Writer       | Writing documentation and reports                 |



## Brainstorming

### Ideas during brainstorming

1. Educational Control System Kit
   - A modular hardware kit with software for teaching control systems, linear algebra, and system dynamics in universities.
   
2. RL & AI Research Platform
   - A benchmark system for reinforcement learning (RL) algorithms, allowing sim-to-real transfer and robustness testing.
   
3. Balance Control Testbed for Personal Transport Devices
   - A prototyping tool for companies developing self-balancing systems like Segways, monowheels, or hoverboards.
   
4. Digital Twin + Remote Lab for STEM Learning
   - An internet-connected cart pole with a digital twin, enabling students to run experiments remotely via a web interface.
   
5. Low-Cost Rehabilitation and Balance Training Robot
   - Adapt the inverted pendulum concept to assistive devices for posture training, with applications in physiotherapy.

### Brief market research / problem validation

While a mechanism is readily available on the market, it remains difficult to find a programmer capable of developing the necessary software for the laboratory setup. Currently, there are no publicly accessible programs that meet our specific requirements. This perspective is shared by professionals in the field and staff at the Innopolis Institute of Robotics. Therefore, our solution not only addresses this gap but also holds significant importance for student practice, providing them with valuable hands-on experience in a practical setting.

## Basic requirements

### Target users and their primary needs

The Cart Pole system serves as a versatile platform for control theory, robotics, and machine learning. It addresses the educational, research, and prototyping needs of a wide range of users. Below is a categorized list of key target users along with their primary motivations and use cases.

1. **University Students (Engineering/Robotics)**

Primary Needs:
- Understand real-world implementation of control algorithms.
- Perform hands-on experiments to complement theoretical coursework.
- Analyze system dynamics through physical modeling and simulation.

Use Case:
Students use the system during labs and final year projects to apply PID, LQR, and state estimation techniques.

2. **Professors and Lab Instructors**

Primary Needs:
- Provide safe, reliable, and repeatable lab experiments.
- Teach core concepts in control systems, feedback, and signal processing.
- Easily reset and monitor the system during student use.

Use Case:
Faculty integrate the cart-pole into structured lab modules or capstone projects for teaching applied control theory.

3. **AI/ML Researchers**

Primary Needs:
- Test reinforcement learning (RL) algorithms on real-world dynamic systems.
- Collect noisy, physical-world data to validate simulation results.
- Bridge the sim-to-real gap for policy transfer.

Use Case:
Researchers deploy and benchmark RL agents (e.g., DQN, PPO) to test robustness and sample efficiency.

### User stories

1.**University Students (Engineering/Robotics)**

- As a student, I want to upload and test a PID or LQR controller so that I can see how different control strategies affect system stability.
- As a student, I want to collect and analyze real-time data so I can validate theoretical models with experimental results.
- As a student, I want to tune controller parameters (e.g., gain values) from a user interface so I can observe the effects without rewriting code.
- As a student, I want to simulate the cart-pole behavior before running it on hardware so I can avoid damaging the system.

2.**Professors and Lab Instructors**

- As an instructor, I want to define pre-configured experiments so students can quickly start working without needing to set up the system from scratch.
- As an instructor, I want to remotely monitor student experiments so I can supervise labs in a hybrid or remote environment.
- As an instructor, I want to reset the system and apply limits to control parameters so I can ensure safety during classroom use.

3.**AI/ML Researchers**

- As a researcher, I want to train and test RL agents on the cart-pole hardware so I can evaluate real-world performance.
- As a researcher, I want to inject noise and disturbances to study the robustness of control algorithms.
- As a researcher, I want access to raw sensor data and control logs so I can analyze the learning process and failure cases.
- As a researcher, I want to compare sim-to-real performance so I can validate simulation-based methods in practice.

### Initial scope

**Objectives:**

- Develop a physical cart-pole system capable of balancing an inverted pole using real-time control.
- Implement fundamental control algorithms (e.g., PID and LQR).
- Provide real-time sensor data visualization and basic user interaction.
- Create a simulator for offline algorithm development and testing.
- Ensure system is modular, safe, and replicable for use in labs and learning environments.

**Hardware Features:**

- Cart and Rail System: Linear rail with motorized cart for 1D motion.
- Pole: Rigid pole mounted on a hinge, free to rotate in 1D plane.
- Sensors:
  - Cart position sensor.
  - Pole angle sensor.
  - End sensor.
- Motor for cart.
- Microcontroller: Raspberry Pi, Arduino, or STM32-based controller.
- Power Supply: Safe and sufficient for motor and control unit.
- Safety Mechanisms:
  - Physical end stops or limit switches.
  - Emergency shutdown button.

**Software Features:**

- Control Loop:
  - Real-time control loop.
  - Initial implementation of PID and LQR controllers.
- Data Logging:
  - Save sensor and control data.
  - Timestamped logs for offline analysis.
- Offline Simulator
- Easy plug-n-play interface

**Documentation:**

- Full assembly and wiring guide.
- Annotated code with comments and modular structure.
- Instructions for uploading code to the controller.
- Lab manual with 3–5 predefined experiments
- Troubleshooting checklist and safety guidelines.

**Deliverables:**

- Functional cart-pole hardware prototype
- Controller software with real-time performance
- Educational material and documentation


## Tech-stack

Microcontroller - STM32 / Raspberry Pi / Arduino

Encoder - SEAVDAN H9740 

Angle sensor - Infineon TLE5012B

Motor - 12V or 24V gear motor with encoder (TBA)

Structure - Aluminum rail, custom cart, pole

Languages - Python, C++

Our cool thing:

![photo_2025-06-11_22-26-30](https://github.com/user-attachments/assets/337321d3-c77e-471d-9b8f-0cb01ae2c196)

# Weekly commitments

## Individual contribution of each participant

Anastasia - [Check linear encoder](https://github.com/IU-Capstone-Project-2025/total_control/commit/1b2943cadd8492cfd284862eac39d235747a7244)

Evgenii - [Write docker and docker compose, creating structure of repository](https://github.com/IU-Capstone-Project-2025/total_control/commit/5c677fc5d25899b8dbd0dc5a0f8e27a5ce8657f2)

Artyom - [Find configuration of sensors and test hardware](https://github.com/IU-Capstone-Project-2025/total_control/commit/0db119c290c39f15f94458de5be372f6a0a9c195)

Petr - [Write report and documentation](https://github.com/IU-Capstone-Project-2025/total_control/blob/Reports/Report_week_1.md)

Marat - [Angle sensor development](https://github.com/IU-Capstone-Project-2025/total_control/tree/dev-angle-sensor-test)

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [X] In working condition.
- [X] Run via docker-compose (or another alternative described in the `README.md`).
