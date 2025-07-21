# Week #3

## Implemented MVP features

This week we completed the core MVP features focused on the Hardware and Firmware and common 

### Hardware

- Cart-Pole hardware assembly ([#27](https://github.com/IU-Capstone-Project-2025/total_control/issues/27))
  - Cart, rail, and pendulum arm assembled
  - Wiring completed and verified
  - End-button added and connected ([#28](https://github.com/IU-Capstone-Project-2025/total_control/issues/28))

- ESP32 physical integration ([#22](https://github.com/IU-Capstone-Project-2025/total_control/issues/22))
  - Mounted and connected to power supply and peripherals

- Case design and 3D modeling ([#20](https://github.com/IU-Capstone-Project-2025/total_control/issues/20), [#21](https://github.com/IU-Capstone-Project-2025/total_control/issues/21))

### Firmware & Backend

- Common firmware structure created ([#11](https://github.com/IU-Capstone-Project-2025/total_control/issues/11))
  - Shared firmware codebase for ESP32
    
- Init script implemented ([#12](https://github.com/IU-Capstone-Project-2025/total_control/issues/12))
  - Boots ESP32 and initializes pins and components

- State management logic added ([#25](https://github.com/IU-Capstone-Project-2025/total_control/issues/25))

### Software Design

- CartPole class structure implemented ([#14](https://github.com/IU-Capstone-Project-2025/total_control/issues/14))
  - Object-oriented design
  - Includes step(), reset(), and render() methods

- Repo structured and cleaned ([#1](https://github.com/IU-Capstone-Project-2025/total_control/issues/1))

### Functional User Journey

> A user connects the ESP32-powered cart-pole system, starts the firmware using the init script, and observes hardware movement while system states are logged for debugging. This demonstrates the full integration of software and hardware for a working MVP.

---

## Demonstration of the working MVP

[Video of tests](https://drive.google.com/file/d/1z7wkOc1qnxFgIIeBLKd8Nusf9HyCIy37/view?usp=sharing)

[Same video on github](https://github.com/IU-Capstone-Project-2025/total_control/blob/Reports/MWP_video_week_3.MOV)

---

## Internal demo

- MVP reviewed by team with all hardware components assembled
- Firmware boot confirmed via serial output
- Class-based code design approved for extensibility

---
## ML integrartion 

The goal is to integrate a RL system that can learn to balance cart-pole system. The program should:

Interact with the real or simulated cart-pole via `step()` and `reset()` functions.

Being trained with `fit()` function

Predicts actions with `predict()` function

The structure of ML API can look like this:

```python
  class RLAgent:
    def init(self, env, **kwargs):
        self.env = env

    def fit(self, episodes: int = 1000):
        raise NotImplementedError

    def predict(self, state):
        raise NotImplementedError

    def evaluate(self, episodes: int = 10):
        raise NotImplementedError
```

Then we make sure that our cart pole class has reset() that returns initial state and step(action) returns (next_state, reward, done)

And then we can implement a simple RL agent

```python

import random
import numpy as np
from collections import deque
import torch
import torch.nn as nn
import torch.optim as optim

class QNetwork(nn.Module):
    def init(self, state_dim, action_dim, hidden_sizes=[64, 64]):
        super(QNetwork, self).init()
        layers = []
        input_dim = state_dim
        for h in hidden_sizes:
            layers.append(nn.Linear(input_dim, h))
            layers.append(nn.ReLU())
            input_dim = h
        layers.append(nn.Linear(input_dim, action_dim))
        self.model = nn.Sequential(*layers)

    def forward(self, x):
        return self.model(x)

class DQNAgent:
    def init(self, env, buffer_size=10000, batch_size=64, gamma=0.99,
                 lr=1e-3, epsilon_start=1.0, epsilon_end=0.01, epsilon_decay=0.995):
        self.env = env
        self.state_dim = env.observation_space.shape[0]
        self.action_dim = env.action_space.n

        self.q_network = QNetwork(self.state_dim, self.action_dim)
        self.target_network = QNetwork(self.state_dim, self.action_dim)
        self.target_network.load_state_dict(self.q_network.state_dict())

        self.optimizer = optim.Adam(self.q_network.parameters(), lr=lr)
        self.criterion = nn.MSELoss()

        self.buffer = deque(maxlen=buffer_size)
        self.batch_size = batch_size
        self.gamma = gamma

        self.epsilon = epsilon_start
        self.epsilon_end = epsilon_end
        self.epsilon_decay = epsilon_decay

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.q_network.to(self.device)
        self.target_network.to(self.device)

    def predict(self, state):
        if np.random.rand() < self.epsilon:
            return self.env.action_space.sample()
        state_tensor = torch.FloatTensor(state).unsqueeze(0).to(self.device)
        with torch.no_grad():
            q_values = self.q_network(state_tensor)
        return q_values.argmax().item()

    def fit(self, episodes=500, target_update=10):
        for ep in range(episodes):
            state = self.env.reset()
            done = False
            total_reward = 0

            while not done:
                action = self.predict(state)
                next_state, reward, done, _ = self.env.step(action)
                self.buffer.append((state, action, reward, next_state, done))
                state = next_state
                total_reward += reward

                self._train_step()

            # Decay epsilon
            self.epsilon = max(self.epsilon_end, self.epsilon * self.epsilon_decay)

            # Update target network
            if ep % target_update == 0:
                self.target_network.load_state_dict(self.q_network.state_dict())

            print(f"Episode {ep}: reward={total_reward:.2f}, epsilon={self.epsilon:.3f}")

    def evaluate(self, episodes=10, render=False):
        total_rewards = []
        for _ in range(episodes):
            state = self.env.reset()
            done = False
            ep_reward = 0
            while not done:
                if render:
                    self.env.render()
                action = self.predict(state)
                state, reward, done, _ = self.env.step(action)
                ep_reward += reward
            total_rewards.append(ep_reward)
        avg_reward = np.mean(total_rewards)
        print(f"Average reward over {episodes} episodes: {avg_reward:.2f}")
        return avg_reward

    def _train_step(self):
        if len(self.buffer) < self.batch_size:
            return
        minibatch = random.sample(self.buffer, self.batch_size)
        states, actions, rewards, next_states, dones = zip(*minibatch)

        states = torch.FloatTensor(states).to(self.device)
        actions = torch.LongTensor(actions).unsqueeze(1).to(self.device)
        rewards = torch.FloatTensor(rewards).unsqueeze(1).to(self.device)
        next_states = torch.FloatTensor(next_states).to(self.device)
        dones = torch.FloatTensor(dones).unsqueeze(1).to(self.device)
        q_values = self.q_network(states).gather(1, actions)
        next_q_values = self.target_network(next_states).max(1)[0].unsqueeze(1)
        expected_q = rewards + self.gamma * next_q_values * (1 - dones)

        loss = self.criterion(q_values, expected_q.detach())
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
```

# Weekly commitments

## Individual contribution of each participant

Anastasia - [Write 🫧 controller](https://github.com/IU-Capstone-Project-2025/total_control/commits?author=StasiaNenastie) 

Evgenii - [3D model and blueprints for controller container](https://github.com/IU-Capstone-Project-2025/total_control/commit/f5d9547fc745bf995561105e6385729346f0d378)

Artyom - [Documentation via Sphinx](https://github.com/IU-Capstone-Project-2025/total_control/commit/760a3a5d4ea73bfbf63ce265c0089f90029d4c9a#diff-8ef404030a484d54db89ecc940a02d66d8cc4f55864528606d79e3f5547b433b)

Petr - [Write report](https://github.com/IU-Capstone-Project-2025/total_control/commit/5e8a2c6f1d7ce5efccc93700c9c3c01922524246)

Marat - [Firmware MVP](https://github.com/IU-Capstone-Project-2025/total_control/commit/921fc9ea2c93f5e39d8e4f7ab2d8c1fe815bc01e)


## Plan for Next Week

- Python library development
- CI/CD for documentation
- Hardware and Firmware documentation

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the README.md).
