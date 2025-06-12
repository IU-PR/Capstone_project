# Week #1

## Project description

### Project name: *Solar Wind*

**Code repository**: https://github.com/IU-Capstone-Project-2025/Solar-Wind

### Problem statement

Keeping yourself motivated and consistent with your workout routine can be very challenging. The solution is to find a like-minded person with the same sports interests and goals: workout partners stay motivated together and push each other. We decided to create a convenient platform that will help people to find their own sport community with respect to partners' avaliability. 

### Project overview
*Solar Wind* is a social matching app designed to connect people based on shared sports and fitness interests. Users specify their preferred activities, locations, and availability, and the app suggests compatible partners. 
Whether you're looking for a workout partner, or just want to meet new people who love staying active, this is the place to start. From casual joggers to competitive players — everyone is welcome.

**Key Features:**

- Personalized matching: user feed suggests people with similar sports preferences, schedules, and locations.
- Profile customization: add sports interests, skill levels, and availability.
- Direct Telegram integration: after users have added each other as friends within the app, they can redirect to Telegram chat for further coordination.
- Community-oriented: encourages local meetups and long-term fitness relationships.

### Team Members

| Team Member                             | Telegram Alias   | Email Address   | Team Role                                          |
|-----------------------------------------|------------------|-----------------|---------------------------------------------|
| Daria Nikolaeva  (Team Leader)     | @aalikorn | da.nikolaeva@innopolis.university | iOS-developer | 
| Maria Ilyina         | @abu_blood | m.ilyina@innopolis.university | backend-developer | 
| Amir Aminov            | @amirhan322 | a.aminov@innopolis.university | designer | 
| Polina Kuzminykh            | @sarrtr | p.kuzminykh@innopolis.university | project manager | 
| Ivan Lobazov            | @XriXis | i.lobazov@innopolis.university | backend-developer |

## Brainstorming

### Ideas during brainstorming

1. **Activity-Based Matching (Chosen Idea)**
- Users select sports, locations, and times to find partners.
- Solves the core problem of mismatched preferences in existing apps.

2. **In-App Training Tracker**
- Integrated workout logs and progress sharing with compatible partners.
- Rejected for MVP: focus first on social matching.

3. **Local Event Integration**
- Partner with gyms/sports clubs to promote group events.
- Future Consideration: Requires third-party collaboration.

4. **Healthy Habit Tracker**
- Users log daily habits and see friends’ progress to foster motivation through friendly competition.
- There are already many apps in this area (e.g., Habitica, Streaks, Apple Health integrations) that offer similar or more advanced features.

### Brief market research 

After a brief market research in App Store for our primary idea (Activity-Based Matching) we concluded that existing apps are either generic (Meetup, Timeleft) or too loosely tied to sport and time (Strava):

- Meetup - a platform for holding informal meetings of people united by common interests.
- Strava - a service for tracking athletes' activity using mobile devices. 
- Timeleft - a service for matching with like-minded people for a shared meal.

*Solar Wind* will combine the best parts of already existing solutions: matching with compatible partners based on common sport interests with respect to schedules and avaliability and supporting motivation for staying active. 

## Basic requirements

### Target users and their primary needs

Target users are young adults (18-30) who want to connect with others for sports, workouts, and fitness activities.

Their primary needs:
- social motivation - encouragement from like-minded people.
- convenience - an easy way to match with people with similar sport interests, locations, and schedules. 
- community - meetings with people who share the passion for an active lifestyle.

### User stories

1.  As a new user, I want to set up a profile with my preferred sports, location, and availability, so the app can suggest compatible activity partners.
2. As a registered user, I want to browse and filter potential matches by sport, location, and availability, so I can find partners suited to my preferences.
3. As a registered user, I want to view a match’s profile and open a Telegram chat with him/her, so we can communicate privately.

### Initial scope

**IN for the MVP:**

- user registration and profile creation, identity verification
- profile management
- main page with feed of users
- selection of preference tags (location, time, sports, etc.)
- adding friends
- redirection to Telegram chat

**OUT for the MVP:**

- geolocation
- training recordings and training calendar
- user posts
- Android support 
- chats inside the app

## Tech-stack

**Frontend:** 
UIKit and modular SwiftUI (for stability and flexibility) + Clean Swift (for clear architecture) + Alamofire (for convenient networking) + Kingfisher (for fast image loading and caching)

**Backend:**
Java 23.0 (for strict typing and performance) + Spring Boot (fast development, enterprise features) + Hibernate (ORM, caching). 
Combines stability, scalability, and clean architecture to match the iOS frontend’s robustness.

**Database:**
PostgreSQL (open-source, easy to work with) + Redis (for caching, fast for data access)

## Weekly commitments

### Individual contribution of each participant

Daria Nikolaeva (iOS-developer):

- Organized the structure of the frontend.
- Started writing the Welcome Screen.
GitHub commits: 
    1. https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/fa7596eaf1502df530d7d22a12ca6ee89dc70b91
    2. https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/cf77a9cb7ba4d196f5fd08df60121870beab66d3

Maria Ilyina (backend-developer):

- Created initial structure of backend.
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/2cd07fd8d0d675831861093ee19e5177f205ac49

Amir Aminov (designer):
- Designed logo and userflow schema with screen pages in Figma.
Figma page: https://www.figma.com/design/si98563MfBSXuDtOfV8655/FitFlame?node-id=27-388&t=qyV0IP1eKj0udmmA-0

 Polina Kuzminykh (project manager):
 
 - Scheduled weekly team meeting. 
 ![Weekly meeting](https://github.com/IU-Capstone-Project-2025/Solar-Wind/blob/main/content/images/week1_meeting.png)
 - Organized GitHub issues in Kanban board in GitHub Projects. 
 ![Kanban board](https://github.com/IU-Capstone-Project-2025/Solar-Wind/blob/main/content/images/week1_kanban.png) 
Kanban board: https://github.com/orgs/IU-Capstone-Project-2025/projects/3/views/1
 - Wrote weekly report including problem statement, project description, market research, and user stories.

Ivan Lobazov (backend-developer) 
- Added boilerplate code for backend.
- Made project dokerizarion.
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/4907aef08128afeee4cd143a501453ced7613c1f 

## Next steps

**Frontend**
- Finish the user's registration/login path
- Write a network layer to access the API

**Backend**

- Create data models
- Design an API
- Start the implementation with authorization and the feed

**Design**

- Complete registration route schema
- Design home screen and profile change logic

## Confirmation of the code's operability

We confirm that the code in the main branch:
-  In working condition.
-  Run via docker-compose.