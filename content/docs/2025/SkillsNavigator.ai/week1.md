---
title: "Week #1"
---

# Week #1

## Project description

### Project name: SkillsNavigator.ai

**Code repository**: https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai

Access to quality, affordable, and personalized learning pathways is severely limited for learners in emerging and restricted markets. Existing solutions either lack tailored guidance, impose high costs, or rely on geo-locked platforms.

SkillNavigator.ai is an AI-driven Study Roadmap generator that provides learners with automated, hyper-personalized sequences of free and low-cost learning resources. By combining user profiling, vector-based content retrieval, and a custom ML recommender, SkillNavigator.ai produces a step-by-step learning plan aligned to individual goals, skill levels, time availability, and budget constraints.



### **Team Members**

| Team Member                         | Telegram Alias    | Email Address                        | Track                                   | Responsibilities                                                                                                                                                                                                                                                        |
|-------------------------------------|-------------------|--------------------------------------|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lana Ermolaeva (lead)               | @oELYAo           | l.ermolaeva@innopolis.university     | Project and Product Management           | market analysis; product vision; team management; task delegation; risk management; quality assurance; technical writing                                                                                                                                                |
| Adilya Saifetdiarova                | @sayfetik         | a.saifetdiarova@innopolis.university | Front-end and UX/UI design               | product ideas and requirements to design; UX/UI design to functional web pages; optimize application performance; collaborate with backend; debug and troubleshoot UI issues                                                                                          |
| Ivan Ershov                         | @spiritonchiс     | i.ershov@innopolis.university        | ML                                       | find best ML model to solve the problem; select deatures; train the model; test the model; improve model quailty; collaborate with backend                                                                                                                               |
| Bulat Gazizov                       | @BulatGazizov0    | b.gazizov@innopolis.university       | Back-end working with Front-end, DevOps  | design and implement server-side logic, APIs and databases; work with frontend, external services; automate deployment; manage CI/CD pipelines; implements infrastructure as code (IaC) and containerization |
| Arthur Popov                        | @ee_boooy         | ar.popov@innopolis.university        | Back-end working with ML, MLOps,         | collaborates with ML specialists; integrates ML models into backend services; translate research into production-ready code                                                           |

## Brainstorming

        
### Ideas during brainstorming
- **Sentiment Analysis of Customer Feedback**: Gather information from multiple sourses and automatically determine the sentiment (positive, negative, neutral) in multisource customer reviews and feedback. Team ranked idea:⭐⭐⭐
- **AI-driven Study Roadmap**: Generate personalized course-based learning paths for students knowing their goals, level of knowledge and budget.
  Team ranked idea:⭐⭐⭐
- **AI-Driven Employee Development**: Assess employee skills by KPI, recommend training, and track progress for professional growth. Team ranked idea:⭐⭐☆
- **Automation of document and invoice processing**: Employ AI to extract, validate, and process information from documents and invoices, reducing manual work. Team ranked idea:⭐☆☆
- **AI-driven analytics of marketing campaigns**: Analyze marketing campaign data with AI to uncover trends, measure effectiveness, and suggest improvements. Team ranked idea:⭐☆☆
        


### Brief market research / problem validation
- **Sentiment Analysis of Customer Feedback**: 
  - No identical service available in Russia
  - Corporations have their own solutions
  - Monitor reviews to take ideas of new features, polish product and fix bugs if they reach production
  - Big decisions are based on product metrics, trends and business, not on the reviews

- **AI-driven Study Roadmap**: 
  - No identical service
  - Lack of low-cost learning resourses (Coursera & EdX left Russia, YouTube is unavailable)
  - All-in-one courses cost like higher education
  - GPT search does not solve the problem or does it poorly
  - Course platforms (like Stepic) do not offer personalised roadmaps

The team made a choice that the AI-driven Study Roadmap fits the market better, came up with the name "SkillNavigator.ai".
    
## Basic requirements

### Target users and their primary needs
As we aim to make roadmap as neetly personalised as possible, this part is the most important foundation of our product. 
For this reason we detect as many stereotypes as it is possible. For the same reason, primary needs are about content of courses.

- Recent Graduates & Students
   - Skill‐level calibration: start at the right spot (no wasteful repetition).
   - Goal alignment: tie courses directly to desired entry-level roles.
   - Cost-effectiveness: maximize free or budget-friendly learning.
   - Fast feedback loops: courses with quizzes, mini-projects or peer communities to validate learning.
   - Certification guidance: advice on which certificates carry weight in hiring markets.

- Budget-Constrained Learners in Emerging Markets
  - Region-accessible resources: courses that don’t require geo-locked payment or VPN.
  - Localized recommendations: content in their native language or with subtitles.
  - Low-cost alternatives: open-source, government-funded, or community-driven courses.
  - Up-to-date availability checks: alerts when popular platforms return or new local ones emerge.
  - Peer-reviewed quality checks: crowd-sourced ratings to avoid low-quality, obscure videos.

- Career Switchers & Advancers
  - Clear end-to-end plan: step-by-step progression from foundational to advanced.
  - Time efficiency: realistic schedules that fit around a full-time job.
  - Budget control: mix of free & paid options that total under their threshold.
  - Credibility signals: course ratings, instructor reputations, market-relevance data.
  - Outcome tracking: milestones/checkpoints and suggestions for portfolio projects or certifications.

- Self-Learners & Hobbyists
  - Breadth & depth balance: enough theory to understand “why,” plus hands-on tutorials.
  - Flexible pacing: ability to pause, remix, or skip modules based on interest.
  - Community pointers: links to forums, Discords, or project prompts.
  - Resource diversity: combination of articles, videos, podcasts, and interactive tools.
  - Inspiration & challenges: suggested capstone projects to apply new skills.

- Side-Project Makers
   - Technology Deep Dives: in-depth courses on specific stacks (e.g. React + Node.js)
   - API & Tooling Tutorials: step-by-step guides for popular services (Stripe, Firebase)
   - Git-Centric Workflows: courses with built-in GitHub integration and code reviews
   - Deployment Clinics: end-to-end hosting/deployment walkthroughs 
   - Modular Add-Ons: “plug-in” micro-courses for adding new features
     
- Freelancers & Gig Workers
  - Rapid-Skill Sprints: 4–6 week focus courses on high-demand skills (SEO, Facebook Ads)
  - Portfolio Workshops: template-driven projects to present to clients
  - Low-Cost Certificates: sub-5000rubles certificates that clients recognize
  - Business Essentials: mini-courses on proposals, contracts, and pricing
  - Continuous Refreshers: monthly updates on platform algorithm changes

 - Unemployed Job Seekers
   - Zero-Cost Academies: government-sponsored or NGO-funded full tracks
   - Job-Readiness Bundles: combo of resume-building, interview practice, and role-specific skills
   - Live Coaching Sessions: free or subsidized group webinars with industry mentors
   - Local Market Spotlights: courses highlighting in-demand regional skills
   - Placement-Linked Programs: courses offering direct introductions to employers
     
 - Corporate Trainers & L&D Managers
   - Cohort Programs: group-paced “leadership” or “agile transformation” tracks
   - Bulk-License Courses: discounted enterprise-scale subscriptions (e.g. 50 seats)
   - Customizable Curricula: white-label modules with company branding
   - Data-Rich Dashboards: courses with built-in analytics on learner engagement
   - Compliance & Certification Packs: up-to-date regulatory or standards training

 - College & High-School Students
   - Curriculum-Aligned Modules: courses that mirror school syllabi
   - Credit-Bearing Classes: MOOCs that offer university credits upon completion
   - Summer Intensives: short, immersive workshops during school breaks
   - Scholarship Prep Tracks: test-prep courses plus application workshops
   - Study-Buddy Forums: built-in peer chatrooms and group project options



### User stories

5 main high-level user stories:

- As a busy professional, I want to input my goals, current skill level, and available time in one place, so that I can receive a clear, personalized study roadmap without spending hours researching.
- As a budget-constrained learner, I want to set a maximum spend, so that every recommended step fits my financial limits and I don’t encounter hidden costs.
- As a returning user, I want to update my profile and regenerate my roadmap on demand, so that my learning plan always adapts to my evolving goals and circumstances.
- As a freelancer with shifting project loads, I want to rearrange or skip roadmap steps, so that I can fit my learning into a dynamic schedule without losing overall progress.
- As a user, I want to export or copy my personalized roadmap (course titles + links), so that I can save or share it outside the platform.

### Initial scope
IN FOR MVP:
- User Profile & Intake: Brief onboarding poll
- Free-form Topic Input: Single text field, vector-search backend
- Roadmap Generation Engine: sequencing of 5–10 recommended links of courses into a linear “roadmap”
- Budget & Time Constraints: Enforce user-entered max spend and weekly-hours limits when selecting resources, display total estimated spend and cumulative hours 
- Allow users to check off completed roadmap items

OUT FOR MVP:
- Advanced Personalization
- Advanced Filtering & Discovery
- Card-Based & Rich UI Layouts
- Path Editing & Customization
- Notifications & Integrations


## Tech-stack

React, FastAPI, qdrant (vector DB), PyTorch + Scikit-learn, Docker

We are builing a website with vector search, custom ML model and interactive UI elements (roadmap of cards). 


- React - reusable components, efficient rendering, and a flexible architecture;
- FastAPI - async features to handle many requests with minimal latency is suitable for real-time applications;
- qdrant (vector DB) - store, search, and manage high-dimensional poinys (Vector Embeddings);
- PyTorch + Scikit-learn - PyTorch's flexibility is complemented by Scikit-learn's efficiency and ease of use;
- Docker - consistent behavior in different environments, streamline deployments, and enhance scalability.

The stack satisfies the techical aspecks and matches the team experience. 

## The way we work

We are focused on building MVP, then continuously and costantly delivering new features leading to the final version of product which satisfies customers' and business needs.

# Weekly commitments

## Individual contribution of each participant

| Team Member                         | Telegram Alias    | Email Address                        | Track                                   | Responsibilities                                                                                                                                                                                                                                                        |
|-------------------------------------|-------------------|--------------------------------------|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lana Ermolaeva (lead)               | @oELYAo           | l.ermolaeva@innopolis.university     | Project and Product Management           | Product ideas & market fit analysis https://drive.google.com/drive/folders/1wNSaIEqXm6eq8XSebGiH2Uj80ij_uFLZ?usp=sharing; readme update: https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/455da89cfa962b6d8170d5a7bfdb7228246c0f4f; report writing                                                                                                                                                |
| Adilya Saifetdiarova                | @sayfetik         | a.saifetdiarova@innopolis.university | Front-end and UX/UI design               | React Frontend boilerplate and setup, readme update: https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/8e96eed5491919ba60b0c1c3c9428b952d3f258c  https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/d8f17f573a72a3722a843095d0b813081b5e849c, hi-fi design: https://www.figma.com/design/JjmqRt1Tr5xyc9X3vRJN5L/SkillsNavigator?node-id=0-1 |                                                                                         |
| Ivan Ershov                         | @spiritonchiс     | i.ershov@innopolis.university        | ML                                       | Base project structure, added Qdrant (vector DB) to Docker: https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/b26404b5a2f556f3ed1beade4273793a8a85b816                                                                                                                               |
| Bulat Gazizov                       | @BulatGazizov0    | b.gazizov@innopolis.university       | Back-end working with Front-end, DevOps  | FastAPI Back-end boilerplate, Dockerfile and docker-compose editing, needed libraries to requirements.txt: https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/pull/1|
| Arthur Popov                        | @ee_boooy         | ar.popov@innopolis.university        | Back-end working with ML, MLOps,         | Front-end service added to Docker, front-end added to docker-compose: https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/add8f5cf5737e91ab147ec52c846610908f57b5c                                                        |


## Confirmation of the code's operability

We confirm that the code in the main branch:
- [✔] In working condition.
- [✔] Run via docker-compose (or another alternative described in the `README.md`).
