# **Bookinng**
> _— desirable room booking service for Innopolis University_

# **Week 1**

> Team formation and project proposal

## **Team Members**

| **Member**                 | **Telegram**                                  | **E-mail**                           |
|----------------------------|-----------------------------------------------|--------------------------------------|
| Vladislav Deryabkin (Lead) | [evermake](https://t.me/evermake)             | v.deryabkin@innopolis.university     |
| Yaroslav Kivaev            | [catdog905](https://t.me/catdog905)           | k.yaroslav@innopolis.university      |
| Ekaterina Koshmanova       | [k_koshmann](https://t.me/k_koshmann)         | e.koshmanova@innopolis.university    |
| Vadim Zbarashchenko        | [metafates](https://t.me/metafates)           | v.zbarashchenko@innopolis.university |
| Ruslan Bakirov             | [monyter](https://t.me/monyter)               | r.bakirov@innopolis.university       |
| Anton Skorkin              | [PozhiloyProger](https://t.me/PozhiloyProger) | a.skorkin@innopolis.university       |

## **Value Proposition**

### The Problem

Innopolis University offers students and employees the opportunity to book rooms
for personal use through the
[my.university.innopolis.ru](http://my.university.innopolis.ru/) website. While
this service is appreciated, there are several issues with the current process
of rooms booking that need to be addressed.

Currently, users must select a specific room and check its calendar for
availability. If a time slot is free, they can book the room by creating an
event in the calendar. This system is convenient if the user knows exactly which
room they want to book or if most rooms are available. However, when students
need a free room for a specific time slot they must check the schedule of every
room which can be time-consuming and frustrating.

Another related problem that we observe is that students and employees often
struggle to physically locate specific rooms, auditoriums, and offices in the
university building.

To justify the problems and make sure we are not the only one who have troubles,
we conducted a survey with 26 participants (excluding those who do not book
rooms and our team members). The results showed that:

1. Students in general actively use the rooms booking service.
2. More than a half of participants spend more than 5 minutes on average to
   choose and book a room.
3. Participants are generally dissatisfied with the usability of the current
   system. Furthermore, none of the participants rated the system's convenience
   as a five out of five.
4. Two-thirds of the participants would very much like to be able to see rooms
   available at a selected time interval, while a quarter found it to be a good
   idea. Almost the same for the ability to see available time slots for a
   specific room.
5. Over half of participants would appreciate a visual view of the room layout
   while booking.

![piechart_how-often-do-u-book-rooms.png](/bookinng/piechart_how-often-do-u-book-rooms.png)

You can find the complete survey results in the
[attached PDF file](/bookinng/Rooms-Booking-Survey-Report.pdf).


### Solution

Both of the problems listed above can be solved by a service that provide a
convenient interface for choosing an available room in the university and a map
of each floor. User can check available rooms for a specific time, entering
period of time and see free rooms at this time on the graphical map (where free
and booked rooms will look differently helping a user to find an appropriate
room). Grouping all free room entering specific time helps to quickly find a
room within a specific time period. Also this service helps to get the position
of rooms in Innopolis University building having its name/number.


### Benefits To Users

Time saving is the most valuable outcome for users from our service. We expect
these things to happen after we finish the project:

- Users will not have to scramble through the rooms to find a free one for the
  desired time slot;
- Users will find a free time slot for the selected room faster as this will
  be done in a more convenient way;
- Users will not run around a minute before the meeting to look for a room, as
  they will see the room locations on the map at the time of booking;
- An overall user experience will be improved by making the process of the
  events planning more pleasant.


### Uniqueness

The proposed (tentative) system is better than the existing Microsoft Outlook
solution of room booking in different aspects:

1. It provides extra functionality for finding an available room;
2. It will show a visual representation of rooms location to help users find
   rooms;
3. It will have a mobile-friendly interface to simplify the booking process
   using a phone, which is usually most often at the fingertips of people.

One of our optional goals is to make the process of adding new building map
easily, that can make this project useful for others companies and took it to
commercial level.


### User Impact

We believe that successful solution will not only improve users experience and
their productivity but also will highly affect on the university’s ecosystem
level. Such unique solutions make ecosystem more innovative and underline the
IT technologies in our university. 


### User Testimonials or Use Cases

Use case of a building map — many shopping malls provides a digital map of the
building with description and navigation to specific shops that helps customers
locate different facilities. But these solutions usually implemented using
stationary displays. Another drawback of existing solutions is that they are
not globalized.


## **Lean Startup Questionnaire**

**1. What problem or need does your software project address?**

> The primary problem our project addresses is the inconvenience of the rooms
> booking process in Innopolis University.

**2. Who are your target users or customers?**

> Our target users are the university students and employees who take advantage
> of the rooms booking service.

**3. How will you validate and test your assumptions about the project?**

> We will give an opportunity to the users to try our MVP version’s and test
> our assumptions by measuring the performance and considering overall feedback.
> After that we will analyze the results and make decisions abou the testes
> assumptions.

**4. What metrics will you use to measure the success of your project?**

> We are going to make another survey similar to the mentioned above and make
> sure that performance has improved, users are happy with the interface and
> spend a minimum of time searching and booking rooms. We will collect the
> following metrics to evaluate our success:
> - Amount of reduction of the average booking time of a room;
> - Positive feedback from users — how much are they satisfied with the
>   interface and performance of our system.

**5. How do you plan to iterate and pivot if necessary based on user feedback?**

> We will see the main complaining points, ask for ideas from users and
> generate new solutions for these tasks. After that we will try to implement
> the best ones and once again give it for testing to users.

## **Leveraging AI, Open-Source, and Experts**

### Artificial Intelligence

Our team plans to use LLM code generation (GitHub Copilot) to make the process
of development faster, especially working with Outlook Calendar API, that is,
AI will help us find relevant API endpoints and their response schemas quicker,
than browsing documentation ourselves.

We are also considering incorporating AI-powered features  in our system that
will require use of AI, such as suggesting the best place and time for a meeting
based on a user's preferences and predicting room occupancy at different times
to help users make better decisions when booking a room.

### Open-Source

First of all, we are going to use open-source libraries and frameworks during
development. Particularly, for frontend part we are going to use either Vue.js
or React.js framework; for backend we will use one of the most popular
frameworks (Django or FastAPI for Python, Spring for Java), but it depends on
the programming language and stack we will agree on.

Secondly, we will also open-source all our code, which is not intended to be
private and may be useful for others.

### Experts in Relevant Domains

We have reached out to the individual involved with Innopolis current room
booking system. They have given their approval for our proposal and will be
available to assist us whenever any issues arise.

## **Inviting Other Students**
We found out that there is a group of first year students who are working on a
Software Project to create a Telegram bot for rooms booking. We have contacted
them and plan to discuss combining our projects to add a Telegram bot to the
system. If we will agree to work together, we can get the project done faster
and better.

## **Vision Of The Project**

### Overview

We want to create a service for convenient booking rooms. A lot of people have
difficulties with finding rooms, checking accessibility of a rooms and finally
booking them. Our project will try to solve these problems.

### Schematic Drawings

We do not have a clear understanding of which components will we have in our
system and how will they communicate, but we can share our our current view of
what the system’s core components may look like on the diagram:

![components-diagram.png](/bookinng/components-diagram.png)

There are two core parts:

- Backend — responsible for handling booking requests and managing database
  operations.
- Web-interface — user-facing aspect of the project, what the user will see and
  interact with.

Additionally, we are considering incorporating a Telegram Bot as an optional
feature, but we have not yet decided whether to implement it or to ask for help
from first-year students for its development.

### Tech Stack

We have not yet decided about our stack, but we have some ideas. For frontend
part we are going to use either Vue.js or React.js framework; for backend we
will use one of the most popular frameworks (Django or FastAPI for Python,
Spring for Java).

It is very likely that we will use some kind of data storage. We plan to use
Postgres as a  DBMS and/or Redis for caching.

### Anticipating Future Problems

We see 2 primary problems we can face in the future:

1. **Obtaining the map of the university and making the interactive digital copy
   of it.** If this task turns out to be too complicated and time-consuming, we
   plan to implement it in a simpler way, such as using static photos to help
   people locate the rooms.
2. **Finding a way to integrate our system into the life of the university, as
   this will most likely require working with the Microsoft Outlook API.** To
   solve this problem we are going to consult with people in university who are
   responsible for My University portal or can give us advice.

### Elaborate Explanations

For now we do not have a clear vision of components that make up our system and
their relations. But the core parts we are going to implement are the following:

- Backend that utilizes currently used Outlook API to provide a better interface
  for rooms booking;
- Mobile-friendly interface with focus on usability and simplicity;
- Digital map or other way to help users find rooms location.

{{< hint danger >}}
**Feedback**  

**Value Proposition**
Very nice details and approach. Although we previously had an opportunity to book rooms though calendar in outlooks and it was very convenient. It will check which free rooms available at the desired time. 

Also, the university does have a map to tell which room and where is it. You can contact me to sent it to you.

**Lean startup question**
- Only positive feedback? Why :) negative feedback is important also

**AI** 
I hardly see AI application in your product 

Vision Of The Project 
One very easy way to tell people where is meeting room. Is to tell them they are located next to what rooms? 
Or maybe give description how to reach by description the road to take. 

**Overall**
Very good report! But try to think more about AI utilizing. 
5/5

_Feedback by Moofiy_
{{< /hint >}}

---

# **Week 2**

> Choosing the tech stack, designing the architecture

## **Tech Stack Selection**

After discussing the possibility of incorporating our project into the Innopolis
University's current room booking service with Andrey Markov, who developed the
current active service, we identified two constraints on our backend that would
need to be addressed:

1. We MUST use Microsoft Outlook API to actually book rooms — this enables us to
   integrate our project into the university's life without a need of
   introducing changes to the current infrastructure;
2. We MUST use a well-known programming language with a popular framework — this
   is required so that in the future it will not be difficult to find developers
   who can easily make changes to our code-base.

Following discussions with Andrey and the team, we concluded that Python would
be the ideal programming language for our backend, with FastAPI as our
web-framework. This decision was based on the following factors:

1. Firstly, [Python](https://www.python.org/) — is one of the most popular 
   programming languages;
2. Secondly, [FastAPI](https://fastapi.tiangolo.com/) — is one of the most
   popular web-frameworks for Python and it is actively maintained by the
   open-source community;
3. Finally, [exchangelib](https://github.com/ecederstrand/exchangelib) — is one
   of the few actively maintained libraries for working with Microsoft Outlook
   API (which is crucial in our case) with the good API and documentation, and
   which is written in Python.

We also decided not to implement Telegram Bot ourselves, since we don’t have
enough resources for that, and, moreover, there are already several groups of
first-year students who are already working on it.

Our frontend application will be written in Next.js — powerful and very popular
open-source web framework, which has a great documentation and a large
community. Also, it will not take much effort to start working with it, as our
team members have experience working with React, and Next.js is based on React.
Moreover, Next.js provides an SSR (server-side rendering), which will have a
good impact on the performance and security of our application.

We’re going to setup automated Docker images building process for our backend
and frontend. This will allow us easily deploy them on any VPS, which more
likely will be provided by the university, when we finish the project. But for
now, we are going to deploy frontend on GitHub Pages or other free static-assets
hosting solutions. We also plan to use Kubernetes to orchestrate our Docker
containers to achieve high fault-tolerance.

Speaking of CI/CD we will use GitHub Actions configured with code linters and
test runners to protect the main branch from unexpected bugs and to enforce the
same coding style along all team members. We decided to use GitHub Actions
because it's the most approachable tool for our repositories that are hosted
on GitHub.

To conclude, our tech stack is the following:

1. Backend
    - Python + FastAPI + SQLAlchemy
    - Redis
    - PostgreSQL
    - Docker
2. Frontend
    - TypeScript + Next.js
    - Docker
3. CI/CD — GitHub Actions

## **Architecture Design**

### Component Breakdown

The end user will interact with the frontend part, which will communicate with
our backend.

Frontend part is the **web interface** with **interactive university map**,
which user can utilize in order to locate rooms and choose them for booking.

Backend part implements an **API**, that hides the complexity of Outlook API
and exposes some method for searching and booking rooms. The API will have
identification and authentication via SSO for students.

### Data Management

Basically, Outlook server stores all information about room’s schedules, but we
suffer from lack of methods in Outlook API, so other caching technique on our
side may be applied. For example, presumably, every time when we want to get
all free rooms for specified time period, we have to request schedule of each
room separately. Obviously, that increases latency of the whole operation. To
solve this problem we are going to employ two techniques:

- **Reliability via redundancy**. We are going to query bigger period of time
  that user request in order to avoid duplicate request to Outlook API if user
  will make a small change of time period.
- **Caching**. We will cache all schedules that goes through our API in order
  to reduce amount of redundant requests to Outlook server. Sometimes our API
  will refresh the whole information from Outlook server in order to get room
  booking changes that was made by aside instruments. We are going to use Redis
  as our cache.

We will also need to store some information about user’s (to validate API
tokens, for example), this will be stored in PostgreSQL database and accessed
using SQLAlchemy framework in the code. PostgreSQL is our choice, because it is
an open-source and performant DBMS, and, moreover, most of the team members have
an experience of working with it.

### User Interface (UI) Design

See our [UI design drafts]({{< relref "#ui-design-drafts" >}}).

### Scalability and Performance

Currently the number of supposed clients for our application is not high, but
we definitely consider possibility of scaling. We have three objects of scaling:

- API application
- Redis database
- Outlook server

The first one, API application, we can scale in Kubernetes increasing the number
of pods for the deployment. Obviously, we will need some software load balancer
in order to multiplex the traffic. We will choose it later, when the problem of
scaling come.

Redis database can be scaled using it’s partitioning mechanism.

And the most problematic part of scaling for us is Outlook server. If the
problem appears we will first contact with university IT department to resolve
the problem before planning scaling.

### Security and Privacy

All API requests to our system will be protected with the FastAPI middleware.
Before accessing the system, a user will be required to authenticate in the
Innopolis SSO, which is used in all online-tools that students use every day.
After confirming the user's identity, our backend will generate a JWT token,
which will be send with every request (via header or cookie) from our frontend
app. Therefore, user will be able to log in only if it has a valid token, which
can only be obtained from a database that only the backend will have access to.

### Error Handling and Resilience

We are going to add metrics for each request in API and log all improtant
information in our code and use basic functionality of k8s platform for
restarting the application in case of failure and getting logs from a pods.

### Deployment and DevOps

We utilize GitHub Actions to automate the process of type-checking, linting
code, validating code-style, running tests and building Docker images.

We are going to deploy our backend application to kubernetes cluster, which
solves a huge amount of problems of orchestration.

We also protected our main branches from direct commits and establish rules for
making commits and PRs, which will allow us to keep the history clean and
automatically generate changelogs.

## **UI Design Drafts**

For now we plan to have only 3 main screens in our web-application.

### Authentication

Before booking a room, a user need to authenticate in our service. We think that
it will be enough to have a single “Login” button, which will redirect the user
to the Innopolis SSO page.

![auth.png](/bookinng/design-drafts/auth.png)

### Booking a Room

When authorized, the user will see the main booking screen, where it can choose
date and time for a new event, specify a title, and see all available rooms on
the map of the 3rd floor.

![booking.png](/bookinng/design-drafts/booking.png)

### TV-screen Dashboard

We also want to use the TVs that are located outside the rooms to provide useful
information to students and staff who pass near the room and want to know about
the current event that is going on in the room and get a general idea of the
current schedule of this room. We received a useful feedback during the first
week from students, where they talked about current problems with displaying
time and other data, and also offered interesting ideas about what they would
like to see on these screens.

![tv.png](/bookinng/design-drafts/tv.png)

So far, we have only managed to develop a calendar design that will be visible
on the TV, but we are still thinking about what the most important information
should be visible on TVs and how it can be displayed in the most convenient way
for user’s perception.

{{< hint info >}}
Of course, these are just the wireframes, and the actual design will be
consistent with the Innopolis University’s infrastructure and be user-friendly.
We arere hardly working on making it minimalistic and intuitively useful for
our users.
{{< /hint >}}

## **Week 2 Questionnaire**

**1. Tech Stack Resources**

> Our team members are actively developing and pumping up their skills by
> completing online courses and reading classic literature in our field.
> 
> 1. **[Fluent Python by Luciano Ramalho](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)**
> 2. **[Clean Architecture by Robert Martin](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/)**
> 3. **[Design Patterns by GoF](https://www.amazon.com/gp/product/0201633612)**
> 
> This way we get acquainted with the experience of other successful developers
> and fill the cones ourselves.

**2. Mentorship Support**

> 1. We communicate with Andrey Markov, he will help us in case of difficulties
>    with creating a booking API (backend).
> 2. We can contact developers of open-source tools we participated in
>    developing of which in public Telegram groups.

**3. Exploring Alternative Resources**

> We feel comfortable with our tech stack and we have the great resources that
> we hope will fill all the gaps we will encounter during the development
> process:
> 
> 1. [Next.js documentation](https://nextjs.org/docs)
> 2. [FastAPI documentation](https://fastapi.tiangolo.com/)
> 3. [Docker documentation](https://docs.docker.com/)
> 4. [exchangelib documentation](https://ecederstrand.github.io/exchangelib/)
>    for working with Microsoft Outlook API
> 5. [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
>    as a JavaScript reference

**4. Identifying Knowledge Gaps**

> Overall, our team consist of several people. And aggregation of their skills
> and knowledge cover all necessary fields of our project. However, we can
> highlight several point of development where our experience is weak:
> 
> - DevOps
> - QA
> 
> We don’t consider this a big problem, and if these weaknesses will raise some
> issues, we have a lot of resources and smart developers in the university to
> resolve the problems. As a last resort, we can get support and ready-made code
> templates from language models like ChatGPT.

**5. Engaging with the Tech Community**

> We consulted with development department in Innopolis University and agreed
> that we are going to use and that is suitable for them for further
> maintenance. We also have an experience to work with our tech stack in
> real-world projects maintained by experts, so we can contact them when we
> need an advice.

**6. Learning Objectives**

> Obtaining experience of working with our tech stack and experience of working
> as a team is the main goal of our project. To achieve this goal we …
> (see next question).

**7. Sharing Knowledge with Peers**

> Currently, we have several chats, where we share our knowledge about
> different fields:
>
> - Backend
> - Frontend
> - DevOps
>
> We also a have a common Notion workspace, where we create guides and collect
> all information and resources we found to be useful.

**8. How have you leveraged AI to compensate for any lacking expertise in your tech stack?**

> We use ChatGPT and GitHub Copilot to increase the code-writing speed and to
> save time on reading documentation and searching for frequently used pieces
> of code on the Internet.

## **Team Allocation**

- **Vladislav Deryabkin** is responsible for managing the project execution,
  designing the system architecture, uploading weekly reports on time, helping
  with writing code for frontend and backend, making sure each team member
  actively works on his task and receives support in case of any difficulty.
- **Yaroslav Kivaev** is responsible for DevOps, helping with Docker, k8s, etc.,
  designing architecture of the backend, managing team communication, helping
  with writing code for frontend and backend.
- **Koshmanova Ekaterina** is responsible for designing all interfaces,
  creating diagrams and flowcharts for reports, making sure that design of our
  application is consistent with the style of Innopolis University, creating an
  SVG image of the map from the PDF drawing, which then will be used by Anton
  to create the interactive React-component.
- **Vadim Zbarashchenko** is responsible for the backend in general, writing the
  code, breaking the system down into small pieces, delegating part of the work
  to Ruslan, making sure code meets the requirements and code-style set by the
  team.
- **Ruslan Bakirov** is responsible for writing backend code, closing tasks and
  issues that will appear during development and after receiving users feedback.
- **Skorkin Anton** is responsible for creating an interactive map of the
  university and wrapping it into the React-component, which will be improted
  and used in our web-application.
