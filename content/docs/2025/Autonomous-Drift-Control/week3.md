# **Week #3**

## Implemented MVP features

### **Hardware Integration**
Completely rewired the RC car. Arduino, Raspberry Pi, and sensors are mounted and connected on the vehicle.

### **Communication Setup**
Stable SSH connection established between Raspberry Pi and Arduino. IMU data is streamed and accessed remotely.

### **Sensor Fusion**
Orientation is calculated using both gyroscope and accelerometer. The values are compared and visualized with error tracking.

### **Dataset Collection** 
Collected [32 datasets](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/tree/main/old_data): 16 for normal driving, 16 with drift transitions. Ready for training the control model.

## Demonstration of the working MVP

[Videos demonstrating MVP](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Robot/IMG_0024.MOV)

## ML

**Link to the training code**: [Link](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/ML/mvp.ipynb)

We trained a feed-forward neural network (5-128-128-4) on 94k real-world (state, action -> next state) samples from straight driving and drifting. Data was preprocessed (yaw integration, normalization, rotation to global frame). The model is used in a random-shooting MPC with a 0.2s horizon, minimizing yaw rate and lateral acceleration. It outputs steering every 20 ms. In tests, the controller damped drifts approximately 3x faster than a human, completing a full data-to-control pipeline.

**Links to the initial model artifacts**: [Link](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/ML/dyn_model.pt
)

# Weekly commitments

## Individual contribution of each participant


**Valeria:**
- Collecting driving [datasets](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/tree/main/old_data)
- Writing [code](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/%20Hardware%20integration%20layer/arduino_imu_integration.cpp) for control a servo motor based on a signal from RL  
- Working with platform:  
Connecting all the elements according to the new scheme  
Integrating all computing components (Arduino, Raspberry Pi, IMU) on the machine and set up stable communication between them  
[Photo 1](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Robot/System%20Connection%2024.06.jpg), [Photo 2](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Robot/Arduino%20Connection%2024.06.jpg), [Photo 3](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Robot/Rasberry%20Pi%20Connection%2024.06.jpg)

**Nikolay:**
- Collecting driving [datasets](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/tree/main/old_data)
- Implementing the [MPC controller](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/commit/9c2aeeef97c427bb94a1aa4f3ba6913ff0463584) (random-shooting, 0.2s horizon, UART control output)

**Lidia:**
- Working with sensors:  
Preprocessed raw sensor data: timestamp conversion, yaw integration, coordinate frame rotation, angular acceleration computation  
Analyzing the values from the IMU sensors  
[Estimated](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/%20Hardware%20integration%20layer/imu/imu_angle_error.ino) the magnitude of the gyroscope error  
[Visualization](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/ML/README.md) of angular acceleration and trajectory of car (for 3 cases) 
- Helping with the collection [datasets](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/tree/main/old_data)

**Ilyas:**
- Built the full dynamics [dataset](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/tree/main/old_data): created (state, action) → next state pairs and computed normalization stats
- Trained the neural network model (5-128-128-4) using MSE and Adam, saved model weights and stats  
[Training Code](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/ML/mvp.ipynb), [Initial Model](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/ML/dyn_model.pt
)

**Andrey:**
- Replacing the [burnt-out servo](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Robot/Burnt-out%20Servo.jpg) motor with a [new one](https://github.com/IU-Capstone-Project-2025/Autonomous-drift-control/blob/main/Robot/New%20Servo.jpg)
- Сompiling a weekly report


## Plan for Next Week

**Upgrade Arduino Wiring:**  
Replace Arduino wires with higher-quality ones, solder them securely, and reinforce connections to prevent disconnections.

**Model and Mount Hardware Frames:**  
Design and 3D print custom mounts for all components to ensure a compact, safe, and organized layout inside the RC car.

**Fix Arduino–Raspberry Pi Communication:**  
Debug and optimize the connection between Arduino and Raspberry Pi to ensure fast, stable, and lossless data transfer — current delays and dropouts need to be resolved.

**Improve RL Stability:**  
Collect additional driving datasets to increase the robustness and consistency of the reinforcement learning model during drifting.

**Refactor Arduino Code:**  
Add interrupt handling for all critical and unpredictable car states to improve reliability and prevent unexpected behavior.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [ ] In working condition.
- [ ] Run via docker-compose (or another alternative described in the `README.md`).