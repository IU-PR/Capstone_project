---
title: "Week #1"
---

# Week #1

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member              | Telegram ID   | Email Address   |
|--------------------------|---------------|-----------------|
| Kalviyainen Arsenii (Lead) | @tyw_0 | a.kalviyainen@innopolis.university |
| Karim Nasybullin | @karim_nasybullin | k.nasybullin@innopolis.university |
| Arsenii Pavlov | @arsepav | ars.pavlov@innopolis.university |
| Ilia Sardanadze | @Damncaf_you_crazy | I.sardanadze@innopolis.university |
| Team Member 5 | @FORZpewpew | i.beltsov@innopolis.university |

### **Value Proposition**

- Identify the Problem:\
Our project/application aims to create a convenient environment for exploring the sights. The relevance of this project can be seen even within Innopolis, as there are approximately 100 excursion groups visiting the city each day, all interested in learning about its famous places and attractions. We solve the problem of the inaccessibility of information that is of interest to tourists and visitors to our city (and in the future, to any city).

- Solution Description:\
Our solution is to develop an application that provides users with a map of attractions, recommendations, and interesting stories, as well as the opportunity to communicate with friends. The app will contain detailed information about each attraction, allowing users to explore them in more depth. Additionally, we have decided to include a social network component to encourage users to interact with each other and share their experiences.

- Benefits to Users:\
In addition to receiving information about the sights in various formats (audio guide, text, photos, etc.), our users will also have the opportunity to compete with their friends (achievement system) and post beautiful photos next to interesting places, write reviews, and of course, ask questions about various objects.

- Differentiation:\
Our project is similar to the idea behind Yandex maps in many ways, but we specialize in attractions and provide not only a vast amount of information, but also an opportunity to ask questions. Additionally, we have a social network concept that will be more engaging for users than a traditional map with labels. Furthermore, we will implement an adaptive recommendation system.

- User Impact:\
Our solution is specifically designed for tourists, as we help them save time and money on individual tours. We give them the freedom to explore independently and comfortably, without spending too much time or money. For many tourists, this is an important and necessary feature.

- User Testimonials or Use Cases:\
Any tourist who wishes to visit Innopolis (or any other city), in theory, can find a brief overview of the attractions beforehand and decide whether they want to visit them. 
Another possible scenario is when a tourist arrives and is unsure of where to go. In such a case, we can provide them with a map and, if necessary, guide them along the route to their desired destination.

## **Lean Questionnaire**

Please answer the following questions related to the lean methodology:

1. What problem or need does your software project address? \
   Our project aims to solve the problem of lack of information about the sights and important places in the city, as well as a lack of interest in exploring them. In addition, we provide information about any place, regardless of whether or not the customer has visited it, so everyone has the opportunity to learn about those places they want to visit in advance.

2. Who are your target users or customers\
   Our target audience is tourists of all ages who are interested in learning more about a specific attraction in the city they have visited or are planning to visit. Our application also provides information about places that are not easily accessible, so people who may not be able to drive can still access information, photos, and audio guides.

3. How will you validate and test your assumptions about the project?\
   Before the start of the project, we conducted customer development, during which we learned exactly what people need. Customer development was conducted with tourists who came to Innopolis as a group or individually, with or without children. About 50 people were interviewed in May. Here is a list of the things we were able to learn:
   * We need a filter for attractions: with children and without children (for example, do not go to the theater with children, etc.)
   * We need the ability to build a route for several attractions at once
   * We need the ability to plan a route several days in advance
   * We need offline mode

   During the development process, we planned both a closed alpha test and an open beta test. For the beta test, we have already reached an agreement with a company based in Innopolis to help us. During each test, we will collect feedback and use it to improve our product.

4. What metrics will you use to measure the success of your project?\
   Our project is primarily aimed at working with people, so the key factor for success will be the satisfaction of people with our application.

5. How do you plan to iterate and pivot if necessary based on user feedback\
   In our project roadmap, there is time allocated for alpha and beta testing as well as bug fixes based on user feedback. In early July, we will have a week to test and add features based on the feedback and comments received. Also, in week 7, when the post-MVP is completed, we will repeat the process, but this time with real users.

## **Leveraging AI, Open-Source, and Experts**

Our team has a strategic plan to leverage the following resources for the development and success of our project:
   * Experts:\
   In order for our application to be successful, it is important for us to understand what tourists want from their visit to our attractions. Therefore, before we started development, we conducted several consultations with tour guides from Innopolis. We wanted to understand the key points that tourists are interested in and what they want to see. Throughout the development process, we will continue to hold meetings with these guides to discuss how we can make our attractions more interesting for tour operators. We want to ensure that our application meets the needs of our target audience and is successful.

   * Open-Source:\
   The basis of our application is a map, and in order to successfully implement it, we use the Yandex Maps open-source API, which will significantly reduce the amount of work involved. Additionally, a variety of open-source libraries and frameworks will assist us during the development process.

   * AI:\
   Our project currently does not incorporate AI, but we plan to incorporate it in the future as a consultant for tourists. This will allow them to interact with the AI and receive personalized recommendations for their cultural program. The AI will be able to provide additional information about the attractions and events on offer.
   
## **Defining the Vision for Your Project**

- Overview:\
   Our project is an app that includes: a map with markers for each attraction, a list of recommendations based on friends' preferences and categories, a profile with posts and stories, and a system for adding friends. We also have a system of achievements and rankings.\
   We have only one monetization method: a paid subscription, which gives users access to an audio guide, offline maps, and photo storage.\
   Our goal is to make it easier for people to find the information they need. Tourism is an important part of many Russian regions' economies, and we want to help tourists by simplifying their experience and saving them time and money.We want our solution to encourage people to travel and discover interesting places in every city in Russia, as many people are afraid or unwilling to start exploring other parts of the world for various reasons. With our application, this can be done right from their own homes.

- Schematic Drawings:\
   Before starting development, we created a roadmap for our project to understand how many resources and what we needed to implement our project successfully. Additionally, before the project began, we had already assembled a team of 5 people, including 4 developers and 1 project manager, and assigned responsibilities and scheduled tasks using Trello.
   <img src="../image.svg" alt="Untitled" border="0" style="max-width: 1600px; margin-top: -120px;">

- Tech Stack:
   * Back-end:\
      For this project, the following technologies, frameworks, and programming languages will be utilized:
      FastAPI,
      PostgreSQL,
      SQLAlchemy,
      PostGIS

      1. FastAPI\
      Reasons for Choosing FastAPI:\
      Performance: FastAPI is built on Starlette and Pydantic, making it one of the fastest web frameworks for Python. Its asynchronous nature ensures high performance, which is crucial for handling multiple requests efficiently.
      Ease of Development: FastAPI offers an intuitive and easy-to-use interface with automatic generation of interactive API documentation (Swagger UI and ReDoc). This enhances developer productivity and facilitates debugging.
      Type Safety: By leveraging Python type hints, FastAPI ensures robust code with fewer bugs and better maintainability.
      Scalability: FastAPI’s asynchronous support makes it highly scalable, handling large numbers of concurrent connections with ease.

      2. PostgreSQL\
      Reasons for Choosing PostgreSQL:\
      Reliability and Robustness: PostgreSQL is known for its stability and reliability, making it an excellent choice for production environments.
      Advanced Features: PostgreSQL supports advanced data types and performance optimization features, such as indexing, full-text search, and JSON support, which are beneficial for a wide range of applications.
      Open Source: Being open-source, PostgreSQL has a strong community and a wealth of resources, ensuring continuous improvements and support without licensing costs.

      3. SQLAlchemy\
      Reasons for Choosing SQLAlchemy:\
      ORM Capabilities: SQLAlchemy provides a robust Object-Relational Mapping (ORM) system, which simplifies database interactions by allowing developers to work with Python objects instead of raw SQL queries.
      Flexibility: It offers flexibility by supporting both ORM and Core (SQL Expression Language), making it adaptable to various project needs.
      Database Agnosticism: SQLAlchemy’s design allows for easy switching between different database backends, which provides future-proofing and flexibility in case the database needs to be changed.
      
      4. PostGIS\
      Reasons for Choosing PostGIS:\
      Geospatial Data Support: PostGIS extends PostgreSQL to handle geospatial data, providing powerful spatial querying capabilities. This is essential for projects involving geographical information and spatial analysis.
      Performance: PostGIS is optimized for handling large volumes of spatial data efficiently, making it suitable for applications that require geospatial computations.
      Integration: As an extension of PostgreSQL, PostGIS integrates seamlessly with the database, ensuring consistent performance and reliability.
   * Android development:
   For this project, the following technologies, frameworks, and programming languages will be utilized:
   Kotlin,
   Dagger 2,
   Coroutines,
   Compose,
   Flow,
   MVI/MVVM\
      1. Kotlin\
      Reasons for Choosing Kotlin:\
      Interoperability: Kotlin is fully interoperable with Java, allowing for seamless integration with existing Java codebases and libraries.
      Conciseness: Kotlin's concise syntax reduces boilerplate code, leading to improved readability and faster development.
      Safety: Kotlin's null safety features help eliminate null pointer exceptions, resulting in more stable and reliable code.
      Performance: Kotlin compiles to bytecode, running on the JVM with performance comparable to Java, making it suitable for high-performance applications.

      2. Dagger 2\
      Reasons for Choosing Dagger 2:\
      Dependency Injection: Dagger 2 provides a powerful dependency injection framework, allowing for better code organization, testability, and maintainability.
      Performance: Dagger 2 generates code at compile-time, ensuring efficient dependency injection with minimal runtime overhead.
      Scalability: It supports complex dependency graphs and scopes, making it suitable for large-scale applications.
      Community and Support: Dagger 2 has strong community support and is widely adopted in the industry, ensuring availability of resources and best practices.

      3. Coroutines\
      Reasons for Choosing Coroutines:\
      Asynchronous Programming: Coroutines simplify asynchronous programming in Kotlin, allowing for easier management of background tasks and concurrency.
      Readability: They enable writing asynchronous code in a sequential manner, improving code readability and maintainability.
      Performance: Coroutines are lightweight and efficient, reducing the overhead associated with traditional threading models.
      Integration: Coroutines integrate seamlessly with other Kotlin libraries and frameworks, enhancing overall developer productivity.
 
      4. Compose\
      Reasons for Choosing Compose:\
      Modern UI Development: Compose provides a modern, declarative approach to building UIs, enabling faster development and more intuitive code.
      Reusability: Compose encourages the creation of reusable UI components, promoting code reuse and modularity.
      State Management: It simplifies state management with built-in tools, leading to more predictable and maintainable UI code.
      Compatibility: Compose is designed to work seamlessly with existing Android views and UI frameworks, ensuring easy adoption in existing projects.

      5. Flow\
      Reasons for Choosing Flow:\
      Reactive Programming: Flow provides a robust framework for reactive programming in Kotlin, allowing for efficient handling of data streams and events.
      Concurrency: It offers built-in support for concurrent data streams, enabling responsive and scalable applications.
      Integration: Flow integrates well with coroutines, providing a cohesive and consistent programming model.
      Backpressure Handling: Flow includes mechanisms for handling backpressure, ensuring efficient and stable data processing.

      6. MVI/MVVM\
      Reasons for Choosing MVI/MVVM:\
      Architecture Patterns: MVI (Model-View-Intent) and MVVM (Model-View-ViewModel) provide structured approaches to building scalable and maintainable applications.
      Separation of Concerns: Both patterns promote a clear separation of concerns, making the codebase easier to understand, test, and maintain.
      Reactivity: MVI and MVVM support reactive programming principles, enabling responsive and dynamic UIs.
      Community and Best Practices: These patterns are widely adopted in the industry, with extensive documentation and best practices available to guide development.