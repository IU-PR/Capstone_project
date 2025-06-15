---
title: "Week #1"
---

# Week #1

## Project description

### Project name: *Open Labs Share*

**Code repository**: https://github.com/IU-Capstone-Project-2025/open-labs-share

Open Labs Share is an innovative educational platform that combines structured learning with academic collaboration. The platform addresses the problem of fragmented educational resources and lack of constructive feedback mechanisms for students and researchers.

**Problem Statement:** Current educational platforms either focus solely on structured learning (like traditional LMS) or academic publishing (like ResearchGate), but fail to bridge the gap between practical learning and academic discourse. Students struggle to get meaningful feedback on their work in the early stage of their career, while researchers lack accessible and open platforms to share knowledge with learners. Our platform solves this by creating a dual-environment system that facilitates both guided learning through practical assignments (labs) and open academic collaboration through research publication and peer review.

### **Team Members**

| Team Member                             | Telegram Alias   | Email Address   | Track                                       | Responsibilities   |
|-----------------------------------------|------------------|-----------------|---------------------------------------------|--------------------|
| Kirill Efimovich (Lead)     | @Cblblblblblp | k.efimovich@innopolis.university | DevOps/PM | Project coordination, infrastructure, deployment, monitoring, performance optimization |
| Mikhail Trifonov            | @LuminiteTime | m.trifonov@innopolis.university | Backend | Backend development, API development |
| Nikita Maksimenko            | @Nexonm | n.maksimenko@innopolis.university | Backend | Backend development, API development |
| Timur Salakhov            | @ClayMix | t.salakhov@innopolis.university | Backend | Backend development, service development |
| Ravil Kazeev            | @Ravwvil | r.kazeev@innopolis.university | Backend | Backend development, service development |
| Kirill Shumskiy | @graf_shuiskiy | ki.shumskii@innopolis.university | ML | Recommendation system, content moderation, AI integration |
| Aleliya Turushkina | @aleliya_turushkina | a.turushkina@innopolis.university | Frontend/Design | UI/UX design, frontend development |


## Brainstorming

### Ideas during brainstorming
1. Dual-Platform Educational System (Chosen) - Combines structured learning labs with academic publication platform
2. Travel app - ML utilization for searching and making trip for group of people in different places (use: for e.g. on weekends)
3. ML optimized CI-CD platform - ML utilization for predicting level of approval of coming pipeline with further analysis

### Brief market research / problem validation

**Market Gap:** Existing platforms like Coursera focus on content delivery, while GitHub lacks educational structure. ResearchGate serves researchers but intimidates beginners.

**Approximate Target Market Size:** 1.3 billion students worldwide + growing online education market ($340B by 2025)

**Validation:** Surveys indicate 78% of students want more peer feedback, 65% of researchers willing to mentor if platform is user-friendly


## Basic requirements

### Target users and their primary needs

Primary Users:

- Students (University/High School): Need structured learning paths, practical assignments, and constructive feedback on their work in the start of their career

- Early-Career Researchers: Require open platforms to publish preliminary research, get feedback, and meet academic mentors

- Educators/Mentors: Want tools to guide students and share expertise in accessible formats, freely teach and give their knowledge

Secondary Users:

- Industry Professionals: Seeking to share practical knowledge and discover emerging talent

- Academic Institutions: Looking for platforms to enhance their educational offerings

### User stories

- As a student, I want to complete labs and receive detailed feedback so that I can improve my skills progressively

- As a researcher, I want to publish my work and get constructive reviews from peers so that I can refine my research before formal publication

- As an educator, I want to create assignments and monitor student progress so that I can provide targeted guidance and improve my experience

- As a platform user, I want to discover relevant content (labs related to articles, articles supporting lab concepts) so that I can deepen my understanding in chosen topic

### Initial scope

MVP Features:

- Learning Module: Basic lab assignment system with file upload and peer review

- Academic Module: Article publication with commenting system

- User Management: Registration, profiles, basic moderation tools

- Feedback System: Simple review templates for feedback

Future Features:

- Labs and research papers categorization

- Recommendation system connecting related labs and articles

- AI-powered content recommendations

- Advanced moderation tools

- Monetization features (premium accounts, advertising)


## Tech-stack

- Frontend: React + Tailwind CSS
- Backend: Java (Spring) + *Go**
- Database: PostgreSQL
- Authentication: JWT with OAuth 
- File Storage: AWS S3 or *MinIO**
- Deployment: Docker containers
- Monitoring: Prometheus + Grafana
- AI/ML: Python + Torch + numpy + pandas + langchain + tensorflow

*\* - still under consideration*

## *Something else you want to add*

Monetization Strategy: non-intrusive advertising, *premium features**, institutional partnerships

*\* - still under consideration*

# Weekly commitments

## Individual contribution of each participant


-  **Kirill Efimovich:** Conducted several team meetings, suggested idea of adding academic papers tab into our system, filled weekly report, set up GitHub repositories, containerized boilerplate [(link)](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/2)
  
-  **Mikhail Trifonov:** Constructed service architecture [(repo link)](https://github.com/LuminiteTime/Open-Labs-Share-Docs), actively suggested ideas for MVP and for future, made boilerplate [(link)](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/1)

-  **Nikita Maksimenko:** Main idea holder, constructed service architecture [(repo link)](https://github.com/LuminiteTime/Open-Labs-Share-Docs), actively suggested ideas for MVP and for future

-  **Timur Salakhov:** Helped with all sides of architecture [he said and Mikhail \ Nikita typed (repo link)](https://github.com/LuminiteTime/Open-Labs-Share-Docs), actively suggested ideas for MVP and for future

-  **Ravil Kazeev:** Helped with all sides of architecture [he said and Mikhail \ Nikita typed (repo link)](https://github.com/LuminiteTime/Open-Labs-Share-Docs), actively suggested ideas for MVP and for future

-  **Kirill Shumskiy:** Assisted with theoretical ML usage in our project [he said and Mikhail \ Nikita typed (repo link)](https://github.com/LuminiteTime/Open-Labs-Share-Docs), started research for tools for ML side implementation 

-  **Aleliya Turushkina:** Prototyped design in Figma [(link)](https://www.figma.com/design/mvegZwCxX8KHxhtI2PeMHQ/OpenLabsShare?node-id=0-1&p=f&t=M2kuxYrgLTacXKCY-0), started research for tools for frontend side implementation
  


## Confirmation of the code's operability

We confirm that the code in the main branch:

  ☑️ In working condition. \
  ☑️ Run via docker-compose (or another alternative described in the `README.md`).