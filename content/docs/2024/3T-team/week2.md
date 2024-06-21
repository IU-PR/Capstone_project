---
title: "Week #2"
---

# Week #2

## **Choosing the Tech Stack, Designing the Architecture**

### **Team Allocation**

| Team Member              | Role   | Tech Stack Used|
|--------------------------|---------------|-----------------|
| Kalviyainen Arsenii | Team Lead | Trello, Figma, Google meet |
| Karim Nasybullin | Android Developer/Designer | Kotlin, Dagger 2, Coroutines, Compose, Flow, MVI/MVVM Architecture, Yandex map API / Figma |
| Ilia Sardanadze | Android Developer | Kotlin, Dagger 2, Coroutines, Compose, Flow, MVI/MVVM Architecture, Yandex map API |
| Arsenii Pavlov | Backend Developer | FastAPI, SQLAlchemy, PostgreSQL, PostGIS |
| Ivan Beltsov | Backend Developer | FastAPI, SQLAlchemy, PostgreSQL, PostGIS |

### **Evaluation and Recommendations for Our Project's Tech Stack from AI**
   The explanations and which technical stack we have chosen are in the last paragraph of the report week1.md. Since the technical stack has been discussed and selected since week 1, we decided to turn to AI and find out how to improve it and what else can be added there:
## **Current Tech Stack**

**Android Development:**
- Kotlin
- Dagger 2
- Coroutines
- Compose
- Flow
- MVI/MVVM
- Yandex Map API

**Backend Development:**
- FastAPI
- PostgreSQL
- SQLAlchemy
- PostGIS

## **Key Considerations**

1. Scalability
2. Performance
3. Security
4. Expertise of Team Members

## **Android Development Stack**

Kotlin
- **Pros:** Modern language with excellent Android support, concise syntax, null safety, and interoperability with Java.
- **Cons:** Newer compared to Java, but rapidly gaining support.

Dagger 2
- **Pros:** Robust dependency injection framework, compile-time verification, and broad adoption.
- **Cons:** Steeper learning curve, boilerplate code.

Coroutines
- **Pros:** Simplifies asynchronous programming, less error-prone compared to callbacks or RxJava.
- **Cons:** Newer approach; requires understanding of coroutine scope and context.

Compose
- **Pros:** Modern toolkit for building native UI, reduces boilerplate, declarative UI.
- **Cons:** Still evolving, requires learning a new paradigm if accustomed to XML-based UI.

Flow
- **Pros:** Integrated with Kotlin coroutines, designed for reactive programming.
- **Cons:** May require a shift in thinking for those used to RxJava.

MVI/MVVM
- **Pros:** Promotes a clear separation of concerns, easier to test, and maintain.
- **Cons:** Can be complex to implement correctly; requires discipline.

Yandex Map API
- **Pros:** Specialized for certain regions, comprehensive mapping solutions.
- **Cons:** Limited global coverage compared to Google Maps API, licensing restrictions.

## **Backend Development Stack**

FastAPI
- **Pros:** Modern, high-performance, easy to use, async support, great documentation.
- **Cons:** Newer framework, smaller community compared to more established frameworks.

PostgreSQL
- **Pros:** Advanced SQL compliance, strong community, robustness, extensibility with PostGIS.
- **Cons:** Can be complex to manage; tuning performance requires expertise.

SQLAlchemy
- **Pros:** Powerful ORM, flexible, supports both SQL and ORM querying.
- **Cons:** Can introduce complexity; performance overhead compared to raw SQL.

PostGIS
- **Pros:** Adds spatial database capabilities to PostgreSQL, excellent for geospatial queries.
- **Cons:** Learning curve for spatial SQL; potential performance impact.

## **Recommendations**

Scalability
- **Android:** Your current stack should scale well with appropriate architecture and modularization.
- **Backend:** FastAPI can handle high concurrency; PostgreSQL with PostGIS is scalable but ensure indexing and query optimization for geospatial data.

Performance
- **Android:** Use profiling tools to optimize Compose and ensure efficient coroutine usage.
- **Backend:** FastAPI is performant, but ensure database performance tuning and appropriate caching mechanisms.

Security
- **Android:** Follow secure coding practices, use encryption where necessary, and validate inputs from the Yandex Map API.
- **Backend:** Implement secure authentication/authorization, use parameterized queries to avoid SQL injection, and ensure secure communication (HTTPS).

## **Additional Tools & Considerations**

1. **Monitoring & Logging:**
   - Use tools like **Sentry** or **Crashlytics** for Android, and **Prometheus** with **Grafana** for backend monitoring.

2. **Testing:**
   - Ensure comprehensive unit and integration testing. Use **JUnit** and **Espresso** for Android, and **pytest** for backend.

3. **CI/CD:**
   - Implement CI/CD pipelines with tools like **GitHub Actions**, **Travis CI**, or **Jenkins** to streamline deployment and ensure code quality.

4. **API Documentation:**
   - Utilize **Swagger** (OpenAPI) with FastAPI for automatically generated and interactive API documentation.

## **Conclusion (tech stack)**

Based on the response from AI, we realized what we were missing at one of the stages described above, we will be able to take the advice and use what we were advised


## **Architecture Design**

Please answer the following questions related to the lean methodology:

1. Component Breakdown:\
Externally, the application has 3 pages, the first is the map itself with markers, the second is a list of recommendations and the third is a user profile.\

   First page:
   * visual representation of the map (Frontend using the Yandex Maps Api)
   * clickable markers, which will pop out the bottom sheet with information (Frontend + Backend)
   * determining the user's location using geolocation (Backend)
   * route rendering (Frontend + Backend)

   Second page:
   * Creating a list of attractions based on user preferences (Backend)
   * Drawing a list of attractions for the user (Front end)
   * Sorting Filters (Frontend + Backend)

   Third page:
   * Record and give information about the user (Frontend)
   * Visual design of information for the user (Backend)
   * Registration system (Frontend + Backend)


2. Data Management:

   We chose to use the PostgreSQL relational database system to store our data for several reasons:
- **Security**: PostgreSQL prioritizes security, offering robust mechanisms for user authentication, data encryption, and access control.
- **Reliability and Stability**: Renowned for its robustness and stability, PostgreSQL is widely used in production environments for both small and large-scale applications.
- **Scalability**: PostgreSQL can manage large volumes of data and scale effectively as our project grows.

3. User Interface (UI) Design:\
Even before the start of development, we discussed and worked out the design of our application in the field of ui/ux, you can find it here:
https://www.figma.com/design/jqjzGlMgBuEyci7hsU4Yf7/travelling?node-id=1-2&t=aCALY30XQ9yohEAH-1

4. Integration and APIs:\
For our project, the main one is the map. In order to make it and work with it conveniently, we use the open Yandex Maps API. Which helps us to significantly reduce the amount of work and not create our own map.

5. Scalability and Performance:\
All parts of our project are designed to be easily scalable and work with a large number of users. At the time of launch, we have set a limit of 5,000 monthly users, but if the project grows, this number can be increased. However, we will need additional funding for this expansion, as the Yandex Maps API for 5,000+ users comes with a paid subscription, and we will also need to invest in a more powerful server for our databases and backend.

6. Deployment and DevOps:\
To be honest, we haven't discussed this yet, but most updates to the client, regarding content (pictures, videos, etc.) will be automatically updated once they are changed on the server.

## **Week 2 questionnaire**

1. Tech Stack Resources: Are you utilizing any project-based books that specifically cover your tech stack and help you build your project? If yes, please provide the names of these books (name at least 3). How do you anticipate utilizing these materials to enhance your knowledge and expertise in your tech stack?

   Since our team members were familiar with the technical stack before the project started, no specific books were used during the work.

2. Mentorship Support: Do you currently have a mentor actively involved in your project? If yes, kindly share the name of your mentor and explain how their guidance has positively influenced your project. If you don’t have a mentor yet, have you considered seeking one? How do you believe having a mentor could contribute to the success of your project? Remember, having an experienced mentor that can guide you and your team is your responsibility.

   We don't have an experienced mentor, but one of our team members has extensive experience in development in a large corporation. He is willing to help and mentor us during our project.
3. Exploring Alternative Resources: In addition to project-based books, what other resources have you explored to expand your understanding of your tech stack? This could include online courses, video tutorials, documentation, or any other sources that have been valuable in filling knowledge gaps. Please, name at least 3 resources

   1) To understand how to work with Yandex API, we used https://yandex.ru/maps-api/.
   2) To understand how to work with Compose, we used https://developer.android.com/develop/ui/compose/documentation
   3) To understand how to work with FastApi, we used https://fastapi.tiangolo.com/

4. Identifying Knowledge Gaps:

   We used AI to identify these issues and it helped us realize that we had not thought about monitoring and testing our solution. So, we decided to revise our technical stack and add missing tools, but first, we needed to understand the principles of their operation. We are doing this in parallel with our main task. At the moment, we don't need this technology stack because it's at least a week until we test our solution, and according to our plan, it will be 2 weeks.

5. Learning Objectives: What specific learning objectives have you set for yourself and your team in relation to your tech stack this week? How do you plan to achieve these objectives, and what strategies or resources will you employ to deepen your understanding?

   This week, our Android developers had a training task. One of them was an experienced developer who knew how to use the Yandex Maps API and Compose, while the other was a beginner. During this week, it was necessary for the beginner to learn how to work with these tools. The training task was completed successfully, and both developers are now comfortable using Compose and have no difficulty with it.

6. Sharing Knowledge with Peers: How have you been sharing your knowledge and expertise with your teammates? Have you organized any knowledge-sharing sessions or discussions to facilitate the exchange of insights and experiences related to your tech stack?

   We had two meetings to share experiences between team members. Since we had a person with extensive experience in development, they explained exactly how we would create our application and what needs to be done for it. After that, the team familiarized themselves with the documentation on the necessary technical stack and began working. In the course of our work, we also shared our experiences so that the development was productive. If someone lacked knowledge in a particular area, we found someone who could help, either within the team or externally.

7. How have you leveraged AI to compensate for any lacking expertise in your tech stack?

   As mentioned in the previous section, we used this tool to identify any gaps in our technology stack and determine what additional tools could be added to make the project more successful. I am pleased that the AI has identified our current technology stack as optimal, suggesting only a few additional tools for monitoring and testing. In any case, these tools will be useful in the next two weeks when we begin testing our project.

## **First Sprint Progress Report**

In our roadmap for the first sprint (06/03/2024 - 06/16/2024), we have planned two major goals: creating a database of attractions and creating a map with interactive markers for the attractions.

For each major task, we initially broke down the subtasks and assigned them to team members based on their skill sets. Android developers had their own set of tasks, and back-end developers had theirs. Once the tasks were assigned, we started working on them.

During the course of the project, we encountered some unexpected challenges, but they did not significantly impact our team's productivity or our ability to stay on schedule.

In this particular sprint, we completed the following:

1. Map with the boundaries of Innopolis city and markers for each landmark.
2. Data database: sights, cities, categories, reviews, files.
3. Methods of communication between client and server to retrieve data: information about attractions, user information.
4. Progress bar with information for each marker.