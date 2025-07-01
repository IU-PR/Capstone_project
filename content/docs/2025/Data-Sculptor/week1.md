## Project description

### Project name: Data Sculptor

**Code repository**: https://github.com/IU-Capstone-Project-2025/Data-Sculptor

> **Problem Statement**
> Providing expert human feedback when validating practice cases of ML&DS students is extremely expensive and time-consuming on scale

> **Solution**
> Automate 90% of feedback providing tasks to enable cheap, fast, yet still reliable validation by retaining 10% engagement of human experts

### **Team Members**

| Team Member       | Telegram Alias  | Email Address                       | Track                  | Responsibilities                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------- | --------------- | ----------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dmitriy Prokopyev | @control_w      | d.prokopyev@innopolis.university    | Team Lead              | Define project business goals, strategy, target audience, key hypotheses. Make key choices regarding project stack, system design, and organization of development and product acceptance processes. Regularly update and validate all aspects of project requirements and system design to ensure alignment with business goals according to latest insights. Organize weekly sprint planning and other events to coordinate incremental development and delivery of value by other team members. Responsible for value delivery. |
| Nikita Tiurkov    | @NikitaTuyrkov  | n.tiurkov@innopolis.university      | ML Engineer            | Analyze ML requirements to choose and experiment with large language models. Develop microservices utilizing these LLMs to perform intellectually difficult tasks, primarily feedback generation. Build and review the segments of system design related to ML components. Responsible for high-quality ML solutions and architecture.                                                                                                                                                                                             |
| Egor Torshin      | @egor_torshin   | e.torshin@innopolis.university      | Lead Backend Developer | Analyze backend requirements and increment specifications to develop and coordinate development of backend microservices. Build and review the segments of system design related to backend components and integrations with external tools.   Responsible for backend increments delivery.                                                                                                                                                                                                                                        |
| Dmitriy Yashin    | @guBaH11        | d.yashin@innopolis.university       | QA/Security Engineer   | Ensure compliance with all the claimed non-functional requirements of the system, especially security. Design security requirements, transform all the non-functional requirements into tests/benchmarks, and/or CI/CD validation stages as to enable easy compliance testing for developers. Review and control the security requirements compliance in system design. Responsive for non-functional requirements delivery.                                                                                                       |
| Oleg Shchendrigin | @Quartz_Admirer | o.shchendrigin@innopolis.university | ML Engineer            | Analyze ML requirements to choose and experiment with large language models. Develop microservices utilizing these LLMs to perform intellectually difficult tasks, primarily feedback generation. Coordinate ML development efforts and ensure delivery of ML-related increments. Responsible for delivery of ML increments.                                                                                                                                                                                                       |
| Marsel Fayzullin  | @icinisani      | m.fayzullin@innopolis.university    | DevOps Engineer        | Analyze infrastructure requirements to setup and deploy all the system microservices and intermediate components. Maintain distinct staging and production environments, CI/CD pipelines, and external solutions deployment to enable seamless and smooth development practices. Manage hardware availability (A100 GPUs in this project). Responsible for managing and maintaining server infrastructure.                                                                                                                         |
| Aziz Vundirov     | @alibaba228999  | a.vundirov@innopolis.university     | Backend Developer      | Develop backend microservices, such as FastAPI servers and services-adapters for integrating external open-source solutions. Responsible for backend tasks delivery.                                                                                                                                                                                                                                                                                                                                                               |

> Note: we identified a way to use an already existing open-source frontend for this project, thus the need for frontend developers and designers is diminished

## Brainstorming

Project planning in this case was organized not only by brainstorming, but primarily through application of Socio-Technical Systems Design Framework ([Фреймворк Проектирования Социотехнических Систем, Бындюсофт](https://byndyusoft.com/academy#:~:text=%D0%90%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D1%80%D0%B0%D1%81%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D1%91%D0%BD%D0%BD%D1%8B%D1%85%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC-,%D0%A4%D1%80%D0%B5%D0%B9%D0%BC%D0%B2%D0%BE%D1%80%D0%BA%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20%D1%81%D0%BE%D1%86%D0%B8%D0%BE%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D1%85%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC,-%D0%9C%D1%8B%C2%A0%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BB%D0%B8%20%D1%84%D1%80%D0%B5%D0%B9%D0%BC%D0%B2%D0%BE%D1%80%D0%BA)) empowered by brainstorming. See project [hypotheses map](https://strategic-control.kaiten.ru/documents/d/25edfaac-364b-49e3-8ce0-64a1d926eb4a) and [process-experience map](https://strategic-control.kaiten.ru/documents/d/3c16a965-34eb-40e9-ba0c-cc0d92e16c03) for details.

### Ideas during brainstorming

Application of hypotheses mapping empowered the project by providing a structured framework for constructing and validating key business value ideas. Since simply stating these ideas out of context would strip them of logic and value used in their construction, the reader is encouraged to view the project [hypotheses map](https://strategic-control.kaiten.ru/documents/d/25edfaac-364b-49e3-8ce0-64a1d926eb4a) (==ideas = hypotheses = yellow cards==).

All high-level ideas that passed the structure and common sense validation are present on the hypotheses map.

Please note the distinction between hypotheses tiers:
- Primary hypothesis
	- Marked with red path (goal -> subjects -> pain points and wishes -> hypothesis -> tasks)
	- The primary focus of the MVP
- Secondary hypotheses
	- All the other hypotheses
	- Not required in the MVP

### Brief market research / problem validation

The primary hypothesis suggests to integrate fully automated system for validating the solutions (code) of ML and DS practice cases into existing educational courses for commercial purposes, suggesting that **cheapness, speed, and 24/7 availability** of this solution brings a significant benefit to the owners of the courses mentioned above, while retaining their ability to utilize **human mentorship** as a strategic advantage, thus enabling sales for achieving the project goal.

This hypothesis relies on certain assumptions.

> Market assumptions:
> - Current ML and DS courses are quite expensive for their students
> - Mentioned educational courses suffer from slow/delayed practice cases validations
> - Validations mentioned above are not available 24/7 in those courses

> Technical assumptions:
> - It is possible to reduce the validation cost significantly (at least by 50%) through automation
> - It is possible to provide validations in minutes or seconds instead of hours
> - It is possible to ensure 24/7 availability of the validation system
> - It is possible to integrate such a solution into other educational platforms

Technical expertise and work experience of the project team lead (3 years as a mentor on online courses) suggests the technical assumptions are correct.

As for the market assumptions, let's briefly validate them by investigating the aforementioned courses:

| Company              | Average full cost of online courses in ML&DS | Average waiting time for practice validation | Average mentors availability |
| -------------------- | -------------------------------------------- | -------------------------------------------- | ---------------------------- |
| **Karpov.Courses**   | 100 000 - 130 000 ₽                          | 1-2 days                                     | 16 часов в сутки             |
| **Яндекс Практикум** | 140 000 - 170 000 ₽                          | Up to 24 hours                               | 12-16 часов в сутки          |
| **Нетология**        | 110 000 - 150 000 ₽                          | 1-3 days                                     | 12-16 часов в сутки          |
| **SkillFactory**     | 150 000 - 190 000 ₽                          | 2-4 days                                     | 10-15 часов в сутки          |
| **Skillbox**         | 120 000 - 150 000 ₽                          | 1-3 days                                     | 12-16 часов в сутки          |

Even assuming that real-life metrics for these platforms are twice as optimistic as suggested in the table, the overall market state is still quite unfriendly to the consumer. Thus, this table suggests that the aforementioned assumptions are reliable enough to risk making them.

## Basic requirements

### Target users and their primary needs

**Target Audience**
- B2C
	- Students of online courses in ML&DS fields
	- The primary need is to ensure that their skill level by the end of their education is sufficient enough to get employed in the target company
- B2B
	- Companies selling online courses in ML&DS fields to aforementioned students
	- The primary need is profit and economic stability

### User stories

> This section contains top priority user stories extracted from system architecture artifacts mentioned above 

- As a student, I want to receive near-instant feedback for my solution of a practice case, because it enables me to effectively and efficiently learn from my mistakes
- As a student, I want to request feedback at any time, because then I won't have to waste time on waiting, which increases my rate of learning
- As a student, I want to receive a follow up on those feedback points I don't understand, because then I can uncover and eliminate gaps in my knowledge
- As a company selling online courses, I want to minimize operational costs for my courses, because then I can increase my margins or decrease my pricing to obtain a larger market share
- As a company selling online courses, I want to retain human mentorship claim when selling my courses, because it positions me as a high-quality professional platform on the market

### Initial scope

**MVP includes**:
- Web IDE with basic code validation mechanisms
- LLM-powered feedback generation mechanisms with 5 seconds limit on feedback latency
- Deep static analysis with 5 seconds limit on feedback latency
- Multi-user mode support
- Permanent memory for user sessions
- Progress tracking for students
- Moderate system security

**MVP does not include**:
- Deep training for specific tools/practices
- A platform for selecting practice cases and tracking acquired skills
- Transfer of solved cases into students' resumes or GitHub profiles
- Case-profile generation mechanisms
- On-premise deployment support for sensitive data protection

## Tech-stack

**Web IDE basis**: JupyterHub 

### **Backend & APIs**
- **Languages**: 
  - **Primary**: Python (FastAPI) for most microservices (development speed, async support, and ML integration).
- **API Design**:
  - **REST**: FastAPI (for Python), OpenAPI/Swagger compliance.
  - **Event-Driven**: Apache Kafka (for async communication between services, e.g., user activity tracking for recommendations).
- **Database**:
	- **Relational**: PostgreSQL (ACID-compliant, scalable with read replicas, JSONB support).
	- **File Storage**: MinIO (S3-compatible, open-source object storage for high-frequency file changes).
- **Documentation**:
	- **API Docs**: Swagger/OpenAPI (auto-generated by FastAPI and ASP.NET Core).
	- **Internal Docs**: Markdown enhanced with diagrams and documents.
- **Testing**:
  - **Backend**: Pytest (Python).

### **DevOps & Infrastructure**
- **Orchestration**: Docker Compose, suitable for rapid iterations due to simplicity
- **CI/CD**: GitHub Actions, enforced by course requirements
- **Monitoring**:
  - **Metrics**: Prometheus (scraping metrics) + Grafana (dashboards), well documented and widely used observability tools
  - **Logging**: Loki (open-source log aggregation) + Promtail, integrates well with observability stack
  - **Tracing**: Jaeger (distributed tracing for microservices), required for performance observability and microservices debugging
- **IaC**: Terraform, enables seamless infrastructure migration, which is predicted to occur for the project

### **Core ML & LLM Tools**

- **HuggingFace**: most common source of open-source models
- **GitHub**: data (prompts) versioning and experiment tracking
- [Qwen/Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B): primary (for now) LLM for feedback generation, chosen due to constrained generation support and [experimental inference speed evaluations](https://strategic-control.kaiten.ru/documents/d/ca5a59b6-a218-409b-ac71-ce50d3c56ee2)
- vllm: open-source solution for enhancing LLM inference, does not reurie hardware expertise

### **Security & Compliance**
- **Authentication**: Keycloak (open-source OpenID Connect provider, integrates with FastAPI).
- **Authorization**:
  - **RBAC**: Built into Keycloak for coarse-grained roles.
  - **Fine-Grained Policies**: Open Policy Agent (OPA) for service-to-service authz.
- **Secret Management**: Conjur Open Source as primary secret manager + Secret-less Broker by CyberArk as a secret broker, matches the security requirements for the project and simplifies security-aware development


# Weekly commitments

## Individual contribution of each participant

| Team Member       | Role                   | Commitments (Artifacts)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dmitriy Prokopyev | Team Lead              | Project Strategy as a [Hypotheses Map](https://strategic-control.kaiten.ru/documents/d/25edfaac-364b-49e3-8ce0-64a1d926eb4a), User Flow + System Flow as a [Process-Experience Map](https://strategic-control.kaiten.ru/documents/d/3c16a965-34eb-40e9-ba0c-cc0d92e16c03), [System Design](https://strategic-control.kaiten.ru/documents/d/75a331fd-6a8b-4109-9ac9-20e4346e8111) sketching, [Requirements Engineering](https://strategic-control.kaiten.ru/space/606285/boards) efforts, [Product Backlog](https://strategic-control.kaiten.ru/space/606257/boards) setup and maintenance, [Technical Backlog](https://strategic-control.kaiten.ru/space/606259/boards) setup and partial maintenance, have chosen and bought three domain names in Рег.ру (proof on request) |
| Nikita Tiurkov    | ML Engineer            | [ML microservices commits](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commits/dev/), numerous completed tasks in [Technical Backlog](https://strategic-control.kaiten.ru/space/606259/boards)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Egor Torshin      | Lead Backend Developer | Maintenance and tasks decomposition in [Technical Backlog](https://strategic-control.kaiten.ru/space/606259/boards), participation in [System Design](https://strategic-control.kaiten.ru/documents/d/75a331fd-6a8b-4109-9ac9-20e4346e8111) sketching                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Dmitriy Yashin    | QA/Security Engineer   | Analysis and design of [security measures](https://strategic-control.kaiten.ru/documents/d/91c76aad-b7aa-49dc-8e92-bf7188551c40) necessary for JupyterHub deployment and extension services                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Oleg Shchendrigin | ML Engineer            | Maintenance and tasks decomposition in [Technical Backlog](https://strategic-control.kaiten.ru/space/606259/boards), [comparative analysis](https://strategic-control.kaiten.ru/documents/d/ca5a59b6-a218-409b-ac71-ce50d3c56ee2) of inference speed for various LLMs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Marsel Fayzullin  | DevOps Engineer        | Setup of the server infrastructure and [deployment mechanisms](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/tree/dev/deployment/dev)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Aziz Vundirov     | Backend Developer      | [Backend microservices commits](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commits/dev/), numerous completed tasks in [Technical Backlog](https://strategic-control.kaiten.ru/space/606259/boards)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Plans for the next week

- Finalize the key microservices, their connections, and security requirements
- Integrate real-time static analysis the IDE
- Integrate deep static analysis (manualy triggered) into the IDE
- Finalize three-stage deployment setup
- Analyze and integrate required security solutions into the system design
- Implement localized feedback generation as warnings and non-localized feedback generation as MD text
- Prepare increment specifications for weeks ahead

## Confirmation of the code’s operability

We confirm that the code in the main branch:

- [x]  In working condition.
- [x]  Runs via docker-compose (or another alternative described in `README.md`).

In order to enter the system you will need to know temporary password, you can find it [here](https://strategic-control.kaiten.ru/documents/d/c3e7daa4-1678-4e99-839b-6caee4383234)
