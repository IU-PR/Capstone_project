---
title: "Week #3"
---

# **Week #3**

## **Developing the first prototype, creating the priority list**

- **Technical Infrastructure**: 

The development team has successfully set up all the necessary technical infrastructure for the A-Level exam preparation web service project. We have established a robust GitHub repository, accessible to both team members and course instructors, which organizes our work into several focused directories:
  - `app_client`: Manages front-end development and user interface design.
  - `app_model`: Hosts the machine learning models that classify exam questions into specific topics.
  - `app_server`: Handles all back-end functionalities.
  - `data`: Contains the datasets utilized for training our machine learning models.
  - `notebooks`: Provides a space for conducting and sharing machine learning experiments.
  - Additional repository components include `README.md` and `docker-compose.yml`, which facilitate the setup of a consistent development environment using Docker.

  To accommodate various aspects of our project, we have structured our development process around multiple branches, namely:
  - `backend`
  - `data_parsing`
  - `dataset_reading_improvement`
  - `frontend`
  - `ml_experiments`
  - `pdf_parsing`

  Currently, the machine learning tasks are being executed using personal GPUs by team members. This approach has proven effective for our present needs and allows flexibility in development, but later on we plan to rent the computing resources from internal/external sources.

  Furthermore, we have conducted a comprehensive meeting to ensure all team members are fully aware of their tasks and the overall project vision. This meeting has helped ensure that every member can efficiently utilize the development infrastructure and contribute effectively to the project.

- **Backend Development**:

The progress has been made in the backend development of our A-Level exam preparation web service. Key advancements include:

  - **Enhanced Question Parsing**: The question parsing mechanism has been refined and now performs as expected. This improvement is crucial for accurately interpreting and categorizing the questions submitted by users.

  - **Unit Testing**: Comprehensive unit tests have been developed to ensure the stability and reliability of our backend functionalities. These tests cover:
    - General backend logic.
    - API connectivity with the machine learning model, ensuring that the integration is seamless and functions correctly under various scenarios.

These developments are pivotal in building a robust backend that supports efficient data management and user interaction. Our focus remains on enhancing the core functionalities to support the primary user interactions more effectively. The back-end has been developed in a way that integrates with Docker for scalability.

- **Frontend Development**:
- **Frontend Development**: Our team has made substantial progress in the frontend development of our A-Level exam preparation web service. Below are the key milestones we've achieved:

  - **Figma Prototype Completion**: We have fully developed the Figma prototype for the project, which serves as a detailed visual blueprint. This prototype includes all main components necessary for the MVP and adheres to the wireframes designed earlier. 
  
  - **Implementation Using React and Next.js**: Transitioning from prototype to production, we have begun to implement the design in code using React and Next.js frameworks. So far, we have successfully coded two main pages of the website. These pages are foundational to our application, enabling primary user interactions as outlined in our MVP. 

This phase of development focuses on ensuring that the user interface is not only intuitive and user-friendly but also aligns perfectly with the planned functionality of our service. While prioritizing functionality, we are also mindful of the aesthetic aspects to ensure a pleasant user experience.

- **Data Management**:

Our team has taken careful steps to establish a foundational data management system for the A-Level exam preparation web service. Here are the key aspects of our current setup:

  - **Data Folder Structure**: We have organized a `data` directory within our project repository. This directory is crucial as it stores all essential data needed for the machine learning model, including PDF files and other relevant datasets. This structured approach ensures that all necessary data is accessible and well-managed.

  - **Database Preparation**: While real user data storage requirements are anticipated in future development phases, we have already started preparing a placeholder for the database. This preparation includes setting up basic database functionalities that will allow us to handle and manage user data once backend requests for data storage begin.

  - **Future Planning**: Our current focus is on ensuring that our data management capabilities are robust enough to handle initial MVP features without complexity. As user interaction increases and data storage needs become more apparent, our system is designed to scale and incorporate more comprehensive data handling and storage functionalities.

This setup meets the current needs of our project and also lays the groundwork for future expansions in data management as user engagement and feature sets grow.

- **Prototype Testing**:

Initial testing phases for our A-Level exam preparation web service have been conducted, focusing on the functionalities that have been implemented so far. Here are the key points regarding the testing process:

  - **Current Testing Status**: The team has successfully developed and executed unit tests for the available backend functionalities. These tests are crucial for ensuring that the core logic and data interactions perform as expected.

  - **Frontend Development Alignment**: As the frontend development is still in progress with React and Next.js, not all functionalities have been fully implemented and thus could not be included in this round of testing. The completion of frontend features will enable additional and more comprehensive testing phases.

  - **Future Testing Plans**: Further testing is scheduled to follow the completion of the frontend coding. This will allow us to conduct thorough tests across the entire application, aligning with defined user flows and scenarios to identify any usability issues or bugs.

  - **Feedback Collection**: Feedback from team members has been and will continue to be a vital component of our testing phases. This feedback is instrumental in making necessary refinifications and enhancing the overall user experience.

Our approach ensures that testing keeps pace with development, allowing for the timely identification and resolution of any issues, thus maintaining the quality and reliability of the prototype.

## Weekly Progress Report

### Overview
This week, our team has made significant strides across various aspects of the A-Level exam preparation web service project. Here are the key developments:

### Technical Infrastructure
- A robust GitHub repository has been set up and organized into multiple directories to facilitate efficient collaboration and development.
- Multiple development branches have been established to handle different components of the project such as backend logic, data parsing, and frontend development.

### Backend Development
- We enhanced the question parsing mechanism, improving its performance to meet our expectations.
- Comprehensive unit tests have been developed, including tests for the API connectivity with the machine learning model.

### Machine Learning Model Development
- Several baseline machine learning models have been developed:
  - **Multinomial Naive Bayes** achieving 78% F1 score.
  - **Word2Vec tokenization with Support Vector Machine (SVM)** classifier achieving 66% F1 score.
  - **Fast Roberta tokenization** with the DistilRoberta model achieving 87% accuracy.
  - **Yandex GPT API** based solution achieving 51% accuracy.
- Exploratory data analysis was conducted, revealing significant patterns in the data related to the topics of the questions. This analysis is crucial for refining our model development.

  <p align="center">
    <img src="/2024/A-Level/word_clouds.png" alt="Word Cloud" style="width: 40%;"/>
    <img src="/2024/A-Level/historgams_of_frequency.png" alt="Histograms of Word Frequency" style="width: 40%;"/>
  </p>

### Frontend Development
- The Figma prototype for the project has been completed, serving as a guide for the frontend development using React and Next.js.
- Implementation of the prototype into code has begun, with two main website pages developed so far.

    ![Figma Prototype](/2024/A-Level/figma1.png "Figma Prototype 1")
    ![Figma Prototype](/2024/A-Level/figma2.png "Figma Prototype 2")
    ![Figma Prototype](/2024/A-Level/figma3.png "Figma Prototype 3")
    ![Figma Prototype](/2024/A-Level/figma4.png "Figma Prototype 3")
    ![Figma Prototype](/2024/A-Level/figma5.png "Figma Prototype 4")
    ![Figma Prototype](/2024/A-Level/figma6.png "Figma Prototype 5")
    ![Figma Prototype](/2024/A-Level/figma7.png "Figma Prototype 6")

### Prototype Testing
- Initial rounds of unit testing have been conducted, with further comprehensive testing planned following the completion of frontend development.
- Feedback from team members is being actively collected to refine and enhance user experience.

### **Challenges & Solutions**

This week, our development process faced several challenges across different areas of the project. Here's how we addressed each issue:

#### Computing Power for Machine Learning Models
- **Challenge**: Our team encountered significant limitations in computing power, which hindered our ability to experiment with multiple layers of LSTMs before feeding the output to the transformer model. The lack of memory and computing resources restricted our testing capabilities.
- **Solution**: We are exploring options to rent additional computing power from the university or other organizations. This approach will provide the necessary resources to expand our model's complexity and improve its performance.

#### Frontend Development Learning Curve
- **Challenge**: Frontend development pace was impacted by the steep learning curve associated with the React and Next.js technologies we are employing.
- **Solution**: To overcome this, the team has adopted a hands-on approach, diving deeper into practical applications of these technologies to accelerate our learning and proficiency, thus speeding up the development process.

#### Backend Integration with Docker
- **Challenge**: Integrating the backend with Docker from the outset posed difficulties, particularly in conducting unit testing efficiently.
- **Solution**: We are considering the adoption of Hydra and utilizing YAML configurations to streamline the development and testing process, making it more flexible and less dependent on Docker's constraints.

#### Insufficient Data for Training ML Models
- **Challenge**: The machine learning aspect of the project suffered from a scarcity of training data, which could potentially affect the model's accuracy and reliability.
- **Solution**: We have opted to implement data augmentation techniques to artificially expand our dataset, thereby enhancing the robustness and performance of our machine learning models.

### **Conclusions & Next Steps**

As our project progresses, we have outlined a clear path forward to enhance the functionality and robustness of our A-Level exam preparation web service. Here are our immediate priorities and the planned focus for the upcoming weeks:

#### Priority List of Features:
1. **Completion of Frontend Development**: Ensure that all user interface components are fully developed and integrated, providing a seamless and engaging user experience.

2. **Advanced Machine Learning Models**: Develop more complex, state-of-the-art machine learning models to improve the accuracy and efficiency of our question classification and user interaction.

3. **Backend Enhancements**:
    - **Unit and User Tests**: Conduct comprehensive testing to ensure the backend is robust, reliable, and secure.
    - **Completion of API**: Finalize all API endpoints to ensure smooth data flow between the frontend, backend, and database systems.

4. **Database Integration**: Fully integrate and optimize the database to support all data management requirements, ensuring fast, efficient, and secure data transactions.

#### Expected Advancements:
- In the next four weeks, we aim to finalize the frontend and enhance our backend capabilities. This includes completing all API integrations and ensuring the database supports the dynamic needs of our platform.
- Subsequent phases will focus on refining our machine learning models and expanding our testing to include real-user environments, which will help us fine-tune the system before a broader release.

### Conclusion
Our team remains dedicated to delivering a high-quality educational tool that meets the needs of A-Level students and educators. By focusing on cutting-edge technology and user-centered design, we are poised to provide a platform that not only aids in exam preparation but also enhances the learning experience. As we move forward, we will continue to iterate based on feedback and testing results, ensuring our service evolves to meet user demands and educational standards.