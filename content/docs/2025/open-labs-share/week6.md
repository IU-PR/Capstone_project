---
title: "Week #6"
---

# **Week #6**

## Links

*Final deployment and project resources:*

- **Deployment**: link
- **API Docs**: link
- **Design**: link
- **Demo**: link
- **Repository**: link
- **Presentation**: link

## Final deliverables

### Project overview

Open Labs Share is an innovative educational platform that combines structured learning with academic collaboration, addressing the fragmented nature of educational resources and lack of constructive feedback mechanisms for students and researchers. Our platform bridges the gap between practical learning and academic discourse by creating a dual-environment system that facilitates both guided learning through practical assignments (labs) and open academic collaboration through research publication and peer review.

The platform solves critical problems in modern education: students struggling to get meaningful feedback on their work early in their careers, researchers lacking accessible platforms to share knowledge with learners, and the disconnect between theoretical learning and practical application. Our solution provides structured learning paths with practical assignments, comprehensive feedback systems, and tools for educators to guide students effectively.

### Features

**Implemented Core Features:**

- **Authentication & User Management**: Complete JWT-based authentication system with secure session management across all microservices, user registration with role selection, and comprehensive profile management
- **Labs Management System**: Full lab creation, browsing, and submission workflow with file upload capabilities, lab resource management via MinIO storage, and submission tracking with cost-based point system
- **Search & Discovery**: Advanced search functionality with tag-based filtering, comprehensive tagging system for content categorization, and efficient content discovery mechanisms
- **Feedback & Review System**: Complete comment system for detailed discussions, submission feedback workflows, and reviewer assignment logic with notification systems
- **User Interface & Experience**: Dark/light theme switching with persistent preferences, intuitive navigation with sidebar and header components, search integration across platform, and consistent design system with reusable components
- **File Storage & Management**: Robust file upload system with MinIO integration, concurrent upload handling, file versioning support, and metadata storage with validation

**Advanced Features:**

- **ML-Powered Chat Assistant**: RAG-based intelligent chat system using FAISS vector storage and BGE embeddings, context-aware responses with memory persistence, and educational content integration
- **Code Auto-Grading Pipeline**: Automated code evaluation system using fine-tuned Qwen2.5-Coder model, Redis queue-based job processing, and comprehensive assessment rubrics
- **Marimo Integration**: Reactive Python notebook environment for interactive computational education, component independence with session isolation, and stateless architecture for scalability
- **Advanced Analytics**: Comprehensive user progress tracking, instructor dashboards, and platform usage analytics
- **Responsive Design**: Mobile-optimized interface with adaptive design patterns and cross-platform compatibility

### Tech stack

**Frontend:**
- React 18.2 with TypeScript for type-safe development
- Tailwind CSS for utility-first styling and responsive design
- Vite for fast development and optimized production builds
- React Router for client-side navigation
- Axios for HTTP client with request/response interceptors

**Backend Microservices:**
- **API Gateway**: Spring Boot with JWT validation middleware and RESTful endpoint orchestration
- **Auth Service**: Spring Security with JWT authentication and password encryption
- **Users Service**: Spring Boot with user profile management and data persistence
- **Labs Service**: Spring Boot with MongoDB integration for lab and submission management
- **Feedback Service**: Spring Boot with MongoDB for comments and review systems
- **ML Service**: Python with FastAPI, FAISS vector database, and PyTorch for AI capabilities
- **Marimo Service**: Python with PostgreSQL for reactive notebook management

**Databases & Storage:**
- PostgreSQL for structured data (users, authentication, marimo components)
- MongoDB for document-based data (labs, articles, feedback)
- MinIO for object storage (files, assets, media)
- FAISS for vector search and ML embeddings
- Redis for caching and job queue management

**Infrastructure & DevOps:**
- Docker containers with Docker Compose orchestration
- GitHub Actions for CI/CD pipeline automation
- Self-hosted deployment with Cloudflare and CloudPub integration
- SSL certificates with domain management (open-labs-share.online)
- Automated testing and deployment workflows

**Machine Learning:**
- **Vector Embeddings**: BAAI/bge-small-en-v1.5 (33.4M parameters)
- **Language Model**: Qwen/Qwen2.5-Coder-1.5B-Instruct fine-tuned for educational content
- **Training Framework**: PyTorch with custom training pipelines
- **Vector Storage**: FAISS for efficient similarity search

### Setup instructions

**Prerequisites:**
- Docker and Docker Compose installed
- Git for repository cloning
- Minimum 8GB RAM and 4 CPU cores recommended

**Quick Start (Recommended):**

1. **Clone the Repository:**
   ```bash
   git clone link
   cd open-labs-share
   ```

2. **Environment Configuration:**
   ```bash
   cp .env.example .env
   # Configure environment variables for your setup
   ```

3. **Launch with Docker Compose:**
   ```bash
   docker-compose up -d
   ```

4. **Access the Application:**
   - Frontend: `http://localhost:3000`
   - API Gateway: `http://localhost:8080`
   - MinIO Console: `http://localhost:9001`

**Development Setup:**

1. **Backend Services Setup:**
   ```bash
   # Start infrastructure services
   docker-compose up -d postgres mongodb minio redis
   
   # Run individual services for development
   cd services/api-gateway && ./gradlew bootRun
   cd services/auth-service && ./gradlew bootRun
   cd services/users-service && ./gradlew bootRun
   cd services/labs-service && ./gradlew bootRun
   cd services/feedback-service && ./gradlew bootRun
   ```

2. **Frontend Development:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

3. **ML Service Setup:**
   ```bash
   cd services/ml-service
   pip install -r requirements.txt
   python app.py
   ```

**Database Initialization:**
- PostgreSQL databases auto-initialize with required schemas
- MongoDB collections are created automatically on first use
- MinIO buckets are configured through the startup process

**Testing:**
```bash
# Run all service tests
./scripts/run-tests.sh

# Run specific service tests
cd services/api-gateway && ./gradlew test
cd frontend && npm test
```

## Presentation draft

*Link to comprehensive final presentation covering project overview, technical architecture, live demonstration, and future roadmap.*

link

# Weekly commitments

## Individual contribution of each participant

- **Kirill Efimovich (PM / DevOps):**

**Kanban board (clickable):** link \
**Milestone (clickable):** link \
**Closed issues (clickable):** Issue, Issue, Issue, Issue, Issue, Issue, Issue, Issue \
**Closed PR's (clickable):** PR, PR, PR, PR, PR \
**Summary of TA feedback:** Excellent final project delivery with comprehensive feature set. Presentation preparation is well-structured and technical implementation demonstrates strong understanding of microservices architecture. Team coordination and project management throughout all weeks has been exemplary. \
**Weekly contribution:** Coordinated final project polish and code freeze implementation, managed comprehensive final testing across all microservices, finalized production deployment with SSL certificates and domain configuration, prepared final presentation slides and demo environment, conducted team retrospective and documented lessons learned, coordinated final documentation review and README completion, managed final milestone tracking and deliverable validation.

- **Mikhail Trifonov (Backend):**

**Closed issues (clickable):** Issue, Issue, Issue, Issue, Issue \
**Closed PR's (clickable):** PR, PR, PR, PR \
**Weekly contribution:** Finalized Marimo service architecture with complete database schema implementation and PostgreSQL integration, completed comprehensive documentation for all backend services including API specifications and deployment guides, conducted final code review and refactoring for production readiness across Users and Auth services, implemented final security enhancements including input validation and error handling, contributed to final system integration testing and bug fixes.
  
- **Nikita Maksimenko (Backend):**

**Closed issues (clickable):** Issue, Issue, Issue, Issue, Issue, Issue \
**Closed PR's (clickable):** PR, PR, PR, PR, PR \
**Weekly contribution:** Finalized API Gateway service with comprehensive error handling and rate limiting implementation, completed final integration of all microservice communication protocols and gRPC endpoints, implemented final performance optimizations including response caching and connection pooling, conducted comprehensive API documentation update with Swagger specifications, finalized health check endpoints and monitoring integration for all services, completed final security audit and vulnerability assessment.

- **Timur Salakhov (Backend):**

**Closed issues (clickable):** Issue, Issue, Issue, Issue, Issue, Issue, Issue \
**Closed PR's (clickable):** PR, PR, PR, PR, PR \
**Weekly contribution:** Completed final Labs and Articles services optimization with MongoDB performance tuning and indexing strategies, implemented comprehensive search functionality with advanced filtering and pagination, finalized tag system integration with full CRUD operations and search optimization, completed lab submission workflow with file validation and storage optimization, conducted final service documentation and API endpoint testing, implemented final backup and recovery procedures for MongoDB collections.

- **Ravil Kazeev (Backend):**

**Closed issues (clickable):** Issue, Issue, Issue, Issue \
**Closed PR's (clickable):** PR, PR, PR \
**Weekly contribution:** Finalized Feedback service with complete comment threading and notification system implementation, completed final MongoDB integration with optimized query performance and data modeling, implemented comprehensive service monitoring and logging for production deployment, conducted final Docker configuration optimization and container resource management, completed final integration testing between Feedback service and other microservices.

- **Kirill Shumskiy (ML):**

**Closed issues (clickable):** Issue, Issue, Issue, Issue, Issue \
**Closed PR's (clickable):** PR, PR, PR \
**Weekly contribution:** Finalized code auto-grading system with complete model integration and Redis queue implementation, completed RAG system optimization with improved vector search performance and context relevance, implemented final chat assistant features including conversation history and context management, conducted final ML model testing and validation with comprehensive accuracy metrics, completed final ML service documentation including model architecture and training procedures, implemented production-ready inference endpoints with proper error handling and scaling.

- **Aleliya Turushkina (Designer / Frontend):**

**Figma board (clickable):** link \
**User Flow diagram (clickable):** link \
**Closed issues (clickable):** Issue, Issue, Issue, Issue, Issue, Issue \
**Closed PR's (clickable):** PR, PR, PR, PR \
**Weekly contribution:** Completed final UI/UX polish with comprehensive responsive design implementation and mobile optimization, finalized user interface consistency across all platform components with standardized design patterns, implemented final accessibility features including screen reader support and keyboard navigation, completed comprehensive user testing and feedback integration for optimal user experience, finalized design system documentation with component specifications and usage guidelines, implemented final theme system optimization and user preference persistence.

**More detailed descriptions of services and technical implementations can be found in the project repository link.**

## Plan for Next Week

**Post-Submission Activities:**

With the capstone project successfully completed and delivered, our focus shifts to final presentation preparation and potential project continuation planning.

**Final Presentation Preparation:**
- **Live Demo Rehearsal**: Multiple run-throughs of the complete user journey demonstration with backup scenarios
- **Technical Deep-Dive Preparation**: Detailed preparation for architecture questions and implementation discussions
- **Q&A Session Preparation**: Comprehensive preparation for questions about design decisions, scalability, and future enhancements
- **Presentation Timeline Management**: Strict timing rehearsal to ensure all key features are demonstrated within allocated time

**Project Continuation Assessment:**
- **Production Deployment Evaluation**: Assessment of current deployment readiness and production optimization requirements
- **Feature Roadmap Definition**: Documentation of planned future features and enhancement priorities
- **Open Source Preparation**: Evaluation of open-source release preparation including license selection and contribution guidelines
- **User Adoption Strategy**: Planning for potential user onboarding and platform growth strategies

**Knowledge Transfer & Documentation:**
- **Technical Knowledge Transfer**: Comprehensive documentation of all technical decisions and implementation details
- **Lessons Learned Documentation**: Detailed analysis of project challenges, solutions, and team insights
- **Maintenance Documentation**: Guidelines for ongoing platform maintenance and feature development
- **Team Retrospective**: Final team assessment of project success and individual growth throughout the capstone experience

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).