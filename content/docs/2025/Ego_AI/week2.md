# Week 2

# Detailed Requirements Elaboration

## Updated/detailed user stories

- As a user, I want to chat with the AI in natural language (e.g., "Reschedule my meetings for today") so I can manage tasks conversationally.

- As a user, I want the AI to answer follow-up questions about my schedule (e.g., "What's my next task?") so I can stay informed without checking manually.

- As a user, I want to add or edit tasks by speaking (e.g., "Add a gym session at 6 PM") so I can capture ideas hands-free.

- As a user, I want the AI to transcribe my brainstorming sessions into actionable notes so I can organize ideas faster.

- As a user, I want the AI to automatically shift tasks if I'm running late so my schedule stays realistic.

- As a user, I want the AI to suggest urgent task rescheduling (e.g., "Move this deadline due to low priority") so I can focus on what matters.

- As a user, I want the AI to remind me of habits (e.g., "You usually read at 9 PM") so I can maintain routines.

- As a user, I want the AI to propose breaks based on my productivity patterns so I can avoid burnout.

- As a user, I want the AI to auto-categorize tasks into "To-Do/Doing/Done" columns so I can visualize progress.

- As a user, I want the AI to flag stalled tasks (e.g., "This hasn't moved in 3 days") so I can take action.

- As a user, I want the AI to suggest indoor tasks (e.g., "Work on emails") when bad weather is forecasted so my plans stay flexible.

- As a user, I want the AI to recommend nearby coffee shops for meetings based on my preferences (e.g., "Quiet, with WiFi").

- As a user, I want a weekly report showing my peak productivity hours so I can plan deep work accordingly.

- As a user, I want the AI to compare planned vs. actual task time so I can improve time estimates.

- As a user, I want two-factor authentication for my connected accounts so my data stays secure.

- As a user, I want a free tier with basic features (e.g., task tracking) so I can test the tool before paying.

## Requirements

 We considered all the user stories and marking those that are either difficult to implement or not necessary, and based on this we define this requirements:

- Account creation and data saving
- Calendar with tasks (basic CRUD functions)
- AI chat
- Speech-To-Task
- Dynamic rescheduling with AI
- Smart suggestions and reminders
- Kanban board with AI for some projects
- Weather and place recommendations
- Visualization and analytics of user productivity

We've distributed all requirements into weeks:

- **Week 2**
   - Account creation and data saving
   - Calendar with tasks (basic CRUD functions)
   - AI chat(tech part)
- **Week 3**
   - AI chat(final part with frontend)
   - Dynamic rescheduling with AI
- **Week 4**
   - Smart suggestions and reminders
   - Speech-To-Task
- **Week 5**
   - Weather and place recommendations
- **Week 6**
 - Visualization and analytics of user productivity

## Project Architecture

![Architecture](https://github.com/setterwars/Capstone-project-2025/blob/main/arch.png?raw=true)

### Core Components (Dockerized Microservices)

1. Backend (Server)
   - Handles the core logic and processing of calendar data.

   - Exposes REST APIs for interaction with both the frontend and AI agent.

   - Interfaces with a database to store and retrieve calendar data.

   - Processes incoming calendar data and responds to AI-generated suggestions or user requests.

2. Database
   - Responsible for persisting calendar data.

   - Communicates with the backend to store or retrieve events, tasks, or other time-related data.

   - Runs in a Docker container, managed with Docker Compose.

3. Web Interface
   - A user-facing frontend application.

   - Connects to the backend via REST API.

   - Provides a graphical interface for users to manage calendar entries.

   - Also containerized with Docker for isolated deployment.

4. Docker Compose
   - Manages the lifecycle and orchestration of the backend and frontend containers.

   - Ensures both services are networked correctly and can communicate via internal Docker networking.

### AI Agent Integration

- The AI agent interacts with the backend via API requests.

- It can enhance the calendar functionality through:

   - DeepSeek API

   - ChatGPT API

   - Hugging Face Transformers API

- Possible tasks for the AI agent include:

   - Natural language interpretation of user input.

   - Suggesting optimal scheduling based on user behavior or preferences.

   - Summarizing tasks, rescheduling, detecting conflicts



## User flow

Based on the choosen requirements, we have developed a user flow that will underpin our project.

![User flow](https://github.com/setterwars/Capstone-project-2025/blob/main/user_flow.png?raw=true)

1. Main Page with Basic Information

   - This is the landing page where users are introduced to the application.

   - It contains general information about the service and encourages users to register.

2. Registration Page

   - After viewing the main page, users proceed to register for access to the platform.

   - Successful registration leads to the main interface.

3. Main Page

   - After registration, users enter the main page of the application.

   - This serves as the central hub for all user activity.

4. Topbar Navigation (highlighted in pink)

   - From the main page, users can navigate through the app using a topbar menu.

   - This allows quick access to all core features of the platform.

5. Core Features (Accessible via Topbar Navigation):

   - Calendar: Manage personal events and schedules.

   - Dashboard / Analytics: View user-specific data and visual analytics.

   - Chat with AI: Engage in interactive conversations with an AI assistant.

   - Recommendations: Receive personalized suggestions based on user data.

   - Geo/Weather Assistant: Access location-based services and weather forecasts.

## Prioritized Backlog

**Link to the backlog**:
https://github.com/orgs/IU-Capstone-Project-2025/projects/1

**Backlog screenshot**:

![Backlog](https://github.com/setterwars/Capstone-project-2025/blob/main/backlog.png?raw=true)

All issues are divided into iterations. In total we have 6 iterations. Also, as you can see, all issues are prioritized in the backlog. The issues have their size indicated to estimate the time needed to complete each task.

# Project-specific progress

## Frontend

This week we designed the frontend and start develop it.

**Link to the Figma design:** https://www.figma.com/design/um3jVUbRhCpPOtH0rnKo8D/EGO-AI--Copy-?node-id=0-1&p=f&t=U4B3WouucLmUfJRt-0

In this week will be implemented to 2 pages of the frontend part. Firstly it is calendar page. And In this week will be implemented skeleton of the main page.

**Image of ready frontend pages**

**Calendar page**
![Calendar page](https://github.com/setterwars/Capstone-project-2025/blob/main/calendar_page.png?raw=true)

**Skeletone of the main page**

![image 1](https://github.com/setterwars/Capstone-project-2025/blob/main/first_image_skeletone.png?raw=true)

![image 2](https://github.com/setterwars/Capstone-project-2025/blob/main/second_image_skeletone.png?raw=true)

![image 3](https://github.com/setterwars/Capstone-project-2025/blob/main/image_3_skeletone.png?raw=true)

![image 4](https://github.com/setterwars/Capstone-project-2025/blob/main/image_five_skeletone.png?raw=true)

## Backend

In this week In backend side will be realized base CRUD logic and authorization via google account. Also will add connection to the database and database initialization.

Link to API documentation provided in repository README.md

**Images with API documentation**

![API image](https://github.com/setterwars/Capstone-project-2025/blob/main/Api%20phot.jpg?raw=true)

**Google Account usage**

In this week we implement authentication using google account. In the next week we planed to implement integration with google calendar.

![Google auth 1](https://github.com/setterwars/Capstone-project-2025/blob/main/photo_2025-06-17_12-37-45.jpg?raw=true)

![Google auth 2](https://github.com/setterwars/Capstone-project-2025/blob/main/photo_2025-06-17_12-37-45%20(2).jpg?raw=true)

## ML

In week #2 we added:

- voice chat with Whisper
- chat with LLM Architecture

For chat with LLM used **deepseek-r1:1.5b**. For voice model used **whisper** and for embedding used model **mxbai-embed-large**

In the next week for LLM chat we will create pages in frontend and we will connect this page with this LLM chat

## DevOps

This week, our DevOps engineer worked on automating project deployments by setting up a custom script to seamlessly push updates to the server. 
Manually deploying code changes is time-consuming and error-prone. To improve efficiency, we needed a reliable automation script that would:
- Fetch the latest code from the repository
-  Run necessary build steps (e.g., dependency installation, compilation)
-  Securely transfer files to the production/staging server
-  Restart services if required

**Deployment Script snippet**

![deployment script](https://github.com/setterwars/Capstone-project-2025/blob/main/deployment_script.png?raw=true)

**CI/CD Script snippet**

![CICD](https://github.com/setterwars/Capstone-project-2025/blob/main/CI_CD_script.png?raw=true)

# Weekly commitments

## Individual contribution of each participant

- **Dmitriy Ryazanov**: Write account creation via Google, edite structure of the backend

   **Links:**
   
   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/736fbeffc8d1623b6114afb88b900dfd1d2cd6d0

   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/429f8d86277e4d736e69a55ff39ed4bff1b4c488



- **Diana Tsoi**: Frontend Design, create skeletone of the main page

   **Links:**

   - Link to the Figma design: https://www.figma.com/design/um3jVUbRhCpPOtH0rnKo8D/EGO-AI--Copy-?node-id=0-1&p=f&t=U4B3WouucLmUfJRt-0

- **Stepan Sarantsev**: Implemented CRUD (Calendar system), wrote database initializer

   **Links:**

   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/939ba7b97afb306da79af3e93c77f46466b5349d

   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/927cc22a48a63ee6446826191cadc2664542e1af

- **Andrey Zhdanov**: Added voice chat with Whisper, implemented chat with LLM, added temporary calendar and vector DB support

   **Links:**
   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/7ddf982abdd316508f080808a724794c54909132

- **Artyom Lapin**: Create auto deploy script for github CI/CD

   **Links:**

   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/32d78cc9990f6067cf11b6aa3d04e21c3a401c20


- **Mikhail Sofin**: Create calendar frontend page

   **Links:**
   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/b924176e6e2a77e6772856bfd866aa9e86f3e1d8

- **Salavat Zaynulin**: Wrote report, created user flow diagram and architecture diagram, backlog creation, work on design

   **Links**
   - Link to the online board: https://excalidraw.com/#room=0a55400de3e2cf3441c6,bBFRwjpDKsK64Lti2_I28A

   - Link to the figma: https://www.figma.com/design/um3jVUbRhCpPOtH0rnKo8D/EGO-AI--Copy-?node-id=0-1&p=f&t=U4B3WouucLmUfJRt-0


## Plan for Next Week

Next week we plan to implement these functions: 
 - Dynamic rescheduling with AI
 - Smart suggestions and reminders
 - frontend of the AI chat and connection with models

We also plan to test the parts of the project we've created so far and fix any bugs we find.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- Is in working condition
- Runs via Docker Compose
