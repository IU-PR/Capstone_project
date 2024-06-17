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
    - **LLM Microservice**: Using Azure AI to power our large language model, bringing advanced AI capabilities to our app.
    - **Backend**: Built with FastAPI for smooth and efficient operations.
    - **Web App**: Using Next.js with the Vercel AI SDK to seamlessly integrate AI features.
    - **Database**: Managed with Supabase for reliable and real-time data access.

2. **Data Management**:
    For real-time data access, we use the Supabase SDK to connect to our Postgres database. On the frontend, we use localStorage to temporarily store user data, keeping everything quick and responsive. We also leverage the Vercel AI SDK to stream data from our language models, ensuring our AI features are always up-to-date and running smoothly.

3. **User Interface (UI) Design**:
    In our project, we have two pages:
    - **Main Page**:
        - **Purpose**: Greet the user, assist them, and direct them to the relevant area.
        - **Design**:
            - **Background**: Soft, calming colors, such as light shades of blue or green.
            - **Header**: "Welcome! How can we help you today?".
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
    By using a serverless platform with built-in autoscaling, our system can automatically adjust to the demand, ensuring everything runs smoothly even during peak times. This setup means we don’t have to worry about managing servers, and our users always get a fast and responsive experience, no matter how many people are using the app.

6. **Security and Privacy**:
    On the frontend, we use middleware to keep things secure. On the backend, we use token-based authentication to ensure only authorized users can access our services. We've also implemented Google authentication for app access, adding an extra layer of protection. Additionally, connections to our microservices are restricted by IP address to further enhance security.

7. **Error Handling and Resilience**:
    We’ve built our architecture using some of the most reliable platforms out there, ensuring we get top-notch uptime and resilience. If something does go wrong, our user interface is designed to keep users in the loop with clear, helpful error messages.

    Our use of a microservice architecture really shines here. Each part of our system works independently, so if one piece encounters an issue, it doesn’t bring everything else down with it. This setup not only helps us fix problems faster but also keeps the overall system running smoothly and reliably.

8. **Deployment and DevOps**:
    During our development and testing phases, we're using free platform plans (Supabase, Vercel, Azure) that handle automatic deployment for us. This setup means we don't need any specialized DevOps skills to get our solutions up and running. It allows us to focus more on building and refining our product, rather than worrying about the deployment process. Most of these instruments have an automatic CI/CD pipeline.

### **Week 2 Questionnaire:**

1. **Tech Stack Resources**:
    FastAPI, Next.js, Supabase, TailwindCSS, and the Vercel AI SDK all come with solid documentation and active communities. There are plenty of training materials to help our team stay up to date.

    Everything integrates smoothly, making our workflow efficient. We follow best practices to ensure our app is fast, scalable, and secure.

2. **Mentorship Support**:
    This week, we conducted a meeting with Eleonora Ilina, a psychologist at IU, to discuss the process of emergency and crisis intervention. During the session, we identified several key points relevant to our project:
    - **Neuro-linguistic Programming (NLP)**: It was noted that neuro-linguistic programming could be highly beneficial for our project. NLP involves the analysis of human language patterns, which aligns well with our project's objectives.
    - **Emergency and Crisis Intervention**: For a project of this nature, it is feasible to incorporate a format of emergency assistance during crisis situations. This approach ensures that individuals can quickly find external support to address and resolve their issues effectively.
    - **Voice Communication**: It was determined that voice messages would be more effective than text-based communication. This method allows clients to express their thoughts more easily and clearly.

3. **Exploring Alternative Resources**:
    After analyzing the market, we identified four main competitors for our service:
    - **Psychological Emergency Lines**: These can be helpful but have their drawbacks. Speaking with a real person can be difficult and overwhelming during panic or anxiety attacks. Additionally, there is no information about the qualifications of the person on the other end, which raises concerns about their competence to provide advice to mentally unstable users.

    - **Real Psychologists (In-Person and Online)**: While this is the safest option, it involves live communication, which can be daunting for some. Scheduling a session with a real psychologist usually requires booking in advance and waiting several days, which can be critical in urgent situations. Moreover, therapy sessions are often expensive, making them inaccessible to many people.

    - **Self-Help Methods**: This includes journaling and reaching out to friends and family. While this can be helpful, some people may not trust themselves or those around them enough to effectively analyze and share their feelings. Even when they do share, they might not receive the needed help, as neither they nor their close ones are professionally trained to handle such situations.

    - **Other AI Psychologist Services**: We found several competitors, like FlowGPT and Character.AI. These services are not free and tend to be quite expensive. Additionally, their websites often don’t function properly and are not designed to cater to individuals in a mental health emergency.

4. **Identifying Knowledge Gaps**:
    - **Lack of Psychologists on Team**: We currently do not have a psychologist on our team, which creates a gap in professional psychological expertise. To address this, we will seek external consultations with licensed psychologists to ensure the therapeutic methods used by our AI are effective and ethical. Additionally, we will conduct thorough research on psychological practices and integrate validated information into our project.
    - **Inexperienced Backend Developer**: One of our backend developers is in the process of gaining experience, which presents an opportunity for growth within our team. To support this, we will provide targeted training through online courses and resources. Furthermore, experienced team members will offer mentorship and support to ensure the developer acquires the required skills and can effectively contribute to the project.
    - **Learning New Technology for Frontend Developer**: One of our frontend developers will be working with a new technology, Next.js, which requires additional learning and adaptation. To facilitate this transition, we will allocate time for the developer to engage in comprehensive learning through online tutorials, documentation, and courses. Additionally, another team member who is already familiar with Next.js will provide guidance and support, ensuring a smooth learning curve and successful integration of the new technology into our project.

5. **Engaging with the Tech Community**: 
    Ever since large language models came onto the scene, people have been excited about using them as personal psychologists. This week, we looked into how machine learning engineers and regular users are training these neural networks for AI psychology and the challenges they face.

    The main problems users encounter when training their AI psychologists are:
    - **Ambiguity in User Requests**: Users often find it hard to clearly express what they need, leading to confusion and misinterpretation by the AI. This means the responses might not really address what the user is concerned about.
    - **Contextual Understanding**: AI systems often struggle to fully understand the context behind user requests. This can lead to responses that aren’t relevant or empathetic, especially with complex or nuanced issues.

    From our exploration, we learned that to overcome these challenges, it's crucial to develop AI systems that can effectively understand user intent and respond in a way that’s both accurate and empathetic.

6. **Learning Objectives**:
    -

 Gain a fundamental understanding of psychological first aid.
    - Develop skills in designing conversational agents to match the task.
    - Get practical experience in developing and integrating models with user-facing applications.
    - Learn how to manage user data to provide personalized support.

7. **Sharing Knowledge with Peers**:
    - **Mentorship for Inexperienced Backend Developer**: One of our backend developers is new to the field, but we are fortunate to have a more experienced team member who will provide mentorship and guidance. This experienced developer will help the newcomer with adaptation, ensuring they gain the necessary skills and confidence to contribute effectively to the project. Through regular collaboration and knowledge sharing, we aim to foster a supportive learning environment that benefits the entire team.
    - **Support for Frontend Developer Learning Next.js**: Although one of our frontend developers has substantial experience in frontend development, they are unfamiliar with Next.js. To assist with this transition, a more experienced team member who is proficient in Next.js will provide the necessary support and guidance. This one-on-one mentorship will help the developer adapt quickly and effectively, ensuring a smooth integration of Next.js into our project while enhancing the overall skill set of our team.

8. **Leveraging AI**: 
    To create an effective psychological first aid agent, we plan to start with a LangChain system prompt to guide the chatbot's interaction. Then, by using cookies, we will save conversation histories and ensure that the chatbot can remember past interactions with the user and provide direct support. After testing that prototype, we will transition to a fully functional LangChain LLM agent specifically designed to handle psychological first aid tasks.

### **Tech Stack and Team Allocation**

| Team Member              | Track                                       | Responsibilities   |
|--------------------------|---------------------------------------------|--------------------|
| Sergei Polin (Lead)     | Fullstack | Web + AI |
| Eleonora Pikalo            | Backend | Backend |
| Alexandra Egorova            | Business analytics | AI |
| Mikita Drazdou            | Backend + ML | AI + Telegram |
| Iakov Saparov            | ML | AI |
| Natalia Agapova | Design + Frontend | Web |
| Anastasiia Ankudinova | Design + Frontend | Web |

### **Weekly Progress Report**

This week, we made great progress on our project. We kicked things off with an initial team meeting to outline our project scope and research existing AI solutions in mental health support. To get a better understanding of real-life scenarios and effective interaction techniques, we met with a professional psychologist. We then developed a simple prototype of our chatbot on Telegram, focusing on creating a basic conversational flow and integrating some initial response capabilities.

We also implemented the LangChain API to boost the chatbot's language processing and got it hosted successfully. To help the chatbot maintain context, we set up a system to save users' previous conversations. Finally, we conducted some initial tests with the prototype to pinpoint areas for improvement. All in all, these steps have given us a strong foundation and valuable feedback for moving forward.

### **Challenges & Solutions**

This week, all the processes went smoothly with no significant problems.

### **Conclusions & Next Steps**

This week, we hit all our targets. We studied the market for our product and received valuable advice from a professional psychologist. We also launched our first prototype—a Telegram bot—to test our hypotheses on LLM models and started designing our web application.

Next week, we'll focus on the web application. Our plan is to finish the design and kick off development. We'll also continue testing our ideas on the architecture of LLM agents to refine our approach.