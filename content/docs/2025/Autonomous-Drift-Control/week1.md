# Week #1

## Project description

**Project name:** Autonomous drift control

**Code repository:** https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control

**Description**



We’re developing an autonomous drift stabilization system for all-wheel-drive vehicles, with testing on an RC car. Using minimal sensor data, the control system will calculate the vehicle’s current and predicted states, then apply corrective actions to maintain stability during drifts. This small-scale prototype will demonstrate how advanced control algorithms can handle extreme driving conditions.


---

## Team Members

| Team Member               | Telegram Alias   | Email Address                     | Track                | Responsibilities |
|---------------------------|------------------|-----------------------------------|----------------------|------------------|
| Valeria Neganova (Lead)   | @leryamerlennnnn     | v.neganova@innopolis.university   | Control Theory       | Implementation of control actions on the vehicle, mathematical model design, sensor integration and data processing |
| Nikolay Rostov            | @rostovw1n        | n.rostov@innopolis.university     | Control Engineering  | RaspberryPi-Arduino communication, sensor data processing, vehicle kinematics modeling, control algorithm development |
| Lidia Davydova            | @LidaDavydova     | l.davydova@innopolis.university   | Computer Vision      | Lane detection, sensor validation and testing, hardware assistance |
| Ilyas Galiev              | @ilyasGaliev      | il.galiev@innopolis.university    | Machine Learning     | Dataset creation, data annotation, model training and validation |
| Andrey Krasnov             | @krassand     | an.krasnov@innopolis.university    | Technical Writer    | Reserch analysist, data annotation, tech writter|

---

## Brainstorming

### Ideas during brainstorming


During brainstorming, we evaluated three potential methods for our vehicle stabilization system:

1. **LIDAR + SLAM + Obstacle-Aware NMPC**  
   - *Concept*: Combines LIDAR mapping with Nonlinear MPC that accounts for surrounding vehicles/obstacles in trajectory optimization.  
   - *Pros*: Enables collision-avoiding stabilization, ideal for real-world scenarios.  
   - *Cons*: Requires expensive sensors and multi-layer sensor fusion (2x complexity).

2. **NMPC (No Obstacle Consideration)**  
   - *Concept*: Standard NMPC focusing only on vehicle dynamics during drifts.  
   - *Pros*: Theoretically optimal for handling drift dynamics.  
   - *Cons*: Needs high-fidelity vehicle modeling and is computationally intensive.  

3. **Reinforcement Learning (RL) Controller**  
   - *Concept*: Train an RL agent to learn stabilization policies through simulated drift scenarios.  
   - *Pros*: Adaptable to nonlinearities, requires less explicit modeling.  
   - *Cons*: Needs careful reward function design.  

*Final Decision*: Chose Option 3 due to time constraints - basic NMPC would require 3+ months for proper implementation, while obstacle-aware NMPC (Option 1) would need 6+ months with current resources.


### Brief market research / problem validation
**Intelligent Vehicle Stabilization System**
#### Problem validation

**Problem:** Existing active safety systems (ABS, ESP, VDC, DSC) are limited to severe scenarios and are not able to effectively cope with a skid that has already occurred.

**Solution:** Develop a system that can predict and control a skid using AI and  control theory, which provides a higher level of safety.

**Uniqueness:**
The lack of serial solutions capable of stabilizing a car with an already occurring skid using AI. Scientific developments (Toyota Research Institute, Stanford Dynamic Design Lab) demonstrate experimental platforms for drifting, but have no industrial implementation. Domestic solution for own automobile production

#### Market research
TAM (Total Addressable Market): $650+ billion — global market for active safety systems, motorsport simulators, drifting and autonomous driving technologies.

SAM (Serviceable Available Market): $1.2–1.5 billion — companies and organizations interested in managing transport in extreme conditions.

SOM (Serviceable Obtainable Market): $3–5 million — first B2B partners, driving schools, universities, show drifting and teams interested in the experimental platform and licensing.

---

## Basic requirements

### Target users and their primary needs
1. **Automakers and active safety system suppliers** \\
Need advanced AI solutions to improve the safety and competitiveness of vehicles, especially those with all-wheel drive.

2. **Driving schools and driver training centers** \\
Look for tools to teach driving in difficult road conditions, including skidding.

3. **Autonomous driving and ADAS engineers and researchers** \\
Look for platforms to test and implement intelligent stabilization systems.

4. **Motorsport teams and drift schools** \\
Need systems that help study and stabilize skidding without losing control of the vehicle.

5. **Advanced car enthusiasts and owners of all-wheel drive vehicles** \\
Look for ways to improve safety and control in winter, mountain and extreme conditions.

### User stories
1. As an active safety engineer, \\
I want to integrate an AI stabilization algorithm \\
to improve the stability of the car during skidding.

2. As a driving instructor, \\
I want to use an AI skid simulator \\
to teach students how to drive in critical situations.

3. As an autonomous driving researcher, \\
I want to test a predictive stabilization system \\
to analyze its effectiveness under conditions of traction loss.

4. As a drift instructor, \\
I want to see real-time trajectory correction recommendations \\
to explain to students how to exit a controlled skid.

5. As an owner of an all-wheel drive vehicle, \\
I want the car to automatically correct its behavior during skidding \\
to feel safer in winter conditions.

### Initial scope

1. **Sensor Data Acquisition**  
   - Collect real-time vehicle dynamics data from all critical sensors (IMU, wheel speed, steering angle, etc.)

2. **Data Processing Pipeline**  
   - Filter and fuse sensor inputs for state estimation  
   - Calculate key parameters: slip angles, yaw rate, friction coefficients  

3. **Trajectory Optimization**  
   - Real trajectory optimization
   - Generate optimal stabilization trajectories during skid conditions  

4. **Vehicle Control Implementation**  
   - RL control policy for trajectory following  
   - Output corrective actions (steering/throttle/braking commands)


---

## Tech-stack

**Hardware Layer:** Arduino, Raspberry Pi 4B, Sensors (IMU, steering angle sensor)

**Control Theory:** Control algorithms, Kalman filter for sensor data processing

**Physics:** Vehicle kinematics, electronic circuits, motor control

**ML:** Reinforcement Learning (RL)

**Sensor Processing:** Kalman filter, Low-pass filters, High-pass filters


---

## Weekly commitments

During the first week, our team held several meetings where we discussed the main idea of ​​the project and defined the roles and responsibilities of each team member. We also defined the target users and the initial scope of the project.

### Individual contribution of each participant

**Valeria:**
- Preparing and assembling the platform and replacing components: \\
Replacing electrical speed controller (ESC) module \\
Integration Arduino \\
Сonnection Arduino to motors, wheel rotation control and signal transmitter \\
Changing tires for better drift entry \\
[Photos](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/tree/main/Robot)

**Nikolay:**
- Installing the OS on Raspberry Pi [Screenshot](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/RaspberryPi/Installed%20OS%20on%20Raspberry%20Pi.jpg)
- Setting up Raspberry Pi for remote control [Screenshot](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/RaspberryPi/Setup%20Raspberry%20Pi%20Remote%20Control.jpg)
- Writing sample code for communication between IMU sensor and the Raspberry Pi [Code](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/commit/ec93889acf8c9435f2a5095d5127139a4670b23f)

**Lidia:**
- Review research of receiving data from IMU sensor [Reference](https://github.com/hibit-dev/mpu9250/tree/master/src/complementary_filter)
- Selecting algorithm for filtering noise from the sensor [Reference](https://www.hibit.dev/posts/67/complementary-filter-and-relative-orientation-with-mpu9250)

**Ilyas:**
- Searching and reviewing many researches on existing solutions in the field of vehicle dynamics, unmanned systems, and security systems \\
Reviewed researches: [Research 1](https://www.tandfonline.com/doi/epdf/10.1080/00423114.2025.2487186?needAccess=true), [Research 2](https://www.semanticscholar.org/paper/Multivoltage-Vector-Modulation-Based-Integrated-of-Wang-Zhu/731e0a52688689f3527cad52defe0c4c51ff0ab7), [Research 3](https://www.semanticscholar.org/paper/Adaptive-Learning-based-Model-Predictive-Control-Zhou-Hu/2ded05fe7f0f68c1fb979924b865b2652292a1e7), [Research 4](https://www.semanticscholar.org/paper/Sensor-Fusion-for-Accurate-Computation-of-Yaw-Rate-Gustafsson-Ahlqvist/72720e385f630b386cdf518e6c8169e6a8a92101), [Research 5](https://www.semanticscholar.org/paper/Front-Rear-Axle-Torque-Vectoring-Control-for-Diez-Velenis/68f1281c93369b454906b95ab099ca3354cfd914), [Research 6](https://i.cs.hku.hk/fyp/2017/fyp17014/docs/Final_report.pdf), [Research 7](#https://alexliniger.github.io/assets/pdf/master_thesis_liniger.pdf)
- Сonducted problem validation and market research

**Andrey:**
- Helping to search and review researches on the project topic \\
Reviewed researches: [Research 1](https://www.semanticscholar.org/paper/Autonomous-RC-Car-Drifting-Henry-Perrault/5fd62344fe835c07356fd222a5647274fa502b26), [Research 2](https://www.semanticscholar.org/paper/Design-of-a-Drift-Assist-Control-System-Applied-to-Wu-Yao/f314010db3658ae067ff06e595999a39fcd0f070), [Research 3](https://www.semanticscholar.org/paper/Consecutive-Inertia-Drift-of-Autonomous-RC-Car-via-Lu-Yang/58cb4525eec57d823a7e874a30fc4ff960b0cb6b)
- Compiling user stories
- Сompiling a weekly report

### Confirmation of the code’s operability

We confirm that the code in the main branch:

- 🟩 In working condition.
- 🟩 Run via docker-compose (or another alternative described in the `README.md`).
