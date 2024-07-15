---
title: "Week #3"
---

# **Week #3**

## **Developing the First Prototype, Creating the Priority List**

### **Technical Infrastructure:**

This week, we ensured that our technical infrastructure is fully set up and operational to support the development of our prototype. We established a shared development environment that includes Unity for game development, TensorFlow and Mediapipe for model training and inference, and GPU servers for efficient model training. All team members have been given access to the necessary tools and resources, and we organized learning sessions to ensure everyone can utilize the infrastructure effectively.

### **Model Development:**

We focused on developing the machine learning model for gesture recognition. The model is being trained locally using TensorFlow and Mediapipe. We collected initial datasets and began the training process, fine-tuning the model to accurately detect and interpret hand gestures. The goal is to achieve real-time performance suitable for in-game use.

### **Game Development:**

We are developing the game using Unity. This included implementing core game mechanics, setting up the multiplayer mode, and integrating the gesture recognition system. We created the basic structure of the game, focusing on key gameplay elements and interactions. The user interface was designed and integrated to ensure a seamless user experience, prioritizing functionality over appearance at this stage.

### **Data Management:**

We implemented the necessary data management capabilities for our prototype. This involved setting up a local database using Unity’s PlayerPrefs and basic JSON files for storing user settings and game states. We designed simple data models and implemented data retrieval and storage functionalities to handle and manage user data effectively.

### **Prototype Testing:**

By the end of the week, we conducted initial rounds of testing to identify and address usability issues or bugs in our prototype. We tested the implemented features against defined user flows and scenarios to ensure they function as intended. Feedback was collected from team members to gain insights and make necessary refinements to improve the user experience.

## **Weekly Progress Report**

### **Our Team Did:**

- Set up the technical infrastructure, including Unity, TensorFlow, Mediapipe.
- Developed the gesture recognition model for training locally using TensorFlow and Mediapipe.
- Created the base structure of the game in Unity, focusing on core mechanics and multiplayer mode.
- Designed key UI elements to support gameplay.
- Implemented basic data management using Unity’s PlayerPrefs and JSON files.
- Conducted initial rounds of prototype testing and collected feedback.

### **Prototype Features:**

- **Gesture Recognition**: Implemented using Mediapipe and TensorFlow, allowing users to control the game with hand gestures.
- **Basic Game Mechanics**: Developed core game logic and interactions in Unity.
- **User Interface**: Designed and integrated key UI elements, including health bars, spell indicators, and gesture displays.
- **Data Management**: Basic storage and retrieval of user settings and game states.

### **Challenges & Solutions:**

- **Challenge**: Integrating Mediapipe with Unity for real-time gesture recognition.
  - **Solution**: Conducted research on best practices to enable efficient communication and data exchange between Unity and Mediapipe/TensorFlow.

- **Challenge**: Ensuring efficient performance across multiple platforms.
  - **Solution**: Researched optimization techniques specific to Unity and TensorFlow. Applied these best practices to enhance rendering and gesture detection performance.

- **Challenge**: Addressing privacy concerns related to webcam access.
  - **Solution**: Investigated industry standards and implemented strict data privacy measures, ensuring only essential data is collected and user permissions are obtained. We will process images in real-time with saving webcam images in any way.

### **Conclusions & Next Steps:**

This week, we successfully created the base for our game and multiplayer mode, designed key elements, established the model learning pipeline, and began data collection. Our next steps include:

- **Further Development**: Continue enhancing the core components of the game, including more advanced game mechanics and accurate gesture recognition.
- **UI Refinement**: Improve the user interface for better usability and visual appeal.
- **Advanced Data Management**: Implement more robust data management solutions to handle increased data complexity.
- **Comprehensive Testing**: Conduct more extensive testing to identify and fix potential issues.
- **User Feedback**: Start collecting feedback from internally (testing by ourselves) to gain insights.

By focusing on these areas, we aim to refine our prototype and ensure it meets the goals and expectations outlined in our project plan.