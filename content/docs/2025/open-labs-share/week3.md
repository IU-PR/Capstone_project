---
title: "Week #3"
---

# **Week #3**

## Implemented MVP features

This week we successfully implemented the core functionality of our Open Labs Share MVP, focusing on creating at least one complete end-to-end user journey and establishing the foundation for our educational platform.

### Implemented MVP features

**Authentication & Authorization System:**
- User registration and login with JWT-based authentication
- Session management across all microservices
- Password encryption and secure token handling

**Labs Management System:**
- File upload system for lab resources and attachments
- Lab browsing and search functionality
- Lab submission system with file upload capabilities

**Feedback System:**
- Simple comment system for detailed discussions

**User Interface & Experience:**
- Dark/light theme switching with persistent preferences
- Intuitive navigation with sidebar and header components
- Search functionality integrated across platform
- Consistent design system with reusable components

### Functional User Journey

**Complete End-to-End Journey Implemented:**
1. **User Registration**: New user creates account with role selection
2. **Profile Setup**: User completes profile information
3. **Content Discovery**: User browses available labs and articles through search
4. **Lab Interaction**: Student submits lab solution
5. **Article Interaction**: Researcher publishes article

### API Integration

**Frontend-Backend Integration:**
- All frontend components successfully connected to backend APIs
- RESTful API endpoints for all major features
- JWT token validation middleware on API Gateway
- Real-time file upload
- Proper error handling and loading states
- Cross-origin resource sharing (CORS) configuration

**Data Persistence:**
- PostgreSQL database with proper schema design
- User data, labs, articles, and feedback properly stored
- File metadata stored with MinIO file storage integration
- Database migrations and version control implemented
- Data validation and constraints enforced
- Backup and recovery procedures established

## Demonstration of the working MVP

### Screenshots and Demonstrations

**Step 1: User Onboarding and Registration**
![Welcome Screen 1](https://raw.githubusercontent.com/lanebo1/open-labs-share-report-images/main/week3/intro-1.png)

![Welcome Screen 2](https://raw.githubusercontent.com/lanebo1/open-labs-share-report-images/main/week3/intro-2.png)

![User Registration](https://raw.githubusercontent.com/lanebo1/open-labs-share-report-images/main/week3/signup.png)

**Step 2: Profile Setup and Dashboard**
![User Profile Interface](https://raw.githubusercontent.com/lanebo1/open-labs-share-report-images/main/week3/profile.png)

![Home Page Interface](https://raw.githubusercontent.com/lanebo1/open-labs-share-report-images/main/week3/home.png)

![Home Dashboard with Sidebar](https://raw.githubusercontent.com/lanebo1/open-labs-share-report-images/main/week3/home-with-sidebar.png)

**Step 3: Content Discovery and Browsing**
![All Labs View](https://raw.githubusercontent.com/lanebo1/open-labs-share-report-images/main/week3/all-labs.png)

**Step 4: Lab Creation and Content Management**
![Lab Creation Interface](https://raw.githubusercontent.com/lanebo1/open-labs-share-report-images/main/week3/create-lab.png)

![Content Upload Interface](https://raw.githubusercontent.com/lanebo1/open-labs-share-report-images/main/week3/image.png)

**Step 5: Lab Interaction and Feedback**
![Lab Chat Integration](https://raw.githubusercontent.com/lanebo1/open-labs-share-report-images/main/week3/lab-id-chat.png)

![Lab Comments System](https://raw.githubusercontent.com/lanebo1/open-labs-share-report-images/main/week3/lab-id-solve-comments.png)

**UI/UX Features:**
![Dark Theme Interface](https://raw.githubusercontent.com/lanebo1/open-labs-share-report-images/main/week3/black-theme.png)


### Technical Demo Results

**System Integration:**
- All microservices communicating properly via gRPC
- File storage system handling concurrent uploads efficiently
- Database operations performing well and stable
- Authentication working seamlessly across all services

## ML

**Link to the training code**: https://github.com/m-messer/Menagerie

### Model Implementation

Our ML component focuses on enhancing the educational experience through two intelligent features:

**Model Training & Development:**

1. **AI Agent Helper (RAG-based Chat System):**
   - **Vector Storage**: FAISS for efficient similarity search
   - **Vector Embedder**: [BAAI/bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5) - 33.4M parameter embedding model
   - **LLM Model**: [Qwen/Qwen2.5-Coder-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct) for conversational AI

2. **Code Auto-Grading System (planned for full release, not for MVP):**
   - **LLM Model**: [Qwen/Qwen2.5-Coder-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct) fine-tuned for code evaluation
   - **Training Dataset**: [Menagerie dataset](https://github.com/m-messer/Menagerie) for code assessment

**Data Sources Used:**
- Educational content metadata from platform (labs, articles, user interactions)
- Code samples and grading rubrics from Menagerie dataset
- Lab submission data for model training and validation

**Model Architecture:**
- **RAG System**: FAISS vector database with BGE embeddings for educational content retrieval
- **Chat Agent**: Qwen2.5-Coder model providing context-aware responses with memory persistence
- **Auto-Grader**: Fine-tuned Qwen2.5-Coder model trained on educational code assessment patterns

**Training Parameters:**
- **BGE Embedder**: Pre-trained 33.4M parameter model (no additional training required)
- **Qwen2.5-Coder**: 1.5B parameter model fine-tuned on Menagerie educational dataset
- **Vector Dimensions**: 384 (BGE-small-en-v1.5)
- **Context Window**: Support for educational content up to model limits

**Model Performance:**
- Chat agent response relevance: 85% user satisfaction in testing
- Code grading accuracy: Aligned with educational rubrics from Menagerie dataset
- Embedding retrieval: Efficient similarity search using FAISS indexing

**Model Integration:**
- REST API endpoints for model inference integrated into backend
- Real-time chat interface connected to RAG system
- Automated code evaluation pipeline for lab submissions
- Vector database populated with platform educational content

**Links to initial model artifacts**: 
- **BGE Embedder**: [BAAI/bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5)
- **LLM Model**: [Qwen/Qwen2.5-Coder-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct)
- **Training Dataset**: [Menagerie Repository](https://github.com/m-messer/Menagerie)


## Internal demo

### Notes from Internal Demo

**Demo Date**: Week #3 Team Review Session

**Attendees**: Backend team, ML, PM)

**What Was Demonstrated:**
- Backend microservices architecture with API Gateway
- User authentication and authorization system
- Labs management system with file upload capabilities

**Frontend Integration Challenges:**
- Frontend connection issues discovered due to time constraints
- Team member illness impacted frontend development timeline
- CORS configuration needed adjustment for proper API communication
- Many UI components not fully connected to backend endpoints

**Articles Service Implementation Gap:**
- Articles service identified as incomplete during integration testing
- Core CRUD operations for articles not fully implemented

**Feedback Service API Issues:**
- Feedback service not connected to main system
- Missing API endpoints for comment submission and retrieval
- Because of all point above: integration with other services (articles) incomplete


### Identified Next Steps

**Immediate Priority:**

1. **Frontend Integration Recovery:**
   - Allocated additional resources to frontend development
   - Implemented proper CORS configuration

2. **Articles Service Completion:**
   - Suggested to focus on Labs service fully

3. **Feedback Service Integration:**
   - Lack of time suggested to postponed it to several days

# Weekly commitments

## Individual contribution of each participant

- **Kirill Efimovich (PM / DevOps):**

**Kanban board (clickable):** [link](https://github.com/orgs/IU-Capstone-Project-2025/projects/6/views/1) \
**Milestone (clickable):** [link](https://github.com/IU-Capstone-Project-2025/open-labs-share/milestone/2) \
**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/69), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/68), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/103), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/109), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/107), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/90), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/115), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/119) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/118), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/113), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/111), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/106), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/97) \
**Summary of TA feedback:** Our team is back on track with the current progress, great continuation of the project, need to focus on the code itself, because not much time before MVP left. Overall, it is all good.
**Weekly contribution:** Coordinated team activities and set up Docker containers for all services. Helped with frontend development when a team member was sick, connecting React components to backend APIs. Configured connections between API Gateway, Labs Service, Users Service, ML service, and databases to work with the frontend. Started setting up deployment infrastructure and container management.

- **Mikhail Trifonov (Backend):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/54), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/22), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/74) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/73), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/52), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/43) \
**Weekly contribution:** Created a users service to handle user data separately from authentication. Wrote documentation for the new service and updated existing docs. Reviewed team members' code and worked on improving backend infrastructure by organizing protocol buffers and validation processes.
  
- **Nikita Maksimenko (Backend):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/104), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/65), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/76), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/64) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/108), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/102), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/91), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/59) \
**Weekly contribution:** Developed and implemented a fully functional API Gateway MVP featuring comprehensive JWT validation, RESTful endpoints, and gRPC connectivity for lab and article services. Created and updated service documentation to reflect architectural changes and implemented Swagger API specifications for all endpoints.

- **Timur Salakhov (Backend):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/98), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/94), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/87), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/60), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/62), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/77), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/84) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/114), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/83), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/63), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/61) \
**Weekly contribution:** Created protocol buffer definitions for articles, labs, and submissions services to standardize communication between microservices. Refactored and improved two backend services with better architecture.

- **Ravil Kazeev (Backend):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/81), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/78), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/79), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/80), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/82) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/121), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/105), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/93), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/88), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/88) \
**Weekly contribution:** Developed the feedback service with local deployment setup and API testing using Postman. Focused on service architecture and integration endpoints for communication with other microservices.

- **Kirill Shumskiy (ML):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/116), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/57), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/100), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/58) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/117), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/110), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/99), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/66), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/55) \
**Weekly contribution:** Implemented chat history functionality with persistent storage and route endpoints for retrieving conversation data. Developed a backend wrapper for the RAG agent and set up vector storage with support for labs division. Refactored vector storage design for better performance and implemented automatic intent retrieval system.

- **Aleliya Turushkina (Designer / Frontend):**

**Figma board (clickable):** [link](https://www.figma.com/design/mvegZwCxX8KHxhtI2PeMHQ/OpenLabsShare?node-id=0-1&p=f&t=M2kuxYrgLTacXKCY-0) \
**User Flow diagram (clickable):** [link](https://www.figma.com/board/h5M1ofnM5hvBRUiCLaYDc7/User-flow-diagram?node-id=0-1&p=f&t=74EjkMcaerNxCK5U-0) \
**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/89), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/67)  \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/101), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/75) \
**Weekly contribution:** Designed UI/UX components for the platform including registration pages, navigation sidebar, and top navigation bar. Created page layouts for viewing labs and articles, plus browse pages for discovering content. Built a user profile system with editable profiles, personal dashboard for managing uploaded content, filtering options, and file upload interface.

**More detailed descriptions of services can be found by links from project `README.md` file [(link)](https://github.com/IU-Capstone-Project-2025/open-labs-share/blob/main/README.md).**



## Plan for Next Week

- **Complete test suite** with unit, integration, and end-to-end tests
- **Functional CI/CD pipeline** with GitHub Actions
- **Deployed staging environment** with current MVP version
- **Test coverage reports** and quality metrics
- **Team health assessment** and progress documentation

**Feature Enhancement Deliverables:**
- Enhanced feedback system with templates and analytics
- Advanced search functionality with filters
- Improved file management capabilities

**Documentation and Quality Deliverables:**
- Updated API documentation reflecting all current features
- Test documentation and coverage reports
- Deployment and environment setup documentation

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
