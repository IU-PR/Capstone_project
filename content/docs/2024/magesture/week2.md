---
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

This week, we focused on selecting the appropriate technologies to develop our game and implementing gesture recognition.

- **Game Development**: Unity
- **Model Training and Inference**: Mediapipe and TensorFlow
- **Programming Language**: C# for Unity, Python for model training
- **Development Environment**: Visual Studio Code, Unity Editor, Git for version control
- **Libraries**: TensorFlow for training models, Mediapipe for hand gesture recognition
- **Tools**: Docker for containerization, Jenkins for CI/CD

### **Architecture Design**

1. **Component Breakdown**:
    - **Gesture Recognition Module**: Utilizes Mediapipe and TensorFlow for detecting and interpreting hand gestures.
    - **Game Engine**: Unity handles game logic, physics, and rendering.
    - **User Interface**: Unity's UI system provides visual feedback and user interactions.
    - **Networking (Future)**: For potential multiplayer capabilities.
    - **Data Management**: Manages game state and user settings within Unity.

2. **Data Management**:
    - **Local Storage**: Unity PlayerPrefs for user settings and game states.
    - **Temporary Data**: Managed in-memory using Unity's data structures.
    - **Persistence**: Local storage within the Unity environment for the current scope.

3. **User Interface (UI) Design**:
    - **Game Screen**: Displays characters, health bars, timers, and spells.
    - **HUD**: Shows player stats, current spells, and last detected gesture.
    - **Menus**: For game settings, player setup, and instructions.

4. **Integration and APIs**:
    - **Gesture API**: Custom module in Unity to interface with Python scripts for gesture detection via Mediapipe and TensorFlow.
    - **Game Logic API**: Interfaces between the gesture module and Unity game engine to trigger in-game actions.

5. **Scalability and Performance**:
    - **Optimized Rendering**: Using Unity's optimization tools to maintain smooth performance.
    - **Efficient Gesture Detection**: Using lightweight models in TensorFlow and Mediapipe to reduce processing load.

6. **Security and Privacy**:
    - **Data Privacy**: Ensuring minimal data collection, focusing solely on necessary gesture data.
    - **Secure Local Storage**: Protecting user data within the Unity environment.
    - **Webcam Access**: Obtaining explicit user permission for webcam use.

7. **Error Handling and Resilience**:
    - **Robust Error Handling**: Implementing comprehensive error handling in both C# (Unity) and Python.
    - **Logging**: Using logging frameworks in Unity and Python to record errors and debug information.

8. **Deployment and DevOps**:

    - **Platform-Specific Builds**: We will build the game for multiple platforms, including Windows, and Linux, leveraging Unity's cross-platform capabilities.
    - **Updates**: Setting up a streamlined process for releasing updates and patches across all supported platforms.

### **Week 2 Questionnaire:**

1. **Tech Stack Resources**:
   - We identified and began using several key resources, including official documentation for Unity, Mediapipe, and TensorFlow. We also explored community forums and tutorials to better understand implementation strategies.

2. **Mentorship Support**:
   - We consulted with our industry mentors to validate our tech stack choices and gain insights into potential pitfalls and best practices.

3. **Exploring Alternative Resources**:
   - We evaluated other game development engines and machine learning frameworks but found Unity, Mediapipe, and TensorFlow best suited to our needs.

4. **Identifying Knowledge Gaps**:
   - We recognized gaps in our understanding of advanced gesture recognition and real-time game rendering. We are addressing these through targeted learning sessions and online courses.

5. **Engaging with the Tech Community**:
   - We joined relevant forums and groups such as the Unity community, TensorFlow forums, and Mediapipe discussion groups to seek advice, share our progress, and learn from experienced developers.

6. **Learning Objectives**:
   - Our objectives this week included mastering the basics of Mediapipe for gesture detection, integrating TensorFlow for model training, and using Unity for game development.

7. **Sharing Knowledge with Peers**:
   - We held a knowledge-sharing session within our team to ensure everyone is up to speed with the selected technologies and their applications in our project.

8. **Leveraging AI**:
   - We are leveraging AI through Mediapipe’s hand-tracking capabilities and TensorFlow’s machine learning models to accurately detect and interpret hand gestures in real-time.

### **Tech Stack and Team Allocation**

| Team Member              | Track                                       | Responsibilities   |
|--------------------------|---------------------------------------------|--------------------|
| Dzhavid Sadreddinov      | ML | Gesture recognition model |
| Pavel Volkov            | Game Dev | Game |
| Diana Vostrova            | Design | Game Design |
| Alsu Khairullina           | Data  | Data for model training |
| Makar Vavilov            | Project Manager | Manage tasks/deadlines, reports |

### **Weekly Progress Report**

Our team made significant progress this week by finalizing the tech stack for our project and designing the overall architecture. Specifically, we:

- Selected Unity for game development to leverage its robust cross-platform capabilities.
- Chose Mediapipe and TensorFlow for gesture recognition and model training.
- Defined the core components of our architecture, including the Gesture Recognition Module, Game Engine, User Interface, and Data Management.
- Established a detailed plan for integrating our components and ensuring scalability, performance, and security.
- Set up our development environment with essential tools like Visual Studio Code, Unity Editor, Docker, and Jenkins.

### **Challenges & Solutions**

1. **Challenge**: Integrating Mediapipe with Unity for real-time gesture recognition.
   - **Solution**: Conducted thorough research on best practices for integrating Python-based machine learning models with Unity. We found and implemented a custom module approach that allows for efficient communication and real-time data exchange between Unity and Mediapipe/TensorFlow.

2. **Challenge**: Ensuring the game runs efficiently across various platforms.
   - **Solution**: Researched optimization techniques specific to Unity and lightweight models for TensorFlow and Mediapipe. By applying these best practices, we improved rendering and gesture detection performance, ensuring a smooth gameplay experience on all target platforms.

3. **Challenge**: Addressing potential security and privacy concerns related to webcam access.
   - **Solution**: Investigated industry standards and best practices for data privacy and security. Implemented strict data privacy measures based on our findings, ensuring only essential data is collected, and user permissions are explicitly obtained for webcam access. Local storage data is encrypted to protect user information.

### **Conclusions & Next Steps**

This week, we successfully laid the groundwork for our project with a clear understanding of our tech stack and architecture. Our next steps include:

1. **Development**: Begin coding the core components of the game, starting with the Gesture Recognition Module and basic game mechanics in Unity.
2. **Integration**: Integrate Mediapipe and TensorFlow with Unity, ensuring seamless communication and real-time gesture recognition.
3. **UI Design**: Develop the initial user interface, focusing on player feedback elements like health bars, spell indicators, and gesture displays.
4. **Community Engagement**: Continue engaging with tech communities for support and feedback, and share our progress to gain insights from experienced developers.

By following these steps, we aim to transition smoothly from planning to development, ensuring that our game remains on track for a successful launch.