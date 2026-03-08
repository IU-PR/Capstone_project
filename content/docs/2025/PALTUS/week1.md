# Practicum Project  
PALTUS team. Report 1  

## Project name: PALTUS: Personalized Adaptive Learning & Time Utilization System

## Code repository:
https://github.com/IU-Capstone-Project-2025/PALTUS  

## Project Idea  
An AI-powered self-learning planner that helps users create personalized study plans for any topic, using AI-model to generate lessons, structure schedules, and track progress with gamification to maintain engagement. User can add a course using AI-model interaction: user writes that he wants to learn some discipline, adds amount of lessons and available time, then AI-model generates a full course depending on user’s preferences and requested topic. The main goal - courses are built to fit user’s comfort and free time. Lessons include an option to edit the course model or lesson topics, add notes on each lesson and see the description of the generated course. Everything is customisable individually, starting from lesson amount and lesson duration, ending with calendar dates and time. There will be an option to give feedback to in a chat with AI-model after lesson or a course.

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

## Brainstorming   
**Ideas during brainstorming**  
1. **AI Study Planner (Chosen idea)** — An AI-powered self-learning planner that helps users create personalized study plans for any topic, using AI-model to generate lessons, structure schedules, and track progress with gamification to maintain engagement.  
2. **Smart Scheduler Bot** — A Telegram bot that understands free-form user input about upcoming tasks or events, adds them to a calendar, and sends reminders in advance. Could be integrated with Google Calendar API.  
3. **MeetDev** — A web platform to help developers find pet projects and teammates by stack and experience level. Aimed at beginners looking for practice and teams searching for collaborators.  
4. **CarsToBuy** — A web service that aggregates reviews, listings from popular marketplaces, and technical data for each car model to help users make informed purchasing decisions.  

## Brief market research / problem validation  
Application analogues:
The Habitica and Life RPG applications allow you to create tasks, receive rewards for completing them, and buy various equipment, pets, and skills for in-app currency. The Todoist app motivates through points for completing tasks
Coursebox.ai and MiniCourse Generator generates courses based on the provided materials (videos, docs)
Our app combines the possibilities of creating a course using AI and tracking progress and maintaining motivation through game elements.

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

## Weekly commitments #
1. Sergey Knyazkin (lead):
   * Configured Docker for frontend
   * Added Frontend configuration (boilerplate)
   * Created design in Figma
2. Aidar Sarvartdinov:
   * Created overall idea and most functions
   * Added backend configuration
3. Amir Fayzullin:
   * Created a prompt for AI-model
4. Ramazan Gizamov:
   * Wrote report
   * Helped with design in Figma
5. Igor Dubrovsky
   - Explored available LLM models and their API to utilize them in the project
   - Configured Docker for backend
6. Danil Demin
   - Suggested format for JSON used in prompt
