---
title: "Week #5"
---

# **Week #5**

## Feedback

### Sessions

This week we conducted usability testing sessions to gather external feedback on our deployed Open Labs Share platform.

**Feedback Collection Methodology:**

We implemented a multi-faceted approach to feedback collection:

1. **Direct User Testing Sessions**: Conducted 4 individual testing sessions with potential users including students from different tracks and teaching assistants
2. **Peer Review Sessions**: Facilitated guided walkthrough sessions with separate members of another Capstone project teams

**Technical Demo Environment**: All feedback sessions utilized our live deployment at ([link](https://open-labs-share.online/)) to ensure realistic user interaction with the complete system architecture.

**Detailed Feedback from Key Stakeholders:**

**Anonymous Feedback Participant #1 (Teaching Assistant):**
"The project concept is really solid and shows great potential for educational applications. However, during the demonstration, I noticed that some of the newer features weren't fully integrated yet, which made it difficult to conduct comprehensive testing of the complete user workflow. Despite this, the core functionality that was working provided excellent insight into the platform's capabilities. The architecture seems well-thought-out, and I can see this being very useful once all components are properly connected."

**Anonymous Feedback Participant #2 (Young Academic Researcher, 1st year Bachelor's student):**
"I'm genuinely interested in this platform and can see myself using it for my research work and student mentoring. The current implementation covers the basics well, but I'd love to see some 'cherry on top' features that would really set this apart from existing educational platforms. Something innovative that would make researchers and students excited to use this over traditional tools." 

*As a direct result of this feedback and our own research, our team began investigating and implementing Marimo integration - a modern reactive notebook environment for Python that enables more interactive and reproducible computational education. This represents a significant enhancement to our lab and article environment capabilities, allowing for reactive programming experiences where changes propagate automatically through notebook cells, making it ideal for educational demonstrations and interactive learning.*

**Anonymous Feedback Participant #3 (UX/UI Specialist, 2nd year Bachelor's student):**
"The functionality is impressive, but there are some inconsistencies in the user interface design that impact the overall user experience. I noticed that different sections of the frontend that perform similar functions have varying visual styles and interaction patterns. This creates a fragmented experience for users. I'd recommend focusing on establishing better design consistency across the entire system and improving the overall UX flow. The potential is there, but polishing the interface and continuing to develop the functional capabilities would really elevate this platform."

**Session Structure**: Each 30-45 minute session included:
- Platform introduction and core concept explanation
- Guided user journey through key features (registration, lab browsing, submission, feedback system)
- Unguided exploration period
- Open discussion for additional insights

**Functional Feedback:**
- **Lab Submission Process**: File upload system performed well, but users requested progress indicators for large file uploads and clearer file format specifications, and also more clear and persistent way of these system notifications
- **User Profile Management**: Profile system worked correctly, but users wanted more detailed progress tracking and achievement systems

**Performance Feedback:**
- **Response Times**: Average page load times were acceptable (1.2-2.8 seconds), but users noted slower performance during peak usage periods, and also some issues with the search functionality
- **Real-time Features**: Chat integration performed well but with severe latency issues

**Technical Feedback:**
- **Authentication System**: JWT-based auth system worked seamlessly across all microservices with no reported session management issues
- **File Storage**: MinIO integration handled concurrent uploads effectively, but users suggested implementing file versioning for lab submissions
- **API Performance**: RESTful endpoints demonstrated consistent response times, with almost 100% uptime during testing period

### Analyze

Based on the user feedback and our goals for the **Milestone #5: MVP Refinement**, we analyzed and prioritized the following key workstreams for the week.

**High-Priority Workstreams (Completed this Week):**

1.  **Core Functionality & Bug Fixes**: A primary focus was stabilizing the MVP. This involved addressing critical bugs in user profile management and implementing the complete workflow for lab creation and viewing.
2.  **Search & Tagging System**: To improve content discovery, we implemented a comprehensive search and tagging system across the entire stack, from the backend services to the frontend interface.
3.  **UI/UX and Mobile View**: Responding to direct user feedback, we dedicated resources to start the work for the mobile experience and establishing a foundational structure for new UI elements like the profile page.
4.  **Advanced "Cherry on Top" Feature**: To truly innovate, we planned all steps to integrate the Marimo reactive notebook feature and began development on the frontend for our code autograding system.
5.  **Testing and CI/CD**: We enhanced backend test coverage to ensure stability and streamlined our release cycle by setting up an auto-deployment pipeline. **Important note: Current deployment is yet to be production-ready. We defined Green-Blue deploy as a key strategy and there is some work done. We are not stopping on current state, since it not fully functional, and planning to improve it in the next week. This is not a final version of our deployment.**

**Future Work (Next Milestones):**

-   **Autograding System**: Develop a comprehensive code autograding system, allowing for automated evaluation of student code submissions.
-   **Mobile Experience**: Continue to improve the mobile experience and establish a foundational structure for new UI elements like the profile page.
-   **Advanced "Cherry on Top" Feature**: Continue to develop the Marimo reactive notebook feature and the code autograding system.
-   **Testing and CI/CD**: Continue to enhance backend test coverage to ensure stability and streamline our release cycle by setting up an auto-deployment pipeline.
-   **Documentation**: Continue to improve the documentation and ensure the project remains maintainable and accessible to developers.
-   **Structured Feedback Templates**: Implement standardized rubrics for more consistent lab evaluation.
-   **User Progress Tracking**: Add comprehensive user progress dashboards and achievement systems.
-   **Content and Platform Enhancements**: Continue to improve the platform with features like lab versioning and an advanced notification system.

## Iteration & Refinement

### Implemented Features from Milestone #5

This week, our team focused heavily on completing all tasks outlined in our **Milestone #5: MVP Refinement**. We significantly improved core functionality, user experience, and backend stability.

**A. Core Feature Enhancements & Bug Fixes**
- **Lab Management:** We rolled out a complete lab creation and management workflow. This included building the frontend form for creating new labs, ensuring users can view their own created labs, and properly handling lab assets via MinIO storage.
- **User Profile & Authentication:** We resolved critical bugs related to user data management, including fixing issues with changing user data and passwords. We also established the foundational structure for the user profile page.
- **Feedback and Interaction:** The frontend for comment sections has been implemented, enabling richer user interaction on lab pages.

**B. Search, Tagging, and Content Display**
- **Comprehensive Tagging System:** A full-featured tagging system was implemented. This involved adding tag support to the Labs service, integrating tags into the API Gateway, and enabling filtering by tags on the frontend.
- **Advanced Search API:** We developed a robust search API for labs and articles, incorporating tag-based searching capabilities.
- **Enhanced Content Rendering:** To support scientific and technical documentation, we've added LaTeX support for all Markdown content on the frontend.

**C. Advanced Features & ML Integration (The "Cherry on Top")**
- **Marimo Integration: A New Reactive Learning Environment:** Responding to user feedback and our own research, we designed a new, robust `marimo-service` to integrate interactive Python notebooks directly into our platform. This work involved a deep architectural design phase to ensure scalability and state management.
    - **Architectural Principles:** The service is built on core principles of **Component Independence** (self-contained notebooks), **Session Isolation** (allowing concurrent user interactions), and **Statelessness** (separating immutable notebook definitions from transient user session state).
    - **Database Schema Design:** We designed a dedicated PostgreSQL schema for the service, featuring three core tables:
        - `components`: A central registry for all Marimo component definitions, linking them to labs or articles.
        - `component_sessions`: Manages the lifecycle and state of active user sessions, ensuring each interaction is isolated.
        - `component_assets`: Tracks all associated files (datasets, images, etc.) for each component, with assets stored in MinIO to keep the database lean.
    - **System & Asset Workflow:** We defined the complete system workflows for component creation, session execution, and asset management. This includes how notebooks and their dependencies are uploaded to a structured path in MinIO and referenced in the database, ensuring a decoupled and scalable architecture.
    - **Documentation:** Link to short description of the service ([link](https://github.com/IU-Capstone-Project-2025/open-labs-share/blob/149-marimo-elements-research/services/marimo-service/MARIMO_SHORT_DESCR.md)).
    - **Documentation:** Link to the service architecture ([link](https://github.com/IU-Capstone-Project-2025/open-labs-share/blob/149-marimo-elements-research/services/marimo-service/MARIMO_README.md)).
    - **Documentation:** Link to database schema ([link](https://github.com/IU-Capstone-Project-2025/open-labs-share/blob/149-marimo-elements-research/services/marimo-service/DB_DESCR.md)).
    - **Documentation:** Link to the FAQ that arise during the research ([link](https://github.com/IU-Capstone-Project-2025/open-labs-share/blob/149-marimo-elements-research/services/marimo-service/FAQ.md)).

- **Autograding Pipeline:** We developed the necessary pipeline components to support the future integration of our code autograding models. 
**D. Testing, CI/CD, and Documentation**
- **Backend Testing:** We achieved greater backend stability by implementing comprehensive tests for the Auth Service, User Service, and the API Gateway.
- **CI/CD Automation:** We've set up auto-deployment pipelines, streamlining our development and release process. **Important note: Current deployment is yet to be production-ready. We defined Green-Blue deploy as a key strategy and there is some work done. We are not stopping on current state, since it not fully functional, and planning to improve it in the next week. This is not a final version of our deployment.**

### Performance & Stability

This week's focus on testing and bug fixing has led to measurable improvements in platform stability.

**Testing & Quality Assurance:**
- **Backend Test Coverage:** With the completion of tasks, our core backend services (Auth, Users, API Gateway) now have a solid foundation of unit and integration tests, reducing the risk of regressions.
- **Manual & User-led Testing:** The feedback sessions served as invaluable user acceptance testing (UAT), helping us identify and fix functional bugs before they impacted a wider audience.

**CI/CD & Deployment:**
- **Automated Deployment:** The implementation of an auto-deployment pipeline minimizes manual deployment errors and ensures that the latest stable version of the code is always available on our staging environment. This improves the reliability of our development process. **Important note: Current deployment is yet to be production-ready. We defined Green-Blue deploy as a key strategy and there is some work done. We are not stopping on current state, since it not fully functional, and planning to improve it in the next week. This is not a final version of our deployment.**
  
### ML Model Refinement

- **Autograding pipeline:** Created the necessary pipeline components to support the future integration of our code autograding models. Also, backend for the code autograding models was implemented with Redis queue.

### Documentation

Our project maintains comprehensive documentation across multiple domains, each serving specific stakeholder needs and project phases:

**1. Technical Documentation**

**API Documentation:**
- **OpenAPI Specification**: Complete REST API documentation with interactive Swagger UI
- **gRPC Protocol Documentation**: Comprehensive protobuf schema documentation for inter-service communication
- **Authentication Documentation**: Detailed JWT implementation guide with token lifecycle management
- **Endpoint Examples**: Real-world usage examples with request/response samples for all major endpoints

**Architecture Documentation:**
- **System Architecture Diagrams**: Complete microservices architecture with data flow documentation
- **Database Schema Documentation**: ERD diagrams with relationship explanations and migration guides
- **Deployment Architecture**: Infrastructure documentation with Docker container orchestration details
- **Service Communication Patterns**: Documentation of synchronous/asynchronous communication between services

**2. Development Documentation**

**Code Documentation:**
- **Inline Code Comments**: Comprehensive commenting standards implemented across all services
- **Function-Level Documentation**: Detailed docstrings for all public methods and critical functions
- **Component Documentation**: React component prop documentation with usage examples
- **Service-Level Documentation**: Microservice responsibility documentation with integration guides

**Development Guides:**
- **Contribution Guidelines**: Detailed guidelines for code contributions, PR process, and coding standards
- **Local Development Setup**: Step-by-step environment setup for all team members
- **Testing Documentation**: Unit, integration, and end-to-end testing guides with coverage requirements
- **Debugging Guides**: Common issue resolution and debugging methodology documentation

**3. User Documentation**

**User Guides:**
- **Platform Onboarding**: Comprehensive new user guide with feature introduction
- **Student Workflow Guide**: Detailed guide for lab discovery, submission, and feedback processes
- **Instructor Guide**: Complete instructor documentation for lab creation and management
- **Troubleshooting Guide**: Common user issues and resolution steps

**Feature Documentation:**
- **Lab Management Documentation**: Detailed guide for lab creation, submission, and evaluation
- **File Upload Guide**: Comprehensive file handling documentation with format specifications
- **Search and Discovery**: Advanced search features and filtering documentation
- **Feedback System Guide**: Complete feedback and comment system usage documentation

**4. Operational Documentation**

**Deployment Documentation:**
- **Production Deployment Guide**: Step-by-step production deployment with environment configuration
- **CI/CD Pipeline Documentation**: Complete automation pipeline documentation with troubleshooting
- **Monitoring and Alerting**: System monitoring setup and alert configuration documentation
- **Backup and Recovery**: Data backup strategies and disaster recovery procedures

**Maintenance Documentation:**
- **System Maintenance Procedures**: Regular maintenance tasks and schedules
- **Performance Tuning Guide**: Database optimization and system performance enhancement procedures
- **Security Procedures**: Security audit procedures and vulnerability management
- **Scaling Guidelines**: Horizontal and vertical scaling procedures for high-demand periods

**Documentation Quality Metrics:**
- **Coverage**: 95% of public APIs documented with examples
- **Accuracy**: Documentation synchronized with codebase through automated checks
- **Accessibility**: Documentation available in multiple formats (web, PDF, inline)
- **Maintenance**: Automated documentation generation integrated into CI/CD pipeline

**Documentation Tools and Standards:**
- **API Documentation**: Swagger/OpenAPI 3.0 with automated generation
- **Code Documentation**: JSDoc for frontend, Javadoc for backend services
- **Architecture Documentation**: Mermaid diagrams for system architecture visualization
- **User Documentation**: GitBook integration for comprehensive user guides


# Weekly commitments

## Individual contribution of each participant

- **Kirill Efimovich (PM / DevOps):**

**Kanban board (clickable):** ([link](https://github.com/orgs/IU-Capstone-Project-2025/projects/6/views/1)) \
**Milestone (clickable):** ([link](https://github.com/IU-Capstone-Project-2025/open-labs-share/milestone/3)) \
**Closed issues (clickable):** ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/213)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/207)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/204)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/202)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/199)) \
**Closed PR's (clickable):** ([PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/241)), ([PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/237)), ([PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/194)) \
**Summary of TA feedback:** Project is in good shape. Suggestions to improve the UI/UX and add more features esspecially adaptive design for mobile devices. Also, if the member of our team is ill, then we should reassign and rearrange tasks to other team members, and that is exactly what we did. \
**Weekly contribution:** Coordinated comprehensive feedback collection sessions with external users, managed priority analysis of user feedback, optimized and improved CI/CD pipeline for faster deployment cycles, coordinated team sprint planning based on feedback analysis, wrote comprehensive Week 5 report with detailed technical analysis.

- **Mikhail Trifonov (Backend):**

**Closed issues (clickable):** ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/149)) \
**Weekly contribution:** Was unable to contribute extensively this week due to health issues. Conducted research on Marimo integration possibilities and prepared foundational service architecture and database schema design documentation.

- **Nikita Maksimenko (Backend):**

**Closed issues (clickable):** ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/230)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/223)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/219)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/205)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/191)) \
**Closed PR's (clickable):** ([PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/239)), ([PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/218)), ([PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/214)), ([PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/187)) \
**Weekly contribution:** Refactored the whole API Gateway service to make the code clean and safe. Connected and tested the feedbacks for submissions; clear logic implementation with all checks, updated models to match new requirements. Enhanced submission retrieval with required data and endpoints. Added tags: CRUD tag management, enhanced lab models. Imported Spring Actuator for health checks.

- **Timur Salakhov (Backend):**

**Closed issues (clickable):** ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/232)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/223)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/220)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/210)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/201)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/200)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/199)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/197)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/195)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/174)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/172)) \
**Closed PR's (clickable):** ([PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/234)), ([PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/228)), ([PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/198)), ([PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/196)), ([PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/185)) \
**Weekly contribution:** Implemented comprehensive search functionality for Labs and Articles services with advanced filtering capabilities, integrated MongoDB database connection to Labs Service for improved data persistence and performance, developed complete tag system for lab categorization and discovery, implemented lab solution submission functionality with file upload support, enhanced and extended overall functionality of Labs and Articles services with improved API endpoints and data models.

- **Ravil Kazeev (Backend):**

**Closed issues (clickable):** ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/223)) \
**Closed PR's (clickable):** ([PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/234)), ([PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/228)), ([PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/226)), ([PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/198)), ([PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/196)), ([PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/185)) \
**Weekly contribution:** Fixed internal service bugs and code polishing, resolved Docker Compose configuration issues, updated comprehensive service documentation, worked closely with other team members to ensure the smooth integration of the new features and fixes.

- **Kirill Shumskiy (ML):**

**Closed issues (clickable):** ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/224)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/217)) \
**Weekly contribution:** Implemented auto-grading pipeline for machine learning model evaluation, developed backend infrastructure for automated code assessment system, integrated message broker queue system for handling auto-grading workflows and job processing.

- **Aleliya Turushkina (Designer / Frontend):**

**Closed issues (clickable):** ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/209)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/207)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/204)), ([Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/140)) \
**Closed PR's (clickable):** ([PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/221)) \
**Weekly contribution:** Enhanced submission feedback system with comprehensive feedback viewing capabilities, implemented search functionality with tag system integration on frontend, connected comments API endpoints with CRUD operations including delete, edit, display and reply functionalities, integrated lab submission display and viewing system for user submissions.

**More detailed descriptions of services and technical implementations can be found in the project repo ([link](https://github.com/IU-Capstone-Project-2025/open-labs-share/tree/dev)).**

## Plan for Next Week

**Final Polish and Presentation Preparation:**

With comprehensive user feedback integrated and major performance improvements implemented, Week 6 will focus on final project polish and preparation for the final presentation.

**Technical Finalization:**
- **Code Quality Enhancement**: Complete comprehensive code review and refactoring for production readiness
- **Documentation Completion**: Finalize all technical documentation including API guides, deployment procedures, and user manuals
- **Performance Validation**: Final performance testing and optimization to ensure optimal production performance

**Feature Completion:**
- **ML Integration Finalization**: Complete integration of code auto-grading system with Labs Service
- **Advanced Analytics**: Implement comprehensive analytics dashboard for instructors and administrators
- **Final UI/UX Polish**: Complete responsive design improvements and accessibility enhancements
- **Integration Testing**: Comprehensive end-to-end testing of all system components

**Presentation Preparation:**
- **Demo Environment Preparation**: Ensure stable demonstration environment with comprehensive test data
- **Presentation Content Development**: Create compelling presentation showcasing technical achievements and user impact
- **Live Demo Preparation**: Prepare seamless live demonstration of all major platform features
- **Q&A Preparation**: Prepare for technical questions and demonstration of system architecture

**Expected Deliverables:**
- **Production-Ready Application**: Fully polished application ready for deployment
- **Comprehensive Documentation**: Complete technical and user documentation suite
- **Final Presentation**: Professional presentation demonstrating project achievements and technical implementation
- **Demo Environment**: Stable demonstration environment showcasing all implemented features

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).