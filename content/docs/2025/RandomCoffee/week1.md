---
title: "Week #1"
---

# Week #1

## Project description

### Project name: *Random Coffee*

**Code repository**: [GitHub](https://github.com/IU-Capstone-Project-2025/RandomCoffee)

#### Problem statement
In many companies, universities, and other organizations, individuals often interact mostly with people in their immediate teams, departments, or circles. As a result, there are limited opportunities for informal interaction across different groups. This lack of spontaneous connection means that people:  
	•	Miss out on sharing knowledge or best practices across teams or disciplines.  
	•	Find it harder to build relationships outside of their usual networks.  
	•	May feel isolated or disconnected from the larger community.  
	•	Are less likely to collaborate across functions, which can reduce innovation and problem-solving potential.  

While formal meetings and events exist, they rarely create the kind of casual, serendipitous encounters where meaningful conversations and relationships begin. These informal connections are often where people exchange experiences, find mentors or discover collaboration opportunities.

#### Project description
Random Coffee is a Telegram Mini App designed to foster meaningful connections through casual meetups. Users can register, set their preferences, and choose relevant tags suggested by our machine learning algorithm. The tags reflect their interests or professional background. Once a week, the system matches users with other people who share similar tags and suggests setting up a meeting.

The bot is intended for deployment within organizations to promote networking, experience sharing, and informal communication among members. By facilitating regular low-pressure interactions, Random Coffee helps build stronger internal networks and promotes a culture of collaboration and openness.


### **Team Members**

| Team Member                             | Telegram Alias   | Email Address                    | Track                      | Responsibilities   |
|-----------------------------------------|------------------|----------------------------------|----------------------------|--------------------|
| Anastasia Mitutneva (Lead)              | @Mituttta        | a.mitiutneva@innopolis.university| Project Manager            | Assigning tasks, monitoring project progress against the plan, reviewing code, analyzing accomplished work and performing reports weekly |
| Maksim Al Dandan                        | @almax_good      | m.aldandan@innopolis.university  | Backend                    | Interaction with Telegram API, user profile management, matchmaking logic  |
| Aleksandr Andreev                       | @iamkoldun       | al.andreev@innopolis.university  | Frontend                   | Telegram Mini App: user settings page, matchmaking pages |
| Ivan Ilyichev                           | @ralpem          | i.ilyichev@innopolis.university  | ML                         | A model that processes text and determines appropriate tags based on context |
| Rail Sabirov                            | @raulrail        | rai.sabirov@innopolis.university | ML                         | A model that processes text and determines appropriate tags based on context |



## Brainstorming

### Ideas during brainstorming
1. A Telegram bot that matches people for informal coffee meetings based on their interests and availability
2. A Telegram Bot for Memorizing Foreign Words (with Context & Synonyms)
3. Baam attendance reverse-engineering
4. A Telegram bot that sends daily weather updates and clothing recommendations


### Brief market research / problem validation
**1. Random Coffee**

Problem Validation:  
	•	Loneliness and networking barriers: Many remote workers, students, and digital nomads express difficulty meeting like-minded people casually.  
	•	Current options are inefficient: Platforms like Meetup or Bumble Bizz exist, but they’re either too formal, slow-moving, or socially awkward for spontaneous, low-pressure meetings.  
	•	Telegram’s rise as a platform: Telegram’s popularity for community building (especially in Europe, Asia, and tech-savvy regions) makes it a fitting medium for a low-friction, chat-based matching tool.  

Comparable services:  
	•	Lunchclub (more professional, email-based)  
	•	Bumble Bizz (more dating-app-like)  
	•	Slack/Discord coffee bots (usually confined to teams, not public spaces)  


**2. Telegram Bot for Memorizing Foreign Words (with Context & Synonyms)**

Problem Validation:  
	•	Language learners struggle with retention: Especially vocabulary and correct contextual usage.  
	•	Existing tools lack engagement or context: Apps like Anki and Duolingo are widely used, but flashcards can feel repetitive, and Duolingo doesn’t offer enough personalized contextual learning.  
	•	High demand for flexible learning: Language learners want portable, on-demand tools integrated into daily life (like messaging platforms).  

Comparable services:  
	•	Anki (manual, static)   
	•	Quizlet (less personalized)  
	•	Lang Practice bot (few focus on word usage in context with synonyms)  

After analyzing both ideas, we chose to implement *Random Coffee* because it addresses a more pressing need for social connection in remote and hybrid work environments, while offering a simpler MVP scope with clear value proposition for organizations and individuals alike.


## Basic requirements

**Target Users and Their Primary Needs**  
	•	*Remote workers*: Want informal social contact and professional networking outside structured settings.  
	•	*Students*: Especially those new to a university, looking to expand their social circle in a casual, low-pressure way.  
	•	*Digital nomads & expats*: Seeking local connections in a new city or country.  
	•	*Employees in large organizations*: Interested in cross-team informal interaction, especially in remote-first companies.  

⸻

**User Stories**  
	•	As a remote worker, I want to be matched with someone for a casual chat once a week based on my interests and schedule, so I can feel less isolated.  
	•	As a new student, I want to meet people outside my classes who share similar hobbies, so I can make friends easily.  
	•	As an HR manager, I want a tool that encourages informal connections between employees from different teams, to improve company culture.  
    •   As a team lead, I want to encourage my team members to network across the organization, so they can bring fresh perspectives and ideas to our projects.  
    •   As a new employee, I want to be automatically matched with experienced colleagues, so I can learn about the organization's culture and practices.  
    •   As a user, I want to see my match's professional background and interests before meeting, so I can prepare relevant topics for discussion.  
	•	As a Telegram user, I want to opt in and out of weekly matching easily, so I stay in control of my social time.

⸻

**Initial Scope (What's IN for the MVP)**  
	Simple Telegram Mini App with the following features:  
	•	User registration (name, age, description, tags)  
    •	Tags are chosen from tag database  
    •	Matchmaking algorithm based on tags using Evolutionary Algorithms  
    •	Weekly sending of messages with an offer to meet with a suitable user  

**What's OUT for the MVP but IN for the Final version**  
	•	User can add custom tags, that possibly will be validated by ML algorithm  
	•	User chooses each week whether he participates or not.  
	•	User chooses his goal for the week: "Share experience", "Gain knowledge", "Just chat"  
	•	User chooses whether to find partner with similar or different interests  
	•	Edit page for the user  
	•	Matchmaking history is stored, so the user does not meet the same person twice  
	•	Tags autocompletion ("Jav" -> "Java", "JavaScript")  

**Possible, but not guaranteed features**  
	•	The rating system (user that has better rating gets better match)  
	•	Tags suggestion (If the user has selected "Spring Boot" tag -> "Backend", "Java" tags will be suggested by ML)  
	•	Customized user profile fields for different types of organizations (for example, course/track for the universities)  
	•	User can "Rematch" - algorithm will find another match for this week  
	•	User chooses the priority topic for this week  
    
## Tech-stack

**Backend:** Java + Spring + PostgreSQL + Kafka + OpenAPI + MSA - robust, scalable server-side framework  
**Frontend:** TypeScript + React + Telegram Mini Apps API - type-safe UI with Telegram integration for convinient user registration  
**ML(under discussion):** Python + data processing libs (numpy & pandas) + standard NLP libs (nltk) - industry standard for machine learning tasks  


# Weekly commitments

## Individual contribution of each participant
The whole team has discussed project ideas and chosen one. We have defined approximately what the MVP will look like.  

The work done by each team member:  
1. **Anastasia Mitiutneva**: create an idea of the project, created basic architecture of the project, created the repository, conducted market research (see Brainstorming section), assigned first tasks to each team member, managed all team flows (git workflow, kanban boards, etc.)     
[Pull request 1](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/7)  
[Pull request 2](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/8) 
2. **Maksim Al Dandan**: created initial version of backend project with a basic boilerplate structure and a Dockerfile  
[Pull request 1](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/1)  
[Pull request 2](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/3)  
3. **Aleksandr Andreev**: created initial version of frontend project with a basic boilerplate structure and a Dockerfile  
[Pull request 1](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/4)  
[Pull request 2](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/5)  
4. **Ivan Ilyichev**: created initial version of ML project with a basic boilerplate structure and a Dockerfile  
[Pull Request](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/2)
5. **Rail Sabirov**: conducted research by reading machine learning articles relevant to our project:  
•	[Sun, Y., Qiu, H., Zheng, Y., Wang, Z., & Zhang, C. (2020). SIFRank: A New Baseline for Unsupervised Keyphrase Extraction Based on Pre-trained Language Model.](https://www.sci-hub.ru/10.1109/access.2020.2965087)  
•	[Applying Transformer-based Text Summarization for Keyphrase Generation by Anna Glazkova and Dmitry Morozov](https://arxiv.org/pdf/2209.03791)  
•	[KeyBert (embeddings based finding)](https://github.com/MaartenGr/KeyBERT)  
•	[Synonyms and typos handling](https://rapidfuzz.github.io/RapidFuzz/)  
•	Efficient Estimation of Word Representations in Vector Space by Mikolov et al.  
•	[Tokenization](https://huggingface.co/docs/transformers/tokenizer_summary)  
•	Github papers from documentations/Researches/HF documentation


## Confirmation of the code's operability

We confirm that the code in the main branch:  
✅ In working condition.  
✅ Run via docker-compose.  

# Plan for the next week
### Backend:  
Implement a Telegram bot microservice that will handle all Telegram bot messages and send scheduled messages to users with reminders.  
Implement API contract for frontend interaction  
### Frontend:  
Implement a basic profile creation page with a mock client for the backend.  
### ML:  
Design of a tag suggesting algorithm  
Research appropriate articles   
Start gathering and preparing a data set.  