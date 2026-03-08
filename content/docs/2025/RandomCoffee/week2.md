---
title: "Week #2"
---

# **Week #2**

## Detailed Requirements Elaboration

### US1 - Casual Chat Matching for Remote Workers

As a remote worker, I want to be matched once a week with someone based on my interests and schedule, so I can feel less isolated.  
Acceptance Criteria:  
	•	User can select preferred meeting days/times (basic availability setting - out of MVP).  
	•	Matching is based on shared tags/interests.  
	•	User receives a Telegram message with match info once per week.  

### US2 - Social Networking for Students

As a new student, I want to connect with others who share similar hobbies and interests outside my academic program, so I can make friends and integrate into the community more easily.  
Acceptance Criteria:  
	•	Tags can include social or hobby interests (e.g., “hiking”, “video games”).  
	•	Matching considers these tags.  
	•	Profile supports a short “about me” section to enhance context.  

### US3 - Teamwide Networking Tool for HR

As an HR manager, I want a tool that regularly connects employees from different teams through informal conversations, so I can strengthen company culture and break down silos.  
Acceptance Criteria:  
	•	Users can belong to different departments/teams.  
	•	HR dashboard/analytics (out of MVP).  

### US4 - Cross-functional Networking for Team Leads

As a team lead, I want my team members to network outside our group regularly, so they can gain new perspectives, feel more engaged, and bring diverse input to our projects.  
Acceptance Criteria:  
	•	Users can be matched with people outside their immediate team.  
	•	Tag matching logic doesn't prioritize teammates unless tags strongly overlap.  

### US5 - Onboarding Support for New Employees

As a new employee, I want to be matched with more experienced colleagues automatically, so I can better understand the company culture, tools, and unwritten practices.  
Acceptance Criteria:  
	•	MVP supports user-defined tags like “Senior Developer”, “HR”, etc (out of MVP).  
	•	Users can choose whether they want to share their experience or gain new knowledge. (out of MVP).  

### US6 - Match Profile Preview

As a user, I want to receive basic info about my match's background and interests before connecting, so I can prepare meaningful conversation topics and avoid awkwardness.  
Acceptance Criteria:  
	•	Match message includes: Name, description, and selected tags.  
	•	Message is sent via Telegram bot once weekly.  

### US7 - Opt-in/Opt-out Matching Control

As a Telegram user, I want to easily opt in or out of weekly matching, so I can participate only when I have time and feel socially ready.  
Acceptance Criteria:  
	•	User can toggle a participation switch (optional in MVP)  
	•	Opted-out users are excluded from the next matchmaking cycle.  

## Prioritized backlog

Approximate backlog can be found [here](https://app.plane.so/randomcoffee/projects/). Tasks can change over time. New, more technical and detailed tasks will be compiled from current ones.
## User Flow
User flow for [MVP and Final version](https://www.tldraw.com/f/37VWdlc4Mts0bzYcR4qxh?d=v-1384.2649.6367.3980.kNT5Vq7od4SeH8C180OHN)

## Project specific progress

### Frontend

User creation page: name, surname, description with automatic name and surname substitution from Telegram account.  
[Screenshots](https://www.tldraw.com/f/37VWdlc4Mts0bzYcR4qxh?d=v-16447.-5083.13360.8350.kNT5Vq7od4SeH8C180OHN)  

### Backend

Bot Service: the basic bot service structure for handling updates, executing commands, and managing consumer logic within the bot service has been added.

API-Gateway: an API-gateway component project initialization.

### ML
The model architecture for tags selection has been developed. The dataset collection and preparation has started.  


# Weekly commitments

## Individual contribution of each participant
The tasks that were done by several people are duplicated. they are not inserted by accident.  
1. **Anastasia Mitiutneva**:  
developed backend initial [project architecture](https://www.tldraw.com/f/37VWdlc4Mts0bzYcR4qxh?d=v2569.-593.2535.1585.kNT5Vq7od4SeH8C180OHN)  
formulated project requirements (see section *Detailed Requirements Elaboration*)  
created backlog for each team: [Frontend,](https://app.plane.so/randomcoffee/projects/5f8e4b92-c3fc-499e-905d-f8765dabcc14/issues/) [Backend,](https://app.plane.so/randomcoffee/projects/9afd4e61-7649-4a59-bcb7-6aa373bad7db/issues/) [ML,](https://app.plane.so/randomcoffee/projects/09b5e856-9558-4344-9c95-8a7220fb46a0/issues/) [DevOps](https://app.plane.so/randomcoffee/projects/3dfe4a85-bba6-4117-b7e3-4d250c651f80/issues/)  
created User Flows (see section User Flow)  
initial [database schema](https://www.tldraw.com/f/37VWdlc4Mts0bzYcR4qxh?d=v5114.1484.2387.1492.kNT5Vq7od4SeH8C180OHN) for Profile Service  
2. **Maksim Al Dandan**: Bot Service structure and API-Gateway project initialization, defined 3 API endpoints (without authorization headers), initial database schema for Profile Service, Profile Service initialization  
[Pull request 1](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/12)  
[Pull request 2](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/13)  
[Pull request 3](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/16)  
[Pull request 4](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/18)  
3. **Aleksandr Andreev**: user creation page in mini-app, defined 3 API endpoints (without authorization headers), initial database schema for Profile Service  
[Pull request](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/17)  
4. **Ivan Ilyichev**: collected resume datasets:  
[Resume Dataset 1](https://www.kaggle.com/datasets/saugataroyarghya/resume-dataset?resource=download)  
[Resume Dataset 2](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset)  
[Resume Dataset with tech fields](https://www.kaggle.com/datasets/jillanisofttech/updated-resume-dataset)  
[Dating app user data](https://www.kaggle.com/datasets/anandshaw2001/dating-dataset)  
5. **Rail Sabirov**: added datasets to our project, started preprocessing, developed model design for tags selection  
[Pull request 1](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/14)  
[Pull request 2](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/15)  

## Plan for Next Week
### Backend:  
Database schema for Profile Service implementation.  
Interaction with ML to get user matches.  
Endpoint to get user matches.  
### Frontend:  
Home page and match partner info page.  
Connect frontend components to backend APIs.  

### ML/Data Science:  
Matchmaking algorithm based on tags and bio using Evolutionary Algorithms  

## Important mention

We have updated MVP and Final project features. See Week 1 report.

## Confirmation of the code's operability

We confirm that the code in the main branch:  
✅ In working condition.  
✅ Run via docker-compose (see `README.md`).

---

### Endnote
If some links don't open, please contact Team Lead Anastasia Mitiutneva (@Mituttta) through Telegram.