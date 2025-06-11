---
title: "Week #1"
---

# Week #1

## Project description

### Project name: *Recommendation System*

**Code repository**: https://github.com/IU-Capstone-Project-2025/Recommendation-System

**General idea**

The project is a distributed system that enables users to rate books. Based on their reading history and given ratings, the system generates personalized recommendations.

**Problem Statement**

In today's world, where thousands of books across various genres and topics are published every day, it becomes increasingly difficult for the average user to choose what to read. Faced with *information overload* and *a general decline in reading habits*, users are less willing to spend time browsing and comparing options. They expect **fast**, **accurate**, and **personalized recommendations**. 

Our motivation for this project is to address this growing challenge by developing a scalable, efficient recommendation system that processes large volumes of user-generated data (ratings, reviews) and delivers high-quality book recommendations tailored to individual preferences — all with minimal delay. This not only enhances user experience but also promotes reading by reducing friction in the decision-making process. 

*Key problems* include managing data consistency across components, optimizing performance for analytical workloads, and optionally, integrating ML techniques for semantic understanding of user feedback.


### **Team Members**





| Team Member                             | Telegram Alias   | Email Address   | Track                    | Responsibilities                                                                          |
|-----------------------------------------|---------------|-----------------|--------------------------|-------------------------------------------------------------------------------------------|
| Denis Troegubov     | @BogGoro | d.troegubov@innopolis.university | Data Engineer, Team lead | Сreate data pipeline, analyse user data, generate personalised recommendations datamart, scrape or find books data |
| Timur Garifullin            | @CyberToad | t.garifullin@innopolis.university | Backend                  | Endpoints, authentication, and user data collection                                       |
| Grigorii Belyaev            | @bluvvis | g.belyaev@innopolis.university | Frontend                 | Website visualization, interaction with the backend                                       |
| Peter Zavadskii             | @user_abraham | p.zavadskii@innopolis.university | Backend                  | Kubernetes, deployment, proxy for the database.                                           |
| Adelina Karavaeva             | @a_adelina_k | ad.karavaeva@innopolis.university | Frontend/Design          | 	Frontend design, website visualization, reports                                          |


## Brainstorming

### Ideas during brainstorming

1. **Efficient Personalized Recommendations** – Apply data engineering for generating recommendations for a larger audience  with less computational power (Use an analytical database and independently create data marts outside the backend to reduce its load)

2. **Discovery Mode** – Optional toggle to recommend books outside the user’s comfort zone, promoting discovery. 

3. **Mood-Based Recommendations** *(optional)* – Recommends books based on inferred or user-selected moods (e.g., "thought-provoking").

### Brief market research / problem validation


After a brief market research, we identified several products similar to ours. However, upon analyzing them, we concluded that they fail to meet some of our key requirements, which makes the development of our own solution *relevant and justified*.

**Goodreads** uses a hybrid recommendation system (based on reading history, ratings, friends, and similar books), but it is primarily focused on the **English-speaking market**.

**Bookmate (Yandex Books)** is a monolithic mobile application **limited to its internal licensed content**. In contrast, our project is a **distributed system** designed for scalability, microservice architecture, and easy integration with external platforms.
### 📊 Feature Comparison Table

| **Feature**                                             | **Goodreads**                     | **Bookmate (Yandex Books)**                 | **Our Project**                     |
|---------------------------------------------------------|-----------------------------------|---------------------------------------------|-------------------------------------|
| Personalized Recommendations                            | ✅ Yes, hybrid-based               | ⚠️ Limited to its internal licensed content | ✅ Planned                           |
| Book Ratings & Reviews                                  | ✅ Fully supported                 | ✅ Supported                                 | ✅ Planned                           |
| User Reading Lists (*Read*, *Reading*, *Planned*)       | ✅ Read, Want to Read, etc.       | ⚠️ Limited                                  | ✅ Planned                           |
| Language/Localization Focus                             | ❌ Primarily English-only         | ❌ Primarily Russian-only           | ✅ Multi-language support planned    |
| Scalable Infrastructure                                 | ⚠️ Medium                         | ❌ Monolithic                                | ✅ Kubernetes-based scaling  planned |
             

## Basic requirements

### Target users and their primary needs

-   **Casual readers**  
    These users occasionally read books and want quick, personalized suggestions without spending time browsing.  
    **Needs:** simplicity, speed, and relevance in recommendations.
    
-   **Avid readers**  
    Users who read frequently and want diverse, high-quality recommendations based on their reading history and preferences.  
    **Needs:** constant and frequent updates of recommendations, accurate filtering, personalized content, variety across genres
-   **Authors and Writers**  
    Writers looking to better understand market demand, current trends, and reader preferences in order to improve their work or target it more effectively.  
    **Needs:** access to weekly popularity rankings, visibility into trending genres and titles, feedback via user ratings and comments.

    
### User stories

-   **As a user**, I want to receive a list of recommended books that match my interests based on past ratings so I can quickly decide what to read.
-   **As a user**, I want to rate a book I've read so that the system can better understand my preferences.
-   **As a user**, I want to see brief descriptions of recommended books so I can quickly  understand if the book suits me
- **As a user**, I want to maintain a personal reading list (Read, Reading, Planned) so I can organize my reading journey.
- **As a user**, I want to leave and read comments on books so I can share opinions and discover what others think.
- **As an author**, I want to see aggregated feedback (ratings and comments) on my books so I can understand reader reception.
- **As an author**, I want to view the "Most Popular This Week" list so I can understand current reader interests and trends to better align my future writing.
    

### Initial scope


Book Sorting and Listing

 - Support for multiple sorting modes: Top Rated, Most Popular, Trending This Week (optional), Personal Recommendations


Book Details and Interactions

- Dedicated book detail page displaying metadata (title, author, description)

- Ability to submit a rating for the book

- Ability to leave comments on the book

User Profile and Lists

- Personal library with categorized book statuses: (Already Read, Currently Reading, Planned to Read)

- Display of previously given ratings


## Tech-stack
-   **Python, FastAPI** – main backend technologies

-   **Golang** – will be used for building a proxy service

-   **Airflow** – will be used as the data orchestration tool
    
-   **Hadoop** – distributed file system for large-scale data storage
    
-   **PostgreSQL** – transactional relational database
    
-   **Greenplum** – analytical database for complex queries and reporting
    
-   **Nginx** – will be used as a load balancer to ensure availability and scalability
    
-   **Kubernetes** – for container orchestration and deployment
    
-   **CI/CD** (optional) – for continuous integration and deployment automation
    
-   **Frontend** – will be implemented using HTML, CSS, and React
    
-   **Machine Learning** (optional) – to enhance recommendation quality through sentiment analysis of user comments and reviews




# Weekly commitments

## Individual contribution of each participant


Denis Troegubov - initial project and repositories setup, defining tech stack, brainstorming

Timur Garifullin - brainstorming, defining tech and initial stack,

Grigorii Belyaev - brainstorming, user stories

Peter Zavadskii  - initial project and repositories setup, defining tech stack, prototyping the backend, brainstorming

Adelina Karavaeva - report, initial design in figma, brainstorming

