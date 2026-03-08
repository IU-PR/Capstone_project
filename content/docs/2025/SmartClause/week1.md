---
title: "Week #1"
---

# Week #1

## Project description

### Project name: *Smart Clause*

**Code repository**: https://github.com/IU-Capstone-Project-2025/SmartClause

Smart Clause is an AI-powered legal document analysis platformfocused on Russian legal market and legislation with a comprehensive chat-based document management system. The platform leverages RAG (Retrieval-Augmented Generation) technology with legal vector databases to provide intelligent document analysis and interactive consultation capabilities.

The MVP version focuses on single document upload and analysis with legal vector database verification, while the final version transforms into a chat-like web platform with document spaces where users can organize collections of preloaded documents and interact with them through conversational AI built on a dual RAG system.


### **Team Members**

| Team Member                             | Telegram Alias   | Email Address   | Track                                       | Responsibilities   |
|-----------------------------------------|------------------|-----------------|---------------------------------------------|--------------------|
| Alexander Malyy     | @narly651 | a.malyy@innopolis.university | Project Manager/Backend/ML | Team Organization (Meetings, Tasks), Product Vision, Code Reviews, Development of RAG and AI |
| Arthur Babkin            | @theother_archeee | a.babkin@innopolis.university | Backend/ML/Business Analytics | Market Analysis, RAG Microservices Development, R&D on RAG Systems for Legal Services |
| Vladimir Zhidkov            | @volodyavtg | v.zhidkov@innopolis.university | Backend/DevOps | Backend Development, Containerization and Orchestration (Docker), CI/CD Pipelines, Application Deployment |
| Ilsaf Abdulkhakov            | @haruyume | i.abdulkhakov@innopolis.university | Frontend/Design | UI/UX Design and Frontend Development |
| Nikita Tsukanov            | @Nikron_Becon | n.tsukanov@innopolis.university | Backend/ML/Business Analytics | Customer Development, RAG Microservices Development, Legal Databases Research and Parsing |


## Brainstorming

### Ideas during brainstorming

1. **Individual Contract Analysis Tool** - AI service for single contract review targeting non-legal professionals
2. **Mass Document Processing Platform** - Advanced clustering and analysis system for legal professionals handling multiple documents  
3. **Document Pipeline Automation** - Automated workflow for routine legal document processing

### Brief market research / problem validation

**Customer Development Insights:**

Through three rounds of customer interviews with practicing lawyers and law students, several key findings emerged:

**For Individual Users:**
- Occasional contract encounters (employment, NDAs) can be handled adequately by existing AI tools like ChatGPT
- Most complex contract types requiring careful review: NDAs and Intellectual Property agreements
- Mass market shows limited willingness to pay for single-use contract analysis

**For Legal Professionals:**
- Simple civil contracts: Issues are easily identifiable within one page of reading
- Large organizations: Already have dedicated legal teams for complex contract analysis
- Smaller firms: Documents are typically less complex and staff can quickly identify problems

**Competitive Landscape Analysis:**

**Key Competitors Identified:**
- **[No Roots](https://noroots.ru/)**: Direct Russian competitor with B2C focus, professional orientation, revenue of 74k rubles in 2024
- **[Embedica](https://embedika.ru/)**: B2B/B2G company with government contracts (482M from Ministry of Digital Development), custom solutions
- **[iUrist](https://айюрист.рф)**: Telegram bot with limited functionality, considered less serious competitor

**Key Market Opportunity:**
The research identified specific value in automated document clustering and anomaly detection for legal professionals who need to analyze large volumes of documents efficiently, with strong value proposition for automatic document grouping by semantic similarity, anomaly detection for non-standard contract terms, and significant time reduction in document review processes.


## Basic requirements

### Target users and their primary needs

**Primary Target:** Legal professionals and document analysts who need to process large volumes of documents efficiently
- **Need:** Efficient analysis and categorization of multiple contracts
- **Pain Point:** Manual sorting and risk identification across numerous documents

**Secondary Target:** Users with low legal qualification but frequent document interaction needs (freelancers, small business owners, contract managers)
- **Need:** Professional-level contract review without legal consultation costs
- **Pain Point:** Understanding complex legal language and identifying potential risks

### User stories

1. **As a corporate lawyer**, I want to automatically cluster similar contracts so that I can quickly identify anomalies requiring detailed review
2. **As a freelancer**, I want to upload an NDA and receive plain-language explanations of risks so that I can make informed decisions
3. **As a small business owner**, I want to verify contract compliance with regulations so that I can avoid legal issues
4. **As a legal professional**, I want to batch-analyze contract collections so that I can complete document reviews efficiently
5. **As a document analyst**, I want to chat about specific documents in my workspace so that I can get instant answers about risks and legal requirements

### Initial scope

**MVP Scope (Weeks 1-3):**
- Single document upload and analysis with legal vector database verification
- Risk identification and highlighting with plain language explanations
- Web interface inspired by NoRoots competitor design
- Compliance checking against Russian legal databases

**Final Product Scope (Weeks 4-6):**
- Chat-like web platform with document spaces
- Space-based document organization with background analysis
- Dual RAG system combining legal database search and user document collection search
- Interactive document consultation through conversational AI

## Tech-stack

**Frontend:** Vue, TypeScript, Vue Router, Pinia (maybe), Vite

**Backend:** Java (Spring), Python (FastAPI)

**Database:** PostgreSQL with pgvector extension for semantic search

**ML/AI:** Python: Langchain, Langgraph, 

**Infrastructure:** Docker containerization with docker-compose orchestration

## Business Model
- Individual document analysis (B2C)
- Professional subscriptions for space management (B2B)  
- Enterprise solutions for large document collections


## Market Analysis

### Market Size Assessment

**PAM (Potential Available Market)**: Global market for contract verification services targeting individuals who encounter contract review needs at least once annually
- Target Population: ~1.6 billion adults globally
- Average Service Price: $30 per review
- **PAM Size: $48 billion annually**

**TAM (Total Available Market)**: Russian market for contract analysis services
- Target Population: 65 million potential users in Russia
- Average Service Price: 2,000 rubles per review
- **TAM Size: 130 billion rubles annually**

**SAM (Serviceable Available Market)**: Online-accessible Russian market segment
- Target Population: 13 million users (20% of TAM)
- **SAM Size: 26 billion rubles annually**

**SOM (Serviceable Obtainable Market)**: Realistic market capture potential
- Year 1: 1% market share = **260 million rubles annually**
- Years 2-3: 3% market share = **780 million rubles annually**


**Market Context**: Legal document management software market valued at $1.9B (2022), projected to reach $4.73B by 2030 with 12.28% CAGR. AI contract analysis adoption growing rapidly due to 70% time reduction capabilities and enhanced compliance monitoring


# Weekly commitments

## Individual contribution of each participant

**Alexander Malyy:** 
- Organized and facilitated 3 team meetings for project planning and coordination
- Defined initial problem statement and project scope for Smart Clause platform
- Created and assigned initial task distribution across team members
- Conducted customer development interview with professional lawyer for market validation
- Compiled and authored Week 1 project report
- Led brainstorming sessions for idea generation and selection

**Arthur Babkin:**
- Validated and analyzed brainstormed project ideas against market viability
- Conducted initial market research and problem validation analysis
- Provided detailed analysis of target entrepreneurs' pain points and needs
- Contributed to competitive landscape assessment
- Supported customer development research methodology

**Vladimir Zhidkov:**
- Conducted comprehensive market size analysis (PAM/TAM/SAM/SOM calculations) (included in report)
- Performed detailed competitive analysis of key market players (NoRoots, Embedica, iUrist) (included in report)
- Analyzed target audience segments and their specific requirements (included in report)
- Contributed to tech stack selection and justification

**Ilsaf Abdulkhakov:**
- Created initial boilerplate project architecture and repository structure ([commit #1](https://github.com/IU-Capstone-Project-2025/SmartClause/commit/e85fc8f50f9c6f351911b1369e355b23f660101b), [commit #2](https://github.com/IU-Capstone-Project-2025/SmartClause/commit/950760bcf3cf9ea76bd41261acb88e80860801d8))
- Analyzed competitors' UI/UX designs and interface approaches (NoRoots, Embedica)
- Defined and justified frontend technology stack selection (Vue, TypeScript, etc.)
- Established project development environment and initial setup 

**Nikita Tsukanov:**
- Organized and conducted customer development interviews with 2 law students
- Provided in-depth analysis of legal professionals' pain points and workflow challenges
- Researched and identified initial legal databases and data sources for RAG implementation (Consultant Plus, etc.)
- Contributed to ML/AI technology stack selection and approach definition
- Analyzed technical requirements for legal document processing and vectorization

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).
