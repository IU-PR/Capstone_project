---
title: "Week #3"
---

# **Week #3**

## Implemented MVP features

### Complete AI-Powered Legal Document Analysis Platform

**SmartClause** is a fully functional MVP that provides comprehensive legal document analysis capabilities focused on the Russian legal market. The platform leverages RAG (Retrieval-Augmented Generation) technology with legal vector databases.

#### Core Implemented Features:

**Document Upload and Analysis Pipeline**
- **Smart Upload Interface**: Drag-and-drop document upload with progress tracking (up to 10MB files)
- **AI-Powered Risk Analysis**: Comprehensive legal document analysis for risks, compliance issues, and recommendations
- **Detailed Results**: Analysis with causes, risks, and actionable recommendations
- **Multiple File Format Support**: Text files and structured documents

**Semantic Legal Search Engine**
- **Vector-based Search**: Natural language queries against comprehensive Civil Code database
- **Chunked Database**: 190,000+ legal rules with 413,000+ optimized text chunks
- **BAAI/bge-m3 Embeddings**: 1024-dimensional vectors for high-quality semantic understanding
- **Configurable Retrieval**: Multiple distance functions (cosine, L2, inner product)
- **Advanced Retrieval Techniques**: Vector Search together with BM25 via Reciprocal Rank Fusion
- **Structured Metadata**: Articles organized by sections, chapters, and legal references

**Complete Web Application**
- **Vue.js 3 Frontend**: Modern responsive UI with three main screens:
  - Upload Screen: Intuitive document upload interface
  - Results Screen: Comprehensive analysis results presentation
- **Full User Journey**: Complete workflow from document upload to detailed analysis results

**REST API Integration**
- **Spring Boot Backend** (Port 8000): Document processing and orchestration
- **FastAPI AI Service** (Port 8001): RAG pipeline and LLM integration
- **Swagger Documentation**: Interactive API documentation at `/docs`
- **Comprehensive Endpoints**: Document analysis, semantic search, embedding generation

**Production-Ready Infrastructure**
- **Docker Compose Orchestration**: Complete service deployment with one command
- **PostgreSQL with pgvector**: Vector similarity search capabilities
- **Error Handling**: Comprehensive validation and user feedback
- **Performance Optimization**: Concurrent processing and retry mechanisms

#### Functional User Journey:

1. **Document Upload**: User drags and drops legal document onto web interface
2. **Processing Initiation**: System validates file and begins analysis pipeline
3. **Real-time Feedback**: User sees live processing status with progress updates
4. **AI Analysis**: Document analyzed using RAG with legal knowledge base
5. **Results Presentation**: Comprehensive analysis with risks and recommendations displayed

## Demonstration of the working MVP

![MVP Demo](https://github.com/IU-Capstone-Project-2025/SmartClause/blob/course-metadata/course-metadata/week3/mvp-demo.mp4)

**🌐 Live Demo**: Platform deployed and accessible at [SmartClause](http://158.160.190.57:8080/)

### API Documentation

#### Analyzer API (Port 8001)
- **GET /health**: Health check with database connectivity status
- **POST /api/v1/retrieve-chunk**: Semantic document chunk retrieval
- **POST /api/v1/retrieve-rules**: Semantic retrieval of unique legal rules
- **POST /api/v1/analyze**: Legal document analysis with risk assessment
- **POST /api/v1/embed**: Text embedding generation
- **GET /api/v1/metrics/retrieval**: Embedding quality metrics

#### Backend API (Port 8000)
- **POST /api/v1/get_analysis**: Document upload and analysis orchestration
- **GET /api/v1/health**: Service health check

## ML

### Model Architecture

**Embedding Model: BAAI/bge-m3**
- **Model Type**: Multilingual sentence transformer optimized for semantic similarity
- **Embedding Dimension**: 1024-dimensional vectors
- **Language Support**: Multilingual with strong Russian language capabilities
- **Use Case**: Converting legal text chunks into semantic vectors for similarity search

**LLM: Google Gemini 2.5 Flash**
- **Integration**: Via OpenRouter API for analysis generation
- **Purpose**: Legal document analysis, risk assessment, and recommendation generation
- **Configuration**: Optimized for legal domain with structured prompt engineering

### Embedding Generation Process

**Legal Knowledge Base**:
- **Dataset**: Complete Russian Civil Code with comprehensive legal rules
- **Scale**: 190,846 legal rules processed into 413,453 text chunks
- **Chunking Strategy**: 800-character chunks with 500-character overlap for comprehensive coverage
- **Processing Pipeline**: Rules → Chunks → Embeddings → Vector Database

**Embedding Generation Process**:
```bash
# Batch processing for efficiency
Batch Size: 50-200 chunks per batch
Model: BAAI/bge-m3
Dimension: 1024
Processing: ~413k chunks with concurrent batch processing
```

**Vector Database Configuration**:
- **Storage**: PostgreSQL with pgvector extension
- **Indexing**: Optimized vector storage with efficient similarity search capabilities

### Retrieval System

**Hybrid Retrieval Architecture**:
- **Vector Search**: Semantic similarity search using configurable distance functions (cosine, euclidean, dot product)
- **BM25 Integration**: Traditional keyword-based search for exact term matching
- **Fusion Strategy**: Reciprocal Rank Fusion (RRF) combining vector and BM25 results for optimal relevance

### Data Processing Scripts

**Link to processing code**: `analyzer/scripts/process_and_upload_datasets.py`

**Key Processing Features**:
- Unified script for embedding generation and database upload
- Batch processing with memory optimization
- Concurrent embedding generation
- Progress tracking and error handling
- Flexible configuration for different deployment scenarios

### Model Artifacts

**Generated Artifacts**:
- **`chunks_with_embeddings.csv`** [link](https://github.com/IU-Capstone-Project-2025/SmartClause/blob/main/analyzer/scripts/datasets/chunks_with_embeddings.csv): ~1GB file with pre-generated embeddings (stored via Git LFS)
- **Vector Database**: PostgreSQL tables with indexed embeddings for fast retrieval
- **Metadata Storage**: Complete rule hierarchy and chunk relationships

**Model Performance**:
- **Embedding Quality**: Optimized for legal domain semantic understanding
- **Retrieval Speed**: Sub-second response times for similarity search
- **Scalability**: Handles 400k+ vectors with efficient indexing

## Internal demo

### Demo Results and Feedback

**Successfully Demonstrated**:
- Complete end-to-end document analysis workflow
- Semantic search capabilities with relevant legal code retrieval

**Key Strengths Identified**:
- Intuitive user interface with clear workflow
- Fast and relevant semantic search results
- Comprehensive legal analysis output

**Areas for Future Enhancement**:
- User authentication and document history
- Interactive chat interface for legal consultation

**Technical Performance**:
- Platform handles large legal documents efficiently
- Vector search provides relevant legal code matches
- AI analysis generates comprehensive risk assessments
- System demonstrates production-ready stability

# Weekly commitments

## Individual contribution of each participant

**Alexander Malyy:** 
- Reviewed team's work and merged PRs
- Optimized processing part (batch processing, async, concurrency, caching) [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/77)
- Co-authored in [PR #86](https://github.com/IU-Capstone-Project-2025/SmartClause/pull/86) and [PR #89](https://github.com/IU-Capstone-Project-2025/SmartClause/pull/89)
- Created a report for week 3

**Arthur Babkin:**
- Expanded legal dataset [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/80)
- Optimized prompt for LLM [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/78)
- Experimented and provided report on different document chunking techniques [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/25)

**Vladimir Zhidkov:**
- Deployed the MVP [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/20)

**Ilsaf Abdulkhakov:**
- Fixed frontend issues [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/79) and [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/76)
- Updated views [(PR)](https://github.com/IU-Capstone-Project-2025/SmartClause/pull/88)
- Recorded demo

**Nikita Tsukanov:**
- Researched better retrieve techniques and analyzed the results [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/27)
- Created an assessment data and criteria [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/26)

## Plan for Next Week

**Priority Tasks**:
1. **Message broker**: Implement message broker for communication between microservices
2. **Finalize user flow**: Define user flow for the final product
3. **Design the final UI/UX**: Design the final UI/UX for the final product
4. **User Authentication**: Implement user registration and login system

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).
