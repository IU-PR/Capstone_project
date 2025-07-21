# **Week #2**

## Detailed Requirements Elaboration

### User Story 1: Active Safety Engineer

#### High-level:
As an active safety engineer, I want to integrate an AI stabilization algorithm to improve stability during skidding.

#### Expanded MVP Story:
As an active safety engineer, I want to test how an AI algorithm on a small-scale RC vehicle responds to simulated skids, so I can evaluate its stabilization logic before considering full-size deployment.

#### Acceptance Criteria:
- The system must detect a simulated drift event based on sensor data.
- The algorithm should predict vehicle trajectory for at least 1 second ahead.
- It must trigger at least one corrective action (e.g., throttle/brake/steering) within 0.5s of drift onset.
- Log data of predicted vs actual path should be available after test.

---

### User Story 2: Driving Instructor

#### High-level:
As a driving instructor, I want to use an AI skid simulator to teach students.

#### Expanded MVP Story:
As a driving instructor, I want to use a small RC car equipped with drift control to visually demonstrate skidding behavior and automatic correction to students in real-time.

##### Acceptance Criteria:
- RC car must drift on slippery surface and perform correction.
- Students must be able to see real-time status (e.g., “drift detected”, “correcting”).
- A simple UI must display car behavior: angle, speed, correction.

---

### User Story 3: ADAS Researcher

#### High-level:
As an autonomous driving researcher, I want to test a predictive stabilization system.

#### Expanded MVP Story:
As a researcher, I want to run experiments on an RC platform that includes prediction of future vehicle state and corresponding corrective response, to analyze control performance.

#### Acceptance Criteria:
- Prediction module must output trajectory over next 1–2 seconds.
- At least two different drift scenarios must be testable.
- Logs must show prediction errors and actions taken.

---

### User Story 4: Drift Instructor

#### High-level:
As a drift instructor, I want real-time trajectory correction suggestions.

#### Expanded MVP Story:
As a drift instructor, I want to get visualized data about RC car trajectory and corrections applied, so I can explain to students what correction works and why.

#### Acceptance Criteria:
- Real-time visual of car trajectory on screen (2D map or graph).
- Correction direction shown as vector or label (e.g., “steer left”).
- Historical trail (last 5 seconds) visible.

---

### User Story 5: AWD Vehicle Owner

#### High-level:
As an AWD owner, I want the car to auto-correct in skids.

#### Expanded MVP Story:
As an AWD owner, I want to see how the RC model handles a skid automatically, so I can evaluate if such a system would improve safety in real driving.

#### Acceptance Criteria:
- RC model must respond to slip and recover path within 2 seconds.
- Skid detection must trigger correction without human input.
- System should visibly reduce overshoot or spinout in 3 test cases.

---

### Prioritized backlog

[Prioritized backlog (Kanban board)](https://app.weeek.net/ws/815806/shared/board/1WypMVQYOJySBGTs6enMdwLVWQJTZqyw)

---

## Project specific progress

### Control

In the control domain, the team selected the PILCO algorithm from reinforcement learning due to its high sample efficiency, based on insights from prior research. The RC car platform was prepared and tested for state data collection, and communication between the Raspberry Pi and Arduino was successfully established via SSH.

### Sensors

In the sensor domain, a Kalman filter was implemented to fuse gyroscope and accelerometer data, improving angle accuracy. A low-pass filter reduced noise, resulting in smooth and stable readings, which were validated via the Arduino serial plotter.

### ML

In the ML/RL domain, the project structure was finalized with a detailed Markdown plan outlining goals, milestones, and data formats. A first code prototype was developed, demonstrating random policy generation and GP training on synthetic data. Additionally, a functional PILCO baseline script was created, featuring a basic environment, rollout collection, GP models, RBF policy, and CLI for training and evaluation.

---

# Weekly commitments

## Individual contribution of each participant

**Valeria:**
- Writing the code for Arduino and Rasberry Pi for PWM control: \\
[Code](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Arduino%20Uno/accept_pwm.cpp) and [Library TimeLib](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/tree/main/Arduino%20Uno/TimerLib) (written for synchronization) for Arduino \\
[Rasberry Pi code](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/RaspberryPi/send_pwm.py) that sends PWM signal to Arduino UNO \\

**Nikolay:**
- Finishing writing the code for reading data from the IMU sensor on the Arduino via wired connections [Code](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/RaspberryPi/readSerial.py)
- Analyzing ready-made solutions of RL approaches for automatic drift in simulation [Reference](https://i.cs.hku.hk/fyp/2017/fyp17014/docs/Final_report.pdf)

**Lidia:**
- Made a filtering of gyroscope angles using a Kalman filter, which takes into account the gyroscope prediction and compares it with the calculated angle value using an accelerometer: \\
Tested the data output. Compared how the rotation converges with the data on the serial flow graph in Arduino IDE \\
Used a low pass filter to smooth out the acceleration noise from the accelerometer \\
Made the values ​​smooth and stable (with low error) \\
[Code](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/imu/imu.ino)

**Ilyas:**
- Writing first code prototype \\
[first_version.ipynb](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/ML/first_version.ipynb) contains working snippets: \\
 Importing TF 2 / GPflow libraries \\
 Random policy generation \\
 Quick test of GP-learning on synthetic data \\
- Create [PILCO framework](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/ML/ml_plan.md) that include: \\
CarEnv framework \\
collect_rollout function \\
Trained GP models for Δs \\
RBF policy + minimum optimisation loop \\
CLI (train / eval) and serialisation of weights (pilco_weights.npz) \\

**Andrey:**
- Expand high-level user stories, define Acceptance Criteria user stories, and create an initial backlog with prioritized tasks
- Сompiling a weekly report

---

## Plan for Next Week

- ML + Control \\
Begin training the control model. The training will be based on real-world driving data instead of simulations to improve real-environment adaptation.

- Microcontrollers \\
Test and establish a stable, error-free connection between the Arduino and Raspberry Pi to ensure reliable and continuous communication.

- Wiring  \\
Create a compact and safe wiring setup that connects all components neatly and securely within the RC car chassis.

- Electric Safety in RC Car \\
Design and implement a safe power distribution system to prevent Arduino damage. Currently, Arduino is connected to motors and servos, so powering it on without external supply may cause hardware failure. A protective solution must be developed.

- Data Visualization \\
Implement a method for visualizing sensor and control data to demonstrate logical system behavior and prove that the system functions as intended—not as a simulation or placeholder.

---

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [ ] In working condition.
- [ ] Run via docker-compose (or another alternative described in the `README.md`).