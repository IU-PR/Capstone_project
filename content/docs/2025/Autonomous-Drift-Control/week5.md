---
title: "Week #5"
---

# **Week #5**

## Feedback

### Sessions

We conducted [interviews with three motorsport enthusiasts](https://docs.google.com/spreadsheets/d/1S-oA4u_IXEhWL7dinKlwEAH9mcN0Br7n4A8gmBqBUuM/edit?usp=sharing) involved in drifting or rally driving. All interviewees are external to the development team and actively participate in amateur or semi-professional motorsport environments.

#### Interviewee 1 (Andrey): Drift car builder, winter competitions
- Uses ECU data and competition telemetry to analyze performance.
- Skeptical about autonomous drift systems.
- Sees drift as a matter of personal control and sensation.
- Predictive tools not useful for experienced drivers but helpful for post-run analysis.
- Would not test predictive control modules; values human control.
- **Success metric:** Stable runs.

#### Interviewee 2 (Ilya): Amateur rally driver
- Drift is important in rally, not for show but for cornering performance.
- Avoids tech due to weight constraints in rally cars.
- Unfamiliar with autonomous drift systems.
- Prefers practice over theoretical tools; prefers manual driving.
- Open to viewing the system, but wouldn’t test it.
- **Success metric:** Avoiding crashes.

#### Interviewee 3 (Dmitry): Track-day and drift hobbyist
- Uses GPS logs and video for drift analysis.
- Aware of Toyota and Stanford drift projects; finds them inspiring.
- Predictive tools could help beginners.
- Supports AI for error analysis and post-run feedback.
- Would test drift prediction system if optional and safe.
- **Success metrics:** Stability, safety, and transparent logic.

---

### Analyze

Based on these user sessions, we extracted key insights and prioritized issues as follows:

| Priority | Issue | Notes |
|----------|------------------|-------|
| High | **Experienced drivers rely on "feel" over data** | Predictive alerts seen as unnecessary or distracting for skilled users. |
| High | **Stability and safety are top priorities** | All users agree that if the system is unpredictable or unstable, it won’t be trusted. |
| Medium | **AI is more accepted as an analytical tool than a controller** | Users are open to post-run feedback or visualization, not live control override. |
| Medium | **Skepticism toward autonomy remains strong** | Most users would only test autonomous drift in simulation or on closed tracks. |
| Low | **Beginners and non-sport users could benefit from predictive alerts** | Some believe such tools could help regular drivers or large vehicles (e.g., trucks). |

## Iteration & Refinement

### Implemented features based on feedback

Based on the user interviews, we refined our focus toward making the drift control system more interpretable, stable, and suitable for real-world use:

- **Prioritized system stability** as the key success metric, reflecting feedback that unpredictability is unacceptable in drift control.

- **Planned visualization** of control logic and prediction errors, as several users expressed interest in reviewing their drift behavior retrospectively.

- **Refined control thresholds and yaw rate damping** in the MPC logic to improve predictability and smoothness — directly addressing concerns about loss of control during surface transitions.

These changes were implemented to align better with user expectations and practical usability in real-world motorsport scenarios.

### Performance & Stability

We measure the performance and stability of our system based on key real-world indicators relevant to drift control:

- **Drift Recovery Time**: how quickly the system reduces yaw rate after initiating a skid.

- **Prediction Error (MSE)**: accuracy of the dynamics model in predicting next-state values from real driving data.

- **Control Loop Latency**: time between sensor input and control output; our target is ≤ 20 ms.

- **Consistency of Trajectory Correction**: whether the car follows a predictable, repeatable path during recovery.

These metrics are tracked during offline analysis and real RC car tests. Early experiments show the MPC controller can reduce yaw rate ~3× faster than human input. Future improvements will focus on reducing prediction error and enhancing real-time responsiveness.

### Documentation

Our project includes the following types of documentation to support development, collaboration, and reproducibility:

- **README.md**  
Project overview, setup instructions, usage guide, and contributor info.

- **ML/RL Work Plan**  
Describes the learning architecture, dataset structure, training goals, and rollout pipeline.

- **CI/CD Configuration**  
GitHub Actions workflow file documents automated testing and code checks on push/PR.

- **Hardware Setup Guide (Planned)**  
Will document connection diagrams, component list, and on-board installation for the RC car.

- **Sprint Reports / Progress Logs**  
Track team activity and feature development over time.

### ML Model Refinement

Initially, our MVP used a simple ML model that adjusted the steering angle based on vehicle state to prevent loss of control. The model was trained on a small dataset of 32 drift recovery sequences and showed promising results in early tests.

In the second iteration, we expanded the dataset to 60 sequences and enhanced the model to control both steering and throttle, giving it greater flexibility and realism. However, the increased complexity led to slower inference times. To address this, we reduced the hidden layer size from 128 to 32 units, which improved speed but slightly degraded prediction accuracy.

To balance performance and precision, we plan to:

- Expand the dataset further to improve generalization;

- Use a hidden layer size of 64 units as a compromise between speed and accuracy;

- Perform hyperparameter tuning, instead of relying solely on the default Adam optimizer settings.

All iterations so far have used the Adam optimizer due to its robustness and efficiency, but more advanced tuning will be applied in the final product to maximize accuracy and control stability.

# Weekly commitments

## Individual contribution of each participant

**Valeria:**
- Testing the wiring in the RC Car
- Testing a [new algorithm](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/%20Hardware%20integration%20layer/arduino_imu_integration.cpp) (drift + skidding)
- Composing [interview questions](https://docs.google.com/spreadsheets/d/1S-oA4u_IXEhWL7dinKlwEAH9mcN0Br7n4A8gmBqBUuM/edit?usp=sharing)

**Nikolay:**
- Refactoring [code for old model](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/commit/cac1a95f97cc925e07f68eb918268c27f93d0ae9) and [tune hyperparameters](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/commit/7a9543e5ffa4b789d813e7755691f66aa91a67ce)
- Refactoring [code for new model](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/commit/ae9501569d67e22f6eeb1ad2e95d5597d9880b0f) and test whole code

**Lidia:**
- Simulating of movement in a circle (different number of circles) with final stabilization
- Doing graphs of trajectories and car control

[Link](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/commit/3cffe15d70179fde6809637f8a0b12abc7c2dbd0)

**Ilyas:**
- Redesigning the [model training script](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/ML/light_version/new_train.py) for new data (everything has changed except preprocessing)
- Writing a [script for inference](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/ML/light_version/dyn_v3.pt) of the model and the operation of the machine
- [Simplifying inference script](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/tree/main/ML/light_version) so that the raspberry pi can process the input and output of the model within 2 ms
- [Simplifying the model](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/ML/light_version/model_dataset_v3.npz): made the dataset more accurate, changed the hidden layer from 128 to 32

**Andrey:**
- Conducting [interviews](https://docs.google.com/spreadsheets/d/1S-oA4u_IXEhWL7dinKlwEAH9mcN0Br7n4A8gmBqBUuM/edit?usp=sharing) and analyzing the results obtained
- Сompiling a weekly report

## Plan for Next Week

- Set up cameras and teach the algorithm to drift while avoiding obstacles 
- Print the case onto the machine itself, for individual elements 
- Make printed circuit boards for reliable connection

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [✅] In working condition.
- [✅] Run via docker-compose (or another alternative described in the `README.md`).