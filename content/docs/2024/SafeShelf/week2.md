# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

This week, we focused on selecting the appropriate technologies for our project, SafeShelf. After thorough consideration and discussions, we decided to use Kotlin for our backend development due to its modern language features, strong performance, and seamless integration with Java libraries. We chose Spring Boot as our primary framework to leverage its powerful, easy-to-use features for building robust and scalable web applications. For our database management, PostgreSQL was selected due to its advanced features, reliability, and strong support for complex queries and transactions. Additionally, we are exploring the integration of the ФНС API (or similar) to retrieve product information from QR codes on receipts. This combination of technologies ensures that our application will be scalable, maintainable, and efficient, meeting both current and future needs.


### **Architecture Design**

1. **Component Breakdown**: Identified the major components of SafeShelf, including backend services, data storage, machine learning modules, and the user interface. Each component's responsibilities and interactions were outlined to ensure a cohesive structure.
   - **User Interface (UI)**: 
     - Frontend: Built using React and TypeScript, ensuring a responsive and interactive user experience.
     - Components: Login menu, settings window, and chat log for minimal manual interaction.
   - **Backend Services**:
     - API Management: Developed with Kotlin and Spring Boot, handling requests and managing data.
     - Database: PostgreSQL for storing user data, including inventory and meal plans.
     - Deployment: Docker for containerization, GitHub Actions for CI/CD.
   - **Machine Learning**:
     - Recipe Generation: Using AI to generate personalized meal plans based on available ingredients.
     - Optimization: Evolutionary algorithms to optimize meal plans for expiration dates and nutritional balance.

2. **Data Management**: 
   - Short-Term Storage: Utilizing PostgreSQL for temporary storage of user data and meal plans.
   - Caching: Implementing caching mechanisms to enhance performance and reduce database load.
   - Privacy: Ensuring that sensitive user data, such as inventory and meal plans, is securely handled and not stored longer than necessary.

3. **User Interface (UI) Design**: 
   - Considered user experience and design principles. Created initial wireframes and mockups using Figma to visualize the layout and flow of the application.

4. **Integration and APIs**: 
   - Assessed the availability of APIs for retrieving product information from QR codes. Currently exploring the ФНС API and other potential alternatives for seamless integration.

5. **Scalability and Performance**: 
   - Server Scalability: Additional server instances for handling peak loads can be spun up on demand.
   - Performance Optimization: Regular profiling and optimization of AI models and backend services to ensure efficient performance.

6. **Security and Privacy**: 
   - User Data Protection: Storing minimal user data and implementing strong encryption for sensitive information.

7. **Error Handling and Resilience**: 
   - Error Logging: Implementing comprehensive error logging on the server for manual inspection and troubleshooting.
   - Automatic Recovery: Ensuring that the system can gracefully recover from failures and maintain functionality.

8. **Deployment and DevOps**: 
   - Deployment Strategy: Using Docker for containerization and GitHub Actions for automated deployment.
   - Continuous Integration/Continuous Deployment (CI/CD): Ensuring frequent and reliable updates to the application with minimal downtime.

### **Week 2 Questionnaire:**

1) **Tech Stack Resources**: 
   - Utilized project-based book like "Spring in Action" to enhance our knowledge. These resources provided in-depth insights into Kotlin and Spring, essential for our backend development.

2) **Mentorship Support**: 
   - Our mentor, Danila Korneenko from Innopolis University, has been actively involved, offering valuable guidance and helping us navigate challenges in our project.

3) **Exploring Alternative Resources**: 
   - In addition to book, we explored online courses on platforms like Coursera and Udemy, video tutorials on YouTube, and official documentation for Kotlin and Spring to fill knowledge gaps.

4) **Identifying Knowledge Gaps**: 
   - We identified gaps in our understanding of API integration and advanced Kotlin features. We plan to address these by conducting focused study sessions and leveraging our mentor's expertise.

5) **Engaging with the Tech Community**: 
   - Engaged with the broader tech community through online forums, Telegram groups, and local meetups to seek guidance and learn from experienced professionals.

6) **Learning Objectives**: 
   - This week, our learning objectives included mastering Kotlin for backend development, understanding API integration, and designing robust architecture. We employed hands-on coding sessions and peer discussions to achieve these goals.

7) **Sharing Knowledge with Peers**: 
   - Organized knowledge-sharing sessions and discussions to facilitate the exchange of insights and experiences related to our tech stack.

8) **Leveraging AI**: 
   - Used AI-powered tools and platforms, such as GitHub Copilot and ChatGPT, to expedite the process of acquiring knowledge and solving technical challenges.

### **Tech Stack and Team Allocation**

| Team Member              | Track          | Responsibilities                                             |
|--------------------------|----------------|----------------------------------------------------------------------|
| Nikolai Kuzmin (Lead)    | Backend        | Working on additional backend functionalities                        |
| Andrey Alexeev           | Backend        | Finding API for getting info about products from QR codes on receipts|
| Emil Davlityarov         | Backend        | Assisting in backend development and API integration                 |
| Arsenii Belugin          | ML             | Developing machine learning models for data analysis                 |
| Alyona Sinyagina         | ML             | Supporting ML model development and integration                      |

### **Weekly Progress Report**

Our team researched the availability of APIs for retrieving product information from QR codes. We started writing the Spring Kotlin application and discussed and approved the design for our application (link to Figma: [link](https://www.figma.com/design/iq9CZe5zonFNUGu1TBoIxf/SafeShelf?node-id=0-1)). The ML team explored useful resources and techniques for implementing machine learning models in our project.

### **Challenges & Solutions**

We faced challenges in selecting the most suitable API for our needs. To overcome this, we conducted thorough research and consulted with our mentor to identify the best options. Additionally, we encountered difficulties in understanding advanced Kotlin features, which we addressed through focused study sessions and peer learning.

### **Conclusions & Next Steps**

In conclusion, we made significant progress in choosing our tech stack and designing the architecture. Next steps include finalizing the API selection, continuing the development of the Spring Kotlin application, and beginning the implementation of machine learning models. We will also continue to engage with our mentor and the tech community to refine our approach and address any emerging challenges.
