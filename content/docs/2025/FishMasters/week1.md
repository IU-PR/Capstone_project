---
title: "Week #1"
---

# Week #1

## Project description

### Project name: Fish Masters

**Code repository**: https://github.com/IU-Capstone-Project-2025/FishMasters

The problem with fishing novices is lack of knowledge of good spots, different species, and bait types. On the other hand, veteran fishermen might lose interest in the craft after some time.

The core idea of the project is to make fishing more accessible for beginners and more engaging for experienced anglers.

**For beginners**, the app helps answer key questions like:
- Where to fish?
- What species are found in nearby waters?
- What bait and techniques to use?

**For experienced users**, the app introduces a gamified experience:
- Catch-based ranking and level system;
- Rewards and in-app bonuses for contributing data, helping others, and catching rare fish.

To support this, the mobile application includes:
- A map of nearby fishing spots with information on fish species and user activity;
- A rating and level system that progresses based on catches;
- A machine learning component that processes photos of caught fish to identify the species and award experience points based on rarity.

By combining useful information, social interaction, and gamification, the app creates a fishing companion that grows with the user.

### **Team Members**

| Team Member                             | Telegram Alias   | Email Address   | Track                                       | Responsibilities   |
|-----------------------------------------|------------------|-----------------|---------------------------------------------|--------------------|
| Stepan Vagin     | @Pan_or_propan | s.vagin@innopolis.university | ML, Lead | Overall project coordination, Fish species identification algorithms using computer vision |
| Kostya Zimin            | @plaffyyy | k.zimin@innopolis.university | Backend | Schema design for users, catches, fish species, and location data, User authentication, authorization, and data protection |
| Ivan Vasilev            | @Worried_Seat | i.vasilev@innopolis.university | ML | Photo analysis for catch verification and quality assessment, Performance tracking and continuous model improvement
 |
| Kirill Greshnov           | @didukyril | k.greshnov@innopolis.university | Flutter, UI/UX | Primary Flutter app development and architecture, User journey mapping, wireframing, and interaction design |
| Egor Belozerov            | @againlose | e.belozerov@innopolis.university | DevOps | Automated testing, building, and deployment pipelines, Database deployment, backup strategies, and maintenance  |
| Damir Sadykov | @SamAntonD | d.sadykov@innopolis.university | Flutter, UI/UX | Primary Flutter app development and architecture, Usability testing coordination and feedback implementation|
| Adel Gaznanov | @eternald3spair | a.gaznanov@innopolis.university | Backend | Backend scalability and response time optimization |


## Brainstorming

### Ideas during brainstorming

1. Game for fishermen - an application for fisherman to find fishing places, check on fish speices and compete between each other.
2. DnD game - website for playing Dnd, user joins as master, chooses all necessary attributes and invite other players
3. Map for runners - an application for runners to build routes for their runs, have social platform
4. Death by AI - a game where dangerous situation is given and the user should provide the way to escape it, AI continue building the story and decide if user survived or not
5. Game for hunters - same as the fish game, but with birds, animalc, etc.

### Brief market research / problem validation

### **1. Global Fishing Watch ([https://globalfishingwatch.org/](https://globalfishingwatch.org/))**

**Focus:** Monitoring global fishing activity via satellite/AIS data (more about tracking vessels than fish species).  

**Pluses:**
- Uses **real-time satellite tracking** to monitor fishing vessels worldwide (great for transparency and anti-illegal fishing).
- Strong **data visualization** (heatmaps, vessel tracks).
- Focus on **sustainability and overfishing prevention**.

**Minuses:**
- **Not focused on fish species or fishing techniques**—more about vessel movement.
- **Limited practical use for small-scale fishers** (geared toward policymakers/NGOs).
- **Requires technical expertise** to interpret data.
---

### **2. FisherMap ([https://ru.fishermap.org/fish-map/](https://ru.fishermap.org/fish-map/))**

**Focus:** Interactive map of fishing spots with species info and user reports.  

**Pluses:**
- **Crowdsourced data** (users submit fishing reports, photos, and tips).
- **Detailed species profiles** (habitat, bait, techniques).  
- **Localized insights** (water conditions, best seasons).

**Minuses:**
- **UI is outdated**
- **Relies heavily on user submissions**—may lack data in some areas.
---

### **3. Mesto.Fish ([https://mesto.fish/](https://mesto.fish/))**

**Focus:** Social network for fishers (sharing catches, spots, techniques).  

**Pluses:**
- **Community-driven** (like "Instagram for fishers").   
- **Gamification** (leaderboards, catch records).
- **Mobile-friendly**.

**Minuses:**
- **UI is outdated**
---

## Basic requirements

### Target users and their primary needs

### Target Audience
We defined target audience as 2 main groups: **primary target audience** and **secondary target audience**

#### Primary Target Audience
- **Recreational Fishers**
    - People who catch fish as a hobby or during vacation
    - Prefer discover new spots
    - Share photos of their catches
    - Track personal fishing history

- **Competitive fishers**
    - Highly engaged fishers who participate in tournaments
    - Compete on leaderboards
    - Earn points and achievements
    - Find high-potential spots

- **Content creators**
    - Users who create content in social medias (e.g. YouTube)
    - Share verified or top catches
    - Film educational and guideline content

#### Secondary Target Audience
- **Newbees in fishing**
    - People who only start their fishing journey
    - Discover beginner-friendly spots
    - Learn what species can be found in specific places
    - Get motivation from other users

- **Fishing clubs and communities**
    - Local fishing groups who organize group challenges
    - Share member catches
    - Track club performance or leaderboard standings
### User stories

- **Fishing Location Discovery**

    As a fisherman
I want to search and discover fishing locations with detailed information (water type, fish species, accessibility, regulations) 

    So that I can plan effective fishing trips and find new spots that match my preferences and skill level.

    Acceptance Criteria:

    - Interactive map showing fishing locations with filters (freshwater/saltwater, fish species, difficulty)

    - Location details including GPS coordinates, access instructions, parking availability

    - User ratings and recent fishing reports for each location
    
    - Weather conditions and best fishing times for each spot

- Fish Species Knowledge Base

    As a fishing enthusiast
I want to access a comprehensive database of fish species with identification guides, behavior patterns, and fishing techniques

    So that I can improve my fishing success rate and learn about different fish I might encounter.

    Acceptance Criteria:

    - Searchable database with high-quality images and detailed descriptions
    
    - Information on habitat, feeding patterns, seasonal behavior, and best baits/lures

    - Quick identification tool using visual characteristics

    - Regional fish species filtering based on location

- Catch Logging and Competition

    As a competitive angler
I want to log my catches with photos, measurements, and location data, and compare my achievements with other users

    So that I can track my progress, participate in competitions, and establish my reputation in the fishing community.

    Acceptance Criteria:

    - Photo upload with automatic metadata capture (location, timestamp)

    - Measurement tools for length/weight with verification mechanisms

    - Leaderboards for biggest fish, rarest catches, and seasonal competitions

    - Achievement badges and ranking system

    - Catch verification through community voting or photo analysis

### Initial scope

**Core Features (MVP - Minimum Viable Product)**
**User Authentication**

- User registration/login system

**Fishing Location Database**
- Map with locations

**Fish Species Knowledge Base**
- Database of 10+ common fish species with images and basic info

**Catch Logging System**
- Photo upload with basic metadata
- Manual entry of catch details (species, size, location, date)
- Personal catch history and statistics

**Final Features**
**User Authentication & Profiles**

- User registration/login system
- Basic profile creation with fishing experience level
- Profile customization and privacy settings

**Fishing Location Database**
- Interactive map with 50+ pre-populated fishing locations
- Basic location information (coordinates, fish species, access type)
- Simple search and filtering capabilities

**Fish Species Knowledge Base**
- Database of 100+ common fish species with images and basic info
- Search functionality by name or characteristics
- Basic identification guide with key visual features

**Catch Logging System**
- Photo upload with basic metadata
- Manual entry of catch details (species, size, location, date)
- Personal catch history and statistics


## Tech-stack

**Flutter**
- High performance for iOS and Android apps (smooth UI interactions);
- Rich plugin ecosystem;
- Hot Reload;

**Flutter plugins**
- firebase_auth - secure user authentification;
- cloud_firestore - real-time sharing/updating of user messages;
- geolocator - for user's current location
- flutter_rating_bar - UI for rating
- image_picker - pictures upload from gallery/camera
- flutter_map - map draw and interaction

1. Java: powerful and popular programming language, built-in auth support, integration with Spring Boot. Maybe add Kotlin, which is just the best Java.
2. Spring Boot: very powerful tool that helps you write coherent code quickly, build-in Spring Security(for auth and registration), Kafka configuration , Redis configuration, Spring Data JPA for communication with database.
3. Spring Security + JWT - fast realizable secure authentication for mobile app.
4. PostgreSQL - store user data, fishing spots, and support geo-queries.
5. Redis - caching user rankings, recent catches, and heavy-read data. Ranking data for integrating with ML, as it's frequently changable is a good way to store it in cache.
6. Kafka - asynchronous communication for tasks like image processing or notifications. For microservices communication.
7. Spring WebClient - this tool currently in decision process. It can be powerful when our ML service proccess some image, all our program can do another staff in the same time. Or we can push notification in async tasks by another threads in program.
8. Liquibase - manage database schema migrations.
9. Docker + Docker Compose - package the backend with all dependencies. Also, it's easy way to build project in CI/CD when we don't have many resources for the project.


# Weekly commitments

## Individual contribution of each participant

Stepan Vagin - created both repository, completed report, assigned tasks, wrote user-stories and initial scope, team member description, wrote general ML idea of the project  ([https://docs.google.com/document/d/1cXK-wSGzl9AX5f-sgE7ZeGW06-FSuYZvN-cBA3Hh3g0/edit?tab=t.0](https://docs.google.com/document/d/1cXK-wSGzl9AX5f-sgE7ZeGW06-FSuYZvN-cBA3Hh3g0/edit?tab=t.0))

Kostya Zimin - created mock test PR ([https://github.com/IU-Capstone-Project-2025/FishMasters/pull/3](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/3)), wrote backend stack description

Ivan Vasiliev - wrote market analysis, found 3 competitors (links at the start of the document), found several datasets for ML part: 
1. [https://www.kaggle.com/datasets/markdaniellampa/fish-dataset](https://www.kaggle.com/datasets/markdaniellampa/fish-dataset)
2. [https://www.kaggle.com/code/fahadmehfoooz/fish-analysis](https://www.kaggle.com/code/fahadmehfoooz/fish-analysis)
3. [https://www.kaggle.com/datasets/crowww/a-large-scale-fish-dataset/data](https://www.kaggle.com/datasets/crowww/a-large-scale-fish-dataset/data)
4. [https://www.kaggle.com/datasets/sripaadsrinivasan/fish-species-image-data](https://www.kaggle.com/datasets/sripaadsrinivasan/fish-species-image-data)

Kirill Greshnov - wrote project statement and project idea, developed hello world flutter app with map, PR: ([https://github.com/IU-Capstone-Project-2025/FishMasters/pull/1](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/1))

Egor Belozerov - defined rules of the repository, add initial structure, commit: ([https://github.com/IU-Capstone-Project-2025/FishMasters/commit/57eae440431cd0f1a3528526e9f66945cd3fbac3](https://github.com/IU-Capstone-Project-2025/FishMasters/commit/57eae440431cd0f1a3528526e9f66945cd3fbac3))

Damir Sadykov - wrote flutter tech stack explanation, designed the first version of UI: [https://drive.google.com/drive/folders/1MiDyIRxjoWyxYUD77iSfidDhBQRPLCr3?usp=drive_link](https://drive.google.com/drive/folders/1MiDyIRxjoWyxYUD77iSfidDhBQRPLCr3?usp=drive_link)

Adel Gaznanov - wrote targer audience analysis, created hello world endpoint, PR: ([https://github.com/IU-Capstone-Project-2025/FishMasters/pull/2](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/2))

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).