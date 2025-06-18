# Week #2

**Project name**: *Solar Wind*
**Code repository**: https://github.com/IU-Capstone-Project-2025/Solar-Wind

| Team Member                             | Telegram Alias   | Email Address   | Team Role                                          |
|-----------------------------------------|------------------|-----------------|---------------------------------------------|
| Daria Nikolaeva  (Team Leader)     | @aalikorn | da.nikolaeva@innopolis.university | iOS-developer | 
| Maria Ilyina         | @abu_blood | m.ilyina@innopolis.university | backend-developer | 
| Amir Aminov            | @amirhan322 | a.aminov@innopolis.university | designer | 
| Polina Kuzminykh            | @sarrtr | p.kuzminykh@innopolis.university | project manager | 
| Ivan Lobazov            | @XriXis | i.lobazov@innopolis.university | backend-developer |

## Detailed requirements elaboration

### Prioritized backlog
Kanban board:
https://github.com/orgs/IU-Capstone-Project-2025/projects/3/views/1
### Project specific progress
**Frontend**
- Organized the frontend structure for scalability.
- Implemented basic routing for navigation.
- Developed partially registration page.

**Backend**
- Organized the backend structure for scalability.
- Dockerized the project for deployment.
- Established database schema and connected the profile microservice to PostgreSQL.
- Defined the initial API contract for future integrations.
- Implemented authorization via Telegram.

**Design**
- Created Figma designs for registration and user feeds pages.
- Completed registration userflow schemas.

### Expanded user stories

- As a new user, I want to set up a profile with my preferred sports, location, and availability, so the app can suggest compatible activity partners.
    - As a new user, I want to sign up via Telegram, so that I can register quickly without creating a password.
    - As a new user, I want to select multiple sports from a list, so that partners are suggested based on my activity interests.
    - As a new user, I want to specify my favorite places to do sports, so that partners are suggested based on my preferred sport locations.
    - As a new user, I want to mark my weekly availability, so that partners are suggested based on my availability.
    
- As a registered user, I want to browse and filter potential matches by sport, location, and availability, so I can find partners suited to my preferences.

- As a registered user, I want to view a match’s profile and open a Telegram chat with him/her, so we can communicate privately.
    - As a registered user, I want to view a match's complete sports profile, so that I know if we share enough interests.
    - As a registered user, I want to initiate a Telegram chat directly from a profile, so that we can coordinate without sharing phone numbers.

**Key user stories with acceptance criteria:**

- As a new user, I want to sign up via Telegram, so that I can register quickly without creating a password.
    - AC: After Telegram OAuth, the user is automatically registered and redirected to the profile setup.
- As a registered user, I want to initiate a Telegram chat directly from a profile, so that we can coordinate without sharing phone numbers.
    - AC: Clicking "Message" opens Telegram directly to a chat with the match’s username. 
- As a registered user, I want to browse and filter potential matches by sport, location, and availability, so I can find partners suited to my preferences.
    - AC:  Potential matches sorted by compatibility score, from highest to lowest.
        
## Weekly commitments

### TA's last week feedback summary 
- Although the project is dockerized, for some reason it only runs on Linux -> we need to ensure cross-platform compatibility (Windows/macOS support).
- It is recommended to use Telegram-based authentication (user registration and authorization via Telegram).
- For better user experience, the user feed should be ranked from higher to lower match relevance.

### Individual contribution of each participant

Daria Nikolaeva (iOS-developer):
- Wrote a network layer to access the API.
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/62db91d189e5c7fd3434db316365b2b73e87fc55
- Developed navigation in the app + app separate components.
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/7b3332bcc42d39f1ba369ecd9456e79c5e637305

Maria Ilyina (backend-developer):

- Created description of fields for the user profile database and a system of likes between users.
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/40c432405797d8e480622c456669a44dd74cfe73
- Implemented authorization via Telegram.
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/de713c715f92d4e08e1b29bae7d579100e8e45ef#diff-8666bda38be0e15c63494832743beb67b6cdb0b96cb3a4d29ff13d1a958d7015

Ivan Lobazov (backend-developer):
- Wrote API specification.
Link to Postman: https://www.postman.com/joint-operations-geoscientist-81913565/solar-wind/overview
- Fixed Docker.
Closed GitHub issue with a comment: https://github.com/IU-Capstone-Project-2025/Solar-Wind/issues/17
- Improved project structure.
Gitub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/7d1567fba433f3483656a16a0f1aace6fde1971f

Amir Aminov (designer):
- Finished registration userflow schema.
Figma page: https://www.figma.com/design/si98563MfBSXuDtOfV8655/FitFlame?node-id=27-388&t=bBKoTEIvw5Kbwg4h-0
- Developed design of main page (user feed).
Figma page: https://www.figma.com/design/si98563MfBSXuDtOfV8655/FitFlame?node-id=129-1161&p=f&t=bBKoTEIvw5Kbwg4h-0

Polina Kuzminykh (project manager):
 
 - Scheduled weekly team meeting. 
 ![Weekly meeting](https://github.com/IU-Capstone-Project-2025/Solar-Wind/blob/main/content/images/week2_meeting.png)

 - Wrote weekly report including extended user stories with acceptance criteria and summary of TA's feedback from last week.
 - Updated project backlog.
    Kanban board: https://github.com/orgs/IU-Capstone-Project-2025/projects/3/views/1

### Plan for next week
Main goal for next week is to develop an MVP. Based on it, our tasks are:

**Frontend**
- Finish registration routing.
- Implement structure and layout of the main page (user feed).

**Backend**
- Develop profile microservice.
- Develop deck-shuffler microservice.
- Establish communication between the profile microservice and deck-shuffler microservice.
- Deploy backend to server.

**Design**
- Design userflow schemas of profile changes and viewing other users' profiles.
- Design the logic of mutual likes and exchange of contacts.

### Confirmation of the code's operability

We confirm that the code in the main branch:
-  In working condition.
-  Run via docker-compose.