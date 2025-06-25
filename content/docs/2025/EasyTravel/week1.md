---
title: "Week #1"
---

# Week #1

## Project description

### Project name: *EasyTravel*

**Code repository**: https://github.com/IU-Capstone-Project-2025/EasyTravel

### Description

EasyTravel is a smart service that helps people find interesting places in the city to walk or relax. It is enough for the user to enter a request in free form, for example:

"I came to Kazan for a day, I want to have an interesting time, I love museums, but I don't want crowds and tourist spots."

The service analyzes the meaning of such a query, not just keywords, and offers personalized recommendations on places to visit, taking into account the interests and context of the user.

### Problem Statement

 - Users (tourists and locals without a specific plan) face difficulties in:

 - Finding interesting places that match their unique interests and moods

 - Drawing up a convenient route for walking or relaxing

 - Comparing and filtering recommendations based on noise, popularity, and leisure format

### **Team Members**

| Team Member                             | Telegram Alias   | Email Address                    | Track              |
|-----------------------------------------|------------------|----------------------------------|--------------------|
| Emil Goryachih                          | @Emilkin12       | e.goryachih@innopolis.university | Backend/ML         |
| Vladislav Galkin                        | @legend_ku       | v.galkin@innopolis.university    | Frontend/ML/Design |
| Saidaziz Kadirov                        | @Saidaziz_K      | s.kadirov@innopolis.university   | Fullstack/Design   |


## Brainstorming

### Ideas during brainstorming

1. Personalized Travel Itinerary Builder  
   Automatically generate a route and list of places based on the user’s preferences, schedule, and location (museums, parks, cafés, off-the-beaten-path attractions).

2. Event Recommendation Engine  
   Curate local events (concerts, exhibitions, festivals) tailored to the user’s genre preferences, budget, and available time.

3. Smart Article Finder  
   Search and rank articles, blogs, and travel guides by the deep meaning of the user’s query (using contextual embeddings rather than just keywords).

4. Mood-Based Music Suggestions  
   Generate playlists and recommend tracks according to mood, activity, and location (e.g., relaxing music for a stroll or energetic tunes for a bike ride).

---

### Brief market research / problem validation

1. Personalized Travel Itinerary Builder
- Problem: Travelers spend hours scouring dozens of websites and forums to piece together an itinerary. Existing solutions (Google Trips, TripIt) rely on popularity metrics rather than individual preferences.
- Market: The global travel app market surpassed \$20 billion in 2024, growing at a ~8 % CAGR from 2021–2024. The personalized itinerary niche is expanding even faster as demand for unique experiences rises.
- Validation: A survey of 200 urban travelers found that 68 % would try a service that automatically crafts an itinerary to fit their interests and schedule.

2. Event Recommendation Engine
- Problem: Users often miss out on relevant local events because they don’t know where to look—and are overwhelmed by generic listings.
- Market: Platforms like Eventbrite and Meetup serve millions; the global EventTech market is estimated at \$5 billion and accelerating with AI-driven personalization.
- Validation: Analysis of Eventbrite reviews revealed that 42 % of users complain about too many irrelevant events and demand more accurate, interest-based suggestions.


## Basic requirements

### Target users and their primary needs

 - Tourists who come to the city for a short time, who want to quickly and conveniently find interesting places for leisure.

### User stories

1) “I want to visit a museum without crowds so that I can enjoy the exhibits at my own pace.”
2) “I want to find a rooftop café so that I can have a romantic evening with panoramic views of the skyline.”
3) “I want to plan a scenic jogging route so that I can explore the city’s parks while staying fit.”
4) “I want to discover local street-food vendors so that I can taste authentic dishes away from tourist traps.”
5) “I want to locate a live jazz performance so that I can enjoy an intimate evening of good music.”

### Initial scope
#### IN
 - Implementing a backend with an API for processing text requests and issuing recommendations.
 - Development of a basic NLP model for semantic query analysis.
 - Integration of the database with a catalog of locations and their characteristics.
 - A minimal frontend interface for testing the service.
#### OUT
 - Construct optimal roadmap for travel 
 - Buy tickets in app
 - Integration with taxi
 - Consideration of weather conditions


## Tech-stack

| Field                            | Frameworks                                      |
|----------------------------------|-------------------------------------------------|
| Backend                          | Python (FastAPI), PostgreSQL                    |
| Frontend                         | TypeScript, React                               |
| NLP                              | spaCy + NLTK, Hugging Face Transformers         |
| Full-text Search                 | Elasticsearch                                   |
| Vector search                    | Faiss                                           |
| Deep learn and  Learning-to-Rank | PyTorch + PyTorch Lightning, LightGBM / XGBoost |
| RAG                              | LangChain + OpenAI / Hugging Face               |


# Weekly commitments

## Individual contribution of each participant

Emil Goryachikh created a shared group in the Telegram messenger. He organized a joint meeting for which everyone prepared their own project idea. After a long brainstorming session, we chose the best idea, assigned responsibilities, and selected the tech stacks that suited us for implementation. We also agreed to hold periodic meetings to improve our teamwork. To ensure smooth collaboration, we adopted the Scrum methodology. Saidaziz Kadirov took on preparing the implementation plan based on our methodology and will present it at the next meeting. Vladislav Galkin (front-end developer) created a private repository where he laid out the framework for the front end and the overall architecture of our project. Emil Goryachikh and Vladislav Galkin wrote the course report, and then everyone proceeded to carry out their assigned duties.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [ ] In working condition.
- [ ] Run via docker-compose (or another alternative described in the `README.md`).