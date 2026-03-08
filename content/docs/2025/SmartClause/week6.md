---
title: "Week #6"
---

# **Week #6**

## Links

- **Deployment**: https://smartclause.ru/
- **API Docs**: https://github.com/IU-Capstone-Project-2025/SmartClause/blob/main/docs/README.md
- **Demo**: [link](https://drive.google.com/file/d/1yOBGLbs4Fp3S2_oiYeAQGPmEVDwGJt1b/view?usp=sharing)
- **Repository**: https://github.com/IU-Capstone-Project-2025/SmartClause

## Final deliverables

### Project overview

SmartClause is a comprehensive AI-powered legal document analysis platform focused on the Russian legal market. The platform leverages RAG (Retrieval-Augmented Generation) technology with legal vector databases to provide intelligent document analysis and interactive legal consultation capabilities. 

**Key Problems Solved:**
- **Document Risk Analysis**: Automated identification of legal risks, compliance issues, and unfavorable terms in contracts
- **Legal Consultation**: Interactive AI assistant providing professional-level legal advice with conversation memory
- **Knowledge Access**: Semantic search through Russian legal rules with natural language queries
- **User Workflow**: Complete document processing pipeline from upload to detailed analysis and consultation

**Target Users:** Legal professionals, freelancers, small business owners, and individuals who need professional contract review without expensive legal consultation fees.

### Features

**Core Implemented Features:**
- **🔐 Secure User Authentication**: JWT-based registration and login with encrypted password storage
- **📄 AI Document Analysis**: Upload legal documents (up to 10MB) and receive comprehensive risk analysis with causes, recommendations, and severity ratings
- **💬 Interactive Legal Chat**: AI-powered legal assistant with conversation memory, document-aware responses, and legal context integration
- **🔍 Semantic Legal Search**: Vector-based search through 413,000+ legal text chunks using combined semantic and BM25 retrieval
- **📊 Risk Visualization**: Traffic-light risk assessment system with detailed explanations
- **📁 Document Spaces**: Organize documents in private workspaces with background analysis
- **📋 Export Capabilities**: Download analysis results as PDF reports
- **🌐 Modern Web Interface**: Vue.js responsive UI with drag-and-drop upload, real-time processing status, and chat interface
- **🔒 Rate Limiting**: API abuse prevention with tiered access (anonymous vs authenticated users)
- **🌍 Internationalization**: Multi-language support (English/Russian) interface

**Legal Knowledge Base:**
- 190,846 Russian Civil Code rules with complete metadata
- 413,453 optimized text chunks with BAAI/bge-m3 embeddings (1024 dimensions)
- Structured hierarchical organization with sections, chapters, and legal references
- Dataset is uploaded to the Hugging Face for public access

### Tech stack

**Frontend:**
- Vue.js 3 with TypeScript and Vue Router
- Modern responsive UI with Vite build system
- Real-time status updates and interactive components

**Backend:**
- Java Spring Boot API Gateway (main orchestration service)
- Python FastAPI Analyzer microservice (RAG pipeline and LLM integration)
- Python FastAPI Chat microservice (legal consultation with memory management)

**Database & Storage:**
- PostgreSQL with pgvector extension for vector similarity search
- Optimized database structure with rules metadata and searchable chunks

**AI & ML:**
- Google Gemini 2.5 Flash via OpenRouter for analysis and chat generation
- BAAI/bge-m3 sentence transformers for semantic embeddings
- Vector search with cosine similarity and BM25 hybrid retrieval

**Infrastructure:**
- Docker containerization with multi-service Docker Compose orchestration
- Jenkins CI/CD pipeline with automated deployment
- Apache reverse proxy configuration
- SSL certificate integration for secure connections

**Development Tools:**
- Swagger/OpenAPI documentation for all services
- Comprehensive error handling and validation
- Memory-optimized batch processing for large datasets

### Setup instructions

**Prerequisites:**
- Docker and Docker Compose installed
- Python 3.11+
- OpenRouter API key ([Get one here](https://openrouter.ai/))
- 8GB+ RAM recommended for embedding processing

**Step-by-step setup:**

1. **Clone Repository**
```bash
git clone https://github.com/IU-Capstone-Project-2025/SmartClause.git
cd SmartClause
```

2. **Download Legal Datasets** (~1.2GB total)
```bash
python analyzer/scripts/download_datasets.py
```

3. **Configure Environment**
```bash
# Copy environment templates
cp analyzer/env.example analyzer/.env
cp chat/env.example chat/.env

# Edit both .env files and add your OpenRouter API key and jwt secret
# Replace 'your_openrouter_api_key_here' with actual key
# Replace 'your_jwt_secret_here' with actual secret
```

4. **Launch Platform**
```bash
# Build and start all services (first launch ~10-15 minutes)
docker-compose up --build -d

# Monitor startup process
docker-compose logs -f
```

5. **Initialize Database and Load Legal Dataset**
```bash
# Load complete legal dataset (413k+ chunks with embeddings)
docker-compose exec analyzer python scripts/process_and_upload_datasets.py --upload --clear
```

6. **Access the Application**
- **Web Interface**: http://localhost:8080
- **Backend API**: http://localhost:8000/swagger-ui/index.html
- **Analyzer API**: http://localhost:8001/docs
- **Chat API**: http://localhost:8002/docs

**Production Deployment:**
The platform is deployed using Jenkins CI/CD pipeline with automated builds and deployments to production server via SSH. SSL certificates and domain configuration are managed through the deployment infrastructure.

## Presentation draft

[Presentation draft](https://docs.google.com/presentation/d/1tF4KNoouJt-mmnjW1wl2iqwprQXyS9qW_t34cSdsc7U/edit?usp=sharing)

## Deployment

### Staging

**Staging Environment Process:**

Our staging environment serves as a testing ground before production deployment, ensuring code quality and stability through automated testing and manual validation.

**Infrastructure Setup:**
- **Environment**: Local development servers and Docker containers
- **Purpose**: Pre-production testing, feature validation, and integration testing
- **Configuration**: Mirrors production setup but with test databases and mock external services

**Staging Pipeline:**
- **Trigger**: Pull requests and feature branch merges to develop branch
- **Process**:
  1. Automated tests run on microservices (Python analyzer service and Java backend service)
  2. Docker images built with staging configuration
  3. Services deployed to staging environment
  4. Integration tests executed
  5. Manual testing and validation performed
  6. Performance and security checks conducted

**Testing Environment:**
- **Database**: Isolated test database with sample data
- **External Services**: Mock APIs and test configurations
- **Monitoring**: Basic logging and health checks for validation
- **Access Control**: Limited access for development team and stakeholders

### Production

**Production Deployment Process:**

Our production environment is hosted on **Yandex Cloud** using a Virtual Dedicated Server (VDS) instance with fully automated CI/CD pipeline through Jenkins.

**Infrastructure Setup:**
- **Cloud Provider**: Yandex Cloud VDS (158.160.190.57)
- **Operating System**: Ubuntu 22.04 LTS
- **Domain**: Purchased and managed through reg.ru
- **SSL Certificate**: SSL certificate obtained and configured for secure HTTPS connections
- **Reverse Proxy**: Apache HTTP Server configured as a reverse proxy to route traffic to containerized services

**CI/CD Pipeline (Jenkins):**
- **Trigger**: Pushes and merges to main branch automatically trigger deployment
- **Automated Pipeline Stages**:
  1. **Checkout**: Jenkins pulls latest code from repository
  2. **Parallel Testing**: 
     - Python Service: Tests analyzer microservice using Python 3.11 container with cached dependencies
     - Java Service: Tests backend microservice using Maven 3.9.6 with Eclipse Temurin 21
  3. **Auto-Deploy**: Upon successful tests, automatic deployment to production server via SSH
     - Fetches latest main branch code
     - Builds frontend using custom build script
     - Recreates Docker containers with latest images
     - Ensures zero-downtime deployment

**Production Environment Configuration:**
- **Containerization**: All services run in Docker containers orchestrated by docker-compose
- **Network Security**: Apache proxy handles external traffic, internal services communicate through Docker network
- **SSL Termination**: Apache handles SSL termination, ensuring encrypted connections
- **Port Management**: Only necessary ports (80, 443) exposed externally, internal services isolated
- **Automated Deployment**: SSH-based deployment with key authentication for secure access

**Public Access:**
- **Domain**: Custom domain name registered through reg.ru
- **SSL**: Full SSL/TLS encryption enabled for all communications
- **High Availability**: Production server configured for stable 24/7 operation with automated deployment pipeline

# Weekly commitments

## Individual contribution of each participant

**Alexander Malyy:** 
- Added summary of the analysis to the report ([issue](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/129))
- Linked domain name and added SSL certificate ([issue](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/130))
- Improved risks display in analysis results by sorting them by severity ([issue](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/138))
- Implemented dataset chunks preprocessing for RAG pipeline ([issue](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/143))
- Closed opened docker ports for security reasons ([issue](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/144))
- Added rate limit for API requests to prevent abuse ([issue](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/155))
- Created a report for week 6

**Arthur Babkin:**
- Further improved analysis validation pipeline and decreased API calls ([pr](https://github.com/IU-Capstone-Project-2025/SmartClause/pull/145))
- Parsed Constitution of the Russian Federation to extend dataset for RAG pipeline ([issue](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/133))
- Recorded demo video

**Vladimir Zhidkov:**
- Impelemnted autodeploy and improved CI/CD pipeline ([issue](https://github.com/IU-Capstone-Project-2025/SmartClause/pull/149))

**Ilsaf Abdulkhakov:**
- Implemented language switch for interface ([issue](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/137))
- Improved UX/UI aspects and applied fixes for the frontend ([issue](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/141), [pr](https://github.com/IU-Capstone-Project-2025/SmartClause/pull/156))

**Nikita Tsukanov:**
- Conducted comprehensive analysis of current RAG pipeline and proposed future improvements ([issue](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/119))

## Plan for Next Week

- Presentation

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x\] In working condition.
- [x\] Run via docker-compose (or another alternative described in the `README.md`).
