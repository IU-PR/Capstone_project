# Detailed Requirements Elaboration 
This week, the primary objective is to implement the core functionality for both backend and frontend of the application. 

### Backend Tasks:
* Develop full CRUD functionality for the following entities: bookings, books, libraries, and users.

* Implement all necessary API endpoints for the above CRUD operations.

* Set up user authorization and registration.

* Establish a working database, and encapsulate it using Docker containers for consistent deployment.

* Integrate CI/CD pipelines to enable automated deployment on each push to the main branch.

* Configure a temporary domain to test deployed versions of the application.

### Frontend Tasks:
* Begin layout of the Main Page, initially without styling.

* Start building the Book Page and the Account Page, including navigation between them.

* Implement user authorization and registration pages with completed styling and functionality.

### Prioritized backlog 
* https://raw.githubusercontent.com/IU-Capstone-Project-2025/libnet/59f0b98faee5ead448693cbe40dd9480398a3c4c/reports/photo_2025-06-18_22-13-24%20(6).jpg
* https://raw.githubusercontent.com/IU-Capstone-Project-2025/libnet/59f0b98faee5ead448693cbe40dd9480398a3c4c/reports/photo_2025-06-18_22-13-24.jpg
## Project specific progress 

### Frontend
We have successfully completed all the planned tasks for this week.

### Backend

We have successfully completed all the planned tasks for this week.

#### Link to API endpoints documentation.
* http://83.222.18.122:8000/docs

### Design
#### User Flow Diagrams
We've developed 4 comprehensive user flow diagrams to visualize our system's navigation:

 **Auth Selection Flow**  
   Demonstrates the initial account type selection between:
   - Administrator
   - Library Manager
   - User (Reader)

https://raw.githubusercontent.com/IU-Capstone-Project-2025/libnet/59f0b98faee5ead448693cbe40dd9480398a3c4c/reports/photo_2025-06-18_22-13-24%20(5).jpg

**Administrator**
* https://raw.githubusercontent.com/IU-Capstone-Project-2025/libnet/59f0b98faee5ead448693cbe40dd9480398a3c4c/reports/photo_2025-06-18_22-13-24%20(4).jpg

**Manager**
* https://raw.githubusercontent.com/IU-Capstone-Project-2025/libnet/59f0b98faee5ead448693cbe40dd9480398a3c4c/reports/photo_2025-06-18_22-13-24%20(2).jpg

**User** 
* https://raw.githubusercontent.com/IU-Capstone-Project-2025/libnet/59f0b98faee5ead448693cbe40dd9480398a3c4c/reports/photo_2025-06-18_22-13-24%20(3).jpg
#### Wireframes
The initial wireframes were refined into the final design.

Here is the link in Figma: https://www.figma.com/design/PEK6pAX4gh7f5oO9C0jNfq/libnet?node-id=0-1&t=sEVJZ4Fg0AY8jxIw-1


## Weekly commitments
### Individual contribution of each participant
| Team Member     | Completed Work                                                                                                                                                                                      |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ivan Murzin     | Set up CI/CD, Connected a temporary domain, Purchased and configured a server, Implemented frontend work (styling components/pages).                                                                |
| Aliya Sagdieva  | Wrote the project report, Created a README.md, Designed a user flow diagram.                                                                                                                        |
| Alena Averina   | Wrote CRUD for bookings and libraries, Containerized database, Composed .dockerignore, Maintained Docker: edited Dockerfiles and docker-compose.yml.                                                |
| Anna Serova     | Implemented the following frontend: skeleton for all user pages, loading books on the main screen, login, registration, user account in process: data update, account logout.                                                                                                                                                                                                    |
| Artem Ostapenko | Deployed the database on the server, Made crud for users and books, Made registration and login for three types of users, Made loading of the library catalog, Made joining/removing managers. <br/> |

### Plan for Next Week 

#### Backend Focus
- Implement full authorization system for all user types (Admin, Manager, User)
- Develop manager administration panel with:
- Build library editing features
- Create book status management system

#### Frontend Focus
- Develop corresponding UI pages for:
  - Manager administration panel
  - Library information editing
  - Book status management
  - User authorization flows

## Confirmation of the code’s operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the README.md). 
