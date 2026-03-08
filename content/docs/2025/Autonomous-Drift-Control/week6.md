---
title: "Week #6"
---

# **Week #6**

## Links

- **Deployment**: [Link](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Documentation/Code_Launch_Documentation.pdf)
- **API Docs**: [Link](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/tree/main/Documentation)
- **Design**: [Link](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Robot/IMG20250715211223.jpg)
- **Demo**: [Link](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Robot/IMG_0210.MOV)

## Final deliverables

### Project overview

Autonomous Drift Control is a prototype system for stabilizing vehicles during skids, tested on an RC car. It predicts vehicle dynamics and applies corrective control to maintain or recover from drifts, addressing stability issues in low-grip conditions.

#### Key implemented features:

**Integrated hardware:** Rewired RC car with Arduino, Raspberry Pi, and IMU for real-time state tracking.

**Stable data pipeline:** Low-latency communication between components via SSH.

**Sensor fusion:** Kalman-filtered gyroscope and accelerometer data for accurate angle estimation.

**Dataset & model:** 60 driving sequences collected; model predicts vehicle state and controls steering and throttle.

**MPC control:** Random-shooting MPC reduces yaw rate ~3× faster than manual driving in tests.

**ML:** 60 circular RC-auto drifts (position, IMU, steering, throttle). Based on them, a compact dynamics model has been trained:  
State + Command → forecast of sliding/orientation changes.  
The model feeds the MPC, stabilizing the trajectory during skidding.

The current MVP forms a full data → model → control pipeline, enabling semi-autonomous drift stabilization.

### Tech stack

**Hardware Layer:** Arduino, Raspberry Pi 4B, Sensors (IMU, steering angle sensor)

**Control Theory:** Control algorithms, Kalman filter for sensor data processing

**Physics:** Vehicle kinematics, electronic circuits, motor control

**ML:** Reinforcement Learning (RL)

**Sensor Processing:** Kalman filter, Low-pass filters, High-pass filters

### Setup instructions

1. Clone the repository
2. Prepare the hardware platform:  
Use an RC car RC8.2 with Arduino and Raspberry Pi 4B installed  
Mount the IMU and steering angle sensor as described in the hardware setup section
3. Upload the Arduino firmware:  
Flash the Arduino with the provided control firmware from the repository  
4. Install the ML model on Raspberry Pi:  
Deploy the trained ML model (provided in the repo) to the Raspberry Pi
5. Configure Arduino ↔ Raspberry Pi connection:  
Follow the instructions in the repository to set up the SSH-based connection
6. Run the system:  
Power up the RC car and launch the main control script on the Raspberry Pi  
The car will start following the control algorithm automatically



## Presentation draft

[Link to the presentation draft in Figma](https://www.figma.com/slides/A1NC4U1LhfgDjTTa2d7Qxs/Untitled?node-id=2-27&t=xejCLA1syrstmVhg-1)

# Weekly commitments

## Individual contribution of each participant

**Valeria:**
- Testing a new filter - magwick on quaternions for angle filtering
- Сompiling the [documentation for the electrical circuit](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Documentation/Wires_connection.pdf)
- Replacing the servo motor 
- Mading the next step (calculated mathematically)  
Algorithm development → following the path → drift along the perfect figure eight

**Nikolay:**
- Writing the [documentation for launching an autonomous drift](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Documentation/Code_Launch_Documentation.pdf)
- Designing drawings of component models for 3D printing

**Lidia:**
- Soldering wires for robot wiring
- Writing [documentation for IMU sensor](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Documentation/doc_imu.pdf)

**Ilyas:**
- Doing 20 new tests for each tested unit in the code, put everything in the tests folder
- Improving pylint performance
- Refactoring the code by 10/10 in syntax 
- Writing the [documentation for the ML part](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/ML/old_staff/mvp.ipynb) of the project

**Andrey:**
- Drafting [presentation](https://www.figma.com/slides/A1NC4U1LhfgDjTTa2d7Qxs/Untitled?node-id=2-27&t=xejCLA1syrstmVhg-1) 
- Сompiling a weekly report

## Plan for Next Week

- Develop and test a new figure-eight drift algorithm with three track sizes to evaluate how size affects drift accuracy.

- Build a protective car frame to cover components and improve the RC car’s appearance.

- Compare algorithm performance with previous versions and summarize results.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [✅] In working condition.
- [✅] Run via docker-compose (or another alternative described in the `README.md`).
