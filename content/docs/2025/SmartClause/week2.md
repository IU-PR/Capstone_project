---
title: "Week #2"
---

# **Week #2**

## Detailed Requirements Elaboration
### **User stories for MVP**
1. **Frelancer**:
    - *Motivation*: Protecting professional interests and minimizing legal risks when working with clients.
    - *Pain*: Lack of legal knowledge, disputes with clients, payment delays, unclear project boundaries, fear of fraud.
    - *Needs*: Fast contract review, identification of dangerous clauses, clear recommendations, copyright protection.
    - *Expectations*: Intuitive interface, fast analysis, specific recommendations in plain language, support for different types of contracts.
    - *Features*: Limited budget, high workload, irregular income, working with different types of clients.
    - *Key areas of analysis*: Payment terms, intellectual property rights, scope of work, deadlines and penalties, contract termination, confidentiality.
2. **Small business owner**
    - *Motivation*: Protection of business when working with clients and contractors.
    - *Disadvantages*: Lack of legal education, fear of unscrupulous partners, lengthy negotiation of terms.
    - *Needs*: Quick check, identification of weaknesses, recommendations on how to improve the contract.
    - *Expectations*: The service should be simple, provide clear recommendations, help avoid mistakes and protect business interests.
    - *Features*: Limited budget, high workload, need to save time.
3. **Tenants/Landlords**
    - *Motivation*: Minimization of risks when renting/leasing housing or office.
    - *Pain*: Lack of legal literacy, fear of fraud, lack of accessible and cheap legal advice.
    - *Needs*: Simplicity, speed, affordable cost, clear explanations.
    - *Expectations*: Service should be intuitive, provide clear advice, highlight risks and explain complex points.
    - *Features*: Not ready to pay a lot of money for services, value convenience and accessibility.
4. **Procurement and Tender Departments**
    - *Motivation*: Optimization of work with suppliers, reduction of risks when concluding contracts, acceleration of procurement processes.
    - *Pain*: Passage of disputable or unfavorable conditions due to lack of legal expertise at all stages, the need to quickly check a large number of documents.
    - *Needs*: Automatic audit of contract terms, quick search for non-standard wording, screening of potential risks.
    - *Expectations*: The service should provide a summary of key differences, support work with large amounts of data, be easy to use.
    - *Features*: Working with documents from different suppliers, the need to comply with internal standards, high responsibility for each decision.

### **Acceptance criteria**
1. **Document Upload**
- *Given*: user is in space
- *When*: user uploads a PDF or DOC file up to 10 pages
- *Then*: the file is successfully uploaded in 5 seconds

2. **Analyzing the document**
- *Given*: document is uploaded
- *When*: user begins chat with the system
- *Then*: the system already has the document in the database and can answer the user's question

3. **Displaying the results**
- *Given*: analysis is completed
- *When*: user opens analyzed document
- *Then*: he/she can see:
    - List of problems found
    - Risk level for each problem (high/medium/low)
    - Simple explanation of each problem.

4. **Basic checks**
- *Given*: user is in space
- *When*: user asks the system to check the document
- *Then*: the system checks:
    - *Payment terms*
    - *Due dates*
    - *Termination terms*

5. **Errors**
- *Given*: user uploads an unsupported file
- *When*: the system processes the request
- *Then*: a clear error message is displayed.

## Prioritized backlog
![Backlog](https://github.com/IU-Capstone-Project-2025/SmartClause/blob/main/course-metadata/week2-images/backlog.png)

### Sprint analysis
![Sprint-2](https://github.com/IU-Capstone-Project-2025/SmartClause/blob/main/course-metadata/week2-images/sprint-2-analysis.png)

### Tasks for the next week
![Sprint-3](https://github.com/IU-Capstone-Project-2025/SmartClause/blob/main/course-metadata/week2-images/sprint-3.png)

## Project specific progress

### User flow diagram
![User flow diagram](https://github.com/IU-Capstone-Project-2025/SmartClause/blob/main/course-metadata/week2-images/userflow.png)

### Design
The platform provides a complete web interface with three main screens:
1. **Upload Screen**: Drag-and-drop interface for document upload.
2. **Processing Screen**: Real-time processing status with progress indicators.
3. **Results Screen**: Comprehensive analysis results with risks and recommendations.

### Frontend
- **Technology**: Vue.js 3 with modern UI components and routing.
- **User Interface**: A full web application with a complete UI workflow for document analysis, featuring:
    - A smart upload interface with drag-and-drop and progress tracking.
    - A real-time processing screen with status updates.
    - A comprehensive results screen with detailed analysis.
- **Architecture**: The frontend is a Vue.js Single Page Application (SPA) running on port 8080.

![pic3](https://github.com/IU-Capstone-Project-2025/SmartClause/blob/main/course-metadata/week2-images/pic3.png)

![pic4](https://github.com/IU-Capstone-Project-2025/SmartClause/blob/main/course-metadata/week2-images/pic4.png)

![pic5](https://github.com/IU-Capstone-Project-2025/SmartClause/blob/main/course-metadata/week2-images/pic5.png)

### Backend
- **Technology**: Spring Boot, PostgreSQL with pgvector, and Docker Compose.
- **Architecture**:
    - **Backend API (port 8000)**: A Spring Boot application that handles document uploads and orchestrates the analysis pipeline.
    - **Database (port 5432)**: PostgreSQL with the `pgvector` extension for vector similarity search.
- **Key Features**:
    - **REST API**: Comprehensive endpoints with Swagger documentation.
    - **Docker Deployment**: Fully containerized for easy setup.
    - **Error Handling**: Includes robust validation and user feedback.

### ML
- **Technology**: FastAPI, LangChain, OpenRouter, and BAAI/bge-m3 embeddings.
- **Architecture**:
    - **Analyzer Microservice (port 8001)**: A FastAPI service providing endpoints for analysis, retrieval, and embedding. It contains the RAG pipeline.
- **AI Capabilities**:
    - **AI-Powered Analysis**: Leverages LLM for in-depth legal document review.
    - **Legal Knowledge Base**: A vector database of over 4,400 Russian Civil Code articles.
    - **Semantic Search**: Vector-based search with configurable distance functions (cosine, L2, inner product).


# Weekly commitments

## Individual contribution of each participant

**Alexander Malyy:** 
- Define API endpoints for MVP [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/9)
- Initialize database schema [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/10)
- Implement RAG functionality [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/18)
- Implement analysis of the document point by point [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/23)
- Fix the issues with the frontend [(pull request)](https://github.com/IU-Capstone-Project-2025/SmartClause/pull/58)

**Arthur Babkin:**
- Create a parser of Russian Legal Database [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/6)
- Defined database schema

**Vladimir Zhidkov:**
- Setup Java backend service for routing between ML microservices and Frontend [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/7)
- Сonfigure docker [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/32)
- Implement swagger documentation [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/35)
- Analyse user stories in more details [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/56)
- Analyze acceptance criteria [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/57)
- Wrote report to week2

**Ilsaf Abdulkhakov:**
- Set up the frontend project structure [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/3)
- Create a user-flow diagram for MVP [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/14)
- Link frontend and backend [(pull request)](https://github.com/IU-Capstone-Project-2025/SmartClause/pull/55)

**Nikita Tsukanov:**
- Inspect and analyze the thesis provided by Albert [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/12)
- Defined the initial RAG architecture


## Plan for Next Week

### Frontend

- Implement final version of frontend
- Link frontend and backend

### Backend

- Implement message broker
- Deploy mvp version of project

### ML

- Experiment and provide report on different document chunking techniques
- Create an assessment data and criteria
- Research better retrieve techniques and analyze the results
- Research and analyze different approaches for better query construction

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).
