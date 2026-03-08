---
title: "Week #2"
---

# Week #2

## Detailed Requirements Elaboration

### Detailed User Stories for MVP

Based on the high-level user stories from Week 1 and aligned with our microservices architecture, we have expanded them into detailed, actionable user stories:

#### **Authentication and User Management (Auth Service + Users Service)**

- **User 01**: As a new user, I want to register into platform so that I can securely access the all the materials
  - *Acceptance Criteria*: Auth Service validates credentials, generates JWT tokens, API Gateway validates tokens for all requests
  - *Technical Implementation*: Auth Service handles registration/login, Users Service stores profile data
  - *Priority*: High

- **User 02**: As a user, I want to manage my profile (for e.g. credentials) through the Users Service so that I can update my information and maintain accurate account details
  - *Acceptance Criteria*: CRUD operations for user profiles, data persistence in Users DB
  - *Technical Implementation*: Frontend → API Gateway → Users Service → Users DB
  - *Priority*: High

- **User 03**: As a user, I want my authentication state to persist across all services so that I don't need to re-login when accessing different modules
  - *Acceptance Criteria*: JWT tokens validated by API Gateway, user context passed to microservices via gRPC
  - *Technical Implementation*: API Gateway middleware validates JWT, passes user ID to services
  - *Priority*: High

#### **Labs Management (Labs Service + File Storage)**

- **User 04**: As a student, I want to browse and search available labs through the Labs Service so that I can find relevant assignments
  - *Acceptance Criteria*: Labs Service provides REST API for lab listing
  - *Technical Implementation*: Frontend → API Gateway → Labs Service → Labs DB
  - *Priority*: High

- **User 05**: As a student, I want to submit lab solutions by uploading files to the platform
  - *Acceptance Criteria*: File upload to MinIO, submission metadata stored in Labs DB
  - *Technical Implementation*: Frontend uploads to MinIO, Labs Service stores file references and metadata
  - *Priority*: High

- **User 06**: As an educator, I want to create lab assignments through Labs Service with file attachments stored in the platform
  - *Acceptance Criteria*: Labs Service API for CRUD operations, file uploads to MinIO, lab publishing workflow
  - *Technical Implementation*: Rich editor uploads resources to MinIO, Labs Service stores lab structure
  - *Priority*: High

#### **Articles Management (Articles Service + File Storage)**

- **User 07**: As a researcher, I want to publish articles through Articles Service with supporting documents stored in the platform
  - *Acceptance Criteria*: Articles Service handles article CRUD, file references to MinIO
  - *Technical Implementation*: Frontend → API Gateway → Articles Service → Articles DB
  - *Priority*: High

- **User 08**: As a user, I want to browse published articles through Articles Service
  - *Acceptance Criteria*: Articles Service provides REST API for articles listing
  - *Technical Implementation*: Frontend → API Gateway → Articles Service → Articles DB
  - *Priority*: High

#### **Feedback and Review System (Feedback Service)**

- **User 09**: As a student, I want to receive structured feedback on lab submissions through Feedback Service so that I can improve my skills and learn from detailed reviews
  - *Acceptance Criteria*: Feedback Service stores reviews linked to lab submissions
  - *Technical Implementation*: Feedback Service connects to Labs Service via gRPC for submission data
  - *Priority*: High

- **User 10**: As a reviewer, I want to provide feedback on articles and labs
  - *Acceptance Criteria*: Comment systems, reviewer assignment logic
  - *Technical Implementation*: Feedback Service handles review workflows and notifications
  - *Priority*: High

- **User 11**: As a platform user, I want to track feedback history and respond to reviews
  - *Acceptance Criteria*: Feedback threads, notification system, response tracking, review status management
  - *Technical Implementation*: Feedback Service manages review conversations and state
  - *Priority*: Medium

### Prioritized backlog

Can be found by this [(link)](https://github.com/orgs/IU-Capstone-Project-2025/projects/6/views/1)

## Project specific progress

### Frontend

- **Project Structure Development**: Established comprehensive frontend project architecture with organized component hierarchy and module separation
- **Design System Enhancement**: Updated and expanded design system components including lab cards, user interface elements, and consistent styling patterns
- **User Interface Implementation**: Developed key platform pages including Sign Up forms, user profile interfaces, My Articles section, and article viewing components
- **User Experience Design**: Created detailed user flow diagrams to map platform navigation and interaction patterns
- **Component Development**: Built foundational page skeletons with registration forms, sidebar navigation featuring theme switching capabilities, and header components with integrated search and profile functionality

### Backend

- **Microservices Architecture**: Finalized comprehensive microservices design with documented API communication protocols, endpoints, models, and error handling between frontend and backend teams
- **Authentication Service (for now merged with User Service)**: Developed fully functional Auth Service with JWT authentication, database entities, and API endpoints for frontend authentication flows and API Gateway token validation
- **Labs & Articles Services**: Designed Labs and Articles services including database entities, API development, inter-service interactions, user stories, and technical implementation specifications
- **Feedback Service**: Built complete Feedback service architecture with detailed documentation, protobuf schemas for inter-service communication, database migration scripts, and storage structure specifications
- **Storage Solutions**: Contributed to final storage architecture design and implementation planning

### ML

- **Data Research & Experimentation**: Conducted comprehensive data experiments and research activities, including finding suitable datasets, reviewing code review methodologies, and identifying effective training approaches with all references documented in commits and pull requests
- **Chat Agent Development**: Developed intelligent chat agent with context memory capabilities for answering contextual questions and supporting markdown rendering for enhanced response formatting
- **RAG Database Foundation**: Created foundational RAG (Retrieval-Augmented Generation) database infrastructure, currently pending backend wrapper implementation for efficient storage and indexing
- **Chat History Implementation**: Implemented comprehensive chat history functionality with user ID tracking for personalized conversation management
- **Cross-Team Coordination**: Actively coordinating with backend team on user storage APIs and frontend team on chat interface implementation to ensure seamless integration

# Weekly commitments

## Individual contribution of each participant

- **Kirill Efimovich (PM / DevOps):**

**Kanban board (clickable):** [link](https://github.com/orgs/IU-Capstone-Project-2025/projects/6/views/1) \
**Milestone (clickable)** [link](https://github.com/IU-Capstone-Project-2025/open-labs-share/milestone/1) \
**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/4), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/16), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/31), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/3), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/27) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/37), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/35), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/29), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/28) \
**Summary of TA feedback:** Good project idea, a little bit behind of other groups due to lack of meetings efficiency. Clear previous report, but more artifacts required for the future. \
**Weekly contribution:** Coordinated team meetings and TA meeting, managed project backlog with automation, established contributing guidelines with PR/commit rules, and prepared weekly report. Actively motivated team members throughout the week, provided guidance and answered questions to ensure smooth progress, and coordinated extensive communication between team members to maintain project momentum.

- **Mikhail Trifonov (Backend):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/25), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/18), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/10), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/11), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/15) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/43), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/40), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/39) \
**Weekly contribution:** Worked on Auth Service including database entities and authentication logic. Developed API endpoints for frontend authentication flows and token validation for API Gateway. Built fully functional Auth Service with JWT authentication (excluding non-essential endpoints like password reset and email interactions, which are stubbed). Updated inter-service communication schema to reflect new connections.
  
- **Nikita Maksimenko (Backend):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/16), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/25), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/10), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/11), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/15), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/44), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/19) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/48) \
**Weekly contribution:** Documented API communication protocols (endpoints, models, error handling) between frontend and backend teams. Contributed to final microservices architecture design and storage solutions.

- **Timur Salakhov (Backend):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/21), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/23), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/11) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/42), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/41) \
**Weekly contribution:** Worked on Labs and Articles services design and development. For each service: justified its purpose, designed database entities, collaborated with Nikita on API development, described inter-service interactions, wrote user stories, and specified technical implementation details of his services (Labs and Articles).

- **Ravil Kazeev (Backend):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/26), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/11) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/47) \
**Weekly contribution:** Developed full Feedback service architecture including detailed service documentation, protobuf schemas for inter-service communication, database migration scripts, and storage structure specifications. Core service implementation is being made. Repository contributions include comprehensive service descriptions and database/storage design documentation.

- **Kirill Shumskiy (ML):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/32), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/13), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/14) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/38), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/34) \
**Weekly contribution:** Conducted data experiments and research - found suitable datasets, reviewed code review methodologies, and identified training approaches (all references available in commits/PRs). Developed chat agent with context memory capable of answering contextual questions. Created RAG database foundation, pending backend wrapper implementation for storage and indexing. Implemented chat history functionality with user ID tracking. Currently coordinating with backend team on user storage APIs and frontend team on chat interface implementation. Agent supports markdown rendering for responses.

- **Aleliya Turushkina (Designer / Frontend):**

**Figma board (clickable):** [link](https://www.figma.com/design/mvegZwCxX8KHxhtI2PeMHQ/OpenLabsShare?node-id=0-1&p=f&t=M2kuxYrgLTacXKCY-0) \
**User Flow diagram (clickable):** [link](https://www.figma.com/board/h5M1ofnM5hvBRUiCLaYDc7/User-flow-diagram?node-id=0-1&p=f&t=74EjkMcaerNxCK5U-0) \
**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/6), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/8), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/7), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/5) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/49), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/30) \
**Weekly contribution:** Created frontend project structure and updated design system with lab cards, Sign Up page, user profile pages, My Articles section, and article viewing pages. Developed comprehensive user flow diagram. Built page skeletons including registration forms, sidebar navigation with theme switching, and header with search and profile components.

**More detailed descriptions of services can be found by links from project `README.md` file [(link)](https://github.com/IU-Capstone-Project-2025/open-labs-share/blob/main/README.md).**
## Plan for Next Week

With all preparation work and documentation completed, our team is ready to focus entirely on developing the MVP over the next week.

### Tasks to be tackled

- **Backend Development:**
  - Implement core API endpoints for user authentication and study materials management
  - Set up database schema and data models
  - Implement basic CRUD operations for study materials and user profiles

- **Frontend Development:**
  - Create main user interface components based on finalized designs
  - Implement projected user authentication flows (login/register)
  - Develop study materials browsing functionality
  - Build projected basic user profile management interface

- **ML Integration:**
  - Deploy trained model
  - Create API endpoints for model inference
  - Test model performance with user data

### Expected Deliverables

- **Functional MVP** with core features implemented
- **Deployed application** accessible via Docker image
- **Complete API documentation** for all implemented endpoints
- **Updated project documentation** reflecting current implementation status

## Confirmation of the code's operability

We confirm that the code in the main branch:

  ☑️ In working condition. \
  ☑️ Run via docker-compose (or another alternative described in the `README.md`).
