# Week #5

## Feedback

### Sessions

We conducted three feedback sessions with external users:

| External user | Review | Main problem | Overall score |
|----------|----------|--------------|--------------|
| Dmitriy Mistrikov, Master student | This solution is very convenient for testing RL, but I was shown a very short emergency stop wire, which needs to be made longer | Emeregency Buttom wire| 4.5/5 |
| Dmitriy Vizitei, Bachelor Studnet | It's an interesting thing, but the only inconvenient thing is that the position is not in meters, but in some kind of ticks, and the force on the motor is also measured in parrots, not in N/m, and you have to add coefficients in the program | Units of measurement | 4.2/5 |
| Yaroslav Gorbunov, Student of Tomsk Polytechnic University | Given my limited experience in robotics (which I have none of), the most difficult and confusing part for me was determining the connection port, and I still can't replicate it myself | Auto connect | 5/5 |


### Analyze

Key insights and actions:

| Feedback | Priority | Action Taken |
|----------|----------|--------------|
| Solve problem with units | Medium | Created issue to this problem |
| A longer wire is needed | Low | A better wire was ordered |
| Needs Auto connect | Medium | Implemented automatic connection |

## Iteration & Refinement

### Implemented features based on feedback

- A better wire was ordered
- Implemented automatic connection


### Performance & Stability

The main measure of our solution's performance is the communication frequency between the controller and the library, which is also considered the sampling frequency for the entire system.

Currently, the frequency: 100 Hz.

There are several main approaches for optimizing the solution (although this is not necessary at the moment):

- Simplifying the transmitted data

- Replacing the controller with a more powerful one

- Simplifying the communication concept (moving the control function directly to the controller)

We use standard Python libraries for development and performance/stability:

- **PyTorch** – For implementing and training the DQN agent
- **NumPy** – For efficient numerical operations
- **Matplotlib** (WIP) – Planned for visualizing training performance
- **serial / pyserial** – For hardware communication with the motor controller

Basic logging and exception handling are implemented. Training is currently stable for hardware episodes up to 300+ iterations.
### Documentation

All documentation is hosted at:  
**📘 https://iu-capstone-project-2025.github.io/total_control/**

The documentation contains:

- **Firmware Documentation** – Auto-generated documentation for deep understnading how firmware works
- **API Reference** – Auto-generated documentation for interacting with the system

#### API Reference Structure:

- **LabDevice**  
  Base class for communication with lab hardware over serial interface. Provides methods for:
  - `connect()` / `disconnect()` for managing serial connection
  - Context manager support (`__enter__` / `__exit__`)
  
- **CartPole** *(inherits from LabDevice)*  
  Interface for controlling the Cart-Pole hardware:
  - `get_joint_state()` – Returns position and velocity as a string
  - `set_joint_efforts(effort)` – Applies a force to the cart (input: int or str)
  - `start_experimnet()` – Begins data flow and operation mode
  - `stop_experiment()` – Gracefully stops the experiment
  - `get_state()` – [WIP: internal state snapshot method]

This API is actively used by the Reinforcement Learning integration and will be further expanded to include reward shaping and safety checks.

This approach to documentation is chosen because it represents the industry standard and provides an extremely convenient interface for automatically generating documentation based on properly written code with documentation.

### ML Model Refinement

We developed and integrated a Deep Q-Network (DQN) agent into the real CartPole system using the `CartPole` Python API. The RL agent observes position and velocity of the cart and applies motor effort as an action.

Improvements made:

- Switched to a real-time environment using `get_joint_state()` and `set_joint_efforts()` methods
- Refactored training loop to work asynchronously with hardware delays and serial communication
- Normalized the input state and clipped motor outputs to avoid unsafe operations
- Adjusted reward structure to favor longer balance time and penalize large accelerations

Planned refinements:

- Add reward shaping for smoother convergence
- Implement checkpoint saving/loading during training
- Tune hyperparameters: learning rate, epsilon decay, and discount factor

# Weekly commitments

## Individual contribution of each participant

Anastasia - [Library development](https://github.com/IU-Capstone-Project-2025/total_control/commit/8118eac04ecb0ac3c7f6e20531de8e2bdcd1cd64)

Evgenii - [Board design and printing](https://github.com/IU-Capstone-Project-2025/total_control/commit/6ae7315a5173997c19df38adedaf9763e8b1ccb2)

Artyom - [Add firmware auto-generated documentation](https://github.com/IU-Capstone-Project-2025/total_control/commit/51691fd3e6aefafd780ab99fbfac08c6e035d255)

Petr - [Write report, RL RnD](https://github.com/IU-Capstone-Project-2025/total_control/commit/835eb63842421206d9d4818b6205c2aaf735148b)

Marat - [Port scan feature](https://github.com/IU-Capstone-Project-2025/total_control/commit/cfa3bad0f9504bd06ee40481e967a6f25a9747a6)

## Plan for Next Week

- Test RL
- Test Controll  
- Fix code style and bags 
- Implement final features

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the README.md).
