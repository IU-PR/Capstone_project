## **Tech Stack:**

**Backend:** 
Python will be used for backend development. For now the LLM is accessed via API call to Replicate’s serverless infrastructure. This way the development is very easy and fast. Later, we can switch to our own deployed model or a different serverless infrastructure if needed.

**Data Storage (Mobile):** 
- CoreData will be used for local data storage within the iOS application, providing efficient and reliable storage and retrieval of user data on the device. 
- For Android, we will use Room for local data storage, ensuring efficient and reliable management of user data on Android devices.

**Deployment:** We'll utilize TestFlight for beta testing and distributing pre-release versions of our iOS app to external testers, ensuring comprehensive feedback and bug testing before the official release. For Android, we'll employ Google Play's internal testing track for efficient beta testing and validation across devices. This streamlined approach enhances our ability to iterate and refine our applications based on user feedback prior to full deployment.

**Design and Prototyping:** Figma will be utilized for designing and prototyping the user interface, allowing for collaborative design iterations and ensuring a seamless user experience.

**Mobile Development:**
- For iOS mobile development, we'll use Swift programming language and the iOS SDK to create a native mobile application. Swift will enable us to build high-performance, feature-rich applications optimized for iOS devices. We'll also utilize API integration to connect our iOS app with backend services for data retrieval and manipulation.

- For Android mobile development, we'll use Kotlin programming language and Android Studio to create a native mobile application. Kotlin will enable us to build robust, high-performance applications optimized for Android devices. Similar to the iOS app, we'll utilize API integration to connect our Android app with backend services for data retrieval and manipulation.


## **Architecture Design**

1. **Component Breakdown**: 
{{<mermaid>}}
graph TD;
    API["LLM from API provider"]
    BackendServer["Backend Server (Python)"]
    AndroidApp["Android App"]
    iOSApp["iOS App"]
    Room["Room (Local storage)"]
    CoreData["CoreData (Local storage)"]

    API -.response.-> BackendServer
    BackendServer -.prompt.-> API
    BackendServer -.response.-> AndroidApp
    BackendServer -.response.-> iOSApp
    AndroidApp -.request.-> BackendServer
    iOSApp -.request.-> BackendServer
    AndroidApp <--> Room
    iOSApp <--> CoreData

{{</mermaid>}}

    - LLM API — generates text from prompts

    - Backend — provides endpoints for the apps and contains all business logic for processing (but not storing) the data

    - App — user applications for 2 mobile operating systems. Store data, send requests to backend. Do not talk to the LLM API directly


2. **Data Management**: We will store user’s data on device to ensure maximum security. This way, user’s private thoughts are only accessible by the user and can be easily deleted. Described in more detail above.

3. **User Interface (UI) Design**: To ensure a positive user experience (UX) and adhere to effective design principles, we meticulously crafted wireframes and mockups. These visual representations allowed us to iterate on the layout and flow of our application, ensuring intuitive navigation and seamless interaction for our users. By prioritizing clarity, simplicity, and user-centric design, we aimed to create an engaging and user-friendly interface that meets the needs and expectations of our target audience.

<img src="/2024/dear-diary/loading.png" alt="Loading Screen" width="150">
<img src="/2024/dear-diary/main-screen.png" alt="Main Screen" width="150">
<img src="/2024/dear-diary/emotions.png" alt="Emotion Screen" width="150">
<img src="/2024/dear-diary/chat.png" alt="Chat Screen" width="150">

[View Figma Design](https://www.figma.com/design/f0ED5N3A4DEwiGBbNzHEoU/%D0%9A%D0%B0%D0%BF%D1%81%D1%82%D0%BE%D0%BD-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82?node-id=57-64&t=iuqwLmJYgZQvyebC-1) 🔗

4. **Integration and APIs**:  During the development we will use free of charge serverless Replicate Instance API. This API will be called from a simple python backend server. 

5. **Scalability and Performance**: 
    - When designing iOS applications, scalability involves anticipating future user growth and ensuring the architecture can handle increased loads and data volumes.  We will utilize CoreData for efficient local data storage, optimizing fetch requests and utilizing background contexts to maintain UI responsiveness and leverage Swift's concurrency features for parallelism and managing concurrent tasks.
    - For Android, scalability means designing with scalability in mind from the outset. Room Persistence Library provides a robust ORM for local data storage, supporting large datasets efficiently. We will employ Kotlin Coroutines for asynchronous programming, enhancing responsiveness by running non-blocking tasks on multiple threads.

6. **Security and Privacy**: All requests to backend server will be encrypted with SSL. User’s data on device to ensure maximum security. We are also exploring other appropriate security measures.

7. **Error Handling and Resilience**: To maintain reliability, we will develop comprehensive error handling strategies. This includes setting up effective error logging, proactive monitoring, and implementing graceful error recovery mechanisms to minimize disruptions to user experience.

8. **Deployment and DevOps**:  Our deployment approach involves beta testing through TestFlight for iOS and Google Play's internal testing track for Android.


## **Week 2 questionnaire:**  

**1. Tech Stack Resources:** 
We are utilizing the following project-based books to enhance our knowledge and expertise in our tech stack:

- **"Designing Interfaces: Patterns for Effective Interaction Design"** by Jenifer Tidwell: This resource focuses on interaction design principles and UI patterns, helping us create intuitive and engaging user experiences in our mobile app.

- **iOS Programming: The Big Nerd Ranch Guide"** by Christian Keur and Aaron Hillegass: This book guides our iOS app development using Swift, covering UI design, data persistence, networking, and API integration with practical exercises for hands-on learning.

- **"Android Programming: The Big Nerd Ranch Guide"** by Bill Phillips and Chris Stewart: Known for its practical approach, this guide supports our Android development efforts, covering UI, networking, data persistence, and web service integration.

- **"Python Machine Learning"** by Sebastian Raschka and Vahid Mirjalili: Despite its broader focus, this book equips us with essential machine learning techniques in Python, beneficial for integrating AI features like sentiment analysis and recommendations.


These resources ensure we build a robust foundation and implement best practices across both iOS and Android platforms, enhancing our project's usability and functionality.

**2. Mentorship Support:**
This week, we plan to seek guidance from Eleonora Ilina, a psychologist at Innopolis University. We aim to consult her on the conditions that should be applied to our AI-assisted features from a psychological standpoint. Additionally, we intend to reach out to her later to demonstrate our working product and gather feedback for further improvements.

**3. Exploring Alternative Resources:**

- **Kotlin Documentation:**
    
    Kotlin is a modern programming language used for Android development, known for its concise syntax and interoperability with Java. The official Kotlin documentation provides comprehensive guides, tutorials, and reference materials essential for learning Kotlin:

- **Jetpack Compose Documentation:**

    Jetpack Compose is a modern UI toolkit for Android, designed to simplify UI development and enhance productivity. The official Jetpack Compose documentation offers guides, samples, and APIs for building declarative UIs in Android:

- **iOS Documentation:**

    iOS Documentation provides a comprehensive guide to the user interface framework, which offers a declarative approach to building intuitive interfaces across Apple's ecosystem.

**4. Identifying Knowledge Gaps:** 

- We acknowledge that our team lacks extensive experience in Android mobile development. To address this gap and ensure adherence to best practices, we are committed to watching the free lectures on "Школа мобильной разработки Android" offered by Young&&Yandex.

- In our pursuit of optimal AI models and practices for our project, we are actively researching various options. Our approach involves exploring different AI models through experimentation and testing to identify the most suitable one that aligns with our project's requirements and objectives.


**5. Engaging with the Tech Community:** Alyona Maksimova  is a member of the Coffee&Code club of Kazan iOS developers. It's important to note that we do not assign tasks to them. But we will seek support if necessary during the future project evolution.

**6. Learning Objectives:**

**Mastering CoreData for iOS Development:** 
- Objective: Gain a thorough understanding of CoreData to implement efficient local data storage in our iOS app.
- Plan: Follow the "iOS Programming: The Big Nerd Ranch Guide" and complete hands-on exercises related to CoreData. Utilize Apple's official documentation and online tutorials to reinforce learning.
- Strategies/Resources: Practical implementation in our project

**Enhancing Android Development Skills:**
- Objective: Strengthen our knowledge of best practices in Android development, focusing on Jetpack Compose and Kotlin.
- Plan: Watch the "Школа мобильной разработки Android" lectures by Young&&Yandex. Additionally, refer to "Android Programming: The Big Nerd Ranch Guide" for practical exercises.
- Strategies/Resources: Regular progress check-ins and application of learned concepts in our project.

**Integrating AI Features:**
- Objective: Research and effectively integrate AI models and pipelines into our application for features like sentiment analysis and personalized recommendations, ensuring they are appropriate and useful from a psychological perspective to enhance user well-being.
- Plan: Study "Python Machine Learning" by Sebastian Raschka and Vahid Mirjalili to understand machine learning concepts and algorithms. Investigate AI models and practices that align with our psychological objectives. Experiment with different AI models to find the best fit for our needs.
- Strategies/Resources: Conduct experiments, analyze results, and iteratively improve AI integration.

**Improving UI/UX Design:**
- Objective: Enhance our understanding of effective interaction design principles to create a user-friendly interface.
- Plan: Study "Designing Interfaces: Patterns for Effective Interaction Design" by Jenifer Tidwell. Create and iterate on wireframes and mockups using Figma.
- Strategies/Resources: Organize design critique sessions, gather feedback from team members, and apply design patterns in our project.

**7. Sharing Knowledge with Peers:**
We meet weekly to share progress and discuss challenges. These sessions are crucial for aligning on technical decisions and fostering collaboration. Additionally, we maintain ongoing discussions through various communication channels to ensure continuous knowledge exchange and refinement of project strategies.

**8. How have you leveraged AI to compensate for any lacking expertise in your tech stack?** 
- **AI-Driven Code Suggestions**: We use GitHub Copilot  for code completion and suggestions. These tools help us write efficient and accurate code by providing real-time assistance, reducing the learning curve, and enhancing productivity.
- **Chatbots and Virtual Assistants**: We use AI-driven chatbots like OpenAI’s ChatGPT for troubleshooting and finding solutions to coding problems. This allows us to quickly address issues and obtain guidance without extensive searching.


## **Tech Stack and Team Allocation**
| Team Member              | Role              | Responsibilities                                                                                                                                                   |
|--------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Alyona Maksimova (Lead)  | iOS mobile Dev    | Develop and maintain the iOS mobile application using Swift and Xcode.                                                                                           |
|                          |                   | Implement UI/UX designs into the iOS application ensuring a seamless user experience.                                                                             |
|                          |                   | Integrate APIs and backend services for data retrieval and synchronization.                                                                                       |
|                          |                   | Ensure compatibility, performance optimization, and bug fixing for iOS devices.                                                                                   |
| Elizaveta Nikolaeva      | UX/UI design      | Create wireframes, mockups, and prototypes for the iOS and Android applications using Figma.                                                                     |
|                          |                   | Design intuitive and user-friendly interfaces following design principles and usability guidelines.                                                                 |
|                          |                   | Collaborate with the development team to implement UI designs and provide design support throughout the development lifecycle.                                   |
| Kristina Bondarenko      | Android mobile Dev| Develop and maintain the Android mobile application using Kotlin and Android Studio.                                                                             |
|                          |                   | Implement UI components and navigation flows based on UX/UI designs.                                                                                              |
|                          |                   | Integrate with backend services and APIs to ensure data connectivity and functionality across Android devices.                                                    |
|                          |                   | Conduct unit testing, debugging, and performance optimization for the Android application.                                                                        |
| Andrew Levada            | ML & Backend              | Research and evaluate AI models and algorithms suitable for the project’s behavioral and mental health care applications.                                       |
|                          |                   | Implement AI functionalities such as sentiment analysis, personalized recommendations, or virtual assistant features in collaboration with the mobile development teams. |
|                          |                   | Ensure ethical considerations and data privacy in AI implementations within the application.                                                                      |
|                          |                   | Test and validate AI models for accuracy, efficiency, and integration with the mobile applications.                                                               |



## **Conclusion & Next Steps**

**iOS Development:**
Starting iOS app development, next week focuses on finishing UI layouts and starting Core Data integration. This sets the stage for efficient data management and storage.

**Android Development:**
Beginning Android app development, the goal next week is to finalize UI designs and begin implementing Room Persistence Library. This ensures smooth data handling and enhances app functionality on Android.

**ML & Backend:**
Developed a prototype backend server, testing various serverless providers before opting for Replicate Instance API. Currently, the code runs locally with interaction implemented for LLM (Meta-Llama-3-8B-Instruct). Additionally, Started on a basic system prompt that currently provides mediocre results, which will be refined in future iterations. Next steps involve experimenting with open-source models to find the most suitable one, setting up endpoints with their initial logic, and selecting a server hosting infrastructure.

## **Challenges & Solutions**

A key challenge was managing costs for LLM inference, resolved by using Replicate's free API with a limited rate. Challenges also included setting up a UICollectionView layout and navigating between pages in iOS, along with limited experience in Android development. Solutions focused on studying UICollectionViewLayout and mastering UINavigationController for iOS. Efforts also aimed at learning Android development fundamentals.

---
