# Practicum Project  
PALTUS team. Report 1  

## Project name: PALTUS: Personalized Adaptive Learning & Time Utilization System

## Code repository:
https://github.com/IU-Capstone-Project-2025/PALTUS  

## Project Idea  
An AI-powered self-learning planner that helps users create personalized study plans for any topic, using GigaChat to generate lessons, structure schedules, and track progress with gamification to maintain engagement.

## Problem Statement  
Many students and self-learners struggle to structure their self-study process, leading to inconsistencies and inefficiencies. Existing platforms lack personalization and flexibility, often resulting in lost motivation.

## Team Members 

| Team Member             | Telegram Alias   | Email Address                     | Track                    | Responsibilities                                                                 |
|-------------------------|------------------|-----------------------------------|--------------------------|----------------------------------------------------------------------------------|
| Sergey Knyazkin (Lead)  | @poeticlama      | s.knyazkin@innopolis.university   | Frontend/Design/DevOps   | Creating UX/UI, designing frontend structure, assisting deployment               |
| Aidar Sarvartdinov      | @aidar_sar       | a.sarvardinov@innopolis.university| Backend                  | Creating overall backend structure                                               |
| Amir Fayzullin          | @HoriFa7z        | a.fayzullin@innopolis.university  | Fullstack                | Developing frontend components, assisting backend code                           |
| Ramazan Gizamov         | @ramzeuus        | r.gizamov@innopolis.university    | DevOps/Tech communication| Application deployment, report/presentation writing                              |
| Igor Dubrovsky          | @chomosuce       | i.dubrovsky@innopolis.university  | Backend                  | Writing logic for GPT interaction                                                |
| Danil Demin             | @degradatorus    | da.demin@innopolis.university     | Frontend                 | Creating frontend components and views                                           |

## Brainstorming #  
**Ideas during brainstorming #**  
1. **AI Study Planner (Chosen idea)** — An AI-powered self-learning planner that helps users create personalized study plans for any topic, using AI-model to generate lessons, structure schedules, and track progress with gamification to maintain engagement.  
2. **Smart Scheduler Bot** — A Telegram bot that understands free-form user input about upcoming tasks or events, adds them to a calendar, and sends reminders in advance. Could be integrated with Google Calendar API.  
3. **MeetDev** — A web platform to help developers find pet projects and teammates by stack and experience level. Aimed at beginners looking for practice and teams searching for collaborators.  
4. **CarsToBuy** — A web service that aggregates reviews, listings from popular marketplaces, and technical data for each car model to help users make informed purchasing decisions.  

## Brief market research / problem validation #  
The current learning platforms offer structured courses but limited flexibility and personalization. Many self-learners report a lack of motivation due to rigid course structures and insufficient feedback on progress. Our idea addresses this by generating personalized study plans and tracking individual progress dynamically, which makes learning more adaptable and engaging.

Our validation shows that:
- Many users desire more adaptive learning flows that adjust to their pace and knowledge gaps.
- Existing solutions are not user-centric enough in terms of progress tracking or creating unique, custom-fit courses.

## Basic requirements #  
- AI-generated topic-based study plans  
- Ability to input any study topic  
- Text-based lesson delivery  
- Clear and simple progress tracking system  
- Web-based interface  

## Target users and their primary needs #  
- **Self-learners / students** — need structured and personalized study plans.  
- **Busy professionals** — want to upgrade skills with limited time using adaptive tools.  
- **People preparing for exams / new skills** — require guided, gamified paths to stay motivated.  

## User stories #  
1. As a client, I want a course with structured learning materials to self-learn new skills.  
2. As a client, I need flexibility in my learning schedule to study at my convenience.  
3. As a client, I require clear progress tracking to stay engaged and understand my improvement.  

## Initial scope #  
**Included in MVP:**  
- AI-generated topic-based study plans  
- Text-based lesson delivery  
- Progress tracking  

**Excluded (future iterations):**  
- Calendar integrations  
- Social features  

## Tech-stack #  

### Frontend  
- **Vue.js, Vuetify**  
  *Justification:* Vue.js offers simplicity and reactivity. Vuetify provides ready-to-use, well-designed components, accelerating development and ensuring a clean, consistent UI.

### Backend  
- **Java Spring Boot**  
  *Justification:* Selected for robustness, scalability, and a strong ecosystem for RESTful APIs. Includes powerful tools for authentication, scheduling, and database interactions.
