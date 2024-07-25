---
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

We chose our tech stack to make sure our app is fast, reliable, and easy to develop.

The Vision Framework is perfect for detecting face landmarks in real-time, which is crucial for accurate eye tracking. CoreML lets us use Apple's Neural Engine and M family chips to process gaze estimation quickly on the user's device without needing external help.

For the backend, we picked FastAPI because it’s simple and stable, making it easy to build and maintain. SwiftUI was our choice for the user interface because it has a great API, is easy to learn, and allows for rapid development.

In short, our tech stack includes the Vision Framework for real-time face detection, CoreML for efficient model processing, FastAPI for a reliable backend, and SwiftUI for fast UI development. This setup ensures our app works well and is easy to build and maintain.

### **Architecture Design**

1. **Component Breakdown**:

   Our system consists of three main components: the Server, the App, and a simple Web page. The Server handles backend processes and logging. The App performs eye tracking and proctoring, ensuring all actions are processed locally on the user's device. The Web page allows administrators to monitor user behavior and detect cheating in real-time.

2. **Data Management**:

   There's no need for extensive data management since we don't store any user data. Proctoring sessions are temporary and exist only while they are running. This approach ensures maximum privacy and reduces the risk of data breaches.

3. **User Interface (UI) Design**:

   The UI design follows Apple’s Human Interface Guidelines, ensuring a seamless and intuitive user experience. SwiftUI helps us create a responsive and visually appealing interface that aligns with Apple’s design principles.

4. **Integration and APIs**:

   Our integration relies on robust APIs to ensure smooth communication between components. The app communicates with the server using efficient and secure endpoints provided by FastAPI, enabling real-time monitoring and updates.

5. **Scalability and Performance**:

   By leveraging CoreML and the Vision Framework, our app runs efficiently on user devices, making it scalable without the need for powerful external servers. The use of Docker for deployment ensures that our server environment is consistent and can handle multiple instances easily.

6. **Security and Privacy**:

   Security and privacy are paramount. All processing is done locally on the user’s device, ensuring that no sensitive data leaves the device. The backend server only logs necessary actions without storing any personal information.

7. **Error Handling and Resilience**:

   For error handling, the app relies on Swift’s type and memory safety, ensuring that all errors are managed effectively. The server uses logging to track and manage errors, providing resilience and easy troubleshooting.

8. **Deployment and DevOps**:

   Deployment is handled using Docker, allowing for a consistent and isolated environment. This ensures that our app and server can be easily deployed and scaled across different platforms without compatibility issues.

### **Week 2 questionnaire:**

1. Tech Stack Resources:

   For our tech stack resources, we primarily use StackOverflow, Pytorch, and Apple Documentation. These resources provide the necessary information and support for working with the various technologies and frameworks in our project.

   - [Vision Framework](https://developer.apple.com/documentation/vision)
   - [Core ML](https://developer.apple.com/documentation/coreml/)
   - [Swift UI](https://developer.apple.com/tutorials/swiftui/)

2. Mentorship Support:

   Currently, I do not have any mentorship support. I work independently and rely on self-learning and online resources to advance my knowledge and skills.

3. Exploring Alternative Resources:

   To supplement my learning, I explore alternative resources such as online tutorials, forums, and documentation. These help me gain a deeper understanding of the technologies I am working with and find solutions to any challenges I encounter.

4. Identifying Knowledge Gaps:

   As a web developer, I need to learn more about Apple frameworks and machine learning. These areas are crucial for our project's success, and I am focusing on improving my skills in these domains.

5. Engaging with the Tech Community:

   Engaging with the tech community is important, but currently, I mainly interact with online communities and forums like StackOverflow to seek advice and share knowledge.

6. Learning Objectives:

   My main learning objective is to understand how SwiftUI apps are built. This involves mastering SwiftUI, AppKit, and other related Apple frameworks to create a seamless and efficient app.

7. Sharing Knowledge with Peers:

   At this moment, I do not share knowledge with peers since I have no teammates and there is no mentorship support. My learning is self-directed and independent.

8. Leveraging AI:

   We use an LLM as a Cognitive Model inside Xcode to provide better code completions. This AI support helps improve coding efficiency and accuracy, making development smoother and more productive.

### **Tech Stack and Team Allocation**

| Team Member        | Track      | Responsibilities      |
| ------------------ | ---------- | --------------------- |
| Aleksandr Strijnev | Everything | App, Sever, Web Panel |

### **Weekly Progress Report**

Our team did some initial research on available solutions and began writing parts of the app in SwiftUI. We focused on understanding how to implement eye-tracking features and integrating them with the Vision Framework and CoreML. The initial coding efforts in SwiftUI are aimed at setting up the user interface and ensuring it aligns with Apple’s Human Interface Guidelines. This week’s progress lays the foundation for developing a reliable, privacy-focused eye-tracking app for remote exams and interviews.

### **Challenges & Solutions**

This week, we faced a significant challenge due to the lack of tutorials on handling frames from AVCaptureSession in SwiftUI apps. This made it difficult to find clear guidance on integrating real-time video processing with our app’s user interface.

### **Conclusions & Next Steps**

This week, we made progress in understanding and starting the integration of AVCaptureSession with SwiftUI, despite the challenges. Next, we will focus on performing face detection and drawing detected landmarks for debugging. This will help us ensure that our eye-tracking feature works accurately and efficiently in real-time.
