# Week #3

**Project name**: *Solar Wind* 
**Code repository**: https://github.com/IU-Capstone-Project-2025/Solar-Wind

| Team Member                             | Telegram Alias   | Email Address   | Team Role                                          |
|-----------------------------------------|------------------|-----------------|---------------------------------------------|
| Daria Nikolaeva  (Team Leader)     | @aalikorn | da.nikolaeva@innopolis.university | iOS-developer | 
| Maria Ilyina         | @abu_blood | m.ilyina@innopolis.university | backend-developer | 
| Amir Aminov            | @amirhan322 | a.aminov@innopolis.university | designer | 
| Polina Kuzminykh            | @sarrtr | p.kuzminykh@innopolis.university | project manager | 
| Ivan Lobazov            | @XriXis | i.lobazov@innopolis.university | backend-developer |

## Implemented MVP features

In MVP we implemented 'user matching' and partially 'registration of a new user by filling out a questionnaire' end-to-end user journeys.

Implemented features:

- During registration user can choose a city, training categories, day of a week when he is avaliable, and write his name with short introduction of himself.
- A feed of users on the main page with users' names, locations, prefered sports and a few words about them.
GitHub commits:
1. https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/40c432405797d8e480622c456669a44dd74cfe73
2. https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/de713c715f92d4e08e1b29bae7d579100e8e45ef#diff-8666bda38be0e15c63494832743beb67b6cdb0b96cb3a4d29ff13d1a958d7015
3. https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/7b3332bcc42d39f1ba369ecd9456e79c5e637305
- Matching system: user can like other users.
GitHub commits:
1. https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/4ab288426f1cc0bc9fed1d8af8fd162899ccdb03

## Demonstration of the working MVP
Link to video demonstrating the working MVP: https://drive.google.com/drive/folders/1lO29NToFl0WpknMkrCI6qjNsPKmltQHu

## Internal demo
- Fix design issues in frontend.
- Complete the real authentication via Telegram.
- Add more categories for sports.
- Enhance main page (users' feed), make it look more interesting.
        
## Weekly commitments

### TA's last week feedback summary 
- It is recommended to focus on the main functionality of the app for MVP presenatation, leaving aside registration, authorization, and error handling for now.
- The pictures in the report are not displayed outside the GitHub -> we need to fix it.
- To make meetings with TA more productive, we need to prepare a mini-demo with new functionality for each meeting to save time.
- For now our app have 2 end-to-end user journeys:
    - registration of a new user by filling out a questionnaire;
    - user matching.
    
For MVP it is better to prepare the second end-to-end user journey functional.

### Individual contribution of each participant

Daria Nikolaeva (iOS-developer):

- Finished registration route.
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/69ecacf341f3d1882c46a10f78fb3b1775505893
- Implemented basics of main page.
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/466b89d0eceab9db23b403ed15f550dff376fc6f

Maria Ilyina (backend-developer):

- Developed service for matching user profiles with similar ones and recommendations.
- Corrected endpoints for filling up personal info.
GitHub commits: 
1. https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/590c9b0a0cfd87754af461594bb109db9fae36c5
2. https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/bfe23060e1e4059b2f962db1e22c13c1cf61070e


Ivan Lobazov (backend-developer):

- Developed 'like' service.
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/4ab288426f1cc0bc9fed1d8af8fd162899ccdb03
- Made a temporary solution for notification service via manual pooling.
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/d72b685160d6f15c03b29ff677a458c75fc0a2c1
- Prepared security configuration.
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/5a2fe73ffd287436b061a1ed6435ce7eadb4a166
- Organized basic CI/CD.

Amir Aminov (designer):

- Designed 'users matching' userflow, 'exchange of contacts' userflow.
- Designed user profile (your own and others').
- Designed page with matchings list.
Figma page: https://www.figma.com/design/si98563MfBSXuDtOfV8655/FitFlame?node-id=129-1161&p=f&t=yX6EjVHpVC9d2q2j-0

Polina Kuzminykh (project manager):
 
 - Scheduled weekly team meeting. 
 ![Weekly meeting](https://github.com/IU-Capstone-Project-2025/Solar-Wind/blob/main/content/images/week3_meeting.png?raw=true)

 - Wrote weekly report including description of MVP features and summary of TA's feedback from last week.
 - Updated project backlog.
    Kanban board: https://github.com/orgs/IU-Capstone-Project-2025/projects/3/views/1
- Fixed issue in previous reports connected with image display.

### Plan for next week


**Frontend**
- Fix bugs in registration.
- Enhance error processing and forms validation.
- Create basics of user profile.

**Backend**
- Adjust security services  on user-server communication and on service-service communication.
- Handle errors.
- Develop tests.
- Enhace existing services.

**Design**
- Design 'change of profile' userflow.

### Confirmation of the code's operability

We confirm that the code in the main branch:
-  In working condition.
-  Run via docker-compose.