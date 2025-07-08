# Week #4

**Project name**: *Solar Wind* 
**Code repository**: https://github.com/IU-Capstone-Project-2025/Solar-Wind

| Team Member                             | Telegram Alias   | Email Address   | Team Role                                          |
|-----------------------------------------|------------------|-----------------|---------------------------------------------|
| Daria Nikolaeva  (Team Leader)     | @aalikorn | da.nikolaeva@innopolis.university | iOS-developer | 
| Maria Ilyina         | @abu_blood | m.ilyina@innopolis.university | backend-developer | 
| Amir Aminov            | @amirhan322 | a.aminov@innopolis.university | designer | 
| Polina Kuzminykh            | @sarrtr | p.kuzminykh@innopolis.university | project manager | 
| Ivan Lobazov            | @XriXis | i.lobazov@innopolis.university | backend-developer |

## Testing and QA

**Frontend**
The developed tests for the frontend allow to:

- Verify that categories and cities are successfully loaded from the worker and presented to the view.
- Check that toggling selection for categories and cities correctly updates the selected lists by adding or removing items.
- Confirm that selected category and city IDs are properly saved and retrieved from UserDefaults.
- Ensure the presenter correctly updates and notifies the view with the latest data for categories and cities.
- Validate that data loading, toggling functions, and data source snapshot applications execute without errors and complete successfully.

 ![Frontend tests](https://github.com/IU-Capstone-Project-2025/Solar-Wind/blob/main/content/images/frontend_tests.jpg?raw=true)

**Backend**
The developed tests for the backend test 3 different microservices:

*Profile Microservice:*
The tests for controllers check the correct operation of REST controllers: creating, receiving, deleting users, as well as getting lists of sports and cities. They use mock services to isolate business logic and verify the correctness of HTTP responses and JSON content. In this way, the tests ensure that the controllers correctly process requests and return the expected data.

The tests for services check the business logic of the services: correct pagination when getting lists of cities and sports, as well as creating and deleting users. They use mock repositories and mappers to isolate the service layer and verify that the methods return the correct data and trigger the necessary operations. In this way, the tests ensure that the services work correctly with the data and interact with the repositories.

![Bakend test1](https://github.com/IU-Capstone-Project-2025/Solar-Wind/blob/main/content/images/backend_test1.jpg?raw=true)

*DeckShuffle Microservice:*
The test verifies the method of creating a profile deck in the DeckCreationServiceImp service. It makes sure that when requesting a user by ID, the mappers and repository are correctly called to get suitable users by the specified parameters (gender, preferences, city, age), and that the correct list of DTO profiles is returned. The test also verifies that all the necessary methods are called the right number of times and the result contains the expected objects.

![Bakend test3](https://github.com/IU-Capstone-Project-2025/Solar-Wind/blob/main/content/images/backend_test3.jpg?raw=true)

*Likes Microservice:*
The test checks the MatchController controller, which processes a POST request to create a like. It makes sure that when an endpoint is called with the necessary parameters, the saveOrUpdateDecision service method is called exactly once with a correctly formed DTO containing the sender's ID, recipient, and the first like sign. The test also verifies that the controller's response returns the 200 OK status.

![Bakend test2](https://github.com/IU-Capstone-Project-2025/Solar-Wind/blob/main/content/images/backend_test2.jpg?raw=true)

## CI/CD
CI/CD setup includes creation and configuration of described environments. The tools used are Nginx, GitHub Workflows, Ubuntu, Docker Compose. There also was a challenge in the difference of the docker external host name between the systems.

## Deployment
### Staging

Staging environment:
Github Runnner with local db running, which configured on preparation step for running tests. After the tests are comleting - server is no more accessed, but it is enought for the automatic testings.

### Production

Remote server has SHH connection, it is located in Netherlands and has minimal hadrdware setup: 1 core, 2Gb. Additionally solar-wind-gymbro.ru domain name was bought and assosiated with the server. Because of microservices architecture on one-server setup, ports are used for differentiating between services.

This setup is configured only as first step variant and could be changed in the future to use kubernates with ingresses and multiple servers.

How to run:
Clone the repository, locally build it, and run.

## Vibe Check

At first, it was difficult to cooperate because we didn't know each other before, but after we got to know each other better, teamwork began to improve.  We agreed that we have no complaints about each other and communication is going well. Also, to be more productive, we decided that we need another meeting at the end of the week to summarize the results that were done during the week and make the report more detailed.

## Weekly commitments

### TA's last week feedback summary 
- It is recommended to either further improve the functionality of the application, or add llm for a personalized selection of users in the feed.
- Now we need to focus on developing a user profile and user matching.

### Individual contribution of each participant

Daria Nikolaeva (iOS-developer):

- Implemented layout of user profile.
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/pull/51/commits/5734dc00b50f5a1422c02270c1eb686fb272927e
- Finished the logic of sending network requests.
- Fixed bugs in registration.
- Wrote unit tests for frontend.
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/pull/51/commits/5559765015b1cb4dcab15c87d6cf02e67d3332e5

Maria Ilyina (backend-developer):

- Wrote unit and integration tests for microservices (controllers, services, repositories).
GitHub commit: https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/004535964cf841380bb6321f3cfae22ff54e67b3
- Adjusted endpoints to reduce the data sent to the frontend.
GitHub commit:https://github.com/IU-Capstone-Project-2025/Solar-Wind/commit/b6638ad768dedc8e9af61a6982136f807bb8c3a4

Ivan Lobazov (backend-developer):

- Set up CI/CD pipeline.
Closed GitHub issue: https://github.com/IU-Capstone-Project-2025/Solar-Wind/issues/46
- Set up staging environment and described it.
Closed GitHub issue: https://github.com/IU-Capstone-Project-2025/Solar-Wind/issues/49

Amir Aminov (designer):

- Updated the registration flow with pages for filling age and selecting user gender and desired gender.
Figma page: https://www.figma.com/design/si98563MfBSXuDtOfV8655/FitFlame?node-id=123-193&t=9DpALhOCU5l3kdqH-0
- Added logic for changing profile information.
Figma page: https://www.figma.com/design/si98563MfBSXuDtOfV8655/FitFlame?node-id=129-1161&p=f&t=VYT0bMOH2YglxDOk-0

Polina Kuzminykh (project manager):
 
 - Scheduled weekly team meeting. 
 ![Weekly meeting](https://github.com/IU-Capstone-Project-2025/Solar-Wind/blob/main/content/images/week4_meeting.png?raw=true)
 - Wrote weekly report including summary of TA's feedback from last week.
 - Conducted the team health check.
 - Updated project backlog.
    Kanban board: https://github.com/orgs/IU-Capstone-Project-2025/projects/3/views/1

### Plan for next week

**Frontend**
- Make a small  refactoring.
- Continue fix bugs in frontend.
- Create a screen of the current user's page with the ability to edit info.
- Implement logic of user likes.

**Backend**
- Continue adjusting security services on user-server communication and on service-service communication.
- Develop tests for new features.
- Optimize the deck service and user selection options.

**Design**
- Update pages of other people's and your profiles with the addition of new parameters of age and gender.
- Create user search logic.

### Confirmation of the code's operability

We confirm that the code in the main branch:
-  In working condition.
-  Run via docker-compose.