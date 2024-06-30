# Developing the first prototype, creating the priority list

## Priority lists

### Technical Infrastructure & DevOps

The project is designed such way, so that it could run from very low-level
machines to very high-level infrastructure. At bare minimum, the project require
free-tier VM with 10% 2vCPU and 4GB RAM (already done). In this configuration,
all the services are deployed on the same machine and use inner docker network
for communication.

The technical infrastructure cloud be scaled up to:

- Designated MongoDB cluster with several nodes
- Designated High-Speed RAM VM for caching mechanisms (using Redis)
- Several dedicated VMs for the API service (with scalability on demand)
- Efficient DNS/Proxy Load Balancer server
- Several dedicated VMs for the frontend server (with scalability on demand)
- CDN for the static content
- Dedicated GPU servers for the ML models
- VM with high memory capacity for RabbitMQ
- Infrastructure controllers and master nodes for architecture and deployment
  management

Priority list for the infrastructure is the following (sorted by business Return
On Investment (ROI) value):

1. GPU servers for the ML models
2. Single powerful VM for the API service
3. MongoDB cluster
4. Several VMs for the frontend server
5. Several VMs for the backend server
6. Load Balancer
7. DNS/CDN/Proxy servers
8. Dedicated RabbitMQ server
9. High-Speed RAM VM for caching mechanisms

Infrastructure progress is the following:

- [x] Traefik proxy with TLS certificates
- [x] Container registry & container app deployment
- [x] Portainer for container management
- [x] RabbitMQ server
- [x] MongoDB cluster
- [x] Traefik load balancer
- [ ] API service
- [ ] Frontend service
- [ ] ML workers service
- [ ] Redis cache

### Backend Development

Backend development is one of the most important parts of the project, since all
business logic is implemented here. Backend development task include:

- Business logic
- GraphQL API service
- Webhook service for telegram
- Storage and data management using MongoDB
- ML workers implementation
- Managing the deployment of the project

Priority list for the backend development is the following (sorted by business
Return On Investment (ROI) value):

1. ML workers implementation
2. Storage and data management using MongoDB
3. Business logic
4. GraphQL API service
5. Webhook service for telegram
6. ML workers requests
7. Managing the deployment of the project

There are a lot of dependencies between the backend task, so that they should be
done in the specific order. Current progress is the following:

- [x] Domain entities defined
- [x] GraphQL API designed
- [x] Storage and data management objects defined
- [x] Storage services implemented
- [ ] Business logic implemented
- [ ] GraphQL API services implemented
- [ ] Authorization implemented
- [ ] Webhook service implemented
- [ ] ML workers implemented

### Design, Business Value & Frontend Development

Frontend development is strongly related to the backend development, since it
devpends on the API service. Frontend development task include:

- Choose the theme, fonts, colors
- Project business value definition
- Designe the UI and prototyping elements
- Authorization implementation
- Recommendation infinity scrollable feed implementation
- Admin panel implementation

Priority list for the frontend development is the following (sorted by business
Return On Investment (ROI) value):

1. Project business value definition
2. Choosing the theme, fonts, colors.
3. Desing the UI and prototyping elements
4. Authorization implementation
5. Recommendation infinity scrollable feed implementation
6. Admin panel implementation

Current progress is the following:

- [x] Project business value definition
- [x] Choosing the theme, fonts, colors.
- [x] Desing the UI and prototyping elements
- [ ] Authorization implementation
- [ ] Recommendation infinity scrollable feed implementation
- [ ] Admin panel implementation

### Data Management

Data management is one of the most important aspects of this project. To ensure
project scalability and rapid development, the data management is implemented
using MongoDB. For caching mechanism on several stages, such as Telegram Bot
State storage, DataLoaders caching, request caching, etc., Redis is used. For
the ML models, vectorized data is stored in Milvus.

Priority list for the data management is the following (sorted by business
Return On Investment (ROI) value):

1. MongoDB cluster
2. ML models storage using Milvus
3. Caching mechanism using Redis

Current progress is the following:

- [x] MongoDB document schema
- [ ] ML models storage using Milvus
- [ ] Caching mechanism using Redis

## Prototype Testing

Developement is done by several independent teams, so that the different project
parts can be tested by different people on stage of unit and ingration testing.
During futher project development, also system and acceptance testing would be
done.

[Go to prototype](https://github.com/randorm/research/blob/main/experiments/recommendation_algorithm/recommendation_system.py)

Unit & ingration testing plans:

- Backend unit testing (bussiness logic, storage packages, etc)
- Backend ingration testing (API responses, data storage, telegram responses,
  etc)
- Frontend unit testing (components, pages, api requests, etc)
- Frontend ingration testing (authorization, feed, etc)
- ML workers unit testing (recommendation systems, room allocation, etc)
- ML workers ingration testing (receive and submit message from rabbitmq, fetch
  data from milvus, etc)

System testing plans:

- Backend - ML workers communication (send and receive messages from rabbitmq,
  fetch data from milvus, spawn workers, correct sync of recommentations and
  user feedback, etc)
- Frontend - Backend communication (responsive UI, low latency, great UX, etc)
- Telegram - Backend communication (flawless communication, state persistence,
  etc)
- Complete system testing including data flow tracing, security, load testing,
  etc

Acceptance testing would be done later with customers and real users, most
probably out of the capstone course scope.

## Progress report

Our accomplishments this week include successfully prototyping the
recommendation model, testing the model through the CLI, and making significant
progress on the GraphQL API. We continue to work on improving the algorithms and
API, and are preparing to begin a new phase of the project - the development of
an algorithm for assigning students to rooms.

<details><summary>Prototype Features</summary>

This week, we focused on implementing the recommendation algorithm whose
hypotheses we created and tested in Weeks 1 and 2. Key features and capabilities
that were successfully implemented in our prototype include:

- **Hybrid neighbor selection**: Students who are close to the user's interests
  are recommended first, then students who are close to the subscribers'
  interests are recommended.
- **Issuing recommendations**: The prototype can issue up to 10 recommendations
  at a time. The modes alternate with each new call.
- **Model testing**: Currently, model testing is done through the CLI
  (terminal).

</details>

<details><summary>User Interface</summary>

Since our current prototype does not include a GUI, this part of the report will
be skipped.

</details>

<details><summary>Challenges and Solutions</summary>

**Challenge A**: Faced the need to allocate more time to develop GraphQL API to
interact with the distributed recommendation model deployment system. This was
due to the complexity of integrating different components of the system.

**Solution**: Reorganized tasks and reallocated team time to focus on the core
elements of the API. Development is on track, but with some adjustments to the

timeline.

</details>

<details><summary>Next Steps</summary>

Next week, our team plans to:

- Optimizing and improving the accuracy of the recommendation algorithm based on
  the data and feedback received.
- Continued work on the GraphQL API, including implementing additional features
  and testing of the API.
- Defining basic criteria and creating a basic model for allocation of students
  to rooms.

</details>

We are grateful for the feedback and are committed to improving our reports and
results in line with the recommendations received.
