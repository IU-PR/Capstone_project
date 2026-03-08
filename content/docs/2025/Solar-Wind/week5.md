# Week #5

**Project name**: *Solar Wind* 
**Code repository**: https://github.com/IU-Capstone-Project-2025/Solar-Wind

| Team Member                             | Telegram Alias   | Email Address   | Team Role                                          |
|-----------------------------------------|------------------|-----------------|---------------------------------------------|
| Daria Nikolaeva  (Team Leader)     | @aalikorn | da.nikolaeva@innopolis.university | iOS-developer | 
| Maria Ilyina         | @abu_blood | m.ilyina@innopolis.university | backend-developer | 
| Amir Aminov            | @amirhan322 | a.aminov@innopolis.university | designer | 
| Polina Kuzminykh            | @sarrtr | p.kuzminykh@innopolis.university | project manager | 
| Ivan Lobazov            | @XriXis | i.lobazov@innopolis.university | backend-developer |

## Feedback

### Testing Sessions
Here are summaries of users' reviews of our app (all users are our classmates):

**User 1:**
During registration user tried to select a lot of sport tags but UI got broken. Also she pointed that it would be nice if already selected sports will be highlited in the list to make selection easier. After registration she logout and tried to login again but did not manage.  

GitHub Issues this review inspires:

- highlight which sports have already been selected during registration
- fix: when selecting a large number of tags, the UI breaks
- enable user to login to account after logout

**User 2:**
During registartion user tried to skip Name field, but app did not warn her that username is mandatory, and as a result she could not see anything in the app and error came to the server. During second try user filled in all fields, check feed with the users and return to profile. Here she pointed that it would be good if she could change her profile in case some info become not relevant.

GitHub Issues this review inspires:

- add fields validation during registration (mandatory fields should be filled in)
- add feature to change profile information after registration

**User 3:**
During registartion user managed to skip all fields to see what will happen, but app did not warn him that some fields were mandatory. As a result user did not see anything in the app and also an error came to the server. 

GitHub Issues this review inspires:

- add fields validation during registration (mandatory fields should be filled in)

**General problems**
All users pointed that search bar in city and sport selection did not work. 
GitHub Issues this review inspires:

- fix city and sports search when registering

### Analyze
Based on feedback that was collected during testing sessions new GitHub issues were created:
- https://github.com/IU-Capstone-Project-2025/Solar-Wind/issues/60
- https://github.com/IU-Capstone-Project-2025/Solar-Wind/issues/59
- https://github.com/IU-Capstone-Project-2025/Solar-Wind/issues/58
- https://github.com/IU-Capstone-Project-2025/Solar-Wind/issues/57
- https://github.com/IU-Capstone-Project-2025/Solar-Wind/issues/61
- https://github.com/IU-Capstone-Project-2025/Solar-Wind/issues/62

Almost all of them were assigned P0 or P1 priority because they directly affect core user flows such as registration, login, and profile management.

## Iteration & Refinement
Closed GitHub issues that were created based on feedback:
https://github.com/IU-Capstone-Project-2025/Solar-Wind/issues/57
https://github.com/IU-Capstone-Project-2025/Solar-Wind/issues/59
https://github.com/IU-Capstone-Project-2025/Solar-Wind/issues/58

Other features will be implemented next week.

## Documentation 
API Specification:

Each microservice has its own Swagger UI documentation:

- [Likes Service API](https://solar-wind-gymbro.ru/likes/swagger-ui.html)
- [Profiles Service API](https://solar-wind-gymbro.ru/profiles/swagger-ui.html)
- [Notifications Service API](https://solar-wind-gymbro.ru/notifications/swagger-ui.html)
- [Deck Shuffle Service API](https://solar-wind-gymbro.ru/deckShuffle/swagger-ui.html)

Frontend and backend teams can reference only the service they need. Also, as new services are added, they can have their own Swagger docs without cluttering others.

Full Postman collection:
- [Solar Wind API on Postman](https://www.postman.com/grey-satellite-701545/solar-wind/overview)

Groups all endpoints together in one place for full-system testing.

## Weekly commitments

### TA's last week feedback summary 
- We can consider that our staging is ready when we deploy production - we do not need second server.
- We need to fix deployment link - it did not work.
- For project presentation we need to add more users with photos to the app to make it look more interesting.

### Individual contribution of each participant

Daria Nikolaeva (iOS-developer):
- Implemented search of cities and sport types.
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/f4c9a8b70b272f1f37a57839e4e8bd957c1f5437
- Implemented fields validation during registartion.
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/ad446ab0192b52082e38d1c396d0c24ad5ea93b2
- Created screen "My profile".
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/b7a80d43dbf20494a858339b339cba3aaafe1fa7


Maria Ilyina (backend-developer):
- Add the ability to filter a set of users in the feed.
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/29076b19b4e3046a4135cfa35a9cc7c74b73fe16

Ivan Lobazov (backend-developer):
- Implemented a mechanism of authorization and authorized access.
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/94f5809d7510a14fdd57931737f173a0cc240ac0
- Implemented a caching of the most massive data - user decks.
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/ac52df34c1dca0f1fe3fb2fb5e0c059dbbbdbbb6

Amir Aminov (designer):
- Designed user search logic.
- Update pages of other people's and your profiles with the addition of new parameters of age and gender.
Figma page: https://www.figma.com/design/si98563MfBSXuDtOfV8655/FitFlame?node-id=129-1161&t=jFzpIg805e50cmF7-1

Polina Kuzminykh (project manager):
 
 - Scheduled weekly team meeting. 
 ![Weekly meeting](https://github.com/IU-Capstone-Project-2025/Solar-Wind/blob/main/content/images/week5_meeting.png?raw=true)
 - Wrote weekly report including summary of TA's feedback from last week.
 - Wrote project README.
 - Created new issues based on usability testing sessions and updated project backlog.
    Kanban board: https://github.com/orgs/IU-Capstone-Project-2025/projects/3/views/1

### Plan for next week

**Frontend**
- Finish implementation of logic of user likes in frontend.
- Add feature to enable users to add their photos in profile.
- Finish verification via Telegram.
- Fix all bugs and flaws that were revealed during testing sessions.

**Backend**
- Fix all remaining bugs and flaws.
- Enhance existing tests and write new ones for new functionality.
- Add feature to enable users to add their photos in profile.

**Design**
- Change design of account verification via telegram

**Other**
- Finish README.
- Prepare draft presentation slides for final project  presenation.
- Measure performance of application.

### Confirmation of the code's operability

We confirm that the code in the main branch:
-  In working condition.
-  Run via docker-compose.