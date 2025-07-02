---
title: "Week #4"
---

# **Week #4**

## Testing and QA

We have tests that check:  
Signal availability between receiver and control panel  
The control device of the robot at the moment  
The speed of the wheel motors and steering angle

### Evidence of test execution

Signal availability [Code](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Robot/Tests/Test%20Signal%20Availability.ino), [Screenshot](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Robot/Tests/Test%20Signal%20Availability.png)  
Control device of the robot [Code](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Robot/Tests/Test%20Control%20Robot%20Device.ino), [Screenshot](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Robot/Tests/Test%20Control%20Robot%20Device.jpg)  
Wheel motors and steering angle [Code](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Robot/Tests/Test%20Wheel%20motors%20and%20Steering%20angle.py)

## CI/CD

### Links to CI/CD configuration files

[CI/CD](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/.github/workflows/ci.yml)

## Vibe Check
The team conducted a short health check to reflect on progress and coordination. Overall motivation remains high, and all members are aligned on the current goals. There was a need identified to improve coordination and task visibility across the team.

Action Items:
- Improve communication on task ownership and current blockers.
- Introduce regular short sync meetings to track progress and address issues early.

# Weekly commitments

## Individual contribution of each participant

**Valeria:**
- Working with platform:  
Soldering wiring, making connectors for connection and security [Photo](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Robot/System%20Connection%2001.07.jpg)  
Connecting all the wiring elements and testing the soldering correctness using an oscilloscope  
Thinking over the mat model of the machine, taking into account the frame for the correct distribution of the center of mass [Photo](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Robot/Component%20disribution%20model.jpg)   
Connecting pins for emergency stop of the machine [Photo (blue wire)](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Robot/Pins%20for%20emergency%20stop.jpg)
- Testing and optimizing the arduino [code](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/%20Hardware%20integration%20layer/arduino_imu_integration.cpp) 


**Nikolay:**
- Modeling of components for mounting equipment on a RC car [Link](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/commit/b10a2968360fa34b3cb4f9edd4e55284afea86ea)
- Printing simulated components on a 3D printer and mounting them on a car
- Making new datasets

**Lidia:**
- Preprocessing of updated datasets  
[Link](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/ML/old_staff/data_preproc_new.ipynb)  
[Link](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/ML/old_staff/data_in_world_frame_new.ipynb)  
[Link](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/tree/main/new_data)  
- Soldering and crimping wires to create a reliable connection between the IMU and Arduino  
[Photo](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Robot/Connection%20IMU%20and%20Arduino.jpg)

**Ilyas:**
- Adding the extended dataset (60 logs)
- Building a new [training set](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/ML/model_dataset_v3.npz)
- Training an updated [dynamics model](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/ML/new_train.ipynb)
- Saving [model checkpoint](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/ML/dyn_v3.pt) 


**Andrey:**
- Compiling [tests](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/tree/main/Robot/Tests) to check the operability of robot elements
- Doing [CI/CD](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/.github/workflows/ci.yml) 
- Сompiling a weekly report

## Plan for Next Week

- Defactoring code
- Solving issues with wiress
- Test MVP v2

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [✅] In working condition.
- [✅] Run via docker-compose (or another alternative described in the `README.md`).
