---
title: "Week #1"
---

# Week #1

## Project description

### Project name: *NeuroCoach*

**Code repository**: https://github.com/IU-Capstone-Project-2025/NeuroCoach

The Problem
The main challenge in self-guided fitness journeys is the lack of properly structured training plans and ongoing support. Most apps offer generic workout programs that don't account for individual fitness levels, goals, or limitations. Without proper exercise technique guidance and a clear progression plan, users quickly lose motivation - 65% abandon their workouts within the first three months. While personal trainers could solve this problem, their services remain expensive and unavailable exactly when needed.

The Solution
NeuroCoach creates fully personalized training plan for each user. Our AI coach is available 24/7 - it provides detailed exercise technique explanations, answers all training-related questions, and adjusts the program as users progress. To make workouts truly engaging, we've implemented a gamification system: achieving milestones, completing levels, and earning rewards for consistency create a game-like experience that keeps users coming back. This approach makes professional guidance accessible to everyone, transforming routine workouts into an exciting self-improvement journey.

### **Team Members**

| Team Member              | Telegram Alias     | Email Address                        | Track                    | Responsibilities   |
|--------------------------|--------------------|--------------------------------------|--------------------------|--------------------|
| [Mariia Nikolashina]     | [@nikolashina_mary] | [m.nikolashina@innopolis.university]| [Backend]                | [Developing the backend architecture, implementing core modules (authentication, user management, workouts), integrating with databases, and preparing APIs for the frontend and mobile app.] |
| [Mark Petrov]            | [@pavorkmert]      | [ma.petrov@innopolis.university]     | [Product management]     | [Setting tasks, planning sprints, conducting market and user research, interviewing experts, shaping the product vision, and ensuring product-market fit.] |
| [Oleynik Maxim]          | [@DartGGWP]        | [m.oleynik@innopolis.university]     | [Backend]                | [Designing and optimizing the database structure (PostgreSQL and MongoDB), defining entity relationships, normalization, and preparing schemas for development.] |
| [Klimentii Chistyakov]   | [@blazz1t]         | [k.chistyakov@innopolis.university]  | [Mobile App development] | [Building the architecture and initial modules of the Flutter-based mobile app, setting up backend integration, and implementing basic screen logic.] |
| [Danil Fishchenko]       | [@ppepegaa]        | [d.fishchenko@innopolis.university]  | [ML and Design]          | [Creating the UI/UX design for both the mobile and web apps — from prototyping to final screen layouts — following a unified design system.] |
| [Saidaziz Kadirov]       | [@Saidaziz_K]      | [s.kadirov@innopolis.university]     | [Frontend]               | [Developing the frontend architecture for the web version using Next.js + Tailwind, coding key pages, and setting up communication with the backend via REST API.] |


## Brainstorming

### Ideas during brainstorming

To generate high-quality ideas, we used the Six Thinking Hats method, where each team member took on a specific role (optimist, pessimist, analyst, creative, etc.). Our main focus was identifying real problems rather than jumping to solutions that might not resonate with users. We explored various niches and target audiences before ultimately choosing NeuroCoach.

Here are 5 other ideas we considered but decided against:

1. AI Nutritionist: Personalized Meal Plans & Grocery Optimization
Problem: People struggle with meal planning—either they lack time, don’t know what’s healthy, or waste money on unused groceries.
Solution: An AI that generates weekly meal plans based on dietary goals, budget, and fridge inventory, then auto-generates a shopping list.
Why we rejected it:
- Requires integration with grocery APIs (complex partnerships).
- Nutrition is highly subjective (hard to standardize).

2. Sleep Coach AI: Smart Alarm & Sleep Habit Trainer
Problem: Poor sleep habits lead to fatigue, but most people don’t know how to fix them.
Solution: An AI that analyzes sleep patterns via wearables, suggests optimal bedtimes, and wakes users at the right sleep cycle.
Why we rejected it:
- Heavy reliance on third-party hardware (Apple Watch, Fitbit).
- Competing with built-in phone features (e.g., iOS Sleep Mode).

3. AI Interview Simulator for Specific Careers (e.g., Doctors, Engineers)
Problem: Job seekers in specialized fields struggle to find realistic mock interviews.
Solution: A role-specific interview trainer with industry-tailored questions and scoring.
Why we rejected it:
- Too niche—would need separate models for each profession.
- Harder to scale than general career coaching.

4. AI "Focus Buddy" for ADHD & Productivity
Problem: People with ADHD or focus issues get distracted and lose productivity.
Solution: A chatbot that breaks tasks into micro-steps, sends reminders, and blocks distractions.
Why we rejected it:
- Medical/accessibility compliance adds complexity.
- Existing apps (like Focus@Will) already cover parts of this.

5. AI Language Tutor with Real-Time Accent Correction
Problem: Language learners often practice speaking incorrectly, cementing bad accents.
Solution: Voice-based AI that detects pronunciation errors and corrects them in real time.
Why we rejected it:
- Requires extremely low-latency voice processing.
- Big competitors (Duolingo, Babbel) are adding similar features.

### Brief market research / problem validation

1. NeuroCoach: AI Fitness Coach
Market Analysis
The Russian fitness market is showing steady growth, reaching a volume of 260 billion rubles in 2025. However, 58% of beginners quit training within the first few months due to a lack of professional guidance and clear workout programs. Traditional personal training remains an expensive option (starting at 2,500 rubles per session ), creating a perfect niche for digital solutions.

Problem Validation
The main issue users face is the lack of personalized approach in mass-market fitness apps. Pre-made workout plans often ignore individual characteristics such as fitness level, available equipment, injuries, and progress. Surveys show that 89% of beginner athletes would prefer adaptive workout plans tailored to their abilities. NeuroCoach solves this problem through dynamically adjusted programs and interactive support from an AI coach.

2. AI Nutritionist: Personalized Meal Plans
Market Analysis
The global market for digital nutrition solutions is growing by 10.5% annually . In Russia, 63% of people interested in healthy lifestyles struggle to organize their diets due to the complexity of tracking and lack of expert advice. Meanwhile, consultations with dietitians remain largely inaccessible (average cost — 3,000 rubles per session ), and existing apps require manual data input.

Problem Validation
The main barrier is the lack of convenient tools that automatically generate meal plans based on real dietary habits and user goals. Most services offer either generic recommendations or require complex integrations with fitness trackers. An AI nutritionist could fill this gap, but high competition (50+ similar apps ) and the need for medical validation of algorithms make market entry challenging.

3. Interview Trainer for Niche Professions
Market Analysis
Demand for specialized interview preparation is especially noticeable in the IT sector, where 82% of junior specialists fail their first interviews due to lack of practice. Existing platforms offer either generic questions or expensive sessions with recruiters (from 5,000 rubles per session ). For niche professions (medicine, engineering), there are practically no quality solutions available.

Problem Validation
The key challenge is the absence of realistic simulators capable of generating industry-specific case studies. Candidates are forced to collect information fragmentarily from various sources, which reduces the effectiveness of their preparation. Although an AI-based trainer could solve this problem, development requires deep expertise in each professional field and partnerships with industry professionals.

## Basic requirements

### Target users and their primary needs

Our primary target audience consists of individual consumers who start their fitness journey on their own, without the support of a personal trainer. We focus on two key customer segments within the B2C market.

The first customer profile is young people aged 16 to 27. These are individuals who are either just starting their fitness journey or have tried working out independently but faced challenges such as lack of knowledge, motivation, and structured training plans. They are tech-savvy, open to AI technologies, and expect an interactive and engaging experience. For this group, accessibility, ease of use, and the ability to get instant answers to their questions are crucial. They are also highly motivated by gamified elements that make workouts more immersive and enjoyable, turning exercise into a game-like experience. Many of them want to track their progress over time, compare results, and receive recognition—even if it comes from an AI coach.

The second customer profile is adults aged 30 to 45. This group typically includes busy professionals who want to maintain their health, physical shape, and work-life balance. They have limited time but understand the importance of regular exercise. They value efficiency, a personalized approach, and the flexibility to train at their own pace. This group tends to be less experimental and prefers reliable, proven solutions. At the same time, they are price-sensitive—traditional personal training services are often out of reach. With NeuroCoach, they find an affordable alternative that combines professional guidance with adaptability to real-life circumstances.

In addition, our product has strong potential for expansion into the B2B segment. We can offer our AI-driven technology to fitness clubs, online platforms, and corporate wellness programs, enhancing their services with personalized training plans and 24/7 support from an AI coach. This allows us to broaden our reach and create additional revenue streams while staying true to our core mission: making high-quality fitness coaching accessible to everyone.

### User stories

1. Maria, 22, Student
Maria wants to get in shape but has no prior workout experience and a limited budget. She downloaded several fitness apps, but all of them offered generic programs that didn’t match her fitness level or how she felt after workouts. As a result, she felt discouraged and gave up. After learning about NeuroCoach, she decided to give herself another chance. The AI coach helped her start with the most basic exercises, explained proper technique, and provided guidance on intensity and rest. Gradually, she began to feel more energetic, started understanding how her body works, and now works out regularly. She loves being able to ask questions anytime and receive support, while the system tracks her progress and motivates her to keep going.

2. Alexey, 38, Department Head
For Alexey, an active lifestyle became a matter of health—prolonged sitting and high stress levels started taking a toll. He would like to exercise, but his schedule changes dramatically from month to month. Hiring a personal trainer is too expensive, and standard programs don’t take into account his physical condition or capabilities. With NeuroCoach, he was able to create a flexible plan that adapts to his mood, fatigue level, and available time. The AI coach helps him adjust the program, explains how to reduce tension after work, and guides him through recovery. Alexey feels back in control of his health and appreciates that he can train without extra costs or rigid schedules.

3. Daria, 17, High School Student Interested in Bodybuilding
Daria is passionate about fitness, watches YouTube videos, and reads articles, but finds it hard to figure out which exercises are actually suitable for her. She’s afraid of doing something wrong and getting injured. When she found NeuroCoach, she started training under the guidance of an AI coach who explains every movement, tracks her progress, and gives advice on increasing intensity. It’s important to her that the program considers her age, fitness level, and goals. She feels like she’s learning and growing rather than just copying someone else's routine.

4. "Energiya" Fitness Club (B2B Scenario)
A local fitness club faced a problem: clients often lost motivation and stopped coming to the gym. Administrators noticed that those who followed personalized programs with trainers stayed longer, but hiring a dedicated coach for each member wasn’t feasible due to budget constraints. After integrating NeuroCoach as an additional service, members gained access to adaptive workout plans, were able to ask the AI coach questions, and could visually track their progress. This increased engagement and loyalty, reduced churn, and allowed staff to use progress data for more effective collaboration with human trainers.

### Initial scope

At the initial stage of the NeuroCoach project, we will focus on building a Minimum Viable Product (MVP) that enables users to receive personalized workout plans, support from an AI coach, and progress tracking. The main goal is to establish a sustainable user cycle: registration → assessment of fitness level and goals → creation of an individual plan → execution of workouts with feedback → program adaptation based on progress.

The product will be launched as a mobile app, complemented by a basic web dashboard for analytics and management. The initial feature set includes:

User Profile – Collection of data such as age, gender, weight, height, fitness level, existing injuries or limitations and personal goals.
AI Coach with Chat Interface – Users can ask questions about exercise technique, training programs, and recovery, and receive clear, natural language responses in real time.
Personalized Workout Plan – Automatically generated based on user input and dynamically adjusted according to performance and feedback.
Progress Tracking – Logging of completed workouts, load metrics, session duration, and subjective feelings post-exercise.
Gamification Elements – A system of levels, achievements, and rewards designed to motivate users and encourage consistency.

In the future, we plan to expand functionality through integrations with wearable devices, voice assistant support, a nutrition diary feature, and partnerships with fitness clubs within a B2B model.


## Tech-stack

For the development of NeuroCoach, we are using a modern and high-performance technology stack that ensures reliability, scalability, and ease of future product development.

Backend:
We have chosen Golang (Go) as the primary language for backend development due to its performance, concurrency support, and maintainability. It is an excellent choice for building fast and robust services.

Databases:
We will use a combination of two database systems:
PostgreSQL – for storing structured data such as user profiles, workout plans, progress metrics, and goals.
MongoDB – for flexible storage of unstructured data, such as chat logs with the AI coach and temporary interaction records.

Mobile App:
The mobile frontend will be built using Flutter , allowing us to develop a cross-platform application with a native-like experience for both iOS and Android.

Web Interface:
For the web version and admin dashboard, we are using the Next.js framework based on React. The UI will be styled with Tailwind CSS , which enables rapid development, responsive design, and clean interface architecture.

Infrastructure and Deployment:
For containerization and infrastructure management, we will use:
Docker – to simplify development, testing, and deployment across different environments.
Nginx – as a reverse proxy server for request routing and load optimization.
GitHub Actions – for continuous integration and delivery (CI/CD), including automated builds, testing, and deployment.

This tech stack allows us to build a stable, scalable, and maintainable product that is ready for growth and continuous feature enhancements.

## *Something else you want to add*

To gain a deeper understanding of user needs and the specifics of the market, we conducted 10 customer discovery interviews (CustDevs) — 5 with representatives from each of our B2C target groups: teenagers and young adults aged 16–27, and working professionals aged 30–45. The main goal of these interviews was to uncover real pain points, motivations, and behavioral patterns related to self-guided fitness journeys.

During the interviews with younger users, we learned about their strong reliance on engaging UX, the importance of gamification, and the need for instant feedback. We also discovered that the fear of performing exercises incorrectly and getting injured is a significant barrier at the early stages of their fitness journey.

Among adult users, key themes included time constraints, the need for flexible workouts that adapt to an unpredictable schedule, and the desire to see clear progress and receive recommendations tailored to their personal circumstances and physical limitations.

In addition, we held a series of conversations with experts in the SportTech industry , including founders of fitness apps, digital coaching specialists, and gym owners. These discussions helped us better understand current trends, technological capabilities, and the challenges and entry barriers in the fitness tech space. We explored topics such as personalization, user retention, hardware integrations, and potential paths for scaling the product, including the B2B direction.

These insights formed the foundation of our product development and gave us confidence that we are solving real problems for our target audience, offering a truly valuable and in-demand service.

# Weekly commitments

## Individual contribution of each participant

Mariia Nikolashina
Maria focused on designing and developing the backend architecture for the NeuroCoach app. She structured the microservices, selected key interaction patterns between components, defined the API format, and outlined integration strategies with the frontend and mobile app. She also began implementing core modules such as user authentication, user management, and workout plan generation. Additionally, Maria participated in discussions around database selection (PostgreSQL and MongoDB) and prepared technical documentation to guide further development.

Mark Petrov
Mark acted as the Product Owner and team coordinator. He organized weekly meetings, planned sprints, and set clear goals for the upcoming stages of product development. As part of the market research efforts, he conducted a comprehensive market analysis, studied competitors, and dove deep into understanding our target audience. During the week, Mark personally held 10 customer discovery interviews (castdevs) — 5 with each of the two main user groups (youth aged 16–27 and adults aged 30–45), to better understand their pain points, motivations, and expectations from fitness apps. In addition, he conducted 4 expert interviews with SportTech professionals to gain external insights and ensure our solution aligns closely with real market needs and achieves strong product-market fit after launch.

Maxim Oleynik
Maxim worked on designing the structure of the databases that will power NeuroCoach. He analyzed data flows across the system and created logical models for both relational (PostgreSQL) and non-relational (MongoDB) storage. He mapped out how user profiles, workout plans, progress logs, chat interactions with the AI coach, and feedback would be stored and retrieved. Maxim also defined relationships between entities, normalized tables where necessary, and optimized schemas for scalability and performance. His work laid the foundation for efficient data handling across all parts of the application.

Danil Fishchenko
Daniil worked on the design of the user interface and overall UX/UI for both the mobile app and web version of the service. He designed screens for the home page, user profile, workouts, progress tracking, and gamification features. Daniil created prototypes of all key modules and coordinated them with the team before development began. His design focuses on simplicity, engagement, and intuitive navigation — especially important for fitness newcomers. He also participated in discussions about color schemes, typography, and animations to be used in the app.

Klimentii Chistyakov
Klim worked on the architecture of the Flutter-based mobile app. He designed the project structure, implemented basic architectural patterns (MVVM and Bloc), configured routing, and started building screen logic. Klim also initiated the integration of the mobile client with backend services to enable data exchange related to users, workouts, and progress tracking. He actively tested the app’s performance and is already working on making the interface as responsive and device-adaptive as possible.

Saidaziz Kadirov
Said focused on the frontend architecture of the web version of NeuroCoach. He designed the structure, selected necessary libraries, and started coding the main pages: profile, workouts, and progress dashboard. He collaborated closely with Daniil to maintain a consistent design system across both mobile and web platforms. Said also built initial components for displaying user progress and configured communication between the frontend and backend via REST API. His goal is to make the web interface user-friendly for regular users and scalable for potential B2B clients like fitness clubs.
## Confirmation of the code's operability

We confirm that the code in the main branch:
- [ ] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).