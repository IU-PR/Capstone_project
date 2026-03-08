---
title: "Week #4"
---

# **Week #4**

## Testing and QA

We made unit tests for backend and frontend and integrational tests for backend

### Evidence of test execution

![unit-test](https://github.com/FluentlyOrg/Fluently-fork/blob/feature/refactor-struct/report-imges/unit-tests.png?raw=true)

## CI/CD

### Setup and Architecture

The project implements a complex CI/CD pipeline using **GitHub Actions** with environment-specific deployments. The main configuration is located at:

- **Main CI/CD Configuration**: [deploy.yml](https://github.com/FluentlyOrg/Fluently-fork/blob/main/.github/workflows/deploy.yml)
- **Docker Configuration**: [docker-compose.yml](https://github.com/FluentlyOrg/Fluently-fork/blob/main/docker-compose.yml)

### Pipeline Structure

The CI/CD pipeline consists of two main jobs:

1. **Setup Job**: Environment determination and configuration

   - Automatically determines deployment environment based on branch:
     - `main` branch → Production environment (`fluently-app.ru`)
     - `develop/feature/fix` branches → Staging environment (`fluently-app.online`)
   - Sets environment-specific variables (domains, SSH credentials, ZeroTier IPs)
   - Supports manual environment override and rollback functionality

2. **Deploy Job**: Application deployment and health verification
   - Code synchronization with GitHub repository
   - Environment-specific configuration generation
   - Docker container orchestration
   - Comprehensive health checks
   - Automatic rollback on failure

### Tools and Technologies Used

- **CI/CD Platform**: GitHub Actions
- **Containerization**: Docker & Docker Compose
- **Deployment**: SSH-based deployment using `appleboy/ssh-action`
- **Configuration Management**: Environment variable substitution (`envsubst`)
- **Reverse Proxy**: Nginx with SSL termination
- **SSL/TLS**: Cloudflare Origin Certificates for end-to-end encryption
- **Networking**: ZeroTier for secure server access
- **Monitoring**: Built-in health checks for all services

### Advanced Features

- **Template-based Configuration**: Dynamic generation of environment-specific files
  - Nginx configuration templates
  - Backup script templates
  - Environment-specific variable substitution
- **Automated Backup System**: Pre-deployment backups with automatic cleanup
- **Rollback Capability**: Automatic and manual rollback functionality
- **Health Monitoring**: Multi-service health checks with timeout handling
- **Security**: ZeroTier VPN integration for secure server communication

### Challenges Faced

1. **Complex Service Dependencies**: Managing startup order and health checks for ML API, PostgreSQL, and backend services
2. **Configuration Management**: Avoiding file duplication through template-based approach
3. **Long Build Times**: ML API container builds required careful timeout handling
4. **Network Conflicts**: Docker network cleanup to prevent deployment conflicts
5. **SSL Certificate Management**: Cloudflare Origin Certificate integration for multiple domains

### Links to CI/CD configuration files

- **Main CI/CD Configuration**: [deploy.yml](https://github.com/FluentlyOrg/Fluently-fork/blob/main/.github/workflows/deploy.yml)
- **Docker Configuration**: [docker-compose.yml](https://github.com/FluentlyOrg/Fluently-fork/blob/main/docker-compose.yml)

## Deployment

### Staging

**Domain**: `fluently-app.online`  
**Server**: Ubuntu 24.04 LTS VDS staging server with dedicated staging user

#### Environment Setup

- **Branch Strategy**: All non-main branches (`develop`, `feature/*`, `fix/*`) deploy to staging
- **Directory Structure**: `/home/deploy-staging/Fluently-fork`
- **Backup Location**: `/home/deploy-staging/backups`
- **Network Access**: ZeroTier VPN for secure remote access

#### Deployment Process

1. **Pre-deployment**: Current state backup creation
2. **Code Update**: Git fetch, checkout, and pull latest changes
3. **Configuration**: Environment-specific `.env` file generation
4. **Template Processing**: Dynamic configuration file generation using `envsubst`
5. **Container Orchestration**: Docker Compose build and deployment
6. **Health Verification**: Multi-service health checks
7. **Cleanup**: Old Docker image removal and backup management

#### Services Architecture

- **Backend API**: Go-based REST API with Swagger documentation
- **ML API**: Python-based machine learning service with HuggingFace models
- **PostgreSQL**: Database with health checks and optimized configuration
- **Nginx**: Reverse proxy with SSL termination
- **Directus CMS**: Content management system
- **Monitoring Stack**: Prometheus, Grafana, Loki for observability

### Production

**Domain**: `fluently-app.ru`  
**Server**: Ubuntu 24.04 LTS Production VDS with dedicated production user

#### Environment Setup

- **Branch Strategy**: Only `main` branch deploys to production
- **Directory Structure**: `/home/deploy/Fluently-fork`
- **Backup Location**: `/home/deploy/backups`
- **SSL/TLS**: Cloudflare Origin Certificates with Full (Strict) SSL mode
- **Network Access**: ZeroTier VPN for secure remote access

#### Production-Specific Features

1. **Enhanced Backup Strategy**:

   - Automatic pre-deployment backups
   - Retention policy (last 5 backups)
   - Rollback capability with state restoration

2. **SSL/TLS Security**:

   - Cloudflare Origin Certificates for end-to-end encryption
   - HSTS headers and security configurations
   - Certificate management for `fluently-app.ru`

3. **Performance Optimizations**:

   - PostgreSQL tuned for production workloads
   - Docker BuildKit for faster builds
   - Resource limits and reservations for ML services

4. **Monitoring and Observability**:
   - Prometheus metrics collection
   - Grafana dashboards
   - Loki log aggregation
   - cAdvisor for container metrics
   - Node exporter for system metrics

#### VDS Setup and Infrastructure

- **Operating System**: Ubuntu 24.04 LTS
- **Network**: ZeroTier mesh network for secure access
- **SSL Certificates**: Cloudflare Origin Certificates managed automatically
- **Docker**: Latest Docker Engine with Compose V2
- **Storage**: External Docker volumes for data persistence
- **Backup Strategy**: Automated backup scripts with cron scheduling

#### Security Measures

- **Network Isolation**: ZeroTier VPN for all administrative access
- **SSL/TLS**: Full (Strict) SSL mode with Cloudflare
- **Container Security**: Non-root containers where possible
- **Secret Management**: Environment-specific secrets via GitHub Actions
- **Access Control**: Dedicated deployment users with minimal privileges

## Vibe Check

All members of the team are satisfied with team workflow
The recomendations that suggest members are:

- Have more team meetings for clarification of some unclear moments
- Write more complete structure of issues

# Weekly commitments

## Individual contribution of each participant

### Danila Kochegarov (Team Lead & Backend Developer)

- [Wrote filling database go script](https://github.com/FluentlyOrg/Fluently-fork/pull/173)
- [Wrote clearing database go script](https://github.com/FluentlyOrg/Fluently-fork/pull/173)
- [Made docker compose centralized so now it composes all services from root: ML, backend, postgres, directus, grafana, loki, promtail, exporters for prometheus, nginx, prometheus, cadvisor](https://github.com/FluentlyOrg/Fluently-fork/pull/160)
- Start developing Telegram bot

### Savva Ponomarev (iOS Developer & Project Manager)

- Wrote Report
- Organize retrospective
- Wrote Unit-tests for Network layer
- Integrate backend to iOS app
- Made new screens:
  - Dicrionary screen: dictionary of all learned words
  - Launch screen: screen that is shown on launching
  - Draft screens for
    - Diary
    - Non-learned words
- refactor code, due to new structs (lessons) on backend

### George Selivanov (System Analyst)

- Together with Anton, a system for selecting relevant words based on a thesaurus was developed and implemented, the basis for which is the same dataset as for generating tasks
- Various LLMs were selected and tested to implement work with user dialog training

### Timofey Ivlev (DevOps Engineer)

#### **Core Setup**

- **GitHub Actions** for CI/CD, with environment-specific deployments (staging/production).
- **Key Files**: `deploy.yml` (main workflow), `docker-compose.yml` (container orchestration).

#### **Pipeline Flow**

1. **Setup Job**

   - Auto-detects environment based on branch (`main` → production, others → staging).
   - Configures variables (domains, SSH, ZeroTier IPs) and supports manual overrides.

2. **Deploy Job**
   - Syncs code, generates configs, manages Docker, runs health checks, and auto-rolls back on failure.

#### **Key Tools & Features**

- **Docker** for containerization, **Nginx** for reverse proxy, **Cloudflare SSL** for security.
- **ZeroTier VPN** for secure server access, **automated backups**, and **template-based configs** (envsubst).
- **Multi-service health checks** with rollback capability.

#### **Environments**

- **Staging** (`fluently-app.online`): Non-`main` branches, automated backups, isolated directory structure.
- **Production** (`fluently-app.ru`): `main` branch only, enhanced backups, Cloudflare SSL, performance tuning.

#### **Challenges Solved**

- Complex service dependencies (ML API, PostgreSQL).
- Docker network conflicts, long build times, SSL management.
- Secure deployments via ZeroTier and least-privilege access.

#### Also

- Fixed issues with Sonarqube: [link to issue](https://github.com/FluentlyOrg/Fluently-fork/issues/141)
- Added backup scripts for most essential Fluently services
  https://github.com/FluentlyOrg/Fluently-fork/pull/165

### Anton Korotkov (ML Engineer)

- Developing the word selection model itself
  - developing
  - fine-tuning
- The model can currently select suitable words for training, they are linked to:
  - topic
  - subtopic
  - subsubtopic
- Also ranked by :
  - popularity
  - difficulty
- The number of recommended words can be parametrically set to optimize the selection. Each word also has a "reason" for which it was suggested

### Daniil Tskhe (Backend Developer)

- Helped with csv parsing
- Wrote full testing of CRUD operations for models in the repository
- Wrote Unit-tests to check the validity of endpoints that work with models from the repository
- Wrote Integration-tests for http handlers

### Evgeniy Bortsov (Android Developer)

- Configured serialization/deserialization of messages from the server
- Added integration with backend
- Configured caching of user progress
- Made new screens:
  - Type word Exercise
- Added event logging

## Plan for Next Week

- Finalize backend integration with frontend
- Fixing BERT algorithm
- Collect user feedback
- Start developing SPA (Single Page Application)

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
