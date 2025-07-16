# Week #6

**Project name**: *Solar Wind* 
**Code repository**: https://github.com/IU-Capstone-Project-2025/Solar-Wind

| Team Member                             | Telegram Alias   | Email Address   | Team Role                                          |
|-----------------------------------------|------------------|-----------------|---------------------------------------------|
| Daria Nikolaeva  (Team Leader)     | @aalikorn | da.nikolaeva@innopolis.university | iOS-developer | 
| Maria Ilyina         | @abu_blood | m.ilyina@innopolis.university | backend-developer | 
| Amir Aminov            | @amirhan322 | a.aminov@innopolis.university | designer | 
| Polina Kuzminykh            | @sarrtr | p.kuzminykh@innopolis.university | project manager | 
| Ivan Lobazov            | @XriXis | i.lobazov@innopolis.university | backend-developer |

## Links

**Deployment:**
API:
- [Likes Service API](https://solar-wind-gymbro.ru/likes/swagger-ui.html)
- [Profiles Service API](https://solar-wind-gymbro.ru/profiles/swagger-ui.html)
- [Notifications Service API](https://solar-wind-gymbro.ru/notifications/swagger-ui.html)
- [Deck Shuffle Service API](https://solar-wind-gymbro.ru/deckShuffle/swagger-ui.html)

**API Docs:**
Each microservice has its own Swagger UI documentation:

- [Likes Service API](https://solar-wind-gymbro.ru/likes/swagger-ui.html)
- [Profiles Service API](https://solar-wind-gymbro.ru/profiles/swagger-ui.html)
- [Notifications Service API](https://solar-wind-gymbro.ru/notifications/swagger-ui.html)
- [Deck Shuffle Service API](https://solar-wind-gymbro.ru/deckShuffle/swagger-ui.html)

Full Postman collection:
- [Solar Wind API on Postman](https://www.postman.com/grey-satellite-701545/solar-wind/overview)

**Design:**
Figma pages with app design and userflow diagrams:

 - [ Registration flow](https://www.figma.com/design/si98563MfBSXuDtOfV8655/FitFlame?node-id=0-1&p=f&t=0YEz2ac3MJ8uvHij-0)
- [Main flow](https://www.figma.com/design/si98563MfBSXuDtOfV8655/FitFlame?node-id=129-1161&p=f&t=ZYFIR9AQSHxESbqE-0)

**Demo:** https://drive.google.com/file/d/1y5Siws0zB_LL7GOsayok_Wlz7wFygmLg/view?usp=drivesdk

## Final deliverables
### Project overview
Solar Wind is a social matching iOS app designed to connect people based on shared sports and fitness interests.

**Problem statement:** 
Staying consistent with a workout routine is tough — but having a reliable partner makes it easier. Solar Wind solves this by helping users find nearby people with similar fitness goals, interests, and availability. Unlike generic meetup platforms, Solar Wind is focused entirely on building a sport-oriented community with personal matching.

**Target users:**
Young adults (18–30) who want to stay motivated and find compatible workout partners.

**Key features:**
- **Filling out the profile:** Users specify their city and favourite sports.
- **Matching:** Feed suggests other users from which user can choose his partner.
- **Contact with matched people:** After users matched with each other, they can redirect to Telegram chat.

### Features

1. **Verification via Telegram**
    - @SolarWindAuthorization_bot sends a code for athorization after user's "/start" message.
    
2. **Filling out the profile:**
    - search for a city by the first letters in the search bar.
    - search for a specific sports by the first letters in the search bar or choose from a list.
    - specify the user's name and write something about himself in a specific field.
    - specify the user's gender and birthdate.

3. **Matching:**
    - a feed in the main page with other users.
    - user can like other users they like.
    
4. **Contact with matched people:**
    - if users' like is mutual, a button leading to Telegram appears on the notification page.
    
5. **Additional features:**
    - Change of language (RU/EN).
    - Change of theme (dark/lite).

### Tech stack
**Frontend (iOS):**
- UIKit + modular SwiftUI for flexibility and stability
- Clean Swift architecture for maintainability
- Alamofire for HTTP networking
- Kingfisher for image loading and caching

**Backend:**
- Java 23.0
- Python 3.12
- Spring Boot for RESTful services
- Hibernate for ORM and caching

**Database:**
- PostgreSQL (primary data storage)
- Redis (caching layer)

### Setup instructions for local run

1. Clone this repo:
```bash
git clone https://github.com/your-username/solar-wind.git
cd solar-wind
```
   
2. For iOS frontend:
- Open ``Solar-Wind-iOS-app/Solar-Wind-iOS-app.xcodeproj/project.xcworkspace`` in Xcode
- In Xcode, go to:
    `File` → `Packages` → `Resolve Package Versions`
To refresh all packages to their latest compatible versions:  
   `File` → `Packages` → `Update to Latest Package Versions`
- Build and run on simulator or device
    
3. For backend:
- Prerequisites: [Docker](https://www.docker.com/products/docker-desktop) and [GNU Make (for Windows)](https://www.gnu.org/software/make/) installed.

```bash
cd backend
make all
```

## Presentation draft
[Here](https://docs.google.com/presentation/d/1hQhK7SUbRs6wKJnNa03cGYqfkkTK9B-y0uINCLNjwpQ/edit?slide=id.g342bf66e35b_2_104#slide=id.g342bf66e35b_2_104) is the draft of the final presentation.

## Weekly commitments

### TA's last week feedback summary 
It would be better if we will include ML into the project (as recommendation system for users), otherwise we should justify its absence in the final presentation. 

### Individual contribution of each participant

Daria Nikolaeva (iOS-developer):
- Rewrote the app on Flutter (now it's cross-platform).
- Added localization.
- Added a dark theme.
- Completed all the requests.
- Fixed bugs.

GitHub pull request: https://github.com/IU-Capstone-Project-2025/Solar-Wind/pull/68

Maria Ilyina (backend-developer):

- Developed the base for adding photos to user profile.

GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/e1b4f284c151eff1f2e9876015a53fcf26dae268

Ivan Lobazov (backend-developer):
- Fixed bugs:
    - Invisibility of authorization in swagger.
    - Unavailability of resources based on the provided keys.
    - Unavailability of a resource when trying to get it from the cache.

GitHub commits: 
1. https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/63fdb519b0d16e3c718ef244936c4f4c596c0c55
2. https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/e7d52899c249407767e4428ab24cc7ba093e3c1a

- Developed the base of ML pipeline. 

Amir Aminov (designer):
- Changed the design of account verification via Telegram to match the current functional solution.

Figma page: https://www.figma.com/design/si98563MfBSXuDtOfV8655/FitFlame?node-id=129-1161&t=jFzpIg805e50cmF7-1

Polina Kuzminykh (project manager):
 
 - Scheduled weekly team meeting. 
 ![Weekly meeting](https://github.com/IU-Capstone-Project-2025/Solar-Wind/blob/main/content/images/week6_meeting.png?raw=true)
 - Wrote weekly report including summary of TA's feedback from last week.
 - Updated project README, made the draft of the final presentation.
 - Updated project backlog.

    Kanban board: https://github.com/orgs/IU-Capstone-Project-2025/projects/3/views/1

### Plan for next week

**Frontend**
- Clean up the code.
- Add localization to the entire application.
- Continue fix bugs.

**Backend**
- Redesign the shuffle system.
- Add photos sending.
- Split db into several servers.

### Confirmation of the code's operability

We confirm that the code in the main branch:
-  In working condition.
-  Run via docker-compose.