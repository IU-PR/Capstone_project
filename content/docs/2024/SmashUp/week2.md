# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**



### **Architecture Design**

1. **Component Breakdown**:
- Frontend - user-friendly platform to browse, search and play mash-ups, create and manage playlists, configure settings and use accounts. Interacts with backend server to retrieve content.
- Backend - server that handles user authentication and access limitations, manages database and streams tracks. Communicates with UI and database to manage data storage and retrieval.
- Recommendation system - system of algorithms to recommend content based on user history and preferences.

2. **Data Management**:
- Static content like uploaded mashups is stored as files and streamed by server when need arises.
- User data and data about files are stored using MySQL.

3. **User Interface (UI) Design**:
- https://www.figma.com/design/rRag5NIqwib0N69njQFTbK/SmashUp-2.0?node-id=139-1473&t=RVEeiOwmeob01DIO-0
- Main design principles we had in our mind are consistency, convenience and intuitivity.

4. **Integration and APIs**: As an ability to search for content in database is vital and central for our application, we use Elasticsearch as a search engine. We chose it because it is powerful, non-consuming (for our volumes of data) and easy for integration.

5. **Scalability and Performance**: Right now we are not creating an application for a large number of users, but we keep in mind that the need for scalability might arise during the development process. Changing host or database management system or even breaking backend into microservices are the ways of reasonably easy scaling application for more simultaneous users.

6. **Security and Privacy**: For now passwords are the only private information our application stores, we will use encryption to protect them. While we use Rest API, SSL certificates can be used to encrypt all the queries and responses.

7. **Error Handling and Resilience**: We will use logging in human-comprehensible format for all the exceptions that arise in the application working process, so that user would be able to understand the problem encountered and report it if necessary.

8. **Deployment and DevOps**: We are going to use linters for front-end and SonarQube as static analyser for back-end for every single commit. For robust development workflow, we are going to use pull requests and code reviews, so only correct and good code will be added to the main branch.

### **Week 2 questionnaire:**

1) Tech Stack Resources: None

2) Mentorship Support: None

3) Exploring Alternative Resources:

    For back-end:
* Spring Docs (https://docs.spring.io/spring-framework/reference/index.html)
* MySQL Docs (https://dev.mysql.com/doc/)
* Elastic search Docs (https://www.elastic.co/docs)

    For front-end:
* Typescript Docs (https://www.typescriptlang.org/docs/)
* Next.js Docs (https://nextjs.org/docs)
* Tailwind CSS Docs (https://tailwindcss.com/docs/installation)
* ESLint Docs (https://eslint.org/docs/latest/)
* Prettier Docs (https://prettier.io/docs/en/options.html)
* Husky Docs (https://typicode.github.io/husky/)
* lint-staged Docs (https://github.com/lint-staged/lint-staged)
* Next-intl Docs (https://next-intl-docs.vercel.app/docs/getting-started)
* MDN Web Docs (https://developer.mozilla.org/en-US/)

4) Identifying Knowledge Gaps: we found out two knowledge gaps:
* Some frontenders do not have any experience with TypeScript, and some do not have a lot of experience with React.js
* Lack of expertise in modern approaches for audio content recommendation systems

This defines our lerning objectives for this week.

5) Engaging with the Tech Community: None

6) Learning Objectives: Explore state-of-the art approaches and solutions for music recommendation systems.

7) Sharing Knowledge with Peers: Code reviews with discussions and productional meetings on big tasks are the main ways of knowledge sharing we will use.

8) Leveraging AI: Noneц
### **Tech Stack and Team Allocation**

| Team Member              | Track                                       | Responsibilities                                |
|--------------------------|---------------------------------------------|-------------------------------------------------|
| Leonid Meshcheriakov     | Fullstack, Dev-Ops                          | Backend REST API, frontend scripts, deployment  |
| Sviatoslav Svyatkin      | Frontend                                    | Frontend layout, frontend scripts               |
| Sofia Shulyak            | Frontend, ML                                | Frontent tests and fixes, recommendation system |
| Aleksandr Skvorcov       | Database manager                            | Database schemas and optimization               |
| Artem Matevosian         | Design                                      | Layout design                                   |

### **Weekly Progress Report**

Our team on this week:
* Reviewed and optimized database schemas
* Created environment for the backend deployment
* Deployed current version of the backend
* Setup DNS records for the backend
* Added internationalization in the frontend
* Introduce basic API usage in the frontend


### **Challenges & Solutions**

At this week no one faced with any real challenges in our team, but just few frontenders were having some troubles with learning and understanding TypeScript or React.

### **Conclusions & Next Steps**

Next week frontenders are going to focus on integrating API from the backend and, if they will have time, on introducing tests.

At the backend we need to focus on optimization, including database, and, if there will be enough time, make some preparations to start integration with ElasticSearch.

Also, we are planning to prepare more safety environment for the deployment by using Docker containers and enabling backups.
