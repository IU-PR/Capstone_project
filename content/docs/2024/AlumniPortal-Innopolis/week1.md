---
title: "Week #1"
---

# Week #1

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member              | Telegram ID       | Email Address                     |
|--------------------------|-------------------|-----------------------------------|
| Vasilev Daniil           | @NPggL            | d.vasilev@innopolis.university    |
| Leonov Stepan            | @locturui         | s.leonov@innopolis.university     |
| Volkonitin Artem         | @artem_volkonitin | a.volkonitin@innopolis.university |
| Martynova Julia          | @jmartynova       | j.martynova@innopolis.university  |
| Azarskova Apollinariia   | @Apolline_Az      | a.azarskova@innopolis.university  |
| Zaitseva Ekaterina       | @kkkaterinaaaaaa  | e.zaitseva@innopolis.university   |
| Murtazina Dinara         | @cucumur          | d.murtazina@innopolis.university  |

## Value Proposition

**Identifying the Current Problem:**

Innopolis University alumni and students lack a well-organized platform for interaction and collaboration. This gap hinders alumni engagement in university activities, leading to missed opportunities for mentorship, funding, and job placements for students, as well as a disconnection between alumni and the university community.

**Solution Provided by the Website:**

The proposed solution is a comprehensive alumni portal designed to strengthen connections between the university and its graduates. The portal will enable funding for university and student projects, allow alumni to participate in university events, and provide a platform for students to propose projects and seek mentorship or employment from alumni.

**Benefits to Users:**

*For Alumni:*

- Opportunities to invest in and support promising university projects.
- Engage students for internships or employment within their companies.
- Collaborate with the university to solve existing challenges.
- Participate in university events, such as job fairs, to promote their companies.

*For Students:*

- Access to funding, mentorship, and volunteers for their projects.
- Ability to propose or organize events at the university or partner venues.
- Enhanced job search opportunities through alumni networks.

*For the University:*

- Gain new partners and additional funding.
- Foster collaboration with companies represented by alumni.

**Differentiation:**

No similar platforms currently offer this functionality for Innopolis University. A comparable but less comprehensive platform exists on the MISIS website, lacking the crucial alumni engagement component.

**Impact:**

**Enhanced User Experience:** The platform will provide a centralized and efficient way for alumni to stay involved with the university and for students to access resources and opportunities.

**Increased Collaboration:** Facilitating interactions between alumni, students, and the university will lead to a more connected and supportive community.

**Boosted University Pride:** Strengthening the relationship between alumni and the university fosters a greater sense of belonging and pride.

---

## Lean Startup Methodology

**Problem/Need Addressed:**

The software project addresses the lack of a centralized platform for alumni to engage with Innopolis University, providing a convenient way for alumni to support university projects, participate in events, and offer job opportunities to students.

**Target Users:**

Primary users include Innopolis University alumni, students, and university staff. This encompasses both undergraduate and graduate students seeking mentorship, funding, and job opportunities, as well as alumni who wish to stay connected with the university and contribute to its development.

**Validation and Testing:**

Validation and testing will involve user surveys and interviews with both students and alumni. A pilot version of the platform will be tested with a small group of users to gather feedback. Additionally, analyzing site usage statistics and collecting feedback through forms will help validate our assumptions.

**Metrics for Success:**

- **Number of Active Users:** Tracking the number of registered alumni and students using the platform.
- **Project Submissions:** Monitoring the number of projects submitted and funded.
- **User Engagement:** Measuring participation in events and the number of job postings by alumni.
- **User Satisfaction:** Conducting surveys to gauge satisfaction levels among users.
- **Donations Amount:** Collecting statistics related to alumni donations.

**Iteration and Pivot Strategy:**

Regularly collect user feedback through surveys, interviews, and feedback forms. Analyze this feedback to identify areas for improvement. Update the platform iteratively based on analysis results. Consider a strategic pivot if significant changes are needed, with approval from university administration.

---

## Leveraging AI, Open-Source, and Experts

**AI Integration:**

- **Spam Filtering:** Implement AI algorithms to filter spam and inappropriate content.
- **Recommendation System:** Use AI to recommend relevant projects and events to users based on their interests and activities.

**Open Source:**

Utilize open-source frameworks and libraries for building the platform, ensuring scalability and community support.

**Expert Collaboration:**

Collaborate with university administration, alumni, and industry professionals to guide development and ensure the project meets user needs.

---

## Defining the Vision for Your Project

**Overview:**

Our project aims to create a comprehensive alumni portal for Innopolis University, addressing the need for a stronger connection between alumni, students, and the university. The portal will facilitate funding, mentorship, and job opportunities, enhancing the overall university experience.

**Schematic Drawings:**

The report includes two diagrams to illustrate user interactions and service communications. They can be found at the end of the report.

**Tech Stack:**

- **Front-end:** HTML5, CSS3, JavaScript, Vue 3 (+Pinia)
- **Back-end:** Go (+Redis, GORM), GRPC for microservices interaction
- **Database:** PostgreSQL (+Redis)
- **AI Integration:** Python (+Tensorflow) for implementing recommendation systems and spam filtering
- **Proxy:** Envoy for GRPC integration

The tech stack choices for the project were made based on several factors, including suitability for project requirements and team expertise. Here's a justification for each component of the tech stack:

1. **Front-end (HTML5, CSS3, JavaScript, Vue 3):**
   - **Suitability:** Vue.js is a progressive JavaScript framework known for its simplicity and scalability, making it suitable for building interactive and responsive user interfaces.
   - **Team Expertise:** Two team members have commercial experience programming using Vue 3, making it easier to develop the front-end with this Framework.

2. **Back-end (Go, Redis, GORM):**
   - **Suitability:** Go is known for its high performance, concurrency support, and simplicity, making it suitable for building scalable and efficient back-end services. Redis can be used for caching and fast data retrieval. GORM is the only well-written and fulfilling ORM library for Go that simplifies database interactions.
   - **Team Expertise:** Some team members were learning Go for a short period of time and also have some skills in back-end development. There is also a team lead with commercial experience in writing back-end via Go.

3. **Database (PostgreSQL, Redis):**
   - **Suitability:** PostgreSQL is a powerful, open-source relational database known for its reliability, scalability, and extensibility, making it suitable for storing structured data such as user information and project details. Redis can be used for caching and managing session data.
   - **Team Expertise:** PostgreSQL is a widely used database technology, and the team have experience in working with it (at least via Database course).

4. **AI Integration (Python, TensorFlow):**
   - **Suitability:** Python is widely used for machine learning and AI applications due to its extensive libraries and frameworks, making it suitable for implementing recommendation systems and spam filtering. TensorFlow is a popular deep learning framework that can be used for building and training AI models.
   - **Team Expertise:** Python is a commonly known language, and all team members have an experience in machine learning and TensorFlow (thanks to ML course).

5. **Proxy (Envoy for gRPC integration):**
   - **Suitability:** Envoy is a modern, high-performance proxy that can be used for handling gRPC communication between microservices, making it suitable for building a scalable and efficient microservices architecture.
   - **Team Expertise:** While Envoy may require some learning curve, its use aligns with modern microservices architecture principles, and we will learn and leverage its features for efficient communication between services.

Overall, the chosen tech stack prioritizes scalability, performance, security, and ease of development, considering the project requirements and the team's expertise. Each component is selected to ensure compatibility and efficiency in building a comprehensive alumni portal for Innopolis University.

**Anticipating Future Problems:**

- **Resource Limitations:** Careful planning and task prioritization to manage development resources.
- **External Dependencies:** Have backup options for external services to avoid disruptions.

**Elaborate Explanations:**

Our solution addresses the current disconnection by providing a platform for alumni to engage deeply with the university, offering their expertise and resources. This creates a symbiotic relationship benefiting alumni, students, and the university. Implementing these strategies aims to bridge the gap between alumni and the university, fostering a thriving and collaborative community.

---

## Detailed Functionalities

### 1. User Registration

**Description:** Registration field for new users.

**Functions:**

- **Registration:** User registration via email/Google account with subsequent approval or rejection by the university.
- **For Alumni:** Addition to the alumni database.
- **For University Students/Staff:** After additional approval, adding the name of the student organization/department (DoE, 319, Dorm’s administration, etc).

### 2. Project Proposal Portal

**Description:** Section where users can submit new project ideas.

**Functions:**

- **Project Submission Form:** Fields for project title, description, required resources, estimated budget and timeline, and the name of the alumnus/student organization that owns/co-owns the project.
- **Categories and Tags:** Classification of projects (e.g., infrastructure, events, research) and the addition of relevant tags.
- **File Uploads:** Capability to upload related documents or images with specified size limitations.
- **Alumni Events:** Apply for a venue at the university or its partners for conferences, defenses, or other events.
- **Verification:** If the idea affects the university campus or activities, it undergoes verification by the student community or university administration before publication.

### 3. Project Viewing and Filtering

**Description:** A searchable database of all submitted projects.

**Functions:**

- **Search Bar:** Allows users to search projects by keywords.
- **Filters:** Refine projects by category, status (e.g., open for funding, seeking volunteers), and tags.
- **Sorting Options:** Sort projects by novelty, highest funding, popularity, etc.
- **Prioritization:** Prioritize socially significant or university-conducted projects.

### 4. Project Details Page

**Description:** Detailed view for each project.

**Functions:**

- **Project Overview:** Detailed description, names/contacts/organization of project owners/co-owners, goals, required resources, budget, and timeline.
- **Progress Updates:** Section for the owner/co-owners to post updates.
- **Support:** Ability to express interest in volunteering or funding the project.

### 5. Funding and Donation System

**Description:** System for financial support of projects by alumni.

**Functions:**

- **Donation Portal:** Secure system for making one-time or recurring donations.
- **Funding Progress Indicator:** Visual representation of funding progress toward the goal.
- **Donation History:** For owners/co-owners to track donations (from whom, amount, with an option for full anonymity).
- **Gamification and Ranks:** Implement virtual ranks and achievements based on the amount of funds donated or projects initiated.

### 6. Volunteer Management

**Description:** Tools for managing project volunteers.

**Functions:**

- **Volunteer Registration:** Allows alumni to register their interest in volunteering and the owner/co-owners to accept volunteers.
- **Task Assignment:** Project owners can assign specific tasks to volunteers.
- **Volunteer Profiles:** View profiles of potential volunteers, including their skills and past project experience.

### 7. Notifications and Updates

**Description:** Informs users about project actions.

**Functions:**

- **Email and Telegram Notifications:** Notify users about new projects, updates on projects they are involved in, funding, etc. Notifications can be turned off.
- **Subscriptions:** Allow subscribing to specific types of events (e.g., by tags, organizer) to make notifications more effective and less likely to be ignored.

### 8. Project Management Dashboard

**Description:** Interface for project owners.

**Functions:**

- **Submission Management:** Approving, editing, or deleting project updates (e.g., volunteer commits).
- **Project Status Updates:** Changing the project status (e.g., in progress, completed, need volunteers, seeking funding, etc.).
- **Contribution Monitoring:** Monitoring volunteer registrations and donation history.

### 9. Social Media Integration

**Description:** Connects the platform with a wider network (social media).

**Functions:**

- **Profile Linking:** Alumni can link their profiles with the university alumni database and social networks.
- **Networking Opportunities:** Promotion of events, mentoring programs, and meetings related to project interests.

### 10. Analytics and Reports

**Description:** Provides information and data for project owners and platform administrators.

**Functions:**

- **Project Analytics:** Viewing metrics such as page views, donation amounts, number of volunteers, engagement levels, etc.
- **User Analytics:** Tracking user activity and engagement on the platform.

### 11. Community Interaction Features

**Description:** Enhances user interaction and community building.

**Functions:**

- **Discussion Channels:** Special, automatically generated Telegram channels for discussing specific ideas, projects, and collaboration opportunities.
- **Success Stories:** Showcasing completed projects and their creation stories.

### 12. Additional Features

**Description:** Additional functionalities that can be tied to various service features.

**Functions:**

- **Temporary Pass Requests:** Separate microservice for requesting temporary passes for alumni.
- **Temporary Housing Requests:** Separate microservice for requesting temporary housing for alumni attending events.
- **Student Hiring:** Microservice for posting job offers from alumni/portfolio of student applicants needing internships.
- **Consult & CustDev:** Students can contact successful alumni to propose collaboration, request consultation, or conduct customer development.

## Useful Diagrams
### Communication Diagram (made like sequence diagram)
{{<mermaid>}}
sequenceDiagram
    participant User as User
    participant Frontend as Frontend
    participant Backend as Backend
    participant Database as Database
    participant AIService as AI Service
    participant Proxy as Proxy (Envoy)

    User->>Frontend: Interacts with UI
    Frontend->>Backend: Sends HTTP requests
    Backend->>Database: Reads/writes data
    Backend->>AIService: Requests AI functionality
    Backend->>Proxy: Sends requests via gRPC
    Proxy-->>Backend: Handles incoming requests
    Backend-->>Frontend: Sends data/response
    Backend->>AIService: Utilizes AI features
    AIService-->>Backend: Provides AI results
    Backend-->>Frontend: Returns AI results
{{</mermaid>}}
### Functionality Diagram (still in progress)
{{<mermaid>}}
graph TD
    subgraph "User"
        N[Student] --> |Register| B[User Registration]
        B --> |Post the request| H[Registration Approval]
        N --> |Submit Projects| C[Project Proposal Service]
        C --> |Post the request| I[Project Submission Approval]
        N --> |View Projects| D[Project Viewing and Filtering]
        N --> |View Details| E[Project Details Page]
        N --> |Submit Portfolio| F[Student Hiring Service]
        N --> |See Offers| F[Student Hiring Service]
        N --> |Request consultation or CustDev Interview| G[Consult & CustDev Service]
    end
{{</mermaid>}}
{{<mermaid>}}
graph TD
   subgraph "University Admin"
            U[Admin] --> |Approve or Decline request| H2[Registration Approval Service]
            U --> |Approve or Decline request| I2[Project Submission Approval Service]
            U --> |Approve or Decline request| A2[Additional Feature Services]
            U --> |Change the project status| B[Project Status Management]
            U --> |Watch donation and volunteer registartion history| C[Contribution Monitoring]
            U --> |View metrics| D[Analytics and Reports]
      end
{{</mermaid>}}
{{<mermaid>}}
graph TD
   subgraph "Alumni"
            A[Alumni] --> |Register| B[User Registration]
            B --> |Post the request| C[Registration Approval]
            A --> |Submit Project| D[Project Proposal Service]
            D --> |Post the request| I[Project Submission Approval]
            A --> |Watch donation history| F[Contribution Monitoring]
            A --> |Submit Job Offer| F2[Student Hiring Service]
            A --> |Make donation to support projects| G[Funding and Donation]
            A --> |Register in volunteering, assignments, view volunteer profiles.| Z[Volunteer Management]
      end
{{</mermaid>}}