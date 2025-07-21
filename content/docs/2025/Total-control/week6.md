# **Week #6**

## Links

- **Deployment**: https://pypi.org/project/innocontrol/
- **API Docs**: https://iu-capstone-project-2025.github.io/total_control/
- **PCB Design**:

   <img width="768" height="455" alt="PCB_PCB_controller_3_2025-07-11" src="https://github.com/user-attachments/assets/dbe6e792-924f-4745-8e1a-72ed901c5c44" />

- **Demo**: https://github.com/IU-Capstone-Project-2025/total_control/blob/Reports/Simple_controller_test.MOV

## Final deliverables

### Project overview

Our project is a **Python-based control library** for interacting with physical cart-pole mechanism. The library abstracts the complexity of serial communication and device management into a simple, user-friendly API.

The library supports both real hardware control, making it suitable for algorithm development and testing.

This solution targets robotics students, engineers and researchers working with physical lab devices, helping them simplify the process of cart-pole control and experimentation.

### Features

- Control library (`innocontrol`) for CartPole hardware interaction.
- Device connection management:
    - `connect()`
    - `disconnect()`
- Joint state retrieval:
    - `get_joint_state()` — returns positions and velocities.
- Force control:
    - `set_joint_efforts()` — sends effort/force commands to motors.
- Experiment control:
    - `start_experimnet()`
    - `stop_experiment()`
- Public API documentation (via GitHub Pages).

### Tech stack

- **Python 3.10+**
- **Serial communication** via `pyserial`
- **Sphinx** (for API documentation)
- **Docker** (optional, for packaging)
- **Markdown / GitHub Pages** (documentation hosting)
- **ESP 32 dev board** (main computaton of Controll Box)
- **C/C++ for ESP32**

### Setup instructions

1. By clonning repository:
Clone repository:

```bash
git clone https://github.com/iu-capstone-project-2025/total_control.git
cd total_control
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or by pip:

```bash
pip install innocontrol
```

2. Connect cartpole via USB
   
3. Example usage:
  
```python

from inno_control.devices import CartPole

cart = CartPole('<your /dev port>')
cart.connect()
cart.start_experimnet()

state = cart.get_joint_state()
cart.set_joint_efforts(100)

cart.stop_experiment()
cart.disconnect()

```

4. Access API documentation:
   
https://iu-capstone-project-2025.github.io/total_control/

## Presentation draft

https://docs.google.com/presentation/d/1-JeMrnjwtoxeAh8rwuWfYGbkSolINBjYeGRhfkOGHkk/edit?usp=sharing

# Weekly commitments

## Individual contribution of each participant

Artyom - [dosc API and refactor](https://github.com/IU-Capstone-Project-2025/total_control/commit/f1173bf771a13f7292a1bfdfb6d0a62f9f53584d)

Evgenii - [Hardware design and refactoring](https://github.com/IU-Capstone-Project-2025/total_control/commit/42b95bf8c38bc83b16bbf3c7bed942a0b1f4ec3d)

Anastasia - [Presentation and RL research](https://docs.google.com/presentation/d/1-JeMrnjwtoxeAh8rwuWfYGbkSolINBjYeGRhfkOGHkk/edit?usp=sharing)

Petr - [Write report and RL](https://github.com/IU-Capstone-Project-2025/total_control/commit/fbd5fbb5e1ed42d4319cdc7e44424f2c96b14beb)

Marat - [Control system and RL](https://github.com/IU-Capstone-Project-2025/total_control/commit/32db13f1aa0ac31c228c8fe1cf9f5b900ba67925)

## Plan for Next Week

- Final project presentation.

- Release library and documentation.

- Fix bugs and prepare presentation programms

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
