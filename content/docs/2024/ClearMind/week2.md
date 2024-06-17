---
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

- **LLM’s**: LangChain, LangSmith, LangServe
- **Frontend**: Next.js, TailwindCSS, Vercel AI SDK
- **Backend**: PostgreSQL, FastAPI, Supabase SDK

### **Architecture Design**

1. **Component Breakdown**:
    - **LLM Microservice**: Powered by Azure AI, this handles our large language model. It processes user inputs, generates smart responses, and integrates smoothly with the rest of the system to provide intelligent and context-aware interactions.
    - **Backend**: Built with FastAPI, it handles API requests, manages data flow between the frontend and the database, and communicates with the LLM microservice to fetch and deliver AI-generated responses. It also takes care of user authentication and security.
    - **Web App**: Developed using Next.js and enhanced with the Vercel AI SDK for real-time AI interactions. It provides a user-friendly interface where users can interact with the AI, access features, and manage their accounts. The Vercel AI SDK ensures these interactions are responsive and engaging.
    - **Database**: Managed by Supabase, providing reliable and real-time data access. It stores user data, chat histories, and other essential information, maintaining context for personalized interactions based on past conversations.

    Each component works together to create a seamless system. The web app communicates with the backend to handle user requests. The backend interacts with both the LLM microservice for AI processing and the database for data management. This setup ensures our solution is flexible, scalable, and easy to maintain, allowing continuous improvement and expansion.

2. **Data Management**:
    - **Real-Time Database Access**: Using the Supabase SDK to connect to our Postgres database, we manage and retrieve data quickly and reliably, ensuring smooth backend operations.
    - **Frontend Storage**: On the frontend, we use `localStorage` to temporarily store user data, helping keep the user experience fast and responsive by reducing the need to constantly fetch data from the server.
    - **AI Data Streaming**: Using the Vercel AI SDK to stream data from our language models, we keep our AI features up-to-date and running smoothly, providing users with accurate and timely responses.

3. **User Interface (UI) Design**:
    In our project, we have two pages:
    - **Main Page**:
        - **Purpose**: Greet the user, assist them, and direct them to the relevant area.
        - **Design**:
            - **Background**: Soft, calming colors, such as light shades of blue or green.
            - **Header**: "Welcome! How can we help you today?"
            - **Buttons**: Large, clearly labeled buttons with options like "Start Conversation".
            - **Images**: Images of nature and the brain.
        
    - **Conversation Page with AI**:
        - **Purpose**: Establish a cozy and private space for the AI to converse in.
        - **Design**:
            - **Background**: Soft, calming colors, such as light shades of blue or green.
            - **Chat Window**: Simple and clean, with a large, easily readable font.
                - **User Messages**: Located on the right in blue or green bubbles.
                - **AI Messages**: Located on the left in grey or white bubbles.
            - **Input Field**: Large, with clear "Send" or up arrow sign and "Voice message" or microphone symbol buttons.

    Link for design: [Figma Design](https://www.figma.com/design/UwyAJLNxMfAARTkEx9Oril/ClearMind?node-id=0-1&t=nGdNlvfKx201NQpC-1)

4. **Integration and APIs**:
    For our AI capabilities, we rely on Azure OpenAI and Azure AI Studio for open-source language models. Our database and user authentication are managed by Supabase, with Supabase Auth (including Google sign-in) keeping things secure. For deployment, we use Vercel, which makes hosting our application smooth and scalable.

5. **Scalability and Performance**:
    Using a serverless platform with built-in autoscaling, our system can automatically adjust to demand, ensuring smooth operation even during peak times. This setup means we don’t have to manage servers, and our users always get a fast and responsive experience.

6. **Security and Privacy**:
    On the frontend, we use middleware to keep things secure. On the backend, we use token-based authentication to ensure only authorized users can access our services. We've also implemented Google authentication for app access, adding an extra layer of protection. Additionally, connections to our microservices are restricted by IP address to further enhance security.

7. **Error Handling and Resilience**:
    We’ve built our architecture using reliable platforms, ensuring top-notch uptime and resilience. If something goes wrong, our user interface is designed to keep users in the loop with clear, helpful error messages.

    Our use of a microservice architecture shines here. Each part of our system works independently, so if one piece encounters an issue, it doesn’t bring everything else down. This setup helps us fix problems faster and keeps the overall system running smoothly and reliably.

8. **Deployment and DevOps**:
    During development and testing phases, we use free platform plans (Supabase, Vercel, Azure) that handle automatic deployment for us. This setup means we don't need specialized DevOps skills to get our solutions up and running. It allows us to focus on building and refining our product rather than worrying about the deployment process. Most of these instruments have an automatic CI/CD pipeline.

### **Week 2 Questionnaire:**

1. **Tech Stack Resources**:
    Our tech stack is backed by excellent resources to ensure smooth development and operations. Each technology we use comes with thorough documentation and vibrant communities, providing us with plenty of support.

    Here are some key books that help us deepen our expertise and stay up-to-date:

    - "Building Python Web APIs with FastAPI" by Abdulazeez Adeshina: This book is a practical guide to developing production-ready web APIs with FastAPI, covering everything from the basics to advanced features.
    - "Next.js in Action" by Adam Boduch: This book provides a comprehensive guide to building server-rendered web apps with React and Next.js, covering everything from creating application pages to constructing API endpoints and deploying apps effectively.
    - "Learning React: Functional Web Development with React and Redux" by Alex Banks and Eve Porcello: This book teaches you how to build efficient React applications, covering essential concepts like functional programming, component trees, and advanced techniques like hooks and testing.

2. **Mentorship Support**:
    We started working with Eleonora Ilina, a psychologist at IU, as a mentor. With her help and the perspective of a qualified psychologist, we can create a project that can really help users psychologically. We believe that for our chosen field, it is crucial to consult with a working specialist to better understand the specifics and achieve a good result. 

    We are also on the lookout for mentors for ML and Development parts. With their experience, we will be able to create a working web application much faster, and we will be able to deal with complexities that arise in the work more easily.

3. **Exploring Alternative Resources**:
    In addition to project-based books, we’ve explored several other valuable resources to expand our understanding of our tech stack. Here are some key resources that have helped us fill knowledge gaps and gain practical insights:

    - **Prompt Engineering Course**: This YouTube video provides real examples and tutorials on prompt engineering, which is crucial for optimizing AI interactions. Watch the course: [Link](https://youtu.be/_ZvnD73m40o?si=pwAVIYPTBkSPEKMt)
    - **FastAPI Tutorials**: This YouTube playlist offers a series of tutorials on FastAPI, covering everything from the basics to more advanced concepts. It’s been incredibly helpful in understanding how to build and deploy APIs efficiently. Watch the playlist: [Link](https://www.youtube.com/playlist?list=PLqAmigZvYxIL9dnYeZEhMoHcoP4zop8-p)
    - **FastAPI + Next.js Tutorial**: This tutorial combines FastAPI with Next.js, providing a comprehensive guide on integrating backend and frontend technologies. It’s been instrumental in our project development. Watch the tutorial: [Link](https://youtu.be/HJ314MNcCck?si=vXwvSbxShM4so75t)

4. **Identifying Knowledge Gaps**:
    Here’s how we plan to address these gaps to ensure a well-rounded understanding of our chosen technologies:
    
    - **Inexperienced Backend Developer**: One of our backend developers is still gaining experience, presenting both a challenge and an opportunity for growth. To support this team member, we will provide targeted training through online courses and resources such as Udemy and Coursera. Additionally, experienced team members will offer mentorship and support, ensuring the developer acquires the necessary skills and can effectively contribute to the project.

    - **Learning New Technology for Frontend Developer**: One of our frontend developers is new to Next.js, requiring additional learning and adaptation. To facilitate this transition, we will allocate time for the developer to engage in comprehensive learning through online tutorials, documentation, and courses such as those offered by Pluralsight and freeCodeCamp. Another team member familiar with Next.js will provide guidance and support, ensuring a smooth learning curve and successful integration of the new technology into our project.

5. **Engaging with the Tech Community**:
    To network with professionals, we participate in discussions on Reddit, study materials in large communities on Telegram, and discuss ideas and problems with classmates and other university students who already have a lot of experience in ML and AI-based product development. If critical problems arise, we plan to look for offline specialists within the university.

6. **Learning Objectives**:
    This week, we have set specific learning objectives for ourselves and our team to deepen our understanding of our tech stack and enhance our project development:

    - **Gain a Fundamental Understanding of Psychological First Aid**: Our goal is to understand the basics of psychological first aid to ensure our AI provides appropriate support. We will achieve this by taking online courses on platforms like Coursera and edX, and reviewing literature from reputable sources such as the World Health Organization (WHO) and the American Psychological Association (APA).
    - **Develop Skills in Designing Conversational Agents**: We aim to enhance our ability to design conversational agents that effectively match the task at hand. To do this, we will study best practices in conversational AI design through resources like the book "Designing Bots" by Amir Shevat and tutorials from AI experts on YouTube and Medium.
    - **Get Practical Experience in Developing and Integrating Models**: We plan to gain hands-on experience in developing and integrating AI models with user-facing applications. This will involve working through practical tutorials on FastAPI, Next.js, and using tools like LangChain and Azure OpenAI. We will also utilize coding platforms like GitHub for collaborative projects and code reviews.
    - **Learn How to Manage User Data for Personalized Support**: Our objective is to learn effective methods for managing user data to provide personalized support. We will explore Supabase for real-time database management and use online tutorials and documentation to understand best practices for data security and privacy. Additionally, we will participate in webinars and online forums to learn from industry experts.

7. **Sharing Knowledge with Peers**:
    To ensure a continuous exchange of insights and experiences within our team, we have implemented several knowledge-sharing initiatives:

    - **Mentorship for Inexperienced Backend Developer**: One of our backend developers is new to the field, and to support their growth, we have paired them with a more experienced team member. This mentorship involves regular collaboration and guidance sessions where the experienced developer helps the newcomer adapt to our tech stack and workflows. By providing hands-on assistance and sharing practical insights, we aim to build their confidence and skills, fostering a supportive and productive learning environment.
    - **Support for Frontend Developer Learning Next.js**: While one of our frontend developers has a solid background in frontend development, they are new to Next.js. To facilitate their learning, we have assigned an experienced team member who is well-versed in Next.js to mentor them. This one-on-one support focuses on bridging the knowledge gap and ensuring the smooth integration of Next.js into our project. Through this targeted mentorship, we are enhancing our team's overall competency and ensuring effective implementation of new technologies.

8. **Leveraging AI**:
    - **Tools Used**: Stack Overflow, ChatGPT.
    - **Implementation**: For every new challenge or error encountered, AI tools provided quick and contextual answers. ChatGPT, in particular, was used to explain complex concepts, debug code, and suggest optimal solutions, accelerating the learning curve, and even for creating roadmaps for diving into development.

    By integrating these AI-powered tools and platforms, we were able to rapidly upskill our backend developer, ensuring they could contribute effectively to the project despite their initial lack of experience. 

### **Tech Stack and Team Allocation**

| Team Member          | Track           | Responsibilities                                                                                       |
|----------------------|-----------------|--------------------------------------------------------------------------------------------------------|
| Sergei Polin (Lead)  | Fullstack       | Overseeing web development and AI integration, ensuring cohesive project execution                    |
| Eleonora Pikalo      | Backend         | Developing and maintaining the backend systems using FastAPI and managing database operations with Supabase |
| Alexandra Egorova    | Business Analytics | Analyzing data to refine AI algorithms and ensuring that business needs are met through effective AI solutions |
| Mikita Drazdou       | Backend + ML    | Implementing AI models and managing Telegram bot integration, ensuring smooth communication between the backend and AI components |
| Iakov Saparov        | ML              | Developing and optimizing machine learning models to enhance AI capabilities, focusing on improving model accuracy and performance |
| Natalia Agapova      | Design + Frontend | Designing user interfaces and ensuring responsive web design using Next.js and TailwindCSS            |
| Anastasiia Ankudinova | Design + Frontend | Collaborating on web design and frontend development, focusing on user experience and interface consistency using Next.js and TailwindCSS |

- **Backend**:
    - **Technologies**: FastAPI, Supabase
    - **Team Members**: Eleonora Pikalo, Mikita Drazdou
    - **Responsibilities**: Eleonora focuses on developing the core backend services and managing database operations. Mikita integrates machine learning models into the backend and ensures the Telegram bot communicates effectively with the backend services.

- **Frontend**:
    - **Technologies**: Next.js, TailwindCSS
    - **Team Members**: Natalia Agapova, Anastasiia Ankudinova
    - **Responsibilities**: Natalia and Anastasiia collaborate on designing and developing the user interface, ensuring a seamless and responsive user experience. They focus on creating a visually appealing and user-friendly frontend.

- **AI and Machine Learning**:
    - **Technologies**: LangChain, Azure OpenAI, Supabase for real-time data, Vercel AI SDK
    - **Team Members**: Sergei Polin, Alexandra Egorova, Mikita Drazdou, Iakov Saparov
    - **Responsibilities**: Sergei oversees the integration of AI into the web application, ensuring all AI components function correctly. Alexandra focuses on business analytics, using data to refine AI algorithms. Mikita works on backend AI integration and Telegram bot functionality, while Iakov develops and optimizes machine learning models.

### **Weekly Progress Report**

This week, we made great progress on our project. We kicked things off with an initial team meeting to outline our project scope and research existing AI solutions in mental health support. To get a better understanding of real-life scenarios and effective interaction techniques, we met with a professional psychologist. We then developed a simple prototype of our chatbot on Telegram, focusing on creating a basic conversational flow and integrating some initial response capabilities.

We also implemented the LangChain API to boost the chatbot's language processing and got it hosted successfully. To help the chatbot maintain context, we set up a system to save users' previous conversations. Finally, we conducted some initial tests with the prototype to pinpoint areas for improvement. All in all, these steps have given us a strong foundation and valuable feedback for moving forward.

### **Challenges & Solutions**

Our processes generally ran smoothly this week, but we encountered a small problem that served as a valuable lesson:

- **New Technologies**: Some team members experienced a learning curve while adapting to new technologies like Next.js and the Vercel AI SDK. To mitigate this, we allocated additional time for training and provided access to online tutorials and documentation. Team members also engaged in peer programming sessions, which helped accelerate the learning process and fostered collaborative problem-solving.

Embracing new technologies can be challenging, but with proper resources and collaborative learning, the team can adapt more quickly and effectively.

### **Conclusions & Next Steps**

This week, we hit all our targets. We studied the market for our product and received valuable advice from a professional psychologist. We also launched our first prototype—a Telegram bot—to test our hypotheses on LLM models and started designing our web application.

Next week, we'll focus on the web application. Our plan is to finish the design and kick off development. We'll also continue testing our ideas on the architecture of LLM agents to refine our approach.
