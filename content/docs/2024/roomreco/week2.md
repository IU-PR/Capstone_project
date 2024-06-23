# Choosing the Tech Stack, Designing the Architecture

## Tech Stack Selection

We choose python as backend language and react as frontend language because
corresponding team members are the most experienced in these languages. We
choose MongoDB as document database and Redis as key-value database because they
are the most popular and widely used databases in the industry. Also, document
based approach of mongodb would be more helpful in changes-intensive
development. We also choose RabbitMQ as message broker because it is a popular
and reliable messaging system that can handle high volumes of messages. Finally,
we choose Milvus as vector database because it is a high-performance vector
database that can handle large-scale vector data. Traefik and Caddy are used for
load balancing and reverse proxying, respectively, they are selected as better
alternatives to Nginx.

### Backend

- [Python 3.12](https://www.python.org/)
- [Aiohttp](https://docs.aiohttp.org/en/stable/)
- [GraphQL](https://graphql.org/)
- [Strawberry](https://strawberry.rocks/)
- [Aiogram](https://aiogram.dev/)
- [Beanie + Motor](https://beanie-odm.dev/)
- [RabbitMQ](https://www.rabbitmq.com/)

### Frontend

- [React](https://reactjs.org/)
- [Next.js](https://nextjs.org/)
- [HeadlessUI](https://headlessui.dev/)

### ML Workers

- [RabbitMQ](https://www.rabbitmq.com/)
- [PyTorch](https://pytorch.org/)
- [SurpiseFramework](https://github.com/HazyResearch/Surprise)
- [LightFM](https://github.com/lyst/lightfm)
- [NetworkX](https://networkx.org/)
- [Sklearn](https://scikit-learn.org/stable/)
- [Linear Optimization PuLP](https://coin-or.github.io/pulp/)
- Genetic Algorithm, Tabu Search, SWO, SA, etc

### Infrastructure

- [Redis](https://redis.io/)
- [MongoDB](https://www.mongodb.com/)
- [Milvus](https://milvus.io/)
- [RabbitMQ](https://www.rabbitmq.com/)
- [Docker](https://www.docker.com/)
- [Github Actions](https://github.com/features/actions)
- [Traefik](https://traefik.io/)/[Caddy](https://caddyserver.com/)

## Architecture Design

![Schematic drawing](/2024/roomreco/week-2-schema.svg)

<details><summary>Component Breakdown</summary>

Our system consists of four main components:

1. **The administrator's web application**

   The task of the web application is to provide the administrator with a
   user-friendly interface for managing forms, room stock, and the room
   allocation process.

2. **The user's Telegram application**

   The task of the telegram application is to provide the user with a convenient
   and quickly accessible interface for filling out forms and interaction with
   the recommendation system.

3. **Central server for processing requests and storing data**

   The task of the central server is to provide an API for interacting with user
   data, establish a channel for secure client interaction with ML workers, as
   well as provide information about statistics and user profiles. The central
   server will contain all the business logic, including processing requests,
   responses, errors, and data consistency.

4. **Dynamic ML workers for processing requests and issuing responses**

   The task of ML workers is to provide an isolated environment for performing
   ML tasks, such as a recommendation system and the room allocation of users.
   Replicas of ML workers will be spawned on the server, horizontally
   distributing load between several workers.

Other infrastructure components that we are going to use include:

- Vector database (milvus) (datalake)
- Document database (mongodb)
- Cache (redis)
- Message broker (rabbitmq)
- Server administration (caddy/traefik/docker/gunicorn etc)

</details>

<details><summary>Data Management</summary>

We plan to store data in different databases based on their nature and usage:

- Users' profile data, room stock, and room allocation data would be stored in a
  document database (MongoDB) and would be accessible through an API.
- Users' unfinished forms, states, and additional telegram-related data would be
  stored in a key-value database (Redis). Some server caches also would be
  stored there.
- Users' embedded (vectorized) profiles and recommendation system feedbacks
  (like/dont like) would be stored in a datalake (vector db - Milvus).

Futhermore, we have established access control policies to ensure data security:

- Client applications has no access to data in databases (only conroled access
  through APIs).
- API Server has full read/write access to document database and key-value
  database.
- ML workers have full read/write access to datalake.

</details>

<details><summary>User Interface (UI) Design</summary>

We plan to design user interfaces that are intuitive and user-friendly. The
administrator's web application will have a clean and organized layout with
features such as form management, room stock management, and room allocation
process. The user's Telegram application will have a simple and interactive
interface for filling out forms and receiving recommendations. We will conduct
usability testing to gather feedback and improve the user experience design
based on user preferences.

</details>

<details><summary>Integration and APIs</summary>

We do not plan to integrate with any third-party services or APIs. All solutions
will be self-hosted or implemented as part of the project. However, we might
ingerate with some cloud servuces in the future in order to reduce operational
costs.

</details>

<details><summary>Scalability and Performance</summary>

We plan to utilize horinzontal scaling to handle a large number of users and
requests. We would configure cloud infrastructure providers to automatically
spawn service replicas when needed. Several replicas of main server would be
spawned behind a load balancer to achive high availability and fault tolerance.
Message brokers would be used to decouple ML workers and ensure task persistence
and completion. ML workers are also replicated horizontally to improve
performance and scalability. In the future, we might add more sophisticated load
balancing and caching mechanisms to further improve performance and scalability.

</details>

<details><summary>Security and Privacy</summary>

We plan to implement various security measures to protect user data and prevent
unauthorized access. All traffic between the server and clients will be
encrypted using TLS/SSL. Authentication mechanisms such as OAuth2 and JWT will
be used to ensure secure access to user data from web applications. Secret codes
and telegram api bot proxies would be used to protect user data for telegram
applications. ML workers and server would be protected by firewalls and
encapsulated in closed local networks.

</details>

<details><summary>Error Handling and Resilience</summary>

We aim to implement robust error handling on a side of API server, as well as
comprehensive logging and data tracing mechanisms. Persistent message queues
would be used to ensure reliable message delivery and task completion by ML
workers.

</details>

<details><summary>Deployment and DevOps</summary>

To automate the deployment and management of the system, we plan to use
containerization technologies (docker stack: dockerfiles, docker,
docker-compose) and CI/CD pipelines (Github Actions) for testing, building, and
deploying components of the system independently.

</details>

## Week 2 questionnaire

<details><summary>Tech Stack Resources</summary>

No, we don't have any resources for the tech stack we have chosen. We have
chosen the tech stack based on the expertise of the team members and the
requirements of the project.

</details>

<details><summary>Mentorship Support</summary>

As a team, we are not currently partnered with a mentor specifically for our
project, primarily due to the difficulty in sourcing someone with expertise in
the specialized field of graph algorithms. We recognize the immense value that
mentorship brings to the table, especially in navigating the complexities of our
project.

</details>

<details><summary>Exploring Alternative Resources</summary>

In order to distribute students into rooms, it is necessary to work either with
classical clustering or with the so-called community detection / graph
clustering. According to the first one, classical clustering methods such as K
means, Dbscan, etc.
[were reviewed](https://link.springer.com/article/10.1007/S40745-015-0040-1).
For graph clustering, it was useful to familiarize yourself with the contents of
[this video](https://www.youtube.com/watch?v=CDMQR422LGM). SOTA solutions was
also viewed at this
[link](https://paperswithcode.com/paper/rethinking-graph-autoencoder-models-for).
It was found out that graph autoencoders are the best available solutions. There
are also simpler classical algorithms in the
[NetworkX library](https://networkx.org/documentation/stable/reference/algorithms/community.html)
that can also be used to speed up the program.

</details>

<details><summary>Identifying Knowledge Gaps</summary>

No one in the ML team has had any experience in the domain of recommendational
systems. For this reason, the main goal of the week 1 and half of week 2 for us
was to do a very thorough and meaningful research of the topic and to propose a
list of different techniques, models, and libraries that we will compare and
experiment with. This way we well ensure a well-rounded understanding of the
stack by both researching it, and experimenting with different solutions of the
task at hand.

</details>

<details><summary>Engaging with the Tech Community</summary>

We did not engage with the broader IT community, apart from reading several
personal blogs on the related topics and publications on platforms such as
Medium and Habr. We have also asked for an advice from a TA from our previous
corses, before the TA distribution on the Capstone course.

</details>

<details><summary>Learning Objectives</summary>

After researching potential solutions for recommendation and distribution
systems during week 1, this week we aim to put all this research into practice.
We have picked several promising technologies to try and use with our own data.
This will allow us to understand our field and data even further, as well as
create some testing pipelines for the future iterations.

</details>

<details><summary>Sharing Knowledge with Peers</summary>

Every week we have separate meetings for the whole team, for the ML team, and
for the dev team. The first one is for planning the general trajectory of the
week and sharing important findings. The second one is inclusively to share
knowledge and progress on the ML part. Usually, before the meeting, each person
creates a document with their findings. We read those documents before or during
the meeting, discuss them, and therefore share and explain the knowledge. A
similar procedure is used in a dev team.

</details>

<details><summary>Leveraging AI</summary>

We did use ChatGPT as a supplement for our research. For example, to see an
overview of the field or its subfields, or to verify domain-specific
terminology. It was also useful to generate code examples for the libraries
where the documentation was too complex or lacking.

</details>

## Tech Stack and Team Allocation

Once we have a clear understanding of the project requirements and architecture,
we can assign responsibilities to team members based on their expertise and
interests. This will help us streamline the development process and ensure that
each component is handled effectively.

| Member Name            | Track                            | Responsibilities                                        |
| ---------------------- | -------------------------------- | ------------------------------------------------------- |
| Egor Machnev           | `Product management`, `Frontend` | Overseeing product development, frontend coding         |
| Anton Kudryavtsev      | `Backend`                        | Developing and maintaining backend systems, devops      |
| Sofia Tkachenko        | `Machine learning`               | Designing and implementing ML models                    |
| Apollinaria Chernikova | `Machine learning`               | Data preprocessing, ML model evaluation                 |
| David Khachikov        | `Machine learning`               | Research and development of ML algorithms               |
| Sergey Katkov          | `UI/UX`, `Testing`               | Designing user interfaces, conducting usability testing |

## Weekly Progress Report

This week, our team concentrated on developing the architecture of the room
recommendation system. We divided components, outlined data management
strategies, and designed the user interface. In addition, we discussed
scalability, security, and error handling to ensure system reliability.

### Challenges & Solutions

a. **Challenge**: The integration of machine learning models with the backend
system is a key objective.

**Solution**: After careful consideration, we have opted to utilise RabbitMQ as
the communication bridge between the backend and ML components. This will
facilitate seamless integration and communication between the two.

b. **Challenge**: It is our responsibility to ensure the privacy and security of
our clients' data.

**Solution**: We have implemented encryption algorithms to protect user data and
established strict access controls to prevent unauthorized access.

c. **Challenge**: Designing a user interface that is intuitive to use..

**Solution**: We conducted user testing to gather feedback and improve the user
interface and user experience design based on user preferences.

### Conclusions & Next Steps

The team has made significant progress in defining the system architecture and
allocating responsibilities. Next week, we plan to start developing the backend
and frontend components, focusing on implementing the machine learning models
and designing the user interface.
