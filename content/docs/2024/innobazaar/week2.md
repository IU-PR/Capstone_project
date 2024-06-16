### Week #2
#### Week 2 - Choosing the Tech Stack, Designing the Architecture

**Tech Stack Selection**
- After evaluating various options, we've chosen the following technologies for our project:
  - **Frontend:** React.js for dynamic and responsive user interface.
  - **Backend:** Python Django for server-side logic.
  - **Database:** We decided to use default Django database which uses SQLite.

**Architecture Design**
1. **Component Breakdown**:
  - **Frontend** - provides interactive pages for users to view and interact with product listings, wishlist items etc. It manages navigation, form submissions, and other user actions. 

  - **Backend** - Handles user authentication, and manages product inventory. Also it provides data to the frontend and handles incoming requests.
    
  - **Database** - Manages all persistent data such as vendor information, product details, vendor contacts etc.
2. **Data Management**:
  - All data will be stored using SQLite which is the default for the django. Moreover, Django uses Object-Relational Model(ORM) which allows to work with databases using python code instead of SQL. The following database schema is used in the current version of the project:
    ![db_schema](/static/2024/innobazaar/week2_1.png)
3. **User Interface (UI) Design**:
  - Built with React.js, it offers an interface for users to navigate and interact with the system. The interactive protoype with some functionality of the website can be found [here](https://www.figma.com/proto/OqYWcu5new2YzWO7XfQE2I/capstone-project?node-id=1-2200&t=C79svI9vX0ffFJWD-0&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=1%3A2200). Preview of the prototype:
    ![figma_preview](/static/2024/innobazaar/week2_2.png)
4. **Integration and APIs**:
  - For now, we are not planning to use any external API's or integrations. The only API's we are using are the ones provided by our own backend. Our backend service provides API's which are later used by the frontend side to list products, or retrieve an item info. Moreover, we are planning to implement authorization system.
5. **Scalability and Performance**:
  - For the current version, we are assuming that only one user will use the system, but for the future, we are planning to make it asyncronous.
6. **Security and Privacy**:
  - Django framework already has built-in protection against most types of attacks. Also, Django provides an option of having a superuser in the project, meaning you can restrict access.
7. **Error Handling and Resilience**:
  - In our project, error handling mechanisms are implemented to provide meaningful feedback to users in case of unexpected scenarios, for example when someone is trying to access nonexisting item. Also, we are planning to add a logging mechanism to diagnose issues quickly.
8. **Deployment and DevOps**:
  - We are planning to use docker-compose to ensure consistency and reliablity accross different environemnts. For now it is planned to be consisting of 2 services - frontend and backend. If there will be time left, we are planning to migrate to PosgreSQL to optimize our queries.

#### Week 2 Questionnaire:
- **Tech Stack Resources**:
  - Our team prefers online courses/tutorials rather than books.
- **Mentorship Support**:
  - Currently we do not have any mentor involved in our project. 
- **Exploring Alternative Resources**:
  - Django documentation - it provides very useful guides and tutorials.
  - Youtube - huge amounts of tutorials on what we need.
  - Blogposts - blogs of people creating simple projects using the same or similar stack as we do.
  - LLM's - ChatGPT or Gemini are good at explaining library documentation, so if someting is not clear, LLM's can help you to get better insights.
- **Identifying Knowledge Gaps**:
  - Django - we are not experienced enough to utilize the advanced features of this framework. We will need some time to deepen our understanding about.
  - Frontend to Backend communication - out teams lacks experience in establishing efficient communication between frontend and backend. To overcome this we will explore best practices for designing APIs using Django. and  improve our knowledge of integrating frontend frameworks like React.js with Django.
- **Engaging with the Tech Community**:
  - We have not yet engaged with a tech community or tech forum. But if necessary, we can always ask questions in online forums like stackoverflow, quora, reddit.
- **Learning Objectives**:
  - Become proficient in Django, focus on mastering its capabilities for efficient data management, robust API development, and secure backend operations.
  - Enhance ability to integrate React.js with Django seamlessly. This involves improving skills in handling data synchronization and ensuring smooth communication between frontend and backend components.
  - Improving frontend development skills, including proficiency in React.js, to be able to develop robust frontend components.
- **Sharing Knowledge with Peers**:
  - We have a telegram group chat, to where we also send the links with materials which we think can help us with the project. 
- **Leveraging AI**:
  - We use ChatGPT and Gemini to quickly access the documentations, and to write repetitive code.

#### Tech Stack and Team Allocation
Because many of our members are backend developers, we have thought of an idea to distribute endpoints between them, meaning everyone gets to write a code for 1-2 endpoints.

| Team Member         | Track                       | Responsibilities                                       |
|---------------------|-----------------------------|--------------------------------------------------------|
| Azizullo Sadriddinzoda (Lead)| Design, Backend | UI/UX design, API development, Reports |
| Habibullo Assoev | Design, Backend | UI/UX design, API development |
| Askar Akhmetkhanov | Frontend | Develop frontend part of the website |
| Aleksei Kureikin | Backend, Testing | Testing, API development |
| Kamil Mirgasimov | Frontend | Develop frontend part of the website |
| Muhibullo Khujabekov | Backend, Testing | Testing, API development |
| Yoqub Davlatov | Backend | Architect API design, API development |

#### Weekly Progress Report
- **Our team did**:
  - Finalized the tech stack.
  - Designed the initial architecture.
  - Created a responsive prototype.
  - Created an API to retrieve list of products, to which filters(category, sort by, min/max price) can be applied.
  - Created and API to retrieve info about a specific product.

#### Challenges & Solutions
- **Challenge**: Ensuring correct communation between frontend and backend.
  - **Solution**: At first we had errors when we tried to map API response in React.js, but we were able to solve it by adding extra if statement, which check whether the response is undefined or no.
- **Challenge**: Having clean directory structure.
  - **Solution**: We adopted a well-defined directory structure based on best practices, categorizing all components into clear sections:
  ![dir_structure](/static/2024/innobazaar/week2_3.png)

#### Conclusions & Next Steps
- We were able to successfully implement several backend endpoints, which we think were the most complex ones in the project. Now we will focus on how to correctly utilize them in the frontend part of the website. Moreover, if everything goes smoothly we will think of a new features which could potentially be added to the website.